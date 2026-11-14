# Row 904: does the account's fixed-horizon universality give (UNIV-FP)?

Author: Claude Opus 5.5 (high effort), FINISH row 904. Reading and port item.
Clone: /Users/jonreilly/ym4d-lead/clone at 4c53df409a5b061cd32f73708dcb489a5f1e66e4.
Source: Sussman-Alpoge account YM4_1400.tex, revision 2bc0658f91d2 (Ethan Sussman and
Levent Alpoge; text authored with Claude and Codex). Quotes are short phrases; line
numbers refer to that file.

Plan.
1. Read D/library/gap-finishline-opus.md lines 110-160 (first-passage datum, s_*, (SEED-FP))
   and the relevant parts of gap-next3-max.md (attack 2) and gap-mine858-opus.md (row 900).
2. Read the universality statement near YM4_1400.tex line 94031 and its hypotheses.
3. Trace the class of bare weights, the horizon, the constants, the compared objects.
4. Answer (a)-(e), mark READ / ARGUED / OPEN, say what is missing.

## Step 1. The target, as the lane states it (READ)

- (SEED-FP), READ D/library/gap-finishline-opus.md L116-118: there are K_0, a physical size ell
  and s_* < 1/5041 with S_(K,beta)(ell/(2 a_K); (ell/a_K)^3) <= s_* for every first-passage
  datum (K, beta) at g with K >= K_0. It is a statement on the BARE Wilson measure at (K, beta),
  equivalently on the total masses of the account's rho_K (L120, L136). The quantity is a ratio
  of eigenvalues of the bare transfer operator of the periodic cube of physical side ell.
- Uniformity, READ L148: one size and one margin for every first-passage datum with K >= K_0.
- (UNIV-FP), READ D/library/gap-next3-max.md L496 (and L303-305, C2): the universality holds at
  the first-passage horizon with constants uniform in K, covers a mixed weight
  exp(beta_F x_p + centre-blind part) with beta_F small and FIXED (L494: "let only the
  centre-blind coupling run"), and bounds the difference of the seed numbers of two weights by
  less than s_*/2.
- Row 900, READ D/library/gap-mine858-opus.md L45, L134: the flag is the subsection opening at
  YM4_1400 L94031.

## Step 2. The account's subsection (READ YM4_1400.tex L94029-94512)

Layout. It is a layered expansion file, "background/regular_trajectory_stability.tex"
(L94029 BEGIN, L94512 END), titled "Universality for bounded ultraviolet profiles at a fixed
horizon" (L94030), label rts:section.

- Scope sentence, L94033-94039: one finite horizon, one family of regular maps, one frozen
  cutoff presentation; the ultraviolet irrelevant profile ranges over a bounded ball; retuning
  the bare coupling to the same infrared value makes the final profiles exponentially close;
  "it does not compare different horizons or construct an infinite-horizon flow" (L94038-39).
- The ball, L94045-94057: B_0 = "the same gauge-invariant, hypercubic-covariant, normalized
  complete pointings, with zero first jet and zero companion curvature coefficient"; "An input
  with a nonzero marginal coefficient is not part of the irrelevant ball considered here"
  (L94056-57). Radius R_uv fixed; estimates on ||h_0|| <= R_uv.
- Constants, L94066-94068: "may depend on this fixed ball and on the fixed rates, but not on
  depth, horizon or compatible volume".
- Frozen frame, L94070-94080: a_j = X_0 + sum_{l >= j} b_l, theta_j = a_j, a_N = X_0; "every
  cutoff, fluctuation scaling, gauge normalization and map stays fixed when h_0 or the endpoint
  is varied" (L94079-80).
- Recursion, L94111-94114: x_{j+1} = x_j - b_j - r_j(x_j, h_j), h_{j+1} = T_j h_j + n_j +
  f_j(x_j, h_j), with |r_j| + ||f_j|| <= C e_j etc. (L94120-94124), e_j = (log a_j)^m / a_j.
- Proposition rts-bounded-UV-tuning (L94131-94146), proved L94147-94184: for each R_uv a floor
  X_0 independent of N; a unique trajectory with h_0 = H, x_N = X_0 + zeta, ||H|| < R_uv + 2,
  |zeta| < c X_0, holomorphic, ||h_j|| <= H_*.
- Proposition rts-exponential-universality (L94368-94386), proof L94387-94402: for H, H~ in the
  smaller ball, same endpoint, horizon and frozen presentation,
  |x_j(H) - x_j(H~)| <= C e_j q_2^j ||H - H~||, ||h_j(H) - h_j(H~)|| <= C q_2^j ||H - H~||;
  ||D_H x_0|| <= C e_0, ||D_H h_N|| <= C q_2^N; constants "independent of the horizon and
  compatible volume" (L94384-85).
- Finite-volume law, L94457-94510: with a fixed final coarse volume V,
  sup_V |H_N^H(V) - H_N^H~(V)| <= C V q_2^N ||H - H~|| (L94466-94469); "Scalar vacuum factors
  may differ and do not affect a normalized final law" (L94474-75). The compared laws are
  dP_H = Z_H^{-1} e^{-X S_N(V) + H_N^H(V)} 1_D(V) dnu(V) (L94485-94488), D a fixed common real
  domain "inside the working ball", nu a fixed finite measure (L94478-94483). Then
  TV(P_H, P_H~) <= min{1, exp(C V q_2^N ||H - H~||) - 1} (L94500-94504). Its own limits,
  L94505-94509: "It is not uniform over growing volumes, and it proves neither clustering nor
  consistency between horizons. No complementary-history measure has been introduced in this
  comparison."

## Step 3. Context lines that fix the class and the scope (READ)

- What "regular" excludes. HRT section opening, L93441-93446: the integral operations are "the
  homogeneous regular steps on the literal buffered domains"; "The large-field complementary
  operations are not included in the trajectory constructed here." HRT (Prop. hrt-regular-
  trajectory, L93864-93890) solves h_0 = 0, x_N = X with constants and floor "independent of N
  and compatible volume"; Prop. rts-bounded-UV-tuning replaces h_0 = 0 by h_0 = H (L94138).
- The profile norm. L59546-59556 (Prop. lcf input norm): h_z(B) is a sum of local analytic
  pieces, "B = i^{-1} log V is in old coarse units", norm ||h||_{r,kappa} with a FIXED radius r
  (L59544, and L93452-53 "the same field radius r and carrier rate at every scale"); companion
  (curvature) coefficient zero (L59561-62). The profile enters the weight additively:
  e^{-X S_N(V) + H_N^H(V)} (L94485-86); it is not multiplied by the coupling.
- Where the large-field small factor comes from. L4592: failed-test fields "do form a small set
  for the Wilson weight, since e^{-x_j A} <= e^{-c x_j eps_j^2} = e^{-c p_0(g_j)^2}". L61905:
  regularity means plaquettes within eps_k eta_k^2 of 1, eps_k = g_k p_0(g_k); "For a failed
  plaquette test this weight is the Wilson weight." L4214: T_k(Z)1 "carries no small factor";
  the first source of the small factor is "the Wilson weight: near a failed plaquette test of
  step j, x_j A >= c p_0(g_j)^2". L61932: each component keeps e^{-c p_0(g_k) - kappa_1 |C|_k},
  and kappa_1 "outweighs the number C^n of connected sets".
- Where the subsection is used. grep of prop:rts / rts: labels outside L94029-94512: only the
  construction map L3471-3474 ("allow a bounded irrelevant initial profile and estimate its
  effect after retuning to the same endpoint") and the proof index L136275-76, L136536-39
  ("retune the same finite regular problem"). No other proposition cites it. The next sentence
  of the map, L3477-3478: "Changing a plaquette weight is a different derivative." (it refers to
  the weighted background, not to a bare action).

## Step 4. Answers (a)-(e)

**(a) The statement (READ L94368-94386 with L94031-94080, L94131-94146, L94457-94510).**
Hypotheses: one finite horizon N, one frozen presentation (frame a_j, cutoffs, fluctuation
scaling, gauge normalization and maps fixed, L94070-94080), the homogeneous REGULAR steps only.
Bare weight: Wilson at bare inverse coupling x_0 plus an initial profile h_0 = H in the ball
||H||_{B_0} <= R_uv (R_uv fixed), H a gauge-invariant, hypercubic-covariant local analytic
family on the fixed raw bond-angle ball of radius r, normalized at the flat field, with zero
first jet and zero curvature (marginal) coefficient. The infrared endpoint x_N = X_0 + zeta is
held fixed and the bare coupling x_0(H) is retuned. Constants: depend on R_uv and the rates,
not on depth, horizon or compatible volume (L94066-68, L94384-85); the floor X_0 depends on
R_uv (L94132-34). Compared: the coupling sequences, |x_j(H) - x_j(H~)| <= C e_j q_2^j ||H - H~||,
and the profiles, ||h_j(H) - h_j(H~)|| <= C q_2^j ||H - H~||; at a fixed final coarse volume V,
the final regular interactions differ by at most C V q_2^N ||H - H~|| in sup norm, and the
NORMALIZED final laws on one fixed common regular domain D with one fixed measure nu are within
TV distance exp(C V q_2^N ||H - H~||) - 1.

**(b) First-passage horizon, K-uniform constants.** READ: the constants and the floor are
independent of the horizon N, so the statement holds for every K with the same constants, and
the retuning at a fixed endpoint matches the first-passage reading (one endpoint, bare coupling
solved for). ARGUED: the endpoint must lie above the R_uv-dependent floor, so the reference
coupling g must be chosen small depending on R_uv; for a fixed R_uv that is a choice, not an
obstruction. So (b) is yes, for the regular trajectory only, with R_uv fixed.

**(c) The mixed weight (ARGUED from the READ lines above).** It is not covered, in either of
two forms.
1. Polynomial form w = beta_F chi_F + beta_A chi_A, beta_F fixed. For U = exp(i theta n.sigma),
   chi_F = 2 cos theta, chi_A = 1 + 2 cos 2 theta. Matching the quadratic term fixes the
   Wilson coupling x_0 = beta_F + 4 beta_A; the remainder is h_0 = beta_A theta^4 + O(beta_A
   theta^6) per plaquette. On the fixed raw ball of radius r its norm is of order x_0 r^4, which
   grows linearly in K along the continuum limit. So H leaves every fixed ball; the floor
   X_0(R_uv) then grows with K and the endpoint cannot stay at first passage. Not covered.
2. Matched form w = beta_F chi_F + (x_0 - beta_F)|chi_F|. The centre-blind part |chi_F| =
   2 |cos theta| is a function of cos 2 theta, and w = x_0 chi_F wherever chi_F > 0, which
   contains every regular plaquette (plaquettes within eps_k of 1, L61905). So h_0 = 0 and the
   regular data of the two weights are IDENTICAL. The statement is then empty for this pair: it
   compares nothing that differs. The two weights differ only where plaquettes are far from 1,
   that is in the complementary (large-field) histories that the statement excludes (L93444-46,
   L94509-10). (Whether this w has a positive transfer operator, (TM), is a separate question I
   did not settle.)
3. For either form the account's large-field mechanism fails at the bare level. Its small
   factor for a failed plaquette test is the Wilson weight, x_j A >= c p_0(g_j)^2 (L4214,
   L4592, L61905). With beta_F fixed a plaquette at -1 costs only e^{-4 beta_F} relative to the
   identity (chi_A(-1) = chi_A(1), and for form 2 |chi_F|(-1) = |chi_F|(1)): an order-one
   factor, not e^{-c p_0(g_0)^2}. So thin centre vortices are not rare, and the label sum
   (kappa_1 against C^n, L61932) has no reason to converge. That is the design aim of attack 2
   (cheap vortices) and it is exactly the hypothesis the account's large-field ledger uses. The
   account is not stated, and as written does not run, for such a bare weight.
Class allowed (READ): Wilson plus an irrelevant analytic profile of bounded raw norm, on the
regular domain only. A centre-blind part with small beta_F does not fit, because its whole
effect is outside that domain and it removes the Wilson large-field suppression.

**(d) The seed numbers (ARGUED).** No. The statement gives: closeness of couplings and regular
profiles (decaying like q_2^j), and a TV bound on normalized final regular laws on ONE fixed
volume and ONE fixed common domain. What S(N; (2N)^3) needs, and what is not there:
1. the full bare measure: the complementary histories are not included ("No
   complementary-history measure has been introduced", L94509-10);
2. unnormalized partition functions on two tori (Lemma Z' consumes Phi_rho, a combination of
   log Z on T_ell and T_{L ell}, READ finishline L127-129): "Scalar vacuum factors may differ"
   (L94474) and are not compared; the finite-period parts stay in the profiles (L94098), so
   they do not cancel exactly in Phi_rho;
3. eigenvalue ratios of the bare transfer operator, which are not functions of one normalized
   block-field law on one volume; the TV bound "is not uniform over growing volumes" (L94505).
And there is a structural obstruction for the intended pair. By row 898's own premise (MULTIPLET,
READ gap-next3-max.md L311), the mixed weight's slice transfer operator has a quasi-degenerate
multiplet of eight vacua; then its plain seed number S is close to 7, not below 1/5041. If the
Wilson seed holds (S <= s_*), the two seed numbers differ by about 7, far above s_*/2. So
(UNIV-FP) in the form "difference below s_*/2" is false for this pair if the multiplet picture
is right (ARGUED; it rests on row 898's unchecked MULTIPLET reading, not on the account). The
flux half is a large-field (thin-vortex) quantity at fixed physical size; a weight chosen to
make it cheap changes it by order one, and a universality bound that saw it would have to say so.

**(e) Status (READ).** Both propositions are stated with proofs in place (L94147-94184,
L94387-94402; "This proves the nonlinear difference bounds, not only stability of a formal
linear recurrence", L94399-94401), and the proof index lists them under "Bounded initial
irrelevant profiles" (L136536-38). The account's own scope words: it "does not compare
different horizons or construct an infinite-horizon flow" (L94038-39); the TV bound "proves
neither clustering nor consistency between horizons" (L94506-07). So: proved in the account
for what it states, which is a finite-horizon statement on the regular trajectory; it is not a
sketch, and it is not a statement about bare measures. (I did not check the proofs line by
line; the constants chain through Prop. lcf-buffered-formation and HRT, which I read only at
their statements, L60548-60580 and L93864-93890.)

## Marks

- READ: the statement, its hypotheses, constants and scope (L94031-94510); the regular-only
  scope of HRT (L93441-46); the raw profile norm (L59546-62); the Wilson-weight source of the
  large-field small factor (L4214, L4592, L61905, L61932); the citation map (L3471-78,
  L136275-76, L136536-39).
- ARGUED: (b) yes for the regular trajectory with R_uv fixed and g below the floor; (c) the
  polynomial mixed weight is outside every K-uniform ball (h_0 of raw norm ~ x_0 r^4); the
  matched weight has h_0 = 0, so the statement is empty for it; both remove the Wilson
  large-field suppression on which the account's complementary ledger rests; (d) no seed-number
  bound, and on row 898's multiplet premise the two seed numbers differ by about 7.
- OPEN: a universality theorem for bare weights that differ on large fields (centre vortices),
  at fixed physical size and uniform in K, for full (unnormalized, multi-torus) partition
  functions; the account's construction run for a mixed bare weight; (TM) for the matched
  weight.

## What is missing for (UNIV-FP)

Three things, none in the account: (1) a comparison of the FULL bare measures, complementary
histories included, for two bare weights that differ on large fields; (2) its form for
unnormalized partition functions on T_ell and T_{L ell} (or for transfer-operator eigenvalue
ratios), to an absolute accuracy below s_*/2 (or below ~0.13 L in Phi_L), uniform in K; (3) a
large-field ledger for a weight whose plaquettes at -1 are not suppressed by x_0. Even then (d)
would fail for the plain seed if the eight-vacuum multiplet is real; the lane would need the
seed in a multiplet form for the mixed weight and a separate argument that its continuum limit
is the account's SU(2) theory (the SO(3)-versus-SU(2) question of row 898 C3, OPEN).

RESULT: row 904 (Claude Opus 5.5 high, unchecked): (UNIV-FP) does NOT follow from the account. READ YM4_1400 L94031-94510 (Ethan Sussman and Levent Alpoge, text with Claude and Codex): Prop. rts-exponential-universality (L94368-86, proved in place) compares two bare weights Wilson+h_0, h_0 in a FIXED ball of irrelevant analytic profiles on the raw regular ball (L59546-62), at one frozen endpoint after retuning x_0; constants independent of the horizon and volume (so K-uniform, (b) yes for the regular part), giving coupling/profile differences ~q_2^j and a TV bound exp(C V q_2^N ||H-H~||)-1 on NORMALIZED final regular laws on one fixed volume; it excludes the large-field complementary histories (L93444-46, L94509-10), does not compare vacuum factors (L94474), and "is not uniform over growing volumes" (L94505). (c) ARGUED: a fixed-beta_F mixed weight is not covered: the polynomial form has h_0 ~ beta_A theta^4 of raw norm ~x_0, unbounded in K; the matched form beta_F chi_F+(x_0-beta_F)|chi_F| has h_0=0, so the theorem is empty for it; both drop the Wilson large-field small factor the account's ledger uses (L4214, L4592, L61905). (d) No bound on seed numbers; on row 898's own multiplet premise the mixed weight's plain seed is ~7, so a difference below s_*/2 is false for that pair. Missing: a full-measure, unnormalized multi-torus comparison for weights differing on large fields, uniform in K, plus a large-field ledger without x_0 suppression of vortices. Attack 2's stop condition ("stop all if the port says no") applies.
