# Mammoth - Conversion of DOCX to Markdown for Rootstalk's Digital-First Publication Plan

This very simple project was inspired by [Word 
Document to HTML or Markdown with Python - An Example Use of Python for Beginner](https://towardsdatascience.com/word-document-to-html-or-markdown-with-python-37db7150258c).  It 
also follows the procedure I have outlined in [Proper Python](https://blog.summittdweller.com/proper-python/).    

My first use...  

```
(.venv) ╭─mcfatem@MAC02FK0XXQ05Q ~/GitHub/mammoth
╰─$ mammoth Squirrel.docx moffett-squirrel.md --output-format=markdown      
(.venv) ╭─mcfatem@MAC02FK0XXQ05Q ~/GitHub/mammoth
╰─$ ll
total 96
-rw-------@ 1 mcfatem  GRIN\Domain Users    30K Jan 18 11:23 Squirrel.docx
-rw-r--r--  1 mcfatem  GRIN\Domain Users    11K Jan 18 11:26 moffett-squirrel.md
-rw-r--r--  1 mcfatem  GRIN\Domain Users    29B Jan 18 11:22 python-requirements.txt
(.venv) ╭─mcfatem@MAC02FK0XXQ05Q ~/GitHub/mammoth
╰─$ macdown moffett-squirrel.md
(.venv) ╭─mcfatem@MAC02FK0XXQ05Q ~/GitHub/mammoth
╰─$
(.venv) ╭─mcfatem@MAC02FK0XXQ05Q ~/GitHub/mammoth
╰─$ ll
total 96
-rw-------@ 1 mcfatem  GRIN\Domain Users    30K Jan 18 11:23 Squirrel.docx
-rw-r--r--@ 1 mcfatem  GRIN\Domain Users    11K Jan 18 11:26 moffett-squirrel.md
-rw-r--r--  1 mcfatem  GRIN\Domain Users    29B Jan 18 11:22 python-requirements.txt
```

## Also of Interest
After that initial experience I found [https://github.com/mwilliamson/python-mammoth](https://github.com/mwilliamson/python-mammoth).  
