"""Independent T14 kill check.  Own implementation, not importing the attacker's code except for comparison.
Models: naive Dirac fermion (4-comp, m) + real scalar (mu), Yukawa g phi psibar psi, Euclidean lattice,
spatial step 1, time step eps, tree speeds tuned to 1.
Fermion inverse propagator M(P)=i gamma.s(P)+m ; self-energy Sigma(P)=g^2 int D(k) S(P-k).
We compute BOTH pieces of the massive-fermion speed: the gamma-vector part (attacker) and the scalar part
of the self-energy (m-dependent, omitted by attacker).
Speed of fermion from  det: (Z_nu s_nu)^2 + M_eff(P)^2 = 0, M_eff = m - g^2 B(P), B(P)=int D(k) m/den(P-k).
To O(g^2): coefficient of P_nu^2 : Z_nu^2 - 2 m g^2 b_nu ; so log v = (fx - ft) - m (b_x - b_t)   (c_psi=1)
where b_nu = (1/2) d^2 B/dP_nu^2 at P=0.
Everything by FINITE DIFFERENCE in the external momentum (independent of attacker's analytic derivatives).
"""
import numpy as np

def grids(Nt,Ns,eps):
    th=2*np.pi*np.arange(Nt)/Nt; ks=2*np.pi*np.arange(Ns)/Ns
    return th,ks

def mk(Nt,Ns,eps,m,mu,shift=(0,0,0,0)):
    """Return functions evaluated on shifted grids for numerical P-derivatives.  external momentum P=(w,p,0,0) physical."""
    pass

def integrals(Nt,Ns,eps,m,mu,w=0.0,p=0.0,lam=1.0,cpsi=1.0):
    # loop momentum k=(theta_k/eps, kx,ky,kz) on torus; fermion carries P-k
    th=2*np.pi*np.arange(Nt)/Nt; ks=2*np.pi*np.arange(Ns)/Ns
    T,X,Y,Z=np.meshgrid(th,ks,ks,ks,indexing='ij')
    # scalar propagator D(k)
    Dinv=mu**2+lam*4*np.sin(T/2)**2/eps**2+4*np.sin(X/2)**2+4*np.sin(Y/2)**2+4*np.sin(Z/2)**2
    D=1/Dinv
    # fermion with momentum P-k : theta' = eps*w - T ; spatial p-k
    Tq=eps*w-T; Xq=p-X; Yq=-Y; Zq=-Z
    s0=cpsi*np.sin(Tq)/eps; s1=np.sin(Xq); s2=np.sin(Yq); s3=np.sin(Zq)
    den=m**2+s0**2+s1**2+s2**2+s3**2
    meas=1.0/(eps*Nt*Ns**3)
    F0=meas*np.sum(D*s0/den); F1=meas*np.sum(D*s1/den)
    B=meas*np.sum(D*m/den)
    return F0,F1,B

def fermion_coeffs(Nt,Ns,eps,m,mu,h=0.05):
    # F_nu(P)= f_nu * P_nu + ...  ; use odd finite difference for first derivative in P_nu; B second derivative even
    F0p,_,Bw=integrals(Nt,Ns,eps,m,mu,w=+h)
    F0m,_,Bw2=integrals(Nt,Ns,eps,m,mu,w=-h)
    _,F1p,Bp=integrals(Nt,Ns,eps,m,mu,p=+h)
    _,F1m,Bp2=integrals(Nt,Ns,eps,m,mu,p=-h)
    _,_,B0=integrals(Nt,Ns,eps,m,mu)
    ft=(F0p-F0m)/(2*h); fx=(F1p-F1m)/(2*h)
    bt=(Bw+Bw2-2*B0)/(h*h)/2; bx=(Bp+Bp2-2*B0)/(h*h)/2
    return ft,fx,bt,bx

if __name__=="__main__":
    import sys
    for (eps,m,mu) in [(1.0,0.5,0.5),(0.9,0.5,0.5),(0.5,0.5,0.5),(0.12,0.5,0.5),(0.12,0.25,0.25)]:
        Nt=int(round(24/eps)); Ns=24
        ft,fx,bt,bx=fermion_coeffs(Nt,Ns,eps,m,mu)
        print(f"eps={eps} m={m} mu={mu}: ft={ft:.6f} fx={fx:.6f} a_psi(attacker form)={fx-ft:.6f}  bt={bt:.5f} bx={bx:.5f}  mass-part -m(bx-bt)={-m*(bx-bt):.6f}  a_psi(full)={fx-ft-m*(bx-bt):.6f}")
