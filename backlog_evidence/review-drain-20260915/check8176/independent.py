from pathlib import Path
import ast,itertools
from fractions import Fraction as Q
p=next(Path('/private/tmp/review-drain-20260915/review-draft-slot/scripts').glob('*minimal_marked_tree*.py'))
t=ast.parse(p.read_text());data={}
for n in t.body:
 if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('Z_A','Z_B','W1'):
  data[n.targets[0].id]=ast.literal_eval(n.value)
def solve(w,num,den):
 root,dims,marks=w; live=set();marks=set(marks)
 for z in itertools.product(*(range(d) for d in dims)):
  a,b,c=z
  ps=[(a-1,b,c),(a,b-1,c),(a,b,c-1)]
  if z in marks or sum(v in live for v in ps)>=2:live.add(z)
 # Pairwise squared Euclidean distance: arrows d^2=1 and forks d^2=2 with same coordinate sum.
 adj={z:set() for z in live}
 for x,y in itertools.combinations(live,2):
  d=sum((a-b)**2 for a,b in zip(x,y))
  if d==1 or (d==2 and sum(x)==sum(y)):adj[x].add(y);adj[y].add(x)
 comp={root};todo=[root]
 while todo:
  for z in adj[todo.pop()]-comp:comp.add(z);todo.append(z)
 pred={z:[v for v in adj[z] if sum(v)==sum(z)-1] for z in comp}
 seeds=[z for z in comp if not pred[z]];assert len(seeds)==1
 levels=[[z for z in sorted(comp) if sum(z)==i] for i in range(sum(seeds[0]),max(map(sum,comp))+1)]
 # Bottom-up integer transfer: each chosen upper vertex needs some lower predecessor;
 # seed forced and root forced at its level. This enumerates all admissible node sets,
 # and level descent proves every arrow chain terminates at the unique seed.
 prev=levels[0]; states={1:0}
 for row in levels[1:]:
  masks=[sum(1<<prev.index(v) for v in pred[z]) for z in row]
  costs=[den if len(pred[z])>=2 else -num for z in row]
  new={}
  for s in range(1<<len(row)):
   if root in row and not s>>row.index(root)&1:continue
   possible=[v for lower,v in states.items() if all(not(s>>i&1) or masks[i]&lower for i in range(len(row)))]
   if possible:new[s]=min(possible)+sum(v for i,v in enumerate(costs) if s>>i&1)
  states=new;prev=row
 return Q(min(states.values()),den),len(live),len(comp),len(marks)
for name,pars in [('Z_A',[(0,1),(3,4),(99,100),(1,1),(101,100)]),('Z_B',[(99,100),(1,1)]),('W1',[(74,100),(3,4)])]:
 for a,b in pars:print(name,str(Q(a,b)),solve(data[name],a,b),flush=True)
# Explicit isolated seed: only tree {root}, E=A=F=0,S=1. Budget valid for all c;
# the paper's restricted ratio min over A>=1 has empty domain.
print('isolated seed: tree budget=0 for every c; restricted ratio minimum empty (undefined).')
for p in [367,368]:
 d=Q(2*p+11,p*p+2*p+11); print('floor',p,d,'minus4/729',d-Q(4,729))
print('completed square: t*(4/27-t)=4/729-(t-2/27)^2; for c>=1 and 0<t<1, t^c<=t')
