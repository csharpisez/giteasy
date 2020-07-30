import os
import tkinter as tk

root= tk.Tk()

root.wm_title("easygit")

canvas1 = tk.Canvas(root, width = 200, height = 650, bg = '#fbceb1', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='easygit v0.4 Alpha', bg = '#fbceb1')
label1.config(font=('calibri', 10))
canvas1.create_window(100, 25, window=label1)

entry1 = tk.Entry (root) 
canvas1.create_window(100, 50, window=entry1)

def changeUserName ():
    username = entry1.get()
    os.system(f'start cmd /k git config --global user.name {username}')

def changeEmail ():
    email = entry1.get()
    os.system(f'start cmd /k git config --global user.email {email}')

def showOrigin ():
    os.system(f'start cmd /k git config --list --show-origin')

def listSettings ():
    os.system(f'start cmd /k git config --list')

def cloneRepo ():
    repourl = entry1.get()
    os.system(f'start cmd /k git clone {repourl}')

def makeRepo ():
    repodir = entry1.get()
    os.chdir(f'{repodir}')
    os.system(f'start cmd /k git init')

def addFile ():
    repodir2 = entry1.get()
    filename =  input("Enter File Name : ")
    os.chdir(f'{repodir2}')
    os.system(f'start cmd /k git add {filename}')

def status ():
    repodir2 = entry1.get()
    os.chdir(f'{repodir2}')
    os.system(f'start cmd /k git status')

def commit ():
    repodir2 = entry1.get()
    os.chdir(f'{repodir2}')
    os.system(f'start cmd /k git commit')

def remove ():
    repodir2 = entry1.get()
    filename = input("Enter Filename To Reomve : ")
    os.chdir(f'{repodir2}')
    os.system(f'start cmd /k git rm {filename}')

def history ():
    repodir2 = entry1.get()
    os.chdir(f'{repodir2}')
    os.system(f'start cmd /k git log')


    
button1 = tk.Button(text='      Change User      ', command=changeUserName, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=button1)

button2 = tk.Button(text='     Change Email    ', command=changeEmail, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 150, window=button2)

button3 = tk.Button(text='      Show Origin     ', command=showOrigin, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 200, window=button3)

button4 = tk.Button(text='      List Settings     ', command=listSettings, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 250, window=button4)

button5 = tk.Button(text='     Clone Repo     ', command=cloneRepo, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 300, window=button5)

button6 = tk.Button(text='      Make Repo     ', command=makeRepo, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 350, window=button6)

button7 = tk.Button(text='      Add File    ', command=addFile, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 400, window=button7)

button8 = tk.Button(text='      Check Status    ', command=status, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 450, window=button8)

button9 = tk.Button(text='      Commit    ', command=commit, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 500, window=button9)

button10 = tk.Button(text='      Remove    ', command=remove, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 550, window=button10)

button11 = tk.Button(text='      History    ', command=history, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 600, window=button11)


root.mainloop()
