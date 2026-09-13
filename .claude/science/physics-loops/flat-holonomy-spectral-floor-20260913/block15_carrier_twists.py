"""Explore supplied mixed-quartet torus energies; no global-minimum claim."""
from pathlib import Path
from itertools import product
import numpy as np,json
from scipy.optimize import minimize

s1=np.array([[0,1],[1,0]],complex);s2=np.array([[0,-1j],[1j,0]]);s3=np.diag([1.,-1.]);I=np.eye(2)
sig=[np.kron(I,s) for s in [s1,s2,s3]]
tx=np.kron(s1,I);tz=np.kron(s3,I)
sinb,cosb,zeta,mu=.8,.6,.6,.2
on=(2+zeta)*sig[2]+mu*tx@(sinb*sig[0]+cosb*sig[2])
Cs=[-sinb*sig[0]-cosb*sig[2],-sig[2],-sig[2]]
Ss=[tz@(cosb*sig[0]-sinb*sig[2]),sig[1],np.zeros((4,4))]
Ts=[(c-1j*s)/2 for c,s in zip(Cs,Ss)]


def bloch(k):
    return on+sum(c*np.cos(q)+s*np.sin(q) for q,c,s in zip(k,Cs,Ss))


def band_energy(phi,L):
    points=(2*np.pi*np.array(list(product(range(L),repeat=3)))+np.array(phi))/L
    h=np.array([bloch(k) for k in points])
    return float(np.sort(np.linalg.eigvalsh(h).ravel())[:2*L**3].sum())


def direct_energy(phi,L):
    vertices=list(product(range(L),repeat=3));vi={v:j for j,v in enumerate(vertices)}
    H=np.kron(np.eye(L**3),on)
    for v in vertices:
        for axis,T in enumerate(Ts):
            w=list(v);w[axis]=(w[axis]+1)%L;w=tuple(w)
            a,b=4*vi[v],4*vi[w]
            H[a:a+4,b:b+4]+=T*np.exp(1j*phi[axis]/L)
            H[b:b+4,a:a+4]+=T.conj().T*np.exp(-1j*phi[axis]/L)
    return float(np.linalg.eigvalsh(H)[:2*L**3].sum())


rows=[]
for L in [3,4,5,6,8]:
    grid=[dict(phi=list(phi),energy=band_energy(phi,L)) for phi in product([0.,np.pi],repeat=3)]
    rows.append(dict(L=L,identity=band_energy([0,0,0],L),corners=grid))
for row in rows[:2]:
    L=row['L'];best=min(row['corners'],key=lambda x:x['energy'])
    result=minimize(lambda phi:band_energy(phi,L),np.array(best['phi'])+.031,
                    method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-10,maxiter=1200))
    row['local_optimizer']=dict(success=bool(result.success),phi=(result.x%(2*np.pi)).tolist(),energy=float(result.fun))
    row['direct_checks']=[dict(phi=phi,bloch=band_energy(phi,L),direct=direct_energy(phi,L))
                          for phi in [[0,0,0],best['phi'],[.4,1.2,2.1]]]
out=dict(parameters=dict(sinb=sinb,cosb=cosb,zeta=zeta,mu=mu),rows=rows,
         limitation='Sampled corners and local optimization; no global minimum, interacting phase or infinite-volume rate certified.')
p=Path(__file__).resolve().parent;(p/'BLOCK15_CARRIER_TWISTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
