"""w6 Part N: the negative control HW §29 l.1462-1464 promised for check (ii) and never ran
(REVIEW_HW_S5 S5-25, scope defect 1): the two-species toy at activities ABOVE the stated threshold, 2z^2 >= 1.
Same model as w5_criteria.md Part C, but in EXACT Fraction arithmetic (no numpy, no floats, no BLAS -> no lock).
Criteria: checks/w6_criteria.md (written before this script).  Informational, never a proof."""
import itertools
import time
from fractions import Fraction as F

t0 = time.time()
n0, n1 = 12, 4

# ---- group the 2^12 level-0 configurations by (ok0, k0, dirty pattern) ----
classes = {}
for cfg in itertools.product((0, 1), repeat=n0):
    ok0 = all(not (cfg[i] and cfg[(i + 1) % n0]) for i in range(n0))   # no adjacent level-0 defects (ring)
    if not ok0:
        continue                                                        # configurations outside R contribute to neither Z
    k0 = sum(cfg)
    dirty = tuple(1 if max(cfg[3 * X:3 * X + 3]) else 0 for X in range(n1))
    classes[(k0, dirty)] = classes.get((k0, dirty), 0) + 1
XIS = list(itertools.product((0, 1, 2), repeat=n1))
ADJ = [(X, (X + 1) % n1) for X in range(n1)]


def ratio_exact(p, q, qp):
    """Z(R^-B)/Z(R), exact."""
    num = F(0)
    den = F(0)
    pr = (q, qp - q, 1 - qp)
    for (k0, dirty), mult in classes.items():
        w0 = F(mult) * p ** k0 * (1 - p) ** (n0 - k0)
        for xis in XIS:
            w = w0
            for X in range(n1):
                w *= pr[xis[X]]
            if w == 0:
                continue
            D1 = [1 if (xis[X] == 0 or (xis[X] == 1 and dirty[X])) else 0 for X in range(n1)]
            full = any(D1[X] and D1[Z] for (X, Z) in ADJ)
            relB = any(D1[X] and D1[Z] for (X, Z) in ADJ if X != 0 and Z != 0)
            if not relB:
                num += w
                if not full:
                    den += w
    return num / den


GRID = [('0.3', '0.5', '0.95'), ('0.9', '0.5', '0.99'), ('0.3', '0.4', '0.9'),
        ('0.1', '0.6', '0.99'), ('0.02', '0.707', '0.707'), ('0.3', '0.1', '0.9')]
above = []
below = []
print("N: the never-run negative control: the two-species bound rho <= 1/(1 - 2z^2) at activities above the threshold")
print("   z := q + (1 - (1-p)^3)(q' - q) ; exact enumeration of the 2^12 * 3^4 configurations in Fraction arithmetic")
for ps, qs, qps in GRID:
    p, q, qp = F(ps), F(qs), F(qps)
    z = q + (1 - (1 - p) ** 3) * (qp - q)
    twoz2 = 2 * z * z
    r = ratio_exact(p, q, qp)
    bound = None if twoz2 >= 1 else 1 / (1 - twoz2)
    print("   p=%-5s q=%-6s q'=%-6s : z=%.6f  2z^2=%.6f  exact ratio=%.6f  bound=%s"
          % (ps, qs, qps, float(z), float(twoz2), float(r),
             "VACUOUS (1 - 2z^2 = %.6f <= 0)" % float(1 - twoz2) if bound is None else "%.6f" % float(bound)))
    (above if twoz2 >= 1 else below).append((float(twoz2), float(r), None if bound is None else float(bound)))

n1ok = len(above) >= 3 and all(b is None and r == r and r < float('inf') for (_, r, b) in above)
n2ok = len(below) >= 1 and all(b is not None and r <= b * (1 + 1e-12) for (_, r, b) in below)
print("   N1: %d points with 2z^2 >= 1; at every one the bound is VACUOUS (1 - 2z^2 <= 0) while the exact ratio is finite"
      " (max %.6f): %s" % (len(above), max(r for (_, r, _) in above), "PASS" if n1ok else "FAIL"))
print("   N2: %d points with 2z^2 < 1 (nearest to the threshold 2z^2 = %.6f, ratio %.6f, bound %.6f); the exact ratio stays"
      " bounded and satisfies the bound: %s"
      % (len(below), max(t for (t, _, _) in below),
         [r for (t, r, _) in below if t == max(x[0] for x in below)][0],
         [b for (t, _, b) in below if t == max(x[0] for x in below)][0], "PASS" if n2ok else "FAIL"))
print("RESULTS: N1:%s N2:%s" % ("PASS" if n1ok else "FAIL", "PASS" if n2ok else "FAIL"))
print("OVERALL N " + ("PASS" if (n1ok and n2ok) else "FAIL"))
print("secs %.1f" % (time.time() - t0))
