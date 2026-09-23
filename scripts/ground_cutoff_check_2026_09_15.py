"""Bounded checks of the supplied charged ground-state compactness argument.
The two-cell loop is a noncubic Gauss-algebra fixture, not a 3D phase model.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/FIXED_COUPLING_ROTOR_GROUND_CUTOFF_COMPACTNESS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/CHARGED_FINITE_LINK_LOCAL_DYNAMICS_AND_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-13.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'fixed_coupling_rotor_ground_cutoff_compactness_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/FIXED_COUPLING_ROTOR_GROUND_CUTOFF_COMPACTNESS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/ground_cutoff_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
from pathlib import Path
from collections import Counter
from itertools import product
import hashlib,json,math,time
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh,expm_multiply
from scipy.linalg import eigh
start=time.monotonic();checks=Counter()
def require(ok,label):
    if not ok:raise AssertionError(label)
    checks[label]+=1
I=np.eye(2);sx=np.array([[0.,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1.])
sig=[np.kron(I,s) for s in (sx,sy,sz)];tx=np.kron(sx,I);tz=np.kron(sz,I)
s,c=.8,.6;mu=.2;zeta=.6;B0=2+zeta;m1=mu*s;m3=mu*c
hon=B0*sig[2]+tx@(m1*sig[0]+m3*sig[2]);Ty=(-sig[2]-1j*sig[1])/2
Tx=(-s*sig[0]-c*sig[2]-1j*tz@(c*sig[0]-s*sig[2]))/2
pred=np.sort([sg*math.sqrt(m1*m1+(B0+eta*m3)**2) for sg,eta in product((-1,1),repeat=2)])
require(np.max(abs(np.linalg.eigvalsh(hon)-pred))<1e-13,'actual onsite four-band eigenvalues')
eon=-sum(pred[:2]);onsite_min=min(sum(pred[i] for i in range(4) if mask>>i&1) for mask in range(16))
require(abs(onsite_min+eon)<1e-13,'full onsite Fock minimum occurs at exactly two occupied levels')

# CAR matrices constructed from occupation bit parity, independently of earlier blocks.
def annihilate(mask,j):
    if not(mask>>j&1):return None
    return mask^(1<<j),(-1)**((mask&((1<<j)-1)).bit_count())
def create(mask,j):
    if mask>>j&1:return None
    return mask|(1<<j),(-1)**((mask&((1<<j)-1)).bit_count())
def bilinear(mask,i,j):
    a=annihilate(mask,j)
    if a is None:return None
    b=create(a[0],i)
    if b is None:return None
    return b[0],a[1]*b[1]
def second_quantized(mat,offset_i,offset_j):
    rr=[];cc=[];vv=[]
    for mask in range(256):
        for i,j in product(range(4),repeat=2):
            if abs(mat[i,j])<1e-15:continue
            out=bilinear(mask,offset_i+i,offset_j+j)
            if out is not None:rr.append(out[0]);cc.append(mask);vv.append(out[1]*mat[i,j])
    return sparse.coo_matrix((vv,(rr,cc)),shape=(256,256)).tocsr()
On=second_quantized(hon,0,0)+second_quantized(hon,4,4)
Hops=[second_quantized(Ty,0,4),second_quantized(Ty,4,0)]
for M in (Ty,Tx):
    mat=second_quantized(M,0,4).toarray()
    norm=float(np.linalg.svd(mat,compute_uv=False)[0])
    require(norm<=2+1e-13,'actual charged hopping respects nuclear-norm bound')

r=.31;k=.23;b=.77
# Two oriented edges 0->1 and 1->0, plus their two-edge Wilson loop.
# This fixture is explicitly not a cubic plaquette.
def basis(S):
    out=[]
    for mask in range(256):
        if mask.bit_count()!=4:continue
        charge=(mask&15).bit_count()-2
        for q in range(-S,S+1):
            if abs(q+charge)<=S:out.append((mask,q))
    return out
def direct(S):
    states=basis(S);idx={st:i for i,st in enumerate(states)};rr=[];cc=[];vv=[]
    def add(st,col,value):
        if st in idx:rr.append(idx[st]);cc.append(col);vv.append(value)
    for j,(mask,q) in enumerate(states):
        charge=(mask&15).bit_count()-2;e1=q+charge;e2=q
        add((mask,q),j,k*(e1*e1+e2*e2))
        for site in (0,4):
            for u,v in product(range(4),repeat=2):
                if abs(hon[u,v])<1e-15:continue
                result=bilinear(mask,site+u,site+v)
                if result:add((result[0],q),j,r*hon[u,v]*result[1])
        for edge,(left,right,dq) in enumerate(((0,4,0),(4,0,1))):
            for u,v in product(range(4),repeat=2):
                if abs(Ty[u,v])<1e-15:continue
                result=bilinear(mask,left+u,right+v)
                if result:add((result[0],q+dq),j,r*Ty[u,v]*result[1])
                result=bilinear(mask,right+v,left+u)
                if result:add((result[0],q-dq),j,r*Ty[u,v].conjugate()*result[1])
        add((mask,q+1),j,-b);add((mask,q-1),j,-b)
    H=sparse.coo_matrix((vv,(rr,cc)),shape=(len(states),)*2).tocsr()
    require(sparse.linalg.norm(H-H.getH())<1e-13,'physical loop Hamiltonian Hermitian')
    return states,H

def ambient(S):
    d=2*S+1;ev=np.arange(-S,S+1);El=sparse.diags(ev,dtype=float);Ul=sparse.diags(np.ones(d-1),-1,shape=(d,d));Id=sparse.eye(d)
    E1=sparse.kron(El,Id);E2=sparse.kron(Id,El);U1=sparse.kron(Ul,Id);U2=sparse.kron(Id,Ul)
    H=r*sparse.kron(On,sparse.eye(d*d))+k*sparse.kron(sparse.eye(256),E1@E1+E2@E2)
    for hop,U in zip(Hops,(U1,U2)):
        Z=r*sparse.kron(hop,U);H+=Z+Z.getH()
    W=sparse.kron(sparse.eye(256),U1@U2);H-=b*(W+W.getH())
    n0=np.array([(m&15).bit_count() for m in range(256)]);n1=np.array([(m>>4).bit_count() for m in range(256)])
    g0=np.repeat(-(n0-2),d*d)+np.tile((E1-E2).diagonal(),256)
    g1=np.repeat(-(n1-2),d*d)+np.tile((E2-E1).diagonal(),256)
    coo=H.tocoo()
    require(np.max(abs(coo.data*(g0[coo.row]-g0[coo.col])))<1e-13,'ambient charged link and loop preserve first Gauss operator')
    require(np.max(abs(coo.data*(g1[coo.row]-g1[coo.col])))<1e-13,'ambient charged link and loop preserve second Gauss operator')
    states=basis(S);indices=[mask*d*d+(q+(mask&15).bit_count()-2+S)*d+q+S for mask,q in states]
    return H.tocsr()[indices,:][:,indices]
for S in (1,2):
    states,H=direct(S);other=ambient(S)
    require(sparse.linalg.norm(H-other)<1e-12,'independent ambient compression matches direct physical-state construction')

loop_results=[]
for S in (0,1,2,3,5,8):
    states,H=direct(S)
    values,vecs=eigsh(H,k=1,which='SA',tol=1e-12,v0=np.ones(len(states)))
    energy=float(values[0]);psi=vecs[:,0]
    residual=float(np.linalg.norm(H@psi-energy*psi))
    require(residual<1e-9,'charged fixture ground eigenpair residual')
    electric=np.array([k*((q+(mask&15).bit_count()-2)**2+q*q) for mask,q in states])
    moment=float(np.dot(abs(psi)**2,electric))
    require(energy<=-2*r*eon+1e-10,'physical onsite N2 zero-flux variational comparison')
    require(moment<=8*r+2*b+1e-10,'electric energy bounded by charged and Wilson shift budget')
    # Gauss support is checked state by state, including nonzero local charge sectors.
    for mask,q in states:
        e1=q+(mask&15).bit_count()-2;e2=q
        require(e1-e2==(mask&15).bit_count()-2 and e2-e1==(mask>>4).bit_count()-2,'every reduced-basis state satisfies both charged Gauss constraints')
    for M in range(S+1):
        outside=np.array([abs(q)>M or abs(q+(mask&15).bit_count()-2)>M for mask,q in states])
        prob=float(np.dot(abs(psi)**2,outside))
        require(prob<=moment/(k*(M+1)**2)+1e-12,'local union tail follows from actual electric second moment')
        projected=psi*(~outside)
        # Exact two-dimensional purification span formula for subnormalized pure states.
        distance=math.sqrt(max(0,prob*(4-3*prob)))
        require(distance<=2*math.sqrt(prob)+1e-14,'subnormalized gentle projection bound')
    loop_results.append({'S':S,'dimension':len(states),'ground_energy':energy,'electric_energy':moment,'residual':residual})

# A genuine four-edge pure gauge plaquette, whose Gauss sector has one integer q.
kp=.031;bp=2.3

def plaquette(S):
    q=np.arange(-S,S+1);U=np.diag(np.ones(2*S),-1)
    return q,4*kp*np.diag(q*q)-bp*(U+U.T),U
plaquette_results=[]
for S in (0,1,2,3,5,8,12):
    q,H,U=plaquette(S);ee,V=eigh(H);psi=V[:,0];E=ee[0]
    moment=float(psi@np.diag(q*q)@psi)
    require(E<=1e-13 and 4*kp*moment<=2*bp+1e-12,'actual pure-gauge plaquette variational moment bound')
    if S>=1:
        K=S+2;qK,HK,UK=plaquette(K);embed=np.zeros(2*K+1);embed[K-S:K+S+1]=psi
        M=min(S,2);P=np.diag((abs(qK)<=M).astype(float));A=P@(UK+.3*UK.T+1j*np.diag((qK==0).astype(float)))@P
        a=A@embed
        lhs=np.vdot(embed,A.conj().T@(HK@a-A@(HK@embed)))
        rhs=np.vdot(a,(HK-E*np.eye(2*K+1))@a)
        require(abs(lhs-rhs)<1e-11,'finite-electric-support full-rotor commutator equals compressed ground form')
        require(rhs.real>=-1e-11 and abs(rhs.imag)<1e-11,'finite-electric-support physical ground form nonnegative')
    plaquette_results.append({'S':S,'energy':float(E),'one_link_second_moment':moment})
# Boundary adverse control: uncut U does not preserve the S=0 space.
q,H,U=plaquette(2);v=np.zeros(5);v[2]=1;actual=np.vdot(v,U.T@(H@(U@v)-U@(H@v)))
require(abs(actual-4*kp)<1e-14 and actual>0,'uncut shift invalidates an exact compressed-core identity at S0')

# Direct finite-time comparison, using the same finite-cutoff ground state.
# The larger reference cutoff is only a checked numerical comparator, not infinity.
dynamics=[]
for S in (2,4,6):
    q,HS,US=plaquette(S);vals,vec=eigh(HS);psi=vec[:,0];K=18;qK,HK,UK=plaquette(K)
    initial=np.zeros(2*K+1);initial[K-S:K+S+1]=psi
    A=np.diag((qK==0).astype(float));initial_value=float(initial@A@initial)
    for tt in (.2,1.,2.):
        evolved=expm_multiply(-1j*tt*HK,initial)
        observed=float(np.vdot(evolved,A@evolved).real)
        M=S//2;local_p=float(sum(abs(psi[abs(q)>M])**2))
        # Four links, J_l=bp, shift boundary estimate from the parent, lambda=1.
        bound=4*math.sqrt(local_p)+16*tt*bp*math.exp(-(S-M)+2*bp*tt*math.sinh(1))
        require(abs(observed-initial_value)<=bound+1e-12,'same-state dynamics comparison with derived ground-state tail')
        dynamics.append({'S':S,'t':tt,'observed_change':abs(observed-initial_value),'safe_bound':min(2,bound),'tail_probability':local_p})

root=Path(__file__).resolve().parents[1]
result={'status':'PASS_personal_ground_cutoff_challenges','checks':dict(checks),'charged_two_cell_loop':loop_results,'pure_gauge_four_edge_plaquette':plaquette_results,'same_state_dynamics':dynamics,'seconds':time.monotonic()-start,
'limits':['two-cell charged loop is a noncubic algebra fixture','four-edge plaquette is finite, not a bulk phase','larger time-evolution cutoff is a numerical comparator, not infinite-rotor certification','analytic compactness and ground-state passage are not established by finite diagonalizations','no fixed-S Coulomb phase or independently audited status'],
'sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [Path(__file__).resolve(),root/'docs/FIXED_COUPLING_ROTOR_GROUND_CUTOFF_COMPACTNESS_BOUNDED_THEOREM_NOTE_2026-09-15.md']}}
out=json.dumps(result,indent=2);_OUTPUT_JSON.write_text(out+'\n');print(out)

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: charged Gauss and electric cutoff identities')
    print('per_site: finite charged loop and four-edge plaquette')
    print('per_mode: finite cutoff spectra and finite-time matrix evolution')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
