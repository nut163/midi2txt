import mido
from mido import MidiFile

class MIDIParser:
    def __init__(self, midi_file_path):
        self.midi_file_path = midi_file_path

    def parse_midi(self):
        midi_data = []
        midi_file = MidiFile(self.midi_file_path)

        for track in midi_file.tracks:
            for msg in track:
                midi_data.append(str(msg))

        return midi_data

    def convert_to_text(self, midi_data):
        text_data = '\n'.join(midi_data)
        return text_data