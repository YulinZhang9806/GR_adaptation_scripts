########################################################
###plot Figure 5 & S7, just change input files & generation numbers
###use the output of 'extract_phenotype_beforeGR' & 'extract_phenotype_afterGR'
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
from numpy import std
from math import exp
from math import sqrt

model=['model1','model2']
simID=['purple','blue','green','black']
colorID=['plum','lightsteelblue','mediumspringgreen','grey']

fig=plt.figure(figsize=(3,3))
fig,ax=plt.subplots(3,1,sharex='all',sharey='all')

###read in phenotype data before GR
infile=open('recessive_sqrt3000.txt')
line=infile.readlines()
infile.close()
if line[-1]=='\n':
	lines=line[:-1]
else:
	lines=line
###could change gen_before to 500 for Figure 5
gen_before=100
scale=0-int(gen_before)-2
r=int(gen_before)+1
###store phenotype data before GR
model=2
opt1=[]
opt2=[]
opt5=[]
ind=0
while ind<len(lines):
	if model==1:
		ind+=1
		while not lines[ind].startswith('opt1'):
			s=lines[ind].strip(',').strip('\n').strip(' ').split(',')
			data=[]
			for i in s:
				if not i=='' or i==' ':
					data.append(abs(float(i)-1))
			opt1.append(data[int(scale):-1])
			data=[]
			ind+=1

		while not lines[ind].startswith('opt2 model1'):
			ind+=1
		ind+=1
		while not lines[ind].startswith('opt2'):
			s=lines[ind].strip(',').strip('\n').strip(' ').split(',')
			data=[]
			for i in s:
				if not i=='' or i==' ':
					data.append(abs(float(i)-2))
			opt2.append(data[int(scale):-1])
			data=[]
			ind+=1

		while not lines[ind].startswith('opt5 model1'):
			ind+=1
		ind+=1
		while ind<len(lines) and not lines[ind].startswith('opt5'):
			s=lines[ind].strip(',').strip('\n').strip(' ').split(',')
			data=[]
			for i in s:
				if not i=='' or i==' ':
					data.append(abs(float(i)-5))
			opt5.append(data[int(scale):-1])
			data=[]
			ind+=1

		ind=len(lines)
	if model==2:
		while not lines[ind].startswith('opt1 model2'):
			ind+=1
		ind+=1
		while not lines[ind].startswith('opt2'):
			s=lines[ind].strip(',').strip('\n').strip(' ').split(',')
			data=[]
			for i in s:
				if not i=='' or i==' ':
					data.append(abs(float(i)-1))
			opt1.append(data[int(scale):-1])
			data=[]
			ind+=1

		while not lines[ind].startswith('opt2 model2'):
			ind+=1
		ind+=1
		while not lines[ind].startswith('opt5'):
			s=lines[ind].strip(',').strip('\n').strip(' ').split(',')
			data=[]
			for i in s:
				if not i=='' or i==' ':
					data.append(abs(float(i)-2))
			opt2.append(data[int(scale):-1])
			data=[]
			ind+=1

		while not lines[ind].startswith('opt5 model2'):
			ind+=1
		ind+=1
		while ind<len(lines):
			s=lines[ind].strip(',').strip('\n').strip(' ').split(',')
			data=[]
			for i in s:
				if not i=='' or i==' ':
					data.append(abs(float(i)-5))
			opt5.append(data[int(scale):-1])
			ind+=1

		ind=len(lines)
###calculate mean & standard error of each point on the trajectory
opt1_mean=[]
opt1_error=[]
for i in range(0,int(r)):
	d=[]
	for li in opt1:
#		print(len(li))
		d.append(float(li[i]))
	m=np.mean(d)
	e=float(np.std(d)/sqrt(int(len(d))))
	opt1_mean.append(m)
	opt1_error.append(e)

opt2_mean=[]
opt2_error=[]
for i in range(0,int(r)):
	d=[]
	for li in opt2:
		d.append(float(li[i]))
	m=np.mean(d)
	e=float(np.std(d)/sqrt(int(len(d))))
	opt2_mean.append(m)
	opt2_error.append(e)

opt5_mean=[]
opt5_error=[]
for i in range(0,int(r)):
	d=[]
	for li in opt5:
		d.append(float(li[i]))
	m=np.mean(d)
	e=float(np.std(d)/sqrt(int(len(d))))
	opt5_mean.append(m)
	opt5_error.append(e)

###read in phenotype data after GR
infile=open('recessive_sqrt3000_model2.txt')
line=infile.readlines()
infile.close()
if line[-1]=='\n':
	lines=line[:-1]
else:
	lines=line

n=['opt1','opt2','opt5']
nn=[opt1_mean,opt2_mean,opt5_mean]
ne=[opt1_error,opt2_error,opt5_error]
t=[1,2,5]
b=['0','0.1','1','10']
###generate x_lab
gen1=[-int(gen_before)]
for z in range(1,int(gen_before)):
	gen1.append(int(1*z)-int(gen_before))
gen1.append(0)
###could change gen_after to 2000 for Figure 5
gen_after=100
gen2=[1]
for z in range(1,int(int(gen_after)+1)):
	a=float(z)
	gen2.append(int(1*a))


for run in range(0,3):
###plot trajectory before GR
	ax1=ax[int(run)]
	ax1.errorbar(gen1, nn[run], yerr=ne[run], fmt='none', ecolor='orange', mec=None, ms=0, capsize=0, elinewidth=1)
	ax1.plot(gen1,nn[run],'darkorange')
	a1=[]
###calculate phenotype data for each point on the trajectory after GR and plot them
	ind=0
	while not lines[ind].startswith(str(n[run])):
		ind+=1
	g=0
	if not run==2:
		while not lines[ind].startswith(str(n[run+1])):
			ind+=1
			g+=1
			while ind<len(lines) and not lines[ind].startswith(str(n[run])) and not lines[ind].startswith(str(n[run+1])):
				s=lines[ind].strip(',').strip('\n').strip(' ').split(',')
				data=[]
				for i in s:
					if not i=='' or i==' ':
						data.append(abs(float(i)-float(t[run])))
				a1.append(data)
				ind+=1
			a1_mean=[]
			a1_error=[]
			for i in range(0,int(int(gen_after)+1)):
				d=[]
				for li in a1:
					d.append(float(li[i]))
				m=np.mean(d)
				e=float(np.std(d)/sqrt(int(len(d))))
				a1_mean.append(m)
				a1_error.append(e)
				d=[]
			print(g)
			ax1.errorbar(gen2, a1_mean, yerr=a1_error, ecolor=colorID[g-1], fmt='none', mec=None, ms=0, capsize=0, elinewidth=1)
			ax1.plot(gen2,a1_mean,simID[g-1])
			a1=[]
			a1_mean=[]
			a1_error=[]
	else:
		while ind<len(lines):
			ind+=1
			g+=1
			while ind<len(lines) and not lines[ind].startswith(str(n[run])):
				s=lines[ind].strip(',').strip('\n').strip(' ').split(',')
				data=[]
				temp=[]
				for i in s:
					if not i=='' or i==' ':
						data.append(abs(float(i)-float(t[run])))
				a1.append(data)
				ind+=1
			a1_mean=[]
			a1_error=[]
			for i in range(0,int(int(gen_after)+1)):
				d=[]
				for li in a1:
					d.append(float(li[i]))
				m=np.mean(d)
				e=float(np.std(d)/sqrt(int(len(d))))
				a1_mean.append(m)
				a1_error.append(e)
				d=[]
			print(g)
			ax1.errorbar(gen2, a1_mean, yerr=a1_error, ecolor=colorID[g-1], fmt='none', mec=None, ms=0, capsize=0, elinewidth=1)
			ax1.plot(gen2,a1_mean,simID[g-1])
			a1=[]
			a1_mean=[]
			a1_error=[]
ax1=ax[0]
plt.ylim(ymax=10)
ax1.set_title('Recessive deleterious mutations')
fig.text(0.5, 0, 'Generation before and after admixture', ha='center')
plt.savefig('meanPhenotype_sqrt3000_recessive_continue_m2_100.svg',format='svg',bbox_inches = 'tight')
plt.close()