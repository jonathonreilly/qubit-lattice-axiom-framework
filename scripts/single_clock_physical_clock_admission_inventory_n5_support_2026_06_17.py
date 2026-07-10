#!/usr/bin/env python3
"""Source-inventory support for B-AXIS.3 physical-clock admission.

This runner distinguishes admitted physical-clock transfers from arbitrary
positive finite operators on tensor factors. It intentionally does not prove
that commuting factor transfers are mathematically impossible.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17.md"
SINGLE_CLOCK = ROOT / "docs" / "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
RP2 = ROOT / "docs" / "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
SC2 = ROOT / "docs" / "AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
STONE = ROOT / "docs" / "SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md"
POST_RECORD = ROOT / "docs" / "POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md"

MANIFEST_HEADER = "MANIFEST-VERSION: 2026-07-10"
TRANSFER_MENTION_NEEDLES = (
    "transfer matrix",
    "t_hat",
    "t̂",
    "stone generator",
    "kms",
    "thermal circle",
    "positive factor transfer",
)


@dataclass
class Check:
    ok: bool
    label: str
    detail: str = ""


checks: list[Check] = []


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(ok: bool, label: str, detail: str = "") -> None:
    checks.append(Check(bool(ok), label, detail))
    status = "PASS" if ok else "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {label}{suffix}")


def assert_contains(path: Path, needle: str, label: str | None = None) -> None:
    body = read(path)
    check(needle in body, label or f"{path.name} contains {needle!r}")


def flat(path: Path) -> str:
    return " ".join(read(path).split())


def manifest_lines(note: str) -> list[str]:
    heading = "## Source-Packet Admission Manifest (2026-07-10)"
    start = note.index(heading)
    fence_start = note.index("```text", start) + len("```text")
    fence_end = note.index("```", fence_start)
    return note[fence_start:fence_end].strip().splitlines()


def parse_manifest(note: str) -> tuple[str, list[str], list[dict[str, object]]]:
    """Parse the deliberately small, line-based dated packet manifest."""
    version = ""
    packet_sources: list[str] = []
    candidates: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    in_packet_sources = False

    for raw in manifest_lines(note):
        line = raw.rstrip()
        if line.startswith("MANIFEST-VERSION: "):
            version = line.split(": ", 1)[1]
            in_packet_sources = False
        elif line == "PACKET-SOURCES:":
            in_packet_sources = True
        elif line.startswith("CANDIDATE: "):
            current = {"CANDIDATE": line.split(": ", 1)[1], "RELATED-SOURCE": []}
            candidates.append(current)
            in_packet_sources = False
        elif in_packet_sources and line.startswith("  "):
            packet_sources.append(line.strip())
        elif current is not None and line.startswith("  ") and ": " in line:
            key, value = line.strip().split(": ", 1)
            if key == "RELATED-SOURCE":
                related = current[key]
                assert isinstance(related, list)
                related.append(value)
            elif key == "ADMISSION-NEEDLES":
                current[key] = value.split(" || ")
            else:
                current[key] = value

    return version, packet_sources, candidates


def section(note: str, heading: str) -> str:
    start = note.index(heading)
    end = note.find("\n## ", start + len(heading))
    return note[start:] if end < 0 else note[start:end]


def opnorm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def positive_transfer(generator: np.ndarray, tau: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(generator)
    return vecs @ np.diag(np.exp(-tau * vals)) @ vecs.conj().T


def main() -> int:
    print("single-clock physical-clock admission inventory N5 support")
    print("=" * 72)

    note = read(NOTE)
    assert_contains(NOTE, "ADMITTED_PHYSICAL_CLOCK_TRANSFERS=1")
    assert_contains(NOTE, "MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE")
    assert_contains(NOTE, "Does not mathematically exclude independent commuting transfer factors")
    assert_contains(NOTE, "Does not add an axiom")
    assert_contains(NOTE, "**Claim boundary:** source-inventory support")
    assert_contains(NOTE, "No second physical-clock transfer is currently admitted.")
    assert_contains(NOTE, MANIFEST_HEADER, "note pins the dated admission manifest")
    assert_contains(NOTE, "## Repair Note", "note records the 2026-07-10 repair")
    stale_minimal = "MINIMAL_AXIOMS_" + "2026-" + "06-05"
    check(stale_minimal not in note,
          "note has no stale minimal-axiom markdown link")
    check(stale_minimal not in read(Path(__file__)),
          "runner has no stale minimal-axiom path")

    assert_contains(SINGLE_CLOCK, "(B-AXIS.3)", "single-clock source names B-AXIS.3")
    assert_contains(SINGLE_CLOCK, "admitted\n    as a second physical clock", "B-AXIS.3 is phrased as an admission statement")
    assert_contains(SINGLE_CLOCK, "(T̂², 2a_τ)", "single-clock source names the sole supplied transfer/step pair")
    check("This note **complies** by declaring those clauses as (B-AXIS)" in flat(SINGLE_CLOCK),
          "single-clock source keeps B-AXIS declared")

    minimal_flat = flat(MINIMAL)
    check("does not choose a Hamiltonian or transfer operator" in minimal_flat,
          "current minimal axioms supply no Hamiltonian or transfer")
    check("Further physical structure requires derivation, bridge, explicit admission" in minimal_flat,
          "current minimal axioms require an explicit downstream authority")
    assert_contains(MINIMAL, "define a time metric", "current minimal axioms supply no time metric")
    assert_contains(MINIMAL, "does not derive or enlarge the axiom set", "minimal axiom runner does not enlarge axioms")

    assert_contains(RP2, "2-step blocked transfer matrix", "RP2 supplies the two-step transfer")
    assert_contains(RP2, "positive Hermitian", "RP2 supplies positivity")
    assert_contains(RP2, "single-step transfer operator is NOT positive", "RP2 excludes the single-step object as the physical positive transfer")
    assert_contains(SC2, "2 a_τ", "SC2 supplies the blocked time denominator")
    assert_contains(SC2, "H  :=  -(1/(2 a_τ)) log(T_hat^2 / M_T)", "SC2 supplies corrected log normalization")

    assert_contains(STONE, "given", "Stone note is transfer-relative")
    check("uniquely determined by `T`" in read(STONE), "Stone uniqueness does not add a transfer")
    assert_contains(POST_RECORD, "supplied clock map", "post-record rates require supplied clock map")
    assert_contains(POST_RECORD, "does not supply physical elapsed time", "post-record layer does not derive a clock")

    version, packet_sources, candidates = parse_manifest(note)
    check(version == "2026-07-10", "parsed manifest version is current")
    check(len(packet_sources) == len(set(packet_sources)),
          "packet source enumeration contains no duplicates")
    check(len(candidates) == 5, "manifest enumerates all five inventory rows")
    check(
        {str(candidate["CANDIDATE"]) for candidate in candidates}
        == {
            "T_hat2_two_step",
            "stone_generator",
            "post_record_event_order",
            "local_positive_factor_transfer",
            "kms_apbc_thermal_circle",
        },
        "manifest candidate identifiers match the inventory table",
    )

    definition = section(note, "## Definition: Physical-Clock Admission On This Source Surface")
    computed: dict[str, bool] = {}
    mapped_sources: set[str] = set()
    for candidate in candidates:
        candidate_id = str(candidate["CANDIDATE"])
        kind = str(candidate.get("KIND", ""))
        source_name = candidate.get("SOURCE")
        if source_name is not None:
            mapped_sources.add(str(source_name))
        related = candidate.get("RELATED-SOURCE", [])
        assert isinstance(related, list)
        mapped_sources.update(str(path) for path in related)

        if kind == "supplied-transfer":
            needles = candidate.get("ADMISSION-NEEDLES", [])
            assert isinstance(needles, list)
            source_text = read(ROOT / str(source_name))
            evidence_found = bool(needles) and all(str(needle) in source_text for needle in needles)
            check(evidence_found, f"{candidate_id} admission needles all occur in its source")
            computed[candidate_id] = evidence_found
        else:
            disqualifier = str(candidate.get("DISQUALIFIER", ""))
            if kind == "class-candidate":
                evidence_text = definition
                evidence_surface = "admission definition"
            else:
                evidence_text = read(ROOT / str(source_name))
                evidence_surface = "candidate source"
            evidence_flat = " ".join(evidence_text.split())
            disqualified = bool(disqualifier) and disqualifier in evidence_flat
            check(disqualified, f"{candidate_id} disqualifier occurs in {evidence_surface}")
            computed[candidate_id] = not disqualified

        expected = candidate.get("EXPECTED") == "admitted"
        check(computed[candidate_id] == expected,
              f"{candidate_id} computed admission matches manifest expectation")

    packet_paths = [ROOT / source for source in packet_sources]
    check(all(path.is_file() for path in packet_paths), "every packet source exists")
    check(mapped_sources.issubset(set(packet_sources)),
          "every candidate source mapping belongs to the dated packet")
    for source, path in zip(packet_sources, packet_paths):
        source_lower = read(path).lower()
        mentions = [needle for needle in TRANSFER_MENTION_NEEDLES if needle in source_lower]
        if mentions:
            check(source in mapped_sources,
                  f"transfer mentions in {Path(source).name} map to a manifest candidate",
                  ", ".join(mentions))

    admitted_candidates = [candidate for candidate in candidates if computed[str(candidate["CANDIDATE"])]]
    admitted_pairs = [
        (str(candidate.get("TRANSFER", "")), str(candidate.get("SPACING", "")))
        for candidate in admitted_candidates
    ]
    comparators = [
        {
            "name": "T_A x I",
            "source": "finite tensor-factor comparator",
            "positive_transfer": True,
            "clock_denominator": "arbitrary tau_A",
        },
        {
            "name": "I x T_B",
            "source": "finite tensor-factor comparator",
            "positive_transfer": True,
            "clock_denominator": "arbitrary tau_B",
        },
    ]

    check(len(admitted_candidates) == 1, "computed inventory contains exactly one admitted physical-clock transfer")
    check(admitted_pairs == [("T_hat^2", "2 a_tau")],
          "the admitted transfer is the two-step blocked transfer with denominator 2 a_tau")
    check(sum(computed.values()) == 1,
          "admitted physical-clock count is computed as one after candidate scan")

    ident = np.eye(2)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]])
    h_a = 1.1 * ident + 0.2 * sigma_z
    h_b = 0.8 * ident + 0.3 * sigma_z
    t_a = np.kron(positive_transfer(h_a, 1.0), ident)
    t_b = np.kron(ident, positive_transfer(h_b, 1.4))

    check(np.min(np.linalg.eigvalsh(t_a)) > 0, "mathematical comparator T_A x I is positive")
    check(np.min(np.linalg.eigvalsh(t_b)) > 0, "mathematical comparator I x T_B is positive")
    check(opnorm(t_a @ t_b - t_b @ t_a) < 1e-13,
          "mathematical comparator transfers commute", f"resid={opnorm(t_a @ t_b - t_b @ t_a):.2e}")

    h_a_lift = np.kron(h_a, ident)
    h_b_lift = np.kron(ident, h_b)
    span_rank = np.linalg.matrix_rank(np.stack([h_a_lift.ravel(), h_b_lift.ravel()]), tol=1e-12)
    check(span_rank == 2, "factor comparator tangent space is two-dimensional", f"rank={span_rank}")
    check(sum(1 for c in comparators if c["positive_transfer"]) == 2,
          "two positive factor transfers exist as mathematical comparators")
    counterfactual = dict(computed)
    comparator_id = "local_positive_factor_transfer"
    counterfactual[comparator_id] = True
    counterfactual_is_sole = sum(counterfactual.values()) == 1
    check(sum(counterfactual.values()) == 2 and not counterfactual_is_sole,
          "counterfactual comparator admission visibly breaks sole admission")
    check("not a theorem over all positive operators" in read(NOTE),
          "note states why the support is source-inventory, not algebraic exclusion")

    passed = sum(1 for c in checks if c.ok)
    failed = sum(1 for c in checks if not c.ok)
    print()
    print(f"SUMMARY: PASS={passed} FAIL={failed}")
    admitted_rendered = ", ".join(f"({transfer}, {spacing})" for transfer, spacing in admitted_pairs)
    print(f"COMPUTED_ADMITTED_SET={{{admitted_rendered}}}")
    print(f"ADMITTED_PHYSICAL_CLOCK_TRANSFERS={len(admitted_pairs)}")
    print("B_AXIS_DERIVED=FALSE")
    print("MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
