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

infile=open('PG_stabilizing_recessive_sqrt3000_opt1_run2.out')
lines=infile.readlines()
infile.close()

times1=[0,1,5000,10000,15000,20000,25000,30000,45000,50000,55000,60000]
times2=[44000,44001,45000,46000,47000,48000,49000,50000,51000,52000,53000,54000,55000,56000,57000,58000,59000,60000]
gen1=[]
meanPhenotype1=[]
meanPhenotype2=[]
fitness1=[]
fitness2=[]
gen2=[]
data1=[]
data2=[]
position44000=[]
p2_position44000=[]
effect44000=[]
p2_effect44000=[]

ind=0
while not lines[ind].startswith('44000'):
	while not lines[ind].startswith('Mean'):
		ind+=1
	ind-=1
	s1=lines[ind].strip('\n').split(' ')
	gen=float(s1[0])
	gen1.append(gen)
	ind+=1
	while lines[ind].startswith('Mean'):
		s2=lines[ind].strip('\n').split(' ')
		phe=s2[2].strip(':')
		phe=float(phe)
		meanPhenotype1.append(phe)
		while not lines[ind].startswith('Fitness'):
			ind+=1
		s3=lines[ind].strip('\n').split(' ')
		fitness=float(s3[3])
		fitness1.append(fitness)
	ind+=1
gen=float(44000)
gen1.append(gen)
ind+=1
if lines[ind].startswith('Mean'):
	s2=lines[ind].strip('\n').split(' ')
	phe=s2[2].strip(':')
	phe=float(phe)
	meanPhenotype1.append(phe)
while not lines[ind].startswith('p1'):
	ind+=1
ind+=2

while not lines[ind].startswith('Fitness'):
	s7=lines[ind].strip('\n').split('\t')
	mut=s7[0].strip('\t').split(':')
	pos=int(mut[1])
	effect=float(s7[2])
	position44000.append(pos)
	effect44000.append(effect)
	ind+=1
s3=lines[ind].strip('\n').split(' ')
fitness=float(s3[3])
fitness1.append(fitness)

output=''
output+='defineConstant("m2_pos",c('
for i in position44000:
	output+=str(i)+','
output+='));\n'
output+='defineConstant("m2_effect",c('
for j in effect44000:
	output+=str(j)+','
output+='));\n'

outfile=open('recessive_sqrt3000_opt1_run2_44000_effect.txt','w')
outfile.write(output)
outfile.close()
