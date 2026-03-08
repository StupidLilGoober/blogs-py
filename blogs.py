"""Main"""

import sys
import os
import json
from datetime import date

import markdown as md

import scripts
import scripts.config

args = sys.argv

def new_blog(name):
	"""Setup a blogsite."""

	try:
		os.mkdir(name)
	except FileExistsError:
		print("that blog already exists")
		quit(1)
	with open("blogs.json", "w", encoding="utf8") as file:
		file.write(scripts.config.default_config_json)
	scripts.config.write_style(name+"/style.css", scripts.config.default_config)
	os.mkdir(name + "/html")
	os.mkdir(name + "/src")
	with open(name + "/src/" + f"{date.today()}" + ".md", "w", encoding="utf8") as file:
		file.write("# Title\n")
		file.write("*date*")

def build(name):
	"""Build a blogsite."""

	with open("blogs.json", "r", encoding="utf8") as file:
		conf = json.load(file)
		scripts.config.write_style(name+"/style.css", conf)
	try:
		os.remove(name + "/index.html")
	except FileNotFoundError:
		pass
	with open(name + "/index.html", "w", encoding="utf8") as file:
		file.write("<!-- auto-generated !-->\n")
		file.write("<!DOCTYPE html>\n")
		file.write("<link href='style.css' rel='stylesheet'>\n")
		file.write("<h1>Blogs</h1>")
	# build markdown blogs
	for dirpath, dirname, filenames in os.walk("blogs/src"):
		for filename in filenames:
			file_path = os.path.join(dirpath, filename)
			with open(file_path, "r", encoding="utf8") as file:
				html = md.markdown(file.read())
				with open("blogs/html/" + filename[:-3] + ".html", "w", encoding="utf8") as htmlfile:
					htmlfile.write("<!-- auto-generated !-->\n")
					htmlfile.write("<!DOCTYPE html>\n")
					htmlfile.write('<link rel="stylesheet" href="../style.css">\n')
					htmlfile.write(html)
			# add to index.html
			with open(name + "/index.html", "a", encoding="utf8") as file:
				file.write(f"\n<a href='html/{filename[:-3]+".html"}'>{filename[:-3]}</a>")

def new_article():
	"""Setup a new article."""

	with open("blogs/src/" + f"{date.today()}" + ".md", "w", encoding="utf8") as file:
		file.write("# Title\n")
		file.write("*date*")

try:
	args[1] = args[1]
except IndexError:
	print("no arguments passed")
	quit(1)

if args[1] == "new":
	new_blog("blogs")

if args[1] == "build":
	build("blogs")

if args[1] == "blog":
	new_article()
