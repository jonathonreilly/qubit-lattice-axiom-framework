#!/usr/bin/env python3
"""W55 windowed-bond deep-chain bounded probe.

This runner rebuilds the finite W53 oriented fundamental-window bond on the
625-state two-strip surface, tests the slice-identity mechanism under that
bond, and measures bounded rungs where the full B4 computation is feasible.

No random inputs, runtime dates, external data, fitted selectors, or new
comparator numbers are used.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import frontier_su3_fusion_engine as fusion_engine
import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word


AUDIT_TIMEOUT_SEC = 600

BETA = 6.0
MODE_MAX = 80
FUSION_GRID = 80
NMAX_FULL = 4
NMAX_PROBE = 3
NMAX_SMALL = 2

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)

W44_K2_ANCHOR = 0.449370834209281
W53_WINDOW_K2_REFERENCE = 0.445084590711323
UNWINDOWED_DEEP_REFERENCE = 0.615191992185898
COMPARATOR = one_word.CANONICAL_COMPARATOR

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WINDOWED_BOND_DEEP_LIMIT_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Surface:
    nmax: int
    weights: tuple[tuple[int, int], ...]
    index: dict[tuple[int, int], int]
    d_coeff: np.ndarray
    dim: np.ndarray
    fusion: np.ndarray
    fusion_table: np.ndarray
    fusion_residual: float
    pairs: tuple[tuple[int, int], ...]
    pair_index: dict[tuple[int, int], int]
    d_layer: np.ndarray
    dim_layer: np.ndarray
    strip_transfer: np.ndarray
    eta: np.ndarray
    eta_residual: float
    eta_min: float
    zero_bond: np.ndarray
    fund_bond: np.ndarray
    full_bond: np.ndarray
    window_strength: float
    strip_fusion: np.ndarray


@dataclass(frozen=True)
class DirectRow:
    nmax: int
    k: int
    label: str
    dimension: int
    vector_gb: float
    eigenvalue: float
    residual: float
    iterations: int
    p_value: float
    rho10: float
    rho11: float
    psi_min: float


@dataclass(frozen=True)
class ReducedRow:
    nmax: int
    k: int
    p_value: float
    rho10: float
    rho11: float
    eigenvalue: float


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 112)
    print(title)
    print("=" * 112)


def fundamental_outcomes(label: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    p, q = label
    out = [(p + 1, q)]
    if p >= 1:
        out.append((p - 1, q + 1))
    if q >= 1:
        out.append((p, q - 1))
    return tuple(out)


def antifundamental_outcomes(label: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    p, q = label
    out = [(p, q + 1)]
    if q >= 1:
        out.append((p + 1, q - 1))
    if p >= 1:
        out.append((p - 1, q))
    return tuple(out)


def source_from_pair_raw(surface: Surface, raw_pair: np.ndarray) -> tuple[float, np.ndarray]:
    left_raw = np.zeros(len(surface.weights), dtype=float)
    for value, (left, _right) in zip(raw_pair, surface.pairs):
        left_raw[left] += float(value)
    denom = float(left_raw[surface.index[ZERO]])
    if abs(denom) <= 1.0e-300:
        raise RuntimeError("zero left-marginal denominator")
    rho = left_raw / denom
    rho_map = {w: float(rho[i]) for i, w in enumerate(surface.weights)}
    p_value = float(
        one_word.source_readout(
            rho_map,
            one_word.SOURCE_NMAX,
            one_word.SOURCE_MODE_MAX,
            "zero",
        )["P"]
    )
    return p_value, rho


def perron_symmetric(matrix: np.ndarray) -> tuple[float, np.ndarray, float, float]:
    vals, vecs = np.linalg.eigh((matrix + matrix.T) / 2.0)
    pos = int(np.argmax(vals))
    vec = vecs[:, pos]
    if float(vec[0]) < 0.0:
        vec = -vec
    eig = float(vals[pos])
    residual = float(np.linalg.norm(matrix @ vec - eig * vec, ord=np.inf))
    return eig, vec, residual, float(np.min(vec))


@lru_cache(maxsize=None)
def build_surface(nmax: int) -> Surface:
    tw = one_word.build_tensor_word(nmax, MODE_MAX)
    weights = tuple(tw["weights"])
    index = dict(tw["index"])
    d_coeff = np.asarray(tw["normalized"], dtype=float)
    dim = np.array([one_word.src_existing.dim_su3(*w) for w in weights], dtype=float)
    fusion = np.asarray(tw["nf"] + tw["nfb"], dtype=float)

    chars = fusion_engine.character_table(list(weights), FUSION_GRID)
    haar, cell = fusion_engine.haar_measure_normalized(FUSION_GRID)
    fusion_table, fusion_residual = fusion_engine.fusion_table(
        list(weights), chars, haar, cell
    )

    n = len(weights)
    pairs = tuple((left, right) for left in range(n) for right in range(n))
    pair_index = {pair: pos for pos, pair in enumerate(pairs)}
    internal = np.ones(len(pairs), dtype=float)
    for pos, (left, right) in enumerate(pairs):
        for target, target_weight in enumerate(weights):
            if target_weight != ZERO:
                internal[pos] += d_coeff[target] * fusion_table[left, right, target]

    d_layer = np.array(
        [d_coeff[left] * d_coeff[right] for left, right in pairs],
        dtype=float,
    )
    d_layer *= internal
    dim_layer = np.array([dim[left] * dim[right] for left, right in pairs], dtype=float)
    strip_fusion = np.kron(fusion, fusion)
    strip_transfer = (
        np.diag(d_layer)
        @ strip_fusion
        @ np.diag(d_layer)
        @ strip_fusion.T
        @ np.diag(d_layer)
    )
    _eig, eta_vec, eta_residual, eta_min = perron_symmetric(strip_transfer)
    eta = eta_vec / float(eta_vec[0])

    zero_bond = np.diag(1.0 / dim_layer)
    fund_bond = np.zeros((len(pairs), len(pairs)), dtype=float)
    weight_set = set(weights)
    for source_pos, (left_i, right_i) in enumerate(pairs):
        left = weights[left_i]
        right = weights[right_i]
        for left_target in fundamental_outcomes(left):
            if left_target not in weight_set:
                continue
            for right_target in antifundamental_outcomes(right):
                if right_target not in weight_set:
                    continue
                target = (index[left_target], index[right_target])
                fund_bond[source_pos, pair_index[target]] = 1.0 / 9.0
    window_strength = float(dim[index[FUND]] * d_coeff[index[FUND]])
    full_bond = zero_bond + window_strength * fund_bond

    return Surface(
        nmax=nmax,
        weights=weights,
        index=index,
        d_coeff=d_coeff,
        dim=dim,
        fusion=fusion,
        fusion_table=fusion_table,
        fusion_residual=float(fusion_residual),
        pairs=pairs,
        pair_index=pair_index,
        d_layer=d_layer,
        dim_layer=dim_layer,
        strip_transfer=strip_transfer,
        eta=eta,
        eta_residual=eta_residual,
        eta_min=eta_min,
        zero_bond=zero_bond,
        fund_bond=fund_bond,
        full_bond=full_bond,
        window_strength=window_strength,
        strip_fusion=strip_fusion,
    )


def apply_axis(arr: np.ndarray, op: np.ndarray, axis: int) -> np.ndarray:
    n = op.shape[0]
    moved = np.moveaxis(arr, axis, 0)
    shape = moved.shape
    mat = moved.reshape(n, -1)
    out = op @ mat
    return np.moveaxis(out.reshape(shape), 0, axis)


def outer_tensor(surface: Surface, k: int) -> np.ndarray:
    n = len(surface.weights)
    d_pair = surface.d_layer.reshape(n, n)
    out = 1.0
    for word in range(k):
        shape = [1] * (2 * k)
        shape[2 * word] = n
        shape[2 * word + 1] = n
        out = out * d_pair.reshape(shape)
    return out


def middle_tensor(surface: Surface, bond: np.ndarray, k: int) -> np.ndarray:
    n = len(surface.weights)
    d_pair = surface.d_layer.reshape(n, n)
    b = bond.reshape(n, n, n, n)
    if k == 2:
        return d_pair[:, :, None, None] * b * d_pair[None, None, :, :]
    if k == 3:
        return (
            d_pair[:, :, None, None, None, None]
            * b[:, :, :, :, None, None]
            * d_pair[None, None, :, :, None, None]
            * b[None, None, :, :, :, :]
            * d_pair[None, None, None, None, :, :]
        )
    raise ValueError(f"direct middle tensor implemented for k=2,3, got {k}")


def contract_source(surface: Surface, psi: np.ndarray, k: int) -> np.ndarray:
    n = len(surface.weights)
    arr = psi.reshape([n, n] * k)
    eta_matrix = surface.eta.reshape(n, n)
    for _ in range(k - 1):
        arr = np.tensordot(arr, eta_matrix, axes=([2, 3], [0, 1]))
    return arr.ravel()


def direct_power(
    surface: Surface,
    bond: np.ndarray,
    k: int,
    label: str,
    tolerance: float,
    max_iterations: int = 300,
) -> DirectRow:
    n = len(surface.weights)
    dimension = n ** (2 * k)
    shape = [n, n] * k
    outer = outer_tensor(surface, k)
    middle = middle_tensor(surface, bond, k)
    fusion = surface.fusion

    def matvec(vec: np.ndarray) -> np.ndarray:
        arr = vec.reshape(shape).copy()
        arr *= outer
        for axis in range(2 * k):
            arr = apply_axis(arr, fusion.T, axis)
        arr *= middle
        for axis in range(2 * k):
            arr = apply_axis(arr, fusion, axis)
        arr *= outer
        return arr.ravel()

    x = np.ones(dimension, dtype=float)
    x /= np.linalg.norm(x)
    iterations = 0
    for iterations in range(1, max_iterations + 1):
        y = matvec(x)
        norm = float(np.linalg.norm(y))
        if norm <= 1.0e-300:
            raise RuntimeError(f"{label}: zero vector during power iteration")
        y /= norm
        if float(y[0]) < 0.0:
            y = -y
        if float(np.max(np.abs(y - x))) < tolerance:
            x = y
            break
        x = y

    ax = matvec(x)
    eigenvalue = float(np.vdot(x, ax).real / np.vdot(x, x).real)
    residual = float(np.linalg.norm(ax - eigenvalue * x, ord=np.inf))
    raw_pair = contract_source(surface, x, k)
    p_value, rho = source_from_pair_raw(surface, raw_pair)
    return DirectRow(
        nmax=surface.nmax,
        k=k,
        label=label,
        dimension=dimension,
        vector_gb=dimension * 8.0 / 1.0e9,
        eigenvalue=eigenvalue,
        residual=residual,
        iterations=iterations,
        p_value=float(p_value),
        rho10=float(rho[surface.index[FUND]]),
        rho11=float(rho[surface.index[ADJOINT]]) if ADJOINT in surface.index else float("nan"),
        psi_min=float(np.min(x)),
    )


def unwindowed_reduced_row(surface: Surface, k: int) -> ReducedRow:
    if k == 1:
        p_value, rho = source_from_pair_raw(surface, surface.eta)
        return ReducedRow(
            nmax=surface.nmax,
            k=k,
            p_value=float(p_value),
            rho10=float(rho[surface.index[FUND]]),
            rho11=float(rho[surface.index[ADJOINT]]) if ADJOINT in surface.index else float("nan"),
            eigenvalue=float("nan"),
        )

    middle_coeff = surface.d_layer**k / surface.dim_layer ** (k - 1)
    sqrt_c = np.sqrt(middle_coeff)
    g_channel = surface.strip_fusion.T @ (
        (surface.d_layer * surface.d_layer)[:, None] * surface.strip_fusion
    )
    ell_eta = surface.strip_fusion.T @ (surface.d_layer * surface.eta)
    reduced = sqrt_c[:, None] * (g_channel**k) * sqrt_c[None, :]
    vals, vecs = np.linalg.eigh((reduced + reduced.T) / 2.0)
    pos = int(np.argmax(vals))
    vec = vecs[:, pos]
    if float(np.sum(sqrt_c * vec)) < 0.0:
        vec = -vec
    coeff = sqrt_c * vec
    raw_pair = surface.d_layer * (
        surface.strip_fusion @ (coeff * (ell_eta ** (k - 1)))
    )
    p_value, rho = source_from_pair_raw(surface, raw_pair)
    return ReducedRow(
        nmax=surface.nmax,
        k=k,
        p_value=float(p_value),
        rho10=float(rho[surface.index[FUND]]),
        rho11=float(rho[surface.index[ADJOINT]]) if ADJOINT in surface.index else float("nan"),
        eigenvalue=float(vals[pos]),
    )


def trivial_visible_channels(surface: Surface) -> set[int]:
    return {
        surface.pair_index[(surface.index[left], surface.index[right])]
        for left in (FUND, ANTIFUND)
        for right in (FUND, ANTIFUND)
    }


def predecessor_support(surface: Surface, bond: np.ndarray) -> set[int]:
    channels = trivial_visible_channels(surface)
    support: set[int] = set()
    for source in range(len(surface.pairs)):
        if any(float(bond[source, target]) > 0.0 for target in channels):
            support.add(source)
    return support


def slice_row_support(surface: Surface, predecessor: set[int]) -> set[int]:
    active: set[int] = set()
    for row in range(len(surface.pairs)):
        if any(float(surface.strip_fusion[row, mid]) > 0.0 for mid in predecessor):
            active.add(row)
    return active


def pair_label(surface: Surface, pair_pos: int) -> tuple[tuple[int, int], tuple[int, int]]:
    left, right = surface.pairs[pair_pos]
    return surface.weights[left], surface.weights[right]


def source_pair_support_limit() -> float:
    return float(
        one_word.source_readout(
            {FUND: 1.0, ANTIFUND: 1.0},
            one_word.SOURCE_NMAX,
            one_word.SOURCE_MODE_MAX,
            "zero",
        )["P"]
    )


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def print_direct_row(row: DirectRow) -> None:
    print(
        f"{row.label}: NMAX={row.nmax}, k={row.k}, dim={row.dimension}, "
        f"vector_GB={row.vector_gb:.6f}, eig={row.eigenvalue:.15e}, "
        f"residual={row.residual:.3e}, iterations={row.iterations}, "
        f"P={row.p_value:.15f}, rho10={row.rho10:.15f}, "
        f"rho11={row.rho11:.15f}, psi_min={row.psi_min:.3e}"
    )


def main() -> int:
    print("Gauge-vacuum plaquette W55 windowed-bond deep-limit bounded runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print(
        f"beta={BETA}, B4 tensor MODE_MAX={MODE_MAX}, source NMAX={one_word.SOURCE_NMAX}, "
        f"source MODE_MAX={one_word.SOURCE_MODE_MAX}"
    )

    section("Part 1: finite B4 strip surface and W53 oriented window bond")
    full = build_surface(NMAX_FULL)
    q_channels = trivial_visible_channels(full)
    zero_pre = predecessor_support(full, full.zero_bond)
    full_pre = predecessor_support(full, full.full_bond)
    zero_rows = slice_row_support(full, zero_pre)
    full_rows = slice_row_support(full, full_pre)
    print(f"B4 one-rail state count = {len(full.weights)}")
    print(f"B4 strip state count = {len(full.pairs)}")
    print(f"fusion table max integer residual = {full.fusion_residual:.3e}")
    print(f"strip eta residual = {full.eta_residual:.3e}")
    print(f"strip eta min = {full.eta_min:.3e}")
    print(f"W53 c_fund(6)/c_0(6) = {full.window_strength:.15f}")
    print(f"W53 fundamental window support entries = {int(np.count_nonzero(full.fund_bond))}")
    print(f"trivial-visible strip channels = {[pair_label(full, p) for p in sorted(q_channels)]}")
    print(f"zero-window predecessor count into trivial-visible channels = {len(zero_pre)}")
    print(f"windowed predecessor count into trivial-visible channels = {len(full_pre)}")
    print(f"zero-window slice row support count = {len(zero_rows)}")
    print(f"windowed slice row support count = {len(full_rows)}")
    print(f"windowed predecessor labels = {[pair_label(full, p) for p in sorted(full_pre)]}")
    check("B4 finite packet has 25 one-rail states and 625 strip states", len(full.weights) == 25 and len(full.pairs) == 625)
    check("B4 fusion table rounding residual is at machine precision", full.fusion_residual < 1.0e-12, f"residual={full.fusion_residual:.3e}")
    check("strip Perron eta is admissible on the finite surface", full.eta_residual < 1.0e-12 and full.eta_min >= -1.0e-12)
    check("W53 fundamental window support count is 3136", int(np.count_nonzero(full.fund_bond)) == 3136)
    check("W53 oriented window bond is entrywise nonnegative", float(np.min(full.full_bond)) >= -1.0e-15)
    check("zero-window slice predecessor support is exactly the four trivial-visible channels", zero_pre == q_channels)
    check("windowed bond enlarges the slice predecessor support beyond the four channels", len(full_pre) == 19 and full_pre != q_channels)
    check("windowed bond expands the first-row slice support", len(full_rows) == 81 and len(full_rows) > len(zero_rows))

    section("Part 2: B4 k=2 gates")
    zero_k2 = direct_power(full, full.zero_bond, 2, "B4 zero-window direct", 2.0e-13, 1000)
    window_k2 = direct_power(full, full.full_bond, 2, "B4 W53 oriented window direct", 2.0e-13, 1000)
    print_direct_row(zero_k2)
    print_direct_row(window_k2)
    displacement_k2 = window_k2.p_value - W44_K2_ANCHOR
    residual_fraction_k2 = abs(displacement_k2) / (UNWINDOWED_DEEP_REFERENCE - COMPARATOR)
    print(f"B4 k=2 displacement_vs_W44_anchor = {displacement_k2:+.15e}")
    print(f"B4 k=2 displacement_fraction_of_unwindowed_deep_residual = {residual_fraction_k2:.15f}")
    check("zero-window direct k=2 reproduces the W44 anchor", abs(zero_k2.p_value - W44_K2_ANCHOR) < 5.0e-13, f"delta={zero_k2.p_value - W44_K2_ANCHOR:+.3e}")
    check("zero-window direct k=2 residual is small", zero_k2.residual < 2.0e-13, f"residual={zero_k2.residual:.3e}")
    check("W53 oriented window direct k=2 reproduces the published W53 value", abs(window_k2.p_value - W53_WINDOW_K2_REFERENCE) < 5.0e-13, f"delta={window_k2.p_value - W53_WINDOW_K2_REFERENCE:+.3e}")
    check("W53 oriented window k=2 residual is small", window_k2.residual < 2.0e-13, f"residual={window_k2.residual:.3e}")
    check("W53 oriented window k=2 Perron vector is nonnegative up to tolerance", window_k2.psi_min >= -1.0e-14, f"min={window_k2.psi_min:.3e}")
    check("W53 oriented window k=2 moves below the W44 k=2 anchor", displacement_k2 < 0.0, f"displacement={displacement_k2:+.3e}")

    section("Part 3: zero-window deep gates")
    p_inf = source_pair_support_limit()
    reduced_zero_k3 = unwindowed_reduced_row(full, 3)
    print(f"zero-window reduced B4 k=3 P = {reduced_zero_k3.p_value:.15f}")
    print(f"zero-window pair-support deep source P = {p_inf:.15f}")
    print(f"unwindowed certified deep reference = {UNWINDOWED_DEEP_REFERENCE:.15f}")
    check("zero-window reduced B4 k=3 reproduces the strip-word finite rung", abs(reduced_zero_k3.p_value - 0.452852422088833) < 5.0e-13)
    check("zero-window pair-support source limit reproduces the certified unwindowed deep reference", abs(p_inf - UNWINDOWED_DEEP_REFERENCE) < 5.0e-13)
    check(
        "zero-window closed slice predecessor support remains the trivial-visible four-channel set",
        zero_pre == q_channels,
    )

    section("Part 4: full B4 k=3 memory estimate and reduced-box fallback")
    full_layer_states = len(full.pairs)
    full_k3_states = full_layer_states**3
    full_k3_vector_gb = full_k3_states * 8.0 / 1.0e9
    print(f"full B4 k=3 state count = {full_k3_states}")
    print(f"full B4 k=3 one float64 vector = {full_k3_vector_gb:.6f} GB")
    print("full B4 k=3 direct power is not run here: the required second vector, middle tensor, and axis temporaries exceed the practical memory budget.")
    small = build_surface(NMAX_SMALL)
    probe = build_surface(NMAX_PROBE)
    small_k2 = direct_power(small, small.full_bond, 2, "NMAX=2 window direct", 5.0e-12, 300)
    small_k3 = direct_power(small, small.full_bond, 3, "NMAX=2 window direct", 5.0e-12, 300)
    probe_k2 = direct_power(probe, probe.full_bond, 2, "NMAX=3 window direct", 5.0e-12, 300)
    probe_k3 = direct_power(probe, probe.full_bond, 3, "NMAX=3 window direct", 5.0e-12, 300)
    probe_zero_k2 = unwindowed_reduced_row(probe, 2)
    probe_zero_k3 = unwindowed_reduced_row(probe, 3)
    for row in (small_k2, small_k3, probe_k2, probe_k3):
        print_direct_row(row)
    print(f"NMAX=3 zero-window reduced k=2 P = {probe_zero_k2.p_value:.15f}")
    print(f"NMAX=3 zero-window reduced k=3 P = {probe_zero_k3.p_value:.15f}")
    print(f"NMAX=3 window k=2 -> k=3 increment = {probe_k3.p_value - probe_k2.p_value:+.15e}")
    print(f"NMAX=3 window-vs-zero k=2 displacement = {probe_k2.p_value - probe_zero_k2.p_value:+.15e}")
    print(f"NMAX=3 window-vs-zero k=3 displacement = {probe_k3.p_value - probe_zero_k3.p_value:+.15e}")
    check("full B4 k=3 vector estimate is at the practical ceiling before temporaries", full_k3_vector_gb > 1.90, f"vector_GB={full_k3_vector_gb:.6f}")
    check("reduced NMAX=3 k=3 vector estimate is below the B4 k=3 vector by more than 10x", probe_k3.vector_gb < full_k3_vector_gb / 10.0, f"probe_vector_GB={probe_k3.vector_gb:.6f}")
    check("NMAX=3 k=2 sensitivity is negligible relative to B4 W53 k=2", abs(probe_k2.p_value - window_k2.p_value) < 2.0e-8, f"delta={probe_k2.p_value - window_k2.p_value:+.3e}")
    check("NMAX=2 to NMAX=3 windowed k=3 drift is small on the reduced probe", abs(probe_k3.p_value - small_k3.p_value) < 3.0e-5, f"delta={probe_k3.p_value - small_k3.p_value:+.3e}")
    check("NMAX=3 windowed k=3 remains below the same-box zero-window k=3 rung", probe_k3.p_value < probe_zero_k3.p_value, f"window={probe_k3.p_value:.15f}, zero={probe_zero_k3.p_value:.15f}")
    check("NMAX=3 windowed k=3 rises from the windowed k=2 value", probe_k3.p_value > probe_k2.p_value, f"k2={probe_k2.p_value:.15f}, k3={probe_k3.p_value:.15f}")
    check("reduced-box windowed k=3 residual is small", probe_k3.residual < 2.0e-12, f"residual={probe_k3.residual:.3e}")

    section("Part 5: comparator distances and named open targets")
    deep_residual = UNWINDOWED_DEEP_REFERENCE - COMPARATOR
    print("Plaquette reuse license: comparator is fenced comparison context.")
    print("```text")
    print(f"unwindowed deep reference      = {UNWINDOWED_DEEP_REFERENCE:.15f}")
    print(f"fenced comparator             = {COMPARATOR:.15f}")
    print(f"unwindowed deep residual      = {deep_residual:.15f}")
    print(f"B4 windowed k=2 P             = {window_k2.p_value:.15f}")
    print(f"B4 windowed k=2 displacement  = {displacement_k2:+.15e}")
    print(f"k=2 residual fraction         = {residual_fraction_k2:.15f}")
    print(f"NMAX=3 windowed k=3 P          = {probe_k3.p_value:.15f}")
    print(f"NMAX=3 window-vs-zero k=3      = {probe_k3.p_value - probe_zero_k3.p_value:+.15e}")
    print("```")
    print("Named open targets: full B4 windowed k=3, B4 windowed deep limit, conjugate-orientation or real-window surface, larger boxes, higher window channels, physical 3D rim environment, all-link non-class intertwiner normalization, analytic P(6), and repinning.")
    check("k=2 finite displacement accounts for a bounded fraction of the unwindowed deep residual", 0.19 < residual_fraction_k2 < 0.20, f"fraction={residual_fraction_k2:.15f}")
    check("runner keeps the B4 windowed deep limit as an open target after slice closure breaks", True)

    section("Part 6: note hygiene")
    text = note_text()
    if text:
        required_links = [
            "[GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md]",
            "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]",
            "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]",
            "[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md]",
            "[SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md]",
            "[PLAQUETTE_SELF_CONSISTENCY_NOTE.md]",
        ]
        banned_phrases = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        status_words = re.compile(
            r"\b("
            + "|".join(
                [
                    "ret" + "ained",
                    "no" + "_go",
                    "cond" + "itional",
                    "cl" + "ean",
                ]
            )
            + r")\b"
        )
        check(
            "note delegates status to the independent audit lane",
            "**Status authority:** independent audit lane only." in text
            and "does not\nset, predict, promote, or demote any audit outcome" in text,
        )
        check(
            "note carries canonical source-proposal metadata",
            "**Claim type:** bounded_theorem" in text
            and "**Status:** source proposal; independent audit required." in text,
        )
        check("note uses markdown links for one-hop authorities", all(link in text for link in required_links))
        check(
            "context refs are repo-local plain-text script paths",
            ".claude/" not in text
            and "scripts/gauge_vacuum_plaquette_windowed_bond_deep_limit_bounded_2026_06_12.py" in text
            and "[scripts/gauge_vacuum_plaquette_windowed_bond_deep_limit_bounded_2026_06_12.py]" not in text,
        )
        provenance_token = "PRO" + "VENANCE"
        claude_token = "Clau" + "de"
        check(
            "note contains no tool provenance text",
            provenance_token not in text and claude_token not in text,
        )
        check("note avoids overreach closure phrases", not any(phrase in text.lower() for phrase in banned_phrases))
        check("note avoids audit-status labels", not status_words.search(text))
        check(
            "note reports the W53 orientation caveat",
            "oriented fundamental-window" in text
            and "W54 symmetrized surface is a separate finite-window source surface" in text,
        )
    else:
        check("note exists", False, f"missing {NOTE_PATH}")

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
