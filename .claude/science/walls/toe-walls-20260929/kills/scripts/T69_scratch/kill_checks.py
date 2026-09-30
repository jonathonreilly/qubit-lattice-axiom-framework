"""Independent kill checks for T69 (own code; only the physical model H = sum_a sigma_a sin k_a, H_w = phi H phi,
phi = exp(u/2), u = eps cos(q.x), sea = all negative levels, is taken from the attack)."""
import numpy as np, scipy.sparse as sp, scipy.linalg as sl, itertools, json, sys

sx = np.array([[0,1],[1,0]],complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]],complex)
SIG = [sx, sy, sz]

def shift_op(L, a, dim=3):
    """T psi(x) = psi(x+e_a), antiperiodic on torus L^dim."""
    T1 = np.zeros((L,L)); 
    for i in range(L):
        j=(i+1)%L; T1[i,j] = -1.0 if i+1>=L else 1.0
    mats=[np.eye(L)]*dim; mats=list(mats); mats[a]=T1
    out=sp.csr_matrix(mats[0])
    for m in mats[1:]: out=sp.kron(out, sp.csr_matrix(m), format='csr')
    return out

def build_H(L, dim=3, s2=0.0):
    N=L**dim
    H=sp.csr_matrix((2*N,2*N),dtype=complex)
    for a in range(dim):
        T=shift_op(L,a,dim); Ti=T.T.conj()   # antiperiodic T is real orthogonal -> T^-1 = T^T
        hop=(T-Ti)/(2j)
        H = H + sp.kron(hop, sp.csr_matrix(SIG[a]), format='csr')
    return H

def sea_energy(H, u, N):
    phi=np.exp(np.repeat(u,2)/2)
    Hw=(sp.diags(phi)@H@sp.diags(phi)).toarray()
    ev=np.linalg.eigvalsh(Hw)
    return ev[ev<0].sum()

def coords(L,dim=3):
    return np.array(list(itertools.product(range(L),repeat=dim)))

def a2_ed_generic(L, mvec, eps=0.004):
    H=build_H(L); C=coords(L); N=L**3
    q=2*np.pi*np.array(mvec)/L
    E=lambda e: sea_energy(H, e*np.cos(C@q), N)
    E0=E(0.0)
    sec=lambda e:(E(e)+E(-e)-2*E0)/(2*e*e)
    v=(4*sec(eps)-sec(2*eps))/3
    return v/N, E0/N

def a2_bz_generic(N, mvec):
    """from-scratch BZ formula, antiperiodic mesh, general q = 2 pi m/N"""
    ks=2*np.pi*(np.arange(N)+0.5)/N
    kx,ky,kz=np.meshgrid(ks,ks,ks,indexing='ij')
    s=np.stack([np.sin(kx),np.sin(ky),np.sin(kz)],-1)
    A=np.linalg.norm(s,axis=-1); n=s/A[...,None]
    ax=(0,1,2)
    def sh(arr,sign):
        out=arr
        for ax_,m in enumerate(mvec):
            if m: out=np.roll(out, -sign*m, axis=ax_)
        return out
    sP=sh(s,+1); sM=sh(s,-1)
    AP=np.linalg.norm(sP,axis=-1); nP=sP/AP[...,None]
    diag=-A/8-(1/16)*np.einsum('...i,...i->...',n,sP+sM)
    pert=-(1/16)*(A-AP)**2*(1-np.einsum('...i,...i->...',n,nP))/(A+AP)
    return diag.mean()+pert.mean(), -A.mean()

if __name__=='__main__':
    out={}
    # ---- (a) generic-q ED vs BZ, L=6 and L=4
    rows=[]
    for L,m in [(6,(1,2,0)),(6,(1,1,2)),(6,(3,0,0)),(4,(1,1,0)),(6,(2,2,1))]:
        aed,c0=a2_ed_generic(L,m); abz,c0b=a2_bz_generic(L,m)
        rows.append(dict(L=L,m=m,ed=aed,bz=abz,rel=abs(aed-abz)/abs(abz)))
        print('generic-q ED vs BZ',rows[-1],flush=True)
    out['generic_q']=rows
    json.dump(out,open('kill_checks_out.json','w'),indent=1,default=float)
