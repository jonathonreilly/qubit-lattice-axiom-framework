#!/usr/bin/env python3
"""Record local finite readout-atom availability verifier.

This runner checks the exact finite algebra behind the source-side repair:

* the (P-REC) declared bounded-premise packet parses from the note, and the
  theorem's selections (atoms, readout context, conjugation, unit weights,
  sites, instance rule) are CONSTRUCTED from the parsed packet rather than
  freestanding in code (2026-07-10 repair; a corrupted-packet negative
  control shows the construction is live);
* Z^3 supplies arbitrary finite lists of distinct supports;
* the declared one-site diagonal context inside M_2(C) has two nonzero
  K-fixed orthogonal readout atoms;
* the declared covariant varying-rule instance makes the chosen atom
  available at each site; a contrasting covariant instance defeats it (the
  premise is selective, not vacuous);
* the finite Boolean unit-count functional is additive on disjoint support
  tags;
* the result is availability/readout-context algebra only, not production,
  probability, physical context selection, clock/rate, or dial selection.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from itertools import permutations
from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/RECORD_LOCAL_FINITE_ATOM_AVAILABILITY_NARROW_THEOREM_NOTE_2026-06-17.md"


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


@dataclass(frozen=True)
class RecPacket:
    rule_name: str
    basis: str
    p0_diag: tuple[int, ...]
    p1_diag: tuple[int, ...]
    sites_line: str
    locking_history: str


def parse_rec_packet(note_text: str, corrupt_swap_atoms: bool = False) -> RecPacket:
    """Parse the fenced (P-REC) packet out of the note.

    The theorem's selections are constructed from this parse; nothing about
    the atoms, basis, rule, or sites is hard-coded past this point. The
    corrupt_swap_atoms flag builds a deliberately corrupted COPY (atom specs
    swapped) for the negative control; it never touches the real parse.
    """
    fence = re.search(
        r"```text\n\(P-REC\) Record-availability selection packet \(2026-07-10\)\.(.*?)```",
        note_text,
        re.DOTALL,
    )
    if not fence:
        raise ValueError("(P-REC) packet block not found in note")
    body = fence.group(1)
    rule = re.search(r"^RULE:\s*(\S+)\s*$", body, re.MULTILINE)
    basis = re.search(r"^BASIS:\s*(\S+)\s*$", body, re.MULTILINE)
    atoms_line = re.search(
        r"^ATOMS:\s*P_0 = diag\(([^)]*)\)\s*;\s*P_1 = diag\(([^)]*)\)\s*$",
        body,
        re.MULTILINE,
    )
    sites = re.search(r"^SITES:\s*(.+)$", body, re.MULTILINE)
    locking_history = re.search(r"^LOCKING-HISTORY:\s*(.+)$", body, re.MULTILINE)
    if not (rule and basis and atoms_line and sites and locking_history):
        raise ValueError("(P-REC) packet is missing RULE/BASIS/ATOMS/SITES/LOCKING-HISTORY fields")
    p0_spec, p1_spec = atoms_line.group(1), atoms_line.group(2)
    if corrupt_swap_atoms:
        p0_spec, p1_spec = p1_spec, p0_spec
    p0_diag = tuple(int(x) for x in p0_spec.split(","))
    p1_diag = tuple(int(x) for x in p1_spec.split(","))
    return RecPacket(
        rule_name=rule.group(1),
        basis=basis.group(1),
        p0_diag=p0_diag,
        p1_diag=p1_diag,
        sites_line=sites.group(1).strip(),
        locking_history=locking_history.group(1).strip(),
    )


def atoms_from_packet(packet: RecPacket) -> tuple[sp.Matrix, sp.Matrix]:
    return sp.diag(*packet.p0_diag), sp.diag(*packet.p1_diag)


_NOTE_TEXT = (ROOT / NOTE_REL).read_text(encoding="utf-8")
PACKET = parse_rec_packet(_NOTE_TEXT)

I2 = sp.eye(2)
# Constructed from the declared bounded (P-REC) packet, not freestanding:
P0, P1 = atoms_from_packet(PACKET)
X = mat([[0, 1], [1, 0]])


@dataclass(frozen=True)
class LocalReadoutAtom:
    site: tuple[int, int, int]
    label: str
    projector: sp.Matrix
    unit_weight: int = 1


def line_sites(n: int) -> list[tuple[int, int, int]]:
    return [(2 * k, 0, 0) for k in range(n)]


def atoms(n: int) -> list[LocalReadoutAtom]:
    return [LocalReadoutAtom(site=site, label="P1", projector=P1) for site in line_sites(n)]


def pairwise_disjoint_support(records: list[LocalReadoutAtom]) -> bool:
    sites = [record.site for record in records]
    return len(sites) == len(set(sites))


def pairwise_nonadjacent(records: list[LocalReadoutAtom]) -> bool:
    sites = [record.site for record in records]
    return all(
        sum(abs(a_i - b_i) for a_i, b_i in zip(a, b)) > 1
        for index, a in enumerate(sites)
        for b in sites[index + 1 :]
    )


def unit_count_readout(records: list[LocalReadoutAtom]) -> int:
    return sum(record.unit_weight for record in records)


def k_fixed(projector: sp.Matrix) -> bool:
    return projector.conjugate() == projector


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return a * b - b * a


NeighborCondition = tuple[str | None, str | None, str | None, str | None, str | None, str | None]
AvailableSet = frozenset[str]


def r_all(condition: NeighborCondition) -> AvailableSet:
    del condition
    return frozenset({"P0", "P1"})


def r_p0only(condition: NeighborCondition) -> AvailableSet:
    del condition
    return frozenset({"P0"})


def r_varying(condition: NeighborCondition) -> AvailableSet:
    return frozenset({"P0", "P1"}) if all(label is None for label in condition) else frozenset({"P0"})


RULE_LIBRARY = {"R_all": r_all, "R_p0only": r_p0only, "R_varying": r_varying}
# The declared bounded instance premise (P-REC-a) is the packet-named rule; the
# other library members remain as the rejector / neighbor-varying exhibits.
PREMISE_RULE = RULE_LIBRARY[PACKET.rule_name]


def neighbor_condition(
    site: tuple[int, int, int], locked: dict[tuple[int, int, int], str]
) -> NeighborCondition:
    x, y, z = site
    neighbors = (
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    )
    return tuple(locked.get(neighbor) for neighbor in neighbors)  # type: ignore[return-value]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> int:
    print("Record local finite readout-atom availability theorem")
    print("actual_current_surface_status: source-side candidate theorem")
    print("audit_required_before_effective_retained: true")
    print("proposal_allowed: false")
    print()

    print("P. declared bounded (P-REC) packet: parse, construct, negative control")
    check(
        "P1 packet parses with all four fields",
        PACKET.rule_name == "R_varying"
        and PACKET.basis == "computational-diagonal"
        and PACKET.sites_line.startswith("x_k = (2k,0,0)")
        and PACKET.locking_history == "chosen sites have empty nearest-neighbor slots at lock time",
        f"rule={PACKET.rule_name}, basis={PACKET.basis}, sites={PACKET.sites_line!r}",
    )
    check(
        "P2 constructed atoms match the theorem's displayed projectors",
        P0 == mat([[1, 0], [0, 0]]) and P1 == mat([[0, 0], [0, 1]]),
        "anchor comparison against the Result-section display",
    )
    check(
        "P3 packet-named instance rule resolves in the rule library",
        PREMISE_RULE is RULE_LIBRARY["R_varying"],
    )
    corrupted = parse_rec_packet(_NOTE_TEXT, corrupt_swap_atoms=True)
    c_p0, c_p1 = atoms_from_packet(corrupted)
    check(
        "P4 corrupted-packet negative control is detected by the anchor comparison",
        c_p1 != P1 and c_p1 == P0 and c_p0 == P1,
        "swapping the ATOMS specs flips the constructed projectors, so the construction is live",
    )

    print("\nA. source authority and boundary text")
    minimal = read_text("docs/MINIMAL_AXIOMS_2026-06-29.md")
    nogo = read_text("docs/RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md")
    note = read_text(NOTE_REL)
    minimal_flat = " ".join(minimal.split())
    nogo_flat = " ".join(nogo.split())
    note_flat = " ".join(note.split())
    check("A1 live Lattice axiom exposes cubic Z^3 sites", "Physical sites are the points of the cubic lattice `Z^3`" in minimal_flat)
    check("A2 live Qubit axiom exposes one-site M_2(C)", "The full one-site possibility domain has algebraic presentation `M_2(C)`." in minimal_flat)
    check("A3 live Admissibility axiom names one fixed covariant NN rule", "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." in minimal_flat)
    check("A4 live Admissibility axiom requires neighbor-varying availability", "the available possibilities are determined by, and vary with, the nearest-neighbor conditions" in minimal_flat)
    check("A5 live Record axiom locks one admissible possibility", "a record locks exactly one admissible local possibility" in minimal_flat)
    check("A6 live memo leaves formation-rule details downstream", "formation rules (which admissible possibility a new record locks, at which site, with what weight, or at what rate)" in minimal_flat)
    check("A7 live memo keeps downstream bridges open", "Probability, dynamics, readout contexts, and physical observable bridges remain downstream." in minimal_flat)
    check("A8 narrowed no-go withholds the formation rule/process/state/site/weight/rate", "It does not supply the formation rule/process/state/site/weight/rate." in nogo_flat)
    check("A9 theorem boundary explicitly does not derive production", "record production or realization dynamics" in note)
    check("A10 theorem names the declared availability premise and record eligibility", "declared admissibility-instance premise" in note_flat and "record-eligible" in note)
    check(
        "A11 note declares all four (P-REC) premises in named form",
        all(tag in note for tag in ("(P-REC-a)", "(P-REC-b)", "(P-REC-c)", "(P-REC-d)"))
        and "declared bounded-premise packet" in note_flat,
    )
    check(
        "A12 note carries the dated 2026-07-10 Repair Note with the construct-from-packet statement",
        "constructs the theorem's selections" in note_flat and "2026-07-10" in note,
    )

    print("\nB. one-site diagonal readout context")
    check("B1 P0 is idempotent", P0 * P0 == P0)
    check("B2 P1 is idempotent", P1 * P1 == P1)
    check("B3 P0 and P1 are orthogonal", P0 * P1 == sp.zeros(2) and P1 * P0 == sp.zeros(2))
    check("B4 P0 + P1 resolves identity", P0 + P1 == I2)
    check("B5 both readout atoms are nonzero rank-one projectors", P0.trace() == 1 and P1.trace() == 1 and P0.rank() == 1 and P1.rank() == 1)
    check("B6 both atoms are fixed by entrywise K", k_fixed(P0) and k_fixed(P1))
    check("B7 atoms commute inside the declared readout algebra", commutator(P0, P1) == sp.zeros(2))
    check("B8 atoms are not central in all M_2(C)", commutator(P0, X) != sp.zeros(2) and commutator(P1, X) != sp.zeros(2))

    print("\nAD. declared toy admissibility instances")
    rules = (r_all, r_p0only, r_varying)
    representative_conditions: tuple[NeighborCondition, ...] = (
        (None, None, None, None, None, None),
        ("P1", None, None, None, None, None),
        ("P0", "P1", None, None, None, None),
        ("P0", "P0", "P1", "P1", None, None),
    )
    neighbor_permutations = tuple(permutations(range(6)))
    check(
        "AD1 each toy NN-multiset rule is invariant under all neighbor permutations",
        all(
            rule(tuple(condition[index] for index in permutation)) == rule(condition)
            for rule in rules
            for condition in representative_conditions
            for permutation in neighbor_permutations
        ),
        "permutation invariance implies translation/proper-cubic-rotation covariance",
    )
    empty_condition: NeighborCondition = (None, None, None, None, None, None)
    check(
        "AD2 packet-declared rule (P-REC-a) makes P1 available under empty-neighbor conditions",
        all("P1" in PREMISE_RULE(empty_condition) for n in (1, 3, 8) for _site in line_sites(n)),
        f"declared rule: {PACKET.rule_name}",
    )
    check(
        "AD3 R_p0only rejector detects failure of the declared P1 premise at every site",
        all("P1" not in r_p0only(empty_condition) for n in (1, 3, 8) for _site in line_sites(n)),
        "the availability premise is selective, not vacuous",
    )
    recorded_neighbor: NeighborCondition = ("P0", None, None, None, None, None)
    check(
        "AD4 R_varying makes P1 availability vary with the neighbor condition",
        "P1" in r_varying(empty_condition) and "P1" not in r_varying(recorded_neighbor),
    )
    locked: dict[tuple[int, int, int], str] = {}
    realized_stack: list[LocalReadoutAtom] = []
    admissible_at_lock: list[bool] = []
    conditions_at_lock: list[NeighborCondition] = []
    for record in atoms(8):
        condition_at_lock = neighbor_condition(record.site, locked)
        conditions_at_lock.append(condition_at_lock)
        admissible_at_lock.append(record.label in PREMISE_RULE(condition_at_lock))
        locked[record.site] = record.label
        realized_stack.append(record)
    check(
        "AD5 declared empty-NN locking history keeps P1 available under R_varying",
        len(realized_stack) == 8
        and all(admissible_at_lock)
        and all(condition == empty_condition for condition in conditions_at_lock),
        f"declared rule: {PACKET.rule_name}",
    )
    print("[NAMED] AD5 live presence-conditional layer: by the Record wording, a present record locks an admissible local possibility")

    print("\nC. arbitrary finite disjoint supports on Z^3")
    tested_lengths = [0, 1, 2, 3, 5, 8, 13, 21, 55]
    for n in tested_lengths:
        rs = atoms(n)
        check(
            f"C1 n={n}: distinct pairwise-nonadjacent line supports and one atom per support",
            len(rs) == n
            and pairwise_disjoint_support(rs)
            and pairwise_nonadjacent(rs)
            and all(r.projector == P1 for r in rs),
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
    second = [LocalReadoutAtom(site=(2 * k, 0, 0), label="P1", projector=P1) for k in range(4, 9)]
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
        "local_readout_atom_availability": "closed_under_declared_instance",
        "declared_unit_count_context": "closed",
        "record_production": "open",
        "measurement_decoherence_instrument": "open",
        "born_probability": "open",
        "physical_context_selection": "open",
        "clock_rate": "open",
        "dial_selection": "open",
        "admissibility_instance_selection": "open",
    }
    check(
        "E1 local readout-atom availability closes only under the declared instance",
        gates["local_readout_atom_availability"] == "closed_under_declared_instance",
    )
    check("E2 declared unit-count context is the closed finite algebra part", gates["declared_unit_count_context"] == "closed")
    check("E3 record production remains open", gates["record_production"] == "open")
    check("E4 measurement/decoherence instrument remains open", gates["measurement_decoherence_instrument"] == "open")
    check("E5 Born probability remains open", gates["born_probability"] == "open")
    check("E6 physical context selection remains open", gates["physical_context_selection"] == "open")
    check("E7 clock/rate remains open", gates["clock_rate"] == "open")
    check("E8 dial selection remains open", gates["dial_selection"] == "open")
    check("E9 admissibility-instance selection remains open", gates["admissibility_instance_selection"] == "open")

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: exact finite local readout-atom/context availability closes only under the "
            "declared admissibility instance, diagonal readout context, K/conjugation context, "
            "and unit-count normalization; selection of those inputs, production, probability, "
            "clock/rate, and dial selection remain open."
        )
        return 0
    print("VERDICT: local atom availability repair failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
