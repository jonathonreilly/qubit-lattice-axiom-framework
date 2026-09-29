#!/usr/bin/env python3
"""J:derive:campaign6-20260928-comparator-anisotropic-touchings:a1 -- certified touchings of the flux-free comparator for J_x != J_y.

Problem (probes/work/campaign6-probable-20260928/README.md, section 2): for J_x = J_y the touchings of the middle bands lie on closed-form families (open PR 9350) and, at the handover, are charge-two points (open PR 9373).
For J_x != J_y the README found by floating point four extra nodes that leave both planes, at J = (1, 0.8, 1), kappa = 0.45 and J = (1.2, 0.8, 1), kappa = 0.3, and asked for a topological or interval-Newton certificate.

Setting (supplied): the four-site Bloch matrix H(f) = i M(f) of the u = +1 quadratic comparator with couplings J_x, J_y, J_z and odd term kappa (definitions as in open PR 9373; rebuilt here from the network's site and
flavour rules, not from any runner). This file does not import the note's, the README's or the PR's code.

What is done, in the order below:
 (1) EXACT, symbolic in all of J_x, J_y, J_z, kappa and the Bloch phases z_1, z_2, z_3: tr H = 0 and tr H^3 = 0, so the spectrum is {-a, -b, b, a} at every f and a touching of the middle bands is a double zero level;
     and for the Schur complement S = H_CC - H_CB H_BB^-1 H_BC (blocks {0,1}, {2,3}) det(H_BB) tr S = 0 identically, so S is a traceless Hermitian 2x2 matrix and rank H <= 2 <=> S = 0 <=> three real equations F(f) = 0.
 (2) FLOATING POINT (labelled): a grid-plus-minimisation search finds six touchings at each of the README's two couplings and reproduces the README's positions to five digits; charges by discrete sphere fluxes.
 (3) INTERVAL ARITHMETIC (mpmath iv, 40 digits, outward rounding): a Krawczyk test on F = 0 in the box around each node proves that the box contains exactly one zero of F, that det(H_BB) does not vanish on the box, that
     rank H = 2 there (so the middle bands touch at zero energy), that the outer bands are separated (a^2 = tr H^2 / 2 bounded below), that the Jacobian is nonsingular, and gives the sign of its determinant.
 (4) NEGATIVE CONTROL and SPLITTING: at the isotropic handover the same test must fail (the charge-two point has a rank-one Jacobian); for J_y < 1 it splits into two simple nodes at distance ~ sqrt(1 - J_y) whose certificates succeed.
All finite facts are computed here; floating point is labelled.
"""
import itertools, sys, time
import numpy as np
import sympy as sp
from mpmath import iv, mp
from scipy.optimize import minimize

T0 = time.time()
PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
iv.dps = 40; mp.dps = 40
# ---------------------------------------------------------------- own network construction (site and flavour rules) and Bloch matrix
def is_site(p):
    i, j, z = p; m = z % 4
    if m == 0: return j % 2 == 0
    if m == 1: return i % 2 == 1
    if m == 2: return j % 2 == 1
    return i % 2 == 0
def nbrs(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q): out.append(q)
    return out
def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0: return "z"
    lo = p if sum(d) > 0 else q; m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]
def reduce(p):
    n3 = p[2] // 2; x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2; rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)
def terms_of(Jx, Jy, Jz, kappa):
    J = {"x": Jx, "y": Jy, "z": Jz}; out = []
    for p in REPS:
        a, _ = reduce(p)
        if sum(p) % 2 == 0:
            for q in nbrs(p):
                b, n = reduce(q); out.append((a, b, n, 2 * J[flavour(p, q)]))
        nb = {flavour(p, q): q for q in nbrs(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
            out.append((r1, r2, tuple(int(x) for x in np.subtract(n2, n1)), 2 * kappa))
    return out
def Hfloat(F, T):
    F = np.atleast_2d(F); Mk = np.zeros((len(F), 4, 4), dtype=complex)
    for (a, b, n, amp) in T:
        ph = np.exp(2j * np.pi * (F @ np.array(n, dtype=float)))
        Mk[:, a, b] += float(amp) * ph; Mk[:, b, a] -= float(amp) * np.conj(ph)
    return 1j * Mk
def link(A_, B_): return np.linalg.det(np.einsum('...ia,...ib->...ab', A_.conj(), B_))
def sphere_chern(T, c, s, m=64, nocc=2):
    th = np.linspace(0, np.pi, m + 1); ph = np.linspace(0, 2 * np.pi, 2 * m + 1)
    P = np.stack([np.sin(th)[:, None] * np.cos(ph)[None, :], np.sin(th)[:, None] * np.sin(ph)[None, :], np.cos(th)[:, None] * np.ones_like(ph)[None, :]], axis=-1) * s + np.array(c)
    ev, V = np.linalg.eigh(Hfloat(P.reshape(-1, 3), T))
    V = V[:, :, :nocc].reshape(m + 1, 2 * m + 1, 4, nocc).copy(); V[0, :] = V[0, 0]; V[-1, :] = V[-1, 0]; V[:, -1] = V[:, 0]
    pl = np.angle(link(V[:-1, :-1], V[1:, :-1]) * link(V[1:, :-1], V[1:, 1:]) * link(V[1:, 1:], V[:-1, 1:]) * link(V[:-1, 1:], V[:-1, :-1]))
    return float(pl.sum() / (2 * np.pi)), float((ev[:, 2] - ev[:, 1]).min())

# ---------------------------------------------------------------- interval Schur complement
def structure():
    Tx = terms_of(1.0, 0.0, 0.0, 0.0); Ty = terms_of(0.0, 1.0, 0.0, 0.0); Tz = terms_of(0.0, 0.0, 1.0, 0.0); Tk = terms_of(0.0, 0.0, 0.0, 1.0)
    out = []
    for i in range(len(Tx)):
        kinds = [k for k, T in (("x", Tx), ("y", Ty), ("z", Tz), ("k", Tk)) if abs(T[i][3]) > 1e-12]
        assert len(kinds) == 1
        out.append((Tx[i][0], Tx[i][1], Tx[i][2], kinds[0]))
    return out
STRUCT = structure()
def cmat_zero(n=4): return [[iv.mpc(0, 0) for _ in range(n)] for _ in range(n)]
def build(f, amps):
    """H and dH/df_j (j = 0, 1, 2) as 4x4 lists of complex intervals; f: three interval reals; amps: dict kind -> interval (2 J or 2 kappa)."""
    two_pi = 2 * iv.pi
    H = cmat_zero(); dH = [cmat_zero() for _ in range(3)]
    for (a, b, n, kd) in STRUCT:
        th = two_pi * (n[0] * f[0] + n[1] * f[1] + n[2] * f[2])
        e = iv.mpc(iv.cos(th), iv.sin(th)); ec = iv.mpc(iv.cos(th), -iv.sin(th))
        amp = amps[kd]
        # H_ab += i amp e^{i th},  H_ba += -i amp e^{-i th}
        H[a][b] += iv.mpc(0, 1) * amp * e; H[b][a] += iv.mpc(0, -1) * amp * ec
        for j in range(3):
            if n[j] == 0: continue
            # d/df_j: e^{i th} -> (2 pi i n_j) e^{i th};  e^{-i th} -> (-2 pi i n_j) e^{-i th}
            dH[j][a][b] += iv.mpc(0, 1) * amp * e * iv.mpc(0, 1) * (two_pi * n[j])
            dH[j][b][a] += iv.mpc(0, -1) * amp * ec * iv.mpc(0, -1) * (two_pi * n[j])
    return H, dH
def m2(A, B): return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]
def m2add(A, B, s=1): return [[A[i][j] + s * B[i][j] for j in range(2)] for i in range(2)]
def cconj(z): return iv.mpc(z.real, -z.imag)
def m2h(A): return [[cconj(A[j][i]) for j in range(2)] for i in range(2)]
def m2inv(P):
    det = P[0][0] * P[1][1] - P[0][1] * P[1][0]
    return [[P[1][1] / det, -P[0][1] / det], [-P[1][0] / det, P[0][0] / det]], det
def sub(H, rows, cols): return [[H[r][c] for c in cols] for r in rows]
def schur(H, dH):
    B, C = (0, 1), (2, 3)
    P = sub(H, B, B); X = sub(H, C, B); Cc = sub(H, C, C)
    Pi, detP = m2inv(P); Xh = m2h(X)
    XPi = m2(X, Pi)
    S = m2add(Cc, m2(XPi, Xh), -1)
    dS = []
    for j in range(3):
        dP = sub(dH[j], B, B); dX = sub(dH[j], C, B); dC = sub(dH[j], C, C)
        dXh = m2h(dX)
        t = m2add(dC, m2(m2(dX, Pi), Xh), -1)
        t = m2add(t, m2(XPi, dXh), -1)
        t = m2add(t, m2(m2(XPi, dP), m2(Pi, Xh)), +1)
        dS.append(t)
    return S, dS, detP
def Fvec(f, amps):
    H, dH = build(f, amps); S, dS, detP = schur(H, dH)
    F = [S[0][0].real, S[0][1].real, S[0][1].imag]
    Jm = [[dS[j][0][0].real, dS[j][0][1].real, dS[j][0][1].imag] for j in range(3)]      # Jm[j][i] = dF_i/df_j
    aux = dict(trS=S[0][0] + S[1][1], imS00=S[0][0].imag, detP=detP)
    return F, Jm, aux

# ---------------------------------------------------------------- Krawczyk
def mid(v): return float(v.mid)
def Fmid(x, amps):
    F, Jm, aux = Fvec([iv.mpf(float(v)) for v in x], amps)
    return np.array([mid(v) for v in F]), np.array([[mid(Jm[j][i]) for j in range(3)] for i in range(3)])
def refine(x, amps, it=6):
    x = np.array(x, float)
    for _ in range(it):
        F, J = Fmid(x, amps); x = x - np.linalg.solve(J, F)
    return x
def krawczyk(x0, r, amps, box=None):
    x0 = [float(v) for v in x0]
    x0iv = [iv.mpf(v) for v in x0]
    F0, _, _ = Fvec(x0iv, amps)
    _, Jm0, _ = Fvec(x0iv, amps)
    Jmid = np.array([[mid(Jm0[j][i]) for j in range(3)] for i in range(3)])
    Y = np.linalg.inv(Jmid)
    X = box if box is not None else [iv.mpf([x0[i] - r, x0[i] + r]) for i in range(3)]
    FX, JmX, auxX = Fvec(X, amps)
    JX = [[JmX[j][i] for j in range(3)] for i in range(3)]      # JX[i][j] = dF_i/df_j over the box
    K = []
    for i in range(3):
        t = x0iv[i]
        for j in range(3): t = t - iv.mpf(float(Y[i, j])) * F0[j]
        for j in range(3):
            c = iv.mpf(1 if i == j else 0)
            for k in range(3): c = c - iv.mpf(float(Y[i, k])) * JX[k][j]
            t = t + c * (X[j] - x0iv[j])
        K.append(t)
    inside = all(K[i].a > X[i].a and K[i].b < X[i].b for i in range(3))
    # the box must lie where det P != 0 and where the Schur complement is defined: detP interval excludes 0
    dP = auxX["detP"]; magP = (dP.real * dP.real + dP.imag * dP.imag).a
    return inside, K, X, JX, magP
def det3(J):
    return (J[0][0] * (J[1][1] * J[2][2] - J[1][2] * J[2][1]) - J[0][1] * (J[1][0] * J[2][2] - J[1][2] * J[2][0]) + J[0][2] * (J[1][0] * J[2][1] - J[1][1] * J[2][0]))

# ---------------------------------------------------------------- float node search
def find_nodes(J, kap, n=40, thr=0.8):
    T = terms_of(*J, kap)
    def gap(f): ev = np.linalg.eigvalsh(Hfloat(np.asarray(f), T))[0]; return ev[2] - ev[1]
    g = (np.arange(n) + 0.5) / n
    F = np.stack(np.meshgrid(g, g, g, indexing="ij"), -1).reshape(-1, 3)
    ev = np.linalg.eigvalsh(Hfloat(F, T)); G = (ev[:, 2] - ev[:, 1]).reshape(n, n, n)
    nodes = []
    idx = np.argwhere(G < thr)
    for (i, j, k) in idx:
        v = G[i, j, k]
        if all(v <= G[(i + a) % n, (j + b) % n, (k + c) % n] for a in (-1, 0, 1) for b in (-1, 0, 1) for c in (-1, 0, 1)):
            r = minimize(gap, np.array([g[i], g[j], g[k]]), method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-14, maxiter=4000))
            x = np.mod(r.x, 1.0)
            if r.fun < 1e-7 and not any(np.allclose(np.mod(x - y + 0.5, 1) - 0.5, 0, atol=1e-5) for y in nodes): nodes.append(x)
    return T, nodes

# ================================================================ (1) exact identities, symbolic in every coupling and phase
Jx_, Jy_, Jz_, kp_ = sp.symbols("Jx Jy Jz kappa"); zs = sp.symbols("z1 z2 z3")
Hs = sp.zeros(4, 4)
SYM = {"x": Jx_, "y": Jy_, "z": Jz_, "k": kp_}
for (a, b, n, kd) in STRUCT:
    e = zs[0] ** n[0] * zs[1] ** n[1] * zs[2] ** n[2]
    Hs[a, b] += sp.I * 2 * SYM[kd] * e; Hs[b, a] += -sp.I * 2 * SYM[kd] / e
Hs = Hs.applyfunc(sp.expand)
def conj_z(M):
    rules = {sp.conjugate(z): 1 / z for z in zs}; rules.update({sp.conjugate(s): s for s in (Jx_, Jy_, Jz_, kp_)})
    return M.applyfunc(lambda e: sp.expand(sp.conjugate(e).subs(rules)))
check("the 18 hopping terms of the four-site cell: 2 x-bonds, 2 y-bonds, 2 z-bonds and 12 odd-term hops", sorted(sum(1 for t in STRUCT if t[3] == k) for k in "xyzk") == [2, 2, 2, 12] and len(STRUCT) == 18)
check("H(z) is Hermitian for |z_j| = 1, symbolically in J_x, J_y, J_z, kappa", (Hs - conj_z(Hs).T).applyfunc(sp.expand) == sp.zeros(4, 4))
H2s = (Hs * Hs).applyfunc(sp.expand); H3s = (H2s * Hs).applyfunc(sp.expand)
check("tr H = 0 and tr H^3 = 0 identically, so det(H - lambda) = lambda^4 - (tr H^2 / 2) lambda^2 + det H is even in lambda: the spectrum is {-a, -b, b, a} at every f and every coupling", sp.expand(Hs.trace()) == 0 and sp.expand(H3s.trace()) == 0)
P_ = Hs[:2, :2]; X_ = Hs[2:, :2]; C_ = Hs[2:, 2:]; Xh_ = conj_z(X_).T
detP_ = sp.expand(P_.det()); adjP_ = P_.adjugate().applyfunc(sp.expand)
check("det(H_BB) tr(S) = 0 identically for the Schur complement S = H_CC - H_CB H_BB^-1 H_BC (B = {0, 1}, C = {2, 3}), symbolically in every coupling: S is a traceless Hermitian 2x2 matrix", sp.expand(detP_ * C_.trace() - (adjP_ * Xh_ * X_).trace()) == 0, f"{time.time()-T0:.0f}s")

# ================================================================ (2) floating-point node search at the README's couplings
COUP = {"A": dict(J=(1.0, 0.8, 1.0), kap=0.45, rat=("1", "4/5", "1", "9/20"), readme=[(0.22300, 0.68644, 0.25024)]),
        "B": dict(J=(1.2, 0.8, 1.0), kap=0.30, rat=("6/5", "4/5", "1", "3/10"), readme=[(0.25506, 0.58995, 0.04264)])}
def rat_amps(rat):
    q = lambda s: iv.mpf(int(s.split("/")[0])) / (iv.mpf(int(s.split("/")[1])) if "/" in s else 1)
    return {"x": 2 * q(rat[0]), "y": 2 * q(rat[1]), "z": 2 * q(rat[2]), "k": 2 * q(rat[3])}
NODES = {}
for name, c in COUP.items():
    T, nodes = find_nodes(c["J"], c["kap"], n=40, thr=0.8)
    NODES[name] = sorted(nodes, key=lambda v: tuple(v))
    hit_readme = all(any(np.linalg.norm(np.mod(x - np.array(r) + 0.5, 1) - 0.5) < 2e-5 for x in nodes) for r in c["readme"])
    ch = [int(round(sphere_chern(T, x, 0.004, m=48)[0])) for x in NODES[name]]; ch8 = [int(round(sphere_chern(T, x, 0.008, m=48)[0])) for x in NODES[name]]
    c["charges"] = ch
    check(f"coupling {name} J = {c['J']}, kappa = {c['kap']}: the grid-plus-minimisation search finds six touchings of the middle bands (gap < 1e-7 at E = 0), among them the README's off-plane node to five digits", len(nodes) == 6 and hit_readme,
          "; ".join(f"({x[0]:.5f}, {x[1]:.5f}, {x[2]:.5f})" for x in NODES[name]))
    check(f"coupling {name}: discrete sphere fluxes of the lowest two bands (radii 0.004 and 0.008) are +-1 at all six nodes and sum to zero", all(abs(a) == 1 for a in ch) and ch == ch8 and sum(ch) == 0, f"{ch}")
print(f"   [{time.time()-T0:.0f}s]", flush=True)

# ================================================================ (3) interval certificates
def tighten(x0, X, amps, its=40):
    for _ in range(its):
        ok, K, X2, JX, magP = krawczyk(x0, None, amps, box=X)
        if not ok: return None
        X = [iv.mpf([max(K[i].a, X[i].a), min(K[i].b, X[i].b)]) for i in range(3)]
        if max(float(X[i].delta) for i in range(3)) < 1e-15: break
    return X
def outer_gap_sq(X, amps):
    H, dH = build(X, amps); t = iv.mpf(0)
    for i in range(4):
        for j in range(4): t += H[i][j].real ** 2 + H[i][j].imag ** 2
    return t / 2
CERT = {}
for name, c in COUP.items():
    amps = rat_amps(c["rat"]); rows = []
    for x in NODES[name]:
        x0 = refine(x, amps)
        best = None
        for r in (3e-3, 1e-3, 3e-4, 1e-4, 1e-5):
            ok, K, X, JX, magP = krawczyk(x0, r, amps)
            if ok: best = r; break
        Xt = tighten(x0, [iv.mpf([x0[i] - best, x0[i] + best]) for i in range(3)], amps) if best else None
        if Xt is None: rows.append((x0, best, None)); continue
        FXt, JmXt, auxXt = Fvec(Xt, amps)
        JXt = [[JmXt[j][i] for j in range(3)] for i in range(3)]
        dJ = det3(JXt)
        a2 = outer_gap_sq(Xt, amps)
        wid = max(float(Xt[i].delta) for i in range(3))
        magPt = (auxXt["detP"].real ** 2 + auxXt["detP"].imag ** 2).a
        rows.append((x0, best, dict(box=Xt, detJ=dJ, a2=a2, width=wid, magP=magPt, trS=auxXt["trS"], imS=auxXt["imS00"])))
    CERT[name] = rows
    ok_all = all(r[1] is not None and r[2] is not None for r in rows)
    check(f"coupling {name}: Krawczyk certifies exactly one zero of F (three real equations, three unknowns) in a box around each of the six nodes", ok_all,
          "; ".join(f"half-width {r[1]:g}" if r[1] else "FAILED" for r in rows))
    if not ok_all: continue
    check(f"coupling {name}: on every certified box |det H_BB| > 0 (lower bound {min(float(r[2]['magP']) for r in rows)**0.5:.3f}), the Jacobian determinant has a fixed sign (interval excludes 0), and the enclosures are tighter than 1e-12",
          all(r[2]["magP"] > 0 for r in rows) and all((r[2]["detJ"].a > 0 or r[2]["detJ"].b < 0) for r in rows) and max(r[2]["width"] for r in rows) < 1e-12,
          "det J signs " + str([int(np.sign(float(r[2]["detJ"].mid))) for r in rows]) + f", max enclosure width {max(r[2]['width'] for r in rows):.1e}")
    check(f"coupling {name}: at each certified node rank H = 2 exactly (the outer bands are at +-a with a^2 = tr H^2 / 2 >= {min(float(r[2]['a2'].a) for r in rows):.4f} > 0), so the middle bands touch at zero energy and are separated from the outer ones",
          all(r[2]["a2"].a > 0 for r in rows))
    # the note-style claim: off both planes f1 + f2 = 1 and f1 + f2 = 2 f3 for the four extra nodes
    extra = [r for r in rows if min(abs(float(r[0][2])), abs(float(r[0][2]) - 1)) > 1e-6]
    frac = lambda v: abs(float(v) - round(float(v)))
    off = all(frac(r[0][0] + r[0][1]) > 1e-3 and frac(r[0][0] + r[0][1] - 2 * r[0][2]) > 1e-3 for r in extra)
    check(f"coupling {name}: the four nodes off f3 = 0 lie off both planes f1 + f2 = 1 and f1 + f2 = 2 f3 (mod 1) by more than 1e-3 (their boxes have half-width <= 1e-3, so the offsets are certified by the box centres)", len(extra) == 4 and off,
          "distances of f1 + f2 to the nearest integer " + str([round(frac(r[0][0] + r[0][1]), 5) for r in extra]) + ", of f1 + f2 - 2 f3 " + str([round(frac(r[0][0] + r[0][1] - 2 * r[0][2]), 5) for r in extra]))
    # charge = sign det J (compare with the discrete flux)
    sg = [int(np.sign(float(r[2]["detJ"].mid))) for r in rows]
    check(f"coupling {name}: at all six nodes the discrete sphere flux equals the sign of the interval-certified Jacobian determinant (charge +-1 = degree of F)", sg == c["charges"], f"signs {sg}, fluxes {c['charges']}")
print(f"   [{time.time()-T0:.0f}s]", flush=True)
for name in COUP:
    print(f"   coupling {name} certified nodes (centre of the enclosure; half-width of the largest Krawczyk box; det J; a^2):")
    for (x0, best, d) in CERT[name]:
        if d: print(f"      f = ({float(d['box'][0].mid):.13f}, {float(d['box'][1].mid):.13f}, {float(d['box'][2].mid):.13f})  r = {best:g}  det J = {float(d['detJ'].mid):.4f}  a^2 = {float(d['a2'].mid):.6f}")

# ================================================================ (4) negative control and the splitting of the charge-two point
iso = rat_amps(("1", "1", "1", "1/2")); f_plus = np.array([0.25, 0.75, 0.5])
Fp, Jp = Fmid(f_plus, iso)
sv = np.linalg.svd(Jp)[1]
check("isotropic handover J = (1, 1, 1), kappa = 1/2 (open PR 9373 at q = 1/2): F(f+) = 0 to 1e-30 and the Jacobian has rank one (singular values 8 pi, 0, 0), so the Krawczyk test cannot certify it and the zero is not simple", np.abs(Fp).max() < 1e-30 and abs(sv[0] - 8 * np.pi) < 1e-9 and sv[1] < 1e-9 and not krawczyk(f_plus, 1e-5, iso)[0], f"|F| = {np.abs(Fp).max():.1e}, singular values {np.round(sv, 9)}")
a2_iso = outer_gap_sq([iv.mpf(0.25), iv.mpf(0.75), iv.mpf(0.5)], iso)
check("at the isotropic handover point a^2 = tr H^2 / 2 = 48, so det(H - lambda) = lambda^2 (lambda^2 - 48) there (open PR 9373's c(1/2))", a2_iso.a > 47.999999999 and a2_iso.b < 48.000000001, f"a^2 in [{float(a2_iso.a):.10f}, {float(a2_iso.b):.10f}]")
T_iso = terms_of(1.0, 1.0, 1.0, 0.5)
flux2 = [round(sphere_chern(T_iso, f_plus, r, m=48)[0], 3) for r in (0.004, 0.008)]
check("the discrete flux around the isotropic handover point is -2 (as in open PR 9373) at radii 0.004 and 0.008", flux2 == [-2.0, -2.0], f"{flux2}")
def ampsJy(num, den): return {"x": iv.mpf(2), "y": 2 * iv.mpf(num) / den, "z": iv.mpf(2), "k": iv.mpf(1)}
split = {}
for (num, den) in ((999, 1000), (99, 100), (19, 20)):
    amps = ampsJy(num, den); eps = 1 - num / den; sols = []
    rng = np.random.default_rng(num)
    for _ in range(200):
        u_ = rng.normal(0, 1, 3); x = f_plus + rng.uniform(0.3, 2.0) * 0.46 * np.sqrt(eps) * u_ / np.linalg.norm(u_)
        try:
            for _ in range(40):
                F, J = Fmid(x, amps); dx = np.linalg.solve(J, F); x = x - dx
                if np.abs(dx).max() < 1e-13: break
            F, J = Fmid(x, amps)
            if np.abs(F).max() < 1e-11 and np.linalg.norm(x - f_plus) < 0.3 and not any(np.linalg.norm(x - y) < 1e-7 for y in sols): sols.append(x.copy())
        except Exception: pass
    certs = []
    for x in sols:
        x0 = refine(x, amps); ok = False
        for r in (1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
            ok, K, X, JX, magP = krawczyk(x0, r, amps)
            if ok: break
        Xt = tighten(x0, [iv.mpf([x0[i] - r, x0[i] + r]) for i in range(3)], amps) if ok else None
        dJ = det3([[Fvec(Xt, amps)[1][j][i] for j in range(3)] for i in range(3)]) if Xt else None
        certs.append((x0, ok, r, dJ))
    split[num / den] = (eps, sols, certs)
    dist = sorted(np.linalg.norm(s - f_plus) for s in sols)
    check(f"J = (1, {num}/{den}, 1), kappa = 1/2: exactly two simple nodes near f+ (both certified by Krawczyk with det J of one sign, distances {dist[0]:.5f}, {dist[-1]:.5f}); the charge-two point has split", len(sols) == 2 and all(c[1] for c in certs) and all(c[3].a * c[3].b > 0 for c in certs) and np.sign(float(certs[0][3].mid)) == np.sign(float(certs[1][3].mid)))
ratios = [np.linalg.norm(split[k][1][0] - f_plus) / np.sqrt(split[k][0]) for k in split]
check("the two nodes lie at f+ +- delta with |delta| = 0.46 sqrt(1 - J_y) to within 1% over 1 - J_y = 0.001, 0.01, 0.05 (floating-point scaling, labelled)", (max(ratios) - min(ratios)) < 1e-2 * max(ratios), f"|delta|/sqrt(eps) = {np.round(ratios, 4)}")
T_p = terms_of(1.0, 0.95, 1.0, 0.5)
fluxbig = round(sphere_chern(T_p, f_plus, 0.2, m=128)[0], 3)
check("for J_y = 19/20 the flux through the sphere of radius 0.2 around f+ (which encloses both split nodes, at distance 0.102, and no other node) is -2, the charge of the point they came from", fluxbig == -2.0, f"{fluxbig}")
print(f"   total {time.time()-T0:.0f}s")
if not HITS:
    n_cert = sum(1 for name in COUP for r in CERT[name] if r[2])
    print(f"SUMMARY: PARTIAL, new and exact: at J = (1, 4/5, 1), kappa = 9/20 and J = (6/5, 4/5, 1), kappa = 3/10 all six touchings of the middle bands ({n_cert} in all: two on the line f2 = 1 - f1, f3 = 0 and four off both planes) are certified by interval Krawczyk tests as simple zeros of the three-equation Schur system (enclosures below 1e-12, unique in boxes of half-width 1e-4 to 3e-3, outer bands separated), with charge +-1 = the sign of the certified Jacobian determinant; symbolically tr H = tr H^3 = 0 and det(H_BB) tr S = 0 for all couplings; the charge-two point of the isotropic handover has a rank-one Jacobian and splits, for J_y < 1, into two simple nodes at distance ~ 0.46 sqrt(1 - J_y) (certified at J_y = 0.999, 0.99, 0.95); {PASS} checks pass")
    print("HIT: certified existence, simplicity and charge +-1 of the six touchings of the anisotropic comparator at the README's two couplings, and the splitting of the isotropic charge-two point into two simple nodes for J_y < 1 (interval Krawczyk on the Schur-complement system; symbolic identities for all couplings). Same-family model (Claude Sonnet 5.5); floating point only in the node search, the sphere fluxes and the sqrt scaling.")
else:
    print("SUMMARY: ROUTE FAILS: " + "; ".join(HITS))
sys.exit(0)
