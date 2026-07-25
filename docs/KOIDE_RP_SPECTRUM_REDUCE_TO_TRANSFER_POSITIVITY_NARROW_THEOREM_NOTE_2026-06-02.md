# RP and the Spectrum Condition Reduce to Transfer-Operator Positivity, with a Records-Route Target

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit.
**Primary runner:** [`scripts/frontier_koide_rp_spectrum_reduce_to_transfer_positivity.py`](../scripts/frontier_koide_rp_spectrum_reduce_to_transfer_positivity.py)

## Context

The companion note
[`KOIDE_MATTER_ATTACHMENT_GATE_EXTRA_ASSUMPTIONS_REVIEW_NOTE_2026-06-02`](KOIDE_MATTER_ATTACHMENT_GATE_EXTRA_ASSUMPTIONS_REVIEW_NOTE_2026-06-02.md)
located the charged-lepton matter-attachment escape in the emergent-time
dynamics arena: a `free_sector` reduction forces CAR (fermionic) statistics
from energy-positivity plus microcausality, FOR a reconstructed relativistic
field. The keystone rungs are reflection positivity (RP,
`axiom_first_reflection_positivity_theorem_note_2026-04-29`, unaudited) and the
spectrum condition (`Hhat >= 0`,
`axiom_first_spectrum_condition_theorem_note_2026-04-29`, unaudited). This note
records what those two rungs actually reduce to, and a route to that statement
that uses no import.

## Claim

RP and the spectrum condition reduce to **one statement** -- the emergent-time
transfer operator `T` is positive Hermitian. A non-staggered records-route
scaffold reaches that statement if the records/decoherence generator is
trace-symmetric with respect to the retained tracial reference. That antecedent
is a derivation target, not a result of this note. The staggered Kogut-Susskind
plus Wilson-`SU(3)` route to the same statement is an **import** (two open gates)
and is named, not adopted.

### A. The reduction (`Hhat >= 0  <==>  T positive Hermitian`)

Via the retained
`single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10`
(**retained**), the emergent-time Hamiltonian is
`Hhat = -(1/a) log(T / ||T||)`. Then:

```text
T positive Hermitian, spectrum in (0, ||T||]  ==>  Hhat self-adjoint, Hhat >= 0, E_0 = 0.
```

So the spectrum condition is a corollary of `T`-positivity, not an independent
postulate. And the Osterwalder-Schrader reconstruction gives RP from a positive
self-adjoint transfer matrix (the reflected Gram matrix
`M_ij = <v| T^{i+j} |v>` is PSD). **RP and the spectrum condition are therefore
the same statement: `T` is positive Hermitian.**

### B. The records-route scaffold (records CP semigroup + tracial reference)

Model the emergent-time step as the framework's records / decoherence
completely-positive map (the CP / Kraus structure is carried by
`kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`,
`persistent_record_as_kraus_operator_note_2026-05-20`, and
`decoherence_action_independence_note`; status per ledger for each, and this
note does not assert their grades). If the record / Lindblad operators are HERMITIAN, then
with the retained tracial reference state
`rho_ref = (x) I/2`
(`pre_record_reference_state_tracial_derivation_note_2026-05-20`, **retained**)
the dissipator `D` is TRACE-SYMMETRIC (self-adjoint as a superoperator on the
trace inner product). Hence:

```text
D self-adjoint, dissipative (spec(D) <= 0)  ==>  T = e^{aD} positive Hermitian, spectrum in (0,1]
                                            ==>  Hhat >= 0  (via the Stone map)  AND  OS reflection positivity.
```

The runner verifies all of this on a finite carrier (`D = D^dag` to machine
precision; `spec(T) in (0,1]`; `Hhat >= 0`; the reflected Gram matrix PSD). No
staggered or Wilson structure enters.

### C. Why the tracial reference is exactly right

Trace-symmetry of the dissipator (detailed balance) holds precisely with the
tracial = maximally mixed = infinite-temperature reference `rho_ref = I/2`,
which is exactly the retained pre-record reference state. So the framework's own
retained reference state is the detailed-balance reference under which Hermitian
records give a positive Hermitian transfer operator. This is a structural match,
not a fit.

### D. The staggered / Wilson route is an import (named, not adopted)

A generic, NON-Hermitian record operator gives a dissipator that is not
trace-symmetric, so the single-step `T` is not Hermitian and one must pass to
the two-step `T^dag T` (the `axiom_first_rp_two_step_transfer_matrix_positivity`
construction, **audited_conditional**) -- which is proven about the staggered
Kogut-Susskind Dirac operator and the Wilson `SU(3)` plaquette measure. That
arena is the staggered-Dirac realization gate plus the `g_bare`/Wilson gate,
both OPEN per `MINIMAL_AXIOMS_2026-05-20.md`. Adopting RP
"because the staggered/Wilson lattice has it" presupposes those open gates and
is an import requiring explicit user approval. It is named here and **not
adopted**; the records-route scaffold (B) bypasses that particular import only
if its trace-symmetry antecedent is separately derived.

## What is and is not claimed

**Claimed:** the reduction (A), the records-route MATH scaffold (B, C) -- both
verified -- and the identification of the staggered route as an import (D). RP
and `Hhat >= 0` reduce to a single transfer-positivity target, with
records-generator trace-symmetry left as an unbuilt step.

**Not claimed:** that RP or `Hhat >= 0` are hereby derived. The route's
antecedent -- that the framework's records-growth dynamics is a trace-symmetric
CP semigroup with respect to the tracial reference -- is an unbuilt DERIVATION
TARGET, not an assumption. Positing a specific emergent-time map would be the
disallowed move; this note instead localizes the cascade to a checkable target.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| [`single_clock_stone_finite_dim_uniqueness_narrow_theorem_note_2026-05-10`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md) | status per ledger |
| [`pre_record_reference_state_tracial_derivation_note_2026-05-20`](PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md) | retained |
| [`kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md) | retained |
| [`persistent_record_as_kraus_operator_note_2026-05-20`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md) | retained_bounded |
| [`decoherence_action_independence_note`](DECOHERENCE_ACTION_INDEPENDENCE_NOTE.md) | status per ledger |
| [`axiom_first_reflection_positivity_theorem_note_2026-04-29`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md) | unaudited |
| [`axiom_first_spectrum_condition_theorem_note_2026-04-29`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md) | unaudited |
| [`axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md) | audited_conditional |
| [`rp_p2_gauge_extension_and_realization_residual_note_2026-05-28`](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md) | audited_conditional |
| [`staggered_dirac_grassmann_forcing_theorem_note_2026-05-07`](STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md) | unaudited |

## Non-circularity

The dynamics in the runner is a generic trace-symmetric dissipator, not a
posited specific map; nothing assumes CAR, the faithful representation, or
`Q = 2/3`. The reduction (A) is finite-dimensional spectral theory; the route
(B) is the standard fact that the exponential of a self-adjoint dissipative
generator is a positive Hermitian contraction.

## No-Go Discipline Gate

- **N1 alternative routes:** direct transfer positivity, Hermitian-record
  dynamics, generic non-Hermitian records, the staggered/Wilson two-step route,
  and future action-native transfer construction are all distinguished.
- **N2 wall independence:** RP and the spectrum condition collapse to one wall,
  `T` positive Hermitian; records-generator trace-symmetry remains a separate
  antecedent.
- **N3 hidden walls:** the note does not assume a concrete dynamics map; the
  Hermitian-record condition is named as an unbuilt derivation target.
- **N4 residual matching:** the staggered/Wilson route and the records route
  both target transfer positivity but with different antecedents; neither is
  used as evidence for the other.
- **N5 rhetoric audit:** "same statement" is scoped to the finite-dimensional
  transfer-operator reduction, not to a derived physical time evolution.
- **N6 partial-closure scan:** the records scaffold is a partial-closure path
  that could avoid the staggered/Wilson import if separately derived.
- **N7 steelman:** a non-Hermitian record channel can defeat the records route;
  that risk is named here and handled by the companion counterexample note.
- **N8 cross-cycle echo:** prior RP notes used two-step positivity in the
  staggered arena; this note preserves that as a distinct import route.

## Next paths this opens

- The single derivation target: show that the framework's records-growth /
  decoherence Lindblad operators are Hermitian (self-adjoint records of
  Hermitian observables) with respect to the retained tracial reference. The
  CP / Kraus half is retained; the Hermiticity of the record operators is the
  sharp checkable piece. If it lands, `T`-positivity -- hence RP, `Hhat >= 0`,
  the `free_sector` CAR forcing, and the matter-attachment -- follow as
  corollaries through the dynamics arena, with no staggered / Wilson import.
- Independently, the import route remains available if the staggered-Dirac
  realization and `g_bare`/Wilson gates are closed by separate retained
  derivations; that is a distinct program and a user-approval question, not a
  prerequisite for the route above.

This is a reduction of the RP / spectrum-condition cascade to one
transfer-positivity target, not a closure.
