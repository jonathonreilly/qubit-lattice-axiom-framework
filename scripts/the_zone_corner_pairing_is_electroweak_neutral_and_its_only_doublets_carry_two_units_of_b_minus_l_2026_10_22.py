AUDIT_INPUT_PATHS = ('docs/THE_ZONE_CORNER_PAIRING_IS_ELECTROWEAK_NEUTRAL_AND_ITS_ONLY_DOUBLETS_CARRY_TWO_UNITS_OF_B_MINUS_L_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Does any structure the laws already contain give a scalar electroweak doublet (Y = 1/2, colour
singlet) as a composite or collective mode, without naming content?  (seeded, self-contained)

Sections:
  A  exact weight census of the 16, the so(10) roots, 16bar x 16 (Dirac pairs) and 16 x 16 (pairs)
  B  the CL-1 cube band and its step-pi/2 generator H' at the zone corner R = pi(1,1,1):
     which light-mirror bilinears are Lorentz scalars, what the corner pairing carries,
     which continuous symmetries it could break
  C  conditional coset: grant separate light and mirror rotations at R (not in the laws)
     -> misalignment angle, Yukawa-type selection by the Z4 = i^(B-L), gauge-loop alignment
  D  edge-dressed composites and the copy pair (copy factor commutant, the 10-channel angle)
  E  scale estimate and gate summary
"""
import itertools
import os
import time
from fractions import Fraction as Fr

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from scipy.linalg import expm, null_space

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0


def check(ok, tag, text):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}")


H = Fr(1, 2)
# ------------------------------------------------------------------ A. weights
print("== A. weight census (exact rationals)")
W16 = [w for w in itertools.product((H, -H), repeat=5) if sum(1 for x in w if x < 0) % 2 == 1]


def charges(w):
    s3 = w[0] + w[1] + w[2]
    bl = Fr(2, 3) * s3
    t3l, t3r = (w[3] + w[4]) / 2, (w[3] - w[4]) / 2
    col = tuple(x - s3 / 3 for x in w[:3])          # colour weight (orthogonal to (1,1,1))
    return dict(bl=bl, t3l=t3l, t3r=t3r, y=t3r + bl / 2, col=col, colourless=all(c == 0 for c in col))


C16 = [charges(w) for w in W16]


def name(c):
    if c["colourless"]:
        if c["t3l"] != 0:
            return "L"
        return {1: "e^c", 0: "n^c"}[int(c["y"])]
    if c["t3l"] != 0:
        return "q"
    return "u^c" if c["y"] == Fr(-2, 3) else "d^c"


cnt = {}
for c in C16:
    cnt[name(c)] = cnt.get(name(c), 0) + 1
ok = cnt == {"q": 6, "u^c": 3, "d^c": 3, "L": 2, "e^c": 1, "n^c": 1} and all(
    (name(c) != "u^c" or c["y"] == Fr(-2, 3)) and (name(c) != "q" or c["y"] == Fr(1, 6)) for c in C16)
check(ok, "A1", f"16 weights (+-1/2)^5, odd minus signs, B-L = (2/3)(w1+w2+w3), T3L,R = (w4 +- w5)/2, Y = T3R + (B-L)/2: content {cnt}")

roots = []
for i, j in itertools.combinations(range(5), 2):
    for si, sj in itertools.product((1, -1), repeat=2):
        r = [Fr(0)] * 5
        r[i], r[j] = Fr(si), Fr(sj)
        roots.append(tuple(r))
bad = [r for r in roots if charges(r)["colourless"] and charges(r)["t3l"] in (H, -H)]
check(len(roots) == 40 and not bad, "A2",
      f"so(10): 40 roots +-e_i +- e_j (+5 Cartan); colour-zero roots with T3L = +-1/2: {len(bad)}. "
      "No generator of Spin(10) is a colour-singlet doublet, so no Goldstone of any Spin(10)-breaking vacuum is one")


def census(sign):
    """sign=-1: 16bar x 16 (Dirac pair psi^dag chi); sign=+1: 16 x 16 (pair psi chi)."""
    out = {}
    for a, b in itertools.product(range(16), repeat=2):
        ca, cb = C16[a], C16[b]
        t3l = cb["t3l"] + sign * ca["t3l"]
        col = tuple(x + sign * y for x, y in zip(cb["col"], ca["col"]))
        if all(z == 0 for z in col) and t3l in (H, -H):
            y, bl = cb["y"] + sign * ca["y"], cb["bl"] + sign * ca["bl"]
            key = (str(y), str(bl))
            out.setdefault(key, set()).add((name(ca), name(cb), ca["colourless"] and cb["colourless"]))
    return out


Dp = census(-1)
okD = all(k[1] in ("2", "-2") for k in Dp) and set(k[0] for k in Dp) == {"1/2", "-1/2", "3/2", "-3/2"} \
    and all(all(x[2] for x in v) for v in Dp.values())
check(okD, "A3", "16bar x 16 (Dirac, psi^dag chi): every colour-zero, T3L = +-1/2 component comes from lepton x lepton "
      f"(so it is a colour singlet); (Y, B-L) = {sorted(Dp)}; constituents {sorted(set((x[0], x[1]) for v in Dp.values() for x in v))}. "
      "The Y = +1/2 doublet is Lbar n^c with B-L = +2: no B-L = 0 doublet")
Pp_ = census(+1)
okP = set(Pp_) == {("1/2", "0"), ("-1/2", "0")}
check(okP, "A4", f"16 x 16 (pair psi chi): colour-zero doublet components have (Y, B-L) = {sorted(Pp_)} only, "
      f"from {sorted(set((x[0], x[1]) for v in Pp_.values() for x in v))}: the B-L = 0 Higgs-type doublets live in pairs, not in Dirac bilinears")

# ------------------------------------------------------------------ B. band at R
print("== B. CL-1 cube band and H' at the zone corner R")
Cc = [tuple(c) for c in itertools.product((0, 1), repeat=3)]
idx = {c: a for a, c in enumerate(Cc)}
I8 = np.eye(8)
EPS = np.diag([(-1.0) ** sum(c) for c in Cc])


def eta(i, c):
    return (-1.0) ** sum(c[:i])


def Ri_e(i):
    M = np.zeros((8, 8))
    for c in Cc:
        if c[i] == 0:
            d = list(c); d[i] = 1; d = tuple(d)
            M[idx[d], idx[c]] = M[idx[c], idx[d]] = eta(i, c)
    return M


def Ri_o(i, K):
    M = np.zeros((8, 8), complex)
    for c in Cc:
        if c[i] == 1:
            d = list(c); d[i] = 0; d = tuple(d)
            M[idx[d], idx[c]] = eta(i, c) * np.exp(1j * K[i])
            M[idx[c], idx[d]] = eta(i, c) * np.exp(-1j * K[i])
    return M


RE = [Ri_e(i) for i in range(3)]
Re = sum(RE) / np.sqrt(3)


def Ro(K):
    return sum(Ri_o(i, K) for i in range(3)) / np.sqrt(3)


S = 1j * RE[0] @ RE[1] @ RE[2] @ Re              # copy sign s = i R1 R2 R3 R
Pp, Pm = (I8 + S) / 2, (I8 - S) / 2


def Hp(K):
    A = Ro(K)
    return 0.5j * (A @ Re - Re @ A)


GAM, RR = np.zeros(3), np.pi * np.ones(3)


def alph(P, h=1e-6):
    return [(Hp(P + h * np.eye(3)[a]) - Hp(P - h * np.eye(3)[a])) / (2 * h) for a in range(3)]


al = alph(RR)
v = np.sqrt(np.trace(al[0] @ al[0]).real / 8)
g5 = 1j * al[0] @ al[1] @ al[2] / v ** 3
chi = {}
for e in (1, -1):
    for c in (1, -1):
        Pr = (I8 + e * EPS) / 2 @ (I8 + c * S) / 2
        chi[(e, c)] = round(np.trace(g5 @ Pr).real / 2)
okc = all(chi[(e, c)] == -e * c for e in (1, -1) for c in (1, -1)) and np.abs(Hp(RR)).max() < 1e-12
check(okc, "B1", f"at R, H'(R) = 0 and each (eps, s) block is one Weyl of chirality -eps*s ({chi}). "
      "Same eps: light (s=+) and mirror (s=-) have OPPOSITE chirality, so their Lorentz scalar is Dirac psi^dag chi "
      "(internal 16bar x 16, A3). Same chirality needs opposite eps: an eps-odd pair (internal 16 x 16, A4)")

rows = [np.kron(EPS, I8) - np.kron(I8, EPS.T)] + [np.kron(x, I8) + np.kron(I8, x.T) for x in al]
nsR = null_space(np.vstack(rows))
Xs = []
for j in range(nsR.shape[1]):
    X = nsR[:, j].reshape(8, 8)
    for Y_ in (X + X.conj().T, 1j * (X - X.conj().T)):
        if np.abs(Y_).max() > 1e-8:
            Xs.append(Y_)
diag_s = max(max(np.abs(Pp @ X @ Pp).max(), np.abs(Pm @ X @ Pm).max()) for X in Xs)
Xm = Xs[0] / np.sqrt(np.trace(Xs[0] @ Xs[0]).real / 8)
ev, U = np.linalg.eigh(Xm)
mw = [np.real(U[:, k].conj() @ Pm @ U[:, k]) for k in range(8)]
check(nsR.shape[1] == 4 and diag_s < 1e-9 and np.allclose(mw, 0.5),
      "B2", f"eps-preserving masses at R: dim {nsR.shape[1]}, all purely s+ <-> s- (max diagonal block {diag_s:.0e}): "
      f"the corner pairing chirality needs is light-mirror Dirac; its eigenmodes are exactly half mirror (s- weight {np.round(mw[:2], 6)}), "
      "so the corner modes feel the mirror term at full strength")

grid = [np.array(k) for k in itertools.product(np.linspace(-np.pi, np.pi, 9)[:-1] + 0.1, repeat=3)]
cs = max(np.abs(S @ Hp(K) - Hp(K) @ S).max() for K in grid)
c_nodes = max(np.abs(S @ a - a @ S).max() for a in al)
Ks = [RNG.uniform(-np.pi, np.pi, 3) for _ in range(5)]
cm = null_space(np.vstack([np.kron(Hp(K), I8) - np.kron(I8, Hp(K).T) for K in Ks])).shape[1]
eo = max(np.abs(EPS @ X + X @ EPS).max() for X in (Re, Ro(Ks[0])))
check(cs > 0.1 and c_nodes < 1e-6 and cm == 2 and eo < 1e-12, "B3",
      f"max |[s, H'(K)]| off the nodes = {cs:.2f} (0 at the nodes, {c_nodes:.0e}); cell-local commutant of H' has dim {cm} = span(1, eps); "
      f"the CL-1 hops anticommute with eps ({eo:.0e}). So no update has a separate light or mirror rotation: the free generator's internal "
      "symmetry is at most U(16N)_eps+ x U(16N)_eps- (H') or U(16N) (CL-1), and both rotate the light and mirror corner modes together")
print("   => a gauge-invariant corner pairing is sum over the six SM multiplets of w_f (f^dag f'), each Y = 0, T = 0: EW-neutral;")
print("      the Spin(10)-singlet one (w_f all equal) commutes with every internal rotation: it breaks no continuous symmetry, so")
print("      its 210 doublet fluctuations (A3) are not Goldstones (estimate: two-fermion states near twice the corner gap).")

# ------------------------------------------------------------------ C. conditional coset
print("== C. conditional: grant separate light/mirror rotations at R (U(16) x U(16) -> U(16), not in the laws)")
lab = [name(c) for c in C16]
order = sorted(range(16), key=lambda a: (lab[a], C16[a]["col"], C16[a]["t3l"]))
Cs = [C16[a] for a in order]
labs = [lab[a] for a in order]
Yd = np.diag([float(c["y"]) for c in Cs])
BLd = np.diag([float(c["bl"]) for c in Cs])
T3d = np.diag([float(c["t3l"]) for c in Cs])
Qd = T3d + Yd
pos = {(labs[a], Cs[a]["col"], Cs[a]["t3l"]): a for a in range(16)}
T1 = np.zeros((16, 16)); T2 = np.zeros((16, 16), complex)
for a in range(16):
    if Cs[a]["t3l"] == H:
        b = pos[(labs[a], Cs[a]["col"], -H)]
        T1[a, b] = T1[b, a] = 0.5
        T2[a, b], T2[b, a] = -0.5j, 0.5j
lam = [np.array(m, complex) for m in (
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], np.diag([1, 1, -2]) / np.sqrt(3))]
# colour on 16: quarks by colour weight; fundamental on q, antifundamental on u^c, d^c
cw = sorted(set(Cs[a]["col"] for a in range(16) if labs[a] == "q"))
TC = []
for L_ in lam:
    M = np.zeros((16, 16), complex)
    for f, conj in (("q", False), ("u^c", True), ("d^c", True)):
        for t in ((H, -H) if f == "q" else (Fr(0),)):
            ids = [pos[(f, c, t)] for c in (cw if not conj else [tuple(-x for x in c) for c in cw])]
            M[np.ix_(ids, ids)] += (-L_.conj() if conj else L_) / 2
    TC.append(M)
cas = sum(T @ T for T in TC)
okcol = np.allclose(np.diag(cas)[[a for a in range(16) if labs[a] != "L" and labs[a][0] in "qud"]], 4 / 3) and \
    max(np.abs(TC[i] @ T1 - T1 @ TC[i]).max() for i in range(8)) < 1e-12
nu = [a for a in range(16) if labs[a] == "L" and abs(Qd[a, a]) < 1e-12][0]
nc = labs.index("n^c")
X = np.zeros((16, 16)); X[nu, nc] = X[nc, nu] = 1.0
th = np.linspace(0.05, np.pi, 12)
mw2 = np.array([sum(np.linalg.norm(T @ expm(1j * t * X) - expm(1j * t * X) @ T) ** 2 for T in (T1, T2)) for t in th])
colb = max(sum(np.linalg.norm(T @ expm(1j * t * X) - expm(1j * t * X) @ T) ** 2 for T in TC) for t in th)
qb = max(np.linalg.norm(Qd @ expm(1j * t * X) - expm(1j * t * X) @ Qd) for t in th)
blb = np.linalg.norm(BLd @ expm(1j * 1.0 * X) - expm(1j * 1.0 * X) @ BLd)
check(okcol and np.allclose(mw2 / mw2[-1], np.sin(th / 2) ** 2) and colb < 1e-20 and qb < 1e-12 and blb > 0.1, "C1",
      "Sigma = exp(i theta X), X = |n^c><nu| + h.c. (the neutral Lbar n^c direction of A3): colour Casimir 4/3 on quarks; "
      f"colour breaking {colb:.0e}, charge breaking {qb:.0e} at every theta; m_W^2(theta)/m_W^2(pi) = sin^2(theta/2) exactly, "
      f"so v = f sin(theta/2); B-L broken ({blb:.2f}). Unlike the 10's S^9, this coset HAS a colour-safe misalignment angle")
# Yukawa-type selection: Phi x (light pair psi_a psi_b), Lorentz-scalar pairs are 16 x 16
nY = {0: 0, 2: 0}
for a, b in itertools.combinations_with_replacement(range(16), 2):
    ca, cb = C16[a], C16[b]
    col = tuple(x + y for x, y in zip(ca["col"], cb["col"]))
    if all(z == 0 for z in col) and (ca["t3l"] + cb["t3l"]) in (H, -H) and abs(ca["y"] + cb["y"]) == H:
        for blphi in (0, 2, -2):
            tot = ca["bl"] + cb["bl"] + blphi
            if tot.denominator == 1 and int(tot) % 4 == 0:
                nY[abs(blphi)] += 1
check(nY[2] == 0 and nY[0] > 0, "C2",
      f"Yukawa-type terms Phi psi psi with a colour-singlet |Y| = 1/2 doublet Phi and a light Lorentz-scalar pair: allowed by Z4 = i^(B-L): "
      f"{nY[0]} weight-pairings for a B-L = 0 Phi (q u^c, q d^c, L e^c, L n^c), {nY[2]} for the corner doublet (B-L = +-2, Z4 charge 2). "
      "Any odd number of corner doublets has Z4 charge 2, so it gives no fermion a mass at ANY order; its vev breaks the Z4 (two vacua)")
g2, gp2 = 0.6517 ** 2, 0.3576 ** 2
Vg = np.array([g2 * sum(np.linalg.norm(T @ expm(1j * t * X) - expm(1j * t * X) @ T) ** 2 for T in (T1, T2, T3d))
               + gp2 * np.linalg.norm(Yd @ expm(1j * t * X) - expm(1j * t * X) @ Yd) ** 2 for t in th])
A_ = np.vstack([np.sin(th / 2) ** 2, np.sin(th) ** 2]).T
coef, res, *_ = np.linalg.lstsq(A_, Vg, rcond=None)
check(np.all(coef > 0) and np.abs(A_ @ coef - Vg).max() < 1e-10, "C3",
      f"gauge-loop invariant sum g^2 |[T, Sigma]|^2 = a sin^2(theta/2) + b sin^2(theta), a = {coef[0]:.3f}, b = {coef[1]:.3f} > 0: "
      "with the standard positive vector-like sign (supplied) the vacuum aligns at theta = 0. Misaligning needs a Z4-odd source; the laws have none")

# ------------------------------------------------------------------ D. edges and copies
print("== D. edge-dressed composites and the copy pair")
de = 5
Tm = [np.kron(T, np.eye(de)) for T in (T1, T2, T3d)]
Bm = np.kron(np.eye(16), RNG.normal(size=(de, de)))
cmix = max(np.abs(T @ Bm - Bm @ T).max() for T in Tm)
cas_c = sum(T @ T for T in Tm)
check(cmix < 1e-12 and np.allclose(np.diag(cas_c), np.repeat(np.diag(sum(T @ T for T in (T1, T2, T3d))).real, de)), "D1",
      "edge registers are gauge singlets with no B-L (Y = 0, centre-blind): on matter x edge the gauge generators are T x 1, so a "
      "dressed bilinear has its matter bilinear's Casimir, Y and B-L exactly; edge dressing reduces (b) to A3/A4")
Mc = 0.2
Dcopy = np.diag([0.0, Mc])
comm = null_space(np.vstack([np.kron(Dcopy, np.eye(2)) - np.kron(np.eye(2), Dcopy.T)])).shape[1]
check(comm == 2, "D2", f"copy factor: operators commuting with the copy mass diag(0, M) span dim {comm} = u(1) + u(1): abelian, "
      "no doublet generator; the copies carry the same 16, so copy-pair bilinears are 16bar x 16 or 16 x 16 (A3/A4), with the s = -1 member at M")
t_ = RNG.normal(size=3) + 1j * RNG.normal(size=3); t_ /= np.linalg.norm(t_)
h_ = RNG.normal(size=2) + 1j * RNG.normal(size=2); h_ /= np.linalg.norm(h_)
tau = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]])]
okS9 = True
for ang in (0.3, 0.9, 1.4):
    zc, zh = np.cos(ang) * t_, np.sin(ang) * h_
    w_ = sum(np.linalg.norm(T / 2 @ zh) ** 2 for T in tau)
    cb_ = sum(np.linalg.norm(L_ / 2 @ zc) ** 2 for L_ in lam)
    okS9 &= abs(w_ - np.sin(ang) ** 2 / 2) < 1e-12 and abs(cb_ - 4 / 3 * np.cos(ang) ** 2) < 1e-12
check(okS9, "D3", "the B-L = 0 doublets (A4) sit in the pair-square 10: on n = cos(theta) t + sin(theta) h the W sum is sin^2(theta)/2 "
      "and the colour-breaking sum (4/3) cos^2(theta), so unbroken colour forces v = f (mirror-condensate C3 rederived)")

# ------------------------------------------------------------------ E. scale and gate
print("== E. scale estimate and gate")
eps0 = 0.3
gapR = 2 * eps0
vf = 246.22 / 2.44e18
print(f"   corner modes sit at quasi-energy 2 eps0 = {gapR:.2f} per tick (cell scale), so f ~ M = 2.44e18 GeV and the conditional coset")
print(f"   needs sin(theta/2) = v/f ~ {vf:.1e}: FITTED (and Z4-odd). m_H and v/f are not computed: no unfitted input exists.")
check(vf < 1e-15, "E1", "estimate: f at the corner gap gives v/f ~ 1e-16; the angle would be a fitted 1e-16 with no source in the laws")
print("   GATE (tested candidate 'conserved copy sign at R'): (1) sin(theta/2) FITTED; (2) names no content (pass);")
print("   (3) predicts no Yukawa-type mass from the doublet (C2) -> contradicted by m_t = 172.6 GeV; Z4 breaking (Majorana nu, walls);")
print("   (4) bends Admissibility/CL-1 (s is not conserved off the nodes, B3). RESULT: FAIL; no structure yields a light B-L = 0 doublet.")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
