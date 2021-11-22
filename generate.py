import os

from jinja2 import Environment, FileSystemLoader, Template
import mistune
import yaml


content_folder = "_pages/"

template = None
with open("templates/page.html") as f:
  template = Environment(loader=FileSystemLoader("templates")).from_string(f.read())
  f.close()


# read pages
pages = []
for page_file in os.listdir(content_folder):
  print(page_file)
  contents = ""
  with open(content_folder+page_file) as f:
    contents = f.read().split("---")
    f.close()
  context = yaml.safe_load(contents[1])
  context["body"] = mistune.markdown(contents[2], escape=False)
  context["path"] = page_file.strip(".md")+".html"
  if context["path"]=="home.html":
    context["path"] = "index.html"
  pages.append(context)

for page in pages:      
  rendered_page = template.render(**page)
  with open(page["path"], "w") as f:
    f.write(rendered_page)
    f.close()  
  
