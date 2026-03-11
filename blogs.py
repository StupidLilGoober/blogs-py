import config
import markdown as md
import json
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
	with open("blogs.json", "w") as file:
		file.write(config.default_config_json)
	config.writeStyle(name+"/style.css", config.default_config)
	os.mkdir(name + "/html")
	os.mkdir(name + "/src")
	with open(name + "/src/" + f"{date.today()}" + ".md", "w") as file:
		file.write("# Title\n")
		file.write("*date*")

def build(name):
	with open("blogs.json", "r") as file:
		conf = json.load(file)
		config.writeStyle(name+"/style.css", conf)
	try:
		os.remove(name + "/index.html")
	except FileNotFoundError:
		pass
	with open(name + "/index.html", "w") as file:
		file.write("<!-- auto-generated !-->\n")
		file.write("<!DOCTYPE html>\n")
		file.write("<link href='style.css' rel='stylesheet'>\n")
		file.write("<h1>Blogs</h1>")
	
	# build markdown blogs
	for dirpath, dirname, filenames in os.walk("blogs/src"):
		for filename in filenames:
			file_path = os.path.join(dirpath, filename)
			with open(file_path, "r") as file:
				html = md.markdown(file.read())
				with open("blogs/html/" + filename[:-3] + ".html", "w") as htmlfile:
					htmlfile.write("<!-- auto-generated !-->\n")
					htmlfile.write("<!DOCTYPE html>\n")
					htmlfile.write('<link rel="stylesheet" href="../style.css">\n')
					htmlfile.write(html)
			# add to index.html
			with open(name + "/index.html", "a") as file:
				file.write(f"\n<a href='html/{filename[:-3]+".html"}'>{filename[:-3]}</a>")

def newArticle():
	with open("blogs/src/" + f"{date.today()}" + ".md", "w") as file:
		file.write("# Title\n")
		file.write("*date*")

try:
	args[1] = args[1]
except IndexError:
	print("no arguments passed")
	quit(1)

if args[1] == "new":
	newBlog("blogs")

if args[1] == "build":
	build("blogs")

if args[1] == "blog":
	newArticle()