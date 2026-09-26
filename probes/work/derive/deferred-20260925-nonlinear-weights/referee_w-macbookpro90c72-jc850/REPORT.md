# Referee: nonlinear self-weighted laws, attempt 1

Attempt `w-jonathonsmac4f50-j7529`. The steered state and the chord obstruction are rebuilt here. The attempt's script is not imported.

The law gives the probability of outcome `+q` for a qubit of Bloch vector `r`. It is covariant, normalized on antipodes, and measurable on pure states. A partner qubit of one pure joint state uses the same law as its weight. After that record, the site is the steered pure state.

## Verdicts

**Geometry.** For every Bloch length `0 < ℓ < 1`, the state `√((1+ℓ)/2)|+x⟩|0⟩ + √((1−ℓ)/2)|−x⟩|1⟩` has Bloch vectors `ℓ x̂` and `ℓ ẑ`. The partner's `z` menu steers the site to `±x̂`. Its `y` menu, orthogonal to its own Bloch vector, steers the site to `(ℓ, ±√(1−ℓ²), 0)`, each with Born weight `1/2`. Those Born weights certify the state; the no-signalling average uses the law's own weights.

**Chords.** Antipodal normalization makes `H = h − 1/2` odd, and the radial average is `(2w−1) H`. Subtracting the two menus gives, for every direction `q`,
`(2w−1) H(x̂·q) = (1/2)[H(n₊·q) + H(n₋·q)]`.

**Harmonics.** Completeness of the spherical harmonics, so that a degree-`L` piece can be read off by itself, is imported. The circle formula
`P_L(cos ψ) = Σ_j C(2j,j) C(2(L−j), L−j) 4^{−L} cos((L−2j)ψ)`
is the classical expansion; it was checked for `L = 1..13`. The addition formula turns each cosine into a factor `cos(kβ)`. For odd `L`, the coefficients of `cos θ` and `cos 3θ` are twice a product of central binomials, hence positive. The identity was compared with `P_L` through degree 7.

**Exclusion.** If any degree `L ≥ 3` is present, both `cos β = 2w−1` and `cos 3β = 2w−1`. But `cos 3β − cos β = −2 sin(2β) sin β`, which is nonzero for `β ∈ (0, π/2)`. At `ℓ = 3/5` the two cosines are `3/5` and `−117/125`. So `H(c) = a₁ c` almost everywhere.

**Born or constant.** The degree-1 mode forces `2w−1 = ℓ` when `a₁ ≠ 0`, and the radial value at the pole forces `a₁ = 1/2`. Then `h(c) = (1+c)/2` and `f(ℓ, x) = (1+x)/2`. If `a₁ = 0`, both are the constant `1/2`. The endpoint condition `h(1) = 1` removes that constant. Continuity would drop the almost-everywhere qualifier.

**What the plane alone misses.** A pure triple angle, `H(cos θ) = cos 3θ`, satisfies the in-plane chord at `2w−1 = cos 3β`. The out-of-plane menus are what bring in the degree-1 piece of `P_3` and exclude it. On the affine family the radial chord alone forces `λ(λ−1) = 0`, while the perpendicular chord holds for every slope. The cubic `h = 1/2 + (3c−c³)/4` has no weight that satisfies both Fourier modes at `ℓ = 3/5`.

## What stays open

The floating-point tanh scan was not rebuilt. Laws with extra directional input, higher-dimensional sites, and a pointwise statement without measurability were not treated. The steering update is a premise. The replacement-rule countermodel was not rebuilt.

## Result

HIT: confirmed. At one Bloch length, the two partner menus force a measurable self-weighted qubit law to be Born or constant, and the endpoint condition removes the constant.
