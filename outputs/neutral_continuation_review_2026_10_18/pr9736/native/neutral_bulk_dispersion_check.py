import numpy as np,json
from scipy.integrate import quad_vec
from pathlib import Path
def greens(E,Qx=0,Qy=0):
 bx=4*np.cos(Qx/2);by=4*np.cos(Qy/2)
 def f(x):
  cx=np.cos(x);a=E+bx*cx;root=np.sqrt(a-by)*np.sqrt(a+by);g=1/root;y=(1-a*g)/by;yy=-a*y/by
  return np.array([g,cx*g-y,cx*g+y,cx*cx*g-2*cx*y+yy,cx*cx*g+2*cx*y+yy])
 return quad_vec(f,0,np.pi,epsabs=2e-10,epsrel=2e-10,points=[np.pi/2],limit=1500)[0]/np.pi
rows=[]
for eta in [1e-3,1e-4,1e-5]:
 E=-4+1j*eta;G00,Gd0,Gs0,G,Gs=greens(E);eps=1e-4;Gp=(greens(E+eps)[3]-greens(E-eps)[3])/(2*eps)
 Gq=(greens(E,.002)[3]-G)/.002**2;analytic=(G+E*Gp)/16;a=4*G/(2+4*G);aq=(G+E*Gp)/(2*(2+4*G)**2);Gsh=Gs-Gs0**2/G00
 # Finite-regulator controls, not a uniform eta->0 theorem. Tolerance1e-6
 # allows quadrature/finite-difference errors while rejecting sign/factor mistakes.
 discrepancy=abs(Gq-analytic)
 assert discrepancy<1e-6, ('Q derivative finite-regulator discrepancy',eta,discrepancy)
 assert abs(G00)>.05 and abs(Gd0)<1e-9, ('hard-core normalization',eta,G00,Gd0)
 assert min(abs(2+4*G),abs(2+4*Gsh))>.5 and abs(4*(G-Gsh))>.5, ('distinct nonzero channels',eta)
 assert G.imag<0 and Gp.real<0 and aq.real<0 and aq.imag>0, ('retarded sign and transverse curvature',eta)
 assert abs(aq-8*analytic/(2+4*G)**2)<1e-12, ('boundary derivative normalization',eta)
 if eta==1e-5:
  assert abs(aq-complex(-.08901367093,.01449119580))<3e-6, ('finite-regulator boundary coefficient',aq)
 print('finite-regulator dispersion PASS',eta,'discrepancy',discrepancy,'aQ',aq,flush=True)
 vals=dict(eta=eta,G=G,Gprime=Gp,GQ_numeric=Gq,GQ_formula=analytic,a=a,aQ=aq,Gd0=Gd0,Gs_hardcore=Gsh,channel_den_d=2+4*G,channel_den_s=2+4*Gsh)
 rows.append({k:([float(v.real),float(v.imag)] if isinstance(v,complex) or np.iscomplexobj(v) else v) for k,v in vals.items()})
Path('/private/tmp/neutral-bulk-dispersion-independent.json').write_text(json.dumps(rows,indent=2));print(rows[-1])
