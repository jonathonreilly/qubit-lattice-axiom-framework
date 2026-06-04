# Frobenius-Schur Chiral/Vector Mode Count for the Koide r Candidate Route (Open Gate)

**Date:** 2026-06-04
**Type:** open_gate
**Claim type:** open_gate (conditional algebra companion).
**Claim scope:** On the finite C3 generation-triplet split with
`E_singlet = 3a^2` and `E_doublet = 6|b|^2`, the Frobenius-Schur
indicators distinguish the real singlet parameter `a` from the complex
doublet parameter `b`. A vector/real readout counts `(Re b, Im b)` as
two doublet modes and gives `(1,2) -> r = 1`; a holomorphic/chiral
readout counts `b` once and gives `(1,1) -> r = 1/2`. This refines the
landed [holomorphic supertrace open gate](SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md)
by making the real/complex Frobenius-Schur asymmetry explicit.
**actual_current_surface_status:** open gate. The paired runner verifies
the finite C3 Frobenius-Schur indicators, the vector/chiral weighting
map, and the uniform-rescaling objection. It does not select the chiral
readout, does not derive Koide `r = 1/2`, and does not promote any
status.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_koide_r_reduces_to_chiral_vs_vector_yukawa_binary_exact.py`](./../scripts/audit_companion_koide_r_reduces_to_chiral_vs_vector_yukawa_binary_exact.py)
**Runner cache:** [`logs/runner-cache/audit_companion_koide_r_reduces_to_chiral_vs_vector_yukawa_binary_exact.txt`](./../logs/runner-cache/audit_companion_koide_r_reduces_to_chiral_vs_vector_yukawa_binary_exact.txt)

## Context

The parent [holomorphic supertrace open gate](SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md)
records a candidate route: a chiral/holomorphic readout of the
generation fluctuation would count the complex doublet coefficient `b`
once, while the vector/real readout counts `Re b` and `Im b`
separately. This companion checks the finite C3 representation-theory
reason the singlet is not similarly halved: the trivial isotype is
Frobenius-Schur real, while the nontrivial conjugate pair is
Frobenius-Schur complex.

So the natural objection is answered narrowly:

- a uniform "complex-mode count" rescales `(1,2)` to `(1/2,1)`, which is
  proportional to `(1,2)` and still gives `r = 1`;
- the `(1,1)` candidate needs the asymmetric FS fact that `a` remains a
  real singlet mode while only the complex doublet changes from two real
  modes to one holomorphic mode.

This is an algebraic refinement of the open gate, not a proof that the
framework's mass/Yukawa fluctuation determinant is chiral.

## Statement

1. (**Frobenius-Schur types**) For C3,
   `FS(rho) = (1/|G|) sum_g chi_rho(g^2)`. The trivial irrep has
   `FS = +1` (real type). The `omega` and `omega-bar` irreps have
   `FS = 0` (complex type).
2. (**mode counts**) The trivial-isotype coefficient `a` is
   self-conjugate and contributes one real fluctuation mode in both the
   vector and chiral cases. The conjugate-pair doublet coefficient `b`
   contributes two real modes under a vector readout and one
   holomorphic mode under a chiral readout.
3. (**weighting map**) With `E_singlet = 3a^2`,
   `E_doublet = 6|b|^2`, and weights `(w_s, w_d)`, the singlet energy
   fraction is `x = w_s/(w_s+w_d)` and
   `r = (1-x)/(2x)`. Thus `(1,2) -> r = 1` and `(1,1) -> r = 1/2`.
4. (**uniform rescaling objection**) Uniform complex counting gives
   `(1/2,1)`, proportional to `(1,2)`, so it still gives `r = 1`. The
   chiral candidate is not a uniform rescaling; it is the asymmetric
   real/complex FS split.

All runner checks are exact symbolic checks.

## What Is Not Claimed

- This note does not select the chiral/holomorphic readout. The
  staggered-Dirac mass/Yukawa realization remains the gate.
- This note does not derive `r = 1/2`; it only states the condition under
  which the parent open gate would produce `(1,1)`.
- This note does not use PDG values, observed lepton masses, empirical
  Koide matching, or a new axiom/primitive.
- The [Lattice + Quantum + Record baseline](MINIMAL_AXIOMS_2026-06-04.md)
  does not decide this readout choice.

## Trace Gate

```yaml
trace_class: open_gate
target_blocker_text: "BAE admission |b|^2/a^2=1/2 (r=1/2) on the charged-lepton lane"
source_of_blocker_text: audit_ledger
reachability_to_target: candidate_condition
artifact_role: open_gate
next_trace_action: "evaluate the gated bit: compute the generation Yukawa fluctuation determinant on the hw=1 corners with the staggered-Dirac mass and determine whether it is chiral/holomorphic (b once -> r=1/2) or vector/real (Re b, Im b separately -> r=1)."
```

## Forbidden Imports

- The Frobenius-Schur indicators and C3 characters are computed in the
  runner.
- The isotype energy form is inherited from
  [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md).
- Literature on FS indicators, chiral determinants, or staggered
  fermions is comparator context only.

## Cross-References

- [Holomorphic supertrace open gate](SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md)
  - parent candidate route refined by this companion.
- [Multi-factor companion](MULTIFACTOR_CONNES_LOTT_PURCHASES_NOT_DERIVES_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
  - explains why C3-trivial extra factors preserve the vector `(1,2)`
  weighting.
- [Koide kappa Frobenius-measure theorem](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md)
  - source for the `E_singlet = 3a^2`, `E_doublet = 6|b|^2` energy form.
