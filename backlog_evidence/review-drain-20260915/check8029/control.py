"""Independent exact local-normality support checks; no primary imports/runs."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib,time
start=time.monotonic();checks=[]
def ck(n,b):
 assert b,n
 checks.append(n)
# Whole grouped plaquette support {0,e1,e2,e3}; exactly four translates meet0.
S={(0,0,0),(1,0,0),(0,1,0),(0,0,1)}
meet=[z for z in product(range(-1,2),repeat=3) if tuple(-x for x in z) in S]
ck('four_touching_groups',len(meet)==4)
# For rho=|sqrt(1-q),sqrt(q)><...|, rho-PrhoP has determinant -q(1-q),
# trace q; its trace norm squared is q^2+4q(1-q)=4q-3q^2.
for q in [F(1,100),F(1,9),F(1,4),F(1,2),F(1)]:
 norm2=4*q-3*q*q
 ck('gentle_projection_'+str(q),0<=norm2<=4*q)
 if q<1:ck('mass_alone_not_trace_distance_'+str(q),norm2>q*q)
# Energy tail Markov estimate, exact finitely supported densities with coherences
# irrelevant to diagonal energy trace. This is not a full compactness proof.
for probs in [(F(1,2),F(1,3),F(1,6)),(F(1,7),F(2,7),F(4,7))]:
 energies=(0,3,11);E=sum(p*t for p,t in zip(probs,energies))
 for cutoff in (2,5,10):
  tail=sum(p for p,t in zip(probs,energies) if t>cutoff)
  ck('tail_'+str(probs)+'_'+str(cutoff),tail<=E/cutoff)
out={'passed':len(checks),'checks':checks,'elapsed_sec':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact local incidence, gentle-compression and energy-tail identities supporting normality reasoning; full imported GNS and resolvent limit read analytically.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
