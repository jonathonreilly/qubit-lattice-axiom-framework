AUDIT_INPUT_PATHS = ('docs/GLIDE_KEEPING_CUBE_TICKS_CARRY_AN_EVEN_NUMBER_OF_LIGHT_WEYL_DOUBLETS_PER_GLIDE_LABEL_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""glide-band: can a cube-covariant, glide-keeping deformation of the CL-1 tick leave exactly
L(q=2, glide +) + R(q=2, glide -) light?  Answer: no (glide parity obstruction).
  A  glide-keeping ticks are exactly U = (DP) A (DP)^-1 A, U = P^2 G^-2, G = A^-1 D P, any local A
  B  the glide label  Lam = e^{-i th.1/2} G U^{1/2}: involution, commutes with U, ANTIPERIODIC in th;
     at K = 0 and the zone corner th_c = pi(1,1,1) it commutes with all 12 kept rotations, whose
     fermion irreps there are doublets -> each label sector is a sum of doublets
  C  parity theorem (counting): gapped at 0 and pi away from the K = 0 light nodes => light Weyl
     doublets per glide label are EVEN; the target has one per label: impossible (every placement)
  D  diagnostics: the natural glide-symmetric copy terms fail exactly as C predicts; AX-3 evades
     because it breaks the glide; one kept turn alone (no 2-fold rotations) lifts the doublets.
Self-contained (numpy + scipy). Seeded. Bloch over 2Z^3: twisted 2^3 torus, twist th = 2k.
"""
import itertools as it
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(20261022)
NP = [0, 0]
W3 = np.exp(2j * np.pi / 3)
EPS = 0.6


def check(name, ok, detail=""):
    NP[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))


CELL = list(it.product([0, 1], repeat=3))
IDX = {a: n for n, a in enumerate(CELL)}
I8 = np.eye(8)


def eta(i, x):
    return [1, (-1) ** x[0], (-1) ** (x[0] + x[1])][i]


def build(th):
    We, Wo = [], []
    for i in range(3):
        for par, out in ((0, We), (1, Wo)):
            M = np.zeros((8, 8), complex)
            for x in CELL:
                if x[i] == par:
                    y = list(x); y[i] = (y[i] + 1) % 2; y = tuple(y)
                    ph = np.exp(1j * th[i]) if x[i] == 1 else 1
                    M[IDX[y], IDX[x]] += eta(i, x) * ph
                    M[IDX[x], IDX[y]] += eta(i, x) * np.conj(ph)
            out.append(M)
    P = np.zeros((8, 8), complex)
    for x in CELL:
        y = tuple((np.array(x) + 1) % 2)
        P[IDX[y], IDX[x]] = np.prod([np.exp(1j * th[i]) if x[i] == 1 else 1 for i in range(3)])
    return We, Wo, P


DG = np.diag([(-1) ** (a[0] + a[2]) for a in CELL]).astype(complex)   # glide gauge (-1)^(x1+x3)
We0, _, P00 = build(np.zeros(3))
ReC = sum(We0) / np.sqrt(3)                                           # even-cube hop (k-independent)
S = 1j * We0[0] @ We0[1] @ We0[2] @ ReC                               # copy sign s of AX-3
DI = DG @ P00                                                         # gauged cube inversion
PS, PC = (I8 + S) / 2, (I8 - S) / 2


def band(th, A_of, eps=EPS):
    """glide-keeping tick from an even half-step A = Ue * A_of(th): U = (DP)A(DP)^-1 A, G = A^-1 DP."""
    We, Wo, P = build(th)
    A = expm(-1j * eps * sum(We) / np.sqrt(3)) @ A_of(th)
    DP = DG @ P
    G = np.linalg.inv(A) @ DP
    return DP @ A @ np.linalg.inv(DP) @ A, G, P


def massless(th, eps=EPS):
    We, Wo, P = build(th)
    Ue, Uo = expm(-1j * eps * sum(We) / np.sqrt(3)), expm(1j * eps * sum(Wo) / np.sqrt(3))
    return Uo @ Ue, np.linalg.inv(Ue) @ DG @ P, P


def lam(U, G, th):
    w, v = np.linalg.eig(U)
    Uh = v @ np.diag(np.exp(1j * np.angle(w) / 2)) @ np.linalg.inv(v)   # principal square root
    return np.exp(-1j * np.sum(th) / 2) * G @ Uh


ROTS = []
for p in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[p[i], i] = sg[i]
        if np.linalg.det(R) > 0:
            ROTS.append(R)
cen = np.full(3, 0.5)
KT = [np.array([.2, -.3, .5]), np.array([-.6, .1, .3])]


def perm(R):
    Pm = np.zeros((8, 8))
    for a in CELL:
        b = tuple(np.rint(R @ (np.array(a) - cen) + cen).astype(int)); Pm[IDX[b], IDX[a]] = 1
    return Pm


def rot_gauge(R, f):
    Pm = perm(R)
    for sg in it.product([1, -1], repeat=8):
        V = np.diag(sg) @ Pm
        if all(np.allclose(V @ f(t) @ V.T, f(R @ t), atol=1e-10) for t in KT):
            return V
    return None


G24 = [(R, rot_gauge(R, lambda t: massless(t)[0])) for R in ROTS]
TG = [(R, V) for R, V in G24 if V is not None and np.allclose(V @ S @ V.T, S)]   # the 12 kept by s
TURNS = [V for R, V in TG if round(np.trace(R)) == 0]

# random range-2 T-symmetric deformation: hops of fine displacement |d|_inf <= 2, T-averaged
HOPS = []
for a in CELL:
    for d in it.product(range(-2, 3), repeat=3):
        y = np.array(a) + np.array(d); n = y // 2; b = tuple(y % 2)
        HOPS.append((IDX[b], IDX[a], n, 0.05 * (rng.normal() + 1j * rng.normal())))


def Xraw(th):
    X = np.zeros((8, 8), complex)
    for b, a, n, c in HOPS:
        X[b, a] += c * np.exp(1j * np.dot(n, th))
    return X + X.conj().T


def XT(th):
    return sum(V.T @ Xraw(R @ th) @ V for R, V in TG) / len(TG)


Cb = rng.normal(size=4)
CR = PS + PC @ expm(1j * sum(c * B for c, B in zip(Cb, [I8, ReC, DI, 1j * ReC @ DI]))) @ PC
A_rand = lambda th: CR @ expm(1j * XT(th))
th_r = rng.uniform(0, 2 * np.pi, 3)
THC = np.pi * np.ones(3)

# ------------------------------------------------------------------ A
print("== A. glide-keeping ticks (exact) ==")
U0, G0, P0 = massless(th_r)
e1 = np.abs(U0 - P0 @ P0 @ np.linalg.matrix_power(np.linalg.inv(G0), 2)).max()
Ur, Gr, Pr = band(th_r, A_rand)
e2 = max(np.abs(Gr @ Ur - Ur @ Gr).max(), np.abs(Ur - Pr @ Pr @ np.linalg.matrix_power(np.linalg.inv(Gr), 2)).max())
check("A1 massless CL-1 tick: U = P^2 G^-2 with G = Ue^-1 D P (the glide determines the tick)", e1 < 1e-12, f"{e1:.1e}")
check("A2 any local even half-step A: U = (DP)A(DP)^-1 A keeps G = A^-1 DP and U = P^2 G^-2 "
      "(GLIDE-KEEP <=> odd half-step = glide image of even half-step)", e2 < 1e-12, f"{e2:.1e}")
cov = max(np.abs(V @ band(t, A_rand)[0] @ V.T - band(R @ t, A_rand)[0]).max() for R, V in TG for t in KT[:1])
check("A3 a random range-2 T-symmetric glide-keeping deformation (plus a random copy-sector cube unitary) "
      "keeps all 12 rotations", len(TG) == 12 and cov < 1e-10, f"max err {cov:.1e}")

# ------------------------------------------------------------------ B
print("== B. the glide label Lam = e^{-i th.1/2} G U^{1/2} ==")
L1 = lam(Ur, Gr, th_r)
U2, G2, _ = band(th_r + np.array([2 * np.pi, 0, 0]), A_rand); L2 = lam(U2, G2, th_r + np.array([2 * np.pi, 0, 0]))
check("B1 Lam^2 = 1, [Lam, U] = 0, Lam(th + 2 pi e1) = -Lam(th): an antiperiodic involution (labels swap round "
      "every cycle)", np.allclose(L1 @ L1, I8) and np.allclose(L1 @ Ur, Ur @ L1) and np.allclose(L2, -L1))
Um0, Gm0, _ = massless(np.zeros(3))
lab = []
for g, sv in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
    Pp = (I8 + g * Gm0) / 2 @ (I8 + sv * S) / 2
    ew, ev = np.linalg.eigh((Pp + Pp.conj().T) / 2); B = ev[:, ew > 0.5]
    d = np.linalg.det(B.conj().T @ TURNS[0] @ B)
    lab.append((g, sv, B.shape[1], [q for q in range(3) if abs(d - W3 ** (2 * q)) < 1e-6]))
check("B2 massless K = 0 doublets (glide, s, dim, q): L2 (+,+,q=2), L1 (+,-,q=1), R2 (-,+,q=2), R1 (-,-,q=1); "
      "target = L2 + R2 = ONE light doublet per label", [x[3] for x in lab] == [[2], [1], [2], [1]] and all(x[2] == 2 for x in lab),
      str([(x[0], x[1], x[3][0]) for x in lab]))
res = {}
for nm, th in (("K=0", np.zeros(3)), ("corner", THC), ("(pi,0,0)", np.array([np.pi, 0, 0]))):
    U, G, _ = band(th, A_rand); L = lam(U, G, th)
    lg = [V for R, V in TG if np.allclose(np.exp(1j * R @ th), np.exp(1j * th))]
    res[nm] = "".join("c" if np.allclose(V @ L @ V.T, L, atol=1e-8) else ("a" if np.allclose(V @ L @ V.T, -L, atol=1e-8) else "?") for V in lg)
check("B3 at K = 0 and at the corner pi(1,1,1) all 12 rotations COMMUTE with Lam (random deformation); at "
      "(pi,0,0) two of the four 2-fold elements anticommute (no constraint there)",
      res["K=0"] == "c" * 12 and res["corner"] == "c" * 12 and res["(pi,0,0)"].count("a") == 2, str(res))
dbl = []
for th in (np.zeros(3), THC):
    U, G, _ = band(th, A_rand); L = lam(U, G, th)
    H = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)); H = H + H.conj().T
    H = sum(V @ H @ V.T for R, V in TG); H = H + L @ H @ L
    ev = np.sort(np.linalg.eigvalsh(H)); dbl.append(np.abs(ev[0::2] - ev[1::2]).max())
    wU = np.sort(np.angle(np.linalg.eigvals(U))); dbl.append(np.abs(wU[0::2] - wU[1::2]).max())
check("B4 at K = 0 and the corner the 12 rotations act spinorially: every T- and Lam-symmetric operator, and the "
      "tick itself, is doubly degenerate -> each label sector is a sum of doublets", max(dbl) < 1e-8, f"{max(dbl):.1e}")
C3 = [V for R, V in TG if np.allclose(R @ np.ones(3), np.ones(3)) and round(np.trace(R)) == 0]
H = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)); H = H + H.conj().T
H = H + sum(V @ H @ V.T for V in C3)
ev = np.sort(np.linalg.eigvalsh(H))
check("B5 one kept turn alone (C3 about (1,1,1), no 2-fold rotations) forces no doublets: escape needs the 2-fold "
      "rotations broken", np.min(np.diff(ev)) > 1e-3, f"min splitting {np.min(np.diff(ev)):.2e}")

# ------------------------------------------------------------------ C
print("== C. glide parity theorem (counting) ==")
print("   n(w,l) = rank of window w in {(-pi,0),(0,pi)} x label l: constant off the nodes; equal for l = +-")
print("   (B1); even at the corner (B3-B4); near K = 0 each light Weyl doublet adds 1 to n(-,l), others 2.")
viol = []
for sides in it.product([1, -1], repeat=2):          # copy doublets: labels (+,-) or (+,+)/(-,-), sides
    for labs in ((1, -1), (1, 1), (-1, -1)):
        neg = {1: 1, -1: 1}                            # L2 lower (+), R2 lower (-)
        for sd, lb in zip(sides, labs):
            if sd < 0:
                neg[lb] += 2
        bal = neg[1] == neg[-1]
        even = neg[1] % 2 == 0 and neg[-1] % 2 == 0
        viol.append(not (bal and even))
check("C1 every placement of the two copy doublets (labels x sides) with light L2(+) + R2(-) violates label "
      "balance or corner evenness: NO clean glide-keeping band has exactly one light doublet per label", all(viol),
      f"{len(viol)} placements, all excluded")
GR = [2 * np.pi * (np.array(c) + 0.5) / 6 for c in it.product(range(6), repeat=3)]


def census(f):
    neg, d0, dp = [], 9.0, 9.0
    for th in GR:
        E = np.angle(np.linalg.eigvals(f(th)))
        neg.append(int(np.sum(E < 0))); d0 = min(d0, np.min(abs(E))); dp = min(dp, np.min(np.pi - abs(E)))
    return sorted(set(neg)), d0, dp


c_m = census(lambda t: massless(t)[0])
Uc, Gc, _ = massless(THC); Lc = lam(Uc, Gc, THC)
wc, vc = np.linalg.eig(Uc); Qn, _ = np.linalg.qr(vc[:, np.angle(wc) < 0]); Pn = Qn @ Qn.conj().T
nl = [int(round(np.trace(Pn @ (I8 + s * Lc) / 2).real)) for s in (1, -1)]
check("C2 control, massless tick: 2 light doublets per label; n_neg = 4 on the whole grid, (2,2) per label at the "
      "corner: consistent with the theorem", c_m[0] == [4] and nl == [2, 2], f"n_neg {c_m[0]}, corner labels {nl}")

# ------------------------------------------------------------------ D
print("== D. natural glide-symmetric copy terms fail as predicted; AX-3 evades by breaking the glide ==")
cands = {
    "copy inversion   PS + DI PC": lambda t: PS + DI @ PC,
    "glide Dirac mass PS + i DI PC": lambda t: PS + 1j * DI @ PC,
    "copy shift       PS + e^{i pi/4} PC": lambda t: PS + np.exp(1j * np.pi / 4) * PC,
}
from scipy.optimize import minimize


def zero_hunt(f, n=8):
    r = np.random.default_rng(7); hits = 0
    obj = lambda th: np.min(abs(np.angle(np.linalg.eigvals(f(th)))))
    for st in r.uniform(0, 2 * np.pi, (n, 3)):
        x = minimize(obj, st, method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-11, "maxiter": 1500})
        if x.fun < 1e-6 and np.linalg.norm(np.angle(np.exp(1j * x.x))) > 0.1:
            hits += 1
    return hits


def k0_doublets(Af):
    U, G, _ = band(np.zeros(3), Af); L = lam(U, G, np.zeros(3)); w, v = np.linalg.eig(U); out = []
    for E in sorted(set(np.round(np.angle(w), 6))):
        if abs(E) > 1e-6:
            Q, _ = np.linalg.qr(v[:, abs(np.angle(w) - E) < 1e-5])
            out.append((round(float(E), 2), int(round(np.trace(Q.conj().T @ L @ Q).real))))
    return out


for k, (nm, Af) in enumerate(cands.items()):
    f = lambda t, Af=Af: band(t, Af)[0]
    nl0 = int(np.sum(abs(np.angle(np.linalg.eigvals(f(np.zeros(3))))) < 1e-9))
    nn, d0, dp = census(f); hz = zero_hunt(f)
    check(f"D{k + 1} {nm}: 4 light at K=0, copy levels (E, tr Lam) {k0_doublets(Af)} -> E=0 points off K=0 "
          f"in {hz}/8 searches, min dist to pi {dp:.3f}", nl0 == 4 and (hz > 0 or dp < 1e-6))
BEST = np.array([2.92241516, 0.99862395, 0.28155887, -1.55308283, -2.04218853, 3.21108179, 0.09865608, -2.69464758])


def A_best(th):
    We, Wo, P = build(th); DP = DG @ P
    Ce = PS + PC @ expm(1j * sum(c * B for c, B in zip(BEST[:4], [I8, ReC, DI, 1j * ReC @ DI]))) @ PC
    Co = PS + PC @ expm(1j * sum(c * B for c, B in zip(BEST[4:], [I8, ReC, DI, 1j * ReC @ DI]))) @ PC
    return Ce @ DP @ Co @ np.linalg.inv(DP)


zb = [float(np.min(abs(np.angle(np.linalg.eigvals(band(np.pi * np.array(v), A_best)[0])))))
      for v in ([.5, .5, .5], [.5, 1.5, 1.5], [1.5, .5, 1.5], [1.5, 1.5, .5])]
check("D4 best of a 12-start Nelder-Mead search over even+odd copy-sector cube unitaries (margin -> 0-, never > 0): "
      "an E = 0 doublet sits on the 4-orbit pi(1/2,1/2,1/2) of the turn axes (finite diagnostic)", max(zb) < 1e-4,
      f"min|E| there {max(zb):.1e}")


def ax3(th, M=0.7):
    We, Wo, P = build(th)
    Re, Ro = sum(We) / np.sqrt(3), sum(Wo) / np.sqrt(3)
    Ce = expm(1j * (M / 4) * (I8 - S) @ Re)
    return expm(1j * EPS * Ro) @ Ce @ expm(-1j * EPS * Re) @ Ce


ca = census(ax3); gb = np.abs(massless(th_r)[1] @ ax3(th_r) - ax3(th_r) @ massless(th_r)[1]).max()
check("D5 AX-3 (glide broken) evades: one light pair at K = 0, n_neg constant, no E=0 off K=0, pi-gap open",
      len(ca[0]) == 1 and ca[2] > 0.1 and gb > 0.1 and zero_hunt(ax3) == 0,
      f"|[G,U]| {gb:.2f}, n_neg {ca[0]}, grid min|E| {ca[1]:.3f}, min dist to pi {ca[2]:.3f}")
print("verdict: GLIDE-KEEP + 2-fold rotations + one light doublet per label is impossible at any range;")
print("open escapes: an odd number of extra light doublets per label (e.g. at the corner), break the 2-fold")
print("rotations (keep one turn), or a composite (multi-site/multi-mode) cell")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
