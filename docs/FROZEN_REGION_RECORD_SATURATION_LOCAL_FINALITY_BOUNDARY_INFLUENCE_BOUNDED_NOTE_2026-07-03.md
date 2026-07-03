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
**Runner output:** `outputs/frontier_frozen_region_saturation_finality_2026_07_03.txt` (exact-arithmetic; int/tuple/set/frozenset only; 33/33 per-check PASS; nonzero exit on any FAIL)

## Firewall (read first)

- **Permanence is LANDED (commit 50f0db6187).** The Record restoration that
  replaces the locking clause's final segment "the locked possibility is
  invariant under repeated readout" with "records are permanent." is LANDED on
  main (commit 50f0db6187; drafted as PR #4874, review-loop-closed). Permanence
  yields DOMAIN MONOTONICITY (reading-free), the primary lever for T2's halting
  and T4's finite-lattice bound; T1's no-removal/no-alteration bars and T3's
  monotone containment also rest on it. These now ground on LANDED axiom text,
  with readout-invariance surviving as a derived lemma. This block grounds on
  the landed restoration: the runner's Record locking guard (check 1) keys to
  the current landed Record section (permanence at commit 50f0db6187, one-per-
  site at commit 7950d9202c). Supervisor-supplied.
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
- **Model postulate M1's one-per-site content is now LANDED axiom text (commit 7950d9202c, PR #4879).** After this
  note was drafted, the owner approved a one-per-site clause and it LANDED -- the
  Record axiom now reads "A site never carries more than one record." (commit
  7950d9202c, PR #4879 "axioms: restore one record per site"), separate from the
  earlier permanence restoration. M1's one-per-site content is therefore GROUNDED
  on landed axiom text, and the M1-based set-level results (T1's `4^8`
  enumeration, T4's distinct-record tail) no longer carry a reading residue. The
  site-functional one-record-per-site set individuation (below) now rests on the
  landed sentence; M1's mathematical content is unchanged.
- **Nothing adopted.** The event-ordering and static-world admissibility are
  REBUILT from scratch as small exact constructions; the review-pending sibling
  (PR #4882, recut of closed #4873, branch-only) is cited by number only and was not read. The audit
  lane owns all statuses.

## Purpose

State, at note level with exact finite witnesses, four bounded/narrow theorems
about record-saturated regions of `Z^3`: (T1) a saturated region is locally
final; (T2) its local record-time halts while events continue outside; (T3) it
exerts a MONOTONE possibility-level boundary constraint (containment in general,
exact singleton pinning for cavity sites) within the note-level model, without
any dynamical claim; (T4) global saturation is unreachable at any finite stage in
the named finitary realized sector, so the infinite lattice is load-bearing for
unbounded record-time. T5 gives the consequence map and the complete residue set.
The halting content (T2, T4's finite bound) is derived reading-free from domain
monotonicity; the record-SET content (T1's set-constancy, T4's distinct-record
tail) additionally uses model postulate M1.

## Supplied surface (quotes)

Axiom sentences quoted verbatim from `docs/MINIMAL_AXIOMS_2026-06-29.md` (merged
to current main; the runner's Record locking guard at check 1 keys to the current
landed Record section -- one-per-site landed at commit 7950d9202c (PR #4879),
permanence at commit 50f0db6187 (PR #4874); checks 2-5 match this merged file
verbatim):

- Record (locking): "When present, a record locks exactly one admissible local
  possibility. A site never carries more than one record; records are
  permanent." (current landed Record section; the one-per-site sentence "A site
  never carries more than one record." landed via commit 7950d9202c (PR #4879),
  and permanence "records are permanent." at commit 50f0db6187 (PR #4874), from
  which readout-invariance is a derived lemma. The check-1 guard keys to this
  current text.)
- Record (readout): "For any finite collection of pairwise-disjoint records,
  scalar readout `I` is additive, with `I(empty)=0`." (Honesty: quantifying over
  "pairwise-disjoint records" CONTEMPLATES non-disjoint, same-site records as a
  live axiom-level possibility and merely WITHHOLDS additivity from them; it does
  not bar them. Model postulate M1 elects the site-functional reading.)
- Admissibility: "For each site, the available possibilities are determined by,
  and vary with, the nearest-neighbor conditions" under "one fixed
  nearest-neighbor admissibility rule, covariant under lattice translations and
  proper cubic rotations."
- Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with
  nearest-neighbor adjacency, standard translations, and proper cubic rotations
  about each site."
- Qualification: "A state is a configuration of records."

Supervisor-supplied surface (not read from repo files; used as stated): the
permanence restoration that makes the Record locking clause end "records are
permanent." (readout-invariance becoming a derived lemma) is LANDED on main
(commit 50f0db6187; drafted as PR #4874, review-loop-closed). The one-per-site
clause "A site never carries more than one record." is LANDED via PR #4879
(commit 7950d9202c, "axioms: restore one record per site"). Owner ruling: non-triviality is contingent realized
data, not law (vacuum-solution analogy); theorems condition on the realized
sector. Sibling PR #4882 (recut of closed #4873; review-pending, branch-only, NOT read) derives the
event-ordering from permanence + "A state is a configuration of records",
exhibits the admissible static world, and carries an exact `2x2x2` saturation
witness with covariant boundary pinning -- rebuilt here from scratch. Owner
reading (a name, not a claim): a saturated region is "frozen-star /
black-hole-like" -- fully written reality, local time ended.

Note-level model (exactness firewall). A locked value is modelled by a scalar tag
in `{+1,-1}` -- the note-level image of the Record locking clause, NOT a claim
about the full one-site `M_2(C)` domain. A configuration is a partial map
site -> locked value. The availability model is `available_at(s) = { locked
values of records on nearest neighbors of s }` if nonempty, else `{+1,-1}`.

Domain monotonicity (permanence-derived, reading-free). Under permanence
("records are permanent.", LANDED -- commit 50f0db6187) plus "A state is a
configuration of records", a
realized history has record sets nested with agreeing values, so the
recorded-site domain grows monotonically: `dom(C_{t-1})` is a subset of
`dom(C_t)`. A FIRST-REGISTRATION (dom-event) at stage `t` is a site in
`dom(C_t) \ dom(C_{t-1})`. Monotonicity is the primary lever for T2's halting and
T4's finite-lattice bound; it needs no reading beyond permanence.

Model postulate M1 (one-per-site content now grounded on landed axiom text).
Reading "A state is a configuration of records" together with the singular "a
record locks exactly one admissible local possibility" phrasing, this note models
a state as a site-functional SET of records, each individuated as a pair
`(site, value)`, with at most one record per site. A same-value re-registration
at an already-recorded site is the SAME set element -- a non-event by IDENTITY,
not by prohibition. M1's one-per-site content is now GROUNDED on the LANDED axiom
sentence "A site never carries more than one record." (commit 7950d9202c,
PR #4879): "locks exactly one admissible local possibility" quantifies
possibilities per record, and the landed one-per-site sentence fixes records per
site directly (permanence separately bars removal and alteration); the readout
clause's "pairwise-disjoint records" contemplates non-disjoint (same-site)
records and merely withholds additivity from them. M1 elects the site-functional
individuation, now resting on landed axiom text. M1 is load-bearing ONLY where
flagged: T1's set-constancy `4^8` enumeration and T4's distinct-record pigeonhole
tail. Event layering: a same-value re-registration is a non-event under BOTH the
dom-based definition (no domain growth) and the M1 set definition (same element);
the two event notions agree on same-value re-registration and differ only on the
overlapping/multi-valued case, which the landed one-per-site sentence now excludes
and M1 models away.

## T1 -- Saturation implies local finality (bounded; M1 set-constancy grounded on landed one-per-site, commit 7950d9202c) [checks 6-12]

A region `R` is record-saturated in `C` iff every site of `R` carries a record.
Both exact windows -- the `2x2x2` (8-site) and `3x3x3` (27-site), one record per
site -- have zero registrable sites [checks 6-7].

Primary statement (dom-based, reading-free). Permanence makes the recorded-site
domain monotone. Once `R` is saturated, `R` is a subset of `dom(C_t)` at every
later stage, so no first-registration (dom-event) can ever occur in `R` again --
the `R`-restriction of the domain is final. This needs NO per-site uniqueness
[check 8].

Stronger statement (model-relative, uses M1). That the record SET on `R` is
constant is proven by exact enumeration over the `4^8` MODEL-RELATIVE candidate
later `R`-restrictions on the `2x2x2` window. The four-symbol per-site alphabet
`{absent, +1, -1, double}` is itself a modeling device: `absent` is removal and
each of `+1,-1` a possible locked value, while `double` -- a second, DISTINCT
record at an already-recorded site -- is inexpressible inside the partial-map
model and only multi-valued outside it. Permanence bars removal and alteration;
the `double` candidate is barred by model postulate M1 (site-functional set, at
most one record per site), NOT by "locks exactly one" (which quantifies
possibilities per record). Exactly one candidate survives and it equals `C|R`
[check 9]; the three barred kinds are each independently rejected [check 10].

Global corollary (rule-dependent, within the note-level model). A globally
saturated all-`(+1)` configuration is admissible against the EXHIBITED
availability rule -- every locked value lies in its neighbor-determined
availability set -- and readout is additive over disjoint sub-collections with
`readout(empty)=0` [check 11]; the check has teeth, since flipping one CORNER
site (the `2x2x2` block has no interior site) to `-1` amid `+1` neighbors makes
the configuration non-admissible [check 12]. Both verdicts are decided by the
exhibited covariant rule, not by axiom text: a different covariant admissibility
rule could reverse them (rule-dependence residue, extended to T1). Per the owner
ruling, the static globally saturated world is a legal solution (final and
physical, like a vacuum solution), not a defect.

## T2 -- Local record-time stops (bounded) [checks 13-19]

Primary statement (dom-based, reading-free). Permanence plus "A state is a
configuration of records" makes the recorded-site domain monotone along any
realized history; a first-registration (dom-event) at stage `t` is a site in
`dom(C_t) \ dom(C_{t-1})`. Once `R` is saturated, `R` is a subset of `dom(C_t)`
forever, so its in-`R` first-registration count halts -- local record-time in `R`
ends -- while first-registrations continue on the unsaturated complement. NO
per-site uniqueness is used.

Exact witness history (4 stages on a 16-site window; `R` = the `2x2x2` block):
record sets are nested with agreeing values so the domain is monotone [check 13];
`R` is unsaturated at stage 1, saturated at stage 2, so a frozen region is
produced [check 14]; per-stage in-`R` first-registration counts are `(4,4,0,0)`
[check 15] while outside-`R` counts are `(0,0,2,2)` [check 16]; the recorded-site
count in `R` is constant at 8 for stages 2,3,4 [check 17]; the outside count
strictly increases at stages 3 and 4 while `R` is frozen [check 18].

Event-definition layering (explicit). A same-value re-registration at an
already-recorded site is a NON-EVENT under BOTH definitions: it does not enlarge
the domain (dom-based), and it is the same `(site,value)` element (M1 set)
[check 19]. Frontier picture (count-level only): record-time flows exactly where
unwritten possibility remains.

## T3 -- Boundary influence without evolution (bounded) [checks 20-26]

General statement (monotone containment, within the note-level model). Under the
exhibited covariant neighbor-dependent availability rule, permanence makes the
recorded-neighbor value set at any site monotonically nondecreasing: once the
frozen region's value is available at a neighbor site (some recorded neighbor
carries it), it remains available FOREVER. Exact witness: a boundary site adjacent
to the saturated `2x2x2` block, whose in-`R` neighbor records `+1`, has `+1`
available at every stage and its recorded-neighbor value set never loses `+1`
[check 20]. A far site with no recorded neighbors retains `{+1,-1}` at every stage
[check 23].

The singleton pin is NOT permanent for a boundary site. A later ADMISSIBLE `-1`
record on a DIFFERENT neighbor of the boundary site relaxes its availability from
`{+1}` to `{+1,-1}` -- monotone containment of `+1` still holds, but the
singleton is broken [check 21]. Full singleton pinning holds EXACTLY for CAVITY
sites: a site all six of whose neighbors lie inside the saturated region has
availability `{+1}` at every stage regardless of any outside events (its neighbor
set is complete and permanent) -- checked on a `3x3x3` saturated shell with a
hollow (unrecorded) center [check 22].

The influence is possibility-level, not a force: the boundary and cavity sites
stay registrable (unrecorded) at every stage while their availability is
constrained [check 24] -- no record is placed on them, no evolution is asserted.
The rule is covariant under lattice translation [check 25] and under a proper
cubic rotation [check 26], matching the Admissibility clause.

Honesty scope. The availability rule is a NOTE-LEVEL model of the Admissibility
clause "determined by, and vary with, the nearest-neighbor conditions"; the axiom
fixes the clause, not the specific rule. The proven content is: monotone
containment in general, exact singleton pinning for cavity sites, and
witness-level pinning otherwise, all for the EXHIBITED covariant rule. The general
statement -- that ANY rule with determined-by + vary-with + covariance carries
SOME permanent boundary constraint from a saturated neighborhood -- is the named
conditional and is flagged as rule-dependence residue, not claimed here.

## T4 -- Global saturation unreachable at finite stage (narrow, scoped) [checks 27-33]

Scope (named realized-sector class): histories with finite initial record support
and finitely many registrations per step. Then the recorded set is finite at every
finite stage [check 27], because a finite union of finite sets is finite
[check 28]. Since `Z^3` minus a finite set is infinite, unrecorded sites remain
without bound: the unrecorded count in the `(2k+1)^3` window strictly increases as
`(25,122,339)` for `k=1,2,3` [check 29], and an explicit unrecorded witness
`(M+1,0,0)` sits outside the recorded bounding window at any finite stage
[check 30]. So global saturation is never reached at any finite stage; it is at
most a limit notion.

Finite-lattice bound. Primary statement (dom-based, reading-free): on an `N`-site
lattice the domain is monotone and bounded by `N`, so a saturating history has
exactly `N` first-registrations and every attempted `(N+1)`-th registration
yields zero domain growth (a forced non-event) [check 31]. A one-record-per-stage
history saturates in exactly `N` stages with zero registrable sites afterward
[check 32]. Stronger statement (model-relative, uses M1): under M1's
site-functional `(site,value)` individuation the saturated lattice carries
exactly `N` distinct record elements and a same-value re-registration adds none,
so no `(N+1)`-th DISTINCT record exists (the pigeonhole tail) [check 33].
Unbounded record-time therefore requires the infinite `Z^3` of the Lattice axiom
-- it is load-bearing. Consequence: the frozen WORLD is admissible as an
initial/boundary datum but is not producible from sparse beginnings in finite
record-time; frozen REGIONS are producible (T2 produced one).

## T5 -- Consequence map and complete residues

Consequence map. A record-saturated region is locally final (T1), its local
record-time is halted (T2), and it constrains its boundary at the possibility
level -- monotone containment in general, singleton pinning for cavity sites --
without evolving (T3); any finite frozen region is producible, while the globally
frozen world is only a limit / datum in the finitary sector (T4). The
"frozen-star / black-hole-like" label is the owner interpretive READING of this
record-level picture and carries no GR content.

Complete residues (this campaign's #1 refutation failure mode is a dropped
residue, so the set is stated in full):

1. **Permanence LANDED (commit 50f0db6187)** -- permanence ("records are
   permanent.") is the premise for the DOMAIN MONOTONICITY that grounds T2's
   halting and T4's finite-lattice bound, for T1's no-removal/no-alteration bars,
   and for the monotone-containment half of T3; all now ground on LANDED axiom
   text (drafted as PR #4874, review-loop-closed). Domain monotonicity itself is
   permanence-derived (reading-free) and is the load-bearing permanence
   consequence after the dom-based rederivation. The check-1 quote guard is live
   on the current landed Record section (permanence at commit 50f0db6187,
   one-per-site at commit 7950d9202c).
2. **Realized-sector / finitary scoping of T4** -- finite initial support plus
   finitely many registrations per step is a named scope, not a universal claim.
3. **Availability-rule dependence of T3** -- the axiom fixes the clause
   "determined by, and vary with, the nearest-neighbor conditions", not the
   specific rule; the exhibited union-over-recorded-neighbors rule is a note-level
   model, and the monotone-containment / cavity-singleton split is a property of
   THIS rule.
4. **No rate / metric / clock content** anywhere; the landed count-not-rate
   firewalls are cited as review-pending / unaudited post-reset.
5. **Event-ordering matches the review-pending sibling** PR #4882 (recut of closed #4873; branch-only,
   not read); its status is review-pending.
6. **No GR claims**; the frozen-star label is an interpretive reading only.
7. **Nothing adopted**; the static world's admissibility is the sibling's result
   rebuilt as an exact witness, not new content.
8. **Audit lane owns all statuses**; this note sets and predicts none.
9. **Model postulate M1 (site-functional set individuation; one-per-site content now LANDED as axiom text, commit 7950d9202c, PR #4879, via the sentence "A site never carries more than one record.")** -- the site-functional individuation of
   records as `(site,value)` with at most one per site, now grounded on landed
   axiom text so the M1 set-level results no longer carry a reading residue.
   Load-bearing for T1's set-constancy `4^8` enumeration and T4's distinct-record
   pigeonhole tail; NOT used for the dom-based halting content.
10. **Rule-dependence of T1's corollary** -- the all-`(+1)` admissibility verdict
    and the `-1`-flip control are decided by the exhibited covariant rule, not by
    axiom text; a different covariant rule could reverse both.

## Consequence

Grounded on the LANDED permanence restoration (commit 50f0db6187) and within the
note-level model, record saturation is the end of local registration: a region
becomes final (T1), its local event count halts (T2), and it constrains its
boundary's available possibilities -- monotone containment in general, singleton
only for cavity sites -- never a force or evolution law (T3). Globally the
finitary realized sector cannot saturate in finite record-time, so the infinite
lattice supports unbounded record-time (T4). The set-level refinements (T1's
set-constancy, T4's distinct-record tail) additionally use model postulate M1,
whose one-per-site content is now grounded on landed axiom text (commit 7950d9202c).

## Does NOT

This note does not assert GR content, rate, duration, metric, or clock; does not
choose a dynamics, Hamiltonian, transition rule, or record-production process;
does not fix the admissibility rule beyond the quoted clause; does not claim
general (non-cavity) singleton boundary pinning -- only monotone containment;
does not claim the globally frozen world is produced (only that it is an
admissible datum); does not adopt, promote, or rule; and does not read the
review-pending sibling or predict any audit outcome.

## Dependencies

Lattice, Qubit, Admissibility, Record axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`);
quote guards at checks 1-5 cover the Record locking sentence (check 1 keys to the
current landed Record section -- one-per-site at commit 7950d9202c, permanence at
commit 50f0db6187), the
Admissibility clause, "A state is a configuration of records." (M1's named basis),
the Lattice sentence, and the Record readout-additivity sentence -- Qubit is cited
but is not separately quote-guarded. Further premises: the LANDED permanence
clause "records are permanent." (commit 50f0db6187; drafted as PR #4874,
review-loop-closed); domain monotonicity (permanence-derived); model postulate M1
(residue 9; one-per-site content now grounded on landed axiom text, commit 7950d9202c); the
supervisor-supplied covariant availability model and owner realized-sector ruling.
The event-ordering and static-world admissibility overlap the review-pending
sibling PR #4882, recut of closed #4873 (cited, not read).

## No-Promotion

Nothing here is a Tier-A admission, primitive, axiom, or source of bounded status.
It prepares a reviewer-facing bounded/narrow theorem surface only. The audit and
review lanes own every status and landing decision; this worker draft hands off
and lands nothing.

## Summary (<=10 lines)

- Layering: the halting content is dom-based and reading-free -- permanence makes the recorded-site domain monotone, so first-registrations in a saturated region halt (T2) and an `N`-site lattice admits at most `N` first-registrations (T4).
- Model postulate M1 (site-functional set of `(site,value)` records, at most one per site) is load-bearing ONLY for the set-level statements: T1's `4^8` set-constancy enumeration and T4's distinct-record pigeonhole tail.
- T1: a saturated region is locally final (domain-level, reading-free); its record SET is forced constant under permanence + M1 (model-relative `4^8` enumeration).
- T3 (corrected): the boundary constraint is MONOTONE CONTAINMENT in general (the region value stays available forever), exact SINGLETON pinning only for CAVITY sites (all six neighbors inside `R`); a boundary singleton RELAXES under an admissible `-1` on a different neighbor -- all within the note-level model.
- T4: in the finitary realized sector, global saturation is unreachable at any finite stage; the infinite `Z^3` is load-bearing for unbounded record-time.
- T5: frozen-star label is an owner reading (no GR content); residues now number 10 (adds the M1 grounding note and T1-corollary rule-dependence).
- Permanence LANDED (commit 50f0db6187, drafted as PR #4874, review-loop-closed); one-per-site LANDED as PR #4879 (commit 7950d9202c; M1's set-level content grounded on it); the check-1 quote guard is live on the current landed Record section; nothing adopted; audit lane owns all statuses; runner 33/33 exact checks PASS.
