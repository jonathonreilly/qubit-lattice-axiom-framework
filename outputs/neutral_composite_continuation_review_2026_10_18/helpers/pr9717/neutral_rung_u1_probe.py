"""Check whether derived XY charge survives the finite full native low band."""
from pathlib import Path
import itertools,json,numpy as np
from scipy.sparse.linalg import LinearOperator,eigsh
from scipy.linalg import polar
from neutral_rung_model import h,Ds,kron
P=Path(__file__).resolve().parent;E,U=np.linalg.eigh(h);w=U[:,:2];de=[U.T@d@U for d in Ds];v2=-sum(kron(d,d) for d in de)
t1=np.sqrt(2)*w.T@Ds[0]@Ds[1]@w;t2=np.sqrt(2)*w.T@Ds[0]@Ds[2]@w;t3=-1j*t1@t2
L=4;N=8**L;ee=np.array([sum(t) for t in itertools.product(E,repeat=L)]);ids=[sum(bit*8**(L-1-j) for j,bit in enumerate(bits)) for bits in itertools.product(range(2),repeat=L)];W=np.zeros((N,16));W[ids,np.arange(16)]=1
charge=sum(kron(*[t3 if i==j else np.eye(2) for i in range(L)]) for j in range(L))
def applyV(x):
 wasvec=x.ndim==1;xx=x.reshape(N,-1);k=xx.shape[1];out=np.zeros_like(xx)
 for i in range(L-1):out+=np.einsum('ab,ibjk->iajk',v2,xx.reshape(8**i,64,8**(L-i-2),k),optimize=True).reshape(N,k)
 return out[:,0] if wasvec else out
ev3,uv3=np.linalg.eigh(t3);down=kron(*[uv3[:,0:1]]*L).ravel();up=kron(*[uv3[:,1:2]]*L).ravel()
rows=[]
for lam in [.05,.1,.2,.3,.5]:
 op=LinearOperator((N,N),matvec=lambda x:ee*x+lam*applyV(x),dtype=float)
 ev,u=eigsh(op,k=18,which='SA',tol=1e-13,ncv=80,v0=np.random.default_rng(182).normal(size=N));ix=np.argsort(ev);ev=ev[ix];u=u[:,ix];low=u[:,:16];Q,_=polar(low.T@W);aligned=low@Q;heff=Q.T@np.diag(ev[:16])@Q
 com=float(np.linalg.norm(heff@charge-charge@heff));res=max(float(np.linalg.norm(op@u[:,i]-ev[i]*u[:,i])) for i in range(18))
 rows.append(dict(lambda_z=lam,band_gap=float(ev[16]-ev[15]),max_eigen_residual=res,min_projection_singular=float(min(np.linalg.svd(low.T@W,compute_uv=False))),charge_commutator=com,all_up_down_matrix_element_abs=float(abs(up.conj()@heff@down)),all_up_down_over_lambda6=float(abs(up.conj()@heff@down))/lam**6,commutator_over_lambda6=com/lam**6))
(P/'neutral_rung_u1_probe.json').write_text(json.dumps(dict(rows=rows,scope='Finite polar-gauge low-band charge diagnostic; not all-orders operator identity or bulk criticality proof.'),indent=2)+'\n');print(rows)
