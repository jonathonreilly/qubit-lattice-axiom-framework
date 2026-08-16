---
claim_id: two_tick_record_content_chiral_rival_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Whether a two-tick rival whose tick-2 neighbor alphabet is Record content {0,+,−} admits a P-odd formation predicate (the July-3 k=3 pair), while occupancy-only tick-1 cannot, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_tick_record_content_chiral_rival_2026_08_15.py
---

# Two-Tick Record-Content Chiral Rival (Displayed, Not Adopted)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact finite formation predicates on the six nearest-neighbor
directions. Tick 1 is occupancy-only. Tick 2 is allowed to read Record
content in the three-letter alphabet `{0,+,−}`. The July-3 unique `k=3`
chiral pair is used only as a displayed rival predicate. No rule is written
into Admissibility. L1 is not attached.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_tick_record_content_chiral_rival_2026_08_15.py`](../scripts/two_tick_record_content_chiral_rival_2026_08_15.py)

## Question

Investment `#6630` / July-3: occupancy-only L1 formation is automatically
achiral. July-3 theorem 3: a chiral rule needs a 3-value channel; the unique
`k=3` pair is the handed fully-mixed patterns. Investment `#6328`: L1 lock
labels do not feed `n`. Those leftovers are not this residual. `#6328` is
`10→L1`'s refusal. `#6630` is occupancy-only. The new residual is whether a
*rival* two-tick member may let tick-2 formation depend on neighbor *record
content* (Record is readable) and whether that tick-2 rule can be `P`-odd.

`f_L1` is `n≠0`, not Hamming. This note does not attach L1. It does not
reopen born-compiler / color-unital-m3. Occupancy is not run on a
`20→`new spatial patch.

## Answer

Yes as a displayed capacity, no as an adopted rule.

Tick 1 stays the occupancy predicate on `{0,1}^6`. Tick 2 may use the
three-letter nearest-neighbor condition `{0,+,−}` that Record plus
Admissibility already allow: absence is unread, and two readable Record
contents are distinct. The July-3 unique `k=3` pair is then a well-defined
formation predicate `f` on that alphabet, and `f` is not `P`-invariant. Every
two-letter occupancy projection of `f` is `P`-invariant, so occupancy-only
tick 1 cannot carry the same `P`-odd grade. A Record-conditioned two-tick
rival can therefore match a `P`-odd / V−A *capacity* that L1 cannot.
Displayed, not adopted. Do not write the pair or V−A into Admissibility.

claim_scope: Whether a two-tick rival whose tick-2 neighbor alphabet is
Record content `{0,+,−}` admits a P-odd formation predicate (the July-3 k=3
pair), while occupancy-only tick-1 cannot, is reported. Displayed, not
adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite enumeration of six-direction colorings exhibits one P-odd three-letter formation predicate and P-invariance of every occupancy projection; the rival is displayed, not adopted."
trace_class: displayed_rival
target_claim_id: two_tick_record_content_chiral_rival
target_blocker_text: "can a two-tick rival use Record content to be chiral"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "leave the pair displayed; do not adopt it, do not attach L1, and do not write it into Admissibility"
conditional_surface_status: "exact for the named six-direction alphabets and the July-3 k=3 pair re-earned as a formation predicate"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

Quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

The distribution concerns which possibility a forming record locks, conditional
on formation at that site; it does not supply the formation site, probability,
or rate.

Records form.

When present, a record locks exactly one admissible local possibility.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.

July-3 theorem 3 is the classification fact used as a named finite object, not
as an axiom edit:
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).
At `k=3` there is exactly one chiral pair, whose members are the handed
fully-mixed patterns (every axis bi-colored, every value used twice). The
paired runner re-earns that pair on the six axis directions and does not
consume a cache.

## Algebra

Order the six nearest-neighbor directions as

```text
(+x, -x, +y, -y, +z, -z).
```

Spatial inversion `P = -I` is central in the full cubic group and acts by
swapping opposite directions:

```text
P · (+x,-x,+y,-y,+z,-z) = (-x,+x,-y,+y,-z,+z).
```

The proper cubic group `G+` has 24 elements. It acts by permuting the six
directions.

**Tick 1 (occupancy, two-letter).** A neighbor condition is `c ∈ {0,1}^6`.
Write `d = c_1+⋯+c_6` and `n = d/3`. Formation is

```text
f_L1(c) = 1  iff  n≠0.
```

That is the occupancy predicate `d≠0`, not a Hamming-grade rule and not a
function of lock labels. `#6630` / July-3 theorem 2 already make every
openness-level (two-letter) proper-covariant rule automatically `P`-even.
The runner re-earns: all 64 occupancy colorings are proper-equivalent to
their `P`-images, and `f_L1` itself is `P`-invariant. Exactly 63 of the 64
occupancy patterns form.

**Tick 2 (Record content, three-letter).** Each neighbor is `0` (no record),
`+`, or `−` (two readable Record contents). That is a 3-letter nearest-neighbor
condition allowed by Record + Admissibility. The configuration space is

```text
{0,+,−}^6,    |{0,+,−}^6| = 3^6 = 729.
```

A *handed fully-mixed* coloring is one in which every axis is bi-colored with
two distinct letters and every letter is used exactly twice. There are exactly
48 such colorings. They split into two `G+`-orbits of size 24. `P` exchanges
the two orbits and no proper element does. That is the unique `k=3` chiral
pair.

A runner-anchored representative of one hand is

```text
r = (0, +, 0, −, +, −).
```

Every axis of `r` is bi-colored and the letter counts are `2/2/2`. Define the
displayed rival formation predicate `f` to be the indicator of the proper
orbit of `r`:

```text
f(c) = 1  iff  c ∈ G+ · r.
```

This is a well-defined function `{0,+,−}^6 → {0,1}`. It is not attached to
L1. L1 remains the occupancy rule `f_L1`.

The occupancy (two-letter) projection of a three-letter coloring is

```text
π(0)=0,   π(+)=π(−)=1,   π(c)_i = π(c_i).
```

The occupancy projection of `f` is the set `{π(c) : f(c)=1} ⊂ {0,1}^6`, or
equivalently the existential predicate `F_occ(b)=1` iff some lift of `b` lies
in `G+ · r`. A general two-letter projection is the same construction for an
arbitrary letter map `{0,+,−} → {0,1}`.

## Theorem 1 — the July-3 k=3 pair is a P-odd tick-2 predicate

The July-3 unique `k=3` chiral pair is a well-defined formation predicate `f`
on `{0,+,−}^6`. Direct enumeration gives

```text
N_form    = |{c : f(c)=1}|           = 24,
N_P_form  = |{c : f(P·c)=1}|         = 24,
N_both    = |{c : f(c)=f(P·c)=1}|    = 0.
```

Hence `N_both < N_form`, so `f` is not `P`-invariant. Tick-2 *can* be
`P`-odd.

*Proof.* The 24 proper direction permutations produce 24 distinct images of
`r`. Their `P`-images form a disjoint 24-set, the other hand. If `f(c)=1`
then `P·c` lies in the other hand, so `f(P·c)=0`. The two counts are
therefore complementary and the intersection is empty. Burnside orbit counts
on the 729 colorings recover July-3 theorem 3: 57 proper orbits, 56 full
orbits, difference one chiral pair. Every member of either orbit is handed
fully-mixed, and every handed fully-mixed coloring lies in the pair.

## Theorem 2 — occupancy projections cannot carry the same P-odd grade

Every two-letter (occupancy) projection of `f` is `P`-invariant.
Occupancy-only tick-1 cannot carry the same `P`-odd grade.

*Proof.* Let `ψ:{0,+,−}→{0,1}` be any letter map and write
`S_ψ = {ψ∘c : f(c)=1}`. For the occupancy map `π` one has `|S_π|=12` and
`P(S_π)=S_π`. The same identity `P(S_ψ)=S_ψ` holds for all eight maps to
`{0,1}`. In particular the existential occupancy predicate of `f` is
`P`-even.

Independently, tick-1 formation is `f_L1(c)=(n≠0)` on `{0,1}^6`. That
predicate depends on occupancy only. It is `P`-invariant because `P` merely
reorders the six bits. Stronger: every one of the 64 occupancy colorings is
proper-equivalent to its `P`-image, so no occupancy-only formation set that
is a union of proper orbits can be `P`-odd. Occupancy-only tick-1 therefore
cannot carry the `P`-odd grade that `f` carries on `{0,+,−}^6`.

## Theorem 3 — displayed V−A capacity, not an adopted rule

Displayed: a Record-conditioned two-tick rival can match a `P`-odd / V−A
*capacity* that L1 cannot. Displayed, not adopted. Do not write the pair or
V−A into Admissibility. Do not attach L1.

The only load-bearing statements are Theorems 1 and 2. Theorem 3 names the
comparison: L1, kept as `f_L1` with `n≠0`, has no `P`-odd formation grade;
the displayed tick-2 rival does. The pair is not selected as the framework's
fixed admissibility rule. No V−A coupling, no weak current, and no fermion
sector identification is derived. The word "capacity" is used only for this
finite `P`-odd possibility.

## What this note does and does not claim

- It reports whether the named two-tick rival *admits* a `P`-odd tick-2
  predicate. It does not adopt that rival.
- It does not attach L1. `f_L1` remains `n≠0`, not Hamming, and lock labels
  still do not feed `n`.
- It does not write the pair or V−A into Admissibility, and it does not edit
  any axiom, primitive, or registry.
- It does not reopen born-compiler / color-unital-m3.
- It is not leftover-character of `#6328` or of `#6630`.
- It does not run occupancy on a `20→`new spatial patch.
- It does not identify the physical condition alphabet beyond the displayed
  tick-2 hypothesis that Record content `{0,+,−}` is readable.
- Formation site, probability, process, and rate remain unsupplied.

## No-Go Discipline

The negative statement is only: occupancy-only tick-1 cannot host the same
`P`-odd grade as the displayed three-letter pair. It is not a no-go against
every future chiral proposal.

### N1 — materially distinct route scan

| route | marker | outcome |
|---|---|---|
| occupancy-only L1, `f_L1` is `n≠0` | **ATTEMPTED** | automatically `P`-even; `#6630` / July-3 theorem 2 |
| feed L1 lock labels into `n` | **ATTEMPTED** | `#6328` already refuses; not this residual |
| tick-2 reads Record content `{0,+,−}` | **DISPLAYED** | July-3 unique `k=3` pair is `P`-odd |
| write the pair or V−A into Admissibility | **REFUSED** | displayed, not adopted |
| attach the pair to L1 | **REFUSED** | do not attach L1 |
| born-compiler / color-unital-m3 | **REFUSED** | not reopened |
| occupancy on a `20→`new spatial patch | **REFUSED** | not executed |

### N2 — wall independence

One wall is claimed: two-letter occupancy cannot carry this `P`-odd grade.
The displayed existence of a three-letter `P`-odd predicate is a positive
enumeration, not a second impossibility wall.

### N3 — hidden-wall scan

The alphabets, `P`, `G+`, `f`, `f_L1`, and the projections are declared. No
dynamics, no spatial 20-site patch, no Born compiler, and no axiom edit is
imported.

### N4 — residual matching

The residual answered is exactly the tick-2 Record-content chirality
question. It is not the leftover character of `#6328` or `#6630`.

### N5 — certificate granularity

```text
per-element: executed — all 729 three-letter and 64 two-letter colorings
per-site: not applicable — one origin star, six directions
per-mode: not applicable
per-block: executed — the unique k=3 pair and its occupancy projections
lattice-wide: not executed — no new spatial patch
```

### N6 — partial-closure paths

A later derivation could still refuse tick-2 content dependence, or could
adopt a different three-letter predicate. Either path is additional work.
Adopting the pair would be an axiom-level or rule-level act and is out of
scope.

### N7 — steelman

The strongest objection is that tick-2 is still "the" admissibility rule, so
July-3 already classified it and nothing new is displayed. The distinction
held here is only compositional: occupancy-only tick-1 is forced achiral,
while a *rival two-tick member* whose second tick is allowed to read Record
content can host the already-classified `k=3` pair. The pair itself is not
new. The two-tick capacity comparison is the reported residual.

### N8 — cross-cycle echo

July-3 theorem 2 and theorem 3 are used as named finite facts and are
re-earned on the same six directions. No status is borrowed from those
notes' audit rows.

## Verification

Run:

```bash
python3 scripts/two_tick_record_content_chiral_rival_2026_08_15.py
```

The runner re-earns the unique `k=3` pair, evaluates `N_form`, `N_P_form`,
and `N_both`, checks every two-letter projection, pins `f_L1` as `n≠0`, and
refuses axiom edits. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
