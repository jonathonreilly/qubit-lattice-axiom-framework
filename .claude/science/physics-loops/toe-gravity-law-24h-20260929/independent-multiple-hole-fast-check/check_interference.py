import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
import time,resource,signal,json,hashlib,collections
out=Path(__file__).resolve().parent
old=out/'check_words.py';ns={'__file__':str(old)}
exec(compile(old.read_text().split('fixtures=')[0],str(old),'exec'),ns)
signal.alarm(60);resource.setrlimit(resource.RLIMIT_CPU,(20,21));t=time.process_time();w=time.monotonic()
base,H,info,step,near,physical=[ns[k] for k in ('base','H','info','step','near','physical')]
# Dense only near selected alternative stars; different geometry from author ball.
holes={(0,0,0),(0,2,0)}
centers=holes|{(2,2,0),(2,2,2),(2,4,0),(0,0,2),(0,-2,0)}
B={b for a in centers for b in near(a)}
if len(B)%2:B.add((9,0,0))
st=base(holes,B);zz,bs,h,g,phi=info(st);assert g==0
b=(h[0]+1,h[1],h[2]);c=(h[0]+2,h[1],h[2]);target=step(step(st,h,b,'in'),c,b,'out')
rev=H(target);assert rev[st]==1;zt=info(target)[0];classes=collections.Counter();incs=[]
for s,v in rev.items():
 z,Bs,mx,G,p=info(s)
 if G or s==st:continue
 assert p-phi>=6
 if z==zt:classes['same_hole_set']+=1;assert p-phi>=10
 elif c in z:classes['selected_hole_retained']+=1;assert p-phi>=12
 else:classes['selected_hole_replaced']+=1
 incs.append(p-phi)
assert all(classes[k]>0 for k in ['same_hole_set','selected_hole_retained','selected_hole_replaced']),classes
r={'m':len(holes),'k':len(B),'reverse_words':len(rev),'Gauss_words':physical(rev),'dark_interference_classes':dict(classes),'minimum_height_increment':min(incs),'CPU_seconds':time.process_time()-t,'wall_seconds':time.monotonic()-w,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'purpose':'Additional distinct-star fixture activates reverse interference absent from first control; no author code imported.'}
(out/'INTERFERENCE_RESULTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r));assert r['rss_bytes']<120*1024**2
