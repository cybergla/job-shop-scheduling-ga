from calc_makespan import jobs, m1, m2, makespan

L1 = []
L2 = []

J1 = []
J2 = []

for x in jobs:
	J1.append(x[0])
	J2.append(x[1])


for x in xrange(len(jobs)):
	minJob1 = min(J1)
	minJob2 = min(J2)

	i_minJob1 = J1.index(minJob1)
	i_minJob2 = J2.index(minJob2)

	if minJob1 < minJob2:
		L1.append(jobs.index((minJob1,J2[i_minJob1])))
		J2.remove(J2[i_minJob1])
		J1.remove(minJob1)
	else:
		L2.append(jobs.index((J1[i_minJob2],minJob2)))
		J1.remove(J1[i_minJob2])
		J2.remove(minJob2)

L2.reverse()
L1.extend(L2)

print L1



	