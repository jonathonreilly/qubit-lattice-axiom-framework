#!/usr/bin/env python3
"""Staggered-Dirac link integration: class-coupling transposition checks.

Companion runner for
    docs/STAGGERED_DIRAC_LINK_INTEGRATION_CLASS_COUPLING_TRANSPOSITION_NARROW_THEOREM_NOTE_2026-07-02.md

Deterministic, no network, no randomness.  Uses only numpy + stdlib.

Surfaces:
  S1: open 2x2 patch, sites (x,y), positive +x/+y open edges.
  S2: open 3x2 patch, same orientations.
  S3: 2x2 torus, one directed +x and one directed +y edge from each site,
      with wrap edges included as distinct directed edges.

Gate count: flux registration plus moment=6, degree=4, transposition=9,
blindness=7, fixed-background=2, first-order=4, wrap=3, refinement=2,
for TOTAL PASS=38 FAIL=0.  The moment gate keeps the six one-link moment
pairs by grouping the three paired moments into one gate and leaving the
three unpaired moments as separate gates; the two non-uniform-measure
discriminators are separate gates.

Exit code 0 iff FAIL == 0.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from itertools import product
from math import exp, pi

import numpy as np


_pass = 0
_fail = 0


def check(num: int, tag: str, desc: str, ok: bool, extra: str = "") -> bool:
    global _pass, _fail
    status = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{status}] [{tag}] {num:2d}. {desc}"
    if extra:
        line += f"  |  {extra}"
    print(line)
    return bool(ok)


@dataclass(frozen=True)
class Surface:
    name: str
    sites: tuple[tuple[int, int], ...]
    edges: tuple[tuple[int, int, tuple[int, int], int], ...]
    plaquettes: tuple[tuple[tuple[int, int], ...], ...]


def make_open_surface(name: str, nx: int, ny: int) -> Surface:
    sites = tuple((x, y) for y in range(ny) for x in range(nx))
    site_index = {xy: i for i, xy in enumerate(sites)}
    edges = []
    edge_index = {}
    for y in range(ny):
        for x in range(nx):
            tail = site_index[(x, y)]
            if x + 1 < nx:
                head = site_index[(x + 1, y)]
                edge_index[(x, y, 0)] = len(edges)
                edges.append((tail, head, (x, y), 0))
            if y + 1 < ny:
                head = site_index[(x, y + 1)]
                edge_index[(x, y, 1)] = len(edges)
                edges.append((tail, head, (x, y), 1))

    plaquettes = []
    for y in range(ny - 1):
        for x in range(nx - 1):
            plaquettes.append(
                (
                    (edge_index[(x, y, 0)], +1),
                    (edge_index[(x + 1, y, 1)], +1),
                    (edge_index[(x, y + 1, 0)], -1),
                    (edge_index[(x, y, 1)], -1),
                )
            )
    return Surface(name, sites, tuple(edges), tuple(plaquettes))


def make_torus_2x2() -> Surface:
    n = 2
    sites = tuple((x, y) for y in range(n) for x in range(n))
    site_index = {xy: i for i, xy in enumerate(sites)}
    edges = []
    edge_index = {}
    for y in range(n):
        for x in range(n):
            tail = site_index[(x, y)]
            head_x = site_index[((x + 1) % n, y)]
            edge_index[(x, y, 0)] = len(edges)
            edges.append((tail, head_x, (x, y), 0))
            head_y = site_index[(x, (y + 1) % n)]
            edge_index[(x, y, 1)] = len(edges)
            edges.append((tail, head_y, (x, y), 1))

    plaquettes = []
    for y in range(n):
        for x in range(n):
            plaquettes.append(
                (
                    (edge_index[(x, y, 0)], +1),
                    (edge_index[((x + 1) % n, y, 1)], +1),
                    (edge_index[(x, (y + 1) % n, 0)], -1),
                    (edge_index[(x, y, 1)], -1),
                )
            )
    return Surface("S3", sites, tuple(edges), tuple(plaquettes))


S1 = make_open_surface("S1", 2, 2)
S2 = make_open_surface("S2", 3, 2)
S3 = make_torus_2x2()


def phase_values(surface: Surface, label: str) -> np.ndarray:
    vals = []
    for _tail, _head, (x, _y), direction in surface.edges:
        if label == "K0":
            vals.append(1.0 + 0.0j)
        elif label == "K1":
            vals.append(1.0 + 0.0j if direction == 0 else ((-1) ** x) + 0.0j)
        elif label == "twist":
            vals.append(1.0j if direction == 0 else 1.0 + 0.0j)
        else:
            raise ValueError(f"unknown phase label {label!r}")
    return np.array(vals, dtype=np.complex128)


def plaquette_word(values: np.ndarray, plaquette: tuple[tuple[int, int], ...]) -> complex:
    out = 1.0 + 0.0j
    for edge_idx, sign in plaquette:
        z = values[edge_idx]
        out *= z if sign == +1 else np.conj(z)
    return complex(out)


def plaquette_fluxes(surface: Surface, phase_label: str) -> list[complex]:
    t = phase_values(surface, phase_label)
    return [plaquette_word(t, p) for p in surface.plaquettes]


def hopping_matrix(surface: Surface, edge_values: np.ndarray) -> np.ndarray:
    h = np.zeros((len(surface.sites), len(surface.sites)), dtype=np.complex128)
    for value, (tail, head, _xy, _direction) in zip(edge_values, surface.edges):
        h[head, tail] += value
        h[tail, head] += np.conj(value)
    return h


def matrix_observables(surface: Surface, edge_values: np.ndarray) -> dict[str, complex]:
    h = hopping_matrix(surface, edge_values)
    h2 = h @ h
    h4 = h2 @ h2
    h6 = h4 @ h2
    return {
        "trH2": np.trace(h2),
        "trH4": np.trace(h4),
        "trH6": np.trace(h6),
        "detIplusH": np.linalg.det(np.eye(h.shape[0], dtype=np.complex128) + h),
    }


def loop_observable(surface: Surface, edge_values: np.ndarray, plaquette_index: int = 0) -> complex:
    return plaquette_word(edge_values, surface.plaquettes[plaquette_index])


def format_complex(z: complex) -> str:
    z = complex(z)
    if abs(z.imag) < 5e-13:
        return f"{z.real:.12g}"
    return f"{z.real:.12g}{z.imag:+.12g}j"


_integration_cache: dict[tuple[str, int, str, tuple[float, ...]], dict[str, complex]] = {}


def integrate(surface: Surface, k: int, phase_label: str, betas: float | tuple[float, ...]) -> dict[str, complex]:
    if isinstance(betas, (int, float)):
        beta_tuple = tuple(float(betas) for _ in surface.plaquettes)
    else:
        beta_tuple = tuple(float(b) for b in betas)
    if len(beta_tuple) != len(surface.plaquettes):
        raise ValueError("one beta per plaquette is required")

    key = (surface.name, int(k), phase_label, beta_tuple)
    cached = _integration_cache.get(key)
    if cached is not None:
        return cached

    roots = np.exp(2j * pi * np.arange(k) / k)
    t = phase_values(surface, phase_label)
    total = float(k ** len(surface.edges))
    z_sum = 0.0
    obs_sum = {
        "trH2": 0.0 + 0.0j,
        "trH4": 0.0 + 0.0j,
        "trH6": 0.0 + 0.0j,
        "detIplusH": 0.0 + 0.0j,
        "W": 0.0 + 0.0j,
        "ReW": 0.0 + 0.0j,
    }

    for powers in product(range(k), repeat=len(surface.edges)):
        u = roots[list(powers)]
        exponent = 0.0
        for beta, plaquette in zip(beta_tuple, surface.plaquettes):
            exponent += beta * plaquette_word(u, plaquette).real
        weight = exp(exponent)
        w = t * u
        obs = matrix_observables(surface, w)
        loop = loop_observable(surface, w)
        z_sum += weight
        for name, value in obs.items():
            obs_sum[name] += weight * value
        obs_sum["W"] += weight * loop
        obs_sum["ReW"] += weight * loop.real

    result = {"Z": z_sum / total}
    for name, value in obs_sum.items():
        result[name] = value / z_sum
    _integration_cache[key] = result
    return result


def fixed_background(surface: Surface, phase_label: str) -> dict[str, complex]:
    edge_values = phase_values(surface, phase_label)
    obs = matrix_observables(surface, edge_values)
    obs["W"] = loop_observable(surface, edge_values)
    return obs


def max_abs_diff(a: dict[str, complex], b: dict[str, complex], names: tuple[str, ...]) -> float:
    return max(abs(a[name] - b[name]) for name in names)


def fd_derivative_rew(surface: Surface, k: int, phase_label: str, h: float) -> float:
    plus = integrate(surface, k, phase_label, h)["ReW"].real
    minus = integrate(surface, k, phase_label, -h)["ReW"].real
    return (plus - minus) / (2.0 * h)


def average_h_entries(surface: Surface, k: int, phase_label: str) -> tuple[float, np.ndarray]:
    roots = np.exp(2j * pi * np.arange(k) / k)
    t = phase_values(surface, phase_label)
    h_sum = np.zeros((len(surface.sites), len(surface.sites)), dtype=np.complex128)
    h2_diag_sum = np.zeros(len(surface.sites), dtype=np.complex128)
    total = float(k ** len(surface.edges))
    for powers in product(range(k), repeat=len(surface.edges)):
        u = roots[list(powers)]
        h = hopping_matrix(surface, t * u)
        h_sum += h
        h2_diag_sum += np.diag(h @ h)
    return float(np.max(np.abs(h_sum / total))), h2_diag_sum / total


def open_degrees(surface: Surface) -> np.ndarray:
    deg = np.zeros(len(surface.sites), dtype=np.float64)
    for tail, head, _xy, _direction in surface.edges:
        deg[tail] += 1
        deg[head] += 1
    return deg


def run() -> int:
    num = 0

    s1_k0_flux = plaquette_fluxes(S1, "K0")
    s1_k1_flux = plaquette_fluxes(S1, "K1")
    gate0_ok = (
        len(s1_k0_flux) == 1
        and abs(s1_k0_flux[0] - 1.0) < 1e-14
        and abs(s1_k1_flux[0] + 1.0) < 1e-14
    )
    check(num, "flux", "S1 plaquette flux Phi_P(K0)=+1 and Phi_P(K1)=-1", gate0_ok,
          f"K0={format_complex(s1_k0_flux[0])}, K1={format_complex(s1_k1_flux[0])}")

    omega = np.exp(2j * pi * np.arange(8) / 8)
    moment = lambda m, n: np.mean(omega ** (m - n))
    paired = [moment(0, 0), moment(1, 1), moment(2, 2)]
    num += 1
    check(num, "moment", "Z_8 paired one-link moments (0,0),(1,1),(2,2) equal 1",
          all(abs(v - 1.0) < 1e-14 for v in paired),
          "values=" + ",".join(format_complex(v) for v in paired))
    for pair in ((1, 0), (2, 1), (3, 1)):
        num += 1
        value = moment(*pair)
        check(num, "moment", f"Z_8 unpaired one-link moment {pair} vanishes",
              abs(value) < 1e-14, f"value={format_complex(value)}")
    theta = 2 * pi * np.arange(8) / 8
    weights = np.exp(0.7 * np.cos(theta))
    weighted_first = np.sum(weights * omega) / np.sum(weights)
    uniform_first = moment(1, 0)
    num += 1
    check(num, "moment", "von-Mises-weighted Z_8 first moment detects non-uniform measure",
          abs(weighted_first) > 0.05, f"|<u>|={abs(weighted_first):.12g}")
    num += 1
    check(num, "moment", "uniform Z_8 first moment remains zero",
          abs(uniform_first) < 1e-14, f"|<u>|={abs(uniform_first):.12g}")

    degree = open_degrees(S1)
    for label in ("K0", "K1"):
        h_mean_max, h2_diag = average_h_entries(S1, 8, label)
        num += 1
        check(num, "degree", f"S1 <H_e>=0 entrywise for {label}",
              h_mean_max < 1e-14, f"max={h_mean_max:.3e}")
        num += 1
        diag_diff = float(np.max(np.abs(h2_diag - degree)))
        check(num, "degree", f"S1 <(H^2)_xx> equals degree(x) for {label}",
              diag_diff < 1e-12, f"max_diff={diag_diff:.3e}")

    for beta in (0.0, 0.3, 0.7):
        lhs = integrate(S1, 8, "K1", beta)["Z"]
        rhs = integrate(S1, 8, "K0", -beta)["Z"]
        num += 1
        check(num, "transpose", f"S1 K=8 Z[K1,{beta}] = Z[1,{-beta}]",
              abs(lhs - rhs) < 1e-12, f"diff={abs(lhs - rhs):.3e}")
    lhs = integrate(S1, 8, "K1", 0.7)
    rhs = integrate(S1, 8, "K0", -0.7)
    for obs in ("trH4", "detIplusH", "W"):
        num += 1
        diff = abs(lhs[obs] - rhs[obs])
        check(num, "transpose", f"S1 K=8 beta=0.7 transposition for {obs}",
              diff < 1e-12, f"diff={diff:.3e}")
    lhs = integrate(S2, 4, "K1", 0.5)
    rhs = integrate(S2, 4, "K0", tuple(-0.5 for _ in S2.plaquettes))
    for obs in ("Z", "trH4"):
        num += 1
        diff = abs(lhs[obs] - rhs[obs])
        check(num, "transpose", f"S2 K=4 beta=0.5 transposition for {obs}",
              diff < 1e-12, f"diff={diff:.3e}")
    lhs = integrate(S3, 4, "K1", 0.5)
    rhs = integrate(S3, 4, "K0", tuple(-0.5 for _ in S3.plaquettes))
    num += 1
    check(num, "transpose", "S3 K=4 beta=0.5 transposition for Z",
          abs(lhs["Z"] - rhs["Z"]) < 1e-12, f"diff={abs(lhs['Z'] - rhs['Z']):.3e}")

    s1_k0_bare = integrate(S1, 8, "K0", 0.0)
    s1_k1_bare = integrate(S1, 8, "K1", 0.0)
    for obs in ("trH2", "trH4", "trH6", "detIplusH", "W"):
        num += 1
        diff = abs(s1_k0_bare[obs] - s1_k1_bare[obs])
        check(num, "blind", f"S1 K=8 beta=0 blindness for {obs}",
              diff < 1e-12, f"diff={diff:.3e}")
    s2_k0_bare = integrate(S2, 4, "K0", 0.0)
    s2_k1_bare = integrate(S2, 4, "K1", 0.0)
    for obs in ("trH4", "detIplusH"):
        num += 1
        diff = abs(s2_k0_bare[obs] - s2_k1_bare[obs])
        check(num, "blind", f"S2 K=4 beta=0 blindness for {obs}",
              diff < 1e-12, f"diff={diff:.3e}")

    fixed_k0 = fixed_background(S1, "K0")
    fixed_k1 = fixed_background(S1, "K1")
    # For one square plaquette, tr(H^4) contains 4 starting sites times
    # 2 loop orientations, giving 8*Re(Phi_P).  K0-K1 is therefore
    # 8*(+1 - -1) = 16, in addition to identical backtracking terms.
    trh4_delta = int(round((fixed_k0["trH4"] - fixed_k1["trH4"]).real))
    num += 1
    check(num, "fixed", "fixed u=1 S1 tr(H^4) discriminator equals exact 16",
          abs((fixed_k0["trH4"] - fixed_k1["trH4"]).imag) < 1e-12 and trh4_delta == 16,
          f"K0={format_complex(fixed_k0['trH4'])}, K1={format_complex(fixed_k1['trH4'])}, delta={trh4_delta}")
    num += 1
    check(num, "fixed", "fixed u=1 S1 W_P changes sign between K0 and K1",
          fixed_k0["W"].real > 0.9 and fixed_k1["W"].real < -0.9,
          f"K0={format_complex(fixed_k0['W'])}, K1={format_complex(fixed_k1['W'])}")

    h = 1e-3
    c0_h = fd_derivative_rew(S1, 8, "K0", h)
    c0_h2 = fd_derivative_rew(S1, 8, "K0", h / 2.0)
    c0_h4 = fd_derivative_rew(S1, 8, "K0", h / 4.0)
    c1_h = fd_derivative_rew(S1, 8, "K1", h)
    num += 1
    check(num, "linear", "registration derivative c(K0) is positive",
          c0_h > 0.0, f"c_h={c0_h:.12g}")
    num += 1
    check(num, "linear", "registration derivative c(K1) = -c(K0)",
          abs(c1_h + c0_h) < 1e-10, f"c0={c0_h:.12g}, c1={c1_h:.12g}")
    diff_h = abs(c0_h - c0_h2)
    diff_h2 = abs(c0_h2 - c0_h4)
    ratio = diff_h / diff_h2 if diff_h2 else 0.0
    num += 1
    check(num, "linear", "symmetric FD convergence ratio is second-order",
          diff_h > 1e-10 and diff_h2 > 1e-11 and ratio >= 3.5,
          f"diff_h={diff_h:.3e}, diff_h2={diff_h2:.3e}, ratio={ratio:.6g}")
    num += 1
    check(num, "linear", "registration coefficient c(K0) matches derived 1/2",
          abs(c0_h - 0.5) < 1e-6, f"c_h={c0_h:.12g}")

    s3_untwisted_bare = integrate(S3, 4, "K0", 0.0)
    s3_twisted_bare = integrate(S3, 4, "twist", 0.0)
    battery = ("Z", "trH2", "trH4", "trH6", "detIplusH", "W")
    battery_diff = max_abs_diff(s3_untwisted_bare, s3_twisted_bare, battery)
    num += 1
    check(num, "wrap", "S3 zero-flux wrap twist washes out at beta=0 battery",
          battery_diff < 1e-12, f"max_diff={battery_diff:.3e}")
    z_untwisted = integrate(S3, 4, "K0", 0.5)["Z"]
    z_twisted = integrate(S3, 4, "twist", 0.5)["Z"]
    num += 1
    check(num, "wrap", "S3 zero-flux wrap twist leaves beta=0.5 Z unchanged",
          abs(z_untwisted - z_twisted) < 1e-12, f"diff={abs(z_untwisted - z_twisted):.3e}")
    fixed_s3_untwisted = fixed_background(S3, "K0")
    fixed_s3_twisted = fixed_background(S3, "twist")
    winding_a = fixed_s3_untwisted["trH2"].real
    winding_b = fixed_s3_twisted["trH2"].real
    num += 1
    check(num, "wrap", "fixed-background S3 winding diagnostic differs",
          abs(winding_a - winding_b) > 1e-9,
          f"untwisted_trH2={winding_a:.12g}, twisted_trH2={winding_b:.12g}")

    refine_diffs = []
    for kk in (4, 8, 16):
        a = integrate(S1, kk, "K0", 0.0)
        b = integrate(S1, kk, "K1", 0.0)
        refine_diffs.append(max_abs_diff(a, b, ("trH2", "trH4", "trH6", "detIplusH", "W")))
    refine_max = max(refine_diffs)
    num += 1
    check(num, "refine", "S1 beta=0 blindness stable at K=4,8,16",
          refine_max < 1e-13, f"max_diff={refine_max:.3e}")
    a = integrate(S1, 16, "K1", 0.7)
    b = integrate(S1, 16, "K0", -0.7)
    trans_k16 = max_abs_diff(a, b, ("Z", "trH4", "detIplusH", "W"))
    num += 1
    check(num, "refine", "S1 K=16 beta=0.7 transposition identity",
          trans_k16 < 1e-12, f"max_diff={trans_k16:.3e}")

    print(f"TOTAL: PASS={_pass} FAIL={_fail}")
    return 0 if _fail == 0 else 1


if __name__ == "__main__":
    sys.exit(run())
