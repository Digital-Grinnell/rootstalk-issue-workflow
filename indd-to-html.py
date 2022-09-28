import os
import sys
import re
import yaml
import logging
from datetime import datetime
from markdownify import markdownify as md

file_pattern = r"^\d{4}-(spring|fall)\.md$"
year_term_pattern = r"(\d{4})-(spring|fall)"
image_pattern = r".{3}\(.+/image/(.+)\)$"
header_pattern = r"^.+ | .+$"
replacement = '{{% figure_azure pid="xPIDx" caption="" %}}'

frontmatter = '---\n' \
              'title: \n' \
              'index: \n' \
              'description: \n' \
              'date: \n' \
              'draft: false \n' \
              'authors: \n' \
              '  - name: \n' \
              '    headshot: \n' \
              '    bio: " "\n' \
              '  - name: \n' \
              '    headshot: \n' \
              '    bio: " "\n' \
              'articletype: \n' \
              'tags: [" "," "] \n' \
              'azure_dir: \n' \
              "azure_header: \n" \
              "---\n"


# Open the year-term.html file and run the "markdownify" package
#   (https://github.com/matthewwithanm/python-markdownify) on it.
# This produces a new .md file with the same name.
def rootstalk_markdownify(filepath):
   with open(filepath, "r") as html:
     html_string = html.read()
     # Open a new .md file to receive translated text
     (path, filename) = os.path.split(filepath)
     (name, ext) = filename.split('.')
     new_file = '{}/{}.{}'.format(path, name, 'md')
     logging.info("Creating new .md file: " + new_file)
     with open(new_file, "w") as mdf:
       markdown_text = md(html_string)
       print(markdown_text, file=mdf)


def rootstalk_azure_media(year, term, filepath):
  ytmd = "{}-{}.md".format(year, term)

  # Open the issue's year-term.md file...
  logging.info("Attempting to open markdown file: " + ytmd)
  with open(ytmd, "r") as issue_md:
    azure_path = "{}-{}-azure.md".format(year, term)
  
    # Open and read the issue's year-term.md file...
    with open(filepath, "r") as issue_md:
      logging.info("Creating new Azure .md file at '{}'.".format(azure_path))
      # Open and write a new year-term-azure.md file...
      with open(azure_path, "w") as azure_md:
        lines = issue_md.readlines()

        # Clean-up...
        # - translate any year-term-web-resources folder references to new Azure format.
        # - remove all repeated blank lines (reduces whitespace)
        # - remove any line that entirely matches the pattern:  ^.+ | .+$

        previous_blank = False

        for line in lines:
          match_image = re.match(image_pattern, line)
          match_header = re.match(header_pattern, line)
          if match_image:  # transform image references
            new_line = replacement.replace("xPIDx", match_image.group(1))
            print(new_line, end='\n', file=azure_md)
            previous_blank = False
          elif match_header:  # skip page headers
            previous_blank = True
          elif previous_blank and len(line) == 0:  # skip redundant blank lines
            previous_blank = True
          else:
            print(line, file=azure_md)  # write the line out
            if len(line) == 0:
              previous_blank = True
            else:
              previous_blank = False


def rootstalk_make_articles(year, term):
  ytyml = "{}-{}.yml".format(year, term)
  
  # Look for a year-term.yml file...
  if not os.path.exists(ytyml):
    logging.error("ERROR: No {} YAML file found! You need to create this file if you wish to proceed with the {}-{} issue!".format(ytyml, year, term))
  else:
    logging.info("Processing the {} file.".format(ytyml))
        
    # Check for corresponding .html and -azure.md files in the same directory
    html_file = '{}-{}{}'.format(year, term, '.html')
    azure_md = '{}-{}{}'.format(year, term, '-azure.md')
    if not os.path.exists(html_file):
      logging.error(
            "ERROR: No HTML file '{}' found! You may need to export HTML from InDesign before proceeding.".format(
              html_file))
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
          
      # Read each article name/index and create a new article_index.md file if one does not already exist
      for name in yml["articles"]:
        md_path = '{}-{}-web-resources/{}-{}-{}.md'.format(year, term, year, term, name)
        logging.info("Creating article markdown file '{}'...".format(md_path))
        if os.path.exists(md_path):
          logging.warning(
                "WARNING: Markdown file '{}' already exists and will not be replaced! Be sure to move or remove the existing file if you wish to generate a new copy.".format(
                  md_path))
        else:
          with open(azure_md, "r") as md:
            issue_md_content = md.read()
                
            # Customize the front matter before inserting it...
            fm = frontmatter.replace("index: ", "index: {}".format(name)).replace("azure_dir: ",
                                                                                      "azure_dir: rootstalk-{}-{}".format(
                                                                                        year, term)).replace("date: ",
                                                                                                             "date: '{}'".format(
                                                                                                               datetime.now().strftime(
                                                                                                                 '%d/%m/%Y %H:%M:%S')))
            # Write the front matter and content to the article.md file
            with open(md_path, "w") as article_md:
              print(fm, file=article_md)
              print(issue_md_content, file=article_md)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  
  # Iterate over the working directory tree subdirectories
  for subdir, dirs, files in os.walk(r'.'):
    for filename in files:
      filepath = subdir + os.sep + filename
      # Looking for year-term.html files...
      (path, filename) = os.path.split(filepath)
      match = re.match(year_term_pattern, filename)
      if match and filename.endswith(".html"):
        year = match.group(0)
        term = match.group(1)
        issue = "{}-{}".format(year, term)
        logging.basicConfig(filename=issue+".log", encoding='utf-8', level=logging.DEBUG)
        logging.info("Found .html file: " + filepath)
  
        rootstalk_markdownify(filepath)
        rootstalk_azure_media(year, term)
        rootstalk_make_articles(year, term)

      break  # stop search at first level

# See PyCharm help at https://www.jetbrains.com/help/pycharm/