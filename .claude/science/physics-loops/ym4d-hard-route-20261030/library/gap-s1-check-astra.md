# Repo search

The lead's `prior/repo-search-2026-11-08.md` was read in full. It covers earlier hard-route targets, not this thin-torus S1. Its `S1-loc` hits concern a constrained inverse, and its W1/W2 hits concern large-field witnesses: these are different objects. Its finite-clock and noncompact Maxwell examples use different measures. No target-specific `prior/gap-s1-check-astra.md` exists. The task row supplies no further “Repo prior work” paths.

I fetched main and PR heads 10114, 10133, 10134, 10141. A targeted search for `twist.eat|twisted thin|gap-s1|gap-twist-chart`, outside this lane, found no matching Markdown or TeX file. Read refs: main `bb4ec020d5ad`; PRs `f76f6c649cff`, `89faef229ff6`, `1e70c7211a2c`, `fb99b4dddc72`, respectively. This is a bounded search, not an absence theorem. The local registry has no row for this check or the thin-torus chart; its bare S1 and chessboard hits concern other obligations.

The actual inputs are already in this lane: `gap-twist-chart.md` (CH, read in full), by Claude Fable 5.2, and the source under check, `gap-s1-opus.md` (A), by Claude Opus 5.5. CH already supplies the rectangular chart and sketches the product-complex extension. This report checks A's extension; it does not claim that method as new.

The outline index (README, matching chunk-03 and chunk-22 rows with neighbours, and obligations) locates existing site-reflection and chessboard proofs. I read Sussman–Alpoge outline lines 2811–2818 and 2885–2943: the integral-of-squares argument and the longest-run proof are already there. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. A's twisted-base application, rather than those general methods, is the check target. No duplicate completed check was found. The CA 4.12–4.19 index has no match for the targeted thin-torus terms; no CA theorem is used.

Provenance: OpenAI/Codex, gpt-6-astra xhigh as dispatched; source commit `df424a7a5f2981c1d464de093e23a1009ab1437b`; research check, not an audit, no status granted. Source line numbers below refer to that commit. Both requested Sussman–Alpoge files were downloaded once at `31a47c543775`, into `/tmp/sa-gap-s1-check-astra.X9srqK/`. No numerical proof, machine enumeration, guide run, or Balaban-paper import is used. Historical numerical reports are not verified or consumed. The output alone is edited.

Completed scope: RP, CB, Z, BAD and its threshold, CH-D first; then BAD-s, TB, GR, FLUX, U1, W1 and W2, including their proposed restatements. Verdicts were appended one at a time. “FAILS” can mean a false statement or an invalid argument; the text distinguishes them. Nothing here proves S1.

## 1. Lemma RP — HOLDS

A:178–197. Every elementary plaquette lies in a closed half for even M >= 4. The shared variables are precisely tangential links on the two site planes. Reflection fixes those variables individually. The twisted fibre plaquettes never cross the cut; their weights remain positive real numbers even though their Wilson coupling has the opposite sign.

Condition on the shared links. The two remaining Haar product spaces are identified by reflection, and the density factors into E times its reflection. Thus the unnormalised form equals the ordinary real L2 inner product of the two conditional integrals. This proves symmetry, positivity and Cauchy–Schwarz, with no gauge-invariance assumption on F or G. The argument also covers direction 4. First failing step: none. This is the site-cut method already present at outline 2811–2818, with the twist checked explicitly here.

## 2. Lemma CB — HOLDS

A:199–226. For even M >= 4, in each coordinate the even translations reach the even cells and the site reflections reach the odd cells, uniquely. Reflected oriented links are inverted as in RP. Shared boundary links are allowed in both half-algebras, so overlapping closed cells do not invalidate the Schwarz step.

For completeness, consider a maximizing normalized filling and a longest cyclic run of identical columns, of length k. Reflect at its right endpoint and retain the half on the left. If k <= M/2, that half contains the run; its mirror joins it to form a run of length 2k. If k > M/2, the retained half is constant and its dissemination is constant in that coordinate. Both reflected fillings are still maximizers: their product is at least the squared maximum, and neither exceeds the maximum. Thus k < M is impossible for the chosen maximizer. Repeating for rows preserves the equality of columns and produces a constant filling, whose normalized value is 1. The finite-label maximum argument requires no power-of-two assumption.

If a disseminated integral vanishes, adding eta > 0 to every profile and taking eta down to zero proves the stated version by bounded convergence. First failing step: none. The run argument is already proved in Sussman–Alpoge outline 2907–2938; this check verifies its two-coordinate closed-cell application and does not claim a new chessboard method.

## 3. Lemma Z — HOLDS

A:228–238. The explicit twist eater V has plaquette z_p, including on the stack. Replacing the four factors one at a time gives rho(U_p,z_p) <= 4r. Since 1-cos(t/2) <= t^2/8, beta A <= 12 n^2 M^2 on the product of radius-r balls, r = beta^(-1/2).

The exact one-link Haar probability is (r-sin r)/(2 pi). For 0 <= r <= 1, Taylor's alternating remainder gives r-sin r >= 19 r^3/120. The rational bound pi < 22/7 < 19/6 gives a probability >= r^3/40. Therefore

    log Z >= -n^2 M^2 [6 log beta + 12 + 4 log 40].

The final constant is valid: e^3 > sum_{j=0}^8 3^j/j! = 806769/40320 > 20, and e^(3/4) > 1+3/4+9/32 > 2. Hence log 40 < 15/4 and 12+4 log 40 < 27. This is hand arithmetic, not a computed bound. Coincident variables at small M do not affect the four-factor distance bound or the labelled plaquette count. First failing step: none.

## 4. Theorem BAD, BAD-b and beta_BAD — HOLDS

A:240–271, for SU(2), n >= 2, even M >= 4. Each chosen defective plaquette is measurable over its closed base cell. Under dissemination the same geometric plaquette can occur at most four times: a fibre face belongs to four cells, a mixed face to two, and a base face to one. Orientation reversal preserves its SU(2) defect. The action on the disseminated event is therefore at least delta M^2/4. Divide its Haar integral by Z, take the M^2-th root, and apply CB. The union over 6n^2 choices at each marked base point gives exactly

    eps = 6n^2 beta^(6n^2) exp(27n^2-beta delta/4).

For disjoint blocks, choose one marked point in each block and sum. There are at most m^k choices, proving BAD-b with (m eps)^k. Connectedness is unnecessary; this does not change the coefficient 1/4 to the earlier requested 1/2.

For the threshold write delta = delta_0 and a=48n^2/delta. CH's constants give 0 < delta_0 < 1. Also log(6n^2) <= 2n^2. It suffices to split beta delta/8 into two equal parts, paying 6n^2 log beta and 29n^2, respectively. At B=4a log(4a),

    B-2a log B = 2a [log(4a)-log log(4a)] > 0.

The left side is increasing for beta > 2a, so beta/2 >= a log beta for beta >= B. Since 4a >= 768 and log 768 > 3, B > 576 n^2/delta > 464 n^2/delta, which pays the constant part. Thus eps <= exp(-beta delta_0/8) at exactly the stated beta_BAD. The asymptotic order n^34 log n follows from CH's fixed absolute C_3,C_4 and delta_0 asymptotic to a constant times n^(-32).

**The group-free rider FAILS** (A:275–277, repeated at 481 and 652). Z uses a zero-action twist eater, not merely small Haar balls. In twisted U(1), the fibre angles satisfy sum |phi_p| >= pi, giving sum_{fibre} d_p >= 2/n^2. Take delta=1/n^4. Every base point then has a defective fibre plaquette, for every configuration. The probability in BAD is 1 for any nonempty S, whereas its claimed eps tends to zero as beta tends to infinity. Thus BAD with the displayed constants and bare defect cannot hold for that U(1) model. Correct text: RP and CB have the stated general symmetry scope; Z and BAD additionally need an admissible zero-action background and the corresponding action and Haar bounds. Untwisted U(1) has such a background; twisted U(1) here does not.

## 5. Theorem CH-D — HOLDS AFTER CORRECTION

A:294–381. Correct the domain to **finite connected D**, as needed for the finite-torus and polymer applications, and in (c'') say **every link l based at b_0 that belongs to both complexes**. Without the latter, take r=0, D={0,e_3}, D'={0}: the balls agree but X' on the link (0,e_3) is undefined. The printed proof imports finite-dimensional contractions; it does not state an infinite-volume extension for arbitrary infinite D in Z^2. No such extension is needed here or claimed by this verdict.

The substantive hole extension holds, with the printed constants. Here is the check against CH's full proof.

1. Grouping the fibre factors gives d=d_F tensor 1 + gamma_F tensor d_K. The mixed terms in its Hodge square cancel because gamma_F anticommutes with d_F and d_F*. Thus Delta=Delta_F tensor 1 + 1 tensor Delta_K. The antiperiodic fibre factor gives mu_n in every degree; the arbitrary base complex contributes a nonnegative form. No simple connectivity or base spectral gap is used.
2. For Delta_0, a path-distance Lipschitz weight changes only base neighbour entries. The real part of the conjugated form loses at most 4 alpha_n^2=mu_n/2. Its inverse kernel and weighted row sum follow exactly as in CH. The graph distance dominates ambient distance; hence the row sum is bounded by n^2 times the full Z^2 exponential sum, also on a torus by choosing nearest lifts. This retains K_n=25n^6 and K'=350n^6.
3. The one-fibre construction and the mixed-plaquette argument supply signs on each available base edge. On each available face their product has distance less than 2 pi from 1, hence is +1. Trivializing e times a prescribed cohomologous representative requires only the definition of H^1. It does not trivialize a nontrivial class. Two admissible fibre gauges differ pointwise by a gauge close to a central sign; the fibre comparison makes that sign constant over each fibre. The edge signs therefore differ by a vertex coboundary. This also proves gauge invariance and compatibility under restriction.
4. Central representatives disappear from both the nonlinear gauge equation and its linearization. The same contraction with G_0 D_0* constructs a transverse field; the fibre argument followed by the same contraction proves uniqueness. Multiplying the chart gauge by a vertex sign changes the representative and leaves X unchanged.
5. The four central factors cancel on every face. CH's BCH error bound and the transverse gap therefore give the same coercivity: |Q| <= sqrt(6) C_4 eps_2 |X| <= sqrt(mu_n)|X|/10, then A >= (47/48)(81/100)mu_n|X|^2/8 >= mu_n|X|^2/16.
6. In a common path ball choose identical rough fibre gauges, so its edge signs agree. The comparison gauge is close to one central sign throughout the connected ball. Cutting its logarithm off at radius r-1 leaves forcing supported outside radius r-2. CH's weighted contraction is unchanged. Its constant is at most 102(25)(2.4)e^(1/2)n^7 < 11000n^7, using e^(1/2)<7/4. Also alpha_n/2 >= 1/(3n). This verifies (c'') without choosing a common global trivialization around holes.

The size constant is valid without using CH's decimal evaluation: 13650 pi sqrt(2) < 13650(22/7)(99/70) = 424710/7 < 61000. Thus C(n)sqrt(delta_0)=eps_2 and every smallness condition above is met. The existence-defined C_3,C_4 are finite analytic derivative bounds, not numerical certificates.

**Corollary CH-T — HOLDS**, on the even base tori under discussion. The flat signs modulo vertex signs give H^1(T^2;Z_2)=Z_2^2. The four classes label four charts, with the same X convention. This is a chart theorem; it supplies neither a Jacobian estimate nor probabilities of the classes.

## 6. Corollary BAD-s — HOLDS

A:489–501, inheriting beta >= 1, n >= 2 and even M >= 4. Substitution gives exactly

    log eps = log(6n^2)-2n^2-kappa <= -kappa.

If delta_1>2 the bad event is empty, so no application of BAD outside its stated delta range is needed. Otherwise BAD applies directly. Put a=24n^2/delta_0. For beta >= 4a log(4a), the calculation in section 4 gives beta/2 >= a log beta. The other threshold gives beta delta_0/2 >= 4kappa+116n^2. Adding yields delta_1 <= delta_0 with the printed beta_SF.

On each finite good component CH-D gives sup |X| <= C(n)sqrt(delta_1) <= eps_2. Since a plaquette has four arguments, |u_p| <= 2C(n)sqrt(delta_1). TB then gives the displayed 8 C_5 C(n)^3 (beta delta_1)^(3/2) beta^(-1/2) remainder per plaquette. It tends to zero for fixed n,kappa. Neither that local error nor the unconditional bad-set bound proves conditional polymer activity estimates. First failing step: none with CH-D's domain corrections.

## 7. Lemma TB — HOLDS

A:390–404. This is a local SU(2) identity once a small chart with flat central representative exists. Put L_p=(D_1X)_p. Four isometric link arguments give |L_p|<=2|u_p| and |Q_p|<=C_4|u_p|^2/2. Thus

    ||Y_p|^2-|L_p|^2| <= (2C_4+C_4^2|u_p|/4)|u_p|^3
                          <= 3C_4|u_p|^3.

CH's eps_2 gives |u_p|<=2eps_2<=1/C_4 and 3|u_p|<=1. Taylor's integral remainder gives |1-cos(t/2)-t^2/8|<=t^4/384 for every real t. Since |Y_p|<=3|u_p|, its remainder is <=|u_p|^3. Hence C_5=3C_4/8+1 works. Summing over faces gives the exact quadratic coefficient beta/8 and the claimed bound on R. No Jacobian or measure approximation is part of this statement. First failing step: none.

## 8. Lemma GR and the transverse covariance — HOLDS AFTER CORRECTION

A:406–425. The rate a_n=sqrt(mu_n/192) and prefactor 2/mu_n survive. The printed conjugation proof does not.

At A:413–417 it treats every coupled pair of link base points as distance at most one. On the three-vertex base D={(-1,0),(0,0),(0,-1)}, the two edges entering (0,0) have base points at path distance two. They share a site and no face, so their off-diagonal Hodge entry is nonzero. Also the assertion “two distinct links share at most one plaquette” fails at n=2: parallel direction-1 links at x_2=0 and x_2=1 belong to both (1,2) faces. Finally the weight selected at A:418 has the wrong sign for the displayed decay bound.

**Replacement proof, preserving the constants.** Use the product splitting already proved in CH-D:

    Delta_1 = (Delta_F,1 tensor 1 + 1 tensor Delta_K,0)
              direct-sum (Delta_F,0 tensor 1 + 1 tensor Delta_K,1).

Fibre terms commute with any base weight. In the first summand, the base vertex Laplacian has at most four neighbour incidences, at distance one. In the second, a base edge has two endpoints, each with at most three other edge incidences, and at most two incident faces, each with three other edges. Thus its off-diagonal absolute row sum, counted with multiplicity before any cancellation, is at most 6+6=12. All those base points are within path distance two. This argument also respects parallel edges at small periods.

For T=e^(a phi) Delta_1 e^(-a phi), symmetrize the real quadratic form. The first block loses at most 4a^2 and the second at most

    12(cosh(2a)-1) <= 48a^2 = mu_n/4,

where 2a<=1. Since the unweighted operator is >=mu_n, Re T>=3mu_n/4. Its inverse norm is at most 4/(3mu_n), hence at most 2/mu_n. Choose phi(b)=+d_D(b,b(l')) (or -d_D(b,b(l))). This gives the claimed decaying kernel. The hand rate comparison is sqrt(192)<14 and sqrt(mu_n)>=2/n, so a_n>=1/(7n).

The covariance identity also holds: on ker D_0*, the precision is (beta/4)Delta_1, and the orthogonal projection is 1-D_0 Delta_0^(-1)D_0*. The relation Delta_1D_0=D_0Delta_0 gives

    Cov_G = (4/beta)[Delta_1^(-1)-D_0 Delta_0^(-2)D_0*].

To justify decay at the *same* rate, not merely assert it after a convolution, put site and link weights at their base points. The weighted norms of D_0 and D_0* are at most 4e^a by their two-entry rows/eight-entry columns. Since a<alpha_n, weighted Delta_0^(-1) has norm <=2/mu_n. Therefore each covariance kernel entry is bounded by

    (4/beta)[2/mu_n+64e^(2a)/mu_n^2] exp(-a d_D(b(l),b(l'))).

This proves the rate uniformly over finite D, with an n-dependent prefactor (uniform for beta>=1). It is a Gaussian result, not an interacting spectral gap.

## 9. Proposition FLUX — HOLDS

A:503–512, with “rectangle R” meaning the filled, contractible rectangle used in CH, rather than a wrapping torus. If H has no bad base point, every point of R is good. The rough fibre construction may be chosen identically on D in the two domains. Thus the sign class on D is the restriction of the sign class on R. The latter is trivial because every flat Z_2 edge cochain on a filled rectangle is a coboundary. Its product on every closed path is +1, contrary to the hypothesis. First failing step: none.

This is a deterministic obstruction to an entirely good filling. It supplies no vortex density, position law, action upper bound or probabilistic boundary-influence estimate. Those are distinct inputs in W1.

## 10. Proposition U1 — HOLDS AFTER CORRECTION

A:441–464. Parts (i), (iii) and the U(1) calculation in (ii) hold. Correct the SU(2) comparison in (ii) to **Hess A^tw(V) >= mu_n/4 >= 1/n^2 on transverse fields**, or explicitly call D_1*D_1 the rescaled Hessian. TB fixes A's quadratic term as |D_1X|^2/8, so its second derivative is D_1*D_1/4. The statement at A:461 with mu_n for the actual Hessian misses this factor four. The Gaussian precision beta K_V/4 in GR is already correctly normalized.

(i) Multiplying all fibre U(1) plaquettes cancels every link. Shifting the stack angle by pi leaves total phi equal to pi modulo 2pi. Thus sum |phi_p| >= pi and sum phi_p^2 >= pi^2/n^2. The inequality 1-cos phi >= 2phi^2/pi^2 gives the printed 2M^2/n^2 lower bound.

(ii) The claimed critical configuration exists without a cohomological existence assumption. Put f=pi/n^2 and, on each fibre, set

    U_2(j,k)=exp(i f j),
    U_1(j,k)=1 for j<n-1,
    U_1(n-1,k)=exp(-i n f k).

Set base links to 1 and use the same fibre at each base point. Its plaquettes are exp(i f), except at the stack where they are -exp(i f); hence every shifted fibre angle is f. The first variation telescopes on each fibre. Hessian weights are cos f>0 on fibre faces and 1 on all other faces.

For X_1(x,b)=h(b), all other components zero, D_0*X=0. Only mixed plaquettes contribute, giving precisely the base Laplacian Rayleigh quotient. A nonconstant Fourier mode gives 4sin^2(pi/M) for M>=2; a constant gives zero. In fact the positive weights make the transverse kernel the harmonic 1-cochains on the four-torus, of dimension four, as stated in A's assembly table. At each nonzero Fourier momentum, dX=0 forces X to be a gradient, and d*X=0 then forces X=0. The four constant components remain. No uniform positive Hessian gap exists for U(1).

(iii) The two SU(2) adjoint holonomies have no common fixed vector, while U(1)'s adjoint action is trivial. This explains the different fibre spectrum. It does not by itself prove or refute the interacting U(1) analogue of S1. No use is made of the unverified power-law claim cited after U1.

## 11. W1 — FAILS as an argument; its proposed obstruction remains open

A:516–525. The first unsupported step is A:520: an asserted action cost is turned into a delocalized vortex-position law and an order-one difference of central marginals. FLUX gives only existence of a bad point. It gives no normalized weights, entropy estimate, lower bound on its probability of lying in the central region, or comparison for boundaries differing at one link. An order-one effect also depends on the size of the observed central region; it does not follow for a fixed local detector from a position spread over a large box.

The later appeal to `gap-ds-gauge.md` Proposition B is not valid. I read its lines 81–95 and 165–191. It bounds a finite-box scale from a *proved covariance correlation length*. A mean spacing of rare defects is not that correlation length: independent Bernoulli plaquette defects can have arbitrarily small density while all separated local defect covariances are zero. Neither vortex-density nor covariance estimates for this SU(2) model are supplied. Moreover the cited W theorem uses four-dimensional cubes with all torus sides >=R+4; a criterion on whole-fibre base blocks needs its own formulation.

Correct replacement: “FLUX warns that some boundary data force defects. Whether this prevents a specified all-boundary finite-box criterion at scale O(n) is open; a quantitative conditional-measure estimate is needed.” W1 cannot justify changing S1's statement or declaring a required exponential box scale.

## 12. W2 — FAILS as an argument for restating S1

A:527–538. The first missing input is A:530: no dilute-vortex representation with the stated perimeter factor, nor a uniform connected detector/loop estimate, has been derived for this measure. The detector is not defined. A law for a Wilson-loop mean does not by itself give a lower bound on its covariance with that detector. The argument would need those estimates uniformly up to exponentially large loop radii.

Its elementary optimization is conditionally right. If the proposed two-sided asymptotics held, put m=c/n and A=m-8a. For A>0,

    max_{r>=0} [Ar-4sigma r^2] = A^2/(16sigma),
    r_* = A/(8sigma).

The support prefactors contribute only logarithmic terms to this comparison. If A<=0, the maximum is 0, not A^2/(16sigma). With sigma of order exp(-k beta), the proposed lower bound for C would indeed be doubly exponential, conditional on all these unproved inputs.

The converse assertion “S1 contains an area law” does not follow even from covariance decay alone. It bounds a centered detector/loop correlation, not the loop mean, and linear-exponential suppression can satisfy that bound without quadratic area suppression. The sigma=0 argument only tests the additional proposed asymptotic formula with 8a<m and a nonzero detector coefficient. It is not a theorem about the Wilson measure. A particular cluster expansion yielding an exponential-in-support prefactor also does not prove that the stronger polynomial prefactor is false.

Correct replacement: “The large-loop covariance bound and the area law are separate open estimates. The dilute-vortex model suggests a potentially large constant if its specified asymptotics can be proved. It does not yet require weakening S1.”

## 13. Proposed restatements and the claimed implication — FAILS as written

A:540–545. The proposed S1-loc is an unproved target. Its hypothesis bounds cardinalities, but its claimed derivation from S1-T uses bounded diameters. These differ for disconnected supports. For example X={(0,0),(2r,2r)} and Y={(0,2r),(2r,0)} each have two base points, are at distance 2r, and have identical projections on both base axes. No coordinate cut separates the two sets. Fibre observables over those points are allowed. Connected supports, or an explicit diameter and separation hypothesis, would repair the stated geometric step; cardinality alone does not prove it. On a torus the cuts must also account for both periodic arcs.

More seriously, **the torus covariance version of S1-T with prefactor 2 and rate c/n independent of beta is false for this very measure**. This can be seen without a vortex approximation.

Fix n and a finite even M. For t in Z/M let

    F_t(U) = (1/2) tr prod_{j=0}^{M-1} U_4(x,t,j),

at one fixed fibre point x. It is a bounded gauge-invariant observable on a single base-direction-3 slice. A centre flip of direction-4 links changes its sign and preserves the measure, so mu(F_t)=0.

On every zero-action configuration, CH-T and coercivity give X=0 and a flat central base field. Thus all parallel loops have the same sign and F_0 F_d=1. The finite configuration space is compact, the action and loop product are continuous, and A>=0. Lemma Z shows concentration on the zero set: for each eta>0,

    mu(A>=eta) <= exp[-beta eta+n^2 M^2(6 log beta+27)] -> 0.

Compactness then gives mu(F_0 F_d)->1 as beta->infinity, for every fixed M and d. Explicitly, outside any neighbourhood on which F_0F_d is close to 1, the continuous action has a strictly positive minimum. Hence Cov(F_0,F_d)->1.

For any proposed c>0 choose an integer d with 2exp(-cd/n)<1/2 and set M=4d. These slice observables are separated by d. For sufficiently large beta their covariance exceeds 3/4, contradicting the proposed bound 2exp(-cd/n). This is a hand counterexample to the claimed equivalent covariance formulation, using only the centre-flip symmetry, Z and the chart's zero set.

It does **not** refute the original S1: that statement permits C(n,beta), which can grow as beta grows. Nor does this calculation alone determine the spectrum of an infinite-time transfer operator at fixed transverse size. A finite-period torus expectation is a trace state, not its vacuum vector state; the asserted equivalence needs separate hypotheses and proof. Site-plane RP also does not by itself prove positivity of a one-step transfer operator: link-plane positivity or an explicit positive kernel construction is needed.

The claim that both replacements supply T3 and T4 is likewise not established here. The actual consumer table (`gap-skeleton-final.md:83–85`, read) names the full covariance target, the separate area-law step, and a cutoff-uniform continuum passage. No uniform bound on the beta-dependent constants or replacement consumer proof is supplied. Keep S1, its large-support scope and the separate transfer/continuum targets open; do not adopt the printed S1-T on the strength of W1 or W2.

## Disposition

The finite SU(2) bad-set bound is usable at the printed beta_BAD. The finite-region chart is usable with the common-link wording; the Gaussian decay rate survives the replacement proof above. The action Hessian is K_V/4, not K_V. The group-free BAD claim must be removed. W1 and W2 do not justify weakening the original S1. PE still names substantial open estimates, and its inclusion of the false torus-covariance version of S1-T requires correction before it can be a proof target. Odd-M BAD, the chart Jacobian, conditional activities, the interacting expansion, large-support S1 and continuum passage were not proved by this check.

RESULT: RP, CB, Z, SU(2) BAD with beta_BAD, BAD-b, BAD-s, TB, FLUX and CH-T HOLD; finite-region CH-D, GR and U1 HOLD AFTER CORRECTION; the twisted-U(1) BAD rider, W1/W2 as arguments for restating S1, and the asserted torus-covariance form/equivalence of S1-T FAIL. S1 remains unproved; this is a check of repository research text, not an audit or a status grant.
