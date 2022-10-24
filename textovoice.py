from gtts import gTTS
import os
import pygame


from tkinter import *
from tkinter import ttk
from turtle import color
from PIL import ImageTk, Image

import subprocess


root = Tk()
root.title('Text to Voice Converter')
root.geometry('285x400')
# root['bg'] = 'white' 


pygame.mixer.init()


# Language selection:

gtlang = {
    "English": "en",
    "French": "fr",
    "German": "de"
}
langs = list(gtlang.keys())

def sectinglang():
    s_lng = drop.get()
    return s_lng


drop = ttk.Combobox( value=langs)
drop.current(0)
drop.grid(column=0, row=1, pady=20, padx=10)


# ===========================================

def callback(event):

    root.after(50, select_all, event.widget)

def select_all(widget):
    # select text
    widget.select_range(0, 'end')
    # move cursor to the end
    widget.icursor('end')



un_entry = Entry(root, font=('Helvetica', 12), width=30, fg="#336d92", bd=0)
un_entry.grid(column=0, row=0, pady=20, padx=20)
un_entry.bind('<Control-a>', callback)



def createbtn():
    mytext = un_entry.get()
    #mytext = "Hi, this is an example of converting text to audio. This is a bot speaking here, not a real human!"
    # audio = gTTS(text=mytext, --nocheck , slow=False)
    audio = gTTS(text=mytext, lang=gtlang[sectinglang()], slow=False)
    audio.save("example.mp3")
    music_path = os.getcwd()
    pygame.mixer.music.load(f"{music_path}/example.mp3")
    pygame.mixer.music.play(loops = 0)



img_connect_btn = PhotoImage(file='create.png')
img_connect_label = Label(image=img_connect_btn)



create_wifi_btn = Button(root, image=img_connect_btn, borderwidth=0, command=createbtn)
create_wifi_btn.grid(column=0, row=2, pady=20)


copyright_label = Label(root, text='\u00A9 2022 Pooria Danaeifar, All rights reserved.', font=('Helvica',7))
copyright_label.grid(column=0, row=3, pady=30)


root.mainloop()
