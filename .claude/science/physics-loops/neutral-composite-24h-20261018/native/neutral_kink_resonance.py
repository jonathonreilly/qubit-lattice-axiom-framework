from pathlib import Path
"""Second-sheet pole of the explicitly truncated derived relative model."""
import mpmath as m,json
m.mp.dps=45
I=m.eye(3)
def freeG(z,continued=False):
 root=m.sqrt(z-4)*m.sqrt(z+4)
 if continued and m.im(z)<0:root=-root
 g=(z-root)/8
 return m.matrix([[g,(z*g-1)/2,((z*z-4)*g-z)/4],[(z*g-1)/2,(z*z*g-z)/4,(z*(z*z-4)*g-z*z)/8],[((z*z-4)*g-z)/4,(z*(z*z-4)*g-z*z)/8,((z*z-4)**2*g-z**3+4*z)/16]])
def calc(lam):
 a=lam*lam/128;b=-lam/16;c=1-13*lam*lam/32
 def host(z):
  near=m.findroot(lambda r:a*r**3+b*r*r+c*r-z,z)
  # Divide cubic by the nearby root to find the remote two roots.
  bb=b+a*near;cc=c+bb*near;disc=m.sqrt(bb*bb-4*a*cc)
  roots=[near,(-bb+disc)/(2*a),(-bb-disc)/(2*a)];G=m.zeros(3)
  for j,r in enumerate(roots):G+=freeG(r,continued=(j==0))/(3*a*r*r+2*b*r+c)
  V=m.zeros(3);V[0,0]=lam/4;V[0,1]=V[1,0]=-11*lam*lam/32
  return (I-G*V)**-1*G
 v=m.matrix([-m.sqrt(2)*lam**2,-m.sqrt(2)*lam,lam**2/m.sqrt(2)])
 sig=lambda z:(v.T*host(z)*v)[0]
 pole=m.findroot(lambda z:z+2*lam-sig(z),-2*lam-1j*9*lam**4/64)
 den=1-m.diff(sig,pole);bare=m.matrix([2,0,0]);physical=m.matrix([2*lam,-lam**2,0])
 residue=lambda s:((s.T*host(pole)*v)[0])**2/den
 return dict(ratio=float(lam),pole_real=float(m.re(pole)),pole_imag=float(m.im(pole)),full_width_over_ratio4=float(-2*m.im(pole)/lam**4),bare_residue_over_ratio2=float(m.re(residue(bare))/lam**2),O_residue_over_ratio4=float(m.re(residue(physical))/lam**4))
rows=[calc(m.mpf(x)) for x in ['.2','.1','.05','.02','.01']]
print(rows);open(Path(__file__).resolve().parent/'neutral_kink_resonance.json','w').write(json.dumps(dict(rows=rows,scope='Pole of third-order derived halfline truncation. Coefficient extrapolation assumes bulk/locality of finite-derived matrices and controlled higher-order expansion; not full native model lifetime.'),indent=2))
