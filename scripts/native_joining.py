from fractions import Fraction as F
import json
from pathlib import Path
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_JOINING_PROOF.md']

def path(J):
 L=len(J)+1;v={0:F(1)}
 for S in range(1,1<<L):
  x=sum(v[S^(1<<i)] for i in range(L) if S>>i&1)
  if S!=(1<<L)-1:
   den=4*sum(J[i] for i in range(L-1) if ((S>>i)^(S>>(i+1)))&1)
   x/=den
  v[S]=x
 pred=F(1)
 for j in J:pred/=2*j
 assert v[(1<<L)-1]==pred
 return str(pred)

out=[]
for g in [F(1,3),F(1),F(2)]:
 out.append(dict(g=str(g),t10=path([F(1)]*4+[g]+[F(1)]*4)))
# Exact representation: choose gauge a0=+; enumerate all a1..3,b0..5.
Nx,Ny=4,6;patterns=[]
for a in range(1<<(Nx-1)):
 aa=[1]+[1-2*((a>>i)&1) for i in range(Nx-1)]
 for b in range(1<<Ny):
  bb=[1-2*((b>>j)&1) for j in range(Ny)]
  patterns.append(tuple(x*y for x in aa for y in bb))
assert len(set(patterns))==512
mismatches=[sum(x!=1 for x in s) for s in patterns]
assert min(k for k in mismatches if k)==4
# Character table of the translation action of Z2^9. Orthogonality via
# exact integer Walsh transform, avoiding floating eigensolver selection.
for h in range(512):
 trace=sum((-1)**((h&x).bit_count()) for x in range(512))
 assert trace==(512 if h==0 else 0)
result=dict(status='bounded-support',pair_coefficients=out,pattern_count=len(patterns),min_pattern_interface_cost_over_g=2*min(k for k in mismatches if k),characters=512,neutral_multiplicity=1,scope='Exact path and representation controls, not240-spin diagonalization or observational test')
p=Path(__file__).resolve().parents[1]/'outputs/native_joining/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
