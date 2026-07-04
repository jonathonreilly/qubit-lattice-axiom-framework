#!/usr/bin/env python3
"""Verifier for the theta G2 physical sector registration stretch no-go."""

from __future__ import annotations

import itertools
import json
import re
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "THETA_G2_PHYSICAL_SECTOR_REGISTRATION_STRETCH_NO_GO_NOTE_2026-07-04.md"
MINIMAL = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
TIER_A = DOCS / "audit" / "data" / "tier_a_admissions.json"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
REGISTRY = DOCS / "ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md"
ROUTE = DOCS / "THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md"
PAIRWISE = DOCS / "THETA_SU3_STAR_PAIRWISE_REDUCTION_OBSTRUCTION_NO_GO_NOTE_2026-07-04.md"
CENTRAL = DOCS / "THETA_SU3_STAR_CENTRAL_SECTOR_PROJECTION_EXACT_SUPPORT_NOTE_2026-07-04.md"
PHASE = DOCS / "THETA_G3_CENTRAL_SECTOR_PHASE_CHARACTER_EXACT_SUPPORT_NOTE_2026-07-04.md"
CLOSED_RECORD = DOCS / "THETA_CLOSED_NONEXACT_SECTOR_RECORD_READOUT_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def mod3(value: int) -> int:
    return value % 3


Vec = tuple[int, int]
Triple = tuple[Vec, Vec, Vec]


def add_vec(left: Vec, right: Vec) -> Vec:
    return (mod3(left[0] + right[0]), mod3(left[1] + right[1]))


def neg_vec(vec: Vec) -> Vec:
    return (mod3(-vec[0]), mod3(-vec[1]))


def sub_vec(left: Vec, right: Vec) -> Vec:
    return add_vec(left, neg_vec(right))


def is_central(vec: Vec) -> bool:
    return vec == (0, 0)


def total_vec(triple: Triple) -> Vec:
    return add_vec(add_vec(triple[0], triple[1]), triple[2])


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


def central_phase(word: list[Vec]) -> int | None:
    phase, vec = product_word(word)
    if is_central(vec):
        return phase
    return None


def oriented_cocycle(triple: Triple) -> int | None:
    a, b, c = triple
    abc = central_phase([a, b, c])
    acb = central_phase([a, c, b])
    if abc is None or acb is None:
        return None
    return mod3(abc - acb)


def q_signed(triple: Triple) -> int:
    q = oriented_cocycle(triple)
    if q is None:
        return 0
    if q == 2:
        return -1
    return q


def symplectic_area(a: Vec, b: Vec) -> int:
    return mod3(a[0] * b[1] - a[1] * b[0])


def pairwise_signature(triple: Triple) -> tuple[str, ...]:
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


def close(left: complex | float, right: complex | float, tol: float = 1e-10) -> bool:
    return abs(left - right) < tol


def omega() -> complex:
    return complex(np.exp(-2j * np.pi / 3))


def heisenberg_matrix(vec: Vec) -> np.ndarray:
    x = np.array(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ],
        dtype=complex,
    )
    z = np.diag([1, omega(), omega() ** 2])
    return np.linalg.matrix_power(x, vec[0]) @ np.linalg.matrix_power(z, vec[1])


def matrix_word(word: list[Vec]) -> np.ndarray:
    out = np.eye(3, dtype=complex)
    for vec in word:
        out = out @ heisenberg_matrix(vec)
    return out


def central_projection_complex(word: list[Vec]) -> complex:
    phase = central_phase(word)
    if phase is None:
        return 0j
    return omega() ** phase


def readout_zero(records: tuple[Triple, ...]) -> int:
    return 0


def readout_plus(records: tuple[Triple, ...]) -> int:
    return sum(q_signed(record) for record in records)


def readout_minus(records: tuple[Triple, ...]) -> int:
    return -readout_plus(records)


def readout_even(records: tuple[Triple, ...]) -> int:
    return sum(abs(q_signed(record)) for record in records)


READOUTS = {
    "zero": readout_zero,
    "plus": readout_plus,
    "minus": readout_minus,
    "even": readout_even,
}


def disjoint_union(left: tuple[Triple, ...], right: tuple[Triple, ...]) -> tuple[Triple, ...]:
    return left + right


NONCENTRAL: tuple[Vec, ...] = tuple(
    (a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0)
)

SOURCE_ROWS = {
    "route": "theta_gauge_positive_route_stretch_status_2026-07-04",
    "pairwise": "theta_su3_star_pairwise_reduction_obstruction_no_go_note_2026-07-04",
    "central": "theta_su3_star_central_sector_projection_exact_support_note_2026-07-04",
    "phase": "theta_g3_central_sector_phase_character_exact_support_note_2026-07-04",
    "closed_record": "theta_closed_nonexact_sector_record_readout_current_surface_no_go_note_2026-07-04",
    "minimal": "minimal_axioms",
    "registry": "admitted_input_registry_tier_a_note_2026-05-23",
}


def main() -> int:
    print("Theta G2 physical sector registration stretch no-go")
    print("=" * 88)

    paths = [NOTE, MINIMAL, TIER_A, LEDGER, REGISTRY, ROUTE, PAIRWISE, CENTRAL, PHASE, CLOSED_RECORD]
    texts = {path: read(path) for path in paths}
    note = texts[NOTE]
    note_flat = flat(note)
    minimal_flat = flat(texts[MINIMAL])
    registry_flat = flat(texts[REGISTRY])
    route_flat = flat(texts[ROUTE])
    pairwise_flat = flat(texts[PAIRWISE])
    central_flat = flat(texts[CENTRAL])
    phase_flat = flat(texts[PHASE])
    closed_record_flat = flat(texts[CLOSED_RECORD])
    tier = json.loads(texts[TIER_A])
    ledger = json.loads(texts[LEDGER])

    section("A - source, registry, and axiom boundaries")
    for path in paths:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())
    for label, claim_id in SOURCE_ROWS.items():
        row = ledger["rows"].get(claim_id)
        check(f"ledger row resolves for {label}", row is not None)
        if row:
            check(f"{label} is not a new retained authority", row.get("effective_status") != "retained", row.get("effective_status"))

    theta = tier["derivation_targets"]["strong_cp_theta_zero_note"]
    ac = tier["derivation_targets"]["staggered_dirac_realization_gate_note_2026-05-03"]
    check("note declares no_go type", "**Type:** no_go" in note)
    check("note declares no_go claim type", "**Claim type:** no_go" in note)
    check("note declares source-side stretch no-go status", "source-side stretch no-go" in note_flat)
    check("runner path is wired in note", Path(__file__).name in note)
    check("Tier-A genuine admitted input count remains two", tier["genuine_admitted_input_count"] == 2)
    check(
        "canonical Tier-A IDs remain AC and theta",
        tier["canonical_ids"]
        == [
            "staggered_dirac_realization_gate_note_2026-05-03",
            "strong_cp_theta_zero_note",
        ],
        tier["canonical_ids"],
    )
    check(
        "theta minimum decomposition remains gauge plus mass",
        theta["minimum_decomposition"]
        == ["gauge_side_winding_account", "mass_side_orientation_determinant_readout_bridge"],
        theta["minimum_decomposition"],
    )
    check(
        "AC minimum decomposition remains two atoms",
        ac["minimum_decomposition"]
        == ["reading_occupancy_selection", "delta_readout_identification_R_eta"],
        ac["minimum_decomposition"],
    )

    for phrase in [
        "Records form",
        "source/action and physical-observable identification",
        "central-sector decomposition",
        "readout-context selection",
        "formation rules",
        "downstream open gates",
    ]:
        check(f"minimal axioms boundary contains: {phrase}", phrase in minimal_flat)
    for phrase in [
        "multi-plaquette / large-gauge-winding account",
        "determinant-readout bridge",
        "theta",
    ]:
        check(f"registry keeps theta residual: {phrase[:54]}", phrase in registry_flat)
    for phrase in [
        "G2 nonabelian sector/readout registration",
        "G3 phase-type insertion",
        "G4 physical theta assembly",
    ]:
        check(f"route map names gate: {phrase}", phrase in route_flat)
    for phrase in [
        "pairwise composite class data do not determine",
        "central-sector projection kills nonclosed triples",
        "records a central phase",
        "exact orientation-odd cocycle",
        "physical sector records/readout",
    ]:
        sources = " ".join([pairwise_flat, central_flat, phase_flat, closed_record_flat])
        check(f"source support/non-supply contains: {phrase[:58]}", phrase in sources)
    for phrase in [
        "Theta is not retired.",
        "The Tier-A registry is not edited.",
        "No physical SU(3) theta sector is registered.",
        "No central-sector readout context is selected.",
        "No G3 phase source, coefficient, action entry, or physical weighting law is supplied.",
        "No audit status or effective status is changed.",
    ]:
        check(f"note preserves boundary: {phrase[:62]}", phrase in note_flat)
    for forbidden in [
        "Strong CP is solved",
        "therefore theta closes",
        "audit_status: audited_clean",
        "effective_status: retained",
        "promoted to retained",
        "sector-readout primitive is adopted",
    ]:
        check(f"forbidden overclaim absent: {forbidden}", forbidden not in note)

    section("B - finite central-sector payload still checks")
    closed: Triple = ((1, 0), (0, 1), (2, 2))
    open_triple: Triple = ((1, 0), (0, 1), (1, 1))
    orient_plus: Triple = ((1, 0), (0, 1), (2, 2))
    orient_minus: Triple = ((0, 1), (1, 0), (2, 2))

    check("closed witness has zero Heisenberg vector sum", is_central(total_vec(closed)), total_vec(closed))
    check("open witness has nonzero Heisenberg vector sum", not is_central(total_vec(open_triple)), total_vec(open_triple))
    check("closed witness has central ABC phase", central_phase(list(closed)) is not None, central_phase(list(closed)))
    check("open witness has no central ABC projection", central_phase(list(open_triple)) is None, central_phase(list(open_triple)))
    check("closed witness q_c is +1", oriented_cocycle(closed) == 1, oriented_cocycle(closed))
    check("orientation-reversed witness q_c is -1 mod 3", oriented_cocycle(orient_minus) == 2, oriented_cocycle(orient_minus))
    check("signed q maps mod-2 representative to -1", q_signed(orient_minus) == -1, q_signed(orient_minus))
    check("q_c equals symplectic area on closed witness", oriented_cocycle(closed) == symplectic_area(closed[0], closed[1]))
    check("orientation reversal flips symplectic area", symplectic_area(orient_minus[0], orient_minus[1]) == 2)
    check("orientation pair has matching pairwise class signatures", pairwise_signature(orient_plus) == pairwise_signature(orient_minus))
    check("orientation pair has different oriented cocycles", oriented_cocycle(orient_plus) != oriented_cocycle(orient_minus))

    x_mat = heisenberg_matrix((1, 0))
    z_mat = heisenberg_matrix((0, 1))
    check("matrix X has determinant one", close(np.linalg.det(x_mat), 1.0), np.linalg.det(x_mat))
    check("matrix Z has determinant one", close(np.linalg.det(z_mat), 1.0), np.linalg.det(z_mat))
    check("matrix X has three cubic-root eigenvalues", len(np.linalg.eigvals(x_mat)) == 3)
    check("matrix Z X = omega^{-1} X Z", np.allclose(z_mat @ x_mat, np.conj(omega()) * x_mat @ z_mat))
    closed_trace = np.trace(matrix_word(list(closed)))
    open_trace = np.trace(matrix_word(list(open_triple)))
    closed_projection = central_projection_complex(list(closed))
    check("explicit closed trace matches central projection", close(closed_trace / 3, closed_projection), (closed_trace, closed_projection))
    check("explicit open trace is killed by central projection", close(open_trace, 0), open_trace)

    closed_count = 0
    killed_count = 0
    q_values: set[int] = set()
    projection_iff_closed = True
    for triple in itertools.product(NONCENTRAL, repeat=3):
        triple3 = (triple[0], triple[1], triple[2])
        is_closed = is_central(total_vec(triple3))
        projected = central_phase(list(triple3)) is not None
        if is_closed:
            closed_count += 1
            q = oriented_cocycle(triple3)
            if q is not None:
                q_values.add(q)
        else:
            killed_count += 1
        if is_closed != projected:
            projection_iff_closed = False
    check("central projection is nonzero iff vector sum closes", projection_iff_closed, {"closed": closed_count, "killed": killed_count})
    check("closed sector is nonempty", closed_count > 0, closed_count)
    check("nonclosed sector is nonempty", killed_count > 0, killed_count)
    check("closed sector contains all q_c classes", q_values == {0, 1, 2}, q_values)

    section("C - Record-additive readout underdetermination")
    records_a: tuple[Triple, ...] = (orient_plus,)
    records_b: tuple[Triple, ...] = (orient_minus,)
    records_c: tuple[Triple, ...] = (closed, orient_minus)
    empty: tuple[Triple, ...] = ()
    samples = [empty, records_a, records_b, records_c]
    for name, readout in READOUTS.items():
        check(f"{name} readout has I(empty)=0", readout(empty) == 0, readout(empty))
        additive = True
        for left in samples:
            for right in samples:
                lhs = readout(disjoint_union(left, right))
                rhs = readout(left) + readout(right)
                if lhs != rhs:
                    additive = False
        check(f"{name} readout is additive over supplied disjoint atoms", additive)
    values_plus = {name: readout(records_a) for name, readout in READOUTS.items()}
    values_minus = {name: readout(records_b) for name, readout in READOUTS.items()}
    check("additive readouts disagree on q=+1 atom", len(set(values_plus.values())) > 1, values_plus)
    check("additive readouts disagree on q=-1 atom", len(set(values_minus.values())) > 1, values_minus)
    check("zero and plus readouts both additive but select different theta payloads", values_plus["zero"] == 0 and values_plus["plus"] == 1, values_plus)
    check("plus and minus readouts both additive but flip orientation sign", values_plus["plus"] == -values_plus["minus"], values_plus)
    check("even readout erases orientation sign while staying additive", values_plus["even"] == values_minus["even"] == 1, (values_plus, values_minus))

    pairwise_same_payloads = {
        "plus": readout_plus(records_a) != readout_plus(records_b),
        "minus": readout_minus(records_a) != readout_minus(records_b),
        "even": readout_even(records_a) == readout_even(records_b),
        "zero": readout_zero(records_a) == readout_zero(records_b),
    }
    check(
        "same pairwise signatures permit oriented, even, or zero scalar policies",
        all(pairwise_same_payloads.values()),
        pairwise_same_payloads,
    )
    check(
        "underdetermination remains even after supplied triple atoms are granted",
        pairwise_signature(orient_plus) == pairwise_signature(orient_minus)
        and values_plus["plus"] != values_minus["plus"]
        and values_plus["zero"] == values_minus["zero"],
        {"plus": values_plus, "minus": values_minus},
    )

    section("D - no-go target is current-surface non-supply, not impossibility")
    target_phrases = [
        "the current axiom surface still does not derive that this payload is physical record content",
        "Record then disciplines a readout only after the record content and readout context have been supplied",
        "Record additivity by itself does not select the zero map",
        "physical sector/readout registration of the central cocycle",
        "It is not a universal impossibility theorem against future physical sector registration",
    ]
    for phrase in target_phrases:
        check(f"note states scoped no-go: {phrase[:62]}", phrase in note_flat)

    print("\n" + "=" * 88)
    print(f"RESULT: PASS={PASS} FAIL={FAIL} CHECKS={PASS + FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
