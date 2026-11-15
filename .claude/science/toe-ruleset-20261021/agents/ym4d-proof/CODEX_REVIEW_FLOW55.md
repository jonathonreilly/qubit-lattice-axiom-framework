## PRE-STATED

Independent hostile review of `FLOW55.md`, requested 2026-10-28 (local date). Reviewer: Codex, independent of the target's authorship. This is a mathematical review, not an audit-status promotion. Only this file may be written. No git commands. Large-file content is read by search and bounded `sed` ranges. Arithmetic checks will use exact integers, rationals, or symbolic expressions; no floating-point agreement will count as evidence.

Prior exposure before this block: the user's claims and priorities; `FLOW55.md` headings/search matches, lines 1–83 and 568–616 (including both errata and the author's status inventory); the repository science-workflow instructions and the initial review-loop skill instructions. I have not yet read the proofs in §§3–6 or the check implementations. No independent calculation has yet run. The author’s reported PASS results and upstream review labels are not independent evidence.

Pre-stated tests, in the requested order:

1. **K̄ / K̄-1L.** Check the gauge-action/covariance identity, the distinction between invariance and Hessian transversality at stationary versus arbitrary points, all Schur-complement terms, induced quotient measures, primes/zero modes, and determinant normalizations. Independently derive a finite-dimensional block identity and test any claimed cancellation with exact non-diagonal positive matrices. A missing field-dependent determinant, omitted residual-curvature term, or false off-shell Hessian inference refutes the corresponding statement; a missing analytic hypothesis yields NOT-VERIFIED.
2. **K̄-tad.** Reproduce the transported-covariance finite checks only after reading their scope; independently inspect the contraction and its linearization. Identify the exact imported Green-function bound and its source, dimension, zero-mode convention, volume uniformity, and weighted summability requirements. Check erratum 1's chain-rule limit and whether it suffices for the marginal coefficient. Pure-gauge cancellation alone does not prove vanishing on transverse low momentum.
3. **GH0 / UIR♮.** Follow the ghost determinant scaling and Taylor coefficient through the fine/level subtraction, including additive constants and volume/infrared limits. Re-derive the equivalence algebra only with its actual prerequisites. An unproved prerequisite is not repaired by naming the residual estimate.
4. **WARD-J / JET-MARG.** Derive the infinitesimal link-log gauge transformation through cubic order and the Taylor identities at orders 2–4. Independently classify the relevant hypercubic cubic tensor structures and their transverse subspace; distinguish that finite classification from locality/analyticity and the full marginal-jet theorem.
5. **W-loc and normalization.** Inspect FLOW's actual F-rem/F-flow/F-tune/F-ind hypotheses and proofs, plus the stated C1/C2 interfaces, using locating strings. Independently check the exact coefficient arithmetic, including `11 = 12 − 1`, `2N·2b_0`, and `1/22 : 21/22`.

Verdicts will be **CONFIRMED**, **NOT-VERIFIED**, or **REFUTED**, each attached to a file and locating string. CONFIRMED may apply to an explicitly stated conditional implication, but will not silently confirm its hypotheses. Any literature recollection will carry `[m]`; sourced imports will be distinguished from recollection. The final section will state exactly what may be banked and which route-level conclusions remain unsupported.

---

## Review result

The orbit-average idea survives the mathematical checks **at the stated formal one-loop, fixed-n coefficient level**, with an essential normalization qualification. The Schur complement, quotient Jacobian, transported tadpole cancellation, ghost scale subtraction, and Ward-jet argument are sound under the conditions detailed below. They do not prove the n-uniform estimate (UIR♮).

The strongest wording cannot be banked unchanged. For N ≥ 3, the exact normalized-kernel exponent must be the **φ-tower**, not FLOW's literally defined k̃-tower. An exact SU(3) S4′ example below refutes the cited zero-residual normalization for k̃. This distinction does not change the Taylor coefficients used for β. There are also two incorrect logical identifications in the prose: (F-1) with an unspecified positive slope is not equivalent to (UNIV-1L), and the scalar bound (UIR♮) does not imply the integrand bounds (R-a)/(R-b). The main conditional coefficient reduction survives those corrections.

All file names below are relative to this report's directory unless stated otherwise. Locating strings, rather than line numbers alone, identify the reviewed statements. Earlier reviewers' status labels were not treated as proofs.

## 1. K̄, the Schur complement, and the quotient

### 1.1 Exact averaging — CONFIRMED

**Source:** `FLOW55.md`, `Theorem K̄ (exact)`; `PROOF.md`, `Decision 4: the RG kernel`, especially `𝒩(hMh'^{-1}) = 𝒩(M)`; `LINEAR_PACKAGE.md`, `The averaging S4' and its linearisation`.

The restriction map from the fine product gauge group to the level-n sites is surjective. Extend a prescribed coarse gauge transformation by arbitrary values at the other fine sites. Haar changes of variables in the intermediate fields give the claimed composite covariance. Haar averaging in h then makes K̄ invariant separately in its two arguments. This argument uses the **actual normalized kernel**, and is unaffected by the φ/k̃ issue below. With normalized Haar measure, the displayed group-volume factor is simply one.

This proves invariance, not unrestricted off-shell Hessian transversality. If J_λ is the gauge vector field and f is invariant, differentiation gives

`Hess f(Y, J_λ) = −df(∂_Y J_λ)`

in a fixed chart, with the corresponding chart correction in right-exponential coordinates. The right side vanishes at a critical point. `FLOW55.md`, `and W* is a critical point`, supplies precisely the condition needed for **H♮D₀ = 0 at W*(V), for each admissible V**. It does not assert, and must not be paraphrased as asserting, that the fine Hessian vanishes on gauge tangents at every fine configuration. For example, the rotation-invariant function `(x²+y²)/2` has Hessian equal to the identity away from its critical point.

### 1.2 Every-background normalization — REFUTED under the literal cited k̃ convention

**Sources:** `FLOW55.md`, `FLOW's one-loop conventions (U-dec)` and `its orbit is that of FLOW's tower Φ_0(V)`; `FLOW.md`, `Proposition U-dec`, `Ψ := min_{U_1,…,U_{n−1}}κΣk̃`, and `[RFL-fix §3.1, per HIST Lemma HF`; `HIST.md`, `Lemma HF (HIST's φ-tower against FLOW's k̃-tower)`.

FLOW explicitly corrects its own normalization: for N ≥ 3,

`k̃(V,M) = φ_M(V) + d(M)`,

and `log 𝒩′` contains `−κu d(M)`. Thus the true order-u exponent of the normalized kernel is κφ, not κk̃. FLOW's `Def F-strip` still defines 𝒯 by k̃. Equality of their jets at 1 does not make these functionals equal throughout a neighborhood.

Here is an exact example using the actual S4′ contour geometry, not an arbitrary inadmissible matrix. Take L = 3 and adjacent blocks `{0,1,2}⁴` and `{3,4,5}×{0,1,2}³`, with centers `(1,1,1,1)` and `(4,1,1,1)`. Set every fine link to 1 except the positively oriented link `(2,0,0,0) → (3,0,0,0)`, whose value is

`U = diag(z,z,z⁻²)`, `z = (1+it)/(1−it)`, `t > 0` rational.

The axial end pieces stay inside their blocks. Among the `24·3⁴ = 1944` contours, exactly `24·3 = 72` straight pieces cross the selected link; the remaining 1872 have transporter 1. Exact enumeration independently reproduced these integers. Therefore

`M̄ = (26/27)I + (1/27)U`,

`Im det M̄ = 5200 t³ / [19683(1+t²)²] > 0`.

At `t = 1/100` the last expression is exactly `520000/1968693679683`. The example can be made arbitrarily close to 1 by decreasing t. The polar factor W consequently has `det W ≠ 1`. Since equality in `Re tr(V⁻¹WP) ≤ tr P` requires V = W for P > 0, compactness of SU(3) gives **min_V k̃(V,M̄) = d(M̄) > 0**. Already at n = 1, the cited k̃ version of `Ψ(U₀;𝔪(U₀)) = 0` is false.

**Required reading/correction:** use the true normalized φ-composite exponent, its SU(N) maximizing map, and its minimizing tower in the every-background statement. The abstract proof below then works. Identifying that tower with the k̃-defined 𝒯/Φ at arbitrary backgrounds is **NOT-VERIFIED** and is not licensed by the five-jet agreement. At the trivial point, `d = O(y⁶)` makes the jets through order five agree; the one-loop two-point coefficient uses only the lower jets. Hence this defect does **not** refute the proposed β-level reduction.

**NOT-VERIFIED as an exact nonlinear equation:** `FLOW55.md`, `at the tower D_V^*𝒞^{-1}r = 0`. The exact orbit stationarity equation is `D_V* ∇_VΨ = 0`; replacing the gradient by `𝒞⁻¹r` is justified at linear order, not for a general nonquadratic Ψ. The conclusion h* = 1 at the chosen tower follows directly from simultaneous gauge covariance and fine stationarity, without this substitution.

### 1.3 Schur/envelope and quotient factors — CONFIRMED, with the normalized exponent

**Source:** `FLOW55.md`, `Proposition K̄-1L`, proof (a)–(c); `FLOW.md`, `Lemma GH (Landau regrouping of COV-GI)`, especially the Gram-matrix argument in (iii).

Work at fixed n on a finite torus on a regular gauge stratum; remove stabilizers in both integrals consistently. Put `A = Hess_h Ψ` and write the joint Hessian in fine/orbit coordinates as

`[[B,E],[E*,A]]`.

On the nonzero h directions, differentiating the h stationarity equation gives `Dh* = −A⁻¹E*`. Therefore

`H♮ = B − EA⁻¹E*`.

This is the Hessian of the partially minimized function at the saddle. No assumption `H_Wilson D₀ = 0` has entered. Gauge invariance of that partially minimized function and its fine criticality give `H♮D₀ = 0`.

The quotient sign is also correct. Write a fine tangent as `s + D₀λ`, with `s ∈ ker D₀*`. The product measure has Jacobian `det′(D₀*D₀)^(1/2)`. Dividing out the gauge-parameter volume and integrating s gives

`½ log det_{ker D₀*} H♮ − ½ log det′(D₀*D₀)`.

Integrating h first supplies `+½ log det′ A` to the negative logarithm. This sequential derivation is the appropriate interpretation of the proof: multiplying ambient **pseudodeterminants** of a singular block matrix without its orbit-volume factor would not be a valid Schur rule.

For the coarse identity, choose orthonormal frames U for `ker D*` and V for `Ran D`, and write `D = VR`, where `R*R = D*D` on the nonzero gauge parameters. The complementary-minor identity gives

`det(V*𝒞⁻¹V) = det(U*𝒞U)/det 𝒞`.

Consequently

`det 𝒞 · det′(D*𝒞⁻¹D) = det_{ker D*}(P⊥𝒞P⊥) · det′(D*D)`.

This uses positivity of 𝒞 and the rank convention, not Wilson criticality. As an independent exact check, I used

`𝒞 = [[5,1,2],[1,4,1],[2,1,6]]`, `D = (2,1,0)ᵀ`.

The four determinants are `97`, `102/97`, `102/5`, and `5`, respectively: both products are **102**. The identity and

`Π = 𝒞⁻¹ − 𝒞⁻¹D(D*𝒞⁻¹D)⁻¹D*𝒞⁻¹`

were checked symbolically, including the deformation `𝒞 → 𝒞 + tDD*` for every `t ≥ 0`. The compressed transverse determinant is unchanged by that deformation. There is no missing fine or coarse square-root Jacobian in the stated grouping.

Thus the explicit determinant pair cancels the longitudinal covariance block. **This is not a proof that all vertices of H♮ are independent of that block, or that all remaining κ-dependent terms are uniformly bounded in n.** The Schur complement uses `A = 𝔊₀+R`, and its background derivatives must still be controlled in the remaining transverse problem.

At V = 1, eliminating h in the quadratic form gives exactly `H♮ = d*d + Q*ΠQ` and hence the stated `O♯ = H♮+dd*`. The transverse inverse and the full Feynman-completed inverse must not be confused: the latter still contains the longitudinal massless `dd*` sector. Zero modes, stabilizer volumes, and the order “infinite-volume density first, external momentum second, n last” remain part of the convention. A uniform Laplace theorem across changing stabilizers, volumes, or n is **NOT-VERIFIED** here and is not supplied by the block identity.

## 2. K̄-tad, the Green-function input, and erratum 1

### 2.1 Transported covariance — CONFIRMED; the finite check has a narrower scope

**Sources:** `FLOW55.md`, `Covariance: under a fine gauge transformation`; `checks/fl55_3.py`, `G_of`, `tadpole`, and `P1 pure-gauge tadpole`.

On a pure-gauge background, the inverse h-Hessian is conjugated at **both** endpoint color indices. After also transporting the orbit commutator, its contraction is the conjugate of the trivial-background contraction. The latter vanishes because the scalar-color covariance contracts a Lie bracket on equal color indices. This is an algebraic identity, valid beyond the one finite test.

The unmodified script reproduced exact zero on all 18 links and a nonzero untransported value on all 18. Its three first-order gradient tests also reproduced exact zero, with the omitted-covariance-variation controls nonzero on all 18 links. Its setting is `(Z/3)²`, SU(2) adjoint, diagonal rational link weights, and **m² = 1/3**. It tests covariance and the orbit-commutator component; it does not test massless four-dimensional decay, the full composite Ψ vertices, or n-uniformity.

**REFUTED as a nontrivial linearity test:** `checks/fl55_3.py`, `lam = [rand_vec(random.Random(5506), ...) ...]`. The seed is reset at every site. All site values coincide, so the gradient in P3 is identically zero. I checked this directly: **0/18 nonzero gradient links**. Reusing one generator, in memory only, gives **18/18 nonzero gradient links**; the nontrivial linearity identity and gradient cancellation both pass exactly. This coverage defect does not invalidate P1/P2.

### 2.2 (G-dec) — CONFIRMED by a direct argument; the import is not an n-uniform estimate

**Sources:** `FLOW55.md`, `(G-dec) [IMPORTED-standard]`; `FLOW.md`, `23.2 Inputs`, `(I3) The composite covariance`, and `(I5) Linear towers`.

The statement of (G-dec) is mathematically correct under its stated symbol hypotheses. FLOW55 supplies no bibliographic citation for the import. A relevant primary-source comparison is Lawler–Limic, *Random Walk: A Modern Introduction*, Theorem 4.3.1 and Corollary 4.3.3, which give Green-function and difference asymptotics for their random-walk class. That class is not automatically the class of symbols `d*𝒞⁻¹d`, so a bare citation would not establish this application. [Primary-source text](https://www.math.uchicago.edu/~lawler/srwbook.pdf).

The needed more general statement follows directly. Let `a(p)=1/g(p)`. Positivity away from zero and `g(p)=c|p|²+O(|p|⁴)` imply, near zero,

`|∂^α a(p)| ≤ C_α |p|^(−2−|α|)`.

Take a smooth dyadic partition into shells `|p| ≍ r`, `r = 2^(−j)`. After scaling a shell to unit size and integrating by parts M times, its Fourier coefficient is bounded by

`C_M r² (1+r|x|)^(−M)`.

A discrete first difference inserts `exp(ip_μ)−1`, changing r² to r³ with the corresponding derivative bounds. Summing the shells below and above `r = (1+|x|)⁻¹`, with M > 3, proves `|G(x)| ≤ C(1+|x|)⁻²` and `|∇G(x)| ≤ C(1+|x|)⁻³`. The smooth part away from zero decays faster than any prescribed power. This proof does not require a Markov-kernel representation.

For the application, (I3) gives a positive upper and lower bound for 𝒞⁻¹ at each fixed n. Thus `ŝ*𝒞̂⁻¹ŝ` has its only real zero at p = 0. The level symmetries make `𝒞̂⁻¹(0)` scalar, and analyticity supplies the required local expansion. **All constants may depend on n.** No claim of uniformity in n, or an unqualified finite-torus Green-function bound without a zero-mode prescription, follows.

### 2.3 Erratum 1 and the marginal limit — CONFIRMED at fixed n with the full local-vertex inputs

**Sources:** `FLOW55.md`, `Erratum 1 (to §5.3 steps (3)-(4)` and `The symbol of Hess 𝔗′(1)`; `FLOW.md`, `(I1) Vertex tensors`, `(I2) The intermediate Hessian`, `(I5) Linear towers`, and `Lemma U-loc'`.

The erratum is necessary: ℓ¹ locality belongs to the derivative of Ξ in its **independent arguments** `(V′,W)`, not automatically to its pullback through the massless orbit minimizer. Its use in the proof is valid. Here is the full chain, including what the short citation to (I3) alone omits.

1. The residual satisfies `Dρ*(1)v = O(|P|²)v` on a transverse external mode, at fixed n. Orbit stationarity and tree stationarity give the quadratic version of this assertion; F-tree/F-bg give the same estimate. Pure-gauge input has zero residual.
2. Global color invariance gives `Ξ(1,1)=0`. Joint gauge covariance gives `DΞ(1)[d_nλ_n,d₀λ₀]=0` for compatible gauge parameters. This statement applies to the full covariant R-linear coefficient, not just the commutator tested in fl55_3.
3. Differentiating the inverse h-Hessian gives `−G(δ𝔊₀)G`. At the trivial field,

   `δ𝔊₀ = (δD)*𝒞⁻¹d + d*𝒞⁻¹δD + d*δ(𝒞⁻¹)d`.

   The first two terms put a discrete derivative on one Green function; the third puts one on each. With (G-dec), the long-distance bounds are `(1+|b−c|)⁻⁵` and `(1+|b−c|)⁻⁶`. Direct variations of the R-linear vertex are local. The required locality of these vertices follows from (I1), (I2), and (I5), by differentiating the intermediate stationary equations through the requisite orders and using their gapped inverse. **(I3) by itself would not establish those derivative statements.** Exponential vertex tails preserve these power bounds. They are summable in four dimensions, so the resulting Fourier symbol of DΞ is continuous.
4. In the orthogonal fine representative, F-bg gives the input limit `(v,v/ℓ)`. The orbit correction has symbol

   `d̂(d̂*𝒞̂⁻¹d̂)⁻¹d̂*𝒞̂⁻¹(v−Q̂a)`.

   The denominator is of order `|P|²`, the left factor is of order `|P|`, and the right contraction is `O(|P|²)` for transverse v with the F-bg matching. The correction is therefore `O(|P|)`, not an additional constant transverse term. The limit pair is a compatible gradient: use the coordinate measured from the common coarse root, `λ₀(x)=x·v/ℓ` and `λ_n(X)=X·v`. Cut both off at radius R compatibly. Their discrete gradients stay bounded and converge on every fixed set. Dominated convergence against the ℓ¹ kernel proves that DΞ annihilates the limit pair. Hence the pulled-back linear coefficient is `o(1)`, even without ℓ¹ locality of the pullback itself.
5. For the quadratic-in-ρ term, the two massless propagators give a bubble bounded by

   `C_n ∫_{BZ} dk/[|k|² |k+P|²] ≤ C'_n(1+log(1/|P|))`.

   Split into balls around 0 and −P and their complement to obtain this bound; the one-propagator second-vertex term is finite. This argument is preferable to inferring a pointwise Fourier bound solely from an `O(|x|⁻⁴)` kernel. Thus the two residual factors give `O(|P|⁴ log(1/|P|))`.

Combining these statements gives `Hess 𝔗′(1) = O(|P|²)o(1) + O(|P|⁴ log(1/|P|)) = o(|P|²)`. Therefore **β[𝔗′_n] = 0 for every fixed n**, with the directional coefficient and thermodynamic prescription of the paper. The original, pre-erratum claim that `DΞ*(1)` itself is ℓ¹ should remain withdrawn.

The sentence `This is the one place where a κ-dependent term could have reached the coefficient of n log L` is **NOT-VERIFIED** as an exhaustive assertion. The argument eliminates this tadpole. It does not prove the missing n-uniform bounds for H♮'s remaining vertices.

## 3. GH0, K̄-β, and the remaining estimate

### 3.1 GH0 — CONFIRMED at the trivial-point coefficient level

**Sources:** `FLOW55.md`, `Lemma GH0`; `FLOW.md`, `Lemma FINE-IR (the fine scalar polarisation)`, `Corollary VFINE-gh`, `Lemma F-bg`, and `GH-log` part (d) for the normalization comparison.

I checked the scalar Ward rewrite and the infrared coefficient used here, rather than accepting the earlier review labels. In FLOW's notation the scalar polarization is

`x₀(p) = [16 sin²(p/2)/p²] J(p)`.

The continuum part of J has angular average `⟨n₁²n₂²⟩ = 1/24`. Its logarithmic coefficient is `1/(192π²)`; the prefactor tends to 4. The integrable lattice-minus-continuum remainder gives a common finite part a₀. Thus `x₀(p) = 2c_g log(1/|p|)+a₀+o(1)`, with `c_g = 1/(96π²)`, as required. This scalar statement needs no finite-flux magnetic asymptotic.

The linear tower sends a transverse coarse wave to a smooth fine wave of momentum `P/ℓ` and amplitude `(ε/ℓ)(1+O(P))`; its nonzero transverse aliases are O(P³). Gauge invariance removes longitudinal fine components, and color invariance removes the first-derivative chain-rule term. Translation invariance forbids smooth/alias cross terms at nonzero sufficiently small P. At fixed n, aliases contribute O(P⁶), while the amplitude correction contributes `O(P³ log(1/|P|))` to the quadratic density. The factor `ℓ⁴·ℓ⁻²·ℓ⁻²` is exactly one.

Consequently the ghost difference contains **the same scalar function** at the two scales:

`x₀(P) − x₀(P/ℓ) → −2c_g log ℓ`.

The finite part cancels, not merely up to an n-dependent constant. For clarity about real/complex counting, one positive root represents two real adjoint directions, so `½ log det_R` becomes one complex scalar determinant. Its density difference is `−q_α² c_g P² log ℓ`. Dividing by the Wilson-wave density `P²/4` gives `−4q_α²c_g log ℓ`. If `H = i diag(h₁,…,h_N)` has `Σh_i=0` and `Σh_i²=N` in FLOW's normalization, then

`Σ_{i<j}(h_i−h_j)² = NΣ_i h_i² = N²`.

Hence

`β[G_gh,n] = −4N²c_g log ℓ = −N²/(24π²) log ℓ = −(1/22)β₀^std log ℓ`.

“Exactly” refers to this limiting marginal coefficient, after the thermodynamic limit at fixed n. It does not mean the finite-P polarization has no corrections, or that a finite-torus determinant with changing zero modes is an ordinary analytic function without a prescription.

### 3.2 K̄-β and the equivalence — CONFIRMED as a conditional coefficient reduction

**Sources:** `FLOW55.md`, `Corollary K̄-β` and `(UNIV-1L) ⟺ (UIR^♮)`; `FLOW.md`, `Lemma U-pair`, application (1), and `(UNIV-1L)` in §4.

Use the normalized exponent in §1.2, the quotient convention in §1.3, the fixed-n tadpole result, and U-pair's local-vertex hypotheses. The endpoint drift contributes zero: one can choose the saddle representative to be the actual original tower, with h* = 1, so this is precisely U-pair's drift application. Gauge-changing the representative cannot change its scalar value. The k̃/φ jet agreement preserves the same β at the trivial field.

Writing `a = β₀^std log L` and `X_n = β[G♮_⊥,n]`, the result is

`B_n = −X_n + an/22`,

and therefore, identically for every n,

`B_n − an = −[X_n + 21an/22]`.

The two absolute deviations are equal. Their suprema are finite simultaneously, with the same bound. This verifies the claimed **(UNIV-1L) ⇔ (UIR♮)**, conditional on the determinant/coefficient identification above. It does not prove either bound. In particular it does not prove convergence of the individual b_k; bounded partial-sum error alone permits persistent oscillations.

### 3.3 What is still NOT-VERIFIED; one reversed implication is REFUTED

**Sources:** `FLOW55.md`, `Missing: the estimate that combines them`, `(UIR^♮) is OPEN`, and `which (UIR^♮) bounds uniformly in n`; `FLOW.md`, `Lemma U-res`, `(R-a)`, `(R-b)`, and `Lemma U-res' ((R-a) needed only in integrated form)`.

The n-uniform transverse estimate, including the composite vertices and the level transverse determinant, remains **NOT-VERIFIED**. FLOW55 correctly labels (UIR♮) open. The algebraic cancellation and fixed-n ℓ¹ argument supply no n-uniform constant for it.

The assertion in KAPPA's proof that (UIR♮) bounds (R-a)/(R-b) is **REFUTED as a logical implication**. (UIR♮) bounds an integrated scalar coefficient. The residue lemma's pointwise estimate and absolute-integral bounds are sufficient conditions, not consequences. For example, adding `n Σ_{μ=1}⁴ cos q_μ` to an integrand changes no integral over the Brillouin torus, preserves evenness and hypercubic symmetry, and destroys a uniform pointwise (R-a) bound at a fixed nonzero q. Likewise zero-integral bumps concentrated inside `|q|<1/ℓ` can have arbitrarily large absolute integral there. These are counterexamples to the implication between estimates, not claims about the actual Yang–Mills integrand.

KAPPA's **conclusion as a conditional scalar statement is CONFIRMED** without that inference: (UIR♮) and the exact identity above immediately give `B_n = β₀^std n log L + O_κ(1)`. To claim this for every κ > 0 requires (UIR♮) for each such κ. No uniformity as κ tends to zero or infinity has been proved.

## 4. Ward identities and marginal jets

### 4.1 WARD-J — CONFIRMED, including the displayed signs and factors

**Source:** `FLOW55.md`, `Lemma WARD-J (jet Ward identities at the trivial point)`.

For `dλ = λ_y−λ_x`, the infinitesimal link-log transformation is

`Θ = −dλ − ½[X,λ_x+λ_y] − (1/12)[X,[X,dλ]] + O(X⁴)`.

The two one-sided exponential derivatives give this formula, with no cubic Bernoulli term. Constant color transformations fix 1; an invariant linear functional on su(N) is zero, giving F₁ = 0. Substituting Θ into `DF(X)[Θ]=0` and comparing homogeneous degrees 1, 2, and 3 gives exactly W2, W3, and W4. In particular the quartic coefficients are **−3/2** and **−1/2**.

As a separate exact check I expanded a single SU(2) Wilson plaquette by matrix power series, without the author's BCH implementation. In units of the anti-Hermitian Pauli matrices, the four link directions were `(1,2,0)`, `(0,−1,1)`, `(2,1,1)`, `(−1,0,2)`, and the four site gauge parameters were `(1,0,1)`, `(−1,2,0)`, `(0,1,−2)`, `(2,−1,1)`. Truncation retained the coefficients `s^j t`, j ≤ 3. The exact results were

`W2 = 0`, `W3: 48 = 48`, `W4: −192 = −192`.

The last two are nonzero checks, so the sign/factor comparisons are not vacuous.

### 4.2 fl55_4 and JET-MARG — CONFIRMED; one sentence about the symmetric channel is REFUTED

**Sources:** `checks/fl55_4.py`, `eqs_H`, `eqs_S`, `eqs_W0`; `FLOW55.md`, `Proposition JET-MARG`, `spanned by V^YM`, and `Erratum 2`.

The script's equations impose the stated generators of B₄, both required leg transpositions, and polynomial transversality. Its ranks reproduced the claimed dimensions. I also used an independent, smaller classification. Sign flips force each of the four vector indices in a coefficient tensor to occur an even number of times. Axis permutations therefore leave four tensor types, namely the three pairings of Kronecker deltas and the tensor with all four indices equal. For the p and q coefficients together this is **eight**, not 512, unknowns.

Exact elimination in this eight-dimensional space gave:

| Bose type | Dimension before transversality | Dimension after transversality |
|---|---:|---:|
| antisymmetric | 1 | 0 |
| symmetric | 1 | 0 |

The antisymmetric generator is V^YM, up to sign. The symmetric generator is instead

`S_{μνρ} = δ_{μν}r_ρ + δ_{νρ}p_μ + δ_{ρμ}q_ν`, `r = −p−q`.

It is nonzero and is not V^YM. Thus `without transversality ... spanned by V^YM` is **REFUTED if applied to both color channels**, as the surrounding sentence does. Only the antisymmetric channel has that generator. Both generators fail the homogeneous Ward identity, so this wording defect does not affect JET-MARG. At `p=e₁`, `q=e₂`, `ν=ρ=2`, the first-leg contraction of each displayed generator is 1.

There is also a short check that avoids any imported classification of invariant color three-tensors. For each fixed set of color indices write a linear cubic tensor as

`T_{μνρ}=A_{μνρσ}p_σ+B_{μνρσ}q_σ`.

Transversality in the p-leg forces B = 0, because the monomials `p_μq_σ` are independent. Transversality in the q-leg then forces A = 0. Full Bose symmetry and the Ward identities provide both leg identities. Thus there is no homogeneous linear cubic remainder even before using the f/d color decomposition.

For completeness, the quadratic normalization is unique: hypercubic covariance makes the diagonal quadratic entries `b p_μ²+cΣ_{ν≠μ}p_ν²` and the off-diagonal entries `a p_μp_ν`. Transversality imposes b = 0 and a = −c. This leaves `c(p²δ−pp)`, with c fixed by β. After subtracting β times Wilson, W3 therefore makes the marginal cubic tensor homogeneous-transverse and hence zero. W4 then makes the constant quartic tensor transverse against an arbitrary leg momentum; that tensor is zero as well. Exponential locality supplies the required momentum Taylor expansions. Link-center phases do not change these conclusions about the first nonvanishing degree; erratum 2 supplies the parity explanation used in the author's presentation.

**Bankable scope:** all dimension-four Taylor pieces at orders 2–4 are fixed by β, under the stated locality and symmetry hypotheses. This is not an estimate of the higher Taylor remainder without the polydisc hypothesis, nor an n-uniform irrelevance gain.

### 4.3 Envelope jets — CONFIRMED

**Sources:** `FLOW55.md`, `Lemma ENV`; `checks/fl55_2.py`, `E4 quartic with exchange`.

The stationary equation gives `Au″=−c`. Differentiating the value function then gives the cubic pullback and the quartic term **−3c*A⁻¹c**. The author's exact polynomial checks reproduced. Independently, for

`f(u,v) = (3/2)u² + 2uv + 2v² + (5/2)uv² + (7/6)v³ + (11/24)v⁴`,

the stationary solution is `u*(v)=−2v/3−5v²/6`. Direct substitution gives `D²W=8/3`, `D³W=−3`, and `D⁴W=−14=11−3·25/3`. This checks the exchange coefficient separately from the author's polynomial.

## 5. W-loc and the coefficient arithmetic

### 5.1 W-loc's operative diagnosis — CONFIRMED, with two scope corrections

**Sources:** `FLOW55.md`, `Lemma W-loc`; `FLOW.md`, `Proposition F-rem`, `Theorem F-flow`, `Theorem F-tune`, `Lemma F-ind`, `[RFL10-fix S10-2] (DEF) is RETIRED`, `Lemma GP-L`, `Lemma T-tel`, and `(T-a1-M)` / `(T-b)` / `(T-c)` in §§99, 103.

F-rem applies β, F-ren, the polymer Cauchy bound, and the supplied large-field estimate. F-flow sums the resulting scalar inequalities. F-tune uses those inequalities and continuity in the bare coupling. F-ind orders the constants and requires that the layer-1 hypotheses at level k use only the flow through level k. **These downstream proofs perform no new operator inversion.** Their nontrivial background control is supplied by the polymer/continuity/infinite-volume hypotheses; it is not proved by Ward identities.

The C1/C2 reading is accurate for the nontrivial-background obstruction under discussion. FLOW's explicit definition of `c^tot_n` on the critical flux family removes its off-shell Wilson-Hessian defect. GP-L and T-tel then expose the bare `H_⊥⁻¹`. The stated plane-wave vertices in T-a1-M and the polarization identity T-b are Taylor data at 1. T-c is the extra finite-flux comparison. An orbit-averaged, normalized-exponent organization can formulate the coefficient problem without that finite-flux detour, while leaving a difficult transverse estimate.

Two literal claims need narrowing:

* **REFUTED:** `FLOW55.md`, `In FLOW's proof of (F-1) = (UNIV-1L)`. FLOW's F-1 permits a computed positive slope β₀′; UNIV-1L fixes it to β₀^std. For the exact sequence `b_k = 2β₀^std log L`, F-1 holds with R = 0 and β₀′ = 2β₀^std, while UNIV-1L fails. Equivalence holds after fixing the slope to the standard value (and allowing the harmless factor two between prefix and interval bounds).
* **REFUTED as an exhaustive inverse inventory:** `FLOW55.md`, the table row `F-tree, F-bg, F-ren, F-depth, F-tel, Lemma TOW` listing only a gapped one-step inverse. `FLOW.md`, `the transverse inverse symbol Ĝ_k := (Ĥ_k|_⊥)^{-1}` and `Base: Ĝ_0 = P_⊥/|ŝ|²`, explicitly use massless trivial-background inverses in F-tree/F-bg. These are not nontrivial-background Wilson resolvents. Their presence does not refute the narrower C1/C2 diagnosis, but “all remaining inverses are gapped” is too strong if read literally, especially once the scalar h/ghost inverses are included.

### 5.2 fl55_1 and the numerical fractions — CONFIRMED as exact coefficient arithmetic

**Sources:** `checks/fl55_1.py`, `Part A`, `B2`, `B3`, `C1`, `C2`; `FLOW55.md`, `What is re-verified exactly`; `FLOW.md`, `Conventions fixed for this file`.

All 13 verdict lines and all four controls reproduced exactly. The script uses explicit SU(2)/SU(3) generators and exact symbolic/rational data. Independently, write `t = tr_ad ΣΩ_{μν}Ω_{μν}`. With the displayed spin coupling 2,

`X_gh=t/12`, `X_vec=4t/12−2t=−20X_gh`.

Thus `(½X_vec−X_gh)/(−X_gh)=11`, with orbital-plus-ghost contribution −1 and spin contribution 12. This derivation is independent of the random field-strength example. It verifies the arithmetic of the supplied heat coefficient and operator, not a replacement proof of the complete heat-kernel theorem or of the soft-chain residue bounds.

The Wilson expansion is `1−Re tr(exp(itX))/N = t² tr(X²)/(2N)+O(t⁴)`, so the conversion is `u=2N/g_std²`. With the stated `b₀=11N/(48π²)`,

`2N·2b₀ = 11N²/(12π²)`,

`(1/22)β₀^std = N²/(24π²)`,

`½(−20)−1 = −11`, `½(−20)−½ = −21/2`, `(−21/2)/(−11)=21/22`.

The sphere moments are exactly `1/4`, `1/8`, and `1/24` for `n₁²`, `n₁⁴`, and `n₁²n₂²`. The scalar angular combination is `−32/24+4/4+4/4−1=−1/3`; multiplying by `|S³|/(2π)⁴=1/(8π²)` gives the stated magnitude `1/(24π²)`. The **1/22 : 21/22 split is for this transverse/half-ghost grouping**. It is not a universal separate ghost fraction independent of determinant convention.

## 6. Execution and provenance

The four unmodified scripts were run with `PYTHONDONTWRITEBYTECODE=1 python3 -B`, with outputs returned directly to the tool transcript. No output/check files were created or overwritten. Their actual reproduced results were: fl55_1, 13/13 and 4/4 controls; fl55_2, E0/E3/E4 and both controls; fl55_3, 4/4 and both controls, with the P3 limitation above; fl55_4, dimensions 1/1 before and 0/0 after transversality, and both controls. A successful process exit alone was not used as the verdict: these scripts report outcomes in stdout.

Independent calculations used exact SymPy expressions or `fractions.Fraction`: the non-diagonal Schur example and its symbolic deformation; the eight-coefficient tensor classification; the nonzero plaquette Ward checks; the separate envelope polynomial; the corrected-in-memory P3; and the SU(3) S4′ normalization counterexample. No floating-point comparison, quadrature, fitted slope, or author's previously printed decimal was used as evidence. The Green bound and infrared limits above are analytic arguments, not numerical tests. No unsourced literature recollection is used as a load-bearing step; the literature comparison in §2.2 was read directly.

SHA-256 of the reviewed target and check implementations:

| File | SHA-256 |
|---|---|
| FLOW55.md | `56d2707f4b571585db26cf2a077dbaee57bc936c76821cdbc50710e4b36e9d25` |
| FLOW.md | `085cd225228a23847b053650fe8bff4c14529d7e630a74565b301d39855e442f` |
| checks/fl55_1.py | `ddda45c5e12b2ceea4a29b4ad975205b88f53290064841d16d05293e23511536` |
| checks/fl55_2.py | `b12adc49b31206a6b3064dfb1cf945977e67e3474ec5325d416f2140998b227d` |
| checks/fl55_3.py | `39e5fe95a50e7cbd2977bd998d21f6078309c5f0658cf0681c55ff0e7e8176bb` |
| checks/fl55_4.py | `55bce5e507ed2e3ca91a3c0772ae03b0023a7437fc6a49ec5b0030accfced9e2` |

The six hashes were rechecked after drafting and were unchanged. Only this review file was written. No git command was used. The local science-workflow and review-loop evidence lenses were applied within the user's narrower scope; no registry status, source file, branch, or external message was changed.

## Exactly what may be banked

1. **CONFIRMED — exact symmetry:** Theorem K̄ for the normalized composite kernel. Fine Hessian transversality holds at the partially minimized **critical** saddle, not at arbitrary fine configurations.
2. **CONFIRMED — formal one-loop algebra, with the explicit normalization condition:** Schur/envelope elimination, the fine quotient Jacobian, and cancellation of the explicit `½ log det 𝒞 + ½ log det(D*𝒞⁻¹D)` pair. For N ≥ 3, the every-background version must use the actual φ-tower; the literal k̃-based zero-minimum setting is **REFUTED**. Their trivial-point jets relevant to β agree.
3. **CONFIRMED — fixed-n coefficient statements under the named local-vertex and density conventions:** the transported tadpole has β = 0, erratum 1 supplies the correct continuity argument, and the ghost coefficient is exactly `−(1/22)β₀^std n log L`. The needed Green decay is justified in §2.2; no n-uniform Green constant was inferred.
4. **CONFIRMED — conditional reduction:** `B_n = −β[G♮_⊥,n]+(1/22)β₀^std n log L`, and therefore **(UNIV-1L) ⇔ (UIR♮)**, at that coefficient level. Conditional κ-independence of the slope follows directly. **(UIR♮) itself remains NOT-VERIFIED.** Its scalar bound does not imply the stronger integrand estimates.
5. **CONFIRMED — local Taylor structure and arithmetic:** WARD-J, absence of a nonzero homogeneous transverse linear cubic remainder, marginal quartic uniqueness, the envelope exchange term, `11 = 12−1`, `2N·2b₀`, and the `1/22 : 21/22` split in the stated grouping. The symmetric generator and P3 coverage corrections are recorded above.
6. **CONFIRMED — the narrow workflow diagnosis:** F-rem/F-flow/F-tune/F-ind introduce no new operator inversion, and the specified finite-flux comparison is a choice of FLOW's current organization. The result is a reformulation of the remaining coupling problem. **No n-uniform transverse estimate, completed nonperturbative flow theorem, or constructive four-dimensional Yang–Mills closure may be banked from FLOW55.**
