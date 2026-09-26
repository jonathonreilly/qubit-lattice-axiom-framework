#!/usr/bin/env python3
"""Independent check of record charges under two admissible energies.

Does not import the author's script. The 8^3 float run is not rebuilt.
Detailed balance and the even-kernel cancellation are identities; the
3^3 charges and bond averages are exact fractions.
"""
from fractions import Fraction as Fr
from itertools import combinations, product

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


# --- T1: crossing balance is an identity; leaving-site balance is the other law ---
Wc, Wp, sx, sy, cx, cy, wx, wy = sp.symbols("Wc Wp sx sy cx cy wx wy", positive=True)
cross_f = sx * sy / (cx * cy) * Wp / (Wc + Wp)
cross_b = sy * sx / (cy * cx) * Wc / (Wp + Wc)
site_f = wx * Wp / (Wc + Wp)
site_b = wy * Wc / (Wp + Wc)
pi_c = Wc / wx
pi_p = Wp / wy
check(
    "T1 balance identities",
    sp.simplify(Wc * cross_f - Wp * cross_b) == 0
    and sp.simplify(pi_c * site_f - pi_p * site_b) == 0,
    "pi proportional to W balances the symmetric crossing factor; leaving-site timing balances W/w_leaving",
)
# concrete witness: one move on 3^3
sites = list(product(range(3), repeat=3))
ix = {p: i for i, p in enumerate(sites)}
nb = []
for p in sites:
    nb.append([ix[tuple((p[a] + d) % 3 if a == axis else p[a] for a in range(3))]
               for axis in range(3) for d in (1, -1)])
s = [Fr(k + 2, 5) for k in range(27)]
chi = [Fr(k + 3, 7) for k in range(27)]
w = [v * v for v in s]
C = (0, 4, 8)
y = nb[0][0]
Cp = tuple(sorted((set(C) - {0}) | {y}))
omega = {}
for d in product(range(-1, 2), repeat=3):
    key = tuple(c % 3 for c in d)
    omega[key] = Fr(1 + sum(abs(c) for c in d), 3)


def weight(conf):
    acc = Fr(1)
    for a, b in combinations(conf, 2):
        pa, pb = sites[a], sites[b]
        acc *= omega[tuple((pa[k] - pb[k]) % 3 for k in range(3))]
    return acc


def cross(conf, x, yy, other, ww):
    return s[x] * s[yy] / (chi[x] * chi[yy]) * ww / 6


WcC, WcP = weight(C), weight(Cp)
fwd = cross(C, 0, y, Cp, WcP / (WcC + WcP))
back = cross(Cp, y, 0, C, WcC / (WcP + WcC))
check(
    "T1 witness",
    WcC * fwd == WcP * back and y not in C,
    "one hop on 3^3: W(C) times the crossing rate equals the reverse",
)

# --- T1b: an even displacement kernel cancels at first order ---
def disp(a, b):
    return tuple((sites[b][k] - sites[a][k]) % 3 for k in range(3))


def field(kernel, conf, z):
    return sum(kernel[disp(z, r)] for r in conf)


even = {d: Fr(1 + sum(min(c, 3 - c) ** 2 for c in d), 4) for d in (tuple((sites[j][k]) for k in range(3)) for j in range(27))}
# rebuild even on the 27 displacements from the origin
even = {}
for j, p in enumerate(sites):
    even[p] = Fr(2, 3 + sum(min(c, 3 - c) ** 2 for c in p))
cancel = True
seen = 0
for conf in combinations(range(27), 3):
    occ = set(conf)
    for x in conf:
        for yy in nb[x]:
            if yy in occ:
                continue
            other = tuple(sorted((occ - {x}) | {yy}))
            delta = (field(even, conf, x) + field(even, conf, yy)
                     - field(even, other, yy) - field(even, other, x))
            gap = even[disp(x, yy)] - even[disp(yy, x)]
            cancel = cancel and delta == gap == 0
            seen += 1
check_moves = seen > 0
check(
    "T1b even kernel",
    cancel and check_moves,
    "for every 3-record move the first-order field change equals K(y-x)-K(x-y), which vanishes for an even K",
)

# mean-zero Green function of the 3^3 Laplacian
L = sp.zeros(27)
for i in range(27):
    L[i, i] = 6
    for j in nb[i]:
        L[i, j] -= 1
Ginv = (L + sp.ones(27) / 27).inv() - sp.ones(27) / 27
green = {sites[j]: sp.Rational(Ginv[0, j]) for j in range(27)}
check(
    "T1b Green",
    all(green[p] == green[tuple((-c) % 3 for c in p)] for p in sites)
    and sp.simplify(sum(green.values())) == 0
    and all(sp.simplify((L * sp.Matrix([Ginv[0, j] for j in range(27)]))[i] - (1 if i == 0 else 0) + sp.Rational(1, 27)) == 0
            for i in range(27)),
    "the torus Green function is even, mean zero, and inverts the Laplacian on mean-zero functions",
)

# --- T2: the two clauses ---
def rate(wv, cv, x, yy):
    return sp.sqrt(sp.Rational(wv[x] * wv[yy])) / (cv[x] * cv[yy])


def charges(conf, wv, cv, m, mu):
    occ = set(conf)
    tau = [Fr(0) for _ in range(27)]
    for x in range(27):
        for yy in nb[x]:
            if (x in occ) != (yy in occ):
                bond = rate(wv, cv, x, yy)
                if not bond.is_Rational:
                    raise RuntimeError("crossing rate left the rationals")
                tau[x] += mu * bond / 4
    energy = [(m * wv[x] if x in occ else Fr(0)) + tau[x] for x in range(27)]
    P = sum((energy[x] + 2 * tau[x]) / (8 * cv[x]) for x in range(27))
    Q = sum(energy[x] / (8 * wv[x] * cv[x]) for x in range(27))
    return sp.Rational(P), sp.Rational(Q)


eps = Fr(1, 20)
wv = [Fr(1)] * 27
cv = [Fr(1)] * 27
for z in (0, 1, 3):
    wv[z] = (1 - eps) ** 2
    cv[z] = 1 + eps / 2
PR, QR = charges((0, 1, 3), wv, cv, Fr(1), Fr(0))
PA, QA = charges((0, 1, 3), wv, cv, Fr(1), Fr(1))
lam, scale, wx, wy, cx, cy = sp.symbols("lam scale wx wy cx cy", positive=True)
kap = sp.sqrt(wx * wy) / (cx * cy)
hom = (sp.simplify(kap.subs({wx: lam * wx, wy: lam * wy}) / kap - lam) == 0
       and sp.simplify(kap.subs({cx: scale * cx, cy: scale * cy}) * scale**2 / kap - 1) == 0)
check(
    "T2 opposite charges",
    PR - QR == sp.Rational(-117, 3280) and PA - QA == sp.Rational(3893397, 2555120) and hom,
    f"rest only P-Q={PR - QR}, activity P-Q={PA - QA}",
)

# --- T3: uniform bond count and the weak-field ratio ---
def bonds(conf):
    occ = set(conf)
    return sum(1 for x in conf for yy in nb[x] if yy not in occ)


def ratio(mean_b, n):
    stau = mean_b / 2
    return 1 + 2 * stau / (n + stau)


uniform_ok = True
for n in (2, 3):
    configs = list(combinations(range(27), n))
    mean_b = Fr(sum(bonds(c) for c in configs), len(configs))
    uniform_ok = uniform_ok and mean_b == Fr(6 * n * (27 - n), 26)
check(
    "T3 uniform",
    uniform_ok and ratio(Fr(6 * 2 * 25, 26), 2) == sp.Rational(251, 101)
    and ratio(Fr(6 * 3 * 24, 26), 3) == sp.Rational(121, 49),
    "uniform <B>=6N(V-N)/(V-1); P/Q is 251/101 for two records and 121/49 for three",
)

den = sp.ilcm(*[sp.Rational(green[p]).q for p in sites])
q = Fr(3, 2)
gas_ok = True
gas_txt = []
for n in (2, 3):
    num = Fr(0)
    part = Fr(0)
    for conf in combinations(range(27), n):
        expo = sum(int(sp.Rational(green[disp(a, b)]) * den) for a, b in combinations(conf, 2))
        wt = q ** expo
        part += wt
        num += wt * bonds(conf)
    mean_b = num / part
    rho = ratio(mean_b, n)
    gas_ok = gas_ok and rho > 1 and mean_b < Fr(6 * n * (27 - n), 26)
    gas_txt.append(f"N={n}: <B>={mean_b} P/Q={rho}")
check(
    "T3 clocked gas",
    gas_ok and den == 486,
    "q=3/2 on the exact Green weights, denominator 486; " + "; ".join(gas_txt),
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL on 3^3. The crossing factor balances pi proportional to W for any fixed clocks and lengths, "
        "and an even record-following kernel does not bind a clump at first order. Rest-only and crossing-activity "
        "energies give P-Q = -117/3280 and 3893397/2555120 on the same three records. At weak field the activity "
        "clause has P/Q = 251/101 and 121/49 for the uniform two- and three-record laws, and the clocked-gas law "
        "stays above 1. The 8^3 simulation was not rebuilt. Which clause is the record's energy is open.",
        flush=True,
    )
    print(
        "HIT: confirmed - block 60's derivatives do not fix a record's (e, tau): the two admissible energies "
        "give opposite signs of P-Q, records that cross at sqrt(w_x w_y)/(chi_x chi_y) stay field-blind, "
        "and the activity clause has P/Q > 1 at weak field whenever a record can move.",
        flush=True,
    )
