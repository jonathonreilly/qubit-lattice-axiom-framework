"""Native fourth-order interaction via finite linked-cluster controls."""
from pathlib import Path
import numpy as np,json,itertools
from neutral_rung_model import h,Ds,kron
P=Path(__file__).resolve().parent;E,U=np.linalg.eigh(h);w=U[:,:2];de=[U.T@d@U for d in Ds];v2=-sum(kron(d,d) for d in de)
t1=np.sqrt(2)*w.T@Ds[0]@Ds[1]@w;t2=np.sqrt(2)*w.T@Ds[0]@Ds[2]@w;t3=-1j*t1@t2
rows=[]
for L in [2,3,4]:
 N=8**L;k=2**L;ee=np.array([sum(t) for t in itertools.product(E,repeat=L)]);e0=-2*np.sqrt(2)*L;r=np.zeros(N);ok=abs(ee-e0)>1e-9;r[ok]=1/(e0-ee[ok]);ids=[sum(bit*8**(L-1-j) for j,bit in enumerate(bits)) for bits in itertools.product(range(2),repeat=L)]
 W=np.zeros((N,k));W[ids,np.arange(k)]=1
 def applyV(x):
  out=np.zeros_like(x)
  for i in range(L-1):
   xx=x.reshape(8**i,64,8**(L-i-2),k)
   out+=np.einsum('ab,ibjk->iajk',v2,xx,optimize=True).reshape(N,k)
  return out
 x=applyV(W);rx=r[:,None]*x;K2=x.T@rx;N2=rx.T@rx;y=applyV(rx)
 K4=y.T@(r[:,None]*y)-(N2@K2+K2@N2)/2
 identity=np.eye(k,dtype=complex);expected=np.zeros_like(identity)
 def pair(a,i,j):return kron(*[a if q in (i,j) else np.eye(2) for q in range(L)])
 def XY(i,j):return pair(t1,i,j)+pair(t2,i,j)
 for i in range(L-1):expected+=(-identity/32+XY(i,i+1)/16-5*pair(t3,i,i+1)/32)/np.sqrt(2)
 for i in range(L-2):expected+=(-identity/8-(XY(i,i+1)+XY(i+1,i+2))/16-3*XY(i,i+2)/16)/np.sqrt(2)
 err=float(np.max(abs(K4-expected)));assert err<1e-11
 rows.append(dict(L=L,low_dimension=k,full_rung_dimension=N,linked_fourth_error=err))
(P/'neutral_rung_linked_fourth.json').write_text(json.dumps(dict(rows=rows,scope='Explicit finite2,3,4rung fourth-order coefficient checks; general linked support argument requires independent review, no all-orders criticality.'),indent=2)+'\n');print(rows)
