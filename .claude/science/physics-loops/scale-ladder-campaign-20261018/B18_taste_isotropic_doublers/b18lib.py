import os
for _v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS"): os.environ.setdefault(_v,"1")
# B18 shared definitions. Builds the supplied corner model via the campaign exploration
# library (scratchpad qca/walklib.py -> c20/diraclib.py -> corner_psg.py, bloch.py; L=4 torus,
# translation-invariant gauge). Not modified; exec'd read-only.
import itertools, numpy as np
SCR='/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad'
exec(open(SCR+'/qca/walklib.py').read())
Sreal=np.load(SCR+'/qca/S_110_0.npy')
blS=blocks_from(Sreal); SK=lambda k: Hk(blS,k)
HL=lambda k: Hk(blli,k)                      # link hopping, H_link(k)^2 = 2
wl_,Vl_=np.linalg.eigh(Lam)
LamVals=sorted(set(np.round(wl_,6)))
Qs=[Vl_[:,np.abs(wl_-l)<1e-6]@Vl_[:,np.abs(wl_-l)<1e-6].conj().T for l in LamVals]
ph=[1,1j,-1,-1j]
def UHf(a,b): return Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]
def ULf(a,b,c): return Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3]
UH=UHf(2,3); UL=ULf(1,1,0)                   # runner Part 6 labels H23, L110
Ws=lambda k: SK(k)@RL(k)@UH@UL               # eight-node step S.R_L.U_H.U_L
EX=np.eye(3)
CUBE=[np.array(s)*np.pi/2 for s in itertools.product((1,-1),repeat=3)]
def onsite_blocks(M): return {(0,0,0):np.array(M,complex)}
def blocks_of(f, shifts):
    """Fourier blocks of a k-function f of known shift support (exact via grid of size 5)."""
    N=5; g=np.arange(N)*2*np.pi/N; out={}
    for s in shifts:
        acc=np.zeros((12,12),complex)
        for kk in itertools.product(g,repeat=3):
            acc+=f(np.array(kk))*np.exp(-1j*np.dot(kk,s))
        out[tuple(s)]=acc/N**3
    return {s:M for s,M in out.items() if np.abs(M).max()>1e-10}
def shifted(bl,e,omega=1.0):
    """blocks of omega * X(k + pi e)."""
    return {s:omega*M*(-1.0)**int(np.dot(s,e)) for s,M in bl.items()}
def intertwiners(bl1, bl2, r=0, basis=None, tol=1e-9):
    """Basis of {V(k)=sum_{|t|_inf<=r} V_t e^{ik.t}, V_t in span(basis) (default: all 12x12):
    V(k) X1(k) = X2(k) V(k) for all k}. Exact: Fourier-coefficient equations, SVD null space."""
    if basis is None: basis=[np.eye(12)[:,[i]]@np.eye(12)[[j],:] for i in range(12) for j in range(12)]
    ts=list(itertools.product(range(-r,r+1),repeat=3)); nb=len(basis)
    shifts=set(bl1)|set(bl2); us=sorted({tuple(np.add(t,s)) for t in ts for s in shifts})
    uid={u:i for i,u in enumerate(us)}
    A=np.zeros((len(us)*144,len(ts)*nb),complex)
    for it,t in enumerate(ts):
        for s in shifts:
            X1=bl1.get(s,np.zeros((12,12))); X2=bl2.get(s,np.zeros((12,12)))
            iu=uid[tuple(np.add(t,s))]
            for a,Ba in enumerate(basis):
                A[iu*144:(iu+1)*144,it*nb+a]+=(Ba@X1-X2@Ba).reshape(-1)
    _,sv,Vh=np.linalg.svd(A,full_matrices=True)
    sv=np.concatenate([sv,np.zeros(Vh.shape[0]-len(sv))])
    null=Vh[sv<tol*max(1,sv.max())].conj()
    out=[{t:sum(v[it*nb+a]*basis[a] for a in range(nb)) for it,t in enumerate(ts)} for v in null]
    return out, sv
def Vk(Vd,k): return sum(M*np.exp(1j*np.dot(k,t)) for t,M in Vd.items())
def generic_invertible(basis, ntest=4, seed=0):
    """min over random k of smallest singular value of a random combination (generic test)."""
    if not basis: return 0.0
    r_=np.random.default_rng(seed); c=r_.normal(size=len(basis))+1j*r_.normal(size=len(basis))
    V={t:sum(ci*b[t] for ci,b in zip(c,basis)) for t in basis[0]}
    return min(np.linalg.svd(Vk(V,r_.uniform(-np.pi,np.pi,3)),compute_uv=False).min() for _ in range(ntest))
