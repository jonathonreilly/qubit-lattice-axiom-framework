#!/usr/bin/env python3
"""d4-lattice-cp-parities: is lattice CP (improper W(F4) spinor lift x charge conjugation, psi <-> psibar) exact on the D4
route, and what CP parities do the bilinear channels 16 x 16 = 10_s + 126_s + 120_a carry on the register?
 1  exactness: D4 fixed-point slab (Borici, Shamir; wall-preserving or wall-swapping?), far-wall Spin(12) pair, Cayley
    4-form, link theta carrier.
 2  channel parities: pre-registered matrix definition, and the Grassmann-correct one (family index included).
 3  SM-component mass matrices from register Clebsches (SU(3)_c x U(1)_em-invariant vev tensors), J, arg det, the bit.
Labels: [T] exact, [F] finite/seeded diagnostic, [E] estimate with supplied literature numbers.
Supplied: the 16 (5-mode occupation basis), the channel content, Yukawa entries (random), vev directions (random within
the invariant subspaces), the Q_em assignment, the loop estimate. Self-contained, seeded, no external files."""
AUDIT_TIMEOUT_SEC = 120
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"): os.environ[v] = "1"
import itertools, time, warnings
import numpy as np
warnings.filterwarnings("ignore")
T0 = time.time(); rng = np.random.default_rng(20261026); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))
# ---------------- lattice data, W(F4) with spinor representatives, gammas
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
g5 = gm[0] @ gm[1] @ gm[2] @ gm[3]; g5 = g5 / np.sqrt((g5 @ g5)[0, 0])
gv = lambda v: np.einsum('...m,mab->...ab', v, gm)
E4 = np.eye(4); rt = np.array([1., 1, 0, 0]); ut = rt / np.sqrt(2); Pp = (E4 + g5) / 2; Pm = (E4 - g5) / 2
gens = []; gS = []
for i in range(3):
    n = np.zeros(4); n[i], n[i + 1] = 1 / np.sqrt(2), -1 / np.sqrt(2); gens.append(E4 - 2 * np.outer(n, n)); gS.append(g5 @ gv(n))
n = np.zeros(4); n[0] = 1; gens.append(E4 - 2 * np.outer(n, n)); gS.append(g5 @ gv(n))
n = np.ones(4) / 2; gens.append(E4 - 2 * np.outer(n, n)); gS.append(g5 @ gv(n))
key = lambda A: tuple(np.round(2 * A).astype(int).ravel()); Dd = {key(E4): (E4, np.eye(4, dtype=complex))}; fr = [key(E4)]
while fr:
    nf = []
    for kk in fr:
        A, SA = Dd[kk]
        for g, sg in zip(gens, gS):
            B = g @ A
            if key(B) not in Dd: Dd[key(B)] = (B, sg @ SA); nf.append(key(B))
    fr = nf
GW4 = np.array([v[0] for v in Dd.values()]); SW = np.array([v[1] for v in Dd.values()]); DET = np.round(np.linalg.det(GW4)).astype(int)
def fq(c):  # f(q) from c_a = cos(q_a): (1 + sum_roots/2 cos + sum_S2/8 cos)/16, exact rewrite
    s = c.sum(-1); return (s * s - 0.5 * (c * c).sum(-1) + 2 * c.prod(-1)) / 16



# ---------------- fixed point by image sum
JL = 8


def Pi(q):
    out = np.ones(q.shape[:-1], dtype=q.dtype)
    for j in range(1, JL + 1): out = out * fq(np.cos(q / 2.0 ** j))
    q2 = np.sum(q * q, -1)
    return out * np.exp(-(9 / 32) * q2 / (3 * 4.0 ** JL) - (17 / 2048) * q2 ** 2 / (15 * 16.0 ** JL))


def chi(x, N):
    u = np.clip((x - (N - 2)) / 2.0, 0, 1); g = lambda t: np.where(t > 0, np.exp(-1 / np.maximum(t, 1e-300)), 0.)
    return g(1 - u) / (g(1 - u) + g(u))


IMC = {}


def images(N):
    if N not in IMC:
        a = np.array(list(itertools.product(range(-N - 1, N + 2), repeat=4)), float); L_ = np.vstack([a, a + 0.5]) * 2 * np.pi
        IMC[N] = L_[np.linalg.norm(L_, axis=1) <= 2 * np.pi * (N + 1)]   # |p| <= 2pi after folding
    return IMC[N]


def fold(p):
    x = p / (2 * np.pi); a = np.round(x); b = np.floor(x) + 0.5
    return p - 2 * np.pi * np.where((np.sum((x - a) ** 2, -1) <= np.sum((x - b) ** 2, -1))[:, None], a, b)


def Gstar(p, N=6, m=0.0, al=0.5):   # G* = sigma - i g.rho
    p = fold(np.atleast_2d(p)); IM = images(N); sig = np.zeros(len(p)); rho = np.zeros((len(p), 4)); st = max(1, 200000 // len(IM))
    for i in range(0, len(p), st):
        q = p[i:i + st, None, :] + IM[None]; q2 = np.sum(q * q, -1)
        w = Pi(q) ** 2 / (q2 + m * m) * chi(np.sqrt(q2) / (2 * np.pi), N)
        sig[i:i + st] = m * w.sum(1); rho[i:i + st] = np.einsum('pl,plm->pm', w, q)
    return sig + al, rho


Gm = lambda s, r: s[..., None, None] * E4 - 1j * gv(r)
Bm = np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]], float).T


Gm = lambda s_, r: s_[..., None, None] * E4 - 1j * gv(r)
def Dstar(p, N=6):
    sg, rh = Gstar(p, N, 0.0, 0.5); return np.linalg.inv(Gm(sg, rh))
def D5(Ak, Ls, mf, b, c):   # Moebius slab of d4-zoom-chirality
    Mx = np.zeros((Ls, 4, Ls, 4), complex); hop = c * Ak - E4
    for s_ in range(Ls):
        Mx[s_, :, s_] = b * Ak + E4
        Mx[s_, :, (s_ + 1) % Ls] += (1 if s_ + 1 < Ls else -mf) * hop @ Pm
        Mx[s_, :, (s_ - 1) % Ls] += (1 if s_ >= 1 else -mf) * hop @ Pp
    return Mx.reshape(4 * Ls, 4 * Ls)
def Deff(Ak, Ls, mf, b, c):
    Pr = np.zeros((Ls, 4, Ls, 4), complex)
    for s_ in range(Ls): Pr[s_, :, s_] = Pm; Pr[s_, :, (s_ + 1) % Ls] = Pp
    Pr = Pr.reshape(4 * Ls, 4 * Ls); return (np.linalg.inv(Pr) @ np.linalg.solve(D5(Ak, Ls, 1.0, b, c), D5(Ak, Ls, mf, b, c)) @ Pr)[:4, :4]
print("== 1. exactness of lattice CP_g = (improper lift S_g) x C, psi -> M psibar^T, M = C S_g^-T, no s-reflection")
Cm = gm[0] @ gm[2]; LS = 8; M0 = 1.0; Jr = np.kron(np.eye(LS)[::-1], E4)
imp = [i for i in range(1152) if DET[i] < 0]
cC = max(np.abs(Cm @ gm[m].T @ np.linalg.inv(Cm) + gm[m]).max() for m in range(4)); c5 = np.abs(Cm @ g5.T @ np.linalg.inv(Cm) - g5).max()
pc = rng.uniform(-2, 2, (2, 4)); n = len(pc)
P = np.concatenate([pc, -pc] + [-np.einsum('ij,pj->pi', GW4[i], pc) for i in imp]); DS = Dstar(P)
Dp, Dmn, DmR = DS[:n], DS[n:2 * n], DS[2 * n:].reshape(len(imp), n, 4, 4)
cD = max(np.abs(Cm @ Dp[k].T @ np.linalg.inv(Cm) - Dmn[k]).max() for k in range(n))
check("1a [T] C = g0 g2 obeys C g^T C^-1 = -g, C g5^T C^-1 = g5; the D4 fixed-point symbol obeys C D*(p)^T C^-1 = D*(-p)",
      max(cC, c5, cD) < 1e-12, f"{max(cC, c5):.0e}, D* {cD:.0e}")
res = {}
for nm, b, c in (("Borici", .5, .5), ("Shamir", 1., 0.)):
    Cb = np.kron(np.eye(LS), Cm); X0 = [np.kron(np.eye(LS), c * (Dmn[k] - M0 * E4) - E4) for k in range(n)]
    eCJ = max(np.abs(Cb @ D5(Dp[k] - M0 * E4, LS, .1, b, c).T @ np.linalg.inv(Cb) - np.linalg.inv(X0[k]) @ Jr @ D5(Dmn[k] - M0 * E4, LS, .1, b, c) @ Jr @ X0[k]).max() for k in range(n))
    e0 = ej = eD = 0; ejmin = 9
    for j, i in enumerate(imp):
        M4 = Cm @ np.linalg.inv(SW[i]).T; Mb = np.kron(np.eye(LS), M4); Mi = np.linalg.inv(Mb)
        for k in range(n):
            A2 = DmR[j, k] - M0 * E4; X = np.kron(np.eye(LS), c * A2 - E4); Xi = np.linalg.inv(X); L = Mb @ D5(Dp[k] - M0 * E4, LS, .1, b, c).T @ Mi
            e0 = max(e0, np.abs(L - Xi @ D5(A2, LS, .1, b, c) @ X).max()); ejmin = min(ejmin, np.abs(L - Xi @ Jr @ D5(A2, LS, .1, b, c) @ Jr @ X).max())
            eD = max(eD, np.abs(M4 @ Deff(Dp[k] - M0 * E4, LS, .1, b, c).T @ np.linalg.inv(M4) - Deff(A2, LS, .1, b, c)).max())
    res[nm] = (eCJ, e0, ejmin, eD)
check("1b [T] slab (Ls = 8, mf = 0.1): C alone needs the wall reflection J (C D5(p)^T C^-1 = X^-1 J D5(-p) J X); CP_g for all 576 "
      "improper g is WALL-PRESERVING: M D5(p)^T M^-1 = X^-1 D5(-g p) X with NO J (X = c A - 1, s-independent and local; X = -1 for "
      "Shamir), and the wall-fermion operator obeys M D_eff(p)^T M^-1 = D_eff(-g p): not the face swap",
      all(v[0] < 1e-10 and v[1] < 1e-10 and v[2] > 0.1 and v[3] < 1e-10 for v in res.values()),
      "; ".join(f"{k}: C+J {v[0]:.0e}, CP no-J {v[1]:.0e}, CP with-J >= {v[2]:.2f}, D_eff {v[3]:.0e}" for k, v in res.items()))
# Luscher projector (informational): gamma5_hat = g5 (1 - D_ov / rho), D_ov = D*/2 (Borici Ls -> inf)
Dov = 0.5 * Dp[0]; rho = None
for r_ in (0.5, 1.0, 2.0):
    gh = g5 @ (E4 - Dov / r_)
    if np.abs(gh @ gh - E4).max() < 1e-10: rho = r_
gh = g5 @ (E4 - Dov / rho); M4 = Cm @ np.linalg.inv(SW[imp[0]]).T
img = (np.linalg.inv(M4) @ ((E4 - g5 @ (E4 - 0.5 * DmR[0, 0] / rho)) / 2) @ M4).T
print(f"  [info] Luscher split (P_hat_- on psi, P_+ on psibar) is not CP-symmetric: the CP image of psi's P_hat_- is a "
      f"D-dependent projector on psibar, |image - P_+| = {np.abs(img - Pp).max():.2f} (cf. Fujikawa-Ishibashi-Suzuki 2002); the slab is exact")
# ---- Fock helpers
def ann(nm_):
    dim = 1 << nm_; st = np.arange(dim); out = []
    for j in range(nm_):
        A = np.zeros((dim, dim)); src = st[(st >> j) & 1 == 1]
        A[src ^ (1 << j), src] = 1 - 2 * (np.array([bin(int(x) & ((1 << j) - 1)).count('1') for x in src]) & 1); out.append(A)
    return out
c4 = ann(4); nm4 = np.array([bin(m).count('1') for m in range(16)]); Om = np.zeros((16, 16)); Om[0, 15] = 1
sig = np.vdot((c4[0] @ c4[1] @ c4[2] @ c4[3]).ravel(), Om.ravel())
w2 = lambda N: ((4 * np.eye(16) - 2 * N) @ (4 * np.eye(16) - 2 * N) - 4 * np.eye(16)) / 2
Cay = 8 * (Om + Om.T) - w2(np.diag(nm4).astype(float)); ecay = 0; dets = []
for i in imp:
    W4 = Cm @ np.linalg.inv(SW[i]).T; dets.append(np.linalg.det(W4)); cp = [sum(W4[a, b] * c4[b].T for b in range(4)) for a in range(4)]
    Op = sig * cp[0] @ cp[1] @ cp[2] @ cp[3]; Np = sum(x.conj().T @ x for x in cp)
    ecay = max(ecay, np.abs(8 * (Op + Op.conj().T) - w2(Np) - Cay).max())
check("1c [T] Cayley 4-form on the 4 spinor modes is invariant under the Fock particle-hole psi -> W4 psi^+, W4 = C S_g^-T, for all "
      "576 improper g (det W4 = 1, so the free phase alpha = 0 mod pi/2)", ecay < 1e-12 and max(abs(np.array(dets) - 1)) < 1e-12, f"{ecay:.0e}")
b5 = ann(5); G = []
for k in range(5): G += [b5[k] + b5[k].T, 1j * (b5[k] - b5[k].T)]
s = np.array([1 if np.allclose(g.conj(), g) else -1 for g in G]); evn = [x for x in range(32) if bin(x).count('1') % 2 == 0]
R16 = lambda X: X[np.ix_(evn, evn)]; Cc = np.linalg.multi_dot(G[0::2])
t16 = [R16(-0.25j * (G[a] @ G[c] - G[c] @ G[a])) for a, c in itertools.combinations(range(10), 2)]
TB = np.array([t.ravel() for t in t16]).T; espan = 0
for a, (i, j) in enumerate(itertools.combinations(range(10), 2)):
    co = np.linalg.lstsq(TB, -t16[a].T.ravel(), rcond=None)[0]; e_ = co.copy(); e_[a] -= s[i] * s[j]; espan = max(espan, np.abs(e_).max())
M16 = [R16(Cc @ g) for g in G]; eps = np.array([[0, 1], [-1, 0]])
Ka = [np.kron(eps, m) for m in M16]; KB = np.array([k_.conj().T.ravel() for k_ in Ka]).T; eU = 0
WLs = [np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))[0] for _ in range(3)]
ev_, U_ = np.linalg.eigh(g5); Vm = U_[:, ev_ < 0]; WLs.append(Vm.conj().T @ Cm @ np.linalg.inv(SW[imp[0]]).T @ gm[0].T @ Vm)
for WL in WLs:
    W = np.kron(WL, np.eye(16)); Umat = np.array([np.linalg.lstsq(KB, (W.T @ K_ @ W).ravel(), rcond=None)[0] for K_ in Ka])
    rs = max(np.abs(KB @ Umat[a] - (W.T @ Ka[a] @ W).ravel()).max() for a in range(10)); eU = max(eU, rs, np.abs(Umat @ Umat.conj().T - np.eye(10)).max())
check("1d [T] far-wall Spin(12) pair: W_int = 1 (occupation-basis conjugation) is Spin(10)-covariant (-t^T = s_a s_b t: outer automorphism "
      "R = diag(s), s = (+,-,...)), and B_a -> sum_b U_ab B_b^+ with U unitary for any unitary Weyl block (incl. the lift's): "
      "sum_a {B_a, B_a^+} is CP-invariant", espan < 1e-12 and eU < 1e-12, f"span {espan:.0e}, U {eU:.0e}")
roots = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(abs(np.array(v))) == 2], float)
rset = set(map(tuple, roots)); rok = all(set(map(tuple, np.round(roots @ GW4[i].T, 9) + 0.)) == rset for i in imp)
Fa = rng.normal(size=(4, 4)); Fa = Fa - Fa.T; pf = lambda F: F[0, 1] * F[2, 3] - F[0, 2] * F[1, 3] + F[0, 3] * F[1, 2]
eth = max(abs(pf(GW4[i] @ (-Fa) @ GW4[i].T) + pf(Fa)) for i in imp)
check("1e [T] links: every improper g maps the 24 D4 roots (hence every root plaquette) to themselves; the theta carrier "
      "eps F F = 8 Pf(F) is C-even (F -> -F^T) and P-odd (Pf(g F g^T) = det g Pf F): CP-odd, so theta_gauge in {0, pi}", rok and eth < 1e-12, f"{eth:.0e}")
print(f"  [t = {time.time() - T0:.0f} s]")
print("== 2. channel CP parities on the register (16 x 16 = 10_s + 120_a + 126_s, Weyl form eps)")
def kforms(k):
    return [(A, R16(Cc @ np.linalg.multi_dot([G[a] for a in A]) if k > 1 else Cc @ G[A[0]])) for A in itertools.combinations(range(10), k)]
KF = {k: kforms(k) for k in (1, 3, 5)}; pre = {}
for k in (1, 3, 5):
    lam = []
    for A, X in KF[k]:
        K_ = np.kron(eps, X); Kd = K_.conj().T; l_ = np.vdot(Kd.ravel(), K_.ravel()) / np.vdot(Kd.ravel(), Kd.ravel())
        lam.append((l_ / np.prod(s[list(A)]), np.abs(K_ - l_ * Kd).max()))
    pre[k] = (np.mean([x[0] for x in lam]), max(abs(x[0] - lam[0][0]) for x in lam), max(x[1] for x in lam))
e1 = pre[1][0]; pat = tuple(int(np.sign((pre[k][0] / e1).real)) for k in (1, 3, 5))
check("2a [T] PRE-REGISTERED definition W^T K^A W = eta_k r_A (K^A)^+ (K^A = eps x C Gamma^A, W = 1): eta_k constant over all "
      "components; pattern (eta_10, eta_120, eta_126) =", all(pre[k][1] < 1e-12 and pre[k][2] < 1e-12 for k in pre), f"{pat} (literal pre-reg PASS pattern)")
print("  -> but (K^A)^+ = (-1)^(k(k-1)/2) r_A K^A x (eps sign): this 'eta' is the transpose sign of C Gamma^(k), i.e. the s/a/s labels")
print("     themselves. A Grassmann bilinear also carries the family index (Y120 antisymmetric), which cancels that sign:")
def Ktot(Y, X): return np.kron(Y, np.kron(eps, X))
gS = np.zeros((16, 16), complex)
for t in t16: gS = gS + rng.normal() * t
from scipy.linalg import expm
cor = {}
for lab, Wint in (("W_int = 1", np.eye(16)), ("W_int = random Spin(10) g", expm(1j * gS))):
    W = np.kron(np.eye(3), np.kron(np.eye(2), Wint)); out = {}
    # vector automorphism from k = 1 with the Grassmann-correct image (coefficient Y^*)
    Y1 = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); Y1 = Y1 + Y1.T
    Bs = np.array([Ktot(Y1.conj(), X).conj().T.ravel() for A, X in KF[1]]).T
    T1 = np.array([np.linalg.lstsq(Bs, (W.T @ Ktot(Y1, X) @ W).ravel(), rcond=None)[0] for A, X in KF[1]]).T
    ph = T1.ravel()[np.argmax(np.abs(T1))]; ph = ph / abs(ph); R1 = (T1 / ph).real
    ok1 = np.abs(T1 / ph - R1).max() < 1e-10 and np.abs(R1 @ R1.T - np.eye(10)).max() < 1e-10
    for k in (1, 3, 5):
        Y = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); Y = Y - Y.T if k == 3 else Y + Y.T
        idx = list(itertools.combinations(range(10), k)); RA = np.array([[np.linalg.det(R1[np.ix_(a, b)]) for b in idx] for a in idx])
        errs = {}
        for sg_ in (+1, -1):
            e_ = 0
            for ia, (A, X) in enumerate(KF[k]):
                Z = W.T @ Ktot(Y, X) @ W; pred = sum(sg_ * ph * RA[ib, ia] * Ktot(Y.conj(), KF[k][ib][1]).conj().T for ib in np.nonzero(np.abs(RA[:, ia]) > 1e-12)[0])
                e_ = max(e_, np.abs(Z - pred).max())
                if ia > 12: break
            errs[sg_] = e_
        out[k] = (+1 if errs[1] < 1e-10 else (-1 if errs[-1] < 1e-10 else 0), errs)
    cor[lab] = (ok1, out)
pat2 = {lab: tuple(v[1][k][0] for k in (1, 3, 5)) for lab, v in cor.items()}
check("2b [T] Grassmann-correct parity: the CP image of channel k with Yukawa Y is channel k with Yukawa Y^* times ONE common "
      "factor (phase x wedge^k R) for all k (first 14 components per channel); same with W_int x random Spin(10) element: pattern (eta_10, eta_120, eta_126) =",
      all(v[0] for v in cor.values()) and all(p == (1, 1, 1) for p in pat2.values()), "; ".join(f"{l}: {p}" for l, p in pat2.items()) + " -> UNIFORM (+,+,+)")
print(f"  [t = {time.time() - T0:.0f} s]")
print("== 3. SM-component mass matrices from register Clebsches (vev tensors real, SU(3)_c x U(1)_em invariant; Yukawas real)")
ix = lambda bits: evn.index(sum(1 << x for x in bits)); cs = np.array([1, -1, 1])   # colour-ordering sign of the antiquark states
uL = [ix([a, 3]) for a in range(3)]; uc = [ix(sorted({0, 1, 2} - {a})) for a in range(3)]
dL = [ix([a, 4]) for a in range(3)]; dc = [ix(sorted(set(range(5)) - {a})) for a in range(3)]
q = np.array([-1 / 3, -1 / 3, -1 / 3, 1, 0]); n16 = np.array([[(x >> i) & 1 for i in range(5)] for x in evn])
gens = [np.diag(n16 @ q)] + [R16(b5[a].T @ b5[c]) for a in range(3) for c in range(3) if a != c] + \
       [R16(b5[0].T @ b5[0] - b5[1].T @ b5[1]), R16(b5[1].T @ b5[1] - b5[2].T @ b5[2])]
SUB = {}
for k in (1, 3, 5):
    Xs = np.array([X for A, X in KF[k]]); rA = np.array([np.prod(s[list(A)]) for A, X in KF[k]])
    Mt = np.vstack([(np.einsum('ij,ajk->aik', t.T, Xs) + np.einsum('aij,jk->aik', Xs, t)).reshape(len(Xs), -1).T for t in gens])
    sv, vh = np.linalg.svd(np.vstack([Mt.real, Mt.imag]))[1:]; null = vh[np.sum(sv > 1e-9):]
    for par in (1, -1):
        u_, sv2, vh2 = np.linalg.svd(null * ((1 + par * rA) / 2)[None, :]); SUB[(k, par)] = (Xs, vh2[:np.sum(sv2 > 1e-9)])
def masses(vac, r_):
    Mu = np.zeros((3, 3), complex); Md = np.zeros((3, 3), complex); col = 0
    for k, par in vac.items():
        Xs, B = SUB[(k, par)]; V = r_.normal(size=len(B)) @ B; O = np.einsum('a,aij->ij', V, Xs)
        cu = np.array([O[uL[a], uc[a]] for a in range(3)]) * cs; cd = np.array([O[dL[a], dc[a]] for a in range(3)]) * cs
        col = max(col, np.abs(cu - cu[0]).max(), np.abs(cd - cd[0]).max())
        Y = r_.normal(size=(3, 3)); Y = Y - Y.T if k == 3 else Y + Y.T; Mu += Y * cu[0]; Md += Y * cd[0]
    return Mu, Md, col
def jarl(Mu, Md):
    Hu, Hd = Mu @ Mu.conj().T, Md @ Md.conj().T; eu, ed = np.linalg.eigvalsh(Hu), np.linalg.eigvalsh(Hd)
    den = np.prod([e[i] - e[j] for e in (eu, ed) for i, j in ((2, 1), (2, 0), (1, 0))])
    return np.imag(np.linalg.det(Hu @ Hd - Hd @ Hu)) / (-2 * den)
print("  invariant vev dimensions (CP-even, CP-odd):", {k: (len(SUB[(k, 1)][1]), len(SUB[(k, -1)][1])) for k in (1, 3, 5)})
R3 = {}
for lab, vac in (("all CP-even", {1: 1, 3: 1, 5: 1}), ("120 CP-odd only", {1: 1, 3: -1, 5: 1}), ("10 CP-odd only (control)", {1: -1, 3: 1, 5: 1}),
                 ("126 CP-odd only (control)", {1: 1, 3: 1, 5: -1})):
    r_ = np.random.default_rng(7); J_, H_, I_, A_, C_ = [], [], [], [], []
    for t in range(200):
        Mu, Md, col = masses(vac, r_); J_.append(abs(jarl(Mu, Md))); C_.append(col)
        H_.append(max(np.abs(M - M.conj().T).max() / np.abs(M).max() for M in (Mu, Md))); I_.append(max(np.abs(M.imag).max() / np.abs(M).max() for M in (Mu, Md)))
        A_.append(np.angle(np.linalg.det(Mu @ Md)))
    A_ = np.abs(np.array(A_)); two = np.all(np.minimum(A_, np.abs(A_ - np.pi)) < 1e-9)
    R3[lab] = (np.median(J_), max(J_), max(H_), max(I_), two, np.mean(np.abs(A_ - np.pi) < 1e-9), np.median(np.minimum(A_, np.abs(A_ - np.pi))), max(C_))
    v = R3[lab]; print(f"  {lab:27s} median|J| {v[0]:.1e} max {v[1]:.1e} | non-Herm {v[2]:.0e} | Im/|M| {v[3]:.0e} | arg det in {{0,pi}}: {v[4]}"
                      f" (frac pi {v[5]:.2f}; median dist {v[6]:.1e}) | colour-blind {v[7]:.0e}")
a, b_, c_, d_ = R3["all CP-even"], R3["120 CP-odd only"], R3["10 CP-odd only (control)"], R3["126 CP-odd only (control)"]
check("3a [F] all vevs CP-even: M_u, M_d real, J = 0 (200 seeded samples): the exact lattice CP alone forbids the CKM phase",
      a[1] < 1e-14 and a[3] < 1e-12 and a[4] and a[7] < 1e-12, f"max|J| {a[1]:.0e}")
check("3b [F] CP broken only by the 120 vev: M_u, M_d Hermitian, arg det(M_u M_d) in {0, pi}, J != 0 -- the Grimus-Kuhbock shape follows "
      "from WHERE the CP-odd vev sits, not from channel parities", b_[2] < 1e-12 and b_[4] and b_[0] > 1e-6, f"median|J| {b_[0]:.1e}")
check("3c [F] controls: a CP-odd 10 or 126 vev gives non-Hermitian masses and generic theta_tree (~9 orders above 1e-10)",
      min(c_[2], d_[2]) > 1e-2 and min(c_[6], d_[6]) > 1e-4, f"median |theta_tree| {c_[6]:.1e}, {d_[6]:.1e}")
check("3d [F] arg-det bit with the 120-only breaking: det(M_u M_d) < 0 in a fraction strictly between 0 and 1: theta_tree = 0 or pi is "
      "NOT fixed by the symmetry (one unfixed bit)", 0 < b_[5] < 1, f"fraction pi = {b_[5]:.2f}")
print("== 4. loop estimate [E] (supplied literature scale, order of magnitude only)")
print("  After spontaneous CP breaking the Hermitian form is unprotected: one-loop dressing by the CP-odd 120 vev in heavy-scalar")
print("  loops gives theta_bar ~ (1/16 pi^2) x lambda_mix x y^2 x sin(phi) (generic parity/Hermitian-mass solutions; e.g.")
print(f"  Babu-Mohapatra 1990, Barr-Chang-Senjanovic 1991, Hall-Harigaya 2018). With y ~ 1, sin phi ~ 1: {1 / (16 * np.pi ** 2):.1e} x lambda_mix,")
print("  so theta_bar < 1e-10 needs lambda_mix <~ 1e-8 (or a loop-level protection): a quality problem, as the menu flagged.")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
