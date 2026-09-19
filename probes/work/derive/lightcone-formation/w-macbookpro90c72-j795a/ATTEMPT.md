# lightcone-formation, attempt 5 (worker w-macbookpro90c72-j795a, model grok-4.6)

Plan formed before reading other attempts' `ATTEMPT.md`. This attempt takes a
different route from the FSS/LRO claim and from a mere linearisation of
Dobrushin: it proves `‖Cov_{vMF(κ)}‖ ≤ 1/3` for every `κ ≥ 0`, which upgrades
the linearised threshold `β = 3/7` to a uniqueness theorem for the 7-stencil
sphere PCA, and it records the two-sided envelope of the linear kernel.

Objects: the symmetric 7-stencil formation law of
`probes/lib/formation_levelplane.py` (`dim=3s`),
`S_x = s_x + Σ_j (s_{x+e_j}+s_{x−e_j})`, kernel
`s'_x ∼ vMF(β S_x)` independently given the past, menu the unit sphere.
Reversibility w.r.t. `π ∝ ∏_x Z(β |S_x|)` is used as in the LEAD (the bilinear
identity `Σ s'_x · S_x(s) = Σ s_x · S_x(s')` for `N = −N`); it is not re-proved
here.

## (1) The statement attempted

**Uniqueness.** For every `β < 3/7`, the 7-stencil sphere PCA on `Z^3` has at
most one bounded-Lipschitz stationary law. Proof: the vMF mean map
`S ↦ A(β|S|) Ŝ` is `(β/3)`-Lipschitz on `R^3` because the covariance of
`vMF(κ)` has operator norm `≤ 1/3` for every `κ` (longitudinal eigenvalue
`A'(κ) ≤ 1/3`, transverse eigenvalue `A(κ)/κ ≤ 1/3`); each past spin enters
seven stars, so the Dobrushin coefficient is `≤ 7β/3 < 1`.

**Linear kernel envelope.** For the gain-one linear model,
`S(k)/σ² = 49 / (E(k)(14 − E(k)))` with `E ∈ (0, 12]`, hence
```
(7/2) σ² / E(k)  ≤  S(k)  ≤  (49/2) σ² / E(k).
```
(The nonlinear sphere kernel is not claimed.)

Long-range order at large `β` is not attempted.

## (2) Steps

**Step 1 — `exp(t) − 1 − t > 0` for `t > 0` (PROVED; CHECKED as E0).**
Taylor remainder `Σ_{n≥2} t^n/n!`, first term `t²/2 > 0`. Hence `1+t < e^t`,
and `1+t < e^t` is strict for `t > 0`.

**Step 2 — `e^u (1−u) ≤ 1` for `u ≥ 0` (PROVED; CHECKED as E1).**
`ψ(u) = e^u (1−u)`, `ψ(0) = 1`, `ψ'(u) = −u e^u ≤ 0`. Thus `ψ ≤ 1`. For
`u = κ²/3 ∈ [0, 1)`, this is `e^{κ²/3} (3−κ²) ≤ 3`, i.e.
`e^{κ²/3} ≤ 3/(3−κ²)`.

**Step 3 — `A'(κ) ≤ 1/3` (PROVED; CHECKED as E2).**
`A(κ) = coth κ − 1/κ`, `A'(κ) = 1/κ² − csch² κ`. Limit `κ → 0` is `1/3`
(series of `(κ coth κ − 1)/κ²`).
- If `κ² ≥ 3` then `1/κ² ≤ 1/3` and `csch² > 0`, so `A' < 1/3`.
- If `0 < κ² < 3`: the product `(sinh κ)/κ = ∏_{n≥1} (1 + κ²/(n²π²))`.
  `1+t < e^t` (Step 1) gives `(sinh κ)/κ < exp(Σ_n κ²/(n²π²))`.
  `Σ_n 1/n² = π²/6` (CHECKED E2d), so `Σ κ²/(n²π²) = κ²/6`, hence
  `sinh κ < κ exp(κ²/6)` and `sinh² κ < κ² exp(κ²/3)`.
  Step 2: `exp(κ²/3) ≤ 3/(3−κ²)`, so `sinh² κ < 3κ²/(3−κ²)`, i.e.
  `1/sinh² κ > (3−κ²)/(3κ²) = 1/κ² − 1/3`, i.e. `A'(κ) < 1/3`.

**Step 4 — `A(κ)/κ ≤ 1/3` (PROVED; CHECKED as E3).**
Equivalent to `(3+κ²) sinh κ ≥ 3κ cosh κ`. Put
`q(κ) = (3+κ²) sinh κ − 3κ cosh κ`. Then `q(0) = 0` and
`q'(κ) = κ (κ cosh κ − sinh κ)` (algebra, CHECKED). Put
`r(κ) = κ cosh κ − sinh κ`. Then `r(0) = 0` and `r'(κ) = κ sinh κ ≥ 0`.
So `r ≥ 0`, hence `q' ≥ 0`, hence `q ≥ 0`. The series of
`(κ coth κ − 1)/κ²` starts `1/3 − κ²/45 + O(κ⁴)`.

**Step 5 — Dobrushin coefficient (PROVED from 3–4).**
The Jacobian of the vMF mean in the exponential-family parameter `η = β S` is
the covariance of `s`. In an orthonormal frame along `S`, the eigenvalues are
the longitudinal variance `A'(κ)` and the two transverse variances `A(κ)/κ`.
Steps 3–4: both `≤ 1/3`. Hence `‖Cov‖ ≤ 1/3` and the mean map in `S` is
`(β/3)`-Lipschitz. One past spin at `y` enters `S_x` for each of the seven
`x ∈ y+N`. Wasserstein-1 (Euclidean) influence of that spin on the next level
is at most `7 · (β/3)`. Unique stationary law whenever `7β/3 < 1`, i.e.
`β < 3/7`. (The identity `7·(3/7)/3 = 1` is CHECKED as E4.)

**Step 6 — linear two-sided envelope (CHECKED as E5).**
`φ = 1 − E/7`, `1/(1−φ²) = 49/(E(14−E))` identically. For `E ∈ (0, 12]`,
`14−E ∈ [2, 14)`, so `49/(14E) ≤ 49/(E(14−E)) ≤ 49/(2E)`, i.e.
`(7/2)/E ≤ S/σ² ≤ (49/2)/E`.

## (3) First failing step of routes not taken

- *LRO by FSS on the doubled graph:* not attempted (classical RP not re-proved).
- *Two-sided bound for the nonlinear sphere kernel:* the envelope of Step 6 is
  for the linear model only. A cluster expansion around it at small `β` is open.
- *Uniqueness at `β = 3/7`:* the coefficient equals 1; Dobrushin is silent.

## (4) What would finish it

- FSS/RP on the doubled Heisenberg graph `Γ` of attempt 6, for an explicit
  large-`β` LRO threshold.
- A nonlinear two-sided bound `c₁(β)/E(k) ≤ S(k) ≤ c₂(β)/E(k)` in the unique
  phase `β < 3/7`.
- Uniqueness on the line `β = 3/7` by a stricter coupling.

Nothing here edits notes or runners.
