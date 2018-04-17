import sys
import os
from typing import List, Dict
from tkinter import Tk, Label, Button, LEFT, RIGHT
import mp3play

class TheGUI():
    AB_PATH = os.path.abspath(__file__)
    CUR_DIR = os.getcwd()
    LOAD_CONFIG = CUR_DIR + "config.json"

    def __init__(self, master, sound_files):
        self.master = master
        master.title("Simple GUI")

        self.label = Label(master, text="This is our first GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        self.sound_files = sound_files

    def greet(self):
        print("GREETINGS")

    def play_sound(self, the_file):
        the_sound = mp3play.load(the_file)
        play_sound = lambda: the_sound.play()

    def get_all_sound_files(self, dir_name):
        all_sound_files = []
        sound_dir = TheGUI.CUR_DIR + '/' + 'obdm_recent_sounds'
        all_sounds_files = os.listdir(sound_dir)
        for sound_file in all_sounds_files:
            if sound_file.split('.')[1] is 'mp3':
                all_files.append(sound_file)
        self.sound_files = all_sound_files
        return self.sound_files

    def create_sound_buttons(self):
        for file_name in self.sound_files:
            Button(self.master, text=str(file_name), command=self.play_sound(the_file=file_name))
        pass




if __name__ == "__main__":
    #root = Tk()
    #my_gui = TheGUI(root)
    #root.mainloop()

    all_files = os.listdir('C:/Users/maxwem1/cobragit/ESM_ITPA_TOP/ESM_ITPA/maxxwem1_sandbox/machine_learning')
    for i in all_files:
        print("FILE EXT: ", i.split('.')[1])