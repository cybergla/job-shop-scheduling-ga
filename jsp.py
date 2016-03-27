from random import randint, random
from calc_makespan import jobs, m1, m2, makespan


def individual(length):
	'Create a random sequence of given length.'
	sequence = []
	while len(sequence) < length:
		x = randint(0,length-1)
		if sequence.count(x) == 0:
			sequence.append(x)
	return sequence

def population(count,length):
	"""
	Create a number of individuals

	count: number of individuals
	length: length of the sequences

	"""

	return [ individual(length) for x in xrange(count)]

def fitness(individual):
	"""
	Determine the fitness of an individual. Lower is better.

	"""
	return makespan(individual)

def grade(population):
	'Find average fitness for a population'
	Sum = 0
	for x in population:
		Sum = Sum + fitness(x)
	return Sum / (len(population) * 1.0)

def evolve(population, retain=0.2, random_select=0.05, mutate=0.01):
	"""
	Evolve a population based on some parameters

	"""

	graded = [(fitness(x), x) for x in population]   #Make an ordered pair of (fitness_of_individual, individual)
	graded = [ x[1] for x in sorted(graded)] 		 #Sort the list and remove fitness info
	retain_length = int(len(graded)*retain)
	parents = graded[:retain_length] 				 #Select few fittest members

	# randomly add other individuals to promote genetic diversity
	for individual in graded[retain_length:]:
		if random_select > random():
		    parents.append(individual)

    # mutate some individuals
	for individual in parents:
		if mutate > random():
			pos1 = randint(0, len(individual)-1)
			pos2 = randint(0, len(individual)-1)		#Swap two positions in the sequence
			while pos2 == pos1:
				pos2 = randint(0, len(individual)-1)
			individual[pos1], individual[pos2] = individual[pos2], individual[pos1]

    # crossover parents to create children
	parents_length = len(parents)
	desired_length = len(population) - parents_length
	children = []
	while len(children) < desired_length:
		male = randint(0, parents_length-1)
		female = randint(0, parents_length-1)
		if male != female:
			male = parents[male]
			female = parents[female]
			half = len(male) / 2
			child = male[:half]
			for x in female:
				if child.count(x) == 0:
					child.append(x)
			children.append(child)

	parents.extend(children)
	return parents

p_count = 100
i_length = 7

p = population(p_count,i_length)
fitness_history = [grade(p),]

for i in xrange(100):
	p = evolve(p)
	fitness_history.append(grade(p))

for datum in fitness_history:
	print datum

seq = p[len(p)-1]
for x in xrange(len(seq)):
	seq[x] = seq[x] + 1

print seq
print m2




