import ast,pathlib,itertools,time,resource,json
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_CPU,(20,20));t0=time.monotonic()
p=next(pathlib.Path('/private/tmp/review-drain-20260915/drain8175-original/head/scripts').glob('*.py'));a=ast.parse(p.read_text());fn=next(n for n in a.body if isinstance(n,ast.FunctionDef) and n.name=='family_d');d=next(n.value for n in fn.body if isinstance(n,ast.Assign) and n.targets[0].id=='certs');certs=eval(compile(ast.Expression(d),'cert-data','eval'),{'Fraction':F})
menu=[(a,s) for a in range(3) for s in [-1,1]];target=(0,1)
for (p,q,r),(t,D,U,K) in certs.items():
 def weight(x,y):return p if x==y else q if x[0]==y[0] else r
 ds=[]
 for neighbours in [[target]*3,[target,target,(0,-1)],[target,target,(1,1)]]:
  weights=[__import__('math').prod(weight(x,y) for y in neighbours) for x in menu];ds.append(1-F(weights[menu.index(target)],sum(weights)))
 x=t+max(ds[1:])/t;y=ds[0]/t**3
 # Enumerate binary choices for each port independently to evaluate the tree recursion.
 def ports(terms):
  return sum(__import__('math').prod(v for v in pick) for pick in itertools.product(*[(1,z) for z in terms]))
 rhs=[ports([x*U]*2+[3*x*D]+[y*K]*6),ports([x*U]*3+[y*K]*6),ports([x*U]*3+[3*x*D]+[y*K]*5)]
 assert all(v>=z for v,z in zip([D,U,K],rhs));assert ds[0]*ports([x*U]*3+[3*x*D]+[y*K]*6)<F(1,100000)
 print('cert',p,q,r,'positive margins',[str(v-z) for v,z in zip([D,U,K],rhs)])
u=resource.getrusage(resource.RUSAGE_SELF);print(json.dumps({'wall':time.monotonic()-t0,'user_cpu':u.ru_utime,'sys_cpu':u.ru_stime,'max_rss_bytes':u.ru_maxrss}))
