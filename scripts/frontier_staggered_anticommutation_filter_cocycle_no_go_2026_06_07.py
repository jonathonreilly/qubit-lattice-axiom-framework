#!/usr/bin/env python3
"""Multi-loop exchange-cocycle consistency does not force CAR.

This runner attacks the first route left open by the spin-statistics exercise:
could joint consistency of many exchange loops on a Z^3 patch force the
fermionic cross-site sign?  In the abelian Z2 exchange-character reduction, the
Coxeter/braid relations force only a uniform statistics character.  The value
of that character remains q=+1 or q=-1.

The consequence for the staggered chirality lane is narrow: this route cannot
supply the CAR/graded-locality premise that would then supply the
{D,gamma5}=0 filter used by the staggered epsilon enumerator.
"""

from __future__ import annotations

import itertools
import sys
from dataclasses import dataclass
from typing import Iterable


PASS: list[str] = []
FAIL: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> bool:
    bucket = PASS if cond else FAIL
    bucket.append(name)
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}{suffix}")
    return cond


@dataclass(frozen=True)
class Assignment:
    """A one-dimensional Z2 exchange character on Coxeter generators."""

    signs: tuple[int, ...]  # signs[i] is chi(s_{i+1}) in {+1,-1}

    def sign_of_word(self, word: Iterable[int]) -> int:
        out = 1
        for generator in word:
            out *= self.signs[generator - 1]
        return out

    @property
    def is_uniform(self) -> bool:
        return len(set(self.signs)) == 1

    @property
    def label(self) -> str:
        if self.signs and all(s == 1 for s in self.signs):
            return "hard-core-boson/trivial exchange character"
        if self.signs and all(s == -1 for s in self.signs):
            return "CAR/fermion sign character"
        return "mixed nonuniform character"


def coxeter_relations_hold(n_particles: int, assignment: Assignment) -> bool:
    """Check the type-A Coxeter relations for S_n in a Z2 character."""

    n_generators = n_particles - 1

    # Involutions: s_i^2 = e.
    for i in range(1, n_generators + 1):
        if assignment.sign_of_word([i, i]) != 1:
            return False

    # Distant commute: s_i s_j = s_j s_i for |i-j| > 1.
    for i in range(1, n_generators + 1):
        for j in range(i + 2, n_generators + 1):
            if assignment.sign_of_word([i, j]) != assignment.sign_of_word([j, i]):
                return False

    # Adjacent braid loops: s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1}.
    for i in range(1, n_generators):
        lhs = assignment.sign_of_word([i, i + 1, i])
        rhs = assignment.sign_of_word([i + 1, i, i + 1])
        if lhs != rhs:
            return False

    return True


def enumerate_survivors(n_particles: int) -> list[Assignment]:
    n_generators = n_particles - 1
    candidates = [Assignment(tuple(signs)) for signs in itertools.product((1, -1), repeat=n_generators)]
    return [a for a in candidates if coxeter_relations_hold(n_particles, a)]


def adjacent_braid_forces_uniformity(n_particles: int) -> bool:
    survivors = enumerate_survivors(n_particles)
    return bool(survivors) and all(a.is_uniform for a in survivors)


def block1_exchange_relations() -> None:
    print("\n[BLOCK 1] Multi-loop Coxeter consistency leaves two uniform characters")
    for n_particles in (3, 4, 5, 6):
        survivors = enumerate_survivors(n_particles)
        labels = [a.label for a in survivors]
        check(
            f"S_{n_particles}: exactly two Z2 exchange-character survivors",
            len(survivors) == 2,
            f"labels={labels}",
        )
        check(
            f"S_{n_particles}: adjacent braid loops force uniformity, not sign value",
            adjacent_braid_forces_uniformity(n_particles),
            f"survivors={[a.signs for a in survivors]}",
        )


def block2_both_statistics_frames_survive() -> None:
    print("\n[BLOCK 2] Boson and fermion characters both satisfy all loop relations")
    for n_particles in (4, 5):
        boson = Assignment(tuple(1 for _ in range(n_particles - 1)))
        fermion = Assignment(tuple(-1 for _ in range(n_particles - 1)))
        check(
            f"S_{n_particles}: hard-core-boson/trivial character passes",
            coxeter_relations_hold(n_particles, boson),
            f"signs={boson.signs}",
        )
        check(
            f"S_{n_particles}: CAR/fermion sign character passes",
            coxeter_relations_hold(n_particles, fermion),
            f"signs={fermion.signs}",
        )


def block3_selector_location() -> None:
    print("\n[BLOCK 3] Selecting CAR requires an extra predicate")
    n_particles = 5
    survivors = enumerate_survivors(n_particles)
    selected_by_car_predicate = [a for a in survivors if a.signs[0] == -1]
    selected_by_boson_predicate = [a for a in survivors if a.signs[0] == 1]
    check(
        "extra predicate chi(s_1)=-1 selects CAR uniquely",
        len(selected_by_car_predicate) == 1 and selected_by_car_predicate[0].label.startswith("CAR"),
        f"selected={selected_by_car_predicate[0].signs if selected_by_car_predicate else None}",
    )
    check(
        "opposite predicate chi(s_1)=+1 selects hard-core-boson uniquely",
        len(selected_by_boson_predicate) == 1 and selected_by_boson_predicate[0].label.startswith("hard-core"),
        f"selected={selected_by_boson_predicate[0].signs if selected_by_boson_predicate else None}",
    )
    check(
        "loop consistency alone has no predicate that ranks the two survivors",
        len(survivors) == 2 and {a.signs[0] for a in survivors} == {1, -1},
        "the selector is exactly the global exchange sign q",
    )


def block4_staggered_filter_consequence() -> None:
    print("\n[BLOCK 4] Consequence for the staggered anticommutation filter")
    survivors = enumerate_survivors(5)
    hard_core_survives = any(all(s == 1 for s in a.signs) for a in survivors)
    car_survives = any(all(s == -1 for s in a.signs) for a in survivors)
    check(
        "hard-core-boson exchange survives every tested multi-loop constraint",
        hard_core_survives,
    )
    check(
        "CAR exchange also survives, so consistency gives compatibility not forcing",
        car_survives,
    )
    check(
        "therefore this route cannot supply the {D,gamma5}=0 filter",
        hard_core_survives and car_survives,
        "the staggered epsilon theorem still needs a separate CAR/graded-locality/chiral premise",
    )


def main() -> int:
    print("=" * 88)
    print("Staggered anticommutation filter: multi-loop cocycle no-go for CAR forcing")
    print("=" * 88)
    block1_exchange_relations()
    block2_both_statistics_frames_survive()
    block3_selector_location()
    block4_staggered_filter_consequence()
    print("\n" + "=" * 88)
    print(f"SCORECARD: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("FAILURES:", FAIL)
    print("=" * 88)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    sys.exit(main())
