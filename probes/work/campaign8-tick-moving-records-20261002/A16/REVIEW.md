# A16 hostile review of Campaign 8 claims

**What I read.** BRIEF; LOG (including the A12, A14 and A15 entries that were added at 23:21, while I was reviewing); MORNING_DRAFT v3 (22:19); the reports for A1–A11 and A13. I did not review A12, A14 or A15 themselves; I cite their LOG entries only where they bear on a claim below.

**What I ran.** Three tiny checks in `.../scratchpad/c8/A16/`:
- `check_sc_cycle.py`
- `check_two_record_rotation.py`
- `check_two_record_translation.py`

Each ran under 10 s, under 100 MB, with `nice -n 10` and one thread. I also redid the arithmetic: A3's leak (0.28465), A7's gap (√2−1), A9's rank-1 star rate (4.96e-6), 1/7!, and the pacing-fork times.

---

## 1. A3: one-site moves, the net-flow rule, Step 10

**Verdict: STANDS-NARROWED. Two sub-statements fail as worded.**

**(a) Mathematics**
- **"Moves exist for every state iff the tick is strictly range-1."** EXACT. Hall–Gale step: Π_Y U = Π_Y U Π_{N̄(Y)} gives P_{t+1}(Y) ≤ P_t(N̄(Y)). This holds in the supplied toy with a fixed number of excitations.
- **"U = exp(−iHτ) with nearest-neighbour H fails for all but isolated τ" (Step 3). FAILS both ways.**
  - Uniform d=1 hopping fails for every τ > 0, not just away from isolated values.
  - An H made of commuting terms on one fixed pairing never fails.
  - Consequence: the LOG's "I2 plus consistency forces stepwise, strictly local change" and the draft's "Smooth change leaks too far in a tick" are overbroad.
  - What fails is one time-independent, everywhere-the-same star-local generator (Campaign 7 sentence 2).
  - A smooth generator acting on one partner set per tick keeps every intermediate map range-1. A10's G(θ) = exp(−iθ·SWAP) layers are exactly this, and A11 notes SWAP is smoothly generated.
  - So A13's "Q2's 'continuously' means 'without end'", listed as *forced*, is not forced.
- **Uniqueness on a line.** EXACT under its four stated conditions: one record; ring with N≥5 or Z; a local flow law obeying continuity for all states; no counterflow.
- **Step 10.** EXACT for ticks that are all of: homogeneous, strictly range-1, covariant at every tick, and number-conserving in a rotation-invariant basis. The one-excitation symbol is then a Laurent unit, hence a monomial, and covariance kills it.
  - Not covered: non-conserving covariant ticks. Example: bond-direction "compass" gates σ^aσ^a on a-bonds are covariant under spin-½ soldering.
  - Not covered: cycled ticks (A10).

**(b) Semantics.** Under R3 the "record" does not lock anything; A3 itself says "'locks' becomes 'names'". It is a Bell-type position variable (comparator). The range-1 conclusion also follows under the axiom-literal reading R1, because the one-site limit applies from the agreeing state. Headline 1 therefore survives under both readings, and the draft should say so.

**(c) Overbroad wording**
- "Smooth change leaks too far in a tick."
- "Lone records can't move": this drops per-tick covariance, homogeneity and number conservation, and A10 evades it.

**(d) Narrowed wording.** "If moving records' places match the uncut odds, each tick's net change reaches at most one site. A fixed, everywhere-the-same nearest-neighbour change leaks past that. A smooth change on one partner set per tick does not."

---

## 2. A7: readable places plus uncut links force signalling, so option A

**Verdict: STANDS-NARROWED.**

**(a) Mathematics.** I rechecked the core argument: P(b1≠a1) = sin²θ, P(b2≠α) = sin²(θ−φ), α = a1 forced by the one-site limit, then the triangle inequality, giving a gap ≥ sin φ + cos φ − 1. Correct.
- But "under every rule" quantifies over rules **for one hand-built instance**. That instance uses supplied, non-covariant ticks and a supplied "choice".
- The LOG's "force signalling under EVERY rule" should read "there are linked states for which every rule signals". A7's own "Narrow claim" is right.

**(b) Semantics**
- **Option A is the axiom-literal reading.** A record sitting at a site has, per the Record axiom, "locked" that site's possibility, which is the cut. Option A is therefore not a new cost; R3 is the departure. Present it that way.
- **Option B has an unstated rule, and without it, it fails.** Under Q7 ("menus set by recorded neighbours"), a neighbour z can form a record whose menu depends on a guided record's place. That registers b1 without cutting B's possibilities, and Step 6 then signals.
  - A7's "any register … cuts B under Q1" holds only under a broad reading of "agree with it".
  - Option B therefore needs explicit text: any formation whose odds or menu depend on a guided record's place also cuts that record's possibilities to agree.
  - Corollary for claim 4: menus set by records are safe only for records that agree with their sites.

**(c) Overbroad wording.** "Must re-form" is ARGUED beyond the toy:
- partial cuts were tested only in a uniform family;
- the covariant regime (cycled pairings) was not tested.

---

## 3. A1/A2: W3 = 0 for strictly local steps; covariance kills flow

**Verdict: STANDS-NARROWED.**

**The K-theory is applied correctly.**
- **A2 D6.** By Bass–Heller–Swan for regular rings, K₁(C[z^±]) = C*⊕Z³ = units, so SK₁ = 0. Stabilise, contract the elementary factors, and use the homotopy invariance and additivity of W3. Correct.
- **A1 D20.** Suslin's SL_N = E_N needs N ≥ 3. The 2×2 spin-½ walks must first be stabilised to W⊕1. A1's comparator box mentions this; the D20 body omits it. One-line fix.
- **A1 D18.** I re-derived it: the axis slope must be an integer and √3 times the slope must also be an integer, so v = 0. Correct.

**Scope is missing in the draft and in A13.**
- The result is for translation-invariant (any period), finite-dimension, **single-particle** steps.
- Interacting steps and Haah-type QCAs are open (A1 open edge 3, A2 open edge 1).
- The LOG's narrowing of the Campaign 7 flag must say "single-particle".

**Overbroad wording**
- **"Two independent proofs."** Both rest on the same algebraic K-theory of Laurent rings, in stable and unstable form. Only A2 D5 (shift-and-mix circuits) is self-contained.
- **"Faint longer reach can tip the balance."** This holds only for a mover with ≥2 internal states: more than one qubit per site, or a multi-site cell, which breaks unit translations.
  - With literally one qubit per site, number-conserving: a scalar walk, so nothing moves under covariance (A2 D9a).
  - With pairing: W3 = 0 even quasi-locally (A2 D9b).
  - A10's cycles: ν₃ = 0.
- **"Covariance kills net flow."** STANDS, EXACT per tick. For cycles, the index is 1 (A10).

---

## 4. A9: linear chance, menus, the sea

**(a) "The chance must be tr(Fρ)": STANDS-NARROWED.**
- The affine-to-Riesz step is correct.
- H2 is the steering hypothesis: a distant record can leave the neighbourhood in any chosen mix of states. It needs:
  - joint possibilities as states on the tensor product (Campaign 7 sentence 1);
  - Born odds and Lüders post-states at b (sentence 3);
  - every decomposition of every star state realisable as a snapshot.
- H3 is no-signalling (sentence 4). None of these sentences is adopted.
- Q1 supplies linking and "change at once to agree", but not steering of every possible mix.
- **Is H2 available?** Only inside the supplied quantum model. It is consistent with Q1 and Q7 (a distant record pattern serves as the "setting"), but it is not derivable from the axioms plus approved readings. "Must" should read "if no-signalling, in the supplied sharing model". The LOG's "steering (via Q1 sharing)" needs this qualifier.

**(b) "Menus set by unrecorded possibilities signal": STANDS-NARROWED.**
- What is shown: a lock frame taken as a *nonlinear* function of unrecorded possibilities signals.
  - Own Bloch axis: TV 1.0 (coordinator check).
  - Neighbour's Bloch axis: 0.47 (`sig_toy.py`, "N-menu").
- A9 itself allows "one joint linear instrument on the star".

**(c) "The half-filled sea is not quiet": STANDS.**
- EXACT for the massless sea, with a full-rank marginal on every finite region.
- Scope: single-tick, memoryless, linear weights.
- A12 finds multi-tick windows with per-site memory can reach exponentially small rates, never zero, and that A9's R⁻³ is not the optimum.

**Coordinator's Q7 "correction": FAILS as worded.**
1. Q7 never proposed an own-state menu. The TV = 1 check refutes the timing-probe rule, not Q7.
2. Q7 defines the menu as "the possibilities with nonzero odds". Under any linear instrument the odds, and hence their support, vary with unrecorded neighbours. This is required by Admissibility ("varies with the nearest-neighbor conditions") together with Q1. Even A13's own F = c·P_singlet makes the support depend on unrecorded possibilities.
3. The LOG's consequence (1) keeps "or by one joint linear instrument"; the draft drops it.
4. Record-set frames are safe only for records cut to agree with their site (see claim 2).

---

## 5. A4/A6/A8: bounded formation time, net sink, β = 1/2

**(a) Bounded formation time: STANDS-NARROWED.**
- E[formations per site] ≤ 1−ρ₀ requires a **translation-invariant start**, or no moves.
- In a non-uniform state, formations in R ≤ |R| + (boundary bonds)·t. A region can keep forming by exporting records (A6 3.2).
- The move-event "clock" is stored in no record. Readable accumulated time in a fixed region is ≤ |R| in every reading (A13 T4).
- A steady move rate needs a positive-density gas of wandering records filling space; finite record sets dilute on Z³ (A13 T3).

**(b) 1/r needs a net sink and a quiet void: STANDS-NARROWED** to the content-blind wanderer toy (closed linear mean equation, Liouville).
- "Detailed-balance odds give a flat far field" is shown only for hops that ignore the neighbourhood (A6 3.5). An equilibrium state with a massless mode can carry a harmonic static profile (ARGUED).
- The quiet void can be evaded by fine-tuning void formation against breeding (m² = 0), but void formation freezes regions anyway.

**(c) β locked at 1/2: STANDS-NARROWED.**
- EXACT in the dilute mean field: single carrier, arrival-gated linear clock, flat lattice transport.
- β_eff is read off g₀₀ = −N² with U ≡ 1−N in lattice coordinates. The toy has no test-body dynamics.
- A14 names a ratio clock that would give β = 1, though nothing supplies it.

**Missing from the draft**
- γ = 0 (half the light bending and radar delay), a first-order mismatch. A14's AND gating restores γ = 1 but needs a global coincidence tick.
- The establishment limit: about 5×10⁻⁵ m in the age of the universe at Planck steps (A8).

---

## 6. A5: ticks unreadable except ties and seams; low-speed relativity

**(a) Ticks: STANDS-NARROWED.**
- It needs condition (a), condition (b), and neighbourhood ticks that keep in step ("rebuild the same network").
- Out-of-step ticks are strongly readable: A15 Theorem A shows phase-mismatched bonds never act, so seams are perfect mirrors.
- The tie fraction p/(2−p) assumes a constant, state-independent p and independent waits. Under A9's state-dependent chance, one linked site's formation changes its partner's chance, so the formula does not apply.

**(b) Relativity: STANDS-NARROWED to the 1D Dirac toy (EXACT).** In 3D under the axioms' covariance it is not established:
- strictly local, exactly covariant spin-½ walks have **zero** long-wavelength speed (A1 D18);
- the strictly covariant six-ordering step splits linearly, ω = |k| ± |k|²n_xn_yn_z, which gamma-ray burst timing disfavours for light;
- A10's isotropic cone needs the Kogut–Susskind signs. Z·G·Z is not covariant under spin-½ soldering (S13d), so this privileges a basis. Covariance holds only up to re-phasing; C3-symmetric words split linearly, and palindromes keep only 8 of the 24 rotations.

---

## 7. A10/A11: cycled pairings, flow around records

**(a) Motion with one qubit per site: EXACT. "Schedule-covariant": FAILS.** A11 D10 (EXACT) applies to A10's own round. My checks:

**One record (`check_sc_cycle.py`, 6³ torus, θ = 0.6)**

| Symmetry | Realised as |
|---|---|
| Cube-centred O | Exact symmetry |
| T_x | Forward restart 1 |
| T_y | Forward restart 3 |
| Site-centred C4z | Forward restart 1 |
| T_(1,1,0), T_(1,1,1), the 180° face turn about a site | No forward restart (residual 0.15); match only the **reversed** round |

- The relabellings do not even compose as a group: two forward shifts produce a reversal.
- The sub-step film is never a shifted film, except under cube-centred C2.
- (L = 4 is degenerate, so I used L = 6.)

**Two option-A records (`check_two_record_*.py`)**
- Exact enumeration, A13's relocation rule, 30 nearby starts.
- The quarter turn matches no forward restart under any of the 8 parity shifts: worst best-TV 0.028. It matches the reversed round shifted by (1,1,1) exactly, which confirms A10 S7.
- Every odd translation matches no forward or reversed restart. Worst best-TV runs from 0.038 (T_x) to 0.39 (T_(1,1,1)).
- **Conclusion.** Once records interact, readable statistics tell sites apart by which of 8 sublattices they sit on. This conflicts with "No site is privileged. Sites are distinguished by the supplied lattice structure alone."

**(b) 2D one-way flow: STANDS** (supplied 2D toy, schedule-covariant reading).

**(c) None in 3D: STANDS-NARROWED.**
- EXACT under the schedule-covariant reading, including A10's round.
- Under the flux-level reading: no flow on periodic facets or axis hinges.
- Low-symmetry hinges are OPEN.

---

## 8. A13: the assembled model and the pacing fork

**Verdict: STANDS-NARROWED.**

**What holds.** Consistency (C), locality (L), no-signalling (NS), the quiet vacuum, one record per site and count preservation are EXACT by construction, CHECKED in 1D (N = 8, 4 ticks).

**What is not met**
- **Covariance.** It fails as shown in claim 7.
- **"No possibility is privileged."** The formation and relocation instruments use a fixed axis ("the axis z stands in for a recorded frame"; open edge E2 is open). In the void there are no records, so the axis must come from the law (privileged) or from the unrecorded emptiness direction n (a state-set frame, the class A9 shows signals). A covariant lock would cut the partner to a random −n, away from the emptiness, which breeds (ARGUED). The no-breeding property depends on the fixed axis.
- **Record content.** Every record locks the same content (the anti-emptiness state), so readouts carry no content information. M7's "½ and ½ … where Q4's equal odds appear" is about *which site* forms, not about content odds.

**Overclaims**
- **"The round fixes only aligned states (EXACT)."** The proof covers states fixed gate by gate. Any eigenvector of the round, such as one-magnon Bloch states, is fixed up to phase. The aligned family follows from quietness (A9 n3), not from the round.
- **"Confirmations (forced)."** Q2 "without end" and "menus set by records" are not forced (claims 1 and 4). All six rest on Campaign 7 sentences 1, 3 and 4.

**Pacing fork**
- The algebra is right. I get 30.8 s, **9.1 μs** (the LOG says 9.3), 0.93 ns and 15 fs.
- The M² scaling assumes the whole object's rest-mass phase advances by one shared random step count per arm, independent between arms, with τ_e = t_P.
- If constituents are paced independently, the rate goes as Σm_i² and t_coh is longer by up to the number of independently paced parts. With rarer wanderer events (u∞ ≲ 1e-6) it gets worse.
- It is not binary: A15's angle lapse (change per beat set by records) avoids random pacing; A17 is examining it.
- State up front that event pacing means **no change at all where no records are**, so light cannot cross truly empty regions.

---

## 9. MORNING_DRAFT v3 as a whole

**Stale.**
- Says A10, A11 and A12 are "testing"; all three have landed.
- Has no A13, A14 or A15 content.

**Contradicted by later results or by the coordinator's own runs**
- "Smooth change leaks" (claim 1).
- "Lone records can't move" (A10 moves them).
- "Big ones lose records faster": the coordinator's 3D runs show side 4 losing 32 records in 120 ticks (0.27 per tick) and side 8 losing 256 in 1087 (0.24 per tick).

**Missing caveats**
- The unadopted Campaign 7 sentences 1, 3 and 4.
- γ = 0.
- The establishment time.
- 3D relativity.
- Single-particle scope for chirality.
- The sublattice and reversal costs.
- The unreadable move clock.

**Language rule.** No violations found. Change "calls … into question" to avoid any echo of a "question is asked".

**Jargon.** "TV = 1", "cut", "staggered fermions".

---

## Exact wording fixes for MORNING_DRAFT.md

1. **Intro, after "graded in each lane report…"**, add: "Most results also assume Campaign 7's bookkeeping for shared possibilities (joint possibilities on the product of sites, odds from the site's part, the cut when a record forms) and no faraway influence. You have not adopted those; read each 'must' below as 'if those hold'."

2. **Headline 1**
   - Title "Your two instincts are tied together" → "One site per tick limits the change too".
   - Replace "Then the change between records must also come in strict, local steps. Smooth change leaks too far in a tick. (A3, exact)" with: "Then over each tick the change may carry possibilities no further than one site. A change that is the same everywhere, switched on smoothly for a whole tick, leaks past that (about 28% in the toy). A smooth change that works on one set of partner pairs at a time, switching partners each tick, does not leak. So what is ruled out is Campaign 7's sentence 2 as written, not smoothness; your Q2 'evolves continuously' can stay. (A3, exact in a one-record toy)"

3. **Headline 2**
   - "resets the shared possibilities" → "after which the shared possibilities change at once to agree with it".
   - "Otherwise a faraway choice leaks into the record's path, which is faster-than-light signalling. In a two-tick example, no rule at all avoids this." → "Otherwise, for some linked states, a faraway choice shows up in the record's path faster than one site per tick; in a hand-built two-tick example no rule avoids this. This matches the Record axiom's 'locks'."
   - Line 15: append "If a record's place could set a neighbour's menu without that cut, the leak returns."

4. **Headline 3.** Title → "Steps give an exact speed limit; slow-speed relativity appears in a one-dimensional toy (A5)". Replace the bullets with:
   - "In that toy, moving clocks slow by the Einstein amount, each kind of matter with its own top speed."
   - "In 3D it is not secured. A strictly local rule that treats all 24 turns alike gives a spinning particle no long-wavelength speed (A1). Rules with equal speeds in all directions either split speed in step with energy, which burst timing rules out for light, or need a sign pattern that singles out one direction and keeps half the turns (A5, A10)."
   - "If neighbourhood ticks keep in step, records can't tell them from one universal tick. Where they fall out of step, records show it: exact ties thin out across the boundary, and the boundary reflects what reaches it (A5, A15)."

5. **Headline 4**
   - "Moving records give each place a steady clock." → "If a thin gas of wandering records fills space, each place sees a steady rate of moves. No record stores that count; a readable clock needs something that keeps capturing records."
   - After "falling off as 1/distance." add: "Swallowing needs a 'stopped' mark that record content alone can't show (A8)."
   - Mismatches: change "the next-order correction comes out at half" → "the next-order term of the slowing is half of Einstein's (Mercury)".
   - Add: "light bends and radar echoes are delayed by half the measured amount unless moves need events at both ends on one global beat (A5, A8, A14)".
   - Add: "the profile spreads by diffusion and reaches only about 50 micrometres in the age of the universe at Planck steps".
   - Add: "if the change itself waits for record events, all clocks slow alike, but nothing changes where no records are, and random pacing would wash out atom interference in about a nanosecond if a whole atom keeps one pace (A13; A15's change-per-beat variant avoids this, under check)".

6. **Headline 5**
   - Title → "If regions are not to freeze, empty space must not make records on its own".
   - "every region freezes" → "every region freezes within about one over that rate in ticks".
   - "any local rule makes records in it at a small steady rate" → "any single-tick rule whose chance is a straight average makes records in it at least 5 in a million per tick (best case; 1 in 80 for an energy-based rule); at Planck ticks that freezes everything at once. Many-tick rules with per-site memory can push this down exponentially but never to zero, and the memory is not in the axioms (A12)."

7. **Headline 6**
   - "Strict one-site steps also can't tip … (A1, A2: exact, by two independent proofs)" → "For a single free particle in an otherwise uniform grid, steps of strictly limited reach always pair each left-handed mover with a right-handed one: the doubling problem in its free-particle form (A1, A2; exact, resting on one standard algebra theorem reached two ways). Interactions and record edges are untested."
   - Replace the A11 line with: "On a flat 2D toy, a round of trades carries possibilities one way around every recorded region. On the 3D grid with all 24 turns, such rules carry no trades at all, and looser versions cancel flow on flat faces and straight edges; slanted edges are open (A11)."

8. **Menu section.** Retitle to "One clarification of your menu decision" and replace the bullets with:
   - "Your Q7 stands if unrecorded neighbours enter only as a straight average: they may shape the odds, and so which choices have nonzero odds."
   - "Which possibilities a record can lock must be set by the law and the records around it; records re-formed at each step are safe for this (A9 + my check: no signalling)."
   - "What fails is taking those directions from the current state of unrecorded possibilities, e.g. 'lock along wherever the site now points'; a faraway choice then shows up locally every time (my check). Yesterday's 'own-state' probe columns are of this kind and are illustrative only."
   - Proposed text: "The menu is set by the conditions. Recorded neighbours may set which possibilities are on offer; unrecorded possibilities shape the odds over them only as a fixed weighted average."

9. **Ideas 1.** "Linked neighbours tie a fraction p/(2−p)…" → prefix "If each site has the same fixed chance p per tick," and add "With a chance that depends on the possibilities (A9), this has not been computed."

10. **Ideas 2**
    - "It gives a steady clock" → "It gives a steady rate of events (stored in no record)".
    - "each place fills only about once" → "across a uniform grid each place fills only about once on average".
    - Replace "Lone records can't move…" through "…staggered fermions." with: "With one qubit per site, a step that is the same every tick, keeps the record count, reaches one site and treats all turns alike never moves a lone record (A3). Cycling partner pairs does move it (A10). But once two records meet, the rule tells sites apart by which of 8 interleaved sub-grids they sit on, and a quarter turn matches the rule only with the round run backwards (A10; my check). That conflicts with 'No site is privileged' unless the round counts as supplied lattice structure."

11. **Ideas 3**
    - "every cut" → "every dividing plane".
    - Chirality line → "for a single free particle, strict-reach steps keep left and right balanced; faint longer reach can tip it only for movers with a two-state label (more than one qubit per site) (A1/A2)".

12. **Ideas 4**
    - Crowding line → "Crowding clumps always leak. In the 3D toy a clump 8 times bigger lasted about 9 times longer, losing records at about the same rate; nothing like a black hole's lifetime growing as mass cubed (A4 + my runs)."
    - "their pull grows with their radius" → "their effect on nearby clocks grows with their radius, not their record count".
    - Add "Moving possibilities are turned back at a full region rather than swallowed (A13)."

13. **Ideas 5**
    - "If it doesn't: … events thin out forever" → "If it doesn't: the empty grid stays empty and activity spreads from existing records; crowded regions then freeze if a lone empty spot among records can form, and thin out forever if not (A4)."
    - Linear-chance line → "If no faraway choice may show up locally, the chance of forming must be a straight average of a local weighting (A9, exact in the supplied model); if that weighting is zero on empty space, records form only where something is going on."

14. **Decisions**
    - (1) → "May the change run smoothly within a tick on one set of partner pairs, switching between ticks? Consistent moving records rule out a change that is the same everywhere at every instant (A3)."
    - (2) Add "(for movers with more than one qubit's worth of label; places then match the odds only approximately)".
    - (3) → "Are moving things records re-formed at every step (classical wanderers), or unrecorded possibilities that leave a fresh record only when one forms (interference survives)? A record with an uncut place leaks faraway choices (A7)."
    - (4) "The results say no, which then calls … into question" → "Keeping regions from freezing says no, which puts the half-filled-sea vacuum in doubt unless a many-tick rule with per-site memory is allowed (A9, A12)."
    - (5) Add "(the second is unbounded but stored in no record)".
    - (7) Replace with the menu text in fix 8.
    - Add (8): "Do you accept a rule that, once records meet, tells sites apart by sub-grid and matches a quarter turn only with the round reversed (A10, A11, A13)?"

15. **Before sending.** Verify that the ai/probes path in the intro exists.

---

## Top 3 risks

1. **The menu "correction" would narrow an approved reading that no result requires.** As worded it contradicts Admissibility + Q1 and A13's own model. It also misses the real hazard: guided, uncut records setting menus, which re-opens A7's signalling.

2. **The cycled-pairing route is presented as covariant when it is not.** This covers the "schedule-covariant" label, A13's "assembled model is consistent" and its "forced confirmations". A11 D10 and my checks show:
   - no forward restart realises translations by (1,1,0) or (1,1,1), or the face turn about a site, even for one record;
   - with two records, sublattices become readable (TV 0.04–0.39) and quarter turns need the reversed round;
   - the model's lock axis privileges a possibility.

   It satisfies C, L, NS and the quiet vacuum, not Lattice, Qubit or Admissibility covariance.

3. **Unflagged conditionality and overbroad "must"s.** Linear chance, post-update lock odds, the no-record reshaping, re-formation and "menus by records" all rest on the unadopted Campaign 7 sentences 1, 3 and 4. The "steps, not smooth" overreach drives an unnecessary re-reading of Q2. Add to that 3D relativity, the single-particle scope of chirality, γ = 0, the unreadable move clock and the jam-evaporation sign. Together these could lead the owner to decide on readings from overstated premises.