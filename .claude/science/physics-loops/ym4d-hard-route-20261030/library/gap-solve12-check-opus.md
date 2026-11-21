# Check of library/gap-solve12-astra62.md (FINISH row 1168)

Status: DONE. Written step by step as the check went; RESULT at the end.

Checker: Claude Opus 5.5 (max effort), laptop subagent. Row 1168 checks
row 1167. Cross-provider: row 1167 was written by Codex. The check is by
hand. Any numeric run is a guide only.

Line numbers refer to `library/gap-solve12-astra62.md` (306 lines plus a
trailing blank line).

## Plan (at most eight steps)

1. Read the setting (`library/gap-council-brief.md`) and the cited prior
   parts: row 1155 (27), row 1157 (8)-(9), row 1161 one-cube test,
   row 1165 (19)-(24), row 720.
2. Check (1) and (2): full-direction deletion and the relative-curvature
   bound.
3. Check (3): the six-face count on the winding line, the error count and
   the error exponent; the range claim (slope 1/6).
4. Check (4), (5) and the winding-product slope 1/6.
5. Check the directional count lemma, (6)-(8) and the sheet recovery.
6. Check (9), the consumer, (10) and the threshold 8/25.
7. Check (11)-(21) and the comparison laws, with (17) and (20) first.
8. Verdict table, counts and the RESULT line.

## Step log

### Step 1. Setting and cited sources (done)

- Read in full: `library/gap-solve12-astra62.md` (L1-L306), `library/gap-council-brief.md`.
- Read the cited parts: row 1155 (`library/gap-solve7-astra62.md`) (9) at L130-L134, (27)-(35)
  at L386-L528, the slope note at L74; row 1157 (`library/gap-solve8-astra62.md`) (7)-(9) at
  L119-L165 and (19)-(20) at L314-L336; row 1161 (`library/gap-solve9-astra62.md`) (3)-(4) at
  L46-L63, (8)-(12) at L111-L167 and the explicit K = 512 test at L213-L227; row 1165
  (`library/gap-solve11-astra62.md`) (19)-(24) at L281-L376; Lemma E' in
  `library/gap-crux-restate.md` L213-L219; the seed threshold 1/1650 in `library/gap-phys-seed.md`
  L55, L263.
- Status of the inputs. Row 1155 was checked by row 1156 (HOLDS). Row 1157 by row 1160 (HOLDS).
  Row 1161 by row 1162 (HOLDS AFTER CORRECTION, credit only; range 4 | n, n >= 2^70). Row 1165 by
  row 1166 (HOLDS AFTER CORRECTION, constants only, in (25); (19)-(24) HOLD). Row 1167 L5 says it
  treats row 1165 as unchecked. It is now checked. Nothing in row 1167 depends on the corrected
  part (25) of row 1165.
- All local link targets of row 1167 exist (`prior/repo-search-2026-11-08.md`,
  `prior/gap-crux-prior-ym.md`, `../parts/gap.md`, and the eight library files).

Notation used below. h = h_beta = e^{-beta}/z_beta. q(s) is the one-link lift error of row 1157
(8): c sqrt(1+s) e^{-s} <= q(s) <= C sqrt(1+s) e^{-s}, q nonincreasing. kappa = lim or liminf of
beta/log n, as each statement says. The conditional one-loop slope is 11/(3 pi^2) = 0.3715.

### Step 2. The inputs (1) and (2) (done)

**S1. (1), full deletion in one direction (L13-L17, proof L20). HOLDS.**
- Take the common direction as time. A face containing it is an electric face. It is one
  (spatial link, layer) pair. Setting its coupling to zero replaces K_beta = z_beta C_beta by
  K_0 = C_0 on that link and layer.
- C_beta has eigenvalue a_j(beta)/(d_j a_0(beta)) in [0, 1] on spin j, by the character expansion
  of e^{beta tr g/2} with nonnegative coefficients. C_0 is the projection on constants. So
  0 <= C_0 <= C_beta. Tensor products keep the order. P_G commutes with both electric products,
  and the magnetic sandwich keeps the order. So 0 <= F_i <= F.
- Min-max gives lambda_k(F_i) <= lambda_k(F). Schatten Hoelder gives
  |Tr prod F_i| <= prod ||F_i||_b <= Tr F^b.
- E e^{beta sum_D a_p} = Z_D/Z = z_beta^{-|D|} Tr(prod F_i)/Tr F^b <= z_beta^{-|D|}.
- z_beta >= (2/pi) int_0^rho e^{-1/2} sin^2 theta d theta >= c rho^3 with rho = (1+beta)^{-1/2},
  since beta(1 - cos theta) <= beta rho^2/2 <= 1/2. So h <= C (1+beta)^{3/2} e^{-beta}.
- Also z_beta >= e^{-beta} by Jensen (the mean of cos theta is 0). So h <= 1. This is used
  silently later (h^{d_*} <= h^{|S|/2}).

**S2. L18 (remark). HOLDS.** It agrees with row 1155 L134 (halved couplings, constant cost per
mark, Hoelder over four directions).

**S3. (2) (L22-L27). HOLDS.**
- Each face has exactly two directions. So sum_i d_i(S) = 2|S| and d_* >= |S|/2.
- On a face of B the two traces are opposite, so a_p + a'_p = 2. On {D in B} the exponent
  -beta|D| + (beta/2) sum_D (a_p + a'_p) is zero. Off it the bound is positive.
- Cauchy-Schwarz and (1) for each marginal give e^{-beta|D|} z_beta^{-|D|} = h^{|D|}. No joint
  property of the pair is used beyond equal adjoints on the faces of S.

### Step 3. The fixed-radius sign recovery (3) and its error exponent (done)

**S4. (3) as stated (L31-L37). HOLDS.** The proof is S5-S8. The two error terms are the
large-component event and the event that a small filled component changes the observed winding.

**S5. The six relevant faces (L39-L43). HOLDS.**
- Let c be the filling of one compact component S, so dc = S, and b(y) = sum_{x_1} c_1(x_1, y).
  Summing dc over the n faces (1i) between the lines at y and y + e_i, the transverse i-links
  telescope round the x_1 circle. This gives b(y) + b(y + e_i) = sum_{x_1} S_{1i}(x_1, y).
- The sign changes iff b(y_0) = 1. b vanishes outside the transverse shadow of the buffered box,
  whose widths 2k + 4 are below n and inside the collar. On each of the three transverse lines
  through y_0, going forward and backward from y_0 gives two distinct edges where b changes. The
  six edges have pairwise disjoint strips. Each strip has an odd number of faces of S, all of type
  (1i). So d_1(S) >= 6, and d_*(S) >= max(6, |S|/2).
- Precision (no change needed). The remark at L43 says a six-face bound alone would not give six
  faces sharing a direction. That is true of the bare count. The lemma at L75-L77 (S12-S13) gives
  d_*(S) >= 6 for every nonempty finite closed chain, so the winding line is not needed for the
  exponent 6 itself. The L43 argument is correct and self-contained.

**S6. The error count (L45). HOLDS.**
- The large-component term: at most 3n^3 central spatial roots, C_0^{k_0} rooted connected sets,
  and h^{d_*} <= h^{k_0/2} by (2) and h <= 1. This gives C n^3 (C_0 sqrt h)^{k_0}.
- A changing component of size k has a face within C(k+1) of one of the n links of the line.
  So there are at most C n (k+1)^4 C_0^k candidate sets. Each candidate S is a fixed closed set
  with b_S(y_0) = 1, so S5 gives d_*(S) >= max(6, k/2) deterministically, and (2) applies.
- Sum: the terms k <= 12 are at most a constant times n h^6. For k = 12 + j > 12 the term is
  C n C_0^{12} h^6 (13 + j)^4 (C_0 sqrt h)^j, and the sum over j >= 1 is at most C n h^6 when
  C_0 sqrt h <= 1/2.

**S7. The channel and the coupling (L47). HOLDS.**
- The channel draws the comparison given A_i only, keeps its central slice, and applies the
  direction-1 flat flip when needed to match the observed s_i. Its output is an H-orbit.
- The switch of row 1155 (27) multiplies the original and the i-th comparison by c_i in collar i.
  I rechecked the invariance with two comparisons: on a selected face of collar 1 the weights of
  the original and comparison 1 are exchanged; comparison 2 is unchanged there; the normalisers
  depend on A_1, A_2 only, which are fixed. So the joint law is invariant.
- On the good event the switched original and the comparison differ on the central slice by a
  flat cochain. The switched original has winding sign s_i c_i(gamma). So the channel output is the
  correct H-orbit exactly when c_i(gamma) = +1. The coupling inequality gives (3), with a factor
  two for two collars.

**S8. The range (L49). HOLDS.**
- n h^6 <= C n (1+beta)^9 e^{-6 beta} = C exp(log n + 9 log(1+beta) - 6 beta). This tends to zero
  iff the displayed quantity tends to infinity, and it does when liminf beta/log n > 1/6.
- First term: (C sqrt h)^{k_0} <= n^{-k_0 kappa'/2 + o(1)} with 1/6 < kappa' < kappa. Any fixed
  r with floor(r/10) > 6/kappa' (for example r = 370) makes n^3 times it vanish.
- 11/(3 pi^2) = 0.3715 > 1/6. The flow inputs stay conditional, as the line says.

Step 3 verdict: S4-S8 HOLD. The error exponent of (3) is C n h^6 = n exp(-6 beta + O(log(2+beta))).

### Guide run 1 (numerics, not proof)

Scripts in the scratchpad (pure Python, about 16 MB). For 3000 random compact link cochains a in
Z^4 (1 to 25 clustered links), the first script forms S = da, splits S into components by common
three-cubes, and checks: every component is closed; max_i d_i >= 6 (the L75-L77 lemma); and when
b(y_0) = 1 on some direction-1 line, d_1(S) >= 6 (the L43 count). Result: 6509 components, all
closed, smallest max_i d_i = 6 (elementary cube boundaries), no violation; 1819 winding cases,
smallest d_1 = 6, no violation. A second random family (up to 40 links, 9798 components) produced
no component in the second case of the lemma. A third family (unions of short collinear segments,
19269 components) found 73 components in the second case (all four projections vanish); the
smallest had 16 faces, above the bound 12; no violation of max_i d_i >= 6 or of closedness.

### Step 4. The winding product (4), (5) and the slope 1/6 (done)

**S9. (4) (L53-L58) and its proof (L60). HOLDS.**
- A (1, mu) face has its two 1-links at transverse positions y and y + e_mu. So no face contains
  two links of one straight line. The two lines are at least two time steps apart on both arcs,
  so no face contains links of both.
- Given the fundamental exterior the 2n links are independent with density e^{beta k.v}, |k| <= 6
  (six unit staples). W_gamma is odd under each single flip. The posterior bias of one link sign
  given its adjoint is |tanh(beta k.v)|, whose mean is 1 - 2 q(beta|k|) <= 1 - 2 q(6 beta), since
  q is nonincreasing.
- f is measurable for (all adjoints, exterior). So |E(W f)| <= E |E(W | all adjoints, exterior)|
  = E prod_e (1 - 2 q(beta|k_e|)) <= (1 - 2 q(6 beta))^{2n}, and q(6 beta) >= c sqrt(1+beta) e^{-6 beta}.
  This holds at every beta (the exact product form vanishes at beta = 0).
- L58, "the no-query case of row 1165 (24) with the earlier annealed exponent": correct as a
  comparison. The exact form (1 - 2q(6 beta))^{2n} implies row 1165 (24) at D = 0, because
  E|tanh(s t)| <= tanh s <= exp(-2 e^{-2s}). The displayed form with a small c improves the
  exponent e^{-12 beta} to sqrt(1+beta) e^{-6 beta} only for large beta. Wording only.

**S10. (5) (L62-L67) and its proof (L69). HOLDS.**
- The ribbon R is a cylinder: its boundary is gamma_1 + gamma_2, since the time links at x_1 and
  x_1 + n are identified. For two lifts with equal adjoints on V_R, the ratio of the boundary sign
  products is (-1)^{<B, R>} by Stokes.
- Both conditional draws have the Wilson marginal, so (2) applies to sets of faces of V_R.
- A component meeting R of size >= k_0 is rooted at one of the nt faces of R: the first term.
- A smaller component meeting R lies within distance k_0 + 1 of R, inside V_R, so it is a whole
  closed component. Its filling c_S lies within about 3k + 4 < r of R. <S, R> = <c_S, gamma_1> +
  <c_S, gamma_2>. So odd pairing needs a winding change at one end, and S5-S6 bound this by
  C n h^6 per end.
- Given V_R, the two draws disagree with probability 2p(1-p) >= min(p, 1-p), the error of the more
  likely sign. Averaging gives (5).

**S11. The sharp slope 1/6 (L71). HOLDS.**
- Above 1/6: with t, u - t of order n and r fixed and large, n t (C sqrt h)^{k_0} -> 0 and
  n h^6 -> 0.
- Below 1/6: 2n q(6 beta) >= n^{1 - 6 kappa''} -> infinity for beta <= kappa'' log n,
  kappa'' < 1/6 (also for bounded beta). So sup_f |E(W f)| -> 0 even for the observation of (4),
  which contains V_R. The optimal error is (1 - E|E(W|F)|)/2 -> 1/2.
- The identity E|E(W | V_R)| = 1 - 2 inf_J Pr(J != W) holds for any sign W. At the conditional
  slope 0.3715 > 1/6 the absolute bias given V_R tends to one, so a bound that takes this absolute
  value first cannot be below one by a fixed amount. The remaining sentences are interpretation.

Step 4 verdict: S9-S11 HOLD. The winding-product slope 1/6 is sharp at leading order. The
logarithmic window at kappa = 1/6 is not decided, and L71 does not claim it.

### Step 5. The local rule (6)-(7), the count lemma, (8) and the sheet (done)

**S12. The directional count lemma, first case (L75). HOLDS.** I checked it in the dual picture.
A primal face of type (m, n) is dual to a 2-cell in the two other directions. Projecting the dual
complex along direction i kills the dual cells that contain i (they collapse to edges) and keeps
the others. The kept dual cells are exactly the primal faces that contain i, so the image has at
most d_i(S) cells. The projection is a chain map mod two: a cell of type (i, b) has its two b-edges
mapped to one edge (they cancel) and its i-edges collapsed. So the image is a finite closed 2-chain
in the dual Z^3. In Z^3: project along the third direction of a chosen square; a finite closed
2-chain in Z^2 is zero (each edge has two incident squares); so a parallel square covers the chosen
one. Each of the four edges of the chosen square needs one more incident cell, and a cell other than
the chosen one contains at most one of its edges; the parallel square contains none. So at least
six cells, and d_i(S) >= 6 whenever the i-image is nonzero.

**S13. The second case (L77). HOLDS.**
- If all four images vanish, the (a, b)-cells over one square have a 0-1 height matrix with even
  row sums (projection along c) and even column sums (projection along d). A nonempty such matrix
  has at least four ones.
- At one pair of heights, the extreme (a, b)-square has an a-edge and a b-edge met by no other
  (a, b)-cell at those heights. Closedness at these dual edges forces a cell of type (a, c) or
  (a, d), and one of type (b, c) or (b, d). These two types differ from each other and from (a, b).
- Each type present has at least four cells, so |S| >= 12, and sum_i d_i = 2|S| >= 24 gives
  max_i d_i >= 6. Guide run 1 agrees (smallest second-case component: 16 faces).

**S14. (6)-(7) as stated (L79-L88). HOLDS.**
- The rule uses only the adjoints of the faces at face-graph distance <= 12 from p. It contains
  no beta, no period and no Wilson marginal. A zero trace is a null event.

**S15. Uniqueness of the admitted sign (L90). HOLDS.**
- Two admitted lifts with B_p = 1. If the component of p (within the neighbourhood) has >= 11
  faces, a connected 11-subset through p lies within distance 10. Its direction counts sum to 22,
  so some d_i >= 6 (4 x 5 < 22).
- If it has <= 10 faces, all lie within distance 9, every incident cube has all faces within
  distance 10, and B = da has even parity on each such cube. So the component is closed. With
  periods >= 100 it lifts to a finite closed chain in Z^4, and S12-S13 give six faces of one
  direction.
- On a face of B the deficits are 1 - w and 1 + w, so six faces carry total deficit 12. Both lifts
  cannot have deficit sum < 6 there. So all admitted lifts give one sign.
- Gauge invariance and measurability: as stated. A lifted vertex gauge keeps every w_q, so it maps
  the admitted set onto the admitted set.
- Error: the realized lift is admitted unless some six-set D of one direction has
  sum_D a_q >= 6. Markov and (1) give e^{-6 beta} z_beta^{-6} = h^6 for each of a bounded number of
  six-sets. This gives (6).

**S16. (8) and the sheet (L92-L98). HOLDS.**
- Upper bound on the error for N faces: union bound, C N h^6.
- Lower bound: retain >= cN faces at mutual distance >= 4 (greedy, bounded neighbourhoods), one
  link on each. No face contains two selected links. Given the exterior and the selected adjoints
  the retained signs are independent, so the maximal posterior mass of the retained tuple is the
  product of the single maxima. Its mean is prod (1 - q(beta|k_e|)) <= (1 - q(6 beta))^{cN}. This
  bounds the success of any rule that sees all adjoints.
- At beta/log n -> kappa: C N h^6 = n^{d - 6 kappa + o(1)} and N q(6 beta) = n^{d - 6 kappa + o(1)}.
  So recovery for d < 6 kappa and failure for d > 6 kappa. 22/pi^2 = 2.229, so a two-dimensional
  sheet (d = 2) is recovered on the conditional trajectory and a slice (d = 3) is not.
- One face: q(6 beta) <= Pr(error) <= C (1+beta)^9 e^{-6 beta}. Both are
  exp(-6 beta + O(log(2+beta))). So beta^{-1} log Pr(error) -> -6, uniformly in the rectangles
  with periods >= 100; also for the best rule on the fixed neighbourhood, whose error lies between
  the two bounds.

Step 5 verdict: S12-S16 HOLD. The fixed-radius recovery of a realized plaquette sign holds with
error exp(-6 beta + O(log(2+beta))), optimal in the leading exponent. The sheet recovery holds on
the conditional one-loop trajectory.

### Step 6. The surface sign (9), the consumer and (10) with 8/25 (done)

**S17. (9) (L102-L110). HOLDS.**
- Write U_e = eps_e v~_e. Then s_1 s_2 = s_1^0 s_2^0 prod_{dR} eps_e, and by Stokes on the cylinder R
  this is s_1^0 s_2^0 prod_R (d eps)_p, with (d eps)_p = xi_p xi_p^0. Replacing xi_p by g_p gives
  J_R^0. If g_p = xi_p on R, then J_R^0 = s_1 s_2. The union bound and (6) give C|R| h^6.
- A section change flips s^0 and the xi^0 consistently by the same Stokes identity. g_p is gauge
  invariant. J_R^0 is a function of the adjoints within a fixed radius of R.
- At |R| = O(n^2), C n^2 h^6 = n^{2 - 6 kappa + o(1)} -> 0 when liminf beta/log n > 1/3. The
  conditional slope 0.3715 exceeds 1/3, with a margin 0.038 in kappa.

**S18. The consumer, sufficiency (L112-L126). HOLDS.**
- Without the winding signs, the channels from A_i alone recover the G-orbits with the
  large-component error only. Hellinger contraction under the product channel, d^2 <= 2 TV and the
  marginal TV bound give d_G <= d_adj + sqrt(2 eps) + 2 sqrt(eps).
- The kernel step is row 1165 (19) with H = G, g = 8 (checked in row 1166, S1): (z - m)(1 - z) >= 0
  gives E z^2 <= (1+m) E z - m; the minimum of b/sqrt((1+m) b - m) on [m, 1] is at b = 2m/(1+m) and
  equals 2 sqrt(m)/(1+m); testing C on the unit rank-one product root gives
  ||C||_op >= b - d_G ||C||_HS.
- ||C||_HS^2/||C||_op^2 = Tr(Pi_G F^{2t})/lambda^{2t} = X_G(u), the periodic neutral trace, since
  the vacuum is G-invariant. With m = 8^{-1/2}: 2 sqrt(m)/(1+m) = 0.8786; minus 1/32 gives 0.8473;
  its inverse square is 1.393 < 3/2. (The stated route through m > 1/3 also works:
  sqrt(3)/2 - 1/32 = 0.8348 > sqrt(2/3) = 0.8165.)
- u = 2 floor(n/1024) <= n/512 and u >= 3 for n >= 2048. Row 1161's checked test (4 | n,
  n >= 2^70) then gives S_per(n/2) < 2^{-19} < 1/1650, or seven charged top weights
  (lambda_q/lambda_0)^n >= 1 - 2^{-46}, with X_q(u) <= X_0(u) <= 3/2 by row 1161 (3).
- Second branch, constants rechecked: E(h_q) = 1 - r_q^u <= delta; E(|h_q|) <= E(h_q); the neutral
  gap at time u is >= 1/2; Var|h_q| <= 2 delta; ||h_q - sigma_q||^2 <= 4 delta;
  E(sigma_q)^{1/2} <= sqrt(delta) + 2 sqrt(delta), so E(sigma_q) <= 9 delta <= 10 delta;
  E(sigma_chi sigma_q) <= 20 delta; nonleading eigenvalues in character q + chi are <= 1/2 + delta,
  so the off-line part has squared norm <= 40 delta/(1 - 2 delta) < 41 delta; then
  (2 + sqrt 41) sqrt(delta) = 8.40 sqrt(delta) < 9 sqrt(delta). Eight ordered pairs of top lines,
  products of t-step eigenvalues >= 1 - delta (t <= n/2), X(u) <= 12: correlation
  >= (2/3)(1 - delta)(1 - 81 delta) = 0.6667 > 3/5.
- sigma_chi is H-invariant and odd under the direction-1 flip, so it lives on the H-quotient.
  The channel output flips by the nontrivial coset when only s_i flips, so the pulled-back reading
  is s_i f(A_i) with |f| <= 1. The half-period translation makes the two channels translates, so
  one f serves both ends, as C_1 requires. The correlation changes by at most 2 TV of (3).
- So limsup C_1 < 3/5 excludes the second branch at all fine cutoffs, and the first branch gives
  the strict seed of L9, hence (W). This needs liminf beta/log n > 1/6, as stated.

**S19. The consumer, necessity (L128). HOLDS.** It is row 1165's argument (checked in row 1166,
S6), with f depending on A_i only.
- Lemma E' with a = b/2, b -> n: exponent n/(b/2) = 2D per side, (2D)^3 for three sides.
- b/2 = n/8192 <= u and <= 2d = u - 4r for large n; X decreases in time.
- E|f_1 f_2 - 1| <= sqrt(X(2d)) sqrt(X(2d) - 1) + sqrt(X(2d) - 1); the two factors are
  dependent but Cauchy-Schwarz does not need independence. Normalisation costs |X(u) - 1|.
- Under the product of two stationary segments, the direction-1 flip of one whole segment keeps
  its law (it commutes with the transfer and fixes the neutral vacuum), keeps A_i and flips s_i.
  So every s_i f(A_i) has mean zero there, and C_1 <= 2 TV -> 0. Also d_adj^2 <= 2 TV -> 0.

**S20. (10) and the threshold 8/25 (L130-L139). HOLDS.**
- Given A, the two completions give independent copies of s_1 s_2 with mean b(A). So they differ
  with probability (1 - b^2)/2, and the unconditional rate is (1 - E b^2)/2.
- Replacing both by J_R^0 costs <= 2 C |R| h^6 = o(1) at slope > 1/3 (each completion has the
  Wilson marginal). So p_R = (1 - E b^2)/2 + o(1).
- E[s_1 s_2 f(A_1) f(A_2)] = E[b f f] <= E|b| <= (E b^2)^{1/2}. If liminf p_R > 8/25, then
  limsup E b^2 < 1 - 16/25 = 9/25 and limsup C_1 < 3/5 strictly. With d_adj < 1/32 the consumer
  gives (W).
- Necessity: under the product of the two full collar laws, s_1 is uniform given A_1 and
  independent of (A_2, s_2). So E[s_1 s_2 sgn b] = 0 there, while it equals E|b| under the true
  law. Hence E b^2 <= E|b| <= 2 TV -> 0, p_R -> 1/2 > 8/25, and d_adj -> 0.
- Remark (L139) on row 1158 section 5.2: a pointer to earlier work, not a proof step. The section
  exists (`library/gap-paths-fable.md` L319).

Step 6 verdict: S17-S20 HOLD. The charged test with (9) and the threshold 8/25 is equivalent to
(W) at slope > 1/3, together with d_adj < 1/32, on the stated inputs (row 1155 (27), row 1161's
K = 512 test, Lemma E', row 720).

### Step 7. (11)-(21) and the comparison laws (done)

Positive claims (17) and (20) first.

**S21. (17) as stated (L197-L203). HOLDS.**

**S22. Upper bound in (17) (L205). HOLDS.**
- In collar i the two completions have equal adjoints and Wilson marginals, so (2) and S5-S6
  apply to their relative curvature. On the good event the filled cochain a_i c_i is flat on the
  central slice, so its direction-1 winding is one sign b_i on all n^2 parallel lines.
- The relative winding at line y is b_i c_i(gamma_y). So theta_y differs from b_1 b_2 only if
  c_1(gamma_y) c_2(gamma_y) = -1 or on the large-component event. Per line this is at most
  4 C n h^6 + 2 C n^3 (C sqrt h)^{k_0}.
- r fixed with floor(r/10) kappa/2 > 6 kappa + 2 makes the second term at most the first. Then
  E D_n <= C n^3 h^6 = n^{3 - 6 kappa + o(1)}, and Markov gives the upper bound.

**S23. Lower bound in (17) (L207-L216). HOLDS.**
- Lines with both transverse coordinates even: a (1, mu) face has its 1-links at y and y + e_mu,
  so for mu = 2, 3 not both are selected, and for mu = time the second link is at another time. So
  no face has two selected links.
- The second completion depends on the first only through the collar adjoints, which are fixed by
  the exterior and the selected adjoints. So, given (exterior, selected adjoints, second
  completion), the selected signs are independent with their one-link posteriors.
- theta_y is the product of the n selected signs of line y times a known sign. Its smaller
  posterior probability is v_y = (1 - prod_e a_e)/2 and does not depend on the second path.
- For a fixed common sign b the mismatch indicators are independent Bernoulli(p_y), p_y >= v_y. So
  E e^{-#} <= prod_y (1 - (1 - e^{-1}) v_y). Given the exterior, the v_y are independent with mean
  >= v_* = (1 - (1 - 2 q(6 beta))^n)/2. Chernoff and two signs give Pr(D_n <= d) <=
  2 exp[d - (1 - e^{-1}) M v_*].
- n q(6 beta) = n^{1 - 6 kappa + o(1)} -> 0 (kappa > 1/6), so v_* is of order n q(6 beta) and
  M v_* = n^{3 - 6 kappa + o(1)} -> infinity (kappa < 1/2). Take d = n^{3 - 6 kappa - eps}.

**S24. Obstruction to counting rare flips (L218). HOLDS.**
- Pr(theta_y != b_1 b_2) <= n^{1 - 6 kappa + o(1)} by S22. The majority differs from b_1 b_2 only
  if at least n^2/2 lines do, which has probability <= E#/(n^2/2) = n^{1 - 6 kappa + o(1)}. So the
  majority and one-line mismatch probabilities agree up to o(1).
- At the conditional slope, 3 - 6 kappa = 3 - 22/pi^2 = 0.771, so D_n diverges and is sublinear
  in n, as stated. The last two sentences are interpretation.

**S25. (20) as stated (L266-L270). HOLDS.**

**S26. The tail of incorrect readings (L272-L276). HOLDS.**
- The radius-12 neighbourhoods have bounded overlap degree, so a bounded greedy colouring exists
  on every torus. An incorrect face has a six-face witness of one direction with deficit sum >= 6
  (the realized lift is not admitted). Pigeonhole over colours and four directions gives
  m = floor(c_d n) incorrect centres of one colour and one witness direction.
- Same colour means disjoint neighbourhoods, so the m witnesses are disjoint: 6m distinct faces of
  one direction with total deficit >= 6m. Markov and (1) give h^{6m}.
- Choices: (3 e n^3/m)^m centre sets and C_0^m witness sets. Total C (C' n^3 h^6/m)^m =
  C (C_d n^2 h^6)^m. At slope > 1/3, n^2 h^6 <= n^{-eta} with eta > 0, so the bound is
  exp(-c_d n log n).

**S27. The interface count (L278). HOLDS.**
- For two lifts with equal adjoints, Stokes on the strip between lines y and y + e_j at slice i
  gives s_i(y) s_i(y + e_j) s'_i(y) s'_i(y + e_j) = prod over the strip of xi_p xi'_p. So a change of
  theta across a transverse edge needs a face in one of its two strips (one per slice) where the
  completions differ. Strips of distinct edges are disjoint.
- On such a face the predictor neighbourhood lies in the shared collar (r >= 100 > 13), so both
  completions have the same g_p, and one of them is incorrect. So #changed edges <= the sum of
  the four counts E.
- A colouring of the n-torus with both colours >= n^2/4: if >= n/8 rows are mixed, >= n/4 changes;
  else more than 7n/8 rows are solid, both colours occur among them (one colour alone in the solid
  rows would leave the other <= n^2/8), so every column is mixed and there are >= 2n changes.
- So some slice has E >= n/16. Four applications of S26 give (20).

**S28. Obstruction to a local relaxation argument (L280). HOLDS.**
- p_R = Pr(theta_{y_0} = -1) + o(1) by (9). The filling estimate gives theta_{y_0} = b_1 b_2
  except with probability o(1), and the majority equals b_1 b_2 except with probability o(1)
  (S24). So Pr(majority -1) >= liminf p_R - o(1). Pr(theta_{y_0} = +1) = (1 + E b^2)/2 >= 1/2 gives
  the other majority.
- For a reversible chain with this stationary law moving at most n^2/4 entries, a crossing of
  N_- = n^2/2 has an end with N_- in [n^2/4, 3n^2/4]. The Dirichlet form of the indicator is at
  most twice the probability of (20). Its variance is bounded below. So the gap is
  <= C' exp(-c n log n). This is a conditional obstruction, as stated.

**S29. (11) (L143-L147). HOLDS.**
- The observation sigma(links outside the k links) is mapped to itself by vertex gauges and flat
  flips, so Q commutes with them.
- With the temporal links kept, the joint density of (b, v) given R is a product of one-sided
  factors times exp(beta sum_e v_e . h_e(b)), since each missing link enters only its own last
  electric factor K(.) = e^{-beta} e^{beta v.h}. The four-point log ratio is <= 4 k beta.
- Tilt TV bound: for tau in [1, D], (tau - z)_+ <= (tau - 1)(D - z)/(D - 1) by convexity, so
  TV <= (z - 1)(D - z)/(z(D - 1)), maximal at z = sqrt(D): (sqrt D - 1)/(sqrt D + 1) = tanh(k beta)
  for D = e^{4 k beta}. This is Birkhoff's contraction for a projective diameter 4 k beta.
- The return operator is K K^*, positive, with a bounded kernel, hence Hilbert-Schmidt with bounded
  eigenfunctions. An eigenvalue on centred functions is <= q^2 by the oscillation bound.
- E Var(f(Y) | b, R) >= (1 - q^2) E Var(f(Y) | R), E Var(f(Y) | X) >= E Var(f(Y) | X, temporal, R),
  and E Var(f(Y) | X) = ||f||^2 - ||P f||^2. Since 1 - tanh^2 = sech^2 this is (11).

**S30. (12) (L153-L160). HOLDS.**
- (11) on an eigenvector gives ||Q h||^2 >= 1 - (1 - r^2)/s. With r >= 0 (positive transfer) and
  A_Q(t) = sum r^t ||Q h||^2, the excited states with 1 - r^2 <= s/2 have sum r^t <= 2(A_Q - 1).
  sum x^p <= (sum x)^p for p = T/t >= 1.
- The other states have r <= (1 - s/2)^{1/2} <= e^{-s/4}, so their sum at T is <= e^{-s(T-t)/4} X(t).
- Fibre ratio: varying the k missing links at an end changes the k last electric factors by a
  ratio in [e^{-2 k beta}, e^{2 k beta}], and the eigenfunction equation gives the same for psi/D.
  So p_t varies by at most e^{4 k beta} along the fibre, also after the flip average.
- Tr(Q P^t Q) = Tr(P^t Q) = int pi(dx) E[p_t(x, Y') | R(Y') = R(x)] >= e^{-4 k beta} X(t).

**S31. Consequence for a physical period and (13) (L162-L167). HOLDS.**
- s = sech^2 beta >= e^{-2 beta}. With beta <= kappa'' log n, kappa'' < 1/2, and T - t >= c n,
  e^{4 beta} e^{-s(T-t)/4} <= n^{4 kappa''} exp(-c n^{1 - 2 kappa''}/4) -> 0.
- t = floor(n/2048), T = 2 floor(n/1024): floor(n/1024) >= 2 floor(n/2048), so T/t >= 4. If
  limsup A_Q(t) < 5/4 then [2(A_Q - 1)]^{T/t} < (1/2)^4 = 1/16. T <= n/512, so this is the neutral
  input s(T) <= 1/2 of row 1161's test.
- (13): on the spectral range r >= e^{-E}, <f, (I - P^2) f> <= (1 - e^{-2E}) ||f||^2, so (11) gives
  ||(I - Q) f||^2 <= cosh^2 beta (1 - e^{-2M/n}) ||f||^2 <= e^{2 beta} 2M/n -> 0 for kappa < 1/2.

**S32. (14) (L171-L175). HOLDS.**
- Upper: p(F) = (1 - E b_F^2)/2 decreases as F grows. From the proof of (5),
  p(sigma(V_R)) <= C n t (C sqrt h)^{k_0} + C n h^6. With kappa finite, n h^6 = n^{1 - 6 kappa + o(1)},
  and k_0 > 2(1 + 6 kappa)/kappa makes the first term smaller.
- Lower: sgn b_F is measurable for the observation of (4), so E|b_F| <= (1 - x)^{2n},
  x = c sqrt(1+beta) e^{-6 beta}. Then p(F) >= (1 - E|b_F|)/2 >= c min(1, n x) = n^{1 - 6 kappa + o(1)}.

**S33. (15) and (16) (L177-L189). HOLDS.**
- J_+ needs the adjoints of a fixed neighbourhood of its ribbons. The faces near an end reach
  12 steps into the collar, which the enlargement covers. So J_+ is measurable for A and the open
  + arc. Pr(J_+- != Z) <= 3 C n (u/2) h^6 = O(n^2 h^6).
- Fano with eight values: H(X | Y, A) <= h_2(v) + v log 7 for mismatch probability v <= 1/2. So
  |H(J_+ | A) - H(Z | A)| <= h_2(eps) + eps log 7 and 0 <= H(J_+ | J_-, A) <= h_2(2 eps) + 2 eps log 7.
  This is (15).
- D(L(A, Z) || L(A) x Unif_8) = log 8 - H(Z | A). With (15) this is (16).

**S34. Obstruction to a local adjoint replacement (L191). HOLDS, under (W) as stated.**
- Under (W) the full collar pair is close in TV to the product of its marginals (S19). Under the
  product, the three winding triples are uniform given their own adjoints (three flat flips), so
  their product Z is uniform given A. With Pr(J_+- != Z) <= eps this gives the ideal law, also after
  returning to the true A-marginal.
- H(Z | A) -> log 8 by a coupling of Z with the ideal uniform variable and Fano. Then (15) gives
  I(J_+; J_- | A) -> log 8.

**S35. The TV lower bound 1 - 8^{-1/2} (L193). HOLDS, under (W).**
- If the arcs are conditionally independent given A under the comparison law, the readings given A
  have law p_A x q_A. Its affinity to the uniform diagonal is sum_z sqrt(p_A(z) q_A(z)/8) <= 8^{-1/2}.
  Affinity of the A-marginals is <= 1, TV >= 1 - affinity, and data processing plus the ideal-law
  approximation finish it.
- The glued law gives two independent uniform readings on the same A-marginal. TV between the
  uniform law on 64 pairs and the uniform law on the 8 diagonal pairs is 8 (1/8 - 1/64) = 7/8.

**S36. (18) (L222-L233). HOLDS.**
- An odd product B_{i,S} changes under the direction-1 flip, so it selects the H-coset. The
  switched product differs from the observed one by prod_{y in S} c(gamma_y). So the error adds
  M times the per-line term of S6.
- Second line: c M pairwise nonadjacent lines at both ends; all their 1-links are in distinct
  faces; the product changes under each single flip. Given the exterior, the bias is a product of
  2cMn one-link biases with mean <= (1 - 2 q(6 beta))^{2cMn}. Conditioning on less only lowers
  E|E(. | .)| (Jensen).

**S37. (19) (L235-L241). HOLDS.**
- The global flat flip fixes V and flips s_0 and B_{i,S}, so both are conditionally uniform. For two
  mean-zero signs the joint law given V is (1 + x y m)/4, and the TV to the uniform pair is
  E|m|/2.
- s_0 B_{i,S} = prod over S triangle {y_0}, at least M - 1 lines at one end. The second line of
  (18) at one end bounds E|m|. The last sentence (two products near two independent fair signs
  given the collars) follows from E[B_i | V] = 0 and the second line of (18).

**S38. Scope (L243). HOLDS.** M n h^6 = n^{a + 1 - 6 kappa + o(1)} and M n q(6 beta) =
n^{a + 1 - 6 kappa + o(1)}: reconstruction for 1 + a < 6 kappa, decorrelation and loss of the
reference bit for 1 + a > 6 kappa. The window at equality is left open, as stated.

**S39. The calibration (L246). HOLDS.**
- Two ends, 2Mn individually odd links: the dressed correlation is <= (1 - 2q(6 beta))^{2Mn} = a^2.
- Reference outside S and revealed with the exterior: E[s_0 B_{i,S} f_i] <= a, so 1 - 2 delta_i <= a.
- 1 - 2(delta_1 + delta_2) <= 2a - 1 <= a^2, since (1 - a)^2 >= 0. The binary example has clean
  correlation 1 and observed correlation a^2. All correct; it is a statement about these two
  estimates only.

**S40. The sharp four-point diameter (L250). HOLDS.**
- With identity temporal transporters, h_e = X_e. With v_e = +-1 and X_e = +-1 constant, the
  interaction is +- k beta, and the four-point sum is exactly 4 k beta. The one-sided factors cancel
  in the four-point ratio. Positive-measure neighbourhoods make this the essential diameter.
- The limiting binary channel has weights e^{+-k beta}, ratio e^{2 k beta}, centred eigenvalue
  tanh(k beta). So tanh(k beta) cannot be improved for this class of one-sided weights.
- At the conditional slope, n sech^2(2 beta) <= 4 n e^{-4 beta} = n^{1 - 1.486 + o(1)} -> 0.

**S41. The two spatial wells (L252-L262). HOLDS AFTER CORRECTION (hypothesis only).** The
mathematics of L254-L262 holds. The statement at L252 must carry the slope hypothesis used at
L262 (see the last item).
- Class functions of 16 disjoint plaquette holonomies (no common link or vertex) embed
  isometrically, and they are gauge and flat-flip invariant (a plaquette has 0 or 2 links on any
  flip plane).
- The electric step acts on them as the product of fourfold convolutions: V_e = eta_e U_e with
  iid increments; moving increments past fixed links uses the conjugation invariance of the
  increment law, and inversion symmetry handles orientation.
- The restricted kernel is continuous and strictly positive, so its top eigenfunction is positive.
  It is an eigenfunction of the full positivity-improving transfer, so it is the full top vector.
- As lambda -> infinity, rho_lambda dg -> (delta_+ + delta_-)/2 with cell masses exactly 1/2 by the
  symmetry g -> -g. The kernel converges in Hilbert-Schmidt norm to the two-point kernel
  (1/2)[[a, b], [b, a]], with eigenvalues (a +- b)/2.
- d(1, -1) = pi and the triangle inequality give one angle >= pi/4, so
  w^{*4}(-1) <= e^{-(1 - 2^{-1/2}) beta}. Balls of radius (1+beta)^{-1/2}/4 give
  w^{*4}(1) >= c (1+beta)^{-9/2}. With m = 16: n b/a <= n (C (1+beta)^{9/2})^{16} e^{-4.686 beta} -> 0
  at slope > 1/3.
- Both eigenvectors, also divided by the vacuum, depend only on the block holonomies, so Q fixes
  them, and A_Q(t) >= 1 + (lambda_2/lambda_0)^t >= 2 - o(1) for t <= n.
- (11) and (12) hold for these weights: their proofs use only the electric step, positivity and a
  positive spatial half-weight.
- Correction (L252): add "for liminf_j beta_j/log n > 1/3", the hypothesis of L262. Without it the
  statement is not proved: at bounded beta and a fixed block, (a - b)/(a + b) is a fixed number
  below one and its n-th power tends to zero, so the construction gives no lower bound beyond one.
  With m = 16 any liminf slope above 1/(16(1 - 2^{-1/2})) = 0.2134 suffices; a larger fixed m lowers
  this threshold. The conditional trajectory (0.3715) satisfies the hypothesis, so the use made of
  the example in L296 and L304 is unaffected.

**S42. (21) (L284-L294). HOLDS.**
- K = p_h/sqrt(X(v)) is the square root of the true pair density; B = (E[K^2 | R_1, R_2])^{1/2} is
  the square root of the reconstructed density; C = E[K | R_1, R_2] is the kernel of QKQ.
- Varying both fibres changes K by at most e^{8 k beta}, so C >= e^{-8 k beta} B pointwise.
  ||QKQ||_op = 1/sqrt(X(v)), since Q P^h Q fixes the constant and has norm <= 1. Testing on the unit
  rank-one product root D >= 0 gives X(v)^{-1/2} >= <D, C> >= e^{-8 k beta} H_Q(v).
- ||K - C||^2 <= ||(I - Q) K||^2 + ||K (I - Q)||^2 = 2 ||(I - Q) K||^2 (orthogonal ranges, K symmetric).
  Under the trace, (11) gives ||(I - Q) K||^2 <= cosh^2(k beta) [1 - X(2t + 2)/X(2t)].
  1 - r^2 <= -2 log r and Jensen on r^{-t} give 1 - X(2t+2)/X(2t) <= (2/t) log(X(t)/X(2t)).
- 0 <= C <= B gives ||B - C||^2 <= 1 - ||C||^2 = ||K - C||^2. K - C is orthogonal to the
  R-measurable B - C. So d_rec^2 = ||K - B||^2 <= 2 ||K - C||^2 <= (8 cosh^2(k beta)/t) log(X(t)/X(2t)).

**S43. Its limit as an upper-bound route (L296). HOLDS.**
- d_rec(2t)^2 <= (8 cosh^2 beta/t)(16 beta - 2 log H_Q(t)). The first part is about
  32 beta e^{2 beta}/t -> 0 for kappa < 1/2; the second is o(1) by hypothesis.
- ||K||_op = X(2t)^{-1/2} >= <D, K> >= H_Q(2t) - d_rec(2t). If liminf H_Q(2t) > sqrt(2/3), then
  X(2t) < 3/2 eventually.
- 2t = 4 floor(n/88) <= n/22, so S(n/2) <= S(2t)^{11} < 2^{-11} = 1/2048 < 1/1650.
- Under (W), both affinities tend to one (BC >= 1 - TV), and -log H_Q(t) -> 0 = o(t/cosh^2 beta).

**S44. The comparison laws (L300-L302). HOLDS.**
- W_y = s_{1,y} s_{2,y} = m_{1,y} m_{2,y} b e_{1,y} e_{2,y}. The arc reading m_{1,y} m_{2,y} b errs
  iff e_{1,y} e_{2,y} = -1, with probability 2 delta (1 - delta); the e's are independent of all
  other data.
- One-collar laws: collar 2 carries the sign l b, which is fair and independent of A in both
  laws, since l is fresh. So the one-collar laws coincide. Each raw sign carries its own private
  fair sign m_{i,y}, so all raw signs are independent fair signs. A_1 and A_2 are independent.
- Two completions: theta_y = b b' times four independent signs, so p = [1 - (1 - 2 delta)^4]/2,
  about 4 delta. Mean n^2 p = n^{3 - 6 kappa + o(1)} -> infinity, variance <= mean, so (17) by
  Chebyshev. The event of (20) needs Bin(n^2, p) >= n^2/4: at most 2^{n^2} p^{n^2/4}. Per line,
  p(F) for F generated by A and the readings is of order delta = n^{1 - 6 kappa}, the exponent in (14).
- Readings in two completions: b, b' independent in the first law (disagree with probability 1/2)
  and b = b' = a_1 a_2 in the second (never disagree). The statement is about inference from the
  listed data only, as it says.

**S45. The remaining remarks.** HOLD. L37, L67, L88 (no machine search; finite definitions);
L98 last sentence; L110 last sentence; L117 last two sentences; L175 last sentence; L189;
L203 last two sentences; L218 last two sentences; L243 last sentence; L262 last two sentences;
L296 last three sentences; L302 last three sentences. Each is a scope note or interpretation
consistent with the checked statements.

**Setting, scope and summary lines.**
- **S46. L3 (OPEN, plan).** HOLDS as a plan; it claims nothing.
- **S47. L5 (GUIDE, repo search).** Not re-run. The cited local files exist. The PR and main pins
  were not re-read. GUIDE.
- **S48. L7 and the external link at L49 (GUIDE, the account).** Spot-checked in the lane's local
  copy of the account (line numbers agree; the copy was not verified against revision
  `31a47c543775`). Outline L2313-L2336 is the transfer contraction inequality. Outline L31871-L31882
  gives the measure E e^{-E} dE with Laplace transform (1 + t)^{-2}: polynomial clustering does not
  give a gap. CA-I L2704-L2712 lists "a mass gap" under "Not asserted". CA-I L2643-L2656 gives the
  normalisation g^{-2} = 2N/g_std^2 and the growth 11N/(24 pi^2) of g_std^{-2} per e-fold. With
  N = 2 this is 4 x 22/(24 pi^2) = 11/(3 pi^2) per e-fold for beta, as used at L49. HOLDS as a
  reading. Credits to Balaban, Chatterjee (L7) and Mack-Petkova (L22) are present.
- **S49. L9 (OPEN, setting).** HOLDS. The strict seed 1/1650 at T = n/2 is the r = 2 seed of
  Theorem SH (`library/gap-phys-seed.md` L55, L263), and row 720 gives its equivalence with (W).
- **S50. L304 (OPEN).** HOLDS as a summary. Each listed item is an estimate checked above or a
  stated absence.
- **S51. L306 (RESULT).** HOLDS as a summary of what the file proves. "error
  exp[-6 beta + O(log(2+beta))], optimal in its leading exponent" is S15-S16; "a whole
  two-dimensional sheet on the conditional one-loop trajectory" is S16; "(9) and the threshold
  p_R > 8/25 together with neutral decorrelation" is S17-S20; "sharp leading slope 1/6" is S11;
  (17) and (20) are S21-S27. The OPEN list is accurate. It does not mention the L252 hypothesis
  correction (S41), which does not affect any of these claims.

### Guide run 2 (numerics, not proof)

Script in the scratchpad (pure Python and numpy, about 40 MB, under one second). It checks: on a
grid of s, 1 - 2q(s) <= tanh s <= exp(-2e^{-2s}) (q by quadrature; equality only at s = 0); 20000
random tilts in [1, D] obey the TV bound (sqrt D - 1)/(sqrt D + 1); h_8 = 0.87858,
(h_8 - 1/32)^{-2} = 1.3928 < 3/2; (2/3)(1 - delta)(1 - 81 delta) - 3/5 = 0.0667 at delta = 2^{-46};
2 + sqrt 41 = 8.403 < 9; kappa = 11/(3 pi^2) = 0.37151, 6 kappa = 2.22907, 3 - 6 kappa = 0.77093,
4 kappa = 1.48604; the m = 16 well threshold slope 0.2134; 2^{-11} < 1/1650 and 2^{-19} < 1/1650;
and random two-colourings of the n-torus (n = 8, 12, 16) with both colours >= n^2/4 always have at
least n/4 changed edges. No violation. These runs guide only.

### Step 8. Verdict table and result (done)

| Statement | Lines | Verdict |
|---|---|---|
| S1 (1), full deletion | L13-L20 | HOLDS |
| S2 remark on row 1155 (9) | L18 | HOLDS |
| S3 (2), relative curvature | L22-L27 | HOLDS |
| S4 (3) | L31-L37 | HOLDS |
| S5 six relevant faces | L39-L43 | HOLDS (precision: L75-L77 also gives six) |
| S6 error count | L45 | HOLDS |
| S7 channel and coupling | L47 | HOLDS |
| S8 range | L49 | HOLDS (flow input conditional, as stated) |
| S9 (4) | L53-L60 | HOLDS (wording precision at L58) |
| S10 (5) | L62-L69 | HOLDS |
| S11 sharp slope 1/6 | L71 | HOLDS |
| S12-S13 directional count lemma | L75-L77 | HOLDS |
| S14-S15 (6)-(7) and uniqueness | L79-L90 | HOLDS |
| S16 (8) and the sheet | L92-L98 | HOLDS |
| S17 (9) | L102-L110 | HOLDS |
| S18 consumer, sufficiency | L112-L126 | HOLDS |
| S19 consumer, necessity | L128 | HOLDS |
| S20 (10) and 8/25 | L130-L139 | HOLDS |
| S21-S23 (17) | L197-L216 | HOLDS |
| S24 rare flips | L218 | HOLDS |
| S25-S27 (20) | L266-L278 | HOLDS |
| S28 relaxation obstruction | L280 | HOLDS (conditional, as stated) |
| S29 (11) | L143-L151 | HOLDS |
| S30 (12) | L153-L160 | HOLDS |
| S31 period consequence, (13) | L162-L167 | HOLDS |
| S32 (14) | L171-L175 | HOLDS |
| S33 (15)-(16) | L177-L189 | HOLDS |
| S34 ideal law under (W) | L191 | HOLDS |
| S35 TV bound 1 - 8^{-1/2}, 7/8 | L193 | HOLDS |
| S36 (18) | L222-L233 | HOLDS |
| S37 (19) | L235-L241 | HOLDS |
| S38 scope | L243 | HOLDS |
| S39 calibration | L246 | HOLDS |
| S40 sharp four-point diameter | L250 | HOLDS |
| S41 two spatial wells | L252-L262 | HOLDS AFTER CORRECTION (L252 must state liminf beta/log n > 1/3) |
| S42 (21) | L284-L294 | HOLDS |
| S43 upper-bound route | L296 | HOLDS |
| S44 comparison laws | L300-L302 | HOLDS |
| S45 remaining remarks | listed in S45 | HOLD |
| S46 plan | L3 | HOLDS |
| S47 repo search | L5 | GUIDE (not re-run) |
| S48 account readings | L7, L49 | GUIDE, HOLDS as a reading |
| S49 setting | L9 | HOLDS |
| S50 OPEN | L304 | HOLDS |
| S51 RESULT | L306 | HOLDS as a summary |

Counts: 51 statements. 48 HOLD, 1 HOLDS AFTER CORRECTION (S41, hypothesis only), 2 GUIDE (S47
not re-run; S48 a reading of external text), none FAILS.

Needed correction, exact line:
- L252 (statement of the two spatial wells): add the hypothesis liminf_j beta_j/log n > 1/3,
  which L262 uses. With m = 16 any liminf slope above 0.2134 suffices. Without a slope hypothesis the
  claim is not proved: at bounded beta the construction gives no bound beyond one.

Precisions (no change needed): L43 (the count lemma L75-L77 gives six faces of one direction for
every closed component, so the winding line is not needed for the exponent); L58 (the exact
annealed form implies row 1165 (24) at D = 0; the displayed small-c form improves its exponent only
at large beta).

Not verified here: the account's flow inputs behind the slope 11/(3 pi^2) (conditional, as row 1167
says); the external PR pins of L5; the identity of the local account copy with revision
`31a47c543775`.

RESULT: HOLDS AFTER CORRECTION (hypothesis only) - check of row 1167 (`library/gap-solve12-astra62.md`), checked line by line by hand by Claude Opus 5.5 (max effort) as FINISH row 1168, positive claims first: 51 statements, 48 HOLD, 1 HOLDS AFTER CORRECTION, 2 GUIDE, none FAILS; the fixed-radius adjoint rule (6)-(7) recovers a realized plaquette sign with error exp(-6 beta + O(log(2+beta))), optimal in the leading exponent (directional count lemma L75-L77 checked in both cases), and (3) recovers one winding sign with error C n h^6; the sheet recovery holds for d < 6 kappa, so on the conditional trajectory (6 kappa = 2.229) a two-dimensional sheet is recovered and a slice is not; (9), the consumer and (10) with the threshold 8/25 hold, so at slope > 1/3 (W) is equivalent to limsup d_adj < 1/32 with liminf p_R > 8/25; the winding-product slope 1/6 is sharp at leading order via (4) and (5); (17) and (20) hold; the one correction is at L252, which must state the slope hypothesis liminf beta/log n > 1/3 used at L262 for the two spatial wells; guide runs (pure Python and numpy, under 50 MB) agree and prove nothing; the Wilson bounds d_adj < 1/32 and p_R > 8/25, the neutral upper bound, (W) and the four-dimensional SU(2) mass gap remain OPEN.
