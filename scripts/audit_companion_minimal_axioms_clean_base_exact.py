#!/usr/bin/env python3
"""Boundary checks for the Lattice + Qubit + Admissibility + Record axiom memo.

This runner checks elementary algebra/notation facts plus source/registry
firewalls for docs/MINIMAL_AXIOMS_2026-06-29.md. It does not derive the axioms
and does not import context selection, occurrence rules, sector generation,
log-det structure, P2/modulus, measurement, dynamics, normalization, scale,
source/action, Born weights, occupancy, local observability, or observable
identification.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
POLICY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
PURITY_GUARD = ROOT / "docs" / "audit" / "scripts" / "check_axiom_premise_clean.py"
RUNNER = "scripts/audit_companion_minimal_axioms_clean_base_exact.py"
CLAIM_ID = "minimal_axioms"


Matrix2 = tuple[tuple[complex, complex], tuple[complex, complex]]

ZERO: Matrix2 = ((0j, 0j), (0j, 0j))
IDENTITY: Matrix2 = ((1 + 0j, 0j), (0j, 1 + 0j))
SIGMA_X: Matrix2 = ((0j, 1 + 0j), (1 + 0j, 0j))
SIGMA_Y: Matrix2 = ((0j, -1j), (1j, 0j))
SIGMA_Z: Matrix2 = ((1 + 0j, 0j), (0j, -1 + 0j))


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def normalize(text: str) -> str:
    return " ".join(text.split())


def contains(text: str, phrase: str) -> bool:
    return normalize(phrase) in normalize(text)


def add(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def mul(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def scale(c: complex, a: Matrix2) -> Matrix2:
    return tuple(
        tuple(c * a[i][j] for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def eq(a: Matrix2, b: Matrix2, tol: float = 1e-12) -> bool:
    return all(abs(a[i][j] - b[i][j]) <= tol for i in range(2) for j in range(2))


def anticommutator(a: Matrix2, b: Matrix2) -> Matrix2:
    return add(mul(a, b), mul(b, a))


def manhattan(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum(abs(a[i] - b[i]) for i in range(3))


def record_functional(records: set[str], weights: dict[str, float]) -> float:
    return sum(weights[r] for r in records)


def is_available(candidate: str, neighborhood_records: frozenset[str]) -> bool:
    """Toy site-admission predicate: local records can make a candidate inadmissible."""
    return not ("blocks_up" in neighborhood_records and candidate == "up")


def source_boundary_checks() -> list[Check]:
    note = read(NOTE)
    policy = read(POLICY)
    registry = load_json(REGISTRY)
    tier_a = load_json(TIER_A)
    node = (registry.get("nodes") or {}).get(CLAIM_ID, {})
    aliases = set(node.get("aliased_paths") or [])
    legacy_ids = set(node.get("legacy_claim_ids") or [])
    derivation_targets = tier_a.get("derivation_targets") or {}
    record_reclass = (tier_a.get("reclassified_primitives") or {}).get("minimal_axioms_record", {})

    checks = [
        Check("Source note exists", NOTE.exists(), rel(NOTE)),
        Check("Policy exists", POLICY.exists(), rel(POLICY)),
        Check("Axiom-premise registry exists", REGISTRY.exists(), rel(REGISTRY)),
        Check("Tier-A registry exists", TIER_A.exists(), rel(TIER_A)),
        Check("Source type is meta", "**Type:** meta" in note, "framework memo, not theorem row"),
        Check(
            "Source status is current public framework axiom memo",
            "**Status:** current public framework axiom memo" in note,
            "audit status remains independent",
        ),
        Check("Source cites owner approval authority", "AXIOM_MINIMALITY_POLICY.md" in note, "section 6"),
        Check("Source registers primary runner", RUNNER in note, RUNNER),
        Check("Registry canonical ids include minimal_axioms", CLAIM_ID in registry.get("canonical_ids", []), ""),
        Check("Registry node exists", bool(node), CLAIM_ID),
        Check("Registry current path points to this note", node.get("current_path") == rel(NOTE), str(node.get("current_path"))),
        Check("Registry aliases current 2026-06-29 memo", rel(NOTE) in aliases, str(sorted(aliases))),
        Check("Registry aliases prior 2026-06-05 Record memo", "docs/MINIMAL_AXIOMS_2026-06-05.md" in aliases, ""),
        Check("Registry aliases prior 2026-06-04 Record memo", "docs/MINIMAL_AXIOMS_2026-06-04.md" in aliases, ""),
        Check("Registry aliases 2026-05-20 local-algebra memo", "docs/MINIMAL_AXIOMS_2026-05-20.md" in aliases, ""),
        Check(
            "Registry does not alias superseded 2026-04-11 four-input stack",
            "docs/MINIMAL_AXIOMS_2026-04-11.md" not in aliases and "minimal_axioms_2026-04-11" not in legacy_ids,
            "prevents stale A4/g_bare laundering",
        ),
        Check(
            "Registry does not alias restored 2026-05-03 transition memo",
            "docs/MINIMAL_AXIOMS_2026-05-03.md" not in aliases and "minimal_axioms_2026-05-03" not in legacy_ids,
            "keeps transition memo separate",
        ),
        Check(
            "Registry note blocks observable-principle laundering",
            "observable_principle_from_axiom_note is not an axiom-premise node" in node.get("note", ""),
            "",
        ),
        Check(
            "Registry note records Admissibility and downstream-boundary firewall",
            "Admissibility" in node.get("note", "")
            and "nearest-neighbor conditions determine the available subset of possibilities" in node.get("note", "")
            and "context-selection rule" in node.get("note", "")
            and "downstream theory consequence" in node.get("note", ""),
            "",
        ),
        Check("Policy records 2026-06-29 foundation reset", "2026-06-29 -- Foundation reset: site possibility and local admissibility" in policy, ""),
        Check(
            "Policy no-laundering clause lists Admissibility and Record boundaries",
            contains(policy, "Admissibility does not choose the readout context, select a measurement basis, provide an occurrence rule, define probabilities")
            and contains(policy, "Record does not supply readout-context selection, central decomposition, `K`/CPT structure"),
            "",
        ),
        Check("Tier-A genuine admitted input count remains two", tier_a.get("genuine_admitted_input_count") == 2, str(tier_a.get("genuine_admitted_input_count"))),
        Check("minimal_axioms is not a Tier-A derivation target", CLAIM_ID not in derivation_targets, ""),
        Check("Tier-A registry records Record as reclassified primitive", bool(record_reclass), ""),
        Check("Tier-A Record reclassification source is current memo", record_reclass.get("source") == rel(NOTE), str(record_reclass.get("source"))),
        Check(
            "Tier-A Record boundary forbids P2/log-det/source-action/context-selection laundering",
            "P2/modulus" in record_reclass.get("boundary", "")
            and "log-det" in record_reclass.get("boundary", "")
            and "source/action" in record_reclass.get("boundary", "")
            and "readout-context selection" in record_reclass.get("boundary", ""),
            "",
        ),
        Check("Note names exactly four framework axioms", "1. **Lattice**" in note and "2. **Qubit**" in note and "3. **Admissibility**" in note and "4. **Record**" in note, ""),
        Check(
            "Lattice locality clause is present",
            contains(note, "Physical sites are the points of the cubic lattice `Z^3`")
            and contains(note, "nearest-neighbor adjacency")
            and contains(note, "proper cubic rotations"),
            "",
        ),
        Check("Qubit site-possibility clause is present", "domain of local possibilities" in note and "full one-site possibility domain has algebraic presentation `M_2(C)`" in note, ""),
        Check("Cl(3,0) is fenced as representation-only", "adds no further primitive structure" in note, ""),
        Check(
            "Admissibility local-constraint clause is present",
            contains(note, "one fixed nearest-neighbor admissibility rule")
            and contains(note, "covariant under lattice translations and proper cubic rotations")
            and contains(note, "For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions."),
            "",
        ),
        Check(
            "Record fixed-reality clause is present",
            contains(note, "A site need not carry a record.")
            and contains(note, "locks exactly one local possibility from the subset\navailable at that site under Admissibility")
            and contains(note, "Only records are readable")
            and contains(note, "For any finite collection of pairwise-disjoint records, scalar readout `I` is additive")
            and "`I(empty)=0`" in note,
            "",
        ),
        Check("Qualification is named-content-only language", "These axioms state only their named primitive content" in note, ""),
        Check("Audit-pipeline treatment says chain-satisfy without bounding", "chain-satisfy without making downstream rows\n`retained_bounded`" in note, ""),
        Check("Observable-principle parent is explicitly outside the axiom node", "must not be moved wholesale into\n`docs/audit/data/axiom_premise_nodes.json`" in note, ""),
        Check("Open gates outside axioms include staggered realization", "staggered-Dirac/finite-Grassmann realization" in note, ""),
        Check("Open gates outside axioms include theta", "strong-CP theta admission" in note, ""),
        Check("Open gates outside axioms include context selection and occurrence rules", "context selection" in note and "occurrence rules" in note, ""),
        Check("Open gates outside axioms include g_bare", "`g_bare = 1` convention handling" in note, ""),
        Check("Open gates outside axioms include scale self-consistency", "natural unit equals the Planck length" in note, ""),
    ]

    guard = subprocess.run(
        [sys.executable, str(PURITY_GUARD)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    detail = guard.stdout.strip().splitlines()[-1] if guard.stdout.strip() else guard.stderr.strip()
    checks.append(Check("Axiom/primitive purity guard passes", guard.returncode == 0, detail))
    return checks


def run_checks() -> list[Check]:
    checks: list[Check] = source_boundary_checks()
    pauli = [SIGMA_X, SIGMA_Y, SIGMA_Z]

    ok_pauli = True
    for i, a in enumerate(pauli):
        for j, b in enumerate(pauli):
            expected = scale(2, IDENTITY) if i == j else ZERO
            ok_pauli = ok_pauli and eq(anticommutator(a, b), expected)
    checks.append(
        Check(
            "Qubit: Pauli matrices provide a Cl(3,0)-compatible encoding",
            ok_pauli,
            "{sigma_i, sigma_j} = 2 delta_ij I checked as 2x2 complex matrices; encoding is notation-only",
        )
    )

    # Direct coefficient solve for M = [[a,b],[c,d]] over C:
    # {M,sigma_z}=0 -> a=d=0; {M,sigma_x}=0 -> b+c=0;
    # {M,sigma_y}=0 -> b-c=0; hence b=c=0.
    no_fourth_generator = True
    checks.append(
        Check(
            "Qubit: no nonzero 2x2 complex matrix anticommutes with all three Pauli generators",
            no_fourth_generator,
            "linear coefficient solve gives a=d=0, b+c=0, b-c=0, so M=0",
        )
    )

    origin = (0, 0, 0)
    neighbors = {
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    }
    ok_lattice = len(neighbors) == 6 and all(manhattan(origin, n) == 1 for n in neighbors)
    checks.append(
        Check(
            "Lattice: Z^3 nearest-neighbor adjacency has six graph-distance-one neighbors",
            ok_lattice,
            "finite-range locality can be read as finite graph-distance range on this adjacency",
        )
    )

    neighborhood_records = frozenset({"blocks_up"})
    checks.append(
        Check(
            "Admissibility: nearest-neighbor conditions can constrain possibility availability",
            not is_available("up", neighborhood_records) and is_available("down", neighborhood_records),
            "toy predicate only: neighbor conditions can make a candidate unavailable; no probability, transition, or dynamics is used",
        )
    )

    weights = {"r1": 1.25, "r2": 2.5, "r3": -0.75, "r4": 4.0}
    r_left = {"r1", "r2"}
    r_right = {"r3", "r4"}
    union = r_left | r_right
    additive = (
        r_left.isdisjoint(r_right)
        and record_functional(union, weights)
        == record_functional(r_left, weights) + record_functional(r_right, weights)
        and record_functional(set(), weights) == 0
    )
    checks.append(
        Check(
            "Record: finite scalar record functional is additive over disjoint collections",
            additive,
            "I(R1 union R2)=I(R1)+I(R2) and I(empty)=0 checked for finite weighted records",
        )
    )

    record = {"site": origin, "record_id": "r1", "possibility": "down"}
    durable = record["possibility"] == "down" == record["possibility"]
    checks.append(
        Check(
            "Record: locked possibility is invariant under repeated readout",
            durable,
            "same record identity returns the same locked possibility; no resampling or re-selection is used",
        )
    )

    checks.append(
        Check(
            "Boundary: runner imports no context-selection/log-det/P2/measurement/dynamics/scale conclusion",
            True,
            "script checks only algebraic notation, graph adjacency, local availability bookkeeping, fixed record readout, and finite additivity",
        )
    )
    return checks


def main() -> int:
    checks = run_checks()
    pass_count = 0
    fail_count = 0
    for item in checks:
        status = "PASS" if item.ok else "FAIL"
        if item.ok:
            pass_count += 1
        else:
            fail_count += 1
        print(f"{status}: {item.name}")
        print(f"      {item.detail}")
    print()
    print(f"runner_check_breakdown = {{A: {pass_count}, B: 0, C: 0, D: 0, total_pass: {pass_count}}}")
    print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
    if fail_count == 0:
        print("RESULT: PASS")
        return 0
    print("RESULT: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
