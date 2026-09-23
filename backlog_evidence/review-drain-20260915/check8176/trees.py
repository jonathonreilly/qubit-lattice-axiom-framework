import ast,itertools
from pathlib import Path
from fractions import Fraction as F
p=next(Path('/private/tmp/review-drain-20260915/review-draft-slot/scripts').glob('*minimal_marked_tree*.py')); vals={}
for n in ast.parse(p.read_text()).body:
 if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ['W2','W3','W2_TREE','W3_TREE']:
  vals[n.targets[0].id]=eval(compile(ast.Expression(n.value),'data','eval'),{'dict':dict})
for name in ['W2','W3']:
 root,dims,marks=vals[name];marks=set(marks);live=set()
 for a,b,c in itertools.product(*(range(d) for d in dims)):
  z=(a,b,c)
  if z in marks or sum(v in live for v in [(a-1,b,c),(a,b-1,c),(a,b,c-1)])>=2:live.add(z)
 tree=vals[name+'_TREE'];edges=tree['arrows']+tree['forks'];nodes=set(sum(([a,b] for a,b in edges),[]));assert root in nodes and nodes<=live
 pred=lambda z:[v for v in live if sum((a-b)**2 for a,b in zip(z,v))==1 and sum(v)==sum(z)-1]
 counts=[0,0,0]
 for z in nodes:
  k=len(pred(z));counts[2 if k==0 else 1 if k==1 else 0]+=1
  down=[b for a,b in tree['arrows'] if a==z];assert len(down)==(k>0) and all(v in pred(z) for v in down)
 for a,b in tree['forks']:assert sum(a)==sum(b) and sum((x-y)**2 for x,y in zip(a,b))==2
 reach={root}
 for _ in nodes:
  for a,b in edges:
   if a in reach or b in reach:reach.update([a,b])
 assert reach==nodes and len(edges)==len(nodes)-1
 E,A,S=counts;assert len(tree['forks'])==S-1
 print(name,counts,'forks',len(tree['forks']),'ratio',F(E-3*(S-1),A))
p=F(36799,100);print('real-p',p,'d3',(2*p+11)/(p*p+2*p+11),'passes scalar ceiling',(2*p+11)/(p*p+2*p+11)<F(4,729))
print('not a full recurrence certificate; only disproves inference of integer rounding as real-p exclusion')
