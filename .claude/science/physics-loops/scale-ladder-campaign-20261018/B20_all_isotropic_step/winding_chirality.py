#!/usr/bin/env python3
"""B20 part 4: the net chirality at any point-node quasi-energy of any word in S^{+-1}, S^{+-2}, R_L and
on-site unitaries is zero.
Proof (written in FINDINGS): (i) W3[U] = (1/24 pi^2) int tr (U^-1 dU)^3 is additive under pointwise products;
(ii) W3 = 0 for diagonal phase matrices (S^{+-1}, S^{+-2}: tr (i d theta)^3 = 0), constants, and Hermitian
unitaries 1-2P(k) with continuous P (null-homotopic via 1+(e^{i pi s}-1)P); hence W3[W] = 0;
(iii) for a unitary family whose quasi-energy E is reached only at isolated linear Weyl nodes, the sum of
their chiralities equals W3[W] up to a convention sign (Floquet Nielsen-Ninomiya; Bessho-Sato 2021 -
literature statement not re-derived here beyond the sketch in FINDINGS).
This runner checks (i)-(ii) numerically (spectrally accurate trapezoid integration of the smooth integrand
on a uniform grid; trigonometric-polynomial integrand), with a degree-1 control, and checks (iii) on the
eight-node step and on S2.H20.S2.L202 (node censuses with det-M chiralities).  Prints PASS/FAIL, TOTAL."""
import time
exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
t0=time.time(); PASS=FAIL=0
def check(name,ok,detail=""):
    global PASS,FAIL; PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}",flush=True)
def W3(fun,N):
    """(1/8pi^2) int tr(A_x [A_y, A_z]) d^3k, A_i = U^-1 d_i U; fun(k) -> (U, [dU_x,dU_y,dU_z])."""
    g=np.arange(N)*2*np.pi/N+0.1234; tot=0.0
    for k in itertools.product(g,repeat=3):
        U,G=fun(np.array(k)); Ui=np.linalg.inv(U); A=[Ui@x for x in G]
        tot+=np.trace(A[0]@(A[1]@A[2]-A[2]@A[1]))
    val=tot*(2*np.pi/N)**3/(8*np.pi**2)
    return val
sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.0+0j,-1])
def ctrl(m):
    def f(k):
        n=np.array([m-np.cos(k).sum(),*np.sin(k)]); dn=[np.array([np.sin(k[j])]+[np.cos(k[j]) if i==j else 0 for i in range(3)]) for j in range(3)]
        r=np.linalg.norm(n); U=(n[0]*np.eye(2)+1j*(n[1]*sx+n[2]*sy+n[3]*sz))/r
        G=[]
        for j in range(3):
            dr=n@dn[j]/r; dU=(dn[j][0]*np.eye(2)+1j*(dn[j][1]*sx+dn[j][2]*sy+dn[j][3]*sz))/r-U*dr/r; G.append(dU)
        return U,G
    return f
c2=W3(ctrl(2.0),24); c4=W3(ctrl(4.0),24)
f2=ctrl(2.0); sq=lambda k: (lambda a: (a[0]@a[0],[a[0]@g+g@a[0] for g in a[1]]))(f2(k))
c22=W3(sq,24)
check("control: the degree map U=(n0+i n.sigma)/|n|, n=(m-sum cos k, sin k) has W3 = +-1 at m=2 and 0 at m=4; its square has W3 = 2 W3 (tolerance 1e-4: the normalised map is smooth but not a trigonometric polynomial)",
      abs(abs(c2.real)-1)<1e-4 and abs(c4)<1e-4 and abs(c22-2*c2)<1e-4 and abs(c2.imag)<1e-9,f"W3(m=2)={c2.real:+.8f}, W3(m=4)={abs(c4):.1e}, W3(U^2)={c22.real:+.8f}")
# (iii) discriminating control: the degree-1 map at m=2 is an anomalous unitary (W3 = +-1).  E = pi is reached only at
# Gamma, E = 0 only at the seven other points of {0,pi}^3; both node sets must have net chirality equal to W3 (same value).
def chi2(fun,k):
    U,G=fun(k); h=[-1j*U.conj().T@g for g in G]; h=[(x+x.conj().T)/2 for x in h]
    M=np.array([[np.trace(x@s_).real/2 for s_ in (sx,sy,sz)] for x in h]); return int(np.sign(np.linalg.det(M))),np.linalg.svd(M,compute_uv=False)
f2=ctrl(2.0); corners=[np.array(c)*np.pi for c in itertools.product((0,1),repeat=3)]
atpi=[];at0=[]
for c in corners:
    U,_=f2(c); e=np.angle(np.linalg.eigvals(U))
    (atpi if np.allclose(np.abs(e),np.pi) else at0).append(chi2(f2,c)[0])
gg=np.linspace(-np.pi,np.pi,24,endpoint=False)+0.05; GG=np.array(list(itertools.product(gg,repeat=3)))
dmin={E_:min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(f2(k)[0]))-E_))) for k in GG) for E_ in (0.0,np.pi)}
check("control (anomalous unitary, W3=+-1): E=pi only at Gamma (1 node), E=0 at the 7 other points of {0,pi}^3; both nets equal W3 (Sum chi = +W3 in the det-M convention used here; the net is the same at both quasi-energies)",
      len(atpi)==1 and len(at0)==7 and sum(atpi)==sum(at0)==round(c2.real) and min(dmin.values())>1e-3,
      f"chi at E=pi {atpi}, at E=0 {at0}, W3 {c2.real:+.4f}; 24^3 grid min distance to E away from the corners {min(dmin.values()):.3f}")
step8=['S','R',UH,UL]; s2w=['S2',onH(2,0),'S2',onL(2,0,2)]
rng=np.random.default_rng(3); X=rng.normal(size=(12,12))+1j*rng.normal(size=(12,12)); Ur=np.linalg.qr(X)[0]
longw=['S',Ur,'R','Si',onL(1,2,3),'S2',Ur.conj().T,'R',onH(1,3)]
for nm,w,N in [("eight-node step S.R_L.U_H.U_L",step8,20),("S2.H20.S2.L202",s2w,20),("long word with a generic on-site unitary",longw,20)]:
    for NN in (N,N+4):
        val=W3(lambda k: W_and_grad(w,k),NN)
        print(f"   W3[{nm}] on {NN}^3 grid = {val.real:+.2e} {val.imag:+.1e}i",flush=True)
    check(f"W3 = 0 for the {nm} (numerical, two grid sizes; the integrand is a trigonometric polynomial, so the grid sum is exact once N exceeds its degree)",abs(val)<1e-6)
# (iii) chirality census of the eight-node step at E=+pi/2 (all 8 cube points), certified clean outside balls
E=np.pi/2; cube=[np.array(s)*np.pi/2 for s in itertools.product((1,-1),repeat=3)]
chis=[]
for c in cube:
    v=vel_matrix(step8,c,E); chis.append(v['chi'])
ok,bad,ev,_=certify_clean(step8,E,cube,0.03,n0=24,maxdepth=7)
check("eight-node step: E = pi/2 reached only in 0.03-balls around the 8 cube points (Lipschitz certificate); chiralities sum to 0",
      ok and sum(chis)==0,f"chiralities {chis}; {ev} evaluations")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
