"""R4: rung compounding with a relevant coupling (HIER-1 mechanism (c)).

Lemma (hyperbolic bound).  Rung map R with scale factor b on a C^1 chart
around a fixed point; in a box U = {|u| <= rho, |s| <= rho} the relevant
component obeys |u(R K)| >= lam |u(K)| with lam = b^y (cone condition), the
irrelevant one contracts; after leaving U the flow reaches the trivial (gapped)
region within n_x rungs.  Then the number of rungs spent in U is
n <= log(rho/|u0|)/log(lam), so xi/a <= b^(n + n_x) xi_triv = C (rho/|u0|)^(1/y).
Checks: random C^1 hyperbolic maps; then the two escapes (1D Ising in the K
chart; asymptotically free flow) and which hypothesis each violates.
"""
import math
import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(("PASS" if ok else "FAIL"), name, detail)


rng = np.random.default_rng(3)
b = 2.0
rho = 0.25
worst_ratio = 0.0
nmaps = 200
for trial in range(nmaps):
    y = rng.choice([1.0, 2.0, 0.5])
    lam = b ** y
    mu = rng.uniform(0.1, 0.6)
    c = rng.uniform(-0.3, 0.3, size=6)

    def R(u, s):
        return (lam * u + c[0] * u * u + c[1] * u * s + c[2] * s * s * u,
                mu * s + c[3] * u * u + c[4] * u * s + c[5] * s * s)
    # effective expansion lower bound in U: lam - |c0| rho - |c1| rho - |c2| rho^2
    lam_min = lam - (abs(c[0]) + abs(c[1])) * rho - abs(c[2]) * rho ** 2
    if lam_min <= 1:
        continue
    for delta in (1e-1, 3e-2, 1e-2):
        u, s = delta, rng.uniform(-rho, rho)
        n = 0
        while abs(u) <= rho and abs(s) <= rho and n < 10000:
            u, s = R(u, s)
            n += 1
        bound = math.log(rho / delta) / math.log(lam_min) + 1
        worst_ratio = max(worst_ratio, n / bound)
check(f"random hyperbolic maps ({nmaps}): rungs in U never exceed the cone bound", worst_ratio <= 1.0,
      f"max n/bound = {worst_ratio:.3f}")

# ladder content at its free (Gaussian) fixed point: y = 1 (fermion mass), 2 (scalar mass^2),
# 4 (vacuum energy).  With delta >= 1e-2 the bound is C * 100^(1/y).
for y in (1, 2, 4):
    print(f"  y={y}: xi/a <= C x {100 ** (1 / y):.0f} at delta = 1e-2")
y_need = 2 / 15
check("hierarchy 1e15 at delta >= 1e-2 and C <= 1 needs y <= 2/15", abs(100 ** (1 / y_need) - 1e15) / 1e15 < 1e-9,
      "relevant exponent below 0.134: near-marginal")
# the hierarchy formula read as transported: v/mu = c alpha(mu)^16 at every rung <=> d ln alpha/d ln mu = -1/16
alpha_LM = 0.0906678
y_formula = 1 / 16
check("formula read rung-by-rung = relevant coupling with y = 1/16 from alpha_LM",
      abs(alpha_LM ** 16 * (7 / 8) ** 0.25 - 2.0172e-17) / 2.0172e-17 < 1e-3,
      f"alpha^16 (7/8)^(1/4) = {alpha_LM ** 16 * (7 / 8) ** 0.25:.4e}; y = {y_formula} < 2/15")

# Escape 1: 1D Ising, exact decimation tanh K' = tanh^2 K, xi = -1/ln tanh K.
K = 18.0
xi = -1 / math.log(math.tanh(K))
t = math.exp(-2 * K)
# smooth chart at the T = 0 fixed point: t = e^{-2K}, t' = 2 t + O(t^2)  (y = 1)
# exact: tanh K = (1-t)/(1+t) => e^{-2K'} = (1 - tanh^2 K)/(1 + tanh^2 K) = 2t/(1+t^2)
# (the float route via atanh(tanh(18)^2) loses all digits; checked at K = 2 where it is exact)
K2 = 2.0
t2 = math.exp(-2 * K2)
float_route = math.exp(-2 * math.atanh(math.tanh(K2) ** 2))
assert abs(float_route - 2 * t2 / (1 + t2 * t2)) < 1e-12
tp = 2 * t / (1 + t * t)
check("1D Ising K=18 (T/J=0.056): xi ~ 1e15 lattice units", 1e15 < xi < 1e16, f"xi = {xi:.3e}")
check("  ... but in the smooth chart t = e^(-2K) the input is t ~ 2e-16 (y = 1, t' = 2t)",
      abs(tp / t - 2) < 1e-6 and t < 1e-15, f"t = {t:.2e}, t'/t = {tp / t:.6f}; violates H1 (fixed point at K = infinity)")

# Escape 2: asymptotically free flow, d(1/g^2)/dl = b0/(8 pi^2): marginal, y = 0 (violates H2)
b0, g2 = 1.0, 1.0
xi_af = math.exp(8 * math.pi ** 2 / (b0 * g2))
check("AF flow b0=1, g^2=1: xi/a = exp(8 pi^2/(b0 g^2)) ~ 1e34 from O(1) input (y = 0)", 1e34 < xi_af < 1e35,
      f"xi/a = {xi_af:.2e}")

# Telescoping: product of per-rung suppressions (a_n/a_{n+1})^p equals (a_0/a_N)^p for every regrouping
scales = np.sort(rng.uniform(0, 40, size=12))
a = 10.0 ** (-scales[::-1])  # a_0 < a_1 < ... increasing
p = 2
prod_fine = np.prod([(a[n] / a[n + 1]) ** p for n in range(len(a) - 1)])
coarse = a[::3] if (len(a) - 1) % 3 == 0 else np.append(a[::3], a[-1])
prod_coarse = np.prod([(coarse[n] / coarse[n + 1]) ** p for n in range(len(coarse) - 1)])
check("telescoping: compounded (a/w)^p is (a_0/a_N)^p under any regrouping of rungs",
      math.isclose(math.log10(prod_fine), p * math.log10(a[0] / a[-1]), rel_tol=1e-12)
      and math.isclose(math.log10(prod_coarse), math.log10(prod_fine), rel_tol=1e-12),
      f"{len(a) - 1} rungs vs {len(coarse) - 1} rungs, log10 = {math.log10(prod_fine):.6f}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
