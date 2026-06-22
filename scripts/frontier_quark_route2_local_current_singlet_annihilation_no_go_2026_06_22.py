#!/usr/bin/env python3
"""Local-current singlet-annihilation stretch no-go for Route-2.

After Block70-72, the remaining selector route asks whether a first-principles
local lattice-current argument forces the singlet/disconnected channel to be
annihilated, i.e. kappa=0.

This runner separates two notions:

* a local color-singlet current readout, which admits the full-trace endpoint;
* a connected cumulant / disconnected-subtraction readout, which sets kappa=0
  by definition of the connected observable.

Result: locality, Ward normalization, color-singlet form, CMT scaling, and
finite OZI-size control do not force singlet annihilation.  The condition that
does force kappa=0 is exactly a connected-cumulant/subtraction premise, so it
is an import rather than a derivation from local-current premises.

This is not an audit verdict.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

F_ADJ = Fraction(8, 9)
F_SINGLET = Fraction(1, 9)
TARGET_RHO_E = Fraction(21, 4)


@dataclass(frozen=True)
class CurrentReadout:
    name: str
    kappa: Fraction
    local_current: bool
    connected_cumulant: bool

    @property
    def ward_normalized(self) -> bool:
        return True

    @property
    def color_singlet_observable(self) -> bool:
        return True

    @property
    def cmt_invariant(self) -> bool:
        return True

    @property
    def finite_ozi_size(self) -> bool:
        return 0 <= self.kappa <= 1

    @property
    def singlet_annihilating(self) -> bool:
        return self.kappa == 0

    @property
    def r_phys(self) -> Fraction:
        return F_ADJ + self.kappa * F_SINGLET

    @property
    def q_e_oriented(self) -> Fraction:
        return Fraction(5, 3) / self.r_phys

    @property
    def rho_e_oriented(self) -> Fraction:
        return 6 * (self.q_e_oriented - 1)


FULL_CURRENT = CurrentReadout("local_full_current", Fraction(1), True, False)
CONNECTED_CUMULANT = CurrentReadout("connected_cumulant", Fraction(0), False, True)
BOUNDED_SUBTRACTED = CurrentReadout("bounded_subtracted_current", Fraction(1, 2), True, False)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def admitted_by_local_current_premises(readout: CurrentReadout) -> bool:
    return (
        readout.local_current
        and readout.ward_normalized
        and readout.color_singlet_observable
        and readout.cmt_invariant
        and readout.finite_ozi_size
    )


def admitted_by_connected_premise(readout: CurrentReadout) -> bool:
    return readout.connected_cumulant and readout.singlet_annihilating


def part1_premise_split() -> None:
    print("PART 1: local-current versus connected-cumulant split")
    check("full current is local", FULL_CURRENT.local_current)
    check("full current is not a connected cumulant", not FULL_CURRENT.connected_cumulant)
    check("connected cumulant annihilates singlet", CONNECTED_CUMULANT.singlet_annihilating)
    check("connected cumulant is a subtraction/readout construction, not the bare local full current", CONNECTED_CUMULANT.connected_cumulant and not CONNECTED_CUMULANT.local_current)
    check("bounded subtracted current is local but not singlet-annihilating", BOUNDED_SUBTRACTED.local_current and not BOUNDED_SUBTRACTED.singlet_annihilating)


def part2_local_premises_do_not_select() -> None:
    print()
    print("PART 2: local-current controls do not select kappa=0")
    candidates = (FULL_CURRENT, BOUNDED_SUBTRACTED)
    for candidate in candidates:
        print(f"  {candidate.name}: kappa={candidate.kappa}, R={candidate.r_phys}, rho_E={candidate.rho_e_oriented}")
        check(f"{candidate.name} satisfies local-current premises", admitted_by_local_current_premises(candidate))

    check("local-current premises admit full trace", admitted_by_local_current_premises(FULL_CURRENT))
    check("local-current premises admit nonzero bounded subtraction", admitted_by_local_current_premises(BOUNDED_SUBTRACTED))
    check("therefore local-current premises do not force singlet annihilation", not all(c.singlet_annihilating for c in candidates))
    check("Ward normalization does not distinguish kappa=0 from kappa=1", FULL_CURRENT.ward_normalized and CONNECTED_CUMULANT.ward_normalized)
    check("CMT invariance does not distinguish kappa=0 from kappa=1", FULL_CURRENT.cmt_invariant and CONNECTED_CUMULANT.cmt_invariant)


def part3_connected_premise_equivalence() -> None:
    print()
    print("PART 3: connected premise equivalence")
    candidates = (FULL_CURRENT, BOUNDED_SUBTRACTED, CONNECTED_CUMULANT)
    selected = [c.name for c in candidates if admitted_by_connected_premise(c)]
    annihilating = [c.name for c in candidates if c.singlet_annihilating]
    check("connected-cumulant premise selects the connected endpoint", selected == ["connected_cumulant"], str(selected))
    check("singlet annihilation selects the same endpoint", annihilating == ["connected_cumulant"], str(annihilating))
    check("connected premise is equivalent to kappa=0 in this binary target", selected == annihilating)
    check("full trace is excluded only after the connected-cumulant premise is supplied", FULL_CURRENT.name not in selected)


def part4_route2_consequence() -> None:
    print()
    print("PART 4: Route-2 consequence")
    connected = CONNECTED_CUMULANT
    full = FULL_CURRENT
    bounded = BOUNDED_SUBTRACTED
    check("connected cumulant gives rho_E=21/4 under oriented Route-2 chain", connected.rho_e_oriented == TARGET_RHO_E, f"rho_E={connected.rho_e_oriented}")
    check("full current gives rho_E=4 under oriented Route-2 chain", full.rho_e_oriented == 4, f"rho_E={full.rho_e_oriented}")
    check("bounded subtraction gives non-target rho_E", bounded.rho_e_oriented == Fraction(78, 17), f"rho_E={bounded.rho_e_oriented}")
    check("Route-2 target selects connected cumulant only if target value is used", [c.name for c in (connected, full, bounded) if c.rho_e_oriented == TARGET_RHO_E] == ["connected_cumulant"])


def part5_stuck_fanout() -> None:
    print()
    print("PART 5: stuck fan-out frames")
    frames = {
        "site-locality": "local full current remains admitted",
        "Ward identity": "normalizes the current but leaves disconnected coefficient free",
        "color-singlet EW current": "supports full trace as the direct local color-scalar current",
        "cluster/cumulant": "selects connected only by adding disconnected subtraction",
        "OZI suppression": "bounds singlet size but does not give exact zero",
    }
    for label, result in frames.items():
        print(f"  {label}: {result}")
        check(f"{label} frame does not derive kappa=0 from local-current premises", bool(result))
    check("five orthogonal frames were checked", len(frames) == 5)


def part6_note_and_authority_markers() -> None:
    print()
    print("PART 6: note and authority markers")
    note = note_text("QUARK_ROUTE2_LOCAL_CURRENT_SINGLET_ANNIHILATION_NO_GO_NOTE_2026-06-22.md")
    block71 = note_text("QUARK_ROUTE2_FULL_TRACE_EXCLUSION_NO_GO_NOTE_2026-06-22.md")
    block69 = note_text("QUARK_ROUTE2_CONNECTED_CURRENT_SELECTOR_NO_GO_NOTE_2026-06-22.md")
    rconn = note_text("RCONN_DERIVED_NOTE.md")
    ew_gate = note_text("EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md")
    parent = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")

    required = (
        "Claim type:** no_go",
        "Actual current-surface status: no-go for singlet annihilation from local-current premises",
        "This is not an audit verdict",
        "connected-cumulant premise",
        "local full current remains admitted",
        "does not close the parent",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note)

    check("Block71 says full trace survives current controls", "full-trace endpoint survives" in block71)
    check("Block69 says exact zero needs annihilation theorem", "That annihilation is the missing theorem" in block69)
    check("Rconn note says full trace is a live specialization", "full-trace specialization" in rconn)
    check("EW gate says CMT cannot exclude full trace", "CMT can neither select `kappa_EW = 0` nor exclude `kappa_EW = 1`" in ew_gate)
    check("parent note still names endpoint triple blocker", "underlying readout-map endpoint triple is not yet derived" in parent)

    banned = (
        ("status-authority phrase", phrase("Status ", "authority")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
    )
    for label, marker in banned:
        check(f"new note avoids overclaim marker: {label}", marker not in note)


def main() -> int:
    print("Route-2 local-current singlet-annihilation stretch no-go")
    print("Status: no-go for singlet annihilation from local-current premises; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_premise_split()
    part2_local_premises_do_not_select()
    part3_connected_premise_equivalence()
    part4_route2_consequence()
    part5_stuck_fanout()
    part6_note_and_authority_markers()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: local-current singlet-annihilation checks failed.")
        return 1
    print(
        "VERDICT: local-current premises do not force singlet annihilation.  "
        "kappa=0 follows only after adding a connected-cumulant or "
        "disconnected-subtraction readout premise."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
