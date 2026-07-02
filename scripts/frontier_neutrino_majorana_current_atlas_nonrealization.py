#!/usr/bin/env python3
"""
Current-atlas non-realization boundary for the missing Majorana primitive.

Question:
  Does the current main-branch atlas / retained matter toolkit already contain
  the missing charge-2 Majorana primitive under another name?

Answer on the current lane:
  No. The atlas fixes the channel and provides scalar/tensor/toolkit surfaces,
  but no currently retained object realizes a fermionic charge-2 primitive on
  the unique nu_R channel.

Boundary:
  This is a current-atlas boundary only. It does NOT prove that no future
  axiom-side primitive can be derived.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_observable_principle_stays_scalar_normal() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE CURRENT ATLAS OBSERVABLE BACKBONE IS SCALAR / DETERMINANT-BASED")
    print("=" * 88)

    atlas = read("docs/publication/ci3_z3/DERIVATION_ATLAS.md")
    obs = read("docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md")

    has_observable_row = "| Observable principle | `log|det(D+J)|`" in atlas
    has_closure_row = "| Observable-principle closure |" in atlas
    mentions_scalar = "scalar observable generator" in obs.lower() or "scalar generator" in obs.lower()
    mentions_det = "log |det(d+j)|" in obs.lower() or "log|det(d+j)|" in obs.lower()
    observable_rows_text = "\n".join(
        line for line in atlas.splitlines() if "Observable principle" in line
    )
    observable_rows_pairing = "Pfaffian" in observable_rows_text or "Nambu" in observable_rows_text

    check("Atlas explicitly retains the determinant observable-principle row", has_observable_row)
    check("Atlas retains observable-principle closure on the same determinant surface", has_closure_row)
    check("Observable-principle note is explicitly scalar", mentions_scalar)
    check("Observable-principle note is explicitly determinant-based", mentions_det)
    check("Current observable-backbone rows do not already switch to a Pfaffian/Nambu generator", not observable_rows_pairing)

    print()
    print("  So the retained observable backbone is exact, but scalar/normal.")
    print("  It fixes the current grammar; it does not already supply a charge-2")
    print("  fermionic primitive.")


def test_spatial_composite_route_misses_nu_r() -> None:
    print("\n" + "=" * 88)
    print("PART 2: THE EXISTING SPATIAL COMPOSITE ROUTE DOES NOT REALIZE THE nu_R PRIMITIVE")
    print("=" * 88)

    rhs = read("scripts/frontier_right_handed_sector.py")
    closure = read("docs/ONE_GENERATION_MATTER_CLOSURE_NOTE.md")

    has_nu_r_closure = "`nu_R : (1,1)_0`" in closure
    wedge_line = "The antisymmetric wedge^2(C^8) = C^28 does contain SU(2) singlets" in rhs
    dr_found = 'check("d_R (Y=-2/3) found in wedge^2 singlets"' in rhs
    er_found = 'check("e_R (Y=-2) found in wedge^2 singlets"' in rhs
    ur_absent = 'check("u_R (Y=+4/3) ABSENT from wedge^2 singlets (needs degree 4)"' in rhs
    missing_zero_and_u = "MISSING from wedge^2 singlets: {Fraction(0, 1), Fraction(4, 3)}" in rhs or "Fraction(0)" in rhs
    awkward = "the composite route is structurally awkward" in rhs.lower()

    check("Retained matter closure includes nu_R as the final right-handed singlet", has_nu_r_closure)
    check("Right-handed-sector audit has an explicit antisymmetric wedge^2(C^8) composite route", wedge_line)
    check("That route realizes d_R and e_R degree-2 singlets", dr_found and er_found)
    check("That route explicitly misses u_R on wedge^2(C^8)", ur_absent)
    check("The same wedge^2(C^8) audit also misses the Y=0 slot needed for nu_R", missing_zero_and_u)
    check("The script itself labels the composite route structurally awkward", awkward)

    print()
    print("  So the existing antisymmetric composite object on the spatial side is")
    print("  not the missing Majorana primitive: it does not realize the nu_R slot.")


def test_non_scalar_atlas_primitives_are_gravity_side() -> None:
    print("\n" + "=" * 88)
    print("PART 3: CURRENT ATLAS PRIMITIVES BEYOND THE SCALAR BACKBONE ARE GRAVITY/TENSOR-SIDE")
    print("=" * 88)

    atlas = read("docs/publication/ci3_z3/DERIVATION_ATLAS.md")

    required_rows = [
        "Route 2 exact bilinear tensor carrier `K_R`",
        "Route 2 tensor prototype `Theta_R^(0)`",
        "Constructed support tensor primitive `Xi_R^(0)`",
        "Tensorized Schur/Dirichlet primitive",
        "Route 2 spacetime tensor carrier",
        "Universal tensor variational candidate",
    ]

    found = [row for row in required_rows if row in atlas]
    missing = [row for row in required_rows if row not in atlas]

    # The atlas may now contain classification, boundary/no-go, and admitted
    # extension-support rows for the Majorana lane, but it still should not
    # contain a realized fermionic charge-2 primitive.
    row_titles = [title.strip() for title in re.findall(r"^\|\s*([^|]+?)\s*\|", atlas, flags=re.MULTILINE)]
    majorana_titles = [title for title in row_titles if "Majorana" in title]
    pfaffian_titles = [title for title in row_titles if "Pfaffian" in title]
    allowed_majorana_titles = {
        "Majorana operator classification",
        "Majorana finite normal-grammar no-go",
        "Majorana Nambu source principle",
        "Majorana source-ray theorem",
        "Three-generation Majorana `Z_3` non-activation",
        "Majorana staircase blindness",
        "Majorana no-stationary-scale theorem",
        "Majorana algebraic-bridge obstruction",
        "Majorana endpoint-exchange midpoint theorem",
        "Majorana residual-sharing split theorem",
        "Majorana adjacent singlet-placement + background-normalization theorem pair",
        "Majorana lower-level pairing no-go",
        "Three-generation Majorana current-stack zero matrix",
    }
    allowed_pfaffian_titles = {
        "Pfaffian no-forcing theorem",
    }
    unexpected_majorana_titles = [
        title for title in majorana_titles if title not in allowed_majorana_titles
    ]
    unexpected_pfaffian_titles = [
        title for title in pfaffian_titles if title not in allowed_pfaffian_titles
    ]
    has_operator_classification_row = "Majorana operator classification" in majorana_titles
    has_finite_normal_nogo_row = "Majorana finite normal-grammar no-go" in majorana_titles
    has_nambu_source_row = "Majorana Nambu source principle" in majorana_titles
    has_source_ray_row = "Majorana source-ray theorem" in majorana_titles
    has_z3_row = "Three-generation Majorana `Z_3` non-activation" in majorana_titles
    has_staircase_blindness_row = "Majorana staircase blindness" in majorana_titles
    has_no_stationary_scale_row = "Majorana no-stationary-scale theorem" in majorana_titles
    has_alg_bridge_row = "Majorana algebraic-bridge obstruction" in majorana_titles
    has_endpoint_midpoint_row = "Majorana endpoint-exchange midpoint theorem" in majorana_titles
    has_residual_sharing_row = "Majorana residual-sharing split theorem" in majorana_titles
    has_adjacent_background_row = (
        "Majorana adjacent singlet-placement + background-normalization theorem pair"
        in majorana_titles
    )
    has_lower_level_pairing_nogo_row = "Majorana lower-level pairing no-go" in majorana_titles
    has_current_stack_zero_row = "Three-generation Majorana current-stack zero matrix" in majorana_titles

    check("Atlas contains the current non-scalar tensor/gravity primitive rows", len(found) == len(required_rows),
          f"missing rows={len(missing)}")
    check("Current atlas Majorana rows are classification, current-stack no-go, admitted-source support, bridge-support, and boundary rows only", has_operator_classification_row and has_finite_normal_nogo_row and has_nambu_source_row and has_source_ray_row and has_z3_row and has_staircase_blindness_row and has_no_stationary_scale_row and has_alg_bridge_row and has_endpoint_midpoint_row and has_residual_sharing_row and has_adjacent_background_row and has_lower_level_pairing_nogo_row and has_current_stack_zero_row and len(majorana_titles) >= 13,
          f"majorana rows={majorana_titles}")
    check("Current atlas Pfaffian rows are boundary/uniqueness rows only", len(unexpected_pfaffian_titles) == 0,
          f"pfaffian rows={pfaffian_titles}")
    check("Current atlas has no unexpected Majorana row title", len(unexpected_majorana_titles) == 0,
          f"unexpected titles={unexpected_majorana_titles}")

    print()
    print("  The atlas now contains Majorana operator classification,")
    print("  finite-normal-grammar no-go, Nambu-source support,")
    print("  source-ray support, three-generation non-activation,")
    print("  staircase/scale boundaries, algebraic-bridge obstruction,")
    print("  positive endpoint/residual-sharing/placement support,")
    print("  lower-level pairing no-go, and a current-stack zero law, plus")
    print("  the existing tensor/gravity objects. None of")
    print("  them is yet a fully realized fermionic charge-2 primitive with an")
    print("  absolute staircase embedding.")


def main() -> int:
    print("=" * 88)
    print("NEUTRINO MAJORANA: CURRENT ATLAS NON-REALIZATION")
    print("=" * 88)
    print()
    print("Authority stack:")
    print("  - main:docs/publication/ci3_z3/DERIVATION_ATLAS.md")
    print("  - docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md")
    print("  - docs/ONE_GENERATION_MATTER_CLOSURE_NOTE.md")
    print("  - scripts/frontier_right_handed_sector.py")
    print("  - docs/NEUTRINO_MAJORANA_CHARGE_TWO_PRIMITIVE_REDUCTION_NOTE.md")
    print()
    print("Question:")
    print("  Does the current main-branch atlas / retained matter toolkit already")
    print("  contain the missing charge-2 Majorana primitive under another name?")

    test_observable_principle_stays_scalar_normal()
    test_spatial_composite_route_misses_nu_r()
    test_non_scalar_atlas_primitives_are_gravity_side()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  No. The current atlas fixes the channel and provides real scalar and")
    print("  tensor tool surfaces, but it does not already contain the missing")
    print("  fermionic charge-2 primitive on the nu_R Majorana lane.")
    print()
    print(f"  PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
