#My_Home_Page.2

#Necessary imports 
import glob
import os

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

#TODO fix brokkkkkkken links by removing ./docs/ and commit changes 
#TODO put def main lines into growing pages.. ie create a list containing your pages and loop them...


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

