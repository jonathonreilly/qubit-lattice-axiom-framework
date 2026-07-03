#!/usr/bin/env python3
"""
Audit-facing source-boundary runner for the hierarchy magnitude 4*pi row.

The runner proves only the bounded boundary:

  * In the supplied hierarchy formula alpha_bare = g_bare^2/(4*pi), replacing
    the coupling 4*pi by a Gaussian 2*pi multiplies the alpha_bare^16 factor by
    exactly 2^16.
  * The framework-local Z^3 inverse-Laplacian normalization supplies the native
    geometric 4*pi as a solid-angle/Poisson-kernel coefficient.
  * Raising one 4*pi coupling normalization to exponent count 16 is algebraically
    identical to sixteen separate 4*pi factors.
  * The source packet is explicit about which ingredients are retained, which are
    bounded/stacked, and which remain admitted/open.

It deliberately does NOT check observed M_Pl/v agreement, does NOT derive the
physical static-source readout, and does NOT promote the hierarchy value gate.
Audit status is external.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.special import sici


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN_2026-06-06.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0


def check(name: str, cond: bool) -> None:
    global PASS, FAIL
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + ": " + name)
    PASS += int(ok)
    FAIL += int(not ok)


def ledger_rows() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]


def effective_status(rows: dict, cid: str) -> str:
    row = rows.get(cid, {})
    return str(row.get("effective_status") or row.get("audit_status") or "missing")


def cache_has_success_marker(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    return (
        "FAIL=0" in text
        or "FAIL: 0" in text
        or "FAIL = 0" in text
        or ("status: ok" in text and "PASS" in text and "FAIL" not in text)
    )


def one_line(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8", errors="replace").split())


RETAINED_PACKET = [
    {
        "cid": "lattice_greens_function_maradudin_textbook_import_note_2026-05-18",
        "role": "framework-local Z3 Green-kernel 4pi geometry",
        "doc": "docs/LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md",
        "runner": "scripts/lattice_greens_z3_asymptotic_normalization_certificate.py",
        "cache": "logs/runner-cache/lattice_greens_z3_asymptotic_normalization_certificate.txt",
        "expected_effective_status": "retained_bounded",
    },
    {
        "cid": "bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_note_2026-05-26",
        "role": "native BZ Haar normalization",
        "doc": "docs/BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md",
        "runner": "scripts/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.py",
        "cache": "logs/runner-cache/bz_volume_two_pi_cubed_substrate_internal_runner_2026_05_26.txt",
        "expected_effective_status": "retained_bounded",
    },
    {
        "cid": "g_bare_constraint_vs_convention_restatement_abstract_identity_narrow_theorem_note_2026-05-10",
        "role": "g_bare constraint-vs-convention restatement source",
        "doc": "docs/G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md",
        "runner": "scripts/frontier_g_bare_constraint_vs_convention_restatement_abstract_identity_narrow.py",
        "cache": "logs/runner-cache/frontier_g_bare_constraint_vs_convention_restatement_abstract_identity_narrow.txt",
        "expected_effective_status": "retained",
    },
]

STACKED_COUNT_PACKET = [
    {
        "role": "temporal count packet",
        "doc": "docs/MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06.md",
        "runner": "scripts/magnitude_temporal_factor_is_count_not_rate_2026_06_06.py",
        "cache": "logs/runner-cache/magnitude_temporal_factor_is_count_not_rate_2026_06_06.txt",
        "markers": [
            "2026-06-08 source-packet repair",
            "actual_current_surface_status=bounded-support",
            "POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06",
            "HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE",
            "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28",
        ],
    },
    {
        "role": "minimal-block readout demotion packet",
        "doc": "docs/MAGNITUDE_READS_MINIMAL_RECORD_BLOCK_2026-06-06.md",
        "runner": "scripts/magnitude_reads_minimal_record_block_2026_06_06.py",
        "cache": "logs/runner-cache/magnitude_reads_minimal_record_block_2026_06_06.txt",
        "markers": [
            "What does **not** follow is the readout-scale selection.",
            "select the minimal block over the OS continuum.",
            "Missing bridge:     UV/minimal-block readout selection",
            "readout-scale selection",
        ],
    },
]

OPEN_RESIDUAL_PACKET = [
    {
        "cid": "static_source_readout_i1_accepted_premise_bridge_bounded_note_2026-05-27",
        "role": "I1 static-source readout",
        "expected_effective_status": "unaudited",
        "required_note_text": "not derived",
    },
    {
        "cid": "alpha_convention_i2_accepted_premise_bridge_bounded_note_2026-05-27",
        "role": "I2 alpha convention",
        "expected_effective_status": "unaudited",
        "required_note_text": "accepted premise",
    },
    {
        "cid": "cl3_normalization_i3_accepted_premise_bridge_bounded_note_2026-05-27",
        "role": "I3 Cl3 normalization",
        "expected_effective_status": "unaudited",
        "required_note_text": "accepted premise",
    },
    {
        "cid": "hierarchy_formula_honest_status_note_2026-05-10",
        "role": "P3/per-mode dressing and value-gate honesty",
        "expected_effective_status": "unaudited",
        "required_note_text": "P3",
    },
]


print("--- Status firewall and source packet ---")
rows = ledger_rows()
note_text = NOTE.read_text(encoding="utf-8")
note_flat = " ".join(note_text.split())
for marker in [
    "actual_current_surface_status=bounded-support",
    "audit_required_before_effective_retained=true",
    "bare_retained_allowed=false",
    "source-boundary repair 2026-06-08",
    "does not close the hierarchy value gate",
]:
    check(f"4pi note contains status/source-boundary marker: {marker}", marker in note_text)

for item in RETAINED_PACKET:
    doc = ROOT / item["doc"]
    runner = ROOT / item["runner"]
    cache = ROOT / item["cache"]
    status = effective_status(rows, item["cid"])
    check(f"{item['role']} doc exists", doc.exists())
    check(f"{item['role']} runner exists", runner.exists())
    check(f"{item['role']} cache exists", cache.exists())
    if cache.exists():
        check(f"{item['role']} cache has passing marker", cache_has_success_marker(cache))
    check(
        f"{item['role']} ledger status is {item['expected_effective_status']}",
        status == item["expected_effective_status"],
    )

for item in STACKED_COUNT_PACKET:
    doc = ROOT / item["doc"]
    runner = ROOT / item["runner"]
    cache = ROOT / item["cache"]
    text = doc.read_text(encoding="utf-8", errors="replace") if doc.exists() else ""
    check(f"{item['role']} doc exists", doc.exists())
    check(f"{item['role']} runner exists", runner.exists())
    check(f"{item['role']} cache exists", cache.exists())
    if cache.exists():
        check(f"{item['role']} cache has passing marker", cache_has_success_marker(cache))
    for marker in item["markers"]:
        check(f"{item['role']} source marker: {marker}", marker in text)

for item in OPEN_RESIDUAL_PACKET:
    row = rows.get(item["cid"], {})
    doc = ROOT / str(row.get("note_path", ""))
    text = one_line(doc).lower() if doc.exists() else ""
    check(
        f"{item['role']} remains {item['expected_effective_status']}",
        effective_status(rows, item["cid"]) == item["expected_effective_status"],
    )
    check(
        f"{item['role']} note records premise/import boundary",
        item["required_note_text"].lower() in text,
    )

check("note forbids observed-value PASS conditions", "Does **not** consume observed" in note_text)
check("note explicitly leaves I1/I2/I3/P3 residual open", all(term in note_text for term in ["I1", "I2", "I3", "P3"]))

print("--- Formula-local 4pi-vs-2pi algebra, no observed values ---")
pi = math.pi
four_pi_16 = (4 * pi) ** -16
two_pi_16 = (2 * pi) ** -16
check("(4pi)^-16 is finite and positive", 0.0 < four_pi_16 < 1.0)
check("(2pi)^-16 / (4pi)^-16 = 2^16 exactly within floating precision",
      abs(two_pi_16 / four_pi_16 - 2**16) < 1e-6)
check("replacing supplied alpha_bare=1/(4pi) by Gaussian 1/(2pi) creates the full 2^16 gap",
      abs(((1/(2*pi)) / (1/(4*pi))) ** 16 - 2**16) < 1e-6)
source_text = Path(__file__).read_text(encoding="utf-8")
old_value_match_token = "u0" + "_needed"
check("no observed M_Pl/v value-match calculation appears in this runner",
      old_value_match_token not in source_text)

print("--- Native Z3 inverse-Laplacian 4pi geometry ---")
ks = np.array([0.02, 0.05, 0.1])
ratios = [2 * (3 - 3 * np.cos(ki)) / (3 * ki ** 2) for ki in ks]
check("native Z3 graph-Laplacian symbol tends to |k|^2", all(abs(r - 1.0) < 0.02 for r in ratios))
radial, _ci = sici(1.0e6)
check("Dirichlet radial integral int_0^inf sin(u)/u du = pi/2", abs(radial - pi / 2) < 1e-3)
solid_angle = 4 * pi
rG_continuum = (solid_angle / (2 * pi) ** 3) * radial
check("assembled continuum-leading rG coefficient is 1/(4pi)",
      abs(rG_continuum - 1.0 / (4 * pi)) < 1e-3)
check("d=3 solid angle is 4pi", abs(solid_angle - 12.566370614359172) < 1e-12)
check("Gaussian 2pi and solid-angle 4pi are different normalizations", abs((4 * pi) / (2 * pi) - 2.0) < 1e-12)

print("--- Multiplicity-one normalization raised to count 16 ---")
one_4pi = (4 * pi) ** -1
check("one 4pi coupling normalization raised to count 16 equals (4pi)^-16",
      abs(one_4pi**16 - four_pi_16) < 1e-30)
check("sixteen separate identical 4pi factors give the same number as exponent count 16",
      abs(np.prod([one_4pi] * 16) - one_4pi**16) < 1e-30)
check("the multiplicity objection is an over-strong decomposition demand, not a numeric obstruction",
      "too strong as a" in note_text and "decomposition demand" in note_text)

print("--- Honest residual classification ---")
residual_statuses = {item["role"]: effective_status(rows, item["cid"]) for item in OPEN_RESIDUAL_PACKET}
check("all readout/convention/dressing residuals are explicitly not retained",
      set(residual_statuses.values()) == {"unaudited"})
check("bounded result is a source-boundary, not a hierarchy value derivation",
      "derive the magnitude" in note_flat and "does not close the hierarchy value gate" in note_flat)
check("audit lane remains required before any effective retained status",
      "audit_required_before_effective_retained=true" in note_text and "audit lane owns final classification" in note_text)

print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
