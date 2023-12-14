def firstFit(p_size,b_size):
    n=len(p_size)
    m=len(b_size)
    allot=[-1]*n
    for i in range(n):
        for j in range(m):
            if b_size[j]>=p_size[i]:
                allot[i]=j
                b_size[j]-=p_size[i]
                break
    print("\np\tps\tbno")
    for i in range(n):
        print(f"\n{i+1}\t{p_size[i]}",end=" ")
        if allot[i]!=-1:
            print(f"\t{allot[i]+1}",end=" ")
        else:
            print("\tnot alloted",end=" ")

def bestFit(p_size,b_size):
    n=len(p_size)
    m=len(b_size)
    allot=[-1]*n
    
    for i in range(n):
        min=float('inf')
        for j in range(m):
            if b_size[j]>=p_size[i]:
                diff=b_size[j]-p_size[i]
                if diff<min:
                    min=diff
                    allot[i]=j
        if allot[i]!=-1:
            b_size[allot[i]]-=p_size[i]
        
                
    print("\np\tps\tbno")
    for i in range(n):
        print(f"\n{i+1}\t{p_size[i]}",end=" ")
        if allot[i]!=-1:
            print(f"\t{allot[i]+1}",end=" ")
        else:
            print("\tnot alloted",end=" ")

def worstFit(p_size,b_size):
    n=len(p_size)
    m=len(b_size)
    allot=[-1]*n

    b_size_sorted=sorted(range(len(b_size)),key=lambda k:b_size[k],reverse=True)
    
    for i in range(n):
        for j in b_size_sorted:
            if b_size[j]>=p_size[i]:
                allot[i]=j
                b_size[j]-=p_size[i]
                break
        
                
    print("\np\tps\tbno")
    for i in range(n):
        print(f"\n{i+1}\t{p_size[i]}",end=" ")
        if allot[i]!=-1:
            print(f"\t{allot[i]+1}",end=" ")
        else:
            print("\tnot alloted",end=" ")

n=int(input("enter no of prosses"))
p_size=[]
b_size=[]
print("\nenter p size")
for _ in range(n):
    p_size.append(int(input()))
print("\nenter b size")
for _ in range(n):
    b_size.append(int(input()))
worstFit(p_size,b_size)

