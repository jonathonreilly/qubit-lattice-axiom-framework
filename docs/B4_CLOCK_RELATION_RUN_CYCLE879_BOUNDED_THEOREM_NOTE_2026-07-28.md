# The B=4 relation run: a bounded finite-corpus measurement — constant-offset class coverage edges up, the within-key family stays sparse at declared caps, and a detector-selected 11-tick period appears on 16 clocks — Cycle 879

Date: 2026-08-04 (revised 2026-08-09, review-loop iterations 1–4; see
Review record)

Authority: none

Audit: unset

Status: bounded finite-corpus measurement, demoted from its original
headline by adversarial review (one worker-authored primary and one
independent checker spec'd to refute; no axiom surface touched).
Campaign/queue identifiers appear only under Provenance context below and
carry no naming weight.

Claim type: bounded_theorem (narrowed finite-corpus statements only; the
live surface is bounded-support and every claim is conditional on the
unaudited Cycle-719 substrate named under Imports)

Runners:

- [`frontier_cycle879_b4_clock_relation_2026_07_28.py`](../scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py)
- [`frontier_cycle879_b4_relation_independent_check_2026_07_28.py`](../scripts/frontier_cycle879_b4_relation_independent_check_2026_07_28.py)

Both runners are co-load-bearing: the per-comparison refutation
adjudication, the per-witness re-verification and the exact 16-clock
period census live in the independent checker, so no audit packet for
this note is complete without it (see Review record and the
`packet_helper_runner` declaration under Status fields).

Receipt:

- [`b4_clock_relation_cycle879_receipt_2026_07_28.json`](../outputs/b4_clock_relation_cycle879_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted; substitution disclosed). Checker independence
is cross-context, not cross-model. Independent audit still required.

## Scope, the declared box, and the disclosed deviations

The B=4 probe box is DECLARED by this package: 27 stations, 324 separated
placements, census 648 keys, events {0,1}, k=2, horizon 8,192 chunks —
re-derived from the landed Cycle-719 controller core and gated, never
quoted.  (Provenance context, non-load-bearing: the same box was first
named by an earlier unlanded exploration referred to as Cycle 866; no
landed Cycle-866 artifact exists on the main line, and nothing here
executes or inherits it.)  Measured corpus: 4,770,145 clock events (5.8x
B=3); longest clock 6,512 events.

Deviations from the Cycle-869 search declaration, disclosed in the
emitted pricing payload and re-priced by the checker: the cadence store
cap was set to the horizon rather than the unlanded exploration's nominal
1,024 (the nominal cap would have truncated 1,788 clocks and silently
discarded 1,956,769 events — both figures checker-recomputed); the
across-key representative cap was raised 600 -> 648 so it structurally
cannot bite (max observed 221); a dict lookup was replaced by a
gated-equivalent binary search.  No cap saturated.  CAVEAT carried on the
comparison table: the B=3 side (parsed from the sha-pinned LANDED
Cycle-869 cache) ran at the nominal store cap, so B-comparisons are
capped-vs-uncapped wherever the cap can matter.

Every cap, floor and qualitative boundary (the 8-event evidence floor,
the 1/2 partial-coverage floor, the 1/10 rarity boundary and 1/2 majority
boundary of the comparison-table rules, the period-detector walls, the
anchor and overlap floors) is an ANALYST-DECLARED operational boundary
condition, enumerated in the emitted `analyst_declared_thresholds` block;
none is derived from the axioms, the Cycle-719 kernel, or data, and every
conclusion is conditional on the full finite box.

## Within a key: the family-priced sparse residual persists, priced

436 of 8,171 substantive pair-of-pair comparisons carry a whole-cadence
dictionary in the declared family (5.3%, vs 2.7% at B=3); 427 are
identity-like containment and **9 move the tick values**.  A further 60
comparisons carry a genuinely partial lag overlap (all 60 tick-moving).
Bank clocks: 18/3,840 (4 non-identity), plus 5 partial.

The dictionary/partial split is measured under the ENFORCED partial
clause: the partial member may not carry a whole cadence onto another,
so a run covering the whole of either clock is published as the total
index-lag member.  An earlier revision of this package left that clause
declared but unenforced and reported 278 dictionaries / 269
identity-like / 218 partial; re-running the corpus with the clause
enforced re-expressed 158 whole-cadence maps as the total member and
re-parameterised 41 more onto genuinely partial lags, with no comparison
changing between "related" and "refused".  Two consequences of that are
load-bearing for the reader.  First, the refusal counts below — the
figures the negative rests on — are byte-identical across the change.
Second, the B=3 side of every comparison row is parsed from the landed
Cycle-869 cache, which does NOT enforce the clause, so the B=3 and B=4
dictionary magnitudes are not measured under identical member
conventions; the row's direction (weakened) is unchanged, but the
magnitudes are convention-sensitive and are read only as such.

Two family members fire for the first time at this scale: the
windowed time offset (F1W, 3 hits) and the periodic
residue law (F4) at P = 54 = exactly 2 orbits with rotation c in
{0, 27}.  The within-key refusals stand at B=4 exactly as at B=3: a
negative priced to the declared family, its caps and its horizon — never
a universal "no dictionary" claim — with a genuinely larger (still
small) exception set whose members are all emitted with witnesses, and
with the COMPLETE per-comparison disposition table and all 531 witness
records published in the primary's cache for independent adjudication.
The checker's wider search demonstrates the beyond-caps space is
populated (3,355 relations beyond the declared caps; see Checker), which
is exactly what the pricing predicts and never what the negative excludes.

## Across keys: class coverage edges up; the nonzero-offset property is unchanged

At FULL-CORPUS discipline from the start (the Cycle-875 standard; the
pair-only sub-corpus 3,094/3,094 with residue 371 is emitted labelled,
never as headline), the two obligations are kept separate:

- the nonzero-offset PROPERTY is exactly 1 at B=3 and exactly 1 at B=4
  (**5,085 of 5,085** constant-offset edges carry nonzero offsets):
  `PERSISTS_UNCHANGED`, not strengthened;
- the constant-offset CLASS COVERAGE rises slightly: 5,455 of 6,258
  sounding keys sit inside some nontrivial equal-gap-word class (87.2%,
  up from B=3's 86.4%); the uncovered residue is 803 keys; the gap-word
  factor layer holds 2,367 edges.

The constant offset inside a bucket follows from identical complete gap
words once origins differ; the measured content is the class occupancy
and the all-nonzero origin differences, and only those are claimed.

## The period finding: a detector-selected 11-tick tail on 16 clocks

Every period claim on both sides is DETECTOR-SELECTED under the declared
tail-ladder contract — not a least period, not a complete census.  At
B=3 all three detector-selected periods are whole 19-station orbits.  At
B=4 the detector selects seven period values; six are whole 27-station
orbits (27, 54, 81, 1512, 1971, 2214) — and **P = 11 is not** (11/27 of
an orbit).  The checker's exact census: precisely 16 canonical clocks
(8 bank + 8 pair, matching the published census exactly, by clock
identity, 128-152 events each, 6 residues each) survive the direct
membership adjudication t in S iff t+11 in S, and **P = 27 fails on
every one of those 16 clocks**.  The safe statement, and the only one
made: the declared detector finds a stable 11-periodic tail on 16 B=4
clocks; direct membership supports P=11 and rejects P=27 on exactly
those clocks; therefore the B=3-corpus observation "every
detector-selected period is a whole number of ring orbits" does not
extend to B=4.  No least-period, only-period, or complete-census claim
is made at either B.

## The comparison table (data, not narrative)

Against the landed sha-pinned Cycle-869 figures: 4 rows
PERSISTS_STRENGTHENED, 1 PERSISTS_UNCHANGED (the nonzero-offset
property), 3 PERSISTS_WEAKENED, 1 BREAKS_AT_B4 (the detector-selected
whole-orbit divisibility) — each row computed by its stated rule, with
the capped-vs-uncapped caveat attached to the WEAKENED labels and the
1/10 and 1/2 rule thresholds declared as analyst boundaries.

## What this does to the second-leg discharge map

The landed second-leg map of the evolution-axis premise (legacy alias:
B-AXIS; Cycle 875) carried "the ENTIRE B=4 relation-family run" as its
largest open row.  That row is now SUPPLIED with data.  It does not
auto-discharge leg (ii): the 9 non-identity within-key dictionaries and
the P=11 clock class must be adjudicated against the leg-(ii) conjunction
(record-native x global x independent-of-F) before the row's status moves
— the P=11 class is 16 clocks (prima facie local, not global), but
adjudication is a successor's job, not this note's.

## Checker

The checker rebuilds the substrate by a complementary route (single-zero
watched probe, reversed lane packing, swap-network masks; corpus sha
equal), replays 8 keys through the Cycle-719 reference step with zero
mismatches, and replicates every pinned number.  Its refutation surface
is PER-COMPARISON, never aggregate:

- the primary's complete disposition table (648 keys x 15 pair-clock and
  x 6 bank-clock comparisons) is parsed from the primary's pinned cache
  and matched comparison by canonical comparison — class structure
  (silent / saturated / comparable) agrees on all 13,608 comparisons;
- every comparison the primary admitted is re-found by the strictly
  wider search (0 admitted-but-empty);
- all 531 published witness records re-verify from their serialized
  parameters against each member's complete declared contract, with the
  identity-like flag recomputed per witness (0 mismatches; the 427
  identity-like substantive dictionaries recompute exactly);
- on every one of the 11,492 substantive comparisons the primary
  recorded as NO_RELATION_IN_F (7,675 pair + 3,817 bank), the primary's
  DECLARED box is searched EXHAUSTIVELY in both orientations — every
  member over its complete declared parameter range, never a first-hit
  search — so a within-caps witness cannot be masked behind a
  beyond-caps one: **0 within-caps refutations**, with the declared box
  recorded as exhausted on all 11,492; 3,355 beyond-caps relations
  (2,246 pair + 1,109 bank) are reported as priced surplus that the
  family-scoped negative explicitly does not exclude;
- the gate carries two permanent adversarial probes reproducing the two
  defects it was rebuilt against: a comparison whose first wide witness
  is beyond-cap while an in-cap total map exists (the exhaustive gate
  must find it), and a whole-clock partial witness (both verifiers must
  refuse it and the total member must accept the same map).  On this
  corpus the masking hole never bit — 0 of the 11,492 refusals had an
  in-cap witness that a first-hit gate would have missed — so the fix is
  behaviourally neutral on the refusal side and the hole is now closed
  by construction rather than by luck;
- the P=11 break gate is an EXACT canonical census (16 clocks, 8+8, all
  rejecting P=27), with three executed mutation controls — an understated
  published count, an injected extra supporting clock, and a
  saturation-closure double-support probe — each failing exactly the
  intended gate;
- the primary carries **15 verifier clause-regression probes** (malformed
  or contract-violating witnesses that the complete-contract verifier
  must refuse: non-canonical and offset-mismatched windowed-offset
  windows [2], unit and non-positive affine slopes [2], zero-step and
  negative-start index maps [2], a negative-lag whole-clock map [1],
  below-floor / out-of-bounds / below-coverage partial overlaps [3],
  whole-target and whole-source partial overlaps [2], and wrong-period /
  right-period-mismatch / transient-mismatch residue witnesses [3]),
  plus **3 search-side probes** that the emitted partial witness is
  never a whole cadence — **18 clause probes in total**, and the runner
  COUNTS them from the rows it emits rather than asserting a number:
  `C_FAMILY_CONTROLS.clause_probe_inventory` publishes the two counts
  and their total, and the gate fails if the executed inventory departs
  from the declared one.  The runner also emits a standing count of
  whole-cadence partial witnesses (0 pair, 0 bank) that gates its own
  within-key blocks;
- the import firewall on the primary is verified to fire, and both
  runners' scientific payloads are byte-stable across PYTHONHASHSEED.

Aggregate counts (wide-search identity and value-moving censuses) are
emitted as bookkeeping only and cannot carry any PASS.

## No-Go Discipline Gate

This section is the committed N1–N8 record for the negative content that
survives the demotion: ONE family-priced measured absence — the declared
relation family F (7 members, declared caps, horizon 8,192) refused a
witness in 7,675 of 8,171 substantive pair-of-pair and 3,817 of 3,840
substantive bank-clock comparisons at B=4 — plus the permanently open
family-closure wall (O1).  No `no_go` claim ships; this is a bounded,
family-priced measurement.  The N5 execution certificate (one line per
resolution class) is in the primary runner's cached stdout,
`logs/runner-cache/frontier_cycle879_b4_clock_relation_2026_07_28.txt`.
The gate closes NOT PASS (see Status at the end of this section): the
narrowed claims ship; nothing wider does.

**N1 — Alternative route enumeration.**
1. Exact dictionary inside the declared family at declared caps
   (relation-family route): ATTEMPTED — the primary exhausted F at its
   declared caps on all 12,453 comparable comparisons, with the complete
   per-comparison disposition table emitted.
2. Relation visible only beyond the declared caps (loosened-cap route):
   ATTEMPTED — the checker's strictly wider search (complete offset
   candidates, floor-8 partial lags, unexhausted index maps, every-anchor
   affine, full-border-chain periods) found 3,355 beyond-caps relations,
   all priced as surplus, none suppressed; and an exhaustive search of
   the primary's declared box on all 11,492 substantive refusals — every
   member, every declared parameterisation, both orientations — found 0
   within-caps relations with the box recorded exhausted on every one.
3. Value-moving relation misfiled as identity-like containment
   (identity route): ATTEMPTED — all 531 published witnesses re-verified
   per witness with recomputed identity flags; 0 misfiled.
4. Periodic-residue structure at detector granularity (period route):
   ATTEMPTED — detector-selected census adjudicated by direct membership
   with an exact canonical clock census; only divisibility arithmetic and
   listed-value support claimed (O4).
5. Across-key translation structure as a rival carrier (translation
   route): ATTEMPTED — every headline recomputed at every scope it could
   have been quoted at; the full corpus is the headline scope and the
   sub-corpora are labelled.
6. Transformations outside F, beyond the declared caps, or beyond
   horizon 8,192 (beyond-box route): NEITHER `ATTEMPTED` NOR `RULED OUT
   BY PRIOR` — attempting it would be new science outside this fix
   round, and no prior authority rules it out; the emitted pricing line
   says the opposite ("It does not exclude transformations outside F,
   nor relations that only appear beyond tick 8192").  Under N1's marker
   contract this enumerated, untested route is PASS-blocking.  It is
   carried as O1 (permanently open); see Status below.

Routes 1–5 satisfy N1's five-distinct-routes floor with permitted
markers; route 6 is enumerated for honesty and blocks PASS.

**N2 — Wall-independence audit.**  Open walls: O1 (family/caps/horizon
closure — unclosable by declaration), O2 (capped-vs-uncapped B=3
comparator), O3 (unaudited Cycle-719 substrate chain), O4
(detector-selection: no least-period or complete census), O5 (leg-(ii)
adjudication of the exception sets), O6 (P=11 mechanism
characterization).  All 15 unordered pairs, with both directional
closure answers and the resulting independence value:

| Pair | left closes right? | right closes left? | Independent? |
|---|---|---|---|
| O1–O2 | yes (vacuous: an all-family, all-caps, all-corpus exhaustion includes the uncapped B=3 re-run) | no | no — one-way; O1 is unclosable by declaration, so O2 is carried at its priced face (the capped-vs-uncapped caveat on every WEAKENED row) |
| O1–O3 | no | no | yes |
| O1–O4 | no (family exhaustion says nothing about period minimality) | no | yes |
| O1–O5 | no (the leg-(ii) conjunction is about record-nativeness and globality, not family membership) | no | yes |
| O1–O6 | no | no | yes |
| O2–O3 | no | no | yes |
| O2–O4 | no | no | yes |
| O2–O5 | no | no | yes |
| O2–O6 | no | no | yes |
| O3–O4 | no | no | yes |
| O3–O5 | no | no | yes |
| O3–O6 | no | no | yes |
| O4–O5 | no | no | yes |
| O4–O6 | no (a least-period census would name the periods, not their mechanism) | no (a mechanism for P=11 would not enumerate all periods) | yes |
| O5–O6 | no | no (characterizing the P=11 class informs but does not adjudicate the 9-dictionary leg) | yes |

Collapse: 14 pairs are independent; the one one-way dependency points
FROM O1 into O2, so O2 COLLAPSES under O1 per the pairwise contract.
The collapsed independent wall set is FIVE walls: {O1 (carrying O2 at
its priced face), O3, O4, O5, O6}, and the claim uses this collapsed set
everywhere.

**N3 — Hidden-wall scan.**  Iteration-1 review found three hidden
conditions; all are now explicit: the byte-specific unlanded-ancestor
dependency (repaired — every pinned input is now the landed-on-main
revision, verified by content sha and git blob), the unbound independent
checker (repaired — machine-readable `packet_helper_runner` declaration
plus explicit authority links under Imports), and the undeclared analyst
thresholds (promoted into the emitted `analyst_declared_thresholds`
block and the Declared scope inputs below).  The unaudited Cycle-719
substrate import is O3.  N2 was re-run after these promotions.

**N4 — Residual matching.**  Per-citation table (witness residual vs the
residual the claim needs, one row per load-bearing citation, including
the dropped row):

| Citation | Witness residual | Claimed residual | Match? |
|---|---|---|---|
| `logs/runner-cache/frontier_cycle879_b4_clock_relation_2026_07_28.txt` (D_WITHIN_KEY_PAIR_OF_PAIRS) | exact F-relations between pair clocks at declared caps at B=4, full disposition table | the pair part of the family-priced residual: 7,675/8,171 substantive refusals | yes |
| same cache (E_WITHIN_KEY_BANK_CLOCKS) | exact F-relations between bank clocks at declared caps at B=4 | the bank part: 3,817/3,840 substantive refusals | yes |
| `logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt` (landed; parsed by H_B_DEPENDENCE) | the B=3 side of every comparison row, measured at the nominal store cap | the B-dependence rows, carried with the capped-vs-uncapped caveat (O2) | yes (pricing-to-pricing; the caveat is load-bearing) |
| `logs/runner-cache/frontier_cycle879_b4_relation_independent_check_2026_07_28.txt` (E_REFUTATION_SEARCH) | the declared box exhausted on all 11,492 refused comparisons with 0 within-caps relations; 3,355 beyond-caps relations priced as surplus | the refusals stand within the declared caps and nothing wider is claimed | yes |
| same cache (G, L3) | exact 16-clock canonical P=11 census with P=27 rejected on every one | the detector-selected non-orbit period exists at B=4 (a positive counterexample, not a negative witness) | yes |
| the unlanded exploration referred to as Cycle 866 | probe-box provenance only | any authority role | **no — dropped**; provenance context only, carries nothing |

Each surviving claim rests on exactly the witnesses whose residuals it
names, which is sufficient support for the family-priced measured
residual and for nothing wider.

**N5 — Rhetoric audit.**  The surviving negative was checked across
per-element / per-site / per-mode / per-block / lattice-wide resolutions;
the five substantive resolution lines are committed in the primary's
cached stdout (N5_RESOLUTION_CERTIFICATE: per_element — every comparison
carries an explicit disposition, refusals family-priced; per_site —
per-clock census with exact cap-free saturation; per_mode — per-member
histograms, members outside F untested; per_block — all 648 per-key
disposition codes emitted; lattice_wide — NO lattice-wide negative is
claimed).  Every phrase wider than these resolutions was narrowed in
iteration 1; the note carries no lattice-wide negative.

**N6 — Partial-closure path scan.**  No registered primitive supplies a
family-closure or clock-identity lemma (axiom surface: four axioms, none
about clock identity; no approved primitive names it), and no
convention/labeling reframe closes O1 or O5 — both need theorems.  The
legitimate import-bearing path is named: a consuming theorem may import
the family-priced residual at its stated caps as a conditional input.

**N7 — Steelman.**  The strongest rival reading is live and stated: maps
outside F, longer horizons, alternative tail detectors, and the
checker's own 3,355 beyond-caps relations show the wider transformation
space is genuinely populated.  Nothing in this package excludes a
dictionary there; therefore no universal negative ships, and the
conclusion below carries the family qualifier in the same sentence as
the residual.

**N8 — Prior-lesson incorporation.**  The landed Cycle-869 review
lessons are incorporated rather than re-learned: exact keyed/canonical
set gates instead of count gates (here: per-comparison disposition
matching and the exact 16-clock census), detector-selection period
contracts instead of least-period language, complete-definition witness
verifiers with clause-regression probes, and provenance-only handling of
the unlanded Cycle-866 lineage.  All pinned ancestors are the
landed-on-main revisions.

**Status: NOT PASS** (`partial-attempt-with-named-untested-routes`): the
beyond-box route is neither attemptable in a fix round nor ruled out by
any prior, so the narrowed family-priced disposition, not PASS, is the
honest status.  The narrowed claims ship; no `no_go` claim exists to
ship.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the ENTIRE B=4 relation-family run (the largest open row of the second-leg discharge map of the evolution-axis premise, legacy alias B-AXIS, Cycle 875)"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "adjudicate the 9 non-identity dictionaries and the P=11 clock class against the leg-(ii) conjunction; characterize the P=11 clock class (which keys, which banks, what mechanism sets an 11-tick period on a 27-station ring)"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact witness-verified searches over a declared closed family at declared caps on one finite B=4 corpus; the within-key residual family-priced with its full disposition table published; the P=11 finding gated by an exact canonical brute-force census with executed mutation controls; the comparison table computed against the landed Cycle-869 cache with the capped-vs-uncapped caveat; all of it conditional on the unaudited Cycle-719 substrate"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/frontier_cycle879_b4_relation_independent_check_2026_07_28.py
```

The `packet_helper_runner` line is the machine-readable declaration that
the independent checker is a claim-scoped, co-load-bearing packet
source: no audit packet generated for this note is complete without that
runner, and at landing the citation-graph builder's explicit
packet-helper table must carry the matching entry (see Review record).

## Imports, declared scope, provenance, derived, open

### Imports (load-bearing)

- the Cycle-719 two-rail recurrent controller core
  ([`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py);
  sha-pinned by both runners, byte-identical to the landed main-line
  revision), whose source authority is
  [`RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md`](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md).
  Its audit ledger row is unaudited; every result here is CONDITIONAL on
  that upstream chain and support-only until it is independently
  retained (wall O3).
- the landed Cycle-869 B=3 runner and cache as the pinned comparison
  target
  ([`frontier_cycle869_clock_relation_2026_07_28.py`](../scripts/frontier_cycle869_clock_relation_2026_07_28.py)
  and its runner cache, both pinned at the landed-on-main revisions —
  cache sha256 `586fd6a6…`, runner sha256 `3ff406e5…` — and parsed,
  never assumed), whose source authority is
  [`LOCAL_CLOCK_RELATION_CYCLE869_BOUNDED_THEOREM_NOTE_2026-07-28.md`](LOCAL_CLOCK_RELATION_CYCLE869_BOUNDED_THEOREM_NOTE_2026-07-28.md).
- the Cycle-875 full-corpus headline standard and the second-leg
  discharge-map row this run supplies, whose source authority is
  [`BAXIS_SECOND_LEG_CERTIFICATE_CYCLE875_SUPPORT_NOTE_2026-07-28.md`](BAXIS_SECOND_LEG_CERTIFICATE_CYCLE875_SUPPORT_NOTE_2026-07-28.md).

### Declared scope inputs (stipulated boundary choices, not derived)

- B=4 fixture banks, 27 stations, horizon 8,192 chunks, the event-seeded
  k=2 census (648 keys), the store-at-horizon cap, the eight-event
  evidence floor, the 1/2 partial-coverage floor, the eight windowed
  offset anchors, the eight-event lag-overlap floor, the period-detector
  walls (tail window 2,048, tail floor 16, ladder ratio 3/4, block cap
  512, repeat floor 2), the eight-tick saturation-run floor, the 648
  representative cap, and the 1/10 rarity and 1/2 majority boundaries of
  the comparison-table rules.  These are normalizations, enumerated in
  the emitted `analyst_declared_thresholds` block; all claims are
  conditional on them.

### Provenance context (non-load-bearing)

- the exploration referred to as Cycle 866: no landed artifact exists on
  origin/main; it is probe-box provenance only, carries no authority,
  and nothing here executes or inherits it;
- owner campaign/queue identifiers (goal-queue item, PR branch): work
  provenance only, never scientific names.

### Derived (on this corpus, conditional on the imports above)

- the B=4 within-key decomposition with witnesses and the full
  per-comparison disposition surface (436 dictionaries / 427
  identity-like / 9 tick-moving of 8,171 substantive; 60 partial, all 60
  non-identity; bank clocks 18/3,840 with 4 non-identity, plus 5
  partial), measured under the enforced partial clause;
- the full-corpus across-key measurement (5,085/5,085 nonzero
  constant-offset edges — property unchanged from B=3; class coverage
  5,455/6,258 = 87.2%, up from 86.4%; 2,367 factor edges);
- the detector-selected period census (seven values; six whole-orbit)
  and the exact 16-clock P=11 non-orbit class with P=27 rejected on
  every member;
- the computed B-dependence table (4 strengthened / 1 unchanged / 3
  weakened / 1 breaks, capped-vs-uncapped caveat attached).

### Open

- the P=11 characterization (mechanism, key/bank incidence) — O6;
- the leg-(ii) adjudication of the new exception sets — O5;
- capped-vs-capped re-comparison if the audit lane wants the B=3 side
  uncapped too — O2 (priced face of O1);
- the family-closure wall — O1 (permanently open by construction).

## Review record (Sol, iterations 1–4, 2026-08-08/09 — FIX_THEN_PROCEED)

An adversarial review demoted this package from its original headline
("the translation law strengthens, the orbit law breaks") to the bounded
finite-corpus measurement stated above, and found that the committed
evidence did not yet support even the narrowed claims: the checker's
refutation, identity and period gates compared aggregate counts rather
than canonical objects; the note and receipt claimed nine mutation
controls that did not exist in any committed artifact; the witness
verifier skipped declared clauses for three members; both runners
load-bore on unlanded ancestor bytes; the audit row had no dependency
edges and no checker binding; and the negative shipped with no N1–N8
record or N5 certificate.  The original headline and any earlier
checklist for it must not be cited as a passed gate.

Fixes applied in this iteration: every pinned ancestor moved to the
landed-on-main revision (Cycle-869 runner/cache re-pinned by sha and git
blob; parse keys ported to the landed detector-scoped field names); the
primary now emits its complete per-comparison disposition table, all
witness records with serialized parameters, and the five-line N5
resolution certificate; the checker adjudicates per canonical comparison
(class structure, admitted-must-be-refound, per-witness re-verification
with recomputed identity flags, and an EXHAUSTIVE search of the
primary's declared box — every member, every declared parameterisation,
both orientations — on every refused comparison, so no within-caps
witness can be masked behind a beyond-caps one; aggregate budgets
demoted to bookkeeping); the false mutation claims were deleted
and replaced by controls that exist and run (three L3 census mutation
controls in the checker; fifteen verifier clause-regression probes and
three search-side whole-cadence probes — eighteen in total, counted by
the primary itself and published as
`C_FAMILY_CONTROLS.clause_probe_inventory`; two permanent
gate probes in the checker reproducing the masking and whole-clock
defects); the witness verifier enforces every declared clause for
every member, including the partial member's non-whole-cadence clause,
which moved 199 of the 531 published witness records onto their correct
member or parameters without moving a single refusal; the period
surfaces are detector-scoped end to end; the
translation headline is factored into the unchanged property and the
slightly-strengthened coverage; the within-key negative carries its
family qualifier in every sentence that states it; the analyst
thresholds are declared and inventoried; and the authority links,
`packet_helper_runner` declaration and N1–N8 record above were added.

Confirmation rounds 2 and 3 found two further defects, both fixed above.
Round 2: the refutation gate still adjudicated only the first witness the
wide search returned, and the partial member's declared
non-whole-cadence clause was declared but not enforced — the exhaustive
declared-box search, the enforced clause and the two permanent
confirmation-round probes are the fix, and re-running the corpus under
the enforced clause moved 199 of the 531 witness records onto their
correct member or parameters while leaving every refusal, every refusal
count and both headline tick-moving dictionary counts (9 pair, 4 bank)
exactly where they were.  Round 3: this note and the receipt claimed
eighteen VERIFIER clause probes when fifteen verifier probes and three
search-side probes exist — the prose above is corrected to that real
inventory, and the primary now counts the inventory from the rows it
emits and publishes it, so the number on this page and the number in
the code cannot drift apart again.  No probe was added or removed for
that correction and no measured figure moved.

Outstanding at landing (outside this PR's frozen file set), as hard
landing conditions: (a) add to `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
`docs/audit/scripts/build_citation_graph.py` the claim-scoped entry
mapping this note's claim id
`b4_clock_relation_run_cycle879_bounded_theorem_note_2026-07-28` to
`["scripts/frontier_cycle879_b4_relation_independent_check_2026_07_28.py"]`,
so the generated packet's helper closure carries the checker; (b)
co-land the citation-graph manifest acknowledgment for this note's node,
regenerated on the actual landing tree.  Do not spend an audit seat on
this row before both are done and the Cycle-719 chain is independently
retained.

## Verdict

On this finite B=4 corpus the declared family yields a sparse within-key
dictionary residual priced to the family, its caps and its horizon (9
tick-moving of 8,171 substantive comparisons, every disposition
published); inside observed equal-gap-word classes every constant-offset
edge is an exact nonzero time translation, with class coverage edging up
to 87.2% while the nonzero-offset property itself is unchanged from B=3;
and the declared detector finds a stable 11-tick tail on exactly 16
clocks of a 27-station ring, where direct membership supports P=11 and
rejects P=27 — so the B=3-corpus whole-orbit divisibility of
detector-selected periods does not extend to B=4, and nothing in the
landed story says why.  These are bounded measurements conditional on an
unaudited upstream substrate; independent audit is still required, and
no universal, least-period, or physical-symmetry claim is made.
