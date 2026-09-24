#!/usr/bin/env python3
"""Referee check for bound-bodies-and-the-two-far-fields a2.

One interior site of Z^3, six held wall neighbours. Content on the six wall
bonds plus a rest term. Independent of the attempt's box, which puts no
content on wall bonds.
"""
import sympy as sp

K, h, rho = sp.symbols("K h rho", positive=True)
u, lam = sp.symbols("u lam", real=True)
w = sp.exp(u)
chi = sp.exp(lam / 2)
N = w * chi
# six wall neighbours, each at w = chi = 1
deg = 6
# bond energy to one wall: h * sqrt(w * 1) / (chi * 1)
bond = h * sp.sqrt(w) / chi
E = rho * w + deg * bond
# Delta chi at interior = deg * (1 - chi); at one wall = chi - 1
# F = -8K * sum_bonds (N_wall - N)(chi_wall - chi) = -8K * deg * (1 - N)(1 - chi)
F = -8 * K * deg * (1 - N) * (1 - chi)
Q = -deg * (1 - chi)          # -Delta chi_interior
P = deg * (N - 1)             # Delta N_interior = deg * (1 - N)? 
# lap(N)_interior = sum_walls (N_wall - N) = deg * (1 - N)
# attempt: P = sum_interior Delta N, so P = deg*(1-N) = -deg*(N-1)
P = deg * (1 - N)

ledger = E + F
# interior stationarity of the ledger
su = sp.diff(ledger, u)
sl = sp.diff(ledger, lam)
sol = sp.solve([su, sl], [h, rho], dict=True)[0]

def at(expr):
    return sp.simplify(expr.subs(sol))

T_int = at(-sp.diff(E, lam))
# each wall bond contributes half its energy to the wall's u-derivative
# tau_wall for one wall = half a bond; six walls: T_walls = deg * (bond/2) on the solution
T_walls = at(deg * (bond / 2))
E_s, F_s, Q_s, P_s = at(E), at(F), at(Q), at(P)
rate_residual = sp.simplify(8 * K * Q_s - (E_s + F_s))
length_residual = sp.simplify(P_s - Q_s - (T_int - F_s) / (4 * K))
sum_residual = sp.simplify(P_s + Q_s - (E_s + T_int) / (4 * K))

# a concrete stationary point: u = log 2, lam = 0, K = 1
num = {u: sp.log(2), lam: 0, K: 1}
rate_n = sp.simplify(rate_residual.subs(num))
length_n = sp.simplify(length_residual.subs(num))
# stationarity really holds at that point
stat_u = sp.simplify(su.subs(sol).subs(num))
stat_l = sp.simplify(sl.subs(sol).subs(num))

ok_counter = stat_u == 0 and stat_l == 0 and rate_n != 0 and length_n == 0
print(
    "step2: interior stationarity holds, but 8KQ - (E+F) = "
    f"{rate_n} at u=log 2, lam=0, K=1; P-Q-(T_interior-F)/(4K) = {length_n}"
)
print(
    "wall content: 8KQ - (E+F) + T_walls simplifies to "
    f"{sp.factor(sp.simplify(rate_residual + T_walls))}"
)
if ok_counter:
    print(
        "SUMMARY: fails at step 2 - 8KQ = E+F does not hold once content sits on bonds "
        "that touch a held wall; the wall share of dE/du is omitted. "
        f"At the stationary point u=log 2, K=1, the residual is {rate_n}, while "
        "P - Q = (T_interior - F)/(4K) still holds"
    )
else:
    print("SUMMARY: fails at the referee check - the one-site counterexample did not evaluate")
