#!/usr/bin/env python3
"""J:derive:shadow-force-dilute-exact:a3 - checks for ATTEMPT.md (same directory).

Dilute limit of block 44's inertial gas (open PR #8550): independent records, each keeping its content; six-axis records
move along their axis at rate 1, sphere-menu records step to x + e_k at rate p_k(s) = max(0, s.e_k)/sqrt3 (a directed
random walk). Capturing bodies remove a record at its first attempt to enter a body site and take up its content.
Steady state fed by a distant uniform reservoir of density rho. EXACT = Fractions / sympy / integer counting; FLOAT = Gauss
quadrature over contents of exact per-content expressions (errors estimated by node doubling), or extrapolation.
"""
import sys
from fractions import Fraction as Fr
from itertools import product
from math import comb, lgamma

import numpy as np
import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


AX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


# ------------------------------------------------------------------ A: six-axis menu, exact ray (line) counting
def six_force(A, B):
    """force on A in units of j (records per line per tick per direction): each line along each axis carries one stream
    per direction; a stream is absorbed at the first body site it meets."""
    bodies = [(a, 0) for a in A] + [(b, 1) for b in B]
    F = [0, 0, 0]
    for ax in range(3):
        lines = {}
        for site, who in bodies:
            key = tuple(site[i] for i in range(3) if i != ax)
            lines.setdefault(key, []).append((site[ax], who))
        for key, pts in lines.items():
            pts.sort()
            if pts[0][1] == 0:   # stream moving +ax meets A first
                F[ax] += 1
            if pts[-1][1] == 0:  # stream moving -ax meets A first
                F[ax] -= 1
    return tuple(F)


def overlap(A, B, ax):
    pa = {tuple(s[i] for i in range(3) if i != ax) for s in A}
    pb = {tuple(s[i] for i in range(3) if i != ax) for s in B}
    return len(pa & pb)


def box(o, d):
    return [(o[0] + i, o[1] + j, o[2] + k) for i in range(d[0]) for j in range(d[1]) for k in range(d[2])]


shapes = {"site": box((0, 0, 0), (1, 1, 1)), "cube2": box((0, 0, 0), (2, 2, 2)), "slab": box((0, 0, 0), (1, 3, 2)),
          "L": [(0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 0, 1), (1, 0, 0)]}
allok, rows = True, 0
alone = all(six_force(S, []) == (0, 0, 0) for S in shapes.values())
for (na, SA), (nb, SB) in product(shapes.items(), repeat=2):
    for dy, dz in ((0, 0), (1, 0), (1, 1), (2, 1), (5, 0)):
        prev = None
        for sep in (3, 5, 8, 13, 21):
            Bs = [(x + sep, y + dy, z + dz) for x, y, z in SB]
            F = six_force(SA, Bs)
            expect = (overlap(SA, Bs, 0), 0, 0)  # B lies at larger x and is disjoint in x from A
            allok &= F == expect and (prev is None or F == prev)
            prev = F
            rows += 1
# a diagonal placement: overlaps along two axes at once
Fd = six_force(shapes["cube2"], box((5, 1, 0), (2, 2, 2)))
Fd2 = six_force(shapes["cube2"], box((1, 5, 0), (2, 2, 2)))
ok("A1", alone and allok and Fd == (2, 0, 0) and Fd2 == (0, 2, 0),
   f"six axes, {rows} placements (4 shapes x 4 shapes x 5 transverse offsets x 5 separations 3..21): a body alone feels "
   "0; with B, F_A = j x (number of axis lines through both A and B) towards B along that axis, the same at every "
   "separation: beams, no inverse-square law; no overlap, no force")

# ------------------------------------------------------------------ B: sphere menu, per content (EXACT)
q = sp.symbols("q0:3", nonnegative=True)


def walk_visit(n, qv):
    """exact visit probability of the site n (oriented, n >= 0) for the directed walk from 0 with step probabilities qv,
    by dynamic programming over levels."""
    N = sum(n)
    prob = {(0, 0, 0): Fr(1)}
    for _ in range(N):
        nxt = {}
        for site, p in prob.items():
            for k in range(3):
                t = list(site); t[k] += 1; t = tuple(t)
                if all(t[i] <= n[i] for i in range(3)):
                    nxt[t] = nxt.get(t, Fr(0)) + p * qv[k]
        prob = nxt
    return prob.get(tuple(n), Fr(0))


qv = (Fr(1, 2), Fr(1, 3), Fr(1, 6))
b2 = all(walk_visit(n, qv) == Fr(comb(sum(n), n[0]) * comb(n[1] + n[2], n[1])) * qv[0] ** n[0] * qv[1] ** n[1] * qv[2] ** n[2]
         for n in [(3, 0, 0), (2, 1, 0), (1, 1, 1), (4, 2, 1), (0, 3, 2)])
u_, v_ = sp.symbols("u v", positive=True)


def dirichlet(n):
    N = sum(n)
    coef = sp.factorial(N) / (sp.factorial(n[0]) * sp.factorial(n[1]) * sp.factorial(n[2]))
    qx, qy, qz = u_, (1 - u_) * v_, (1 - u_) * (1 - v_)
    return sp.integrate(sp.integrate(coef * qx ** n[0] * qy ** n[1] * qz ** n[2] * (1 - u_), (v_, 0, 1)), (u_, 0, 1))


b3 = all(dirichlet(n) == sp.Rational(1, (sum(n) + 1) * (sum(n) + 2)) for n in [(3, 0, 0), (2, 1, 0), (1, 1, 1), (2, 2, 1)])
ok("B1", b2 and b3,
   "sphere menu, per content s: a record steps along e_k at rate |s_k|/sqrt3 in the directions of s's signs, so it "
   "visits the oriented site n with the multinomial probability N!/(n_x! n_y! n_z!) q^n, q = |s|/|s|_1, N = |n|_1 "
   "(exact DP over levels, rational q); over each octant's simplex it integrates to 1/((N+1)(N+2)) (sympy), and "
   "d^2q = dOmega/|s|_1^3; a site is entered at rate rho |s|_1/sqrt3 per dOmega/4pi: per site the arrivals are not "
   "isotropic (|s|_1 = projected area of the unit cube), per unit projected area they are")

SQ3 = np.sqrt(3.0)
J = 1 / (4 * SQ3)  # one-sided flux through a face per unit density: j = rho/(4 sqrt3)


def duffy(nq):
    x, w = np.polynomial.legendre.leggauss(nq)
    u = (x + 1) / 2; wu = w / 2
    U, V = np.meshgrid(u, u, indexing="ij"); WU, WV = np.meshgrid(wu, wu, indexing="ij")
    Q = np.array([U.ravel(), ((1 - U) * V).ravel(), ((1 - U) * (1 - V)).ravel()])
    return Q, (WU * WV * (1 - U)).ravel()


def single_force(n, nq=400, emit=False):
    """B at n relative to A (single sites): force on A (per unit rho), or for emit=True the rate at which records emitted
    isotropically by B (unit rate) are captured by A, with their momentum."""
    m = -np.array(n)  # displacement from B to A
    perm = np.argsort(-np.abs(m))  # largest component first: its corner is the Duffy collapse point
    Q, W = duffy(nq)
    q2 = np.sqrt((Q ** 2).sum(0))
    tot = np.zeros(3)
    for sig in product((1, -1), repeat=3):
        sig = np.array(sig)
        mo = sig * m[perm]
        if (mo < 0).any():
            continue
        N = int(mo.sum())
        logc = lgamma(N + 1) - sum(lgamma(int(v) + 1) for v in mo)
        with np.errstate(divide="ignore"):
            lm = logc + sum(int(mo[k]) * np.log(np.maximum(Q[k], 1e-300)) for k in range(3))
        mult = np.exp(lm)
        dOm = W / q2 ** 3
        s = np.zeros_like(Q)
        s[perm] = sig[:, None] * Q / q2
        if emit:
            wgt = mult * dOm / (4 * np.pi)
        else:
            wgt = mult * dOm * (1 / (q2 * SQ3)) / (4 * np.pi)  # rho_s x entry rate at B x visit probability
        tot += (s * wgt).sum(1)
    return tot if emit else -tot


def ratio(n0, mult_, nq=400):
    n = tuple(mult_ * np.array(n0))
    F = single_force(n, nq)
    r = np.linalg.norm(n); rh = np.array(n) / r
    return F @ rh * r ** 2 / (J / np.pi), np.linalg.norm(F - (F @ rh) * rh) * r ** 2


dirs = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (3, 2, 1)]
lines, good = [], True
for d in dirs:
    dv = np.array(d, float); z = int((dv == 0).sum()); l1 = np.abs(dv).sum() / np.linalg.norm(dv)
    target = 2 ** z * l1 ** 2
    ms = (32, 64, 128) if d != (3, 2, 1) else (16, 32, 64)
    vals = [ratio(d, m)[0] for m in ms]
    rich = 2 * vals[2] - vals[1]  # Richardson in 1/m
    ctrl = ratio(d, ms[1], nq=600)[0]
    perp = ratio(d, ms[1])[1]
    lines.append(f"{d}: {vals[0]:.3f}, {vals[1]:.3f}, {vals[2]:.3f} -> {rich:.3f} (2^z |r|_1^2 = {target:.3f})")
    good &= abs(rich - target) < 0.02 * target and abs(ctrl - vals[1]) < 1e-6 * target
ok("B2", good, "FLOAT (Gauss over contents of the exact multinomial, node doubling agrees to 1e-6): single-site bodies, "
   "r^2 F/(j/pi) along " + "; ".join(lines) + ": F = (j/pi) 2^z(r) |r_hat|_1^2 / r^2 towards B, z = number of zero "
   "components of r (the peak is shared by 2^z octants: channelling along lattice planes and axes)")


# ------------------------------------------------------------------ B3: extended bodies by exact per-content densities
def dp_force(A, B, nq=160, emitB=False):
    """exact steady-state density of the directed walk for each content node (B absorbing vs transparent), Gauss over
    contents; returns the force on A per unit rho (or, emitB, the capture momentum of B's emission, unit rate per site
    of B... not used)."""
    Q, W = duffy(nq)
    q2 = np.sqrt((Q ** 2).sum(0))
    F = np.zeros(3)
    for sig in product((1, -1), repeat=3):
        sig = np.array(sig)
        Ao = {tuple(sig * np.array(a)) for a in A}
        Bo = {tuple(sig * np.array(b)) for b in B}
        pts = np.array(sorted(Ao | Bo))
        lo = pts.min(0) - 1; hi = pts.max(0)
        shape = tuple(int(v) for v in hi - lo + 1)
        caps = {}
        for mode in (0, 1):
            dens = np.ones(shape + (Q.shape[1],))
            cap = np.zeros(Q.shape[1])
            for idx in np.ndindex(*shape):
                site = tuple(int(v) for v in np.array(idx) + lo)
                inflow = np.zeros(Q.shape[1])
                for k in range(3):
                    up = dens[idx[:k] + (idx[k] - 1,) + idx[k + 1:]] if idx[k] > 0 else 1.0
                    inflow = inflow + Q[k] * up
                if site in Ao:
                    cap += inflow
                    dens[idx] = 0
                elif site in Bo and mode == 1:
                    dens[idx] = 0
                else:
                    dens[idx] = inflow
            caps[mode] = cap
        deficit = caps[0] - caps[1]
        s = sig[:, None] * Q / q2
        wgt = W / q2 ** 3 * (1 / (q2 * SQ3)) / (4 * np.pi) * deficit
        F -= (s * wgt).sum(1)
    return F


cubeA = box((0, 0, 0), (2, 2, 2))
col_pairs = sum(2 ** ((a[1] == b[1]) + (a[2] == b[2])) for a in [(0, y, z) for y in (0, 1) for z in (0, 1)]
                for b in [(0, y, z) for y in (0, 1) for z in (0, 1)])
vals = []
for sep in (48, 96, 192):
    Fc = dp_force(cubeA, box((sep, 0, 0), (2, 2, 2)))
    vals.append(Fc[0] * sep ** 2 / (J / np.pi))  # sep = centre-to-centre distance
rich = 2 * vals[2] - vals[1]
dbl = dp_force(cubeA, box((96, 0, 0), (2, 2, 2)), nq=240)[0] * 96 ** 2 / (J / np.pi)
single_chk = dp_force([(0, 0, 0)], [(16, 0, 0)])[0] * 256 / (J / np.pi)
ok("B3", abs(rich - col_pairs) < 0.01 * col_pairs and abs(single_chk - ratio((1, 0, 0), 16)[0]) < 1e-4
   and abs(dbl - vals[1]) < 1e-8,
   f"FLOAT (exact densities per content, Gauss over contents; 160 and 240 nodes agree to 1e-8): two 2x2x2 cubes on an "
   f"axis, r^2 F/(j/pi) = {vals[0]:.2f}, {vals[1]:.2f}, {vals[2]:.2f} at r = 48, 96, 192 (differences halving: 1/r) -> "
   f"{rich:.2f}; the sum over pairs of facing columns of 2^(number of equal transverse coordinates) is {col_pairs}, "
   "against the smooth A_A A_B = 16; the DP reproduces the single-site multinomial to 1e-4")

# ------------------------------------------------------------------ C: porous bodies (EXACT six axes, FLOAT sphere)
a_lines, T_len = 16, 8  # each body fills a 4x4 cross-section, 8 sites long, with N random sites


def p_line(Nsites):  # probability that a given line holds at least one of N sites placed without repetition
    tot = a_lines * T_len
    return 1 - Fr(comb(tot - T_len, Nsites), comb(tot, Nsites))


# exhaustive check of the expectation on a tiny body: 2 lines x 2 sites each, N sites
tiny_ok = True
for Nn in range(0, 5):
    cells = [(0, y, 0) for y in range(2)] + [(1, y, 0) for y in range(2)]
    from itertools import combinations
    tot, cnt = 0, 0
    for S in combinations(cells, Nn):
        tot += len({(c[1], c[2]) for c in S}); cnt += 1
    exp_lines = Fr(tot, cnt) if cnt else Fr(0)
    tiny_ok &= exp_lines == 2 * (1 - Fr(comb(2, Nn), comb(4, Nn)))
Fexp = {Nn: a_lines * p_line(Nn) ** 2 for Nn in (1, 2, 4, 8, 16, 32, 64, 128)}
additive = all(abs(float(Fexp[Nn]) / (Nn * Nn / a_lines) - 1) < 0.35 for Nn in (1, 2, 4))
sat = abs(float(Fexp[128]) - a_lines) < 1e-12
tau_half = next(Nn for Nn in range(1, 129) if p_line(Nn) >= Fr(1, 2))
ok("C1", tiny_ok and additive and sat and abs(tau_half / a_lines - np.log(2)) < 0.03,
   f"six axes, two porous bodies (N random capturing sites each in a 4x4x8 block, placed apart along x): E[F]/j = a p(N)^2, "
   f"p = 1 - C(aT - T, N)/C(aT, N) exact (checked by enumeration); N = 1, 2, 4: {', '.join(str(Fexp[n]) for n in (1, 2, 4))} "
   f"~ N_A N_B/a (additive); N = 128: {Fexp[128]} = a (the cross-section); a line is blocked with probability 1/2 from "
   f"N = {tau_half} sites, opacity tau = N/a = {tau_half / a_lines:.3f} ~ ln 2 x (1 + O(1/T)): saturation at tau ~ 1")


def cluster_sigma(sites, s, K):
    """capture cross-section (in units of the unit-cube projection |s|_1) of a porous cluster for one content s."""
    sig = np.sign(s); qv = np.abs(s) / np.abs(s).sum()
    So = {tuple(sig * np.array(a)) for a in sites}
    pts = np.array(sorted(So)); lo = pts.min(0) - 1; hi = pts.max(0)
    shape = tuple(int(v) for v in hi - lo + 1)
    dens = np.ones(shape); cap = 0.0
    for idx in np.ndindex(*shape):
        site = tuple(int(v) for v in np.array(idx) + lo)
        inflow = sum(qv[k] * (dens[idx[:k] + (idx[k] - 1,) + idx[k + 1:]] if idx[k] > 0 else 1.0) for k in range(3))
        if site in So:
            cap += inflow; dens[idx] = 0
        else:
            dens[idx] = inflow
    return cap  # capture flux per unit (rho_s x step rate): N for sparse sites, the projection/|s|_1 when opaque


rng = np.random.default_rng(1)
Kc = 6
s_gen = np.array([0.7, 0.5, 0.3]); s_gen /= np.linalg.norm(s_gen)
allc = [(x, y, z) for x in range(Kc) for y in range(Kc) for z in range(Kc)]
proj = cluster_sigma(allc, s_gen, Kc)
sig_rows = []
for Nn in (2, 8, 32, 108, 216):
    vals = [cluster_sigma([allc[i] for i in rng.choice(len(allc), Nn, replace=False)], s_gen, Kc) for _ in range(6)]
    sig_rows.append((Nn, float(np.mean(vals))))
ok("C2", sig_rows[0][1] / 2 > 0.97 and abs(proj - Kc * Kc) < 1e-9 and abs(sig_rows[-1][1] - Kc * Kc) < 1e-9
   and sig_rows[2][1] < 32,
   "FLOAT (exact per content): sphere menu, porous clusters in a 6^3 block, one generic content: capture cross-section "
   "in units of one site's " + ", ".join(f"N={n}: {v:.2f}" for n, v in sig_rows) + f" (block alone {proj:.0f} = K^2): "
   "additive at low opacity, saturating to the block's projection")

# ------------------------------------------------------------------ D: emitting bodies
lines_e, good_e = [], True
for d in dirs[:3]:
    dv = np.array(d, float); z = int((dv == 0).sum()); l1 = np.abs(dv).sum() / np.linalg.norm(dv)
    m1, m2 = 64, 128
    v = []
    for m in (m1, m2):
        n = tuple(m * np.array(d)); r = np.linalg.norm(n)
        P = single_force(n, emit=True)  # captured momentum per unit emission rate (A at origin, B at n)
        v.append(np.linalg.norm(P) * r ** 2 * 4 * np.pi)
    rich_e = 2 * v[1] - v[0]
    lines_e.append(f"{d}: {rich_e:.3f} (2^z |r|_1 = {2 ** z * l1:.3f})")
    good_e &= abs(rich_e - 2 ** z * l1) < 0.02 * 2 ** z * l1
n_ax = (40, 0, 0)
last_x = Fr(n_ax[0], sum(n_ax))
ok("D1", good_e and last_x == 1,
   "FLOAT: a single site emitting Q records per tick isotropically: a capturing site at r takes up momentum "
   "(Q/4pi) 2^z |r_hat|_1 / r^2 away from the emitter (r^2 x 4pi F/Q -> " + "; ".join(lines_e) + "): repulsion with the "
   "same law as the shadow; a reflecting receiver on an axis takes 2 s_x per arrival (the last step is along x with "
   "probability n_x/N = 1, exact), twice the capture")

print(f"SUMMARY: {'PROVED' if not FAILS else 'PARTIAL (failed checks: ' + ', '.join(FAILS) + ')'} in the dilute limit "
      "the six-axis shadow force is j x (lines through both bodies) along the axis, independent of separation; on the "
      "sphere menu each record is a directed walk with multinomial visits, and r^2 F -> (j/pi) 2^z |r_hat|_1^2 for "
      "single sites (C = 2^z/pi with the cube projections as cross-sections; z zero components: channelling; for "
      "extended aligned bodies the facing-column sum, checked, not proved); porous bodies add, then saturate at "
      "opacity ~ 1; emitters repel by the same law")
if not FAILS:
    print("HIT: dilute inertial gas, block 44's clause: six axes, the force of a capturing body B on A is j (records per "
          "line per tick per direction) times the number of axis lines through both, towards B, at every separation; "
          "sphere menu, a record visits the site n with probability N!/prod n_k! prod q_k^n_k, whose integral over each "
          "octant is 1/((N+1)(N+2)), so r^2 F -> (j/pi) 2^z |r_hat|_1^2 for two sites, j = rho/(4 sqrt3), z = number of "
          "zero components of r (x2 on lattice planes, x4 on axes; arrivals isotropic only per unit-cube projection "
          "|s|_1); an isotropic emitter pushes a capturing site with (Q/4pi) 2^z |r_hat|_1/r^2")
