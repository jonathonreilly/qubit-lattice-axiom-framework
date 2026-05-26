# Koide Quartic-Ansatz Algebra Bounded Certificate

**Date:** 2026-04-22; narrowed 2026-05-26
**Claim type:** bounded_theorem
**Status:** bounded support theorem. This row is narrowed to the exact algebra
of an admitted quartic ansatz; it is not a derivation of that ansatz from the
framework.
**Runner:** [`scripts/frontier_koide_a1_ansatz_algebra_certificate.py`](../scripts/frontier_koide_a1_ansatz_algebra_certificate.py)

## Purpose

The prior "final status" packet mixed a broad Koide investigation summary with
one exact algebraic fact. This repair keeps only the auditable fact:

```text
tr(Phi) = 3a,
tr(Phi^2) = 3a^2 + 6r^2,
V0(Phi) = 2 tr(Phi)^2 - 3 tr(Phi^2) = 9(a^2 - 2r^2),
V(Phi) = V0(Phi)^2 = 81(a^2 - 2r^2)^2.
```

Here `r = |b|` is a formal nonnegative variable. The quartic `V(Phi)` is an
input ansatz for this certificate.

## Bounded Claim

Given the formal trace data above and the ansatz
`V(Phi) := [2 tr(Phi)^2 - 3 tr(Phi^2)]^2`:

1. `V(Phi) = 81(a^2 - 2r^2)^2`.
2. `V(Phi) >= 0` as a square.
3. `V(Phi) = 0` is exactly the formal surface `a^2 = 2r^2`.
4. On `a > 0`, this is equivalently `r/a = 1/sqrt(2)`.
5. If the Brannen parameter is defined as `c := 2r/a`, then the zero-locus
   gives `c^2 = 2` and the formal expression `Q := 1/3 + c^2/6` gives
   `Q = 2/3`.

These statements are exact algebraic consequences of the declared ansatz and
definitions. They do not identify a physical charged-lepton packet.

## Boundary

This row does not claim:

- a derivation of the quartic ansatz from the minimal axiom surface;
- a derivation of the charged-lepton Koide relation from the framework;
- a derivation of Standard Model Yukawa structure;
- a physical mass-spectrum theorem;
- closure of the Brannen phase, quartic-potential primitive, or charged-lepton
  package;
- any new axiom or audit verdict.

Downstream use of this row must carry the ansatz premise explicitly. Removing
that premise remains separate science work.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_a1_ansatz_algebra_certificate.py
```
