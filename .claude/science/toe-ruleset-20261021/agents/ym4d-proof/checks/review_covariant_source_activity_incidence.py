"""Post-run strengthening of the registered column/remote incidence control."""
import json,math,os,re,resource,subprocess,time
from collections import defaultdict
start=time.monotonic();resources=[]
def guard(where):
 p=subprocess.run(['/usr/bin/memory_pressure','-Q'],capture_output=True,text=True,timeout=5);m=re.search(r'System-wide memory free percentage:\s*(\d+)%',p.stdout);assert p.returncode==0 and m
 r={'where':where,'rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'free':int(m.group(1)),'load':list(os.getloadavg()),'nice':os.getpriority(os.PRIO_PROCESS,0),'elapsed':time.monotonic()-start,'threads':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']}};resources.append(r);assert r['rss']<2e9 and r['free']>=50 and max(r['load'])<20 and r['nice']>=10 and r['elapsed']<60 and set(r['threads'].values())=={'1'}
def norms(atoms,beta):
 rows=defaultdict(float);cols=defaultdict(float);inc=defaultdict(float)
 for i,j,S,c in atoms:
  w=math.exp(beta*len(S))*abs(c);rows[i]+=w;cols[j]+=w
  for v in S:inc[v]+=w
 return {'row':max(rows.values()),'column':max(cols.values()),'M':max(max(rows.values()),max(cols.values())),'B':max(inc.values()),'remote':inc.get(-1,0.)}
guard('start');n=m=256;beta=4.;A=[];B={}
for j in range(m):
 B[j]=(j,j,frozenset([j,-1]),1.)
 for r in range(n):
  i=m+j*n+r;A.append((i,j,frozenset([i,j]),1.))
C=[]
for i,j,S,c in A:
 k,l,T,d=B[j];assert j==k and S&T
 C.append((i,l,S|T,c*d))
na,nb,nc=norms(A,beta),norms(B.values(),beta),norms(C,beta)
correct=na['B']*nb['M']+na['M']*nb['B'];row_only=na['B']*nb['M']+na['row']*nb['B'];root_only=na['B']*nb['M']
assert nc['B']<=correct and nc['B']>row_only and nc['B']>root_only
assert na['remote']==0 and nb['remote']==nb['B'] and nc['remote']==nc['B']
assert abs(nc['B']/(n*m*math.exp(3*beta))-1)<1e-11
guard('completion');print(json.dumps({'scope':'Sparse matrices with B_jj=z_v, |z_v|<=1, support {j,v}; all actual product atoms enumerated. This strengthens the earlier closed-count control, not an extra theorem.','counts':{'A':len(A),'B':len(B),'AB':len(C)},'A_norms':na,'B_norms':nb,'product_norms':nc,'correct_bound':correct,'row_only_wrong_bound':row_only,'root_only_wrong_bound':root_only,'all_expected_controls_rejected':True,'resources':resources},indent=2))
