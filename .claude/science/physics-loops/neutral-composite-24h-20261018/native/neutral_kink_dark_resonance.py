"""General-q second-sheet pole of derived relative Hamiltonian truncation."""
from pathlib import Path
import mpmath as m,json
m.mp.dps=40
I=m.eye(3)
def freeG(z,t,continued=False):
 root=m.sqrt(z-2*t)*m.sqrt(z+2*t)
 if continued and m.im(z)<0:root=-root
 g=(z-root)/(2*t*t)
 return m.matrix([[g,(z*g-1)/t,((z*z-t*t)*g-z)/t**2],[(z*g-1)/t,(z*z*g-z)/t**2,(z*(z*z-t*t)*g-z*z)/t**3],[((z*z-t*t)*g-z)/t**2,(z*(z*z-t*t)*g-z*z)/t**3,((z*z-t*t)**2*g-z**3+t*t*z)/t**4]])
def calc(lam,q):
 u=m.cos(q);c=m.cos(q/2);t=2*c
 alpha=-u/(4*t*t);beta=(u-1)/2;delta=m.mpf(3)/4-u/2
 gamma=(2*u-1)/(32*t*t);eta=-(7+6*u)/32;k=t*(-21+10*u)/64
 a=lam*lam*gamma;b=lam*alpha;cc=1+lam*lam*eta;d=lam*beta
 def host(z):
  near=m.findroot(lambda r:a*r**3+b*r*r+cc*r+d-z,z-d)
  if abs(a)<m.mpf('1e-30'):
   roots=[near,-cc/b-near]
  else:
   bb=b+a*near;ccc=cc+bb*near;disc=m.sqrt(bb*bb-4*a*ccc)
   roots=[near,(-bb+disc)/(2*a),(-bb-disc)/(2*a)]
  G=m.zeros(3)
  for j,r in enumerate(roots):G+=freeG(r,t,continued=(j==0))/(3*a*r*r+2*b*r+cc)
  V=m.zeros(3);V[0,0]=lam*delta;V[0,1]=V[1,0]=lam*lam*k
  return (I-G*V)**-1*G
 v=m.matrix([-m.sqrt(2)*c*lam**2,-m.sqrt(2)*lam,c*lam**2/m.sqrt(2)])
 sig=lambda z:(v.T*host(z)*v)[0]
 predicted=9*(1-2*u)**2/(32*c**3)
 diag4=-m.mpf(73)/192
 bulk=-m.mpf(13)/96;hop=-3*u/32;defect=(1-479*u)/(192*(1+u))
 if abs(defect)<=abs(hop):return dict(q=float(q),ratio=float(lam),bound=False)
 predicted_shift=bulk+defect+hop*hop/defect;Z=1-(hop/defect)**2
 def darksig(z):
  if abs(hop)<m.mpf('1e-30'):return m.mpf(0)
  x=z+2*lam-lam**3*bulk;T=lam**3*abs(hop)
  root=m.sqrt(x-2*T)*m.sqrt(x+2*T)
  return (x-root)/2
 total=lambda z:sig(z)+darksig(z)
 pole=m.findroot(lambda z:z+2*lam-diag4*lam**3-total(z),-2*lam+predicted_shift*lam**3-1j*max(predicted,m.mpf('.0001'))*lam**4/2)
 source=u*m.matrix([2*lam,-t*lam**2/2,0])
 residue=((source.T*host(pole)*v)[0])**2/(1-m.diff(total,pole))
 return dict(source_residue_coefficient=float(m.re(residue)/lam**4),predicted_source=float(2*Z*u*u/(c*c)),q=float(q),ratio=float(lam),shift_coefficient=float((m.re(pole)+2*lam)/lam**3),predicted_shift=float(predicted_shift),width_coefficient=float(-2*m.im(pole)/lam**4),predicted_width=float(predicted*Z))
rows=[]
for q in [0,m.pi/6,m.pi/3,m.pi/2,2*m.pi/3]:
 for lam in [m.mpf('.05'),m.mpf('.02'),m.mpf('.01')]:
  row=calc(lam,q);rows.append(row);print(row,flush=True)
Path(Path(__file__).with_suffix('.json')).write_text(json.dumps(dict(rows=rows,scope='Expanded dark-chain effective model, no full native lifetime theorem; q=pi excluded and q=pi/3 leading width cancellation not protected.'),indent=2))
