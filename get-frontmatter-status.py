# get-frontmatter-status.py
## This script is designed to read all of the .md files in a directory tree, 
## and populate a single .csv file with the contents/status of all the frontmatter found 
## in those Markdown files.

import os
import glob
from datetime import datetime

from queue import Empty
from typing import Dict
import frontmatter
import csv

filtered = dict()
fields = {
  "title": "title",
  "articleIndex": "articleIndex",
  "index": "index",
  "description": "description",
  "date": "date",
  "draft": "draft",
  "contributors": "contributors",
  "role": "contributor.role",
  "name": "contributor.name",
  "headshot": "contributor.headshot",
  "caption": "contributor.caption",
  "bio": "contributor.bio",
  "articletype": "articletype",
  "azure_dir": "azure_dir",
  "filename": "header_image.filename",
  "alt_text": "header_image.alt_text",
  "tags": "tags",
  "byline": "byline"
}

# file_pattern = r"^\d{4}-(spring|fall)\.md$"
# year_term_pattern = r"(\d{4})-(spring|fall)"
# image_pattern = r".{3}\(.+/image/(.+)\)$"
# header_pattern = r"^Rootstalk \| .+$"
# replacement = '{{% figure_azure pid="xPIDx" caption="" %}}'

# frontmatter = '---\n' \
#               'title: \n' \
#               'articleIndex: \n' \
#               'index: \n' \
#               'description: \n' \
#               'date: \n' \
#               'draft: false \n' \
#               'contributors: \n' \
#               '  - role: author \n' \
#               '    name: \n' \
#               '    headshot: \n' \
#               '    caption: \n' \
#               '    bio: " "\n' \
#               'articletype: \n' \
#               'azure_dir: \n' \
#               'header_image: \n' \
#               '  filename: \n' \
#               '  alt_text: \n' \
#               'tags: [" "," "] \n' \
#               "---\n"

# # Open the year-term.html file and run the "markdownify" package
# #   (https://github.com/matthewwithanm/python-markdownify) on it.
# # This produces a new .md file with the same name.
# def rootstalk_markdownify(filepath):
#    with open(filepath, "r") as html:
#      html_string = html.read()
#      # Open a new .md file to receive translated text
#      (path, filename) = os.path.split(filepath)
#      (name, ext) = filename.split('.')
#      new_file = '{}/{}.{}'.format(path, name, 'md')
#      logging.info("Creating new .md file: " + new_file)
#      with open(new_file, "w") as mdf:
#        markdown_text = md(html_string)
#        print(markdown_text, file=mdf)


# def rootstalk_azure_media(year, term, filepath):
#   # ytmd = "{}-{}.md".format(year, term, year, term)
#   ytmd = filepath.replace(".html", ".md")

#   # Open the issue's year-term.md file...
#   logging.info("Attempting to open markdown file: " + ytmd)
#   with open(ytmd, "r") as issue_md:
#     # azure_path = "{}-{}-azure.md".format(year, term)
#     azure_path = filepath.replace(".html", "-azure.md")
  
#     logging.info("Creating new Azure .md file at '{}'.".format(azure_path))

#     # Open and write a new year-term-azure.md file...
#     with open(azure_path, "w") as azure_md:
#       lines = issue_md.readlines()

#       # Clean-up...
#       # - translate any year-term-web-resources folder references to new Azure format.
#       # - remove any line that entirely matches the pattern:  ^.+ | .+$

#       for line in lines:
#         match_image = re.match(image_pattern, line)
#         match_header = re.match(header_pattern, line)
#         if match_image:  # transform image references
#           new_line = replacement.replace("xPIDx", match_image.group(1))
#           print(new_line, end='\n', file=azure_md)
#         elif not match_header:  # skip page headers
#           print(line, file=azure_md)  # write the line out

#   # Now, remove all repeated blank lines (reduces whitespace)
#   with open(azure_path, "r+") as azure_md:
#     contents = azure_md.read( )
#     # stripped = re.sub(r'^$\n', '', contents, flags=re.MULTILINE)
#     stripped = re.sub(r'\n\s*\n', '\n\n', contents)
#     azure_md.seek(0)  # rewind the file
#     azure_md.writelines(stripped)  # write the stripped version


# def rootstalk_make_articles(year, term, filepath):
#   ytyml = filepath.replace(".html", ".yml")
  
#   # Look for a year-term.yml file...
#   if not os.path.exists(ytyml):
#     logging.error("ERROR: No {} YAML file found! You need to create this file if you wish to proceed with the {}-{} issue!".format(ytyml, year, term))
#   else:
#     logging.info("Processing the {} file.".format(ytyml))
        
#     # Check for corresponding -azure.md file in the same directory
#     azure_md = filepath.replace(".html", "-azure.md") 
#     if not os.path.exists(azure_md):
#       logging.error(
#             "ERROR: No Azure-formatted markdown file '{}' found! You may need to run the 'rootstalk_azure_media' scripts before proceeding.".format(
#               azure_md))
        
#     # Everything is in place, read the year-term.yml file...
#     with open(ytyml, "r") as stream:
#       try:
#         yml = yaml.safe_load(stream)
#       except yaml.YAMLError as exc:
#         sys.exit(exc)
      
#       for key, value in yml.items():
#         logging.info("{}: {}".format(key, value))

#       aIndex = 0

#       # Read each article name/index and create a new article_index.md file if one does not already exist
#       for name in yml["articles"]:
#         web_resources = '-web-resources/{}.md'.format(name)
#         md_path = filepath.replace(".html", web_resources)
#         logging.info("Creating article markdown file '{}'...".format(md_path))
#         if os.path.exists(md_path):
#           logging.warning(
#                 "WARNING: Markdown file '{}' already exists and will not be replaced! Be sure to move or remove the existing file if you wish to generate a new copy.".format(
#                   md_path))
#         else:
#           with open(azure_md, "r") as md:
#             issue_md_content = md.read()
                
#             # Customize the front matter before inserting it...
#             fm = frontmatter.replace("index: ", "index: {}".format(name))
#             fm = fm.replace("articleIndex: ", "articleIndex: {}".format(aIndex))
#             fm = fm.replace("azure_dir: ", "azure_dir: rootstalk-{}-{}".format(year, term))
#             fm = fm.replace("date: ", "date: '{}'".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
            
#             aIndex += 1
            
#             # Write the front matter and content to the article.md file
#             with open(md_path, "w") as article_md:
#               print(fm, file=article_md)
#               print(issue_md_content, file=article_md)


# Main...
if __name__ == '__main__':
  
  # Open the .csv file for output
  with open("frontmatter-status.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields.values())
    writer.writeheader()

    # Iterate over the working directory tree + subdirectories for all {issue}/{article}.md files
    # Using '*.md' pattern recursively
    for filepath in glob.glob('**/*.md'):
    
      # Looking for article.md files...
      (path, filename) = os.path.split(filepath)
      article = frontmatter.load(filepath)
      for field in fields:
        if field not in article.metadata.keys():
          newvalue = ""
        else:
          newvalue = article.metadata[field]
          if type(newvalue) is list:
            print(f"Field '{field}' for file '{filepath}' is a list, joining with commas.")
            newvalue = ",".join(newvalue)
            
          filtered[fields[field]] = newvalue
      writer.writerow(filtered)


# See VSCode Python setup at https://blog.summittdweller.com/posts/2022/09/proper-python/


## from https://git.kucharczyk.xyz/lukas/frontmatter-to-csv/src/branch/main/frontmatter_to_csv/convert.py

# """
# Convert YAML front matter to CSV
# """

# from queue import Empty
# from typing import Dict
# from durations import Duration
# import os
# import frontmatter
# import csv
# import click

# filtered = dict()
# fields = {
#     "name": "Name",
#     "playtime": "Playtime",
#     "platform": "Platform",
#     "infinite": "Infinite",
#     "finished": "Finished",
#     "refunded": "Refunded",
#     "dropped": "Dropped",
#     "date-released": "DateReleased",
#     "date-purchased": "DatePurchased",
#     "date-started": "DateStarted",
#     "date-finished": "DateFinished",
# }


# @click.command()
# @click.option(
#     "--input-directory",
#     "-i",
#     help="Directory with files that have frontmatter.",
#     prompt="Input directory",
# )
# @click.option(
#     "--output-file",
#     "-o",
#     default="output.csv",
#     help="The output CSV file.",
# )
# def convert(input_directory, output_file):
#     if not os.path.isdir(input_directory):
#         exit(f"The directory {input_directory} does not exist!")
#     with open(output_file, "w", newline="") as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fields.values())
#         writer.writeheader()
#         for filename in os.listdir(input_directory):
#             f = os.path.join(input_directory, filename)

#             if os.path.isfile(f):
#                 article = frontmatter.load(f)
#                 for field in fields:
#                     if field not in article.metadata.keys():
#                         newvalue = ""
#                     else:
#                         newvalue = article.metadata[field]
#                     if field == "playtime" and newvalue != 0 and newvalue is not None:
#                         if type(newvalue) is dict:
#                             totalvalue = 0
#                             for key in newvalue:
#                                 timevalue = Duration(newvalue[key]).to_hours()
#                                 totalvalue += timevalue
#                             newvalue = totalvalue
#                         else:
#                             timevalue = Duration(newvalue)
#                             newvalue = timevalue.to_hours()
#                     if type(newvalue) is list:
#                         print(
#                             f"Field '{field}' for file '{filename}' is a list, joining with commas."
#                         )
#                         newvalue = ",".join(newvalue)
#                     filtered[fields[field]] = newvalue

#                 writer.writerow(filtered)


# if __name__ == "__main__":
#     convert()
