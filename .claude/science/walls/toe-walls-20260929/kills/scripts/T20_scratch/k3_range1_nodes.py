"""Range-1 (26-neighbour) covariant families: how often does a random member have isolated Weyl nodes
(nonsingular Jacobian, charge +-1)?  Independent root-finder: dense grid seeding + Newton on d(k)=0 with analytic Jacobian
via finite differences of the basis functions."""
import numpy as np, sys
from scipy.optimize import fsolve
from k1_function_space import *
rng=np.random.default_rng(5)
vs=half_vectors(1)
def make_funcs(x,fs,nb,vs):
    def d(k):
        fk=np.array([f(k) for f in fs]); return np.array([x[nb*(1+i):nb*(2+i)]@fk for i in range(3)])
    return d
def jac(d,k,h=1e-6):
    J=np.zeros((3,3))
    for m in range(3):
        e=np.zeros(3);e[m]=h; J[:,m]=(d(k+e)-d(k-e))/(2*h)
    return J
def find_nodes(d,ngrid=14,starts=150):
    found=[]
    # seeds: coarse grid points with small |d| plus random
    g=np.linspace(-np.pi,np.pi,ngrid,endpoint=False)
    seeds=[np.array(p) for p in itertools.product(g,g,g)]
    vals=np.array([np.linalg.norm(d(s)) for s in seeds])
    idx=np.argsort(vals)[:starts]
    for i in idx:
        s=seeds[i]
        k,info,ier,msg=fsolve(d,s,full_output=True,xtol=1e-13)
        if ier==1 and np.linalg.norm(d(k))<1e-9:
            k=(k+np.pi)%(2*np.pi)-np.pi
            if not any(np.linalg.norm(((k-q+np.pi)%(2*np.pi))-np.pi)<1e-5 for q in found): found.append(k)
    return found
for kind in ['trivial','sign','axis','full']:
    null,fs,nb=family(kind,vs)
    hit=0;N=40; charges_ok=0; counts=[]
    for t in range(N):
        x=rng.normal(size=len(null))@null
        d=make_funcs(x,fs,nb,vs)
        nodes=find_nodes(d)
        iso=[k for k in nodes if np.linalg.svd(jac(d,k),compute_uv=False)[-1]>1e-5]
        if iso:
            hit+=1; counts.append(len(iso))
            ch=[int(np.sign(np.linalg.det(jac(d,k)))) for k in iso]
            charges_ok+= (sum(ch)==0)
    print(f'{kind:8s} range1: members with >=1 isolated rank-3 node: {hit}/{N}; total charge zero in {charges_ok}/{hit}; node counts {counts[:10]}')
