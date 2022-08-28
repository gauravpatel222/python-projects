



def fun( a):
   for i in range(2,a):
    if(a%i==0):
        print("not prime")
        return  "not a prime no."
   print("it's a prime no.")
   return   
a=38
print(fun(700))
def sumarr(b):
    s=0
    for i in b:
        s=s+i
        
    print(s)
    max=b[0]
    for i1 in b:
        if(i1>max):
            max=i1
    print(max)

b1=[1,2,3,4]
sumarr(b1)
def check(c,d):
    for i in range(0,len(c)):
        x=0
        if(c[i]==d[0]):
            for j in range(0,len(d)):
                if(c[i]==d[j]):
                    x=x+1
                    i=i+1
                
            if(x==len(d)):
                return "present"     
    return "not present"      

c="abcdef"
d="ced"
print(check(c,d))
y="kjg da"
print(y.title())
k=y.split()

#print(k.capitalize())
