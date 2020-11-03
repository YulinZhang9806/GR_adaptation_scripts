########################################################
###for Figure 6 & S8
###use the output of 'calculate_geneticAdditiveVariance.py'
########################################################

import numpy as np
from math import exp
from copy import deepcopy
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, FuncFormatter

from scipy.stats import gaussian_kde
from numpy import arange

from numpy import mean
from numpy import median
from numpy import var
from math import exp

###read in and store data
opt=[1,2,5]
admix=[0.1,1,10]
simID=['purple','blue','green','black']
#mutset=['additive','partial','recessive']
additive=dict({})
partial=dict({})
recessive=dict({})

for i in opt:
	for j in admix:
		data=[]
		for t in range(1,6):
			percentage=[]
			infile=open('admix_sqrt3000_model1_additive'+str(j)+'_opt'+str(i)+'_run'+str(t)+'.txt')
			lines=infile.readlines()
			infile.close()

			ind=0
			while not lines[ind].startswith('p2_specific'):
				ind+=1
			ind+=1
			p2num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
#			print(p2num)
			ind+=2
			p1num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
#			print(p1num)
			for t in range(0,len(p2num)-1):
				if not float(p1num[t])==0:
					percent=float(p2num[t])/(float(p1num[t])+float(p2num[t]))
#					percent1="%.2f%%" % (percent * 100)
				else:
					percent=1
#					percent1="%.2f%%" % (1.0 * 100)
				percentage.append(percent)
			percentage=np.array(percentage)
			data.append(percentage)
		d1_1=np.array(data[0:1])
		d1_2=np.array(data[1:2])
		d1_3=np.array(data[2:3])
		d1_4=np.array(data[3:4])
		d1_5=np.array(data[4:5])
		dd1=d1_1+d1_2+d1_3+d1_4+d1_5
		dd1=dd1/5
		dd1=list(dd1[0])
		key='model1_opt'+str(i)+'_admix'+str(j)
		additive[key]=dd1
	for j in admix:
		data=[]
		for t in range(1,6):
			percentage=[]
			infile=open('admix_sqrt3000_model2_additive'+str(j)+'_opt'+str(i)+'_run'+str(t)+'.txt')
			lines=infile.readlines()
			infile.close()

			ind=0
			while not lines[ind].startswith('p2_specific'):
				ind+=1
			ind+=1
			p2num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			ind+=2
			p1num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			for t in range(0,len(p2num)-1):
				if not float(p1num[t])==0:
					percent=float(p2num[t])/(float(p1num[t])+float(p2num[t]))
#					percent1="%.2f%%" % (percent * 100)
				else:
					percent=1
#					percent1="%.2f%%" % (1.0 * 100)
				percentage.append(percent)
			percentage=np.array(percentage)
			data.append(percentage)
		d2_1=np.array(data[0:1])
		d2_2=np.array(data[1:2])
		d2_3=np.array(data[2:3])
		d2_4=np.array(data[3:4])
		d2_5=np.array(data[4:5])
		dd2=d2_1+d2_2+d2_3+d2_4+d2_5
		dd2=dd2/5
		dd2=list(dd2[0])
		key='model2_opt'+str(i)+'_admix'+str(j)
		additive[key]=dd2
opt=[1,2,5]
for i in opt:
	for j in admix:
		data=[]
		for t in range(1,6):
			percentage=[]
			infile=open('admix_sqrt3000_model1_partial'+str(j)+'_opt'+str(i)+'_run'+str(t)+'.txt')
			lines=infile.readlines()
			infile.close()

			ind=0
			while not lines[ind].startswith('p2_specific'):
				ind+=1
			ind+=1
			p2num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			ind+=2
			p1num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			for t in range(0,len(p2num)-1):
				if not float(p1num[t])==0:
					percent=float(p2num[t])/(float(p1num[t])+float(p2num[t]))
#					percent1="%.2f%%" % (percent * 100)
				else:
					percent=1
#					percent1="%.2f%%" % (1.0 * 100)
				percentage.append(percent)
			percentage=np.array(percentage)
			data.append(percentage)
		d3_1=np.array(data[0:1])
		d3_2=np.array(data[1:2])
		d3_3=np.array(data[2:3])
		d3_4=np.array(data[3:4])
		d3_5=np.array(data[4:5])
		dd3=d3_1+d3_2+d3_3+d3_4+d3_5
		dd3=dd3/5
		dd3=list(dd3[0])
		key='model1_opt'+str(i)+'_admix'+str(j)
		partial[key]=dd3
	for j in admix:
		data=[]
		for t in range(1,6):
			percentage=[]
			infile=open('admix_sqrt3000_model2_partial'+str(j)+'_opt'+str(i)+'_run'+str(t)+'.txt')
			lines=infile.readlines()
			infile.close()

			ind=0
			while not lines[ind].startswith('p2_specific'):
				ind+=1
			ind+=1
			p2num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			ind+=2
			p1num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			for t in range(0,len(p2num)-1):
				if not float(p1num[t])==0:
					percent=float(p2num[t])/(float(p1num[t])+float(p2num[t]))
#					percent1="%.2f%%" % (percent * 100)
				else:
					percent=1
#					percent1="%.2f%%" % (1.0 * 100)
				percentage.append(percent)
			percentage=np.array(percentage)
			data.append(percentage)
		d4_1=np.array(data[0:1])
		d4_2=np.array(data[1:2])
		d4_3=np.array(data[2:3])
		d4_4=np.array(data[3:4])
		d4_5=np.array(data[4:5])
		dd4=d4_1+d4_2+d4_3+d4_4+d4_5
		dd4=dd4/5
		dd4=list(dd4[0])
		key='model2_opt'+str(i)+'_admix'+str(j)
		partial[key]=dd4

for i in opt:
	for j in admix:
		data=[]
		for t in range(1,6):
			percentage=[]
			infile=open('admix_sqrt3000_model2_recessive'+str(j)+'_opt'+str(i)+'_run'+str(t)+'.txt')
			lines=infile.readlines()
			infile.close()

			ind=0
			while not lines[ind].startswith('p2_specific'):
				ind+=1
			ind+=1
			p2num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			ind+=2
			p1num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			for t in range(0,len(p2num)-1):
				if not float(p1num[t])==0:
					percent=float(p2num[t])/(float(p1num[t])+float(p2num[t]))
#					percent1="%.2f%%" % (percent * 100)
				else:
					percent=1
#					percent1="%.2f%%" % (1.0 * 100)
				percentage.append(percent)
			percentage=np.array(percentage)
			data.append(percentage)
		d5_1=np.array(data[0:1])
		d5_2=np.array(data[1:2])
		d5_3=np.array(data[2:3])
		d5_4=np.array(data[3:4])
		d5_5=np.array(data[4:5])
		dd5=d5_1+d5_2+d5_3+d5_4+d5_5
		dd5=dd5/5
		dd5=list(dd5[0])
		key='model2_opt'+str(i)+'_admix'+str(j)
		recessive[key]=dd5

	for j in admix:
		data=[]
		for t in range(1,6):
			percentage=[]
			infile=open('admix_sqrt3000_model1_recessive'+str(j)+'_opt'+str(i)+'_run'+str(t)+'.txt')
			lines=infile.readlines()
			infile.close()

			ind=0
			while not lines[ind].startswith('p2_specific'):
				ind+=1
			ind+=1
			p2num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			ind+=2
			p1num=lines[ind].strip(',').strip('\n').strip('\t').split(',')
			for t in range(0,len(p2num)-1):
				if not float(p1num[t])==0:
					percent=float(p2num[t])/(float(p1num[t])+float(p2num[t]))
#					percent1="%.2f%%" % (percent * 100)
				else:
					percent=1
#					percent1="%.2f%%" % (1.0 * 100)
				percentage.append(percent)
			percentage=np.array(percentage)
			data.append(percentage)
		d6_1=np.array(data[0:1])
		d6_2=np.array(data[1:2])
		d6_3=np.array(data[2:3])
		d6_4=np.array(data[3:4])
		d6_5=np.array(data[4:5])
		dd6=d6_2+d6_3+d6_4+d6_5+d6_1
		dd6=dd6/5
		dd6=list(dd6[0])
#		print(data)
		key='model1_opt'+str(i)+'_admix'+str(j)
		recessive[key]=dd6

def to_percent(temp, position):
	return '%.2f'%(100 * temp) + '%'

###could change r to 20 for Figure 6
r=100	
fig,ax=plt.subplots(2,2,sharex='all',sharey='all')
gen=range(1,int(int(r)+1))


ax1=ax[0,0]
key='model1_opt1_admix0.1'
data1=additive[key]
ax1.plot(gen[1:int(r)],data1[1:int(r)],color='purple',linestyle='-')
key='model1_opt1_admix1'
data2=additive[key]
ax1.plot(gen[1:int(r)],data2[1:int(r)],color='blue',linestyle='-')
key='model1_opt1_admix10'
data3=additive[key]
ax1.plot(gen[1:int(r)],data3[1:int(r)],color='green',linestyle='-')
#l1,=plt.plot(gen,data1,color='purple',linestyle='-',label="0.1%")
#l2,=plt.plot(gen,data2,color='blue',linestyle='-',label="1%")
#l3,=plt.plot(gen,data3,color='green',linestyle='-',label="10%")
#legend1=plt.legend(handles=[l1,l2,l3],title='Admixture fraction',loc='lower right',bbox_to_anchor=(2.4,0),edgecolor='black')
#fig = plt.gca().add_artist(legend1)

for j in range(0,len(admix)):
	key='model2_opt1_admix'+str(admix[j])
	data=additive[key]
	ax1.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-.')
ax1.set_title('Optimum 1')

ax2=ax[0,1]
for j in range(0,len(admix)):
	key='model1_opt2_admix'+str(admix[j])
	data=additive[key]
	ax2.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-')
for j in range(0,len(admix)):
	key='model2_opt2_admix'+str(admix[j])
	data=additive[key]
	ax2.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-.')
ax2.set_title('Optimum 2')
#plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

ax3=ax[0,2]
for j in range(0,len(admix)):
	key='model1_opt5_admix'+str(admix[j])
	data=additive[key]
	ax3.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-')
for j in range(0,len(admix)):
	key='model2_opt5_admix'+str(admix[j])
	data=additive[key]
	ax3.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-.')
ax3.set_title('Optimum 5')
ax3.text(21, 0.5, 'Additive', va='center', rotation=-90)

ax4=ax[1,0]
for j in range(0,len(admix)):
	key='model1_opt1_admix'+str(admix[j])
	data=partial[key]
	ax4.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-')
for j in range(0,len(admix)):
	key='model2_opt1_admix'+str(admix[j])
	data=partial[key]
	ax4.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-.')
#ax4.set_title('Partially recessive')
#plt.xscale("log")

ax5=ax[1,1]
for j in range(0,len(admix)):
	key='model1_opt2_admix'+str(admix[j])
	data=partial[key]
	ax5.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-')
for j in range(0,len(admix)):
	key='model2_opt2_admix'+str(admix[j])
	data=partial[key]
	ax5.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-.')
#ax5.set_title('Optimum 2')
#plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

ax6=ax[1,2]
for j in range(0,len(admix)):
	key='model1_opt5_admix'+str(admix[j])
	data1=partial[key]
	ax6.plot(gen[1:int(r)],data1[1:int(r)],simID[j],linestyle='-')
for j in range(0,len(admix)):
	key='model2_opt5_admix'+str(admix[j])
	data2=partial[key]
	ax6.plot(gen[1:int(r)],data2[1:int(r)],simID[j],linestyle='-.')
ax6.text(21, 0.5, 'Partially recessive', va='center', rotation=-90)
#ax6.set_title('Optimum 5')
#l1,=plt.plot(gen,data1,simID[j],linestyle='-',label="Model1")
#l2,=plt.plot(gen,data2,simID[j],linestyle='-.',label="Model2")
#legend2=plt.legend(handles=[l1,l2],title='Demographic model',loc='lower right',bbox_to_anchor=(2.4,0.7),edgecolor='black')


ax7=ax[2,0]
for j in range(0,len(admix)):
	key='model1_opt1_admix'+str(admix[j])
	data=recessive[key]
	ax7.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-')
for j in range(0,len(admix)):
	key='model2_opt1_admix'+str(admix[j])
	data=recessive[key]
	ax7.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-.')
#ax7.set_title('Recessive')
#plt.yscale('log')


ax8=ax[2,1]
for j in range(0,len(admix)):
	key='model1_opt2_admix'+str(admix[j])
	data=recessive[key]
	ax8.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-')
for j in range(0,len(admix)):
	key='model2_opt2_admix'+str(admix[j])
	data=recessive[key]
	ax8.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-.')
#plt.yscale('log')


ax9=ax[2,2]
for j in range(0,len(admix)):
	key='model1_opt5_admix'+str(admix[j])
	data=recessive[key]
	ax9.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-')
for j in range(0,len(admix)):
	key='model2_opt5_admix'+str(admix[j])
	data=recessive[key]
	ax9.plot(gen[1:int(r)],data[1:int(r)],simID[j],linestyle='-.')
#plt.yscale('log')

ax9.text(21, 0.5, 'Recessive', va='center', rotation=-90)

#legend1=plt.legend(title='Admixture fraction',loc='lower right',bbox_to_anchor=(1.31,0),edgecolor='black')
#ax = plt.gca().add_artist(legend1)



#plt.xscale('log')
#plt.ylim((0,1.05))
#plt.xticks([2,4,6,8,10,12,14,16,18,20])
#plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
fig.text(0.5, 0, 'Generation after admixture', ha='center')
fig.text(0, 0.5, 'Proportion of genetic additive variance', va='center', rotation='vertical')
plt.tight_layout()
plt.subplots_adjust(wspace = 0.1, hspace =0.2)
#plt.title('Recessive deleterious mutations')
plt.savefig('phenotype_h2_p1p2_1_100.svg',format='svg',bbox_inches = 'tight')
plt.close()