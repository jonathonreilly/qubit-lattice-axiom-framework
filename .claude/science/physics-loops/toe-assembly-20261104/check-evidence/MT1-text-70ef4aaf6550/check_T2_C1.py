# Theorem 2 and C1: resolved three-hop identity on an explicit Fock space, link operators random or the laws' own.
import numpy as np, itertools
import scipy.sparse as sp
_orig_allclose=np.allclose
def _d(x): return x.toarray() if sp.issparse(x) else x
np.allclose=lambda a,b,**k: _orig_allclose(_d(a),_d(b),**k)
_orig_norm=np.linalg.norm
np.linalg.norm=lambda a: sp.linalg.norm(a) if sp.issparse(a) else _orig_norm(a)
import scipy.sparse.linalg
rng=np.random.default_rng(0)
def jw(n):
    X=np.array([[0,1],[1,0]]);Zm=np.diag([1,-1]);a=np.array([[0,1],[0,0]]);I=np.eye(2)
    ops=[]
    for k in range(n):
        m=sp.csr_matrix(np.array([[1.0]]))
        for j in range(n): m=sp.kron(m, Zm if j<k else (a if j==k else I),format='csr')
        ops.append(m)
    return ops
ok=True
def chk(n,c):
    global ok; ok&=bool(c); print(('PASS ' if c else 'FAIL ')+n)
# matter: 4 sites i,j,k,l with 2 colours each = 8 modes; links: three link registers of dim 3 with random matrices (commute with matter)
c=jw(8); mode=lambda site,col: c[2*site+col]
i,j,k,l=0,1,2,3
dl=2
def link(which,M):
    mats=[np.eye(dl)]*3; mats[which]=M
    return sp.csr_matrix(np.kron(np.kron(mats[0],mats[1]),mats[2]))
def full(m,L): return sp.kron(m,L,format='csr')
res=[]
for trial in range(4):
    Xs=[rng.normal(size=(dl,dl))+1j*rng.normal(size=(dl,dl)) for _ in range(3)]
    e,b,cc,f=rng.integers(0,2,4)
    t_il=full(mode(i,e).T@mode(l,b),link(0,Xs[0]))
    t_ki=full(mode(k,cc).T@mode(i,e),link(1,Xs[1]))
    t_ij=full(mode(i,e).T@mode(j,f),link(2,Xs[2]))
    L_=t_il@t_ki@t_ij; R_=t_ij@t_ki@t_il
    res.append(np.allclose(L_,-R_) and np.linalg.norm(L_)>1e-6)
chk('T2 (U): t_il t_ki t_ij = - t_ij t_ki t_il, nonzero, random link matrices, random colours', all(res))
# control 1: different central colour in the middle hop breaks the identity's mechanism
t_il=full(mode(i,0).T@mode(l,0),link(0,Xs[0])); t_ki=full(mode(k,0).T@mode(i,1),link(1,Xs[1])); t_ij=full(mode(i,0).T@mode(j,0),link(2,Xs[2]))
L_=t_il@t_ki@t_ij; R_=t_ij@t_ki@t_il
chk('T2 control: with a different central mode the relation L=-R with L nonzero fails', not (np.allclose(L_,-R_) and np.linalg.norm(L_)>1e-6))
# control 2: bosonic (commuting hard-core) hops give + sign
sm=np.array([[0.,1],[0,0]]); 
def hc(k_,n=4):
    m=np.array([[1.0]])
    for q in range(n): m=np.kron(m, sm if q==k_ else np.eye(2))
    return m
bi,bj,bk,bl=[hc(q) for q in range(4)]
Lb=(bi.T@bl)@(bk.T@bi)@(bi.T@bj); Rb=(bi.T@bj)@(bk.T@bi)@(bi.T@bl)
chk('T2 control: hard-core boson hops give L=+R (nonzero), not L=-R', np.allclose(Lb,Rb) and np.linalg.norm(Lb)>0)
# O: Majoranas
gam=[]
for m_ in c: gam += [m_+m_.T, -1j*(m_-m_.T)]
gm=lambda site,a: gam[4*site+a]   # 4 Majorana labels per site
res=[]
for trial in range(4):
    Xs=[rng.normal(size=(dl,dl))+1j*rng.normal(size=(dl,dl)) for _ in range(3)]
    e,b,cc,f=rng.integers(0,4,4)
    t_il=full(0.5j*gm(i,e)@gm(l,b),link(0,Xs[0]))
    t_ki=full(0.5j*gm(k,cc)@gm(i,e),link(1,Xs[1]))
    t_ij=full(0.5j*gm(i,e)@gm(j,f),link(2,Xs[2]))
    L_=t_il@t_ki@t_ij; R_=t_ij@t_ki@t_il
    res.append(np.allclose(L_,-R_) and np.linalg.norm(L_)>1e-6)
chk('T2 (O): Majorana version, random link matrices', all(res))
# C1: the laws' own link components are nonzero.  U: r^y_j r^x_k^dagger on Lambda^m C^10 for every 1<=m<=9 ; O: (i eta_a eta_{10+b})^2 = 1
r=jw(10)
N=sum(x.T@x for x in r); num=np.rint(N.diagonal()).astype(int)
allm=True
for m in range(0,11):
    sel=np.where(num==m)[0]
    nz=True
    for jj in range(5):          # y-end modes 0..4, x-end modes 5..9
        for kk in range(5,10):
            op=(r[jj]@r[kk].T).tocsr()[sel][:,sel]
            nz&=np.linalg.norm(op)>0
    if 1<=m<=9: allm&=nz
    else: print(f'   control m={m}: link hop component nonzero? {nz} (expected False)'); allm&= (not nz)
chk('C1 (U): r^y_j r^x_k^dagger nonzero on Lambda^m C^10 for all 1<=m<=9, zero for m=0,10', allm)
eta=[]
for m_ in r: eta += [m_+m_.T, -1j*(m_-m_.T)]
sq=all(np.allclose((1j*eta[a]@eta[10+b])@(1j*eta[a]@eta[10+b]),sp.identity(1024,format='csr')) for a in range(10) for b in range(10))
chk('C1 (O): (i eta_a eta_{10+b})^2 = 1 for all a,b', sq)
# C2/C8 ingredients: product of ten Majoranas of one end = i(-1)^p ; Gamma=-eta_1..eta_20 = (-1)^{p_x+p_y}
p1=sp.identity(1024,dtype=complex,format='csr')
for a in range(10): p1=p1@eta[a]
py=sum(r[q].T@r[q] for q in range(5)); 
import scipy.linalg as sl
chk('C2 [check]: product of the ten Majoranas of one end = i(-1)^p', np.allclose(p1,1j*sp.diags((-1.0)**np.rint(py.diagonal()))))
p2=sp.identity(1024,dtype=complex,format='csr')
for a in range(10,20): p2=p2@eta[a]
chk('C2/C8: eta_1...eta_20 = -(-1)^{p_x+p_y}, i.e. -1 on the even (S_+) sector; end factors commute', np.allclose(p1@p2,-sp.diags((-1.0)**num)) and np.allclose(p1@p2,p2@p1))
# C2 step 1: r_A^dagger r_B restricted to Lambda^m is +- a matrix unit ; d_A^dagger P0 d_B is a matrix unit
import random
random.seed(1)
def prod(lst):
    m_=sp.identity(1024,format='csr')
    for x in lst: m_=m_@x
    return m_
good=True
for m in (1,3,5,9):
    sel=np.where(num==m)[0]
    for t in range(3):
        Aset=sorted(random.sample(range(10),m)); Bset=sorted(random.sample(range(10),m))
        op=(prod([r[a].T for a in Aset])@prod([r[b] for b in Bset])).tocsr()[sel][:,sel].toarray()
        good&= (np.count_nonzero(np.abs(op)>1e-12)==1) and abs(abs(op).max()-1)<1e-12
chk('C2 step 1 (U): r_A^dagger r_B restricts to +-(one matrix unit) on Lambda^m C^10', good)
P0=prod([sp.identity(1024,format='csr')-x.T@x for x in r]); good=True
for t in range(6):
    a=random.randrange(0,11); b=random.randrange(0,11)
    Aset=random.sample(range(10),a); Bset=random.sample(range(10),b)
    op=(prod([r[q].T for q in Aset])@P0@prod([r[q] for q in Bset])).toarray()
    good&=(np.count_nonzero(np.abs(op)>1e-12)==1)
chk('C2 step 1 (O): d_A^dagger P_0 d_B is +-(one matrix unit) on the 10-mode Fock space', good)
print('ALL PASS' if ok else 'SOME FAIL')
