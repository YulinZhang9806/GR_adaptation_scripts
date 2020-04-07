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
gen=[1,2,4,8,16,32,64,128,256,512,1000,1500,2000]
out1=[]
out2=[]
out3=[]
runset=[3,4,5,6,7,8,9,10]

for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for i in range(0,8):
		infile=open('admix_stabilizing_model1_sqrt3000_additive'+str(hset[run])+'_opt1_run'+str(runset[i])+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		polyscore=[]
		polyScore=dict({})
		tempscore=[]
		fitness=[]
		ancestryGenome=[]
		data=[]
		ind=0
		while ind<len(lines)-5:
			while not lines[ind].startswith('Mutation') and ind<len(lines)-5:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60000)
			ind+=1
	#		print (gen[-1])
			while not lines[ind].startswith('Ancestral') and ind<len(lines)-5:
				ind+=1
			s3=lines[ind].strip('\n').split(' ')
			ances=float(s3[-1])#/7151
			ancestryGenome.append(ances)
			ind+=1
			if gen[-1]==2000:
				ind=len(lines)
		ancestryGenome=np.array(ancestryGenome)
		out1.append(ancestryGenome)
	out1_1=np.array(out1[0:1])
	out1_2=np.array(out1[1:2])
	out1_3=np.array(out1[2:3])
	out1_4=np.array(out1[3:4])
	out1_5=np.array(out1[4:5])
	out1_6=np.array(out1[5:6])
	out1_7=np.array(out1[6:7])
	out1_8=np.array(out1[7:8])
	out1_9=np.array(out1[8:9])
	out1=out1_1+out1_2+out1_3+out1_4+out1_5+out1_6+out1_7+out1_8+out1_9
	out1=out1/9
	out1=list(out1[0])
	print (len(out1))
	print (len(gen))
	plt.plot(gen,out1,simID[run],linestyle=':',label=str(hset[run])+"%")
out1=np.array(out1)
#legend1=plt.legend(title='Admixture fraction',loc='lower right',bbox_to_anchor=(1.31,0),edgecolor='black')
#ax = plt.gca().add_artist(legend1)

runset=[1,3,4,5,6,7,8,9,10]
for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for i in range(0,9):
		infile=open('admix_stabilizing_model1_sqrt3000_additive'+str(hset[run])+'_opt2_run'+str(runset[i])+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		polyscore=[]
		polyScore=dict({})
		tempscore=[]
		fitness=[]
		ancestryGenome=[]
		data=[]
		ind=0
		while ind<len(lines)-5:
			while not lines[ind].startswith('Mutation') and ind<len(lines)-5:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60000)
			ind+=1
	#		print (gen[-1])
			while not lines[ind].startswith('Ancestral') and ind<len(lines)-5:
				ind+=1
			s3=lines[ind].strip('\n').split(' ')
			ances=float(s3[-1])#/7151
			ancestryGenome.append(ances)
			ind+=1
			if gen[-1]==2000:
				ind=len(lines)
		ancestryGenome=np.array(ancestryGenome)
		out2.append(ancestryGenome)
	out2_1=np.array(out2[0:1])
	out2_2=np.array(out2[1:2])
	out2_3=np.array(out2[2:3])
	out2_4=np.array(out2[3:4])
	out2_5=np.array(out2[4:5])
	out2_6=np.array(out2[5:6])
	out2_7=np.array(out2[6:7])
	out2_8=np.array(out2[7:8])
	out2_9=np.array(out2[8:9])
	out2=out2_1+out2_2+out2_3+out2_4+out2_5+out2_6+out2_7+out2_8+out2_9
	out2=out2/9
	out2=list(out2[0])
	print (len(out2))
	print (len(gen))
	plt.plot(gen,out2,simID[run],linestyle='-.')
out2=np.array(out2)

runset=[2,3,5,6,7,8,9,10]
for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for i in range(0,8):
		infile=open('admix_stabilizing_model1_sqrt3000_additive'+str(hset[run])+'_opt5_run'+str(runset[i])+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		polyscore=[]
		polyScore=dict({})
		tempscore=[]
		fitness=[]
		ancestryGenome=[]
		data=[]
		ind=0
		while ind<len(lines)-5:
			while not lines[ind].startswith('Mutation') and ind<len(lines)-5:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			gen.append(float(s1[0])-60000)
			ind+=1
	#		print (gen[-1])
			while not lines[ind].startswith('Ancestral') and ind<len(lines)-5:
				ind+=1
			s3=lines[ind].strip('\n').split(' ')
			ances=float(s3[-1])#/7151
			ancestryGenome.append(ances)
			ind+=1
			if gen[-1]==2000:
				ind=len(lines)
		ancestryGenome=np.array(ancestryGenome)
		out3.append(ancestryGenome)
	out3_1=np.array(out3[0:1])
	out3_2=np.array(out3[1:2])
	out3_3=np.array(out3[2:3])
	out3_4=np.array(out3[3:4])
	out3_5=np.array(out3[4:5])
	out3_6=np.array(out3[5:6])
	out3_7=np.array(out3[6:7])
	out3_8=np.array(out3[7:8])
	out3_9=np.array(out3[8:9])
	out3=out3_1+out3_2+out3_3+out3_4+out3_5+out3_6+out3_7+out3_8+out3_9
	out3=out3/9
	out3=list(out3[0])
	print (len(out3))
	print (len(gen))
	plt.plot(gen,out3,simID[run],linestyle='-')
out3=np.array(out3)


'''
l1,=plt.plot(gen,out1,simID[run],linestyle=':',label="1")
l2,=plt.plot(gen,out2,simID[run],linestyle='-.',label="2")
l3,=plt.plot(gen,out3,simID[run],linestyle='-',label="5")
legend1=plt.legend(handles=[l1,l2,l3],title='p2 optimum',loc='lower right',bbox_to_anchor=(1.33,0.7),edgecolor='black')
'''

plt.title('Additive deleterious mutations')
plt.xscale('log')
plt.ylim((-0.05,1.05))
plt.xlim((3,2000))
plt.xlabel('Generations after admixture')
plt.ylabel('Recipient population ancestry fraction')
plt.savefig('ancestryGenome_stabilizing_model1_sqrt3000_additive_opt1_admix.pdf',format='pdf',bbox_inches = 'tight')
plt.close()
