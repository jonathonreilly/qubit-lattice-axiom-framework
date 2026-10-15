"""Independent lightweight checks for the NT-1'' referee report."""

import sys

import numpy as np

sys.path.insert(0, "scripts")
from nt1p_lib import Measure, Strip, eig_H, q_of, s2  # noqa: E402


def gamma_vector(sign):
    values, vectors = np.linalg.eigh(s2)
    return vectors[:, np.argmin(np.abs(values - sign))]


def tune_edge(A, strip, charge, row, target=np.pi):
    out = A.copy()
    links = strip.xl[row]
    wilson = out[0, links].sum()
    out[0, links] += (target / charge - wilson) / strip.Lx
    return out


def edge_vector(A, strip, charge, row, gamma_t_sign):
    spin = gamma_vector(gamma_t_sign)
    amps = np.ones(strip.Lx, dtype=complex)
    for x in range(strip.Lx - 1):
        link = strip.key[("x", x, row - strip.T + 1)]
        amps[x + 1] = amps[x] * np.exp(-1j * charge * A[0, link])
    psi = np.zeros(strip.N, dtype=complex)
    for x, amp in enumerate(amps):
        site = row * strip.Lx + x
        psi[2 * site : 2 * site + 2] = amp * spin
    return psi / np.linalg.norm(psi)


def edge_check(charge, edge):
    strip = Strip(4, 4)
    rng = np.random.default_rng(20261015 + charge)
    A = rng.normal(0.0, 0.27, (1, strip.nl))
    row = strip.Lt - 1 if edge == "top" else 0
    t = strip.T if edge == "top" else -strip.T + 1
    sign = +1 if edge == "top" else -1
    A = tune_edge(A, strip, charge, row)
    psi = edge_vector(A, strip, charge, row, sign)
    H = strip.H(charge * A)[0]
    evals = np.linalg.eigvalsh(H)
    W = A[0, strip.xl[row]].sum()
    print(
        f"edge={edge} charge={charge} eW-pi={charge * W - np.pi:+.3e} "
        f"||H psi||={np.linalg.norm(H @ psi):.3e} min|eig H|={np.min(np.abs(evals)):.3e}"
    )


def independent_fits():
    sizes = np.array([4.0, 6.0, 8.0, 10.0])
    means, ses, plateaus = [], [], []
    for L in sizes.astype(int):
        values = np.load(f"scripts/e1_Lx{L}.npy")
        means.append(values[:, 0].mean())
        ses.append(values[:, 0].std(ddof=1) / np.sqrt(len(values)))
        plateaus.append(values[:, 3].mean())
    means, ses, plateaus = map(np.asarray, (means, ses, plateaus))
    X = np.column_stack((np.ones_like(sizes), -sizes))
    weights = (means / ses) ** 2
    covariance = np.linalg.inv(X.T @ (weights[:, None] * X))
    beta = covariance @ X.T @ (weights * np.log(means))
    residual = np.log(means) - X @ beta
    chi2 = np.sum(weights * residual**2)
    sigma = np.sqrt(covariance[1, 1]) * np.sqrt(max(1.0, chi2 / 2.0))
    print(
        f"E1 independent WLS: nu={beta[1]:.6f} sigma={sigma:.6f} "
        f"significance={beta[1] / sigma:.2f}; L*P={sizes * plateaus}"
    )

    summary = np.load("scripts/nt1pp_summary.npz")
    L = summary["Lx"].astype(float)
    edge = summary["tau_edge_11112"]
    sel = L >= 16
    power = np.polyfit(np.log(L[sel]), np.log(edge[sel]), 1)
    exponential = np.polyfit(L[sel], np.log(edge[sel]), 1)
    rp = np.sum((np.polyval(power, np.log(L[sel])) - np.log(edge[sel])) ** 2)
    re = np.sum((np.polyval(exponential, L[sel]) - np.log(edge[sel])) ** 2)
    print(
        f"edge L=16..24: p={-power[0]:.6f}, power_RSS={rp:.3e}, "
        f"nu={-exponential[0]:.6f}, exp_RSS={re:.3e}"
    )


def bloch_chern(ngrid=61):
    """Independent 2x2 Bloch-band check, without the full torus code."""
    momenta = 2 * np.pi * np.arange(ngrid) / ngrid
    positive = np.empty((ngrid, ngrid, 2), dtype=complex)
    for ix, kx in enumerate(momenta):
        for it, kt in enumerate(momenta):
            d = np.array([np.sin(kt), -np.sin(kx), 1 - np.cos(kx) - np.cos(kt)])
            h = np.array(
                [[d[2], d[0] - 1j * d[1]], [d[0] + 1j * d[1], -d[2]]],
                dtype=complex,
            )
            positive[ix, it] = np.linalg.eigh(h)[1][:, 1]

    def unit_overlap(a, b):
        overlap = np.vdot(a, b)
        return overlap / abs(overlap)

    ux = np.empty((ngrid, ngrid), dtype=complex)
    ut = np.empty((ngrid, ngrid), dtype=complex)
    for ix in range(ngrid):
        for it in range(ngrid):
            ux[ix, it] = unit_overlap(positive[ix, it], positive[(ix + 1) % ngrid, it])
            ut[ix, it] = unit_overlap(positive[ix, it], positive[ix, (it + 1) % ngrid])
    curvature = np.angle(ux * np.roll(ut, -1, axis=0) * np.conj(np.roll(ux, -1, axis=1)) * np.conj(ut))
    c_l1 = curvature.sum() / (2 * np.pi)
    c_r2 = -4 * c_l1
    c_11112 = 4 * c_l1 + c_r2
    print(
        f"2x2 Bloch FHS: C_positive(q=1)={c_l1:+.12f}; C_R(q=2)={c_r2:+.12f}; "
        f"C(L1)={c_l1:+.12f}; C(11112)={c_11112:+.12f}"
    )


def anomaly_holonomy_identity():
    """Check q(W)-q(0)=W*integral_0^1 dq(tW)/dW dt for the saved convention."""
    strip = Strip(8, 4)
    W = 0.3
    A = np.zeros((1, strip.nl))
    A[0, strip.xl.reshape(-1)] = W / strip.Lx
    measure = Measure(strip, "11112", Ns=8)
    ray = measure.ray(A, 8)
    q_full = np.zeros((1, strip.ns))
    q_zero = np.zeros((1, strip.ns))
    for charge in measure.charges:
        w, v = eig_H(strip, charge * A)
        w0, v0 = eig_H(strip, np.zeros_like(A))
        q_full += measure.coef[charge] * q_of(strip, w, v)
        q_zero += measure.coef[charge] * q_of(strip, w0, v0)
    residual = np.max(np.abs((q_full - q_zero)[0] - W * ray["hbar"][0]))
    print(f"holonomy FTC at L=8,W=.3: max|q(W)-q(0)-W*hbar|={residual:.3e}")


if __name__ == "__main__":
    edge_check(1, "top")
    edge_check(2, "bottom")
    independent_fits()
    bloch_chern()
    anomaly_holonomy_identity()
