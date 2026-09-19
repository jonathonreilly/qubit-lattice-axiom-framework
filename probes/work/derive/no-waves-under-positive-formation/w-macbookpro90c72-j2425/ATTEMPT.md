# no-waves-under-positive-formation, attempt 3 (worker w-macbookpro90c72-j2425, model grok-4.6)

Independent of grok a4 (NEC Sigma vs block 35). Route: triangle inequality plus the covariance of a finite nonnegative predecessor measure.

## (1) The statement attempted

Let a gain-one linear formation law on one earlier level have nonnegative weights `w_y` on a finite predecessor set `F`, `∑ w_y=1`. Its multiplier is `λ(k)=∑_y w_y e^{-ik·y}`. Then `|λ(k)|≤1`, with equality in a neighbourhood of the origin only at `k=0` whenever the covariance `Cov=∑ w (y-m)(y-m)^T` is positive definite. In that case

    λ(k)=1 − i m·k − ½ k^T M k + O(|k|³),    |λ|²=1 − k^T Cov k + O(|k|⁴),

so the mode nearest 1 is drift plus diffusion, not a wave `|λ|=1` with `arg λ = c|k|`. NEC has PD covariance (Hessian of `|λ|²` at 0 is `-2 Cov`, entries `-4/9` and `2/9`). The 7-stencil light-cone kernel is real, `λ=1−E/7`, `|λ|<1` for `k≠0`. Collinear support is the degenerate exception (a transverse undamped direction). A single predecessor is a pure drift `arg=v·k`. Negative weights can violate `|λ|≤1`. Waves would require dropping positivity, taking a complex/spinor record with unitary overlaps, or adding a conserved oscillatory quantity.

## (2) Steps

**Step 1 — triangle inequality (PROVED; CHECKED X.1).** `|∑ w_y e^{-ik·y}| ≤ ∑ w_y=1`, equality iff all phases `e^{-ik·y}` agree on the support of `w`.

**Step 2 — expansion (PROVED; CHECKED N, C).** `λ(k)=E[e^{-ik·Y}]=1 − i k·m − ½ k^T M k + O(|k|³)` with `m=E Y`, `M=E[YY^T]`. Then `|λ|²=1 − k^T Cov k + O(|k|⁴)`. If `Cov` is PD, `|λ|<1` for small `k≠0`. A wave would need `|λ|=1` and `arg λ ∝ |k|`; the first already fails. Checked: NEC Hessian of `|λ|²` is `H_{11}=H_{22}=-4/9`, `H_{12}=2/9`, `det=4/27>0` (`H=-2 Cov`). NEC mean `(-1/3,-1/3)`, `Cov` PD with `det=1/27`.

**Step 3 — 7-stencil (PROVED; CHECKED S).** Symmetric neighbourhood: `λ=(1+2∑ cos k_j)/7=1−E/7` real (no drift). `|λ|=1` iff `E=0` iff `k=0` on `(-π,π)³`. Hessian of `|λ|²` at 0 is negative (`H_{11}=-4/7`).

**Step 4 — exceptions (PROVED; CHECKED C.3, X.2).** If `F` lies in an affine line, `Cov` has rank 1 and a transverse `k` is undamped to this order (checked: three collinear points, `det Cov=0`). A singleton `F={v}` gives `λ=e^{-ik·v}`, `|λ|=1`, `arg=-v·k`: a drift, not an isotropic wave `c|k|`. `arg=c|k|` is not the Fourier transform of a finite positive measure (radial phase is not a linear character).

**Step 5 — what would give waves (PROVED as a reading).** Drop positivity: `|λ|` need not be `≤1` (e.g. weights `(2,-1)`). A complex record with unitary overlap can have `|λ|=1` on a sphere in `k`. A second conserved quantity with an oscillatory pair of modes can propagate. Each costs an axiom sentence: positivity of overlap weights; the record being a real vector on the sphere/menu; or an extra conserved structure the formation law does not supply.

## (3) Where the route stops

Multi-level delay (companion matrix of several earlier levels) is the same near `λ=1`: the Perron root still expands as drift plus the covariance of the *first-moment* delay measure. That expansion is not written out as a companion-matrix identity here. Nonlinear (sphere) formation is not linear; the statement is for the linear kernels the task names.

## (4) What would finish it

The two-level companion expansion matching block 35 T2; a classification of all finite supports with `Cov` degenerate.
