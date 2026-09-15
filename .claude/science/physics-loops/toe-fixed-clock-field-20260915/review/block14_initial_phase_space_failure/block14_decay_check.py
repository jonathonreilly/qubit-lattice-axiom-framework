"""Canonical Weyl phase-space checks; no microscopic quantum phase is simulated."""
from pathlib import Path
from collections import Counter
from itertools import product
import hashlib,json,math,time
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
start=time.monotonic();checks=Counter()
def require(ok,label):
    if not ok:raise AssertionError(label)
    checks[label]+=1
sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1.]);sig=[sx,sy,sz]
def sigma(v):return sum(v[i]*sig[i] for i in range(3))
def proj(n):return (np.eye(2)+sigma(n))/2
def unit(n):return np.asarray(n)/np.linalg.norm(n)
def perp(n):
    n=unit(n);base=np.eye(3)[np.argmin(abs(n))];a=unit(np.cross(n,base));return a,np.cross(n,a)
a,x,v=sp.symbols('a x v',positive=True)
xmax=2/(1+a);poly=1-a*x+(1+a*a)*x*x/4
I=sp.integrate(poly,(x,0,xmax));I1=sp.integrate(x*poly,(x,0,xmax))
rate=sp.simplify((1-a*a)*I/(4*sp.pi))
power=sp.simplify(a*(1-a*a)*I1/(4*sp.pi))
exact=(v-1)*(4*v*v+3*v+1)/(6*sp.pi*v*(v+1)**2)
exact_power=(v-1)*(9*v*v+4*v+1)/(12*sp.pi*v*(v+1)**3)
require(sp.simplify(rate.subs(a,1/v)-exact)==0,'exact canonical Cherenkov number rate integral')
require(sp.simplify(power.subs(a,1/v)-exact_power)==0,'energy-weighted integral gives distinct radiated power')
u=sp.symbols('u',real=True)
require(sp.simplify(sp.diff(exact.subs(v,1+u),u).subs(u,0)-1/(3*sp.pi))==0,'Cherenkov leading massless coefficient')
require(sp.simplify(sp.diff(exact_power.subs(v,1+u),u).subs(u,0)-7/(48*sp.pi))==0,'radiated-power leading massless coefficient')
beta_v=-(v-1)*(4*v*v+3*v+1)/(6*sp.pi**2*(v+1)**2)
beta_c=(v-1/v)/(12*sp.pi**2)
require(sp.simplify(exact+sp.pi*beta_v/v)==0,'isotropic number rate agrees with separate fermion beta comparator')
require(sp.simplify((1-v*v)/(12*sp.pi*v)+sp.pi*beta_c)==0,'Dirac photon rate agrees with separate photon beta comparator')

# Actual Pauli matrices challenge the transverse spin contraction.
rng=np.random.default_rng(13217)
for ii in range(30):
    n=unit(rng.normal(size=3));m=unit(rng.normal(size=3));ph=unit(rng.normal(size=3));eps=perp(ph)
    M=rng.normal(size=(3,3));V=np.eye(3)+.04*(M+M.T)
    require(min(np.linalg.eigvalsh(V))>0,'positive coframe fixture')
    K=V@(np.eye(3)-np.outer(ph,ph))@V
    actual=sum(np.trace(proj(m)@sigma(V@e)@proj(n)@sigma(V@e)).real for e in eps)
    expected=.5*np.trace(K)*(1-m@n)+m@K@n
    require(abs(actual-expected)<2e-14,'actual Pauli transverse trace matches general-coframe formula')

# Exact angular cap formula for a general positive coframe, charge e^2=1.
def fermion_cap(V,p,degree=64,nphi=32):
    G=V@V;E=np.linalg.norm(V@p);g=G@p/E;speed=np.linalg.norm(g)
    if speed<=1:return 0.
    w=g/speed;b1,b2=perp(w);c0=1/speed
    points,weights=leggauss(degree);cc=c0+(1-c0)*(points+1)/2;weights*=((1-c0)/2)
    npart=V@p/E;ans=0.
    for c,wc in zip(cc,weights):
        ss=math.sqrt(max(0,1-c*c))
        for j in range(nphi):
            phi=2*math.pi*j/nphi;m=c*w+ss*(math.cos(phi)*b1+math.sin(phi)*b2)
            aa=m@G@m-1;bb=m@G@p-E;kk=2*bb/aa;Eq=E-kk;q=p-kk*m
            require(aa>0 and kk>0 and Eq>0,'general Cherenkov cap has a physical positive-energy root')
            require(abs(np.linalg.norm(V@q)-Eq)<2e-11,'cap root satisfies actual anisotropic energy conservation')
            K=V@(np.eye(3)-np.outer(m,m))@V;Vq=V@q
            T=.5*np.trace(K)*(Eq-Vq@npart)+Vq@K@npart
            require(T>=-1e-12,'cap spin-weighted energy is nonnegative')
            ans+=wc*(2*math.pi/nphi)*T/aa
    return ans/(4*math.pi**2)
scalar_results=[]
for vv in (1.01,1.1,1.5,2.):
    actual=fermion_cap(vv*np.eye(3),np.array([0.,0,1]),32,8)/vv
    expected=float(exact.subs(v,vv))
    require(abs(actual-expected)<2e-13,'independent angular cap recovers exact isotropic number rate')
    scalar_results.append({'v':vv,'rate_per_energy':actual,'error':abs(actual-expected)})

# Exact photon tensor and an independent Pauli phase-space integral.
def photon_tensor(V,k):
    omega=np.linalg.norm(k);G=V@V;Q2=omega*omega-k@G@k;eps=np.stack(perp(k))
    if Q2<=0:return np.zeros((2,2))
    a=eps@G@k
    return (Q2*eps@G@eps.T+np.outer(a,a))/(24*math.pi*omega*np.linalg.det(V))
def photon_phase_space(V,k,degree=64,nphi=8):
    omega=np.linalg.norm(k);Kvec=V@k;K=np.linalg.norm(Kvec);eps=np.stack(perp(k));currents=[sigma(V@e) for e in eps]
    if omega<=K:return np.zeros((2,2),complex)
    direction=Kvec/K;b1,b2=perp(direction);xx,ww=leggauss(degree)
    ps=omega/2+K*xx/2;ww=ww*K/2;answer=np.zeros((2,2),complex)
    for p,weight in zip(ps,ww):
        c=(K*K-omega*omega+2*omega*p)/(2*K*p);sn=math.sqrt(max(0,1-c*c));q=omega-p
        for j in range(nphi):
            phi=2*math.pi*j/nphi;n=c*direction+sn*(math.cos(phi)*b1+math.sin(phi)*b2)
            m=(Kvec-p*n)/q
            require(abs(np.linalg.norm(m)-1)<2e-12,'photon final rescaled spin directions satisfy energy constraint')
            PP=proj(n);PM=proj(m)
            SS=np.array([[np.trace(PP@Ja@PM@Jb) for Jb in currents] for Ja in currents])
            answer+=weight*(2*math.pi/nphi)*p*q/K*SS
    return answer/(8*math.pi**2*omega*np.linalg.det(V))
O=np.array([[0.,0,1],[0,0,0],[1,0,0]])
fixtures=[(.8*np.eye(3),unit([1,2,3])),(np.diag([.9,1.1,.95]),unit([1,2,3])),(np.eye(3)-.13*O,unit([1,2,3])),(np.array([[.91,.02,.03],[.02,.94,-.01],[.03,-.01,1.02]]),unit([2,1,1]))]
photon_results=[]
for V,k in fixtures:
    analytic=photon_tensor(V,k);numeric=photon_phase_space(V,k,64,8);refined=photon_phase_space(V,k,128,12)
    error=float(np.linalg.norm(analytic-numeric))
    require(error<1e-13 and np.linalg.norm(numeric-refined)<1e-13,'full Pauli phase-space integral matches anisotropic photon decay tensor')
    require(min(np.linalg.eigvalsh(analytic))>=-1e-14,'anisotropic photon probability-decay matrix positive')
    photon_results.append({'metric':(V@V).tolist(),'momentum':k.tolist(),'tensor':analytic.tolist(),'phase_space_error':error})
for vv in (.5,.8,.99):
    tensor=photon_tensor(vv*np.eye(3),np.array([0.,0,1]))
    expected=(1-vv*vv)/(24*math.pi*vv)
    require(np.linalg.norm(tensor-expected*np.eye(2))<1e-14,'one-Weyl isotropic photon rate has half Dirac multiplicity')
require(np.linalg.norm(photon_tensor(1.1*np.eye(3),unit([1,2,3])))==0,'superluminal cone cannot receive a photon pair')

# Actual reflected quartet: two fast and two slow cones. Rates add positively.
n=unit([1,2,3]);quartet=[]
for d in (.04,.02,.01):
    for z in (1.,3.,10.):
        e2=1/z;Vs=[np.eye(3)+sign*d*O/z for sign in (1,1,-1,-1)]
        photon=e2*sum(photon_tensor(V,n) for V in Vs)
        predicted=d*abs(n[0]*n[2])/(3*math.pi*z*z)
        error=float(np.linalg.norm(photon-predicted*np.eye(2)))
        require(error<d*d/z**3,'native quartet photon leading contrast and Weyl count')
        fermion=e2*fermion_cap(Vs[0],n,48,24)/np.linalg.norm(Vs[0]@n)
        predictedf=2*predicted
        require(abs(fermion-predictedf)<d*d/z**3,'native fast-cone Cherenkov leading angular coefficient')
        require(min(np.linalg.eigvalsh(photon))>0 and fermion>0,'zero mean and chirality cancellation do not cancel allowed rates')
        quartet.append({'d':d,'z':z,'photon_rate_eigenvalues':np.linalg.eigvalsh(photon).tolist(),'leading_photon_rate':predicted,'fermion_rate_per_energy':fermion,'leading_fermion_rate':predictedf})
# Adverse angular-boundary control: n.C.n=0 is not an exact zero-rate criterion.
boundary=[]
for d in (.04,.02,.01):
    V=np.eye(3)+d*O;p=np.array([1.,0,0]);G=V@V;E=np.linalg.norm(V@p);speed2=np.linalg.norm(G@p/E)**2
    require(abs(speed2-(1+6*d*d+d**4)/(1+d*d))<1e-14 and speed2>1,'phase-contrast zero can still have superluminal group velocity')
    rate=fermion_cap(V,p,64,32)/E;refined=fermion_cap(V,p,128,64)/E
    require(rate>0 and abs(rate-refined)<1e-10,'exact angular-boundary emission escapes a zero-first-order-rate inference')
    require(fermion_cap(V,np.array([0.,1,0]))==0,'unchanged y direction remains at exact no-emission threshold')
    boundary.append({'d':d,'group_speed_squared':speed2,'rate_per_energy':rate,'refinement_error':abs(rate-refined)})

root=Path(__file__).resolve().parents[1];files=[Path(__file__).resolve(),root/'notes/BLOCK14_QUARTET_DECAY_AND_CONE_STABILITY.md']
result={'status':'PASS_personal_decay_and_kinematic_challenges','checks':dict(checks),'isotropic_fermion':scalar_results,'anisotropic_photon':photon_results,'native_quartet':quartet,'angular_boundary_escape':boundary,'seconds':time.monotonic()-start,
'limits':['leading coupling order in a supplied massless action','continuum cones, not an interacting finite-link ground state','running substitution is a leading-log approximation','no pole residue, soft-photon dressing or all-order lifetime theorem','same-author verification'],
'sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
out=json.dumps(result,indent=2);Path(__file__).with_suffix('.json').write_text(out+'\n');print(out)
