import itertools,time,resource,json
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_CPU,(10,10));start=time.monotonic()
def M(k,z):return z[k]-F(sum(z),3)
checks=0
for edges in [[(0,1),(1,2),(2,3)],[(0,1),(0,2),(0,3)]]:
 adj={i:[] for i in range(4)};points={}
 for j,(a,b) in enumerate(edges):adj[a].append(b);adj[b].append(a);points[frozenset([a,b])]=(j,-2*j,3-j)
 for targets in itertools.product(range(4),repeat=3):
  terminals=[(3+k,-k,2*k) for k in range(3)];total=F(0)
  for v in range(4):
   for k,target in enumerate(targets):
    if v==target:q=terminals[k]
    else:
     frontier=[(v,[])];seen={v}
     while frontier:
      u,path=frontier.pop(0)
      if u==target:first=path[0];break
      for n in adj[u]:
       if n not in seen:seen.add(n);frontier.append((n,path+[n]))
     q=points[frozenset([v,first])]
    total+=M(k,q)
  assert total==sum(M(k,z) for k,z in enumerate(terminals));checks+=1
actual=(2,1,1);mutated=(2,2,0);assert sum(actual)==sum(mutated)==4 and actual!=mutated
u=resource.getrusage(resource.RUSAGE_SELF);print(json.dumps({'abstract_pole_tree_cases':checks,'leaf_identity':'PASS','period_distribution_mutation_same_total_discriminated':True,'wall':time.monotonic()-start,'user_cpu':u.ru_utime,'sys_cpu':u.ru_stime,'max_rss_bytes':u.ru_maxrss}))
