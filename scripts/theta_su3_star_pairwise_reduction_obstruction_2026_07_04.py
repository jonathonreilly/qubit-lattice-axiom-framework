#!/usr/bin/env python3
"""Verifier for the theta SU(3) star pairwise-reduction obstruction."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_SU3_STAR_PAIRWISE_REDUCTION_OBSTRUCTION_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
LINK_STAR = DOCS / "THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
CARTAN = DOCS / "THETA_CARTAN_VALUED_CROSS_PLANE_PAIRING_DIAGONAL_WEYL_FRAME_THEOREMS_AND_TRIALITY_FRACTIONAL_VALUES_BOUNDED_THEOREM_NOTE_2026-07-02.md"
POSITIVE_ROUTE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
G3_NO_GO = DOCS / "THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def mod3(value: int) -> int:
    return value % 3


Vec = tuple[int, int]


def add_vec(left: Vec, right: Vec) -> Vec:
    return (mod3(left[0] + right[0]), mod3(left[1] + right[1]))


def neg_vec(vec: Vec) -> Vec:
    return (mod3(-vec[0]), mod3(-vec[1]))


def sub_vec(left: Vec, right: Vec) -> Vec:
    return add_vec(left, neg_vec(right))


def product_word(word: list[Vec]) -> tuple[int, Vec]:
    """Return central phase exponent k and Heisenberg vector for prod X^a Z^b."""

    phase = 0
    a = 0
    b = 0
    for c, d in word:
        phase = mod3(phase + b * c)
        a = mod3(a + c)
        b = mod3(b + d)
    return phase, (a, b)


def is_central(vec: Vec) -> bool:
    return vec == (0, 0)


def trace_real_exact(word: list[Vec]) -> float:
    phase, vec = product_word(word)
    if not is_central(vec):
        return 0.0
    if phase == 0:
        return 3.0
    return -1.5


def dagger_even_triple_invariant(triple: tuple[Vec, Vec, Vec]) -> float:
    a, b, c = triple
    return trace_real_exact([a, b, c]) + trace_real_exact([a, c, b])


def vector_signature(triple: tuple[Vec, Vec, Vec]) -> tuple[str, ...]:
    """Separate plus pairwise composite class data, reduced to SU(3) class type."""

    labels: list[str] = []
    for vec in triple:
        labels.append("central" if is_central(vec) else "noncentral")
    for i in range(3):
        for j in range(i + 1, 3):
            vi = triple[i]
            vj = triple[j]
            labels.append("sum:central" if is_central(add_vec(vi, vj)) else "sum:noncentral")
            labels.append("diff:central" if is_central(sub_vec(vi, vj)) else "diff:noncentral")
            labels.append("diff:central" if is_central(sub_vec(vj, vi)) else "diff:noncentral")
    return tuple(sorted(labels))


def heisenberg_matrix(vec: Vec) -> np.ndarray:
    omega = np.exp(2j * np.pi / 3)
    x = np.array(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ],
        dtype=complex,
    )
    z = np.diag([1, omega, omega**2])
    return np.linalg.matrix_power(x, vec[0]) @ np.linalg.matrix_power(z, vec[1])


def matrix_class_probe(matrix: np.ndarray) -> tuple[complex, complex, complex]:
    return (np.trace(matrix), np.trace(matrix @ matrix), np.linalg.det(matrix))


def close_complex(left: complex, right: complex, tol: float = 1e-10) -> bool:
    return abs(left - right) < tol


def same_probe(left: tuple[complex, complex, complex], right: tuple[complex, complex, complex]) -> bool:
    return all(close_complex(a, b) for a, b in zip(left, right))


def matrix_pairwise_signature(mats: tuple[np.ndarray, np.ndarray, np.ndarray]) -> list[tuple[complex, complex, complex]]:
    probes: list[tuple[complex, complex, complex]] = []
    for mat in mats:
        probes.append(matrix_class_probe(mat))
    for i in range(3):
        for j in range(i + 1, 3):
            mi = mats[i]
            mj = mats[j]
            probes.append(matrix_class_probe(mi @ mj))
            probes.append(matrix_class_probe(mi.conj().T @ mj))
            probes.append(matrix_class_probe(mj.conj().T @ mi))
    return probes


def dagger_even_matrix_value(mats: tuple[np.ndarray, np.ndarray, np.ndarray]) -> float:
    a, b, c = mats
    return float(np.real(np.trace(a @ b @ c) + np.trace(a @ c @ b)))


def main() -> int:
    print("Theta SU(3) star pairwise-reduction obstruction")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    minimal = MINIMAL.read_text(encoding="utf-8")
    tier = json.loads(TIER_A.read_text(encoding="utf-8"))
    registry = REGISTRY.read_text(encoding="utf-8")
    link_star = LINK_STAR.read_text(encoding="utf-8")
    cartan = CARTAN.read_text(encoding="utf-8")
    positive = POSITIVE_ROUTE.read_text(encoding="utf-8")
    g3 = G3_NO_GO.read_text(encoding="utf-8")

    note_flat = flat(note)
    registry_flat = flat(registry)
    link_star_flat = flat(link_star)
    cartan_flat = flat(cartan)
    positive_flat = flat(positive)
    g3_flat = flat(g3)

    section("A - source and registry boundaries")
    for path in [NOTE, MINIMAL, TIER_A, REGISTRY, LINK_STAR, CARTAN, POSITIVE_ROUTE, G3_NO_GO]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("note declares no-go claim type", "**Claim type:** no_go" in note)
    check("runner path is wired in note", Path(__file__).name in note)
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "theta minimum decomposition remains the two residual atoms",
        theta["minimum_decomposition"]
        == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    check(
        "registry names gauge-side winding account",
        "multi-plaquette / large-gauge-winding account" in registry_flat,
    )
    check("minimal axioms withhold source/action", "source/action" in flat(minimal))
    check("link-star note names SU(3) star reduction as open", "SU(3) star reduction" in link_star)
    check("positive route names G2/G3 gates", "G2 nonabelian sector/readout registration" in positive and "G3 phase-type insertion" in positive)
    check("Cartan note names relative-frame correlation residual", "relative-frame correlation" in cartan_flat)
    check("G3 no-go keeps phase insertion open", "phase-type" in g3_flat and "not derived" in g3_flat)

    section("B - exact finite Heisenberg witness")
    closed_sum_triple: tuple[Vec, Vec, Vec] = ((1, 0), (0, 1), (2, 2))
    open_sum_triple: tuple[Vec, Vec, Vec] = ((1, 0), (0, 1), (1, 1))

    for name, triple in [("closed-sum", closed_sum_triple), ("open-sum", open_sum_triple)]:
        check(f"{name} has three noncentral staples", all(not is_central(v) for v in triple), triple)
        pair_sums = [add_vec(triple[i], triple[j]) for i in range(3) for j in range(i + 1, 3)]
        pair_diffs = [sub_vec(triple[i], triple[j]) for i in range(3) for j in range(3) if i != j]
        check(f"{name} pair sums are all noncentral", all(not is_central(v) for v in pair_sums), pair_sums)
        check(f"{name} pair differences are all noncentral", all(not is_central(v) for v in pair_diffs), pair_diffs)

    sig_closed = vector_signature(closed_sum_triple)
    sig_open = vector_signature(open_sum_triple)
    check("separate plus pairwise vector-class signatures match", sig_closed == sig_open, (sig_closed, sig_open))

    closed_abc = product_word(list(closed_sum_triple))
    closed_acb = product_word([closed_sum_triple[0], closed_sum_triple[2], closed_sum_triple[1]])
    open_abc = product_word(list(open_sum_triple))
    open_acb = product_word([open_sum_triple[0], open_sum_triple[2], open_sum_triple[1]])
    check("closed-sum ABC is central with phase omega^2", closed_abc == (2, (0, 0)), closed_abc)
    check("closed-sum ACB is central with phase one", closed_acb == (0, (0, 0)), closed_acb)
    check("open-sum ABC is noncentral", not is_central(open_abc[1]), open_abc)
    check("open-sum ACB is noncentral", not is_central(open_acb[1]), open_acb)

    exact_closed_even = dagger_even_triple_invariant(closed_sum_triple)
    exact_open_even = dagger_even_triple_invariant(open_sum_triple)
    check("closed-sum dagger-even triple invariant is 3/2", abs(exact_closed_even - 1.5) < 1e-12, exact_closed_even)
    check("open-sum dagger-even triple invariant is zero", abs(exact_open_even) < 1e-12, exact_open_even)
    check("same pairwise data but different even triple invariant", abs(exact_closed_even - exact_open_even) > 1.0)

    section("C - matrix-level SU(3) checks")
    mats_closed = tuple(heisenberg_matrix(v) for v in closed_sum_triple)
    mats_open = tuple(heisenberg_matrix(v) for v in open_sum_triple)
    identity = np.eye(3, dtype=complex)

    for name, mats in [("closed-sum", mats_closed), ("open-sum", mats_open)]:
        for idx, mat in enumerate(mats):
            check(f"{name} staple {idx} is unitary", np.linalg.norm(mat.conj().T @ mat - identity) < 1e-12)
            check(f"{name} staple {idx} has determinant one", close_complex(np.linalg.det(mat), 1.0 + 0.0j), np.linalg.det(mat))
            probe = matrix_class_probe(mat)
            check(f"{name} staple {idx} is traceless noncentral class", abs(probe[0]) < 1e-12 and abs(probe[1]) < 1e-12, probe)

    sig_m_closed = matrix_pairwise_signature(mats_closed)
    sig_m_open = matrix_pairwise_signature(mats_open)
    check("matrix pairwise signature lengths match", len(sig_m_closed) == len(sig_m_open), (len(sig_m_closed), len(sig_m_open)))
    check("all matrix pairwise probes match", all(same_probe(a, b) for a, b in zip(sig_m_closed, sig_m_open)))

    numeric_closed_even = dagger_even_matrix_value(mats_closed)
    numeric_open_even = dagger_even_matrix_value(mats_open)
    check("matrix closed-sum even invariant matches exact value", abs(numeric_closed_even - exact_closed_even) < 1e-10, numeric_closed_even)
    check("matrix open-sum even invariant matches exact value", abs(numeric_open_even - exact_open_even) < 1e-10, numeric_open_even)

    for name, mats in [("closed-sum", mats_closed), ("open-sum", mats_open)]:
        daggered = tuple(mat.conj().T for mat in mats)
        check(
            f"{name} even invariant is stable under simultaneous dagger",
            abs(dagger_even_matrix_value(daggered) - dagger_even_matrix_value(mats)) < 1e-10,
        )

    section("D - obstruction and scope guards")
    check("note states pairwise-reduction shortcut is pruned", "pairwise-reduction shortcut is pruned" in note_flat)
    check("note states theta is not retired", "Theta is not retired" in note)
    check("note states Tier-A registry is not edited", "The Tier-A registry is not edited" in note)
    check("note preserves phase-source route", "phase-source theorem remains open" in note_flat)
    check("note preserves sector-level route", "sector-level SU(3) star/readout route remains open" in note_flat)
    check("note classifies support as source-side no-go", "source-side no-go" in note_flat)

    banned = [
        "theta is derived",
        "theta is retired",
        "theta_bar = 0 is derived",
        "Tier-A registry is edited",
        "SU(3) sector is physically registered",
        "phase insertion is now derived",
        "all gauge-side routes are closed",
        "audited_clean",
        "retained_no_go",
    ]
    found = [phrase for phrase in banned if phrase in note]
    check("banned overclaim phrases are absent", not found, found)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
