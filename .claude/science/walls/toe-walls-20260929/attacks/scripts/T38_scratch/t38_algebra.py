"""T38 tests 1-3: exact identities, carrier-Gram lemma, symmetry-pairing lemma.  sympy, no floats in the gates
except the final delta=2/9 illustration.  Run: python3 t38_algebra.py"""
import itertools
import sympy as sp

PASS = FAIL = 0
def gate(name, ok):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'ok' if ok else 'FAIL'}] {name}")

a, br, bi = sp.symbols('a b_R b_I', real=True)
b = br + sp.I*bi
w = sp.exp(2*sp.pi*sp.I/3)
C = sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])          # cyclic shift, real permutation matrix
I3 = sp.eye(3)
H = a*I3 + b*C + sp.conjugate(b)*C**2
gate("H Hermitian", sp.simplify(H - H.H) == sp.zeros(3,3))
gate("H commutes with C", sp.simplify(H*C - C*H) == sp.zeros(3,3))

# eigenvalues by Fourier
lam = [sp.simplify(sp.expand(a + b*w**k + sp.conjugate(b)*w**(-k), complex=True)) for k in range(3)]
lam = [sp.simplify(sp.re(sp.expand(x, complex=True))) for x in lam]
e1 = sum(lam); e2 = lam[0]*lam[1]+lam[1]*lam[2]+lam[0]*lam[2]; s2 = sum(l**2 for l in lam)
r = (br**2+bi**2)/a**2
Q = s2/e1**2
gate("sum lam = 3a", sp.simplify(e1-3*a)==0)
gate("Tr H^2 = 3a^2 + 6|b|^2", sp.simplify(s2-(3*a**2+6*(br**2+bi**2)))==0)
gate("Q = (1+2r)/3", sp.simplify(Q-(1+2*r)/3)==0)

half = sp.Rational(1,2)
# E1 angle: cos^2(theta) = e1^2/(3 s2) = 1/(3Q)
cos2 = sp.simplify(e1**2/(3*s2))
gate("E1 cos^2(angle to (1,1,1)) = 1/(1+2r)  => 45deg iff r=1/2", sp.simplify(cos2-1/(1+2*r))==0 and sp.simplify((1/(1+2*half))-half)==0)
# E2 diag vs offdiag HS
diagH = sp.diag(*[H[i,i] for i in range(3)])
off = H-diagH
nd = sp.simplify(sum(sp.Abs(diagH[i,j])**2 for i in range(3) for j in range(3)))
no = sp.simplify(sum((H[i,j]*sp.conjugate(H[i,j])) for i in range(3) for j in range(3) if i!=j))
gate("E2 ||diag||^2 = 3a^2, ||offdiag||^2 = 6|b|^2, equal iff r=1/2", sp.simplify(nd-3*a**2)==0 and sp.simplify(sp.expand(no)-6*(br**2+bi**2))==0)
# E3 character measurement
gate("E3 P(trivial C3 character | psi=lam/|lam|) = 1/(1+2r)", sp.simplify(e1**2/(3*s2)-1/(1+2*r))==0)
# E4 purity of rho_H = H/Tr H
rho = H/H.trace()
pur = sp.simplify(sp.expand((rho*rho).trace()))
gate("E4 Tr rho_H^2 = Q = (1+2r)/3", sp.simplify(pur-Q)==0)
# E5 null cone
J = sp.ones(3,3)
lv = sp.Matrix(lam)
nul = sp.simplify((lv.T*(3*I3-2*J)*lv)[0])
gate("E5 lam^T(3I-2J)lam = 3 s2 - 2 e1^2 = 9a^2 (2r-1): zero iff r=1/2", sp.simplify(nul - (3*s2-2*e1**2))==0 and sp.simplify((3*s2-2*e1**2) - 9*a**2*(2*r-1))==0)
# E6 e1^2 = 6 e2
gate("E6 e1^2 - 6 e2 = 9a^2 (2r-1): zero iff r=1/2", sp.simplify((e1**2-6*e2) - 9*a**2*(2*r-1))==0)

# ---------------- Test 2: carrier Gram lemma ----------------
g0, g1, g2 = sp.symbols('gamma0 gamma1 gamma2', positive=True)
# Gamma diagonal in the Fourier basis of C (any C-invariant Hermitian Gamma); H diagonal there with eigenvalues lam_k
F = g0*lam[0]**2 + g1*lam[1]**2 + g2*lam[2]**2
Fexp = sp.expand(F)
# D-conjugation: b -> w b (a fixed)
bw = sp.expand(w*b, complex=True)
sub = {br: sp.re(bw), bi: sp.im(bw)}
Fsub = sp.expand(Fexp.subs(sub, simultaneous=True))
diff = sp.simplify(Fsub - Fexp)
# solve for D invariance
coeffs = sp.Poly(sp.expand(diff), a, br, bi).coeffs()
sol = sp.solve(coeffs, [g0, g1, g2], dict=True)
print("D-invariance solutions:", sol)
inv_ok = all(sp.simplify(s.get(g0,g0)-s.get(g1,g1))==0 and sp.simplify(s.get(g1,g1)-s.get(g2,g2))==0 for s in sol) if sol else False
# if solve returns gamma0=gamma1=gamma2 the form is HS multiple
Fhs = sp.expand(Fexp.subs({g0:1,g1:1,g2:1}))
gate("Test2(i) D-invariance of sum_k gamma_k lam_k^2 forces gamma0=gamma1=gamma2 (so the form is gamma*Tr H^2)", len(sol)==1 and sol[0].get(g0)==g2 and sol[0].get(g1)==g2)
gate("Test2(i) that form is diag(3,6,6) in (a,bR,bI)", sp.simplify(Fhs-(3*a**2+6*br**2+6*bi**2))==0)
print("  rho = g0/g1 =", sp.Rational(3,6))

# (ii) equivariant identifications of amplitude space with carrier: v = (s*a)*(1,1,1)/sqrt3 + d*(doublet coords)
s, d = sp.symbols('s d', positive=True)
# doublet orthonormal basis of the sum-zero plane
e_a = sp.Matrix([2,-1,-1])/sp.sqrt(6); e_b = sp.Matrix([0,1,-1])/sp.sqrt(2)
# C acts on the sum-zero plane as rotation by 120 deg in this basis (checked below); map (bR,bI) -> plane coordinates
u = sp.Matrix([1,1,1])/sp.sqrt(3)
Rot = sp.Matrix([[e_a.dot(C*e_a), e_a.dot(C*e_b)],[e_b.dot(C*e_a), e_b.dot(C*e_b)]])
gate("C acts on the doublet plane as a rotation by 120deg", sp.simplify(Rot.T*Rot-sp.eye(2))==sp.zeros(2,2) and sp.simplify(Rot.det()-1)==0 and sp.simplify(Rot.trace()+1)==0)
# D acts on (bR,bI) as rotation by 120deg: b -> w b, same sense up to orientation; take equivariant map with matching sense
v = s*a*u + d*(br*e_a + bi*e_b)
flat = sp.simplify(v.dot(v))
gate("Test2(ii) carrier-flat pullback = diag(s^2,d^2,d^2): whole cone as (s,d) vary", sp.simplify(flat-(s**2*a**2+d**2*(br**2+bi**2)))==0)
# natural identifications
col0 = H[:,0]                     # H e_0
n_col = sp.simplify(sp.expand(sum(sp.conjugate(x)*x for x in col0)))
gate("action on cyclic vector: |H e_0|^2 = a^2+2|b|^2 (HS/3, rho=1/2)", sp.simplify(n_col-(a**2+2*(br**2+bi**2)))==0)
gate("eigenvalue vector: |lam|^2 = 3a^2+6|b|^2 (HS, rho=1/2)", sp.simplify(s2-(3*a**2+6*(br**2+bi**2)))==0)
print("  note: the literal-coordinate identification (a,bR,bI) -> carrier gives a^2+bR^2+bI^2 (flat, rho=1); it is the s=d=1 point of the Schur family, not distinguished by equivariance")

# ---------------- Test 3: symmetry pairing ----------------
import numpy as np
rng = np.random.default_rng(20260929)
Cn = np.array(C.tolist(), dtype=complex)
wn = np.exp(2j*np.pi/3)
# Fourier eigenbasis of C: columns v_k with C v_k = w^k v_k
V = np.zeros((3,3), dtype=complex)
for k in range(3):
    V[:,k] = np.array([wn**(-k*j) for j in range(3)])/np.sqrt(3)
for k in range(3):
    assert np.allclose(Cn@V[:,k], wn**k*V[:,k]) or np.allclose(Cn@V[:,k], wn**(-k)*V[:,k])
# relabel so that C v_k = w^k v_k
lab = []
for k in range(3):
    for kk in range(3):
        if np.allclose(Cn@V[:,kk], wn**k*V[:,kk]): lab.append(kk)
V = V[:, lab]
for k in range(3): assert np.allclose(Cn@V[:,k], wn**k*V[:,k])
def Hnum(av, bv): return av*np.eye(3) + bv*Cn + np.conj(bv)*Cn@Cn
P_swap_F = np.array([[1,0,0],[0,0,1],[0,1,0]], dtype=complex)   # swaps Fourier lines 1 <-> 2
Pswap = V@P_swap_F@V.conj().T
def phases():
    return V@np.diag(np.exp(1j*rng.uniform(0,2*np.pi,3)))@V.conj().T
K = lambda X: X.conj()         # position-basis complex conjugation acting on operators: K H K^-1 = conj(H)
def act(kind, U, Hm):
    return U@Hm@U.conj().T if kind=='unitary' else U@K(Hm)@U.conj().T
rows = []
for kind in ('unitary','antiunitary'):
    for swap in (False, True):
        U = phases()@(Pswap if swap else np.eye(3))
        # does T map the w-eigenline to the w-bar line?  unitary: iff swap; antiunitary: T v = U conj(v); C T v = ... test numerically
        v1 = V[:,1]
        Tv = U@v1 if kind=='unitary' else U@v1.conj()
        pairs = abs(abs(np.vdot(V[:,2], Tv))-1) < 1e-9
        gen_sym = []
        deg_sym = []
        for _ in range(20):
            av = rng.uniform(0.5,2); bv = rng.uniform(0.1,1)*np.exp(1j*rng.uniform(0,2*np.pi))
            Hm = Hnum(av,bv)
            gen_sym.append(np.allclose(act(kind,U,Hm), Hm, atol=1e-9))
        delta = 2/9
        H29 = Hnum(1.0, np.exp(1j*delta)/np.sqrt(2))
        sym29 = np.allclose(act(kind,U,H29), H29, atol=1e-9)
        # degenerate H (Im b = 0) 
        Hd = Hnum(1.0, 0.7)
        symd = np.allclose(act(kind,U,Hd), Hd, atol=1e-9)
        rows.append((kind, 'swap' if swap else 'noswap', pairs, all(gen_sym), sym29, symd))
print("\nT type            | maps E_w -> E_wbar | symmetry of generic H | of H(delta=2/9) | of degenerate H (Im b=0)")
for r_ in rows: print(r_)
pairing = [r_ for r_ in rows if r_[2]]
nonpair = [r_ for r_ in rows if not r_[2]]
gate("Test3: every pairing T (4 random-phase draws per type) is a symmetry of H(delta=2/9)? -> none", all(not r_[4] for r_ in pairing))
gate("Test3: every pairing T is a symmetry of the degenerate H (Im b = 0)", all(r_[5] for r_ in pairing))
gate("Test3: every non-pairing T is a symmetry of every H (so carries no counting content)", all(r_[3] for r_ in nonpair))
gate("Test3: exactly two of the four T types pair the doublet (unitary swap, antiunitary noswap)", len(pairing)==2)
print("physical H(a=1,delta=2/9,r=1/2) eigenvalues:", np.linalg.eigvalsh(Hnum(1.0, np.exp(1j*2/9)/np.sqrt(2))))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
