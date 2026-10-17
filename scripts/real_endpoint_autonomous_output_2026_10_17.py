#!/usr/bin/env python3
"""Exact local and analytical-bound corroboration; not a Hamiltonian proof.

No import-time execution, runtime scientific-code imports, output-file writes,
network, matrix allocation above 4 by 4, or large-clock simulation. The fixed
parameters and manifest are runtime inputs. Manifest-bound historical evidence
is read only for integrity; no historical receipt is treated as a current run.
The external canonical envelope owns timeout/resource caps and source hashes.
"""
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from collections import deque

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/ARTIFACT_MANIFEST.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/FAILURES_AND_SCOPE.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/RESOURCE_PLAN.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/ROUTE.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/SOURCE_MANIFEST.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/THEOREM_NOTE_V1.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/check_route.py.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/launch_check.py.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/run_01/EXECUTION.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/run_01/PRELAUNCH.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/run_01/RESULT.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/run_01/stderr.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/historical_author/run_01/stdout.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/parameters.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/ROOT_QUALIFICATION.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/ROUTE_SOURCE_IDENTITY_CHECK.json',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/endpoint_spectral_check/REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/positive_jump_onset/CANDIDATE.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/positive_jump_onset/CORRECTED_V2.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/positive_jump_onset/SPECTRAL_SUM_ADDENDUM.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/positive_jump_onset/SPECTRAL_SUM_CORRECTED.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/positive_jump_onset/WEIGHTED_VARIATION_CANDIDATE.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/positive_jump_onset_check/ADDENDUM_REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/positive_jump_onset_check/REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/positive_jump_onset_check/WEIGHTED_REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/quantitative_programs/check_quantitative.py.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/quantitative_programs/launch_quantitative.py.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/quantitative_run/EXECUTION.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/quantitative_run/PRELAUNCH.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/quantitative_run/RESULT.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/quantitative_run/stderr.txt.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/quantitative_run/stdout.jsonl.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/real_two_port_structural_check/QUANTITATIVE.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/real_two_port_structural_check/QUANTITATIVE_PRECHECK.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/real_two_port_structural_check/RECEIPT.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/real_two_port_structural_check/REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/real_two_port_structural_check/SOURCE_PINS.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/tradeoff/CONJUGATE_PACKET_QUALIFICATION.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/tradeoff/ENDPOINT_COLUMN_QUALIFICATION.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/tradeoff/conjugate_packet_independent_check/REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/tradeoff/conjugate_packet_tradeoff_proposal/PROPOSAL.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/tradeoff/endpoint_column_independent_check/REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/tradeoff/weighted_core_derivative_proposal/PROPOSAL.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/source_premises/family.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/source_premises/family_acceptance.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/source_premises/family_qualification.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/source_premises/interval.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/source_premises/interval_acceptance.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/source_premises/interval_qualification.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/core_strip_contour/PROPOSAL.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/core_strip_contour/CORRECTED_V2.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/core_strip_contour/CORRECTIONS.json.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/core_strip_contour_independent_check/REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/core_strip_scalar_independent_check/REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/CORE_STRIP_QUALIFICATION.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/endpoint_weighted_profile/PROPOSAL.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/endpoint_weighted_profile_independent_check/REVIEW.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/WEIGHTED_STRIP_COMPOSITION.md.txt',
    'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/review_sources/weighted_strip/weighted_strip_composition_check/REVIEW.md.txt',
)
PARAMETERS_PATH = 'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/parameters.json'
MANIFEST_PATH = 'outputs/real_endpoint_autonomous_output_2026_10_17_inputs/ARTIFACT_MANIFEST.json'


def read_regular_input(repo, rel):
    """Read only a normalized regular file with no symlink below repo."""
    path = Path(rel)
    if (not isinstance(rel, str) or path.is_absolute() or not path.parts
            or '..' in path.parts or path.as_posix() != rel):
        raise ValueError('invalid input path: '+str(rel))
    current = repo
    for part in path.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError('symlink input or ancestor: '+rel)
    if not current.is_file():
        raise ValueError('input is not a regular file: '+rel)
    return current.read_bytes()


def verify_inputs(repo):
    """Integrity only, separate from mathematical checks and runner self hash."""
    manifest = json.loads(read_regular_input(repo, MANIFEST_PATH))
    rows = manifest['files']
    seen = set()
    for row in rows:
        rel = row['path']
        path = Path(rel)
        if (path.is_absolute() or '..' in path.parts or path.as_posix() != rel
                or rel in seen or rel not in AUDIT_INPUT_PATHS
                or rel == MANIFEST_PATH):
            raise ValueError('invalid/undeclared manifest path: '+str(rel))
        seen.add(rel)
        raw = read_regular_input(repo, rel)
        if len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise ValueError('integrity mismatch: '+rel)
    if seen != set(AUDIT_INPUT_PATHS) - {MANIFEST_PATH}:
        raise ValueError('manifest does not cover declared inputs exactly')
    return sorted(seen)


class C:
    def __init__(self, re=0, im=0): self.re, self.im = F(re), F(im)
    def __add__(self, other):
        if not isinstance(other,C): other=C(other)
        return C(self.re+other.re,self.im+other.im)
    __radd__=__add__
    def __neg__(self): return C(-self.re,-self.im)
    def __sub__(self,other): return self+-as_c(other)
    def __rsub__(self,other): return as_c(other)+-self
    def __mul__(self,other):
        other=as_c(other)
        return C(self.re*other.re-self.im*other.im,
                 self.re*other.im+self.im*other.re)
    __rmul__=__mul__
    def conj(self): return C(self.re,-self.im)
    def abs2(self): return self.re*self.re+self.im*self.im
    def __truediv__(self,other):
        other=as_c(other)
        return self*other.conj()*(1/other.abs2())
    def __rtruediv__(self,other): return as_c(other)/self
    def __pow__(self,n):
        if n<0:return (1/self)**(-n)
        ans=C(1)
        for _ in range(n):ans=ans*self
        return ans
    def __eq__(self,other):
        other=as_c(other)
        return self.re==other.re and self.im==other.im
    def __str__(self): return f'({self.re})+i*({self.im})'
def as_c(x): return x if isinstance(x,C) else C(x)
def inv2(m):
    det=m[0][0]*m[1][1]-m[0][1]*m[1][0]
    if not det.abs2() > 0:
        raise AssertionError("singular exact two-by-two matrix")
    return [[m[1][1]/det,-m[0][1]/det],[-m[1][0]/det,m[0][0]/det]]
def mv(m,v):return [sum((a*b for a,b in zip(row,v)),C()) for row in m]
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(2)),C())
                     for j in range(2)] for i in range(2)]


def check_arithmetic(params):
    rows = []
    def relation(name, a, b, op):
        ok = {'=': lambda: a == b, '<': lambda: a < b, '<=': lambda: a <= b}[op]()
        if not ok:
            raise AssertionError((name, str(a), op, str(b)))
        rows.append({'name':name, 'relation':op, 'lhs':str(a), 'rhs':str(b)})
        print('PASS arithmetic: '+name, flush=True)
    def eq(name,a,b): relation(name,a,b,'=')
    def lt(name,a,b): relation(name,a,b,'<')
    def le(name,a,b): relation(name,a,b,'<=')
    p={k:F(v) for k,v in params.items()}
    J,C0,S0,E0=p['J'],p['cos_k'],p['sin_k'],p['epsilon']
    sig=F(1,10**6); kap=F(1,10**12); r=F(1,7); g=F(9,50); v=F(1,40)
    d0=F(176,10**15); Fpos=20; N=44; ell=20; Dgeom=40
    u=-J/C0; tf=J*S0/C0; beta=J*((1+S0)/C0-1)
    w=J*(1+(1-S0)/C0); z=C(C0,S0); ii=C(0,1)
    eq('unit exact momentum',C0*C0+S0*S0,F(1))
    eq('exact E0',E0,2*J*(1-C0))
    lt('band sine lower',F(2,5),S0-sig)
    lt('band tangent half lower',F(1,5),(S0-sig)/(1+C0+sig))
    lt('filter norm',w,F(1,20));lt('filter norm exceeds J',J,w)
    lt('filter vacancy positive',0,beta);lt('filter t positive',0,tf)
    lt('filter t below J',tf,J)
    lt('emitter occupation positive',kap,E0);lt('endpoint occupation positive',kap,J)
    lt('velocity bound',v,2*J*(S0-sig))
    lt('velocity derivative bound',2*J/v,F(5,2))

    def rv(vv):return -(vv+J*z)/(vv+J/z)
    re,ro=rv(u-tf),rv(u+tf)
    eq('even filter phase',re,ii*z)
    eq('odd filter phase',ro,-ii*z)
    eq('filter reflection zero',(re+ro)/2,C())
    eq('relative free bond phase',(re-ro)/(2*z),ii)
    eq('free even phase',rv(-J),z);eq('free odd phase',rv(J),-z)
    eq('free endpoint convention',rv(F(0)),-z*z)

    # Direct two boundary-row solve, independent of the parity reduction.
    dd=u+J/z
    direct=mv(inv2([[dd,C(-tf)],[C(-tf),dd]]),[-(u+J*z),C(tf)])
    eq('direct matching reflection',direct[0],C())
    eq('direct matching transmission',direct[1],ii*z)
    # Lippmann-Schrödinger rank-one reflection coefficient at the same origin.
    A=-ii/(2*J*S0)
    V=[[C(u),C(J-tf)],[C(J-tf),C(u)]]
    Gfree=[[A,A*z],[A*z,A]]
    GV=mm(Gfree,V)
    Dfree=[[C(int(i==j))-GV[i][j] for j in range(2)] for i in range(2)]
    local=mv(inv2(Dfree),[C(1),z]);drive=mv(V,local)
    eq('Lippmann reflection at center',A*(drive[0]+z*drive[1]),C())
    eq('Lippmann transmission relative free bond',1+A*(drive[0]+drive[1]/z),ii)

    # Full-qubit PSD identities at both hopping signs, using a rank-one Gram.
    for sign in [-1,1]:
        vec=[F(0),F(1),F(sign),F(0)]
        gram=[[vec[i]*vec[j]+(2 if i==j==3 else 0) for j in range(4)] for i in range(4)]
        target=[[F(0) for _ in range(4)] for _ in range(4)]
        target[1][1]=target[2][2]=1;target[3][3]=2
        target[1][2]=target[2][1]=sign
        eq('local PSD Gram sign '+str(sign), gram, target)


    lt('scalar opposite-arm error',5*sig+17*sig/(1-5*sig),23*sig)
    lt('closed filter inverse margin',((1+r)/g+211*r**38)/20,F(1,3))
    lt('open rank-one inverse ceiling',10+400/(1-5*sig),500)
    lt('full Schur Neumann margin',500*338*r**38,F(1,2))
    aa=F(45,2)*r**19
    lt('full filter inverse ceiling',1000*(1+aa)**2+F(3,2),2000)
    lt('open local difference coefficient',1000*(507000*r+F(765,2)),10**8)
    lt('open local difference less than one',10**8*r**37,1)
    lt('closed local coefficient',F(51,2)+F(67545,2)*r,5000)
    lt('open reflection feedback coefficient',6*10**8+F(211,20)*5000,10**9)
    ecl=10**9*r**37
    lt('all closed channels reflection error',ecl,F(1,10**20))
    lt('filter exterior C norm squared',2*(40+206)**2,350**2)
    lt('modified exterior kernel ceiling',206+350**2*F(1,20)*2000,13*10**6)
    eta=12*sig;delta_tau=d0+714*sig
    lt('two-port reflection', (23*sig+ecl)/2,eta)
    lt('two-port transmission error',d0+702*sig+(23*sig+ecl)/2,delta_tau)
    K=13*10**6;dx=3*K*r**44
    lt('terminated-port full closed correction',dx,F(1,10**28))
    lt('unperturbed end factor',40*(1+eta),41)
    lt('terminated inverse Neumann',21/(1-21*dx),22)
    lip=1+22*41+41*22*21*41+41*21
    lt('terminated matrix Lipschitz',lip,10**6)
    lt('end Green error',lip*dx,F(1,10**22))
    lt('end matrix norm',1/J*(1+eta)/(1-eta)+F(1,10**22),35)
    zlip=22*21*41+21
    lt('outgoing row error',4*K*r**44+40*zlip*dx,F(1,10**21))
    eG=F(1,10**22);eL=F(1,10**21);eD=F(1,40000)
    lt('all emitter complementary inverse',1/(g-35*kap**2),6)
    lt('emitter denominator correction',2*eta/(1-eta)+(eG+6*kap**2*eG**2)*J/(S0-sig),eD)
    lt('emitter imaginary lower constant',12,(1-eD)*(S0-sig)/J)
    lt('all emitter inverse multiplied by kappa squared',6*kap**2+(1+6*kap**2*eG)**2/12,F(1,10))
    eF=F(752,10**6)
    profile=(delta_tau+eta+eD+eta*eD)/((1-eta)*(1-eD))+2*J*eL/(1-eD)
    lt('complete outgoing profile relative error',profile,eF)
    tail=kap/(v*sig);massdef=tail**2
    eq('variance tail amplitude',tail,F(4,10**5))
    eq('reference spectral mass deficit',massdef,F(16,10**10))
    lt('normalization error bound',massdef,F(2,10**9))
    lt('root two bound squared',2,F(283,200)**2)
    col=eF+tail+F(2,10**9)
    lt('complete old/reference seed packet cost',F(283,200)*col,F(1121,10**6))

    lt('base kernel bound',40+206,250)
    lt('all filter finite-coordinate blocks',250+2*250**2*F(1,20)*2000,13*10**6)
    lt('port transformed blocks',2*13*10**6,3*10**7)
    lt('terminated finite-coordinate blocks',3*10**7+22*(3*10**7)**2,2*10**16)
    lt('installed finite-coordinate blocks',2*10**16+kap**2*(2*10**16)**2*10**23,5*10**31)
    lt('installed core matching inverse',113*5*10**31,6*10**33)
    lt('matching derivative',3*J,F(1,10))
    lt('core inverse derivative',(6*10**33)**2*F(1,10),4*10**66)
    lt('stationary core amplitude',2*J*6*10**33,4*10**32)
    lt('stationary core derivative',2*J*(4*10**66+6*10**33),3*10**65)
    lt('closed-tail ratio simple majorant',r*r/(1-r*r),F(1,6)**2)
    lt('localized core and tail',4*10**32+2+F(1,6)*4*10**32,10**33)
    # sqrt((1+r²)/(1-r²)^3)<2, a loose derivative-tail majorant.
    lt('tail derivative sum majorant squared',(1+r*r)/(1-r*r)**3,4)
    lt('localized derivative',6*10**65+F(1,6)*3*10**65+F(1,12)*4*10**32,10**66)
    lt('reference positive normalization',F(99,100)**2,1-massdef)
    lt('reference f sup',2*J/(kap*2*F(99,100)),4*10**10)
    lt('Dref logarithmic derivative',(2*J+kap**2/J)/(12*kap**2),6*10**21)
    lt('reference derivative multiplier',F(5,2)+(ell+1+2*N+4)+6*10**21,7*10**21)
    lt('reference f derivative sup',4*10**10*7*10**21,3*10**32)
    lt('f L1 squared',2*sig,F(1,500)**2)
    lt('endpoint inclusive variation',8*10**10+2*sig*3*10**32,7*10**26)
    lt('incoming coefficient variation',7*10**26+F(1,500)*3*10**65,7*10**62)
    lt('localized IBP column budget',7*10**62*10**33+F(1,500)*10**66+F(1,200)*10**33,8*10**95)
    lt('localized two-column aggregation',F(3,2)*8*10**95,2*10**96)
    T=10**136;M=50*T
    lt('time denominator lower squared',(2*10**67)**2,3*v*T)
    esc=(8*10**62+8*10**26)/F(2*10**67)+F(2*10**96)/(2*v*T)
    lt('uniform all-future escape at T',esc,F(1,10**4))
    lt('infinite complete ceiling',F(1121,10**6)+F(1,10**4),F(13,10**4))
    Vmax=2*p['lambdaA']+p['mu0']
    lt('one-head spectral radius',F(19,2)+2*J+w+2*J+kap+Vmax,18)
    lt('finite horizon exponent margin',18*(2*T)*F(6,5)+9,M+23)
    lt('exponential tail constant',F(32,5)*F(3,8)**9,F(1,1000))
    lt('finite complete ceiling',F(1121,10**6)+F(1,10**4)+F(1,1000),F(23,10**4))
    lt('filter incident load',2*J+2*tf+beta,F(12,100))
    lt('junction incident load sqrt2 ceiling',(1+3*F(10,7))*J,F(16,100))
    lt('emitter load',E0+kap,F(6,1000))
    lt('input endpoint load',3*J+kap,F(91,1000))
    lt('old1 added load',2*p['gA'],2);lt('old2 added load',2*p['gB'],2)

    # A bounded exact embedding check. No dynamics or finite large chain is run.
    Msmall=4
    a0=[(n,1,1) for n in range(Dgeom-3)]+[
     (Dgeom-4,1,2),(Dgeom-4,1,3),(Dgeom-3,1,3),(Dgeom-2,1,3),
     (Dgeom-2,1,2),(Dgeom-2,1,1),(Dgeom-1,1,1),(Dgeom,1,1)]
    a1=[(n,1,-1) for n in range(Dgeom+2)]+[
     (Dgeom+1,2,-1),(Dgeom+1,2,0),(Dgeom+1,2,1)]
    out=[(Dgeom+1+m,1,1) for m in range(Msmall+1)] # includes first omitted site
    inp=[(Dgeom,2+m,1) for m in range(ell+1)]
    emit=(Dgeom,2+ell+1,1)
    olds=[(0,0,0),(1,0,0),(0,1,0),(1,1,0)]
    eq('arm0 sites',len(a0),N+1);eq('arm1 sites',len(a1),N+1)
    head=a0+a1+out+inp+[emit]
    eq('distinct head and internal sites',len(set(head+olds)),len(head)+4)
    edges=[]
    for path in [a0,a1,out,inp]:edges.extend(zip(path,path[1:]))
    edges.extend((aa,bb) for aa in [a0[-1],a1[-1]] for bb in [out[0],inp[0]])
    edges.append((inp[-1],emit))
    internal=[(olds[0],olds[1]),(olds[0],olds[2]),(olds[1],olds[3]),(olds[2],olds[3])]
    internal.extend([(olds[2],a0[0]),(olds[2],a1[0]),(olds[3],a0[1]),(olds[3],a1[1])])
    eq('geometry NN edges', all(sum(abs(x-y) for x,y in zip(a,b))==1 for a,b in edges+internal), True)
    adj={x:[] for x in head}
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    dist={emit:0};q=deque([emit])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if b not in dist:dist[b]=dist[a]+1;q.append(b)
    eq('first omitted output distance',dist[out[-1]],Msmall+23)
    eq('finite head sites count',len(head)-1,Msmall+112)
    eq('finite total qubits count',len(head)-1+4,Msmall+116)
    eq('finite head edges count',len(edges)-1,Msmall+112)
    lt('executed graph vertex cap',len(head)+4,256)


    # Additional scalar substitutions from CORRECTED_V2 and SPECTRAL_SUM_CORRECTED.
    # These assert arithmetic under the named analytical hypotheses; the jump,
    # spectral projection inequality and reciprocal identity are NOT computed here.
    E2=F(61,1000); derivative=F(1,10); core_rank=113*8
    x_bound=10**17; xp_bound=7*10**49
    lt('positive-jump Eprime ceiling',2*J,E2)
    lt('positive-jump finite-core trace substitution',2*E2*core_rank*5*10**31,x_bound**2)
    lt('positive-jump differentiated matching substitution',6*10**33*(E2+derivative*x_bound),xp_bound)
    Rp=2*E2/v+derivative*x_bound**2/v
    lt('reciprocal reflection derivative substitution',Rp,5*10**34)
    lt('closed-tail derivative multiplier squared',F(1,24)**2*(1+r*r)/(1-r*r)**3,F(1,20)**2)
    loc0=2*10**17;loc1=2*10**50
    lt('positive-jump localized norm',x_bound+2+x_bound/F(6),loc0)
    lt('positive-jump localized derivative',xp_bound+5*10**34+xp_bound/F(6)+x_bound/F(20),loc1)
    fmax=4*10**10;fpmax=3*10**32;fL1=F(1,500);fvar=7*10**26
    lt('positive-jump incoming variation',fvar+fL1*5*10**34,2*10**32)
    # Do not drop the fourth term: derivative of 1/R in a=omega*f/R.
    point_terms=[2*fmax*loc0,2*sig*fpmax*loc0,fL1*loc1,
                 fL1*loc0*5*10**34,fL1*loc0*E2/v]
    eq('corrected pointwise derivative term expansion',point_terms,
       [16*10**27,12*10**43,4*10**47,2*10**49,976*10**12])
    lt('corrected pointwise localized variation',sum(point_terms),21*10**48)
    lt('corrected pointwise aggregated ceiling',21*10**48,10**50)
    Tpoint=10**78
    lt('corrected pointwise denominator squared',(2*10**38)**2,3*v*Tpoint)
    point_escape=F(4*10**32+8*10**26,2*10**38)+F(10**50)/(v*Tpoint)
    lt('corrected pointwise escape at historical intermediate onset',point_escape,F(3,10**6))
    # pi bounds are analytical inputs: 3 < pi < 10/3, not floating approximations.
    pi_upper=F(10,3)
    spectral_mass=2*pi_upper*core_rank
    weighted=2*(E2/v)*fL1+(derivative/v)*fmax*spectral_mass
    lt('finite spectral-mass weighted reflection derivative',weighted,10**15)
    lt('finite spectral-mass incoming variation',fvar+10**15,8*10**26)
    lt('finite spectral-mass incoming numerator',8*10**26+(E2/v)*fL1,9*10**26)
    integrated_terms=[2*fmax*loc0,2*sig*fpmax*loc0,fL1*loc1,
                      loc0*10**15,fL1*loc0*E2/v]
    eq('integrated phase derivative term expansion',integrated_terms,
       [16*10**27,12*10**43,4*10**47,2*10**32,976*10**12])
    lt('integrated localized variation',sum(integrated_terms),5*10**47)
    # sqrt(2) columns / sqrt(2pi) < 1; using pi>3 is more than enough.
    lt('integrated localized operator ceiling',5*10**47,10**49)
    Tnew=10**66;Mnew=50*Tnew
    lt('refined onset denominator squared',(2*10**32)**2,3*v*Tnew)
    escape_new=F(9*10**26+8*10**26,2*10**32)+F(10**49)/(v*Tnew)
    lt('refined onset escape arithmetic',escape_new,F(9,10**6))
    lt('refined onset infinite complete ceiling',F(1121,10**6)+escape_new,F(13,10**4))
    lt('refined onset finite exponent margin',18*(2*Tnew)*F(6,5)+9,Mnew+23)
    lt('refined onset finite complete ceiling',F(1121,10**6)+escape_new+F(1,1000),F(23,10**4))
    # Weighted variation refinement; all integrals below are analytical bounds,
    # not quadrature or computed spectral densities. Same supplied apparatus.
    lt('weighted J lower',F(3,100),J)
    lt('weighted J upper',J,F(31,1000))
    alpha=kap**2/J
    lt('weighted monotone real denominator derivative',F(24,1000),v-alpha)
    lt('weighted denominator derivative upper',E2+alpha,F(62,1000))
    lt('weighted imaginary denominator lower coefficient',12,F(2,5)/J)
    # sqrt(2pi)>2 and p0>=1-massdef. Squaring positive factors checks A<17*kappa.
    lt('weighted reference amplitude coefficient squared',1,(2*J*17)**2*(1-massdef))
    phase_derivative=ell+1+2*N+4
    eq('weighted reference phase derivative',phase_derivative,113)
    derivative_regular=(E2/v+phase_derivative)*fL1
    lt('weighted regular reference variation',derivative_regular,F(232,1000))
    # X'>.024, Y>12*kappa^2; monotone X substitution and pi<4 give this ceiling.
    integral_ceiling=F(4)/(F(24,1000)*12*kap**2)
    derivative_resonant=17*kap*E2*F(62,1000)*integral_ceiling
    lt('weighted resonant reference variation',derivative_resonant,1/kap)
    weighted_fvar=2*10**12
    lt('weighted endpoint inclusive reference variation',F(232,1000)+1/kap+2*fmax,weighted_fvar)
    lt('weighted incoming variation',weighted_fvar+10**15,2*10**15)
    lt('weighted incoming scalar numerator',2*10**15+(E2/v)*fL1,3*10**15)
    lt('weighted outgoing scalar numerator',weighted_fvar+(E2/v)*fL1,3*10**12)
    # ||f||_2=1 and integral ||x||^2 <=2*pi*904; pi<4 gives 7232.
    spectral_mass_loose=2*4*core_rank
    lt('weighted Cauchy Schwarz core bound squared',spectral_mass_loose,86**2)
    weighted_xprime=6*10**33*(E2*fL1+derivative*86)
    lt('weighted matching derivative integral',weighted_xprime,52*10**33)
    weighted_cprime=F(7,6)*52*10**33+10**15+F(86,20)
    lt('weighted closed-tail localized derivative integral',weighted_cprime,7*10**34)
    # Four complete terms: f variation/endpoints, C derivative, 1/R derivative,
    # and curvature from differentiating 1/E'. Keep each term explicitly.
    weighted_terms=[loc0*weighted_fvar,7*10**34,loc0*10**15,(E2/v)*loc0*fL1]
    eq('weighted full localized term expansion',weighted_terms,
       [4*10**29,7*10**34,2*10**32,976*10**12])
    lt('weighted full localized variation',sum(weighted_terms),8*10**34)
    lt('weighted localized aggregated ceiling',8*10**34,10**35)
    Tweighted=10**42;Mweighted=50*Tweighted
    lt('weighted onset denominator squared',(2*10**20)**2,3*v*Tweighted)
    weighted_escape=F(3*10**15+3*10**12,2*10**20)+F(10**35)/(v*Tweighted)
    lt('weighted onset escape arithmetic',weighted_escape,F(2,10**5))
    lt('weighted onset infinite complete ceiling',F(1121,10**6)+weighted_escape,F(13,10**4))
    lt('weighted onset finite exponent margin',18*(2*Tweighted)*F(6,5)+9,Mweighted+23)
    lt('weighted onset finite complete ceiling',F(1121,10**6)+weighted_escape+F(1,1000),F(23,10**4))
    # Separately reviewed endpoint-column refinement and conjugate-packet tradeoff.
    # These scalar substitutions do not prove contour deformation or Schur identities.
    lt('endpoint selected column',3*10**7*(1+22*41),3*10**10)
    endpoint_col_sq=112*(3*10**10)**2
    emitter_update_norm=112*2*10**16+(1+kap**2*endpoint_col_sq)*10**23
    lt('endpoint full core inverse',emitter_update_norm,12*10**22)
    lt('endpoint background diagonal',2*10**16+kap**2*(3*10**10)**2*10**23,10**20)
    lt('endpoint jump trace',2*E2*8*(112*10**20+10**23),(4*10**11)**2)
    lt('endpoint complete localized norm',F(7,6)*4*10**11+2,5*10**11)
    lt('endpoint weighted x derivative',12*10**22*(E2*fL1+derivative*86),11*10**23)
    lt('endpoint weighted C derivative',F(7,6)*11*10**23+10**15+F(86,20),13*10**23)
    # A nontrivial exact algebra fixture for F=R conjugate(F); not spectral data.
    fixture_F=C(3,4);fixture_g=C(2,1);fixture_R=fixture_F/fixture_F.conj()
    fixture_e=fixture_F-fixture_g
    eq('conjugate packet outgoing identity fixture',fixture_R*fixture_g.conj()-fixture_g,
       fixture_e-fixture_R*fixture_e.conj())
    outgoing_tradeoff=2*eF
    eq('conjugate packet outgoing ceiling',outgoing_tradeoff,F(1504,10**6))
    strip_h=sig/2
    le('contour strip range',2*strip_h,1)
    lt('contour complex velocity ceiling',2*J*(1+strip_h**2),F(62,1000))
    lt('contour vertical denominator floor',F(24,1000)*sig,
       v*sig-E2*strip_h**2-kap**2/J)
    lt('contour coefficient ceiling',17*F(62,1000)/F(24,1000),44)
    lt('contour bottom squared bound',(88*kap)**2/strip_h,F(13,10**8)**2)
    localized_tradeoff_terms=[5*10**11*weighted_fvar,13*10**23,(E2/v)*5*10**11*fL1]
    eq('conjugate localized complete expansion',localized_tradeoff_terms,
       [10**24,13*10**23,244*10**7])
    lt('conjugate localized numerator',sum(localized_tradeoff_terms),24*10**23)
    lt('conjugate localized Fourier aggregation squared',(24*10**23)**2,3*(15*10**23)**2)
    Ttradeoff=10**30;Mtradeoff=50*Ttradeoff
    lt('tradeoff time denominator squared',(2*10**14)**2,3*v*Ttradeoff)
    contour_incoming=F(13,10**8)+88*kap/(sig*2*10**14)
    lt('tradeoff incoming ceiling',contour_incoming,F(2,10**7))
    # Exact positive-normalization fixture p=4/5,q=3/5: 1-p=q^2/(1+p).
    fixture_p=F(4,5);fixture_q=F(3,5)
    eq('positive normalization squared identity fixture',1-fixture_p,fixture_q**2/(1+fixture_p))
    le('positive normalization squared cost fixture',1-fixture_p,fixture_q**2)
    target_tail=F(3*10**12,2*10**14)
    lt('tradeoff target nonzero',target_tail,1)
    le('tradeoff normalization cost',target_tail**2,F(225,10**6))
    le('tradeoff localized ceiling',F(15*10**23)/(v*Ttradeoff),F(60,10**6))
    tradeoff_total=F(1121,10**6)+outgoing_tradeoff+F(225,10**6)+F(60,10**6)+F(2,10**7)
    eq('tradeoff five-term budget',tradeoff_total,F(29102,10**7))
    lt('tradeoff infinite complete ceiling',tradeoff_total,F(3,1000))
    lt('tradeoff finite exponent margin',18*(2*Ttradeoff)*F(6,5)+9,Mtradeoff+23)
    lt('tradeoff finite complete ceiling',tradeoff_total+F(1,1000),F(4,1000))
    # Thin-strip and weighted-profile constants only; analyticity is an analytical proof.
    thin_h=F(1,10**23);Tthin=10**27;Mthin=50*Tthin
    lt('thin closed spectral gap',F(17,100),F('2.186826508897014')-2-F('0.0061'))
    lt('thin energy band ceiling',E0+F('.061')*sig,F('.0061'))
    lt('thin closed resolvent coefficient',J/(F('.17')*(F('.17')-F('.062')*thin_h)),2)
    lt('thin closed root continuation',r+2*F('.062')*thin_h,F(1,6))
    lt('thin closed self energy variation',J*2*F('.062'),F('.004'))
    lt('thin physical matrix variation',F('.062')+F('.031'),F('.1'))
    thin_neumann=12*10**22*F('.1')*thin_h
    eq('thin Neumann product',thin_neumann,F('.12'))
    lt('thin continued inverse',F(12*10**22)/(1-thin_neumann),14*10**22)
    lt('thin incoming core column',14*10**22*F('.062'),9*10**21)
    lt('thin closed tail squared',(F(1,6)**2)/(1-F(1,6)**2),F(1,5)**2)
    lt('thin complete localized vector',3*9*10**21+4,4*10**22)
    lt('thin outgoing imaginary floor',12*kap**2,F('.4')*(32*kap**2-F('.061')*thin_h))
    lt('thin conjugate coefficient',17*kap*F('.062')/(12*kap**2),10**11)
    lt('thin target coefficient',2*17*kap*F('.062')/(12*kap**2),2*10**11)
    lt('thin outgoing side floor',F('.024')*sig,v*sig-F('.061')*thin_h**2-2*alpha)
    eq('thin exponential argument',v*Tthin*thin_h,250)
    lt('thin integer exponential majorant',10**75,2**250)
    lt('thin target bottom squared prefactor',(2*10**11*sig)**2/thin_h,(10**17)**2)
    lt('thin localized aggregate',F(3,2)*(F(4*10**27,10**75)+F(176*10**16)/(v*Tthin)),F(3,10**7))
    lt('thin negative tail side denominator',(10**13)**2,6*(v*Tthin-113))
    thin_tail=F(10**17,10**75)+88*kap/(sig*10**13)
    lt('thin negative tail ceiling',thin_tail,F(1,10**16))
    lt('thin incoming denominator',(8*10**12)**2,3*v*Tthin)
    lt('thin incoming total',F(13,10**8)+88*kap/(sig*8*10**12),F(2,10**7))
    rmax=F(12,10**6);dmax=F(25,10**6)
    lt('profile weighted denominator floor',F('.99996'),(1-rmax)*(1-dmax))
    lt('profile weighted denominator slope',23/(1-rmax),24)
    lt('profile weighted denominator intercept',F(1,10**20)/(1-rmax)+F(1,10**23),F(2,10**20))
    lt('profile weighted complex slope',(749+F('.000288'))/F('.99996'),750)
    point_intercept=(d0+F(3,10**20)+F(24,10**26))/F('.99996')+F(32,10**24)
    lt('profile weighted complex intercept',point_intercept,F(2,10**13))
    lt('profile weighted moment squared',kap**2/((1-massdef)*v**2),F(41,10**12)**2)
    delta_weighted=F(2,10**13)+750*F(41,10**12)
    lt('profile weighted L2 mismatch',delta_weighted,F(31,10**9))
    weighted_preparation=F(1415,1000)*(F(4,10**5)+F(31,10**9)+F(16,10**10))
    lt('profile weighted preparation',weighted_preparation,F(567,10**7))
    weighted_static=F(567,10**7)+2*F(31,10**9)
    lt('profile weighted static',weighted_static,F(568,10**7))
    thin_composed=F(568,10**7)+F(3,10**7)+F(2,10**7)+F(1,10**32)
    lt('weighted strip complete infinite',thin_composed,F(58,10**6))
    lt('weighted strip finite exponent',18*2*Tthin*F(6,5)+9,Mthin+23)
    lt('weighted strip complete finite',thin_composed+F(1,1000),F(1058,10**6))
    return {'checks': rows,
            'historical_onsets': {'original':str(T), 'corrected_pointwise':str(Tpoint),
                                 'integrated_spectral_mass':str(Tnew)},
            'thin_weighted_onset':str(Tthin), 'thin_weighted_output_sites':str(Mthin),
            'thin_weighted_infinite_ceiling':'.000058', 'thin_weighted_finite_ceiling':'.001058',
            'tradeoff_onset':str(Ttradeoff), 'tradeoff_output_sites':str(Mtradeoff),
            'tradeoff_infinite_ceiling':'.003', 'tradeoff_finite_ceiling':'.004',
            'weighted_onset': str(Tweighted), 'weighted_output_sites': str(Mweighted),
            'executed_geometry_vertices':len(head)+4, 'dense_dimension_max':4,
            'large_matching_matrices_executed':False}



def main():
    repo = Path(__file__).resolve().parents[1]
    print('SCOPE: exact local finite algebra and conditional analytical-bound arithmetic.')
    print('BOUNDARY: no spectrum, dynamics, 904/1808 matrix, native realization, or independent proof computed.')
    print('BOUNDARY: residual spectral mass remains paid; finite guarantee is only [T,2T].')
    print('BOUNDARY: no general impossibility claim or negative-packet verdict is tested.')
    try:
        inputs = verify_inputs(repo)
        print('PASS integrity: declared package files match manifest (not a mathematical check).')
        params=json.loads(read_regular_input(repo, PARAMETERS_PATH))['exact_parameters']
        result=check_arithmetic(params)
        result['runtime_reads']={'scientific_data':[PARAMETERS_PATH],
            'package_integrity':[MANIFEST_PATH]+inputs, 'self_integrity':[]}
        result['scope']='Scalar corroboration of conditional bounds; no proof or audit status.'
        print(json.dumps(result, sort_keys=True, indent=2))
    except Exception as exc:
        print('TOTAL FAIL: '+str(exc), flush=True)
        return 1
    print('TOTAL PASS: declared integrity and scoped arithmetic checks only.', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
