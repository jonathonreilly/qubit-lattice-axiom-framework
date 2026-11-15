# B8b(i): backward cone of one tick. One-body proxy (the dressed gates have the same cube supports and conserve cube number):
# outputs within sup-distance 1 of x must have zero amplitude from inputs at sup-distance >= 4, for every residue of x.
import numpy as np, itertools
L=12; sites=list(itertools.product(range(L),repeat=3)); idx={s:i for i,s in enumerate(sites)}; n=len(sites); E=np.eye(3,dtype=int)
def eta(i,x): return (-1)**(sum(x[:i])%2)
def Rmat(o):
    R=np.zeros((n,n))
    for x in sites:
        for i in range(3):
            if x[i]%2==o:
                y=tuple((np.array(x)+E[i])%L); R[idx[y],idx[x]]=R[idx[x],idx[y]]=eta(i,x)/np.sqrt(3)
    return R
Re,Ro=Rmat(0),Rmat(1); eps,mu=0.8,0.5; ae,ao=eps-mu/2,eps+mu/2
V=(np.cos(ao)*np.eye(n)+1j*np.sin(ao)*Ro)@(np.cos(ae)*np.eye(n)-1j*np.sin(ae)*Re)
def dist(a,b): return max(min((p-q)%L,(q-p)%L) for p,q in zip(a,b))
for x in itertools.product((5,6),repeat=3):
    outs=[s for s in sites if dist(s,x)<=1 and sum(abs(min((p-q)%L,(q-p)%L)) for p,q in zip(s,x))<=1]   # x and its six neighbours
    far=[idx[s] for s in sites if dist(s,x)>=4]; ring3=[idx[s] for s in sites if dist(s,x)==3]
    leak=max(abs(V[idx[o],far]).max() for o in outs); used3=max(abs(V[idx[o],ring3]).max() for o in outs)
    print(f"x={x}: outputs {len(outs)}; max |V[out,in]| from distance>=4: {leak:.1e}; from distance exactly 3: {used3:.3f}")
