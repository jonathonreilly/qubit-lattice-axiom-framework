# Repo search

Provenance: OpenAI Codex, gpt-6-astra, xhigh (the dispatched model and effort), checking commit `929e7723535a2eeaf65d15e439fe8e5db8d6b54e`. Research check only; no audit, status grant, or mass-gap claim. This report does not read row 1047, run a numerical proof, or attack a new route.

The task-specific prior note is absent. The lead's November 8 digest records searches of main and PRs 10114, 10133, 10134, and 10141. I read its search contract and relevant Hessian, boundary-law and screening entries. There is no target-specific “Repo prior work” list in row 1048. I fetched main and PR 10114, checked the following source passages, and ran a short label/method search on those refs. I did not repeat the lead's other three branch searches.

| Source checked | Proximity to this target |
|---|---|
| Main `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`, `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` | Covariance/score identities for a supplied noncompact Dirichlet Maxwell law; no pinned SU(2) extension minimization. |
| PR 10114 `f76f6c649cff7dffbab664d8976e680e8f287fe9`, soft-route `BARE_COUPLING_MATCH_ASTRA.md:362–375` | A fixed-domain Haar-normalizer saddle Hessian, sharing the symbol H_c but not the object. |
| Same ref, `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | A one-step plaquette correlation lower bound via convolution; no response/extension theorem. |
| Same ref, `SOURCE_LOCAL_RETURN_ASTRA.md:315–369` | Exact forest-gauge Haar change of variables retaining history factors; useful gauge-invariance method, but no frozen-boundary score correction or cost infimum. Located through `SESSION25_RESULTS.md:2267–2285`. |
| Same ref, `SOFTHARD.md:492–496`, `REVIEW_SOFTHARD.md:178–182` | Dimock/Balaban history-return discussion, explicitly an open 4D return package; different meaning of “gauge return.” |
| Main, `NATIVE_WEAK_ELECTRIC_SPECTATOR_GAP_NOTE_2026-09-08.md:53–66` | A signed gauge return in a supplied Majorana Hamiltonian; different model. |

The closest actual prior result is this lane's FLOW (`gap-short-step-max.md:217–232`, Claude Fable 5.2): the score identity, with minimizer existence left ARGUED. EXT supplies a finite-dimensional infimum argument for that same object. GR and the cube formulas come from Fable's `gap-boundary-q.md`; the response hierarchy and SQ come from its `gap-coulomb-frame.md`. K1 is the continuous frame construction in Opus 5.5's row 1044 check, and the chart bound is from the gpt-6-astra row 1041 check. These are credited inputs, not new discoveries of this report. The searches found no separately owned registry row for this assigned extension check. They are bounded search results, not an absence theorem. I did not read the concurrent row 1047 file.

The Sussman–Alpoge index was searched first for the extension, Haar Laplacian, gauge return, score variance, boundary response and gap objects, including the CA 4.12–4.19 index. Neighbouring rows were read before their cited passages. Outline L232–293 proves the finite-product measure and gauge invariance, and explicitly limits cutoff-uniform conclusions; L588–599 distinguishes decay from a gap. These are credited background inputs. The CA index's Laplacian hit at CA-I L46484–46506 concerns lattice site/bond operators, not the configuration-space Haar Laplacian in POLY. The label match `cube-extraction` in the full index is a different Cauchy estimate. No indexed supplier of the target's extension theorem was located. Nothing here claims to have searched all 166711 CA-I lines by full reading.

## Working checkpoint

Pinned source: `library/gap-o2-extension.md`, 511 lines. Both Sussman–Alpoge source files were fetched once at `31a47c543775` into the newly created `/tmp/sa-gap-o2-extension-check-astra.B8i7ie/`. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for any input taken from those files.

Plan: (1) check source identity, prior hits, index and consumer; (2) do the three requested hand tests; (3) check TAN and CUBE-EXT; (4) check POLY, EXT and EQ; (5) check HIER+, O2-GR and its remainder; (6) check AVG, MEAN and the wall; (7) check GR+, O2-GR+, CURL-Q and U(1); (8) finish statement verdicts and one RESULT line.

Completed: all seven mathematical checks below and the requested hand tests. Only this report is edited. The open obligations remain exact minimizer attainment, a common site-frame realization on upper faces, pin probabilities, classical constants and the consumer's N1–N3/O1/tiling inputs. No new attack on them was made.

## 1. Three hand tests

**Cube zero score — HOLDS.** At the base pin, set the gauge parameter to the displayed `psi_x` on the four bottom vertices, and zero on the top vertices. Its generator on a bottom link is `psi_x - Ad(H_l) psi_y`; on a vertical link it is `psi_x`; on a top link it is zero. Thus it agrees with the proposed extension at every free configuration. Differentiating each plaquette trace under this gauge map gives zero. Every free component is a fixed left rotation, hence has zero Haar divergence. Therefore `Psi(U)=0` for every `U` at this base pin.

This does **not** say `V Psi=0`. The boundary rotation is frozen at the base pin, rather than updated to the gauge generator at nearby pins. This distinction permits a nonzero response. FLOW gives `Q=H_c` at the base pin.

**One exact GR variance value — HOLDS.** Set `phi=pi/2`, `gamma=pi/2`, `lambda_A=1`, and `lambda_o=lambda_B=lambda_C=0`. Write `c=1/sqrt(2)`. Only the side above `(o,A)` contributes to the free part of the second action derivative. Its returned link has `|a-Ad(q)a|^2=2-sqrt(2)` and `(a cross Ad(q)a).u=1/sqrt(2)`. Its mean force is `kappa u`. Consequently

`Q_GR=(2-sqrt(2)) beta xbar - sqrt(2)(b_0+kappa)`,

`H_c=-sqrt(2)(b_0+kappa)`, and therefore

`Var(Psi_GR)=(2-sqrt(2)) beta xbar`.

These follow from differentiating the single side trace and the pinned plaquette, not from a numerical integral. Substitution in 2.3 agrees: `T=1+sqrt(2)`, `Lam=1`, and `T-2c(1+c)=0`.

**AVG on two atoms — HOLDS.** Let a pin law put probability `p` on a good atom and `1-p` on a bad atom. For a unit closed field, take the two scalar responses to be `-A_0` and `A_0`, respectively. These are an algebraic test of AVG's hypotheses, not proposed Wilson pins. Their average is `(1-2p)A_0`, while AVG gives `(1-p)A_0`. The inequality holds and the average can be positive when `p<1/2`. A positive-measure negative set alone does not yield an averaged curl bound.

## 2. Cube statements

**TAN and CUBE-EXT — HOLDS**, with the frozen-base interpretation above. Writing `z=exp(i phi/2)`, the four transverse equations reduce to `(z^2-z^(-2))w_C=sin(gamma)[theta_1(1-z)-theta_2(1-z^(-1))]`. The denominator is `2i sin(phi)`, nonzero on the stated domain. This verifies all four equations, including the one not used to define the other three unknowns. The longitudinal equations are ordinary differences. Since `1-c>0` and the eigenvalues of `T` are `1+c` and `1+3c`, the claimed strictness follows whenever `b_0+kappa>0` and `sin(gamma)!=0`.

For TAN's value, conjugating the frozen path by the inverse site gauge gives residual logarithm `s^2(psi_x cross Ad(omega_l)psi_y)+O(s^3)`. Pairing twice this acceleration with `grad F_c=E N` gives precisely its displayed force formula. The restriction `h!=+-1` matters. The off-axis colour on this one-holonomy cube is not a covariant colour; the note states this correctly.

**Exact GR variance — HOLDS AFTER CORRECTION of 2.4.** The formula in 2.3 is correct. The first sentence of 2.4 incorrectly equates `Q_GR` with its variance at `b_0=0`. Replace it by:

> At `b_0=0`, put `B=beta xbar-2kappa c(1+c)`. Then `Q_GR=2 sin^2(gamma)(1-c) B Lam>=0`; generally `Var(Psi_GR)=Q_GR-H_c`, not `Q_GR`.

Here is the missing sign argument. Take all three head values `lambda_A=lambda_B=lambda_C=1`. Then `T=0`, `Lam=4`, and `H_c=0`. Positivity of the variance gives `B>=0` (choose a transverse colour). The same `B` applies to every potential. Thus the claimed nonnegative sign survives, without the false equality. The equality really does fail within the stated domain: CUBE-Z's positive character coefficients give `kappa(1)>0` for beta positive, since `U'_(d-1)(1)=d(d^2-1)/3` and the d=2 coefficient is positive. Continuity gives noncentral pins close to 1 with `kappa>0`; choose `theta_1=1`, `theta_2=0` and a transverse colour there. At b_0=0 their response is strictly negative, so cost and variance differ.

## 3. POLY, EXT and the meaning of EQ

**POLY — HOLDS AFTER CORRECTION at target L182.** The Laplacian assertion is correct. The incidental claim that *every* force `N_l` has degree at most three must say **every pinned-link force**. A plaquette derivative at a free link can still have four free factors. On the four top links of the cube, the top-plaquette force is odd separately in each of those four quaternion variables. It is nonzero, whereas a polynomial of total degree at most three has zero projection onto that parity sector. Thus the unqualified degree claim fails. Only pinned forces enter EXT, so its degree `4n+3` remains valid.

For completeness, the finite-dimensional inversion reads as follows. Left multiplication of one quaternion is linear in its four real coordinates. Its derivative preserves polynomials of bounded degree, including their restrictions. Haar integration gives `<p,Delta p>=-sum ||R p||_2^2`. A vector in the kernel is constant under every one-link rotation; these rotations generate the connected product `SU(2)^n_f`. The kernel therefore consists of constants. Symmetry in the finite-dimensional restriction space gives range equal to the orthogonal complement of that kernel. This proves the unique mean-zero inverse without a numerical inversion or an elliptic regularity import. If `n_f=0`, the space consists of constants and the mean-zero assertion is vacuous.

**EXT — HOLDS for every pin and every boundary field of the stated SU(2) cell.** There is always an eligible base field: freeze `B` on the pinned links and use zero on the free links. Its score is a polynomial of degree at most three. Its coefficients need not have any sign, and the pin need not be regular or irreducible.

The essential identity is a weighted divergence identity:

`(W A+div W)e^A=div(e^A W)`.

With `W=e^(-A) grad v_n`, its right side is `Delta v_n=g_n-gbar_n`. Since `int f e^A=0`,

`gbar_n=int f(e^A-E_n)` and

`Psi_n-c=e^(-A){f(e^A-E_n)-gbar_n}`.

Thus `|gbar_n|<=r_n||f||_infinity`, and `||Psi_n-c||_infinity<=2e^(a_0)r_n||f||_infinity`. The same identities show `E(Psi_n)=c` exactly. As `||f||_infinity<=2||Psi_0||_infinity`, the variance bound is precisely

`Var(Psi_n)<=16e^(2a_0)r_n^2||Psi_0||_infinity^2`.

The exponential series remainder tends to zero. Every field is smooth on the compact free-link space and extends smoothly to neighbouring pins by freezing its base-pin coefficients. Its flow is complete locally in the boundary parameter. Applying FLOW proves both inequalities and `inf_V Q_V=H_c`. This is an infimum, not an asserted attained minimum. For a linear base rule, all operations, including `c` and the inverse of `Delta`, are linear in `B`. One index `n` therefore controls a whole finite-dimensional field space after bounding `||Psi_0(B)||_infinity` by its operator norm times `||B||`.

**A-FLOW — HOLDS**, conditional on the corrected EXIST input. In L220–225, use `||lambda||_Y`, with the corner omitted, throughout. The score does not see the corner. Each head occurs at most four times, giving `||Psi_0||_infinity<=24 beta sqrt(N)||lambda||_Y`. The constant works because `2*9216=18432<136^2=18496`. This proves the displayed margin `m_0/2` with one linear extension rule for every potential and every pin of `P'`.

**Group scope — correction required at L216.** Replace “every compact group” by “SU(2), and compact U(1) by the same polynomial argument.” More generally the proof needs a connected compact matrix group, polynomial action and boundary score, and a spanning invariant Laplacian. Compactness alone is insufficient: on a disconnected group the Laplacian kernel contains the functions constant separately on connected components. Total mean zero then does not imply membership in its range. No general disconnected-group extension theorem was proved here or in the target.

**EQ(i)–(iii) — HOLDS. The exact-equivalence reading at L305–308 and L350–351 needs correction.** FLOW proves (i). The finite-dimensional uniform choice of `n` proves (ii) and (iii). What has no extra information is the **infimum of costs**. A specified extension's cost still has its nonnegative score variance.

Replace the inference after EQ by:

> The infimum over smooth FLOW extensions equals `H_c` pointwise, and a linear rule approximates it within `delta||theta||^2`. Strictly negative response on the relevant quotient yields an actual negative-cost extension. The exact non-strict bound `(S')` does not, by this infimum argument alone, produce one extension satisfying `(S)` with the same constant and no mass error. Attainment or an additional margin would be needed for that inference.

In particular, `H_c<=0` is necessary for literal O2; a strict margin is sufficient. Literal O2 is not equivalent to *strict* O2-min: the U(1) zero form is an immediate counterexample to that wording. These qualifications do not reopen A-FLOW, which has a strict margin.

## 4. HIER+, the chart remainder, and O2-GR

**HIER+ — HOLDS AFTER CORRECTION of the induction at L236–240.** As stated, `gamma_ab` may depend on all angles. The old upper-left block at step `j` need not tend to the previously evaluated block when the new angle is chosen. The application in 4.5 has only pairwise angle dependence and avoids this issue. The following replacement proves the full stated lemma.

Choose `M>=max_ab sup|gamma_ab|` on the full angle domain and set `K=kM`. For every real `v`,

`v^T Gamma_r v <= M(sum_a r_a|v_a|)^2 <= K sum_a r_a^2 v_a^2`.

Run HIER's induction with the stronger requirement

`Hess E_j + K diag(r_1^2,...,r_j^2)<0`.

At `j=1`, choose `r_1` small enough that `-r_1|b_1|+Kr_1^2<0`, also respecting HIER's bounds. The critical-point branch depends only on `E_j`. At its limit the upper-left block is the preceding strictly negative matrix. The off-diagonal block is `O(r_j)`. The last diagonal entry is `-r_j|g_j|+o(r_j)+Kr_j^2`. Its Schur complement is negative for sufficiently small positive `r_j`. Preserve all earlier size inequalities and proceed through the finite list. The displayed domination then gives `Hess E+Gamma_r<0`, and also `Hess E<0`. This supplies the missing uniformity without differentiating `gamma`.

**The flagged K7 reuse — HOLDS.** Define the *full* covariance matrix `C(eta)` of pinned forces at `H_l=exp(eta_l)`, in the fixed gauge coordinates used for that chart. It is smooth on the closed ball because the integration domain is a fixed compact product and `Z>=e^(-a_0)>0`. Set `L_C=sup||D C||`, `B_C=||C(0)||`. These are the constants for this chart; a numerical constant from a smaller tree slice is not silently reused.

For `r=||eta||_2<=r_0<=1`, `Lambda=max_l|lambda_head(l)|`, and a frozen unit colour `a`, let

`d_l=lambda_l(a-Ad(exp eta_l)a)`, `d_l^0=2lambda_l(a cross eta_l)`.

The integral remainder of the rotation exponential gives `||d||,||d^0||<=2Lambda r` and `||d-d^0||<=2Lambda r^2`. Split the difference of the two covariance quadratic forms by first replacing `C(eta)` with `C(0)`, and then replacing the two vectors. This gives

`|d^T C(eta)d-(d^0)^T C(0)d^0| <= (4L_C+8B_C)Lambda^2 r^3`.

At zero, constant-colour invariance makes `C(0)_(l,l')=C_0(l,l') I_3`, so the leading term is exactly `4 sum C_0(l,l') lambda_l lambda_l' eta_perp,l.eta_perp,l'`. No tree identity occurs. Likewise Taylor's formula for `Phi(eta)=F_c(exp eta)` gives the response error `6M_3 Lambda^2 r^3`, using `||eta'||<=2Lambda r` and `||eta''||<=4Lambda^2 r`. Hence both remainders apply to the arbitrary gauge used in O2-GR.

**O2-GR — HOLDS with these specifications.** In its construction, the leading variance is `4rho^2 VV_z`; only active heads occur, so its entries have the factors `r_i r_j`. HIER+ supplies a strict negative sum with the Hessian. After choosing the hierarchy, choose `rho>0` small enough for the stated cubic error to be at most `2mu_2 rho^2`. Continuity gives a ball of strict negativity for all `lambda` at once. These are finite matrix inequalities, so no directional compactness is omitted.

The covariant frame uses the already supplied K1 construction (row 1044, L262–277): two nonparallel tree holonomy axes determine an SO(3) frame; choose `H_0` in the ball and that open chart, freeze its inverse canonical gauge, and compose it with the canonical gauge of each pin. The inverse image of the ball is open, gauge invariant, nonempty, and carries the same strict matrix inequality. The SU(2) lift need only be local up to a common central sign, which cancels in every link and adjoint vector. Thus one continuous covariant frame on `Omega_12` and one pin set `P_2` work for all potentials. No uniformity in cell size or high probability follows.

## 5. Whole-boundary extension and its field class

**GR+ — HOLDS for the displayed FLOW extension.** On each free link, the two terms are the generators of fixed left and fixed right multiplication. Each preserves Haar measure, even though the right generator's left-coordinate expression contains `Ad(U_l)`. The full site-gauge generator differs from the frozen boundary move by `lambda_head D_l n` on pinned links only. Gauge invariance gives exactly the score in 6.1(b). The finite gauge map in 6.1(c) cancels the two endpoint exponentials; it holds for every boundary potential. FLOW then gives (d). All of this is independent of the sign of the response.

**The site-frame identification at L380–381 FAILS as a simultaneous assertion.** A separate transported vector on each incoming upper-face link need not be one vector at their common free tail. This distinction matters because row 1034 defines a frame move by `V_l=theta_l n_tail(l)` with one `n_x` per site (its L37–40).

Here is a hand witness within the stated box class. Take all sides equal to two, the free site `x=(1,1,1,1)`, and upper-face sites `y=(2,1,1,1)` and `z=(1,2,1,1)`. Normalize the potential to zero at the theorem's ground `(1,1,1,2)` and put `lambda_y=lambda_z=1`, with the free-site potential zero. At any fixed pin, choose the two free link values so that

`Ad(U_xy)n_y=i`, `Ad(U_xz)n_z=j`.

Such choices exist since rotations act transitively on unit axes. The conditional Wilson density has full support. The proposed extension has components `-i` and `-j`, while both scalar gradient components are `-1`. A common site vector would have to equal both `i` and `j`. Even allowing arbitrary scalar coefficients cannot make two noncollinear vectors share a common axis. Noncollinearity persists on an open set of free configurations.

Replace that remark by:

> On an incoming upper-face link, V+ is a right rotation by the boundary-site vector. This is a smooth divergence-free extension of class E-FLOW (also the explicitly enlarged right-rotation convention of E-FROZEN). It is not in general a single site-frame move at the free tails. No existence or nonexistence statement for a different whole-cell site frame follows.

**CONN+ — HOLDS under the stated coupling condition.** The source graph proof (row 1044, L280–305) establishes connectivity *before* collapsing U. Its essential edges join the two heads of adjacent links in one boundary plaquette. At the trivial pin, their direct coupling is `+/-beta w_p`. A link in a two-face has deterministic force, so its covariance row is zero. Otherwise it has one free plaquette, and isotropy bounds each relevant scalar force variance by `beta^2/3`. Thus all the chosen pairs are nonzero for `0<beta<3/2`. Every non-axis boundary edge is supplied by such a plaquette. Within each face, sites with two nonzero face coordinates connect by increasing missing coordinates and then decreasing to ones. Adjacent faces meet in sites of this type. Each remaining nonzero axis site connects to one of them by a transverse boundary edge. This connects the boundary minus 0, with no collapse of upper sites.

There are finitely many chosen pairs. Their couplings are real analytic in beta and nonzero on that interval. Each has isolated zeros, and their finite union has no accumulation in `(0,infinity)`. The same exceptional set can therefore be used for CONN+. No particular beta in `[2.3,2.6]` is supplied by this argument.

**O2-GR+ — HOLDS for V+ on the new set P_3, with the field-class correction above.** Ground one upper site, rather than all upper sites. Choose the finite pattern coefficients outside the finitely many zero sets of nonzero bilinear forms. Such a choice exists because their product is a nonzero real polynomial, which cannot vanish on an open Euclidean box (prove by induction on the number of variables). The connected graph gives HIER's required ordering. HIER+, the chart estimate, and the same continuous frame construction then yield one strictly negative matrix on all ungrounded head variables, with one open pin set.

Subtracting the ground value at **every** boundary site preserves `d lambda`. Use that normalized potential to define V+. The corner has no incoming pinned link and no adjacent free link. Its potential affects neither score nor response: the outgoing corner rotations form a gauge map, commuting with all other frame rotations on those links. This also kills every mixed term involving the corner direction. Hence the displayed bound with `sum_(Y+)(lambda_y-lambda_ground)^2` holds for every potential. It is a grounded norm, not literally the Euclidean squared distance to the space of constants. The zero space is exactly the stated one.

This closes the missing upper-gradient **response** estimate of CURL-P on P_3 and gives its written FLOW cost extension. It does not establish a common interior site frame for all these gradients, nor the upper-face sign on P' or P_2.

**CURL-Q — HOLDS on the explicitly stated space `(ker d)^perp + gradients`.** Use the linear rule specified in 6.4 and discard the corner value. The Hessian bilinear norm is at most `A_0`; the two score norms are at most `6 beta sqrt(N)||theta_c||` and `24 beta sqrt(N)||lambda||_(Y+)`. Cauchy–Schwarz for centered scores bounds their covariance by the product of these norms. With `||d lambda||<=4||lambda||_(Y+)`, this gives the stated `A_1` and `B_1` as bounds for the quadratic and *bilinear* terms, respectively. The cross term in `Q(theta_c+d lambda)` is twice that bilinear term.

Completing the square gives `(A_1+B_1^2/m_3)||theta_c||^2`. The least positive eigenvalue of the finite matrix `d^T d` gives `||theta_c||^2<=||d theta_c||^2/mu_1`. This is exactly the advertised constant. No estimate `mu_1` of order `S^(-2)` is needed. The optional identification of this space with all boundary fields uses the separately cited vanishing of first cohomology of the cubical boundary; this check does not rebuild that topological input. All gradients, including upper-face gradients, are covered without it.

## 6. AVG, MEAN, U(1), and the consumer

**AVG — HOLDS for H_c, as written.** For a deterministic scalar field theta in its field class, split the expectation into the good and bad pin sets. Apply the curl bound on the first and the uniform response bound on the second. This proves exactly

`E H_c <= p C||d theta||^2+(1-p)A_0||theta||^2`.

It is not a bound on an arbitrary chosen Q outside the good set. A random theta would instead require expectations of the two norms with their indicators. On `(ker d)^perp`, the *remainder furnished by this estimate* is absorbable into `c||d theta||^2` uniformly exactly when `(1-p)A_0<=c mu_1`. This is a limitation of that upper bound, not a necessary high-probability condition on every possible proof of the consumer. No upper or lower estimate for p is supplied by the note.

**MEAN — HOLDS for the response, not the full cost or an indicator of its sign.** The maps T commute and have coordinate period pi. For `i=j`, integrating `partial_i^2 f` over that coordinate gives zero by periodicity. For `i!=j`, integrate `partial_i partial_j f` in coordinate i first. The finite sum with coefficients `lambda_i lambda_j` also has zero integral. A continuous nonzero quadratic-direction Hessian must therefore take both signs. By gauge return the same statement holds for the response with the frozen colour carried along this orbit. In general `Q=H_c+Var(Psi)` has nonnegative, rather than zero, orbit mean. Neither statement transfers to a newly chosen covariant frame at each pin or to the ring law. The note's detailed scope paragraph has these restrictions; its short phrase “the sign has mean zero” should say “the response has mean zero.”

**U(1) control — HOLDS for a common constant axis.** Ad is trivial, the returned pin is unchanged, and the gauge-gradient extension has `Psi=Q=H_c=0`, including upper faces. The polynomial inverse proof works on products of circles because their rotation derivatives preserve coordinate polynomials and their common kernel is the constants. For an arbitrary scalar link field, differentiating the abelian plaquette phase gives direct cost at most `beta sum w_p(d theta)_p^2`. No hierarchy exists without a transverse colour, and no selective gain is obtained. Site-dependent signs of the axis are outside this control, as the target acknowledges.

**Meaning for the wall — HOLDS AFTER the field-class and infimum qualifications.** The actual consumer still requires a bound with its classical constant on the pins and cells carrying the ring measure, compatible across a tiling. Strict negativity on a chosen open set proves the existential local inequality, not that consumer. AVG leaves a mass error; the pin-set probability is unestimated; CURL-Q has a non-classical constant. The first unsupplied step in this proposed transfer is N1. N2, N3, O1, tiling compatibility, the gain across scales and W are not proved or refuted by this check. A torus-orbit descent of F_c supplies no mass gap.

## 7. Verdicts and limits

Checked line by line by Codex against the frozen target. The first false equality in its mathematical text is L134. The table distinguishes that failure from the surviving conclusions.

| Statement | Verdict | Exact scope or first correction |
|---|---|---|
| TAN; CUBE-EXT | HOLDS | Score zero at the base pin; derivative of that score need not vanish. |
| Cube GR variance and nonnegative cost at b_0=0 | HOLDS AFTER CORRECTION | L134's equality of cost and variance FAILS; replace it by the sign argument in section 2. |
| POLY | HOLDS AFTER CORRECTION | L182: degree three is for pinned forces. |
| EXT; A-FLOW | HOLDS | Every SU(2) pin and boundary field, infimum, exact stated variance constant; omit corner from the potential norm. L216's all-compact-group scope needs restriction. |
| EQ(i)–(iii) | HOLDS | Infimum and uniform finite-dimensional approximation; an exact non-strict consumer bound does not follow from approximation alone. |
| HIER+ | HOLDS AFTER CORRECTION | L236–240 for arbitrary angle dependence; uniform diagonal domination repairs it. |
| O2-GR; K7 in an arbitrary near-identity gauge | HOLDS | One P_2 and one covariant frame, all lower-support potentials; constants on the full chart. |
| AVG; MEAN | HOLDS | AVG bounds H_c; MEAN is an orbit integral of the response with a carried frozen colour. |
| GR+; O2-GR+ | HOLDS AFTER CORRECTION of field-class wording | The displayed FLOW identities and bound on P_3 hold. The simultaneous site-frame identification at L380–381 FAILS. |
| CURL-Q | HOLDS | Displayed constant on co-exact fields plus all gradients, with the written linear FLOW rule. |
| U(1) control | HOLDS | Common constant axis, zero gradient cost, no gain. |
| No movement of W; first missing consumer step N1 | HOLDS | Absence of a transfer proof, not an impossibility theorem. |

Source identity: target SHA-256 `a4e11e62779ba2bad300ac721a6d25b7f68508f33a94647d4320c29ddf1bee3a`. The target was read in full, using bounded ranges. Load-bearing input ranges read: FLOW L217–246; GR/CUBE-Z L25–116; Coulomb-frame L124–363 and L376–452; row 1041 L205–265; row 1044 L260–305 and L352–370; symmetry/regularity L33–44, L245–287 and L334–376; pinned-cell consumer L440–449 and L486–513. The wall's definition was checked in `parts/gap.md:15–26`. Older sources are used only for the statements specified above.

Not covered: row 1047; replay of the author's GUIDE run; any numeric integration, search, enumeration or computer-assisted proof; a Lean implementation; new estimates for beta, cell size, the pin-set probabilities or the classical constant; exact minimizer existence; a whole-cell site frame realizing V+; a new proof of boundary first-cohomology vanishing; continuum reconstruction or a mass gap. No Balaban paper was imported. Only the assigned report was changed; no source, registry, FINISH entry or status record was edited.

RESULT: HOLDS AFTER CORRECTION: the SU(2) FLOW infimum theorem, cube zero-score extension, lower-face O2 on P_2, and whole-boundary FLOW bound on P_3 survive the hand check; the cost/variance equality, degree and group scope, general HIER+ induction, exact-equivalence reading, and upper-face site-frame identification require the corrections above. The upper-gradient response gap closes on P_3, but a common interior site frame is not supplied. W does not move; N1 is the first missing consumer step. Research check only; no status or mass gap claimed.
