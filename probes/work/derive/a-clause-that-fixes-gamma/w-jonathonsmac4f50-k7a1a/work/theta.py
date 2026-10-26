import numpy as np, itertools, time
M=32
ks=(np.arange(M)+0.5)*2*np.pi/M
K=np.stack(np.meshgrid(ks,ks,ks,indexing='ij'),-1).reshape(-1,3)
d1=np.sin(K); r1=np.linalg.norm(d1,axis=1)
rbar=r1.mean(); kap=rbar/12
def hNO(q):
    d2=np.sin(K+q); r2=np.linalg.norm(d2,axis=1)
    return ((r1*r2-(d1*d2).sum(1))/(r1+r2)).mean()
best=(0,None)
t0=time.time()
Q=M  # q grid multiples of 2pi/M, 0..M/2
res={}
for a in range(0,M//2+1):
  for b in range(a,M//2+1):
    for c in range(b,M//2+1):
        if a==b==c==0: continue
        q=2*np.pi*np.array([a,b,c])/M
        L=(2*(1-np.cos(q))).sum()
        h=hNO(q)
        ratio=h/(kap*L)
        res[(a,b,c)]=ratio
        if 1-ratio>best[0]: best=(1-ratio,(a,b,c))
print("max R/(kL)=",best, "min ratio h/(kL)",min(res.values()), time.time()-t0)
srt=sorted(res.items(), key=lambda kv: kv[1])[:8]
print(srt)
