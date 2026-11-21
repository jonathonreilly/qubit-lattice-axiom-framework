# Gate of a3-clauses, queue row 108
Provenance: OpenAI Codex (GPT-6; exact backend identifier not exposed), requested effort xhigh; checkout `ea8962a25baee6aefb6a460105d3dc7b21125cbb`; Sussman–Alpoge commit `31a47c543775`; hand mathematical review, research text, not an audit and grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's statements, regular-pair class, operators and conventions used below. Claude wrote `library/a3-clauses.md` and `library/p82-curved.md`; the real package is read with the repairs in `gates/p82-curved-gate.md`. Balaban's architecture is used through those stated library inputs. The outline was fetched once to `/tmp/sa_ym4.tex`; its line numbers below refer to that pinned text. No numerical or computer-assisted proof step is used.

Scope: Sections 1–5 of `library/a3-clauses.md`, with verdicts on the implications actually stated. Row 105 counting is the decision affected. Existing real and flat packages remain explicit inputs; no independent-current interpretation is identified with the outline merely because it agrees on shell. Only this report is edited. The entry-point path `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent in this checkout.

## 1. Clauses and scope — CORRECT-NO-ADVANCE

First failing step: none in the identification of the requested clauses (source lines 14–26). SA 9678–9744 distinguishes continuation in the datum at a real reference from a complex-reference pair theorem, and puts periodisation in Theorem 4's next paragraph. The exclusions of the pointed-core claims of Theorems 5 and 6 are appropriate to this item. The earlier derivative gate's two missing inputs and its rejection of mere strip holomorphy are accurately reported.

The sentence at source line 12 about Theorem 4 standing “in full” must retain the qualifications of Sections 3–4: it can only mean an implication on the specified regular class and for a specified pair operator. Agreement on shell does not identify an off-shell system. Section 4 is checked separately below; this paragraph supplies no proof or status by itself.

## 2. Theorem Pi — ADVANCE as an implication

First failing step: none. The inputs are precisely (I1), identification with the flat saddle lift, and (I2), the repaired Theorem P on every admissible torus. This does repair the depth-uniformity defect in the earlier 9.2 argument.

- **Setting and (2.1), lines 30–43.** On the single lattice every top has scale one; there is no sum over the bare bonds in applying the weighted supremum estimate to one counting row source. The source norm is one. Moving from tops to bond midpoints costs a bounded distance, hence the factor `exp(2 theta)`. Fix, for example, the unused Hölder exponent to `1/2` in Theorem P to make these value-bound constants depend on L only. The gap is vacuous and the nonwrapping floor is fixed in top units. Neither the number of intra-block sites nor k enters this argument. Invertibility, including removal of constant modes by K and Q', is an input already supplied by Theorem P.
- **Covering identity, lines 45–53.** “Translation-invariant stencil” here means equivariant under integer top-lattice translations, with the fine site's position within its block retained as a species; it does not mean invariance under arbitrary bare translations. Each primitive operator and its transpose commutes with covering pullback because the blocks, paths and pairing weights are copied exactly. Its physical range is bounded by a geometric sum of sub-block sizes, uniformly in k. Inverses then commute with pullback by uniqueness. This applies to the scalar Gram inverse before R and to the saddle inverse after R; no locality of R itself is assumed. Pullback of a counting delta is the sum of its copies, with no covering-degree factor. This proves (2.2).
- **Image sum, lines 55–60.** Choose for each nonzero image class a representative of least infinity norm. Distinct classes give distinct nonzero lattice points, and the triangle inequality bounds the relevant torus distance below by that norm minus `ell/2`. The shell count is exactly `64 s^3+16 s`. The numerical constant can be verified without evaluation of a series: for `q=exp(-1)<3/8`, differentiating the geometric series three times gives `sum(s>=1) s^3 q^(s-1)=(1+4q+q^2)/(1-q)^4 <10816/625<50`. The inequality `exp(1)>8/3` follows already from the first five positive Taylor terms. Thus the stated `4000 C1` is more than sufficient, uniformly in the cover degree and depth.
- **Limit, lines 62–75.** Two admissible integer sides have an admissible common multiple. The image bound therefore gives a Cauchy family for each fixed pair of bonds, not merely a convergent subsequence. Translation covariance and decay pass to this limit. For periodisation, the half-open box centred at `b'-c` supplies one representative per image class; extending the summand by zero outside that box gives the fixed summable majorant `C1 exp(-theta |b'-c-n|_infty)`. Every fixed image eventually occurs. Dominated convergence proves the full image identity. For `theta ell<1`, the two value bounds give `2 C1`, absorbed by the stated larger constant. The comparison estimate forces uniqueness.

The rate is the fixed walk rate divided by two, and the same is true at every k. The conclusion is a kernel and its periodisations; identification with a separately constructed infinite-volume Hilbert-space inverse is neither needed nor claimed. The extension in line 77 applies to other blocks only after inserting their own source/output normalizations and uniform exponential bounds; it supplies no new such bounds.

## 3. Theorem P^c and Lemma 6.1′ — ADVANCE as implications

First failing step: none in the complex extension with the repaired real inputs. In particular, neither positivity of a complex transpose form nor Kato at complex links is used. The separate curvature bounds in this section's class are additional to the real theorem's Reg condition and must be retained.

**Class, definitions, Steps 1–2 (lines 83–118).** Strict inequalities in the complex perturbation coordinates give an open neighbourhood of each admitted configuration, keeping its real representative fixed. All gauges used for estimates are real and therefore preserve the Hermitian norm. In such a gauge, the product logarithm obeys

\[
 m|\widehat A|+m^2|\nabla\widehat A|
 \le C_L(\alpha_0+\alpha_1).
\]

Indeed `∇(Ad(g)A')` is its covariant difference plus an `O(|A_0||A'|)` term; differentiating each convergent BCH monomial leaves a first difference on one factor. The extra η in nonlinear terms is bounded by m. This proves (3.1), including its derivative member. The global H² norm comparison also uses this derivative member, not just the first-difference inequality quoted at line 89; in bare cells the finite-mesh norm equivalence supplies it directly.

In one common cell gauge the j-step averaging errors are `C_L delta L^(q-j)` at step q. Telescoping the Jacobians and endpoint transports gives an error product bounded by `exp(C_L delta/(L-1))`, for complex matrices too. Row and column sums are submultiplicative for their absolute norms. Thus the row factors are `s_j`, the fine coefficient/column factors are `eta^4 s_j^-3`, and pillar coefficients are `eta^4 m_y^-4`, with only adjacent-scale losses at seams. For the transpose of Q', disjoint pillars and bounded complex transports give the needed upper bound; Hermitian isometry is not asserted. Integration by parts uses the bilinear transpose, and its pairing is bounded by the two Hermitian norms. Expanding the second-order scalar block gives `Acal D`, `D Acal` and the derivative of its coefficient, controlled by the just-proved first-difference bound. These check all seven items of Step 2.

There is also a direct check of the top-mass independence in line 91. Write `A_s=Delta+Q'^T a Q'`. In the scalar equations with source `(g,0,0)`, `Q'lambda=0`, so the first equation is `h+Delta lambda=g`; in the second, `Delta h=Q'^T(mu-a Q'h)`. Changing a only changes mu. Thus the h block and R are independent of a wherever the scalar systems are invertible, over the complex numbers as well. Near the real reference scalar elimination identifies this block with the displayed Gram formula. The identity theorem on the small perturbation ball then gives its canonical holomorphic continuation. It is not a choice of a new projection or a new slice.

**Step 3, especially bare cells (lines 120–128).** Use the real gate's enlarged cells, including their whole read collars. An interior cell has a flat inverse conjugated by a real gauge. A bare cell has `m=eta`, `Q'=I`, `K=eta I`, with the actual real transports retained; for the plaquette version retain its actual real plaquette curl. In bare scaling,

\[
 \|D_{\mathbf U}-D_U\|_{2\to2}\le C\alpha_1\eta^{-1},\qquad
 \|A_s(\mathbf U)-A_s(U)\|_{2\to2}\le C\alpha_1\eta^{-2}.
\]

The second inequality follows by expanding the product of two first differences, each bounded by `C/eta`; it needs no derivative of A'. Each plaquette transport is a product of at most four links, so its complex-minus-real difference obeys the same first-order estimate. Pairing a vector quadratic-form difference against two test fields and integrating one difference by parts makes it `O(alpha_1)` in the E norms. The scalar estimate is `O(alpha_1)` from H² to L² and in the transposed block. All remaining bare blocks either have these bounds or are unchanged. Arbitrarily rough real bare links therefore cause no mesh loss.

The cutoff product rules remain algebraic, with transport norm at most `1+C alpha_1`. Pairing smooth-cutoff assembly against a test field and using bounded overlap gives

\[
 \|\mathbb R^{\mathsf c}\|
 \le C_L B_LN_L\{M^{-1}+\alpha_0+\alpha_1\}.
\]

Choose M with spare room in the commutator bound, then decrease the two radii. This proves the right inverse by its Neumann series; finite dimension makes it the inverse. Apply the same argument to the scalar subsystem. For decay, apply the series to an **already supported** source. Its nth term cannot reach farther than `(n+1)D_L M`, and its norm is bounded by `C 4^-n`. This is precisely the repaired real proof; no sharp cutoff is asserted bounded on a dual Sobolev space.

**Step 4 (line 130).** Eliminating the scalar subsystem gives `h=(1-R)D^T A`. The remaining first row is `(d^T d+DRD^T+K^T K)A-K^T nu=f`, and the last row is `-KA=g_5`. Adding `K^T` times the constraint gives the source transformation `(f,b) -> (f+K^T b,-b)` with the displayed signs. No positivity is needed. Solving for arbitrary b proves that K is onto.

**Lemma 6.1′ (lines 132–156).** Let `A_*=r^-2 ||u||_2+r^2 ||g||_infty` in this paragraph only. Real adjoint transports are unitary on the complexified colour space, so taking the real part of the Hermitian pairing proves `Delta|u_mu| <= |Delta_U u_mu|`. At a zero of u the left side is nonpositive. This Kato step is legitimate for complex-valued u at real U.

For `d<32 eta`, the single-site L² bound and the two-site difference bound give both weighted maxima at most `C r^-2 ||u||_2`: in the gradient term the factor is `d^3 eta^-3/r^2`. For larger d, on the smaller cube and its stencil neighbourhood,

\[
 |u|\le C r^2d^{-2}\Phi,\quad
 |\nabla u|\le C r^2d^{-3}\Psi,\quad
 |Eu|\le Ca(d^{-2}\Phi+rd^{-3}\Psi).
\]

The value Green–Poisson bound multiplied by `d^2/r^2` therefore gives

\[
 \Phi\le C A_*+Ca(\Phi+\Psi).
\]

The critical powers are `d^4/r^2`: multiplying the two error terms leaves `d^2/r^2` and `d/r`, both at most one. After writing `Delta_U=Delta+B nabla+C_0`, with the finite-range coefficients bounded by `Ca/r` and `Ca/r^2`, the central-gradient estimate multiplied by `d^3/r^2` gives

\[
 \Psi\le C\Phi+C A_*+Ca(\Phi+\Psi).
\]

**Substitute the first inequality into the second before adding them.** The resulting coefficient of `Phi+Psi` is `C' a`, not the order-one coefficient of Phi in the gradient estimate. Choosing `C'a<=1/2` closes both maxima simultaneously. Any central-gradient cube only a bounded number of mesh steps wide can instead be handled by the preceding finite-mesh estimate. This avoids a dependence on the precise integer rounding of the cubes.

On the intermediate cube this bounds the ordinary forcing by `C(r^-4 ||u||_2+||g||_infty)`. The supplied free estimate with zero divergence source gives the gradient Hölder member. Its bounded-forcing contribution is `C ||Delta u||_infty t(1+log(r/t)) <= C_beta ||Delta u||_infty r^(1-beta)t^beta`; no Hölder regularity of g is assumed. The ordinary-to-real-covariant correction has first difference bounded by `C(|nabla A||u|+|A||nabla u|)`. Real path transport differs from one by `Ca t/r`. This proves all of (6.1), not just its value member.

**Steps 5–6 (lines 158–171).** Pairing the opposite shifts is essential. With tildes denoting real parallel transport, the linear complex difference is exactly

\[
 -i\sum_\nu\left\{\operatorname{ad}A'_\nu\nabla_{U,\nu}f
 +\operatorname{ad}\frac{A'_\nu-\widetilde A'_\nu}{\eta}\,f
 +\operatorname{ad}\widetilde A'_\nu\,
                  \frac{f-\widetilde f_-}{\eta}\right\}.
\]

The quadratic remainder is bounded by `C |A'|^2` times the maximum of |f| on the neighbouring stencil. Thus there is no `alpha_1/(eta m)` zeroth-order loss: the error is bounded by `C alpha_1(m^-1 |nabla_U f|+m^-2 |f|)` on that stencil. This is exactly Lemma 6.1′'s permitted error. First apply it to the scalar h equation to bound Dh, then to the vector equation; reversing that order would be circular. The forcing powers remain `m^-4` and `m^-3`, respectively. At `m<=64L eta` the finite-mesh argument suffices, including arbitrary bare boundaries.

For the **complex** gradient output one must also add `nabla_Ubold f-nabla_U f`. Its coefficient is `O(alpha_1/m)` and its first difference is `O(alpha_1/m^2)` in the real gauge. The value/gradient estimates just proved therefore bound its Hölder quotient. For the path comparison the product norm is at most `exp(C alpha_1 t/m)` and its difference from the real transport at most `C alpha_1 t/m` for `t<=m`. Both corrections are harmless, so the proof really does give the claimed complex-covariant Hölder member.

The plaquette-minus-forward curl has finite-range coefficients `C alpha_0 eta/m^2`; expanding its quadratic form gives coefficients `C alpha_0/m^2`, without differentiating curvature. Bare cells were already handled with the exact models. Supported-source summation uses the unchanged geometry and the fixed gap, and phase alignment with finitely many colour coordinates gives **row** sums only. The scalar h output separately gives `D(1-R)D^T:X_w->F_w`. Finally, all finite matrix entries are holomorphic and the established inverses have nonzero determinants on the open class. This proves (g). No complex Kato inequality, column estimate, or bound on the actual current was smuggled into this argument.

## 4. Pair system — ADVANCE for Theorem Sigma; WRONG for a literal identification with (B)

First failing step: **line 178 if (B) means the actual SA second system**, rather than the explicitly simplified system subsequently defined at line 191. The assertion that the independent current enters only through the multiplier forcing overlooks its occurrence in H and S. The qualification about the current correction in G does not specify the missing terms. This is a matching defect, not a counterexample to Theorem Sigma. The latter and its applications to (A) and to the system actually defined at line 191 pass; their first failing step is none.

**(A) and the specified alternative.** Call the latter **B0** in this report: `F_U=K_U^T H_U^T`, `Pi=0`, with H taken from Section 3 and hence independent of J. Its (H1) follows by composing the multiplier block `-H^T:F_w->Y_w` with `K^T:Y_w->F_w`; (H2) is immediate. No column estimate is being inferred. (A) has `F_U=I`, `Pi=0`.

The off-shell distinction is real. On the flat single lattice at positive depth there are more fine bonds than determining rows. Since K is onto, choose a nonzero real j in `ker K`; it is orthogonal to `ran K^T` in the fine pairing, so it cannot lie in that range. Scale j to meet any positive current ceiling. At B=0, (A) cannot have a=0, since its first equation would require `j=K^T lambda`; its first current derivative is `-Tj`, which is nonzero for the same reason. B0 has exactly `a=0, lambda=H^T j`. If `j=K^T z`, then `H^T j=z` because `KH=I`, and the two forcing operators coincide. Thus they agree in that case as entire specified equations, not just to first order. This verifies the claimed ambiguity without any dimension enumeration by a machine. It does not identify either choice with every physical off-shell system.

**D1 — exact repair of the (B) matching calculation.** The outline at SA 10148–10158 defines `G=(G_0^-1-E[J])^-1`, where `E[J]=Delta'_pi[J]`, and constructs H from G. Its second system at SA 10414–10436 uses **H0 and Gtilde** in the field equation, but **H and S** in the multiplier equation. In common raw-row coordinates write

\[
 L_0=\Delta^{\rm W}+DRD^{\mathsf T},\quad
 G_0=(L_0+K^{\mathsf T}\mathsf a K)^{-1},\quad
 G=(G_0^{-1}-E[J])^{-1},\quad
 S=(KGK^{\mathsf T})^{-1},\quad H=GK^{\mathsf T}S,
\]

and define `H0`, `S0`, `T0=G0-H0 K G0` using G0. Put `b=B'-C(x)` and `q=N(x)-C'(x)^T lambda`. The field equation `x=H0 b-T0 q` gives

\[
 Kx=b,\qquad L_0x+q=K^{\mathsf T}\mu,
 \quad \mu=(S_0-\mathsf a)b+H_0^{\mathsf T}q.
\]

Since `H^T(L0-E)=(S-a)K`, the actual multiplier equation gives

\[
 \mu=\lambda-H^{\mathsf T}J+H^{\mathsf T}E[J]x.
\]

Consequently the exact combined equation is

\[
 \boxed{\ K^{\mathsf T}H(U,J)^{\mathsf T}J
 +(L_0-K^{\mathsf T}H(U,J)^{\mathsf T}E[J])x
 +N(x)-C'(x)^{\mathsf T}\lambda=K^{\mathsf T}\lambda.\ }
\]

Conversely, applying T0 and H^T to this equation with the constraint recovers the two reduced equations. Thus the extra term is `-K^T H(U,J)^T E[J]x`, and both this coefficient and the force map generally depend on J. They are not the J-independent F_U and J-linear Pi_U[J] required by (H1)–(H2). Section 4.3 correctly leaves the outline's operators unproved, but its suggestion that only checking those two hypotheses remains omits this parameter-dependence issue.

This dependence is not merely possible for arbitrary matrices. At the flat reference let `A=H0 b` be a nonzero lift in a fixed colour. Choose a real site field chi with `Q'chi=0` and with `[chi(b_-)+chi(b_+),A(b)]` nonzero on a bond where A is nonzero; compensate its mean at other sites of each pillar. Such sites exist on the single lattice at positive depth. The scalar gauge identity gives `lambda_A=0`, `lambda_{D chi}=chi`, and `KD chi=0`. The explicit correction at SA 10170–10185 therefore gives

\[
 \langle D\chi,E[j]A\rangle
 =\tfrac12\langle i[\chi+\chi^+,A],j\rangle\ne0
\]

when j is supported on that bond in the indicated nonzero colour direction. Differentiating the constrained lift at `J=tj` yields `H'(0)b=T0 E[j]H0 b`, which is nonzero: otherwise `E[j]A` would lie in `ran K^T`, contradicting the displayed pairing with `D chi`. Hence H, and therefore the force **operator** `K^T H^T`, actually changes with J. This is a hand refutation of J-independence, not a claim that the literal (B) response estimate is false.

**Repair and remaining obligation.** Keep the proved alternative named B0 and leave literal (B) open. A useful abstract repair of Sigma is also proved by the argument below: replace (H1)–(H2) by jointly holomorphic functions `f(U,J)` and `P(U,J)`, linear in the field argument of P, with `||f(U,J)||_F<=C_F gamma_0` and `||P(U,J)||_{X_w->F_w}<=C_P gamma_0` for every allowed weight. Neither needs to be linear in J. Use `f=K^T H(U,J)^T J` and `P=-K^T H(U,J)^T E[J]` for the displayed combined equation. The same contraction and datum-response proof works under these hypotheses; holomorphy, rather than affineness in J, suffices. **Unchecked:** the uniform bounds and holomorphy for these actual outline operators, including E. This report does not discharge them or the missing column estimates by analogy.

**(B1), lines 212–219 — ADVANCE.** For one inner plaquette, write its four transported variations as `X_r=eta Ad(T_{r-1})v_r`. The mixed Hessian consists of sixteen insertion terms. At P=1 their commutator traces cancel and the sum is the plaquette-curl bilinear form. Subtracting this expression leaves a factor `P-1` in each remainder term. Each complex prefix has at most four links and norm bounded by a fixed `exp(C alpha_1)`, so the remainder coefficient after division by the fine pairing weight is

\[
 C\eta^{-4}\eta^2|P-1|
 \le C\alpha_0\xi^{-2}.
\]

The current bound needs no second difference of the background. Each first insertion has coefficient eta; the trace of a traceless insertion against the identity vanishes. Summing at most six inner plaquettes and dividing by eta^4 gives

\[
 |J(\mathbf U)(b)|\le C\eta^{-3}
                 \max_{p\ni b}|P_p-1|
 \le C_L\alpha_0\eta^{-1}\xi(b)^{-2}.
\]

Missing boundary plaquettes only remove summands. If converting left variations to an exponential chart introduces a current term, the differentiated chart has an **extra eta**, so its coefficient is at most `C eta |J(Ubold)| <= C_L alpha_0 xi^-2`. This is exactly the factor that prevents the feared `xi/eta` loss. Neighbouring scales and weights are comparable on this fixed stencil. Multiplying the value input `xi^-1` by `xi^-2` proves `||Delta'v||_{F,w}<=C_L alpha_0 ||v||_{X,w}`. It is not necessary to assume the actual current has the independent current's stronger bound.

**(B2)–(B4), lines 220–222 — ADVANCE.** The SU(2) cubic trace identity holds over the complex numbers. Its surviving cubic term contains the plaquette curl; summation by parts gives `a nabla a` and `eta(nabla a)^2`. Higher terms give `a^3`, while curvature remainders give `alpha_0 eta xi^-2 a^2`. These are all `O(r^2 xi^-3)`. If boundary cancellation is absent, the scale there is eta and the crude `eta^-1 a^2` has the same bound. Local Cauchy differentiation gives `Cr ||h||_{X,w}`, without a second-difference premise. This verifies the extension of (12).

For the constraint, the one-step complex series, first-exit bound and geometric sum give the entry density `eta^4 s^-3`. One and two Cauchy circles give the derivative bounds (10)–(11); the fine transpose cancels eta^4, and bounded carrier overlap gives the weighted force norm. Bare level-zero rows are exactly linear. The reduced datum is a fixed local holomorphic function. Its outward conjugation is uniformly bounded because the accumulated complex site factors have logarithmic norm bounded by `C alpha_1 sum(q<j)L^(q-j)`, not `Cj alpha_1`. This proves its weighted derivative bound, including the fixed carrier-distance factor.

**Theorem Sigma, lines 224–236 — ADVANCE.** The fixed-point equation (4.1) has the correct signs. In the radius-r ball its Lipschitz constant is

\[
 q\le C^{\circ}_{\mathsf c}
      (C_\Pi\gamma_0+C\alpha_0+C_Nr).
\]

For the mixed constraint term split its difference into the change of `C'(a)` times the old multiplier and `C'(a)` times the change of multiplier. The two factors are respectively `O(r)` and `O(r)`. Choose r, then alpha_0, then gamma_0 so q is at most 1/4; choose the force and datum radii so the value of the map at zero is at most r/2. It maps the closed ball strictly inside itself and has exactly one fixed point there, bounded by `4/3` times that value, hence by the stated factor 2.

The iterates are jointly holomorphic and converge locally uniformly in fixed finite-dimensional coordinates. Although the displayed norms vary with U, their local equivalence permits this conclusion. This also proves the generalized repair above with f and P. Differentiation in B puts no derivative on the fixed current or reference. All local nonlinear estimates hold in every allowed weight, and any nonlocal Pi is controlled by (H2), **not** by the sentence claiming every term is local. Thus `(1-partial Psi)^-1` has weighted norm at most 4/3. Apply P^c to the two resulting forcings for the Hölder member.

Finally the differentiated first equation bounds the augmented curl member directly. The scalar output bounds `D(1-R)D^T h`, and the interior-stencil Weitzenböck identity supplies the component Laplacian. The forward/plaquette correction has the `C alpha_0 xi^-2` coefficient bound on the common plaquette domain. Here the explicit curvature assumption holds even in the bare layer, unlike Reg alone in the earlier real gate's D3. At real critical references with (A), the known physical pair lies inside the same ball after decreasing its datum/reference radii; uniqueness identifies it. The multiplier throughout is the **counting** multiplier. This completes Sigma for its declared systems without identifying the literal outline (B).

## 5. Disposition — CORRECT-NO-ADVANCE for the summary, with D1's scope correction

First failing step: none additional to the literal-(B) identification in Section 4. The closing table is accurate when its “(B) with Section 3's propagators” means precisely the system defined at line 191, here called B0, and never the unchanged SA second system.

| Section / statement | Verdict | First failing step or limit |
|---|---|---|
| 1, identification of the clauses | CORRECT-NO-ADVANCE | None; the full-scope claim needs the declared operator and inherited inputs. |
| 2, Theorem Pi | ADVANCE, implication | None; its kernel bound, cover identity and image summation are uniform in depth. |
| 3, Lemma 6.1′ and Theorem P^c | ADVANCE, implications | None; the coupled absorption closes, and Kato is used only at real links. |
| 4, (B1), (H1)–(H2), Sigma for (A) and B0 | ADVANCE, implications | None; actual-current chart terms carry eta, and weighted contraction gives all stated response members. |
| 4, identification of literal SA (B) with the stated force-only alternative / present hypotheses | WRONG | Line 178's incomplete elimination; actual H depends on J and the extra term is `-K^T H(U,J)^T E[J]x`. D1 supplies the exact algebraic repair and a proved conditional generalization. |
| 5, counting conclusion for the specified implications | CORRECT-NO-ADVANCE | No additional mathematical result. Literal (B)'s operator bounds remain unchecked. |

Only **D1** breaks an identification. It does not break Pi, P^c or Sigma for the systems actually defined. The source's Section 4.3 already excludes the outline's actual operators from its proof; retain that exclusion and correct its explanation as above. Calling (A) the chosen extension is legitimate. Calling it a demonstrated interpretation of every later use of the outline's pair system is not.

The large-actual-current warning at source line 206 is a scaling diagnostic, not by itself a proved counterexample to the discarded operator: a potentially large estimate on its factors does not establish a lower bound on their composition. Nothing in the accepted proof uses that negative assertion. Likewise the final text search for consumers is only search evidence, as the source itself says; it cannot remove an operator-matching obligation.

The small-radius order is consistent: L and the Hölder exponent, the flat constants and M, the gap and walk rate, the real/complex reference ceilings, then the solution/current/datum radii. Every subsequent decrease is by a constant independent of depth, mesh, volume and shape. The ceiling on alpha_1 can be imposed while choosing the final field strengths; it does not supply any new core admission theorem.

**Research decision for row 105:** periodisation and the complex regular-class inverse advance on their explicit real/flat inputs; the independent-current clause advances for the specification (A), and more generally for Sigma's declared hypotheses. Preserve the literal outline (B) as an open matching-and-bounds obligation, with the repaired equation in D1. No new P81, core admission, localization identification, column bound, audit verdict or scientific status follows. Sections 1–5 have been checked; the report is complete.
