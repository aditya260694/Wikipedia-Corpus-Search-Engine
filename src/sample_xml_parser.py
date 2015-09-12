import xml.sax
import re
from blist import sorteddict,blist,sortedlist
import sys

def processTitle(title):
	return re.findall('[a-zA-Z]+',title)

def processText(text):
	infobox_words = []
	for i in range(len(text)):
		if '{{Infobox' in text[i:i+9]:
			j = i+9
			count = 2
			while count != 0:
				j = j+1
				if text[j] == '{':
					count+=1
				elif text[j] == '}':
					count-=1
			important_info = re.findall('=(.*?)(\||$)',text[i:j],re.M|re.I)

			for info in important_info:
				infobox_words += re.findall('[a-zA-Z]+',info[0])
			
			text = text[:i] + text[j:]
			break
	return infobox_words,list(re.findall('((http|ftp|https){0,1}:\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?|[a-zA-Z]+)',text))

class ABContentHandler(xml.sax.ContentHandler):
  def __init__(self):
	self.index = sorteddict() 
	self.tag = []
	self.pgid = None
	self.title = None
	self.title_words = sorteddict()
	self.text = ''
	self.page_map = sortedlist()
	self.Infobox = sorteddict()
	self.Links = sorteddict()
	self.stopwords = open('stopwords.txt','r').readlines()[0].strip().split(',')
	xml.sax.ContentHandler.__init__(self)

  def printOutput(self):
	print "Printing Index"
	file_number = 1
	f2 = open('Index/fileMap.txt','w')
	f = open('Index/BodyWords'+str(file_number)+'.txt','w')  
	start_word = None
	for i in self.index:
		if start_word == None:
			start_word = i
		output = ''
		output += str(i)+':'
		for page_id in self.index[i]:
			output+=str(page_id)+'-'+str(self.index[i][page_id]) + ';'
		f.write(output+'\n')
		if f.tell() > 500000000:
			f2.write(start_word + '\n')
			start_word = None
			f.close()
			file_number+=1	
			f = open('Index/BodyWords'+str(file_number)+'.txt','w')  
	f2.write(start_word + '\n')
	f2.close()
	f.close()	
	
	f = open('Index/pageMap.txt','w')
	for i in range(len(self.page_map)):
		txt = str(i) + ' ' + str(self.page_map[i]) + '\n'
		f.write(txt)
	f.close()


	f = open('Index/InfoboxWords.txt','w')
	for i in self.Infobox:
		output = ''
		output += str(i)+':'
		for page_id in self.Infobox[i]:
			output+=str(page_id)+'-'+str(self.Infobox[i][page_id]) + ';'
		f.write(output+'\n')		
	f.close()

	f = open('Index/Links.txt','w')
	for i in self.Links:
		output = ''
		output += str(i)+':'
		for page_id in self.Links[i]:
			output+=str(page_id)+'-'+str(self.Links[i][page_id]) + ';'
		f.write(output+'\n')		
	f.close()

	f = open('Index/Title.txt','w')
	for i in self.title_words:
		output = ''
		output += str(i)+':'
		for page_id in self.title_words[i]:
			output+=str(page_id)+'-'+str(self.title_words[i][page_id]) + ';'
		f.write(output+'\n')		
	f.close()


  def startElement(self, name, attrs):
	self.tag.append(name)

  def endElement(self, name):
	self.tag=self.tag[:-1]
	if name == 'page':
		if int(self.pgid)%1000 == 0:
			print self.pgid	
		infobox_words,tokens = processText(self.text)
		for token in infobox_words:
			token = token.lower()
			if token in self.Infobox:
				if self.pgid not in self.Infobox[token]:
					self.Infobox[token][self.pgid] = 1
				else:
					self.Infobox[token][self.pgid] += 1
			elif token not in self.stopwords:
				self.Infobox[token] = sorteddict()
				self.Infobox[token][self.pgid] = 1

		for token in tokens:
			if token[2]!='':
				token = token[2]
				if token in self.Links:
					if self.pgid not in self.Links[token]:
						self.Links[token][self.pgid] = 1
					else:
						self.Links[token][self.pgid] += 1
					
				else:	
					self.Links[token] = sorteddict()
					self.Links[token][self.pgid] = 1
				

			else:
				token = token[0]
				token = token.lower()
				if token in self.index:
					if self.pgid not in self.index[token]:
						self.index[token][self.pgid] = 1
					else:
						self.index[token][self.pgid] += 1
					
				elif token not in self.stopwords:	
					self.index[token] = sorteddict()
					self.index[token][self.pgid] = 1
				
		
		title_words = processTitle(self.title)
		for i in title_words:		
				if i in self.title_words:
					if self.pgid in self.title_words[i]:
						self.title_words[i][self.pgid] += 1
					else:
						self.title_words[i][self.pgid] = 1
				else:
					self.title_words[i] = sorteddict()
					self.title_words[i][self.pgid] = 1

		self.pgid = None
		self.title = None
		self.text = ''
		
	if name == 'file':
		self.printOutput()
#		None
		
  def characters(self, content):
	if self.tag[-1] == 'id' and self.pgid == None:
		self.page_map.add(content)
		self.pgid = str(len(self.page_map) - 1)
	elif self.tag[-1] == 'title':
		self.title = content
	elif self.tag[-1] == 'text':
		self.text = self.text + content

def main(sourceFileName):
  source = open(sourceFileName)
  xml.sax.parse(source, ABContentHandler())


if __name__ == "__main__":
	source_file = sys.argv[1]
	main(source_file)
