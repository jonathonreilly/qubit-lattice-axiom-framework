"""Fourth-order canonical finite rung-band interaction, native bonds only."""
from pathlib import Path
import numpy as np,json,itertools
from scipy.linalg import polar
from neutral_rung_model import h,Ds,kron
P=Path(__file__).resolve().parent
E,U=np.linalg.eigh(h);w=U[:,:2];t1=np.sqrt(2)*w.T@Ds[0]@Ds[1]@w;t2=np.sqrt(2)*w.T@Ds[0]@Ds[2]@w;t3=-1j*t1@t2
I=np.eye(8);H0=kron(h,I,I)+kron(I,h,I)+kron(I,I,h);V=-sum(kron(d,d,I)+kron(I,d,d) for d in Ds)
W=kron(w,w,w);EE=np.array([sum(x) for x in itertools.product(E,repeat=3)]);UU=kron(U,U,U);e0=-6*np.sqrt(2)
inv=np.zeros_like(EE);sel=abs(EE-e0)>1e-9;inv[sel]=1/(e0-EE[sel]);R=(UU*inv)@UU.T
K2=W.T@V@R@V@W;N2=W.T@V@R@R@V@W
K4=W.T@V@R@V@R@V@R@V@W-(N2@K2+K2@N2)/2
paulis=[np.eye(2),t1,t2,t3];coeff=[]
for word in itertools.product(range(4),repeat=3):
 c=np.trace(kron(*(paulis[i] for i in word))@K4)/8
 if abs(c)>1e-9:coeff.append(dict(word=word,coefficient_real=float(c.real),imag=float(c.imag),coefficient_times_sqrt2=float((c*np.sqrt(2)).real)))
charge=kron(t3,np.eye(2),np.eye(2))+kron(np.eye(2),t3,np.eye(2))+kron(np.eye(2),np.eye(2),t3)
rows=[]
for lam in [.02,.04,.08,.16,.3]:
 ev,u=np.linalg.eigh(H0+lam*V);low=u[:,:8];Q,_=polar(low.T@W);aligned=low@Q;hh=aligned.T@(H0+lam*V)@aligned
 err=float(np.linalg.norm(hh-e0*np.eye(8)-lam**2*K2-lam**4*K4))
 rows.append(dict(lambda_z=lam,fourth_order_error=err,error_over_lambda6=err/lam**6,second_order_error=float(np.linalg.norm(hh-e0*np.eye(8)-lam**2*K2))))
out=dict(K4_pauli_coefficients=coeff,commutator_with_total_tau3_norm=float(np.linalg.norm(K4@charge-charge@K4)),rows=rows,scope='Finite three-rung canonical perturbative interaction. Fourth-order source derived from native H; not an all-orders U1 symmetry or equal-coupling/bulk claim.')
(P/'neutral_rung_fourth.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
