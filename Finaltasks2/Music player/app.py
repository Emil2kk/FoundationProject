
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
music_player=tkr.Tk()
music_player.title("Mahni oxuyan")
music_player.geometry("500x340")

directory=askdirectory()
os.chdir(directory)
songlist=os.listdir()

playlist=tkr.Listbox(music_player, font="Verdona 12 bold",fg="navy",bg="green",selectmode=tkr.SINGLE)

x=0
for i in songlist:
    playlist.insert(x,i)
    x+=1
    
    
pygame.init()
pygame.mixer.init()

def oxuma():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
def OXuma():
    pygame.mixer.music.stop()
    
def Dayan():
    pygame.mixer.music.pause()
    
    
def dayanma():
    pygame.mixer.music.unpause()
    
    
button1=tkr.Button(music_player,width=5,height=3,font="verona 12 bold" ,text="OXu " ,command=oxuma ,bg="navy",fg="blue"  )
    
button2=tkr.Button(music_player,width=5,height=3,font="verona 12 bold" ,text="OXu " ,command=OXuma ,bg="navy",fg="blue"  )

button3=tkr.Button(music_player,width=5,height=3,font="verona 12 bold" ,text="OXu " ,command=Dayan ,bg="navy",fg="blue"  )

button4=tkr.Button(music_player,width=5,height=3,font="verona 12 bold" ,text="OXu " ,command=dayanma,bg="navy",fg="blue"  )



var=tkr.StringVar()
song_title=tkr.Label(music_player, font="Verdona 12 bold" ,textvariable=var)

song_title.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")

playlist.pack(fill="both",expand="yes")

music_player.mainloop()