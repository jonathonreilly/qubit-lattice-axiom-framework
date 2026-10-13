"""Independent checks for C5 R19-26.

This does not import any r1926_* checker.  It reconstructs the stress-placement
and field-position phases from the stated R9-9/R19-9 conventions, contracts W1
in independently generated transverse frames, and performs a fresh Fourier
test on a line not used in the worker's scripts.
"""

import sys

import numpy as np

import lib1926 as R


L = R.L
RADIUS = 0.1

# True positions of the rotated fields (E_x,E_y,E_z,B_x,B_y,B_z).
FIELD_POS = np.array(
    [
        [0.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.0, 0.5],
        [0.0, 0.5, 0.5],
        [0.5, 0.0, 0.5],
        [0.5, 0.5, 0.0],
    ]
)

# R9-9 stress placements p_{mu nu}=(e_mu+e_nu)/2, e_0=0.
STRESS_POS = np.zeros((4, 4, 3))
for mu in range(4):
    for nu in range(4):
        if mu:
            STRESS_POS[mu, nu, mu - 1] += 0.5
        if nu:
            STRESS_POS[mu, nu, nu - 1] += 0.5


def transverse_frame(k):
    """Orthonormal E/B transverse frame, independent of lib199.projs."""
    s = L.sig(k)
    _, _, vh = np.linalg.svd(s.reshape(1, 3), full_matrices=True)
    e = vh[1:].T
    q = np.zeros((6, 4))
    q[:3, :2] = e
    q[3:, 2:] = e
    return q


def periodic_gauge_symbol(q, k2):
    """Ordinary periodic-cell symbol after restoring placement and field phases."""
    k1 = L.wrap(k2 + q)
    m = L.glued(k1, k2, RADIUS)
    left = np.exp(1j * (FIELD_POS @ k1))
    right = np.exp(-1j * (FIELD_POS @ k2))
    placement = np.exp(-1j * np.einsum("mna,a->mn", STRESS_POS, q))
    return placement[:, :, None, None] * left[None, None, :, None] * m * right[None, None, None, :]


def placement_lemma_check():
    # A finite toy cell symbol b(q) is periodic.  Its placement-stripped
    # representative is exp(+iq p)b(q), hence changes by exp(2 pi i p).
    eps = 1e-9
    for p in (0.0, 0.5, 1.0):
        b_plus = 1.0 + 0.2 * np.cos(np.pi - eps)
        b_minus = 1.0 + 0.2 * np.cos(-np.pi + eps)
        mt_plus = np.exp(1j * (np.pi - eps) * p) * b_plus
        mt_minus = np.exp(1j * (-np.pi + eps) * p) * b_minus
        ratio = mt_plus / mt_minus
        restored_jump = abs(np.exp(-1j * (np.pi - eps) * p) * mt_plus - np.exp(-1j * (-np.pi + eps) * p) * mt_minus)
        print(
            "toy p=%3.1f: Mtilde(+pi)/Mtilde(-pi)=%+.9f%+.9fi; restored jump %.2e"
            % (p, ratio.real, ratio.imag, restored_jump)
        )


def stencil_check():
    qs = np.linspace(-np.pi, np.pi, 1001)
    lhs = np.exp(-0.5j * qs) * R.Fplace(qs)
    rhs = (9.0 / 16.0) * (1.0 + np.exp(-1j * qs)) - (1.0 / 16.0) * (
        np.exp(1j * qs) + np.exp(-2j * qs)
    )
    # Keep h large enough to avoid fourth-difference cancellation in float64.
    h = 2e-2
    q4_coeff = (R.Fplace(h) - 1.0) / h**4
    print("F stencil identity max error %.2e; numerical q^4 coefficient %.9f (target %.9f)" % (
        np.max(np.abs(lhs - rhs)), q4_coeff, -3.0 / 128.0
    ))


def cut_and_w1_check():
    k2 = np.array([0.4, 1.0, 0.7])
    eps = 1e-8
    ka = np.array([L.wrap(np.array([0.4 + np.pi - eps]))[0], 1.0, 0.7])
    kb = np.array([L.wrap(np.array([0.4 - np.pi + eps]))[0], 1.0, 0.7])
    q2 = transverse_frame(k2)
    for patched in (False, True):
        (R.patch if patched else R.unpatch)()
        ma, mb = L.glued(ka, k2, RADIUS), L.glued(kb, k2, RADIUS)
        qa, qb = L.wrap(ka - k2), L.wrap(kb - k2)
        ga = periodic_gauge_symbol(qa, k2)
        gb = periodic_gauge_symbol(qb, k2)
        qfa, qfb = transverse_frame(ka), transverse_frame(kb)
        w1 = 0.0
        for k1, m, qf in ((ka, ma, qfa), (kb, mb, qfb)):
            h1, h2 = L.hmat(L.sig(k1)), L.hmat(L.sig(k2))
            d = L.dsym(L.wrap(k1 - k2))
            for nu in range(4):
                resid = h1 @ m[0, nu] - m[0, nu] @ h2
                resid -= sum(d[j] * m[1 + j, nu] for j in range(3))
                w1 = max(w1, np.abs(qf.T @ resid @ q2).max())
        print(
            "%s: raw jump %.9e; restored-periodic jump %.9e; projected M02 raw %.9e; independent W1 %.2e"
            % (
                "repaired" if patched else "R19-16",
                np.abs(ma - mb).max(),
                np.abs(ga - gb).max(),
                np.abs(qfa.T @ ma[0, 2] @ q2 - qfb.T @ mb[0, 2] @ q2).max(),
                w1,
            )
        )
    R.patch()


def covariance_check():
    rotations = (
        np.array([[0.0, -1, 0], [1, 0, 0], [0, 0, 1]]),
        np.array([[0.0, 0, 1], [1, 0, 0], [0, 1, 0]]),
        np.array([[0.0, 1, 0], [1, 0, 0], [0, 0, -1]]),
    )
    rng = np.random.default_rng(2601)
    worst = 0.0
    for rot in rotations:
        lor = np.eye(4)
        lor[1:, 1:] = rot
        field_rot = np.kron(np.eye(2), rot)
        for _ in range(80):
            k1, k2 = rng.uniform(-np.pi, np.pi, (2, 3))
            lhs = L.glued(rot @ k1, rot @ k2, RADIUS)
            rhs = np.einsum(
                "ma,nb,xy,abyz,wz->mnxw",
                lor,
                lor,
                field_rot,
                L.glued(k1, k2, RADIUS),
                field_rot,
            )
            worst = max(worst, np.abs(lhs - rhs).max())
    print("fresh cubic covariance max error %.2e" % worst)


def fourier_check(npoints):
    # This line and seed are different from every worker Fourier script.
    k2 = np.array([-1.713, 0.842, 2.177])
    q_other = np.array([0.0, 1.431, -2.019])
    qs = -np.pi + 2 * np.pi * (np.arange(npoints) + 0.5) / npoints
    bands = ((32, 64), (128, 256), (512, min(900, npoints // 2 - 1)))
    for patched in (False, True):
        (R.patch if patched else R.unpatch)()
        vals = []
        for qx in qs:
            q = q_other.copy()
            q[0] = qx
            vals.append(periodic_gauge_symbol(q, k2))
        coeff = np.fft.fft(np.asarray(vals), axis=0) / npoints
        amp = np.abs(coeff).reshape(npoints, -1).max(axis=1)
        out = []
        for lo, hi in bands:
            if hi <= lo:
                continue
            a = max(amp[lo : hi + 1].max(), amp[npoints - hi : npoints - lo + 1].max())
            out.append("[%d,%d] %.3e" % (lo, hi, a))
        print(("repaired" if patched else "R19-16") + " Fourier bands: " + "; ".join(out))
    R.patch()


if __name__ == "__main__":
    npoints = int(sys.argv[1]) if len(sys.argv) > 1 else 2048
    R.patch()
    placement_lemma_check()
    stencil_check()
    cut_and_w1_check()
    covariance_check()
    fourier_check(npoints)
