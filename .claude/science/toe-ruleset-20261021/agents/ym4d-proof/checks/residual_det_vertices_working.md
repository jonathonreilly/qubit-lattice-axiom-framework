# Actual residual vertices: normalized gauge path and equation-of-motion trace

This is a separately reviewable continuation. The original model note and the harmonic/free-symbol checkpoint remain frozen. The target is the actual normalized action's residual coefficient, not a new physical axiom. Every auxiliary gap below is distinct from the physical Hamiltonian mass gap now included in the full requested theorem.

The load-bearing local sources are the [frozen harmonic lattice bridge](residual_det_lattice_bridge_working.md), the [finite/model determinant construction](../RESIDUAL_DETERMINANT_ASTRA.md), the [actual root-sector residual definition](../UIR2_55.md), the [normalized flow conventions](../FLOW55.md), and the [actual contour/action definitions](../PROOF.md). The [harmonic-bridge review](../REVIEW_RESIDUAL_LATTICE_BRIDGE_ASTRA.md) confirms only its stated finite/free input; it does not review the new vertices below.

## Pre-stated target and discriminating criteria

At fixed depth n and κ>0, preserve the same finite determinant and gauge domains as the harmonic checkpoint. Derive a local off-shell residual representation, then prove that its mixed equation-of-motion/background coefficient is continuous and that its quadratic-residual coefficient is negligible after multiplying by the two external O(P²) residual factors. The needed conclusion is the actual Ρ_n=0 (or an explicit weaker all-increments bound), not free-symbol equality alone.

The decisive algebraic checks are: (i) an exact normalized gauge-change identity at ρ=0, with the Wilson off-shell row retained; (ii) a gauge path whose **massive-band Schur** longitudinal coefficient is identically one; (iii) cancellation in the differentiated gauge condition at fixed fluctuation, not after silently differentiating its minimizer as if it were fixed; (iv) all separate pole powers stated before integration. A finite-regulator identity does not establish the periodic thermodynamic limit. Any unsupported passage remains a hypothesis here.

## 1. A local h=1 saddle section at fixed depth

Before minimizing h, the actual free fine Hessian with only internal gauge fixing is

`Z_int=H_W+M*𝒞⁻¹M+D_fP_intD_f*`.

It is strictly positive on every free Bloch cell, including K=0. For K≠0, zero Wilson energy makes a=D_fλ; zero soft energy gives `D_c evλ=0`, hence evλ=0; then zero internal fixing gives `Δ_intλ_int=0`, hence a=0. At K=0 a closed fine one-form is a gradient plus a constant one-form. The top map sends the latter to ℓ times that constant, so zero soft energy removes it; subtracting the root value from the remaining periodic scalar and using Δ_int removes the gradient. Compactness of the Brillouin cell therefore gives a strictly positive fixed-depth gap, uniform in the number of cells.

A local analytic gauge section near the trivial field can consequently be obtained by minimizing the unminimized Q(U,V,1) with a nonlinear internal Coulomb penalty. Variation along the internal gauge group forces the penalty to vanish near the trivial point, because its Faddeev–Popov derivative is Δ_int there. The resulting critical point has Q_U=0. The combined fine/h gauge identity `D_f*Q_U−ev*Q_h=0` then gives Q_h=0 as well, since ev* is injective. Thus this is an h=1 representative of the same fine/h saddle, not a replacement tree action.

At each finite volume the implicit-function theorem gives its Taylor germ. The inverse of Z_int has an exponentially decaying kernel at fixed depth, so the finitely many tree derivatives needed for the present second variation are local and have analytic Bloch symbols with volume-uniform fixed-depth bounds. This route supplies an analytic external tree section without applying an external inverse Laplacian. The local section is equivariant under coarse gauge transformations up to an internal gauge transformation; all determinant expressions used below are invariant under that internal transformation. No n-uniform background neighborhood or physical spectral gap follows.

## 2. What the harmonic expression becomes exactly at zero residual

Let R(U,V) denote the right side of A5 in the harmonic checkpoint, using the actual H_loc, H_h, M and 𝒞 at h=1. It equals the original Δ at the actual fine/h saddle. It is also a finite off-shell function wherever its matrices are invertible; its off-shell value is not asserted equal to the original Φ.

Set V=𝔪(U), so ρ=0. The unminimized soft Hessian is exactly the Gauss–Newton block `(-M,I)*𝒞⁻¹(-M,I)`, and `H_h=G_c`. Eliminate the massive coarse one-form block and put

`R_c=(I+D_c*𝒞D_c)⁻¹`,

`F_1=P_intD_f*+J R_c^(1/2) D_c*M`,  `F_0=D_f*`.

Both F_j map fine one-forms to fine scalar coordinates; the root output of F_1 is identified through J. Its fixing form is

`F_1*F_1=D_fP_intD_f*+M*D_c R_c D_c*M`.

Using the harmonic scalar coordinates (I,L),

`det(F_1D_f)=det Δ_int ·det Δ_c ·det R_c^(1/2)`.

The massive coarse determinant, the 𝒞 normalization, H_h and G_c then cancel exactly as specified in A5. Consequently

```
R(U,𝔪(U)) = Γ_F1(U)−Γ_F0(U),
Γ_F(U)=½log det(H_W(U)+F(U)*F(U))−log det(F(U)D_f(U)).   (V1)
```

This is a normalized **Wilson gauge change**, including its scalar determinant. It is not zero off shell merely because it is a gauge change.

## 3. The exact equation-of-motion derivative

For any differentiable family F_t with invertible `Q_t=H_W+F_t*F_t` and `B_t=F_tD_f`, define `T_E=H_WD_f`. Gauge invariance makes T_E a local operator linear in the Wilson equation of motion E_W; it need not vanish off shell. Direct differentiation gives

```
∂_t Γ_Ft
 =Tr(Q_t⁻¹F_t* dotF_t)−Tr(B_t⁻¹dotF_t D_f)
 =−Tr(Q_t⁻¹ T_E B_t⁻¹ dotF_t).                         (V2)
```

The second equality uses `Q_tD_f=T_E+F_t*B_t`. The two scalar traces cancel by cyclicity. The initial ½ is present in the derivative of log det Q_t and cancels only because the two transposed variations of F_t*F_t give equal real traces. V2 does not change the ½ bubble coefficient in a later second variation.

For explicit locality, in right link charts U_l exp(a_l), choose `D_Uλ=Ad(U_l⁻¹)λ_x−λ_y` on l=(x,y). Expanding the gauge action to first order in a gives the generator derivative `½[Ad(U_l⁻¹)λ_x+λ_y,a_l]`. Differentiating the Ward identity therefore gives

`(T_Eλ)_l=−½[E_l,Ad(U_l⁻¹)λ_x+λ_y]`.

An opposite generator convention changes the matching signs together; V2 uses T_E=H_WD_f and is invariant under that choice. This is the actual lattice endpoint row, not a substitution of the continuum shorthand ad E. It has finite range and no inverse derivative.

## 4. A path preserving the low longitudinal coefficient

Use

```
F_t=P_intD_f*+J[u(t)J*D_f*+v(t)R_c^(1/2)D_c*M],
u(0)=1, v(0)=0, u(1)=0, v(1)=1.
```

For fixed depth put α=ℓ² and r=ℓ⁴−1. Choose the positive path

`u=1−t`, `v=sqrt(1+r u²)−αu`.

Then `a:=αu+v=sqrt(1+r u²)>0`. An equivalent rational parametrization, useful for exact controls, is

```
z=1−t,
u=2z/[(α+1)−(α−1)z²],
v=(1−z)[(α+1)−(α−1)z]/[(α+1)−(α−1)z²].
```

These are the same curve with different parameter speeds. The coefficients are nonnegative, and `a²=1+r u²` along either parametrization. The profile R_c^(1/2) has local Taylor kernels: I+D_c*𝒞D_c has a positive lower bound one at the free point, a fixed-depth upper bound, and local coefficients; analytic functional calculus and its differentiated resolvents therefore have an exponential fixed-depth bound. In harmonic scalar coordinates,

`det B_t=det Δ_int ·det b_t`,  `b_t=uS+vR_c^(1/2)Δ_c`.

At the free point b_t is a positive scalar symbol away from K=0. All high bands of Q_t are massive, and the low gauge coefficient is computed below. This gives a regular path in a neighborhood of each specified finite regulated base point. No common open background neighborhood in infinite volume is asserted.

### 4.1 High gradients change the apparent coefficient

Let `b=J*Δ_f I` at K=0. Since the harmonic lift of the constant root value is the constant fine scalar,

`Δ_int⁻¹ b* = −1_int`, so `b Δ_int⁻² b*=r`.

For a slow gauge scalar η, write its high scalar adjustment as ξ and put y=Δ_intξ. To leading order the gauge fixing energy is

`‖y‖² + |u b Δ_int⁻¹y + a |K|²η|²`.

The vector `h=Δ_int⁻¹b*` has squared norm r. Minimizing y gives

`y_min=−u a |K|²η h/(1+u²r)`

and the effective energy

`a²/(1+u²r) · |K|⁴|η|²`.

Therefore the chosen path has coefficient exactly one. A straight interpolation u=1−t, v=t would not: for ℓ=3 and t=½ its coefficient is 25/21. This is a preserved failure of the naive interpolation, not a physical obstruction.

### 4.2 The differentiated fixing on the low Schur embedding

At fixed fluctuation, not differentiating y_min inside dotF, the leading root component of dotF on this minimizing low gauge field is

`[dot a − dot u ·u r a/(1+u²r)] |K|²η`.

It vanishes identically because `a²=1+u²r`. A transverse low mode has no degree-one divergence in the first place. High physical transverse aliases do not change this computation: their coupling to the low fixing starts at order |K|², so their minimizing amplitude has that order. Thus, if E_t denotes the exact analytic massive-band Schur embedding of the four low one-form modes,

`dotF_t E_t = J k_t`, with `k_t(K)=O(|K|²)` at the free point.   (V3)

The internal high gradient correction is essential for V3. Comparing only the raw constant fine mode with the coarse fixing would miss it.

## 5. Local vertex grouping and its Ward obligation

A background-covariant local frame can be built cellwise: parallel transport a fixed orthonormal scalar basis from the coarse root to each fine site, using the normalized constant vector as its first column, and tensor with the four link directions. Every transport is orthogonal in the adjoint representation. The full frame has determinant modulus one at every background. Its derivatives must remain in the transformed operator; they are local, not absent.

In this frame the high block of Q_t is massive at the trivial point. Its Schur inverse and the exact embedding E_t have fixed-depth local Taylor kernels. Put `q_t=E_t*Q_tE_t` after Schur elimination, and use the exact inverse decomposition into its low Schur inverse and the high inverse. Since dotF_t has only root output, harmonic scalar elimination gives

```
B_t⁻¹dotF_t=L b_t⁻¹ dotf_t,
dotF_t=J dotf_t.
```

V2 consequently splits into two types of traces:

```
−Tr[b_t⁻¹ k_t q_t⁻¹ e_t(E_W)],
−Tr[b_t⁻¹ h_t(E_W)],                                  (V4)
```

where `e_t(E)=E_t*T_E L` and h_t is the corresponding high-block expression. Both are local at fixed depth and linear in E; the second trace has only one massless scalar propagator. The first has two simple propagators, and its k_t has the free double zero V3.

The needed vertex conclusion is stronger than the free double zero: after composing with the local tree section, k_t's **first background vertex** must be O(|K|+|P|). The proof in §6 uses analyticity plus the background Ward identity. The low/root frames transform under the coarse root gauge group, so the analytic vertex obeys a difference identity whose right side is `k_t(K+P)−k_t(K)`. With k_t=O(K²), its constant background vertex would have zero contraction with every P; hence it must vanish. This argument includes the derivatives of E_t and of the local tree section. Those derivatives are present in the definition of k_t; they are not to be discarded in an implementation.

With the Ward step stated in §6, the mixed E/background traces have the following separate pole ledger before integration:

* Differentiating k_t gives two simple propagators and a degree-one numerator: bounded by a sum of `1/(|K| |K+P|²)` and `1/(|K|² |K+P|)`.
* Differentiating q_t⁻¹ gives three propagators. The free k_t supplies two powers on its adjacent momentum, cancelling that adjacent extra pole; the q_t background vertex supplies one more momentum. The same (1,2) and (2,1) bounds result.
* Differentiating b_t⁻¹ similarly uses k_t's two adjacent powers and the scalar background vertex's degree-one numerator, again yielding (1,2) and (2,1).
* Differentiating e_t or a local frame gives at most a single effective |K|⁻² singularity after k_t's cancellation. The high trace has at most a scalar bubble with one numerator power, or a single simple pole.

Each listed centre exponent is <4 and the worst total exponent is 3, strictly below dimension four. These are continuity bounds, not a conclusion from total degree alone. At fixed external P the regulator must still be common to the whole ratio, and volume must be taken before P→0 in the source's order.

The remaining residual difference `R(U,V)−R(U,𝔪(U))` is a local-matrix determinant difference with the harmonic representation's simple free poles. Section 7 applies the Ward lemma to its mixed U/ρ kernel; its ρ/ρ bubble is at worst (2,2), giving logarithmic growth, while its tadpole has one simple pole. With each external ρ_1=O(P²), the latter contributes O(P² log(1/|P|)) after division by the Wilson P² coefficient and vanishes. The complete operator list and the actual covariance check are given in §§6–7; locality alone is not used to infer that vertex property.

Sections 6–8 give the Ward argument and the stated antiperiodic root-sector limit for review. The full-colour periodic comparison remains separate, as specified in §8.

## 6. Actual background-vertex Ward lemma

The following supplies the previously isolated vertex decision within the stated root-sector calculation. It uses the actual local operators, not a replacement soft-distance Hessian.

**Analytic Ward lemma.** Let A be the coarse background connection, with any fine background obtained from the local tree section of §1. Let K(A) be an exponentially local operator between fields transforming in fixed adjoint root frames. Suppose its free Bloch symbol satisfies `K_0(k)=O(|k|²)`. Its first background vertex is analytic in the incoming and external momenta. Background covariance gives, for a Cartan gauge parameter and a charged root pair,

`Σ_μ d_μ(p) K^(1)_μ(k+p,k) = R(λ)K_0(k)−K_0(k+p)R(λ)`,

with the appropriate representation factors on the two sides; the free operator is colour scalar on that pair. Set k=0 and p=t e_ν. The right side is O(t²). The coefficient of t on the left is therefore zero for every ν. Hence

`K^(1)_μ(0,0)=0`, and `‖K^(1)(k+p,k)‖≤C(|k|+|k+p|)` locally.     (V5)

The same argument applies to rectangular k_t. There is no inference that its derivative vanishes merely because its free value vanishes: the analytic Ward identity is the missing premise and has been used explicitly.

Here the covariance premise is available for the actual blocks. In right link charts the field frame transforms at the endpoint appropriate to that chart. Parallel-transport each fixed cell basis from the coarse root to that endpoint. This gives a local orthonormal frame with determinant modulus one. The background-dependent high inverse, Schur embedding E_t, k_t, b_t, and q_t all transform in the corresponding coarse-root frames. Their background derivatives include those of every transport and every projector. The actual M obeys `M D_f=D_c ev`, and the actual 𝒞, normalized Ψ Hessians and Wilson Hessian are covariant in the same charts. Composing with the locally fixed tree section only introduces an internal gauge transformation, which these root-frame operators eliminate by covariance. Thus V5 applies to k_t because of V3, and to b_t and q_t because their free zeros are quadratic. It also applies to every massless low block of the local determinants in R at ρ=0.

A global cell frame can be used for the massive elimination: at K=0 its low columns are the four normalized constant one-forms; its other columns span the high subspace. For every t the high compression is positive at K=0. Away from K=0 the full Q_t is positive because `H_Wa=0` makes a a gradient and `F_tD_f` is invertible. Compactness of t∈[0,1] and of the Brillouin cell gives a uniform-in-t, fixed-depth high gap. Its inverse and the derivatives used here are therefore exponentially local. The analytic fine alias frame used to compute V3 differs from this fixed-cell frame by an analytic O(K) change; the actual low Schur embedding absorbs that change. The coefficient of order one in k_t is unchanged. This accounts for the moving-frame terms rather than differentiating an alias basis as constant.

## 7. Complete groups in the auxiliary off-shell decomposition

Write `R_0(U)=R(U,𝔪(U))` and `R_ρ(U,ρ)=R(U,𝔪(U)e^ρ)−R_0(U)`. At the actual h=1 saddle,

`Δ_n(V)=R_0(U*(V))+R_ρ(U*(V),ρ*(V))`.                 (V6)

The equality is used only on that saddle. Off the saddle, R is the auxiliary RHS defined in §2.

### 7.1 R_ρ: four actual local determinants

At fixed U, the only ρ-dependent terms in A5 are

`½log det L_harm −log det Δ_c +½log det G_c −½log det H_h`.       (V7)

Here H_loc inside L_harm is the actual unminimized Ψ Hessian, with all its third and fourth tree derivatives; H_h is the actual h Hessian. There is no omitted internal h propagator: its determinant has remained explicitly in V7 after the exact shear. The other four determinants in A5 depend only on U and cancel from R_ρ.

For each operator O in V7, its complete mixed second derivative is

`D_A D_ρ log det O = Tr(G O_Aρ)−Tr(G O_A G O_ρ)`.

Its complete repeated residual derivative is

`D_ρ² log det O = Tr(G O_ρρ)−Tr(G O_ρ G O_ρ)`.

Multiply by the displayed weight in V7. Equivalently, in an expansion `O=O_0+εO_1+ε²O_2`, the coefficient is `Tr(G O_2)−½Tr(G O_1 G O_1)`. Thus the relative ½ bubble coefficient is preserved. These tadpole and bubble groups are the full second derivative, not selected diagrams.

Eliminate every massive high block analytically before assigning pole powers, retaining its log determinant. For each remaining low block the propagator is bounded by C/|k|², its A vertex obeys V5, and its ρ and Aρ vertices are bounded analytic kernels. Consequently each Aρ bubble has separate powers (1,2) or (2,1); each tadpole has (2,0). The high-block determinant is analytic. Each ρρ bubble has at worst (2,2), and each ρρ tadpole has (2,0). No claim that a quadratic background amplitude by itself improves a pole is made: the two explicit external ρ_1 factors are used only after this ledger.

### 7.2 R_0: the normalized Nielsen groups

V1–V4 express R_0 as an equation-of-motion pairing. All terms come from the two traces in V4. Differentiating the first trace once in the background gives exactly four groups: differentiation of b_t⁻¹, k_t, q_t⁻¹, or e_t. Differentiating the second gives exactly two groups: differentiation of b_t⁻¹ or h_t. The already retained high-block inverse, the frame derivatives and the derivative of T_E's local endpoint factors lie in e_t and h_t; they are not additional unlisted massless lines.

V3 and V5 give the separate bounds listed in §5: every mixed E/background group is a sum of (1,2), (2,1), or (2,0) kernels. In particular, when b_t⁻¹ or q_t⁻¹ is differentiated, the free k_t is evaluated at the momentum adjacent to the duplicated propagator and supplies exactly the two powers needed there. The estimate is not based only on total degree and does not assume those powers can be transferred from one singular centre to another.

Let c_E(U) be the covariant coefficient of E_W in the integrated Nielsen trace. The actual saddle equation before h minimization gives

`E_W(U*)=−Ψ_U(U*,V)`,

and, to first order, `E_W,1=M*𝒞⁻¹ρ_1`, since `Ψ_U=−M*𝒞⁻¹ρ+O(ρ²)`. Both maps are local in this unminimized representation. The zero-background coefficient c_E(1) vanishes: the Wilson gauge-row insertion is a commutator, and the free matrices are colour scalar on a paired real root plane, so its colour trace is zero. Thus D²R_0 along the saddle is precisely the mixed derivative of c_E paired with E_W,1. There is no surviving term from E_W's second derivative multiplied by a nonzero c_E(1).

For the same reason the one-point residual coefficient of V7 vanishes on a paired root plane. More explicitly, the actual action is built from real traces of unitary words and their normalized analytic minima. For anti-Hermitian X,Y,Z,

`Re tr(XYZ)=½Re tr(X[Y,Z])`.

Thus its cubic colour tensor is a commutator tensor; eliminating intermediate fields at cubic order contracts it only with colour-scalar quadratic inverses. First derivatives of M, 𝒞, the frame and the square-root profile have the same commutator colour structure. Their free paired-root colour traces vanish. This is why second derivatives of the external tree/residual maps do not introduce a missing one-point term. The normalized φ action is used here; no unmatched k̃ normalization is imported.

### 7.3 Ward pairing after the integral

On the charged pair, the external Cartan gauge transformations preserve the antiperiodic quantum boundary condition. The coefficient of the coarse residual transforms covariantly, and the local tree section sends a coarse pure gauge into a fine pure gauge with the same root value. Its first response Y therefore obeys `Y(p)d_c(p)=0`. The mixed Nielsen coefficient, after the local map `M*𝒞⁻¹` is paired with ρ_1, obeys the same identity. Once continuity at p=0 is justified, dividing this Ward identity by |p| along every direction gives Y(0)=0. This is the precise use of covariance; covariance without continuity would not suffice.

## 8. The stated antiperiodic root-sector limit and its exact scope

UIR2_55 §1 explicitly fixes the root sector, a regulated antiperiodic torus, and then per-site densities. Use that same paired real root plane, the same antiperiodic twist for every fine/coarse/ghost operator in V6–V7, and periodic external Cartan momenta. Do not replace it by a pin at a global site. Take volume to infinity at fixed nonzero external p before taking p→0.

At fixed depth all local-jet constants above are uniform in the number of cells. The antiperiodic momentum mesh stays a distance comparable to T⁻¹ from each singular centre; adding a periodic external momentum preserves that mesh. For 0≤s<4, counting sites in dyadic annuli gives

`T⁻⁴ Σ_{0<|k|<r}|k|⁻s ≤ C_s r^(4−s)`

with constants uniform in T (and the analogous bound around k=−p). Each mixed group is bounded by a sum of |k|⁻³, |k+p|⁻³, |k|⁻² and their bounded complements, using the separate powers in §7. These estimates give uniform integrability. Away from the two centres the analytic symbols converge normally, so the per-site sums converge to the common Brillouin-zone integrals; the same bounds give continuity as p→0. The constants are uniform in the compact gauge-path parameter t, which permits integration over t after taking the limit.

For a ρρ bubble, the separate (2,2) powers are integrable at fixed nonzero p. Splitting into balls of radius |p| around the two centres and dyadic outer annuli gives `C(1+|log |p||)`. Each actual external residual is `ρ_1(p)=𝒞_n(p) H_n(p)v=O(|p|²)` at fixed depth. Dividing their product by the Wilson |p|² normalization therefore leaves `O(|p|²(1+|log |p||))→0`. A tadpole is better. No reversal of the two limits is used.

**Candidate root-sector conclusion for independent review.** Combining V6–V7, the normalized Nielsen path, V5 and this common antiperiodic limit yields zero residual F² coefficient for each paired charged root sector, at every fixed n. The constants may depend on n; the limiting value zero does not. This is an author derivation awaiting independent review, not an audit/status promotion.

**Boundary of that conclusion.** This calculation does not by itself identify the antiperiodic root-sector result with an unspecified full-colour periodic determinant or with a nontrivial clock/shift flux sector. The neutral Cartan modes have a separate periodic zero-mode prescription; their mixed cubic vertex vanishes by the commuting real-trace symmetry, and their remaining local tadpoles have simple-pole bounds, but a complete finite determinant/Gram treatment of that prescription has not been supplied in this note. A fixed Fourier zero-mode omission could be compared after grouping at fixed nonzero p; it is not silently substituted for the source's prescription. Therefore the full-colour, original-periodic statement of Ρ_n, if it requires that additional identification beyond UIR2_55's explicitly stated root-sector convention, remains a named open bridge. No physical Hamiltonian mass gap, interacting continuum measure, OS axiom, or full Yang–Mills theorem follows from this one-loop calculation.

## 9. Exact controls and status

`residual_det_04.criteria.md` was written before the script. The first run of `residual_det_04.py` passed 13/13 exact checks. It uses the full 80-dimensional high-gradient quadratic form on the actual 3⁴ scalar cell, verifies the **partial** dotF cancellation while the high minimizer is held fixed, retains the naive interpolation's 25/21 counter-control, and independently differentiates finite off-shell determinant ratios. Dropping the off-shell Wilson row gives the wrong derivative 1/4 in that control. The controls verify the stated algebra, not the analytic Ward or regulator proof by themselves.

The exact remaining decision is independent review of the covariance/Schur-embedding Ward argument V5 and the complete grouping V6–V7 on the stated root-sector domain, followed by the neutral/full-periodic domain comparison if required by the consumer. All auxiliary gaps used to obtain locality are fixed-depth operator gaps and are not a physical mass gap.


Frozen for independent review UTC: 2026-10-29T14:16:38.228208+00:00

This checkpoint is an author proposal with explicit domain limits. It does not apply an audit verdict or promote any shared science status. Further changes will be separate unless the coordinator requests a reviewed repair.
