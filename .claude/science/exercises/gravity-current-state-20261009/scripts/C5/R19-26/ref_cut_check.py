"""Independent numerical checks for C5/R19-16.

This script deliberately does not call lib199.w1_resid, the worker's seam
runner, or the old eigenprojector Sylvester implementation for its load-bearing
checks.  It also probes the q-wrap cut, which is absent from the worker's line
scans.
"""

import warnings

import mpmath as mp
import numpy as np
from scipy.linalg import solve_sylvester

import lib1916 as R


L = R.L
RADIUS = 0.1
RNG = np.random.default_rng(191616)


def transverse_frame(k):
    """Independent 6x4 transverse frame."""
    s = L.sig(k)
    _, _, vh = np.linalg.svd(s.reshape(1, 3), full_matrices=True)
    e = vh[1:].T
    q = np.zeros((6, 4))
    q[:3, :2] = e
    q[3:, 2:] = e
    return q


def raw_w1(k1, k2):
    """Return the four unprojected W1 residual matrices and the kernel."""
    m = L.glued(k1, k2, RADIUS)
    h1, h2 = L.hmat(L.sig(k1)), L.hmat(L.sig(k2))
    d = L.dsym(L.wrap(k1 - k2))
    raw = [
        h1 @ m[0, nu]
        - m[0, nu] @ h2
        - sum(d[j] * m[1 + j, nu] for j in range(3))
        for nu in range(4)
    ]
    return raw, m


def independent_seam_and_zero():
    midpoint = np.array([3.05, 1.0, 0.7])
    k1, k2 = midpoint.copy(), midpoint.copy()
    k1[0] += 9.99e-8 / 2
    k2[0] -= 9.99e-8 / 2
    raw, _ = raw_w1(k1, k2)
    q1, q2 = transverse_frame(k1), transverse_frame(k2)
    seam = max(np.max(np.abs(q1.T @ x @ q2)) for x in raw)

    z = np.zeros(3)
    hard = np.array([0.9, -1.3, 0.4])
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        raw0, m0 = raw_w1(z, hard)
    qh = transverse_frame(hard)
    zero = max(np.max(np.abs(x @ qh)) for x in raw0)
    print(
        "independent W1: seam %.3e; exact-zero full-left x transverse-right "
        "%.3e; finite %s; warnings %d"
        % (seam, zero, np.isfinite(m0).all(), len(caught))
    )

    direction = np.array([0.3, -0.4, 0.5])
    direction /= np.linalg.norm(direction)
    diffs = []
    for eps in (1e-6, 1e-8, 1e-10):
        me = L.glued(eps * direction, hard, RADIUS)
        diffs.append(np.max(np.abs(me - m0)))
    print("exact-zero directional limit eps=1e-6,1e-8,1e-10:", diffs)


def sstep_mp(x):
    if x <= 0:
        return mp.mpf("0")
    if x >= 1:
        return mp.mpf("1")
    a = mp.exp(-1 / x)
    b = mp.exp(-1 / (1 - x))
    return a / (a + b)


def d_mp(x):
    b = mp.mpf(str(R.BG))
    width = mp.pi - b
    x = abs(mp.mpf(str(x)))
    if x <= b:
        return x
    return x - width * mp.quad(sstep_mp, [0, (x - b) / width])


def independent_r0_r1():
    mp.mp.dps = 60
    points = [0.0, R.BG, 0.5 * (R.BG + np.pi), np.pi]
    law_err = max(
        abs(float(R.d_exact(np.array([x]))[0]) - float(d_mp(x))) for x in points
    )
    print("R0 stated-law max error at 0,b,(b+pi)/2,pi: %.3e" % law_err)

    # Equality with the defining quotient away from its removable zero.
    quotient_err = 0.0
    for _ in range(200):
        k2 = RNG.uniform(-np.pi, np.pi)
        q = RNG.choice((-1.0, 1.0)) * RNG.uniform(1e-3, np.pi - 1e-3)
        k1 = float(L.wrap(np.array([k2 + q]))[0])
        qw = float(L.wrap(np.array([k1 - k2]))[0])
        direct = (
            float(R.sig(np.array([k1]))[0]) ** 2
            - float(R.sig(np.array([k2]))[0]) ** 2
        ) / float(L.dsym(np.array([qw]))[0])
        quotient_err = max(quotient_err, abs(R.dd1(k1, k2) - direct))
    k = 3.05
    zero_limit = abs(
        R.dd1(k, k)
        - 2 * float(R.sig(np.array([k]))[0]) * float(R.cfun(np.array([k]))[0])
    )
    print(
        "R1 defining quotient (200 nonsingular pairs) max error %.3e; q=0 limit error %.3e"
        % (quotient_err, zero_limit)
    )

    # The endpoints below differ by only 2 eps in an ordinary interior k1
    # coordinate chart, but their wrapped momentum transfers approach +pi and
    # -pi.  A smooth function of (k1,k2) must have a common limit here.
    base = 0.4
    fixed = np.array([base, 1.0, 0.7])
    for eps in (1e-4, 1e-6, 1e-8, 1e-10):
        xa = float(L.wrap(np.array([base + np.pi - eps]))[0])
        xb = float(L.wrap(np.array([base - np.pi + eps]))[0])
        ka = np.array([xa, 1.0, 0.7])
        kb = np.array([xb, 1.0, 0.7])
        raw_a, ma = raw_w1(ka, fixed)
        raw_b, mb = raw_w1(kb, fixed)
        qa, qb = transverse_frame(ka), transverse_frame(kb)
        w1a = max(np.max(np.abs(qa.T @ x @ transverse_frame(fixed))) for x in raw_a)
        w1b = max(np.max(np.abs(qb.T @ x @ transverse_frame(fixed))) for x in raw_b)
        print(
            "q-wrap eps %.0e: |dk1| %.3e; Delta limits %+.9e %+.9e; "
            "kernel jump %.9e (M00 %.3e, M02 %.9e, projected M02 %.9e); "
            "W1 sides %.2e %.2e"
            % (
                eps,
                abs(xa - xb),
                R.dd1(xa, base),
                R.dd1(xb, base),
                np.max(np.abs(ma - mb)),
                np.max(np.abs(ma[0, 0] - mb[0, 0])),
                np.max(np.abs(ma[0, 2] - mb[0, 2])),
                np.max(
                    np.abs(
                        L.projs(ka)[4] @ ma[0, 2] @ L.projs(fixed)[4]
                        - L.projs(kb)[4] @ mb[0, 2] @ L.projs(fixed)[4]
                    )
                ),
                w1a,
                w1b,
            )
        )


def independent_soft_solve(source, k1, k2, left_full):
    """Solve the supported Sylvester problem in transverse bases."""
    h1, h2 = L.hmat(L.sig(k1)), L.hmat(L.sig(k2))
    if left_full:
        q2 = transverse_frame(k2)
        h2t = q2.T @ h2 @ q2
        y = solve_sylvester(h1, -h2t, source @ q2)
        return y @ q2.T
    q1 = transverse_frame(k1)
    h1t = q1.T @ h1 @ q1
    z = solve_sylvester(h1t, -h2, q1.T @ source)
    return q1 @ z


def independent_r2():
    worst = 0.0
    for left in (True, False):
        for _ in range(30):
            soft = RNG.normal(size=3)
            soft *= RNG.uniform(1e-6, RADIUS / 8) / np.linalg.norm(soft)
            hard = RNG.normal(size=3)
            hard *= RNG.uniform(RADIUS / 2, 2.5) / np.linalg.norm(hard)
            k1, k2 = (soft, hard) if left else (hard, soft)
            msp = L.spatial_VW(k1, k2)
            d = L.dsym(L.wrap(k1 - k2))
            source = np.einsum("i,iab->ab", d, msp[:, 1])
            got = R.neumann_left(source, k1, k2) if left else R.neumann_right(source, k1, k2)
            ref = independent_soft_solve(source, k1, k2, left)
            worst = max(worst, np.max(np.abs(got - ref)))

    hard = np.array([0.9, -1.3, 0.4])
    z = np.zeros(3)
    source = RNG.normal(size=(6, 6))
    h2, w2, pp2, pm2, _, _ = L.projs(hard)
    hp2 = (pp2 - pm2) / w2
    left_err = np.max(np.abs(R.neumann_left(source, z, hard) + source @ hp2))
    h1, w1, pp1, pm1, _, _ = L.projs(hard)
    hp1 = (pp1 - pm1) / w1
    right_err = np.max(np.abs(R.neumann_right(source, hard, z) - hp1 @ source))
    print(
        "R2 vs independent transverse-basis Sylvester max abs %.3e; exact-zero formula errors %.3e %.3e"
        % (worst, left_err, right_err)
    )


if __name__ == "__main__":
    independent_seam_and_zero()
    independent_r0_r1()
    independent_r2()
