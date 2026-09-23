# J:derive:axioms-and-the-event-lattice:a2 — worker w-macbookpro90c72-j59ee

**Model:** claude-opus-5-5.

**Check:** `python3 probes/work/derive/axioms-and-the-event-lattice/w-macbookpro90c72-j59ee/check.py`
- Under a second. It needs `git`, and it reads main pinned at `b8d0017208a2`, which is also the current `origin/main`.
- **What it verifies.**
  - Every quotation below appears verbatim at its path and line (69 quotations, 7 files).
  - The axiom-level corpus is the four canonical premise nodes.
  - Every keyword line of those four files is cited here or classified.
  - The tension of S4.

**Reading rule followed.** The axioms memo `docs/MINIMAL_AXIOMS_2026-06-29.md` was read in full (233 lines). So were the approved primitives it depends on through `docs/audit/data/axiom_premise_nodes.json`:
- `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (99 lines);
- `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (110 lines);
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` (57 lines; units only).

The causal-time texts named by the task's phrases were read in their claim sections:
- "3+1" and "anomaly forces time": `docs/ANOMALY_FORCES_TIME_THEOREM.md`;
- "one clock": `docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`;
- the arrow: `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`.

No physics verdict is given.

**Provenance.**
- **Round 1:**
  - a1, `w-jonathonsmac4f50-j8065`, claude-opus-5, mapped the memo;
  - a3, `w-jonathonsmac4f50-jaf7d`, claude-opus-5, found that a1 left out memo L166–168, L199–202 and L228–233.
- No referee (`J:confirm`) logs exist, so nothing is GIVEN.
- My plan was formed before I read them: the whole memo, the premise-node allowlist, and the causal-time notes by phrase.
- **What this attempt adds:**
  - the three approved primitives, read in full;
  - the premises of the single-clock and anomaly notes;
  - an exhaustive keyword scan, which answers round 1's completeness gap;
  - the tension in S4.
- Where this map agrees with a1 and a3, it is an independent confirmation.
- My physics units in the formation lane (#8714; today's unit on blocks 90–91) are not reused.

## 1. The statement attempted

- (a) Every sentence of the axiom-level texts and of the causal-time notes on main that constrains:
  - which records a new record is formed from;
  - whether records are permanent;
  - whether time is a lattice direction or derived;
  - the role of `Z^3`.
- (b) The predecessor structures that are consistent with them and those that are excluded, each with the deciding sentence.
- (c) If the text does not decide, the clause that would have to be added, and its cost.

## 2. The map

**S1. The axiom-level corpus. CHECKED (Q2).**
- `axiom_premise_nodes.json` L5–8 lists exactly `minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive` and `realized_state_primitive`.
- These, and only these, are premises on main. Every other text below is a bounded note, conditional on its declared premises.

**S2. The sentences. CHECKED (Q1: verbatim at the cited lines).** `AX` = memo, `KI` = kinetic isotropy, `RS` = realized state, `SC` = single clock, `AN` = anomaly bridge, `AR` = arrow note.

*(i) Where records live.*
- AX L37–38: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site."
- AX L40: "No site is privileged."

*(ii) Uniqueness and permanence.*
- AX L77: "Records form."
- AX L79–80: "a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent."
- Restated at AX L166–167: "one-record-per-site uniqueness, permanence".

*(iii) What a forming record depends on.*
- AX L57: "one fixed nearest-neighbor admissibility rule, covariant under lattice [translations and proper cubic rotations]".
- AX L60–61: "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
- AX L67–69: the distribution concerns "which possibility a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate."

*(iv) What is not supplied.*
- AX L89–90: "A choice not fixed by the supplied structure remains a named conditional or open dependency."
- AX L92: "A state is a configuration of records."
- AX L116, L122–123: Admissibility "is not a dynamics axiom", and does not "define a time metric, or provide a record-production process or physical persistence dynamics".
- AX L143: rows that need "record-production dynamics" cite a separate authority.
- AX L183–185: the open gates include "the remaining formation rules (the distribution's form and values, at which site, and at what rate)" and "arrow, record-production dynamics, physical persistence dynamics, time metric".
- AX L201–202, L212, L232: formation site, weight and rate, and "dynamics", are downstream.

*(v) The approved primitives.*
- KI L15–16: "the emergent evolution tick is grained on the same footing as the spatial lattice edge".
- KI L23–24: "the Euclidean regulator block `Z^3 x Z_tau` on which loops are computed is hypercubic-symmetric".
- KI L31: "not a fourth spatial dimension, not a new dynamics, and not a re-axiomatization [of time]".
- KI L32–33: "the framework's time remains emergent and derived (the single-clock codimension-1 evolution theorem)".
- KI L40–41: "records' causal order" is listed among things "not used here". It is named, but nowhere supplied.
- KI L67: "It does not re-axiomatize time."
- RS L21: "The laws do not pick the state; the world does, among the states the laws permit."
- RS L30: "The past hypothesis is a separate, stronger input."
- RS L35: the realized state is "supplied by the physical history".
- RS L64: no "special boundary condition on the realized history".

*(vi) The causal-time notes.* Each is a `bounded_theorem`: SC L8, AN L8.
- SC L21–23: "each lattice time slice `Σ_t = {t} × Z^3` is a codimension-1 Cauchy surface: the equal-time local algebra is the mutually commuting tensor product of per-site one-qubit `M_2(C)` Pauli [factors]". These are slices of the amplitude algebra, not levels of records.
- SC L30–31: "the axis is a premise, not a derivation".
- SC L38: "exactly one clock" holds "conditional on (B-AXIS)".
- AN L1, L13: "3+1 Spacetime", "conditional 3+1 derivation".
- AN L20–21, L23: "given … the declared B-AXIS premise (one supplied blocked time step, one declared evolution axis/transfer construction …)", then "d_t = 1 and the spacetime signature is (3,1)".
- AN L25–26: "(d_t <= 1) is local to the declared B-AXIS boundary. No step defines time via the anomaly."
- AR L18–19: the memo lists "the arrow, decoherence mechanisms, and record-production dynamics among the gates **outside** the four axioms".

**S3. Nothing that bears is left out. CHECKED (Q3).**
- 39 lines in the four axiom-level files match the task's keywords: past, time, order, clock, tick, dynamic, formation, permanen, history, `Z^3`, `Z_tau`, 3+1.
- Each is cited above or classified in `check.py` with a reason (history entries, headings, continuations, contrast lines).

**S4. The tension. CHECKED (Q4).**
- The approved primitive calls time "emergent and derived", citing the single-clock theorem (KI L32–33). That theorem makes the axis a declared premise and withdraws its earlier derivation (SC L30–37). Its one clock is conditional on B-AXIS (SC L38).
- The 3+1 bridge obtains `d_t = 1` only with B-AXIS, and "No step defines time via the anomaly" (AN L20–26).
- **So on main a time axis is never axiom content.** It enters only as B-AXIS, a declared premise of bounded notes.
- The primitive's wording predates the theorem's re-scope. The primitive is dated 2026-06-09; the theorem was re-scoped 2026-06-11 and split 2026-06-17 (SC L3–7). Settling that is for the audit lane, not this attempt.

**S5. (b) The predecessor structures. Read from S2; each verdict names the deciding sentence.**

*What the text says a record's past is.* The nearest-neighbour conditions at its site when it forms (AX L60–61, L67–68): the states of its six `Z^3` neighbours, recorded or not. Which site forms next, at what rate, and in what order is not supplied (AX L68, L183–184, L201–202). RS L21 leaves the realized order to history.

*Consistent.* Every order that forms each `Z^3` site at most once, with the forming record's distribution a covariant function of its neighbours' conditions. Examples:
- plane-by-plane sweeps along an axis, i.e. the backward "2+1" past, with time taken from one axis of `Z^3`;
- diagonal sweeps;
- random sequential orders.

Deciding sentences: AX L37 (the sites), L60–61 (what determines the draw), L68 (the order is free), L79–80 (once, and permanent). In every such order the sets that form together lie inside `Z^3`. So one record per `Z^3` site can give time-levels that are at most two-dimensional, or no foliation at all.

*Excluded as written.* Every structure that records a `Z^3` site at each tick:
- the 3+1 event lattice with three-dimensional level planes;
- the level-ordered past;
- the symmetric light-cone past of block 90.

Deciding sentences:
- AX L79–80 and L166–167: a site would carry more than one record;
- AX L37: the sites are the points of `Z^3`.

Neither the primitives nor the causal-time notes supply record levels:
- KI's `Z^3 x Z_tau` is a regulator for loops, "not a fourth spatial dimension" (KI L23–24, L31);
- the single-clock slices are slices of the amplitude algebra (SC L21–23).

*Undecided.*
- Whether an unrecorded neighbour enters a site's "conditions". AX L82–83 makes it unreadable, which is not the same as absent from the conditions.
- Which admissible order is realized.

**S6. (c) What would decide it, and the cost.**
- **To host the probes' three-dimensional level planes** (3+1, the light cone), the least change is: "A site carries at most one record per tick; the records of a tick are formed from the records of the previous tick at the site and its nearest neighbours". It would:
  1. change Record's one-record-per-site sentence in both of its places (AX L79–80 and L166–167);
  2. supply a tick, i.e. a time lattice direction, which the memo leaves out (AX L122, L185), which KI says it does not supply (KI L31, L67), and which the causal-time notes only declare (B-AXIS);
  3. fix, by fiat, the formation site and rate and the past, which the memo keeps downstream (AX L68, L183–184).
  - The layman-simple form: *each site writes one record per tick, and its next record is formed from the records around it at the tick before.*
- **Without amending Record,** the only structures on offer take time from one axis of `Z^3`: the 2+1 reading, AX L37 with L68. The probes found that reading forgets and has no three-dimensional potential (task statement).
- **Either way,** KI L32–33 would need to cite B-AXIS as a premise rather than "derived" (S4).

**ASSUMED:** nothing. This is a reading, and every quotation is checked.

## 3. Where it stops

This is a map, not a physics verdict. The choice between amending Record (a record per tick) and keeping one record per site belongs to the owner. The stale wording of S4 belongs to the audit lane.

## 4. What would finish it

1. A referee of another model family for S2–S5, run against the pinned sha.
2. The owner's decision on the per-tick clause of S6. After that, a re-run of block 90's reversibility with levels that are sites.
3. The audit lane's reading of S4.
