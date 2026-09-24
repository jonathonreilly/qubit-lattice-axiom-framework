#!/usr/bin/env python3
"""Exact physical four-site matrices, authored personally before review.
Construct F and unchanged j from local hard-core states and Gauss-fixed fields.
The test graph is a single degree-three A vertex. No cube builder is imported.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/exact_star_energy.py',)
from pathlib import Path
from itertools import product
import json
import sympy as s
HERE=Path(__file__).resolve().parent
e=s.symbols('epsilon',positive=True)
delta,kappa=s.symbols('delta kappa',positive=True)
# All charge configurations in the Gauss sector sum(q)=1.
bases={N:tuple(q for q in product((-1,0,1),repeat=4) if sum(q)==1 and sum(x*x for x in q)==N) for N in (1,3)}
def fields(q):return tuple(-q[b] for b in (1,2,3))
def check_gauss(q):
 E=fields(q)
 return sum(E)==q[0]-1 and all(-E[b-1]==q[b] for b in (1,2,3))
def local_F(N):
 base=bases[N];idx={q:i for i,q in enumerate(base)};F=s.zeros(len(base))
 for col,q in enumerate(base):
  for b in (1,2,3):
   if q[0] and not q[b]:
    r=list(q);r[b]=q[0];r[0]=0;r=tuple(r)
    # Normalized spin transition is 0 -> +/-1 and has coefficient 1
    # for every integer S >= 1. Check the field change, not just q.
    E=list(fields(q));E[b-1]-=q[0]
    assert tuple(E)==fields(r)
    F[idx[r],col]+=1
 return F
def jump(b,sign):
 out=s.zeros(len(bases[3]),len(bases[1]));idx={q:i for i,q in enumerate(bases[3])}
 for col,q in enumerate(bases[1]):
  if q[0]==0 and q[b]==0:
   r=list(q);r[0]=sign;r[b]=-sign;r=tuple(r)
   E=list(fields(q));E[b-1]+=sign
   assert tuple(E)==fields(r)
   out[idx[r],col]=1
 return out
def simp(M):return M.applyfunc(s.simplify)
def scalar(M):return s.factor(M[0])
operators={}
for N,base in bases.items():
 assert all(check_gauss(q) for q in base)
 F=local_F(N);W=s.diag(*[int(q[0]==0) for q in base]);C=F.T*F
 # D_S-D_infinity vanishes on these physical sectors because the field
 # on each active outward edge is zero. Q_a is the empty product.
 for q in base:
  for b in (1,2,3):
   if q[0] and not q[b]:assert fields(q)[b-1]==0
 h=W-e*(F+F.T)+e**2*C
 L=W-e*F
 assert simp(h-L.T*L)==s.zeros(len(base))
 assert F*F==s.zeros(len(base))
 operators[N]=(F,W,h)
F1,W1,h1=operators[1];F3,W3,h3=operators[3]
v0=s.zeros(4,1);v0[bases[1].index((1,0,0,0))]=1
psi_num=v0+e*F1*v0
norm=scalar(psi_num.T*psi_num)
assert norm==1+3*e**2
assert h1*psi_num==s.zeros(4,1)
# Polynomial spectral identity proves the full N=3 spectrum; no tolerance.
assert simp(h3*h3-(1+3*e**2)*h3)==s.zeros(12)
assert s.simplify(s.trace(h3)-3*(1+3*e**2))==0
P_hi=simp(h3/(1+3*e**2))
assert simp(P_hi*P_hi-P_hi)==s.zeros(12)
assert simp(P_hi-P_hi.T)==s.zeros(12)
assert F3*F3.T==3*W3
rows=[];drift={}
for label in ('resolved','coherent'):
 total=s.Integer(0)
 for b in (1,2,3):
  marks=[(str(sig),jump(b,sig)) for sig in (1,-1)] if label=='resolved' else [('coherent',jump(b,1)+jump(b,-1))]
  for mark,j in marks:
   out=simp(j*psi_num)
   nn=scalar(out.T*out)
   rate=s.factor(kappa/e**2*nn/norm)
   E=s.factor(delta/e**4*scalar(out.T*h3*out)/nn)
   E2=s.factor(delta**2/e**8*scalar(out.T*h3*h3*out)/nn)
   p=s.factor(scalar(out.T*P_hi*out)/nn)
   var=s.factor(E2-E**2)
   assert s.simplify(E-p*delta/e**4*(1+3*e**2))==0
   assert s.simplify(var-p*(1-p)*(delta/e**4*(1+3*e**2))**2)==0
   assert W3*out==s.zeros(12,1) # Bare W population is exactly zero.
   # Leading target B is obtained directly from the microscopic matrices.
   Bv=j*F1*v0
   assert out==e*Bv
   c=scalar(Bv.T*F3.T*F3*Bv)/scalar(Bv.T*Bv)
   assert s.simplify(E-c*delta/e**2)==0
   total+=rate*E
   rows.append({'instrument':label,'edge':[0,b],'mark':mark,'rate':str(rate),
    'target_B_norm_squared':str(scalar(Bv.T*Bv)),'c':str(c),
    'conditional_energy':str(E),'high_spectral_probability':str(p),
    'conditional_energy_variance':str(var),
    'physical_output':[{ 'q':list(q),'E':list(fields(q)),'unnormalized_amplitude':str(Bv[i])} for i,q in enumerate(bases[3]) if Bv[i]]})
 drift[label]=str(s.factor(total))
assert drift['resolved']==drift['coherent']
result={'scope':'Exact supplied original formation model on one A center with three B leaves; not a repeated-birth graph',
 'basis_dimensions':{str(N):len(base) for N,base in bases.items()},
 'physical_bases':{str(N):[{'q':list(q),'E':list(fields(q))} for q in base] for N,base in bases.items()},
 'F_matrices':{str(N):op[0].tolist() for N,op in operators.items()},
 'initial_energy':'0','dressed_input_norm_squared':str(norm),
 'N3_high_dimensionless_eigenvalue':str(1+3*e**2),'N3_high_multiplicity':3,
 'N3_low_eigenvalue':'0','N3_low_multiplicity':9,
 'bare_A_input_energy':str(s.factor(delta/e**4*scalar(v0.T*h1*v0))),
 'bare_A_initial_dissipative_energy_derivative':'0',
 'rows':rows,'dressed_initial_energy_derivative':drift,
 'physical_Gauss_check':True,'spin_scope':'All integer S>=1, exact normalized amplitudes 0 <-> +/-1',
 'identities':'Exact symbolic matrix equality; idempotent high spectral projector; square factorization; all actual jump outputs'}
(HERE/'EXACT_STAR_ENERGY_RESULTS.json').write_text(json.dumps(result,default=str,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('basis_dimensions','initial_energy','N3_high_dimensionless_eigenvalue','dressed_initial_energy_derivative')},indent=2))
for row in rows[:3]:print(json.dumps({k:row[k] for k in ('instrument','mark','rate','conditional_energy','high_spectral_probability','conditional_energy_variance')}))
