########################################################
###extract data before admixture for Figure 5 & S7, just change "additive" to "partial"/"recessive"
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
model=['model1','model2']
simID=['blue','green']
times=[1,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000]
out1=[]
out2=[]
out3=[]
runset=[1,2,3,4,5,6,7,8,9,10]

output=''
for run in range(0,2):
	out1_p1=[]
	out1_p2=[]
	out2=[]
	out3=[]
	data1=[]
	data2=[]
	for i in range(0,10):
		infile=open('/'+str(model[run])+'/PG_stabilizing_additive_sqrt3000_60000_opt1_run'+str(runset[i])+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		phenotype_p1=[]
		phenotype_p2=[]
		fitness=[]
		ancestryGenome=[]
		data=[]
		ind=0
		l=0
		if run==0:
			while not lines[ind].startswith("59500"):
				ind+=1
		if run==1:
			while not lines[ind].startswith("59520"):
				ind+=1
		while ind<len(lines)-7:
			while not lines[ind].startswith('Mean phenotype') and ind<len(lines)-1:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split(' ')
			#print(s1[0])
			gen.append(float(s1[0])-59500)
			l+=1
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
			if l==501:
				ind=len(lines)
		phenotype_p1=np.array(phenotype_p1)
		phenotype_p2=np.array(phenotype_p2)
		out1_p1.append(phenotype_p1)
		out1_p2.append(phenotype_p2)

	output+='opt1 '+str(model[run])+'\n'
	for li in out1_p2:
		for i in li:
			output+=str(i)+','
		output+='\n'

for run in range(0,2):
	out1_p1=[]
	out1_p2=[]
	out2=[]
	out3=[]
	data1=[]
	data2=[]
	for i in range(0,10):
		infile=open('/'+str(model[run])+'/PG_stabilizing_additive_sqrt3000_60000_opt2_run'+str(runset[i])+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		phenotype_p1=[]
		phenotype_p2=[]
		fitness=[]
		ancestryGenome=[]
		data=[]
		ind=0
		l=0
		if run==0:
			while not lines[ind].startswith("59500"):
				ind+=1
		if run==1:
			while not lines[ind].startswith("59520"):
				ind+=1
		while ind<len(lines)-7:
			while not lines[ind].startswith('Mean phenotype') and ind<len(lines)-1:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split(' ')
			#print(s1[0])
			gen.append(float(s1[0])-59500)
			l+=1
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
			if l==501:
				ind=len(lines)
		phenotype_p1=np.array(phenotype_p1)
		phenotype_p2=np.array(phenotype_p2)
		out1_p1.append(phenotype_p1)
		out1_p2.append(phenotype_p2)

	output+='opt2 '+str(model[run])+'\n'
	for li in out1_p2:
		for i in li:
			output+=str(i)+','
		output+='\n'

for run in range(0,2):
	out1_p1=[]
	out1_p2=[]
	out2=[]
	out3=[]
	data1=[]
	data2=[]
	for i in range(0,10):
		infile=open('/'+str(model[run])+'/PG_stabilizing_additive_sqrt3000_60000_opt5_run'+str(runset[i])+'.out')
		lines=infile.readlines()
		infile.close()
		gen=[]
		phenotype_p1=[]
		phenotype_p2=[]
		fitness=[]
		ancestryGenome=[]
		data=[]
		ind=0
		l=0
		if run==0:
			while not lines[ind].startswith("59500"):
				ind+=1
		if run==1:
			while not lines[ind].startswith("59520"):
				ind+=1
		while ind<len(lines)-7:
			while not lines[ind].startswith('Mean phenotype') and ind<len(lines)-1:
				ind+=1
			ind-=1
			s1=lines[ind].strip('"').strip('\n').strip(':').split(' ')
			#print(s1[0])
			gen.append(float(s1[0])-59500)
			l+=1
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
			if l==501:
				ind=len(lines)
		phenotype_p1=np.array(phenotype_p1)
		phenotype_p2=np.array(phenotype_p2)
		out1_p1.append(phenotype_p1)
		out1_p2.append(phenotype_p2)

	output+='opt5 '+str(model[run])+'\n'
	for li in out1_p2:
		for i in li:
			output+=str(i)+','
		output+='\n'

outfile=open('additive_sqrt3000.txt','w')
outfile.write(output)
outfile.close()

