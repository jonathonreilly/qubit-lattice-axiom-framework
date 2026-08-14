# Landed status and bounded identity census for the witness invariant `J`

Date: 2026-08-11 (revised 2026-08-14 by review-loop)

Cycle: 981

Claim type: `bounded_theorem`

Audit-status authority: independent audit lane only

Effective status: pipeline-derived only after independent audit ratification
and dependency closure

## Trace gate

```yaml
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: "is J a NEW object, or does it coincide with something the corpus already carries?"
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "extend the typed candidate ledger before making any corpus-wide uniqueness claim"
```

## Status fields

```yaml
claim_id: cycle981_j_landed_invariant_identification
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite pinned-corpus identification census; no branch-local retained-grade proposal"
claim_type_reason: "exact landed-status check, independent finite-group invariance test, and typed comparison over a declared candidate inventory"
audit_required_before_effective_retained: true
bare_retained_allowed: false
audit_status_authority: independent audit lane only
negative_assertion_classes: [bounded_with_named_walls]
packet_primary_runner: scripts/frontier_cycle981_j_landed_invariant_identification_2026_08_11.py
packet_helper_runner: scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py
packet_helper_claim_scope: cycle981_j_landed_invariant_identification
```

## Packet binding

```yaml
hard_landing_packet_helper_mapping:
  j_landed_invariant_identification_cycle981_bounded_theorem_note_2026-08-11:
    - scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py
```

## Result

`J` is landed at the pinned current-main snapshot
`625236e91e1c3ddbfe5aeaa36c7d37a7c9e78b46`: Cycle 980 defines it on the
declared 21-word witness family and checks it in executable evidence. Cycle
981 independently reconstructs the 24 orientation-preserving signed
permutations and verifies all `21 * 24 = 504` action pairs. Thus `J` is a
proper-cubic invariant on the declared 21-word family, with translations
acting trivially after recentering.

This is a bounded mathematical invariant, not a new framework primitive or a
general physical observable. Its exact domain is the pairwise-distinct
semantic quotient of centre-targeting radius-one CNOT/TOF witnesses fixed by
Cycle 980. Repeated operands, arbitrary gate sequences, larger supports,
other gate alphabets, and unrecentered absolute positions are outside this
claim.

The typed identity census finds no coincidence among the eleven enumerated
candidates. That finite negative result does **not** prove that `J` is
corpus-wide unique or “landed-new.” The token index is a discovery surface,
not an exhaustive classification of every semantic invariant in the corpus.

## Exact landed and invariance checks

For a witness word `w`, with centre-relative control displacements `c_i`,

```text
J(w) = ||sum_i c_i||^2.
```

For every proper cubic rotation `R`,

```text
J(R.w) = ||sum_i R c_i||^2 = ||R(sum_i c_i)||^2 = J(w),
```

because each enumerated matrix has determinant `+1` and is orthogonal. A
common translation cancels when the centre is subtracted from every control.
The primary constructs the matrices directly and checks group order, closure,
all 504 invariance pairs, 567 translation/recentring pairs, and orbit-size
spectrum `{3,6,12}`. The checker uses a separate `(axis permutation, sign)`
representation and obtains the same result without importing the primary or
Cycle 980.

The exact finite values are:

| orbit | members | `J` |
|---|---:|---:|
| CNOT | 6 | 1 |
| perpendicular-control TOF | 12 | 2 |
| opposite-control TOF | 3 | 0 |

## A_CANDIDATE_ENUMERATION

All full-body reads use immutable `git show` at the literal current-main pin
`625236e91e1c3ddbfe5aeaa36c7d37a7c9e78b46`, which also supplies the landed
Cycle 980 source. The nine pinned bodies are SHA-256 and Git-blob bound. The
repository-wide token index reports discovery paths only; it is not counted
as a full-body read or an exhaustiveness proof.

Cycle 736 and Cycle 746 are now landed and are therefore included. The later
Cycle 752/753/754/761 paths remain absent at the pin and are recorded only as
presence probes.

| candidate | landed at pin? | native domain -> codomain | native spectrum |
|---|---:|---|---|
| Cycle 980 control arity | yes | witness word -> integer | `{1,2}` |
| Cycle 980 unordered-pair control-Gram sum | yes | witness word -> integer | `{-1,0}` |
| Cycle 719 B-rail occupation `sum(b)` | yes | controller trace -> integer | finite rail occupancy |
| Cycle 719 two-rail token total | yes | controller state -> integer | `{2}` on the declared code |
| `O_h` star shell leverage | yes | six-arm representation -> rational constant | `{3/2}` |
| Cycle 732 cell adjacency cost | yes | least-volume dissection -> integer | `{108,110,...,128}` |
| Cycle 732 228-point cover parity | yes | least-volume dissection -> integer mod 2 | `{0}` |
| Cycle 733 column-subset cost parity | yes | piece/dissection plus column subset -> integer mod 2 | ten laws, one exception |
| Cycle 735 piece-borne charge | yes | least-cost cutting -> integer mod 2 | `{0,1}` |
| Cycle 736 cutting charge space | yes | least-cost cutting -> integer mod 2 | three nonconstant charges up to complement |
| Cycle 746 carrier block-parity triple | yes | target-carrier support -> `(integer mod 2)^3` | `{(0,0,0),(0,1,1)}` |

The bound sources are the [Cycle 980 corroboration](WITNESS_ORBIT_MULTIPLICITY_CYCLE980_BOUNDED_THEOREM_NOTE_2026-08-11.md),
[Cycle 719 controller theorem](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
and its [executable core](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py),
[`O_h` shell leverage](OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md),
[Cycle 732 intake](historic_intake/HISTORIC_PHYSICAL_PARITY_CERTIFICATE_COST_SPECTRUM_CYCLE732_NOTE_2026_08_04_INTAKE_NOTE_2026-08-05.md),
[Cycle 733 intake](historic_intake/HISTORIC_PHYSICAL_COLUMN_FAMILY_PARITY_LAW_FORCED_ORBITS_CYCLE733_NOTE_2026_08_04_INTAKE_NOTE_2026-08-05.md),
[Cycle 735 intake](historic_intake/HISTORIC_PHYSICAL_LEAST_COST_CUTTING_PIECE_CHARGE_CYCLE735_NOTE_2026_08_05_INTAKE_NOTE_2026-08-05.md),
[Cycle 736 charge space](PHYSICAL_CELL_CUTTING_CHARGE_SPACE_CYCLE736_NOTE_2026-08-05.md),
and [Cycle 746 parity licensing](PHYSICAL_CELL_CUTTING_CARRIER_PARITY_LAW_CYCLE746_NOTE_2026-08-08.md).

## B_IDENTIFICATION_TEST

No affine rescaling, value permutation, sign change, or spectrum relabeling is
allowed. Domain and codomain schemas must match before values are compared.
Only the two Cycle 980 neighbours share the witness-word domain:

| candidate | result | first witness | `J` | candidate |
|---|---|---|---:|---:|
| control arity | `DISAGREES` | `TOF(+x,-x->C)` | 0 | 2 |
| unordered-pair control-Gram sum | `DISAGREES` | `CNOT(+x->C)` | 1 | 0 |

The remaining nine candidates are `NOT_COMPARABLE`: they have controller,
representation, cell-dissection, cutting, or carrier-support domains rather
than the declared witness-word domain. In particular, a three-dimensional
charge space or a three-coordinate parity triple does not become identical to
the three-valued integer `J` merely because each surface displays a “three.”

## C_VERDICT

No candidate in the enumerated inventory coincides with
`J(w)=||sum_i c_i||^2`. Therefore this test establishes no cross-lane numeric
bridge. Inventory completeness is false, so corpus-wide landed-newness remains
open.

Even a future 21-row numerical agreement would identify two functions on this
finite shared domain only. It would not identify their physics, turn a
cell-cutting charge into a gate-word observable, supply a probability rule, or
extend either object beyond its declared domain.

## Current Record boundary

The pinned [current minimal-axiom memo](MINIMAL_AXIOMS_2026-06-29.md) is read
to prevent premise drift. Its Record axiom says that records form; a present
record locks one admissible local possibility, no site carries more than one,
records are permanent, only records are readable, readout depends on record
content alone, and an unrecorded site cannot be read.

No Record property is used in the `J` definition, group action, or typed
candidate comparison. Finite additivity, scalar `I`, and `I(empty)=0` are not
used and are not current Record content. The only framework geometry used by
the invariance statement is the pinned Lattice structure, with Cycle 980 as
the direct bounded provenance surface.

## D_CONTROLS

- Nine literal source bodies are read by immutable `git show`, with SHA-256
  and Git-blob pins.
- The 24-element group and all 21 witnesses are reconstructed rather than
  accepted from receipt values.
- The science outcome is not a PASS condition: coincidence, disagreement, or
  clean non-comparability all pass when bookkeeping reconciles.
- The checker imports and executes neither the primary nor Cycle 980. It
  parses the primary as inert text/AST, independently reconstructs values and
  rotations, binds the receipt/cache/note, and rejects hostile mutations.
- No audit verdict, effective status, probability interpretation, framework
  primitive, or axiom is added.

## No-Go Discipline: N1-N8

The bounded negative is only “no coincidence among these eleven typed
candidates.” It is not a corpus-exhaustive uniqueness claim.

### N1 — alternative routes

Four routes were attempted. Exact row-by-row comparison rejects both
same-domain Cycle 980 candidates. Source-native domain typing rejects the nine
cross-domain candidates without value relabeling. The exact-`J` token scan
finds the Cycle 980 definition and its checker but is not promoted to semantic
completeness. Finally, the independent checker rebuilds the witness table and
candidate outcomes without importing the primary.

### N2 — wall independence

The finite witness wall, eleven-candidate inventory wall, source-native type
wall, and pinned-snapshot wall are independent. Closing the 21-word
comparison does not close the candidate inventory; adding candidates does not
enlarge the witness domain; and snapshot presence does not create a shared
domain.

### N3 — hidden walls

The search lexicon, nine-body read cap, no-rescaling normalization, semantic
quotient, radius-one support, CNOT/TOF alphabet, recentering convention, and
proper-cubic group are explicit. No claim covers arbitrary gate objects,
multi-gate histories, unrecentered positions, nonlinear identifications, or
semantic candidates not captured by the inventory.

### N4 — residual matching

The two disagreement witnesses attack exact equality only on the common
21-word domain. Type mismatches attack comparability only; they do not prove
physical unrelatedness. Absent later cell-cutting paths attack only presence
at the pin. None of these residuals is used to infer corpus-wide uniqueness.

### N5 — rhetoric audit

The primary cache lands substantive `per_element:`, `per_site:`, `per_mode:`,
`per_block:`, and `lattice_wide:` lines. The result consistently says
“enumerated inventory,” “bounded invariant,” and “landed-newness open.” It
does not call `J` a universal observable, conserved charge, or new primitive.

### N6 — partial-closure paths

The candidate ledger can grow mechanically without a new axiom. A future
candidate with the same domain can be compared row by row. A larger gate
family can receive a new invariant-extension theorem. A semantic search over
all indexed hits remains an open finite curation task.

### N7 — steelman

A differently named corpus quantity may restrict to `J` on these 21 words; an
affine or nonlinear map may relate another spectrum if such normalization is
physically justified; and a future landed cell-cutting surface may supply an
explicit bridge. None is excluded. Conversely, a matching three-valued
spectrum alone is not an identity proof.

### N8 — cross-cycle echo

Cycle 980 owns the definition, invariant separator, and exact finite domain.
Cycles 736 and 746 own different cutting/carrier domains and are included only
as typed candidates. Cycle 981 adds the current-main landed-status check,
independent group-action corroboration, and bounded identity ledger; it does
not restate any of those upstream claims as novel.

## Artifacts and reproduction

Primary:

- [`frontier_cycle981_j_landed_invariant_identification_2026_08_11.py`](../scripts/frontier_cycle981_j_landed_invariant_identification_2026_08_11.py)
- [`j_landed_invariant_identification_cycle981_receipt_2026_08_11.json`](../outputs/j_landed_invariant_identification_cycle981_receipt_2026_08_11.json)
- [`frontier_cycle981_j_landed_invariant_identification_2026_08_11.txt`](../logs/runner-cache/frontier_cycle981_j_landed_invariant_identification_2026_08_11.txt)

Independent checker:

- [`frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py`](../scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py)
- [`j_landed_invariant_identification_cycle981_independent_check_receipt_2026_08_11.json`](../outputs/j_landed_invariant_identification_cycle981_independent_check_receipt_2026_08_11.json)
- [`frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.txt`](../logs/runner-cache/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.txt)

```bash
python3 scripts/cached_runner_output.py --refresh --timeout-sec 300 scripts/frontier_cycle981_j_landed_invariant_identification_2026_08_11.py
python3 scripts/cached_runner_output.py --refresh --timeout-sec 300 scripts/frontier_cycle981_j_landed_invariant_identification_independent_check_2026_08_11.py
```
