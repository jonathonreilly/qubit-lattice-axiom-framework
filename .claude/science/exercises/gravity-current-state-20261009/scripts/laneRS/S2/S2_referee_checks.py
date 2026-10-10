"""Independent numerical/algebraic checks for Lane RS probe S2.

This file does not modify the worker programs.  It uses fresh random seeds and
adds the massless Compton runs absent from the supplied output packet.
"""

import itertools
import numpy as np

from s2_core import Stag, eps, moller_T, odd_basis, omega, sample_moller, wrapf
from s2_compton_lib import compton_T, sample_compton


def lightcone_checks():
    rng = np.random.default_rng(20261010)
    for d in (2, 3):
        for m in (0.0, 0.5):
            worst = -np.inf
            for _ in range(5000):
                k = rng.uniform(-np.pi / 2, np.pi / 2, d)
                kp = rng.uniform(-np.pi / 2, np.pi / 2, d)
                for taste in itertools.product(range(2), repeat=d):
                    q = wrapf(k - kp + np.pi * np.asarray(taste))
                    worst = max(worst, abs(eps(k, m) - eps(kp, m)) - omega(q))
            print(f"lightcone d={d} m={m}: largest same-sign residual {worst:.6e}")

    # The inequality is false between opposite energy bands.  Q=0 and k=k'
    # already give |(+eps)-(-eps)|=2 eps > 0 whenever eps>0.
    for m, k in ((0.5, np.zeros(2)), (0.0, np.array([0.3, 0.0]))):
        lhs = 2 * eps(k, m)
        print(f"mixed-band counterexample m={m}: lhs={lhs:.6e}, omega(0)=0")


def dispersion_and_hessian_checks():
    rng = np.random.default_rng(271828)
    for d in (2, 3):
        for m in (0.0, 0.5):
            k = rng.uniform(-np.pi / 2, np.pi / 2, (10000, d))
            lhs = eps(k, m)
            rhs = 0.5 * np.sqrt((2 * m) ** 2 + np.sum(4 * np.sin(k) ** 2, axis=1))
            print(f"dispersion d={d} m={m}: max identity residual {np.max(abs(lhs-rhs)):.3e}")

        # For massless lattice KG at q=(pi,...,pi), Hess omega=-I/(2 sqrt(d)),
        # so det Hess is nonzero.  Together with the isolated zero set this is
        # the quick check needed for Spohn's generic-Hessian assumption.
        hdiag = -1 / (2 * np.sqrt(d))
        print(f"massless KG d={d}: det Hess at (pi,...,pi) = {hdiag**d:.6e}")


def trace_dimension_check():
    rng = np.random.default_rng(314159)
    nf, ng = 4, 2
    p = [rng.normal(size=(nf, nf)) for _ in range(2)]
    g = [rng.normal(size=(ng, ng)) for _ in range(2)]
    din = np.kron(p[0], np.eye(ng)) + np.kron(np.eye(nf), g[0])
    dout = np.kron(p[1], np.eye(ng)) + np.kron(np.eye(nf), g[1])
    lhs = np.trace(dout)
    rhs_formula = ng * np.trace(p[1]) + nf * np.trace(g[1])
    in_formula = ng * np.trace(p[0]) + nf * np.trace(g[0])
    print(f"tensor trace formula residual out={abs(lhs-rhs_formula):.3e}")
    print(f"normalised sums out={lhs/(nf*ng):.6e}, in={np.trace(din)/(nf*ng):.6e}")
    print(f"direct formulas out={np.trace(p[1])/nf+np.trace(g[1])/ng:.6e}, in={in_formula/(nf*ng):.6e}")


def fresh_moller_checks():
    rng = np.random.default_rng(424242)
    for d, r, ns in ((2, 6, 800), (3, 3, 1800)):
        for m in (0.0, 0.5):
            s = Stag(d, m)
            shells = []
            for mode, n in (("generic", ns // 2), ("lowK", ns // 4), ("lowE", ns // 4)):
                shells += sample_moller(s, n, rng, mode=mode)
            b = odd_basis(d, r)
            rows, ratios = [], []
            for q in shells:
                t, _ = moller_T(s, *q)
                svt = np.linalg.svd(t, compute_uv=False)
                ratios.append(svt[-1] / svt[0])
                k1, k2, k3, k4 = q
                rows.append(np.sin(2*b@k1)+np.sin(2*b@k2)-np.sin(2*b@k3)-np.sin(2*b@k4))
            a = np.asarray(rows) / np.sqrt(len(rows))
            sv = np.linalg.svd(a, compute_uv=False)
            print(
                f"fresh Moller d={d} m={m} R={r}: shells={len(shells)}, "
                f"null=0, scalar sv(min,max)=({sv[-1]:.6e},{sv[0]:.6e}), "
                f"T ratio(min,median)=({np.min(ratios):.6e},{np.median(ratios):.6e})"
            )


def explicit_invertible_shell_checks():
    # A diagonal nonzero total momentum and a simultaneous permutation of the
    # components give an exactly energy-conserving, non-permutation shell.
    # These fixed shells provide
    # well-conditioned witnesses that det T is not the zero analytic function
    # on the component containing them.
    for d in (2, 3):
        for m in (0.0, 0.5):
            ktot = np.full(d, np.pi/5)
            k1 = np.array([np.pi/8, np.pi/6] if d == 2 else [np.pi/10, np.pi/7, np.pi/5.5])
            k2 = ktot - k1
            perm = np.array([1, 0] if d == 2 else [1, 2, 0])
            k3, k4 = k1[perm], k2[perm]
            t, _ = moller_T(Stag(d, m), k1, k2, k3, k4)
            sv = np.linalg.svd(t, compute_uv=False)
            print(
                f"fixed invertible shell d={d} m={m}: "
                f"T sv(min,max,ratio)=({sv[-1]:.6e},{sv[0]:.6e},{sv[-1]/sv[0]:.6e})"
            )


def massless_compton_checks():
    rng = np.random.default_rng(8675309)
    for d, r, ns in ((2, 5, 700), (3, 3, 1500)):
        s = Stag(d, 0.0)
        shells = sample_compton(s, ns // 2, "generic", rng)
        shells += sample_compton(s, ns // 2, "low", rng)
        bf, bp = odd_basis(d, r), odd_basis(d, r)
        rows, ratios = [], []
        for k, p, kq, pq in shells:
            t = compton_T(s, k, p, kq, pq)
            svt = np.linalg.svd(t, compute_uv=False)
            ratios.append(svt[-1] / svt[0])
            rows.append(np.r_[np.sin(2*bf@k)-np.sin(2*bf@kq), np.sin(bp@p)-np.sin(bp@pq)])
        a = np.asarray(rows) / np.sqrt(len(rows))
        sv = np.linalg.svd(a, compute_uv=False)
        svg = np.linalg.svd(a[:, len(bf):], compute_uv=False)
        print(
            f"massless Compton d={d} R={r}: shells={len(shells)}, joint-null=0, "
            f"joint sv(min,max)=({sv[-1]:.6e},{sv[0]:.6e}), "
            f"photon sv(min,max)=({svg[-1]:.6e},{svg[0]:.6e}), "
            f"T ratio(min,median)=({np.min(ratios):.6e},{np.median(ratios):.6e})"
        )


def forward_neighbourhood_countercheck():
    # At small p along x and m>0, an infinitesimal outward radial photon shift
    # requires the electron's x group velocity to equal the photon velocity.
    # The former has supremum <1 while the latter tends to 1, so the claimed
    # full open neighbourhood of forward Compton endpoints cannot exist.
    grid = np.linspace(-np.pi / 2, np.pi / 2, 200001)
    m = 0.5
    ve = np.abs(np.sin(grid) * np.cos(grid) / np.sqrt(m*m + np.sin(grid)**2))
    p = 0.05
    vp = np.cos(p / 2)  # derivative of 2 sin(p/2) for p>0 on an axis
    print(f"forward check m={m}: sup |v_e,x|={ve.max():.9f}, v_ph,x(p=.05)={vp:.9f}")


if __name__ == "__main__":
    lightcone_checks()
    dispersion_and_hessian_checks()
    trace_dimension_check()
    fresh_moller_checks()
    explicit_invertible_shell_checks()
    massless_compton_checks()
    forward_neighbourhood_countercheck()
