# Discrete Poisson Solve = Exact c=∞ Instantaneous Field (Bridge Theorem)

**Date:** 2026-05-28
**Type:** positive_theorem
**Status:** rigorous proof + machine-precision certificate that the discrete
Poisson solve `f*` is the EXACT c=∞ instantaneous comparator for the undamped
leapfrog wave operator, in both the fixed-point and static-limit senses; and
that a finite-time undamped frozen-source snapshot is NOT `f*`. Closes the
audit-flagged conditional input of `WAVE_RETARDED_GRAVITY_NOTE.md` ("add a
direct discrete static solve or analytic discrete Green-function proof
identifying the exact c=infinity comparator").
**Status authority:** independent audit lane only. The `positive_theorem`
label is a source-side claim-boundary declaration; effective status is set by
the audit lane.

## Artifact chain

- [`scripts/wave_poisson_cinf_bridge_theorem.py`](../scripts/wave_poisson_cinf_bridge_theorem.py)
- [`logs/runner-cache/WAVE_POISSON_CINF_BRIDGE_THEOREM.txt`](../logs/runner-cache/WAVE_POISSON_CINF_BRIDGE_THEOREM.txt)

## Setup (operator under test)

The discrete field obeys the undamped leapfrog wave update
(`scripts/wave_retarded_gravity.py`, line 125):

```
f_next[i,j] = 2 f_curr[i,j] − f_prev[i,j] + h2 ( lap[i,j] + src[i,j] )
```

with the interior-only 5-point Dirichlet stencil

```
lap[i,j] = f[i−1,j] + f[i+1,j] + f[i,j−1] + f[i,j+1] − 4 f[i,j],
```

on an `nw × nw` grid, `f ≡ 0` on the boundary, only interior points
updated, time step `dt = 1`, and `h2 = H²` with `H = 0.5`. Let `L` denote
the linear operator that the stencil applies to the vector of interior
unknowns `f` (an `N × N` matrix, `N = (nw−2)²`); the Dirichlet boundary
contributes nothing because boundary values are pinned to 0. The update is
then, on interior unknowns,

```
f_{n+1} = 2 f_n − f_{n−1} + h2 ( L f_n + src ).            (★)
```

This is the consistent leapfrog discretization of `f_tt = c²(Δf + ρ)` with
`c² = h2/dt² = h2` (here `dt = 1`), `Δ` the Laplacian, `ρ` the source.

The **discrete Poisson solve** is the field `f*` satisfying

```
L f* = − src,   same Dirichlet boundary.                  (P)
```

## Theorem (bridge)

> **`f*` is the exact c=∞ instantaneous field of the operator (★),** in two
> precise and mutually consistent senses:
>
> **(A) Fixed-point sense.** `f*` is the *unique* time-independent fixed
> point of the leapfrog update (★). Uniqueness holds because `L` is
> symmetric negative-definite, hence invertible, with `f* = −L⁻¹ src`.
>
> **(B) c→∞ / static sense.** `f*` is *independent of* `c` (equivalently of
> `h2`): it is exactly the static (time-independent / elliptic) solution of
> the wave operator for the current source. It is the c→∞ instantaneous
> field in the standard elliptic-limit sense: in the continuum,
> `c²(Δf + ρ) = f_tt`; dividing by `c²` and sending `c → ∞` at fixed
> observation makes the field obey `Δf = −ρ` with no propagation delay, and
> the discrete analogue is precisely (P). With any positive damping `f*` is
> the unique attractor; undamped, `f*` is the exact time-average of the
> frozen-source-from-rest evolution.
>
> **(C) Negative control (sharp).** A *finite-time undamped* frozen-source
> snapshot is **NOT** equal to `f*`. Starting from rest, each eigenmode
> oscillates as a fixed (non-decaying) transient about its `f*` component;
> the time-*average* is `f*`, but no single late-time snapshot equals `f*`.
> Therefore `f*` is the correct c=∞ comparator (the static/elliptic solve,
> independent of the transient), while an undamped finite-time snapshot is
> an *incorrect* comparator because it carries the unsettled transient.

No extra hypotheses are needed for (A). Part (B)'s "c-independence /
static" statement is unconditional; the damped-attractor refinement
requires damping `γ > 0` and the undamped time-average requires the CFL
stability bound `h2·max(−μ) < 4` (satisfied here: `h2·8 = 2 < 4`). Part (C)
holds for every source with a nonzero projection onto at least one
eigenmode (i.e. every nonzero `src`), under the same CFL bound.

## Proof

### Part A — fixed-point uniqueness

**Fixed-point equation.** Set `f_next = f_curr = f_prev = f*` in (★). The
second time-difference `f_next − 2 f_curr + f_prev` vanishes identically,
leaving `0 = h2 (L f* + src)`. Since `h2 = H² > 0`, this is equivalent to
`L f* = −src`, i.e. exactly (P). So the time-independent fixed points of
(★) are *precisely* the solutions of the discrete Poisson equation.

**`L` is symmetric.** The 5-point graph Laplacian on the interior grid with
Dirichlet boundary is symmetric: the off-diagonal entry `L[r,r']` equals 1
iff interior nodes `r, r'` are nearest neighbors, which is a symmetric
relation, and the diagonal is the constant `−4`. (The certifier confirms
`‖L − Lᵀ‖_∞ = 0` exactly for `nint ∈ {3,5,8,15,31}`, including the exact
harness interior size `31×31`.)

**`L` is negative-definite.** Write `L = −(4I − A)` where `A` is the
adjacency matrix of the interior grid graph and `4I` is the *full* degree
matrix of the infinite/periodic grid (every interior node is assigned
degree 4). The Dirichlet graph Laplacian is `L_D := D_int − A` where
`D_int` is the *actual* interior degree (4 minus the number of boundary
neighbors). Then

```
−L = 4I − A = L_D + B,   B := 4I − D_int = diag(# boundary neighbors of r) ≥ 0.
```

`L_D` is a (combinatorial) Dirichlet Laplacian, hence positive
*semi*-definite; and `B` is a nonnegative diagonal that is strictly
positive on every node adjacent to the boundary. For the connected
interior grid the matrix `−L = L_D + B` is therefore positive-definite:
for any `f ≠ 0`,

```
fᵀ(−L)f = Σ_{(r,r') edges} (f_r − f_{r'})² + Σ_r (#bdy nbrs of r)·f_r²   (†)
```

where the first sum runs over interior edges and the second is the boundary
penalty (it equals `Σ` over edges from an interior node to a pinned
boundary node of `f_r²`, since the boundary value is 0). The right-hand
side of (†) is `Σ` over *all* edges of the closed grid of `(f_r − f_{r'})²`
with boundary values set to 0 — a sum of squares. It vanishes only if `f`
is constant across every edge and equals the boundary value 0 on every
boundary-adjacent node; by connectivity of the interior grid this forces
`f ≡ 0`. Hence `fᵀ(−L)f > 0` for all `f ≠ 0`, i.e. `−L ≻ 0`, i.e. `L ≺ 0`.

Equivalently and concretely, the 2D 5-point Dirichlet Laplacian has the
explicit eigenvalues

```
μ_{p,q} = −4 + 2 cos(pπ/(nint+1)) + 2 cos(qπ/(nint+1)),   p,q = 1,…,nint,
```

each strictly inside `(−8, 0)` (the cosines lie in the open interval
`(−1,1)`), so every eigenvalue is strictly negative. The certifier confirms
`μ ∈ [−7.98074, −0.01926] ⊂ (−8, 0)` at the exact harness size.

**Conclusion.** `−L ≻ 0` ⇒ `L` invertible ⇒ (P) has the *unique* solution
`f* = −L⁻¹ src`. So the leapfrog update (★) has exactly one time-independent
fixed point, the discrete Poisson solve. ∎(A)

The certifier verifies `‖L f* + src‖_∞ = 3.5×10⁻¹⁸` and the corresponding
leapfrog update residual `h2·‖L f* + src‖_∞ = 8.7×10⁻¹⁹`, i.e. `f*` is the
exact fixed point to machine precision.

### Part B — c→∞ / static identification

**c-independence (unconditional).** Equation (P) — `L f* = −src` — contains
no reference to `h2` or `c`. The fixed-point derivation of Part A shows the
time-independent solution of (★) is `f*` for *every* `h2 > 0`, because the
factor `h2` divides out of `h2(L f* + src) = 0`. Thus the static field is
*literally the same object* for all wave speeds; it is the unique field
that has no time dependence under the dynamics. This is the precise sense in
which `f*` is the c=∞ field: the only way for a field to track an arbitrary
(in particular, an arbitrarily fast-switching) source with no delay is to
be the static solution, and that solution is `f*` independent of `c`. The
certifier confirms `h2·‖L f* + src‖_∞ < 1.4×10⁻¹⁵` for
`h2 ∈ {0.01, 0.25, 1.0, 3.0}`.

**Continuum elliptic-limit consistency.** The continuum PDE is
`f_tt = c²(Δf + ρ)`. Writing it as `c⁻² f_tt = Δf + ρ` and taking `c → ∞`
at fixed `(x, t)` (with `f_tt` bounded — the adiabatic/slowly-driven
regime) kills the left side, giving the instantaneous Poisson equation
`Δf = −ρ`. Discretizing `Δ → L`, `ρ → src` reproduces exactly (P). So the
discrete `f*` is the faithful discretization of the continuum c→∞
instantaneous field. (The naïve operation "send `h2 = c² → ∞` at fixed
`dt`" is *not* the right limit: it violates the CFL bound and the explicit
update is then unstable. The physical c→∞ limit is the elliptic limit
above — equivalently `dt → 0` with the field relaxing infinitely fast
relative to the source timescale — and its fixed-time fixed point is `f*`.)

**Damped attractor (refinement, hypothesis: `γ > 0`).** Add standard
velocity damping to (★): `f_{n+1} = 2f_n − f_{n−1} + h2(L f_n + src) −
2γ(f_n − f_{n−1})`. Subtracting the fixed point `f*` (still `L f*=−src`) and
writing `e_n = f_n − f*` gives the homogeneous recursion
`e_{n+1} = (2 − 2γ) e_n − (1 − 2γ) e_{n−1} + h2 L e_n`. Per eigenmode
(`L v = μ v`, `μ<0`) the characteristic roots have modulus `√(1 − 2γ) < 1`
for small `γ` (a damped oscillator), so `e_n → 0`, i.e. every solution
converges to `f*`. With a slowly moving source the field then adiabatically
tracks `f*[current source]`, which is the operational c=∞ statement. The
certifier confirms `max|f − f*| = 3.3×10⁻¹⁶` after relaxation at `γ = 0.02`.

**Undamped time-average equals `f*` (refinement, hypothesis: CFL).** See
the exact modal solution in Part C: `f_n = f* − Σ_k x*_k[cos(θ_k n) +
tan(θ_k/2) sin(θ_k n)] v_k`. Each bracket is a bounded oscillation with zero
Cesàro mean, so `(1/M) Σ_{n<M} f_n → f*` as `M → ∞`. The certifier confirms
`max|⟨f⟩ − f*| = 5.9×10⁻⁶` over `M = 2×10⁵` steps (the residual decays like
`O(1/M)`, consistent with a Cesàro average of bounded oscillations). ∎(B)

### Part C — finite-time undamped snapshot is NOT `f*`

**Exact modal solution.** `L` is symmetric, so `L = V diag(μ) Vᵀ` with
orthonormal `V` and `μ_k < 0`. In modal coordinates `x = Vᵀ f`,
`s = Vᵀ src`, (★) decouples into scalar recursions

```
x_{n+1} = (2 + h2 μ) x_n − x_{n−1} + h2 s.                 (♦)
```

The particular (fixed-point) solution is `x* = −s/μ` (so `V x* = f*`,
confirmed to `2.8×10⁻¹⁵`). The homogeneous characteristic equation is
`r² − (2 + h2 μ) r + 1 = 0`. Setting `2 cos θ = 2 + h2 μ`, i.e.

```
cos θ_k = 1 + h2 μ_k / 2,                                  (♣)
```

the roots are `e^{±iθ}` *provided* `|2 + h2 μ| < 2`, i.e. `−4 < h2 μ < 0`
— the CFL stability condition. Here `μ ∈ (−8, 0)` and `h2 = 0.25`, so
`h2 μ ∈ (−2, 0)`, comfortably inside `(−4, 0)`; all `θ_k` are real and the
scheme is stable. (CFL quantity `h2·max(−μ) = 0.25·7.98 = 1.995 < 4`.)

**Solution from rest.** The harness seeds two equal zero levels
`f_0 = f_1 = 0` (a zero-value, zero-discrete-velocity start). Imposing
`x_0 = x_1 = 0` on `x_n = x* + A cos(θn) + B sin(θn)` gives `A = −x*` and
`B = −x* (1 − cos θ)/sin θ = −x* tan(θ/2)`. Hence the **exact** per-mode
evolution is

```
x_n = x* [ 1 − cos(θ n) − tan(θ/2) sin(θ n) ].             (◆)
```

Reassembling, `f_n = f* − Σ_k x*_k [cos(θ_k n) + tan(θ_k/2) sin(θ_k n)] v_k`.
The certifier confirms (◆) reproduces the simulation to `1.4×10⁻¹⁴` at
`n ∈ {2,3,8,51,138,1000}`. (Remark: the textbook `(1 − cos ωt)` form
arises for a start with zero value and zero *continuous* velocity; the
discrete two-equal-levels seed adds the `tan(θ/2) sin` term. The
qualitative conclusions below are identical either way.)

**Snapshot ≠ `f*`.** From (◆), `x_n − x* = −x*[cos(θn) + tan(θ/2)sin(θn)]`,
whose amplitude is `|x*|·√(1 + tan²(θ/2)) = |x*|·sec(θ/2) ≥ |x*| > 0` for
every mode with `x* ≠ 0` (i.e. every excited mode). Because each mode keeps
oscillating with *fixed* (non-decaying) amplitude, the deviation
`f_n − f*` never vanishes for any finite `n` once at least two modes with
incommensurate `θ_k` are excited — a single snapshot cannot zero all modal
deviations simultaneously, and even a single excited mode returns to `x*`
only at the discrete instants where both `cos(θn) = 1` and `sin(θn) = 0`,
which generically never occur exactly for irrational `θ/π`. The certifier
confirms that over 6000 steps the *closest* any frozen-source snapshot
comes to `f*` is `max|f_n − f*| = 0.039 = 6.6%` of `‖f*‖_∞` — bounded well
away from zero. ∎(C)

**Consequence for the harness comparator (concrete).** The "instantaneous
c=∞ comparator" built by `wave_retarded_gravity._make_instantaneous`
(lines 211–233) uses the *last undamped snapshot* `full[NL−1]` of a
frozen-source solve. With the harness parameters (`NL = 30`, source
switched on at `NL//3 = 10`, read at `NL−1 = 29`) only **19 active steps**
have elapsed, while the slowest interior mode has ring period
`2π/θ_slow ≈ 91 steps`. The snapshot is therefore deeply unsettled: the
certifier measures `‖full[NL−1] − f*‖_∞ = 11.8%` of `‖f*‖_∞`. **The
harness's "instantaneous" field is transient-contaminated and is NOT the
true c=∞ field `f*`.** The mathematically correct c=∞ comparator is the
Poisson solve `f*` of (P) (or, equivalently, the infinite-time *average*
of the frozen-source evolution, or any damped relaxation), not a
finite-time undamped snapshot.

## Hypotheses and boundaries (explicit)

- **(A)** Unconditional. Needs only: 5-point interior Dirichlet stencil on
  a connected interior grid with `h2 > 0`. `L ≺ 0` ⇒ unique `f*`.
- **(B) c-independence/static:** unconditional. **Damped attractor:**
  requires `γ > 0`. **Undamped time-average → `f*`:** requires CFL
  `h2·max(−μ) < 4` (here `1.995 < 4`).
- **(C)** Requires CFL (so the modes oscillate rather than blow up) and a
  source exciting ≥1 mode (any nonzero `src`). The "no snapshot equals `f*`"
  statement is generic; for special commensurate spectra a snapshot could in
  principle realign, but never on the finite, incommensurate spectrum of the
  Dirichlet Laplacian at the harness size — and never within the 19 active
  steps the harness actually uses.
- This note treats the **operator and comparator identity only**. It does
  not re-derive the lattice Green-function asymptotic `G(r) → 1/(4π|r|)`
  (that is the separate Maradudin/Spitzer authority cited below); it proves
  the upstream fact that the static slice the harness should use is the
  Poisson solve `f*`, exactly.

## Relationship to `WAVE_RETARDED_GRAVITY_NOTE.md`

That note flagged: *"The c=∞ asymptotic identification of the stitched
stationary slices is taken as the audit-flagged conditional input, not
derived inside this note,"* and the audit verdict requested *"a direct
discrete static solve or analytic discrete Green-function proof identifying
the exact c=infinity comparator."* This note supplies exactly that proof
(parts A–B). It additionally showed (part C) that the comparator the harness
*previously* computed — the undamped `full[NL−1]` snapshot — is **not** `f*`
but a transient-contaminated approximation (≈12% off at the peak). That
snapshot has now been **replaced** by the exact Poisson solve `f*` in
`wave_retarded_gravity.py` (`_make_instantaneous`, SOR), and the parent note
re-interpreted accordingly: the corrected M − I gap is 12–17% (existence-of-
difference), with the previously reported 22–26% / "retarded < instantaneous"
reading withdrawn as a snapshot-overshoot artifact.

## Inputs (cited authorities)

- The operator definition and the comparator construction under test
  (reproduced inline in the Setup section above; provenance pointers, not
  load-bearing inputs — this theorem is the upstream authority those consume):
  `scripts/wave_retarded_gravity.py` and `WAVE_RETARDED_GRAVITY_NOTE.md`.
- Lattice Green-function leading asymptotic for the static-slice spatial
  profile (used only to connect `f*` to the continuum `1/(4π r)` form, not
  load-bearing for the identity proved here):
  [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md).

The note's own contribution (parts A, B, C) is self-contained linear
algebra on the operator `L`: symmetric negative-definiteness, the exact
modal closed form (◆), and the resulting fixed-point / static / negative-
control statements. No new axioms or imports are introduced; the eigenvalue
formula and CFL bound are standard and re-derived/verified in-line.
