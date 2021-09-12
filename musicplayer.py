import tkinter as tkr
from tkinter.filedialog import askdirectory
import pygame
import os

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def ExitMusicPlayer():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def resume():
    pygame.mixer.music.unpause()

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x350")
directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font ="Cambria 14 bold", bg="cyan2", selectmode = tkr.SINGLE)
for item in songlist:
    pos=0
    playlist.insert(pos, item)
    pos = pos + 1


pygame.init()
pygame.mixer.init()
Button1 = tkr.Button(musicplayer, width=5, height=3, font="Cambria 20 bold", text="Play Music", command=play, bg="lime green", fg="black")

Button2 = tkr.Button(musicplayer, width=5,height=3, font="Cambria 20 bold", text="Stop Music", command=ExitMusicPlayer, bg="red",fg="black")
Button3 = tkr.Button(musicplayer, width=5,height=3, font="Cambria 16 bold", text="Pause Music", command=pause, bg="yellow", fg="black")
Button4 = tkr.Button(musicplayer, width=5,height=3, font="Cambria 16 bold", text="Resume Music", command=resume, bg="skyblue", fg="black")
var = tkr.StringVar()
songtitle = tkr.Label(musicplayer,font="Helvetica 12 bold", textvariable=var)
songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")
musicplayer.mainloop()

