def format_name(s):
    #for i in range(0,len(s)):
    #    s[i]=s[i][0:1].upper()+s[i][1:].lower()
    s = s[0:1].upper() + s[1:].lower()
    return s
x=['dama','LISA']
print(list(map(format_name,x)))
print(x)
