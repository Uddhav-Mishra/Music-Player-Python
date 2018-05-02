import os
from os import listdir
from os.path import isfile, join
from tkinter import *
import webbrowser
import urllib.parse,urllib.request
import re,subprocess,getpass,random,ssl


# list of directories in which audio/video files are present
dir_list = [];
dir_set = set([])

# implements the search algo and playes the best matching file
def my_player(s):
    random.shuffle(dir_list)
    dir_size=len(dir_list)
    flag = 0
    for d in range(0,dir_size):
        xx = dir_list[d]
        a = [f for f in listdir(xx) if isfile(join(xx, f))]
        #print(a)
        i = 800;
        j=50
        m = [[0 for x in range(j)] for y in range(i)]
        b = [0 for x in range(j)]
        #print (a)
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


# fetch all directories with possible audio/video files
def get_all_dirs():

    user_name = getpass.getuser()
    if sys.platform == "win32" or sys.platform == "win64":
        root_dir = ('C:/Users/'+user_name)
    elif sys.platform == "darwin":
        root_dir =('/Users/'+user_name)
    file_path = (root_dir + '/py_music_player_048.txt')
    if os.path.exists(file_path):

        with open(file_path) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                dir_set.add(line.strip())
                line = fp.readline()
                cnt += 1
    else:
        for subdir, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.mp3') or file.endswith('.mp4') or file.endswith('.mkv') or file.endswith('.avi') or file.endswith('.wkv'):
                    dir_set.add(subdir)
        f = open(file_path, "w+")
        for dir_names in dir_set:
            f.write(dir_names+'\n')


    for dir_name in dir_set:
        dir_list.append(dir_name)


# in case the file is not present in system , play on youtube
def play_on_youtube(s):

    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    query_string = urllib.parse.urlencode({"search_query": s})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string,context=gcontext)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    webbrowser.open(
        ("http://www.youtube.com/watch?v=" + search_results[0]))


# deals with gui of the finder
def get_gui():
    top = Tk()
    top.wm_title("Audio/Video Finder")
    f=Frame(top,height=200,width=80 )
    l1 = Label(top,text="Search ")
    l1.config(width=10)
    l1.config(font=("Courier",20))
    l1.pack(side=LEFT)
    e1=Entry(top,bd=5)

    e1.config(width=30)
    e1.config(font=("Courier",15))

    b1=Button(top,text="Play",command=lambda:my_player(e1.get()))
    b1.config(height=1,width=10)
    b1.config(font=("Courier",20))
    e1.pack(side=LEFT)
    b1.pack(side=RIGHT)
    f.pack()
    top.mainloop()


get_all_dirs()

get_gui()
