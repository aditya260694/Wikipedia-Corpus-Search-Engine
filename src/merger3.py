from os import rename,remove,listdir


f = open('NewIndex/Bodywords/File0.txt','r')
files = listdir('NewIndex/Bodywords')
f_out = open('NewIndex/Bodywords/Final.txt','w')

print len(files)
files.remove('File0.txt')
files.remove('Final.txt')

	
for i in files:
    file_name = 'NewIndex/Bodywords/' + str(i)
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
    remove('NewIndex/Bodywords/File0.txt')	
    remove(file_name)	
    rename('NewIndex/Bodywords/Final.txt','NewIndex/Bodywords/File0.txt')
    f = open('NewIndex/Bodywords/File0.txt','r')
    f_out = open('NewIndex/Bodywords/Final.txt','w')
f.close()
f_out.close()
remove('NewIndex/Bodywords/Final.txt')	
rename('NewIndex/Bodywords/File0.txt','NewIndex/Bodywords/Final.txt')

