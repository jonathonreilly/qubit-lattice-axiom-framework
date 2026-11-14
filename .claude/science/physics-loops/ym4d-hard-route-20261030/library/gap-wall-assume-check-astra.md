# Repo search

Provenance: OpenAI Codex, gpt-6-astra/xhigh, FINISH row 901; check of Claude Fable 5.2/max's row 899 at `63f31959f9dad093245a4c56e9c044f2e3a49cec`, source SHA-256 `140f85672b520b321256b727d3968c9d26e02f61ace3bb3eced6c32133f5a39e`. Research text, not an audit; grants no status. Paths below are relative to this lane's `library/` unless stated otherwise. Only this report is written.

The task-specific `prior/gap-wall-assume-check-astra.md` is absent. Read `prior/repo-search-2026-11-08.md` in full: its PI/GW, geometry, averaging and history obligations do not cover this check. Its W1/W2/W5 labels denote different RG witness statements. No competing owner was found by the target-name, half-torus, Langevin and slab searches in `open-registry.md`.

Before deriving anything, searched Markdown/TeX on `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141` in `/Users/jonreilly/Projects/Physics`. Exact query: `VAR-SLAB|W1-t|W4-uni|W3-psi|W1-abs|W2-L2|gap-wall-assume|twisted two-slice|half-torus slab`. Only hits: `pr/10114` and `pr/10133`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/SPHERE2_55.md:266`, whose “W1-type vanishing” is a Ward-profile channel assumption, not this slab proposition (lines 254–272 read). No exact target hit on the other three refs. Broader method searches were capped by unrelated matches and establish no absence. The narrowed method search and outline/account comparison follow.

Relevant existing inputs, credited rather than reopened: Claude Fable 5.2's Identity L (`gap-crux-fp.md:367–386`) already expresses the torus twist ratio as the mean layer ratio. Claude Opus 5.5's Proposition TB, with `gap-compress-check-astra.md:57–65`, already gives the positive two-slice trace law, the absolute-ratio bound and the positive-kernel representation for magnetic backgrounds. Row 882's tube identity is the antecedent of T2/T3, not a new obstruction here. Rows 708–715 already own coupling comparison; this check does not attack that open problem.

The narrowed method query was `Langevin gap|half.torus slab|annealed block|background.uniform layer|twist.ratio.{0,25}(variance|Poincar)|uniform (law on |random )?(cycles|boundaries)|Proposition MIX`, excluding this lane. It completed below its cap. The relevant hit on pr/10114 and pr/10133 is `ym4d-proof/LITERATURE_BRIDGES.md:24` (neighbours 18–29 read): it reports Shen–Zhu–Zhu's fixed-spacing strong-coupling result in `|beta_W|<N²/48` and explicitly says it supplies no continuum gap. Adjacent B15 retains the missing small block-influence matrix; B16 requires uniform boundary decay. These are prior methods, not a supplier for FR or order-one lambda. The other hit, `archive/notes/docs/work_history/repo/review_feedback/AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md:656`, is the unrelated substring “nonuniform boundaries.” No target result was found by this search.

Refs at the read: main `993f5e4f6d11a7e20a1cab9612c5749a53bae073`; pr/10114 `f76f6c649cff7dffbab664d8976e680e8f287fe9`; pr/10133 `89faef229ff6e6bde42baad15ed8270c2f4087d8`; pr/10134 `1e70c7211a2cdbc39001e619f1dd89db45e25851`; pr/10141 `c73ad7b177d94f89ff37b77386936e3d52b48b05`. No refs were fetched or changed. The sparse checkout lacks SCIENCE_WORKFLOW; its current map, RULES and check procedure were read from main. The explicit pinned-file task determines this report's path and verdict vocabulary.

Outline/account check: consulted `sa-index/README.md`, searched chunks and `obligations.md` for the named objects, likelihood ratio, Langevin, kurtosis, Dirichlet slab, electric flux, centre flip, spin network, thermal sum, relative filling and uniform cycles. No exact target locator was found. Poincare/first-passage searches led to neighbouring `chunk-01.md:65–87`, `chunk-06.md:60–81`, and obligations 20–29, 130–138, 306–314. Read SA 588–613, 687–707, 766–779 and 6854–6869 at the supplied source revision `31a47c543775`: scalar block Poincare is a Gaussian/cochain estimate, explicitly not a physical gap; first passage fixes the unit of length via exact dilation. It is not the Wilson Langevin inequality in T6. Read CA-I 2546–2592 and 3352–3415 for the cited block-law claim; its correction is in section 13. No CA-II/III input is needed by the checked statements. The targeted `lit-balaban.md` search returned no relevant locator; no unavailable Balaban theorem is imported. Credit Sussman and Alpoge, with Claude and Codex, for the account and outline; Balaban for their cited UV framework, not for these new identities.

Checkpoint: all requested statement checks completed. T1–T6 and FR, Proposition W1-t, W4-uni/W3-psi/W1-abs/W2-L2, SA1–SA6 and section 6.2 have verdicts below. The core reductions survive; W1-abs's finite-length formula and the common-wall interpretations need correction; SA6's universal statement fails. Next decision: apply these narrow corrections before using row 899 to select a new proof task. FR, a useful order-one lambda, the t>=2 ordering hypotheses and every cutoff-uniform supplier remain open. Numerical GUIDE claims are not verified and discharge nothing. The pinned source is not edited.

## 1. T2, the flip identity — HOLDS

Source lines 312–315. Write `H=A^(t)`, `K=A^(a-t)` and `dq=du dv`. Symmetry and simultaneous-J invariance give

`w_t = H(u,v) K(u,v) dq/Z`,
`w_t o Theta = H(u,Jv) K(u,Jv) dq/Z = rho_t rho_(a-t) w_t`.

Changing variables by the Haar-preserving involution proves the stated identity for every bounded F. Integrating either single ratio gives `Tr(T^a C)/Z=r` by kernel composition and cyclicity. Therefore their covariance is `1-r²`. The same calculation applies to the positive-kernel magnetic-background representative identified in row 849, not an arbitrary square root of its operator.

## 2. T3, half-torus moments and chi-square distance — HOLDS

Source lines 316–320. A direct square-norm check avoids a moment inference: put `H=A^(a/2)`. Then `Z=integral H² dq`, `w=H² dq/Z`, and `rho=H o Theta/H`. Consequently

`E_w rho² = ||H o Theta||²/||H||² = 1`,
`E_w rho = <H,H o Theta>/||H||² = r`,
`Var_w rho = 1-r² = 4p(1-p)`.

The twisted marginal has density `rho/r` relative to w, giving chi-square distance `(1-r²)/r²`. Strictly positive kernels imply `r>0`; nonnegative sector traces imply `r<=1`. Thus `0<=p<1/2`, including p=0 at beta=0. These are identities, not smallness estimates.

## 3. T4, twisted symmetry and the positive form — HOLDS

Source lines 321–324. The twisted density is `H(H o Theta)/(rZ)`, invariant under Theta, whereas `rho o Theta=1/rho`. Thus X=log rho has a symmetric law and mean zero. All its moments exist on each finite compact configuration space. Direct integration gives `E_tw exp(X)=E_tw exp(-X)=1/r`. Therefore

`E_tw sinh²(X/2) = (1/r-1)/2 = p/(1-2p)`,
`Var_tw X = E_tw X² <= 4p/(1-2p)`.

This last inequality bounds the log-ratio variance from above by the flux weight; it is not a converse criterion by itself. The displayed Ising half-ring check is correct for finite ferromagnetic K, with the printed tau. It is distinct from the erroneous finite-length assertion in W1-abs below.

## 4. T5, middle-slice smoothing — HOLDS

Source line 326. The relevant conditional density is `A^t(u,m) A^t(m,v)/A^(2t)(u,v) dm` for an untwisted slab. Multiplying it by `rho_t(m,v)` replaces its second kernel by `A^t(m,Jv)`. Integration yields the claimed ratio. This is a conditional-expectation identity, not a decay or strict contraction estimate. When using the torus notation w_(2t), retain `2t<=a-1`; the standalone slab identity has no such restriction.

## 5. T6, Poincare reduction — HOLDS AFTER CORRECTION of the force description

Source lines 328–332. The inequality itself holds exactly. Lift rho from the two slices to the torus. It is smooth and gauge invariant under the independent gauge actions on both slices, since the kernel is gauge averaged. Its torus gradient has only the two slices' spatial-link components. For `F=|grad X|²`, the product metric and central multiplication give `F o Theta=F`. T2 then gives

`mu(|grad rho|²) = E_w[rho² F] = E_w F`.

Applying the stated gauge-invariant Poincare inequality proves `4p(1-p)<=lambda^(-1) E_w|grad X|²`. No pointwise comparison of marginal densities, boundary supremum, or replacement of the true two-slice law is used.

Correct the sentence identifying G itself as the time-like force. The actual identity is

`grad log A^t = -grad(V(u)+V(v))/2 + E_slab[grad log(time-like weights)]`.

G includes the wall potential term. That term cancels in `Delta G=Theta^*G-G`, exactly as the proof later says. Thus the desired force-difference interpretation is correct. In the unit-S³ metric each boundary spatial link touches one time-like plaquette in this slab. Its trace-coordinate gradient has norm at most one. Hence `|Delta G_b|<=2 beta`, and the `6|B|` links give the printed `24 beta²|B|` bound.

## 6. FR and its flux consequence — HOLDS as a conditional implication

Source lines 334–342. Summing FR over the `6|B|` boundary links and applying T6 gives precisely `p(1-p)<=3|B| eps²/(2 lambda)`. The ratio has `p<1/2`, so this controls p itself: if the right side is `eta<1/4`, then `p<=(1-sqrt(1-4 eta))/2<=2 eta`. For a target `p<=p_*<1/2`, it suffices that `eps²<=2 lambda p_*(1-p_*)/(3|B|)`.

For an upper-wall link, use simultaneous-J covariance to express its response as a flip of the lower wall; for a lower-wall link flip the upper wall. The isometric pullback of the tangent vector is essential. A seam can be moved away from the observed link without changing the derivative observable. No estimate of that response follows from moving it.

FR and a useful volume-uniform lambda remain OPEN at the claimed order-one couplings. Smallness at one cutoff does not supply first-passage uniformity. The comparison with Proposition MIX's numerical tolerance is GUIDE only: different laws and prefactors are involved. The reduction supplies a flux estimate for each chosen cut/background when its own hypotheses hold, not the glue seed or a mass gap.

## 7. T1 and W3-beta, coupling derivatives — HOLDS with the source's stated correction

Source T1 and section 3.3. At finite volume differentiation under the compact integral is legitimate. For each plaquette separately, move the twist sheet away from it. The differentiated signed plaquette then becomes the ordinary plaquette in that representative. Hence `d_beta log r=sum_p D_p` and `Cov_0(x_p,W_Sigma)=r D_p` for each sheet avoiding p.

For a spatial plaquette insertion O, set `x_e=Tr(O P_e T^a)/Z_e`, `x_o=Tr(O P_o T^a)/Z_o`. Subtracting the ordinary mean `(1-p)x_e+p x_o` from the signed mean `((1-p)x_e-p x_o)/r` gives `-2p(1-p)(x_o-x_e)/r`, including its sign. A time-like plaquette uses a differentiated one-step kernel, as the source's Summary already corrects; it is not a multiplication operator on a slice.

W3-beta follows by differentiating `log Z_o-log Z_e`. The odd “mean” here is the derivative of a sector trace, not expectation under a positive local gauge-field Gibbs density. The formula requires `Z_o>0` (beta>0); at beta=0 its logarithm is undefined. T1's full twist-ratio derivative remains defined there, without separately normalized odd means.

## 8. Proposition W1-t — HOLDS; the ladder interpretation needs correction

Source section 8.1, lines 360–372, superseding the earlier ARGUED lemma. Its domain `4|b`, `b,c,d>=3`, `t>=1` is sufficient. Integrating the time-like links gives the product of the original slice kernels; endpoint spatial potentials are equal at 1 and J1. Thus the slab ratio is exactly the kernel-power ratio, with all normalization constants cancelling.

For the transverse transfer, exchange its two cross-sections and invert each intervening nu-link. The new plaquette trace is the old inverse trace up to cyclic order; the real SU(2) trace is unchanged. Haar inversion preserves the integral, establishing self-adjointness. The top-link flip R preserves within-section plaquettes and changes precisely the seam bonds. Hence `Z_anti=Tr(R T^b)`, and `1-Z_anti/Z_per=2w_o`.

For a component M of the summed wall-to-wall line, `RMR=-M`, `||M||<=cd`. Put `A=P_e T^(b/2)`, `B=P_o T^(b/2)`. Because `b/2` is even, A and B are positive, regardless of the sign of T. Expanding the correlator eliminates the same-parity terms and gives

`Tr(M T^(b/2) M T^(b/2))=2||A^(1/2) M B^(1/2)||_HS²`.

Schatten Hölder bounds this by `2(cd)² sqrt(Tr A² Tr B²)`. Sum the four real quaternion components and divide by `(cd)² Z_per`: `0<=gbar<=8 sqrt(w_e w_o)<=8 sqrt(w_o)`. Therefore `1-Z_anti/Z_per>=gbar²/32` and `kappa_t>=gbar²/64`. No infrared or numerical input is used in this proposition.

The resulting implication `ORD_t => kappa_t does not tend to zero` holds. **HOLDS AFTER CORRECTION** for the surrounding “exactly”/“equivalently” readings at lines 376 and 389: absence of a positive long-distance limit is only necessary. It does not imply an area law, any rate, or a uniform bound over other boundary pairs. Correlations may tend to zero subexponentially. Nor does this proposition establish a unique critical thickness or monotonicity in thickness. Replace “survives exactly from” by “is not excluded by this flat-pair obstruction at thicknesses where ORD_t fails.” All t>=2 ordering claims from section 8.3 remain GUIDE; its runs were not inspected or repeated.

## 9. Lemma W4-uni — HOLDS on the cited box domain

Source lines 212–215; definitions checked against `gap-seeddec-max.md:68–77,178–188` and its check, sections 1, 2 and 7. Retain the full domain from row 887: each side has between 2 and L-1 sites. “Interior” means not contained in the boundary, not merely all edges whose endpoints lie in the box.

There is also a direct check of equality of the marginals without counting fillings. For each of the three torus generators choose a winding coordinate loop outside N's interior edges, using a transverse coordinate omitted by N. Given any torus cycle z, subtract the appropriate three loops. The resulting cycle is null-homologous, hence a boundary, with the same restriction to N. Thus the restriction images of cycles and boundaries coincide. A linear map sends uniform measure on a finite vector space to uniform measure on its image. This proves equality of the two laws. To identify that image, a relative cycle has a relative filling because `H_1(N,boundary N;Z_2)=0`; extend that filling by zero. All four plaquettes incident to an interior edge are interior, so its global boundary restricts to the desired cycle.

The quotient has eight homology classes of equal size, giving 7/8 versus zero. For the decoder constant, apply SEL on L=4g, giving `(7/8)/64=7/512`. The one-box marginal is uniform on the same relative cycle space in any admissible larger ambient torus, so the same local lower bound transfers. Consequently `64 p_0>=7/8`, which violates SEED-DEC-U's strict `64 p_0<1/192` even under law B.

The density is 1/2: adding an elementary plaquette boundary through any edge pairs configurations with opposite occupation of that edge, under either law. This is a **maximal-entropy** example, not literally a maximal-density example (the full edge set is itself a cycle of density one). The conditional first-passage extrapolation remains conditional; this lemma proves no convergence of Wilson label marginals. Equal single-box marginals also do not make their joint law over several boxes equal.

## 10. Lemma W3-psi — HOLDS

Source section 3.3, with definitions and inputs at `gap-means-max.md:150–162,202–213`. Keep the dyadic sequence `t=2^k t_0`, integer `t_0>=3`; independence of t_0 is not needed or asserted here. Lemma K(b) makes `e(t,c,d)/t` nonincreasing. In the source's normalized Wilson convention the kernel is at least `exp(-12 beta tcd)`, so its constant-function Rayleigh quotient gives `e(t,c,d)/t>=-12 beta cd`. This supplies the lower bound omitted from the short proof.

For fixed `(a,c,d)`, nonnegative transfer eigenvalues and trace class give `S(t)<=S(t_0)<infinity` for t>=t_0. Therefore `t^(-1)log Z(t;(a,c,d)) -> e(a,c,d)`. Axis exchange and the established limit of `e(t,c,d)/t` give the full thermal density `psi=e(a,c,d)-a e_inf(c,d)`. The even-sector projector average satisfies `Z/8<=Z_0<=Z`: the untwisted term is in the average, all electric twists are positive partition functions, and their absolute traces are at most Z. The even vacuum eigenvalue is the same lambda_0. Dividing logs by t removes the factor eight, proving the identical even density and its nonnegativity.

In `2psi(a)-psi(2a)` the e_inf terms cancel exactly. This proves Delta_1 and its upper bound. Successively doubling the three spatial sides gives `delta=4Delta_1+2Delta_2+Delta_3`; substitution gives the printed weighted sum of psi. It is a long-tube reformulation, not a bound on that density from the even sum of one cube.

## 11. Lemma W1-abs — HOLDS AFTER CORRECTION

Source lines 64–66, repeated incorrectly as “at every length” in Summary item 1. Assume ferromagnetic `0<=K<infinity` and integer ring length n>=3. Put `q=tanh K`. The two transfer eigenvalues are `2 cosh K` and `2 sinh K`, so

`Z_anti/Z_per=(1-q^n)/(1+q^n)`.

Differentiating `Z_per=(2cosh K)^n(1+q^n)` gives the exact bond mean `E(ss')=(q+q^(n-1))/(1+q^n)`. With `R=exp(-2Kss')`, direct substitution then gives

`(1/2) E|1-R| = q/(1+q^n)`,
`(1/2) E(1-R) = q^n/(1+q^n)`.

For 0<K<infinity the first is strictly less than tanh K at every finite n, and tends to tanh K as n grows. The second tends to zero. Replace the claimed finite-length equality/floor by these formulas, or restrict the equality to the infinite-length limit. A uniform lower bound q/2 is valid. The intended cancellation example survives. For negative K the printed positive tanh K expression cannot be an absolute expectation; that regime is outside the intended ferromagnetic example.

## 12. Lemma W2-L2 — HOLDS

Source lines 114–115; checked against the actual response identity `gap-annealed-opus.md:29–54` and its check, sections 1–3. Regard `xi_(j,c)` as the linear map from the tangent space at exterior link j to that at resampled link c; its transpose brings gradients back to j. Differentiating the normalized conditional integral gives exactly the printed derivative operator. For j outside the block, conditional integration leaves its tangent fibre fixed, so the direct term is well defined. For j inside, the result is independent of U_j and has zero derivative.

The assumed inequality is on gradient fields only, which suffices: `P^s f` is smooth and each iterate remains in that class. Thus `||grad P^s f||_2<=q^s||grad f||_2`, with `0<=q<1` understood. A finite constant C exists because the positive smooth Wilson density on the finite product of spheres is bounded above and below. It need not be uniform in volume.

For centred smooth f and its spectral measure nu_f,

`integral lambda^(2s) dnu_f(lambda)=||P^s f||_2²<=C q^(2s)||grad f||_2²`.

Positive measure on `|lambda|>=q+eta` contradicts this as s grows. Density of centred smooth functions removes that spectral interval on the whole centred space. Moreover P averages orthogonal conditional projections, so its spectrum is actually nonnegative. Hence `sum_a mu Var_(B_a) f = |A| <f,(I-P)f> >= |A|(1-q)Var f`, first for smooth f and then all L² functions. If q=0, gradient zero makes Pf constant directly. No square-root loss occurs here, unlike the older L¹ spectral argument.

This proves only the conversion from the stipulated L² contraction. A bound on the norm of each individual decomposable block operator is not a necessity for a norm bound on their sum. No general impossibility of cancellation or “decoherence” methods follows.

## 13. SA1, scale and bare variables — HOLDS AFTER CORRECTION

Source line 261, tables 1d/2g/2h/4c/5g. The application mismatch is real: an estimate for an order-one bare Wilson coupling is not the required bound uniform over first-passage data (`gap-finishline-opus.md:114–148`). However, “one order-one coupling in bare variables” is not a common theorem hypothesis. W2's repeated-update equivalence holds for any such block Gibbs law; W4's homology/counting statements have no coupling; W5 is explicitly an abstract Markov-operator statement. These persist under a change of scale whenever their hypotheses persist.

The account claim needs a concrete correction. CA-I 2556–2560 excludes block-law statements from its main theorem and calls their proofs outstanding. But CA-I 3362–3368 **defines** the positive normalized block law `nu^B_(K,s)=rho_(K-s)dV_(K-s)/integral rho_0`. CA-I 3370–3398 states a quantitative comparison and explicitly says it is not proved. CA-I 2582 gives the exact mass identity. Thus replace “gives neither a block law nor a transfer operator” by “defines the block law but does not supply the comparison/transfer structure needed for this application.” The cited passages do not prove nonexistence of a transfer representation.

Likewise, neither W4-uni nor the cited checks prove that the Wilson label law becomes locally uniform along first passage. The typical one-layer ratio and Gaussian-block assertions are ARGUED in their sources. Keep all three as proposed ultraviolet mechanisms, not established reasons that every wall becomes worse. The sound shared issue is matching a useful estimate to the actual first-passage family with uniform constants.

## 14. SA2, uniform conditioning — HOLDS AFTER CORRECTION

Source line 262. W1 does demand a supremum over a pair of slices. W2's literal AN1 really is the conditional exterior supremum, by the repeated-update calculation in `gap-annealed-check-astra.md:69–87`. Rare exteriors do not weaken that condition. These are faithful readings.

W5 is different: quantifying over an abstract operator class is not conditioning on an exterior, and no disintegration identifies the two. Use it as an analogy about discarded model structure, not a shared conditioning hypothesis. Also, TB2 exhibits an obstructing flat pair; it does not prove that a flat pair globally maximizes the layer functional. The cited zero-field claim concerns a particular single-site response bound (`gap-blockcrit-opus.md:263–270`, explicitly ARGUED for its sharp realization), not every transport field or block response. Replace “extremal points” by “known obstructing/test configurations for different functionals.”

The W5 summary also omits a material premise of its numerical consumer. D/D1 need `S_ev(a)<=160^(-16)` and a>=82; K′'s sufficient 1.66 needs **also** even a, the matching Wilson sector-trace domination, and `S_ev(a/2)<=1` (`gap-wall-check-astra.md:154–182`; `gap-wall-max.md:298–306`). Smallness at time a alone does not bound the half-time sum: many small eigenvalues can have a small sum of a-th powers and a large sum of half-powers. Restore the full GLUE premises wherever 1.66 is used. The floor kappa>=1.66 is sufficient under those premises, not an equivalent characterization of the flux half. The two one-way implications in table 5e do not prove existence of a Wilson sector in the intermediate range; use the checked threshold 1.132, not 1.13.

## 15. SA3, absolute majorants — HOLDS AFTER CORRECTION

Source line 263. The identified losses are real: TB bounds a signed deficit by an absolute mean; AN1 uses nonnegative transport norms; the two W4 majorants forget signs and much geometry. W1-abs, with its corrected finite-ring formulas, shows that this can lose the whole long-distance gain. PAR's signed mixture is correctly retained by row 891, section 9. Neither input proves quantitatively large cancellations for the actual SU(2) law at order one or along first passage. W4's positive cycle probability is not itself a signed measure; the signed representation and its possible benefit must be kept distinct.

In particular, dropping the absolute value does not remove the W1 flat-pair obstruction **while retaining uniformity**: at that pair the deficit already has the positive lower bound of TB2. Signed averaging can escape that obstruction only when the demand for uniform boundary control also changes. The theorem about the flat pair does not logically require an absolute value.

The moment symmetry needs its variable specified. Under w, T2 gives `E rho^s=E rho^(2-s)`. The line `E Q^s=E Q^(1-s)` is correct for **Q=rho²**, the Radon–Nikodym derivative of the flipped untwisted marginal relative to w. Under w_tw, instead, `E exp(sX)=E exp(-sX)`. This does not make rho/r the flip derivative. T4 and VAR-SLAB themselves already use the correct transformations.

## 16. SA4, torus and conserved charge — HOLDS for the named consumer

Source line 264. Row 882's covariance is a conserved-sector variance on the torus; it is independent of sheet separation, not a correlation controlled by within-sector decay. Theorem S's current input is periodic trace partition functions with axis exchange (`gap-crux-restate.md:170–183`). W5's electric sectors and W1's winding seam use that setting. Thus a free-boundary replacement requires a changed consumer and a proof connecting its hypotheses to the goal.

This is a restriction of the currently used route, not a theorem that no other boundary consumer can exist. Open/fixed boundary choices also need their allowed boundary gauge transformations specified before declaring a centre flip gauge-trivial. The table's low-priority judgment is a research choice, not a mathematical consequence.

## 17. SA5, one coupling — HOLDS AFTER CORRECTION

Source line 265. The proposed order-one tests are evaluated at one coupling; their algebraic/topological obstructions are not restricted to a single coupling. Their hypotheses can be tested at every beta. Following beta does not invalidate the obstruction at any beta where it applies.

The alternative supplier is accurately credited prior work. `gap-mid-max.md:252–276` proves Lemma M and Proposition MIX: the folded long-torus marginal and the short-torus law have identical one-link rules away from the seam; comparison of their central plaquettes **for every s in (0,beta]** bounds `Phi_B<=12a|B| beta eps(a)`. The BOOT_eps formulation at lines 81–86 compares restrictions of symmetric states. These are sufficient coupling-interval estimates, not consequences of continuity at one endpoint. Tables 3b and 5e do not add a new supplier. Keep the useful “follow the coupling” proposal, but describe “one coupling” as the chosen attack, not a hypothesis common to all five wall theorems.

## 18. SA6, every compact group with a centre — FAILS as stated

Source line 266. The universal quantifier exceeds the stated mathematics. W3 and W4 here use an involutive centre operation and Z_2 chains. For example SU(3) has centre Z_3 and no nonidentity central involution: its twist obeys C^3=1, not the C²=1 used to obtain `1-r²=4p(1-p)`. The same proof and numerical identity do not run verbatim. W1's quantitative threshold uses the O(4) flat-layer representation and its infrared bound; it is not a proof for an arbitrary compact group or action. W2's moment/supremum equivalence is much more general, while its tangent-field conclusions require a smooth setting. W5's abstract counterexamples show insufficiency of S+, not a theorem about the Wilson measure of every group.

Correct replacement: these obstructions use broadly shared structures and, in their demonstrated comparison models, do not isolate the SU(2) mechanism needed for the seed. Match each proposed extension to its centre element, representation, action and analytic hypotheses. This weaker reading is supported by the cited checks. The further statement that all open ends are *the same* vacuum response to a thick vortex remains an analogy: no implication from block absorption to the decoder's S1/S2 or to the actual kurtosis floor is supplied. It cannot be used as an equivalence or a restriction on all possible future methods.

## 19. Section 6.2, five ways to one comparison — HOLDS AFTER CORRECTION as a research reading

Proposition MIX is a valid common **sufficient target**. It compares a particular pair of laws at central plaquettes over a coupling interval and then integrates that difference. T1 is the corresponding twisted derivative identity. Neither says that every seed proof must prove such an absolute comparison, or that every listed alternative is equivalent to it. Integration can also cancel differences of opposite signs. The original large and small torus laws are symmetric; the folded marginal on the small torus has a distinguished seam and is not claimed to have all its translations.

The cited checks support these narrower statements:

- W1 excludes the specified background-uniform one-layer bounds above the exact threshold. It leaves typical-law and thicker-slab estimates open.
- W2 collapses literal AN1 to an exterior worst-case criterion. It does not exclude the random-schedule/path-sum, Lyapunov or signed L² alternatives; row 852 explicitly keeps them open. A within-law clustering result is not automatically the between-law comparison required by MIX.
- W3 prevents obtaining decay of this conserved-sector covariance by increasing sheet separation. It does not prohibit comparisons, additional tube estimates, or the half-torus variance upper bound. This part of section 6.2 is faithful to row 882.
- W4 excludes neither the electric route nor every support method. Rows 882 and 891 establish arithmetic restrictions on two specified majorants, conditional on unproved model inputs. Section 4.1 of the checked note says this correctly; “closes the electric route by supports” in section 6.2 loses that qualification.
- W5 shows that S+ alone cannot force the kurtosis floor and that WALL_40's minimum form reduces to kappa>=2 under its GLUE hypotheses. It does not prove that locality/transverse extent/thick-vortex splitting is the only possible supplier. K′ makes kappa>=1.66 sufficient with its full premises, not necessary for a flux estimate.

Replace the title/readout by: **“Five restrictions on proposed sufficient routes; a plaquette comparison is one common open target.”** This preserves the useful distinction between clustering and comparison without declaring five exhaustive or equivalent closures. W4's GUIDE density and W5's sufficient threshold cannot carry stronger exclusion language.

## 20. Related signed good-set estimate, table 1a — HOLDS AFTER CORRECTION

Line 49 writes `E(1-rho)<=sup_G(1-rho)+P(G^c)`. Positivity of rho only proves `E(1-rho)<=P(G) sup_G(1-rho)+P(G^c)`. Dropping P(G) is valid if the supremum is nonnegative. Otherwise use its positive part. This matters when cancellations are the proposed benefit. The good-set route remains a sufficient route with this correction; no good-set estimate is supplied here.

## Coverage and disposition

All requested formal statements and the six shared assumptions were checked against the pinned text. Corrections are recorded here only. The source, FINISH, registry, audit files and remote refs are unchanged. No numerical job, proof search, formal verifier, literature download or posting was run. Section 8.3's scripts, measurements and phase interpretation were not verified. Prior check verdicts were used only at their stated scopes; a second provider alone is not the independent path. The present hand checks use square norms/change of variables, parity-block operator bounds, restriction images of chain spaces, exact Ising transfer eigenvalues and the spectral-measure argument.

The remaining scientific obligations are estimates for FR and the Langevin gap with the required family of constants; an upper bound on thick-slab kappa; the actual Wilson decoder inputs; and a source of the kurtosis floor under the full consumer hypotheses. This check proves none of them and rules out no additional route beyond the quantified statements above. The report is left locally for the lead; it is uncommitted and unpushed.

RESULT: Row 901: the VAR-SLAB moment identities, twisted symmetry, Poincare inequality and conditional FR reduction HOLD (correct G's force description); Proposition W1-t, W4-uni, W3-psi and W2-L2 HOLD on their stated domains; W1-abs HOLDS AFTER the finite-length correction. SA4 HOLDS for the named torus consumer; SA1, SA2, SA3, SA5 and the “five ways to one comparison” reading HOLD AFTER the scope/premise corrections above; SA6's “every compact group with a centre” statement FAILS. No order-one or cutoff-uniform mass-gap input is supplied and no status is granted.
