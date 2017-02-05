import re
for i in range(5):
    co=input("Input your password:")
    m0=re.search('\w',co)
    m=re.search('\W',co)
    m1=re.search('\d',co)
    m2=re.search('[a-z]',co)
    if m0==None and m==None:
        print("Please print something")
        continue
    elif len(co) < 13:
        print("Weak password. Password should be longer")
        ask=input("Do you want try again? Y/N ")
        if ask=='Y' or ask=='y':
            continue
        else:
            break
    elif m==None and m1 and m2:
        print('''Password is not complex enough but ok. You can try some special
              characters like $ % @ !''')
        ask=input("Do you want try again? Y/N")
        if ask=='Y'or ask=='y':
            continue
        else:
            break
    elif m and m1 and m2:
        print("your password is good.")
        break
    else:
        print("loss of letters or numbers")
        ask=input("Do you want try again? Y/N")
        if ask=='Y'or ask=='y':
            continue
        else:
            break
if i==4:
    print("-"*45)
    print('''   You have tried so many times
    If you want to try again
    please restart the program''')
else:
    pass
