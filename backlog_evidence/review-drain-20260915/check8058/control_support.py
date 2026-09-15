from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import json,math,time
st=time.monotonic();w=Path('/private/tmp/review-drain-20260915/unit8058');p=json.loads((w/'outputs/native_weak_electric_spectator_gap_2026_09_08_inputs/PREFIXES.json').read_text());vs=list(product(range(4),repeat=3));ix={v:i for i,v in enumerate(vs)};edges=[]
for v in vs:
 for a in range(3):
  z=list(v);z[a]=(z[a]+1)%4;edges.append(tuple(sorted((ix[v],ix[tuple(z)]))))
assert p['edge_order']==list(map(list,edges));u,v=0,16
inc=[{e for e,ab in enumerate(edges) if i in ab} for i in range(64)];boundary=inc[u]^inc[v];assert boundary==set(p['boundary_edges'])
def matchings(occ):
 if not occ:return {()}
 e=occ[0];out=set()
 for j,f in enumerate(occ[1:],1):
  if e!=f and set(edges[e])&set(edges[f]):
   rest=occ[1:j]+occ[j+1:]
   for m in matchings(rest):out.add(tuple(sorted((tuple(sorted((e,f))),)+m)))
 return out
families={}
for bridge in range(len(edges)):
 ms=matchings(sorted(boundary)+[bridge,bridge])
 if ms:families[bridge]=ms
assert set(families)=={0,3,9,12,36,96}
rows=[];totalproper=0
for row in p['rows']:
 bridge=row['bridge_edge'];ms=families[bridge];assert len(ms)==row['unordered_pair_sets'];keys=set()
 for m in ms:
  for mask in range(64):
   selected=[m[j] for j in range(6) if mask>>j&1];used=set();bc=0
   for pair in selected:
    for e in pair:
     if e==bridge:bc+=1
     else:assert e not in used;used.add(e)
   keys.add((len(selected),sum(1<<e for e in used),bc))
 expected={(x['k'],int(x['boundary_used_mask']),x['bridge_count']) for x in row['prefixes']};assert keys==expected
 singletons=0
 for k,used,bc in keys:
  if k in (0,6):continue
  toggle=used^((1<<bridge) if bc%2 else 0)
  assert toggle
  # Solve cut equation by propagation from one vertex; detect all returns.
  signs={0:0};todo=[0];consistent=True
  for a in todo:
   for e in inc[a]:
    b=edges[e][0]^edges[e][1]^a;z=signs[a]^((toggle>>e)&1)
    if b in signs:
     if signs[b]!=z:consistent=False
    else:signs[b]=z;todo.append(b)
  if consistent:
   s=sum(signs.values());assert min(s,64-s)==1;singletons+=1
 totalproper+=sum(0<k<6 for k,_,_ in keys)
 rows.append({'bridge':bridge,'unordered_pair_sets':len(ms),'all_keys':len(keys),'proper_singleton_returns':singletons})
assert totalproper==2292
# Wrong-sector Jensen separation and outward root bounds checked exactly.
ell=F(2449489742783178,10**15);upper=ell+F(1,10**15);assert ell*ell<6<upper*upper
assert F(128,8*144*12)/4==F(1,432)
# Two successive scalar Newton updates have the displayed trace decomposition.
for a in [F(0),F(1),F(6),F(36)]:
 c=F(5,2);n1=(c+a/c)/2;n2=(n1+a/n1)/2
 formula=(a+c*c)/(4*c)+c*(1-c*c/(a+c*c));assert n2==formula and n2*n2>=a
# Third-order analytical coefficients and singleton normalization.
def alpha(x):return 15*(6*x*x+18*x+14)/(F(8*24)*(x*x+2*x+F(1,3))*(x*x+2*x+F(2,3)))
assert alpha(F(0))==F(315,64) and alpha(F(-6))==F(2745,172864);assert 4*alpha(F(0))**2/24==F(33075,8192)
out={'scope':'Independent complete incident-multiset matching and prefix/cut reconstruction; no candidate vectors or author code imported. Rational analytical constants checked separately.','rows':rows,'proper_states':totalproper,'words':sum(len(x)*math.factorial(6) for x in families.values()),'seconds':time.monotonic()-st};Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
