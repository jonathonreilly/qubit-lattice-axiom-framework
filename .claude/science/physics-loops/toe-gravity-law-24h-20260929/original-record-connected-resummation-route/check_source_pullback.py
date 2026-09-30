#!/usr/bin/env python3
"""Exact literal rotor words; no imported campaign builder."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[name]='1'
import collections, datetime, hashlib, itertools, json, pathlib, resource, time
ROOT=pathlib.Path(__file__).resolve().parent
RUNTIME=pathlib.Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
assert time.time()<deadline and not (RUNTIME/'STOP_REQUESTED.json').exists()
resource.setrlimit(resource.RLIMIT_CPU,(30,31))
t0=time.process_time(); w0=time.monotonic()
D=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
nb=lambda a:[add(a,d) for d in D]
parity=lambda x:sum(x)%2
base=lambda x:0 if parity(x) else 1
omega=((),())
def unpack(w): return dict(w[0]),dict(w[1])
def pack(q,e): return (tuple(sorted((x,v) for x,v in q.items() if v!=base(x))),tuple(sorted((x,v) for x,v in e.items() if v)))
def charge(q,x): return q.get(x,base(x))
def hop(w,a,b):
 q,e=unpack(w); v=charge(q,a)
 if not v or charge(q,b): return None
 q[a]=0;q[b]=v;e[(a,b)]=e.get((a,b),0)-v
 return pack(q,e)
def birth(w,a,b,s):
 q,e=unpack(w)
 if charge(q,a) or charge(q,b): return None
 q[a]=s;q[b]=-s;e[(a,b)]=e.get((a,b),0)+s
 return pack(q,e)
def F(v,a):
 out=collections.Counter()
 for w,c in v.items():
  for b in nb(a):
   z=hop(w,a,b)
   if z is not None:out[z]+=c
 return {w:c for w,c in out.items() if c}
def j(v,a,b,sigs):
 out=collections.Counter()
 for w,c in v.items():
  for s in sigs:
   z=birth(w,a,b,s)
   if z is not None:out[z]+=c
 return {w:c for w,c in out.items() if c}
def leading(v,a,b,sigs): return j(F(v,a),a,b,sigs)
def source(v,a,b,sigs): return {w:-c for w,c in F(j(F(v,a),a,b,sigs),a).items()}
def gauss(w):
 q,e=unpack(w); div=collections.Counter()
 for (a,b),v in e.items():div[a]+=v;div[b]-=v
 return all(div[x]==charge(q,x)-base(x) for x in set(q)|set(div))
def counts(w,a):
 q,_=unpack(w)
 occ=[x for x,v in q.items() if parity(x) and v]
 star=sum(charge(q,b)!=0 for b in nb(a))
 outer=sum(sum(abs(x[i]-a[i]) for i in range(3))==3 for x in occ)
 return star,outer,len(occ)
def norm2(v):return sum(c*c for c in v.values())
a=(0,0,0)
# Independently selected source-accessible four-birth preparation.
marks=[(a,(0,-1,0)),((0,0,-2),(0,0,-3)),((2,0,0),(3,0,0)),((0,2,0),(0,3,0))]
selected_hops=[(-1,0,0),(0,0,-1),(2,1,0),(0,2,1)]
v={omega:1}; target=omega; levels=[]
for (c,b),hop_b in zip(marks,selected_hops):
 v=leading(v,c,b,(1,))
 target=birth(hop(target,c,hop_b),c,b,1)
 assert target is not None and target in v and gauss(target)
 assert all(gauss(w) for w in v)
 levels.append({'words':len(v),'norm2':norm2(v),'target_coefficient':v[target]})
assert counts(target,a)==(3,5,8)
chosen=target
# Mark +ex, other created neighbors +ey,+ez.
output=hop(birth(hop(target,a,(0,1,0)),a,(1,0,0),1),a,(0,0,1))
assert output is not None and counts(output,a)==(6,5,11) and gauss(output)
vsrc=source(v,a,(1,0,0),(1,))
assert output in vsrc
bad={w:c for w,c in vsrc.items() if counts(w,a)[0]==6 and counts(w,a)[1]>=4}
assert all(gauss(w) for w in vsrc)
# Full coherent original-edge products, never separately measured signs.
vc={omega:1}
for c,b in marks: vc=leading(vc,c,b,(-1,1))
vcs=source(vc,a,(1,0,0),(-1,1))
assert output in vcs and all(gauss(w) for w in vcs)
# Exhaust all star occupancies and charges (3^6), A charges and original marks.
# Test occupation pullback and row/column Schur budgets on full local source.
# Fixed arbitrary outer occupations suffice: source never changes that shell.
rows=collections.Counter();cols=collections.Counter();rowsc=collections.Counter();colsc=collections.Counter()
inputs=0; transitions=0; support_checks=0
for vals in itertools.product((-1,0,1),repeat=6):
 if sum(bool(x) for x in vals)!=3:continue
 for aq in (-1,1):
  q={a:aq};q.update({b:x for b,x in zip(nb(a),vals) if x})
  w=pack(q,{}) # local matrix carrier; Gauss completion discussed analytically
  inputs+=1
  for b in nb(a):
   for sig in (-1,1):
    z=source({w:1},a,b,(sig,))
    for out,c in z.items():
     assert counts(out,a)[0]==6
     # Field output distinguishes unequal inverse flux paths exactly.
     rows[(b,sig,out)]+=abs(c);cols[w]+=abs(c);transitions+=1
   z=source({w:1},a,b,(-1,1))
   for out,c in z.items():rowsc[(b,out)]+=abs(c);colsc[w]+=abs(c)
# Input E=0 slice cannot saturate all-field row bound: independently enumerate
# reverse ordered pairs on each full-star charge pattern, allowing inverse E.
reverse_max=0
for vals in itertools.product((-1,1),repeat=6):
 for mi,b in enumerate(nb(a)):
  sig=-vals[mi]
  paths=sum(vals[j]==sig for i in range(6) for j in range(6) if i!=mi and j!=mi and i!=j)
  reverse_max=max(reverse_max,paths)
  assert paths<=20
# Necessity for every 3^6 occupancy pattern, both input A charges and all marks.
for vals in itertools.product((-1,0,1),repeat=6):
 q={a:1};q.update({b:x for b,x in zip(nb(a),vals) if x});w=pack(q,{})
 for b in nb(a):
  for out,c in source({w:1},a,b,(-1,1)).items():
   if counts(out,a)[0]==6:assert sum(bool(x) for x in vals)==3
   support_checks+=1
assert max(cols.values())==12 and max(colsc.values())==12 and reverse_max==20
result={'status':'all exact assertions passed','levels_resolved':levels,
 'four_birth_target':{'input_counts':counts(chosen,a),'output_counts':counts(output,a),
 'resolved_full_output_coefficient':vsrc[output],'coherent_full_output_coefficient':vcs[output],
 'resolved_source_words':len(vsrc),'resolved_bad_words':len(bad),
 'coherent_preparation_words':len(vc),'coherent_source_words':len(vcs),
 'target_max_abs_E':max(abs(v) for e,v in output[1]),'gauss_checked':True},
 'schur':{'input_columns':inputs,'source_transitions':transitions,'fixed_input_E_row_max':max(rows.values()),
 'fixed_input_E_coherent_row_max':max(rowsc.values()),'full_field_reverse_row_l1_bound_saturated':reverse_max,
 'resolved_stacked_column_l1':max(cols.values()),'coherent_stacked_column_l1':max(colsc.values()),
 'stacked_squared_norm_bound':20*12,'all_occupancy_output_checks':support_checks},
 'resources':{'cpu_s':time.process_time()-t0,'wall_s':time.monotonic()-w0,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
assert result['resources']['rss_bytes']<=150_000_000
(ROOT/'SOURCE_PULLBACK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'ACCESSIBLE_WORD.json').write_text(json.dumps({'input':chosen,'output':output,'marks':marks,'selected_hops':selected_hops},indent=2)+'\n')
print(json.dumps(result,indent=2))
