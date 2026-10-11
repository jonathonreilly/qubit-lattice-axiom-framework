"""Independent numerical/algebraic spot checks for the RL1 referee.

This deliberately does not import any RL1 implementation module.  It uses an
adaptive integral for the BD zero, checks the projective duplicates in the
resolved F4b output, and recomputes the physical-scale arithmetic.
"""

import numpy as np
from scipy.integrate import quad_vec
from scipy.optimize import root
from scipy.special import kv


def bd_symbol_residual(q):
    """Real and imaginary parts of f_tilde(z)-1 by adaptive quadrature."""
    z = q[0] + 1j * q[1]

    def integrand(tau):
        m = np.pi * tau**4 / 24
        f = np.exp(-m) * (1 - 9 * m + 8 * m**2 - (4 / 3) * m**3)
        return 4 * np.pi * tau**3 * f * kv(1, z * tau) / (z * tau)

    value = quad_vec(
        integrand, 0, 10, epsabs=2e-11, epsrel=2e-11, limit=500
    )[0] - 1
    return np.array([value.real, value.imag])


fit = root(bd_symbol_residual, [0.3756, 5.0522], tol=1e-10)
z = fit.x[0] + 1j * fit.x[1]
print("BD root z:", z)
print("residual:", bd_symbol_residual(fit.x))
print("squared variable Z=z^2:", z**2)


# F4b samples a sphere in the three-dimensional nullspace.  Antipodal q and
# -q become the same coefficient vector after division by f0, so the six saved
# rows should occur in three near-identical projective pairs.
coefficients = np.load("RL1_F4b_stable_L6.npy")
print("F4b saved rows:", len(coefficients))
for i, j in [(0, 3), (1, 4), (2, 5)]:
    absolute = np.linalg.norm(coefficients[i] - coefficients[j])
    relative = absolute / np.linalg.norm(coefficients[i])
    print(f"projective pair {i},{j}: absolute={absolute:.3e} relative={relative:.3e}")


ell_planck = 1.616255e-35
gpc = 3.0857e25
k_variance = 2.8446
ell_k_locality = 1e-19
sd_efold_length = (2 / k_variance) * ell_k_locality**3 / ell_planck**2
ell_k_bound = (gpc * ell_planck**2 * k_variance / 2) ** (1 / 3)
print("conditional sd e-fold length at ell_k=1e-19 m:", sd_efold_length)
print("conditional ell_k bound for one sd e-fold over 1 Gpc:", ell_k_bound)


# Flat-space normalization check for the distributional statement in (a):
# G0=delta(t-r)/(4*pi*r), so the radial convolution at (T,0) is
# (1/(4*pi))*integral_0^infinity delta(T-2r) dr = 1/(8*pi).
print("flat G0*G0 jump:", 1 / (8 * np.pi))


# For a thin lens at u=0 with endpoints y<0<x, the density transform is
# F_eta(y,x)=int_y^x (u-y)(x-u) eta(u)du.  Any ordinary eta obeys
# d_x^2 F_eta=(x-y)eta(x).  The required first-order target from
# -ln(nu*Delta) is F_req=R*y*x*(x^2-3*x*y+y^2)/6, for which
# d_x^2 F_req/(x-y)=R*y.  Dependence on y makes equality for all endpoint
# pairs impossible, even without assuming eta is supported inside the lens.
for y, x in [(-1.0, 2.0), (-2.0, 2.0)]:
    required_eta_at_x = y  # set the nonzero lens strength R to one
    print(f"density integrability at (y,x)=({y},{x}): eta(x) would have to be {required_eta_at_x}")
