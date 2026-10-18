"""Exact projection/leakage calculation; even-dimer subspace is not invariant."""
import itertools,json
from fractions import Fraction as F
from pathlib import Path
from compass_local_transport import word,product
from compass_dimer_state import mean
P=Path(__file__).resolve().parent
def even(b):
 parity={}
 for x,y,z,a in b:
  if a!=2:
   d=(x//2,y,z);parity[d]=1-parity.get(d,0)
 return not any(parity.values())
def run(L):
 bs=[]
 for x in itertools.product(range(L),repeat=3):
  for a in range(3):
   y=list(x);y[a]=(y[a]+1)%L;bs.append(word([(x,a),(tuple(y),a)]))
 rows={}
 for name,terms in [('P',[b for b in bs if even(b)]),('Q',[b for b in bs if not even(b)])]:
  E=sum(map(mean,terms)); norm=F(0)
  for i,b in enumerate(terms):
   for j in range(i,len(terms)):
    w,ph=product(b,terms[j]);norm+=(1 if i==j else 2)*int(ph.real)*mean(w)
  rows[name]=dict(bonds=len(terms),mean_per_site=str(E/L**3),variance_per_site=str((norm-E*E)/L**3))
 if L>=6:
  assert F(rows['P']['variance_per_site'])==F(1,128)
  assert F(rows['Q']['variance_per_site'])==F(25,16)
 return dict(L=L,sectors=rows)
if __name__=='__main__':
 rows=[run(L) for L in [4,6,8]]
 (P/'compass_dimer_projection.json').write_text(json.dumps(dict(rows=rows,scope='Exact projected-subspace leakage on a supplied trial state; no invariant low energy sector'),indent=2)+'\n');print(rows)
