import os
from tkinter import filedialog
from tkinter import Tk

class FileHandler:
    def __init__(self):
        self.midi_file_path = None
        self.text_file_path = None

    def upload_midi(self):
        Tk().withdraw() 
        self.midi_file_path = filedialog.askopenfilename(filetypes=[("MIDI files", "*.midi")])
        if self.midi_file_path:
            print("midi_upload_success")
        return self.midi_file_path

    def upload_text(self):
        Tk().withdraw() 
        self.text_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.text_file_path:
            print("text_upload_success")
        return self.text_file_path

    def save_text(self, text_data, filename):
        with open(filename, 'w') as f:
            f.write(text_data)
        print("Text file saved successfully.")

    def save_midi(self, midi_data, filename):
        with open(filename, 'wb') as f:
            f.write(midi_data)
        print("MIDI file saved successfully.")