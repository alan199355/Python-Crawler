# coding=utf-8
arg=[]
arg2=[]
arg3=[]
x=input()
for num in x.split(" "):
	try:
		arg.append(int(num))		
	except ValueError:
		print('%s is not number!'%num)
row=1
while row<=arg[0]:
	y=input()
	col=[]
	for num in y.split(" "):
		col.append(int(num))	
	arg2.append(col)
	row=row+1
# arg2=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
if arg[2]==0:
	for new_list in arg2:
		new_list.reverse()	
		arg3.append(new_list)
elif arg[2]==1:
	arg2.reverse()
	for new_list in arg2:			
		new_list.reverse
		arg3.append(new_list)
for x in arg3:
	for y in x:
		print(y,end=" ")		
	print('\n')
print(arg3)
