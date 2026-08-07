#!/usr/bin/env python3
"""Current-packet boundary for YT EW matching rule M.

The runner checks only a finite packet boundary:

- F_adj = (N_c^2 - 1) / N_c^2 = 8/9 at N_c = 3.
- The note states that no retained selector is supplied by this packet.
- The note avoids the broader finite-N_c and exhaustive no-go claims rejected
  by audit.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "YT_EW_MATCHING_RULE_M_NOTE_2026-05-02.md"


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        if ok:
            self.pass_count += 1
            tag = "PASS"
        else:
            self.fail_count += 1
            tag = "FAIL"
        suffix = f" ({detail})" if detail else ""
        print(f"  [{tag}] {label}{suffix}")


def main() -> int:
    gate = Gate()
    text = NOTE.read_text(encoding="utf-8")
    print("YT EW matching rule M current-packet boundary")

    required = [
        "Current-Packet Boundary",
        "Claim type:** no_go",
        "current-packet boundary",
        "F_adj = (N_c^2 - 1) / N_c^2 = 8/9",
        "not derived by this packet",
        "not supplied by this packet",
        "not an exhaustive proof",
        "No external OZI theorem",
        "No external OZI theorem, glueball-spectrum computation, PDG Yukawa value",
        "no retained selector deriving exact physical EW matching rule M",
    ]
    for phrase in required:
        gate.check(f"note contains {phrase!r}", phrase in text)

    forbidden = [
        "The matching rule M is **NOT exact at any finite N_c**",
        "NOT exact at any finite N_c",
        "This is **false**. Glueball intermediate states exist",
        "standard QFT machinery",
        "exact OZI-vanishing theorem at all genus orders — not available",
        "downstream rows may cite an exact physical R_conn = 8/9 derivation",
        "would become retained",
        "\nStatus: retained\n",
        "\nStatus: promoted\n",
    ]
    for phrase in forbidden:
        gate.check(f"note avoids broad/forbidden phrase {phrase!r}", phrase not in text)

    n_c = Fraction(3, 1)
    dim_full = n_c * n_c
    dim_singlet = Fraction(1, 1)
    dim_adjoint = dim_full - dim_singlet
    f_adj = dim_adjoint / dim_full
    gate.check("N_c is the configured color rank 3", n_c == 3, f"N_c={n_c}")
    gate.check("full color trace dimension is N_c^2 = 9", dim_full == 9, f"dim_full={dim_full}")
    gate.check("singlet channel dimension is 1", dim_singlet == 1, f"dim_singlet={dim_singlet}")
    gate.check("adjoint channel dimension is 8", dim_adjoint == 8, f"dim_adjoint={dim_adjoint}")
    gate.check("F_adj is exactly 8/9", f_adj == Fraction(8, 9), f"F_adj={f_adj}")

    for route in ["S1", "S2", "S3"]:
        gate.check(f"{route} is listed as a current-packet gap", f"`{route}`" in text)

    gate.check("the repaired note links no conditional OZI dependency", "EW_CURRENT_MATCHING_OZI_SUPPRESSION" not in text)
    gate.check("the repaired note leaves audit authority external", "independent audit lane only" in text)

    total = gate.pass_count + gate.fail_count
    n_arith = 5
    print("\nN5 execution certificate")
    print(
        f"per_element: checked and not executed — stated plainly, this file is "
        f"a note-structure verifier plus a dimension count, and it never "
        f"builds an operator, a vector or a matrix of any kind, so it resolves "
        f"no matrix element whatsoever."
    )
    print(
        f"per_site: checked and not executed — the boundary it certifies "
        f"concerns which sentences the source note may and may not contain, "
        f"together with colour-channel dimensions; neither of those carries a "
        f"position argument and no lattice site is ever defined."
    )
    print(
        f"per_mode: checked and not executed — there is no spectrum, no "
        f"momentum variable and no eigenvector in the file; the only numbers "
        f"it computes are the integers {dim_full}, {dim_singlet} and "
        f"{dim_adjoint} together with their ratio."
    )
    print(
        f"per_block: dimension counting only — the colour blocks enter purely "
        f"as the integer dimensions singlet {dim_singlet} and adjoint "
        f"{dim_adjoint} out of N_c^2 = {dim_full}, giving F_adj = {f_adj} "
        f"exactly in Fraction arithmetic, and that count is the whole "
        f"numerical content: {total - n_arith} of the {total} checks are "
        f"note-substring assertions and the remaining {n_arith} are this "
        f"count."
    )
    print(
        f"lattice_wide: checked and not executed — no lattice object of any "
        f"kind is present here, and the runner's own declared scope is a "
        f"current-packet boundary on a single note, which asserts nothing at "
        f"any lattice extent, volume or limit."
    )

    ok = gate.fail_count == 0
    print(f"\nYT EW matching rule M current-packet boundary: {'PASS' if ok else 'FAIL'}")
    print(f"PASS={gate.pass_count} FAIL={gate.fail_count}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
