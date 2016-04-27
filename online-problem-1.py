# coding=utf-8
str1=input()
str2=input()

res=""
for num in range(0,len(str1)):	
	if(str1[num]==str2[num]):
		res+="1"
	elif(str1[num]!=str2[num]):
		res+="0"
print(res)