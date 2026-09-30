"""Small exact controls for the full rotor-process bridge.

No author/other packet program is imported. No torus Hilbert matrix is built.
The exact local word controls check actual F,j algebra; the one-rotor boundary
control is explicitly a generic graded fixture, not substituted for PR9345.
"""
from itertools import product,combinations
from collections import defaultdict
from pathlib import Path
from math import isqrt
import json

OUT=Path(__file__).resolve().parent

# Full six-neighbour root-star B words, retaining both input charge signs and
# every B occupancy word. Link orientations all point outward from the root.
actions=0
for qa in (-1,1):
 for bs in product((-1,0,1),repeat=6):
  for b in range(6):
   for sigma in (-1,1):
    for d in range(6):
     if d==b or bs[b] or bs[d]:continue
     final=list(bs);final[b]=-sigma;final[d]=qa
     shifts=[0]*6;shifts[b]=sigma;shifts[d]=-qa
     assert sum(v!=0 for v in final)==sum(v!=0 for v in bs)+2
     assert sigma+sum(final)==qa+sum(bs)
     assert sum(shifts)==sigma-qa
     assert all(-shifts[i]==final[i]-bs[i] for i in range(6))
     assert sum(abs(v) for v in shifts)==2
     actions+=1

def births(state):
 qa,bs,es=state
 for b in range(6):
  if bs[b]:continue
  for sigma in (-1,1):
   for d in range(6):
    if d==b or bs[d]:continue
    q=list(bs);q[b]=-sigma;q[d]=qa
    e=list(es);e[b]+=sigma;e[d]-=qa
    yield sigma,tuple(q),tuple(e)
states={(1,(0,)*6,(0,)*6)}
layers=[len(states)]
for j in range(1,5):
 states={new for old in states for new in births(old)}
 assert all(sum(v!=0 for v in st[1])==2*j for st in states)
 layers.append(len(states))
assert layers[3]>0 and layers[4]==0

# Literal F_a,F_c,F_c*,F_a* paths on two overlapping degree-three stars.
# Shared B vertices 0,1; each A has one extra B. These are legal cubic subwords.
adj=((0,1,2),(0,1,3));edges=tuple((a,b) for a in range(2) for b in adj[a])
def hop(state,a,reverse=False):
 aq,bq,ee=state
 if not reverse:
  if not aq[a]:return
  for b in adj[a]:
   if bq[b]:continue
   aa=list(aq);bb=list(bq);e=list(ee);charge=aa[a]
   aa[a]=0;bb[b]=charge;e[edges.index((a,b))]-=charge
   yield tuple(aa),tuple(bb),tuple(e)
 else:
  if aq[a]:return
  for b in adj[a]:
   if not bq[b]:continue
   aa=list(aq);bb=list(bq);e=list(ee);charge=bb[b]
   aa[a]=charge;bb[b]=0;e[edges.index((a,b))]+=charge
   yield tuple(aa),tuple(bb),tuple(e)
paths=0;relocations=0
for aq in product((-1,1),repeat=2):
 for bq in product((-1,0,1),repeat=4):
  start=(aq,bq,(0,)*len(edges));out=[start]
  for a,rev in ((0,False),(1,False),(1,True),(0,True)):
   out=[v for u in out for v in hop(u,a,rev)]
  for aa,bb,ee in out:
   assert all(aa) and sum(v!=0 for v in bb)==sum(v!=0 for v in bq)
   assert sum(aa)+sum(bb)==sum(aq)+sum(bq)
   assert sum(abs(v) for v in ee)<=4
   paths+=1;relocations+=tuple(v!=0 for v in bb)!=tuple(v!=0 for v in bq)
assert paths>0 and relocations>0

# Gaussian-integer vector implementation of a separate one-rotor graded model.
# D_k(E)=E^2 for k<2, and 0 for the last grade: later unconfined electric fields
# are deliberately retained. B=(grade raising)*(T_+ + T_-), A=T_+ + T_-.
Z=(0,0);I=(0,1)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
PHASE=((1,0),(0,1),(-1,0),(0,-1))
def clean(v):return {k:z for k,z in v.items() if z!=Z}
def combine(terms):
 out={}
 for c,v in terms:
  for k,z in v.items():out[k]=add(out.get(k,Z),mul(c,z))
 return clean(out)
def base(v,kind,R=None):
 out={}
 for (grade,e),amp in v.items():
  if kind=='B' and grade==2:continue
  if kind=='Bt' and grade==0:continue
  gr=grade+(1 if kind=='B' else -1 if kind=='Bt' else 0)
  for step in (-1,1):
   key=(gr,e+step)
   if R is None or abs(key[1])<=R:out[key]=add(out.get(key,Z),amp)
 return clean(out)
def gamma(v,R=None):return base(base(v,'B',R),'Bt',R)
def diagphase(v,tick):
 return {k:mul(PHASE[(tick*(k[1]**2 if k[0]<2 else 0))%4],z) for k,z in v.items()}
def act(v,kind,tick,R=None):
 v=diagphase(v,-tick)
 if kind=='B':w=base(v,'B',R)
 else:w=combine([((0,-2),base(v,'A',R)),((-1,0),gamma(v,R))])
 return diagphase(w,tick)
coefficient_cases=0
for R in (2,4,6,8,12):
 for n in range(3):
  for j in range(3):
   if 4*n+2*j>R:continue
   for jump_positions in combinations(range(n+j),j):
    word=['B' if k in jump_positions else 'G2' for k in range(n+j)]
    full=cut={(0,0):(1,0)}
    for k,kind in enumerate(word):
     full=act(full,kind,(2*k+1)%4)
     cut=act(cut,kind,(2*k+1)%4,R)
    assert full==cut,(R,word,full,cut)
    coefficient_cases+=1
# P Gamma P differs from Gamma_R at a real boundary even at grade zero.
edge={(0,4):(1,0)}
old={k:z for k,z in gamma(edge).items() if abs(k[1])<=4}
correct=gamma(edge,4)
boundary_flux=combine([((1,0),old),((-1,0),correct)])
assert boundary_flux=={(0,4):(1,0)}

# Integer certificate for a deliberately loose actual-torus resource row.
# Never evaluate 2^(millions): bit lengths certify the exponents directly.
N=24**3//2;M=N//2;b=1+2*M
v=2592*N;g=300*N;X=v+g//2;Y=g
k=16*(X+Y+N+1);r=k-1;R=2*M+4*r+8
assert k>=6*X
poly=(b+4*X)**2+16*X
qk2=(b+4*k)**2
sh_coeff=2*poly+v
sp_coeff=g*(316*poly+2*v)
eh_coeff=4*qk2+3*v
ep_coeff=4*g*(316*qk2+2*v)
base_exp=2*Y+2*X-k
upper_exponents={
 'marked_trace_error':3+Y-k,
 'energy_first_moment':sh_coeff.bit_length()+3+base_exp,
 'energy_second_moment':(sh_coeff*eh_coeff).bit_length()+2+base_exp,
 'source_current_first_moment':(2*sp_coeff+ep_coeff).bit_length()+1+base_exp,
 'source_current_second_moment':(sp_coeff*ep_coeff).bit_length()+2+base_exp}
assert all(power<-100 for power in upper_exponents.values())
system_qubits=3*N+6*N*(2*R+1).bit_length()
hbar=2*R*R+2*v;pbar=g*(316*(1+R)**2+2*v)
nu_den=1000*(1+hbar*hbar+pbar*pbar)
q=3;cmark=7*g*g+4*hbar*g
sqrtg=isqrt(g)+(isqrt(g)**2<g)
n0=max(8,2*g,(704*q*sqrtg*nu_den)**6,4*cmark*nu_den,64*q*nu_den)
n=3*((n0+2)//3)
def ceil_cuberoot(n):
 lo=0;hi=1<<((n.bit_length()+2)//3)
 while lo+1<hi:
  mid=(lo+hi)//2
  if mid**3>=n:hi=mid
  else:lo=mid
 return hi
w=ceil_cuberoot(n);buffer=16*n;LB=64*q*nu_den
assert w**3>=n and (w-1)**3<n
result={
 'root_star_legal_B_words_checked':actions,'root_star_reachable_word_layers':layers,
 'overlap_pair_return_paths_checked':paths,'B_relocations_preserving_total_count':relocations,
 'exact_Dyson_word_coefficient_cases':coefficient_cases,
 'wrong_boundary_loss_detected':True,'boundary_missing_flux_on_unit_vector':1,
 'actual_torus_example':{'L':24,'N':N,'maximum_births':M,'K_delta_kappa_T':[1,1,1,1],
  'v':v,'g':g,'a':X,'tail_start_k':k,'radial_field_cutoff':R,
  'error_upper_bounds_as_powers_of_2':upper_exponents,
  'all_five_rotor_bridge_errors_below_2_to_minus_100':True,
  'system_encoding_qubits_upper_bound':system_qubits,
  'h_R_positive_norm_upper':str(hbar),'source_current_norm_upper':str(pbar),
  'apparatus_error_target':'1/'+str(nu_den),'grid_observations':q,
  'collision_bins':str(n),'collision_bins_decimal_digits':len(str(n)),
  'clock_width':str(w),'clock_buffer':'16 * collision_bins',
  'clock_dimension_decimal_digits':len(str(n+w+2*buffer+1)),
  'battery_ladder_width':str(LB),'positive_gap_count_upper':'2^'+str(system_qubits)+' - 1',
  'apparatus_process_and_four_moment_errors_each_below':'1/1000',
  'resource_scope':'Sufficient symbolic construction only; no torus or apparatus matrices constructed.'},
 'scope':'Small exact word controls and integer sufficient-resource bounds; analytic proof carries continuous histories and unbounded domains.'}
(OUT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
print('TOTAL: PASS=6 FAIL=0 (original B words; later births; H4 reverse paths; coefficient agreement; boundary-loss mutation; integer resource certificate)')
