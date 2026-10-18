"""Exact local second-order kernels of signed interval states; no fitted coefficients."""
import sys,json
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
sys.path.insert(0,'/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native')
from neutral_kink_core import h,bits
moves=[[(i,int(h[i,j])) for i in range(8) if h[i,j]] for j in range(8)]
rows=[]
for L in [16,18]:
 powers=[8**j for j in range(L)];cache={}
 def energy(st):
  if st not in cache:
   ds=[st//p%8 for p in powers];cache[st]=sum(2*(bits[ds[j]]^bits[ds[(j+1)%L]]).bit_count() for j in range(L))
  return cache[st]
 def V(vec):
  out=defaultdict(F)
  for st,v in vec.items():
   for p in powers:
    old=st//p%8
    for new,c in moves[old]:out[st+(new-old)*p]+=v*c
  return {x:a for x,a in out.items() if a}
 def interval(kind,ell,start):
  out={}
  for a in range(8):
   for b in range(8):
    if (bits[a]^bits[b]).bit_count()!=2:continue
    if bool(h[b,a])!=(kind=='edge'):continue
    st=sum((b if (j-start)%L<ell else a)*p for j,p in enumerate(powers))
    out[st]=F(int(h[b,a])**ell if kind=='edge' else 1)
  return out
 for kind,ell in [('edge',j) for j in range(1,7)]+[('diagonal',j) for j in [2,4,6]]:
  src=interval(kind,ell,0);w={st:a/F(8-energy(st)) for st,a in V(src).items() if energy(st)!=8};out={st:a for st,a in V(w).items() if energy(st)==8}
  for st,a in src.items():out[st]=out.get(st,F(0))+F(L,2)*a
  out={st:a for st,a in out.items() if a};kernels=[];reconstruct=defaultdict(F)
  for destkind in ['edge','diagonal']:
   for destell in range(1,8):
    if destkind=='diagonal' and destell%2:continue
    for start in range(L):
     dest=interval(destkind,destell,start);overlap=sum(a*out.get(st,0) for st,a in dest.items());norm=sum(a*a for a in dest.values())
     if overlap:
      coef=overlap/norm;kernels.append(dict(kind=destkind,ell=destell,start=start,unnormalized_coefficient=str(coef),source_norm=int(sum(a*a for a in src.values())),target_norm=int(norm)))
      for st,a in dest.items():reconstruct[st]+=coef*a
  assert {st:a for st,a in reconstruct.items() if a}==out,(L,kind,ell,'incomplete target')
  rows.append(dict(L=L,kind=kind,ell=ell,kernels=kernels));print(L,kind,ell,kernels,flush=True)
Path('/private/tmp/neutral_zone_local_second.json').write_text(json.dumps(rows,indent=2))
