# sc55_vm.py -- certified rational enclosures of the constants of SRCCD55 Lemma V.
# Criteria: sc55_vm_criteria.md (written first). Exact rational arithmetic only.
from fractions import Fraction as Fr

def exp_enclosure(x, n=40):
    """x > 0 rational: S_n(x) <= e^x <= S_n(x) + x^(n+1)/((n+1)! (1 - x/(n+2)))  (needs x < n+2)."""
    assert 0 < x < n + 2
    s, term = Fr(1), Fr(1)
    for k in range(1, n + 1):
        term = term * x / k
        s += term
    tail = term * x / (n + 1) / (1 - x / (n + 2))
    return s, s + tail

def expneg_enclosure(x):
    lo, hi = exp_enclosure(x)
    return 1 / hi, 1 / lo

def arctan_enclosure(q, terms=30):
    """q in (0,1) rational: alternating series; partial sums bracket arctan(q)."""
    s, sums = Fr(0), []
    for k in range(terms):
        s += (-1) ** k * q ** (2 * k + 1) / (2 * k + 1)
        sums.append(s)
    a, b = sums[-1], sums[-2]
    return min(a, b), max(a, b)

def pi_enclosure():
    a_lo, a_hi = arctan_enclosure(Fr(1, 5))
    b_lo, b_hi = arctan_enclosure(Fr(1, 239))
    return 16 * a_lo - 4 * b_hi, 16 * a_hi - 4 * b_lo

def sqrt_enclosure(lo_sq, hi_sq, steps=60):
    """returns (l, u) with l^2 <= lo_sq and u^2 >= hi_sq (so l <= sqrt(lo_sq) and u >= sqrt(hi_sq))."""
    def low(t):
        a, b = Fr(0), max(Fr(1), t)
        for _ in range(steps):
            m = (a + b) / 2
            if m * m <= t: a = m
            else: b = m
        return a
    def high(t):
        a, b = Fr(0), max(Fr(1), t)
        for _ in range(steps):
            m = (a + b) / 2
            if m * m >= t: b = m
            else: a = m
        return b
    return low(lo_sq), high(hi_sq)

pi_lo, pi_hi = pi_enclosure()
r2_lo, r2_hi = sqrt_enclosure(Fr(2), Fr(2))
rpi_lo, rpi_hi = sqrt_enclosure(pi_lo, pi_hi)
pi32_lo, pi32_hi = pi_lo * rpi_lo, pi_hi * rpi_hi          # pi^{3/2}
e12_lo, e12_hi = expneg_enclosure(Fr(1, 2))
e92_lo, e92_hi = expneg_enclosure(Fr(9, 2))
e5_lo, e5_hi = expneg_enclosure(Fr(5))

PB_lo = 2 * r2_lo * e12_lo / pi32_hi
PB_hi = 2 * r2_hi * e12_hi / pi32_lo
PA_lo = 2 * r2_lo * e92_lo / pi32_hi
PA_hi = 2 * r2_hi * e92_hi / pi32_lo
cv_lo = 8 * e5_lo / pi_hi ** 3
cv_hi = 8 * e5_hi / pi_lo ** 3

def dec(q, d=9):
    return format(q.numerator * 10**d // q.denominator, 'd')

print("pi in [%s, %s] * 1e-9" % (dec(pi_lo), dec(pi_hi)))
print("P_B in [%s, %s] * 1e-9" % (dec(PB_lo), dec(PB_hi)))
print("P_A in [%s, %s] * 1e-9" % (dec(PA_lo), dec(PA_hi)))
print("c_v in [%s, %s] * 1e-9" % (dec(cv_lo), dec(cv_hi)))
print("c_v/1152 in [%s, %s] * 1e-12" % (dec(cv_lo / 1152, 12), dec(cv_hi / 1152, 12)))

V1 = PB_lo >= Fr(3, 10)
V2 = PA_lo >= Fr(56, 10000)
V3 = cv_lo >= Fr(17, 10000) and PA_lo * PB_lo >= Fr(17, 10000)
V4 = cv_lo / 1152 >= Fr(15, 10**7)
V5a = all(Fr(3) / (2 * k) - Fr(2) / (3 * k * k) - 1 / k == (3 * k - 4) / (6 * k * k)
          for k in [Fr(j, 7) for j in range(1, 201)])
V5b = 4 * (1 - Fr(2) / (3 * 4)) ** 2 >= Fr(27, 10)
C_fired = cv_hi < Fr(18, 10000)
for name, ok in [("V1 P_B >= 3/10", V1), ("V2 P_A >= 56/10000", V2), ("V3 c_v >= 17/10000", V3),
                 ("V4 c_v/1152 >= 1.5e-6", V4), ("V5a gap algebra (3k-4)/(6k^2)", V5a),
                 ("V5b 4(1-2/(3*4))^2 >= 2.7", V5b)]:
    print(name, "PASS" if ok else "FAIL")
print("C control (false claim c_v >= 18/10000 rejected):", "FIRED" if C_fired else "DID NOT FIRE")
print("VERDICT:", "PASS" if all([V1, V2, V3, V4, V5a, V5b, C_fired]) else "FAIL")
