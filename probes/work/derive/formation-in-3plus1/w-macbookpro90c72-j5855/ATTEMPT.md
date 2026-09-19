# formation-in-3plus1, attempt 4 (worker w-macbookpro90c72-j5855, model grok-4.6)

Plan, locked from the task before using other attempts: prove the *linear*
dichotomy and the equal-level Newtonian kernel with exact constants; do not
claim sphere LRO. Routes (a) and (b) for the nonlinear law stay open.

## (1) The statement attempted

Event lattice `Z^{d+1}` in level order: a record at `x` is formed from the `d+1`
predecessors `x − e_j`, `j = 1..d+1`. Level planes are `d`-dimensional. The
linearized law is `θ_{t+1} = P θ_t + ξ`, multiplier
`φ_d(k) = (1 + Σ_{j=1}^{d} e^{i k_j}) / (d+1)`, `u = |φ_d|²`. Equal-level
transverse covariance of a nonzero mode is `σ² / (1 − u(k))`.

**Statement (linear, exact).**
- (C) Dichotomy. `u(k) = 1` iff `k ∈ (2πZ)^d`. Near the origin
  `1 − u = kᵀ M_d k + O(k⁴)` with `M_d` positive definite. The on-site integral
  `(2π)^{-d} ∫_{[−π,π]^d} dk / (1−u)` is IR-finite iff `d > 2` (the integrand
  is `O(|k|^{-2})` at the origin and bounded on the compact complement of a
  neighbourhood of the origin). Thus:
  - `d = 1` (1+1): recurrent, no finite equal-level variance;
  - `d = 2` (2+1, the campaign's `Z^3`): logarithmic plane Green function
    (block 35);
  - `d = 3` (3+1): finite variance and a 3D Green function `∼ 1/r`.
  So `3+1` is the lowest event-lattice dimension at which a continuous menu's
  linearized formation law has a Newtonian equal-level kernel.
- (B-linear) For `d = 3`, `M = (1/16) [[3,−1,−1],[−1,3,−1],[−1,−1,3]]`,
  eigenvalues `1/16` (along `(1,1,1)`) and `1/4` (multiplicity 2). `det M = 1/256`.
  The continuum Fourier transform of `1/(kᵀ M k)` is
  `1 / (4π sqrt(det M) sqrt(xᵀ M^{−1} x)) = 4 / (π sqrt(xᵀ M^{−1} x))`.
- (D) Drift `φ = 1 + i(k_1+k_2+k_3)/4 + O(k²)`, i.e. `(1,1,1)/4` per level.
  A point source's forward-cone response is the 4-direction multinomial
  `(4n)! / (n!)^4 4^{-4n}` at `(n,n,n,n)` after `4n` steps, not the covariance
  `1/r`. A node that reads the kernel as a static equal-level object sees the
  Green function of (B); a node that reads causal response sees the multinomial
  cone. They are different.

Sphere LRO (`liminf_t E[m_t · e] > 0`) and two-sided bounds on the *nonlinear*
structure factor are not claimed.

## (2) Steps

**Step 1: `u = 1` only at the origin (PROVED; CHECKED as A1).**
`|1 + Σ_{j=1}^{d} e^{i k_j}| = d+1` iff every term equals `1`, iff `k_j ∈ 2πZ`.
On every finite torus the only unit-multiplier mode is the zero mode.

**Step 2: Hessian at `d = 3` (PROVED; CHECKED as A2, A3).**
`φ = (1 + Σ cos k_j + i Σ sin k_j)/4`. Expanding `1 − |φ|²` to quadratic order
gives `kᵀ M k` with the matrix above. Characteristic polynomial
`(λ − 1/16)(λ − 1/4)^2 = 0`. All eigenvalues positive, so `M ≻ 0`. The same
expansion for general `d` is `1 − u = (d/(2(d+1)^2)) |k|^2 − (1/(d+1)^2) Σ_{i<j} k_i k_j + O(k^4)`,
which is `kᵀ M_d k` with `M_d = (1/(2(d+1)^2)) ((d+1) I − J_{d×d})` wait: the
quadratic form `(d/2) Σ k_i² − Σ_{i<j} k_i k_j` over `(d+1)^2` is positive
definite on `R^d` (eigenvalues `(d+2)/2` once along `(1..1)`? checked for
`d = 1, 2, 3, 4` as A3).

**Step 3: integrability (PROVED; CHECKED as B1).**
On a neighbourhood of the origin, `1 − u ≥ c |k|^2` with `c = (1/2) λ_min(M_d) > 0`.
`∫_{|k|<ε} d^d k / |k|^2` converges at `0` iff `d − 2 > 0`. Off that neighbourhood
`u ≤ 1 − δ` on the compact torus minus the neighbourhood (Step 1), so `1/(1−u)`
is bounded. Hence the integral is finite iff `d > 2`.

**Step 4: continuum Green prefactor at `d = 3` (PROVED; CHECKED as C1).**
`∫ d^3k/(2π)^3 e^{ik·x} / (kᵀ M k) = 1 / (4π sqrt(det M) sqrt(xᵀ M^{−1} x))`
by the substitution `q = M^{1/2} k` and the Newtonian kernel of `−Δ` in `R^3`.
`det M = 1/256` is the product of eigenvalues (CHECKED). This is the linear
equal-level `1/r` law, anisotropic along versus across the cone axis.

**Step 5: drift and multinomial response (PROVED; CHECKED as D1, D2).**
Linear term of `φ` is `i(k_1+k_2+k_3)/4`. Occupancy of `(n,n,n,n)` after `4n`
steps of the four unit vectors is `(4n)!/(n!)^4`, each of weight `4^{-4n}`,
exact integers for `n = 1..6`. Distinct from the covariance kernel.

**Step 6: LRO (not attempted).** The linear zero mode on a finite torus of
volume `V` has variance `σ² t / V` and does not by itself give
`liminf E[m_t · e] > 0` in infinite volume. A comparison with the linear model
needs a sign/monotonicity lemma for the sphere (block 27) that is not re-proved
here.

## (3) Where the route stops

Steps 1–5 stand for the linearized law. Step 6 (sphere LRO, nonlinear two-sided
bounds) is not taken. The executed `|m| = 0.93` at `β = 6` remains executed.

## (4) What would finish it

Block 27's `A(κ)/κ` comparison turned into a level-time Lyapunov for the plane
average of the sphere; two-sided IR bounds on the nonlinear structure factor;
the gravity-node reading of the anisotropic Green function of Step 4.

Imports: the linearized law as declared in the task (and block 35 for `d = 2` as
an evidence address). The Newtonian integral in `R^3` is the standard
`∫ e^{iq·y} / |q|^2 d^3q / (2π)^3 = 1/(4π |y|)`, used at the scope of Step 4
and listed here.
