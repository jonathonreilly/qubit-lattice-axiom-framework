import itertools
def intervals(N,ell):
    m=N//ell; s=[ell]*m
    for i in range(N-m*ell): s[i%m]+=1
    assert all(ell<=t<=2*ell for t in s) and m>=12
    x=[0]
    for t in s[:-1]: x.append(x[-1]+t)
    I=[]
    for i in range(m):
        lo=x[i]-(2*s[i-1])//3; hi=x[i]+(2*s[i])//3
        I.append(set(t%N for t in range(lo,hi+1)))
    return I
worst={}
for ell in [12,13,17]:
  for N in [12*ell,12*ell+5,12*ell+ell-1,15*ell+7]:
    I=intervals(N,ell); m=len(I)
    assert set().union(*I)==set(range(N))
    ov=min(len(I[i]&I[(i+1)%m]) for i in range(m))
    # separation of i,i+2
    def dist(A,B): return min(min((a-b)%N,(b-a)%N) for a in A for b in B)
    sep=min(dist(I[i],I[(i+2)%m]) for i in range(m))
    worst.setdefault('ov',99); worst['ov']=min(worst['ov'],ov); worst.setdefault('sep',99); worst['sep']=min(worst['sep'],sep)
    # 2D mixed-vertex test: blocks P=(i,j),Q=(i+a,j+b); links (x,mu) mu in {0,1} plus "transverse" links assumed in both
    def inblk(p,ij): return p[0] in I[ij[0]%m] and p[1] in I[ij[1]%m]
    res={}
    for (a,b) in [(1,-1),(1,1),(1,0),(0,1)]:
        Bk=(3,3);Ck=(3+a,3+b); found=False
        for v in itertools.product(range(N),repeat=2):
            if not (inblk(v,Bk) or inblk(v,Ck)): continue
            # incident links: outgoing base v (mu=0,1), incoming bases v-e0, v-e1; transverse incoming bases same 2D point v
            bases=[v,((v[0]-1)%N,v[1]),(v[0],(v[1]-1)%N)]
            lab=[]
            ok=True
            for bp in bases:
                inB=inblk(bp,Bk); inC=inblk(bp,Ck)
                if not(inB or inC): ok=False
                lab.append((inB,inC))
            if ok and any(l==(True,False) for l in lab) and any(l==(False,True) for l in lab): found=True;break
        res[(a,b)]=found
    print(ell,N,"overlap",ov,"sep",sep,res)
