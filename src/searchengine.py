from blist import sorteddict
import operator

stopwords = open('../stopwords.txt','r').readlines()[0].strip().split(',')
def findFileNumber(word,category):
	f = open('NewIndex/'+category+'/filemap.txt','r')
	line = f.readline()
	count = -1
	while line < word:
		line = f.readline()
		count+=1
	return count

def findDocList(word,category,file_number):
	index_file = open('NewIndex/'+category+'/File'+str(file_number)+'.txt','r')
	line = index_file.readline().strip().split(':')
		
	while line[0]<word:
		line = index_file.readline().strip().split(':')
		
	if line[0] == word:
		return line[1].split(';')[:-1]
	else:
		return []

def printTitles(docs):
	for i in docs:
		file_number = int(i[0])/300000
		f = open('NewIndex/pageMap'+str(file_number)+'.txt')
		line = f.readline().strip().split(' ')
		
		while int(line[0]) < int(i[0]):
			line = f.readline().strip().split(' ')

		print ' '.join(line[1:])	
		

def findNormalQuery(query):
	query_items = query.split(' ')
	docs = {} 
	for word in query_items:
		file_number = findFileNumber(word,"Title")
		doc_list = findDocList(word,"Title",file_number)
		for i in doc_list:
			data = i.split('-')
			if data[0] not in docs:
				docs[data[0]] = 1000
			else:
				docs[data[0]] += 1000
		
	
	for word in query_items:
		word = word.lower()
		file_number = findFileNumber(word,"Infobox")
		if file_number == -1:
			continue
		doc_list = findDocList(word,"Infobox",file_number)
		for i in doc_list:
			data = i.split('-')
			if data[0] not in docs:
				docs[data[0]] = int(data[1])
			else:
				docs[data[0]] += int(data[1])
		
	for word in query_items:
		word = word.lower()
		file_number = findFileNumber(word,"Bodywords")
		if file_number == -1:
			continue
		doc_list = findDocList(word,"Bodywords",file_number)
		for i in doc_list:
			data = i.split('-')
			if data[0] not in docs:
				docs[data[0]] = int(data[1])
			else:
				docs[data[0]] += int(data[1])
				

	docs = sorted(docs.iteritems(),key = operator.itemgetter(1),reverse = True)[:10]
	printTitles(docs)
	print
	return
		


def findCatQuery(query):
	query_items = query.split(' ')
	docs = {} 
	for item in query_items:
		item = item.split(':')
		category=''
		if item[0]=='b':
			category = "Bodywords"
			item[1] = item[1].lower()
		elif item[0] == 't':
			category= "Title"
		elif item[0]=='i':
			category = "Infobox"
			item[1] = item[1].lower()
		elif item[0] == 'l':
			category= "Links"
		else:	
			category = "Bodywords"
			item[1] = item[1].lower()

		file_number = findFileNumber(item[1],category)
		if file_number == -1:
			continue
		doc_list = findDocList(item[1],category,file_number)
		for i in doc_list:
			data = i.split('-')
			if data[0] not in docs:
				docs[data[0]] = 1
			else:
				docs[data[0]] += 1
	
	docs = sorted(docs.iteritems(),key = operator.itemgetter(1),reverse = True)[:10]
	printTitles(docs)
	print
	return

		


def findDocs(query):
	if ':' in query:
		findCatQuery(query)
	else:
		findNormalQuery(query)


if __name__=="__main__":
	num_of_queries = input()
	while num_of_queries != 0:
		query = raw_input()
		findDocs(query)
		num_of_queries-=1
