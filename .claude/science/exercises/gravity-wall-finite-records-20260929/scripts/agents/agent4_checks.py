"""Two quick checks for the misframing brief (agent 4).

Check 1: coupling of helicity +-1 vs TT polarisation tensors to a conserved
quadrupole source.  For a conserved T^{mu nu}, T^{ij}(q->0, w) = -(w^2/2) Q^{ij}(w).
Static sources (w=0, q_i T^{ij} = 0) give eps^{+-1}:T = sqrt2 qhat_i e_j T^{ij} = 0.
Radiating sources: direction-averaged  sum_{+-1}|eps:Q|^2 / sum_{TT}|eps:Q|^2.

Check 2: perihelion advance of a test body for the 1PN Lagrangian
  L = v^2/2 + Phi + v^4/8 + A Phi v^2 + B Phi (xhat.v)^2 + C Phi^2,  Phi = GM/r
  GR (isotropic):           A = 3/2, B = 0,   C = -1/2   -> 6 pi GM/(a(1-e^2))
  broken-branch profile h_ij = Phi(delta + xhat xhat)/r (from the m^2-minimiser
  under the sourced scalar rule), same h_00:  A = 1, B = 1/2, C = -1/2.
"""
import numpy as np
from numpy.linalg import norm

rng = np.random.default_rng(0)

# ---------- Check 1 ----------
def basis(qhat):
    a = np.array([1.0, 0, 0]) if abs(qhat[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(qhat, a); e1 /= norm(e1)
    e2 = np.cross(qhat, e1)
    return e1, e2

def pol_tensors(qhat):
    e1, e2 = basis(qhat)
    sym = lambda a, b: 0.5 * (np.outer(a, b) + np.outer(b, a))
    tt = [(np.outer(e1, e1) - np.outer(e2, e2)) / np.sqrt(2), (np.outer(e1, e2) + np.outer(e2, e1)) / np.sqrt(2)]
    h1 = [np.sqrt(2) * sym(qhat, e1), np.sqrt(2) * sym(qhat, e2)]
    for t in tt + h1:
        assert abs(np.sum(t * t) - 1) < 1e-12
    return tt, h1

# circular binary in the xy plane: Q^{ij}(2 Omega) ~ [[1, i, 0],[i, -1, 0],[0,0,0]] (complex amplitude)
Q = np.array([[1, 1j, 0], [1j, -1, 0], [0, 0, 0]], dtype=complex)
# generic random symmetric traceless source as well
R = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); R = R + R.T; R -= np.trace(R) / 3 * np.eye(3)

def avg_ratio(Qc, n=20000):
    num = den = 0.0
    for _ in range(n):
        qhat = rng.normal(size=3); qhat /= norm(qhat)
        tt, h1 = pol_tensors(qhat)
        den += sum(abs(np.sum(t * Qc)) ** 2 for t in tt)
        num += sum(abs(np.sum(t * Qc)) ** 2 for t in h1)
    return num / den

print("Check 1: direction-averaged  P(+-1 coupling)/P(TT coupling), circular binary:", round(avg_ratio(Q), 4))
print("Check 1: same, random traceless symmetric source:", round(avg_ratio(R), 4))

# static source: T^{ij} with q_i T^{ij} = 0 (e.g. static stress); eps^{+-1}:T = sqrt2 qhat_i e_j T^{ij} = 0
qhat = rng.normal(size=3); qhat /= norm(qhat)
e1, e2 = basis(qhat)
Tstat = np.outer(e1, e1) * 0.3 + np.outer(e2, e2) * 0.7 + 0.2 * (np.outer(e1, e2) + np.outer(e2, e1))  # transverse
tt, h1 = pol_tensors(qhat)
print("Check 1: static (q_i T^ij = 0) coupling to +-1 tensors:", [round(abs(np.sum(t * Tstat)), 15) for t in h1],
      " to TT:", [round(abs(np.sum(t * Tstat)), 4) for t in tt])

# ---------- Check 2 ----------
from scipy.integrate import solve_ivp

GM = 1.0

def eom(A, B, C):
    # Lagrangian L = v^2/2 + Phi + v^4/8 + A Phi v^2 + B Phi (xhat.v)^2 + C Phi^2
    # Equations of motion via numerical Euler-Lagrange: p = dL/dv, dp/dt = dL/dx.
    def dL_dv(x, v):
        r = norm(x); xh = x / r; Phi = GM / r
        return v * (1 + 0.5 * v @ v + 2 * A * Phi) + 2 * B * Phi * (xh @ v) * xh
    def dL_dx(x, v):
        r = norm(x); xh = x / r; Phi = GM / r
        dPhi = -Phi / r * xh
        vv = v @ v; xv = xh @ v
        # d/dx of (xhat.v)^2 = 2 (xhat.v) * d(xhat.v)/dx ; d xhat_i/dx_j = (delta_ij - xh_i xh_j)/r
        dxv = (v - xv * xh) / r
        return dPhi * (1 + A * vv + B * xv ** 2 + 2 * C * Phi) + B * Phi * 2 * xv * dxv
    def rhs(t, y):
        x, v = y[:3], y[3:]
        # solve M(x,v) a = dL/dx - (d/dt of p at fixed a) ... do it implicitly by finite-difference Jacobian of p wrt v
        eps = 1e-7
        p0 = dL_dv(x, v)
        M = np.zeros((3, 3)); dpdx = np.zeros((3, 3))
        for k in range(3):
            dv = np.zeros(3); dv[k] = eps
            M[:, k] = (dL_dv(x, v + dv) - p0) / eps
            dx = np.zeros(3); dx[k] = eps
            dpdx[:, k] = (dL_dv(x + dx, v) - p0) / eps
        a = np.linalg.solve(M, dL_dx(x, v) - dpdx @ v)
        return np.concatenate([v, a])
    return rhs

def precession(A, B, C, a=2000.0, e=0.3, orbits=6):
    # PN parameter GM/a = 5e-4; use Newtonian initial data at perihelion
    rp = a * (1 - e)
    vp = np.sqrt(GM * (1 + e) / (a * (1 - e)))
    y0 = np.array([rp, 0, 0, 0, vp, 0])
    T = 2 * np.pi * np.sqrt(a ** 3 / GM)
    sol = solve_ivp(eom(A, B, C), [0, orbits * T], y0, rtol=1e-11, atol=1e-13, dense_output=True, max_step=T / 400)
    ts = np.linspace(0, orbits * T, orbits * 4000)
    xy = sol.sol(ts)[:2]
    r = norm(xy, axis=0); phi = np.unwrap(np.arctan2(xy[1], xy[0]))
    # perihelion passages: local minima of r
    idx = [i for i in range(1, len(r) - 1) if r[i] < r[i - 1] and r[i] < r[i + 1]]
    # parabolic interpolation of each minimum in (t, r), then phi at the interpolated time
    peri_phi = []
    for i in idx:
        t0, t1, t2 = ts[i - 1], ts[i], ts[i + 1]
        r0, r1, r2 = r[i - 1], r[i], r[i + 1]
        denom = (r0 - 2 * r1 + r2)
        tmin = t1 - 0.5 * (t2 - t1) * (r2 - r0) / denom if denom != 0 else t1
        x, y = sol.sol(tmin)[:2]
        peri_phi.append(np.arctan2(y, x))
    peri_phi = np.unwrap(np.array(peri_phi))
    dphi = np.diff(peri_phi)  # advance per orbit (wrapped angles, so no 2pi to remove)
    p_meas = 2 * r.min() * r.max() / (r.min() + r.max())  # semi-latus rectum from the orbit
    return dphi.mean(), 6 * np.pi * GM / p_meas

gr, gr_pred = precession(1.5, 0.0, -0.5)
bb, _ = precession(1.0, 0.5, -0.5)
g_half, _ = precession(1.0, 0.0, -0.5)
print(f"Check 2: perihelion advance per orbit  GR-Lagrangian {gr:.4e}  (6piGM/p from the orbit = {gr_pred:.4e}, ratio {gr/gr_pred:.4f})")
print(f"Check 2: broken-branch profile (A=1,B=1/2,C=-1/2): {bb:.4e}, ratio to GR {bb/gr:.4f}")
print(f"Check 2: A=1,B=0   (pure gamma=1/2, PPN (2+2g-b)/3 = 2/3): ratio {g_half/gr:.4f}")
