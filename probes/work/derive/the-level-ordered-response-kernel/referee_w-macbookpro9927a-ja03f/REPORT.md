# Referee report — J:derive:the-level-ordered-response-kernel:a2

**Referee:** `w-macbookpro9927a-ja03f` (claude-opus-5-5).

**Attempt under review:** the files `ATTEMPT.md` and `check.py` in `probes/work/derive/the-level-ordered-response-kernel/w-macbookpro90c72-jf747/`. The log records the model as `grok-4.6`.

**The attempt's HIT:** the gain-one kernel is the unique causal solution of the parent recursion, (4/3) L!/(a!b!c!) 3^-L on the forward octant. Each level carries 4/3. The symbol is 8/E on drift-free modes.

**Independent checks:** `check.py` in this directory. All code is my own, and every check is exact unless it is labelled [float].

**Disclosure.** The label `jf747` was issued to a claim of the a2 unit that the referee's session held. The attempt's files and log were written by a different agent (`grok-4.6`), and the referee wrote none of them. Before that agent finished the unit, the referee had read attempt a1's log summary and the referee of a1, as the claim tool prints them. The referee has landed nothing on this problem.

## Verdict

**Confirmed.** Every step S1–S6 follows. The attempt's own open items (S7, and the large-distance form) are stated honestly as open.

The kernel is the same as attempt a1's, which was already confirmed by `w-macbookpro90c72-j4d1b`. What a2 adds is the uniqueness framing: its S1 and S2 characterise the kernel as the causal solution of the recursion.

## Step by step

**S1: follows (R1).**
- G(0) = Σ(1/4)^n = 4/3.
- The support lies in the octant, because every step is 0 or +e_j.
- Taking the last step gives G = (4/3)δ + (1/3)Σ_j G(· − e_j).
- Checked by a route of my own. The generating-function identity (3 − Σz)·Σ_{L≤K}(4/3)(Σz/3)^L = 4 − 4(Σz/3)^(K+1) holds, so 4/(3 − Σz) has exactly the coefficients (4/3) L!/(a!b!c!) 3^-L (all 455 monomials up to L = 12). Separately, the walk's exact visit sums over 80 steps meet the closed form within 10⁻²⁰ at every site with L ≤ 6, and the walk never leaves the octant.

**S2: follows.**
- Induction on the level L = a + b + c, given the support condition, which the statement includes.
- Without causality the recursion is not unique: any constant solves its homogeneous part (R2).

**S3: follows.** My own loop confirms the recursion through level 12 (R2). The identity holds for every L by the telescoping in R1.

**S4: follows.** The level sums are 4/3 for L ≤ 12 (R2), and for every L because the trinomial law sums to 1.

**S5: follows.**
- G(1,0,0) = 4/9 and G(−1,0,0) = 0.
- "The wake points along (1,1,1)" is carried by the formula: level L's trinomial is centred on (L/3)(1,1,1).
- The large-distance form itself (on-axis decay and Gaussian width) is not derived here, as §3 says. Attempt a1 gives it as a labelled numerical result.

**S6: follows (R3, symbolic).** On k = (q, −q, 0), 4/(3 − Σe^{−ik}) = 8/E, and the light-cone gain-one kernel is 7/E.

A note on units. Those two symbols are Neumann-series kernels (1 − P)⁻¹. Block 91's window uses a different unit: the source enters the rule's argument like one more predecessor. In that unit the response is (1/c)(1 − P_c)⁻¹, with c = 4 for level-ordered formation and c = 7 for light-cone formation. On drift-free modes these give 2/E and 1/E, so the comparison is 2 to 1, not 8 to 7 (R4).

**S7: open, as the attempt says.**

**Statement against the task.** The task's HIT criterion is "(a) exact", and the kernel is exact. Part (a) also asks for the large-distance form against the inverse Laplacian, which a2 leaves open.

## Referee side computation for (b), exact (R4)

This part is not refereed.

At zero temperature the rule becomes s′ = H/|H|. Around the aligned state its transverse part is v/c + O(v²). So the nonlinear rule itself, at β = ∞, answers a held source as follows:
- **Light-cone formation:** exactly 1/E(k), which is the top of block 91's window.
- **Level-ordered formation:** exactly R(k) = 1/(3 − Σ_j e^{−ik_j}).

For the level-ordered response:
- |R|·E = 2(3 − Σcos k_j)/|3 − Σe^{−ik_j}|, which is at most 2. It equals 2 exactly on the drift-free set Σ_j sin k_j = 0: 163 modes on 16³ ([float] scan), with the maximum elsewhere below 2.
- In position space, R = G/4. Its drops at r = 1 are 4/3 (forward) and 2 (backward) times the inverse Laplacian's drop, which is exactly 1/6.

So at β = ∞ the answer to (b) is yes: the level-ordered law exceeds the light-cone bound by up to a factor of 2.

The probes' finite-β position-space ratios for level-ordered formation are 0.918–1.060 (block 91). These are far below the zero-temperature values. Either the nonlinear law at the probed β is not close to its zero-temperature limit, or the probes' r = 1…4 average mixes directions. Which one is not settled here.
