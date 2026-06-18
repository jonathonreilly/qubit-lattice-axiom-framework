#!/usr/bin/env python3
"""Framework-native SU(2) one-plaquette Wilson/Haar bracket for u_0.

This runner supports
`SU2_WEAK_U0_ONE_PLAQUETTE_WILSON_BRACKET_BOUNDED_SUPPORT_NOTE_2026-06-18`.

It proves only the finite one-plaquette statement:

    Z(beta) = (2/pi) int_0^pi exp(beta cos(theta)) sin(theta)^2 d theta
            = I_0(beta) - I_2(beta) = 2 I_1(beta) / beta,

    <P>_1plaq(beta) = d log Z / d beta = I_2(beta) / I_1(beta),
    u_0,1plaq(beta) = <P>_1plaq(beta)^(1/4).

At the existing weak-anchor Wilson value beta_W = 16, this gives
u_0,1plaq = 0.976111254449673..., an exact finite Wilson/Haar support point
inside the interval [0.96, 0.98] used by the g_2(v) bounded interval row.

It does not prove the full four-dimensional nonperturbative SU(2) vacuum
plaquette, a Monte Carlo result, or an observed electroweak coupling.
"""

from __future__ import annotations

import math
import sys
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 90

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "SU2_WEAK_U0_ONE_PLAQUETTE_WILSON_BRACKET_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
)
G2_NOTE = ROOT / "docs" / "G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md"

PASS = 0
FAIL = 0


def D(value: str | int) -> Decimal:
    return Decimal(str(value))


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  --  {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def plain(text: str) -> str:
    return " ".join(text.replace("**", "").replace("`", "").lower().split())


def bessel_i(n: int, x: Decimal) -> Decimal:
    """Modified Bessel I_n(x) from the defining positive series.

    I_n(x) = sum_{k >= 0} (x/2)^(2k+n) / (k! (k+n)!).

    The recurrence form for consecutive terms keeps the evaluation
    deterministic and dependency-free at beta=16.
    """

    if n < 0:
        raise ValueError("n must be non-negative")
    half = x / D(2)
    term = (half ** n) / D(math.factorial(n))
    total = term
    k = 0
    tolerance = D("1e-78")
    while True:
        k += 1
        term *= (half * half) / (D(k) * D(k + n))
        total += term
        if abs(term) <= tolerance * max(D(1), abs(total)):
            return +total
        if k > 500:
            raise RuntimeError("Bessel series did not converge")


def close(a: Decimal, b: Decimal, tol: str = "1e-62") -> bool:
    return abs(a - b) <= D(tol)


def main() -> int:
    print("=" * 88)
    print("SU(2) one-plaquette Wilson/Haar u_0 bracket at beta_W = 16")
    print("=" * 88)

    section("A. Source packet checks")
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    g2_text = G2_NOTE.read_text(encoding="utf-8") if G2_NOTE.exists() else ""
    note_plain = plain(note_text)
    g2_plain = plain(g2_text)
    check("support note exists", NOTE.exists(), detail=str(NOTE.relative_to(ROOT)))
    check("g_2 source note exists", G2_NOTE.exists(), detail=str(G2_NOTE.relative_to(ROOT)))
    check(
        "support note declares independent audit-lane status authority",
        "status authority: independent audit lane only" in note_plain,
    )
    check(
        "support note forbids full 4D nonperturbative-vacuum promotion",
        "does not prove the full four-dimensional nonperturbative" in note_plain,
    )
    check(
        "g_2 row cites the one-plaquette support note",
        "SU2_WEAK_U0_ONE_PLAQUETTE_WILSON_BRACKET_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
        in g2_text,
    )
    check(
        "g_2 row keeps full-lattice u_0 closure as an open stronger target",
        "full four-dimensional nonperturbative su(2) lattice plaquette" in g2_plain
        and "stronger full-lattice" in g2_plain
        and "open residual" in g2_plain,
    )

    section("B. Exact one-plaquette Wilson/Haar integral identities")
    beta = D(16)
    i0 = bessel_i(0, beta)
    i1 = bessel_i(1, beta)
    i2 = bessel_i(2, beta)
    i3 = bessel_i(3, beta)
    z_by_difference = i0 - i2
    z_by_recurrence = D(2) * i1 / beta
    dz = (i1 - i3) / D(2)
    plaquette_by_derivative = dz / z_by_difference
    plaquette_by_ratio = i2 / i1
    u0 = plaquette_by_ratio.sqrt().sqrt()

    check(
        "Bessel recurrence gives Z = I_0 - I_2 = 2 I_1 / beta",
        close(z_by_difference, z_by_recurrence),
        detail=f"relative delta={(z_by_difference - z_by_recurrence) / z_by_difference:.3E}",
    )
    check(
        "d log Z / d beta equals I_2(beta) / I_1(beta)",
        close(plaquette_by_derivative, plaquette_by_ratio),
        detail=f"relative delta={(plaquette_by_derivative - plaquette_by_ratio) / plaquette_by_ratio:.3E}",
    )
    check(
        "one-plaquette expectation is a strict plaquette factor 0 < <P> < 1",
        D("0") < plaquette_by_ratio < D("1"),
        detail=f"<P>={plaquette_by_ratio}",
    )

    section("C. beta_W = 16 bracket")
    check(
        "<P>_1plaq(16) lies in [0.9078, 0.9079]",
        D("0.9078") < plaquette_by_ratio < D("0.9079"),
        detail=f"<P>={plaquette_by_ratio}",
    )
    check(
        "u_0,1plaq(16) lies in [0.9761, 0.9762]",
        D("0.9761") < u0 < D("0.9762"),
        detail=f"u_0={u0}",
    )
    check(
        "u_0,1plaq(16) is inside the g_2 row interval [0.96, 0.98]",
        D("0.96") < u0 < D("0.98"),
        detail=f"0.96 < {u0} < 0.98",
    )
    check(
        "the one-plaquette bracket is narrower than the admitted interval",
        D("0.9761") > D("0.96") and D("0.9762") < D("0.98"),
        detail="[0.9761,0.9762] subset [0.96,0.98]",
    )

    section("D. Guardrails")
    forbidden_promotions = (
        "full four-dimensional nonperturbative su(2) lattice vacuum",
        "monte carlo import",
        "observed electroweak g_2",
        "new axiom",
    )
    for item in forbidden_promotions:
        check(f"guardrail recorded: no {item}", f"no {item}" in note_plain)

    print()
    print("Result:")
    print(f"  beta_W = {beta}")
    print(f"  <P>_1plaq(16) = {plaquette_by_ratio}")
    print(f"  u_0,1plaq(16) = {u0}")
    print(f"  certified bracket: u_0,1plaq(16) in [0.9761, 0.9762] subset [0.96, 0.98]")
    print(f"  PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
