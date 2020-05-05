import numpy as np
from markov import Markov
from midi_reader import Midi_Reader
from midi_creator import Midi_Creator


def main(file_path, sim_length, dest_path):
	"""
	file_path : location of midi file
	sim_length : number of notes to generate
	dest_path : save location
	"""
	reader = Midi_Reader(file_path)
	note_seq = reader.get_note_sequence()
	dur_seq = reader.get_duration_sequence()

	note_markov, dur_markov = Markov(120), Markov(40)
	# print("note_seq =", note_seq)
	# print("dur_seq =", dur_seq)
	note_markov.set_sampled_matrix(note_seq)
	dur_markov.set_sampled_matrix(dur_seq)
	sim_notes = note_markov.simulate_markov_process(sim_length)
	sim_durs = dur_markov.simulate_markov_process(sim_length)

	creator = Midi_Creator()
	creator.create_mid(sim_notes, sim_durs)
	# print("sim_notes", sim_notes)
	# print("sim_durs", sim_durs)
	creator.save(dest_path)


if __name__ == '__main__':
	main('midi_training_data/telemann_fantasia.mid', 50, 'new_midi.mid')
	print("Job Completed")