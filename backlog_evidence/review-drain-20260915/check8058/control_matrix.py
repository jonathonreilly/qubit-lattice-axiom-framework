from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time
st=time.monotonic();w=Path('/private/tmp/review-drain-20260915/unit8058');data=w/'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs';frame=json.loads((data/'FRAME_RESULT.json').read_text());prefix=json.loads((data/'PREFIXES.json').read_text());spec=importlib.util.spec_from_file_location('comparison_core',w/'scripts/native_weak_electric_rational_core_2026_09_08.py');core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core);model=core.ExactModel(frame,prefix)
# Independent direct ordered CAR application, no compressed two-bit formula.
mask=(1<<0)|(1<<1);K=[row[:] for row in model.K]
for e in (0,1):
 i,j=model.edges[e];K[i][j]*=-1;K[j][i]*=-1
Q=[[-sum(model.r[i][v]*K[v][z]*model.kr[j][z] for v in range(64) for z in range(64))/12 for j in range(10)] for i in range(10)]
actual={};closing=[]
for col,b in enumerate(model.states):
 actual[col,col]=F(10)
 for i in range(10):
  for j in range(10):
   mid=b^(1<<j);a=mid^(1<<i);sgn=(-1)**((b&((1<<j)-1)).bit_count()+(mid&((1<<i)-1)).bit_count())
   factor=1/model.d[i] if i==j else model.d[i]**(((b>>i)&1)-1)*model.d[j]**(((b>>j)&1)-1)
   key=(model.ix[a],col);actual[key]=actual.get(key,F(0))-Q[i][j]*F(sgn,2)*(1-2*((b>>j)&1))*factor
actual={k:v for k,v in actual.items() if v};target={k:F(v,model.den) for k,v in model.matrix(mask).items()};assert actual==target
assert all(model.W[i]*a==model.W[j]*actual.get((j,i),F(0)) for (i,j),a in actual.items())
# Closing row norm derives from gamma_v gamma_w unit norm, not a fitted coefficient.
assert sum(x*x/d for x,d in zip(model.ell,model.W))==6
# Recompute one dyadic residual entirely with Fraction vector operations.
cand=([(-1)**i*(i%7) for i in range(512)],8);incoming=([int(i==0) for i in range(512)],1);res=[-F(z,2) for z in incoming[0]]
for (i,j),a in actual.items():res[i]-=a*F(cand[0][j],cand[1])
square=sum(d*x*x for d,x in zip(model.W,res));upper=core.residual(model,model.matrix(mask),cand,[incoming]);assert upper*upper>=square and (upper-F(1,10**50))**2<square
out={'matrix_entries_compared':512**2,'actual_nonzeros':len(actual),'mask':str(mask),'scope':'Direct ordered CAR versus compressed rational sparse matrix on one actual512-state prefix; exact weighted self-adjointness and Fraction residual against integer implementation. No physical solve or all-prefix execution.','seconds':time.monotonic()-st};Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
