import numpy as np, itertools, math
SX=np.array([[0,1],[1,0]],complex); SY=np.array([[0,-1j],[1j,0]]); SZ=np.array([[1,0],[0,-1]],complex); I2=np.eye(2,dtype=complex)
PA=(SX,SY,SZ)
def kr(a,b): return np.kron(a,b)
SWAP=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],complex)
POS=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
DIFFS=set()
for r in POS+[(0,0,0)]:
    for s in POS+[(0,0,0)]:
        DIFFS.add(tuple(a-b for a,b in zip(r,s)))
DIFFS=sorted(DIFFS)
def Hq(q,K):
    """q: (n,3) array, K: (3,) -> H (n,4,4), Hd[a] (n,4,4), Hdd[a]"""
    n=q.shape[0]
    H=np.zeros((n,4,4),complex); Hd=[];Hdd=[]
    for a in range(3):
        s1=np.sin(K[a]/2+q[:,a]); s2=np.sin(K[a]/2-q[:,a]); c1=np.cos(K[a]/2+q[:,a]); c2=np.cos(K[a]/2-q[:,a])
        A=kr(PA[a],I2); B=kr(I2,PA[a])
        Ha=s1[:,None,None]*A+s2[:,None,None]*B
        H+=Ha
        Hd.append(0.5*(c1[:,None,None]*A+c2[:,None,None]*B))
        Hdd.append(-0.25*Ha)
    return H,Hd,Hdd
def free_G(E,K,N,axes=(0,1,2),order=2):
    """dict d-> {'G','GE',('d1',a),('d2',a)} 4x4 lattice Green blocks via slice-wise 2D FFT"""
    g=2*np.pi*np.arange(N)/N
    K=np.asarray(K,float)
    keys=['G']+(['GE'] if order>=1 else [])+[(t,a) for a in axes for t in ('d1','d2')]
    res={d:{k:np.zeros((4,4),complex) for k in keys} for d in DIFFS}
    qy,qz=np.meshgrid(g,g,indexing='ij')
    for ix in range(N):
        q=np.stack([np.full(qy.size,g[ix]),qy.ravel(),qz.ravel()],1)
        H,Hd,Hdd=Hq(q,K)
        R=np.linalg.inv(E*np.eye(4)-H)
        mats={'G':R}
        if order>=1: mats['GE']=-(R@R)
        for a in axes:
            RH=R@Hd[a]@R
            mats[('d1',a)]=RH
            mats[('d2',a)]=R@Hdd[a]@R+2*RH@Hd[a]@R
        for k,M in mats.items():
            F=np.fft.ifft2(M.reshape(N,N,4,4),axes=(0,1))*(N*N)   # sum_{qy,qz} e^{i(qy dy+qz dz)} M
            for d in DIFFS:
                res[d][k]+=np.exp(1j*g[ix]*d[0])*F[d[1]%N,d[2]%N]
    n=N**3
    for d in DIFFS:
        for k in res[d]: res[d][k]=res[d][k]/n
    return res
from scipy.linalg import expm
def U_rot(axis,ang):
    n=np.array(axis,float); n/=np.linalg.norm(n)
    return expm(-1j*ang/2*(n[0]*SX+n[1]*SY+n[2]*SZ))
def commutant_z():
    """hermitian 4x4 M(e_z) commuting with quarter turn about z (both coins) and (half-turn about x) o SWAP."""
    Uq=U_rot((0,0,1),np.pi/2); G1=kr(Uq,Uq)
    Ux=U_rot((1,0,0),np.pi); G2=SWAP@kr(Ux,Ux)
    # basis of hermitian 4x4: 16 real
    basis=[]
    for i in range(4):
        for j in range(4):
            if i==j:
                m=np.zeros((4,4),complex); m[i,i]=1; basis.append(m)
            elif i<j:
                m=np.zeros((4,4),complex); m[i,j]=1; m[j,i]=1; basis.append(m)
                m=np.zeros((4,4),complex); m[i,j]=1j; m[j,i]=-1j; basis.append(m)
    # constraints [M,G]=0 linear in real coeffs
    rows=[]
    for G in (G1,G2):
        cols=[]
        for b in basis:
            c=b@G-G@b
            cols.append(np.concatenate([c.real.ravel(),c.imag.ravel()]))
        rows.append(np.array(cols).T)
    A=np.vstack(rows)
    u,s,vt=np.linalg.svd(A)
    null=vt[np.sum(s>1e-10):]
    Ms=[sum(c*b for c,b in zip(v,basis)) for v in null]
    return Ms
def build_M_all(Mz):
    """M(r) for the six bonds from M(e_z): rotations x->y->z->x about (1,1,1) by 2pi/3 ; exchange for negatives."""
    Rc=U_rot((1,1,1),2*np.pi/3); Uc=kr(Rc,Rc)
    # which maps e_z -> ? check rotation: rotation by +2pi/3 about (1,1,1) sends x->y->z->x
    # so e_x -> e_y, e_y -> e_z, e_z -> e_x. M(e_x)=Uc M(e_z) Uc^dag ; M(e_y)=Uc M(e_x)Uc^dag
    Mx=Uc@Mz@Uc.conj().T; My=Uc@Mx@Uc.conj().T
    # check consistency: M(e_z)=Uc M(e_y) Uc^dag
    assert np.allclose(Uc@My@Uc.conj().T,Mz)
    Mm={ (1,0,0):Mx,(0,1,0):My,(0,0,1):Mz}
    out={}
    for r,m in Mm.items():
        out[r]=m; out[tuple(-x for x in r)]=SWAP@m@SWAP
    return out
def Vmat(g,Mall):
    V=np.zeros((24,24),complex)
    for i,r in enumerate(POS): V[4*i:4*i+4,4*i:4*i+4]=g*Mall[r]
    return V

def blocks(res,key):
    """assemble 24x24 Gpp, 24x4 Gp0, 4x24 G0p, 4x4 G00 from dict res[d][key]"""
    Gpp=np.zeros((24,24),complex); Gp0=np.zeros((24,4),complex); G0p=np.zeros((4,24),complex)
    for i,r in enumerate(POS):
        for j,s in enumerate(POS):
            d=tuple(a-b for a,b in zip(r,s)); Gpp[4*i:4*i+4,4*j:4*j+4]=res[d][key]
        Gp0[4*i:4*i+4,:]=res[r][key]
        G0p[:,4*i:4*i+4]=res[tuple(-x for x in r)][key]
    return Gpp,Gp0,G0p,res[(0,0,0)][key]
# series: list [v0,v1,v2] with X(t)=v0+t v1+t^2/2 v2
def smul(X,Y):
    return [X[0]@Y[0], X[1]@Y[0]+X[0]@Y[1], X[2]@Y[0]+2*X[1]@Y[1]+X[0]@Y[2]]
def sinv(X):
    i0=np.linalg.inv(X[0])
    return [i0, -i0@X[1]@i0, -i0@X[2]@i0+2*i0@X[1]@i0@X[1]@i0]
def ssub(X,Y): return [x-y for x,y in zip(X,Y)]
def sconst(M): return [M,np.zeros_like(M),np.zeros_like(M)]
def G1_series(res,a):
    parts=[blocks(res,k) for k in ('G',('d1',a),('d2',a))]
    Gpp=[p[0] for p in parts]; Gp0=[p[1] for p in parts]; G0p=[p[2] for p in parts]; G00=[p[3] for p in parts]
    corr=smul(smul(Gp0,sinv(G00)),G0p)
    return ssub(Gpp,corr)
def G1_E(res):
    Gpp,Gp0,G0p,G00=blocks(res,'G'); Epp,Ep0,E0p,E00=blocks(res,'GE')
    i0=np.linalg.inv(G00)
    corr=Ep0@i0@G0p - Gp0@i0@E00@i0@G0p + Gp0@i0@E0p
    return Epp-corr
def B_series(res,a,V):
    S=G1_series(res,a)
    Bs=sinv(S)
    Bs[0]=Bs[0]-V
    return Bs
def B_all(E,g,Mall,N):
    res=free_G(E,(0,0,0),N)
    V=Vmat(g,Mall)
    return res,V

from scipy.optimize import brentq
EC=2*np.sqrt(3.0)
def Bvals(E,V,N,cache=None):
    res=free_G(E,(0,0,0),N,axes=(),order=0)
    S=blocks(res,'G'); Gpp,Gp0,G0p,G00=S
    G1=Gpp-Gp0@np.linalg.inv(G00)@G0p
    B=np.linalg.inv(G1)-V
    B=(B+B.conj().T)/2
    return np.linalg.eigvalsh(B)
def find_levels(V,N,side=+1,Emax=None,nscan=14,eta=0.02):
    nV=np.linalg.norm(V,2)
    if Emax is None: Emax=EC+1.5*nV+20
    Es=side*(EC+eta+(Emax-EC-eta)*np.linspace(0,1,nscan)**2)
    vals=np.array([Bvals(E,V,N) for E in Es])
    roots=[]; assigned=set()
    for j in range(24):
        if j in assigned: continue
        v=vals[:,j]
        for k in range(nscan-1):
            if v[k]*v[k+1]<0:
                f=lambda E:Bvals(E,V,N)[j]
                r=brentq(f,Es[k],Es[k+1],xtol=1e-12,rtol=1e-13)
                bv=Bvals(r,V,N)
                js=[jj for jj in range(24) if abs(bv[jj])<1e-6]
                for jj in js: assigned.add(jj)
                roots.append((js,r))
                break
    return roots
def level_weights(E0,V,N,tol=1e-6):
    res=free_G(E0,(0,0,0),N)
    GE=G1_E(res)
    S0=G1_series(res,0)
    i0=np.linalg.inv(S0[0]); BE=-i0@GE@i0
    B0=i0-V; B0=(B0+B0.conj().T)/2
    w,U=np.linalg.eigh(B0)
    nullidx=np.where(np.abs(w)<tol)[0]
    if len(nullidx)==0: return None
    Nn=U[:,nullidx]; Q=U[:,[i for i in range(24) if i not in nullidx]]; wq=w[[i for i in range(24) if i not in nullidx]]
    P0plus=Q@np.diag(1/wq)@Q.conj().T
    NE=Nn.conj().T@BE@Nn; NE=(NE+NE.conj().T)/2
    ev,evec=np.linalg.eigh(NE); L=evec@np.diag(ev**-0.5)@evec.conj().T
    Ws=[];first=0
    for a in range(3):
        S=G1_series(res,a); Bs=sinv(S)   # B_d = (G1^-1)_d
        Bd=Bs[1]; Bdd=Bs[2]
        first=max(first,np.abs(Nn.conj().T@Bd@Nn).max())
        C=Nn.conj().T@(Bdd-2*Bd@P0plus@Bd)@Nn
        W=-E0*L@C@L; W=(W+W.conj().T)/2
        Ws.append(W)
    return dict(null=len(nullidx),first=first,W=Ws,Wsum=sum(Ws),NE=NE,nullvecs=Nn,gap=np.min(np.abs(wq)))

def group_roots(roots,tol=2e-5):
    grp=[]
    for j,r in sorted(roots,key=lambda t:t[1]):
        if grp and abs(grp[-1][0]-r)<tol: grp[-1][1].append(j)
        else: grp.append([r,[j]])
    return grp
def scan_g(Mall,g,N,side=+1,nscan=12,eta=0.02,verbose=True):
    V=Vmat(g,Mall)
    roots=find_levels(V,N,side,nscan=nscan,eta=eta)
    out=[]
    for js,r in sorted(roots,key=lambda t:t[1]):
        o=level_weights(r,V,N)
        if o is None: continue
        ev=np.linalg.eigvalsh(o['Wsum'])
        out.append((r,len(js),o['null'],o['first'],ev))
    return out

import scipy.sparse as sps, scipy.sparse.linalg as spl
def box_H(L,K,V6):
    """sparse relative generator on box |r_i|<=L minus origin, K total wave vector, bond term V6: dict r->4x4"""
    idx={}
    for x in range(-L,L+1):
        for y in range(-L,L+1):
            for z in range(-L,L+1):
                if (x,y,z)!=(0,0,0): idx[(x,y,z)]=len(idx)
    n=len(idx); rows=[];cols=[];vals=[]
    def hop(a,sgn):
        ph=np.exp(1j*K[a]/2)
        if sgn>0: return (kr(PA[a],I2)*ph-kr(I2,PA[a])/ph)/2j
        return (-kr(PA[a],I2)/ph+kr(I2,PA[a])*ph)/2j
    H=sps.lil_matrix((4*n,4*n),dtype=complex)
    blocks=[]
    for r,i in idx.items():
        for a in range(3):
            for sgn in (1,-1):
                rp=list(r); rp[a]+=sgn; rp=tuple(rp)
                if rp in idx:
                    j=idx[rp]
                    blocks.append((i,j,hop(a,sgn)))
        if r in V6: blocks.append((i,i,V6[r]))
    for i,j,m in blocks:
        for u in range(4):
            for v in range(4):
                if m[u,v]!=0:
                    rows.append(4*i+u); cols.append(4*j+v); vals.append(m[u,v])
    return sps.csr_matrix((vals,(rows,cols)),shape=(4*n,4*n))

import pickle, os
def make_tab(E,N):
    res=free_G(E,(0,0,0),N,axes=(0,1,2),order=1)
    S=[G1_series(res,a) for a in range(3)]
    GE=G1_E(res)
    return dict(E=E,N=N,G1=S[0][0],S=S,GE=GE)
def N_for(dl):
    return 48 if dl>=0.4 else (72 if dl>=0.08 else 100)
def herm_sqrt(A):
    w,U=np.linalg.eigh((A+A.conj().T)/2); return U@np.diag(np.sqrt(w))@U.conj().T
def weights_tab(tab,g,M,tolN=1e-7):
    G1=tab['G1']; S=tab['S']; GE=tab['GE']; E=tab['E']
    i0=np.linalg.inv(G1); BE=-i0@GE@i0
    V=g*M
    B0=i0-V; B0=(B0+B0.conj().T)/2
    w,U=np.linalg.eigh(B0)
    nidx=np.where(np.abs(w)<tolN)[0]
    if len(nidx)==0: return None
    qidx=[i for i in range(24) if i not in set(nidx)]
    Nn=U[:,nidx]; Q=U[:,qidx]; wq=w[qidx]
    P0=Q@np.diag(1/wq)@Q.conj().T
    NE=Nn.conj().T@BE@Nn; NE=(NE+NE.conj().T)/2
    ev,evec=np.linalg.eigh(NE); L=evec@np.diag(ev**-0.5)@evec.conj().T
    Ws=[]; first=0
    for a in range(3):
        Bs=sinv(S[a]); Bd=Bs[1]; Bdd=Bs[2]
        first=max(first,np.abs(Nn.conj().T@Bd@Nn).max())
        C=Nn.conj().T@(Bdd-2*Bd@P0@Bd)@Nn
        W=-E*L@C@L; Ws.append((W+W.conj().T)/2)
    return dict(null=len(nidx),first=first,W=Ws,Wsum=sum(Ws),gap=np.min(np.abs(wq)),nullvecs=Nn)
def levels_tab(tab,M,tauTol=1e-9):
    G1=tab['G1']; R=herm_sqrt(G1)
    T=R@M@R; tau,_=np.linalg.eigh((T+T.conj().T)/2)
    out=[]
    for t in tau:
        if t>1e-6:
            if out and abs(out[-1]-t)<tauTol*max(1,abs(t)): continue
            out.append(t)
    return [1/t for t in out]

def P_ex():
    P=np.zeros((24,24),complex)
    for i,r in enumerate(POS):
        j=POS.index(tuple(-x for x in r))
        P[4*j:4*j+4,4*i:4*i+4]=SWAP
    return P
PEX=P_ex()
def Bvals_K(E,V,N,K):
    res=free_G(E,K,N,axes=(),order=0)
    Gpp,Gp0,G0p,G00=blocks(res,'G')
    G1=Gpp-Gp0@np.linalg.inv(G00)@G0p
    B=np.linalg.inv(G1)-V
    B=(B+B.conj().T)/2
    return np.linalg.eigvalsh(B)
def roots_near(E0,V,N,K,width=0.2,nj=None,npts=9):
    """all roots of eigenvalue branches of B(E,K) in [E0-width,E0+width]"""
    Es=np.linspace(E0-width,E0+width,npts)
    vals=np.array([Bvals_K(E,V,N,K) for E in Es])
    out=[]
    for j in range(24):
        v=vals[:,j]
        for k in range(npts-1):
            if v[k]*v[k+1]<0:
                f=lambda E:Bvals_K(E,V,N,K)[j]
                out.append(brentq(f,Es[k],Es[k+1],xtol=1e-13,rtol=1e-14))
    return sorted(out)
