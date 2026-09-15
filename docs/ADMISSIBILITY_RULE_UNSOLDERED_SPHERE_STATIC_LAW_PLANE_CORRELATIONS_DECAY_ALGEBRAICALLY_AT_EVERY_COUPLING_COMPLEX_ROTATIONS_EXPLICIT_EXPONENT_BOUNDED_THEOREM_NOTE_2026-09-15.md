---
claim_id: admissibility_rule_unsoldered_sphere_static_law_plane_correlations_decay_algebraically_at_every_coupling_complex_rotations_explicit_exponent_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the static law of the exponential zonal rule on the pure-state sphere under the unsoldered reading on a coordinate plane of the lattice — finite windows Lambda of Z^2 with any exterior records, and the torus (Z/2LZ)^2 — with d(y) the Euclidean or torus distance to the origin, H_R = sum_{j<=R} 1/j, and kappa(beta) = 5/(512 beta) for beta >= 5/256, kappa(beta) = 1 - 128 beta/5 for beta <= 5/256: (P1) for every real function a on the sites (zero at exterior sites), |<s_0^1 s_x^1 + s_0^2 s_x^2>| <= exp(a_x - a_0 + beta sum_b (cosh(a_y - a_z) - 1)), likewise for the other two component pairs, hence |<s_0 . s_x>| <= (3/2) times the same (proved; the complex-cosine identity, the modulus identity, the cosine-cosh inequality and the shift lemma on a trigonometric polynomial executed symbolically); (P2) the shift function a_y = gamma max(0, log((1+R)/(1+d(y)))) with R = d(x) has |a_y - a_z| <= gamma/(1 + min(d(y), d(z))) on every bond and sum_b (cosh(a_y - a_z) - 1) <= 2 gamma^2 cosh(gamma) (1 + 8 H_R) on every window containing {d < R} and on the torus (proved; the shell counts, the harmonic bound and the series inequality executed exactly); (P3) hence |<s_0 . s_x>| <= (3/2) e^{18 beta gamma^2 cosh gamma} (1 + R)^{-(gamma - 16 beta gamma^2 cosh gamma)}, and with gamma = min(1, 5/(256 beta)) and cosh 1 <= 8/5: |<s_0 . s_x>| <= (3/2) e^{9/16} (1 + d(x))^{-kappa(beta)}, uniformly in the window, the exterior records and the side (proved; the constants executed exactly); (P4) on the torus M_N^2 <= 6 e^{9/16} (1 + L)^{-min(kappa, 1)} + 1/(4 L^2), every infinite-volume static law on the plane, should one exist, has |<s_0 . s_x>| <= (3/2) e^{9/16} (1 + |x|)^{-kappa(beta)}, and no kernel with a coupling-independent power law — in particular no Green-function-type kernel — exists on planes at any coupling (proved; the torus sum executed). Two standard mathematical imports named at definition level; no coupling, reading or rule is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.py
---

# On a plane the unsoldered sphere static law's correlations decay at least as a power with a coupling-dependent exponent, at every coupling: complex rotations with explicit constants, the order parameter's rate upgraded to a power of the side, and no Green-function-type kernel on planes

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Block 20 (PR #8154) shows the unsoldered sphere static law never orders on
a plane, but says nothing about how its correlations fall off, and its rate
for the order parameter is a bare inverse logarithm of the side. This note
supplies the rate. On any plane window, with any exterior records, and on the
plane torus:
```
|⟨s_0·s_x⟩| ≤ (3/2) e^{9/16} (1 + d(x))^{−κ(β)},   κ(β) = 5/(512β) for β ≥ 5/256,  κ(β) = 1 − 128β/5 ≥ 1/2 for β ≤ 5/256.
```
A power law, with an exponent that shrinks as the coupling grows but never
vanishes, uniform in the window and the side. On the torus this gives
`M_N² ≤ 6e^{9/16}(1 + L)^{−min(κ,1)} + 1/(4L²)`, a power of the side where
block 20 had `(log L)^{−1/2}`; every infinite-volume static law on the plane,
should one exist, decays the same way; and since the exponent depends on `β`
while a Green-function kernel's would be fixed by the dimension, no such
kernel exists on planes at any coupling — the counterpart of block 19's
channel on `Z³`.

The mechanism is the complex rotation. Write each record as
`(ρ cos φ, ρ sin φ, ζ)`; the correlation of the first two components is the
real part of `⟨ρ_0ρ_x e^{i(φ_0 − φ_x)}⟩`; shift every angle `φ_y` by `i a_y`
with a real `a_y`, which leaves each period integral unchanged; the
observable picks up `e^{a_x − a_0}` and each bond weight's modulus grows by
at most `e^{β(cosh(a_y − a_z) − 1)}`. With `a_y = γ log((1+R)/(1+d(y)))`
inside the disc of radius `R = d(x)` and zero outside, the observable gives
`(1+R)^{−γ}`, and the bond sum is a discrete Dirichlet energy of a logarithm,
of order `γ² log R`. Optimizing `γ` gives the power law. The constants are
the crude ones of this route; the true decay is faster and is not claimed.

Exactly: P1 (the shift bound); P2 (the shift function: `|a_y − a_z| ≤
γ/(1 + min(d(y), d(z)))`, `Σ_b(cosh(a_y − a_z) − 1) ≤ 2γ²cosh γ(1 + 8H_R)`);
P3 (the rate with `γ = min(1, 5/(256β))`); P4 (the torus, the infinite-volume
laws, the placement). Executed with exact arithmetic: 20 checks, 13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the derivation campaign's gravity node (#8093): blocks 19-22 (PRs #8153-#8156) locate its kernel in the ordered unsoldered static law on Z^3 with the coupling window [sqrt(3)/6, 76/100] and show it needs the third dimension; what replaces it on a plane"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "on planes the record correlations decay at least as (1 + d)^{-kappa(beta)} with kappa(beta) = 5/(512 beta) above beta = 5/256, uniformly in the window and the side: a coupling-dependent power law, so no Green-function-type kernel on planes at any coupling; block 20's order-parameter rate upgraded to a power of the side. Open: the true decay (faster; not claimed); the normalization on Z^3; the band. Consumers: #8093's assembly (the dimension placement with a rate); the campaign's queue"
conditional_surface_status: "P1-P4 proved for every beta > 0 on every finite plane window containing the disc {d < R} with any exterior records, on tori of even side, and for every infinite-volume static law on the plane should one exist; the algebraic skeleton executed exactly (the identities, the shell counts, the series inequality, the constants, the torus sum); conditional on the sphere as the possibility domain, the unsoldered and static readings and the exponential overlap as supplied conditions; two standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "Each site has a domain of local possibilities.", "No possibility is privileged.", "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", and "Records form.". The landed possibility-covariance note (`docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md`, section "Empty-neighbourhood sphere laws") supplies the pure-state sphere `S²` as the possibility domain and the unsoldered reading. Block 01 (on `main`) supplies the static reading of finite windows with exterior records; the plane is the coordinate sublattice `Z²` of the Lattice axiom's `Z³`, with the window convention of blocks 12, 17 and 20 (no records outside the window). All proposed and unaudited; blocks 19 and 20 (PRs #8153, #8154, open) are referenced under Prior art as evidence addresses for the placement.

Declared objects.
- **Coordinates on the sphere.** `s = (ρ cos φ, ρ sin φ, ζ)` with `ζ ∈ [−1, 1]`, `ρ = (1 − ζ²)^{1/2}`, `φ ∈ [0, 2π)`; the uniform surface measure is `dσ = dζ dφ` (the area-preserving cylindrical projection, named under Imports). For records `s, s'`: `s·s' = ρρ' cos(φ − φ') + ζζ'`.
- **Windows and the torus.** A finite `Λ ⊂ Z²` with exterior records `ω` on the sites adjacent to `Λ`; the bonds `b = ⟨yz⟩` are the nearest-neighbour pairs with at least one endpoint in `Λ`; `μ_Λ^ω(ds_Λ) ∝ Π_b e^{β s_y·s_z} Π_{y∈Λ} dσ(s_y)` with `s_z = ω_z` at exterior endpoints. The torus law on `(Z/2LZ)²`, `N = 4L²`, as in block 20. `⟨·⟩` denotes either expectation.
- **Distances.** `d(y) = |y|` (Euclidean) on `Z²`; `d(y) = d_T(0, y)` (the torus Euclidean distance, `(d_1² + d_2²)^{1/2}` with `d_i = min(|y_i|, 2L − |y_i|)`) on the torus. Both are `1`-Lipschitz along bonds and dominate the sup-norm distance `d_∞`.
- **Shells.** `{y : d_∞(y) = j}` has `8j` sites on `Z²` for `j ≥ 1`, and on the torus `8j` sites for `j < L` and `4L − 1 ≤ 8L` for `j = L` (block 20's count).
- **Constants.** `H_R = Σ_{j=1}^R 1/j`; `κ(β)` as in the claim scope; `C_1 = (3/2)e^{9/16}`; `M_N² = N^{−2}⟨|Σ_x s_x|²⟩` on the torus.

## Prior art and what is new

The complex-rotation bound is McBryan and Spencer's (1977) for the `O(N)` models on `Z²`, giving power-law decay at every temperature; Fröhlich and Spencer, and Fröhlich and Pfister, refined it; the sharp low-temperature behaviour of the two-component model is the Kosterlitz–Thouless picture (not used). On `main`, block 20 proves the absence of long-range order on planes by the zero-field inequality with the rate `(log L)^{−1/2}`; the quantum no-order notes give no rate. What is new here: (i) the route re-proved at scope for this record law, on finite windows with exterior records and on the torus, with every constant explicit (`κ(β) = 5/(512β)`, prefactor `(3/2)e^{9/16}`); (ii) the torus consequence upgrading block 20's rate for `M_N²` to a power of the side; (iii) the decay for every infinite-volume static law on the plane; (iv) the placement: the exponent depends on `β`, so no Green-function-type kernel on planes, the rate-level counterpart of block 20's dimension placement.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| P1 | the complex-shift bound for any real `a` | the complex cosine; the modulus; `cos φ cosh a ≤ cos φ + (cosh a − 1)`; the shift lemma | B |
| P2 | the shift function's Lipschitz bound and the bond sum `≤ 2γ²cosh γ(1 + 8H_R)` | the mean value bound for `log(1+t)`; sup-norm shells; `cosh t − 1 ≤ (t²/2)cosh t` | B, C |
| P3 | the rate with explicit `κ(β)` and prefactor | `H_R ≤ 1 + log R`; `cosh 1 ≤ 8/5`; the optimization of `γ` | C, D |
| P4 | the torus bound; infinite-volume laws; the placement | shells again; the DLR property | D, E |

## Theorem P1 — the complex-shift bound

**Statement.** Let `Λ` be a finite plane window with exterior records `ω` (or the torus), `0, x ∈ Λ`, and `a` any real function on the sites with `a_z = 0` at exterior sites. Then
```
|⟨s_0^1 s_x^1 + s_0^2 s_x^2⟩| ≤ exp( a_x − a_0 + β Σ_b (cosh(a_y − a_z) − 1) ),
```
the sum over all bonds meeting `Λ`; the same bound holds for the component pairs `(2, 3)` and `(1, 3)`; hence `|⟨s_0·s_x⟩| ≤ (3/2) exp(a_x − a_0 + β Σ_b (cosh(a_y − a_z) − 1))`.

**Proof.** (i) *The observable.* `s_0^1 s_x^1 + s_0^2 s_x^2 = ρ_0ρ_x cos(φ_0 − φ_x) = Re[ρ_0ρ_x e^{i(φ_0 − φ_x)}]`, so it suffices to bound `|⟨ρ_0ρ_x e^{i(φ_0 − φ_x)}⟩|`. (ii) *The shift.* Fix all variables but one angle `φ_y`, `y ∈ Λ`. The integrand — the observable times `Π_b e^{β[ρ_yρ_z cos(φ_y − φ_z) + ζ_yζ_z]}` — is an entire, `2π`-periodic function of `φ_y`, so its integral over a period is unchanged when `φ_y` is replaced by `φ_y + i a_y` (the shift lemma, named under Imports: integrate around the rectangle with vertices `0, 2π, 2π + ia_y, ia_y`; the vertical sides cancel by periodicity). Do this for every `y ∈ Λ`. (iii) *Moduli.* `cos(θ + iτ) = cos θ cosh τ − i sin θ sinh τ`, so for real `c`, `|e^{c cos(θ + iτ)}| = e^{c cos θ cosh τ}`; and `cos θ cosh τ − cos θ − (cosh τ − 1) = −(1 − cos θ)(cosh τ − 1) ≤ 0`, so `cos θ cosh τ ≤ cos θ + (cosh τ − 1)`. On a bond, `c = βρ_yρ_z ≥ 0` with `ρ_yρ_z ≤ 1`, hence `|e^{βρ_yρ_z cos(φ_y − φ_z + i(a_y − a_z))}| ≤ e^{βρ_yρ_z cos(φ_y − φ_z)} e^{β(cosh(a_y − a_z) − 1)}`; the factors `e^{βζ_yζ_z}` are untouched; at an exterior endpoint `a_z = 0` and `φ_z` is the exterior record's angle. The observable becomes `ρ_0ρ_x e^{i(φ_0 − φ_x)} e^{−(a_0 − a_x)}`, of modulus at most `e^{a_x − a_0}`. (iv) *Assemble.* The shifted integral has modulus at most `e^{a_x − a_0} e^{βΣ_b(cosh(a_y − a_z) − 1)}` times the unshifted weight integrated, i.e. times `Z`; dividing by `Z` gives the bound. (v) *The other pairs and the sum.* Rotating the roles of the components gives the same bound for `⟨s^2s^2 + s^3s^3⟩` and `⟨s^1s^1 + s^3s^3⟩`, and `2 s_0·s_x` is the sum of the three pair sums. ∎

Executed: the complex-cosine identity and the modulus, the inequality `(1 − cos θ)(cosh τ − 1) ≥ 0`, and the shift lemma on the trigonometric polynomial `(Σ_{m≤4}(c cos φ)^m/m!) e^{iφ}`, whose period integral `πc(c² + 8)/8` is nonzero (B1–B2, B4).

## Theorem P2 — the shift function and the bond sum

**Statement.** Let `R = d(x) ≥ 1`, `γ > 0`, and `a_y = γ max(0, log((1+R)/(1+d(y))))` for every site `y` (exterior sites included), on a window `Λ ⊇ {y : d(y) < R}` or on the torus. Then (a) `a_0 = γ log(1+R)`, `a_x = 0`, and `a_z = 0` at every exterior site; (b) on every bond, `|a_y − a_z| ≤ γ/(1 + min(d(y), d(z))) ≤ γ`, and `a_y = a_z = 0` unless `min(d(y), d(z)) < R`; (c) `Σ_b (cosh(a_y − a_z) − 1) ≤ 2γ² cosh γ (1 + 8H_R)`.

**Proof.** (a) `d(0) = 0`, `d(x) = R`; exterior sites of a window containing `{d < R}` have `d ≥ R`, where the formula gives `0`. (b) `t ↦ γ max(0, log((1+R)/(1+t)))` is nonincreasing, and for `p, q ≥ 0`, `|log(1+p) − log(1+q)| ≤ |p − q|/(1 + min(p, q))` (the derivative of `log(1+t)` is `1/(1+t)`, at most `1/(1 + min(p,q))` on the segment); `max(0, ·)` is `1`-Lipschitz; and `|d(y) − d(z)| ≤ 1` on a bond. If both `d(y), d(z) ≥ R` both values are `0`. (c) For `|t| ≤ γ`, `cosh t − 1 ≤ (t²/2) cosh t ≤ (t²/2) cosh γ`: the coefficient of `t^{2k}` in `cosh t − 1` is `1/(2k)!` and in `(t²/2)cosh t` is `1/(2(2k−2)!)`, with ratio `2/((2k)(2k−1)) ≤ 1` for `k ≥ 1`. Hence `Σ_b (cosh(a_y − a_z) − 1) ≤ (γ² cosh γ/2) Σ_{b : m_b < R} 1/(1 + m_b)²`, `m_b = min(d(y), d(z))`. Since `1/(1+m_b)² ≤ 1/(1+d(y))² + 1/(1+d(z))²`, and a bond with `m_b < R` has both endpoints at `d < R + 1`, and each site lies on at most four bonds, `Σ_{b : m_b < R} 1/(1+m_b)² ≤ 4 Σ_{y : d(y) < R+1} 1/(1 + d(y))²`. Group the sites by `j = d_∞(y)`: the origin contributes `1`; the shell `j ≥ 1` has at most `8j` sites (on the torus too), each with `d(y) ≥ j`, and only shells with `j < R + 1`, i.e. `j ≤ R`, contain sites with `d < R + 1`; so the sum is at most `1 + Σ_{j=1}^R 8j/(1+j)² ≤ 1 + 8H_R`. Multiply: `(γ²cosh γ/2) · 4(1 + 8H_R) = 2γ²cosh γ(1 + 8H_R)`. ∎

Executed: the series ratios (B3); the mean value bound (C1); the shell counts on `Z²` and on the torus and `Σ_{j≤R} 8j/(1+j)² ≤ 8H_R` for `R ≤ 60` (C1).

## Theorem P3 — the rate

**Statement.** In the setting of P2, for every `γ > 0`:
```
|⟨s_0·s_x⟩| ≤ (3/2) exp(18βγ² cosh γ) (1 + R)^{−(γ − 16βγ² cosh γ)}.
```
With `γ = min(1, 5/(256β))`: `|⟨s_0·s_x⟩| ≤ (3/2) e^{9/16} (1 + d(x))^{−κ(β)}` for every `β > 0`, where `κ(β) = 5/(512β)` for `β ≥ 5/256` and `κ(β) = 1 − 128β/5 ≥ 1/2` for `β ≤ 5/256`.

**Proof.** P1 with P2: the exponent is at most `−γ log(1+R) + 2βγ²cosh γ(1 + 8H_R)`, and `H_R ≤ 1 + log R ≤ 1 + log(1+R)` (for `j ≥ 2`, `1/j ≤ ∫_{j−1}^{j} dt/t`, because `log(1 + u) ≥ u/(1+u)` at `u = 1/(j−1)`), so the exponent is at most `18βγ²cosh γ − (γ − 16βγ²cosh γ) log(1+R)`. For the constants: `e ≥ 1 + 1 + 1/2 + 1/6 = 8/3` and `e ≤ 65/24 + Σ_{k≥5} 1/k! ≤ 65/24 + (1/120)(1 + 1/6 + 1/36 + …) = 65/24 + 1/100 ≤ 11/4`, so `cosh 1 = (e + 1/e)/2 ≤ (11/4 + 3/8)/2 = 25/16 ≤ 8/5`; for `γ ≤ 1`, `cosh γ ≤ 8/5`. If `β ≥ 5/256`, take `γ = 5/(256β) ≤ 1`: the exponent's coefficient is at least `γ − (128/5)βγ² = 5/(512β)` (the maximum of `γ − (128/5)βγ²`, attained at `γ = 5/(256β)`), and the prefactor's exponent is at most `(144/5)βγ² = 45/(4096β) ≤ 9/16`. If `β ≤ 5/256`, take `γ = 1`: the coefficient is at least `1 − (128/5)β ≥ 1/2` and the prefactor's exponent at most `(144/5)β ≤ 9/16`. ∎

Executed: the harmonic bound's ingredient (C2); the `e` bounds and `cosh 1 ≤ 8/5` (D1); the optimization and the two branches (D2, D4).

## Theorem P4 — the torus, the infinite-volume laws, and the placement

**Statement.** (a) On the torus `(Z/2LZ)²`, for every `β > 0` and `L ≥ 1`, with `κ' = min(κ(β), 1)`: `M_N² ≤ 6e^{9/16}(1 + L)^{−κ'} + 1/(4L²)`. (b) Every infinite-volume static law `ν` on `Z²` (a probability measure whose conditional law on every finite window given the exterior records is `μ_Λ^ω`), should one exist, satisfies `|⟨s_0·s_x⟩_ν| ≤ (3/2)e^{9/16}(1 + |x|)^{−κ(β)}` for every `x ≠ 0`; in particular `⟨s_0·s_x⟩_ν → 0` as `|x| → ∞`. (c) On planes the record correlations decay, at every `β > 0`, at least as a power whose exponent depends on `β`; a kernel of Green-function type has a power fixed by the dimension (or, in two dimensions, grows logarithmically); hence no Green-function-type kernel exists in the plane's record correlations at any coupling, in contrast with block 19's channel on `Z³`.

**Proof.** (a) By translation invariance `M_N² = N^{−1}Σ_x ⟨s_0·s_x⟩`; the term `x = 0` is `1`; for `x ≠ 0`, P3 with `R = d_T(0, x) ≥ d_∞(x) = j` gives `⟨s_0·s_x⟩ ≤ C_1(1+j)^{−κ'}` (a smaller exponent only weakens the bound). Grouping by shells, `Σ_{x≠0} ⟨s_0·s_x⟩ ≤ C_1 Σ_{j=1}^{L} 8j(1+j)^{−κ'} ≤ 8C_1 L(1+L)^{1−κ'}`, since for `κ' ≤ 1` and `j ≤ L`, `j(1+j)^{−κ'} ≤ (1+j)^{1−κ'} ≤ (1+L)^{1−κ'}`. With `N = 4L²`: `M_N² ≤ 1/(4L²) + 2C_1(1+L)^{1−κ'}/L ≤ 1/(4L²) + 4C_1(1+L)^{−κ'}`, using `(1+L)/L ≤ 2`; and `4C_1 = 6e^{9/16}`. (b) Take `Λ ⊇ {y : |y| < |x| + 1}` finite; by the defining property, `⟨s_0·s_x⟩_ν = ∫ ν(dω) ⟨s_0·s_x⟩_Λ^ω`, and P3 bounds the integrand uniformly in `ω`. (c) is the reading of P3 and (b) against block 19's G5 (a lower bound `(M²/3)²/(βE(k))` on `Z³`, whose real-space form is a fixed power), cited as an evidence address. ∎

Executed: the shell sum inequality at `κ' = 1/2` and `κ' = 1` for `L ≤ 40` (D3); the chain identity of the solvable two-site instance and P1's bound there (E1).

## No-Go Discipline Gate

The negative sentence is P4(c): no Green-function-type kernel on planes at any coupling. Its escapes are named, not closed: the constants are not sharp and the true decay is faster (nothing about the true rate is claimed); the third dimension (block 19); other overlaps (the Born overlap is not treated).

### N1 — Routes by which P4(c) could fail
1. *The shift lemma fails for the weight* — closed: the integrand is entire and periodic in each angle; executed on a trigonometric polynomial with a nonzero integral (B4), the general case by the named lemma.
2. *The modulus step for bonds to exterior records* — closed: `a_z = 0` there and the identity holds with `τ = a_y` (P1 iii).
3. *The Lipschitz bound of the shift function on the torus* — closed: `d_T` is `1`-Lipschitz along bonds; the shells have at most `8j` sites (C1).
4. *The bond sum's constant* — closed: the series inequality and the shell sum executed (B3, C1).
5. *The optimization or the `e` bounds* — closed: executed exactly (D1–D2, D4).
6. *A faster true decay, `d = 3`, other overlaps* — escapes, named above.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, the parent note's sphere law and reading, block 01's static reading, and the supplied overlap.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the five sentences under Premises | yes (premise) |
| the possibility-covariance note (`main`) | the sphere domain and the unsoldered reading | yes (premise, proposed) |
| block 01 (`main`) | the static reading | yes (premise, proposed) |
| block 20 (PR #8154) | the rate it is compared with; the torus shell count | comparison only (evidence address) |
| block 19 (PR #8153) | the channel on `Z³`, for P4(c) | P4(c) only (evidence address) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no Green-function-type kernel on planes" | executed: the complex-cosine identity; the modulus; the cosine-cosh inequality; the series ratios | executed: the shift lemma on a trigonometric polynomial; the mean value bound | executed: the shell counts on `Z²` and the torus; `Σ 8j/(1+j)² ≤ 8H_R` to `R = 60` | executed: the `e` bounds; the optimization; the two branches; the torus sum at two exponents | proved for every `β > 0` on every window containing the disc, on tori and for infinite-volume laws (P1–P4); the true rate not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or overlap; none is a wall.

### N7 — Steelman
Hostile reviewer: "This is the 1977 theorem with worse constants; the exponent `5/(512β)` is absurdly small, and the three-component model actually decays exponentially on the plane." Reply: the framework question is the rate-level counterpart of block 20's dimension placement — what the plane's record correlations do where `Z³` carries the kernel — and the answer needed a volume-uniform bound with explicit constants at scope; the exponent's dependence on `β`, not its size, is what excludes a Green-function-type kernel. Conceded: the constants are crude and the true decay is faster; neither is claimed.

### N8 — Cross-cycle echo
Block 20's zero-field route gave the absence of order with a logarithmic rate; this route gives a power law by a different mechanism (complex rotations rather than the sum rule); block 17's discrete law orders on the plane, so the continuous menu is again the cause; block 19's channel on `Z³` is the object whose absence on planes is now quantified.

## Falsifiers
- A failure of `cos(φ + ia) = cos φ cosh a − i sin φ sinh a`, of the modulus identity, of `cos φ + cosh a − 1 − cos φ cosh a = (1 − cos φ)(cosh a − 1)`, or of the shift lemma on the trigonometric polynomial (B1–B2, B4); a coefficient ratio other than `2/((2k)(2k−1))` (B3).
- A shell of `Z²` or of the torus with more than `8j` sites, or `Σ_{j≤R} 8j/(1+j)² > 8H_R` for some `R ≤ 60` (C1); a failure of the mean value bound's derivative identity or of `log(1+u) ≥ u/(1+u)` (C1–C2).
- `e < 8/3`, `65/24 + 1/100 > 11/4`, or `(11/4 + 3/8)/2 > 8/5` (D1); a maximizer other than `5/(256β)` or a maximum other than `5/(512β)`, or a prefactor exponent above `9/16` on either branch (D2, D4); the shell sum inequality failing at `κ' = 1/2` or `1` (D3).
- The two-site instance's `⟨s_0·s_1⟩ ≠ coth β − 1/β`, or P1's bound violated there for some shift (E1).

## Boundaries and non-claims
This note proves, for the unsoldered static law with the exponential overlap on a coordinate plane of the lattice, a volume-uniform power-law bound on the record correlations with an explicit coupling-dependent exponent, at every `β > 0`, on finite windows with exterior records, on tori and for infinite-volume static laws; it does not state the true rate of decay, does not claim the exponent is sharp, does not treat the Born overlap, does not re-prove blocks 19 or 20, does not select a reading, rule, coupling or dimension as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- The possibility-covariance note and block 01 (both on `main`): the readings and the object; proposed, unaudited. PRs #8153 and #8154 (open) referenced as evidence addresses for the placement only.
- Re-proved at scope: P1 (the complex cosine, the modulus, the cosine-cosh inequality, the assembly), P2 (the mean value bound, the shell sums, the series inequality), P3 (the harmonic bound, the `e` bounds, the optimization), P4 (the shell sum, the DLR step).
- Named standard imports at definition level (never as authority for physics): the shift lemma for the period integral of an entire `2π`-periodic function (Cauchy's theorem on a rectangle); the area-preserving cylindrical projection of the sphere (Archimedes), giving `dσ = dζ dφ`.
- Reference only (named, not used): McBryan–Spencer (1977); Fröhlich–Spencer (1981); Fröhlich–Pfister (1981); Kosterlitz–Thouless (1973).

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane at each conclusion; no subagents). The control (`specs/supervisor_control_block23_complex_rotations.py`) checked the identities, the Lipschitz bound of the shift function on a `81×81` patch (worst ratio `0.976` of the bound), the shell sums on `Z²` and on tori, the harmonic bound to `10⁵`, the `e` bounds, the optimization, and P1's inequality on the exactly solvable two- and three-site chains for `41` shift values at three couplings (tightest ratio `1.77`), before the contract; the lens pass is in `GOAL_block23.md`; the primary seat wrote P1–P4 and the runner; the refuting pass (`CHECKER_block23_findings.md`) checked the full shift bound numerically on a `4×4` window by direct quadrature of the angle integrals against the truth at two couplings, the shift function's bound on the torus with the torus distance, the harmonic-sum route through the integral test, and the optimization by a grid. Facts settled while executing: on the torus the shift function may be centred at `0` with `R = d_T(0, x)` up to `√2 L` because the sup-norm shells never exceed `8j` sites; exterior records need `Λ ⊇ {d < R}` so that the formula vanishes at exterior sites.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.py --mutation claim_plane_kernel_injected
```

Families: A authority and inputs; B the complex-shift identities, the series inequality and the shift lemma; C the shell counts and the harmonic bound; D the `e` bounds, the optimization, the torus sum and the small-coupling branch; E the solvable two-site instance; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
