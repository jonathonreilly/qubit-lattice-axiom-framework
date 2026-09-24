#!/usr/bin/env python3
"""Independent rate-control ingredients from local charge/link actions.
No campaign builder is imported. Exact checks precede numerical illustrations.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
import json, math
import numpy as np
import scipy.linalg as la
import sympy as s
HERE=Path(__file__).resolve().parent
A=(0,3,5,6);B=(1,2,4,7)
edges=tuple((a,b) for a in A for b in B if (a^b) in (1,2,4))
chords=(0,5,7,8,10)
qs=[q for q in product((-1,0,1),repeat=8) if sum(x!=0 for x in q)==6 and sum(q)==4]
lookup={q:i for i,q in enumerate(qs)}
mid=[i for i,q in enumerate(qs) if sum(q[a]==0 for a in A)==1]
qm=[qs[i] for i in mid]; mi={q:i for i,q in enumerate(qm)}
dark=[i for i,q in enumerate(qm) if not any(q[a]==q[b]==0 for a,b in edges)]
bright=[i for i in range(len(qm)) if i not in dark]
trans=[]
for j,q in enumerate(qs):
 for e,(a,b) in enumerate(edges):
  if q[a] and not q[b]:
   qq=list(q);qq[b]=qq[a];qq[a]=0
   winding=[0]*5
   if e in chords:winding[chords.index(e)]=-q[a]
   trans.append((lookup[tuple(qq)],j,tuple(winding)))
F0=s.zeros(len(qs))
for i,j,z in trans:F0[i,j]+=1
G0=(F0*F0.T-F0.T*F0).extract(mid,mid)
Gamma=s.diag(*[0 if i in dark else 2 for i in range(96)])
u=s.Matrix([int(i in dark) for i in range(96)])
assert len(qs)==168 and len(mid)==96 and len(dark)==24
assert G0*u==s.zeros(96,1) and Gamma*u==s.zeros(96,1)
Q=G0.extract(bright,dark);rank=Q.rank()
assert rank==23
assert G0.extract(dark,dark)==s.zeros(24)
# Physical finite-word construction keeps all fields distinct.
def transport(vec,center=None):
 out=defaultdict(int)
 for (q,E),v in vec.items():
  for ei,(a,b) in enumerate(edges):
   if center is not None and a!=center:continue
   if q[a] and not q[b]:
    qq=list(q);ee=list(E);qq[b]=qq[a];ee[ei]-=qq[a];qq[a]=0
    out[(tuple(qq),tuple(ee))]+=v
 return {key:v for key,v in out.items() if v}
def mark(vec,signs):
 out=defaultdict(int)
 for (q,E),v in vec.items():
  if q[0] or q[1]:continue
  for sign in signs:
   qq=list(q);ee=list(E);qq[0]=sign;qq[1]=-sign;ee[0]+=sign
   out[(tuple(qq),tuple(ee))]+=v
 return {key:v for key,v in out.items() if v}
g={(tuple(int(i in A) for i in range(8)),(0,)*12):1}
records=[];rvectors=[]
for name,signs in [('resolved_plus',(1,)),('resolved_minus',(-1,)),('coherent',(1,-1))]:
 bv=mark(transport(g),signs);rv={k:-v for k,v in transport(bv,0).items()}
 b=sum(v*v for v in bv.values());r=sum(v*v for v in rv.values())
 flat=s.zeros(96,1)
 for (q,E),v in rv.items():
  assert mi[q] in dark
  flat[mi[q]]+=v
 alpha2=s.factor((u.T*flat)[0]**2/(24*s.Integer(b)))
 M=s.simplify(sum(abs(v) for v in rv.values())/s.sqrt(b))
 lip=s.simplify(sum(abs(v)*s.sqrt(sum(E[c]**2 for c in chords)) for (q,E),v in rv.items())/s.sqrt(b))
 records.append({'mark':name,'b':b,'physical_R_norm_squared':r,'flat_projection_squared_normalized':str(alpha2),'uniform_fiber_norm_bound_M':str(M),'fiber_Lipschitz_bound_d':str(lip),'physical_R':[{'q':q,'E':E,'coefficient':v} for (q,E),v in sorted(rv.items())]})
 rvectors.append((rv,b))
assert [(x['b'],x['physical_R_norm_squared'],x['flat_projection_squared_normalized']) for x in records]==[(2,4,'1/12'),(2,2,'1/12'),(4,6,'1/6')]
# A physically different relative-minus coherent mark is a discriminator:
# its equal-dark projection vanishes, so this theorem's input hypothesis fails.
mutant=defaultdict(int)
for (rv,b),sign in zip(rvectors[:2],(1,-1)):
 for word,value in rv.items():mutant[word]+=sign*value
mutant={word:value for word,value in mutant.items() if value}
mutant_projection=s.factor(s.Integer(sum(mutant.values()))**2/96)
assert mutant_projection==0
# Independent finite-matrix perturbation illustrations, not a proof by samples.
un=np.array(u,dtype=float).ravel()/math.sqrt(24)
U=la.null_space(un.reshape(1,-1))
Gzero=np.array(G0,dtype=float);gam=np.array(Gamma,dtype=float)
def G(theta):
 f=np.zeros((168,168),complex)
 for i,j,z in trans:f[i,j]+=np.exp(1j*np.dot(theta,z))
 return (f@f.conj().T-f.conj().T@f)[np.ix_(mid,mid)]
def rhat(theta,rv,b):
 r=np.zeros(96,complex)
 for (q,E),v in rv.items():r[mi[q]]+=v*np.exp(1j*np.dot(theta,[E[c] for c in chords]))/math.sqrt(b)
 return r
samples=[]
direction=np.array([1,-2,3,1,-1],float);direction/=la.norm(direction)
for delta,kappa in [(1.,1.),(.7,1.3),(2.,.4)]:
 A0=-1j*delta*Gzero-kappa*gam/2
 B0=U.conj().T@A0@U
 m=la.norm(la.inv(B0),2);L=240*delta;beta=64*kappa*m*m*L*L
 assert la.norm(A0@un)<1e-12 and la.norm(un@A0)<1e-12
 for scale in [1e-2,5e-3,2.5e-3]:
  theta=scale*direction;At=-1j*delta*G(theta)-kappa*gam/2
  vals,vl,vr=la.eig(At,left=True,right=True)
  idx=np.argmin(np.abs(vals));ev=vals[idx];v=vr[:,idx];l=vl[:,idx]
  P=np.outer(v,l.conj())/np.vdot(l,v)
  energy_real=-kappa*la.norm(v[bright])**2/la.norm(v)**2
  assert abs(ev.real-energy_real)<2e-11
  assert la.norm(P@P-P)<1e-11
  assert la.norm(G(theta)-Gzero,2)<=240*la.norm(theta)+1e-12
  overlaps=[float(la.norm(P@rhat(theta,rv,b))**2) for rv,b in rvectors]
  samples.append({'delta':delta,'kappa':kappa,'phase_radius':scale,'lambda_real':float(ev.real),'lambda_imag':float(ev.imag),'minus_real_over_radius_squared':float(-ev.real/scale**2),'projection_norm':float(la.norm(P,2)),'normalized_projected_input_norm_squared':overlaps,'complement_inverse_norm_m':float(m),'conservative_quadratic_bound_beta':float(beta)})
result={'scope':'Exact local flat-fiber and physical-input certificates plus finite numerical perturbation illustrations; the global polynomial lower bound is proved analytically in PRE_RATE_ARGUMENT.md.','all_assertions_passed':True,'charge_order':qm,'dark_indices':dark,'bright_indices':bright,'G_zero':[[int(x) for x in G0.row(i)] for i in range(96)],'Gamma_diagonal':[int(Gamma[i,i]) for i in range(96)],'exact_flat_bright_dark_rank':rank,'flat_uniform_dark_right_and_left_null':True,'actual_first_marks':records,'relative_minus_mark_discriminator_projection_squared':str(mutant_projection),'numerical_perturbation_samples':samples}
(HERE/'LOCAL_RATE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'exact_flat_bright_dark_rank':rank,'actual_first_marks':[{k:v for k,v in row.items() if k!='physical_R'} for row in records],'numerical_perturbation_samples':samples},indent=2))
print('per_element: exact local charge moves retain each integer electric word and its amplitude.')
print('per_site: all eight cube sites enter the complete fixed-charge matter enumeration.')
print('per_mode: exact flat-fiber null mode and nearby numerical spectral projections are checked.')
print('per_block: the complete 96-dimensional W=1 block and its 24-dimensional dark subspace are checked.')
print('lattice_wide: checked and not executed — no growing-lattice or other-graph rate theorem is claimed.')
