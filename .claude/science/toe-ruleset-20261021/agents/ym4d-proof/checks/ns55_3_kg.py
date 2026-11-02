"""ns55_3 -- rational brackets for the Lemma B majorant constant K_G (NSL55 §3.2, §7 E4).

Criteria: checks/ns55_3_criteria.md (written before this file). Exact Fractions only; no floats in any verdict.
"""
from fractions import Fraction as Fr
from math import factorial


def exp_bracket(q, N=40):
    """[lo, hi] with lo <= e^q <= hi, rational q >= 0."""
    assert q >= 0
    s = sum(q**n / factorial(n) for n in range(N + 1))
    ratio = q / (N + 2)
    assert ratio < 1
    tail = q**(N + 1) / factorial(N + 1) / (1 - ratio)
    return s, s + tail


def log_bracket(w, N=81):
    """[lo, hi] with lo <= log(w) <= hi, rational w > 1 (artanh series)."""
    assert w > 1
    t = (w - 1) / (w + 1)
    s = 2 * sum(t**n / n for n in range(1, N + 1, 2))
    tail = 2 * t**(N + 2) / ((N + 2) * (1 - t * t))
    return s, s + tail


def neglog_bracket(z_lo, z_hi):
    """bracket of -log z for z in [z_lo, z_hi] subset (0, 1)."""
    assert 0 < z_lo <= z_hi < 1
    lo, _ = log_bracket(1 / z_hi)      # -log z >= -log z_hi = log(1/z_hi)
    _, hi = log_bracket(1 / z_lo)      # -log z <= log(1/z_lo)
    return lo, hi


def m_bracket(R):
    """bracket of m(R) = -log(2 - e^{4R}) + 2R, or None if 2 - e^{4R} <= 0 cannot be excluded."""
    eL, eU = exp_bracket(4 * R)
    z_lo, z_hi = 2 - eU, 2 - eL
    if z_lo <= 0:
        return None
    lo, hi = neglog_bracket(z_lo, z_hi)
    return lo + 2 * R, hi + 2 * R


# K1: control -- undefined at R = 9/50
K1 = m_bracket(Fr(9, 50)) is None

m20 = m_bracket(Fr(1, 20))
m10 = m_bracket(Fr(1, 10))
K2 = (m20[1] - m20[0] < Fr(1, 10**6)) and (m10[1] - m10[0] < Fr(1, 10**6))

# K3: log(e^{1/2}) contains 1/2
eL, eU = exp_bracket(Fr(1, 2))
lL, _ = log_bracket(eL)
_, lU = log_bracket(eU)
K3 = lL <= Fr(1, 2) <= lU

draft_lo = 16 * max(400 * m20[0], 200 * m10[0])
fixed_hi = 8 * max(400 * m20[1], 200 * m10[1])
A = draft_lo > 1500
B = fixed_hi < 1500

print("m(1/20) in [%.9f, %.9f]   (display only)" % (float(m20[0]), float(m20[1])))
print("m(1/10) in [%.9f, %.9f]   (display only)" % (float(m10[0]), float(m10[1])))
print("draft formula 2*C_alg*max(400 m(1/20), 200 m(1/10)) >= %.3f   (display only)" % float(draft_lo))
print("re-derived    C_alg*max(400 m(1/20), 200 m(1/10))   <= %.3f   (display only)" % float(fixed_hi))
print(f"K1(undefined at R=9/50)={K1} K2(brackets tight)={K2} K3(exp/log consistent)={K3} A(draft>1500)={A} B(fixed<1500)={B}")
print("OVERALL:", "PASS" if (K1 and K2 and K3 and A and B) else "FAIL")
