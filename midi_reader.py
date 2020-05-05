#
#	Module for experimenting with and implementing
#	the midi reader using music21
#
from music21 import *

class Midi_Reader:
	def __init__(self, file_path):
		self.score = converter.parse(file_path)

	def get_note_sequence(self):
		"""
		Returns a sequence of midi note values
		"""
		seq = []
		for el in self.score.recurse().notes:
			if isinstance(el, note.Note):
				seq.append(el.pitch.midi)
		return seq

	def get_duration_sequence(self):
		"""
		Returns a sequence of integer valued durations
		"""
		seq = []
		for el in self.score.recurse().notes:
			if isinstance(el, note.Note):
				seq.append(el.duration.quarterLength)
		return seq


if __name__ == '__main__':
	#
	# Tests the implementation of MidiReader above
	#
	reader = Midi_Reader('midi_training_data/canon.mid')
	print(reader.get_note_sequence())
	dur_seq = reader.get_duration_sequence()
