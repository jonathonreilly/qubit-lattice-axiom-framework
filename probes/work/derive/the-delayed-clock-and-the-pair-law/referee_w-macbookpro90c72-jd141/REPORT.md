# Referee report — J:derive:the-delayed-clock-and-the-pair-law:a2

**Referee:** `w-macbookpro90c72-jd141` (claude-opus-5-5).

**Under review:** `probes/work/derive/the-delayed-clock-and-the-pair-law/w-macbookpro90c72-ja546/`, which holds ATTEMPT.md and check.py. The log records the model as `grok-4.6`. The claimed HIT is: "no joint law of product form (a law of the records times one deterministic clock field) is stationary at finite Gamma when log kappa != 0; a single record does not trap its direction".

**Independent checks:** `check.py` in this directory. Every check uses my own code. They are exact unless labelled [float].

**Disclosure.**
- The worker label `ja546` was issued to this machine's claim of the a2 unit, and the referee's session held that claim.
- The files and log under that label were written and run by a different agent (the log records `grok-4.6`). The referee wrote none of them.
- The referee's own draft for this problem was never landed. The referee read the attempt only for this report.

## Verdict

**The attempt fails at step S3.**
- S3 does not prove the attempt's own statement (b). It treats the flat field and the slaved bump, and nothing else.
- That statement is itself weaker than the task's. Section 1 replaces "a joint law of product form" with a law of positions times one deterministic field.
- Neither (a)'s hop rate nor (b)'s pair-law correction and reversibility is derived.
- The narrow claim is true once one line is added (R3). As written, it is not proved, and it does not meet the task's HIT criterion.

## Step by step

**Section 1 (statement): weaker than, and next to, the task's statement.**

*(a)* The task asks for the hop rate or diffusion constant in the joint stationary state. It also asks whether the record traps itself on its own trail, meaning that sites it has visited keep slow clocks.
- The attempt answers a different question: whether the direction is biased.
- Under departure timing the trail can act only through waiting times, and the attempt never computes them.

*(b)* The task's HIT names "an exact proof that no joint law of product form is stationary".
- The attempt restricts the field factor to a point mass δ(u − ū).
- A product law μ(C)·Q(du) with any field law Q is the task's form. The point-mass case is a strict special case.
- (b)'s first-order pair-law correction is not attempted, and the attempt says so. Reversibility is not attempted either.

**S1: follows (R1).**
- Block 95 P3 at a = 1 has rate `w_x^a w_y^(1−a) h/q`.
- One record occupies no bond, so W = 1 and h = 1/2.
- The rate to every neighbour is therefore w_x/(2q), whatever the field. One record's jump chain is the simple random walk at every Γ.
- The attempt's rate `w_x/d` is twice block 95's. That does not matter for S1, but the factor enters every 1/Γ coefficient.

**S2: the formula follows (R2).**
- Checked exactly for L = 3..12: the profile is 2 log κ·G, it has mean zero, and its on-site value is log κ (L²−1)/(6L). At L = 4, u0 − u1 = −3/4.
- Two precision notes:
  1. "`w_z > 0` only reparametrizes time" is false for a factor that differs from site to site. At u = (1,0,0,0) the weighted and unweighted velocities are not parallel. Only the zero set is shared, and that is all S2 needs.
  2. The relaxation conserves Σ_z 1/w_z exactly (symbolic check). That invariant, not block 95's "mean of log w" convention, fixes the level of the field in the joint process. The on-site contrast u0 − mean(u) is gauge-free, so S2's conclusion holds for the contrast.

**S3: does not follow as written. This is the first failing step.**

The statement covers every fixed field ū. The text treats two cases:
1. the flat field;
2. the slaved bump u*(positions).

The second case is not of the form μ ⊗ δ_ū at all, because it moves with the positions. The following are never treated:
- a fixed field that is neither flat nor any configuration's equilibrium. Example: ū = (1,0,0,0) on the ring of 4. Its drift is nonzero for all 10 configurations with 1 or 2 records (R3).
- as a product law, the case ū = u*(C0) for one fixed C0. The sentence "a hop leaves u* behind" comes closest.

**Repair** (the referee's, one line). Suppose μ ⊗ δ_ū is stationary.
- Then F_C(ū) = 0 for every C in the support of μ.
- F_C(ū) − F_D(ū) = Γ log κ · w ⊙ (n_C − n_D), which is nonzero for C ≠ D (R3, symbolic field on rings of 4–6). So ū is an equilibrium of at most one configuration, and μ = δ_{C0}.
- C0 is left at the positive rate Σ r0 w_x, so the law is not stationary. ∎

Case (2) does show that the slaved law is not stationary. That is true, but it is not the product statement.

**S4: fine (comparison only).** A note on the task text: its quoted law for departure timing, "W(C) exp(6 log(kappa) sum_pairs G)", has the opposite sign to block 95's T2 at a = 1, which is exp(−6 log κ Σ G).
- R5: on the ring of 6, across all moves of two records, detailed balance holds for exp(−2 log κ ΣG) and fails for the + sign.
- The attempt does not depend on this.

**Sections 3–4: incomplete list of what is missing.** The attempt names the pair-law correction as missing. It does not name (a)'s hop rate, which is computable at first order and is not zero.

R4 is a referee side computation. It is not refereed here and is offered only to show that (a) has a definite answer at order 1/Γ.
- After a hop, the field at the new site lags.
- Linearise the relaxation. Use (−M)⁺ = qG and the exact identity G2(0) − G2(e) = G(0)/q, where G2 = G∗G. The identity is checked on rings 3–12 and on the 4³ torus.
- The mean wait comes out as (1 − H)/R∞, with H = −q log κ G(0)/(2Γ) + O(log²κ/Γ, Γ⁻²). Here block 95's r0 = 1/(2q).
- So the long-run hop rate is R∞(1 − q log κ G(0)/(2Γ)). For κ < 1 the lagging record is faster than the slaved one. At this order it outruns its slow clock and is not trapped by its trail.
- [float] On the ring of 8, integrating the full nonlinear relaxation reproduces the linear coefficient −qG(0) = −1.3125 to 5×10⁻⁵. At log κ = −0.5 the nonlinear value is −0.91 per log κ.

**Toward the task's product statement.** Here Q is any law of the field, and the point-mass argument does not carry over, because a spread law can be carried into itself by the flow.

One possible route, sketched and not verified here:
- Test functions of the field alone show that Q must be invariant under the averaged flow Γ w ⊙ (Mu + log κ (ρ − n̄)).
- That flow's Dirichlet energy relative to its equilibria strictly decreases, which forces Q onto those equilibria.
- A test function that vanishes there and has a gradient transverse to the constant direction then gives π(C) log κ = 0 for every C with n_C ≠ ρ.

## Independent checks (this directory's check.py)

| Check | What it verifies |
|---|---|
| Q | Six definitions of block 95 (head f9b34475, PR #8860), five lines of the task and five lines of the attempt, all quoted verbatim |
| R1 | S1: symbolic rates for q = 2 and 6. Also shows that a = 0 would follow the target clock |
| R2 | S2: the profile exactly for L = 3..12; the invariant Σ 1/w (symbolic); the non-parallel velocities |
| R3 | S3: the gap example; the identity F_C − F_D = Γ log κ w (n_C − n_D) on rings of 4–6 |
| R4a | The exact ingredients of the first-order hop rate on rings and on the 4³ torus |
| R4b | [float] The nonlinear transient integral |
| R5 | The sign of block 95's a = 1 law against the task text |
