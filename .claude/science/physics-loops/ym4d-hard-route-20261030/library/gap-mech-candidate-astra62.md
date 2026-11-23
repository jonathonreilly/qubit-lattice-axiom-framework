# Repo search

Searched Markdown and TeX on `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9). Terms included M-neutral, N-phys, neutral seed, two-period, order-one band, ZD-c, crosscap, Frobenius–Schur, heat-kernel divisibility, backward heat, high-spin Wilson rectangle, factorial character tail, coarse Wilson factor and deleted coarse plaquette.

| Relevant hit | Statement and relation to this row |
|---|---|
| `origin/main:research/mass-gap/library/gap-phys-seed.md`, Theorem ZD-c, 311–320 | On the stated dyadic grid the periodic seed is equivalent, given its inputs, to a bounded doubling defect together with an unbounded scaled cube gap. This is a consumer of a seed. The companion `prior/gap-prior.md` at 126 requires the same trajectory, matched blocking and common or dense observables to combine routes. |
| `pr/10114` and `pr/10133`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md`, (7), (11) | A rank-one convolution minorant gives the centered fundamental plaquette correlation at one lattice time at least $v_N^2 e^{-68\beta}/(1+v_N/r_f^4)$. This is a positive correlation for a fixed representation. The present test ranges over representations of one blocked loop. The November 8 digest identifies this predecessor in §11. |
| Earlier files in this lane | Row 1330, (1), retains a heat factor on a subprobability and pays a positive error. Row 1169 and row 1367 give the separated-link conditional law and angular upper estimates. The checked fundamental rectangle argument in `gap-solve14-astra62.md`, (4), uses a positive open-line transfer. These steps are reused below. |
| Crosscap search | Drouffe–Zuber's twisted surface contraction and Witten's projective-plane indicator are already documented in `prior/gap-lit-assoc.md`. Row 1127 rules out positive or absolute twist bounds from support groupings resolving a crosscap, with negative mass of order exp(c n⁴) relative to the full partition function on [2.3,2.6]. This candidate was dropped. |

The narrower five-ref queries for a heat factor of a Wilson marginal, a factorial lower tail of a blocked rectangle, and a one-sign remainder after deleting a coarse plaquette term printed no matching statement. The broad target hits in `archive_unlanded/MANIFEST.md` and the `neutral_continuation4/7` files concern neutral currents and spin bands. The 2x2 factorial-design hit concerns gravity and electromagnetism. The row-specific prior file is absent. The bounded searches are a record of the matches examined.

**Result for row 1434.** A positive independent heat time on a coarse square contradicts a factorial lower bound in spin for the actual Wilson loop. For a factor-two block the factorial power is exactly four. The same loop also detects arbitrarily high coefficients of both signs after extracting a positive Wilson plaquette term from the full coarse action. The neutral thermal seed remains open.

## Plan saved at the start

1. Read the row-specific prior, owner rules, indexed source ranges and the existing chain through row 1367. Search the designated repository refs for the statement and the proposed method before deriving it.
2. Write a candidate mechanism and its first lemma from the four-dimensional SU(2) target and the published evidence before opening the later direction rows.
3. Compare that proposal with the excluded directions, both registries of prior work and the exact-block-map test. Retire any equivalent proposal.
4. Prove a surviving first lemma or a precisely scoped class obstruction. Record the trusted base for any exact computation used in a proof and end with two decisive follow-up rows.

Research note for FINISH row 1434, assigned to gpt-6.2-astra max on the laptop. Author only. No status conferred.

## Target and source checkpoint

The checkout is at `45a4ff04184a0f8f7c4ab2cb6fd12080185c08b1`. The supplied source export is identified as `31a47c543775` and has no local Git metadata. In Sussman and Alpoge's outline (with Claude and Codex), `sa-index` chunks 01 and 29 and obligation line 24 point to outline 588–599 and 31871–31882, where a mass gap excludes an interval immediately above the vacuum. Polynomial clustering permits support down to zero. CA-III 108223–108267, Proposition 10.7:prop-clustering-mass-gap, uses a gap as a hypothesis for reflected decay. Bałaban's quoted regular-background estimates in `lit-balaban.md` §0 concern a constrained operator. Jaffe and Witten's target requires a nontrivial theory on four-dimensional Euclidean space with positive physical gap.

Let $s_j(t)$ be the sum of the excited centre-neutral transfer eigenvalue ratios to power $t$. At one admissible physical side $L$, let $n_j=L/a_j$, with $4\mid n_j$ and $n_j\ge 2^{70}$ eventually. Row 1367 asks for $s_j(2w_j)\le4/21$ with $1\le w_j\le\lfloor n_j/1024\rfloor$ at all late cutoffs. Monotonicity permits the largest such time. The specified coupling range is $\beta_0\le\beta_j\le B_0\log(L/a_j)$. One physical cube is tested for each cutoff.

Rows 1356/1359 give the squared optimal rank-one error $s_j(2w_j)/(1+s_j(2w_j))$. At tolerance $2/5$ this supplies the neutral seed at $u_j=\max(3,2w_j)$. Rows 1342/1349 propagate that seed in either flux branch to a neutral physical gap with vanishing thermal excess at each fixed cutoff. Matching (H2), totality (TOT) and the specified continuum data, including (P4) for the vacuum conclusion, yield the gap in the reconstructed space. The periodic test (W) additionally selects eventual finite branch I. The calculation below supplies a class obstruction at the finite Wilson step. [Rank-one check](gap-mini-mneutral-check-astra.md) · [Seed and continuum check](gap-seed-audit-check-astra.md)

## Phase 1. Candidate recorded before opening the rows after 1378

**GUIDE.** Colour rotations from two transverse fluctuations have a commutator in SU(2). For circle-valued rotations the group commutator is the identity for every pair. The mechanism to test is whether accumulated transverse commutators release an independent, isotropic Brownian rotation of positive duration into a coarse link at each blocking step. The proposed source of SU(2) dependence is this group word. Hartman–Watson spherical heat mixtures, as used in row 1330, motivate testing whether such a component can be extracted exactly. The proof would need the finite-step statement below.

Fix the block map first. On a periodic Wilson torus keep the ordered straight products on the edges of the grid of spacing b. Push the full normalized Wilson measure forward and call its density on the coarse links F_b. Sequential straight products give the same map at the product of the block sizes. The proposed first lemma is that F_b is the result of applying independent central heat convolution, of strictly positive time on at least one edge of a nonwrapping coarse face, to some positive residual law. The residual may couple every coarse link. Heat acts on genuine variables of the full marginal. At a coarse fundamental plaquette its density coefficient would acquire the product of the four heat multipliers. For the action coupling fixed by projecting log F_b onto that plaquette, the heat equation for log F also has a quadratic-gradient term. Its sign and the transport to the thermal bound would both have to be proved. No such sign or transport is assumed.

**First falsification test.** Fix a coarse rectangular loop crossing a diffused edge once. A heat factor would give a Gaussian upper bound in the spin of the normalized Wilson-loop character, for every spin. Test this against a factorial lower bound for the same characters of the *interacting four-dimensional periodic law*, keeping the finite box, block size and coupling fixed as spin increases. Failure at arbitrarily small positive time would rule out the whole stated class, including any positive coarse-coupling rate obtained through it. The one-bond Bessel series is already in Sussman–Alpoge GL3 (outline 2195–2231). The finite-period open-line transfer and the reflection argument for fundamental rectangles are already in gap-solve6-astra62 and gap-solve14-astra62, equation (4), after Bachas, Osterwalder–Seiler and Lüscher. Row 1330, equation (1), extracts a heat-smoothed subprobability from a fine temporal link with an explicitly retained positive error. These are inputs and comparison points.

## Phase 2. Comparison with the direction rows

| Rows and checks | Closest statement and decision |
|---|---|
| 1380/1381, 1386/1387 | The soft-move argument bounds the gain by the spread of the move costs. The later check preserves row 1141's positive lower bound for the covariant Laplacian of every adjoint section on typical large boxes, and row 1283's neutral bridge restriction. Neither identifies the distribution of an independent rotation of a retained coarse link. Row 1132's (A) asks for a dominated fraction of the two-slice kernel in Moser coordinates with independent Haar commutators, whose fundamental multiplier is 1/4. It allows an unsmoothed fraction. |
| 1390/1393, 1396/1401 | Bond moving compares traces and partially ordered spectra. Geometric time coarsening changes the temporal coupling. The checks limit both the rigidity claim for changes of grid and the claimed equivalence with STEP. Here the coarse variables are exact straight products of the *original* isotropic Wilson links in every direction. The test is an identity of their joint law. |
| 1402/1407, 1409/1411 | The cover/swap trace and the curvature-descent proposals are distinct. The latter uses a straight-product map too. Its first lemma, preservation of weighted fibre measures up to a scalar by horizontal transport, fails on a regular fibre. Our identity allows arbitrary changes of the conditional fibre law and places a Fourier constraint on the pushforward itself. |
| 1418/1420, 1421/1423, 1424/1426, 1425/1429 | Row 1418 bounds an omitted bare spin tail in Hilbert–Schmidt norm. Row 1421's mismatch on one fused link saves $3c_f^6/32$ per four-spin pattern, with $c_f=2I_2(\beta)/I_1(\beta)$. The single-fundamental two-cycle response vanishes under axis exchange. The ring's tested magnitude increases. A factorial *lower* bound on the full high-spin coefficient answers a different question from the bare tensor tail upper bound. |
| 1430/1431, 1432/1433 | The crossed decrement and ring increment read the same signed moment with different reference coefficients. The Lean replay covers finite arithmetic, with analytic identifications outstanding. The test below uses one fixed map and the full measure. |

**Filter of row 1386 §4.5, with check 1387.** (t1) The commutator is the identity on the circle before a representation is chosen. In SU(2), take a=iσ_z and b=exp(iπσ_x/6) for the Pauli matrices. Then aba⁻¹=b⁻¹ and the commutator b⁻² is noncentral. This establishes a group distinction for the proposed source only. (t2) Commutators are present in five dimensions too. A four-dimensional rate would have to enter in the blocking step. (t3) The source also exists for SU(3), where the rate would need its own derivation. (t4) At fixed lattice the countertest applies at each finite positive coupling, however large. (t5) The first lemma is a distributional assertion on a single block. A fixed positive strong-coupling Wilson comparison below separates it from the seed. The full proposed four-dimensional carry has no demonstrated rate.

**Decision.** Test this candidate for a class obstruction. Its exact-law premise is distinct from row 1330's positive submeasure, from row 1409's weighted horizontal transport, and from the signed response of row 1430. No row in open-registry names the high-spin lower bound or the heat factor of a straight-path marginal. Row 1434 has no additional “Repo prior work” entry.

## Phase 3. All-spin lower bound in the unmodified Wilson measure

**PROVED by hand, author only.** Use the SU(2) representation of highest weight m = 0,1,2,…, dimension d_m=m+1 and normalized character φ_m=χ_m/d_m. Throughout, take finite rectangular periodic lattices with fine periods at least three. In the Wilson measure take any nonwrapping coordinate rectangle C of fine side lengths r,s≥1, strictly shorter than the corresponding periods, with distinct edges on its boundary. At every 0<β<∞,

$$
 W_m(r,s):=\mathbb E_\beta\,\phi_m(U_C)
 \ \ge\ L_m(\beta,rs):=
 \left[e^{-\beta}\frac{(\beta/2)^m}{(m+1)!}\right]^{rs}.                 \tag{1}
$$

The bound is uniform in the other periods. The heat-factor countertests below use even m alone. Those characters are invariant under a change of sign on any link. Representation spin in (1) labels an observable.

**One plaquette.** Use probability Haar and the unshifted Wilson weight w(g)=exp(β χ_1(g)/2). Let C_h denote convolution with a central function h. On one electric bond,

$$
 C_{w\phi_m}\succeq c_m C_1,\qquad
 c_m=\int w\phi_m=2 I_{m+1}(\beta)/\beta
       \ge (\beta/2)^m/(m+1)! .                                      \tag{2}
$$

Here C_1 is the projection onto constants. To see the operator order, expand the exponential in powers of χ_1. Each term times χ_m is the character of a tensor product with a nonnegative coefficient. Convolution by an irreducible character is its Peter–Weyl projection divided by its dimension. The series converges uniformly. The constant mode of C_{wφ_m} is c_m and the remaining spectrum is nonnegative. The formula and the first positive Bessel-series term are GL3 with the scalar factor exp(−β) removed (outline 2195–2231).

Turn one direction of the plaquette p into time. Write M for multiplication by the square root of the spatial Wilson weight within a slice and P for vertex gauge averaging. The ordinary one-step transfer is T=M P(⊗ C_w)P M. Integration of the time bonds inserts P, and cyclic multiplication of the weights M yields the periodic partition function Tr T^k for period k. Replacing the one electric bond kernel by C_h in one step gives the same trace with that plaquette weight replaced by h. This follows directly by inserting h in its two-slice integral. Tensor (2) with the unaffected positive bond convolutions, conjugate by P M, and test with the positive T^{k−1}. The trace of a product of two positive operators here is nonnegative by the square-root factorization. Thus Z W_m(1,1)≥c_m Z_{p,1}, where Z_{p,1} is the partition function with the weight at p set to one. Pointwise w≤exp(β) gives Z_{p,1}≥exp(−β) Z. This proves (1) for one face. Positivity of the convolution was used even though its character-valued kernel may change sign.

**Rectangle.** Use the finite-period open-line transfer of gap-solve14-astra62, (4), checked in gap-solve14-check-opus, S15. In that construction replace its fundamental transporter by D_m(U_γ) on a straight spatial path γ of length s. Matrix-valued slice functions carry the gauge actions at its two endpoints. With matrix inner product tr(A*B)/d_m, multiplication J by this transporter is an isometry from scalar gauge-invariant functions into the endpoint space because D_m is unitary. In the latter space the transfer T_c uses the same M and product convolution, tensored with the matrix identity and restricted by the orthogonal gauge projection for the endpoint actions. It is positive. Inserting the two transporters at time distance r gives Tr(T^{k−r} J* T_c^r J)/Tr(T^k). In the two-slice integral the gauge actions at the endpoint indices supply the two temporal sides. The normalized matrix trace closes the rectangle.

For scalar eigenvalues λ_i>0 and charged eigenvalues ν_l≥0 the weights λ_i^k |J_li|²/Tr T^k sum to one. Include the charged nullspace in the resolution of identity. For 1≤r<k, W_m(r,s) is the r-th moment of ν_l/λ_i under these weights. Scalar null vectors make zero contribution since k−r>0. Jensen gives W_m(r,s)≥W_m(1,s)^r. Turn the other coordinate direction into time to obtain W_m(1,s)≥W_m(1,1)^s. Together with (2) this proves (1) at the stated periods. The use of normalized characters keeps all constants independent of m except for the displayed factorial.

**Neutral ensemble.** Formula (1) also holds for even m in the normalized sum of the eight unnormalized temporal-twist Wilson measures defining Z_+. Here is the additional point needed when the transfer direction changes. Label a twist by three independent bits on planes 0i, with 0 the original time. Use the stack representative which changes a plaquette sign at one fixed value of each of its two coordinates, for every value of the other coordinates. Moving a stack by one layer changes variables by centre signs on links of the intervening sheet. An even-m loop is unchanged. In any chosen transfer direction k, place every stack containing k at the closing seam. Other stacks are constant along k and modify only the positive spatial multiplication M. For fixed values of those other bits, summing the independent seam bits is a positive multiple of the orthogonal projection onto the invariants of their commuting spatial centre flips. This is the reorientation used in gap-solve9-astra62, proof of (3), with zero original magnetic twist. Explicitly, across the seam a stack in the ki-plane translates the slice by −1 on the i-links meeting the corresponding transverse cut, reproducing the signs of the temporal plaquettes in the two-slice kernel.

The projected trace formula is Theorem TW-T (T2), (T4)–(T6) in `gap-transfer-twisted.md`. The projection commutes with M, the bond convolutions and vertex gauge averaging. The isometry J for even m intertwines the flips since centre factors on its path act as the identity in D_m. Consequently the trace and Jensen proof works in the projected spaces at each fixed choice of the spatial stack bits. For a one-plaquette deletion, place the seam away from that plaquette. The operator inequality (2) survives projection, and Z_{p,1}≥exp(−β)Z still follows in the positive sum of seam integrals for those fixed bits. For each direction the full expectation is a convex combination over the remaining bits, weighted by their partition functions. The Jensen weights may equally well include this extra index, so the inequality W_m(r,s)≥W_m(1,s)^r holds for the mixture itself. Reorient the mixture for the second Jensen step. This proves (1) on the ensemble relevant to the neutral trace. No inequality for a single prescribed temporal seam was used.

## The obstruction on a genuine coarse link

**PROVED by hand, author only.** In dimension four take any block factor b dividing the periods, with a nonwrapping coarse square whose four edges are distinct. Let P_b be the straight-path pushforward of either of the preceding Wilson laws. With Haar as the fine reference, the products on distinct coarse links are independent Haar. Thus the positive Wilson weight has an ordinary coarse density F_b. Fix the heat convention on SU(2) by H_t D_m=exp(−t c(m))D_m, c(m)=m(m+2). Multiplying the generator by a fixed positive constant just changes the unit of time.

Consider the following whole class of candidate block laws Q. Choose an arbitrary joint distribution of base coarse links V and numbers t_e≥0. Conditional on these, multiply V_e on the left by independent central heat rotations of times t_e. On the four edges of the tested square assume only ∑ t_e≥τ almost surely for some τ>0. The choice of active edges may depend on V and the times may otherwise fluctuate arbitrarily. Both τ and the base law may depend on the box, b and β. Then

$$
                               P_b\ne Q.                            \tag{3}
$$

For a single deterministic heat factor even a residual finite signed measure of arbitrary finite total variation cannot produce P_b.

Indeed, each heat rotation or its inverse has matrix mean exp(−t_e c(m)) times the identity. Each edge occurs once. Conditional integration multiplies φ_m(V_C) by exp(−c(m)∑ t_e), and |φ_m|≤1. Hence |E_Q φ_m|≤exp(−τ c(m)). Under P_b the same coarse character is the fine b by b rectangle, so its expectation for every even m is at least L_m(β,b²) from (1). Since log((m+1)!)≤(m+1)log(m+1),

$$
 \lim_{m\to\infty}\frac{-\log L_m(\beta,b^2)}{m(m+2)}=0 .
$$

For every fixed finite b, β>0 and τ>0 some even m therefore violates the heat bound. With a finite signed residual the upper bound acquires only its total variation as a prefactor, which leaves the contradiction unchanged. Composition of any finite sequence of exact straight blockings gives the same fine rectangle with b the product of the block sizes. The contradiction applies at each such step, even for a cutoff-dependent positive time that tends to zero.

**Other noise laws in the scope of the proof.** The same argument excludes independent central factors whose combined absolute multipliers on the tested square are bounded by h_m with h_m<L_m for some even m. In particular it excludes any uniform bound C exp(−c m^{1+ε}) for fixed C,c,ε>0 on all even m. For a heat time S=∑ t_e without a floor, exact reproduction would require, at every u>0,

$$
 \Pr(S<u)\ \ge\
 \frac{[L_m(\beta,b^2)-e^{-u c(m)}]_+}{1-e^{-u c(m)}}\qquad(m\ge2\text{ even}). \tag{4}
$$

Split the conditional multiplier into S<u and S≥u to get (4). It allows S to be positive almost surely with times arbitrarily close to zero. If Q has a floor τ and P_b=(1−ε)Q+εR for a probability R, the same bound with u=τ is necessary for ε. The positive error allowed in row 1330 is precisely the kind of escape on which (3) makes no exact-identity claim.

### A bound on the cost of an approximate factor

**PROVED by hand, author only.** Fix b, τ>0, and a compact band 0<β₋≤β≤β₊<∞. Put

$$
 \ell_m=\left[e^{-\beta_+}(\beta_-/2)^m/(m+1)!\right]^{b^2},\qquad
 h_m=e^{-\tau c(m)}.
$$

Choose an even m≥2 with δ=ℓ_m−h_m>0 by the limit above. These choices precede the size of the torus and any choice of the residual law. For example, for b=2 throughout [2,513/256] one may take the first even m with τm(m+2)>4[513/256+log((m+1)!)]. This specifies an order-one-band test without evaluating a tail numerically.

Let K coarse elementary squares have pairwise disjoint edge sets. Suppose the candidate Q has total conditional heat time at least τ on *each* of them. For every finite constant D for which the measure inequality P_b≤D Q holds,

$$
                              \log D\ \ge\ K\delta^2/2 .              \tag{5}
$$

To prove it let X_i=φ_m(U_{C_i}). Under P_b, each has mean at least ℓ_m. Under Q they are independent conditional on all bases and times, and each conditional mean is at most h_m. Under exponential tilting, any variable in [−1,1] has variance at most 1. Hence the conditional log moment generating function of X_i at θ≥0 is at most θ h_m+θ²/2, by integrating its second derivative from zero. Multiplication and integration give the same bound times K for the sum. Now Jensen under P_b and domination by D Q imply

$$
 e^{\theta K\ell_m}\le \mathbb E_{P_b}e^{\theta\sum X_i}
 \le D\,\mathbb E_Qe^{\theta\sum X_i}
 \le D e^{K(\theta h_m+\theta^2/2)} .
$$

Take θ=δ. The relative entropy obeys the same lower bound. Apply nonnegativity of the entropy of P_b relative to the probability proportional to exp(θ∑ X_i)dQ and take θ=δ. No independence or decay of correlations under the Wilson law enters (5). With N_i coarse sites along direction i, take the basepoints in directions 1 and 2 at 0,2,…,2⌊N_i/2⌋−2 and all basepoints in directions 3 and 4. This yields K=⌊N_1/2⌋⌊N_2/2⌋N_3N_4. Thus an independently heat-smoothed comparison with this floor on every coarse plaquette costs at least a constant times the coarse four-volume in a one-sided log density bound. The coefficient of K is δ²/2. Signed cancellations between two different torus free energies could still be effective.

### Separation from the seed and the five tests

**PROVED GIVEN the checked strong-coupling comparison.** Take the *same isotropic four-dimensional Wilson action* at fixed 0<β<2/9. On any admissible grid with n_j→∞ set w_j=⌊n_j/1024⌋ and t_j=2w_j. Theorem DOB (18), checked at row 790, gives, for the periodic full excited sum on B=n_j³,

$$
 \log(1+S(t_j;B))\le\Phi_B(t_j;\beta)
 \le\frac{96\beta}{1-q}\,t_j n_j^3 q^{\lfloor t_j/2\rfloor-1},
 \qquad q=9\beta/2<1 .
$$

The right side tends to zero. The inequality $s_j(t_j)\le S(t_j;B)$ supplies (M-neutral) and the neutral seed. The full two-period defect tends to zero as well, including at t=n_j/2 by the same formula, so the periodic seed (W) holds. Yet (3) forbids the proposed heat extraction on every one of these finite tori. This is an explicit separation for Wilson measures, including growing boxes, on a comparison trajectory at fixed strong coupling. It makes no assertion about the truth value of the seed on the prescribed asymptotically free trajectory. [Theorem DOB (17)–(21)](gap-vmf-lip.md) · [Check of Theorem DOB](gap-vmf-lip-check-opus.md)

**Group and dimension.** The failure also occurs in five-dimensional SU(2). Increasing the number of unaffected positive bond factors in (2) leaves the inequality intact. The phase-1 commutator is identically one for U(1), yet rotations on the circle separately exhibit the same heat-factor obstruction. In the charge-m channel the constant coefficient of exp(β cos x) exp(imx) is at least (β/2)^m/m!, from the term containing m copies of exp(−ix) in the exponential series. For ordinary SU(3) with w=exp(β Re tr g/3), use the irreducible Sym^m of the defining representation, of dimension (m+1)(m+2)/2. Its dual occurs in the m-fold conjugate tensor power. The constant coefficient of w times its normalized character is at least $(\beta/6)^m/[m!\binom{m+2}{2}]$. All contributions to this coefficient are nonnegative. The positivity and rectangle argument then applies. The heat Casimir grows at least as a positive constant times m² because the diagonal generator diag(i,−i,0) acts on the highest vector by im, and the Casimir form includes the squared action of the corresponding unit generator. Thus there is no group- or dimension-selective *positive* band rate from this premise. At fixed lattice the obstruction holds for every finite β, however large. No limit at β=∞ is taken.

**The coarse coupling.** In (3) the heat coefficients are fixed by the pushforward and the group heat kernel. For a smooth positive density F_s under simultaneous heat flow with generator ∑ a_e Δ_e, its log satisfies

$$
 \partial_s\log F_s=\sum_e a_e\big(\Delta_e\log F_s+
                        |\nabla_e\log F_s|^2\big).
$$

Projecting onto a fundamental square gives a negative linear multiple of its log-density coefficient and the projection of the displayed sum of squares. That projection has no automatic sign because the character changes sign. Row 1431 requires the full residual and a rate in the extracted coupling. The impossibility of the positive-time premise holds *before* either condition could supply a gain. No individual response coefficient has been reclassified as a change in the coarse action.

### How much angular smoothing the factor-two map actually has

**PROVED by hand, author only.** On a 2 by 2 fine rectangle whose ambient periods are at least four, the factorial power in (1) is sharp. For the ordinary expectation, and for even m in the neutral expectation,

$$
 \left[e^{-\beta}\frac{(\beta/2)^m}{(m+1)!}\right]^4
 \ \le W_m(2,2)\le
 \left[\frac{(3\beta)^m}{(m+1)!}\right]^4.                          \tag{6}
$$

Consequently −log W_m(2,2)/(m log m) tends to 4, uniformly over these tori and over any compact subinterval of 0<β<∞. The squeeze uses log((m+1)!)/(m log m)→1, for example by the upper and lower integrals of log x.

Use the single-link conditional Wilson law from row 1367, before its angular projection. Condition on the seam and all fine links except the four horizontal boundary links, two along each of the opposite sides of the 2 by 2 square. No elementary plaquette contains two of them. Collinear consecutive links cannot be opposite sides of an elementary square, and the parallel rows are at least two lattice spacings apart in either periodic direction around their transverse circle. The four conditional laws therefore factor. On each such link the six signed Wilson staples give a quaternion tilt z≤6β. Up to a translation its conditional density is exp(z Re tr g/2) divided by its Haar integral. Its matrix mean, or that of its inverse, has operator norm I_{m+1}(z)/I_1(z). In the two positive Bessel series, the termwise inequality (k+m+1)!/(k+1)!≥(m+1)! gives the upper bound (z/2)^m/(m+1)! for their ratio, also at z=0 by continuity. The remaining transporter matrices are unitary. Integrating the four chosen links and bounding normalized trace by operator norm proves the upper half of (6). The lower half is (1). [Wilson link conditional](gap-seed-astra62.md) · [Outline index, GL3 and GL14](sa-index/chunk-02.md)

This also tests a non-Gaussian proposal using four independent *Wilson* convolution noises with fixed concentrations γ₁,…,γ₄ on the four coarse edges. Their combined absolute multiplier is bounded by (∏γ_e/16)^m/((m+1)!)⁴. By (6) exact representation with a probability residual requires ∏γ_e≥β⁴. If all four concentrations equal γ<β, the candidate fails at a single factor-two step, at every positive β. An equal or larger γ is not certified by this test. Concentration of an auxiliary noise is a different parameter from the projected Wilson coupling in log F_b.

## Sign of the residual after extracting a coarse action term

**PROVED by hand, author only.** Fix b≥2 and a coarse face C with at least two coarse sites in both directions and four distinct coarse edges. On the *full joint* density F_b remove a prescribed plaquette term exp(γ φ_l(V_C)), where γ>0 and l≥1 is a fixed highest weight. The normalized remaining density on the coarse links is

$$
 R(V)=\frac{F_b(V)e^{-\gamma\phi_l(V_C)}}{\int F_b e^{-\gamma\phi_l(V_C)}}. \tag{7}
$$

For both the ordinary and the neutral-twist law, the coefficients

$$
                         B_m=\int\chi_m(V_C) R(V)\,dV
$$

are strictly positive for infinitely many m and strictly negative for infinitely many m. For even l this remains true on the even m subsequence alone. For a fundamental Wilson term this sign change concerns the full sequence of characters, with the other coarse interactions integrated exactly.

**Proof.** In the proof of (6), for a b by b fine square choose all q=2b links parallel to the first axis on its opposite sides. The distance between the rows, also around the periodic complement, is at least two. No fine plaquette uses two chosen links. Conditioning on the other links and on the seam gives, for *all* m in either ensemble, the absolute upper bound

$$
 |W_m(b,b)|\le [(3\beta)^m/(m+1)!]^q .                                 \tag{8}
$$

The square holonomy has a central density f, by gauge invariance. Its character coefficients are a_m=d_m W_m(b,b). Character orthogonality and (8) give the convergent expansion f=∑ a_m χ_m with Haar normalization. More explicitly, the series converges uniformly by (8) and has the same integrals against every character as the marginal. Centrality and density of the character polynomials in the continuous class functions identify the measures. On SU(2) the latter density follows by polynomial approximation on the half-trace interval [−1,1], since the characters are the Chebyshev polynomials of the second kind.

At real z≥1 evaluate the character Laurent polynomials $\chi_m(z)=z^m+z^{m-2}+\cdots+z^{-m}$. They obey z^m≤χ_m(z)≤(m+1)z^m there. With q≥2, (8) and (m+1)²≤(m+1)^q give

$$
 \sum_m |a_m|\chi_m(z)
 \le\sum_m\left[\frac{(3\beta z^{1/q})^m}{m!}\right]^q
 \le e^{3q\beta z^{1/q}}.                                               \tag{9}
$$

The holonomy marginal of (7) is Z_R^{-1} f exp(−γ φ_l), with Z_R>0 its normalizing constant. Multiplication gives its character series at the same z, with the limit

$$
 \sum_m B_m\chi_m(z)
   =Z_R^{-1} f(z)\exp[-\gamma\chi_l(z)/(l+1)]\ \longrightarrow\ 0 .
                                                                            \tag{10}
$$

To justify the multiplication, expand the exponential as its power series. Each product of characters decomposes with nonnegative integer multiplicities. Replacing a_m by |a_m| and −γ by γ bounds the total absolute sum at each z by the left side of (9) times exp(γ φ_l(z))/Z_R. At z=1 this also bounds the expansion uniformly on the compact group, so its coefficients really are the integrals B_m in (7). At z≥1 it permits the same regrouping of Laurent polynomials. Finally χ_l(z)≥z^l and l>1/q, so (9) proves the limit in (10).

A nonzero finite linear combination of these characters either grows like its highest power or is a nonzero constant. An infinite combination with an eventually positive-or-zero tail and infinitely many nonzero coefficients grows without bound. One positive term of degree higher than every negative term dominates their finite sum since χ_m(z)≥z^m. The negative-or-zero tail has the same argument with the opposite sign. All alternatives to infinitely many coefficients of each sign contradict (10), since B_0=1. For even l take the even part in the identity, by averaging at z and −z. The exponential is unchanged, the bound (9) still applies, and the constant coefficient stays 1. This proves the even assertion.

A direct real-group check detects at least one negative coefficient for the fundamental extraction. If all B_m were nonnegative, multiply the residual marginal by exp(γ χ₁/2) to recover f up to normalization. The product exp(γ χ₁/2) φ_m has nonnegative character coefficients and constant term at least (γ/2)^m/(m+1)! by (2). Its residual expectation is at least that constant, while the normalization is at most exp(γ). This would give a single-factorial lower bound for W_m(b,b), contradicted by (8) with q>1. The Laurent argument localizes the contradiction above every cutoff.

Equation (7) measures the residual in the preassigned action decomposition, including the other coarse interactions. Any choice of γ made by an exact chart, including projection of log F_b when that projection is positive with the stated normalization, is covered. A method might sum the positive and negative coefficients before taking a bound, leave high spins to a summable error or use multi-face terms. The theorem only excludes one-sign control coefficient by coefficient after the displayed extraction. Pointwise the residual density itself is positive.

There is also a uniform bound on the omitted *marginal* coefficients. Putting z=2 in the absolute-series estimate, using Z_R≥exp(−γ) and the decrease of (m+1)/2^m for m≥1, gives

$$
 \sum_{m>N}(m+1)|B_m|
 \le (N+2)2^{-(N+1)}
       \exp\{\gamma+3q\beta\,2^{1/q}+\gamma\chi_l(2)/(l+1)\},
 \qquad N\ge0 .                                                        \tag{11}
$$

Thus the eventual signs matter for an exact one-sign certificate even though the marginal tail can be bounded in absolute value. Controlling the joint residual when a second block is formed is an additional estimate.

**RESULT (row 1434).** The exact straight-product Wilson marginal admits no independent heat time with a positive floor on a coarse square. For a factor-two square the high-spin factorial exponent is exactly four. Removing any positive single-character plaquette term from the joint coarse density leaves both signs above every character cutoff. An even term has this property in the centre-blind labels. These are hand arguments, author only. No numerical or Lean computation supplies a proof step. The late-cutoff (M-neutral) condition and the matched four-dimensional SU(2) mass gap remain open.

## Next two rows

1. **Check the obstruction on the neutral torus.** Rebuild the one-plaquette minorant in (2) and the charged open-line transfer after reorienting the three original twist bits. Check (6) on the smallest allowed transverse period four, then check the evaluation in (10) for an even extracted label. A failure of reorientation would withdraw the neutral lower bound and its consequences in (1)–(6). The conditional-link proof of (8)–(11) would stand. A successful check retires exact independent heat time and eventual character positivity after the stipulated extraction on both ensembles.
2. **Test a signed residual on the second exact blocking.** One finite pilot is the ordinary 12⁴ periodic Wilson law on 2≤β≤513/256, with straight products 12⁴→6⁴→3⁴. For a normalized density F define g(F)=4∫φ₁(V_C)log F(V)dV with product probability Haar and a coordinate face C. The squared Haar norm of φ₁(V_C) is 1/4. Distinct elementary faces have orthogonal characters on these grids, so g of the bare Wilson density equals its coupling. Write D for one block pushforward, F=D W_β, γ=g(F), and W_γ for the Wilson reference on 6⁴. Freeze the signed test g(D F)−g(D W_γ)≤0 and the two reference decreases β−γ and γ−g(D W_γ), both strictly larger than (log 2)/4 throughout the pilot band. A proof would give two steps of the prescribed rate in this chart, with the second residual included in full. One rigorous violating β rejects this signed pilot. An unresolved bound is open. The threshold is row 1386's rate guide. Extending a successful pilot would require group and dimension comparisons, uniform control of the other couplings and transport of both thermal masses on the admitted trajectory.
