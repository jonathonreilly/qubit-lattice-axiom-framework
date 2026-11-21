# Uniqueness and locality of the constrained minimizer

Provenance: Codex, 2026-11-05, checkout `c04b80758f0ed2cac26749baca173a0dd8a50c4a`. Research text, not an audit; no status granted. Hand proofs only. The three new bridges received a separate Codex reading; the imported theorems were not re-proved or checked by another provider in this session.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`; Tadeusz Balaban for the constrained minimizer construction and CMP 109 Lemma 4.

## Current checkpoint

Target: CA-I Lemma `4.13:lem-minimizer-unique`, lines 45162–45201. Result: a hand proof in the account's regular-real/continued-complex meaning, with explicit amplitude ceilings in its order of choice. The frozen texts alone do not prove its full statement. The proof ports the account's real refinement and literal-frame bound, supplies uniform chart admission, and checks the changed boundary and axial representative. A product-order error in the near-case consumer is identified in §6; the invariant nesting identity and the relative element agree with the account's later convention clarification. The final Result states exactly what has been proved. This file is the current checkpoint; no further mathematical obligation is left open within that statement.

## 1. Sources and exact comparison

The four requested sources were fetched once in this session from the pinned raw URLs. SHA-256:

| Source | SHA-256 |
|---|---|
| [SA outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex) | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| [CA-I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex) | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| [CA-II](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_II.tex) | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| [CA-III](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_III.tex) | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

The source indexes were consulted before the corresponding excerpts. The useful outline entries are chunk 09, especially SA 9591–9625, 9660–9676, 9776–9781, 9842–9849 and 9913–9916, and the matching obligations. These state or sketch the regular-orbit and restriction assertions. They do not supply a proof of the complete-account lemma on its own domains. The complete-account entries are `ca-4.12-4.19/chunk-02.md`, CA-I 45162–45201, and `ca-full/index.tsv`. The status sentence is **Proof outstanding.**

The exact label occurs only at its declaration across CA-I/II/III. Searching the content is therefore necessary. Its first consumer is CA-I 33602–33827, `4.8:prf-near-case-labels`: the first hypothesis is the sub-tower conjugation lemma. In particular, CA-I 33678–33682 asserts regularity, uniqueness and complex-polydisc admission as inputs. CA-I 34241–34418 uses the resulting near-case membership. CA-III 111211–111212 still lists uniqueness and locality as outstanding. The scalar one-power estimates following the conjugation identity are already proved in the account and must be ported, not re-derived.

The other semantic-use anchors checked are CA-I 10607, 29235–29240, 31073–31131, 32422, 121193, 121226, 121389, 121436–121467, 121522, 123126–123129, 129545, 130188, 144933 and 154420; and CA-II 35714, 44422 and 44454. The 4.7 and 4.8 uses require the actual conjugator and its norm cost; later uses carry the identity to junctions, stage composites and local/global comparisons. The last two CA-II citations concern response estimates, which the present proof does not establish. There is no literal label-use in CA-II or CA-III. The table and plan of `port-map.md` and `sa-index/ca-full/README.md` were read before proof work; none of their status entries is changed.

| Target line or clause | Closest frozen statement | Exact difference |
|---|---|---|
| CA-I 45164–45165: the fields and constants of CMP 109 Lemma 4 | `st1-r4.md` 347–359 | ST1 assumes A1/F0/REG and its own admitted separated systems. It does not identify them with every system of CMP 109 Lemma 4. |
| CA-I 45167–45169: unique minimizer | `a1-balaban.md` §§8–9; ST1 Lemma 5 | A1 proves a unique **regular critical residual orbit**, conditionally on F0, for the outline's default determining rows. ST1 selects the mean-contour representative under CV. Balaban uses his average and axial gauge. The averaging maps and row conventions are not interchangeable. |
| CA-I 45170–45175: every allowed subdomain | `a1-balaban.md` §9.2, 2547–2610 | Its extension-of-variations argument treats a memberwise smaller separated sequence. It explicitly proves the boundary and coarse-row assertions for that convention. It does not itself check CA's two tower rules and window margins. |
| CA-I 45185–45191: regularity, criticality, representative | `p82.md` Theorems P/P82, 192–220 | P82 gives an inverse **after** real regular-class admission, under I1–I8. It cannot admit all minimizers or identify their branch by itself. Its counting multiplier and the outline's straightened rows are separate conventions. |
| Actual-step use, PH3 | `hma.md` D6, 281–286; Theorem 8 proof, 373–393 | PH1 supplies a common chart, PH2 criticality for the next constraint, PH3 the branch match, and PH4 matching rows and normalization. The proof consumes PH3; it does not prove it. ST1 can supply it only with its listed admission and restriction premises. |

The source meaning of uniqueness matters. CMP 102b, pp. 278–279, (6)–(8), is a problem on a regular class modulo gauges fixing determining sites. CMP 109, p. 260, (1.1), has the same convention. CA-I 33062–33067 and 38515–38527 specify axial representatives. Complex fields mean the continuation of CMP 102b Proposition 9, not minimization of a complex-valued action. Neither residual gauge copies nor the absence of an order on complex numbers is a counterexample to the statement as used.

Published inputs are credited to Balaban. The existing literature search `lit-balaban.md` was reused. Its later source table distinguishes the proved analyticity assertion from the derivative estimates (189)–(190) printed without calculation. Only the former is used in this proof. The relevant paper-folder OCR excerpts include CMP 98 pp. 23–26, 37–39, 42–43; CMP 102b pp. 277–281, 301–303, 305–309; CMP 109 pp. 256, 260–263, 274–280. Formulas damaged by OCR are not treated as exact quotations.

## 2. What the account already supplies

1. **Tower geometry:** CA-I 32839–33043 defines both rules, proves their separation and collars, and gives locality of the layered datum. The tower of a subdomain is intrinsic to that subdomain.
2. **Real refinement:** CA-III 36939–37007, Lemma `9.3:lem-refinement`, proves the refinement implication using the composition of averages and CMP 102b Theorem 1. This is a port, not a new proof of that lemma.
3. **Analytic continuation:** CA-I 38500–38673 records the real admitted set, the chart set \(\mathcal S(\mathcal T)\), the orbit extension, and the existence set \(\mathcal V(\mathcal T)\). CA-I 39170–39277 proves holomorphy **on that existence set**. It does not prove that every restricted window field belongs to it.
4. **Gauge algebra:** CA-I 129758–129790 fixes \(U^h(b)=h(b_-)U(b)h(b_+)^{-1}\), hence \((U^a)^c=U^{ca}\). CA-I 130021–130176 proves the tree formula for the relative gauge. Its remark at 130178–130191 explains the mirrored convention. Products below must follow the stated action, not a silently reversed convention.

## 3. Precise conventions and the reduction

Throughout this argument the averages are Balaban's actual group averages, and the auxiliary nonlinear potential average is his \(Q\). The outline's symmetrised replacement is not substituted. The input window is \(\square _0=\tilde\square ^5\). The domain in the nesting assertion is a subdomain \(Z\subset X\subset\tilde\square ^2\), where \(X\) is the output domain of CMP 109 Lemma 4. This is exactly the reading in CA-I 33602–33618 and 33654–33676. It is not a claim about freely changing boundary conditions at the edge of the input window.

Write \(\mathcal T=\boldsymbol\Omega^{\mathfrak r}(Z,n)\), for either of the two rules, with \(1\le n\le p\le j\). All block grids, roots, outward bonds and seam readouts retain the source conventions. Empty terminal members are allowed. The outer depth-\(j\) tower is \((\square_q)_{q\le j}\). In the outer problem's own units its top block has side one and its fine spacing is \(\xi_j=L^{-j}\).

For independent outer data \(D\), use the account's notation
\[
 W_j(D)=U_j(\square_0,e^{iD})
       =\mathcal U_j(D)^{u_j(D)},\qquad
 \mathcal U_j(D)=e^{i\xi_j H_j(D)}.                 \tag{3.1}
\]
The potential and the Landau-to-axial map here are the functions of CMP 102b §G, Proposition 9, at base datum \(1\). No uniqueness of arbitrary complex critical points is claimed: at complex data the definition is the specified analytic continuation, as in CA-I 38500–38680.

The proof has two quantitative tasks. First establish nesting for **every** \(D\) in a fixed ball, uniformly in the towers and depths. Then put the actual datum \(D=\tau B+B'\) of CMP 109 (3.30), (3.53), including the proof radius \(|B'|<2\alpha _3\), in that ball. This avoids assuming that openness of the existence set gives a uniform radius.

## 4. A common chart and admission of the restricted data

### 4.1 The value bound needs no derivative-decay theorem

Fix a positive \(\varepsilon_*\) below the thresholds of CMP 102b Theorem 1 and §G, and below the account's already chosen \(\bar\varepsilon _1\). Decrease it so \(B_3\varepsilon_*<a_0/4\). The identity datum satisfies (7) with this positive parameter on every admissible tower. Equation (172) and Proposition 9 therefore give a number \(r>0\), independent of depth and domain, such that the base-one chart exists for \(\|B\|_\infty<r\). Choose \(r\le\min(1/4,C_1\varepsilon_*/4)\); then \(\|e^{iB}-1\|<C_1\varepsilon_*\). All logarithms are in the fixed identity chart of the fixed group \(G\); shrink the group-neighbourhood radii if needed so their logarithms lie in \(\mathfrak g^c\). Here and below a norm on a datum is the supremum over its actual determining bonds.

For a tower \(\mathcal S\), put
\[
 N_{0,\mathcal S}(F)=\sup_b\ell_{\mathcal S}(b)|F(b)|,
\]
where \(\ell_{\mathcal S}\) is the local block side. The first inequality of (19), with (173), gives
\[
 N_{0,\mathcal S}(H_{\mathcal S}(B))\le B_5\varepsilon_*
                  \quad (\|B\|_\infty<r).        \tag{4.1}
\]
Moreover \(H_{\mathcal S}(0)=0\): the identity is the axial minimizer, the corresponding Landau field is zero, and §G fixes that branch.

For completeness, restrict this holomorphic map to \(zB/\|B\|_\infty\), \(|z|<r\), and apply the scalar Schwarz inequality to every norm-one linear functional of its weighted bond value. Taking the supremum over bonds and functionals proves
\[
 N_{0,\mathcal S}(H_{\mathcal S}(B))
       \le K\|B\|_\infty,\qquad K=B_5\varepsilon_*/r,
       \quad \|B\|_\infty<r.                    \tag{4.2}
\]
Using \(2K\) instead makes no difference if the chart was initially specified on an open smaller ball. This is a hand argument in each finite-dimensional configuration space; the constants do not involve its dimension. It uses the value and analyticity assertions of Proposition 9, not the derivative estimates (189)–(190) whose calculations are omitted in the paper.

### 4.2 The averaging estimate in the units of its output block

Port CMP 98 Proposition 6 at reference \(U_0=1\), together with Proposition 4 for the auxiliary \(Q\). There are \(a_{98}>0\) and \(C_A\ge1\), fixed at \((d,L)\), with the following consequence. Let a level-\(q\) output bond have side \(s\), fine spacing \(h\), and two-block carrier \(E\). If \(F\) is complex and
\[
       s\sup_E|F|<a_{98},
\]
then both the plain averaged datum and the auxiliary potential average are defined and holomorphic there, with
\[
 \left|\frac1i\log M^q(e^{ihF})(c)\right|
       \le C_A s\sup_E|F|,\qquad
 |Q_q(hF)(c)|\le C_A s\sup_E|F|.                \tag{4.3}
\]
These are two bounds, not an identification of the two maps. To check the units, replace the fine spacing by \(h/s=L^{-q}\) and the potential by \(sF\). The background has zero curvature, so the hypothesis (52) is automatic. Proposition 6 and (159)–(164) apply to the plain average; Proposition 4 and (131), (134)–(135) apply to \(Q\). Shrink \(a_{98}\) so the group error is less than \(1/2\); the power-series estimate \(|\log(1+E)|\le2|E|\) gives the displayed logarithm. The two-block locality is CA-I 24239–24405. Values outside the carrier may be extended by zero when applying the uniform theorem. No bound on derivatives of \(F\) is needed here.

All inner carriers and axial-tree carriers lie in the outer top region. The geometric reason is that \(Z\subset\tilde\square ^2\), whereas \(\square_j\supset\tilde\square ^4\); the two layers between them exceed the diameter of the level-\(j\) blocks and their nearest-neighbour carriers under \(M\ge2LR_1M_1\), \(R_1\ge4d\). In the units used in the window construction the layer side is \(M\), and the largest block side is at most \(L\), so even a two-block carrier has length at most \(2dL<2M\). The same inclusion holds for every \(Z\subset X\), including domains with holes. The inner gap supplies its own fine frozen collar.

On the outer top region (4.2) is \(|H_j(D)|\le K\|D\|_\infty\). A level-\(q\) inner block has side \(L^{q-j}\le1\) in those units. Hence (4.3) gives, simultaneously on every determining row of every inner tower,
\[
 \|B_{\mathcal T}(D)\|_\infty
 :=\left\|\frac1i\log M_{\mathcal T}
                 (\mathcal U_j(D)|_Z)\right\|_\infty
 \le C_AK\|D\|_\infty .                        \tag{4.4}
\]
The level-zero rows satisfy the same inequality directly. Choose \(\delta>0\) so
\[
 \delta<r/2,\quad K\delta<a_{98}/2,\quad
 C_AK\delta<r/2 .                              \tag{4.5}
\]
Then the **whole** ball \(\|D\|_\infty<\delta\) maps into the base-one chart of every \(\mathcal T\), with margin. In particular it maps into the existence set defined in CA-I 38650–38673. This is stronger than merely knowing that this set is open.

For real data a further fixed decrease of \(\delta\) will be made in §5. All choices so far depend only on the previously fixed analytic and geometric constants, never on \(j,n,p,Z\).

## 5. Real restriction, including the change of action domain

Let \(D\) be real with \(\|D\|_\infty<\delta\). Decrease \(\delta\) so \(L\delta<a_{98}/2\). The plaquette and seam tests (7) of CMP 102b for \(e^{iD}\) are bounded by \(C_D\|D\|_\infty\), with a fixed \(C_D(d,L)\). Indeed an ordinary factor has distance at most \(\|D\|_\infty\) from one. A seam replaces a missing factor by the prescribed one-level finer average. In that finer lattice's units, (4.3) gives its logarithm size at most \(C_AL\|D\|_\infty\). All these factors are unitary, so telescoping the four factors gives the bound with \(C_D=4C_AL\) (or any larger fixed constant). The separation excludes a jump over arbitrarily many levels at a seam. This is the same seam convention as CMP 102b p. 278, (7), and CA-I 18616–18620.

Theorem 1 gives
\[
 W_j(D)\in\mathfrak U_j(\boldsymbol\square,\epsilon_W),
       \qquad \epsilon_W=B_3C_D\delta.          \tag{5.1}
\]
Let \(C_7\) be the converse data-test constant from CMP 98 Proposition 2 and CMP 102b p. 278, as fixed in CA-I 17533. Decrease \(\delta\) so that
\[
 C_D\delta<a_1/2,\quad
 C_7\epsilon_W<a_1/2,\quad
 B_3C_7\epsilon_W<a_0/2,\quad
 \epsilon_W<a_0/2 .                            \tag{5.2}
\]
This explicitly pays for the second application of Theorem 1; the two occurrences of \(B_3\) are not dropped. Both applications may use the regular uniqueness ceiling \(\varepsilon_0=a_0/2\), since their minimal-orbit radii lie strictly below it.

Make a refined tower on the **same outer domain**:
\[
 \widehat\Omega_0=\square_0,\qquad
 \widehat\Omega_q=\Omega_q^{\mathfrak r}(Z) (1\le q\le n),\qquad
 \widehat\Omega_q=\varnothing (n<q\le j).     \tag{5.3}
\]
It is admissible. Its first separation follows from the inner separation and \(Z\subset\square_0\); all later non-vacuous separations are the inner ones. It is memberwise smaller than \(\boldsymbol\square\), since \(Z\subset\square_j\). Rule 2 is admissible with the propagator block \(\mathfrak M\) as already proved in CA-I 32975–32985; both towers may be read at the common gap threshold \(R_1\). Thus the two rules cause no mismatch in applying the theorem. Empty terminal layers can simply be discarded, leaving the same determining rows and action; if \(\Omega_1(Z)\) is empty, every inner fine bond is prescribed and the restriction assertion is immediate.

Port CA-III Lemma `9.3:lem-refinement`, 36939–37007, to (5.3). It gives that \(W_j(D)\) is a regular critical minimizer for the refined data \(M_{\widehat{\mathcal T}}W_j(D)\). This imports precisely its fiber inclusion for the **actual** averages, with their seam rows. It does not assert that a minimizer is generally insensitive to boundary data.

Now let \(V(t)\) be a differentiable constraint-preserving inner curve through \(W_j(D)|_Z\). Extend it by the fixed outer field. The level-zero shell of the inner tower fixes every potentially changing bond except bonds touching \(\Omega_1(Z)\). The first inner separation puts every plaquette containing a changing bond inside the inner action domain. Thus
\[
 \left.\frac d{dt}A_{\square_0}(\widehat V(t))\right|_{0}
 =\left.\frac d{dt}A_Z(V(t))\right|_{0}.        \tag{5.4}
\]
All other plaquette terms are fixed. The extended curve preserves the refined constraints: its positive-level rows are exactly the inner rows, and every extra level-zero row is fixed. For small \(t\) it stays in the regular open class of the refined problem, since the base field is strictly inside that class. Consequently the left side of (5.4) vanishes. This verifies the change of action domain; the same-domain refinement lemma alone would not have done so. It is the boundary mechanism of our `a1-balaban.md` §9.2, now checked on the complete account's actual towers and rows. Its use here does not import that note's different averaging convention or its F0 premise.

Local scales in the inner problem only decrease. The curvature and current bounds of \(W_j(D)\) therefore imply its membership in the inner regular uniqueness space. By Proposition 2 of CMP 98 with the seam convention, the inner datum has test parameter at most \(C_7\epsilon_W\). Equations (5.2) give all hypotheses of Theorem 1 for the inner problem. Its unique critical orbit is its minimal orbit, so \(W_j(D)|_Z\) belongs to it.

There is no residual ambiguity in the axial representative. The inner hierarchy uses a subset of the globally aligned trees on which the outer axial field and its iterated averages equal one. This follows since its blocks have levels at most \(n\le j\) and all those blocks lie in the outer top region; see CA-I 130021–130050. Therefore \(W_j(D)|_Z\) is already inner axial. A residual gauge taking one such representative to another equals one at each determining root. The tree equations force equality of its values along every tree edge, successively at every level; it is thus one throughout each block and on the fixed shell. This proves the literal equality
\[
 U_{\mathcal T}\bigl(M_{\mathcal T}(W_j(D)|_Z)\bigr)
                      = W_j(D)|_Z .             \tag{5.5}
\]

Finally, every attained real minimizer in the problem's regular open space is critical: along every admissible two-sided differentiable curve its action has derivative zero. Theorem 1's uniqueness space contains that problem under its stated smallness ceiling \(\varepsilon_0\le a_0\). Hence **every** such minimizer is on the same orbit, and axial normalization gives exactly one. This does not make a statement about minima outside Balaban's regular variational space.

## 6. Complex nesting and the order of the gauge factors

Let \(\bar u_{\mathcal T}(D)\) be constant on each structure block of the inner tower and equal to \(u_j(D)\) at its root; on the fixed fine shell it is \(u_j(D)\). For real \(D\), covariance of the actual averages and CMP 102b (181), followed by (5.5), give
\[
 \begin{split}
 U_{\mathcal T}\bigl(M_{\mathcal T}(\mathcal U_j(D)|_Z)\bigr)
 &=\bigl[U_{\mathcal T}(M_{\mathcal T}(W_j(D)|_Z))
                                      \bigr]^{\bar u_{\mathcal T}^{-1}}\\
 &=(W_j(D)|_Z)^{\bar u_{\mathcal T}^{-1}}\\
 &=(\mathcal U_j(D)|_Z)^{\bar u_{\mathcal T}^{-1}u_j}.
 \end{split}                                                   \tag{6.1}
\]
Both sides of the first-to-last equality are holomorphic on the entire ball \(\|D\|_\infty<\delta\). For the left side this is (4.4)–(4.5) and the actual inner base-one chart, not an assumed continuation outside its domain. For the right side it is §G's holomorphic outer field and gauge, root evaluation, and matrix inversion. They agree on an open real slice. Apply the one-variable identity theorem successively in a real basis of the finitely many Lie-algebra coordinates, then analytic continuation in the connected ball. Equation (6.1) holds everywhere in that ball.

This also explains the convention issue in the account. Under its stated action \((U^a)^c=U^{ca}\), the acting element is
\[
             g_{\mathcal T}=\bar u_{\mathcal T}^{-1}u_j .         \tag{6.2}
\]
The product \(u_j\bar u^{-1}\) printed in CA-I 29236, 31077, 31110, 33615, 33686–33689 and 121436–121437 is reversed for this action (the account uses the correct order at 121440 and 123129, and its remark at 130188 covers it). The correction is not load-bearing: every consumer uses only the norm of \(\mathrm{Ad}_g\), which is the same for both orders. It is the product for the mirrored action discussed explicitly at CA-I 130178–130191. Equation (6.1), rather than a bare product name, removes the ambiguity. Both products have the same bound obtained by multiplying the norms of the two factors, but they need not act identically. No assertion of their equality is used here.

Curvature and the local current transform covariantly. Thus, on the source's corresponding plaquette/current domains, (6.1) gives
\[
 \partial U_{\mathcal T}=R(g_{\mathcal T})\partial\mathcal U_j,
 \qquad J_{n,\mathcal T}
      =(L^n\xi_j)^3R(g_{\mathcal T})\mathcal J_j .                \tag{6.3}
\]
The second factor changes the current to the inner top-block units. These are the identities used at CA-I 33691–33698 and 31106–31131. The norm costs already calculated there apply also to (6.2), because both use the same bounds for \(u_j^{\pm1}\) and \(\bar u_{\mathcal T}^{\pm1}\). Their scalar curvature/current estimates are ported, not proved again here.

## 7. Putting every actual Lemma 4 datum in the ball

Here it is essential to use a bound on **all** the window determining rows. CMP 109 (3.32) on \(\tilde\square^4\) alone would not suffice.

Port only (AX1), (AX2-poly), and the first, chart-admission paragraph of (AX3) from CA-I Lemma `4.5:lem-literal-frame`, 17519–17597 and 17673–17778. For the literal generalised axial datum \(V\), they give on the whole input twist polydisc
\[
 \|V-1\|_\infty\le C_VM(\alpha_0'''+\alpha_1'''),\qquad
 \|B_V\|_\infty\le 2C_VM(\alpha_0'''+\alpha_1'''),\quad
 B_V=\tfrac1i\log V .                                           \tag{7.1}
\]
The map is precisely the literal frame of CA-I 17322–17447, not the alternative fine frame. Those clauses' proof uses real CMP 98 Proposition 2, complex Proposition 6 about that real field, and explicit finite contour products. It does not use (AX2-pt), the unproved complex-curvature strengthening, the glued-background conclusion, or the sub-tower identity being proved. Conditions (i)–(ii) of the input space supply its real field and twist; (iii) and the output hereditary clause are not used to obtain (7.1). The definition of the twist polydisc and its inclusion of the actual field are CA-I 17433–17460.

Impose \(2C_VM(\alpha_0'''+\alpha_1''')<r/2\). Then apply (4.2) to the incoming depth-\((k+1)\) chart at \(B_V\). This bounds its Landau potential in **every** layer, including the collar, by \(K\|B_V\|_\infty\) in that layer's unit. No estimate based on the unprinted derivative-decay calculation is used.

Consider now one actual row of the truncated outgoing depth-\(j\) datum. A level-\(q\) row and its two-block carrier lie in \(\square_{q-1}\) if \(q\ge1\), even when the row is outward at \(\partial\square_q\). To verify this, use alignment: its second block is either inside \(\square_q\) or is the adjacent block across one face. Its points are at most one level-\(q\) block side from \(\square_q\). The separation from \(\square_{q-1}^c\) exceeds that side, since \(R_1\ge L\) and \(\mathfrak M\ge1\). Thus the potential bound on the carrier loses at most the fixed factor \(L\). This explicitly includes outward rows; it is not the outline's different boundary convention.

In the \(\eta\)-units of CMP 109 (3.30), put
\[
 F=\frac1{i\eta}\log\bigl(e^{i\eta A}
                         e^{iL^{-1}\eta H_{k+1}(B_V)}\bigr).
\]
Here \(|A|<\alpha_2\) on the entire window. On a row of side \(s_q=L^q\eta\), the preceding carrier check and (4.2) give
\[
 s_q\sup_E|L^{-1}H_{k+1}(B_V)|\le LK\|B_V\|_\infty,
 \qquad s_q\sup_E|A|\le L\alpha_2 .                            \tag{7.2}
\]
The factors of \(L\) accommodate the source's incoming top side \(L\) in \(\eta\)-units; all indices obey \(q\le j\le k+1\). The same bound at \(q=0\) follows directly from the fine-row chart bound.

For matrices in a fixed sufficiently small ball, the logarithm power series gives
\(|\log(e^{iX}e^{iY})|\le2(|X|+|Y|)\). Explicitly, if \(t=|X|+|Y|\le\log(4/3)\), submultiplicativity gives \(|e^{iX}e^{iY}-1|\le e^t-1\), and the log series bounds the logarithm by \(-\log(2-e^t)\le2t\); the last inequality follows by integrating \(e^t/(2-e^t)\le2\). Apply this with \(X=\eta A\), \(Y=L^{-1}\eta H_{k+1}\), shrinking \(a_{98}\) once if needed. The smallness follows from (7.2) and its amplitude ceiling, since \(\eta\le s_q\). Therefore
\[
 s_q\sup_E|F|\le 2L(\alpha_2+K\|B_V\|_\infty).                \tag{7.3}
\]
Choose the radii so the right side is below \(a_{98}\). Applying the **auxiliary** \(Q\) bound in (4.3) to (3.30), with its unchanged rows, yields
\[
 \|B\|_\infty\le2LC_A(\alpha_2+K\|B_V\|_\infty).
\]
For the actual range \(|\tau|\le1\) and \(|B'|<2\alpha_3\), it follows that
\[
 \boxed{\ \|D\|_\infty
 \le2LC_A\bigl[\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')\bigr]
                   +2\alpha_3<\delta .\ }                     \tag{7.4}
\]
The near case \(A=0\) is included. This proves full complex chart admission from the input conditions, without invoking the conclusion of CMP 109 Lemma 4 or the near-case membership proposition. If a later Cauchy argument uses a fixed enlarged \(\tau\)-disc, multiply the first term of (7.4) by that fixed radius before choosing the amplitudes.

## 8. Order of choice

The additional ceilings are (4.5), (5.2), and (7.4), together with the two preliminary ceilings in §7 and the published chart/averaging ceilings. In the literal-frame port one keeps the ceilings actually used by (AX1) and (AX2-poly), in particular \(\alpha_1'''\le\min(\alpha_1^{(98)},1)\), \(2C_vM\alpha_1'''\le1/6\), and the small real-curvature threshold for Proposition 2. One also requires the bound on \(V-1\) in (7.1) to lie in the identity logarithm chart. Their order is:

1. Fix \(d,G,\beta\), then \(L\) with the account's floors, then the propagator and averaging constants, block sizes and gaps. Keep the account's order \(C_1,C_H,\bar\varepsilon_1\); choose \(\varepsilon_*,r,K,a_{98},C_A,C_D,C_7,\delta\) after these, all independently of the depths and domain.
2. Choose \(B^{(109)}\) and \(M\) with their existing one-sided floors. This proof imposes no upper bound on \(M\).
3. Choose \(\alpha_1\) small enough for its existing conditions and (7.4); choose \(\alpha_0\) small enough for its existing conditions, including the conditions relative to \(\alpha_1\); choose \(\alpha_3\) small enough for \(4B_3\alpha_3\le\beta L^{-2}\alpha_0\) and \(2B_3\alpha_3<\alpha_1/2\); then choose \(\alpha_2\) small enough for \(c\alpha_2\le\alpha_3\). Decrease them further, in the same order, to meet (7.4).

This is a specification of the phrase “sufficiently small and satisfying all the restrictions” in CMP 109 Lemma 4, not a ceiling depending on \(Z\), the number of blocks, or the depth. The existing order and the proof radius are recorded in CA-I 34745–34883. For fixed preceding constants, every new amplitude inequality has a positive right-hand side and is preserved by decreasing the amplitudes. No current estimate or physical conclusion of another open lemma has been discharged here.

## 9. Checks and limits

A separate Codex reader checked the boundary extension, inherited axial representative, weighted Schwarz estimate, rescaled averaging bounds, and the literal outgoing-row calculation. It found no load-bearing failure in those bridges, taking the cited complete-account proofs and Balaban propositions as inputs. Its explicit unit check was \(s_qL^{-1}/\ell_{q-1}=L\) for an outward row and loss one for a fine row. This is a second reading of the new arguments, not an independent re-proof of the published inputs or a check by another provider.

The sources used were read in bounded excerpts; damaged OCR equations were checked against the complete account's explicit formulas or were not quoted as exact formulas. Shell tools were used only for fetching, navigation, hashes, source excerpts and file editing. No computation is a proof step. No audit, ledger, claim status, source-account file, prompt or platform instruction was changed.

The numbered source excerpts, hash manifest and separate reader's finding are saved under `/tmp/mu-research-c04b80758/`. The durable source identities and the complete argument are in this file; the scratch packet is a navigation record, not additional mathematical evidence.

The result supplies the minimizer identity the complete account's consumers need. (PH3 is our hma's hypothesis, not a label of the account; this result bears on it.) Applying it to `hma.md` still requires that note's PH1, PH2, PH4 and the identification of its actual rows with the Balaban rows. It proves neither those hypotheses nor a transfer to the outline's different averaging map. The already proved scalar estimates in the consumers and all unrelated open steps retain their own dependencies.

## Result

**Proof**

In the regular variational space and axial convention of CMP 109 Lemma 4, every admitted real datum has exactly one axial minimizer, and every admitted complex datum has its single-valued holomorphic continuation. With the phrase “sufficiently small” specified by §§4, 5 and 7 in the account's order of choice, this holds uniformly in the depth and domain. For every subdomain \(Z\subset X\subset\tilde\square^2\) required by the one-power hereditary class, either tower rule, and \(1\le n\le p\le j\), the layered datum of the Landau copy \(\mathcal U_j\) belongs to the actual inner minimizer chart and
\[
 U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U_j)\bigr)
   =(W_j|_Z)^{\bar u_{\mathcal T}^{-1}}
   =(\mathcal U_j|_Z)^{\bar u_{\mathcal T}^{-1}u_j}.
\]
This is the arbitrary-subdomain nesting property of CA-I Lemma `4.13:lem-minimizer-unique`, with curvature and current identities (6.3). Sections 4 and 7 establish admission; §5 proves real criticality, uniqueness and the representative; §6 proves the equality throughout the complex domain. The product-order correction in §6 is a correction of notation under the account's left gauge action; no consumer's estimate changes. Locality means this nesting and dependence on the intrinsic layered datum, not finite-range response to changes of that datum. No scientific status is granted. \(\square\)

## Change log (freeze, 2026-11-05)

Written by Codex in one proof-lane round. Refereed line by line by a fresh Claude session ([mu-gate](../gates/mu-gate.md)): first failing step none, nothing fabricated, findings all repairable. Applied by the lead (Claude):

1. Uniqueness is proved in Balaban's regular space; existence comes from the Theorem 1 orbit in CMP 102b (8) and "at most one" from its (6), matching CMP 109 (1.1).
2. The product-order correction (§6) is real but not load-bearing (every consumer uses only \(\|\mathrm{Ad}_g\|\)); all printed occurrences are listed; the account already uses the correct order at 121440, 123129 and covers it at 130188.
3. PH3 is our hma's hypothesis, not a label of the account.

Scope (referee): their 4.13 is proved **as stated**, for regular real data with the analytic continuation for complex data: (a) and the nesting identity (b) for every \(Z\subset X\subset\tilde\square^2\), both tower rules, \(1\le n\le p\le j\); and **as used** by its 4.8 near-case and 4.7 consumers, for which "locality" means nesting. Uses outside the statement (4.26 stage composites, CA-II 35714) read (3.38) at other data radii and domains; the §§4–6 argument carries over but those radii are not checked here. One input is unconfirmed: the port of CMP 98 Prop. 4 (134), whose OCR is garbled; check it against the PDF before any outward use.

Status: **frozen.** CA-I 4.13:lem-minimizer-unique, marked "Proof outstanding" in the account, has a proof here. Candidate contribution to Sussman and Alpoge (nothing goes outward without the owner's approval of the exact text).


## Source check (lead, 2026-11-05)

Balaban CMP 98, Proposition 4, read by the lead (Claude) from the printed page (journal p. 38, PDF page 22 of the local copy; the OCR there is garbled): for \(\alpha_0,\alpha_1\le c_4\), \(Q_k(U_0,\eta A)=Q_k(U_0)A+C_k(U_0,A)\) (134) and \(|C_k(U_0,A)|\le C_2|A|^2<C_2\alpha_1^2\) (135), with (131) \(|(L^j\eta)^{-1}Q_j(U_0,\eta A)|<2\alpha_1\). With the bounded linear part this gives the \(Q\) half of (4.3), \(|Q_q(hF)(c)|\le C_A s\sup_E|F|\), after shrinking \(a_{98}\); at \(U_0=1\) the curvature condition on \(\alpha_0\) is automatic. The unconfirmed-input note in the change log above is closed. Remaining before outward use: the radius check for the uses outside the statement (4.26 stage composites, CA-II 35714).
