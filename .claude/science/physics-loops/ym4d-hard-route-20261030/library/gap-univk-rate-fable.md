lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-23T00:40Z

# Row 1391, gap-univk-rate-fable: the ultraviolet carry (UNIV-K) in rate form, hypothesis (A1) of Theorem T

Started 2026-11-22T12:40Z (date -u), pinned at commit a1f83f4da. Worker file, not checked by another model. Research-stage working state; no status.

Moves: hypothesis (A1) of Theorem T (row 1332, `library/gap-shrink-box-fable.md` section 4.4; check 1335), which is also uniqueness of the continuum limit at a fixed physical size.

Credit: the account read here is YM4_1400.tex by Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Rows 924 and 925 (`library/gap-univk-opus.md`, `library/gap-univk-check-astra.md`) are the prior work this row builds on.

## Plan (written before any reading beyond FINISH.md and GOAL.md)

1. Repo search: rows 924, 925, 1332, 1335, 1386 and `library/open-core.md` for (UNIV-K), (A1), (MAPCONV), (VAC-ID), (DENS-K), (CLASS).
2. State (A1) in the rate form that Theorem T reads, with the dependence on ell.
3. For each of (MAPCONV), (VAC-ID), (DENS-K), (CLASS): find the account's passage, quote it, classify as proved / sketched / assumed.
4. Attack: prove (A1) in rate form as an implication from statements the account proves, or name the first input that fails with the explicit failure.
5. Equivalence test (rule "Equivalent is not progress") on any sufficient statement proposed.
6. Next two rows and their decisive outcomes.

Each step is appended below when it is done.

## Step 1. Repo search and prior work (written 12:43Z by date -u)

Search done inside this lane folder only. `origin/main` and the PR branches are not refs in this checkout, so the wider "Repo first" search was not run here; check 925 ran it on 2026-11-14 for these labels and found no hit outside this lane (`library/gap-univk-check-astra.md` L3-L46).

`library/open-core.md` has no entry for (UNIV-K), (MAPCONV), (VAC-ID), (DENS-K) or (CLASS) (grep, zero hits). FINISH rows that carry (UNIV-K): 916, 917, 924, 925, 978, 1225, 1229, 1233, 1237, 1238, 1240, 1242, 1248, 1263, 1326, 1331, 1332, 1335, 1340-1351, 1386. What they leave on file for the four inputs:

| Input | On file | Row |
|---|---|---|
| (CLASS) | Proposition 3.3 of row 1237 holds as an abstract tuning lemma; its application to the two runs FAILS (the account proves tuning for one frozen presentation) | 1237, check 1240 |
| (MAPCONV) | The account proves depth convergence only for the Taylor orders 2-4 of the classical action at the flat reference, the Gaussian polarization, and b_j, m_j. The rest is split into (M1) background map, (M2) Gaussian pointing, (M3) formation map; none is in the account | 1238 (unchecked on this point) |
| (VAC-ID) | Reduced to the account's Statement 3.4 (common companion, L84159-84204, an open input of the account) and the class bounds; Lemma VAC | 1248, check 1263 |
| (DENS-K) | B1 (extra bare level) and B2 (matched levels) open; the exponent of p_0 exceeds 8, so B1's arithmetic premise holds | 924, 1248 |
| Edge matching | The predecessor must be a first-passage datum; open | 925, 1242 |
| One-sided form | (ONE-K) needs only Phi(d) - Phi(pi d) <= (L^4+1) eps_K | 1238 Lemmas 3.1-3.2 |

Row 1238 Step 2.7 says that no text of the account states the two-cutoff comparison, and that YM4_SI makes it a hypothesis. That search was a grep of the nine submanuscripts. **It missed the account's own two-cutoff text inside YM4_1400.tex:** the subsections "Coupling coordinates and conditional comparisons" (L126164-131280) and "Weighted derivatives and matched presentations" (L131281-135994). No gap-lane file cites their matched-run statements (grep for "terminal-coupling", "partnered run", "matched limit", "geometric relabelling" in `library/gap-*.md`: the only hits are unrelated uses; row 1248 read L126169-126198 for the vacuum accounting only). These 9,800 lines are the account's treatment of exactly the object of this row. Steps 2-4 read them.

## Step 2. The account's own two-cutoff text: first reading (written 12:46Z by date -u)

Source: YM4_1400.tex (Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of its text), the copy at LOCAL:ym4d-papers/sa1400, 136,637 lines. "L n" is a line of that file. READ in this step: L126164-126330, L126377-126470, L130770-131110.

**2.1 The account says that its matched-cutoff estimates are hypotheses (READ L126170-126177).** The subsection "Coupling coordinates and conditional comparisons" opens: "The coupling, matched-run and Ward estimates below imply their stated conclusions by elementary analytic arguments. The interacting estimates themselves remain hypotheses." and ends its first paragraph: "None computes the one-loop trace or proves a matched-cutoff or typed Ward estimate." So the status of the two-cutoff comparison in the account is: **assumed** (a stated input of a conditional proposition), with a long sketch of how the inputs would be produced (L126445-130770, L131685-135912).

**2.2 The form of the account's matched comparison (READ L126377-126419, (CP8)-(CP9)).** Fix a torus T_ell, h = g^-2 and a separated tuple of n >= 2 tests. beta_K^nat is the torus-independent tuned bare centre, Xi_K(t) = x_K^nat(beta_K^nat - t) the terminal coupling at offset t, n_K = Xi_(K+1)^-1 o Xi_K the matching map. The required inputs are
  |n_K - t| + |n_K' - 1| + |Xi_(K+1) - Xi_K| <= C eta_K,
  |F_(K,n)(t) - n_K'(t)^n F_(K+1,n)(n_K(t))| <= C_(n,ell,f) eps_K,   sum_K (eta_K + eps_K) < infinity,
with F_(K,n) the n-point function at cutoff K. "Constants and cutoff floors may depend on this fixed ell." "Often eta_K = Upsilon_K <= C K^(-3/2) (log(2+K))^(p+1); a separate remainder error Pi_K is part of eps_K". The matched scalar increments are to obey (L126432-126436) sup_t |b^B_[u](n_K(t)) - b^A_[u](t)| <= C (rho^(K-u) + Pi_K), where "Pi_K is the error from the unmatched large-field terms at the bare end".

Three facts follow for this row.
- (a) The comparison is between cutoffs K and K+1 at **matched terminal coupling**, as rows 916 and 924 proposed. It is stated for n >= 2 separated tests on one torus. The zero-source two-torus quantity Phi is not in (CP9).
- (b) The dependence on ell is left free ("may depend on this fixed ell"; the strip has height c rho e^(-C(g) ell^4), L126407-126410). (A1) asks for C_U ell^4.
- (c) **The rates are polynomial in K, not geometric.** eta_K is of order K^(-3/2) up to logarithms, and Pi_K is polynomial in the account's own example (next item).

**2.3 The account's own warning on geometric rates (READ L130953-131103, "Why a geometric relabelling needs another construction").** The account gives the three-number example F_K(t) = (1, 1 + t, 1 + Pi_K), Pi_K = K^(-q), q > 1: all summable matching inequalities hold, and no reparametrisation and common normalisation make the increments geometrically small. It then bounds the difference of the transferred coefficients of two cutoffs (L131036-131076): the remainders born at depth s from the terminal lattice compare with a geometric factor rho^(K-s), but the terms born near the bare end have only their one-run size, so "a geometric comparison at each fixed depth may still yield a polynomial error for the sum of the transferred coefficients"; the bound is O(r-hat_K) with r-hat_K "of order theta_[K]^(2 - kappa_0/2) times a power of its logarithm", "summable for kappa_0 > 6". Here theta_[K] is the bare inverse coupling, which grows linearly in K.

So in the account's coordinates the two-cutoff error that the account aims at is a negative power of K. The reason is structural: the remainders and the large-field weights at the bare level are small only by a power of the bare coupling (g_0^(kappa_0), e^(-c p_0(g_0))), the bare inverse coupling grows only linearly in K (asymptotic freedom), and the terms born within a bounded number of steps of the bare end are not matched between the two runs.

**2.4 Consequence for the rate form (A1) (ARGUED from 2.2-2.3; made exact in Step 5).** (A1) asks eps_K <= C_U ell^4 q^K with q < 1. The account does not aim at this rate. Its own target gives, at best, eps_K <= C_ell K^(-r) with r > 1. So "prove (A1) in the geometric rate form from statements the account proves" has two separate failures: the comparison is assumed, not proved (2.1); and the rate the account sketches is polynomial (2.3). Step 5 shows which rate the consumer really needs.

**2.5 The account's use of the comparison (READ L130770-130952).** Proposition "The conditional terminal-coupling limit" (L130770-130795): the inputs give convergence of F_(K,n) without a subsequence, at each terminal coupling x. The first-passage application (L130814-130853) needs "a live frozen run of length K' from the same bare value, in the admitted real tuning class" (input E4), and "The comparison between the ordinary and the frozen bookkeeping, including admission of the frozen run, is the input to this argument." The two-run coupling comparison is required in the form (L130872-130877) |x^[i+1]_[s] - x^[i]_[s]| <= C (L^(-c(i-s)) + s Pi_i), sup_(s>=1) s sum_(i>=s) Pi_i < infinity. This is the account's version of (MAPCONV) for the scalar coupling, and it is a requirement, not a theorem.

## Step 3. Where the account names the two-cutoff comparison as an input (written 12:53Z by date -u)

READ in this step: L1650-1760 (first passage, the theorem's opening), L1831-1836 (clause (d)), L2490-2545 (Technical statements E1-E4), L3046-3058, L81165-81173, L83538-83544, L83898-83905, L99276-99282, L99834-99841, L126445-126660, L127265-127334, L131685-132060.

**3.1 The main theorem assumes it (READ L1748-1753).** "Assume the uniform background, interaction, history, flow and ordinary-source estimates of [the dependency catalogue], with their stated domains and normalization. For the short-distance clauses assume the interacting comparison and running-normalization estimates there; for the matched-cutoff and Ward clauses assume their additional estimates."

**3.2 The input has a name: Technical statement E3 (READ L2521-2534).** "Technical statement E3: a summable matched-cutoff comparison. At matched terminal coupling, require for each fixed torus and separated tuple |S^T_(n;K+1)(X) - S^T_(n;K)(X)| <= C(n,d,g,ell) eps_K prod_i ||f_i||_sharp, sum_K eps_K < infinity. The floor in K may depend on the fixed torus. [...] This is the actual analytic input behind the matched-run claims numbered 8a and the tuned Cauchy sequence; a bounded difference at each cutoff does not suffice."

**3.3 Edge matching has a name too: Technical statement E4 (READ L2536-2543).** "When moving between a self-calibrated first-passage run and a frozen run, the maps must represent the same bare integral and satisfy a stated uniform bound on their coupling discrepancy. [...] Exact dilation identifies the same finite lattice in two units, but supplies no estimate on this calibration discrepancy."

**3.4 Status lines elsewhere in the account (READ).**
- L83904-83905: "A whole-sequence limit along tuned runs requires the later matched-cutoff input; compactness alone gives no such conclusion."
- L81171: "The proposed summable matched-cutoff comparison and the resulting whole-sequence tuned convergence use the stronger comparison route."
- L81165: "the smallest useful replacement is an actual comparison of the two tuned trajectories: a step inequality, domination of the observable evaluations by the comparison distance, and a terminal-integral inequality with summable defects."
- L99838-99840: the fixed-cutoff measure argument "supplies no identification of two different extracted limits, no matched-cutoff convergence rate".
- L3052-3053: "The additional weighted, matched-cutoff and Ward conclusions require their stated hypotheses."

**3.5 What the account does prove at equal depth (READ L83538-83544, L1668).** The scalar Gaussian increments converge geometrically in depth (Corollary gpl-geometric-increments; rows 924 R10 and 1238 2.2 read the same fact at L94530-94545 and L93360-93392): "These estimates preserve the geometric comparison used at equal depth in the stronger matched-cutoff route." The increments b_k of one run do not depend on the torus or on the number of later steps (L1668, statement E1 names this as a hypothesis of the first-passage argument, L2494-2497).

**3.6 What the account sketches (READ L126445-126660, L127265-127334, L131685-132060; not checked line by line).** The two subsections of Step 1 are a long prose derivation of E3 from finer inputs. Its pieces, in the vocabulary of row 924:
- the scalar clause of (MAPCONV): the matched increments, (L126432-126436), from "the transfer of the regular chain, with the fixed physical extraction radius" and "the weighted forgetting estimate" (L126453-126457);
- the kernel clauses of (MAPCONV): "Transfer between the two bare lattices" and "The regional row form" (L131776-132040): for the finer lattice (sharp) and the other lattice (flat), an exact row-defect identity (comparison-regional-row-defect), a consistency estimate with the power (eta/xi_y)^beta, 0 < beta < 1, and the conclusions "At unit rows the entrywise rate is C L^(-beta k) when the step has k finer levels" and "a bound C L^(-alpha_K k) on the differences of the inverse covariance and the auxiliary Gaussian kernel, for some alpha_K > 0";
- the source-independent normaliser of a healed component: "divide the two integrals before taking the logarithm [...] its log difference costs at most sup |S_B - S_A| on the same cut" (L127281-127287), with the class estimate C theta_w^(n/8);
- the history comparison ((DENS-K) B2): "The integrated part requires the full comparison of weighted histories, including the shell and availability estimates below" (L126557-126558) and "The local estimate still requires the compared history masses on their actual test domains" (L126608-126609);
- the unmatched bare end ((DENS-K) B1): "Terms at an extra bare depth can be bounded by their one-run size" (L131046-131047); "the extra bare-end input" h <= C theta_[K]^(-nu-1), nu = (kappa_0 - 4)/2 (L126576-126577, L126493-126494).

So row 1238's finding "(M1)-(M3) are in no account text" needs a correction: YM4_1400 **sketches** the two-lattice comparison of the propagators, kernels, normalisers and Wilson response in L131776-132726, and of the earlier activities and matched histories in L132726-135912. It does not state them as numbered propositions with proofs, and its own header (2.1) says the matched-cutoff estimate is not proved there.
