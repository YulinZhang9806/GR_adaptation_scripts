########################################################
###for Figure 3, just change generation number of input files
###use the outputFull file of SLiM as input
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

coeff=dict({})

from numpy import mean
from numpy import median
from numpy import var
from math import exp

times=[1]
m_set=['','0.0%','0.1%','1%','3%','10%']
color_set=['','purple','blue','green','red','black']

mean_load=[]
var_load=[]
mean_neand=[]
var_neand=[]
load_dist=[]
sum_neand_ancestry=[]
sum_var_neand_ancestry=[]
boxplot_data0=[]
out=[]
runset=['',0,0.1,1,3,10]
ID=['','',0,0,0,'1904259127055','2177873806400']

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
#        load_count[(t,'p1:'+str(i))]=0
    for i in range(0,10000):
        load[(t,'p2:'+str(i))]=0
    for i in range(0,10000):
        neand_ancestry[(t,'p2:'+str(i))]=0
    for i in range(0,10000):
        neand_ancestry[(t,'p1:'+str(i))]=0

    infile=open('MI0.01hard_model2_recessive1_run'+str(t)+'_gen60022_1607788198993.txt')
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
    #while not lines[ind].startswith('p2'):
    #    ind+=1
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
#                load_count[(t,ID)]+=1

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
 #                   load_count[(t,ID)]+=1
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
#           human_count.append(load_count[(t,'p1:'+str(i))])
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

output=''
for i in neand:
    output+=str(i)+','
output+='\n'
for i in nean_ancestry:
    output+=str(i)+','
outfile=open('recessive1_60022.txt','w')
outfile.write(output)
outfile.close()

def density_scatter( x , y, ax = None, sort = True, bins = 20, **kwargs )   :
    fig , ax = plt.subplots()
    """
    Scatter plot colored by 2d histogram
    """
    data , x_e, y_e = np.histogram2d( x, y, bins = bins, density = True )
    z = interpn( ( 0.5*(x_e[1:] + x_e[:-1]) , 0.5*(y_e[1:]+y_e[:-1]) ) , data , np.vstack([x,y]).T , method = "splinef2d", bounds_error = False)

    #To be sure to plot all data
    z[np.where(np.isnan(z))] = 0.0

    # Sort the points by density, so that the densest points are plotted last
    if sort :
        idx = z.argsort()
        x, y, z = x[idx], y[idx], z[idx]

    ax.scatter( x, y, c=z, **kwargs )
    plt.colorbar()

    norm = Normalize(vmin = np.min(z), vmax = np.max(z))
    cbar = fig.colorbar(cm.ScalarMappable(norm = norm), ax=ax)
    cbar.ax.set_ylabel('Density')
    return ax

infile=open('recessive1_60022.txt')
lines=infile.readlines()
infile.close()

ancestry=[]
fitness=[]
l=0
while l<len(lines):
    s1=lines[l].strip('\n').strip(',').split(',')
    for i in s1:
        ancestry.append(float(i))
    s2=lines[l+1].strip('\n').strip(',').split(',')
    for j in s2:
        fitness.append(float(j))
    l+=3

density_scatter(fitness,ancestry, bins=[30,30])


