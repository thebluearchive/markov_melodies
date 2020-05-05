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

	def get_duration_sequence(self, norm=True):
		"""
		Returns a sequence of integer valued durations
		normalization attempts to make the durations
		integer-valued. Duration of 1 is 1/12 of a quarter
		note.
		"""
		if norm:
			n_constant = 12
		else:
			n_constant = 1
		seq = []
		for el in self.score.recurse().notes:
			if isinstance(el, note.Note):
				seq.append(int(el.duration.quarterLength*n_constant))
		return seq


if __name__ == '__main__':
	#
	# Tests the implementation of MidiReader above
	#
	reader = Midi_Reader('fur_elise.mid')
	# print(reader.get_note_sequence())
	dur_seq = reader.get_duration_sequence()
