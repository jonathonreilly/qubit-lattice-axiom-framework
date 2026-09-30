"""Kill check T22: does the tails-tick 'pump' survive when the flux couples to an anomaly-free gauged charge?
Winding of det Q(kz) for the attacker's range-2 tails tick, with Peierls flux q*2pi/12 per plaquette (charge q).
Then sum over an SM-like charge assignment: species i has hypercharge Y_i; total winding = sum_i W(q_i)."""
import sys, numpy as np
sys.path.insert(0, '.')
import test_C3_winding as t
coef = t.fourier_coeffs(); M = t.hop_matrices(coef)
res = {}
for q in (1, -1, 2, -2, 3):
    t.B = q*2*np.pi/12*1.0*12/144*12/12  # placeholder overwritten below
    t.B = q*(2*np.pi*12/(144))   # flux 2*pi*q/12 per plaquette, N_phi = 12 q
    Qs = t.build_Q_nz(M)
    w, mx = t.wind_det(Qs, 800 if abs(q)<3 else 1600)
    res[q] = w
    print(f"charge q={q:+d}: winding = {w:+.4f}   (48*q = {48*q})  max step {mx:.2f}", flush=True)
# SM-like: 16 left-handed Weyl per generation, hypercharge in units of 1/3 (Y*3 values), all same handedness
Y3 = [1]*6 + [-3]*2 + [-4]*3 + [2]*3 + [6] + [0]   # Q_L(3x2), L(2), u^c(3), d^c(3), e^c, nu^c  (times 3)
Ysum = sum(Y3); print("sum of 3Y over 16 states =", Ysum, " sum of (3Y)^3 =", sum(y**3 for y in Y3))
print("pump for Y background ~ 48/3 * sum(3Y) =", 48/3*Ysum)
