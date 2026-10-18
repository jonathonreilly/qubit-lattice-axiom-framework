import os
for _v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS"): os.environ.setdefault(_v,"1")
# B20 shared definitions.  Builds the supplied corner model through B18's b18lib.py (which execs the
# campaign exploration library scratchpad qca/walklib.py -> c20/diraclib.py read-only; L=4 torus,
# translation-invariant gauge).  Adds: batched word evaluation, exact factor derivatives, degenerate
# perturbation theory velocity matrices, refined node search, and a Lipschitz cleanliness certificate.
import itertools, numpy as np
B20='/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step'
B18=os.path.join(os.path.dirname(B20),'B18_taste_isotropic_doublers')
_cwd=os.getcwd()
exec(open(os.path.join(B18,'b18lib.py')).read())
os.chdir(_cwd)
from scipy.optimize import minimize
# ---- S(k) = diag(sig_c exp(i k.f_c)) (checked below against the library's S)
F=np.array([[1,1,0],[1,-1,0],[1,0,1],[1,0,-1],[-1,1,0],[-1,-1,0],[-1,0,1],[-1,0,-1],[0,1,1],[0,1,-1],[0,-1,1],[0,-1,-1]],float)
SIG=np.array([1,-1,-1,1,-1,1,1,-1,1,-1,-1,1],float)
_k=np.array([0.3,0.7,-1.1]); assert np.allclose(SK(_k),np.diag(SIG*np.exp(1j*F@_k)))
assert np.allclose(SK(_k)@SK(_k).conj().T,np.eye(12))
RLsh=np.array(sorted(blli.keys()),float); RLM=np.array([blli[tuple(int(x) for x in s)] for s in RLsh])/np.sqrt(2)
assert np.allclose(sum(M*np.exp(1j*_k@s) for s,M in zip(RLsh,RLM)),RL(_k))
PLANE=np.array([0 if f[2]==0 else (1 if f[1]==0 else 2) for f in F])     # 0: xy, 1: xz, 2: yz corners
# ---- on-site factors: phases (multiples of 2pi/12 when 'pi6') on spectral projectors of H_on (Ps) and Lambda (Qs)
PH12=np.exp(1j*np.pi*np.arange(12)/6)
def onH(a,b,c=0,unit=3): return PH12[(unit*c)%12]*Ps[0]+PH12[(unit*a)%12]*Ps[1]+PH12[(unit*b)%12]*Ps[2]
def onL(a,b,c,d=0,unit=3): return PH12[(unit*d)%12]*Qs[0]+PH12[(unit*a)%12]*Qs[1]+PH12[(unit*b)%12]*Qs[2]+PH12[(unit*c)%12]*Qs[3]
# unit=3 gives Clifford phases i^n, matching B18's UHf/ULf labels (H{a}{b} = onH(a,b), L{a}{b}{c} = onL(a,b,c)).
assert np.allclose(onH(2,3),UHf(2,3)) and np.allclose(onL(1,1,0),ULf(1,1,0))
# ---- words: list of letters; k-letters 'S','Si','S2','S2i','R'; on-site letters are 12x12 arrays
KL={'S':(1,),'Si':(-1,),'S2':(2,),'S2i':(-2,)}
def Wbatch(word,ks):
    """W(k) for an (N,3) array of momenta: product of letters left to right."""
    ks=np.atleast_2d(ks); N=len(ks); W=np.broadcast_to(np.eye(12,dtype=complex),(N,12,12)).copy()
    for L in word:
        if isinstance(L,str):
            if L=='R':
                R=np.einsum('nt,tij->nij',np.exp(1j*ks@RLsh.T),RLM); W=W@R
            else:
                p=KL[L][0]; d=(SIG**(abs(p)))*np.exp(1j*p*(ks@F.T))     # (N,12)
                W=W*d[:,None,:]
        else: W=W@L
    return W
def Wk(word,k): return Wbatch(word,np.asarray(k,float)[None])[0]
def factor_and_grad(L,k):
    if isinstance(L,str):
        if L=='R':
            ph=np.exp(1j*RLsh@k); M=np.einsum('t,tij->ij',ph,RLM); G=[np.einsum('t,tij->ij',1j*RLsh[:,j]*ph,RLM) for j in range(3)]
            return M,G
        p=KL[L][0]; d=(SIG**abs(p))*np.exp(1j*p*(F@k)); return np.diag(d),[np.diag(1j*p*F[:,j]*d) for j in range(3)]
    return L,[np.zeros((12,12))]*3
def W_and_grad(word,k):
    k=np.asarray(k,float); fs=[factor_and_grad(L,k) for L in word]; n=len(fs)
    pre=[np.eye(12,dtype=complex)]
    for M,_ in fs: pre.append(pre[-1]@M)
    suf=[np.eye(12,dtype=complex)]
    for M,_ in fs[::-1]: suf.append(M@suf[-1])
    suf=suf[::-1]
    G=[sum(pre[i]@fs[i][1][j]@suf[i+1] for i in range(n)) for j in range(3)]
    return pre[-1],G
def lipschitz(word):
    """Rigorous bound on sup_k sup_|u|=1 ||u.grad W(k)|| (sum over letters of per-letter bounds)."""
    L_=0.0
    for L in word:
        if isinstance(L,str): L_+= np.sqrt(6.0) if L=='R' else abs(KL[L][0])*np.sqrt(2.0)
    return L_
def eph(W): return np.angle(np.linalg.eigvals(W))
def dist_to_E(word,ks,E):
    e=np.angle(np.linalg.eigvals(Wbatch(word,ks)))
    return np.min(np.abs(wrap(e-E)),axis=-1)
def node_levels(word,k,tol=1e-7):
    return levels(lambda kk: Wk(word,kk),np.asarray(k,float),tol)
def vel_matrix(word,k0,E,m=2):
    """Degenerate perturbation theory at k0 for the m eigenphases closest to E.
    h_j = -i P^dag W0^dag d_jW P (m x m Hermitian); for m=2 h(q) = a.q 1 + sigma.(M q)."""
    import scipy.linalg as sl
    W0,G=W_and_grad(word,k0)
    T,Z=sl.schur(W0,output='complex'); ev=np.angle(np.diag(T)); idx=np.argsort(np.abs(wrap(ev-E)))[:m]
    P=Z[:,idx]; spread=np.ptp(wrap(ev[idx]-E)); nxt=np.sort(np.abs(wrap(ev-E)))[m] if m<12 else np.inf
    h=[-1j*P.conj().T@W0.conj().T@G[j]@P for j in range(3)]
    h=[(x+x.conj().T)/2 for x in h]
    if m!=2: return dict(h=h,spread=spread,next=nxt)
    sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1])
    a=np.array([np.trace(x).real/2 for x in h]); M=np.array([[np.trace(x@s).real/2 for s in (sx,sy,sz)] for x in h])   # M[j,b]
    sv=np.linalg.svd(M,compute_uv=False)
    return dict(a=a,M=M,sv=sv,chi=int(np.sign(np.linalg.det(M))),spread=spread,next=nxt,aniso=(sv.max()-sv.min())/max(sv.mean(),1e-300),tilt=np.linalg.norm(a))
def chirality_flux(word,k0,E,r=1e-3,n=24):
    """Berry flux of the lower branch (eigenphase just below E) through a sphere of radius r (lattice FHS method)."""
    th=np.linspace(0,np.pi,n+1); phs=np.linspace(0,2*np.pi,2*n,endpoint=False)
    pts=np.array([[np.sin(t)*np.cos(p),np.sin(t)*np.sin(p),np.cos(t)] for t in th for p in phs])*r+k0
    Ws=Wbatch(word,pts); Uv=[]
    for W in Ws:
        e,v=np.linalg.eig(W); a=wrap(np.angle(e)-E); cand=np.where((a<0)&(a>-0.5),a,-9); i=np.argmax(cand)
        x=v[:,i]; Uv.append(x/np.linalg.norm(x))
    Uv=np.array(Uv).reshape(n+1,2*n,12); tot=0
    for i in range(n):
        for j in range(2*n):
            a_,b_,c_,d_=Uv[i,j],Uv[i+1,j],Uv[i+1,(j+1)%(2*n)],Uv[i,(j+1)%(2*n)]
            tot+=np.angle(np.vdot(a_,b_)*np.vdot(b_,c_)*np.vdot(c_,d_)*np.vdot(d_,a_))
    return tot/(2*np.pi)
def find_crossings(word,E,ngrid=16,nstart=80,lo=-np.pi,hi=np.pi,period=2*np.pi,tol=1e-7,seed=0,extra=()):
    """Refined search for momenta where E is an eigenphase: batched grid, local minima, Nelder-Mead.
    Returns list of distinct crossing momenta (mod period cube) and the grid minimum."""
    g=np.linspace(lo,hi,ngrid,endpoint=False)+(hi-lo)/ngrid*0.37
    G=np.array(list(itertools.product(g,repeat=3))); d=dist_to_E(word,G,E)
    order=np.argsort(d); starts=list(G[order[:nstart]])+list(extra)
    f=lambda k: float(dist_to_E(word,np.asarray(k)[None],E)[0])
    sols=[]
    for k0 in starts:
        r=minimize(f,k0,method='Nelder-Mead',options={'xatol':1e-11,'fatol':1e-14,'maxiter':4000})
        if r.fun<tol:
            x=np.mod(r.x-lo,period)+lo
            if not any(np.linalg.norm(wrap((x-s)*2*np.pi/period))<1e-4 for s in sols): sols.append(x)
    return sols,float(d.min())
def certify_clean(word,E,balls,radius,lo=-np.pi,hi=np.pi,n0=24,maxdepth=7,Lip=None,budget=3_000_000):
    """Lipschitz certificate: every cube cell outside the balls (centres `balls`, given radius, periodic box)
    either has dist(spec W(centre), E) > Lip * half-diagonal (so E is not reached in it) or is subdivided.
    Returns (certified, n_uncertified_leaf_cells, evaluations, min margin seen)."""
    Lip=lipschitz(word) if Lip is None else Lip; P=hi-lo
    balls=np.array(balls) if len(balls) else np.zeros((0,3))
    h=P/n0; g=lo+h*(np.arange(n0)+0.5)
    cells=np.array(list(itertools.product(g,repeat=3))); size=h; evals=0; bad=0; minmarg=np.inf
    for depth in range(maxdepth+1):
        if len(cells)==0: break
        rad=size*np.sqrt(3)/2
        if len(balls):
            dd=np.min(np.linalg.norm(np.mod(cells[:,None,:]-balls[None]+P/2,P)-P/2,axis=2),axis=1)
            cells=cells[dd+rad>radius]          # drop cells wholly inside a ball
        if len(cells)==0: break
        dist=np.concatenate([dist_to_E(word,cells[i:i+4096],E) for i in range(0,len(cells),4096)]); evals+=len(cells)
        marg=dist-Lip*rad; minmarg=min(minmarg,marg.min()) if depth==0 else minmarg
        if np.any(dist<1e-9):
            # a genuine crossing outside the balls (at a cell centre)
            return False,int(np.sum(dist<1e-9)),evals,0.0
        todo=cells[marg<=0]
        if depth==maxdepth or evals+8*len(todo)>budget: bad=len(todo); break
        off=np.array(list(itertools.product((-0.25,0.25),repeat=3)))*size
        cells=(todo[:,None,:]+off[None]).reshape(-1,3); size/=2
    return bad==0,bad,evals,minmarg
