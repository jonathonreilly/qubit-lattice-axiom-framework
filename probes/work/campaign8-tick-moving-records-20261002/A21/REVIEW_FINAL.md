I've finished both the original scope and the added A20 and lock-and-move scope. One finding drives most of the new fixes. A20's Theorem N is correct, but the v5 draft frames it as being about records. In fact it stops all motion, including light and matter waves, and the lock-and-move rule rescues only records.

# A21 hostile review, final (late lanes, A20, the lock-and-move synthesis, MORNING_DRAFT v5)

**Provenance**
- `A21/REVIEW.md` (00:44) and the LOG's "A21 corrections C11–C20" were not written by me in this session. They match my pre-A20 findings almost exactly, including my r1/r2 numbers, so they look like an earlier save of this review.
- C13's "verified on origin/main" is the coordinator's check, not mine.
- This message supersedes that file and adds A20 and the lock-and-move rule. I wrote no files apart from three check scripts in `.../c8/A21/`:
  - `r1_capacity_and_scales.py`
  - `r2_fixed_coupling_ns.py`
  - `r3_lock_and_move.py`
- Each ran in under 2 s and under 80 MB, at `nice -n 10` with one thread.

## Claims 1–8: verdicts, and their status in v5

v5 has absorbed most of the earlier fixes. Remaining problems are in bold.

1. **A12**
   - Lattice Reeh–Schlieder: **STANDS** (EXACT). It covers rules that ignore records and act on a finite region; a finite time window needs a change with a strict speed limit. It assumes a fermion-style product across sites, which the axioms don't fix.
   - The e^{−2κT} ceiling: **STANDS-NARROWED**. It holds for a fixed seed, per unit of window length plus seed width.
   - The memory import: **STANDS-NARROWED**. A memory at every empty site is an import; a memory carried by matter is not excluded.
   - "Coherent light favours formation gated by records": **STANDS-NARROWED** (ARGUED). It is one of two ways out; a rule blind to light is the other.
   - v5 handles all of this.
2. **A14**
   - "Records as walls fail": **STANDS-NARROWED**. The pinning lemma is EXACT; the result is for a capturing clump in the dilute mean field.
   - AND gating gives γ = 1: **STANDS-NARROWED**. It holds only in the averaged small-dose limit. Real events bring A17's jitter, and light stops wherever there are no wanderers.
   - β = ½: **STANDS** (EXACT, mean field).
   - **v5 still omits the photon-mass cross-constraint (u∞ ≲ 1e-47 if wanderers pin light).**
3. **A15**
   - Theorems A, B and C: **STAND** (EXACT). A needs rigid clocks, the handshake rule, and one slot per pair per round. B: |c(x) − c(y)| ≤ 2p, re-derived. C freezes the whole connected component.
   - The angle lapse transmits: **STANDS-NARROWED**. CHECKED in 1D only; the band top reflects; it needs a smooth, wide average.
   - "Change per tick, not tick rate": **STANDS-NARROWED**. EXACT within fixed-schedule toys, ARGUED beyond.
4. **A17**
   - The capacity floor: **STANDS** (EXACT for linear drives). I re-computed Cap(star) = 11.6192, giving a floor of 2.066 ticks.
   - Time windows don't help: **STANDS** for long-time dephasing.
   - Matter scrambling: **STANDS-NARROWED**. The physical rate is ARGUED.
   - "Field of the possibilities": **STANDS-NARROWED** to "not excluded". It must enter through a fixed coupling; r2 shows a fixed coupling gives TV 2.7e-16, against 6.9e-2 for A15's dial.
   - **It now also needs the Theorem N caveat (claim 9).**
5. **A18**
   - The exponential metric: **STANDS-NARROWED**. It holds at the level of rays, for two-site light, with supplied items.
   - The dialled choices: **STANDS** (EXACT).
   - β = 1 − 1/(2m): **STANDS** for the exponential response.
   - D23 wakes: **STANDS** (EXACT mean field). It is in scope and survives carrier persistence, because inverse-square tests cap persistence at about 50 μm.
   - **v5 dropped the cost that the averaging region becomes galaxy-sized under the photon-mass bound.**
6. **A19**
   - Sharp records give no inertia: **STANDS** (EXACT in the toy).
   - Coarse records give the first law, and mediated records give coarse cuts: **STANDS-NARROWED**.
   - Time-umklapp: **a potential falsifier only**.
   - **New: all of A19's motion runs on A13's round of partner pairs, which is not exactly symmetric on every tick (A16, A20).**
7. **Gravity synthesis.** The v5 version **STANDS-NARROWED** as "the candidate left open". **But a ripple of the possibilities needs a reversible change that moves things, which Theorem N forbids at one-site reach with exact symmetry on every tick (claim 9).**
8. **The draft as a whole.**
   - No language-rule violations. v5's line 115 is a good unifying sentence.
   - Remaining issues are listed in the fixes below:
     - the bottom line omits Theorem N;
     - "independent" reviews overstates provenance;
     - point 1 and decision 1 hide that one set of pairs per tick is a supplied pattern;
     - point 3 and decisions 2 and 8 are misframed.

## 9. A20 Theorem N: **STANDS (EXACT)**

The statement: every reversible tick on one qubit per site that has nearest-neighbour reach and commutes with the soldered rotations about every site is the identity. I checked each step:

| Step | Check |
|---|---|
| N1 support lemma | Sound. Expand both algebras in product bases of the disjoint P and Q; e_j ⊗ f_k are independent, so every O-coefficient commutator vanishes (Schumacher–Werner). It needs O, P and Q pairwise disjoint. |
| N2 | Sound. N̄(x) ∩ N̄(x + 2e_a) = {m}. The algebras invariant under the quarter turn are C1, span{1,σ^a} and M₂. The half turn about m swaps x and y, and N1 rules out M₂. |
| N3 | Sound, and it has a 3-line proof. If any element of T_x carries σ^a on m₁ alone, T_z must avoid σ^b on m₁ and σ^b ⊗ σ^a on (m₁, m₂), so its support on m₁ is trivial; the same holds for σ^b on m₂. Only the parity pair survives. |
| N3 brute force (`t6_nn_lemma.py`) | Correct. It enumerates all 15 partitions, i.e. every unital subalgebra, and requires non-trivial support on both sites; one pair survives. The "all six neighbours trivial or all non-trivial" step is implicit but valid, because rotations about x act transitively on the neighbours. |
| N4 | Sound. The octahedron is connected, so α(A_x) ⊆ A_x ⊗ span{1, S_x}. |
| N5 | Sound. A unital map M₂ → M₂ ⊕ M₂ is inner in each block (Skolem–Noether). |
| N6 | Sound. S_x is fixed with sign +1, and O acts irreducibly on Bloch vectors, so Ad u± = id by Schur. |

**Scope**
- "Nearest neighbour" means a site's content lands only on the site and its 6 face neighbours. Diagonal (unit-cube) reach is open for non-Clifford ticks.
- The soldering of possibilities to the grid's turns (Q3) is load-bearing.
- It requires one qubit per site, an ordinary (ungraded) product across sites, and exact covariance on every tick.
- The proof never uses unit translations; rotations about sites generate only even translations. So the theorem is slightly stronger than stated.

**One overreach in A20's summary.** It says "nothing moves… not records". Records can still move by irreversible steps, which is A20's own relaxation 6. The correct reading is "nothing moves under any reversible change".

**Draft problem.** v5 frames Theorem N as being about records. It stops all motion: light, matter waves and the "field" candidates.

There is also a fork the draft misses:
- If records follow the possibilities, A3 holds the change to one site per tick, and then nothing moves at all.
- If records step by their own rule (D23), A3's premise fails, so the change may reach further per tick (ARGUED). The one-site limit then binds records only.

## 10. The lock-and-move rule (A1 D23, coordinator synthesis)

**Verdicts**
- Complete and 24-turn covariant for one record: **STANDS** (EXACT). The coordinator's script is correct.
- "The clean covariant one-site move": **STANDS-NARROWED** for one isolated record. **FAILS** as written as a rule for several records.

**(b1) A six-possibility, non-orthogonal menu vs "locks exactly one admissible possibility"**
- Compatible as stated, if read the right way. It is a Lüders instrument of the six-outcome Pauli measurement (P_v/3 sums to 1), applied to the record's **own** qubit, followed by a swap with the target site. That gives one outcome and one locked possibility, and the support (5 directions, never backwards) is the menu.
- **Q3 conflict.** The lockable possibilities are the grid's six directions, so this glues formation to the grid. Your Q3 says formation odds are not glued. This is a decision, not merely "not fixed by the axioms".
- **Content is renewed at most steps** (2/3 of the time), which stretches "locks" and "permanent".
- **"Re-forms next door" is ambiguous.** If it means locking the target site's own possibility, the odds don't come from that site's own part (against Campaign 7 sentence 3 and Q3), and the target's shared possibilities are erased rather than cut.
- **As written, the odds ignore the neighbours**, against Admissibility's "varies with the nearest-neighbor conditions".

**(b2) Record count and one record per site**
- The count is conserved for one record.
- Applied independently to several records, two records enter one site with probability 1/9 per tick when both point at it along an axis. The worst face-diagonal pair is 5/36 ≈ 0.139 (CHECKED, r3). This breaks "never more than one record" and I2.
- It has no stay outcome, so every record moves every tick, and a jammed region is undefined.
- A fix: a blocked record stays put, still locking the direction it tried. That keeps it complete, covariant and inside the six-direction menu (r3).
- The clash rule for two records choosing one empty site (I3) is constructible but not built or checked.

**(b3) Handedness ("handed per A1 D22")**
- This is convention-dependent. The rule is handed if a mirror leaves possibilities unflipped (axial), and achiral if a mirror flips them (polar).
- The axioms contain no mirror operations, so it is not framework content.
- Trails (the sequence of places) are statistically identical to the mirror rule's (CHECKED). Handedness shows only in whether the content equals the last step or its reverse.
- It is classical dust and has no bearing on the chirality problem. "Fully symmetric" in decision 8 should read "symmetric under the 24 turns".

**(b4) A9 linear-instrument requirements**
- Consistent in the swap reading: linear odds tr(E_v ρ) with ΣE_v = 1, Lüders post-states, local, no-signalling. It forms every tick, which A9 allows.
- Because a record's content is pure, the odds are fixed numbers. It is a classical persistent walk: 1/3 straight on, 1/6 for each of the four turns, never back.
- Step-to-step correlation is 1/3, and mean-square displacement grows at 2 per tick: dust (r3).
- A7 option A is satisfied trivially, since nothing unrecorded guides the step.
- **It moves records only.**

## Exact wording fixes for MORNING_DRAFT v5

1. Old: "It also forces the change between records to come in strict one-site steps."
   New: "If records follow the shared possibilities, it also holds the change to one site per tick. A reversible change of that kind that treats every site and turn exactly alike on every tick does nothing at all: no record, no light, no matter wave moves (A20, exact). Something has to give; see point 3."
2. Old: "How often ticks come cannot vary."
   New: "In these toys, how often ticks come cannot vary."
3. Old: "matches Einstein's main numbers for light and planets. But gravity carried by records cannot make waves or hold a moving Moon. The candidate left open is a field carried by the shared possibilities."
   New: "matches Einstein's main numbers for planets and for one kind of light, at the level of rays. But gravity carried by wandering records cannot make waves or hold a moving Moon (argued). The candidate left open is a field carried by the shared possibilities, which needs a change that lets ripples move (point 3)."
4. Old: "Two independent hostile reviews attacked the main claims, and their corrections are included."
   New: "Two hostile reviews by separate agents attacked the main claims (the second had read the first), and their corrections are included."
5. Line 28: after "can stay." append: "But one set of pairs per tick is a supplied pattern. It cannot treat every site and turn alike on every tick (A20), and once records meet it tells sub-grids apart (point 3)."
6. Line 34: after "a thrown ball qualifies easily." append: "(This toy moves things with a fixed round of partner pairs; see point 3.)"
7. Old: "### 3. How can a record move at all? (A3, A10, A20, plus my check)"
   New: "### 3. How can anything move at all? (A3, A10, A20, plus my check)"
8. Old: "Any reversible step that reaches only nearest neighbours, and treats every site and every turn of the grid exactly alike on every tick, changes nothing at all."
   New: "Take any reversible step on one qubit per site in which a site's possibilities can reach only its six neighbours in one tick. Suppose it treats every site and every turn of the grid exactly alike on every tick, with possibilities turning along with the grid (your Q3). Then it changes nothing at all. That stops everything, not just records: light and matter waves could not move either."
9. Old: "What travels is a spreading web of links, not a record."
   New: "What travels is a spreading web of links, not a record, and no calm empty background survives (exact for the simplest class of such rules). Rules reaching 2 or 3 sites are untested."
10. Old: the block from "- **The clean option is an irreversible step,** which point 2 requires anyway." through "The cost: a menu of six direction possibilities, which the axioms do not fix."
    New:
    "- **For a single record, an irreversible step works** (point 2 requires re-forming anyway; A1, my check).
      - The record re-locks its own possibility onto one of the grid's six directions, then trades places with the neighbour that way. Its new content points the way it stepped, and that neighbour's unrecorded possibilities move into the vacated site.
      - It is exactly symmetric under all 24 turns. It goes straight 1/3 of the time, turns 2/3 of the time, and never steps back. It never stays put, and it forgets its heading within a few steps, so over many ticks it wanders like dust. It leans only weakly toward your earlier 'a record moves the way its content points'.
      - Costs:
        - its lockable possibilities are the grid's six directions, which ties forming to the grid, while your Q3 left formation odds unglued;
        - what it locks changes at most steps;
        - as written it covers one record only. Two records can step into one site, up to 1 in 9 per tick when both point at it. Letting a blocked record stay keeps the rule complete and symmetric, but the rule for two records wanting one empty site is not built.
      - It moves records only. Light and anything that interferes still need a reversible change, which by the first bullet must reach further than one site per tick, use a supplied pattern, hold more than one qubit per site, or be exactly alike only on average. With records stepping by their own rule, point 1's one-site limit on the change no longer applies (argued)."
11. Old: "Nothing can get more than one site per tick: an exact limit, where smooth change only gives an approximate one."
    New: "Nothing can get further in one tick than the change reaches: an exact limit (one site per tick if the change is held to one site), where smooth change only gives an approximate one."
12. Line 68: after "(A17; argued, not built)." append: "For it to spread at all, its rule must escape point 3's first bullet."
13. After "  - nearest-neighbour versions jitter far too much." add: "  - if wandering records also hold light back, as records do in A14, the photon-mass limit forces them so sparse that the averaging region must be about the size of our galaxy, so the Sun's own field could not be resolved."
14. Line 87: after "the way light works in the photon lane." append: "A rule held to one site per tick and exactly alike on every tick moves no ripple (point 3). So this route needs a change that reaches further per tick, with records stepping by their own rule, or another of point 3's ways out. If the photon lane's rule runs smoothly and the same everywhere, point 1 says it already reaches past one site per tick."
15. Decision 1: append "That pattern of pairs is supplied structure: it cannot treat every site and turn alike on every tick (A20)."
16. Old: "2. **Reach.** Strictly one site per tick, or a faint longer reach?"
    New: "2. **Reach of the change.** Strictly one site per tick (then, if every tick treats every site and turn alike, nothing moves: A20), a longer reach (4 sites works but scrambles; 2–3 untested), or a faint longer reach?"
17. Decision 7: append "Under the six-direction step, what a record locks also changes at most steps."
18. Old: decision 8, from "Re-form next door with a six-direction menu" through "(A20)?"
    New: "8. **How records step.** By their own irreversible rule with a six-direction menu, so the content points the way the record stepped? It is symmetric under all 24 turns, but it ties lockable possibilities to the grid (your Q3 left formation unglued) and still needs a rule for two records wanting one site. Or by a supplied sub-grid pattern (A10)? (A20's longer-reach rules move only spreading webs of links, not records.)"
19. Add: "12. **How unrecorded things move.** Light and matter waves need a reversible change that moves something, and under one-site reach with exact sameness on every tick nothing moves (A20). Which gives: longer reach for the change, a supplied pattern, more than one qubit per site, or sameness only on average?"
20. Old: "and a second-reviewer pass on A20.*"
    New: ".*" (this pass is done).

**LOG fixes**
- Line 849, "This is the clean covariant one-site move … handed per A1 D22". New: "For one isolated record, a covariant one-site move: a six-outcome lock on its own qubit, then a swap. Use with several records needs exclusion and a clash rule. It is handed only if a mirror leaves possibilities unflipped; its trails are mirror-identical."
- A20's "nothing moves… not records". New: "nothing moves under any reversible change".

## Top 3 risks

1. **Theorem N is misframed as a "how records move" result, and the owner may think motion is solved.**
   - It stops all reversible motion at one-site reach with exact symmetry on every tick, including light, matter waves, A19's coasting movers and the gravity-field candidate.
   - The lock-and-move rule rescues records only.
   - Decisions 1 and 2 still offer "one set of pairs per tick" and "strictly one site" without saying that the first is a supplied pattern and the second means nothing moves.
   - No known reversible change carries particle-like content while treating every site and turn exactly alike on every tick with no supplied schedule. The Clifford movers scramble, and reach 2–3 is open.
2. **The lock-and-move rule is presented as "clean" but as written breaks "one record per site" with several records.** Collisions run up to 1/9 to 0.14 per pair per tick, and there is no stay outcome. It also:
   - conflicts with Q3's unglued formation;
   - renews what a record locks at most steps;
   - carries a handedness claim that depends on a convention the axioms leave open.

   Decision 8 also lists A20's long-reach rules as a way for records to step, which they are not.
3. **The "field of possibilities" candidate for gravity and smooth pacing collides with points 1 and 3.**
   - No ripple moves under one-site rules that are exactly symmetric on every tick.
   - The photon lane's smoothly running rule reaches past one site per tick.
   - Separately, v5 dropped the galaxy-sized averaging cost from the A18 package, so that package still reads stronger than it is.