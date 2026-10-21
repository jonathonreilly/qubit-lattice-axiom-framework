# Reuse only the earlier independently written binary Pauli representation, not root code.
from pathlib import Path
from collections import defaultdict
import json
src=(Path(__file__).parent/'independent_transport.py').read_text();src=src.replace('coords=list(product(range(-5,6),repeat=3))','coords=sorted([p for p in product(range(-8,9),repeat=3) if sum(map(abs,p))<=8],key=lambda p:(sum(map(abs,p)),p))');exec(src[:src.index('A={}')])
def axis(w,i):
 x,z=w;return 1 if ((x>>i)&1 and (z>>i)&1) else (0 if (x>>i)&1 else 2)
def native(w):
 if (w[0]|w[1]).bit_count()!=2:return False
 ss=sites(w)
 i,j=ss;a=axis(w,i)
 return axis(w,j)==a and abs(coords[i][a]-coords[j][a])==1 and all(coords[i][b]==coords[j][b] for b in range(3) if b!=a)
def thermal(A):
 out=defaultdict(int)
 for (x,z),c in A.items():
  if (x|z).bit_count() not in (2,4):continue
  bs=set()
  for i in sites((x,z)):bs.update(incident(i))
  for xx,zz in bs:
   ww=(x^xx,z^zz)
   if not native(ww):continue
   ph=((x&z).bit_count()+(xx&zz).bit_count()-(ww[0]&ww[1]).bit_count()+2*(z&xx).bit_count())%4
   if ph%2:continue
   sign=1 if ph==0 else -1
   for i in sites((xx,zz)):out[coords[i]]+=c*sign
 return {r:v for r,v in out.items() if v}
A={}
for a in range(3):
 p=[0,0,0];q=p.copy();p[a]=-1;q[a]=1;A[pauli((tuple(p),tuple(q)),a)]=1
root=(Path(__file__).parent/'compass_thermal_bridge.json')
expected=json.loads(root.read_text());rows=[]
for n in range(7):
 values=thermal(A);target={tuple(t['displacement']):t['value'] for t in expected['rows'][n]['twice_F']};assert values==target
 assert sum(values.values())==(12 if n==0 else 0)
 print('checked order',n,'words',len(A),'support',len(values),flush=True);rows.append({'n':n,'nonzero_displacements':len(values),'twice_F':{str(r):v for r,v in sorted(values.items())}})
 if n<6:A=D(A)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
print([{'n':r['n'],'nonzero_displacements':r['nonzero_displacements']}for r in rows])
