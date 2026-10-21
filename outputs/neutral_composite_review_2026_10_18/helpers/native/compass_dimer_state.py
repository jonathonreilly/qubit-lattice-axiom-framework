"""Exact rational dimer-product energy and residual; not ground-state inference."""
import itertools,json
from pathlib import Path
from fractions import Fraction as F
from compass_local_transport import word,product
P=Path(__file__).resolve().parent
# m=sqrt(15)/4; even number of Z-only factors in all relevant even words.
def mean(w):
 groups={}
 for v in w:
  x,y,z,a=v; key=(x//2,y,z);groups.setdefault(key,{})[x%2]=a
 zcount=0;value=F(1)
 for g in groups.values():
  if len(g)==1:
   if next(iter(g.values()))!=2:return F(0)
   zcount+=1
  else:
   a,b=g[0],g[1]
   if a!=b:return F(0)
   value*= [F(1,4),F(-1,4),F(1)][a]
 assert zcount%2==0
 return value*F(15,16)**(zcount//2)
def run(L):
 sites=list(itertools.product(range(L),repeat=3));bs=[];cs=[]
 for x in sites:
  for a in range(3):
   y=list(x);y[a]=(y[a]+1)%L;bs.append(word([(x,a),(tuple(y),a)]))
   z=list(x);z[a]=(z[a]-1)%L;cs.append(word([(tuple(z),a),(tuple(y),a)]))
 E=sum(map(mean,bs));variance=F(0)
 for i,b in enumerate(bs):
  for j in range(i,len(bs)):
   c=bs[j];w,ph=product(b,c)
   # H is taken with K=+1; variance independent of overall sign.
   variance+=(1 if i==j else 2)*(int(ph.real)*mean(w)-mean(b)*mean(c))
 N=L**3;assert E/N==F(17,16)
 assert sum(map(mean,cs))/N==F(15,16)
 return dict(L=L,sites=N,energy_per_site_over_K=str(E/N),variance_per_site_over_K_squared=str(variance/N),composite_per_site='15/16')
if __name__=='__main__':
 rows=[run(L) for L in [4,6,8]]
 (P/'compass_dimer_state.json').write_text(json.dumps(dict(rows=rows,scope='Exact correlated trial state at sin2theta=1/4; residual retained, not a ground state'),indent=2)+'\n');print(rows)
