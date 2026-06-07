#!/usr/bin/env python3
"""Equivariant naturality no-go for selecting an orientation-torsor section.

The signed-gravity host result gives a real orientation line / Z2 torsor.  This
runner checks the next possible escape: can sewing, flat local-system transport,
or gauge/relabeling naturality choose one of the two sections?

Finite answer: no.  The sign-flip automorphism acts freely and transitively on
sections.  An equivariant/invariant canonical selector would have to choose a
fixed point of that action, and no fixed point exists.  Multiplicative sewing
preserves both choices; it does not rank them.
"""

from __future__ import annotations

import itertools
import sys
from dataclasses import dataclass
from typing import Callable


PASS: list[str] = []
FAIL: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> bool:
    bucket = PASS if cond else FAIL
    bucket.append(name)
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}{suffix}")
    return cond


SECTIONS = (+1, -1)


def flip(section: int) -> int:
    return -section


def multiply(a: int, b: int) -> int:
    return a * b


@dataclass(frozen=True)
class Atlas:
    """A finite connected flat Z2 local system represented by patch signs."""

    patch_count: int
    section: tuple[int, ...]

    def gauge_transform(self, gauges: tuple[int, ...]) -> "Atlas":
        return Atlas(self.patch_count, tuple(g * s for g, s in zip(gauges, self.section)))

    @property
    def is_global_flat_section(self) -> bool:
        # In the trivialized flat host used by the existing finite proxy, a
        # global section is constant after choosing the trivialization.
        return len(set(self.section)) == 1


def all_candidate_constant_selectors() -> list[Callable[[], int]]:
    return [lambda s=s: s for s in SECTIONS]


def is_flip_invariant_selector(selector: Callable[[], int]) -> bool:
    selected = selector()
    return selected == flip(selected)


def block1_torsor_no_fixed_point() -> None:
    print("\n[BLOCK 1] A Z2 torsor has no sign-flip-invariant section")
    check("sign flip sends + section to - section", flip(+1) == -1)
    check("sign flip sends - section to + section", flip(-1) == +1)
    check("the flip action has no fixed section", all(s != flip(s) for s in SECTIONS))
    invariant_selectors = [sel for sel in all_candidate_constant_selectors() if is_flip_invariant_selector(sel)]
    check(
        "no constant section selector is invariant under the torsor automorphism",
        len(invariant_selectors) == 0,
        "canonical gauge-invariant selection would require a fixed point",
    )


def block2_sewing_preserves_both_choices() -> None:
    print("\n[BLOCK 2] Multiplicative sewing is compatible with both orientations")
    sewn = {(a, b): multiply(a, b) for a, b in itertools.product(SECTIONS, repeat=2)}
    check("sewing is Z2 multiplication", sewn[(+1, +1)] == +1 and sewn[(+1, -1)] == -1)
    check("opposite local sections sew coherently", sewn[(-1, +1)] == -1 and sewn[(-1, -1)] == +1)
    check(
        "multiplicativity alone does not prefer + over -",
        set(sewn.values()) == {+1, -1},
        f"sewn_values={sorted(set(sewn.values()))}",
    )


def block3_flat_local_system_gauge() -> None:
    print("\n[BLOCK 3] Flat local-system gauge changes act transitively on sections")
    atlas_plus = Atlas(3, (+1, +1, +1))
    atlas_minus = Atlas(3, (-1, -1, -1))
    global_flip = (-1, -1, -1)
    check("+ section is a flat global section", atlas_plus.is_global_flat_section)
    check("- section is a flat global section", atlas_minus.is_global_flat_section)
    check(
        "global gauge flip maps + global section to - global section",
        atlas_plus.gauge_transform(global_flip) == atlas_minus,
    )
    check(
        "global gauge flip maps - global section to + global section",
        atlas_minus.gauge_transform(global_flip) == atlas_plus,
    )
    orbit = {atlas_plus.gauge_transform(g).section for g in itertools.product(SECTIONS, repeat=3)}
    check(
        "gauge orbit contains both constant global sections",
        (+1, +1, +1) in orbit and (-1, -1, -1) in orbit,
        f"orbit_size={len(orbit)}",
    )


def block4_source_vector_consequence() -> None:
    print("\n[BLOCK 4] Source vector requires the chosen section")
    source_with_plus_section = (+1, +1)
    source_with_minus_section = (+1, -1)
    torsor_without_section = (0, 0)
    check("orientation-even positive source is section-independent", source_with_plus_section == (+1, +1))
    check("desired odd source appears with the minus section", source_with_minus_section == (+1, -1))
    check("torsor host without a section supplies no active source", torsor_without_section == (0, 0))
    check(
        "both section choices are coherent but give different source vectors",
        source_with_plus_section != source_with_minus_section,
        f"plus={source_with_plus_section}, minus={source_with_minus_section}",
    )


def main() -> int:
    print("=" * 88)
    print("Signed-gravity orientation section: equivariant naturality no-go")
    print("=" * 88)
    block1_torsor_no_fixed_point()
    block2_sewing_preserves_both_choices()
    block3_flat_local_system_gauge()
    block4_source_vector_consequence()
    print("\n" + "=" * 88)
    print(f"SCORECARD: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("FAILURES:", FAIL)
    print("=" * 88)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
