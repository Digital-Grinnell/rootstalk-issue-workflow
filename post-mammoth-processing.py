# post-mammoth-processing.py... derived from indd-to-html.py

import os
import sys
import re
import yaml
import logging
import glob
from datetime import datetime
from markdownify import markdownify as md
from bs4 import BeautifulSoup

converted_pattern = r"(\d{4})-(spring|fall)/(.+)/converted/(.+)\.html"
file_pattern = r"^\d{4}-(spring|fall)\.md$"
year_term_pattern = r"(\d{4})-(spring|fall)"
image_pattern = r".{3}\(.+/image/(.+)\)$"
header_pattern = r"^Rootstalk \| .+$"
replacement = '{{% figure_azure pid="xPIDx" caption="" %}}'

frontmatter = '---\n' \
              'index: \n' \
              'azure_dir: \n' \
              'articleIndex: \n' \
              'title: \n' \
              'subtitle: \n' \
              'byline: \n' \
              'byline2: \n' \
              'categories: \n' \
              '  - category\n'  \
              'tags: \n' \
              '  - \n'  \
              'header_image: \n' \
              '  filename: \n' \
              '  alt_text: \n' \
              'contributors: \n' \
              '  - role: author \n' \
              '    name: \n' \
              '    headshot: \n' \
              '    caption: \n' \
              '    bio: " "\n' \
              'description: \n' \
              'date: \n' \
              'draft: false \n' \
              'no_leaf_bug: false\n' \
              "---\n"


# Parse the Mammoth-converted HTML to find key/frontmatter elements from our
#    rootstalk-custom-style.map file.  Substitute them into `frontmatter`.
# See https://www.geeksforgeeks.org/find-tags-by-css-class-using-beautifulsoup/ for guidance.
# -----------------------------------------------------------------------------
def parse_post_mammoth_converted_html(html_file, fm):
	
  # Parse the HTML content
	soup = BeautifulSoup(html_file, "html.parser")
	
  # Find key tags by CSS class
	title = soup.find("h1", class_= "Primary-Title")
	byline = soup.find("p", class_= "Byline")

  article_type = soup.find("p", class_= "Article-Type")
  hero_image = soup.find("img", class_= "Hero-Image")

  # Drop found elements into the frontmatter (fm)...
  if title:
    fm = fm.replace("title: ", "title: {}".format(title))
  
  if byline:
    fm = fm.replace("byline: ", "byline: {}".format(byline))

  if article_type:
    fm = fm.replace("- category", "- {}".format(article_type))
    
  if hero_image:
    fm = fm.replace("  filename: ", "  filename: {}".format(hero_image))


# Open the "converted" article.html file and make our Rootstalk-specific additions
# to a new .md copy of the HTML.
#
# This produces a new .md file with the same name.
# ------------------------------------------------------------------------------
def rootstalk_markdownify(filepath):
  
  with open(filepath, "r") as html:
    html_string = html.read()
     
    # Open a new .md file to receive translated text
    (path, filename) = os.path.split(filepath)
    (name, ext) = filename.split('.')
    new_file = '{}/{}.{}'.format(path, name, 'md')
    logging.info("Creating new .md file: " + new_file)

    # Customize the front matter before inserting it...
    fm = frontmatter.replace("index: ", "index: {}".format(name))
    fm = fm.replace("articleIndex: ", "articleIndex: {}".format(aIndex))
    fm = fm.replace("azure_dir: ", "azure_dir: rootstalk-{}-{}".format(year, term))
    fm = fm.replace("date: ", "date: '{}'".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S')))

    # Parse the Mammoth-converted HTML to make additional substitutions into the frontmatter
    parsed = parse_post_mammoth_converted_html(filepath, fm)

    # Write the front matter and content to the article.md file
    with open(new_file, "w") as mdf:
      aIndex += 1
            
      #       with open(md_path, "w") as article_md:
      #         print(fm, file=article_md)
      #         print(issue_md_content, file=article_md)
      #  markdown_text = md(html_string)
      #  print(markdown_text, file=mdf)


def rootstalk_azure_media(year, term, filepath):
  # ytmd = "{}-{}.md".format(year, term, year, term)
  ytmd = filepath.replace(".html", ".md")

  # Open the issue's year-term.md file...
  logging.info("Attempting to open markdown file: " + ytmd)
  with open(ytmd, "r") as issue_md:
    # azure_path = "{}-{}-azure.md".format(year, term)
    azure_path = filepath.replace(".html", "-azure.md")
  
    logging.info("Creating new Azure .md file at '{}'.".format(azure_path))

    # Open and write a new year-term-azure.md file...
    with open(azure_path, "w") as azure_md:
      lines = issue_md.readlines()

      # Clean-up...
      # - translate any year-term-web-resources folder references to new Azure format.
      # - remove any line that entirely matches the pattern:  ^.+ | .+$

      for line in lines:
        match_image = re.match(image_pattern, line)
        match_header = re.match(header_pattern, line)
        if match_image:  # transform image references
          new_line = replacement.replace("xPIDx", match_image.group(1))
          print(new_line, end='\n', file=azure_md)
        elif not match_header:  # skip page headers
          print(line, file=azure_md)  # write the line out

  # Now, remove all repeated blank lines (reduces whitespace)
  with open(azure_path, "r+") as azure_md:
    contents = azure_md.read( )
    # stripped = re.sub(r'^$\n', '', contents, flags=re.MULTILINE)
    stripped = re.sub(r'\n\s*\n', '\n\n', contents)
    azure_md.seek(0)  # rewind the file
    azure_md.writelines(stripped)  # write the stripped version


def rootstalk_make_articles(year, term, filepath):
  ytyml = filepath.replace(".html", ".yml")
  
  # Look for a year-term.yml file...
  if not os.path.exists(ytyml):
    logging.error("ERROR: No {} YAML file found! You need to create this file if you wish to proceed with the {}-{} issue!".format(ytyml, year, term))
  else:
    logging.info("Processing the {} file.".format(ytyml))
        
    # Check for corresponding -azure.md file in the same directory
    azure_md = filepath.replace(".html", "-azure.md") 
    if not os.path.exists(azure_md):
      logging.error(
            "ERROR: No Azure-formatted markdown file '{}' found! You may need to run the 'rootstalk_azure_media' scripts before proceeding.".format(
              azure_md))
        
    # Everything is in place, read the year-term.yml file...
    with open(ytyml, "r") as stream:
      try:
        yml = yaml.safe_load(stream)
      except yaml.YAMLError as exc:
        sys.exit(exc)
      
      for key, value in yml.items():
        logging.info("{}: {}".format(key, value))

      aIndex = 0

      # Read each article name/index and create a new article_index.md file if one does not already exist
      for name in yml["articles"]:
        web_resources = '-web-resources/{}.md'.format(name)
        md_path = filepath.replace(".html", web_resources)
        logging.info("Creating article markdown file '{}'...".format(md_path))
        if os.path.exists(md_path):
          logging.warning(
                "WARNING: Markdown file '{}' already exists and will not be replaced! Be sure to move or remove the existing file if you wish to generate a new copy.".format(
                  md_path))
        else:
          with open(azure_md, "r") as md:
            issue_md_content = md.read()
                
            # Customize the front matter before inserting it...
            fm = frontmatter.replace("index: ", "index: {}".format(name))
            fm = fm.replace("articleIndex: ", "articleIndex: {}".format(aIndex))
            fm = fm.replace("azure_dir: ", "azure_dir: rootstalk-{}-{}".format(year, term))
            fm = fm.replace("date: ", "date: '{}'".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
            
            aIndex += 1
            
            # Write the front matter and content to the article.md file
            with open(md_path, "w") as article_md:
              print(fm, file=article_md)
              print(issue_md_content, file=article_md)


# Main...
if __name__ == '__main__':
  
  # Iterate over the working directory tree + subdirectories for article/converted sub-directories and '*.html' files within.
  for filepath in glob.glob('**/**/converted/*.html'):
    
      # Looking for "converted" article.html files...
      (path, filename) = os.path.split(filepath)
      match = re.match(converted_pattern, filepath)
      
      if match: 
        year = match.group(1)
        term = match.group(2)
        index = match.group(3)
        html_name = match.group(4)

        issue = "{}-{}".format(year, term)
        logfile = filepath.replace(".html", ".log")
        logging.basicConfig(filename=logfile, encoding='utf-8', level=logging.DEBUG)
        logging.info("Found .html file: " + filepath)
  
        rootstalk_markdownify(filepath)
        rootstalk_azure_media(year, term, filepath)
        rootstalk_make_articles(year, term, filepath)

      break  # stop search at first level

# See VSCode Python setup at https://blog.summittdweller.com/posts/2022/09/proper-python/