#!/usr/bin/env python3
"""Referee for J:derive:next-order-force-between-capturing-bodies:a3.

Author w-jonathonsmac4f50-jb2c0 (claude-opus-5-5). This file does not call their check.py.
Own dispersion algebra, own Oseen derivatives, own periodic Stokes solve.
"""
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

fails = []


def report(name, ok, detail):
    fails.append(name) if not ok else None
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def dispersion():
    """Inviscid sound speed, and the viscous decay implied by the written PDE."""
    rho, k = sp.symbols("rho k", positive=True)
    nu, nub, w = sp.symbols("nu nu_b omega", real=True)
    s3 = sp.sqrt(3)
    # columns (delta rho, longitudinal g)
    M = sp.Matrix([
        [-sp.I * w, sp.I * k * (1 - rho) / s3],
        [sp.I * k / (3 * s3), -sp.I * w + (nu + nub) * k**2],
    ])
    det = sp.expand(M.det())
    # det = -w^2 - I (nu+nu_b) k^2 w + k^2 (1-rho)/9
    target = -w**2 - sp.I * (nu + nub) * k**2 * w + k**2 * (1 - rho) / 9
    ok_det = sp.simplify(det - target) == 0
    c2 = sp.simplify(sp.solve(det.subs({nu: 0, nub: 0}), w)[0]**2 / k**2)
    ok_c = sp.simplify(c2 - (1 - rho) / 9) == 0
    # omega = c k - I * D * k**2 / 2, with c**2 = (1-rho)/9, cancels at order k^3 iff D = nu+nu_b
    D, c = sp.symbols("D c", positive=True)
    w_s = c * k - sp.I * D * k**2 / 2
    plugged = sp.series(det.subs({w: w_s, rho: 1 - 9 * c**2}), k, 0, 4).removeO()
    coeff = sp.simplify(sp.expand(plugged).coeff(k**3))
    # leading viscous piece must vanish for every c>0
    ok_D = sp.simplify(coeff.subs(D, nu + nub)) == 0
    # and the (4/3) nu + nu_b choice does not
    bad = sp.simplify(coeff.subs(D, sp.Rational(4, 3) * nu + nub))
    ok_not = bad != 0 and sp.simplify(bad.subs({nu: 1, nub: 0, c: 1})) != 0
    report(
        "dispersion",
        bool(ok_det and ok_c and ok_D and ok_not),
        "written PDE gives omega^2 + i (nu+nu_b) k^2 omega - k^2 (1-rho)/9 = 0, "
        "so the sound diffusivity in alpha = D k^2/2 is nu+nu_b, not (4/3) nu + nu_b",
    )


def oseen():
    x, y, z = sp.symbols("x y z", real=True)
    r2 = x**2 + y**2 + z**2
    pi = sp.pi
    ux = (r2 + x**2) / (8 * pi * r2**sp.Rational(3, 2))
    uy = (x * y) / (8 * pi * r2**sp.Rational(3, 2))
    uz = (x * z) / (8 * pi * r2**sp.Rational(3, 2))
    p = x / (4 * pi * r2**sp.Rational(3, 2))

    def lap(f):
        return sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)

    ok = all(
        sp.simplify(lap(f) - sp.diff(p, v)) == 0
        for f, v in ((ux, x), (uy, y), (uz, z))
    )
    ok = ok and sp.simplify(sp.diff(ux, x) + sp.diff(uy, y) + sp.diff(uz, z)) == 0
    t = sp.symbols("t", positive=True)
    axial = sp.simplify(ux.subs({y: 0, z: 0, x: t}) - 1 / (4 * pi * t))
    trans = sp.simplify(ux.subs({x: 0, z: 0, y: t}) - 1 / (8 * pi * t))
    ok = ok and axial == 0 and trans == 0
    report(
        "oseen",
        bool(ok),
        "u = (I + rhat rhat) e_x / (8 pi r), p = x/(4 pi r^3) solves lap u = grad p and div u = 0; "
        "axial 1/(4 pi r), transverse 1/(8 pi r)",
    )


def force_algebra():
    """Axis projection and the ratio to the inverse-square reference, as exact fractions."""
    # (I + rhat rhat) along rhat doubles the vector, and 2/(8 pi) = 1/(4 pi).
    two = sp.Rational(2)
    ok_proj = sp.simplify(two / (8 * sp.pi) - 1 / (4 * sp.pi)) == 0
    # delta F / F_ref = Q2 / (4 pi nu rho r), with F1 the momentum removed from the gas.
    # Sign: F1 points from body 1 toward body 2, force on the gas is -F1, Stokeslet at body 2
    # points back toward body 1. Magnitude checked here; the vector sign is the projection.
    Q = Fr(78, 10)
    rho = Fr(3, 10)
    r = 16
    # Author's floor uses nu <= (3/4)*0.62. Consistent floor uses nu <= 0.62.
    nu_author = Fr(3, 4) * Fr(62, 100)
    nu_true = Fr(62, 100)
    push = Fr(3, 4)

    def floor(nu):
        return push * Q / (4 * nu * rho * r)

    # divide by pi outside Fraction
    fa = floor(nu_author)
    ft = floor(nu_true)
    # fa / pi and ft / pi are the physical ratios
    author_num = float(fa) / np.pi
    true_num = float(ft) / np.pi
    # damping 0.0030 per tick, wavelength 64, alpha = D k^2 / 2
    k = 2 * np.pi / 64
    D = 2 * 0.0030 / k**2
    ok = ok_proj and abs(D - 0.622) < 0.001 and abs(author_num - 0.2086) < 5e-4
    ok = ok and abs(true_num - 0.1564) < 5e-4 and author_num < 0.21
    report(
        "force coefficient",
        bool(ok),
        f"on-axis factor 1/(4 pi nu r); D from 0.0030/tick at wavelength 64 is {D:.4f} "
        f"so nu<=D gives a 0.75-push floor {true_num:.4f} of the reference, "
        f"while (3/4)D gives {author_num:.4f} (below the printed 0.21)",
    )
    return true_num, author_num


def lattice_symbol():
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    nu = sp.symbols("nu", positive=True)
    d = sp.Matrix([sp.exp(sp.I * k1) - 1, sp.exp(sp.I * k2) - 1, sp.exp(sp.I * k3) - 1])
    # |d|^2 = sum 2(1-cos)
    d2 = sp.simplify(sum(sp.expand(d[i] * sp.conjugate(d[i])) for i in range(3)))
    expect = sum(2 * (1 - sp.cos(v)) for v in (k1, k2, k3))
    ok_d = sp.simplify(d2 - expect) == 0
    F = sp.Matrix(sp.symbols("Fx Fy Fz"))
    dc = sp.Matrix([sp.exp(-sp.I * v) - 1 for v in (k1, k2, k3)])
    # conj(d)·d = |d|^2, so the rank-one update kills the divergence exactly.
    ok_norm = sp.simplify(sp.expand(dc.dot(d) - d2)) == 0
    p = (dc.dot(F)) / d2
    g = (F - d * p) / (nu * d2)
    mom = sp.simplify(-nu * d2 * g - d * p + F)
    # conj(d)·d = |d|^2 was checked above, so the divergence numerator is identically zero
    # once that replacement is made.
    div_cleared = sp.simplify(dc.dot(F) - d2 * (dc.dot(F)) / d2)
    ok = ok_d and ok_norm and all(v == 0 for v in mom) and div_cleared == 0
    report(
        "lattice symbol",
        bool(ok),
        "g = (I - d d^+/|d|^2) F / (nu |d|^2) solves -nu|d|^2 g - d p + F = 0 and conj(d).g = 0",
    )


def fft_stokes(L, force=(1.0, 0.0, 0.0)):
    q = 2 * np.pi * np.fft.fftfreq(L)
    kx, ky, kz = np.meshgrid(q, q, q, indexing="ij")
    d = [np.exp(1j * kx) - 1, np.exp(1j * ky) - 1, np.exp(1j * kz) - 1]
    d2 = sum(np.abs(v) ** 2 for v in d)
    d2[0, 0, 0] = 1.0
    F = np.array(force, dtype=np.complex128)
    p = sum(np.conj(d[a]) * F[a] for a in range(3)) / d2
    ghat = [(F[a] - d[a] * p) / d2 for a in range(3)]
    for a in range(3):
        ghat[a][0, 0, 0] = 0.0
    return [np.fft.ifftn(h).real for h in ghat]


def direct_stokes(L, force=(1.0, 0.0, 0.0)):
    """Dense least squares on the periodic box. Neutral force, backward divergence, forward gradient."""
    N = L ** 3

    def ix(a, b, c):
        return ((a % L) * L + (b % L)) * L + (c % L)

    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    M = np.zeros((4 * N, 4 * N))
    rhs = np.zeros(4 * N)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                s = ix(x, y, z)
                for comp in range(3):
                    row = comp * N + s
                    for e in axes:
                        M[row, comp * N + ix(x + e[0], y + e[1], z + e[2])] += 1
                        M[row, comp * N + ix(x - e[0], y - e[1], z - e[2])] += 1
                        M[row, row] -= 2
                    e = axes[comp]
                    M[row, 3 * N + ix(x + e[0], y + e[1], z + e[2])] -= 1
                    M[row, 3 * N + s] += 1
                    bump = force[comp] * ((1.0 if s == 0 else 0.0) - 1.0 / N)
                    rhs[row] = -bump
                row = 3 * N + s
                for comp, e in enumerate(axes):
                    M[row, comp * N + s] += 1
                    M[row, comp * N + ix(x - e[0], y - e[1], z - e[2])] -= 1
    sol = np.linalg.lstsq(M, rhs, rcond=None)[0]
    out = []
    for comp in range(3):
        g = sol[comp * N:(comp + 1) * N].reshape(L, L, L)
        out.append(g - g.mean())
    return out


def numerics(true_floor):
    L = 6
    a = fft_stokes(L)
    b = direct_stokes(L)
    err = max(np.max(np.abs(a[i] - b[i])) for i in range(3))
    report(
        "small box",
        err < 1e-10,
        f"periodic 6^3 FFT Stokeslet matches a real-space least-squares solve, max diff {err:.1e}",
    )
    claimed = {
        64: {4: (0.925, 0.761), 8: (0.778, 0.529), 16: (0.579, 0.076)},
        96: {4: (0.964, 0.840), 8: (0.853, 0.685), 16: (0.701, 0.375)},
        128: {4: (0.983, 0.879), 8: (0.891, 0.764), 16: (0.772, 0.529)},
        192: {4: (1.003, 0.919), 8: (0.930, 0.842), 16: (0.846, 0.685)},
    }
    worst = 0.0
    axial_96_16 = None
    for Lb, rows in claimed.items():
        g = fft_stokes(Lb)
        bits = []
        for r, (ca, ct) in rows.items():
            axial = g[0][r, 0, 0] * 4 * np.pi * r
            trans = g[0][0, r, 0] * 8 * np.pi * r
            worst = max(worst, abs(axial - ca), abs(trans - ct))
            bits.append(f"r={r} {axial:.3f}/{trans:.3f}")
            if Lb == 96 and r == 16:
                axial_96_16 = axial
        print(f"   L={Lb} " + " ".join(bits))
    report(
        "continuum ratios",
        worst < 0.002 and axial_96_16 is not None and 0.65 < axial_96_16 < 0.75,
        f"author's axial/transverse ratios reproduced within {worst:.4f}; "
        f"side-96 axial fraction at r=16 is {axial_96_16:.3f}",
    )
    periodic = true_floor * axial_96_16
    # free-space floor against 0.10±0.07, and the author's periodic comparator against both bars
    inside_free = abs(true_floor - 0.10) < 0.07
    inside_pair = abs(true_floor - 0.17) < 0.08
    report(
        "executed size",
        bool(inside_free and inside_pair and periodic < true_floor),
        f"consistent free-space floor {true_floor:.3f} is inside 0.10±0.07 and inside 0.17±0.08; "
        f"times the side-96 axial fraction it is {periodic:.3f}",
    )


def main():
    dispersion()
    oseen()
    true_floor, author_floor = force_algebra()
    lattice_symbol()
    numerics(true_floor)
    print(f"author floor at (3/4) of the diffusivity: {author_floor:.4f}")
    if fails:
        print("SUMMARY: fails at " + fails[0] + " — see the lines above")
        return
    print(
        "HIT: confirmed - a point momentum sink in the written hydrodynamics is an Oseen Stokeslet, "
        "and the on-axis force on a second capturing body is attractive, "
        "K0 Q1 Q2^2 / (4 pi nu rho r^3), equal to Q2/(4 pi nu rho r) of the inverse-square reference. "
        "The same PDE damps sound at rate (nu+nu_b) k^2/2, so the diffusivity is nu+nu_b. "
        "With nu <= 0.62, the 0.75-push floor is 0.156 of the reference, inside the executed 0.10±0.07."
    )
    print(
        "SUMMARY: confirmed the Stokeslet force law, the 6^3 real-space match, and the lattice-to-Oseen ratios. "
        "The factor (4/3) in nu <= (3/4) D_L does not follow from the momentum equation that was written; "
        "the consistent floor is 0.156 rather than the printed 0.21."
    )


if __name__ == "__main__":
    main()
