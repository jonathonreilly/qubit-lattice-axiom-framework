---
claim_id: admissibility_rule_sphere_static_law_planar_complex_rotation_correlation_upper_bounds_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the supplied uniform-sphere exponential nearest-neighbour static model on independent Z^2: P1 proves the complex-shift inequality; P2 bounds the logarithmic shift energy by charging each active bond to a nearer endpoint; P3 gives an explicit correlation upper bound with exponent kappa(beta)>0; P4 gives the torus magnetization bound and the same correlation bound conditional on a DLR law. Windows must contain 0,x and every site with distance less than R=distance(x); tori have L>=2. No exact decay exponent, faster-power exclusion, gravity or dimension-selection claim is retained."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.py
---

# Sphere Static Law Planar Complex Rotation Correlation Upper Bounds

**Type:** bounded_theorem

**Status:** bounded-support; conditional supplied model; unaudited.

## Result up front

For the supplied uniform-sphere exponential nearest-neighbour static model on independent Z^2: P1 proves the complex-shift inequality; P2 bounds the logarithmic shift energy by charging each active bond to a nearer endpoint; P3 gives an explicit correlation upper bound with exponent kappa(beta)>0; P4 gives the torus magnetization bound and the same correlation bound conditional on a DLR law. Windows must contain 0,x and every site with distance less than R=distance(x); tori have L>=2. No exact decay exponent, faster-power exclusion, gravity or dimension-selection claim is retained.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Quantitative mathematical bounds for explicitly supplied sphere static models; no physical channel classification."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Original independent affected-source confirmation and bounded finite evidence capture; retained-grade audit remains separate."
conditional_surface_status: "For the supplied uniform-sphere exponential nearest-neighbour static model on independent Z^2: P1 proves the complex-shift inequality; P2 bounds the logarithmic shift energy by charging each active bond to a nearer endpoint; P3 gives an explicit correlation upper bound with exponent kappa(beta)>0; P4 gives the torus magnetization bound and the same correlation bound conditional on a DLR law. Windows must contain 0,x and every site with distance less than R=distance(x); tori have L>=2. No exact decay exponent, faster-power exclusion, gravity or dimension-selection claim is retained."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The linked repository context is [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md); [POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md). The possibility parent supplies conditional representation vocabulary; it does not select this probability law. We explicitly supply the uniform surface measure on S², beta>0, the exponential pair weight and the static specification. These are mathematical model premises, not consequences selecting physics from the axioms. The independent d-dimensional nearest-neighbour model omits all couplings outside that dimension; a two-dimensional model is not the marginal of a plane in an interacting three-dimensional model. All torus claims below use L>=2 (side at least four), so neighbours are distinct.

Declared objects.
- **Coordinates on the sphere.** `s = (ρ cos φ, ρ sin φ, ζ)` with `ζ ∈ [−1, 1]`, `ρ = (1 − ζ²)^{1/2}`, `φ ∈ [0, 2π)`; the uniform surface measure is `dσ = dζ dφ` (the area-preserving cylindrical projection, named under Imports). For records `s, s'`: `s·s' = ρρ' cos(φ − φ') + ζζ'`.
- **Windows and the torus.** A finite `Λ ⊂ Z²` with exterior records `ω` on the sites adjacent to `Λ`; the bonds `b = ⟨yz⟩` are the nearest-neighbour pairs with at least one endpoint in `Λ`; `μ_Λ^ω(ds_Λ) ∝ Π_b e^{β s_y·s_z} Π_{y∈Λ} dσ(s_y)` with `s_z = ω_z` at exterior endpoints. The torus law on `(Z/2LZ)²`, `N = 4L²`, with each positive-coordinate bond counted once and L ≥ 2. `⟨·⟩` denotes either expectation.
- **Distances.** `d(y) = |y|` (Euclidean) on `Z²`; `d(y) = d_T(0, y)` (the torus Euclidean distance, `(d_1² + d_2²)^{1/2}` with `d_i = min(|y_i|, 2L − |y_i|)`) on the torus. Both are `1`-Lipschitz along bonds and dominate the sup-norm distance `d_∞`.
- **Shells.** `{y : d_∞(y) = j}` has `8j` sites on `Z²` for `j ≥ 1`, and on the torus `8j` sites for `j < L` and `4L − 1 ≤ 8L` for `j = L`.
- **Constants.** `H_R = Σ_{j=1}^{floor(R)} 1/j`; `κ(β)` as in the claim scope; `C_1 = (3/2)e^{9/16}`; `M_N² = N^{−2}⟨|Σ_x s_x|²⟩` on the torus.



## Prior art and what is new


The complex-rotation bound is McBryan and Spencer's (1977) for the `O(N)` models on `Z²`, giving power-law decay at every temperature; Fröhlich and Spencer, and Fröhlich and Pfister, refined it; the sharp low-temperature behaviour of the two-component model is the Kosterlitz–Thouless picture (not used).  The contribution retained here is the explicit mathematical bounds for the supplied model. No comparison with physical channels is used.

## Theorem P1 — the complex-shift bound

**Statement.** Let `Λ` be a finite plane window with exterior records `ω` (or the torus), `0, x ∈ Λ`, and `a` any real function on the sites with `a_z = 0` at exterior sites. Then
```
|⟨s_0^1 s_x^1 + s_0^2 s_x^2⟩| ≤ exp( a_x − a_0 + β Σ_b (cosh(a_y − a_z) − 1) ),
```
the sum over all bonds meeting `Λ`; the same bound holds for the component pairs `(2, 3)` and `(1, 3)`; hence `|⟨s_0·s_x⟩| ≤ (3/2) exp(a_x − a_0 + β Σ_b (cosh(a_y − a_z) − 1))`.

**Proof.** (i) *The observable.* `s_0^1 s_x^1 + s_0^2 s_x^2 = ρ_0ρ_x cos(φ_0 − φ_x) = Re[ρ_0ρ_x e^{i(φ_0 − φ_x)}]`, so it suffices to bound `|⟨ρ_0ρ_x e^{i(φ_0 − φ_x)}⟩|`. (ii) *The shift.* Fix all variables but one angle `φ_y`, `y ∈ Λ`. The integrand — the observable times `Π_b e^{β[ρ_yρ_z cos(φ_y − φ_z) + ζ_yζ_z]}` — is an entire, `2π`-periodic function of `φ_y`, so its integral over a period is unchanged when `φ_y` is replaced by `φ_y + i a_y` (the shift lemma, named under Imports: integrate around the rectangle with vertices `0, 2π, 2π + ia_y, ia_y`; the vertical sides cancel by periodicity). Do this for every `y ∈ Λ`. (iii) *Moduli.* `cos(θ + iτ) = cos θ cosh τ − i sin θ sinh τ`, so for real `c`, `|e^{c cos(θ + iτ)}| = e^{c cos θ cosh τ}`; and `cos θ cosh τ − cos θ − (cosh τ − 1) = −(1 − cos θ)(cosh τ − 1) ≤ 0`, so `cos θ cosh τ ≤ cos θ + (cosh τ − 1)`. On a bond, `c = βρ_yρ_z ≥ 0` with `ρ_yρ_z ≤ 1`, hence `|e^{βρ_yρ_z cos(φ_y − φ_z + i(a_y − a_z))}| ≤ e^{βρ_yρ_z cos(φ_y − φ_z)} e^{β(cosh(a_y − a_z) − 1)}`; the factors `e^{βζ_yζ_z}` are untouched; at an exterior endpoint `a_z = 0` and `φ_z` is the exterior record's angle. The observable becomes `ρ_0ρ_x e^{i(φ_0 − φ_x)} e^{−(a_0 − a_x)}`, of modulus at most `e^{a_x − a_0}`. (iv) *Assemble.* The shifted integral has modulus at most `e^{a_x − a_0} e^{βΣ_b(cosh(a_y − a_z) − 1)}` times the unshifted weight integrated, i.e. times `Z`; dividing by `Z` gives the bound. (v) *The other pairs and the sum.* Rotating the roles of the components gives the same bound for `⟨s^2s^2 + s^3s^3⟩` and `⟨s^1s^1 + s^3s^3⟩`, and `2 s_0·s_x` is the sum of the three pair sums. ∎

Executed: the complex-cosine identity and the modulus, the inequality `(1 − cos θ)(cosh τ − 1) ≥ 0`, and the shift lemma on the trigonometric polynomial `(Σ_{m≤4}(c cos φ)^m/m!) e^{iφ}`, whose period integral `πc(c² + 8)/8` is nonzero (B1–B2, B4).

## Theorem P2 — the shift function and the bond sum

**Statement.** Let `R = d(x) ≥ 1`, `γ > 0`, and `a_y = γ max(0, log((1+R)/(1+d(y))))` for every site `y` (exterior sites included), on a window with `0,x ∈ Λ` and `Λ ⊇ {y : d(y) < R}` or on the torus. Then (a) `a_0 = γ log(1+R)`, `a_x = 0`, and `a_z = 0` at every exterior site; (b) on every bond, `|a_y − a_z| ≤ γ/(1 + min(d(y), d(z))) ≤ γ`, and `a_y = a_z = 0` unless `min(d(y), d(z)) < R`; (c) `Σ_b (cosh(a_y − a_z) − 1) ≤ 2γ² cosh γ (1 + 8H_R)`.

**Proof.** (a) `d(0) = 0`, `d(x) = R`; exterior sites of a window containing `{d < R}` have `d ≥ R`, where the formula gives `0`. (b) `t ↦ γ max(0, log((1+R)/(1+t)))` is nonincreasing, and for `p, q ≥ 0`, `|log(1+p) − log(1+q)| ≤ |p − q|/(1 + min(p, q))` (the derivative of `log(1+t)` is `1/(1+t)`, at most `1/(1 + min(p,q))` on the segment); `max(0, ·)` is `1`-Lipschitz; and `|d(y) − d(z)| ≤ 1` on a bond. If both `d(y), d(z) ≥ R` both values are `0`. (c) For `|t| ≤ γ`, `cosh t − 1 ≤ (t²/2) cosh t ≤ (t²/2) cosh γ`: the coefficient of `t^{2k}` in `cosh t − 1` is `1/(2k)!` and in `(t²/2)cosh t` is `1/(2(2k−2)!)`, with ratio `2/((2k)(2k−1)) ≤ 1` for `k ≥ 1`. Hence `Σ_b (cosh(a_y − a_z) − 1) ≤ (γ² cosh γ/2) Σ_{b : m_b < R} 1/(1 + m_b)²`, `m_b = min(d(y), d(z))`. Charge each active bond to one endpoint attaining the smaller distance `m_b<R` (choose either endpoint for a tie). Each site receives at most four bonds. Thus `Σ_{b:m_b<R}(1+m_b)^{-2} ≤ 4Σ_{y:d(y)<R}(1+d(y))^{-2}`. The origin contributes one; the sup-norm shell `j≥1` has at most `8j` sites and `d(y)≥j`. Every charged site has `j<R`, so including all `1≤j≤floor(R)` only increases the sum. Consequently it is at most `1+Σ_{j=1}^{floor(R)}8j/(1+j)² ≤ 1+8H_R`. This charging applies to noninteger R as well as integer R. Multiply: `(γ²cosh γ/2) · 4(1 + 8H_R) = 2γ²cosh γ(1 + 8H_R)`. ∎

Executed: the series ratios (B3); the mean value bound (C1); the shell counts on `Z²` and on the torus and `Σ_{j≤R} 8j/(1+j)² ≤ 8H_R` for `R ≤ 60` (C1).

## Theorem P3 — the rate

**Statement.** In the setting of P2, for every `γ > 0`:
```
|⟨s_0·s_x⟩| ≤ (3/2) exp(18βγ² cosh γ) (1 + R)^{−(γ − 16βγ² cosh γ)}.
```
With `γ = min(1, 5/(256β))`: `|⟨s_0·s_x⟩| ≤ (3/2) e^{9/16} (1 + d(x))^{−κ(β)}` for every `β > 0`, where `κ(β) = 5/(512β)` for `β ≥ 5/256` and `κ(β) = 1 − 128β/5 ≥ 1/2` for `β ≤ 5/256`.

**Proof.** P1 with P2: the exponent is at most `−γ log(1+R) + 2βγ²cosh γ(1 + 8H_R)`, and `H_R ≤ 1 + log R ≤ 1 + log(1+R)` (for `j ≥ 2`, `1/j ≤ ∫_{j−1}^{j} dt/t`, because `log(1 + u) ≥ u/(1+u)` at `u = 1/(j−1)`), so the exponent is at most `18βγ²cosh γ − (γ − 16βγ²cosh γ) log(1+R)`. For the constants: `e ≥ 1 + 1 + 1/2 + 1/6 = 8/3` and `e ≤ 65/24 + Σ_{k≥5} 1/k! ≤ 65/24 + (1/120)(1 + 1/6 + 1/36 + …) = 65/24 + 1/100 ≤ 11/4`, so `cosh 1 = (e + 1/e)/2 ≤ (11/4 + 3/8)/2 = 25/16 ≤ 8/5`; for `γ ≤ 1`, `cosh γ ≤ 8/5`. If `β ≥ 5/256`, take `γ = 5/(256β) ≤ 1`: the exponent's coefficient is at least `γ − (128/5)βγ² = 5/(512β)` (the maximum of `γ − (128/5)βγ²`, attained at `γ = 5/(256β)`), and the prefactor's exponent is at most `(144/5)βγ² = 45/(4096β) ≤ 9/16`. If `β ≤ 5/256`, take `γ = 1`: the coefficient is at least `1 − (128/5)β ≥ 1/2` and the prefactor's exponent at most `(144/5)β ≤ 9/16`. ∎

Executed: the harmonic bound's ingredient (C2); the `e` bounds and `cosh 1 ≤ 8/5` (D1); the optimization and the two branches (D2, D4).

## Theorem P4 — the torus, the infinite-volume laws

**Statement.** (a) On the torus `(Z/2LZ)²`, for every `β > 0` and `L ≥ 2`, with `κ' = min(κ(β), 1)`: `M_N² ≤ 6e^{9/16}(1 + L)^{−κ'} + 1/(4L²)`. (b) Every infinite-volume static law `ν` on `Z²` (a probability measure whose conditional law on every finite window given the exterior records is `μ_Λ^ω`), should one exist, satisfies `|⟨s_0·s_x⟩_ν| ≤ (3/2)e^{9/16}(1 + |x|)^{−κ(β)}` for every `x ≠ 0`; in particular `⟨s_0·s_x⟩_ν → 0` as `|x| → ∞`.

**Proof.** (a) By translation invariance `M_N² = N^{−1}Σ_x ⟨s_0·s_x⟩`; the term `x = 0` is `1`; for `x ≠ 0`, P3 with `R = d_T(0, x) ≥ d_∞(x) = j` gives `⟨s_0·s_x⟩ ≤ C_1(1+j)^{−κ'}` (a smaller exponent only weakens the bound). Grouping by shells, `Σ_{x≠0} ⟨s_0·s_x⟩ ≤ C_1 Σ_{j=1}^{L} 8j(1+j)^{−κ'} ≤ 8C_1 L(1+L)^{1−κ'}`, since for `κ' ≤ 1` and `j ≤ L`, `j(1+j)^{−κ'} ≤ (1+j)^{1−κ'} ≤ (1+L)^{1−κ'}`. With `N = 4L²`: `M_N² ≤ 1/(4L²) + 2C_1(1+L)^{1−κ'}/L ≤ 1/(4L²) + 4C_1(1+L)^{−κ'}`, using `(1+L)/L ≤ 2`; and `4C_1 = 6e^{9/16}`. (b) Take `Λ ⊇ {y : |y| < |x| + 1}` finite; by the defining property, `⟨s_0·s_x⟩_ν = ∫ ν(dω) ⟨s_0·s_x⟩_Λ^ω`, and P3 bounds the integrand uniformly in `ω`. ∎

Executed: the shell sum inequality at `κ' = 1/2` and `κ' = 1` for `L ≤ 40` (D3); the chain identity of the solvable two-site instance and P1's bound there (E1).

## No-Go Discipline Gate

Broad negative certification is withheld. The original five-route tables listed proof obligations and changes of scope rather than five independent attacks on the exact exclusion. They do not establish a negative certificate. Full original arguments remain available in the archive and original branches are retained. P4(c) is withdrawn: a coupling-dependent upper exponent does not exclude a faster fixed power. For example, (1+R)^(-2) satisfies every upper bound (1+R)^(-kappa) with 0<kappa<=1. The upper bound does not identify the true rate.

## Falsifiers
- A failure of `cos(φ + ia) = cos φ cosh a − i sin φ sinh a`, of the modulus identity, of `cos φ + cosh a − 1 − cos φ cosh a = (1 − cos φ)(cosh a − 1)`, or of the shift lemma on the trigonometric polynomial (B1–B2, B4); a coefficient ratio other than `2/((2k)(2k−1))` (B3).
- A shell of `Z²` or of the torus with more than `8j` sites, or `Σ_{j≤R} 8j/(1+j)² > 8H_R` for some `R ≤ 60` (C1); a failure of the mean value bound's derivative identity or of `log(1+u) ≥ u/(1+u)` (C1–C2).
- `e < 8/3`, `65/24 + 1/100 > 11/4`, or `(11/4 + 3/8)/2 > 8/5` (D1); a maximizer other than `5/(256β)` or a maximum other than `5/(512β)`, or a prefactor exponent above `9/16` on either branch (D2, D4); the shell sum inequality failing at `κ' = 1/2` or `1` (D3).
- The two-site instance's `⟨s_0·s_1⟩ ≠ coth β − 1/β`, or P1's bound violated there for some shift (E1).

## Boundaries and non-claims

For the supplied uniform-sphere exponential nearest-neighbour static model on independent Z^2: P1 proves the complex-shift inequality; P2 bounds the logarithmic shift energy by charging each active bond to a nearer endpoint; P3 gives an explicit correlation upper bound with exponent kappa(beta)>0; P4 gives the torus magnetization bound and the same correlation bound conditional on a DLR law. Windows must contain 0,x and every site with distance less than R=distance(x); tori have L>=2. No exact decay exponent, faster-power exclusion, gravity or dimension-selection claim is retained. This note does not select a physical reading, coupling, rule or dimension and adopts no clause.

No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The standard mathematical imports are stated explicitly; they supply mathematical tools, not physical selection.

## Imports
- Re-proved at scope: P1 (the complex cosine, the modulus, the cosine-cosh inequality, the assembly), P2 (the mean value bound, the shell sums, the series inequality), P3 (the harmonic bound, the `e` bounds, the optimization), P4 (the shell sum, the DLR step).
- Named standard imports at definition level (never as authority for physics): the shift lemma for the period integral of an entire `2π`-periodic function (Cauchy's theorem on a rectangle); the area-preserving cylindrical projection of the sphere (Archimedes), giving `dσ = dζ dφ`.
- Reference only (named, not used): McBryan–Spencer (1977); Fröhlich–Spencer (1981); Fröhlich–Pfister (1981); Kosterlitz–Thouless (1973).


## Review record

[Original recovery manifest](work_history/review_loop/pr8154/original-manifest.json) and [recovery instructions](work_history/review_loop/pr8154/README.md) preserve the complete original versions. The canonical execution address is [runner cache](../logs/runner-cache/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.txt); execution evidence must match the current source and declared inputs; historical caches are not restamped.

The original branch, full note, runner, cache, historical programs and outputs are preserved byte-exact in the recovery archive. Historical controls are evidence of their recorded finite domains, not a new execution or a proof of an infinite-lattice statement. The canonical primary retains its original twenty finite checks and thirteen mutation definitions; the historical mutation census is not a new review. The historical 4×4 refuter used heat-bath Monte Carlo with 6000 sweeps, 500 burn-in sweeps, free boundary and 24 bonds. It was not direct quadrature or a truth calculation, supplied no error analysis, and did not test arbitrary fixed exterior records.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.py --mutation claim_plane_kernel_injected
```

Families: A authority and inputs; B the complex-shift identities, the series inequality and the shift lemma; C the shell counts and the harmonic bound; D the `e` bounds, the optimization, the torus sum and the small-coupling branch; E the solvable two-site instance; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. The historical mutation census assigned each of the 13 declared mutations to one family; no new mutation census is claimed. Expected final line: `TOTAL: PASS=20 FAIL=0`.
