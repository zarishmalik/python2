import time
def data_read():
	f=open('file1.txt')
	line=f.readline().split()
	while line:
		d={}
		d[line[-12]]=line[-11]
		d[line[-10]]=line[-9]
		d[line[-8]]=line[-7]
		d[line[-6]]=line[-5]
		d[line[-4]]=line[-3]
		d[line[-2]]=line[-1]
		di.append(d)
		line=f.readline().split()
	f.close()
def inWaitingq(pname):
	for i in range(0,len(wq)):
		if(wq[i]["pn"] == pname) :
			return True
	return False
def inreadyq(pname):
	for i in range(0,len(rq)):
		if(rq[i]["pn"] == pname) :
			return True
	return False
def find_min() :
	minv = int(wli[0]["rt"])
	ind = 0
	
	return ind	
def update_readyq(check):
	j=0
	d = {'ext':0,'et':0,'iot':0}
	for i in range(0,len(q)):
		
def update_waitingq():
	wq.append(rq[0])
	
def printfun() :
	print "process name	turn around time"
	for a in range (0,len(q)) :
		print output[a]["pn"],"	  	    ",output[a]["ta"]
if __name__ == "__main__" :
	di = []
	q = []
	rq = []
	li = []
	wq = []
	wli = []
	chk = True
	current_time = 0
	output = []
	data_read()
	print di
	#print len(di)
	q = sorted(di, key = lambda k: int(k["at"]))
	update_readyq(False)
	count = 0
	while count != len(q) :
		
def update_readyq(check):
	 i
def printfun() :
	print "process name	turn around time"
	for a in range (0,len(q)) :
		print output[a]["pn"],"	  	    ",output[a]["ta"]
if __name__ == "__main__" :
	di = []
	q = []
	rq = []
	li = []
	wq = []
	wli = []
	chk = True
	current_time = 0
	output = []
	data_read()
	print di
	#print len(di)
	q = sorted(di, key = lambda k: int(k["at"]))
	update_readyq(False)
	count = 0
	
