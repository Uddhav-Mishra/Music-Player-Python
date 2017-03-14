import os
from os import listdir
from os.path import isfile, join
from tkinter import *
import webbrowser
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import urllib.request
import urllib.parse
import re

def my_player(s):
    dir=["C:/Users/ABC/Videos","C:/Users/ABC/Videos/hollywood","C:/Users/ABC/Videos/late","C:/Users/ABC/Downloads","C:/Users/ABC/Music",
         "C:/Users/ABC/Music/arijit","C:/Users/ABC/Music/english","C:/Users/ABC/Music/hindi songs","C:/Users/ABC/Music/random" ]
    dir_size=len(dir)
    flag = 0
    for d in range(0,dir_size):
        xx = dir[d]
        a = [f for f in listdir(xx) if isfile(join(xx, f))]
        #print(a)
        i = 500;j=20
        m = [[0 for x in range(j)] for y in range(i)]
        b = [0 for x in range(j)]

        a_len = len(a)
        s_len = len(s)
        for i in range(a_len):
            z = a[i]
            y = 0
            for j in range(0,500):
                for k in range(0,20):
                    m[j][k]=0;
            a1=a[i].lower()
            ai_len=len(a[i])
            #print("here\n")
            for j in range(0, ai_len+1):
                for k in range(0, s_len+1):
                   if (j==0 or k==0):
                       m[j][k]=0
                   elif (a1[j-1]==s[k-1]):
                       m[j][k]=m[j-1][k-1]+1
                   else:
                       m[j][k]=max(m[j-1][k],m[j][k-1])

            '''for j in range(0, len(a[i])):
                for k in range(0, len(s)):
                    print(m[j][k],end=' ')
                print("\n")'''

            #print(len(a[i]),len(s),"len  ",m[len(a[i])+1][(len(s))+1])

            if (s_len==m[len(a[i])][(len(s))]):
                flag=1
                os.startfile(os.path.normpath(xx+"/"+a[i]))
                break;
        if flag==1:
            break
    if flag==0:
        print("run hoja bhai")
        query_string = urllib.parse.urlencode({"search_query": s})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(("http://www.youtube.com/watch?v=" + search_results[0]))


top = Tk()
top.wm_title("Music Player by Uddhav")
f=Frame(top,height=200,width=300 )
l1 = Label(top,text="Search ")
l1.config(width=20)
l1.config(font=("Courier",10))
l1.pack(side=LEFT)
e1=Entry(top,bd=5)

e1.config(width=20)
e1.config(font=("Courier",10))

b1=Button(top,text="play",command=lambda:my_player(e1.get()))
b1.config(height=2,width=20)
b1.config(font=("Courier",10))
e1.pack(side=LEFT)
b1.pack(side=BOTTOM)
f.pack()
top.mainloop()





#webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

