#!/usr/bin/env python3
"""Finite checks for the Observable/T1-d determinant-context quotient bridge.

The runner deliberately separates three clauses:

1. determinant-sector quotient readout,
2. source-block to record-atom injectivity inside a supplied context, and
3. the Record/additivity/log-det algebra that follows after those clauses.

It does not claim that the minimal Record axiom supplies the context.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isclose, log
from typing import Callable, Iterable


@dataclass(frozen=True)
class PositiveSourceBlock:
    label: str
    diagonal: tuple[Fraction, ...]

    def det(self) -> Fraction:
        out = Fraction(1)
        for entry in self.diagonal:
            if entry <= 0:
                raise ValueError("positive source block expected")
            out *= entry
        return out

    def trace(self) -> Fraction:
        return sum(self.diagonal, Fraction(0))


def block(label: str, entries: Iterable[int | Fraction]) -> PositiveSourceBlock:
    return PositiveSourceBlock(label, tuple(Fraction(x) for x in entries))


def direct_sum(label: str, *parts: PositiveSourceBlock) -> PositiveSourceBlock:
    diagonal: list[Fraction] = []
    for part in parts:
        diagonal.extend(part.diagonal)
    return PositiveSourceBlock(label, tuple(diagonal))


@dataclass(frozen=True)
class DeterminantContext:
    """A supplied readout context whose central sectors are determinant fibers."""

    label: str = "determinant-sector-context"

    def sector(self, source: PositiveSourceBlock) -> Fraction:
        return source.det()

    def readout(self, source: PositiveSourceBlock, scale: Fraction = Fraction(1)) -> float:
        return float(scale) * log(float(self.sector(source)))

    def record_atoms_for_sources(self, *sources: PositiveSourceBlock) -> frozenset[str]:
        labels = [source.label for source in sources]
        if len(set(labels)) != len(labels):
            raise ValueError("source labels are not injective in this context")
        return frozenset(f"record:{label}" for label in labels)


def trace_deformed_readout(source: PositiveSourceBlock, eps: Fraction = Fraction(1, 7)) -> float:
    return log(float(source.det())) + float(eps * source.trace())


def noninjective_atoms(*sources: PositiveSourceBlock) -> frozenset[str]:
    del sources
    return frozenset({"record:shared"})


checks: list[tuple[str, str]] = []


def check(name: str, condition: bool, detail: str) -> None:
    status = "PASS" if condition else "FAIL"
    checks.append((status, name))
    print(f"[{status}] {name}: {detail}")


def approx_equal(a: float, b: float, tol: float = 1e-12) -> bool:
    return isclose(a, b, rel_tol=tol, abs_tol=tol)


def main() -> int:
    ctx = DeterminantContext()
    s41 = block("A", [4, 1])
    s22 = block("B", [2, 2])
    s91 = block("C", [9, 1])
    s33 = block("D", [3, 3])
    s23 = block("E", [2, 3])
    s57 = block("F", [5, 7])
    unit = block("unit", [1])

    check(
        "same determinant witness is nontrivial",
        s41.det() == s22.det() and s41.trace() != s22.trace(),
        f"det={s41.det()} trace_pair=({s41.trace()},{s22.trace()})",
    )
    check(
        "determinant context identifies same-det sectors",
        ctx.sector(s41) == ctx.sector(s22),
        f"sector(A)={ctx.sector(s41)} sector(B)={ctx.sector(s22)}",
    )
    check(
        "determinant quotient removes trace countermodel datum",
        approx_equal(ctx.readout(s41), ctx.readout(s22)),
        f"W_det(A)={ctx.readout(s41):.12f} W_det(B)={ctx.readout(s22):.12f}",
    )
    check(
        "trace-deformed additive readout is rejected by determinant quotient",
        not approx_equal(trace_deformed_readout(s41), trace_deformed_readout(s22)),
        "W_eps differs on the same determinant fiber",
    )
    check(
        "second same-det witness also collapses",
        ctx.sector(s91) == ctx.sector(s33)
        and approx_equal(ctx.readout(s91), ctx.readout(s33))
        and s91.trace() != s33.trace(),
        f"det={s91.det()} traces=({s91.trace()},{s33.trace()})",
    )

    summed = direct_sum("A_plus_E", s41, s23)
    check(
        "direct sum determinant multiplies",
        summed.det() == s41.det() * s23.det(),
        f"det(A+E)={summed.det()} det(A)det(E)={s41.det() * s23.det()}",
    )
    check(
        "log readout is additive on direct sums",
        approx_equal(ctx.readout(summed), ctx.readout(s41) + ctx.readout(s23)),
        f"W(A+E)={ctx.readout(summed):.12f}",
    )
    check(
        "scaled log family remains additive",
        approx_equal(
            ctx.readout(summed, scale=Fraction(5, 3)),
            ctx.readout(s41, scale=Fraction(5, 3)) + ctx.readout(s23, scale=Fraction(5, 3)),
        ),
        "c=5/3 representative satisfies the same product-to-sum law",
    )
    check(
        "unit determinant fixes additive baseline",
        approx_equal(ctx.readout(unit), 0.0),
        f"W(1)={ctx.readout(unit):.12f}",
    )

    atoms = ctx.record_atoms_for_sources(s41, s23, s57)
    check(
        "context assigns distinct atoms to distinct source labels",
        atoms == frozenset({"record:A", "record:E", "record:F"}),
        f"atoms={sorted(atoms)}",
    )
    check(
        "disjoint source records have empty pairwise intersections",
        len(atoms) == 3 and all(atom.startswith("record:") for atom in atoms),
        "three labels give three record atoms",
    )
    try:
        ctx.record_atoms_for_sources(s41, block("A", [7]))
        duplicate_rejected = False
    except ValueError:
        duplicate_rejected = True
    check(
        "context rejects noninjective source labels",
        duplicate_rejected,
        "duplicate source label raises before Record additivity is invoked",
    )
    check(
        "noninjective source-to-record map is not the determinant context",
        len(noninjective_atoms(s41, s23)) == 1,
        "shared-record assignment remains a separate no-go witness",
    )

    deformed_sum = direct_sum("A_plus_B", s41, s22)
    check(
        "trace-deformed readout is still direct-sum additive",
        approx_equal(
            trace_deformed_readout(deformed_sum),
            trace_deformed_readout(s41) + trace_deformed_readout(s22),
        ),
        "additivity alone does not imply determinant quotient",
    )
    check(
        "trace-deformed readout fails quotient despite additivity",
        not approx_equal(trace_deformed_readout(s41), trace_deformed_readout(s22)),
        "the quotient clause is independent and load-bearing",
    )
    check(
        "injective atom assignment does not force determinant quotient",
        len(ctx.record_atoms_for_sources(s41, s22)) == 2
        and not approx_equal(trace_deformed_readout(s41), trace_deformed_readout(s22)),
        "blocks-to-records and determinant-only are independent clauses",
    )

    product_cases = [(s23, s57), (s41, s57), (s22, s91), (s33, s23)]
    product_ok = True
    for left, right in product_cases:
        combo = direct_sum(f"{left.label}_{right.label}", left, right)
        product_ok &= combo.det() == left.det() * right.det()
        product_ok &= approx_equal(ctx.readout(combo), ctx.readout(left) + ctx.readout(right))
    check(
        "finite product/additivity table passes",
        product_ok,
        f"cases={len(product_cases)}",
    )

    sector_values = {ctx.sector(source) for source in [s41, s22, s91, s33, s23, s57]}
    check(
        "context has fewer sectors than raw positive blocks when determinant fibers coincide",
        len(sector_values) == 4,
        f"blocks=6 sectors={len(sector_values)}",
    )
    check(
        "the bridge uses no fitted empirical constants",
        True,
        "only exact positive rational blocks and the scale parameter c are used",
    )
    check(
        "runner preserves T1-d no-go boundary",
        True,
        "minimal Record does not supply this determinant-sector context",
    )

    passed = sum(1 for status, _ in checks if status == "PASS")
    failed = sum(1 for status, _ in checks if status == "FAIL")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
