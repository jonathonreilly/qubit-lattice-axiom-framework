#!/usr/bin/env python3
"""Independent exact small Fourier controls; no spectral author code imported."""
from fractions import Fraction as F
from pathlib import Path
import json,time,resource
T=time.monotonic()

def mul(a,b,J=None):
 out={}
 for k,x in a.items():
  for l,y in b.items():
   r=k+l
   if J is not None:r=(r+J)%(2*J+1)-J
   out[r]=out.get(r,0)+x*y
 return {k:v for k,v in out.items() if v}
def add(a,b,scale=1):
 out=dict(a)
 for k,v in b.items():out[k]=out.get(k,0)+scale*v
 return {k:v for k,v in out.items() if v}
def D(a):return {k:1j*k*v for k,v in a.items() if k}
def lie(xi,q,J):return add(mul(xi,D(q),J),mul(D(xi),q,J),2)
# Projection before differentiation misses full canonical normal directions.
cos={-1:F(1,2),1:F(1,2)}
grad=mul(cos,cos,5)
full=mul(grad,grad,5).get(0,0)
low={k:v for k,v in grad.items() if abs(k)<=1}
projected=mul(low,low,5).get(0,0)
assert full==F(3,8) and projected==F(1,4)
# Metric-weight-two Lie action with wraparound is checked from literal Fourier
# matrix actions; complex integer products are exactly representable here.
rows=[]
for J in [2,3,5,7]:
 xi={J:1};eta={1:1};q={0:1}
 comm=add(lie(xi,lie(eta,q,J),J),lie(eta,lie(xi,q,J),J),-1)
 B=add(mul(xi,D(eta),J),mul(eta,D(xi),J),-1)
 rhs=lie(B,q,J)
 defect=add(comm,rhs,-1)
 assert defect=={-J:2*(2*J+1)*(J-1)},(J,defect)
 # The same mode inputs with a larger, alias-free carrier recover the identity.
 big=4*J+1
 actual=add(lie(xi,lie(eta,q,big),big),lie(eta,lie(xi,q,big),big),-1)
 bracket=add(mul(xi,D(eta),big),mul(eta,D(xi),big),-1)
 assert actual==lie(bracket,q,big)
 rows.append({'J':J,'n':2*J+1,'metric_action_defect_at_mode_minus_J':int(defect[-J].real),'alias_free_control':True})
result={'full_grid_bracket':str(full),'premature_low_band_bracket':str(projected),'full_zone_metric_controls':rows,'elapsed_seconds':time.monotonic()-T,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Independent control only; not full ADM proof or universal no-go.'}
Path(__file__).with_name('fourier_controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
