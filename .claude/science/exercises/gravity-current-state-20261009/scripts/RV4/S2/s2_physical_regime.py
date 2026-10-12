"""Physical-regime tuning (ma ~ 1e-17): with NN KG dispersion and free p (3D, range<=4, 60 terms), kill the small-M expansion
   mu(M) = sum_n binom(-1/2,n) M^{2n} Q_n,  Q_n with vacuum gradient 1/2 sin k A^{-1/2-n}   (A = sum 4 sin^2(k/2))
for n = 0..3 in E and T2, plus the IR-log conditions p = k + O(k^5) (A = B = 0; rational).  Then mu = O(M^8 ln M) for every mass.
Reports: existence, distance from sin k, mu at M = 1, 0.3 (finite masses are NOT protected), and the E∇E violation."""
import numpy as np
from scipy.optimize import minimize
from s2_core import *
d, L, r = 3, 64, 4
tl = terms(d, r); T = len(tl); c = slope_vec(tl)
Avec = np.array([-t[0]**3/6 for t in tl]); Bvec = np.array([-t[0]*(t[1]**2 + t[2]**2)/4 for t in tl])
def vac_n(n):
    def f(K):
        A = sum(4*np.sin(k/2)**2 for k in K)
        return None, [0.5*np.sin(k)*A**(-0.5-n) for k in K]
    return f
Qn = [quad_forms(d, L, tl, vac_n(n), chans=('E', 'T2')) for n in range(4)]
a_sin = np.zeros(T); a_sin[tl.index((1, 0, 0))] = 1.0
a_imp = np.zeros(T); a_imp[tl.index((1, 0, 0))] = 4/3; a_imp[tl.index((2, 0, 0))] = -1/6
print("sin k      : c_0..c_3 (E) =", [f"{a_sin@Qn[n]['E']@a_sin:+.4e}" for n in range(4)], " (c_3 IR-divergent: grid value only)")
print("improved   : c_0..c_3 (E) =", [f"{a_imp@Qn[n]['E']@a_imp:+.4e}" for n in range(4)], " T2 all 0 (separable)")
cons = [{'type': 'eq', 'fun': lambda a: c @ a - 1}, {'type': 'eq', 'fun': lambda a: Avec @ a}, {'type': 'eq', 'fun': lambda a: Bvec @ a}]
for n in range(4):
    for ch in ('E', 'T2'):
        Q = Qn[n][ch]; s = np.abs(Q).max()
        cons.append({'type': 'eq', 'fun': lambda a, Q=Q, s=s: a @ Q @ a / s})
rng = np.random.default_rng(3); best = None
for s in range(10):
    a0 = a_imp + (0.05*s)*rng.standard_normal(T)
    rr = minimize(lambda a: np.sum((a - a_imp)**2), a0, constraints=cons, method='SLSQP', options={'maxiter': 3000, 'ftol': 1e-15})
    v = max(abs(cn['fun'](rr.x)) for cn in cons)
    if v < 1e-10 and (best is None or rr.fun < best.fun): best = rr
if best is None:
    print("no solution found")
else:
    a = best.x; np.save('s2_physreg_d3.npy', a)
    print(f"solution: |a - a_improved| = {np.sqrt(best.fun):.4f}, |a - a_sin| = {np.linalg.norm(a-a_sin):.4f}; max constraint violation {max(abs(cn['fun'](a)) for cn in cons):.1e}")
    print("   c_n (E):", [f"{a@Qn[n]['E']@a:+.1e}" for n in range(4)], " c_n (T2):", [f"{a@Qn[n]['T2']@a:+.1e}" for n in range(4)])
    for M in [1.0, 0.3]:
        Q = quad_forms(d, 48, tl, lambda K, M=M: kg_vac(K, M))
        print(f"   finite mass M={M}: mu_E={a@Q['E']@a:+.4e} mu_T2={a@Q['T2']@a:+.4e} mu_tr={a@Q['tr']@a:+.4e}  (sin k mu_E {a_sin@Q['E']@a_sin:+.4e})")
    K = grid(d, 32); P = 0
    for cc, t in zip(a, tl):
        Pt, _ = p_and_dp(t, K); P = P + cc*Pt[0]
    print(f"   E∇E violation rms(p_x - sin kx)/rms(sin kx) = {np.sqrt(np.mean((P-np.sin(K[0]))**2)/np.mean(np.sin(K[0])**2)):.4f};  max|a| = {np.abs(a).max():.3f}")
