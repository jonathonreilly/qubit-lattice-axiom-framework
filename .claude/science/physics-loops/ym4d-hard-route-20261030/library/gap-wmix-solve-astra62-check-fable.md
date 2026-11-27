# Check of library/gap-wmix-solve-astra62.md (row 1601) -- FINISH.md row 1606

Checker: Claude Fable 5.2 (subagent of the lead session), 2026-11-27. Line-by-line check; no audit.
Status: COMPLETE (2026-11-27). Verdict: all proofs HOLD; outcome (d) not upheld as progress (non-selective; the wall term is the target restated).

## 0. What was read (primary text, not RESULT lines)

- FINISH.md rows 1601 (brief and RESULT), 1606, 1211, 1351, 1510, in full.
- `library/gap-wmix-solve-astra62.md`, all 267 lines.
- `library/gap-seed-solve-fable.md` sections 3.1, 3.2, 4.1 to 4.3: the kernel, (F1)-(F4), Proposition PC, Lemma REV, (FL).
- `library/gap-k2-tool-design-fable.md` section 3.2: the definition of Q2 (side 2, corner bases, 384 contours, M_c, K_kappa).
- `library/gap-blockstep4-astra62.md`: the conditional temporal step, (17) with its proof, (21) with its three proof paragraphs.
- Not read, as instructed: `library/gap-wmix-wall-astra62.md`, `library/gap-wmix-transverse-astra62.md`, any `library/gap-wmix-*check*` file.

First reading, before the line-by-line record: every displayed estimate (2)-(17) looks correct as mathematics. The open question is what they are worth. Sections 1-3 give the line-by-line record, section 4 the selectivity, section 5 the prior-work search.

## 1. The rows it relies on

| Input | Where read | State | Use in the file |
|---|---|---|---|
| Q2 kernel and posterior | row 1468 file, 3.2; row 1510 file, 3.1 | definitions | The displayed density agrees with them: side 2, corner bases, 384 contours, K = prod exp(kappa <M_c, V_c>)/Zc(kappa abs(M_c)). Zc is a Haar probability integral, so 1 <= Zc(t) <= e^t. The file's weaker bound e^(-kappa) <= Z <= e^kappa is true. The score S = kappa proj M_c is the S_c of Lemma REV. |
| (FL), Lemma REV (H2) | row 1510 file, 4.1, 4.2 | (FL) open; REV checked as a conditional implication by row 1513 | Display (1) of the file is (H2) plus the mean decay of (FL), faithfully. |
| Row 1351 (17) | row 1351 file, "PROVED" before and after (17) | checked line by line by Claude Opus 5.5 max, row 1352, HOLDS | The one-dimensional positive-kernel contraction. The file re-proves the form it needs inside (6) and (13); I checked those proofs on their own. Faithful: both need only "max/min of each transition kernel at most R" and arbitrary positive site weights. |
| Row 1351 (21) | same file | checked, row 1352 | Cited as "carries the finite-memory normalizers". Not used in any step of (5)-(17). |
| Row 1211 | row 1211 RESULT and check 1214 | checked by Claude Opus 5.5 max, HOLDS | Cited as the closest lane hit only. Not used in any step. |

No step of (5)-(17) depends on an unchecked on-file statement.

## 2. Line-by-line verdicts

Notation as in the file. "HOLDS" means I re-derived the step and the stated constants.

**C1. Criterion (2), (3).** HOLDS. pi_i b_i = 0 because F_i is coarser than F_(i-1). nu_V[f b_i] = nu_V[pi_i(f b_i)], norm at most nu_V[(a_i pi_i sum abs(grad f)^2)^(1/2)], then Jensen, and a_i is F_i-measurable. The weighted Cauchy-Schwarz step with sum p_i <= 1 is right. The bound a_i <= C_i pi_i norm(b_i)^2 is Cauchy-Schwarz plus the box Poincare inequality.

**C2. Consequence (4).** HOLDS as a conditional implication. With D_J the torus, h_J is constant; sum over i >= r of A e^(-alpha i)/p_i equals A (1 - e^(-alpha/2))^(-2) e^(-alpha r/2). The hypothesis (4) is not proved for any growing family of boxes in four directions, and the file says so.

**C3. Local constants and the chain form (5).** HOLDS. Contours have at most 10 links with anchors in base + [0,3]^4. Log oscillations: plaquette 2 beta, Q2 factor at most 3 kappa (the file's 4 kappa is safe). A factor meets at most two adjacent time blocks since its time extent is at most 4 sites and blocks have at least 8. H_w counts at most 10 factors per base, at most 23 (2w+9)^3 bases, 12 per factor: a valid loose bound. The density bounds R_w^(-1), R_w for one block given the rest follow.

**C4. (6).** HOLDS. The conditional law of the interval with both ends pinned is an h-transformed Markov chain. Each transition dominates R^(-1) times a law that does not depend on the current state, so total variation contracts by q. The proof gives q^(i+1); the file's q^i is weaker and safe. The case of one outside block that touches both ends is handled correctly (no factor reads three blocks). Averaging over the boundary gives (6).

**C5. (7).** HOLDS. Haar constant: Var f = E abs(f(x) - f(xh))^2 / 2 and the geodesic of length at most pi give pi^2/2 (the sharp constant 1/3 is not needed). Tensorization is Efron-Stein. Replica step: the prefix exchange changes the pair density by the cross ratio of the kernels at the cuts, at most R^2 per cut, two cuts on a circle; then R^2 for the two one-block densities against Haar, R to return the gradient; 1/2 from the two-copy formula; N from the telescoping sum. Total N R^7 pi^2/2.

**C6. (8).** HOLDS. norm(b_0) <= 2 kappa; norm(b_i) <= 8 kappa q^(i-1) from (6); a_i <= (2i+1) R^7 (pi^2/2) 64 kappa^2 q^(2i-2), below the stated A_w kappa^2 (2i+1) q^(2i). The geometric sum and the distance conversion (15(k+1) in time, 3w transverse) are right. The weights are deterministic and supported in U.

**C7. Width that grows with separation.** HOLDS. (1 - e^(-H))^i <= exp(-i e^(-H)); with H_w <= (1/2) log T the stated bound follows.

**C8. (9) and the loop probe.** HOLDS. abs(D) <= 3840. No contour returns to its initial vertex and the terminal vertex is different on sides at least 8, so a gauge rotation at the initial vertex multiplies every contour holonomy on the left and preserves product Haar on D. Left-invariance gives mean zero and second moment (E abs(M)^2 / 4) I (a symmetric matrix that commutes with all left multiplications is scalar). On the event "all links within chord distance 1/20 of 1" each holonomy is within 1/2 of 1, so Re M >= 7/8. Density domination e^(-H_0) and the minimum over t give (9). The total-variance step and "Var S^out <= (1 - delta) Var S" are right. The covariance of the test v.M_c with v.S^in is kappa^(-1) E Var(v.S | W_(U^c)).

**C9. Integrating one eighth of the links; the score identity.** HOLDS. 16^3/32^3 = 1/8; the tubes are 16 apart, the range is 3, so they are conditionally independent. The derivative in V_c of the log marginal density of (Y, V) is nu_V(S_c | Y).

**C10. (10).** HOLDS. Quotient rule; B_(a,u) is bounded by L_0 (beta + 20 kappa); the covariance is zero off the collar; on the collar it equals the covariance of B with h_i - h_*, and (6) applies.

**C11. (11) and the transfer of weights.** HOLDS. The reader B_(a,u) has time span at most 7, so the local-reader form of (8) applies. The total-covariance split and the convolution of two exponentials on a lattice of polynomial growth are right. The file states correctly that this is an equivalence between (FL) for the fine law and the same statement for the exterior law, and that it earns no progress.

**C12. Geometry, (12), (13).** HOLDS. Pinned fraction at most 4L/P by the union bound. Corridors from one chamber leave through different or opposite faces and are more than 3 apart (M >= 40); chambers are L >= 32 apart. So given the chambers, Y and V, the corridor interiors are independent, and the chamber law has one positive pair factor per neighbour pair. The end factors of a corridor read its first or last block, so the same R applies. Cross ratio: A(s,t)/A(s,t') is a conditional mean of a function with values in [1/R, R]; changing s moves it by at most (R - 1/R) q^(n) with n >= floor(L/15) the number of blocks; divide by 1/R. Influence of one neighbour at most eta/2 <= eta in total variation. Eight neighbours give 8 eta = 1/4.

**C13. (14).** HOLDS. delta_u(P_v g) <= delta_u g + eta B_uv delta_v g; the Poisson semigroup bound exp[-t(I - eta B)]; P_v is an orthogonal projection, so the derivative of rho(F T_t g) is a sum of rho[((I - P_v)F)((I - P_v) T_t g)]; the one-chamber Poincare constant is (pi^2/2) e^(2H) by comparison with Haar; path expansion of the inverse.

**C14. The lift and (15).** HOLDS. The gradient of F = E[f | z, Y, V] at a chamber link is the mean gradient plus a covariance with a bounded corridor force; the incident corridors have O(L) links and a Poincare constant that depends on L only. Distances: at most 8P(d + 3). Prefactor exp(O(P^4)) from e^(2H), rate log 4 / (8P).
Precision 1 (not an error): the set E is centred on c. (15) is a statement for one c with E = E(c). No single E is shown to serve all c; a score that reads a corridor or a wall is not covered by (14). Lemma REV needs (H2) for every c in one posterior. The tiling of C9 (one eighth integrated) is the only simultaneous version in the file.

**C15. Simultaneous limit.** HOLDS. P about r^(1/6): prefactor exp(O(r^(2/3))), decay exp(-c r^(5/6)).

**C16. (16).** HOLDS. Standard disagreement bound: with a maximal coupling at each heat-bath update, the vector of disagreement probabilities obeys p' <= [(1 - 1/N')I + eta B_int/N'] p + (eta/N') B_(int,shell) 1; the fixed point is (I - eta B_int)^(-1) eta B_(int,shell) 1; walks from v_0 to the shell have at least k steps and at most 8^j choices. The chamber law given Y, V is a nearest-neighbour Markov field on the chamber grid, so the interior given the shell is the measure used.

**C17. (17).** HOLDS. Given (Y_0, shell chambers, V) the interior chambers and their corridors are independent of all other links (every factor that meets them reads only these). So L(z_(v_0) | y_0, b) is a mixture over shell values of laws in a family of TV diameter d_k. Couple the two laws of Y_0 maximally; on equal values the distance is at most d_k, else at most 1. The inequality holds for every pair (b, b'), hence in the mean.

**C18. Size of the pinned set.** HOLDS for large r. 8P(k+3) <= r/2; abs(Y_0) = O_L(r^3 (log r)^2); d_k <= exp[-c (log r)^2] with any c < (log 4)/16.
Precision 2 (not an error): "large r" means r >= 64 P with P > L, and L is fixed by (12) with R = R_4 = exp(H_4), H_4 = 12 * 10 * 23 * 17^3 = 13,559,880. So L, and the first r at which the bound says anything, exceed 10^(5,800,000) lattice units; m_w in (8) is below 10^(-5,800,000). (FL) asks only for some C and m, so this is allowed. It is not a statement at any size the calibrated tori reach at a finite cutoff of practical meaning, and it is not uniform in beta: R grows like exp(const * beta).

**C19. Gaussian comparison (18).** HOLDS. The constant vector has eigenvalue m_N^2, so Cov(f, s) = 1. Given the pins, the free covariance is the killed-walk series; every free site reaches a pinned site within 8P + 8 steps (two coordinates in gaps suffice, since a corridor has exactly one). Row sums decay as stated; the conditional part of the covariance is at most s_0 8^(s_0)/(8 N^4); with P of order sqrt(log N) the pinned fraction tends to 0 and Cov(f, E[s | Y]) tends to 1.

**C20. Bounded separated readings.** HOLDS. G(0,0) <= 1 + 5/4 (zero mode 1; shells of at most 80 h^3 modes with eigenvalue at least 16 h^2/N^2); some z at distance at least N/8 has G(0,z) >= 1/2; Cov(sin, sin) = e^(-G(0,0)) sinh G(0,z); the conditional covariance is at most abs(G_D(0,z)) because the derivative in the cross covariance is E[cos cos], of modulus at most 1.

**C21. Three-bit example.** HOLDS. Core distance 0; wall distance (1 - 2p)^2/2.

**C22. Scope paragraph.** HOLDS. See section 4, where I confirm it and make it sharper.

**Header claims** ("Result and consumer", "PROVED below"). Each sentence is a correct summary of C3-C18. The ARGUED paragraph claims no proof; its remark that pinned links keep whole plaquettes is right (a plaquette inside one gap slab, away from a corridor, has all four links pinned).

Count: 22 proved items, 22 HOLD, 0 corrections to a proof, 0 FAILS, 2 precisions.

## 3. What the proved statements are worth: three remarks, each proved here

The proofs hold. The question of the brief is whether they move (W-mix). These remarks decide it. Each is elementary; none is claimed as new mathematics.

**Remark T (the headline of (8), (9) in three lines; PROVED).** Let D be the support of S_c (at most 3840 links) and S' = S - nu_V(S | W_(D^c)). Then for every smooth f on the torus, every V, every torus:

    norm(Cov_(nu_V)(f, S'))^2 <= kappa^2 (pi^2/2) e^(2 H_0) sum over e in D of nu_V abs(grad_e f)^2,    Var(v.S') >= delta kappa^2.

Proof. Cov(f, S') = nu_V[Cov(f, S | W_(D^c))]. Conditional Cauchy-Schwarz with abs(S) <= kappa. The conditional law on D has density between e^(-H_0) and e^(H_0) against product Haar, so its Poincare constant is at most (pi^2/2) e^(2 H_0) (C5 and C8). Jensen. The variance bound is (9). QED
So "a component of the score with a volume-independent positive share of the variance obeys (FL)'s gradient estimate with deterministic weights" needs no tube and no chain. It is the remark of row 1510 4.1 ("(H2) always holds with gamma_cl = kappa^2 u_l") applied to a conditional law on a bounded set. (8) enlarges D to a tube and (15) to chambers with corridors. Neither says anything about the part that is left, nu_V(S | Y). (FL) is a statement about S, so it is a statement about that part.

**Remark M (closed walls do better than (15)-(17); PROVED).** Take the file's chambers with gaps of length 4 and no corridors: pin every link anchored at a site that has a coordinate in a gap. The pinned fraction is at most 16/P. No factor reads two chambers (range 3). So, given the pins and V, the chambers are independent, for every model of range at most 3, bounded or not, at every coupling. Consequences, with Y_0 the pinned links read by the factors that meet the chamber of c:
- the analogue of (15) holds with weights (pi^2/2) e^(2H) kappa^2 on the chamber of c and zero elsewhere (same prefactor exp(O(P^4)) as (15), bounded support instead of a tail);
- the first term of (17) is exactly 0: L(z_(v_0) | y_0, b) = L(z_(v_0) | y_0), so d_TV(L(z | b), L(z | b')) <= d_TV(L(Y_0 | b), L(Y_0 | b'));
- with P = floor(r/8) the pinned fraction is O(1/r) and abs(Y_0) = O(r^3), for every r >= 400, with no astronomical constant.
This is the Markov property and the data-processing inequality. It beats the file's "size of the pinned set" paragraph in every number: O(1/r) against O((log r)^2/r), error 0 against exp[-c (log r)^2], abs(Y_0) = O(r^3) against O(r^3 (log r)^2), all r against r above 10^(5,800,000). What the corridors add is one property: the free set is connected and winds. No estimate in the file, and no consumer named in the file or found on file by my search (section 5), reads that property.

**Remark DP (the wall term contains the target; PROVED).** For every measurable g, d_TV(L(g(Y_0) | b), L(g(Y_0) | b')) <= d_TV(L(Y_0 | b), L(Y_0 | b')). Y_0 contains whole pinned plaquettes in the wall next to the chamber of c (a Q2 factor whose base is within one site of a chamber face reads chamber links and all four links of a plaquette in the gap slab), at distance at most 4P = o(r) from c, hence at distance at least r(1 - o(1)) from the data B. So a bound on the second term of (17) is, in particular, a two-sample bound in law for a one-plaquette test at separation r(1 - o(1)), in the same posterior, and in addition a joint total-variation bound for O(r^3 (log r)^2) links out to radius r/2, where the separation from B is only about r/2. The second term is therefore not a remainder. It is the estimate (W-mix) itself, asked for a larger family of tests at a shorter separation, in a stronger metric. The file's own three-bit example (C21) shows that the wall term can be large when the core term is zero, so (17) can lose everything.

**A model inside the stated scope where the left side of (17) is of order one (CITED for one input, not rebuilt).** The nearest-neighbour O(4) model on the four-dimensional torus has spins in S^3, a bounded smooth interaction of range 1 and coordination number 8. So (5)-(17) hold for it at every beta, with a local reader in place of S (the file allows "any vector reader of norm L"). At large beta it has long-range order (Froehlich, Simon and Spencer 1976, the averaged form: the mean over x of E<s_0, s_x> is bounded below uniformly in the volume). Then, as in C20, the two-sample distance of the reader is bounded below at separation N/8, while d_k tends to 0. All of it sits in the wall term. The file's Gaussian comparison (C19, C20; proved there and checked here) shows the same thing without a citation. This input is not load-bearing for my verdict; Remarks M and DP are.

## 4. Selectivity

**(a) Is the scope paragraph right?** Yes. The inputs used in (5)-(17) are exactly four: (i) every local factor is positive with a bounded log oscillation; (ii) finite range; (iii) compact spins with a one-spin Poincare inequality against Haar; (iv) for (9) only, invariance of product Haar under one vertex rotation. No step reads the group beyond (iii) and (iv), the dimension beyond the neighbour count, or the size of beta beyond the value of R.

**(b) Weak 4D compact U(1) and 5D SU(2).** The component holds for both, as the file says.
- 4D compact U(1) with the same block map: (i)-(iv) hold at every fixed beta; R = exp(const * beta). So (8), (9), (15), (16), (17) hold in the massless Coulomb phase at every fixed coupling. They are not uniform as beta grows, for U(1) or for SU(2).
- 5D SU(2): ten chamber neighbours; a longer corridor gives eta <= 1/40; the tube and chamber counts change. Nothing else changes.
- The gapped twin beta < 2/9: holds.
- More than that (Remark M and the O(4) model): statements of this kind hold in models with long-range order. They are blind to mixing, not only to the group and the dimension.

**(c) Does the wall-law term carry the whole difficulty?** Yes, and more than the whole. By Remark M the inequality (17) is the Markov property with a leak term added; it is true in every finite-range model, so it has no content about mixing. By Remark DP the wall term contains the one-test two-sample estimate at essentially the same separation, plus a joint total-variation demand. The file's ARGUED paragraph agrees on the first point ("I have no estimate for these remaining four-dimensional Wilson quantities").

**(d) Does the component move an open input?** No.
- (FL), registry R10: unchanged. R10 asks for (FL) "with a local-to-global theorem". (15) is a local statement at pinned walls. Row 1510 4.3 already names the missing second component as that local-to-global step, and Proposition M of row 1498 says it must contain a uniqueness input. Criterion (4) is such a step stated as a hypothesis; it is not proved, not shown selective, and not shown inequivalent to (FL) (the file says all three).
- (W-mix) in the forms (L3), (CONV), (H-two), (CM_k), (T-mix): unchanged. The wall term fails (WB2) (it is two-sample mixing across the same separation) and (WB3) (no method named); the file says both.
- It is not a first component of a method whose selective step is named. The two "next components" are the wall term (the target, Remark DP) and (4) (a sufficient condition for (FL) with no method). No selective step is named anywhere in the file.

**(e) For the lead, on rows 1608 and 1609 (I have not read their files).** Row 1608 attacks the wall term. By Remark DP that is a row on (W-mix) in a total-variation form for a growing wall, not a reduced problem. Row 1609 attacks (4) for isotropic boxes. The only bound for a_i in the file (C1) is (box Poincare constant) times pi_i norm(b_i)^2, and E norm(b_i)^2 = E norm(h_(i-1))^2 - E norm(h_i)^2 is the in-law influence of the shell at distance i on the score. Through that bound, (4) needs in-law mixing of the score across distance i at a rate that also beats the box constant, for which the file has only exp[C (1+i)^4]. I know no other bound for a_i on file, and I did not prove that (4) implies mixing. Neither row starts from a smaller problem than the one row 1597 paused.

## 5. New or on file

Searches run: FINISH.md and library/ (excluding library/gap-wmix-*) for chamber, corridor, sparse or pinned wall, pinning, Markov property, screening, separating set, conditional independence, decorated, subdivided, dilute, local-to-global, thin tube, quasi-one-dimensional. Read: the corridor passages of eight gap files, row 1375 (8), row 895 (Lemma MC, Proposition FIB), row 1498 2.3, row 1510 4.1-4.3, registry R10.

- Not on file as written statements: (8), (9), (10), (11), (15), (16), (17) for the Q2 posterior, and the chamber-and-corridor geometry. "Chamber" has one unrelated hit (library/ot.md). The nearest corridor passage is row 1353 (library/gap-mini-neutral-step-fable.md 3.3): corridors of width w between parts of a tiling, with the corridor partition function as a mark; a different object, not proved there.
- On file, the parts: the one-dimensional contraction is row 1351 (17), checked by row 1352. The single-site Dobrushin comparison is used in rows 1566 and 1568. The trivial local form of (H2) is the remark after Lemma REV in row 1510 4.1. The split "local at boundary values, then local-to-global" and the statement that the second half needs a uniqueness input are row 1510 4.3 with Proposition M of row 1498. Row 895 (Lemma MC, Proposition FIB) reads averaged block conditions: "either the worst case (finite blocks) or the claim itself (slabs)"; criterion (4) is an averaged block condition and (17)'s wall term is the slab case of that sentence.
- So the component is new as text and not new in content: Markov property, row 1351 (17), a Dobrushin comparison, and a density comparison with Haar.

## 6. Method of this check, and what it is not

Line-by-line reading by Claude Fable 5.2 (one reader, one pass). No Lean. One floating-point guide run outside the repository (random positive kernels on 2 or 3 states, 400 trials: the cross ratio of (13), the total-variation contraction of (6), and a discrete form of (7) never exceeded their bounds; largest ratios 0.9995, 0.53, 0.11). A guide is not a proof step and this run is not a verification record. The file under check has hand proofs only; under the owner's rule of 2026-11-13 it cannot land as a proof note without a compute or Lean record. Given section 4, I see no reason to spend one on it.
Not checked: the outline line numbers cited in "Result and consumer"; the ON FILE summaries of rows 1118, 1120, 1121, 1122, 1304, 1308, 1321, 1388, 1565, 1573, 1584 (none enters a proof step); the author's repo search.

RESULT: Row 1606 (Claude Fable 5.2, laptop subagent; cross-provider check of gpt-6.2-astra row 1601; line-by-line, one reader, no Lean, one float guide run outside the repo; grants no status).
Proofs: 22 PROVED items, 22 HOLD, 0 corrections, 0 FAILS. (2)-(4), (5), (6), (7), (8), (9), (10), (11), (12)-(13), (14), (15), (16), (17), the pinned-set count, (18) and the two examples all HOLD. Two precisions: (15) uses a pinned set E centred on c, so it is not simultaneous in c; "large r" means r above 10^(5,800,000) (R_4 = exp(13,559,880)).
Scope paragraph: right. The component holds at every fixed coupling for weak 4D compact U(1) (not uniformly in beta) and for 5D SU(2), and also in models with long-range order (4D O(4), cited; the file's Gaussian (18), proved). It is not selective.
Worth: Remark M (proved here): closed pinned walls of density O(1/r) give the first term of (17) equal to 0 for every finite-range model; (16)-(17) are the Markov property with a leak added, and (8)-(9) follow in three lines from a Haar comparison on the score's support (Remark T). Remark DP (proved here): the wall-law term contains the one-test two-sample estimate at separation r(1 - o(1)) plus a joint TV demand on O(r^3 (log r)^2) links. The wall term is the whole difficulty; it is (W-mix) restated in a stronger form.
New or on file: new as text; in content it is the Markov property, row 1351 (17), a Dobrushin comparison (rows 1566, 1568) and the remark of row 1510 4.1.
Verdict on outcome (d): NOT UPHELD as progress. The statements are true, but no open input moves: (FL)/R10, (W-mix), (PUR-io) unchanged; the file names no selective step and its residual fails (WB2) and (WB3) by its own words. Record as correct, non-selective, no consumer. Rows 1608 and 1609 do not start from a smaller problem.
