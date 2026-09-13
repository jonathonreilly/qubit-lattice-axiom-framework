"""Small discriminating comparison, not a general Hessian proof."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import sys,itertools,json,time
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(root/'scripts'))
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4

def proposed(k):
    z=np.exp(1j*k); p=2*np.sin(k/2)
    idx={frozenset(i for i,v in enumerate(vv) if v):j for j,vv in enumerate(R4.DIRS15)}
    R=np.zeros((4,15),complex)
    for j,A in enumerate(itertools.combinations(range(4),3)):
        R[j,idx[frozenset(A)]]=1
        for a,b in itertools.combinations(A,2):
            c=next(x for x in A if x not in (a,b))
            R[j,idx[frozenset((a,b))]]-=(1+z[c])/2
        for a in A:
            b,c=[x for x in A if x!=a]
            R[j,idx[frozenset((a,))]]+=(z[b]+z[c])/2
    H=np.zeros((15,4,4),complex)
    for a in range(4):H[idx[frozenset((a,))],a,a]=1
    for a,b in itertools.combinations(range(4),2):
        phase=np.exp(-1j*(k[a]+k[b])/2)/2
        for S,sign in ((frozenset((a,b)),1),(frozenset((a,)),-1),(frozenset((b,)),-1)):
            H[idx[S],a,b]+=sign*phase
            H[idx[S],b,a]+=sign*phase
    lap=p@p
    HP=H@p; tr=np.trace(H,axis1=1,axis2=2); pp=np.einsum('i,aij,j->a',p,H,p)
    F=lap*np.einsum('aij,bij->ab',H.conj(),H)-2*(HP.conj()@HP.T)
    F+=np.outer(tr.conj(),pp)+np.outer(pp.conj(),tr)-lap*np.outer(tr.conj(),tr)
    return -F/4-R.conj().T@R/2,R,H

rows=[]
for k in [np.zeros(4),np.array([.37,-.81,.22,.29]),np.array([.013,.007,-.02,0]),np.array([np.pi,0,0,0])]:
    D=np.diag(1/(2*np.sqrt(np.sum(R4.DIRS15,axis=1))))
    Q=D@R4.bloch_Q(k)@D
    cand,R,H=proposed(k)
    G=np.diag(1/np.diag(D))@R4.gauge_map(k)
    body=[i for i,v in enumerate(R4.DIRS15) if sum(v)==3]
    row={'k':k.tolist(),'full_residual':float(np.max(np.abs(Q-cand))),
         'body_block_residual':float(np.max(np.abs(Q[np.ix_(body,body)]+np.eye(4)/2))),
         'body_constraint_residual':float(np.max(np.abs(Q[body,:]+R/2))),
         'gauge_constraint_residual':float(np.max(np.abs(R@G)))}
    rows.append(row)
    print(json.dumps(row),flush=True)
Path(__file__).with_name('BLOCK07_FIRST_REDUCTION_PROBE.json').write_text(json.dumps({'scope':'four floating-point fixtures, not a global proof','rows':rows},indent=2)+'\n')
