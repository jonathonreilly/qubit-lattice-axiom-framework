# plane-memory-loss, attempt 4 (worker w-macbookpro90c72-jcb00, model grok-4.6)

Plan formed before reading other attempts: take route (ii) of the task (comparison
with the linear model via monotonicity of `A(κ)/κ`) and locate the first failing
step; along the way prove the mean-field critical coupling exactly.

Objects: block 26 (PR #8170) sphere formation in level time, three predecessors,
weight `exp(β s·S)`, `S` the sum of the three recorded predecessors; `A(κ) = coth κ − 1/κ`
the Langevin function (mean length of vMF(`κ`)). Block 27 (PR #8171) uniqueness
for `β < 1/√3` is used only as placement.

## (1) The statement attempted

**Mean-field.** The closed map `m ↦ A(3β |m|)` on `[0, 1]` (replace `S` by its
mean `3m e_z`) has `m_t → 0` from every initial `m ∈ [0, 1]` if and only if
`β ≤ 1`. Proof: `A(κ)/κ < 1/3` for `κ > 0`, so `A(3β m) < β m ≤ m` on `(0, 1]`
when `β ≤ 1`; the derivative at `0` is `β`, so `β > 1` makes `0` linearly unstable.

**Route (ii) no-go.** A comparison of the true output mean
`E[A(β|S|) S/|S|]` with the mean-field map fails at the first step: triangle
`|S| ≥ |E S| = 3|m|` together with `A` increasing (`sinh κ > κ`) gives
`A(β|S|) ≥ A(3β |m|)`, which is the wrong sign for an upper bound on `|m'|`.
The linear model cannot supply the decay either: `φ(0) = 1`, the uniform mode
is conserved.

Infinite-lattice `m_t → 0` for the true process is not proved.

## (2) Steps

**Step 1 — `A(κ)/κ < 1/3` for `κ > 0` (PROVED; CHECKED as E0).**
`q(κ) = (3+κ²) sinh κ − 3κ cosh κ`, `q(0)=0`,
`q' = κ(κ cosh κ − sinh κ)`. `r = κ cosh − sinh`, `r(0)=0`, `r' = κ sinh ≥ 0`.
So `r ≥ 0`, `q ≥ 0`, i.e. `A(κ)/κ ≤ 1/3`, and `r' > 0` for `κ > 0` so the
inequality is strict. Series `A(κ)/κ = 1/3 − κ²/45 + O(κ⁴)`.

**Step 2 — `A` is increasing (PROVED; CHECKED as E2a–b).**
`A' = 1/κ² − csch² κ > 0` iff `sinh κ > κ`. `sinh − κ` vanishes at `0` with
derivative `cosh − 1`, which vanishes at `0` with derivative `sinh ≥ 0`.

**Step 3 — mean-field threshold `β = 1` (PROVED from 1; CHECKED as E1).**
`A(3β m) = 3β m · (A(κ)/κ)` with `κ = 3β m`. For `m ∈ (0, 1]` one has `κ > 0`,
so `A(3β m) < β m`, and `β m ≤ m` iff `β ≤ 1`. At `0`, `A(u) ∼ u/3`, so
`d/dm A(3β m)|_0 = β`. For `β = 2` the series of `A(6m)/m` starts at `2`.
`A(3) < 1` (numerical witness of contraction at the aligned point for `β = 1`).

**Step 4 — route (ii) fails (PROVED; CHECKED as E2c–d).**
`|S| ≥ |s_1+s_2+s_3| = 3|m|` (triangle; equality iff the three records are
parallel). Step 2: `A(β|S|) ≥ A(3β |m|)`. The true mean
`E[A(β|S|) Ŝ]` is therefore not dominated by the mean-field value in the
contracting direction. On the initial aligned plane one has equality
(`|S|=3`); after one step, fluctuations make `|S|<3` on a positive-measure set,
which *lowers* `A` (good for forgetting) but opens a gap that is no longer a
function of `|m|` alone. Integer witness of the triangle: `2 e_z + e_x` has
`|S|² = 5 = (3|m|)²`.

**Step 5 — linear model conserves the uniform mode (CHECKED as E3).**
Backward 3-stencil: `φ(0) = (1+1+1)/3 = 1`. Symmetric 5-stencil in 2D:
`φ(0) = 1`. The linear comparison therefore cannot produce `m_t → 0`.

## (3) First failing step of route (ii)

Step 4: the comparison `|S|` vs `3|m|` has the wrong sign for an upper bound
on the output magnetization. Route (i) (path-space twist) is not attempted
here. Route (iii) (O(3) + ergodicity) is not attempted: uniqueness is known
only for `β < 1/√3` (block 27), which is a different range from mean-field
`β ≤ 1`.

## (4) What would finish it

A correlation inequality that bounds `E[A(β|S|) Ŝ]` by a strictly contractive
function of `|m|` for every `β`, or a relative-entropy argument whose Dirichlet
cost is `o(1)` per level (route (i), with a twist that does not cost `Θ(T)`).
The mean-field threshold `β = 1` is not a proof for the infinite lattice
(block 26's decay is observed also for `β = 3..24 > 1`).

Nothing here edits notes or runners.
