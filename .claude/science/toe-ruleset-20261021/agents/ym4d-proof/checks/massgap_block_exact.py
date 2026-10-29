#!/usr/bin/env python3
"""Finite author controls. Not independent review or a continuum proof."""
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.special import iv
import sympy as sp

HERE = Path(__file__).resolve().parent
checks = []
mutations = []
metrics = {}


def check(name, condition, **detail):
    checks.append(dict(name=name, passed=bool(condition), **detail))


def kill(name, detected, **detail):
    mutations.append(dict(name=name, killed=bool(detected), **detail))
    check('mutation: ' + name, detected, **detail)


def maxerr(a, b):
    return float(np.max(np.abs(np.asarray(a) - np.asarray(b))))


def states(n):
    return np.array(list(itertools.product([-1, 1], repeat=n)), dtype=int)


def torus(side):
    vertices = list(itertools.product(range(side), repeat=3))
    edges = [(v, mu) for v in vertices for mu in range(3)]
    index = {e: i for i, e in enumerate(edges)}
    def shift(v, mu):
        ans = list(v)
        ans[mu] = (ans[mu] + 1) % side
        return tuple(ans)
    plaquettes = []
    for v in vertices:
        for mu in range(3):
            for nu in range(mu + 1, 3):
                plaquettes.append((index[v, mu], index[shift(v, mu), nu],
                                   index[shift(v, nu), mu], index[v, nu]))
    return vertices, edges, plaquettes


def incidence(n, plaquettes, omit_spatial=False):
    m = np.zeros((n, n), dtype=int)
    if not omit_spatial:
        for p in plaquettes:
            for i in p:
                for j in p:
                    if i != j:
                        m[i, j] += 1
    return m


def slab_adjacency(m, depth):
    n = len(m)
    return (np.kron(np.eye(depth, dtype=int), m)
            + np.kron(np.eye(depth, k=1, dtype=int)
                      + np.eye(depth, k=-1, dtype=int), np.eye(n, dtype=int)))


# Exact geometric and contraction constants, before physical diagnostics.
b = sp.Rational(1, 32)
q = 14*b
Q = 12*b + b*b/(1-q)
r = b/(1-Q)
check('endpoint exact constants', (q, Q, r) ==
      (sp.Rational(7, 16), sp.Rational(217, 576), sp.Rational(18, 359)),
      q=str(q), Q=str(Q), r=str(r))
for side in (4, 5):
    vertices, edges, ps = torus(side)
    B = set(ps[0])
    pB = sum(bool(B.intersection(p)) for p in ps)
    m = incidence(len(edges), ps)
    check(f'3D torus side {side}: b=4,p_B=13', len(B) == 4 and pB == 13,
          edges=len(edges), p_B=pB)
    check(f'3D torus side {side}: spatial row 12',
          np.all(m.sum(axis=1) == 12))
    if side == 4:
        adj = slab_adjacency(m, 3)
        n = len(m)
        check('assembled half-slab interior row 14',
              np.all(adj[n:2*n].sum(axis=1) == 14))
        check('assembled half-slab endpoint row 13',
              np.all(adj[:n].sum(axis=1) == 13))
        bad = slab_adjacency(incidence(len(edges), ps, omit_spatial=True), 3)
        kill('omit spatial plaquettes from actual slab adjacency',
             not np.all(bad[n:2*n].sum(axis=1) == 14))

# Exact rational tensor control: B has two coordinates, exterior has two.
ss = states(4)
z = sp.Rational(1, 3)
P1 = sp.Matrix([[1+z, 1-z], [1-z, 1+z]])/2
PB = sp.kronecker_product(P1, P1)
PO = sp.kronecker_product(P1, P1)
P = sp.kronecker_product(PB, PO)
u = sp.Matrix([2 + sp.Rational(2,5)*a*b + sp.Rational(1,3)*a*c
               + sp.Rational(1,4)*b*d + sp.Rational(1,5)*a*b*c*d
               for a,b,c,d in ss])
W = sp.Matrix([int(a*b) for a,b,c,d in ss])
den = (u.T*P*u)[0]/16
pi = [sp.simplify(u[i]*(P*u)[i]/(16*den)) for i in range(16)]
mean = sp.simplify(sum(pi[i]*W[i] for i in range(16)))
F = W - mean*sp.ones(16,1)
g = sp.matrix_multiply_elementwise(u, F)
num = (g.T*P*g)[0]/16
bf, umin, ratios = [], [], []
for o in range(4):
    inds = [4*bb+o for bb in range(4)]
    mn = min(u[i] for i in inds)
    umin.append(mn)
    ratios.extend(u[i]/mn for i in inds)
    bf.append(sum(u[i]*F[i]**2 for i in inds)/4)
R = max(ratios)
Bf, Umin = sp.Matrix(bf), sp.Matrix(umin)
rho = z*z
cc = 1/(1+1/rho)
projected = cc*(Bf.T*PO*Bf)[0]/4
outside = (Umin.T*PO*Umin)[0]/4
eta = cc/R**2
check('exact tensor center is actual Perron pi',
      sum(pi) == 1 and sum(pi[i]*F[i] for i in range(16)) == 0,
      mean=str(mean), construction='psi^2=u(Pu)/<u,Pu>; A=u/psi')
check('operator rank-one projection of full tensor form', num >= projected,
      numerator=str(num), projected=str(projected))
check('pointwise exterior positive kernel lower bound',
      projected >= cc*outside and all(bf[i] >= umin[i] for i in range(4)))
check('pointwise denominator bound retains exterior kernel', den <= R**2*outside)
check('exact entangled tensor witness bound', num/den >= eta,
      correlation=str(sp.simplify(num/den)), eta=str(eta), local_ratio=str(R))
local_F = sp.Matrix([int(a*b)-mean for a,b in states(2)])
sharp_c = 1/(mean**2+1/rho)
sharp_g = PB.inv()*local_F
sharp_quad = (sharp_g.T*PB*sharp_g)[0]/4
sharp_projection = sharp_c*((local_F.T*sharp_g)[0]/4)**2
check('local rank-one sharp saturation', sp.simplify(sharp_quad-sharp_projection) == 0)
rank_matrix = PB-cc*local_F*local_F.T/4
principal = [rank_matrix.extract(ids,ids).det()
             for k in range(1,5) for ids in itertools.combinations(range(4),k)]
check('local operator inequality: all exact principal minors', min(principal) >= 0)
wrong_c = 1/(mean**2+1/z)
kill('omit implemented local edge power in rank-one bound',
     sharp_quad - wrong_c*((local_F.T*sharp_g)[0]/4)**2 < 0)
constant_u_corr = rho
kill('replace local convolution eigenvalue by one', sp.Rational(1,2) > constant_u_corr)
kill('omit edge power in uniform witness fixture', 1/(1+1/z) > constant_u_corr)
identity_projected = cc*(Bf.T*Bf)[0]/4
kill('replace retained exterior kernel by identity', identity_projected != projected,
     exact_difference=str(sp.simplify(identity_projected-projected)))
local_eta = 1/(1+1/z**2)
spectator_results=[]
for nspectator in (0,1,3):
    ns=2+nspectator
    fullP=P1
    for _ in range(ns-1):
        fullP=sp.kronecker_product(fullP,P1)
    fullW=sp.Matrix([int(x[0]*x[1]) for x in states(ns)])
    fullcorr=sp.simplify((fullW.T*fullP*fullW)[0]/2**ns)
    spectator_results.append((nspectator,fullcorr))
    check(f'actual spectator tensor product, spectator count {nspectator}',
          fullcorr==rho and fullcorr>=local_eta,correlation=str(fullcorr),
          local_bound=str(local_eta))
kill('use total edge count instead of block count',
     1/(1+1/z**6) != local_eta)

# Finite Z2 Wilson analogue: two adjacent spatial plaquettes, seven edges.
verts = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]
edges = [((0,0),(1,0)),((1,0),(2,0)),((0,1),(1,1)),
         ((1,1),(2,1)),((0,0),(0,1)),((1,0),(1,1)),((2,0),(2,1))]
ps = [(0,5,2,4),(1,6,3,5)]
X = states(7)
nx = len(X)
lookup = {tuple(x):i for i,x in enumerate(X)}
flips = []
for e in range(7):
    flip = X.copy()
    flip[:,e] *= -1
    flips.append(np.array([lookup[tuple(x)] for x in flip]))
loops = np.array([np.prod(X[:,p], axis=1) for p in ps]).T
mgeom = incidence(7, ps)


def z2_transfer(beta):
    kval = np.prod(1+math.tanh(beta)*X[:,None,:]*X[None,:,:], axis=2)/nx
    A = np.exp(-beta/2*np.sum(1-loops, axis=1))
    T = A[:,None]*kval*A[None,:]
    eig, vec = np.linalg.eigh(T)
    psi = vec[:,-1]*math.sqrt(nx)
    if psi.sum() < 0:
        psi = -psi
    u = A*psi
    PH = kval*u[None,:]/(kval@u)[:,None]
    pi = psi*psi/nx
    return dict(k=kval,A=A,T=T,lam=eig[-1],psi=psi,u=u,P=PH,pi=pi)


zz = z2_transfer(.4)
A, k, T, psi, u, PH, pi = [zz[key] for key in ('A','k','T','psi','u','P','pi')]
check('finite Z2 full transfer Perron identity', maxerr(T@psi,zz['lam']*psi)<2e-13)
check('finite Z2 actual Doob normalization and stationarity',
      maxerr(PH.sum(axis=1),1)<2e-14 and maxerr(pi@PH,pi)<2e-14)
psi2_direct = A*(k@(A*A*(k@A)))
check('actual open slab including terminal half factor', maxerr(psi2_direct,T@(T@np.ones(nx)))<1e-13)
wrong_terminal = A*(k@(A*A*(k@(A*A))))
kill('replace terminal half-spatial factor by full factor',
     maxerr(wrong_terminal,psi2_direct)>1e-6,
     difference=maxerr(wrong_terminal,psi2_direct))
maxratio, maxuratio = 0.0,0.0
for e in range(7):
    ratio = np.log(psi/A)-np.log((psi/A)[flips[e]])
    uratio = np.log(u)-np.log(u[flips[e]])
    pe = sum(e in p for p in ps)
    maxratio = max(maxratio,float(np.max(np.abs(ratio))))
    maxuratio = max(maxuratio,float(np.max(np.abs(uratio))))
    check(f'actual Z2 local Perron ratio edge {e}', np.max(np.abs(ratio))<=.8+1e-13)
    check(f'actual Z2 u ratio edge {e}', np.max(np.abs(uratio))<=.8*(pe+1)+1e-13)
W = loops[:,0]
mean_pi = float(pi@W)
mean_nu = float((u@W)/u.sum())
kill('center observable under auxiliary A psi measure', abs(mean_pi-mean_nu)>1e-7,
     pi_mean=mean_pi, auxiliary_mean=mean_nu)
PH_without_psi = k*A[None,:]/(k@A)[:,None]
kill('omit psi from implemented conditional kernel',
     maxerr(pi@PH_without_psi,pi)>1e-7,
     stationarity_error=maxerr(pi@PH_without_psi,pi))
# Explicit projection over all 2^6 vertex gauge transformations.
vertex_index={v:i for i,v in enumerate(verts)}
permutations=[]
for h in states(6):
    signs=np.array([h[vertex_index[a]]*h[vertex_index[b]] for a,b in edges])
    permutations.append([lookup[tuple(x*signs)] for x in X])
kgauge=sum(k[:,perm] for perm in permutations)/len(permutations)
PG=kgauge*u[None,:]/(kgauge@u)[:,None]
check('explicit gauge projector agrees on both loop observables',
      maxerr(PG@loops,PH@loops)<2e-13)
kill('extend projector-removal equality to gauge-variant functions',
     maxerr(PG@X[:,0],PH@X[:,0])>1e-4)
# Boundary log partition mixed finite difference versus integrated covariance.
idx=lookup[(1,)*7]
e,f=0,2
base=k[idx,:]*A*A*(k@A)
he=-.8*X[:,e]
hf=-.8*X[:,f]
def logZ(s,t):
    return math.log(float(np.sum(base*np.exp(s*he+t*hf))))
mixed=logZ(1,1)-logZ(1,0)-logZ(0,1)+logZ(0,0)
nodes,weights=np.polynomial.legendre.leggauss(16)
integ=0.0
for s,ws in zip((nodes+1)/2,weights/2):
    for t,wt in zip((nodes+1)/2,weights/2):
        p=base*np.exp(s*he+t*hf)
        p/=p.sum()
        integ+=ws*wt*(p@(he*hf)-(p@he)*(p@hf))
check('actual slab mixed-ratio covariance identity', abs(mixed-integ)<3e-13,
      mixed=mixed, integrated_covariance=integ)
kill('omit covariance in actual boundary response', abs(mixed)>1e-8)

# Actual physical one-step sensitivity at the declared endpoint.
beta=.025
zzs=z2_transfer(beta)
A,k,T,psi,u,PH,pi=[zzs[key] for key in ('A','k','T','psi','u','P','pi')]
S=beta*mgeom
vals,vecs=np.linalg.eigh(S)
dvals=2/(1-vals+np.sqrt((1-vals)**2-4*beta**2))
Dfirst=(vecs*dvals)@vecs.T
finiteC=beta*slab_adjacency(mgeom,8)
Dfinite=np.linalg.inv(np.eye(len(finiteC))-finiteC)[:7,:7]
check('half-line boundary resolvent matches independent slab inverse',
      maxerr(Dfirst,Dfinite)<3e-13)
Cstep=S+beta**2*Dfirst
np.fill_diagonal(Cstep,0)
Qb=12*beta+beta**2/(1-14*beta)
rb=beta/(1-Qb)
check('assembled actual step majorant obeys volume-free row bound',
      float(np.max(Cstep.sum(axis=1)))<=Qb+1e-13)
U=X[-1]
weights=u*np.exp(beta*(X@U))
def conditional_plus(ww,i):
    numerator=np.where(X[:,i]>0,ww,ww[flips[i]])
    return numerator/(ww+ww[flips[i]])
Cactual=np.zeros((7,7))
for i in range(7):
    pp=conditional_plus(weights,i)
    for j in range(7):
        if i!=j:
            Cactual[i,j]=np.max(np.abs(pp-pp[flips[j]]))
check('actual ground-state output conditionals satisfy assembled majorant',
      bool(np.all(Cactual<=Cstep+2e-13)), max_actual=float(Cactual.max()),
      max_majorant=float(Cstep.max()))
Cbad=beta**2*Dfirst.copy()
np.fill_diagonal(Cbad,0)
kill('omit magnetic spatial terms from implemented step majorant',
     bool(np.any(Cactual>Cbad+1e-6)))
defects=[]
for i in range(7):
    changed=weights*np.exp(-2*beta*X[:,0])
    defects.append(np.max(np.abs(conditional_plus(weights,i)-conditional_plus(changed,i))))
check('actual input source conditional defect has one-site support',
      defects[0]<=beta+1e-13 and max(defects[1:])<1e-13 and defects[0]>1e-4,
      defects=[float(x) for x in defects])
wrong_support=np.zeros(7)
wrong_support[1]=beta
kill('shift implemented boundary source support to adjacent output link',
     bool(np.any(np.array(defects)>wrong_support+1e-6)))
def oscs(F):
    return np.array([np.max(np.abs(F-F[flip])) for flip in flips])
for name,F in [('left_loop',loops[:,0]),('right_loop',loops[:,1]),
               ('loop_product',loops[:,0]*loops[:,1]),
               ('all_sector_function',np.sin(X@np.arange(1,8)))]:
    lhs=float(oscs(PH@F).sum())
    rhs=float(rb*oscs(F).sum())
    check('actual physical-time oscillation contraction: '+name,lhs<=rhs+2e-13,
          lhs=lhs,rhs=rhs)
    centered=F-pi@F
    fn=centered.copy()
    for n in range(4):
        corr=float((pi*centered)@fn)
        bound=float(.25*oscs(F).sum()**2*rb**n)
        check(f'actual physical covariance {name}, n={n}',abs(corr)<=bound+2e-13)
        fn=PH@fn

# Actual SU(2) cycle: Bessel construction versus coordinate Haar assembly.
M=96
nrep=21
angles=np.arange(1,M+1)*math.pi/(M+1)
xx=np.cos(angles)
haar=2/(M+1)*np.sin(angles)**2
chars=np.sin(angles[:,None]*np.arange(1,nrep+1))/np.sin(angles[:,None])
Qbasis=np.sqrt(haar)[:,None]*chars
check('SU2 coordinate Haar character orthonormality',
      maxerr(Qbasis.T@Qbasis,np.eye(nrep))<2e-13)
check('SU2 coordinate Haar loop variance',abs(float(haar@(xx*xx))-.25)<2e-14)
check('SU3 complex-character Haar loop variance',sp.Rational(2,4*3**2)==sp.Rational(1,18))
kill('use self-conjugate SU2 factor for SU3',sp.Rational(1,3**2)!=sp.Rational(1,18))

def cycle_bessel(beta,power=4):
    rr=iv(np.arange(1,nrep+1),beta)/iv(1,beta)
    A=np.exp(-beta/2*(1-xx))
    return A[:,None]*((Qbasis*(rr**power))@Qbasis.T)*A[None,:],A,rr

def cycle_coordinate(beta,omit_dimension=False):
    coeff=chars.T@(haar*np.exp(beta*xx))
    rr=coeff/coeff[0]
    if not omit_dimension:
        rr=rr/np.arange(1,nrep+1)
    one=(Qbasis*rr)@Qbasis.T
    four=one@one@one@one
    A=np.exp(-beta/2*(1-xx))
    return A[:,None]*four*A[None,:]

for beta in (.125,.5,1.,3.):
    TB,A,rr=cycle_bessel(beta)
    TC=cycle_coordinate(beta)
    check(f'SU2 actual cycle independent operator beta={beta}',maxerr(TB,TC)<3e-10,
          error=maxerr(TB,TC))
    eig,ev=np.linalg.eigh(TB)
    eigC,evC=np.linalg.eigh(TC)
    psiC=evC[:,-1]
    mC=float((psiC*psiC)@xx)
    vC=psiC*(xx-mC)
    corrC=float(vC@(TC@vC)/eigC[-1])
    Kcycle=TC/(A[:,None]*A[None,:])
    slab_direct=A*(Kcycle@(A*A*(Kcycle@(A*np.sqrt(haar)))))
    slab_iterated=TC@(TC@np.sqrt(haar))
    check(f'SU2 actual open-slab factors beta={beta}',
          maxerr(slab_direct,slab_iterated)<3e-13)
    top=ev[:,-1]
    if top.sum()<0:
        top=-top
    psi=top/np.sqrt(haar)
    m=float((top*top)@xx)
    vec=top*(xx-m)
    covariance=float(vec@(TB@vec)/eig[-1])
    check(f'SU2 independent top eigenvalue and centered covariance beta={beta}',
          abs(eig[-1]-eigC[-1])<3e-10 and abs(covariance-corrC)<3e-10,
          covariance_difference=abs(covariance-corrC))
    v=.25
    eta=v*v*math.exp(-20*beta)/(1+v/rr[1]**4)
    check(f'SU2 actual centered one-step witness beta={beta}',covariance>=eta*(1-1e-10),
          covariance=covariance,eta=eta,actual_pi_mean=m)
    logR=np.log(psi/A)
    logu=np.log(A*psi)
    check(f'SU2 actual local Perron and u ratios beta={beta}',
          np.ptp(logR)<=2*beta+3e-12 and np.ptp(logu)<=4*beta+3e-12,
          ratio_log_range=float(np.ptp(logR)),u_log_range=float(np.ptp(logu)))
    badpower=cycle_bessel(beta,power=1)[0]
    baddim=cycle_coordinate(beta,omit_dimension=True)
    kill(f'mutate implemented SU2 cycle power beta={beta}',maxerr(badpower,TC)>3e-10)
    kill(f'mutate implemented SU2 dimension division beta={beta}',maxerr(baddim,TB)>3e-10)
    metrics[f'su2_beta_{beta}']=dict(lambda0=float(eig[-1]),covariance=covariance,eta=eta)

# Explicit scale bookkeeping; neither bound is a continuum witness.
r_endpoint=float(sp.Rational(18,359))
eta_fixed=1e-8
for a in (1.,.5,.25):
    ml=-math.log(r_endpoint)/a
    mu=-math.log(eta_fixed)/a
    check(f'physical units at spacing {a}',
          abs(a*ml+math.log(r_endpoint))<1e-14 and
          abs(a*mu+math.log(eta_fixed))<1e-14)
metrics['full_scope_not_executed']=[
    'continuum existence', 'large-beta all-half-slab covariance bound',
    'exact RG crossover with all source-only and conditional terms',
    'cutoff-uniform physical-time prefactor and onset',
    'continuum finite-energy witness', 'independent review']
result=dict(scope='finite author controls; analytic candidate is separately stated in note',
            versions=dict(python=platform.python_version(),numpy=np.__version__,
                          scipy=scipy.__version__,sympy=sp.__version__),
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            checks=checks,mutations=mutations,metrics=metrics,
            passed=sum(c['passed'] for c in checks),total=len(checks),
            all_passed=all(c['passed'] for c in checks),MG_rows_closed=[],
            independent_review=False)
out=HERE/'massgap_block_results.json'
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:result[k] for k in ('passed','total','all_passed')},sort_keys=True))
for c in checks:
    if not c['passed']:
        print(json.dumps(c,sort_keys=True))
raise SystemExit(0 if result['all_passed'] else 1)
