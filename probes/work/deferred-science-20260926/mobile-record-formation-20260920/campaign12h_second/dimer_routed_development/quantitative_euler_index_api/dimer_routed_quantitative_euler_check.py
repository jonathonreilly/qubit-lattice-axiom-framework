#!/usr/bin/env python3
"""Author exact path/coefficient controls for the quantitative Euler proof."""
from pathlib import Path
from collections import Counter
import datetime,hashlib,itertools,json,math
import numpy as np
import dimer_routed_transport_check as base

HERE=Path(__file__).resolve().parent

def path(a,b):
 current=list(a);out=[tuple(current)]
 for i in range(3):
  while current[i]!=b[i]:
   current[i]+=1 if b[i]>current[i] else -1
   out.append(tuple(current))
 assert out[-1]==tuple(b)
 return out

def edges_of(p):return [tuple(sorted((a,b))) for a,b in zip(p[:-1],p[1:])]

def open_cube_loads():
 rows=[]
 for L in (3,5,7):
  sites=list(itertools.product(range(L),repeat=3));loads=Counter()
  for a in sites:
   for b in sites:
    p=path(a,b);edges=edges_of(p)
    assert len(p)-1<=3*(L-1) and len(set(edges))==len(edges)
    loads.update(edges)
  assert len(loads)==3*(L-1)*L**2
  for (a,b),value in loads.items():
   axes=[i for i in range(3) if a[i]!=b[i]];assert len(axes)==1
   axis=axes[0];cut=max(a[axis],b[axis])
   assert value==2*cut*(L-cut)*L**2
   assert value<=L**4/2
  rows.append(dict(L=L,ordered_paths=L**6,physical_edges=len(loads),
                   maximum_exact_load=max(loads.values()),upper_bound_L4_over2=str(L**4/2)))
 return rows

def contracted_cube(N,l,kind,exhaustive):
 L=2*l+1;xyz,index,nb=base.make_lattice(N)
 M,flips=base.matching(N,8*N**3 if kind=='irregular' else 0,198300+N,
                       winding=kind=='winding')
 black=np.flatnonzero(xyz.sum(axis=1)%2==0)
 owner=np.empty(N**3,dtype=np.int64);owner[black]=black;owner[M[black]]=black
 # Center zero deliberately makes the physical fixture cross periodic seams;
 # paths themselves use the unique unwrapped ordinary cube coordinates.
 sites=list(itertools.product(range(-l,l+1),repeat=3))
 site_index={a:int(index[tuple(x%N for x in a)]) for a in sites}
 reps={}
 for a in sites:reps.setdefault(int(owner[site_index[a]]),a)
 keys=sorted(reps);m=len(keys);assert m*2>=L**3
 physical=Counter();edges=set()
 for a in sites:
  for i in range(3):
   if a[i]==l:continue
   b=list(a);b[i]+=1;b=tuple(b)
   u,v=int(owner[site_index[a]]),int(owner[site_index[b]])
   if u!=v:
    e=tuple(sorted((u,v)));physical[e]+=1;edges.add(e)
 assert max(physical.values())<=2
 adj={u:set() for u in keys}
 for u,v in edges:adj[u].add(v);adj[v].add(u)
 seen={keys[0]};stack=[keys[0]]
 while stack:
  for v in adj[stack.pop()]-seen:seen.add(v);stack.append(v)
 assert seen==set(keys)
 pairs=list(itertools.combinations(keys,2))
 if not exhaustive:
  rng=np.random.default_rng(202609212000+l)
  chosen=sorted(set([0,len(pairs)-1,*map(int,rng.integers(len(pairs),size=3000))]))
  pairs=[pairs[i] for i in chosen]
 loads=Counter();words=Counter();weighted=Counter();maxword=0
 for u,v in pairs:
  raw=[int(owner[site_index[a]]) for a in path(reps[u],reps[v])]
  route=[];position={}
  for k in raw:
   if k in position:
    stop=position[k]+1
    for old in route[stop:]:del position[old]
    del route[stop:]
   else:position[k]=len(route);route.append(k)
  assert route[0]==u and route[-1]==v
  path_edges=edges_of(route)
  assert set(path_edges)<=edges and len(path_edges)<=3*(L-1)
  word=path_edges+path_edges[-2::-1]
  assert len(word)<=6*L and max(Counter(word).values())<=2
  tokens={k:k for k in route}
  for a,b in word:tokens[a],tokens[b]=tokens[b],tokens[a]
  assert tokens[u]==v and tokens[v]==u and all(tokens[k]==k for k in route[1:-1])
  loads.update(path_edges);words.update(word)
  weighted.update({e:count*len(word) for e,count in Counter(word).items()})
  maxword=max(maxword,len(word))
 assert max(loads.values())<=L**4 and max(words.values())<=2*L**4
 assert max(weighted.values())<=12*L**5
 # Every pair is represented by one or two cube vertices. The outside-black
 # boundary correction is counted explicitly, without assuming C is a translate.
 inside_black={int(owner[site_index[a]]) for a in sites if sum(a)%2==0}
 assert inside_black<=set(keys)
 outside_black=set(keys)-inside_black
 assert len(outside_black)<=6*L**2
 return dict(N=N,l=l,L=L,kind=kind,pairs_in_footprint=m,inside_black=len(inside_black),
             outside_black=len(outside_black),fixture_flips=flips,
             all_endpoint_pairs_checked=exhaustive,checked_pairs=len(pairs),
             largest_physical_multiplicity=max(physical.values()),
             max_path_load=max(loads.values()),max_word_use=max(words.values()),
             max_weighted_word_use=max(weighted.values()),max_word_length=maxword,
             all_exact_endpoint_permutations=True,
             variance_factor_bound=48*L**2)

def linear_coefficients():
 rows=[]
 for N,l in [(16,2),(20,3),(32,6)]:
  xyz,index,nb=base.make_lattice(N);black=np.flatnonzero(xyz.sum(axis=1)%2==0);K=len(black)
  offsets=[d for d in itertools.product(range(-l,l+1),repeat=3) if sum(d)%2==0]
  counts=np.zeros(K,dtype=np.int64);black_index=np.full(N**3,-1,dtype=int);black_index[black]=np.arange(K)
  # Exact translated-cube membership and the Schur coefficient estimate.
  rng=np.random.default_rng(199500+N);b=rng.integers(-7,8,size=K);coeff=np.zeros(K,dtype=np.int64)
  for d in offsets:
   shifted=(xyz[black]+np.array(d))%N
   target=np.array([black_index[int(index[tuple(map(int,a))])] for a in shifted])
   assert len(set(map(int,target)))==K
   counts[target]+=1;coeff[target]+=b
  assert np.all(counts==len(offsets)) and abs(coeff).max()<=7*len(offsets)
  modes=[]
  for integer_mode in [(1,0,0),(1,1,0),(2,-1,1)]:
   Q=2*np.pi*np.array(integer_mode);phase=np.exp(-1j*np.array(offsets)@Q/N).mean()
   bound=math.sqrt(3)*float(np.linalg.norm(Q))*l/N
   assert abs(phase-1)<=bound+1e-14
   for d in [(2,0,0),(1,-1,0),(0,1,1)]:
    z=Q@np.array(d)/N
    remainder=N*(np.exp(-1j*z)-1)+1j*Q@np.array(d)
    assert abs(remainder)<=float(Q@np.array(d))**2/(2*N)+1e-13
   modes.append(dict(mode=integer_mode,multiplier=[float(phase.real),float(phase.imag)],
                     error=float(abs(phase-1)),uniform_bound=bound))
  rows.append(dict(N=N,l=l,black_sites=K,cube_black_cardinality=len(offsets),
                   exact_equal_memberships=True,coefficient_abs_bound=7,
                   maximum_normalized_coefficient=float(abs(coeff).max()/len(offsets)),modes=modes))
 return rows

def main():
 out=HERE/'dimer_routed_quantitative_euler_checks';out.mkdir(exist_ok=False)
 physical=open_cube_loads();print('open_cube_loads PASS',flush=True)
 contracted=[]
 for N,l in [(16,2),(20,3)]:
  for kind in ['winding','columnar','irregular']:
   contracted.append(contracted_cube(N,l,kind,True));print(json.dumps(contracted[-1]),flush=True)
 contracted.append(contracted_cube(32,6,'irregular',False));print(json.dumps(contracted[-1]),flush=True)
 coefficients=linear_coefficients();print('linear_coefficients PASS',flush=True)
 result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
  sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in (
   Path(__file__).name,'DIMER_ROUTED_QUANTITATIVE_EULER_BOUND.md','dimer_routed_transport_check.py')},
  open_cube_loads=physical,contracted_footprints=contracted,linear_coefficients=coefficients,
  scope='Exact finite path/permutation/coefficient inventories and explicitly floating phase bounds. Small cubes test the counting lemma; l=6 tests an actual current-containing footprint. No fitted exponent or proof by finite samples.')
 (out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
