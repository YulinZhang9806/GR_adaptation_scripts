########################################################
###for Figure 4 A-C, just change "additive" to "partial"/"recessive"
###change model1/60000 to model2/60020 to reproduce Figure 4 D-F
###set different list 'times' to reproduce Figure S1
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
simID=['purple','blue','green','black']
#times=[2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
times=[2,4,8,16,32,64,128,256,512,1000,1500,2000]
out1=[]
out2=[]
out3=[]

for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for l in range(1,11):
		infile=open('admix_MI0.01hard_additive'+str(hset[run])+'_model1_run'+str(l)+'.out')
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
		while ind<len(lines)-8:
			while not lines[ind].startswith('Mutation'):
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60000)
			ind+=3
			tempscore=[]
			while lines[ind].startswith('"m2'):
				s2=lines[ind].strip('\n').strip('"').split('\t')
				freq=float(s2[1])
				tempscore.append(freq)
				ind+=2
			trait=sum(tempscore)
			polyscore.append(trait)
#		polyscore=np.array(polyscore)
		out3.append(polyscore)
	out3_1=np.array(out3[0:1])
	out3_2=np.array(out3[1:2])
	out3_3=np.array(out3[2:3])
	out3_4=np.array(out3[3:4])
	out3_5=np.array(out3[4:5])
	out3_6=np.array(out3[5:6])
	out3_7=np.array(out3[6:7])
	out3_8=np.array(out3[7:8])
	out3_9=np.array(out3[8:9])
	out3_10=np.array(out3[9:10])
	out3=out3_1+out3_2+out3_3+out3_4+out3_5+out3_6+out3_7+out3_8+out3_9+out3_10
	out3=out3/10
	out3=list(out3[0])
	for t in times:
		t = int(t)
		data1.append(out3[t-1])
	print (len(out3))
	print (len(gen))
	plt.plot(times,data1,simID[run],linestyle='-',label=str(hset[run])+"%")
#legend1=plt.legend(title='Admixture fraction',loc='lower right',bbox_to_anchor=(1.31,0),edgecolor='black')
#ax = plt.gca().add_artist(legend1)

for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for l in range(1,11):
		infile=open('admix_MI0.001hard_additive'+str(hset[run])+'_model1_run'+str(l)+'.out')
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
		while ind<len(lines)-8:
			while not lines[ind].startswith('Mutation'):
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60000)
			ind+=3
			tempscore=[]
			while lines[ind].startswith('"m2'):
				s2=lines[ind].strip('\n').strip('"').split('\t')
				freq=float(s2[1])
				tempscore.append(freq)
				ind+=2
			trait=sum(tempscore)
			polyscore.append(trait)
		out2.append(polyscore)
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
	for t in times:
		t = int(t)
		data2.append(out2[t-1])
	print (len(out2))
	print (len(gen))
	plt.plot(times,data2,simID[run],linestyle='-.')

for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for l in range(1,11):
		infile=open('admix_MI0.0001hard_additive'+str(hset[run])+'_model1_run'+str(l)+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		polyscore=[]
		polyScore=dict({})
		tempscore=[]
		fitness=[]
		ancestryGenome=[]
		data3=[]

		ind=0
		while ind<len(lines)-8:
			while not lines[ind].startswith('Mutation'):
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60000)
			ind+=3
			tempscore=[]
			while lines[ind].startswith('"m2'):
				s2=lines[ind].strip('\n').strip('"').split('\t')
				freq=float(s2[1])
				tempscore.append(freq)
				ind+=2
			trait=sum(tempscore)
			polyscore.append(trait)
#		polyscore=np.array(polyscore)
		out1.append(polyscore)
	out1_1=np.array(out1[0:1])
	out1_2=np.array(out1[1:2])
	out1_3=np.array(out1[2:3])
	out1_4=np.array(out1[3:4])
	out1_5=np.array(out1[4:5])
	out1_6=np.array(out1[5:6])
	out1_7=np.array(out1[6:7])
	out1_8=np.array(out1[7:8])
	out1_9=np.array(out1[8:9])
	out1_10=np.array(out1[9:10])
	out1=out1_1+out1_2+out1_3+out1_4+out1_5+out1_6+out1_7+out1_8+out1_9+out1_10
	out1=out1/10
	out1=list(out1[0])
	for t in times:
		t = int(t)
		data3.append(out1[t-1])
	print (len(out1))
	print (len(gen))
	plt.plot(times,data3,simID[run],linestyle=':')

'''
l1,=plt.plot(times,data1,simID[run],linestyle='-',label="0.01")
l2,=plt.plot(times,data2,simID[run],linestyle='-.',label="0.001")
l3,=plt.plot(times,data3,simID[run],linestyle=':',label="0.0001")
legend1=plt.legend(handles=[l1,l2,l3],title='Selection coefficient',loc='lower right',bbox_to_anchor=(1.33,0.7),edgecolor='black')
'''

plt.xscale('log')
#plt.xticks([2,4,6,8,10,12,14,16,18,20])
plt.ylim((0,1.05))
plt.xlabel('Generations after admixture')
plt.ylabel('Adaptive mutation allele frequency')
plt.title('Additive deleterious mutations')
plt.savefig('AdaptiveMutation_additive_model1.svg',format='svg',bbox_inches = 'tight')
plt.close()

