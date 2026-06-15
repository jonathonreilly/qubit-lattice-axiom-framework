#!/usr/bin/env python3
"""Free staggered two-step dispersion in d spatial dimensions.

Companion runner for
docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md.

The checks are deterministic and use only the in-repo staggered blocking
construction.  They verify:

1. the canonical staggered spatial phases fold into a two-site-cell Clifford
   algebra in d = 2 and d = 3;
2. the blocked spatial hop has squared eigenvalue
   -sum_mu sin^2 p_mu in each reduced momentum sector;
3. the action-derived two-step transfer T_odd T_even on small tori has
   decaying spectrum exp(-2 E(p)) with
   E(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu));
4. the log-kernel has even-offset support and axis decay rate arcsinh(m);
5. the all-direction positive l_inf/l1 contour bound is numerically respected
   on resolved finite blocks.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"{'PASS' if ok else 'FAIL'}: {name}"
    if detail:
        line += f" ({detail})"
    print(line)


def coord_to_index(x: tuple[int, ...], L: int) -> int:
    idx = 0
    stride = 1
    for value in x:
        idx += value * stride
        stride *= L
    return idx


def index_to_coord(idx: int, d: int, L: int) -> tuple[int, ...]:
    out = []
    for _ in range(d):
        out.append(idx % L)
        idx //= L
    return tuple(out)


def spatial_hop(d: int, L: int) -> np.ndarray:
    """Canonical spatial staggered hop H_hop on an even periodic L^d torus.

    eta_mu(t, x) = (-1)^(t + x_1 + ... + x_{mu-1}); this routine returns the
    time-independent spatial part xi_mu(x) = (-1)^(x_1 + ... + x_{mu-1}).
    The time-slice sign (-1)^t is applied in T_even/T_odd.
    """
    V = L**d
    hop = np.zeros((V, V), dtype=complex)
    for site in range(V):
        x = list(index_to_coord(site, d, L))
        for mu in range(d):
            eta = (-1) ** sum(x[:mu])
            xp = x.copy()
            xm = x.copy()
            xp[mu] = (xp[mu] + 1) % L
            xm[mu] = (xm[mu] - 1) % L
            hop[site, coord_to_index(tuple(xp), L)] += 0.5 * eta
            hop[site, coord_to_index(tuple(xm), L)] -= 0.5 * eta
    return hop


def gamma_matrices(d: int) -> list[np.ndarray]:
    """Two-site-cell matrices Gamma_mu |r> = (-1)^r_mu |r xor s_mu>."""
    n = 2**d
    gammas: list[np.ndarray] = []
    for mu in range(d):
        mask = (1 << mu) - 1  # ones in slots nu < mu
        gamma = np.zeros((n, n), dtype=float)
        for r in range(n):
            r_mu = (r >> mu) & 1
            gamma[r ^ mask, r] = -1.0 if r_mu else 1.0
        gammas.append(gamma)
    return gammas


def dispersion(m: float, p: tuple[float, ...]) -> float:
    s2 = sum(np.sin(component) ** 2 for component in p)
    return float(np.arcsinh(np.sqrt(m * m + s2)))


def predicted_decays(d: int, L: int, m: float) -> np.ndarray:
    values = []
    for n in product(range(L), repeat=d):
        p = tuple(2.0 * np.pi * ni / L for ni in n)
        values.append(np.exp(-2.0 * dispersion(m, p)))
    return np.sort(np.array(values))


def two_step_decays_from_blocking(d: int, L: int, m: float) -> tuple[np.ndarray, float]:
    H = spatial_hop(d, L)
    V = H.shape[0]
    I = np.eye(V, dtype=complex)
    Z = np.zeros_like(I)
    T_even = np.block([[-2.0 * (m * I + H), I], [I, Z]])
    T_odd = np.block([[-2.0 * (m * I - H), I], [I, Z]])
    T2 = T_odd @ T_even
    eig = np.linalg.eigvals(T2)
    decaying = eig[np.abs(eig) < 1.0 + 1e-8]
    imag_max = float(np.max(np.abs(decaying.imag))) if decaying.size else float("inf")
    return np.sort(decaying.real), imag_max


def kernel_d(d: int, m: float, N: int) -> np.ndarray:
    p = 2.0 * np.pi * np.arange(N) / N
    grids = np.meshgrid(*([p] * d), indexing="ij", sparse=True)
    radicand = m * m
    for grid in grids:
        radicand = radicand + np.sin(grid) ** 2
    E = np.arcsinh(np.sqrt(radicand))
    return np.fft.ifftn(E).real


def fit_rate(ns: np.ndarray, vals: np.ndarray) -> tuple[float, float]:
    y = np.log(np.abs(vals))
    A = np.column_stack([ns, np.log(ns), np.ones_like(ns), 1.0 / ns])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return -float(coef[0]), -float(coef[1])


def strip_constant(eta: float, m: float, d: int) -> float:
    return float(np.sqrt(m * m + (d - 1) + np.cosh(eta) ** 2))


def linf_offsets(d: int, N: int) -> np.ndarray:
    one = np.minimum(np.arange(N), N - np.arange(N))
    grids = np.meshgrid(*([one] * d), indexing="ij", sparse=True)
    out = grids[0]
    for grid in grids[1:]:
        out = np.maximum(out, grid)
    return out


def test_note_guardrails() -> None:
    text = NOTE.read_text(encoding="utf-8")
    forbidden_tokens = ["ret" + "ained", "audit" + "ed_", "2" + "erJ"]
    checks = [
        "**Status authority:** independent audit lane only" in text,
        "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md" in text,
        "TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md" in text,
        "arcsinh(m)/(2d)" in text,
        "sharp anisotropic" in text and "open" in text,
        "p_mu* + i eta sign(z_mu*)" in text and "exp(-eta |z_mu*|)" in text,
        "p_mu* - i eta sign(z_mu*)" not in text,
        all(token not in text for token in forbidden_tokens),
    ]
    check(
        "source note has audit-authority guardrail, one-hop links, positive-rate/sign boundary, and no status/stale-LR tokens",
        all(checks),
        f"{sum(checks)}/{len(checks)} text guards satisfied",
    )


def test_cell_clifford() -> None:
    ok = True
    details = []
    for d in (2, 3):
        gammas = gamma_matrices(d)
        I = np.eye(2**d)
        worst = 0.0
        for mu in range(d):
            worst = max(worst, float(np.linalg.norm(gammas[mu] @ gammas[mu] - I, ord=np.inf)))
            for nu in range(mu + 1, d):
                anti = gammas[mu] @ gammas[nu] + gammas[nu] @ gammas[mu]
                worst = max(worst, float(np.linalg.norm(anti, ord=np.inf)))
        ok = ok and worst == 0.0
        details.append(f"d={d}: max Clifford residual {worst:.1e}")
    check("two-site-cell staggered phase matrices satisfy Gamma_mu^2=I and anticommutation", ok, "; ".join(details))


def test_cell_hop_square() -> None:
    ok = True
    details = []
    samples = {
        2: [(0.2, 0.4), (0.7, -0.3), (1.1, 0.9)],
        3: [(0.2, 0.4, -0.5), (0.7, -0.3, 0.6), (1.1, 0.9, -0.8)],
    }
    for d, points in samples.items():
        gammas = gamma_matrices(d)
        I = np.eye(2**d, dtype=complex)
        worst = 0.0
        for k in points:
            A = sum(1j * np.sin(k[mu]) * gammas[mu] for mu in range(d))
            s2 = sum(np.sin(k[mu]) ** 2 for mu in range(d))
            worst = max(worst, float(np.linalg.norm(A @ A + s2 * I, ord=np.inf)))
        ok = ok and worst < 1e-14
        details.append(f"d={d}: max ||A(k)^2 + |sin k|^2 I||_inf {worst:.1e}")
    check("folded spatial hop has scalar square -sum_mu sin^2(k_mu) in each cell-momentum sector", ok, "; ".join(details))


def test_two_step_spectrum() -> None:
    ok = True
    details = []
    for d, L in ((2, 4), (2, 6), (3, 4)):
        m = 0.37
        decays, imag_max = two_step_decays_from_blocking(d, L, m)
        pred = predicted_decays(d, L, m)
        residual = float(np.max(np.abs(decays - pred))) if len(decays) == len(pred) else float("inf")
        local_ok = len(decays) == len(pred) and residual < 1e-12 and imag_max < 1e-12
        ok = ok and local_ok
        details.append(f"d={d},L={L}: count {len(decays)}/{len(pred)}, max residual {residual:.1e}, max imag {imag_max:.1e}")
    check("position-space blocked T_odd T_even decaying spectrum equals exp(-2E(p)) on d=2 and d=3 tori", ok, "; ".join(details))


def test_even_support() -> None:
    ok = True
    details = []
    for d, N in ((2, 256), (3, 128)):
        h = kernel_d(d, 0.3, N)
        parity = np.arange(N) % 2
        grids = np.meshgrid(*([parity] * d), indexing="ij", sparse=True)
        any_odd = grids[0] > 0
        for grid in grids[1:]:
            any_odd = any_odd | (grid > 0)
        odd_max = float(np.max(np.abs(h[any_odd])))
        ok = ok and odd_max < 1e-12
        details.append(f"d={d}: max odd-offset |h| {odd_max:.1e}")
    check("kernel support is on even spatial offsets after two-step blocking", ok, "; ".join(details))


def test_axis_rates() -> None:
    ok = True
    details = []
    configs = [(2, 512, 0.3, 20, 80, 0.02), (3, 128, 0.3, 20, 50, 0.03)]
    for d, N, m, lo, hi, tol in configs:
        h = kernel_d(d, m, N)
        ns = np.arange(lo + lo % 2, hi + 1, 2, dtype=float)
        vals = np.array([h[(int(n),) + (0,) * (d - 1)] for n in ns])
        rate, beta = fit_rate(ns, vals)
        target = float(np.arcsinh(m))
        rel = abs(rate - target) / target
        ok = ok and rel < tol
        details.append(f"d={d}: rate {rate:.6f} vs arcsinh(m) {target:.6f}, rel {rel:.3%}, prefactor {beta:.2f}")
    check("axis kernel decay rate matches arcsinh(m) on d=2 and d=3 resolved blocks", ok, "; ".join(details))


def test_positive_direction_bound() -> None:
    ok = True
    details = []
    for d, N, m in ((2, 256, 0.3), (3, 128, 0.3)):
        h = kernel_d(d, m, N)
        eta_star = float(np.arcsinh(m))
        eta = 0.8 * eta_star
        C = strip_constant(eta, m, d)
        linf = linf_offsets(d, N)
        sel = (linf >= 1) & (linf <= min(40, N // 4))
        ratio = float(np.max(np.abs(h[sel]) / (C * np.exp(-eta * linf[sel]))))
        ok = ok and ratio <= 1.0
        rd = eta_star / (2.0 * d)
        details.append(f"d={d}: max ratio {ratio:.3f}, concrete l1 rate r_d=arcsinh(m)/(2d)={rd:.6f}")
    check("all-direction contour bound is respected; it gives an explicit positive l1 rate arcsinh(m)/(2d)", ok, "; ".join(details))


def main() -> int:
    print("FREE STAGGERED TWO-STEP DISPERSION IN D DIMENSIONS")
    print("Deterministic checks; no random inputs.")
    test_note_guardrails()
    test_cell_clifford()
    test_cell_hop_square()
    test_two_step_spectrum()
    test_even_support()
    test_axis_rates()
    test_positive_direction_bound()
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
