from random import randint

jobs = [
	(20, 25), 
	(90, 60),
	(80, 75), 
	(20, 30),          #jobs[job_no][machine_no]
	(120, 90),
	(15, 35),
	(65, 50) 
]

m1 = {
	'in' : [],
	'out' : []
}

m2 = {
	'in' : [],
	'out' : []
}

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


