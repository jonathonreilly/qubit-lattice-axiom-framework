"""R15-6 step 6b: is there a LINEAR fading-memory reader (y_j' = E - beta_j y_j, R = sum k_j y_j), exact on dust and
radiation (G(3) = G(4) = 1), with g <= 0 after EVERY drop into the dust or radiation sector?
Re-derived (r156_linear docstring): after a step release Delta into sector x, e = R - rho_nc = -Delta sum_j a_j e^{-beta_j tau},
a_j = k_j x/(beta_j - x) (uses G(x) = 1); g/H^2 = -e'/R, so g <= 0 for all tau  <=>  P_x(tau) := sum_j k_j beta_j x/(beta_j - x) e^{-beta_j tau} >= 0.
For fixed betas these are LINEAR constraints on k: LP feasibility on a tau grid (0..40), maximizing a margin m with
P_x(tau) >= m * e^{-beta_min tau} (scale-free), x in {3, 4}, subject to G(3) = G(4) = 1, |k_j| <= 1e4.
A smooth release is a positive superposition of steps, so the step condition covers every drop into these sectors.
"""
import numpy as np
from scipy.optimize import linprog
taus = np.concatenate([np.linspace(0, 2, 801), np.linspace(2, 40, 400)[1:]])
def lp(betas):
    b = np.array(betas, float); n = len(b)
    A_ub = []; b_ub = []
    for x in (3.0, 4.0):
        for t in taus:
            row = -(b*x/(b - x))*np.exp(-b*t)            # -P_x(tau) + m e^{-bmin tau} <= 0
            A_ub.append(np.r_[row, np.exp(-b.min()*t)]); b_ub.append(0.0)
    A_eq = [np.r_[3/(b-3), 0.0], np.r_[4/(b-4), 0.0]]; b_eq = [1.0, 1.0]
    c = np.r_[np.zeros(n), -1.0]                        # maximize m
    bounds = [(-1e4, 1e4)]*n + [(None, 10.0)]
    r = linprog(c, A_ub=np.array(A_ub), b_ub=b_ub, A_eq=np.array(A_eq), b_eq=b_eq, bounds=bounds, method='highs')
    return r, b
for betas in [(4.5, 6), (4.5, 6, 12), (4.5, 5, 6, 8, 12, 20), (4.2, 4.5, 5, 6, 8, 12, 20, 40, 80),
              (4.05, 4.1, 4.2, 4.5, 5, 6, 8, 12, 20, 40, 80, 160)]:
    r, b = lp(betas)
    if r.status == 0:
        k = r.x[:-1]; m = r.x[-1]
        print(f"betas={betas}: LP status ok, best margin m = {m:+.3e}  (m >= 0 means g <= 0 after every dust/radiation drop)")
        print(f"   k = {np.round(k, 4)}")
    else:
        print(f"betas={betas}: LP status {r.status} ({r.message})")
# Analytic reason (proved in report): at tau = 0, P_3(0) - P_4(0) ... and the large-tau sign is that of k at beta_min.
# Theorem L check (proved in report): for ANY linear causal kernel with G(x) = x int K e^{xs} ds,
#   int_0^inf P_4(tau) e^{3 tau} dtau = G(4) - G(3),  int_0^inf P_3(tau) e^{4 tau} dtau = G(4) - G(3)  (=0 if exact on both)
from scipy.integrate import quad
print("Theorem L numeric check on exponential-sum kernels:")
for betas, k in [((4.5, 6.0), None), ((5.0, 12.0), None), ((4.5, 6.0, 12.0), (0.0, -1.0, 6.0))]:
    b = np.array(betas)
    if k is None:
        k = np.linalg.solve(np.array([3/(b-3), 4/(b-4)]), np.array([1.0, 1.0]))
    k = np.array(k, float)
    G = lambda x: np.sum(k*x/(b-x))
    Pw = lambda t, x, y: np.sum(k*b*x/(b-x)*np.exp(-(b-y)*t))      # P_x(t) e^{y t}, no overflow
    I4 = quad(lambda t: Pw(t, 4.0, 3.0), 0, 400, limit=800)[0]
    I3 = quad(lambda t: Pw(t, 3.0, 4.0), 0, 400, limit=800)[0]
    print(f"  betas={betas}, k={np.round(k,4)}: G(3)={G(3.0):.6f}, G(4)={G(4.0):.6f}; int P4 e^3t = {I4:+.3e}, int P3 e^4t = {I3:+.3e}, G(4)-G(3) = {G(4.0)-G(3.0):+.3e}")
