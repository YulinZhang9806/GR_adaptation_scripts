import numpy as np
from math import exp
from copy import deepcopy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from scipy.stats import gaussian_kde
from numpy import arange

from numpy import mean
from numpy import median
from numpy import var
from math import exp

infile=open('/space/s1/yulin/stabilizing_mut/admix_sqrt3000_model2_partial10_opt5_run4.out')
lines=infile.readlines()
infile.close()

times1=[0,1,5000,10000,15000,20000,25000,30000,45000,50000,55000,60000]
times2=[44000,44001,45000,46000,47000,48000,49000,50000,51000,52000,53000,54000,55000,56000,57000,58000,59000,60000]
gen=[]
p1_mutations=dict({})
p2_mutations=dict({})
new_mutations=dict({})
position44000=[]
p2_position44000=[]
effect44000=[]
p2_effect44000=[]
p2_specific=[]
p1_specific=[]
new=[]

ind=0
while not lines[ind].startswith('p2'):
	ind+=1
ind+=2
while not lines[ind].startswith('p1'):
	s=lines[ind].strip('\n').strip('\t').split('\t')
	p2_mutations[str(s[0])]=float(s[2])
	ind+=1
ind+=2
while not lines[ind].startswith('"Average'):
	s1=lines[ind].strip('\n').strip('\t').split('\t')
	if str(s1[0]) in p2_mutations.keys():
		ind+=1
	else:
		p1_mutations[str(s1[0])]=float(s1[2])
		ind+=1
l=1
while ind<len(lines)-1:
	while not lines[ind].startswith('p2') and ind<len(lines)-1:
		ind+=1
	ind+=3
	p2_mut=[]
	p1_mut=[]
	new_mut=[]
	p2_temp=[]
	p1_temp=[]
	new_temp=[]
	if ind<len(lines)-1:
		if l==100:
			while not lines[ind].startswith('p1') and ind<len(lines)-1:
				s2=lines[ind].strip('\n').strip('\t').split('\t')
				if str(s2[0]) in p2_mutations.keys():
					if str(s2[0]) in p2_mut:
						h=0
					else:
						p2_mut.append(str(s2[0]))
						freq=float(s2[1])
						effect=p2_mutations[str(s2[0])]
						h=2*freq*(1-freq)*(effect**2)
						p2_temp.append(h)
				elif str(s2[0]) in p1_mutations.keys():
					if str(s2[0]) in p1_mut:
						h=0
					else:
						p1_mut.append(str(s2[0]))
						freq=float(s2[1])
						effect=p1_mutations[str(s2[0])]
						h=2*freq*(1-freq)*(effect**2)
						p1_temp.append(h)
				else:
					if str(s2[0]) in new_mut:
						h=0
					else:
						new_mut.append(str(s2[0]))
						freq=float(s2[1])
						effect=float(s2[2])
						h=2*freq*(1-freq)*(effect**2)
						new_temp.append(h)
				ind+=1
		else:
			while not lines[ind].startswith('Fitness') and ind<len(lines)-1:
				s2=lines[ind].strip('\n').strip('\t').split('\t')
				if str(s2[0]) in p2_mutations.keys():
					if str(s2[0]) in p2_mut:
						h=0
					else:
						p2_mut.append(str(s2[0]))
						freq=float(s2[1])
						effect=p2_mutations[str(s2[0])]
						h=2*freq*(1-freq)*(effect**2)
						p2_temp.append(h)
				elif str(s2[0]) in p1_mutations.keys():
					if str(s2[0]) in p1_mut:
						h=0
					else:
						p1_mut.append(str(s2[0]))
						freq=float(s2[1])
						effect=p1_mutations[str(s2[0])]
						h=2*freq*(1-freq)*(effect**2)
						p1_temp.append(h)
				else:
					if str(s2[0]) in new_mut:
						h=0
					else:
						new_mut.append(str(s2[0]))
						freq=float(s2[1])
						effect=float(s2[2])
						h=2*freq*(1-freq)*(effect**2)
						new_temp.append(h)
				ind+=1			
		if not p2_temp:
			h1_sum=0
		else:
			h1_sum=sum(p2_temp)
		if not p1_temp:
			h2_sum=0
		else:
			h2_sum=sum(p1_temp)
		if not new_temp:
			h3_sum=0
		else:
			h3_sum=sum(new_temp)
		p2_specific.append(float(h1_sum))
		p1_specific.append(float(h2_sum))
		new.append(float(h3_sum))
		gen.append(l)
		l+=1
print(gen)
print(p1_specific)
print(p2_specific)
print(new)
output='p2_specific:\n'
for i in p2_specific:
	output+=str(i)+','
output+='\np1_specific:\n'
for i in p1_specific:
	output+=str(i)+','
output+='\nnew:\n'
for i in new:
	output+=str(i)+','
output+='\n'
outfile1=open('/space/s1/yulin/stabilizing_mut/data/admix_sqrt3000_model2_partial10_opt5_run4.txt','w')
outfile1.write(output)
outfile1.close()
