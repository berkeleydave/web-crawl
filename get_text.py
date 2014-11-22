from json import *
from urllib2 import *
import operator

get = urlopen('http://www.cnn.com/2014/05/30/tech/social-media/apparently-this-matters-weed-fairy/index.html')
keyWords = {}
dictionary = {}
total = 0

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

def constructDictionary():
	temporary = open("dictionary.txt")
	parsebyline = temporary.readlines()
	for item in parsebyline:
		temp = re.sub('\t', " ", item)
		temp = re.sub('\n', "", temp)
		dictItem = temp.split()
		dictionary[dictItem[0]] = int(dictItem[1])

def dictionaryEvaluation(paragraph):
	for word in paragraph:
		if word in dictionary.keys():
			print("Checked")
			global total 
			total += dictionary[word]
			if word in keyWords.keys():
				keyWords[word] += 1
			else:
				keyWords[word] = 1

def getKeyWords():
	sorted_x = sorted(keyWords, key=keyWords.get)
	temp = [sorted_x[len(sorted_x)-1-i] for i in range(0, min(len(sorted_x), 5))]
	return temp

# Run Functions
mod = read_cnn_doc(text)
mod = remove_script(mod)
constructDictionary()
dictionaryEvaluation(mod.split())
print "Total attitude: "
print total
print "Key words: "
print getKeyWords()
