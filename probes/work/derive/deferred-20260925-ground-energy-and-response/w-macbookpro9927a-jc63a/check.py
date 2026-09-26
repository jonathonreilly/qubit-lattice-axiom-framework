#!/usr/bin/env python3
"""Moment-free initial-lag response for the common matter/rotor law -- worker w-macbookpro9927a-jc63a.

Recovery of #9208 (landed at 6b414efff9; group ground-energy-and-response with #9199, #9206).
Families (see ATTEMPT.md):
  D  the gated electric term's mixed second difference is 2 eps tau v n^2 per edge; A_nu = sum_e v_b nu_e^2 is
     bounded; on an elementary plaquette A_p = 2 (v_b1 + v_b2) <= 4.
  C  the exact commutator [U_u(W^eps), W^tau] = W^(eps+tau) e^(iuKf_eps) (e^(2iuK eps tau A) - 1) on a truncated
     single-edge rotor, and the bound |e^(ix) - 1| <= |x|.
  L  the strong limit and the slope matrix: R_XX = KA - K/2 (W^2 + W^-2) A, R_YY = KA + K/2 (W^2 + W^-2) A,
     R_XY = iK/2 (W^2 - W^-2) A; R_XX + R_YY = 2KA = F.
  S  sharpness of the route: a quartic electric term has an unbounded mixed second difference.
Everything is exact (sympy).
"""
import sys
from itertools import product

import sympy as sp

FAILS = []


def ok(tag, cond, msg=""):
    if not cond:
        FAILS.append(tag)
    print(f"{tag} {'ok' if cond else 'FAIL'} {msg}".rstrip())


E, q, v, n, K, u = sp.symbols('E q v n K u', real=True)
eps, tau = sp.symbols('epsilon tau', real=True)

# ------------------------------------------------------------------ family D
De = lambda x: v * x * (x - q)                 # one edge a -> b: gate v = 1[q_b = 0], A charge q = +-1
mixed = sp.expand(De(E + (eps + tau) * n) - De(E + tau * n) - De(E + eps * n) + De(E))
ok("D1", sp.simplify(mixed - 2 * eps * tau * v * n**2) == 0,
   "per edge D_e = v E (E - q): D_e(E+(eps+tau)n) - D_e(E+tau n) - D_e(E+eps n) + D_e(E) = 2 eps tau v n^2, with "
   "no E and no q: A_nu = sum_e v_b nu_e^2 is a bounded gate observable for every finite integer loop nu")
# plaquettes on the bipartite cubic lattice: vertices alternate A (even) / B (odd); each B corner meets two edges
okp = True
for base in product(range(2), repeat=3):
    for mu_, nu_ in ((0, 1), (0, 2), (1, 2)):
        cyc = [base]
        for step in (mu_, nu_):
            x = list(cyc[-1]); x[step] += 1; cyc.append(tuple(x))
        x = list(base); x[nu_] += 1; cyc.insert(3, tuple(x))
        corners = [cyc[0], cyc[1], cyc[2], cyc[3]]
        par = [sum(c) % 2 for c in corners]
        okp &= par in ([0, 1, 0, 1], [1, 0, 1, 0])
        bcorners = [c for c, p in zip(corners, par) if p == 1]
        edges = [(corners[i], corners[(i + 1) % 4]) for i in range(4)]
        okp &= all(sum(1 for e in edges if b in e) == 2 for b in bcorners) and len(bcorners) == 2
ok("D2", okp, "every elementary plaquette alternates A/B corners, and each of its two B corners meets two of its "
   "edges: A_p = 2(v_b1 + v_b2), 0 <= A_p <= 4 (so ||[U_u(W^eps), W^tau]|| <= 8K|u|)")

# ------------------------------------------------------------------ family C
# single edge, electric values E in a window; W|E> = |E+1>; gate v and charge q kept symbolic (commute with W)
Es = list(range(-4, 5))
N = len(Es)
Wm = sp.zeros(N, N)
for i in range(N - 1):
    Wm[i + 1, i] = 1                                    # |E> -> |E+1>
Dm = sp.diag(*[De(e) for e in Es])
Uu = lambda A: sp.diag(*[sp.exp(sp.I * u * K * Dm[i, i]) for i in range(N)]) * A * \
    sp.diag(*[sp.exp(-sp.I * u * K * Dm[i, i]) for i in range(N)])
c_ok = True
for e_, t_ in product((1, -1), repeat=2):
    We = Wm if e_ == 1 else Wm.T
    Wt = Wm if t_ == 1 else Wm.T
    lhs = Uu(We) * Wt - Wt * Uu(We)
    Wet = Wm**2 if e_ + t_ == 2 else ((Wm.T)**2 if e_ + t_ == -2 else sp.eye(N))
    f = sp.diag(*[De(Es[i] + e_) - De(Es[i]) for i in range(N)])
    rhs = Wet * sp.diag(*[sp.exp(sp.I * u * K * f[i, i]) for i in range(N)]) * \
        (sp.exp(2 * sp.I * u * K * e_ * t_ * v) - 1)
    for i in range(2, N - 2):                         # columns away from the window's edges
        for j in range(N):
            c_ok &= sp.simplify(sp.expand(lhs[j, i] - rhs[j, i])) == 0
x = sp.symbols('x', real=True)
bound_ok = sp.simplify(sp.Abs(sp.exp(sp.I * x) - 1)**2 - 4 * sp.sin(x / 2)**2) == 0
ok("C1", c_ok and bound_ok,
   "single-edge rotor (A = v for one edge, n = 1): [U_u(W^eps), W^tau] = W^(eps+tau) e^(iuK f_eps) (e^(2iuK eps "
   "tau v) - 1) exactly for all four sign pairs; |e^(ix) - 1| = 2|sin(x/2)| <= |x|")

# ------------------------------------------------------------------ family L
A_, f_ = sp.symbols('A f', real=True)
lim_ok = all(sp.limit(sp.exp(sp.I * u * K * f_) * (sp.exp(2 * sp.I * u * K * s1 * s2 * A_) - 1) / u, u, 0)
             == 2 * sp.I * K * s1 * s2 * A_ for s1 in (1, -1) for s2 in (1, -1))
# slope matrix from the W-algebra: (i/u)[U_u(Q_a), Q_b] -> sum a_eps b_tau (i)(2iK eps tau) W^(eps+tau) A
Wp, Wmm = sp.symbols('Wp2 Wm2')                          # stand for W^2 and W^-2 (A commutes with W)
coef = {'X': {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}, 'Y': {1: 1 / (2 * sp.I), -1: -1 / (2 * sp.I)}}
def R(al, be):
    tot = 0
    for e_, t_ in product((1, -1), repeat=2):
        w = {2: Wp, -2: Wmm, 0: 1}[e_ + t_]
        tot += coef[al][e_] * coef[be][t_] * sp.I * 2 * sp.I * K * e_ * t_ * w * A_
    return sp.expand(tot)
Rxx, Ryy, Rxy, Ryx = R('X', 'X'), R('Y', 'Y'), R('X', 'Y'), R('Y', 'X')
slope_ok = (sp.simplify(Rxx - (K * A_ - K / 2 * (Wp + Wmm) * A_)) == 0
            and sp.simplify(Ryy - (K * A_ + K / 2 * (Wp + Wmm) * A_)) == 0
            and sp.simplify(Rxy - sp.I * K / 2 * (Wp - Wmm) * A_) == 0 and sp.simplify(Rxy - Ryx) == 0
            and sp.simplify(Rxx + Ryy - 2 * K * A_) == 0)
ok("L1", lim_ok and slope_ok,
   "(1/u) e^(iuKf)(e^(2iuK eps tau A) - 1) -> 2iK eps tau A; slope operators R_XX = KA - K/2 (W^2+W^-2) A, "
   "R_YY = KA + K/2 (W^2+W^-2) A, R_XY = R_YX = iK/2 (W^2 - W^-2) A; R_XX + R_YY = 2KA = F_nu")

# ------------------------------------------------------------------ family S
D4 = lambda x: x**4
m4 = sp.expand(D4(E) - D4(E - 1) - D4(E + 1) + D4(E))     # eps = +1, tau = -1
step = sp.expand(m4.subs(E, E + 1) - m4)
ok("S1", sp.simplify(m4 + 12 * E**2 + 2) == 0 and sp.simplify(step + 24 * E + 12) == 0,
   "quartic electric term: mixed second difference -(12E^2 + 2), unbounded, with steps 24E + 12; so for small "
   "u > 0 the phases uK(12E^2+2) sweep past pi/2 in steps < pi/2 and ||(1/u)[U_u(W), W*]|| >= sqrt 2/u: the "
   "bounded-quotient route needs the quadratic (bounded mixed difference) electric term")

print(f"checks: {'all passed' if not FAILS else 'FAILED ' + ' '.join(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
    sys.exit(1)
print("SUMMARY: PARTIAL #9208's Wilson-quadrature impulse response has an initial-lag slope for every normal "
      "state (no electric moment), with explicit slope operators; the review PRE's bounded strong-quotient route "
      "is validated independently; the route needs the bounded mixed second difference; #9199 and #9206's "
      "stronger claims stay open")
print("HIT: In #9208's common matter/rotor law on a fixed finite cubic torus, for every normal initial density "
      "rho_0, every t >= 0 and every finite integer loop nu, the lag slope lim_{u->0} chi_{a<-b}(t,u)/u of the "
      "Wilson-quadrature impulse response exists and equals Tr rho_t [Q_b,[KD,Q_a]], with R_XX = KA - K/2 "
      "(W^2+W^-2)A, R_YY = KA + K/2 (W^2+W^-2)A, R_XY = R_YX = iK/2 (W^2-W^-2)A, A = sum_e v_b nu_e^2; the "
      "quadrature sum is Tr rho_t F_nu = 2K<A>_t (4K<v_b1 + v_b2>_t on a plaquette). No moment is needed: the "
      "gated electric term's mixed second difference is 2 eps tau A exactly, so (i/u)[U_u(Q_a),Q_b] is bounded "
      "by 2K||A|| and converges strongly, and H4 and the formation channels enter through a bounded Duhamel term "
      "that vanishes on Q. This removes the landed note's fourth-moment hypothesis for its (3)-(5); the route "
      "fails for a quartic electric term (unbounded mixed difference).")
