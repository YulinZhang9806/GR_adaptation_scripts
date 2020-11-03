########################################################
###for Figure 7 A
###change model1/60000 to model2/60020 to reproduce Figure 7 B
###change input files to stabilizing selection outputs to reproduce Figure 7 C-D
###use the direct output of SLiM as input (e.g. .out file in './slim script.slim > script.out')
########################################################

import numpy as np
from math import exp
from copy import deepcopy
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from scipy.stats import gaussian_kde
from numpy import arange

from numpy import mean
from numpy import median
from numpy import var
from math import exp
hset=[0,0.1,1,10]
mutset=['additive','partial','recessive']
colorset1=['black','mediumblue','cornflowerblue']
colorset2=['purple','blueviolet','thistle']
times=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,32,64,128,256,512,1000,1500,2000]
out1=[]
out2=[]
out3=[]

for run in range(0,3):
	out1=[]
	out2=[]
	out3=[]
	for l in range(1,11):
		infile=open('admix_MI0.01hard_'+str(mutset[run])+'0_model1_run'+str(l)+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		polyscore=[]
		polyScore=dict({})
		tempscore=[]
		fitness=[]
		ancestryGenome=[]
		data2=[]

		ind=0
		while ind<len(lines)-3:
			while not lines[ind].startswith('Mutation'):
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60000)
			ind+=1
			tempscore=[]
			while not lines[ind].startswith('"Fitness'):
				ind+=1
			s4=lines[ind].strip('\n').strip('"').split(' ')
			s5=lines[ind+1].strip('\n').strip('"').split(' ')
			nean=float(s4[3])
			human=float(s5[3])
			relFitness=nean/human
			fitness.append(relFitness)
			ind+=3
		fitness=np.array(fitness)
		out2.append(fitness)
	out2_1=np.array(out2[0:1])
	out2_2=np.array(out2[1:2])
	out2_3=np.array(out2[2:3])
	out2_4=np.array(out2[3:4])
	out2_5=np.array(out2[4:5])
	out2_6=np.array(out2[5:6])
	out2_7=np.array(out2[6:7])
	out2_8=np.array(out2[7:8])
	out2_9=np.array(out2[8:9])
	out2_10=np.array(out2[9:10])
	out2=out2_1+out2_2+out2_3+out2_4+out2_5+out2_6+out2_7+out2_8+out2_9+out2_10
	out2=out2/10
	out2=list(out2[0])
	print (len(out2))
	print (len(gen))
	for t in times:
		t = int(t)
		data2.append(out2[t-1])
	
	plt.plot(times,data2,colorset2[run],linestyle='-',label='m=0%,'+str(mutset[run]))



for run in range(0,3):
	out1=[]
	out2=[]
	out3=[]
	for l in range(1,11):
		infile=open('admix_MI0.01hard_'+str(mutset[run])+'1_model1_run'+str(l)+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		polyscore=[]
		polyScore=dict({})
		tempscore=[]
		fitness=[]
		ancestryGenome=[]
		data1=[]

		ind=0
		while ind<len(lines)-3:
			while not lines[ind].startswith('Mutation'):
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60000)
			ind+=1
			tempscore=[]
			while not lines[ind].startswith('"Fitness'):
				ind+=1
			s4=lines[ind].strip('\n').strip('"').split(' ')
			s5=lines[ind+1].strip('\n').strip('"').split(' ')
			nean=float(s4[3])
			human=float(s5[3])
			relFitness=nean/human
			fitness.append(relFitness)
			ind+=3
		fitness=np.array(fitness)
		out2.append(fitness)
	out2_1=np.array(out2[0:1])
	out2_2=np.array(out2[1:2])
	out2_3=np.array(out2[2:3])
	out2_4=np.array(out2[3:4])
	out2_5=np.array(out2[4:5])
	out2_6=np.array(out2[5:6])
	out2_7=np.array(out2[6:7])
	out2_8=np.array(out2[7:8])
	out2_9=np.array(out2[8:9])
	out2_10=np.array(out2[9:10])
	out2=out2_1+out2_2+out2_3+out2_4+out2_5+out2_6+out2_7+out2_8+out2_9+out2_10
	out2=out2/10
	out2=list(out2[0])
	print (len(out2))
	print (len(gen))
	for t in times:
		t = int(t)
		data1.append(out2[t-1])
	
	plt.plot(times,data1,colorset1[run],linestyle='-',label='m=1%,'+str(mutset[run]))

'''
legend1=plt.legend(title='  Admixture_fraction/\nDeleterious_mutations',loc='lower right',bbox_to_anchor=(1.36,0),edgecolor='black')
ax = plt.gca().add_artist(legend1)

l1,=plt.plot(times,data1,colorset1[run],linestyle='-',label="0.01")
l2,=plt.plot(times,data2,colorset1[run],linestyle='-.',label="0.001")
l3,=plt.plot(times,data3,colorset1[run],linestyle=':',label="0.0001")
legend1=plt.legend(handles=[l1,l2,l3],title='Selection coefficient',loc='lower right',bbox_to_anchor=(1.33,0.7),edgecolor='black')
'''

plt.xscale('log')
plt.xlabel('Generations after admixture')
plt.ylabel('Hybrid fitness')
plt.title('Demographic Model 1')
plt.savefig('fitness_MIhard_model1_admix.svg',format='svg',bbox_inches = 'tight')
plt.close()