```python
import mido

class TextParser:
    def __init__(self, text_file_path):
        self.text_file_path = text_file_path

    def parse_text(self):
        with open(self.text_file_path, 'r') as file:
            lines = file.readlines()

        midi_data = []
        for line in lines:
            data = line.strip().split(',')
            midi_data.append(mido.Message.from_str(data))

        return midi_data

    def write_to_midi(self, midi_data, output_path):
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)

        for msg in midi_data:
            track.append(msg)

        mid.save(output_path)
```