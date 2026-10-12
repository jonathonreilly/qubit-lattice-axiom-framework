"""RL1 (D): stability of the retarded MEAN BD operator in flat 4D (rho = 1), via its Laplace symbol.
For a Lorentz-invariant retarded kernel f(tau) (support in the future cone), acting on e^{s t + i k.x}:
   ftilde(z) = 4 pi int_0^inf tau^3 f(tau) K_1(z tau)/(z tau) dtau,   z^2 = s^2 + k^2   (Re z > 0 <=> Re s > 0 for some real k).
Mean operator symbol:  Bbar(z) = beta(-1 + ftilde(z)),  beta = 4/sqrt6;  continuum target: -(s^2 + k^2) = -z^2.
A zero of S(z) = ftilde(z) - 1 with Re z > 0 (other than the double zero at z = 0) is a growing mode of the retarded mean inverse:
growth rate in t up to Re z (k = 0: s = z).  Moment facts used: int f dsigma = int sigma f = int sigma^2 f = 0 (BD), so ftilde is
regular at z = 0 and S(z) = -(sqrt6/4) z^2 + O(z^4 ln z).
"""
import numpy as np
from scipy.special import kv
xg, wg = np.polynomial.legendre.leggauss(600)
TAU = 4.5*(xg+1); WT = 4.5*wg                 # tau in [0, 9]
def fc(tau):
    m = np.pi*tau**4/24; return np.exp(-m)*(1 - 9*m + 8*m**2 - (4/3)*m**3)
F = fc(TAU)
def ftilde(z):
    z = np.asarray(z, complex)[..., None]
    x = z*TAU
    return 4*np.pi*np.sum(WT*TAU**3*F*kv(1, x)/x, axis=-1)
def S(z): return ftilde(z) - 1.0

print("moments: int f dsig = %.3e, int sig f = %.3e, int sig^2 f = %.3e, int sig^3 f = %.4f" %
      tuple(np.sum(WT*2*TAU*TAU**(2*k)*F) for k in range(4)))
for z in [1e-3, 1e-2, 0.05, 0.1, 0.2]:
    print("  z=%.3g  S(z) = %+.6e   -(sqrt6/4) z^2 = %+.6e" % (z, S(z).real, -(np.sqrt(6)/4)*z*z))
# grid search for zeros in Re z > 0
xr = np.linspace(0.02, 6, 300); yi = np.linspace(-8, 8, 400)
Z = xr[None, :] + 1j*yi[:, None]
V = np.abs(S(Z))
cand = []
for i in range(1, V.shape[0]-1):
    for j in range(1, V.shape[1]-1):
        if V[i, j] < V[i-1:i+2, j-1:j+2].min()+1e-15 and V[i, j] == V[i-1:i+2, j-1:j+2].min() and V[i, j] < 0.3:
            cand.append(Z[i, j])
roots = []
for z0 in cand:
    z = z0
    for it in range(60):
        h = 1e-6
        d = (S(z+h)-S(z-h))/(2*h)
        dz = -S(z)/d; z = z + dz
        if abs(dz) < 1e-12: break
    if abs(S(z)) < 1e-9 and z.real > 1e-3 and not any(abs(z-r) < 1e-6 for r in roots):
        roots.append(complex(z))
print("zeros of S(z) with Re z > 0 (growing modes of the retarded mean inverse), sorted by Re z:")
for r in sorted(roots, key=lambda r: -r.real):
    print("  z = %+.6f %+.6fi   |S| = %.1e" % (r.real, r.imag, abs(S(r))))
# argument principle on a rectangle as a count check
def count(x0, x1, y0, y1, n=4000):
    path = np.concatenate([x0+1j*np.linspace(y0, y1, n), np.linspace(x0, x1, n)+1j*y1,
                           x1+1j*np.linspace(y1, y0, n), np.linspace(x1, x0, n)+1j*y0])
    v = S(path); ph = np.unwrap(np.angle(v))
    return (ph[-1]-ph[0])/(2*np.pi)
print("argument-principle count of zeros in [0.05,6]x[-8,8]: %.3f" % count(0.05, 6, -8, 8))
print("argument-principle count in [0.05,1.0]x[-8,8]: %.3f" % count(0.05, 1.0, -8, 8))
