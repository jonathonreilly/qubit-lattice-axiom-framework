import numpy as np, math,json,hashlib
from pathlib import Path
rng=np.random.default_rng(8161)
sig=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]])
maxerr=0.;maxward=0.
for _ in range(100):
 p,k=rng.uniform(-math.pi,math.pi,(2,3));n=[];es=[];us=[]
 for q in [p,p+k]:
  d=np.array([math.sin(q[0]),math.sin(q[1]),2.5-np.cos(q).sum()]);e=np.linalg.norm(d);n.append(d/e);es.append(e);us.append(np.linalg.eigh(np.einsum('i,ijk->jk',d,sig))[1])
 b=np.array([[-math.cos(p[0]+k[0]/2),0,-math.sin(p[0]+k[0]/2)],[0,-math.cos(p[1]+k[1]/2),-math.sin(p[1]+k[1]/2)],[0,0,-math.sin(p[2]+k[2]/2)]])
 s=2*np.sin(k/2);P=np.eye(3)-np.outer(s,s)/(s@s)
 M=np.array([us[1][:,1].conj()@np.einsum('i,ijk->jk',v,sig)@us[0][:,0] for v in b])
 actual=(M.conj()@P@M).real
 formula=sum(P[i,j]*((1+n[0]@n[1])*(b[i]@b[j])-(n[0]@b[i])*(n[1]@b[j])-(n[0]@b[j])*(n[1]@b[i]))/2 for i in range(3) for j in range(3))
 maxerr=max(maxerr,abs(actual-formula));maxward=max(maxward,np.linalg.norm(s@b-(es[0]*n[0]-es[1]*n[1])))
assert maxerr<1e-13 and maxward<1e-13
# Independent rank-one affine lattice: differentiate direct Z by analytic sums, then reconstruct moments and shifted overlap.
errors=[]
for a,g in [(.31,.8),(.47,1.8),(-.63,1.2)]:
 x=np.arange(-30,31)+a;w=np.exp(-g*g*x*x);Z=w.sum();mu=w@x/Z;second=w@(x*x)/Z
 grad=-2*g*g*mu;hess=-2*g*g+4*g**4*(second-mu*mu)
 errors += [abs(mu+grad/(2*g*g)),abs(second-(1/(2*g*g)+hess/(4*g**4)+grad**2/(4*g**4)))]
 t=.7;direct=np.exp(-g*g*(x*x+(x+t)**2)/2).sum()/math.sqrt(Z*np.exp(-g*g*(x+t)**2).sum())
 mid=np.exp(-g*g*(x+t/2)**2).sum();pred=math.exp(-g*g*t*t/4)*mid/math.sqrt(Z*np.exp(-g*g*(x+t)**2).sum())
 errors.append(abs(pred-direct))
assert max(errors)<1e-13
pref=40*15552*10648*6*2*math.factorial(8)
t=math.pi**2/(2*math.sqrt(12)*.1**2);eps0=4e15*math.exp(-t)
assert pref<4e15 and 2*t*eps0<.5
# Exact angular moments: integral(1-nx²)=8pi/3 and r*J=r+r³/8+... yield advertised coefficients.
assert math.isclose((8*math.pi/3)/(2*math.pi)**3/2,1/(6*math.pi**2))
assert math.isclose((8*math.pi/3)/(2*math.pi)**3/32,1/(96*math.pi**2))
out={'pauli_eigenspinor_100_samples_max_error':maxerr,'ward_max_error':maxward,'rank_one_affine_moment_overlap_max_error':max(errors),'cluster_prefactor':pref,'small_g_t':t,'convexity_product':2*t*eps0,'scope':'Independent bounded checks; no primary runner executed; no numerical substitute for uniform proof.'}
out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();print(json.dumps(out,indent=2))
