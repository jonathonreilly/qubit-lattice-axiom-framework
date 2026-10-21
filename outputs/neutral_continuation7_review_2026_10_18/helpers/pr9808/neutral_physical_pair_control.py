"""Finite-volume pair normalization and physical YY-bond dressing controls."""
AUDIT_TIMEOUT_SEC=300
import math,json,itertools
from fractions import Fraction
rows=[]
for R in (6,8,12):
 L=10;sites=list(itertools.product(range(R),repeat=2));N=R*R
 counts=[]
 for dx,dy in ((1,0),(0,1)):
  selected={(0,0),(dx,dy)}
  counts.append(L*sum(((x,y) in selected)!=((x,(y+1)%R) in selected) for x,y in sites))
 for n in ((1,0),(1,2),(2,1)):
  k=[2*math.pi*v/R for v in n];den=math.sqrt(1-2/N)
  norm=0.;overlap=0.;corrected=0.;lam=.031
  for r,s in itertools.combinations(sites,2):
   c=2*math.cos(sum(k[j]*(r[j]-s[j]) for j in (0,1)))/(N*den)
   norm+=c*c
   d=((r[0]-s[0])%R,(r[1]-s[1])%R)
   axis=0 if d in ((1,0),(R-1,0)) else 1 if d in ((0,1),(0,R-1)) else None
   if axis is not None:
    overlap+=c/(math.sqrt(2)*R)
    corrected+=c*(1-counts[axis]*lam**2/32)/(math.sqrt(2)*R)
  expected=math.sqrt(2)/(R*den)*sum(map(math.cos,k))
  expected_corrected=math.sqrt(2)/(R*den)*sum((1-counts[a]*lam**2/32)*math.cos(k[a]) for a in (0,1))
  rows.append(dict(R=R,n=n,norm_error=abs(norm-1),overlap_error=abs(overlap-expected),dressed_error=abs(corrected-expected_corrected),reversed_bonds=counts,amplitude_coefficients=[str(-Fraction(v,32)) for v in counts]))
print(json.dumps(dict(rows=rows,max_error=max(max(r['norm_error'],r['overlap_error'],r['dressed_error']) for r in rows))))
