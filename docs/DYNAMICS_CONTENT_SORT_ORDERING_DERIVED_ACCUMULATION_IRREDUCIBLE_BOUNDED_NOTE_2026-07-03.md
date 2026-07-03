# Dynamics Content Sort: Ordering Derived, Accumulation Irreducible, Bounded

**Date:** 2026-07-03
**Type:** bounded theorem + narrow no-go + governance map
**Status authority:** independent audit lane only. This worker note sets, predicts, and estimates no audit verdict; the audit lane owns every status.
**No-verdict sentence:** no audit verdict is applied, predicted, or requested here; nothing is adopted.
**Primary runner:** `scripts/frontier_dynamics_sort_records_accumulate_2026_07_03.py`
**Generated output:** `outputs/frontier_dynamics_sort_records_accumulate_2026_07_03.txt` (`TOTAL: PASS=35 FAIL=0`)

## FIREWALL (read first)

- Nothing is adopted by this note. No axiom text is changed here.
- Both candidate owner surfaces are flags only.
- T3 is axiom-first and narrow: it is relative to the 20 enumerated axiom-block sentences (the four axiom sections plus the Qualification block), not to all conceivable future axiom systems.
- All cited notes are review-pending or unaudited post the 2026-06-29 reset; the audit lane owns statuses.
- The five source docs' quoted sentences are guarded LIVE against the files (whitespace-normalized substrings), so no quote is dead data. Supervisor-supplied context (PR numbers, cluster wiring) is quoted as supervisor-supplied, not read from files.
- No ledger, policy file, or audit-data surface is touched.
- The words "adopt", "promote", and "select" describe candidate options only; nothing here performs them.

## Purpose

This note separates four Dynamics questions that are easy to conflate, then maps the residue.

- T1 asks whether repeated-readout invariance already gives permanence across events.
- T2 asks what ordering follows once permanence is supplied or clarified.
- T3 asks whether accumulation, `H != 0`, or B-AXIS production content follows from the four quoted axioms.
- T4 maps the compression that results if the two owner surfaces are accepted, conserving every named residue.
- T5 states the governance surfaces and the TOE-leverage, adopting nothing.

The result is bounded support plus a narrow no-go, not an adoption event. The runner exhibits every claim on exact finite witnesses (`Fraction`/`int`/`set`/`str` only, no floats), and it guards every quote against its source file.

## Supplied Surface: Quotes

The runner reads these five source docs and checks each quoted sentence below as a live, whitespace-normalized substring of the file (backticks/emphasis stripped). The old dead-data failure mode -- quoted constants never compared to files -- is closed.

Minimal axiom memo, `docs/MINIMAL_AXIOMS_2026-06-29.md`, Lattice / Qubit / Admissibility / Record sections plus the Qualification block. The runner enumerates every sentence of these blocks as one `SENTENCES` list of 20 entries, including both no-privilege distinction clauses, the `M_2(C)` sentence, both covariance sentences, the state sentence, and the law sentence. A representative subset:

> "A site need not carry a record."
> "When present, a record locks exactly one local possibility from the subset available at that site under Admissibility; the locked possibility is invariant under repeated readout."
> "Only records are readable. A readout value is determined by record content alone. For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`."
> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."
> "For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions."
> "No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone."
> "These axioms state only their named primitive content."
> "A state is a configuration of records."
> "A law privileges no states. Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer."

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

## The One Covariant Availability Rule

Every witness below runs on ONE Admissibility rule, so no witness smuggles a fiat or coordinate-keyed selection:

> `available_at(s)` = the set of locked values of records on the nearest neighbors of `s`, if that set is nonempty; else the full possibility set `{+1, -1}`. Conflicting neighbor values give their union.

This rule is determined by the nearest-neighbor conditions, varies with them, references only relative neighbor offsets (so it is covariant under lattice translations and proper cubic rotations), and selects possibilities only through supplied structure (neighbor record content), never through the site's own coordinates. The runner checks covariance (translate the whole configuration, including an odd-parity shift that flips coordinate parity; availability commutes -- and likewise for a proper cubic rotation), variation (two sites with different neighbor conditions carry different available sets), and no-fiat-privilege (two sites of different parity share an available set; availability equals the neighbor-value set). This is the direct repair of the earlier parity-keyed toy, which violated the covariance and vary-with clauses of Admissibility and the no-privilege clause of Qubit.

## Source Liveness (quotes are live) [checks 01-03]

- All 20 enumerated axiom-block sentences are live substrings of the axioms file, with a per-sentence pass report [check 01].
- The six firewall/form/arrow quoted sentences are live substrings of their four source files [check 02].
- The T1 option (a) in-file intent evidence is live: the axiom heading and the durable-realized-outcome lineage line [check 03].

## T1: Permanence Scope Gap (bounded theorem) [checks 04-12]

The quoted Record sentence locks a value "invariant under repeated readout". It does not literally say that later configurations cannot remove a record.

The runner builds a finite toy on the covariant rule above. A record is a `(site, locked-value)` pair; a configuration is a set of such pairs; sites are points of `Z^3`. The shared configuration `C_STAR` has a `+1` domain and a `-1` domain meeting at a boundary plus a leaf, so several lattice sites carry no record and "A site need not carry a record." holds. The evolution-mortal step is an explicit map on configurations that removes exactly one pair.

Each quoted Record-axiom sentence is checked as an exact operation:

- readout idempotence: reading a record twice returns the same value and leaves the record unchanged [check 04];
- readout value is a pure function of record content [check 05];
- scalar readout `I` is additive over disjoint records with `I(empty)=0` [check 06];
- each present record locks exactly one Admissibility-available possibility under the covariant rule [check 07].

Every quoted Record sentence holds BEFORE the step [check 08]. The runner then exhibits the Admissibility rule's own clauses on `C_STAR`: covariance under translation (including an odd-parity shift) and proper cubic rotation [check 09]; variation, two sites with different neighbor conditions carrying `{+1}` versus `{+1,-1}` [check 10]; and no-fiat-privilege, different-parity sites sharing an available set because availability reads neighbor content only [check 11].

The mortal step then deletes the `(0,0,0)` record. All surviving records are still admissible under the covariant rule, and the geometry is chosen so that each survivor's locked value stays inside its (possibly changed) available set; the availability at `(0,1,0)` changes from `{+1,-1}` to `{-1}`, exhibiting the vary-with clause in action; every quoted Record sentence still holds literally AFTER the step, yet the deleted record is gone [check 12]. The deleting step is not a readout, so it does not contradict the readout-invariance sentence read literally.

Conclusion: permanence-across-events is not derivable from readout-invariance alone. The owner decision is OPEN and this note does not foreclose it:

- Owner option (a): the Record sentence's intent needs a clarity fix, matching the B13 pattern. The in-file intent evidence is the axiom heading "Record / Fixed Reality" and the memo's lineage line, quoted verbatim: "The 2026-06-05 Record axiom named durable realized-outcome registration and gave a `K`/CPT orbit reading once a finite central-sector readout context and fixed `K`/CPT conjugation were supplied." Candidate clarity sentence: "A record, once present, is permanent: no later configuration removes or alters it. Reading it changes nothing."
- Owner option (b): permanence is new content.

This note flags the owner decision and adopts nothing; whether (a) or (b) holds stays an open owner call.

## T2: Ordering Derived, Conditional On Permanence (bounded theorem) [checks 13-21]

Assume the T1 permanence sentence is accepted or otherwise supplied, and combine it with "A state is a configuration of records." Each state is then the set of its present records, and permanence says a later state contains every earlier record. Ordering by record-set inclusion is therefore a **partial** order, not a total or strict one.

The runner exhibits the partial-order laws exactly on the states `{}`, `{A}`, `{A,V}`, `{A,V,R}`: reflexivity [check 13], antisymmetry [check 14], transitivity [check 15]. It then supplies a **realized history** -- a sequence of states -- with idle steps and a multi-registration step: `[{}, {}, {A}, {A}, {A,V,R}]`. Forward inclusion holds at every step, and the idle steps give **equal** consecutive states, unordered by records alone [check 16]. Strict increase happens exactly at the two registration events; the step from `{A}` to `{A,V,R}` registers two records at once, and `registration_events` sums the set-differences `|S_{i+1} \ S_i|` to `3` [check 17].

Because idle steps leave the record-set fixed, record-time is EVENT-time: the history has four steps but only three distinct record-states and two registration events, so record-time is strictly coarser than step-time [check 18]. This is exactly what the count-not-rate firewall protects: "A record history supplies ordered words and counts... A physical time metric or transition rate requires an additional clock/production normalization." Idle steps advance step-time without advancing record-time, and record-history order says nothing about the gap.

A strict decrease would require deleting a record, which permanence forbids, so there are no cycles [check 19]. The order is relabel-invariant (a site permutation is an order isomorphism) and merge-monotone (`A <= B` gives `A|X <= B|X`) [check 20]. Finally, the firewall scope: the same strict chain embedded in two exact step-grids has identical order and counts, but the count-per-step contrast is `1` versus `1/2`, so no rate, metric, clock, generator, or normalization is fixed here; forward is the definitional inclusion direction, not a thermodynamic arrow [check 21]. The arrow note stays untouched and non-overlapping: it remains "**not** a from-nothing derivation of the arrow", whose existence "still requires the supplied low-entropy boundary"; inclusion order imports no entropy boundary, and the arrow note imports no inclusion order.

The realized history is an explicit IMPORT: the axioms have no history vocabulary, so a supplied sequence of states is a modeling ingredient, carried as a residue row, not derived.

## T3: Accumulation Irreducible (narrow no-go, axiom-first) [checks 22-25]

The narrow no-go asks whether "something happens" follows from the four quoted axioms. It does not, on two exact witnesses.

Static witness. The fixed admissible configuration `C_STAR` with the constant history (nothing ever changes) is admissible under the covariant rule at every element of the history [check 22]. It is then guarded against every one of the 20 enumerated axiom-block sentences individually, with a per-sentence pass report, so the witness is genuinely sentence-complete rather than checked against a hand-picked subset [check 23]. Each sentence maps to an exact predicate on the witness: sites are `Z^3` points and the identity law is site-equivariant (no site privileged); locked values lie in the two-value `M_2(C)` domain and the value-flip is a symmetry (no possibility privileged); the one covariant Admissibility rule is covariant and varies with neighbors; the three Record sentences (need-not-carry, locks-one with readout-invariance, additive readout) hold; every state is a configuration of records; and the identity law is total and single-valued, privileging no state. The constant history registers zero new records, so accumulation is not forced while every one of the 20 sentences holds -- no sentence forces change [check 24].

`H = 0` witness. Even the form-class result contains the zero generator. The runner takes exact integer `2x2` generators: the zero generator commutes with the Gauss generator (member of the gauge-covariant class), a nonzero diagonal generator also commutes (the class is non-unique and closed), while an off-diagonal control does not commute (fails class membership) [check 25]. This restates, on an exact witness, the firewall "The class contains `H = 0`..." and the form note "It does **not** force non-trivial dynamics: `H = 0` is in the class."; "Gauge-covariance + locality + Hermiticity supply the **basis** of allowed local terms, not the combination."

Therefore any non-triviality content is genuinely new relative to the quoted axioms: "records accumulate", `H != 0`, and B-AXIS used as production or supplied-axis content. The candidate accumulation sentence is the second owner surface, presented in T5 as a quantifier-honest pair of forms and adopted nowhere here.

## T4: The Compression Map (bounded support) [checks 26-33]

For this map only, assume T1 permanence is supplied and T3 accumulation is supplied. Then:

- (a) production is definitional: an event is the registration of one record, and the production count along a permanence-respecting chain equals the count delta [check 26]; `registration_events` sums the set-differences `|S_{i+1} \ S_i|`, so a multi-registration step `{} -> {r1,r2}` counts `2` and the realized history with idle steps counts `3` [check 27];
- (b) the single discharge map (identical here and in the runner): P3 (persistence) maps to the permanence sentence; P2 (production) maps to the accumulation sentence -- FORM-E discharges `P2` directly, FORM-H discharges `P2` via the definitional move event := registration-step; the map touches only `P2`/`P3` (`P1`/`P4`/`CHART-MIX` untouched) [check 28];
- (c) block #4855's `C-add`: chain concatenation supplies step composition (associative, additive counts); the kernel-convolution clause is NOT auto-supplied and becomes a named derivation target from one-parameter composition + locality + record-compatibility [check 29];
- (d) the landed conditional ladder re-hangs, each rung carrying its named premise: form forced (bounded bridges) -> Stone-unique generator (given the B-AXIS supplied axis, which stays external) -> `d_t` parity (ABJ external premise) -> `d_t = 1` (single-generator N5 cap) -> Dirac branch (review-pending #4797); nothing beyond form/Stone is marked unconditional and the terminal rung is review-pending [check 30];
- (e) the ordering-to-lattice-transfer-axis bridge is a NAMED OPEN derivation target: T2's ordering outputs are exactly `{order, count}`, and B-AXIS is not among them, so ordering alone does not hand the anomaly work its B-AXIS transfer construction [check 31];
- (f) permanent non-goals stay non-goals: rate/metric/clock (landed no-gos), arrow beyond the past hypothesis, and ABJ premise externality are never moved into the discharged set [check 32].

Complete residue enumeration is the conservation rule: nothing dropped, nothing adopted. The table below is the single source of truth; the runner PARSES it from this note, counts the rows, checks that every required key is present, and checks that no status cell carries an adoption or promotion token [check 33].

| Item | Role under this map | Status in this note |
|---|---|---|
| Record permanence premise (T1 owner surface; OPEN (a) clarity / (b) new-content) | discharges `P3` if accepted | owner-surface flag only |
| Accumulation sentence FORM-E (per-event) | discharges `P2` directly | owner-surface flag only |
| Accumulation sentence FORM-H (per-history) | discharges `P2` via definitional event | owner-surface flag only |
| P1 (#4854 premise family) | named premise family member | review-pending; carried open |
| P2 production premise | production premise | maps to accumulation sentence |
| P3 persistence premise | persistence premise | maps to permanence sentence |
| P4 (#4854 premise family) | named premise family member | review-pending; carried open |
| CHART-MIX (#4854 premise family) | named premise family | review-pending; carried external |
| C-add (#4855 composition premise) | chain-concatenation support | review-pending; carried open |
| POS (#4855 premise family) | named premise family member | review-pending; carried open |
| LOC (#4855 premise family) | kernel-target ingredient | review-pending; carried open |
| Kernel-convolution clause (composition + locality + record-compatibility) | named derivation target | derivation target (open) |
| One-parameter composition (kernel-target ingredient) | kernel-target ingredient | carried open |
| Record-compatibility (kernel-target ingredient) | kernel-target ingredient | carried open |
| B-AXIS supplied-axis premise (EXTERNAL) | axis premise in the anomaly/time cluster | external premise; not supplied by ordering |
| Ordering-to-transfer-axis (B-AXIS) bridge | inclusion order -> transfer-axis construction | derivation target (open) |
| D1 H!=0 (PR #4843) | pre-reset nontriviality role | compressed by accumulation surface if owner accepts |
| D2 Dirac branch (PR #4843) / #4797 review-pending | branch-selection role | review-pending external |
| Form-forced (gauge-invariant-local class) | landed conditional form-class result | landed-given-bridges |
| Stone-unique generator (given axis) | landed, given axis | landed-conditional |
| ABJ parity external premise | external parity premise | external premise; unchanged |
| d_t parity (consequence from ABJ premise) | consequence supplied from ABJ premise | named premise |
| d_t=1 single-generator N5 cap | single-generator cap step | named premise |
| Past-hypothesis boundary (universal-floor) | arrow note residual | carried open; permanently out of scope |
| Rate no-go (record order/count) | order/rate firewall non-goal | permanent no-go |
| Metric no-go (record order/count) | order/rate firewall non-goal | permanent no-go |
| Clock no-go (record order/count) | order/rate firewall non-goal | permanent no-go |
| Realized-history import (supplied sequence of states) | modeling ingredient; axioms have no history vocabulary | import; carried open |
| All cited notes: unaudited post 2026-06-29 reset | post-reset status of every cited note | carried open; audit lane owns |
| Audit statuses (audit-lane authority) | audit-lane authority | untouched |

The compression map erases no named premise or residual. It only records which items collapse if the two owner surfaces are accepted, and which named externals -- B-AXIS foremost -- survive regardless.

## T5: Governance Map [checks 34-35]

Exactly two owner surfaces are produced [check 34]:

1. the Record-axiom permanence sentence: "A record, once present, is permanent: no later configuration removes or alters it. Reading it changes nothing." The owner decides whether this is (a) a clarity fix or (b) new content; this note does not foreclose that call, and carries the T1 in-file intent evidence for (a) without ruling on it.
2. the accumulation sentence, presented as a quantifier-honest pair of forms, adopting neither:
   - FORM-E (per-event): "Every step of a realized history registers at least one new record." This is the stronger form; it makes record-time equal to step-time and discharges #4854's `P2` directly.
   - FORM-H (per-history): "Records accumulate: every realized history keeps registering new records; no configuration is final." This is the weaker form; it permits idle steps, and `P2` discharges only via the definitional move event := registration-step.

The trade is stated plainly and left for the panel: FORM-E buys a direct `P2` discharge at the cost of forbidding idle steps; FORM-H keeps idle steps but needs the definitional event move to discharge `P2`. The accumulation sentence uses only defined vocabulary; "realized history" is itself an import, carried as a residue row.

Panel plan: a blind panel hones both surfaces with T1-T4 as acceptance tests; then the owner rules, including the open (a)/(b) call on the permanence surface and the FORM-E/FORM-H choice; then a premise-hash wave follows if wording is accepted. Nothing is adopted here, and the audit lane owns all status changes.

TOE-leverage statement [check 35]: the two owner surfaces replace the `H != 0`/D1 premise and ground event-ordering; nothing here replaces B-AXIS, which stays external because the ordering-to-transfer-axis bridge is OPEN. The conditional ladder's other rungs keep their named statuses (#4797 review-pending, N5 cap, ABJ external, past-hypothesis). So the accumulation sentence is the only genuinely new sentence among the content sorted here, and the leverage is honest about what remains external.

## Consequence

- Readout-invariance alone gives no permanence-across-events theorem (T1).
- Permanence gives a partial inclusion order; inclusion order gives count and event-orientation only (T2), firewall-scoped away from rate/metric/clock, with record-time coarser than step-time.
- Accumulation is new content relative to the four quoted axioms, now against all 20 enumerated axiom-block sentences (T3).
- The two owner surfaces, if accepted, replace the `H != 0`/D1 import and ground event-ordering while preserving every named external, B-AXIS included (T4, T5).

## Does NOT

- Does not change any axiom, and does not adopt either candidate surface or foreclose the (a)/(b) permanence call.
- Does not derive physical time, rate, metric, clock, or generator scale.
- Does not derive the thermodynamic arrow beyond the past-hypothesis residual.
- Does not derive the ABJ input, the B-AXIS transfer construction from ordering alone, or the kernel-convolution theorem.
- Does not edit audit data, policy files, or ledger surfaces, and does not read any file outside the five quoted notes and this note's own residue table.

## Dependencies

- Quoted axiom memo: `docs/MINIMAL_AXIOMS_2026-06-29.md`
- Quoted nontriviality firewall: `docs/DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md`
- Quoted order/rate firewall: `docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`
- Quoted form-class note: `docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`
- Quoted arrow note: `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`
- Supervisor-supplied, not file-read here: PR #4843, #4797, #4854, #4855, and the anomaly/time-cluster context.

## No-Promotion

This note is a draft support artifact for supervisor review. It gives bounded-theorem checks, a narrow no-go, and a governance map. It makes no package-status claim, predicts no audit outcome, and requests no audit outcome. The owner-surface sentences remain flags, and the permanence (a)/(b) call and the FORM-E/FORM-H choice remain open owner decisions. The named open targets remain open: kernel convolution from one-parameter composition + locality + record-compatibility, and the ordering-to-lattice-transfer-axis (B-AXIS) bridge.

## Summary

- Runner: 35 exact checks, `TOTAL: PASS=35 FAIL=0`, no floats.
- Owner surface 1 (permanence, OPEN (a) clarity / (b) new-content): "A record, once present, is permanent: no later configuration removes or alters it. Reading it changes nothing."
- Owner surface 2 (accumulation, both forms): FORM-E "Every step of a realized history registers at least one new record."; FORM-H "Records accumulate: every realized history keeps registering new records; no configuration is final."
- Leverage: the two surfaces replace the `H != 0`/D1 premise and ground event-ordering; B-AXIS stays external because the ordering-to-transfer-axis bridge is OPEN; the accumulation sentence is the only genuinely new sentence among the content sorted here.
- Compression-map named targets: kernel convolution from one-parameter composition + locality + record-compatibility; ordering-to-lattice-transfer-axis (B-AXIS) bridge.
