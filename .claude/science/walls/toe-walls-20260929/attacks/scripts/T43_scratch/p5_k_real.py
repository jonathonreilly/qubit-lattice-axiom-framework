"""S5: K-reality of the Hamiltonian-language surface (09-03 note algebra) and oddness in m5 of the Euclid phase."""
import numpy as np, itertools
from stag import *
out=[]
def rep(s): print(s); out.append(s)
X_=np.array([[0,1],[1,0]],complex); Y_=np.array([[0,-1j],[1j,0]]); Z_=np.diag([1,-1]).astype(complex); I_=np.eye(2,dtype=complex)
def kron(*a):
    M=np.eye(1,dtype=complex)
    for x in a: M=np.kron(M,x)
    return M
Gam=[kron(Y_,I_,I_),kron(Z_,Y_,I_),kron(Z_,Z_,Y_)]
Xi=[kron(X_,I_,I_),kron(Z_,X_,I_),kron(Z_,Z_,X_)]
eps=kron(Z_,Z_,Z_); M2=kron(X_,Y_,X_)
Xc=1j*Gam[0]@Gam[1]@Gam[2]
def H(q,m1=0.0,m2=0.0):
    return sum((1+np.cos(q[a]))*Xi[a]+np.sin(q[a])*Gam[a] for a in range(3))+m1*eps+m2*M2
rep(f"M2 = i Xi1 Xi2 Xi3: dev {np.abs(M2-1j*Xi[0]@Xi[1]@Xi[2]).max():.1e}; X M2 = i eps: dev {np.abs(Xc@M2-1j*eps).max():.1e}")
rep(f"M2 conj = -M2: dev {np.abs(M2.conj()+M2).max():.1e}; eps, Xi_a real: {max(np.abs(eps.imag).max(),*[np.abs(x.imag).max() for x in Xi]):.1e}; Gamma_a imaginary: {max(np.abs(g.real).max() for g in Gam):.1e}")
rng=np.random.default_rng(1); worst0=0; worst1=0
for _ in range(20):
    q=rng.uniform(-np.pi,np.pi,3)
    worst0=max(worst0,np.abs(H(q,0.7,0.0).conj()-H(-q,0.7,0.0)).max())
    worst1=max(worst1,np.abs(H(q,0.7,0.3).conj()-H(-q,0.7,0.3)).max())
rep(f"K-covariance conj(H(q))=H(-q): m2=0 dev {worst0:.1e}; m2=0.3 dev {worst1:.2f}  (real-space H real iff m2=0)")
# node spectrum and taste-splitting term odd in m2
ev=np.linalg.eigvalsh(H(np.array([np.pi]*3),0.3,0.4))
rep(f"node spectrum (m1=.3,m2=.4): {np.round(ev,6)}  (expect +-0.5 x4)")
p=np.array([0.4,0.2,-0.3]); e_plus=np.sort(np.linalg.eigvalsh(H(np.pi+p,0.3,0.4))**2); e_minus=np.sort(np.linalg.eigvalsh(H(np.pi+p,0.3,-0.4))**2)
rep(f"E^2 set at p, m2=+0.4 vs m2=-0.4 equal as sets: dev {np.abs(e_plus-e_minus).max():.1e}")
# chiral rotation at the node only
th=0.7
R=np.cos(th/2)*np.eye(8)+1j*np.sin(th/2)*Xc
Hn=lambda m1,m2: H(np.array([np.pi]*3),m1,m2)
rot=R@Hn(0.5,0)@R.conj().T
rep(f"node: chiral rotation e^(i th X/2) maps m1*eps -> cos th m1 eps + sin th m1 M2 ? dev {np.abs(rot-Hn(0.5*np.cos(th),0.5*np.sin(th))).max():.1e} (or -sin)")
rot2=R@H(np.array([np.pi+0.5,np.pi+0.3,np.pi-0.4]),0.5,0)@R.conj().T
tgt=H(np.array([np.pi+0.5,np.pi+0.3,np.pi-0.4]),0.5*np.cos(th),0.5*np.sin(th))
rep(f"away from node the rotation is NOT a symmetry (Wilson-like Xi terms): dev {min(np.abs(rot2-tgt).max(),np.abs(rot2-H(np.array([np.pi+0.5,np.pi+0.3,np.pi-0.4]),0.5*np.cos(th),-0.5*np.sin(th))).max()):.2f}")
# Euclid phase odd in m5 (2D flux, Gamma_f)
lat=Lat(8,2); U=u1_flux_links_2d(lat,1); D=stag_D(lat,U).toarray(); G=gamma_f_2d(lat,U).toarray()
ap,_=argdet(D+0.2*np.eye(lat.V)+1j*0.05*G); am,_=argdet(D+0.2*np.eye(lat.V)-1j*0.05*G)
rep(f"Euclid singlet phase odd in m5: a(+)={ap:+.5f} a(-)={am:+.5f}")
open("p5_out.txt","w").write("\n".join(out)+"\n")
