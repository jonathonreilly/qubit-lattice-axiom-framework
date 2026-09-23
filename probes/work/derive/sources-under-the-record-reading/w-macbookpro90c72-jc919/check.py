#!/usr/bin/env python3
"""J:derive:sources-under-the-record-reading:a4 (worker w-macbookpro90c72-jc919): exact checks.

Simplest bond energy F = (2/g) sum_bonds (phi_x - phi_y)^2 (block 55 T4(c)), walls of a box held at the ambient rate
phi = 1, amplitudes timed by H_w = phi H phi (block 54), static law and ledger <H_w> + F (block 55's premise).
  L. The ledger is a quadratic form in phi for EVERY amplitude, so the static law is linear in phi: exact.
  B. (b) formation: the point record's ledger E/(1 + k E g_yy), k = g/12; the record energy that keeps the ledger,
     E' = Lam/(1 - k Lam g_yy), for a rest amplitude and for a moving one (walk + rest term); its weak-field form
     k(E^2 g_yy - e.g.e); its dependence on the formation site in a box (none on Z^3); the star's closed form and
     the failure of wall-independence for larger symmetric amplitudes.
  A. (a) records only: the momentum imbalance of block 55 T3 with the packet's source zero.
  C. (c) a discriminator from the test body's records: an amplitude in two places.
All finite claims in exact rationals (fractions); Z^3 Green values at 30 digits (mpmath) for one remark.
"""
import sys
import time
from fractions import Fraction as Fr

import mpmath as mp

T0 = time.time()
FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(s, d):
    return (s[0] + d[0], s[1] + d[1], s[2] + d[2])


def interior(n):
    """interior sites of an n^3 box (n odd) centred at the origin; its boundary layer is the held wall."""
    h = (n - 1) // 2
    return [(x, y, z) for x in range(-h + 1, h) for y in range(-h + 1, h) for z in range(-h + 1, h)]


def solve_multi(A, Bs):
    """exact Gaussian elimination, sparse rows (dicts), structurally symmetric, several right-hand sides."""
    N = len(A)
    A = [dict(r) for r in A]
    Bs = [list(b) for b in Bs]
    for k in range(N):
        piv = A[k][k]
        rowk = A[k]
        for i in [j for j in rowk if j > k]:
            f = A[i].get(k)
            if not f:
                continue
            f = f / piv
            for j, v in rowk.items():
                if j >= k:
                    A[i][j] = A[i].get(j, 0) - f * v
            for b in Bs:
                b[i] -= f * b[k]
            A[i].pop(k, None)
    out = []
    for b in Bs:
        x = [Fr(0)] * N
        for k in range(N - 1, -1, -1):
            x[k] = (b[k] - sum(v * x[j] for j, v in A[k].items() if j > k)) / A[k][k]
        out.append(x)
    return out


def static_ledger(n, M, gam):
    """minimise/stationarise Lam(phi) = sum_xy M_xy phi_x phi_y + (2/gam) sum_bonds (phi_x - phi_y)^2, walls phi = 1.
    M: dict {(s, t): value}, symmetric. Returns (Lam, phi)."""
    S = interior(n)
    idx = {s: i for i, s in enumerate(S)}
    c = Fr(2) / gam
    A = [dict() for _ in S]
    b = [Fr(0)] * len(S)
    for s, i in idx.items():
        A[i][i] = A[i].get(i, 0) + 6 * c
        for d in NB:
            t = add(s, d)
            if t in idx:
                A[i][idx[t]] = A[i].get(idx[t], 0) - c
            else:
                b[i] += c
    for (s, t), v in M.items():
        A[idx[s]][idx[t]] = A[idx[s]].get(idx[t], 0) + v
    phi = dict(zip(S, solve_multi(A, [b])[0]))
    lam = sum(v * phi[s] * phi[t] for (s, t), v in M.items())
    bonds = Fr(0)
    for s in S:
        for d in NB:
            t = add(s, d)
            if t in phi:
                if t > s:
                    bonds += (phi[s] - phi[t]) ** 2
            else:
                bonds += (phi[s] - 1) ** 2
    return lam + c * bonds, phi


def greens(n, ys):
    """g(., y) for (1 - average) with the walls held at zero, for each y in ys (one elimination)."""
    S = interior(n)
    idx = {s: i for i, s in enumerate(S)}
    A = [dict() for _ in S]
    for s, i in idx.items():
        A[i][i] = Fr(1)
        for d in NB:
            t = add(s, d)
            if t in idx:
                A[i][idx[t]] = Fr(-1, 6)
    Bs = []
    for y in ys:
        b = [Fr(0)] * len(S)
        b[idx[y]] = Fr(1)
        Bs.append(b)
    return [dict(zip(S, x)) for x in solve_multi(A, Bs)]


def rest(m):
    return {(s, s): v for s, v in m.items()}


O = (0, 0, 0)
gam = Fr(1)
k = gam / 12

# ================= B. the formation ledger =================
g7 = greens(7, [O])[0]
g9 = greens(9, [O])[0]
good = True
for n, g in ((7, g7), (9, g9)):
    for Ep in (Fr(1), Fr(3), Fr(12)):
        lam, phi = static_ledger(n, rest({O: Ep}), gam)
        good &= lam == Ep / (1 + k * Ep * g[O]) and phi[O] == 1 / (1 + k * Ep * g[O]) and lam == Ep * phi[O]
ok("B1", good, "one record of energy E at y, walls held: the static law is linear in phi, phi_y = 1/(1 + k E g_yy) "
   f"and the ledger is E/(1 + k E g_yy) exactly (k = gamma/12; boxes 7, 9, E = 1, 3, 12; g_yy = {g7[O]}, {g9[O]})")

# a rest amplitude: uniform on the 3^3 cube, E = 1; the record energy that keeps the ledger at each formation site
cube = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
E = Fr(1)
mc = {s: E / 27 for s in cube}
lam_c, _ = static_ledger(7, rest(mc), gam)
gs = greens(7, cube)
Ep = {y: lam_c / (1 - k * lam_c * gs[i][y]) for i, y in enumerate(cube)}
ege = sum(mc[x] * mc[y] * gs[j][x] for j, y in enumerate(cube) for x in cube)
vals = sorted(set(Ep.values()))
nbelow = sum(1 for y in cube if Ep[y] < E)
ok("B2", len(vals) == 4 and Ep[O] == vals[-1],
   f"3^3 cube amplitude, E = 1, gamma = 1, box 7: ledger {float(lam_c):.10f}; the record energy that keeps it, "
   f"E'_y = Lam/(1 - k Lam g_yy), takes {len(vals)} values over the 27 formation sites, "
   f"{float(vals[0]):.8f} (corner) to {float(vals[-1]):.8f} (centre), below E at {nbelow} sites: it depends on "
   "where the record forms")

# weak field: E'_y - E -> k (E^2 g_yy - e.g.e) as gamma -> 0 (exact values at gamma = 1/10^4 and 1/10^5)
good, rows = True, []
for small in (Fr(1, 10**4), Fr(1, 10**5)):
    kk = small / 12
    lam_s, _ = static_ledger(7, rest(mc), small)
    y = O
    gy = gs[cube.index(y)][y]
    Eps = lam_s / (1 - kk * lam_s * gy)
    ratio = (Eps - E) / (kk * (E * E * gy - ege))
    rows.append(f"gamma={small}: ratio {float(ratio):.8f}")
    good &= abs(ratio - 1) < 30 * small
ok("B3", good, "weak field: the record must carry E' - E = (gamma/12)(E^2 g_yy - <e, g e>) + O(gamma^2), the change "
   f"of the field's self-energy; centre formation, <rho, g rho> = {float(ege):.10f}, g_yy = {float(gs[13][O]):.10f}: "
   + "; ".join(rows))

# a moving amplitude: walk H = sum_a sigma_a S_a (symbol sin k_a) plus a rest term m*1, on the 7-site star
I = complex(0, 1)
SIG = [((0, 1), (1, 0)), ((0, -1j), (1j, 0)), ((1, 0), (0, -1))]


def cmat(a):
    return [[complex(v) for v in row] for row in a]


def hop(sa, sign):
    """H_{x, x + e_a} = sigma_a/(2i) (sign +1), H_{x, x - e_a} = -sigma_a/(2i) (sign -1)."""
    return [[sign * v / (2 * I) for v in row] for row in cmat(sa)]


def quad(chi_x, Hm, chi_y):
    """Re chi_x^dagger Hm chi_y, exact for Gaussian-rational chi (entries as (re, im) Fractions)."""
    total_re = Fr(0)
    for a in range(2):
        for b in range(2):
            h = Hm[a][b]
            hr, hi = Fr(h.real).limit_denominator(4), Fr(h.imag).limit_denominator(4)
            xr, xi = chi_x[a]
            yr, yi = chi_y[b]
            # conj(x) * h * y, real part
            pr, pi_ = xr * hr + xi * hi, xr * hi - xi * hr
            total_re += pr * yr - pi_ * yi
    return total_re


chi = {O: ((Fr(1), Fr(0)), (Fr(1, 2), Fr(1, 2)))}
for j, d in enumerate(NB):
    chi[d] = ((Fr(1, 2), Fr(j % 3 - 1, 4)), (Fr(-1, 3) if j % 2 else Fr(1, 3), Fr(1, 4)))
mass = Fr(2)
M = {}
for s, cs in chi.items():
    M[(s, s)] = M.get((s, s), 0) + mass * sum(a * a + b * b for a, b in cs)
    for a_i, d in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
        for sign in (1, -1):
            t = add(s, tuple(sign * c for c in d))
            if t in chi:
                M[(s, t)] = M.get((s, t), 0) + quad(cs, hop(SIG[a_i], sign), chi[t])
sym = all(M[(s, t)] == M.get((t, s)) for (s, t) in M)
Ebare = sum(M.values())
e = {s: sum(v for (a, b), v in M.items() if a == s) for s in chi}
kin = sum(v for (a, b), v in M.items() if a != b)
lam_m, _ = static_ledger(7, M, gam)
Epm = lam_m / (1 - k * lam_m * g7[O])
lam_ms, _ = static_ledger(7, M, Fr(1, 10**4))
g7s = greens(7, list(chi))
ege_m = sum(e[x] * e[y] * g7s[j][x] for j, y in enumerate(chi) for x in chi)
kk = Fr(1, 10**4) / 12
Eps = lam_ms / (1 - kk * lam_ms * g7[O])
ratio = (Eps - Ebare) / (kk * (Ebare ** 2 * g7[O] - ege_m))
ok("B4", sym and kin != 0 and abs(ratio - 1) < Fr(1, 100),
   f"moving amplitude (walk + rest term 2, Gaussian-rational chi on the star; hopping part of <H> = {float(kin):+.6f}, "
   f"E = {float(Ebare):.6f}): the law is still linear in phi; kept-ledger record energy at the centre {float(Epm):.10f} "
   f"(exact rational); weak-field ratio (E'-E)/(k(E^2 g_yy - e.g.e)) = {float(ratio):.6f} at gamma = 1e-4, with e the "
   "full energy density, hopping included")

# the star: closed form and wall-independence; larger symmetric amplitudes are not wall-independent
good = True
for m0, m1 in ((Fr(1, 7), Fr(1, 7)), (Fr(1, 2), Fr(1, 12))):
    ms = {O: m0, **{d: m1 for d in NB}}
    c = m0 / (1 + k * m0) + 6 * m1
    closed = c / (1 - k * c)
    for n, g in ((7, g7), (9, g9)):
        lam_s, _ = static_ledger(n, rest(ms), gam)
        good &= lam_s / (1 - k * lam_s * g[O]) == closed
    if m0 == m1:
        star_val = closed
edge = [(a, b, 0) for a in (1, -1) for b in (1, -1)] + [(a, 0, b) for a in (1, -1) for b in (1, -1)] + \
       [(0, a, b) for a in (1, -1) for b in (1, -1)]
far = [(2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)]
diffs = []
for sites in ([O] + NB + edge, [O] + far):
    ms = {s: Fr(1, len(sites)) for s in sites}
    v = []
    for n, g in ((7, g7), (9, g9)):
        lam_s, _ = static_ledger(n, rest(ms), gam)
        v.append(lam_s / (1 - k * lam_s * g[O]))
    diffs.append(v[1] - v[0])
ok("B5", good and star_val == Fr(1188, 1091) and all(dd != 0 for dd in diffs),
   "star (centre m0, six neighbours m1): the field outside it is exactly a point charge at the centre, and the "
   "record energy keeping the ledger is c/(1 - k c), c = m0/(1 + k m0) + 6 m1, the same in boxes 7 and 9 "
   f"(uniform star, gamma = 1: {star_val}); larger symmetric amplitudes differ between the boxes: 19-site ball "
   f"{float(diffs[0]):+.3e}, distance-2 cross {float(diffs[1]):+.3e}")

# Z^3 remark: g_yy = G0(0) for every y (no walls), so the kept-ledger energy is site-independent there
mp.mp.dps = 30
g0 = (mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24)
      * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24))
ok("B6", abs(g0 - mp.mpf("1.5163860591519780181")) < 1e-18,
   f"on Z^3 (ambient held at infinity) g_yy = G0(0) = {mp.nstr(g0, 12)} at every site: the record energy that keeps "
   "the ledger, Lam/(1 - k Lam G0(0)), does not depend on where the record forms, so a rule that is blind to the "
   "site keeps it exactly there; in a held box (B2) it cannot, and a site-blind energy keeps it on average only "
   "for particular odds")

# ================= A. records only: the unmatched pull =================
gL = greens(9, [(0, -2, 0), (0, 2, 0)])
gp = gL[0]
xp = (1, 0, 0)
pull = -(gam / 6) * (gp[add(xp, (0, 1, 0))] - gp[add(xp, (0, -1, 0))]) / 2
ok("A1", pull != 0, "records only: a packet (energy 1) at (1,0,0) beside a record (energy 1) at (0,-2,0), box 9: the "
   f"packet's pull E_p grad_c u_rec has y-component {float(-pull):+.6f} (exact rational); the record feels nothing "
   "from the packet, so (pull on packet) + (pull on record) = that value: block 55 T3 with S_packet = 0")

# ================= C. the discriminator =================
gR = gL[1]
path = [(x, -1, 0) for x in range(-3, 4)]


def kick(gsrc, w):
    """transverse (y) momentum given to a test packet of energy 1 moving along the x-line y = -1, z = 0, unit speed:
    - sum over the path of grad_y u, u = -(gamma/6) w g(., source)."""
    s = Fr(0)
    for p in path:
        up = gsrc.get(add(p, (0, 1, 0)), Fr(0))
        dn = gsrc.get(add(p, (0, -1, 0)), Fr(0))
        s += (up - dn) / 2
    return (gam / 6) * w * s


dL, dR = kick(gp, 1), kick(gR, 1)
dC = kick(gp, Fr(1, 2)) + kick(gR, Fr(1, 2))
ok("C1", dC == (dL + dR) / 2 and len({dL, dR, dC, Fr(0)}) == 4,
   f"source of energy 1 in two places (0,-2,0), (0,2,0); test line y = -1: kick if the source has formed at one "
   f"place {float(dL):+.6f} or {float(dR):+.6f}, unformed under records only 0, under amplitude sourcing "
   f"{float(dC):+.6f} = their mean (exact): four distinct values")

print(f"runtime {time.time() - T0:.0f} s")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PARTIAL: (b) exact for every amplitude, moving included (linear static law, record ledger "
      "E/(1 + k E g_yy), kept-ledger energy); the star's wall-independence in closed form and its failure for larger "
      "symmetric amplitudes; (a) the unmatched pull; (c) a two-place discriminator; (d) in ATTEMPT.md.")
print("HIT: with the simplest bond energy the ledger <H_w> + F is a quadratic form in phi for every amplitude, so the "
      "static law with held walls is linear: a record of energy E at y has ledger E/(1 + k E g_yy), k = gamma/12, and "
      "formation keeps the ledger iff E' = Lam/(1 - k Lam g_yy), Lam the amplitude's static ledger (hopping energy "
      "included), i.e. E' - E = k(E^2 g_yy - <e, g e>) + O(k^2); site-dependent in a box, site-blind on Z^3. The star "
      "amplitude sources exactly a point charge outside itself: E' = c/(1 - k c), c = m0/(1 + k m0) + 6 m1, "
      "wall-independent (1188/1091 at gamma = 1); larger symmetric amplitudes are not. A source in two places gives "
      "a test body the mean of the one-place kicks only under amplitude sourcing; under records only the kick is 0 "
      "or one of them.")
