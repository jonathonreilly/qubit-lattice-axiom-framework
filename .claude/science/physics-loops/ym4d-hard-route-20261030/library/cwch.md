# CW, CH and CM: consumer corrections

Provenance: Research text in checkout `1c6726c10fb6491cce23c755e5b8e70e9a060504`, consumer lane `cwch`; this text grants no scientific or audit status. Source material from the Yang–Mills outline and complete account at `31a47c543775` is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. All deductions below use hand arguments; searches only locate source passages.

Author: Codex. Credit Tadeusz Bałaban for the constructions cited by the account. This is a consumer investigation, not an independent review of those constructions.

## 1. Question and source conventions

None of CW, CH and CM of [open-core.md](open-core.md), §4, closes by an already proved correction. There are useful corrections to the numerical bounds, reached domains and early decay rate, but the actual source-domain suppliers remain missing. The investigation below applies the method of [l17c.md](l17c.md), §§4 and 7: check the weaker theorem against every consumer, including its input class and the order of constants. A conditional implication is not a proved instance of its antecedent.

SA, I, II and III mean the pinned outline and the three complete-account TeX files. Numbers following them are source lines. SA and I were fetched once. The existing II and III copies were checked against the source identities recorded in WD: respectively `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` and `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d`. Index searches preceded bounded source reads. The outline's regular-pair and walk rows, its WF3–WF6 rows, and its full-polydisc obligations retain admission hypotheses; see SA 10129–10137, 10307–10340, 10552–10579 and 15746–15818. The 4.12–4.19 index likewise distinguishes operator conclusions from stage-space supply at I:49495–49625.

The requested output is the only repository file changed. Retrieval and text searches are navigation, not proof. Local file references below are at the pinned checkout.

## 2. CW: what is actually proved

[wd.md](wd.md), “What the stated Route already proves”, (4)–(10), ports the following implications. Put
\[
 D=d^\wedge(\square,R_n),\quad \rho=1+D/(M/M_1),\quad
 p=6r_{\rm pr},\quad c_u=\log(1+3\lambda u+2c_2).
\]
The share bound is
\[
 L_\circ^{6r(\Delta)}\le
 L^{12}\{\check T_k+3+c_{k-t(\Delta)}\}^{p}.                 \tag{W1}
\]
If the window meets inherited raised cells, geometry gives
\(\rho\ge\check R_k-4\) and \(k-n_0+1\le N_*+\rho\), including the exceptional level-\(k\) band. Shares with \(t(\Delta)\ge n_0-2\) are bounded by \(C_{\rm pr}e^{\delta_PD/8}\). Turning these share estimates into an estimate on the actual datum still requires the block-form hypothesis. I:68697–68806 states that qualification explicitly.

The weaker *screened-share sufficient estimate* proved in WD (S), (11)–(14), is the following implication: if both actual normalized data factors satisfy, with a fixed \(K\ge1\),
\[
 l^2(\square)\le K\max\left\{L_\circ^{6s},
 \max_{\Delta\cap\tilde\square^5\ne\varnothing}
 \frac{L_\circ^{6r(\Delta)}}{(1+c_{(n_0-t(\Delta))_+})^p}\right\},          \tag{W2}
\]
then
\[
 d_v(\square),d_{\delta v}(\square)
 \le1+KC_{\rm pr}e^{\delta_PD/8}.                         \tag{W3}
\]
The inner maximum in (W2) is over inherited raised cells. **The implication is proved; (W2) for the actual windows is not.** WD's geometric-discount condition (9) implies (W2), with a fixed constant, but is also an antecedent.

Here is the hand deduction needed by every numerical consumer. Set \(A=\check T_k+3+c_{k-n_0}\ge1\) and \(u=(n_0-t)_+\). The product inequality for \(1+3\lambda u+2c_2\) gives \(c_{a+b}\le c_a+c_b\). Thus (W1) divided by \((1+c_u)^p\) is at most
\[
 L^{12}\left(\frac{A+c_u}{1+c_u}\right)^p
 \le L^{12}A^p\le C_{\rm pr}e^{\delta_PD/8}.               \tag{W4}
\]
The last inequality is the depth comparison in I:68975–68994. Divide (W2) by \(L_\circ^{6s}\ge1\). If there are no inherited cells, the definition gives \(d=1\). This proves (W3) in each normalization separately. It also includes the exceptional band.

The value normalization is \(c_\alpha C_R(E_0+1)e^{C_2\kappa_1}\); the difference normalization is \(c_\alpha C_Re^{C_2\kappa_1}\) times the prescribed difference size. See I:68168–68240 and WD (2)–(3). At zero difference size use the undivided bound. Two value bounds do not prove this Lipschitz-type assertion.

No proved weaker analytic window theorem in WD covers the full source class. Its Result still requires the actual glued minimizer, the unchanged independent current, kernel-class membership, and holomorphy. Its references to native top-stratum windows and to restriction preserve their original domain hypotheses.

### 2.1. CW consumer inventory

The defining account labels are `4.21:def-datum-hypothesis`, `4.21:eq-datum-hypothesis-a`, `4.21:cor-near-group-weight`, and `5.5:not-interpolated-box-field`. The first two specify the numerical demand; the last specifies the analytic window. Searches also used their displayed factors, `C_dat`, `C_inh`, “inherited”, and the windowed-source definition. In the tables, **accepts** means that the stated weaker conclusion supplies the particular consumer, with all its other hypotheses retained. It does not assert the missing antecedent of a conditional lemma. **Needs more** identifies the clause not supplied on the consumer's full input class.

| Consumer and checked source | Exact demand and decision |
|---|---|
| Joint-induction input, I:61482–61512; the coarser-level correlation reading, I:61724–61744 | The third and fourth summable members, including kept differences, use inherited-data control. **Needs more:** the unrestricted, two-normalization version of (W3). The recent-cell share bound supplies only its covered cases. |
| Near-group block weight, I:68487–68560, `4.21:eq-near-group-weight-a` | Needs \((1+C_{\rm dat})L_\circ^{6s}\mathfrak n_0\theta(1+\mathsf p_j/\theta)e^{-3\delta_PD/8}\). **Accepts (W3)**, hence the conditional implication (W2) ⇒ this bound; no geometric power discount is required. The difference version needs its own normalized (W3). |
| Near-group summation and group totals, I:69576–69614, 69648–69692 | Needs the same finite \(1+C_{\rm dat}\) for old-block and window terms, including old blocks with \(s=0\). **Accepts (W3)**. Restricting to recently raised cells or dropping the exceptional band does not cover this consumer. |
| One-anchor sums, I:69812–69825, 69890–69965 | Needs (W3) at old and window anchors; the latter include the exceptional level-\(k\) band. **Accepts (W3)** on every anchor. The source explicitly retains that band. |
| Per-point group total, I:70252–70282 | Uses the near-group block weight, with remaining decay rate \(3\delta_P/8\ge\delta_P/8\). **Accepts (W3)**, by the multiplication below. |
| Small-field constant, I:69172–69202 | Carries \(1+C_{\rm dat}\) inside \(\mathfrak s_J\), including unit sizes. **Accepts any fixed enlarged data constant** at this point in the order; it cannot set that factor to 1. |
| Coupling conditions, I:70427–70462; differences in the machine, I:70537–70586 | The fixed factor \(1+C_{\rm inh}\) remains inside the unit-size constants; the fourth member uses the difference-size normalization. **Accepts a larger fixed \(C_{\rm dat}\)** chosen before the final ceiling. Does not accept an age-dependent factor or a value-only estimate. |
| Format induction and its substitution, I:70950–70990, 71071–71085; final relative-format input, I:73849–73887 | Carries the preceding hypotheses, including both readings of inherited-data control. **Accepts (W3)** with its uniformity; it supplies no additional screening. |
| Preparatory animal resummation, II:13669–13677, 13729–13758, 13866–13888 | Uses precisely \(d\le1+C_{\rm w}e^{\delta_PD/8}\), for members (3) and (4). **Accepts the conditional cellwise table estimate** discussed in §2.3; its own-level membership, remainder and pair-system inputs remain. |
| Correlation theorem's source/boundary input, II:2371–2388, 2791–2812 | Needs the filed relative, \(R\)-born boundary norm on the declared source/window class. **Needs more:** restricting CW's source to a native top-stratum or physical-current subclass does not give that norm. |
| Windowed-source weight lemma, II:35543–35613, followed by local-box regularity at II:35624–35639 | The second/fourth source clauses, the actual \(\mathbb W\), its analytic re-minimization identity, and \((\mathbb W,\mathbb J)\in\mathfrak K_P\) are inputs. **Needs more:** neither share counting nor an absolute field envelope supplies these analytic admissions. |
| Interpolated box field, II:42622–42720; box-read units, II:42750–42782; stored remainder and correction support, II:42860–42958 | Needs the actual analytic \(\mathbb W\), its averages, its response kernels and the specified independent current. **Needs more:** a substitute local field or an unrelated small-field minimizer cannot be inserted into these identities. |
| Remainder constants and theorem, II:43012–43030, 43062–43140, 43885–43915, 44219–44240 | Needs the preceding source properties uniformly, then finite-constant ceilings in \(\gamma_0^\top\), radii and \(\mathsf A_w(\gamma)\). **Accepts fixed numerical losses after a last ceiling**, but still **needs more** for the source maps and their membership. II:44219–44240 explicitly lists those source properties among the inputs. |
| Non-deep later-presentation norm, I:114978–115020, `4.25:lem-norm-bound` | Lists a window statement among the suppliers of its domain hypothesis: the presented point comes from an admitted global \(\tilde P\in\mathfrak K_P^{(k')}\), with a controlled presenting gauge. **Needs actual admission**, together with its separate presentation/gauge inputs. It is not a consumer of the screened-share formula, and that formula alone cannot supply this domain hypothesis. |

These are the distinct uses of the datum bound and analytic window found by the label and bound searches; repeated proof references have been grouped with the statement they prove. The definition/route at I:68420–68485 and the depth lemma at I:68697–69003 are suppliers, not additional successful applications. I:69032–69063 and 69086–69103 explain why the residual and exceptional cases cannot be omitted. Later assemblies consume the group totals, rather than imposing a new numerical version of CW. The similarly named *native-scale* window at I:148788–148871 is a different, conditional statement: its whole window is in the top stratum, and its conclusion uses the step's own current.

### 2.2. The accepted correction and the remaining failure

For the near-group consumer, put \(q=\theta(1+\mathsf p_j/\theta)\). Its pre-WD bound is \(L_\circ^{6s}\mathfrak n_0q\,d\,e^{-\delta_PD/2}\). Then
\[
 (1+C_{\rm dat}e^{\delta_PD/8})e^{-\delta_PD/2}
 \le(1+C_{\rm dat})e^{-3\delta_PD/8}.                 \tag{W5}
\]
This proves the numerical substitution for all rows of the table that use this block weight. Their subsequent sums have nonnegative majorants, so replacing an input by this bound preserves each inequality. The same proof works with \(\mathfrak n_0|_1\) times the difference size. No linearity of the nonlinear near-group map is asserted. This is why (W2), if proved, would suffice, and why the stronger geometric screening in WD (9) is unnecessary.

A fixed loss \(K\) is harmless: choose \(C_{\rm dat}=KC_{\rm pr}\) at the data-constant step, and only then choose the final coupling ceiling. The six supremum conditions of I:70427–70462 already carry this constant. Similarly the remainder ceilings contain finite constants multiplying quantities tending to zero with the coupling; after those constants are fixed their finitely many upper bounds can be met simultaneously. No condition here feeds back into \(L,\kappa_1,M\). This proves the **numerical** correction, conditional on the actual estimate and domain supply.

It does not turn WD's proved weaker bounds into (W2). For a residual cell, set \(u=n_0-t\). With \(\check T_k,D\) fixed, the unscreened available majorant contains \((A+c_u)^p\), which is unbounded as \(u\to\infty\). No fixed \(C_{\rm dat}\), no fixed positive coupling, and no fixed multiplicative change of a radius dominate it by the right side of (W3). This is a failure of inference from that majorant, not a lower bound on an actual datum. The geometry supplies no upper bound on \(u\) (I:68776–68786).

WD (16) does prove an *absolute* envelope for \(w\alpha\) tending to zero with the final coupling. That is enough for some ordinary small-field ceilings in the last table row, but not for normalized screening: small \(w\alpha\) does not make \(w\) bounded. Explicitly, \(w=T^b\), \(\alpha=T^q e^{-T/2}\), with \(b,q>0\), gives \(w\alpha\to0\) and \(w^3\to\infty\). The consumer divides by its stated coupling-scale normalization. Replacing it by an absolute radius would change the relative boundary norm, not prove its bound.

Nor is an age-dependent shrinking of the source a correction of the constant order: it removes points of the declared source, and hence does not control its supremum or the comparison of two expansions there. Native-window restriction also fails to supply the needed domains. Its top-stratum premise excludes the older cells at issue; lowering the native level incurs the factors \(L^{n_0-m}\), \(L^{2(n_0-m)}\) in WD (19). Finally, restriction preserves inner averages, not independence from exterior data: minimizing \((2x^2-2xy+2y^2)/2\) in \(x\) gives \(x=y/2\). This elementary test explains why a re-minimization identity is no substitute for screening or for the independent-current clause.

Thus every numerical consumer could use the weaker logarithmic condition via (W3). It is **not an already proved window estimate**. Nor is literal logarithmic screening necessary: the account has the alternative conditional route below. In either route the full-source analytic window remains an unresolved consumer input.

### 2.3. The stronger conditional cellwise result must not be missed

WD's comparison table also imports [P6](port/p6-correlation.md), “B2b: window-weight proof and inputs”, W5. This is stronger than a recent-share estimate **once its window, own-read, remainder and paired-domain hypotheses are supplied**. In particular, II:35385–35449 (`5.5:eq-weight-d`–`g`) and II:36251–36483 prove the count-times-weight route to (W3). The displayed data-bound search finds this route even though it does not cite the I:68445 label.

Write
\[
 \mathcal K(\square)=\sum_{\Delta'\subset\tilde\square^2}
                         w^\vee(\Delta')^3.
\]
The degree-three table bound and positive linear resummation give, in the notation of II:34549–34587,
\[
 \mathsf T_3(\square)\le\kappa_Rc_W^3\mathcal K(\square)
                                    \mathfrak N_0(\square).       \tag{W6}
\]
Indeed each anchored group at unit weight is at most \(\kappa_R\mathfrak N_0\), and multiplying its nonnegative sizes by at most \(c_W^3w^\vee(\Delta')^3\) multiplies the group's bound by that number. Summing proves (W6). The account's geometry says that inherited cells actually read within one own unit have \(t\ge n_0-1\); residual cells that meet only the fivefold hypothesis window are not such reads. This is a statement about the **admitted near-unit table**, not an assertion that an unconstructed minimizer is independent of exterior data.

The two count bounds in II:35415–35432 are
\[
 \mathcal K\le2(7L)^d\max\{L_\circ^{6s},C_{\rm pr}e^{\rho-2}\},
 \qquad\text{or}\qquad
 \mathcal K\le C^{\rm tile}e^{\rho-1}.                    \tag{W7}
\]
For the second bound the hand estimate is a geometric series with ratio
\(L_\circ^6L^{-4}\le(27L)^{-1}<1\); the remaining factor \(L^{dN_0(t)}\) is bounded by depth as in II:36348–36396. P6 W5-F3 retains the exceptional-depth and finite-supremum checks. Since \(\rho-1=D/w\le\delta_PD/8\), dividing (W6) by \(L_\circ^{6s}\mathfrak N_0\), and taking the maximum with 1, yields (W3) with
\[
 C_{\rm table}\ge
 \kappa_Rc_W^3\{2(7L)^d(1+C_{\rm pr})+C^{\rm tile}\}.      \tag{W8}
\]
All these constants precede \(\gamma\). For differences the same argument applies after dividing the nonnegative size vector by \(\mathsf l^J\), using \(\kappa_R^\times\) and the same row constants. When \(\mathsf l^J=0\), the admitted per-unit bounds and their positive resummation vanish. See II:36743–36796 and P6 W5-F4.

This route can therefore replace the *numerical* screened-share conclusion by a bound on the resummed data factor; it need not prove (W2). But it does not close CW from existing results. Its exact hypotheses are II:35258–35291; W5(a1) reads the source's auxiliary clause, W5(a2) uses the admitted window and its analytic continuation, and the row/difference proof retains own-read and paired-chart containment. Also retain the explicitly excluded low-order counterterm-variation contribution at \(\nu\le2\): II:35489–35494, 36785–36790; P6 W5-C3 carries its separate supplier, rather than declaring the unrestricted difference total proved. None of this supplies \((\mathbb W,\mathbb J)\in\mathfrak K_P\) for every filed source. Using the resulting total to prove its own window or pair-domain premise would be a logical cycle. The unresolved analytic demand in II:42622–42720 survives even if all the other table inputs are retained.

## 3. CH, including CH4-Aux: what is actually proved

The maximal proved package in [ph.md](ph.md) and [ch-bridge.md](ch-bridge.md) consists of the following implications and estimates, with their antecedents retained. There is no proved instance of PH-L for all the actual localized links.

| Proved version | Precise scope |
|---|---|
| PH §3, (1), and its three-map radius calculation | The admitted chart's response/current estimates include finite exponential losses in \(\kappa_1\). If three compatible maps are defined on radius \(r_*\), each has bound \(B_*\lvert\xi\rvert\), \(B_*\ge1\), then input radius below \(r_*/B_*^2\) admits their composition. Compatibility and actual argument domains remain premises. |
| PH §4, (3)–(6); CH-bridge §5, (8)–(9) | A verified normalized bound \(Ce^{c\kappa_1}T^{-s}\), \(s>0\), is made uniformly small by a final coupling ceiling. A shrinking stage margin additionally requires the stated separation estimate; it is not paid by absolute smallness. |
| PH §8, (9)–(11) | Uniform coefficient/length majorants on a common admitted background imply convergence and a bound for the original repeated tags. The floor on \(M\) pays tag length, the source radius pays degree. The required coefficients for the auxiliary stage readouts have not been supplied. |
| PH §9, (12)–(14) | For a contour whose reference prefixes and inverses are bounded by \(K\), \(A_\Gamma=K^2\sum_j\lVert a_j\rVert\le1/4\) gives \(\lVert\log Q\rVert\le4A_\Gamma\). It controls a retained gauge once the actual contour and its bounds are given; it does not construct missing cube gauges. |
| PH §10, (18)–(21) | Product-form mixed derivatives integrated over \([0,1]^W\) depend only on all Boolean endpoint values. A bounded holomorphic extension with those same values transfers the piece bound. Equality at every masked vertex, for the actual nested construction, is a premise. |
| CH-bridge §3, (1)–(2), and §4, (3)–(5) | An exact tangent-current test and an exact changed-constraint formula. They exhibit the current conversion, boundary residual and constrained inverse that an identification must retain. They do not identify the two constructions. |
| CH-bridge §5, (6)–(7) | A uniformly invertible scaled residual with derivative defect at most \(1/2\), small residual \(\varepsilon\), and readout margins gives a holomorphic solution and admission. These estimates must hold for the actual systems on the entire parameter class. |
| PH §6, (PH-L) ⇒ (8); CH-bridge §6, (11) | Single-valued, jointly holomorphic maps on **open neighborhoods of every reached tuple**, with the actual images in the next domains and finally in \(\mathcal A'_t\), imply the weight lemma's hypothesis. No rectangular background domain, boundary continuity, or continuity in the datum is needed. Outer pieces additionally need a uniform positive membership radius. This implication is proved; PH-L remains open. |

The maps in that last row are exactly \(\mathcal E_4,\mathcal E_3,\mathcal E_2\) of II:47976–48142, in that composition order. Their determining sets are \(\mathbf B_k(Y_3),\mathbf B_1(Y_2),\mathbf B_k(Y_1)\). Each has its own independent switch set, of radius \(e^{\kappa_1}\). Link 3 reads link 4's output as both argument and background; link 2 retains \(u_k\) (II:48464–48487). None of these slots can be replaced by an unswitched or global-carrier slot.

### 3.1. CH consumer inventory

Searches covered `5.6:prop-polydisc-holomorphy`, `5.6:lem-weight`, all `eq-weight-*`, `eq-link-readings-*`, `eq-link-hypotheses-*`, `thm-link-holomorphy`, `cor-link-weight` and their displayed bounds, in I–III. The distinctions between the scalar composite, its suppliers and other chains matter.

| Consumer and checked source | Exact demand and decision |
|---|---|
| Polydisc proposition, II:46131–46165 | The actual localized composite has \(H_\circ\): holomorphy and its term bound on the independent open polydisc. **Accepts reached-open-domain CH**, by §3.2; the proposition's stronger closed-domain formulation is unnecessary for this use. No actual supplier of those reached domains is proved in PH/CH-bridge. |
| Weight lemma (a), II:45154–45189; proof II:45310–45356 | Needs only \(H_\circ\), datum by datum, for the actual function. **Accepts the proved composition implication** when its antecedent is supplied. It also accepts a bound after subtracting a datum-only constant for nonempty differentiated sets. It does not need holomorphy in the datum. |
| Fixed-domain count and decay transfer (b),(c), II:45190–45227; link-weight corollary, II:49229–49332 | Needs the preceding scalar bound, \(\lambda^n\) counting and the tree-length inequality. **Accepts reached-open CH** with the original bound. A fixed logarithmic loss in switch radius is payable by an earlier floor on \(\kappa_1\), as proved below. |
| All-final-domains bound (d), II:45228–45265, and subset telescoping (e),(f), II:45268–45300 | Needs the same \(H_\circ\); (d) additionally pays its stated domain-count prefactor or absorption floor. **Accepts the same weaker domain formulation**. It does not justify discarding the prefactor. No new current estimate occurs here. |
| Link-holomorphy theorem (i),(ii), II:49117–49149 | Needs joint holomorphy in parameter and moving argument, actual link-to-link containment and final membership in the domain where \(t\) is bounded. **Accepts neighborhoods of reached tuples**, without full rectangular products. **Needs more** than the admitted chart estimate or field-only bounds. |
| Link-holomorphy theorem (iii), II:49150–49164, 49195–49225 | Needs joint outer-parameter continuation with \(R_*:=\inf_{\mathfrak d}R(\mathfrak d)>0\), and the term bound throughout that disc. **Accepts open discs**, by Cauchy's formula. A fixed reduction of \(R_*\) costs the inverse factor in amplitude; mere positivity for each datum is insufficient. |
| Optional fourth link, II:49333–49413 | Needs the additional \(\mathcal E_1\), its reached argument domain and final four-link membership. **Accepts the same reached-set correction** for the three inner links, retaining those extra hypotheses. It is explicitly unused for the actual three-link pieces; it does not demand a stronger background rectangle for them. |
| Old terms beside a new region, II:59540–59568 | Needs the actual \(U_k^0\) images to remain inside each old term's analytic domain. **Accepts reached-image membership**. A different carrier with the same physical endpoint has not been identified with those images. |
| Correlation-theorem assembly, II:60275–60286, 60328–60339; III:111237–111239 | Uses the polydisc proposition and earlier created-term amplitudes. **Accepts its corrected scalar conclusion**. The amplitude comes from previously completed induction steps; that ordering supplies no new complex map or auxiliary-stage admission. The III occurrence is a standing list, not an extra analytic consumer. |

The single-field CMP 116 theorem and its cluster-term corollary (II:47554–47674, 47718–47746) have the same scalar consumer, but are not proofs for the localized CMP 122b chain. The optional reduced-switch-radius argument at II:47500–47551 is an implication for that single-field setting. The argument below applies its numerical reasoning to a chain **if the chain itself has the smaller-disc theorem**.

CH4-Aux has no separate label in the account: its consumer is the *input domain of link 3* in II:48422–48524 and the reading at II:48262–48294. Those stage domains include the seven entries spelled out at I:49593–49625, particularly \(\lvert\partial U_{p,X}-I\rvert\) and \(\lvert J_{p,X}\rvert\), with their complete stencils, stage coefficients, radius indices, spacing units and \(\mathsf L_0\) factors. **Needs more:** the actual two auxiliary estimates of CH-bridge's Result for every tuple after link 4. This remains a requirement even at outer parameter zero. The all-blocks dilation corollary II:13933–14006 assumes its own auxiliary bump estimates in (h), separately from its first-order estimates in (g); it cannot discharge this input.

There is an important non-consumer to exclude. The global-carrier reading in I:73545–73635, and its later uses at I:76438, 77050, 77083, use different determining systems. The remark expressly leaves localized containment undecided. Likewise I:62245–62343 (`4.21:prop-link-containment`) retains containment at Bałaban's family in hypothesis (a) and has additional stored-domain/tube hypotheses. It is not an independently proved localized supplier of CH4-Aux. Its descendants cannot be used backwards to prove that hypothesis.

### 3.2. Hand proofs of the admissible domain and radius corrections

Fix a datum. Let \(w_3=\mathcal E_4(\sigma_4;\mathfrak d)\). Its graph
\((\sigma_3,\sigma_4)\mapsto(\sigma_3,w_3)\) is holomorphic into the supplied open domain of \(\mathcal E_3\); composition gives \(w_2\). The same argument for \(\mathcal E_2\) gives \(\mathsf R\). These are local assertions at every reached tuple. Compatible single-valued link continuations agree on overlaps, so they give a single function on the whole switch polydisc. The unchanged term is holomorphic on its original \(\mathcal A_t\) and bounded by \(b_t\) on \(\mathcal A'_t\); final membership therefore gives
\[
 F_t=t\circ\mathsf R\text{ holomorphic on }P_2\times P_3\times P_4,
 \qquad |F_t|\le b_t.                                  \tag{H1}
\]
Thus closed-disc continuity and rectangular background domains can be deleted from this supplier without losing any listed scalar consumer. This is exactly the proved implication in PH §6 and CH-bridge §6, not a proof of its domain antecedent.

For the outer variable, integrate on any circle \(|z|=r<R(\mathfrak d)\):
\[
 \partial_zF_t(\sigma,0;\mathfrak d)
 =\frac1{2\pi i}\int_{|z|=r}\frac{F_t(\sigma,z;\mathfrak d)}{z^2}\,dz,
 \quad |\partial_zF_t|\le b_t/r.
\]
Local Cauchy formulas in the switches commute with this compact contour integral, proving holomorphy. Let \(r\uparrow R(\mathfrak d)\); the uniform bound is \(b_t/R_*\). Boundary values of the outer disc are unnecessary. A proved bound on the smaller disc \(cR\), with fixed \(0<c\le1\), would instead give \(b_t/(cR_*)\). The outer size constant can carry that fixed loss before the final coupling ceiling; it cannot carry a factor depending on history.

For completeness, set \(R=e^\eta>1\). Cauchy's formula on origin-centered circles of radii \(R'<R\), at points of \([0,1]\), gives for \(m\) distinct derivatives
\[
 |\partial^WF|\le b\left[\frac{R'}{(R'-1)^2}\right]^m.
\]
Letting \(R'\uparrow R\) and integrating against any probability measure proves the account's factor \(r(\eta)^m\), where \(r(\eta)=e^\eta/(e^\eta-1)^2\). For \(\eta\ge1\), \((1-e^{-\eta})^{-2}\le(1-e^{-1})^{-2}<e\), so \(r(\eta)\le e^{-(\eta-1)}\). Hence if an actual supplier were proved on radius \(e^{\kappa_1-\epsilon}\) with a **fixed early** \(\epsilon\ge0\), fixed-domain decay transfer would require only
\[
 \kappa_1\ge1+\epsilon+\log\lambda+c'a.                 \tag{H2}
\]
The all-domain version likewise uses its original counting test with \(r(\kappa_1-\epsilon)\); a sufficiently large early lower bound meets it. Choose \(\epsilon\) and those bounds at the \(\kappa_1\) step, then the \(M\) floors, argument radii and coupling ceiling. All arrows go forward. A radius known only near the real interval with no positive, uniform logarithmic size does not meet this test. Increasing \(\kappa_1\) is useful only if the smaller-disc supplier holds for all such larger choices.

Numerical response losses are also payable. In the notation of PH (3) and CH-bridge (8),
\[
 K e^{c\kappa_1}T^a\frac{\delta_j}{\alpha_{*,j}}(1+C_o|z|)
 =\frac{KA_1}{C_*}e^{c\kappa_1}T^{-s}(1+C_o|z|),
 \qquad s=q-p_0-a\ge1.                                \tag{H3}
\]
For a prescribed \(\varepsilon_0>0\), choose
\(T_*\ge[2KA_1(1+C_o)e^{c\kappa_1}/(C_*\varepsilon_0)]^{1/s}\)
and \(\gamma\le e^{-T_*/2}\). Then (H3) is at most \(\varepsilon_0/2\) for every running \(g_j\le\gamma\), \(|z|<1\). This is uniform in the number of records. Take a minimum over the finitely many estimate **types**, not over histories. Geometry, \(\kappa_1,M\) and the radius constants were fixed before this last ceiling, so there is no cycle. The formula presupposes the actual normalized estimate; it does not produce it.

### 3.3. Why the remaining weaker statements do not supply CH4-Aux

The failure is not a finite exponential amplification. First, a first-order field estimate is insufficient for an auxiliary current. PH (15)–(17) gives the explicit oscillating one-generator example: an amplitude of order \(a\eta\) has first difference of order \(a\), whereas its current is at least \(2a/\eta\). Even in the scalar difference calculation, \(h_n=a\eta(-1)^n\) has \(|\nabla_\eta h|=2a\) and \(|\Delta_\eta h|=4a/\eta\). Thus a positive mesh-independent ceiling on \(a\) does not establish the missing current bound from those norms. This tests an inference, not the actual CH response.

Second, uniqueness of a minimizer is tied to its determining rows. CH-bridge (3) gives the exact correction for added independent constraints:
\[
 x-x_0=G_0Q_\partial^{\mathsf T}
          (Q_\partial G_0Q_\partial^{\mathsf T})^{-1}
          (b_\partial-Q_\partial x_0).                  \tag{H4}
\]
For \(A=I\), \(Q_0=(1,0)\), \(b_0=0\), \(Q_\partial=(1,\varepsilon)\), a residual \(r\) gives \(x_2=r/\varepsilon\), despite gap 1 for \(A\). A claim of unchanged background based on uniqueness has omitted the boundary residual and this constrained inverse. The actual localized systems need their own estimates; shrinking source size cannot replace a uniform bound on the omitted inverse.

Third, the contraction criterion of CH-bridge (6) proves admission only after those estimates are known. If its solution satisfies \(\|y\|\le2\varepsilon\), and the actual readout has reference margin \(\Delta_e\) and Lipschitz constant \(L_e\), then \(2L_e\varepsilon\le\Delta_e/2\) leaves positive margin. That is the entire implication. If normalization leaves \(2^nT^{-s}\), no fixed positive coupling controls all \(n\); the geometric separation in PH (5)–(6) must be established on the actual auxiliary carrier. Pointwise openness cannot replace the estimate: \(f_n(z)=1-1/n+z\) maps a centered disc into the unit disc only up to radius \(1/n\), whose infimum is zero.

Finally the Boolean shortcut is weaker for **product-form pieces**. Repeated integration of the fundamental theorem of calculus gives
\[
 \int_{[0,1]^W}\partial^WF(\sigma_W,b)\,d\sigma_W
 =\sum_{\epsilon\in\{0,1\}^W}
       (-1)^{|W|-|\epsilon|}F(\epsilon,b).               \tag{H5}
\]
The original tags and once-tagged products agree at Boolean switches. But to transfer a piece one also needs equality of the **actual nested functions at all these masked vertices**, with their differing backgrounds, auxiliary currents and gauges. PH (21) is not proved. Moreover the general weight lemma allows arbitrary probability measures (II:44783–44837): \(F(s)=s\) and \(G(s)=s^2\) agree at endpoints but \(\int F'\,d\delta_0=1\ne0=\int G'\,d\delta_0\). Thus the proved endpoint implication neither gives the general lemma nor identifies the actual product-form pieces.

The needed full clause is therefore actual auxiliary and intermediate admission, followed by final membership and uniform outer room, on the parameters the consumer uses. A direct proof of the scalar \(H_\circ\) bound could bypass this supplier; none of the listed proved results supplies one. This conclusion does not assert that every stronger rectangular-domain clause is necessary.

## 4. CM: what is actually proved

The strongest actual family estimate in [mf.md](mf.md) is §4, Lemma 1, (3)–(5), for the **same cell-resolvent construction of CA §4.4 on its admitted local class**. Retain its datum-independent form-walk majorants (W′), its cells and full footprints, and cell coercivity on every readable cell. With \(\delta=\delta_{\mathsf A}\), \(\gamma=\gamma_*\), set
\[
 \nu=\min\{\delta/2,e\gamma\delta/(16\mathsf B)\},\quad
 \lambda=\nu/4,\quad a_c=\gamma/2,\quad S_\nu=d(1+4/\nu)^d.
\]
Then after successive lower bounds
\[
 8S_\nu\mathsf B e^{-\delta r'/2}\le\gamma,\qquad
 \ell\ge2(r'+2\rho_w)+4,\qquad
 \frac{2\mathsf B S_\nu}{\gamma}e^{-\nu\ell/8}\le\frac12,
 \qquad M\ge48\ell,                                    \tag{M1}
\]
the original labelled resolvent and integrated families obey
\[
 |||\mathsf R^{Y,W'}(x)|||_\lambda\le\frac{4S_\nu}{x+a_c},
 \qquad |||\mathsf M^{Y,W'}|||_\lambda\le\frac{4S_\nu}{\sqrt{a_c}}.
                                                               \tag{M2}
\]
These are absolute family norms; deleting whole labels is allowed. The rate and prefactor precede \(r',\ell,M\), and holomorphy/normal convergence retain the specified local polydiscs. The source construction and its extra local hypotheses are explicit in I:6219–6305. In particular this is not merely a theorem about the sum of a replacement inverse root.

This improves the account's \(r'\)-dependent cell rate, but not the scope of its cells and data. The proof of cell coercivity starts in \(\mathcal S_0\) with trivial traces (I:6681–6687). The broader free-current local-ball theorem still starts from a globally specified real background (I:46103–46127). Neither premise has been shown for every Chapter-5 decomposition with only its prescribed local data.

MF §8, Lemma 3, (27)–(31), is a second actual weaker result: one real local partial form, with current zero and full reading sets contained in \(S\), can be continued using a containing cube \(Q\supset S^{+\ell}\), under its stated real-gauge smallness. It obeys
\[
 \frac34\gamma_0 I\le \mathsf Q_{\rm loc}^b(U,0)\le\gamma_1 I.       \tag{M3}
\]
It constructs that partial form; it does not construct all the companion words at arbitrary independent complex current.

The other strongest results are sufficient implications, not actual uniform envelopes for those words:

| MF result | What it proves, and what remains a premise |
|---|---|
| §7, Lemma 2, (20)–(26) | With \(a=m_1/2\), an original \(n\)-step resolvent word bounded by \(A_\xi[a/(a+x)]^{n+1}\) integrates to at most \(\sqrt a\,c_nA_\xi\), \(c_n=4^{-n}\binom{2n}{n}\). For already compatible holomorphic original words, locally uniform summable majorants preserve holomorphy under integration. The original-word bounds and continuation are premises. |
| §12, Lemma 5, (44)–(47) | Original normalized envelopes with perturbation factor \((1+\eta)^{n+1}\) and nonnegative prefix/step bounds \(p,q\) suffice if \((1+\eta)q<1\) and \(\sqrt a\,p(1+\eta)/\sqrt{1-(1+\eta)q}\le B_{\rm comp}\). A strict reference budget permits a later small \(\eta\); the actual family has not been placed in that budget. |
| §13, Lemma 6, (48)–(49) | The weaker endpoint bound \(E_n\le D(n+1)^{-2}e^{-\mu_0\rho}\) implies integrated size at most \(5D\sqrt a\,e^{-\mu_0\rho}/3\). It avoids a strict geometric contraction, but assumes the original normalized word envelopes and this bound. |
| §11, Lemma 4 | Physical-current and zero-current restrictions, even with all their pulled-back derivatives, do not uniquely specify an ambient holomorphic function of independent current. This is a non-inference result, not a counterexample to continuation of the assigned family. |

### 4.1. CM consumer inventory

The CM word-majorant display is a sufficient supplier formulated in this repository; it is not itself a label in the account. The account consumes its consequence: the **assigned companion** at the actual decomposition has a uniform local exponential bound with constants chosen before widths and \(M\). Searches covered both `2.4:prop-m-freeness` and `5.10:prop-m-freeness`, both defining displays, the companion-kernel phrases, the covariance-root display and all literal `\mu_0` occurrences in I–III. Proof repetitions and unrelated meanings of \(\mu_0\) are separated below.

| Consumer and checked source | Exact demand and decision |
|---|---|
| Order-of-choice definition, I:1201–1204; Stage 5 and Stage 6, I:1500–1551; restatement I:2058–2084 | Widths and the three \(M\) floors read early kernel constants. **Accepts an earlier common positive rate and finite prefactors**, by §4.2. Merely choosing a rate after \(r'\) or \(M\) does not satisfy this use. |
| `2.4:prop-m-freeness`, I:2239–2271 | Needs the companion estimate for **every actual local density datum**, preserving its cell family, uniformly for all larger \(M\). **Accepts an aggregate bound**; it does not ask for the individual \(c_nA_\xi\) criterion. **Needs more** than (M2)'s restricted local class or (M3)'s real zero-current partial form. |
| Order-consistency hypothesis (A2), I:2325–2345, and its application I:2403–2409 | Needs the just-mentioned local validity, not only the formal placement of constants. **Accepts the early-rate correction**, but (M2) does not verify (A2) on its full class. This is the sole use of (A2) in that proof. |
| Rim constants and transfer bounds, II:8513–8555, with admitted-input order II:2412–2443 | Need an early positive rate for the exponential convolution constants \(C_\rho\), then \(K_0,\delta_1,\Theta_1,K_1,\varpi\). **Accepts a smaller early common rate**, recomputing these constants before widths are fixed. No maximality of the Combes–Thomas rate is used. |
| Conditioned covariance root, II:10104–10186, especially `5.2:eq-covariance-root-2` | Needs the true conditioned covariance at \(\sigma=1\); its proved bound is \(2\gamma_0^{-1/2}e^{-\mu_0\rho}\). **Already accepts the proved true-pair result**, and any smaller rate. Its last paragraph explicitly leaves the decoupled family, differences and \(\sigma=0\) reading to the assigned walk expansion. It cannot supply that reading. |
| Positivity-scope/transfer discussion, II:10385–10508 | True pairs use positivity; complex and non-true pairs use the specified kernel and difference bounds. **Needs more:** a true-pair inverse root does not define those local companion values. An early weaker rate is numerically acceptable once the correct kernels exist. |
| \(\psi\)-free remnant rate, II:12346–12357; the \(\delta_1 M\) floors | Needs \(\delta_1M\ge\kappa_1\), with \(\delta_1=\min\{\mu_0/2,\delta_W/2\}\). **Accepts a smaller early rate** by increasing the later lower bound on \(M\). Any separately imposed larger multiple of this floor is handled at the same later step. |
| Old terms beside a new region and repeated proposition, II:59540–59618 | Needs the actual complex local-data companion on the cell family used there, with early constants, for all larger \(M\). **Needs more:** the step marked \((*)\), II:59607–59609, remains outside (M2)'s proved class. A restricted original-cell theorem cannot be substituted without proving inclusion/identification for these instances. |
| Main assembly, III:110846–110860, 111066–111079 | Uses order-consistency and local M-freeness. **Accepts the corrected early-rate formulation**, but supplies no local continuation. The remaining occurrence, III:111410–111412, is an open-statement list. |

No account consumer found uses the binomial weights themselves. Nor does it require that the separately decoupled root equal the root of the decoupled precision; the outline expressly distinguishes them at SA:14159–14169. The actual assignment, locality, parameter monomials and domains cannot be dropped in replacing CM by a weaker aggregate theorem.

### 4.2. The early-rate correction works numerically, with no cycle

MF's failure to recover a *previously fixed* \(\mu_0\) is not by itself an obstruction to every consumer. Suppose the same required global and local companion families were proved with rates \(\mu_g>0\), \(\lambda>0\), in the same prescribed distance, both determined at the kernel-constant step. Any necessary metric comparison must also have a fixed early constant. Set there
\[
 \widehat\mu_0=\min\{\mu_g,\lambda\}>0.                  \tag{M4}
\]
For \(\rho\ge0\), \(e^{-\mu_g\rho},e^{-\lambda\rho}\le e^{-\widehat\mu_0\rho}\). Hence both estimates hold at this common rate. If necessary choose a common early prefactor as the maximum of the two proved prefactors; (M2)'s prefactor is also early. This retains the true-pair bound as a sharper subcase. The originally chosen numerical rate need not be recovered.

For a rate-only correction, substitute \(\widehat\mu_0\) in the printed rim formulas:
\[
 \widehat\delta_1=\min\{\widehat\mu_0/2,\delta_W/2\}>0,
 \quad
 \widehat K_0=\max\left\{
 \frac{2B_{\mathcal A}}{\gamma_0}C_\rho(\widehat\mu_0/2),
 B^2C_\rho(\delta_W/2)\right\}.                         \tag{M5}
\]
Then define \(\widehat\Theta_1=\max\{1,\widehat K_0C_\rho(\widehat\delta_1)\}\),
\(\widehat K_1=\widehat K_0e^{\widehat\delta_1}C_\rho(\widehat\delta_1/2)\), and choose \(\widehat\varpi\) with \(\widehat K_1e^{-\widehat\delta_1\widehat\varpi/2}\le1/16\). These are finite: shell counts on the fixed-dimensional unit lattice grow polynomially, while every rate here is positive. If a prefactor is enlarged too, enlarge each corresponding product/convolution constant at this same step; one does not leave (M5)'s old numerator in place for a kernel whose amplitude has changed. For example
\[
 \sum_z A e^{-a\rho(x,z)}B e^{-b\rho(z,y)}
 \le AB\left(\sup_x\sum_z e^{-c\rho(x,z)/2}\right)
              e^{-c\rho(x,y)/2},\quad c=\min\{a,b\}>0,  \tag{M6}
\]
by the triangle inequality. Thus these finite losses alter early constants only. No listed consumer places an upper bound on such a kernel prefactor; its later width or smallness condition pays it.

Next choose \(r',\ell\) under (M1) and the original floors, and then an allowed power of \(L\) large enough that
\[
 \widehat\mu_0M\ge2\kappa_1,\quad
 \delta_WM\ge2\kappa_1,\quad
 \delta_WM/4\ge32\kappa_1+2\log(LM)+C(d,L),             \tag{M7}
\]
as well as the other \(M\) floors. The third inequality holds for all sufficiently large \(M\), because a positive linear function dominates \(\log M\); once above \(8/\delta_W\), its left side minus \(2\log M\) is increasing. All larger admissible powers then work. Radii and coupling ceilings are chosen afterwards.

In Chapter 2 this is precisely the order in I:1510–1551: kernel constants, widths, \(r',\ell\), \(M\), radii, coupling. Chapter 5's displayed rim order is stricter: its kernel constants precede \(\Theta_1,\varpi\) and even \(\kappa_1,M_1\) (II:2412–2443). The corrected rate must be fixed before the **earliest** width reading. For the particular §4.4 class, this numerical placement is possible: I:6095–6103 fixes \(\mathsf B,\delta_{\mathsf A},\gamma_*,\rho_w\) from \((d,L,G)\) alone, and (M1)–(M2) use only those in their rate and prefactor. For fixed gauge group they can therefore be put in Chapter 5's early \((d,L)\)-group. A rate which genuinely read a later \(M_1,r'\) or \(M\) could not be substituted there. MF Lemma 1 removes that numerical dependence on its class; it still does not identify that class or its metric and words with every later consumer. No numerical cycle arises in the stated conditional substitution. The missing hypothesis matching is separate.

In contrast, after a consumer has fixed a faster rate \(\mu_0>\vartheta\), a bound \(Dt e^{-\vartheta\rho}\) cannot be made at most \(Be^{-\mu_0\rho}\) for all distances by any fixed \(t>0\): their ratio is \((Dt/B)e^{(\mu_0-\vartheta)\rho}\), unbounded as \(\rho\to\infty\). This is MF (42)'s obstruction to a *late* ceiling. Equation (M4) repairs that numerical issue at the early choice; it does not repair a missing family or local domain.

### 4.3. What the original-word criteria would supply

To separate the strong supplier from its weaker consumer, let \(a=m_1/2\) as in I:48012–48017, \(q_a(x)=a/(a+x)\), and keep each original word and its original switch monomial \(s_\xi\). If
\(\|\mathsf R_\xi(x;u)\|\le A_\xi q_a(x)^{n(\xi)+1}\)
on the full required local class, then
\[
 \frac1\pi\int_0^\infty x^{-1/2}q_a(x)^{n+1}\,dx
 =\sqrt a\,c_n.                                       \tag{M8}
\]
For a hand calculation, substitute \(x=at^2\), then \(t=\tan\theta\). The integral becomes
\((2\sqrt a/\pi)\int_0^{\pi/2}\cos^{2n}\theta\,d\theta\).
Integration by parts gives the ratio \((2n-1)/(2n)\), starting with \(\pi/2\); this is precisely \(\sqrt a\,4^{-n}\binom{2n}{n}\). Therefore
\[
 \sum_\xi |s_\xi|c_{n(\xi)}A_\xi
 \le \frac{B_{\rm comp}}{\sqrt a}e^{-\mu\rho}
 \quad\Longrightarrow\quad
 \left\|\sum_\xi s_\xi\mathsf M_\xi(u)\right\|
 \le B_{\rm comp}e^{-\mu\rho}.                          \tag{M9}
\]
Uniform summable bounds on compact sets justify integration and summation and preserve holomorphy. They preserve the prescribed grouping because no label or monomial was changed. This proves why all aggregate-bound consumers accept CM, and why they could also accept another proof of the same aggregate bound without the individual \(A_\xi\) formulation.

For MF Lemma 5 the resulting series is
\(\sqrt a\,p(1+\eta)\sum_{n\ge0}c_n[(1+\eta)q]^n\).
The binomial series is \((1-(1+\eta)q)^{-1/2}\), giving its stated budget. A strict inequality at \(\eta=0\) persists for sufficiently small \(\eta\) by continuity, with no rate change. For Lemma 6, \(c_n\le(n+1)^{-1/2}\): the induction step follows from
\((2n+1)^2(n+2)\le4(n+1)^3\), whose difference is \(3n+2\). Thus the assumed endpoint envelopes sum to at most
\[
 D\sqrt a\sum_{m\ge1}m^{-5/2}e^{-\mu\rho}
 \le\frac53D\sqrt a\,e^{-\mu\rho},                    \tag{M10}
\]
using \(1+\int_1^\infty x^{-5/2}dx=5/3\). Both weaker criteria are sufficient. Neither supplies its antecedent for the actual Chapter-5 companion.

The surviving demand is **continuation and a bound for that assigned family on its actual local independent-current class**. The source explicitly distinguishes the true-pair \(\sigma=1\) root from the decoupled family (II:10182–10185), and explicitly marks the local passage as missing (II:59607–59609). A real zero-current partial form cannot fill it. Nor does agreement on the physical-current graph determine the continuation: for field coordinates \(z\), independent current \(w\), and physical current \(j(z)\),
\[
 H(z,w)=w_1\bigl(w_1-j_1(z)\bigr)K(z,w)                 \tag{M11}
\]
vanishes on both \(w=0\) and \(w=j(z)\), with every derivative of either pullback, yet need not vanish in any open independent-current neighborhood. This is MF Lemma 4's hand test. Shrinking to any positive current radius does not turn either lower-dimensional set into a determining set for ambient holomorphic functions. Setting the radius to zero removes the independent-current inputs the consumer uses.

Consequently an earlier smaller rate, a larger early prefactor, or a smaller positive radius cannot by itself identify (M2)'s words/domains with all instances at II:59574–59586. Such a correction would be valid **if** an inclusion theorem, compatible original-word continuation and the corresponding uniform bounds were supplied; those are precisely not among the proved weaker versions. The remaining obstruction is not the numerical equality to the initially selected \(\mu_0\).

## 5. Coverage and limits of the conclusion

The searches were performed across all three accounts, followed by bounded reads of the displayed statements, their hypotheses and their uses. For CW the additional displayed-bound aliases `5.5:eq-data-factor-a`, `5.5:eq-weight-g`, `5.5:eq-count-weight-6`, `5.2:eq-animal-resummation-10` lead to the conditional cellwise route in §2.3; they must not be mistaken for new unconditional window admission. Windowed-source references in definitions of the three near-unit classes, their constants, input tables, regularity and remainder proofs are grouped under that route and the analytic-window rows. For CH, proof-local repetitions of the weight/link displays add no stronger consumer; the four-link variant and the single-field chain have been treated separately. For CM, the other occurrences of `\mu_0` denote Gaussian/product measures, unrelated numbered majorant factors, an entropy threshold, or unrelated local constants; they are not the Stage-5 companion rate. The literal root prefactor occurs at II:10120 and 10178, both in the true-pair root lemma treated above.

The target is a correction justified by **already proved results on the consumer's inputs**. Proving that a conditional implication is useful is insufficient. Conversely, an open stronger supplier is not shown indispensable merely because it appears in a proposed proof. The tables identify the weaker actual demands: a full-source analytic window plus normalized totals for CW, bounded analytic actual composites for CH, and a compatible actual local companion bound for CM. Each has some removable numerical or domain-strength requirements; each still has an unsupplied input on the required class. No counterexample to any core statement, and no status change, is asserted.

## Result

CW — **still open**: II:42622–42720 and W5(a1)–(a2), II:35543–35613, need the actual holomorphic glued window with unchanged independent current on every filed source; WD and the cellwise count route retain that admission. Numerical consumers accept (W3), without requiring the stronger geometric screening, but this does not supply the missing analytic input.

CH — **still open**: the link-3 input in II:48422–48524 needs CH4-Aux, including the actual auxiliary current and full stage thresholds after link 4. Open neighborhoods of reached tuples suffice for all scalar consumers, and fixed radius/amplitude losses are payable early, but those reached auxiliary bounds and uniform outer room remain unproved.

CM — **still open**: II:59574–59609 needs the assigned companion on every actual local independent-current class for all larger \(M\). A smaller common rate fixed before widths repairs every numerical rate use, but MF's proved cell-family/real-partial-form results do not supply the required family continuation and domain coverage.
