"""Algebraic inverse for the explicitly conditional clamped-pulse protocol."""
import numpy as np

AUDIT_TIMEOUT_SEC = 120


def infer_coefficients(samples):
    """Use five samples; a singular measured design raises, not passes."""
    d = np.diff(np.asarray(samples)[:5])
    X = np.array([[d[1], -d[0]], [d[2], -d[1]]])
    y = d[2:4]
    return np.linalg.solve(X, y), X, y


def extrapolation_weights(s, p):
    if p <= 0:
        raise ValueError('positive p is required')
    return np.array([-p, s+p, -(1+s), (s+p)/p, -(1+s)/p, 1/p])


def response_surface(D):
    """Reference column0, anchor row0 and last column; nonzero anchor required."""
    E = D-D[:, [0]]
    anchor = E[0, -1]
    if anchor == 0:
        raise ValueError('nonzero response anchor is required')
    return E, anchor, E[:, -1]/anchor, E[0, :]/anchor


def coefficient_gradient(s, p, samples):
    fm2, fm1, f0, f2, f3, f4 = samples
    return ((f2-f3)/p-f0+fm1,
            -(f4-(1+s)*f3+s*f2)/p**2+fm1-fm2)


def coefficient_error_bound(M, epsilon_theta, p_min, S):
    if p_min <= 0 or any(v < 0 for v in (M, epsilon_theta, S)):
        raise ValueError('invalid coefficient error certificate')
    return M*epsilon_theta*(2/p_min+4+(2+2*S)/p_min**2)


def calibration_error_bound(X_hat, theta_hat, epsilon_force):
    if epsilon_force < 0:
        raise ValueError('negative measurement uncertainty')
    norm = np.linalg.norm(np.linalg.inv(X_hat), np.inf)
    eta = norm*4*epsilon_force
    if eta >= 1:
        raise ValueError('calibration error region is not certified invertible')
    return norm/(1-eta)*(2*epsilon_force+4*epsilon_force*np.linalg.norm(theta_hat, np.inf))


def ratio_error_bound(numerator, anchor, epsilon_numerator, epsilon_anchor):
    if abs(anchor) <= epsilon_anchor or min(epsilon_numerator, epsilon_anchor) < 0:
        raise ValueError('uncertified ratio denominator')
    return (epsilon_numerator+abs(numerator/anchor)*epsilon_anchor)/(abs(anchor)-epsilon_anchor)


def shape_error_bound(epsilon_B_x, epsilon_B_y, kappa_hat,
                      integral_epsilon_A, epsilon_kappa, integral_abs_A_hat):
    """Integrals are nonnegative over the unoriented interval between endpoints."""
    if min(epsilon_B_x, epsilon_B_y, integral_epsilon_A,
           epsilon_kappa, integral_abs_A_hat) < 0:
        raise ValueError('error integrals must use increasing endpoint limits')
    return (epsilon_B_x+epsilon_B_y+abs(kappa_hat)*integral_epsilon_A
            +epsilon_kappa*(integral_abs_A_hat+integral_epsilon_A))
