# GUIDE only: Bessel-ratio facts used in (1), Section 11 and (19).
import math

def ratios(x, kmax):
    # R_k = I_{k+1}(x)/I_k(x), k = 0..kmax-1, by backward recurrence (Miller), stable
    K = kmax + int(2 * x) + 60
    R = 0.0
    out = [0.0] * (K + 1)
    for k in range(K, -1, -1):
        R = 1.0 / (2.0 * (k + 1) / x + R)
        out[k] = R
    return out[:kmax]

def logI(n, x):
    # log I_n(x) by the positive series, log-sum-exp
    kmax = int(x) + 50 + int(10 * math.sqrt(x + 1))
    terms = [(n + 2 * k) * math.log(x / 2) - math.lgamma(k + 1) - math.lgamma(n + k + 1) for k in range(kmax)]
    m = max(terms)
    return m + math.log(sum(math.exp(t - m) for t in terms))

viol = {"a": 0, "b": 0, "c": 0}
worst_c = -1e9
grid = [0.01 * 1.07 ** i for i in range(260)]  # 0.01 .. ~ 4e5? limit below
grid = [s for s in grid if s <= 2000]
for s in grid:
    R = ratios(s, 40)
    for k in range(1, 39):
        x = (k + 0.5) / s
        u = math.sqrt(x * x + 1) - x
        if not R[k] < u:
            viol["a"] += 1
        if not R[k + 1] < R[k]:
            viol["b"] += 1
    prod = 1.0
    for d in range(2, 40):
        prod *= R[d - 1]          # I_d/I_1 = R_1 ... R_{d-1}
        lhs = math.log(prod)
        rhs = -(d - 1) / (1 + s)
        worst_c = max(worst_c, lhs - rhs)
        if lhs > rhs + 1e-12:
            viol["c"] += 1
print("grid points", len(grid), "max s", round(grid[-1], 1), "violations", viol, "max(log(I_d/I_1)+(d-1)/(1+s))", worst_c)

# (1+beta) d_beta on [1, 2000]
vals = []
for b in [1 + 0.05 * i for i in range(200)] + [10 * 1.05 ** i for i in range(100)]:
    if b > 2000:
        break
    r = ratios(b, 2)[1]
    vals.append(((1 + b) * (-math.log(r)), b))
print("(1+beta) d_beta: min %.4f at beta %.2f, max %.4f at beta %.2f" % (min(vals)[0], min(vals)[1], max(vals)[0], max(vals)[1]))

# I(2b)/I(b) with I(b) = e^{-b} (2/b) I_1(b): ratio = (1/2) e^{-b} I_1(2b)/I_1(b)
qs = []
for b in [1 + 0.1 * i for i in range(100)] + [11 * 1.1 ** i for i in range(60)]:
    q = 0.5 * math.exp(-b + logI(1, 2 * b) - logI(1, b))
    qs.append((q, b))
print("sup I(2b)/I(b) on grid: %.5f at beta %.2f; value at largest beta %.2f: %.5f; 2^-1.5 = %.5f" % (max(qs)[0], max(qs)[1], qs[-1][1], qs[-1][0], 2 ** -1.5))

# 1 - r_beta versus 3/(2 beta)
for b in [1, 2.5, 10, 100, 1000]:
    r = ratios(b, 2)[1]
    print("beta", b, "r_beta %.6f" % r, "beta(1-r) %.5f" % (b * (1 - r)))

# (12): (1+x)^2 > 1+x+x^2 and the log identity
for x in [1e-6, 0.1, 0.5, 0.9]:
    lhs = -6 * (math.log(1 - x) + math.log(1 - x ** 3) - 2 * math.log(1 - x ** 2))
    rhs = 6 * math.log((1 + x) ** 2 / (1 + x + x * x))
    print("x", x, "lhs %.12f rhs %.12f" % (lhs, rhs))
print("(9/2)log(4/3) = %.6f ; log(1+1/1650) = %.3e" % (4.5 * math.log(4 / 3), math.log(1 + 1 / 1650)))
