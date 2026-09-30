"""Independent literal occupation action; no author code import."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from collections import defaultdict,Counter
import ast,hashlib,json,os,resource,signal,time
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
resource.setrlimit(resource.RLIMIT_CPU,(30,35));signal.alarm(60)
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
assert not (runtime/'STOP_REQUESTED.json').exists()
start=time.monotonic();cpu=time.process_time()
ROOT=Path(__file__).resolve().parent
unit=[(1,0,0),(0,1,0),(0,0,1)]
def add(a,b,L=None):
 v=tuple(x+y for x,y in zip(a,b));return v if L is None else tuple(x%L for x in v)
def scale(a,c):return tuple(c*x for x in a)
def canon(S):
 S=tuple(sorted(S));o=S[0];return tuple(sorted(tuple(x-y for x,y in zip(p,o)) for p in S))
G=[scale(e,s) for e in unit for s in (-2,2)]
G += [add(scale(unit[i],s),scale(unit[j],t)) for i,j in combinations(range(3),2) for s,t in product((-1,1),repeat=2)]
assert len(set(G))==18

def channels(x,L=None):
 axial=[frozenset((add(x,e,L),add(x,scale(e,-1),L))) for e in unit]
 planes=[]
 for i,j in combinations(range(3),2):
  planes.append([(frozenset((add(x,scale(unit[i],s),L),add(x,scale(unit[j],t),L))),F(s*t,2)) for s,t in product((-1,1),repeat=2)])
 return axial,planes

def action(S,L=None):
 S=frozenset(S);assert len(S)==4
 out=defaultdict(lambda:[F(0),F(0)])
 degrees=[sum(add(x,d,L) in S for d in G) for x in S]
 out[tuple(sorted(S))][0]=F(4+sum(m*(m-1)//2 for m in degrees))
 centers={add(x,scale(e,s),L) for x in S for e in unit for s in (-1,1)}
 shifts=[(0,0,0)]+[scale(e,s) for e in unit for s in (-1,1)]
 def put(pair,residual,cm,ct):
  if len(pair)!=2 or pair & residual:return
  key=tuple(sorted(pair|residual));out[key][0]+=cm;out[key][1]+=ct
 for x in centers:
  ax,pl=channels(x,L)
  for j,inside in enumerate(ax):
   if not inside<=S:continue
   residual=S-inside
   for shift in shifts:
    target_ax,_=channels(add(x,shift,L),L)
    for i,pair in enumerate(target_ax):
     coeff=F(int(i==j))-F(1,3)
     put(pair,residual,-2*coeff if shift==(0,0,0) else 0,(6 if shift==(0,0,0) else -1)*coeff)
  for plane,pairs in enumerate(pl):
   for inside,cin in pairs:
    if not inside<=S:continue
    residual=S-inside
    for shift in shifts:
     _,target_pl=channels(add(x,shift,L),L)
     for pair,cout in target_pl[plane]:
      coeff=cin*cout
      put(pair,residual,-coeff if shift==(0,0,0) else 0,(6 if shift==(0,0,0) else -1)*coeff)
 return {k:tuple(v) for k,v in out.items() if any(v)}

def edge_sign(a,b,L=None):
 d=tuple(x-y for x,y in zip(a,b))
 for i,weight in [(0,1),(1,-1)]:
  for sign in (-2,2):
   target=scale(unit[i],sign)
   if L is None and d==target:return weight
   if L is not None and all((x-y)%L==0 for x,y in zip(d,target)):return weight
 return 0

def incoming_w(S,L=None):
 a,b,c,d=sorted(S)
 return (edge_sign(a,b,L)*edge_sign(c,d,L)+edge_sign(a,c,L)*edge_sign(b,d,L)+edge_sign(a,d,L)*edge_sign(b,c,L))

def source_at(S,L=None):
 column=action(S,L)
 return tuple(sum(v[j]*incoming_w(T,L) for T,v in column.items()) for j in (0,1))

S=tuple(sorted(((0,0,0),(3,-1,1),(3,1,1),(6,0,0))))
col=action(S)
assert col[S]==(F(8,3),F(4))
assert source_at(S)==(F(0),F(1,3))
assert incoming_w(S)==0
same_orbit={U:c for U,c in col.items() if canon(U)==canon(S)}
assert same_orbit=={S:col[S]}
differences=[tuple(a-b for a,b in zip(x,y)) for x in S for y in S if x!=y]
assert len(set(differences))==12
for U,value in col.items():assert action(U).get(S,(F(0),F(0)))==value
controls=[]
for mu,tau in [(F(1),F(1)),(F(2),F(1)),(F(1,3),F(3,2))]:
 d=col[S][0]*mu+col[S][1]*tau;f=source_at(S)[0]*mu+source_at(S)[1]*tau
 g=-f/(2*d);bare=52*mu+120*tau
 # Literal physical pulse coefficient: w/2+g times the single occupation orbit.
 corrected=bare+g*f+g*g*d
 assert bare-corrected==tau*tau/(48*(2*mu+3*tau)) and corrected<bare
 controls.append({'mu':str(mu),'tau':str(tau),'diagonal':str(d),'source_w':str(f),'creation_coefficient':str(g),'corrected_u4':str(corrected),'gain':str(bare-corrected)})

# Finite torus orbit normalization is computed from actual translated sets.
def orbit_info(S,L):
 S=tuple(tuple(x%L for x in p) for p in S);assert len(set(S))==4
 orbit=Counter(tuple(sorted(add(p,t,L) for p in S)) for t in product(range(L),repeat=3))
 sizes=set(orbit.values());assert len(sizes)==1
 return {'L':L,'volume':L**3,'distinct_configurations':len(orbit),'stabilizer_order':next(iter(sizes)),'unnormalized_orbit_lift_norm_squared':sum(v*v for v in orbit.values())}
orbits=[orbit_info(S,L) for L in (7,8,13)]
for x in orbits:assert x['stabilizer_order']==1 and x['unnormalized_orbit_lift_norm_squared']==x['volume']
# A real distant-pair exception to assuming all torus N4 orbit sizes equal V.
Sext=((0,0,0),(2,0,0),(8,0,0),(10,0,0));exception=orbit_info(Sext,16)
assert exception['stabilizer_order']==2
assert incoming_w(Sext,16)==1 and source_at(Sext,16)==(0,0)
# Direct finite operator action agrees with periodized compact column at safe L.
L=31;SL=tuple(sorted(tuple(x%L for x in p) for p in S));finite=action(SL,L)
periodized={tuple(sorted(tuple(x%L for x in p) for p in U)):v for U,v in col.items()}
assert finite==periodized
# Compare independent coefficient array to the frozen author output only now.
author_path=ROOT.parent/'native-threshold-variational-route/word_results.json'
author=json.loads(author_path.read_text())
author_col={tuple(ast.literal_eval(k)):tuple(F(v) for v in vals) for k,vals in author['full_sparse_row'].items()}
assert col==author_col
out={'scope':'Independent literal occupation action; actual local/orbit controls, not an all-volume computation. No author code read/imported/executed. Expected word/source were known from contract before prefreeze; author output seen after prefreeze.',
 'column_entries':len(col),'diagonal_mu_tau':list(map(str,col[S])),'source_w_mu_tau':list(map(str,source_at(S))),
 'same_orbit_nonzero_entries':len(same_orbit),'distinct_oriented_differences':len(set(differences)),
 'hermiticity_columns':len(col),'parameter_controls':controls,'compact_word_torus_orbits':orbits,
 'distant_torus_stabilizer_exception':dict(exception,incoming_w=1,H_incoming_source=[0,0]),
 'finite_operator_comparison_L':L,'author_coefficient_array_equal':True,'author_results_sha256':hashlib.sha256(author_path.read_bytes()).hexdigest(),
 'full_column':{str(k):list(map(str,v)) for k,v in sorted(col.items())},
 'wall_seconds':time.monotonic()-start,'cpu_seconds':time.process_time()-cpu,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(ROOT/'literal_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='full_column'},indent=2))
