from json import *
from urllib2 import *

get = urlopen('http://www.cnn.com/2014/11/21/justice/newtown-shooter-adam-lanza-report/index.html?hpt=hp_t1')
wordlist = []
dictionary = {}

#turns get into a string
text = get.read()
# print(text)

def read_cnn_doc(text):
	text.split
	"".join(text)
	div = int(text.find("<strong>(CNN)</strong>"))
	end_div = int(text.rfind("endclickprint"))
	text = str(text)
	return text[div:end_div]

def remove_script(text):
	index = text.find("<script")

	#remove script portions
	while index is not -1:
		end_index = text.find("</script>")
		text = text[:index] + text[end_index+1:]
		index = text.find("<script")

	#remove comments
	string = "<!--"
	index = text.find(string)
	while index is not -1:
		text = text[:index] + text[index:]
		index = text.find(string)

	#purify!
	text = text.replace("<p class="," ")
	text = text.replace("</p>"," ")
	text = text.replace("<"," ")
	text = text.replace(">"," ")
	text = text.replace("<!--"," ")
	text = text.replace("-->"," ")
	text = text.replace("/script"," ")
	text = text.replace("/"," ")


	#remove paragraph tags
	# open_tag = text.find("<p class")
	# end_tag = text.find("</p>")
	# # print(open_tag) # debug
	# # print(end_tag) # debug
	# while open_tag is not -1 and end_tag is not -1:
	# 	remove = text[open_tag:end_tag+4]
	# 	text = text.replace(remove,"")
	# 	open_tag = text.find("<p class")
	# 	end_tag = text.find("</p>")
	# 	print(text) # debug
	# 	open_tag = text.find("<p class")
	# 	end_tag = text.find("</p>")

	return text

# text.replace("",)
# keywords
mod = read_cnn_doc(text)
mod = remove_script(mod)
print(mod)
