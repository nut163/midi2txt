import tkinter as tk
from tkinter import filedialog
from midi_to_text import convert_midi_to_text
from text_to_midi import convert_text_to_midi

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.mode_dropdown = tk.OptionMenu(self, tk.StringVar(), "MIDI to text", "Text to MIDI")
        self.mode_dropdown.pack(side="top")

        self.upload_midi_button = tk.Button(self)
        self.upload_midi_button["text"] = "Upload MIDI"
        self.upload_midi_button["command"] = self.upload_midi
        self.upload_midi_button.pack(side="top")

        self.upload_text_button = tk.Button(self)
        self.upload_text_button["text"] = "Upload Text"
        self.upload_text_button["command"] = self.upload_text
        self.upload_text_button.pack(side="top")

        self.convert_button = tk.Button(self)
        self.convert_button["text"] = "Convert"
        self.convert_button["command"] = self.start_conversion
        self.convert_button.pack(side="top")

    def upload_midi(self):
        self.midi_file_path = filedialog.askopenfilename(filetypes=[("MIDI files", "*.midi")])
        print("midi_upload_success")

    def upload_text(self):
        self.text_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        print("text_upload_success")

    def start_conversion(self):
        mode = self.mode_dropdown.get()
        if mode == "MIDI to text":
            convert_midi_to_text(self.midi_file_path)
        elif mode == "Text to MIDI":
            convert_text_to_midi(self.text_file_path)
        print("conversion_success")

root = tk.Tk()
app = Application(master=root)
app.mainloop()