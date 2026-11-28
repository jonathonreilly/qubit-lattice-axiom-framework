# Polydisc holomorphy in the complete account's correlation chapter

Provenance: Codex (GPT-6), 2026-11-05, checkout `dd375b59821629cd805c8a366ad7b6dd606adc16`. Research text, not an audit; grants no status. No computer-assisted proof steps. Not yet checked by another model.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account and outline at `31a47c543775`. Tadeusz Balaban for the random-walk and renormalisation constructions used by that account.

Target: CA-II Proposition `5.6:prop-polydisc-holomorphy`, at 46131, and its missing configuration-domain argument. The supplied reference to a marked (*) is reconciled below.

## 1. Source reconciliation

The proposition occupies CA-II 46131–46165. The next line of prose, 46167, says “Proof outstanding.” Its proposed route continues through 46216. There is no marked (*) in this proposition or route at the pinned revision. Here the target means the three requirements at 46211–46216: the switched operator bound, the substituted-field bound, and inclusion in the term's analytic domain.

The label occurs only at its declaration, CA-II 60284, and CA-III 111237. The latter two occurrences list outstanding proofs. Thus the correlation theorem's dependence is recorded by its chapter input list, not by an additional direct invocation of this label. The mathematical consumer is the hypothesis (H-circle) of `5.6:lem-weight`, CA-II 45154–45181. That hypothesis requires the full independent polydisc, for each fixed datum, and a bound uniform over the specified data. It requires no regularity in the datum.

In the account's notation, the requested assertion is the following. Fix \(\kappa_1\ge1\), \(b\), and the actual data class \(\mathcal D_b\). For every expansion term \(t\), retain its exempt set \(Y_1(t)\), independent variables \(\mathcal V(t)\), and actual localised configuration \(\mathsf R\). After imposing \(\delta_1M\ge\kappa_1\), with \(M\) chosen after \(\kappa_1\), and a sufficiently small last coupling ceiling, one must prove
\[
 F_t(\sigma;\mathfrak d)=t\bigl(\mathsf R(\sigma;\mathfrak d)\bigr)
 \text{ is holomorphic on }P_{\mathcal V(t)}(e^{\kappa_1}),\qquad
 |F_t(\sigma;\mathfrak d)|\le\sup_{\mathcal A_t}|t|
 \quad(\mathfrak d\in\mathcal D_b).
\]
Here holomorphic has the target's meaning of continuous and separately holomorphic. The datum is fixed throughout each holomorphy assertion. Neither the block floor nor the final ceiling permits an upper bound on depth, age, or \(\kappa_1\). This is the target, not a result of this note.

There are two different constructions in this chapter:

* Site (T): `5.6:prop-localized-field`, CA-II 46896–46959, imports Balaban CMP 116 §1. `5.6:thm-full-polydisc` treats the resulting single substituted field.
* Site (L): the target uses the three links of CMP 122b (1.61)–(1.63). CA-II 47718–47745 explicitly separates this construction from site (T). CA-II 48405–48407 also distinguishes the two functions called H_k.

The later theorem `5.6:thm-link-holomorphy`, CA-II 49117–49227, already proves the composition and outer-derivative consequences. Its hypotheses include the actual link analyticity, intermediate domain inclusions, and final membership. Definitions `5.6:def-link-readings` and `5.6:def-link-hypotheses`, CA-II 48143–48330 and 48422–48612, leave these as hypotheses. The scope remark at 49428–49469 says so explicitly. This lane must supply those hypotheses; another proof of the composition theorem would not close the target.

## 2. Comparison with the frozen texts

| Text | What it supplies | Difference from this target |
|---|---|---|
| `hm.md`, Theorem 7, (19)–(27) | Holomorphic Gaussian matrices with a collared real reference on its specified representative class. | Its fixed pair lies in R4 intersected with Rep. It does not construct the three CMP 122b substitutions or admit them in the stage spaces. |
| `pw.md`, §8 and Result | The specified walk sums H(s), H_1(s), and G(s) have norm at most C_PW exp(16 kappa-bar). | It assumes an admitted regular pair, the fixed walk prescription, and parameter geometry (P). Equality with CMP 122b's nonlinear link maps is not asserted. |
| `dr.md`, Theorem 4 | Its specified nonlinear response is holomorphic for source size below epsilon_D exp(-64 kappa-bar), with field/current bound C_D exp(48 kappa-bar) times source size. | The response equations, current, branches and regular-pair admission are explicit hypotheses. These are not identities for the three CA links. |
| `rows.md`, Result and freeze note | Supplies Rows, Pair, the counting multiplier and NL for exactly DR's equations, on their admitted envelope. | Admission and transport remain separate. The general derivative-majorant sketch retained for ABS supplies no new stage-domain theorem. |
| `port/p4-operator.md`, A4 and A9 | Ports CA's conditional free-current operator bounds and analytic walk calculus. | The port retains its named Balaban premises and the application supply conditions of CA-I 49495–49582. |

Setting kappa-bar equal to kappa_1 aligns the parameter radii only. It does not identify the backgrounds, the source slots, the current, or the three link functions. None of these texts already proves the target on its stated data class.

The outline was checked through its index before reading SA 10129–10153, 10354–10403, 10552–10579, 15145–15174 and 15240–15250. These passages distinguish the reduced switched response from the physical equations. They also retain full-polydisc membership as an input. They do not furnish a second proof of the missing CA link supply.

## 3. First attack: transfer the response construction

The most direct CA supplier is stronger than the Gaussian comparison alone. Proposition `4.5:prf-chart-walk-localisation`, CA-I 15265–15469, supplies a switched **nonlinear** chart on its admitted pair class. Its primitive walks carry the factor
\[
 \prod_{\Delta\text{ read by the whole primitive walk}}s(\Delta).
\]
Its conclusions include
\[
 N_\beta(\mathcal H^J(s)(B)),\quad
 |\mathfrak J(s)(B)|_{(-3)}
 \le C e^{c_{\mathbb K}\kappa_1}|B|,
 \qquad e^{2c_{\mathbb K}\kappa_1}|B|\le c_9.       \tag{1}
\]
The proposition retains the covariance-inverse walk input. Its proof pays for switches with the spare walk exponential and uses a contraction for the reduced nonlinear equation. This is ported as an implication, with that premise retained. It is not a new proof here.

I tried to insert (1), or frozen DR Theorem 4, at the three links. The quantitative nesting itself is harmless. Suppose three compatible maps obey
\[
 \|h_i(s;\xi)\|\le B_*\|\xi\|\quad(\|\xi\|<r_*),
 \qquad B_*\ge1,
\]
in the input norm of the next map. If the innermost source has size
\(a<r_*/B_*^2\), the successive sizes are at most
\(B_*a,B_*^2a,B_*^3a\). The first two remain below \(r_*\). This follows by applying the same inequality three times. For DR one may take
\[
 B_*:=\max\{1,C_De^{48\kappa_1}\},\qquad
 r_*:=\epsilon_De^{-64\kappa_1}.
\]
Thus even this coarser bound would only lower the final coupling ceiling. It would impose no upper bound on \(\kappa_1\), depth, or age.

The application fails before this calculation. The required compatibility of the input norms and the actual maps has not been proved. Link 3 substitutes its field both into an argument and into a background. Link 2 retains the gauge \(u_k\). See CA-II 48464–48487. The account names the required identifications in 48249–48303 as hypotheses. Formula (1) is a theorem about its specified chart; it does not identify those other functions with that chart.

There is a concrete algebraic issue in transferring PW. Tagging a product once is not multiplication of tagged factors. For nonzero matrices \(A,B\) with \(AB\ne0\), both reading one switched cube,
\[
 \operatorname{tag}_s(AB)=sAB,
 \qquad \operatorname{tag}_s(A)\operatorname{tag}_s(B)=s^2AB. \tag{2}
\]
They agree at \(s=1\) but not at general \(s\). PW §8 tags its composed Green coefficients once. CA-I 15306–15314 forms further composites after tagging the listed primitive operators. A proof must match the actual CMP 122b prescription at each occurrence; equality of the unswitched physical maps does not do this. Equation (2) refutes that proposed inference, not the target proposition.

**First attack's remaining step:** identify the actual three link formulas, including their auxiliary backgrounds and gauge, with a common admitted complex chart carrying the prescribed switches. Operator bounds on a different chart do not supply this step.

## 4. Second attack: pay for every image with the available radius

The proposed route, CA-II 46191–46208, displays the single-field radius
\[
 \mathsf w_T=\frac{\alpha_2}{4B_0C_1e^{16\kappa_1}\delta_k},
 \qquad \delta_k=(A_1/A_0)\varepsilon_k,
 \qquad \varepsilon_k=g_kp_0(g_k).
\]
The account proves the corresponding site (T) implication in its later single-field results. That fixed \(\alpha_2\) radius does not itself check the stage spaces of site (L). For those spaces the radius also shrinks with the coupling, so the relevant comparison is a ratio. Use the account's quantities
\[
 T_j=\log g_j^{-2},\qquad
 \delta_j=A_1g_jT_j^{p_0},\qquad
 \alpha_{*,j}=C_*g_jT_j^q.
\]
These are CA-II 1754–1812 and 2246–2255. Here \(T_j\) is a logarithm, not the function called \(T(g)\) elsewhere in CA. Put
\[
 a=(1+d+d\beta_0^{\rm pr})r_{\rm pr},\qquad s=q-p_0-a\ge1.
\]
The last inequality is exactly the exponent floor at CA-II 1776–1783. For a fixed amplification \(D e^{c\kappa_1}\), with \(D>0\),
\[
 \frac{De^{c\kappa_1}T_j^a\delta_j}{\alpha_{*,j}}
   =\frac{DA_1}{C_*}e^{c\kappa_1}T_j^{-s}.          \tag{3}
\]
This is the account's shift-to-radius calculation, CA-II 1957–2003, with the displayed possible polynomial loss retained. It is a ratio estimate; using only \(\delta_j\to0\) would be insufficient.

For any fixed \(0<\varepsilon<1\), choose, **after** \(D,c,\kappa_1,q\),
\[
 T_{\rm PH}\ge
 \max\left\{1,2p_0,
 \left(\frac{2DA_1e^{c\kappa_1}}{\varepsilon C_*}\right)^{1/s}\right\},
 \qquad \gamma_{\rm PH}\le e^{-T_{\rm PH}/2}.       \tag{4}
\]
For every \(g_j\le\gamma_{\rm PH}\), (3) is at most \(\varepsilon/2\). No number of scales occurs. In particular a fixed loss \(e^{48\kappa_1}\), or the coarser \(e^{144\kappa_1}\) from three full DR bounds, can be paid at this point in the order. This calculation does not assert that either is the actual loss of the CA maps.

I also tested the loss from a change of level, rather than stopping at (3). The following hand estimate shows what spatial decay would suffice.

**Level comparison.** Let \(m\le j\), \(n=j-m\), and \(x_\ell=g_\ell^{-2}\). Assume
\[
 1<x_j\le x_m\le x_j+C(1+n),\qquad C\ge0,\quad q>0.
\]
The account's ratio formula, CA-II 1968–1976, gives
\[
 \frac{\alpha_{*,j}}{\alpha_{*,m}}
 =\sqrt{\frac{x_m}{x_j}}
       \left(\frac{\log x_j}{\log x_m}\right)^q
 \le\sqrt{1+C(1+n)}.                              \tag{5}
\]
Suppose a stage has room factor \(\rho_m=\beta2^{-n}\), with \(\beta>0\), and the distance from the forcing to this entry is \(d_{mj}\ge D_0n\), with \(\mu,D_0>0\) and \(\mu D_0\ge\log2+1\). Then
\[
 \frac{e^{-\mu d_{mj}}}{\rho_m}
       \frac{\alpha_{*,j}}{\alpha_{*,m}}
 \le \frac{1+2C}{\beta}.                          \tag{6}
\]
Indeed, \(2^ne^{-\mu d_{mj}}\le e^{-n}\). Also
\(\sqrt{1+C(1+n)}\le1+C(1+n)\), and \(ne^{-n}\le1\), since \(e^n\ge n\). These three inequalities prove (6). Combining (3) and (6) pays the loss of stage room by a further fixed factor in (4). The flow upper bound in CA-II 2879–2884 is of the form used in (5), on a monotone portion of its reference chain. No bound for unrelated frozen histories is inferred.

This is still not an estimate for the actual configuration. The stage domain tests seven quantities, including
\[
 |\partial\mathbb U-1|,\quad |\partial U_{p,X}-1|,\quad
 |\mathbb J|,\quad |J_{p,X}|,\quad |\partial U-1|,\quad
 |A'|,\quad |\nabla_U^\eta A'|,
\]
and also requires gauges on specified cubes. CA-I 49594–49625 identifies these entries and the stage weights. A field/current bound for one response is not a bound on \(U_{p,X}\), \(J_{p,X}\), or their gauges. Nor has it been shown that the appropriate \(d_{mj}\) and room in (6) apply to every entry reached by all three links.

I checked the account's apparent supplier, `5.2:cor-response-dilation`, CA-II 13933–14006. It already proves its containment implication. Its hypotheses (a), (b), (f), (g), and (h) require respectively the actual layer holomorphy, layer bounds, absorption inequality, first-order entry estimates, and the auxiliary-field bump estimate. Importing that conclusion for the present link maps without verifying these hypotheses would assume the needed supply.

**Second attack's remaining step:** derive, for the actual link fields on all reached backgrounds, the stage-normalised entry and cube-gauge estimates to which (3)–(6) apply. Small coupling closes the numerical inequalities once those estimates exist. It does not construct them.

## 5. Third attack: use the carrier theorem and continue from real switches

The next candidate was `5.2:lem-carrier-domain`, CA-II 18138–18368. Its conclusion concerns the right stage spaces. But its hypothesis (a) assumes the consumer-domain membership, and (b) assumes that this membership persists for the decoupling families with their switches free. It therefore cannot supply the target without that same application check. The remark at 18353–18368 compares its conclusion with CMP 122b (1.65); it does not remove (a) or (b).

I then tried continuation from the real switch cube. Fix a datum and a target point \(\sigma\) of the complex polydisc. Along the segment
\[
 \sigma(t)=\mathbb1+t(\sigma-\mathbb1),\qquad 0\le t\le1,
\]
openness and a local analytic chart give continuation while the intermediate fields remain in their argument domains. The segment stays in the parameter polydisc by convexity. However, its image need not stay in the configuration domains. At a first exit, strict inequalities alone provide no positive remaining margin. Taking the coupling smaller helps only after a bound relative to those margins has been established.

Here is a hand test of the precise inference being attempted. Let \(R=e^{\kappa_1}>1\), let \(a=R^{-3/2}\), and set
\[
 E_4(s_4)=a s_4,\qquad
 E_3(s_3;w)=\frac{1}{1-s_3w},\qquad E_2=\mathrm{id}. \tag{7}
\]
For every real \(s_4\in[0,1]\), the composite is holomorphic for \(|s_3|<R\), bounded by \((1-R^{-1/2})^{-1}\). For every real \(s_3\in[0,1]\), the same statement holds with \(s_4\) complex. This follows from
\(|a s_3s_4|\le aR=R^{-1/2}<1\).
But at
\[
 s_3=s_4=R^{3/4}<R
\]
the denominator is zero. Thus bounds on the complex sections obtained by holding the other link real do not yield the independent product polydisc. The maximum principle cannot repair this: applying it to the product would already require the missing holomorphy or boundary control there.

Nor does an absolute small-field estimate alone settle the example. Replace \(E_4\) by \(\epsilon a s_4\) and \(E_3\) by \((1-s_3w/\epsilon)^{-1}\), with arbitrary \(\epsilon>0\). The inner field tends uniformly to zero as \(\epsilon\downarrow0\), but the same pole remains. The argument domain shrinks with it. Equation (3) addresses precisely this issue for a matched same-level radius; it has not been supplied for every actual stage entry.

Equation (7) is a counterexample to this continuation inference only. It is not a counterexample to the Yang–Mills maps, the proposition, or Balaban's construction.

**Third attack's remaining step:** give a common bound or domain inclusion at the complex backgrounds actually reached by the inner links. The existing carrier theorem assumes that extension. Local continuation and real-section bounds do not prove it.

## 6. The single remaining supplier and its consequence

The unresolved item can be stated without imposing a global rectangular argument domain on points the construction never visits. This is a slightly weaker supplier than the full domain hypotheses of CA-II 48422–48612. It keeps the same maps and the same independent switch discs.

**Lemma PH-L (actual link domains on reached configurations; open).** Fix the account's admitted source-free inputs and actual term class. Keep their stated premises, including the primitive walk inputs. Choose the constants in the order of CA-II 2791–2873 and 48615–48762: the earlier geometric and analytic constants, \(\kappa\), then \(\kappa_1\), then the allowed block-size floors, then the small argument radii, and finally the coupling ceiling. In particular retain \(\delta_1M\ge\kappa_1\). There is a single positive ceiling \(\gamma_{\rm PH}\), depending only on these parameters and the specified data-size bound, with the following property.

The premises here do **not** include the complex per-link readings or membership assumptions of CA-II 48143–48612, or the decoupling extension in hypothesis (b) of the carrier-domain lemma. Those are precisely the supply being sought. The original term's bounded analyticity on its stated domain remains an input; no estimate for a different term or domain is substituted.

For every admitted history, term \(t\), domain triple \((Y'_2,Y'_3,Y'_4)\), and datum \(\mathfrak d\in\mathcal D_b\), take **exactly** the maps \(\mathcal E_i\) of CA-II 47976–48142. Include the kept gauge \(u_k\), the auxiliary arguments, and the prescribed walk tags. Put
\[
 P_i=P_{\mathcal V_i}(e^{\kappa_1}),\qquad i=2,3,4.
\]
For this datum there are relatively open sets \(\Omega_i\) in the product of \(P_i\) with the corresponding finite-dimensional complex argument manifold, on which the actual link formulas define single-valued jointly holomorphic maps. They contain every reached tuple, in the following exact sense:
\[
\begin{aligned}
 &(\sigma^{(4)},\mathfrak d)\in\Omega_4
       &&(\sigma^{(4)}\in P_4),\\
 &w_3=\mathcal E_4(\sigma^{(4)};\mathfrak d),\qquad
   (\sigma^{(3)},w_3)\in\Omega_3
       &&((\sigma^{(3)},\sigma^{(4)})\in P_3\times P_4),\\
 &w_2=\mathcal E_3(\sigma^{(3)};w_3),\qquad
   (\sigma^{(2)},w_2)\in\Omega_2
       &&(\sigma\in P_2\times P_3\times P_4),\\
 &\mathcal E_2(\sigma^{(2)};w_2)\in\mathcal A'_t
       &&(\sigma\in P_2\times P_3\times P_4).       \tag{PH-L}
\end{aligned}
\]
Here the datum in the first line means its image in the configuration and complex auxiliary slots. Real auxiliary data stay fixed parameters. The set \(\mathcal A'_t\) is the bounded analytic domain of CA-II 48509–48520 and 48608–48612; take \(\mathcal A'_t=\mathcal A_t\) when the whole domain carries the bound. All stage entries, auxiliary fields and cube-gauge requirements are those of the actual inherited domains. No smaller datum class or replacement response is allowed.

For pieces formed with the outer parameter \(t_\square\), the same assertion holds with that parameter adjoined, on \(|t_\square|<R(\mathfrak d)\), for radii with
\(\inf_{\mathfrak d\in\mathcal D_b}R(\mathfrak d)>0\). The outer factor is the one in CA-II 48312–48328. The sets \(\Omega_i\) may depend on the datum and the term. The ceiling does not depend on their labels, the volume, depth, or age. This asks for no continuity in the datum and no extension beyond the open switch polydisc.

This is a statement about the actual configuration maps, not about arbitrary bounded analytic functions \(t\). It includes the unresolved map identification from attack one and the domain control from attacks two and three. These have not been silently assumed separately.

**Conditional deduction, porting the account's proof.** If PH-L holds, Proposition `5.6:prop-polydisc-holomorphy` follows for its actual term class. To check the slightly weaker, reached-domain formulation, fix \(\mathfrak d\). The first line of (PH-L) defines a holomorphic map \(w_3(\sigma^{(4)})\). The map
\((\sigma^{(3)},\sigma^{(4)})\mapsto(\sigma^{(3)},w_3(\sigma^{(4)}))\)
is holomorphic and takes its values in the open set \(\Omega_3\). Composition with \(\mathcal E_3\) gives holomorphic \(w_2\). Repeating this argument with \(\Omega_2\) gives holomorphic \(\mathsf R\). Its range lies in \(\mathcal A'_t\), so the account's local ambient extension of \(t\) gives
\[
 F_t=t\circ\mathsf R\text{ holomorphic on }P_{\mathcal V(t)}(e^{\kappa_1}),
 \qquad |F_t|\le\sup_{\mathcal A'_t}|t|=\mathfrak b_t. \tag{8}
\]
The supremum over the full domain in the target is at least this bound. This is the proof of CA's composition variant and link-holomorphy theorem, localised to the reached tuples. There is no loss of switch radius.

For an outer derivative, the same argument gives joint holomorphy of \(F(\sigma,z;\mathfrak d)\) with bound \(\mathfrak b_t\). For \(0<r<R(\mathfrak d)\), its derivative at zero is
\[
 \frac{1}{2\pi i}\int_{|z|=r}\frac{F(\sigma,z;\mathfrak d)}{z^2}\,dz,
 \qquad \left|\partial_zF(\sigma,0;\mathfrak d)\right|
       \le\frac{\mathfrak b_t}{r}.
\]
Letting \(r\uparrow R(\mathfrak d)\) gives the account's bound
\(\mathfrak b_t/R_*\), where \(R_*\) is the positive infimum above. For an infinite radius the same limit gives zero. On compact switch sets the integrand is continuous on the fixed circle; integrating its local Cauchy formulas proves holomorphy of the derivative. These are exactly CA-II 49181–49225's steps. The weight lemma then applies unchanged. Subtracting a function of \(\mathfrak d\) alone leaves every nonempty mixed switch derivative unchanged. This proves the conditional deduction and nothing about PH-L itself.

## 7. Reading and recovery record

The source searches used the outline index and neighbouring rows in chunks 10, 13 and 16, its obligation list, the CA 4.12–4.19 index, and the CA full index. Bounded source reads supplied the statements cited above. The mechanical PROVED entry for the target was not treated as evidence.

Additional source checks used CA-II 44707–44810 (the term and its data), 45154–45255 (the consumer), 46464–47070 (the single-field inputs and their radius), 47179–47235 and 47554–47666 (single-field conclusions and use), 47718–47848, 47976–48763 (the three-link definitions and hypotheses), and 48988–49469 (composition, use, optional first operation, and scope). The direct occurrences of the target label in all three CA files were checked. They are the three occurrences recorded in §1.

The wider literature record reused `lit-balaban.md`. Local primary text checks used `~/ym4d-papers/cmp109.txt` around (3.31)–(3.54) and `cmp119.txt` around (2.28), (2.34)–(2.39). The statements of CMP 116 and CMP 122b used here were read as reproduced and delimited by the pinned CA; this note does not claim an independent reading of their original full papers. The stopping reason is the mathematical supply in (PH-L), not lack of a paper or a computational experiment.

The next proof attempt should start with link 4's actual function in CMP 122b (1.64), its exact switching rule, and its source and background slots. It must carry the result into link 3's background and argument simultaneously, then retain link 2's gauge. The useful numerical budget is (3)–(6). Re-proving abstract composition, the weight lemma, or a Gaussian matrix estimate will not supply (PH-L).

## Round 1 result (preserved)

**Open lemma**

Lemma PH-L: the actual CMP 122b three-link configurations must have single-valued holomorphic link formulas on neighbourhoods of every reached complex input, with the full independent radius \(e^{\kappa_1}\), intermediate admissibility and final membership in each term's bounded analytic domain, uniformly under one last coupling ceiling. The outer-parameter pieces require the same property with a uniformly positive membership radius. Its exact quantifiers and domains are (PH-L) in §6.

Three new attacks were carried through: transfer of the switched response, quantitative payment of the radii including a level comparison, and carrier-domain continuation. They fail respectively at the actual map/tag identification, the full stage-entry and gauge estimate, and the unavailable complex reached-domain bound. Equations (3)–(6) and the conditional deduction (8) are preserved. No counterexample to the proposition was obtained. The proposition remains unproved here; no T0 obligation is declared closed.

## 8. Second round: the actual links, with multiplicities retained

Continuation provenance: Codex (GPT-6), 2026-11-05, same checkout and source revision. The first round was read in full. Its proofs and unsuccessful attacks are retained above. This round starts at PH-L. It is research text, not an audit, and has not been checked by another model.

The comparison in §2 survives the source check. There is a further distinction. CA-I `4.21:rem-global-chain`, 73545–73635, works with the global carriers at the construction's determining sets. It expressly separates them from the representations at localized determining sets. The latter depend on earlier localization domains. Its last sentence leaves containment for these localized sets undecided. Thus the global-chain result is not an identification of the maps in PH-L. Likewise, `4.21:prop-link-containment`, CA-I 62245–62343, assumes containment at Balaban's decoupling family in hypothesis (a). Its proof begins by retaining that assumption. Neither passage supplies the missing case.

### Fourth attack: expand the nonlinear links before estimating their switches

The first round's equation (2) rules out a literal identification of two tagging prescriptions. It does not rule out a bound for the prescription actually used. I therefore kept repeated switches. The following calculation tests whether nonlinear source degree can pay their cost.

**Coefficient test (proved implication).** Let \(X,Y\) be finite-dimensional complex normed spaces. Let \(\psi\) range over an open background domain. Consider the germ
\[
 h(s;\xi,\psi)=\sum_{n\ge1}\sum_{\tau\in\mathcal T_n}
       s^{m_\tau}C_\tau(\psi)[\xi,\ldots,\xi].                 \tag{9}
\]
Here \(\xi\in X\), each \(\mathcal T_n\) is countable, and each \(C_\tau:X^n\to Y\) is an \(n\)-linear map, holomorphic in \(\psi\). All tags are subsets of one fixed finite set \(\mathcal V\), and \(s^{m_\tau}:=\prod_{\Delta\in\mathcal V}s_\Delta^{m_\tau(\Delta)}\). A term has \(v_\tau\) primitive operator occurrences, lengths \(\ell_{\tau,r}\ge0\), and tag sets \(S_{\tau,r}\). Put
\[
 \ell_\tau=\sum_{r=1}^{v_\tau}\ell_{\tau,r},\qquad
 m_\tau(\Delta)=\sum_{r=1}^{v_\tau}1_{S_{\tau,r}}(\Delta).
\]
Suppose fixed constants \(A,B,\mu,c>0\), \(c_v,c_0\ge0\) give
\[
 \begin{split}
 &v_\tau\le c_v n+c_0,\\
 &\#S_{\tau,r}\le16+c\ell_{\tau,r}/M,\\
 &\sum_{\tau\in\mathcal T_n}\|C_\tau(\psi)\|e^{\mu\ell_\tau}
       \le AB^n .
 \end{split}                                                     \tag{10}
\]
The last bound is uniform in \(\psi\); a bound uniform on each compact background set also gives the local holomorphy conclusion. Here \(A,B\) are constants of this test, not the account's fields or constants \(B_0,B_1\).

Choose \(M\) after \(\kappa_1\), with \(c\kappa_1/M\le\mu/2\). For \(|s(\Delta)|\le e^{\kappa_1}\),
\[
 |s^{m_\tau}|\le
 e^{16\kappa_1(c_vn+c_0)}e^{\mu\ell_\tau/2}.
\]
Consequently, if \(q:=Be^{16c_v\kappa_1}\|\xi\|<1\), (9) converges normally and
\[
 \begin{split}
 \sum_{n,\tau}|s^{m_\tau}|\,
   \|C_\tau(\psi)[\xi,\ldots,\xi]\|e^{\mu\ell_\tau/2}
 &\le Ae^{16c_0\kappa_1}\frac q{1-q},\\
 \|h(s;\xi,\psi)\|
 &\le2ABe^{16(c_v+c_0)\kappa_1}\|\xi\|\quad(q\le\tfrac12).
 \end{split}                                                     \tag{11}
\]

*Proof.* Sum (10)'s tag count over primitive occurrences. Multiply its coefficient bound by the resulting tag bound and by \(\|\xi\|^n\). This gives \(Ae^{16c_0\kappa_1}q^n\), with the remaining half of the length weight displayed in (11). Summing the geometric series proves both inequalities. On each compact subset with \(q<1\), the same summable majorant is uniform. Every summand is holomorphic. Its Cauchy formula on a small coordinate circle passes through the uniformly convergent sum. Repeating for each coordinate proves holomorphy of the sum. No enumeration or computation of the coefficients is used. \(\square\)

This test allows \(s_\Delta^2,s_\Delta^3,\ldots\). It does not replace them by \(s_\Delta\). If (10) holds for the actual stage readouts, both the small source radius and the amplification cost are finite exponentials in \(\kappa_1\). The last coupling choice in (4) can pay them. No number of scales enters (11).

I tried to obtain (10) from CA-I 15265–15469. That proposition already proves the primitive walk bounds and a nonlinear chart bound. Those parts are ported, not proved again here. Its construction expands the current-dependent insertion series before switching. This grouping matters: insertions involving the background current need not add source degree. Counting each such insertion as a separate switched factor would not give \(v_\tau\le c_vn+c_0\). The account instead includes their concatenated walks in its primitive operators, at 15282–15288 and 15346–15420.

For the actual three links, that leaves two unverified parts of (10): a common background domain for the coefficients, and the weighted coefficient bounds for the auxiliary configurations read by the stage spaces. A bound for \(\mathcal H^J\) alone gives neither. In particular, the background of link 3 itself changes with the result of link 4; CA-II 48464–48470 makes this substitution explicit. The coefficient test cannot be applied on the original fixed background domain after that change without proving its admission there.

**Fourth attack's failure.** I obtained the bound for arbitrary repeated tags under (10), but not (10) for the actual nested stage readouts. Neither retagging nor a further decrease of the source radius proves that background admission. The remaining issue is the actual stage-domain estimate, not a combinatorial cost from repeated switches.

## 9. Fifth attack: verify the stage entries directly

I next tried to avoid a full coefficient expansion. Start with the potential bound of the actual response, estimate the retained gauge by its contour, and test the stage entries directly.

The first-order part is already available on its stated domain. Frozen `hm.md`, Lemma 2, proves
\[
 \eta^{-2}\xi^2|\partial\mathbf U_z-\partial U|\le4\alpha,
 \qquad \alpha\le L^2|z|r,
\]
under its displayed smallness conditions and in its supplied real gauges. Frozen `rows.md` §3, (12), gives the corresponding plaquette estimate for \(e^{i\eta h}\mathbf U\). Its complex prefix bounds belong to that same admitted class. These results control the local plaquette calculation once a common gauge has been supplied. They are used here with that condition intact.

### The retained gauge: a contour estimate

CA-II 35584–35599 uses the formula \(g(x)=W'(\Gamma)^{-1}\mathbb W(\Gamma)\) and bounds the two contour products. The following product calculation quantifies the perturbation in that method. It does not identify a new gauge with the actual \(u_k\).

Use a submultiplicative operator norm, with \(\|I\|=1\). Let \(U_1,\ldots,U_m\) be invertible matrices along an oriented contour. Put \(P_0=I\), \(P_j=U_1\cdots U_j\), and assume
\[
 \|P_j\|,\ \|P_j^{-1}\|\le K\quad(0\le j\le m),\qquad K\ge1.
\]
For matrices \(a_j\), let \(\widetilde P_m=\prod_{j=1}^m(e^{a_j}U_j)\). Then
\[
 \widetilde P_mP_m^{-1}
   =\prod_{j=1}^m\exp(P_{j-1}a_jP_{j-1}^{-1}),\qquad
 A_\Gamma:=K^2\sum_{j=1}^m\|a_j\|.                         \tag{12}
\]
Thus, for \(Q=\widetilde P_mP_m^{-1}\),
\[
 \|Q\|,\|Q^{-1}\|\le e^{A_\Gamma},\qquad
 \|Q-I\|,\|Q^{-1}-I\|\le e^{A_\Gamma}-1.                  \tag{13}
\]
If \(A_\Gamma\le1/4\), the power-series logarithm is single-valued near these products and
\[
 \|\log Q\|\le4A_\Gamma.                                  \tag{14}
\]

*Proof.* Insert successive \(P_j^{-1}P_j\) in the product to obtain (12). Submultiplicativity gives the norm bound. The sum of norms of all nonconstant terms in the product of exponential series is at most \(e^{A_\Gamma}-1\). Reversing the order and signs gives the same estimate for the inverse. For \(0\le A_\Gamma\le1/4\), the scalar power series gives \(e^{A_\Gamma}-1\le2A_\Gamma\le1/2\). Hence
\[
 \|\log Q\|\le\sum_{n\ge1}\frac{\|Q-I\|^n}{n}
       \le2\|Q-I\|\le4A_\Gamma.
\]
Products, inversion of the reference matrices, and these normally convergent series are holomorphic wherever their displayed hypotheses hold locally. This proves the analytic assertion too. \(\square\)

In the order of the account's gauge formula, \(g=\widetilde P_m^{-1}P_m=P_m^{-1}Q^{-1}P_m\). Thus
\[
 \|g-I\|,\ \|g^{-1}-I\|\le K^2(e^{A_\Gamma}-1).
\]
This follows by conjugating \(Q^{-1}-I\) and \(Q-I\), respectively.

There is no necessary fine-mesh factor in this estimate. If \(a_j=i\eta h(e_j)\), \(\xi_j\|h(e_j)\|\le r\), and the scaled contour length satisfies
\[
 \sum_{j=1}^m\eta/\xi_j\le D_\Gamma,
\]
then \(A_\Gamma\le K^2D_\Gamma r\). Fixed bounds on \(K,D_\Gamma\) therefore give a gauge bound independent of the number of fine bonds. These bounds, and the identification of the retained gauge with the contour expression, must hold on the backgrounds actually reached. The real-slice contour formula alone supplies neither assertion at a new complex background.

### Why the first-order field estimate does not finish the entry test

The seven entries in CA-I 49594–49625 include currents and auxiliary minimizers. A curvature estimate is insufficient for those entries. Here is a hand test of the proposed shortcut, even in a commuting subgroup of \(\mathrm{SU}(2)\).

Take an even periodic lattice of mesh \(0<\eta\le1\), and put \(T=\operatorname{diag}(1,-1)\). One may take \(\eta=1/(2N)\) on a fixed unit torus, with arbitrary integer \(N\ge1\). Fix \(0<a\le1/4\). Define
\[
 h_2(n)=a\eta(-1)^{n_1}T,\qquad h_\mu(n)=0\ (\mu\ne2),
 \qquad U_2(n)=e^{i\eta h_2(n)},\quad U_\mu(n)=I\ (\mu\ne2).
                                                               \tag{15}
\]
In scale-one units,
\[
 \|h\|_\infty=a\eta,\qquad
 \|\nabla_\eta h\|_\infty=2a,\qquad
 \|\Delta_\eta h\|_\infty=4a/\eta.                              \tag{16}
\]
Each equality follows by subtracting the two adjacent signs. In particular, the first-order norm is at most \(3a\), uniformly in \(\eta\).

The nontrivial \((1,2)\)-plaquette has phase
\(\phi_n=-2a\eta^2(-1)^{n_1}\). Its normalized Wilson action is
\(1-\tfrac12\operatorname{tr}U_p=1-\cos\phi_n\). Write
\(\theta_{n,2}=a\eta^2(-1)^{n_1}\) for the phase of the second-direction bond. Count each plaquette once, in its positive coordinate orientation. The derivative of the sum of plaquette actions at that bond is
\[
 -\sin\phi_n+\sin\phi_{n-e_1}
       =2\sin\bigl(2a\eta^2(-1)^{n_1}\bigr).
\]
Thus the physical current in the normalization
\(\mathcal J_\eta=\eta^{-3}\partial_{\theta_{n,2}}\sum_p(1-\tfrac12\operatorname{tr}U_p)\) obeys
\[
 |\mathcal J_\eta|=2\eta^{-3}\sin(2a\eta^2)\ge2a/\eta.       \tag{17}
\]
For completeness, \(\sin x\ge x/2\) for \(0\le x\le1\): integrate
\(\cos t\ge1-t^2/2\ge1/2\) on that interval. This proves (17) without an asymptotic or numerical evaluation.

This example refutes only the inference from a first-order potential bound to a uniform physical-current bound. It is not a response satisfying the account's defining equations, and it is not a counterexample to Proposition 5.6. It makes explicit the issue described at SA 10576: the switched response uses its reduced current instead of a uniform full Laplacian estimate.

The next attempt was therefore to use \(\mathfrak J(s)\) from CA-I `4.5:prf-chart-walk-localisation`, rather than the physical current of (15). That proposition does bound its own current. But its exactness identities are restricted to \(s\equiv1\), at CA-I 15338–15339 and 15449–15452. It does not identify this current with every auxiliary current \(J_{p,X}\) after the three substitutions. The all-blocks response-dilation corollary, CA-II 13933–14006, explicitly retains the auxiliary-field bump estimate in hypothesis (h). Its bound for entries two and four is not a consequence of its first-order estimate (g).

**Fifth attack's failure.** The contour product is quantitatively controlled once its prefixes and field are controlled. The local plaquette estimate is also available. These do not control the auxiliary minimizer/current entries on the reached backgrounds. Replacing the missing current estimate by a first-order field estimate fails by (15)–(17). Replacing it by the chart's reduced current still requires the actual auxiliary-current identification and domain estimate. No equation of the account is discarded to make that identification.

## 10. Sixth attack: transfer the integrated pieces through their endpoints

The global carriers have the right kind of complex parameter domain, but their determining sets differ. I tested whether their bounds could still supply the actual localization pieces without identifying the functions at every complex parameter.

There is a useful distinction between the target and its product-form pieces. Frozen `dr.md`, Lemma 10, already proves the Boolean interpolation identity. Applied on a face with fixed complementary coordinates \(b\), it gives
\[
 I_W(F;b):=\int_{[0,1]^W}\partial^WF(s_W,b)\,ds_W
   =\sum_{\epsilon\in\{0,1\}^W}
      (-1)^{|W|-|\epsilon|}F(\epsilon,b),                       \tag{18}
\]
for a function with continuous mixed derivatives on that face. This is its repeated fundamental-theorem-of-calculus argument, with the complementary coordinates held fixed. The case \(W=\varnothing\) is evaluation. We use that proved algebra, not an alternative operator construction from DR's still-open Lemma 11.

**Consequence for tags.** Suppose two normally convergent coefficient expansions have identical coefficients and differ only as follows: one tags the union of primitive read sets once, while the other retains the multiplicity of each switch. At every Boolean vertex \(\epsilon\in\{0,1\}^{\mathcal V}\), their individual tags agree, since
\[
 \prod_r\prod_{\Delta\in S_r}\epsilon_\Delta
      =\prod_{\Delta\in\bigcup_rS_r}\epsilon_\Delta.           \tag{19}
\]
The sums therefore agree there. Finite products and compositions preserve this equality where both sides are defined. If a link uses a fixed point, the equality passes through Picard iteration and its limit when both constructions use the same equation, common invariant ball and iteration seed at the vertex. These conditions are needed; equality of unswitched operators alone does not give them.

For every Boolean complementary base \(b\), (18) now identifies their integrated pieces. In particular, if one extension \(G\) is bounded and holomorphic on the required polydisc, the account's weight lemma bounds the common product-form piece by
\[
 |I_W(F;b)|=|I_W(G;b)|
      \le\sup|G|\,r(\kappa_1)^{|W|}.                         \tag{20}
\]
Here \(r(\kappa_1)=e^{\kappa_1}(e^{\kappa_1}-1)^{-2}\), as in CA-II 45154–45160. This applies to the form described at CA-II 44812–44815: earlier-link base variables are one, and variables off the final domain are zero. It clarifies the first round's tag objection. That objection concerns the actual function on the polydisc. A pure change of tag multiplicities need not change these integrated pieces.

I then tried to apply (20) with \(G\) the global-carrier construction. The needed equality is
\[
 t\bigl(\mathsf R_{\rm localized}(\epsilon;\mathfrak d)\bigr)
   =t\bigl(\mathsf R_{\rm carrier}(\epsilon;\mathfrak d)\bigr)
 \quad\text{at every Boolean vertex and every admitted datum}. \tag{21}
\]
It is not enough that both give the unswitched physical term. One sufficient way to prove equality at a masked vertex is to identify the corresponding local operators, backgrounds, auxiliary fields and gauges on every read of the term. A gauge-covariant identification giving the same term would also suffice. Neither identification follows from agreement at the unswitched endpoint.

CA-I 73545–73635 supplies no such identification. The global chain uses the construction's determining sets. The localized chain instead uses determining sets formed on \(Y_1,Y_2,Y_3\), and these depend on earlier localization families. The zero-parameter conclusion of CA-I 15333–15334 says that kernels and equations separate over components. It does not identify those components with the operators and auxiliary minimizers for a changed determining set. Thus (19) cannot prove (21): the coefficients, and not merely their tags, would have to be compared. The original variable set, exempt set and final-domain filing must also be retained for (20) to be the account's piece bound.

There is a second limit even if (21) is eventually proved. Equation (18) transfers product-form pieces, not the proposition's pointwise holomorphy and bound. Nor does it transfer the general pieces with arbitrary probability measure \(\mu\) in CA-II 44802–44804. For example, \(F(s)=s\) and \(G(s)=s^2\) agree at both Boolean endpoints. Their integrated derivatives both equal one, but
\[
 \int F'(s)\,\delta_0(ds)=1,\qquad
 \int G'(s)\,\delta_0(ds)=0.
\]
This hand example concerns the inference, not the account's maps. No counterexample to Proposition 5.6 follows from it.

**Sixth attack's failure.** The endpoint formula removes the pure tag-multiplicity objection for product-form pieces, under explicit matching conditions. The actual localized and global-carrier maps have not been shown to satisfy those conditions, even at masked vertices. Moreover an endpoint transfer would not prove the proposition on its full polydisc or for the weight lemma's general \(\mu\). I therefore keep the actual maps of PH-L and do not substitute the global carriers for them.

## 11. What remains after the second round

No new claim is made about the proposition's truth or falsity. The three attacks above leave exactly the supplier PH-L in §6. The work narrows how to attack it:

* Repeated switch factors can be estimated without changing their prescription. The required quantitative input is a weighted coefficient bound for the actual stage readouts, as in (10), on the backgrounds reached by the inner links.
* The contour algebra itself has the bound (13). The hard part is admitting its actual prefixes and the auxiliary minimizer/current slots on those backgrounds.
* A transfer from the global carriers requires (21) even for the integrated pieces. Equality at the physical endpoint and component separation do not establish it.

The next direct calculation is therefore link 4 with the actual \(\mathbf B_k(Y_3)\) determining set and its auxiliary readouts. Its output must be checked as both the argument and the background of link 3. The analogous check then goes through link 2 with the retained \(u_k\). At each check, the current is the specified current of that map. The physical current cannot be substituted for it at arbitrary switches, and a new reduced current cannot be substituted for an auxiliary current without an identity. This is still PH-L; it is not a replacement hypothesis assumed true.

The constant order remains CA-II 2791–2873 and 48615–48762. Fix the earlier geometry and analytic constants, then \(\kappa\), \(\kappa_1\), the permitted block-size floors, and the small argument radii. Choose the coupling ceiling last. The coefficient test's optional extra floor on \(M\) and source radius have this order. They prove no new ceiling for the actual maps until their hypotheses are supplied. Equations (3)–(6) still give the available small-coupling budget. No bound on depth, age or volume has been introduced.

### Source checks for this round

The existing `/tmp/sa_ym4.tex` and `/tmp/sa_ca_{I,II,III}.tex` were reused; no duplicate download or whole-file read was made. The outline index, its neighbouring rows and `obligations.md` were consulted for regular pairs, switched responses, the reserved walk decay, and the source-bracket membership. The source reads include SA 10129–10153, 10354–10403, 10552–10579, 15145–15174 and 15240–15250. These are background and membership inputs for this lane, not a proof of PH-L.

The CA index was used for the chart, stored-domain and carrier candidates. The new decisive source passage is CA-I `4.21:rem-global-chain`, 73545–73635. Other new or rechecked passages are CA-I 15265–15469, 49594–49625, 62245–62370 and 72988–73078; CA-II 13933–14006, 35578–35601, 44707–44815, 45154–45181, 46131–46216, 47976–48763 and 49117–49469, read in bounded excerpts. The direct occurrences of the target label remain its declaration and the two outstanding-proof lists, at CA-II 60284 and CA-III 111237.

Frozen comparisons were checked at `hm.md` Lemma 2 and Theorem 7, `pw.md` §8, `dr.md` Theorem 4 and Lemma 10, `rows.md` §3 and Result, and `port/p4-operator.md` A4 and A9. The existing literature record `lit-balaban.md` was reused. The local CMP 119 text was consulted near (2.34)–(2.39); its OCR formulas were not used as proof. No claim of an independent full reading of CMP 116 or CMP 122b is added. No computational test supplies any mathematical step above.

## Result

**Open lemma**

Lemma PH-L (§6): the actual three localized CMP 122b link maps must be single-valued and holomorphic near every reached complex input, on the independent switch polydisc of radius \(e^{\kappa_1}\). All intermediate stage clauses and final membership in the term's bounded analytic domain must hold under one last coupling ceiling, uniformly in history, depth, age and volume. Outer-parameter pieces require the stated uniformly positive membership radius.

Three further attacks were completed: coefficient bounds retaining tag multiplicities, direct stage-entry and contour estimates, and transfer through Boolean endpoints. Their failures are stated in §§8–10. The proved additions are the conditional coefficient estimate (11), the contour estimates (12)–(14), the explicit failure of a first-order-to-current inference (15)–(17), and the conditional transfer of product-form pieces (19)–(20). Earlier proved work is preserved. None supplies PH-L. No counterexample to Proposition 5.6 was obtained; its proof remains open here, and no T0 obligation or status is claimed.
