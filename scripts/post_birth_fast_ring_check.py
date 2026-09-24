
AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/post_birth_fast_ring_check.py',)
from pathlib import Path
from itertools import permutations
import json,hashlib
import numpy as np
from scipy.linalg import eigh
from scipy.special import j0

# Unit-rotor Fourier fiber of the six-site ring, N=5,Q=3.
qs=sorted(set(permutations([0,-1,1,1,1,1])))
ix={q:i for i,q in enumerate(qs)};P=[i for i,q in enumerate(qs) if all(q[a] for a in (0,2,4))];Q=[i for i in range(len(qs)) if i not in P]
# Resolved formation on edge 0 after the plus record hopped 0->5.
initial=(1,-1,1,0,1,1);start=P.index(ix[initial]);stay=[a for a,i in enumerate(P) if qs[i][3]==0]
def fiber(theta):
 T=np.zeros((30,30),complex)
 for col,q in enumerate(qs):
  for e in range(6):
   x,y=e,(e+1)%6
   for a,b,orientation in [(x,y,1),(y,x,-1)]:
    if q[a] and not q[b]:
     qq=list(q);charge=q[a];qq[a]=0;qq[b]=charge
     # Flux coordinate is E_0. Only an edge-zero shift changes it.
     change=-orientation*charge if e==0 else 0
     T[ix[tuple(qq)],col]=-np.exp(1j*change*theta)
 assert np.max(abs(T-T.conj().T))<1e-14
 A=T[np.ix_(Q,P)];H2=-A.conj().T@A
 assert np.max(abs(np.diag(H2)+2))<1e-14
 assert all(np.count_nonzero(abs(row)>1e-12)==3 for row in H2)
 return H2
# Exact integer-exponent certificate for the two-hop graph.
terms={}
for col,q in enumerate(qs):
 for e in range(6):
  x,y=e,(e+1)%6
  for a,b,orientation in [(x,y,1),(y,x,-1)]:
   if q[a] and not q[b]:
    qq=list(q);charge=q[a];qq[a]=0;qq[b]=charge
    terms[ix[tuple(qq)],col]=-orientation*charge if e==0 else 0
arcs={}
for ci,p in enumerate(P):
 for ri,r in enumerate(P):
  if ci==ri:continue
  exps=[terms[q,p]-terms[q,r] for q in Q if (q,p) in terms and (q,r) in terms]
  if exps:
   assert len(exps)==1
   arcs[ci,ri]=exps[0]
assert len(arcs)==30
for a in range(15):
 neighbors=[b for c,b in arcs if c==a]
 assert len(neighbors)==2
 for b in neighbors:assert arcs[a,b]==-arcs[b,a]
order=[start];current=start;previous=None;holonomy=0
for k in range(15):
 neighbors=sorted(b for a,b in arcs if a==current and b!=previous)
 nxt=neighbors[0]
 holonomy+=arcs[current,nxt]
 previous,current=current,nxt
 if k<14:
  assert current not in order
  order.append(current)
assert current==start and sorted(order)==list(range(15)) and abs(holonomy)==3
vacancies=[qs[P[a]].index(0) for a in order]
step=(vacancies[1]-vacancies[0])%6
assert step in (2,4) and all(v==(vacancies[0]+step*k)%6 for k,v in enumerate(vacancies))
exact_graph={'cycle_length':15,'two_hop_diagonal':-2,'off_diagonal_magnitude':1,'ordered_charge_words':[list(qs[P[a]]) for a in order],'vacancy_positions':vacancies,'oriented_flux_increment_after_one_cycle':holonomy,'conclusion':'The fixed integer-flux initial state belongs to an infinite path component: one full 15-step matter circuit changes the integer flux by three. Vacancy position repeats every three path steps.'}
spectra=[]
for theta in [0,np.pi/7,np.pi/2,np.pi]:
 H=fiber(theta);ev=eigh(H,eigvals_only=True)
 expected=np.sort([-2-2*np.cos((2*np.pi*k+3*theta)/15) for k in range(15)])
 err=float(max(abs(ev-expected)));assert err<1e-13
 r=np.zeros((15,15));r[start,start]=1
 spectra.append({'theta':theta,'eigenvalues':ev.tolist(),'formula_error':err,'post_mark_commutator_frobenius':float(np.linalg.norm(H@r-r@H))})
controls=[]
for grid in [64,128,256]:
 probs=np.zeros(6)
 for k in range(grid):
  ev,V=eigh(fiber(2*np.pi*k/grid))
  for a,u in enumerate([0,.125,.25,.5,1,2]):
   psi=V@(np.exp(-1j*u*ev)*V[start,:].conj())
   probs[a]+=float(sum(abs(psi[j])**2 for j in stay))/grid
 for u,p in zip([0,.125,.25,.5,1,2],probs):
  target=(1+2*j0(2*np.sqrt(3)*u))/3
  assert abs(p-target)<2e-13
  controls.append({'grid':grid,'fast_time':u,'vacancy_still_at_B3':p,'bessel_prediction':float(target),'absolute_error':float(abs(p-target))})
out={'model':'six-site unit-rotor ring Fourier fibers, one vacancy, one minus record and four plus records','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'P_dimension':15,'Q1_dimension':15,'exact_graph_certificate':exact_graph,'initial_resolved_birth_output':initial,'spectra':spectra,'controls':controls,'interpretation':'Supplied-model author probe only. The initial state is normalizable at one electric flux; Fourier integration computes its matter probability. No full-time field or repeated-birth theorem is inferred.'}
path=Path(__file__).with_name('POST_BIRTH_FAST_RING_RESULTS.json');assert not path.exists();path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
