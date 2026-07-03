# The Blocking-Isometry Hat Reduces to the Pointer-Frame Admission — Gated, Not Discharged

**Date:** 2026-06-09
**Type:** narrow bounded theorem (consolidation of the einselection / blocking-isometry hat)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_blocking_isometry_reduces_to_pointer_frame_admission_2026_06_09.py`
**Cache:** `logs/runner-cache/frontier_blocking_isometry_reduces_to_pointer_frame_admission_2026_06_09.txt`
**Status authority:** independent audit lane only. This source note does not set,
predict, or assert an audit verdict and does not claim "retained" or "promoted"
standing. Runner is exact finite-dimensional linear algebra, `PASS=30 FAIL=0`, no
Monte-Carlo in the logic path.

---

## The question (the least-worked of the four hats)

The gauge-link / color-einselection frontier carries four undelivered inputs ("hats"):
ADM-1 (the static local color-frame redundancy), R1 (a continuous-time gauge-link
generator), R2 / ADM-2 (the mixing regime / Ad-invariant link step measure — consolidated
across earlier blocks onto two gauge-structure admissions), and **hat 4: the blocking
isometry / einselection selection**. Two landed source proposals frame hat 4 but leave it
open:

- `RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06` (unaudited) proves the **forward**
  direction — a normalized record-writing isometry `W` yields a Kraus/CPTP instrument,
  with `W|psi> = sum_r (P_r|psi>) (x) |r>` for a named pointer projector set `{P_r}` — and
  **deliberately leaves open** the converse "persistent record dynamics ⇒ the isometry `W`".
- `BLOCK_SPIN_CP_COMPRESSION_COLOR_REEMERGENCE...` (unaudited) records that an
  axiom-preserving coarse-graining is a CP compression `E(X) = V† X V`, and states (without
  reducing it) that "the choice of isometry `V` is an undelivered selection — the same
  family as the open gauge-link-dynamics input".

This note makes that reduction **exact** and connects it to the campaign's already-named
record-frame / pointer-projector admission.

## Result

**In the finite pointer-record model tested here, the blocking-isometry hat is not an
independent admission. Its undelivered content reduces to the pointer-projector /
record-frame selection `{P_r}` that already gates the other hats.** Concretely:

1. **Dilation side (record write).** Given a pointer projector set `{P_r}` (orthogonal,
   `sum_r P_r = I`), the record-writing isometry is **fixed**:
   `W|psi> = sum_r (P_r|psi>) (x) |r>` satisfies `W†W = I`, has Kraus blocks
   `K_r = <r|W = P_r`, and dilates the pointer-dephasing channel `rho -> sum_r P_r rho P_r`.
   Given only the **channel**, `W` is unique up to a unitary on the record register — a
   Kraus gauge `K'_s = sum_r U_sr K_r` that reproduces the identical channel and touches
   **no system observable**. If the supplied pointer-record model demands that the
   register realize **orthogonal one-hot atoms** (`K_r† K_s = delta_rs K_r`), then the
   projective representation is singled out and the genuine freedom collapses entirely
   onto `{P_r}`.

2. **Compression side (block spin).** A coarse-graining isometry `V: C^2 -> C^d`
   (`V†V = I_2`, so `E(X) = V†XV` is unital and CP) carries a **survivor-qubit gauge**
   (`V' = VU` for `U ∈ U(2)` has the same range and only conjugates the survivor) plus a
   **physical part**: the choice of range = which 2-dimensional sector survives = the
   surviving pointer observable. That physical part is again a `{P_r}`-type choice; two
   ranges give genuinely different channels.

3. **Color specialization.** On the irreducible color triplet `C^3` the only SU(3)-invariant
   projectors are `0` and `I3` (Schur; the commutant of the irreducible fundamental is the
   scalars — witnessed exactly by the 9-element Heisenberg-Weyl twirl, `HW(3) ⊂ SU(3)`,
   sending any `X` to `(Tr X / 3) I3`). So the structure delivers **no** canonical covariant
   pointer set on color; any nontrivial `{P_r}` **names a color frame** — the same admission
   as the ADM-2 record frame and the block-02 record instruments.

**Therefore hat 4 is gated by the pointer-frame admission, parallel to (in fact rooted in
the same admission as) ADM-1 and ADM-2.** No hat is discharged: the isometry is **not**
delivered from `Lattice + Quantum + Record` — it requires the named `{P_r}`. This is **not**
a no-go: a named pointer set **does** fix the isometry, so the missing object is a canonical
covariant projector set, not an impossibility. The four hats are not four independent open
inputs; hat 4 shares the record-frame admission root.

## What the runner verifies (exact, `PASS=30 FAIL=0`)

- **B1** — for `n = 2, 3, 4`: `W†W = I`, `K_r = P_r`, and the partial trace over the record
  register equals `sum_r P_r rho P_r` (an independent re-derivation of the bridge note's
  forward algebra).
- **B2** — a unitary Kraus mix reproduces the same channel (the Kraus gauge); the projective
  representation is the one obeying `K_r† K_s = delta_rs K_r`; a generic gauge rep is not
  projective (it scrambles the one-hot record atoms); the gauge leaves system statistics
  invariant.
- **B3** — two different pointer sets give different channels (the physical choice); a pure
  record-label relabeling (permutation + phase of `|r>`) leaves the channel and the one-hot
  structure invariant (pure gauge).
- **B4** — the compression isometry: `V†V = I_2`; `V' = VU` shares the range (survivor gauge);
  `E'(Y) = U† E(Y) U`; a different range is a physically distinct surviving sector.
- **B5** — on `C^3`: sampled SU(3) elements are genuine; `I3` is the trivial invariant
  projector; a rank-1 color projector breaks covariance; the exact `HW(3)` twirl sends any
  Hermitian `X` to `(Tr X / 3) I3` (commutant = scalars); only invariant projector ranks are
  `0` and `3`; an `SU(2)`/`C^2` sanity mirror.
- **B6** — the consolidation table: the isometry is fixed given `{P_r}` (gated, not
  impossible); hat 4 reduces to the named pointer-frame admission; **no hat discharged**.

## Grounds (verified live on `origin/main` this block)

`graph_first_su3_integration_note` = retained (SU(3) = commutant of observables, fundamental
on `C^3`); `cl3_color_automorphism_theorem` = retained;
`kraus_choi_representation_normalization_reconciled_narrow_theorem_note` = retained;
`block_gaussian_schur_marginalization_narrow_theorem_note` = retained;
`record_classical_semigroup_boundary` = retained;
`record_markov_generator_embeddability_boundary` = retained_no_go;
`record_formation_not_unconditionally_forced...` = retained_no_go.
`RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE`, `BLOCK_SPIN_CP_COMPRESSION_COLOR_REEMERGENCE`,
and `DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE` are **unaudited** source
proposals — cited for framing, **not** consumed as retained. The loose register-not-read
dichotomy is demoted (2026-06-06 scope correction, meta) and the genuine partition map is
trivial on the irreducible color triplet — consistent with B5.

## Honest boundary — what this does NOT do

- It does **not** discharge hat 4, nor deliver the isometry from the axioms. The pointer
  projector set `{P_r}` (equivalently the surviving sector / record frame) remains a named
  admission Record does not supply (`record_formation_not_unconditionally_forced` =
  retained_no_go; `record_markov_generator_embeddability_boundary` = retained_no_go).
- It does **not** select a canonical pointer set, force `r = 1/2` or any registered value,
  or claim a partition map for the irreducible color triplet (B5 shows there is none beyond
  `0, I3`).
- It does **not** construct a connection, induce a link, or move R1 / R2; it characterizes
  the **converse** the bridge note leaves open by locating its content in the already-named
  frame admission.
- The reduction is conditional on the finite pointer-record model the bridge note uses
  (finite spectral `{P_r}`, ideal label-copy write); it is a structural consolidation, not a
  dynamical production of the record.
- No closing language: other coarse-graining and dilation notions are not enumerated or
  foreclosed; a future structural premise that delivers a canonical covariant pointer set
  would reopen hat 4 as derivable. Walls move.

## No hat discharged

ADM-1, the R1 link generator, the R2 link-measure delivery, and the einselection selection
remain open. No ST1/ST2 ranking is made. The contribution is to **bound** hat 4: its
undelivered content is the pointer-frame admission, the same root the campaign has named for
ADM-1 and ADM-2.
