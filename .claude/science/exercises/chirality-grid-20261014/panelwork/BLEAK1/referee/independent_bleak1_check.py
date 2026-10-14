"""Independent low-memory checks for BLEAK-1.

This does not import the worker's code.  It checks the exact three-dimensional
integrand left after the k4 integral, its two integration-by-parts identities,
the limiting value -1/96, and the static-pull coupling normalization.
"""

import math
import numpy as np


def shat(x):
    return 2.0 * np.sin(0.5 * x)


def stress_vertex(p1, p2, d2=False):
    """Scalar-stress bilinear obtained directly from the displayed K2 stress."""
    s1, s2 = shat(p1), shat(p2)
    c1, c2 = np.cos(0.5 * p1), np.cos(0.5 * p2)
    out = np.zeros((4, 4))
    for mu in range(4):
        for nu in range(4):
            if mu != nu:
                out[mu, nu] = -0.5 * (
                    s1[mu] * c1[nu] * s2[nu] * c2[mu]
                    + s2[mu] * c2[nu] * s1[nu] * c1[mu]
                )
        out[mu, mu] = -0.5 * s1[mu] * s2[mu] * np.cos(0.5 * (p1[mu] - p2[mu]))
        for rho in range(4):
            if rho != mu:
                out[mu, mu] += 0.5 * np.cos(0.5 * (p1[rho] + p2[rho])) * s1[rho] * s2[rho]
    if d2:
        out[3, 3] += 0.25 * s1[3] ** 2 * s2[3] ** 2
    return out


def u_formula(k, alpha):
    s, c = shat(k), np.cos(0.5 * k)
    out = np.zeros((4, 4))
    for mu in range(4):
        out[mu, mu] = math.sin(k[alpha]) * (0.5 - (mu == alpha))
        for nu in range(4):
            if mu != nu:
                out[mu, nu] = -0.5 * (
                    (alpha == mu) * s[nu] * c[mu]
                    + (alpha == nu) * s[mu] * c[nu]
                )
    return out


print("Vertex/O(p^2) extraction:")
print("U^a_mm=(1/2-delta_am) sin(k_a)")
print("U^a_mn=-[delta_am shat(k_n)c_m+delta_an shat(k_m)c_n]/2 (m!=n)")
rng = np.random.default_rng(14031933)
fd_error = 0.0
tt_norm = 0.0
ward_error = 0.0
eps = 1.0e-6
for _ in range(100):
    k = rng.uniform(-math.pi, math.pi, 4)
    q = shat(k[:3])
    theta = np.eye(3) - np.outer(q, q) / np.dot(q, q)
    for alpha in range(4):
        e = np.zeros(4)
        e[alpha] = eps
        for d2 in (False, True):
            fd = (stress_vertex(e, k, d2) - stress_vertex(-e, k, d2)) / (2.0 * eps)
            fd_error = max(fd_error, np.max(np.abs(fd - u_formula(k, alpha))))
        u = u_formula(k, alpha)
        usp = u[:3, :3]
        utt = theta @ usp @ theta - 0.5 * theta * np.trace(theta @ usp)
        tt_norm = max(tt_norm, np.max(np.abs(utt)))
        lhs = shat(k) @ u
        rhs = -0.5 * np.dot(shat(k), shat(k)) * np.eye(4)[alpha] * np.cos(0.5 * k)
        ward_error = max(ward_error, np.max(np.abs(lhs - rhs)))
print("finite-difference error (K2 and D2) = %.2e" % fd_error)
print("max spatial-TT projection of U = %.2e" % tt_norm)
print("off-shell Ward-identity error = %.2e" % ward_error)
print("D2 starts quadratically in the external momentum, so its first derivative U is unchanged.\n")


def midpoint_integrals(m):
    """Integrate one q1 slice at a time; peak arrays are O(m^2)."""
    q = (np.arange(m, dtype=float) + 0.5) * math.pi / m
    q2, q3 = np.meshgrid(q, q, indexing="ij")
    s2sq = shat(q2) ** 2
    s3sq = shat(q3) ** 2
    totals = np.zeros(5)
    for q1 in q:
        s1sq = shat(q1) ** 2
        Q = s1sq + s2sq + s3sq
        tau = s1sq**2 + s2sq**2 + s3sq**2
        R = 1.0 / np.sqrt(Q * (Q + 4.0))
        d = 1.0 / (16.0 * Q) + tau / (32.0 * Q**2) - 1.0 / 6.0 + Q * R / 6.0
        totals += (
            d.sum(),
            (1.0 / Q).sum(),
            (Q * R).sum(),
            (tau / Q**2).sum(),
            Q.size,
        )
    return totals[:4] / totals[4]


def extrapolate(ms, vals):
    x = 1.0 / np.asarray(ms, dtype=float)
    a = np.column_stack((np.ones_like(x), x, x**2, x**3))
    return np.linalg.solve(a, np.asarray(vals, dtype=float))[0]


print("Exact algebra after the k4 average:")
print("d(q) = 1/(16Q) + sum_i(shat(q_i)^4)/(32Q^2) - 1/6 + Q/sqrt(Q(Q+4))/6")
print("IBP: <tau/Q^2> = 1 - 2 W3; hypercubic symmetry: <Q R> = 3/4")
print("Therefore <d> = W3/16 + (1-2W3)/32 - 1/6 + (3/4)/6")
print("              = 1/32 - 1/24 = -1/96")

ms = (32, 64, 128, 256)
rows = []
for m in ms:
    row = midpoint_integrals(m)
    rows.append(row)
    print(
        "M=%3d  <d>=%+.12f  W3=%.12f  <QR>=%.12f  <tau/Q^2>=%.12f"
        % (m, row[0], row[1], row[2], row[3])
    )

rows = np.asarray(rows)
limit = extrapolate(ms, rows[:, 0])
print("Richardson <d> = %+.12f; exact -1/96 = %+.12f" % (limit, -1.0 / 96.0))
print("-16*pi*<d> = %.12f; exact pi/6 = %.12f" % (-16.0 * math.pi * limit, math.pi / 6.0))

print("\nStatic normalization:")
print("V(r) = -2 lambda M1 M2/(4 pi r), so G_N = lambda/(2 pi)")
print("lambda=kappa_R^2/4 gives kappa_R^2=8 pi G_N")
print("kappa_can=2 kappa_R (coupling -kappa_can h.T/2), hence kappa_can^2=32 pi G_N")
print("S_int=-kappa_R^2 D/2=-4 pi G_N D; 8 exchange contractions give -32 pi G_N D")
