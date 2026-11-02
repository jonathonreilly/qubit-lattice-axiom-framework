"""hi55_b -- arithmetic of Theorems H-RED and H-RED-sharp (criteria: hi55_b_criteria.md, written first).

Exact rationals only. ell stands for log L; every tested statement holds for every ell > 0.
"""
from fractions import Fraction as Fr
import math
import random

rng = random.Random(5502)


def rfrac(lo_num, hi_num, den_hi=9):
    return Fr(rng.randint(lo_num, hi_num), rng.randint(1, den_hi))


def ceil_frac(x):
    # exact ceiling of a Fraction
    n, d = x.numerator, x.denominator
    return -((-n) // d)


# ---------------------------------------------------------------- B1
def threshold_m1(u0, cm, Cp, bm, R, ell, theta_half):
    X = 2 * Cp * u0 / cm
    target = X * X if theta_half else X           # need u0 + bm*m*ell - R >= target
    need = (target - u0 + R) / (bm * ell)
    m1 = max(0, ceil_frac(need))
    # verify minimality exactly
    def ok(m):
        return u0 + bm * m * ell - R >= target
    assert ok(m1)
    if m1 > 0:
        assert not ok(m1 - 1)
    return m1


def f_up_le(Cp, um, bound, theta_half):
    # is Cp * um^(theta-1) <= bound ?  theta in {0, 1/2}; um > 0, bound > 0
    if theta_half:
        return Cp * Cp <= bound * bound * um       # Cp/sqrt(um) <= bound
    return Cp <= bound * um                        # Cp/um <= bound


b1_viol = 0
b1_sets = 0
b1f_sets = 0
b1f_fail_ok = 0
b1f_bad = 0
for it in range(300):
    cm = Fr(rng.randint(1, 50), rng.randint(1, 50))
    ratio_exp = rng.randint(0, 6)
    Cp = cm * (1 + Fr(rng.randint(0, 10 ** ratio_exp), rng.randint(1, 9)))
    bm = Fr(rng.randint(1, 40), rng.randint(1, 40))
    R = Fr(rng.randint(0, 30), rng.randint(1, 5))
    u0 = 1 + R + Fr(rng.randint(0, 200), rng.randint(1, 7))
    ell = rng.choice([Fr(10986, 10000), Fr(16094, 10000), Fr(rng.randint(1, 30), rng.randint(1, 10))])
    theta_half = (it % 2 == 1)
    m1 = threshold_m1(u0, cm, Cp, bm, R, ell, theta_half)
    bound = cm / (2 * u0)
    f0 = cm / u0
    zero_slack = (it % 3 == 0)
    b1_sets += 1
    for m in range(m1, m1 + 41):
        slack = Fr(0) if zero_slack else Fr(rng.randint(0, 100), rng.randint(1, 9))
        um = u0 + bm * m * ell - R + slack
        assert um > 0
        if not f_up_le(Cp, um, bound, theta_half):
            b1_viol += 1
        # W >= cm/(2 u0) follows from f_m <= bound and f0 = cm/u0 (exact)
        # (checked implicitly: W = f0 - f_m >= f0 - bound = cm/(2u0))
    if zero_slack and m1 >= 1:
        b1f_sets += 1
        m = m1 - 1
        um = u0 + bm * m * ell - R
        if um > 0 and not f_up_le(Cp, um, bound, theta_half):
            b1f_fail_ok += 1
        elif um <= 0:
            b1f_fail_ok += 1          # (F_R) floor non-positive: the bound is vacuous there, i.e. fails
        else:
            b1f_bad += 1

print('B1 sets', b1_sets, 'violations', b1_viol)
print('B1-F zero-slack sets with m1>=1:', b1f_sets, 'failed as required:', b1f_fail_ok, 'unexpected passes:', b1f_bad)
B1 = (b1_viol == 0)
B1F = (b1f_sets >= 50 and b1f_bad == 0 and b1f_fail_ok == b1f_sets)

# ---------------------------------------------------------------- B2
b2_sets = 0
b2_viol = 0
b2_notmin = 0
b2f_sets = 0
b2f_bad = 0
for it in range(300):
    A = Fr(rng.randint(1, 60), rng.randint(1, 60))
    bm = Fr(rng.randint(1, 40), rng.randint(1, 40))
    R = Fr(rng.randint(0, 30), rng.randint(1, 5))
    C = Fr(rng.randint(0, 30), rng.randint(1, 5))
    ell = rng.choice([Fr(10986, 10000), Fr(rng.randint(1, 30), rng.randint(1, 10))])
    # Delta0 = least integer Delta with bm*Delta*ell > R + 2C
    q = (R + 2 * C) / (bm * ell)
    D0 = math.floor(q) + 1
    assert bm * D0 * ell > R + 2 * C and not (bm * (D0 - 1) * ell > R + 2 * C)
    u1 = bm * (D0 + 5) * ell + 2 * C + 1 + Fr(rng.randint(0, 100), rng.randint(1, 7)) + R
    for Dl in (D0, D0 + 1, D0 + 5):
        u2 = u1 - bm * Dl * ell + R          # slowest running allowed by (F_R)
        assert u2 > C
        b2_sets += 1
        v1, v2 = u1 - C, u2 + C
        W = A * (1 / v2 - 1 / v1)
        bound = A * (bm * Dl * ell - R - 2 * C) / ((u1 + C) * (u2 + C))
        if not (W >= bound and bound > 0):
            b2_viol += 1
        corners = [A * (1 / w2 - 1 / w1) for w1 in (u1 - C, u1 + C) for w2 in (u2 - C, u2 + C)]
        if W != min(corners):
            b2_notmin += 1
    if D0 - 1 >= 1:
        b2f_sets += 1
        Dl = D0 - 1
        u2 = u1 - bm * Dl * ell + R
        v1, v2 = u1 - C, u2 + C
        W = A * (1 / v2 - 1 / v1)
        if not (W <= 0):
            b2f_bad += 1

print('B2 checks', b2_sets, 'violations', b2_viol, 'adversarial corner not minimal', b2_notmin)
print('B2-F sets with Delta0-1>=1:', b2f_sets, 'unexpected W>0:', b2f_bad)
B2 = (b2_viol == 0 and b2_notmin == 0)
B2F = (b2f_sets >= 50 and b2f_bad == 0)

print('B1', 'PASS' if B1 else 'FAIL', '| B1-F', 'behaves' if B1F else 'DOES NOT behave')
print('B2', 'PASS' if B2 else 'FAIL', '| B2-F', 'behaves' if B2F else 'DOES NOT behave')
print('VERDICT', 'PASS' if (B1 and B1F and B2 and B2F) else 'FAIL')
