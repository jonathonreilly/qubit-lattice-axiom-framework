"""T46 kill check K3: independent check of the attacker's P2 (SM Yukawa flow to M_Pl).
Own minimal one-loop system for (y_t, g1, g2, g3) plus the analytic lemma
   d ln V_cb / dt = d ln (m_s/m_b) / dt = (3/2) y_t^2 /(16 pi^2)      (top-Yukawa part; b/s/c self-terms are O(y_b^2) corrections)
so that p(mu) = (ln V0 + x)/(ln R0 + x), x = (3/2) I(mu), I = int y_t^2/(16 pi^2) dt.
Compare with the attacker's full 3x3 matrix integration (t46_p2_sm_rge.py).
"""
import sys
import numpy as np
from scipy.integrate import solve_ivp
sys.path.insert(0, "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T46_scratch")

k = 1/(16*np.pi**2)
def rhs(t, y):
    yt, g1, g2, g3, I = y
    dyt = k*yt*(4.5*yt**2 - 8*g3**2 - 2.25*g2**2 - 17/20*g1**2)
    dg = [k*(41/10)*g1**3, k*(-19/6)*g2**3, k*(-7)*g3**3]
    return [dyt, *dg, k*yt**2]

MT, MPL = 163.0, 1.220890e19
y0 = [0.9369, 0.4629, 0.6478, np.sqrt(4*np.pi*0.1085), 0.0]
tt = np.log(np.array([MT, 246.22, 1e3, 1e6, 1e10, 1.974e16, MPL]))
s = solve_ivp(rhs, [tt[0], tt[-1]], y0, t_eval=tt, rtol=1e-11, atol=1e-13, method="DOP853")
V0, R0 = 0.0422, 0.018854
print("mu[GeV]      y_t      I       exp(1.5 I)   p_lemma = (lnV0+x)/(lnR0+x)")
for mu, yt, I in zip(np.exp(s.t), s.y[0], s.y[4]):
    x = 1.5*I
    print(f"{mu:10.3e}  {yt:.4f}  {I:.5f}  {np.exp(x):.4f}      {(np.log(V0)+x)/(np.log(R0)+x):.4f}")
print("attacker's full 3x3 result at M_Pl: y_t=0.4039, V/V0=1.1387, R/R0=1.1383, p=0.7902")
x_need = (5/6*np.log(R0) - np.log(V0))/(1 - 5/6)
print(f"\nx needed for p=5/6: x = {x_need:+.3f}  (i.e. V and R would have to FALL by a factor {np.exp(x_need):.3f} going up; the SM top Yukawa makes x > 0)")
