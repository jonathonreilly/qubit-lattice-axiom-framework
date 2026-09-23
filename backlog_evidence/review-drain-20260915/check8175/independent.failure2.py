import ast,pathlib,json,itertools,resource,time
from fractions import Fraction as Q
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
t=time.monotonic();src=next(pathlib.Path('/private/tmp/review-drain-20260915/drain8175-original/head/scripts').glob('*.py')); tree=ast.parse(src.read_text());ws={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['W1','W2','W3']}
def pred(v,j):return tuple(x-(i==j) for i,x in enumerate(v))
for name in ['W1','W2']:
 root,shape,marks=ws[name]; marks=set(marks);alive=set()
 for v in itertools.product(*(range(n) for n in shape)):
  if v in marks or sum(pred(v,j) in alive for j in range(3))>=2:alive.add(v)
 # Lex ordering is topological. Independently verify all live sites have same ancestor seed;
 # then their level slices are a single component of the lower-level arrow graph.
 ancestors={}
 for v in sorted(alive):
  ps=[pred(v,j) for j in range(3) if pred(v,j) in alive]
  ancestors[v]=set.union(*(ancestors[p] for p in ps)) if ps else {v}
 poles=[root]*3;edges=[];kept_before=set();log=[]
 while any(any(pred(v,j) in alive for j in range(3)) for v in poles):
  assert all(ancestors[v]=={(0,0,0)} for v in poles)
  dirs=[[j for j in range(3) if pred(v,j) in alive] for v in poles]
  assert all(dirs)
  excuses=[pred(v,ds[0] if len(ds)==1 else next(j for j in ds[:2] if j!=k)) for k,(v,ds) in enumerate(zip(poles,dirs))]
  keep={}
  for k,(v,ds) in enumerate(zip(poles,dirs)):
   if v in kept_before or len(ds)==1 and ds[0]==k:keep.setdefault(v,k)
  if not keep:keep[poles[0]]=0
  a=e=0
  for v,k in keep.items():
   ds=dirs[k];kind='A' if len(ds)==1 else 'E';a+=kind=='A';e+=kind=='E';edges.append((v,excuses[k],kind));kept_before.update([v,excuses[k]])
  bad=sum(len(ds)==1 and ds[0]==k for k,ds in enumerate(dirs));log.append((bad,a,e));poles=excuses
 vertices={v for edge in edges for v in edge[:2]};assert len(edges)==len(vertices)-1
 amps={v for v in vertices if sum(pred(v,j) in alive for j in range(3))==1};seeds={v for v in vertices if not any(pred(v,j) in alive for j in range(3))};E=sum(x[2]=='E' for x in edges)
 pairs=sum(a==(0,0,3) and b==(2,2,1) for a,b in zip(log,log[1:]));ratio=Q(E-3*(len(seeds)-1),len(amps))
 assert ratio=={'W1':Q(8,5),'W2':Q(5,3)}[name]
 print(json.dumps({'witness':name,'E':E,'A':len(amps),'S':len(seeds),'periods':pairs,'ratio':str(ratio),'log':log,'edges':edges,'marks_equal_seed_amp':marks==seeds|amps}))
# Independent elementary accounting and completed square maximum.
rows=[(b,a,e,Q(e-3*(1-b),a)) for b in range(4) for a in range(max(1,b),4) for e in range(4-a)]
assert max(r[3] for r in rows)==2
assert Q(4,729)==Q(2,27)**2
print('fork-free accounting maximum 2; completed square t*(4/27-t)=4/729-(t-2/27)^2')
u=resource.getrusage(resource.RUSAGE_SELF);print(json.dumps({'wall_seconds':time.monotonic()-t,'user_cpu':u.ru_utime,'system_cpu':u.ru_stime,'max_rss_bytes':u.ru_maxrss}))
