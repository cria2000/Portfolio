# !/usr/bin.python
#-*-coding:utf-8-*-
import os
import sys,string
import subprocess as sp
import re
import shutil
RE=sys.argv[1]
i=0

def getListOfFile(filename) :
    files=open(filename,'r')
    lines=files.read().splitlines()
    return lines

def getLineCount(filename) :
    files=open(filename,'r')
    linecount=0
    while True :
        line=files.readline()
        if not line :
            break
        else :
            list=line.split('\n')
            linecount +=1
    return linecount
linecount=0
files=os.listdir('.')
print("---------------------------------")
for index in range(0,len(files)) :
    if RE.startswith("\<")==True and RE.endswith("\>")==True :
        f=open("file1","w")
        RE=RE[2:len(RE)-2]
        sp.call("git ls-files > file2",shell=True)
        File=getListOfFile('file2')
        for line in File : 
            if line.startswith(RE) : 
                if line.find(RE+".")>=0 or line.find(RE+"/")>=0 :
                    f.write(line+"\n")
            if line.find("/"+RE)>=0 and line.find(RE+"/")>=0 :
                f.write(line+"\n")
            if line.find("/"+RE)>=0 and line.find(RE+".")>=0 :
                f.write(line+"\n")
            if line.find("."+RE)>=0 and line.endswith(RE)==True : 
                f.write(line+"\n")
        f.close()
        listOfFiles = getListOfFile('file1')
        linecount = getLineCount('file1')
        linecount=int(linecount)
        if linecount == 0 :
            break
        if linecount == 1 :
            break
        else :
            for item in listOfFiles : 
                i=i+1
                if i>10 or i>linecount :
                    break
                else :
                    print(item + "         ("+str(i)+")")
        RE="\<"+RE+"\>"

    elif (RE.startswith("\<"))==True :
        f=open("file1","w")
        RE=RE[2:]
        sp.call("git ls-files > file2",shell=True)
        File=getListOfFile('file2')
        for line in File : 
            if line.find("/"+RE)>=0 :
                f.write(line+"\n")
            if line.find("."+RE)>=0 :
                f.write(line+"\n")
            if line.startswith(RE)==True : 
                f.write(line+"\n")
        f.close()
        listOfFiles = getListOfFile('file1')
        linecount = getLineCount('file1')

        linecount=int(linecount)
        if linecount == 0 :
            break
        if linecount == 1 :
            break
        else :
            for item in listOfFiles : 
                i=i+1
                if i>10 or i>linecount :
                    break
                else :
                    print(item + "         ("+str(i)+")")
        RE="\<"+RE

    elif RE.endswith("\>")==True :
        f=open("file1","w")
        RE=RE[:len(RE)-2]
        sp.call("git ls-files > file2",shell=True)
        File=getListOfFile('file2')
        for line in File :
            if line.find(RE+"/")>=0 :
                f.write(line+"\n")
            if line.find(RE+".")>=0 :
                f.write(line+"\n")
            if line.endswith(RE)==True :
                f.write(line+"\n")
        f.close()
        listOfFiles = getListOfFile('file1')
        linecount = getLineCount('file1')
        linecount=int(linecount)
        if linecount == 0 :
            break
        if linecount == 1 :
            break
        else :
            for item in listOfFiles : 
                i=i+1
                if i>10 or i>linecount :
                    break
                print(item + "         ("+str(i)+")")
        RE=RE+"\>"
    

    else :
        if sp.call("git ls-files `git rev-parse -show-toplevel` | grep "+RE + ">file1", shell=True)==0 :
            listOfFiles = getListOfFile('file1')
            linecount=getLineCount('file1')
            linecount=int(linecount)
            if linecount == 0 :
                break
            if linecount == 1 :
                break
            else :
                for item in listOfFiles : 
                    i=i+1
                    if i>10 or i>linecount :
                        break
                    else :
                        print(item + "         ("+str(i)+")")
            
while True :
    i=0
    if linecount==0 :
        print("There are no files.")
        if os.path.isfile("file1") :
            os.system("rm file1")
        if os.path.isfile("file2") :
            os.system("rm file2")
        break

    if linecount==1 :
        name=listOfFiles[0]
        if os.path.isfile("file1") :
            os.system("rm file1")
        if os.path.isfile("file2") :
            os.system("rm file2")
        os.system('vi '+name)
        break
    print("Enter file shortcut (shown on the right) or keyword to further refine the search : ")
    command = raw_input() 

    if (command=='1')==1 or (command=='2')==1 or (command=='3')==1 or (command=='4')==1 or (command=='5')==1 or (command=='6')==1 or (command=='7')==1 or (command=='8')==1 or (command=='9')==1 :
        command=int(command)
        name=listOfFiles[command-1]
        if os.path.isfile("file1") :
            os.system("rm file1")
        if os.path.isfile("file2") :
            os.system("rm file2")
        os.system('vi '+ name)
        break
    else :
        RE=command
        if RE.startswith("\<")==True and RE.endswith("\>")==True :
            RE=RE[2:len(RE)-2]
            File=getListOfFile('file1')
            f=open("file1","w+t")
            for line in File : 
                if line.match(RE) : 
                    if line.find(RE+".")>=0 or line.find(RE+"/") :
                        f.write(line)
                if line.find("/"+RE) and line.find(RE+"/") :
                    f.write(line)
                if line.find("/"+RE) and line.find(RE+".") :
                    f.write(line)
                if line.find("."+RE) and line.find(RE+"\n") : 
                    f.write(line)
            f.close()
            listOfFiles = getListOfFile('file1')
            linecount = getLineCount('file1')
            linecount=int(linecount)
            if linecount!=0 :   
                for item in listOfFiles : 
                    i=i+1
                    if i>10 or i>linecount :
                        break
                    print(item + "         ("+str(i)+")")

        elif (RE.startswith("\<"))==True :
            RE=RE[2:]
            File=getListOfFile('file1')
            f=open("file1","w+t")
            for line in File : 
                if line.find("/"+RE)>=0 :
                    f.write(line+"\n")
                if line.find("."+RE)>=0 :
                    f.write(line+"\n")
                if line.startswith(RE)>0 : 
                    f.write(line+"\n")
            f.close()
            listOfFiles = getListOfFile('file1')
            linecount = getLineCount('file1')
            linecount=int(linecount)
            if linecount!=0:   
                for item in listOfFiles : 
                    i=i+1
                    if i>10 or i>linecount :
                        break
                    else : 
                        print(item + "         ("+str(i)+")")

        elif RE.endswith("\>")==True :
            RE=RE[:len(RE)-2]
            File=getListOfFile('file1')
            f=open("file1","w+t")
            for line in File :
                if line.find(RE+"/") :
                    f.write(line)
                if line.find(RE+".") :
                    f.write(line)
                if line.file(RE+"\n") :
                    f.write(line)
            f.close()
            listOfFiles = getListOfFile('file1')
            linecount = getLineCount('file1')
            linecount=int(linecount)
            if linecount!=0 :   
                for item in listOfFiles : 
                    i=i+1
                    if i>10 or i>linecount :
                        break
                    else :
                        print(item + "         ("+str(i)+")")
        else :

            shutil.copy('file1','file2')
            if sp.call("grep "+RE + " file2 >file1", shell=True)==0 :
                listOfFiles = getListOfFile('file1')
                linecount=getLineCount('file1')
                linecount=int(linecount)
                print("---------------------------------")
                if linecount == 1 :
                    name=listOfFiles[0]
                    if os.path.isfile("file1") :
                        os.system("rm file1")
                    if os.path.isfile("file2") :
                        os.system("rm file2")
                    os.system('vi '+name)
                    break
                else :
                    for item in listOfFiles : 
                        i=i+1
                        if i>10 or i>linecount :
                            break
                        print(item + "         ("+str(i)+")")
        
