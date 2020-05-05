# To install, simply run 'pip install MIDIUtil'
from midiutil import MIDIFile


class Midi_Creator:
	def __init__(self):
		self.mid = MIDIFile(1)		# Where prospective midi files are stored
		self.track = 0
		self.channel = 0
		self.time = 0
		self.tempo = 140	# in BPM
		self.volume = 100

	def create_mid(self, note_stream, duration_stream, norm = True):
		"""
		Given a list of notes and durations, creates
		and saves a mid file to self.mid with that
		particular sequence of notes and durations.
		note_stream and duration_stream must be of the
		same length.
		"""
		if norm:
			n_constant = 12
		else:
			n_constant = 1
		self.mid.addTempo(self.track, self.time, self.tempo)

		for i, pitch in enumerate(note_stream):
			duration = duration_stream[i]
			# print("duration =", duration)
			self.mid.addNote(self.track, self.channel, pitch,
							self.time, duration/n_constant, self.volume)
			self.time += duration/n_constant

	def get_mid(self):
		"""
		Returns the midi file
		"""
		return self.mid

	def save(self, file_path):
		"""
		Saves the midi file to a designated file_path
		"""
		with open(file_path, 'wb') as output_file:
			self.mid.writeFile(output_file)

if __name__ == '__main__':
	###
	### We test the above implementation
	###
	note_stream = [33, 67, 45, 64, 76, 74, 69, 57, 40, 52, 72]
	duration_stream = [3, 3, 4, 4, 6, 9, 8, 8, 8, 6, 4]
	creator = Midi_Creator()
	creator.create_mid(note_stream, duration_stream)
	creator.save('creator_test.mid')

