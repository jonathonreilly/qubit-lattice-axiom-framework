# Check of row 1683 (gap-purity-afield-astra62.md), FINISH row 1698

lead: anthropic/claude-opus-5-5 laptop subagent

Started Sat Nov 28 14:34:52 UTC 2026, pinned at commit fe90ec8ae. Checked by Claude Opus 5.5; author of the checked file gpt-6.2-astra max.

## Plan

1. Read gap-purity-crux-card.md (target (PUR-io)).
2. Read gap-purity-afield-astra62.md in full.
3. Read gap-solve2-astra62.md section 1 (Bessel multiplier bounds, row 1145).
4. Read gap-purity-rh-strategy-fable-check-astra62.md section 4 (Y4 filter).
5. Find the files of rows 1141, 1145, 1273, 1283.
6. Check items 1-5; small exact computations as guides only.
7. Verdict per item; RESULT line.

## Findings (appended as the check runs)

### Progress log

- Read in full: `gap-purity-crux-card.md` (60 lines), `gap-purity-afield-astra62.md` (381 lines).
- Read the cited inputs at their locators: row 1145 §1 L15-51; row 1155 (9) L130-134 and the tilted twist bound L420; row 1149 (34) L467-475; row 1153 (4)-(5) L82-92; row 1141 (3) L60-68; row 1283 (1)-(5), (11) by grep; row 1273 Lemma S L334; Y4 filter §4 L93-104.
- Earlier cross-provider checks of the inputs, read by grep only (verdict lines): row 1146 on 1145 (1)-(3) HOLDS; row 1156-file `gap-solve7-check-opus.md` on 1155 (9) and L420 HOLDS; `gap-solve4-check-opus.md` on 1149 (34) HOLDS; `gap-solve6-check-opus.md` on 1153 (5) HOLDS; `gap-solve23-check-opus.md` on 1215 (28) HOLDS; `gap-solve32-check-opus.md` RESULT row 1283 HOLDS; `gap-crux2-check-opus.md` RESULT row 1141 HOLDS. I rely on those checks for the inputs and did not redo them, except the spot guides below.
- Float guides (never proof), script in the scratchpad `guide1698.py`, output: max over s in [0.01,800], d in [2,29] of (I_d/I_1)/exp(-(d-1)/(1+s)) = 0.99937 < 1; Haar SU(2) P(1-C_p<=v)/v^{3/2} -> 0.2757 = 4(3/4)^{3/2}/(3 pi); Haar U(1) P(1-cos t<=v)/v^{1/2} -> 0.4502 = sqrt2/pi; U(1) I_j(x)/I_0(x) increasing in x on the grid; U(1) z_{b/2}/z_b -> 1.414.

## Item 1. The PROVED steps (1)-(18), §7 and §8

All verdicts below are by hand, by Claude Opus 5.5, at fe90ec8ae. "Input" means a cited row; I checked that the cited statement exists at the locator and says what row 1683 uses.

**(1), L34-41. HOLDS (CITED input).** Row 1145 (1)-(2) L19-32 states exactly I_d(s)/I_1(s) <= exp[-(d-1)/b] with b = 1+6 beta, s <= 6 beta, and ||p-1||_inf <= sum_{d>=2} d^2 e^{-(d-1)m/b}. Row 1145 L17 gives the hypotheses: no plaquette holds two selected links; then the selected links are conditionally independent translates of p_s. The Riccati proof of (1) is in row 1145 L24; row 1146 checked it. The factor-out step for C e^{-m/b} at m/b >= 1 is correct. Guide: the bound ratio stays below 1 on the grid.

**(2), L45-60. HOLDS.** Privacy: collinear edges share no plaquette; a plaquette that meets two axes through x contains x, so it uses only the deleted end edges. So m = n-2. Upper bound: a maximal sqrt(s)-separated set has at most 16/s points (disjoint caps of area fraction s/16); at a net point each R_i moves by at most 3 sqrt(s); for a fixed point the Haar chance is 9s/4 (valid since 3 sqrt(s) <= 2 for s <= 1/4); the union gives (16/s)(9s/4)^d = C s^{d-1}. Lower bound: conditional on R_1, its axis is fixed and the other d-1 rotations are independent; each event has chance s/[4(d-1)]. The density sandwich [2^{-d}, (3/2)^d] follows from epsilon <= 1/2. The moment endpoint q < d-1 follows. The slope argument for beta_k = O(k) on the full tail is correct (a bad infinite set would contradict the subsequence statement applied to it). The "dimension test" here only counts spatial directions; see item 5.

**(3)-(4), L68-81. HOLDS (CITED inputs).** Row 1141 (3) L60-68 bounds the pushforward density of Ad(q)n by M_b = 4(1+6b) times area, which gives (3). Row 1283 (2)-(3) give the two-plaquette probability C b v and the box form (C_1 r^2 + C_2/v) Q_B. The 1683 numbering (4) is row 1283 (3).

**(5), L87-113. HOLDS.** I checked: the Perron argument; the stationary path density on slices -1..t+1, so the measured slices 0 and t are interior; conditional independence of the two readings for t >= 2 (no time plaquette meets both); |j - p p| = |Cov| <= eta^2 since each conditional density lies within eta of 1; kernel bound (eta/(1-eta))^2 for the centred compressed operator; the partition argument for the trace of a positive operator with bounded kernel; restriction to the gauge-invariant neutral subspace can only lower the trace. The n^2/4 axis-1 loops with even transverse coordinates have private edges: a (1,j) plaquette holds two parallel edges at transverse offset 1, so one has an odd coordinate.

**Paired flip, L117. HOLDS.** If sigma is the flip, E[W_p | H] = E[W_p o sigma | H] = -E[W_p | H], so E[W_p | H] = 0 and Omega W_p is a nonzero neutral vector orthogonal to all measured functions. **Detour remark, L119. HOLDS** (AB(A'B)^{-1} = A A'^{-1}).

**(6)-(8), L123-170. HOLDS.** Pivots: top edges of squares at (3i,0) share no plaquette with each other and lie in no handle; the translated pattern is in a different parallel plane, and its links are fixed by the conditioning, so a shared plaquette with a pivot does not break the single-link tilt. Column step: |R c^ - z^| <= 2h/|c| <= 2 sqrt3 h. Net: (1+2/sqrt v)^9 points, displacement <= 3 sqrt v, so (7) is C_J b^J v^{J-9/2}; with (1+delta)(J-9/2) >= J the choice v = a z b^{-(1+delta)} gives z/16. Box step: |h_x - h_y| is at most the transported difference, since the pair action is orthogonal in Frobenius norm. Failure of half the tests: 2^{M_B}(z/16)^{M_B/2} = 2^{-M_B} z^{M_B/2}. R ~ (log n)^{1/3} pays the n^3 boxes and n^3 shifts. I did not re-derive the constant 6R^2 of the scalar box Poincare inequality; it is row 1141's, checked by row 1142. (8): dimension < 9 n^6, good-event trace <= 9 n^6 e^{-cu/B'_n} with u = n/512 and B'_n = O(log n); bad event <= 9 n^{6-p}. The r = 0 scalar branch is exact (R I R^* = I).

**(9), L186-200. HOLDS.** Laplace expansion along the y column: each cofactor is the (d-1)-volume of projected rows, at most V by maximality (w is itself a row). So V|w.z| <= V sqrt(d v) and ||B_i z||^2 <= d^2 v. The rule z_S depends only on the prescribed rows; conditioning on at most d-1 blocks leaves J-d+1 independent blocks. The low-rank case gives zero outputs. The count sum_{j<d} C(Jd, j) is right.

**(10) and the 8-dimensional contact fiber, L202-215. HOLDS.** Skew part: displacement norm sqrt2 |Ra - a|, axis length >= 1/2. Symmetric traceless part: lambda_max - lambda_min >= 1/sqrt6 because one eigenvalue has modulus >= 1/sqrt6 and the trace is zero; one end gap is >= 1/(2 sqrt6); (S - lambda)Rw = (S - RSR^*)Rw. With K = Cb, d = 9 or 8, J = 10, (9) gives exponent J-d+1 >= 2, so a small fixed a gives z/16. Since conjugation preserves the identity line, Delta^(0) = Delta_scalar (+) Delta_traceless, which gives the lower bound 0 in (10).

**Model failure, L217. HOLDS.** For |k_i| <= n/(10 pi sqrt u), u lambda <= 0.12. The count is c (n/sqrt u)^3 = c n^{3/2}. Z_{2u} <= Z_u. As the file says, this is internal to the heat model and decides nothing about the Wilson purity.

**(11), L221-255. HOLDS.** I re-derived the partition identity. With normalized indicators of C x B_j, the cell contribution is (1/mu_C) E[1_{E_C} sum_j f_j g_j / p_j]; since the three lists sum to one, sum f g / p - 1 = sum (f-p)(g-p)/p, and |f_j - p_j| <= (h-a) m_j, p_j >= a m_j give D = (h-a)^2/a. S is fixed by the conditioning because it reads only unselected links. Nesting gives the lower bound 1. The R-ratio bounds follow at u and 2u. Caveat (not an error; the file says it): for a partial observation R_F is not a purity, because the compression does not commute with A^u.

**(12)-(14), L259-286. HOLDS.** The set {sum x_i = 0 mod m} is the union of m^2 cubic lattices of spacing m, so the segments tile each line. Twelve classes (direction, two transverse parities) have no two links in one plaquette. Per class D = O((N eps_m)^2). (13): Pi' E Pi' <= e^H Pi' P_0 A^u Pi' with Pi' = Pi - |Omega><Omega|, and the cross terms vanish because Omega is an eigenvector. (14): eps_{m-1} <= C e^{-(log n)^2}. Reconstruction W V^{-1} = U_{x,i} is exact.

**(15), L288-297. HOLDS (method of row 1215 (29)).** The iterated class integration gives the whole-list bridge density in [(1-eps)^N, (1+eps)^N], hence within delta_n of 1 ((1+eps)^N + (1-eps)^N >= 2). |B(X,Y)| <= delta_n nu(|f|) A^2(X,Y) and ||A^2|| = 1 give ||B|| <= delta_n nu(|f|); A^{-1} E_rho has norm <= 1/rho.

**(16), L299-312. HOLDS as stated.** First bound: on D^c more than K/2 plaquettes have 1 - w_p > 3/(8 sqrt beta), since 1 - C_p = (4/3)(1-w_p)(1+w_p) <= (8/3)(1 - w_p); the sum is > 3K/(16 sqrt beta); row 1155 L420 gives the twisted unnormalized moment bound, and sum_b Z_b/Z_0 >= 1 gives the factor 8 C_0^K; Markov gives e^{-cK sqrt beta} for large beta. Second bound: every fine link of a tested plaquette uses its own whole word and its own suffix, so under fully independent Haar readings the K plaquettes are independent Haar; the Haar SU(2) chance of 1 - C_p <= v is C v^{3/2} (guide constant 0.2757); the union gives 2^K (C beta^{-3/4})^{K/2}; the density of Q_t is <= (1+delta_n)^{4m} -> 1. Binary entropy: p log(p/q) + (1-p) log((1-p)/(1-q)) >= p log(1/q) - log 2. All correct. What (16) means is item 2.

**(17), L314-322. HOLDS.** Tr rho_D^2 = Tr(P_0 J A^u J A^u)/[Tr(P_0 J A^u)]^2 by J^2 = J, cyclicity and [J, P_0] = 0. Dividing by the purity gives P_{2u}(D at 0 and u)/P_u(D)^2, with P_t the twist-mixture (neutral) probability. The bounds 1 - 2e^{-cK sqrt beta} and (1 - e^{-cK sqrt beta})^{-2} give 1 + O(e^{-c n^3 sqrt beta}). This is the identity of row 1149 (34) with a different event.

**(18), L324-332. HOLDS.** On D_alpha^c, sum (1 - w_p) >= 3K alpha/(16 beta), so P_t(D_alpha^c) <= 8 (C_0 e^{-3 c_0 alpha/16})^K. Row 1153 (5) gives log Tr A^s ~ (pi^2/15) n^3/s^3 with s = 2 ceil(log(2+beta)) -> infinity along the trajectory, so log Tr P_0 A^t <= log Tr A^s = o(n^3) for t >= s (0 <= A <= I, P_0 commutes with A). Its window s^4 beta^{-1/4} log^{3/2} -> 0 holds since s = O(log beta). The o(n^3) is only n^3/(log log n)^3 here, but it is absorbed. The HS bound follows from P_0 A^u >= e^{-H} E.

**§9 U(1) smoothing, L359-360, and g4 spectator, L362. HOLD.** h = (1+kappa)^{-1/2}; 1 - q^(j) >= c h^2; endpoint L^2 norms <= C b^{1/4}; sup error <= C b^{1/2} e^{-c'(m-2)/b}. Spectator factor (1 + a^{2u})/(1 + a^u)^2 -> 1/2 since a^u = e^{-1/(512 n)}. **g6, L364. HOLDS** (Z = Z_F + Z_perp; 1/Z(u)^2 >= 457/625 iff Z(u) <= 25/sqrt457 ~ 1.1695). That sufficient condition is the seed in other words.

**Item 1 verdict: HOLDS.** I found no FAILS and no needed correction in the PROVED steps. Not re-derived here: the inputs themselves (rows 1141, 1145, 1149, 1153, 1155, 1215, 1283), which rely on their own earlier checks.

## Item 2. The central selectivity claim

**Arithmetic of (16): HOLDS** (item 1). **Selectivity claim: FAILS.** The U(1) zero is an artefact of the test. The step is group-blind in substance.

**2a. The comparison does not fix the U(1) model.** L312 says only that all adjoint readings equal the identity for compact U(1). That is true for every action, coupling, aspect and projector, because the adjoint representation of an abelian group is trivial. So the file states no U(1) action, normalisation or projector, and none is needed for its zero. Y4 test 4 asks for exactly these data (cosine Wilson action, matched aspect, weak coupling, the three half-turn cuts).

**2b. Counterexample: a U(1)-appropriate test gives the same estimate (PROVED from the file's own steps, with one input ARGUED).** Take weak 4D compact U(1) with action beta sum_p (1 - cos theta_p), the same box n = l L^k, the same beta_k (any beta -> infinity with beta = O(log n) suffices), and the eight half-turn cuts (or any positive twist mixture). Keep the same 4m lists F_{s,i}, the same K = n^3/4 disjoint direction-12 plaquettes, the same word/suffix reconstruction. Replace the adjoint trace by the fundamental character: D^U = {at least K/2 have 1 - cos theta_p <= beta^{-1/2}}.
- Lists: the file's own §9 L359-360 proves the U(1) private-link bound sup error <= C b^{1/2} e^{-c'(m-2)/b}. With m - 1 >= b (log n)^2 the whole-list density under each bridge is within o(1) of product Haar, so Q_t has density <= 2 relative to independent Haar readings. PROVED there.
- Haar: the reconstructed plaquettes are independent Haar on the circle. P(1 - cos theta <= v) = arccos(1-v)/pi <= C v^{1/2} (guide constant sqrt2/pi). Thus Q_t(D^U) <= 2 * 2^K (C beta^{-1/4})^{K/2} <= e^{-c K log beta}.
- True law: the U(1) form of row 1155 (9), E exp{c beta sum_{p in S}(1 - cos theta_p)} <= C^{|S|}. ARGUED: the row 1155 proof uses three facts, and each holds for U(1). (i) Halving a marked coupling lowers each normalized multiplier, since I_j(x)/I_0(x) increases in x (classical; guide confirms on a grid). (ii) The scalar cost z_{beta/2}/z_beta -> sqrt2 is bounded (guide 1.414). (iii) Schatten-Holder and the twist-seam step use no group structure. Then P_t((D^U)^c) <= e^{-c K sqrt beta}.
- Hence D_KL((1_{D^U})_* P_t || (1_{D^U})_* Q_t) >= c n^3 log beta for weak 4D U(1). The form is the same; only the constant changes (Haar exponent 1/2 for U(1), 3/2 for SU(2), i.e. half the group dimension).

So the "zero information for U(1)" comes from choosing a representation that is trivial for U(1). The content of (16) is: weak-coupling plaquettes are near the identity, Haar plaquettes are not. That holds for every compact group. It is row 1155 (9) plus a Haar small-ball count.

**2c. The separation from independent draws is trivial in both groups (PROVED).** For i >= 1, F_{s,i} keeps the two other directions whole (L277). So its direction-j words (j != i) are the same random variables as the direction-j words of F_{s,0}. Under P_t they coincide almost surely. Under Q_t the lists are independent with bounded densities, so they coincide with probability 0. Thus P_t and Q_t are mutually singular and D_KL(P_t || Q_t) is infinite, for SU(2) and for U(1) alike. The file notes (L310) that its test "does not count exact equalities of duplicated coordinates". The finite bound c n^3 log beta is therefore a property of the chosen test, not a measure of selective dependence.

**2d. Dimension and coupling (ARGUED).** The same proof in a d-dimensional box gives K of order n^{d-1} and the same form, so it reads the spatial volume only. At bounded beta the first bound of (16) fails in both groups, so the strong-coupling comparison separates couplings, not groups.

**Item 2 verdict: FAILS** as a selectivity claim (counterexample 2b; trivial separation 2c). The inequality (16) itself HOLDS.

## Item 3. (16)-(17) and §8: what they give toward the neutral purity

**(16)-(17): HOLD** (item 1). **What they give: nothing toward a lower bound on the purity.**
- (17) and (18) use only P_t(D^c) at the two periods. They never use Q_t or the entropy gain of (16). So the "separation" is not spent anywhere.
- (17) says: compressing the neutral thermal state to the accepted configurations changes its purity by a factor 1 + O(e^{-c n^3 sqrt beta}). The reason is that the accepted set has probability near 1 at both periods. The compressed purity equals the unknown purity up to that factor. No bound on the purity follows.
- The accepted subspace L^2(D) is small in Haar measure but infinite-dimensional, and by (18) it carries all low neutral states up to e^{H - c n^3}. The file says (L322) that "its internal eigenvalue multiplicities still matter". That is the whole problem.
- The same projection identity is row 1149 (34) with a sign event; the same concentration is row 1155 (9). For U(1) the cosine version of (17)-(18) holds by 2b, while the U(1) purity fails. So (17)-(18) cannot carry a gain to (PUR-io).

**§8 relative trace bound (11): HOLDS** (item 1). What it gives: adding long private-line observations to any exterior observation changes the compressed traces and their ratio by a relative 1 + D, with D = O(n^4 e^{-2n/b}) or smaller. This is a smoothing statement: long lines are almost independent of everything else, so they add almost no trace. It survives U(1) (file L357, L359). It does not reach the purity, since the full slice is never one of the allowed (S, H) pairs (paired flips, L257) and R_F for a partial F is not a purity. (13)-(14) bound overlaps of low states with each list, not the number of low states (L275).

**Item 3 verdict: HOLDS** for the mathematics of (16), (17), (11); the contribution to (PUR-io) is zero, as the file's own ARGUED paragraph L334 half-concedes.

## Item 4. On-file matches and what is genuinely new

**File names: HOLD.** FINISH.md at fe90ec8ae: row 1141 = `gap-crux2-astra62.md` (L1223); row 1145 = `gap-solve2-astra62.md` (L1227); row 1273 = `gap-owner-threeaxis-opus.md` (L1355); row 1283 = `gap-solve32-astra62.md` (L1365). The cited contents exist: 1141 (3) L67 (cap density M_b = 4(1+6b)) and its two-plaquette pinning; 1145 (1)-(4) L19-47; 1273 Lemma S L334; 1283 (1)-(5) L29-63 and (11) L137. Also row 1149 = `gap-solve4`, 1153 = `gap-solve6`, 1155 = `gap-solve7`, 1215 = `gap-solve23` (FINISH L1231, 1235, 1237, 1297).

**On file, not new (ARGUED, from the readings above).**
- (1) is row 1145 (2). (3)-(4) are rows 1141 (3) and 1283 (2)-(3). §6 is row 1273 Lemma S and row 1193.
- (5) and (13) are trace forms of row 1145 (4), which already bounds <F Omega, e^{-H} F Omega> and the band overlap for each centred function of straight transports. Going from one vector to the trace over the subspace is a small step.
- (15) is the method of row 1215 (29), applied to the staggered lists.
- (16) first bound is row 1155 (9) with L420. (17) is the identity of row 1149 (34). (18) is row 1155 (9) plus row 1153 (5). The second bound of (16) is an elementary Haar count.

**Genuinely new in the lane (ARGUED; I found no owner by name search of the library for "maximum-volume", "relative trace", "suffix").**
- The maximum-volume minor small-ball lemma (9) and its use in (6)-(10) for the two-end adjoint operator at every separation, with the exact scalar contact branch and the model purity failure.
- The relative partition identity (11): added private-line observations against any gauge- and centre-stable exterior observation, with loss quadratic in the density oscillation.
- The word-and-suffix pair of lists that recovers every fine link with two readings, with (14) summed over all 4m lists.
- The exact inverse-moment endpoints in (2) for two and three spatial periods.
None of these moves (PUR-io); the file says so (L22, L364).

**Item 4 verdict: HOLDS** for the matches; the novelty list above corrects the file's table only in one place: the row-1683 table (L347) calls (16)-(18) a "new ... quantitative result"; by item 2 its quantitative content is row 1155 (9) plus a Haar count, so it is a new combination, not new information.

## Item 5. The replacement (Y4) filter applied to the adjoint-test estimate (16)-(18)

1. **Box and law. Partly met.** Met: admissible L, calibration, l, n = l L^k, u = n/512, beta_k, periodic links, eight-term electric projection (twist mixture), observable (binary event D on the 4m lists) and its law P_t. Missed: "the part outside the proved weak-scale estimates that the bound covers". D is a plaquette-scale concentration at weak coupling. It covers nothing outside the weak scale.
2. **Sign, size and quantifiers. Partly met.** Met: a signed estimate with reference Q_t, gain c'' n^3 log beta, losses e^{-cK sqrt beta} and e^{-c'K log beta}, absolute constants, all late cutoffs. Missed: no named consumer in whose units the gain is stated.
3. **Use of the gain. Missed.** No inequality spends the gain. (17)-(18) use only P_t(D^c); the entropy gain against Q_t enters nowhere. No term of the budget log(625/457) is paid. No separating example shows information beyond the seed (2b shows the same estimate in a gapless theory).
4. **Group and dimension tests. Missed.**
   - U(1): no action, aspect, coupling or projector stated; the zero is the trivial adjoint; the cosine test with the three half-turn cuts gives the same estimate (2b). Fails.
   - 5D SU(2): the same proof gives K of order n^4 and the same form; the file states (L357) no demonstrated failure. Fails.
   - Strong coupling and 3D abelian: the estimate needs large beta in both groups; in 3D the cosine version holds with K of order n^2. The failure line, where it exists, is coupling, not algebra.
   - **Neutral spectator: fails.** Tensor the Wilson transfer with the file's own two-state spectator (L362). The cuts act trivially on it. All Wilson slice laws are unchanged, so P_t(D), Q_t(D), the entropy gain, the ratio (17) and the bound (18) are unchanged. The purity is multiplied by a factor tending to 1/2. So the gain is unchanged by added low-energy neutral states and cannot bound their contribution. No premise of (16)-(18) detects or excludes the product.

**Item 5 verdict:** meets parts of 1 and 2; misses the weak-scale part of 1, the consumer units of 2, all of 3, and all of 4 including the spectator test.

## Verdict table

| Item | Verdict | Note |
|---|---|---|
| 1. PROVED steps (1)-(18), §7, §8, private links, conditional independence, row 1145 multipliers | HOLDS | no correction needed; inputs rest on their earlier checks |
| 2. Selectivity of the adjoint test | FAILS | U(1) zero is the trivial adjoint; cosine test gives c n^3 log beta for weak 4D U(1); P_t and Q_t are mutually singular in both groups |
| 2'. Inequality (16) as stated | HOLDS | |
| 3. (16)-(17), (11) | HOLDS | they give nothing toward the purity; the gain is never spent |
| 4. File matches 1141, 1145, 1273, 1283 | HOLDS | new: (9), (11), word/suffix reconstruction, (2) endpoints; (16)-(18) a combination of rows 1155, 1149, 1153 |
| 5. Y4 filter | misses 3 and 4 | partly meets 1, 2; fails the U(1), 5D and spectator tests |

(PUR-io) stays open. This check grants no status.

RESULT: Row 1698, Claude Opus 5.5 check of row 1683. Every PROVED step (1)-(18), §7 and §8 HOLDS, with no correction; inputs from rows 1141, 1145, 1149, 1153, 1155, 1215, 1283 match their files. The selectivity claim FAILS: the U(1) zero comes from the adjoint being trivial for abelian groups; the cosine-plaquette test, with the file's own U(1) smoothing, gives the same c n^3 log beta bound for weak 4D U(1); the true and product list laws are mutually singular in both groups anyway. (17)-(18) never spend the gain and give nothing toward the purity. Y4: misses use of gain, group, dimension and spectator tests. New: (9), (11), word/suffix reconstruction. (PUR-io) open.
