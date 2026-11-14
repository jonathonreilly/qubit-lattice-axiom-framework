# PRE-STATED

UTC: 2026-10-28 22:55:28 UTC, recorded before reading the scientific sources for this review.

Target: independently check the settlements claimed in REVIEW55_TUNIF.md for mean preservation, the r_i import, the H_j estimate, substitution into NORMS.md §N6 / Theorem N1-15, and cell-1-form to chain-reparametrisation admissibility; decide (T-UNIF) with the stated repairs; check the reviewer's new objection to NLOC Theorem NL-3′ using the authorized sources.

Prior exposure: the task supplied the earlier review's overall NOT-VERIFIED verdict, the Opus reviewer's claimed CONFIRMED verdict, its summary of four repairs, and its proposed NL-3′ refutation. None is treated as evidence. This review will not claim model identity or runtime settings that it cannot verify.

Refutation criteria, fixed before source inspection:

1. An exactly specified datum satisfying the claim's hypotheses but violating its conclusion refutes that claim. Arithmetic witnesses must use integers or exact rationals, with no floating-point evidence.
2. A failure of mean preservation or root/normalization constraints in the proposed admissible reparametrisation refutes that construction as stated.
3. A cited import whose hypotheses do not cover its actual use, an unjustified interchange of a single-source estimate with a general-data estimate, or an uncancelled T-dependent factor defeats the claimed settlement. An unsupported proof step yields NOT-VERIFIED unless an explicit contradiction or counterexample warrants REFUTED.
4. Substitution must identify every affected term and constant in NORMS §N6, including root corrections and the range of Q^j. A repaired prefactor must contain all stated dependencies and remain uniform in the quantified T.
5. Finite exact checks can refute universal claims and verify their finite instances; passing finite checks cannot replace a proof for all scales, volumes, or data.
6. The NL-3′ objection must establish a genuine mismatch with the reproduced hypotheses and calculation, not merely the absence of a proof. The original NLOC source is outside this read scope, so any conclusion restricted to the authorized transcription will be labeled accordingly.

Execution boundary: no git; only this report may be written. Large scientific files will be located with text search and read in bounded sed ranges. Authorized science inputs are TUNIF.md, REVIEW55_TUNIF.md, NORMS.md §N6, checks/r55u_2_* and checks/r55u_3_*, and cited imports in LINEAR_PACKAGE.md. Mathematical checks will run in memory with exact rational arithmetic and without creating artifacts.

## Additional check criteria, before executing checks

- Reproduce r55u_2's exact polynomial checks and inspect the actual discrepancy counts; its exit code alone is insufficient because its main function always returns zero. These are exact-input finite checks, not a proof for arbitrary closed analytic families.
- Reproduce r55u_3's Fraction decisions, replacing its floating-point display conversions in memory with exact fraction strings. Do not edit the script. Its existing origin-at-zero coordinates must be related to the actual centred root grids by translation, and its finite tests do not replace the tensor-product proof.
- Independently enumerate one-dimensional straight-average column multiplicities and centred periodic hat weights, then use their tensor products to check the claimed d = 4 norm factors. Required identities: each fine link is counted L times; transverse hat weights sum to s; interpolation is exact at roots; refinement/restriction is nested. A failed identity is a counterexample to the associated calculation.
- For the NL-3′ objection, distinguish a false inference from exponential single-source decay from a counterexample to the actual chain theorem. No claim about the latter will be made from an arbitrary fine field alone.

Additional NL-3′ witness criterion, before numeric execution: at d = 4, L = 3, k = 1, κ_0 = 1 and even coarse side T, test Y_1(X) = (−1)^{X_2}, Y_ν = 0 for ν ≠ 1. The proposed minimiser has B_{0,1}(y) equal to (3,5,3,−3,−5,−3)/119 as y_2 runs through its six-site period, with all other components zero. Verify Q_root B_0 = Q_str B_0, co-closedness of r_0, and d_0^*d_0B_0 + Q_root^T r_0 = 0 exactly. Only if these equations hold will its nonzero repeated curvature be used against the quoted universal line-sum inequality. The proposed exact line sum at y_2 = 2 is 18T/119. This witness was derived algebraically after reading N7; it is a prospective computation check, not a claim of discovery without source exposure.

## Decision

**I agree with the Opus reviewer's settlement of all four open items and the separate admissibility step. (T-UNIF), with the stated repairs, is CONFIRMED as a conditional theorem.** The condition includes (N-Q), the stated LINEAR_PACKAGE imports, and the imported vertex identity/admissible-representative rule used in NORMS §N6. This review does not independently certify those external theorem proofs or remove (N-bg).

The conclusion is for d = 4, the trivial background and the abelian/linearised setting, jointly in k and T. At general odd L ≥ 3 the soft sum is L³/(L−1), equal to 27/2 only at L = 3. This is not a constructive nonabelian Yang–Mills existence or mass-gap result.

| Item | Verdict on settlement | File and locating string |
|---|---|---|
| Mean preservation and the torus mean repair | **CONFIRMED** | REVIEW55_TUNIF.md, `N4. Lemma NL-2`, `Mean-zero is preserved`; TUNIF.md, `Constant mode`; LINEAR_PACKAGE.md, `The **straight average**` |
| Import for every r_i, including its scale factor | **CONFIRMED** | REVIEW55_TUNIF.md, `The residual terms need exponential locality`; LINEAR_PACKAGE.md, `Lemma 3.1 (J-str`, `Corollary N2-exp-b`, `Corollary 4.3` |
| H_j bounds, including the column ℓ¹ bound | **CONFIRMED** | REVIEW55_TUNIF.md, `Its cost is controlled by h`; checks/r55u_3_interp.py, `def interp`, `r55u_3-C` |
| Cell 1-form → one nested chain fixing every top root | **CONFIRMED** | REVIEW55_TUNIF.md, `TU-6's admissibility step`; TUNIF.md, `The admissibility correction is NORMS Lemma N1-6` |
| Substitution into the four NORMS estimates | **CONFIRMED** | REVIEW55_TUNIF.md, `Consumer substitution`; NORMS.md §N6, `Theorem N1-15`, steps `(1)`–`(5)` |
| Overall repaired (T-UNIF) | **CONFIRMED**, conditional as above | TUNIF.md, `Theorem TU-6 ((T-UNIF))`; REVIEW55_TUNIF.md, `After (R1)-(R7)` |
| Objection to NL-3′'s quoted general-datum line-sum inequality | **CONFIRMED**; the inequality itself is **REFUTED** | REVIEW55_TUNIF.md, `N7. [NL-corr 1]`, `for the datum Y with` |
| A claim that NL-3′'s existential T-free sup conclusion is false, or that its particular gauge has been refuted on chain minimisers | **NOT-VERIFIED** by N7's argument | REVIEW55_TUNIF.md, `that last step inherits NL-7's unproven lower bound`; see the distinction below |

All science filenames in this report are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.

## 1. Mean preservation: the missing argument is valid

For a fixed orientation μ and a fine link z, the coefficient of that link in the sum of all straight-average outputs is

\[
\sum_X Q_{\rm str}(X,\mu;z,\mu)
=L^{-d}\#\{(X,y,t):y\in B(X),\ 0\le t<L,\ y+t e_\mu=z\}
=L^{1-d}.
\]

For each t there is exactly one y modulo the fine torus and one containing block. The ratio of the fine and coarse numbers of sites is L^d, so componentwise

\[
\operatorname{mean}(Q_{\rm str}B)=L\operatorname{mean}(B).
\]

LINEAR_PACKAGE §1.2 supplies Q_root = Q_str − d∘h. A periodic gradient has zero componentwise torus mean. Also Q_root c = Lc for a constant 1-form: h(c) is independent of the coarse site. Thus both constant and mean-zero sectors are preserved, and they are orthogonal in every quadratic term of Setting SC. In the constant sector the minimum is zero, attained at c_j = L^{−(k−j)}c_k; positivity of all κ_j forces this relation at every minimiser.

For δ_x in one orientation, c_k has exactly that component T^{−d}. Consequently its level-j ℓ¹ mass is **L^{(d−1)(k−j)}**, without a factor d. The factor d used in TUNIF is a permissible overestimate.

Let b^per be TU-4's periodised field and P_0 the componentwise mean projection. Define

\[
b'_0=b^{\rm per}-P_0b^{\rm per}+L^{-k}P_kY.
\]

It has the original minimiser's curl and mean. A periodic closed 1-form with zero componentwise mean has zero fundamental cycle periods: closedness makes parallel cycle sums equal, and their average is the corresponding side length times the component mean. Path integration therefore gives a periodic λ with **b'_0=B_0−d_0λ**. This proves the claimed exactness, including the torus topology.

The mean subtraction is bounded in column ℓ¹ because P_0 is an ℓ¹ contraction. If C := Σ_{X∈Z^d}exp(−η′|X|_1), its contribution is at most **d𝔠_0 C L^{(d−1)k}**, the same bound as for b^per itself. The omitted 𝔠_0 in TUNIF's `contributing another dc_{η′}` is an arithmetic error. The quoted expression for that contribution is **REFUTED**; this is not by itself a counterexample to every possible oversized final prefactor. The old displayed 𝔠_L is not used below.

## 2. The all-level residual import is present, with the needed power

LINEAR_PACKAGE Theorem 4.2′ explicitly covers the B_k-kernels of r_{k−1} and f_0, uniformly in the fine offset, depth and torus side. Theorem 3.8 gives their general-data sup estimates. Lemma 3.1 gives both the exact identity and the bound

\[
r_i=\frac{\kappa_{k-1}}{\kappa_i}(Q_{\rm str}^{T})^{k-1-i}r_{k-1},
\qquad
\|(Q_{\rm str}^{T})^{t}\|_{\infty\to\infty}=L^{-(d-1)t}.
\]

Here r_i lives on level i+1. In d = 4 the power is −3t. Corollary N2-exp-b is named at LINEAR_PACKAGE lines 235–236, and the same all-level exponential locality is listed in Corollary 4.3. Thus the import is not merely an extrapolation from a fixed i. The scalar κ ratios telescope; they do not produce κ̂^t.

There is a finite spatial-range prefactor. One must not treat `local and does not degrade the exponential rate` as saying the prefactor is unchanged. All successive block ranges form a geometric sum, bounded in top-cell units independently of depth. Composing a whole Q power with the straight-transpose transports costs one bounded range enlargement, not one independent penalty per level.

With n=k−j and m=j−1−i, the residual contribution to the level-j potential has scale

\[
L^m L^{-(d-1)(k-1-i)}
=L^{-(d-1)n}L^{-(d-2)m}.
\]

Therefore its sum over i is bounded by L^{−3n}/(1−L^{−2}) at d=4. Its per-cell column count is at most dL^{dn}, so its total column ℓ¹ mass is O(L^n), which is within the required O(L^{3n}) budget. Its row bound is O(L^{−3n}), within O(L^{−n}). The constants are T-free. This verifies U6(d) without importing NORMS §N4 outside the permitted read scope.

## 3. H_j: proof of both norms and of centred-grid nesting

Translate the root grid so that a coarse root is at the origin. Write a level-j site as sX+t, 0≤t_a<s, s=L^{k−j}. For h=d_kμ, the α-component of the interpolated gradient is

\[
(H_jh)_\alpha(sX+t)
=\frac1s\sum_{\varepsilon\in\{0,1\}^{d-1}}
\prod_{\beta\ne\alpha}w_{\varepsilon_\beta}(t_\beta)
\,h_\alpha(X+\varepsilon),
\quad
w_0(t)=1-t/s,\quad w_1(t)=t/s,
\]

where ε_α=0. This is a positive combination of transverse coarse α-edges; it is independent of t_α. The formula holds across the cell seams as well as in the interior.

Its row sum is 1/s. For a fixed coarse edge, summing over the s longitudinal positions cancels 1/s. Each transverse periodic hat has total weight s, including both adjacent intervals. Its column sum is therefore s^{d−1}. Hence, for every torus and every μ,

\[
\boxed{\|H_jh\|_\infty\le s^{-1}\|h\|_\infty,
\qquad \|H_jh\|_1\le s^{d-1}\|h\|_1.}
\]

No bound on μ itself is required. In particular, a large or nonlocal scalar λ does not introduce a T factor through this correction. The factor 2^{d−1} allowed in REVIEW55 U6(e) is conservative; the exact row-sum bound above already includes the transverse weights.

Actual roots are centred: their offset at scale s is (s−1)/2. For s=ab,

\[
(ab-1)/2=(a-1)/2+a(b-1)/2.
\]

Thus the grids are nested after the appropriate translations. A multilinear polynomial on a coarse rectangle restricts to the same polynomial on every smaller rectangle. Restricting the one fine interpolant to intermediate roots therefore equals interpolation at that level. This is a proof in all d, including d=4; r55u_3's d=2,3 checks are supporting finite evidence only.

## 4. Admissibility: an explicit single linear family and a complete budget

Let ζ_jY be any original chain minimiser, r_i(Y) its residuals, and take the mean-corrected b'_0 above. Define the uncorrected upper levels by

\[
\widetilde\zeta_jY=Q^jb'_0-\sum_{i<j}Q^{j-1-i}r_i(Y).
\]

Since b'_0=ζ_0Y−d_0λ and Qd=d\,ev, induction gives

\[
\widetilde\zeta_jY=\zeta_jY-d_j(ev^j\lambda),
\qquad \widetilde\zeta_kY=Y-d_k\mu,
\quad \mu=ev^k\lambda.
\]

Thus these levels are forced by the fine gauge, but their top datum generally differs from Y. Set h=(I−\widetilde\zeta_k)Y=d_kμ. Let λ̂ be the one fine multilinear interpolant of μ on the top root grid. Now put

\[
\boxed{\zeta^{\rm adm}_jY=\widetilde\zeta_jY+H_j(I-\widetilde\zeta_k)Y.}
\]

This equals ζ_jY−d_j(ev^j(λ−λ̂)). The scalar λ−λ̂ vanishes at **every** top root. Hence the family is nested, its top member is Y, all residuals and fine curvature are unchanged, and it belongs to the admissible class imported by NORMS §N6. The construction is linear in Y. Its output is independent of the additive constant chosen for λ. This is the required cell-to-chain bridge, not an inference from the curl identity alone.

Here is one explicit, deliberately oversized replacement for the incomplete constant. It avoids evaluating any exponential or hyperbolic function numerically. Let

\[
q=\max(1,\mathfrak q_0),\quad
C=\sum_{X\in\mathbb Z^d}e^{-\eta'|X|_1},\quad
V=17^d,
\]

\[
A=qV\left(2d\mathfrak c_0 C+1+
\frac{d\widehat\kappa M C}{1-L^{-(d-2)}}\right),
\qquad P=2A+1\quad(d=4).
\]

M is the common entrywise kernel bound for the top residual and f_0, and 𝔠_0 is TU-4's bound for b. To justify the finite integer V, each one-step S4′ contour lies in the two neighbouring blocks. Unrolling a power gives an input-coordinate displacement bounded by
(2L−1)(L^a−1)/(L−1)<3L^a per coordinate. Expressing this in top-cell coordinates changes a cell index by at most three. Combining a forward power and a straight-transpose power is covered, conservatively, by the shifts e∈{−8,…,8}^d. The corresponding envelope is

\[
\max_{|e|_\infty\le8} e^{-\eta'|X+e-x|_1}
\le\sum_{|e|_\infty\le8} e^{-\eta'|X+e-x|_1},
\]

whose sum over X is VC. This is a larger but explicit alternative to the reviewer's e^{O(dη′)} factor. It is paid for each whole transport, not raised to a scale index.

The two 𝔠_0 terms account for b and its subtracted mean. The 1 covers the restored harmonic field. The last term is the geometric residual sum from section 2. Column counting and the row operator bound give, simultaneously for the same \widetilde\zeta,

\[
\sup_x\|\widetilde\zeta_j\delta_x\|_1\le A L^{(d-1)n},
\qquad \|\widetilde\zeta_j\|_{\infty\to\infty}\le A L^{-n}.
\]

At j=k both bounds are ≤A. Therefore

\[
\|(I-\widetilde\zeta_k)\delta_x\|_1\le1+A,
\qquad \|I-\widetilde\zeta_k\|_{\infty\to\infty}\le1+A.
\]

Applying section 3 to these two inequalities adds precisely 1+A to each normalized budget. The admissible family satisfies

\[
\boxed{\sup_x\|\zeta^{\rm adm}_j\delta_x\|_1\le P L^{(d-1)n},
\qquad \|\zeta^{\rm adm}_j\|_{\infty\to\infty}\le P L^{-n}.}
\]

This supplies a concrete repaired 𝔠_L=P and a simultaneous sup constant P, including the mean, root correction and transport range. These constants are not optimized. In particular, the proof never assumes the coarse correction h is purely exponentially decaying; its controlled mean-related tail is allowed by these two operator norms.

## 5. NORMS §N6: the substitution matches every slot

The source actually uses the following four products. Curvature and residuals are invariant under the constructed correction, so their imported bounds apply unchanged in scale.

| NORMS locating string | Factors, omitting T-free constants | Total exponent |
|---|---|---|
| `(1) Wilson vertex, δ_x in the differentiated slot` | L^{(d−2)k} · L^{−k} · L^{−k} | (d−4)k |
| `(2) Wilson vertex, δ_x in an undifferentiated slot` | L^{−2k} · L^{(d−1)k} · L^{−k} | (d−4)k |
| `(3) Soft vertex at level j` | L^{n+d−1} · L^{−n} · L^{−n}, with a bounded L² allowance | d−1−n |
| `(4) Soft vertex at level j` | L^{−(d−1)(n−1)} · L^{(d−1)n} · L^{−n}, with a bounded L² allowance | d−1−n |

Only rows (2) and (4) require the potential column ℓ¹ estimate. Every potential sup factor, including those in rows (1) and (3), uses the **same** ζ^adm. No localized-source bound is substituted for a general-data row bound.

For example, retaining NORMS's conservative constants is legitimate with 𝔠_P=P, c_m=C and M replaced by M_*=VM. The latter harmless enlargement covers the finite range in all residual-kernel uses as well. Since P≤dCP, the original potential-column bound dc_m𝔠_P L^{(d−1)n} is also valid. One admissible pair is therefore

\[
\mathfrak W_*=3M_WP^2\,[d(d-1)^2M_*C+2d^2C_fC],
\]

\[
\mathfrak S_*=3\kappa_+M_SP^2CL^2\,
[2d(d-1)\widehat\kappa M_*+2d^2\widehat\kappa C_R].
\]

M_W,M_S and the vertex/admissibility identity are the imports used by NORMS §N6; C_f,C_R are LINEAR_PACKAGE Theorem 3.8's constants. None of the newly introduced constants depends on T, k, j or x. NORMS step (5) now gives

\[
N3(D^3E_k^{\rm br}(1))
\le\mathfrak W_* L^{(d-4)k}
+\mathfrak S_*\frac{L^{d-1}}{L-1}.
\]

At d=4 this is the requested joint uniformity, with A_soft=1/L. The sum is 27/2 at L=3 and 125/4 at L=5. The report's confirmation does not endorse TU-6's unrepaired `13.5` for all L.

The periodicity repair is also essential to the stated TU-3 theorem. LINEAR_PACKAGE Lemma 4.4 explicitly supplies analytic **2π-periodic** B_k symbols, so the repaired theorem covers this application. Its line integrations, removable divisions and spread choice retain exactly one factor L^k. The finite r55u_2 checks reproduce those algebraic identities; the analytic-family argument, not finite sampling, handles the resonant fibres.

## 6. The NL-3′ objection: an actual chain witness refutes the quoted line inequality

**The objection in REVIEW55_TUNIF.md N7 is correct.** A convolution bound for one δ_x cannot be used as a spatial decay envelope for the response to arbitrary |Y|_∞≤1. Summing many source columns can fill the whole line. N7's arbitrary-fine-field ramp is not by itself a chain-minimiser counterexample, and N7 explicitly acknowledges an unproved step in its assertion about the particular NL-1 gauge. That distinction must remain visible.

The following stronger witness uses the actual S4′ chain definitions in the allowed LINEAR_PACKAGE source. Fix d=4, L=3, k=1, κ_0=1 and any even T. Let

\[
Y_1(X)=(-1)^{X_2},\qquad Y_\nu=0\ (\nu\ne1),
\]

and set B_{0,1}(y)=a(y_2), B_{0,ν}=0 for ν≠1, with period-six sequence

\[
a=(3,5,3,-3,-5,-3)/119.
\]

This is periodic on the fine side 3T and |Y|_∞=1. For each coordinate order in h(B_0), the only nonzero path contribution is (y_1−c_{X,1}) times either a(c_{X,2}) or a(y_2). Averaging the symmetric y_1 offsets makes h(B_0)=0. Hence

\[
(Q_{\rm root}B_0)_1=(Q_{\rm str}B_0)_1
=a(3X_2)+a(3X_2+1)+a(3X_2+2)
=\frac{11}{119}(-1)^{X_2}.
\]

All other components vanish, and r_{0,1}=−(108/119)(−1)^{X_2}. It is co-closed because it has only component 1 and is independent of X_1. Thus Q_root^T r_0=Q_str^T r_0. At a fine link in block X_2, the straight-transpose value is r_{0,1}(X_2)/27. The fine Euler equation reduces to

\[
2a(z)-a(z+1)-a(z-1)+r_{0,1}(\lfloor z/3\rfloor)/27=0.
\]

For z=0,1,2 the first term is 4/119 and the last is −4/119; on the other three sites both signs reverse. Every Euler equation is satisfied. Setting SC's energy is a nonnegative quadratic form, so this stationary point is a global minimiser for Y.

Its 12-curvature over the period is

\[
(d_0B_0)_{12}=(-2,2,6,2,-2,-6)/119.
\]

On the fine line in direction 1 at y_2=2, this component is **6/119 at every point**. Consequently

\[
\boxed{\sum_{y\in\ell}|(d_0B_0)_{12}(y)|=\frac{18T}{119}.}
\]

This exceeds the N7-transcribed NL-3′ bound 2d C_f c_m^{1/d}L^{−k}=8C_fc_m^{1/4}/3 for arbitrarily large even T, including T≥T_0. Thus the quoted general-data line-sum inequality is **REFUTED for actual chain minimisers**, not just unsupported by the single-source import.

This does **not** refute the existence of a T-free sup representative: the repaired TUNIF construction supplies one. It also does not prove that NL-1's particular representative has T-growing sup on this witness; a bad absolute line-sum estimate can coexist with cancellations. The verified conclusion is the failure of the quoted proof step. I did not read NLOC.md, so the attribution of that exact inequality to NL-3′ is limited to REVIEW55's transcription.

## 7. Checks actually executed and evidence boundary

All arithmetic in the executed checks was integer or Fraction arithmetic. No numerical approximation to an analytic constant was used.

- **r55u_2 reproduced:** 24 instances; total nonzero remainders, Φ values, transverse-closedness discrepancies, Dμ discrepancies, curl discrepancies and input-closedness discrepancies all **0**. Omitting b_1 gave nonzero remainders in all 24 instances. The d=2 controls gave Φ=2 and Φ=3. Both nonclosed controls fired. The concentrated primitive had zero remainders and zero equation discrepancies, as expected; this is an equation check, not a bound on its size.
- **r55u_3 reproduced with exact display substitution in memory:** A–D passed in all 24 instances; E fired. Every sup ratio was exactly 1. Every single-site-bump column ratio was exactly 1; the corresponding ratios to the incorrect s^{d−2} budget were exactly 3 or 9. Other ratios were retained as fractions, for example 169/222 and 2630831/3923478. The original file was not edited.
- **Independent mean and centred-hat enumeration:** L∈{3,5}, T∈{2,3} gave straight-average column multiplicity L and d=4 column sum 1/27 or 1/125. For s∈{3,9,27}, T∈{2,3}, each centred hat had row sum 1 and column sum s. The d=4 gradient factors were 1/3 with 27, 1/9 with 729, and 1/27 with 19683. Centred s=9 interpolation, two s=3 interpolations and restriction to the intermediate roots agreed exactly.
- **Independent NL-3′ computation:** the six Euler discrepancies were all zero; Q B_0=(11/119,−11/119) in its nonzero component and r_0=(−108/119,108/119). Direct S4′ contour averaging over all 24 coordinate orders and all 81 fine offsets at each of the two inequivalent coarse sites gave h=0 and precisely those Q_root values. The line sums for T=2,4,8 were 36/119,72/119,144/119. The displayed algebra proves the full even-T family, including the large-volume range.

Both supplied scripts return zero even independently of their printed decisions. I inspected the discrepancy counts and decisions rather than treating exit status as a certificate. Reproduction is not claimed as an independent implementation of their constructions; the independent evidence here is the derivation of the operator bounds, centred-grid checks, complete norm budget, and separate chain counterexample.

The conditional imports were checked for their stated hypotheses and matching use. Their historical review labels were not taken as proofs. In particular, REVIEW55's final cross-reference to REVIEW55_NORMS does not independently establish NQ-1 in this restricted-source review. No conclusion is made about a general background, the small-field-class C_♭ bound, nonlinear nonabelian estimates, or a complete 4D Yang–Mills proof.

## Source record

Read by bounded search/sed ranges: TUNIF §§U1–U2, §§U4–U6 and §U9; REVIEW55's relevant findings N1–N12, U2–U6, check descriptions, agreement discussion and conclusion; NORMS **§N6 only** for its scientific content; LINEAR_PACKAGE §§1.1–1.3 and the cited Lemma 3.1, Theorem 3.8, Theorems 4.2/4.2′, Corollary 4.3 and Lemma 4.4; the two authorized check scripts and their criteria. Heading searches located the relevant sections. Workflow/skill instructions were read separately for procedure. No earlier Codex review, NLOC source, other science lane, or external literature was read. No git command was run.

Local source identities (SHA-256; no git revision or current-main status is claimed):

| File | SHA-256 |
|---|---|
| TUNIF.md | `40b7dd3c41babc8ecd89789ebd2854206444310eaf47cb2820bc8f118ca0af7b` |
| REVIEW55_TUNIF.md | `29ca9187347301ba46f0b17fce4d2554b6c09382070095efa239be48e24cf891` |
| NORMS.md | `3b2c9f90cde226286c24a7169ba217eea10a203bc468e5613d8854a748aa2bd7` |
| LINEAR_PACKAGE.md | `0a2649ff5dbda9963a65ac62770a831d5e9737b9694ea873f28f008496e8e7ad` |
| checks/r55u_2_tu3poly.py | `ad99c20f6b96aa99a334cbaca3b16f2f34105068abcd376baa6acb1229df1201` |
| checks/r55u_2_criteria.md | `8b4c113005a34e87afd85699fc91f40498d2c0110c1c5e42559adfb0ca94ebcf` |
| checks/r55u_3_interp.py | `598f013dbd91be80019cc5e298eb0fdb21a66795b31489c27c55bc6387815bbb` |
| checks/r55u_3_criteria.md | `fd51509600a082cec68413bbf77c0503bf606ce4ec88a3056caeb10f1c7958f7` |

Only this report was written. Scientific source repairs are evaluated and specified here, not applied to other files.

The eight listed source hashes were rechecked at completion and matched the recorded identities. Review completed: 2026-10-28 23:09:35 UTC.

