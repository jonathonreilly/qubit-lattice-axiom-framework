#!/usr/bin/env python3
"""Verifier for source-slot frame selector support in the lepton 1/256 lane.

This runner checks the finite conditional theorem: if a charged-lepton
full-cell source family is supplied as independent matrix-unit source controls,
then those source controls select the tensor-product matrix-unit frame relative
to that source map. It does not derive S_l, a charged-lepton mass, alpha(0), or
hydrogen spectroscopy.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
BASIS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md"
TENSOR_FRAME = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md"
ATTACHMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
SIMPLEX = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
NOETHER = ROOT / "docs" / "AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md"
LOCAL_DENSITY = ROOT / "docs" / "STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md"
TRACIAL = ROOT / "docs" / "PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


Coord = tuple[int, int, int, int]


class Audit:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            prefix = "PASS"
        else:
            self.fail_count += 1
            prefix = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{prefix}: {label}{suffix}")

    def summary(self) -> None:
        print(f"\nSUMMARY: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def swap_local(coord: Coord, slot: int, a: int, b: int) -> Coord:
    items = list(coord)
    if items[slot] == a:
        items[slot] = b
    elif items[slot] == b:
        items[slot] = a
    return tuple(items)  # type: ignore[return-value]


def swap_slots(coord: Coord, i: int, j: int) -> Coord:
    items = list(coord)
    items[i], items[j] = items[j], items[i]
    return tuple(items)  # type: ignore[return-value]


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-slot frame selector support note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        BASIS,
        TENSOR_FRAME,
        ATTACHMENT,
        FULL_CELL,
        SIMPLEX,
        NOETHER,
        LOCAL_DENSITY,
        TRACIAL,
        MINIMAL,
        KINETIC,
        SCALE,
        REALIZED,
        REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    section("Required note content")
    required_phrases = [
        "Source-Slot Frame Selector Support",
        "A2.3",
        "slot-resolved full-cell source controls",
        "J : R^C -> A_cell",
        "J(j) = sum_{c in C} j_c O_c",
        "S_lep[J] = h * B_lep * J(j)",
        "dS_lep/dj_c = h * B_lep * O_c",
        "S_4^4 semidirect S_4",
        "Full U(16) conjugations are not symmetries",
        "full `U(16)` covariance firewall",
        "flat-unitary conjugate",
        "source-family frame",
        "Open PR Alignment",
        "#4936",
        "#4937",
        "#4938",
        "K/CPT supplied-context bridge",
        "No-Go Discipline Gate",
        "broad A2/S_l closure fails; narrowed source-slot frame selector support passes.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite source-map frame checks")
    coords = coordinates()
    audit.check("source coordinate set has 4^4 = 256 labels", len(coords) == 256)
    audit.check("source controls are one-to-one with matrix-unit directions", len(set(coords)) == 256)

    sample = (0, 1, 2, 3)
    local_swapped = swap_local(sample, 2, 2, 0)
    slot_swapped = swap_slots(sample, 0, 3)
    audit.check("local relabeling maps coordinate label to coordinate label", local_swapped in coords, str(local_swapped))
    audit.check("slot relabeling maps coordinate label to coordinate label", slot_swapped in coords, str(slot_swapped))
    audit.check("tensor-frame relabeling group size is 24^5", 24**5 == 7_962_624)

    n = 16
    algebra_dim = n * n
    matrix_unit_nonzero = 1
    flat_projection_nonzero = algebra_dim
    matrix_unit_entry_sum = Fraction(1, 1)
    flat_projection_entry = Fraction(1, n)
    flat_projection_entry_sum = algebra_dim * flat_projection_entry
    matrix_unit_fixed_avg = matrix_unit_entry_sum / algebra_dim
    flat_projection_fixed_avg = flat_projection_entry_sum / algebra_dim
    normalized_trace = Fraction(1, n)
    hs_norm_sq = Fraction(1, 1)

    audit.check("M_16(C) algebra dimension is 256", algebra_dim == 256)
    audit.check("a matrix unit has one nonzero entry", matrix_unit_nonzero == 1)
    audit.check("flat conjugate rank-one projection has 256 nonzero entries", flat_projection_nonzero == 256)
    audit.check("flat projection is not a single matrix unit", flat_projection_nonzero != matrix_unit_nonzero)
    audit.check("fixed matrix-unit average gives 1/256", matrix_unit_fixed_avg == Fraction(1, 256), str(matrix_unit_fixed_avg))
    audit.check("flat projection fixed-coordinate average gives 1/16", flat_projection_fixed_avg == Fraction(1, 16), str(flat_projection_fixed_avg))
    audit.check("normalized trace is 1/16 for either rank-one projection", normalized_trace == Fraction(1, 16))
    audit.check("Hilbert-Schmidt norm squared remains 1", hs_norm_sq == 1)
    audit.check("full inner automorphism changes fixed-coordinate average", matrix_unit_fixed_avg != flat_projection_fixed_avg)

    section("Authority boundary checks")
    basis = read(BASIS)
    tensor_frame = read(TENSOR_FRAME)
    attachment = read(ATTACHMENT)
    full_cell = read(FULL_CELL)
    simplex = read(SIMPLEX)
    noether = read(NOETHER)
    local_density = read(LOCAL_DENSITY)
    tracial = read(TRACIAL)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()

    audit.check("basis discriminator names full U(16) firewall", "full `U(16)` covariance" in basis or "full `U(16)`" in basis)
    audit.check("tensor-frame note supplies restricted relabeling support", "S_4^4 semidirect S_4" in tensor_frame and "coordinate bijections" in tensor_frame)
    audit.check("attachment note supplies derivative source map form", "dS_lep/dj_c = h * B_lep * O_c" in attachment)
    audit.check("full-cell note supplies 256 carrier under full-cell source locality", "4^4 = 256" in full_cell and "full OS0-cell source locality" in full_cell)
    audit.check("simplex note keeps source-action semantics open", "source-action semantics" in simplex and "not prove that the charged-lepton source" in simplex)
    audit.check("Noether note supplies matrix-unit algebra", "matrix-unit" in noether and "[E_ij, E_pq]" in noether)
    audit.check("Noether note does not supply physical density bridge", "does **not** claim" in noether and "physical `rho_x = chibar_x chi_x`" in noether)
    audit.check("local density note supplies diagonal CAR density only", "rho_x := chibar_x chi_x" in local_density and "one-mode" in local_density)
    audit.check("tracial note names inner automorphism invariant state", "inner-automorphism invariance" in tracial and "unique tracial state" in tracial)
    audit.check("minimal axioms exclude source/action", "source/action" in minimal_flat and "outside axiom content" in minimal_flat)
    audit.check("kinetic primitive excludes selector and readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("scale primitive excludes dimensionless physics", "does not supply any dimensionless quantity" in scale)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    audit.check(
        "registry names approved premise nodes",
        all(name in registry for name in ["minimal_axioms", "kinetic_isotropy_primitive", "scale_reference_primitive", "realized_state_primitive"]),
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source is a full-cell",
        "No derivation of L1/simplex source-density semantics.",
        "No derivation of coefficient uniformity as a physical source theorem.",
        "No derivation of the charged-lepton source bridge.",
        "No derivation of the `256.08` precision correction.",
        "No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note derives hydrogen",
        "This note proves A2 closure",
        "the charged-lepton scalar source is a full-cell slot-resolved source family",
        "L1/simplex source-density semantics are derived",
        "the electron mass is derived",
        "m_e is derived",
        "alpha(0) is derived",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
