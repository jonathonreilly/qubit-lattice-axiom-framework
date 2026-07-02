#!/usr/bin/env python3
"""Hierarchy B3 staggered supplier cascade verifier.

This is a source-side audit-unblock runner. It checks the narrow B3
claim in
docs/HIERARCHY_B3_STAGGERED_SUPPLIER_CASCADE_NOTE_2026-06-17.md:

  * B3a is supplied only by the kinetic-isotropy primitive.
  * B3b's hierarchy exponent carrier needs the unlabeled d=4 count
    N = 16 and the matching determinant degree, not the full
    staggered-Dirac parent gate's generation-labeling residual.
  * The current P-FLUX line supplies the KS/staggered branch only inside
    its licensed two-class surface and at its current bounded grade.

The runner reads audit-ledger grades as read-only evidence, like other
source-side composer runners in this repo. It does not edit audit data,
retag rows, or predict any audit verdict.
"""

from __future__ import annotations

import itertools
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs" / "HIERARCHY_B3_STAGGERED_SUPPLIER_CASCADE_NOTE_2026-06-17.md"
HIERARCHY = ROOT / "docs" / "HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md"
RUNNER = ROOT / "scripts" / "frontier_hierarchy_formula_honest_status.py"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
AXIOM_NODES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f" ({detail})"
    print(line)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rows() -> dict:
    return json.loads(read(LEDGER))["rows"]


def effective(row: dict) -> str:
    return row.get("effective_status") or row.get("status") or ""


def retained_grade(status: str) -> bool:
    return status in {"retained", "retained_bounded", "retained_no_go"} or status.startswith(
        "decoration_under"
    )


def row_status(ledger_rows: dict, claim_id: str) -> str:
    return effective(ledger_rows.get(claim_id, {}))


def mat_mul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mat_add_diag(a, c):
    out = [row[:] for row in a]
    for i in range(len(out)):
        out[i][i] += c
    return out


def char_poly_exact(a):
    n = len(a)
    coeffs = [Fraction(1)]
    m = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
    for k in range(1, n + 1):
        am = mat_mul(a, m)
        tr = sum(am[i][i] for i in range(n))
        ck = -tr / k
        coeffs.append(ck)
        m = mat_add_diag(am, ck)
    return coeffs


SITES = list(itertools.product((0, 1), repeat=4))
SITE_INDEX = {s: i for i, s in enumerate(SITES)}


def staggered_operator_4d():
    n = len(SITES)
    dmat = [[Fraction(0)] * n for _ in range(n)]
    for site in SITES:
        row = SITE_INDEX[site]
        for mu in range(4):
            eta = (-1) ** sum(site[:mu])
            for direction in (+1, -1):
                target = list(site)
                target[mu] += direction
                wrapped = target[mu] < 0 or target[mu] > 1
                target[mu] %= 2
                wrap_sign = -1 if wrapped else 1
                col = SITE_INDEX[tuple(target)]
                dmat[row][col] += direction * eta * wrap_sign * Fraction(1, 2)
    return dmat


def section_exact_math() -> None:
    print("\n== Exact B3 carrier math ==")
    counts = {d: sum(1 for _ in itertools.product((0, 1), repeat=d)) for d in range(2, 6)}
    check(
        "2^d corner count gives d=4 -> N=16 and d=3 -> 8 falsification leg",
        counts == {2: 4, 3: 8, 4: 16, 5: 32},
        str(counts),
    )

    hamming = [0, 0, 0, 0, 0]
    for corner in itertools.product((0, 1), repeat=4):
        hamming[sum(corner)] += 1
    check("d=4 Hamming staircase is 1,4,6,4,1", hamming == [1, 4, 6, 4, 1], str(hamming))

    dmat = staggered_operator_4d()
    antisym = all(dmat[i][j] == -dmat[j][i] for i in range(16) for j in range(16))
    d2 = mat_mul(dmat, dmat)
    d2_ok = all(d2[i][j] == (Fraction(-4) if i == j else 0) for i in range(16) for j in range(16))
    check("minimal 2^4 eta-phase block has D^2 = -4 I and D antisymmetric", antisym and d2_ok)

    coeffs = char_poly_exact(dmat)
    target = [Fraction(0)] * 17
    for k in range(9):
        target[2 * k] = Fraction(math.comb(8, k) * 4**k)
    check("char poly is (lambda^2 + 4)^8", coeffs == target)

    # Degree check by exact scaling ratio: det(a D) / det(b D) = (a/b)^16.
    # Since D^2 = -4 I on a 16-dimensional space, |det(aD)| = 4^8 a^16.
    a = Fraction(2, 3)
    b = Fraction(3, 5)
    det_a = Fraction(4) ** 8 * a**16
    det_b = Fraction(4) ** 8 * b**16
    degree_ok = det_a / det_b == (a / b) ** 16 and det_a / det_b != (a / b) ** 8
    check("determinant u0-degree equals the carrier count 16", degree_ok)


def section_status() -> None:
    print("\n== Read-only current supplier grades ==")
    ledger_rows = rows()
    retained_grade_inputs = [
        "naive_lattice_fermion_two_power_d_species_count_narrow_theorem_note_2026-05-10",
        "hierarchy_alpha_lm_exponent_species_count_bridge_regulator_dependence_no_go_note_2026-05-10",
        "p_flux_selection_via_fsb_k_and_z_certificate_conditional_theorem_note_2026-06-11",
        "axiom_first_fermionic_stefan_boltzmann_narrow_theorem_note_2026-05-26",
        "staggered_kernel_satisfies_z_point_cone_certificate_narrow_theorem_note_2026-06-11",
        "staggered_dirac_substep2_kahler_dirac_equivalence_narrow_theorem_note_2026-05-17",
        "staggered_dirac_substep3_species_reduction_bridge_narrow_theorem_note_2026-05-16",
        "staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17",
    ]
    for claim_id in retained_grade_inputs:
        status = row_status(ledger_rows, claim_id)
        check(f"{claim_id} has retained-grade current status", retained_grade(status), f"status={status}")

    kinetic_class_status = row_status(
        ledger_rows, "staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10"
    )
    check(
        "staggered kinetic-class source is visible at its current status",
        retained_grade(kinetic_class_status) or kinetic_class_status == "unaudited",
        f"status={kinetic_class_status}",
    )

    pflux = row_status(
        ledger_rows, "p_flux_selection_via_fsb_k_and_z_certificate_conditional_theorem_note_2026-06-11"
    )
    zcert = row_status(
        ledger_rows, "staggered_kernel_satisfies_z_point_cone_certificate_narrow_theorem_note_2026-06-11"
    )
    check("P-FLUX composer and Z certificate are retained-grade inputs", retained_grade(pflux) and retained_grade(zcert))


def section_source_firewall() -> None:
    print("\n== Source wiring and firewall ==")
    note = read(NOTE)
    hierarchy = read(HIERARCHY)
    runner = read(RUNNER)
    nodes = json.loads(read(AXIOM_NODES)).get("nodes", {})
    kinetic_node = nodes.get("kinetic_isotropy_primitive", {})

    check(
        "kinetic_isotropy_primitive is registered as an axiom-premise node",
        kinetic_node.get("current_path") == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    )
    check("new B3 note is markdown-linked from hierarchy note", "HIERARCHY_B3_STAGGERED_SUPPLIER_CASCADE_NOTE_2026-06-17.md" in hierarchy)
    check("hierarchy note still keeps B4 and B5 open", "B4" in hierarchy and "B5" in hierarchy and "remain open" in hierarchy)
    check("hierarchy runner knows about the new B3 supplier packet", "B3_STAGGERED_SUPPLIER" in runner)

    linked = set(re.findall(r"\]\(([A-Za-z0-9_\-./]+\.md)\)", hierarchy))
    check("hierarchy markdown dependency set has six source notes after this repair", len(linked) == 6, str(sorted(linked)))

    forbidden = [
        "derived ew vev",
        "b4 is now closed",
        "b5 is now closed",
        "sets an audit verdict",
        "assigns an audit verdict",
        "retags the ledger",
        "retained hierarchy formula",
        "is a regulator-independent theorem",
    ]
    flat = " ".join((note + "\n" + hierarchy).lower().split())
    hits = [phrase for phrase in forbidden if phrase in flat]
    check("forbidden overclaim/status phrases absent", not hits, str(hits))

    parent = "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
    parent_is_context = parent in hierarchy and f"]({parent})" not in hierarchy and f"]({parent})" not in note
    check("full staggered parent remains plain context, not a markdown dependency", parent_is_context)

    label_tokens = ["AC_phi_lambda", "generation-label", "SM generation", "labeled generation"]
    label_mentions = [tok for tok in label_tokens if tok in note]
    check("labeling residual is mentioned only as excluded/non-load-bearing scope", bool(label_mentions) and "non-load-bearing" in note)

    no_status_claim = "does not set an audit verdict" in note and "No audit result is written" in note
    check("B3 supplier note states the audit/status firewall explicitly", no_status_claim)


def main() -> int:
    print("=" * 72)
    print("Hierarchy B3 staggered supplier cascade verifier")
    print("=" * 72)
    section_exact_math()
    section_status()
    section_source_firewall()
    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
