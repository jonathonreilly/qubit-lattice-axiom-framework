lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T12:16Z

# Explicit-region two-step test (queue item 32, `explicit-region`, neutral)

Pinned at `eda9debc5`. Finished in this session. **Firewall:** this file reads mapped statements closely and quotes them. An independent-side reader should get Sections 1, 2 and 3 up to Lemma CONC by the lead's extract. No proof text of either attempt is carried; the lemmas proved here are new.

**Provenance.** Anthropic, claude-opus-5-5, effort max, one session, no subagents. Same-model research text, not an audit, and it grants no status. Labels: *discharged* (proof here, by hand), *implication* (proof here, given named inputs), *gap* (no proof), *memory* (recalled, not read and not proved). Dimock's papers were read in the open arXiv text; Balaban only through open abstracts. Nothing from either carries weight until rebuilt here.

## Verdict

**An explicit region does not price the fine energy behind (HW) and (PATCH), and in the form Dimock prints it cannot be run at d = 4. What removes both stops on these two examples is an order of integration, with a state of bounded-age holes and local activities.** Two statements are proved by hand and are not conditional on any attempt: a heavy field is the typical field (Lemma TYP), and persistent regions leave an empty small-field region at the top (Proposition HOLES). The surviving form is a two-step form with named gaps, not a closed induction step.

| Criterion | Persistent regions (Dimock's form) | Bounded-age holes, absorbed |
|---|---|---|
| R1 rare test | raw fine energy: **FAIL**, Lemma TYP | own-level relative test: PASS, Lemma FIB |
| R2 retained data | not reached | PASS, Lemma RD |
| R3 no relative gauge | not reached | PASS |
| R4 column | **FAIL**, (2.1) | PASS at two steps; all depth not claimed |
| R5 insertions | not reached | PASS as a form; size is (INS_k), gap |
| R6 commutator square, locked pair | not reached | PASS |
| R7 sectors | not reached | PASS |

| Queue question | Answer |
|---|---|
| Does a region price the energy? | No. Raw fine energy is typical; own-level energy needs no price to be integrated |
| Boundary-data induction | **Keeps** a small one, bounded age, own level |
| Generated-current K3 | **Avoids** the clause; its decay returns in (INS_k) |
| Across-sector locality | **Avoids** |
| Weighted upper bound | **Avoids** the comparison (UP), (WAM), (PATCH); **keeps** depth-uniform regularity, as (CONTR) |
| Is dropping the state costing more than it saves? | Dropping persistent regions was right: they fail. Keeping one global function looks like the real cost, on the mapped side only; this is an inference, Section 7 |


## 0. Criteria, registered before the derivation

The question: on the two examples of `library/heavy-wall.md` and `library/seam-nlpay.md` (identity-parent pairs at a wall; locked pairs in frozen bricks), does an explicit large-field region price the fine energy that stops (HW) and (PATCH)?

- **R1, the region must be rare.** A region is priced only if its test marks the pack and is rare at typical fields. A test that fires at typical fields prices nothing. *Fail:* the test marks the pack only because it marks everything.
- **R2, retained data.** With the pack on the boundary of a retained region, every term of the conditional partition function must be bounded with no small l^2 energy on a patch larger than a block. *Fail:* a term that grows with the pack size M, other than the common classical term.
- **R3, no relative gauge.** *Fail:* a step that compares two independently given global fields, as (PATCH) does.
- **R4, column.** Sum the history cost at d = 4 on the flow x_j = x_K + b(K - j). *Fail:* a region that must persist to the top, with total cost above its own price.
- **R5, insertions.** Two separated insertions through two steps. *Fail:* a step that needs a generated current under a mixture law.
- **R6, mandatory examples.** The commutator square of `gates/energy-stages-codex-b87de884f.md` and the locked pair, for any new statement.
- **R7, sectors.** A retained boundary with nonzero winding. *Fail:* a comparison of values across sectors by a path.

A pass here is a two-step statement. It does not prove all-depth closure.

## 1. The heavy field is the typical field (R1)

Write A(U) = sum_p (1 - (1/2) tr U_p) and weight exp(-x A). This is the normalization of `parts/hard-core--mapped.md`: its slope c_0 = (11 N^2 / 12 pi^2) log L is the one-loop slope of x = 4/g^2 at N = 2.

**Lemma TYP (discharged).** *Let x >= 1. Let B be a set of links, no two in one plaquette. Given all links off B, with any values, the links of B are independent, and e_b := sum_(p containing b) (1 - (1/2) tr U_p) obeys 0 <= e_b <= 12 and E[e_b | rest] >= 1/(8x). Hence, with n = |B|, sum_b e_b <= A(B^+), the action of the plaquettes meeting B, and P(A(B^+) <= n/(16x) | rest) <= 9216 x^2 / n.*

*Proof.* Independence: no plaquette reads two links of B. Fix b. Its six plaquettes are U_b S_p with S_p in SU(2). A real sum of unit quaternions is a real multiple of a unit quaternion, so sum_p S_p = s R with 0 <= s <= 6, R in SU(2). Put u = (1/2) tr(U_b R). Then e_b = 6 - s u. Under Haar measure u has density (2/pi)(1 - u^2)^(1/2) on [-1, 1], so given the rest, w = 1 - u has density proportional to (w(2 - w))^(1/2) exp(-k w) on [0, 2], with k = x s.
Case k >= 1. On [0, 1/(2k)] the density is at most (2w)^(1/2), with integral 1/(3 k^(3/2)). On [1/(2k), 1/k] it is at least (2k)^(-1/2) e^-1, with integral at least 0.13 k^(-3/2). So P(w >= 1/(2k)) >= 0.13/(0.13 + 0.334) >= 1/4, and E w >= 1/(8k). Thus E[e_b | rest] >= s E w >= 1/(8x).
Case k < 1. Then s < 1/x <= 1 and e_b >= 5.
Each plaquette holds at most one link of B, which gives sum_b e_b <= A(B^+). Each e_b has variance at most 36, so Chebyshev at distance n/(16x) gives the tail. QED

Take the direction-1 links with base points in (2Z)^4 inside a level-j cell, side L^j, so n >= L^(4j)/16:

    fine action on a level-j cell >= L^(4j) / (256 x_0), with probability >= 1 - 147456 x_0^2 / L^(4j).        (1.1)

x_0 grows linearly in the depth K, and L^(4j) exponentially in j. So above j_* := log_(L^4)(10^7 x_0^2) = O(log K), **a level-j cell of a typical field carries fine energy above any fixed multiple of T^2, with probability near one.** The pair pack of (HW) with amplitude about x_0^(-1/2) and M about L^(4j) is the typical field, not a corner. The triggers of `library/energy-by-stages.md` (A_c(U) > kappa T^2, dense boxes) fire on typical fields at every level above j_*, and the hypothesis ||theta(U)||_P <= epsilon_0 of Lemma U fails there on the field being integrated. An excess over a minimal lift does no better: by (R3) of the mapped part, an input here, the lift of a class top has energy at most C T_2^2 on a cell, so the excess of a typical field is still of the size (1.1).

**R1, verdict on raw fine energy: FAIL.** No region defined by fine energy at a fixed threshold can be rare, so none can price that energy. Sections 3 to 5 show what replaces it: the test has to be read at the field's own level, with everything finer already integrated.

## 2. Persistent regions cannot work at d = 4 (R4)

Dimock's induction, rebuilt from the printed statements of arXiv 1212.5562 (Theorem 3.1) and 1304.0705: the regions decrease, Omega_1 > Omega_2 > ... (each Omega_(j+1)^c holds the rounded and buffered Omega_j^c), so a large-field cube found at level i removes one cube of every coarser level, up to the top. The sum over histories is closed at 1304.0705 (205): a level-i cube pays, for its column, sum_(j >= i) C (-log lambda_j) r_j^3, and this is bounded by C (-log lambda_i)^(3r + 2), **using N - i <= -log lambda_i**. That inequality says the column height is at most the logarithm of the inverse coupling. It is the superrenormalizable fact lambda_k = L^(k-N) lambda, and it has no analogue on the flow x_j = x_K + b(K - j), where the height K - i is about x_i/b. The open abstract of Balaban's CMP 119 (1988) says the same in its own terms: the inductive description of the densities with large-field domains completes the analysis for superrenormalizable models. The abstract of CMP 122 (1989) names the R operation as what removes the main obstacle in four dimensions.

This is not only a loss in an estimate. The holes really are everywhere.

**Lemma RARE (discharged).** *Let 0 < T <= 1/2, x >= 1. For a link b and any values of the other links, P(some plaquette at b has angle > T | rest) >= q := (T^3/12) exp(-12 x T^2).*

*Proof.* With the notation of Lemma TYP write u = cos phi, phi in [0, pi], the angle of U_b R. If all six angles are at most T then s u = sum_p (1/2) tr(U_b S_p) >= 6 cos T, so s >= 6 cos T and u >= cos T, that is phi <= T. So the event contains {phi > T}. Given the rest, phi has density proportional to sin^2(phi) exp(k cos phi), with k = x s <= 6x. Let k >= 1. On [T, 2T] the density is at least (4 T^2/pi^2) exp(k(1 - 2T^2)), using sin phi >= 2 phi/pi and cos phi >= 1 - phi^2/2. The full integral is at most exp(k) times the integral over [0, infinity) of phi^2 exp(-2 k phi^2/pi^2), using sin phi <= phi and 1 - cos phi >= 2 phi^2/pi^2. Evaluating, P(phi > T) >= (16/pi^(5/2)) (2/pi^2)^(3/2) k^(3/2) T^3 exp(-2 k T^2) >= (T^3/12) exp(-12 x T^2). For k < 1 the density is within e^2 of Haar, and P(phi > T) >= e^-2 (1 - 2 T^3/(3 pi)) >= q. QED

**Proposition HOLES (discharged, given the flow's upper bound).** *Let x_0 <= x_K + B K, with 12 B T^2 <= 2 log L. Then a level-K cell contains no level-0 plaquette of angle above T with probability at most exp(-n q), with n >= L^(4K)/16, and*

    n q >= (T^3/192) exp( 2 K log L - 12 x_K T^2 ).        (2.1)

*Proof.* Take the link set of (1.1). Given the other links the events are independent, each of probability at least q, so the probability that none occurs is at most (1 - q)^n. Insert the flow. QED

The hypothesis holds for T <= 1/2 at the actual slope B about 0.372 log L. Any smaller threshold only makes more holes, so this covers Balaban's thresholds g p(g), and the fixed T of both attempts. So for K >= K_0 := (6 x_K T^2 + log(192/T^3))/log L, every top cell holds a rough fine plaquette, except with doubly exponentially small probability, and a union bound over the fixed number of top cells keeps that. **In any induction where a large-field cell removes its ancestors at all later levels, the small-field region at the top is empty for K >= K_0.** In phi^4_3 the same count is L^(3(N-j)) exp(-c (N-j)^(2p)) and it is summable, which is why Dimock needs no R. Explicit regions at d = 4 must be absorbed after finitely many levels, or there is nothing left to run the induction on. The same count appears, as a recorded difficulty, in the mapped part's reading of Balaban's R (`parts/hard-core--mapped.md`, Text 1) and it is what its positive gas answers.

**R4, verdict on persistent regions: FAIL, by (2.1).** The state cannot be "regions with histories" in the form of Dimock's Theorem 3.1. Only regions of bounded age can be carried.

## 3. Pricing at the field's own level, on one fibre

Section 1 says what cannot be tested; Section 2 says what cannot be stored. This section gives the test that survives. It reads one level, on one fibre, and needs no replacement, no shell and no gauge on a patch. Here r_lift, bricks and Dev_b are as in `library/quiet-boundary-rarity.md`, Setting.

**Lemma CONC (discharged, from Lemma PL of `library/upper-chain-by-hand.md`).** *Let K in R^n be bounded and convex, S in C^2(K), Hess S >= m Id on K, m > 0, and mu proportional to exp(-S) on K. (i) If f is l-Lipschitz, mu(f >= mu(f) + t) <= exp(-m t^2/(4 l^2)). (ii) If K is a box and eta^* minimises S on K, then mu(|eta - eta^*|^2) <= n/m. (iii) Both hold for the conditional law of some coordinates given the others.*

*Proof.* (i) Convexity gives S((a + b)/2) <= (S(a) + S(b))/2 - (m/8)|a - b|^2. For bounded Lipschitz phi put Q phi(a) := inf_b [phi(b) + (m/4)|a - b|^2]. Then 1_K exp(-S) at the midpoint is at least the geometric mean of 1_K exp(Q phi - S) at a and 1_K exp(-phi - S) at b, so Lemma PL gives mu(exp Q phi) mu(exp(-phi)) <= 1. Take phi = s f, s > 0. Then Q phi >= s f - s^2 l^2/m, and Jensen gives mu(exp(-s f)) >= exp(-s mu(f)). So mu(exp(s(f - mu f))) <= exp(s^2 l^2/m). Chebyshev at s = m t/(2 l^2) gives (i).
(ii) Integrate div(exp(-S)(eta - eta^*)) over K. On the boundary <eta - eta^*, nu> >= 0, so mu(<grad S, eta - eta^*>) <= n. Strong convexity and <grad S(eta^*), eta - eta^*> >= 0 give m mu(|eta - eta^*|^2) <= n.
(iii) A coordinate section of K is a box, and S restricted to it has the same bound. QED

**Input (CHART_k), unchecked here; it is the statement "one uniformly log-concave integral" of the mapped part.** For W in D_(k+1) let Lift(W) minimise F_k on fib(W) := {V : M V = W}. Use tree gauge in each level-(k+1) block, rooted at its centre, with the frames of neighbouring blocks joined by the links of W. Coordinates eta on the free bonds, V = V(eta), V(0) = Lift(W), solving M V = W, box K := {|eta_b| <= R}, V(K) in D_k. Then S_W(eta) := F_k(V(eta)) - log Jac obeys Hess S_W >= x_k gamma Id on K, with gamma = gamma(L) > 0 free of k, volume and W. **All fields of a fibre share one frame bundle: the transition functions between block frames are the links of W.** At k = 0 this is a statement on the Wilson action alone, with no R.

**Input (MODE_k), unchecked here; Theorem F-D level.** With P := b^++ and any values of eta off P in K, the minimiser of S_W on P given those values has Dev_b <= eps_q^2 T^2/16.

**Lemma FIB (implication, given (CHART_k), (MODE_k)).** *Let W be in D_(k+1), S a set of level-k bricks, n_P the number of free bonds of a patch, and x_k >= 1536 n_P/(gamma eps_q^2 T^2). Then, under the law proportional to exp(-S_W) on K,*

    P_W(every brick of S non-quiet) <= exp( - x_k gamma eps_q^2 T^2 |S| / 1600 ),

*and for every E, with Dev_S the sum of Dev_b over S, P_W(Dev_S >= E) <= exp( -x_k gamma (E^(1/2) - eps_q T |S|^(1/2) / 2)_+^2 / 400 ).*

*Proof.* In the frames of the fibre, |theta_c(eta) - theta_c(eta')| <= 2 sum_(b in c) |eta_b - eta'_b| for small logs, and a bond lies in six plaquettes, so f_S := Dev_S^(1/2) is 10-Lipschitz. By Lemma CONC (ii), (iii) and (MODE_k), E[Dev_b | off P] <= eps_q^2 T^2/8 + 192 n_P/(x_k gamma) <= eps_q^2 T^2/4, so E f_S <= eps_q T |S|^(1/2)/2. Apply Lemma CONC (i) with m = x_k gamma and l = 10. QED

Three remarks. The bound is additive in |S| and in energy, so the doubling profile of `library/heavy-wall.md`, Section 1, at own level, is priced in one line: there is no selected layer because nothing is cut. It is a statement on one fibre, so the depth does not enter. And by the tower property, for a top W_r at any level r > k + 1,

    P(S | W_r) = E[ P_(V_(k+1))(S) | W_r ],        (3.1)

so rarity below a class top at any depth is, on the event that V_(k+1) is class, no harder than at depth one. At class fields this is the rarity that the excess inequality (AE-R), and with it (HW), was built to supply. Non-class V_(k+1) is treated in Section 4, row (f). At k >= 1 the input (CHART_k) contains the gas of lower exits, so it stands on row (e); the order is well founded, since row (e) at level k reads exits at lower levels only.

**Test against R1.** A typical field has Dev_b about t_0^4/x_k, far below eps_q^2 T^2 at x_k >= x_*. A brick holding pairs of amplitude a at its own level has Dev_b = 12 a^2 per pair. So the test is rare and it does see own-level packs. R1: **PASS** for the own-level relative test. A pack below the own level is not seen at all, and it should not be.

## 4. The two-step example, SU(2), d = 4

Fields U -> V = M U -> W = M V, at levels 0, 1, 2. M is a hard local covariant block map, as both attempts have; only (CHART_k), (MODE_k) and the row inputs below read which one. A block B of level k + 1 **exits** if the level-(k+1) field is not in D_(k+1) on B^+, or the level-k field on B is not in V(K). A connected set of exit blocks is a *hole*. Its *age* is the number of levels since its first exit.

**The state at level k.** Not one function and not a sum over histories:

    F_k(V; t) = x_k A_k(V) + v_k |cells| + sum_X E_k(X; V)
                - sum_i t_i sum_(Y meets X_i) O_i^(k)(Y; V) - t_1 t_2 sum_(Y meets X_1, X_2) C^(k)(Y; V),        (ST_k)

on fields in D_k off the live holes. Here X, Y are connected polymers of level-k cells with local activities depending on V on the polymer only. A live hole gamma, of bounded age, keeps its field V on gamma^+ as a variable of integration, exactly as a region does, with its conditional partition function below. Two insertions O_1, O_2 are bounded, gauge-invariant, with supports X_1, X_2 at distance d; a finite set of order n is the same with t_I for |I| <= n. At k = 0: F_0 = x_0 A - t_1 O_1 - t_2 O_2, no polymers and no holes. That is exact.

**The conditional partition function.** For a set X of level-2 blocks, hole data d on X, and top W:

    Z(d; W) := integral over V off X, in K, of exp(-F_1(d u V)) Jac,
    zeta_2(X; W) := integral_(d exits on X) Z(d; W) / integral_(d in K) Z(d; W).        (4.1)

The two integrals have the same exterior and the same top, and differ only in the data. Then, exactly, for V in D_1 and W in D_2,

    rho_1(V) = rho_1^b(V) ( 1 + sum_(X != empty) zeta_1(X; V) ),    rho_2(W) = rho_2^b(W) ( 1 + sum_(X != empty) zeta_2(X; W) ),        (4.2)

with rho_(k+1)^b(W) the integral over K of exp(-F_k) Jac. **Absorption:** when W is class on X^+, the hole is gone after this step: zeta_2 enters F_2 through -log(1 + sum zeta_2), localized, and no field is retained. A hole here is the explicit large-field region of this form. A bounded activity at level 1 is averaged by the integral over the fibre at level 2, not multiplied, so a hole costs no factor per later level.

**Lemma RD (data are read at mixed plaquettes only; discharged).** *At level 0 write A = A_D(d) + A_mix(d, U) + A_Omega(U), with A_mix the plaquettes reading both. Then the exterior integral is exp(-x_0 A_D(d)) Z_m(d_mix), with d_mix the links of d in mixed plaquettes. For d_t a path of data, log Z_m(d_1) - log Z_m(d_0) = -x_0 times the integral over t of E_t[d_t A_mix].*

*Proof.* The first statement is locality of the action. The second is differentiation under the integral. QED

So a pack inside retained data enters by its own factor and nothing else. A pack on mixed links enters by a sum over its pairs of local terms, each at most C x_0 a (a + x_0^(-1/2)) once the exterior is in the chart. In the Gaussian limit the dependence is exactly classical: Z_m(d) = Z_m(0) exp(-x_0 H_min(d)). **R2: PASS.** Nothing reads an l^2 energy on a patch larger than a block, because the only gauge used is the block frame.

**The terms of the two steps.**

| Row | Term | Size | Status |
|---|---|---|---|
| (a) | Chart integral rho_1^b: Laplace in (CHART_0), with x_1 = x_0 - beta_1 | one-loop; local after a cluster expansion in blocks | input; the form is standard, not written here for this map |
| (b) | Level-0 exits under class V: zeta_1(X; V) | at most prod_B (C x_0)^(n_B/2) exp(-c x_0 R^2/L^2) | implication at k = 0, given a quiet collar and T_2 small against R/L: a bond log above R forces a loop of area at most C L^2 with holonomy at least R/2, so energy c R^2/L^2 by Stokes and Cauchy-Schwarz, against C T_2^2 for the reference, and Haar mass at most 1 against a Gaussian denominator |
| (c) | First exit at level 1 under class W: U in the chart, V out | exp(-c x_0 R^2/L^2) | Lemma CONC on the two-level fibre of U over W, given the two-level form of (CHART_0), which needs the logs on an L^2-block, at most L^4 T_2, small against gamma(L^2). The bond logs of V are L^-1-Lipschitz in those of U on the tube they read, by Cauchy-Schwarz over its L^3 lines, so a bond log R of V costs c x_0 gamma(L^2) L^2 R^2. Reads no field below U, and at level k reads F_(k-1) only |
| (d) | Exit at level 1 above a level-0 exit | product of (b) and (c), by the tower property | implication, for separated holes; a joint hole is one polymer |
| (e) | Marginal part of the gas: D^2 log(1 + sum zeta) | beta_(k+1) <= beta_k (1 + small) + C x_k^2 z_k, summable | **gap, (GAS2).** At k = 0 direct: differentiating (4.1) costs a factor C(L) x_0 per derivative against z_0, and gauge invariance removes the linear term. All-level: the real-variable form of the R operation |
| (f) | Live hole: W not in D_2 on gamma | conditional partition function kept; age at most log_L(diam gamma) + h_max, h_max := 2 + ceil(log_(L^2)(pi/T_2)), unless a new exit occurs, which has its own price | implication given (PF): a parent's flux reads a child cell with weight about L^-2. Locality of the exterior, (I_k^gamma), is a **gap** |
| (g) | Insertions | below | form exact; size **gap (INS_k)** |

Row (e) is where the count of Section 2 goes. Absorption removes the hole, not its effect: a level-k cell receives about L^(4(k-j)) z_j level-j events. Their field-independent part is the vacuum term v_k. Their dependence on V_k must be small, and a sup-norm bound alone does not give that: a variation of V_k moves the flux of V_j by about L^(-2(k-j)), so a first-order term would sum to L^(2(k-j)) z_j, which is not summable, and only the quadratic term sums, to about x_j^2 z_j per level. The linear term vanishes at V = 1, since the activity is gauge invariant and the fixed box in chart coordinates is too. So the route lives or dies on (GAS2).

Row (f) is what the age bound buys against Section 2. A hole's column is at most log_L(diam) + h_max levels, its cost at most C(L)(|gamma| + log diam) log x, and its price is at least c x |gamma|, so x >= x_*(L, a_*) pays it. **R4: PASS at two steps, for absorbed holes.** All-depth closure is not claimed.

**Insertions.** Let O^(k)(V) := E[O | V_k = V]. The tower property gives, exactly,

    Cov(O_1, O_2) = E Cov(O_1, O_2 | V) + E Cov(O_1^(1), O_2^(1) | W) + Cov(O_1^(2), O_2^(2)).        (4.3)

The first two terms are covariances on one fibre at distance d/L^k in cells, under the actual law, for two functions; the last is the coarse integral. On class fields between the supports it decays in the fibre: this is the source of Y running from X_1 to X_2 in (ST_k), and a hole on the path costs z per block. No mixture law, no generated family, no good set and no boundary screening is read. The output is the polymer form of Proposition 7.3 of `parts/upper-chain.md` in real jets, so Proposition 8.1 and Theorem 7's real form are its consumers; the hard cut gives real jets, and complex sources are not claimed. **R5: PASS as a form.** What is kept is the size: for a plaquette insertion O^(k) must be of order iota_k L^(-4k) times an own-level energy, with the marginal coefficient iota_k extracted exactly, and its activities must decay. That is (INS_k), and it is insertion renormalization, not a saving.

**R3: PASS.** Every comparison above is between fields of one fibre, or of a two-level fibre, in frames joined by the parent. Nothing compares a minimiser with a trial across many levels. The zero-energy example of `library/seam-nlpay.md`, Section 3 (r_old = +1, -1 on two overlaps), cannot occur: frames are fixed by the root and by W, so the parent does the coordinating that example asked for.

**R6: PASS.** Commutator square: in the fibre's tree gauge exp(tX) exp(tY) exp(-tX) exp(-tY) is one bond with log of size about 2 t^2, and its action is half the square of that, 2 t^4 at small t, in agreement with 2 sin^4 t; the inequality that failed read a linear curl in a representative that is not gauge-fixed, and no such step occurs here. Locked pair: Lemma RD, and no bond is frozen except in a live hole.

**R7: PASS.** Take a level-k lump of radius about T^(-1/2), the example of `library/sector-values.md`. It is class, and its parent W carries it, since the frames are joined by W. Each fibre is one chart in every sector, each comparison is on one fibre, and the two sectors meet only in the final coarse integral, where the source is bounded. A hole whose collar winds has polymers around it of size at least T^(-1/2), so they are small.

## 5. The two examples

**Pair pack, `library/heavy-wall.md`.** M pairs of amplitude a = T/8 with identity parents, at level 0, as many as a level-j cell holds. With R of order T_2 we have a <= R, so these fields lie in the chart over V = 1: there is no exit and no label, and they are integrated with their weight. (HW) was asked of an operation on one chain. Here no operation on a chain exists: a level-j test reads V_j, and F_(j-1) already contains the pack's integral. If a consumer wants the marks, Lemma FIB prices them at level 0, additively, at x_0, doubling profile included.

**Seed beside the pack.** A level-j seed of amplitude 3T next to the pack: by (3.1), P(pack, seed | V_(j+1)) <= sup_(V_1) P_(V_1)(pack) times P_(V_(j+1))(seed), with V_1 class near the pack, which holds in the example beyond the seed's collar. The prices multiply. Depth, walls and shells do not appear. Why (HW) stops and this does not: the pack needs depth j >= log_(L^4) M to fit, and a comparison here spans one fibre, or at most h_max + 1 levels in row (f).

**Locked pairs, `library/seam-nlpay.md`.** The copies are quiet, so nothing marks them. There are no frozen bricks: frozen fine data exist only in a live hole, and only at own level. If a copy sits in a live hole, Lemma RD gives the common factor exp(-x_0 M e(a)), which is the cancellation Section 5 of that note found by hand. (U-local) on a top cube is never read, and neither is the inference it refuted.

**Repair of (PATCH) on the mapped route, unproved, evidence for the owner.** Item (R2) of the mapped Text 5.3 builds the minimiser as U = exp(i eta H) U^tr, by a fixed point around a trial, at every depth, with H bounded on local sup norms and a decaying response. That is a relative field by construction, with no patching and no use of Lemma U. (PATCH) is the first stop of a route through two independent local gauges. If (R2) stands, with T close to U^tr, and its response decay gives the kernel K of (NL-pay), then (ALIGN) is an output and (PATCH) is not asked, with no change of state. I have not checked that its norm pays the left side of (NL-pay), nor that (R2) stands.

**Does an explicit region price that energy? No.** At raw fine level nothing can (Section 1). At own level the energy is in the convex chart and needs no price to be integrated; a price exists if a consumer asks (Lemma FIB). **(HW) and (PATCH) are not energy problems. Both come from holding a fine field fixed: (HW) from a statement quantified over every chain, (PATCH) from aligning two fields that share only a distant parent.** Integrating before testing removes both on these examples. This does not decide (HW) or (NL-pay) as statements; it says the route does not need them, subject to the gaps in Section 7.

## 6. What it avoids and what it keeps

For the form that survives, (ST_k) with absorbed holes. The persistent form fails R4 first and is not classified.

| Item | Avoids or keeps | What is left |
|---|---|---|
| **Boundary-data induction** | **Keeps, much smaller** | (I_k^gamma): the exterior of a live hole, with own-level data, a quiet collar and age at most log_L(diam) + h_max. The all-age frozen layers go, and with them uniformity in the number of ages and the junction statements, because the hard core no longer stops on quiet surfaces. A local (ST_k) gives the exterior by construction; it is still owed |
| **Generated-current K3** | **Avoids** | (4.3) reads two functions under one law: no LL mixture closure, no generated family, no good sets, no RC or MC clause. The decay of O^(k) in the far field returns as activity decay in (INS_k), for finitely many functions. Insertion renormalization stays |
| **Across-sector locality** | **Avoids** | No comparison crosses sectors, and values of local activities are bounded directly, not integrated along a path. (VAL), (VAL^d), (Loc^c) are not read. Needs the chart to be blind to the sector, which the mapped text states |
| **Weighted upper bound** | **Avoids the comparison, keeps the need** | (UP), (WAM), (GLUE-E), (LC) and (PATCH) serve FALL, which serves the low orders of the one function R_k through the ladder of lifts. With activities carried level by level, no minimiser is compared with a trial across levels. The need does not vanish. Dimock's contraction (1108.1335, Lemma 11: gain L^-eps once the relevant terms are removed) reads a domain of smooth fine fields that (133) of 1212.5562 supplies uniformly in k. The SU(2) analogue is depth-uniform regularity of the lift plus the contraction of the activities, (CONTR), not written for this map |

Kept in every form: uniform convexity on a fibre, the marginal extraction with no loss per level, the large-field term (GAS2), which is the R operation in real variables, and insertion renormalization.

## 7. Cost against saving, and what is open

**Regions.** Dropping them was right. Proposition HOLES shows persistent regions are not an option at d = 4, and the mapped record of Balaban's R, a component healed after waiting, is the same conclusion. No attempt should carry them.

**One function.** The mapped state, F_k one function with no local form, is where the cost sits. It was chosen because a local density of R_k could not be extracted afterwards from derivative bounds on a class with no global path, and because free-boundary densities carry a surface excess growing like L^3 per level. Both objections are to extracting a local form afterwards or defining it by free boundaries. As far as this test sees, neither reaches activities carried from level 0, with tails summed by a cluster expansion in blocks: the surface excess comes from fine-level surfaces, and a hole has none below its own first exit. What the one function costs, by the dependency recorded in the mapped part: locality has to be recovered by stops on quiet surfaces at all levels, values by a chain sum over the ladder of lifts, and rarity by a statement over all chains. Those three are (I_l^d) with all ages, FALL with (UP), and (AE-R) with (HW). **Inference, not a theorem:** on these examples local activities cost a cluster expansion and (GAS2), and save the three lists above, so the trade is favourable on the mapped side. It has not been shown to close.

**The independent attempt.** Its state already has local coefficients in a tree norm. Nothing here bears on (CN), which is inside one step, except that Proposition HOLES rules out regions there too.

**Ranked open items.**

1. **(GAS2), all levels.** Row (e). The density of Section 2 has to be carried by quadratic vanishing with summable constants, through chain rules at every level. Only k = 0 is written. A first-order term surviving at a hard cut kills this route. Everything below is conditional on it.
2. **(CHART_k), (MODE_k) at k >= 1**, with the gas inside. This is the closure of the small-field step, the same statement the mapped induction owes, and it has not been proved here. The surviving, fully specified induction step of `FINISH.md` is therefore **not delivered**.
3. **(I_k^gamma).** Exterior locality at a live hole, uniformly in the shape.
4. **Large and tall holes.** Rows (c), (f) use a chart over at most a few levels. Beyond it the price is by absolute energy, with entropy per cell. This is written only as a count. The bound on age needs (PF), which has to be checked for the actual map, including dropped blocks with Haar parents.
5. **(INS_k).** The insertion's scale gain and marginal coefficient.
6. **(CONTR).** Contraction of the irrelevant part of the activities on class fields, at flux T_2 at lattice scale. `library/sector-values.md`, Section 3B, records a hazard this must beat: at second variation a level's non-abelian remainder is a constant per level if the l^4 norm of the variation is bounded only by its l^2 norm. In Dimock's scalar model that hazard is absent, since his functionals are analytic on a uniform domain.
7. **Consumers.** The form delivers real jets, so Proposition 8.1 and the real form of Theorem 7, not the Text 14 clauses. Rarity (RAR^1) follows from (3.1) only on class parents, and deep columns (RAR^ch) would need a count of new exits. Whether the witness reads a clause this form does not deliver has not been checked.

**What two steps cannot see.** Anything at depth: the constants of row (e) composed many times, the flow, and a marginal coefficient at a rough field. d = 4 enters here only through Section 2 and the block counts. Passing R1 to R7 justifies attempting the step; it proves nothing past two levels.

## 8. Read and not read

Read: `FINISH.md`, `GOAL.md`, `library/heavy-wall.md` and `library/seam-nlpay.md` in full; the interface and the statements of Text 7 of `parts/upper-chain.md`; `library/quiet-boundary-rarity.md`, Setting through Theorem DM and the restated induction, which includes proof text of Theorem DM read for what it consumes; statements of `library/energy-by-stages.md` Sections 1 to 3, `library/induction-with-boundary-data.md` Sections 1 to 2 and `library/sector-values.md` Sections 0, 1 and 3B heads; the state of attack of `parts/hard-core--mapped.md`, its Text 1 record of Balaban's organization, items (R1) to (R3) of Text 5.3, and the lines of Text 5 and Text 6.0 that record the objections to a local form. **Two oversteps of the item's reading rule, named here:** those part-file lines carry some proof text, read for their statements, and Text 1 paraphrases the Sussman-Alpoge account, so the description of Balaban's R in Sections 2 and 7 comes through that unvetted paraphrase. It supports no proof here; verdict tables of `library/tail-two-step-c.md`, `library/joint-induction-two-step.md`; the statement of (CN) in `library/conditional-normalization.md`; sections 1, 3, 6 of `gates/strategy-codex-b5251ab07.md`.

Literature: Dimock, arXiv 1108.1335 (Sections 3.5, 4.8 only), 1212.5562 (Sections 1 to 3.4 and the bound (133)), and 1304.0705 (Sections 1, 2, 3.5), the last being the same series, read because the sum over regions is closed there. Balaban: the abstracts of CMP 119 (Rutgers record) and CMP 122 (Springer record) only. No full Balaban text was read. His R is known here only from the abstract and that paraphrase, and any statement about how Balaban builds his activities is **memory** and is not used in a proof.

Not read: the Sussman-Alpoge repository; proofs in `parts/hard-core--independent.md`; any proof in the part files beyond the lines named above. No statement of the chain rests on a run. `checks/explicit_region/constants_check.py` checks the elementary constants of Lemmas TYP and RARE numerically, pass criteria written first, RESULT PASS, under the numeric lock at 60 percent memory free; it guides and discharges nothing. No subagent, commit or push was made.
