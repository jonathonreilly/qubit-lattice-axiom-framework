---
claim_id: pvm_luders_instrument_produces_born_weights_on_that_pvm_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Conditional one-qubit matching theorem. On the declared two-outcome PVM {P,Q} with P=diag(1,0) and Q=I-P, the Born-on-this-PVM weights K(sigma,P)=Tr(sigma P) and K(sigma,Q)=Tr(sigma Q) are the exact Fractions 1/2 and 3/5 on the named densities rho_*=I/2 and rho=diag(3/5,2/5), are affine on the midpoint mix, and become certain after a declared Lüders update on a P outcome. The four axioms do not name this PVM or the Lüders map. The matching sentence that the instrument is a PVM Lüders readout is an explicit extra input. The note does not adopt Lüders as an axiom, does not replace the 2026-08-09 frame-lift uniqueness theorem, and does not classify other kernels."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/pvm_luders_instrument_produces_born_weights_on_that_pvm_2026_08_13.py
---

# A Declared PVM Lüders Instrument Produces Born Weights On That PVM

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-qubit algebra on one declared two-outcome PVM and one
declared Lüders update map. The matching of that instrument class to the
framework is an extra input.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/pvm_luders_instrument_produces_born_weights_on_that_pvm_2026_08_13.py`](../scripts/pvm_luders_instrument_produces_born_weights_on_that_pvm_2026_08_13.py)

This dispatch writes no runner cache.

## Result Up Front

Fix one qubit, the projectors

`P = diag(1, 0)`, `Q = I − P = diag(0, 1)`,

and the declared PVM `M = {P, Q}`. On a density `σ` the Born-on-this-PVM
weights are

`K(σ, P) := Tr(σ P)`, `K(σ, Q) := Tr(σ Q)`.

The declared extra instrument, not an axiom, is the Lüders update

`L(σ, P) := P σ P / Tr(σ P)` whenever `Tr(σ P) > 0`.

On the named densities `ρ_* = I/2` and `ρ = diag(3/5, 2/5)` those weights
are the exact Fractions `1/2` and `3/5`, they add to one, and they are
affine at the midpoint mix. After a `P` outcome the same declared update
returns `P`, so a second readout of this PVM is certain. The current
Admissibility and Record sentences do not name `{P, Q}` or the Lüders map.
Conditional on the extra matching “the instrument is a PVM Lüders readout”,
the weights on this PVM are those Born numbers.

This is physical extra matching of one named instrument class. It does not
replace the 2026-08-09 uniqueness theorem for a menu-independent low-arity
grading. It does not classify every kernel. It does not adopt Lüders as an
axiom. No canonical axiom is edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: extra_matching
target_claim_id: pvm_luders_instrument_produces_born_weights_on_that_pvm
target_blocker_text: "match one named instrument class to Born weights on that declared PVM"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Keep the PVM Lüders matching extra; do not promote it into axiom text."
conditional_surface_status: "exact Fractions on the named one-qubit PVM and densities, conditional on declaring that PVM and the Lüders map"
hypothetical_axiom_status: "candidate consequence map only; no canonical axiom edit"
admitted_observation_status: null
claim_type_reason: "The one-qubit traces, affinity, and repeatability identities are exact, but the identification of the physical instrument with this PVM Lüders readout is an extra matching sentence not supplied by the four axioms."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site with Hilbert space `C^2`. Write

`I = diag(1, 1)`,
`P = diag(1, 0)`,
`Q = I − P = diag(0, 1)`.

The declared PVM is the two-outcome resolution `M = {P, Q}`. The named
densities are

`ρ_* = I/2 = diag(1/2, 1/2)`,
`ρ = diag(3/5, 2/5)`.

The Born-on-this-PVM kernel is the pair of exact traces

`K(σ, P) := Tr(σ P)`, `K(σ, Q) := Tr(σ Q)`.

The declared Lüders map on a `P` outcome is

`L(σ, P) := P σ P / Tr(σ P)` when `Tr(σ P) > 0`.

Both maps are extra typed inputs of this note. They are not read out of
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

The 2026-08-09 parent
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md)
is a different theorem: a menu-independent grading on the scaled rank-one
and scalar-identity domain, normalized on every binary and ternary nonzero
resolution, has a unique density-matrix trace form on that domain. This
note does not improve, replace, or re-prove that uniqueness statement. It
does not launch a dimension-two frame-function argument.

## Proof-Obligation Graph

| Obligation | Role | Disposition |
|---|---|---|
| evaluate `K` on `ρ_*` and `ρ` | Theorem 1 | exact `Fraction` traces below |
| additivity `K(σ,P)+K(σ,Q)=1` | Theorem 1 | exact, because `P+Q=I` and `Tr(σ)=1` |
| midpoint affinity | Theorem 2 | exact on `σ_mix=(ρ+ρ_*)/2` |
| Lüders repeatability | Theorem 3 | exact matrix identity `L(ρ,P)=P` |
| axiom text does not name the PVM or Lüders | Theorem 4 | quoted sentences below |
| matching sentence remains extra | Theorem 4 | declared, not derived |
| no axiom adoption and no parent replacement | Theorem 5 | explicit non-claims |

## Theorem 1 — Born Numbers On The Declared PVM

Because `ρ_*` and `ρ` are diagonal in the same basis as `P`,

`K(ρ_*, P) = Tr(ρ_* P) = 1/2`,
`K(ρ, P) = Tr(ρ P) = 3/5`.

The complementary weights are

`K(ρ_*, Q) = 1/2`,
`K(ρ, Q) = 2/5`.

For either named density `σ`, cyclicity and `P+Q=I` give

`K(σ, P) + K(σ, Q) = Tr(σ(P+Q)) = Tr(σ) = 1`.

All values are exact `Fraction` identities. No fitted scalar is used.

## Theorem 2 — Affinity In The Density

Let `λ = 1/2` and

`σ_mix = (ρ + ρ_*)/2 = diag(11/20, 9/20)`.

Then

`K(σ_mix, P) = Tr(σ_mix P) = 11/20`

and

`(K(ρ, P) + K(ρ_*, P))/2 = (3/5 + 1/2)/2 = 11/20`.

Thus `K(·, P)` is affine on this midpoint. The same arithmetic with `Q`
gives `9/20` on both sides.

## Theorem 3 — Repeatability After The Declared Lüders Map

The `P` outcome has positive Born weight on `ρ`:

`Tr(ρ P) = 3/5 > 0`.

The declared update is then defined, and

`P ρ P = diag(3/5, 0)`,
`L(ρ, P) = diag(3/5, 0) / (3/5) = diag(1, 0) = P`.

A second readout of the same PVM therefore has

`K(L(ρ, P), P) = Tr(P P) = 1`.

After a `P` outcome the next readout of this PVM is certain. The step uses
the declared Lüders map. It does not derive that map from the four axioms.

## Theorem 4 — The Matching Sentence Is Extra

Quote the current Admissibility sentence from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Quote the current Record locking and additivity sentences from the same
memo:

> When present, a record locks exactly one admissible local possibility.

> For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.

Neither sentence names the PVM `{P, Q}` or the Lüders map. A predicate
“the four axioms name Lüders” therefore fails on the canonical memo.

The matching sentence used here is extra:

> the instrument is a PVM Lüders readout.

Conditional on that matching, the weights on this PVM are the Born numbers
of Theorems 1 and 2, and the repeatability identity of Theorem 3 holds for
the declared update.

## Theorem 5 — Explicit Non-Claims

- This note does not adopt Lüders as an axiom.
- This note does not claim that the 2026-08-09 frame-lift uniqueness
  theorem is improved or replaced.
- This note does not claim that Born is false.
- This note does not claim that every kernel is Born.
- This note does not classify kernels outside the declared PVM `{P, Q}`.

The result is one named instrument class on one named PVM. It is not a
universal Born theorem and not a Gleason theorem in dimension two.

## Relation To The 2026-08-09 Parent

The parent proves that a supplied menu-independent grading, normalized on
every binary and ternary nonzero scaled-projector resolution, has a unique
density-matrix trace form on that scaled domain. The present note assumes
a declared two-outcome PVM and a declared Lüders instrument, then evaluates
the resulting weights. Those are compatible statements on different
inputs. The parent remains the uniqueness authority for the low-arity
grading class. This note remains the matching authority for one PVM
Lüders readout.

## Relation To The Current Axioms

[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
one-site algebraic possibility presentation `M_2(C)`, a nearest-neighbor
determined distribution over possibilities, and record locking with additive
scalar readout `I`. Qubit names the carrier. Admissibility names that
distribution. Record names locking and additivity. None of those sentences
selects the projectors `{P, Q}` or writes `P σ P / Tr(σ P)`.

If a later derivation produces this PVM and this update from Record
dynamics or other landed structure, the identities of Theorems 1–3 remain
available as the matching algebra. That derivation is not claimed here.

Independent audit remains required. This note authors no audit verdict and
makes no canonical axiom edit.

## Boundary And Degenerate Cases

- The Lüders formula is used only when `Tr(σ P) > 0`. The named density
  `ρ` satisfies that hypothesis; a `P`-null state is outside Theorem 3.
- Only the declared PVM `{P, Q}` is evaluated. No other measurement class
  is classified.
- Only the two named densities and their midpoint mix are used. No general
  Gleason or frame-function reconstruction is attempted.
- The word “kernel” in this note means the declared pair `K(σ, P)`,
  `K(σ, Q)` on this PVM.

## Independent Adversarial Checks

The runner evaluates `K` and `L` by calling `born_pvm(sigma, P)` and
`luders(sigma, P)`. Those identity gates are live traces and live matrix
products, not hardcoded constants. Replacing `born_pvm(ρ, P)` by the
constant `1/2` disagrees with the computed value `3/5` and must fail.
The predicate that the four axioms name Lüders is evaluated on the
canonical memo and fails.

The runner also rereads the parent uniqueness wording and the quoted
Admissibility and Record sentences, and it checks that this note keeps
conditional support, hypothetical axiom wording, and independent audit
explicit.

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| `M_2(C)` one-site presentation | carrier | current Qubit axiom | supplied algebraic presentation |
| Admissibility distribution sentence | quoted baseline | current axiom memo | does not name this PVM |
| Record lock and additive `I` | quoted baseline | current axiom memo | does not name Lüders |
| declared PVM `{P, Q}` | theorem input | this note | extra matching |
| declared Lüders map | theorem input | this note | extra matching; not an axiom |
| Born-on-this-PVM traces | theorem output | exact `Fraction` algebra | only on the declared PVM |
| 2026-08-09 unique trace form | parent uniqueness theorem | linked parent note | not replaced |
| observations or fitted weights | none | not used | not applicable |

Independent audit remains required before the repository may assign any
effective claim status.
