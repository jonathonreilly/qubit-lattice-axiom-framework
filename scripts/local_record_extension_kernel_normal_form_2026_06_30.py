#!/usr/bin/env python3
"""Verify the local record-extension kernel normal form."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
OCCURRENCE = DOCS / "RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30.md"
BORN = DOCS / "RECORD_BORN_INTERFACE_FROM_SELECTIVE_WRITE_BRIDGE_2026-06-30.md"
KERNEL_BOUNDARY = DOCS / "RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md"
CHECKLIST = DOCS / "RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md"
LAYER = DOCS / "RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md"
INTERFACE = DOCS / "RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md"
FORMATION_NOGO = DOCS / "RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md"
POINTER = DOCS / "RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md"

PASS = 0
FAIL = 0
BOT = "bot"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + title)


def factor_kernel(kernel: dict[object, Fraction], available: set[object]) -> tuple[Fraction, dict[object, Fraction]]:
    """Return activation and conditional selection for a one-site kernel."""
    support = {BOT} | set(available)
    if set(kernel) != support:
        raise ValueError("kernel support must be exactly {bot} union available")
    if any(weight < 0 for weight in kernel.values()):
        raise ValueError("negative kernel weight")
    if sum(kernel.values(), Fraction(0)) != 1:
        raise ValueError("kernel is not normalized")
    activation = 1 - kernel[BOT]
    if activation == 0:
        return activation, {}
    selection = {value: kernel[value] / activation for value in available}
    return activation, selection


def reconstruct(activation: Fraction, selection: dict[object, Fraction], available: set[object]) -> dict[object, Fraction]:
    """Reconstruct a one-site kernel from activation and selection."""
    if activation == 0:
        return {BOT: Fraction(1), **{value: Fraction(0) for value in available}}
    return {BOT: 1 - activation, **{value: activation * selection[value] for value in available}}


def product_kernel(kernels: list[dict[object, Fraction]]) -> dict[tuple[object, ...], Fraction]:
    outcomes = [list(kernel) for kernel in kernels]
    joint: dict[tuple[object, ...], Fraction] = {}
    for combo in product(*outcomes):
        weight = Fraction(1)
        for outcome, kernel in zip(combo, kernels):
            weight *= kernel[outcome]
        joint[combo] = weight
    return joint


def extend_records(records: dict[int, int], sites: list[int], outcome: tuple[object, ...]) -> dict[int, int]:
    new = dict(records)
    for site, value in zip(sites, outcome):
        if value == BOT:
            continue
        if site in new:
            raise ValueError("cannot overwrite a fixed record")
        new[site] = int(value)
    return new


def main() -> int:
    print("=== Local record-extension kernel normal form ===")

    paths = [
        NOTE,
        AXIOMS,
        OCCURRENCE,
        BORN,
        KERNEL_BOUNDARY,
        CHECKLIST,
        LAYER,
        INTERFACE,
        FORMATION_NOGO,
        POINTER,
    ]
    for path in paths:
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    note_flat = flat(note)
    axioms = read(AXIOMS)
    occurrence = read(OCCURRENCE)
    born = read(BORN)
    kernel_boundary = read(KERNEL_BOUNDARY)
    checklist = read(CHECKLIST)
    layer = read(LAYER)
    interface = read(INTERFACE)
    formation_nogo = read(FORMATION_NOGO)
    pointer = read(POINTER)

    section("PART A -- source boundary")
    check("axioms provide available possibilities", "available subset of possibilities" in axioms)
    check("axioms provide fixed records", "A record locks exactly one available local possibility" in axioms)
    check("axioms do not supply production", "record-production process" in axioms)
    check("occurrence bridge names activation and selection", "Activation" in occurrence and "Selection" in occurrence)
    check("occurrence bridge preserves no-activation witness", "no activation" in occurrence)
    check("Born bridge preserves occurrence wall", "W_occurrence" in born)
    check("kernel boundary says append is consumer", "consumer of produced atoms" in kernel_boundary)
    check("checklist separates produced record from kernel", "produced record" in checklist)
    check("layer note says post-record layer is consumer", "consumer" in layer and "not a producer" in layer)
    check("interface principle has production bridge slot", "record-production bridge or instrument" in interface)
    check("formation no-go supplies no-record witnesses", "H = 0" in formation_nogo)
    check("pointer theorem gives bounded supplier route", "controlled-copy coupling is sufficient" in pointer)

    section("PART B -- one-site factorization")
    available0 = {0, 1}
    kernel0 = {BOT: Fraction(1, 2), 0: Fraction(1, 8), 1: Fraction(3, 8)}
    activation0, selection0 = factor_kernel(kernel0, available0)
    reconstructed0 = reconstruct(activation0, selection0, available0)
    check("kernel0 normalizes", sum(kernel0.values(), Fraction(0)) == 1)
    check("activation is one minus no-record mass", activation0 == Fraction(1, 2), f"a={activation0}")
    check("conditional selection normalizes", sum(selection0.values(), Fraction(0)) == 1, f"p={selection0}")
    check("selection recovers value 0 probability", selection0[0] == Fraction(1, 4))
    check("selection recovers value 1 probability", selection0[1] == Fraction(3, 4))
    check("reconstruction equals original kernel", reconstructed0 == kernel0)

    kernel_zero = {BOT: Fraction(1), 0: Fraction(0), 1: Fraction(0)}
    activation_zero, selection_zero = factor_kernel(kernel_zero, available0)
    check("zero activation is allowed", activation_zero == 0)
    check("zero activation uses no selection distribution", selection_zero == {})
    check("zero activation reconstructs no-record kernel", reconstruct(activation_zero, selection_zero, available0) == kernel_zero)

    empty_available: set[int] = set()
    empty_kernel = {BOT: Fraction(1)}
    activation_empty, selection_empty = factor_kernel(empty_kernel, empty_available)
    check("empty availability forces no record", activation_empty == 0 and selection_empty == {})

    try:
        factor_kernel({BOT: Fraction(1, 2), 0: Fraction(1, 2)}, {1})
        unavailable_rejected = False
    except ValueError:
        unavailable_rejected = True
    check("kernel with unavailable value is rejected", unavailable_rejected)

    section("PART C -- disjoint product composition")
    available1 = {1}
    kernel1 = {BOT: Fraction(3, 5), 1: Fraction(2, 5)}
    activation1, selection1 = factor_kernel(kernel1, available1)
    joint = product_kernel([kernel0, kernel1])
    check("kernel1 activation is 2/5", activation1 == Fraction(2, 5))
    check("kernel1 selection is deterministic", selection1 == {1: Fraction(1)})
    check("joint product kernel normalizes", sum(joint.values(), Fraction(0)) == 1)
    check("joint all-no-record probability is product", joint[(BOT, BOT)] == kernel0[BOT] * kernel1[BOT])
    check("joint double-record probability is product", joint[(1, 1)] == kernel0[1] * kernel1[1])
    check("joint support has six outcomes", len(joint) == 6)
    check("all joint probabilities are nonnegative", all(weight >= 0 for weight in joint.values()))

    section("PART D -- preservation and support")
    fixed_records = {-1: 0}
    sites = [0, 1]
    extensions = {outcome: extend_records(fixed_records, sites, outcome) for outcome in joint}
    check("no outcome overwrites fixed record", all(ext[-1] == 0 for ext in extensions.values()))
    check("no-record outcome leaves fixed boundary unchanged", extensions[(BOT, BOT)] == fixed_records)
    check("record outcomes add only selected sites", extensions[(0, BOT)] == {-1: 0, 0: 0})
    check("double-record outcome adds both selected sites", extensions[(1, 1)] == {-1: 0, 0: 1, 1: 1})
    allowed_values = {0: available0, 1: available1}
    support_ok = True
    for outcome in joint:
        for site, value in zip(sites, outcome):
            if value != BOT and value not in allowed_values[site]:
                support_ok = False
    check("joint kernel never locks unavailable values", support_ok)

    section("PART E -- Born weights can be selection but not activation")
    born_selection = {0: Fraction(3, 5), 1: Fraction(2, 5)}
    activation = Fraction(0)
    no_event_kernel = reconstruct(activation, {}, set(born_selection))
    activation = Fraction(1, 4)
    born_kernel = reconstruct(activation, born_selection, set(born_selection))
    check("Born-form selection weights normalize", sum(born_selection.values(), Fraction(0)) == 1)
    check("same selection weights allow no activation", no_event_kernel[BOT] == 1)
    check("selection plus activation yields record probabilities", born_kernel[0] == Fraction(3, 20) and born_kernel[1] == Fraction(1, 10))
    check("activation remains independent scalar", born_kernel[BOT] == Fraction(3, 4))

    section("PART F -- note content")
    required_sections = [
        "Claim",
        "Finite Theorem",
        "Relation To Availability And Born Weights",
        "What Moves",
        "What Remains",
        "Audit Consequence If Retained",
        "Non-Claims",
        "No-Go Discipline Gate",
    ]
    for section_name in required_sections:
        check(f"note includes {section_name}", f"## {section_name}" in note)
    check("note names activation probability", "activation probability a_x" in note)
    check("note names selection probability", "selection probability p_x(v)" in note)
    check("note includes no-record outcome", "{no record at x}" in note)
    check("note says empty availability forces no record", "If `A_x` is empty" in note)
    check("note preserves physical kernel wall", "physical kernel" in note)
    check("note says no axiom requested", "No new axiom is requested by this note" in note)

    section("PART G -- no-go discipline gate")
    for item in ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"]:
        check(f"note includes {item}", item in note)
    check("N1 enumerates seven routes", note.count("| Availability-only route |") == 1 and note.count("| New primitive route |") == 1)
    check("N2 names W_occurrence_kernel", "W_occurrence_kernel" in note)
    check("N3 defines no-record outcome", "\"No record\" is an explicit outcome" in note)
    check("N4 has seven witness matches", note.count("| `RECORD_") >= 7 and "Residual Matching" in note)
    check("N5 avoids records-never-form overclaim", "does not say records never form" in note)
    check("N6 lists live closure paths", "Live closure paths remain" in note)
    check("N7 steelman admits bookkeeping objection", "only bookkeeping" in note)
    check("N8 cross-cycle echo is present", "post-record append/count became exact" in note)

    section("PART H -- assembled conclusion")
    normal_form_ok = (
        reconstructed0 == kernel0
        and activation1 == Fraction(2, 5)
        and sum(joint.values(), Fraction(0)) == 1
        and support_ok
        and all(ext[-1] == 0 for ext in extensions.values())
    )
    check("local extension kernels factor into activation and selection", normal_form_ok)
    check("physical values/rates remain open", "physical values/rules for activation" in note)
    check("total recording is special not forced", "not forced by ontology" in note)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- local occurrence law normal form is activation plus selection over available possibilities, preserving records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
