# The Magnitude Reads the Minimal Record Block (Lₜ=2), Not the OS Continuum

**Date:** 2026-06-06
**Type:** bounded positive route / register-not-read principle-extension
**Claim type:** bounded_theorem
**Status:** branch-local bounded. Closes the readout-scale residual of
`MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06` at principle-grade, by
extending the framework's register-not-read ontology to the temporal readout
scale. Sets no audit status; audit lane owns final classification.
`audit_required_before_effective_retained=true; bare_retained_allowed=false`.
**Runner:** [`scripts/magnitude_reads_minimal_record_block_2026_06_06.py`](../scripts/magnitude_reads_minimal_record_block_2026_06_06.py)
(`TOTAL: PASS=13 FAIL=0`).
**Cached log:** `logs/runner-cache/magnitude_reads_minimal_record_block_2026_06_06.txt`

## The residual being closed

`MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06` (bounded) showed the
magnitude's temporal factor of 2 is a transfer-step **count** (not a clock rate),
so the retained clock-rate no-go does not block it; the minimal reflection-
positive temporal block is 2. It left one named residual:

> **(R)** Why is the magnitude read at the **minimal** reflection-positive block
> (`L_t = 2`, temporal count 2) rather than the OS continuum (`L_t -> infinity`,
> count -> infinity)?

This note closes R using the framework's own core principle, **register-not-read**
(`record_outcome_observable_principle_canonical_proposal_note_2026-06-05`, meta;
loaded as the framework's stated ontology).

## The closure (register-not-read, extended to the temporal readout scale)

**Step 1 — irreducibility (retained-grade).** The staggered temporal phase
`eta_1(t) = (-1)^t` has minimal period 2, so a single time-slice is not a
translation-invariant cell; and the single-step transfer is non-positive while the
2-step block `T_hat^2` is reflection-positive
(`axiom_first_rp_two_step_transfer_matrix_positivity`, retained_bounded; 2-step
contraction `e^{-2E} in (0,1]` verified). So the **minimal physical /
registrable temporal unit is irreducibly 2 lattice steps** — there is no positive
sub-block. (Runner Section I.)

**Step 2 — registration vs reconstruction.** In the record ontology, reality **is**
the discrete record stack; the emergent continuous time (the OS-reconstructed
Hamiltonian limit `L_t -> infinity`, `a_tau -> 0`) is a **coarse-grained
reconstruction** built from monotone record accumulation (the arrow). The
registration is the discrete record; its temporal extent is the irreducible
minimal block (Step 1), with temporal count **2**. The continuum count
(`-> infinity`) is a property of the **reconstruction**, not the registration.
(Runner Section R.)

**Step 3 — register-not-read selects the registration.** The canonical principle:
an observable is what the record **registers**; pre-record / reconstructed objects
are calculational devices, and *mistaking a reconstruction for the registration is
the realist slip*. Applied here (an **extension** of the principle from
operator-form to **temporal readout scale** — flagged explicitly below): the
magnitude's bare structural exponent is **registered** at the discrete minimal
block (count 2). Reading that bare exponent at the reconstructed continuum
(count `-> infinity`) is the realist slip — using the reconstruction for the
registration. Hence the temporal count is **2**, and the bare exponent is
`8 (spatial) x 2 (temporal) = 16`. (Runner Sections R, S.)

## The realist slip, checked in both directions

The slip could in principle cut the other way — *"reading the bare lattice count is
itself the slip; the real (measured) mass is the IR continuum."* It does not,
because the magnitude's **exponent** and **value** are different objects:

- The **exponent** (`16`) is a bare / UV / cutoff-scale **structural count** — the
  number of suppression factors at the cutoff `M_Pl = a^{-1}` (the framework's one
  unit, the minimal lattice scale). At the cutoff the temporal structure is the
  irreducible minimal block, so the exponent is registered there: count 2.
- The **value** (`alpha_LM`, the per-mode suppression) is the **running / IR**
  content — the separate `DELTA0` magnitude gate, untouched here.

So the bare exponent is genuinely a registration-scale (UV) quantity and is
correctly read at the minimal block; the IR/measured mass is `exponent-structure x
running(alpha_LM)`. Using the continuum count for the **exponent** is the slip; the
running lives in the value, not the count. (Runner Section S.)

## What this delivers (and the honest tier)

Combined with the count-not-rate note, the magnitude's temporal factor of 2 now
has a **native account**:

```text
temporal factor of 2
  = a transfer-step COUNT, not a rate          (clock-rate no-go does not block it)
  = the minimal reflection-positive block       (RP two-step, retained_bounded)
  = the registered (not reconstructed) extent   (register-not-read, this note)
```

So the bare magnitude exponent `16 = 8 (spatial Z^3 corners, retained) x 2
(temporal, this chain)` is **native modulo the register-not-read principle**. This
is a **bounded** result: the mechanical core (minimal block = 2) is retained-grade;
the readout-scale selection is a **principle-extension** step (register-not-read,
itself claim_type meta, applied to a new domain — the temporal readout scale —
that the canonical note does not explicitly cover). The audit lane owns whether the
extension is accepted as load-bearing.

## Scope — what this does NOT claim

- Does **not** derive the magnitude `v` or close the hierarchy gate. The per-mode
  **value** `alpha_LM` (the `DELTA0` magnitude) is a separate open gate, untouched.
- Does **not** upgrade register-not-read to a mechanical theorem; the readout-scale
  application is a flagged **extension** of a meta principle, hence bounded.
- Does **not** derive a clock, time metric, or rate (consistent with the retained
  clock-rate no-go); the temporal **count** is what is registered, not a rate.
- Does **not** assert the OS continuum is "wrong" — it is the correct emergent /
  IR reconstruction; the claim is only that the **bare exponent** is registered at
  the minimal block, not read off the reconstruction.
- Sets no audit status.

## Load-bearing dependency and context references

- `record_outcome_observable_principle_canonical_proposal_note_2026-06-05`
  (**meta**) — the register-not-read principle (registration vs reconstruction,
  realist slip); the principle extended in Step 3.
- `axiom_first_rp_two_step_transfer_matrix_positivity` (**retained_bounded**) —
  the minimal reflection-positive temporal block is 2 (Step 1).
- `MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE_2026-06-06` (bounded) — the residual
  R closed here; the count-not-rate result this builds on.
- `naive_lattice_fermion_two_power_d_species_count` (**retained**),
  `staggered_dirac_substep3_bz_corner_hamming_orbit` (**retained**) — the 8
  spatial corner count.
- `hierarchy_alpha_lm_magnitude_delta0_open_gate_note_2026-05-30` (**open_gate**) —
  the remaining per-mode value gate (`alpha_LM`/`DELTA0`), unaffected.

## Forbidden imports check

- No PDG observed values consumed (`alpha_LM`/`v` appear only in background, in no
  PASS condition).
- No literature comparators; no fitted selectors; no admitted unit conventions
  load-bearing on retention.
- No new axiom proposed; register-not-read is the framework's own stated ontology.
- All cited statuses verified on the live ledger.

## Validation

`scripts/magnitude_reads_minimal_record_block_2026_06_06.py` (`PASS=13 FAIL=0`):
Section I (period-2 phase, single-time-slice not a cell, 2-step positivity,
single-step non-positivity cited → minimal block 2), Section R (finite
registration count 2 vs unbounded reconstruction limit), Section S (bare exponent =
registration count 16; the continuum would give `8 L_t -> infinity`, the slip; the
exponent is independent of the per-mode value), Section C (closure structure:
retained mechanical core + flagged register-not-read principle-extension).

## Reading rule

This note is the claim boundary for: the magnitude's bare temporal **count** is
read at the irreducible minimal reflection-positive block (`L_t = 2`), not the OS
continuum, via register-not-read (registration over reconstruction) extended to the
temporal readout scale. It closes residual R at **principle-grade (bounded)**; it
does **not** derive the magnitude value `alpha_LM` (the `DELTA0` gate). With the
count-not-rate note, the bare exponent `16 = 8 x 2` has a native account modulo the
register-not-read principle-extension.
