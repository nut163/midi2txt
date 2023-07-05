import mido
from midi_parser import MIDIParser
from file_handler import FileHandler

class MidiToText:
    def __init__(self, midi_file_path):
        self.midi_file_path = midi_file_path
        self.midi_parser = MIDIParser()
        self.file_handler = FileHandler()

    def convert(self):
        midi_file = mido.MidiFile(self.midi_file_path)
        text_data = self.midi_parser.parse(midi_file)
        text_file_path = self.file_handler.save_text_file(text_data)
        return text_file_path