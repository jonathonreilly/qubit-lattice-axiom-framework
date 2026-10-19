"""Phase A (reviewer): on-site action of the 24 rotations of O under AXIS soldering
rho(g) = s(g)|g| (repo convention: scripts/cubic_covariant_..._2026_10_17.py, Q(M,'axis')),
written in the occupation basis = eigenbasis of n.sigma, n=(1,1,1)/sqrt3 (C4b Lemma 2).
Computes an SU(2) lift u_g with u sigma_a u^dag = sum_b rho_ba sigma_b and its form in the n basis."""
import itertools, numpy as np
X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]).astype(complex);S=[X,Y,Z]
O=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product((1,-1),repeat=3):
        M=np.zeros((3,3),int)
        for i in range(3): M[p[i],i]=s[i]
        if round(np.linalg.det(M))==1: O.append(M)
psign=lambda M:int(round(np.linalg.det(np.abs(M))))
nv=np.ones(3)/np.sqrt(3); Hn=sum(nv[a]*S[a] for a in range(3))
w,V=np.linalg.eigh(Hn); V=V[:,::-1]   # columns: n.sigma=+1 (n=0), -1 (n=1)
P=PASS=FAIL=0
def chk(name,ok):
    global PASS,FAIL
    PASS+=ok; FAIL+=(not ok); print(('PASS ' if ok else 'FAIL ')+name)
def lift(R):
    # find u in SU(2): u sigma_a u^dag = sum_b R[b,a] sigma_b ; search via axis-angle
    ang=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
    if abs(ang)<1e-9: return np.eye(2,dtype=complex)
    if abs(ang-np.pi)<1e-9:
        ax=np.sqrt(np.clip((np.diag(R)+1)/2,0,1)); i=np.argmax(ax)
        ax=R[:,i]+np.eye(3)[:,i]; ax=ax/np.linalg.norm(ax)
    else:
        ax=np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])/(2*np.sin(ang))
    return np.cos(ang/2)*np.eye(2)-1j*np.sin(ang/2)*sum(ax[a]*S[a] for a in range(3))
odd_offdiag=[];even_diag=[]
for M in O:
    R=psign(M)*np.abs(M); u=lift(R)
    ok=all(np.allclose(u@S[a]@u.conj().T,sum(R[b,a]*S[b] for b in range(3))) for a in range(3))
    chk(f'lift reproduces rho for g with perm sign {psign(M)}',ok)
    un=V.conj().T@u@V
    if psign(M)==1:
        d=np.allclose(un[0,1],0) and np.allclose(un[1,0],0)
        ph=un[1,1]/un[0,0]; even_diag.append(d)
        chk(f'T element: diagonal in n basis, relative phase ratio^3=1 (got {np.round(ph,3)})', d and np.isclose(ph**3,1))
    else:
        d=np.allclose(un[0,0],0) and np.allclose(un[1,1],0)
        ph=un[1,0]/un[0,1]
        chk(f'odd element: off-diagonal (particle-hole) in n basis, phase ratio {np.round(ph,3)}; ratio^3 = const', d)
        odd_offdiag.append(ph)
chk('odd off-diagonal phase ratios take values in one coset c*{1,w,w^2}',
    len(set(np.round(np.array(odd_offdiag)**3,6)))==1)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
