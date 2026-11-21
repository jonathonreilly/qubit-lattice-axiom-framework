# UM cost and the C4 cycle
Provenance: Codex (GPT-6; exact runtime model ID unavailable), xhigh queue assignment; checkout `8763b32a67edef3d112b2fe4c82211711d55d083`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; grants no status.

## 1. Check of c4-order

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's Gaussian comparison and constant scheme. `SA` denotes their pinned `YM4_sketch_500.tex`, fetched once. Local paths are relative to this research folder. This addresses FINISH rows 160 and 163 only.

Checked line by line by Codex, the same provider as the source. This is not the required other-model check.

- **Row 8: CORRECT-NO-ADVANCE, conditional.** UM18 gives exactly `Theta=C_h(C_0+2+c_ell Lambda)`. UM19 and WF13d give the stated lower and upper endpoints for `lambda`. Their slopes leave room under row 3's bound on `L`. The row explicitly assumes its early cost envelope; it does not establish one.
- **Row 9: CORRECT-NO-ADVANCE.** SA 19477 requires `kappa-bar >> L kappa`. SA 14583 requires `log(exp(kappa-bar)-1)>=Theta`. The WF bound also requires `kappa-bar-1>C_h^WF(lambda+epsilon_rate)`. A sufficiently large `kappa-bar` meets these once the preceding inputs are fixed.
- **Row 12: CORRECT-NO-ADVANCE, with the cycle paragraph read into the row.** Include `delta_0 M >> kappa-bar`, not only the displayed geometric floors. Definition D permits the `M` grid when `M>=l_P`; it does not make the matrix perturbation small. Its bound retains `exp(16 kappa-bar)` (`o1-decoupled.md:120–142`).
- **Row 14: CORRECT-NO-ADVANCE as a dependency inventory.** UM15 has the exact cost displayed below. The corrected box radius is the minimum prescribed at `gates/ref-chart-regate.md:42–44`. The list is not a derivation of `K_G` from that radius. The actual UM Gaussian uses a different operator, as Section 2 explains.
- **Cycle paragraph, lines 72–75: CORRECT-NO-ADVANCE.** Line 72 identifies both opposing inequalities and the cost formula. Line 73 correctly distinguishes exterior-volume uniformity from uniformity in `M,kappa-bar`. Line 74 proposes an envelope, without proving it. Line 75 correctly rejects mere reordering as a proof. No failing step in these conditional statements. They do not imply that the cost must grow with `M`.

The literature record `lit-large-field.md:307–356` identifies the common-order analogues and their missing local uniformity. The QED3 and YM3 manuscripts were not available in the allowed source folders; those analogues remain unread. The sparse checkout's workflow was read through `git show HEAD:docs/ai_methodology/SCIENCE_WORKFLOW.md`.

## 2. What the box constants actually do

Hold `L`, the geometric ratios and the earlier analytic constants fixed. Put `n=C_Lambda M+3`. The displayed definitions give

| Constant | Exact dependence, or an upper bound from its definition |
|---|---|
| `C_Lambda` | fixed box-to-cube ratio; not a power of `M` |
| `n_b` | at most `8(C_Lambda M+1)^4` |
| `A_M` | `3n(n^4+1)=O(M^5)` |
| `C_P` | `n_b A_M^2=O(M^14)` |
| `C_c` | `160n(n+1)^2(8(n+1)^3+1)=O(M^6)` |
| `l_N` | `C_Lambda M+4=O(M)` |
| `C_5` | `O(M^14)`: its largest term is `n_b^2 l_N^6`; all other displayed terms have degree at most 14 |
| `c_*` | `1/(8C_P)`; hence `c_*^{-1}=O(M^14)` |
| corrected `alpha_*` | the minimum in `ref-chart.md:263`, also with `epsilon-bar/(2 max(1,B))`; its reciprocal is `O(M^28)` |

Sources: `ref-chart.md:53,65,71,95,189,257–263`; radius correction at `gates/ref-chart-regate.md:42–44`. These are bounds on the chosen constants, not sharp spectral asymptotics. For the radius, take the maximum of the six reciprocals: their largest degree is `14+14=28`. The new reciprocal is independent of `M`.

Section 7 then gives `a_Lambda^{-1}=O(M^33)`, `C_m,C_2.4=O(M^22)`, and `epsilon_*^{-1}=O(M^55)`. Indeed, `C_m` has degree `2+6+14=22`. The four reciprocals defining `epsilon_*` have degrees at most `33,34,50,55`. Every bound follows by multiplication of the displayed positive constants. No computation is used.

**These powers do not enter UM through a freed-box covariance.** Theorem H frees the reference-box averages. UM instead uses the next-step fibre precision `mathsf A` (SA 14097–14118), including the next average and soft gauge fixing. `ref-chart.md:267` explicitly distinguishes these operators. Thus substituting `c_*^{-1}` for UM's `K_G` has no identified basis.

The box constants restrict admitted data and the later coupling ceiling (`ref-chart.md:280–282`). At a reference, for example, its datum norm is at most `C_2.4(M) epsilon_k`. It must fit the previously fixed regular class. This is a later smallness condition, not an added positive term in the UM cost.

## 3. The exact UM budget

Write `A=A_{K_G}`, `D=A c_m L^4` and `P=C_p^UM`. SA 14526–14528 is exactly

\[
 C_0^{\rm UM}=P L^4(1+A c_m)W_0+D M^4(\varepsilon_G+\gamma_{\rm tilt}/2). \tag{1}
\]

`P` comes from the rooted domain sum and finite tags (SA 14448–14511). A fixed cubical rescaling does not change that count. It can be fixed independently of `M`. The `M^{-4}` density factor cancels the coordinate count in the `W_0` term. UM's failed-bond count and the box's `n_b` are different counts.

Fix any positive envelope `B_0`, for example `B_0=1`, before choosing rates. For any finite `K_G,P` and any fixed `M`, choose

\[
\begin{split}
0<W_0&\le\min\left\{\frac{B_0}{3P L^4(1+A c_m)},\frac{\rho_0(K_G)M^4}{2P}\right\},\\
0<\gamma_{\rm tilt}&\le\min\left\{\frac{2B_0}{3DM^4},\rho_0(K_G)\right\},\\
0<\varepsilon_G&\le\min\left\{\frac{B_0}{3DM^4},\varepsilon_0(K_G)\right\}. \tag{2}
\end{split}
\]

The three terms of (1) are then at most `B_0/3` each. Also `P W_0 M^{-4}+gamma_tilt/2<=rho_0`, which is UM14. Thus `C_0^UM<=B_0` **if the actual matrix error is at most `epsilon_G`**. The first two choices are free budgets. The third is an estimate to prove, not a free change to the matrices.

Even growth of `K_G` would not alone force growth of (1): (2) absorbs it into smaller budgets. What must be controlled is `A_{K_G} M^4` times the unavoidable matrix error. The choice `gamma_tilt=O(M^{-4})` also weakens the failed-test gain. Write `N_b<=c_b(LM)^4` for UM's bond count. Since `p_*=N_b exp(-gamma_tilt b^2/2)`, the threshold `p_*<=exp(-Theta)/4` requires

\[
 b^2\ge\frac{2}{\gamma_{\rm tilt}}\bigl[\Theta+\log(4N_b)\bigr]. \tag{3}
\]

The positive potential threshold from UM23 likewise comes after `W_0`. These are later cutoff and coupling conditions, not upper bounds on `M`.

## 4. The matrix estimate: supplied part and missing part

The exact reference bound is
`K_G>=||C_ref||+||C_ref^{-1}||+||Gamma_ref||` (SA 13911–13917). It is not just an inverse Hessian gap. The actual matrices are

\[
 C=(\chi\mathsf A(s)\chi)^{-1},\qquad
 \Gamma=-\chi\mathsf A(s)(1-\chi)\mathsf r(s). \tag{4}
\]

Here `r(s)` is the separately decoupled inverse-root series. It is **not** `A(s)^(-1/2)` (SA 14164–14170).

For the regular precision, the repaired A2 inputs give `a I<=A_real<=b I`, with positive `a,b` fixed before `M` (`a2-full.md:121–123`; `gates/a2-full-gate.md:68–76`). The checked precision-carrier implication gives

\[
 \|\chi(\mathsf A(s)-\mathsf A)\chi\|
 \le H e^{16\bar\kappa-\delta(w-R_h)/4},\qquad R_h=C_LM_1. \tag{5}
\]

Its retained premises and proof are at `gates/h-walk-gate.md:150–188`. Each varied carrier has length at least `w-R_h`. The cube count pays its parameters using half the decay; a quarter pays the collar, and a quarter the endpoint sum. Thus (5) allows **any** prescribed positive error, not just the fixed half-gap. For `w>=c_w M` and `M>=2R_h/c_w`, it is at most `H exp(16 kappa-bar-d M)`, with `d=delta c_w/8`.

First make the reference collar error at most `a/2`. Its compressed precision then has gap `a/2`, norm at most `b+a/2`, and inverse norm at most `2/a`. If the actual compressed precision differs from this reference by `e<=a/4`, its inverse norm is at most `4/a`. The resolvent identity `C-C_ref=-C(A-A_ref)C_ref` bounds the inverse difference by `8e/a^2`. This follows directly from the Neumann series. No box gap appears.

**The missing step is the second matrix in (4).** A bound on `C` alone does not give a bound on `Gamma`. One sufficient, precisely local input is the following. Put `X_s=chi A(s)(1-chi)`. Uniformly on the declared discs, require

\[
 \|\mathsf r_0\|\le R,\quad \|X_0\|\le B,\quad
 \|(X_s-X_0)\mathsf r_0\|+\|X_s(\mathsf r_s-\mathsf r_0)\|\le T E, \tag{6}
\]

Here subscript zero means `s=0` at the real reference `(U,0)`. Require `R,B,T` fixed before `M,kappa-bar` and
`E=exp(b_d kappa-bar-d M)+LM a_0+a_1+j_0+|tau-1|`. Here `j_0` bounds the independent current in its regular-class norm. Then `||Gamma_0||<=BR` and `||Gamma_s-Gamma_0||<=TE`, by adding and subtracting `X_s r_0`. We may take `K_0=max(1,2/a+b+a/2+BR)`. Together with (5), the A2 pair perturbation bound and the resolvent identity, this gives

\[
 \varepsilon_{\rm actual}\le H_0\left[e^{b_d\bar\kappa-dM}+LM a_0+a_1+j_0+|\tau-1|\right]. \tag{7}
\]

The outline asserts this combined conclusion at SA 14175–14199. Its uniform inverse-root carrier input has not been rebuilt in the cited notes. `h-walk.md:440` explicitly excludes it; `gates/h-walk-gate.md:188` preserves that exclusion. Formula (6), or an equivalent estimate for the actual composed series, remains a **gap**. A global square root of `A(s)` cannot repair it: the form away from the collar need not have a gap (SA 14202–14205).

## 5. Order of choice under the missing matrix estimate

**Conditional theorem.** Assume the uniform matrix bounds (7) and `K_G<=K_0`, with their constants fixed before `M,kappa-bar`. Then the UM budget cycle closes with `C_0^UM<=1` and `Theta=O(1)` as `M` increases.

*Proof.* Fix `B_0=1` and use `A=A_{K_0}` in (2). Keep c4-order rows 1–7, including the geometric rule and row 3's floor on `L`. Set

\[
 t_0=C_h^{\rm UM}(1+2+c_\ell g_*),\qquad
 t_1=C_h^{\rm UM}c_\ell(1+4\beta_s),\qquad
 \Theta=t_0+t_1\kappa.
\]

Choose `kappa` large enough that

\[
 \lambda_0+\sigma_0+(t_0+t_1\kappa)/L
 <\kappa/(2C_h^{\rm WF})-\varepsilon_{\rm rate}. \tag{8}
\]

This is possible since row 3 gives `t_1/L<1/(4C_h^WF)`. Choose `lambda` strictly inside (8). Choose `kappa-bar` above all row 9 floors and `Theta+1`. Then
`exp(kappa-bar)-1>=exp(Theta)`, since `Theta>0` and `e>2`. Thus UM19 and WF13d both hold.

Choose `l_P`, the response radii and the current ceiling as in row 10. Choose rows 11–12's remaining constants. Now take `M` through powers of `L`, above every existing floor and with `delta_0 M/kappa-bar` as large as required. Also impose

\[
 H_0e^{b_d\bar\kappa-dM}
 \le\min\{\varepsilon_0(K_0)/2, 1/(6DM^4)\}. \tag{9}
\]

This is a genuine floor on `M`. Indeed `e^{dM}>=(dM)^5/5!`, so
`M^4 e^{-dM}<=5!/(d^5 M)`, which tends to zero. All other factors in (9) were fixed earlier.

Choose the box constants in Section 2. Choose `W_0,gamma_tilt` by (2), and set `epsilon_G=min(epsilon_0(K_0),1/(3DM^4))`. Shrink the actual core, current and coefficient-ratio radii so their contribution in (7) is at most
`min(epsilon_0(K_0)/2,1/(6DM^4))`. Require each of `H_0 LM a_0`, `H_0 a_1`, `H_0 j_0`, `H_0|tau-1|` to be at most one quarter of this bound. Combining with (9) gives the required matrix error in (2). Equation (1) proves `C_0^UM<=1`. Hence

\[
 \delta_0M\gg\bar\kappa\ge\Theta+1,
 \qquad \Theta=C_h^{\rm UM}\bigl(1+K_*^{\rm UM}\bigr)=O(1)=o(M). \qquad\square
\]

The remaining table rows retain their order. Row 13 allows `c_WF<=b_1 kappa_far/M`; it imposes no reverse floor. Rows 14–15 only set finite box and chart constants. Row 16's radius window survives a common reduction: take `alpha_1=t`, `alpha_0=t/(2D_r)` with `D_r>CM`, then decrease `t`. The inner squared-radius conditions also hold for small `t`. Rows 17–21 set their finite bounds and UM thresholds, including (3), after these choices. Rows 22–25 put the coupling ceiling and run data last. For fixed `M`, powers of `log(g^{-2})` tend to infinity, while `g` times any fixed such power tends to zero. Writing `g=e^{-u}` and using `e^u>=u^n/n!` for an integer above that power proves the needed limiting assertion by hand. No flow constant is redefined; rows 3a and 19 keep the earlier flow and `d_0` repairs. These are dependency checks, not proofs of the estimates assigned to those rows.

Changing only `l_P` does not supply (6). It pays the number of parameter cubes along a long carrier. The unpaid first sixteen cubes still require the support collar. Taking a grid finer than `M` would also change the fixed-ratio counting argument in row 2a. With (6), the existing `M` grid suffices; without it, a new grid is not a proof of an envelope.

## Result

**The cycle closes conditionally by the explicit order in Section 5, with `Theta=O(1)`. Its closure for the actual UM matrices is not yet proved.** The remaining input is the uniform bound and collared perturbation estimate for the composed inverse-root matrix `Gamma`, specified in (6).

No cited line forces `Theta(M)` to grow linearly. The large box constants govern a different Hessian and later smallness radii. Treating their polynomial bounds as a lower bound on the UM cost would be wrong. The exact unresolved question is whether the actual inverse-root carrier series supplies (6), not whether the positive tilt budgets can be chosen. Proved here: the budget allocation and conditional order, by hand; not yet checked by the other model. No status is granted.
