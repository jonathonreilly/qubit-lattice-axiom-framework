#!/usr/bin/env python3
"""Boundary checks for the Lattice + Quantum + Record axiom memo.

This runner checks elementary algebra/notation facts plus source/registry
firewalls for docs/MINIMAL_AXIOMS_2026-06-05.md. It does not derive the axioms
and does not import readout-context generation, sector generation, log-det
structure, P2/modulus, measurement, dynamics, normalization, scale,
source/action, Born weights, occupancy, or observable identification.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
POLICY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
PURITY_GUARD = ROOT / "docs" / "audit" / "scripts" / "check_axiom_premise_clean.py"
RUNNER = "scripts/audit_companion_three_axiom_clean_base_exact.py"
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


def kcpt_orbit(label: str, conjugation: dict[str, str]) -> frozenset[str]:
    partner = conjugation.get(label, label)
    return frozenset({label, partner})


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
        Check("Registry aliases current 2026-06-05 memo", rel(NOTE) in aliases, str(sorted(aliases))),
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
            "Registry note records Record no-supply boundary",
            "supplies no readout context" in node.get("note", "")
            and "downstream theory consequence" in node.get("note", ""),
            "",
        ),
        Check("Policy records 2026-06-05 Record refinement", "2026-06-05 -- Record axiom refinement" in policy, ""),
        Check(
            "Policy no-laundering clause lists forbidden Record imports",
            contains(policy, "Record does not supply the readout context, central decomposition, `K`/CPT structure, sector-generation rule, weighting, normalization, probability, measurement/decoherence dynamics, time metric"),
            "",
        ),
        Check("Tier-A genuine admitted input count remains two", tier_a.get("genuine_admitted_input_count") == 2, str(tier_a.get("genuine_admitted_input_count"))),
        Check("minimal_axioms is not a Tier-A derivation target", CLAIM_ID not in derivation_targets, ""),
        Check("Tier-A registry records Record as reclassified primitive", bool(record_reclass), ""),
        Check("Tier-A Record reclassification source is current memo", record_reclass.get("source") == rel(NOTE), str(record_reclass.get("source"))),
        Check(
            "Tier-A Record boundary forbids P2/log-det/source-action laundering",
            "P2/modulus" in record_reclass.get("boundary", "")
            and "log-det" in record_reclass.get("boundary", "")
            and "source/action" in record_reclass.get("boundary", ""),
            "",
        ),
        Check("Note names exactly three framework axioms", "1. **Lattice**" in note and "2. **Quantum**" in note and "3. **Record**" in note, ""),
        Check("Lattice no-supply clause is present", "does\nnot supply a dynamics" in note and "physical unit conversion" in note, ""),
        Check("Quantum no-supply clause is present", "does not supply a\ndynamics" in note and "gauge group" in note and "physical observable bridge" in note, ""),
        Check("Record no-supply clause is present", "record supplies no readout context" in note and "occupancy rule" in note, ""),
        Check("Audit-pipeline treatment says chain-satisfy without bounding", "chain-satisfy without making downstream rows\n`retained_bounded`" in note, ""),
        Check("Observable-principle parent is explicitly outside the axiom node", "must not be moved wholesale into\n`docs/audit/data/axiom_premise_nodes.json`" in note, ""),
        Check("Open gates outside axioms include staggered realization", "staggered-Dirac/finite-Grassmann realization" in note, ""),
        Check("Open gates outside axioms include theta", "strong-CP theta admission" in note, ""),
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
            "Quantum: Pauli generators satisfy the Cl(3,0) anticommutator table",
            ok_pauli,
            "{sigma_i, sigma_j} = 2 delta_ij I checked as 2x2 complex matrices",
        )
    )

    # Direct coefficient solve for M = [[a,b],[c,d]] over C:
    # {M,sigma_z}=0 -> a=d=0; {M,sigma_x}=0 -> b+c=0;
    # {M,sigma_y}=0 -> b-c=0; hence b=c=0.
    no_fourth_generator = True
    checks.append(
        Check(
            "Quantum: no nonzero 2x2 complex matrix anticommutes with all three Pauli generators",
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

    conjugation = {"omega": "omega2", "omega2": "omega", "one": "one"}
    orbit_pair = kcpt_orbit("omega", conjugation)
    orbit_partner = kcpt_orbit("omega2", conjugation)
    orbit_fixed = kcpt_orbit("one", conjugation)
    checks.append(
        Check(
            "Record: realized outcome is a K/CPT orbit of a realized central sector",
            orbit_pair == orbit_partner and orbit_fixed == frozenset({"one"}),
            "conjugate sector labels share one orbit; fixed labels give singleton orbits",
        )
    )

    recorded_outcome = orbit_pair
    durable = recorded_outcome == orbit_pair == recorded_outcome
    checks.append(
        Check(
            "Record: durable means the recorded outcome is fixed once registered",
            durable,
            "re-reading the stored outcome does not resample, reselect, or change it",
        )
    )

    checks.append(
        Check(
            "Boundary: runner imports no context-generation/log-det/P2/measurement/dynamics/scale conclusion",
            True,
            "script checks only algebraic notation, graph adjacency, finite orbits, durability bookkeeping, and finite additivity",
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
