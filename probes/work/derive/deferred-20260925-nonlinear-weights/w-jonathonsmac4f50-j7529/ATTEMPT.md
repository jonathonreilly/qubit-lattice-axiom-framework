# Deferred science, unit 21 (PR #9083): nonlinear self-weighted laws — attempt a1

Worker `w-jonathonsmac4f50-j7529`, model `claude-opus-5-5`. PR #9083 was written by a Claude session, the same model family. The referee should be of another family.

**Inspection before work.**
- Current `origin/main` is `ef918c1910ccf8b7a1125fbbdfc54eb84186176e`.
- The three bundled originals of PR #9083 match their recorded SHA256. The accepted paths on main match their recorded `accepted_sha256`.
- The landed note (`docs/DYNAMICS_CLAUSE_A_DISTANT_RECORD_IS_A_RECORDED_RANDOMIZER_..._2026-09-24.md`) states the residual worked here: "This argument classifies the already affine family. Tests of five chosen laws do not prove that every nonlinear self-weighted law is affine. That wider closure remains deferred."
- The campaign synthesis on main repeats it: "Self-weighted consistency checked inside the affine covariant family does not classify all nonlinear laws."
- No attempt on this problem and no other active claim existed.
- The related directories `deferred-20260924-formation` (w-macbookpro9927a) and `the-exchange-sign-from-the-coin` (w-macbookpro90c72, refereed) treat other residuals. Nothing from them is reused.

## 1. Statement attempted

**Setting.** This is the landed note's supplied setting, all of it conditional mathematics and nothing adopted:
- finite complex density matrices, tensor composition, pure two-qubit states;
- projective conditional compression: a partner's record updates the site to the steered state.

**The law.** `F(r, q)` is the probability of the outcome `+q` for a qubit with Bloch vector `r` and binary menu `{q, −q}`. Assume:
- **(C) Covariance, no extra directional input:** `F(r, q) = f(|r|, r·q)`. Write `h(c) = f(1, c)` for pure states and assume `h` measurable.
- **(N) Antipodal normalization:** `F(r, q) + F(r, −q) = 1`.
- **(S) Self-weighted records:** a partner qubit `B` of a pure joint state records with the same law. The weight of its outcome `+q'` is `F(r_B, q')`, not a Born weight.
- **(K) Steering composition:** after `B`'s record, `A` is in the pure state obtained by projecting `B` and tracing it out.
- **(NS) Equal-time no-signalling:** for every menu `q` of `A`, the direct law equals the self-weighted average over `B`'s record:
  `F(r_A, q) = Σ_± F(r_B, ±q') F(n_±, q)`.
- **(E) Endpoint support**, where used: `h(1) = 1`.

**Claim.** Fix one Bloch length `0 < ℓ < 1`. Suppose (NS) holds for the two partner menus of C1 (along and orthogonal to `B`'s Bloch vector) and for all menus `q ∈ S²` of `A`. Then either:
- `h(c) = 1/2` a.e. and `f(ℓ, ·) = 1/2` a.e., the constant law; or
- `h(c) = (1 + c)/2` a.e. and `f(ℓ, x) = (1 + x)/2` a.e., Born.

(E) excludes the constant law. **No ensemble affinity and no Born ensemble weights are assumed.** This extends the landed Schmidt test, which is the first of the two menus, from the affine family to all measurable laws.

## 2. Steps

1. **PROVED — oddness.** (N) at pure states gives `h(c) + h(−c) = 1`, so `H := h − 1/2` is odd on `[−1, 1]`. (N) with (C) also gives `f(ℓ, 0) = 1/2`.
2. **PROVED and CHECKED (C1) — the two steerings, by explicit construction for every `0 < ℓ < 1`.**
   - Take `|ψ⟩ = √((1+ℓ)/2)|+x⟩|0⟩ + √((1−ℓ)/2)|−x⟩|1⟩`. Then `r_A = ℓx̂` and `r_B = ℓẑ`.
   - **Radial chord.** `B`'s z-menu (along `r_B`) gives `A` the states `±x̂`, with self-weights `w := f(ℓ, ℓ)` and `1 − w`.
   - **Perpendicular chord.** `B`'s y-menu (`r_B·q' = 0`) gives `A` the states `n_± = (ℓ, ±√(1−ℓ²), 0)`, with self-weights `f(ℓ, 0) = f(ℓ, −0) = 1/2` (step 1).
   - The Born weights `(1 ± ℓ)/2` and `1/2` are printed by C1 only to certify the geometry. They are not used.
   - C1 verifies all of this symbolically for every `ℓ = (1 − u²)/(1 + u²)`, `u > 0`.
3. **PROVED — the chord identity.** Apply (NS) to both menus and subtract.
   - Radial: `f(ℓ, ℓ x̂·q) − 1/2 = (2w − 1) H(x̂·q)`, using step 1.
   - Perpendicular: `f(ℓ, ℓ x̂·q) − 1/2 = (1/2)[H(n₊·q) + H(n₋·q)]`.
   - Hence, **for every `q ∈ S²`**:
     `(2w − 1) H(x̂·q) = (1/2)[H(n₊·q) + H(n₋·q)]`.   `[**]`
4. **ASSUMED (standard, named) — harmonic expansion.**
   - `H ∈ L²[−1, 1]` (bounded, measurable) has a Legendre expansion `H = Σ_{L odd} a_L P_L`.
   - For a unit vector `n`, the function `q ↦ H(n·q)` lies in `L²(S²)`, and its degree-`L` spherical-harmonic component is `a_L P_L(n·q)` (addition theorem / Funk–Hecke).
   - Projecting `[**]` onto degree `L` gives, for every `q`:
     `a_L [(2w − 1) P_L(x̂·q) − (1/2)P_L(n₊·q) − (1/2)P_L(n₋·q)] = 0`.
5. **PROVED, with CHECKED ingredients (C2, C3) — restriction to the chord's great circle.**
   - Put `q = (cos θ, sin θ, 0)` and `cos β = ℓ`.
   - `P_L(cos ψ) = Σ_j a_j a_{L−j} cos((L − 2j)ψ)`, with `a_j = C(2j, j)/4^j > 0`. This is classical, ASSUMED and CHECKED exactly for `L ≤ 13` (C2).
   - So the bracket in step 4 becomes `Σ_{k odd ≤ L} c_k^{(L)} [cos(kβ) − (2w − 1)] cos(kθ)`, with every `c_k^{(L)} > 0` (C3 checks the identity for `L ≤ 7`).
   - If `a_L ≠ 0` for some `L ≥ 3`, then both the `k = 1` and the `k = 3` coefficients must vanish: `cos β = 2w − 1 = cos 3β`.
   - But `cos 3β − cos β = −2 sin 2β sin β ≠ 0` for `β ∈ (0, π/2)`. At `ℓ = 3/5`: `3/5` against `−117/125` (C4).
   - **Hence `a_L = 0` for every odd `L ≥ 3`, and `H(c) = a₁c` a.e.**
   - **Why the full sphere is needed.** With menus `q` only in the chord's plane, the Fourier modes of `θ ↦ H(cos θ)` decouple. A single Chebyshev law `H ∝ T₃` then satisfies the in-plane identity with `2w − 1 = cos 3β`. Only the out-of-plane menus, through the Legendre content of step 4, exclude it.
6. **PROVED and CHECKED (C5c) — Born or constant.**
   - With `H = a₁c` and `a₁ ≠ 0`, the `L = 1` relation gives `2w − 1 = cos β = ℓ`.
   - The perpendicular identity at `q = x̂` gives `w = f(ℓ, ℓ) = 1/2 + a₁ℓ`.
   - So `a₁ = 1/2`, `h(c) = (1 + c)/2`, and `f(ℓ, x) = 1/2 + (2w − 1)H(x/ℓ) = (1 + x)/2`.
   - With `a₁ = 0`: `h = 1/2` and `f(ℓ, ·) = 1/2`, the constant law. (E) excludes it.
   - The a.e. qualifiers can be dropped if `h` is continuous.
7. **CHECKED (C5a, C5b, C5d, C5e) — consistency with the landed note.**
   - The radial chord alone is the landed Schmidt test. On the affine family it gives `λ(λ − 1) = 0` (C5a).
   - The perpendicular chord holds for every affine law (C5b). So it is the pair of menus that does the work beyond the affine family.
   - Born satisfies both chords (C5d).
   - The nonlinear law `h = 1/2 + (3c − c³)/4`, which has the endpoint support, fails for every `w` (C5e).
   - Floating-point evidence (C6): two tanh laws and the cubic leave residuals `0.015`–`0.15` for every `w`; Born leaves `2·10⁻¹⁶`.

## 3. First failing step, and scope

**No step fails for the claim as stated.** Its premises are all explicit and supplied:
- **(K), the steering composition, is essential.** The landed replacement-rule countermodel (the recorded site set to its selected pure possibility, the other site left unchanged) satisfies the lock and no-signalling for every normalized law. So the steering composition is exactly what excludes non-Born laws here. It is supplied, not derived.
- **(C) excludes laws with extra directional input.**
- **The sites are qubits.**

## 4. What would finish it, and the next obligations

- **Pointwise statement without regularity.** Use chords at every `ℓ` and all partner menus to fix `h` on null sets.
- **Higher-dimensional sites.** The analogue for qudit sites with binary or larger menus. A candidate route: harmonic analysis on `CP^{d−1}`.
- **Self-weighted mixed-state ensembles.** The landed general affinity argument imports Born weights. Replace them by self-weights, now that the pure law is fixed.
- **Composition (K) from the record clauses.** Derive the steering update rather than supply it. The replacement-rule countermodel marks what must be excluded.
- Unit 21's other residuals are ranked in `RECOVERY_STATUS.json`.
