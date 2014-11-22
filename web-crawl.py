from json import *
from urllib2 import *

get = urlopen('http://www.cnn.com/2014/11/21/justice/newtown-shooter-adam-lanza-report/index.html?hpt=hp_t1')
wordlist = []
dictionary = {}

#turns get into a string
text = get.read()

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

	#purify!
	text = text.replace("<p class="," ")
	text = text.replace("</p>"," ")
	text = text.replace("<"," ")
	text = text.replace(">"," ")
	text = text.replace("<!--"," ")
	text = text.replace("-->"," ")
	text = text.replace("/script"," ")
	text = text.replace("/"," ")

	return text


# Run Functions
mod = read_cnn_doc(text)
mod = remove_script(mod)
print(mod)
