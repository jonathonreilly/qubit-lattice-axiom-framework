# Frozen-Region Record Saturation: Local Finality, Halting Local Record-Time, and Bounded Boundary Influence

**Date:** 2026-07-03
**Type:** bounded theorem (T1, T2, T3) + narrow scoped theorem (T4) + consequence/residue map (T5)
**Status:** worker draft under the workhorse execution split; the supervising lane reviews and lands.
**Status authority:** this note asserts no audit status and no promotion. Audit
status is set only by the independent audit lane. Nothing here is adopted,
promoted, ruled, or admitted as a premise by this note.
**No-verdict:** the note states bounded/narrow theorem content and its residues
only; it issues no audit verdict and predicts none.
**Runner:** `scripts/frontier_frozen_region_saturation_finality_2026_07_03.py`
**Runner output:** `outputs/frontier_frozen_region_saturation_finality_2026_07_03.txt` (exact-arithmetic; int/tuple/set only; 27/27 per-check PASS; nonzero exit on any FAIL)

## Firewall (read first)

- **Conditional on PR #4874.** Permanence-dependent content (T1, T2, and the
  permanence half of T3) is grounded CONDITIONALLY on the in-flight,
  owner-approved (2026-07-03) PR #4874, which replaces the Record clause "the
  locked possibility is invariant under repeated readout" with "records are
  permanent." Without #4874 these theorems revert to readout-invariance only.
  Supervisor-supplied.
- **Interpretive labels are readings, not claims.** "Frozen star",
  "black-hole-like", and "local time ended" are an owner interpretive READING of
  the record-level phenomenon; they are not asserted as results.
- **No GR content.** No metric, horizon, curvature, geodesic, singularity, or
  Hawking-type content. Nothing here is general relativity.
- **No rate / metric / clock content.** All temporal language is COUNT-level
  (record-inclusion event counts), never rate or duration. The landed
  count-not-rate firewalls are cited as review-pending / unaudited post-reset.
- **Realized-sector conditioning.** Per the owner ruling, non-triviality is
  contingent realized data, not law (vacuum-solution analogy); every theorem
  conditions on the realized sector explicitly, and the empty and saturated
  worlds are equally legal solutions.
- **Nothing adopted.** The event-ordering and static-world admissibility are
  REBUILT from scratch as small exact constructions; the review-pending sibling
  (PR #4873, branch-only) is cited by number only and was not read. The audit
  lane owns all statuses.

## Purpose

State, at note level with exact finite witnesses, four bounded/narrow theorems
about record-saturated regions of `Z^3`: (T1) a saturated region is locally
final; (T2) its local record-time halts while events continue outside; (T3) it
exerts a permanent possibility-level boundary constraint without any dynamical
claim; (T4) global saturation is unreachable at any finite stage in the named
finitary realized sector, so the infinite lattice is load-bearing for unbounded
record-time. T5 gives the consequence map and the complete residue set.

## Supplied surface (quotes)

Axiom sentences quoted verbatim from `docs/MINIMAL_AXIOMS_2026-06-29.md` (this
worktree copy carries the PRE-restoration Record wording; runner quote guards
match this file at checks 1-3):

- Record: "When present, a record locks exactly one local possibility from the
  subset available at that site under Admissibility; the locked possibility is
  invariant under repeated readout."
- Record (readout): "For any finite collection of pairwise-disjoint records,
  scalar readout `I` is additive, with `I(empty)=0`."
- Admissibility: "For each site, the available possibilities are determined by,
  and vary with, the nearest-neighbor conditions" under "one fixed
  nearest-neighbor admissibility rule, covariant under lattice translations and
  proper cubic rotations."
- Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with
  nearest-neighbor adjacency, standard translations, and proper cubic rotations."
- Qualification: "A state is a configuration of records."

Supervisor-supplied surface (not read from repo files; used as stated): PR #4874
(in-flight) makes the Record clause "records are permanent", readout-invariance
becoming a derived lemma. Owner ruling: non-triviality is contingent realized
data, not law (vacuum-solution analogy); theorems condition on the realized
sector. Sibling PR #4873 (review-pending, branch-only, NOT read) derives the
event-ordering from permanence + "A state is a configuration of records",
exhibits the admissible static world, and carries an exact `2x2x2` saturation
witness with covariant boundary pinning -- rebuilt here from scratch. Owner
reading (a name, not a claim): a saturated region is "frozen-star /
black-hole-like" -- fully written reality, local time ended.

Note-level model (exactness firewall). A locked value is modelled by a scalar tag
in `{+1,-1}` -- the note-level image of the Record locking clause, NOT a claim
about the full one-site `M_2(C)` domain. A configuration is a partial map
site -> locked value; under permanence (#4874) plus "A state is a configuration
of records" a realized history has nested record sets with agreeing values, and
an EVENT at stage `t` is a new registration (`dom(C_t) \ dom(C_{t-1})`). The
availability model is `available_at(s) = { locked values of records on nearest
neighbors of s }` if nonempty, else `{+1,-1}`.

## T1 -- Saturation implies local finality (bounded, conditional) [checks 4-9]

A region `R` is record-saturated in `C` iff every site of `R` carries a record.
Since a record "locks exactly one local possibility" per site (quoted) and
permanence bars removal or alteration, no site of `R` can host a new registration
in any later configuration of a realized history: the `R`-restriction is constant
from the first saturated stage. Exact witnesses -- the `2x2x2` (8-site) and
`3x3x3` (27-site) windows, one record per site -- each yield zero registrable
sites [checks 4-5]. Constancy is FORCED, by exact enumeration over all `4^8`
candidate later `R`-restrictions on the `2x2x2` window: each per-site candidate is
a removal, a value change, or a second record; permanence bars the first two and
"locks exactly one" bars the third, so exactly one candidate survives and it
equals `C|R` [check 6]; the three barred kinds are each independently rejected
[check 7]. Global corollary: a globally saturated all-`(+1)` configuration is
admissible -- every locked value lies in its neighbor-determined availability set,
and readout is additive over disjoint sub-collections with `readout(empty)=0`
[check 8]; the check has teeth, since flipping one interior site to `-1` amid `+1`
neighbors makes the configuration non-admissible [check 9]. Per the owner ruling,
the static globally saturated world is a legal solution (final and physical, like
a vacuum solution), not a defect.

## T2 -- Local record-time stops (bounded, conditional) [checks 10-15]

Record-inclusion event-ordering (rebuilt, three lines): permanence plus "A state
is a configuration of records" gives nested record sets along any realized
history; locked values agree on the smaller domain; an EVENT at stage `t` is a
new registration. Inside a saturated region the restricted record set is
constant, so its event count halts -- local record-time in `R` ends -- while
events continue on the unsaturated complement. Exact witness history (4 stages on
a 16-site window; `R` = the `2x2x2` block): record sets are nested with agreeing
values [check 10]; `R` is unsaturated at stage 1, saturated at stage 2, so a
frozen region is produced [check 11]; per-stage in-`R` event counts are
`(4,4,0,0)` [check 12] while outside-`R` counts are `(0,0,2,2)` [check 13]; the
record set in `R` is constant at 8 for stages 2,3,4 [check 14]; the outside count
strictly increases at stages 3 and 4 while `R` is frozen [check 15]. Frontier
picture (count-level only): record-time flows exactly where unwritten possibility
remains.

## T3 -- Boundary influence without evolution (bounded) [checks 16-21]

Under the covariant neighbor-dependent availability rule (rebuilt exactly), a
saturated region's records permanently constrain the available possibilities at
adjacent OUTSIDE sites. Exact witness: an outside site adjacent to the saturated
block, all of whose in-`R` neighbors record `+1`, has availability `{+1}` at every
stage [check 16], while a far site retains `{+1,-1}` [check 17]. The pin is
PERMANENT: the in-`R` neighbor record is constant along the history, so
availability never relaxes [check 18]. The influence is possibility-level, not a
force: the boundary site stays registrable (unrecorded) at every stage while its
availability is pinned [check 19] -- no record is placed on it, no evolution is
asserted. The rule is covariant under lattice translation [check 20] and under a
proper cubic rotation [check 21], matching the Admissibility clause.

Honesty scope. The availability rule is a NOTE-LEVEL model of the Admissibility
clause "determined by, and vary with, the nearest-neighbor conditions"; the axiom
fixes the clause, not the specific rule. The proven content is the exact pinning
for the EXHIBITED covariant rule. The general statement -- that ANY rule with
determined-by + vary-with + covariance carries SOME permanent boundary constraint
from a saturated neighborhood -- is stated as the named conditional and flagged as
rule-dependence residue, not claimed here.

## T4 -- Global saturation unreachable at finite stage (narrow, scoped) [checks 22-27]

Scope (named realized-sector class): histories with finite initial record support
and finitely many registrations per step. Then the recorded set is finite at every
finite stage [check 22], because a finite union of finite sets is finite
[check 23]. Since `Z^3` minus a finite set is infinite, unrecorded sites remain
without bound: the unrecorded count in the `(2k+1)^3` window strictly increases as
`(25,122,339)` for `k=1,2,3` [check 24], and an explicit unrecorded witness
`(M+1,0,0)` sits outside the recorded bounding window at any finite stage
[check 25]. So global saturation is never reached at any finite stage; it is at
most a limit notion. Owner structural remark, checked: on any FINITE lattice of
`N` sites a one-record-per-stage history saturates in exactly `N` stages with zero
registrable sites afterward [check 26], and by pigeonhole no `(N+1)`-th distinct
registration is possible [check 27]. Unbounded record-time therefore requires the
infinite `Z^3` of the Lattice axiom -- it is load-bearing. Consequence: the frozen
WORLD is admissible as an initial/boundary datum but is not producible from sparse
beginnings in finite record-time; frozen REGIONS are producible (T2 produced one).

## T5 -- Consequence map and complete residues

Consequence map. A record-saturated region is locally final (T1), its local
record-time is halted (T2), and it constrains its boundary at the possibility
level without evolving (T3); any finite frozen region is producible, while the
globally frozen world is only a limit / datum in the finitary sector (T4). The
"frozen-star / black-hole-like" label is the owner interpretive READING of this
record-level picture and carries no GR content.

Complete residues (this campaign's #1 refutation failure mode is a dropped
residue, so the set is stated in full):

1. **PR #4874 in-flight** -- permanence is the premise for T1, T2, and the
   permanence half of T3; all are conditional on #4874 landing.
2. **Realized-sector / finitary scoping of T4** -- finite initial support plus
   finitely many registrations per step is a named scope, not a universal claim.
3. **Availability-rule dependence of T3** -- the axiom fixes the clause
   "determined by, and vary with, the nearest-neighbor conditions", not the
   specific rule; the exhibited rule is a note-level model.
4. **No rate / metric / clock content** anywhere; the landed count-not-rate
   firewalls are cited as review-pending / unaudited post-reset.
5. **Event-ordering matches the review-pending sibling** PR #4873 (branch-only,
   not read); its status is review-pending.
6. **No GR claims**; the frozen-star label is an interpretive reading only.
7. **Nothing adopted**; the static world's admissibility is the sibling's result
   rebuilt as an exact witness, not new content.
8. **Audit lane owns all statuses**; this note sets and predicts none.

## Consequence

Conditional on #4874 and within the note-level model, record saturation is the
end of local registration: a region becomes final (T1), its local event count
halts (T2), and it pins its boundary's available possibilities permanently yet
possibility-level, never a force or evolution law (T3). Globally the finitary
realized sector cannot saturate in finite record-time, so the infinite lattice
supports unbounded record-time (T4).

## Does NOT

This note does not assert GR content, rate, duration, metric, or clock; does not
choose a dynamics, Hamiltonian, transition rule, or record-production process;
does not fix the admissibility rule beyond the quoted clause; does not claim the
globally frozen world is produced (only that it is an admissible datum); does not
adopt, promote, or rule; and does not read the review-pending sibling or predict
any audit outcome.

## Dependencies

Lattice, Qubit, Admissibility, Record axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`,
quoted at checks 1-3); the permanence clause of PR #4874 (in-flight); the
supervisor-supplied covariant availability model and owner realized-sector ruling.
The event-ordering and static-world admissibility overlap the review-pending
sibling PR #4873 (cited, not read).

## No-Promotion

Nothing here is a Tier-A admission, primitive, axiom, or source of bounded status.
It prepares a reviewer-facing bounded/narrow theorem surface only. The audit and
review lanes own every status and landing decision; this worker draft hands off
and lands nothing.

## Summary (<=10 lines)

- T1: a saturated region is locally final; its `R`-restriction is forced constant by permanence + locks-exactly-one (exact `4^8` enumeration).
- T2: local record-time halts inside a saturated region while events continue outside (exact 4-stage witness; in-`R` counts `(4,4,0,0)`).
- T3: a saturated region permanently and covariantly pins its boundary's availability, with no force or evolution claim.
- T4: in the finitary realized sector, global saturation is unreachable at any finite stage; the infinite `Z^3` is load-bearing for unbounded record-time.
- T5: frozen-star label is an owner reading (no GR content); residues 1-8 are stated in full.
- Conditional on PR #4874; nothing adopted; audit lane owns all statuses; runner 27/27 exact checks PASS.
