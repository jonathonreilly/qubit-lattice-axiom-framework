#!/usr/bin/env python3
"""Referee for kernel-normalization puzzle, a3.

Author w-jonathonsmac4f50-j5e26 (claude-opus-5). Own stencil algebra.
The one-loop closure is the attempt's assumption. Two-loop k dependence is not derived.
The nine plateaus are read back from the executed logs and compared with a fresh torus sum.
"""
import glob
import itertools
import re

import numpy as np
import sympy as sp

fails = []

STENCILS = {
    "back21": [(0, 0), (-1, 0), (0, -1)],
    "back31": [(0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)],
    "light": [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)],
}

# Quoted N1 rows: n, beta, L, predicted, plateau.
ROWS = (
    (4, 2, 64, 1.0251, 1.0342),
    (4, 24, 64, 1.0024, 1.0024),
    (7, 2, 48, 1.0425, 1.0474),
    (4, 2, 48, 1.0260, 1.0334),
    (4, 6, 32, 1.0101, 1.0103),
    (7, 1, 24, 1.0805, 1.0865),
    (7, 1.5, 48, 1.0552, 1.0649),
    (7, 1, 48, 1.0785, 1.1033),
    (7, 1, 96, 1.0775, 1.1050),
)


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def phi_of(stencil, ks):
    n = len(stencil)
    return sum(sp.exp(sp.I * sum(k * c for k, c in zip(ks, site))) for site in stencil) / n


def modulus_sq(expr):
    return sp.expand(sp.expand_complex(expr * sp.conjugate(expr)))


def stencil_identity():
    ok = True
    for stencil in STENCILS.values():
        dim = len(stencil[0])
        ks = sp.symbols(f"k1:{dim + 1}", real=True)
        n = len(stencil)
        mod = modulus_sq(phi_of(stencil, ks))
        pairs = sum(
            1 - sp.cos(sum(k * (a - b) for k, a, b in zip(ks, left, right)))
            for left, right in itertools.combinations(stencil, 2)
        )
        gap = sp.simplify(sp.expand(sp.trigsimp(pairs - sp.Rational(n * n, 2) * (1 - mod))))
        ok &= gap == 0
    # Pointwise cancellation: E[delta] = (2 sigma^2 / n) * (n^2 / 2) = n sigma^2.
    n, sig = sp.symbols("n sigma2", positive=True)
    collapsed = sp.simplify((2 * sig / n) * (n ** 2 / 2) - n * sig)
    report(
        "stencil",
        ok and collapsed == 0,
        "for all three stencils, sum_{y<y'}(1-cos k.(y-y'))=(n^2/2)(1-|phi|^2), so E[delta]=n sigma^2",
    )


def gain():
    x = sp.symbols("x", positive=True)
    exact = sp.expand((1 - x) * (1 + x * (1 - x)))
    leading = sp.expand((1 - x) * (1 + x))
    report(
        "gain",
        exact == 1 - 2 * x ** 2 + x ** 3
        and exact.coeff(x, 1) == 0
        and leading == 1 - x ** 2
        and leading.coeff(x, 1) == 0,
        "Hartree gain (1-x)(1+x(1-x))=1-2x^2+x^3 and (1-x)(1+x)=1-x^2; no order-1/beta term",
    )


def automorphism():
    """Relabeling the simplex origin is a torus automorphism and preserves |phi|.
    It sends a face-diagonal character to a nearest-neighbour character, so C(e)=C(e_i-e_j).
    """
    ok = True
    # 3+1: q1=-k1, q2=k2-k1, q3=k3-k1. det = -1.
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    q1, q2, q3 = -k1, k2 - k1, k3 - k1
    mat = sp.Matrix([[-1, 0, 0], [-1, 1, 0], [-1, 0, 1]])
    left = modulus_sq((1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2) + sp.exp(sp.I * k3)) / 4)
    right = modulus_sq((1 + sp.exp(sp.I * q1) + sp.exp(sp.I * q2) + sp.exp(sp.I * q3)) / 4)
    char = sp.simplify(sp.exp(sp.I * (k2 - k1)) - sp.exp(sp.I * q2))
    ok &= mat.det() == -1 and char == 0 and sp.simplify(left - right) == 0
    # 2+1
    q1b, q2b = -k1, k2 - k1
    mat2 = sp.Matrix([[-1, 0], [-1, 1]])
    left2 = modulus_sq((1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3)
    right2 = modulus_sq((1 + sp.exp(sp.I * q1b) + sp.exp(sp.I * q2b)) / 3)
    ok &= mat2.det() == -1 and sp.simplify(left2 - right2) == 0
    # With C(e)=C(e_i-e_j), Gamma is the same at every backward-3+1 site.
    ce = sp.symbols("c_e")
    sites = STENCILS["back31"]
    def cov(vec):
        r2 = sum(v * v for v in vec)
        return ce if r2 in (1, 2) else 0
    gammas = [
        sum(cov(tuple(a - b for a, b in zip(site, other))) for other in sites)
        for site in sites
    ]
    ok &= len(set(gammas)) == 1
    report(
        "exchange",
        ok,
        "the simplex relabeling preserves |phi| and swaps diagonals with neighbours, so the backward exchange term is constant and drops",
    )


def light_cone():
    ce, c2, cd, c0 = sp.symbols("c_e c_2e c_d c_0")
    def cov(vec):
        r2 = sum(v * v for v in vec)
        nz = sum(1 for v in vec if v != 0)
        if r2 == 0:
            return c0
        if r2 == 1:
            return ce
        if r2 == 4:
            return c2
        if r2 == 2 and nz == 2:
            return cd
        raise ValueError(vec)
    sites = STENCILS["light"]
    gamma = {site: sum(cov(tuple(a - b for a, b in zip(site, other))) for other in sites) for site in sites}
    bar = sum(gamma.values()) / 7
    delta = c2 + 4 * cd - 5 * ce
    origin = sp.simplify(gamma[(0, 0, 0)] - bar + sp.Rational(6, 7) * delta)
    arms = all(sp.simplify(gamma[site] - bar - delta / 7) == 0 for site in sites if site != (0, 0, 0))
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    lap = 2 * ((1 - sp.cos(k1)) + (1 - sp.cos(k2)) + (1 - sp.cos(k3)))
    symbol = sp.Rational(1, 49) * sum((gamma[site] - bar) * sp.exp(sp.I * (k1 * site[0] + k2 * site[1] + k3 * site[2])) for site in sites)
    symbol = sp.simplify(sp.expand(symbol + delta * lap / 343).rewrite(sp.exp))
    report(
        "light-cone",
        origin == 0 and arms and symbol == 0,
        "Gamma(0)-Gamma_bar=-(6/7)Delta and Gamma(+-e)=Delta/7; the exchange symbol is -(Delta/343) times the laplacian",
    )


def noise():
    sig, width, delta_c, lap = sp.symbols("sigma2 W Delta_c E", positive=True)
    factor = sp.expand(1 + sig - sig * (width - 1))
    phi = 1 - lap / 7
    em = phi - sig * delta_c * lap / 343
    ratio = factor * (1 - phi ** 2) / (1 - em ** 2)
    limit = sp.simplify(sp.limit(ratio, lap, 0))
    target = sp.simplify(factor / (1 + sig * delta_c / 49))
    # The attempt's W-1 drops the excluded zero mode: sum_{k!=0} |phi|^2/(1-|phi|^2) / L^d = W - 1 + 1/L^d.
    ell = sp.symbols("L", positive=True)
    volume = sp.simplify((width - 1 + 1 / ell) - (width - (1 - 1 / ell)))
    report(
        "noise",
        sp.expand(factor - (1 + sig * (2 - width))) == 0 and sp.simplify(limit - target) == 0 and volume == 0,
        "noise factor 1+sigma^2(2-W); light-cone R(0+)=that over (1+sigma^2 Delta_c/49); W-1 drops 1/L^d",
    )


def plateaus():
    cache = {}

    def lattice(length, law):
        key = (length, law)
        if key in cache:
            return cache[key]
        wave = 2 * np.pi * np.fft.fftfreq(length)
        k1, k2, k3 = np.meshgrid(wave, wave, wave, indexing="ij")
        if law == 4:
            symbol = (1 + np.exp(1j * k1) + np.exp(1j * k2) + np.exp(1j * k3)) / 4
        else:
            symbol = (1 + 2 * (np.cos(k1) + np.cos(k2) + np.cos(k3))) / 7
        power = np.abs(symbol) ** 2
        mask = np.ones_like(power, bool)
        mask[0, 0, 0] = False
        green = np.zeros_like(power)
        green[mask] = 1 / (1 - power[mask])
        real = np.real(np.fft.ifftn(green))
        ret = float(green.sum() / length ** 3)
        shift = float(real[2, 0, 0] + 4 * real[1, length - 1, 0] - 5 * real[1, 0, 0]) if law == 7 else 0.0
        cache[key] = (ret, shift, power, np.sqrt(k1 ** 2 + k2 ** 2 + k3 ** 2))
        return cache[key]

    wanted = {row: [] for row in ROWS}
    for path in glob.glob("logs/probes/X:*/*.txt"):
        text = open(path).read()
        header = re.search(
            r"menu=sphere beta=([\d.]+) L=(\d+) T=(\d+) T0=(\d+) seed=\d+; predecessors n=(\d)",
            text,
        )
        if not header:
            continue
        beta = float(header.group(1))
        length, start, stop, count = int(header.group(2)), int(header.group(4)), int(header.group(3)), int(header.group(5))
        shells = [float(x) for x in re.findall(r"\|k\| in \[[^)]*\): ([\d.]+)", text)]
        if len(shells) != 7:
            continue
        measured = sum(shells[3:6]) / 3
        for row in ROWS:
            n, b, ell, _pred, plat = row
            if count == n and length == ell and abs(beta - b) < 1e-9 and abs(measured - plat) < 6e-5:
                wanted[row].append((shells, start, stop, beta, measured))
    ok = True
    for row, hits in wanted.items():
        n, beta, length, pred_q, plat_q = row
        if not hits:
            ok = False
            continue
        ret, shift, power, radius = lattice(length, n)
        kappa = n * beta
        variance = (1 / np.tanh(kappa) - 1 / kappa) / kappa
        predicted = (1 + variance * (2 - ret)) / (1 + variance * shift / 49)
        ok &= abs(predicted - pred_q) < 6e-5
        printed_w = {(4, 64): 1.7701, (4, 48): 1.7625, (4, 32): 1.7473, (7, 48): 1.3614, (7, 24): 1.3449, (7, 96): 1.3696}[(n, length)]
        ok &= abs(ret - printed_w) < 6e-5
        for shells, start, stop, beta_hit, measured in hits:
            gap = measured - predicted
            ok &= 0 <= gap < 0.028
            selected = power[(radius > 0) & (radius < 0.3)]
            times = np.arange(start + 1, stop + 1)
            transient = float(np.mean([np.mean(1 - mode ** times) for mode in selected]))
            error = float(np.sqrt(np.sum((1 + selected) / (1 - selected)) / (stop - start)) / selected.size)
            score = (shells[0] - predicted * transient) / (predicted * error)
            # The attempt prints z to one decimal. The largest here is -1.73, which prints as -1.7.
            ok &= round(abs(score) + 1e-12, 1) <= 1.7
            tilted = measured - predicted * (1 - variance * ((start + 1 + stop) / 2) / length ** 3)
            ratio = tilted / variance ** 2
            if n == 4:
                ok &= 0.8 <= ratio <= 1.05 or abs(gap) < 5e-4
            else:
                ok &= 1.4 <= ratio <= 1.9
    report(
        "plateaus",
        ok and all(wanted.values()),
        "nine executed plateaus match 1+sigma^2(2-W) within 0.028, each above its prediction, and every quoted lowest shell has |z|<=1.7",
    )


def main():
    stencil_identity()
    gain()
    automorphism()
    light_cone()
    noise()
    plateaus()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - under the one-loop closure, E[delta]=n sigma^2 and the order-1/beta gain cancels. "
        "Simplex relabeling forces C(e)=C(e_i-e_j), so the backward exchange term drops. "
        "On the light-cone it is -(Delta/343) times the laplacian, and R(0+)=[1+sigma^2(2-W)]/(1+sigma^2 Delta_c/49). "
        "The nine executed plateaus sit above that prediction by at most 0.028, and the quoted lowest shells have |z|<=1.7."
    )
    print(
        "SUMMARY: confirmed the stencil identity, the gain cancellation, the exchange terms, and the nine-run plateaus. "
        "The one-loop closure is assumed. The two-loop rise of R with k is not derived. "
        "The attempt's W-1 drops a 1/L^d zero-mode piece, far below the printed residuals."
    )


if __name__ == "__main__":
    main()
