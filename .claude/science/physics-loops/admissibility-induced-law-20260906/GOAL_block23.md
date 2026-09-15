# GOAL — block 23: the plane's correlations decay at least algebraically at every coupling — complex rotations with explicit constants; block 20's rate upgraded to a power of the side (2026-09-15)

**Owner directive (2026-09-15):** don't stop; assess the next lane at each conclusion; no subagents; derivations over computation.

**Why this block.** Block 20 (PR #8154) shows the unsoldered sphere static law never orders on a plane, with the weak rate `M_N⁴ ≤ (3π²β + 1)/H_{L−1}`. What replaces block 19's Green-function channel there? This block gives the rate: on any plane window and on the plane torus, `|⟨s_0·s_x⟩| ≤ (3/2)e^{9/16}(1 + d(x))^{−κ(β)}` with `κ(β) = 5/(512β)` for `β ≥ 5/256` and `κ(β) = 1 − 128β/5 ≥ 1/2` below — a power law with a coupling-dependent exponent, uniform in the window and the exterior records. Hence `M_N² ≤ 6e^{9/16}(1+L)^{−min(κ,1)} + 1/(4L²)` on the torus (a power of the side in place of `(log L)^{−1/2}`), every infinite-volume static law on the plane has the same decay, and no Green-function-type kernel (whose exponent would be fixed by the dimension) exists on planes at any coupling.

**Object.** Records `s = (ρ cos φ, ρ sin φ, ζ)` with `ζ ∈ [−1, 1]`, `ρ = (1 − ζ²)^{1/2}`, `dσ = dζ dφ`; the window law `μ_Λ^ω ∝ Π_b e^{β s_y·s_z} Π dσ` on a finite `Λ ⊂ Z²` with exterior records `ω`, or the torus law on `(Z/2LZ)²`; `d(y)` the Euclidean distance to `0` on `Z²` or the torus distance; `H_R = Σ_{j≤R} 1/j`.

**Contract.**
- P1 (the complex-shift bound): for any real `a` on the sites (zero at exterior sites), `|⟨s_0^1 s_x^1 + s_0^2 s_x^2⟩| ≤ exp(a_x − a_0 + β Σ_b (cosh(a_y − a_z) − 1))`; the same for the pairs `(2,3)`, `(1,3)`; hence `|⟨s_0·s_x⟩| ≤ (3/2)·` the same. Route: `cos(φ + ia) = cos φ cosh a − i sin φ sinh a`; `|e^{c cos(φ+ia)}| = e^{c cos φ cosh a}`; `cos φ cosh a ≤ cos φ + (cosh a − 1)`; the period integral of an entire `2π`-periodic function is shift-invariant.
- P2 (the shift function): `a_y = γ max(0, log((1+R)/(1+d(y))))` with `R = d(x)`, on windows `Λ ⊇ {d < R}` and on the torus: `|a_y − a_z| ≤ γ/(1 + min(d(y), d(z)))` on every bond, zero unless the smaller endpoint has `d < R`; `Σ_b (cosh(a_y − a_z) − 1) ≤ 2γ² cosh γ (1 + 8H_R)` (sup-norm shells of at most `8j` sites; `cosh t − 1 ≤ (t²/2)cosh t`).
- P3 (the rate): `|⟨s_0·s_x⟩| ≤ (3/2) e^{18βγ² cosh γ}(1+R)^{−(γ − 16βγ² cosh γ)}`; with `γ = min(1, 5/(256β))` and `cosh 1 ≤ 8/5` (from `8/3 ≤ e ≤ 11/4`): the exponent `κ(β)` and the prefactor `(3/2)e^{9/16}`.
- P4 (consequences): the torus bound on `M_N²`; every infinite-volume static law on `Z²` (should one exist) has `|⟨s_0·s_x⟩| ≤ (3/2)e^{9/16}(1+|x|)^{−κ}`; the placement.
- N-gate: the negative "no Green-function-type kernel on planes" with its escapes (the constants are not sharp; the true decay may be faster; `d = 3`).

**Lens pass (self-run panel).**
- *"This is McBryan–Spencer 1977."* Yes, for `O(N)`; re-proved at scope with explicit constants for this rule, on windows with exterior records and on the torus, and placed against block 20's rate and block 19's kernel.
- *"The exponent `5/(512β)` is tiny."* It is the known weakness of the elementary route; the theorem is the existence of a power law with explicit constants, uniform in the volume; the true decay (faster) is not claimed.
- *"The torus has no exterior; the shift function wraps."* `d_T` is `1`-Lipschitz along bonds and its sup-norm shells have at most `8j` sites, so P2 holds verbatim with `R = d_T(0, x)` up to `√2 L`.
- *"Exterior records are not integrated."* The shift acts on interior angles only; bonds to the exterior get `a_z = 0`, consistent with the formula because `Λ ⊇ {d < R}`.

**Forbidden phrases (beyond the lane's standing list):** "phase transition", "critical", "converge", "certified", "emergent", "Kosterlitz", "the true exponent is", "the plane carries a Green-function kernel".

**Prior-art search at `origin/main`.** Block 20 (no long-range order on planes); main's quantum no-order notes; nothing on algebraic decay for the sphere-valued record law. Open PRs: #8153–#8156 (this lane).
