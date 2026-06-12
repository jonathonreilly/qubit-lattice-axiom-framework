# AC_phi_lambda hw-complement Reading Registration-Equivalence -- Bounded Theorem

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome and does not edit the audit-lane-owned Tier-A registry.
**Primary runner:**
[`scripts/frontier_acphilambda_hw_complement_reading_registration_equivalence_2026_06_12.py`](../scripts/frontier_acphilambda_hw_complement_reading_registration_equivalence_2026_06_12.py)
**Runner cache:**
[`logs/runner-cache/frontier_acphilambda_hw_complement_reading_registration_equivalence_2026_06_12.txt`](../logs/runner-cache/frontier_acphilambda_hw_complement_reading_registration_equivalence_2026_06_12.txt)

## Boundary

This note proves only that, on the supplied finite three-slot circulant slot
model, the two Hamming-complement readings have the same Record-registrable
scalar content.

Explicitly, this note:

- does not select a physical species reading;
- does not prove the choice is pure convention in the **full** dynamics
  (finite slot model only; full-dynamics complementation-equivariance remains
  the named open of the hw support note);
- does not retire `AC_phi_lambda` or any sub-admission;
- does not edit the registry;
- does not derive `r`, `delta`, or the charged-lepton value;
- no new axiom, primitive, admission, normalization, probability rule,
  comparator, or audit verdict.

## The supplied slot model

The supplied slot model used here is stipulated in-note. The corner cube is
`{0,1}^3`. The frame rotation is `R(x,y,z) = (z,x,y)`. Complementation is the
coordinatewise map `b -> 1-b` (written without a symbol to avoid collision
with the cyclic 3-shift `C` in the circulant below). The `hw=1` triplet is
`{(1,0,0), (0,1,0), (0,0,1)}` and the `hw=2` triplet is
`{(0,1,1), (1,0,1), (1,1,0)}`.

The supplied circulant class is
`H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T`, with eigenvalues
`lambda_k = a + 2B cos(delta + 2 pi k/3)`. The physical identification of this
class is carried by the `AC_phi_lambda` admission as a supplied-class pattern.
The hw support note and the staggered gate are context, not load-bearing here:
all finite slot facts used below are reproven in this note's runner.

## The theorem

> **Theorem (hw-complement reading is registration-equivalent on the supplied slot
> model).** On the supplied finite three-slot circulant model (slots x1,x2,x3 carrying
> the supplied charged-lepton circulant readout, eigenvalues
> lambda_k = a + 2B cos(delta + 2 pi k/3)), consider the two complement readings of the
> generation triplet on the Boolean corner cube {0,1}^3: matter-as-hw=1 vs
> matter-as-hw=2 (complementation b -> 1-b maps the hw=1 triplet bijectively to the
> hw=2 triplet and commutes with the C_3[111] rotation, so both readings carry the same
> C_3 orbit structure and the same supplied circulant class). Then every
> Record-registrable scalar readout — finitely additive over pairwise-disjoint records
> and constant on K/CPT orbits — takes the SAME value on the two readings. Proof
> structure: (T1) the registrable surface is the symmetric-function algebra of the
> unordered spectrum [by the cited registrability theorem, Consequence B]; (T2) the
> full polynomial readout algebra on the slot model decomposes as symmetric data ⊕ the
> single orientation-odd C_3-invariant line (u - v) ⊕ frame-dependent
> (non-C_3-invariant) components; (T3) frame-dependent components are not constant on
> the supplied frame orbit, so they are not registrable; (T4) the orientation-odd line
> evaluates to (u - v)(slots) = -6 sqrt(3) B^3 sin(3 delta), which is K-odd and
> additive-class, hence killed by the additive-plus-even registrability theorem; (T5)
> every symmetric function of the unordered spectrum takes equal values on the two
> complement readings (same unordered spectrum; determinant phase enters only through
> cos(3 delta)). Hence the registrable content of the two readings coincides: the
> hw-complement CHOICE is not registrable content on this supplied slot model.

**T1 (runner checks A5, A10, B15).** The registrable surface is the
symmetric-function algebra of the unordered spectrum [by the cited
registrability theorem, Consequence B].

**T2 (runner checks A6, A7).** The full polynomial readout algebra on the slot
model decomposes as symmetric data plus the single orientation-odd
`C_3`-invariant line `(u - v)` plus frame-dependent non-`C_3`-invariant
components; the runner verifies the degree `<= 3` generator surface and the
one-line quotient explicitly.

**T3 (runner check A11).** Frame-dependent components are not constant on the
supplied frame orbit, so they are not registrable.

**T4 (runner checks A7, A8, A9).** The orientation-odd line evaluates to
`(u - v)(slots) = -6 sqrt(3) B^3 sin(3 delta)`, which is K-odd and
additive-class, hence killed by the additive-plus-even registrability theorem.

**T5 (runner checks A5, A10).** Every symmetric function of the unordered
spectrum takes equal values on the two complement readings: the supplied
circulant class and unordered spectrum are the same, and the determinant phase
enters only through `cos(3 delta)`.

## Consequence for the R1b anchor

Within `AC_phi_lambda` sub-admission (iii), the R1b semantic anchor ("the hw=1
triplet is the physical generation sector") carries, on this supplied slot
model, no registrable content: at this level it is frame/convention data. What
remains of sub-admission (iii) is the interpretive abstract-sector ->
physical-species identification itself and the full-dynamics complementation
equivariance, both explicitly NOT addressed here.

## What this note does NOT claim

- The equality of registrable content does not assert the two readings are
  physically identical in the full dynamics; it asserts no registrable readout
  of the supplied slot model distinguishes them.
- It does not select matter-as-`hw=1` or matter-as-`hw=2` as the physical
  species reading.
- It does not prove that the Hamming-complement choice is pure convention in
  the full dynamics.
- It does not close full-dynamics complementation-equivariance.
- It does not retire `AC_phi_lambda`, retire any sub-admission, or edit any
  registry surface.
- It does not derive `r`, force `r=1/2`, derive `delta`, or derive any
  charged-lepton value.
- It adds no axiom, primitive, admission, normalization, probability rule,
  comparator, or audit verdict.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) -- the Record
  boundary (Additivity + Orbit), the theorem's only axiom premise.
- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
  -- T1/T4 (registrable surface = symmetric functions; additive+even kills the
  odd line).

Context (not load-bearing: all facts used are reproven in this note's runner)

- `ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md` --
  where the complementation equivariance and the `(u - v)` line landed
  (open-gate support row; reproven here).
- `TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
  -- the orientation-flip companion (context).
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` -- where the supplied
  circulant class arises physically (context; the class is stipulated in-note).

**No-promotion statement:** this note does not promote, demote, or set the audit status of any dependency. The independent audit lane is the only status authority.
