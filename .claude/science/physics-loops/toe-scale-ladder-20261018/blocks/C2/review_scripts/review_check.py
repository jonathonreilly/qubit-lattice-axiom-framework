"""Independent reviewer checks for block C2.
Route: fermion frame rescaled to c_psi=1, photon speed eta; COULOMB gauge
(D00 = e^2 eta/|k|^2 instantaneous, D_ij transverse); gamma algebra done by hand
(see REVIEW.md) and re-verified here with explicit matrices; log coefficients from
exact sympy angular integrals over S^3 (shape-independent for degree -4 integrands).
Also: B4 / O_h x Z2 invariant counts by explicit projector averaging; flow numbers.
"""
import itertools, math
import numpy as np, sympy as sp
P=F=0
def chk(name, ok, info=""):
    global P,F
    P+=bool(ok); F+=(not ok)
    print(("PASS" if ok else "FAIL"), name, info)

# ---- 1. gamma algebra (Euclidean, {g_mu,g_nu}=2 delta) ----
s1=np.array([[0,1],[1,0]],complex); s2=np.array([[0,-1j],[1j,0]]); s3=np.diag([1,-1]).astype(complex)
Z=np.zeros((2,2)); I2=np.eye(2)
g=[np.block([[Z,I2],[I2,Z]])]+[np.block([[Z,-1j*s],[1j*s,Z]]) for s in (s1,s2,s3)]
chk("clifford", all(np.allclose(g[a]@g[b]+g[b]@g[a],2*(a==b)*np.eye(4)) for a in range(4) for b in range(4)))
rng=np.random.default_rng(1)
q=rng.normal(size=4); kh=rng.normal(size=3); kh/=np.linalg.norm(kh)
qs=sum(q[m]*g[m] for m in range(4)); gk=sum(kh[i]*g[i+1] for i in range(3))
lhs=sum(g[i]@qs@g[j]*((i==j)-kh[i-1]*kh[j-1]) for i in range(1,4) for j in range(1,4))
rhs=-2*g[0]*q[0]-2*np.dot(kh,q[1:])*gk
chk("transverse contraction = -2g0q0-2(khat.q)g.khat", np.allclose(lhs,rhs))
chk("g0 qslash g0 = g0q0 - g.q", np.allclose(g[0]@qs@g[0], g[0]*q[0]-sum(q[i]*g[i] for i in (1,2,3))))

# ---- 2. Coulomb-gauge log coefficients ----
eta=sp.symbols('eta',positive=True); x=sp.symbols('x')
c,s=sp.cos(x),sp.sin(x); Wn=c**2+eta**2*s**2
# closed forms: W=1+(eta^2-1)s^2, I1=int s^2/W=pi/(eta(eta+1)), I2=int s^4/W=(pi/2-I1)/(eta^2-1)
from scipy.integrate import quad
I1=sp.pi/(eta*(eta+1)); I2=(sp.pi/2-I1)/(eta**2-1)
for ev in (0.4,2.5):
    n1=quad(lambda t: math.sin(t)**2/(math.cos(t)**2+ev**2*math.sin(t)**2),0,math.pi)[0]
    n2=quad(lambda t: math.sin(t)**4/(math.cos(t)**2+ev**2*math.sin(t)**2),0,math.pi)[0]
    chk(f"I1,I2 closed forms vs quadrature eta={ev}", abs(n1-float(I1.subs(eta,ev)))<1e-10 and abs(n2-float(I2.subs(eta,ev)))<1e-10)
A0=sp.integrate(1-2*c**2,(x,0,sp.pi))/(4*sp.pi**3)
As=sp.integrate(-1+sp.Rational(2,3)*s**2,(x,0,sp.pi))/(4*sp.pi**3)
# sin^2(-2+4c^2)=2s^2-4s^4 ; sin^2(-2/3+4/3 s^2)
B0=(2*I1-4*I2)/(4*sp.pi**3); Bs=(-sp.Rational(2,3)*I1+sp.Rational(4,3)*I2)/(4*sp.pi**3)
# delta_0 = -eta (A0+B0) e^2, delta_s = -eta(As+Bs) e^2 ; dln c/dl = delta_s - delta_0
fC=sp.simplify(-eta*(As+Bs)+eta*(A0+B0))
fauthor=(eta-4/(1+eta)**2)/(6*sp.pi**2)
for ev in [sp.Rational(1,3),sp.Rational(1,2),1,2,5]:
    a=float(fC.subs(eta,ev)); b=float(fauthor.subs(eta,ev))
    chk(f"Coulomb-gauge dlnc/dl / e^2 at eta={ev}", abs(a-b)<1e-12*max(1,abs(b)), f"mine={a:.12g} author={b:.12g}")
chk("closed form equal symbolically", sp.simplify(fC-fauthor)==0, str(sp.factor(fC)))
lim=sp.limit(fC/eta,eta,sp.oo)
chk("Coulomb limit: dlnc/dl -> e^2 eta/(6pi^2) = 2 alpha_C/(3pi)", sp.simplify(lim-1/(6*sp.pi**2))==0)
chk("eta=1: Z0 = Zs (= e^2/8pi^2)", abs(float(sp.limit(-eta*(A0+B0),eta,1))-1/(8*math.pi**2))<1e-14 and abs(float(sp.limit(-eta*(As+Bs),eta,1))-1/(8*math.pi**2))<1e-14)

# ---- 3. photon: frame rescaling of standard vacuum polarisation, independent bookkeeping ----
cc=sp.symbols('c',positive=True)
# x'=x/c, A0'=A0, Aj'=c Aj => E'=cE, B'=c^2 B, d^4x'=d^4x/c^3
eps_coef=sp.simplify(cc**2/cc**3); muinv_coef=sp.simplify(cc**4/cc**3)
chk("d eps/dl ∝ 1/c, d(1/mu)/dl ∝ c", eps_coef==1/cc and muinv_coef==cc)
e2,Nf=sp.symbols('e2 N_f',positive=True)
v=eta  # c=1
dlnv=sp.Rational(1,2)*(Nf*muinv_coef.subs(cc,1)/(6*sp.pi**2)*e2/v - Nf*eps_coef.subs(cc,1)/(6*sp.pi**2)*e2*v)
dlneta=dlnv - e2*fC
d=sp.symbols('d')
lin=sp.simplify(sp.diff(dlneta.subs(eta,sp.exp(d)),d).subs(d,0))
al=sp.symbols('alpha',positive=True)
chk("linearised d delta/dl = -(2alpha/3pi)(Nf+2)", sp.simplify(lin.subs(e2,4*sp.pi*al)+2*al*(Nf+2)/(3*sp.pi))==0, str(sp.simplify(lin.subs(e2,4*sp.pi*al))))
dd=sp.diff(dlneta,eta)
ok=all(float(dd.subs({e2:1,Nf:n,eta:t}))<0 for n in (1,3,8) for t in np.linspace(0.02,50,400))
chk("d(dln eta/dl)/d eta <0 on (0.02,50): unique attractive fixed point eta=1", ok)
# second-order drift of c_gamma^2 c_psi (Nf=1)
inv=sp.series((2*dlnv+e2*fC).subs({Nf:1}).subs(eta,1+d),d,0,3).removeO()
chk("d ln(c_g^2 c_psi)/dl vanishes at O(delta), nonzero O(delta^2)", sp.simplify(inv.coeff(d,1))==0 and sp.simplify(inv.coeff(d,2))!=0, str(sp.simplify(inv)))

# ---- 4. numbers ----
aIR=1/137.036
def ratio(l,Nf):
    aUV=1/(1/aIR-2*Nf*l/(3*math.pi)); return (aIR/aUV)**((Nf+2)/Nf), 1/aUV
r1,inv1=ratio(51,1); r3,_=ratio(51,3); r8,_=ratio(51,8)
chk("N_f=1,l=51 factor 0.781", abs(r1-0.7813)<5e-4, f"{r1:.5f}, 1/alpha_UV={inv1:.3f}")
chk("N_f=3 0.637, N_f=8 0.287", abs(r3-0.637)<1e-3 and abs(r8-0.287)<1e-3, f"{r3:.4f} {r8:.4f}")
chk("ln(M_Pl/m_e) = 51.53", abs(math.log(1.22e19/0.51099895e-3)-51.53)<0.01, f"{math.log(1.22e19/0.51099895e-3):.3f}")
chk("cutoff mismatch 1e-15/0.781=1.28e-15", abs(1e-15/r1-1.28e-15)<0.01e-15)
# small nonlinear integration (Nf=1) with my own RK4, eta_UV=1.2
def rhs(y):
    et,ie2=y; e=1/ie2
    fm=(et-4/(1+et)**2)/(6*math.pi**2)
    dle=0.5*(e/et/(6*math.pi**2)-e*et/(6*math.pi**2))-e*fm
    return np.array([et*dle,(et+1/et)/(12*math.pi**2)])
# integrate from UV to IR; choose e^2_UV so that at eta=1 we'd hit alpha_IR (declared as author did)
y=np.array([1.2,inv1/(4*math.pi)]); h=51/5000
for _ in range(5000):
    k1=rhs(y);k2=rhs(y+h/2*k1);k3=rhs(y+h/2*k2);k4=rhs(y+h*k3);y=y+h/6*(k1+2*k2+2*k3+k4)
chk("RK4 eta_UV=1.2 -> eta_IR≈1.1525 (author 1.152478)", abs(y[0]-1.152478)<2e-4, f"{y[0]:.6f}")

# ---- 5. group theory ----
def signed_perms(n):
    for p in itertools.permutations(range(n)):
        for sg in itertools.product([1,-1],repeat=n):
            M=np.zeros((n,n)); 
            for i in range(n): M[p[i],i]=sg[i]
            yield M
B4=list(signed_perms(4)); chk("|B4|=384",len(B4)==384)
pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
def L2(M):
    R=np.zeros((6,6))
    for a,(i,j) in enumerate(pairs):
        for b,(k,l) in enumerate(pairs):
            R[b,a]=M[k,i]*M[l,j]-M[l,i]*M[k,j]
    return R
def ninv_sym(G,rep):
    n=rep(G[0]).shape[0]; acc=0
    for M in G:
        R=rep(M); acc+=(np.trace(R)**2+np.trace(R@R))/2
    return round(acc/len(G))
def ninv_t2(G):
    return round(sum(np.trace(M)**2 for M in G)/len(G))
prop=[M for M in B4 if np.linalg.det(M)>0]
cub=[M for M in B4 if abs(M[0,0])==1]   # O_h (signed perms of xyz) x Z2(t)
chk("B4 invariant rank-2 tensors = 1", ninv_t2(B4)==1)
chk("O_h x Z2(t) invariant rank-2 tensors = 2", ninv_t2(cub)==2)
chk("B4 invariant quadratic forms on Lambda^2 = 1", ninv_sym(B4,L2)==1)
chk("proper B4 invariant quadratic forms on Lambda^2 = 2 (F^2, F Ftilde)", ninv_sym(prop,L2)==2)
chk("O_h x Z2(t) invariant quadratic forms on Lambda^2 = 2 (E^2,B^2)", ninv_sym(cub,L2)==2)
# a time-mixing rotation (B4 element) maps E^2-B^2 to something different -> forces equality
chk("|cub| = 96", len(cub)==96)
Oprop=[M for M in cub if M[0,0]==1 and np.linalg.det(M[1:,1:])>0]   # proper O only (Lattice axiom), no time reflection
chk("|O|=24", len(Oprop)==24)
chk("O (proper, no T) rank-2 tensors = 2", ninv_t2(Oprop)==2)
chk("O (proper, no T) quadratic forms on Lambda^2 = 3 (E^2,B^2,E.B)", ninv_sym(Oprop,L2)==3)
OT=[M for M in cub if np.linalg.det(M[1:,1:])>0]   # O x Z2(t)
chk("O x Z2(t) quadratic forms on Lambda^2 = 2", ninv_sym(OT,L2)==2)

# ---- 6. W2 lattice dispersions (direct small-k numerical pole) ----
xi=1.2; kk=1e-3
E=2*math.asinh(math.sqrt(xi**2*(2*math.sin(kk/2))**2/4))
chk("W2 gauge pole: c_gamma = sqrt(beta_s/beta_t)=xi", abs(E/kk-xi)<1e-5, f"{E/kk:.7f}")
E=math.asinh(math.sin(kk)/1.0)
chk("W2 fermion pole zeta0=1: c_psi=1", abs(E/kk-1)<1e-6)
print(f"TOTAL: PASS={P} FAIL={F}")
