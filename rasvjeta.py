################### UNOS 
n=int(input("Unesi duljinu ulice: "))
m=int(input("Unesi broj svjetiljki: "))
k=int(input("Unesi domet svjetiljke: "))

niz=[0]*n
#svjetlo je 1
#tama je 0

for i in range(m):
    p=int(input("Unesi poziciju "+str(i+1)+". svjetiljke: "))
    niz[p-1]=1

#################### OBRADA

brojac=0
### UPALI SVJETLO
####gori sve
if len(niz)==(2*k+1):
    for i in range(len(niz)-1):
        niz[i]=1

####trazi lampe
print(niz)
for i in range(len(niz)):
    if 1==(niz[i]):
        #izlazi lijevo
        if k>i:
            for j in range(i,-1,-1):
                if niz[j]==0:
                    niz[j]=2
            #izlazi desno
            if k>(len(niz)-i-1):
                for j in range(i,len(niz)):
                    if niz[j]==0:
                        niz[j]=2
            else:
                for j in range(i,i+k+1):
                    if niz[j]==0:
                        niz[j]=2
            print(niz)
            continue
        #izlazi desno
        if k>(len(niz)-i-1):
            for j in range(len(niz)-i-1):
                if niz[j]==0:
                    niz[j]=2
            #izlazi lijevo
            if k>i:
                for j in range(i, -1, -1):
                    if niz[j]==0:
                        niz[j]=2
            else:
                for j in range(i,i-k-1,-1):
                    if niz[j]==0:
                        niz[j]=2
            continue
        #ako ne ude prije
        for j in range(i-k,i+k+1):
            if niz[j]==0:
                niz[j]=2

print(niz)
### PROVJERI GDJE JE TAMA
print("tama")

#2
if niz.count(0)!=0:
    t=niz.index(0)
else:
    t=0

while niz.count(0)!=0:
    if niz[t]!=0:
        t+=k
    else:
        niz[t]=1
        #samo to mjesto osvijetli
        if k==0:
            niz[t]=1
            brojac+=1
            print(1)
            continue
        #osvijetli tocno cijelu ulicu
        if len(niz)==(2*k+1):
            for i in range(len(niz)-1):
                if niz[i]==0:
                        niz[i]=1
            brojac+=1
            print(2)
            continue
        #izlazi iz ulice lijevo
        if k>t:
            for i in range(t-1,-1,-1):
                if niz[i]==0:
                        niz[i]=2
            #izlazi iz ulice desno
            if k>(len(niz)-t-1):
                for i in range(t+1,len(niz)):
                    if niz[i]==0:
                        niz[i]=2
            else:
                for i in range(t,t+k+1):
                    if niz[i]==0:
                        niz[i]=2
                    
            brojac+=1
            print(3)
            continue
        #izlazi iz ulice desno
        if k>(len(niz)-t-1):
            for i in range(len(niz)-t-1):
                if niz[i]==0:
                        niz[i]=2
            #izlazi iz ulice lijevo
            if k>t:
                for i in range(t,-1,-1):
                    if niz[i]==0:
                        niz[i]=2
            else:
                for i in range(t,t-k-1,-1):
                    if niz[i]==0:
                        niz[i]=2
            brojac+=1
            print(4)
            continue
        #ako ne prekine prije
        for i in range(t-k,t+k+1):
            if niz[i]==0:
                niz[i]=2
    
        brojac+=1
        print(5)
        print(niz)
    

################### ISPIS

print("Jos: "+str(brojac))

