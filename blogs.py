import scripts
import scripts.config
import markdown as md
from datetime import date

import sys
import os

args = sys.argv

def newBlog(name):
	try:
		os.mkdir(name)
	except FileExistsError:
		print("that blog already exists")
		quit(1)
	with open(name + "/index.html", "w") as file:
		file.write(scripts.config.bloglist_html)
	with open("blogs.json", "w") as file:
		file.write(scripts.config.default_config_json)
	scripts.config.writeStyle(name+"/style.css", scripts.config.default_config)
	os.mkdir(name + "/html")
	os.mkdir(name + "/src")
	with open(name + "/src/" + f"{date.today()}" + ".md", "w") as file:
		file.write("# Title")

def build(name):
	for dirpath, dirname, filenames in os.walk("blogs/src"):
		for filename in filenames:
			file_path = os.path.join(dirpath, filename)
			with open(file_path, "r") as file:
				html = md.markdown(file.read())
				with open("blogs/html/" + filename[:-3] + ".html", "w") as htmlfile:
					htmlfile.write("<!DOCTYPE html>\n")
					htmlfile.write('<link rel="stylesheet" href="../style.css">\n')
					htmlfile.write(html)

try:
	args[1] = args[1]
except IndexError:
	print("no arguments passed")
	quit(1)

if args[1] == "new":
	newBlog("blogs")

if args[1] == "build":
	build("blogs")