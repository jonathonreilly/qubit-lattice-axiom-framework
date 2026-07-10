#!/usr/bin/env python3
"""Tick--Admissibility realization bridge checks.

Deterministic, numpy only, no network, no cache writes. All tick quantities are
computed from explicit complex matrices, and all availability variation sets
are extracted from explicit finite rule tables.

Exit code 0 iff FAIL == 0.
"""

from __future__ import annotations

import itertools
import math
import re
import sys
from pathlib import Path
from typing import Callable

import numpy as np


TOL = 1e-12
L_DEFAULT = 6
PASS = 0
FAIL = 0

Profile = tuple[int, int]
Rule = dict[tuple[int, Profile], frozenset[int]]


def check(tag: str, description: str, ok: bool, extra: str = "") -> bool:
    """Print one required PASS/FAIL line and update the totals."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        prefix = "PASS"
    else:
        FAIL += 1
        prefix = "FAIL"
    line = f"{prefix}: [{tag}] {description}"
    if extra:
        line += f" | {extra}"
    print(line)
    return ok


def max_abs(a: np.ndarray) -> float:
    return float(np.max(np.abs(a))) if a.size else 0.0


def translation_matrix(L: int) -> np.ndarray:
    """T e_x = e_{x+1}."""
    T = np.zeros((L, L), dtype=complex)
    for x in range(L):
        T[(x + 1) % L, x] = 1.0
    return T


def ring_distance(x: int, y: int, L: int) -> int:
    delta = (x - y) % L
    return min(delta, L - delta)


def is_unitary(U: np.ndarray, tol: float = TOL) -> bool:
    I = np.eye(U.shape[0], dtype=complex)
    return max_abs(U.conj().T @ U - I) < tol and max_abs(U @ U.conj().T - I) < tol


def is_nn_supported(U: np.ndarray, tol: float = TOL) -> bool:
    L = U.shape[0]
    return all(
        abs(U[x, y]) < tol
        for x in range(L)
        for y in range(L)
        if ring_distance(x, y, L) > 1
    )


def frame_from_phases(phases: list[float] | np.ndarray) -> np.ndarray:
    return np.diag(np.exp(1j * np.asarray(phases, dtype=float))).astype(complex)


def frame_conjugate(U: np.ndarray, g: np.ndarray) -> np.ndarray:
    return g @ U @ g.conj().T


def modulus_defect(U: np.ndarray) -> float:
    """Compute M(U) literally from T U T^dag and entrywise moduli."""
    T = translation_matrix(U.shape[0])
    translated = T @ U @ T.conj().T
    return float(np.max(np.abs(np.abs(translated) - np.abs(U))))


def offsite_support(U: np.ndarray) -> bool:
    """Compute O(U) literally: at least one nonzero off-diagonal entry."""
    L = U.shape[0]
    return any(U[x, y] != 0 for x in range(L) for y in range(L) if x != y)


def mover(L: int, displacement: int, amplitudes: np.ndarray | None = None) -> np.ndarray:
    if amplitudes is None:
        amplitudes = np.ones(L, dtype=complex)
    U = np.zeros((L, L), dtype=complex)
    for x in range(L):
        U[x, (x + displacement) % L] = amplitudes[x]
    return U


def givens_witness(angles: list[float]) -> np.ndarray:
    L = 2 * len(angles)
    U = np.zeros((L, L), dtype=complex)
    for k, theta in enumerate(angles):
        c = math.cos(theta)
        s = math.sin(theta)
        U[2 * k : 2 * k + 2, 2 * k : 2 * k + 2] = np.array(
            [[c, -s], [s, c]], dtype=complex
        )
    return U


PROFILES: tuple[Profile, ...] = tuple(itertools.product((0, 1), repeat=2))


def build_rule(L: int, law: Callable[[int, Profile], frozenset[int]]) -> Rule:
    return {(x, profile): law(x, profile) for x in range(L) for profile in PROFILES}


def rule_values_valid(rule: Rule, L: int) -> bool:
    possibilities = frozenset((0, 1))
    return all(
        (x, profile) in rule
        and bool(rule[(x, profile)])
        and rule[(x, profile)].issubset(possibilities)
        for x in range(L)
        for profile in PROFILES
    )


def covariance_checker(rule: Rule, L: int) -> bool:
    """Compare A_x(profile) with A_{x+1}(shifted profile)."""
    if not rule_values_valid(rule, L):
        return False
    return all(
        rule[(x, profile)] == rule[((x + 1) % L, profile)]
        for x in range(L)
        for profile in PROFILES
    )


def variation_set(rule: Rule, L: int) -> set[tuple[int, int]]:
    """Enumerate all profiles and profile pairs differing at one neighbor."""
    variation: set[tuple[int, int]] = set()
    for x in range(L):
        for displacement, coordinate in ((-1, 0), (+1, 1)):
            y = (x + displacement) % L
            for profile in PROFILES:
                changed = list(profile)
                changed[coordinate] = 1 - changed[coordinate]
                other = (changed[0], changed[1])
                if rule[(x, profile)] != rule[(x, other)]:
                    variation.add((x, y))
    return variation


def variation_bits(V: set[tuple[int, int]], L: int) -> dict[tuple[int, int], int]:
    return {
        (x, displacement): int((x, (x + displacement) % L) in V)
        for x in range(L)
        for displacement in (-1, 0, +1)
    }


def variation_translation_invariant(V: set[tuple[int, int]], L: int) -> bool:
    shifted = {((x + 1) % L, (y + 1) % L) for x, y in V}
    return shifted == V


def build_from_assignment(
    L: int,
    V: set[tuple[int, int]],
    assignment: Callable[[int, int], complex],
) -> np.ndarray:
    bits = variation_bits(V, L)
    U = np.zeros((L, L), dtype=complex)
    for x in range(L):
        for displacement in (-1, 0, +1):
            U[x, (x + displacement) % L] = assignment(
                displacement, bits[(x, displacement)]
            )
    return U


def phase_uniformization(amplitudes: np.ndarray) -> tuple[complex, np.ndarray, complex]:
    """Cumulative-product gauge for U[x,x-1] = amplitudes[x]."""
    L = len(amplitudes)
    product = complex(np.prod(amplitudes))
    t_bar = np.exp(1j * np.angle(product) / L)
    g_entries = np.ones(L, dtype=complex)
    cumulative = 1.0 + 0.0j
    for x in range(1, L):
        cumulative *= amplitudes[x]
        g_entries[x] = t_bar**x / cumulative
    closure = t_bar**L / product
    return t_bar, np.diag(g_entries), closure


def period2_representative(
    L: int,
    alpha: complex,
    p: complex,
    q: complex,
    r: complex,
    s: complex,
    delta: complex,
) -> np.ndarray:
    """Build U(z)=[[alpha,p+q/z],[r+s*z,delta]] in site space."""
    if L % 2:
        raise ValueError("period-2 representative requires even L")
    U = np.zeros((L, L), dtype=complex)
    cells = L // 2
    for n in range(cells):
        a = 2 * n
        b = 2 * n + 1
        U[a, a] = alpha
        U[b, b] = delta
        U[a, b] = p
        U[a, (b - 2) % L] = q
        U[b, a] = r
        U[b, (a + 2) % L] = s
    return U


def displacement_set(U: np.ndarray, tol: float = TOL) -> set[int]:
    L = U.shape[0]
    out: set[int] = set()
    for x in range(L):
        for y in range(L):
            if abs(U[x, y]) >= tol:
                raw = (y - x) % L
                out.add(raw if raw <= L // 2 else raw - L)
    return out


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_definition_line(text: str, prefix: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(prefix):
            return stripped
    return ""


def main() -> int:
    L = L_DEFAULT
    I = np.eye(L, dtype=complex)
    T = translation_matrix(L)
    U_R = mover(L, -1)
    U_L = mover(L, +1)
    U_giv = givens_witness([0.3, 0.9, 0.3])
    onsite = np.diag(np.exp(1j * np.array([0.2, 0.9, 1.7, 2.2, 2.8, 0.4])))

    print("tick--Admissibility realization bridge checks (2026-07-10)")

    # GROUP A -- surface reconstruction.
    dense_unitary = np.fft.fft(np.eye(L), norm="ortho").astype(complex)
    short_mover = 0.9 * U_R
    check(
        "A1",
        "uniform right mover is unitary and nearest-neighbor supported",
        is_unitary(U_R)
        and is_nn_supported(U_R)
        and not is_unitary(short_mover)
        and not is_nn_supported(dense_unitary),
        "rejectors: 0.9 mover is nonunitary; Fourier unitary is not NN-supported",
    )

    givens_defect = modulus_defect(U_giv)
    check(
        "A2",
        "right mover is exactly translation covariant and has M=0",
        max_abs(T @ U_R @ T.conj().T - U_R) < TOL
        and modulus_defect(U_R) < TOL
        and givens_defect > 0.05,
        f"M(U_R)={modulus_defect(U_R):.3e}; rejector M(U_giv)={givens_defect:.6f}",
    )

    frames_a = [
        frame_from_phases([0.1, 0.4, 1.2, 2.0, 2.7, 0.3]),
        frame_from_phases([0.0, math.pi / 3, -0.4, 1.7, -2.2, 0.8]),
    ]
    frame_invariance = all(
        abs(modulus_defect(frame_conjugate(U, g)) - modulus_defect(U)) < TOL
        for U in (U_R, onsite)
        for g in frames_a
    )
    h_entries = np.array([1.0, 1.3, 0.8, 1.6, 0.7, 1.1], dtype=complex)
    h = np.diag(h_entries)
    nonframe_tick = h @ U_R @ np.linalg.inv(h)
    check(
        "A3",
        "M is invariant under two fixed nontrivial local U(1) frames",
        frame_invariance and modulus_defect(nonframe_tick) > 0.05,
        f"nonunit-modulus diagonal rejector M={modulus_defect(nonframe_tick):.6f}",
    )

    check(
        "A4",
        "O distinguishes the mover from an on-site tick",
        offsite_support(U_R) and not offsite_support(onsite),
        f"O(U_R)={offsite_support(U_R)}, O(onsite)={offsite_support(onsite)}",
    )

    # Covariant rule with genuine dependence on the x-1 neighbor. Profiles are
    # ordered (c(x-1), c(x+1)).
    A_cov = build_rule(
        L,
        lambda _x, profile: frozenset((0,))
        if profile[0] == 0
        else frozenset((0, 1)),
    )
    V_cov = variation_set(A_cov, L)
    bits_cov = variation_bits(V_cov, L)
    bit_columns = {
        displacement: tuple(bits_cov[(x, displacement)] for x in range(L))
        for displacement in (-1, 0, +1)
    }
    A_const = build_rule(L, lambda _x, _profile: frozenset((0, 1)))
    check(
        "B1",
        "covariant varying rule has translation-invariant V and site-independent v_x(d)",
        covariance_checker(A_cov, L)
        and bool(V_cov)
        and variation_translation_invariant(V_cov, L)
        and all(len(set(values)) == 1 for values in bit_columns.values())
        and not variation_set(A_const, L),
        f"|V|={len(V_cov)}, v-columns={bit_columns}; constant-rule rejector has empty V",
    )

    def F_right(displacement: int, varies: int) -> complex:
        return 1.0 if displacement == -1 and varies == 1 else 0.0

    U0 = build_from_assignment(L, V_cov, F_right)
    check(
        "B2",
        "fixed assignment builds an exactly translation-covariant right mover",
        max_abs(U0 - U_R) < TOL
        and max_abs(T @ U0 @ T.conj().T - U0) < TOL
        and max_abs(T @ U_giv @ T.conj().T - U_giv) > 0.05,
        f"T-invariance residual={max_abs(T @ U0 @ T.conj().T - U0):.3e}",
    )

    g_live = frame_from_phases([0.13, 0.71, 1.29, 2.03, 2.81, 0.37])
    U_live = frame_conjugate(U0, g_live)
    check(
        "B3",
        "a nontrivially framed R1 tick has the derived modulus shadow M=0",
        modulus_defect(U_live) < TOL and modulus_defect(nonframe_tick) > 0.05,
        f"M(gU0g^dag)={modulus_defect(U_live):.3e}; nonframe rejector={modulus_defect(nonframe_tick):.6f}",
    )

    def F_left(displacement: int, _varies: int) -> complex:
        return 1.0 if displacement == +1 else 0.0

    U0_left = build_from_assignment(L, V_cov, F_left)
    check(
        "B4",
        "a second fixed assignment gives a translation-covariant left mover with M=0",
        max_abs(U0_left - U_L) < TOL
        and max_abs(T @ U0_left @ T.conj().T - U0_left) < TOL
        and modulus_defect(U0_left) < TOL
        and modulus_defect(U_giv) > 0.05,
        f"left residual={max_abs(T @ U0_left @ T.conj().T - U0_left):.3e}",
    )

    U_alt = np.diag(np.array([(-1.0) ** x for x in range(L)], dtype=complex))
    U_alt_bad = np.diag(np.array([1.0, 0.7, 1.0, 0.7, 1.0, 0.7], dtype=complex))
    check(
        "B5",
        "alternating on-site tick has M=0 despite alternating phase",
        modulus_defect(U_alt) < TOL and modulus_defect(U_alt_bad) > 0.2,
        f"M(U_alt)={modulus_defect(U_alt):.3e}; modulus-alternating rejector={modulus_defect(U_alt_bad):.3f}",
    )

    frame_phase_family = [
        np.zeros(L),
        np.array([0.11, 0.43, 1.07, 1.89, 2.51, -0.37]),
        np.array([math.pi * x / L for x in range(L)]),
        np.array([math.pi * x * (x + 1) / L for x in range(L)]),
        np.array([math.pi * (x % 2) / 3 for x in range(L)]),
        np.array([0.17 * x * x for x in range(L)]),
        np.array([(-1) ** x * 0.29 * (x + 1) for x in range(L)]),
        np.array([2.4, -1.1, 0.6, 2.9, -2.2, 1.3]),
        np.array([math.pi * (x + 1) ** 2 / (L + 1) for x in range(L)]),
    ]
    frame_family = [frame_from_phases(phases) for phases in frame_phase_family]
    family_rigidity = max(
        max_abs(frame_conjugate(U_alt, g) - U_alt) for g in frame_family
    )
    commutator_residual = max(max_abs(g @ U_alt - U_alt @ g) for g in frame_family)
    algebraic_diagonal_identity = (
        max_abs(U_alt - np.diag(np.diag(U_alt))) == 0.0
        and all(max_abs(g - np.diag(np.diag(g))) == 0.0 for g in frame_family)
        and all(max_abs(np.diag(g) * np.conj(np.diag(g)) - 1.0) < TOL for g in frame_family)
    )
    translated_alt = T @ U_alt @ T.conj().T
    check(
        "B6",
        "U_alt is frame-rigid and no diagonal frame can make it one-site covariant",
        len(frame_family) >= 8
        and family_rigidity < TOL
        and commutator_residual == 0.0
        and algebraic_diagonal_identity
        and max_abs(translated_alt + U_alt) < TOL
        and max_abs(translated_alt - U_alt) > 1.0,
        f"frames={len(frame_family)}, rigidity={family_rigidity:.3e}; diagonal matrices commute identically",
    )

    U_giv_perturbed = U_giv.copy()
    U_giv_perturbed[0, 0] += 0.02
    check(
        "B7",
        "Givens direct sum is unitary and nearest-neighbor supported",
        is_unitary(U_giv)
        and is_nn_supported(U_giv)
        and not is_unitary(U_giv_perturbed),
        f"unitarity residual={max_abs(U_giv.conj().T @ U_giv - I):.3e}",
    )

    def site_assignment_table(U: np.ndarray, x: int) -> dict[tuple[int, int], complex]:
        return {
            (displacement, bits_cov[(x, displacement)]): U[
                x, (x + displacement) % L
            ]
            for displacement in (-1, 0, +1)
        }

    table0 = site_assignment_table(U_giv, 0)
    table2 = site_assignment_table(U_giv, 2)
    uniform_givens = givens_witness([0.3, 0.3, 0.3])
    uniform_table0 = site_assignment_table(uniform_givens, 0)
    uniform_table2 = site_assignment_table(uniform_givens, 2)
    multiset0 = sorted(round(abs(value), 14) for value in table0.values())
    multiset2 = sorted(round(abs(value), 14) for value in table2.values())
    check(
        "B8",
        "Givens witness requires differing site-dependent assignment tables",
        multiset0 != multiset2 and uniform_table0 == uniform_table2,
        f"site-0 amplitudes={multiset0}, site-2 amplitudes={multiset2}",
    )

    M_giv = modulus_defect(U_giv)
    check(
        "B9",
        "Givens witness has a strict computed modulus-covariance defect",
        M_giv > 0.05 and modulus_defect(U_R) < TOL,
        f"M(U_giv)={M_giv:.12f}; uniform-mover rejector M={modulus_defect(U_R):.3e}",
    )

    phases6 = np.array([0.1, 0.7, 1.3, 2.1, 2.9, 0.4])
    amplitudes6 = np.exp(1j * phases6)
    decorated6 = mover(6, -1, amplitudes6)
    tbar6, gauge6, closure6 = phase_uniformization(amplitudes6)
    uniform6 = mover(6, -1, np.full(6, tbar6, dtype=complex))
    wrong_root6 = tbar6 * np.exp(0.2j)
    wrong_closure6 = wrong_root6**6 / np.prod(amplitudes6)
    check(
        "B10",
        "L=6 cumulative-product gauge exactly uniformizes the fixed mover phases and closes",
        max_abs(frame_conjugate(decorated6, gauge6) - uniform6) < TOL
        and abs(closure6 - 1.0) < TOL
        and abs(tbar6**6 - np.prod(amplitudes6)) < TOL
        and abs(wrong_closure6 - 1.0) > 0.1,
        f"uniformization={max_abs(frame_conjugate(decorated6, gauge6) - uniform6):.3e}, closure={abs(closure6-1):.3e}",
    )

    phases8 = np.array([0.2, 0.55, 1.05, 1.6, 2.25, 2.8, 0.35, 1.9])
    amplitudes8 = np.exp(1j * phases8)
    decorated8 = mover(8, -1, amplitudes8)
    tbar8, gauge8, closure8 = phase_uniformization(amplitudes8)
    uniform8 = mover(8, -1, np.full(8, tbar8, dtype=complex))
    wrong_root8 = tbar8 * np.exp(0.17j)
    wrong_closure8 = wrong_root8**8 / np.prod(amplitudes8)
    check(
        "B11",
        "L=8 spot-check cumulative-product gauge uniformizes and closes",
        max_abs(frame_conjugate(decorated8, gauge8) - uniform8) < TOL
        and abs(closure8 - 1.0) < TOL
        and abs(tbar8**8 - np.prod(amplitudes8)) < TOL
        and abs(wrong_closure8 - 1.0) > 0.1,
        f"uniformization={max_abs(frame_conjugate(decorated8, gauge8) - uniform8):.3e}, closure={abs(closure8-1):.3e}",
    )

    # GROUP C -- Theorem B2.
    r2_entries_nonzero = all(abs(U0[x, y]) > 0.0 for x, y in V_cov if x != y)
    only_nn_pairs = all(ring_distance(x, y, L) == 1 for x, y in V_cov)
    identity_r2_entries_nonzero = all(abs(I[x, y]) > 0.0 for x, y in V_cov if x != y)
    check(
        "C1",
        "nonempty nearest-neighbor V is carried by U0 and forces O(U0)=true",
        bool(V_cov)
        and only_nn_pairs
        and r2_entries_nonzero
        and offsite_support(U0)
        and not identity_r2_entries_nonzero,
        f"|V|={len(V_cov)}, O(U0)={offsite_support(U0)}; identity fails R2",
    )

    check(
        "C2",
        "dropping R2 lets the same varying rule coexist with the identity tick",
        bool(V_cov) and not offsite_support(I) and offsite_support(U0),
        f"O(I)={offsite_support(I)}, O(R2 witness)={offsite_support(U0)}",
    )

    V_const = variation_set(A_const, L)

    def F_constant_mover(displacement: int, varies: int) -> complex:
        return 1.0 if displacement == -1 and varies == 0 else 0.0

    U_const_mover = build_from_assignment(L, V_const, F_constant_mover)
    check(
        "C3",
        "converse fails: a constant rule has empty V while its fixed-F mover has O=true",
        covariance_checker(A_const, L)
        and not V_const
        and max_abs(U_const_mover - U_R) < TOL
        and offsite_support(U_const_mover)
        and bool(V_cov),
        f"|V(A_const)|={len(V_const)}, O(U_R)={offsite_support(U_const_mover)}",
    )

    A_site_dependent = dict(A_cov)
    A_site_dependent[(0, (0, 0))] = frozenset((1,))
    check(
        "C4",
        "covariance checker rejects a deliberately site-dependent availability rule",
        not covariance_checker(A_site_dependent, L) and covariance_checker(A_cov, L),
        "rejector=False, covariant control=True",
    )

    # GROUP D -- endpoint consistency on five actual unitary matrices.
    U_onsite = period2_representative(
        L, np.exp(0.2j), 0.0, 0.0, 0.0, 0.0, np.exp(1.1j)
    )
    theta_pr = 0.37
    U_pr = period2_representative(
        L,
        math.cos(theta_pr),
        -math.sin(theta_pr),
        0.0,
        math.sin(theta_pr),
        0.0,
        math.cos(theta_pr),
    )
    theta_qs = 0.61
    U_qs = period2_representative(
        L,
        math.cos(theta_qs),
        0.0,
        -math.sin(theta_qs),
        0.0,
        math.sin(theta_qs),
        math.cos(theta_qs),
    )
    U_qr = period2_representative(
        L, 0.0, 0.0, np.exp(0.3j), np.exp(1.2j), 0.0, 0.0
    )
    U_ps = period2_representative(
        L, 0.0, np.exp(0.8j), 0.0, 0.0, np.exp(-0.4j), 0.0
    )

    def passes_filter(U: np.ndarray) -> bool:
        return modulus_defect(U) < TOL and offsite_support(U)

    check(
        "D1",
        "on-site representative has M=0 and O=false, so it fails the combined filter",
        is_unitary(U_onsite)
        and modulus_defect(U_onsite) < TOL
        and not offsite_support(U_onsite)
        and not passes_filter(U_onsite)
        and passes_filter(U_qr),
        f"M={modulus_defect(U_onsite):.3e}, O={offsite_support(U_onsite)}",
    )

    check(
        "D2",
        "mixed p/r representative is unitary but has M>0 and fails the filter",
        is_unitary(U_pr)
        and modulus_defect(U_pr) > 0.05
        and offsite_support(U_pr)
        and not passes_filter(U_pr),
        f"M(p/r)={modulus_defect(U_pr):.12f}",
    )

    check(
        "D3",
        "mixed q/s representative is unitary but has M>0 and fails the filter",
        is_unitary(U_qs)
        and modulus_defect(U_qs) > 0.05
        and offsite_support(U_qs)
        and not passes_filter(U_qs),
        f"M(q/s)={modulus_defect(U_qs):.12f}",
    )

    disp_qr = displacement_set(U_qr)
    check(
        "D4",
        "phase-decorated q/r mover passes and has one displacement sign",
        is_unitary(U_qr)
        and modulus_defect(U_qr) < TOL
        and offsite_support(U_qr)
        and passes_filter(U_qr)
        and disp_qr in ({-1}, {+1}),
        f"M={modulus_defect(U_qr):.3e}, displacement y-x={sorted(disp_qr)}",
    )

    disp_ps = displacement_set(U_ps)
    sign_qr = next(iter(disp_qr)) if len(disp_qr) == 1 else 0
    sign_ps = next(iter(disp_ps)) if len(disp_ps) == 1 else 0
    check(
        "D5",
        "phase-decorated p/s mover passes with the opposite displacement sign",
        is_unitary(U_ps)
        and modulus_defect(U_ps) < TOL
        and offsite_support(U_ps)
        and passes_filter(U_ps)
        and sign_ps == -sign_qr
        and sign_ps != 0,
        f"M={modulus_defect(U_ps):.3e}, displacement y-x={sorted(disp_ps)}",
    )

    representatives = {
        "none/none": U_onsite,
        "p/r": U_pr,
        "q/s": U_qs,
        "q/r mover": U_qr,
        "p/s mover": U_ps,
    }
    survivors = [name for name, U in representatives.items() if passes_filter(U)]
    check(
        "D6",
        "combined filter leaves exactly the two opposite movers",
        survivors == ["q/r mover", "p/s mover"]
        and sign_qr == -sign_ps
        and sign_qr != 0,
        f"survivors={survivors}",
    )

    # GROUP E -- exact source quote pins, with whitespace-normalized matching.
    root = Path(__file__).resolve().parents[1]
    axioms_text = (root / "docs" / "MINIMAL_AXIOMS_2026-06-29.md").read_text(
        encoding="utf-8"
    )
    selector_text = (
        root
        / "docs"
        / "TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md"
    ).read_text(encoding="utf-8")
    note_text = (
        root
        / "docs"
        / "TICK_ADMISSIBILITY_REALIZATION_BRIDGE_CLAUSE_TO_PREDICATE_NARROW_THEOREM_NOTE_2026-07-10.md"
    ).read_text(encoding="utf-8")
    normalized_axioms = normalize_whitespace(axioms_text)
    normalized_note = normalize_whitespace(note_text)
    clause1 = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under "
        "lattice translations and proper cubic rotations."
    )
    clause2 = (
        "For each site, the available possibilities are determined by, and vary "
        "with, the nearest-neighbor conditions."
    )
    check(
        "E1",
        "clause-1 sentence is present verbatim in the axioms and new note",
        clause1 in normalized_axioms and clause1 in normalized_note,
    )
    check(
        "E2",
        "clause-2 sentence is present verbatim in the axioms and new note",
        clause2 in normalized_axioms and clause2 in normalized_note,
    )
    check(
        "E3",
        "note contains the full-covariance phrase",
        "modulo local U(1) frames" in normalized_note,
    )
    check(
        "E4",
        "note contains the support phrase",
        "off-site tick support" in normalized_note,
    )
    selector_M = extract_definition_line(selector_text, "M(U) = max_xy")
    selector_O = extract_definition_line(selector_text, "O(U) = true")
    check(
        "E5",
        "M(U) and O(U) definition lines are copied verbatim from the selector",
        bool(selector_M)
        and bool(selector_O)
        and normalize_whitespace(selector_M) in normalized_note
        and normalize_whitespace(selector_O) in normalized_note,
        f"M line={selector_M!r}; O line={selector_O!r}",
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
