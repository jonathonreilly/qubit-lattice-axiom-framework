"""Derived low-rung-band interaction and composite observable, finite controlled probe."""
from pathlib import Path
import numpy as np,json,itertools
from scipy.linalg import polar
from neutral_rung_model import h,Ds,kron
P=Path(__file__).resolve().parent
E,U=np.linalg.eigh(h);w=U[:,:2];t1=np.sqrt(2)*w.T@Ds[0]@Ds[1]@w;t2=np.sqrt(2)*w.T@Ds[0]@Ds[2]@w;t3=-1j*t1@t2
assert np.max(abs(t1@t1-np.eye(2)))<1e-12 and np.max(abs(t1@t2+t2@t1))<1e-12
L=3;I=np.eye(8);H0=kron(h,I,I)+kron(I,h,I)+kron(I,I,h)
V=-sum(kron(d,d,I)+kron(I,d,d) for d in Ds);O=sum(kron(d,I,d) for d in Ds)
W=kron(w,w,w);EE=np.array([sum(x) for x in itertools.product(E,repeat=L)]);UU=kron(U,U,U);e0=-2*np.sqrt(2)*L
inv=np.zeros_like(EE);sel=abs(EE-e0)>1e-9;inv[sel]=1/(e0-EE[sel]);R=(UU*inv)@UU.T
K=W.T@V@R@V@W;I2=np.eye(2)
expected=-sum(kron(I2,I2,I2)+(kron(t1,t1,I2)+kron(t2,t2,I2))/2 for _ in [0])/np.sqrt(2)
expected+=-(kron(I2,I2,I2)+(kron(I2,t1,t1)+kron(I2,t2,t2))/2)/np.sqrt(2)
assert np.max(abs(K-expected))<1e-12
assert np.max(abs(W.T@V@W))<1e-12 and np.max(abs(W.T@O@W))<1e-12
O2=W.T@(V@R@O@R@V+O@R@V@R@V+V@R@V@R@O)@W
paulis=[I2,t1,t2,t3];coeff=[]
for word in itertools.product(range(4),repeat=L):
 c=np.trace(kron(*(paulis[i] for i in word))@O2)/8
 if abs(c)>1e-9:coeff.append(dict(word=word,coefficient_real=float(c.real),imag=float(c.imag)))
rows=[]
for lam in [.01,.025,.05,.1,.2]:
 ev,u=np.linalg.eigh(H0+lam*V);low=u[:,:8]
 # Canonical polar alignment of low spectral subspace to unperturbed rung band.
 Q,_=polar(low.T@W);aligned=low@Q
 effectiveO=aligned.T@O@aligned
 effectiveH=aligned.T@(H0+lam*V)@aligned
 rows.append(dict(lambda_z=lam,band_gap=float(ev[8]-ev[7]),H_error=float(np.linalg.norm(effectiveH-e0*np.eye(8)-lam**2*K)),O_error=float(np.linalg.norm(effectiveO-lam**2*O2)),O2_relative_error=float(np.linalg.norm(effectiveO/lam**2-O2)/np.linalg.norm(O2)),min_band_projection_singular=float(min(np.linalg.svd(low.T@W,compute_uv=False)))))
out=dict(onsite_spectrum=E.tolist(),XY_coefficient_at_Jperp1='-Jz^2/(2 sqrt(2)) multiplying tau1 tau1 + tau2 tau2',K_error=float(np.max(abs(K-expected))),O2_pauli_coefficients=coeff,rows=rows,scope='Finite weak-longitudinal-coupling expansion of existing native terms; equal-coupling validity and bulk3D scalar not established. Pauli variables encode four original qubits in their two-state low band.')
(P/'neutral_rung_effective.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
