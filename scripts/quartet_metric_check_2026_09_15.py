"""Finite algebra and native-jet challenges of a formal one-loop derivation."""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/SUPPLIED_QUARTET_LINEAR_METRIC_FLOW_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/LOCAL_HALL_FREE_MIXED_WEYL_QUARTET_AND_COMMON_METRIC_BOUNDED_THEOREM_NOTE_2026-09-13.md', 'docs/NATIVE_WEYL_GAUGE_HALL_AND_CONE_FLOW_BOUNDED_THEOREM_NOTE_2026-09-13.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'supplied_quartet_linear_metric_flow_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SUPPLIED_QUARTET_LINEAR_METRIC_FLOW_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/quartet_metric_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib,json,math,time
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

start=time.monotonic();checks=Counter()
def require(ok,label):
    if not ok:raise AssertionError(label)
    checks[label]+=1

def tf(A):return A-np.trace(A)*np.eye(3)/3

# Recompute the coframe derivative coefficients by parameter integration.
x=sp.symbols('x',real=True)
require(sp.integrate(x*(6-4*x),(x,0,1))==sp.Rational(5,3),'fermion coframe derivative coefficient')
require(sp.integrate(2*x*x,(x,0,1))==sp.Rational(2,3),'fermion coframe trace coefficient')
require(8*sp.integrate(x*(1-x),(x,0,1))==sp.Rational(4,3),'Dirac photon bubble radial coefficient')

# Weyl traces and zero linear birefringent insertion, using actual Clifford matrices.
I2=np.eye(2);sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1.])
gamma=[np.kron(sz,I2)]+[np.kron(sx,a) for a in (sx,sy,sz)]
g5=gamma[0]@gamma[1]@gamma[2]@gamma[3]
require(np.max(abs(g5@g5-np.eye(4)))<1e-14,'Euclidean chirality squares to identity')
projectors=[(np.eye(4)+sgn*g5)/2 for sgn in (-1,1)]
for a,b,c,d in product(range(4),repeat=4):
    mat=gamma[a]@gamma[b]@gamma[c]@gamma[d]
    even=.5*(np.trace(projectors[0]@mat)+np.trace(projectors[1]@mat))
    require(abs(even-.5*np.trace(mat))<1e-14,'parity-even Weyl closed trace is half Dirac')

points=[]
for i in range(4):
    for sign in (-1,1):
        p=np.zeros(4);p[i]=sign;points.append(p)
points.extend(np.array(s)/2 for s in product((-1,1),repeat=4))
points=np.array(points)
require(np.max(abs(np.einsum('na,nb->ab',points,points)/24-np.eye(4)/4))<1e-14,'24-cell exact sphere second moment')
for a,b,c,d in product(range(4),repeat=4):
    target=((a==b)*(c==d)+(a==c)*(b==d)+(a==d)*(b==c))/24
    require(abs(np.mean(points[:,a]*points[:,b]*points[:,c]*points[:,d])-target)<1e-14,'24-cell exact sphere fourth moment')
W=np.array([[1,.3,-.2],[.3,-.4,.1],[-.2,.1,-.6]])
avg=np.zeros((4,4,4),complex)
for n in points:
    n0=n[0];k=n[1:];C=np.array([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
    K=np.zeros((4,4));K[0,0]=k@W@k;K[0,1:]=K[1:,0]=-n0*(W@k);K[1:,1:]=n0*n0*W+C.T@W@C
    require(np.linalg.norm(K@n)<1e-14 and abs(np.trace(K))<1e-14,'birefringent kernel transverse and traceless')
    gn=sum(n[a]*gamma[a] for a in range(4))
    for j in range(4):
        Y=gamma[j]-2*n[j]*gn
        actual=sum(K[a,b]*gamma[a]@Y@gamma[b] for a,b in product(range(4),repeat=2))
        expected=2*sum(K[j,b]*gamma[b] for b in range(4))
        require(np.linalg.norm(actual-expected)<1e-13,'pointwise Clifford birefringence insertion identity')
        avg[j]+=actual/24
require(np.linalg.norm(avg)<1e-13,'linear birefringence does not source fermion metric logarithm')

# Actual quartet: weighted graph, multiplicities, conserved average and energy.
B=sp.zeros(5)
for i in range(4):B[i,i]=2;B[i,4]=-2;B[4,i]=-sp.Rational(1,2)
B[4,4]=2
weights=sp.diag(*([sp.Rational(1,2)]*4+[2]))
require(weights*B==(weights*B).T,'quartet graph detailed balance')
require(B.eigenvals()=={sp.Integer(0):1,sp.Integer(2):3,sp.Integer(4):1},'quartet eigenvalues count four Weyl nodes once')
require(B*sp.ones(5,1)==sp.zeros(5,1),'common metric is the unique quartet zero mode')
cs=sp.Matrix(sp.symbols('c0:5'));mean=(sum(cs[i]/2 for i in range(4))+2*cs[4])/4
centered=cs-sp.ones(5,1)*mean
energy=(centered.T*weights*centered)[0]
energy_dot=-2*(centered.T*weights*B*centered)[0]
require(sp.expand(energy_dot+2*sum((cs[i]-cs[4])**2 for i in range(4)))==0,'exact weighted energy dissipation')
# A neutral spectator is a real exception to forced consensus.
B0=B.copy();B0[0,0]=B0[0,4]=B0[4,0]=0;B0[4,4]=sp.Rational(3,2)
require(len(B0.nullspace())==2,'zero-charge adverse control adds a disconnected zero mode')

# Independent symbolic integration of the fixed-coordinate constitutive variance.
z,t=sp.symbols('z t',positive=True)
variance_checks=[]
for N in (1,2,4,6):
    N=sp.Integer(N);p=1+2/N;f=(N+2*t**(-p))/(N+2)
    m1=sp.integrate(f,(t,1,z))/z;m2=sp.integrate(f*f,(t,1,z))/z
    predicted=2*N/(N+4)*(z**-1-z**(-2-4/N))
    require(sp.simplify(2*(m2-m1*m1)-predicted)==0,'metric-mean variance agrees with sourced birefringence ODE')
    contrast=2*sp.integrate(t**(-4/N),(t,1,z))/z
    require(sp.simplify(sp.diff(contrast,z)+contrast/z-2*z**(-1-4/N))==0,
            'contrast variance solves source ODE including resonance')
    variance_checks.append({'N':int(N),'mean_coefficient':str(predicted),'contrast_coefficient':str(contrast)})

# Independently project the literal mixed four-band Hamiltonian and its derivatives.
sinb=4/5;cosb=3/5;b=math.atan2(sinb,cosb);mu=.2;zeta=.6
sig=[np.kron(I2,s) for s in (sx,sy,sz)]
taux=np.kron(sx,I2);tauz=np.kron(sz,I2)
def native(k,theta):
    kx,ky,kz=k
    A=-math.cos(kx)*sinb*np.eye(4)+math.sin(kx)*cosb*tauz+mu*math.sin(theta)*taux
    Bm=(2+zeta-math.cos(kx)*cosb-math.cos(ky)-math.cos(kz))*np.eye(4)-math.sin(kx)*sinb*tauz+mu*math.cos(theta)*taux
    return math.sin(ky)*sig[1]+A@sig[0]+Bm@sig[2]
def velocities(k):
    kx,ky,kz=k
    return [(math.sin(kx)*sinb*np.eye(4)+math.cos(kx)*cosb*tauz)@sig[0]
            +(math.sin(kx)*cosb*np.eye(4)-math.cos(kx)*sinb*tauz)@sig[2],
            math.cos(ky)*sig[1]+math.sin(ky)*sig[2],math.sin(kz)*sig[2]]
def metric(theta,sxnode,sznode):
    R=math.sqrt(1-mu*mu*math.sin(2*theta-b)/sinb)
    X=(cosb-mu*mu*math.sin(2*theta)/(2*sinb))/R
    k=(sxnode*math.acos(X),0.,sznode*math.acos(1+zeta-R))
    H=native(k,theta);values,vecs=np.linalg.eigh(H);order=np.argsort(abs(values));V=vecs[:,order[:2]]
    require(max(abs(values[order[:2]]))<1e-13,'exact root lies in the full native four-band zero space')
    projected=[V.conj().T@v@V for v in velocities(k)]
    require(max(abs(np.trace(v)) for v in projected)<1e-13,'actual node velocities are untilted')
    return np.array([[.5*np.trace(v@w).real for w in projected] for v in projected])
G0=metric(b,1,1);D=np.sqrt(np.diag(G0));jet_results=[]
predicted=-mu*mu/(2*(1-mu*mu)*sinb*sinb)
for eta in (1e-3,5e-4,2.5e-4):
    errors=[]
    for xs,zs in product((-1,1),repeat=2):
        derivative=(metric(b+eta,xs,zs)-metric(b-eta,xs,zs))/(2*eta)
        actual=.5*derivative[0,2]/(D[0]*D[2])
        error=abs(actual-xs*zs*predicted);errors.append(error)
        require(error<5*eta*eta,'projected native shear derivative matches analytic contrast coefficient')
    jet_results.append({'step':eta,'max_error':max(errors),'predicted_coframe_derivative':predicted})

# Full positive constitutive tensors along the linear contrast trajectory.
O=np.array([[0,0,1],[0,0,0],[1,0,0.]])
constitutive_results=[]
for strength in (.02,.01,.005):
    for end in (2.,5.,10.):
        outputs=[]
        for degree in (64,128):
            nodes,ww=leggauss(degree);ts=1+(end-1)*(nodes+1)/2;ww=ww*(end-1)/2
            eps=np.eye(3);bb=np.eye(3)
            for tt,weight in zip(ts,ww):
                for sign in (-1,1):
                    V=np.eye(3)+sign*strength*O/tt
                    e=V@V/np.linalg.det(V);inv=np.linalg.inv(e)
                    eps+=.5*weight*e;bb+=.5*weight*inv
            eps/=end;bb/=end;outputs.append((eps,bb))
        require(max(np.linalg.norm(outputs[0][j]-outputs[1][j]) for j in (0,1))<1e-13,'positive constitutive quadrature cutoff comparison')
        eps,bb=outputs[-1];actual=.5*tf(eps@bb)
        predictedW=2*strength**2*(1/end-1/end**2)*tf(O@O)
        error=np.linalg.norm(actual-predictedW)
        require(error<20*strength**4,'full constitutive mixture matches quadratic variance')
        split=bb[2,2]/eps[1,1]-bb[1,1]/eps[2,2]
        predicted_split=4*strength**2*(1/end-1/end**2)
        require(abs(split-predicted_split)<30*strength**4,'actual photon polarization roots match predicted split')
        require(np.linalg.norm(actual)>strength**2/100,'zero average shear does not erase its variance')
        constitutive_results.append({'strength':strength,'z':end,'W_error':float(error),'split':float(split),'predicted_split':predicted_split})
# Different contrast multiplets can have isotropic variance; no universal split.
Oxy=np.array([[0,1,0],[1,0,0],[0,0,0.]])
Oyz=np.array([[0,0,0],[0,0,1],[0,1,0.]])
Ds=[a*Oxy+b*Oyz+c*O for a,b,c in ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))]
require(np.linalg.norm(sum(Ds))==0 and np.linalg.norm(tf(sum(D@D for D in Ds)/4))==0,
        'nonzero contrasts with isotropic variance need not source quadratic birefringence')

root=Path(__file__).resolve().parents[1]
result={'status':'PASS_personal_bounded_formal_loop_and_native_jet_challenges','quartet_spectrum':{'zero':1,'two':3,'four':1},
        'variance_checks':variance_checks,'native_jet_checks':jet_results,'constitutive_checks':constitutive_results,
        'checks':dict(checks),'seconds':time.monotonic()-start,
        'limits':['one-loop and small-anisotropy calculations, not a full quantum phase',
                  'four Weyl nodes count as two Dirac bubbles; each self-energy is local to its external node',
                  'native metric jets projected from actual four-band matrices',
                  'constitutive trajectories use derived linear running, not nonlinear all-orders flow',
                  'no empirical speed or scale fitted','same author; no independent audit'],
        'sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in
                  [Path(__file__).resolve(),root/'docs/SUPPLIED_QUARTET_LINEAR_METRIC_FLOW_BOUNDED_THEOREM_NOTE_2026-09-15.md']}}
out=json.dumps(result,indent=2);_OUTPUT_JSON.write_text(out+'\n');print(out)

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: quartet gamma/metric and polarization identities')
    print('per_site: not executed: continuum matrix and quadrature fixtures')
    print('per_mode: finite angular/matrix quadrature, not a constructed interacting phase')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
