"""Kill-round checks for routes F5/F6 (independent of agent4_checks.py).

K1  direction-averaged coupling of helicity +-1 vs TT polarisation tensors to a
    symmetric source amplitude T^{ij}(q->0, w); exact quadrature, not Monte Carlo.
K2  radiated power of a massless mode of speed c1 and kinetic weight Z coupled as
    h_ij T^ij: P = w^2/(32 pi^2 Z c1^3) * Int dOmega |eps:T|^2.  Ratio to TT.
K3  Lorentz-violating source: Newtonian binary, kinetic-only stress T^ij = sum m v^i v^j
    (energy flux != momentum density). The +-1/TT ratio is still 1; the identity
    Int T^ij = (1/2) Qddot^ij holds only once the binding stress is included.
K4  Cherenkov: coupling of +-1 vs TT tensors to an ultra-relativistic particle at the
    Cherenkov angle cos(theta) = c1/v, as a function of delta = 1 - c1/c.
K5  Static source (q_i T^ij = 0): +-1 coupling exactly zero.
"""
import numpy as np
from numpy.linalg import norm

# ---------- polarisation basis ----------
def frame(qhat):
    a = np.array([1.0, 0, 0]) if abs(qhat[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(qhat, a); e1 /= norm(e1)
    e2 = np.cross(qhat, e1)
    return e1, e2

def pols(qhat):
    e1, e2 = frame(qhat)
    sym = lambda a, b: 0.5 * (np.outer(a, b) + np.outer(b, a))
    tt = [(np.outer(e1, e1) - np.outer(e2, e2)) / np.sqrt(2), np.sqrt(2) * sym(e1, e2)]
    h1 = [np.sqrt(2) * sym(qhat, e1), np.sqrt(2) * sym(qhat, e2)]
    h0 = [(3 * np.outer(qhat, qhat) - np.eye(3)) / np.sqrt(6)]
    tr = [np.eye(3) / np.sqrt(3)]
    return tt, h1, h0, tr

# Gauss-Legendre x uniform phi quadrature on the sphere
def sphere_quad(nth=64, nph=128):
    x, w = np.polynomial.legendre.leggauss(nth)
    ph = np.arange(nph) * 2 * np.pi / nph
    pts, wts = [], []
    for ct, wt in zip(x, w):
        st = np.sqrt(1 - ct * ct)
        for p in ph:
            pts.append(np.array([st * np.cos(p), st * np.sin(p), ct])); wts.append(wt * 2 * np.pi / nph)
    return np.array(pts), np.array(wts)

PTS, WTS = sphere_quad()

def channel_weights(T):
    """direction-averaged sum_pol |eps:T|^2 for each helicity channel"""
    out = {"TT": 0.0, "pm1": 0.0, "h0": 0.0, "tr": 0.0}
    for qhat, w in zip(PTS, WTS):
        tt, h1, h0, tr = pols(qhat)
        for name, ps in (("TT", tt), ("pm1", h1), ("h0", h0), ("tr", tr)):
            out[name] += w * sum(abs(np.sum(p * T)) ** 2 for p in ps)
    for k in out:
        out[k] /= 4 * np.pi
    return out

print("K1  direction-averaged channel weights of a symmetric source amplitude")
rng = np.random.default_rng(1)
for trial in range(3):
    R = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); R = R + R.T
    Rt = R - np.trace(R) / 3 * np.eye(3)
    cw = channel_weights(R)
    print(f"   random symmetric (with trace): TT={cw['TT']:.6f} pm1={cw['pm1']:.6f} h0={cw['h0']:.6f} tr={cw['tr']:.6f}"
          f"  |Rt|^2/5={np.sum(abs(Rt)**2)/5:.6f}  ratio pm1/TT={cw['pm1']/cw['TT']:.6f}")
Qbin = np.array([[1, 1j, 0], [1j, -1, 0], [0, 0, 0]], dtype=complex)  # circular binary, 2 Omega component
cw = channel_weights(Qbin)
print(f"   circular binary: ratio pm1/TT = {cw['pm1']/cw['TT']:.6f}; h0/TT = {cw['h0']/cw['TT']:.6f}")
print("   => each helicity pair carries 2/5 of |traceless part|^2: exact by SO(3) representation theory.\n")

print("K2  radiated power of a massless mode: P ~ omega^2/(32 pi^2 Z c^3) Int dOmega |eps:T|^2")
print("   P_pm1/P_TT = (Z_TT/Z_pm1) (c_TT/c_pm1)^3 x 1")
for c1 in (0.5, 0.866, 1.0, 1.061, 2.0, 5.0, 12.4, 19.7, 50.0):
    print(f"   c_pm1/c_TT = {c1:6.3f}: P ratio (equal Z) = {c1**-3:.3e};  with Z_pm1 = 4 Z_TT (09-29 floor) = {0.25*c1**-3:.3e}")
bound = 1.3e-4
print(f"   speed needed to hide under the double-pulsar bound {bound:.1e}: equal Z -> c1 >= {bound**(-1/3):.1f} c_TT;"
      f" Z ratio 4 -> c1 >= {(0.25/bound)**(1/3):.1f} c_TT\n")

print("K3  Lorentz-violating source: Newtonian binary, kinetic-only stress")
GM = 1.0; m1 = 0.6; m2 = 0.4; a = 1.0
Om = np.sqrt(GM / a ** 3)
def state(t):
    r1 = m2 / (m1 + m2) * a; r2 = m1 / (m1 + m2) * a
    x1 = r1 * np.array([np.cos(Om * t), np.sin(Om * t), 0]); x2 = -r2 / r1 * x1
    v1 = r1 * Om * np.array([-np.sin(Om * t), np.cos(Om * t), 0]); v2 = -r2 / r1 * v1
    return x1, x2, v1, v2
N = 4096; ts = np.arange(N) * 2 * np.pi / Om / N
Tkin = np.zeros((N, 3, 3)); Tfull = np.zeros((N, 3, 3)); Q = np.zeros((N, 3, 3)); Eflux = np.zeros((N, 3)); Pmom = np.zeros((N, 3))
for n, t in enumerate(ts):
    x1, x2, v1, v2 = state(t)
    Tkin[n] = m1 * np.outer(v1, v1) + m2 * np.outer(v2, v2)
    d = x1 - x2; F = -GM * m1 * m2 / (m1 + m2) * d / norm(d) ** 3 * (m1 + m2) / (m1 * m2) * (m1 * m2 / (m1 + m2))  # force on 1
    F = -GM * m1 * m2 * d / norm(d) ** 3
    # binding stress: int T^ij_field = (1/2)(x1^i F^j + x1^j F^i) + (1 <-> 2, F -> -F)  (virial form)
    Tfull[n] = Tkin[n] + 0.5 * (np.outer(x1 - x2, F) + np.outer(F, x1 - x2))
    Q[n] = m1 * np.outer(x1, x1) + m2 * np.outer(x2, x2)
    Eflux[n] = 0.5 * m1 * v1 @ v1 * v1 + 0.5 * m2 * v2 @ v2 * v2   # kinetic energy flux
    Pmom[n] = m1 * v1 + m2 * v2
def fourier(X, k=2):
    return np.mean(X * np.exp(1j * k * Om * ts)[:, None, None], axis=0)
Qdd2 = -(2 * Om) ** 2 * fourier(Q)
print("   |int T_kin (2Om)|:", np.round(abs(fourier(Tkin)), 4).tolist())
print("   |(1/2) Qddot (2Om)|:", np.round(abs(0.5 * Qdd2), 4).tolist())
print("   |int T_full (2Om)| (kinetic + binding stress):", np.round(abs(fourier(Tfull)), 4).tolist())
print(f"   max|int T_full - Qddot/2| = {np.max(abs(fourier(Tfull) - 0.5*Qdd2)):.2e};  max|int T_kin - Qddot/2| = {np.max(abs(fourier(Tkin) - 0.5*Qdd2)):.2e}")
print(f"   energy flux != momentum density here: max|E-flux| = {np.max(abs(Eflux)):.3f}, max|P| = {np.max(abs(Pmom)):.1e}")
for name, T in (("kinetic-only", fourier(Tkin)), ("full", fourier(Tfull))):
    cw = channel_weights(T)
    print(f"   {name:13s}: pm1/TT = {cw['pm1']/cw['TT']:.6f}")
print("   => the +-1/TT ratio is 1 for ANY symmetric amplitude; only the normalisation (which T^ij) needs conservation.\n")

print("K4  Cherenkov: coupling to an ultra-relativistic particle p = p zhat at cos(theta_C) = c1/v")
p = np.array([0, 0, 1.0])
for delta in (1e-1, 1e-2, 1e-3, 1e-4, 0.5):
    ct = 1 - delta; st = np.sqrt(1 - ct * ct)
    qhat = np.array([st, 0, ct])
    tt, h1, _, _ = pols(qhat)
    T = np.outer(p, p)
    w_tt = sum(abs(np.sum(t * T)) ** 2 for t in tt); w_1 = sum(abs(np.sum(t * T)) ** 2 for t in h1)
    print(f"   delta = {delta:7.1e}: |eps_pm1:pp|^2 = {w_1:.3e} (~4 delta), |eps_TT:pp|^2 = {w_tt:.3e} (~2 delta^2); ratio = {w_1/w_tt:.2e}")
print("   => near-marginal partners are Cherenkov-coupled MORE strongly than TT (delta vs delta^2).\n")

print("K5  static source (q_i T^ij = 0): +-1 coupling")
qhat = rng.normal(size=3); qhat /= norm(qhat); e1, e2 = frame(qhat)
Ts = 0.3 * np.outer(e1, e1) + 0.7 * np.outer(e2, e2) + 0.2 * (np.outer(e1, e2) + np.outer(e2, e1))
_, h1, _, _ = pols(qhat)
print("   ", [f"{abs(np.sum(t*Ts)):.1e}" for t in h1], " (exactly zero)\n")
