from os import rename,remove,listdir

f = open('NewIndex/Infobox/InfoboxWords0.txt','r')
num_of_files = len(listdir('NewIndex/Infobox'))
f_out = open('NewIndex/Infobox/InfoboxWords.txt','w')
print num_of_files
for i in range(1,num_of_files):
    file_name = 'NewIndex/Infobox/InfoboxWords' + str(i) + '.txt'
    f1 = open(file_name,'r')
    line1 = f.readline()
    line2 = f1.readline()
    print i
    while line1 !='' and line2!='':
	  w1 = line1.split(':')
	  w2 = line2.split(':')
	  if w1[0] == w2[0]:
	   	w1[1] = w1[1][:-1] + w2[1]
		f_out.write(':'.join(w1))
		line1 = f.readline()
	  	line2 = f1.readline()
	  elif w1[0] < w2[0]:
		f_out.write(':'.join(w1))
		line1 = f.readline()
	  else:
		f_out.write(':'.join(w2))
	  	line2 = f1.readline()
    while line1 != '':
	f_out.write(line1)
	line1 = f.readline()
    while line2 != '':
	f_out.write(line2)
	line2 = f1.readline()
    f.close()
    f1.close()
    remove('NewIndex/Infobox/InfoboxWords0.txt')	
    remove(file_name)	
    rename('NewIndex/Infobox/InfoboxWords.txt','NewIndex/Infobox/InfoboxWords0.txt')
    f = open('NewIndex/Infobox/InfoboxWords0.txt','r')
    f_out = open('NewIndex/Infobox/InfoboxWords.txt','w')
f.close()
f_out.close()
remove('NewIndex/Infobox/InfoboxWords.txt')	
rename('NewIndex/Infobox/InfoboxWords0.txt','NewIndex/Infobox/InfoboxWords.txt')




f = open('NewIndex/Links/Links0.txt','r')
num_of_files = len(listdir('NewIndex/Links'))
f_out = open('NewIndex/Links/Links.txt','w')
print num_of_files
for i in range(1,num_of_files):
    file_name = 'NewIndex/Links/Links' + str(i) + '.txt'
    f1 = open(file_name,'r')
    line1 = f.readline()
    line2 = f1.readline()
    print i
    while line1 !='' and line2!='':
	  w1 = line1.split(':')
	  w2 = line2.split(':')
	  if w1[0] == w2[0]:
	   	w1[1] = w1[1][:-1] + w2[1]
		f_out.write(':'.join(w1))
		line1 = f.readline()
	  	line2 = f1.readline()
	  elif w1[0] < w2[0]:
		f_out.write(':'.join(w1))
		line1 = f.readline()
	  else:
		f_out.write(':'.join(w2))
	  	line2 = f1.readline()
    while line1 != '':
	f_out.write(line1)
	line1 = f.readline()
    while line2 != '':
	f_out.write(line2)
	line2 = f1.readline()
    f.close()
    f1.close()
    remove('NewIndex/Links/Links0.txt')	
    remove(file_name)	
    rename('NewIndex/Links/Links.txt','NewIndex/Links/Links0.txt')
    f = open('NewIndex/Links/Links0.txt','r')
    f_out = open('NewIndex/Links/Links.txt','w')
f.close()
f_out.close()
remove('NewIndex/Links/Links.txt')	
rename('NewIndex/Links/Links0.txt','NewIndex/Links/Links.txt')




f = open('NewIndex/Title/Title0.txt','r')
num_of_files = len(listdir('NewIndex/Title'))
f_out = open('NewIndex/Title/Title.txt','w')
print num_of_files
for i in range(1,num_of_files):
    file_name = 'NewIndex/Title/Title' + str(i) + '.txt'
    f1 = open(file_name,'r')
    line1 = f.readline()
    line2 = f1.readline()
    print i
    while line1 !='' and line2!='':
	  w1 = line1.split(':')
	  w2 = line2.split(':')
	  if w1[0] == w2[0]:
	   	w1[1] = w1[1][:-1] + w2[1]
		f_out.write(':'.join(w1))
		line1 = f.readline()
	  	line2 = f1.readline()
	  elif w1[0] < w2[0]:
		f_out.write(':'.join(w1))
		line1 = f.readline()
	  else:
		f_out.write(':'.join(w2))
	  	line2 = f1.readline()
    while line1 != '':
	f_out.write(line1)
	line1 = f.readline()
    while line2 != '':
	f_out.write(line2)
	line2 = f1.readline()
    f.close()
    f1.close()
    remove('NewIndex/Title/Title0.txt')	
    remove(file_name)	
    rename('NewIndex/Title/Title.txt','NewIndex/Title/Title0.txt')
    f = open('NewIndex/Title/Title0.txt','r')
    f_out = open('NewIndex/Title/Title.txt','w')
f.close()
f_out.close()
remove('NewIndex/Title/Title.txt')	
rename('NewIndex/Title/Title0.txt','NewIndex/Title/Title.txt')


