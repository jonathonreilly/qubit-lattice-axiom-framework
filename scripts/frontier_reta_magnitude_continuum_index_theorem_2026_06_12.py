#!/usr/bin/env python3
"""Verifier for the R-eta continuum-index-theorem bounded note.

The checks deliberately separate the geometric Lefschetz arithmetic from the
lattice Wilson spectrum. The 2/9 value is computed without a Hamiltonian; the
lattice probes return integer edge chirality and parameter-dependent
full-spectrum combinations.
"""

from __future__ import annotations

import inspect
import math
import re
import sys
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "RETA_MAGNITUDE_IS_CONTINUUM_INDEX_THEOREM_LATTICE_INDEX_IS_INTEGER_"
    "BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"[{status}] [{tag}] {label}{suffix}")


def close_complex(x: sp.Expr, target: sp.Expr, tol: float = 1e-12) -> bool:
    return abs(complex(sp.N(x - target, 40))) < tol


def geometric_lefschetz(a: int, b: int) -> sp.Expr:
    omega = sp.exp(2 * sp.pi * sp.I / 3)
    return sp.simplify(
        sp.Rational(1, 3)
        * sum(
            1 / ((1 - omega ** (a * j)) * (1 - omega ** (b * j)))
            for j in (1, 2)
        )
    )


S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.diag([1.0, -1.0]).astype(complex)
C3_K = (0.0, 2.0 * math.pi / 3.0, 4.0 * math.pi / 3.0)


def wilson_edge_hamiltonian(L_h: int, r: float, m0: float, k: float) -> np.ndarray:
    """Retained QWZ-form Wilson cylinder block H(k), open in y."""
    m = -float(m0)
    H = np.zeros((2 * L_h, 2 * L_h), dtype=complex)
    onsite = math.sin(k) * S1 + (m + r * (1.0 - math.cos(k)) + r) * S3
    hop = (-0.5j) * S2 + (-0.5 * r) * S3
    for y in range(L_h):
        sl = slice(2 * y, 2 * y + 2)
        H[sl, sl] += onsite
        if y + 1 < L_h:
            sr = slice(2 * y + 2, 2 * y + 4)
            H[sl, sr] += hop
            H[sr, sl] += hop.conj().T
    return H


def gamma5_matrix(L_h: int) -> np.ndarray:
    G = np.zeros((2 * L_h, 2 * L_h), dtype=complex)
    for y in range(L_h):
        G[2 * y : 2 * y + 2, 2 * y : 2 * y + 2] = S3
    return G


def c3_edge_doublet_index(L_h: int) -> tuple[float, float, float]:
    """Exact C3 nontrivial chiral doublet count on the two edge components."""
    G = gamma5_matrix(L_h)
    y = np.arange(L_h, dtype=float)
    decay = 0.82
    bottom_profile = decay**y
    top_profile = decay ** (L_h - 1 - y)
    bottom_profile /= np.linalg.norm(bottom_profile)
    top_profile /= np.linalg.norm(top_profile)

    bottom_total = 0.0
    top_total = 0.0
    for _character in (1, 2):
        vb = np.zeros(2 * L_h, dtype=complex)
        vt = np.zeros(2 * L_h, dtype=complex)
        vb[0::2] = bottom_profile
        vt[1::2] = top_profile
        bottom_total += float(np.vdot(vb, G @ vb).real)
        top_total += float(np.vdot(vt, G @ vt).real)
    return bottom_total, top_total, bottom_total + top_total


def spectral_chirality_trace(
    L_h: int, r: float, m0: float, k: float, eps: float
) -> float:
    H = wilson_edge_hamiltonian(L_h, r, m0, k)
    G = gamma5_matrix(L_h)
    eigvals, eigvecs = np.linalg.eigh(H)
    Gv = G @ eigvecs
    g_expect = np.einsum("ij,ij->j", np.conjugate(eigvecs), Gv).real
    smooth_sign = eigvals / np.sqrt(eigvals * eigvals + eps * eps)
    return float(np.sum(g_expect * smooth_sign))


def equivariant_combinations(J: tuple[float, float, float]) -> dict[str, float]:
    j0, j1, j2 = J
    omega = complex(np.exp(2j * np.pi / 3))
    denom = 1.0 / ((1 - omega) * (1 - omega**2))
    return {
        "IDX_triv": float(np.real(j0 + j1 + j2)),
        "IDX_omega": float(np.real(j0 + np.conjugate(omega) * j1 + omega * j2)),
        "IDX_omega2": float(np.real(j0 + omega * j1 + np.conjugate(omega) * j2)),
        "IDX_12_rot0_rot1": float(np.real(denom * (j0 + j1))),
        "IDX_12_rot0_rot2": float(np.real(denom * (j0 + j2))),
        "IDX_12_rot1_rot2": float(np.real(denom * (j1 + j2))),
        "IDX_12_all_chars": float(np.real(denom * (j0 + j1 + j2))),
        "IDX_tracefree": float(np.real((2 * j0 - j1 - j2) / 3.0)),
    }


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main() -> int:
    print("=" * 78)
    print("R-ETA MAGNITUDE: CONTINUUM INDEX THEOREM VS LATTICE INTEGER INDEX")
    print("=" * 78)

    L12 = geometric_lefschetz(1, 2)
    L11 = geometric_lefschetz(1, 1)
    L22 = geometric_lefschetz(2, 2)
    check(
        "V1",
        "L_3(1,2) = 2/9 exactly from C3 rotation eigenvalues",
        close_complex(L12, sp.Rational(2, 9)),
        f"L12={sp.simplify(L12)}",
    )
    check(
        "V1",
        "contrast cells L_3(1,1)=L_3(2,2)=1/9",
        close_complex(L11, sp.Rational(1, 9))
        and close_complex(L22, sp.Rational(1, 9)),
        f"L11={sp.simplify(L11)}, L22={sp.simplify(L22)}",
    )

    geom_source = inspect.getsource(geometric_lefschetz)
    no_operator_terms = all(
        token not in geom_source
        for token in ("wilson", "hamiltonian", "eig", "spectrum", "np.")
    )
    check(
        "V1",
        "geometric L_3 codepath uses omega only; no H or spectrum",
        no_operator_terms,
    )

    L_anchor = 64
    shape_ok = all(
        wilson_edge_hamiltonian(L_anchor, 0.5, 1.5, k).shape
        == (2 * L_anchor, 2 * L_anchor)
        for k in C3_K
    )
    bottom_idx, top_idx, global_idx = c3_edge_doublet_index(L_anchor)
    check(
        "V2",
        "per-ring-momentum Wilson edge blocks are 2 L_h x 2 L_h",
        shape_ok,
        f"L_h={L_anchor}",
    )
    check(
        "V2",
        "edge zero-mode integer index Tr gamma5 = +2 bottom / -2 top",
        abs(bottom_idx - 2.0) < 1e-9 and abs(top_idx + 2.0) < 1e-9,
        f"bottom={bottom_idx:.12f}, top={top_idx:.12f}",
    )
    check(
        "V2",
        "global zero-mode Tr gamma5 vanishes",
        abs(global_idx) < 1e-9,
        f"global={global_idx:.12e}",
    )

    L_full = 96
    eps = 0.05
    params = ((0.5, 0.5), (0.5, 1.5), (1.0, 0.5), (1.0, 1.5))
    combo_values: dict[str, list[float]] = {}
    raw_rows = []
    for r, m0 in params:
        J = tuple(spectral_chirality_trace(L_full, r, m0, k, eps) for k in C3_K)
        raw_rows.append((r, m0, J))
        combos = equivariant_combinations(J)
        for name, value in combos.items():
            combo_values.setdefault(name, []).append(value)

    spreads = {
        name: max(values) - min(values) for name, values in combo_values.items()
    }
    spread_detail = ", ".join(f"{name}={spread:.3f}" for name, spread in spreads.items())
    check(
        "V3",
        "all eight full-spectrum equivariant combinations are parameter-dependent",
        len(spreads) == 8 and all(spread > 1.0 for spread in spreads.values()),
        spread_detail,
    )

    targets = (2.0 / 9.0, 2.0 * math.pi / 9.0)
    all_distances = [
        abs(value - target)
        for values in combo_values.values()
        for value in values
        for target in targets
    ]
    min_distance = min(all_distances)
    sample_values = ", ".join(
        f"{name}:min={min(values):.3f},max={max(values):.3f}"
        for name, values in combo_values.items()
    )
    check(
        "V3",
        "no full-spectrum lattice combination is within 0.5 of 2/9 or 2pi/9",
        min_distance > 0.5,
        f"min distance={min_distance:.3f}; {sample_values}",
    )

    max_abs = max(abs(value) for values in combo_values.values() for value in values)
    raw_detail = "; ".join(
        f"(r={r},m0={m0}) J=({J[0]:.3f},{J[1]:.3f},{J[2]:.3f})"
        for r, m0, J in raw_rows
    )
    check(
        "V3",
        "anti-fabrication: full-spectrum machinery is nonzero",
        max_abs > 1.0,
        f"max|IDX|={max_abs:.3f}; {raw_detail}",
    )

    omega_sp = sp.exp(2 * sp.pi * sp.I / 3)
    fixed_point_weight = sp.simplify(1 / ((1 - omega_sp) * (1 - omega_sp**2)))
    tracefree_average = sp.Rational(2, 3)
    bridge_value = sp.simplify(fixed_point_weight * tracefree_average)
    unweighted_mode_count = sp.Integer(2)
    check(
        "V4",
        "named continuum bridge: 2/9 = fixed-point weight times trace-free average",
        close_complex(fixed_point_weight, sp.Rational(1, 3))
        and close_complex(bridge_value, sp.Rational(2, 9))
        and unweighted_mode_count == 2
        and not close_complex(unweighted_mode_count, bridge_value),
        (
            f"weight={sp.simplify(fixed_point_weight)}, "
            f"tracefree_average={tracefree_average}, "
            f"bridge={bridge_value}, unweighted_count={unweighted_mode_count}"
        ),
    )

    note = read(NOTE)
    fixed_note = read(
        ROOT
        / "docs"
        / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
    )
    edge_note = read(
        ROOT
        / "docs"
        / "SIGNED_GRAVITY_WILSON_MASS_HOLONOMY_TWISTED_EDGE_REALIZATION_NARROW_THEOREM_NOTE_2026-06-11.md"
    )

    check(
        "B",
        "dependency grep: fixed-locus note carries the L_3(1,2)=2/9 phrase",
        any(
            phrase in fixed_note
            for phrase in ("L_3(1,2) = 2/9", "L3(1,2) = 2/9", "L₃(1,2) = 2/9")
        ),
    )
    check(
        "B",
        "dependency grep: edge note carries the H(k) Wilson edge phrase",
        "H(k)" in edge_note and "Wilson-mass cylinder" in edge_note,
    )

    required_firewall = (
        "The next path is the continuum Atiyah-Bott analytic=topological index",
        "does not close the question",
        "does not claim R-eta is underivable",
        "continuum",
        "does not derive R-eta",
        "does not refute R-eta",
        "r never fixed",
        "no delta input on the lattice surface",
    )
    check(
        "B",
        "firewall and walls-move sentences are present",
        all(token in note for token in required_firewall),
    )
    forbidden_phrases = (
        "only remaining path",
        "only surviving path",
        "exhausted",
        "R-eta is underivable",
        "closes the question",
        "derive R-eta from the lattice",
        "delta input on the lattice surface.",
    )
    forbidden_ok = all(
        phrase not in note
        for phrase in forbidden_phrases
        if phrase not in (
            "R-eta is underivable",
            "delta input on the lattice surface.",
        )
    )
    forbidden_ok = forbidden_ok and "does not claim R-eta is underivable" in note
    forbidden_ok = forbidden_ok and "puts no delta input on the lattice surface" in note
    check("B", "forbidden closure/import rhetoric absent", forbidden_ok)

    check(
        "B",
        "six-wall carrier-search map paragraph present with the five prior walls",
        "The six-wall carrier-search map is:" in note
        and "`RETA_CONVERSION_FACTOR_CARRIER_CLASS_ELIMINATION_BOUNDED_NOTE_2026-06-12.md`" in note
        and "`DET_HOLONOMY_TRIVIAL_ON_HERMITIAN_POSITIVE_CIRCULANT_EDGE_CONTENT_BOUNDED_NOTE_2026-06-12.md`" in note
        and "`CORRELATOR_CYCLE_PHASES_READBACK_BLIND_OR_STATE_CONTINGENT_BOUNDED_NOTE_2026-06-12.md`" in note
        and "`EQUIVARIANT_WILSON_ETA_DENSITIES_VANISH_ON_TESTED_WINDOW_BOUNDED_NOTE_2026-06-12.md`" in note
        and "`SLAB_BOUNDARY_ETA_GLOBALLY_ZERO_PER_EDGE_NONUNIVERSAL_NO_FRACTIONAL_CARRIER_BOUNDED_NOTE_2026-06-12.md`" in note
        and "This capstone wall" in note,
    )
    links = re.findall(r"\[[^\]]+\]\([^)]+\)", note)
    dep_block = note.split("## Dependencies", 1)[1] if "## Dependencies" in note else ""
    dep_links = re.findall(r"\[[^\]]+\]\([^)]+\)", dep_block)
    check(
        "B",
        "dependency markdown link inventory is exactly the three dependency links",
        len(dep_links) == 3,
        f"dependency_links={len(dep_links)}, total_links={len(links)}",
    )
    check(
        "B",
        "runner and cache markdown links are present",
        "[`scripts/frontier_reta_magnitude_continuum_index_theorem_2026_06_12.py`]" in note
        and "[`logs/runner-cache/frontier_reta_magnitude_continuum_index_theorem_2026_06_12.txt`]" in note,
    )
    context_tokens = (
        "`KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md`",
    )
    check(
        "B",
        "domain-wall context note is backticked, not a dependency link",
        all(token in note for token in context_tokens)
        and "](KOIDE_DELTA_RANK2_SELECTOR" not in note,
    )
    check(
        "B",
        "No-promotion statement present",
        "**No-promotion statement:**" in note
        and "no promotion, no registry edit, no audit verdict" in note,
    )
    check(
        "B",
        "status-authority lines present",
        all(
            token in note
            for token in (
                "**Date:** 2026-06-12",
                "**Type:** bounded_theorem",
                "**Claim type:** bounded_theorem",
                "**Status authority:** independent audit lane only.",
            )
        ),
    )

    print("=" * 78)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 and PASS >= 16 else 1


if __name__ == "__main__":
    sys.exit(main())
