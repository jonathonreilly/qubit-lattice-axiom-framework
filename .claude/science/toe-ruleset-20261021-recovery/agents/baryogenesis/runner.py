#!/usr/bin/env python3
"""Baryon excess under CL-1..CL-5 plus candidate four-mode terms: which Sakharov ingredients do the rules supply?
(supplied model; exact charge algebra; finite many-body diagnostic; estimates; no physical identification)
 A  exact rationals: sphaleron conversion, a sequestered nu^c (Dirac neutrinos, forced by Z4), the B - L each candidate
    Delta N = 4 term leaves in the sphaleron sector, rephasing count of the coefficient phases
 B  single-particle symmetries of the copy-massed CL-2 tick: T and particle-hole broken, but PH x C4, T x C4 and the
    CPT-type map (chiral x inversion) exact, each half-tick separately
 C  many-body tick on the 2^3 torus twisted by K = (pi,0,0) (fixed by inversion and by C4 about x; 8 modes, 256 states):
    C' = lift of PH x C4 is an exact unitary symmetry that sends N -> 8 - N; four-mode term classes; real structure;
    asymmetry dynamics from a C'-invariant thermal start; stationary states; asymmetry per event vs step
 D  estimates against eta_B = 6.1e-10
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import sympy as sp
from scipy.linalg import expm, null_space, schur

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())

# =============================== A. exact charge bookkeeping ===============================
print('== A. exact rationals (symmetric electroweak phase, chemical potentials; content supplied)')
Q, u, d, l, e, phi, n = sp.symbols('Q u d l e phi n')
def ratio(Nf, NH, extra=None, nu_in_L=False):
    eqs = [sp.Eq(u, Q + phi), sp.Eq(d, Q - phi), sp.Eq(e, l - phi), sp.Eq(3 * Q + l, 0), sp.Eq(Nf * (Q + 2 * u - d - l - e) + 2 * NH * phi, 0)]
    unk = [u, d, e, l, phi] + ([n] if extra is not None else [])
    s = sp.solve(eqs + ([extra] if extra is not None else []), unk, dict=True)[0]
    B = Nf * (2 * Q + u + d); L = Nf * (2 * l + e + (n if nu_in_L else 0))
    return sp.simplify((B / (B - L)).subs(s))
okA1 = all(ratio(f, h) == sp.Rational(8 * f + 4 * h, 22 * f + 13 * h) for f, h in ((1, 1), (3, 1), (3, 2), (4, 1)))
check('A1 [theorem] Yukawa + sphaleron + hypercharge equilibrium: B = (8Nf+4NH)/(22Nf+13NH) (B - L_SM); 28/79 at Nf = 3, NH = 1',
      okA1 and ratio(3, 1) == sp.Rational(28, 79), f'B/(B-L_SM) = {ratio(3, 1)}')
r_yuk = ratio(3, 1, sp.Eq(n, l + phi), True); r_uddn = ratio(3, 1, sp.Eq(-u - 2 * d - n, 0), True)
check('A2 [theorem] nu^c (Y = 0) out of equilibrium is a separate reservoir: B = (28/79)(B - L_SM) whatever it holds, so a pure nu^c asymmetry ((nu^c)^4 alone) '
      'gives B = 0 exactly; with nu^c equilibrated (Dirac Yukawa or a fast uddn) B = (1/4)(B - L)',
      r_yuk == sp.Rational(1, 4) and r_uddn == sp.Rational(1, 4), f'nu^c equilibrated: {r_yuk} (Yukawa), {r_uddn} (uddn)')
# left-handed Weyl fields: B - L and mode number N = 3B + L of each conjugate field (n^c = conjugate of the right-handed neutrino)
BLc = {'u^c': sp.Rational(-1, 3), 'd^c': sp.Rational(-1, 3), 'e^c': 1, 'n^c': 1}
Nc = {'u^c': -1, 'd^c': -1, 'e^c': -1, 'n^c': -1}
terms = {'(n^c)^4': ['n^c'] * 4, 'u^c d^c d^c n^c': ['u^c', 'd^c', 'd^c', 'n^c'], 'u^c u^c d^c e^c': ['u^c', 'u^c', 'd^c', 'e^c']}
tab = {}
for k, fs in terms.items():
    dN = sum(Nc[f] for f in fs); dBL = sum(BLc[f] for f in fs); dBLsm = sum(BLc[f] for f in fs if f != 'n^c')
    tab[k] = (abs(dN), abs(dBL), abs(dBLsm), sp.Rational(28, 79) * abs(dBLsm))
check('A3 [theorem] per net event (|dN|, |d(B-L)|, |d(B-L)_SM|, |dB| after sphalerons): (n^c)^4 (4,4,0,0); uddn (4,0,1,28/79); uude (4,0,0,0). '
      'All three are Z4-allowed (dN = 0 mod 4), the Majorana n^c n^c (dN = 2) is not; uddn moves B - L out of the sphaleron sector into the sequestered nu^c, so a B - L-conserving rule can still leave B',
      tab['(n^c)^4'] == (4, 4, 0, 0) and tab['u^c d^c d^c n^c'] == (4, 0, 1, sp.Rational(28, 79)) and tab['u^c u^c d^c e^c'] == (4, 0, 0, 0)
      and all(v[0] % 4 == 0 for v in tab.values()) and sum(Nc[f] for f in ('n^c', 'n^c')) % 4 == 2)
# rephasing: free tick conserves each species number (U(1) per species: u, d, e, nu); charge vectors of the operators
Cm = sp.Matrix([[0, 0, 0, -4], [-1, -2, 0, -1], [-2, -1, -1, 0]])
check('A4 [theorem] rephasing count: the species U(1)s (u, d, e, nu) of the free tick remove one phase from each of (n^c)^4, uddn, uude (charge rank 3 = 3 operators), '
      'so one coefficient per operator content leaves no CP-odd invariant; every further shape of the same content (point-splittings, placements) adds one',
      Cm.rank() == 3)

# =============================== B. single-particle tick with copy mass ===============================
print('== B. copy-massed CL-2 tick: which antiunitaries survive (random K set, three steps)')
C = np.array(list(itertools.product((0, 1), repeat=3))); cc0 = C - 0.5
def Jm(j):
    dd = int(round(2 * j + 1)); m = j - np.arange(dd); Jp = np.zeros((dd, dd), complex)
    for a in range(1, dd): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    nv = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(nv[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
def hop(dist2, sign):
    H = np.zeros((8, 8), complex)
    for a in range(8):
        for b in range(8):
            if round(float(np.sum((C[a] - C[b]) ** 2))) == dist2: g_ = XI[a].conj() @ XI[b]; H[a, b] = sign * g_ / abs(g_) / np.sqrt(3)
    return H
W = hop(1, -1.0); Fh = hop(2, 1.0); I8 = np.eye(8); S = np.diag([(-1.0) ** int(x.sum()) for x in C]).astype(complex)
s3 = -S @ Fh; PA = (I8 + s3) / 2; PB = (I8 - s3) / 2
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def axang(R):
    a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
def img(R, i): return int(np.argmin(np.sum(abs(cc0 - R @ cc0[i]), 1)))
def Grot(R):
    nv, a = axang(R); Dm = expm(-1j * a * sum(nv[k] * J3[k] for k in range(3))); G = np.zeros((8, 8), complex)
    for i in range(8): k = img(R, i); G[k, i] = XI[k].conj() @ Dm @ XI[i]
    return G
Gs = [Grot(R) for R in rots]; ODD = [nrm(G @ S @ G.conj().T - S) > 1e-9 for G in Gs]
iC3 = [i for i, R in enumerate(rots) if abs(np.trace(R)) < 1e-9 and np.allclose(axang(R)[0], np.ones(3) / np.sqrt(3))][0]
R4 = [R for R in rots if np.allclose(R, [[1, 0, 0], [0, 0, -1], [0, 1, 0]])][0]
OM = np.exp(2j * np.pi / 3)
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def halves(K, st, mu, M):   # even cube, then odd cube; copy mass M/2 on copy A (C3 character w) in each half-tick
    Ue = expm(-1j * ((st - mu / 2) * I8 - M / 2 * PA) @ W)
    Uo = Dg(K).conj().T @ expm(1j * ((st + mu / 2) * I8 + M / 2 * PA) @ W) @ Dg(K)
    return Ue, Uo
def tick(K, st, mu, M): Ue, Uo = halves(K, st, mu, M); return Uo @ Ue
def solve(pairs, conj):     # V with V X(*) = Y V for all pairs
    A = np.vstack([np.kron(I8, (X.conj() if conj else X).T) - np.kron(Y, I8) for X, Y in pairs])
    ns = null_space(A, rcond=1e-9); return [ns[:, i].reshape(8, 8) for i in range(ns.shape[1])]
KR = np.random.default_rng(7).uniform(-np.pi, np.pi, size=(10, 3))
counts, half_counts, e0s, keep = {}, {}, {}, []
for st, mu, M in ((np.pi / 2, 0.0, 0.5), (0.3, 0.1, 0.5), (0.04, 0.02, 0.3)):
    g = lambda K: tick(K, st, mu, M)
    keep.append(max(nrm(L @ g(K) @ L.conj().T - g(R @ K)) for L, R, o in zip(Gs, rots, ODD) if not o for K in KR[:2]) < 1e-10
                and min(nrm(L @ g(K) @ L.conj().T - g(R @ K)) for L, R, o in zip(Gs, rots, ODD) if o for K in KR[:2]) > 0.1)
    counts[st] = [len(solve([(g(K), Y(K)) for K in KR], cj)) for Y, cj in
                  ((lambda K: g(-K), False), (lambda K: g(K).conj().T, False), (lambda K: g(-K).conj().T, True),
                   (lambda K: g(-K), True), (lambda K: g(-(R4 @ K)).conj().T, True), (lambda K: g(R4 @ K), True))]
    hp = lambda f: [p for K in KR[:5] for p in f(K)]
    half_counts[st] = [len(solve(hp(lambda K: [(halves(K, st, mu, M)[j], halves(-K, st, mu, M)[j].conj().T) for j in (0, 1)]), False)),
                       len(solve(hp(lambda K: [(halves(K, st, mu, M)[j], halves(R4 @ K, st, mu, M)[j]) for j in (0, 1)]), True))]
    e0s[st] = np.sort(np.abs(np.angle(np.linalg.eigvals(g(np.zeros(3))))))
check('B1 copy mass M/2 per half-tick on the w copy: 12 tetrahedral turns kept, 12 odd broken; solutions (inversion, chiral, T, PH, T x C4, PH x C4) = (1,1,0,0,1,1) '
      'at steps pi/2, .3, .04; chiral x inversion and PH x C4 hold per half-tick; at K = 0 the light copy keeps mu, the other gets mu + M',
      all(keep) and all(v == [1, 1, 0, 0, 1, 1] for v in counts.values()) and all(v == [1, 1] for v in half_counts.values())
      and np.allclose(e0s[0.3], [0.1] * 4 + [0.6] * 4), f'counts {counts[0.3]}, per half-tick {half_counts[0.3]}')
g = lambda K: tick(K, 0.3, 0.1, 0.5)
Vph = solve([(g(K), g(-K)) for K in KR], True)              # PH alone: none with the copy mass, so take it at M = 0
g0 = lambda K: tick(K, 0.3, 0.1, 0.0)
Vph0 = solve([(g0(K), g0(-K)) for K in KR], True)[0]; L4x = [G for G, R in zip(Gs, rots) if np.allclose(R, R4)][0]
sw = lambda V: nrm(V @ PA.conj() @ V.conj().T / np.sqrt(np.trace(V @ V.conj().T).real / 8) ** 2 - PB)
check('B2 [theorem] PH (at M = 0) and the fourfold turn each swap the copies (an antiunitary commuting with a threefold turn sends w to w^2), so PH x C4 keeps copy A: '
      'the copy mass is C\'-even and the copy phase e^(2 pi i/3) is a representation label, not a CP-odd coefficient',
      len(Vph) == 0 and sw(Vph0) < 1e-9 and nrm(L4x @ PA @ L4x.conj().T - PB) < 1e-9, f'PH with copy mass: {len(Vph)} solutions')

# =============================== C. many-body twisted torus ===============================
print('== C. many-body tick, 2^3 torus twisted by K = (pi,0,0): 8 modes, 256 states (exact)')
sz = np.diag([1., -1.]); aa = np.array([[0., 1.], [0., 0.]])
c = []
for i in range(8):
    o = np.array([[1.0]])
    for M_ in [sz] * i + [aa] + [np.eye(2)] * (7 - i): o = np.kron(o, M_)
    c.append(o.astype(complex))
cd = [x.conj().T for x in c]; Nop = sum(cd[i] @ c[i] for i in range(8)); NN = np.round(np.diag(Nop).real).astype(int)
def quad(h): return sum(h[i, j] * cd[i] @ c[j] for i in range(8) for j in range(8) if abs(h[i, j]) > 1e-15)
def Gam(uu):
    T, Z = schur(uu, output='complex'); return expm(-1j * quad(Z @ np.diag(-np.angle(np.diag(T))) @ Z.conj().T))
Ph = np.eye(256, dtype=complex)
for i in range(8): Ph = Ph @ (c[i] + cd[i])
herm = lambda A: A + A.conj().T
subs = list(itertools.combinations(range(8), 4)); SUBS = np.array(subs)
cS = [c[s[0]] @ c[s[1]] @ c[s[2]] @ c[s[3]] for s in subs]
def L4(G): return np.linalg.det(G[SUBS[:, None, :, None], SUBS[None, :, None, :]])
def vec4(Ub): return np.array([np.linalg.det(Ub[list(R), :]) for R in subs])
def Ofock(v): return sum(np.conj(v[k]) * cS[k] for k in range(70) if abs(v[k]) > 1e-13)
Kt = np.array([np.pi, 0, 0]); Dk = Dg(Kt); twist = np.array([np.prod(np.exp(-1j * (C[list(s)] @ Kt))) for s in subs])
Pi = np.zeros((8, 8))
for i in range(8): Pi[img(-np.eye(3), i), i] = 1
phs = {0: 1.0 + 0j}
while len(phs) < 8:
    for a in list(phs):
        for b in range(8):
            if b not in phs and abs(W[a, b]) > 0:
                ia, ib = int(np.argmax(Pi[:, a])), int(np.argmax(Pi[:, b])); phs[b] = np.conj(W[ia, ib] / (phs[a] * W[a, b]))
LP = L4(Pi @ np.diag([phs[i] for i in range(8)])); LT = [L4(G) for G, o in zip(Gs, ODD) if not o]
EVi = [i for i in range(8) if C[i].sum() % 2 == 0]
def basis(P): w, v = np.linalg.eigh(P); return v[:, w > 0.5]
classes = {}
for nm, v0 in (('1', vec4(I8[:, EVi])), ('w', vec4(basis(PA))), ('w2', vec4(basis(PB)))):
    chi = [complex(v0.conj() @ A @ v0 / (v0.conj() @ v0)) for A in LT]
    full = null_space(np.vstack([A - x * np.eye(70) for A, x in zip(LT, chi)]))
    classes[nm] = (full.shape[1], null_space(np.vstack([A - x * np.eye(70) for A, x in zip(LT, chi)] + [LP - np.eye(70)])))

class Model:
    def __init__(self, st, mu, M, beta=2.0):
        self.Ue, self.Uo = halves(Kt, st, mu, M)
        gq = lambda K: tick(K, st, mu, M)
        V = solve([(gq(K), gq(R4 @ K)) for K in KR], True)[0]; V /= np.sqrt(np.trace(V @ V.conj().T).real / 8)
        Z = solve([p for K in KR[:5] for p in [(halves(K, st, mu, M)[j], halves(-K, st, mu, M)[j].conj().T) for j in (0, 1)]], False)[0]
        Z /= np.sqrt(np.trace(Z @ Z.conj().T).real / 8)
        self.X = Gam(-V) @ Ph; GZ = Gam(Z); self.Th = lambda A: GZ @ Ph @ A.conj() @ Ph.conj().T @ GZ.conj().T
        he = ((st - mu / 2) * I8 - M / 2 * PA) @ W; ho = Dk.conj().T @ (-((st + mu / 2) * I8 + M / 2 * PA) @ W) @ Dk
        self.Qe, self.Qo = quad(he), quad(ho); self.he, self.ho = he, ho
        T_, Z_ = schur(self.Uo @ self.Ue, output='complex'); hF = Z_ @ np.diag(-np.angle(np.diag(T_))) @ Z_.conj().T
        self.wq = np.abs(np.angle(np.diag(T_)))
        wv, vv = np.linalg.eigh(quad((hF + hF.conj().T) / 2)); r = vv @ np.diag(np.exp(-beta * (wv - wv.min()))) @ vv.conj().T
        self.rho0 = r / np.trace(r).real
    def ops(self, cl): B_ = classes[cl][1]; return [Ofock(B_[:, a]) for a in range(B_.shape[1])], [Ofock(B_[:, a] * twist) for a in range(B_.shape[1])]
    def Lam(self, Os):
        k = len(Os); Lm = np.zeros((k, k), complex); res = 0.0
        for a in range(k):
            T = self.X @ Os[a] @ self.X.conj().T
            for b in range(k): Lm[b, a] = np.trace(Os[b] @ T) / np.trace(Os[b] @ Os[b].conj().T)
            res = max(res, nrm(T - sum(Lm[b, a] * Os[b].conj().T for b in range(k))))
        return Lm, res
    def tickV(self, gv, Oe, Oo):
        He = herm(sum(x * O for x, O in zip(gv, Oe))); Ho = herm(sum(x * O for x, O in zip(gv, Oo)))
        Ve = expm(-1j * (self.Qe + He)); Vo = expm(-1j * (self.Qo + Ho)); return Ve, Vo
    def Qt(self, U, T, r=None):
        r = self.rho0.copy() if r is None else r; out = []
        for _ in range(T): r = U @ r @ U.conj().T; out.append(np.trace(r @ Nop).real - 4)
        return np.array(out)
    def eps(self, U):      # asymmetry per number-changing event after one tick, from the N-diagonal start
        num = den = 0.0
        for nn in range(9):
            idx = np.where(NN == nn)[0]
            if idx.size == 0: continue
            r = np.zeros((256, 256), complex); r[np.ix_(idx, idx)] = self.rho0[np.ix_(idx, idx)]
            pr = np.real(np.diag(U @ r @ U.conj().T)); dN = NN - nn; num += (dN * pr).sum(); den += (np.abs(dN) * pr).sum()
        return num / den, den
mdl = Model(0.3, 0.1, 0.5)
Gue, Guo = Gam(mdl.Ue), Gam(mdl.Uo)
cm = lambda A, B: (lambda Y: nrm(Y - Y[0, 0] * np.eye(256)))(A @ B @ A.conj().T @ B.conj().T)
th = lambda B: (lambda Y: nrm(Y - Y[0, 0] * np.eye(256)))(mdl.Th(B) @ B)
check('C1 [theorem, checked] C\' = Gamma(V) P_h (P_h = product of the 8 Majoranas, V the PH x C4 matrix) commutes with each free half-tick (copy mass on) '
      'and sends N to 8 - N; the CPT-type Theta (chiral x inversion) sends each half-tick to its inverse; the start rho0 = exp(-2 H_F)/Z is C\'-invariant, <N - 4> = 0',
      max(cm(mdl.X, Gue), cm(mdl.X, Guo), th(Gue), th(Guo)) < 1e-10 and nrm(mdl.X @ Nop @ mdl.X.conj().T - (8 * np.eye(256) - Nop)) < 1e-10
      and nrm(mdl.X @ mdl.rho0 @ mdl.X.conj().T - mdl.rho0) < 1e-12 and abs(np.trace(mdl.rho0 @ Nop).real - 4) < 1e-12,
      f'max deviation {max(cm(mdl.X, Gue), cm(mdl.X, Guo), th(Gue), th(Guo)):.0e}')
def Mth(m, Os):            # Theta O_a Theta^-1 = sum_b M_ba O_b^dag
    k = len(Os); Mm = np.zeros((k, k), complex)
    for a in range(k):
        T = m.Th(Os[a])
        for b in range(k): Mm[b, a] = np.trace(Os[b] @ T) / np.trace(Os[b] @ Os[b].conj().T)
    return Mm
ODi = [i for i in range(8) if C[i].sum() % 2 == 1]
REF = {'1': vec4(I8[:, EVi]) + vec4(I8[:, ODi]), 'w': vec4(basis(PA)), 'w2': vec4(basis(PB))}     # tetrahedral form, top forms of each copy
def Espace(m, cl):         # CPT-type-even coefficient space (g-space) holding the register's term, and the C' conjugation J on it
    Oe_, Oo_ = m.ops(cl); Me, Mo = Mth(m, Oe_), Mth(m, Oo_); Lm, _ = m.Lam(Oe_); k = len(Oe_)
    c0 = classes[cl][1].conj().T @ REF[cl]; kp = (c0.conj() @ Me @ c0) / (c0.conj() @ c0)
    Eg = null_space(np.vstack([Me - kp * np.eye(k), Mo - kp * np.eye(k)]), rcond=1e-9).conj(); Li = np.linalg.inv(Lm)
    return dict(Oe=Oe_, Oo=Oo_, Eg=Eg, J=lambda g: Li @ g.conj(), Lm=Lm, Me=Me, kp=kp, c0=c0,
                other=null_space(np.vstack([Me + kp * np.eye(k), Mo + kp * np.eye(k)]), rcond=1e-9).shape[1])
def realpair(E, seed):
    r_ = np.random.default_rng(seed); out = []
    for _ in range(2):
        x = E['Eg'] @ (r_.normal(size=E['Eg'].shape[1]) + 1j * r_.normal(size=E['Eg'].shape[1])); y = x + E['J'](x); out.append(y / np.linalg.norm(y))
    a, b = out; b = b - np.real(a.conj() @ b) * a; return a, b / np.linalg.norm(b)
lamres, lamsym, Es = [], [], {}
for cl in ('1', 'w', 'w2'):
    Oe, Oo = mdl.ops(cl); Lm, res = mdl.Lam(Oe); Lmo, reso = mdl.Lam(Oo)
    lamres.append(max(res, reso, nrm(Lm - Lmo))); lamsym.append(max(nrm(Lm @ Lm.conj().T - np.eye(len(Oe))), nrm(Lm - Lm.T))); Es[cl] = Espace(mdl, cl)
dims = [(classes[k][0], classes[k][1].shape[1], Es[k]['Eg'].shape[1], Es[k]['other']) for k in ('1', 'w', 'w2')]
Jok = max(np.linalg.norm((lambda x: E['J'](x) - E['Eg'] @ E['Eg'].conj().T @ E['J'](x))(E['Eg'][:, 0] + 0.3j * E['Eg'][:, -1])) for E in Es.values())
check('C2 [theorem, checked] four-mode cube terms by threefold-turn character (1, w, w^2): dims 10, 6, 6; inversion-even 6, 4, 4; CPT-even (the family holding '
      'the tetrahedral form and both one-copy top forms) 4, 3, 3. C\' acts on each by a unitary symmetric Lam, a real structure: CP-odd parameters 3, 2, 2, none fixed by a law',
      [d[:3] for d in dims] == [(10, 6, 4), (6, 4, 3), (6, 4, 3)] and [d[3] for d in dims] == [2, 1, 1] and max(lamres) < 1e-10 and max(lamsym) < 1e-10 and Jok < 1e-10,
      f'(dim, inv-even, CPT-even, other family) {dims}')
E2 = Es['w2']; uR, wR = realpair(E2, 3); E1 = Es['1']
gB = E2['c0'].conj() / np.linalg.norm(E2['c0']); gT = E1['c0'].conj() / np.linalg.norm(E1['c0'])
run = lambda gv, E, T=40: mdl.Qt((lambda V: V[1] @ V[0])(mdl.tickV(gv, E['Oe'], E['Oo'])), T)
q0 = [np.abs(run(0.3 * np.exp(1j * p) * gB, E2)).max() for p in (0.0, 1.3)] + [np.abs(run(0.3 * np.exp(1j * p) * gT, E1)).max() for p in (0.0, 2.2)]
q0 += [np.abs(run(0.3 * (uR + s * wR), E2)).max() for s in (1, -0.4)]
check('C3 [theorem: exp(i a N) C\' is exact] the one-copy term alone and the tetrahedral form alone, with any phase, and any real-form mixture, give '
      '<N(t) - 4> = 0 at every tick (40 ticks, copy mass on): the copy phase and one coefficient phase make no asymmetry', max(q0) < 1e-12, f'max |<Q>| {max(q0):.0e}')
qp, qm = run(0.3 * (uR + 1j * wR), E2), run(0.3 * (uR - 1j * wR), E2)
check('C4 [finite] a relative phase pi/2 between two CPT-even real-form terms of the w^2 class (g = 0.3) gives <N - 4> != 0, odd in the phase',
      np.abs(qp).max() > 1e-3 and nrm(qp + qm) < 1e-12, f'max |<Q>| over 40 ticks {np.abs(qp).max():.3f}')
def stationary(gv, E):
    Ve, Vo = mdl.tickV(gv, E['Oe'], E['Oo']); wv, vv = np.linalg.eig(Vo @ Ve); vi = np.linalg.inv(vv); out = []
    for beta in (2.0, 5.0):
        r = vv @ np.diag(np.exp(beta * np.angle(wv))) @ vi; r = (r + r.conj().T) / 2; r /= np.trace(r).real
        out.append((np.trace(r @ Nop).real - 4, np.trace(Ve @ r @ Ve.conj().T @ Nop).real - 4))
    return out, vv
st_cp, _ = stationary(0.3 * (uR + 1j * wR), E2)
gbad = 0.3 * (np.random.default_rng(5).normal(size=4) + 1j * np.random.default_rng(6).normal(size=4)); st_bad, _ = stationary(gbad, E2)
qinf = np.abs(mdl.Qt((lambda V: V[1] @ V[0])(mdl.tickV(0.3 * (uR + 1j * wR), E2['Oe'], E2['Oo'])), 20, np.eye(256) / 256)).max()
check('C5 [theorem, checked] equilibrium makes nothing: in every stationary state f(quasi-energy) of the CP-violating but CPT-even tick, Theta gives '
      '<Q>(tick) = -<Q>(half-tick), tick average 0, and infinite temperature stays at 0; a CPT-odd coefficient set would give stationary states a net <Q>',
      all(abs(a + b) < 1e-12 for a, b in st_cp) and max(abs(a) for a, b in st_cp) > 1e-5 and qinf < 1e-13 and max(abs(a + b) for a, b in st_bad) > 1e-4,
      'tick, half-tick: ' + ', '.join(f'({a:+.1e}, {b:+.1e})' for a, b in st_cp) + f'; CPT-odd sums ' + ', '.join(f'{a + b:+.1e}' for a, b in st_bad))
epsv = {}
for stp in (0.3, 0.15, 0.075):
    m2 = mdl if stp == 0.3 else Model(stp, stp / 3, stp * 5 / 3, beta=0.6 / stp)
    for cl in ('w2', '1'):
        Ex = Espace(m2, cl); a2, b2 = realpair(Ex, 1); V2 = m2.tickV(0.02 * (a2 + 1j * b2), Ex['Oe'], Ex['Oo']); epsv[(stp, cl)] = m2.eps(V2[1] @ V2[0])[0]
ev = np.abs(list(epsv.values()))
check('C6 [finite] asymmetry per number-changing event, one tick, g = .02, phase pi/2, steps .3/.15/.075 (mu, M, T scaled): 1e-2 to 2e-1, '
      'g-independent at small g; no clean continuum scaling in this toy', ev.min() > 1e-3 and ev.max() < 0.3,
      ', '.join(f'{s}/{k}: {v:+.1e}' for (s, k), v in epsv.items()))

# =============================== D. estimates ===============================
print('== D. estimates against measurement (formulas and data supplied)')
MP = 1.2209e19; unit = np.sqrt(3) / (2 * np.sqrt(8 * np.pi)) * MP; etaB = 6.1e-10; YB_obs = etaB / 7.04; gs = 112.0
Yeq = 135 * 1.2020569 / (8 * np.pi ** 4) * 2 / gs
eps_c = float(np.exp(np.mean(np.log(ev))))             # geometric mean of the toy range (C6)
def YB(Tm, g=1.0, kap=1.0, sphi=1.0, eps=eps_c):
    GH = kap * g ** 2 * Tm ** 3 * (MP / unit) / (1.66 * np.sqrt(gs)); return 28 / 79 * eps * sphi * GH / 3 * Yeq, GH
y05, GH05 = YB(0.5); Tneed = 0.5 * (YB_obs / y05) ** (1 / 3); lo, hi = YB(0.5, eps=ev.min())[0], YB(0.5, eps=ev.max())[0]
print(f'   1 rad/tick = {unit:.2e} GeV; Y_B(obs) = {YB_obs:.2e}. Freeze-in from T_max: Gamma/H = kappa g^2 T^3 M_P/(1.66 sqrt(g*) unit), events Y_ev = (Gamma/H)/3 Y_eq, Y_eq = {Yeq:.1e}')
print(f'   Y_B = (28/79) eps sin(dphi) Y_ev for a uddn-type transfer, eps = {eps_c:.1e} (toy range {ev.min():.0e}-{ev.max():.0e}, taken T-independent: an upper estimate)')
print(f'   g = kappa = sin(dphi) = 1, T_max = 0.5 rad/tick: Gamma/H = {GH05:.3f}, Y_B = {y05:.1e} ({lo:.0e}-{hi:.0e}) = {y05 / YB_obs:.0e} x observed;')
print(f'   observed needs T_max = {Tneed:.3f} rad/tick = {Tneed * unit:.1e} GeV, or g^2 kappa sin(dphi) = {YB_obs / y05:.1e} at T_max = 0.5')
check('D1 natural size: O(1) coefficient, O(1) phase and a cell-scale hot start overshoot eta_B by ~1e2-1e4; the measured value sits inside the free coefficient '
      'range; no washout, since Gamma/H < 1 for every T below the cell scale', 1e1 < y05 / YB_obs < 1e6 and GH05 < 1)
mnu, Tsph = 0.05e-9, 131.0; Hs = 1.66 * np.sqrt(106.75) * Tsph ** 2 / MP; Gf = (mnu / Tsph) ** 2 * 0.03 * Tsph
check('D2 nu^c stays sequestered: its only link to the plasma below the cell scale is the Dirac mass (Majorana forbidden by Z4); chirality flips at '
      '(m/T)^2 alpha T give Gamma/H ~ 1e-11 at the sphaleron freeze-out (131 GeV), and nu^c carries no link charge (Y = 0)', Gf / Hs < 1e-9, f'Gamma/H = {Gf / Hs:.0e}')
heat = 0.5 * 0.175 * 0.213
print(f'   splits: a heating split leaves {heat:.3f} rad/tick per site (agents/cosmology) at every split, today included (excluded by Lambda); an adiabatic split changes no')
print('   number (agents/nuc-dark-matter D1). So splits are not the departure from equilibrium; the expansion of a hot start is (Gamma/H < 1 for T below the cell scale).')
print('   measured CP violation is missing too: no charged current commutes with the tick (register: weak decays), so no CKM phase (J = 3.1e-5)')
print('theorems: A1-A4, B2, C1-C3, C5 (checked numerically).  finite: B1, C4, C6.  estimates: D1-D2.')
print('supplied: one-family content and the rung-1 species reading, the four-mode terms and their coefficients and phases, (st, mu, M), the twist, the')
print('  start rho0, sphaleron and Yukawa equilibrium premises, Nf = 3 and NH = 1, the unit map, kappa, T_max, the freeze-in formula, all measured numbers.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
