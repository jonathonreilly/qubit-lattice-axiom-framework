"""Deterministic geometry transport controls; no selected experimental density."""
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
checks=[]
def ck(name, cond, **data):
    checks.append(dict(name=name,passed=bool(cond),**data))
def exact(name, expr):
    value=sp.simplify(expr)
    ck(name,value==0,residual=str(value))
r,m=sp.symbols("r m",positive=True)
h=(1+m*r)*sp.exp(-m*r)/r**3
exact("radial derivative",sp.diff(h,r)+sp.exp(-m*r)*((m*r)**2+3*m*r+3)/r**4)
exact("gradient coefficient",h-r*sp.diff(h,r)-sp.exp(-m*r)*(m*r+2)**2/r**3)
exact("force radial decrease",sp.diff(r*h,r)+sp.exp(-m*r)*((m*r)**2+2*m*r+2)/r**3)
x,y=sp.Matrix(sp.symbols("x0:3",real=True)),sp.Matrix(sp.symbols("y0:3",real=True))
J=sp.Matrix([[0,-1,0],[1,0,0],[0,0,0]])
numerator=(y.T*J*x)[0]
exact("x numerator gradient",sum((sp.diff(numerator,x[i])+(J*y)[i])**2 for i in range(3)))
exact("y numerator gradient",sum((sp.diff(numerator,y[i])-(J*x)[i])**2 for i in range(3)))

def constants(mu,d,L):
    return (np.exp(-mu*d)*((1+mu*d)/d**2+L*(mu*d+2)**2/d**3),
            L*np.exp(-mu*d)*(mu*d+2)**2/d**3)
def kernel(a,b,mu):
    delta=a[:,None,:]-b[None,:,:]
    radius=np.linalg.norm(delta,axis=-1)
    jx=np.column_stack((-a[:,1],a[:,0],np.zeros(len(a))))
    num=np.sum(b[None,:,:]*jx[:,None,:],axis=-1)
    return num*(1+mu*radius)*np.exp(-mu*radius)/radius**3
def rotation(a,theta):
    z=a.copy()
    z[:,0]=a[:,0]*np.cos(theta)-a[:,1]*np.sin(theta)
    z[:,1]=a[:,0]*np.sin(theta)+a[:,1]*np.cos(theta)
    return z

# Deterministic mass-element correspondences with a positive vertical gap.
A=np.array([[.1,.2,-.1],[-.15,.05,0.],[.3,-.07,-.15]])
B=np.array([[.25,.1,1.2],[-.2,.25,1.4],[.05,-.1,1.1],[.4,.3,1.5]])
da=np.array([[.01,-.015,.025],[-.02,.01,.01],[.015,.01,-.005]])
db=np.array([[-.015,.02,-.03],[.01,-.005,.015],[.005,.01,-.01],[-.01,-.01,.02]])
wa=np.array([.3,.9,.2]); wb=np.array([.7,.1,.5,.3])
epsa=max(np.linalg.norm(da,axis=1));epsb=max(np.linalg.norm(db,axis=1))
d0=min(B[:,2])-max(A[:,2])
d=d0-epsa-epsb
L=max(np.linalg.norm(A[:,:2],axis=1).max(),np.linalg.norm((A+da)[:,:2],axis=1).max())
D_A=float(wa@np.linalg.norm(da,axis=1)); D_B=float(wb@np.linalg.norm(db,axis=1))
details=[]
for mu in (0.,.4,2.,7.):
    cx,cy=constants(mu,d,L)
    envelope=float(sum(wb)*cx*D_A+sum(wa)*cy*D_B)
    differences=[]
    for theta in np.linspace(0,2*np.pi,41,endpoint=False):
        aa,ap=rotation(A,theta),rotation(A+da,theta)
        old,new=kernel(aa,B,mu),kernel(ap,B+db,mu)
        pair_bound=cx*np.linalg.norm(da,axis=1)[:,None]+cy*np.linalg.norm(db,axis=1)[None,:]
        ck(f"pair transport {mu}:{theta:.5f}",np.all(abs(new-old)<=pair_bound+1e-13),
           maximum_ratio=float(np.max(abs(new-old)/pair_bound)))
        diff=float(wa@(new-old)@wb)
        differences.append(diff)
        ck(f"mass transport {mu}:{theta:.5f}",abs(diff)<=envelope+1e-13,
           error=abs(diff),bound=envelope)
    angles=np.linspace(0,2*np.pi,41,endpoint=False)
    for n in (1,2,3,6):
        coefficient=np.mean(np.array(differences)*np.exp(-1j*n*angles))
        ck(f"complex harmonic {mu}:{n}",abs(coefficient)<=envelope+1e-13,
           amplitude=float(abs(coefficient)),bound=envelope)
        ck(f"real harmonic {mu}:{n}",2*abs(coefficient)<=2*envelope+1e-13)
    details.append(dict(mu=mu,d=d,L=L,D_A=D_A,D_B=D_B,complex_bound=envelope,
                        max_direct_change=max(abs(v) for v in differences)))

# Zero signed net mass does not annihilate the torque response.
contrast=np.array([1.,-1.,0.])
effect=float(contrast@kernel(A,B,0.)@wb)
ck("zero net mass is not zero torque",sum(contrast)==0 and abs(effect)>1e-3,
   signed_net_mass=float(sum(contrast)),total_variation=float(sum(abs(contrast))),torque=effect)
examples=[]
for mu in (0.,20000.):
    ma,mb=.65749e-3,1.19856e-3
    d0,L,ea,eb=50e-6,.027,1e-6,1e-6
    gap=d0-ea-eb
    cx,cy=constants(mu,gap,L)
    complex_geometry=ma*mb*(cx*ea+cy*eb)
    torque=6.6742e-11*complex_geometry
    examples.append(dict(mu_per_m=mu,assumed_gap_m=gap,assumed_lever_m=L,
                         complex_torque_bound_fNm=float(torque*1e15),
                         real_harmonic_bound_fNm=float(2*torque*1e15),
                         assumed_unit_scalar_strength=True,
                         scope="Scale illustration only; displacement certificates and reference coupling are stipulated, not inferred."))
out=dict(source_hashes={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in
                      ("LAB_GEOMETRY_TRANSPORT_v1.md",Path(__file__).name)},
         passed=sum(c["passed"] for c in checks),failed=sum(not c["passed"] for c in checks),
         checks=checks,synthetic_details=details,illustrative_envelopes=examples,
         empirical_validation=False)
print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))
if out["failed"]: raise SystemExit(1)

