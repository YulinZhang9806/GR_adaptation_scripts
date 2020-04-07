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

times=[1]
mean_load=[]
var_load=[]
mean_neand=[]
var_neand=[]
load_dist=[]
sum_neand_ancestry=[]
sum_var_neand_ancestry=[]
boxplot_data0=[]
out=[]
load=dict({})
load_count=dict({})
load_bounds=[0,1]
coeff=dict({})
boxplot_data=[]
boxplot_data1=[]
out_data=[]
neand_ancestry=dict({})

         
for t in times:
    for i in range(0,10000):
        load[(t,'p1:'+str(i))]=0
    for i in range(0,10000):
        load[(t,'p2:'+str(i))]=0
    for i in range(0,10000):
        neand_ancestry[(t,'p2:'+str(i))]=0
    for i in range(0,10000):
        neand_ancestry[(t,'p1:'+str(i))]=0

    infile=open('/space/s1/yulin/GR_MIhard_1/admix_MI0.01hard_bottleneck50_recessive_run1/MI0.01hard_model2_bottleneck50_recessive1_run'+str(t)+'_gen60022_1607788198993.txt')
    lines=infile.readlines()
    infile.close()
    ind=0
    while not lines[ind].startswith('Mutations'):
        ind+=1
    ind+=1
    while not lines[ind].startswith('Individuals'):
        s=lines[ind].strip('\n').split(' ')
        coeff[s[0]]=float(s[4])
        ind+=1
    while not lines[ind].startswith('Genomes'):
        ind+=1
    ind+=1

    while ind<len(lines)-1:
        s=lines[ind].strip('\n').split(' ')
        s2=lines[ind+1].strip('\n').split(' ')
        ID=s[0]
        s.pop(0)
        s2.pop(0)
        s.pop(0)
        s2.pop(0)
        mut_ind2=0
        s.sort(key=int)
        s2.sort(key=int)
        neand_ancestry1=0
        neand_ancestry2=0
        for j in range(len(s)):
            found=False
            i=1
            if coeff[s[j]]==0:
                neand_ancestry1+=1
            elif coeff[s[j]]<0:
                while mut_ind2<len(s2) and int(s2[mut_ind2])<int(s[j]):
                    mut_ind2+=1
                if mut_ind2<len(s2):
                    if s2[mut_ind2]==s[j]:
                        load[(t,ID)]+=coeff[s[j]]
                        s2[mut_ind2]='-1'
                    else:
                        load[(t,ID)]+=0*coeff[s[j]]
                else:
                    load[(t,ID)]+=0*coeff[s[j]]
            elif coeff[s[j]]>0:
                load[(t,ID)]+=0.5*coeff[s[j]]

        for k in range(len(s2)):
            if s2[k]=='-1':
                load[(t,ID)]-=0
            elif coeff[s2[k]]==0:
                neand_ancestry2+=1
            elif coeff[s2[k]]>0:
                load[(t,ID)]+=0.5*coeff[s2[k]]
            else:
                if coeff[s2[k]]<0:
                    load[(t,ID)]+=0*coeff[s2[k]]
        anc1=float(neand_ancestry1)/7151
        anc2=float(neand_ancestry2)/7151
        anc=anc1+anc2
        neand_ancestry[t,ID]+=float(anc)/2
        ind+=2
    human=[]
    neand=[]
    nean_ancestry=[]
    human_count=[]
    neand_count=[]
    for i in range(0,10000):
        if i%2==0:
            human.append(load[(t,'p1:'+str(i))])
    for i in range(0,10000):
        if i%2==0:
            neand.append(load[(t,'p2:'+str(i))])
    for i in range(0,10000):
        if i%2==0:
            nean_ancestry.append(neand_ancestry[(t,'p2:'+str(i))])

    print (min(neand), max(neand))
    print (min(human), max(human))
    mean_human=np.mean(human)
    for i in range(len(neand)):
        neand[i]=exp(neand[i]-mean_human)
    neand_mean=np.mean(neand)
    neand_med=np.median(neand)

    print(neand_mean)
    print(neand_med)

    plt.scatter(neand,nean_ancestry,s=5)

plt.legend(loc=0)
plt.xlabel('Fitness')
plt.ylabel('Ancestry')
plt.savefig('/home/yulin/recessive1_60022.pdf',format='pdf')
plt.close()

