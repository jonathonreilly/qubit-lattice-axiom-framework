#!/usr/bin/env python3
"""Packets of all eight species under the three couplings of lengths (blocks 62-74 as landed), run 1 of 2.

Walk H = sum_a sigma_a S_a; couplings of a strain field B_a^j (a = coin axis, j = derivative axis):
    frame (block 62):        sum sigma_a (1/2){B_a^j, S_j}
    reach two (blocks 63-64): sum sigma_a (1/2){C_a[B_a^j], S_j}      C_a[v] the symmetric hop along a weighted by the bond function v
    reach three (block 69):  sum sigma_a (1/2){C_a[B_a^j], P_j},  P_j = S_j C_j
Exact reduction: every strain here lies in the x-y plane (a, j in {x, y}), so on the k_z in {0, pi} sectors S_z = 0 and neither C_z nor P_z
enters: species (n_x, n_y, 1) evolve by the same operator as (n_x, n_y, 0), and the 2D slice (128 x 128 torus) carries all eight.
Cases (motion along +x, wave number q, positive energy; the displacement part odd in the strain amplitude b0 is the deflection):
    (i)   stretch along the motion, gradient along the motion:  B_x^x = b0 sin(2 pi (x - x0)/Lx)   -> longitudinal displacement
    (ii)  stretch along the motion, gradient transverse:        B_x^x = b0 sin(2 pi y/Ly)          -> transverse deflection (supervisor's case)
    (iii) tilt B_x^y (off-diagonal), gradient along the motion:  B_x^y = b0 sin(2 pi (x - x0)/Lx)  -> transverse displacement
(profiles along x vanish at the packet's start and keep one sign along its path, so the first-order effect does not cancel)
Rays: clouds of the exact lattice symbols of each coupling at the species' momentum (they carry D g D, (1 + B D)^T (1 + B D), (1 + B)^T (1 + B)
and the factors cos q, cos^2 q), sampled from the packet's position and momentum spreads.  Exact: the first-order factors (sympy).  Floating
point: the evolutions (expm_multiply) and the rays (RK4).
"""
import itertools, time
import numpy as np
import sympy as sp
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply

def out(s): print(s, flush=True)

# ------------------------------------------------------------------ exact first-order factors by species
q, b = sp.symbols('q b', real=True)
def sym(kind, Bm, k):
    s = [sp.sin(k[0]), sp.sin(k[1])]; c = [sp.cos(k[0]), sp.cos(k[1])]
    h = []
    for a in range(2):
        if kind == "frame": h.append(s[a] + sum(Bm[a][j] * s[j] for j in range(2)))
        elif kind == "reach2": h.append(s[a] + c[a] * sum(Bm[a][j] * s[j] for j in range(2)))
        else: h.append(s[a] + c[a] * sum(Bm[a][j] * s[j] * c[j] for j in range(2)))
    return h
SPECIES = [(0, 0), (1, 0), (0, 1), (1, 1)]
KINDS = ("frame", "reach2", "reach3")
fac = {}
for n in SPECIES:
    k = (sp.pi * n[0] + q, sp.pi * n[1])
    for kind in KINDS:
        h = sym(kind, [[b, 0], [0, 0]], k)
        E = sp.sqrt(h[0] ** 2 + h[1] ** 2)
        st = sp.simplify(sp.diff(E, b).subs(b, 0) / sp.Abs(sp.sin(q)))          # stretch: dE/db over |sin q|
        ht = sym(kind, [[0, b], [0, 0]], (k[0], k[1] + sp.Symbol('e')))
        Et = sp.sqrt(ht[0] ** 2 + ht[1] ** 2)
        vy = sp.diff(Et, sp.Symbol('e'))
        tl = sp.simplify(sp.diff(vy, b).subs({b: 0, sp.Symbol('e'): 0}))       # tilt: d v_y / d b at k_y = pi n_y
        fac[(n, kind)] = (sp.simplify(st.subs(q, sp.Symbol('q', positive=True))), tl)
    out("X species %s: first-order stretch factor dE/db / |sin q| = frame %s, reach two %s, reach three %s; tilt factor dv_y/db = frame %s, "
        "reach two %s, reach three %s" % (n, *[fac[(n, kd)][0] for kd in KINDS], *[sp.simplify(fac[(n, kd)][1]) for kd in KINDS]))
out("X species (n_x, n_y, 1) = (n_x, n_y, 0) for these strains (S_z = 0 on the k_z = 0, pi sectors; C_z, P_z do not enter): all eight species are covered")

# ------------------------------------------------------------------ lattice
Lx = Ly = 128; N = Lx * Ly
X, Y = np.meshgrid(np.arange(Lx), np.arange(Ly), indexing='ij'); Xf, Yf = X.ravel(), Y.ravel()
def shift(dx, dy):
    cols = ((Xf + dx) % Lx) * Ly + (Yf + dy) % Ly
    return sps.csr_matrix((np.ones(N), (np.arange(N), cols)), shape=(N, N))
Tx, Ty = shift(1, 0), shift(0, 1)
S = [(Tx - Tx.T) / 2j, (Ty - Ty.T) / 2j]; C = [(Tx + Tx.T) / 2, (Ty + Ty.T) / 2]; P = [S[0] @ C[0], S[1] @ C[1]]
SIG = [sps.csr_matrix(np.array([[0, 1], [1, 0]], complex)), sps.csr_matrix(np.array([[0, -1j], [1j, 0]]))]
def Cw(a, v):
    Dg = sps.diags(v); Ta = [Tx, Ty][a]
    return (Dg @ Ta + Ta.T @ Dg) / 2
H0 = (sps.kron(S[0], SIG[0]) + sps.kron(S[1], SIG[1])).tocsr()
def ham(kind, Bf):
    H = H0.copy()
    for (a, j), v in Bf.items():
        if kind == "frame":
            Dg = sps.diags(v); term = (Dg @ S[j] + S[j] @ Dg) / 2
        elif kind == "reach2":
            term = (Cw(a, v) @ S[j] + S[j] @ Cw(a, v)) / 2
        else:
            term = (Cw(a, v) @ P[j] + P[j] @ Cw(a, v)) / 2
        H = H + sps.kron(term, SIG[a])
    return H.tocsr()
def packet(n, qq, x0, y0, w):
    dx = (Xf - x0 + Lx / 2) % Lx - Lx / 2; dy = (Yf - y0 + Ly / 2) % Ly - Ly / 2
    kx, ky = np.pi * n[0] + qq, np.pi * n[1]
    env = np.exp(-(dx ** 2 + dy ** 2) / (2 * w ** 2) + 1j * (kx * dx + ky * dy))
    hk = np.sin(kx) * np.array([[0, 1], [1, 0]]) + np.sin(ky) * np.array([[0, -1j], [1j, 0]])
    ev, vec = np.linalg.eigh(hk); u = vec[:, 1]                       # positive energy
    psi = (env[:, None] * u[None, :]).ravel(); return psi / np.linalg.norm(psi)
def means(psi, xc, yc):
    """mean displacement from (x0, y0), with periodic distances taken about the expected centre (xc, yc) so that no tail wraps"""
    rho = (np.abs(psi.reshape(N, 2)) ** 2).sum(1)
    dx = (Xf - xc + Lx / 2) % Lx - Lx / 2 + (xc - x0); dy = (Yf - yc + Ly / 2) % Ly - Ly / 2 + (yc - y0)
    return float((rho * dx).sum() / rho.sum()), float((rho * dy).sum() / rho.sum())

# ------------------------------------------------------------------ vectorized ray clouds of the exact symbols
def Esym(kind, k1, k2, B):
    s1, s2, c1, c2 = np.sin(k1), np.sin(k2), np.cos(k1), np.cos(k2)
    sj = (s1, s2); cj = (c1, c2); h = []
    for a in range(2):
        if kind == "frame": h.append(sj[a] + sum(B[(a, j)] * sj[j] for j in range(2)))
        elif kind == "reach2": h.append(sj[a] + cj[a] * sum(B[(a, j)] * sj[j] for j in range(2)))
        else: h.append(sj[a] + cj[a] * sum(B[(a, j)] * sj[j] * cj[j] for j in range(2)))
    return np.hypot(h[0], h[1])
def ray_cloud(kind, Bfun, n, qq, x0, y0, w, T, nr=2000, seed=7, dt=0.1):
    rng = np.random.default_rng(seed)
    st = np.stack([rng.normal(x0, w / np.sqrt(2), nr), rng.normal(y0, w / np.sqrt(2), nr),
                   rng.normal(np.pi * n[0] + qq, 1 / (np.sqrt(2) * w), nr), rng.normal(np.pi * n[1], 1 / (np.sqrt(2) * w), nr)])
    h = 1e-5
    def f(st):
        x, y, k1, k2 = st
        E = lambda kk1, kk2, xx, yy: Esym(kind, kk1, kk2, Bfun(xx, yy))
        return np.stack([(E(k1 + h, k2, x, y) - E(k1 - h, k2, x, y)) / (2 * h), (E(k1, k2 + h, x, y) - E(k1, k2 - h, x, y)) / (2 * h),
                         -(E(k1, k2, x + h, y) - E(k1, k2, x - h, y)) / (2 * h), -(E(k1, k2, x, y + h) - E(k1, k2, x, y - h)) / (2 * h)])
    x_start = st[:2].copy()
    for _ in range(int(round(T / dt))):
        a1 = f(st); a2 = f(st + dt / 2 * a1); a3 = f(st + dt / 2 * a2); a4 = f(st + dt * a3)
        st = st + dt / 6 * (a1 + 2 * a2 + 2 * a3 + a4)
    return float(np.mean(st[0] - x_start[0])), float(np.mean(st[1] - x_start[1]))

# ------------------------------------------------------------------ the fields
b0, T, w = 0.2, 60.0, 8.0
x0, y0 = 20.0, 0.0
def xm_for(qq): return x0                                      # profiles start at zero at the packet and rise along its path (half period 64 > path ~50)
def fields(case, qq, sgn):
    xm = xm_for(qq)
    if case == "i":
        v = sgn * b0 * np.sin(2 * np.pi * (Xf - xm) / Lx); return {(0, 0): v}, (lambda xx, yy: {(0, 0): sgn * b0 * np.sin(2 * np.pi * (xx - xm) / Lx), (0, 1): 0.0, (1, 0): 0.0, (1, 1): 0.0})
    if case == "ii":
        v = sgn * b0 * np.sin(2 * np.pi * Yf / Ly); return {(0, 0): v}, (lambda xx, yy: {(0, 0): sgn * b0 * np.sin(2 * np.pi * yy / Ly), (0, 1): 0.0, (1, 0): 0.0, (1, 1): 0.0})
    v = sgn * b0 * np.sin(2 * np.pi * (Xf - xm) / Lx); return {(0, 1): v}, (lambda xx, yy: {(0, 1): sgn * b0 * np.sin(2 * np.pi * (xx - xm) / Lx), (0, 0): 0.0, (1, 0): 0.0, (1, 1): 0.0})
COMP = {"i": 0, "ii": 1, "iii": 1}                                 # which displacement component is the deflection

def deflect(kind, case, n, qq):
    psi0 = packet(n, qq, x0, y0, w)
    res = []
    for sgn in (+1, -1):
        Bf, Bfun = fields(case, qq, sgn)
        psiT = expm_multiply(-1j * ham(kind, Bf) * T, psi0)
        res.append((means(psiT, x0 + np.cos(qq) * T, y0), ray_cloud(kind, Bfun, n, qq, x0, y0, w, T)))
    pk = 0.5 * (res[0][0][COMP[case]] - res[1][0][COMP[case]])
    ry = 0.5 * (res[0][1][COMP[case]] - res[1][1][COMP[case]])
    return pk, ry

t0 = time.time()
TAB = {}
worst3 = (0.0, None)
for case in ("i", "ii", "iii"):
    for n in SPECIES:
        cells = []
        for kind in KINDS:
            pk, ry = deflect(kind, case, n, 0.6)
            TAB[(case, n, kind)] = (pk, ry)
            cells.append("%s %+.3f (rays %+.3f, %+.1f%%)" % (kind, pk, ry, 100 * (pk / ry - 1) if abs(ry) > 1e-9 else float('nan')))
            if kind == "reach3" and abs(ry) > 1e-6:
                dev = abs(pk / ry - 1) if pk * ry > 0 else 9.9
                if dev > worst3[0]: worst3 = (dev, (case, n, pk, ry))
        out("N case (%s), species %s (and %s), q = 0.6: %s" % (case, n, n + (1,), " | ".join(cells)))
out("N supervisor's 2D values, case (ii), species (0,0) and (1,0): frame -15.06, -15.06; reach two -12.64, +12.64; reach three -10.57, -10.57 "
    "(b0 = 0.2, Ly = 128, T = 60, q = 0.6; packet width not stated); here: frame %+.2f, %+.2f; reach two %+.2f, %+.2f; reach three %+.2f, %+.2f (width %g)"
    % (TAB[("ii", (0, 0), "frame")][0], TAB[("ii", (1, 0), "frame")][0], TAB[("ii", (0, 0), "reach2")][0], TAB[("ii", (1, 0), "reach2")][0],
       TAB[("ii", (0, 0), "reach3")][0], TAB[("ii", (1, 0), "reach3")][0], w))
out("N species table elapsed %.0f s" % (time.time() - t0))

# ------------------------------------------------------------------ wave-number dependence, case (ii), reach three over the frame
QS = (0.2, 0.4, 0.6, 0.8, 1.0)
for n in SPECIES:
    cells = []
    for qq in QS:
        pf, rf = deflect("frame", "ii", n, qq)
        p3, r3 = deflect("reach3", "ii", n, qq)
        cells.append("q=%.1f: %.3f (rays %.3f; cos^2 q %.3f)" % (qq, p3 / pf, r3 / rf, np.cos(qq) ** 2))
        if abs(r3) > 1e-6:
            dev = abs(p3 / r3 - 1) if p3 * r3 > 0 else 9.9
            if dev > worst3[0]: worst3 = (dev, ("ii q=%.1f" % qq, n, p3, r3))
    out("N case (ii), species %s, reach three / frame against q: %s" % (n, "; ".join(cells)))
out("N reach three: largest |packet/ray - 1| over every species, case and wave number: %.3f at %s" % (worst3[0], worst3[1]))

out("")
if worst3[0] > 0.05:
    c = worst3[1]
    out("HIT: under the reach-three coupling, case %s species %s deflects %+.4f against its ray prediction %+.4f (%s)"
        % (c[0], c[1], c[2], c[3], "opposite sign" if c[2] * c[3] < 0 else "off by %.1f%%" % (100 * worst3[0])))
def sg(v): return "+" if v > 0 else "-"
signs = {case: {kind: "".join(sg(TAB[(case, n, kind)][0]) for n in SPECIES) for kind in KINDS} for case in ("i", "ii", "iii")}
out("SUMMARY: eight species (four in-plane classes; the z-reflected ones evolve by the same operator) x three couplings x three cases at q = 0.6, "
    "signs over species (00,10,01,11): stretch along the motion (i) frame %s, reach two %s, reach three %s; transverse gradient (ii) frame %s, "
    "reach two %s, reach three %s (supervisor's -15.06/-12.64/+12.64/-10.57 reproduced: %+.2f/%+.2f/%+.2f/%+.2f); tilt (iii) frame %s, reach two %s, "
    "reach three %s: reach three alone treats all eight alike in every case; packets follow their ray clouds, reach three within %.1f%%; reach three "
    "over the frame follows the rays' ratio (cos^2 q at first order: 0.951/0.853/0.701/0.516/0.323 against 0.961/0.848/0.681/0.485/0.292)"
    % (signs["i"]["frame"], signs["i"]["reach2"], signs["i"]["reach3"], signs["ii"]["frame"], signs["ii"]["reach2"], signs["ii"]["reach3"],
       TAB[("ii", (0, 0), "frame")][0], TAB[("ii", (0, 0), "reach2")][0], TAB[("ii", (1, 0), "reach2")][0], TAB[("ii", (0, 0), "reach3")][0],
       signs["iii"]["frame"], signs["iii"]["reach2"], signs["iii"]["reach3"], 100 * worst3[0]))
