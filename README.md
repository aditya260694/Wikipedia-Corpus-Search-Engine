WIKIPEDIA SEARCH ENGINE - PHASE 1
Aditya Chandran
201201115

Index consists of multiple files which represent the word-page mapping along with number of ocurrences of the word in each page of Title,Infobox,Body Text,Links


PACKAGES TO BE INSTALLED
1. blist 
 can be downloaded from https://pypi.python.org/packages/source/b/blist/blist-1.3.6.tar.gz
execute python setup.py install to install


EXTRA FEATURES
Created a secondary indexing for Body Text information i.e Body Text is split into multiple files of 500Mb each and start words for each file are specified
Hashed the document ids so that lesser space is taken for storing multiple ocurrences
Removed stop words, the list of which is in stopwords.txt
Used a B-Tree based implementation of lists and dictionaries which ensures even large data can be handled efficiently by using main memory.
