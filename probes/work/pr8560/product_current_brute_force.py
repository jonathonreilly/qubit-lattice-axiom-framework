#!/usr/bin/env python3
"""J:attack-g:PR8560 - proof step by brute force, on MOBILE_RECORDS_IMMUTABLE_TRANSVERSE_CURL_LIMITS (section 2).

The step attacked: "Averaging the four-site current under the product gives, for every species including 0,
J_a = gamma p_a [e(a) x Y + X x b(a) - 2 X x Y] ... Both rate implementations have the same product current.
In particular sum_a J_a = 0 and J_0 = -2 p_0 Psi", with J_rhoA = (1 - 2 rho_A) Psi, J_rhoB = (1 - 2 rho_B) Psi.
Verified LITERALLY: all 15^4 labellings (l, a, d, r) of a positive-i edge's context, both rates exactly as written
(c = kappa + max(h, 0) and c = K0 + h/2), exact rationals, several random rational products.
Also, as written in section 1-2: the sharp bounds |S_i| <= |gamma|/2, |h_i| <= 2|gamma| and the example attaining
h_3 = 2 gamma; the line identity sum_x h_x = 0 on periodic lines N = 4, 5 (every labelling); and the full fourteen-field
characteristic polynomial lambda^10 (lambda^2 - c^2 |K|^2)^2, c^2 = gamma^2 rho_A rho_B / 3, at orbit-isotropic products.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

import sympy as sp

random.seed(8560)
GAMMA = Fr(3, 2)

# labels: 0 = vacancy; 1..6 = A(+-e_i); 7..14 = B(sigma)
LABELS = [("0", (0, 0, 0), (0, 0, 0))]
for i in range(3):
    for s in (1, -1):
        e = [0, 0, 0]
        e[i] = s
        LABELS.append((f"A{'+' if s > 0 else '-'}e{i + 1}", tuple(e), (0, 0, 0)))
for sg in itertools.product((1, -1), repeat=3):
    LABELS.append(("B" + "".join("+" if v > 0 else "-" for v in sg), (0, 0, 0), sg))
NL = len(LABELS)
E = [lab[1] for lab in LABELS]
B = [lab[2] for lab in LABELS]


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def S(a, d):
    """S(a,d) = (gamma/2)[e(a) x b(d) + e(d) x b(a)] (vector)."""
    c1, c2 = cross(E[a], B[d]), cross(E[d], B[a])
    return tuple(GAMMA / 2 * (c1[k] + c2[k]) for k in range(3))


SS = [[S(a, d) for d in range(NL)] for a in range(NL)]
SI = [[tuple(cross(E[a], B[d])[k] + cross(E[d], B[a])[k] for k in range(3)) for d in range(NL)] for a in range(NL)]


def h(i, l, a, d, r):
    return SS[l][a][i] + SS[a][r][i] - SS[l][d][i] - SS[d][r][i]


def hI(i, l, a, d, r):
    """h in units of gamma/2 (integers): h = (gamma/2) hI."""
    return SI[l][a][i] + SI[a][r][i] - SI[l][d][i] - SI[d][r][i]


FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


# ---- section 1: sharp bounds and the example ----
maxS = abs(GAMMA) / 2 * max(abs(SI[a][d][i]) for a in range(NL) for d in range(NL) for i in range(3))
maxh = abs(GAMMA) / 2 * max(abs(hI(i, *q)) for i in range(3) for q in itertools.product(range(NL), repeat=4))
iB = LABELS.index(next(lab for lab in LABELS if lab[0] == "B+++"))
iAp, iAm = 1, 2
ex = h(2, iB, iAp, iAm, iB)
ok("S1", maxS == abs(GAMMA) / 2 and maxh == 2 * abs(GAMMA) and ex == 2 * GAMMA,
   f"over all 15^2 pairs and 15^4 contexts: max|S_i| = {maxS} = |gamma|/2, max|h_i| = {maxh} = 2|gamma| (gamma = {GAMMA}); "
   f"central A(+e1), A(-e1) with outer B(+,+,+) give h_3 = {ex} = 2 gamma")

rev = all(hI(i, l, d, a, r) == -hI(i, l, a, d, r) for i in range(3) for (l, a, d, r) in itertools.product(range(NL), repeat=4))
ok("S2", rev, "central exchange reverses h for every context and component, so c(eta) - c(eta^edge) = h(eta) for both rates")

line_ok = True
for Nl in (4, 5):
    for i in range(3):
        for conf in itertools.product(range(NL), repeat=Nl):
            if sum(hI(i, conf[(x - 1) % Nl], conf[x], conf[(x + 1) % Nl], conf[(x + 2) % Nl]) for x in range(Nl)) != 0:
                line_ok = False
                break
ok("S3", line_ok, "sum_x h_x = 0 on every labelling of periodic lines N = 4 (15^4) and N = 5 (15^5), all three components")


# ---- section 2: the product current, literally ----
def brute_current(p, rate):
    """J_{s,i} = sum p_l p_a p_d p_r c_i(l,a,d,r) [1(a=s) - 1(d=s)], exact."""
    J = [[Fr(0)] * 3 for _ in range(NL)]
    kappa, K0 = Fr(1, 3), 2 * abs(GAMMA) + 1
    for (l, a, d, r) in itertools.product(range(NL), repeat=4):
        w = p[l] * p[a] * p[d] * p[r]
        if w == 0 or a == d:
            continue
        for i in range(3):
            hh = h(i, l, a, d, r)
            c = kappa + max(hh, 0) if rate == "max" else K0 + hh / 2
            J[a][i] += w * c
            J[d][i] -= w * c
    return J


def formula_current(p):
    X = tuple(sum(p[a] * E[a][k] for a in range(NL)) for k in range(3))
    Y = tuple(sum(p[a] * B[a][k] for a in range(NL)) for k in range(3))
    XY = cross(X, Y)
    out = []
    for a in range(NL):
        t1, t2 = cross(E[a], Y), cross(X, B[a])
        out.append([GAMMA * p[a] * (t1[k] + t2[k] - 2 * XY[k]) for k in range(3)])
    return out, X, Y, tuple(GAMMA * c for c in XY)


good, count = True, 0
for trial in range(3):
    w = [random.randint(1, 9) for _ in range(NL)]
    p = [Fr(v, sum(w)) for v in w]
    F, X, Y, Psi = formula_current(p)
    for rate in ("max", "lin"):
        Jb = brute_current(p, rate)
        good &= all(Jb[a][i] == F[a][i] for a in range(NL) for i in range(3))
        count += 1
    rhoA = sum(p[1:7])
    rhoB = sum(p[7:])
    JA = [sum(F[a][i] for a in range(1, 7)) for i in range(3)]
    JB = [sum(F[a][i] for a in range(7, NL)) for i in range(3)]
    good &= all(sum(F[a][i] for a in range(NL)) == 0 for i in range(3))
    good &= all(F[0][i] == -2 * p[0] * Psi[i] for i in range(3))
    good &= all(JA[i] == (1 - 2 * rhoA) * Psi[i] and JB[i] == (1 - 2 * rhoB) * Psi[i] for i in range(3))
    good &= any(Psi[i] != 0 for i in range(3))
ok("J1", good, f"{count} exact comparisons (3 random rational products, both rates c = kappa + max(h,0) and K0 + h/2, "
   "all 15 species incl. vacancy, 3 directions, 15^4 contexts each): the brute-force current equals "
   "gamma p_a[e(a) x Y + X x b(a) - 2 X x Y]; sum_a J_a = 0, J_0 = -2 p_0 Psi, J_rhoA = (1-2rho_A)Psi, "
   "J_rhoB = (1-2rho_B)Psi, with Psi != 0")


# ---- section 2: the full fourteen-field characteristic polynomial ----
lam = sp.symbols("lambda")
good, rows = True, []
for rhoA, rhoB, K in [(Fr(1, 4), Fr(1, 3), (1, 0, 0)), (Fr(1, 5), Fr(1, 2), (1, 2, 2)), (Fr(3, 10), Fr(2, 5), (2, -1, 3))]:
    p = [1 - rhoA - rhoB] + [rhoA / 6] * 6 + [rhoB / 8] * 8
    # A(K)_{s,t} = d(K . J_s)/d p_t for occupied s, t (p_0 = 1 - sum), exact: J is quadratic in p
    A = sp.zeros(14, 14)
    for s in range(1, NL):
        for t in range(1, NL):
            val = 0
            for i in range(3):
                # derivative of gamma p_s [e(s) x Y + X x b(s) - 2 X x Y]_i in p_t (dp_0/dp_t = -1, e(0) = b(0) = 0)
                X = [sum(p[a] * E[a][k] for a in range(NL)) for k in range(3)]
                Y = [sum(p[a] * B[a][k] for a in range(NL)) for k in range(3)]
                dX, dY = E[t], B[t]
                base = [cross(E[s], Y)[k] + cross(X, B[s])[k] - 2 * cross(X, Y)[k] for k in range(3)]
                dbase = [cross(E[s], dY)[k] + cross(dX, B[s])[k] - 2 * (cross(dX, Y)[k] + cross(X, dY)[k]) for k in range(3)]
                dps = 1 if s == t else 0
                val += K[i] * GAMMA * (dps * base[i] + p[s] * dbase[i])
            A[s - 1, t - 1] = sp.Rational(val.numerator, val.denominator)
    cp = sp.factor(A.charpoly(lam).as_expr())
    K2 = sum(k * k for k in K)
    c2 = sp.Rational(GAMMA ** 2 * rhoA * rhoB / 3)
    target = lam ** 10 * (lam ** 2 - c2 * K2) ** 2
    good &= sp.expand(cp - target) == 0
    rows.append(f"rho_A={rhoA}, rho_B={rhoB}, K={K}: {sp.factor(cp)}")
ok("J2", good, "orbit-isotropic products: det(A(K) - lambda) = lambda^10 (lambda^2 - c^2|K|^2)^2, c^2 = gamma^2 rho_A rho_B/3, "
   "exactly; " + "; ".join(rows))

if FAILS:
    print("SUMMARY: the brute-force check FAILS at " + ", ".join(FAILS) + " (section 1-2 of PR #8560's note)")
    print("HIT: a finite fact stated in the note's section 1-2 fails literal enumeration: " + ", ".join(FAILS))
    sys.exit(0)
print("SUMMARY: pattern applied to section 2's product-current step of PR #8560's transverse-curl note: verified literally "
      "by enumeration (all 15^4 edge contexts, both rate implementations as written, exact rationals, every species "
      "including vacancy) together with section 1's sharp bounds and example, the periodic-line identity, and the "
      "fourteen-field characteristic polynomial; no defect found")
