"""E2: how much can ANY charged matter sector pull an elementary U(1) photon onto its light cone?

Photon quadratic form L = (1/2)(a E^2 - b B^2), c_gamma^2 = b/a.  A Lorentz-invariant matter sector with
speed c_m (however strongly self-coupled) adds X(L) (1/c_m, c_m) to (a, b), where X(L) = 1/e^2(L) - 1/e0^2 is
the same current-two-point log that runs the coupling.  Then, to first order in the split,
    c_gamma - c_m  =  (c_gamma0 - c_m) * e^2(L)/e0^2  =  (c_gamma0 - c_m) * alpha_IR/alpha_UV      (photon side)
Matter is pulled toward the photon by photon exchange at rate p_m * (-d ln e^2/dL); for N copies of an
elementary species p_m = p_1/N with p_1 = 2 (Dirac), 6 (complex scalar) [kappa/(beta0 share), e2_coeffs].
Total: S = (alpha_IR/alpha_UV)^(1 + p_m).  Scan N with alpha(1 TeV) = 1/128 and alpha(M_Pl) <= alpha_max.
Usage: python e2_photon_bound.py
"""
import numpy as np

MPl, TeV = 1.22e19, 1e3
target = 2.66e-19 / 8.55e-3
print(f"needed e/gamma suppression (LHAASO bound / F2 split): {target:.2e}")

# 1) exact (a,b) bookkeeping vs the linear formula, for a check
e0sq, c0, cm = 0.5, 1.01, 1.0
for X in (1.0, 10.0, 100.0):
    a = 1 / (e0sq * c0) + X / cm; b = c0 / e0sq + X * cm
    cg = np.sqrt(b / a); esq = 1 / (1 / e0sq + X)
    print(f"  X = {X:6.1f}: exact c_gamma - c_m = {cg-cm:.6e} ; (c0-cm) e^2/e0^2 = {(c0-cm)*esq/e0sq:.6e}")

L = np.log(MPl / TeV)
for lab, per, p1 in (("Dirac fermions (unit charge)", 2 / (3 * np.pi), 2.0), ("complex scalars (unit charge)", 1 / (6 * np.pi), 6.0)):
    print(f"\n{lab}: d(1/alpha)/dL = {per:.4f} per species; matter-side p_1 = {p1}")
    for amax in (1.0, 4 * np.pi):
        best = (1.0, None)
        for N in np.arange(1, 4000):
            ainv_uv = 128.0 - per * N * L
            if ainv_uv < 1 / amax:
                break
            S = (ainv_uv / 128.0) ** (1 + p1 / N)
            if S < best[0]:
                best = (S, N, 1 / ainv_uv)
        S, N, auv = best
        print(f"  alpha_UV <= {amax:5.2f}: best N = {N}, alpha(M_Pl) = {auv:.3f}, S_min = {S:.2e}  "
              f"(misses target by x{S/target:.1e})")
print("\nFor a strongly coupled charged CFT the photon-side factor alpha_IR/alpha_UV is unchanged;"
      " reaching the target needs 1 + p_m >= ln(target)/ln(alpha_IR/alpha_UV):")
for auv in (0.05, 0.3, 1.0, 4 * np.pi):
    print(f"  alpha_UV = {auv:6.2f}: needs 1 + p_m >= {np.log(target)/np.log((1/128)/auv):.1f}")
