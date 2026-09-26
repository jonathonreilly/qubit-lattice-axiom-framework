#!/usr/bin/env python3
"""Blind finite/exact checks from the supplied 13-label Gauss-loop definition.

No primary campaign source is imported. All algebraic tests below are integer
or rational, including Fourier coefficients represented as Laurent monomials.
"""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
from fractions import Fraction
import hashlib,json,sys
import numpy as np
HERE=Path(__file__).resolve().parent
N=7;VOL=N**3
unit=np.eye(3,dtype=int)
labels=[(0,0,0,0,0,0)]
for species in range(2):
    for axis in range(3):
        for sign in (1,-1):
            q=[0]*6;q[3*species+axis]=sign;labels.append(tuple(q))
labels=np.array(labels,dtype=int)
lookup={tuple(q):a for a,q in enumerate(labels)}
rows=[]
def check(name,condition,detail=None):
    assert condition,(name,detail)
    rows.append(dict(name=name,detail=detail))
    print("VERIFIED",name,json.dumps(detail,sort_keys=True),flush=True)
def pos(q):return tuple(int(x)%N for x in q)
def field(records):
    value=np.zeros((N,N,N,6),dtype=int)
    for site,a in records.items():value[site]=labels[a]
    return value
def div2(value):
    answer=np.zeros((N,N,N,2),dtype=int)
    for species in range(2):
        for axis in range(3):
            coordinate=value[:,:,:,3*species+axis]
            answer[:,:,:,species]+=np.roll(coordinate,-1,axis=axis)-np.roll(coordinate,1,axis=axis)
    return answer
def loop(i,j,species=0,circulation=1,center=(0,0,0)):
    c=np.array(center)
    entries=[(c-unit[j],i,1),(c+unit[i],j,1),(c+unit[j],i,-1),(c-unit[i],j,-1)]
    out={}
    for site,axis,sign in entries:
        q=[0]*6;q[3*species+axis]=sign*circulation
        out[pos(site)]=lookup[tuple(q)]
    assert len(out)==4
    return out
def label_counts(records):return Counter(records.values())
loop_cases=translations=0
for i,j in combinations(range(3),2):
 for species in range(2):
  for circulation in (1,-1):
   records=loop(i,j,species,circulation)
   assert not np.any(div2(field(records)));loop_cases+=1
   for axis in range(3):
    for sign in (1,-1):
     shift=sign*unit[axis]
     moved={pos(np.array(site)+shift):a for site,a in records.items()}
     assert not (set(records)&set(moved)) and len(moved)==4
     assert label_counts(moved)==label_counts(records) and not np.any(div2(field(moved)))
     translations+=1
check("all_loop_species_planes_circulations_and_unit_translations",True,dict(loops=loop_cases,translations=translations))
impulses=0;norms=Counter()
for direction in range(3):
 x=(0,0,0);y=pos(unit[direction])
 for a,b in product(range(13),repeat=2):
  before=field({x:a,y:b});after=field({x:b,y:a})
  delta=div2(after)-div2(before)
  numerator=int(np.sum(delta*delta))
  difference=labels[b]-labels[a]
  expected=int(np.dot(difference,difference))
  assert numerator==4*expected
  if a!=b:assert expected>0
  norms[expected]+=1;impulses+=1
check("nearest_neighbor_centered_divergence_impulse_norm",True,dict(cases=impulses,squared_centered_norm_counts=dict(norms)))
records=loop(0,1)
single=dict(records)
x,y=pos(-unit[1]),pos(unit[1])
single[x],single[y]=single[y],single[x]
defect=int(np.sum(div2(field(single))**2))
both=dict(single);x,y=pos(unit[0]),pos(-unit[0])
both[x],both[y]=both[y],both[x]
check("reversal_is_jointly_Gauss_preserving_but_not_sequential",
 defect==16 and not np.any(div2(field(both))) and label_counts(both)==label_counts(records),
 dict(single_opposite_swap_centered_norm_squared=defect//4))
moved={pos(np.array(site)+unit[2]):a for site,a in records.items()}
reborn=loop(0,1,species=1)
history={**moved,**reborn}
check("departure_and_reformation_with_capacity",
 len(history)==8 and not(set(moved)&set(reborn)) and not np.any(div2(field(history))),
 dict(initial_loop_records=4,departed_vacancies=len(set(records)-set(moved)),final_records=len(history)))
# Step-two graph: simple cycles through a fixed vertex. A two-edge backtrack
# is not an oriented circulation, because the one edge cannot be used twice.
origin=(0,0,0)
def neighbors(site):
 q=np.array(site)
 return [pos(q+sign*2*unit[axis]) for axis in range(3) for sign in (1,-1)]
cycle_counts={}
cycles4=[]
for length in (3,4,5):
 found=[]
 def visit(path):
  if len(path)==length:
   if origin in neighbors(path[-1]):found.append(tuple(path))
   return
  for site in neighbors(path[-1]):
   if site not in path:visit(path+[site])
 visit([origin])
 cycle_counts[length]=len(found)
 if length==4:cycles4=found
check("step_two_graph_minimal_cycles",cycle_counts=={3:0,4:24,5:0},
 dict(rooted_directed_counts=cycle_counts,unrooted_oriented_four_cycles=VOL*len(cycles4)//4,expected=6*VOL))
# Exact low-order spatial/Fourier coefficients, normalized by volume.
# All centers contribute equally; the two orientations double each tensor.
laurent=[[Counter() for j in range(3)] for i in range(3)]
occupancy_per_site=0
for i,j in combinations(range(3),2):
 example=loop(i,j)
 for x,a in example.items():
  u=labels[a,:3]
  for y,b in example.items():
   w=labels[b,:3]
   exponent=pos(np.array(x)-np.array(y))
   for ii,jj in product(range(3),repeat=2):
    laurent[ii][jj][exponent]+=2*int(u[ii]*w[jj])
 occupancy_per_site+=2*len(example)
def clean(counter):return {k:v for k,v in counter.items() if v}
for i,j in product(range(3),repeat=2):
 expected=Counter()
 if i==j:
  for axis in range(3):
   if axis!=i:
    expected[origin]+=4
    expected[pos(2*unit[axis])]-=2;expected[pos(-2*unit[axis])]-=2
 else:
  expected[pos(unit[i]+unit[j])]+=2;expected[pos(-unit[i]-unit[j])]+=2
  expected[pos(unit[i]-unit[j])]-=2;expected[pos(-unit[i]+unit[j])]-=2
 assert clean(laurent[i][j])==clean(expected)
check("exact_Laurent_Fourier_tensor_and_density_coefficient",occupancy_per_site==24,
 dict(covariance="8 z_species^4 (|sin(k)|^2 I-sin(k)sin(k)^T)",density_coefficient=occupancy_per_site,partition_species_coefficient=6*VOL))
# A six-edge rectangle is allowed but has population 2 modulo 4.
rectangle={}
for site,axis,sign in [((1,0,0),0,1),((3,0,0),0,1),((4,1,0),1,1),
                       ((3,2,0),0,-1),((1,2,0),0,-1),((0,1,0),1,-1)]:
 q=[0]*6;q[axis]=sign;rectangle[pos(site)]=lookup[tuple(q)]
check("six_record_zero_flux_state_outside_empty_birth_count_sector",
 len(rectangle)==6 and not np.any(div2(field(rectangle))) and np.all(np.sum(field(rectangle),axis=(0,1,2))==0))
# Directly assemble all minimally long straight winding cycles and zero-mode moment.
moment=np.zeros((3,3),dtype=int);windings=0
for axis in range(3):
 transverse=[i for i in range(3) if i!=axis]
 for coordinates in product(range(N),repeat=2):
  for sign in (1,-1):
   winding={}
   for h in range(N):
    site=[0,0,0];site[axis]=h
    for ii,c in zip(transverse,coordinates):site[ii]=c
    q=[0]*6;q[axis]=sign;winding[tuple(site)]=lookup[tuple(q)]
   f=field(winding);assert not np.any(div2(f))
   total=np.sum(f[:,:,:,:3],axis=(0,1,2))
   assert len(winding)==N and abs(int(total[axis]))==N
   moment+=np.outer(total,total);windings+=1
check("zero_mode_first_winding_coefficient",
 np.array_equal(moment,2*N*VOL*np.eye(3,dtype=int)),
 dict(winding_configurations=windings,normalized_covariance_coefficient=(moment//VOL).tolist(),order=N))
# Restricted exact partition on four diamond sites: every one of 13^4
# local label assignments is checked through its integer divergence charges.
active=sorted(loop(0,1))
phase_sites=sorted({pos(np.array(r)+sign*unit[axis]) for r in active for axis in range(3) for sign in (1,-1)})
phase_index={r:i for i,r in enumerate(phase_sites)}
charges=np.zeros((4,13,2*len(phase_sites)),dtype=int)
for site_index,r in enumerate(active):
 for a,vec in enumerate(labels):
  for species in range(2):
   for axis in range(3):
    sgn=int(vec[3*species+axis])
    charges[site_index,a,species*len(phase_sites)+phase_index[pos(np.array(r)-unit[axis])]]+=sgn
    charges[site_index,a,species*len(phase_sites)+phase_index[pos(np.array(r)+unit[axis])]]-=sgn
partition=Counter();admissible=[]
for config in product(range(13),repeat=4):
 charge=sum((charges[i,a] for i,a in enumerate(config)),np.zeros(2*len(phase_sites),dtype=int))
 if not np.any(charge):
  direct={r:a for r,a in zip(active,config)}
  assert not np.any(div2(field(direct)))
  nA=sum(1<=a<=6 for a in config);nB=sum(a>=7 for a in config)
  partition[(nA,nB)]+=1;admissible.append(config)
check("restricted_phase_constant_term_and_hard_capacity",
 partition=={(0,0):1,(4,0):2,(0,4):2},
 dict(assignments=13**4,admissible=len(admissible),partition={str(k):v for k,v in partition.items()},missing_factorized_mixed_coefficient=4))
# Exact signed-phase counterexample: theta=pi at +e1,+e2,+e3, zero otherwise.
spins=np.ones((N,N,N),dtype=int)
for axis in range(3):spins[pos(unit[axis])]=-1
sums=np.zeros((N,N,N),dtype=int)
for axis in range(3):sums+=np.roll(spins,-1,axis=axis)*np.roll(spins,1,axis=axis)
hist=Counter(int(q) for q in sums.flat)
za=Fraction(1,4);zb=Fraction(1,100)
factors={q:Fraction(1)+2*za*q+6*zb for q in hist}
negative_count=sum(hist[q] for q,f in factors.items() if f<0)
check("compact_phase_integrand_can_be_negative",
 hist=={-3:1,-1:3,1:9,3:VOL-13} and negative_count==1,
 dict(zA=str(za),zB=str(zb),cosine_sum_multiplicity=dict(hist),
      local_factors={str(q):str(f) for q,f in factors.items()},integrand_sign=-1))
result=dict(scope="Blind construction checks; finite integers/rationals, no primary-source access.",
 N=N,checks=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 versions=dict(python=sys.version,numpy=np.__version__))
(HERE/'BLIND_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print("BLIND_CHECK_GROUPS",len(rows),flush=True)
