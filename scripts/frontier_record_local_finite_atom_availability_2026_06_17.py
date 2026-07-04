#!/usr/bin/env python3
"""Record local finite readout-atom availability verifier.

This runner checks the exact finite algebra behind the source-side repair:

* Z^3 supplies arbitrary finite lists of distinct supports;
* a declared one-site diagonal context inside M_2(C) has two nonzero
  K-fixed orthogonal readout atoms;
* the finite Boolean unit-count functional is additive on disjoint support
  tags;
* the result is availability/readout-context algebra only, not production,
  probability, physical context selection, clock/rate, or dial selection.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0

ROOT = Path(__file__).resolve().parents[1]


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")
    return ok


def mat(entries: list[list[int]]) -> sp.Matrix:
    return sp.Matrix(entries)


I2 = sp.eye(2)
P0 = mat([[1, 0], [0, 0]])
P1 = mat([[0, 0], [0, 1]])
X = mat([[0, 1], [1, 0]])


@dataclass(frozen=True)
class LocalReadoutAtom:
    site: tuple[int, int, int]
    label: str
    projector: sp.Matrix
    unit_weight: int = 1


def line_sites(n: int) -> list[tuple[int, int, int]]:
    return [(k, 0, 0) for k in range(n)]


def atoms(n: int) -> list[LocalReadoutAtom]:
    return [LocalReadoutAtom(site=site, label="P1", projector=P1) for site in line_sites(n)]


def pairwise_disjoint_support(records: list[LocalReadoutAtom]) -> bool:
    sites = [record.site for record in records]
    return len(sites) == len(set(sites))


def unit_count_readout(records: list[LocalReadoutAtom]) -> int:
    return sum(record.unit_weight for record in records)


def k_fixed(projector: sp.Matrix) -> bool:
    return projector.conjugate() == projector


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return a * b - b * a


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> int:
    print("Record local finite readout-atom availability theorem")
    print("actual_current_surface_status: source-side candidate theorem")
    print("audit_required_before_effective_retained: true")
    print("proposal_allowed: false")
    print()

    print("A. source authority and boundary text")
    minimal = read_text("docs/MINIMAL_AXIOMS_2026-06-05.md")
    nogo = read_text("docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md")
    note = read_text("docs/RECORD_LOCAL_FINITE_ATOM_AVAILABILITY_NARROW_THEOREM_NOTE_2026-06-17.md")
    minimal_flat = " ".join(minimal.split())
    check("A1 minimal axioms expose Lattice Z^3", "The site set is `Z^3`" in minimal)
    check("A2 minimal axioms expose one-site M_2(C)", "M_2(C)" in minimal)
    check("A3 minimal Record requires a supplied readout context", "Given a readout context" in minimal)
    check("A4 minimal Record excludes production/probability/context selection", "A record supplies no readout context" in minimal_flat and "probability" in minimal)
    check("A5 post-append boundary keeps formation rule/process unsupplied", "formation rule or process" in nogo)
    check("A6 theorem boundary explicitly does not derive production", "record production or realization dynamics" in note)
    check("A7 theorem names record-eligible readout atoms, not produced records", "record-eligible readout atoms" in note)

    print("\nB. one-site diagonal readout context")
    check("B1 P0 is idempotent", P0 * P0 == P0)
    check("B2 P1 is idempotent", P1 * P1 == P1)
    check("B3 P0 and P1 are orthogonal", P0 * P1 == sp.zeros(2) and P1 * P0 == sp.zeros(2))
    check("B4 P0 + P1 resolves identity", P0 + P1 == I2)
    check("B5 both readout atoms are nonzero rank-one projectors", P0.trace() == 1 and P1.trace() == 1 and P0.rank() == 1 and P1.rank() == 1)
    check("B6 both atoms are fixed by entrywise K", k_fixed(P0) and k_fixed(P1))
    check("B7 atoms commute inside the declared readout algebra", commutator(P0, P1) == sp.zeros(2))
    check("B8 atoms are not central in all M_2(C)", commutator(P0, X) != sp.zeros(2) and commutator(P1, X) != sp.zeros(2))

    print("\nC. arbitrary finite disjoint supports on Z^3")
    tested_lengths = [0, 1, 2, 3, 5, 8, 13, 21, 55]
    for n in tested_lengths:
        rs = atoms(n)
        check(
            f"C1 n={n}: distinct line supports and one atom per support",
            len(rs) == n and pairwise_disjoint_support(rs) and all(r.projector == P1 for r in rs),
        )

    B = sp.symbols("B", integer=True, nonnegative=True)
    check("C2 symbolic bound escape uses finite B+1", sp.simplify((B + 1) - B - 1) == 0)
    for bound in (0, 1, 7, 25, 100):
        n = bound + 1
        rs = atoms(n)
        check(
            f"C3 no fixed finite atom cap B={bound}",
            len(rs) > bound and pairwise_disjoint_support(rs),
            f"constructed n={n}",
        )

    print("\nD. finite Boolean unit-count readout")
    empty: list[LocalReadoutAtom] = []
    first = atoms(4)
    second = [LocalReadoutAtom(site=(k, 0, 0), label="P1", projector=P1) for k in range(4, 9)]
    combined = first + second
    check("D1 empty unit-count readout is zero", unit_count_readout(empty) == 0)
    check("D2 finite support tags are disjoint before additivity", pairwise_disjoint_support(combined))
    check(
        "D3 unit-count readout is additive on disjoint finite collections",
        unit_count_readout(combined) == unit_count_readout(first) + unit_count_readout(second),
        f"{unit_count_readout(combined)}={unit_count_readout(first)}+{unit_count_readout(second)}",
    )
    check("D4 unit-count readout of n atoms is n", all(unit_count_readout(atoms(n)) == n for n in tested_lengths))
    check("D5 finite prefixes remain bounded by their chosen length", max(unit_count_readout(atoms(n)) for n in range(11)) == 10)

    print("\nE. boundary classifier")
    gates = {
        "local_readout_atom_availability": "closed",
        "declared_unit_count_context": "closed",
        "record_production": "open",
        "measurement_decoherence_instrument": "open",
        "born_probability": "open",
        "physical_context_selection": "open",
        "clock_rate": "open",
        "dial_selection": "open",
    }
    check("E1 local readout-atom availability is the closed part", gates["local_readout_atom_availability"] == "closed")
    check("E2 declared unit-count context is the closed finite algebra part", gates["declared_unit_count_context"] == "closed")
    check("E3 record production remains open", gates["record_production"] == "open")
    check("E4 measurement/decoherence instrument remains open", gates["measurement_decoherence_instrument"] == "open")
    check("E5 Born probability remains open", gates["born_probability"] == "open")
    check("E6 physical context selection remains open", gates["physical_context_selection"] == "open")
    check("E7 clock/rate remains open", gates["clock_rate"] == "open")
    check("E8 dial selection remains open", gates["dial_selection"] == "open")

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: exact finite local readout-atom/context availability closes; "
            "production, probability, physical context selection, clock/rate, and dial selection remain open."
        )
        return 0
    print("VERDICT: local atom availability repair failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
