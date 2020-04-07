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
times=[1,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000]
out1=[]
out2=[]
out3=[]
runset=[3,4,5,6,7,8,9,10]

output=''
for run in range(0,4):
	out1_p1=[]
	out1_p2=[]
	out2=[]
	out3=[]
	data1=[]
	data2=[]
	for i in range(0,8):
		infile=open('admix_stabilizing_model1_sqrt3000_additive'+str(hset[run])+'_opt1_run'+str(runset[i])+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		phenotype_p1=[]
		phenotype_p2=[]
		fitness=[]
		ancestryGenome=[]
		data=[]
		ind=0
		while ind<len(lines)-10:
			while not lines[ind].startswith('Mean phenotype') and ind<len(lines)-1:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
			#print(s1[0])
			gen.append(float(s1[0])-60000)
			ind+=1
#			print(gen[-1])
			while not lines[ind].startswith('Total') and ind<len(lines)-1:
				ind+=1
			ind-=2
			s4=lines[ind].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			s5=lines[ind+1].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			phe_p1=float(s4[-1])
#				print(s5)
#				print(s5[-1])
			phe_p2=float(s5[-1])
			phenotype_p1.append(phe_p1)
			phenotype_p2.append(phe_p2)
			ind+=5
			if gen[-1]==2000:
				ind=len(lines)
		phenotype_p1=np.array(phenotype_p1)
		phenotype_p2=np.array(phenotype_p2)
		out1_p1.append(phenotype_p1)
		out1_p2.append(phenotype_p2)
	out1_p1_1=np.array(out1_p1[0:1])
	out1_p1_2=np.array(out1_p1[1:2])
	out1_p1_3=np.array(out1_p1[2:3])
	out1_p1_4=np.array(out1_p1[3:4])
	out1_p1_5=np.array(out1_p1[4:5])
	out1_p1_6=np.array(out1_p1[5:6])
	out1_p1_7=np.array(out1_p1[6:7])
	out1_p1_8=np.array(out1_p1[7:8])
#	out1_p1_9=np.array(out1_p1[8:9])
	out1_p1=out1_p1_1+out1_p1_2+out1_p1_3+out1_p1_4+out1_p1_5+out1_p1_6+out1_p1_7+out1_p1_8#+out1_p1_9
	out1_p1=out1_p1/8
	out1_p1=list(out1_p1[0])

	out1_p2_1=np.array(out1_p2[0:1])
	out1_p2_2=np.array(out1_p2[1:2])
	out1_p2_3=np.array(out1_p2[2:3])
	out1_p2_4=np.array(out1_p2[3:4])
	out1_p2_5=np.array(out1_p2[4:5])
	out1_p2_6=np.array(out1_p2[5:6])
	out1_p2_7=np.array(out1_p2[6:7])
	out1_p2_8=np.array(out1_p2[7:8])
#	out1_p2_9=np.array(out1_p2[8:9])
	out1_p2=out1_p2_1+out1_p2_2+out1_p2_3+out1_p2_4+out1_p2_5+out1_p2_6+out1_p2_7+out1_p2_8#+out1_p2_9
	out1_p2=out1_p2/8
	out1_p2=list(out1_p2[0])
        p2_100=out1_p2[0:1000]
        mean_100=np.mean(p2_100)
        print("admix:"+str(hset[run])+"\topt1\t"+str(mean_100-1))
	output+=str(run)+'\np1:\n'
	for phe in out1_p1:
		output+=str(phe)+'\n'
	for phe in out1_p2:
		output+=str(phe)+'\n'


	for t in times:
		t = int(t)
		data1.append(out1_p1[t-1])
		data2.append(out1_p2[t-1])	
	plt.plot(times,data2,simID[run])#,label="m="+str(hset[run])+"%")
#legend1=plt.legend(title='Admixture fraction',loc='lower right',bbox_to_anchor=(1.31,0),edgecolor='black')
#ax = plt.gca().add_artist(legend1)
outfile=open('meanPhenotype_admix_stabilizing_model1_sqrt3000_additive_opt1.txt','w')
outfile.write(output)
outfile.close()

output=''
for run in range(0,4):
	out1_p1=[]
	out1_p2=[]
	out2=[]
	out3=[]
	data1=[]
	data2=[]
	for i in range(0,9):
		infile=open('admix_stabilizing_model1_sqrt3000_additive'+str(hset[run])+'_opt2_run'+str(runset[i])+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		phenotype_p1=[]
		phenotype_p2=[]
		fitness=[]
		ancestryGenome=[]
		data=[]
		ind=0
		while ind<len(lines)-10:
			while not lines[ind].startswith('Mean phenotype') and ind<len(lines)-1:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
#			print(s1[0])
			gen.append(float(s1[0])-60000)
			ind+=1
#			print(gen[-1])
			while not lines[ind].startswith('Total') and ind<len(lines)-1:
				ind+=1
			ind-=2
			s4=lines[ind].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			s5=lines[ind+1].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			phe_p1=float(s4[-1])
#				print(s5)
#				print(s5[-1])
			phe_p2=float(s5[-1])
			phenotype_p1.append(phe_p1)
			phenotype_p2.append(phe_p2)
			ind+=5
			if gen[-1]==2000:
				ind=len(lines)
		phenotype_p1=np.array(phenotype_p1)
		phenotype_p2=np.array(phenotype_p2)
		out1_p1.append(phenotype_p1)
		out1_p2.append(phenotype_p2)
	out1_p1_1=np.array(out1_p1[0:1])
	out1_p1_2=np.array(out1_p1[1:2])
	out1_p1_3=np.array(out1_p1[2:3])
	out1_p1_4=np.array(out1_p1[3:4])
	out1_p1_5=np.array(out1_p1[4:5])
	out1_p1_6=np.array(out1_p1[5:6])
	out1_p1_7=np.array(out1_p1[6:7])
	out1_p1_8=np.array(out1_p1[7:8])
	out1_p1_9=np.array(out1_p1[8:9])
	out1_p1=out1_p1_1+out1_p1_2+out1_p1_3+out1_p1_4+out1_p1_5+out1_p1_6+out1_p1_7+out1_p1_8+out1_p1_9
	out1_p1=out1_p1/9
	out1_p1=list(out1_p1[0])

	out1_p2_1=np.array(out1_p2[0:1])
	out1_p2_2=np.array(out1_p2[1:2])
	out1_p2_3=np.array(out1_p2[2:3])
	out1_p2_4=np.array(out1_p2[3:4])
	out1_p2_5=np.array(out1_p2[4:5])
	out1_p2_6=np.array(out1_p2[5:6])
	out1_p2_7=np.array(out1_p2[6:7])
	out1_p2_8=np.array(out1_p2[7:8])
	out1_p2_9=np.array(out1_p2[8:9])
	out1_p2=out1_p2_1+out1_p2_2+out1_p2_3+out1_p2_4+out1_p2_5+out1_p2_6+out1_p2_7+out1_p2_8+out1_p2_9
	out1_p2=out1_p2/9
	out1_p2=list(out1_p2[0])
        p2_100=out1_p2[0:1000]
        mean_100=np.mean(p2_100)
        print("admix:"+str(hset[run])+"\topt2\t"+str(mean_100-2))
	output+=str(run)+'\np1:\n'
	for phe in out1_p1:
		output+=str(phe)+'\n'
	for phe in out1_p2:
		output+=str(phe)+'\n'

	for t in times:
		t = int(t)
		data1.append(out1_p1[t-1])
		data2.append(out1_p2[t-1])
#	plt.plot(gen,out1_p1,simID[run])
	plt.plot(times,data2,simID[run])#,label="m="+str(hset[run])+"%")
outfile=open('meanPhenotype_admix_stabilizing_model1_sqrt3000_additive_opt2.txt','w')
outfile.write(output)
outfile.close()

output=''
for run in range(0,4):
	out1_p1=[]
	out1_p2=[]
	out2=[]
	out3=[]
	data1=[]
	data2=[]
	for i in range(0,8):
		infile=open('admix_stabilizing_model1_sqrt3000_additive'+str(hset[run])+'_opt5_run'+str(runset[i])+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		phenotype_p1=[]
		phenotype_p2=[]
		fitness=[]
		ancestryGenome=[]
		data=[]
		ind=0
		while ind<len(lines)-10:
			while not lines[ind].startswith('Mean phenotype') and ind<len(lines)-1:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split('\t')
#			print(s1[0])
			gen.append(float(s1[0])-60000)
			ind+=1
#			print(gen[-1])
			while not lines[ind].startswith('Total') and ind<len(lines)-1:
				ind+=1
			ind-=2
			s4=lines[ind].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			s5=lines[ind+1].strip('\n').strip('"').strip(' ').strip('\t').split(' ')
			phe_p1=float(s4[-1])
#				print(s5)
#				print(s5[-1])
			phe_p2=float(s5[-1])
			phenotype_p1.append(phe_p1)
			phenotype_p2.append(phe_p2)
			ind+=5
			if gen[-1]==2000:
				ind=len(lines)
		phenotype_p1=np.array(phenotype_p1)
		phenotype_p2=np.array(phenotype_p2)
		out1_p1.append(phenotype_p1)
		out1_p2.append(phenotype_p2)
	out1_p1_1=np.array(out1_p1[0:1])
	out1_p1_2=np.array(out1_p1[1:2])
	out1_p1_3=np.array(out1_p1[2:3])
	out1_p1_4=np.array(out1_p1[3:4])
	out1_p1_5=np.array(out1_p1[4:5])
	out1_p1_6=np.array(out1_p1[5:6])
	out1_p1_7=np.array(out1_p1[6:7])
	out1_p1_8=np.array(out1_p1[7:8])
#	out1_p1_9=np.array(out1_p1[8:9])
	out1_p1=out1_p1_1+out1_p1_2+out1_p1_3+out1_p1_4+out1_p1_5+out1_p1_6+out1_p1_7+out1_p1_8#+out1_p1_9
	out1_p1=out1_p1/8
	out1_p1=list(out1_p1[0])

	out1_p2_1=np.array(out1_p2[0:1])
	out1_p2_2=np.array(out1_p2[1:2])
	out1_p2_3=np.array(out1_p2[2:3])
	out1_p2_4=np.array(out1_p2[3:4])
	out1_p2_5=np.array(out1_p2[4:5])
	out1_p2_6=np.array(out1_p2[5:6])
	out1_p2_7=np.array(out1_p2[6:7])
	out1_p2_8=np.array(out1_p2[7:8])
#	out1_p2_9=np.array(out1_p2[8:9])
	out1_p2=out1_p2_1+out1_p2_2+out1_p2_3+out1_p2_4+out1_p2_5+out1_p2_6+out1_p2_7+out1_p2_8#+out1_p2_9
	out1_p2=out1_p2/8
	out1_p2=list(out1_p2[0])
        p2_100=out1_p2[0:1000]
        mean_100=np.mean(p2_100)
        print("admix:"+str(hset[run])+"\topt5\t"+str(mean_100-5))
	output+=str(run)+'\np1:\n'
	for phe in out1_p1:
		output+=str(phe)+'\n'
	for phe in out1_p2:
		output+=str(phe)+'\n'

	for t in times:
		t = int(t)
		data1.append(out1_p1[t-1])
		data2.append(out1_p2[t-1])
	plt.plot(times,data2,simID[run],label=str(hset[run])+"%")
outfile=open('meanPhenotype_admix_stabilizing_model1_sqrt3000_additive_opt5.txt','w')
outfile.write(output)
outfile.close()



#out3=np.array(out3)
#plt.hlines(0, -150, 2150, colors = "y",linestyles = "dashed",label = "p1 optimum")
#plt.text(2150, 0.5, 'optimum p1', ha='right', va='center')
plt.hlines(1, -150, 2150, colors = "c",linestyles = "dashed",label = "p2 optimum")
#plt.text(-150, 1.25, 'optimum p2', ha='left', va='center')
plt.hlines(2, -150, 2150, colors = "c",linestyles = "dashed")
#plt.text(-150, 2.25, 'optimum p2', ha='left', va='center')
plt.hlines(5, -150, 2150, colors = "c",linestyles = "dashed")
#plt.text(-150, 5.25, 'optimum p2', ha='left', va='center')
#legend1=plt.legend(handles=[l1,l2],title='Population optimum',loc='lower right',bbox_to_anchor=(1.31,0.7),edgecolor='black')

plt.title('Additive deleterious mutations')
plt.xlabel('Generations after admixture')
plt.ylabel('Mean phenotype')
plt.savefig('meanPhenotype_stabilizing_model1_sqrt3000_additive_opt1_admix.svg',format='svg',bbox_inches = 'tight')
plt.close()
