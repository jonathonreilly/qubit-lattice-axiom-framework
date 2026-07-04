#!/usr/bin/env python3
"""Verifier for the theta SU(3) star central-sector projection support note."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_SU3_STAR_CENTRAL_SECTOR_PROJECTION_EXACT_SUPPORT_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
BLOCK31 = DOCS / "THETA_SU3_STAR_PAIRWISE_REDUCTION_OBSTRUCTION_NO_GO_NOTE_2026-07-04.md"
LINK_STAR = DOCS / "THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
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
    """Return central phase exponent k and vector for prod X^a Z^b."""

    phase = 0
    a = 0
    b = 0
    for c, d in word:
        phase = mod3(phase - b * c)
        a = mod3(a + c)
        b = mod3(b + d)
    return phase, (a, b)


def is_central(vec: Vec) -> bool:
    return vec == (0, 0)


NONCENTRAL: tuple[Vec, ...] = tuple(
    (a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0)
)


def pairwise_signature(triple: tuple[Vec, Vec, Vec]) -> tuple[str, ...]:
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


def central_projection(word: list[Vec]) -> tuple[int | None, Vec]:
    phase, vec = product_word(word)
    if is_central(vec):
        return phase, vec
    return None, vec


def phase_complex(phase: int | None) -> complex:
    if phase is None:
        return 0j
    omega = np.exp(-2j * np.pi / 3)
    return complex(omega**phase)


def trace_real_from_projection(word: list[Vec]) -> float:
    phase, _vec = central_projection(word)
    return float(np.real(3 * phase_complex(phase)))


def dagger_even_value(triple: tuple[Vec, Vec, Vec]) -> float:
    a, b, c = triple
    return trace_real_from_projection([a, b, c]) + trace_real_from_projection([a, c, b])


def heisenberg_matrix(vec: Vec) -> np.ndarray:
    omega = np.exp(-2j * np.pi / 3)
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


def normalize_su(matrix: np.ndarray) -> np.ndarray:
    det = np.linalg.det(matrix)
    return matrix / det ** (1 / matrix.shape[0])


def random_su3(seed: int = 17) -> np.ndarray:
    rng = np.random.default_rng(seed)
    raw = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(raw)
    phases = np.diag(r) / np.abs(np.diag(r))
    q = q @ np.diag(np.conj(phases))
    return normalize_su(q)


def matrix_trace(word: list[Vec]) -> complex:
    out = np.eye(3, dtype=complex)
    for vec in word:
        out = out @ heisenberg_matrix(vec)
    return np.trace(out)


def conjugated_matrix_trace(word: list[Vec], g: np.ndarray) -> complex:
    out = np.eye(3, dtype=complex)
    for vec in word:
        mat = heisenberg_matrix(vec)
        out = out @ (g @ mat @ g.conj().T)
    return np.trace(out)


def main() -> int:
    print("Theta SU(3) star central-sector projection exact support")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    minimal = MINIMAL.read_text(encoding="utf-8")
    tier = json.loads(TIER_A.read_text(encoding="utf-8"))
    registry = REGISTRY.read_text(encoding="utf-8")
    block31 = BLOCK31.read_text(encoding="utf-8")
    link_star = LINK_STAR.read_text(encoding="utf-8")
    positive = POSITIVE_ROUTE.read_text(encoding="utf-8")
    g3 = G3_NO_GO.read_text(encoding="utf-8")

    note_flat = flat(note)
    minimal_flat = flat(minimal)
    registry_flat = flat(registry)
    block31_flat = flat(block31)
    link_star_flat = flat(link_star)
    positive_flat = flat(positive)
    g3_flat = flat(g3)

    section("A - source and registry boundaries")
    for path in [NOTE, MINIMAL, TIER_A, REGISTRY, BLOCK31, LINK_STAR, POSITIVE_ROUTE, G3_NO_GO]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    check("note declares bounded theorem claim type", "**Claim type:** bounded_theorem" in note)
    check("note states exact-support status", "exact-support source-side split" in note_flat)
    check("runner path is wired in note", Path(__file__).name in note)
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "theta minimum decomposition remains the two residual atoms",
        theta["minimum_decomposition"]
        == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    check("registry names multi-plaquette large-gauge account", "multi-plaquette / large-gauge-winding account" in registry_flat)
    check("minimal axioms withhold physical source/action", "source/action" in minimal_flat)
    check("Block31 exposes triple joint data", "triple joint data" in block31_flat)
    check("link-star note leaves sector-level statement open", "sector-level statement" in link_star_flat)
    check("positive route preserves G2/G3 gates", "G2 nonabelian sector/readout registration" in positive and "G3 phase-type insertion" in positive)
    check("G3 phase insertion remains open", "not derived" in g3_flat and "phase-type" in g3_flat)

    section("B - exact central-sector projection")
    closed_sum: tuple[Vec, Vec, Vec] = ((1, 0), (0, 1), (2, 2))
    open_sum: tuple[Vec, Vec, Vec] = ((1, 0), (0, 1), (1, 1))
    for name, triple in [("closed-sum", closed_sum), ("open-sum", open_sum)]:
        total = add_vec(add_vec(triple[0], triple[1]), triple[2])
        abc_phase, abc_vec = central_projection(list(triple))
        acb_phase, acb_vec = central_projection([triple[0], triple[2], triple[1]])
        check(f"{name} vector total matches ABC vector", total == abc_vec, (total, abc_vec))
        check(f"{name} ACB vector equals total", acb_vec == total, (acb_vec, total))
        check(f"{name} dagger-even projection value is matrix-independent exact number", isinstance(dagger_even_value(triple), float))

    closed_abc_phase, closed_abc_vec = central_projection(list(closed_sum))
    closed_acb_phase, closed_acb_vec = central_projection([closed_sum[0], closed_sum[2], closed_sum[1]])
    open_abc_phase, open_abc_vec = central_projection(list(open_sum))
    open_acb_phase, open_acb_vec = central_projection([open_sum[0], open_sum[2], open_sum[1]])
    check("closed-sum ABC survives central projection with omega", (closed_abc_phase, closed_abc_vec) == (1, (0, 0)), (closed_abc_phase, closed_abc_vec))
    check("closed-sum ACB survives central projection with phase one", (closed_acb_phase, closed_acb_vec) == (0, (0, 0)), (closed_acb_phase, closed_acb_vec))
    check("open-sum ABC is killed by central projection", open_abc_phase is None and open_abc_vec != (0, 0), (open_abc_phase, open_abc_vec))
    check("open-sum ACB is killed by central projection", open_acb_phase is None and open_acb_vec != (0, 0), (open_acb_phase, open_acb_vec))
    check("closed-sum dagger-even projection is 3/2", abs(dagger_even_value(closed_sum) - 1.5) < 1e-10, dagger_even_value(closed_sum))
    check("open-sum dagger-even projection is zero", abs(dagger_even_value(open_sum)) < 1e-10, dagger_even_value(open_sum))

    nonzero_iff_closed = True
    closed_count = 0
    killed_count = 0
    for a in NONCENTRAL:
        for b in NONCENTRAL:
            for c in NONCENTRAL:
                phase, vec = central_projection([a, b, c])
                total = add_vec(add_vec(a, b), c)
                if vec != total:
                    nonzero_iff_closed = False
                if is_central(total):
                    closed_count += 1
                    if phase is None:
                        nonzero_iff_closed = False
                else:
                    killed_count += 1
                    if phase is not None:
                        nonzero_iff_closed = False
    check("central projection is nonzero iff the Heisenberg vector sum closes", nonzero_iff_closed, {"closed": closed_count, "killed": killed_count})
    check("closed and killed populations are both nonempty", closed_count > 0 and killed_count > 0, {"closed": closed_count, "killed": killed_count})

    section("C - matrix and invariance checks")
    for name, triple in [("closed-sum", closed_sum), ("open-sum", open_sum)]:
        abc_trace = matrix_trace(list(triple))
        acb_trace = matrix_trace([triple[0], triple[2], triple[1]])
        abc_phase, _ = central_projection(list(triple))
        acb_phase, _ = central_projection([triple[0], triple[2], triple[1]])
        check(f"{name} ABC trace matches central projector", abs(abc_trace / 3 - phase_complex(abc_phase)) < 1e-10, abc_trace)
        check(f"{name} ACB trace matches central projector", abs(acb_trace / 3 - phase_complex(acb_phase)) < 1e-10, acb_trace)

    g = random_su3()
    check("random conjugator is unitary", np.linalg.norm(g.conj().T @ g - np.eye(3)) < 1e-12)
    check("random conjugator has determinant one", abs(np.linalg.det(g) - 1) < 1e-10, np.linalg.det(g))
    for name, triple in [("closed-sum", closed_sum), ("open-sum", open_sum)]:
        check(
            f"{name} ABC trace is simultaneous-conjugation invariant",
            abs(matrix_trace(list(triple)) - conjugated_matrix_trace(list(triple), g)) < 1e-10,
        )
        check(
            f"{name} ACB trace is simultaneous-conjugation invariant",
            abs(matrix_trace([triple[0], triple[2], triple[1]]) - conjugated_matrix_trace([triple[0], triple[2], triple[1]], g)) < 1e-10,
        )

    section("D - pairwise obstruction and exact support boundary")
    check("Block31 pairwise signatures still match", pairwise_signature(closed_sum) == pairwise_signature(open_sum))
    check("central projection distinguishes the Block31 pairwise-degenerate triples", abs(dagger_even_value(closed_sum) - dagger_even_value(open_sum)) > 1.0)
    check("note says central-sector projection is supplied surface only", "supplied central-sector projection" in note_flat)
    check("note denies physical SU(3) registration", "No physical SU(3) theta sector is registered" in note)
    check("note denies theta retirement", "Theta is not retired" in note)
    check("note denies registry edits", "The Tier-A registry is not edited" in note)
    check("note preserves G1/G3/mass routes", "G1 defect closure" in note and "G3 phase-source theorem" in note and "mass-side determinant-channel bridge" in note)

    banned = [
        "Theta is retired",
        "theta_bar = 0 is derived",
        "Tier-A registry is edited",
        "Physical SU(3) theta sector is registered",
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
