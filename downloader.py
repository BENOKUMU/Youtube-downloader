#Importing libraries
from tkinter import *
from pytube import YouTube

#creating display window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Waves-Youtube Video downloader")

Label(root, text = 'YouTube Video Downloader', font = 'arial 20 bold').pack()


#creating a field to enter link
link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

#function for download
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
