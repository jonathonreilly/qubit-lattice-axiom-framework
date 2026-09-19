# axioms-and-the-event-lattice: attempt 1 of 3

Worker `w-jonathonsmac4f50-j8065` (claude-opus-5), unit `J-derive-axioms-and-the-event-lattice-a1`. This is a reading task: a map with citations and no physics verdict. `check.py` verifies that every quoted line exists verbatim at the cited path and line of `main` at `abb98a122eb7acefd37b10ae89dd33c500a9c353`, which was `origin/main` when I read it.

## 0. What was read, and how completely

**Read in full, every line** (lengths checked by `R1`):
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines).
- Every note it cites at axiom level:
  - `docs/audit/AXIOM_MINIMALITY_POLICY.md` (818 lines). This is the status authority for the memo, but its own §1 (L34) says policy text carries no premise or interpretive weight.
  - The premise registry `docs/audit/data/axiom_premise_nodes.json` (`canonical_ids` checked by `Q2b`).
  - The three approved-primitive notes: `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (99), `SCALE_REFERENCE_PRIMITIVE_NOTE.md` (57), `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (110).
- The superseded memo `MINIMAL_AXIOMS_2026-06-05.md` and `KEY_TERMINOLOGY.md` are cited only as history and index, so they carry no current axiom content.

**The causal-time lane on `main`.**
- Read in full: `ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md` (153).
- Read for their claim scopes, changelogs and every line matching time, clock, 3+1, `Z^3`, record, history order and formation order:
  - `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md` (714);
  - `ANOMALY_FORCES_TIME_THEOREM.md` (470);
  - `PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md` (122);
  - block 01's formation-law note on `main`.
- These are downstream bounded or conditional rows. They are cited for what they say, not as premises.

## 1. (a) The sentences that constrain the past of a record

| Topic | Sentence (file:line) | What it fixes |
|---|---|---|
| Sites | `MINIMAL_AXIOMS_2026-06-29.md` L37–38: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." | the only site set is `Z³` |
| No privileged site | L40: "No site is privileged. Sites are distinguished by the supplied lattice structure alone." | no supplied origin, axis or order of sites |
| What a new record depends on | L57: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." L60–61: "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." | a forming record's law is a function of its nearest neighbours' conditions only |
| At formation | L67–68 (reading note, interpretive, non-governing): "… concerns which possibility a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate." | the rule is the conditional given formation; formation itself is not supplied |
| Occurrence | L77: "Records form." | records occur |
| One record per site, permanence | L79–80: "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent." | each site is recorded at most once, forever |
| State | L92: "A state is a configuration of records." | the nearest-neighbour conditions at formation are the neighbours' records or their absence |
| Unfixed choices | L89–90: "A choice not fixed by the supplied structure remains a named conditional or open dependency." | an order of formation, if used, is a named conditional |
| No dynamics or time metric in Admissibility | L116: "Admissibility is not a dynamics axiom." L122–123: "… define a time metric, or provide a record-production process or physical persistence dynamics." | no time metric or production process is supplied |
| Outside the axioms | L183–184: "… the remaining formation rules (the distribution's form and values, at which site, and at what rate);" L185: "- arrow, record-production dynamics, physical persistence dynamics, time metric, …" | the formation order, site and rate, and the arrow and time metric, are open gates |
| Time in the primitives | `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` L15: "… the emergent evolution tick is …"; L23: "… the Euclidean regulator block `Z^3 x Z_tau` on which loops are …"; L31–32: "… is not a fourth spatial dimension, not a new dynamics, and not a re-axiomatization of time: the framework's time remains emergent and derived …"; L67 | time is an emergent tick of a loop regulator whose spatial part is `Z³`; it is not a lattice of record sites |
| State selection | `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` L21: "The laws do not pick the state; the world does, among the states the laws permit." | which records exist is realized data |
| Registry | `axiom_premise_nodes.json` `canonical_ids` = `minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive` | nothing else is a supplied premise |

**The time lane on `main`** (downstream, conditional):
- **Single clock.** `AXIOM_FIRST_SINGLE_CLOCK_…` L21: "each lattice time slice `Σ_t = {t} × Z^3` is a codimension-1 Cauchy surface". L30–31: "(S3′) **the axis is a premise, not a derivation**". The unitary qubit dynamics uses slices `{t} × Z³` with a declared axis (B-AXIS). It has no records at every `(t, x)`.
- **Anomaly forces time.** `ANOMALY_FORCES_TIME_THEOREM.md` L13: "**Claim scope:** conditional 3+1 derivation." L23: "… `d_t = 1` and the spacetime signature is (3,1)." L25–26: "No step defines time via the anomaly." Here "3+1" is the signature of that conditional quantum lane.
- **Arrow.** `ARROW_FROM_RECORD_FORMATION_…` L62: record formation "derives the arrow's **direction** = "away from the low-record boundary"".
- **History order.** `PAST_HYPOTHESIS_EXISTENCE_REDUCTION_…` L30: "The history order throughout is **supplied by the record history**". For records, time is the order of the record history.
- **Formation order.** Block 01, `ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_…` L139–141 defines the formation law for an order `σ` with past `A_k = N(x_k) ∩ {x_1, …, x_{k−1}}`, and says: "The axioms supply no order".

## 2. (b) Predecessor structures: consistent or excluded, with the deciding sentence

**S1 (PROVED from the quoted text). Every one-record-per-site formation order on `Z³` is consistent.** This includes the probes' backward 2+1 structure.
- A formation order forms each site of `Z³` once (L79–80).
- Each record's law is a function of its six nearest neighbours' conditions at formation: their records, or their absence (L60–61, L92).
- The past of `x` is the set of its neighbours already recorded, `A = N(x) ∩ {earlier sites}`, which is block 01's formation law.
- The backward 2+1 structure is the level order `x₁ + x₂ + x₃`: each site forms after its three lower neighbours and before its three upper ones.
- The order is not supplied (L67–68 reading note, L183–184), so it is a named conditional (L89–90). It is not excluded:
  - the rule stays one fixed covariant rule (L57);
  - the order is not part of the rule;
  - the text puts no condition on formation orders beyond these.

**S2 (PROVED from the quoted text). A structure that forms a record at every tick of a site is excluded as written.** This covers:
- the backward 3+1 event lattice, whose level planes are three-dimensional (`Z⁴`-type events, four predecessors);
- the symmetric light-cone past, where the record at `(t+1, x)` is formed from `(t, x)` and `(t, x ± e_j)`.

The reasons:
- These structures put records on the events `(t, x)` with `x ∈ Z³` and every `t`.
- The sites are the points of `Z³` (L37). A site "never carries more than one record; records are permanent" (L80). So the second record at `x` violates L80.
- The light-cone past also includes the site's own previous record, which is a second record at the same site.
- The approved primitive's `Z³ × Z_τ` does not supply record sites. It is a loop regulator, time "remains emergent and derived", and it "is not a fourth spatial dimension" (KIN L23, L31–32).
- The single-clock and anomaly notes are conditional rows whose time axis is a declared premise (CLK L30–31; ANO L25–26). They supply no record sites either.

**S3 (PROVED). The text does not decide between one-record-per-site orders.** Level orders, checkerboard orders, clock-driven orders and single-site versus joint formation units are all open: L183–184 "at which site, and at what rate", and L89–90. The physics differences the probes found inside this class (block 01 onward) are downstream.

## 3. (c) The clause the 3+1 or light-cone structures would need, and its cost

**The clause.** Replace L80's "A site never carries more than one record" by per-tick uniqueness, and supply the tick. For example: "Records form at every site at every tick; a site carries at most one record per tick, and records are permanent. A new record's distribution is determined by the records of the previous tick at the site and its nearest neighbours." This is the light-cone form; the backward 3+1 form would name the previous-tick predecessor set instead.

**The cost.**
1. Record's one-record-per-site sentence becomes one record per site per tick. Records then accumulate at a site.
2. A record tick becomes supplied structure. Today time is emergent and derived (KIN L31–32), and Admissibility defines no time metric (L122).
3. The kinetic-isotropy primitive's `Z_τ` would acquire a second role, as the record tick. Whether its `c_t = c_s` then covers record formation is a new question.
4. The "at which site, and at what rate" gate (L183–184) would be decided: every site, at every tick.

**The one-line insight such a clause would carry.** "Every place is written again at every tick, and each new record reads its neighbourhood's records from the tick before." Contrast the text as written: "Every place is written once, and each new record reads the neighbours already written."

**The route for such a change.** A worker who needs it records it as an explicit science-level decision (policy L59–66) and needs the owner's explicit approval (policy L76–80). Policy text is cited here as process only, not as premise (L34). The repository's own axiom-update criterion (the layman-simple insight) is not stated in any file I found on `main` or `ai/execution`. The one-line insight above is offered for it.

## 4. What would finish it

The map is complete for the axiom text and the approved primitives. What remains is an owner decision, if the physics found under S2's structures is wanted: memory in 3+1, and a static response equal to the lattice Green function under the light-cone past. The alternative is a derivation of a record tick from the four axioms, which no row on `main` supplies.
