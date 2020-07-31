import os
import tkinter as tk

root= tk.Tk()
root.resizable(width=False, height=False)

root.wm_title("giteasy v0.5a")

canvas1 = tk.Canvas(root, width = 800, height = 700, bg = '#e7e7e7', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='giteasy v0.5a Alpha (Powered by Git and Python)', bg = '#e7e7e7', fg = '#676767')
label1.config(font=('calibri', 10))
canvas1.create_window(650, 675, window=label1)

label2 = tk.Label(root, text='giteasy', bg = '#e7e7e7', fg='#676767')
label2.config(font=('calibri', 50))
canvas1.create_window(125, 75, window=label2)

#entry1 = tk.Entry (root) 
#canvas1.create_window(100, 50, window=entry1)

#entry2 = tk.Entry (root) 
#canvas1.create_window(100, 100, window=entry2)

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
    canvas2 = tk.Canvas(root, width = 500, height = 500, bg = '#e7e7e7')
    canvas1.create_window(500, 400, window=canvas2)
    label10 = tk.Label(root, text='Repository Link:', bg = '#e7e7e7', fg = '#676767')
    label10.config(font=('calibri', 20))
    canvas2.create_window(125, 250, window=label10)
    label11 = tk.Label(root, text='(Optional) Destination Folder:', bg = '#e7e7e7', fg = '#676767')
    label11.config(font=('calibri', 10))
    canvas2.create_window(125, 325, window=label11)
    entry3 = tk.Entry (root) 
    canvas2.create_window(300, 250, window=entry3)
    entry4 = tk.Entry (root) 
    canvas2.create_window(300, 325, window=entry4)
    def repoclone ():
            repourl = entry3.get()
            destination = entry4.get()
            os.system(f'start cmd /k git clone {repourl} {destination}')
    button12 = tk.Button(text='      Clone Repo    ', command=repoclone, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
    canvas2.create_window(375, 450, window=button12)

def makeRepo ():
    canvas2 = tk.Canvas(root, width = 500, height = 500, bg = '#e7e7e7')
    canvas1.create_window(500, 400, window=canvas2)
    label10 = tk.Label(root, text='Repo Folder :', bg = '#e7e7e7', fg = '#676767')
    label10.config(font=('calibri', 20))
    canvas2.create_window(125, 250, window=label10)
    entry3 = tk.Entry (root) 
    canvas2.create_window(300, 250, window=entry3)
    def repomake ():
            repodir = entry3.get()
            os.chdir(f'{repodir}')
            os.system(f'start cmd /k git init')
    button12 = tk.Button(text='      Make Repo    ', command=repomake, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
    canvas2.create_window(375, 450, window=button12)

def addFile ():
    canvas2 = tk.Canvas(root, width = 500, height = 500, bg = '#e7e7e7')
    canvas1.create_window(500, 400, window=canvas2)
    entry3 = tk.Entry (root) 
    canvas2.create_window(300, 250, window=entry3)
    entry4 = tk.Entry (root) 
    canvas2.create_window(300, 325, window=entry4)
    label10 = tk.Label(root, text='Repo Directory :', bg = '#e7e7e7', fg = '#676767')
    label10.config(font=('calibri', 20))
    canvas2.create_window(125, 250, window=label10)
    label11 = tk.Label(root, text='File Name :', bg = '#e7e7e7', fg = '#676767')
    label11.config(font=('calibri', 20))
    canvas2.create_window(125, 325, window=label11)
    def fileadd ():
            repodir = entry3.get()
            filename = entry4.get()
            os.chdir(f'{repodir}')
            os.system(f'start cmd /k git add {filename}')
    button12 = tk.Button(text='      Add File    ', command=fileadd, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
    canvas2.create_window(375, 450, window=button12)

def status ():
    canvas2 = tk.Canvas(root, width = 500, height = 500, bg = '#e7e7e7')
    canvas1.create_window(500, 400, window=canvas2)
    label10 = tk.Label(root, text='Repo Directory :', bg = '#e7e7e7', fg = '#676767')
    label10.config(font=('calibri', 20))
    canvas2.create_window(125, 250, window=label10)
    entry3 = tk.Entry (root) 
    canvas2.create_window(300, 250, window=entry3)
    def statuscheck ():
            repodir = entry3.get()
            os.chdir(f'{repodir}')
            os.system(f'start cmd /k git status')
    button12 = tk.Button(text='      Check    ', command=statuscheck, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
    canvas2.create_window(375, 450, window=button12)

def commit ():
    canvas2 = tk.Canvas(root, width = 500, height = 500, bg = '#e7e7e7')
    canvas1.create_window(500, 400, window=canvas2)
    label10 = tk.Label(root, text='Repo Directory :', bg = '#e7e7e7', fg = '#676767')
    label10.config(font=('calibri', 20))
    canvas2.create_window(125, 250, window=label10)
    entry3 = tk.Entry (root) 
    canvas2.create_window(300, 250, window=entry3)
    def gitcommit ():
            repodir = entry3.get()
            os.chdir(f'{repodir}')
            os.system(f'start cmd /k git commit')
    button12 = tk.Button(text='      Commit    ', command=gitcommit, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
    canvas2.create_window(375, 450, window=button12)

def remove ():
    canvas2 = tk.Canvas(root, width = 500, height = 500, bg = '#e7e7e7')
    canvas1.create_window(500, 400, window=canvas2)
    label10 = tk.Label(root, text='Repo Directory :', bg = '#e7e7e7', fg = '#676767')
    label10.config(font=('calibri', 20))
    canvas2.create_window(125, 250, window=label10)
    label11 = tk.Label(root, text='File Name :', bg = '#e7e7e7', fg = '#676767')
    label11.config(font=('calibri', 20))
    canvas2.create_window(125, 325, window=label11)
    entry3 = tk.Entry (root) 
    canvas2.create_window(300, 250, window=entry3)
    entry4 = tk.Entry (root) 
    canvas2.create_window(300, 325, window=entry4)
    def gitremove ():
            repodir = entry3.get()
            filename = entry4.get()
            os.chdir(f'{repodir}')
            os.system(f'start cmd /k git rm {filename}')
    button12 = tk.Button(text='      Remove    ', command=gitremove, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
    canvas2.create_window(375, 450, window=button12)

def history ():
    canvas2 = tk.Canvas(root, width = 500, height = 500, bg = '#e7e7e7')
    canvas1.create_window(500, 400, window=canvas2)
    label10 = tk.Label(root, text='Repo Directory :', bg = '#e7e7e7', fg = '#676767')
    label10.config(font=('calibri', 20))
    canvas2.create_window(125, 250, window=label10)
    entry3 = tk.Entry (root) 
    canvas2.create_window(300, 250, window=entry3)
    def repohistory ():
            repodir = entry3.get()
            os.chdir(f'{repodir}')
            os.system(f'start cmd /k git log')
    button12 = tk.Button(text='      History    ', command=repohistory, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
    canvas2.create_window(375, 450, window=button12)

def login ():
    canvas2 = tk.Canvas(root, width = 500, height = 500, bg = '#e7e7e7')
    canvas1.create_window(500, 400, window=canvas2)
    label10 = tk.Label(root, text='Username :', bg = '#e7e7e7', fg = '#676767')
    label10.config(font=('calibri', 20))
    canvas2.create_window(125, 250, window=label10)
    label11 = tk.Label(root, text='Git Email :', bg = '#e7e7e7', fg = '#676767')
    label11.config(font=('calibri', 20))
    canvas2.create_window(125, 325, window=label11)
    entry3 = tk.Entry (root) 
    canvas2.create_window(300, 250, window=entry3)
    entry4 = tk.Entry (root) 
    canvas2.create_window(300, 325, window=entry4)
    def loginfunction ():
            username = entry3.get()
            email = entry4.get()
            os.system(f'start cmd /k git config --global user.name {username}')
            os.system(f'start cmd /k git config --global user.email {email}')
    button12 = tk.Button(text='      Login    ', command=loginfunction, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
    canvas2.create_window(375, 450, window=button12)

def about ():
    canvas2 = tk.Canvas(root, width = 500, height = 500, bg = '#e7e7e7')
    canvas1.create_window(500, 400, window=canvas2)
    label10 = tk.Label(root, text='easygit is a program powered by python and git to make git easier for everyone\nin while being substantially lighter than other desktop clients.\n Made and maintained by DudeDaCode.', bg = '#e7e7e7', fg = '#676767')
    label10.config(font=('calibri', 10))
    canvas2.create_window(250, 100, window=label10)


    
#button1 = tk.Button(text='      Change User      ', command=changeUserName, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
#canvas1.create_window(100, 150, window=button1)

#button2 = tk.Button(text='     Change Email    ', command=changeEmail, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
#canvas1.create_window(100, 200, window=button2)

button3 = tk.Button(text='      Show Origin     ', command=showOrigin, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 150, window=button3)

button4 = tk.Button(text='      List Settings     ', command=listSettings, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 200, window=button4)

button5 = tk.Button(text='     Clone Repo     ', command=cloneRepo, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 250, window=button5)

button6 = tk.Button(text='      Make Repo     ', command=makeRepo, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 300, window=button6)

button7 = tk.Button(text='     Add File    ', command=addFile, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 350, window=button7)

button8 = tk.Button(text='     Check Status    ', command=status, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 400, window=button8)

button9 = tk.Button(text='      Commit    ', command=commit, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 450, window=button9)

button10 = tk.Button(text='      Remove    ', command=remove, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 500, window=button10)

button11 = tk.Button(text='      History    ', command=history, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 550, window=button11)

button13 = tk.Button(text='      Login    ', command=login, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(700, 100, window=button13)

button14 = tk.Button(text='      About    ', command=about, bg='#676767', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 600, window=button14)


root.mainloop()
