"""Price <=30 CPU s,120 wall s,150MB; exact Gaussian integers, no dense N4.
Reuses the disclosed author literal-action builder; not an independent check.
"""
from pathlib import Path
import json,time,resource,hashlib
from itertools import product
from collections import defaultdict

ns={}
src=Path(__file__).with_name('check_matching.py').read_text()
exec(compile(src.split('# All abstract graphs')[0],'author_literal_action','exec'),ns)
e,nn,disp=[ns[k] for k in ('e','nn','disp')]
add,sub,mul,canonical,perfect,action12=[ns[k] for k in ('add','sub','mul','canonical','perfect','action12')]
t0,c0=time.monotonic(),time.process_time()

# Nine ORTHONORMAL physical bond types, before the five-channel Gram frame.
types=[];pairs=[]
for i in range(3):
 types.append(('Eedge',i));pairs.append(tuple(sorted([mul(-1,e[i]),e[i]])))
for i in range(3):
 for j in range(i+1,3):
  for eta in (-1,1):
   types.append(('Tedge',i,j,eta));pairs.append(tuple(sorted([(0,0,0),add(e[i],mul(eta,e[j]))])))
def identify(pair):
 a,b=pair;d=sub(b,a)
 for i in range(3):
  if d in (mul(2,e[i]),mul(-2,e[i])):
   return i,tuple((x+y)//2 for x,y in zip(a,b))
 ij=[i for i in range(3) if d[i]];assert len(ij)==2
 i,j=ij
 if d[i]<0:a,b=b,a;d=sub(b,a)
 return types.index(('Tedge',i,j,d[j])),a
for i,p in enumerate(pairs):assert identify(p)==(i,(0,0,0))
roots=(1,1j,-1,-1j)
symbol_checks=0
for q in product(range(4),repeat=3):
 ell=6-2*sum((1,0,-1,0)[x] for x in q)
 direct=[[0j]*9 for _ in range(9)]
 for col,pair in enumerate(pairs):
  for z,(a,b) in action12(pair).items():
   row,anchor=identify(z)
   phase=roots[(-sum(q[k]*anchor[k] for k in range(3)))%4]
   direct[row][col]+=(a+b)*phase
 expected=[[24*int(i==j)+0j for j in range(9)] for i in range(9)]
 for i in range(3):
  for j in range(3):expected[i][j]+=(ell-2)*(12*int(i==j)-4)
 for i in range(3):
  for j in range(i+1,3):
   indices=[types.index(('Tedge',i,j,eta)) for eta in (-1,1)]
   v=[-eta*(roots[(eta*q[j])%4]+roots[q[i]]) for eta in (-1,1)]
   for ii,a in enumerate(indices):
    for jj,b in enumerate(indices):expected[a][b]+=3*(ell-1)*v[ii]*v[jj].conjugate()
 assert direct==expected,(q,direct,expected)
 assert all(direct[i][j]==direct[j][i].conjugate() for i in range(9) for j in range(9))
 symbol_checks+=1

def connected(S):
 seen={S[0]}
 while True:
  new=seen|{y for y in S for x in seen if sub(y,x) in disp}
  if new==seen:return len(seen)==len(S)
  seen=new
shapes={((0,0,0),)}
for n in range(2,5):
 shapes={canonical(S+(add(x,d),)) for S in shapes for x in S for d in disp if add(x,d) not in S}
core=sorted(S for S in shapes if perfect(S))
core_set=set(core);assert len(core)==1487
qout=set();extout=set();entries=0;mu_b=0;tau_b=0
digest=hashlib.sha256();maxspan=0
for S in core:
 row=defaultdict(lambda:[0,0])
 for z,(a,b) in action12(S).items():
  sh=canonical(z);row[sh][0]+=a;row[sh][1]+=b
 for z,(a,b) in sorted(row.items()):
  if not(a or b):continue
  entries+=1;digest.update(repr((S,z,a,b)).encode())
  if not perfect(z):
   qout.add(z);mu_b+=int(a!=0);tau_b+=int(b!=0)
  elif connected(z):assert z in core_set
  else:
   extout.add(z)
   # The physical exterior is exactly two disconnected G pairs.
   deg=ns['degrees'](z);assert deg==[1,1,1,1]
  maxspan=max(maxspan,max(max(x[k] for x in z)-min(x[k] for x in z) for k in range(3)))

# All free two-edge collision/overlap indices lie within anchor distance4.
# Enumerate the small enclosing relative box, deduplicating exchange orbits
# only for a count; physical core states are not identified with these indices.
hole_ordered=0;valid_disconnected=0
for a,pa in enumerate(pairs):
 for b,pb in enumerate(pairs):
  for r in product(range(-4,5),repeat=3):
   moved=tuple(add(x,r) for x in pb)
   combined=set(pa)|set(moved)
   forbidden=len(combined)<4 or any(sub(y,x) in disp for x in pa for y in moved)
   if forbidden:hole_ordered+=1
   else:valid_disconnected+=1
assert hole_ordered+valid_disconnected==81*9**3

out={'exact_9x9_Bloch_symbols':symbol_checks,'momenta_coordinates':'0,pi/2,pi,3pi/2',
 'connected_perfect_matching_core_dimension_K0':len(core),
 'nonzero_core_action_coefficients':entries,'closed_Q_boundary_shapes':len(qout),
 'separated_pair_exterior_boundary_shapes':len(extout),
 'core_to_Q_mu_nonzero_coefficients':mu_b,'core_to_Q_tau_nonzero_coefficients':tau_b,
 'maximum_coordinate_span_after_one_core_action':maxspan,
 'ordered_free_collision_hole_indices_in_radius4':hole_ordered,
 'free_collision_hole_count_scope':'Ordered redundant channel coordinates, not an orthonormal symmetric-space dimension.',
 'core_action_coefficient_sha256':digest.hexdigest(),
 'wall_seconds':time.monotonic()-t0,'cpu_seconds':time.process_time()-c0,
 'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'scope':'Finite connected-core and exact symbol checks. Reuses own action builder; no full resolvent, T-matrix or torus diagonalization.'}
Path(__file__).with_name('channel_geometry_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
