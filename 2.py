import os

res2_path = os.path.abspath('res2.res')
ASYM_path = os.path.abspath('ASYM.txt')
ini_path = os.path.abspath('ini.DAT')

if os.path.exists(res2_path)==False:
    res2_path = os.path.abspath('Asym_n_states/res2.res')
    ASYM_path = os.path.abspath('Asym_n_states/ASYM.txt')
    ini_path = os.path.abspath('Asym_n_states/ini.DAT')

file=open (res2_path, 'r')
file2=open (ASYM_path, 'w')
file3=open(ini_path, 'r')

str1=file3.readline()
no, v =str1.split()
no=int(no)
v=int(v)
str1=file3.readline()
J,Ka,Kc=str1.split()
J=int(J)
Ka=int(Ka)
Kc=int(Kc)
kk=1

if no==1:
    while (True):
        str1=file.readline()
        if len(str1) == 0: # Нулевая длина обозначает конец файла (EOF)
            break
        str2=str1.replace ('J=','')
        str2=str2.split()
        str2.pop(1)
        str2.pop(0)
        if int(str2[0])==v and int(str2[1])==J and int(str2[2])==Ka \
               and int(str2[3])==Kc:
            print ('%s' %(str1))
            file2.write ('%s' %(str1))
            J=J+1
            Kc=Kc+1

else:
    while(True):
        str1=file.readline()
        if len(str1)==0:
            break
        
        str2=str1.replace ('J=','')
        str2=str2.split()
        str2.pop(1)
        str2.pop(0)
        if kk==1:
            if int(str2[0])==v and int(str2[1])==J and int(str2[2])==Ka \
               and int(str2[3])==Kc:
                print ('%s' %(str1))
                file2.write ('%s' %(str1))
                Kc=Kc-1
                kk=0
                file.seek(0)
        else:
            if int(str2[0])==v and int(str2[1])==J and int(str2[2])==Ka \
               and int(str2[3])==Kc:
                print ('%s' %(str1))
                file2.write ('%s' %(str1))
                J=J+1
                Kc=Kc+2
                kk=1
                file.seek(0)
                

file.close()
file2.close()
file3.close()
