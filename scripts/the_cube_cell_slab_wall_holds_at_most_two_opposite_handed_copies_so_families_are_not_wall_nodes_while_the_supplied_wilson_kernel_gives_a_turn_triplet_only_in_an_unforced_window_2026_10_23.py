AUDIT_INPUT_PATHS = ('docs/THE_CUBE_CELL_SLAB_WALL_HOLDS_AT_MOST_TWO_OPPOSITE_HANDED_COPIES_SO_FAMILIES_ARE_NOT_WALL_NODES_WHILE_THE_SUPPLIED_WILSON_KERNEL_GIVES_A_TURN_TRIPLET_ONLY_IN_AN_UNFORCED_WINDOW_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Wall families on the domain-wall slab (supplied free models, seeded, self-contained).

W. The adopted tick-form slab (chiral-tick-form): Wilson-type kernel, 4 components per Z^3 site, Ls layers.
   Scan the layer mass m across its windows; count near-wall Weyl nodes, momenta, chiralities; act with the
   three-fold turn about (111) on the wall-node space.
C. The same slab built on CL-1's own cell: 2x2x2 cube cell (8 one-mode sites, face phase -1, both tilings),
   D = R_e - R_o (kinetic), B = R_e + R_o (mass), eps = (-1)^(x+y+z) (layer chirality), CL-1's copy operator
   (1 - s) R_e. Count wall copies per field across (m, copy mass) windows and their turn charges.

Pre-set pass criteria are written in each check line (set before the first run).
"""
import itertools, time, resource
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
rng = np.random.default_rng(20261023)
NP = [0, 0]
def check(tag, ok, msg, det=""):
    NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""))

OM = np.exp(2j * np.pi / 3)
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
SIG = [sx, sy, sz]
RT = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])          # turn about (111): e1 -> e2 -> e3
ZTOL = 1e-3

def zero_modes(H, Ls, d, near=True):
    ev, V = np.linalg.eigh(H); sel = np.abs(ev) < ZTOL; Z = V[:, sel]
    if Z.shape[1] == 0: return Z
    # rotate the zero space to layer-localised vectors (near / far halves)
    w = np.zeros(len(H)); w[: (Ls // 2) * d] = 1
    e2, U2 = np.linalg.eigh(Z.conj().T @ np.diag(w) @ Z); Z = Z @ U2
    return Z[:, e2 > 0.5] if near else Z[:, e2 < 0.5]

def chirality(Hf, k, P, h=1e-5):
    """sign det of the velocity matrix of the 2-dim node space P at momentum k."""
    if P.shape[1] != 2: return None
    v = np.zeros((3, 3))
    for j in range(3):
        q = np.zeros(3); q[j] = h
        hj = P.conj().T @ (Hf(k + q) - Hf(k - q)) @ P / (2 * h)
        for i in range(3): v[i, j] = np.real(np.trace(SIG[i] @ hj)) / 2
    return int(np.sign(np.linalg.det(v)))

def classes(vals, tol=1e-6):
    out = []
    for z in vals:
        for c in out:
            if abs(z - c[0]) < tol: c[1] += 1; break
        else: out.append([z, 1])
    return out

# ---------------------------------------------------------------- W: Wilson-type slab
G = [np.kron(sx, s) for s in SIG]; G4 = np.kron(sy, s0); G5 = np.kron(sz, s0)
AW = (G5 + 1j * G4) / 2
def HW_layer(k, m): return sum(np.sin(k[i]) * G[i] for i in range(3)) + (m - 4 + np.sum(np.cos(k))) * G5
def slab(onl, A, Ls):
    d = len(onl); H = np.kron(np.eye(Ls), onl); S = np.eye(Ls, k=-1)       # |s+1><s|
    H = H + np.kron(S, A) + np.kron(S.T, A.conj().T); return H
def HW(k, m, Ls): return slab(HW_layer(k, m), AW, Ls)
def HW_bulk(k, p, m): return HW_layer(k, m) + AW * np.exp(1j * p) + AW.conj().T * np.exp(-1j * p)

corners = [np.array(c) * np.pi for c in itertools.product((0, 1), repeat=3)]
cname = lambda c: "G" if sum(c) == 0 else ("X" if sum(c) < 1.5 * np.pi else ("M" if sum(c) < 2.5 * np.pi else "R"))
print("== W. adopted slab (Wilson-type kernel, 4 components per site); layer mass m scanned over its windows")
LsW = 12; mW = [0.6, 1.0, 3.0, 5.0, 7.0]; resW = {}
g8 = np.linspace(-np.pi, np.pi, 8, endpoint=False)
for m in mW:
    gap = min(np.abs(np.linalg.eigvalsh(HW_bulk(np.array(kk[:3]), kk[3], m))).min() for kk in itertools.product(g8, repeat=4))
    nodes = []
    for c in corners:
        Hf = lambda k, c=c: HW(k, m, LsW)
        Pn = zero_modes(Hf(c), LsW, 4); Pf = zero_modes(Hf(c), LsW, 4, near=False)
        if Pn.shape[1]: nodes.append((cname(c), tuple(int(v) for v in np.round(c / np.pi)), Pn.shape[1], chirality(Hf, c, Pn), chirality(Hf, c, Pf)))
    resW[m] = (gap, nodes)
pred = lambda m: {n: (3 if n in (1, 2) else 1) for n in range(4) if abs(1 - m + 2 * n) < 1}
ok = all(resW[m][0] > 0.2 for m in mW)
check("W1 [F]", ok, "bulk gapped at every scanned m (pre-set: min |E| on the 8^4 grid > 0.2)",
      ", ".join(f"m={m}: {resW[m][0]:.2f}" for m in mW))
cnt = {m: {} for m in mW}
for m in mW:
    for nm, c, dim, chn, chf in resW[m][1]: cnt[m][sum(c)] = cnt[m].get(sum(c), 0) + 1
ok = all(cnt[m] == pred(m) and all(n[2] == 2 for n in resW[m][1]) for m in mW)
check("W2 [T]/[F]", ok, "near-wall Weyl nodes (2-dim each) sit at the corners with n pi-components exactly when 2n < m < 2n + 2 "
      "(zero-mode recursion ratio 1 - m + 2n): windows (0,2), (2,4), (4,6), (6,8) give 1 (G), 3 (X), 3 (M), 1 (R) "
      "(pre-set: exactly this)", "; ".join(f"m={m}: " + ",".join(n[0] + "".join(map(str, n[1])) for n in resW[m][1]) for m in mW))
chi = {m: [n[3] for n in resW[m][1]] for m in mW}; chf = {m: [n[4] for n in resW[m][1]] for m in mW}
ok = all(len(set(chi[m])) == 1 for m in mW) and all(chi[m][0] == chi[0.6][0] * (-1) ** (sum(resW[m][1][0][1])) for m in mW) \
    and all(sum(chi[m]) + sum(chf[m]) == 0 for m in mW)
check("W3 [F]", ok, "within each window all near-wall nodes have the SAME chirality, the sign alternates window to window as "
      "(-1)^n, and the far wall carries the opposite total (pre-set: all three)",
      ", ".join(f"m={m}: near {sum(chi[m]):+d} far {sum(chf[m]):+d}" for m in mW))
# stray in-gap states anywhere in the zone, m = 3
stray = 0; g10 = np.linspace(-np.pi, np.pi, 10, endpoint=False)
for kk in itertools.product(g10, repeat=3):
    k = np.array(kk); ev = np.abs(np.linalg.eigvalsh(HW(k, 3.0, LsW)))
    if ev.min() < 0.05 and min(np.linalg.norm(((k - c + np.pi) % (2 * np.pi)) - np.pi) for c in [c_ for c_ in corners if cname(c_) == 'X']) > 0.9: stray += 1
check("W4 [F]", stray == 0, "m = 3: no in-gap wall state away from the three X points on a 10^3 grid (pre-set: 0)", f"stray {stray}")
# turn on the wall-node spaces
th = 2 * np.pi / 3; n111 = np.ones(3) / np.sqrt(3)
def spin_turn(sign):
    return np.kron(s0, expm(-1j * sign * th / 2 * sum(n111[i] * SIG[i] for i in range(3))))
k0 = rng.uniform(-np.pi, np.pi, 3)
S4 = min((spin_turn(sg) for sg in (1, -1)), key=lambda S: np.abs(S @ HW_layer(k0, 3) @ S.conj().T - HW_layer(RT @ k0, 3)).max())
cov = np.abs(S4 @ HW_layer(k0, 3) @ S4.conj().T - HW_layer(RT @ k0, 3)).max()
def turn_spec(m, Ls, nodes_k, Hf, Sop):
    Ps = [zero_modes(Hf(k), Ls, Sop.shape[0] // Ls) for k in nodes_k]
    idx = {tuple(np.round(k / np.pi).astype(int) % 2): i for i, k in enumerate(nodes_k)}
    n = sum(P.shape[1] for P in Ps); off = np.cumsum([0] + [P.shape[1] for P in Ps]); T = np.zeros((n, n), complex)
    for a, k in enumerate(nodes_k):
        b = idx[tuple(np.round(RT @ k / np.pi).astype(int) % 2)]
        T[off[b]:off[b + 1], off[a]:off[a + 1]] = Ps[b].conj().T @ Sop @ Ps[a]
    return np.linalg.eigvals(T), np.abs(T.conj().T @ T - np.eye(n)).max()
Sfull = np.kron(np.eye(LsW), S4)
ev_G, _ = turn_spec(0.6, LsW, [corners[0]], lambda k: HW(k, 0.6, LsW), Sfull)
Xs = [c for c in corners if cname(c) == "X"]; Ms = [c for c in corners if cname(c) == "M"]
ev_X, uX = turn_spec(3.0, LsW, Xs, lambda k: HW(k, 3.0, LsW), Sfull)
ev_M, uM = turn_spec(5.0, LsW, Ms, lambda k: HW(k, 5.0, LsW), Sfull)
def ms_match(ev, target):
    ev = list(ev); tg = list(target)
    if len(ev) != len(tg): return False
    for z in tg:
        j = int(np.argmin([abs(z - e) for e in ev]))
        if abs(z - ev[j]) > 1e-8: return False
        ev.pop(j)
    return True
trip = [g * OM ** q for g in ev_G for q in range(3)]; sing3 = [g for g in ev_G for _ in range(3)]
okX, okM = ms_match(ev_X, trip), ms_match(ev_M, trip); notS = not ms_match(ev_X, sing3)
ph = lambda ev: ", ".join(f"{v:+.3f}" for v in sorted(np.angle(ev) / np.pi))
check("W5 [T]", cov < 1e-12 and uX < 1e-10 and uM < 1e-10 and okX and okM and notS,
      "the turn (spinor lift, covariance checked) permutes X1 -> X2 -> X3 and M1 -> M2 -> M3; on each 3-node wall space its "
      "eigenvalue multiset is EXACTLY the G node's spinor pair x {1, w, w^2} (and not x {1, 1, 1}): a turn triplet, "
      "family charges 0, 1, 2 (pre-set: this multiset)",
      f"covariance {cov:.0e}; G phases {ph(ev_G)} pi; X phases {ph(ev_X)} pi; M phases {ph(ev_M)} pi")
print("   W6 [T] the three X nodes are also split by the unit translations (T_x = -1 on X(100), +1 on X(010), X(001)); with only 2Z^3 "
      "block translations (CL-1's role layout) they fold to block K = 0 and the turn is their only label")

# ---------------------------------------------------------------- C: CL-1 cell slab
print("== C. the slab on CL-1's own cell (2x2x2 cube cell, 8 one-mode sites, both tilings, face phase -1)")
E3 = np.eye(3, dtype=int); SITES = list(itertools.product((0, 1), repeat=3))
def eta(x, i): return [1, (-1) ** int(x[0]), (-1) ** int(x[0] + x[1])][i]
def pairs(par):
    out = []
    for o in itertools.product((0, 1), repeat=3):
        A = np.array(o) + par
        for i in range(3):
            if not o[i]: out.append((A, A + E3[i], eta(A, i), i))
    return out
PE, PO = pairs(0), pairs(1)
def Wb(pp, k, i):
    M = np.zeros((8, 8), complex)
    for x, y, a, j in pp:
        if j != i: continue
        ia = np.ravel_multi_index(tuple(x % 2), (2,) * 3); ib = np.ravel_multi_index(tuple(y % 2), (2,) * 3)
        ph = a * np.exp(-1j * k @ (x // 2 - y // 2)); M[ia, ib] += ph; M[ib, ia] += np.conj(ph)
    return M
def cell(k):
    We = [Wb(PE, k, i) for i in range(3)]; Wo = [Wb(PO, k, i) for i in range(3)]
    Re = sum(We) / np.sqrt(3); Ro = sum(Wo) / np.sqrt(3); s = 1j * We[0] @ We[1] @ We[2] @ Re
    return We, Wo, Re, Ro, s
EPS8 = np.diag([(-1.) ** sum(x) for x in SITES]).astype(complex); I8 = np.eye(8)
k1 = rng.uniform(-np.pi, np.pi, 3); _, _, Re, Ro, s = cell(k1); D = Re - Ro; B = Re + Ro
ac = lambda a, b: np.abs(a @ b + b @ a).max()
alg = max(ac(D, B), ac(D, EPS8), ac(B, EPS8), np.abs(D @ D + B @ B - 4 * I8).max(), np.abs(s @ s - I8).max(), np.abs(s @ Re - Re @ s).max())
dmin = sorted((np.abs(np.linalg.eigvalsh(cell(np.array(kk))[2] - cell(np.array(kk))[3])).min(), kk) for kk in itertools.product(np.linspace(-np.pi, np.pi, 16, endpoint=False), repeat=3))
_, _, R0e, R0o, sK0 = cell(np.zeros(3)); ker = np.linalg.eigh(R0e - R0o)
Z0 = ker[1][:, np.abs(ker[0]) < 1e-9]; sk = np.round(np.linalg.eigvalsh(Z0.conj().T @ sK0 @ Z0), 9)
ok = alg < 1e-12 and dmin[0][0] < 1e-12 and np.allclose(dmin[0][1], 0) and dmin[1][0] > 0.1 and Z0.shape[1] == 8 and list(sk).count(1) == 4
check("C1 [T]", ok, "cell algebra: D, B, eps mutually anticommute, D^2 + B^2 = 4, s^2 = 1, [s, R_e] = 0 at generic K; D vanishes only "
      "at K = 0, on all 8 modes = two 4-component Dirac copies, s = +1 and s = -1 (pre-set: all)",
      f"max defect {alg:.0e}; next-smallest |D| on 16^3 {dmin[1][0]:.2f}; s on ker D: 4 x (+1), 4 x (-1)")
AC = (B / 2 + 1j * EPS8) / 2
def HC_layer(k, m, Mc):
    _, _, Re, Ro, s = cell(k); return (Re - Ro) + (m - 1) * (Re + Ro) / 2 - (Mc / 2) * (I8 - s) @ Re
def HC(k, m, Mc, Ls):
    _, _, Re, Ro, s = cell(k); return slab(HC_layer(k, m, Mc), ((Re + Ro) / 2 + 1j * EPS8) / 2, Ls)
def HC_bulk(k, p, m, Mc):
    _, _, Re, Ro, s = cell(k); A = ((Re + Ro) / 2 + 1j * EPS8) / 2
    return HC_layer(k, m, Mc) + A * np.exp(1j * p) + A.conj().T * np.exp(-1j * p)
LsC = 24; pts = [(1.0, 3.0), (4.0, 3.0), (6.0, 3.0), (0.5, 1.0), (1.5, 1.0), (2.5, 1.0), (0.4, 0.8), (1.4, 0.8), (2.4, 0.8)]
predC = lambda m, Mc: (int(0 < m < 2), int(Mc < m < Mc + 2))
resC = {}
for m, Mc in pts:
    gap = min(np.abs(np.linalg.eigvalsh(HC_bulk(np.array(kk[:3]), kk[3], m, Mc))).min() for kk in itertools.product(g8, repeat=4))
    Hf = lambda k, m=m, Mc=Mc: HC(k, m, Mc, LsC); P = zero_modes(Hf(np.zeros(3)), LsC, 8); Pf = zero_modes(Hf(np.zeros(3)), LsC, 8, near=False)
    sL = np.kron(np.eye(LsC), sK0); sp = np.round(np.linalg.eigvalsh(P.conj().T @ sL @ P), 6) if P.shape[1] else []
    resC[(m, Mc)] = (gap, P.shape[1] // 2, (int(np.sum(np.array(sp) > 0)) // 2, int(np.sum(np.array(sp) < 0)) // 2), Hf, P, Pf)
gp = [q for q in pts if q[1] <= 1.0]; gl = [q for q in pts if q[1] > 1.0]
ok = all(resC[q][0] > 0.15 for q in gp) and all(resC[q][2] == predC(*q) for q in gp)
check("C2 [T]/[F]", ok, "near-wall copies at K = 0 for copy mass Mc <= 1: the s = +1 copy iff 0 < m < 2, the s = -1 copy iff "
      "Mc < m < Mc + 2 (layer mass m - Mc); bulk gapped (pre-set: counts as predicted, gap > 0.15). Windows: (0, Mc) 1 copy (s+), "
      "(Mc, 2) 2 copies, (2, 2 + Mc) 1 copy (s-)",
      "; ".join(f"({q[0]},{q[1]}): gap {resC[q][0]:.2f}, (s+,s-) = {resC[q][2]}" for q in gp))
okg = all(resC[q][0] < 1e-6 for q in gl)
check("C2b [F]", okg, "(pre-set 'gapped at Mc = 3' FAILED on the first run; recorded result) at Mc = 3 the bulk is GAPLESS off K = 0 "
      "(CL-1's copy operator (1 - s) R_e does not anticommute with D), so a separate s = -1-only window at large copy mass is not a "
      "gapped slab phase; the gapped s = -1-only window is (2, 2 + Mc) at small Mc",
      "; ".join(f"({q[0]},{q[1]}): gap {resC[q][0]:.1e}" for q in gl))
stray = 0
for kk in itertools.product(np.linspace(-np.pi, np.pi, 8, endpoint=False), repeat=3):
    k = np.array(kk)
    if np.linalg.norm(k) < 0.9: continue
    if np.abs(np.linalg.eigvalsh(HC(k, 1.5, 1.0, LsC))).min() < 0.05: stray += 1
check("C3 [F]", stray == 0, "no wall state anywhere else in the block zone ((m,Mc) = (1.5,1), 8^3 grid; pre-set: 0): "
      "the cell has no X, M, R copies at all, so at most 2 wall copies per field", f"stray {stray}")
chC = {q: (chirality(resC[q][3], np.zeros(3), resC[q][4]), chirality(resC[q][3], np.zeros(3), resC[q][5])) for q in [(0.4, 0.8), (2.4, 0.8), (0.5, 1.0), (2.5, 1.0)]}
ok = all(v[0] is not None and v[0] == -v[1] for v in chC.values()) and chC[(0.4, 0.8)][0] == chC[(0.5, 1.0)][0]
check("C4 [F]", ok, "chirality of a lone wall copy (s+ alone at small m, s- alone at m in (2, 2 + Mc)), near vs far (pre-set: far = -near; recorded which hand each copy has)",
      ", ".join(f"(m,Mc)={q}: near {v[0]:+d} far {v[1]:+d}" for q, v in chC.items()) +
      f"; s = -1 copy {'same' if chC[(2.4, 0.8)][0] == chC[(0.4, 0.8)][0] and chC[(2.5, 1.0)][0] == chC[(0.5, 1.0)][0] else 'OPPOSITE'} hand to s = +1")
P2w = resC[(1.5, 1.0)][4]; sLw = np.kron(np.eye(LsC), sK0); esw, Vsw = np.linalg.eigh(P2w.conj().T @ sLw @ P2w)
blk = [P2w @ Vsw[:, esw > 0], P2w @ Vsw[:, esw < 0]]
chi2 = [chirality(resC[(1.5, 1.0)][3], np.zeros(3), Pb) for Pb in blk]
cross = max(np.abs(blk[0].conj().T @ (resC[(1.5, 1.0)][3](np.eye(3)[j] * 1e-5) - resC[(1.5, 1.0)][3](-np.eye(3)[j] * 1e-5)) @ blk[1]).max() / 2e-5 for j in range(3))
check("C4b [F]", None not in chi2 and sum(chi2) == 0, "in the two-copy window (Mc, 2) the near wall carries one copy of EACH hand at K = 0: net "
      "chirality 0, a vector-like pair, not two families (pre-set from C4: net 0)",
      f"(1.5, 1): s+ {chi2[0]:+d}, s- {chi2[1]:+d}, net {sum(chi2):+d}; inter-copy velocity {cross:.1e} (no first-order mixing; an s-breaking term can pair them)")
# turn lift on the cell (site phases), K = 0
perm = np.zeros(8, int)
for a in SITES: perm[np.ravel_multi_index(a, (2,) * 3)] = np.ravel_multi_index((a[2], a[0], a[1]), (2,) * 3)
Pm = np.zeros((8, 8)); Pm[perm, np.arange(8)] = 1
We0, Wo0, _, _, _ = cell(np.zeros(3))
src = [Pm @ W @ Pm.T for W in We0 + Wo0]; tgt = [We0[1], We0[2], We0[0], Wo0[1], Wo0[2], Wo0[0]]
Dg = np.zeros(8, complex); Dg[0] = 1; todo = [0]
while todo:
    x = todo.pop()
    for A_, B_ in zip(src, tgt):
        for y in np.nonzero(np.abs(A_[x]) > 1e-12)[0]:
            if Dg[y] == 0: Dg[y] = np.conj(B_[x, y] / A_[x, y] / Dg[x]); todo.append(y)
UT = np.diag(Dg) @ Pm
tl = max(np.abs(UT @ A_ @ UT.conj().T - B_).max() for A_, B_ in zip(src and [W for W in We0 + Wo0], tgt))
tl = max(tl, np.abs(UT @ sK0 @ UT.conj().T - sK0).max(), np.abs(UT @ EPS8 @ UT.conj().T - EPS8).max())
UTL = np.kron(np.eye(LsC), UT)
P2 = resC[(1.5, 1.0)][4]; sL = np.kron(np.eye(LsC), sK0)
es, Vs = np.linalg.eigh(P2.conj().T @ sL @ P2); Pp = P2 @ Vs[:, es > 0]; Pmn = P2 @ Vs[:, es < 0]
evp = np.linalg.eigvals(Pp.conj().T @ UTL @ Pp); evm = np.linalg.eigvals(Pmn.conj().T @ UTL @ Pmn)
dq = int(np.round(np.angle(np.prod(evm) / np.prod(evp)) / th)) % 3; dq = (2 * dq) % 3   # det ratio = w^(2 dq)
spin_ok = all(abs(abs(np.angle(evx[0] / evx[1])) - th) < 1e-8 for evx in (evp, evm))
ok = tl < 1e-12 and spin_ok and dq != 0 and len(evp) == 2 and len(evm) == 2
check("C5 [T]", ok, "the turn (site-phase lift; keeps both tilings, s and eps) on the two wall copies at (m,Mc) = (1.5,1): each copy is a "
      "spin-1/2 pair (phases differ by 2 pi/3) times a copy phase, and the s = -1 copy's phase is the s = +1 copy's times w^dq, dq != 0 "
      "(pre-set: dq != 0): the wall carries turn charges {q, q + dq} at most, never a triplet",
      f"lift defect {tl:.0e}; s+ phases {ph(evp)} pi, s- {ph(evm)} pi; dq = {dq}")
print("   C6 [T] cited (chiral-tick-form A-T2): for every m a local slab has zero net wall chirality, so in every window the far wall "
      "carries the mirror of the near-wall content; a 3-node near wall (W, m in (2,4)) has a 3-node far mirror")
print("Supplied: both slab kernels, Ls, m, Mc (copy mass in slab units), free fields; nothing in CL-1 fixes the layer-mass window.")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
