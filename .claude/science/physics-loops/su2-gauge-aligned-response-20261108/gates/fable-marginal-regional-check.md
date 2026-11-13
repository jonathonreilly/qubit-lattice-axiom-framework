# Fresh Fable check of the three marginal suppliers

Research mathematical check, not formal audit or retained status. The owner
requested Fable approach tips; this separate fresh-context call was used for
a targeted independent-provider check. It did not receive the approach
consultation, the host checker's verdict, or the later normalized-energy
extension. The supervisor transcribed the final response below without
editing it and separately records the disposition of its minor findings.

Runtime: local CLI 2.1.321, observed model `claude-fable-5-2`, requested effort
`max`, session `acb04e1a-5da2-4463-b3d4-873ad294e0fc`. Started 2026-11-09
21:09:32 UTC; succeeded in 787883 ms. Tools, MCP and browser access were
disabled. No fallback ran. Full execution receipts remain under
`logs/su2-marginal-regional-chart-20261109/`; no hidden reasoning is reproduced.
Elapsed time and model labels do not establish mathematical correctness.

## Exact input and coverage

The reviewer received these complete files, with finite reader geometry
(radius-one collar, six/nine incidences, path bound 5L, ownership) explicitly
supplied as premises. The two older lemmas and their ancestral chain were
not recertified. The exact supplied paired-path geometry was separately
reconstructed by the host checker.

| Input relative to the pack | SHA-256 |
|---|---|
| parts/two-plaquette-compact-coercivity.md | b77fdb722d19c96594cddded301d9dd019c412b875721f5c28d1461415bb246e |
| parts/partial-terminal-normalizer-hessian.md | a17f372f928930bd9be6e81d68349a62232a027f17a13a7cd47e813f43584139 |
| parts/marginal-nonlinear-chart-estimates.md | cbc1dd1fe3ebeb75bc4c66ff6bb364e5e4fbee3b54563a0b24fb0539aa347d6f |
| parts/marginal-regional-relative-coercivity.md | 2d142414fb4992c2a1e907d42d15ca9f7164ee6e90c892d8c3d529b39e297385 |
| parts/marginal-regional-moments-and-ratios.md | b2d3d9bedfb52b11056788e1f72cd14c4f9846c733c86ee424c2240f13db647f |

Prompt SHA-256: `71060e746ffbf9a597b0e7bd834806204735d0a9ca09323160fa0090d6b4447c`.
Full final-response SHA-256: `7d7667aae13339dcdc7bb1686dc6f7698e61c7e0b0cd448d3ca720d78d220a06`.
The prompt and complete final response are preserved locally as
`fable-regional-proof-check-prompt.txt` and
`fable-regional-proof-check-result.md` in the log directory above.

## Supervisor disposition

The reviewer found no load-bearing defect in the three supplied arguments.
Its five minor points are disposed of separately, rather than discarded:

1. The sharper 5L-4 path bound was not in its supplied geometry. The host
   independently derived it from the actual paired paths: two root legs of
   at most 2(L-1) plus the bridge of L. That derivation is now explicit in
   the chart proof; no constant or inequality is changed.
2. The chart reader condition now expressly includes the local Haar factor
   and frozen components of a partially selected link. This makes the
   principal-coordinate domain unambiguous.
3. The bound |y|<=2 epsilon is absorbed in the uniform constant K in the
   regional contraction estimate. This is a constant convention, not an
   unstated smallness assumption; no formula changed.
4. The score formula now explicitly says chart-conditioned expectation,
   preserving the already stated fixed-chart/frozen-boundary scope.
5. The existence constants and buffer can be large. Torus saturation is
   covered by the same cardinality upper bounds. The primary note expressly
   makes no useful numerical-constant or practical-scale claim.

After these clarifications, the chart hash is
`b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7`.
The other two reviewed proof bytes are unchanged. The normalized-energy
extension only refreshes its chart source pin, reaching
`4e858ca74ea12b7f5a34ef0ac459526268120c30c8061d1ad633bb720e4ec2f8`.
The host checker separately verifies the final deltas, fourth proof and
primary/map scope in [its report](marginal-regional-chart-check.md). This
Fable call did not read those final deltas or the fourth proof; its scope
must not be expanded by association. The supervisor read the full response
and all four final arguments. The reviewer's auxiliary comments about the
location of a chart minimizer are not imported as an additional theorem.
The independent host proof of the complete Haar-energy result is separate.

## Supervisor publication-only whitespace reconciliation

The whole-PR whitespace check found one trailing ASCII space at line 259 of
`parts/marginal-normalized-regional-coercivity.md`. It was removed after the
host mathematical check. Exact byte comparison establishes that this single
space is the only change from checked hash `4e858ca74ea12b7f5a34ef0ac459526268120c30c8061d1ad633bb720e4ec2f8` to publication hash
`bd3fa8b5eb989c7718ad5d760a913e33166f3e9edcf52b9f17f82cbd809ca255`. The checked copy and deterministic reconciliation receipt are
preserved locally as `marginal-normalized-regional-checked.md` and
`publication-whitespace-reconciliation.json` in the log directory. No
mathematical text, source pin or claim changed. The host report remains
unaltered at its checked bytes; this is the supervisor's mechanical mapping,
not an expanded Fable review claim.

## External reviewer's final response (verbatim)

## Verdict

I found no load-bearing defect in A, B or C. Conditional on the two supplied premises and the finite-template data, I re-derived each load-bearing step by hand and each holds as stated: A(2)–(3), B(4)–(6), and C(7), (13), (16)–(17), (21), (25), (32), including the coefficient 5404. My refutation attempts (listed per target) produced no counterexample.

The three results do not combine into a compact connected-four bound or a finite-u minimiser; none of the targets claims they do. Five minor defects are at the end.

## Read limits

- **Read in full:** the two premises (compact coercivity; normalized Hessian/forest-Haar) and the three targets — five texts.
- **Not supplied, not read:** `nonlinear-chart-response.md`, `local-relative-coercivity.md`, `arbitrary-boundary-interior-moments.md`, `buffered-core-conditional-ratio.md`, `compact-forest-exchange.md`, `flat-two-step-bound.md`, `partial-terminal-normalization.md`, and the prior-art note. No load-bearing step needed them, except the constant in minor defect 1.
- **Method:** tools disabled, so everything is hand verification. No ancestral recertification, no formal audit. Premises were used as lemmas, not rechecked.

## A — chart Hessian and cube covariance

**Hessian (2).** With S = uE + Σh(κu·r) − Σlog j:

`D²S ≥ u(c − C₃δ) − C_N,2 − C_A,2 ≥ uc/2` once C₃δ ≤ c/4 and u ≥ 4(C_N,2+C_A,2)/c.

- The mean-value step gives row sums `Σ_j |∫₀¹ Σ_k ∂_ijk E(s(a,v))·(a,v)_k ds| ≤ δC₃`. It needs every reader (frozen b and outputs v) in the cube, which the hypotheses state.
- The regional case is a principal submatrix of the full Hessian at the field extended by zero; the dropped factors do not involve I. Correct.

**Normalizer bound (9).**
- The pushforward of (2/π)√(1−w²)dw under x = 1−w is (2/π)√(x(2−x)), as claimed.
- The denominator is ≥ (4/(3πe))·z^(−3/2) and the n-th moment numerator is ≤ c_n·z^(−n−3/2). The moment-to-cumulant formula is homogeneous of degree q, so |h^(q)(z)| ≤ C_q(1+z)^(−q).
- t^q/(1+tr)^q ≤ r^(−q) ≤ 2^q on r ≥ 1/2.
- Independent cross-check: Z(t) = 2I₁(t)/t, so B = I₂/I₁ and t(1−B(t)) → 3/2. This matches E_z X ≈ 3/(2z) and the premise's η_u = O(1/u). Normalizer second derivatives are O(1), not O(u).

**Cube identity (10)–(11), including corners.**
- Testing with e^S·z gives `∫∇u·∇z dx = ∫(f − ∇S·∇u) z dx`. Cosine modes have ∂_n φ_k = 0, so λ_k u_k = F_k.
- Since (k_i k_j)²(π/2δ)⁴ ≤ λ_k² and the differentiated modes stay orthogonal, the partial sums are Cauchy in H². The H² regularity, zero normal trace and density claims hold.
- Commutation: `∂_i(Lu) = L(∂_i u) + (D²S·∇u)_i`.
- Boundary term `∫_∂D ∂_n(∂_i u_n)·v_i dμ`: on a face normal to j ≠ i, ∂_j∂_i u_n carries sin(k_j π(x_j+δ)/2δ) = 0; on a face normal to i, v_i = 0.
- Gauss–Green on a Lipschitz box has only face measure, so corners contribute nothing. Because u_n is smooth, the identity holds directly for all v ∈ V; the reflection/density paragraph is redundant but harmless.
- `∫f·D*v dμ = ∫∇f·v dμ` needs only v·n = 0 and f·v ∈ W^{1,1}.
- Result: ∇u = T⁻¹∇f, Cov(f,g) = ⟨T⁻¹∇f, ∇g⟩, ‖T⁻¹‖ ≤ 1/M. Sanity check: S = Mx²/2 on an interval gives Var(x) < 1/M, consistent with the Dirichlet condition on the gradient component.

**Weighted conjugation (12).**
- W is constant diagonal and the boundary conditions are componentwise, so q_A(Wv,φ) = q_A(v,Wφ). W therefore preserves V and Dom(T) = Dom(A), and W T W⁻¹ = T + K.
- `K_ij(a) = (W_ii/W_jj − 1)·H_ij(a)`, with |W_ii/W_jj − 1| ≤ e^{αR} − 1 by the 1-Lipschitz distance.
- The Schur bound applies pointwise in a (H is a-dependent, with bounds uniform on the cube): ‖K‖ ≤ uC_H(e^{αR}−1) ≤ M/2.
- Neumann series: ‖(T+K)⁻¹‖ ≤ (1/M)/(1−½) = 4/(uc).
- W∇f = ∇f and |W⁻¹∇g| ≤ e^{−αd(A,B)}|∇g|. No volume-dependent norm enters, so (3) holds.

**Scores and orbits.** A_c = κu⟨D_cV_c, M_1,c⟩ for c ∈ O (the normalizer is V-independent but stays in the measure) and 0 for c ∈ J. (14) is the law of total covariance for the product μ×ν; the orbit term is retained and correctly left unbounded.

## B — regional stationary field and relative coercivity

**Global-to-regional step (8).** Extend q by I. An unselected factor has every reader equal to I, so W_p = 0 and |M| − ⟨·,M⟩ = 1 − 1 = 0; selected factors are unchanged. Hence E_R^J(q,I) = E_J(q̃) exactly.

The premise is applied to the global configuration q̃, never to a regional energy. Detours may leave R, because the inequality is used before restriction and the outside terms it could charge are identically zero. This is legitimate.

**Weighted inverse (12)–(13).** The spectrum of I − H_R/M′ lies in (0, ρ]. Block (X,Y) of the series starts at k₀ = ⌈dist/r₀⌉, giving (1/M′)ρ^{k₀}/(1−ρ) = g⁻¹ρ^{k₀}. The shell sum with w_X/w_Y ≤ e^{α·dist} converges for α < −log ρ/r₀. Ambient distance is the right metric for disconnected R.

**Fixed point (14)–(17).**
- f(y) is supported within r₀ of R^c, because a factor with all readers at I has zero gradient.
- On the ball of radius s = 2ABε: ‖T_y x‖_w ≤ A(Bε + K_α(s+ε)s) ≤ s/2 + s/2.
- The contraction constant is 1/2, the fixed point solves ∇_x F_R = 0, and |x*_X| ≤ 2ABε·e^{−α·dist(X,R^c)}. This is (4).

**Zero means, (19)–(21).** No zero mean is differentiated.
- The derivatives l_f,e are taken only at q = I, where all readers are O(ε) from I and |M| ≥ 1/2.
- Taylor expansion is used only on the δ-cap.
- Off the cap: |D_f| ≤ 2Kε by global Lipschitz continuity (the norm is 1-Lipschitz at M = 0), and |l·b| ≤ Kε since |b| ≤ 1, while the right side is ≥ K₀εδ².
- The cancellation Σ_f l_f,e = 0 is an identity between fixed vectors (stationarity at a* in the right-translation frame, plus zero gradient at the identity baseline), multiplied by the globally defined proxy b(q_e) = Im q_e.
- The error DK₀εΣd² = 2DK₀εΣ(1−w) is ≤ (c_g/2)Σ(1−w) under the stated smallness, so (5) holds for all compact q with c = c_g/2.
- (6) follows from zero gradient and a uniform Hessian bound on the product cap.

**Leading versus finite-u minimum.** The full conditional action is S_R = uE_R^J + Σ_c h(κu·r_c) − Σ_e log j, with h′ = B − 1. At a*:

`∇S_R(a*) = −Σ_c κu[1 − B(κu·r_c)]·∇r_c(a*) − Σ_e ∇log j(x*_e)`, with κu[1−B(κu·r)] → 3/(2r).

- Both terms are O(ε) and u-independent to leading order.
- They vanish at z = I (where a* = I) and have no reason to vanish otherwise; I did not construct an explicit z.
- Given A's bound D²S ≥ uc/2, the finite-u minimiser sits O(ε/u) from a*.
- B claims only the leading-energy statement, which is what it proves. (5) is not a bound for S_R.

## C — radial moments, rough-core ratio, jet

**Which factors survive.** ∫exp(κu⟨v,M⟩)dv = Z(κu|M|), so each J kernel integrates to exactly 1 and both its numerator and its normalizer vanish. Every K0 and every O-kernel keeps both parts.

**(7)–(8).** Take ã = (a on A, z on B_A, I elsewhere). Then E_J(ã) = E_A^J(a,z) + Σ_omitted, and omitted factors read no Q_A coordinate, so Σ_omitted ≤ K_E·T_BA. The premise then gives (7), with detours again handled globally. K_E = 6·4 + 9κ(p+1)² and K_r = 9κp² match the supplied incidences 6 and 9 and length ≤ 5L, with multiplicities.

**Cancellation (10)–(13).**
- (10) follows from (log H)′ = 1 − B ∈ [0,1] and is valid at r = 0.
- Denominator on the cap: integrand ≥ H(κu)^k·exp[−(K_E+K_r)(u·T_BA + nd²/2)].
- Numerator: ≤ H(κu)^k·e^{K_E·u·T_BA}·Π_e ∫e^{−(c_J/4)u·b}.
- Both bounds act on the same product over C_A^J, so H(κu)^k cancels with the same k, and u^(−3n/2) cancels. B_* = 2K_E + K_r is correct.

**Tower (15)–(17).**
- The conditional on N_r(x) of the θ-tilted Ω-law is the θ-tilted N_r-law (same specification, profile inside the box), with collar N_{r+1}∖N_r ⊂ Ω for r < s.
- (1+b_*)·m_r ≤ a_*|N_r|/u + b_*·m_{r+1}; iterate and close with the deterministic bound m_s ≤ 2M0(2s+1)⁴.
- Exterior-uniformity enters only through that last bound times q^s, so an arbitrary exterior is genuinely covered.
- f′(t) = u·Σ_{x∈A} E_{θ=t·1_A} T_x is correct.

**(20)–(21), (25).** The exponent is t_*C_*|S| + t_*u|S|δ²/4 − t_*u|S|δ²/2, and u ≥ 8C_*/δ² gives −t_*uδ²|S|/8. For p ≤ 1/2, both p/(1−p) and −log(1−p) are ≤ 2p.

**Scores and jet.**
- X₃ = κu⟨v_c, M_1,c⟩ only if c ∈ O and its kernel is selected. It is exactly zero for c ∈ J (no V_c anywhere) and for unselected c (the factor is absent from both Z_R and Z_good).
- The log-weight is additively separable in (ζ, s, t, ε_c, ε_d), so one-each derivatives are joint cumulants; (28) holds.
- (23) retains the orbit covariance.

**Partition arithmetic, recomputed.**
- b_k = Σ_j S(k+1,j)(j−1)!: 1+1 = 2; 1+3+2 = 6; 1+7+12+6 = 26; 1+15+50+60+24 = 150.
- g^(j) = (j−1)!/(1−p)^j.
- C4 by block type (15 partitions):
  - (4): 1·2·150 = 300
  - (3,1): 4 × (1·4·26·2) = 832
  - (2,2): 3 × (1·4·36) = 432
  - (2,1,1): 6 × (2·8·6·4) = 2304
  - (1,1,1,1): 6·16·16 = 1536
- Total 5404, as displayed.

## What does and does not transfer

- **A is not the compact four-response.** A is a two-point covariance under the chart-conditioned (hard-wall) law, with all collar readers in the δ-cube and u ≥ u_*. The compact connected-four response is κ₄(F, G, A_c, A_d) under the unrestricted law. A gives no κ₃ or κ₄ estimate and no chart probability.
- **C(32) is generic.** It bounds only κ₄(full) − κ₄(restricted to B_S^c). The same inequality holds for any event with p ≤ 1/2, with p times sup-norms, so its content is exactly (21). It has no decay in the separation of F, G, c, d.
- **A and C do not compose.** B_S^c ("not every cell of S rough") puts no coordinate inside A's chart. A four-response bound would need a sum over all rough sets plus a κ₄ bound on the good part.
- **B needs ε-small collars.** Arbitrary exteriors are covered only by C(7), at the cost −K_E·T_BA.
- **C's scope.** All of C is at V = I, s = t = 0, with c ≠ d.

## Minor defects and unverifiable constants

1. **A §3 path length.** A uses ℓ = 5L − 4; the supplied data says ≤ 5L, and the origin of 5L−4 (`flat-two-step-bound.md`) was not supplied. Use ℓ = 5L; only δ₀ shrinks.
2. **A §1 scalar subsets.** Frozen components of the same link enter through j(a_e), so "read by a factor involving I" must count the Haar factor. True as intended, but unstated.
3. **B(16).** It writes K(s+ε) although |y| ≤ 2ε. This is absorbed in the constants.
4. **A(13) wording.** D_c E f is the derivative of the chart-conditioned expectation at frozen boundary, not of the compact-law expectation.
5. **C §5 buffer.** h grows like log(1/δ²)/log(1/q) with 1−q ≈ c_J/(4(2K_E+K_r)), so the constants are far from effective. If the buffer exceeds the torus, R is the torus and the bound still holds.

Inherited and not verifiable here: the incidence counts 6 and 9, radius-one reader locality, word length, and uniformity of c_J over trees and placements. All were used exactly as supplied, and apart from item 1 no target needs more.
