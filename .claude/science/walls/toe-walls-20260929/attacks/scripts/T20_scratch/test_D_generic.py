"""Test D (route R2, drop rotation covariance): random nearest-neighbour translation-invariant 2-band laws
H(k) = d0 + d(k).sigma, d(k) = c + sum_mu (a_mu cos k_mu + b_mu sin k_mu), a_mu,b_mu,c in R^3 (no symmetry).
Are Weyl nodes (charge +-1) generic, and how isotropic are they?"""
import numpy as np
from scipy.optimize import fsolve

rng = np.random.default_rng(11)


def make():
    a = rng.normal(size=(3, 3)); b = rng.normal(size=(3, 3)); c = rng.normal(size=3) * 1.0
    return a, b, c


def d(k, a, b, c):
    return c + (a * np.cos(k)[:, None]).sum(0) + (b * np.sin(k)[:, None]).sum(0)


def J(k, a, b, c):
    # J[i, m] = d d_i / d k_m = -a[m,i] sin k_m + b[m,i] cos k_m
    return np.array([[-a[m, i] * np.sin(k[m]) + b[m, i] * np.cos(k[m]) for m in range(3)] for i in range(3)])


def nodes(a, b, c, starts=120):
    out = []
    for _ in range(starts):
        k0 = rng.uniform(-np.pi, np.pi, 3)
        k, info, ier, msg = fsolve(lambda k: d(k, a, b, c), k0, fprime=lambda k: J(k, a, b, c), full_output=True, xtol=1e-13)
        if ier == 1 and np.linalg.norm(d(k, a, b, c)) < 1e-10:
            k = (k + np.pi) % (2 * np.pi) - np.pi
            if not any(np.linalg.norm(((k - q + np.pi) % (2 * np.pi)) - np.pi) < 1e-6 for q in out):
                out.append(k)
    return out


N = 400
have = 0; tot_zero = 0; conds = []; counts = []; charges_ok = 0; abs_charge_one = 0
for t in range(N):
    a, b, c = make()
    ns = nodes(a, b, c)
    if ns:
        have += 1
        ch = [int(np.sign(np.linalg.det(J(k, a, b, c)))) for k in ns]
        sv = [np.linalg.svd(J(k, a, b, c), compute_uv=False) for k in ns]
        counts.append(len(ns))
        tot_zero += (sum(ch) == 0)
        abs_charge_one += all(abs(x) == 1 for x in ch)
        conds += [s[0] / s[-1] for s in sv]
print(f"random NN 2-band laws without covariance: {N} samples")
print(f"  with isolated linear nodes: {have} ({100*have/N:.0f}%)")
print(f"  of those: every node has charge +-1 (nonsingular Jacobian): {abs_charge_one}/{have}; total charge zero: {tot_zero}/{have}")
print(f"  node counts (median, min, max): {int(np.median(counts))}, {min(counts)}, {max(counts)}")
print(f"  velocity-matrix condition numbers sigma_max/sigma_min: median {np.median(conds):.2f}, 10th pct {np.percentile(conds,10):.2f}, 90th pct {np.percentile(conds,90):.2f}  (1.00 would be an isotropic cone)")
