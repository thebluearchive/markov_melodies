import numpy as np

class Markov:
	"""
	The Markov class is one representing a sampled
	Markov process
	"""
	def __init__(self, num_states):
		self.num_states = num_states
		self.shape = (num_states, num_states)
		self.trans_matrix = np.zeros(self.shape)

	def set_trans_prob(self, cur_state, next_state, prob):
		"""
		Sets the probability of transitioning from
		cur_state to next_state equal to prob.
		"""
		self.trans_matrix[cur_state. next_state] = prob

	def get_trans_prob(self, cur_state, next_state):
		return self.trans_matrix[cur_state, next_state]

	def set_sampled_matrix(self, arr):
		"""
		Given an array of indices (states), populates
		the markov matrix with the sampled transition
		probabilities.
		"""
		# matrix counting number of transitions from i to j
		count = np.zeros(self.shape)
		prev_note = None
		for note in arr:
			if prev_note is not None:
				count[prev_note][note] += 1
			prev_note = note
		sum_rows = count.sum(axis = 1, keepdims = True)
		sum_rows[sum_rows == 0] = 1
		self.trans_matrix = count/sum_rows
		self.trans_matrix[0] = 0	#bad things happen with duration of 0

	def simulate_markov_process(self, k, start_state = None):
		"""
		Simulates a markov process of a desired length k,
		with desired start_state
		"""
		if start_state == None:
			start_state = np.argmax(self.trans_matrix.sum(axis = 1)) #pick the lowest column with nonzero entires as the start

		state_list = [start_state, ]	# simulation to be returned
		cur_state = start_state
		for i in range(k):
			prob = self.trans_matrix[cur_state]
			if not np.any(prob): # if p is all zeros
				next_state = np.random.randint(0, high = self.num_states)
			else:
				next_state = np.random.choice(self.num_states, p = prob)
			state_list += [next_state]
			cur_state = next_state
		return state_list


if __name__ == '__main__':
	###
	### Below, we test the above Markov implementation
	###
	sequence = [1, 2, 3, 4, 1, 1, 2, 2, 4, 3, 4, 3]
	markov = Markov(5)  # create a represenation with 5 states
	markov.set_sampled_matrix(sequence)
	expected_matrix = np.array([[0, 0, 0, 0, 0],
								[0, 1/3, 2/3, 0, 0],
								[0, 0, 1/3, 1/3, 1/3],
								[0, 0, 0, 0, 2/2],
								[0, 1/3, 0, 2/3, 0]])
	print(markov.trans_matrix)
	print(expected_matrix)
