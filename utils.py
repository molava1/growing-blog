#My_Home_Page.2

#Creating base template htmls 
def template(*building_page_template):
    
    top_template = open('./templates/top.html').read()
    bottom_template = open('./templates/bottom.html').read()
    
    base = top_template + bottom_template
    open('base.html', 'w+').write(base)
  
#replacing content in base template
    template = open('./templates/base.html').read()
    index_content = open('./content/index.html').read() 
     
    finished_index_page = template.replace( '{{content}}', index_content)
    open ('docs/index.html','w+').write(finished_index_page)
 
    return template 
    
template ()

def main():   

    content = open('./content/index.html').read()
    index_html = template(content) 
    open('index.html', 'w+').write(index_html)
    
    about_me = open('./content/about_me.html').read()
    about_me_html = template(about_me)
    open('about_me.html', 'w+').write(str(about_me_html))

    contact_me = open('./content/contact_me.html').read()
    contact_me_html = template(contact_me)
    open('contact_me.html', 'w+').write(str(contact_me_html))
    

main()


#So this code grows your sitek data by adding multiple sets [LISTS].
def growing_pages():
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
        print(pages)
    
growing_pages()

import glob
all_html_files = glob.glob("docs/*.html")
print(all_html_files)

import os
file_path = "docs/about_me.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)

