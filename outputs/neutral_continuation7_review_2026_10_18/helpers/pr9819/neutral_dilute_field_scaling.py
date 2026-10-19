"""Derived two-orientation coefficient matrix, not full-spin numerics."""
AUDIT_TIMEOUT_SEC=300
import json
import mpmath as mp
mp.mp.dps=70
gamma=mp.mpf(12155)/33554432;v=mp.mpf(45)/16384;D=mp.mpf(15)/512
kappa=4*gamma**2/v;eta=4*gamma**2/D;g=mp.sqrt(mp.mpf(2)/10)*gamma*165/17
rows=[]
for ls in ['.01','.001','.0001']:
 l=mp.mpf(ls)
 for kx,ky in [(1,0),(1,1),(2,1)]:
  x=l*l*kx;y=l*l*ky
  a=-kappa*l**12*mp.cos(x)**2;b=-kappa*l**12*mp.cos(y)**2
  c=-eta*l**14*mp.cos(x/2)*mp.cos(y/2)
  e=(a+b)/2-mp.sqrt(((a-b)/2)**2+c*c)
  e0=-kappa*l**12-eta*l**14
  scaled=(e-e0)/l**16;target=kappa*(kx*kx+ky*ky)/2
  rows.append(dict(lambda_value=ls,k=[kx,ky],scaled_energy=float(scaled),limit=float(target),relative_error=float(scaled/target-1)))
assert max(abs(r['relative_error']) for r in rows if r['lambda_value']=='.0001')<1e-6
print(json.dumps(dict(status='conditional-support',kappa=float(kappa),source_g=float(g),source_weight=float(g*g),exponents=dict(contact=4+14-16,global_tail=80-28-16,projector_source=80-14-42,orientation=2,dispersion=2),rows=rows),indent=2))
