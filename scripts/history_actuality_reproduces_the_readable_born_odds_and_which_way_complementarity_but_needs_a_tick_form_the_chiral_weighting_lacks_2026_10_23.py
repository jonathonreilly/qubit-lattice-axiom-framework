AUDIT_INPUT_PATHS = ('docs/HISTORY_ACTUALITY_REPRODUCES_THE_READABLE_BORN_ODDS_AND_WHICH_WAY_COMPLEMENTARITY_BUT_NEEDS_A_TICK_FORM_THE_CHIRAL_WEIGHTING_LACKS_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""History actuality test: one actual history drawn from the history weighting; a record = the class of a
site-local history partition that DECOHERES (decoherence functional D(a,b) = Tr(C_a rho C_b^+) = 0 for a != b;
Gell-Mann-Hartle / Griffiths consistent histories, supplied), selected among decohering partitions by least
surprise (least history entropy over maximal site-local sets).
A: qubit walk on a 4-site ring (coin qubit): single-time Born; unrecorded two-time partitions; pointer-recorded
   partitions vs CL-2's per-tick transport (fewest changes then greatest entropy, log-domain Sinkhorn).
B: which-way pointer: decoherence <-> fringe loss, V = |<p0|p1>| exactly; readers agree; record = outcome entropy.
C: arrow: coarse-graining, coherent erasure, two-boundary decoherence functional (which end is pure).
D: 2D U(1) overlap (Neuberger D, Narayanan-Neuberger chiral overlap with Wigner-Brillouin phase), 4x4 and 6x6:
   vector det >= 0; 3-4-5-0 chiral weight: phase, gauge variation, Q != 0 sectors; class weights by a flux record.
E: set selection (Dowker-Kent risk): Bell U x U* degeneracy; GHZ tridecompositional uniqueness (Elby-Bub 1994).
F: gravity source: single-time expectation of record/occupation density, history vs CL-2 trajectories.
Toy models, supplied coin/couplings; finite diagnostics plus exact identities. Self-contained; seeded; numpy+scipy."""
AUDIT_TIMEOUT_SEC = 120
import time, resource
import numpy as np
from scipy.optimize import linprog, minimize
from scipy.special import logsumexp

rng = np.random.default_rng(20261023)
T0 = time.time()
P = F = 0
def check(name, ok, info=""):
    global P, F
    if ok: P += 1
    else: F += 1
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

def dfun(vecs):                      # D[a,b] = <v_b|v_a> = Tr(C_a rho C_b^+), pure rho
    V = np.array(vecs).T
    return (V.conj().T @ V).T
def offdiag(Dm):
    return np.max(np.abs(Dm - np.diag(np.diag(Dm))))
def H2(p):
    p = np.asarray(p, float).ravel(); p = p[p > 1e-15]; return float(-(p * np.log2(p)).sum())

# ---------------- A. qubit walk, Born and CL-2 transport ----------------
L = 4; NM = 2 * L
def walk(theta=0.6):
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    S = np.zeros((NM, NM))
    for x in range(L):
        S[2 * ((x + 1) % L), 2 * x] = 1; S[2 * ((x - 1) % L) + 1, 2 * x + 1] = 1
    ph = np.diag(np.exp(1j * np.repeat(rng.uniform(0, 2 * np.pi, L), 2)))
    return ph @ S @ np.kron(np.eye(L), R)
U = walk()
psi0 = rng.normal(size=NM) + 1j * rng.normal(size=NM); psi0 /= np.linalg.norm(psi0)
def Pm(m, n=NM):
    v = np.zeros(n); v[m] = 1; return np.diag(v)
psi1 = U @ psi0; psi2 = U @ psi1
p1, p2 = np.abs(psi1) ** 2, np.abs(psi2) ** 2
D1 = dfun([Pm(m) @ psi1 for m in range(NM)])
check("A1 single-time mode partition decoheres and D(a,a) = Born exactly (any state)",
      offdiag(D1) < 1e-15 and np.allclose(np.diag(D1).real, p1, atol=1e-15), f"offdiag {offdiag(D1):.1e}")
hist = [(a, b) for a in range(NM) for b in range(NM)]
D2 = dfun([Pm(b) @ U @ Pm(a) @ psi1 for a, b in hist])
dg = np.diag(D2).real.reshape(NM, NM)
add_err = np.abs(dg.sum(0) - p2).max()
check("A2 unrecorded two-time mode partition does NOT decohere; D(a,a) not additive (prediction)",
      offdiag(D2) > 1e-2 and add_err > 1e-2, f"max offdiag {offdiag(D2):.3f}, marginal error {add_err:.3f}")

def transport(pa, pb, Ustep, eps=0.01, ncost=None):
    sup = np.abs(Ustep) > 1e-12                       # sup[j,i]: i -> j allowed
    C = ncost if ncost is not None else 2.0 * (1 - np.eye(len(pa)))
    n = len(pa)
    A_eq = []; b_eq = []
    for i in range(n):
        r = np.zeros((n, n)); r[i, :] = 1; A_eq.append(r.ravel()); b_eq.append(pa[i])
    for j in range(n):
        r = np.zeros((n, n)); r[:, j] = 1; A_eq.append(r.ravel()); b_eq.append(pb[j])
    bnds = [(0, None) if sup[j, i] else (0, 0) for i in range(n) for j in range(n)]
    lp = linprog(C.ravel(), A_eq=np.array(A_eq), b_eq=b_eq, bounds=bnds, method="highs")
    K = np.where(sup.T, -C / eps, -np.inf)
    la, lb = np.log(pa), np.log(pb); f = np.zeros(n); g = np.zeros(n)
    for _ in range(4000):
        f = la - logsumexp(K + g[None, :], axis=1)
        g = lb - logsumexp(K + f[:, None], axis=0)
    J = np.exp(K + f[:, None] + g[None, :])
    return lp, J
lp, J = transport(p1, p2, U)
merr = max(np.abs(J.sum(1) - p1).max(), np.abs(J.sum(0) - p2).max())
tv = 0.5 * np.abs(J - dg).sum()
check("A3 CL-2 transport exists for the walk tick, Born marginals kept; its two-time joint is not D(a,a)",
      lp.status == 0 and merr < 1e-9 and tv > 1e-2,
      f"LP min changes {lp.fun:.4f}, Sinkhorn cost {(J * 2 * (1 - np.eye(NM))).sum():.4f}, marg err {merr:.1e}, TV(J,Ddiag) {tv:.3f}")
# pointer register r in Z_L copies the site at t1: |x,c,r> -> |x,c,r+x>
NP = NM * L
Cp = np.zeros((NP, NP))
for m in range(NM):
    for r in range(L):
        Cp[m * L + (r + m // 2) % L, m * L + r] = 1
Ub = np.kron(U, np.eye(L))
phi0 = np.kron(psi0, np.eye(L)[0]); phi1 = Ub @ phi0; phi2 = Ub @ Cp @ phi1
def Psite(x):
    v = np.zeros(NP)
    for c in range(2):
        v[(2 * x + c) * L:(2 * x + c + 1) * L] = 1
    return np.diag(v)
hp = [(x, b) for x in range(L) for b in range(NM)]
Dp = dfun([np.kron(Pm(b), np.eye(L)) @ Ub @ Cp @ Psite(x) @ phi1 for x, b in hp])
born_rb = np.array([abs(phi2[b * L + x]) ** 2 for x, b in hp])
check("A4 pointer-recorded two-time partition decoheres exactly; D(a,a) = Born(pointer, mode) at t2",
      offdiag(Dp) < 1e-15 and np.allclose(np.diag(Dp).real, born_rb, atol=1e-15), f"offdiag {offdiag(Dp):.1e}")
pb1 = np.abs(Cp @ phi1) ** 2; pb2 = np.abs(phi2) ** 2
ncost = np.zeros((NP, NP))
for i in range(NP):
    for j in range(NP):
        ncost[i, j] = 2 * (i // L != j // L) + 2 * (i % L != j % L)
mask = (pb1 > 1e-14)
lpw, Jw = transport(pb1 + 1e-300, pb2 + 1e-300, Ub, ncost=ncost)
moved = sum(Jw[i, j] for i in range(NP) for j in range(NP) if i % L != j % L)
check("A5 CL-2 on the recorded toy: copy is a permutation, walk support never changes the pointer, so CL-2's "
      "readable (pointer, mode) joint = D(a,a)", lpw.status == 0 and moved < 1e-14, f"pointer change mass {moved:.1e}")

# ---------------- B. which-way pointer and complementarity ----------------
Hd = np.array([[1, 1], [1, -1]]) / np.sqrt(2); I2 = np.eye(2)
def Ry(t): return np.array([[np.cos(t / 2), -np.sin(t / 2)], [np.sin(t / 2), np.cos(t / 2)]])
def ctrl(Ug):  # control qubit 0 (A), target qubit 1 (B)
    return np.kron(np.diag([1, 0]), I2) + np.kron(np.diag([0, 1]), Ug)
def PA(a): return np.kron(np.diag([1 - a, a]), I2)
def PB(b): return np.kron(I2, np.diag([1 - b, b]))
e00 = np.array([1, 0, 0, 0], complex)
worst = 0; worstV = 0; rec = {}
for th in np.linspace(0, np.pi, 7):
    c = np.cos(th / 2); s1 = np.kron(Hd, I2) @ e00
    vs = []
    for ph in np.linspace(0, 2 * np.pi, 13):
        Ut = np.kron(Hd, I2) @ np.kron(np.diag([1, np.exp(1j * ph)]), I2) @ ctrl(Ry(th))
        w = PA(0) @ Ut @ s1; vs.append(np.vdot(w, w).real)
    V = (max(vs) - min(vs)) / (max(vs) + min(vs))
    Ut = np.kron(Hd, I2) @ ctrl(Ry(th))
    Dm = dfun([PA(o) @ Ut @ PA(a) @ s1 for a in (0, 1) for o in (0, 1)])
    eps_ = abs(Dm[0, 2]); rec[round(th, 6)] = (offdiag(Dm), V)
    worst = max(worst, abs(eps_ - abs(c) / 4)); worstV = max(worstV, abs(V - abs(c)))
check("B1 which-way set {path t1, port t2}: |D(L o,R o)| = |<p0|p1>|/4 and visibility V = |<p0|p1>| (7 couplings)",
      worst < 1e-12 and worstV < 1e-12, f"max dev {worst:.1e}, {worstV:.1e}")
o0, V0 = rec[0.0]; opi, Vpi = rec[round(np.pi, 6)]
check("B2 record (orthogonal pointer): decoheres, V = 0; no record (c = 1): |D_LR| = 1/4, path set inconsistent, V = 1",
      opi < 1e-15 and Vpi < 1e-12 and abs(o0 - 0.25) < 1e-12 and abs(V0 - 1) < 1e-12,
      f"offdiag {opi:.0e} / {o0:.2f}, V {Vpi:.0e} / {V0:.3f}")
# readers: th = pi, reader C copies B after BS2
def k3(a, b, c): return np.kron(np.kron(a, b), c)
CX_BC = k3(I2, np.diag([1, 0]), I2) + k3(I2, np.diag([0, 1]), np.array([[0, 1], [1, 0]]))
Ufull = CX_BC @ np.kron(np.kron(Hd, I2) @ ctrl(Ry(np.pi)), I2)
s1c = np.kron(np.kron(Hd, I2) @ e00, [1, 0])
def P3(i, v): return k3(*[np.diag([1 - v, v]) if k == i else I2 for k in range(3)])
lab = [(a, o, b, c) for a in (0, 1) for o in (0, 1) for b in (0, 1) for c in (0, 1)]
D3 = dfun([P3(0, o) @ P3(1, b) @ P3(2, c) @ Ufull @ P3(0, a) @ s1c for a, o, b, c in lab])
pr = np.diag(D3).real
dis = sum(p for p, (a, o, b, c) in zip(pr, lab) if b != c or b != a)
pj = {}
for p, (a, o, b, c) in zip(pr, lab):
    pj[(a, c)] = pj.get((a, c), 0) + p
MI = H2([sum(v for k, v in pj.items() if k[0] == a) for a in (0, 1)]) + \
     H2([sum(v for k, v in pj.items() if k[1] == c) for c in (0, 1)]) - H2(list(pj.values()))
check("B3 read once / two readers: {path, port, pointer, reader} decoheres; disagreeing classes have weight 0; "
      "the record carries exactly H(path) = 1 bit, a second reading adds 0",
      offdiag(D3) < 1e-15 and dis < 1e-15 and abs(MI - 1) < 1e-12, f"offdiag {offdiag(D3):.1e}, P(disagree) {dis:.0e}, I = {MI:.3f} bit")

# ---------------- C. arrow ----------------
Dco = np.zeros((2, 2), complex)
for i, (a, o, b, c) in enumerate(lab):
    for j, (a2, o2, b2, c2) in enumerate(lab):
        Dco[a, a2] += D3[i, j]
check("C1 coarse-graining a decohering set keeps it decohering, and the late set's path marginal = the t1 record odds",
      offdiag(Dco) < 1e-15 and np.allclose(np.diag(Dco).real, [0.5, 0.5]), "records accumulate when kept")
Uer = np.kron(Hd, I2) @ ctrl(Ry(-np.pi)) @ ctrl(Ry(np.pi))         # copy, then coherent un-copy
s1 = np.kron(Hd, I2) @ e00
De = dfun([PA(o) @ Uer @ PA(a) @ s1 for a in (0, 1) for o in (0, 1)])
Dt1 = dfun([PB(b) @ ctrl(Ry(np.pi)) @ PA(a) @ s1 for a in (0, 1) for b in (0, 1)])
Dsa = dfun([PA(o) @ np.kron(Hd, I2) @ ctrl(Ry(-np.pi)) @ PB(b) @ ctrl(Ry(np.pi)) @ PA(a) @ s1
            for a in (0, 1) for b in (0, 1) for o in (0, 1)])
check("C2 erasure: {path t1, pointer t1'} decoheres if the history ends at t1', but after a coherent un-copy no set "
      "holding path t1 or pointer t1' decoheres (|D| = 1/4): record status is fixed by the whole history",
      offdiag(Dt1) < 1e-15 and abs(abs(De[0, 2]) - 0.25) < 1e-12 and abs(offdiag(Dsa) - 0.25) < 1e-12,
      f"|D_LR| after erase {abs(De[0, 2]):.3f}; with pointer cut {offdiag(Dsa):.3f}")
def PBb(b, basis):
    v = (Hd if basis == "X" else I2)[:, b]; return np.kron(I2, np.outer(v, v.conj()))
res = {}
for basis in ("Z", "X"):
    Dm = dfun([PA(o) @ np.kron(Hd, I2) @ ctrl(Ry(-np.pi)) @ PBb(b, basis) @ ctrl(Ry(np.pi)) @ s1
               for b in (0, 1) for o in (0, 1)])
    res[basis] = offdiag(Dm)
po = abs((Uer @ s1)[0]) ** 2 + abs((Uer @ s1)[1]) ** 2
check("C3 eraser: pointer cut in Z or X at t1' both fail (prediction 1/4 each); the maximal decohering set is "
      "{port} with the fringe restored (P(port 0) = 1); no selector needed", abs(res["Z"] - 0.25) < 1e-12
      and abs(res["X"] - 0.25) < 1e-12 and abs(po - 1) < 1e-12, f"Z {res['Z']:.3f}, X {res['X']:.3f}, P(o=0) {po:.3f}")
# two-boundary decoherence functional D = Tr(rho_f C_a rho_i C_b^+)
CX = ctrl(np.array([[0, 1], [1, 0]]))
def two_state(rho_i, rho_f, early, late):
    labs = [(a, b) for a in (0, 1) for b in (0, 1)]
    Cs = [late(b) @ CX @ early(a) for a, b in labs]
    Dm = np.array([[np.trace(rho_f @ Ca @ rho_i @ Cb.conj().T) for Cb in Cs] for Ca in Cs])
    Dm /= np.trace(Dm).real
    pp = np.diag(Dm).real.reshape(2, 2)
    return offdiag(Dm), H2(pp.sum(1)) + H2(pp.sum(0)) - H2(pp)
plus = np.kron(Hd[:, 0], [1, 0]); rho_fw = np.outer(plus, plus); Id4 = np.eye(4)
rho_rf = np.kron(I2, np.diag([1, 0]))
f_past = two_state(rho_fw, Id4, lambda a: PA(a), lambda b: PB(b))     # path early, pointer late
f_fut = two_state(rho_fw, Id4, lambda b: PB(b), lambda a: PA(a))      # pointer early, path late
r_past = two_state(Id4 / 4, rho_rf, lambda a: PA(a), lambda b: PB(b))
r_fut = two_state(Id4 / 4, rho_rf, lambda b: PB(b), lambda a: PA(a))
check("C4 arrow is the boundary: pure ready pointer at the start -> records of the past only (I = 1, 0 bit); "
      "pure pointer at the end -> records of the future only (0, 1 bit)",
      abs(f_past[1] - 1) < 1e-12 and f_fut[1] < 1e-12 and r_past[1] < 1e-12 and abs(r_fut[1] - 1) < 1e-12
      and max(f_past[0], f_fut[0], r_past[0], r_fut[0]) < 1e-15,
      f"fw {f_past[1]:.2f}/{f_fut[1]:.2f}, rev {r_past[1]:.2f}/{r_fut[1]:.2f}")

# ---------------- D. 2D U(1) overlap ----------------
s1m = np.array([[0, 1], [1, 0]], complex); s2m = np.array([[0, -1j], [1j, 0]]); g5 = np.diag([1., -1]).astype(complex)
M0 = 1.0
def wilson(th, q, Ls):
    N = Ls * Ls; Dw = 2 * np.eye(2 * N, dtype=complex)
    for x in range(Ls):
        for y in range(Ls):
            i = x * Ls + y
            for mu, gm in ((0, s1m), (1, s2m)):
                j = ((x + 1) % Ls) * Ls + y if mu == 0 else x * Ls + (y + 1) % Ls
                u = np.exp(1j * q * th[mu, x, y]) * (-1 if (mu == 0 and x == Ls - 1) else 1)   # antiperiodic in the tick
                Dw[2 * i:2 * i + 2, 2 * j:2 * j + 2] += -0.5 * (np.eye(2) - gm) * u
                Dw[2 * j:2 * j + 2, 2 * i:2 * i + 2] += -0.5 * (np.eye(2) + gm) * np.conj(u)
    return Dw
def G5(N): return np.kron(np.eye(N), g5)
def Hov(th, q, Ls):
    N = Ls * Ls; return G5(N) @ (wilson(th, q, Ls) - M0 * np.eye(2 * N))
def vec_det(th, q, Ls):
    Hm = Hov(th, q, Ls); w, v = np.linalg.eigh(Hm)
    V = G5(Ls * Ls) @ (v * np.sign(w)) @ v.conj().T
    return np.linalg.det(np.eye(len(V)) + V)
def neg_vecs(Hm):
    w, v = np.linalg.eigh(Hm); return v[:, w < 0]
REF = {}
def chiral_det(th, q, Ls, hand):
    N = Ls * Ls; sgn = 1 if hand == "L" else -1
    key = (Ls, hand)
    if key not in REF:
        REF[key] = neg_vecs(sgn * Hov(np.zeros((2, Ls, Ls)), 1, Ls))
    Phi0 = REF[key]
    Phi = neg_vecs(sgn * Hov(th, q, Ls))
    pick = 1 if hand == "L" else 0                       # gamma5 = -1 (L) or +1 (R) components: H_+ = M gamma5
    Phip = np.zeros((2 * N, N), complex)
    for i in range(N): Phip[2 * i + pick, i] = 1
    z0 = np.linalg.det(Phip.conj().T @ Phi0); z0 = np.conj(z0) / abs(z0)   # free weight real positive
    if Phi.shape[1] != N: return 0.0 + 0j, Phi.shape[1] - N
    wb = np.linalg.det(Phi0.conj().T @ Phi)
    return np.linalg.det(Phip.conj().T @ Phi) * np.conj(wb) / abs(wb) * z0, 0
def flux_bg(Ls, Q):
    th = np.zeros((2, Ls, Ls))
    for x in range(Ls):
        th[1, x, :] = 2 * np.pi * Q * x / Ls ** 2
    th[0, Ls - 1, :] = -2 * np.pi * Q * np.arange(Ls) / Ls
    return th
def topQ(th, Ls):
    pl = th[0] + np.roll(th[1], -1, 0) - np.roll(th[0], -1, 1) - th[1]
    return np.round(np.angle(np.exp(1j * pl)).sum() / (2 * np.pi), 6)
def W3450(th, Ls):
    d3, _ = chiral_det(th, 3, Ls, "L"); d4, _ = chiral_det(th, 4, Ls, "L"); d5, _ = chiral_det(th, 5, Ls, "R")
    return d3 * d4 * d5
vimag = 0; vneg = 0; ph_max = {}; gv = {}; lr = 0; qs = set()
for Ls in (4, 6):
    phs = []
    for k in range(5):
        th = 0.03 * rng.normal(size=(2, Ls, Ls)); qs.add(topQ(5 * th, Ls))
        for q in (1, 3):
            dv = vec_det(th, q, Ls); vimag = max(vimag, abs(dv.imag) / abs(dv)); vneg += dv.real < 0
        dl, _ = chiral_det(th, 1, Ls, "L"); dr, _ = chiral_det(th, 1, Ls, "R"); lr = max(lr, abs(np.angle(dl * dr)))
        phs.append(abs(np.angle(W3450(th, Ls))))
    ph_max[Ls] = max(phs)
    th = 0.03 * rng.normal(size=(2, Ls, Ls)); om = 0.05 * rng.normal(size=(Ls, Ls))
    thg = th.copy(); thg[0] += om - np.roll(om, -1, 0); thg[1] += om - np.roll(om, -1, 1)
    d5a, _ = chiral_det(th, 5, Ls, "L"); d5b, _ = chiral_det(thg, 5, Ls, "L")
    gv[Ls] = (abs(np.angle(d5b / d5a)), abs(np.angle(W3450(thg, Ls) / W3450(th, Ls))))
check("D1 vector-like overlap (antiperiodic tick): det(1+V) real, >= 0 on every background; an L x R pair of one "
      "charge is real too (positive history measure)", vimag < 1e-10 and vneg == 0 and lr < 1e-10,
      f"max |Im/det| {vimag:.1e}, negatives {vneg}, max |arg L x R| {lr:.1e}")
check("D2 chiral 3-4-5-0 weight at Q = 0 is complex: small nonzero phase growing with roughness (prediction 1e-7..0.1)",
      qs == {0.0} and all(1e-7 < v < 0.1 for v in ph_max.values()), ", ".join(f"{l}x{l}: max|arg| {v:.1e}" for l, v in ph_max.items()))
check("D3 WB-phase gauge variation: single charge-5 L det varies, anomaly-free product less (first prediction; a later 10x threshold fails on 6x6)",
      all(b < a for a, b in gv.values()), ", ".join(f"{l}x{l}: q5 {a:.1e}, 3450 {b:.1e}, ratio {a / b:.0f}" for l, (a, b) in gv.items()))
mism = {q: chiral_det(flux_bg(6, 1), q, 6, "L" if q != 5 else "R")[1] for q in (3, 4, 5)}
check("D4 Q=1 sector (6x6): negative-mode counts shift by the charge (3+4 L zero modes vs 5 R), weight 0 "
      "without fermion insertions", all(abs(mism[q]) == q for q in (3, 4, 5)), f"shifts {mism}")
# class weights by a local flux record: sign of plaquette (0,0) angle; Q = 0 sample, Gaussian gauge weight
Ls = 4; wcl = {+1: 0j, -1: 0j}; wv = {+1: 0., -1: 0.}
for k in range(24):
    th = 0.04 * rng.normal(size=(2, Ls, Ls))
    pl = th[0, 0, 0] + th[1, 1, 0] - th[0, 0, 1] - th[1, 0, 0]
    sg = 1 if pl >= 0 else -1; w = W3450(th, Ls)
    wcl[sg] += w; wv[sg] += abs(w) ** 2
argc = max(abs(np.angle(v)) for v in wcl.values())
check("D5 classes of Euclidean histories by a local flux record: chiral class weights complex (not probabilities); "
      "only |W|^2 (mirror added = vector-like) is positive", argc > 1e-9 and min(wv.values()) > 0,
      f"max class |arg| {argc:.2e}")

# ---------------- E. set selection ----------------
def rand_u():
    z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))
bell = np.array([1, 0, 0, 1]) / np.sqrt(2); hs = []
for _ in range(5):
    u = rand_u(); B = np.kron(u, u.conj())
    hs.append(H2(np.abs(B.conj().T @ bell) ** 2))
check("E1 two-site record (Bell state): every U x U* local basis is a decohering finest set at least surprise "
      "(H = 1 bit): least surprise does NOT fix the set", max(abs(h - 1) for h in hs) < 1e-12, f"H = {np.round(hs, 12)}")
ghz = np.zeros(8); ghz[0] = ghz[7] = 1 / np.sqrt(2)
def basis(a, b):
    v0 = np.array([np.cos(a / 2), np.exp(1j * b) * np.sin(a / 2)]); v1 = np.array([-np.exp(-1j * b) * np.sin(a / 2), np.cos(a / 2)])
    return np.array([v0, v1]).T
def hghz(x):
    B = np.kron(np.kron(basis(x[0], x[1]), basis(x[2], x[3])), basis(x[4], x[5]))
    return H2(np.abs(B.conj().T @ ghz) ** 2)
mins = []
for _ in range(12):
    r = minimize(hghz, rng.uniform(0, np.pi, 6), method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 4000})
    mins.append((r.fun, np.abs(np.sin(r.x[[0, 2, 4]])).max()))
best = [m for m in mins if m[0] < 1 + 1e-6]
check("E2 three-site redundant record (GHZ): every least-surprise local basis found is the Z basis "
      "(tridecompositional uniqueness, supplied): the selector fixes the set", len(best) > 0 and max(b[1] for b in best) < 1e-3,
      f"{len(best)}/12 starts reach H = 1; max tilt {max(b[1] for b in best):.1e}; other minima H >= {min([m[0] for m in mins if m[0] > 1 + 1e-6] or [9]):.2f}")
hn = H2(np.abs(np.array([ghz, *np.linalg.qr(np.column_stack([ghz, rng.normal(size=(8, 7))]))[0][:, 1:].T]) @ ghz) ** 2)
check("E3 without site-locality the least-surprise partition is the state itself (H = 0): locality is the "
      "Record axiom's, not the selector's", hn < 1e-12, f"H = {hn:.1e}")

# ---------------- F. gravity source ----------------
Tt = 10; ps = [psi0]
for t in range(Tt): ps.append(U @ ps[-1])
pt = [np.abs(p) ** 2 for p in ps]
Ks = []
for t in range(Tt):
    _, Jt = transport(pt[t], pt[t + 1], U)
    Ks.append(Jt / Jt.sum(1, keepdims=True))
Ns = 4000; cnt = np.zeros((Ns, L))
for n in range(Ns):
    m = rng.choice(NM, p=pt[0] / pt[0].sum())
    for t in range(Tt):
        m = rng.choice(NM, p=Ks[t][m] / Ks[t][m].sum()); cnt[n, m // 2] += 1
born_site = sum(p.reshape(L, 2).sum(1) for p in pt[1:])
z = (cnt.mean(0) - born_site) / (cnt.std(0) / np.sqrt(Ns))
check("F1 source expectation: CL-2 record counts per site = sum of single-time Born odds = diagonal D of the "
      "single-time sets (static tick-fraction exterior needs only this)", np.abs(z).max() < 4, f"max z {np.abs(z).max():.2f}")
print("Supplied: decoherence-functional rule (Gell-Mann-Hartle/Griffiths), coin angle, pointer couplings, m0=1, "
      "3-4-5-0 content, WB phase convention (Narayanan-Neuberger), Elby-Bub uniqueness. Toys only.")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.0f} MB")
print(f"TOTAL: PASS={P} FAIL={F}")
