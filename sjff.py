import time
def data_read():
	c1=0
	line=f.readline().split()
	while line:
		c1=c1+1	
		d = {}
		d[line[-6]]=line[-5]#dictionary is actually key-value pair therefore in these lines d[line[-6]] is actually a key that is "pn". If you would see the .txt file then -6 means first word, -5 means second word and soo on. therefor in this case
		d[line[-4]]=line[-3]# "pn" is key and it's value is p1 for first line then line[-4] is actually "at" place that is key and -3 it's arraival time. then lines[-2] is actually  "bt" means 'burst time' and it's a key and it's value will be 8,4,9,5 consecutively
		d[line[-2]]=line[-1]
		
		di.append(d)
		line=f.readline().split()
	return c1

def print_func():
	v=0
	print ("process   turn around time   waiting time")
	while v<count:
		print (proc[v],"		",turn_ar[v],"		", wait[v])#printing information of the processes....
		v=v+1

if __name__ == "__main__" :
	f=open('file.txt')#opening the file
	i=0
	t=0
	tt=0
	dii={}
	st=0#service
	j=0
	k=0
	count =0
	di =[] #it's a list that will contain key-value pair of dictionary that is described in "data_read()" function
	proc = []#list for saving process name
	count=data_read()#return the count of the process
	turn_ar = []#list for saving turnaround time
	wait = []#list for saving waiting timr
	nlist=sorted(di, key = lambda k: k['bt']) # this line is sorting dictionaries that is stored in the "di" list on the basis of their burst time...Coz whose at is short that process will serve first
	print (nlist)
	while i<count:# loop until number of processes
                #
                
		dii=nlist[i]
		
		print (dii)
		print (dii["pn"] ,"execution started")
		j=int(dii["bt"])#accesing burst time
		print (dii["pn"] ," going to execute for ", j, "seconds")
		wait.append(t)
		tt=t+int(dii["bt"])
		
		while j>0:
			time.sleep(1)# sleeping the process for it's burst time
			j=j-1
			t=t+1
		"""while k<i :
			t=t+int(di[k]["bt"])
			k=k+1"""
		print ((dii["pn"]), "execution completed")
                #turn_ar.append(tt)
		#turn_ar.append((st+int(dii["bt"]))-int(dii["at"]))# appending turn around time for each process as turnaround_time= startingtime+burst_time-arraival time
		#wait.append((st-int(dii["at"])))#appending waiting time i.e start_time-arraival time
		proc.append(dii["pn"])#appending process name for eah process
		i=i+1
		turn_ar.append(tt)
		#st=t#saving starting time for next imediate process...as 't' at this point is the finish time for previous process that will become starting time for another process
	print_func()#pring the calculation at the end
