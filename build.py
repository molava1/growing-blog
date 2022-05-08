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
    pages = [
    {
    "my_home_page": "./content/index.html",
    "output": "docs/index.html",
    "title": "Molava's Page",
    },
    {    
    "about_me": "./content/about_me.html",
    "output": "docs/about_me.html",
    "title": "About Molava",
    },
    {
    "contact_me": "./content/contact_me.html",
    "output": "docs/contact_me.html",
    "title": "Ring Ring",
    },
    ]

    for page in pages:
        print(pages)
        
    growing_pages()


