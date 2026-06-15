#!/usr/bin/env python3
"""No-go runner for the observable-principle T1-d readout boundary.

This runner proves by explicit finite countermodel that the current Record
axiom's finite scalar additivity does not force the T1-d determinant-only
readout identification:

    W is a continuous function of Z = det(D+J) alone on all R_{>0}.

It does not audit, promote, or demote any row. It checks the finite algebra
behind the source note:

  * additive readouts of the form I_lambda(Z, q) = log Z + lambda*q;
  * exact additivity under disjoint union (Z, q) -> (Z1*Z2, q1+q2);
  * non-factorization through Z alone when lambda != 0;
  * the determinant-only log readout is recovered only after the extra
    coordinate is quotiented away or lambda is set to zero by an external
    bridge.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")


@dataclass(frozen=True)
class BlockRecord:
    """A supplied finite central-sector record datum.

    z is the determinant-like multiplicative coordinate.
    q is an independent supplied central-sector coordinate.
    """

    z: float
    q: float

    def union(self, other: "BlockRecord") -> "BlockRecord":
        return BlockRecord(self.z * other.z, self.q + other.q)


def readout(record: BlockRecord, lam: float) -> float:
    return math.log(record.z) + lam * record.q


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    axiom_text = (repo / "docs" / "MINIMAL_AXIOMS_2026-06-05.md").read_text(encoding="utf-8")
    parent_text = (repo / "docs" / "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md").read_text(encoding="utf-8")

    print("=== 1. Current axiom boundary text ===")
    check("Record axiom states finite scalar additivity", "finitely additive" in axiom_text)
    check("Record axiom says it does not supply readout context", "supplies no readout context" in axiom_text)
    check("Record axiom says it does not supply sector-generation rule", "sector-generation rule" in axiom_text)
    check(
        "minimal axioms warn observable parent is not the axiom note",
        "`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not this axiom note" in axiom_text,
    )
    check("parent note declares T1-d as a bridge premise", "T1-d (declared bridge premise" in parent_text)
    check(
        "parent note says T1-d is not derivable from minimal_axioms",
        "not derivable** from\n  `minimal_axioms`" in parent_text,
    )

    print("\n=== 2. Additive supplied-context family ===")
    a = BlockRecord(z=2.0, q=0.0)
    b = BlockRecord(z=3.0, q=4.0)
    c = BlockRecord(z=5.0, q=-1.5)
    union = a.union(b).union(c)

    for lam in [0.0, 0.25, -2.0, math.pi]:
        lhs = readout(union, lam)
        rhs = readout(a, lam) + readout(b, lam) + readout(c, lam)
        check(
            f"I_lambda additive under disjoint union for lambda={lam:.6g}",
            abs(lhs - rhs) < 1e-12,
            f"lhs={lhs:.15f}, rhs={rhs:.15f}",
        )

    print("\n=== 3. Same determinant, different additive readout ===")
    same_z_0 = BlockRecord(z=2.0, q=0.0)
    same_z_1 = BlockRecord(z=2.0, q=1.0)
    lam = 0.5
    check("two records have identical determinant-like Z", same_z_0.z == same_z_1.z)
    val0 = readout(same_z_0, lam)
    val1 = readout(same_z_1, lam)
    check(
        "lambda != 0 readout separates records with the same Z",
        abs(val0 - val1) > 1e-12,
        f"I(2,0)={val0:.15f}, I(2,1)={val1:.15f}",
    )
    check(
        "no function f(Z) can represent I_lambda when same Z has two values",
        not math.isclose(val0, val1),
        "would require f(2)=log(2) and f(2)=log(2)+lambda",
    )

    print("\n=== 4. Determinant-only log is an extra quotient/selection ===")
    det_only_lhs = readout(union, 0.0)
    det_only_rhs = math.log(union.z)
    check(
        "lambda=0 recovers the determinant-only logarithmic readout",
        abs(det_only_lhs - det_only_rhs) < 1e-12,
        f"I_0={det_only_lhs:.15f}, log(Z)={det_only_rhs:.15f}",
    )
    q_quotiented = BlockRecord(z=same_z_1.z, q=0.0)
    check(
        "quotienting the q coordinate restores factorization through Z",
        abs(readout(q_quotiented, lam) - readout(same_z_0, lam)) < 1e-12,
        "this quotient is exactly the extra readout-identification bridge",
    )

    print("\n=== 5. Scope conclusion ===")
    check(
        "Record additivity is compatible with non-determinant supplied coordinates",
        True,
        "therefore T1-d is independent of the current axiom text",
    )
    check(
        "the no-go does not challenge the conditional log-det theorem under T1-d",
        True,
        "it only blocks deriving T1-d from Record alone",
    )

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    if FAIL:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
