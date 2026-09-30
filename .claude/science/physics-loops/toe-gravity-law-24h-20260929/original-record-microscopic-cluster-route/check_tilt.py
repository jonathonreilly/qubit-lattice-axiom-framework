"""Exact source-algebra discriminator for the total-defect tilt correction."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from itertools import product
import hashlib,json,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
start=time.process_time();here=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED').exists() and not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
import numpy as np
A=(0,4);B=(1,2,3,5);edges=((0,1),(0,2),(0,3),(4,3),(4,5))
states=[]
for q in product((-1,0,1),repeat=6):
    if sum(q)!=2:continue
    E=(-q[1],-q[2],-q[3]-(q[4]-1+q[5]),q[4]-1+q[5],-q[5])
    if max(map(abs,E))<=1:states.append((q,E))
assert len(states)==72
indices={q:i for i,(q,E) in enumerate(states)};d=len(states)
def move(i,e,kind,sign=1):
    q,E=states[i];a,b=edges[e];r=list(q)
    if kind=='out':
        if not q[a] or q[b]:return None
        r[a]=0;r[b]=q[a];step=-q[a]
    else:
        if q[a] or q[b]:return None
        r[a]=sign;r[b]=-sign;step=sign
    if abs(E[e]+step)>1:return None
    j=indices[tuple(r)];target=list(E);target[e]+=step
    assert states[j][1]==tuple(target)
    return j
def matrix(e,kind,sign=1):
    out=np.zeros((d,d),dtype=np.int64)
    for i in range(d):
        j=move(i,e,kind,sign)
        if j is not None:out[j,i]=1
    return out
Fedge=[matrix(e,'out') for e in range(len(edges))]
Fa={a:sum((Fedge[e] for e,(aa,b) in enumerate(edges) if aa==a),np.zeros((d,d),dtype=np.int64)) for a in A}
F=Fa[0]+Fa[4];T=-F-F.T
w=np.array([sum(q[a]==0 for a in A) for q,E in states],dtype=np.int64)
n=np.array([sum(x!=0 for x in q) for q,E in states],dtype=np.int64)
nb=np.array([sum(q[b]!=0 for b in B) for q,E in states],dtype=np.int64)
k=w+nb;assert np.array_equal(k,n-len(A)+2*w)
W=np.diag(w);N=np.diag(n);K=np.diag(k)
comm=lambda X,Y:X@Y-Y@X
anti=lambda X,Y:X@Y+Y@X
assert np.array_equal(comm(W,F),F) and np.array_equal(comm(K,F),2*F)
C=np.zeros((d,d),dtype=np.int64)
for a in A:
    other=4 if a==0 else 0
    gate=np.array([q[other]!=0 for q,E in states],dtype=np.int64)
    blocked=np.array([sum(q[a]!=0 and q[b]==0 and move(i,e,'out') is None for e,(aa,b) in enumerate(edges) if aa==a) for i,(q,E) in enumerate(states)],dtype=np.int64)
    C+=(Fa[a].T@Fa[a]+np.diag(blocked))*gate[None,:]
assert np.array_equal(C,C.T) and not np.any(comm(W,C)) and not np.any(comm(N,C))
S1=-F+F.T;assert np.array_equal(comm(S1,W),-T)
D2=C+comm(F,F.T)
assert not np.any(comm(D2,W)) and not np.any(comm(D2,K))
H3num=3*comm(S1,C)+comm(S1,comm(S1,T)) # numerator of3*H3
grade=w[:,None]-w[None,:]
assert not np.any(H3num[grade==0])
S3times9=np.zeros((d,d),dtype=np.int64)
for i,j in zip(*np.nonzero(H3num)):
    assert (3*int(H3num[i,j]))%int(grade[i,j])==0
    S3times9[i,j]=3*H3num[i,j]//grade[i,j]
assert np.array_equal(S3times9,-S3times9.T)
assert not np.any(3*H3num+comm(S3times9,W))
omega=indices[(1,0,0,0,1,0)]
rows=[]
for coherent in (False,True):
    jumps=[]
    for e in range(len(edges)):
        plus=matrix(e,'birth',1);minus=matrix(e,'birth',-1)
        jumps.extend([plus+minus] if coherent else [plus,minus])
    X=np.zeros((d,d),dtype=np.int64);first=[];positive2_norm4=0
    for j in jumps:
        assert not np.any(comm(K,j)) and np.array_equal(comm(N,j),2*j)
        j1=comm(S1,j);first.append(j1)
        assert set(grade[np.nonzero(j1)])<={0,-2}
        X+=j.T@j1-j1.T@j
        j2num=comm(S1,j1)
        col=np.where(grade[:,omega]==1,j2num[:,omega],0)
        positive2_norm4+=int(col@col)
    assert positive2_norm4==4*18
    assert np.array_equal(X,-X.T) and set(grade[np.nonzero(X)])<={-1,1}
    IWX=np.zeros((d,d),dtype=np.int64)
    for i,j in zip(*np.nonzero(X)):IWX[i,j]=X[i,j]//grade[i,j]
    assert np.array_equal(IWX,IWX.T) and np.array_equal(comm(IWX,W),-X)
    for q in (2,3):
        Q=np.diag(np.power(q,k,dtype=np.int64));cross2=np.zeros((d,d),dtype=np.int64)
        for j,j1 in zip(jumps,first):
            assert not np.any(2*j.T@Q@j-anti(j.T@j,Q))
            cross2+=2*(j.T@Q@j1+j1.T@Q@j)-anti(j.T@j1+j1.T@j,Q)
        assert np.array_equal(cross2,comm(Q,X)) and np.any(cross2)
        # S_loss=i*kappa*IWX/(2delta). Multiply the pole coefficient by2/kappa.
        ham2=-comm(comm(IWX,W),Q)
        assert not np.any(cross2+ham2)
        assert np.array_equal(cross2-ham2,2*cross2) # wrong-sign control
        prep2num=int(comm(comm(Q,S1),S1)[omega,omega])
        assert prep2num==2*len(edges)*(q*q-1)
        rows.append({'instrument':'coherent_edge' if coherent else 'resolved','q':q,'uncorrected_pole_nonzero_entries':int(np.count_nonzero(cross2)),'corrected_pole_exactly_zero':True,'wrong_sign_doubles_pole':True,'bare_preparation_first_nonzero_tilted_coefficient':prep2num//2,'positive_grade_second_jump_squared_norm_on_Omega':positive2_norm4//4})
result={'model':'complete72-state spin-one Gauss tree, A0 degree3 and A4 degree2; actual compensation and both original instruments','states':len(states),'normal_form_H3_cancellation_exact':True,'K_def_relation_N_minus_NA_plus_2W_exact':True,'rows':rows,'scope':'Finite exact algebra only. No volume-uniform moment, local cluster tail or microscopic target convergence is inferred from this run.','cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'bindings':{name:hashlib.sha256((here/name).read_bytes()).hexdigest() for name in ('CONTRACT.md','RUN_CONTRACT.md','WORKING_ALGEBRA.md')}}
assert result['cpu_seconds']<30 and result['peak_rss_bytes']<150*1024**2
(here/'TILT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
