"""Independent numerical checks for the lane-RG G3 referee.

The checks deliberately avoid modifying or importing the worker's numerical
results, except for using the same stated mathematical definitions.
"""

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.stats import qmc


PI = np.pi


def saw(x):
    return (x + PI) % (2 * PI) - PI


def w_nn(x):
    return 4 * np.sin(x / 2) ** 2


def w_slac(x):
    return saw(x) ** 2


print("== A. Fourier-algebra check of the separable continuity identities ==")
rng = np.random.default_rng(20261010)
for name, wfun in [("NN", w_nn), ("SLAC", w_slac)]:
    worst_e = 0.0
    worst_m = 0.0
    for _ in range(10000):
        a = rng.uniform(-PI, PI, 3)
        b = rng.uniform(-PI, PI, 3)
        qhat = 2 * np.sin((a + b) / 2)
        if np.min(np.abs(qhat)) < 1e-7:
            continue
        dw = wfun(a) - wfun(b)
        ratio = dw / (2 * qhat)
        wa = 1 + np.sum(wfun(a))
        wb = 1 + np.sum(wfun(b))
        energy_dot = (wa - wb) / 2
        div_p = -np.sum(qhat * ratio)
        worst_e = max(worst_e, abs(energy_dot + div_p))
        for j in range(3):
            p_dot = -0.5j * ratio[j] * (wa - wb)
            div_t = 1j * np.sum(qhat * ratio * ratio[j])
            worst_m = max(worst_m, abs(p_dot + div_t))
    print(f"{name}: max absolute algebra residual E={worst_e:.3e}, M={worst_m:.3e}")


print("\n== B. SLAC bilocal coefficient tails (L=1025) ==")
L = 1025
k = 2 * PI * np.fft.fftfreq(L)
a = k[:, None]
b = k[None, :]
q = a + b
qhat = 2 * np.sin(q / 2)
with np.errstate(divide="ignore", invalid="ignore"):
    ratio = (w_slac(a) - w_slac(b)) / (2 * qhat)
bad = np.abs(qhat) < 1e-12
ratio[bad] = np.broadcast_to(saw(a), ratio.shape)[bad]
pcoef = np.fft.fft2(1j * ratio * np.exp(1j * q / 2)) / L**2
tcoef = np.fft.fft2(ratio**2) / L**2
y = np.fft.fftfreq(L) * L
dp = np.maximum(np.abs(y[:, None] - 0.5), np.abs(y[None, :] - 0.5))
dt = np.maximum(np.abs(y[:, None]), np.abs(y[None, :]))
rs = np.array([16, 32, 64, 128, 256], dtype=float)
pmax = []
tmax = []
ptail = []
for radius in rs.astype(int):
    pmax.append(np.max(np.abs(pcoef)[(dp >= radius - 0.5) & (dp < radius + 0.5)]))
    tmax.append(np.max(np.abs(tcoef)[(dt >= radius - 0.5) & (dt < radius + 0.5)]))
    ptail.append(np.sum(np.abs(pcoef)[dp >= radius]))
    print(
        f"R={radius:3d}: maxP={pmax[-1]:.8e}, maxT={tmax[-1]:.8e}, "
        f"sumP(>=R)={ptail[-1]:.8e}"
    )
pmax = np.asarray(pmax)
tmax = np.asarray(tmax)
print(f"P fit R=16..128: {np.polyfit(np.log(rs[:4]), np.log(pmax[:4]), 1)[0]:.4f}")
print(f"T fit R=16..128: {np.polyfit(np.log(rs[:4]), np.log(tmax[:4]), 1)[0]:.4f}")
print(f"T fit R=64..256: {np.polyfit(np.log(rs[2:]), np.log(tmax[2:]), 1)[0]:.4f}")
print("successive P-tail drops per doubling:", " ".join(f"{x:.4f}" for x in -np.diff(ptail)))


print("\n== C. Fixed-zone E-channel Hessian from the analytic integrand ==")
nq = 60
xg, wg = leggauss(nq)
kk = PI * xg
ww = PI * wg
kx, ky, kz = np.meshgrid(kk, kk, kk, indexing="ij")
weight3 = ww[:, None, None] * ww[None, :, None] * ww[None, None, :]
for mass in [0.0, 0.5, 1.0]:
    omega = np.sqrt(mass**2 + kx**2 + ky**2 + kz**2)
    second = 2 * (kx**2 + ky**2) / omega - (kx**2 - ky**2) ** 2 / omega**3
    mu = 0.5 * np.sum(weight3 * second) / (2 * PI) ** 3
    print(f"m={mass:.1f}: mu_E={mu:+.9f}")


def flow_t2(momentum, eps, nsteps=16):
    x = momentum[..., 0].copy()
    y = momentum[..., 1].copy()
    step = 1.0 / nsteps
    for _ in range(nsteps):
        xm = saw(x + 0.5 * step * eps * saw(y))
        ym = saw(y + 0.5 * step * eps * saw(x))
        x = saw(x + step * eps * saw(ym))
        y = saw(y + step * eps * saw(xm))
    out = momentum.copy()
    out[..., 0] = x
    out[..., 1] = y
    return out


def basketball_weight(momentum, dispersion):
    if dispersion == "SLAC":
        omega = np.sqrt(1 + np.sum(saw(momentum) ** 2, axis=-1))
    else:
        omega = np.sqrt(1 + 4 * np.sum(np.sin(momentum / 2) ** 2, axis=-1))
    return 1 / (omega.sum(axis=1) * np.prod(2 * omega, axis=1))


print("\n== D. Continuum-first QMC check of the saw-flow I4 class Hessians ==")
print("Each row is one independently scrambled 2^17-point Sobol integral.")
for dispersion in ["KG", "SLAC"]:
    estimates = {0.02: [], 0.04: []}
    for seed in [1, 2, 3, 4]:
        unit = qmc.Sobol(9, scramble=True, seed=seed).random_base2(17)
        k123 = ((2 * unit - 1) * PI).reshape(-1, 3, 3)
        k4 = saw(-k123.sum(axis=1))
        momenta = np.concatenate([k123, k4[:, None, :]], axis=1)
        winding = np.rint(momenta.sum(axis=1) / (2 * PI)).astype(int)
        normal = np.all(winding == 0, axis=1)
        w0 = basketball_weight(momenta, dispersion)
        for eps in estimates:
            wp = basketball_weight(flow_t2(momenta, eps), dispersion)
            wm = basketball_weight(flow_t2(momenta, -eps), dispersion)
            delta = 0.5 * (wp + wm) - w0
            mu_n = -np.mean(np.where(normal, delta, 0.0)) / (12 * eps**2)
            mu_u = -np.mean(np.where(~normal, delta, 0.0)) / (12 * eps**2)
            estimates[eps].append((mu_n, mu_u))
    print(dispersion)
    for eps, rows in estimates.items():
        rows = np.asarray(rows)
        mean = rows.mean(axis=0)
        spread = rows.std(axis=0, ddof=1)
        print(
            f"eps={eps:.2f}: mu_N={mean[0]:+.6e} (scramble sd {spread[0]:.1e}), "
            f"mu_U={mean[1]:+.6e} (scramble sd {spread[1]:.1e})"
        )


print("\n== E. Readout arithmetic ==")
for bound in [5.7e-99, 9.0e-102, 1.0e-99]:
    print(
        f"B={bound:.1e}: sqrt(B)={np.sqrt(bound):.6e}, "
        f"n_quad={0.5 * np.log(1 / bound):.6f}/c, n_linear={np.log(1 / bound):.6f}/c"
    )
absolute_bound = 1.08e-104
for coeff in [3.4e-6, 4.3e-6]:
    epsmax = np.sqrt(absolute_bound / coeff)
    print(f"mu_U={coeff:.1e} lambda^2: epsmax={epsmax:.6e}/|lambda|, n={-np.log(epsmax):.6f}/c+ln|lambda|/c")
floor = 2.8e-6
print(f"floor/reduced-cell bound={floor / (1.2e-3 * 5.7e-99):.6e}")
print(f"floor/nonreduced-cell bound={floor / absolute_bound:.6e}")
