import numpy as np
from markov import Markov
from midi_reader import Midi_Reader
from midi_creator import Midi_Creator


def generate_hardcoded(states, matrix, sim_length, dest_path):
	"""
	states : List of playable notes
	matrix : The markov matrix representing transition probabilities
	sim_length : number of notes in the final result
	dest_path : where to save the final result
	"""
	note_markov = Markov()
	note_markov.set_markov_matrix(states, matrix)
	sim_notes = note_markov.simulate_markov_process(sim_length)
	sim_durs = [1 for el in sim_notes]

	creator = Midi_Creator()
	creator.create_mid(sim_notes, sim_durs)
	creator.save(dest_path)


def generate_using_data(file_path, sim_length, dest_path):
	"""
	file_path : location of midi file
	sim_length : number of notes to generate
	dest_path : save location
	"""
	reader = Midi_Reader(file_path)
	note_seq = reader.get_note_sequence()
	dur_seq = reader.get_duration_sequence()

	note_markov, dur_markov = Markov(), Markov()
	note_markov.set_sampled_matrix(note_seq)
	dur_markov.set_sampled_matrix(dur_seq)
	sim_notes = note_markov.simulate_markov_process(sim_length)
	sim_durs = dur_markov.simulate_markov_process(sim_length)

	creator = Midi_Creator()
	creator.create_mid(sim_notes, sim_durs)
	creator.save(dest_path)


C_MAJOR_SCALE = [60, 62, 64, 65, 67, 69, 71, 72]
MAJOR_MARKOV = np.array([[1/5, 1/10, 1/10, 1/5, 1/5, 1/10, 1/30, 1/15],
						[1/4, 1/8, 11/128, 11/128, 1/4, 1/8, 1/64, 1/16],
						[1/6, 1/16, 1/16, 1/5, 1/5, 37/480, 37/240, 37/480],
						[1/4, 1/8, 1/8, 1/16, 1/5, 23/160, 1/64, 5/64],
						[1/5, 1/6, 1/8, 1/16, 1/6, 61/1680, 1/7, 1/10],
						[1/7, 1/6, 1/7, 1/10, 1/6, 1/7, 4/105, 1/10],
						[1/8, 1/32, 1/8, 1/32, 1/8, 1/32, 1/32, 1/2],
						[1/5, 1/10, 1/10, 1/6, 1/5, 1/45, 1/90, 1/5]])

C_MINOR_SCALE = [60, 62, 63, 65, 67, 68, 70, 72]
MINOR_MARKOV = np.array([[1/10, 1/20, 1/5, 1/10, 1/5, 1/5, 1/20, 1/10],
						[11/300, 1/10, 1/4, 1/5, 1/6, 1/50, 1/5, 2/75],
						[1/5, 1/4, 1/10, 1/10, 1/10, 1/8, 1/10, 1/40],
						[1/8, 1/5, 1/8, 1/10, 1/8, 1/5, 1/10, 1/40],
						[1/5, 1/14, 1/14, 1/12, 1/10, 1/4, 1/5, 1/42],
						[1/10, 1/50, 1/8, 1/4, 1/4, 1/10, 21/200, 1/20],
						[1/10, 1/8, 1/8, 1/8, 1/4, 3/40, 1/10, 1/10],
						[1/2, 1/20, 1/10, 1/20, 1/20, 1/20, 1/10, 1/10]])

if __name__ == '__main__':
	generate_using_data('midi_training_data/telemann_fantasia.mid', 100, 'new_midi.mid')
	generate_hardcoded(C_MAJOR_SCALE, MAJOR_MARKOV, 20, 'major_scale_tunes.mid')
	print("Job Completed")
