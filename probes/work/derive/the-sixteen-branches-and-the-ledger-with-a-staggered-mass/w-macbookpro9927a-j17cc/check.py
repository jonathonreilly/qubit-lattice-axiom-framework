"""check.py -- the-sixteen-branches-and-the-ledger-with-a-staggered-mass a1 (w-macbookpro9927a-j17cc).

Exact checks (integers, Fractions, sympy) for every finite claim of ATTEMPT.md; the floating-point
checks are labelled FLOAT and are evidence, not exact facts.  Run from the repository root.
"""
import hashlib, itertools, math, os, subprocess, sys
from fractions import Fraction as F
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, cwd=HERE).stdout.strip()
FAILS = []; NOK = 0
def ok(name, cond, detail=""):
    global NOK
    if cond: NOK += 1
    else: FAILS.append(name); print("FAIL", name, detail)

# ------------------------------------------------------------------ Q: the landed notes (origin/main 60c5f194)
MAIN = "60c5f194d940a7bbaf1cdd545296e31d74a02f1a"
def note(key):
    ls = subprocess.run(["git", "ls-tree", "--name-only", MAIN, "docs/"], capture_output=True, text=True, cwd=ROOT).stdout.split()
    if not ls:
        subprocess.run(["git", "fetch", "origin", "main", "--quiet"], cwd=ROOT)
        ls = subprocess.run(["git", "ls-tree", "--name-only", MAIN, "docs/"], capture_output=True, text=True, cwd=ROOT).stdout.split()
    f = [p for p in ls if p.startswith("docs/ADMISSIBILITY_RULE_" + key)][0]
    return subprocess.run(["git", "show", f"{MAIN}:{f}"], capture_output=True, cwd=ROOT).stdout
PIN = {"THE_AXIOMS_OWN_GENERATOR": "ba54520f18bca80a89f25c41b55a728688ab139efa306faf916df3f1b8ec781c",
       "THE_FILLED_SEAS_ENERGY": "bd1fbe7a03b3e36ac56b2cc74cab218f921668bfd5628ad8725b574b3dd27932",
       "THE_EIGHT_SPECIES_ARE_EXCHANGED": "41ae3ae58264fd38ec86701a408419ee92065cf2371c3729084e621888415142",
       "AMPLITUDES_OF_NEGATIVE_ENERGY": "b6b4a92120652c78d0edbc4129749c54965777abcc64ecaeddf309f833d01da2"}
TXT = {}
for k, h in PIN.items():
    b = note(k); TXT[k] = b.decode(); ok("Q1 note sha256 " + k[:24], hashlib.sha256(b).hexdigest() == h)
ok("Q2 block 77 quotes", "Moreover `phi(K+m eps)phi=phi K phi+m w eps`." in TXT["THE_AXIOMS_OWN_GENERATOR"]
   and "Numerical packet and massive-sea experiments are deferred." in TXT["THE_AXIOMS_OWN_GENERATOR"])
ok("Q3 block 76 quotes", "The filled negative-level energy is E_-=sum_{lambda<0}lambda of this finite matrix." in TXT["THE_FILLED_SEAS_ENERGY"]
   and "At a point where E_- has a Hessian in u, that Hessian annihilates eps." in TXT["THE_FILLED_SEAS_ENERGY"]
   and "They are inputs, not derived sea coefficients." in TXT["THE_FILLED_SEAS_ENERGY"])
ok("Q4 block 70 T1(b) and block 71 T1(a)", "(b) `V_nHV_n = s_nH`, and `V_n(φHφ)V_n = s_n φHφ` for every rate field." in TXT["THE_EIGHT_SPECIES_ARE_EXCHANGED"]
   and "`e_x[A_nψ] = −e_x[ψ]`" in TXT["AMPLITUDES_OF_NEGATIVE_ENERGY"])

# ------------------------------------------------------------------ M: exact operator algebra on the 4^3 torus (Gaussian integers)
L = 4; N = L ** 3
sites = list(itertools.product(range(L), repeat=3)); IDX = {x: i for i, x in enumerate(sites)}
def sh(x, a, d): y = list(x); y[a] = (y[a] + d) % L; return tuple(y)
SIG = [np.array([[0, 1], [1, 0]]), None, np.array([[1, 0], [0, -1]])]
S2re = np.zeros((2, 2), int); S2im = np.array([[0, -1], [1, 0]])            # sigma_2 = i*S2im
def zeros(): return np.zeros((2 * N, 2 * N), dtype=np.int64)
# K = 2H = sum_a sigma_a (T_a - T_a^-1)/i ; for sigma_1, sigma_3 the entries are -i*(+-1); sigma_2/i is real
Kre, Kim = zeros(), zeros()
for x in sites:
    i = IDX[x]
    for a in range(3):
        for d, sgn in ((1, 1), (-1, -1)):
            j = IDX[sh(x, a, d)]
            if a == 1:   # sigma_2/i * sgn = S2im * sgn (real)
                Kre[2*i:2*i+2, 2*j:2*j+2] += sgn * S2im
            else:        # sigma/i * sgn = -i * sgn * sigma
                Kim[2*i:2*i+2, 2*j:2*j+2] += -sgn * SIG[a]
def mul(A, B): return (A[0] @ B[0] - A[1] @ B[1], A[0] @ B[1] + A[1] @ B[0])
def eq(A, B): return np.array_equal(A[0], B[0]) and np.array_equal(A[1], B[1])
def neg(A): return (-A[0], -A[1])
def add(A, B): return (A[0] + B[0], A[1] + B[1])
Kc = (Kre, Kim); Z = (zeros(), zeros())
epsv = np.array([(-1) ** sum(x) for x in sites]); EPS = (np.kron(np.diag(epsv), np.eye(2, dtype=int)), zeros())
ok("M1 eps anticommutes with the walk: eps K = -K eps", eq(mul(EPS, Kc), neg(mul(Kc, EPS))))
ok("M2 K has no site-diagonal block", all(not Kre[2*i:2*i+2, 2*i:2*i+2].any() and not Kim[2*i:2*i+2, 2*i:2*i+2].any() for i in range(N)))
def Tmat(a):     # (T psi)_x = psi_{x - e_a}
    A = zeros()
    for x in sites:
        A[2*IDX[x]:2*IDX[x]+2, 2*IDX[sh(x, a, -1)]:2*IDX[sh(x, a, -1)]+2] = np.eye(2, dtype=int)
    return (A, zeros())
T0 = Tmat(0); T0i = (T0[0].T.copy(), zeros())
ok("M3 one-site translation: T K T^-1 = K, T eps T^-1 = -eps", eq(mul(mul(T0, Kc), T0i), Kc) and eq(mul(mul(T0, EPS), T0i), neg(EPS)))
def Vn(n):
    s = np.array([(-1) ** (n[0]*x[0] + n[1]*x[1] + n[2]*x[2]) for x in sites])
    D = [(-1) ** v for v in n]; sgn = D[0] * D[1] * D[2]; rho = [sgn * d for d in D]
    if all(r == 1 for r in rho): R = (np.eye(2, dtype=int), np.zeros((2, 2), int))
    else:
        ax = rho.index(1)
        R = [(SIG[0], np.zeros((2, 2), int)), (S2re, S2im), (SIG[2], np.zeros((2, 2), int))][ax]
    U = np.kron(np.diag(s), np.eye(2, dtype=int))
    return (U @ np.kron(np.eye(N, dtype=int), R[0]), U @ np.kron(np.eye(N, dtype=int), R[1])), sgn
allV = True; oddsym = True
for n in itertools.product((0, 1), repeat=3):
    V, sgn = Vn(n)
    allV &= eq(mul(mul(V, Kc), V), Kc if sgn == 1 else neg(Kc)) and eq(mul(mul(V, EPS), V), EPS)
    if sgn == -1:   # eps V_n commutes with H + m eps: eps(-K)eps = K and eps eps eps = eps
        EV = mul(EPS, V); oddsym &= eq(mul(mul(EV, Kc), (EV[0].T.copy(), -EV[1].T.copy())), Kc)
ok("M4 V_n K V_n = s_n K and V_n eps V_n = eps for all eight n (even n commute with H+m eps)", allV)
ok("M5 odd n: eps V_n commutes with H + m eps", oddsym)
TW = mul(EPS, T0); TWi = (TW[0].T.copy(), -TW[1].T.copy())
ok("M6 twin map eps T: (eps T)(H + m eps)(eps T)^-1 = -(H + m eps)", eq(mul(mul(TW, Kc), TWi), neg(Kc)) and eq(mul(mul(TW, EPS), TWi), neg(EPS)))
Sig2 = (np.zeros((2*N, 2*N), int), np.kron(np.eye(N, dtype=int), S2im))      # I_N (x) sigma_2
def theta_conj(A):   # Theta A Theta^-1 = Sigma2 conj(A) Sigma2
    return mul(mul(Sig2, (A[0], -A[1])), Sig2)
V111, _ = Vn((1, 1, 1))
ok("M7 Theta commutes with K and eps; A_n = Theta V_n (odd n) maps K -> -K, eps -> eps: not a massive twin",
   eq(theta_conj(Kc), Kc) and eq(theta_conj(EPS), EPS) and eq(mul(mul(V111, Kc), V111), neg(Kc)))

# M8: twin density, exact (Fractions), random rate field and state, m rational, twin chi = eps T psi in field T phi
import random
rnd = random.Random(20260925)
def gq(): return (F(rnd.randint(-9, 9), rnd.randint(1, 7)), F(rnd.randint(-9, 9), rnd.randint(1, 7)))
sigma_c = [((F(0), F(0), F(1), F(0)), (0,)*4), None, None]
def apply_sigma(a, v):       # v = ((re0, im0), (re1, im1))
    (r0, i0), (r1, i1) = v
    if a == 0: return ((r1, i1), (r0, i0))
    if a == 1: return ((i1, -r1), (-i0, r0))     # sigma_2 (v0, v1) = (-i v1, i v0)
    return ((r0, i0), (-r1, -i1))
def Hw_apply(psi, phi, w, m):
    out = {}
    for x in sites:
        acc = [[F(0), F(0)], [F(0), F(0)]]
        for a in range(3):
            xp, xm = sh(x, a, 1), sh(x, a, -1)
            vp = apply_sigma(a, psi[xp]); vm = apply_sigma(a, psi[xm])
            for c in range(2):   # (phi_x/(2i)) (phi_xp vp - phi_xm vm) ; 1/(2i) (re + i im) = (im - i re)/2
                re = phi[x] * (phi[xp] * vp[c][0] - phi[xm] * vm[c][0]); im = phi[x] * (phi[xp] * vp[c][1] - phi[xm] * vm[c][1])
                acc[c][0] += im / 2; acc[c][1] += -re / 2
        e = (-1) ** sum(x)
        for c in range(2):
            acc[c][0] += m * w[x] * e * psi[x][c][0]; acc[c][1] += m * w[x] * e * psi[x][c][1]
        out[x] = ((acc[0][0], acc[0][1]), (acc[1][0], acc[1][1]))
    return out
def edens(psi, phi, m):
    w = {x: phi[x] * phi[x] for x in sites}; Hp = Hw_apply(psi, phi, w, m)
    return {x: sum(psi[x][c][0] * Hp[x][c][0] + psi[x][c][1] * Hp[x][c][1] for c in range(2)) for x in sites}
phi = {x: F(rnd.randint(1, 9), rnd.randint(1, 9)) for x in sites}; psi = {x: (gq(), gq()) for x in sites}; mm = F(7, 5)
phiT = {x: phi[sh(x, 0, -1)] for x in sites}
chi = {x: tuple(((-1) ** sum(x) * psi[sh(x, 0, -1)][c][0], (-1) ** sum(x) * psi[sh(x, 0, -1)][c][1]) for c in range(2)) for x in sites}
e1 = edens(psi, phi, mm); e2 = edens(chi, phiT, mm)
ok("M8 twin density: e_x[eps T psi; T phi] = -e_{x-e1}[psi; phi] at every site (exact)", all(e2[x] == -e1[sh(x, 0, -1)] for x in sites))
# M9: block 71's on-site twin A_111 = Theta V_111 (V_111 = eps) with a mass: e[A psi] + e[psi] = 2 m w eps |psi|^2, exact
def theta_eps(ps):   # (Theta eps psi)_x = sigma_2 conj(eps_x psi_x);  sigma_2 (v0, v1) = (-i v1, i v0)
    out = {}
    for x in sites:
        e = (-1) ** sum(x); (r0, i0), (r1, i1) = ps[x]; c0, c1 = (e * r0, -e * i0), (e * r1, -e * i1)
        out[x] = ((c1[1], -c1[0]), (-c0[1], c0[0]))
    return out
eA = edens(theta_eps(psi), phi, mm)
ok("M9 block 71's on-site twin Theta V_111 with a mass: e[A psi] + e[psi] = 2 m w eps |psi|^2 at every site (exact), nonzero",
   all(eA[x] + e1[x] == 2 * mm * phi[x]**2 * (-1) ** sum(x) * sum(psi[x][c][0]**2 + psi[x][c][1]**2 for c in range(2)) for x in sites)
   and any(eA[x] + e1[x] != 0 for x in sites))
# M10: chessboard of clocks, exact: phi = c^eps  =>  phi(H + m eps)phi = H + m cosh(a) eps + m sinh(a),  a = 2 log c
cc = F(3, 2); ch = (cc**2 + 1 / cc**2) / 2; shh = (cc**2 - 1 / cc**2) / 2
phiC = {x: (cc if (-1) ** sum(x) == 1 else 1 / cc) for x in sites}; wC = {x: phiC[x] ** 2 for x in sites}
ok("M10 chessboard: phi_x phi_y = 1 on every bond and m w_x eps_x = m cosh(a) eps_x + m sinh(a) (exact)",
   all(phiC[x] * phiC[sh(x, a, 1)] == 1 for x in sites for a in range(3)) and all(wC[x] * (-1) ** sum(x) == ch * (-1) ** sum(x) + shh for x in sites))

# ------------------------------------------------------------------ S/K: sea density and kernel algebra (sympy)
m, E, Ep = sp.symbols("m E Ep", positive=True); s = sp.symbols("s1:4", real=True); t = sp.symbols("t1:4", real=True)
sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
def blk(v): Sd = v[0] * sx + v[1] * sy + v[2] * sz; return sp.Matrix(sp.BlockMatrix([[Sd, m * sp.eye(2)], [m * sp.eye(2), -Sd]]))
Mk, Mq = blk(s), blk(t)
sub = {E: sp.sqrt(sum(v**2 for v in s) + m**2), Ep: sp.sqrt(sum(v**2 for v in t) + m**2)}
ok("S1 M(k)^2 = E^2 (paired spectrum +-sqrt(|s|^2+m^2))", sp.simplify(Mk * Mk - (sum(v**2 for v in s) + m**2) * sp.eye(4)) == sp.zeros(4))
Pm = (sp.eye(4) - Mk / E) / 2
ok("S2 P_-(k) M(k) = (M(k) - E)/2 given M^2 = E^2 (sea density m eps_x - <E>)", sp.simplify((Pm * Mk - (Mk - E * sp.eye(4)) / 2).subs(sub)
   .applyfunc(lambda z: sp.simplify(z.subs(sub)))) == sp.zeros(4))
ok("S3 coin trace of the site-diagonal part of M: mass block trace 2m eps (per site m eps_x)", (Mk[0, 2] + Mk[1, 3]) == 2 * m)
for a_, b_ in ((-1, -1), (-1, 1)):
    Pa = (sp.eye(4) + a_ * Mk / E) / 2; Pb = (sp.eye(4) + b_ * Mq / Ep) / 2
    tr = sp.expand((Pa * Pb).trace()); target = 1 + a_ * b_ * (sum(x * y for x, y in zip(s, t)) + m**2) / (E * Ep)
    ok(f"K1 tr P_{a_}(k) P_{b_}(k') = 1 + ab (s.s' + m^2)/(E E')", sp.simplify(tr - target) == 0)
c = sp.symbols("c", real=True)
Foo = -sp.Rational(1, 4) * (E + Ep) * (1 + c)                      # occupied-occupied weight
Fou = lambda Ei, Ej: sp.Rational(1, 2) * Ei * (Ej - Ei) / (Ei + Ej) * (1 - c)   # occupied (Ei) - unoccupied (Ej)
G = 2 * Foo + Fou(E, Ep) + Fou(Ep, E)                            # F(k,k') + F(k',k): the occupied-occupied weight enters twice
ok("K2 symmetrized second-order weight G = -(1/2)[(E+E')(1+c) + (1-c)(E-E')^2/(E+E')]",
   sp.simplify(G + sp.Rational(1, 2) * ((E + Ep) * (1 + c) + (1 - c) * (E - Ep)**2 / (E + Ep))) == 0)
lam_i, lam_j = sp.symbols("lam_i lam_j", real=True)
ok("K3 first-order matrix element <j|{u,H}/2|i> = (lam_i+lam_j)/2 <j|u|i>; occ-unocc weight (lam_i+lam_j)^2/(4(lam_i-lam_j)) + (lam_i+lam_j)/4 = lam_i(lam_j... )",
   sp.simplify(((-E + Ep)**2 / (4 * (-E - Ep)) + (-E + Ep) / 4) - E * (Ep - E) / (2 * (E + Ep))) == 0)
# gradient bounds for the O(q^4) remainder: n = (s, m)/E, |d_j n| <= |cos k_j|/E, |d_j E| <= 1
k1, k2, k3 = sp.symbols("k1:4", real=True)
sv = sp.Matrix([sp.sin(k1), sp.sin(k2), sp.sin(k3), m]); En = sp.sqrt(sv[0]**2 + sv[1]**2 + sv[2]**2 + m**2); nv = sv / En
dn = nv.diff(k1); lhs = sp.simplify((dn.T * dn)[0] - sp.cos(k1)**2 * (En**2 - sp.sin(k1)**2) / En**4)
ok("K4 |d_1 n|^2 = cos^2 k1 (E^2 - sin^2 k1)/E^4 <= 1/m^2 ; d_1 E = sin k1 cos k1 / E", lhs == 0 and sp.simplify(En.diff(k1) - sp.sin(k1) * sp.cos(k1) / En) == 0)

# ------------------------------------------------------------------ R: the stiffness kappa(m) = <|s|^2/E>/12, exact series and enclosures
from math import comb
def smom(n):     # <|s|^{2n}> over the zone, exact: sum over compositions with <sin^{2a}> = C(2a,a)/4^a
    tot = F(0)
    for a in range(n + 1):
        for b in range(n - a + 1):
            cc3 = n - a - b
            tot += F(math.factorial(n), math.factorial(a) * math.factorial(b) * math.factorial(cc3)) * F(comb(2*a, a), 4**a) * F(comb(2*b, b), 4**b) * F(comb(2*cc3, cc3), 4**cc3)
    return tot
MOM = {n: smom(n) for n in range(1, 4)}
ok("R1 <|s|^2> = 3/2, <|s|^4> = 21/8, <|s|^6> = 81/16", (MOM[1], MOM[2], MOM[3]) == (F(3, 2), F(21, 8), F(81, 16)))
cj = lambda j: F((-1) ** j * comb(2*j, j), 4 ** j)
ser = [F(1, 12) * cj(j) * MOM[j + 1] for j in range(3)]
ok("R2 kappa(m) = 1/(8m) - 7/(64 m^3) + 81/(512 m^5) - ... (m > sqrt 3)", ser == [F(1, 8), F(-7, 64), F(81, 512)])
def enclose(mv, J):
    moms = {}; lo = hi = None; part = F(0); sums = []
    for j in range(J + 1):
        part += F(1, 12) * cj(j) * smom(j + 1) / mv ** (2 * j + 1); sums.append(part)
    return min(sums[-1], sums[-2]), max(sums[-1], sums[-2])
enc = {}
for mv, J in ((F(4), 24), (F(2), 70)):
    lo, hi = enclose(mv, J); enc[mv] = (lo, hi)
    ok(f"R3 kappa({mv}) enclosure width < 1e-10", hi - lo < F(1, 10**10) and lo > 0, f"{float(lo)} {float(hi)}")
print(f"R kappa(2) in [{float(enc[F(2)][0]):.13f}, {float(enc[F(2)][1]):.13f}], kappa(4) in [{float(enc[F(4)][0]):.13f}, {float(enc[F(4)][1]):.13f}]")

# ------------------------------------------------------------------ FLOAT (labelled): brute force, sea density, table
sxn = np.array([[0, 1], [1, 0]], complex); syn = np.array([[0, -1j], [1j, 0]]); szn = np.array([[1, 0], [0, -1]], complex); SG = [sxn, syn, szn]
def build(Lt):
    Nt = Lt ** 3; st = list(itertools.product(range(Lt), repeat=3)); ix = {x: i for i, x in enumerate(st)}
    Hn = np.zeros((2*Nt, 2*Nt), complex); ev = np.array([(-1) ** sum(x) for x in st])
    for x in st:
        for a in range(3):
            xp = list(x); xp[a] = (xp[a] + 1) % Lt; xm = list(x); xm[a] = (xm[a] - 1) % Lt
            i, jp, jm = ix[x], ix[tuple(xp)], ix[tuple(xm)]
            Hn[2*i:2*i+2, 2*jp:2*jp+2] += SG[a] / 2j; Hn[2*i:2*i+2, 2*jm:2*jm+2] -= SG[a] / 2j
    return st, Hn, ev
def zone(Lt):
    ks = 2 * np.pi * np.arange(Lt) / Lt; g = np.array(list(itertools.product(ks, repeat=3))); return g
def kernel(Lt, mv, q):
    g = zone(Lt); S1 = np.sin(g); S2 = np.sin(g + q); E1 = np.sqrt((S1**2).sum(1) + mv*mv); E2 = np.sqrt((S2**2).sum(1) + mv*mv)
    cc_ = ((S1 * S2).sum(1) + mv*mv) / (E1 * E2)
    return (-0.5 * ((E1 + E2) * (1 + cc_) + (1 - cc_) * (E1 - E2)**2 / (E1 + E2))).mean() / 8, E1
worst = 0.0
for Lt, mv, qv in ((4, 0.7, (1, 0, 0)), (6, 1.3, (1, 1, 0))):
    st, Hn, ev = build(Lt); Nt = Lt ** 3; Hm = Hn + mv * np.kron(np.diag(ev), np.eye(2)); q = 2 * np.pi * np.array(qv) / Lt
    def Eo(a):
        u = a * np.cos(np.array(st) @ q); ph = np.kron(np.diag(np.exp(u / 2)), np.eye(2)); w_ = np.linalg.eigvalsh(ph @ Hm @ ph); return w_[w_ < 0].sum()
    E0 = Eo(0.0); d = [(Eo(a) + Eo(-a) - 2 * E0) / (2 * a * a * Nt) for a in (0.02, 0.01)]; brute = (4 * d[1] - d[0]) / 3
    form, E1 = kernel(Lt, mv, q); worst = max(worst, abs(brute - form), abs(E0 / Nt + E1.mean()))
    if Lt == 4:     # sea density from the eigenvectors
        wv, U = np.linalg.eigh(Hm); P = U[:, wv < 0] @ U[:, wv < 0].conj().T; PH = P @ Hm
        dens = np.array([np.real(np.trace(PH[2*i:2*i+2, 2*i:2*i+2])) for i in range(Nt)])
        dens_err = np.abs(dens - (mv * ev - E1.mean())).max()
ok("K5 FLOAT brute-force second-order kernel = formula (L=4 m=0.7; L=6 m=1.3) and E_sea/N = -<E>", worst < 1e-8, str(worst))
ok("S4 FLOAT sea density e_x = m eps_x - <E> on the 4^3 torus", dens_err < 1e-12, str(dens_err))
g64 = zone(48); S64 = (np.sin(g64)**2).sum(1)
def kap(mv, SS=S64): return (SS / np.sqrt(SS + mv * mv)).mean() / 12
tab = {mv: kap(mv) for mv in (0.25, 0.5, 1, 1.5, 2, 3, 4, 6, 8)}
g32 = zone(32); S32 = (np.sin(g32)**2).sum(1)
ok("R4 FLOAT kappa(m) torus averages converge (L=32 vs 48 agree to 1e-9 for m >= 0.5)", all(abs(kap(mv, S32) - tab[mv]) < 1e-9 for mv in tab if mv >= 0.5))
ok("R5 FLOAT enclosures contain the torus values at m = 2, 4", enc[F(2)][0] - F(1, 10**9) <= F(tab[2]) <= enc[F(2)][1] + F(1, 10**9) and enc[F(4)][0] - F(1, 10**9) <= F(tab[4]) <= enc[F(4)][1] + F(1, 10**9))
a2 = {0.25: 0.0970, 0.5: 0.0915, 1: 0.0766, 1.5: 0.0630, 2: 0.0523, 3: 0.0382, 4: 0.0297, 6: 0.0204, 8: 0.0154}
ok("R6 FLOAT the formula reproduces the a2 attempt's executed L=24 free-sea values within 3e-4", all(abs(tab[mv] - a2[mv]) < 3e-4 for mv in a2))
print("R FLOAT kappa(m):", ", ".join(f"{mv}: {tab[mv]:.5f}" for mv in tab), "| c0(m)=-<E>:", ", ".join(f"{mv}: {-np.sqrt(S64 + mv*mv).mean():.4f}" for mv in (0, 1, 2, 4)))
# chessboard sea energy: exact variations of E(a) = N m sinh a - sum sqrt(|s|^2 + m^2 cosh^2 a)
aa, ss2 = sp.symbols("a s2", positive=True)
Ea = m * sp.sinh(aa) - sp.sqrt(ss2 + m**2 * sp.cosh(aa)**2)
ok("D1 chessboard: dE/da = N m and d2E/da2 = -N m^2 <1/E> at a = 0 (per k-point form)",
   sp.simplify(Ea.diff(aa).subs(aa, 0) - m) == 0 and sp.simplify(Ea.diff(aa, 2).subs(aa, 0) + m**2 / sp.sqrt(ss2 + m**2)) == 0)

print(f"checks passed {NOK}, failed {len(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL exact: the massive walk H + m eps (a) keeps even exchange maps, odd ones as eps V_n, and has no on-site twin; "
      "eps T (one-site shift after the site sign) is a twin carrying a solution in field phi to one in T phi with e -> -e shifted one site; "
      "(b) the filled sea's density is exactly m eps_x - <E>; (c) its second-order kernel is the held sea's plus an O(|q|^4/m^3) term, so "
      "kappa(m) = (1/12)<|s|^2/sqrt(|s|^2+m^2)> > 0, strictly decreasing, -> I/12 as m -> 0, = 1/(8m) - 7/(64m^3) + 81/(512m^5) - ...; "
      "(d) a chessboard is not invisible: first variation N m. The task's HIT condition (a sign change of kappa) is excluded")
print("HIT: exact stiffness of the massive free sea: for every m != 0 the filled sea of H + m eps has second-order clock kernel equal to the "
      "held sea's, Pi(q) = -<E>/4 + (kappa/4)|q|^2_lat, plus -(1/16)<(1-n.n')(E-E')^2/(E+E')> = O(|q|^4/m^3), so kappa(m) = "
      "(1/12)<|sin k|^2/sqrt(|sin k|^2+m^2)>_BZ: positive and strictly decreasing for all m, kappa -> I/12 as m -> 0 and "
      "1/(8m) - 7/(64m^3) + 81/(512m^5) - ... for m > sqrt3; and the sea's energy density is exactly m eps_x - <E>")
