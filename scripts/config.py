import json

default_config = {
	"style":[
		{
			"key":"color",
			"value":"white"
		},
		{
			"key":"background-color",
			"value":"#181818"
		},
		{
			"key":"font-size",
			"value":"14"
		},
		{
			"key":"margin-left",
			"value":"2em"
		},
		{
			"key":"margin-right",
			"value":"2em"
		},
		{
			"key":"text-align",
			"value":"center"
		},
		{
			"key":"font-family",
			"value":"sans-serif"
		}
	]
}
default_config_json = json.dumps(default_config, indent=2)

def writeStyle(path, config):
	with open(path, "w") as file:
		file.write("html {\n")
		for i in config["style"]:
			file.write("	"+i["key"]+":"+i["value"]+";"+"\n")
		file.write("}\n")

		file.write("code {\n")
		file.write("	background-color:black;\n")
		file.write("	border-radius:0.5em;\n")
		file.write("	font-family:monospace;\n")
		file.write("	margin: 0.2em;\n")
		file.write("}")

bloglist_html = """
<!DOCTYPE html>
<head>
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<h1>Blogs<h2>
</body>"""