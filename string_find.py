def find_all(s,c):
    l=[]
    t=0
    #print("s:",s)
    #print("c:",c)
    for i in range(len(s)):
        if(s[i]==c):
            l.append(i)
        else:
            t=t+1
    if(t==len(s)):
        return -1
    else:
        return l
        
