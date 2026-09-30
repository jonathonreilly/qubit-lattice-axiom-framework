import os
for x in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[x]='1'
from pathlib import Path
from collections import defaultdict
import resource,json,time,hashlib
out=Path(__file__).resolve().parent;rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not any((rt/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'));assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
src=out.parent/'independent-fast-propagation-check/check.py';ns={'__file__':str(src)};exec(compile(src.read_text().split('\nfull=Preparation(8)')[0],str(src),'exec'),ns)
resource.setrlimit(resource.RLIMIT_CPU,(5,5));t0=time.process_time()
Preparation,relative_ops,dirs,add=[ns[k] for k in ('Preparation','relative_ops','dirs','add')]
core=Preparation();core.birth_pair((2,0,0));core.move((0,0,0),(0,1,0),'out')
far=Preparation();far.birth_pair((2,0,0));far.move((0,0,0),(0,1,0),'out');far.birth_pair((10,0,0))
for x,y in zip([(14,0,0),(15,0,0),(15,1,0),(14,1,0)],[(15,0,0),(15,1,0),(14,1,0),(14,0,0)]):
 e=(x,y) if sum(x)%2==0 else (y,x);far.E[e]=far.E.get(e,0)+(23 if sum(x)%2==0 else -23)
centers=sorted({add(a,b) for a in dirs for b in dirs}-{(0,0,0)})
loop={}
for x,y in zip([(0,0,0),(1,0,0),(1,1,0),(0,1,0)],[(1,0,0),(1,1,0),(0,1,0),(0,0,0)]):
 e=(x,y) if sum(x)%2==0 else (y,x);loop[e]=core.E.get(e,0)+(3 if sum(x)%2==0 else -3)
key1=((),tuple(sorted((a,b,v) for (a,b),v in loop.items())))
# Raw norm2=2; exactly the coherent ancilla vector |word0,0>+i|word1,1>.
initial={(((),()),0):(1,0),(key1,1):(0,1)}
records=[];all_outputs=[]
for prep in [core,far]:
 move,G,gauss,walk,holes=relative_ops(prep)
 def fa(v,a,kind):
  o=defaultdict(int)
  for st,c in v.items():
   for step in dirs:
    res=move(st,a,add(a,step),kind)
    if res is not None:o[res[0]]+=c
  return {s:c for s,c in o.items() if c}
 def H(st):
  h,=holes(st);o=defaultdict(int)
  def accum(v,sg=1):
   for s,c in v.items():o[s]+=sg*c
  accum(fa(fa({st:1},h,'in'),h,'out'))
  for step in centers:
   a=add(h,step);accum(fa(fa({st:1},a,'out'),a,'in'),-1);accum(fa(fa({st:1},h,'in'),a,'out'));accum(fa(fa({st:1},a,'out'),h,'in'),-1)
  return {s:c for s,c in o.items() if c}
 def inc(o,key,v):
  old=o.get(key,(0,0));o[key]=(old[0]+v[0],old[1]+v[1])
 def A(v):
  o={}
  for (st,anc),(re,im) in v.items():
   for s,c in H(st).items():inc(o,(s,anc),(c*im,-c*re))
   g=G(st)//2;inc(o,(st,anc),(-g*re,-g*im))
  return {s:c for s,c in o.items() if c!=(0,0)}
 def marks(v,coh):
  o={}
  for (st,anc),c in v.items():
   h,=holes(st)
   for step in dirs:
    b=add(h,step)
    for sg in (-1,1):
     res=move(st,h,b,'birth',sg)
     if res is not None:inc(o,((h,b) if coh else (h,b,sg),res[0],anc),c)
  return {s:c for s,c in o.items() if c!=(0,0)}
 v=initial;outs=[]
 for deg in (0,1):
  assert all(gauss(st) for st,anc in v)
  jr=marks(v,False);jc=marks(v,True)
  assert all(gauss(st) for mark,st,anc in jr)
  gsum=sum(G(st)*(a*a+b*b) for (st,anc),(a,b) in v.items())
  assert sum(a*a+b*b for a,b in jr.values())==gsum==sum(a*a+b*b for a,b in jc.values())
  # Relative keys coincide only when all changed factors remain near the core.
  assert all(all(max(map(abs,x))<=5 for x,q in st[0]) and all(max(map(abs,x))<=5 for a,b,e in st[1] for x in (a,b)) for st,anc in v)
  outs.append((v,jr,jc));records.append({'background_B':3 if prep is core else 5,'degree':deg,'no_event_ancilla_words':len(v),'resolved_marked_words':len(jr),'coherent_marked_words':len(jc),'exact_jump_norm2_Gform':gsum})
  if deg==0:v=A(v)
 all_outputs.append(outs)
assert all_outputs[0]==all_outputs[1]
# Within a coherent original mark both sign outputs retain a nonzero cross term;
# resolved marks put these outputs in different classical labels.
coh=all_outputs[0][0][2]; mark=((0,0,0),(-1,0,0));chosen=[(st,anc,c) for (mk,st,anc),c in coh.items() if mk==mark and anc==0];assert len(chosen)==2 and chosen[0][0]!=chosen[1][0] and chosen[0][2]==chosen[1][2]==(1,0)
result={'controls':records,'all_near_and_far_noevent_and_original_marked_coefficients_equal':True,'original_coherent_cross_sign_offdiagonal_raw_coefficient':1,'new_author_code_imported':False,'own_reused_elementary_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'cpu_seconds':time.process_time()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2));assert result['cpu_seconds']<5 and result['peak_rss_bytes']<60*1024**2
(out/'PREFIX_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
