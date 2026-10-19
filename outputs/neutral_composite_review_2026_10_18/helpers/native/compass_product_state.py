"""Exact symbolic uniform-product diagnostic on nonaliasing cubic tori."""
from pathlib import Path
import itertools,json,sympy as s
from compass_local_transport import word,product
P=Path(__file__).resolve().parent
n=s.symbols('nx ny nz', real=True)
def mean(w):
 return s.prod(n[v[3]] for v in w)
def run(L):
 sites=list(itertools.product(range(L),repeat=3)); bonds=[]
 for x in sites:
  for a in range(3):
   y=list(x);y[a]=(y[a]+1)%L;bonds.append(word([(x,a),(tuple(y),a)]))
 # Only intersecting pairs contribute to connected product-state variance.
 var=0
 for i,b in enumerate(bonds):
  bs={v[:3] for v in b}
  for c in bonds[i:]:
   if not bs.intersection(v[:3] for v in c):continue
   w,ph=product(b,c)
   # Symmetrized expectation for distinct terms cancels imaginary parts.
   val=int(ph.real)*mean(w)-mean(b)*mean(c)
   var+=(1 if b==c else 2)*val
 per=s.expand(var/L**3)
 target=3+2*sum(t*t for t in n)-3*sum(t**4 for t in n)-8*sum(n[a]**2*n[b]**2 for a in range(3) for b in range(a+1,3))
 assert s.expand(per-target)==0
 # On the pure-state sphere sum n^2=1 this equals 1+sum n^4.
 assert s.rem(s.Poly(per-1-sum(t**4 for t in n),n[2]),s.Poly(sum(t*t for t in n)-1,n[2])).as_expr()==0
 return dict(L=L,sites=L**3,variance_per_site_over_K_squared=str(per),pure_state_result='1 + nx**4 + ny**4 + nz**4')
if __name__=='__main__':
 rows=[run(L) for L in [3,4,5]]
 (P/'compass_product_state.json').write_text(json.dumps(dict(rows=rows,scope='Exact diagnostic of supplied uniform pure product states; no ground-state or phase inference'),indent=2)+'\n')
 print(rows)
