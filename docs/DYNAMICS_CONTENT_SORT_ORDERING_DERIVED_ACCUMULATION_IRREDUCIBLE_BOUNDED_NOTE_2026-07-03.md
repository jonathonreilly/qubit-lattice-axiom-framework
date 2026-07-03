# Dynamics Content Sort: Ordering Derived, Accumulation Irreducible, Bounded

**Date:** 2026-07-03
**Type:** bounded theorem + narrow no-go + governance map
**Status authority:** independent audit lane only. This worker note sets, predicts, and estimates no audit verdict; the audit lane owns every status.
**No-verdict sentence:** no audit verdict is applied, predicted, or requested here; nothing is adopted.
**Primary runner:** `scripts/frontier_dynamics_sort_records_accumulate_2026_07_03.py`
**Generated output:** `outputs/frontier_dynamics_sort_records_accumulate_2026_07_03.txt` (`TOTAL: PASS=30 FAIL=0`)

## FIREWALL (read first)

- Nothing is adopted by this note. No axiom text is changed here.
- Both candidate sentences are owner-surface flags only.
- T3 is axiom-first and narrow: it is relative to the five quoted sentences, not to all conceivable future axiom systems.
- All cited notes are review-pending or unaudited post the 2026-06-29 reset; the audit lane owns statuses.
- Supervisor-supplied context is quoted as supervisor-supplied, not read from files.
- No ledger, policy file, or audit-data surface is touched.
- The words "adopt", "promote", and "select" describe candidate options only; nothing here performs them.

## Purpose

This note separates four Dynamics questions that are easy to conflate, then maps the residue.

- T1 asks whether repeated-readout invariance already gives permanence across events.
- T2 asks what ordering follows once permanence is supplied or clarified.
- T3 asks whether accumulation, `H != 0`, or B-AXIS production content follows from the four quoted axioms.
- T4 maps the compression that results if the two owner surfaces are accepted, conserving every named residue.
- T5 states the governance surfaces and the TOE-leverage, adopting nothing.

The result is bounded support plus a narrow no-go, not an adoption event. The runner exhibits every claim on exact finite witnesses (`Fraction`/`int`/`set`/`str` only, no floats).

## Supplied Surface: Quotes

Minimal axiom memo, `docs/MINIMAL_AXIOMS_2026-06-29.md`:

> "A site need not carry a record."
> "When present, a record locks exactly one local possibility from the subset available at that site under Admissibility; the locked possibility is invariant under repeated readout."
> "Only records are readable. A readout value is determined by record content alone. For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`."
> "These axioms state only their named primitive content."
> "A state is a configuration of records."
> "A law privileges no states. Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer."
> "Admissibility is not a dynamics axiom."

Order/rate firewall, `docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`:

> "A record history supplies ordered words and counts. A supplied instrument kernel supplies probabilities per admitted step. A physical time metric or transition rate requires an additional clock/production normalization."

Nontriviality/selection firewall, `docs/DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md`:

> "The class contains `H = 0`, and it is closed under real linear combinations of allowed Hermitian terms."

Dynamics-form note, `docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`:

> "Gauge-covariance + locality + Hermiticity supply the **basis** of allowed local terms, not the combination."
> "It does **not** force non-trivial dynamics: `H = 0` is in the class."

Past-hypothesis arrow note, `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`:

> "boundary-condition / structural result; honest pinning, **not** a from-nothing derivation of the arrow."
> "The arrow's *existence* still requires the supplied low-entropy boundary"

Supervisor-supplied context (quoted as supervisor-supplied; not file-read here):

> "the banked pre-reset Dynamics proposal (branch-only, PR #4843) posited D1 H!=0 + D2 Dirac-branch"
> "D2 is now handled by the review-pending #4797 REALIZED_KINETIC_BRANCH family (Admissibility-variation selection)"
> "No step defines time via the anomaly"
> "d_t parity (ABJ premise) + d_t=1 (single-generator N5 cap) GIVEN the B-AXIS supplied-axis premise"
> "blocks #4854/#4855 (review-pending) name premise families P1-P4/CHART-MIX and C-add/POS/LOC"
> "The whole time cluster is unaudited post the 2026-06-29 reset."

## T1: Permanence Scope Gap (bounded theorem) [checks 01-06]

The quoted Record sentence locks a value "invariant under repeated readout". It does not literally say that later configurations cannot remove a record.

The runner builds a finite toy. A record is a `(site, locked-value)` pair; a configuration is a set of such pairs; sites are points of a finite window of `Z^3`. Three records are present, and one lattice site carries no record, so "A site need not carry a record." holds. The evolution-mortal step is an explicit map on configurations that removes exactly one pair.

Each quoted Record-axiom sentence is checked as an exact operation:

- readout idempotence: reading a record twice returns the same value and leaves the record unchanged [check 01];
- readout value is a pure function of record content [check 02];
- scalar readout `I` is additive over disjoint records with `I(empty)=0` [check 03];
- each present record locks exactly one Admissibility-available possibility [check 04].

Every quoted Record sentence holds BEFORE the step [check 05]. The mortal step then deletes one record; all other pairs are present, every quoted sentence still holds literally AFTER the step, yet the deleted record is gone [check 06]. The deleting step is not a readout, so it does not contradict the readout-invariance sentence read literally.

Conclusion: permanence-across-events is not derivable from readout-invariance alone. Owner option (a): the Record sentence's intent needs a clarity fix, matching the B13 pattern; candidate sentence "A record, once present, is permanent: no later configuration removes or alters it. Reading it changes nothing." Owner option (b): permanence is new content. This note flags the owner decision and adopts nothing.

## T2: Ordering Derived, Conditional On Permanence (bounded theorem) [checks 07-13]

Assume the T1 permanence sentence is accepted or otherwise supplied, and combine it with "A state is a configuration of records." Each state is then the set of its present records, and permanence says a later state contains every earlier record. Realized histories are therefore chains in record-set inclusion; forward is strict inclusion, i.e. strictly more records.

The runner exhibits a chain from zero to three records and checks the order laws exactly: reflexivity [check 07], antisymmetry [check 08], transitivity [check 09], and that the realized history strictly adds one record per step [check 10]. Strict monotone count forbids cycles: a return step would have to delete a record, which permanence forbids [check 11]. The order is relabel-invariant (a site permutation is an order isomorphism) and merge-monotone (`A <= B` gives `A|X <= B|X`) [check 12].

This derivation yields order and count only. The order/rate firewall protects the scope: "A record history supplies ordered words and counts... A physical time metric or transition rate requires an additional clock/production normalization." The runner embeds the same chain in two exact step-grids: order and counts are identical, but the count-per-step contrast is `1` versus `1/2`, so no rate, metric, clock, generator, or normalization is fixed here [check 13]. The past-hypothesis arrow note stays untouched: here "forward" is the inclusion direction, definitional after permanence, not a thermodynamic arrow. The arrow note remains "**not** a from-nothing derivation of the arrow", whose existence "still requires the supplied low-entropy boundary". Non-overlap is explicit: inclusion order does not import an entropy boundary, and the arrow note does not import inclusion order.

## T3: Accumulation Irreducible (narrow no-go, axiom-first) [checks 14-21]

The narrow no-go asks whether "something happens" follows from the four quoted axioms. It does not, on two exact witnesses.

Static witness. A fixed admissible configuration with the constant history (nothing ever changes) is guarded against each quoted axiom sentence individually, so the witness is sentence-complete rather than asserted:

- Lattice: every record's site is a `Z^3` point and no site is privileged (the identity law commutes with site relabeling) [check 14];
- Qubit: each locked value lies in the local possibility domain [check 15];
- Admissibility: the configuration is admissible at every element of the constant history [check 16];
- Record: "A site need not carry a record.", locks-exactly-one with readout-invariance, and additive readout all hold [check 17];
- "A state is a configuration of records.": every history element is a configuration of records [check 18];
- "A law privileges no states...": the identity law is total on configurations and single-valued [check 19].

The constant history registers zero new records, so accumulation is not forced while every quoted sentence holds [check 20].

`H = 0` witness. Even the form-class result contains the zero generator. The runner takes exact integer `2x2` generators: the zero generator commutes with the Gauss generator (member of the gauge-covariant class), a nonzero diagonal generator also commutes (the class is non-unique and closed), while an off-diagonal control does not commute (fails class membership) [check 21]. This restates, on an exact witness, the firewall "The class contains `H = 0`..." and the form note "It does **not** force non-trivial dynamics: `H = 0` is in the class."; "Gauge-covariance + locality + Hermiticity supply the **basis** of allowed local terms, not the combination."

Therefore any non-triviality content is genuinely new relative to the quoted axioms: "records accumulate", `H != 0`, and B-AXIS used as production or supplied-axis content. Candidate minimal record-vocabulary sentence: "Records accumulate: every admissible history registers new records; no final configuration is reached." This is candidate-only, the second owner surface, and not adopted here.

## T4: The Compression Map (bounded support) [checks 22-28]

For this map only, assume T1 permanence is clarified and T3 accumulation is supplied. Then:

- (a) production is definitional: an event is the registration of one record, and the production count along a permanence-respecting chain equals the count delta [check 22];
- (b) block #4854's `P2`/`P3` discharge exactly: `P2` maps to the permanence clarity sentence, `P3` to the accumulation sentence; the map is total and touches only `P2`,`P3` (`P1`/`P4`/`CHART-MIX` untouched) [check 23];
- (c) block #4855's `C-add`: chain concatenation supplies step composition (associative, additive counts); the kernel-convolution clause is NOT auto-supplied and becomes a named derivation target from one-parameter composition + locality + record-compatibility [check 24];
- (d) the landed conditional ladder re-hangs, each rung carrying its named premise: form forced (bounded bridges) -> Stone-unique generator (given the B-AXIS axis) -> `d_t` parity (ABJ external premise) -> `d_t = 1` (single-generator N5 cap) -> Dirac branch (review-pending #4797); nothing beyond form/Stone is marked unconditional and the terminal rung is review-pending [check 25];
- (e) the ordering-to-lattice-transfer-axis bridge is a NAMED OPEN derivation target: T2's ordering outputs are exactly `{order, count}`, and B-AXIS is not among them, so ordering alone does not hand the anomaly work its B-AXIS transfer construction [check 26];
- (f) permanent non-goals stay non-goals: rate/metric/clock (landed no-gos), arrow beyond the past hypothesis, and ABJ premise externality are never moved into the discharged set [check 27].

Complete residue enumeration (the conservation rule; nothing dropped, nothing adopted) [check 28 checks closed-vocabulary status, the expected row count, and that no row carries an adoption or promotion status]:

| Item | Role under this map | Status in this note |
|---|---|---|
| Record permanence clarity | T1 owner surface; discharges `P2` if accepted | owner-surface flag only |
| Records accumulate | T3 owner surface; discharges `P3` and the D1/`H != 0` role if accepted | owner-surface flag only |
| `P1` | named #4854 premise family member | conserved, not analyzed here |
| `P2` | permanence premise | maps to T1 sentence |
| `P3` | production/accumulation premise | maps to T3 sentence |
| `P4` | named #4854 premise family member | conserved, not analyzed here |
| `CHART-MIX` | named #4854 premise family | conserved as external family |
| `C-add` | #4855 composition premise | chain-concatenation support |
| `POS` | #4855 premise family member | conserved, not discharged here |
| `LOC` | #4855 premise family member | conserved; kernel-target ingredient |
| Kernel convolution | composition + locality + record-compatibility clause | NAMED derivation target (open) |
| One-parameter composition | kernel-target ingredient | conserved |
| Record-compatibility | kernel-target ingredient | conserved |
| B-AXIS supplied-axis premise | axis premise in the anomaly/time cluster | NOT supplied by ordering |
| Ordering-to-transfer-axis bridge | inclusion order -> transfer-axis construction | NAMED open target |
| D1 `H != 0` | pre-reset nontriviality role (PR #4843) | compressed by accumulation if owner accepts |
| D2 Dirac branch | branch-selection role (PR #4843) | handled by review-pending #4797 family |
| Form forced | landed conditional form-class result | landed-given-bridges; re-hangs before generator work |
| Stone-unique generator | landed, given axis | landed-conditional on axis |
| ABJ premise | external parity premise | unchanged external |
| `d_t` parity | consequence supplied from ABJ premise | unchanged |
| `d_t = 1` | single-generator N5 cap step | named premise |
| Dirac branch #4797 | REALIZED_KINETIC_BRANCH (Admissibility-variation) | review-pending external |
| Past-hypothesis boundary | arrow note residual (universal-floor) | carried open, permanently out of scope |
| Rate / metric / clock | order/rate firewall non-goals | permanent no-go, out of scope |
| All cited notes | unaudited post the 2026-06-29 reset | carried open; audit lane owns |
| Audit statuses | audit-lane authority | untouched |

The compression map erases no named premise or residual. It only records which items collapse if the two owner surfaces are accepted, and which named externals survive regardless.

## T5: Governance Map [checks 29-30]

Exactly two owner surfaces are produced [check 29]:

1. the Record-axiom permanence clarity fix: "A record, once present, is permanent: no later configuration removes or alters it. Reading it changes nothing." (a clarity fix, not new content);
2. the accumulation sentence: "Records accumulate: every admissible history registers new records; no final configuration is reached." (new axiom content, the only genuinely new sentence in the entire Dynamics question).

Panel plan: a blind panel hones both sentences with T1-T4 as acceptance tests; then the owner rules; then a premise-hash wave follows if wording is accepted. Nothing is adopted here, and the audit lane owns all status changes.

TOE-leverage statement [check 30]: one sentence plus one clarity fix replace the B-AXIS/`H != 0` premise load across the time cluster. The runner maps the accumulation sentence to the `H != 0` role and the permanence clarity fix to the B-AXIS-feeding ordering work, and checks that the named externals (ABJ, supplied-axis, past-hypothesis) stay external. Conditional on owner acceptance, the conditional ladder then becomes unconditional except for those named externals.

## Consequence

- Readout-invariance alone gives no permanence-across-events theorem (T1).
- Permanence gives inclusion order; inclusion order gives count and orientation only (T2), firewall-scoped away from rate/metric/clock.
- Accumulation is new content relative to the four quoted axioms (T3).
- The two owner surfaces, if accepted, replace a broad pre-reset Dynamics import with record-vocabulary text while preserving every named external (T4, T5).

## Does NOT

- Does not change any axiom, and does not adopt either candidate sentence.
- Does not derive physical time, rate, metric, clock, or generator scale.
- Does not derive the thermodynamic arrow beyond the past-hypothesis residual.
- Does not derive the ABJ input, the B-AXIS transfer construction from ordering alone, or the kernel-convolution theorem.
- Does not edit audit data, policy files, or ledger surfaces, and does not read any file outside the five quoted notes.

## Dependencies

- Quoted axiom memo: `docs/MINIMAL_AXIOMS_2026-06-29.md`
- Quoted nontriviality firewall: `docs/DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md`
- Quoted order/rate firewall: `docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`
- Quoted form-class note: `docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`
- Quoted arrow note: `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`
- Supervisor-supplied, not file-read here: PR #4843, #4797, #4854, #4855, and the anomaly/time-cluster context.

## No-Promotion

This note is a draft support artifact for supervisor review. It gives bounded-theorem checks, a narrow no-go, and a governance map. It makes no package-status claim, predicts no audit outcome, and requests no audit outcome. The owner-surface sentences remain flags. The named open targets remain open: kernel convolution from one-parameter composition + locality + record-compatibility, and the ordering-to-lattice-transfer-axis bridge.

## Summary

- Runner: 30 exact checks, `TOTAL: PASS=30 FAIL=0`, no floats.
- Owner surface 1 (clarity fix): "A record, once present, is permanent: no later configuration removes or alters it. Reading it changes nothing."
- Owner surface 2 (new content): "Records accumulate: every admissible history registers new records; no final configuration is reached."
- Compression-map named targets: kernel convolution from one-parameter composition + locality + record-compatibility; ordering-to-lattice-transfer-axis (B-AXIS) bridge.
