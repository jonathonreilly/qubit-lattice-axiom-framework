"""hi55_c -- lattice free Maxwell field under the lattice heat (Wilson) flow; INFORMATIONAL
(criteria: hi55_c_criteria.md, written first). Rigorous rational enclosures, fractions only.

F_lat(tau) := tau^2 * B(4 tau)^4,  B(x) := e^{-x} I_0(x);  tau^2 <E_lat(tau)> = (3/2) F_lat(tau) per colour, unit coupling.
"""
from fractions import Fraction as Fr


def exp_encl(x):
    """[lo, hi] with lo <= e^x <= hi, x >= 0 rational."""
    K = max(int(4 * x) + 10, 60)
    term = Fr(1)
    s = Fr(1)
    for n in range(1, K + 1):
        term = term * x / n
        s += term
    # for n >= K: ratio x/(n+1) <= 1/2 since K + 1 >= 2x; tail <= term_K
    assert x / (K + 1) <= Fr(1, 2)
    return s, s + term


def I0_encl(x):
    K = max(int(4 * x) + 10, 60)
    h2 = (x / 2) ** 2
    term = Fr(1)
    s = Fr(1)
    for k in range(1, K + 1):
        term = term * h2 / (k * k)
        s += term
    assert h2 / ((K + 1) ** 2) <= Fr(1, 2)
    return s, s + term


def F_encl(tau):
    x = 4 * tau
    elo, ehi = exp_encl(x)
    ilo, ihi = I0_encl(x)
    blo = ilo / ehi
    bhi = ihi / elo
    return tau * tau * blo ** 4, tau * tau * bhi ** 4


PI2_LO = Fr(98696044010, 10 ** 10)
PI2_HI = Fr(98696044011, 10 ** 10)

big = [Fr(1), Fr(2), Fr(4), Fr(8), Fr(16), Fr(32), Fr(64)]
small = [Fr(1, 32), Fr(1, 16), Fr(1, 8)]
enc = {t: F_encl(t) for t in big + small}

for t in small + big:
    lo, hi = enc[t]
    print('tau', t, 'F_lat in [%.12e, %.12e]' % (float(lo), float(hi)), ' 64pi^2 F - 1 ~ %.6e' % (float(64 * PI2_LO * lo) - 1))

C1 = all(enc[big[i + 1]][1] < enc[big[i]][0] for i in range(len(big) - 1))
C2 = all(enc[small[i + 1]][0] > enc[small[i]][1] for i in range(len(small) - 1))
C3 = True
for t in (Fr(32), Fr(64)):
    lo, hi = enc[t]
    low_ok = 64 * PI2_LO * lo - 1 >= Fr(1, 16) / t
    high_ok = 64 * PI2_HI * hi - 1 <= Fr(1, 4) / t
    C3 = C3 and low_ok and high_ok
print('C1 (decreasing, tau >= 1):', 'PASS' if C1 else 'FAIL')
print('C2 (increasing, tau <= 1/8):', 'PASS' if C2 else 'FAIL')
print('C3 (64 pi^2 F - 1 in [1/(16 tau), 1/(4 tau)] at tau = 32, 64):', 'PASS' if C3 else 'FAIL')
print('note: floats above are display only; verdicts use exact enclosures')
