---
claim_id: menu_identity_i2_is_not_record_i_empty_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "One-site type-separation of two homonymous symbols named I. The menu identity I_2=diag(1,1) in M_2(C) has trace 2 and is the sum of every binary effect menu. The Record readout I is a scalar count of record collections with I(empty)=0. The objects are unequal as rationals and have different types. Identifying them is an extra dictionary, not a current-axiom or August 9 consequence. The note adopts no dictionary, does not claim Born is false, does not force r=1/2, and does not adopt L_phys."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/menu_identity_i2_is_not_record_i_empty_2026_08_13.py
---

# Menu Identity `I_2` Is Not Record `I(empty)=0`

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-site symbol/type separation between the operator identity
used by binary menus and the Record scalar readout of the empty collection.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/menu_identity_i2_is_not_record_i_empty_2026_08_13.py`](../scripts/menu_identity_i2_is_not_record_i_empty_2026_08_13.py)

## Result Up Front

Two different objects in the current surfaces are both written with the letter
`I`.

1. **Menu identity.** The operator identity `I_2=diag(1,1)` in `M_2(C)`
   satisfies `Tr(I_2)=2`. A binary menu `{P, I_2-P}` of effects sums to
   `I_2`.
2. **Record readout.** The Record axiom supplies a scalar readout `I` of
   finite collections of pairwise-disjoint records, with `I(empty)=0` in
   `Z`.

They are not the same object. `Tr(I_2)=2` is not `I(empty)=0`, even after
both numbers are read as rationals. One object is a `2 times 2` matrix; the
other is a scalar count. Quoting the two source sentences does not create a
dictionary that identifies them. This note displays the mismatch and stops.

The result is a type-separation theorem. It does not claim that the Born
trace form is false. It does not force a weight `r=1/2`. It does not adopt a
physical length `L_phys`. No canonical axiom is edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The rational inequality Tr(I_2)=2 != 0=I(empty) and the matrix-versus-scalar type split are proved on declared one-site objects, while any later dictionary, Born-weight identification, or physical-length adoption remains extra and is not taken."
trace_class: negative_route_pruning
target_claim_id: menu_identity_versus_record_readout_i
target_blocker_text: "the menu identity I_2 is not the Record readout I(empty)=0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed rational mismatch and type split; no dictionary, Born negation, r=1/2 forcing, or L_phys adoption"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site, with local algebra `M_2(C)`.

**Menu identity.** Write

`I_2 = ((1, 0), (0, 1))` in `M_2(C)`.

Its trace is the rational

`Tr(I_2)=1+1=2`.

For a rank-one projector `P` in `M_2(C)`, the complementary effect is
`I_2-P`, and the binary menu `{P, I_2-P}` is a two-member family of effects
summing to `I_2`. This is the same operator identity used by the parent
binary/ternary scaled-projector theorem: menus are families of effects
summing to `I_2`.

**Record readout.** The current axiom memo states that only records are
readable, that a readout value is determined by record content alone, and
that for any finite collection of pairwise-disjoint records the scalar
readout `I` is additive, with `I(empty)=0`. The empty collection is a
collection of records. Its readout is the integer `0`, equivalently the
rational `0`.

These two objects share a letter and nothing else required by the quoted
sources.

## Theorem 1 — Unequal Even As Rationals

`Tr(I_2)=2` and `I(empty)=0` are both elements of `Q`. They are unequal:

`2 != 0`.

The hostile predicate `Tr(I_2)=I(empty)` is therefore false. No further
analytic continuation, dictionary, or units conversion is used. The identity
gates that compare the two symbols call the explicit maps `tr_I2()` and
`I_empty()` in the companion runner.

## Theorem 2 — Different Types

`I_2` is a `2 times 2` matrix. `I(empty)` is a scalar count.

A matrix in `M_2(C)` is not an element of `Z`. A scalar count is not an
operator that binary menus can sum to. Type disagreement is independent of
the rational inequality in Theorem 1: even if someone renamed the symbols,
one object still has shape `(2,2)` and the other has no matrix indices.

## Theorem 3 — Quoted Sources Do Not Identify Them

Quote Record from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar
> readout `I` is additive, with `I(empty)=0`.

Quote the August 9 parent
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md):

> The three compressed rank-one projections are scaled rank-one qubit effects
> summing to `I_2`.

and

> A menu is a finite family of nonzero members of `S` summing to `I`.

The parent uses both `I` and `I_2` for the operator identity of a menu. The
Record axiom uses `I` for a scalar readout of record collections. Juxtaposing
those sentences does not identify the menu identity with Record `I`.
Identifying the menu identity with Record `I` is extra.

## Theorem 4 — Display The Mismatch; Adopt No Dictionary

The mismatch is:

| Symbol as written | Object | Value or shape |
|---|---|---|
| `I_2` | operator identity in `M_2(C)` | matrix `diag(1,1)`, `Tr=2` |
| `I` in a menu sum | same operator identity (parent usage) | family of effects summing to `I_2` |
| `I(empty)` | Record scalar readout of the empty collection | `0` in `Z` |

This note displays that table. It does not adopt a dictionary

`I_2 := I(empty)`, `I := Tr(I_2)`, or `I(empty) := 2`.

It does not claim that the Born trace form is false. The parent theorem
remains a conditional one-site implication from a supplied grading and
eligible menus to a unique density-matrix trace form. Homonym collision of
the letter `I` is not a counterexample to that implication.

## Theorem 5 — Do Not Force `r=1/2`; Do Not Adopt `L_phys`

Nothing in Theorems 1--4 selects a Koide or Born weight `r=1/2`. The binary
menu `{P, I_2-P}` is an operator resolution; its existence does not force
equal outcome grades, a unique mixing weight, or `r=1/2`.

Nothing in Theorems 1--4 introduces or adopts a physical length `L_phys`.
No continuum path length, valley length, or other dimensionful scale is
identified with `Tr(I_2)`, with `I(empty)`, or with their difference.

Those refusals are load-bearing. Closing the homonym does not license a
weight-fixing step and does not license a length primitive.

## Proof-Obligation Graph

| Obligation | Role | Disposition |
|---|---|---|
| compute `Tr(I_2)` exactly | Theorem 1 | `1+1=2` in `Q` |
| read `I(empty)` from Record | Theorem 1 | quoted `0` in `Z`, hence `0` in `Q` |
| reject `Tr(I_2)=I(empty)` | mutation | `2 != 0` |
| exhibit matrix versus scalar types | Theorem 2 | `I_2` has shape `(2,2)`; `I(empty)` is a scalar |
| quote both sources without adding a map | Theorem 3 | Record and August 9 sentences displayed |
| refuse a dictionary and refuse Born negation | Theorem 4 | explicit non-adoption |
| refuse `r=1/2` and refuse `L_phys` | Theorem 5 | explicit non-adoption |
| edit a canonical axiom | out of scope | not done |

## Independent Adversarial Checks

The runner constructs `I_2` as an exact rational matrix, computes `tr_I2()`
by summing the diagonal, and returns `I_empty()` as the exact rational `0`.
Every identity-gate comparison calls those two maps. A rank-one projector
`P` and its complement `I_2-P` are added in `M_2(Q)` and compared with
`I_2`. The hostile predicate `tr_I2()==I_empty()` is required to fail.

The runner also checks that the source note quotes both parents, states
Theorems 1--5, refuses a dictionary, refuses a Born-false claim, refuses
`r=1/2`, refuses `L_phys`, and does not mutate the canonical axiom memo.

## Relation To The Current Axioms

[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
one-site algebraic presentation `M_2(C)` and the Record scalar readout with
`I(empty)=0`. It does not say that the operator identity of a menu is that
readout. The August 9 parent supplies the menu-sum convention. Neither
source is edited here.

No hypothetical axiom wording is proposed. The sufficient next step, if a
later note wants a single letter for both objects, is to adopt an explicit
dictionary and justify it. This note does not take that step.

## No-Go Discipline Gate

The negative claim is only that the two homonymous symbols are not already
the same object. The gate does not certify a Born no-go.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Rational identification | set `Tr(I_2)=I(empty)` in `Q` | Theorem 1: `2 != 0` | **ATTEMPTED** |
| Type identification | treat the matrix `I_2` as the scalar count `I(empty)` | Theorem 2: shape `(2,2)` versus a scalar | **ATTEMPTED** |
| Quotation dictionary | read Record and August 9 as already identifying the symbols | Theorem 3: the quoted sentences name different objects | **ATTEMPTED** |
| Silent dictionary | adopt `I_2 := I` or `I := Tr(I_2)` to remove the clash | Theorem 4 refuses the dictionary | **ATTEMPTED** |
| Born negation | treat the homonym as a counterexample to the parent trace form | Theorem 4 refuses the Born-false claim | **ATTEMPTED** |
| Weight forcing | read a binary menu as forcing `r=1/2` | Theorem 5 refuses the forcing | **ATTEMPTED** |
| Length adoption | read `2` or `0` as a physical length `L_phys` | Theorem 5 refuses the adoption | **ATTEMPTED** |

None of these routes supports "Born is false" or "an axiom update is
necessary."

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| rational inequality / type split | no: two rationals can differ while sharing a type | no: two types can differ while some traces coincide | independent |
| source quotation / dictionary | no: quoting two sentences does not write a map | no: a later map would be extra structure, not a quotation | independent |
| homonym display / Born form | no: unequal symbols do not refute a trace grade | no: a density-matrix grade does not identify `I_2` with `I(empty)` | independent |
| homonym display / `r=1/2` | no: `2 != 0` does not select a weight | no: a weight does not identify the two `I` symbols | independent |
| homonym display / `L_phys` | no: the mismatch introduces no length | no: a length would be a new object | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `I_2` | explicit `2 times 2` identity matrix; not Record readout |
| `I(empty)` | explicit Record scalar; not an operator |
| `Tr` | ordinary matrix trace over `Q` |
| binary menu `{P, I_2-P}` | exact operator resolution; grades unused |
| "dictionary" | refused extra identification; not present in the axioms |
| `r=1/2` | refused weight; not derived |
| `L_phys` | refused length; not adopted |
| observations or empirical frequencies | none |

No continuity assumption, fitted value, or selected density matrix is hidden.

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md:82-84`](MINIMAL_AXIOMS_2026-06-29.md) | scalar readout `I` additive with `I(empty)=0` | exact current wording only; no menu-identity conclusion borrowed |
| [`docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md:32-33`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md) | effects summing to `I_2` | menu-identity usage only |
| [`docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md:77`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md) | a menu is a finite family of nonzero members of `S` summing to `I` | parent letter `I` for the same operator identity; not Record readout |

No citation is used as authority for the rational inequality `2 != 0`; that
is proved here and checked by the runner.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | diagonal entries of `I_2` and the empty-collection readout | no classification of every symbol named `I` in the repo |
| per site | one `M_2(C)` site | no composite readout theorem |
| per mode | the identity-versus-empty-readout pair only | no spectral-mode exhaustion |
| per block | the two-symbol homonym only | no Born/Record/history closure |
| lattice-wide | not executed | no lattice-wide dynamics or no-go |

### N6 — live partial-closure paths

1. A later note may adopt an explicit dictionary and justify it from
   retained structure. That map is not present now.
2. The parent frame-lift theorem remains a live conditional derivation of
   the Born trace form on the scaled domain.
3. Binary-menu grades, if derived, remain free of any `r=1/2` forcing from
   this homonym.
4. Physical scales, if derived, must be introduced as their own objects,
   not by renaming `I_2` or `I(empty)` to `L_phys`.

### N7 — hostile steelman

> The letter `I` is used for the menu sum and for Record readout, so the
> framework already treats them as one quantity. Then `Tr(I_2)` should equal
> `I(empty)`, or else the Born form that normalizes menus to `I_2` would be
> false.

This steelman is rejected at the first step. Shared spelling is not an
identification. The predicate `Tr(I_2)=I(empty)` fails, and the parent Born
implication is not thereby refuted.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| parent menus sum to the operator identity | August 9 writes both `I` and `I_2` for that operator | keep the operator identity typed as a matrix |
| Record additivity | the axiom memo fixes `I(empty)=0` as a scalar count | keep the empty readout typed as a scalar |
| letter collision | this note | display the mismatch; adopt no dictionary |

**Gate disposition:** PASS for (i) `Tr(I_2)=2 != 0=I(empty)`, (ii) the
matrix-versus-scalar type split, and (iii) the refusal to treat quotation as
a dictionary. FAIL / DO NOT SHIP for "Born is false," "an axiom update is necessary,"
"force `r=1/2`," or "adopt `L_phys`."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | exact semantic baseline | supplied; no edit |
| August 9 menu-sum convention | source of the operator identity `I_2` | explicit parent |
| matrix trace over `Q` | Theorem 1 | definition-level mathematics |
| matrix-versus-scalar typing | Theorem 2 | definition-level mathematics |
| dictionary identifying the two `I` symbols | refused | not adopted |
| Born-false claim | refused | not made |
| weight `r=1/2` | refused | not forced |
| physical length `L_phys` | refused | not adopted |
| observed probabilities, frequencies, fits | none | not used |

The exact advance is a symbol/type theorem. It does not move TOE percentages
by itself because it derives no new physical interface. It makes the next
update decision testable: keep the two objects distinct, or adopt an explicit
justified dictionary; do not silently read `I_2` as `I(empty)`.

## Review Record

This source is stacked on the parent frame-lift theorem because that parent
is the current menu-identity usage being separated from Record readout.
Independent audit remains required before any effective status may change.
No `review-loop` was invoked in producing or self-reviewing this artifact.
