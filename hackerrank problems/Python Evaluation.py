x, k = input().split()
P = input()

l = []
for i in P:
    if i == "x":
        l.append(x)
    else:
        l.append(i)
  
P_str = str()
for i in l: 
    P_str += str(i)
    
a = eval(P_str)
if a == int(k):
    print(True)
else: 
    print(False)

#Verifies whether P(x) polynomial is equal to k or not.
