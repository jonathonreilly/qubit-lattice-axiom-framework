---
claim_id: graded_constraint_interface_consistency_bounded_note_2026-07-04
claim_type: bounded_theorem
claim_scope: "Defect exhibit for graded_constraint v1, plus N1-N3 interface results conditional on graded_constraint v2 as an unregistered repaired premise."
upstream_dependencies:
  - minimal_axioms
runner: scripts/graded_constraint_interface_consistency_2026_07_04.py
---

# Graded-Constraint Interface Consistency: v1 Defect and v2 Repair

## House Header

**Date:** 2026-07-04
**Type:** bounded_theorem
**Authority:** conditional note only. It records a v1 defect exhibit and proves
interface claims only against the named v2 conditional premise below.
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

- **Defect exhibit premise profile:** the v1 core text below plus the landed
  Admissibility variation sentence only.
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

**Verdict.** the v1 core as literally worded is **DEFECTIVE**.

The collision is unconditional. v1 says `w` is normalized on each menu and also
says every finite orthogonal resolution of the composite identity is
menu-eligible. The landed Admissibility sentence says available possibilities
are determined by, and vary with, nearest-neighbor conditions. Therefore there
can be a record context in which an orthogonal identity resolution is mixed:
one element is available and another element is unavailable in that record
context.

v1 still makes that mixed resolution menu-eligible, so v1 forces it to
normalize as a physical menu. That is the defect. An unavailable element cannot
simultaneously be an unavailable outcome under Admissibility and a physical
menu alternative under the literal v1 menu sentence. No physical reading exists
for that mixed normalized menu.

This exhibit does not use Record, observed facts, Born assumptions, or any
repairing interpretation. It cites only the v1 text above and the Admissibility
variation sentence.

## Named Conditional Premise: v2

**graded_constraint v2 (candidate, unregistered).** A weight function
`w >= 0` is defined on the full projection lattice of every
nearest-neighbor composite, with `w(0) = 0`, `w(identity) = 1`, additive
over all orthogonal pairs, non-contextual, and dependent on the
surrounding record configuration through the nearest-neighbor channel.
Formation statistics on a record-conditioned menu of available
possibilities are `w` conditioned on that menu: the available elements'
weights renormalized by their total. If the available total is zero the
conditional is undefined — a named boundary, not hidden. No rate,
propagation rule, orientation, scale, or record-production rule is
supplied.

The structural change is narrow. Full-lattice additivity is explicit, so the
frame-function strength needed by a later Born-form bridge is preserved. Menus
no longer carry normalization as an axiom; conditioning does; availability filters outcomes, never weights. Mixed resolutions still normalize mathematically by lattice additivity, while unavailable elements cannot be locked and drop out of formation statistics through conditioning.

## N1 v2: Coexistence

**Verdict.** Conditional on v2, grading and availability coexist because they
are different interface objects.

Availability is binary. It is supplied by the landed nearest-neighbor
admissibility rule and governs what can be locked. The weight function `w` is
law-side grading data on the full projection lattice. Formation statistics are
obtained by conditioning `w` on the available elements of the record-conditioned
menu.

The conditioning map never alters availability: it reads the available set,
renormalizes the weights of the available elements by their available total,
and returns statistics or the named undefined boundary. Availability never
alters `w`: unavailable projections still have full-lattice values, and
orthogonal resolution sums still obey additivity. The zero-available-total
boundary is explicit: when the available elements have total `w`-weight zero,
the conditional is undefined rather than silently normalized.

## N2 v2: Conditioning Channel

**Verdict.** Conditional on v2, candidate resolution shapes are
record-independent, while physical menu status and conditioned statistics are
record-dependent.

The prior draft's "eligibility invariance" label was wrong. The invariant
object is only the algebraic candidate shape of a finite resolution, such as a
local `Z` resolution, a local `X` resolution, or an entangled/complement
resolution in the nearest-neighbor composite. Whether all elements of such a
shape are available is a physical menu-status question and varies with the
neighbor records. The conditioned statistics vary as well, because both
availability and `w` are record-conditioned through the nearest-neighbor
channel named by v2.

This variation is not a defect. It is exactly the landed Admissibility sentence
showing through: available possibilities are determined by, and vary with, the
nearest-neighbor conditions.

## N3 v2: Narrow Record Interface

**Verdict.** Conditional on v2, composite projection weights do not enlarge
locking or readout.

The two claims are only these:

1. No record locks a composite entangled projection. Locking quantifies over
   admissible local possibilities: "When present, a record locks exactly one
   admissible local possibility."
2. No readout value queries `w` directly: "Only records are readable. A readout
   value is determined by record content alone."

The sharpened ontology is that `w`, given the records, is law-side data. It is
the law's one answer at that state; distribution-valued answers are still one
answer. It is not extra state content: two states with identical records do not differ in `w`.

This is not a claim that `w` has no readable consequences. Record frequencies can read `w` in aggregate; that is its point. The claim is only that an individual readout value is fixed by record content alone and that no entangled projection becomes lockable content.

## No-Go Discipline Gate

- **N1 route enumeration:** the v1 defect is not repaired by deriving weights
  from Admissibility. Admissibility supplies availability, not a full-lattice
  weight.
- **N2 premise separation:** v2 is a named conditional premise. This note does
  not register it, approve it, or treat it as landed axiom text.
- **N3 hidden-wall scan:** the full-lattice/additivity surface, mixed
  available/unavailable resolutions, the zero-available-total boundary, and the
  aggregate-readability of `w` through record frequencies are explicit.
- **N4 residual matching:** v2 supplies no rate, propagation rule, orientation,
  scale, or record-production rule. Those remain outside this note.
- **N5 rhetoric audit:** "coexistence", "conditioning channel", and "narrow
  record interface" are conditional interface results, not derivations of Born
  values or dynamics.
- **N6 partial-closure path scan:** the note closes only the v2 interface
  checks it states. It does not close probability, measurement-context,
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
- Does **not** derive Born weights.
- Does **not** supply propagation, stability, rate, scale, orientation, or
  record production.
- Does **not** set or forecast any audit verdict.
- Does **not** use the beamsplitter or correlated-neighbor observed-fact
  warrants as premises.

## Verification

Measured runner output:

```text
CHECK 01: PASS - Defect exhibit: v1 mixed identity resolution :: orthogonal identity resolution normalizes while containing unavailable ZA1
CHECK 02: PASS - N1 v2: coexistence and conditioning separation :: availability and w remain distinct; conditioning excludes unavailable outcomes
CHECK 03: PASS - N1 v2: zero-available-total boundary :: conditional is undefined while full-lattice additivity remains intact
CHECK 04: PASS - N2 v2: record-independent shapes, record-dependent menus :: shape function receives records but derives shapes from algebra dimension
CHECK 05: PASS - N3 v2: local locking and record-only readout :: entangled projection not lockable; identical-record different-w state rejected
CHECK 06: PASS - Rejectors: additivity, conditioning, readout mutations caught :: same projections and states fail under three genuine mutations
CHECK 07: PASS - Needle: prose premises and status discipline :: v1/v2 text, landed sentences, boundary, aggregate-readability, measured total
TOTAL: PASS=7 FAIL=0
```
