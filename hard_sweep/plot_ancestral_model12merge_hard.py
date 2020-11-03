########################################################
###for Figure 2 D-F, just change "additive" to "partial"/"recessive"
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
times=[2,4,8,16,32,64,128,256,512,1000,1500,2000]
out1=[]
out2=[]
out3=[]

for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for l in range(1,11):
		infile=open('admix_MI0.001hard_recessive'+str(hset[run])+'_model2_run'+str(l)+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		polyscore=[]
		polyScore=dict({})
		tempscore=[]
		fitness=[]
		ancestryGenome1=[]
		data=[]

		ind=0
		while ind<len(lines)-1:
			while not lines[ind].startswith('Mutation'):
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60020)
			ind+=1
			tempscore=[]
			while not lines[ind].startswith('Ancestral'):
				ind+=1
			s3=lines[ind].strip('\n').split(' ')
			ances=float(s3[3])
			ancestryGenome1.append(ances)
			ind+=5
		ancestryGenome1=np.array(ancestryGenome1)
		out3.append(ancestryGenome1)
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
	print (len(out3))
	print (len(gen))
	plt.plot(gen,ancestryGenome1,simID[run],linestyle='-.')


for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for l in range(1,11):
		infile=open('admix_MI0.001hard_recessive'+str(hset[run])+'_model1_run'+str(l)+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		polyscore=[]
		polyScore=dict({})
		tempscore=[]
		fitness=[]
		ancestryGenome2=[]
		data=[]

		ind=0
		while ind<len(lines)-1:
			while not lines[ind].startswith('Mutation'):
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60000)
			ind+=5
			tempscore=[]
			while not lines[ind].startswith('Ancestral'):
				ind+=1
			s3=lines[ind].strip('\n').split(' ')
			ances=float(s3[3])
			ancestryGenome2.append(ances)
			ind+=5
		ancestryGenome2=np.array(ancestryGenome2)
		out3.append(ancestryGenome2)
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
	print (len(out3))
	print (len(gen))
	plt.plot(gen,ancestryGenome2,simID[run],linestyle='-',label=str(hset[run])+"%")
legend1=plt.legend(title='Admixture fraction',loc='lower right',bbox_to_anchor=(1.31,0),edgecolor='black')
ax = plt.gca().add_artist(legend1)


l1,=plt.plot(gen,ancestryGenome2,simID[run],linestyle='-',label="model 1")
l2,=plt.plot(gen,ancestryGenome1,simID[run],linestyle='-.',label="model 2")
legend1=plt.legend(handles=[l1,l2],title='Demographic Models',loc='lower right',bbox_to_anchor=(1.34,0.7),edgecolor='black')


plt.xscale('log')
plt.xlim((2,2000))
plt.ylim((0,1.1))
plt.xlabel('Generations after admixture')
plt.ylabel('Recipient population ancestry fraction')
plt.title('Recessive deleterious mutations')
plt.savefig('ancestryGenome_MIhard_recessive_merge.svg',format='svg',bbox_inches = 'tight')
plt.close()
