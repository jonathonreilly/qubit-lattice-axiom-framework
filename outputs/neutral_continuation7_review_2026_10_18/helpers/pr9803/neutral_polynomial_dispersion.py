AUDIT_TIMEOUT_SEC=300
import mpmath as m,json
from fractions import Fraction as F
m.mp.dps=400
p=m.mpf(3)/2;g=m.mpf(12155)/33554432;v=m.mpf(45)/16384;D=m.mpf(15)/512;k=4*g*g/v;eta=4*g*g/D
rows=[]
for st in ['1e-2','1e-4','1e-8']:
 l=m.mpf(st);R=2*m.ceil(l**(-p)/2)
 def energy(x,y):
  a=-k*l**12*m.cos(x)**2;b=-k*l**12*m.cos(y)**2;c=-eta*l**14*m.cos(x/2)*m.cos(y/2)
  return (a+b)/2-m.sqrt(((a-b)/2)**2+c*c)
 for nx,ny in [(1,0),(1,1),(2,1)]:
  x,y=2*m.pi*nx/R,2*m.pi*ny/R;shift=energy(x,y)-energy(0,0);leading=k*l**12*(x*x+y*y)/2
  rows.append(dict(lam=st,n=[nx,ny],q_over_lambda=float(m.sqrt(x*x+y*y)/l),dispersion_ratio=float(shift/leading),relative_error=float(abs(shift/leading-1))))
assert max(r['relative_error'] for r in rows[-3:])<1e-4
pf=F(3,2);M=40
powers=dict(leading=str(12+2*pf),orientation_correction=str(10+4*pf),global_tail=str(M-2*pf),source_error=str(M-14-3*pf))
assert M-2*pf>12+2*pf and M-14-3*pf>10 and pf>1 and pf<2
print(json.dumps(dict(kappa=float(k),eta=float(eta),rows=rows,powers=powers,scope='Leading native two-orientation coefficient control; analytic proof supplies microscopic transfer'),indent=2))
