#!/usr/bin/env python3
"""Finite algebra controls of the explicitly supplied exercise models; no empirical fit."""
import sys
if sys.flags.optimize:
    raise RuntimeError('Assertions require unoptimized Python')
import signal
AUDIT_TIMEOUT_SEC = 120
RUNNER_TIMEOUT_SEC = 120
def _deadline(signum, frame):
    raise TimeoutError('120-second aggregate exercise-control deadline exceeded')
signal.signal(signal.SIGALRM, _deadline)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC)
# Literal input closure is filled by the external packager before source freeze.
AUDIT_INPUT_PATHS = ['docs/CONDITIONAL_HIERARCHY_AND_MASS_EXERCISES_NOTE_2026-10-18.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/CORRECTION_REGISTER.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/README.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/scale-ladder/H1/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/scale-ladder/H2/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/scale-ladder/H3/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/K/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/LEE/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/R1/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/R2/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/R3/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/R4/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/T/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/T2/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/FP/derivations/generations-from-lattice-symmetry-2026-10-18.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/K/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R1/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R2/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R3/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R4/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R5/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/T/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/T3/REPORT.md', 'outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/T4/REPORT.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md', 'docs/audit/data/axiom_premise_nodes.json']
GENERATED_OUTPUTS = []
import itertools
from fractions import Fraction as Q
import math
import numpy as np
import sympy as sp
PASS = 0
def check(name, ok, detail):
    global PASS
    if not bool(ok):
        print('[FAIL]', name, detail, flush=True)
        raise AssertionError(name)
    PASS += 1
    print('[PASS]', name, detail, flush=True)

# Exact iterates, not a logarithm rounded to an expected exit index.
for lam, delta, rho in [(Q(2), Q(1,10), Q(1,4)), (Q(3,2),Q(1,100),Q(1,3)),
                        (Q(2),Q(1,16),Q(1,2)),(Q(5,4),Q(1,1000),Q(1,5))]:
    u=delta; n=0
    while u<rho:
        u*=lam; n+=1
    log_bound=math.log(float(rho/delta))/math.log(float(lam))
    check('first-exit '+str((lam,delta,rho)), u>=rho and u/lam<rho and n<=log_bound+1+1e-13,
          {'exit':n,'real_log_bound':log_bound,'rounding_factor':True})
# Exact coefficient substitution and monotonic inequalities for arbitrary symbols.
N,B=sp.symbols('N B', positive=True)
nf=(11*N-3*B)/2
b1=34*N**2/3-(13*N/3-1/N)*nf
expected=-25*N**2/2+sp.Rational(11,2)+B*(13*N-3/N)/2
check('two-loop substitution identity',sp.expand(b1-expected)==0,str(expected))
check('two-loop rational endpoint bound',Q(-201,20)*2+Q(11,2)==Q(-73,5),'-73/5 at N=2; slope -201/20')
check('B elementary numerical guard',8*(22/7)**2/(15*2.3)<2.3,'pi upper and log(10) lower comparator bounds')

# Assemble full two-site matrices and compare their ij block to the stated polynomial.
beta=np.diag([1.,-1.]); hops={'anticommuting':np.array([[0,2+1j],[3-2j,0]]),
                           'commuting':np.diag([2+1j,3-2j])}
for timing in (0.,.25,.5,1.):
    for label,T in hops.items():
        ni,nj,mi,mj=2.,-1.,3.,4.; mass=.7; D=ni*mj-mi*nj
        def H(a,b,m):
            w=timing*a+(1-timing)*b
            return np.block([[m*a*beta,w*T],[w*T.conj().T,m*b*beta]])
        def bracket(m):
            A=H(ni,nj,m); C=H(mi,mj,m);return A@C-C@A
        actual=(bracket(mass)-bracket(0))[:2,2:]
        predicted=mass*D*((1-timing)*beta@T+timing*T@beta)
        err=np.max(np.abs(actual-predicted))
        check('endpoint mass bracket '+label+' t='+str(timing),err<1e-12,{'max_error':float(err),'norm':float(np.linalg.norm(actual))})

# Enumerate the representation image directly; calculate the commutator-map rank.
group=[]
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((-1,1),repeat=3):
        g=np.zeros((3,3),int)
        for i,j in enumerate(perm):g[i,j]=signs[i]
        group.append(g)
keys={tuple(g.ravel()) for g in group}
closed=all(tuple((a@b).ravel()) in keys for a in group for b in group)
check('signed-permutation image closure',len(keys)==48 and closed,{'order':len(keys)})
units=[np.eye(9)[i].reshape(3,3) for i in range(9)]
constraint=np.concatenate([np.column_stack([(g@u-u@g).ravel() for u in units]) for g in group])
rank=np.linalg.matrix_rank(constraint,tol=1e-10)
check('scalar commutant of supplied image',rank==8,{'constraint_rank':int(rank),'commutant_dimension':9-int(rank)})
orbits={frozenset(tuple((g@np.array(c))%2) for g in group) for c in itertools.product((0,1),repeat=3)}
check('period-two corner orbit decomposition',sorted(map(len,orbits))==[1,1,3,3],sorted(map(len,orbits)))

# Analytic Bloch derivatives, arbitrary complex non-normal hopping blocks.
hops=[np.array([[j+1,2+1j*(j+1)],[-1+2j,j-2]],complex) for j in range(3)]
A=np.array([[2,1j],[-1j,3]])
def symbol(corner):
    return A+sum(((-1)**corner[j])*(T+T.conj().T) for j,T in enumerate(hops))
gamma=symbol([0,0,0]); cornerR=symbol([1,1,1]); xs=[]
for i in range(3):
    c=[int(j==i) for j in range(3)]; X=symbol(c); M=symbol([1-x for x in c]); xs.append(X)
    check('nearest-neighbor complementary corners '+str(i),np.array_equal(X+M,gamma+cornerR),{'axis':i})
for i,j in itertools.combinations(range(3),2):
    d_i=-(hops[i]+hops[i].conj().T);d_j=-(hops[j]+hops[j].conj().T)
    check('nearest-neighbor Hessian splitting '+str((i,j)),np.array_equal(xs[i]-xs[j],2*(d_i-d_j)),{'axes':[i,j]})

# Common residual versus two accidental image residuals: direct exact symbolic example.
r=sp.diag(1,-1); t=sp.Matrix([[-sp.Rational(1,2),sp.sqrt(3)/2],[sp.sqrt(3)/2,sp.Rational(1,2)]])
AA=2*sp.eye(2)+r; BB=3*sp.eye(2)+t
zero=lambda M:all(sp.simplify(x)==0 for x in M)
check('image stabilizers need not stabilize pair-state',zero(r*AA-AA*r) and zero(t*BB-BB*t) and not zero(r*BB-BB*r) and not zero(t*AA-AA*t),
      'Both coordinate projections are conjugation-equivariant; residuals of images differ')
C=np.roll(np.eye(3),1,axis=0); omega=np.exp(2j*np.pi/3)
F=np.array([[omega**(i*j) for j in range(3)] for i in range(3)])/np.sqrt(3)
Hu=F@np.diag([1,4,9])@F.conj().T; Hd=F@np.diag([7,2,5])@F.conj().T
_,U=np.linalg.eigh(Hu);_,V=np.linalg.eigh(Hd);mix=np.abs(U.conj().T@V)**2
check('common simple residual finite fixture',np.linalg.norm(C@Hu-Hu@C)<1e-12 and np.linalg.norm(C@Hd-Hd@C)<1e-12 and np.max(np.minimum(abs(mix),abs(mix-1)))<1e-12,mix.tolist())

# Symbolic trace identities for the exact original mass family.
x,y,m0,mJ,a,b=sp.symbols('x y m0 mJ a b',real=True); z=-x-y; e=[x,y,z]; rho2=sum(v*v for v in e)
Off=sp.Matrix([[0,z,y],[z,0,x],[y,x,0]])
M=m0*sp.eye(3)+mJ*(sp.ones(3)-sp.eye(3))+a*sp.diag(*e)+b*Off
tr2=sp.expand(sp.trace(M*M)); pred2=3*m0*m0+6*mJ*mJ+(a*a+2*b*b)*rho2
check('angular family quadratic trace',sp.expand(tr2-pred2)==0,str(pred2))
tr3=sp.expand(sp.trace(M**3)); angle=3*(a-b)**2*(a+2*b)*x*y*z
radial=3*m0**3+18*m0*mJ**2+6*mJ**3+(3*m0*(a*a+2*b*b)+-3*mJ*(2*a*b+b*b))*rho2
check('angular family cubic trace',sp.expand(tr3-angle-radial)==0,str(sp.factor(angle)))
for sub,label in [(a-b,'mu1=mu2'),(a+2*b,'mu1=-2mu2')]:
    value=b if label=='mu1=mu2' else -2*b
    check('flat characteristic coefficients '+label,sp.expand((tr3-radial).subs(a,value))==0 and sp.expand(tr2-pred2)==0,'trace1/2/3 determine characteristic polynomial')
q,S=sp.symbols('q S',positive=True)
check('definite-spectrum derivative identity',sp.simplify(sp.diff(-sp.sqrt(S+q*q),q,3)-3*S*q/(S+q*q)**sp.Rational(5,2))==0,'S>0 and q>0; negative definite has opposite sign')

# Construct the actual compressed four-link trace from the link multiplication
# rule A_ab=|ab><0|/sqrt(3), including both backward links and every color sum.
# Full register indices are base-10 four-link indices; zero rows are omitted
# only after constructing all nonzero matrix elements from those factors.
def flux(a,b): return 1+3*a+b
def full_index(state):
    out=0
    for v in state: out=10*out+v
    return out
entries={}
for a,b,c,d in itertools.product(range(3),repeat=4):
    ket=full_index((flux(a,b),flux(b,c),0,0))
    bra=full_index((0,0,flux(d,c),flux(a,d)))
    entries[ket,bra]=entries.get((ket,bra),Q(0))+Q(1,9)
active=sorted({i for edge in entries for i in edge}); index={v:i for i,v in enumerate(active)}
T=np.zeros((len(active),len(active)))
for (i,j),value in entries.items():T[index[i],index[j]]=float(value)
ceiling=np.linalg.eigvalsh((T+T.T)/6)[-1]
check('specified four-link plaquette ceiling',len(active)==54 and len(entries)==81 and abs(ceiling-1/18)<1e-14,
      {'full_register_dimension':10000,'nonzero_support':len(active),'oriented_entries':len(entries),'maximum':float(ceiling)})

# Charge-graph controls never interpreted as masses without a spectral bridge.
odd=[1,2,4,7]
counts=[]
for mask in range(1,128):
    generators=[s for s in range(1,8) if mask>>(s-1)&1]
    d={0:0}; front=[0]
    while front:
        new=[]
        for v in front:
            for s in generators:
                w=v^s
                if w not in d:d[w]=d[v]+1;new.append(w)
        front=new
    vals={d[c] for c in odd if c in d}
    if len({s.bit_count() for s in generators})==1:
        check('single Hamming-class insertion orders '+str(mask),vals<={1,3},{'generators':generators,'distances':[d.get(c) for c in odd]})
    if len(vals)>=3:counts.append(generators)
check('all 127 charge subsets finite census',len(counts)==12,{'three-order_sets':len(counts),'not_a_gap_census':True})

# Small eigenvalue has order five even though coefficient span stops at degree three.
ratios=[]
for eps in (.1,.05,.025):
    singular=np.linalg.svd([[eps,eps**3],[eps**3,0]],compute_uv=False)
    ratios.append(float(singular[-1]/eps**5))
check('higher-order singular-value counterexample',all(.999<r<1.001 for r in ratios),{'small_singular_over_eps5':ratios})
for c,yv,L in [(1.,2.,10.),(-.3,.5,4.),(.2,3.,.01)]:
    val=c*(-math.expm1(-yv*L))/yv
    check('specified irrelevant integral '+str((c,yv,L)),abs(val)<=abs(c)/yv,{'integral':val,'absolute_bound':abs(c)/yv})
for p in (0.,.1,.4,.75):
    eigen=1-2*p
    check('Pauli phase sign '+str(p),np.isclose(abs(eigen*np.exp(0j)),abs(eigen)) and (np.angle(complex(eigen))==0 if eigen>0 else np.angle(complex(eigen))==np.pi),{'eigenvalue':eigen,'phase':float(np.angle(complex(eigen)))})
for label,description in [
 ('per_element','Finite exact rational and symbolic identities, with stated algebraic hypotheses; no physical mass identification.'),
 ('per_site','Discrete fixtures and full 48-element image plus 127 charge subsets; no complete family of native models claimed.'),
 ('per_mode','Exact symbolic controls and numerical residual checks use declared tolerances; no exploratory scan replayed.'),
 ('per_block','Parameters are supplied model fixtures; empirical and coupling values in historical sources remain comparators.'),
 ('lattice_wide','Continuum, infinite-volume, all-order gap and nonperturbative extensions are not established by these controls.')]:
    print(label+': '+description,flush=True)
print(f'TOTAL: PASS={PASS} FAIL=0',flush=True)
signal.setitimer(signal.ITIMER_REAL,0)
