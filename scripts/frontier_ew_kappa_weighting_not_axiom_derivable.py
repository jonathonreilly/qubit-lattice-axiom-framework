#!/usr/bin/env python3
"""EW kappa_EW is not derivable from the approved axiom baseline alone.

The runner checks repo facts used by the source note: count-versus-weight
algebra, minimal axiom exclusions, primitive registry boundaries, current
Tier-A registry state, and guardrail prose. It does not approve or register
kappa_EW as a Tier-A admission.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
AXIOM_PREMISES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if condition else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(condition)
    FAIL += int(not condition)
    return condition


def section(markdown: str, header: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    grabbing = False
    for line in lines:
        if line.strip().startswith("#"):
            if grabbing:
                break
            grabbing = line.strip().lower().lstrip("# ").startswith(header.lower())
            continue
        if grabbing:
            out.append(line)
    return re.sub(r"\s+", " ", " ".join(out).lower())


def count_weight_check(seed: int = 20260609) -> tuple[bool, str]:
    rng = np.random.default_rng(seed)
    n_color = 3
    matrix = rng.standard_normal((n_color, n_color)) + 1j * rng.standard_normal((n_color, n_color))
    singlet_projection = (np.trace(matrix) / n_color) * np.eye(n_color)
    singlet = float(np.real(np.trace(singlet_projection.conj().T @ singlet_projection)))
    adjoint = float(np.real(np.trace((matrix - singlet_projection).conj().T @ (matrix - singlet_projection))))
    count = (n_color**2 - 1) / n_color**2
    pi_zero = adjoint
    pi_one = adjoint + singlet
    ok = abs(count - 8.0 / 9.0) < 1e-15 and abs(pi_zero - pi_one) > 1e-9 and singlet > 0.0
    return ok, f"count={count:.12f}; Pi(0)={pi_zero:.6f}; Pi(1)={pi_one:.6f}; S={singlet:.6f}"


def primitive_boundary_check() -> tuple[bool, str]:
    registry = json.loads(AXIOM_PREMISES.read_text(encoding="utf-8"))
    nodes = registry["nodes"]
    primitive_ids = {"scale_reference_primitive", "kinetic_isotropy_primitive"}
    has_required = primitive_ids.issubset(set(registry["canonical_ids"]))
    no_kappa_primitive = not any("kappa" in node_id.lower() for node_id in registry["canonical_ids"])

    source_ok = True
    details: list[str] = []
    for primitive_id in primitive_ids:
        source_path = ROOT / nodes[primitive_id]["current_path"]
        source = source_path.read_text(encoding="utf-8").lower()
        mentions_limits = "readout bridge" in source or "dimensionless" in source
        mentions_no_verdict = "does not change any audit verdict" in source
        source_ok = source_ok and mentions_limits and mentions_no_verdict
        details.append(f"{primitive_id}:{source_path.name}")

    return has_required and no_kappa_primitive and source_ok, ", ".join(details)


def tier_a_registry_check() -> tuple[bool, str]:
    registry = json.loads(TIER_A.read_text(encoding="utf-8"))
    ids = [str(item).lower() for item in registry["canonical_ids"]]
    absent = not any("kappa" in item or "ew" in item for item in ids)
    count_ok = registry["genuine_admitted_input_count"] == len(registry["canonical_ids"])
    return absent and count_ok, f"count={registry['genuine_admitted_input_count']}; ids={registry['canonical_ids']}"


def note_guardrails() -> tuple[bool, list[str]]:
    text = re.sub(r"\s+", " ", NOTE.read_text(encoding="utf-8"))
    required = [
        "not derivable from the current approved axiom/primitive baseline alone",
        "candidate admission is descriptive",
        "review-loop does not register it",
        "Cannot claim",
        "No-Go Discipline Gate",
        "OPEN",
        "future derivation, owner-approved admission",
        "Do not audit it as an approved Tier-A",
    ]
    missing = [phrase for phrase in required if phrase not in text]
    return not missing, missing


def sin2_common_factor_cancels() -> tuple[bool, str]:
    g1 = 0.36
    g2 = 0.65
    baseline = g1**2 / (g1**2 + g2**2)
    values = []
    for kappa in (0.0, 0.25, 0.5, 1.0):
        k_factor = 1.0 / (8.0 / 9.0 + kappa / 9.0)
        value = (np.sqrt(k_factor) * g1) ** 2 / (
            (np.sqrt(k_factor) * g1) ** 2 + (np.sqrt(k_factor) * g2) ** 2
        )
        values.append(value)
    return max(abs(value - baseline) for value in values) < 1e-15, "values=" + ", ".join(f"{value:.12f}" for value in values)


def main() -> int:
    print("EW KAPPA WEIGHTING NOT AXIOM-DERIVABLE NO-GO")
    print("=" * 72)

    count_ok, count_detail = count_weight_check()
    check("central-sector count is not the inter-sector kappa_EW weight", count_ok, count_detail)

    axiom_text = AXIOMS.read_text(encoding="utf-8")
    record = section(axiom_text, "Record")
    quantum = section(axiom_text, "Quantum")
    check(
        "Record axiom section explicitly does not supply weighting/readout/normalization",
        all(term in record for term in ("a record supplies no", "readout context", "weighting", "normalization")),
    )
    check(
        "Quantum axiom section explicitly does not supply a physical observable bridge",
        "does not supply" in quantum and "physical observable bridge" in quantum,
    )

    primitive_ok, primitive_detail = primitive_boundary_check()
    check("approved primitives do not include a kappa_EW weighting primitive", primitive_ok, primitive_detail)

    tier_a_ok, tier_a_detail = tier_a_registry_check()
    check("current Tier-A registry does not register kappa_EW", tier_a_ok, tier_a_detail)

    sin2_ok, sin2_detail = sin2_common_factor_cancels()
    check("within the existing construction a common K_EW factor cancels from sin^2(theta_W)", sin2_ok, sin2_detail)

    guardrails_ok, missing = note_guardrails()
    check(
        "source note carries no-go discipline and governance guardrails",
        guardrails_ok,
        "missing guardrails: " + ", ".join(missing) if missing else "all required guardrails present",
    )

    print(f"\nRUNNER STATUS: {'PASS' if FAIL == 0 else 'FAIL'} (PASS={PASS} FAIL={FAIL})")
    print(
        "SCOPE: kappa_EW is not derivable from the current approved axiom/primitive baseline alone; "
        "future derivation or owner-approved admission remains open."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
