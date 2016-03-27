from random import randint

jobs = []

fin = open("jobs.txt",'r')

for line in fin:
	split = str.split(line)
	j1 = int(split[0])
	j2 = int(split[1])
	jobs.append((j1,j2))

m1 = {
	'in' : [],
	'out' : []
}

m2 = {
	'in' : [],
	'out' : []
}

#print jobs

def makespan(sequence = []):
	m1['in'] = []
	m1['out'] = []
	m2['in'] = []
	m2['out'] =[]
	enter = 0
	i = 0
	for job_no in sequence:
		m1['in'].append(enter)
		out = enter + jobs[job_no][0]
		m1['out'].append(out)
		enter = out
		i = i + 1
	out = 0
	i = 0
	for job_no in sequence:
		if m1['out'][i] < out:
			enter = out
		else :
			enter = m1['out'][i]
		m2['in'].append(enter)
		out = enter + jobs[job_no][1]
		m2['out'].append(out)
		i = i + 1
	return m2['out'][len(m2['out'])-1]


