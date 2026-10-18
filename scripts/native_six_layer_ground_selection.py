from pathlib import Path
from fractions import Fraction as F
from math import comb
import json
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_LAYER_GROUND_SELECTION_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_LAYER_NEUTRAL_POLE_PROOF.md','.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md']
rows=[]
for n in range(4,13):
 full=(1<<n)-1; dp=[F(0)]*(full+1);dp[0]=F(1)
 for mask in range(1,full+1):
  total=sum((dp[mask^(1<<i)] for i in range(n) if mask>>i&1),F(0))
  c=sum(bool(mask>>i&1) and not bool(mask>>((i-1)%n)&1) for i in range(n))
  dp[mask]=total if mask==full else total/c
 assert dp[full]==comb(2*n-2,n-1)
 R=2*n; t=2*dp[full]*F(63,8192)**n/F(3,8)**(n-1)
 rows.append(dict(R=R,ordering_sum=str(dp[full]),t_R=str(t),leading_power=R+4))
# Exhaust all flat patterns at manageable sizes with the simultaneous-complement gauge fixed.
flat=[]
for R in [4,6,8]:
 weights=[]
 for a in range(1<<R):
  for b in range(1<<(R-1)):
   k=a.bit_count();l=b.bit_count();w=R*(k+l)-2*k*l
   if w:weights.append(w)
 assert min(weights)==R and weights.count(R)==2*R
 flat.append(dict(R=R,min_nonzero_weight=min(weights),minimizers=weights.count(R)))
# Weighted order bound, including redundant columns and larger native jumps.
for r in range(1,8):
 for extra in range(12):
  total=2*r+2*extra
  assert 3*total-4*(r-1)==total+4+4*extra
out=dict(status='conditional-support',matching_controls=rows,flat_controls=flat,scope='Fixed-R sufficiently weak coupling; no uniform size threshold. Finite checks corroborate the analytic proof, not replace it.')
p=ROOT/'outputs/native_six_layer_ground_selection/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
