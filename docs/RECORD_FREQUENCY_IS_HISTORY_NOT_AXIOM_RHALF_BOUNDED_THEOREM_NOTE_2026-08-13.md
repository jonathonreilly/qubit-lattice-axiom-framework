---
claim_id: record_frequency_is_history_not_axiom_rhalf_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a one-site toy menu of two lock labels, empirical frequency is a function of a nonempty finite history of admissible locks. Live Record does not name a frequency, does not assign a readout to a blank site, and does not select r=1/2. Equal-block Koide (1,1) is a supplied weighting plus a selector, not a theorem of live Record. The note neither adopts r=1/2 nor bans it."
upstream_dependencies:
  - minimal_axioms
runner: scripts/record_frequency_is_history_not_axiom_rhalf_2026_08_13.py
---

# Record Frequency Is History, Not An Axiom `r=1/2`

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite-word frequency on a one-site two-lock toy menu
under the current Record wording.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/record_frequency_is_history_not_axiom_rhalf_2026_08_13.py`](../scripts/record_frequency_is_history_not_axiom_rhalf_2026_08_13.py)
**Parent on origin/main:** the axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Live Record does not select a lock frequency. A realized frequency is a
property of a nonempty finite history of locks. The value `r=1/2` may
occur as one such history (it is not banned science). It is not axiom
content, and it is not the unique frequency of admissible lock sequences.

Three exact statements locate the boundary.

1. Two length-4 histories of admissible locks have different `A`
   frequencies, `3/4` and `1/2`. The axiom text names neither.
2. The empty history has no frequency. A map that returns `1/2` on the
   blank is not a Record readout.
3. Equal-block Koide `(1,1) -> r=1/2` is a supplied weighting plus a
   selector. It is not a theorem of live Record. Koide `Q` is not derived
   here.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Fraction counts on a declared two-letter toy menu, with live Record quoted verbatim; no axiom retype, no frequency adoption, and no Koide Q derivation."
trace_class: negative_route_pruning
target_claim_id: record_frequency_selection
target_blocker_text: "do the current axioms select a lock frequency, in particular r=1/2?"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the declared toy histories and the displayed equal-block selector; no physical flavor, quark, or Koide-Q claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

This is current Record, not a retype. No hypothetical axiom wording is
offered.

## Exact Objects

Fix one site and a toy menu of two lock labels `{A,B}`. Each letter is one
admissible local possibility that a forming record may lock. A history `H`
is a finite word in `{A,B}`. Write `|H|` for its length and `n_A` for the
number of letters equal to `A`.

When `|H| >= 1`, the empirical frequency is the exact rational

`f(H,A) = n_A / |H|`

as a `Fraction`. The empty history has no frequency: blank cannot be read,
and `f(empty, ·)` is undefined. In particular this note does not set
`f(empty)=1/2`.

The construction is a counting interface on already-formed locks. It does
not supply a formation rate, a probability law over words, or a preferred
letter.

## Live Record

The current Record axiom is the `Record / Fixed Reality` section of
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). The three
readout sentences, quoted verbatim, are:

Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read.

The same memo states that finite additivity, a named scalar collection
functional `I`, and an assigned value `I(empty)=0` are not Record axiom
content. Named `I` is not axiom content. A site with no record cannot be
read; the axiom does not assign a scalar to absence.

Record therefore licenses reading the content of formed locks and forbids
reading a blank site. It does not name a frequency of lock labels.

## Theorem 1 — Two Admissible Histories Carry Distinct Frequencies

Let

`H1 = AAAB` and `H2 = AABB`.

Both are length-4 words in `{A,B}`, hence finite sequences of admissible
locks on the toy menu. Exact counts give

`f(H1,A) = 3/4` and `f(H2,A) = 1/2`.

Both values are realized frequencies of admissible lock sequences. The
axiom text does not name either frequency. In particular it does not
select `1/2`, and it does not forbid `3/4`.

The claim of this note is not that every history has `r=1/2`, and not
that `r=1/2` is impossible. The claim is that the axioms do not select a
frequency.

## Theorem 2 — Empty History Has No Frequency

`f(empty, ·)` is undefined. There is no letter count to form a
`Fraction`, and live Record supplies no substitute scalar: a site with no
record cannot be read.

A function that returns `1/2` on the empty history is not a Record
readout. It assigns a value where there is no record content. The same
objection applies to writing `I(empty)=0` and then converting that `0`
into a frequency: `I(empty)=0` is not axiom content, and a blank cannot
be read.

## Theorem 3 — Equal-Block `(1,1)` Is A Supplied Selector

The equal-block Koide weighting `(1,1) -> r=1/2` is a supplied weighting
plus a selector, not a theorem of live Record.

Display the two histories again:

`H1 = AAAB` has `f(H1,A)=3/4`.

`H2 = AABB` has `f(H2,A)=1/2`.

If one supplies block weights `(1,1)` and selects the normalized first
weight

`1 / (1+1) = 1/2`,

one has chosen `r=1/2` by that selector. The same selector is compatible
with `H2` and incompatible with `H1`. Live Record names neither the
weights nor the selector. The two displayed histories remain admissible
lock sequences.

This note does not derive Koide `Q`. It does not identify `{A,B}` with
quark flavors, lepton isotypes, or any physical generation carrier. It
does not say quarks forbid the investigation. The value `r=1/2` may be
recorded frequently under a later supplied law; that possibility is not
banned, and it is not made the whole program.

## Mutation Predicates

The following hostile predicates fail on the objects above.

1. “Every length-4 history has `f(A)=1/2`.” Counterexample: `H1 = AAAB`
   has `f(H1,A)=3/4`. Among the sixteen words of length 4, the possible
   `A` frequencies are `0, 1/4, 1/2, 3/4, 1`.
2. “`f(empty)=1/2` is axiom content.” False: `f(empty, ·)` is undefined,
   and the live Record readout sentences assign no value to a site with
   no record.

## Claim Boundary

| Item | Status |
|---|---|
| live Record readout sentences | quoted; not edited |
| named `I` and `I(empty)=0` | not axiom content |
| `f(H,A)` for `|H|>=1` | exact count on a nonempty word |
| `f(empty, ·)` | undefined |
| `r=1/2` as one realized frequency | permitted (`H2`); not adopted |
| universal `r=1/2` | rejected (`H1`) |
| equal-block `(1,1)` | supplied weighting plus selector |
| Koide `Q` | not derived |
| quark/flavor identification | not used |
| axiom edit or retype | none |

No canonical axiom is edited here.

## Imports And Open

**Imported.** The current four-axiom memo, used only for the Record
readout sentences and the explicit statement that named `I` and
`I(empty)=0` are not Record content.

**Derived here.** Exact frequencies of `H1` and `H2`; undefined empty
frequency; failure of the two mutation predicates; the typing of
equal-block `(1,1)` as a supplied selector.

**Open.** Any physical identification of the toy labels with a flavor
carrier; any formation law that would make one frequency typical; any
Koide `Q` derivation; any claim that a later retained law cannot prefer
`r=1/2`.
