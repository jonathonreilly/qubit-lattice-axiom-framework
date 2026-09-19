# formation-in-3plus1, attempt 5 (worker w-macbookpro90c72-jd7c3, model grok-4.6)

Grok a1/a4 treated the linear dichotomy and the 1/r Green; a2/a6 the mean-field
threshold `3/4` and the small-`k` envelope of `1-|φ|²`. This attempt is task
(d) only: the backward 4-predecessor stencil is a DAG, `φ` is not identically
real, and the causal static response `1/(1-φ)` is not a real multiple of the
equal-level covariance `1/(1-|φ|²)`. Sphere LRO and two-sided `S(k)` bounds
are not claimed. The dichotomy is not re-claimed.

Control: `probes/lib/formation_levelplane.py` (linear law `φ=(1+Σ e^{ik_j})/n`
on the backward stencil; suffix `s` is the symmetric 7-neighbourhood, `φ`
real, no drift).

## (1) The statement attempted

Event lattice `Z^4`, level order: a record at `x` is formed from the four
backward neighbours `x-e_1,…,x-e_4`. The linearized automaton on the
3-dimensional level plane is the AR `θ_{t+1}(k)=φ(k) θ_t(k)+ξ_t(k)` with
`φ(k)=(1+e^{ik_1}+e^{ik_2}+e^{ik_3})/4`.

**Exact partial (task (d)).**

- (DAG) The predecessor relation is not symmetric: if `y=x-e_j` then `x` is
  not a predecessor of `y`. The formation graph is a DAG. CHECKED U.1.
- (`φ` not real) `Im φ=(sin k_1+sin k_2+sin k_3)/4`, identically zero only on
  a proper subvariety. At `k=(π/2,0,0)`, `φ=(3+i)/4`. CHECKED F.2, F.5.
- (FDT mismatch) The equal-level covariance symbol `C=1/(1-|φ|²)` is real.
  The static causal response `R=1/(1-φ)` (sum of the retarded Green
  `Σ_{s≥0} φ^s`) is a real multiple of `C` if and only if `φ` is real. At
  `k=(π/2,0,0)`: `|φ|²=5/8`, `C=8/3`, `R=2(1+i)`, `R/C=(3/4)(1+i)∉R`.
  CHECKED F.3–F.7, I.1.
- (IR class) `∇(1-φ)|_0=-i(1,1,1)/4 ≠ 0`, while `∇(1-|φ|²)|_0=0`. Causal
  response is `O(1/|k|)` and complex at small `k`; covariance is `O(1/k²)`
  and real. CHECKED D.1, I.2.
- (Contrast) The control's symmetric 7-stencil `φ_s=(1+2Σ_j cos k_j)/7` is
  real. At the same mode `φ_s=5/7`, `R_s=7/2`, `C_s=49/24`, `R_s/C_s=12/7=1+φ_s∈R`.
  CHECKED S.1–S.3.
- (Drift) Four equal weights on `{0,e_1,e_2,e_3}`; centroid `(1,1,1)/4`.
  Equivalent: `∂φ/∂k_j|_0=i/4`. CHECKED D.1, D.2.

A gravity node that reads the equal-level covariance sees a 3d Green function
at small `k` (groke a1/a4). One that reads the linear causal response sees a
complex directed kernel with drift `(1,1,1)/4` per level. They are not the
same object, and they are not related by a real fluctuation-dissipation
factor because the stencil is not reversible.

**Not claimed.** (a) Sphere LRO. (b) Two-sided nonlinear `S(k)` bounds.
(c) The `d>2` dichotomy (groke a1/a4). Mean-field `β_c=3/4` (groke a2/a6).

## (2) Steps

**Step 1 — DAG (PROVED; CHECKED U.1).** Predecessors of `x∈Z^4` are
`{x-e_j: j=1..4}`. If `y=x-e_1`, predecessors of `y` are `{x-e_1-e_k: k=1..4}`,
which does not contain `x`. Every formation edge decreases the level
`t=x_1+x_2+x_3+x_4` by 1, so there are no 2-cycles.

**Step 2 — `φ` not identically real (PROVED; CHECKED F.1, F.2, F.5, I.1).**
`φ=(1+Σ_j e^{ik_j})/4`, so `Im φ=(Σ_j sin k_j)/4`. This vanishes on a
codimension-1 subset, not everywhere. Explicitly `φ(π/2,0,0)=(1+i+1+1)/4=(3+i)/4`.
The cosine identity
`|φ|²=(2+Σ_j cos k_j + Σ_{i<j} cos(k_i-k_j))/8`
gives `|φ(π/2,0,0)|²=5/8`.

**Step 3 — FDT mismatch (PROVED; CHECKED F.3–F.7).** Stationary AR covariance
of a nonzero mode is `σ²/(1-|φ|²)`. The retarded Green is `φ^s` (`s≥0`
levels), summing to `1/(1-φ)` when `|φ|<1`. If `R=λ C` for some `λ∈R` then
`(1-|φ|²)/(1-φ)` is real, i.e. `1-φ` is a real multiple of the real number
`1-|φ|²`, i.e. `φ` is real. At the test mode `1-φ=(1-i)/4`, `R=2(1+i)`,
`C=8/3`, and `Im(R/C)=3/4≠0`.

**Step 4 — drift and IR (PROVED; CHECKED D.1, D.2, I.2).** The four
predecessor displacements in plane coordinates are `0,e_1,e_2,e_3` with
equal weight `1/4`; mean `(1,1,1)/4`. Differentiating `φ` at the origin
gives the same vector as `∂φ/∂k_j|_0=i/4`. The gradient of `1-|φ|²` vanishes
at 0 (the covariance is even in `k` only up to the quadratic Hessian), so
the two symbols have different small-`k` order.

**Step 5 — symmetric contrast (PROVED; CHECKED S.1–S.3).** The 7-stencil of
the control's `s` suffix is undirected in the spatial graph of a single
level (site plus six neighbours). Its multiplier is real, and at
`k=(π/2,0,0)` the ratio `R/C=1+φ` is real. Reversibility of that stencil
is the light-cone route, not re-proved here; only the algebraic contrast
is used.

**Step 6 — LRO (not attempted).** Comparison via `A(κ)/κ` decreasing has the
wrong triangle-inequality sign (`|S|≥4|m|`). Executed `|m|=0.93` at `β=6`
stays executed.

## (3) Where the route stops

Task (d) is the exact mismatch and the DAG. Tasks (a) and (b) are not
taken. The small-`k` two-sided envelope of `S(k)` is grok a6, not re-claimed.

## (4) What would finish it

A Lyapunov using `E[A(β|S|)(S·e)/|S|]` and transience of the 3d plane walk
(`G(0)<∞`); two-sided IR bounds on the nonlinear structure factor.
