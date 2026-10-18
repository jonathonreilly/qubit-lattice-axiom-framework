import sys, numpy as np, random
sys.path.insert(0,'.')
from lattice import Lattice
lat=Lattice(2); T=float(sys.argv[1]); N=int(sys.argv[2]); g=1.0
random.seed(5)
nbs=[set(lat.nbh[p,:lat.nnb[p]].tolist()) for p in range(lat.np)]
s0=lat.canonical().copy(); kinks=[]  # sorted list of (t,p)
def flippable(s,p): return abs((s[lat.plinks[p]]*lat.psign).sum())==4
nk=[]
for it in range(N):
    for m in range(30):
        p=random.randrange(lat.np)
        first=[ (t,q) for (t,q) in kinks if q in nbs[p]]
        tf = first[0][0] if first else T
        if random.random()<0.5:
            if not flippable(s0,p): continue
            t=random.random()*tf
            if random.random()< g*tf:
                s0[lat.plinks[p]]*=-1; kinks.append((t,p)); kinks.sort()
        else:
            if not first or first[0][1]!=p: continue
            tf2 = first[1][0] if len(first)>1 else T
            if random.random() < 1/(g*tf2):
                kinks.remove(first[0]); s0[lat.plinks[p]]*=-1
    if it>2000: nk.append(len(kinks))
nk=np.array(nk); print('python start-only <n>', nk.mean(), '+-', nk.std()/np.sqrt(len(nk)/50))
h=np.bincount(nk,minlength=12)[:6]
print("python hist", np.round(h/len(nk),4))
