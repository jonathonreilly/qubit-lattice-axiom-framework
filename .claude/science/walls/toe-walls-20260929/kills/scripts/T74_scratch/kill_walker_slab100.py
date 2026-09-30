"""Kill-check: (100) area coefficient of the induced-law lane's own 'walker sea':
H(k) = sigma . sin(k)  (2 coin states/site, Z^3), filled negative band (block 147 note, T1).
Chain in x for each transverse momentum (ky,kz): H = sigma_x (-i/2)(T-T^dag) + sigma_y sin ky + sigma_z sin kz.
Region = half the periodic chain (two cuts); eta = mean_k S_k / 2 (1 transverse site per cell)."""
import numpy as np, sys
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
def S_of_corr(C):
    nu=np.linalg.eigvalsh(C); nu=np.clip(nu,1e-14,1-1e-14)
    return float(-np.sum(nu*np.log(nu)+(1-nu)*np.log(1-nu)))
def eta100(Lx,Nt,offset=0.5,antiperiodic=True):
    ths=2*np.pi*(np.arange(Nt)+offset)/Nt
    ell=Lx//2; tot=0;cnt=0
    for a in ths:
        for b in ths:
            n=2*Lx; H=np.zeros((n,n),complex)
            for x in range(Lx):
                xp=(x+1)%Lx
                s=-1.0 if (antiperiodic and x==Lx-1) else 1.0
                # (-i/2) sx (T - T^dag): T shifts x->x+1 : H[x+1, x] += (-i/2) sx ... hermitian pair
                blk=(-0.5j)*sx*s
                # term  sum_x  psi_{x+1}^dag blk psi_x  + h.c.  gives sigma_x (-i/2)(T^dag... sign irrelevant to spectrum symmetry
                H[2*xp:2*xp+2,2*x:2*x+2]+=blk
                H[2*x:2*x+2,2*xp:2*xp+2]+=blk.conj().T
                H[2*x:2*x+2,2*x:2*x+2]+=np.sin(a)*sy+np.sin(b)*sz
            E,V=np.linalg.eigh(H)
            occ=V[:,E<0]
            P=occ@occ.conj().T
            sel=np.arange(2*ell)
            tot+=S_of_corr(P[np.ix_(sel,sel)]);cnt+=1
    return tot/cnt/2
if __name__=="__main__":
    Lx=int(sys.argv[1]);Nt=int(sys.argv[2])
    print(f"walker sea (100): Lx={Lx} Nt={Nt} eta={eta100(Lx,Nt):.5f}")
