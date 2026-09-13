"""A charged ring with a dynamical flat holonomy: exploratory evidence."""
from itertools import combinations
from pathlib import Path
import json
import numpy as np
from scipy import sparse as sp
from scipy.sparse.linalg import eigsh

states=[sum(1<<i for i in pair) for pair in combinations(range(4),2)]
fi={s:j for j,s in enumerate(states)}
eta=np.array([0,1,0,1])
offsets=[]
for s in states:
    rho=np.array([(s>>j)&1 for j in range(4)])-eta
    offsets.append(np.r_[np.cumsum(rho)[:3],0])


def move(s,x,y):
    if not s>>y&1 or s>>x&1:return None
    sign=(-1)**((s&((1<<y)-1)).bit_count())
    v=s^(1<<y)
    sign*=(-1)**((v&((1<<x)-1)).bit_count())
    return fi[v|(1<<x)],sign


def matrix(g,S):
    basis=[(f,n) for f in range(6)
           for n in range(-S-int(min(offsets[f])),S-int(max(offsets[f]))+1)]
    ix={v:j for j,v in enumerate(basis)}
    H=sp.lil_matrix((len(basis),len(basis)))
    W=sp.lil_matrix(H.shape)
    for col,(f,n) in enumerate(basis):
        H[col,col]=.5*g*g*np.dot(offsets[f]+n,offsets[f]+n)
        if (f,n+1) in ix:W[ix[f,n+1],col]=1
        for edge in range(4):
            result=move(states[f],edge,(edge+1)%4)
            if result is not None:
                ff,sign=result;label=(ff,n+(edge==3))
                if label in ix:
                    row=ix[label];H[row,col]+=sign;H[col,row]+=sign
    return H.tocsr(),W.tocsr()


def free(theta):
    h=np.zeros((4,4),complex)
    for j in range(4):
        h[j,(j+1)%4]=np.exp(1j*theta) if j==3 else 1
        h[(j+1)%4,j]=h[j,(j+1)%4].conjugate()
    e=np.linalg.eigvalsh(h)
    return e[:2].sum()


rows=[]
for g in [.4,.2,.1,.05,.02,.01]:
    S=int(np.ceil((3+np.log(1/g))/np.sqrt(g)))
    H,W=matrix(g,S)
    e,v=eigsh(H,k=4,which='SA',tol=2e-12)
    order=np.argsort(e);e=e[order];v=v[:,order]
    rows.append(dict(g=g,S=S,levels=e.tolist(),ground_correction_over_g=float((e[0]+2*np.sqrt(2))/g),
                     gap_over_g=float((e[1]-e[0])/g),loop_real=float(v[:,0] @ (W @ v[:,0]))))
out=dict(free_at_zero=float(free(0)),free_at_pi=float(free(np.pi)),
         formal_ground_coefficient=2**(-5/4),formal_gap_coefficient=2**(-1/4),samples=rows)
p=Path(__file__).resolve().parent
(p/'BLOCK15_HOLONOMY_EXPLORATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
