"""Finite canonical sixth-order collective interaction, numerical matrix control."""
from pathlib import Path
P=Path(__file__).resolve().parent
import numpy as np,itertools,json
from neutral_rung_model import h,Ds,kron
E,U=np.linalg.eigh(h);w=U[:,:2];de=[U.T@d@U for d in Ds];v2=-sum(kron(d,d) for d in de)
t1=np.sqrt(2)*w.T@Ds[0]@Ds[1]@w;t2=np.sqrt(2)*w.T@Ds[0]@Ds[2]@w;t3=-1j*t1@t2
L=4;N=8**L;k=2**L;ee=np.array([sum(t) for t in itertools.product(E,repeat=L)]);e0=E[0]*L;r=np.zeros(N);ok=abs(ee-e0)>1e-9;r[ok]=1/(e0-ee[ok]);ids=[sum(bit*8**(L-1-j) for j,bit in enumerate(bits)) for bits in itertools.product(range(2),repeat=L)];W=np.zeros((N,k));W[ids,np.arange(k)]=1

def V(x):
 out=np.zeros_like(x)
 for i in range(L-1):out+=np.einsum('ab,ibjk->iajk',v2,x.reshape(8**i,64,8**(L-i-2),k),optimize=True).reshape(N,k)
 return out
# Bloch wave operator P Omega=P; effective H measured relative to E0.
a=[W];b=[np.zeros((k,k))]
for n in range(1,7):
 va=V(a[n-1]);b.append(W.T@va)
 rhs=va.copy()
 for j in range(1,n):rhs-=a[n-j]@b[j]
 a.append(r[:,None]*rhs)
m=[sum(a[j].T@a[n-j] for j in range(n+1)) for n in range(7)]
# Formal power series square root S^2=M, inverse T=S^-1.
s=[np.eye(k)];t=[np.eye(k)]
for n in range(1,7):
 s.append((m[n]-sum((s[j]@s[n-j] for j in range(1,n)),np.zeros((k,k))))/2)
 t.append(-sum(s[j]@t[n-j] for j in range(1,n+1)))
K=[sum((s[i]@b[j]@t[n-i-j] for i in range(n+1) for j in range(n-i+1)),np.zeros((k,k))) for n in range(7)]
ev,q=np.linalg.eigh(t3);down=kron(*[q[:,0:1]]*L).ravel();up=kron(*[q[:,1:2]]*L).ravel()
charge=sum(kron(*[t3 if i==j else np.eye(2) for i in range(L)]) for j in range(L))
rows=[]
for n in range(1,7):
 row=dict(order=n,norm=float(np.linalg.norm(K[n])),hermiticity=float(np.linalg.norm(K[n]-K[n].T)),commutator=float(np.linalg.norm(K[n]@charge-charge@K[n])),up_down_abs=float(abs(up.conj()@K[n]@down)),up_eigen_res=float(np.linalg.norm(K[n]@up-(up.conj()@K[n]@up)*up)))
 rows.append(row);print(row,flush=True)
print('coefficient times sqrt2',abs(up.conj()@K[6]@down)*np.sqrt(2))

(P/'neutral_rung_sixth.json').open('w').write(json.dumps(rows,indent=2))
y=W.copy()
for j in range(5):y=r[:,None]*V(y)
bare=W.T@V(y)
print('bare',up.conj()@bare@down,'canonical',up.conj()@K[6]@down)

assert max(row["hermiticity"] for row in rows)<1e-12
assert abs(rows[-1]["up_down_abs"]-63/(128*np.sqrt(2)))<1e-12
assert abs(rows[-1]["commutator"]-63/16)<1e-12
