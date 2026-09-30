"""P1 (SU(3) hot 4^4) and P4 (Hermitian-type flavour class), plus C-oddness of the singlet-direction phase."""
import numpy as np
from stag import *
out=[]
def rep(s): print(s); out.append(s)
rng=np.random.default_rng(20260929)
lat=Lat(4,4); V=lat.V; E3=np.kron(np.diag(lat.eps),np.eye(3)); I3=np.eye(3*V)
rep("=== SU(3) hot 4^4: eps direction vs taste-singlet direction (m=0.5, m5=0.2 m, 1 m, 5 m)")
maxphase_eps=0; maxdl=0; sing=[]; codd=0
for cfg in range(6):
    U=hot_su3_links(lat,rng)
    D=stag_D(lat,U).toarray()
    G=singlet_op(lat,U,True).toarray()
    Uc=U.conj()
    Dc=stag_D(lat,Uc).toarray(); Gc=singlet_op(lat,Uc,True).toarray()
    m=0.5
    for r in (0.2,1.0,5.0):
        a,ld=argdet(D+m*I3+1j*r*m*E3)
        ref=np.linalg.slogdet(D+np.sqrt(1+r*r)*m*I3)[1]
        maxphase_eps=max(maxphase_eps,abs((a+np.pi)%(2*np.pi)-np.pi)); maxdl=max(maxdl,abs(ld-ref))
    a_s,_=argdet(D+m*I3+1j*0.2*m*G)
    a_sc,_=argdet(Dc+m*I3+1j*0.2*m*Gc)
    sing.append(a_s); codd=max(codd,abs(a_s+a_sc))
    rep(f"cfg {cfg}: arg det[singlet, r=0.2] = {a_s:+.5f}   arg det[singlet] on U* = {a_sc:+.5f}")
rep(f"P1(SU(3)): max |arg det[eps direction]| over 6 configs x 3 ratios = {maxphase_eps:.2e}; max |dlog|det|| = {maxdl:.2e}")
rep(f"singlet direction: nonzero phases {np.round(sing,4)}; C-odd check max|a(U)+a(U*)| = {codd:.2e}")
rep("=== P4: Hermitian-type flavour class on SU(3) 4^4: even-site mass M_e (2x2 complex), odd-site M_o = M_e^dagger")
nf=2; worst_pos=1e9; worst_arg=0
Deven=(np.diag(lat.eps)>0)
for cfg in range(4):
    U=hot_su3_links(lat,rng); D=stag_D(lat,U).toarray()
    Mfl=rng.normal(size=(nf,nf))+1j*rng.normal(size=(nf,nf))
    Mfl*=0.7
    # mass operator on (site,color)x flavour
    Pe=np.kron(np.diag((lat.eps>0).astype(float)),np.eye(3)); Po=np.eye(3*V)-Pe
    Mass=np.kron(Pe,Mfl)+np.kron(Po,Mfl.conj().T)
    A=np.kron(D,np.eye(nf))+Mass
    a,ld=argdet(A)
    # control: non-Hermitian-type, same complex M on both sublattices
    Ac=np.kron(D,np.eye(nf))+np.kron(np.eye(3*V),Mfl)
    ac,_=argdet(Ac)
    # analytic value det(M M^dag x1 + 1 x B^dag B) is positive; compare with direct evaluation
    rep(f"cfg {cfg}: arg det[M_o=M_e^dag] = {a:+.2e}  (arg det M_e = {np.angle(np.linalg.det(Mfl)):+.3f});  control M_o=M_e: arg det = {ac:+.4f}")
    worst_arg=max(worst_arg,abs(a))
rep(f"P4: max |arg det| in the Hermitian-type class = {worst_arg:.2e}")
open("p1_su3_out.txt","w").write("\n".join(out)+"\n")
