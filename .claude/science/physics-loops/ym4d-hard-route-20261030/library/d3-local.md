# d3-local: locality of new terms and the multiplier current
Provenance: Codex (GPT-6 family; exact serving variant not exposed), requested effort max; checkout `2682cd32b63ed5f4ea0c116516afa0aa687dd522`; Sussman–Alpoge commit `31a47c543775`. Research text; not an audit; grants no status.

Moves: queue row 225, (D3) and the current input of `loc-3.md` Lemma C and Theorem W.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the constructions used below. Sources: [YM4 outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex) (SA) and [YM3_I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex). Line numbers refer to those versions. Both were fetched once. Claude authored `loc-3.md`.

## 1. Source classification before proof

The `(1d)` references survive at SA L3924 and L17541–17548. The pinned file has no section titled *Local Gaussian integration*. Its detailed replacements are the local Gaussian comparison, UM and SI sections below. That title occurs in YM3_I at L37769.

| Object | YM4 passage and short quotation | Classification |
|---|---|---|
| Interaction logarithm | SA L14338–14380, (UM2)–(UM3); L14680–14772, (UM29): “assigned hereditary restrictions”. L14965–15005, (SI7)–(SI8), give the same construction. | **Proved in detail, conditional.** Activities use local Gaussian functionals; convergent connected sums are filed at their union. Heredity and component factorisation remain hypotheses at L14406–14412. The matrix/core inputs remain open at L3926–3937. Cite this implication; do not redo its convergence proof. |
| Gaussian normaliser | SA L17541–17548: “alternating signs”; the summands use regional operator logarithms. L6237–6243 treats the covariance, localisation and logarithm branch as supplied data. | **Sketched.** The regional logarithms must first exist and use only regional data. The finite cancellation is proved in Section 2 below. |
| Kept forms | SA L17550–17558: “connected carriers”. It specifies the Schur chains, their keeping test and their assignment to components. | **Sketched.** Exact locality follows from convergent local chain expansions and the stated keeping test. Positivity is a different obligation. |
| Elimination factors \(z^{(j)}(c)\) | SA L17534 defines their product. L8236–8242: “own double block”; (QC19)–(QC21), (QC25), L8165–8360, construct the pivot inverse and its determinant. | **Proved in detail on the stated chart.** Cite the local coarea formula and its logarithm branch. Formation from an earlier pair still uses the response inputs. |
| First-system multiplier/current | SA L5786–5790: “required independently”. L10404–10410: “formed from the multiplier”. Also (BGD5)–(BGD8), L10007–10076, give an “explicit function”. | **Physical multiplier elimination proved in detail; arbitrary decoupling extension assumed.** BGD6 uses a right inverse of the undecoupled constraint. L10412–10465 gives a second system and limits its identification with the first to physical data. Neither identifies a first-system current on arbitrary independent-current cores. We use BGD6's construction, not claim its absence. |

YM3_I provides more than a heuristic analogy:

- **Gaussian logarithm: proved in detail under hypotheses.** Definition II-19-15, L37890–37958, says the component properties are “required”. Theorem II-19-55, L38144–38183, gives convergence. Proposition `cluster-parameters`, L38505–38576, proves equality of local terms: the conditioning integrals, finite differences and cluster sums “therefore agree”. Its explicit background restriction hypothesis is (II-19-21). The actual Gaussian structure is supplied separately in (II-38-15), L39890–39958.
- **Normaliser and pivots: proved in detail under the regional gap inputs.** Proposition II-44-37, L40674–40949, constructs the “local series” (II-44-14), the regional finite difference (II-44-16), and the pivot logarithm. The component argument and exact determinant identity are at L40892–40944. The history version is explicit too: II-69-13 supplies its regional gap, and II-69-18–19 its locality and determinant identity (L51577–51851). We port only the finite algebra; the three-dimensional analytic estimates are not YM4 inputs.
- **Kept forms: proved in detail under the local-gap and inverse hypotheses.** (II-64-11)–(II-64-15), L51172–51209, define the chains. Proposition II-64-65/75 and its proof, L51211–51335, prove convergence, local coefficients and exact completion of the square. The coefficients read the “pair on $X$”.
- **Multiplier for its coupled system: proved in detail under its operator/nonlinear estimates.** (I-91-62), L49061–49072, specifies both unknowns. Proposition I-91-59, L49055–49179, proves contraction and component locality. The proof retains the “unparameterized identity”, L49131 onward: its component multipliers combine as \(\lambda=-B'+\sum_i\lambda_i^{\rm loc}\), L49162–49168. This is not an identification with YM4's first system away from physical data.

Thus the missing task is a conditional YM4 construction, with its first unavailable input exposed. Rows 214 and 224 do not supply that input. This note does not perform row 224's check.

## 2. Exact locality of new terms

**Claim.** The stated construction implies (D3), once its regional operators, logarithms and summable expansions exist. This proves the algebraic locality step. It does not prove those existence inputs on every move.

Fix a finite cube set \(\mathcal P\); subset sums include both endpoints. Include every read collar in a term's domain. Data means the pair, stored variables, and local history trace. Use (D2) also for the index sets, as [RT] in `um1-fix.md` Corollary R′ requires. Equal local traces must select equal local terms.

**Local Gaussian structure.** This needs the tagged precision and inverse-root expansions too, not only the response walks. SA L14118–14218 sketches these from the operator/core bounds; `h-walk.md` Theorem H gives a conditional precision expansion. At parameters supported in \(Y\), every surviving term has its full read hull in \(Y\). A connected hull lies in one wall-component. The row and plaquette stencils must fit inside that hull. Local sums, products and transposes then split by components. An existing inverse of a block diagonal matrix has the same blocks: multiply the proposed block inverse by the original matrix. Thus the construction
\[
 C=(\chi A(s)\chi^{\mathsf T})^{-1},\qquad
 \Gamma=-\chi A(s)(1-\chi^{\mathsf T}\chi)r(s)
\]
reads only the surviving region. Here \(r(s)\) is its own inverse-root walk series, as at SA L14160–14173. It is not redefined as \(A(s)^{-1/2}\). Block quadratic forms add, so their exponentials multiply. Determinant roots multiply at the positive reference and hence on the chosen analytic branch. Absolute convergence permits Fubini. Exterior auxiliary coordinates integrate to one. This supplies the restriction identity used by the **cited** UM/SI and YM3 cluster-locality proofs. Their conclusion gives the interaction logarithm's part of (D3).

**Normaliser.** Use the intrinsic regional matrix \(A_Y(P|_Y)\), with deep compression, as in YM3 II-44-37 and II-69-13. For a history move, use the tower meet with its sequence and its integration mask. Do not compress the ambient matrix and call it regional. Require its coherent near-real logarithm to exist for every \(Y\subset\mathcal P\). Empty matrices contribute zero. Put
\[
 F(Y;P)=-\tfrac12\operatorname{Tr}\log A_Y(P|_Y),\quad F(\varnothing)=0,
 \qquad
 n_X(P)=\sum_{Y\subset X}(-1)^{|X\setminus Y|}F(Y;P).       \tag{1}
\]
The full-region matrix must be the move's actual precision. Every summand in (1) reads only \(X\). Summing over \(X\subset\mathcal P\) gives coefficient
\(\sum_{X:Y\subset X\subset\mathcal P}(-1)^{|X\setminus Y|}
=(1-1)^{|\mathcal P\setminus Y|}\).
Only \(Y=\mathcal P\) remains. Hence \(\sum_X n_X(P)=F(\mathcal P;P)\) exactly. If centering at \(P_0\), subtract \(n_X(P_0)\) in each slot and retain that slot's constant separately. Such constants can depend on the history; they cannot be discarded as one common number.

The intrinsic tower splits over wall-components. Indeed, a coordinate-monotone cube path reaching another component first reaches the complement, at no greater sup distance. Thus each erosion test is unchanged when made in that component alone. Induction gives the same tower layers. The contained stencils, walks and existing regional inverses then split. Therefore \(A_Y=\bigoplus_i A_{Y_i}\), and \(F(Y)=\sum_iF(Y_i)\). If \(X\) is disconnected, apply this to each \(Y\subset X\) in (1). Each component contribution has the factor \(\sum_{Z\subset X\setminus X_i}(-1)^{|X\setminus(X_i\cup Z)|}=0\). Thus \(n_X=0\). This proves a finite sum over connected polymers. Writing the trace bond by bond recovers the determinant part of (II-68-22). No decay estimate follows from this finite algebra.

**Kept forms.** Write the convergent local expansions as \(\Delta=\sum_\alpha a_\alpha\) and \(C_I=\sum_\beta g_\beta\). Let \(p_I,p_E\) project onto integration and stored coordinates. The conditional form has terms
\[
 p_Ea_\alpha p_E,\qquad
 -p_Ea_\alpha p_Ig_\beta p_Ia_\gamma p_E.       \tag{2}
\]
For each live matrix entry, the intermediate bonds join the factor hulls. Their union is connected and contains both external bonds. Each coefficient reads only that union. Enlarge it by the fixed collar needed for the keeping test. That test asks whether its intersection with \(\Omega\cap Z\) is nonempty and connected, and whether the carrier lies in its one-layer enlargement. All answers use this enlarged polymer alone. Assign the kept term to the component containing that intersection. Its global name is only bookkeeping; it is not a test of distant connectivity. When comparing local pieces, sum over component names, as in YM3 \(K^{\rm kp}(X)\).

Pair (2) with the stored field and group equal polymers. Absolute convergence permits this regrouping. There are finitely many polymers, although each coefficient may contain infinitely many walks. The rejected terms satisfy the same locality argument. This proves the exact split, not positivity of the kept matrix.

**Other normalisers and \(z\)-factors.** Numerical measure factors are assigned to their cells or bonds. This includes the scalar gauge normaliser \(z(\theta,\epsilon)\) at SA L18734–18754; it reads no background. The pivot factors and their logarithms read their double blocks by the cited QC construction. Include those blocks and any earlier-average read hulls in their polymers. Keep products of \(z_c\) as products of local factors; their logarithms are additive terms. If a product must be written as a sum, expand \(\prod_c[1+(z_c-1)]\); each finite product reads its union. A fixed connected enclosure is allowed for this exact identity, but gives no decay estimate. The one-step and stage arguments are identical only after these inputs have been supplied for that move.

## 3. A specified multiplier current with the required locality

Use the existing completion in `wf-room-2.md` (6.1), derived from SA (BGD6). This is a choice of continuation. It is not inferred from agreement on physical pairs. Balaban is also credited for the constrained-response and walk machinery used by these repository notes.

Assume the **field** hypotheses of `loc-3.md` Lemma C. Write \(h=\mathbf H_s\), \(H_s=H(s)\), and \(C'_h=K_h-K_0\) for the nonlinear raw-row derivative. Let \(F'_U(h)\) be the local Wilson force in the chart at \(\mathbf U\). All transposes use the fine physical pairing and counting raw rows, as in `nl-r9.md` Section 4. Define
\[
 \lambda_s^0=H_s^{\mathsf T}F'_U(0),\qquad
 \lambda_s=(I+H_s^{\mathsf T}C'_h{}^{\mathsf T})^{-1}
                    H_s^{\mathsf T}F'_U(h),\qquad
 j_s=R_hK_h^{\mathsf T}\lambda_s-K_0^{\mathsf T}\lambda_s^0.       \tag{3}
\]
Here \(R_h=(E_h^{\mathsf T})^{-1}\) acts bond by bond, with
\(E_hv=\int_0^1\operatorname{Ad}(e^{it\eta h})v\,dt\).
Its inverse exists on the small chart by the geometric series. The independent current remains an argument of \(H_s\) and \(h\); it is not replaced by \(J(\mathbf U)\).

**Existence and walk representation.** Require the absolute Definition D majorant for \(H_s^{\mathsf T}\) to have norm at most \(B\). This is stronger than boundedness of a sum with cancellations. In the same weighted coefficient norms, require the absolute majorant for \(C'_h{}^{\mathsf T}\) to be at most \(cr\), where \(\|h\|\le r\). The [Rows] second-derivative bound gives this from \(C'_h=\int_0^1C''_{th}[h]\,dt\). Take \(Bcr\le1/2\), on the common response ball. Then
\[
 \lambda_s=\sum_{n\ge0}(-H_s^{\mathsf T}C'_h{}^{\mathsf T})^n
                          H_s^{\mathsf T}F'_U(h).                \tag{4}
\]
The absolute majorant is at most \(\sum_{n\ge0}(Bcr)^nB\|F'_U(h)\|\). Thus (4) converges and may be expanded in the constituent walks. Each summand uses Definition D walk terms, their transposes, and local maps only. Products keep their actual parameter monomials, including repeated powers. Replacing them by one tag on the union would change (3) at complex \(s\). At Boolean \(s\), both have the same support test.

**Component locality.** Retain enough of Definition D's enlarged hull to contain every row block touching an endpoint, its plaquettes and the readout stencils. This is the margin in Lemma C; for consecutive local maps use the two-radius floor in `um1-fix.md` (F). For every live product in (4), adjacent walk hulls meet through a local stencil contained in their enlarged hulls. Hence all its walks lie in one surviving wall-component. The force read and the final \(K_h^{\mathsf T}\) readout stay there too. Transposition exchanges endpoints and changes no hull.

At \(s=\mathbf1_{\mathcal K}\), compare one component \(K\) with the problem at \(\mathbf1_K\). The field part of Lemma C gives the same \(h\) on all these stencils. (D2) gives the same walk indices and coefficients. Every summand of (4), and every local readout in (3), therefore agrees. Absolute convergence passes this equality to \(\lambda_s\) and \(j_s\). No value of the pair or datum outside \(K\) was used. This proves the current clause needed by Lemma C **for (3)**.

If the component has no read datum, its field is zero. Then \(C'_0=0\), \(R_0=I\), and (3) gives \(\lambda_s=\lambda_s^0\), \(j_s=0\). The anchor itself need not vanish. At physical \(s=1\), \(K_0H(1)=I\). Thus \(F'_U(0)=\mathbf J=K_0^{\mathsf T}\lambda_*^0\) implies \(\lambda_s^0=\lambda_*^0\). BGD5 identifies \(\lambda_s\) with the physical multiplier. Consequently \(\mathbf J+j_s=R_hF'_U(h)=J(e^{i\eta h}\mathbf U)\). At arbitrary \(s\), (3) asserts no Euler equation \(K_h^{\mathsf T}\lambda_s=F'_U(h)\).

## 4. First input that is not established

For Theorem W's every-move statement, the first unavailable input remains **(D1)**: the specified R9 solution on every required sequence. In particular, `nl-r9.md` (4.4) is an explicit choice of \(W_s\); [RED] identifies that choice with the consumed map. Neither physical agreement nor the multiplier construction above proves [RED]. The named [PW] and regional-domain inputs also remain inputs. No counterexample to their truth is claimed.

Conditional on that field input, (3) closes the current's local construction for the stated completion. It does not identify an unspecified alternative continuation. For (D3), the first additional input is the existence of the **intrinsic regional** Gaussian matrices and coherent logarithms on every move's admitted cores, followed by the stated absolute convergence. The logarithm of the full-region matrix alone is insufficient. For example, the symmetric matrix \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) is invertible, but its one-coordinate compression is zero. This only refutes that shortcut; it is not a Yang–Mills counterexample.

This note chooses (3). The full chain still needs [RED] and the regional Gaussian/core inputs. These hand arguments give conditional locality, not those inputs, uniform current bounds or kept-form positivity. The every-move assertion (D3) remains unproved. No numerical run or computer-assisted certificate supplies a step.

## Result

- **Interaction logarithm and local pivot factors — source check of the outline's proofs:** detailed conditional proofs already exist. Cited and classified in Section 1; their proofs were not independently verified here.
- **Gaussian restriction, normaliser and kept-form locality — proof of steps the outline sketches:** Section 2 supplies the exact algebra using the credited YM3 constructions. Reference constants retain their local slots. The conclusion is conditional on the regional existence and convergence inputs.
- **Multiplier current:** Section 3 proves a step assumed by the outline for the explicit completion (3). BGD6 already proves physical multiplier elimination. Identification with any other independent-current continuation remains open.
- **Corrections:** no correction of a theorem in the outline. In the task's source locator, the current paragraph is L10404–10410, just after L10398–10402. For `loc-3.md`, finite means the outer polymer sum; inner walk and cluster sums require convergence. The first unresolved input remains (D1), then the regional existence part of (D3).
