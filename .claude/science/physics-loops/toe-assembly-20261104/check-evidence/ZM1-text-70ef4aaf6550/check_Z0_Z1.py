# Z0 (geometry facts), Lemma Z1a, Theorem Z1 Step 3/5 structure, Corollary Z1.1 arithmetic. Written from the statements.
import numpy as np, itertools
from scipy.linalg import expm
from check_common import *
rng=np.random.default_rng(3)
# --- Z0(2): one free tick moves a site by sup-distance <=2 and some entry reaches 2 (free-walk instance of the support rule)
N=8; sites=list(itertools.product(range(N),repeat=3)); si={s:i for i,s in enumerate(sites)}
def Rreal(T):
    Mx=np.zeros((N**3,N**3))
    for x in sites:
        for j in range(3):
            own='e' if x[j]%2==0 else 'o'
            if own!=T: continue
            y=list(x); y[j]=(y[j]+1)%N; y=tuple(y)
            Mx[si[y],si[x]]+=eta(j,x)/np.sqrt(3); Mx[si[x],si[y]]+=eta(j,x)/np.sqrt(3)
    return Mx
Re=Rreal('e'); Ro=Rreal('o'); eps=0.6
print("A1 use: ||Re^2-1||,||Ro^2-1||",nrm(Re@Re-np.eye(N**3)),nrm(Ro@Ro-np.eye(N**3)))
V=(np.cos(eps)*np.eye(N**3)+1j*np.sin(eps)*Ro)@(np.cos(eps)*np.eye(N**3)-1j*np.sin(eps)*Re)
def sup(x,y): return max(min((a-b)%N,(b-a)%N) for a,b in zip(x,y))
dmax=max(sup(sites[i],sites[j]) for i,j in zip(*np.nonzero(abs(V)>1e-12)))
print("Z0(2) free instance: max sup-distance moved by one tick =",dmax,"(claim: at most 2; control: it is not <=1)")
# --- Z0(3): coarse-cell centre is an odd cube centre; rotation about it = rotation about c0 + even translation; permutes blocks
def rots():
    out=[]
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1,-1),repeat=3):
            Q=np.zeros((3,3),int)
            for j in range(3): Q[p[j],j]=sg[j]
            if round(np.linalg.det(Q))==1: out.append(Q)
    return out
ok=True; trans=set()
for L in range(1,6):
    for b in [np.array([0,0,0]),np.array([1,-2,3])]:
        p=4*L*b+(2*L-0.5)*np.ones(3); c0=0.5*np.ones(3)
        ok&=all(int(np.floor(pi))%2==1 for pi in p)
        for Q in rots():
            t=(p-c0)-Q@(p-c0)          # x->Q(x-p)+p = [Q(x-c0)+c0] + t
            ok&=all(abs(ti-round(ti))<1e-12 and round(ti)%2==0 for ti in t)
            for u in itertools.product(range(-1,3),repeat=3):
                blk=np.array([[2*L*u[i]+a[i] for i in range(3)] for a in itertools.product((0,2*L-1),repeat=3)])
                img=(Q@(blk-p).T).T+p; lo=img.min(0)
                ok&=all(abs(l-round(l))<1e-12 and round(l)%(2*L)==0 for l in lo) and np.allclose(img.max(0)-lo,2*L-1)
        # transitivity on the 8 blocks of the coarse cell
        orb={tuple(np.rint(((Q@((2*L*np.array([0,0,0])+4*L*b)+ (L-0.5) - p))+p-(L-0.5)-4*L*b)/(2*L)).astype(int)) for Q in rots()}
        ok&=(len(orb)==8)
print("Z0(3): centre parity, even-translation, block permutation, transitivity on 8 blocks, L=1..5:",ok)
p=np.array([1.5,1.5,1.5]); Q=rots()[5]; t=(p-.5)-Q@(p-.5)
# control: a site-centred rotation is not c0-rotation plus an even translation
p=np.array([2.,2.,2.]); bad=[((p-.5)-Q@(p-.5)) for Q in rots()]
print("   control (rotation about a site): all translations even integer vectors?",all(all(abs(ti-round(ti))<1e-12 and round(ti)%2==0 for ti in t) for t in bad))
# Z0(5) count for L_cube: dims
for L in [1,2]:
    S=1; ns=1
    print(f"Z0(5) L={L}: 8L^3 sites={8*L**3}, links with lower endpoint in block={3*8*L**3}; algebra dim exponent check 2*ns*8L^3={2*ns*8*L**3}, 48L^3={48*L**3} (=2 x 24L^3)")
# --- Lemma Z1a
def w(K,eps,mu):
    a=(np.cos(mu)-np.cos(2*eps))/2;b=(-np.cos(2*eps)-np.cos(mu))/2
    return np.arccos(a*np.mean(np.cos(K))-b)
Pi=np.pi*np.ones(3)
for eps,mu,tag in [(1.0,np.pi-2.0,"exceptional 2eps+mu=pi"),(1.0,0.5,"control"),(0.7,0.0,"control mu=0")]:
    vals=[w(K,eps,mu)+w(K+Pi,eps,mu) for K in rng.uniform(-np.pi,np.pi,(200,3))]
    print(f"Z1a(iii) {tag}: range of w(K)+w(K+Pi)-pi over 200 K: [{min(vals)-np.pi:.2e},{max(vals)-np.pi:.2e}]")
# other half-period shifts, exceptional parameters: w(K)+w(K+delta) must not be constant
for d in itertools.product((0,np.pi),repeat=3):
    if sum(d)==0 or sum(d)>3*np.pi-1e-9: continue
    vals=[w(K,1.0,np.pi-2.0)+w(K+np.array(d),1.0,np.pi-2.0) for K in rng.uniform(-np.pi,np.pi,(200,3))]
    assert max(vals)-min(vals)>1e-2
print("Z1a(iii): for the six other half-period shifts the sum varies (spread >1e-2) at exceptional parameters: True")
# --- Theorem Z1 Step 3 structure: multiplicities of the eigenvalues of V_block(theta)^n at a generic theta
def Rblock(th,T,L):
    cells=list(itertools.product(range(L),repeat=3)); ci={c:i for i,c in enumerate(cells)}
    n=8*L**3; Mx=np.zeros((n,n),complex)
    for c in cells:
        for r in RES:
            x=[2*c[i]+r[i] for i in range(3)]
            for j in range(3):
                for sgn in (1,-1):
                    y=list(x); y[j]+=sgn
                    lower=x if sgn==1 else y
                    own='e' if lower[j]%2==0 else 'o'
                    if own!=T: continue
                    cc=[yi//2 for yi in y]; rp=tuple(yi%2 for yi in y)
                    up=[c_//L for c_ in cc]; cp=tuple(c_%L for c_ in cc)
                    Mx[ci[cp]*8+IDX[rp],ci[c]*8+IDX[r]]+=eta(j,lower)*np.exp(-1j*np.dot(th,up))/np.sqrt(3)
    return Mx
def mults(L,n,eps,mu,th):
    Re=Rblock(th,'e',L); Ro=Rblock(th,'o',L)
    Vb=expm(1j*(eps+mu/2)*Ro)@expm(-1j*(eps-mu/2)*Re)
    ev=np.linalg.eigvals(np.linalg.matrix_power(Vb,n)); ev=sorted(np.angle(ev))
    groups=[1]
    for a,b in zip(ev,ev[1:]):
        if abs(a-b)<1e-7: groups[-1]+=1
        else: groups.append(1)
    return sorted(set(groups)),len(groups)
th=np.array([0.31,-0.77,1.23])
for L,n,eps,mu,tag in [(2,1,0.7,0.0,"generic"),(3,2,0.7,0.3,"generic"),(2,2,1.0,np.pi-2.0,"EXCEPTIONAL (L,n even, 2eps+mu=pi)"),(2,1,1.0,np.pi-2.0,"n odd"),(3,2,1.0,np.pi-2.0,"L odd"),(2,2,1.0,0.5,"2eps+mu!=pi")]:
    m,g=mults(L,n,eps,mu,th)
    print(f"Z1 step 3: L={L} n={n} {tag}: multiplicities {m}, distinct eigenvalues {g} (2L^3={2*L**3}, L^3={L**3})")
# block fibre spectrum = union of fine fibres at xi_m (Step 1), incl. label shift
L=3; eps=.7
Vb=expm(1j*eps*Rblock(th,'o',L))@expm(-1j*eps*Rblock(th,'e',L))
ws=sorted(np.concatenate([[s*w((th+2*np.pi*np.array(m))/L,eps,0)]*4 for m in itertools.product(range(L),repeat=3) for s in (1,-1)]))
print("Z1 step 1: block-fibre quasi-energies = {+-w(xi_m)} x4, max mismatch",max(abs(np.array(sorted(np.angle(np.linalg.eigvals(Vb))))-np.array(ws))))
# --- Corollary Z1.1 arithmetic
print("Z1.1(2): L>=2 with L^3 | 40:",[L for L in range(2,5) if 40%L**3==0]," ; Majorana L^3 | 80:",[L for L in range(2,6) if 80%L**3==0])
print("Z1.1(3): (L1 L2)^3 for L1,L2>=2 is >=64; 64|40?",40%64==0,"64|80?",80%64==0,"; any cube n^3>=64 dividing 40 or 80:",[n for n in range(4,6) if 40%n**3==0 or 80%n**3==0])
