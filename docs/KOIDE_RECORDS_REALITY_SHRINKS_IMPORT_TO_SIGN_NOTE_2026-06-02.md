# Reality/CPT Discharges the Records Branch Phase but Not the Sign: the Terminal T-Positivity Import Shrinks From U(1) to a Z_2 Sign

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note adds no axiom and no import; it
characterizes an existing import boundary more precisely.
**Primary runner:** [`scripts/frontier_koide_records_reality_shrinks_import_to_sign.py`](../scripts/frontier_koide_records_reality_shrinks_import_to_sign.py) (SCORECARD PASS=18)

## Context

The reduction note
[`KOIDE_RP_SPECTRUM_REDUCE_TO_TRANSFER_POSITIVITY_NARROW_THEOREM_NOTE_2026-06-02.md`](KOIDE_RP_SPECTRUM_REDUCE_TO_TRANSFER_POSITIVITY_NARROW_THEOREM_NOTE_2026-06-02.md)
collapsed reflection positivity and the spectrum condition to one statement --
the emergent-time transfer operator `T` is positive Hermitian -- with a
records-route antecedent: the records/decoherence Kraus operators are
Hermitian (dissipator trace-symmetric at the tracial reference). The companion
[`KOIDE_HERMITIAN_RECORDS_IMPORT_REQUIRED_NARROW_THEOREM_NOTE_2026-06-02.md`](KOIDE_HERMITIAN_RECORDS_IMPORT_REQUIRED_NARROW_THEOREM_NOTE_2026-06-02.md)
showed
that antecedent is import-required, naming the residual as a positive real
branch-coherence condition with `U = I` (NO-RELATIVE-BRANCH-PHASE) as a
sufficient frame, and noted (as the highest-value lead) that a CPT/reality
condition on the record-writing generator might discharge it -- the same object
as the value-side signed-vs-singular readout phase
([`KOIDE_REALITY_FAVORS_SIGNED_READOUT_SHARED_MECHANISM_NARROW_THEOREM_NOTE_2026-06-02.md`](KOIDE_REALITY_FAVORS_SIGNED_READOUT_SHARED_MECHANISM_NARROW_THEOREM_NOTE_2026-06-02.md)).

This note executes that probe and the emergent-time-construction probe. It
determines precisely how much reality/CPT buys.

## Claim

For the diagonal branch-multiplier record family, a pointer-basis reality/CPT
condition (`E(rho*) = E(rho)*`) -- modeled by the real record-writing
interaction tested below, the records analog of
[`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
-- **discharges the branch PHASE but not the SIGN**:

1. in that branch family it forces the off-diagonal record multiplier `z` to be REAL, killing the
   `U(1)` branch phase and making the transfer operator `T` HERMITIAN
   (self-dual);
2. it does NOT force `T` to be POSITIVE: the explicit real `H_int` witness yields a Hermitian
   transfer with a NEGATIVE eigenvalue for generic tested coupling times. The residual
   is a `Z_2` SIGN, structurally identical to the value-side signed-`sqrt(m)`
   readout sign.

Therefore the terminal T-positivity import shrinks from the prior
`U(1)` NO-RELATIVE-BRANCH-PHASE / `U = I` condition down to the strictly
weaker `Z_2` POSITIVE-SIGN condition: the record-writing Kraus operators are
HERMITIAN (= trace-symmetric dissipator at the tracial reference `I/2`,
= off-diagonal multiplier `z >= 0`) in the tested branch family. This is a
named residual/import candidate for the charged-lepton carrier's dynamics leg;
it is not adopted here.

Separately, the emergent-time single-clock-Stone construction CONSUMES
T-positivity (it is the construction's stated hypothesis), so it cannot FORCE
it; using it as a forcing argument is circular.

### A. Reality kills the U(1) branch phase (self-duality)

The transfer superoperator `T` (column-stacking of `E(rho) = sum_r K_r rho K_r^dag`)
is HERMITIAN as a matrix iff `E` equals its Hilbert-Schmidt dual
`E*(X) = sum_r K_r^dag X K_r`. A dagger-closed Kraus representation is a
sufficient mechanism for that self-duality. For the
phase-twisted diagonal family the off-diagonal multiplier is
`z = sum_r p_r exp(i(a_r - b_r))`; pointer-basis reality `E(rho*) = E(rho)*`
holds iff `z = z*`, i.e. `z` real. The prior counterexample
(`z = 0.5 + 0.5 i`, `spec(T) = {1, 1, 0.5 +- 0.5 i}`) is precisely the
NOT-reality-even case; reality EXCLUDES it. So reality/CPT discharges exactly
the `NO-RELATIVE-BRANCH-PHASE` part of the prior import (it reduces the
continuous `U(1)` eigen-phase to a `Z_2` sign on each Hermitian eigen-sector).

### B. Reality does NOT buy positivity in the tested record model (the sign survives)

A real (reality/CPT-respecting) record-writing model `H_int = sigma_z (x) sigma_x`
gives, via the von Neumann record blocks `K_r = <r|_meter exp(-i H_int t)|0>_meter`,
a transfer operator that is Hermitian for all `t` but has a NEGATIVE eigenvalue
for generic `t` (e.g. `spec(T) = {-0.74, -0.74, 1, 1}` at `t = 1.2`;
`-> {-1, -1, 1, 1}` at `t = pi/2`). The record Kraus blocks are not individually
Hermitian even though `H_int` is real. So self-adjointness of the generator
collapses the `U(1)` eigen-phase to a `Z_2` sign, and leaves the sign free --
exactly the value-side mechanism of `KOIDE_REALITY_FAVORS_SIGNED`.

### C. Positive-Hermitian examples need a stronger sign/detailed-balance condition

Positive-Hermitian `T` (=> the spectrum condition `Hhat >= 0` and OS reflection
positivity via the reduction note) is delivered by the tested stronger
Hermitian-Kraus / detailed-balance examples: the verified Pauli mixtures and
the `sqrt(E_r)` Hermitian-POVM channels are self-dual AND positive. This is a
trace-symmetric / detailed-balance-at-`I/2` class, stronger than branch
reality. The explicit real record model is self-dual but indefinite and is NOT
in this positive class. Hence the terminal residual is the positive-SIGN /
detailed-balance condition, NOT the no-relative-phase condition.

### D. The emergent-time construction consumes, not delivers, T-positivity

`single_clock_stone_finite_dim_uniqueness` (retained) constructs
`H = -(1/tau) log(T)` under its stated hypothesis `0 < spec(T) <= ||T||`. A
non-positive transfer (a negative eigenvalue) yields a non-Hermitian generator,
so the construction cannot run. T-positivity is the premise, not the output;
the construction is therefore not a forcing source. The parent
`axiom_first_single_clock_codimension1_evolution` (audited_conditional)
likewise consumes RP and the spectrum condition as inputs.

### E. Genericity sampling (the import is special)

Among 4000 random two-Kraus qubit channels sampled from a Stinespring unitary,
none landed in the Hermitian-Kraus or positive-Hermitian-transfer classes. This
sampling does not by itself prove a measure-zero theorem, but it confirms the
positive-sign condition is a special constraint, not something the minimal
baseline supplies generically.

## Net standing

Within this records route, closing the dynamics leg's T-positivity now reduces
to the `Z_2` positive-sign (detailed-balance / positive Hermitian transfer)
residual, with the `U(1)`
phase part discharged by the reality/CPT mechanism. This is the same `Z_2` sign
the value-side signed readout needs, on a different tensor factor (records sit
on the site qubit `C^2`; the `sqrt(m)` sign on the generation `C^3`); the
`C^2 -> C^3` bridge is the open generation-identification gate, so the shared
mechanism does not yet collapse the two signs into one object (consistent with
`KOIDE_REALITY_FAVORS_SIGNED`). The Koide VALUE chain (dominated by
`AC_phi_lambda`, with `r = 1/2` and the now-`audited_failed` signed-readout
class) is on a separate axis and is untouched.

## No-Go Discipline Gate

This gate applies to the negative/open part of the claim: the reviewed
reality/CPT route shrinks the residual but does not force `T >= 0`.

- **N1 alternative routes:** (1) branch-multiplier reality; (2) explicit real
  record-writing Hamiltonian; (3) Hermitian-Kraus / detailed-balance examples;
  (4) single-clock Stone construction; (5) random-channel genericity; (6) a
  future site-to-generation sign bridge. Routes (1)-(5) are tested here;
  route (6) is named as a future partial-closure path.
- **N2 wall independence:** the `U(1)` phase wall and the `Z_2` sign wall are
  not independent after the branch-family calculation: reality retires the
  phase wall and leaves only the positivity/sign wall.
- **N3 hidden-wall scan:** "reality/CPT," "Hermitian Kraus," and
  "detailed balance" are not admitted. Reality is imposed as the test
  condition; detailed balance/positive sign remains the named residual.
- **N4 residual matching:** the RP/spectrum reduction consumes positive
  Hermitian `T`; the Hermitian-records note named branch coherence; this note
  tests only the phase-vs-sign split of that residual. It does not claim to
  close the RP/spectrum lane.
- **N5 rhetoric audit:** "reality kills the phase" is scoped to the diagonal
  branch-multiplier family and the explicit real record model. It does not
  claim every real interaction Hamiltonian produces a positive transfer.
- **N6 partial-closure scan:** a retained detailed-balance/KMS derivation for
  records growth, a two-step transfer-positivity route, or a site-to-generation
  sign bridge could retire the residual without adding an axiom.
- **N7 steelman:** a future derivation could show the framework's actual
  records-growth channel is detailed-balanced at `I/2`; that would supply
  `T >= 0` and defeat the open sign residual while preserving this note's
  phase-shrink calculation.
- **N8 cross-cycle echo:** the value-side signed-readout defect and the
  records-side transfer sign have the same `Z_2` shape, but they live on
  different tensor factors until a generation-identification bridge is
  retained.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| [`cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md) | retained_bounded |
| [`single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md) | status per ledger |
| [`pre_record_reference_state_tracial_derivation_note_2026-05-20`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) | retained |
| [`kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md) | retained |
| [`persistent_record_as_kraus_operator_note_2026-05-20`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md) | retained_bounded |
| [`luders_rule_from_composition_consistency_note_2026-05-20`](LUDERS_RULE_FROM_COMPOSITION_CONSISTENCY_NOTE_2026-05-20.md) | retained_bounded |
| [`lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`](LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md) | status per ledger |
| [`yt_lsp_signed_record_source_readout_support_note_2026-05-24`](YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md) | retained_bounded |
| [`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) | retained |
| [`axiom_first_reflection_positivity_theorem_note_2026-04-29`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md) | unaudited |
| [`axiom_first_spectrum_condition_theorem_note_2026-04-29`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md) | unaudited |
| [`axiom_first_cpt_theorem_stretch_note_2026-04-29`](AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md) | unaudited |
| [`observable_principle_from_axiom_note`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md) | audited_conditional |
| [`koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md) | audited_failed |

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
  channel (forces `z >= 0` in the branch-multiplier family, with Hermitian
  Kraus/detailed balance as the stronger sufficient class tested here).
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
