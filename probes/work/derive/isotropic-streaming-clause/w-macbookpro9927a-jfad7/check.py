#!/usr/bin/env python3
"""isotropic-streaming-clause, attempt a3 (worker w-macbookpro9927a-jfad7, claude-opus-5-5).

Forward-only hop rules on the 26 neighbours with a constant speed AND a constant total rate: every unit content s is the
barycentre of its forward neighbours.  Exact rational checks at rational points of the sphere (all 48 cubic images);
the fourth-rank anisotropy is computed by Gauss quadrature on the analytic pieces (float, converged, labelled).
"""
import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
FAILS = []


def check(tag, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + tag + (": " + msg if msg else ""))
    if not ok:
        FAILS.append(tag)


def unit(m, sign):
    v = [0, 0, 0]
    v[m] = sign
    return tuple(v)


def add(*vs):
    return tuple(sum(c) for c in zip(*vs))


def frame(s, order=None):
    ab = [abs(x) for x in s]
    if order is None:
        order = sorted(range(3), key=lambda m: (-ab[m], m))
    i, j, k = order
    u = [unit(m, 1 if s[m] >= 0 else -1) for m in range(3)]
    return ab[i], ab[j], ab[k], u[i], u[j], u[k]


def R1(s, order=None):
    """staircase interpolation: t (a u_i + b u_j + c u_k) + (1 - t)((a-b) u_i + (b-c)(u_i+u_j) + c(u_i+u_j+u_k)),
    t = (1 - a)/(b + c); weights sum to 1, mean step s, at most five forward targets."""
    a, b, c, ui, uj, uk = frame(s, order)
    t = Fr(0) if b + c == 0 else (1 - a) / (b + c)
    return [((1 - t) * (a - b) + t * a, ui), ((1 - t) * (b - c), add(ui, uj)), ((1 - t) * c, add(ui, uj, uk)),
            (t * b, uj), (t * c, uk)]


def R3(s, order=None):
    """axes and face diagonals only: a maximal merge z*, scaled to total weight 1."""
    a, b, c, ui, uj, uk = frame(s, order)
    zs = (b, c, Fr(0)) if a >= b + c else ((a + b - c) / 2, (a - b + c) / 2, (-a + b + c) / 2)
    Z = a + b + c - 1
    th = Fr(0) if sum(zs) == 0 else Z / sum(zs)
    zij, zik, zjk = (th * z for z in zs)
    return [(zij, add(ui, uj)), (zik, add(ui, uk)), (zjk, add(uj, uk)), (a - zij - zik, ui), (b - zij - zjk, uj),
            (c - zik - zjk, uk)]


def agg(W):
    out = {}
    for w, d in W:
        if w != 0:
            out[d] = out.get(d, 0) + w
    return out


def dot(p, q):
    return sum(x * y for x, y in zip(p, q))


def valid(rule, s):
    W = rule(s)
    tot = sum(w for w, _ in W)
    mean = tuple(sum(w * d[m] for w, d in W) for m in range(3))
    return all(w >= 0 for w, _ in W) and tot == 1 and mean == tuple(s) and all(dot(d, s) > 0 for w, d in W if w > 0)


# rational points of the sphere: stereographic images of rational (u, v), and all 48 signed permutations
pts = set()
for p in range(-6, 7):
    for q in range(-6, 7):
        for den in (1, 2, 3, 5, 7):
            u, v = Fr(p, den), Fr(q, den)
            n = 1 + u * u + v * v
            base = (2 * u / n, 2 * v / n, (1 - u * u - v * v) / n)
            for perm in itertools.permutations(range(3)):
                for sg in itertools.product((1, -1), repeat=3):
                    pts.add(tuple(sg[m] * base[perm[m]] for m in range(3)))
pts |= {tuple(sg[m] * b[perm[m]] for m in range(3)) for b in [(Fr(2, 3), Fr(2, 3), Fr(1, 3)), (Fr(6, 7), Fr(3, 7), Fr(2, 7)),
        (Fr(1), Fr(0), Fr(0)), (Fr(3, 5), Fr(4, 5), Fr(0))] for perm in itertools.permutations(range(3))
        for sg in itertools.product((1, -1), repeat=3)}
assert all(dot(s, s) == 1 for s in pts)

okH1 = all(valid(R1, s) for s in pts)
check("H1 forward barycentre", okH1, "on %d rational unit vectors (all 48 cubic images of each): the staircase rule's weights "
      "are >= 0, sum to 1, have mean step exactly s, and sit only on neighbours d with s.d > 0" % len(pts))

# ties and sign flips: the weights do not depend on how ties are broken (continuity across the sector walls)
okH2 = True
nt = 0
for s in pts:
    ab = [abs(x) for x in s]
    orders = {tuple(sorted(range(3), key=lambda m: (-ab[m], perm.index(m)))) for perm in itertools.permutations(range(3))}
    if len(orders) > 1:
        nt += 1
        ref = agg(R1(s, list(next(iter(orders)))))
        okH2 &= all(agg(R1(s, list(o))) == ref for o in orders)
        ref3 = agg(R3(s, list(next(iter(orders)))))
        okH2 &= all(agg(R3(s, list(o))) == ref3 for o in orders)
# near the axis t -> 0: 1 - a = (b^2 + c^2)/(1 + a) <= (b + c)^2, so t <= b + c
okAx = all((lambda a, b, c: b + c == 0 or (1 - a) / (b + c) <= b + c)(*frame(s)[:3]) for s in pts)
check("H2 continuity", okH2 and okAx, "at all %d points with tied magnitudes both rules give the same weights for every tie-break; "
      "at a zero component its target carries weight 0; near an axis t = (1 - a)/(b + c) <= b + c -> 0" % nt)

okH3 = all(valid(R3, s) for s in pts)
check("H3 second rule", okH3, "the axes-and-face-diagonals rule (a maximal merge, scaled to total weight 1) is also a forward "
      "barycentre at every point")

# the capture law: total rate identically 1 (both rules, hence every mixture); speed kappa = 1 for every content
okH4 = all(sum(w for w, _ in R1(s)) == 1 == sum(w for w, _ in R3(s)) for s in pts)
check("H4 isotropic capture", okH4, "r(s) = sum_d a(s,d) = 1 for every content: a capturing site takes content-s records at rate "
      "rho r(s) = rho whatever s (block 48's |s|_1 and a1's 15-33% spreads become 0), and a1's far shadow per unit capture "
      "r(n)/(4 pi <r>) is 1/(4 pi) in every direction")


# inversion: a(-s, d) = a(s, -d) (a1's stationarity with reflecting solids needs it; the rules are cubic-covariant)
okH5 = all(agg(R(tuple(-x for x in s))) == {tuple(-x for x in d): w for d, w in agg(R(s)).items()} for s in pts for R in (R1, R3))
check("H5 inversion", okH5, "a(-s, d) = a(s, -d) for both rules at every point, as a1's stationarity theorem needs with reflecting "
      "solids (a1 proves the uniform product measure stationary for every rate function on any hop set)")

# no pointwise route: on the arcs (a, b, 0), 0 < b < a, no forward rule with total 1 and mean s has M in span{I, s s^T}
NB = [d for d in itertools.product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]
okH6 = True
arcs = [(Fr(p, h), Fr(q, h)) for p, q, h in ((4, 3, 5), (12, 5, 13), (15, 8, 17), (24, 7, 25), (21, 20, 29), (35, 12, 37),
                                            (40, 9, 41), (99, 20, 101))]
for a, b in arcs:
    s = (a, b, Fr(0))
    fwd = {d for d in NB if dot(d, s) > 0}
    okH6 &= fwd == {d for d in NB if d[0] == 1} | {(0, 1, e) for e in (-1, 0, 1)}
    beta = (a + b - 1) / (a * b)                     # forced by M12 = a + b - 1 (weight 1 - a sits on d_1 = 0, all with d_2 = 1)
    need22 = a - beta * (a * a - b * b)              # forced by M11 - M22 = beta (a^2 - b^2), M11 = a
    okH6 &= need22 - b == -(a - b) * (1 - a) * (1 - b) / (a * b) and need22 < b   # but M22 >= sum w d_2 = b
    for R in (R1, R3):
        W = agg(R(s))
        okH6 &= sum(w for d, w in W.items() if d[0] == 1) == a and sum(w * d[0] * d[1] for d, w in W.items()) == a + b - 1
check("H6 no pointwise isotropy", okH6, "on %d rational points of the arcs (a, b, 0), 0 < b < a: the forward set is {d_1 = 1} and "
      "(0, 1, *); any rule with total 1 and mean s has M11 = a, M12 = a + b - 1, M22 >= b, and M = alpha I + beta s s^T would "
      "need M22 - b = -(a-b)(1-a)(1-b)/(ab) < 0 (instances: both rules)" % len(arcs))


# the universal diagonal: targets with d_m in {0, sign(s_m)} and mean s give M_mm = sum w |d_m| = |s_m|, whatever the rule
import sympy as sp
okH7 = all(sum(w * d[m] * d[m] for d, w in agg(R(s)).items()) == abs(s[m]) and all(x * y >= 0 for d in agg(R(s)) for x, y in zip(d, s))
           for s in pts for R in (R1, R3) for m in range(3))
th, ph = sp.symbols("theta phi", real=True)
m3 = sp.integrate(sp.integrate(sp.cos(th) ** 3 * sp.sin(th), (th, 0, sp.pi / 2)) * 2, (ph, 0, 2 * sp.pi)) / (4 * sp.pi)
m21 = sp.integrate(sp.integrate(sp.sin(th) ** 3 * sp.cos(th) * sp.cos(ph) ** 2, (th, 0, sp.pi / 2)) * 2, (ph, 0, 2 * sp.pi)) / (4 * sp.pi)
okH7 &= sp.simplify(m3 - sp.Rational(1, 4)) == 0 and sp.simplify(m21 - sp.Rational(1, 8)) == 0
check("H7 universal diagonal", okH7, "both rules step only to d with d_m in {0, sign(s_m)}, so M_mm(s) = |s_m| exactly at every "
      "point: for EVERY such rule with mean s, T1111 = <|s_1|^3> = %s and T1122 = <s_1^2 |s_2|> = %s (sympy), the axis rule's "
      "values; so T = (1/8) d_ij d_kl + beta (d_ik d_jl + d_il d_jk) + (1/8 - 2 beta) d_ijkl with beta = T1212 = "
      "<|s_1 s_2| W_12>, W_12 the rate of joint steps, and (a)'s isotropy is the one condition beta = 1/16 (axis hops: beta = 0)"
      % (m3, m21))


# ================================================================= N (float): the fourth-rank moment and the isotropic mixture
def M_R1(a, b, c):
    t = (1 - a) / (b + c)
    wx, wp, wv, wy, wz = (1 - t) * (a - b) + t * a, (1 - t) * (b - c), (1 - t) * c, t * b, t * c
    return np.array([[wx + wp + wv, wp + wv, wv], [wp + wv, wp + wv + wy, wv], [wv, wv, wv + wz]])


def M_R3(a, b, c):
    zs = (b, c, 0.0) if a >= b + c else ((a + b - c) / 2, (a - b + c) / 2, (-a + b + c) / 2)
    th = (a + b + c - 1) / sum(zs)
    zij, zik, zjk = (th * z for z in zs)
    xi, yj, zk = a - zij - zik, b - zij - zjk, c - zik - zjk
    return np.array([[zij + zik + xi, zij, zik], [zij, zij + zjk + yj, zjk], [zik, zjk, zik + zjk + zk]])


sector_pts = [s for s in pts if s[0] >= s[1] >= s[2] >= 0 and s[1] + s[2] > 0]
dev = max(abs(float(sum(w * d[m] * d[q] for d, w in agg(R(s)).items())) - Mf(*(float(x) for x in s))[m, q])
          for s in sector_pts for R, Mf in ((R1, M_R1), (R3, M_R3)) for m in range(3) for q in range(3))
check("N0 float = exact", dev < 1e-12, "the float M of both rules equals the exact rules' M at all %d rational sector points "
      "(max deviation %.0e)" % (len(sector_pts), dev))


def T_sector(Mf, n):
    """T1111, T1122, T1212 of a cubic-covariant rule: Gauss-Legendre on the sector a >= b >= c >= 0 in (psi, rho), the rho
    range split at the kink a = b + c of the axes-and-faces rule, so every piece is analytic."""
    xr, wr = np.polynomial.legendre.leggauss(n)
    acc, area = np.zeros(3), 0.0
    for px, pw in zip(xr, wr):
        psi, dpsi = (px + 1) * np.pi / 8, np.pi / 8 * pw
        rmax, rk = 1 / np.sqrt(1 + np.cos(psi) ** 2), 1 / np.sqrt(1 + (np.cos(psi) + np.sin(psi)) ** 2)
        for lo, hi in ((0.0, rk), (rk, rmax)):
            for rx, rw in zip(xr, wr):
                rho, drho = lo + (rx + 1) * (hi - lo) / 2, (hi - lo) / 2 * rw
                b, c = rho * np.cos(psi), rho * np.sin(psi)
                a = np.sqrt(1 - b * b - c * c)
                s, M, dA = (a, b, c), Mf(a, b, c), rho * drho * dpsi / a
                off = [(m, q) for m in range(3) for q in range(3) if m != q]
                acc += dA * np.array([sum(s[m] ** 2 * M[m, m] for m in range(3)) / 3,
                                      sum(s[m] ** 2 * M[q, q] for m, q in off) / 6, sum(s[m] * s[q] * M[m, q] for m, q in off) / 6])
                area += dA
    return acc / area, area


(T1, ar1), (T1b, _) = T_sector(M_R1, 16), T_sector(M_R1, 32)
(T3, ar3), (T3b, _) = T_sector(M_R3, 16), T_sector(M_R3, 32)
A1, A3 = T1b[0] - T1b[1] - 2 * T1b[2], T3b[0] - T3b[1] - 2 * T3b[2]
dN2 = max(np.abs(T1 - T1b).max(), np.abs(T3 - T3b).max())
lam = A1 / (A1 - A3)
Tm = (1 - lam) * T1b + lam * T3b
print("N2 (float, sector quadrature, kink split, n=16 vs 32 differ by %.0e; sector area %.12f vs pi/12 = %.12f): staircase T1111, T1122, "
      "T1212 = %.8f %.8f %.8f, A = %.10f, eta_lat = A/T1122 = %.4f; axes+faces %.8f %.8f %.8f, A = %.10f, eta_lat = %.4f "
      "(block 51's axis hops: A/T1122 = 1); mixture lambda = %.8f: alpha = %.6f, beta = %.6f, A = %.1e" %
      (dN2, ar1, np.pi / 12, *T1b, A1, A1 / T1b[1], *T3b, A3, A3 / T3b[1], lam, Tm[1], Tm[2], Tm[0] - Tm[1] - 2 * Tm[2]))
check("N2 converged", dN2 < 1e-9 and abs(ar1 - np.pi / 12) < 1e-12 and max(abs(T1b[0] - 0.25), abs(T3b[0] - 0.25), abs(T1b[1] - 0.125), abs(T3b[1] - 0.125)) < 1e-12,
      "the two orders agree to 1e-9 and T1111, T1122 match H7's 1/4, 1/8 to 1e-12")

G48 = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        Mg = np.zeros((3, 3))
        for r, cidx in enumerate(perm):
            Mg[r, cidx] = sg[r]
        G48.append(Mg)


def fl_rule(Mf, s):
    """the rule's M at a general s, by the frame: M(g s0) = g M(s0) g^T with g the signed permutation to the sector."""
    ab = np.abs(s)
    order = sorted(range(3), key=lambda m: (-ab[m], m))
    g = np.zeros((3, 3))
    for r, m in enumerate(order):
        g[m, r] = 1.0 if s[m] >= 0 else -1.0
    return g @ Mf(*ab[order]) @ g.T


def A_full(Mf, n):
    """independent route: the full sphere as 48 images of the sector, T1111 - T1122 - 2 T1212 read off directly."""
    xr, wr = np.polynomial.legendre.leggauss(n)
    T, area = np.zeros((3, 3, 3, 3)), 0.0
    for px, pw in zip(xr, wr):
        psi, dpsi = (px + 1) * np.pi / 8, np.pi / 8 * pw
        rmax, rk = 1 / np.sqrt(1 + np.cos(psi) ** 2), 1 / np.sqrt(1 + (np.cos(psi) + np.sin(psi)) ** 2)
        for lo, hi in ((0.0, rk), (rk, rmax)):
            for rx, rw in zip(xr, wr):
                rho, drho = lo + (rx + 1) * (hi - lo) / 2, (hi - lo) / 2 * rw
                b, c = rho * np.cos(psi), rho * np.sin(psi)
                a = np.sqrt(1 - b * b - c * c)
                dA = rho * drho * dpsi / a
                for g in G48:
                    s = g @ np.array([a, b, c])
                    T += dA * np.einsum("i,j,kl->ijkl", s, s, fl_rule(Mf, s))
                    area += dA
    T /= area
    return T[0, 0, 0, 0] - T[0, 0, 1, 1] - 2 * T[0, 1, 0, 1]


A1f, A3f = A_full(M_R1, 12), A_full(M_R3, 12)
print("N1 (float, independent route: 48 images, the tensor read off in the lab frame, n=12): staircase %.10f, axes+faces %.10f" %
      (A1f, A3f))
check("N1 signs", A1 < -1e-3 and A3 > 1e-3 and abs(A1f - A1) < 1e-8 and abs(A3f - A3) < 1e-8,
      "the two routes agree to 1e-8 and the anisotropies have opposite signs with margins far above both, so a convex "
      "mixture has T exactly isotropic (T is linear in the rule); lambda itself is a float")

print("time %.0f s" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PARTIAL (answers a1's open item 3 and block 52's open route 1 up to one float). Exact: every unit content s is the "
      "barycentre of its forward, sign-compatible neighbours among the 26 (staircase interpolation between a u_i + b u_j + c u_k "
      "and (a-b)u_i + (b-c)(u_i+u_j) + c(u_i+u_j+u_k), t = (1-a)/(b+c)): continuous cubic-covariant forward rules with a "
      "constant speed AND a constant total rate exist, so the first-order capture law is rho for every content and a1's far "
      "shadow (flux form) is isotropic. Every sign-compatible rule with mean s has M_mm = |s_m|, so T1111 = 1/4, T1122 = 1/8 "
      "(block 52's least diffusion) and isotropy is T1212 = 1/16; no constant-rate rule has M(s) in span{I, s s^T} on the arcs (a, b, 0). Float: T1212 = "
      "%.5f (staircase), %.5f (axes-and-faces), so the mixture lambda = %.4f is isotropic." % (T1b[2], T3b[2], lam))
print("HIT: forward-only hop rules on the 26 neighbours with a constant speed and a constant total rate exist (every unit s is "
      "the barycentre of its forward sign-compatible neighbours; explicit continuous rule, at most five targets), giving an "
      "isotropic capture law and far shadow; for every sign-compatible rule with mean s, T1111 = 1/4 and T1122 = 1/8 exactly, "
      "so (a)'s isotropy is T1212 = 1/16, met (float quadrature) by a mixture of the staircase and an axes-and-faces rule")
