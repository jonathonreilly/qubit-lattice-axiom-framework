# ti-cov: symmetry of the old regular totals
Provenance: Codex (GPT-6), max effort; checkout `9e98c836e6ab930f0bb5e04318e5f7dacadf5a3c`; Sussman–Alpoge `31a47c543775`. Research text; not an audit; grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Their outline supplies R14, PH1–PH23, the step construction and the defect alternative. Balaban supplies the Ward-identity method. SA line numbers refer to the single fetched outline. This note uses written arguments only.

## 1. Check of `b2-extract.md`, Sections 3–7

**Theorem P: ADVANCE as an implication.** Checked line by line by Codex; first failing step none.

Steps 1–2 remove the first derivative and make the colour kernel scalar. Step 3 differentiates gauge invariance. In Step 4, the cutoff derivative has polynomial growth uniformly in its radius. Thus (Mo) permits its removal. Steps 5–6 kill constant fields and symmetric affine gradients. Reflections remove tensor entries with an odd index multiplicity. Permutations identify the remaining entries. Consequently

\[
 T_{\mu\nu,\kappa\lambda}
 =b_z(\delta_{\mu\nu}\delta_{\kappa\lambda}
       -\delta_{\mu\lambda}\delta_{\kappa\nu}),\qquad
 D^2F_z(0)[\ell_F,\ell_F]=b_z\sum_{\mu<\nu}|F_{\mu\nu}|^2.
\]

Here squares mean the bilinear colour pairing. Expanding the displacement moment gives
\(-T_{\mu\nu,\mu\nu}-T_{\mu\nu,\nu\mu}=b_z\), with the stated sign. Step 9 gives curl \(\eta F\) in the bare potential chart. The additional \(\eta^2\) and four one-dimensional tent sums give exactly unit normalization. Step 10 only reindexes absolutely convergent sums. Hence (20) is equivalent to \(b=b_z\); (Tr) makes this the bulk coefficient. All these statements retain the named inputs.

**Section 4: CORRECT-NO-ADVANCE, conditional on (Id) and its cited class inputs.** At fixed \(j\), Cauchy gives \(g_jr_j^{-2}\) times the domain weight. Exponential response decay controls the two bond sums. Choose the moment exponent small enough that the domain decay still exceeds the rooted counting rate. This proves (D), (Mo), with constants depending on \(j\). Block-constant gauge covariance gives (C), (G). Affine reproduction gives (AR), after converting bare coordinates. No estimate here supplies uniform radii or (R14). Theorem IC itself retains its building-block covariance inputs.

**Examples 1–3: ADVANCE for their stated obstructions.** Unequal plane coefficients leave \((c_{\mu\nu}-b)|F_{\mu\nu}|^2\). In Example 2 the total telescopes, whereas the pointed coefficient changes by \(\theta(z)-\theta(z-e_1)\). Choose \(\theta\) varying in direction 1. This example need not preserve (H_z); its isotropic affine jet follows directly from the two tent actions. In Example 3,
\(Q_{\mu\nu}=t\eta^2F_{\mu\nu}+O(t^2)\).
Thus the coefficient of \(t^2\) is \(2\theta\sum\epsilon_{\mu\nu\kappa\lambda}\langle F_{\mu\nu},F_{\kappa\lambda}\rangle\). Its repeated-index moment is zero. Taking \(F_{12}=F_{34}=T\ne0\) makes its jet nonzero. This proves the reflection obstruction. The later total-derivative remark is needed only for this quadratic jet, not as a nonlinear identity for the clover density.

**Lemma R(i)–(v): ADVANCE on its invariant core.** Substitute \(g=hg'\) in the average. This proves equivariance, also after summing domains. Each transformed summand reads only \(X\); the triangle inequality preserves its bound. There are \(M^4\) grid offsets. Summing all labels gives the Reynolds average \(\mathcal R\operatorname{Tot}_G\). Its equality with \(\operatorname{Tot}_G\) is equivalent to (TI), since the image of \(\mathcal R\) is invariant.

The companion conclusion also needs the original grid covariance and companion. Mapping non-wrapping domains alone does not prove it. With those inputs, write every translation as \(a+Mm\), \(a\in\{0,\ldots,M-1\}^4\). Grid covariance removes \(Mm\). The average is therefore the same finite average over offsets and signed permutations on every admissible torus. Common lifts agree term by term. For the actual grid-covariant families this supplies the missing justification. Averaging preserves a total only on the class where (TI) holds; physical-background covariance does not establish equality on arbitrary independent-current pairs.

**Proposition W: CORRECT-NO-ADVANCE as a conditional bound.** Checked line by line, retaining (P20), (ER8u), (BX), (UR), (YA), and its listed window bounds. Take the small-domain threshold below the fixed Cauchy constant; the intervening bounded range goes into the large-domain estimate. Cancellation replaces the small-domain affine Hessian by its large-domain tail. The two errors cost
\(Cg_j(\rho^2\sigma^{4+\alpha_H}+\rho^3\sigma^6)\).
The cubic remainder costs \(Cg_j\rho^3\sigma^6D_X^3\). Exponential domain summation pays this polynomial. Multiplication by \(C_M\sigma^{-4}\), then Cauchy in \(\nu\), gives
\(Cs_kg_j(1+k-j)^{3/2}L^{-\alpha_H(k-j)}\).
The box Hessian tail is absorbed by the same weight. This does not prove (BX), uniform response moments, or (YA). Section 4's fixed-depth estimate cannot replace them. At this checkout, `c1-repr.md` Section 8 supplies a proposed ER7 repair, not yet checked by the other model. The older statement that ER7 has no proof is therefore outdated.

## 2. The total step: the symmetry argument that works

Read first: SA's QED3, lines 1101–1123, and YM3_I, lines 33833–33855 and 38578–38609, at the same commit. They use relabelling, orthogonal fibre maps and uniqueness. Their polymer argument preserves the supplied partitions; it does not remove that restriction. The following argument removes partitions only from the **complete physical integral**.

Let \(g\) be a unit translation or a signed permutation of the level-\(j\) torus. It preserves all finer lattices. The centred blocks and the family of all contour orders map bijectively. Reversing a coarse bond reverses its average: reindexing the start block changes each logarithm to its negative conjugate. Thus \(\mathcal M(gV)=g\mathcal M(V)\). The Wilson action and the soft contour gauge factor are invariant. Uniqueness of the augmented critical branch gives \(U_l(gV)=gU_l(V)\) on their common domain, as in `prefactor-loc.md` Lemma D(c).

There is no tree-gauge assumption in the following change of variables. On a reversed bond,

\[
 (e^{iA_b}V_b)^{-1}
 =e^{-i\operatorname{Ad}(V_b^{-1})A_b}V_b^{-1}.
 \tag{1}
\]

For real \(V\), this is an orthogonal map of each colour fibre. It preserves each bond ball and product Lebesgue measure. The middle bond of a coarse path maps to the middle bond of the image path. Hence pivots and free bonds correspond. The unique small pivot solution corresponds too: both transformed solutions solve the same constraint with the same free coordinates. The coarea density therefore transforms with its coordinates. Alternatively use Haar invariance and inversion before resolving the constraint. The soft contour factors in SA 7181 are merely permuted. Their thresholds and normalizers are scalar. These facts prove, for the actual sharp small-field kernel of SA 7142,

\[
 (T^{\rm sf}_{j-1}F)(gW)
   =(T^{\rm sf}_{j-1}(F\circ g))(W).
 \tag{2}
\]

Suppose the earlier list action \(S\) is invariant at **every background read on this integration support**. Substitute
\(F(V)=\exp[-xA(U_{j-1}(V))+S(U_{j-1}(V))]\)
in (2). The two background subtractions in SA 6219–6225 are invariant as well. Therefore

\[
 \mathcal E^{(j)}[\theta;x;S](gW)
 =\mathcal E^{(j)}[\theta;x;S](W).                 \tag{3}
\]

At real data the integral is positive, so its logarithm has no branch ambiguity. Holomorphic continuation extends (3) through a common connected domain, using the same logarithm branch. It does not extend it to unrelated independent-current pairs.

This proves the induction step for totals. The empty list supplies its base. Vacuum subtraction and scalar multiples of \(A\) preserve the induction. An aged remainder may enter only if its total also satisfies (3). Every exact localisation preserves the complete total by definition. Thus (3), then Lemma R, closes the algebraic induction **provided** the earlier totals have this support-domain covariance and each admitted remainder is invariant. SA 20636–20646 explicitly retains these domain and naturality requirements. A small neighbourhood of the external zero datum alone does not establish them.

## 3. What the adopted rules preserve

Carry grids, regions, frames and parameters as data. Covariance with those data carried is different from invariance with them fixed.

1. **Definition A and the half-cell profile.** Distances and cube membership give
   \(T_q^{g\pi}(gZ)=gT_q^\pi(Z)\), by induction in its erosion recursion. Intersections, cut meets and collars commute with \(g\). Likewise
   \(\widehat\varphi[gA](gp)=\widehat\varphi[A](p)\), directly from its distance formula. With a fixed grid, Definition A supplies only its stabilizer. Unit translations generally change that grid. Lemma R's offset average addresses localisation; it cannot prove invariance of an integral that actually uses a different grid.

2. **Upper face bound.** The inequalities \(m_i\le\text{face increment}\le Km_i\) are invariant. They do not specify an equivariant choice of the faces. Section 4 gives an admitted asymmetric choice. This is the first missing geometric input in the requested induction through all operations.

3. **Rule W and box first.** Carrying the partitions preserves \(p(z)\), the drop-out classification, the containing cube, and its enlargements. It therefore carries each of W1–W3 to itself. For fixed partitions, a unit translation need not do so. Nevertheless `wf7-bf.md` (2) sums exactly to the endpoint difference. Hence this choice does not change a complete physical total, provided **all** complementary, long-domain and removed pieces are retained. Covariance of one near-window piece does not follow. The same caveat applies to its off-shell extension.

4. **Definition D and [RED].** The image of a walk hull is the hull of the image walk. Thus \(\mathsf P(g\omega)=g\mathsf P(\omega)\) when the parameter grid is carried. Set \((gs)_{g\Delta}=s_\Delta\); then the parameter monomials agree. The midpoint convention in `h-walk-fix.md` makes scalar cutoffs commute with (1). The undecomposed equations transform as follows. Differentiate the equivariant average and invariant action in the charts (1); this transports \(Q\), its higher derivatives, \(J\), and the Wilson Hessian. Differentiating the gauge action transports \(D\). Transposes, scalar scale weights, products and inverses preserve these identities. Orthogonal projection onto a transported range does too, by uniqueness of the orthogonal decomposition. This covers the enlarged saddle equations and their local inverses, wherever they exist. Pivot elimination and strict axial restriction require the pivots **and trees** to be carried. An independent current is transported in the same fibre as \(J\), so the current-linear corrections obey the same identities.

   In [RED], \(-a_0I\) is invariant, including at walls. Uniqueness in \(d=\mathcal C(a-Hd)\) transports \(d\); differentiation transports \(d'\). Bilinear orthogonality transports each transpose. Each of the five terms of (4.4) therefore transforms correctly. This verifies naturality of the assigned algebra, not existence of its inverses. It gives no extra symmetry for a fixed strict axial tree. At \(s=1\), the uncut walk sum is the original operator, so its auxiliary grid disappears.

5. **Stored carrier series.** Length cutoffs, the fixed polynomial coefficients, chain multiplication and transposition commute with every symmetry of their input data. Retention does too when the stored components are carried. The arbitrary order selecting \(X(\mu)\) in Lemma P need not commute with reflections. It only files terms: summing over \(X\) gives exactly \(-\frac12\sum_{\mu\text{ rejected}}\langle A',\mu A'\rangle\). To make the filing covariant, divide each term equally among all minimal containing polymers. Their sizes and distances obey the same bounds in Lemma P; weights sum to one. Thus its bound (P) is unchanged. This does not enlarge the covariance group of the underlying strict axial precision.

6. **Definition R.** If \(z_c\), the nest and frame are carried, every comb is carried, so its ordered transport and \(S^R\) are carried. The source averages **all** post-stage objects over frames, including tests, normalizers and drop-outs (SA 17585). Reindexing \(r\mapsto gr\) then proves point-group covariance. But the adopted instruction “a site nearest its centre” supplies no tie rule. Choose the first nearest site in the frame's coordinate order; the image frame gives the image site. This is a covariant version. It is extra supplied data, not a consequence of nearestness. Also, the source's frame average occurs after the stages. It cannot correct an asymmetric nest selected before those stages.

Integration, multiplication, exact telescoping, differentiation, connected-cluster summation and the logarithm preserve covariance once their inputs do. For integration this is (2). For products and derivatives, apply the same change of variables to every factor. For clusters, it bijects vertices, edges and connected index sets; absolute convergence permits reindexing. None of these operations repairs a noncovariant input merely because the sum over histories preserves mass.

## 4. The first geometric failure, and a covariant version

**WRONG:** the adopted upper face bound implies covariance of the selected nests.

Use the quiet symmetric component of `geo-prop23.md` Section 3. At its first preparation stage \(i=a+1<k\), put \(m=m_i\). Its core has carrier \([-h,h]^4\), with \(h=13\check R m_a/2\). Choose \(\check R\) divisible by \(L^2\), as that example permits. Then both faces lie in \(F_{i+1}=Lm(\mathbb Z+1/2)\). The permitted lower-face-first recursion gives

\[
 D_i=[-h-m,\ h+Lm]^4.                          \tag{4}
\]

Indeed, the next point of \(F_{i+1}\) above \(h+m\) is \(h+Lm\). Each face moves between \(m\) and \((L+1)m\). The minimum carrier gap is \(m\). The quiet hole's padding contains this box, as in `geo-3.md` (2.3). Thus every adopted upper/lower constraint holds. Reflection in coordinate 1 fixes the input core and every centred grid. It changes the first interval in (4) to \([-h-Lm,h+m]\). Applying the rule to the reflected input still gives (4). The rule is not covariant. This is a hand counterexample to the **formation-rule implication**, not a computed counterexample to an actual regular total.

`geo-5.md` Section 3.1 explicitly retains supplied nests without choosing this or another recursion. Therefore the actual selector's covariance is missing, rather than disproved for an identified selector. The example proves that the missing property cannot follow from its bounds. The later frame average does not move (4). Consequently it cannot supply the missing permutation of stage outcomes.

**A covariant selector exists.** At each stage take the smallest box with faces in \(F_i\) containing

\[
 D_{i-1}+[-m_i,m_i]^4.                         \tag{5}
\]

Round every lower face downward and every upper face upward. Rounding costs less than \(m_i\); every increment lies in \([m_i,2m_i)\). This meets \(K=L+1\). It gives the required lower gap, though equality need not hold. The rule commutes with signed permutations and translations preserving the face grids: the image satisfies precisely the same containing-box criterion. If \(D_{i-1}\subset B_{i-1}\subset H_i\), (5) lies in \(H_i+[-2m_i,2m_i]^4\subset H_i^{[8]}\), since \(s_i\ge m_i\). Thus the old containment induction still works. The rule uses the same local lifts on every torus with room.

At the allowed insertion age, \(M\check R_j\le L^{m+1-j}\) (SA 20651–20654). Both sides are powers of \(L\). Hence a level-\((m+1)\) unit translation is a multiple of the remainder's cell side and of every finer nested face-grid spacing. Centred grids are also preserved by signed permutations about those coarse sites. Thus grid covariance suffices for these aged data. It does not suffice before that age, exactly when the source keeps them outside the regular exponent.

Together with the frame-dependent nearest-site tie rule of Section 3 and averaged polymer filing, (5) supplies covariant versions of these choices. No change to another file is made here. These versions need to define the actual formation data before their covariance can be used. Bounds alone do not identify them with the existing operation.

## 5. What a symmetry defect would cost

There is an exact filing with an explicit bound. On an invariant common core, let \(\mathcal R\) denote the finite symmetry average of Lemma R. For any already bounded family \(H\), set

\[
 H^{\rm sym}=\mathcal RH,\qquad D_H=H-\mathcal RH.
 \quad
 \|H^{\rm sym}\|_{j,\kappa}\le\|H\|_{j,\kappa},\qquad
 \|D_H\|_{j,\kappa}\le2\|H\|_{j,\kappa}.          \tag{6}
\]

Each summand is local on its transformed domain. The triangle inequality proves both bounds. The identity \(H=H^{\rm sym}+D_H\) preserves the original exponent exactly. No claim that averaging alone preserves it is used.

For a remainder with its required bound \(\|R^{(j)}\|\le\bar g_j^{\kappa_0}\), (6) gives
\(d_j\le2\bar g_j^{\kappa_0}\).
This is a scale-small noncovariant defect of the kind allowed at SA 4007–4010. If all offsets of its \(M\check R_j\)-grid are needed, the rooted count gains at most \((M\check R_j)^4\). With \(\check R_j\le L(\log\bar g_j^{-2})^r\), the resulting absolute-sum bound is

\[
 2(ML)^4(\log\bar g_j^{-2})^{4r}\bar g_j^{\kappa_0}
 \le C\bar g_j^{\kappa'},\qquad
 \kappa'=(\kappa_0+4)/2>4.                     \tag{7}
\]

For a hand proof, put \(t=\log(1/\bar g_j)\ge1\), \(q=\lceil4r\rceil\), and \(\epsilon=\kappa_0-\kappa'>0\). The exponential series gives \(t^q e^{-\epsilon t}\le q!\epsilon^{-q}\). This proves (7) with an explicit constant. If the symmetry already preserves the remainder grid, there is no offset cost.

This bound is conditional on the remainder bound; it does not prove that bound or the large-field construction. Nor does it prove (TI) for the original marked regular outputs. Propagating \(D_H\) through later steps still needs the ordinary defect estimate, with squared-radius load \(\sum_j\rho_j^2d_j\). For an arbitrary old regular member, (6) only gives \(2g_j\). Its norm can be of order one. That estimate supplies no scale-small defect and no summable age gain. SA's permission to carry defects is not a bound on this missing quantity.

## Result

Theorem P and the finite-torus averaging lemma pass under their named inputs. Their fixed-depth inputs and Proposition W remain conditional as specified in Section 1. The companion argument needs grid covariance; the finite-offset proof supplies it.

**(TI) for every actual old regular member is not proved.** Equation (3) proves the total-step implication by hand. Its induction needs covariance on the full fluctuation support and invariant totals for admitted aged remainders. These are not consequences of covariance near the external zero datum or of mass preservation.

The first failed geometric input is **equivariance of the selected pre-frame nests**. The adopted face bounds permit the explicit reflection failure (4), and no selector is specified. Definition R also needs its nearest-site tie rule. Formula (5) and frame-dependent ties give covariant versions. Formula (6) files the defect of an already small remainder with its own bound (7). No such small bound has been shown here for the original regular total. Thus (R14), (20) for every old member, and B4's (19) remain open for the unchanged adopted chain. The new arguments in Sections 2–5 are by Codex, not yet checked by the other model.

