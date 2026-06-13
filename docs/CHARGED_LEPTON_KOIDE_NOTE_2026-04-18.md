# Charged-Lepton Koide Two-Gate Open Certificate

**Date:** 2026-04-18; narrowed 2026-05-26
**Claim type:** open_gate
**Status:** open gate. This row is a finite certificate of the two remaining
charged-lepton Koide gates, not a derivation of the physical charged-lepton
ratios.
**Runner:** [`scripts/frontier_charged_lepton_koide_two_gate_open_certificate.py`](../scripts/frontier_charged_lepton_koide_two_gate_open_certificate.py)
(TOTAL: PASS=25 FAIL=0; cached:
[`logs/runner-cache/frontier_charged_lepton_koide_two_gate_open_certificate.txt`](../logs/runner-cache/frontier_charged_lepton_koide_two_gate_open_certificate.txt))

## Purpose

The prior packet summarized a long charged-lepton Koide campaign. Its durable
science is not a closure theorem. The durable result is sharper:

1. the formal Koide algebra has a small exact target surface;
2. the physical charged-lepton package is still missing exactly the bridge
   that selects that surface from the framework.

This note keeps the finite open-gate statement and removes package-level
closure language.

## 2026-06-13 Tier-A Bounded-Consumer Split

The later Tier-A row
`CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md`
supplies a bounded consumer of the Brannen-BAE algebra under explicit
Tier-A admission of the `AC_phi_lambda` phase/amplitude packet. That
bounded-admission lane does **not** close either first-principles gate
in this note. It only records what follows if the phase/amplitude inputs
are accepted at bounded tier.

Therefore this open-gate map now has two safe downstream uses:

1. as a first-principles target map for deriving `Q = 2/3` and the
   `delta = Q/3` readout without Tier-A admission; and
2. as a boundary map for bounded Tier-A consumers, which must cite the
   Tier-A bounded row and keep the admission explicit.

No downstream row may cite this note alone as a derivation of the Koide
surface, the Brannen phase, charged-lepton masses, or the absolute scale.

## Formal Algebra Kept

On the Brannen-style cyclic parameterization, take a nonzero scalar amplitude
`a > 0`, a nonnegative doublet radius `r >= 0`, and define

```text
c := 2r/a,
Q := 1/3 + c^2/6.
```

Then the target value `Q = 2/3` is equivalent to

```text
c^2 = 2
r^2/a^2 = 1/2.
```

If a separate selected-line phase bridge identifies the physical Brannen phase
by the formal rule

```text
delta := Q/3,
```

then the same target gives `delta = 2/9`.

## Open Gates

The charged-lepton package is not closed on the current surface because two
bridges remain open:

1. **Koide surface selection gate.** Derive, without fitting observed lepton
   masses, why the physical charged-lepton packet must satisfy `c^2 = 2`
   (equivalently `Q = 2/3`).
2. **Brannen phase identification gate.** Derive, without a convention-only
   period choice or observed phase pin, why the physical selected-line phase is
   the `delta = Q/3` readout and therefore equals `2/9` at the Koide target.

The formal identities above are useful because they make the missing bridges
small and checkable. They do not supply those bridges.

## Boundary

This row does not claim:

- a framework derivation of charged-lepton `Q = 2/3`;
- a framework derivation of physical `delta = 2/9`;
- a physical charged-lepton mass-spectrum theorem;
- a derivation of the overall charged-lepton scale;
- a Standard Model Yukawa theorem;
- any new axiom or audit verdict.

Downstream work may use this row only as an open-gate map. Any positive
charged-lepton Koide theorem must close both gates explicitly or state which
gate it assumes.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_charged_lepton_koide_two_gate_open_certificate.py
```
