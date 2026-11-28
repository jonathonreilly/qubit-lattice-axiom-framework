# Re-gate of ref-chart.md — queue row 146
Provenance: OpenAI Codex (GPT-6; exact serving variant and configured effort are not exposed; row 146 requests xhigh), checkout `f7ff517e56aec86d278c3f121228d51d4604b0e5`; Sussman–Alpoge commit `31a47c543775`; research-text check, not an audit, grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline's reference problem, averaging construction, Proposition 2.4, prepared substitutions and pair decomposition. T. Balaban is credited for the background construction and the cited box-minimiser statement. The outline was fetched once to `/tmp/sa_ym4.tex`. All mathematical checks below are by hand; commands retrieve, locate, read and write text only.

## 1. Scope and premises — CORRECT-NO-ADVANCE

First failing step: none in attribution or scope. Read GOAL, the requested FINISH instructions and rows 133, 140, 143, 146, and the entire earlier gate in bounded ranges. The prescribed `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent from this checkout. This report checks the row-143 repairs, with P81, T4, RD, BC, GEO4 and SEP retained as named conditional inputs, not newly established results. The output did not previously exist.

Balaban CMP 102, Theorem 1 (p. 279), is a theorem on a prescribed constraint fibre; Proposition 8 (pp. 304–305) improves an already critical field's regularity; Section G (pp. 305–306) explicitly introduces the Landau gauge for analytic dependence. CMP 109, Section 2, (2.2)–(2.3) (pp. 265–266), minimises subject to the next average and explicitly keeps the axial-to-Landau transformation. Neither supplies the freed-box gap by itself. CMP 122 Proposition 1 is unavailable in the allowed paper folder and was not read: the claim checked here is the reconstruction of SA 17656, not verification of Balaban's unavailable proof.

## 2. Revised counterexample attempts — CORRECT-NO-ADVANCE

First failing step: none as conditional diagnostics, after the radius correction in Section 3 below. Attempt 1 correctly takes the curl after retaining the flat node coboundary. Attempt 2 correctly removes the variable-site gauge directions with the external tree edge. Attempts 3–4 now identify the actual potential and top-node responses; the second node jet cancels and the remaining terms have summable bounds, as checked below. Attempt 5 uses the gradient at the cycle centre, not a claim that the mild class is convex. The convex containing ball is what excludes a boundary minimiser. These are not exhaustive counterexample searches or independent evidence for H; their exclusions depend on H and its named premises. No counterexample to the curved minimiser theorem is established here.

## 3. Landau tangent, Ward identity and Theorem H — ADVANCE with an explicit radius correction

First substantive failing step in the new node-jet calculation: none. The earlier gate's missing representative identification is repaired. Two old local details still need correction: the use of Lemma R at `U=Phi(V)` needs `B alpha <= bar epsilon`, and its printed half-radius Cauchy circle does not give the stated constant 3. Both have explicit repairs below; neither requires a new mathematical premise.

**Matching T4.** `a3-derivative.md` (35), (37), Section 7.5 and its gate Section 7 bound `h=Da(0)w` and the node factor of each node's own level. They do not bound the raw fine tangent. Differentiating the product defining the top factor costs

`C exp(C r/(L-1)) sum_(n<j) L^n eta sup_pillar |h| <= C xi_j sup_pillar |h|`.

The pillar has bounded determining-metric diameter and comparable local scale. Thus the potential and node members in (T4), and their superpositions (6.1), are for the same Landau curve. This uses the product factors from the earlier derivative gate; dropping them at complex data would be incorrect. H itself uses a real base.

**WI and V'.** Gauge covariance gives `Dq_raw[X_chi]=delta_V chi` and gauge invariance gives `DA[X_chi]=0`. The multiplier identity therefore annihilates every node coboundary. Extend a node field to the other fine sites; no bound on that extension is needed. Put `A=sigma(c_-)`, `C=Ad(V_c)sigma(c_+)`. The second-order BCH expansion of

`v_-(t) exp(it w_c) V_c v_+(t)^(-1) V_c^(-1)`

has logarithmic second derivative

`delta_V tau + i([A,w_c]-[A,C]-[w_c,C])`.

The signs and the factor of one are correct. Differentiating the raw row along `exp(i eta a(tw))U` and eliminating `eta a''(0)` gives exactly (5.1'). WI kills only the term linear in `tau`; it does not kill the displayed quadratic first-jet term. No estimate of the second node jet is assumed. The same WI gives the repaired M identity `tr(lambda_c e)=DA[eta h_(c,e)]`, including away from a critical point of the *freed* problem.

**Uniform sums and flat comparison.** The node terms involving `w_c` have only `n_b` rows and contribute at most `8 C_M C_4 n_b^2 r ||w||_infinity^2`. The remaining product of two node jets costs at most `32 C_M C_4^2 n_b^2 exp(2 theta D_L) C_BC(C_Lambda M+6)^4 r ||w||_infinity^2`. These are exactly the two terms in `E_node`; the collar tower is included. The far-plaquette power count is `eta^2 xi^-2 * eta^2 xi^-2 * (xi/eta)^4=1`. The row Hessian cancels its scale against the potential's `xi^-1`. Both sums use the same tangent and fixed metric.

In the fixed real axial gauge on N, the row equation is `K Y'=w'^0+delta_(V^g)sigma'+m`. Subtracting `d sigma'` before taking curl is legitimate on all bonds of Lambda-plus. Its remainder is `(1-Ad V^g)sigma'`, bounded by `2 C_R bar a C_4 n_b ||w||_infinity/r_*`. The bound on `V^g-1` follows from the flat raw row's bounded analytic map and Schwarz, not from choosing a new datum representative. The tree zeros of `w'` and its Euclidean norm survive conjugation. E, P and two applications of the elementary square inequality give the printed leading `1/(4 C_P)` and the loss `8 |S| tilde_mu^2`. Substitution of `bar a=6 ell_N B alpha` gives the coefficients 36864 and 288 in C5. The added node loss in C5 is correct.

**Proved local repairs.** Replace the radius in H by

`alpha_*^new = min(alpha_*^printed, bar epsilon/(2 max(1,B)))`.

Use this smaller radius in every subsequent definition of `a_Lambda` and `epsilon_*`. This supplies Lemma R's explicit regularity hypothesis; the earlier gate requested this restriction and row 143 did not insert it. For R's second derivative, use Cauchy circles of radius tending to `r_*/(s sup|h|)`, obtaining `2 C_R(s sup|h|)^2/r_*^2`, and then relax 2 to 3. Its printed half-radius circle would give 8. This is the earlier gate's valid repair, still applicable because the map is bounded on the full open ball. With these corrections all terms absorb at `c_*=1/(8 C_P)`, uniformly in depth and volume. At flat data the multiplier and both mismatches vanish and the sharper constant `C_P^-1` follows exactly.

## 4. Theorem 2.4 — ADVANCE as an implication with the corrected radius

First failing step: none after Section 3's explicit radius correction; analyticity uses Section 5 below. SA 17656's clauses are matched, without claiming Balaban's sharper powers of M. The half-cell carrier comparison from the earlier gate is now included and identifies the actual mild class.

Steps 1–2 use the larger convex coordinate ball, not convexity of the plaquette class. For `rho_2=alpha_*/16<=1/64`, the coordinate velocity has norm at least `(1-4 rho_2)||w||_2`; the multiplier times coordinate acceleration is bounded by `2 n_b C_M B alpha_* C_X rho_2 ||w||_infinity^2<=c_*||w||_2^2/8`. Hence the ordinary coordinate Hessian is at least `c_*/2`. At the centre the gradient is at most `2 sqrt(n_b) C_M B C_c epsilon`; the compact-ball minimum therefore has `||u_Lambda||_2<=C_m epsilon<rho_1`. It is interior and, by the final epsilon restriction, in the mild class. Strict convexity proves uniqueness and the lower bound on the whole class via its slice representatives.

Step 6 uses the *full* variable tangent space: the tree slice plus gauge directions exhaust it, so every variable multiplier vanishes. Actual averaging carriers inside or crossing from a Lambda block read only variable rows; the distant collar tower does not read those bonds. Thus the indicated bare current vanishes. H supplies the axial Hessian. The fixed complex chart below supplies (e), with no appeal to complex minimisation. These conclusions remain implications from the listed inputs and geometry; this research check grants no retained status.

## 5. Section 8: G8, C, P, TL and D — ADVANCE with local constant clarifications

**G8 and the chart. First failing step: none.** Differentiating `F(a(B))` gives `omega D b(B)`, not the raw-coordinate multiplier. A box row is an interior top-level row and cannot feed a higher-level outward reduction. Therefore `D_(v_c^a)b` is exactly the single Pauli direction at c. This proves the printed G8 equality without a dexp factor. It would be false for a general outward datum coordinate; that is not the coordinate used here.

The norm comparison `|z|<=||z.sigma||<=sqrt(2)|z|` is correct for complex colour coordinates. It replaces the erroneous complex equality still appearing in Section 3's introductory convention; read that older equality only on the real Lie algebra. The contraction now works on the colour-Euclidean ball: its bond-supremum norm is at most `sqrt(2)rho_v`, below both the analytic radius and the Hessian tolerance. In the proof's invocation of CE use the actual maximum radius `rho=max(||beta||,||v||)<=min(r_B/8,rho_H)`, rather than literally setting `rho=rho_H` if the latter exceeds `r_B/8`. This yields the same quarter contraction. Take the harmless fixed restriction `r_B<=1/2` before defining these radii; it also supplies the small BCH balls used in (iv).

The centre displacement is at most `3rho_v/4`, so the contraction maps the closed ball into itself; its uniform convergence gives holomorphy. The real admission bound now includes exterior bonds: `C_(2.4)epsilon+4(1+C_v)rho_beta<=3a_Lambda/8`. The exterior tests remain within `epsilon_*`. Part (iii) is a bound on `Re(w*Hw)`, correctly distinguished from a complex bilinear square. In (iv), `4(1/32+sqrt(2)/16)<1/2` puts the BCH coordinate inside P. Here u' denotes the free axial-slice coordinates used by the reference integral; arbitrary nonzero tree coordinates would not lie in P as defined. Integrating the bounded gradient and then applying Schwarz twice is valid for the complete action, whose linear coefficient is zero.

P's overlap allowance also works: `4(sqrt(2)+8)<40`. Both critical points lie in the first chart's uniqueness ball; no dependence on the chosen splitting remains. Its admitted-pair and real-cutoff premises remain premises, not consequences of holomorphy. The earlier gate's exterior-cutoff allowance and matrix/colour factor have both been included.

**TL. First failure in the displayed auxiliary calculation:** step 4 asserts `|sum X_i|<=4 eta^2|nabla a|` for the transported plaquette insertions. With the forward covariant derivative of the cited T4 this omits the plaquette-curl correction. It is a bounded, explicitly repairable term, not a loss of the tail estimate. If `P_0` is the reference plaquette, the difference between the transported insertion sum and the forward curl consists of terms of size at most `C eta ||P_0-1|| |a|`. Consequently use

`||P_a-1|| <= ||P_0-1|| + C[eta^2|nabla a| + eta ||P_0-1|| |a| + eta^2|a|^2]`.

P81 and (31) bound this by `C_U^new eta^2 xi^-2`: the extra term is `C r(U_0)||B|| eta^3 xi^-3 <= C r(U_0)||B|| eta^2 xi^-2`. This is also the curl correction explicitly retained in `a3-derivative-gate.md` Section 7. Enlarge `C_U` accordingly before freezing `C_TL`. Where the action boundary needs the crude current estimate, include its absolute derivative constant in `C_deltaJ`: differentiating the at-most-six plaquette contributions gives `|delta J|<=C eta^-2 sup_stencil|h|<=C eta^-3 exp(-theta d)|e|`, and `xi=eta` there. Replace `r(U_0)` in the constant by its fixed uniform upper bound when calling the constant datum-independent.

With these clarifications the tail proof passes. Gauge invariance is used plaquette by plaquette to work in the Landau field; the complex dexp is now retained as Xi, with norm at most 2. The exact cutoff product rule gives a current term and a cutoff-difference term. Their topwise mesh counts are respectively

`eta^3 xi^-3 * eta xi^-1 * (xi/eta)^4 = 1`,

`eta * eta^2 xi^-2 * eta xi^-1 * (xi/eta)^4 = xi <= 1`.

The factors 16 and 192 include the trace, four positive bonds per site and six plaquettes per bond. No separate plaquette-gradient sum without the cutoff difference would work. Splitting the exponential and using BC' at half rate gives exactly the asserted `exp(-theta D_phi/2)` tail, with the enlarged constants. This is conditional on CUT, including its uniform Lipschitz constant and distance; the geometric claim `D_phi>=c_phi M Rcheck` is not proved merely by naming CUT.

**D. First failing step: none after these local clarifications.** The beta line has fixed radius `rho_beta/2`; its direction may be complex, since only the reference at z=0 must be real. The direct complex tail supplies the other coefficient bound. For (e), integrate TL along the *whole* u'-segment in P, using its uniform derivative bound there; a bound at u'=0 alone would not suffice. This gives the printed centred bound K'. Expanding the centred action in one scalar u'-direction, its linear coefficient costs `2TH/g`, while degrees at least two cost

`(2K'H^2/r^2) beta_A/(rho_beta/2-beta_A)`.

The positive real reference integral, with its exact Haar density, then gives the denominator ratio estimate. Both terms tend to zero under the stated scale/distance premises by elementary exponential domination. There is no shrinking analytic radius and no discarded cutoff linear term.

## 6. Proposition Ref — ADVANCE under ADM and CUT

First failing step: none with Section 5's corrected constants. The two constant actions cancel exactly in the centred reference law. D bounds the remaining exponent difference at every point of the real cutoff, and `delta_*<=log(3/2)` puts the denominator ratio within one half of 1. Thus `|log ratio|<=2(exp(delta_*)-1)<=4delta_*`, giving `|V_X^Ref|<=5delta_*`. This repairs both defects in the earlier gate's 9a and does not require a Gaussian comparison or separation of the full Q.

## 7. Proposition S' and the alleged refutation of (9.1)

**S' (admission only): ADVANCE. First failing step: none under GP, real prepared admission I5, and the fixed geometry.** In the box the reference problem has scale 1. The potential part of a shell row is consequently `O(xi_j ||B||)`, while both endpoint gauge factors are only `O(||B||)`. For the latter, combine the T4 node value with the downward contour recursion: the intermediate increments are `O(||B|| t/s)` and their geometric sum is bounded independently of depth. This is a comparison of gauges relative to the same real canonical reference; it does not identify that gauge with a node-fixing one.

In the displayed product estimate the two endpoint terms cost `6 C_w||B||`, the potential term costs `4 C_R C_a||B||/r_*`, and the logarithm costs a further factor 2. These give exactly C_S. The conjugation by the stored real `exp(ig B_fluc)` is unitary, so it preserves this bound. Shrinking the coupling puts the prepared datum in the P81 ball about its real prepared datum. It proves admission and holomorphy of that prepared substitution; the note correctly does not infer admission of the four meet data from it.

**Claim that (9.1) is refuted: WRONG. First failing step:** the passage from the exact conjugation identity to an admitted reference whose innermost shell row stays farther than `C_S xi_j` from the centre. The note explicitly acknowledges that its needed size step is stated rather than displayed. An upper bound `|u_Lambda(b)|<=C_m epsilon`, or the observation that a fundamental cycle has area up to A_M, supplies no lower bound on any critical reference. In particular it does not produce `|u_Lambda(b)|>C_cross epsilon`, does not rule out cancellation by the two internal-block holonomies, and does not exhibit an admissible core crossing that bond. A failed proof of (9.1) is not a refutation of it.

The exact identity itself passes for the **specified** U-circ representative: the tree recursion forces the constant box gauge g, the block-constant extension preserves every comb constraint, and covariance/uniqueness gives `V_0(p')(c)=g V_0(p)(c) g^-1` on rows with both endpoints in those blocks. Thus the derivative is indeed `(1-Ad V_0(c))Z`. This identifies a possible obstruction. It is not yet a counterexample on the actual domain. Moreover, SA 17591–17596 does not expressly prescribe U-circ for this substitution; SA 9668 describes it and the following remark also describes an alternative gauge. State the chosen representative as a condition, not as an additional source instruction.

**Visible repair of the claim:** replace “REFUTED” by “not established in U-circ; the conjugation family yields the following counterexample criterion.” Supply admitted references and shell rows with

`||(1-Ad V_0(c))Z|| / xi_j -> infinity`

and admissible pair curves whose size is controlled by their parameter, uniformly in j. Choose a nonzero parameter small enough that the quadratic remainder is at most half the linear term. If beta_A is held fixed as the domain radius, choose the parameter relative to that radius and compare the *finite* increment with `C_S xi_j beta_A`; differentiating an inequality with a fixed beta_A does not give a derivative bound. Alternatively state and prove a Lipschitz version with beta_A proportional to the curve parameter. No such lower-bound family is constructed in row 143 or in this report. The weaker S' estimate and the Landau-representative estimate with xi_j remain valid regardless.

## 8. Proposition I' and the proposed change of variables

**The displayed upper bound in I': ADVANCE conditionally; first failing step none for the named prepared chart.** On its admitted segment,

`xi_y |Delta a(y)| <= C_4 C_S beta_A sum_c exp(-theta d(y,y_c)) <= 8 C_4 C_S C_BC' beta_A`.

This is the Landau-potential difference in a chart based at the real prepared reference. It neither bounds an un-gauged raw difference nor identifies a different truncated inner background. The stored-core rows have zero datum increment. No xi_j factor is available from S' alone.

**“Moves at first order” and the claimed refutation of inner suppression: WRONG as established conclusions.** The first failing step is again a lower bound: mechanism (a) assumes the unproved size assertion of 9b; mechanism (b) calls `sigma(y_1)-sigma(y_2)` generically order one, although T4 supplies only an upper bound. It also does not demonstrate that this difference survives in the actual inner gauge-invariant read. The proved `O(beta_A)` bound does not exclude a sharper bound. Withdraw the assertion that a counterexample has already been given. It is correct to keep Inn open because its required estimate and matching have not been proved.

RAD is at most a proposed sufficient size condition, not a necessary condition established by I'. For an analytic inner activity the denominator in a Cauchy estimate is the distance of its real read to the boundary of the full inner domain. Replace RAD's radius comparison by an explicit interior-margin premise, controlling every potential/current/tower norm read by that domain. A nominal radius alone is not that margin. This was requested in the earlier gate's 9c and remains unsupplied.

**The proposed core-only substitution has an additional algebraic failure.** Its first incorrect equality is that transforming the core alone makes the whole prepared datum the u_B-transform of Landau shells with the *same* stored B_fluc. On a shell bond c, the actual field is

`V_shell^circ(c)=exp(ig B_fluc(c)) u_-(c) W(c) u_+(c)^(-1)`.

Pulling back its gauge gives exactly

`u_-^(-1) V_shell^circ u_+ = exp(ig Ad(u_-^(-1)) B_fluc) W`.

It is not `exp(ig B_fluc)W` unless the factors commute. The visible algebraic repair is to transform the fluctuation variables as well:

`B_fluc^L(c)=Ad(u_-(c)^(-1)) B_fluc^circ(c)`,
`V_core^L=(V_core^circ)^(u^(-1))`.

At real pairs these adjoint changes preserve bond norms, zero tree-fluctuation values and the corresponding Lebesgue measure; the core gauge preserves Haar measure. Those facts do not prove covariance of the stored inner tree/reference constraints or last-shell tests, nor equality and holomorphic continuation of the complete operation. In a complex gauge the real integration domain is not automatically preserved. These matching obligations remain open. In the corrected variables the *shell-data* increment has the Landau xi_j factor at fixed B_fluc^L; restoring suppression in the actual integral still requires the missing equivalence of operations. The earlier gate's request to carry the representative through the stored fields has therefore not been completed.

## 9. Section 9d: the inner Wilson factor and the claimed outline gap

**Withdrawal of the old regular-plaquette argument: CORRECT-NO-ADVANCE.** No failure in withdrawing it or in leaving the comparison open. SA 18061–18075 retains the real inner Wilson factor with the old large plaquettes. It cannot be replaced by an arbitrary regular prepared background. The exact phrase concerning a truncated prepared sequence occurs at SA 18070; searches of truncation/preparation and the related U-double-prime passages did not supply a complete row/datum definition of this real comparison background. This is a specification/matching gap in the passages checked, not a counterexample to the outline theorem.

**The replacement dichotomy in 9d: WRONG.** Its first unsupported step is that reading moving shells implies a first-order inner change, which inherits Section 8's unproved lower-bound assertion. Independently, pair independence of the *real reference* does not make the inner contribution to V_X vanish. SA 17889–17902 explicitly compares the actual complex prepared action with that real reference:

`A(x'' phi_c,U''(p)) - A(x'' phi_c,U''(xi))`.

Even if the second term depends on xi alone, the first can vary with p. It is precisely this difference that requires the bound. SA 17919–17924 also says the new argument, gauge and stored data are formed together; a comparison which freezes one of them in a different representative must first match that rule.

**Visible repair:** specify (i) the truncated determining sequence, (ii) every real determining row and collar lift as a function of xi alone, (iii) the actual complex read and its identification with the integrand, and (iv) the weighted difference of these two actions. Retain the exact real inner action in Phi-circle. On old large plaquettes a regular-reference small-curvature factor is unavailable unless independently proved in their own local units. SA 19281–19315 gives an own-layer action/volume bound for the real source term; that alone is not a derivative/locality bound for this complex difference. Thus the conclusion “Inn remains open” is justified, while 9d's proposed two-case argument does not close or refute it.

## 10. The 2.8-T-complex replacements

**Matrix Hessian constants: ADVANCE with the following transport clarification.** The first literal slip is “at most three factors” for all insertions. With left bond variations one of the four transported insertions uses the full plaquette transport, of length four. The same proposed `kappa_c=3` nevertheless works under the printed smallness restrictions: its condition number is at most

`(6/5)^4 exp(8 eta sup|a|) <= (6/5)^4 (11/10)^2 < 3`,

because `6 eta sup|a|<=log(11/10)`. The numerator of the last rational product is 156816 and the denominator 62500, so it is strictly below 3 by hand. No length-dependent loss is hidden. The gauge factors telescope along the transport; GP is needed at every bare endpoint, not just at tops.

Use the convention `P(t)=P exp(it X_1+t^2 X_2+O(t^3))`. Then `|X_1|<=4 kappa_c |A|_p`, `|X_2|<=6 kappa_c^2 |A|_p^2`, and `tr X_2=0`. Directly differentiating gives the printed trace identity. Its error is bounded by `(12+16)kappa_c^2 ||P-1|| |A|_p^2<=32kappa_c^2 ||P-1|| |A|_p^2`; the first derivative is bounded by `4kappa_c ||P-1|| |A|_p`. These are estimates for a complex bilinear Hessian, not a positive Hermitian quadratic energy. The acceleration contribution `K_2` is correctly retained. The scalar SL(2,C) determinant estimate and the complex integral Taylor remainder also survive.

**Use of TQ at a complex base: CORRECT-NO-ADVANCE without the matched family.** The matrix estimates do not supply that family. TQ's proof is a fixed-real-reference Cauchy estimate; moving a point inside its roomy polydisc is allowed, but identifying its derivatives with the Landau chart re-centred at S(p) is a separate step. The phrase “a Cauchy estimate” cannot itself establish that identification. A visible local route is to retain one real-reference prepared Landau family a(beta,u), subtract its value at u=0 by the analytic BCH product, and then conjugate by the *fixed-in-u* base gauge. This yields a curve through S(p) with controlled first and second derivatives on a smaller fixed ball. One must still match its quadratic form with the Q used in the real splitting, including all gauge/coordinate terms. This is part of the Gaussian-family obligation already left open by row 143. The algebraic constants above pass; no complete R9/2.8 complex theorem is discharged by them.

**Power count: ADVANCE as the collection implication. First failing step: none.** With `p=max(p_0+2r,q)`, the combined amplitude is `O(g(1+ell)^p)`. Quadratic uses cost at most `2 max(0,q-p_0-2r)` extra logarithmic powers over the corrected real bound, and linear uses cost no more. The separate cubic fluctuation remainder already has its explicit positive power of g. Fixing these powers and constants before the ceiling preserves the exponential-domination argument. SA 6033 and 17828–17831 explicitly permit q to exceed the old regularity exponent, so the withdrawn same-order assertion must indeed stay withdrawn.

**I5's xi-squared factor for S: ADVANCE with the same curl correction as TL.** The first inaccurate displayed estimate is again the omission of `C eta ||P_0-1|| |a|` when bounding the plaquette insertion sum by a forward gradient. Including it, on the box where S's reference scale is 1, gives

`||P_(S(p))-1|| <= C(M)[epsilon_k + beta_A + beta_A^2 + epsilon_k beta_A] eta^2`

in the controlled complex gauge, and hence `<=C'(M)(epsilon_k+beta_A) eta^2` on the smaller ball. The complex conjugator has bounded condition number. Since curvature in the units of a prepared top is the bare curvature times `(xi_y/eta)^2`, this proves

`a_S(y) <= C'(M)(epsilon_k+beta_A) xi_y^2`.

Thus the factor xi_y^2 is sound and does not require the disputed raw shell-row factor xi_j. Increase the displayed fixed curvature constants before the ceiling; the literal coefficients 4 and 20 are not justified by dropping the curvature correction. S' supplies admission of the prepared substitution given real I5. It still supplies neither the four meet comparisons nor every clause of I5 on its own.

**I1, LM/I4, and the complete theorem.** I4 and the local complete-stationarity identities follow conditionally from H/C; analytic identities may be continued only on their established common domains. Lemma 6c-complex is expressly unrepaired. Normalise the collar datum before inserting it into the joined chart, and use the added-row mismatch set for the W4/W3 decay, as the earlier gate required. The Gaussian family still needs its fixed exterior radius and equality with the literal real full Q. These are open premises, so the full 2.8-T-complex conclusion is CORRECT-NO-ADVANCE as an acknowledged programme, not an established estimate.

## 11. Disposition and recovery checkpoint

| Row-143 part | Verdict | First failure / qualification |
|---|---|---|
| Section 2 attempts | CORRECT-NO-ADVANCE | No independent counterexample proof; the conditional gap argument now works. |
| WI, V', M, T4 matching, H | ADVANCE with local correction | No new node-jet failure; insert the missing regularity-radius restriction and use the full Cauchy radius. |
| Theorem 2.4 | ADVANCE as an implication | None after that correction and the chart proof. CMP 122's proof was unavailable. |
| G8, C and P | ADVANCE | None after the stated norm/radius clarifications; ADM remains explicit. |
| TL, D, Ref | ADVANCE with local correction | Retain the forward-curl curvature term and enlarge constants; CUT and its separation remain premises. |
| S' admission | ADVANCE conditionally | None for the named prepared chart; meet admission remains separate. |
| Refutation of (9.1) | WRONG | No admitted lower-bound reference is exhibited. Exact conjugation alone is insufficient. |
| I' upper estimate | ADVANCE conditionally | None for the prepared Landau potential. It does not identify the inner read. |
| First-order inner change; core-only repair | WRONG | Missing lower bound; additionally the shell fluctuations must be conjugated. |
| 9d | CORRECT-NO-ADVANCE for leaving the gap open; WRONG for its dichotomy | An independent real reference does not remove the complex action difference. |
| Hessian constants, power count, xi-squared curvature | ADVANCE with local corrections | Four-factor transport and curved-curl terms retained; matched complex/Q family still required. |
| Complete Pre/Inn/Act conclusion | CORRECT-NO-ADVANCE as open work | Several independent comparisons remain open; an ordering of these gaps is not a proof. |

The breaking defects are grouped into four items: (1) the unproved lower bounds behind both “refutations”; (2) the incomplete change of variables and missing inner-domain margin; (3) the actual inner Wilson read/comparison, including 9d's invalid dichotomy; (4) the still-unmatched complex prepared/meet/Q families. The radius, Cauchy, forward-curl and short-transport corrections are explicit local repairs written above. None refutes the real curved gap or the fixed-radius reference-law mechanism.

The source Outcome, Section 10 table and final verdict must not say that (9.1) or literal inner suppression has been refuted, or that first-order motion of the inner read has been proved. What survives is a conditional real freed-box gap, its minimiser/chart consequence, the fixed-radius reference-law bound, and a weaker prepared-data admission estimate. The full pointwise-pair bound remains open through Pre, Inn and Act. No consumer file or status was edited.

Current checkpoint: all requested row-143 sections and their earlier-gate repair requests have been covered, including the original gate in full. Sources remain identified by the pinned checkout and the single fetched outline; the supporting excerpts used are the a3 Landau identities/T4 and their gate, a1 Section 9.1 and its gate, the 2.13 comparison proof, the 2.8 LM/TQ/R9 calculations and their gate, Balaban CMP 102/109 passages listed in Section 1, and the cited SA ranges. Reuse these findings at this revision. The next mathematical decisions are to construct an actual admitted lower-bound shell family or withdraw the refutation; to specify and compare the real inner Wilson read; and to supply the correctly transformed, admitted prepared/meet/Q families. The unproved routes are preserved explicitly. Only `gates/ref-chart-regate.md` was written; no editable prompt file, source proof, audit, ledger, commit, PR or external post was changed, and no subagent or computational proof was used.

Final source check: HEAD remains `f7ff517e56aec86d278c3f121228d51d4604b0e5`; the lane's tracked files have no differences from that commit, and Git reports only this new report. SHA-256: `library/ref-chart.md` = `a4492cd24cc9024098b796e647a68de6f7869edca891ae86179b4bfdbb2b635d`; fetched outline = `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. These are source-identity checks, not mathematical evidence.
