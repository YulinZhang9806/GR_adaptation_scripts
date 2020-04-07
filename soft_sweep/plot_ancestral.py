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
		infile=open('admix_MI0.01soft_recessive'+str(hset[run])+'_model1_run1.out')
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
			ancestryGenome.append(ances)
			ind+=5
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
	out1_10=np.array(out1[9:10])
	out1=out1_1+out1_2+out1_3+out1_4+out1_5+out1_6+out1_7+out1_8+out1_9+out1_10
	out1=out1/10
	out1=list(out1[0])
	print (len(out1))
	print (len(gen))
	plt.plot(gen,ancestryGenome,simID[run],linestyle='-',label=str(hset[run])+"%")
legend1=plt.legend(title='Admixture fraction',loc='lower right',bbox_to_anchor=(1.31,0),edgecolor='black')
ax = plt.gca().add_artist(legend1)

out1=np.array(out1)
np.savetxt('ancestryGenome_MI0.01soft_recessive_admix.txt',out1,fmt='%s',delimiter='\n',newline='\n')


for run in range(0,4):
	out1=[]
	out2=[]
	out3=[]
	for l in range(1,9):
		infile=open('admix_MI0.001soft_recessive'+str(hset[run])+'_model1_run1.out')
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
#	out3_9=np.array(out3[8:9])
#	out3_10=np.array(out3[9:10])
	out3=out3_1+out3_2+out3_3+out3_4+out3_5+out3_6+out3_7+out3_8#+out3_9+out3_10
	out3=out3/8
	out3=list(out3[0])
	print (len(out3))
	print (len(gen))
	plt.plot(gen,ancestryGenome2,simID[run],linestyle='-.')
out3=np.array(out3)
np.savetxt('ancestryGenome_MI0.001soft_recessive_admix.txt',out3,fmt='%s',delimiter='\n',newline='\n')


l1,=plt.plot(gen,ancestryGenome,simID[run],linestyle='-',label="0.01")
l2,=plt.plot(gen,ancestryGenome2,simID[run],linestyle='-.',label="0.001")
legend1=plt.legend(handles=[l1,l2],title='Selection coefficient',loc='lower right',bbox_to_anchor=(1.33,0.7),edgecolor='black')


plt.xscale('log')
plt.xlim((2,2000))
plt.ylim((0,1.1))
plt.xlabel('Generations after admixture')
plt.ylabel('Recipient population ancestry fraction')
plt.title('Recessive deleterious mutations')
plt.savefig('ancestryGenome_MIsoft_recessive_admix.svg',format='svg',bbox_inches = 'tight')
plt.close()
