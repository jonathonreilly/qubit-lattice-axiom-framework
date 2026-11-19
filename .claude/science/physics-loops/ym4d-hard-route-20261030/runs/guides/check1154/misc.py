# GUIDE only (pure Python). (a) larger-m box mode sums; (b) scalar subgroup
# example; (c) Bessel ratios a_beta(d); (d) vMF radial mean on S^3;
# (e) Monte Carlo test of the Gaussian product inequality (17) in R^2.
import math, random, sys

def f(x):
    return math.log((1 + math.exp(-x)) / (1 - math.exp(-x)))

def box_sum(bs, m):
    tot = 0.0
    s = [[4 * math.sin(math.pi * q / (2 * b))**2 for q in range(b)] for b in bs]
    for q1 in range(bs[0]):
        for q2 in range(bs[1]):
            l12 = s[0][q1] + s[1][q2]
            r12 = (q1 > 0) + (q2 > 0)
            for q3 in range(bs[2]):
                rq = r12 + (q3 > 0)
                if rq < 2:
                    continue
                x = 2 * m * math.asinh(math.sqrt(l12 + s[2][q3]) / 2)
                if x > 40:
                    continue
                tot += (rq - 1) * f(x)
    return m**3 / (bs[0] * bs[1] * bs[2]) * 3 * tot

print("pi^2/8 =", math.pi**2 / 8)
for m in (12, 16):
    b = 15 * m
    print("m", m, "box", (b, b + 1, b), "normalized sum", box_sum((b, b + 1, b), m)); sys.stdout.flush()

# (b) scalar subgroup example: beta=1e4, b=25, d=beta^-1/2
beta = 1e4; b = 25; d = beta ** -0.5
Ew1 = math.cos(d)
ok = True
for k in range(1, b + 1):
    Ewk = (1 / (8 * b)) * math.cos(k * d) + (1 - 1 / (8 * b)) * (math.cos(d) if k % 2 else 1.0)
    if Ewk < Ew1 ** k - 1e-15:
        ok = False; print("FAIL at k", k)
    Eqk2 = 2 * (1 - Ewk)
    if Eqk2 > 2 * k / beta:
        print("strip mean square exceeds 2k/beta at k", k)
qb4 = (1 / (8 * b)) * (2 - 2 * math.cos(b * d)) ** 2
print("scalar example: E w_k >= (E w_1)^k for all k<=b:", ok, "; E q_b^4 =", qb4, " b^3/beta^2 =", b**3 / beta**2, " ratio =", qb4 / (b**3 / beta**2))

# (c) a_beta(d) = I_d(beta)/I_1(beta) via the angle integral (SU(2) Haar angle density)
def a_beta(beta, dd, N=20000):
    num = den = 0.0
    for i in range(1, N):
        r = math.pi * i / N
        w = math.exp(-beta * (1 - math.cos(r))) * math.sin(r) ** 2
        num += w * math.sin(dd * r) / (dd * math.sin(r)); den += w
    return num / den
for beta in (100.0, 400.0):
    c1 = 0.5
    dmax = int(c1 * math.sqrt(beta))
    print("beta", beta, " a_beta(d) at d=", dmax, ":", a_beta(beta, dmax), " (claim >= 1/2 for d <= c1 sqrt beta)")

# (d) vMF on S^3 with concentration k: radial mean A(k) = E cos r, density e^{k cos r} sin^2 r
def A(k, N=200000):
    num = den = 0.0
    for i in range(1, N):
        r = math.pi * i / N
        w = math.exp(k * (math.cos(r) - 1)) * math.sin(r) ** 2
        num += w * math.cos(r); den += w
    return num / den
for beta in (50.0, 500.0):
    print("beta", beta, " beta*(1 - A(6 beta)) =", beta * (1 - A(6 * beta)), " (claim >= c > 0)")

# (e) Gaussian product inequality (17) in R^2: six unit rows at angles k pi/6,
# sum L*L = 3 I, so sum L*L/6 = I/2 <= I. Test E prod f_p(L_p Z) <= prod (E f_p^6)^(1/6).
random.seed(1)
angles = [k * math.pi / 6 for k in range(6)]
fs = [lambda x, s=s: math.exp(0.3 * math.tanh(x + s)) for s in (0.0, 0.5, -0.7, 1.1, -0.2, 0.3)]
M = 400000
lhs = 0.0
mom = [0.0] * 6
for _ in range(M):
    z1 = random.gauss(0, 1); z2 = random.gauss(0, 1)
    prod = 1.0
    for k, th in enumerate(angles):
        prod *= fs[k](math.cos(th) * z1 + math.sin(th) * z2)
    lhs += prod
    for k in range(6):
        mom[k] += fs[k](z1) ** 6
lhs /= M
rhs = 1.0
for k in range(6):
    rhs *= (mom[k] / M) ** (1 / 6)
print("BL test: E prod =", lhs, " prod (E f^6)^(1/6) =", rhs, " holds:", lhs <= rhs)
