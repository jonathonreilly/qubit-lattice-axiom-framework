#!/usr/bin/env python3
"""Wilson generator-rescaling beta bookkeeping.

This runner verifies the bounded algebraic convention map in
docs/WILSON_GENERATOR_RESCALING_BETA_BOOKKEEPING_BOUNDED_NOTE_2026-06-17.md.

It does not derive the Wilson action surface, beta=6, or g_bare=1, and it does
not apply an audit verdict.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "WILSON_GENERATOR_RESCALING_BETA_BOOKKEEPING_BOUNDED_NOTE_2026-06-17.md"
GBARE_NOTE = ROOT / "docs" / "G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")
    return ok


def q_coeff(beta: Fraction, g_sq: Fraction, kappa: Fraction, n: int = 3) -> Fraction:
    """Wilson small-plaquette quadratic coefficient up to common geometry."""
    return beta * g_sq * kappa / n


def beta_match(g_sq: Fraction, kappa: Fraction, n: int = 3) -> Fraction:
    """General trace-metric Wilson matching beta = N/(kappa g^2)."""
    return Fraction(n, 1) / (kappa * g_sq)


def main() -> int:
    print("Wilson generator-rescaling beta bookkeeping")
    print("=" * 72)
    print("Claim boundary: exact convention bookkeeping only; no audit verdict.")

    note = NOTE.read_text(encoding="utf-8")
    gbare = GBARE_NOTE.read_text(encoding="utf-8")

    kappa0 = Fraction(1, 2)
    beta0 = Fraction(6, 1)
    g_sq0 = Fraction(1, 1)
    n = 3
    q0 = q_coeff(beta0, g_sq0, kappa0, n)

    check("canonical beta formula beta=N/(kappa g^2) gives beta=6 for N=3,kappa=1/2,g^2=1",
          beta_match(g_sq0, kappa0, n) == beta0)
    check("canonical quadratic coefficient is finite positive",
          q0 == Fraction(1, 1), f"Q0={q0}")

    samples = [Fraction(1, 4), Fraction(2), Fraction(4), Fraction(9)]
    for c_sq in samples:
        kappa_new = c_sq * kappa0
        check(
            f"trace metric scales by c^2={c_sq}",
            kappa_new == c_sq * kappa0,
            f"kappa_new={kappa_new}",
        )

        fixed_component_q = q_coeff(beta0, g_sq0, kappa_new, n)
        check(
            f"fixed beta,g components scale Q by c^2={c_sq}",
            fixed_component_q == c_sq * q0,
            f"Q_new/Q_old={fixed_component_q / q0}",
        )

        beta_fixed_component = beta0 / c_sq
        q_rematched = q_coeff(beta_fixed_component, g_sq0, kappa_new, n)
        check(
            f"fixed-component rematch has beta_new/beta_old=1/c^2 for c^2={c_sq}",
            q_rematched == q0,
            f"beta_new/beta_old={beta_fixed_component / beta0}",
        )

        # Holding the Lie-algebra exponent fixed under T' = c T means the
        # coupling coordinate scales as g_new = g_old / c, so g_new^2 = g^2/c^2.
        g_sq_exponent_fixed = g_sq0 / c_sq
        q_exponent_fixed = q_coeff(beta0, g_sq_exponent_fixed, kappa_new, n)
        check(
            f"fixed-exponent convention leaves Q unchanged at same beta for c^2={c_sq}",
            q_exponent_fixed == q0,
            f"g_new^2={g_sq_exponent_fixed}",
        )

        beta_canonical_old = beta_match(g_sq0, kappa0, n)
        beta_canonical_new = beta_match(g_sq_exponent_fixed, kappa0, n)
        check(
            f"re-canonicalized coupling report gives beta_ratio=c^2 for c^2={c_sq}",
            beta_canonical_new / beta_canonical_old == c_sq,
            f"ratio={beta_canonical_new / beta_canonical_old}",
        )

    flat = " ".join(note.split())
    check("note states no single convention-free beta law",
          "There is no single convention-free `beta_new / beta_old` law" in note)
    check("note states fixed-component ratio",
          "beta_new / beta_old = 1 / c^2" in note)
    check("note states re-canonicalized coordinate ratio",
          "beta_canonical(g_new) / beta_canonical(g_old) = c^2" in note)
    check("note forbids beta=6 derivation",
          "does not derive or audit `beta = 6`" in note or "derive or audit `beta = 6`" in note)
    check("note forbids g_bare=1 derivation",
          "does not prove `g_bare = 1`" in flat
          or "does not prove `g_bare=1`" in flat
          or "- derive `g_bare = 1`" in note)
    check("note forbids audit status edit",
          "does not retag any ledger row" in flat and "does not set or predict an audit outcome" in flat)
    check("g_bare rescaling note links this companion",
          "WILSON_GENERATOR_RESCALING_BETA_BOOKKEEPING_BOUNDED_NOTE_2026-06-17.md" in gbare)

    print("=" * 72)
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
