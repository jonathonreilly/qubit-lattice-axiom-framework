# geo-4: remaining geometry and the EXT-out consumers
Provenance: Codex (GPT-6; effort: xhigh), checkout `c3acdca073afdb66a362c4b818d95a91d3dce4ce`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit, grants no status.

## 1. Scope and fixed definitions

This is queue row 122: the remaining geometric inputs of the A3/Proposition 2.8 route, and the consumers of EXT after its replacement by EXT-out. A counterexample changes the hypotheses available to those consumers; it does not refute an analytic implication that retains them or make a claim about Yang–Mills existence.

Adopt `geo-prop23.md` (5.1), Definition A of `assign-adopt.md` with the repairs in `../gates/a2-full-gate.md`, and the upper face-movement rule of `geo-2.md` §6. Cite, without redoing, the profile locality proof in row 118, the size/count estimates in row 119, and formation compatibility, EXT-out and the restriction lemma in `geo-3.md` §§2, 4–5 (row 121). All three predecessor reports were read in full, in bounded excerpts.

Credit: the source regions, class, nests, preparation, healing and determining rows are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. SA line numbers refer to their `YM4_sketch_500.tex` at the pinned revision, fetched once to `/tmp/sa_ym4.tex`. The earlier literature search is `lit-large-field.md` §§0–1; the targeted source for this geometric lane is the pinned outline. No run discharges a mathematical step.

Write `a=k-N_k`, `R=Rcheck_k`, `xi_i=L^(i-k)`, `m_i=M xi_i`, `s_i=Rcheck_i m_i`, `C=X intersect Z_a`, `D_i=Z''_i(X)`, and `Lambda=D_k` enlarged by one level-k M-layer. All distances between boxes below use their cubical carriers and the periodic sup metric unless explicitly stated otherwise.

## 2. A literal clause of GEO1 fails under the adopted localisation

**REFUTED clause:** “In `X minus Lambda` every sequence is at level `k`” (`sa-2.8-terms.md` §3, GEO1). The localised prepared and healed sequences are among the sequences used there. This assertion is false for them. This is a quantifier defect, not a failure of the two-cell clearance or of the intended exterior comparison. The smaller, correct statement is proved in §3; the consumer check below does not use the false clause.

The adversarial checks distinguished the following cases. A merger during `(a,k]` is excluded by the class definition; a merger at or before a changes the old core, as treated in `geo-3.md` §2. Older nested marks have disjoint active windows by quarantine. These do not remove the outer localisation collar. Taking several separated components does not change the cell-size condition on each X. Taking the thinnest allowed nest still keeps `C subset D_(q-1)` behind its required next-box gap; taking a deeper nest does not reduce the tower's bare boundary layer. Finally, translating a component across the chosen torus seam preserves the site distances used below, while the W4 complement is allowed to wrap. The surviving elementary counterexample is therefore at the localisation boundary, not at a forbidden merge or a wrapping lift.

Use the entire single-creation configuration of `geo-prop23.md` §3 and `geo-3.md` (3.1), with its ordinary nest, whose admission was already checked in those texts. In particular choose odd `L>=27`, powers `mu=M_1'>=max(3,rho)` and `M>=L^3 mu`, collar counts 5 and 9, and the ordinary upper face bound `K=L+1`. Choose `R=L^h`, `h>=2`, above the coupling floors in row 118, `a=1`, `k=R+1`, `eta=L^(-k)`, and the constant-R frame of that row. The torus has side greater than `100MR`, with all the required grids. With `s=MR`, the final component is

\[
 X=[-21s/2,21s/2)^4.
 \tag{2.1}
\]

There is no joining or operation in its waiting window. Its nest obeys the adopted upper bound and the outline's lower gaps; the final box has side less than `(L+7)M`. The profile is exactly the adopted half-cell profile. Nothing from the counterexamples' discarded profile or exceptional face jump is used.

Let `b=21s/2` and choose the last bare site before the positive first face:

\[
 u=\eta(\lceil b/\eta\rceil-1),\qquad
 z=(u,0,0,0),\qquad z'=z+\eta e_2.
 \tag{2.2}
\]

Then `u<b<=u+eta`; `z,z'` belong to X and the bare sites `z+eta e_1,z'+eta e_1` do not. Their site-set distance to `X^c` is exactly eta. Both points lie outside Lambda: the latter is at carrier distance at least `2s-M` from `X^c`, while the points have carrier depth at most eta and `2s-M>eta`.

For the second-rule tower of X, every cube admitted to `T_1(X)` has distance at least `mu xi_1=mu L eta` from `T_0(X)^c=X^c`. An admitted cube containing z would have distance at most eta, because it contains z. Since `mu L>1`, this is impossible. The same argument applies to z'. Thus

\[
 z,z'\in T_0(X)\setminus T_1(X).
 \tag{2.3}
\]

Healing gives `O_q^h intersect X=X` for every `0<=q<=k`. Therefore `L_X O^h` equals `T_q(X)` in X, and (2.3) places z and z' in its **level-zero** layer. The bond `[z,z']` is an actual level-zero determining row: its endpoints are in the first domain and neither is in its first positive member (SA 5614–5628). It is not merely a point falling between coarse grid tops. Both endpoints are in `X minus Lambda`, but `k=R+1>0`. This contradicts the quoted clause of GEO1.

One can put two such components at centres 0 and `50s e_1` on a torus of side greater than `400s`, as in `geo-2.md` §3; the same row remains a witness. The contradiction holds for arbitrarily deep R and the ordinary thin nest. No long history or merger is necessary. The failure comes from the deliberately supplied boundary erosion, which every localised problem has even when its parent is level k there. The full package requested in part (1), literally as stated, is therefore REFUTED.

## 3. The smaller GEO1 statement, with its constants, is proved

The correct replacement keeps the global level-k assertion and qualifies each meet by its own erosion strip. Put

\[
 C_X=3\mu+3,\qquad C_A=\rho+3,
 \qquad n_{\rm col}=5,\quad n_{\rm sep}=9.
 \tag{3.1}
\]

Choose fixed powers in the order `L`, `rho`, `mu>=max(rho,3)`, `M>=max(L^3 mu,80mu,8)`, then the coupling floor so that

\[
 R\ge\max\{8,\,4+4C_X/M\}.
 \tag{3.2}
\]

The other previously named analytic floors can be included before the coupling choice. These constants do not depend on the history, depth or torus.

**Corrected GEO1.** For every eligible X:

* `dist(Lambda,X^c)>=2MR-M` for carriers.
* The **global** prepared and healed determining sequences have level k throughout `X minus Lambda`.
* Their localisations in X agree with those global sequences, including rows and data, at distance greater than `C_X` from `X^c`. A further first-rule meet at a part A of collar level j agrees with its parent, including row carriers, at distance greater than `C_A xi_j` from `A^c`. No level-k assertion is made inside these strips.
* For the cutoff of `sa-2.8-terms.md`, its support has depth at least `3MR/4`, and `dist(Lambda,supp(1-chi))>=MR`. Every sequence's weighted metric dominates the periodic unweighted path distance, hence the periodic sup distance.

**Proof.** Quietness gives `A_k=H_k^[8]` and `X=H_k^[10]` (SA 17575–17583). Each face of X is two level-k cells beyond the corresponding face of `A_k`. The retained box `D_k` lies in `A_k`. Adding an M-layer costs at most M in each coordinate. Thus the first clearance is at least `2s-M`, `s=MR`. A class box has a non-wrapping neighbourhood by the stated torus floor; the same argument applies to a lift across a chosen fundamental-domain seam. Distances are still periodic distances, not distances between arbitrary distant lifts.

By EXT-out (`geo-3.md` §4), the global prepared and healed members agree off `D_k`. Healing puts every point of X in every member through k. Hence every point of `X minus Lambda` belongs to the global kth members. As depth is k, this proves exactly the second assertion. It neither asserts nor requires that such a point survives localisation.

The proved erosion bounds of repaired Definition A are `e_q<=3mu xi_q` for the second rule and `e_q<=rho xi_q` for the first. Every point deeper than the respective erosion radius survives all tower factors through the relevant cut. For a row together with its double-block carrier, allow three further local units. This gives (3.1) and the stated row/data equality, exactly the repaired (SEP-L) of `a2-full-gate.md`, assign-adopt §4. The argument is pointwise: neither connectedness nor a non-wrapping lift of the complement is required. For cut meets above their collar level, use the supplied cut-meet definition and its proved single-layer-collar property, not an uncut tower in an arbitrary part. The W3 full-tower identification still reads its separate nest clearance.

Depth at least `3s/4` on `supp chi` is the definition of chi. If `chi(p)=0` and p is inside X, its midpoint has depth less than `3s/4`. The distance-to-`X^c` function is 1-Lipschitz, so for every `z in Lambda`,

\[
 d_\infty(z,p)\ge (2s-M)-3s/4=5s/4-M\ge s.
 \tag{3.3}
\]

If p is outside X the first clearance is stronger. The last inequality uses `R>=4`. For site/carrier translations or an assigned pillar top, reserve two level-k units: the bound remains at least s under (3.2), because `s/4-M>=M>=2`. A pillar corner moves by at most one local unit, and the midpoint-to-corner displacement is at most eta; local units are at most one. This explicitly accounts for the endpoint loss noted in `a3-close-meet-gate.md` §G.

Finally every weight in the definition of `d_B` at SA 9600–9605 is `xi_j^(-1)>=1` or `eta^(-1)>=1`. Every path's weighted length is at least its unweighted length. Taking the infimum proves the metric assertion, including paths crossing other holes or winding around the torus. This proves all clauses of the smaller replacement. In particular, the witness (2.2) is confined to the excluded localisation strip. QED.

## 4. The common exterior problem exists although the full domains differ

This section checks the change from EXT to EXT-out. It retains the consumers' other stated geometric and analytic hypotheses; it does not prove their A1, P82, regular-data or response inputs anew. In particular, no occurrence of an unproved analytic theorem below is being promoted by this geometric check.

Let `F_p=O_0^p`, `F_h=O_0^h`, and `A=T minus Lambda`. EXT-out's global member equality, before taking the localisation in X, gives

\[
 O_q^p\cap A=O_q^h\cap A\quad(0\le q\le k),
 \qquad F:=F_p\cap A=F_h\cap A.
 \tag{4.1}
\]

Outside X the history is identical in the pair; inside X this is precisely (4.1) of `geo-3.md`. All domain differences are contained in `D_k`. Thus a first-domain hole in another component stays a hole of F. There is no filling of those holes in (4.1).

For the first-rule tower of A used by W4, put

\[
 B_q=O_q^p\cap T_q(A)=O_q^h\cap T_q(A).
 \tag{4.2}
\]

The equality follows point by point from `T_q(A) subset A` and (4.1); in particular `B_0=F`. Its original rows have both endpoints in A, hence the same functional and datum by EXT-out. All newly introduced rows lie within `rho+3` of Lambda. Their entire lift footprint lies in the level-k collar of A: its width `5mu+2` exceeds `rho+3`, and the fixed inequalities in (3.2) keep this collar inside `X minus Lambda`. The parent sequences are both level k there by corrected GEO1. Consequently each new row is the same lift of the same `V_k` in the two constructions. Their joined data agree.

Both weighted metrics have exactly the same layer weight on A, including near other components and their old holes. Any path from a point of F to Lambda can be truncated at its first entrance into Lambda without increasing its nonnegative length. Before that entrance its weights agree in the two problems. Taking infima in both directions proves

\[
 d_{O^p}(y,\Lambda)=d_{O^h}(y,\Lambda),\qquad y\in F.
 \tag{4.3}
\]

This assertion concerns distance **to Lambda**, not arbitrary pairwise distances whose minimisers could cross Lambda and leave it again. On a lattice path, stop at the boundary crossing with the same exterior edge convention; on geometric paths the endpoint has zero length. This is the convention in the source's weighted path metric.

For `Y=X minus J_X`, the localised prepared domain, every `q_ext` row has both endpoints outside Lambda. Its double block lies within two level-k units of an endpoint (SA 9631), whereas `D_k` is separated from `Lambda^c` by an M-layer. Since `M>=8`, that carrier misses not just `J_X subset D_k` but its one-bare-plaquette neighbourhood. It is a genuine common constraint on Y and X. This is the only part of the exterior row identity needed for the multiplier calculation.

## 5. Written repair of Lemma LM

**Classification: needs the following repair.** Replace its title by “multiplier form; `T(0)=S|_Y`”, write its first identity on X, and write its last identity on Y. The unrepaired equality of fields on a common full domain fails on `geo-3.md` (3.5); EXT-out does not restore it.

Retain I2 and I4 and the separated first gap supplied by the consumer's GEO4/SEP. In particular take `M>rho>=2`; the prepared first gap exceeds `rho eta`. Set `S_Y=S|_Y`. The repaired conclusions are

\[
 DA_X(S)=Dq_{\rm ext}(S)^{\mathsf T}\lambda_{\rm ext}.
 \tag{5.1}
\]
\[
 T(0)=S_Y\quad\hbox{modulo the prepared residual gauge}.
 \tag{5.2}
\]
\[
 q_{\rm ext}(\widetilde T(u))=q_{\rm ext}(S_Y),\qquad
 DA_Y(S_Y)[\eta\mathsf H v]=0
 \quad\hbox{for every shell datum }v.
 \tag{5.3}
\]

Here the action in (5.3) contains exactly the plaquettes contained in Y. One may equivalently use `A_X` after extending the variation by zero on bonds not wholly in Y; that is an identity proved below, not an identification of domains.

**Multiplier step.** All of this step takes place on X. Split the healed constraint into `(q_ext,q_Lambda)`, assigning any row with an endpoint in Lambda to `q_Lambda`. I2 supplies a datum chart `Phi_h` with `q Phi_h=id` and the multiplier identity for `A_X`. For every allowed tangent delta of the independent box datum, I4 gives

\[
 0=D(A_X\circ\Phi_h)[0,\delta]
   =\lambda\cdot Dq\,D\Phi_h[0,\delta]
   =\lambda_\Lambda\cdot\delta.
 \tag{5.4}
\]

Thus the box part of the multiplier covector vanishes, exactly as in the original LM proof, with the same chart/gauge convention. This proves (5.1). It uses no equality of prepared and healed domains.

**Criticality and admission of the restriction.** Apply the proved restriction lemma of `geo-3.md` §5 to (5.1), the first gap and the common exterior carriers in §4. It proves that `S_Y` is critical for the prepared problem with its own averages. For completeness, its analytic admission does not require a new uniformity assumption merely because a hole has been cut out. The following verifies the effect of that cut under the regular-background hypotheses already read by LM.

Write `c_S=C(M)` for I4's curvature constant on Lambda and its fixed neighbourhood, and let `epsilon_h` be the regularity radius of S in its healed localised problem, supplied by I2. On the unchanged region the layer, action stencils and constraints are unchanged. In the interior region where the prepared scale is finer, `xi_prepared<=xi_healed=1`, so I4's bound `c_S epsilon_k eta^2` implies the prepared curvature bound with radius `c_S epsilon_k`. The common exterior row carriers miss a neighbourhood of `D_k` of width at least `M-3` (two units for the carrier and one for the site convention); hence (5.1) makes the full-X current zero there. The only changed current stencils are the bonds adjacent to a deleted plaquette. By the first gap these bonds, when wholly in Y, are in its bare layer.

In four dimensions an unoriented bond is incident to at most six plaquettes. The SU(2) Wilson term `1-tr(U_p)/2` has derivative on a bond variation `exp(i eta tB)` of absolute value at most `eta ||B|| ||1-U_p||`: move the varying factor to the start of the trace, use `tr B=0` and `|tr AB|<=2||A||||B||`. In the current normalisation SA 5562–5571 this bounds each plaquette contribution by `eta^(-3)||1-U_p||`. Thus at a new bare boundary,

\[
 |J_Y(S_Y)(b)|\le6c_S\varepsilon_k\eta^{-1}
                  \le6c_S\varepsilon_k\eta^{-3}.
 \tag{5.5}
\]

Conjugations preserve the norm. With the usual SU(2) pairing `tr(AB)/2`, the norm of a traceless Hermitian matrix equals its operator norm, so no dimension-dependent conversion is hidden here. Changing the fixed Lie-algebra pairing merely changes this fixed factor. Therefore the radius

\[
 \varepsilon_{\rm res}=2\max\{\varepsilon_h,6c_S\varepsilon_k\}
 \tag{5.6}
\]

admits the restriction, with strict room. Choose the coupling ceiling so this radius is inside the existing uniqueness neighbourhood of I2. Its own-average datum is admitted by the same converse/admission clause of the regular-orbit input that original LM uses. This is a fixed enlargement, with no dependence on depth, the number of deleted plaquettes or the history. Uniqueness now gives (5.2). This also explains why simply quoting a curvature estimate while ignoring the new action-boundary current would have been incomplete.

**Shell derivatives.** Choose the representative of the prepared chart centred at `S_Y`. Shell data occur only at levels `a,...,k`, where `a>=1`; all level-zero rows adjacent to the deleted domain remain fixed throughout the chart. Extend `widetilde T(u)` to X by S on every bond not wholly in Y and denote the extension by `E widetilde T(u)`. The plaquette identity in the restriction lemma applies to this entire chart: every deleted plaquette has any surviving edges among those fixed bare rows. Hence

\[
 A_X(E\widetilde T(u))=A_Y(\widetilde T(u))+K_J,
 \qquad K_J=\sum_{p\subset X,\ p\not\subset Y}a_p(S),
 \tag{5.7}
\]

where `K_J` is independent of u. Every exterior row is fixed on the chart and has carrier in Y. Differentiate (5.7) at zero and pair the extended derivative with (5.1): it is zero, proving (5.3). No estimate of `K_J` is used and no boundary term is dropped.

The downstream uses of LM survive with these domains. Since `J_X subset C` and `psi=1` on plaquettes wholly in the core-margin region, while any plaquette meeting `J_X` lies in that region by the first nest gap, `phi` vanishes on every deleted plaquette. Thus `A_X(phi,S)=A_Y(phi,S_Y)=F(0)`. The decomposition of the derivative into the `phi`, `psi` and `1-chi` pieces is made on Y; by (5.7) it has the same derivative if written on X with the extended response. The Gaussian quadratic form on `supp phi` is also unchanged. These are equalities of the actual terms, not an assertion that `A_X` and `A_Y` are the same action.

## 6. The six requested EXT consumers

“Goes through” below means that replacing EXT by EXT-out requires no change to that consumer's mathematical conclusion or to its other input boundary. The repairs already required by `a3-close-meet-gate.md` and `a2-full-gate.md` remain in force, including the cut-meet convention, the one-sided mismatch-weight estimate and the endpoint allowance. Corrected GEO1 of §3 replaces its false universal layer clause. Analytic results conditional on GEO4, I5, A1 and response estimates remain conditional on them.

| Consumer | Decision under EXT-out |
|---|---|
| `sa-2.8-terms.md`, term R_1 and §5.5 | Goes through; no full-domain equality is used. |
| Its I1-W4 comparison | Goes through on the common exterior domain F in (4.1). |
| Its Lemma LM | Needs the written repair (5.1)–(5.7). |
| `meet-6c.md`, Lemma C, W4 | Goes through as stated; (4.1)–(4.3) replace the EXT citation. |
| Its Lemma D, W4 | Goes through as stated; the joined rows and their lift tests are identical. |
| Its Theorem M, W4 | Goes through as stated at its original analytic input boundary. |

**R_1.** A plaquette present in one global action domain but absent in the other has a corner in their symmetric difference, contained in `D_k`. All its corners are within eta of `D_k`, so its midpoint has depth at least `2MR-eta` in X. This exceeds `3MR/4`; hence `1-chi=0` there. Consequently R_1 is exactly the difference of actions on a common set of plaquettes outside the domain defect. It is not necessary to assign a fictitious P-field on a healed-only plaquette.

At every top carrying a plaquette with `1-chi !=0`, (3.3) and its explicit two-unit allowance give `d_B(y,Lambda)>=MR`. Such tops lie outside the W4 mismatch strip of width `rho+3`, by (3.2), so their local scales are those of the global parents. Apply the common-meet comparison of §4 and the same pointwise action bound of `sa-2.8-terms.md` (4.1). The weight estimate is its unchanged Lemma W item 4, and the global counting estimate is its unchanged Lemma BC with `s=1`, `R_0=MR`. The resulting bound is exactly

\[
 |R_1|\le C_{\rm SC}\Pi(1+B_*d_0)(1+R)
 C_{\rm BC}(1)(2C_\Lambda M+4)^4e^{-\theta MR/2}.
 \tag{6.1}
\]

All constants here are those already named in that consumer; the replacement of EXT introduces no new one. The shell used to anchor Lemma BC is the common global level-k outer shell of Lambda. It is not the artificial boundary collar of the W4 meet. Other holes of the label remain in F and contribute to the same global counting bound; there is no change of decay set to `F^c`.

**I1-W4 and Lemma C.** The comparison is between restrictions `P|_F` and `H|_F`, each obtained from its own original variational problem. The members agree on A by (4.1); the original exterior rows and their functionals agree by EXT-out; the joined datum agrees by (4.2). This proves Lemma C(d) and the common-meet assertion C(e) for W4. Equation (4.3) proves its metric assertion with exactly the distance to Lambda required by I1. No step equates `F_p` and `F_h`. For the other explicit invocation of EXT in Lemma C(c), the averages of `S_Y` on rows outside Lambda equal S's averages there, since those carriers lie in Y. Hence the exterior/collar-data part of the W3 proof also survives; its separate core/shell and nest hypotheses are unchanged.

**Lemma D.** The W4 collar is wholly in `X minus Lambda`, where both original sequences have level k. A new fine row is assigned 1 within a level-k block and the common `V_k(c)` across a face between two such blocks. A fine plaquette's four factors therefore give 1 within one block, `V_k(c)V_k(c)^(-1)=1` across one face, or the common coarse plaquette product (up to conjugation and orientation) where four blocks meet. These are precisely the three cases of Lemma D. Its mixed tests use the exact one-step averaging identity for a lift, so they reduce to the same cases with no accumulation in the number of levels. All the necessary blocks are in the thickened collar; the deleted set `J_X` is inside `D_k`, an M-layer away. Old tests away from this collar, including all tests near other holes, are literally unchanged. Thus the same regularity premise and the same interpolation admission estimate apply, with the original constants. No extension of the datum across `J_X` is being used.

**Theorem M for W4.** Its six premises can now be checked for the replacement in order. The common sequence and datum are (4.2). Its separatedness, alignment and first gap are exactly the meet conclusions previously used in Proposition 5.1, whose hypotheses on the parents are retained. The analytic P81/Reg/P82 conclusions therefore have the same inputs. The restriction step is applied separately from `F_p` to F and from `F_h` to F, as the theorem already states; the first domains need not be equal. Its collar datum and interpolation use the identical lift just checked in Lemma D. Finally its mismatch support is still only the collar of Lambda; the one-sided estimate

\[
 d_B(y,\mathcal C_A)\ge d_B(y,\Lambda)-(2\rho+8)
 \tag{6.2}
\]

is unchanged, since its connecting paths run through that common level-k collar. Thus its conclusion remains

\[
 U|_F=(e^{i\eta f}U_4^\circ)^w,\qquad
 \xi'_y|f|,\ \xi_y'^2|\nabla f|,\ \xi_y'^3|D^{\mathsf T}Df|
 \le E e^{-\theta d_B(y,\Lambda)},
 \tag{6.3}
\]

for each `U=P,H`, with one and the same `U_4^circ` and the original
`E=C exp(theta(2rho+8+D_L)) C_L epsilon_1`. Equality of the distances follows from (4.3), not from equality of the metrics inside Lambda. The analytic constants C, `C_L`, `D_L`, theta are precisely the constants of Theorem M's stated response inputs. EXT-out changes none of them. This completes every requested EXT-consumer check as an implication at the existing input boundary.

## 7. Disposition

**REFUTED, in the literal sense specified in §2.** GEO1's assertion that every sequence is level k on all of `X minus Lambda` fails on the explicit level-zero row (2.2)–(2.3), even with all three adopted rules. Its geometric clearance inequalities survive. The smaller replacement, which distinguishes global sequences from the collar layers of their localisations and meets, is PROVED in §3. This wording repair is necessary but supplies no new obstruction to the analytic route.

The independent EXT-out consumer question is closed at its stated conditional boundary: R_1, I1-W4, Lemmas C and D and Theorem M for W4 retain their conclusions; LM must use the two-domain formulation proved in §5. The work changes the geometric statement the consumers may quote and supplies the missing LM domain-transfer and derivative formulas. It does not claim a failure of the intended W4 decay estimate.

Scope of the remaining geometry: the explicit contradiction decides the requested conjunction; this report does not claim a universal proof or a counterexample for the independent GEO2, GEO4, GEO6 or W3 nest assertion. The tests of those clauses did not produce an additional failure. Their original hypotheses, together with the analytic inputs of the consumers, remain where those consumers use them. No audit, numerical discharge or scientific status is supplied.
