def loop_sum(a):
	sum=0
	for item in a:
		if isinstance(item,(int,float)):
			sum+=item
			
		if isinstance(item,(list)):
			from functools import reduce
			sum+=reduce(lambda x,y:x+y,item)

	return sum

a=[1,2,3,[4,5,6]]
print(loop_sum(a))
			
			
