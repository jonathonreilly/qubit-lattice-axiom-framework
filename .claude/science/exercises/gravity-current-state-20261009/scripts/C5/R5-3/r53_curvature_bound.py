"""R5-3: what KP's <R>=0 (k int a dt = int a adot^2 dt - [a^3 H] >= int a adot^2 dt) demands of a
universe that looks like ours today. Units a0 = 1, H0 = 1. Past = LCDM-like (Omega_m = 0.315,
Omega_r = 9.1e-5, Omega_k ~ 0). Bound: Omega_k0 = k/adot0^2 >= <adot^2>_a / adot0^2 over the WHOLE history."""
import numpy as np
from scipy.integrate import quad
Om, Or = 0.315, 9.1e-5
OL = 1 - Om - Or
H = lambda a: np.sqrt(Or/a**4 + Om/a**3 + OL)
past_num = quad(lambda a: a**2*H(a), 0, 1, limit=200)[0]     # int a adot^2 dt = int a^2 H da
past_den = quad(lambda a: 1/H(a), 0, 1, limit=200)[0]        # int a dt = int da / H
print(f"past (Big Bang -> today): int a adot^2 dt = {past_num:.4f}, int a dt = {past_den:.4f}  (units a0/H0, adot0 = 1)")
print(f"past-only a-weighted <adot^2> = {past_num/past_den:.4f} adot0^2")
for Omk_max in [0.0034, 0.002, 0.001]:
    need = past_num/Omk_max
    print(f"|Omega_k0| <= {Omk_max}: total int a dt must be >= {need:.1f} (past supplies {past_den:.3f});"
          f" a future phase at a = a_l with adot ~ 0 must last >= {(need - past_den):.0f} (a0/a_l) Hubble times")
# a future de Sitter-like continuation adds to the numerator: show it can only make things worse
for T in [1, 3, 10]:
    # continue LCDM for T Hubble times: adot grows; numerator and denominator both grow
    from scipy.integrate import solve_ivp
    f = lambda t, y: [y[0]*H(y[0]), y[0], y[0]*(y[0]*H(y[0]))**2]
    s = solve_ivp(f, [0, T], [1.0, 0, 0], rtol=1e-10)
    num = past_num + s.y[2, -1]; den = past_den + s.y[1, -1]
    print(f"LCDM continued {T} H0^-1: <adot^2>_a = {num/den:.3f} adot0^2 (bound on Omega_k0 grows)")
