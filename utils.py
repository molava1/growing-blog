#My_Home_Page.2

#Necessary imports 

import glob
import os

#Adding content to base template

def template(*building_page_template):
    
    template = {
                        'content': './content/index.html',
                        'title' : 'Molavas Page',

               },
    open('./templates/base.html').read()
           
    return template 
    
template ()

#So this code grows your site data by adding multiple sets [LISTS].
def main():
    pages = []
    pages.append([{
    "filename": "content/index.html",
    "title": "Molava's Page",
    "output": "docs/index.html",
    },
    {"filename" : "content/about_me.html",
    "title" : "About Molava",
    "output": "docs/about_me.html",
    },
    {"filename": "content/contact_me.html",
    "title": "Ring Ring",
    "output": "docs/contact_me.html",
    }])
    for page in pages:
        all_html_files = glob.glob("docs/*.html")
        template(all_html_files)
    
main()

all_html_files = glob.glob("docs/*.html")
print(all_html_files)

file_path = "docs/about_me.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)

