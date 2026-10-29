# Residual determinant continuation

Author runtime requested: Astra / max. This worker's visible system identifies GPT-6 generically; model selection is coordinator dispatch metadata, not inferred from the mathematics.

## Pre-stated contract

Science baseline: `962f97c259d8c241df632a07e27f498f4ad33b09`. Methodology revision: `6c269770273c3fe00de350d5a3c14cacb70c2833`, freshly fetched by the coordinator. Read-only `git show` reads bind the operating map, physics-loop skill and discovery/claim-status/delivery/proof-search references to that exact revision. The installed skill was inspected first, then superseded by the pinned current-main source. No git mutation is performed by this worker. Writes are confined to this note and `checks/residual_det_*`.

Target and domain: for the actual normalized φ-chain, fixed colour rank N≥2, odd L≥3, fixed positive uniform κ, all finite depths n≥1, derive the complete quadratic residual determinant after exact fine gauge-row completion. Keep all inverses on one common finite regulator, take the thermodynamic limit at fixed external momentum and fixed n before the P→0 coefficient, and only then compare depths. The desired sufficient bound is

`|Ρ_n−Ρ_j| ≤ r(n−j) log L + C_R`, for every `0≤j≤n`, with constants independent of n,j and `0≤r<β₀^std`.

Uniform boundedness of Ρ_n or depth independence would suffice; a fixed-n block identity or a merely conditional restatement of this bound would not. The downstream objective remains the PR's full non-free SU(N) theory on R⁴ satisfying OS0–OS3. This scoped determinant calculation cannot alone establish that objective.

Accepted supplied mathematics: the Wilson action and normalized S4′ soft density of this PR, the exact finite-dimensional minimization problem and its finite-regulator analytic germ, standard finite-dimensional differential and determinant calculus. No physical axiom or primitive is added. The current primitive registry was read: its units, kinetic-form and realized-state slots do not supply a determinant estimate. The recovery tree-jet proposal is under separate independent review and will not be used as a completed input here.

Read coverage before this contract: complete `RECOVERY_UIR_ASTRA.md` (272 lines), `UIR2_55.md` (320 lines), `CODEX_REVIEW_UIR.md` (219 lines); UIR55 §§2–3.3; FLOW55 §§5.1–5.5; FLOW conventions, normalized-tree correction and U-dec/U-pair; PROOF's complete NA-alg statement/proof and TOWER-VAR statement/proof. These source arguments, including their corrections, rather than historical verdict labels, control the calculation. A broad initial repository keyword query was noisy/truncated and establishes no novelty claim; a narrower statement search will be recorded with its actual outcome.

Approach families to pursue: (A) exact joint Hessian and its differentiated Schur complement; (B) undo the h-minimization, using the local enlarged Hessian to pair apparent poles before power counting; (C) a principal continuum soft-distance model derived from the actual local vertices, followed by an explicit degree table. These are candidate mechanisms, not hypotheses that the result is true.

Check criteria fixed before calculations: preserve the 1/2 trace bubble coefficient; retain the off-shell equation-of-motion gauge rows until their exact completion; include the transverse completion and all h-exchange terms; give separate singular exponents at K=0 and K=−P before integrating. Any unmatched leading transverse term, nonintegrable separate pole, regulator-dependent rearrangement or unbounded depth-dependent coefficient defeats a claimed closure. A nonzero scalar subdiagram alone does not defeat full cancellation. Exact finite controls will compare different algebraic constructions and deliberately omit a load-bearing term; they do not prove infinite-volume field-theory instantiation.

Current author status: open. Independent review and audit status are not changed.

Pre-statement UTC: 2026-10-29T11:47:08.924413+00:00


## 1. Exact completion before any infrared approximation

This section is a finite-regulator theorem for the actual `F(U,V)=𝒯₀(U)+Ψ_min(U;V)` of FLOW55. Work on a fixed regular gauge stratum where all displayed inverses and determinant branches exist, and evaluate at the fine stationary family `U=W*(V)`. Right-chart Hessians are those of UIR2, including their BCH terms. No off-shell Wilson gauge row is set to zero.

### 1.1 The mixed block is transverse on both sides

Separate invariance gives `F_U[D_f λ]=0` and `F_V[D_c μ]=0` for every `(U,V)`. Differentiating the first identity in V and the second in U, and using that D_f depends only on U and D_c only on V, gives exactly

`D_f* Y = 0`, `Y D_c = 0`, where `Y=F_UV`.

At the fine saddle alone, `F_UU D_f=0`. Put `Z=F_UU+D_fD_f*`, `X=F_VV+D_cD_c*` and `W=H_W(U)+D_fD_f*`.

Choose orthonormal Hodge frames `S_f` and `S_c` for `ker D_f*` and `ker D_c*`, and set `I_f=D_f Δ_f^(-1/2)`, `I_c=D_c Δ_c^(-1/2)`, `Δ=D*D` on the prescribed nonzero-mode domain. Then `[S_f,I_f]` and `[S_c,I_c]` are isometries. These frames depend on the background. They are not held constant while differentiating.

In the ordered variables (fine transverse, fine gauge, coarse transverse, coarse gauge), the **actual** joint Hessian has the form

```
J = [ Z_T   0   Y_T   0 ]
    [  0   Δ_f   0    0 ]
    [ Y_T*  0   X_T   b ]
    [  0    0    b*   c ],
```

where `Z_T=S_f*ZS_f`, `Y_T=S_f*YS_c`, `X_T=S_c*XS_c`, `b=S_c*XI_c`, `c=I_c*XI_c`.

Let `R=X_T^(-1)` and define

`A=Z_T−Y_T R Y_T*`, `B=−Y_T R b`, `C=c−b*R b`, `J_red=[[A,B],[B*,C]]`.

Schur elimination, with no approximation, gives

`det J = det Δ_f · det X_T · det J_red`.                 (1)

The transverse entry which must be matched is therefore **A**, not an asserted copy of `S_f*H_WS_f`. The corrected finite `J_corr` is relevant only after this A and its actual couplings have been derived.

### 1.2 Full determinant and its measure factors

Write `S=S_c*𝒞(U)S_c`, and express W in its full fine Hodge frame, `W_H=[S_f,I_f]*W[S_f,I_f]`. The exact residual identity is

`Δ_n = ½ log det X_T + ½ log det S + ½ log det Δ_f − ½ log det Δ_c + ½ log det J_red − ½ log det W_H`.       (2)

All six determinants use the same finite regulator. Equation (2) follows by substituting (1) into the V-first Φ identity; it contains the full level-group determinant and both gauge Jacobians.

There is no additional Jacobian for the displayed **orthonormal** Hodge frames: their determinant modulus is one at every background. Their derivatives still occur inside each differentiated block. If instead gauge coordinates are written as `a=S_f x+D_f λ`, the column Gram matrix is `diag(1,Δ_f)` and

`det W = det(T_f* W T_f)/det Δ_f`, `T_f=[S_f,D_f]`.

This is why unnormalized gauge-parameter blocks with Δ² cannot be substituted into (2) without the Gram determinant. In either convention, differentiating a frame-independent determinant and then changing frame agrees with differentiating the entire moving-frame expression. Keeping just derivatives of H while omitting S′, I′, S″, I″ does not.

At the trivial point, `b=0`, `A=H_W|_T`, `B=0`, `C=Δ_c`, `X_T=Π|_T`, `S=X_T^(-1)`. These base identities alone do not identify their derivatives.

### 1.3 Exact grouped second variation

For any background curve, write `O=O₀+εO₁+ε²O₂+O(ε³)` and `G=O₀^(-1)`. Then

`[ε²]½ log det O = ½ Tr(GO₂) − ¼ Tr(GO₁GO₁)`.           (3)

Equivalently the bubble coefficient **inside** `½[Tr(GO₂)−½Tr(GO₁GO₁)]` is 1/2. For a phase-averaged ±P plane wave both ordered transfers remain. No relative-factor convention changes (3).

Since `J_red,0=diag(A₀,C₀)`, its contribution is exactly

```
½ Tr(G_A A₂ + G_C C₂)
 −¼ Tr(G_A A₁ G_A A₁ + G_C C₁ G_C C₁)
 −½ Tr(G_A B₁ G_C B₁*).
```

Thus the complete reduced-sector enumeration consists of: transverse tadpole, transverse bubble, gauge tadpole, gauge bubble, and the mixed transverse–gauge bubble. Apply (3) also to X_T, S, Δ_f, Δ_c and W_H, with the signs in (2). No residual remainder is dropped by this enumeration. It is an exact organization, not yet an infrared bound on its groups.

For independent variations i,j the Schur jets are explicitly generated by

`R_i=−R X_i R`,
`R_ij=R X_i R X_j R+R X_j R X_i R−R X_ij R`,

```
A_i  = Z_i − Y_i R Y* − Y R_i Y* − Y R Y_i*,
A_ij = Z_ij − Y_ij R Y* − Y R Y_ij*
       − Y_i R Y_j* − Y_j R Y_i*
       − Y_i R_j Y* − Y_j R_i Y*
       − Y R_i Y_j* − Y R_j Y_i* − Y R_ij Y*.
```

At `b₀=0`,

`B_i=−Y R b_i`,
`B_ij=−Y_i R b_j−Y_j R b_i−Y R_i b_j−Y R_j b_i−Y R b_ij`,
`C_i=c_i`, `C_ij=c_ij−b_i*R b_j−b_j*R b_i`.

All blocks on the right are in the moving frames; these formulas therefore retain projector/frame derivatives. Together with (3) they give the full Hessian once the actual F jets are supplied.

### 1.4 Undoing h-elimination: an exhaustive source for the F jets

Let `q(U,V,h)=Ψ(U;V^h)` before h-minimization, `Q=𝒯₀(U)+q`, `G_h=Q_hh^(-1)`, and let z denote (U,V). At an h-critical point, define `ζ_i=(e_i,−G_h Q_hz e_i)` and `c_ij=Q_hzz[ζ_i,ζ_j]`, with the last notation meaning that the other two slots run over the full (z,h) variables. Differentiating h-stationarity gives

`F₂[i,j]=Q₂[ζ_i,ζ_j]`,
`F₃[i,j,k]=Q₃[ζ_i,ζ_j,ζ_k]`,
`F₄[i,j,k,l]=Q₄[ζ_i,ζ_j,ζ_k,ζ_l]−Σ_(three pairings) <c_ij,G_h c_kl>`.

The original intermediate-level minimization can be handled by the identical tree formula with its own fixed-endpoint inverse. These formulas include the h-exchange vertices which cannot be removed merely because the *external* response h₁ρ₁ vanishes. Coordinate pullbacks from `(U,V)` to `(U,ρ)` must additionally be differentiated; the actual total pullback to `W*(V)` has no independent second-response term only after the full residual tadpole is shown to vanish.

Section 1 is frozen as an exact algebraic checkpoint. It proves neither principal-symbol matching nor boundedness of Ρ_n. The next calculation treats A's transverse correction rather than replacing it by H_W.

Checkpoint UTC: 2026-10-29T12:03:10.669809+00:00


## 2. Solved algebra of the soft-distance principal model

This section solves a specified model calculation. It does **not** identify the actual multi-level lattice action with that model. The model uses affine continuum connections A and B in the same length units, with

`q(A,B,h)=μ/2 ||B^h−A||²`, `μ>0`, `δ=B−A`, `T=ad_δ`,
`D_B=D_A+T`, `Δ_A=D_A*D_A`, `Δ_B=D_B*D_B`.

The scalar product is the invariant adjoint inner product summed over vector components. Choose the gauge convention `d B^(exp tη)/dt|₀=−D_Bη`. At h=1, h-stationarity is `D_B*δ=0`; the fine saddle is `E_A=S′(A)=μδ`. The Wilson gauge-row identity in this affine chart is `H_W D_A=ad_(E_A)=μT`. These conditions imply that `K=D_A*D_B=D_B*D_A` is self-adjoint: the difference is the adjoint action of the covariant divergence of δ, which vanishes. Inverses below have the same nonzero-mode prescription.

For the exact finite-block statements, it is enough to have compatible real/complex finite matrices D_A,D_B,H_W satisfying these identities and μ>0. The continuum notation explains their origin, but the determinant proofs do not require a continuum determinant to be defined. Fourier pole statements later are about the model's explicit homogeneous symbols.

### 2.1 h elimination and the actual transverse completion

Direct differentiation of q gives

`q_AA=μI`, `q_AB=−μI`, `q_BB=μI`,
`q_Ah=μD_B`, `q_Bh=−μD_A`, `q_hh=μK`.

For example, differentiating `q_h[η]=−μ<δ,D_Bη>` in B yields `−μD_Aη`, since `<δ,[b,η]>=<[η,δ],b>`. The h-Hessian is

`μ[D_B*D_B−½(T*D_B+D_B*T)]=μK`.

Therefore the h-minimized Hessian blocks are

```
F_AA = H_W+μI−μD_B K⁻¹D_B*,
F_AB = −μI+μD_B K⁻¹D_A*,
F_BB = μI−μD_A K⁻¹D_A*.
```

These formulas give, by multiplication, `F_AA D_A=0`, `D_A*F_AB=0`, `F_AB D_B=0`. The off-shell Wilson row `H_WD_A=μT` is cancelled, not discarded.

Let `P_A=1−D_AΔ_A⁻¹D_A*`, `P_B=1−D_BΔ_B⁻¹D_B*`. The projected h couplings are `μP_A T` and `μP_B T`: each vanishes at δ=0. Eliminating coarse transverse fluctuations and h in the opposite order gives the **exact** transverse Schur block

```
A_eff = P_A H_W P_A
 + μ P_A T Δ_B⁻¹ T* P_A
 − μ P_A(1+P_B)T [K−T*P_B T]⁻¹ T*(1+P_B)P_A.       (4)
```

This follows by first eliminating the coarse transverse block μI in the unminimized (a_transverse,b_transverse,h) Hessian. Its remaining h block is `μ[K−D_A*P_BD_A]=μ[K−T*P_BT]`; its remaining a–h block is `μP_A(1+P_B)T`. The remaining direct a block is `P_AH_WP_A+μP_A(1−P_B)P_A`, and

`P_A(1−P_B)P_A=P_A T Δ_B⁻¹T*P_A`.

Thus the missing transverse completion is generally nonzero. It is not legitimate to replace A_eff by the Wilson transverse block as an exact operator.

At quadratic external-field order around A=B=0, both explicit T factors in (4) already consume the two external fields. All other factors are therefore evaluated at zero. Writing `P=P_T`, `Δ=−∂²`, one obtains exactly

`[ε²](A_eff−P_AH_WP_A)=−3μ P ad_(δ₁) Δ⁻¹ ad_(δ₁)* P`.       (5)

The coefficient −3 is `1−4`, not zero. The finite control `D_A=(1,0)^T`, `D_B=(1,t)^T`, μ=3/2, `H_W,TT=5` gives the full value

`A_eff=5−(9/2)t²−(3/2)t⁴`.

It is obtained both from the original 3×3 unminimized Hessian and by eliminating h first. This is an algebraic control, not an actual lattice SU(N) background.

### 2.2 Separate poles of the transverse correction

For an external plane wave ±P, insertion of (5) into the transverse log determinant has the bound

`C μ |δ̂₁(P)|² / (|K|² |K+P|²)`.

The colour commutator matrices are bounded by a fixed-rank constant times |δ̂₁|, and the zero-background transverse projectors are norm bounded. There is one Wilson transverse propagator and one h propagator. The separate exponents are **(2,2)**, not (4,2) or (3,3).

For 0<|P|<r/4, the two-centre estimate proved by splitting `|K|<2|P|` from its complement gives

`∫_(|K|<r) d⁴K/(|K|² |K+P|²) ≤ C_r[1+log(1/|P|)]`.

At either pole the exponent is 2<4. On the fine saddle `δ̂₁=μ⁻¹ Ê₁=O(P² v̂)`; division by the Wilson P² density leaves `O(μ⁻¹P² log(1/|P|))→0` for every fixed μ. This is a momentum estimate, not the invalid inference that every quadratic-amplitude term is irrelevant. A separately integrable (3,3) kernel would instead give a marginal contribution; a (4,2) kernel is not locally integrable at fixed P.

### 2.3 Failed termwise route, preserved

The same harmless estimate cannot be assigned to every term of the Hodge Schur decomposition. For example, the coarse gauge-row identity gives `b=P_B ad_E Δ_B^(-1/2)` in an orthonormal gauge frame. The term `−b*X_T⁻¹b` in C can then produce a bound proportional to `|E|²/|K|⁴` in a gauge tadpole. For fixed nonzero external P this bound has a fourth-order pole at K=0, and a mere extra power of P does not repair it. The full determinant can still cancel it. I therefore did **not** integrate this piece or claim its separate negligibility. The next exact regrouping removes this artificial pole before assigning integrability.

### 2.4 An exact gauge shear removes the double-pole organization

Restore h instead of expanding its Schur complement. With fine and coarse gauge-fixing terms, the augmented Hessian is

```
O_aug = [ H_W+μI+D_AD_A*   −μI          μD_B ]
        [      −μI       μI+D_BD_B*   −μD_A ]
        [     μD_B*       −μD_A*        μK  ].
```

Before gauge fixing, `(D_A,0,−I)` is an exact null column; this follows from `H_WD_A=μ(D_B−D_A)` and K=K*. Make the triangular change

`a=a′+D_Aλ`, `b=b′`, `h=−λ`.

Its determinant modulus is one even when D_A depends on the background. The transformed fine-gauge block is Δ_A². Its only mixed entry is `D_AΔ_A` in the a′ row; eliminating λ removes precisely the added fine gauge fixing. The remaining local block is

`L=[[H_W+μI,−μI],[−μI,μI+D_BD_B*]]`.

Consequently, if J is the h-eliminated joint Hessian used in Φ,

`det J = det(Δ_A²) det L / det(μK)`.                   (6)

Eliminating the massive b block gives

`det L = det(μI+D_BD_B*) det O_eff`,
`O_eff=H_W+μD_B(μ+Δ_B)⁻¹D_B*`.                       (7)

Every factor here is necessary. Equations (6)–(7) are exact finite-matrix identities, with the actual transverse correction already included. They do not appeal to the invalid printed J_LS identification or to an omitted off-shell row.

For this model `𝒞=μ⁻¹I`, so the level group is `−(dim 1-forms−dim gauge parameters) log μ/2`. Substitution into Φ, retaining that factor and the coarse ghost, yields

```
Φ_model = ½ log det O_eff − ½ log det W
        + log det Δ_A − ½ log det Δ_B − ½ log det K
        + ½ log det(1+Δ_B/μ),                         (8)
W=H_W+D_AD_A*.
```

The dimension-dependent powers of μ cancel exactly as displayed. This provides a better grouped vertex enumeration than separately expanding the gauge tadpole of §2.3.

### 2.5 The remaining model vertices have simple poles

To separate the residual shift from a change of gauge-fixing profile, denote the right-hand side of (8), for arbitrary nearby A,B, by R(A,B). The determinant identity requires the saddle relation, but R(A,B) itself is a defined local-operator expression wherever its inverses exist. Write

`R(A,B) = [R(A,B)−R(A,A)] + R(A,A)`.

In the first bracket, B−A=δ enters only the covariant local operators D_B, Δ_B, K=D_A*D_B and the massive inverse `(μ+Δ_B)⁻¹`. No massless inverse is hidden in a vertex.

For the second term put

`f(z)=[sqrt(1+z/μ)−1]/z`, with `f(0)=1/(2μ)`,
`C_A=I+D_A f(Δ_A)D_A*`.

At a fixed ultraviolet regulator f is analytic on a neighborhood of the positive spectrum; it has no zero-momentum pole. One has

`C_A [μD_A(μ+Δ_A)⁻¹D_A*] C_A=D_AD_A*`,
`det C_A²=det(1+Δ_A/μ)`.

Thus the profile determinant in (8) is exactly the congruence Jacobian and

`R(A,A)=½log det(W+R_E)−½log det W`,

where, with `T_E=H_WD_A=ad_E`,

`R_E=D_A f T_E*+T_E f D_A*+D_A f(D_A*T_E)fD_A*`.        (9)

Equation (9) is a local equation-of-motion insertion with a covariant derivative. In particular there is no Δ⁻¹ between two E factors. The last term in (9) is needed; discarding it fails the exact matrix check.

At zero background the scalar inverses in (8) are `|K|⁻²`, and

`O_eff,0⁻¹=|K|⁻² I+μ⁻¹P_L(K)`.

The second summand is bounded. The apparent Δ⁻² h propagator in the previous organization has disappeared from the **complete** determinant before expansion.

Here is the separate-pole table for the resulting two-external-field groups. The vertices come from the local Wilson Hessian, D, massive inverses and (9); derivatives of the massive inverses introduce no massless denominator. Put K′=K+P.

| Group in (8)–(9) | Numerator / propagators before integration | Separate exponents after expanding the bound | Consequence |
|---|---|---|---|
| One residual (δ or E) and one ordinary A leg, bubble | `C(|K|+|K′|)²/(|K|²|K′|²)` | `(2,0)`, `(1,1)`, `(0,2)` | Continuous at P=0 |
| One residual and one A leg, tadpole | `C/|K|²` | `(2,0)` | Continuous at P=0 |
| Two residual legs, bubble | Same bound, or a bound with fewer massless lines | At worst the same three pairs | Bounded kernel; residual factors give O(P⁴) |
| Two residual legs, tadpole | `C/|K|²` | `(2,0)` | Bounded kernel |
| Massive profile term | Massive inverse only | `(0,0)` | Analytic near zero |
| Explicit transverse completion (5), before regrouping (8) | `C/(|K|²|K′|²)` | `(2,2)` | At worst log(1/|P|); still o(P²) after two residual factors |

For the bubble rows, each linear residual vertex contains at least one internal derivative or the external transfer P; the ordinary Yang–Mills/gauge-fixing linear vertex does too. Since P=K′−K, each is bounded by C(|K|+|K′|). Expanding the square gives the three displayed pole pairs. Quadratic vertices may contain a commutator of the two external fields with no internal derivative, but then there is just one simple massless propagator. These are statements about the model's grouped vertices, not a claim that individual Hodge-frame vertices obey those bounds.

On a fixed ultraviolet domain, the two-centre split proves uniform integrability for every s=a+b≤2 row. Hence their integrated symbols are continuous at P=0. No exchange of the P→0 limit with a fourth-order pole is used.

**Regulator scope of the infrared corollary.** If the model is supplied with a common ultraviolet completion/regulator which preserves background covariance and these local vertex bounds, the continuous coefficient of a linear residual is a covariant adjoint one-form, vanishes at the zero field by colour invariance, and its derivative Y satisfies `Y(P)P=0`. Continuity then gives Y(0)=0 by approaching along every ray. Its pairing with `δ₁` or `E₁`, both O(P²), is o(P²); the quadratic-residual rows are likewise o(P²). Under that explicit regulator condition the model has Ρ_model=0 for every μ>0.

The finite identities (4), (6)–(9), the transverse two-centre estimate, and the displayed principal-symbol pole table do not depend on selecting such a completion. What has **not** been supplied here is a standalone ultraviolet-complete continuum model or a proof that the actual lattice Φ is that completion. A hard momentum cutoff must not be declared covariant by fiat, and different determinant regulators must not be mixed. The actual-model bridge remains in §3.

## 3. Actual lattice input obtained, and the bridge still being developed

The current-main statement search was rerun precisely, using `git grep -n -F -e 'rho-null' -e 'J_corr' -e 'Ψ_min'` at `6c269770273c3fe00de350d5a3c14cacb70c2833` over docs and the named lane: no matches (exit 1). This is a bounded statement search, not an exhaustive novelty claim. The relevant unmerged prior arguments were read in full as listed above.

One actual fixed-depth premise can be derived without importing the unreviewed tree-jet transfer. Before h minimization, eliminate only the intermediate levels of the normalized soft chain, with both endpoint fields fixed. At the trivial point its quadratic form is

`κ Σ_(j=0)^(n−1) ||a_(j+1)−Q_j a_j||²`, `a₀=a_n=0`.

Let `q_n=max_j||Q_j||` (finite for the fixed finite-range S4′ maps) and `S_n=Σ_(r=0)^(n−1)q_n^(2r)`. Recursion gives

`Σ_(j=1)^(n−1)||a_j||² ≤ (n−1)S_n Σ_j||a_(j+1)−Q_j a_j||²`.

For n≥2 the intermediate Hessian therefore has gap at least κ/[(n−1)S_n], uniformly in the finite volume at this fixed depth; n=1 has no intermediate elimination. Its Bloch matrix is finite-dimensional and analytic at fixed n, so the inverse is analytic in a complex strip by compactness and invertibility on the real torus. Fourier coefficients decay exponentially. The stationary tree formulas of §1.4 then give exponentially summable jets of Ψ through order four at fixed n. This matches FLOW §23's actual fixed-endpoint argument, which was read through (I5); no n-uniform bound is inferred from this elementary gap.

The actual free symbols also give `𝒞̂_n(0)=c_n I` with `c_n>0` and the main-alias linear map M→identity after the prescribed level-unit rescaling. Thus μ=1/c_n is the candidate model stiffness. Locality of the remaining vertices and these free-symbol values are real inputs, but they do not complete the identification. In particular they do not justify replacing a differentiated Hodge projector by its constant leading value inside a separately divergent trace.

**Unfinished bridge, stated concretely.** The actual q is Ψ(U;V^h), with a nonlinear S4′ map, field-dependent matrix covariance, several fine aliases, and right-chart BCH vertices. To transfer §2 one must perform the analogue of the gauge shear (6) on this actual augmented Hessian, using a local lift of coarse gauge parameters to fine block roots. The remaining fine gauge directions and the determinant of that lift must be retained. Then eliminate the massive intermediate/alias blocks and calculate the resulting local two-field Hessian through order four. The test is whether its complete grouped difference from (8)–(9) gains a momentum power **at each potential singular centre**, including the projector and change-of-coordinate terms.

This is a finite-depth structural calculation with explicit input tensors, not the statement `Ρ_n is bounded` renamed as a lemma. It is stronger than the desired residual bound if it proves Ρ_n=0, and it has not been established by the present free-symbol data. A claim of only total-degree improvement would fail the fourth-order-pole test of §2.3. The model calculation supplies a new mechanism for that calculation: restore h and eliminate the gauge shear before differentiating the massless terms, so the separate-pole cancellation can occur algebraically.

No value or bound for the actual Ρ_n, no all-increments estimate, and no OS/non-freeness conclusion is claimed by this checkpoint. The full PR objective remains open.

## 4. Check record and author disposition

`checks/residual_det_01.py` ran once after its separate criteria file: **21/21 predicates true**, empty stderr. Its determinant coefficients use a permutation expansion, independently of the inverse/trace calculation. It rejects an omitted gauge factor, a frozen transverse frame, the incorrect A substitution, a missing Gram determinant, half the required bubble coefficient, and either omitted projected h coupling. Its pole predicates check scaling arithmetic; the universal two-centre bounds are proved in the text.

The exact finite completion in §1 applies to the actual regulated Φ. The solved soft-distance model in §2 includes its nonzero transverse completion, a determinant reorganization removing the artificial double poles, and an explicit pole table. Actual lattice identification and uniform residual control remain open. Independent review of this new unit is pending. No source, PR, git state or scientific/audit authority surface was changed by this worker.

Author classification: `actual_current_surface_status: conditional-support`; `target_claim_type: bounded_theorem`; `trace_class: upstream_support`; `reachability_to_target: supports`; `bare_retained_allowed: false`. The finite algebraic statements are exact support under their stated domains; the regulator-dependent model corollary and the unproved lattice bridge have not been promoted to an unconditional physical result.

Checkpoint UTC: 2026-10-29T12:30:48.823291+00:00

`checks/residual_det_02.py` ran once after its separate criteria file: **17/17 predicates true**, empty stderr. The second check uses independent permutation determinants for the augmented gauge shear and massive elimination, and an exact rational congruence instance for the profile restoration. Controls reject a missing Δ_A factor, a missing h determinant, the wrong background derivative in the gauge profile, and omission of the last EOM completion term.

Frozen unit for independent review: §§1–4, exact finite completion and the specified soft-distance principal-model calculation, including the explicit regulator qualification and open actual lattice bridge. Freeze UTC: 2026-10-29T12:33:32.416103+00:00
