# PRE-STATED

Independent hostile review of `COFM55.md`, begun 2026-10-29T00:38Z. Scope: Theorem COF and CC-FUN (b), exponentially weighted at the trivial background, uniformly in k, T and weight centre. No git; the sole write target is this file. Large source files are inspected by locating-string searches and bounded `sed` ranges. Calculations will use integers, rational arithmetic and exact symbolic inequalities only.

Prior exposure: the user brief, repository workflow, review-procedure excerpts, and a heading/locating-string search of COFM55 have been read before this section. No proof body or check output has yet been inspected. Earlier reviews supply locations, not proof authority.

Review order and falsifiers:

1. Lemma K and GU_m: reconstruct the divergence-source dual pairing, powers of n and L, scale weights, cutoff bootstrap, absorption constant, small-torus case, gauge invariance and absence of circular use of GU_m/DX_m/DB_m. A lost factor depending on k or T, a non-curvature pairing, or an unsupported weighted boundary estimate defeats the stated proof.
2. COF_m (d): compare the hypotheses and outputs of W0-loc with the actual j-only equation, including the weighted residual term, local data and Hölder norm. A local estimate with the wrong forcing or scaling is not a replacement for LE.
3. TOP-cc_m and locality: trace every input at m < m_*′ independently of the plaquette-response bootstrap. Check FLUX, DEC and FT radii in the actual distance/root convention; finite enumeration alone cannot prove all levels or tori.
4. Combes–Thomas and DX_m/DB_m: distinguish failure of a proposed proof from falsity of an estimate, and distinguish a solid-space operator bound from a gauge-invariant response bound. Require an exact argument for any claimed obstruction.
5. Weighted inventory: inspect QH_m, Proposition W versus BL-4, and the LP row sum, including endpoint restrictions and constants.

Verdicts: CONFIRMED means verified within explicitly stated supplied hypotheses; NOT-VERIFIED means a proof obligation remains; REFUTED requires an exact contradiction/counterexample to the particular assertion. Each verdict will identify a file and locating string. Final banking will distinguish conditional mathematical implications from any claim of completed constructive Yang–Mills or retained scientific status.

# Review result

**CONFIRMED, as conditional mathematical implications:** Lemma K, GU_m, COF_m and CC-FUN_m (b), with constants independent of k, T and the weight centre. The new curvature pairing and bootstrap work. W0-loc supplies the required local Hölder estimate. TOP-cc_m genuinely has the larger range m < m_*′.

This is not blanket confirmation of every sentence in COFM55. The exact funnel-radius formula fails at l = 0, although its e^{2m} bound survives. The fine-position version of the displayed LP constant needs an argument absent from the proposed elementary row sum; §5 below supplies one using the full strip hypothesis. The assertion that this exact M-prefactor is written in Proposition W is false: that proposition uses M_f. The claimed asymptotic Ma(m) ≍ mn is not established by the displayed inequalities.

All file names below refer to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. Locating strings are authoritative if line numbers move. This is review of the specified local candidate, not an audit or a verification of current-main status. The underlying linear package and the stated local elliptic/kernel inputs remain supplied mathematical inputs; I checked their relevant statements and the new uses, not every earlier proof in their ancestry. No git was used. No source, check script, ledger or other review file was changed.

## 1. Lemma K and GU_m

**Verdict: CONFIRMED as an implication of the cited LD, corrected EX, CS, W and BW inputs.**

Locations: `COFM55.md`, `Lemma K (weighted curvature-ℓ¹ dual of the plaquette response)` and `(K1)`; `BFT_A.md`, `23.2 Lemma DUAL`, `23.3 Lemma LD`, `23.4 Lemma EX`, `[RBA5-fix] U3`, `[RBA5-fix] U4'`, `28.1 Lemma CS`, and `*Lemma BW.*`.

### The pairing really is a curvature pairing

For an arbitrary level-l two-form G, with the unweighted counting pairings used by the chain,

\[
\langle d_l^*G,Y_l\rangle=\langle G,d_lY_l\rangle.
\]

No weighted integration by parts is performed. The weight is introduced **after** this identity, through the pointwise bound on G. Thus no derivative of the exponential weight and no gauge-dependent potential term is generated. Composite gauge changes add an exact one-form to each Y_l, and d_l² = 0. The right side is independent of the representative. This is the precise difference from the smooth carrier pieces estimated through ∇A in DX/DB.

CS applies to every bounded G, including a pointwise sign choice: d*G/6 is co-closed and its straight averages at all higher levels have sup at most one. The latter fact is a transverse telescoping identity, not an assumption that the sign field is smooth. Consequently, the corrected EX carrier bound gives

\[
\sum_{q'}|dg_l(q')|
\le6C_{\rm EX}(c)(k-l+1)^2L^{-2l}.
\]

For the real component used by the linear package, take G(q′) = sgn(dg_l(q′)); zero entries can be assigned zero. Fixed Lie-algebra components can be treated separately. The U3 correction to EX's cutoff derivatives must be retained in C_EX.

### The bootstrap closes without assuming its conclusion

LD is an identity of minimizers modulo composite gauge. Replacing β by β_str changes curvatures by zero. Applying d_l therefore gives (K1) directly. It does not require any norm of the original Y^p, weighted or unweighted.

Write a = L^c. The explicit curvature has coarse ℓ¹ support radius at most 4(a + 4). For a ≥ 260 and m ≤ ln(2)/(16a),

\[
e^{4m(a+4)}\le2^{33/130}<6/5.
\]

The strict inequality was checked by the integer comparison
`2^33 * 5^130 < 6^130`. This gives the stated explicit contribution (36/5)C_EX(k−l+1)²L^{-2l}.

For the screened part, W gives a bound on **curvature** at rate m′. There are six plaquette orientations and L^{4(k−l)} sites per coarse cell. Thus the complete normalization is

\[
L^{-2(k-l)}\,n^{-2}\,6L^{4(k-l)}
=6L^{-2l}.
\]

The comparisons with the source cell and the summation cell contribute e^{4m}e^{4(m′−m)} = e^{4m′}. The sum over cells is bounded by S(m′−m), uniformly on every torus. This establishes exactly the screened-part estimate used in K, with C_Z in the matching weighted convention.

The sharpened unweighted coefficient is also sufficient:

\[
48(41/20)^5=347568603/200000<1738,
\qquad a\ge6952C_j\ \Longrightarrow\ \sum_q|G_e(q)|\le1/4.
\]

The cell/position distinction in BW does not invalidate the new bootstrap. Even the conservative radius used in COFM55's appended precision satisfies

\[
4((103/100)a+1)+8=(103/25)a+12\le(21/5)a
\quad(a\ge260).
\]

Hence

\[
\sum_q|G_e(q)|e^{m\operatorname{dist}(q,p)}
\le\tfrac14 2^{21/80}<\tfrac12.
\]

The triangle inequality then gives K_l ≤ E_l + Z_l + K_l/2. For fixed k and T, this K_l is finite: the chain has finitely many sites, and the curvature is the same for every minimizer. Taking the supremum before absorption is therefore legitimate. This is not an infinite-volume limit argument and does not assume a uniform bound in advance.

For T < 8a, LD has no error source. The coarse ℓ¹ torus diameter is at most 2T < 16a, so its weight is at most 2 on the stated range. EX with r = ∞ and the data estimate give Case B. This also handles T = 1,2; k = 1 has no positive-level GU slot but does have the l = 0 statement of K.

The resulting dependency chain is acyclic:

\[
\text{LD + EX + CS + W + BW}\ \Longrightarrow\ K
\ \Longrightarrow\ \text{weighted GU sup}.
\]

The part of Theorem Y step 4 that is used is W's bound on Z′. Its subsequent applications of DX and DB are not used. Nor is the unweighted carrier bound on Y used to prove K; the remark comparing them is only a comparison.

### GU_m and summing the levels

**Verdict: CONFIRMED.** Locations: `COFM55.md`, `Theorem GU_m`, especially its proof `(i)`; `BFT_A.md`, `28.7 Theorem GU`, `28.2 Lemma TOPD`, `13.8 Lemma TS`, and `33.10 Lemma WT`.

Duality supplies f_0(p) = n²⟨G_l,dY_l^p⟩. Weighting the absolute pairing uses

\[
w(p)\le w(q)e^{m\operatorname{dist}(p,q)},
\qquad n^2L^{-2(k-l)}L^{-2l}=1.
\]

There is no lost fine-lattice volume. This proves GU_m (i). For (ii), TOPD/TS use the source-free response with datum δ_b/κ_{k−1}; the two factors L^{-2(k−l)} from G_l and dy_l cancel its 6L^{4(k−l)} plaquette count. Only the data map is used, so (ii) holds whenever 0 ≤ m < m′ < m_*′.

The lower residual relations are local straight transposes on the co-closed quantities actually appearing there. The Hölder step uses the local LES input, not the global Coulomb representative. WT and the local upper-level transfer complete (iii). Where the convenient inequality R ≤ 4n/3 fails at small n, use the existing small-n sup bound; no asymptotic assumption on n is needed.

Finally, with q = L^{−(θ−α)} ∈ (0,1), the full level factor is bounded by

\[
\sum_{t\ge1}(t+1)^2q^t
=\frac{q(4-3q+q^2)}{(1-q)^3}<\infty.
\]

Thus the level sum is genuinely uniform in k. DX_m and DB_m are absent from this argument.

## 2. COF_m step (d), and the COF/CC-FUN assembly

**Verdict: CONFIRMED. W0-loc does the required job for the j-only response.**

Locations: `COFM55.md`, `**(d) Plain currents, Hölder half.**`; `BFT_A.md`, `33.8 Lemma LES-dd`, `33.9 Theorem W0-loc`; `BFT_B.md`, `29.1 Lemma RT-cc`, part `(d)`, and `35.3 Lemma DF-cc`.

For the actual response, F = dx_0 is closed and

\[
d^*F=C(j)-(Q_{\rm str}^{(0\to k)})^T\rho_{k-1}=:h.
\]

The coordinate equation is a local scalar Laplace equation for F, with right side dh (up to the stated Laplacian sign convention). This is LES-dd with its double-divergence input set to zero. It is also the K = 0 special case of the local LES estimate. There is no use of d*Δ^{-1}F and no hidden appeal to weighted LE.

The conversion to coarse units is decisive: multiplication by n² and division by (ρ/n)^α turn R H_0, with R = n, into **n³ sup|h|**. The transpose reads at most two coarse links per component, with coefficients summing to n^{-3}. Therefore the local forcing is bounded by C(j)^c and κ_+r_{k−1} in precisely the required units. The fact that C(j) came from several levels is irrelevant once this equation has been obtained. Co-closedness of h follows automatically from the equation; no extra solvability assumption is introduced by the local estimate.

The enclosing boxes and transpose stencils have bounded coarse radius. WT multiplies the local estimate by a bounded e^{cm}, and weighted BL-C converts the box Campanato bound to the pointwise Hölder norm. The branches ρ_c > 1/4 and n < 16 follow from the weighted sup on the box. This proves

\[
[f_0(S^j)]^\infty_{\alpha,m}
\le C(m)\bigl(\|f_0(S^j)\|_{\infty,m}
+\pi_{0,m}(C(j))+\kappa_+\|r_{k-1}(S^j)\|_{\infty,m}\bigr).
\]

**Verdict: CONFIRMED, conditionally, for the complete COF_m and CC-FUN_m (b) assembly.** Locations: `COFM55.md`, `Theorem COF_m`, `**(c) Plain currents, sup half.**`, and `Theorem CC-FUN_m`.

The remaining checks were substantive:

- The non-co-closed top residual slot must first be moved into the top plain slot, or removed by DEC. SPLIT's unrepaired assertion about all residual slots would be insufficient; COFM55 explicitly uses the repair.
- Under (CC-0), d*C(j) = 0 and DF-cc replaces the total push-down by the straight push-down of the modified currents. The modified level-zero current must be **ĵ_0 = j_0 + h_0^Tψ_0** in this regrouping, as specified by COFUN_CC's later precision. The older `ĵ_0 := j_0` convention is not admissible here.
- The weighted funnel convolution and straight-transpose contraction bound Σ_lπ_{l,m}(ĵ_l), and hence C(j), without a factor k. The Σ-source version has coefficient 1 + 8/(1−3^{-3}) = 121/13 before local weight losses.
- The residual-pairing exponent is exactly `−3a − 3(k−l) + (k−l+a) = −2a − 2(k−l)`. Both resulting geometric sums converge. No top response is being assumed bounded in the proof of the sup half.
- BFT_A's older 𝒩_m notation uses cell distances in places. Passing that estimate to COFM55's position distances costs at most e^{8m}; absorb this in C_YN(m) when comparing the displayed constants. This affects no range or uniformity.
- Step (d) initially contains the **j-only** top residual. Subtracting the G- and s-response residuals, bounded by W0's top step, GU_m (ii) and W, gives the top residual of S in the stated theorem.
- DEC's residual identity contains the extra b/κ_{k−1}. COFM55 retains it through the factor G_D(m)+1. Omitting it would give the wrong residual.

The G_0 response uses QH_m/W0_m, the positive G_l responses use K/GU_m, and the plain-current pairing uses the 𝒩_m bootstrap. These are the three small-rate uses. The datum added by DEC is bounded by Proposition W and weighted BL-C. There is no remaining LE, DX_m or DB_m dependency in this assembly.

## 3. TOP-cc_m, the larger range, and locality radii

### TOP-cc_m

**Verdict: CONFIRMED for each 0 ≤ m < m_*′, with constants allowed to depend on the strict gap m′−m.**

Locations: `COFM55.md`, `Lemma TOP-cc_m` and `No step uses Y^p`; `BFT_A.md`, `33.12 Theorem W0_m`, step `2. *Top residual`, and `13.13 Corollary FP`; `COFUN_CC.md`, `Lemma TOP-cc`.

The top-residual proof uses a data response Y^{(b)}, not a plaquette response Y^p. Its G-source pairings see dy_l, which Proposition W controls. Its j-source pairing is

\[
\langle C(j'),Y_0^{(b)}\rangle
-\sum_i\langle T_i(j'),r_i(y^{(b)})\rangle.
\]

C(j′) is co-closed. Thus it can be paired with the tent representative from FP. Its weighted ℓ¹ norm is O(n³), cancelling the n^{-3} plain-current normalization. The remaining terms have the same two convergent geometric sums as COF; the absence of n² outside the pairing is matched by the absence of n^{-2} in the data-response residual bound.

Although W0_m is headed by the small-rate range, its top-residual step uses only W/FP/TOPD/TS. Reading that step separately is legitimate. Choose any m′ strictly between m and m_*′ and, wherever Proposition W itself needs an inner kernel rate, choose a further rate between m′ and m_*′. This does not force m ≤ m_*′/2 or m ≤ m_Y. There is no uniform claim as m approaches m_*′.

For T ≤ 2, the periodic lift must be used with care: a lifted localized datum has several copies, so a single-centre weighted norm on the larger torus is not literally unchanged. An independent repair is immediate and uniform: use the unweighted lift to produce the descended representative, then multiply by the small torus's weight ≤ e^{4m}. Its cell count is at most 16. This costs only a constant and leaves the entire range intact. It can also be absorbed in the large displayed S(μ) factor: μ < 1/10 implies S(μ) > 20^4, while 16e^{4m} < 80/3. No large-T loss is hidden in the lift.

The lower residual estimates use RT-cc's local transport and FT, so their larger range survives too. The RHT weight bookkeeping is 10+2 = 12 on the plain/funnel part, and 12 on the G part; e^{14m} is conservative. Combining these residual estimates with the local curvature transfer gives CC-INV_m on the smaller curvature range. This does not give a bound on gauge-dependent field derivatives.

### FLUX and DEC

**Verdict: CONFIRMED at the stated L = 3 convention.** Locations: `COFM55.md`, `Lemma FLUX_m`, `Lemma DEC_m`; `checks/cm55_loc.py`, `# ---------------- L1` and `# ---------------- L2`; `LINEAR_PACKAGE.md`, `1.1 Lattices, levels, torus` and `1.4 Norms`.

For FLUX, the upper-face links have base offsets in `[0,s−1]^4/s`, s = L^{k−l}. Their maximal unwrapped ℓ¹ displacement is 4(1−s^{-1}), attained with all four offsets maximal. Multiplying the own sup by the s³ face links cancels π_l's normalization. Thus the cost is e^{4(1−L^{l−k})m}. At m = 0 the comparison to e^{4m} is equality, so the strict `<` in the prose should be read as `≤` at that endpoint.

For a straight transpose at scale ratio s, a lower link with offset r reads its own block and, in its direction ν, the previous block only if r_ν ≤ s−2. The latter maximum is

\[
\rho_a(4s-5)+\rho_b=5(\rho_b-\rho_a)<5\rho_b.
\]

This proves the all-scale bound, not just the cases in cm55. In particular the one-step top transpose has radius 5(1−1/3) = 10/3. For h^Td*, block-interior support imposes the same missing endpoint in the output-link direction, so its radius is at most 10/3 as well. This proves DEC's e^{(10/3)m} factor. For a different odd L the corresponding exact radius is 5(1−1/L); the literal 10/3 is an L = 3 constant. Torus wrapping can only shorten these distances.

### FT: the bound is right; the claimed exact formula has an exception

**Verdict: CONFIRMED for e^{2m}; REFUTED for the unconditional exact formula `2(ρ_{l+1} − ρ_0)` at l = 0.**

Locations: `COFM55.md`, `4.4 Lemma FT (iv)` and `R-2`; `checks/cm55_loc.py`, `def ft_radius` and `DFT2 = ft_radius(2, (0, 1), "centre")`; `BFT_B.md`, `29.2 Lemma FT`, parts `(i)` and `(iv)`.

Here is a nonzero read that the exact formula misses. Let L = 3, k = 1, T = 6, l = l′ = 0, and take the block with root c = (1,1,1,1). The output link has base (0,0,0,2) and direction 1. The order-averaged h coefficient of this link is **−1/324**: the target is (0,0,0,2), direction 1 is last, and precisely 6 of the 24 orders traverse it backwards. The divergence at c reads the direction-4 link with base c−e_4 = (1,1,1,0). The base-point distance is

\[
(1+1+1+2)/3=5/3,
\]

whereas the asserted formula gives 2(1−1/3) = 4/3. This is not a zero-coefficient stencil artifact. A current along the three-link path joining c−3e_4 to c has divergence only at those two coarse roots, so the root-support restriction does not eliminate the read.

The correct maximal **unwrapped** radii for centre roots are

\[
D_{\rm FT}(l)=
\begin{cases}
(2L-1)\rho_0,&l=0,\\
2(\rho_{l+1}-\rho_0),&l\ge1.
\end{cases}
\]

To derive them, the read root at level l′ has position
`ρ_{l+1}X + (ρ_{l+1}−ρ_{l′})/2 · (1,1,1,1)`, and d* reads that point or one step backwards. The output has offsets ρ_l r with one coordinate at most L−2. For l′ = l the maximal distance is (2L−1)ρ_l. For l′ < l, the centre displacement dominates and the maximum is 2(ρ_{l+1}−ρ_{l′}); its maximum occurs at l′ = 0. Both branches are strictly less than 2 when l < k.

Thus e^{2m} is valid for all k, including k = 1. The exact values 16/9 at k = 2 and 52/27 at k = 3 are correct. The script takes a maximum over l = 0,1 at k = 2, masking the l = 0 formula error; it does not test k = 1. With corner roots, the cited 8/3 read is real and e^{2m} no longer follows. The centre-root convention is essential to this particular constant.

## 4. Combes–Thomas and the DX_m/DB_m claim

### What is, and is not, ruled out

**Verdict: CONFIRMED for the Neumann-series algebra and for the failure to infer it directly from the banked gauge-invariant estimates.** Locations: `COFM55.md`, `3. T8`, items 1–3; `BFT_B.md`, `**Lemma BB-MCT: PROVEN-HERE.**`.

The algebra requires a single invertible operator on specified spaces and a bound on its conjugated perturbation in those same spaces. COF and GU control curvature/residual outputs from particular source norms. They do not bound the undifferentiated potential generated when multiplication by a weight is commuted through the Hessian, or ensure preservation of a gauge slice. Consequently those estimates alone do not instantiate the template.

**Verdict: CONFIRMED for nonuniformity in the natural own-unit solid spaces, with an independent exact witness.** Location: `BFT_B.md`, `B3-F3: OCCURS for solid norms`; normalization input: `BFT_A.md`, `8.2 BL-2`, the identities `Q_l(ae_μ) = L·ae_μ` and `Q_str^T` on constants.

Consider the Hessian of the stated chain energy on its spatially constant one-component sector, with x_k = 0. This sector has no gauge kernel. For the test chain x_j = L^{j−k}e_1, all residuals except the top one vanish, dx_0 = 0, and the top residual is e_1. In the own-unit counting ℓ² norm,

\[
\frac{\langle x,Hx\rangle}{\|x\|_2^2}
=\frac{\kappa_{k-1}}{\sum_{t=1}^kL^{2t}}
\le\kappa_+L^{-2k}.
\]

Constants are orthogonal to every periodic gradient, so this is a positive-sector small-eigenvalue witness, not an exploitation of a zero gauge eigenvalue.

There is also an exact ℓ∞ inverse witness. Use the constant source j_0 = e_1, j_j = 0 for j > 0. The constant-sector Euler equations give

\[
\kappa_i r_i=L^{3(i+1)}e_1,
\qquad
x_0=\sum_{i=0}^{k-1}\frac{L^{2(i+1)}}{\kappa_i}e_1.
\]

Thus the own-unit inverse norm is at least κ_+^{-1}Σ_{t=1}^kL^{2t}. This verifies the cited lower-bound phenomenon without relying on a numerical smooth-mode argument. It concerns the full solid-space inverse; it is not a counterexample for divergence-form inputs measured in the COF/GU norms, nor a theorem about every possible rescaled or restricted space.

**Verdict: NOT-VERIFIED for the literal asymptotic `Ma(m) ≍ m·n`.** Location: `COFM55.md`, `My own scaling count agrees (ARGUED, not a theorem)`.

The displayed commutator inequality is an **upper bound** for one block. Combining an upper bound O(m/n) with an inverse lower bound does not establish a two-sided asymptotic for their product, a lower bound on the full conjugated operator, or failure of every relative perturbation estimate. BB-MCT's coarse crude estimate and COFM55's fine-block count are also different bounds. What is bankable is the missing uniform hypothesis in the proposed application. A general prohibition on Combes–Thomas methods, smoothed weights, different norms or relative-form estimates is not proved here.

### DX_m and DB_m are not the proposed rate shift

**Verdict: REFUTED for the claim that the cited DX/DB proof becomes weighted simply by replacing m′ with m′−m.** Locations: `REVIEW_BFT_A_S6.md`, `DX_m, DB_m: mechanical, 1-2 pages`; `BFT_A.md`, `18.4 Theorem XR`, steps 3–5, `18.5 Theorem XB`, steps 3–4, and `18.2 LRL (a)`; `COFM55.md`, `R-7`.

Those proofs estimate A−Q_str^T𝔽A and related smooth pieces through the gradient of the **global Coulomb representative**. LRL (a) obtains `(1+D)^{-5}` by cancellation of the zero total curvature in its far-field term III. The input curvature is exponentially localized, but that estimate on ∇A is polynomial. Replacing the test-current sup by exponential growth therefore gives an unbounded majorant as T increases; it cannot be handled by the stated rate substitution.

A polynomial upper bound alone would not prove an actual tail. The following independent example identifies the obstruction to an exponential estimate for that representative. On the infinite lattice, let B = δ_0e_1 and F = dB, which is exact and finitely supported. The Coulomb representative has symbol

\[
\widehat A_1=1-|\nu_1|^2/\psi,
\qquad \psi=\sum_a|\nu_a|^2,
\qquad \nu_a=e^{ip_a}-1.
\]

The symbol of ∂_2A_1 is ν_2(1−|ν_1|²/ψ). Its directional derivatives at zero are 0 in direction e_1, i in direction e_2, and i/2 in direction e_1+e_2. These cannot be the derivatives of a differentiable function. Exponentially summable coefficients would give an analytic symbol, a contradiction. Uniform exponential estimates on the corresponding growing tori would imply such an infinite-lattice estimate. Thus the lost exponential localization is a real feature of this representative, not merely a loose inequality.

This refutes the claimed proof shortcut, **not DX_m or DB_m themselves**. Their co-closed pairings may admit cancellations or other representatives. They remain NOT-VERIFIED by the cited work. K avoids the issue because its integration by parts pairs directly against dY.

## 5. Weighted-input inventory and the exact LP constant

### QH_m and Proposition W

**Verdict: CONFIRMED for the relevant Lipschitz-weighted QH_m input.** Locations: `BFT_A.md`, `33.11 Lemma QH_m`; `REVIEW_BFT_A_S7.md`, `Lemma QH_m (33.11): CONFIRMED`; `COFM55.md`, `R-3` and its definition of `||G_0||^L_m`.

The needed norm is 𝒬^L_{H,m}, with a position-distance weight inside a **local** pointwise Hölder norm. Its multiplier is ≤ 1 and has Hölder seminorm ≤ 8m for separations at most one. Its bootstrap coefficient is bounded by

\[
\tfrac14(1+8m)e^{(41/10)mL^c}<1
\]

on the stated small-rate range. The added explicit-field term is proportional to mL^c, which is bounded there. Its screened term uses W, and its small-torus branch uses the bounded diameter. No DX_m or DB_m is hidden in that proof. The old `28.13` heading saying 𝒬_{H,m} is ARGUED is stale as an inventory of this Lipschitz-weighted input; it should not be confused with an assertion about discontinuous cell weights inside a Hölder product.

**Verdict: CONFIRMED that Proposition W supplies weighted BL-4, including the local Hölder step.** Locations: `BFT_A.md`, `13.9 Proposition W`, `*f_0 Campanato (the weighted LES)*`, `*Weighted BL-C.*`, and `*Assembly.*`; `COFM55.md`, `4.3 BFT_A Proposition BL-4`.

The only global maps are the two data kernels. The remaining current, local LES, Campanato-to-pointwise and upper-level transfers have bounded coarse support. The proof therefore works for every 0 ≤ m < m′ < m_*′. It does not derive a Hölder modulus in the fine offset directly from LP 4.2; that regularity comes from the local elliptic step.

### The raw row sum needs its offset convention stated

**Verdict: CONFIRMED for `C_D(m) = 4M coth^4((m′−m)/2)`, with the additional strip argument below for the position-weighted f_0 norm. REFUTED for the assertion that this exact M-prefactor is written in Proposition W's f_0-sup step.**

Locations: `COFM55.md`, `4.2 LINEAR_PACKAGE Theorem 4.2 (ii)` and `This is written in BFT_A Proposition W's`; `LINEAR_PACKAGE.md`, `Theorem 4.2'`, `Lemma 6.7 (KF)`, and `Theorem 6.8`; `BFT_A.md`, `13.9 Proposition W`, `*f_0 sup.*`; `PROOF.md`, `Lemma KF`, locating string `the offset of a fine plaquette inside its coarse cell is absorbed into e^{4m'}`.

For the integer cell displacement and μ = m′−m,

\[
\sum_{Z\in\mathbb Z^4}e^{-\mu|Z|_1}
=\left(\frac{1+e^{-\mu}}{1-e^{-\mu}}\right)^4
=\coth^4(\mu/2).
\]

There are four input link orientations and no sum over output offsets. Periodization turns the sum over torus inputs and images into this single lattice sum, uniformly in T. This directly gives 4MS(μ) for the coarse residual output or a cell-weighted fine output.

For the position-weighted fine output at P = X+u/n, the elementary triangle-inequality argument instead gives **4e^{4m}MS(μ)**: the offset satisfies |u/n|_1 < 4. Also, Proposition W literally uses **4M_fS(μ)**, where LP defines M_f = Me^{8m′}(1+6κ̂_SC). It does not contain the asserted equality with 4MS(μ).

Nevertheless the smaller displayed 4MS(μ) can be retained using LP 4.2′ **(i)**, which bounds each full per-offset symbol by M throughout the strip. Here is a proof independent of the disputed row-sum sentence. Partition Z⁴ into its 16 sign orthants. Contour shift and Parseval, at imaginary part ±m′ in each coordinate, give for each orthant O

\[
\sum_{Z\in O}|K_u(Z)|^2e^{2m'|Z|_1}\le M^2.
\]

Cauchy–Schwarz on that orthant, then addition of the 16 bounds, yields

\[
\sum_Z|K_u(Z)|e^{m|Z|_1}
\le\frac{16M}{(1-e^{-2\mu})^2}.
\]

The position factor is absorbed by the slack in S(μ). Set q = e^{-μ}. The strip definition gives m′ ≤ 1/10, hence q > 9/10 and e^{4m} < 5/3. Therefore

\[
\frac{16e^{4m}/(1-q^2)^2}{S(\mu)}
=\frac{16e^{4m}(1-q)^2}{(1+q)^6}
<\frac{800000}{141137643}<1.
\]

After multiplying by four input orientations and periodizing, this proves the requested **4MS(μ)** position-weighted bound with the original strip M. Thus the value is bankable, but the author's purported two-line derivation and attribution need this correction. Merely having the entrywise envelope, without the full strip bound, would not justify dropping the offset cost.

### Rate convention

**Verdict: CONFIRMED with the minimum retained; NOT-VERIFIED as an unrestricted identification of the two branches for arbitrary soft-constant intervals.** Locations: `COFM55.md`, `m_Y := min(m′/2, ln 2/(16L^c))` and `**How small m must be.**`; `BFT_A.md`, `28.13`, last bullet.

The general proved range is

\[
0\le m\le\min\{m_*'/6,\ln(2)/(16L^c)\},
\qquad m'=m_*'/3.
\]

Calling the endpoint simply ln(2)/(16L^c), as in the request, also requires ln(2)/(16L^c) ≤ m_*′/6. This is consistent with the tabulated cases and can always be enforced by increasing the fixed c after the positive strip is supplied. The exact arithmetic comparison of tabulated decimals does not independently certify those strip widths or a uniform lower bound over an arbitrary κ interval. No such new certification was performed here.

## 6. Exact checks and disposition of remaining claims

Four in-memory `python3 -I -B` invocations used only integers, `fractions.Fraction`, and finite combinatorics. They created no artifacts. They checked:

- The explicit-part factor 2^{33/130} < 6/5, the BW radius comparison, and `48(41/20)^5 < 1738`.
- The funnel extrema separately at every l for k = 1,2,3,4. The rows were respectively `5/3`; `5/9,16/9`; `5/27,16/27,52/27`; and `5/81,16/81,52/81,160/81`.
- The nonzero h coefficient −1/324 of the l = 0 counterexample by enumerating its paths. An initial hand-entered diagnostic witness line had the wrong coordinates; that line was superseded by this explicitly recomputed witness before any verdict was based on it.
- The constant-sector Euler equations for k = 1,…,5 with rational, nonconstant κ_i, and their exact x_0 formula. The all-k proof is the recurrence in §4, not those examples.
- Straight-transpose displacement maxima at s = 3,9,27: `10,40,130`, agreeing with `5(s−1)`.
- An entrywise-envelope-only weighted-row diagnostic, and the rational Parseval slack bound `800000/141137643 < 1`. The envelope diagnostic is not a counterexample to the actual LP kernel; the full strip hypothesis resolves that issue.

I read the cm55 criteria, scripts and relevant recorded output; I did not rerun or modify the author's checks. Their finite locality tests do not establish uniformity in k or T. The coordinate arguments, finite-dimensional bootstrap and summable level factors above establish that uniformity for the reviewed implications.

Remaining NOT-VERIFIED items are the general DX_m/DB_m estimates, a successful configuration-space Combes–Thomas application, and the literal two-sided Ma(m) asymptotic. Nothing here establishes the gauge-dependent field-component half of BFT-5 (b), its transfer to Z ≠ 1, a nonlinear contraction, a k-independent bound on every nonlinear row's source norm, or a constructive four-dimensional Yang–Mills theorem. The supplied package itself is not newly audited by this review. Only the requested review file was written.

## Exactly what may be banked

Fix the trivial background, the stated root map with centre roots, fixed L and 0 < κ_- ≤ κ_i ≤ κ_+, and 0 < α < θ < 1. The numerical locality constants 10/3 and 121/13 are for L = 3. Assume the cited linear package, corrected EX, local elliptic estimates and weighted W/W0/Y inputs with their stated hypotheses. Choose c so that L^c ≥ max(260,6952C_j) and ln(2)/(16L^c) ≤ m_*′/6, and put **m_Y = ln(2)/(16L^c)**. Without the last condition, retain the minimum above. Constants may depend on these fixed parameters and rates, but not on k ≥ 1, T ≥ 1 or the weight centre.

1. **CONFIRMED:** Lemma K,
   \[
   \sup_p\sum_{q'}e^{m\operatorname{dist}(q',p)}|dY_l^p(q')|
   \le C(m)(k-l+1)^2L^{-2l},\qquad 0\le m\le m_Y,
   \]
   and GU_m (i)/(iii), including its uniform level sum. These need neither DX_m nor DB_m. Locations: `COFM55.md`, `Lemma K` and `Theorem GU_m`.

2. **CONFIRMED:** COF_m under (CC-0), and, after DEC, CC-FUN_m (a), (b) and (c) for every stated composite-co-closed source S with B_k = 0:
   \[
   \|f_0(S)\|_{\infty,m}+[f_0(S)]^\infty_{\alpha,m}
   \le C(m)N_m(S),\qquad 0\le m\le m_Y.
   \]
   In particular the requested (b) form with `N_m(S)+κ_+||r^c_{k−1}(S)||_{∞,m}` also holds. Both source-norm versions N_m and N_{Σ,m} are allowed. W0-loc supplies the local Hölder step. With the stated local residual/curvature transfer, the same range gives **||x(S)||_{inv,m} ≤ C(m)N_m(S)** and its N_{Σ,m} version. Locations: `COFM55.md`, `Theorem COF_m`, `Theorem CC-FUN_m`, and `Theorem CC-INV_m`.

3. **CONFIRMED on the larger range:** TOP-cc_m and the lower gauge-invariant residual bounds for every **0 ≤ m < m_*′**, with constants depending on a strictly positive strip margin. Locations: `COFM55.md`, `Lemma TOP-cc_m` and `Its residual half`; `BFT_B.md`, `29.5 Theorem RHT_m-cc`.

4. **CONFIRMED inputs and bookkeeping:** Lipschitz-weighted QH_m; Proposition W as weighted BL-4; the LP constant **4M coth⁴((m′−m)/2)** with the full-strip argument in §5; FLUX's **e^{4(1−L^{l−k})m}**, DEC's **e^{(10/3)m}** at L = 3, straight transposes' **e^{5m}**, and centre-root funnels' **e^{2m}**. The exact funnel radius must use the piecewise formula in §3. Locations: `BFT_A.md`, `33.11 Lemma QH_m` and `13.9 Proposition W`; `COFM55.md`, `4.1`, `4.2`, and `4.4`.

