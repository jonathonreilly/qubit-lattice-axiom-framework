"""How often does a random unsoldered (trivial-action) range-1 covariant law have isolated Weyl nodes?
d(k) = c + m1 f1 + m2 f2 + m3 f3 (3 O-orbits of hops: 6 faces, 12 edges, 8 corners). Use the explicit form."""
import numpy as np, itertools
from scipy.optimize import fsolve
rng=np.random.default_rng(99)
def f(k):
    kx,ky,kz=k
    f1=np.cos(kx)+np.cos(ky)+np.cos(kz)
    f2=np.cos(kx)*np.cos(ky)+np.cos(ky)*np.cos(kz)+np.cos(kz)*np.cos(kx)
    f3=np.cos(kx)*np.cos(ky)*np.cos(kz)
    return np.array([f1,f2,f3])
# check: these span the same functions as the covariant-space basis (orbit sums of cos(k.v) over faces, edges, corners)
def orbit_sum(vs,k): return sum(np.cos(k@np.array(v)) for v in vs)/1.0
faces=[v for v in itertools.product([-1,0,1],repeat=3) if sum(map(abs,v))==1]
edges=[v for v in itertools.product([-1,0,1],repeat=3) if sum(map(abs,v))==2]
corn=[v for v in itertools.product([-1,0,1],repeat=3) if sum(map(abs,v))==3]
k=rng.uniform(-3,3,3)
A=np.array([orbit_sum(faces,k),orbit_sum(edges,k),orbit_sum(corn,k)])
print('orbit sums vs f-basis (should be a fixed invertible linear map):')
ks=rng.uniform(-3,3,(20,3))
F=np.array([f(q) for q in ks]); S=np.array([[orbit_sum(o,q) for o in (faces,edges,corn)] for q in ks])
coef,res,*_=np.linalg.lstsq(F,S,rcond=None); print(' max fit residual',np.abs(F@coef-S).max())
# image of f: sample
ks=rng.uniform(-np.pi,np.pi,(200000,3)); Fimg=np.array([f(q) for q in ks])
lo=Fimg.min(0);hi=Fimg.max(0);print(' f-range', lo.round(2),hi.round(2))
hit=0;N=3000;nodes_all=[]
def det_jac(k,c,M):
    h=1e-6;J=np.zeros((3,3))
    for m in range(3):
        e=np.zeros(3);e[m]=h;J[:,m]=(M@f(k+e)-M@f(k-e))/(2*h)
    return J
sample=Fimg[rng.choice(len(Fimg),20000)]
for t in range(N):
    M=rng.normal(size=(3,3)); c=rng.normal(size=3)
    if abs(np.linalg.det(M))<1e-3: continue
    fstar=-np.linalg.solve(M,c)
    # is fstar in image? find nearest sampled image point then Newton in k
    i=np.argmin(np.linalg.norm(sample-fstar,axis=1))
    if np.linalg.norm(sample[i]-fstar)>0.3: continue
    # locate a k by Newton from nearest of the 200k
    j=np.argmin(np.linalg.norm(Fimg-fstar,axis=1))
    k,info,ier,msg=fsolve(lambda q: f(q)-fstar,ks[j],full_output=True,xtol=1e-13)
    if ier==1 and np.linalg.norm(f(k)-fstar)<1e-10:
        J=det_jac(k,c,M); sv=np.linalg.svd(J,compute_uv=False)
        if sv[-1]>1e-5: hit+=1
print(f'random trivial-action range-1 members: {hit}/{N} have >=1 isolated rank-3 node ({100*hit/N:.1f}%)')
