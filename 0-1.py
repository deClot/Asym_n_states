while(True):
    f=open('TRANS.RES', 'r').readlines()
    l=len(f)

    if f[l-1].find('J=',0,len(f[l-1]))==-1:    
        f.pop(-1)
        with open('TRANS.RES','w') as F:
            F.writelines(f)
    else:
        break

file = open('TRANS.RES', 'r')
file2 = open('res.res','w')
while (True):
    str1=file.readline()
    if len (str1)==0:
        break

    if str1.find ('iteration',0,len(str1))!=-1:
        t=file.tell ()

file.seek (t,0)
while(True):
    str1=file.readline()
    if str1.find ('matrix',0,len(str1))!=-1: #sodershit matrix
        break

for line in file:
    file2.write (line)
    
file.close()
