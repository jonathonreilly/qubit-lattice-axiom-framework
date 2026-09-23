#!/usr/bin/env python3
"""J:derive:gamma-the-one-number:a2 -- worker w-macbookpro90c72-j0f83 (claude-opus-5-5).

Block 55's simplest bond energy F = (2/gamma) sum_bonds (phi_x - phi_y)^2 and a point body of bare rest energy m on a box
with walls held at the ambient rate. Every line is exact (Fractions, sympy).
"""
import itertools, sys, time
from fractions import Fraction as F
import sympy as sp

T0 = time.time(); FAILS = []
def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)

def solve_linear(A, b):
    """exact Gaussian elimination over the rationals."""
    n = len(A); M = [row[:] + [bi] for row, bi in zip(A, b)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        piv = M[c][c]; M[c] = [v / piv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
    return [M[r][n] for r in range(n)]

def box(n):
    sites = list(itertools.product(range(n), repeat=3)); idx = {s: i for i, s in enumerate(sites)}
    nbr = []
    for s in sites:
        lst = []
        for j in range(3):
            for d in (1, -1):
                t = list(s); t[j] += d; t = tuple(t)
                lst.append(idx[t] if t in idx else None)            # None = wall at the ambient rate (phi = 1)
        nbr.append(lst)
    return sites, idx, nbr

def G0_at_centre(n):
    """(1 - average over six neighbours) g = delta at the centre, g = 0 on the walls."""
    sites, idx, nbr = box(n); N = len(sites); c = idx[(n // 2,) * 3]
    A = [[F(0)] * N for _ in range(N)]; b = [F(0)] * N
    for i in range(N):
        A[i][i] += 1
        for j in nbr[i]:
            if j is not None:
                A[i][j] -= F(1, 6)
    b[c] = F(1)
    g = solve_linear(A, b)
    return g[c], g, sites, idx, nbr, c

def body(n, gam, m):
    """divided law: phi_x - avg phi = 0 off the body, (12/gamma)(phi_0 - avg phi) = -m phi_0 at the body; walls phi = 1."""
    g0, g, sites, idx, nbr, c = G0_at_centre(n); N = len(sites)
    A = [[F(0)] * N for _ in range(N)]; b = [F(0)] * N
    for i in range(N):
        coef = F(12) / gam if i == c else F(1)
        A[i][i] += coef + (m if i == c else 0)
        for j in nbr[i]:
            if j is None:
                b[i] += coef / 6
            else:
                A[i][j] -= coef / 6
    phi = solve_linear(A, b)
    return phi, g0, nbr, c

# ------------------------------------------------------------------ G.a: the point body, exactly, and the undivided law
good = True; rows = []
for n in (1, 3, 5):
    for gam, m in ((F(1), F(3)), (F(7, 2), F(2, 5))):
        phi, g0, nbr, c = body(n, gam, m)
        x = gam * g0 * m / 12
        good &= phi[c] == 1 / (1 + x)
        # the undivided law (12/gamma) phi_x (phi_x - avg phi) = -e_x with e = m phi_0^2 at the body, 0 elsewhere (mu = 0: walls held)
        for i in range(len(phi)):
            avg = sum((phi[j] if j is not None else F(1)) for j in nbr[i]) / 6
            e = m * phi[i] ** 2 if i == c else F(0)
            good &= F(12) / gam * phi[i] * (phi[i] - avg) == -e
        # every neighbour of the body sits at phi_0 (1 + gamma m/12)
        good &= all((phi[j] if j is not None else F(1)) == phi[c] * (1 + gam * m / 12) for j in nbr[c])
    rows.append(f"side {n}: G0(0) = {g0}")
ok("G.a", good, "on boxes of side 1, 3, 5 with walls at the ambient rate, two (gamma, m) pairs each: dividing the law by phi_x makes it "
   "linear, and the exact solution has phi_0 = 1/(1 + x), x = (gamma/12) G0(0) m, satisfies the undivided law "
   "(12/gamma) phi (phi - avg) = -e at every site, and puts every neighbour of the body at phi_0 (1 + gamma m/12); " + ", ".join(rows))

# ------------------------------------------------------------------ G.self: the proposed self-consistency
gs, ms, g0s = sp.symbols("gamma m G0", positive=True)
phi0 = 1 / (1 + gs * g0s * ms / 12); phin = phi0 * (1 + gs * ms / 12)
kappa = phi0 ** 2 / phin ** 2                     # the record's tick ratio to its neighbours' mean
cond = sp.factor(sp.simplify(kappa - phi0 ** 2))  # kappa equated with exp(u_0) = w_0 = phi_0^2
good = sp.simplify(kappa - 1 / (1 + gs * ms / 12) ** 2) == 0
good &= sp.simplify(cond.subs(g0s, 1)) == 0       # an identity when G0(0) = 1: the body's neighbours are the walls
sol = sp.solve(sp.Eq(kappa, phi0 ** 2), ms)
good &= all(sp.simplify(s_) == 0 for s_ in sol) or sol == []
g0_3 = G0_at_centre(3)[0]; g0_5 = G0_at_centre(5)[0]
good &= G0_at_centre(1)[0] == 1 and g0_3 > 1 and g0_5 > g0_3
ok("G.self", good, "the field gives the record's tick ratio kappa = phi_0^2/phi_nbr^2 = (1 + gamma m/12)^-2 identically, so reading kappa "
   "off the field is an identity with no content; equating it with the site's own rate w_0 = phi_0^2 = (1 + x)^-2 requires "
   "gamma m/12 = x, i.e. G0(0) = 1 or m = 0: an identity exactly when the body's neighbours are the walls (side 1), and for "
   f"every larger box (G0(0) = {g0_3}, {g0_5}) no m > 0 at all; it fixes no value of gamma m")

# ------------------------------------------------------------------ G.sat and G.free: saturation, and gamma as a free label
lim = sp.limit(ms * phi0, ms, sp.oo)
good = sp.simplify(lim - 12 / (gs * g0s)) == 0
# the law is the stationarity of the ledger E_gamma = m w_0 + (2/gamma) sum_bonds (phi_x - phi_y)^2 for EVERY gamma: check on side 3
n = 3; sites, idx, nbr = box(n); c = idx[(1, 1, 1)]
ph = sp.symbols(f"p0:{len(sites)}", positive=True)
inner_bonds = set(); wall_bonds = []                       # wall bonds kept with multiplicity (corner sites have three)
for i in range(len(sites)):
    for j in nbr[i]:
        if j is None:
            wall_bonds.append(i)
        else:
            inner_bonds.add((min(i, j), max(i, j)))
Eg = ms * ph[c] ** 2 + (2 / gs) * (sum((ph[a] - ph[b]) ** 2 for (a, b) in inner_bonds) + sum((ph[i] - 1) ** 2 for i in wall_bonds))
for gam_v, m_v in ((F(1), F(3)), (F(9, 4), F(5, 3))):
    phi, g0, _, _ = body(n, gam_v, m_v)
    subs = {ph[i]: sp.Rational(phi[i].numerator, phi[i].denominator) for i in range(len(sites))}
    subs.update({gs: sp.Rational(gam_v.numerator, gam_v.denominator), ms: sp.Rational(m_v.numerator, m_v.denominator)})
    good &= all(sp.simplify(sp.diff(Eg, ph[i]).subs(subs)) == 0 for i in range(len(sites)))
ok("G.sat", good, "the energy seen from afar m phi_0 = m/(1 + x) tends to 12/(gamma G0(0)) as m -> infinity (exact limit), and on the "
   "side-3 box the solved field is a stationary point of the ledger m w_0 + (2/gamma) sum_bonds (phi_x - phi_y)^2 at two unrelated "
   "gammas: the law and the kept ledger are consistent for every gamma > 0, so gamma labels a family and nothing in blocks 53-55 "
   "selects a member")
print(f"runtime {time.time() - T0:.0f} s")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL nothing in the clauses of blocks 53-55 fixes gamma: the point body is solved exactly, its proposed "
      "self-consistency is an identity or has no solution, the (law, ledger) pair is consistent for every gamma, and reading "
      "gamma from the scale reference presupposes the open gravitational statement a = l_P")
print("HIT: for block 55's simplest bond energy a point body of bare rest energy m on a box with ambient walls has phi_0 = 1/(1 + x), "
      "x = (gamma/12) G0(0) m, and every neighbour at phi_0 (1 + gamma m/12) exactly, so its tick ratio kappa = (1 + gamma m/12)^-2; "
      "equating kappa with the site's rate w_0 holds for every gamma m when the neighbours are the walls and for no m > 0 in any "
      "larger box: the self-consistency fixes nothing.")
print("HIT: the static law and the kept ledger m w_0 + (2/gamma) sum (phi_x - phi_y)^2 are consistent for every gamma > 0 (exact "
      "stationarity at unrelated gammas), no number forced in blocks 39-55 involves the field energy that gamma weights, and the "
      "scale reference (a^-1 = M_Pl, no dimensionless content) yields gamma = 4 pi only by assuming the open statement a = l_P.")
