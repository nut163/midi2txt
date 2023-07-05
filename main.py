```python
import tkinter as tk
from tkinter import filedialog
from ui import UI
from file_handler import FileHandler
from midi_to_text import MidiToText
from text_to_midi import TextToMidi

class MainApp:
    def __init__(self):
        self.ui = UI()
        self.file_handler = FileHandler()
        self.midi_to_text = MidiToText()
        self.text_to_midi = TextToMidi()

        self.ui.upload_midi_button.config(command=self.upload_midi)
        self.ui.upload_text_button.config(command=self.upload_text)
        self.ui.convert_button.config(command=self.start_conversion)
        self.ui.mode_dropdown.config(command=self.select_mode)

    def upload_midi(self):
        midi_file_path = filedialog.askopenfilename()
        self.file_handler.midi_file_path = midi_file_path
        self.ui.show_message("midi_upload_success")

    def upload_text(self):
        text_file_path = filedialog.askopenfilename()
        self.file_handler.text_file_path = text_file_path
        self.ui.show_message("text_upload_success")

    def select_mode(self):
        self.mode = self.ui.get_selected_mode()

    def start_conversion(self):
        if self.mode == "MIDI to text":
            self.midi_to_text.convert(self.file_handler.midi_file_path)
            self.ui.show_message("conversion_success")
        elif self.mode == "Text to MIDI":
            self.text_to_midi.convert(self.file_handler.text_file_path)
            self.ui.show_message("conversion_success")

if __name__ == "__main__":
    app = MainApp()
    tk.mainloop()
```