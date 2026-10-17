#!/usr/bin/env python3
"""Different assembly/path checks: full four-qubit Pauli operator and finite leads.

The finite lead uses only an outgoing vacuum-channel termination; all closed
channels end at a hard wall. No closed-channel matrix square root is used.
This is an author different-path check, not independent reviewer acceptance.
"""
from pathlib import Path
from fractions import Fraction as F
import json,time,sys
import numpy as np
import scipy
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve
import sympy as sy
OUT=Path(__file__).resolve().parent/'evidence';start=time.monotonic()
c=json.loads((OUT/'rational_point_certificate.json').read_text());P={k:F(v) for k,v in c['exact_parameters'].items()}
I=np.eye(2,dtype=object);I[:]=[[F(1),F(0)],[F(0),F(1)]]
X=np.array([[F(0),F(1)],[F(1),F(0)]],object);Z=np.diag([F(1),F(-1)])
n=(I-Z)/2;a=np.array([[F(0),F(1)],[F(0),F(0)]],object)
def kron(xs):
 y=np.array([[F(1)]],object)
 for x in xs:y=np.kron(y,x)
 return y
def site(x,j):return kron([x if k==j else I for k in range(4)])
E16=kron([I]*4);xs=[site(X,j) for j in range(4)];ns=[site(n,j) for j in range(4)]
K=2*E16+site(Z,0)@site(Z,1)
hop=site(a.T,2)@site(a,3)+site(a.T,3)@site(a,2)
B=K+P['DeltaA']*ns[2]+P['DeltaB']*ns[3]+P['t']*(ns[2]+ns[3]-hop)+P['u']*ns[2]@ns[3]
B+=P['gA']*ns[2]@(E16+xs[0])+P['gB']*ns[3]@(E16+xs[1])
VA=P['lambdaA']*(E16+xs[2])+P['mu0']*E16
VB=P['lambdaB']*(E16+xs[3])+P['mu1']*E16
Jvac=np.zeros((16,4),object);Jvac[:]=F(0)
for old in range(4):Jvac[4*old,old]=F(1)
Kold=2*np.eye(4,dtype=object)+np.kron(Z,Z)
assert np.array_equal(B@Jvac,Jvac@Kold)
assert np.array_equal(B@(xs[0]@xs[1]),(xs[0]@xs[1])@B)
blocks={};states={};spectra=[]
for p in [1,-1]:
 T=np.zeros((16,8),object);T[:]=F(0)
 vp=np.array([F(1),F(0),F(0),F(p)],object)
 vm=np.array([F(0),F(p),F(1),F(0)],object)
 for source in range(4):
  for ss,v in enumerate([vp,vm]):
   for old in range(4):T[old*4+source,source*2+ss]=v[old]
 block=T.T@B@T/2;blocks[p]=block
 # A second source-by-source algebraic reconstruction.
 expected=np.zeros((8,8),object);expected[:]=F(0)
 for source in range(4):
  aa=(source>>1)&1;bb=source&1
  diagonal=P['DeltaA']*aa+P['DeltaB']*bb+P['t']*(aa+bb)+P['u']*aa*bb+P['gA']*aa+P['gB']*bb
  f=P['gA']*aa+p*P['gB']*bb
  expected[2*source:2*source+2,2*source:2*source+2]=np.array([[3+diagonal,f],[f,1+diagonal]],object)
 for ss in [0,1]:expected[2+ss,4+ss]=expected[4+ss,2+ss]=-P['t']
 assert np.array_equal(block,expected)
 lam=sy.Symbol('lambda')
 def sr(q):return sy.Rational(q.numerator,q.denominator)
 aA=2+P['DeltaA']+P['t']+P['gA'];aB=2+P['DeltaB']+P['t']+P['gB']
 xa=lam-sr(aA);xb=lam-sr(aB);ga=sr(P['gA']);gb=sr(P['gB']);tt=sr(P['t'])
 quartic=(xa*xb+1+p*ga*gb-tt**2)**2-(xa+xb)**2-(ga*xb+p*gb*xa)**2+(ga-p*gb)**2
 ch=sy.Matrix(block[2:6,2:6].tolist()).charpoly(lam).as_expr()
 assert sy.expand(ch-quartic)==0
 eigen=np.linalg.eigvalsh(np.array(block,float))
 spectra.append(dict(p=p,bulk_eigenvalues=eigen.tolist(),
   complete_bands_without_common_scalar=[[float(v),float(v+4*float(P['J']))] for v in eigen],
   single_excitation_quartic_coefficients=[str(v) for v in sy.Poly(ch,lam).all_coeffs()],
   exact_description='vacuum 1,3; four roots of displayed quartic; double-excitation 2+C +/- sqrt(1+(gA+p*gB)^2)'))
 for s,ss in [(1,0),(-1,1)]:states[s,p]=np.array(T[:,ss],float)/np.sqrt(2)
bf=np.array(B,float);vaf=np.array(VA,float);vbf=np.array(VB,float)
J=float(P['J']);z=complex(float(P['cos_k']),float(P['sin_k']));sn=float(P['sin_k']);eps=float(P['epsilon'])
rows=[]
for L in [12,20,32]:
 for s in [1,-1]:
  E=2+s+eps;incoming=np.column_stack([states[s,1],states[s,-1]])
  open_projector=incoming@incoming.T
  base=sp.kron(sp.eye(L,format='csc'),sp.csc_matrix((E-2*J)*np.eye(16)-bf),format='csc')
  adj=sp.diags([np.ones(L-1),np.ones(L-1)],[-1,1],shape=(L,L),format='csc')
  M=(base+sp.kron(adj,sp.eye(16)*J,format='csc')).tolil().astype(complex)
  M[:16,:16]-=vaf;M[16:32,16:32]-=vbf;M[-16:,-16:]+=J*z*open_projector
  M=M.tocsc();rhs=np.zeros((16*L,2),complex);rhs[-16:]=2j*J*sn*incoming
  solution=spsolve(M,rhs)
  r_end=incoming.T@solution[-16:]-np.eye(2)
  r_reference=r_end*z**(-2*(L-2))
  target=[]
  for p in [1,-1]:
   row=next(v for v in c['channels'] if v['s']==s and v['p']==p)
   target.append(complex(float(F(row['reflection_real'])),float(F(row['reflection_imag']))))
  diff=np.linalg.norm(r_reference-np.diag(target),2)
  residual=np.linalg.norm(M@solution-rhs,np.inf)
  rows.append(dict(L=L,s=s,dimension=16*L,maximum_rhs_columns=2,difference_from_certified_surface=float(diff),
    linear_residual_infinity=float(residual),offdiagonal=float(max(abs(r_reference[0,1]),abs(r_reference[1,0]))),
    r_real=r_reference.real.tolist(),r_imag=r_reference.imag.tolist()))
assert max(r['difference_from_certified_surface'] for r in rows if r['L']==32)<1e-8
result=dict(exact_full_matrix_checks=['vacuum darkness','XX symmetry','two 8x8 block identities'],
 finite_lead_method='full 16-dimensional physical internal tensor; closed channels hard-wall terminated; open vacuum outgoing termination',
 excludes='No independent reviewer, arbitrary-energy certificate, wavepacket evolution or all-future bound',
 bulk_spectra=spectra,source_threshold_lower=float(1+min(P['DeltaA'],P['DeltaB'])),
 physical_common_scalar=float(P['scalar_reserve']),
 rows=rows,versions=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,sympy=sy.__version__),elapsed_seconds=time.monotonic()-start)
(OUT/'different_path_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
