# Check of library/lfi-ho.md, collar revision (HC-WEIGHT)

Checked line by line by Claude (Opus 5.5), 2026-11-08. One check. Not an audit.
Clone at `c59ce25b0` (branch claude/ym4d-hard-route).
Sources read: Y = YM4_1400.tex 73556–73909, 80704–80748, 63044–63158; SA = YM4_sketch_500.tex 4866–4906, 5820–5881, 6180–6205, 6280–6314, 19440–19445, 23095–23150; IN1 in1.md 60–240.

## Verdict: FIX

The earlier repairs are applied correctly.
Section 4A is correct as written. Its algebra (C1)–(C7) checks.
The stop (c) at HC-WEIGHT is honest.
Per-carrier decay is needed. Restating H-O with the unweighted total would break its consumers.
But HC-WEIGHT is stated too broadly. Two of its three parts may already close from Y.
Route 3 also misses the real reason it stops: a strict rate margin is needed.
The repairs narrow the first open input. They do not change the proofs.

## Findings

1. **Earlier repairs.** Check findings 3, 6, 7, 9, 11, 13, 14, 16.
   CONFIRMED.
   - F3: ledger row SKETCHED at note 72. Reasons at 531–534.
   - F6: tie listed as input at 180–181, 200–201, 563. Sup over all admitted triples at 200.
   - F7: every δ_R through the full reader at 207.
   - F9: b_V open in the status table at 561–562, and attacked in 4A.
   - F11: (9a) at 258–263. Arithmetic checked. E+12r+2<0 is exactly q>2p₀+p₁+41r/2+2. Then ε>2p₀−5r>0. η>0 is exactly p₁<p₀−5r/2.
   - F13: radius (11r) at 504–510 matches 2/a_R from (3).
   - F14: split into (11a) DOM and (11b) H-E at 520–529. SA 6305–6307 and IN1 line 186 say what the note says.
   - F16: sa-2.13-2 §7 cited at 544.
   One gap: the registry row D4-CARRIED still lacks (11r). The task allowed only lfi-ho.md. Repair: the lead adds (11r) to that row.

2. **(C1).** Note 321–334; SA 5850–5856.
   CONFIRMED. SA gives 2M/ϱ by Schwarz. With ϱ=2/a_e this is a_eM_e. Cauchy gives (e^κ̄−1)^{−|K|}. Two pairs give the factor 2. The anchor bracket is pair-independent and cancels.

3. **(C2) and b_V = 2C_HC.** Note 340–373.
   CONFIRMED as a conditional implication. The grouping hypothesis at 340 is explicit. (C2) and (C3) give Σ osc ≤ 2C_HC ℓ^{2p₀}e^{−κd}.

4. **Route 1 test (C4).** Note 386–398.
   CONFIRMED. Sup one, anchor zero, endpoint oscillation a. Weighted value ae^{κn} is unbounded at fixed t,u. It tests the inference from depth discount alone. It is labelled correctly.

5. **The test at line 416.** Note 412–417; Y 73746–73758.
   CONFIRMED arithmetic. v_n has sup one and oscillation two. Its carrier spans n. It meets (C5) with N₀=n+1. At fixed ℓ_t it violates 2 ≤ b_V ℓ_t^{2p₀}e^{−κn} for large n.
   It is a real obstruction to deriving the per-carrier form from (C5). It is not an obstruction to the per-carrier form itself. An actual long-carrier collar piece comes from a switch extension, with Cauchy decay (R_s−1)^{−|K|}. Line 417 says this correctly.

6. **Does IN1 (18) need per-carrier decay?** IN1 199–201; Y 73561–73640; SA 4900–4906, 23108–23140, 6311.
   YES. The unweighted total does not suffice. Four reasons:
   - The next birth reads (18) per carrier. Y 73576–73580 gives b_R^♯ ≤ B_Φ^♯ ℓ̂^{p^♯} e^{−κd^in(R)} for each island-member carrier.
   - That decay is spent twice in (5). Y 73592–73596 counts carriers through a rooting cube by entropy. Y 73609–73617 pays the lost depth discount of gap-crossing carriers with e^{−cL^m}. A total per island gives neither.
   - SA 4900–4906 requires both a bound on |Ψ|/N(ω) and a carrier-by-carrier oscillation bound. SA 23108–23140 also uses M_R per carrier for the source slope.
   - The total C_col(1+c̄)N₀ is not uniform. N₀ = M⁴Σz_j(X) grows with the island (SA 6311: no small factor in the size). Y already uses this total as the envelope |V_X| ≤ [C_col(1+c̄)+1]N₀ at Y 73769.
   So a restated H-O with the total would duplicate the envelope and drop the clause SA calls required. Repair: add one sentence to Section 4A naming these consumers.

7. **HC-WEIGHT is broader than needed.** Note 302–303, 351–368; Y 73657, 73707–73756.
   UNCLEAR. Line 303 gives the wrong reason for keeping small carriers. The real reason is size: filing on X^∼ pays the total, and that is N₀-sized for the action difference (Y 73684–73703) and for W_X (Y 73749–73751).
   Two parts may close now:
   - The small Wilson sum is written 𝔳(X^∼) at Y 73657. Its bound is C(1+c̄)ℓ_t^{5r}, uniform in X (Y 73710–73711, 73736). If its prescribed carrier is X^∼, its weight is one and 5r<2p₀. That part of (C3) holds.
   - W_X splits into local plaquette carriers (Y 73754–73756). Each carrier is a bounded read with cost O(1+c̄). If no switch extensions enter, the per-carrier weighted sum is bounded. (C6) then applies with a bounded star.
   Repair: split HC-WEIGHT into three parts. Check the carriers of 𝔳(X^∼) and of the W_X pieces. Name the action-difference part as the first open input if the other two close.

8. **Route 3 is distinct and stops where stated, but for a sharper reason.** Note 421–474; Y 63044–63158 (C_b depends on the read star at 63124); SA 5873–5881.
   CONFIRMED (C6) and (C7). Distinct from Routes 1 and 2.
   Missed point: a strict rate margin is necessary. Test on majorants: take same-level entries at the class bound M_Y = E₀e^{−κd(Y)} (SA R13 is a sup norm, and SA 5880–5881 says domain sums need separate summability). Fix a large box R. Let Y be R minus m scattered interior cubes, and K the removed cubes. Then Y is connected, R(e,K)=R, and d(Y) ≤ d(R). The sum in (C3) is at least E₀Σ_m C(|R|,m)(R_s−1)^{−m} = E₀(1+(R_s−1)^{−1})^{|R|}. That is unbounded.
   So (C3) at rate κ cannot follow from rate-κ class bounds. It is a test of an inference, not of the actual collar. Also, line 426 bounds the base by c_h n_e. With c_h ≥ 1 this already spends more than rate κ on the base.
   Repair: state the margin requirement in Route 3. Use d(R_e∪K) ≤ d(R_e)+c|K| with R_e the entry's full class carrier, not c_h(n+n_e).

9. **SA 19445 supplies a margin.** Note 464–466; SA 19445.
   CONFIRMED in part. SA 19445 also says terms produced by 𝐓 decay at rate (1+4β_s)κ. For j<k it gives e^{−κd_j(X)} ≤ e^{−cκd_j(X)}e^{−(1+3β_s)κd_k(X̂)}. The note cites only the comparison. The margin is the useful part.
   Repair: cite the rate (1+4β_s)κ. Then the residual is a mask-and-label comparison, below.

10. **Swallowed exempt hulls.** Note 467–471; SA 6191–6198.
    CONFIRMED as a test of the metric inference. UNCLEAR whether it bites. SA 6195–6196 uses the hulls of the label's standing islands. The check could not find whether the label in (18) for an island's own factors also exempts its nested inner hulls. If it does, this test does not apply.
    Repair: settle which exempt family (18) uses for a new island's factors.

11. **CA and Y 80704–80748 alternatives.** Note 476–480.
    CONFIRMED. Y 80708–80710 uses the whole island carrier C^∼ with length zero.

## Closing routes

- **A. Split by part.** Close the 𝔳(X^∼) and W_X parts from Y 73707–73756 (finding 7). The residual is the action difference.
- **B. Margin lemma for the action difference (HC-MARGIN).** For each actual collar entry with class carrier R_e and switch set K, prove
  d_t^♮(𝒮; R(e,K)) ≤ (1+2β_s) d_t(R̂_e) + c|K| + C,
  with masks included and c, C fixed before κ̄. With the SA 19445 rate (1+3β_s)κ, the leftover β_sκ d pays the root entropy. This is Route 3 with the right input. Its failure would be a long mask layer or an unexempted swallowed hull.
- **C. Restate the consumer's rate, not its form.** Return (18) at a fixed lower rate κ_O, for example κ/C_mask. The consumers in finding 6 (Y 73592–73617, SA 23108–23140) need only a rate above their entropy floors. Kept changes are refiled on X^∼ (Y 73887–73892), so the lower rate does not compound across births. This removes the rate problem. It does not remove finding 10. It changes IN1 (18). Every reader of (18) must be checked for a match with the class rate κ of R23 first.
- **Not a route:** the unweighted total of Y 73660–73758 (finding 6).

## Corrected status rows

| Claim | Status |
|---|---|
| Earlier check repairs | Applied. (11r) still to be added to the D4-CARRIED row by the lead. |
| HC-WEIGHT, small Wilson and W_X parts | Possibly closed from Y 73707–73756; carriers to be checked. |
| **First open input: HC-WEIGHT, action-difference part** | **Open.** Needs a strict rate margin (finding 8); route B or C. |
| H-O restated with the unweighted total | **Rejected.** Consumers need per-carrier decay (finding 6). |
