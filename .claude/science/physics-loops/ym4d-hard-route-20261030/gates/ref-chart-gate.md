# Gate of ref-chart.md — queue row 140
Provenance: Codex (GPT-6; exact runtime variant and effort are not exposed), checkout `6b7b4273725c67eec7c2571f32f1068865748049`; Sussman–Alpoge commit `31a47c543775`; research-text check, not an audit, grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the outline's construction, Proposition 2.4, averaging formulas and complex-pair decomposition. Source: `YM4_sketch_500.tex` at the commit above, fetched once to `/tmp/sa_ym4.tex`. Balaban is credited separately below. All arguments in this report are by hand; commands only locate, retrieve, read or write text. Only this gate file is edited. The prescribed workflow file is absent from this pinned checkout; GOAL.md and the specified FINISH.md instructions govern this narrow check. Rows 102, 107, 112, 117, 133 and 140 were read. Named mathematical premises are taken conditionally: their proofs are not reopened, but a bound for one representative is not a bound for another.

## 1. Scope, sources, credit — CORRECT-NO-ADVANCE

First failing step: none in the scope or attribution. CMP 122 (1989), 175–202 was not available and its proof was not read. Thus this is a proposed independent reconstruction, not a verification of that paper's Proposition 1.

CMP 102, Theorem 1 (p. 279), supplies the minimal orbit and uniqueness among sufficiently regular configurations **on the prescribed constraint fibre**, with local regular gauges. Proposition 8 (p. 304) improves the regularity of an already critical configuration. Section G (pp. 305 onward) constructs the analytic dependence after gauge fixing. These statements do not themselves assert a gap after freeing the reference-box rows. CMP 109, Section 2, (2.2)–(2.3), studies the next-step constraint `M(V)=W`: its minimiser is obtained from `U_{k+1}(W)`. That is another constrained problem, not the box-exterior problem. Its subsequent passage from axial to Landau gauge also keeps the gauge transformation explicitly. None supplies the missing identification discussed in Sections 5–6 below.

## 2. Counterexample first — WRONG as an exclusion of all four mechanisms

First failing inference: attempt 3 applies T4 to the raw response without checking the node gauge; attempt 4 then relies on the resulting Theorem H and Lemma M. The flat curl mechanism in attempt 1 survives (Section 4). Gauge fixing removes exact variable-site gauge directions (Lemma G). Those two facts do not establish the curved gap or exclude a boundary minimum. No counterexample to the actual minimiser theorem is asserted here.

Repair: retain the flat and slice tests as conditional diagnostics; replace the claimed exclusions of the curved and boundary mechanisms by the outstanding response/gauge identification in Section 6. Absence of a found counterexample is not its proof.

## 3. Reference problem, slice and class — ADVANCE after the carrier/site repair

First failing step: the parenthesis claiming that a Euclidean reading necessarily leaves edge plaquettes uncontrolled. It confuses the geometric box `Lambda^pr` in SA 17656 with its set of lattice sites Lambda. The outline fixes centred half-open M-cubes (SA 5585–5596), with M a power of the odd L. The prepared box is enlarged in that partition (SA 17585); `geo-4.md` Section 1 explicitly uses its cubical carrier. Its faces lie halfway between adjacent level-k sites. These are the actual consumer conventions, not an invented new mild class.

**Proved repair of the class identification.** In each coordinate let the sites in the box run from a through b; the carrier runs from `a-1/2` to `b+1/2`, with the fixed half-open endpoint choice. Every site of Lambda-plus is at most 1/2 outside this interval in each coordinate. In four dimensions its Euclidean distance to the carrier is therefore at most `sqrt(4)/2=1`. Conversely a site outside Lambda-plus is at least 3/2 beyond a carrier face, so is not in its distance-one neighbourhood. Thus the two **site neighbourhoods coincide**, even if “distance” in SA 17656 is Euclidean. If “within” is interpreted strictly, the only extra excluded sites have all four coordinates outside, at distance exactly 1; plaquettes touching such a corner have no variable bond and are already controlled by H-epsilon. Since epsilon<=a, the admitted classes still agree. The note's Euclidean warning is wrong, but its explicit cubical class is the right class for these consumers. No new premise is needed for this repair beyond their fixed aligned-box convention.

For the **explicit cubical class defined here**, no step of G or S fails. Solving the external tree edge fixes the root gauge, and recursion fixes all other variable-site gauges. Its derivative is triangular, proving the tangent splitting. The fundamental cycle's tree portion uses only fixed exterior transports on the slice. The axial triangles telescope as 2-chains and give the stated area bound. Consequently `|hol(gamma)-1| <= A_M a`, and the local logarithm gives `|u| <= 2 A_M a`. In the centre, variable fundamental cycles are identities; only at most four exterior cycles enter a plaquette. For the shell filling, move top-face excursions to the rim, fill each excursion and its replacement inside that three-face, then drop the resulting rim/side loop to the bottom face. The stated `40 n(n+1)^2` per-edge budget exceeds the sum of these strip areas and path lengths. All filling plaquettes are exterior. Four variable bond increments give the `8 rho` error in S(iii). The containing ball, rather than the class itself, is convex; the subsequent argument correctly uses that ball.

For the reference cutoff the sufficient admission bound is `C_{2.4} epsilon + 8 M_0 epsilon_k < a_Lambda`, once the minimiser is established. This bounds every S-plaquette and matches the preceding class comparison. It does not establish the minimiser itself. A different site-box convention would require its own comparison; it must not be silently substituted for the source's geometric carrier.

## 4. Two exact linear facts — ADVANCE

First failing step: none for E or P on the specified cubical patch. From the actual QC3 derivative, SA 8177–8189, the four endpoint terms `sigma` cancel. Translation of the blocks makes the remaining four straight segments the boundary of an L-by-L square. Abelian Stokes gives exactly `d K = P d`, with nonnegative weights. In four dimensions a row sum is `L^2` and a column sum is `L^(-2)`: fixing `(r,s)` fixes the starting site and its unique block. Thus

`sum_i |sum_j P_ij f_j|^2 <= L^2 sum_j (sum_i P_ij)|f_j|^2 = sum_j |f_j|^2`.

Composition preserves this bound at every depth. Restricting to S and to its full ancestor support preserves it as well. The ancestor support stays inside the union of the endpoint/corner blocks: at each step internal contours stay within a block and crossings stay between the two endpoint blocks. This also checks the near-region support assertion used later.

For P, the circulation of `w^0` around a variable fundamental cycle is exactly its single non-tree value, since the rest is zero. With at most `A_M` plaquettes counted with multiplicity, Cauchy–Schwarz and then summation over at most `n_b` bonds give `C_P = n_b A_M^2`. No depth or volume enters. In particular a **raw** flat lift with `K^(k)Y=w^0` has curl energy at least `C_P^(-1)|w|_2^2`. This is a lower bound on every such lift; it does not require an unproved identification of its minimiser.

## 5. Envelope, second variation, multipliers — V ADVANCE; response identification WRONG

**V(a)–(c): ADVANCE. First failing step: none, including at non-critical box data.** Put `q=q_raw`, as defined in this section. The right inverse `Dq D Phi=id` makes Dq onto. Constrained criticality means DA annihilates its kernel, so `DA=lambda Dq`, uniquely. Along the actual raw section write `Phi_V(tw)=exp(iY(t))U`. The identities

`(A o exp_U o Y)'' = Hess A[Y_1,Y_1] + DA[Y''(0)]`,

`0 = (q o exp_U o Y)'' = D²q[Y_1,Y_1] + Dq[Y''(0)]`

give (5.1) with **all** multipliers. Neither equation requires `Df(V)=0`. Dropping exterior multipliers, or using the ordinary action Hessian alone, would be wrong; this lemma does neither.

**First failing step: the sentence after V, `Y_1=eta h` for the T4 responses.** The cited `a3-derivative.md` Sections 6.1–7 explicitly have

`Phi_V(B)=(exp(i eta H(B))U)^{u_B}`,  `u_B v[H(B)]=1` at tops,

and T4 bounds `h=D H(0)[w]`. If `u_tw=exp(i t chi+O(t²))`, differentiation instead gives

`Y_1(b)=eta h(b)+chi(b_-)-Ad(U_b)chi(b_+)`.

There is no assertion that chi vanishes. The source's (35) likewise gives, for the Landau lift, `Dq_raw[eta h]=w+delta_V sigma`, where `sigma=(1/i)D v[H(tw)]|_0` and `(delta_V sigma)_c=sigma(c_-)-Ad(V_c)sigma(c_+)`. Thus the first line of M's proof, `Dq_raw[eta h_c]=e_c`, is not that source's identity. This is a misuse of a named premise, not a challenge to T4's proof. If “T4” in the input table is instead *defined* to assume the stronger raw-representative estimate, H becomes a conditional theorem with that **additional** premise; the cited result has not discharged it.

The distinction can be seen without computation. At flat data choose a coarse pure gauge which is `exp(it Z)` at one coarse site and 1 elsewhere. Its block-axial fine representative is the same pure gauge extended constantly over each block. All internal bonds are 1; fine bonds crossing that block boundary have angle `+/-t Z`. Only the eight incident coarse bonds change. Thus its raw fine tangent is of order 1 at such crossings, not `eta` times a bounded continuum potential. A Landau representative distributes the same variation differently. This refutes a representative-independent raw-response reading of T4, not the axial freed-gap theorem (this datum direction is a gauge direction).

**M has a proved repair at a real base.** Gauge invariance and V(a) give the Ward identity `sum_c tr(lambda_c(delta_V sigma)_c)=0` for every node field sigma (extend it arbitrarily to fine sites). Pairing the correct Landau row identity with lambda therefore still gives `tr(lambda_c e)=DA[eta h_c]`. The displayed current pairing and T4 then prove the multiplier bound: each top contributes `eta^4 * 4(xi/eta)^4 * r L^3 xi^(-3) * C4 xi^(-1)`, with the trace factor 2. Summing BC-prime yields the stated `4 L^3 C4 C_BC' r`. This repair does not identify the two second variations.

**BC-prime: ADVANCE. First failing step: none under the stated gap premise.** An R-ball about a level-q top meets at most `2(R+1)/c_g+3` levels. Its largest scale is at most `xi_q L^((R+1)/c_g+1)`. Packing at the smallest accessible scale gives the displayed fourth power. Its exponential part is bounded by `exp(-(theta-8 log L/c_g)R)`, with a polynomial factor. The gap gives `8 log L/c_g<=theta/8`. The same argument at rate theta/2 still converges. No volume or finest-scale cutoff occurs in the bound.

**R: ADVANCE for the re-centred raw row; first failing substantive step none.** RD supplies the bounded analytic row on the carrier ball. Cauchy on radii tending to `r_*/(s sup|h|)` gives a second derivative bound `2 C_R(s sup|h|)^2/r_*²`, hence the stated 3. The printed half-radius circle alone would give 8, so use these larger circles, permitted at the central base. For the mismatch, differentiate the flat row F on two scalar discs, integrate `D²F(ta)[a,h]`, and add the bond BCH and output-log BCH derivatives. They cost respectively `C eta|a||h|` and `C|F(a)|s sup|h|`; `eta<=s` and `|F(a)|<=C s sup|a|` give (5.2). Here the raw logarithm must be centred at the row of the current base, as its proof does, rather than at an unrelated fixed V. This is exactly the version used in the flat comparison. Shrink the real datum radius if necessary to put `r(U)<=bar epsilon`, rather than inferring that from `alpha<=bar epsilon` when `r(U)<=B alpha`.

**N and the plaquette Hessian: ADVANCE. First failing step: none.** Each axial strip has at most `3 ell_N/eta` plaquettes, giving a bond angle at most `6 ell_N B alpha eta`. For the Hessian, the transported insertion sum is the covariant curl. Twice differentiating the product gives its square plus terms containing `U_p-1`; commutator traces at the identity vanish. Bounding the four-insertion sums gives (5.3). The comparison of transports with 1 costs at most `16 eta bar a sum|Y|`. These are real-unitary estimates, as stipulated; no complex version with the same isometry is inferred.

## 6. Theorem H — WRONG as the claimed reconstruction; flat bound ADVANCE

First failing step: its opening identification `Y=Y_1=eta sum h_c`, followed by (6.1) for that Y. Section 5 explains the missing gauge derivative. With the actual raw tangent, (5.1) and the row equation are true but the quoted T4 bound is not supplied. With the Landau tangent, T4 is true but the row equation in the “Flat comparison” paragraph has the extra `delta_V sigma`, and (5.1) has an extra second-jet term. Choosing one tangent in each half of the proof does not identify a Hessian.

The remaining numerical structure is sound **if** a single raw lift with the stated decay is added as a premise. This conditional check is worth preserving:

- Far plaquettes contribute `r eta² xi^(-2) * eta² xi^(-2) * (xi/eta)^4 = r` per top, times the squared exponential response. BC at rate `2 theta` sums it. Use lower-corner assignment to justify six plaquettes per site (with the stated adjacent-scale factor L); using the finest-corner assignment of the ten-term paper requires 24 instead.
- A row's Hessian costs `(s sup|h|)^2`; at its carrier `s` and xi are comparable. Multiplying by the repaired M and summing at most eight oriented incident rows per top gives `C(M) r |w|_infinity²` through BC. No total number of exterior rows appears.
- On the near patch N the axial gauge is fixed at the base, so it transforms a left tangent by `Ad g`, without a derivative of g. Near losses are `O((bar a²+B alpha)|w|_infinity²)` after the four-dimensional mesh cancellation. Lemma R then gives an `O(bar a |w|_infinity)` mismatch to the **raw** flat row. Applying E and P twice with `|a+b|²>=|a|²/2-|b|²` gives the printed leading `1/(4 C_P)` and the displayed `8|S| mu_0²` loss. Substitution of `bar a=6 ell_N B alpha` gives the coefficients 36864 and 288 in C5. The final absorption is valid for the chosen radius.

Thus E is not the broken step, and neither is the near/far summation. The missing step is the identification of the response to which they are applied. At flat data the gauge discrepancy is an ordinary coboundary: `K^(k)(eta h)=w^0+d sigma`. Hence `d K^(k)(eta h)=d w^0`; `lambda=0`; gauge invariance removes the gauge part of the action variation. E and P prove the claimed flat gap even in the Landau description.

**Visible repair of the curved argument (not completed here): keep the node jets.** For `U_L(t)=exp(i eta H(tw))U`, define

`q_curve(t)=(1/i)log(v(t) exp(itw)V v(t)^(-1) V^(-1))`

row by row, with the two endpoint values of v understood. The exact replacement for (5.1) is

`h_V(w)=Hess A[eta h,eta h]-lambda D²q_raw[eta h,eta h]+lambda q_curve''(0)`.

This follows by differentiating `q_raw(U_L(t))=q_curve(t)` and eliminating `H''(0)`, exactly as in V. Write the node logarithm as `t sigma+t² tau/2+O(t³)`. Its term linear in tau is `delta_V tau` and vanishes when paired with lambda by the Ward identity. What remains is quadratic in sigma and w. The top-factor member of T4 (`a3-derivative.md` 7.5) is the appropriate input to bound it; it is not a bound on the raw fine tangent.

For the near comparison, after the fixed gauge g, use

`K^(k)(eta h')=w'^0+delta_(V^g) sigma'+m`.

Subtract the exact coboundary `d sigma'` before taking the curl. Since `V^g=1+O(ell_N B alpha)` on these rows, the remaining `delta_(V^g) sigma'-d sigma'` is small if the top-factor response is controlled. This suggests a loss `C_node(M) alpha |w|²`, with a smaller datum radius, not the printed C5. A full repair must write its node-jet/carrier sum and its bound uniformly through the tower, or instead construct a raw lift with the required weighted bounds. Those estimates and a revised constant are **unproved in ref-chart.md**. No curved uniform-gap theorem is certified by the printed proof.

## 7. Proposition 2.4 — WRONG as discharged; the convexity implication survives

First failing step: step 1 invokes the unestablished curved Theorem H. Section 3 repairs the mild-class identification for the actual carrier convention. The missing freed-gap identification is not supplied by CMP 102 Proposition 8 or CMP 109.

There is no further failure in steps 1–5 **conditional on H and the stated class**. S puts the slice inside radius rho1 and gives admissibility on the larger convex ball rho2. The BCH velocity differs from w by at most `4 rho2 |w|`; its acceleration is `O(rho2 |w|²)`. The repaired real multiplier estimate controls the acceleration term, and the last restriction on alpha-star absorbs it. This proves ordinary-coordinate convexity, rather than incorrectly identifying it with a left-geodesic Hessian away from criticality. At the centre `|grad phi(0)|<=2 sqrt(n_b) C_M B C_c epsilon`; the quadratic lower bound excludes the boundary of the compact rho1 ball. The minimiser is interior and belongs to K by the final epsilon restriction. Strict convexity along the entire segment between two slice points proves uniqueness and the displayed strict minimum bound. A nonconvex K causes no problem because those segments lie in the larger admitted convex ball.

Step 6's current conclusion is valid once the minimiser exists: the slice critical point is critical in every variable direction by G, so all variable multipliers vanish. At every averaging step the support is contained in the two endpoint blocks and their crossings. Induction therefore confines a bare bond inside a Lambda block, or crossing from it to an adjacent block, to rows incident to Lambda. The remote tower reads none of them. Only zero multipliers then contribute to that bare current. Step 7's Hessian is H; analyticity depends on Section 8, not just on uniqueness of an orbit.

Repair: retain these as a convexity-to-minimiser implication; complete the node-jet repair of H, use the carrier/site comparison of Section 3, then use the corrected finite-dimensional analytic construction below. The source's cruder M-only constants would suffice. No proof of the actual curved critical orbit, and no removal of I4's premise, follows yet.

## 8. Joint chart, P and D — WRONG as written; local analytic mechanism repairable

**Complex multiplier bound and CE.** The first inherited failure is the raw/Landau identification in the complex reuse of M. Gauge invariance still removes the varying gauge from the scalar action, but differentiating `exp(i eta H(B))` away from B=0 introduces its dexp factor; differentiation with respect to v introduces another coordinate factor. Their norms on a smaller fixed ball are bounded by fixed constants, not identically 1. Enlarge C_G after these factors are included. Conditional on a uniform bound for each scalar component of G, CE is sound: one complex directional disc controls the increment independently of the number of exterior coordinates; Cauchy controls an H entry; an n'-by-n' matrix has operator norm at most n' times the largest entry. No volume factor is necessary.

**Theorem C: first independent failure is the complex norm/radius step in (i).** The text specifies the operator norm on complex traceless matrices but uses `|v|_infinity<=|v|_2` for complex colour coordinates. In fact, with `Z=(sigma_1+i sigma_2)/sqrt(2)`, the Euclidean colour norm is 1 and the matrix operator norm is sqrt(2). Thus the stated Euclidean ball need not lie in the sup-norm rho_H ball where the `1/4` contraction and Hessian estimates were proved. This is a fixed-factor defect, not an obstruction to an analytic implicit-function argument.

If instead `|v|_2` means the square sum of matrix operator norms, the same comparison factor is needed when importing the Euclidean spectral bound `||H(0,0)^(-1)||<=1/c_*`. The two complex norms cannot be identified in both steps.

**Proved radius repair, conditional on the corrected G bound and real gap:** keep rho_H as defined using the enlarged C_G, and use

`rho_v = min(rho_H/2, r_B/16)`.

Keep the beta restriction `3 c_* r_B rho_v/(16 sqrt(n') C_G)` and `rho_beta<=rho_v`, with the admission restrictions below. Then `||v||_bond-sup<=sqrt(2)|v|_colour-2<=rho_H` and is below `r_B/8`. CE gives `||D_v T_beta||<=1/4`, while `|T_beta(0)|<=3 rho_v/4`. The ball maps into itself and contracts. Its iterates converge geometrically on every closed smaller beta ball, so Cauchy's formula proves holomorphy of the limit. Invertibility at zero and the same contraction prove uniqueness there; conjugation proves reality. The fixed-point bound is the displayed C_v bound. The complex Hessian perturbation is at most c-star/4 and its Hermitian real part is therefore at least 3 c-star/4. Interpret this as `Re(w* H w)`, not as positivity of a complex bilinear square.

In (ii), changing exterior bonds also changes plaquettes in S. The printed bound omits their `8 rho_beta` contribution. Replace its last admission restriction by `rho_beta<=a_Lambda/[32(1+C_v)]`, for example; then `C_{2.4}epsilon+8(1+C_v)rho_beta<a_Lambda` with room. The real exterior test uses `epsilon+8 rho_beta`, as correctly stated. In (iv), shrink `|u'|_infinity` by another fixed factor if necessary to control BCH and its derivative. Integrating the bounded gradient gives a uniform bound on the **centred complete** action. Its first derivative is zero, so applying the scalar Schwarz lemma twice gives a quadratic bound. This part is valid for the complete action only.

**P: CORRECT-NO-ADVANCE as an application of the repaired C and its explicit ADM premise.** The row Cauchy estimate gives beta_A. The overlap argument is valid: two real centres within `4 beta_A` have critical representatives on the same real branch, and both complex zeros lie inside the uniqueness ball once `10 C_v beta_A<=rho_v`, with the fixed complex-norm allowance. Thus the branch is splitting independent; J is absent from the Wilson-only law. The real-diameter construction is valid under its explicitly enlarged `5 alpha_A` premise. Its cutoff admission must use `C_{2.4}(epsilon+40 beta_A)+8 M_0 epsilon_k<a_Lambda`, not the unperturbed epsilon alone. All these quantities tend to zero at a fixed coupling ceiling. This checks use of ADM; it does not prove ADM for literal operations.

**D: WRONG at the inference that its displayed slice radius gives delta-star tending to zero.** Put `t=||A'_I||` and evaluate at `s=i t`. Its offered radius is `4t`, hence `|s|/(rho-|s|)=1/3` (and less room after Lemma 3.2). In (3.4) of `sa-2.13-2.md` the quadratic term is then of order H², not `O(g polylog)`. Holomorphy on a disc shrinking with the displacement supplies no small parameter factor. At t=0 use the real case directly; a zero-radius disc is not a chart.

**Visible repair:** use the fixed beta radius furnished by the repaired C for the coefficients of degree at least two in u'. The short real slice may still be used to bound the linear cutoff tail. For a fixed-degree coefficient the beta increment costs `beta_A/(R_beta-beta_A)`, with `R_beta>0` chosen after M and before the coupling ceiling. Keep the linear term separately, as in Section 9 below. CUT and the real-tail premise must apply on the entire real diameter, as the antecedent explicitly requires. The centred cutoff-action coefficient bound can be volume free if its derivative is proved by the cutoff-current pairing and the summable response; the mere assertion that the two separate centred pieces are bounded is not a reason to discard their linear coefficients. Consequently D's complete criticality and admission reduce to the repaired C/P, but its stated zero-free conclusion does not follow by the radius calculation printed here.

## 9. Complex-pair remainder — WRONG as a completed bound

### 9a. Proposition Ref — WRONG; the cutoff-tail repair is explicit

First failing step: its quadratic bound for `F_beta(u')-F_beta(0)`. Complete criticality gives `D F_all(0)=0`, whereas `D F(0)=-D F_out(0)` need not vanish. A small nonzero linear coefficient cannot be bounded by a constant times `|u'|²` on a neighbourhood of zero. For an exact scalar test take `F_all,beta(u)=u²/2`, `F_out,beta(u)=t beta u`, with t arbitrarily small. All functions are holomorphic, the complete branch is critical, and the cutoff tail is small. Nevertheless `F_beta(u)-F_beta(0)=u²/2-t beta u` is not uniformly quadratic for beta nonzero. This refutes the inference, not the actual denominator theorem.

**Proved repair of the analytic implication:** expand in u, retain the linear coefficient, and apply the large beta-disc bound only to degrees at least two. If the centred coefficient bound is K', the u radius is r, `gH<=r/2`, and the complex linear tail is at most T at both reads, the exponent difference on the full real cutoff is bounded by

`delta <= 2 T H/g + (2 K' H²/r²) beta_A/(R_beta-beta_A)`.

The first term is exactly the term retained in `sa-2.13-2.md` (3.4); the second uses the fixed radius of the repaired C. For `T<=polylog * exp(-c M Rcheck)` and `beta_A=O(g polylog)`, both tend to zero: `Rcheck>=c(log g^(-2))^r`, r>=2, beats the first term's g-inverse, and the second is g times a fixed polynomial. Division by the positive actual real reference integral then gives `|Dhat(p)/Dhat(p_r)-1|<=exp(delta)-1`, retaining the Haar density exactly. For delta small the logarithm exists and is at most `2(exp(delta)-1)`. The constant-action cancellation in Ref is algebraic and passes. This repair needs the corrected chart and the named tail bound, and proves no relative-Hessian comparison or Gaussian decoupling.

### 9b. Proposition S — WRONG for the raw prepared data

First failing step: `U_0(p)=exp(i eta a(p))U_0(p_r)` with the Landau-potential bound. P81 actually supplies this representation **with a gauge factor**, as Section 5 shows. A raw shell row transforms at its two endpoints. Its increment therefore contains endpoint-gauge terms as well as the small-potential row increment. Dropping them is especially consequential in (9.1): a bound `O(beta_A)` is not `O(xi_j beta_A)` uniformly down the shells. The block-axial pure-gauge example in Section 5 also illustrates this: averages of a fine crossing of a coarse block boundary retain the full coarse angle even at smaller averaging scales.

The last conjugation by `exp(i g B)` is harmless for real stored B (it is exactly unitary); it is not the missing gauge. Given (9.1) in a **specified common representative**, the subsequent admission follows by shrinking the fixed radius to include the factor `2 C_S`, and P81 supplies holomorphy for each separately admitted prepared/meet datum. A bound for the prepared datum alone does not automatically prove admission of all four other data unless their row/lift constructions are included, as in the stated I5/meet premises.

Visible repair, unproved for the literal substitution: choose the common Landau representative for U0, carry its node gauges through every shell average, and show that this change preserves the fixed old-core datum, the stored tree constraints and the reference integration variables, or prove the required endpoint-gauge increment bound in the actual representative. The estimate for a potential in a chosen gauge is not by itself an estimate for the specified stored fields.

### 9c. Proposition I and its inductive use — CORRECT-NO-ADVANCE conditional on repaired S

First failing dependency is (9.1). Assuming that row bound and an admitted real prepared reference, no depth loss occurs in the response sum. At a core top split the response exponential in half. One half pays the shell count by BC-prime, the other pays `M(j-k_flat-1)_+`. The scale in (9.1) gives

`sum_(j>=k_flat) xi_j exp(-theta M(j-k_flat-1)_+/2)`
`<=xi_kflat sum_(m>=0) L^m exp(-theta M(m-1)_+/2)`.

The last series converges by the stated gap condition. Insert the bounded number of rows per top in C_I. T4's current member yields the corresponding estimate for the **scaled** current, with its xi³ weight. This proves the asserted suppression in local units, conditional on S, rather than for an unspecified raw representative.

Schwarz estimates for an inner activity additionally require that its real read has room inside its inner pair domain. “Size of the domain” alone is not that distance to the boundary. Apply the estimate on a specified interior subdomain, or retain this margin as an admission premise. The quadratic inner q must similarly have a uniformly bounded coefficient derivative in the chosen real splitting; being quadratic in stored variables does not prove that derivative bound. Neither issue permits replacing the full mixed Q by separated Gaussian laws; the row-107 gate's full-Q repair remains mandatory.

### 9d. Proposition I(b) — WRONG reading of SA 18068–18072

First failing step: “the pair moves only plaquettes of regular backgrounds.” The cited passage identifies the retained Wilson factor as the **real inner background from the truncated prepared sequence and its stored innermost datum**, distinguishes it from the glued background in q_X, and explicitly keeps the old large plaquettes with their positive action. The note has not identified its differentiated prepared background with this inner read, or shown exactly which plaquettes of this factor change when the outer pair changes.

`floor-screen-gate.md` Section 1 does not justify that inference. Its repair of Lemma O is independence under changes preserving the **entire fixed joined datum and geometry**, including collar lifts. It explicitly rejects the assertion that all raw floor variables are off that datum; level-zero bonds can themselves be determining rows. Being off a particular determining set is neither a bound on a physical plaquette retained in another Wilson factor nor proof that a change preserves that factor's full datum.

Conditional on the missing identification and local scaled-curvature bound, the displayed scalar inequality and shell/layer sums have the right mesh cancellation and suppression. That conditional calculation does not validate the reading. A possible repair is to keep the exact stored real inner action in Phi-circle, identify its unchanged bonds and complete boundary datum, and compare only the remaining action on a common admitted region. If the comparison requires non-small plaquettes, write the corresponding weighted bound explicitly; the small-curvature factor used here is then unavailable. A uniform summable bound for their **scaled** curvature could suffice because `L^(-N/2)` beats even an extra g-inverse. Neither that bound nor the required support identity is proved here. The literal inner contribution therefore remains open before (Act).

### 9e. Lemma 6c-complex — WRONG as written; the identity theorem itself is valid

First failing step in step 1: asserting that `Phi_(B')(B'(beta))` is defined on the polydisc. Its B' is formed from `M_(B')(U(beta)|_W)` **before** the collar node gauge. R2 in `a3-derivative.md` Section 10 asserts closeness to the joined datum only **after a node gauge equal to 1 at old nodes**. That gauge can act at the new collar nodes. It is not a residual gauge fixing all joined nodes. Consequently neither `B'(0)` nor `B'(beta)` has been shown to lie in the small joined-datum chart. An axial canonicalization fixing the joined nodes cannot change this row mismatch. The identity theorem cannot extend a composition which has not been defined on its asserted domain.

**Visible repair:** perform the holomorphic collar normalization G(beta) first and define

`Bhat(beta)=(1/i)log(M_(B')(U(beta)^G|_W) (V_r^J)^(-1))`.

Prove step 2's bound for this Bhat, with `Bhat=B0 * beta^J`, `||B0||<=C_L(epsilon_1+C9 beta_*)`, on a fixed subpolydisc. This is the datum to insert into the joined chart. Then the two canonical representatives are holomorphic on that common domain and agree on a real open box by real restriction compatibility and uniqueness. Applying the one-variable identity theorem successively in each datum coordinate proves equality throughout that domain. The explicit canonical maps then recover the complex residual gauge; G(beta) is carried separately. This proves the continuation mechanism, conditional on the corrected normalized-data bound; it does not use real uniqueness directly at complex data.

Step 2's geometric sum of average-plaquette errors is sound in controlled local complex gauges: `sum_(m<j)L^(2(m-j))` converges. Its printed direct use of a raw identity `U(beta)=exp(i eta a)U_r` must retain the P81 gauge, as in S. In step 3 the integral of D H along the admitted segment is legitimate, the weight `exp(theta d(y,W^c))` is admissible for the joined metric, and BCH converts the difference of potentials. When returning to the canonical comparison field, use covariance of its covariant derivative and bound the conjugators on the complete local stencil; values at tops alone do not prove a bound on that stencil. These are representative/admission obligations, not failures of holomorphic uniqueness.

### 9f. Theorem 2.8-T-complex — WRONG; several replacements need more than a factor 3

The first failed dependency is Lemma 6c-complex above. Independently, the replacement of I1 says that decay from `A_i^c` is merely a choice of W. It is not. For W4 the actual meet domain is `Omega_0 intersect (Torus minus Lambda)`; its complement includes the old holes. The lemma as stated decays from that complement and gives no suppression near those holes, even arbitrarily far from Lambda. This is precisely the distinction already required by row 107's gate and `meet-6c.md` Theorem M. The analogous W3 forcing set is the added collar, not every boundary of the localised domain.

**Visible repair of I1:** after the normalized complex collar construction, retain the support of B0 on the added rows `C_Ai`. In step 3 use the admissible weight `exp(theta d(y,C_Ai))`. Locality of the reduced-datum map confines its forcing to the D_L neighbourhood of those rows. The weighted inverse estimate then gives decay from C_Ai; the geometric comparison of Theorem M gives decay from `A_i^c` at cost `exp(theta(2rho+8))`. Keep also the fixed `mu+2` distance loss for R3/R6. This is the real meet proof's actual repair and carries over once the complex chart and support assertions have been established.

The rest of the replacement list checks as follows, conditional on the preceding repairs:

| Replacement | Verdict and first failure, if any |
|---|---|
| Algebra (1.3), GEO, EXT, FLOW, W | ADVANCE; none in the algebra. Use the already repaired real premises, including the 2L rounded-radius bound, 24-plaquette finest-corner count and frozen pre-ceiling constants. |
| I2, I3 | CORRECT-NO-ADVANCE on actually admitted complex data about a real reference. T4 bounds the Landau potential, not a new raw representative. |
| I4 and LM | CORRECT-NO-ADVANCE after H/C are repaired. Full criticality and the holomorphic identity then continue; real minimisation itself is not a complex ordering statement. |
| I5 and the xi² factor for S | WRONG as supplied by S, for the gauge/admission reason in 9b. A uniform level-k potential in a controlled common gauge would retain this factor; ordinary prepared local regularity alone does not. |
| SL(2,C) scalar step | ADVANCE; none. For E=G-1, `det G=1` gives `tr E=-det E` and `a(G)=det E/2`; polarization bounds the difference by `3(||1-G||+||1-H||)||G-H||/2`. |
| Taylor remainder and TQ | ADVANCE on the stated roomy chart, after the existing counting repair. The integral remainder is valid for complex functions and its weight integrates to 1/6. Cauchy's directional estimate needs no real mean-value point. |
| R9 matrix Hessian | WRONG with the literal unchanged constants. The trace identities continue, but the estimates `|X1|<=4|A|`, `|X2|<=8|A|²` used unitary transports. Include the bounded complex transport/conjugator condition numbers in the constants and retain the acceleration term. This is a finite constant repair once local complex gauges are supplied. |

**First failure in collecting powers:** “x beta_A² is ... of the same order as x epsilon_1².” With `ell=log(g^(-2))`, the admitted pair radius can have `beta_A=O(g ell^q)` (SA 6033), whereas `epsilon_1=O(g ell^(p_0+2r))`. The outline explicitly allows, and uses, `q>p_0+2r` at SA 17828–17831. The ratio can therefore grow like `ell^(2(q-p_0-2r))`. Being polylogarithmic does not mean the same order. The displayed original power K-star and the unchanged ceiling have not been preserved.

**Proved power-count repair:** put `p=max(p_0+2r,q)` and use `epsilon_1^C<=C g(1+ell)^p`. Enlarge the polynomial exponent, for example by `2 max(0,q-p_0-2r)` above the repaired real K-star, since these estimates are at most quadratic in that amplitude. Freeze q and every enlarged constant before choosing a new ceiling. The exponentially decaying comparison terms and the remaining `g(1+ell)^K` terms still imply `C g^(1/2)` by elementary exponential domination. This proves the collection implication; it does not supply its analytic inputs.

**Gaussian comparison: WRONG as inferred from the admitted polydisc alone.** A bound for a holomorphic function on a ball of radius comparable to beta_A yields an increment of order its bound at distance beta_A, not an extra `beta_A/r_B`. For example `f(z)=z/beta_A` is bounded by 1 on that ball and changes by 1. Moreover the Landau response re-centred at S(p), used to define H_p, must be matched to the fixed-real-reference response whose full-polydisc estimate is actually available. A real identity at p_r does not establish this analytic family with a uniform radius.

Visible repair: construct that gauge-consistent family on a fixed exterior-datum ball `R_Q(M)>0`, include the prepared substitution on that larger ball, and prove `|Q^C|<=C K_X(A1 p1)^2` there. Directional Schwarz then gives

`|Q^C-Q(p_r)|<=C K_X(A1 p1)^2 beta_A/(R_Q-beta_A)`.

This is `O(g polylog)` if R_Q is fixed, and any fixed ratio r_B/R_Q can be included in C(M). The family/radius and equality with the literal real glued Q are required matching statements, not consequences of positivity of Q. No factorisation of inner and outer Q is introduced.

### 9g. “Where V_X stops” and the final counterexample attempts — WRONG

First failing step: calling Ref, Pre and Inn completed and making (Act) the first open step. Ref loses a linear term and the fixed analytic radius; Pre needs the gauge-consistent substitution and complex meet comparison; Inn needs the actual inner-read/support identification. Their conditional repairs do not make them supplied inputs. (Act) remains an acknowledged open obligation, but is not the only one. The alleged exclusions (a)–(d) merely reuse those failed implications. No actual zero of the reference denominator, or counterexample to the Yang–Mills construction, is proved by this gate.

## 10. Standing, consumers and verdict — WRONG as the completion claim

First failing step in the opening Outcome and Section 10's table: listing H, Theorem 2.4, the joint chart and the three remainder parts as already proved from the cited inputs. The valid pieces and conditional deductions must be separated from the missing representative, domain and support identifications. The source's statement that only (Act) is the first failing step is not sustained.

| Source section | Verdict | First failure or surviving result |
|---|---|---|
| 1 | CORRECT-NO-ADVANCE | None in attribution/scope; cited fibre theorems do not supply a freed-box gap. |
| 2 | WRONG as exclusion | Curved response used as raw response in attempt 3. Flat and tree tests survive. |
| 3 | ADVANCE after carrier/site repair | G/S pass; centred half-open geometric carriers make the source and cubical classes agree. The warning about Euclidean distance was wrong. |
| 4 | ADVANCE | None: actual averaging contraction and tree curl inequality pass. |
| 5 | ADVANCE for V, BC-prime, R, N; WRONG at response identification | `Y_1=eta h` omits the node gauge. M has the Ward-identity repair above. |
| 6 | WRONG as supplied H; ADVANCE at flat data | Opening raw/Landau substitution. Near/far and mismatch arithmetic work given the stronger matched lift. |
| 7 | WRONG as discharged; valid convexity implication | Invokes the missing curved H; uniqueness/minimality argument otherwise passes on the explicit class. |
| 8 | WRONG as written | Inherited gap, complex norm/radius losses, and a slice radius shrinking with the target displacement. Local contraction and overlap mechanism have fixed-factor repairs. |
| 9 | WRONG as completed Ref/Pre/Inn | Cutoff linear term; raw shell gauge; joined-chart admission; mismatch-set decay; literal inner read; analytic-radius and power-count replacements. |
| 10 and Outcome | WRONG | Promote these failed implications to supplied consumer inputs. |

Defects ranked by the consumer they break, grouped into **eight** items rather than counting repeated consequences; item 7 is repaired here:

1. **Matched gauge/response jets:** H and S use the Landau response as a raw representative derivative. Keep the node first and second jets or prove a controlled raw lift. This blocks the claimed discharge of Proposition 2.4 and the shrinking-shell substitution. The flat theorem and V survive.
2. **Actual inner Wilson read:** I(b) has not identified the changing factor with the regular background it estimates; SA explicitly distinguishes the retained real inner factor. Keep that action exact and prove the complete-datum/support comparison. This blocks Inn independently of H.
3. **Joined complex datum admission:** 6c-complex composes with the joined chart before the node normalization that makes its datum small. Normalize first, then apply the identity theorem on an established common domain.
4. **Correct mismatch set:** the complex 2.8 replacement needs Theorem M's added-row weight, not decay from every boundary of W. This independently blocks the global R1 sum near other holes.
5. **Cutoff action and zero-free comparison:** complete criticality does not make the cutoff action quadratic; the short slice does not provide the small coefficient increment. Retain `2TH/g` and use the fixed beta radius for the higher coefficients. The corrected analytic implication is written above.
6. **Complex norms, gauges and analytic room:** adjust C's matrix/colour norms and real-cutoff radius, bound complex transport factors, and give the prepared/inner/Q families their actual common interior domains. Fixed-factor changes repair the local contraction; the substitution and Gaussian family identifications remain to be supplied.
7. **Carrier versus site distance — repaired:** the Euclidean warning ignores the half-cell boundary offset. Section 3 proves that the actual source class and the cubical class agree. The reference cutoff uses the stated all-plaquette admission bound.
8. **Logarithmic powers and constants:** the admitted complex radius has exponent q, generally larger than `p_0+2r`. Enlarge the polynomial bound, retain row 107's counting/radius/meet repairs, and choose the ceiling only after every constant and exponent. The repaired asymptotic collection still works conditionally.

**What may be retained:** the exact flat averaging-energy contraction at every depth, the cubical slice/class lemmas, the raw envelope and second-variation identities at non-critical data, the single-top count, the real multiplier estimate with its Ward repair, and the stated conditional minimisation/analytic mechanisms with their explicit repairs. **What may not be changed by this gate:** I4 is not discharged; `sa-2.13-2.md` Sections 3 and 7 still require a gauge-consistent curved reference chart and the literal complex prepared/inner comparison. The full mixed Q and field-dependent denominator remain intact. No status is granted to any premise or scientific claim.

Recovery checkpoint: the opening claims, Sections 1–10, every named lemma/theorem/corollary, and each Section 9 replacement have been covered. All required companion texts were read in bounded ranges; the outline was fetched once. The next repair should start with the node-jet equations in Section 6 or the actual inner-action support in 9d, not repeat Lemma E or V. No subagent, audit, numerical proof, commit, push, PR or external post was used.
