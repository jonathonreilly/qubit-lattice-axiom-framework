#!/usr/bin/env python3
"""Staggered-Dirac coupling-sign channel registration checks.

Companion runner for
    docs/STAGGERED_DIRAC_COUPLING_SIGN_CHANNEL_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-03.md

Deterministic, no network, no randomness.  Uses only numpy + stdlib.

The S2 single-plaquette gates evaluate the unfixed four-link integrand.
The S2 two-plaquette strip uses tree gauge fixing to the two independent
plaquette variables; the determinant matter weight is gauge-invariant, so
the omitted tree variables contribute only the normalized Haar volume.

Exit code 0 iff FAIL == 0.
"""

from __future__ import annotations

import json
import math
import os
import sys
from dataclasses import dataclass
from itertools import product

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


def relerr(a: complex | float, b: complex | float) -> float:
    return float(abs(a - b) / max(1.0, abs(a), abs(b)))


def eta_phase(direction: int, x: tuple[int, ...], dim: int) -> int:
    if direction == 0:
        return 1
    if direction == 1:
        return 1 if x[0] % 2 == 0 else -1
    if dim == 3 and direction == 2:
        return 1 if (x[0] + x[1]) % 2 == 0 else -1
    raise ValueError("invalid eta direction")


def wrong_eta_phase(direction: int, x: tuple[int, ...], dim: int) -> int:
    if direction == 0:
        return 1
    if direction == 1:
        return 1 if x[1] % 2 == 0 else -1
    if dim == 3 and direction == 2:
        return 1 if (x[0] + x[1]) % 2 == 0 else -1
    raise ValueError("invalid eta direction")


def plaquette_flux(
    phase_func,
    x: tuple[int, ...],
    i: int,
    j: int,
    dim: int,
) -> int:
    xp_i = list(x)
    xp_i[i] += 1
    xp_j = list(x)
    xp_j[j] += 1
    return (
        phase_func(i, x, dim)
        * phase_func(j, tuple(xp_i), dim)
        * phase_func(i, tuple(xp_j), dim)
        * phase_func(j, x, dim)
    )


def s1_eta_gate() -> tuple[bool, str]:
    flux_ok = True
    f2_ok = True
    f3_ok = True
    for x in product(range(4), repeat=3):
        for i in range(3):
            xp = list(x)
            xp[i] += 1
            f2_ok = f2_ok and eta_phase(i, tuple(xp), 3) == eta_phase(i, x, 3)
        for i in range(3):
            for j in range(i + 1, 3):
                flux_ok = flux_ok and plaquette_flux(eta_phase, x, i, j, 3) == -1
                xp_i = list(x)
                xp_i[i] += 1
                xp_j = list(x)
                xp_j[j] += 1
                lhs = eta_phase(i, x, 3) * eta_phase(j, tuple(xp_i), 3)
                rhs = eta_phase(j, x, 3) * eta_phase(i, tuple(xp_j), 3)
                f3_ok = f3_ok and lhs == -rhs
    return flux_ok and f2_ok and f3_ok, f"flux={flux_ok}, F2={f2_ok}, F3={f3_ok}"


def s1_eta_2d_flux() -> tuple[bool, str]:
    count_bad = 0
    for x in product(range(5), repeat=2):
        if x[0] < 4 and x[1] < 4:
            count_bad += int(plaquette_flux(eta_phase, x, 0, 1, 2) != -1)
    return count_bad == 0, f"bad_flux_count={count_bad}"


def s1_wrong_eta_rejector() -> tuple[bool, str]:
    plus = 0
    total = 0
    for x in product(range(4), repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                total += 1
                plus += int(plaquette_flux(wrong_eta_phase, x, i, j, 3) == 1)
    return plus > 0, f"plus_flux={plus}/{total}"


def eta_wrap_consistent(lengths: tuple[int, int, int]) -> tuple[bool, int]:
    violations = 0
    for x in product(*(range(l) for l in lengths)):
        for i in range(3):
            base = eta_phase(i, x, 3)
            for j in range(3):
                shifted = list(x)
                shifted[j] += lengths[j]
                if eta_phase(i, tuple(shifted), 3) != base:
                    violations += 1
    return violations == 0, violations


def single_plaquette_arrays(n: int) -> np.ndarray:
    roots = np.exp(2j * math.pi * np.arange(n) / n)
    return (
        roots[:, None, None, None]
        * roots[None, :, None, None]
        * np.conj(roots[None, None, :, None])
        * np.conj(roots[None, None, None, :])
    )


def det_matter_from_flux(real_w_plaquette: np.ndarray, m: float = 0.5) -> np.ndarray:
    # For the four-site square, direct block evaluation of det(m^2 I + H^2).
    m2 = m * m
    return ((m2 + 2.0) ** 2 - (2.0 + 2.0 * real_w_plaquette)) ** 2


def trh4_square(real_w_plaquette: np.ndarray) -> np.ndarray:
    # Exact trace from the same 4x4 hopping matrix block product.
    return 24.0 + 8.0 * real_w_plaquette


def z_single_unfixed(n: int, t_flux: int, beta: float) -> tuple[float, float]:
    u_p = single_plaquette_arrays(n)
    re_u = u_p.real
    re_w = (t_flux * u_p).real
    f = det_matter_from_flux(re_w)
    weights = np.exp(beta * re_u)
    z = float(np.mean(weights * f))
    trh4 = float(np.mean(weights * f * trh4_square(re_w)) / z)
    return z, trh4


@dataclass(frozen=True)
class Strip:
    sites: tuple[tuple[int, int], ...]
    edges: tuple[tuple[int, int, tuple[int, int], int], ...]


def make_strip() -> Strip:
    sites = tuple((x, y) for y in range(2) for x in range(3))
    idx = {xy: n for n, xy in enumerate(sites)}
    raw_edges = [
        ((0, 0), (1, 0), 0),
        ((1, 0), (2, 0), 0),
        ((0, 1), (1, 1), 0),
        ((1, 1), (2, 1), 0),
        ((0, 0), (0, 1), 1),
        ((1, 0), (1, 1), 1),
        ((2, 0), (2, 1), 1),
    ]
    edges = tuple((idx[a], idx[b], a, d) for a, b, d in raw_edges)
    return Strip(sites, edges)


STRIP = make_strip()


def eta2d_edge(x: tuple[int, int], direction: int) -> int:
    return 1 if direction == 0 or x[0] % 2 == 0 else -1


def hopping_matrix_open(
    sites: tuple[tuple[int, int], ...],
    edges: tuple[tuple[int, int, tuple[int, int], int], ...],
    values: np.ndarray,
) -> np.ndarray:
    h = np.zeros((len(sites), len(sites)), dtype=np.complex128)
    for val, (tail, head, _xy, _direction) in zip(values, edges):
        h[head, tail] += val
        h[tail, head] += np.conj(val)
    return h


def strip_tree_values(p0: complex, p1: complex, t_label: str) -> np.ndarray:
    # Edge order: h0,h1,h2,h3,v0,v1,v2.  h2,h3 carry the two plaquettes.
    u = np.array([1.0, 1.0, np.conj(p0), np.conj(p1), 1.0, 1.0, 1.0], dtype=np.complex128)
    if t_label == "K0":
        t = np.ones(7, dtype=np.complex128)
    elif t_label == "K1":
        t = np.array([eta2d_edge(xy, d) for _tail, _head, xy, d in STRIP.edges], dtype=np.complex128)
    else:
        raise ValueError(t_label)
    return t * u


def z_strip_tree(n: int, t_label: str, beta: float) -> float:
    roots = np.exp(2j * math.pi * np.arange(n) / n)
    z_sum = 0.0
    for p0 in roots:
        for p1 in roots:
            h = hopping_matrix_open(STRIP.sites, STRIP.edges, strip_tree_values(p0, p1, t_label))
            h2 = h @ h
            f = float(np.linalg.det(0.25 * np.eye(h.shape[0]) + h2).real)
            weight = math.exp(beta * (p0.real + p1.real))
            z_sum += weight * f
    return z_sum / float(n * n)


def bessel_i_quad(n: int, beta: float, m: int = 8192) -> float:
    theta = 2.0 * math.pi * np.arange(m) / m
    vals = np.exp(beta * np.cos(theta)) * np.cos(n * theta)
    return float(np.mean(vals))


def bessel_table(beta: float, max_n: int = 60, m: int = 8192) -> dict[int, float]:
    return {n: bessel_i_quad(n, beta, m) for n in range(max_n + 1)}


def bessel_from_table(table: dict[int, float], n: int) -> float:
    return table[abs(n)]


def z_bessel(beta: float, nplaquettes: int, max_n: int = 60) -> float:
    table = bessel_table(beta, max_n)
    return float(sum(bessel_from_table(table, n) ** nplaquettes for n in range(-max_n, max_n + 1)))


def brute_torus_2x1(beta: float, n: int = 64) -> float:
    roots = np.exp(2j * math.pi * np.arange(n) / n)
    ux0 = roots[:, None, None, None]
    ux1 = roots[None, :, None, None]
    uy0 = roots[None, None, :, None]
    uy1 = roots[None, None, None, :]
    p0 = ux0 * uy1 * np.conj(ux0) * np.conj(uy0)
    p1 = ux1 * uy0 * np.conj(ux1) * np.conj(uy1)
    return float(np.mean(np.exp(beta * (p0.real + p1.real))))


def gf2_rank(mat: np.ndarray) -> int:
    a = np.array(mat, dtype=np.uint8, copy=True) & 1
    rows, cols = a.shape
    rank = 0
    for col in range(cols):
        pivot = None
        for r in range(rank, rows):
            if a[r, col]:
                pivot = r
                break
        if pivot is None:
            continue
        if pivot != rank:
            a[[rank, pivot]] = a[[pivot, rank]]
        for r in range(rows):
            if r != rank and a[r, col]:
                a[r] ^= a[rank]
        rank += 1
        if rank == rows:
            break
    return rank


def gf2_boundary(lengths: tuple[int, ...]) -> np.ndarray:
    dim = len(lengths)
    sites = tuple(product(*(range(l) for l in lengths)))
    edge_index = {}
    col = 0
    for x in sites:
        for i in range(dim):
            edge_index[(x, i)] = col
            col += 1
    rows = []
    for x in sites:
        for i in range(dim):
            for j in range(i + 1, dim):
                xp_i = list(x)
                xp_i[i] = (xp_i[i] + 1) % lengths[i]
                xp_j = list(x)
                xp_j[j] = (xp_j[j] + 1) % lengths[j]
                row = np.zeros(col, dtype=np.uint8)
                for key in ((x, i), (tuple(xp_i), j), (tuple(xp_j), i), (x, j)):
                    row[edge_index[key]] ^= 1
                rows.append(row)
    return np.vstack(rows)


def gf2_exists(lengths: tuple[int, ...]) -> bool:
    dmat = gf2_boundary(lengths)
    ones = np.ones((dmat.shape[0], 1), dtype=np.uint8)
    return gf2_rank(dmat) == gf2_rank(np.hstack([dmat, ones]))


def simpson_ratio(beta: float, intervals: int = 32768) -> float:
    if intervals % 2:
        raise ValueError("Simpson intervals must be even")
    theta = np.linspace(0.0, 2.0 * math.pi, intervals + 1)
    weights = np.ones(intervals + 1)
    weights[1:-1:2] = 4.0
    weights[2:-1:2] = 2.0
    density = np.exp(beta * np.cos(theta))
    denom = np.sum(weights * density)
    numer = np.sum(weights * density * np.cos(theta))
    return float(numer / denom)


def first_moment(beta: float) -> float:
    return bessel_i_quad(1, beta) / bessel_i_quad(0, beta)


def open_patch_pure_first_moment(beta: float, n: int = 512) -> float:
    theta = 2.0 * math.pi * np.arange(n) / n
    weights = np.exp(beta * np.cos(theta))
    return float(np.sum(weights * np.cos(theta)) / np.sum(weights))


def angular_distance_to_pi(theta: np.ndarray) -> np.ndarray:
    return np.abs((theta - math.pi + math.pi) % (2.0 * math.pi) - math.pi)


def density_mass_near_pi(beta: float, width: float, n: int = 262144) -> float:
    theta = 2.0 * math.pi * np.arange(n) / n
    weights = np.exp(beta * np.cos(theta))
    mask = angular_distance_to_pi(theta) < width
    return float(np.sum(weights[mask]) / np.sum(weights))


def circular_std_about_pi(beta: float, n: int = 262144) -> float:
    theta = 2.0 * math.pi * np.arange(n) / n
    weights = np.exp(beta * np.cos(theta))
    centered = np.exp(1j * (theta - math.pi))
    resultant = abs(np.sum(weights * centered) / np.sum(weights))
    return float(math.sqrt(max(0.0, -2.0 * math.log(resultant))))


def site_index_3d(x: int, y: int, z: int, l_size: int) -> int:
    return x + l_size * (y + l_size * z)


def eta3d_edge(x: int, y: int, _z: int, direction: int) -> int:
    if direction == 0:
        return 1
    if direction == 1:
        return 1 if x % 2 == 0 else -1
    return 1 if (x + y) % 2 == 0 else -1


def wrong_eta3d_edge(x: int, y: int, _z: int, direction: int) -> int:
    if direction == 0:
        return 1
    if direction == 1:
        return 1 if y % 2 == 0 else -1
    return 1 if (x + y) % 2 == 0 else -1


def hopping_3d(l_size: int, phase_kind: str = "K0", link_u: np.ndarray | None = None) -> np.ndarray:
    nsites = l_size ** 3
    h = np.zeros((nsites, nsites), dtype=np.complex128)
    edge_counter = 0
    for z in range(l_size):
        for y in range(l_size):
            for x in range(l_size):
                tail = site_index_3d(x, y, z, l_size)
                for direction, delta in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                    nx = (x + delta[0]) % l_size
                    ny = (y + delta[1]) % l_size
                    nz = (z + delta[2]) % l_size
                    head = site_index_3d(nx, ny, nz, l_size)
                    if phase_kind == "K0":
                        phase = 1.0 + 0.0j
                    elif phase_kind == "eta":
                        phase = complex(eta3d_edge(x, y, z, direction))
                    elif phase_kind == "wrong":
                        phase = complex(wrong_eta3d_edge(x, y, z, direction))
                    else:
                        raise ValueError(phase_kind)
                    if link_u is not None:
                        phase *= link_u[edge_counter]
                    h[head, tail] += phase
                    h[tail, head] += np.conj(phase)
                    edge_counter += 1
    return h


def shift2_operator(l_size: int) -> np.ndarray:
    nsites = l_size ** 3
    out = 6.0 * np.eye(nsites, dtype=np.complex128)
    for z in range(l_size):
        for y in range(l_size):
            for x in range(l_size):
                tail = site_index_3d(x, y, z, l_size)
                for delta in ((2, 0, 0), (0, 2, 0), (0, 0, 2)):
                    head_p = site_index_3d((x + delta[0]) % l_size, (y + delta[1]) % l_size, (z + delta[2]) % l_size, l_size)
                    head_m = site_index_3d((x - delta[0]) % l_size, (y - delta[1]) % l_size, (z - delta[2]) % l_size, l_size)
                    out[head_p, tail] += 1.0
                    out[head_m, tail] += 1.0
    return out


def k_grid(l_size: int) -> np.ndarray:
    return 2.0 * math.pi * np.arange(l_size) / l_size


def k0_values(l_size: int) -> np.ndarray:
    k = k_grid(l_size)
    vals = [2.0 * (math.cos(a) + math.cos(b) + math.cos(c)) for a in k for b in k for c in k]
    return np.array(vals)


def k1_square_values(l_size: int, trig: str = "cos") -> np.ndarray:
    k = k_grid(l_size)
    fn = math.cos if trig == "cos" else math.sin
    vals = [4.0 * (fn(a) ** 2 + fn(b) ** 2 + fn(c) ** 2) for a in k for b in k for c in k]
    return np.array(vals)


def sorted_max_abs(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.max(np.abs(np.sort(a) - np.sort(b))))


def zero_grid_count_k0(l_size: int) -> int:
    vals = k0_values(l_size) / 2.0
    return int(np.count_nonzero(np.abs(vals) < 1e-12))


def deterministic_links_3d(l_size: int) -> np.ndarray:
    n_edges = 3 * l_size ** 3
    phi_golden = 0.6180339887498949
    phases = []
    for j in range(n_edges):
        frac = (j * phi_golden) % 1.0
        phases.append(np.exp(2j * math.pi * frac))
    return np.array(phases, dtype=np.complex128)


def run() -> int:
    num = 0

    num += 1
    ok, extra = s1_eta_gate()
    check(num, "S1", "3D eta has flux -1 and satisfies F2/F3 on 4^3 open patch", ok, extra)

    num += 1
    ok, extra = s1_eta_2d_flux()
    check(num, "S1", "2D eta has flux -1 on every plaquette of 5x5 open patch", ok, extra)

    num += 1
    ok, extra = s1_wrong_eta_rejector()
    check(num, "S1", "wrong eta family is rejected by a +1 plaquette flux", ok, extra)

    good_444, v444 = eta_wrap_consistent((4, 4, 4))
    good_443, v443 = eta_wrap_consistent((4, 4, 3))
    good_344, v344 = eta_wrap_consistent((3, 4, 4))
    num += 1
    check(
        num,
        "S1",
        "torus eta wrap well-definedness accepts (4,4,4),(4,4,3) and rejects (3,4,4)",
        good_444 and good_443 and (not good_344) and v344 > 0,
        f"violations=(444:{v444},443:{v443},344:{v344})",
    )

    z_k0_11, tr_k0_11 = z_single_unfixed(24, +1, 1.1)
    z_k1_m11, tr_k1_m11 = z_single_unfixed(24, -1, -1.1)
    num += 1
    check(num, "S2", "single plaquette Z[1,1.1] = Z[eta,-1.1]", relerr(z_k0_11, z_k1_m11) < 1e-12, f"rel={relerr(z_k0_11, z_k1_m11):.3e}")

    z_k0_m07, _ = z_single_unfixed(24, +1, -0.7)
    z_k1_p07, _ = z_single_unfixed(24, -1, 0.7)
    num += 1
    check(num, "S2", "single plaquette Z[1,-0.7] = Z[eta,0.7]", relerr(z_k0_m07, z_k1_p07) < 1e-12, f"rel={relerr(z_k0_m07, z_k1_p07):.3e}")

    z_k1_p11, _ = z_single_unfixed(24, -1, 1.1)
    num += 1
    check(num, "S2", "same-sign replacement rejector on single plaquette", relerr(z_k0_11, z_k1_p11) > 1e-3, f"rel={relerr(z_k0_11, z_k1_p11):.3e}")

    z_strip_k0 = z_strip_tree(12, "K0", 0.9)
    z_strip_k1 = z_strip_tree(12, "K1", -0.9)
    num += 1
    check(num, "S2", "two-plaquette strip tree-gauge Z[1,0.9] = Z[eta,-0.9]", relerr(z_strip_k0, z_strip_k1) < 1e-10, f"rel={relerr(z_strip_k0, z_strip_k1):.3e}")

    num += 1
    check(num, "S2", "single plaquette <tr(H^4)> covariant under replacement", relerr(tr_k0_11, tr_k1_m11) < 1e-12, f"rel={relerr(tr_k0_11, tr_k1_m11):.3e}")

    z_k0_11_n48, _ = z_single_unfixed(48, +1, 1.1)
    num += 1
    check(num, "S2", "N=24 vs N=48 Z[1,1.1] quadrature convergence", relerr(z_k0_11, z_k0_11_n48) < 1e-10, f"rel={relerr(z_k0_11, z_k0_11_n48):.3e}")

    table_m = bessel_table(1.3, 8, 4096)
    table_2m = bessel_table(1.3, 8, 8192)
    conv = max(abs(table_m[n] - table_2m[n]) for n in range(9))
    num += 1
    check(num, "S3", "Bessel trapezoid M vs 2M convergence for n=0..8", conv < 1e-13, f"max={conv:.3e}")

    table_13 = bessel_table(1.3, 60, 8192)
    gen_sum = sum(bessel_from_table(table_13, n) for n in range(-60, 61))
    num += 1
    check(num, "S3", "generating-function anchor sum_n I_n(1.3) = exp(1.3)", relerr(gen_sum, math.exp(1.3)) < 1e-12, f"rel={relerr(gen_sum, math.exp(1.3)):.3e}")

    brute = brute_torus_2x1(1.3, 64)
    zb2 = sum(bessel_from_table(table_13, n) ** 2 for n in range(-60, 61))
    num += 1
    check(num, "S3", "2x1 torus brute quadrature matches Bessel #P=2", relerr(brute, zb2) < 1e-8, f"rel={relerr(brute, zb2):.3e}")

    even_diffs = []
    for nplaquettes in (2, 4, 6):
        pos = sum(bessel_from_table(table_13, n) ** nplaquettes for n in range(-60, 61))
        neg = sum(((-1) ** abs(n) * bessel_from_table(table_13, n)) ** nplaquettes for n in range(-60, 61))
        even_diffs.append(relerr(pos, neg))
    num += 1
    check(num, "S3", "even #P torus is sign-blind in character expansion", max(even_diffs) < 1e-13, f"max_rel={max(even_diffs):.3e}")

    z9_pos = sum(bessel_from_table(table_13, n) ** 9 for n in range(-60, 61))
    z9_neg = sum(((-1) ** abs(n) * bessel_from_table(table_13, n)) ** 9 for n in range(-60, 61))
    d9 = z9_pos - z9_neg
    num += 1
    check(num, "S3", "odd #P=9 torus registers sign at beta=1.3", 0.50 < d9 < 0.55 and d9 > 0.0, f"D={d9:.12g}")

    even_only_pos = sum(bessel_from_table(table_13, n) ** 9 for n in range(-60, 61) if n % 2 == 0)
    even_only_neg = sum(((-1) ** abs(n) * bessel_from_table(table_13, n)) ** 9 for n in range(-60, 61) if n % 2 == 0)
    num += 1
    check(num, "S3", "even-charge-only discriminator removes #P=9 difference", abs(even_only_pos - even_only_neg) < 1e-13, f"diff={abs(even_only_pos - even_only_neg):.3e}")

    odd_formula = 2.0 * sum(bessel_from_table(table_13, n) ** 9 for n in range(-60, 61) if n % 2 != 0)
    num += 1
    check(num, "S3", "odd-sector formula equals the #P=9 sign difference", relerr(d9, odd_formula) < 1e-12, f"rel={relerr(d9, odd_formula):.3e}")

    num += 1
    ok = gf2_exists((2, 2)) and gf2_exists((2, 3)) and not gf2_exists((3, 3))
    check(num, "S4", "2D GF(2) examples accept even area and reject 3x3", ok)

    laws_2d = []
    for l1 in range(2, 6):
        for l2 in range(2, 6):
            laws_2d.append(gf2_exists((l1, l2)) == ((l1 * l2) % 2 == 0))
    num += 1
    check(num, "S4", "2D GF(2) law matches L1*L2 even for 2..5", all(laws_2d))

    num += 1
    ok = gf2_exists((2, 2, 2)) and gf2_exists((2, 2, 3)) and not gf2_exists((2, 3, 3)) and not gf2_exists((3, 3, 3))
    check(num, "S4", "3D GF(2) examples accept at most one odd side", ok)

    laws_3d = []
    for lengths in product((2, 3), repeat=3):
        laws_3d.append(gf2_exists(lengths) == (sum(l % 2 for l in lengths) <= 1))
    num += 1
    check(num, "S4", "3D GF(2) law matches at most one odd side on {2,3}^3", all(laws_3d))

    simpson_diffs = []
    for beta in (0.25, 1.3, 3.0):
        simpson_diffs.append(relerr(first_moment(beta), simpson_ratio(beta)))
    num += 1
    check(num, "S5", "I1/I0 first moment matches separate Simpson quadrature", max(simpson_diffs) < 1e-11, f"max_rel={max(simpson_diffs):.3e}")

    odd_diffs = [abs(first_moment(beta) + first_moment(-beta)) for beta in (0.25, 0.7, 1.3, 3.0)]
    num += 1
    check(num, "S5", "first moment is odd in beta", max(odd_diffs) < 1e-13, f"max={max(odd_diffs):.3e}")

    sign_ok = True
    min_margin = 1.0
    for beta in (-3.0, -1.3, -0.7, -0.25, 0.25, 0.7, 1.3, 3.0):
        value = first_moment(beta)
        bound = 0.1 * abs(beta) / (1.0 + abs(beta))
        sign_ok = sign_ok and math.copysign(1.0, value) == math.copysign(1.0, beta) and abs(value) > bound
        min_margin = min(min_margin, abs(value) - bound)
    num += 1
    check(num, "S5", "first moment is sign-faithful on the beta grid", sign_ok, f"min_margin={min_margin:.3e}")

    open_m = open_patch_pure_first_moment(1.3)
    num += 1
    check(num, "S5", "pure-gauge open plaquette <Re u_P> matches I1/I0", relerr(open_m, first_moment(1.3)) < 1e-10, f"rel={relerr(open_m, first_moment(1.3)):.3e}")

    mass_neg = density_mass_near_pi(-25.0, 0.5)
    num += 1
    check(num, "S6", "beta=-25 mass within |theta-pi|<0.5 exceeds 0.98", mass_neg > 0.98, f"mass={mass_neg:.12g}")

    mass_pos = density_mass_near_pi(25.0, 0.5)
    num += 1
    check(num, "S6", "beta=+25 mass within |theta-pi|<0.5 is tiny", mass_pos < 1e-6, f"mass={mass_pos:.3e}")

    width_ratio = circular_std_about_pi(-25.0) / circular_std_about_pi(-100.0)
    num += 1
    check(num, "S6", "circular width ratio follows 1/sqrt(|beta|)", 1.96 < width_ratio < 2.04, f"ratio={width_ratio:.12g}")

    k0_errors = []
    for l_size in (4, 6):
        eig = np.linalg.eigvalsh(hopping_3d(l_size, "K0"))
        k0_errors.append(sorted_max_abs(eig, k0_values(l_size)))
    num += 1
    check(num, "S7", "K0 eigenvalues match 2 sum_i cos(k_i) for L=4,6", max(k0_errors) < 1e-12, f"max={max(k0_errors):.3e}")

    k1_errors = []
    k1_h2_eigs: dict[int, np.ndarray] = {}
    for l_size in (4, 6):
        h = hopping_3d(l_size, "eta")
        eig_h2 = np.linalg.eigvalsh(h @ h)
        k1_h2_eigs[l_size] = eig_h2
        k1_errors.append(sorted_max_abs(eig_h2, k1_square_values(l_size, "cos")))
    num += 1
    check(num, "S7", "K1 H^2 eigenvalues match 4 sum_i cos^2(k_i) for L=4,6", max(k1_errors) < 1e-12, f"max={max(k1_errors):.3e}")

    h4_eta = hopping_3d(4, "eta")
    op_resid = float(np.max(np.abs(h4_eta @ h4_eta - shift2_operator(4))))
    num += 1
    check(num, "S7", "operator identity H[eta]^2 = sum_i(S_2i+S_2i^T+2I)", op_resid < 1e-14, f"max={op_resid:.3e}")

    h_wrong = hopping_3d(4, "wrong")
    wrong_resid = float(np.max(np.abs(h_wrong @ h_wrong - shift2_operator(4))))
    wrong_dev = sorted_max_abs(np.linalg.eigvalsh(h_wrong @ h_wrong), k1_square_values(4, "cos"))
    num += 1
    check(num, "S7", "wrong cochain rejects the operator and spectral anchors", wrong_resid > 0.5 and wrong_dev > 0.1, f"resid={wrong_resid:.3e}, eig_dev={wrong_dev:.3e}")

    k1_zero_counts = []
    for l_size in (4, 8):
        eig = np.linalg.eigvalsh(hopping_3d(l_size, "eta"))
        k1_zero_counts.append(int(np.count_nonzero(np.abs(eig) < 1e-10)))
    num += 1
    check(num, "S7", "K1 exact zero count is 8 for L=4,8", k1_zero_counts == [8, 8], f"counts={k1_zero_counts}")

    eig6 = np.linalg.eigvalsh(hopping_3d(6, "eta"))
    gap6 = float(np.min(np.abs(eig6)))
    grid_gap6 = 2.0 * math.sqrt(float(np.min(k1_square_values(6, "cos") / 4.0)))
    num += 1
    check(num, "S7", "K1 L=6 finite-size gap matches grid formula", abs(gap6 - grid_gap6) < 1e-12 and gap6 > 0.4, f"gap={gap6:.12g}, grid={grid_gap6:.12g}")

    k0_counts = []
    grid_counts = []
    for l_size in (8, 12):
        eig = np.linalg.eigvalsh(hopping_3d(l_size, "K0"))
        k0_counts.append(int(np.count_nonzero(np.abs(eig) < 1e-10)))
        grid_counts.append(zero_grid_count_k0(l_size))
    num += 1
    check(num, "S7", "K0 zero counts match grid and grow from L=8 to L=12", k0_counts == grid_counts and k0_counts[1] > k0_counts[0], f"eig={k0_counts}, grid={grid_counts}")

    sin_dev_l6 = sorted_max_abs(k1_h2_eigs[6], k1_square_values(6, "sin"))
    sin_cos_l4 = sorted_max_abs(k1_square_values(4, "sin"), k1_square_values(4, "cos"))
    num += 1
    check(num, "S7", "wrong sin^2 anchor rejected at L=6 but coincides at L=4", sin_dev_l6 > 1.0 and sin_cos_l4 < 1e-12, f"L6_dev={sin_dev_l6:.3e}, L4_dev={sin_cos_l4:.3e}")

    links = deterministic_links_3d(4)
    eig_eta_u = np.linalg.eigvalsh(hopping_3d(4, "eta", links))
    eta_links = []
    edge_counter = 0
    for z in range(4):
        for y in range(4):
            for x in range(4):
                for direction in range(3):
                    eta_links.append(eta3d_edge(x, y, z, direction) * links[edge_counter])
                    edge_counter += 1
    eig_1_etau = np.linalg.eigvalsh(hopping_3d(4, "K0", np.array(eta_links, dtype=np.complex128)))
    num += 1
    check(num, "S8", "combined field H[eta,u] and H[1,eta u] have identical spectra", sorted_max_abs(eig_eta_u, eig_1_etau) < 1e-12, f"max={sorted_max_abs(eig_eta_u, eig_1_etau):.3e}")

    eig_1_u = np.linalg.eigvalsh(hopping_3d(4, "K0", links))
    diff_generic = sorted_max_abs(eig_1_u, eig_1_etau)
    num += 1
    check(num, "S8", "generic-link rejector distinguishes H[1,u] from H[1,eta u]", diff_generic > 1e-3, f"max_dev={diff_generic:.3e}")

    repo = os.getcwd()
    with open(os.path.join(repo, "docs/audit/data/audit_ledger.json"), encoding="utf-8") as f:
        ledger = json.load(f)
    rows = ledger["rows"] if isinstance(ledger, dict) and "rows" in ledger else ledger
    if isinstance(rows, dict):
        row = rows["staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07"]
    else:
        row = next(r for r in rows if r.get("claim_id") == "staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07")
    needle = " ".join(row["claim_scope"].split())
    with open(
        os.path.join(repo, "docs/STAGGERED_DIRAC_COUPLING_SIGN_CHANNEL_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-03.md"),
        encoding="utf-8",
    ) as f:
        haystack = " ".join(f.read().split())
    num += 1
    check(num, "S9", "Kawamoto-Smit ledger claim_scope appears verbatim in the note", needle in haystack)

    print(f"TOTAL: PASS={_pass} FAIL={_fail}")
    return 0 if _fail == 0 else 1


if __name__ == "__main__":
    sys.exit(run())
