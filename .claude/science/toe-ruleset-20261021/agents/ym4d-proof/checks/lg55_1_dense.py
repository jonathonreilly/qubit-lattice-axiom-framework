# lg55_1 -- exact rational check of Theorem DENSE's density condition (LARGE55 section 2.1).
# Criteria: lg55_1_criteria.md (written before this script). Exact arithmetic only (fractions.Fraction).
from fractions import Fraction as F
import sys

NS = [2, 3, 4, 5, 6, 8, 10]
GRID = [F(k, 1000) for k in range(1, 683)]

def A(N, e):
    return F(24, N) * (1 + e * e) ** 2 + 6 * e

def beta_up(N):
    return F(11 * N * N, 1) / (12 * F(333, 106) ** 2)

def beta_lo(N):
    return F(11 * N * N, 1) / (12 * F(355, 113) ** 2)

def cond(N, e, beta):
    return e * e * A(N, e) * beta < 4

def eps_lo(N, beta):
    last = None
    for e in GRID:
        if cond(N, e, beta):
            last = e
        else:
            break
    return last

def eps_hi(N):
    for e in GRID:
        if not cond(N, e, beta_lo(N)):
            return e
    return None

out = []
ok = True
# feasibility of the construction on the whole grid
feas = all(e + e ** 3 <= 1 for e in GRID)
out.append("feasibility eps+eps^3<=1 on grid: %s (max grid eps = %s)" % (feas, GRID[-1]))
ok = ok and feas

mono_all = True
lo_vals = {}
for N in NS:
    vals = [e * e * A(N, e) for e in GRID]
    mono = all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))
    mono_all = mono_all and mono
    lo = eps_lo(N, beta_up(N))
    lo11 = eps_lo(N, beta_up(N) * F(11, 10))
    hi = eps_hi(N)
    lo_vals[N] = lo
    out.append("N=%d: monotone=%s eps_lo(beta_up)=%s eps_lo(1.1*beta_up)=%s eps_hi(beta_lo)=%s" %
               (N, mono, lo, lo11, hi))

P1 = lo_vals[2] is not None and F(600, 1000) <= lo_vals[2] <= F(640, 1000)
P2 = lo_vals[3] is not None and F(500, 1000) <= lo_vals[3] <= F(560, 1000)
P3 = mono_all
P4 = all(lo_vals[NS[i]] >= lo_vals[NS[i + 1]] for i in range(len(NS) - 1))
C1 = not cond(2, F(682, 1000), beta_lo(2))
C2 = cond(10, F(1, 1000), beta_up(10))
out.append("P1 (eps_lo(2) in [0.600,0.640]): %s" % ("PASS" if P1 else "FAIL"))
out.append("P2 (eps_lo(3) in [0.500,0.560]): %s" % ("PASS" if P2 else "FAIL"))
out.append("P3 (monotone for every N): %s" % ("PASS" if P3 else "FAIL"))
out.append("P4 (eps_lo non-increasing in N): %s" % ("PASS" if P4 else "FAIL"))
out.append("C1 (control: condition FAILS at eps=0.682, N=2, beta_lo): %s" % ("PASS" if C1 else "FAIL"))
out.append("C2 (control: condition holds at eps=0.001, N=10, beta_up): %s" % ("PASS" if C2 else "FAIL"))

# report-only: lane's eps_1 = 6.7e-40
e1 = F(67, 10 ** 41)
rep = all(cond(N, e1, beta_up(N) * F(11, 10)) for N in NS)
out.append("report: lane eps_1=6.7e-40 satisfies C (with 1.1*beta_up) for all N listed: %s" % rep)
# report the exact margin value at N=2 threshold grid point
N = 2
e = lo_vals[2]
out.append("report: at N=2, eps=%s: eps^2*A*beta_up = %s ~ %.6f (display only)" %
           (e, e * e * A(2, e) * beta_up(2), float(e * e * A(2, e) * beta_up(2))))
ok = ok and P1 and P2 and P3 and P4 and C1 and C2
out.append("OVERALL: %s" % ("PASS" if ok else "FAIL"))
print("\n".join(out))
