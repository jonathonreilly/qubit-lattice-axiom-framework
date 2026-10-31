# Actual-action harmonic gauge shear: finite and free-symbol checkpoint

This is a separate frozen checkpoint after the original §§1–4 model unit. It records the actual finite-regulator gauge shear, the failed point-lift pole inference, the harmonic repair, and the actual free principal symbol. It awaits independent review; the off-shell residual bound and full proof remain open. No shared source or git state is changed.

## Pre-stated test and domains

Target: undo h elimination in the **actual** normalized Ψ(U;V^h), without changing its S4′ or intermediate-level vertices. Use a point-supported lift of coarse gauge parameters to fine block roots and keep its determinant. The exact identities are finite-dimensional identities on one specified invertible gauge stratum. A calculation on a full gauge space with a singular Laplacian is not an identity on a mean-zero quotient by default.

The clean domain for the local lift calculation is a charged root sector at a Cartan background, with compatible nontrivial Cartan holonomy twists on the fine and coarse tori. For example SU(2) has Ω=diag(i,−i), acting as −1 on each charged root; use the same twist around corresponding fine and coarse cycles. Gauge parameters in that root sector obey the twist, the covariant difference is injective near the trivial connection, and all determinants in the identity are ordinary determinants on those spaces. Use the real two-dimensional charged root plane when counting determinants; complex notation must retain the conjugate root multiplicity. This is a legitimate common sector regulator; it does not establish the neutral sector or any change of thermodynamic limit.

For periodic untwisted parameters the mean-zero prescription is a different domain. A global mean-zero projection makes the root lift's projector nonlocal, as shown below. The local 72I calculation must not be silently applied to that pseudodeterminant quotient. A root-fixed gauge also changes the background gauge stratum/translation boundary and is not substituted here for the source's full gauge quotient.

The derivative in the displayed 72I identity is the **unscaled unit fine-lattice difference**. If D_f is multiplied by a_f^(-1), Δ_f is multiplied by a_f^(-2), and G_J by a_f^(-4).

Criteria: prove the augmented null columns from actual fine/h stationarity and covariance; obtain the complete determinant by a triangular shear; verify the exact range-two lattice Gram matrix; preserve the failure of locality under a global mean-zero projection. These results are not a proof that the remaining local Schur operator matches the Wilson principal symbol.

## 1. Exact actual-action identity

Let Q(U,V,h)=S_W(U)+Ψ(U;V^h), evaluated at the fine/h saddle `(W*(V),V,1)`. Let H_loc be the (U,V) Hessian of Q with h held equal to 1, and H_h=Q_hh. Its entries are the actual unminimized composite soft-action entries, including BCH and the S4′ map; no μ-distance approximation occurs.

Let `ev` restrict a fine gauge parameter to the coarse roots. Let J inject a coarse gauge parameter at exactly those roots and set it to zero elsewhere; `ev J=I`. Choose the sign of the h chart so that the combined fine gauge orbit has tangent `(D_f λ,0,−ev λ)`. The action is invariant along that orbit, and its derivatives in U and h vanish at the saddle. Thus its **ungaugefixed** full Hessian annihilates `(D_f J,0,−I)` exactly. The coarse gradient need not vanish, since this gauge action keeps V fixed.

Add the same fine and coarse gauge-fixing forms as in Φ, respectively `D_fD_f*` and `D_cD_c*`. Make the triangular change

`a=a′+D_f Jη`, `w=w′`, `h=−η`.

It has determinant modulus one. The η block and the a′–η block are

`G_J=J*Δ_f²J`, `D_fΔ_fJ`, where `Δ_f=D_f*D_f`.

Eliminating η therefore produces the actual local block

```
L_J = H_loc + diag(D_f Q_J D_f*, D_cD_c*),
Q_J = I−Δ_f J G_J⁻¹J*Δ_f,
```

and, denoting the h-minimized joint Hessian by J_min,

`det J_min = det G_J · det L_J / det H_h`.             (A1)

This is Schur elimination in two orders on the same finite matrix. The changing J-gauge shear has unit determinant at **every** background, so there is no unrecorded shear Jacobian; its derivatives remain inside the displayed operators. The actual finite Φ is consequently

`Φ = ½log det L_J −½log det W +½log det G_J −½log det H_h + LG −½log det Δ_c`.  (A2)

Equivalently, with `G_c=D_c*𝒞(U)⁻¹D_c`, the exact level-group identity gives

`Φ = ½log det L_J −½log det W +½log det G_J +½log det 𝒞(U) −log det Δ_c +½log det G_c −½log det H_h`.  (A3)

All factors use the specified common domains; no determinant is replaced by an inconsistent pseudodeterminant. H_loc, H_h, G_c and 𝒞 have fixed-depth local Taylor kernels before h minimization, by the fixed-endpoint locality argument in the frozen note. Q_J is local on the twisted full parameter space by the next section.

## 2. Range-two Gram matrix and the mean-zero exception

On a four-dimensional unit fine lattice, for covariant nearest-neighbour differences with unitary adjoint transports, Δ_f has diagonal 8I and eight off-diagonal unitary entries with minus signs. Its squared diagonal is therefore `(8²+8)I=72I`; Δ_f² has graph range two. Fine roots in J are separated by ℓ=L^n≥3. If the fine torus periods are at least 3ℓ (so no short wrapping collision), distinct roots cannot be joined by a path of length at most two. Hence

`J*Δ_f²J = 72 I`                                     (A4)

on the full charged root parameter space, with the twist included in every boundary transport. Unit-modulus boundary phases cancel in the two-step return products. The same reasoning works for matrix adjoint transports. For a derivative scaled by inverse spacing the right side is `72 a_f⁻⁴ I`.

Thus Q_J has finite range at this regulator: each column Δ_fJ is supported within one fine step of its root. The nontrivial twist removes the constant gauge kernel without any spatial mean projector. At the trivial connection injectivity follows directly: D_fλ=0 forces λ to be parallel constant; transport around a twisted cycle multiplies it by −1 in the SU(2) charged example, hence λ=0. Invertibility persists in a finite-regulator neighborhood.

For comparison, on a periodic torus put `Π_c=I−11*/N_c` and use J on coarse mean-zero parameters. The inverse of G_J on that subspace is Π_c/72, so

`Q_mean − Q_full = (Δ_fJ1)(Δ_fJ1)* /(72N_c)`.

At two arbitrarily separated coarse-root sites, `(Δ_fJ1)_x=8`; the corresponding matrix entry is `64/(72N_c)`, not zero. Therefore this prescription is a finite-rank **nonlocal** correction. Its per-volume effect cannot be discarded from a differentiated determinant without an estimate in the prescribed order of limits. That estimate has not been given here. This explicitly preserves the zero-mode limitation rather than hiding it in det′ notation.

## 3. Next actual calculation

At the trivial field, eliminating the massive coarse one-form block of L_J gives

`O_J,0 = H_W,0 + D_fQ_JD_f* + M*D_c(1+D_c*𝒞D_c)⁻¹D_c*M`.

This follows from Woodbury using `Ψ_UU=M*𝒞⁻¹M`, `Ψ_UV=−M*𝒞⁻¹`, `Ψ_VV=𝒞⁻¹`. It is a local fine-field operator at fixed n, but its residual gauge modes mix fine aliases. Its main-alias gauge profile cannot be read by discarding the high aliases: the root lift itself contains those aliases. The next exact step is the low/high-alias Schur complement of this O_J,0 together with the first and second background derivatives of A3, including the H_h and G_c scalar factors. This is the concrete remaining calculation; no bound on actual Ρ_n is asserted.

Working checkpoint UTC: 2026-10-29T12:47:24.420289+00:00


## 4. Preserved failed inference: the point-lift operator has a quartic sector

The inference “Q_J is local, so O_J,0 has only simple massless poles” is false. This is a failure of that proposed route, not a failure of grouped cancellation in Φ.

For a coarse scalar η put a=D_f Jη. Exact covariance gives `M D_f=D_c ev`, while `Q_J Δ_f J=0` and `H_W,0 D_f=0`. Consequently

`〈a,O_J,0 a〉=〈η,Δ_c(1+D_c*𝒞D_c)⁻¹Δ_cη〉`.

For the unit fine difference, `‖D_fJη‖²=〈η,J*Δ_fJη〉=8‖η‖²`, since distinct roots are separated by at least three fine steps. For a coarse Fourier mode of momentum K, the Rayleigh quotient is therefore `λ_c(K)²/[8(1+g_n(K))]`, with `λ_c(K)=O(|K|²)` and `g_n(K)=D_c(K)*𝒞_n(K)D_c(K)=O(|K|²)` at fixed depth. It is O(|K|⁴). Positivity and the inverse Cauchy–Schwarz inequality then force an inverse quadratic form of order at least |K|⁻⁴ along these vectors.

The point lift injects high fine aliases whose norm remains nonzero at K=0. Its residual coarse gauge cost contains two coarse Laplacians. Thus no volume-uniform lower bound `O_J,0(K)≥c_n|K|²` can hold on this representation. The factors in A3 must be regrouped before transferring the solved model's pole table. No term with this quartic pole is declared harmless by locality or by its quadratic background-amplitude order.

## 5. Harmonic lift: exact finite identity and a local residual fixing

This section tests the coordinator's alternative lift. Keep the same finite invertible gauge stratum as above. Let I inject fine scalar values at all non-root sites, so that `II*+JJ*=I_f`; define

```
Δ_int=I*Δ_f I,
L=J−I Δ_int⁻¹ I*Δ_f J,
S=J*Δ_fJ−J*Δ_f I Δ_int⁻¹ I*Δ_fJ.
```

The symbol L here denotes the harmonic lift, not the odd blocking factor used in ℓ=L^n. Δ_int is positive even on the full periodic space: a vector vanishing at each root and having zero covariant difference vanishes everywhere on the connected lattice. On the current injective Δ_f stratum, S is positive as well. Direct block multiplication yields

`ev L=I`, `I*Δ_fL=0`, `Δ_f L=J S`, `L*Δ_fL=S`, and `L*Δ_f²L=S²`.

There is no replacement of a singular inverse by a pseudoinverse in these equations. Therefore the same actual-action shear, with this L in place of J, gives

```
Q_L=I−Δ_f L (L*Δ_f²L)⁻¹L*Δ_f=I−JJ*=P_int,
L_harm=H_loc+diag(D_f P_int D_f*,D_cD_c*),
det J_min=det(S²) det L_harm / det H_h.
```

The final operator L_harm is local at fixed depth, despite the inverse used to construct L. The shear has determinant modulus one pointwise in the background; differentiating the final equality therefore retains all moving-lift terms inside S and L_harm without an additional Jacobian. The block determinant identity also gives

`det Δ_f=det Δ_int det S`.

Substituting into the same Φ, with no change to H_h or the level normalization, yields the actual finite identity

```
Φ=½log det L_harm−½log det W
  +log det Δ_f−log det Δ_int−½log det H_h
  +LG−½log det Δ_c.                                  (A5)
```

Equivalently, the final line is `+½log det 𝒞−log det Δ_c+½log det G_c−½log det H_h` together with `+log det Δ_f−log det Δ_int`. These are identities of the same finite regulated determinants, not a statement that their background derivatives already cancel. Δ_int carries the background dependence of the harmonic lift, and its determinant cannot be dropped as a constant.

For the free operator after the massive coarse one-form block is eliminated,

`O_harm,0=H_W,0+D_fP_intD_f*+M*D_c(1+D_c*𝒞D_c)⁻¹D_c*M`.

The special gauge vectors now have `a=D_f Lη`, norm `〈η,Sη〉`, and the same coarse energy `〈η,Δ_c(1+D_c*𝒞D_c)⁻¹Δ_cη〉`. The scalar S has a quadratic low-momentum zero, so this particular quotient is now of order |K|². This observation alone is not yet a lower bound on every mode of O_harm,0; that bound and the determinant's derivative grouping are the next checks.

The periodic mean-zero problem has not disappeared. For a connected untwisted free lattice S has the constant kernel. Restricting to a fixed mean-zero coarse subspace in the formula for Q_L produces `I−JΠ_cJ*`, leaving a rank-one root-supported correction, and can also conflict with the fine mean-zero domain of L. A complete periodic quotient identity needs a compatible harmonic-coordinate decomposition and its Gram factors. A5 is currently asserted only on the explicitly injective common stratum above.


## 6. Dirichlet gap, complete alias scalar symbol, and the free Gram cancellation

### 6.1 A fixed-depth gap uniform in the number of blocks

Partition the fine vertices into cells of side ℓ rooted at their distinguished coarse vertex. Join each vertex to its root by a coordinate path inside its cell of length at most `m=4(ℓ−1)`. For a scalar f vanishing at every root, telescope along the path using the unitary adjoint edge transports. Cauchy–Schwarz gives `|f(x)|²≤m Σ_path|D_f f|²`. Each edge is used by at most ℓ⁴ such paths. Hence

`‖f‖²≤4(ℓ−1)ℓ⁴‖D_f f‖²`,

and `Δ_int≥[4(ℓ−1)ℓ⁴]⁻¹ I` for the unit fine difference, uniformly in volume and in unitary background transports. This deliberately nonoptimal bound depends on depth; it is not a uniform-in-n claim. Also `‖Δ_int‖≤16`. The convergent series `Δ_int⁻¹=(1/16)Σ_{r≥0}(I−Δ_int/16)^r`, together with finite propagation of each power, gives an exponential off-diagonal bound with constants depending only on ℓ. Fixed finitely many background derivatives of the inverse are products of this inverse and local differentiated Laplacians, and retain fixed-depth exponential bounds. Thus L and S have fixed-depth exponentially local Taylor kernels without a massless scalar inverse hidden in their definitions.

### 6.2 All aliases, including their normalization

At the trivial field use a coarse Bloch momentum K and a fine cell of ℓ⁴ sites. The normalized fine scalar alias basis has momenta `q_r=(K+2πr)/ℓ`, one representative r in each class modulo ℓ. The root injection has coefficient ℓ⁻² in every alias. For `λ_f(q)=Σ_μ4sin²(q_μ/2)`, the scalar Schur complement satisfies the exact identity

`S(K)⁻¹=J*Δ_f(K)⁻¹J=ℓ⁻⁴ Σ_r λ_f(q_r)⁻¹`.

For K near zero the r=0 summand is `1/(ℓ²|K|²)+O(1)` and the remaining finite alias sum is analytic and bounded at fixed ℓ. Therefore

`S(K)=ℓ²|K|²+O(|K|⁴)`.

The O(|K|⁴) remainder uses the even hypercubic scalar symbol; only fixed depth is claimed. In particular `‖D_f Lη‖²=〈η,Sη〉` has quadratic, rather than constant, size on a slow root mode. The root Dirichlet determinant supplies exactly the extra scalar factor in `det Δ_f=det Δ_int det S`; no alias has been dropped to obtain this normalization.

### 6.3 Exact free Hodge factorization

Keep an invertible finite Bloch sector and let T be an orthonormal transverse frame for the fine one-forms. Write each fine one-form uniquely as

`a=T t+D_f(I ξ+Lη)`.

Here `(I,L)` is a triangular change of scalar coordinates of determinant modulus one, because `J*L=I` and `J*I=0`. The Gram determinant of the **one-form** map `(t,ξ,η)↦a` is `det Δ_f`, not one. This is where discarding a gauge-coordinate Jacobian would give a wrong determinant.

Let `R_c=(I+D_c*𝒞D_c)⁻¹`. At the free background, using `H_W D_f=0`, `M D_f=D_c ev`, and `I*Δ_fL=0`, the exact form of O_harm,0 is

```
〈a,O_harm,0 a〉
 =〈t,H_T t〉+‖Δ_int ξ‖²
  +〈D_c*M Tt+Δ_cη,R_c(D_c*M Tt+Δ_cη)〉.
```

There is no ξ in the last term. The triangular replacement `η↦η+Δ_c⁻¹D_c*M Tt` has determinant one on the specified invertible sector; it is used here only to evaluate this finite determinant, not to declare its inverse local or to freeze a moving basis. It follows that

`det O_harm,0=det H_T ·(det Δ_int)²·(det Δ_c)²·det R_c /det Δ_f`.

The eliminated coarse one-form block is `𝒞⁻¹+D_cD_c*` and has determinant `det(𝒞)⁻¹det(R_c)⁻¹`. Thus

`det L_harm,0=det H_T ·(det Δ_int)²·(det Δ_c)² /[det Δ_f det 𝒞]`.   (A6)

At the same free background `det W=det H_T det Δ_f` and `H_h=G_c`. Inserting these expressions into A5 and the exact LG identity cancels every factor and gives Φ(1,0)=0. This checks the ghost/Gram ledger at the base point; it does **not** differentiate A6 as if H_WD_f=0 held at an arbitrary off-shell background. The off-shell Wilson gauge-row defect is still required in the second derivative.

### 6.4 A genuine simple-pole bound for the repaired free operator

The same form proves more than the special-vector quotient. At fixed ℓ, for 0<|K|≪1, let `E=〈a,O_harm,0(K)a〉`. On the transverse space the free Wilson curl Hessian gives `‖t‖²≤C_ℓ |K|⁻² E`. The Dirichlet gap controls `‖D_f Iξ‖²≤C_ℓ E`. Since `S(K)≤C_ℓ|K|²`, `Δ_c(K)≥c|K|²`, the actual fixed-depth M(K) is bounded, and R_c(K) is uniformly positive near K=0,

```
‖D_fLη‖² ≤ C_ℓ |K|² |η|²
 ≤ C_ℓ |K|⁻² |Δ_cη|²
 ≤ C_ℓ |K|⁻² |D_c*M a|² + C_ℓ‖t‖²
 ≤ C_{n,κ}|K|⁻² E.
```

In the middle line use `D_c*M a=D_c*M Tt+Δ_cη` and `‖D_c(K)‖≤C|K|`; the ξ term vanishes by exact covariance. Consequently

`O_harm,0(K)≥c_{n,κ}|K|² I`.

The constants may depend on fixed depth, κ, and the exact S4′ map. This proof uses the actual free M only through its already exact covariance and fixed-depth boundedness. At K=0 the kernel consists of the four constant fine one-form modes: zero Wilson energy makes a a gradient plus a constant, the interior fixing makes its gradient harmonic with the prescribed root value, and at zero Bloch momentum that harmonic scalar is constant. The remaining finite-cell eigenvalues therefore have a positive gap. The original coarse block is massive as well. Hence L_harm,0 has precisely four low one-form modes per colour and no extra quartic branch. This is a free propagator statement; differentiating its background-dependent low-mode projector has not yet been eliminated or bounded.

### 6.5 Exact next decision

The harmonic representation repairs the free pole obstruction and preserves the finite determinant normalization. The outstanding principal-symbol decision is now sharply defined: differentiate A5 using the **actual** H_loc, H_h and level kernels; include the derivatives of Δ_int and the low-mode Schur projector; compare the resulting linear-residual and quadratic-residual vertices with their local degree-one and degree-zero model counterparts. A product of two simple propagators is not automatically harmless if a vertex or an external projection introduces additional inverse momentum factors. The off-shell Wilson completion and the common periodic zero-mode/volume limit are still outstanding. No actual Ρ_n bound follows from A5–A6 and the free coercivity alone.


## 7. The actual free low-band principal matrix, with the high-band minimization retained

This refines §6.4 and verifies the normalization suggested by the coordinator. It applies to the free Wilson quadratic form in the unit fine-lattice convention and the actual S4′ composite M. Choose the analytic fine Fourier alias frame at coarse momentum K. The low embedding E(K) consists of the four main-alias one-forms, each of norm one per fine cell. At K=0 their link value is ℓ⁻². Since the actual constant-field root map sums a length-ℓ link, `M(0)E(0)=ℓ⁻¹I`. The high band is every other fine alias.

The high block of O_harm,0 is strictly positive at K=0 by §6.4; its Schur inverse is therefore analytic near zero. The mixed high/low block vanishes at K=0. For fixed low amplitude v, the minimizing high field is consequently O(|K||v|). In this moving Fourier frame the Wilson curl Hessian is **exactly diagonal in aliases**, so its low contribution is

`ℓ⁻²〈v,(|K|²I−KK*)v〉+O(|K|³|v|²)`.

The high Wilson energy is nonnegative and has no cross term with this expression. Since the minimizing high field is O(|K|), its contribution inside `D_c*M a` is O(|K|²). Also `R_c=I+O(|K|²)`. Therefore the leading coarse gauge energy, for any such high field, is

`ℓ⁻²|K*v|²+O(|K|³|v|²)`.

It remains to check that the interior fixing and high Wilson energy need not add another term of order |K|². Use a high-alias **pure gradient** `a_H=D_f φ_H` to cancel the interior divergence. The linear map

`φ_H ↦ I*Δ_f(K)φ_H`

from high scalar aliases to the interior scalar coordinates is square and invertible at K=0: if its value is zero, Δ_fφ_H is supported only at the root; its sum over the cell is zero, so it is zero; the high scalar φ_H is then zero. Its inverse is analytic near zero. Thus solve

`I*Δ_f(K)φ_H=−I*D_f(K)*E(K)v`.

The right side is O(|K||v|), so φ_H and a_H are O(|K||v|). This choice makes the interior fixing exactly zero and adds exactly zero Wilson energy. It provides a matching upper bound for the previous lower bound. Hence the actual massive-band Schur matrix is

`O_low(K)=ℓ⁻²|K|²I_4+O(|K|³)`                         (A7)

per colour. This is an identity of the principal coefficient, derived with every high alias present. In coarse link units, v=ℓ w, and the coefficient becomes `|K|²I_4`, the Feynman principal symbol. The factors of ℓ agree with `M a=ℓ a` and `‖a‖_fine²=ℓ⁴|a|²` for an unnormalized constant fine link value a. No derivative of a background-dependent low-band frame has been set to zero: A7 is a calculation only of the **free** Bloch operator, and extending it to first and second background jets remains work.

The unit convention matters. The displayed comparison uses the unit fine difference and the corresponding Wilson quadratic form. Rescaling D_f alone without rescaling the action and interlevel fields is a different operator; the earlier `72a_f⁻⁴` Gram formula does not authorize that inconsistent substitution.

## 8. Exact controls recorded before implementation

`residual_det_03.criteria.md` was written before `residual_det_03.py`. The first run passed 27/27 exact checks with empty stderr. The implementation independently constructs the side-nine four-dimensional Laplacian's root columns (all 6,561 Gram entries), solves a complete 3⁴ rational Bloch Dirichlet system, compares its scalar root Green function against all aliases, and checks the finite Schur and scalar normalization identities on a changing rational gauge-compatible matrix family. The rational Bloch root Green value is `1047/7280`, so S=`7280/1047`; no numerical extrapolation is used.

The deliberate controls confirm that dropping Δ_int, replacing S² by S, or omitting the null-column premise gives a wrong determinant. The changing family has a nonconstant harmonic lift and a nonzero second derivative of log det Δ_int. These are algebra and free-geometry controls, not a numerical evaluation of the actual S4′ background vertices or a proof of the regulator interchange.

The full periodic prescription still needs attention after this checkpoint. Pinning one global site is not substituted for the chosen stratum: that pin can introduce a scalar eigenvalue of order inverse volume and a long-range constant term in the inverse. Its rank alone does not show that twice-differentiated normalized determinants have the same thermodynamic limit. Any continuation must either prove cancellation of those contributions in the full common ratio or give an estimate in the source's prescribed order of limits.


Checkpoint frozen UTC: 2026-10-29T13:17:21.815618+00:00

Further background-vertex work will use a separate residual_det_* artifact so these bytes remain reviewable. Status: conditional/support progress, with the exact domains and remaining conditions stated above; no scientific or audit status promotion.
