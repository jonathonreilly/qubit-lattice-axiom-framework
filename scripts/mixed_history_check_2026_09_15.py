"""Structural native census and small CAR controls, not a native sixth-order solve."""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/NATIVE_MIXED_SIXTH_ORDER_COEFFICIENT_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md', 'docs/NATIVE_UNIFORM_QUASILOCAL_STAR_VERTEX_NOTE_2026-09-09.md', 'docs/NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md', 'docs/NATIVE_FULL_STAR_INFRARED_RESPONSE_NOTE_2026-09-09.md', 'docs/NATIVE_POSITIVE_WARD_SCALAR_BOUNDED_THEOREM_NOTE_2026-09-13.md', 'docs/NATIVE_STAR_INFRARED_SPECTRAL_DOMINANCE_BOUNDED_THEOREM_NOTE_2026-09-13.md', 'docs/NATIVE_WEAK_ELECTRIC_SPECTATOR_GAP_NOTE_2026-09-08.md', 'docs/NATIVE_THIRD_ORDER_STAR_VERTEX_NOTE_2026-09-08.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'native_mixed_sixth_order_coefficient_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/NATIVE_MIXED_SIXTH_ORDER_COEFFICIENT_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/mixed_history_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import hashlib,json,math,time
import numpy as np
from scipy.linalg import expm

start=time.monotonic();checks=Counter()
def require(ok,label):
    if not ok:raise AssertionError(label)
    checks[label]+=1
def shift(r,a,n):
    s=list(r);s[a]+=n;return tuple(s)
def star(v):return [(v,a) for a in range(3)]+[(shift(v,a,-1),a) for a in range(3)]
def edge_faces(e):
    r,a=e
    return {(r,*sorted((a,b))) for b in range(3) if b!=a}|{(shift(r,b,-1),*sorted((a,b))) for b in range(3) if b!=a}
def faces(edges):
    out=set()
    for e in edges:out.symmetric_difference_update(edge_faces(e))
    return frozenset(out)
def partitions():
    out=[]
    for a in combinations(range(6),2):
        rest=set(range(6))-set(a)
        for b in combinations(sorted(rest),2):
            c=tuple(sorted(rest-set(b)));masks=[sum(1<<j for j in q) for q in [a,b,c]]
            out.append((0,masks[0],masks[0]|masks[1],63))
    return out
parts=partitions();require(len(parts)==90 and len(set(parts))==90,'all ordered star pair partitions are distinct')
interleavings=[tuple(0 if j in positions else 1 for j in range(6)) for positions in combinations(range(6),3)]
census=[]
for offset in [(4,0,0),(2,2,0),(1,1,2),(0,0,5)]:
    stars=[star((0,0,0)),star(offset)]
    fs=[{mask:faces([e for j,e in enumerate(st) if mask>>j&1]) for mask in range(64)} for st in stars]
    require(not set().union(*fs[0].values()).intersection(set().union(*fs[1].values())),'separated star plaquette supports are disjoint')
    for f in fs:
        require(len(f[0])==0 and len(f[63])==0,'complete native star is a flux-preserving gauge cut')
        require(all(len(f[m]) in (6,8) for m in range(64) if m.bit_count() in (2,4)),'every two- or four-edge partial star has six or eight defective faces')
    counts=Counter();prefix_counts=Counter();minmixed=100
    for pa,pb in product(parts,repeat=2):
        for word in interleavings:
            progress=[0,0];zero=[];minfaces=100
            for step,side in enumerate(word[:5],1):
                progress[side]+=1
                defect=fs[0][pa[progress[0]]]^fs[1][pb[progress[1]]]
                n=len(defect);prefix_counts[n]+=1;minfaces=min(minfaces,n)
                if n==0:zero.append(step)
            single=word[:3] in ((0,0,0),(1,1,1))
            if single:
                if zero!=[3]:raise AssertionError(('singleton middle classification',word,zero))
                counts['singleton']+=1
            else:
                if zero or minfaces<6:raise AssertionError(('mixed history loses wrong-flux gap',word,zero,minfaces))
                counts['mixed']+=1;minmixed=min(minmixed,minfaces)
    require(counts==Counter(singleton=16200,mixed=145800),'complete native separated-center history census')
    require(minmixed==6,'actual mixed prefixes attain six-face minimum')
    census.append({'offset':offset,'histories':dict(counts),'proper_prefix_defect_counts':dict(prefix_counts),'minimum_mixed_defective_faces':minmixed})

# Literal ordered CAR matrices, using occupancy bits rather than tensor templates.
def car(n):
    dim=1<<n;aa=[]
    for j in range(n):
        a=np.zeros((dim,dim),complex)
        for b in range(dim):
            if b>>j&1:a[b^(1<<j),b]=(-1)**((b&((1<<j)-1)).bit_count())
        aa.append(a)
    gam=[]
    for a in aa:gam.extend([a+a.conj().T,1j*(a.conj().T-a)])
    return aa,gam
aa,gam=car(4);eye=np.eye(16)
for i,j in product(range(8),repeat=2):
    require(np.linalg.norm(gam[i]@gam[j]+gam[j]@gam[i]-2*(i==j)*eye)<1e-14,'literal CAR convention')

def quadratic(K):return sum(.25j*K[i,j]*(gam[i]@gam[j]) for i,j in product(range(8),repeat=2))
def norm(A):return float(np.linalg.norm(A,2))
K=np.zeros((8,8))
for j in range(7):K[j,j+1]=.7+.11*j;K[j+1,j]=-K[j,j+1]
Hraw=quadratic(K);energy,U=np.linalg.eigh(Hraw);H=Hraw-energy[0]*eye;vac=U[:,0]
Vs=[np.zeros((16,16)),.23j*gam[0]@gam[1],-.19j*gam[0]@gam[2],.31j*gam[0]@gam[1]]
Ws=[np.zeros((16,16)),.17j*gam[7]@gam[6],.13j*gam[7]@gam[5],-.29j*gam[7]@gam[6]]
progress=[(1,0),(1,1),(2,1),(2,2),(3,2)]
times=[.13,-.07,.19,.11,-.17]
def cocycle(H,B,t):return expm(-1j*t*(H+B))@expm(1j*t*H)
def tau(H,A,t):return expm(-1j*t*H)@A@expm(1j*t*H)
def word_control(H,vac):
    direct=vac.copy()
    for (a,b),t in zip(progress,times):direct=expm(-1j*t*(H+Vs[a]+Ws[b]))@direct
    formed=eye.copy();group_v=eye.copy();group_w=eye.copy();elapsed=0.
    for (a,b),t in reversed(list(zip(progress,times))):
        formed=formed@tau(H,cocycle(H,Vs[a]+Ws[b],t),elapsed)
        group_v=group_v@tau(H,cocycle(H,Vs[a],t),elapsed)
        group_w=group_w@tau(H,cocycle(H,Ws[b],t),elapsed)
        elapsed+=t
    err=np.linalg.norm(direct-formed@vac)
    require(err<2e-13,'five-exponential word equals shifted cocycle product on original vacuum')
    closure=gam[0]@gam[7]
    exact=closure@formed
    separated=(gam[0]@group_v)@(gam[7]@group_w)
    return float(err),norm(exact-separated)
word_error,coupled_error=word_control(H,vac)
Kd=K.copy();Kd[3,4]=Kd[4,3]=0
Hd0=quadratic(Kd);ed,Ud=np.linalg.eigh(Hd0);Hd=Hd0-ed[0]*eye
decoupled_word_error,decoupled_factor_error=word_control(Hd,Ud[:,0])
require(decoupled_factor_error<2e-13,'two separated clusters factor exactly with odd center fields')
require(coupled_error>1e-10,'coupled propagation is not silently replaced by exact factorization')
duhamel=[]
for t in [.1,.4,1.]:
    exact=cocycle(H,Vs[1]+Ws[1],t);factor=cocycle(H,Vs[1],t)@cocycle(H,Ws[1],t)
    error=norm(exact-factor);bound=norm(Vs[1])*norm(Ws[1])*t*t
    require(error<=bound+2e-14,'unitary two-cocycle Duhamel bound')
    duhamel.append({'time':t,'error':error,'coarse_bound':bound})

# Cross-family Bessel estimate in a correlated free vacuum; no clustering input.
As=[];Bs=[]
for j in range(8):
    local=.21j*gam[j]@gam[(j+1)%8]
    As.append(gam[j]@cocycle(H,local,.4))
    Bs.append(gam[j]@cocycle(H,-.6*local,-.3))
def schur(family):
    return max(sum(norm(A.conj().T@B+B@A.conj().T) for B in family) for A in family)
JA=schur(As);JB=schur(Bs)
cross=np.array([[np.vdot(vac,A@B@vac) for B in Bs] for A in As])
require(norm(cross)<=math.sqrt(JA*JB)+1e-13,'graded Schur bound controls non-Hermitian odd cross-correlation kernel')
require(norm(gam[0]@gam[7]+gam[7]@gam[0])==0 and norm(gam[0]@gam[7]-gam[7]@gam[0])==2,'disjoint odd fields require anticommutators')

# Active two-mode vacuum with four spectator Majoranas, all in one CAR frame.
alpha=1.3;frequencies=[1.1,2.7]
Hactive=sum(frequencies[j]*(aa[j].conj().T@aa[j]) for j in range(2))
V=sum(-1j*alpha*(gam[j]@gam[j+4]) for j in range(4))
Pindex=[b for b in range(16) if b&3==0];embed=eye[:,Pindex]
energies=np.diag(Hactive).real;inv=np.zeros(16);inv[energies>1e-12]=-1/energies[energies>1e-12]
actual=embed.conj().T@V@np.diag(inv)@V@embed
Kactive=np.zeros((4,4));Omega_inv2=np.zeros((4,4))
for j,omega in enumerate(frequencies):
    Kactive[2*j,2*j+1]=omega;Kactive[2*j+1,2*j]=-omega
    Omega_inv2[2*j,2*j]=Omega_inv2[2*j+1,2*j+1]=1/omega**2
Kbeta=-4*alpha*alpha*Kactive@Omega_inv2
beta=[embed.conj().T@gam[j+4]@embed for j in range(4)]
scalar=-2*alpha*alpha*sum(1/x for x in frequencies)
quadratic_beta=sum(.25j*Kbeta[i,j]*(beta[i]@beta[j]) for i,j in product(range(4),repeat=2))
expected=scalar*np.eye(4)+quadratic_beta
singleton_error=norm(actual-expected)
require(singleton_error<2e-13,'actual CAR elimination gives minus-four singleton skew matrix and scalar')
require(norm(actual-(scalar*np.eye(4)+quadratic_beta/2))>.1,'omitting one ordered-center factor is rejected')
require(norm(actual-(scalar*np.eye(4)-quadratic_beta))>.1,'reversing the singleton sign is rejected')
pv=-1j*gam[0]@gam[4];pw=-1j*gam[1]@gam[5]
require(norm(pv@pw-gam[0]@gam[1]@gam[4]@gam[5])<1e-14,'two native parity closures retain the active-spectator CAR sign')

# Diagnostic Bloch matrices with an explicitly bounded, noncommuting remainder.
# These are not the evaluated complete native mixed-history coefficient.
X=np.array([[0,1],[1,0]],complex);Z=np.diag([1.,-1.]);I=np.eye(2)
def kron3(a,b,c):return np.kron(np.kron(a,b),c)
Gamma=[kron3(X,I,I),kron3(Z,X,I),kron3(Z,Z,X)]
bounded=.3*kron3(Z,Z,Z);diagnostic=[]
limit=2*alpha*alpha/(math.pi*math.sqrt(3))
for L in [16,32,64,128,256]:
    k=np.full(3,2*math.pi/L);hh=sum(2*math.sin(k[j]/2)*Gamma[j] for j in range(3));omega=2*math.sqrt(3)*math.sin(math.pi/L)
    C=alpha+.1*sum(1-np.cos(k))
    full=-4*C*C*hh/omega**2+bounded
    eig=np.linalg.eigvalsh(full);leading=np.linalg.eigvalsh(-4*C*C*hh/omega**2)
    require(max(abs(eig-leading))<=norm(bounded)+1e-12,'bounded Hermitian remainder satisfies spectral perturbation bound')
    diagnostic.append({'L':L,'matrix_norm_over_L':norm(full)/L,'predicted_limit':limit})
require(abs(diagnostic[-1]['matrix_norm_over_L']-limit)<abs(diagnostic[0]['matrix_norm_over_L']-limit)/100,'diagnostic volume scaling approaches the derived coefficient')

root=Path(__file__).resolve().parents[1]
files=[Path(__file__).resolve(),root/'docs/NATIVE_MIXED_SIXTH_ORDER_COEFFICIENT_BOUNDED_THEOREM_NOTE_2026-09-15.md']
result={'status':'PASS_personal_structural_and_normalization_controls','checks':dict(checks),'native_history_census':census,'cocycle':{'word_error':word_error,'decoupled_word_error':decoupled_word_error,'decoupled_factor_error':decoupled_factor_error,'coupled_factor_error':coupled_error,'duhamel':duhamel},'graded_cross_family':{'kernel_norm':norm(cross),'bound':math.sqrt(JA*JB)},'singleton_elimination_error':singleton_error,'diagnostic_bloch':diagnostic,'seconds':time.monotonic()-start,'limits':['no native mixed resolvent spectrum is evaluated','finite CAR matrices challenge identities, not the infinite locality theorem','Bloch remainder is an explicit diagnostic, not a fitted physical kernel','uniform flux stiffness and positive native amplitude are inherited conditional sources','same author, no independent audit'],'sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}}
out=json.dumps(result,indent=2);_OUTPUT_JSON.write_text(out+'\n');print(out)

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: native star histories, CAR signs and finite cocycle identities')
    print('per_site: finite star-support patterns and CAR matrices')
    print('per_mode: diagnostic Bloch values only; no native mixed-resolvent spectrum executed')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
