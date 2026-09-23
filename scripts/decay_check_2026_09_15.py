"""Canonical Weyl phase-space checks; no microscopic quantum phase is simulated."""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/SUPPLIED_QUARTET_LEADING_DECAY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/SUPPLIED_QUARTET_LINEAR_METRIC_FLOW_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/SUPPLIED_QUARTET_QUADRATIC_BACKREACTION_BOUNDED_THEOREM_NOTE_2026-09-15.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'supplied_quartet_leading_decay_bounds_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SUPPLIED_QUARTET_LEADING_DECAY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/decay_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
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
    for x,p,weight in zip(xx,ps,ww):
        # Solve the momentum triangle symmetrically. Avoid 1-cos(theta)^2
        # followed by subtraction of two nearly parallel large vectors.
        q=(omega-K*x)/2;parallel_p=(K+omega*x)/2;parallel_q=(K-omega*x)/2
        transverse=math.sqrt((omega-K)*(omega+K)*(1-x)*(1+x))/2
        for j in range(nphi):
            phi=2*math.pi*j/nphi;tangent=math.cos(phi)*b1+math.sin(phi)*b2
            n=(parallel_p*direction+transverse*tangent)/p
            m=(parallel_q*direction-transverse*tangent)/q
            require(np.linalg.norm(p*n+q*m-Kvec)<2e-14,'symmetric phase-space triangle conserves vector momentum')
            require(max(abs(np.linalg.norm(n)-1),abs(np.linalg.norm(m)-1))<2e-12,'photon final rescaled spin directions satisfy energy constraint')
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
    rate=fermion_cap(V,p,192,128)/E;refined=fermion_cap(V,p,256,256)/E
    require(rate>0 and abs(rate-refined)<1e-10,'exact angular-boundary emission escapes a zero-first-order-rate inference')
    require(fermion_cap(V,np.array([0.,1,0]))==0,'unchanged y direction remains at exact no-emission threshold')
    require(abs(rate-7*d*d/(12*math.pi))<.2*d**4,'analytic boundary coefficient agrees with exact cap integral')
    boundary.append({'d':d,'group_speed_squared':speed2,'rate_per_energy':rate,'leading_boundary_rate':7*d*d/(12*math.pi),'refinement_error':abs(rate-refined)})

# Expand the original tensor contraction on the paraxial boundary chart.
dsym,yy,zz=sp.symbols('dsym yy zz',real=True);rr=yy*yy+zz*zz
VV=sp.Matrix([[1,0,dsym],[0,1,0],[dsym,0,1]]);GG=VV*VV
mm=sp.Matrix([1-dsym*dsym*rr/2,dsym*yy,dsym*zz]);pp=sp.Matrix([1,0,0])
EE=1+dsym*dsym/2;hh=VV*pp*(1-dsym*dsym/2)
kk=(1-rr+4*zz)/(1+4*zz);KK=GG-(VV*mm)*(VV*mm).T;Vqq=EE*hh-kk*VV*mm
TT=(EE-kk-(Vqq.T*hh)[0])*sp.trace(KK)/2+(Vqq.T*KK*hh)[0]
FF=(1+4*zz+8*rr-4*zz*rr+rr*rr)/(2*(1+4*zz)**2)
require(sp.factor(sp.expand(TT).coeff(dsym,2)/(1+4*zz)-FF)==0,'original coframe current gives boundary cap rational integrand')

# Independent exact integration of the boundary cap after y is integrated.
zeta=sp.symbols('zeta',real=True);A0=1+4*zeta;DD=A0-zeta*zeta
BB=sp.expand(A0+(8-4*zeta)*zeta*zeta+zeta**4+DD*((8-4*zeta)+2*zeta*zeta)/3+DD*DD/5)
apart=zeta*zeta/30-7*zeta/60+sp.Rational(131,480)+193/(60*A0)+181/(480*A0*A0)
require(sp.simplify(BB/A0**2-apart)==0,'boundary cap polynomial division exact')
semicircle=sp.Rational(105,8)/30-sp.Rational(7,60)*5+sp.Rational(131,480)*sp.Rational(5,2)+sp.Rational(193,120)+sp.Rational(181,960)
require(sp.simplify(semicircle-sp.Rational(7,3))==0,'boundary integrated coefficient equals seven pi over three')
# A phase-speed-one collinear ray may lie on the cap boundary, never its interior.
Gedge=np.array([[1.,0,.2],[0,1.,0],[.2,0,1.]]);lam,U=np.linalg.eigh(Gedge);Vedge=(U*np.sqrt(lam))@U.T
ped=np.array([1.,0,0]);med=ped;Eed=np.linalg.norm(Vedge@ped);aed=med@Gedge@med-1;bed=med@Gedge@ped-Eed
# Here a=b=0 for m=p: the photon and fermion line coincide on this direction.
# This direction is on the cap boundary (v_g dot m=1), not inside it.
require(abs(aed)<1e-14 and abs(bed)<1e-14,'phase-speed-one collinear ray is an exceptional cap boundary')

root=Path(__file__).resolve().parents[1];files=[Path(__file__).resolve(),root/'docs/SUPPLIED_QUARTET_LEADING_DECAY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
result={'status':'PASS_personal_decay_and_kinematic_challenges','checks':dict(checks),'isotropic_fermion':scalar_results,'anisotropic_photon':photon_results,'native_quartet':quartet,'angular_boundary_escape':boundary,'seconds':time.monotonic()-start,
'limits':['leading coupling order in a supplied massless action','continuum cones, not an interacting finite-link ground state','running substitution is a leading-log approximation','no pole residue, soft-photon dressing or all-order lifetime theorem','same-author verification'],
'sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
out=json.dumps(result,indent=2);_OUTPUT_JSON.write_text(out+'\n');print(out)

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: leading kinematic and polarization fixtures')
    print('per_site: not executed: continuum phase-space fixtures')
    print('per_mode: finite angular quadrature and momentum-direction samples')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
