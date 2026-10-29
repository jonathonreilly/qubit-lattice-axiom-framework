# al55_sub.py -- certify C^{1,beta}, beta > 1/2, for L-adic 4-point Deslauriers-Dubuc schemes (ALIGN55.md, input (SUB)).
# Criteria: checks/al55_sub_criteria.md (written first). Fractions/ints only. stdout only.
from fractions import Fraction as F

results = []
def rep(name, ok, info=""):
    results.append((name, ok)); print(("PASS " if ok else "FAIL ") + name + ((" | " + info) if info else ""))
def ctl(name, fired, info=""):
    results.append((name, fired)); print(("CONTROL FIRES " if fired else "CONTROL DOES NOT FIRE ") + name + ((" | " + info) if info else ""))

# Laurent polynomials as dict exponent -> Fraction
def lmul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1+e2] = r.get(e1+e2, F(0)) + c1*c2
    return {e: c for e, c in r.items() if c != 0}
def ldiv_sigma(p, b):
    """divide Laurent p by sigma_b(z) = 1 + ... + z^{b-1}; return (quotient, exact?)"""
    if not p: return {}, True
    lo = min(p); hi = max(p)
    P = [p.get(lo + i, F(0)) for i in range(hi - lo + 1)]   # ascending coefficients
    # long division from the top degree
    P = P[:]; Q = [F(0)] * max(0, len(P) - (b - 1))
    for k in range(len(P) - 1, b - 2, -1):
        coef = P[k]
        if coef != 0:
            Q[k - (b - 1)] = coef
            for t in range(b):
                P[k - t] -= coef
    exact = all(v == 0 for v in P)
    return {lo + i: c for i, c in enumerate(Q) if c != 0}, exact
def subst_pow(p, m):        # p(z^m)
    return {e*m: c for e, c in p.items()}
def norm_iter(c, b, n):
    cn = dict(c)
    for i in range(1, n):
        cn = lmul(cn, subst_pow(c, b**i))
    M = b**n; sums = {}
    for e, v in cn.items():
        r = e % M; sums[r] = sums.get(r, F(0)) + abs(v)
    return max(sums.values())

def dd4_mask(b):
    def w(m, t):
        if m == -1: return -t*(t-1)*(t-2)/6
        if m == 0: return (t+1)*(t-1)*(t-2)/2
        if m == 1: return -(t+1)*t*(t-2)/2
        return (t+1)*t*(t-1)/6
    a = {0: F(1)}
    for r in range(1, b):
        t = F(r, b)
        for m in (-1, 0, 1, 2):
            a[r - b*m] = a.get(r - b*m, F(0)) + w(m, t)
    return {e: c for e, c in a.items() if c != 0}

def sigma_power_divides(a, b, m):
    q = dict(a)
    for _ in range(m):
        q, ex = ldiv_sigma(q, b)
        if not ex: return False, None
    return True, q

def certify(a, b, nmax, label):
    ok2, q2 = sigma_power_divides(a, b, 2)
    if not ok2: return None, "sigma^2 does not divide a"
    c = {e: b*v for e, v in q2.items()}
    best = None
    for n in range(1, nmax + 1):
        nm = norm_iter(c, b, n)
        val = nm*nm*(b**n)
        print("INFO %s n=%d ||S_c^n||_inf=%s  (norm^2 * b^n = %s ~ %s)" % (label, n, nm, val, format(val.numerator/val.denominator, ".6f")))
        if val < 1 and best is None:
            best = (n, nm)
    return best, "ok"

# s3
a3 = {e: F(v, 81) for e, v in zip(range(-5, 6), (-4, -5, 0, 30, 60, 81, 60, 30, 0, -5, -4)) if v != 0}  # run-2 fix: drop zero keys
assert a3 == dd4_mask(3), "mask transcription"
d4, _ = sigma_power_divides(a3, 3, 4); d5, _ = sigma_power_divides(a3, 3, 5)
rep("P1 s3: sigma_3^4 | a and sigma_3^5 does not", d4 and not d5)
best3, msg3 = certify(a3, 3, 7, "s3")
rep("P2 s3 certified C^{1,beta}, beta > 1/2", best3 is not None, "first n = %s, ||S_c^n|| = %s" % (best3[0], best3[1]) if best3 else msg3)
rep("P4a s3 interpolatory", all(a3.get(3*m, F(0)) == (1 if m == 0 else 0) for m in range(-3, 4)))
# s5
a5 = dd4_mask(5)
print("INFO s5 mask (x 15625?):", {e: str(v) for e, v in sorted(a5.items())})
d45, _ = sigma_power_divides(a5, 5, 4)
best5, msg5 = certify(a5, 5, 5, "s5") if d45 else (None, "sigma_5^4 does not divide")
rep("P3 s5: sigma_5^4 | a and certified C^{1,beta}, beta > 1/2 at n <= 5", d45 and best5 is not None,
    ("first n = %s, ||S_c^n|| = %s" % (best5[0], best5[1])) if best5 else msg5)
rep("P4b s5 interpolatory", all(a5.get(5*m, F(0)) == (1 if m == 0 else 0) for m in range(-3, 4)))

# best certified exponent for s3 at the best n found up to 7, against a few rational thresholds (informational)
if best3:
    ok2, q2 = sigma_power_divides(a3, 3, 2); c3 = {e: 3*v for e, v in q2.items()}
    n = 7; nm = norm_iter(c3, 3, n)
    for num, den in ((1, 2), (3, 5), (2, 3), (7, 10), (3, 4), (4, 5)):
        # beta > num/den certified iff nm^den * 3^(n*num) < 1
        print("INFO s3 n=7: beta > %d/%d certified: %s" % (num, den, nm**den * F(3)**(n*num) < 1))

# controls
lin3 = {-2: F(1, 3), -1: F(2, 3), 0: F(1), 1: F(2, 3), 2: F(1, 3)}
okl, ql = sigma_power_divides(lin3, 3, 2)
fired = True
if okl:
    cl = {e: 3*v for e, v in ql.items()}
    for n in range(1, 8):
        nm = norm_iter(cl, 3, n)
        if nm*nm*(3**n) < 1: fired = False
ctl("C1 linear interpolation (C^0) is not certified C^{1,beta} for any n <= 7", fired)
pert = dict(a3); pert[1] = pert[1] + F(1, 81)
okp, _ = sigma_power_divides(pert, 3, 2)
bp = None
if okp: bp, _ = certify(pert, 3, 7, "pert")
ctl("C2 perturbed s3 loses sigma^2-divisibility or certification", (not okp) or bp is None)

print("SUMMARY: %d items, all ok = %s" % (len(results), all(ok for _, ok in results)))
