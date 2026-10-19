"""Rational residual enclosures around numerical eigenvectors; exact arithmetic bounds."""
from pathlib import Path
import json,numpy as np,sympy as S
P=Path(__file__).resolve().parent;R=P.parents[3];raw=(R/'data/collective_corner_response/candidate.json').read_text();d=json.loads(raw,parse_float=S.Rational);c=json.loads((P/'exact_no_flat_transition.json').read_text());sh=d['shifts'];I=S.I
B=[S.Matrix(12,12,lambda i,j:d['blocks']['real'][t][i][j]+I*d['blocks']['imag'][t][i][j]) for t in range(7)]
def clean(A):return A.applyfunc(S.expand)
def l1(z):return abs(S.re(z))+abs(S.im(z))
def bound(A):
 return max(max(sum(l1(A[i,j]) for j in range(A.cols)) for i in range(A.rows)),max(sum(l1(A[i,j]) for i in range(A.rows)) for j in range(A.cols)))
def enclosure(A):
 A=clean(A);assert A==A.H
 e,u=np.linalg.eigh(np.array(A.tolist(),dtype=complex))
 D=S.diag(*[S.Rational(str(x)) for x in e]);U=S.Matrix(12,12,lambda i,j:S.Rational(str(u[i,j].real))+I*S.Rational(str(u[i,j].imag)))
 delta=bound(clean(U.H*U-S.eye(12)));r=bound(clean(A*U-U*D));assert delta<1
 error=r+(bound(A)+max(abs(x) for x in D.diagonal()))*delta
 return list(D.diagonal()),error,dict(orthogonality_bound=str(delta),residual_bound=str(r),eigenvalue_error_bound=str(error),error_float=float(error))
allvals=[];errors=[];receipts=[]
for point in c['phase_triples']:
 z=[S.Rational(a,cc)+I*S.Rational(b,cc) for a,b,cc in point];hs=[]
 for staggered in [False,True]:
  h=S.zeros(12)
  for shift,block in zip(sh,B):
   phase=S.prod(x**n for x,n in zip(z,shift));phase=S.expand_complex(phase)
   h+=(-1 if staggered and sum(shift)%2 else 1)*phase*block
  hs.append(enclosure(h))
 e,err,receipt=hs[0];eq,errq,receiptq=hs[1];allvals.append([b-a for a in e for b in eq]);errors.append(err+errq);receipts.extend([receipt,receiptq]);print('point complete errors',float(err),float(errq),flush=True)
sep=min(abs(x-y) for x in allvals[0] for y in allvals[1]);lower=sep-sum(errors);assert lower>0
# Each of7 12x12 hopping blocks may change each complex entry by epsilon,
# preserving paired Hermiticity. ||delta h||<=84 epsilon; cross-difference
# separation can fall by at most4*84 epsilon.
radius=lower/336
out=dict(scope='Exact rational enclosures for stored decimal model and chosen rational phases; all four eigenvalue lists certified through polar-decomposition residual bound; Hermiticity-preserving entrywise perturbations smaller than stated radius retain separated transition spectra',receipts=receipts,separation_lower_bound=str(lower),separation_lower_float=float(lower),entry_perturbation_radius=str(radius),entry_radius_float=float(radius))
(P/'rational_spectral_enclosure.json').write_text(json.dumps(out,indent=2)+'\n');print('certified lower separation',float(lower),'entry radius',float(radius))
