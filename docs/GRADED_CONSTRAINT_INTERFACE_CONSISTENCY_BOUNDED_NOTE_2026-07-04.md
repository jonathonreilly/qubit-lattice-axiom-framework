---
claim_id: graded_constraint_interface_consistency_bounded_note_2026-07-04
claim_type: bounded_theorem
claim_scope: "Conditional defect exhibit for graded_constraint v1 when a mixed-support context is separately supplied, plus N1-N3 algebraic interface results for an auxiliary grading w conditional on graded_constraint v2 as an unregistered repaired premise; no identification of w with the Admissibility distribution or formation statistics is made."
upstream_dependencies:
  - minimal_axioms
runner: scripts/graded_constraint_interface_consistency_2026_07_04.py
---

# Graded-Constraint Interface Consistency: v1 Defect and v2 Repair

## House Header

**Date:** 2026-07-04
**Type:** bounded_theorem
**Authority:** conditional note only. It records a v1 defect exhibit under a
separately supplied mixed-support context and proves algebraic interface claims
only against the named v2 conditional premise below.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and makes no audit forecast.
**Primary runner:**
[`scripts/graded_constraint_interface_consistency_2026_07_04.py`](../scripts/graded_constraint_interface_consistency_2026_07_04.py)
**Runner cache:**
[`logs/runner-cache/graded_constraint_interface_consistency_2026_07_04.txt`](../logs/runner-cache/graded_constraint_interface_consistency_2026_07_04.txt)

The landed pager's core text (v1) is superseded by v2 for this interface note;
the pager amendment travels separately. This note records the defect and the
repaired premise only. This is the pipeline working: the three-seat refutation
found a literal-core collision, this note accepts it, and the runner checks the
replacement interface mechanically.

## Premise Profile

- **Defect exhibit premise profile:** the v1 core text below plus a separately
  supplied mixed-support context. The revised Admissibility variation sentence
  alone does not force support variation; probabilities may vary at fixed
  support.
- **N1-N3 premise profile:** conditional on `graded_constraint v2 (candidate,
  unregistered)` as the named repaired premise, together with the quoted
  landed Record and Admissibility sentences where each result names them.
- **Status discipline:** no audit forecasting, no primitive registration, and
  no claim that v2 is already approved framework content.

## Landed Sentences Used

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

- "For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions."
- "Records form."
- "When present, a record locks exactly one admissible local possibility."
- "Only records are readable."
- "A readout value is determined by record content alone."

> **Scope note (2026-08-05, adoption repair).** The Admissibility second
> sentence quoted above was replaced by owner-approved revision on 2026-08-05.
> It now reads: "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
> Availability is the distribution's support. The quotation above is retained as
> the wording this note consumed when it landed.

## Superseded v1 Core Text

**graded_constraint v1 (superseded core text).** For record-conditioned
menus of admissible possibilities, a weight function `w >= 0` exists with
`w(0) = 0`, `w(identity) = 1`: normalized on each menu, additive over
exclusive alternatives, non-contextual across embedding menus, and defined
on the full projection lattice of every nearest-neighbor composite, with
every finite orthogonal resolution of the composite identity menu-eligible.
No rate, propagation rule, orientation, scale, or record-production rule is
supplied.

## Defect Exhibit: v1 Is Defective

**Conditional verdict.** The v1 core is defective whenever a mixed-support
context is supplied. The current axiom does not by itself establish that such a
context occurs.

The collision is conditional on mixed support. v1 says `w` is normalized on each menu and also
says every finite orthogonal resolution of the composite identity is
menu-eligible. Supply a record context in which an orthogonal identity
resolution is mixed: one element lies in the Admissibility distribution's
support and another does not.

v1 still makes that mixed resolution menu-eligible, so v1 forces it to
normalize as a physical menu. That is the defect. An unavailable element cannot
simultaneously be an unavailable outcome under Admissibility and a physical
menu alternative under the literal v1 menu sentence. No physical reading exists
for that mixed normalized menu.

This exhibit does not use Record, observed facts, or Born assumptions. It uses
the v1 text plus the named mixed-support condition; it is not an axiom-text
consequence.

## Named Conditional Premise: v2

**graded_constraint v2 (candidate, unregistered).** A weight function
`w >= 0` is defined on the full projection lattice of every
nearest-neighbor composite, with `w(0) = 0`, `w(identity) = 1`, additive
over all orthogonal pairs, non-contextual, and dependent on the
surrounding record configuration through the nearest-neighbor channel.
The auxiliary menu grading is `w` conditioned on the Admissibility support:
the supported elements' `w`-values renormalized by their total. If that total
is zero the auxiliary conditional is undefined — a named mathematical
boundary, not hidden. This conditional is not a formation-statistics law
unless a separate bridge relates `w` to the Admissibility distribution. No rate,
propagation rule, orientation, scale, or record-production rule is
supplied.

The structural change is narrow. Full-lattice additivity is explicit, so the
frame-function strength needed by a later Born-form bridge is preserved. Menus
no longer carry `w`-normalization as a premise; auxiliary conditioning does;
availability is the support of the axiom's distribution. Mixed resolutions
still normalize mathematically by lattice additivity, while unsupported
elements drop out of the auxiliary conditioned grading.

## N1 v2: Coexistence

**Verdict.** Conditional on v2, grading and availability coexist because they
are different interface objects.

> **Scope note (2026-08-05, adoption repair).** The 2026-08-05 owner-approved
> Admissibility revision makes availability the support of a law-level
> distribution rather than a separately supplied primitive set. That does not
> merge the two objects this section holds apart: `w` here is the
> graded-constraint v2 grading on the full projection lattice, a named
> conditional premise, and it is not the Admissibility distribution. It is an
> auxiliary nonphysical grading until a bridge supplies a relation to that
> distribution. Read
> post-revision, "availability is binary" is a statement about the support
> predicate (in/out), not about how availability is supplied; the coexistence
> result stands for `w` against availability. The zero-available-total
> boundary remains non-vacuous only as a boundary on the auxiliary grading: it
> is a boundary on the
> available elements' total `w`-weight, and `w` may vanish where the
> Admissibility distribution does not. This note supplies no relation between
> `w` and the Admissibility distribution. If `w` were identified with that
> distribution, the zero-available-total boundary would be vacuous and the
> conditioned values would merely reproduce the axiom's probabilities.

Availability is the binary support predicate of the landed nearest-neighbor
probability rule and governs what can be locked. The weight function `w` is
auxiliary grading data on the full projection lattice. Its conditioned values
are mathematical interface data, not formation statistics.

The conditioning map never alters availability: it reads the available set,
renormalizes the weights of the available elements by their available total,
and returns an auxiliary grading or the named undefined boundary. Availability never
alters `w`: unavailable projections still have full-lattice values, and
orthogonal resolution sums still obey additivity. The zero-available-total
boundary is explicit: when the available elements have total `w`-weight zero,
the conditional is undefined rather than silently normalized.

## N2 v2: Conditioning Channel

**Verdict.** Conditional on v2, candidate resolution shapes are
record-independent, while physical menu status and the conditioned auxiliary grading are
record-dependent.

The prior draft's "eligibility invariance" label was wrong. The invariant
object is only the algebraic candidate shape of a finite resolution, such as a
local `Z` resolution, a local `X` resolution, or an entangled/complement
resolution in the nearest-neighbor composite. Whether all elements of such a
shape are available is a physical menu-status question and varies with the
neighbor records. The conditioned auxiliary grading varies as well, because
both support and `w` are record-conditioned in the named v2 fixtures.

This variation is not a defect, but it is fixture content rather than a
consequence of distribution variation alone: the axiom allows probabilities to
vary while support remains constant.

## N3 v2: Narrow Record Interface

**Verdict.** Conditional on v2, composite projection weights do not enlarge
locking or readout.

The two claims are only these:

1. No record locks a composite entangled projection. Locking quantifies over
   admissible local possibilities: "When present, a record locks exactly one
   admissible local possibility."
2. No readout value queries `w` directly: "Only records are readable. A readout
   value is determined by record content alone."

The conditional premise makes `w`, given the records, auxiliary law-side data.
It is not extra state content: two states with identical records do not differ
in `w`.

No readable or frequency consequence of `w` follows without a bridge to the
Admissibility distribution or another operational rule. The claim here is only
that an individual readout value is fixed by record content alone and that no
entangled projection becomes lockable content.

## No-Go Discipline Gate

- **N1 route enumeration:** the conditional v1 defect is not repaired by
  conflating the Admissibility distribution with a full projection-lattice
  grading.
- **N2 premise separation:** v2 is a named conditional premise. This note does
  not register it, approve it, or treat it as landed axiom text.
- **N3 hidden-wall scan:** the full-lattice/additivity surface, mixed
  available/unavailable resolutions, the zero-available-total boundary, and the
  absence of an operational bridge for `w` are explicit.
- **N4 residual matching:** v2 supplies no rate, propagation rule, orientation,
  scale, or record-production rule. Those remain outside this note.
- **N5 rhetoric audit:** "coexistence", "conditioning channel", and "narrow
  record interface" are conditional interface results, not derivations of Born
  values or dynamics.
- **N6 partial-closure path scan:** the note closes only the v2 interface
  checks it states. It does not close a Born-form bridge, probability values, measurement-context,
  dynamics, or readout-context gates.
- **N7 steelman:** an objector can reject v1 literally, and this note agrees.
  The repaired claim is v2 only: normalization is by conditioning, not by
  declaring every mixed resolution a physical menu.
- **N8 cross-cycle echo:** no observed-fact warrant, beamsplitter statistic,
  correlated-neighbor statistic, older probability note, or older measurement
  context is imported as a premise.

## Non-Claims

- Does **not** claim v1 is consistent.
- Does **not** register, approve, or claim v2 as a framework primitive.
- Does **not** derive Born weights or identify `w` with the Admissibility distribution.
- Does **not** supply propagation, stability, rate, scale, orientation, or
  record production.
- Does **not** set or forecast any audit verdict.
- Does **not** use the beamsplitter or correlated-neighbor observed-fact
  warrants as premises.

## Verification

Measured runner output:

```text
CHECK 01: PASS - Conditional defect exhibit: v1 mixed identity resolution :: supplied mixed-support resolution normalizes while containing unsupported ZA1
CHECK 02: PASS - N1 v2: auxiliary-grading coexistence and conditioning separation :: Admissibility support and auxiliary w remain distinct
CHECK 03: PASS - N1 v2: zero-available-total boundary :: conditional is undefined while full-lattice additivity remains intact
CHECK 04: PASS - N2 v2: record-independent shapes, fixture-dependent menus and auxiliary grading :: shape function receives records but derives shapes from algebra dimension
CHECK 05: PASS - N3 v2: local locking and record-only readout :: entangled projection not lockable; identical-record different-w state rejected
CHECK 06: PASS - Rejectors: additivity, conditioning, readout mutations caught :: same projections and states fail under three genuine mutations
CHECK 07: PASS - Needle: prose premises and status discipline :: v1/v2 text, landed sentences, auxiliary boundary, no-readability fence, measured total
TOTAL: PASS=7 FAIL=0
```
