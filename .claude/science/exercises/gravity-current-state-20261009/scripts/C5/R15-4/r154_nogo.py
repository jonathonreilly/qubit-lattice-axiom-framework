"""R15-4 no-go check (Lemma N+): positive, dust-exact linear readers obey G(x) <= x(4-x)/3 on (0,3) and G(x) <= 0 on x<0.

Class R+: rho_hat(u) = int_0^inf K(s) E(u-s) ds (causal, linear, u-translation invariant, reads only E = -d rho_tot/du),
with (i) G(3) = 1 (dust read exactly) and (ii) rho_hat >= 0 on every reheating history (all content created as radiation
from a vacuum at one instant), which is equivalent to H(t) := int_0^t K(s) e^{4s} ds >= 0 for all t (proof in report).
Proof sketch: F(x) := int K e^{xs} ds = (4-x) L_H(4-x) (parts), L_H(p) = int H e^{-ps} ds is nonincreasing in p (H>=0),
L_H(1) = F(3) = 1/3; so for 0<x<3: F(x) <= (4-x)/3, G(x) = x F(x) <= x(4-x)/3; for x<0: G(x) = x (4-x) L_H(4-x) <= 0.
Numerical check: LP over K = sum_j k_j e^{-beta_j s} (40 rates in [4.5, 400]) with H(t_i) >= 0 on a fine grid, G(3)=G(4)=1,
|k_j| <= Kmax, maximising G(x*). Reported: the LP optimum vs the bound, and the transition sensitivity T_K of the optimum.
"""
import numpy as np
from scipy.optimize import linprog

b = np.geomspace(4.5, 400, 40)
t = np.concatenate([[0.0], np.geomspace(1e-5, 40, 1500)])
Hrows = np.array([(1 - np.exp(-(b - 4) * tt)) / (b - 4) for tt in t])
Grow = lambda x: x / (b - x)
for xs in (0.15, 0.3, 0.75, 1.5, 2.5, -0.3, -1.0):
    out = []
    for Kmax in (1e2, 1e4, 1e6):
        res = linprog(-Grow(xs), A_ub=-Hrows, b_ub=np.zeros(len(t)), A_eq=np.array([Grow(3.0), Grow(4.0)]),
                      b_eq=[1.0, 1.0], bounds=[(-Kmax, Kmax)] * len(b), method='highs')
        if res.status == 0:
            k = res.x
            TK = np.max(np.abs(1 - 4 * (Hrows @ k)))
            out.append(f'Kmax={Kmax:.0e}: max G={-res.fun:+.4f} (T_K={TK:.1f})')
        else:
            out.append(f'Kmax={Kmax:.0e}: LP status {res.status}')
    bound = xs * (4 - xs) / 3 if xs > 0 else 0.0
    print(f'x*={xs:+.2f} (w={-1+xs/3:+.3f}): bound {bound:+.4f} | ' + '; '.join(out))
