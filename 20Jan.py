#CRZ
x=int(input("Please enter an integer:")) #input will be stored as str thus we need int()
if x < 0 :
    x=0
    print("Negative changed to zero")
#else: print (x)
elif x==0:
    #x= "my dad"
    print ("zero")
elif x==1:
    #x= "my mom"
    print ('single')
else:
    print('tiger')
words=["cat","window","defenestrate"]#list
for w in words:
    print("w",len(w))
print(range(10))
print(list(range(10)))
for w in words[:]:#lis2
    if len(w)>6:
        words.insert(0,w)#list1
        print(words)
#FYP
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"=",x,'*',n//x)
            break
        else:
            print(n,'is a prime number')
for n in range(2,10):
    for x in range(2,n):
        #global x
        if n%x==0:
            print(n,"=",x,'*',n//x)
            break
    else:#######!!!!
            print(n,'is a prime number')
#Addition
def ask_ok(prompt,retries=4,reminder='Please try again'):
    while True:
        ok=input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries=retries-1
        if retries<0:
            raise ValueError('invalid user response')
        print(reminder)
