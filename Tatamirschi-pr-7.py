s=str(input('introduceti sirul de caractere'))
print(s.count('A'))
x=[] 
for i in range(0,len(s)):
  
    x=s.replace('A','*')
print(x)
y=[]    
for i in range(0,len(s)):
    y=s.replace('B','')
print(y)
z=[]
for i in range(0,len(s)):
    z=s.count('MA')
print(z) 
a=[]
for i in range(0,len(s)):
    a=s.replace('MA','TA')
print(z) 
q=[]
for i in range(0,len(s)):
    q=s.replace('TO','')
print(q)
print(s[::-1])



    









