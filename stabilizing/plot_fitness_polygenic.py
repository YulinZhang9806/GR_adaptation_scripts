########################################################
###for Figure S10 D-F, just change "additive" to "partial"/"recessive"
###change model2/60020 to model1/60000 to reproduce Figure S10 A-C
###use the direct output of SLiM as input (e.g. .out file in './slim script.slim > script.out')
########################################################

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
hset=[0,0.1,1,10]
simID=['purple','blue','green','black']
times=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,32,64,128,256,512,1000,1500,2000]
out1=[]
out2=[]
out3=[]
runset=[1,2,3,4,5,6,7,8,9,10]

for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for i in range(0,10):
		infile=open('admix_stabilizing_model2_sqrt3000_additive'+str(hset[run])+'_opt1_run'+str(runset[i])+'.out')
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
		while ind<len(lines)-2:
			while not lines[ind].startswith('Mean phenotype') and ind<len(lines)-1:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60020)
			ind+=1
			while not lines[ind].startswith('"Fitness') and ind<len(lines)-1:
				ind+=1
			s4=lines[ind].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			s5=lines[ind+1].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			nean=float(s4[3])
	#			print(s5)
	#			print(s5[-1])
			human=float(s5[3])
			relFitness=nean/human
			fitness.append(relFitness)
			ind+=1
		fitness=np.array(fitness)
		out1.append(fitness)
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
	print (len(out1))
	print (len(gen))
	for t in times:
		t = int(t)
		data1.append(out1[t-1])
	
	plt.plot(times,data1,simID[run],linestyle=':',label=str(hset[run])+"%")
#legend1=plt.legend(title='Admixture fraction',loc='lower right',bbox_to_anchor=(1.31,0),edgecolor='black')
#ax = plt.gca().add_artist(legend1)


for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for i in range(0,10):
		infile=open('admix_stabilizing_model2_sqrt3000_additive'+str(hset[run])+'_opt2_run'+str(runset[i])+'.out')
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
		while ind<len(lines)-2:
			while not lines[ind].startswith('Mean phenotype') and ind<len(lines)-1:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60020)
			ind+=1
			while not lines[ind].startswith('"Fitness') and ind<len(lines)-1:
				ind+=1
			s4=lines[ind].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			s5=lines[ind+1].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			nean=float(s4[3])
	#			print(s5)
	#			print(s5[-1])
			human=float(s5[3])
			relFitness=nean/human
			fitness.append(relFitness)
			ind+=1
		fitness=np.array(fitness)
		out3.append(fitness)
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
	for t in times:
		t = int(t)
		data2.append(out3[t-1])
	
	plt.plot(times,data2,simID[run],linestyle='-.')


for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for i in range(0,10):
		infile=open('admix_stabilizing_model2_sqrt3000_additive'+str(hset[run])+'_opt5_run'+str(runset[i])+'.out')
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
		while ind<len(lines)-2:
			while not lines[ind].startswith('Mean phenotype') and ind<len(lines)-1:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60020)
			ind+=1
			while not lines[ind].startswith('"Fitness') and ind<len(lines)-1:
				ind+=1
			s4=lines[ind].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			s5=lines[ind+1].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			nean=float(s4[3])
	#			print(s5)
	#			print(s5[-1])
			human=float(s5[3])
			relFitness=nean/human
			fitness.append(relFitness)
			ind+=1
		fitness=np.array(fitness)
		out3.append(fitness)
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
	for t in times:
		t = int(t)
		data3.append(out3[t-1])
	
	plt.plot(times,data3,simID[run],linestyle='-')

'''
l1,=plt.plot(times,data1,simID[run],linestyle='-',label="1")
l2,=plt.plot(times,data2,simID[run],linestyle='-.',label="2")
l3,=plt.plot(times,data3,simID[run],linestyle=':',label="5")
legend1=plt.legend(handles=[l1,l2,l3],title='p2 optimum',loc='lower right',bbox_to_anchor=(1.33,0.7),edgecolor='black')
'''


plt.title('Additive deleterious mutations')
plt.xscale('log')
#plt.xlim((44001,60020))
plt.ylim((-0.05,1))
plt.xlabel('Generations after admixture')
plt.ylabel('Hybrid fitness')
plt.savefig('fitness_stabilizing_model2_sqrt3000_additive_opt1_admix_1.pdf',format='pdf')
plt.close()
