# digital-first-workflow.py
# ----------------------------------------------------------------------------------
# This is a Streamlit (https://streamlit.io/) app that leverages
# 'mammoth' (the Python version from https://github.com/mwilliamson/python-mammoth)
# to transform a single "article" presented as an MS Word .docx file, one presumably 
# formatted with Rootstalk styles, into a Markdown (.md) file suitable for clean-up 
# and subsequent publication in the digital edition of Rootstalk 
# (https://rootstalk.grinnell.edu).
# 
# See VSCode Python setup at https://blog.summittdweller.com/posts/2022/09/proper-python/

import streamlit as st
import os
import re
import logging
import glob
from datetime import datetime
from markdownify import markdownify as md
from bs4 import BeautifulSoup
import tempfile, shutil
from azure.storage.blob import BlobServiceClient
import subprocess, sys


# Define some globals -------------------------------------------------

converted_pattern = r"(\d{4})-(spring|fall)/(.+)/converted/(.+)\.html"
file_pattern = r"^\d{4}-(spring|fall)\.md$"
year_term_pattern = r"(\d{4})-(spring|fall)"
image_pattern = r".{3}\(.+/image/(.+)\)$"
reference_pattern = r"\[(\d+)]"
endnote_pattern = r"endnote-(\d+)"

fm_template = '---\n' \
              'index: \n' \
              'azure_dir: \n' \
              'articleIndex: \n' \
              '_title: \n' \
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

default_path = '/Users/mcfatem/Library/CloudStorage/OneDrive-GrinnellCollege/Digital-Versions'

# run_mammoth( ) -------------------------------------------------
# Prompt the user to select a .docx for processing and hand it off to a `mammoth` subprocess.

def run_mammoth( ): 

    # Prompt the user to enter the path to their LOCAL sync of the 'Digital-Versions' directory (or accept the default)
    local_path = st.text_input("Path to your LOCAL/sync `Digital-Versions` directory", default_path)
    
    # Glob all the .docx files recursively from path
    files = glob.glob(f'{local_path}/**/*.docx', recursive=True) 
    
    if not files:
        st.error(f"No `.docx` files could be found in `{local_path}`!")
        return False

    filenames = [ ]
    for file in files: 
        no_path = file.removeprefix(local_path)
        filenames.append(no_path)
    
    # Now the form...
    with st.form("select_docx"):
        selected = st.selectbox('Select a Word Document', filenames)[1:]   # remove leading slash or os.path.join will FAIL
    
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f'You selected {selected}')
            selected_path = os.path.join(local_path, selected)

            # OK, a .docx has been selected, run 'mammoth'
            dir = os.path.dirname(selected_path)
            doc = os.path.basename(selected_path)

            # Report progress and mkdir
            st.write(f"Creating the `{dir}/converted` subdirectory if it does not already exist.")
            subprocess.run(f"mkdir -p '{dir}/converted'", shell=True, executable="/bin/bash")
            st.success('Done!')

            # Report progress and run 'mammoth'
            html_name = doc[:-5] + ".html"
            html_path = os.path.join(dir, "converted", html_name)
            st.write(f"Running **mammoth** on `{dir}/{doc}` to create `{html_path}`.")

            # With a spinner widget...
            with st.spinner("**Mammoth**'s are not quick, wait for it..."):
                subprocess.run(f"mammoth '{dir}/{doc}' --output-dir='{dir}/converted' --style-map=rootstalk-custom-style.map", shell=True, executable="/bin/bash")
            st.success('Done!')

            return html_path
        
    return False


# main -----------------------------------------------------------------
if __name__ == '__main__':

    # Initialize our Streamlit session_state keys
    if 'html_path' not in st.session_state:
        st.session_state.html_path = False

    # Explain the OneDrive prep required before running this app...
    md = "This app assumes that you have already COPIED the contents of Professor Baechtel's OneDrive, specifically the `Rootstalk, Spring 2024` : `Digital-Versions` subdirectory, to YOUR OWN OneDrive and synchronized that copy with your workstation.  To do this open the appropriate OneDrive, navigate to YOUR aforementioned subdirectory and click on the `Sync` option.  You may be prompted for your Grinnell login credentials before the directory is sync'd to your workstation.  On a Mac the sync'd local folder is likely to be `~/Library/CloudStorage/OneDrive-GrinnellCollege/Digital-Versions`, the default path in this app."
    st.write(md)

    # Select a .docx file for processing, prep for and run a 'mammoth' command to convert the .docx 
    # into an HTML document and corresponding media
    st.session_state.html_path = run_mammoth( )

    # Initialize some globals...
    aIndex = 0
    frontmatter = fm_template
    open_shortcode = "{{%"
    close_shortcode = "%}}"

    # Run a 'mammoth' command to convert the .docx file into an HTML document and media
    # if st.session_state.file_path:
    #     run_mammoth(st.session_state.file_path)

    # # Retrieve the Azure connection string for use with the application. The storage
    # # connection string is stored in an environment variable on the machine
    # # running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment 
    # # variable is created after the application is launched in a console or with Visual Studio,
    # # the shell or application needs to be closed and reloaded to take the
    # # environment variable into account.

    # connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    # # Create the BlobServiceClient object
    # blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  
    # # Iterate over the working directory tree + subdirectories for article/converted sub-directories and '*.html' files within.
    # for filepath in glob.glob('**/**/converted/*.html'):
    
    #     # Looking for "converted" article.html files...
    #     (path, filename) = os.path.split(filepath)
    #     match = re.match(converted_pattern, filepath)
      
    #     if match: 
    #         year = match.group(1)
    #         term = match.group(2)
    #         a_name = match.group(3)
    #         html_name = match.group(4)

    #         issue = "{}-{}".format(year, term)
    #         logfile = filepath.replace(".html", ".log")
    #         logging.basicConfig(filename=logfile, encoding='utf-8', level=logging.DEBUG)
    #         logging.info("Found .html file: " + filepath)

    #         # Reset our frontmatter from the template and increment the article index
    #         frontmatter = fm_template
    #         aIndex += 1

    #         # Go for liftoff
    #         rootstalk_markdownify(filepath)
    #         # rootstalk_azure_media(year, term, filepath)
    #         # rootstalk_make_articles(year, term, filepath)




# # directory_selector(path) -------------------------------------------------
# def directory_selector(path):
#     with st.form("select_directory"):
#         dir_names = [filename for filename in os.listdir(path) if os.path.isdir(os.path.join(path,filename))]
#         selected = st.selectbox('Select a Directory', dir_names)

#         # Every form must have a submit button.
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             dir_path = os.path.join(path, selected)
#             st.write(f'You selected {dir_path}')
#             return dir_path

#     return False

