import numpy as np, itertools
def buildZ4(L,k1,k2):
    N=L*L; idx=lambda x,y:(x%L)*L+(y%L)
    T1=np.zeros((N,N),complex);T2=np.zeros((N,N),complex)
    for x in range(L):
        for y in range(L):
            T1[idx(x,y),idx(x+1,y)]=1j**k1[x,y]; T2[idx(x,y),idx(x,y+1)]=1j**k2[x,y]
    eta2=np.diag([(-1.)**x for x in range(L) for y in range(L)]).astype(complex)
    eps=np.diag([(-1.)**(x+y) for x in range(L) for y in range(L)]).astype(complex)
    D=0.5*((T1-T1.conj().T)+eta2@(T2-T2.conj().T))
    C1=(T1+T1.conj().T)/2;C2=(T2+T2.conj().T)/2
    G=1j*eta2@((C1@C2+C2@C1)/2)
    return D,G,eps
def Qof(L,k1,k2):
    tot=0
    for x in range(L):
        for y in range(L):
            k=(k1[x,y]+k2[(x+1)%L,y]-k1[x,(y+1)%L]-k2[x,y])%4
            tot+= {0:0,1:1,2:2,3:-1}[k]
    assert tot%4==0
    return tot//4
rng=np.random.default_rng(1)
L=4
cnt=0
for t in range(4000):
    k1=rng.integers(0,4,(L,L));k2=rng.integers(0,4,(L,L))
    D,G,eps=buildZ4(L,k1,k2)
    w=np.linalg.eigvalsh(1j*D)
    n0=(abs(w)<1e-9).sum()
    Q=Qof(L,k1,k2)
    if n0>0 and Q!=0:
        M=D+0.3*np.eye(16)+0.2j*G
        d=np.linalg.det(M)
        cnt+=1
        if cnt<12: print(t,'n0',n0,'Q',Q,'det',np.round(d,6),'tr',np.trace(G).real)
print(cnt)

print('--- admissible (no pi plaquette) search')
def plaqk(L,k1,k2):
    return [(k1[x,y]+k2[(x+1)%L,y]-k1[x,(y+1)%L]-k2[x,y])%4 for x in range(L) for y in range(L)]
rng=np.random.default_rng(20260929)
tot=0;res=[]
for t in range(200000):
    k1=rng.integers(0,4,(L,L));k2=rng.integers(0,4,(L,L))
    pk=plaqk(L,k1,k2)
    if 2 in pk: continue
    Q=Qof(L,k1,k2)
    tot+=1
    if Q==0: continue
    D,G,eps=buildZ4(L,k1,k2)
    w=np.linalg.eigvalsh(1j*D); n0=(abs(w)<1e-9).sum()
    d=np.linalg.det(D+0.3*np.eye(16)+0.2j*G)
    res.append((t,Q,n0,round(d.imag,5)))
    if len(res)>=15: break
print(tot,res)
