"""Lane RI, probe I3, script 1: cubic (separable) single-band designs on the fine Z^3 grid.

Free real lattice scalar, omega^2 = m^2 + sum_i w(k_i), u = omega^2/2 (lane RC C3 notation).
Per fine site (zone averages), for each design:
  zone mean of u_xx                       (C3 sum rule: exactly 0 for periodic u)
  rho   = 1/2 <omega>                      (vacuum energy density, zero-point)
  p_x   = 1/2 <(d_x u)^2/omega>            (vacuum pressure, from the flow-defined linear coupling)
  a_x   = 1/2 <(u_xx - 1) omega>           (vacuum value of the C3 boost anomaly E_x - H, per site)
  ident = a_x + rho + p_x                  (claimed exact identity: should be 0; integration by parts)
  mu_E, mu_T2 = -1/8 <X^2/omega^3>         (RN L1 linear-only paramagnetic TT Hessian, same normalization)
  Aw    = <(u_xx-1) X_T^2/omega^3>/<X_T^2/omega^3>  (C3 anomaly weighted by the T2 loop measure)
  A_IR exponent of u_xx - 1 along the axis at small k.
Designs: NN (RN L1 control), Taylor-improved range r, naive boson (w = sin^2 k, doublers),
and 'separable-flat(L)': w'(k) = 2k S((|k|-kappa)/kappa), kappa = pi/L (flat for |k_i| >= 2 kappa).
With the unitary seagull of the RN L1 referee every mu is exactly 0 (isospectral flow), for every design.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

np.set_printoptions(linewidth=160)


def smooth_step(t):
    """C-infinity step: 1 for t<=0, 0 for t>=1."""
    t = np.clip(t, 0.0, 1.0)
    def psi(x):
        out = np.zeros_like(x)
        pos = x > 0
        out[pos] = np.exp(-1.0 / x[pos])
        return out
    a, b = psi(1 - t), psi(t)
    return a / (a + b)


def smooth_step_d(t, h=1e-6):
    return (smooth_step(t + h) - smooth_step(t - h)) / (2 * h)


def improved_coeffs(r):
    # w(k) = sum_n c_n 2(1-cos nk) = k^2 + O(k^(2r+2)): sum c_n n^2 = 1, sum c_n n^(2j) = 0 (j=2..r)
    n = np.arange(1, r + 1, dtype=float)
    M = np.array([n ** (2 * j) for j in range(1, r + 1)])
    rhs = np.zeros(r); rhs[0] = 1.0
    return np.linalg.solve(M, rhs)


def design(name, L=None, r=None):
    """Return functions w, w', w'' of one axis momentum k in [0, pi]."""
    if name == "NN":
        return (lambda k: 2 - 2 * np.cos(k), lambda k: 2 * np.sin(k), lambda k: 2 * np.cos(k))
    if name == "improved":
        c = improved_coeffs(r); n = np.arange(1, r + 1)
        w = lambda k: sum(ci * 2 * (1 - np.cos(ni * k)) for ci, ni in zip(c, n))
        w1 = lambda k: sum(ci * 2 * ni * np.sin(ni * k) for ci, ni in zip(c, n))
        w2 = lambda k: sum(ci * 2 * ni * ni * np.cos(ni * k) for ci, ni in zip(c, n))
        return (w, w1, w2)
    if name == "naive":
        return (lambda k: np.sin(k) ** 2, lambda k: np.sin(2 * k), lambda k: 2 * np.cos(2 * k))
    if name == "sepflat":
        kap = np.pi / L
        # w'(k) = 2k S((k-kap)/kap) on [0,pi]; w by accurate quadrature on a fine table
        kt = np.linspace(0, np.pi, 200001)
        w1t = 2 * kt * smooth_step((kt - kap) / kap)
        wt = np.concatenate([[0.0], np.cumsum(0.5 * (w1t[1:] + w1t[:-1]) * np.diff(kt))])
        w = lambda k: np.interp(k, kt, wt)
        w1 = lambda k: 2 * k * smooth_step((k - kap) / kap)
        w2 = lambda k: 2 * smooth_step((k - kap) / kap) + 2 * k * smooth_step_d((k - kap) / kap) / kap
        return (w, w1, w2)
    raise ValueError(name)


def axis_nodes(breaks, n):
    xs, ws = [], []
    x0, w0 = leggauss(n)
    for a, b in zip(breaks[:-1], breaks[1:]):
        xs.append(0.5 * (b - a) * x0 + 0.5 * (b + a)); ws.append(0.5 * (b - a) * w0)
    x = np.concatenate(xs); w = np.concatenate(ws)
    return x, w / np.pi  # normalized average over [0,pi] (integrands are even in each k_i)


def measure(name, m, L=None, r=None, n=48):
    w, w1, w2 = design(name, L=L, r=r)
    if name == "sepflat":
        kap = np.pi / L
        breaks = [0, kap, 2 * kap, np.pi] if 2 * kap < np.pi else [0, kap, np.pi]
    else:
        breaks = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi]
    k, wt = axis_nodes(breaks, n)
    W, W1, W2 = w(k), w1(k), w2(k)
    acc = dict(uxx=0.0, rho=0.0, px=0.0, ax=0.0, muE=0.0, muT=0.0, AwN=0.0, AwD=0.0)
    for iz in range(len(k)):
        om2 = m * m + W[:, None] + W[None, :] + W[iz]
        om = np.sqrt(om2)
        ww = wt[:, None] * wt[None, :] * wt[iz]
        dxu = 0.5 * W1[:, None] * np.ones_like(om)
        dyu = 0.5 * W1[None, :] * np.ones_like(om)
        uxx = 0.5 * W2[:, None] * np.ones_like(om)
        XE = dxu ** 2 - dyu ** 2
        XT = 2 * dxu * dyu
        acc["uxx"] += np.sum(ww * uxx)
        acc["rho"] += np.sum(ww * 0.5 * om)
        acc["px"] += np.sum(ww * 0.5 * dxu ** 2 / om)
        acc["ax"] += np.sum(ww * 0.5 * (uxx - 1) * om)
        acc["muE"] += np.sum(ww * XE ** 2 / om ** 3)
        acc["muT"] += np.sum(ww * XT ** 2 / om ** 3)
        acc["AwN"] += np.sum(ww * (uxx - 1) * XT ** 2 / om ** 3)
        acc["AwD"] += np.sum(ww * XT ** 2 / om ** 3)
    out = dict(uxx=acc["uxx"], rho=acc["rho"], px=acc["px"], ax=acc["ax"],
               ident=acc["ax"] + acc["rho"] + acc["px"],
               muE=-acc["muE"] / 8, muT=-acc["muT"] / 8, Aw=acc["AwN"] / acc["AwD"])
    # IR exponent of A = u_xx - 1 along the x axis
    ks = np.array([1e-2, 2e-2]) * (np.pi / L if L else 1.0)
    A = 0.5 * w2(ks) - 1.0
    if np.all(np.abs(A) > 1e-13):
        out["IRexp"] = np.log(abs(A[1] / A[0])) / np.log(2)
    else:
        out["IRexp"] = float("inf")  # exactly zero below kappa (C-infinity design)
    out["Api"] = 0.5 * w2(np.array([np.pi]))[0] - 1.0
    return out


def show(tag, o):
    print(f"{tag:28s} <u_xx>={o['uxx']:+.2e} rho={o['rho']:.5e} p_x={o['px']:.5e} a_x={o['ax']:+.5e} "
          f"a+rho+p={o['ident']:+.1e} muE={o['muE']:+.5e} muT2={o['muT']:+.5e} A_w(T2)={o['Aw']:+.3f} "
          f"IRexp={o['IRexp']:.2f} A(pi)={o['Api']:+.3f}")


if __name__ == "__main__":
    print("== Control: RN L1 NN scalar, m=0 (expect muE=-0.003695, muT2=-0.011782) ==")
    for n in (32, 48):
        show(f"NN m=0 n={n}", measure("NN", 0.0, n=n))
    show("NN m=0.5", measure("NN", 0.5))
    show("NN m=1", measure("NN", 1.0))
    print("\n== Taylor-improved stencils (range r), m=0 ==")
    for r in (1, 2, 3, 4, 5):
        show(f"improved r={r}", measure("improved", 0.0, r=r))
    print("\n== Naive boson w=sin^2 k (8 doubler cones), m=0 ==")
    show("naive m=0", measure("naive", 0.0))
    print("\n== Separable-flat(L): relativistic for |k_i|<pi/L, flat for |k_i|>2pi/L, m=0 ==")
    rows = []
    for L in (2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64):
        o = measure("sepflat", 0.0, L=L, n=40)
        rows.append((L, o)); show(f"sepflat L={L}", o)
    print("\n   local log-slopes d ln|Q| / d ln L between successive L (separable-flat):")
    for (L1, o1), (L2, o2) in zip(rows[:-1], rows[1:]):
        s = lambda key: np.log(abs(o2[key] / o1[key])) / np.log(L2 / L1)
        print(f"   L {L1:3d}->{L2:3d}: rho {s('rho'):+.2f}  p_x {s('px'):+.2f}  a_x {s('ax'):+.2f}  "
              f"muE {s('muE'):+.2f}  muT2 {s('muT'):+.2f}")
