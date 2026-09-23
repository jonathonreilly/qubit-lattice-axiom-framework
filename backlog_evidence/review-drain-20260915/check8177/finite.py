import resource,signal,importlib.util,pathlib,itertools
resource.setrlimit(resource.RLIMIT_CPU,(90,90));signal.alarm(100)
p=next(pathlib.Path('/private/tmp/review-drain-20260915/drain-author-slot/scripts').glob('*rooted_inequality_reduces*.py'))
spec=importlib.util.spec_from_file_location('candidate',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def independent(eta,root,c,restricted):
 V=sorted(z for z,v in eta.items() if v and sum(z)<=sum(root));kind={}
 for z in V:
  n=sum(eta.get(tuple(z[i]-(i==j) for i in range(3)),0) for j in range(3));kind[z]=0 if n==0 else 1 if n==1 else 2
 best=None
 for mask in range(1<<len(V)):
  N=[z for i,z in enumerate(V) if mask>>i&1]
  if root not in N:continue
  edges=[]
  for a,b in itertools.combinations(N,2):
   d=tuple(a[i]-b[i] for i in range(3))
   if sorted(d)==[0,0,1]:edges.append((a,b,'a'))
   elif sorted(d)==[-1,0,0]:edges.append((b,a,'a'))
   elif sorted(d)==[-1,0,1]:edges.append((a,b,'f'))
  for E in itertools.combinations(edges,len(N)-1):
   down={z:0 for z in N};pc={z:0 for z in N};adj={z:set() for z in N}
   for a,b,k in E:
    adj[a].add(b);adj[b].add(a)
    if k=='a':down[a]+=1;pc[b]+=kind[a]==2
   if any(down[z]!=(kind[z]>0) for z in N) or restricted and max(pc.values())>1:continue
   seen={root}
   while True:
    more=seen|set().union(*(adj[z] for z in seen))
    if more==seen:break
    seen=more
   if len(seen)!=len(N):continue
   cost=sum(1 if kind[z]==2 else -c if kind[z]==1 else -3 for z in N)+3
   best=cost if best is None else min(best,cost)
 return best
sites=list(itertools.product(range(2),repeat=3));tests=0
for mask in range(0,256,7):
 marks={z:1 for i,z in enumerate(sites) if mask>>i&1};eta=m.run_automaton(sites,marks)
 if sum(eta.values())>6:continue
 for root in sites:
  if not eta[root]:continue
  for c in (1,2):
   for restricted in (False,True):
    a=independent(eta,root,c,restricted);b=m.brute_rooted(eta,root,c,restricted)
    assert a==b,(mask,root,c,restricted,a,b);tests+=1
print('independent edge-subset rooted/full-restriction comparisons',tests,'PASS')
checks=m.Checks();m.family_b(checks);m.family_e(checks);assert checks.failed==0
m.ACTIVE_MUTATION='seed_lemma_wrong';bad=m.Checks();m.family_b(bad);assert bad.failed_families=={'B'}
print('targeted seed mutation detected PASS')
