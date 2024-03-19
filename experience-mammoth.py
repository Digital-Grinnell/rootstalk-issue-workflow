# experience-mammoth.py

import mammoth

custom_styles = """ b => i
                    p[style-name='Caption'] => caption"""

with open('Submitted-Word-Documents/klassen/klassen.docx', "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map = custom_styles)
    text = result.value
    with open('output.html', 'w') as html_file:
        html_file.write(text)