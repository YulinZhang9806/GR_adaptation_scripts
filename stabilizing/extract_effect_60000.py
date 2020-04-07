infile=open('PG_stabilizing_recessive_sqrt3000_60000_opt5_run10.out')
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
pos=[]
effect=[]

ind=0
while not lines[ind].startswith('44001'):
	ind+=1
while ind<len(lines)-3:
	while not lines[ind].startswith('Mean'):
		ind+=1
	ind-=1
	s1=lines[ind].strip('\n').split(' ')
	gen=float(s1[0])
	gen1.append(gen)
	gen2.append(gen)
	ind+=1
	while lines[ind].startswith('Mean') and ind<len(lines)-3:
		s2=lines[ind+1].strip('\n').split(' ')
		s3=lines[ind+2].strip('\n').split(' ')
		phe_p1=s2[4]
		phe_p2=s3[4]
		phe_p1=float(phe_p1)
		phe_p2=float(phe_p2)
		meanPhenotype1.append(phe_p1)
		meanPhenotype2.append(phe_p2)
		if gen==60000:
			while not lines[ind].startswith('p2'):
				ind+=1
			ind+=2
			while not lines[ind].startswith('p1'):
				s4=lines[ind].strip('\n').split('\t')
		#		print(s4)
				posi=s4[0].strip('\n').strip('\t').split(':')
				pos.append(int(posi[1]))
				effect.append(float(s4[2]))
				ind+=1
			ind+=2
			while not lines[ind].startswith('Fitness'):
				s4=lines[ind].strip('\n').split('\t')
				posi=s4[0].strip('\n').strip('\t').split(':')
				pos.append(int(posi[1]))
				effect.append(float(s4[2]))
				ind+=1
		while not lines[ind].startswith('Fitness'):
			ind+=1
		s4=lines[ind+1].strip('\n').split(' ')
		s5=lines[ind].strip('\n').split(' ')
		fitness_p1=float(s4[3])
		fitness_p2=float(s5[3])
		fitness1.append(fitness_p1)
		fitness2.append(fitness_p2)
	ind+=2

output=''
output+='defineConstant("m2_pos",c('
for i in pos:
	output+=str(i)+','
output+='));\n'
output+='defineConstant("m2_effect",c('
for j in effect:
	output+=str(j)+','
output+='));\n'
outfile=open('recessive_sqrt3000_opt5_60000_effect_run10.txt','w')
outfile.write(output)
outfile.close()
