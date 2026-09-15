import json,gzip,hashlib,math,signal,time
from pathlib import Path
from fractions import Fraction as F
from itertools import product
signal.alarm(90);start=time.monotonic();r=Path(__file__).parent;raw=next((r/'8056/original/.claude').rglob('RAW_CANDIDATES'));m=json.loads((raw/'MANIFEST.json').read_text());seen=[];sums={}
for job in m['jobs']:
 p=raw/job['file'];b=p.read_bytes();assert len(b)==job['compressed_bytes'] and hashlib.sha256(b).hexdigest()==job['compressed_sha'];h=hashlib.sha256();size=0;n=0;lo=hi=F(0);rep=job['rep'];expected=list(product(range(4*job['block'],4*job['block']+4),range(16),range(16)))
 with gzip.open(p,'rb') as f:
  for line in f:
   h.update(line);size+=len(line);v=json.loads(line);assert v['job']==job['job'] and v['rep']==rep and tuple(v['index'])==expected[n];n+=1
   ev=[float.fromhex(x) for x in v['eigenvalues_hex']];q=v['vectors_hex'];assert len(ev)==16 and ev==sorted(ev) and all(math.isfinite(x) for x in ev);assert len(q)==16 and all(len(row)==16 and all(len(z)==2 and all(math.isfinite(float.fromhex(t)) for t in z) for z in row) for row in q)
   c=v['certificate'];assert c['dimension']==16 and len(c['root_intervals'])==16;assert F(c['eta'])<=F(1,2);assert all(0<=F(a)<=F(b) for a,b in c['root_intervals']);assert F(c['density_lower'])==-sum(F(b) for a,b in c['root_intervals'])/32 and F(c['density_upper'])==-sum(F(a) for a,b in c['root_intervals'])/32;lo+=F(c['density_lower']);hi+=F(c['density_upper'])
 assert n==1024 and size==job['decompressed_bytes'] and h.hexdigest()==job['decompressed_sha'];seen.append({'file':job['file'],'nodes':n,'compressed_sha':hashlib.sha256(b).hexdigest(),'raw_sha':h.hexdigest()});acc=sums.setdefault(rep,[F(0),F(0)]);acc[0]+=lo;acc[1]+=hi
accepted=json.loads((raw/'ACCEPTED_ANALYSIS.json').read_text());assert {str(k):[str(x/4096) for x in v] for k,v in sums.items()}==accepted['grid_density_intervals'];out={'scope':'Full 24-stream structural and exact saved-interval aggregation read; no replacement of upcoming complete residual/Gram replay','jobs':seen,'nodes':sum(v['nodes'] for v in seen),'seconds':time.monotonic()-start};(r/'stream-read.json').write_text(json.dumps(out,indent=2));print(out['nodes'],out['seconds'])
