import os
from os import listdir
from os.path import isfile, join
from tkinter import *
import webbrowser
import urllib.parse
import urllib.request
import re
import subprocess
import getpass


def my_player(s):

    user_name = getpass.getuser()
    direc = [];

    if sys.platform == "win32" or sys.platform == "win64":
        direc = [ ('C:/Users/'+user_name+'/Music') , ('C:/Users/'+user_name+'/Videos') ]
    elif sys.platform == "darwin":
        direc =[('/Users/'+user_name+'/Music'),('/Users/'+user_name+'/Movies')]

    dir_size=len(direc)
    flag = 0
    for d in range(0,dir_size):
        xx = direc[d]
        a = [f for f in listdir(xx) if isfile(join(xx, f))]
        #print(a)
        i = 500;
        j=20
        m = [[0 for x in range(j)] for y in range(i)]
        b = [0 for x in range(j)]
        print (a)
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
                   elif ( a1[j-1] == s[k-1] ):
                       m[j][k] = m[j-1][k-1]+1
                   else:
                       m[j][k] = max(m[j-1][k],m[j][k-1])

            #print(len(a[i]),len(s),"len  ",m[len(a[i])+1][(len(s))+1])

            if (s_len == m[len(a[i])][(len(s))]):
                flag=1
                if sys.platform == "win32" or sys.platform == "win64" :
                    os.startfile(os.path.normpath(xx+"/"+a[i]))
                    break
                else:
                    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    filename = os.path.normpath(xx+"/"+a[i])
                    subprocess.call([opener, filename])
                    break;

        if flag == 1:
            break

    if flag == 0:
        play_on_youtube(s)



def play_on_youtube(s):
    query_string = urllib.parse.urlencode({"search_query": s})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(
        ("http://www.youtube.com/watch?v=" + search_results[0]))


def get_gui():
    top = Tk()
    top.wm_title("Audio/Video Finder by Uddhav")
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

get_gui()


#webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
