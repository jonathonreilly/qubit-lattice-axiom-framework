"""R15-6 step 3: what a size bound on g costs, for ANY reader (best case: the reader's estimator is the oracle rho_nc).
Identity (r156_identity): V' = (g/H^2) R,  e := R - rho_nc = rho_v - V  =>  e' = rho_v' - (g/H^2) R.
Hence for every reader:
  (Lemma U, upper bound)  g <= c+ H^2  =>  e' >= rho_v' - c+ (rho_nc + e).
  (Lemma L, lower bound)  g >= -c- H^2 =>  e' <= rho_v' + c- (rho_nc + e).
Radiation only after the change (rho_nc' = -4 rho_nc), x := e/rho_nc:
  Lemma U: x' >= -c+ + (4 - c+) x  -> if x > c+/(4 - c+) (c+ < 4), x grows without bound (residual Lambda_tilde dominates).
  Lemma L: y := R/rho_nc = 1 + x:  y' <= -4 + (4 + c-) y -> if y < 4/(4 + c-), R reaches 0 in finite u (H -> 0).
Test: the BEST reader allowed by each bound: R' = -3h + clip(gam (rho_nc - R), -c+ R, c- R), oracle estimator,
gam = 200; radiation q0 = 1 at u = 0, no dust; vacuum change -D s(u) over width W (D > 0 drop, D < 0 rise).
Predictions for W -> 0: drop collapses iff c- < 4 alpha; rise runs away iff alpha > c+/4 (alpha = |D|/rho_nc before).
"""
import numpy as np
from scipy.integrate import solve_ivp
def run(D, W, cp, cm, gam=200.0, uT=0.0, q0=1.0, u_end=8.0):
    def s1(u): x = (u - uT)/W; return (1 - np.tanh(x)**2)/(2*W)
    u0 = uT - 10*W - 0.5
    def rhs(u, y):
        q, R = y
        if R <= 0: return [-4*q + D*s1(u), 0.0]
        h = 4*q/3
        Gam = np.clip(gam*(q - R), -cp*R, cm*R)
        return [-4*q + D*s1(u), -3*h + Gam]
    def collapse(u, y): return y[1] - 1e-9*y[0]
    collapse.terminal = True; collapse.direction = -1
    qs = q0*np.exp(-4*u0)
    sol = solve_ivp(rhs, (u0, u_end), [qs, qs], rtol=1e-10, atol=1e-30, method='LSODA', max_step=W/5, events=collapse)
    q, R = sol.y; u = sol.t
    x = R/q - 1
    alpha = D/(q0*np.exp(-4*uT)) if D > 0 else D/(q0*np.exp(-4*uT))
    status = "COLLAPSE (R->0) at u=%.2f" % sol.t_events[0][0] if len(sol.t_events[0]) else "no collapse"
    return u, q, R, x, status
print("=== Lemma L: drops with a lower bound g >= -c- H^2 (c+ = 1) ===")
for alpha in [0.1, 0.5, 2.0, 5.0]:
    for cm in [0.3, 1.0, 4.0, 10.0, 30.0]:
        u, q, R, x, st = run(alpha*1.0, 0.01, 1.0, cm)
        pred = "collapse" if cm < 4*alpha else "survive"
        print(f"  alpha={alpha:4.1f} c-={cm:5.1f}: {st:28s}  x(end)=R/rho_nc-1={x[-1]:+.2e}  [W->0 prediction: {pred}]")
print("=== Lemma U: rises with an upper bound g <= c+ H^2 (c- = 1e3) ===")
for alpha in [0.1, 0.2, 0.3, 0.5]:
    for cp in [0.5, 1.0, 2.0, 4.5]:
        u, q, R, x, st = run(-alpha*1.0, 0.01, cp, 1e3)
        xs = [np.interp(v, u, x) for v in (1.0, 4.0, 8.0)]
        pred = "runaway" if (cp < 4 and alpha/(1-alpha) > cp/(4-cp)) else "absorbed"
        print(f"  alpha={alpha:4.2f} c+={cp:4.1f}: x=(R-rho_nc)/rho_nc at u=1,4,8: {xs[0]:+.2e} {xs[1]:+.2e} {xs[2]:+.2e}"
              f"  [prediction: {pred}]")
print("=== Same rises, slower (W = 0.3; tanh tails e^{-2u/W} must decay faster than radiation e^{-4u}, else q < 0 = NEC violated) ===")
for alpha in [0.3, 0.5]:
    for cp in [1.0, 2.0]:
        u, q, R, x, st = run(-alpha*1.0, 0.3, cp, 1e3, u_end=12.0)
        xs = [np.interp(v, u, x) for v in (4.0, 8.0, 12.0)]
        print(f"  alpha={alpha:4.2f} c+={cp:4.1f} W=0.3: x at u=4,8,12: {xs[0]:+.2e} {xs[1]:+.2e} {xs[2]:+.2e};  min q*e^{{4u}} = {np.min(q*np.exp(4*u)):+.3f} (>0: NEC holds)")
print("=== Oracle (unbounded) reader on rises: max g/H^2 = max rho_v'/rho_nc ===")
for alpha in [0.1, 0.3, 0.5]:
    for W in [0.01, 0.1, 0.3, 0.45]:
        uu = np.linspace(-10*W - 1, 10*W + 6, 20001)
        s1 = (1 - np.tanh(uu/W)**2)/(2*W); D = -alpha
        # radiation with q' = -4q + D s1, q(-inf) e^{4u} = 1
        from scipy.integrate import cumulative_trapezoid
        qe = 1 + cumulative_trapezoid(D*s1*np.exp(4*uu), uu, initial=0)   # q e^{4u}
        q = qe*np.exp(-4*uu); gH2 = -D*s1/q
        print(f"  alpha={alpha:4.2f} W={W:4.2f}: oracle max g/H^2 = {gH2.max():+.3f};  min q e^{{4u}} = {qe.min():+.3f} (NEC);  "
              f"int(g/H^2 R)du/rho_nc(0) = {np.trapezoid(gH2*q, uu):+.4f} (= alpha)")
