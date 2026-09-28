# The curvature member solved with moving records as its sources: when can the two charges balance?

Worker `w-jonathonsmac4f50-jae2d` (Claude Opus 5.5), unit `J:derive:the-member-with-record-sources:a1`.

**Provenance, disclosed.** Block 171 is a harvest by the supervisor on this same machine, in the same model family as this worker. It harvested #9122 (another machine, Claude), which #9336 refereed (`grok-4.6`). This attempt treats the case block 171 leaves open: "the member solved self-consistently with records as its sources", and "whether a clause whose hop energy vanishes with the field can balance". It is not a referee of block 171. It needs a referee from another family.

Sources: blocks 60, 95 and 110 read as landed on main; block 171 read on its pushed branch.

## 1. Statement attempted

**Setting.**
- **Member and walls.** Block 60's curvature member (T4, landed) on a box with walls held at w = ℓ = 1. Its site equations are block 110 T2(a) (landed): (Δχ)_z = −e_z/(8K w_z χ_z) and (ΔN)_z = (e_z + 2τ_z)/(8K χ_z). Write ε = 1/(8K).
- **Records.** One per site, on the interior sites; a configuration is C. They cross to an empty interior neighbour at block 110's crossing factor κ = √(w_x w_y)/(χ_x χ_y), as in block 171 T1.
- **Clause (supplied, a family).** H = m Σ_{x∈C} w_x + Σ_{b∈∂C} g(κ_b). Here ∂C is the set of the B interior bonds with exactly one end occupied, and g is smooth at κ = 1.
  - Block 171's rest-only clause is g = 0.
  - Its activity clause is g = μκ/2.
  - The task's example, "only the field's change of the crossing activity", is g = (μ/2)(κ − 1).
- **Charges.** Q = Σ e/(8Kwχ) and P = Σ(e + 2τ)/(8Kχ) (block 110 T2(b)), for the member solved self-consistently: the fields are sourced by (e, τ), and (e, τ) are evaluated on those fields.
- **In a stationary law**, the charges are averaged over the records' stationary law.

**Claims** (weak field, exact).

- **(i) The field's change of the crossing activity.** This clause has the same (e, τ) as block 171's activity clause, because the constant drops out of every derivative. Its hop energy vanishes with the field; its τ does not (μ/4 per end of each movable bond). So block 171 T3 applies: P/Q > 1 at weak field whenever a record can move.

- **(ii) The charges at the first two orders.** For every clause,

  P − Q = 2g′(1) B ε + ε² [−4m g″(1) S − 2m² n·Gn] + O(ε³),

  where the ε² bracket is for g′(1) = 0. Here G is the Dirichlet Green function of the box, n is the occupation vector, and S = Σ_{b∈∂C} [(Gn)_x + (Gn)_y].

- **(iii) What balances.**
  - Balance at the first order that does not vanish needs τ to vanish with the field (g′(1) = 0) and a concave clause tuned to g″(1) = −m n·Gn/(2S) < 0.
  - A clause with g′(1) ≠ 0 misses at order ε, on the side of the sign of g′(1): P > Q for block 171's activity clause.
  - With g′(1) = 0, every clause with g″(1) ≥ 0 (including rest only), and every jammed configuration, gives P < Q at order ε².
  - In a stationary law, the tuned value is −m⟨n·Gn⟩/(2⟨S⟩).

- **(iv) No clause fixed once balances two bodies.**
  - On the 5³ box (27 interior sites) under the uniform law, the tuned curvature is −(3739/36462)m for N = 1, −(103877/1011162)m for N = 2 and −(690875/6664644)m for N = 3.
  - For single records it differs at every site class: −11/162, −145/1762, −23/222 and −353/2546 (×m).
  - So for small ε every fixed clause leaves P ≠ Q for at least one of any two such bodies.
  - Even for one body, balance at finite field needs the clause tuned again at every order. For the centre record, the ε³ term is m²(472392 g‴(1) − 73777m)/280908.

- **(v) Dilute against compact bodies (floating point).**
  - Dilute records need about the single-record value. On the infinite lattice that value is −mG(0)/(2(12G(0) − 1)) ≈ −0.0622m, with G(0) Watson's constant.
  - Compact bodies need a curvature that grows with their size: −0.112, −0.165, −0.221, −0.284 (×m) for cubes of side 2 to 5 on a 17³ box.

**HIT.** (ii) is exact. Together with (iii) and (iv) it answers the question: P = Q can hold only for a concave clause tuned to the body, never for a clause fixed once. The task's example clause misses on block 171's side.

## 2. Steps

**Step 1 — the site equations with the record clause. CHECKED (A1), exact, symbolic, on a 4³ box.**
- From F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x) with N = e^u χ: ∂F/∂u_z = 8K w_z χ_z (Δχ)_z and ∂F/∂χ_z = 8K(w_z(Δχ)_z + (ΔN)_z).
- With λ = 2 log χ, the clause gives e_z = m w_z n_z + Σ_{b∋z} g′(κ_b)κ_b/2 and τ_z = Σ_{b∋z} g′(κ_b)κ_b/2. This uses ∂κ/∂u_x = κ/2 and ∂κ/∂λ_x = −κ/2.
- Stationarity is therefore block 110 T2(a).

**Step 2 — (i). CHECKED (A2), exact, symbolic.**
- The two clauses differ by the constant (μ/2)B, so they have equal derivatives.
- At zero field, τ = μ/4 at each end of every movable bond.

**Step 3 — existence of the self-consistent member at weak field. PROVED (standard import: the analytic implicit function theorem).**
- The equations −Δ(χ − 1) = ε e/(wχ) and −Δ(1 − N) = ε(e + 2τ)/χ, with zero walls, are analytic in (χ, N, ε) near (1, 1, 0).
- Their linearisation at ε = 0 is −Δ_D ⊕ −Δ_D, which is invertible.
- So there is a unique analytic branch, and its series is computed exactly in Step 5.

**Step 4 — the formula (ii). PROVED.**
- P − Q = ε Σ_x [2τ_x − e_x(1 − w_x)/w_x]/χ_x (block 110 T2(b)).
- **Order ε.** At zero field Στ⁰ = (g′(1)/2)·2B, which gives 2g′(1)B.
- **Order ε², with g′(1) = 0.**
  - The sources at zeroth order are e⁰ = mn and τ⁰ = 0.
  - So χ − 1 = εmGn and 1 − N = εmGn. Hence u = log N − log χ = −2εmGn, and κ_b − 1 = (u_x + u_y)/2 − (χ_x − 1) − (χ_y − 1) = −2εm[(Gn)_x + (Gn)_y], all up to O(ε²).
  - Then τ_z = Σ_{b∋z} g″(1)(κ_b − 1)/2, so Σ_z τ_z = −2εm g″(1) S.
  - The rest part gives e(1 − w)/w = mn(1 − w) = 2εm² n(Gn).
  - The hop part of e(1 − w)/w and the corrections from χ are O(ε²).
  - So the bracket is ε[−4m g″(1) S − 2m² n·Gn] + O(ε²).

**Step 5 — (ii) checked against the exact self-consistent series. CHECKED (B1, B2), exact rationals.**
- On the 5³ box the fields are iterated as series in ε, symbolic in (m, g′(1), g″(1), g‴(1)), with the exact Dirichlet Green matrix.
- The ε and ε² coefficients of P − Q equal (ii) for five configurations: centre, corner, a neighbouring pair, a distant pair, and three records.
- **FLOATING POINT (D1).** The full nonlinear site equations, solved by Newton to residual 10⁻¹⁵ at ε = 0.04, 0.02 and 0.01, reproduce the series.
  - Rest only: (P − Q)/ε² → −2m²n·Gn = −0.4314 (−0.4277 at ε = 0.01).
  - Tuned: (P − Q)/ε³ → −0.2626 (−0.2599 at ε = 0.01).

**Step 6 — signs. PROVED.**
- The Dirichlet Green matrix is the inverse of an irreducible nonsingular M-matrix, so every entry is positive.
- Hence n·Gn > 0 for N ≥ 1, and S > 0 whenever B > 0.
- So if g′(1) = 0 and g″(1) ≥ 0, the ε² coefficient is negative, and it is negative for B = 0 whatever g is.
- If g′(1) ≠ 0 and B > 0, the sign of P − Q at order ε is the sign of g′(1).
- **CHECKED (C3, C4).** The jammed 5³ box, and every two-record configuration on it.

**Step 7 — the stationary law. PROVED (standard: analytic perturbation of the stationary law of a finite irreducible chain).**
- At zero field κ ≡ 1, and the law is π₀ ∝ W (block 171 T1, with block 95's heat bath).
- The rates depend analytically on the self-consistent fields, so π_ε = π₀ + O(ε).
- When g′(1) = 0, P − Q = O(ε²) in every configuration. Hence ⟨P − Q⟩_{π_ε} = ⟨P − Q⟩_{π₀} + O(ε³), and the balance condition at order ε² is g″(1) = −m⟨n·Gn⟩/(2⟨S⟩)_{π₀}.
- **CHECKED (C2).** The uniform law (W = 1) on 5³, with N = 1, 2, 3: exact averages over all 27, 351 and 2925 configurations.

**Step 8 — (iv). PROVED from Steps 4 and 7 with the exact values in C1, C2 and C5.**
- A fixed clause gives c(C) = −4m g″(1)S(C) − 2m² n·Gn(C). If the tuned values of two bodies differ, their c's cannot both vanish, so for all small ε > 0 at least one of them has P ≠ Q.
- **CHECKED (B3).** For one body at order ε³.

**Step 9 — (v). FLOATING POINT (E1).** On a 17³ box: one record −0.0633m; four far-apart records −0.0636m; cubes of side 2 to 5: −0.112m, −0.165m, −0.221m, −0.284m.
- The infinite-lattice single-record value follows from n·Gn = G(0) and S = 6(G(0) + G(e₁)) = 12G(0) − 1, using −ΔG(0) = 1.

## 3. Where the route fails

It does not fail at weak field. The answer is structural. The rest energy's clock deficit grows like the body's own potential (n·Gn). The hop energy that could pay for it sits only on the movable bonds, weighted by the local field there (S). So their ratio is a property of the body's size and shape, not of the records.

## 4. What would finish or extend it

- A clause whose hop energy scales with the body's potential rather than with its boundary. For example, per record ∝ (Gn)_x: its τ would be a nonlocal functional, outside block 110's bond form.
- The clocked gas's law (block 171 T3). There W ≠ 1 favours clumps, which by (v) makes the tuned curvature more body-dependent.
- Beyond weak field: the fields that follow the records beyond first order change π at O(ε), which enters ⟨P − Q⟩ at O(ε³).
- Mean-field charges (the fields sourced by ⟨n⟩ rather than the average of charges per configuration) give a different weak-field average. That is a choice for whoever owns the clause.

## Prior art

- Blocks 60, 95 and 110 (landed) are restated.
- Block 171 (this machine's supervisor) evaluated the charges at prescribed fields.
- #9122 found T1–T3 at prescribed fields and simulated a clump on 8³ in floating point, with P/Q ≈ 2.16 under the activity clause.
- No probes attempt on this problem existed; the claim listed none.
- The positivity of the Dirichlet Green function and the analytic implicit function theorem are standard imports.

## Check

`python3 check.py` runs in about 10 s. Sections A–C are exact (sympy and Fractions); sections D–E are floating point and labelled as such. It prints `SUMMARY: PROVED …` and `HIT: …`.
