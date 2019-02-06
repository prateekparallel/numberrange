import time
import datetime
from threading import Thread
from time import sleep
from multiprocessing.pool import ThreadPool
import json

def threaded_function(numbers_to_add,start,end):
	i = start
	sum = 0
	while( i < end ):
		sum = sum + numbers_to_add[i]
		i = i + 1
	return sum

def getTodaysDate():
	return datetime.datetime.today().strftime('%Y%m%d')

def getCurrentTime():
	ts = time.time()
	return datetime.datetime.fromtimestamp(ts).strftime('%H%M%S')
	
def generateJsonObject(key, val):
	lst = []
	d = {}
	d[key]=val
	lst.append(d)
	return json.dumps(lst)

	
def getTotalFromARangeOf():
	arrayLength = 10000001
	ran = len(str(arrayLength))

	if(ran > 4):
		ran = ran - 2

	numbers_to_add = list(range(arrayLength))

	start = 0
	endRange = int(arrayLength/ran)
	end = endRange

	print("Time before calculation :" + str(getCurrentTime()))

	pool = ThreadPool(processes=ran+1)
	i = 0
	result  = [None] * (ran + 1)

	while( i <= ran ):
		#print(start, end)
		result[i] = pool.apply_async(threaded_function, (numbers_to_add,start,end)) 
		start = end
		if ( (end + endRange) < arrayLength):
			end = end + endRange
		else:
			end = arrayLength
		i = i + 1
		
		
	i = 0
	total = 0
	while( i <= ran ):
		total = total + result[i].get()
		i = i + 1
		
	print(total)
	print("Time after calculation :" + str(getCurrentTime()))
	return total

def main():	
	
	getTotalFromARangeOf()
		
if __name__ == '__main__':
    main()