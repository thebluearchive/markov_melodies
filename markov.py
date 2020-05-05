import numpy as np

class Markov:
	"""
	The Markov class is one representing a sampled
	Markov process
	"""
	def __init__(self):
		self.num_states = None
		self.shape = None
		self.states = {}	#mapping from states to indices
		self.ind_dict = {}	#mapping from indices to states
		self.trans_matrix = None

	def get_trans_prob(self, cur_state, next_state):
		if self.trans_matrix is None:
			print("No transition matrix has been initialized.")
			return None
		else:
			cur_ind = self.states[cur_state]
			next_ind = self.states[next_state]
			return self.trans_matrix[cur_ind, next_ind]

	def set_sampled_matrix(self, arr):
		"""
		Given an array of indices (states), populates
		the markov matrix with the sampled transition
		probabilities.
		"""
		# initialize necessary variables
		for el in arr:
			if el not in self.states:
				self.states[el] = len(self.states)
				self.ind_dict[self.states[el]] = el
		self.num_states = len(self.states)
		self.shape = (self.num_states, self.num_states)
		self.trans_matrix = np.zeros(self.shape)

		# matrix counting number of transitions from i to j
		count = np.zeros(self.shape)
		prev_el = None
		for el in arr:
			if prev_el is not None:
				state = self.states[el]
				prev_state = self.states[prev_el]
				count[prev_state][state] += 1
			prev_el = el
		sum_rows = count.sum(axis = 1, keepdims = True)
		sum_rows[sum_rows == 0] = 1
		self.trans_matrix = count/sum_rows
		# self.trans_matrix[0] = 0	#bad things happen with duration of 0

	def simulate_markov_process(self, k, start_state = None):
		"""
		Simulates a markov process of a desired length k,
		with desired start_state
		Note: start_state must be contained within the dict
		self.states
		"""
		if start_state is None:
			start_ind = np.argmax(self.trans_matrix.sum(axis = 1)) #pick the lowest column with nonzero entires as the start
		else:
			start_ind = self.states[start_state]

		# print("start_ind", start_ind)
		ind_list = [start_ind, ]	# list of indices representing states
		cur_ind = start_ind
		for i in range(k):
			prob = self.trans_matrix[cur_ind]
			if not np.any(prob): # if p is all zeros
				next_ind = np.random.randint(0, high = self.num_states)
			else:
				next_ind = np.random.choice(self.num_states, p = prob)
			ind_list += [next_ind]
			cur_ind = next_ind

		# print("self.states =", self.states)
		# print("ind_list =", ind_list)
		# print("ind_dict =", self.ind_dict)
		return [self.ind_dict[ind] for ind in ind_list]


if __name__ == '__main__':
	###
	### Below, we test the above Markov implementation
	###
	sequence = [1, 2, 3, 4, 1, 1, 2, 2, 4, 3, 4, 3]
	markov = Markov()  # create a represenation with 5 states
	markov.set_sampled_matrix(sequence)
	expected_matrix = np.array([[1/3, 2/3, 0, 0],
								[0, 1/3, 1/3, 1/3],
								[0, 0, 0, 2/2],
								[1/3, 0, 2/3, 0]])
	print(markov.trans_matrix)
	print(expected_matrix)

	print(markov.get_trans_prob(1, 4))
	print(markov.get_trans_prob(2, 4))

	print(markov.simulate_markov_process(10))
