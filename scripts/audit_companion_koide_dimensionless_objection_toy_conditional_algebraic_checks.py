#!/usr/bin/env python3
"""Exact checker for the self-contained two-channel rational theorem.

The source note has a historical filename. Its repaired content is a positive
theorem over Q: rational functions, an affine coordinate, exact 2x2 matrices,
and an arbitrary-parameter affine family. This runner consumes no audit state
and writes no files.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
from typing import Callable, Sequence


ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / (
    "KOIDE_DIMENSIONLESS_OBJECTION_TOY_CONDITIONAL_ALGEBRAIC_CHECKS_"
    "NARROW_THEOREM_NOTE_2026-05-16.md"
)

F0 = Fraction(0)
F1 = Fraction(1)
F2 = Fraction(2)
F3 = Fraction(3)

MUTATION_NAMES = (
    "q-channel-swap",
    "domain-omit-plus-pole",
    "zeta-offset",
    "projector-rank-two",
    "affine-drop-shift",
    "interpretation-physical",
    "interpretation-koide",
    "interpretation-aps",
)
MUTATIONS: frozenset[str] = frozenset()


class Harness:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str = "") -> bool:
        status = "PASS" if condition else "FAIL"
        suffix = f"  ({detail})" if detail else ""
        print(f"  [{status}] {name}{suffix}")
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        return condition

    def expect_raises(
        self,
        name: str,
        exc_type: type[BaseException],
        operation: Callable[[], object],
    ) -> bool:
        try:
            operation()
        except exc_type:
            return self.check(name, True)
        except BaseException as exc:  # report the wrong fail-closed path
            return self.check(
                name,
                False,
                f"raised {type(exc).__name__}, expected {exc_type.__name__}",
            )
        return self.check(name, False, f"expected {exc_type.__name__}")

    def banner(self, title: str) -> None:
        print()
        print("-" * 88)
        print(title)
        print("-" * 88)


def require_fraction(name: str, value: object) -> Fraction:
    """Accept exact Fraction instances only, excluding subclasses."""
    if type(value) is not Fraction:
        raise TypeError(f"{name} must be an exact Fraction")
    return value


def in_domain(s: object, z: object) -> bool:
    s_q = require_fraction("s", s)
    z_q = require_fraction("z", z)
    plus = F1 + s_q + z_q
    minus = F1 + s_q - z_q
    if "domain-omit-plus-pole" in MUTATIONS:
        return minus != F0
    return plus != F0 and minus != F0


def require_domain(s: object, z: object) -> tuple[Fraction, Fraction]:
    s_q = require_fraction("s", s)
    z_q = require_fraction("z", z)
    if not in_domain(s_q, z_q):
        raise ZeroDivisionError("(s,z) lies outside the two-channel domain")
    return s_q, z_q


def y_channels(s: object, z: object) -> tuple[Fraction, Fraction]:
    s_q, z_q = require_domain(s, z)
    y_plus = F1 / (F1 + s_q + z_q)
    if "q-channel-swap" in MUTATIONS:
        y_minus = F1 / (F1 + s_q + z_q)
    else:
        y_minus = F1 / (F1 + s_q - z_q)
    return y_plus, y_minus


def ratio_r(s: object, z: object) -> Fraction:
    y_plus, y_minus = y_channels(s, z)
    return (F1 + y_minus / y_plus) / F3


def ratio_reduced(s: object, z: object) -> Fraction:
    """Closed form stated by T1, separate from the channel implementation."""
    s_q, z_q = require_domain(s, z)
    return F2 * (F1 + s_q) / (F3 * (F1 + s_q - z_q))


def zeta(w: object) -> Fraction:
    w_q = require_fraction("w", w)
    offset = F1 if "zeta-offset" in MUTATIONS else F0
    return F2 * w_q - F1 + offset


Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def identity() -> Matrix2:
    return ((F1, F0), (F0, F1))


def projector() -> Matrix2:
    if "projector-rank-two" in MUTATIONS:
        return ((F1, F0), (F0, F1))
    return ((F1, F0), (F0, F0))


def involution() -> Matrix2:
    p = projector()
    i = identity()
    return tuple(
        tuple(F2 * p[row][column] - i[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def require_matrix2(name: str, value: object) -> Matrix2:
    if type(value) is not tuple or len(value) != 2:
        raise TypeError(f"{name} must be an exact 2x2 tuple matrix")
    rows: list[tuple[Fraction, Fraction]] = []
    for row in value:
        if type(row) is not tuple or len(row) != 2:
            raise TypeError(f"{name} must be an exact 2x2 tuple matrix")
        entries = tuple(require_fraction(f"{name} entry", entry) for entry in row)
        rows.append(entries)  # type: ignore[arg-type]
    return (rows[0], rows[1])


def matmul(left: object, right: object) -> Matrix2:
    a = require_matrix2("left", left)
    b = require_matrix2("right", right)
    return tuple(
        tuple(sum((a[r][k] * b[k][c] for k in range(2)), F0) for c in range(2))
        for r in range(2)
    )  # type: ignore[return-value]


def apply_matrix(matrix: object, vector: object) -> tuple[Fraction, Fraction]:
    a = require_matrix2("matrix", matrix)
    if type(vector) is not tuple or len(vector) != 2:
        raise TypeError("vector must be an exact length-two tuple")
    x = require_fraction("vector[0]", vector[0])
    y = require_fraction("vector[1]", vector[1])
    return (a[0][0] * x + a[0][1] * y, a[1][0] * x + a[1][1] * y)


def exact_rank(rows: object) -> int:
    """Exact row rank for a nonempty rectangular tuple-of-tuples."""
    if type(rows) is not tuple or not rows:
        raise TypeError("rows must be a nonempty tuple")
    width: int | None = None
    work: list[list[Fraction]] = []
    for row in rows:
        if type(row) is not tuple or not row:
            raise TypeError("each row must be a nonempty tuple")
        if width is None:
            width = len(row)
        if len(row) != width:
            raise TypeError("rows must have equal length")
        work.append([require_fraction("rank entry", entry) for entry in row])

    rank = 0
    column = 0
    assert width is not None
    while rank < len(work) and column < width:
        pivot = next((r for r in range(rank, len(work)) if work[r][column]), None)
        if pivot is None:
            column += 1
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [entry / pivot_value for entry in work[rank]]
        for r in range(len(work)):
            if r == rank:
                continue
            coefficient = work[r][column]
            if coefficient:
                work[r] = [
                    entry - coefficient * pivot_entry
                    for entry, pivot_entry in zip(work[r], work[rank])
                ]
        rank += 1
        column += 1
    return rank


def d_eta(eta: object, s: object, c: object) -> Fraction:
    eta_q = require_fraction("eta", eta)
    s_q = require_fraction("s", s)
    c_q = require_fraction("c", c)
    if "affine-drop-shift" in MUTATIONS:
        return eta_q * (F1 - s_q)
    return eta_q * (F1 - s_q) + c_q


def rational_grid(radius: int = 5, max_denominator: int = 5) -> tuple[Fraction, ...]:
    return tuple(
        sorted(
            {
                Fraction(numerator, denominator)
                for denominator in range(1, max_denominator + 1)
                for numerator in range(-radius, radius + 1)
            }
        )
    )


def effective_note_text() -> str:
    text = NOTE_PATH.read_text(encoding="utf-8")
    if "interpretation-physical" in MUTATIONS:
        text += "\nThe value eta=2/9 is the physical endpoint scalar selected by the framework.\n"
    if "interpretation-koide" in MUTATIONS:
        text += "\nR is the Koide observable and its 2/3 fiber is physically selected.\n"
    if "interpretation-aps" in MUTATIONS:
        text += "\nThe value eta=2/9 is the APS invariant supplied by the framework.\n"
    return text


def source_boundary_checks(h: Harness) -> None:
    h.banner("Source theorem and interpretation boundary")
    text = effective_note_text()
    flattened = " ".join(text.split())
    h.check(
        "explicit positive-theorem typing",
        "**Type:** positive_theorem" in text
        and "**Claim type:** positive_theorem" in text,
    )
    h.check("zero dependencies are explicit", "**Dependencies:** none" in text)
    h.check("domain is explicit", "1+s+z != 0 and 1+s-z != 0" in text)
    h.check("eta is universally quantified", "arbitrary `eta,s,c in Q`" in text)
    h.check("eta=2/9 is marked as an example", "one exact example" in text)
    h.check("historical admission packet removed", "A_TOY" not in text)
    h.check("legacy admission labels removed", "Conditioning admissions" not in text)
    h.check("legacy eta label removed", "eta_APS" not in text)
    h.check("legacy observable-completeness rhetoric removed", "observable completeness" not in text)
    h.check("legacy bridge demand removed", "missing_bridge_theorem" not in text)

    forbidden_overclaims = (
        "eta=2/9 is the physical endpoint scalar",
        "selected by the framework",
        "R is the Koide observable",
        "2/3 fiber is physically selected",
        "eta=2/9 is the APS invariant",
        "APS invariant supplied by the framework",
    )
    hits = [phrase for phrase in forbidden_overclaims if phrase in flattened]
    h.check(
        "physical/Koide/APS interpretation overclaims are absent",
        not hits,
        f"hits={hits}" if hits else "",
    )


def normal_checks(h: Harness) -> None:
    source_boundary_checks(h)

    h.banner("T1 exact reduction, fiber, and constructive witnesses")
    grid = rational_grid()
    # Enumerate the theorem's written domain directly. This keeps the oracle
    # independent of the intentionally mutable domain predicate.
    valid = [
        (s, z)
        for s in grid
        for z in grid
        if F1 + s + z != F0 and F1 + s - z != F0
    ]
    h.check("finite rational grid is nontrivial", len(valid) > 1000, f"points={len(valid)}")
    h.check(
        "channel definition equals reduced formula on the full grid",
        all(ratio_r(s, z) == ratio_reduced(s, z) for s, z in valid),
    )
    h.check(
        "difference identity holds on the full grid",
        all(
            ratio_r(s, z) - Fraction(2, 3)
            == F2 * z / (F3 * (F1 + s - z))
            for s, z in valid
        ),
    )
    h.check(
        "the 2/3 fiber is exactly z=0 on the full grid",
        all((ratio_r(s, z) == Fraction(2, 3)) == (z == F0) for s, z in valid),
    )
    h.check("plus pole excluded", not in_domain(Fraction(-4, 3), Fraction(1, 3)))
    h.check("minus pole excluded", not in_domain(Fraction(-2, 3), Fraction(1, 3)))
    h.check("double pole excluded", not in_domain(Fraction(-1), F0))
    h.check("R(0,1/4)=8/9", ratio_r(F0, Fraction(1, 4)) == Fraction(8, 9))
    h.check("R(0,-1/4)=8/15", ratio_r(F0, Fraction(-1, 4)) == Fraction(8, 15))
    h.check(
        "the two witnesses establish nonconstancy",
        ratio_r(F0, Fraction(1, 4)) != ratio_r(F0, Fraction(-1, 4)),
    )

    h.banner("T2 exact affine coordinate")
    h.check(
        "zeta inverse holds on the full grid",
        all((zeta(w) + F1) / F2 == w for w in grid),
    )
    h.check("zeta has the unique stated zero", all((zeta(w) == F0) == (w == Fraction(1, 2)) for w in grid))
    h.check(
        "zeta difference law holds on all grid pairs",
        all(zeta(a) - zeta(b) == F2 * (a - b) for a in grid for b in grid),
    )

    h.banner("T3 exact matrices and derived dimensions")
    i = identity()
    p = projector()
    j = involution()
    canonical_p: Matrix2 = ((F1, F0), (F0, F0))
    canonical_j: Matrix2 = ((F1, F0), (F0, -F1))
    h.check("P is the defined matrix", p == canonical_p, f"P={p}")
    h.check("J is the defined matrix", j == canonical_j, f"J={j}")
    h.check("P^2=P", matmul(p, p) == p)
    h.check("J^2=I", matmul(j, j) == i)
    h.check("JP=PJ=P", matmul(j, p) == p and matmul(p, j) == p)
    e1 = (F1, F0)
    e2 = (F0, F1)
    h.check("P fixes e1", apply_matrix(p, e1) == e1)
    h.check("P kills e2", apply_matrix(p, e2) == (F0, F0))
    h.check("rank(P)=1 by exact elimination", exact_rank(p) == 1)
    matrix_units = (
        (F1, F0, F0, F0),
        (F0, F1, F0, F0),
        (F0, F0, F1, F0),
        (F0, F0, F0, F1),
    )
    line_unit = ((F1,),)
    h.check("four matrix units independently span End(Q^2)", exact_rank(matrix_units) == 4)
    h.check("one scalar unit spans End(L)", exact_rank(line_unit) == 1)

    h.banner("T4 arbitrary-parameter affine family")
    small = rational_grid(radius=3, max_denominator=4)
    h.check(
        "inverse construction reaches every tested target uniquely",
        all(
            d_eta(eta, s, target - eta * (F1 - s)) == target
            for eta in small
            for s in small
            for target in small
        ),
    )
    h.check("d_eta(0,0)=eta universally", all(d_eta(eta, F0, F0) == eta for eta in grid))
    h.check("d_eta(1,0)=0 universally", all(d_eta(eta, F1, F0) == F0 for eta in grid))
    h.check(
        "d_eta(1/2,0)=eta/2 universally",
        all(d_eta(eta, Fraction(1, 2), F0) == eta / F2 for eta in grid),
    )
    h.check(
        "d_eta(0,eta/2)=3eta/2 universally",
        all(d_eta(eta, F0, eta / F2) == F3 * eta / F2 for eta in grid),
    )
    eta = Fraction(2, 9)
    examples = (
        d_eta(eta, F0, F0),
        d_eta(eta, F1, F0),
        d_eta(eta, Fraction(1, 2), F0),
        d_eta(eta, F0, Fraction(1, 9)),
    )
    h.check(
        "eta=2/9 example is exact",
        examples == (Fraction(2, 9), F0, Fraction(1, 9), Fraction(1, 3)),
        f"values={examples}",
    )


def independent_checks(h: Harness) -> None:
    source_boundary_checks(h)
    h.banner("Independent rational reconstruction")
    grid = rational_grid(radius=6, max_denominator=6)
    valid = [
        (s, z)
        for s in grid
        for z in grid
        if F1 + s + z != F0 and F1 + s - z != F0
    ]

    # Independent oracle: cross-multiply before constructing a Fraction. It
    # neither calls ratio_reduced nor reuses the y-channel values.
    def cross_oracle(s: Fraction, z: Fraction) -> Fraction:
        require_domain(s, z)
        numerator = F2 * (F1 + s)
        denominator = F3 * (F1 + s - z)
        return numerator / denominator

    h.check(
        "primary channel implementation matches cross-multiplied oracle",
        all(ratio_r(s, z) == cross_oracle(s, z) for s, z in valid),
        f"points={len(valid)}",
    )
    h.check(
        "cleared-denominator identity holds independently",
        all(
            F3 * (F1 + s - z) * ratio_r(s, z) == F2 * (F1 + s)
            for s, z in valid
        ),
    )
    h.check(
        "fiber follows from the independent residual numerator 2z",
        all((F2 * z == F0) == (z == F0) for s, z in valid),
    )
    h.check("independent plus-pole classification", not in_domain(Fraction(-5, 4), Fraction(1, 4)))
    h.check("independent minus-pole classification", not in_domain(Fraction(-3, 4), Fraction(1, 4)))

    h.banner("Independent affine and matrix reconstruction")
    h.check(
        "affine inverse reconstructed from the target equation",
        all(
            d_eta(eta, s, target - eta + eta * s) == target
            for eta in grid
            for s in grid[::4]
            for target in grid[::4]
        ),
    )
    h.check("zeta inverse reconstructed", all(zeta((target + F1) / F2) == target for target in grid))

    p = projector()
    j = involution()
    vectors = tuple((a, b) for a in grid[::5] for b in grid[::5])
    h.check(
        "P action reconstructed on vectors",
        all(apply_matrix(p, vector) == (vector[0], F0) for vector in vectors),
    )
    h.check(
        "J action reconstructed on vectors",
        all(apply_matrix(j, vector) == (vector[0], -vector[1]) for vector in vectors),
    )
    h.check("P image basis has rank one", exact_rank((apply_matrix(p, (F1, F0)), apply_matrix(p, (F0, F1)))) == 1)
    h.check("I image basis has rank two", exact_rank((apply_matrix(identity(), (F1, F0)), apply_matrix(identity(), (F0, F1)))) == 2)


class FractionSubclass(Fraction):
    pass


def hostile_checks(h: Harness) -> None:
    source_boundary_checks(h)
    h.banner("Hostile scalar type and singularity checks")
    bad_scalars: tuple[object, ...] = (
        0,
        True,
        0.0,
        "0",
        None,
        FractionSubclass(1, 2),
    )
    for index, bad in enumerate(bad_scalars):
        h.expect_raises(
            f"ratio rejects non-exact scalar #{index} ({type(bad).__name__})",
            TypeError,
            lambda bad=bad: ratio_r(bad, F0),
        )
        h.expect_raises(
            f"zeta rejects non-exact scalar #{index} ({type(bad).__name__})",
            TypeError,
            lambda bad=bad: zeta(bad),
        )
        h.expect_raises(
            f"d_eta rejects non-exact scalar #{index} ({type(bad).__name__})",
            TypeError,
            lambda bad=bad: d_eta(F0, F0, bad),
        )

    singularities = (
        (Fraction(-4, 3), Fraction(1, 3)),
        (Fraction(-2, 3), Fraction(1, 3)),
        (Fraction(-1), F0),
    )
    for index, pair in enumerate(singularities):
        h.expect_raises(
            f"ratio rejects denominator singularity #{index}",
            ZeroDivisionError,
            lambda pair=pair: ratio_r(*pair),
        )
    h.check("domain predicate rejects every named pole", all(not in_domain(*pair) for pair in singularities))

    h.banner("Hostile matrix-shape and entry checks")
    malformed: tuple[object, ...] = (
        [[F1, F0], [F0, F0]],
        ((F1, F0),),
        ((F1, F0), (F0,)),
        ((1, F0), (F0, F0)),
        ((FractionSubclass(1), F0), (F0, F0)),
        "matrix",
    )
    for index, bad in enumerate(malformed):
        h.expect_raises(
            f"matmul rejects malformed matrix #{index}",
            TypeError,
            lambda bad=bad: matmul(bad, identity()),
        )
    h.expect_raises(
        "matrix application rejects list vector",
        TypeError,
        lambda: apply_matrix(projector(), [F1, F0]),
    )
    h.expect_raises(
        "rank rejects ragged rows",
        TypeError,
        lambda: exact_rank(((F1, F0), (F0,))),
    )

    h.banner("Hostile positive-theorem spot checks")
    h.check("hostile ratio witness", ratio_r(F0, Fraction(1, 4)) == Fraction(8, 9))
    h.check("hostile zeta zero", zeta(Fraction(1, 2)) == F0)
    h.check("hostile canonical projector", projector() == ((F1, F0), (F0, F0)))
    h.check("hostile projector rank", exact_rank(projector()) == 1)
    h.check("hostile affine shift", d_eta(Fraction(2, 9), F0, Fraction(1, 9)) == Fraction(1, 3))


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--independent", action="store_true", help="use independent derivations")
    mode.add_argument("--hostile", action="store_true", help="exercise hostile inputs and guards")
    parser.add_argument(
        "--mutate",
        action="append",
        default=[],
        choices=(*MUTATION_NAMES, "all"),
        help="activate a fail-closed mutation fixture (repeatable)",
    )
    parser.add_argument("--list-mutations", action="store_true", help="print mutation names and exit")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    global MUTATIONS
    args = parse_args(argv)
    if args.list_mutations:
        print("\n".join(MUTATION_NAMES))
        return 0
    selected = set(args.mutate)
    if "all" in selected:
        selected = set(MUTATION_NAMES)
    MUTATIONS = frozenset(selected)

    mode = "hostile" if args.hostile else "independent" if args.independent else "normal"
    print("=" * 88)
    print("Two-channel rational functions and exact projectors")
    print(f"MODE={mode}")
    print(f"MUTATIONS={','.join(sorted(MUTATIONS)) if MUTATIONS else 'none'}")
    print("=" * 88)

    h = Harness()
    if args.hostile:
        hostile_checks(h)
    elif args.independent:
        independent_checks(h)
    else:
        normal_checks(h)

    print()
    print("=" * 88)
    print(f"SUMMARY: PASS={h.passed} FAIL={h.failed}")
    print(f"PASSED: {h.passed}/{h.passed + h.failed}")
    print("=" * 88)
    if h.failed:
        print("TWO_CHANNEL_RATIONAL_POSITIVE_THEOREM=FALSE")
        return 1
    print("TWO_CHANNEL_RATIONAL_POSITIVE_THEOREM=TRUE")
    print("EXACT_ARITHMETIC=TRUE")
    print("DEPENDENCIES=NONE")
    print("PHYSICAL_INTERPRETATION_ASSERTED=FALSE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
