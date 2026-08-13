---
claim_id: three_qubit_c8_carries_y0_cubic_cancel_still_extra_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "A single 3-qubit Hilbert H=(C^2)^{otimes 3} congruent to C^8 can host the stipulated block-scalar operator Y_0=Pi_+-3 Pi_-, and then dim H=8 with exact integer cubic trace Tr(Y_0^3)=6-54=-48 nonzero. The complementary copy on H oplus H with Y_oplus=Y_0 oplus (-Y_0) cancels the cubic and has dimension 16. One 3-qubit Hilbert matches only the first C^8 dimension; it does not supply the complementary copy or force Tr(Y^3)=0. The current Qubit axiom names one-site M_2(C) and names neither Y_0 nor a second C^8. No generation axiom is adopted. The result is independent of the dim-16-versus-one-site-C^2 comparison and of the Hilbert-versus-M_3 comparison."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_qubit_c8_carries_y0_cubic_cancel_still_extra_2026_08_13.py
---

# Three-Qubit C^8 Can Carry Y_0; Cubic Cancel Still Needs a Second 8

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact integer traces of a stipulated block-scalar operator on one
3-qubit Hilbert and on a complementary direct sum; no charge naming.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_qubit_c8_carries_y0_cubic_cancel_still_extra_2026_08_13.py`](../scripts/three_qubit_c8_carries_y0_cubic_cancel_still_extra_2026_08_13.py)

No runner cache is written in this dispatch.

## Result Up Front

Identify the 3-qubit Hilbert space

`H = (C^2)^{⊗3} ≅ C^8`.

In a fixed orthonormal basis of `H`, write the complementary projectors

`Pi_+ = diag(I_6, 0_2)`, `Pi_- = diag(0_6, I_2)`

and the stipulated block-scalar operator

`Y_0 = Pi_+ − 3 Pi_-`.

Then `dim H = 8` and the cubic trace reconstructs exactly as

`Tr(Y_0^3) = 6(1)^3 + 2(−3)^3 = 6 − 54 = −48 ≠ 0`.

So one 3-qubit Hilbert can carry `Y_0`. It does not cancel the cubic.

On the extra matching `H ⊕ H` with

`Y_⊕ = Y_0 ⊕ (−Y_0)`,

one has `dim(H ⊕ H) = 16` and

`Tr(Y_⊕^3) = −48 + 48 = 0`.

The complementary copy is not supplied by the first `C^8`. The current Qubit
axiom names one-site `M_2(C)` and names neither `Y_0` nor a second `C^8`. This
note does not adopt a generation axiom.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer traces and dimensions are proved for a stipulated Y_0 on one 3-qubit Hilbert and for the complementary direct-sum matching; the axioms do not name Y_0 or a second C^8, and no generation axiom is adopted."
trace_class: negative_route_pruning
target_claim_id: three_qubit_c8_carries_y0_cubic_cancel_still_extra
target_blocker_text: "Tr(Y^3)=0 matching is not supplied by having one 3-qubit Hilbert"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the stipulated Y_0 on C^8 and for the extra H oplus H matching; physical derivation of Y_0 and of the complementary copy remains open"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim; no generation axiom"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `C^2` be the one-qubit Hilbert space of complex dimension 2. The 3-qubit
tensor product is the Hilbert space

`H = (C^2) ⊗ (C^2) ⊗ (C^2)`.

Its complex dimension is `2^3 = 8`, so there is a linear isomorphism
`H ≅ C^8`. All traces below are exact integer traces of operators on these
finite-dimensional complex vector spaces.

Fix an orthonormal basis of `H` in which the complementary projectors are
diagonal as stipulated:

`Pi_+ = diag(I_6, 0_2)`, `Pi_- = diag(0_6, I_2)`.

These are orthogonal complementary projectors of ranks 6 and 2:

`Pi_+^2 = Pi_+`, `Pi_-^2 = Pi_-`, `Pi_+ Pi_- = 0`, `Pi_+ + Pi_- = I_8`.

The stipulated operator is the integer combination

`Y_0 = Pi_+ − 3 Pi_- = diag(I_6, −3 I_2)`.

Its spectrum is `+1` with multiplicity 6 and `−3` with multiplicity 2. No
species name, charge table, or observational identification is attached to
these eigenvalues.

The complementary matching, when extra-supplied, is the direct sum
`H ⊕ H` of complex dimension 16 together with

`Y_⊕ = Y_0 ⊕ (−Y_0)`.

## Theorem 1

**Theorem 1.** `dim H = 8` and `Tr(Y_0^3) = −48 ≠ 0`.

**Proof.** Dimension: `dim H = 2^3 = 8`. For the cubic, the spectrum of `Y_0`
gives the exact integer identity

`Tr(Y_0^3) = 6 (1)^3 + 2 (−3)^3 = 6 + 2(−27) = 6 − 54 = −48`.

The same value is the matrix trace of the integer cube `Y_0^3`. In particular
`Tr(Y_0^3) ≠ 0`.

## Theorem 2

**Theorem 2.** On `H ⊕ H` with `Y_⊕ = Y_0 ⊕ (−Y_0)`,

`Tr(Y_⊕^3) = −48 + 48 = 0` and `dim = 16`.

**Proof.** Dimension: `dim(H ⊕ H) = 8 + 8 = 16`. Cubing a direct sum is the
direct sum of the cubes, and `(−Y_0)^3 = − Y_0^3`, so

`Tr(Y_⊕^3) = Tr(Y_0^3) + Tr((−Y_0)^3) = −48 + (−(−48)) = −48 + 48 = 0`.

## Theorem 3

**Theorem 3.** One 3-qubit Hilbert matches the *dimension* of the first
`C^8`. It does not supply the complementary copy or force `Tr(Y^3)=0`.
The cancel is an extra matching.

**Proof.** Theorem 1 already computes `dim H = 8` and `Tr(Y_0^3) = −48 ≠ 0` on
that single copy. The object that cancels the cubic in Theorem 2 is a second,
independently supplied `C^8` together with the sign-reversed operator. Nothing
in the construction of `H = (C^2)^{⊗3}` produces that second summand or
forces the cubic trace to vanish. Therefore `Tr(Y^3)=0` matching is not
supplied by having one 3-qubit Hilbert.

## Theorem 4

**Theorem 4.** The current Qubit axiom names a one-site algebraic presentation
`M_2(C)`. Neither `Y_0` nor a second `C^8` is named. This note does not adopt
a generation axiom.

**Quoted current Qubit wording** (from
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)):

> Each site has a domain of local possibilities.
>
> The full one-site possibility domain has algebraic presentation `M_2(C)`.
>
> A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
> adds no further primitive structure.

That wording names one-site `M_2(C)`. It does not name a 3-qubit Hilbert, the
operator `Y_0`, a complementary `C^8`, or a generation count. Qualification in
the same memo states that further physical structure requires a retained
derivation or bridge, or explicit approved-primitive registration, before use
as a premise. This note therefore treats `Y_0` and the second `C^8` as
stipulated extra matching, not as axiom content, and it does not adopt a
generation axiom.

## Hostile Mutations

Two predicates that would collapse the hole are false on the objects above.

1. The predicate `Tr(Y_0^3) == 0` fails: Theorem 1 gives `−48 ≠ 0`.
2. The predicate `dim(H ⊕ H) == 8` fails: Theorem 2 gives dimension 16.

## What This Note Does Not Claim

- It does not identify `Y_0` with a physical charge, a `U(1)` gauge generator,
  or any observational particle-data table.
- It does not derive `Y_0` or the complementary copy from the four axioms.
- It does not adopt a generation axiom, a second Hilbert as axiom content, or
  any edit of the Qubit wording.
- It is independent of the comparison of dimension 16 with one-site `C^2`,
  and independent of the comparison of a Hilbert space with `M_3`. Those are
  separate holes; this hole is only that `Tr(Y^3)=0` matching is not supplied
  by having one 3-qubit Hilbert.

Parents on `origin/main` are the axiom memo only.
