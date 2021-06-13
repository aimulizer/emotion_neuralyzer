from tkinter import *
import pygame
from tkinter import filedialog
import os
import random
import detect_emotion

root = Tk()
root.title("mp3")
root.geometry("800x350")
global pauseState
pauseState=False
# initialising mixer
pygame.mixer.init()

dir = '/home/aimulizer/Desktop/mp3/songs/'
# add song function
def song_to_song_box(song):
    # song=song.replace("/home/aimulizer/Desktop/mp3/songs/","")
    # song=song.replace(".wav","")
    song_box.insert(END,song)
def add_songs():
    songs_dialog = Tk()
    songs_dialog.title("songs")
    mood = detect_emotion.mood()
    songs=os.listdir(f'{dir}/{mood}')
    random.shuffle(songs)
    songs=songs[:5]
    # s1=songs[0]
    s1 = f'{mood}/{songs[0]}'
    s1 = s1.replace(".wav","")
    song1 = Button(songs_dialog,text=s1,fg='green',bg='black',activebackground='gray',activeforeground='black',command= lambda:  [song_to_song_box(s1),songs_dialog.destroy()])
    # s2=songs[1]
    s2 = f'{mood}/{songs[1]}'
    s2 = s2.replace(".wav","")
    song2 = Button(songs_dialog,text=s2,fg='green',bg='black',activebackground='gray',activeforeground='black',command= lambda:  [song_to_song_box(s2),songs_dialog.destroy()])
    # s3= songs[2]
    s3 = f'{mood}/{songs[2]}'
    s3 = s3.replace(".wav","")
    song3 = Button(songs_dialog,text=s3,fg='green',bg='black',activebackground='gray',activeforeground='black',command= lambda:  [song_to_song_box(s3),songs_dialog.destroy()])
    # s4 = songs[3]
    s4 = f'{mood}/{songs[3]}'
    s4 = s4.replace(".wav","")
    song4 = Button(songs_dialog,text=s4,fg='green',bg='black',activebackground='gray',activeforeground='black',command= lambda:  [song_to_song_box(s4),songs_dialog.destroy()])
    # s5=songs[4]
    s5 = f'{mood}/{songs[4]}'
    s5 = s5.replace(".wav","")
    song5 = Button(songs_dialog,text=s5,fg='green',bg='black',activebackground='gray',activeforeground='black',command= lambda:  [song_to_song_box(s5),songs_dialog.destroy()])
    
    song1.grid(row=0,column=0,columnspan=2)
    song2.grid(row=1,column=0,columnspan=2)
    song3.grid(row=2,column=0,columnspan=2)
    song4.grid(row=3,column=0,columnspan=2)
    song5.grid(row=4,column=0,columnspan=2)
    
    # song_box.insert(END,song)
    songs_dialog.mainloop()
def play():
    song = song_box.get(ACTIVE)
    song = f"songs/{song}.wav"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # song_box.selection_clear(ACTIVE)
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
def pause(is_paused):
    global pauseState
    pauseState=is_paused
    if pauseState:
        pygame.mixer.music.unpause()
        pauseState=False
    else:
        pygame.mixer.music.pause()
        pauseState=True
# def manually_add_song():
#     song = filedialog.askopenfilename(initialdir='/home/aimulizer/Desktop/mp3/songs/',title='choose a song',filetypes=(("wav files","*.wav"),))
#     print(song)
if __name__ == "__main__":
    # create playlist box
    song_box = Listbox(root,bg='black',fg='green',height=20,width=100)
    song_box.pack(padx=40,pady=20)
    # creating player buttons
    back_btn_image = PhotoImage(file="buttons/previous-track-button.png")
    forward_btn_image = PhotoImage(file="buttons/play-and-pause-button.png")
    play_btn_image =PhotoImage(file="buttons/play-button.png")
    pause_btn_image = PhotoImage(file="buttons/pause.png")
    stop_btn_image = PhotoImage(file="buttons/stop-button.png")

    # creating player control frame
    control_frame = Frame(root)
    control_frame.pack()

    # creating buttons for player
    back_button = Button(control_frame,image=back_btn_image,borderwidth=0)
    forward_button = Button(control_frame,image=forward_btn_image,borderwidth=0)
    play_button = Button(control_frame,image=play_btn_image,borderwidth=0,command=play)
    pause_button = Button(control_frame,borderwidth=0,image=pause_btn_image,command= lambda: pause(pauseState))
    stop_button = Button(control_frame,image=stop_btn_image,borderwidth=0,command=stop)

    # placing buttons
    back_button.grid(row=0,column=1,padx=10)
    forward_button.grid(row=0,column=3,padx=10)
    play_button.grid(row=0,column=2,padx=10)
    pause_button.grid(row=0,column=0,padx=10)
    stop_button.grid(row=0,column=4,padx=10)


    # creating  menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # adding tabs to menu
    add_song = Menu(my_menu)
    my_menu.add_cascade(label="Add Song",menu=add_song,activeforeground='black',activebackground='gray')
    add_song.add_command(label="add one mood song to playlist",command=add_songs,activebackground='gray',activeforeground='black')
    # add_song.add_command(label="manually add song",activebackground='gray',activeforeground='black',command=manually_add_song)

    root.mainloop()