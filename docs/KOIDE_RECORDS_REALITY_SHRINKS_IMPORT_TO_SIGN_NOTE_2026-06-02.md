# Reality/CPT Discharges the Records Branch Phase but Not the Sign: the Terminal T-Positivity Import Shrinks From U(1) to a Z_2 Sign

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note adds no axiom and no import; it
characterizes an existing import boundary more precisely.
**Primary runner:** [`scripts/frontier_koide_records_reality_shrinks_import_to_sign.py`](../scripts/frontier_koide_records_reality_shrinks_import_to_sign.py) (SCORECARD PASS=18)

## Context

The reduction note
`KOIDE_RP_SPECTRUM_REDUCE_TO_TRANSFER_POSITIVITY_NARROW_THEOREM_NOTE_2026-06-02`
collapsed reflection positivity and the spectrum condition to one statement --
the emergent-time transfer operator `T` is positive Hermitian -- with a
records-route antecedent: the records/decoherence Kraus operators are
Hermitian (dissipator trace-symmetric at the tracial reference). The companion
`KOIDE_HERMITIAN_RECORDS_IMPORT_REQUIRED_NARROW_THEOREM_NOTE_2026-06-02` showed
that antecedent is import-required, naming the residual as a positive real
branch-coherence condition with `U = I` (NO-RELATIVE-BRANCH-PHASE) as a
sufficient frame, and observed (as the highest-value lead) that a CPT/reality
condition on the record-writing generator might discharge it -- the same object
as the value-side signed-vs-singular readout phase
(`KOIDE_REALITY_FAVORS_SIGNED_READOUT_SHARED_MECHANISM_NARROW_THEOREM_NOTE_2026-06-02`).

This note executes that probe and the emergent-time-construction probe. It
determines precisely how much reality/CPT buys.

## Claim

A reality/CPT condition on the record-writing coupling -- a real interaction
Hamiltonian `H_int` (the records analog of
`cpt_exact_real_anti_hermitian_d` "D real anti-Hermitian", equivalently the
antiunitary symmetry `K H_int K = H_int`, equivalently pointer-basis reality
`E(rho*) = E(rho)*`) -- **discharges the branch PHASE but not the SIGN**:

1. it forces the off-diagonal record multiplier `z` to be REAL, killing the
   `U(1)` branch phase and making the transfer operator `T` HERMITIAN
   (self-dual);
2. it does NOT force `T` to be POSITIVE: a real `H_int` yields a Hermitian
   transfer with a NEGATIVE eigenvalue for generic coupling time. The residual
   is a `Z_2` SIGN, structurally identical to the value-side signed-`sqrt(m)`
   readout sign.

Therefore the terminal T-positivity import shrinks from the prior
`U(1)` NO-RELATIVE-BRANCH-PHASE / `U = I` condition down to the strictly
weaker `Z_2` POSITIVE-SIGN condition: the record-writing Kraus operators are
HERMITIAN (= trace-symmetric dissipator at the tracial reference `I/2`,
= off-diagonal multiplier `z >= 0`). This is the irreducible Tier-A admission
of the charged-lepton carrier's dynamics leg. It is named, not adopted.

Separately, the emergent-time single-clock-Stone construction CONSUMES
T-positivity (it is the construction's stated hypothesis), so it cannot FORCE
it; using it as a forcing argument is circular.

### A. Reality kills the U(1) branch phase (self-duality)

The transfer superoperator `T` (column-stacking of `E(rho) = sum_r K_r rho K_r^dag`)
is HERMITIAN as a matrix iff `E` equals its Hilbert-Schmidt dual
`E*(X) = sum_r K_r^dag X K_r`, iff the Kraus set is closed under dagger. For the
phase-twisted diagonal family the off-diagonal multiplier is
`z = sum_r p_r exp(i(a_r - b_r))`; pointer-basis reality `E(rho*) = E(rho)*`
holds iff `z = z*`, i.e. `z` real. The prior counterexample
(`z = 0.5 + 0.5 i`, `spec(T) = {1, 1, 0.5 +- 0.5 i}`) is precisely the
NOT-reality-even case; reality EXCLUDES it. So reality/CPT discharges exactly
the `NO-RELATIVE-BRANCH-PHASE` part of the prior import (it reduces the
continuous `U(1)` eigen-phase to a `Z_2` sign on each Hermitian eigen-sector).

### B. Reality does NOT buy positivity (the sign survives)

A real (reality/CPT-respecting) record-writing `H_int = sigma_z (x) sigma_x`
gives, via the von Neumann record blocks `K_r = <r|_meter exp(-i H_int t)|0>_meter`,
a transfer operator that is Hermitian for all `t` but has a NEGATIVE eigenvalue
for generic `t` (e.g. `spec(T) = {-0.74, -0.74, 1, 1}` at `t = 1.2`;
`-> {-1, -1, 1, 1}` at `t = pi/2`). The record Kraus blocks are not individually
Hermitian even though `H_int` is real. So self-adjointness of the generator
collapses the `U(1)` eigen-phase to a `Z_2` sign, and leaves the sign free --
exactly the value-side mechanism of `KOIDE_REALITY_FAVORS_SIGNED`.

### C. Positivity <=> Hermitian Kraus (strictly stronger than reality)

Positive-Hermitian `T` (=> the spectrum condition `Hhat >= 0` and OS reflection
positivity via the reduction note) is delivered by HERMITIAN Kraus operators:
the `sqrt(p_i) sigma_i` Pauli channels and the `sqrt(E_r)` Hermitian-POVM
channels are self-dual AND positive (verified). This is the trace-symmetric /
detailed-balance-at-`I/2` class. Reality (self-dual but indefinite) is NOT in
this class. Hence the terminal residual is the positive-SIGN / Hermitian-Kraus
condition, NOT the no-relative-phase condition.

### D. The emergent-time construction consumes, not delivers, T-positivity

`single_clock_stone_finite_dim_uniqueness` (retained) constructs
`H = -(1/tau) log(T)` under its stated hypothesis `0 < spec(T) <= ||T||`. A
non-positive transfer (a negative eigenvalue) yields a non-Hermitian generator,
so the construction cannot run. T-positivity is the premise, not the output;
the construction is therefore not a forcing source. The parent
`axiom_first_single_clock_codimension1_evolution` (audited_conditional)
likewise consumes RP and the spectrum condition as inputs.

### E. Genericity (the import is real)

Among random unital qubit channels, Hermitian-Kraus and positive-Hermitian
transfer are measure-zero (0 of 4000). So the positive-sign condition is a
genuine constraint, not a generic property -- an import, not a theorem on the
minimal baseline.

## Net standing

Closing the dynamics leg's T-positivity now requires exactly the `Z_2`
positive-sign (Hermitian-Kraus / detailed-balance) admission, with the `U(1)`
phase part discharged by the reality/CPT mechanism. This is the same `Z_2` sign
the value-side signed readout needs, on a different tensor factor (records sit
on the site qubit `C^2`; the `sqrt(m)` sign on the generation `C^3`); the
`C^2 -> C^3` bridge is the open generation-identification gate, so the shared
mechanism does not yet collapse the two signs into one object (consistent with
`KOIDE_REALITY_FAVORS_SIGNED`). The Koide VALUE chain (dominated by
`AC_phi_lambda`, with `r = 1/2` and the now-`audited_failed` signed-readout
class) is on a separate axis and is untouched.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` | retained_bounded |
| `single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10` | retained |
| `pre_record_reference_state_tracial_derivation_note_2026-05-20` | retained |
| `kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20` | retained |
| `persistent_record_as_kraus_operator_note_2026-05-20` | retained_bounded |
| `luders_rule_from_composition_consistency_note_2026-05-20` | retained_bounded |
| `lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22` | retained_bounded |
| `yt_lsp_signed_record_source_readout_support_note_2026-05-24` | retained_bounded |
| `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | retained |
| `axiom_first_reflection_positivity_theorem_note_2026-04-29` | unaudited |
| `axiom_first_spectrum_condition_theorem_note_2026-04-29` | unaudited |
| `axiom_first_cpt_theorem_stretch_note_2026-04-29` | unaudited |
| `observable_principle_from_axiom_note` | audited_conditional |
| `koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29` | audited_failed |

## Non-circularity

No step assumes `T` positive, `T` Hermitian, CAR, or Hermitian records as an
INPUT to derive them. Sections A-B IMPOSE the reality condition (real `H_int`)
and COMPUTE that the resulting transfer is Hermitian-but-signed -- a forward
computation; the conclusion is not assumed. Section C shows Hermitian-Kraus is
SUFFICIENT for positivity (forward). Section D reads the Stone construction's
stated hypothesis. `Q = 2/3` never appears; no PDG value is consumed.

## Next paths this opens

- The shrunk terminal gate is now a `Z_2` SIGN. The smallest closing step is a
  detailed-balance / KMS-at-`I/2` derivation for the framework's records-growth
  channel (forces `z >= 0`, equivalently Hermitian Kraus).
- A reality-respecting `C^2 (site) -> C^3 (generation)` bridge would make the
  records-side `Z_2` sign and the value-side `sqrt(m)` `Z_2` sign one operator's
  eigen-sector sign, upgrading the shared mechanism to a shared object and
  discharging both `Z_2` residuals at once.
- Independently, the action-native two-step transfer-positivity route
  (`axiom_first_rp_two_step_transfer_matrix_positivity`, audited_conditional)
  remains an alternative to the records route, contingent on the
  staggered-Dirac and `g_bare` gates.

This sharpens the dynamics-leg import boundary from a `U(1)` phase to a `Z_2`
sign and shows the construction cannot supply positivity; it is a sharpening,
not a closure.
