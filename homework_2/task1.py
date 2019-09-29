InputStr = str(raw_input("enter string:"))
InputStrLen = 0
InputStrLen = len(InputStr)
TStr = ''
k = 0
max_k = 0
for i in range(1, InputStrLen):
 TStr = InputStr[0:i]
 k = InputStr.count(TStr)
 num = k*len(TStr)
 if (num == InputStrLen):
 	max_k = k
	break

if(max_k != 0):
	print(max_k)
else:
	print("no such string was found, try to enter another string")

