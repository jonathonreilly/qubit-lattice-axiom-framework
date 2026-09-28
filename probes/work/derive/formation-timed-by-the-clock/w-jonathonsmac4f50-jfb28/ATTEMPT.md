# Formation timed by the clock: no formation law of the form z·e^{b·u} keeps block 95's pair law

Worker `w-jonathonsmac4f50-jfb28` (Claude Sonnet 5.5), unit `J:derive:formation-timed-by-the-clock:a1`.

**Provenance and overlap, disclosed.**
- **Overlap.** Attempt a2 (`w-macbookpro9927a-jef4e`, Claude Opus 5.5, unrefereed) reaches the same central theorem. Both attempts use the same Laguerre-rule argument for condition (ii) and find the same two roots on 3³ (21.3588 and 7.0872).
  - This attempt is therefore not independent of a2 in method or in family.
  - It re-derives and re-checks that theorem, and extends it in the four ways listed in the next paragraph.
  - I recommend that a referee check a1 and a2 together.
- **Order of work.**
  - The claim's printed summary of a2 gave the shape of the iff (conditions on the creation flux and on the total creation rate).
  - I derived the reduction, the proofs and every check below myself, then read a2's ATTEMPT.md and compared.
  - Blocks 95 and 171 were read as landed (95) and on its branch (171). Both are the supervisor's family (Claude).
- **New relative to a2, as far as I read it:**
  - the exact series of the joint chain on 3³, and the exact first-order deviation formula;
  - the single exception, b = 0 with W = e^{m(2a−1)E}, which a2 lists as untreated;
  - the case a = 0;
  - an exact time-to-jam on the 3×3 torus, with the coupon-collector identity for b = 0 (a2 has a ring of 7).
- **Nothing is adopted.**

## 1. Statement attempted

**Model** (block 95 as landed, plus the task's formation).
- On the L^dim torus, u_z(C) = m Σ_{r∈C} G(z − r) with m = 2dim·λ, w = e^u, and G the mean-zero inverse of Δ = 2dim·I − Adj.
- **Motion.** A record at x moves to an empty neighbour y at rate exp[a u_x + (1 − a) u_y]·h/(2dim), with h = W(C′)/(W(C) + W(C′)). Block 95 T2: the pair law is π_n(C) ∝ W(C)·exp[m(1 − 2a) E(C)], E(C) = Σ_{pairs} G.
- **Formation.** An empty site x forms a record at rate z·e^{b u_x(C)}. Records are permanent.
- The hypotheses are listed so that the headline only names the class proved: `W ≡ 1`, one record per site, `a ∈ {0, 1}` in the exact checks, `b` an integer in the exact checks and real in the argument, cubic 3³ torus for the machine checks.

**Claims.**

- **(b1) The exact criterion, any finite state space.**
  - The law of C given the count n equals π_n at every count and every time, from the empty lattice, iff both:
    - (i) the creation flux F_n(C) = Σ_{x∈C} π_{n−1}(C∖x)·f(x; C∖x) is proportional to π_n(C);
    - (ii) the total creation rate β(C) = Σ_{x∉C} f(x; C) depends on |C| only.
  - Here f is any positive creation rate and the motion preserves π_n at each count.

- **(b2) For the family f = z·e^{bu}.**
  - **Condition (i).** On 3³ with W ≡ 1, condition (i) at count 2 holds iff b = 1 − 2a.
  - **Condition (ii).** Condition (ii) at count 2 holds iff λb = 0. That is a proof for every real λb ≠ 0, not only isolated values.
  - **The conclusion.** With λ ≠ 0 and a ≠ 1/2 (a nontrivial pair law), no b works. (i) needs b = 1 − 2a ≠ 0, and (ii) needs b = 0.
  - **The only survivors** are:
    - a = 1/2, b = 0, where the pair law is flat;
    - b = 0 with W = e^{m(2a − 1)E}, which cancels the pair law (π_n uniform).

- **(b3) How it fails, at b = 1 − 2a.**
  - The count-2 law is π₂ at leading order, and then drifts.
  - Exactly: d/dt of the conditional law at t = 0⁺ equals −(1/3)·π₂(C)·(β₂(C) − E_{π₂}β₂). This holds for all 351 pairs, and is nonzero.

- **(a) Where the second record forms.**
  - Its offset law is q_b(d) ∝ e^{bmG(d)}. At a = 1, π₂(d) ∝ e^{−mG(d)}, so q_b ∝ π₂^{−b}: the reciprocal power of the equilibrium law.
  - At b = 1 with slowed clocks near records (κ = 24/25), the second record forms at a nearest neighbour with probability 0.128 < 6/26, and on the body diagonal with 0.401 > 8/26. It goes into the void.
  - Motion then pulls the pair together: π₂ has nearest 0.377 and diagonal 0.214.

- **(c) Time to jam (exact, 2D 3×3 analogue).**
  - The lattice always jams. The full lattice is the unique absorbing state, and every state reaches it.
  - z·E[T] = H₉ = 2.8290 exactly for b = 0, whatever z or the motion.
  - z·E[T] lies between the slow-formation and frozen-motion limits, and rises with z:
    - b = 1: 2.5141, 2.5154, 2.5161 at z = 10⁻⁶, 1, 10⁶;
    - b = −1: 3.1897, 3.1903, 3.1906.
  - Forming on the site's own clock (b = 1) jams sooner than uniform formation; against it (b = −1), later.

**HIT.** (b2) with (b3), the exception, and (a) and (c). They overlap a2's theorem; the new content is listed above.

## 2. Steps

**Step 1 — the criterion (b1). PROVED.**
- Suppose the joint chain on subsets, with counts n = |C|, satisfies P(C, t) = p_n(t)·π_n(C) at every count. The forward equation at count n is
  ∂_t P(C) = (Q_n P)(C) + Σ_{x∈C} P(C∖x)·f(x; C∖x) − β(C)·P(C).
- Q_n is the motion generator. It preserves π_n, so Q_n π_n = 0 (block 95 T2 for W as supplied; re-checked in B).
- Substituting gives p_n′·π_n(C) = p_{n−1}·F_n(C) − p_n·β(C)·π_n(C), for every C and t.
- Summing over the configurations of count n (π_n normalised): p_n′ = m_{n−1}·p_{n−1} − β̄_n·p_n, with m_{n−1} = Σ_C F_n(C) and β̄_n = E_{π_n}β.
- Substituting back and subtracting: p_{n−1}·[F_n(C) − m_{n−1}·π_n(C)] = p_n·π_n(C)·[β(C) − β̄_n] for every C and t.
- **Small t.**
  - From the empty start p_n(t) ~ c_n·tⁿ with c_n > 0, because every formation rate is positive and each count is entered only from below. So p_n/p_{n−1} → 0 as t → 0, and p_n > 0 for t > 0.
  - If A(C)·p_{n−1} = B(C)·p_n for all t with A, B not both zero, then A(C)/B(C) = p_n/p_{n−1} is constant in t. That contradicts p_n/p_{n−1} → 0 unless B = 0, and then A = 0.
  - So both brackets vanish: (i) with the constant m_{n−1}, and (ii).
- **Sufficiency.** If (i) and (ii) hold, then P = p_n(t)π_n(C) solves the equation with p_n′ = m_{n−1}p_{n−1} − β̄_n p_n. By uniqueness of the finite chain, it is the law.

**Step 2 — (i) at count 2. PROVED, CHECKED (D1).**
- F₂({r, s}) = (1/V)·(f(s; {r}) + f(r; {s})) = (2/V)·E(d)^b, since π₁ is uniform. π₂ ∝ E(d)^{1−2a}.
- They are proportional over all offsets iff E(d)^{b − 1 + 2a} is constant, iff b = 1 − 2a. This needs E to take at least two values: on 3³ it takes four (A2).
- **D1:** exact for a = 0, 1 and b = −3..3.

**Step 3 — (ii) at count 2. PROVED (E1–E4), exact and interval.**
- **The rate.** β₂({0, d})/z = Σ_{x∉{0,d}} exp(t·(G(x) + G(x − d))) with t = m·b. That is an exponential sum with integer coefficients.
- **The differences.** Take f_A = β₂({0, e₁}) − β₂({0, (1,1,1)}) and f_B = β₂({0, (1,1,0)}) − β₂({0, (1,1,1)}).
  - Each has exactly 6 exponents and 2 sign changes; f(0) = 0; f′(0) = −7/81 and −2/81 ≠ 0.
  - So t = 0 is a simple zero.
- **Laguerre's rule.**
  - A real sum Σ c_j e^{μ_j t} has at most as many real zeros, counted with multiplicity, as sign changes in its coefficients ordered by exponent.
  - Hence each of f_A and f_B has at most one nonzero real zero.
  - The sign pattern (0⁺ against +∞) makes it positive.
- **Interval brackets (40 digits).**
  - f_A has its zero in [21.3588082, 21.3588102].
  - f_B has its zero in [7.0871683, 7.0871703].
  - They are disjoint, so no t ≠ 0 makes β₂ equal on all offset classes.
- **Consequence.** (ii) holds iff λb = 0, on the smallest cubic torus. Exact witness E4: three distinct β₂ values for b = ±1, ±2, ±3.
- **General L.** On every torus L ≥ 3, β₂ is non-constant to first order in t: ∂_t β₂({0, d})/z at t = 0 is Σ_{x∉{0,d}}[G(x) + G(x − d)] = −2(G(0) + G(d)), using ΣG = 0 and G even, and it differs between offsets with different G(d). The all-orders proof above is for 3³ only.

**Step 4 — the exact series (C1–C4). CHECKED.**
- The Taylor coefficients of P_k(C, t), k ≤ 2, through t⁴, exactly, on 3³ (351 pairs), with creation out of level 2 as a killing term. It is exact for level 2 because nothing returns from level 3.
- **Result.**
  - The t² coefficient of the level-2 law is ∝ π₂ exactly for (a, b) = (1, −1) and (0, 1), and for no other b tried.
  - The t³ coefficient is never ∝ the t² one, except for the flat case: with b ≠ 0, β₂ is not constant; with b = 0 the failure is at t².
  - **The exception (C3).** b = 0 with W = e^{m(2a−1)E} passes at every order through t⁴.
- **The first-order deviation.**
  - a₂₂ = c·π₂, since Q₂π₂ = 0 and the leading coefficient is proportional to it.
  - a₂₃ = (1/3)·[F a₁₂ − β₂·a₂₂], and F a₁₂ ∝ F₂ ∝ π₂, because a₁₂ is uniform (by translation symmetry).
  - So the conditional law is π̂₂·[1 − (t/3)(β₂ − β̄₂) + O(t²)]. C4 checks this identity for all 351 pairs.

**Step 5 — (a). PROVED, CHECKED (F1, F2).**
- At one record all formation rates depend only on the offset: f(x; {r}) = e^{bmG(x − r)}. So the second record's offset law is q_b ∝ e^{bmG(d)}, whatever the first record's history and z.
- q_b·π₂^b is constant exactly (b = ±1, ±2).

**Step 6 — (c). CHECKED (G1–G4), exact.**
- Level-by-level linear solves on the 2D 3×3 torus (512 states), with exact rational data.
- **b = 0.** Formation rates are z per empty site, so the count process is a pure birth chain with rates z(9 − n), independent of motion. E[T] = H₉/z.
- **Limits.**
  - The slow-formation limit Σ_n 1/E_{π_n}β_n is the adiabatic value: formations are rare enough that motion equilibrates between them.
  - The frozen-motion limit is random sequential formation.
  - z·E[T] at z = 10⁻⁶ and 10⁶ lies within 10⁻⁵ of them (exact rational comparison).
- **Monotonicity in z** is shown at three values, not proved.

## 3. Where it stops

- **Scope of (ii).** The all-orders proof of (ii) is for 3³ only; general L is first order in λb.
- **The class W.** Only W ≡ 1 and the one W that cancels the pair law were treated.
- **What "no formation law" means here.** No law of the form z·e^{bu} with block 95's motion. Nonlocal or state-dependent creation rates are not excluded.
  - A transportation-polytope argument shows a suitable f can exist at count 1→2, where f ∝ π₂/π₁.
  - The obstruction is at count 2→3, through (ii).
  - The general existence question at every count is not settled here.
- **The 2D analogue.** The jam times are for the 2D 3×3 torus, which is block 95's construction with Δ = 4I − Adj, not the cubic torus.
- **Not covered:** records with removal (the block 39 birth–death pair), and the time law of E[N(t)] in closed form.

## 4. What would finish it

1. (ii) for every real λb on every torus L ≥ 3.
2. The general-W version, where π_n carries a weight the clock cannot.
3. Whether any nonlocal creation rate keeps the pair law at every count: a Hall-type condition on the marginals of π_n and π_{n+1}.

## Prior art

- Block 95 (landed): T2 gives the pair law. Block 171 (the supervisor's harvest): the crossing-rate law and the exact 3³ clocked-gas ratios.
- **Attempt a2** (`w-macbookpro9927a-jef4e`): the criterion, condition (i), the Laguerre argument with the same brackets on 3³, and the ring-of-7 jam times.

## Check

`python3 check.py` runs in about 4 minutes. All exact (Fractions and sympy); the interval brackets in E use mpmath interval arithmetic. It prints `SUMMARY: PROVED …` and `HIT: …`.
