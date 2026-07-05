# AC_phi_lambda Sub-Admission (iii): Species-Bridge Decomposition Under the Realized-State Primitive

**Date:** 2026-06-11
**Type:** bounded_theorem (decomposition / relocation)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets,
predicts, and estimates no audit verdict and edits no registry.
**Primary runner:**
[`scripts/frontier_acphilambda_species_bridge_realized_state_2026_06_11.py`](../scripts/frontier_acphilambda_species_bridge_realized_state_2026_06_11.py)
(`TOTAL: PASS=19 FAIL=0`)
**Runner cache:**
[`logs/runner-cache/frontier_acphilambda_species_bridge_realized_state_2026_06_11.txt`](../logs/runner-cache/frontier_acphilambda_species_bridge_realized_state_2026_06_11.txt)
**Axiom-surface update:** 2026-07-05 — current axiom surface is the four-axiom
memo `MINIMAL_AXIOMS_2026-06-29.md`; this note had no live
`MINIMAL_AXIOMS_2026-06-05.md` axiom-premise citation to re-point, and no
Record-axiom orbit/outcome wording is used as live axiom text. No claim is
strengthened; this is citation-surface alignment only.

## Statement

The Tier-A registry
([`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md),
`meta`) carries AC_phi_lambda sub-admission **(iii)**: the abstract-sector ->
physical-species **bridge**, described there as "an interpretive bridge, akin
to the abstract-su(3) -> physical-color gap," with the R1b anchor sentence
(owner review record on PR #3428): *"the hw=1 triplet is the physical
generation sector."*

This note decomposes that bridge, using the newly approved
`realized_state_primitive`
([`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md),
approved framework primitive, `meta` ledger row), into three named components
and shows where each lives:

- **(a) Naming** — the bijection between the abstract sector labels and the
  species names (e/mu/tau). Already excluded as an input by the registry's
  de-naming row; verified vacuous here (runner A2: every registered invariant
  is fixed by all 6 relabelings).
- **(b) Registration** — *which abstract sector carries which registered mass
  pattern* is a **registration statement**: given the standing supplied
  readout context (the central-sector resolution `{P_k}` of the
  generation-monitored family; guardrail G1 of
  [`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05`](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md),
  `meta`), the sector-to-pattern assignment is evaluated **pointwise at the
  realized state**, is uniquely determined by the records for a nondegenerate
  registered pattern (runner B3: exactly 1 of 6 assignments survives the
  records), and is certified by the primitive's counterfactual test as
  **registered data, not derivation output** (runner B5: a second
  law-admissible realized configuration permutes the assignment). No
  sector-selection rule is needed or supplied.
- **(c) Structural residual** — what genuinely cannot be a registration
  statement is the **carrier-locus selection**: why the generation-monitored
  family is supported on the hw=1 triplet at all. That is a pre-context
  operator-class fact (runner C1/C2: the naive dispersion is hw-blind across
  all 8 corners with grading (1,3,3,1); the Wilson operator distinguishes
  hw=0, not hw=1), and it is the **same named chirality-gate family** already
  tracked at
  [`KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02`](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md)
  (`retained_bounded`) and consolidated by the carrier note
  `FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31` (`unaudited`; its
  two locus counterfactuals are re-verified independently by this note's
  runner) — **not a new input**. The hw=1-vs-hw=2 face of the locus is the
  compensated complementation class named by
  `ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09`
  (`open_gate`; exchange + C3-commutation re-verified, runner C3).

**R1b therefore splits.** "The hw=1 triplet is the physical generation
sector" = (i) a **tautology given the supplied context** — the supplied
`{P_k}` already live under the hw=1 projector, so "the registered sectors are
sectors of the hw=1 triplet" is a context datum, not additional content
(runner B4: `P_k <= P_hw1`, `sum_k P_k = P_hw1` in the explicit `C^8`
embedding) — **plus** (ii) the carrier-locus chirality gate (why THAT context
family; component (c)) **plus** (iii) the separate, already-tracked
empirical-anchor step (matching the registered pattern to measured values,
"matched like the masses," guardrail G3). The answer to the framing question
is **(iii)-partially-each**: part dissolves into the supplied-context premise,
and the surviving genuinely-additional content is exactly the already-named
chirality gate plus the standing readout-context input plus the external
empirical anchor. **No admitted content beyond named, already-tracked items
survives in sub-admission (iii) on this surface.**

## Why the realized-state primitive moves the generation case and not the color case

The registry's analogy clause ("akin to the abstract-su(3) -> physical-color
gap") is now sharpened into an exact **disanalogy**:

1. **The color gap.** The
   `CL3_COLOR_AUTOMORPHISM_THEOREM` context row (`unaudited` on the current
   ledger) states its own bridge requirement: the identification "the 3D
   symmetric base subspace **is** the physical SM color carrier SU(3)_c" is a
   deferred representation-match requirement. Intra-color sector labels are
   gauge-moved: conjugating the frame leaves every registered invariant
   (characters/traces of words) fixed while moving the sector projectors
   (runner D2). On the landed (unaudited, contrast-only) single-frame
   color-einselection surface
   `COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09`),
   even a *named* color record frame (itself an admission on the
   `retained_no_go` record-formation ground) erases per-sector color data in
   one step for an amplitude-dense unitary (runner D1: `T_U = J/3`, unique
   stationary vector uniform). **There is no per-sector color record stack for
   the primitive to evaluate pointwise.** The color bridge content is
   structural (a rep match), not registrational; the realized-state primitive
   leaves it untouched.
2. **The generation case.** The generation sectors are exactly what the mass
   records register: the monitored family is sector-diagonal in the supplied
   context, the registration map `D` is faithful on it and preserves
   per-sector data exactly (runner B1, D1b), and the per-sector pattern values
   are durable registered data. The species identification (stripped of
   naming) is **constituted in the records** — and the primitive's pointwise
   clause is precisely the license to evaluate it there without a
   state-selection rule. This is the structural asymmetry: generation has an
   in-framework record stack carrying per-sector data; color does not.

## Derivation (runner map)

Concrete model: the corner cube `{0,1}^3` with C3[111]; the hw=1 triplet
carrier `C^3` embedded in `C^8 = (C^2)^{x3}`; the K-real circulant monitored
family `M(a,B,delta) = aI + bJ + conj(b)J^2`, `b = B e^{i delta}`, with
**arbitrary admissible placeholder values** (never matched values; `r` and
`delta` are never assigned their lane settings here — dial discipline).

- **A1/B0/B0b** — carrier, free C3 orbit, real distinct registered pattern,
  supplied context `{P_k}` resolves the carrier and diagonalizes the family.
- **A2 (naming vacuity)** — all 6 label bijections fix every registered
  invariant: component (a) carries zero physical content.
- **B1/B2 (registration)** — `D(M) = M`; inter-sector coherence of a probe is
  stripped (canonical-principle behavior); the identification map
  `iota: sector -> registered value` is reconstructed pointwise from
  registered data (`tr(P_k M)`) with no further rule.
- **B3 (rigidity)** — exactly 1 of the 6 candidate value-to-sector
  assignments is consistent with the records: given (context, records) the
  identification has **zero residual freedom**; the 6-fold orbit is exactly
  the vacuous naming.
- **B4/B4b (tautology-given-context)** — carrier membership of the registered
  sectors is a context datum in the explicit `C^8` embedding; the embedded
  C3[111] restricts to the triplet 3-cycle.
- **B5 (counterfactual test)** — `delta -> -delta` is equally law-admissible
  and permutes the assignment (k=1,2 exchange): by the primitive's policing
  clause the assignment is **registered data**, exactly the classification
  the decomposition asserts.
- **C1/C2/C3 (the genuine residual)** — no record-side statement picks the
  locus: the dispersion counterfactuals are operator-class facts prior to any
  readout context; hw=1<->hw=2 is the compensated complementation class.
- **D1/D1b/D2 (color contrast)** — single-frame color erases per-sector data;
  generation registration preserves it; color sector labels are gauge-moved
  with registered invariants fixed.
- **E1/E2 (hostile guards)** — see below.

## Hostile-guard

- **(a) "You have just renamed the bridge as 'supplied context'."** No. The
  supplied readout context is not introduced by this note: it is the standing
  G1 input every record-readout lane already pays, tracked at the canonical
  principle note, together with the G2 coarseness predicate (K-reality — the
  standing pin, already sub-admission (i)'s face). The decomposition has
  falsifiable content beyond relabeling: it proves (runner E2) a **strict
  reduction of the assignment freedom from 6 to 1** — pre-decomposition the
  bridge was tracked as carrying an unquantified interpretive degree of
  freedom; post-decomposition, given the standing context plus the realized
  records, the identification is rigid, and the entire 6-fold orbit is the
  already-excluded vacuous naming. What remains is itemized against
  *pre-existing named* inputs (chirality gate; G1/G2 context; empirical
  anchor), each separately tracked before this note. A renaming would add a
  new premise; this decomposition adds none.
- **(b) "Pointwise evaluation cannot constitute an identification between an
  abstract rep label and a PDG species — that is a comparator import."**
  Agreed as stated — and that is not the claim. The registration statement
  identifies the abstract sector with the **record-stack sector** (the sector
  carrying the realized registered pattern); both sides are
  framework-internal. The match of the registered pattern to PDG values
  remains the **separate, already-tracked empirical-anchor step**, exactly as
  for the masses themselves (guardrail G3: registered patterns are matched,
  not derived). The runner contains no PDG number and no matched value; the
  construction is equivariant in the supplied pattern (runner E1: it
  reconstructs whatever admissible `(a,B,delta)` is supplied). The phrase
  "charged-lepton pattern" in the anchor sentence functions as a lane
  address, and the species *names* are vacuous per the de-naming row.
- **(c) "The registration story presupposes the very family it identifies."**
  Correct — and that is the content of component (c): the choice of the
  monitored family (the carrier locus, the operator class) is exactly what
  cannot be a registration statement, and it is named, not hidden. The note
  relocates it onto the pre-existing chirality gate rather than absorbing it.
- **(d) "The counterfactual test cuts against you: the assignment is
  state-contingent, so you have derived nothing."** The decomposition does
  not claim to derive the assignment; it claims the assignment **need not be
  derived** — the primitive classifies it as registered data, which is
  precisely how the masses themselves are already handled. The would-be
  missing "rule" for which sector carries the pattern is shown to be a
  non-requirement.

## Boundary

- This note does **not** edit the Tier-A registry, retire or re-grade any
  admission, change the admission count, unbound any consumer, or move
  AC_phi_lambda or any sub-admission to another class. Any registry
  consequence of this decomposition is named here as **available to a future
  gated owner-approved lane**, after independent audit of this note.
- It does **not** derive the carrier locus, the readout context, the K-reality
  predicate, a record-formation dynamics (G4), the value of `r`, the value of
  `delta`, or any species mass; it does **not** select `r=1/2` (dial
  discipline: sector data, never forced).
- It does **not** close, complete, or finally settle sub-admission (iii); it
  decomposes it on the current landed surface and names the surviving
  content. The cross-type alignment of the up/down/lepton mass bases
  (CKM/PMNS structure) is the registry's separately listed third non-naming
  residual and is untouched here.
- The color-einselection contrast citations are `unaudited` source proposals
  used as **contrast surface**, with the specific arithmetic facts replicated
  inside this note's runner; nothing here is conditional on their audit
  outcome. The color disanalogy claim is correspondingly bounded: it rests on
  the retained color note's own deferred-bridge wording, the gauge-move fact
  (runner D2), and the replicated single-frame arithmetic (runner D1).
- The rigidity statement (B3) is for a nondegenerate registered pattern;
  degenerate patterns leave a residual stabilizer subgroup of the naming
  orbit (still vacuous on registered invariants, runner A2).
- The runner's `C^8` embedding uses the corner-cube/Hamming structure of the
  retained substep-3 surface; it is a finite verification model, not a
  re-derivation of that surface.

## Honest-auditor-read

What is genuinely new here: (1) the exact formalization of the R1b anchor as
a registration statement and its split into
tautology-given-context + chirality-gate + empirical-anchor, with each piece
verified finite-dimensionally; (2) the certified use of the realized-state
primitive's pointwise/counterfactual clauses to reclassify the
"which-sector-carries-the-pattern" content as registered data (a move not
available before the primitive's approval); (3) the sharpened
color-vs-generation disanalogy (registrational vs structural bridge content).
What is *not* new: every input it lands on (chirality gate, G1/G2 context,
empirical anchor, de-named labeling) was already named and tracked. The
honest summary is a **relocation with zero new premises and one dissolved
pseudo-premise** (the apparent need for a sector-assignment rule), not a
retirement of sub-admission (iii). The next path this opens: the surviving
structural content of (iii) is now co-located with the recurring chirality
gate, so a single advance on that gate (forcing the first-order chiral
operator class from the bosonic qubit substrate) would move sub-admission
(iii)'s structural residual and the generation-ID/Q-gate surface together.

## Dependencies (current-main status reviewed 2026-07-05; statuses are quoted, not set)

| id | role | effective_status |
|---|---|---|
| [`realized_state_primitive`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) (axiom_premise node; note row) | the pointwise-evaluation license + counterfactual test | `meta` (approved framework primitive; chain-satisfying) |
| [`admitted_input_registry_tier_a_note_2026-05-23`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md) | the sub-admission (iii) wording + de-naming row | `meta` |
| [`record_outcome_observable_principle_canonical_proposal_note_2026-06-05`](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md) | G1-G4 guardrails; registration map | `meta` |
| [`three_generation_observable_theorem_note`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) | the C^3 / hw=1 triplet observable algebra | `retained` |
| [`staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17`](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md) | corner-cube Hamming orbit structure | `retained` |
| [`staggered_dirac_substep3_species_reduction_bridge_narrow_theorem_note_2026-05-16`](STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md) | species-reduction surface | `retained_bounded` |
| [`koide_generation_id_cl3_grade1_bridge_narrow_theorem_note_2026-06-02`](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md) | the named chirality gate (component (c) target) | `retained_bounded` |
| `cl3_color_automorphism_theorem` | color-contrast wording; not load-bearing for the registration decomposition | `unaudited` (context only) |
| [`record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md) | record-frame-as-admission ground (color contrast) | `retained_no_go` |
| `acphilambda_hw_complementation_equivariance_support_note_2026-06-09` | hw=1/hw=2 compensation class (support; facts re-verified here) | `open_gate` |
| `flavor_carrier_from_axioms_momentum_forced_2026-05-31` | locus counterfactuals (context; facts re-verified here) | `unaudited` |
| `color_einselection_pointer_frame_fork_is_a_unistochastic_irreducibility_criterion_narrow_theorem_note_2026-06-09` | color contrast surface (arithmetic replicated) | `unaudited` |

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the single
status authority.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [acphilambda_hw_complementation_equivariance_support_note_2026-06-09](ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md)
- [flavor_carrier_from_axioms_momentum_forced_2026-05-31](FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md)
- [color_einselection_pointer_frame_fork_is_a_unistochastic_irreducibility_criterion_narrow_theorem_note_2026-06-09](COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md)
