import mido
from mido import Message, MidiFile, MidiTrack
from text_parser import TextParser

class TextToMidi:
    def __init__(self, text_file_path):
        self.text_file_path = text_file_path
        self.text_parser = TextParser()

    def convert(self):
        midi_data = self.text_parser.parse(self.text_file_path)
        midi_file = MidiFile()
        track = MidiTrack()
        midi_file.tracks.append(track)

        for data in midi_data:
            track.append(Message('note_on', note=data['note'], velocity=data['velocity'], time=data['time']))

        return midi_file

    def save_midi_file(self, midi_file, output_path):
        midi_file.save(output_path)