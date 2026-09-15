"""Independent reviewer controls: no primary imports or primary execution."""
import json,time
from pathlib import Path
import numpy as np
import scipy.linalg as la
from numpy.polynomial.legendre import leggauss
start=time.monotonic(); checks=[]
def check(name, ok, **details):
 assert bool(ok),(name,details)
 checks.append(dict(name=name,**details))
rng=np.random.default_rng(80919294)
# Arbitrary indefinite finite one-body matrix; finite differences directly
# challenge the stated universal congruence convexity and Hessian weights.
x=rng.normal(size=(6,6))+1j*rng.normal(size=(6,6)); h=x+x.conj().T
w,u=la.eigh(h); h=u@np.diag([-3.,-1.7,-.4,.8,2.,4.])@u.conj().T
phi=np.diag(rng.normal(size=6)); vals,vec=la.eigh(h);o=vals<0
p=vec[:,o]@vec[:,o].conj().T
v=(phi@h+h@phi)/2
vo=vec[:,~o].conj().T@v@vec[:,o]
gap=vals[~o,None]-vals[None,o]
arith=-2*np.sum(abs(vo)**2/gap)
contact=-np.trace(p@(phi@phi@h-2*phi@h@phi+h@phi@phi)).real/4
po=vec[:,~o].conj().T@phi@vec[:,o]
cong=np.sum(-2*vals[~o,None]*vals[None,o]*abs(po)**2/gap)
check('arithmetic_plus_contact_equals_congruence',abs(arith+contact-cong)<1e-11)
check('opposite_free_curvature_signs',arith<0 and cong>0)
def energy(mat):return np.minimum(la.eigvalsh(mat),0).sum()
eps=2e-4; diag=np.diag(phi).real
es=[]
for t in [-eps,0,eps]:
 r=np.diag(np.sqrt(1+t*diag));es.append(energy(r@h@r))
check('direct_congruence_energy_curvature',abs((es[0]-2*es[1]+es[2])/eps**2-cong)<2e-6)
# Direct unitary frame conjugation fixes the scalar sign.
X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]);sig=[X,Y,Z]
t=.37;tp=.8;U=la.expm(1j*t*Z/2);dUH=-1j*tp*Z@U.conj().T/2
check('rotating_frame_connection_sign',np.max(abs(-1j*U@Z@dUH+tp*np.eye(2)/2))<1e-14)
# Ellipsoid response integrated using actual 2x2 eigenspaces, not the note's
# polynomial trace implementation, for non-axis transfer and generic strains.
Q=np.array([.2,-.3,.4]);om=1.4;L=(om**2-Q@Q)*np.eye(3)+np.outer(Q,Q);root=la.sqrtm(L)
A=np.array([[.3,.2,-.1],[.2,-.6,.4],[-.1,.4,.7]])
B=np.array([[.2,-.4,.3],[-.4,.1,.2],[.3,.2,-.5]])
z,weights=leggauss(12); integral=0.
for zz,ww in zip(z,weights):
 for angle in 2*np.pi*np.arange(24)/24:
  n=np.array([np.sqrt(1-zz**2)*np.cos(angle),np.sqrt(1-zz**2)*np.sin(angle),zz]);pp=root@n/2
  hm=sum(a*b for a,b in zip(pp-Q/2,sig));hp=sum(a*b for a,b in zip(pp+Q/2,sig))
  em,um=la.eigh(hm);ep,up=la.eigh(hp)
  va=sum(a*b for a,b in zip(A@pp,sig));vb=sum(a*b for a,b in zip(B@pp,sig))
  j=2*np.real(np.vdot(um[:,0],va@up[:,1])*np.vdot(up[:,1],vb@um[:,0]))
  integral+=ww/2/24*j*(-em[0])*ep[1]/(4*np.pi**2)
target=(np.trace(A@L@B@L)-np.trace(A@L)*np.trace(B@L)/3)/(160*np.pi**2)
check('spectral_shell_from_eigenvectors',abs(integral-target)<1e-14,residual=float(abs(integral-target)))
# Independent lapse projection of the spectral polynomial.
q2=Q@Q
pol=np.trace(L@L)-np.trace(L)**2/3
check('isotropic_shell_frequency_cancels',abs(pol-2*q2*q2/3)<1e-14)
check('Dirac_two_node_normalization',abs((2/np.pi**4)/320*np.pi**2*2-1/(80*np.pi**2))<1e-17)
print(json.dumps(dict(status='ok',checks=checks,count=len(checks),elapsed_seconds=time.monotonic()-start),indent=2))
