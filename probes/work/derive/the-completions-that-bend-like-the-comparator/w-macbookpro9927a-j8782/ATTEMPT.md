# The completions that bend like the comparator, attempt 1: one plane of third-order jets, and not only the curvature member

Worker `w-macbookpro9927a-j8782` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory. They run in about 35 seconds with a peak of about 140 MB.

| Family | What it checks | Arithmetic |
|---|---|---|
| Q | pinned sources | — |
| S | the exterior and the turn | exact (sympy) |
| B | the classification | exact (sympy) |
| W | bilinear members | exact (sympy) |
| N | nonlinear radial equations and capture thresholds | floating point, marked `[float]` |

## Sources, provenance and scope

**Sources, all as landed on main at `60c5f194`.** Family Q checks the hashes and the quoted lines.

- **Block 110.** The task cites PR #8960 as open. That PR is closed and the note has landed on main; the landed version is used here. It supplies:
  - the curvature member `F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`;
  - the exterior `χ = 1 + a/r`, `N = 1 − p/r`;
  - the index `n = χ³/N`;
  - the turn `2ν₁/b + π(ν₂ + ν₁²/2)/b² + …`.
- **Block 60.**
  - Rates `w = e^u` have weight one; lengths `ℓ = e^λ` have weight zero; `χ = √ℓ`; `N = wχ`.
  - T3: "the part of `F` of second order in `(u − ū, λ)` is `K w̄ [a u·Δλ + (ap − b) λ·Δλ]`; there is no term in `u` alone."
  - T1: the ledger is a wall term.
- **Block 55.** "A variational field equation keeps that ledger." Also: "An onsite term c w_x … spoils that normalized uniform-vacuum condition."

**Provenance.** The claim printed no prior attempts. Two of my earlier units are related, and neither is used as a premise:
- **#8912** treated the strong-field turn for the index `e^{A/r}`. Block 110 T5 re-derives that index as the log-linear completion.
- **#8721** is the first-order family law for lengths.

**The weight-one reduction.**

1. *The form of F.* A nearest-neighbour bond energy of weight one has the form `√(w_xw_y) φ(u_y − u_x, λ_x, λ_y)`. This is block 55 T4's homogeneity argument, extended to lengths.
2. *Its long-wave limit.* At long wavelength, keeping two derivatives, the cubic lattice gives a rotation-invariant quadratic form in `(∇u, ∇λ)`. So every weight-one, covariant, nearest-neighbour field energy that vanishes on uniform fields is

   `F = −K ∫ e^u [A(λ) ∇u·∇λ + C(λ) |∇λ|² + D(λ) |∇u|²]`.

   Uniform fields are excluded from carrying energy, as block 55 excludes the on-site term.
3. *Block 60 T3's second-order jet.* After integrating by parts, it is `A(0) = a`, `C(0) = ap − b`, `D(0) = 0`, with `β = A(0)/(2C(0))`. I normalise `A(0) = 1`, and use `β = 1` (the curvature member, lengths doubling the bend) wherever the comparator is compared.
4. *The free jets.* The completion's free data are:
   - the third-order jet `(A₁, C₁, D₁) = (A′, C′, D′)(0)`;
   - the fourth-order jet `(A₂, C₂, D₂) = (A″, C″, D″)(0)`.

**Examples.**
- The curvature member is `A = e^λ`, `C = e^λ/2`, `D = 0`, with jets `(1, 1/2, 0)` and `(1, 1/2, 0)`.
- Block 110's log-linear completion, the quadratic form without the factor `e^u`, is not of weight one. Neither is block 56's simplest member, which has no lengths. Both lie outside this family.

**The body and the index.**
- A point body's exterior is `u ≈ U₁/r` and `λ ≈ L₁/r`, where `L₁` and `U₁` are the exact `1/r` coefficients.
- Write `σ = −U₁/L₁`. For a body at rest at weak field, `σ = 1/β`, which is `1` here (block 60 T3(b)). For a real body `σ` depends on its content (block 110 T2).
- The index is `n = ℓ/w = χ³/N = 1 + ν₁/r + ν₂/r² + ν₃/r³ + …`.
- `M` is defined by `ν₁ = 2M`, so the first-order turn is `4M/b`.

## (1) The statement attempted

**(a) The exterior to second order, and ν₂.** Take `β = 1`.

*The fields.*
- `λ = L₁/r + l₂/r²`, with `l₂ = (L₁² − 2A₁L₁² − 4D₁L₁U₁)/4`.
- `u = U₁/r + u₂/r²`, with `u₂ = (2A₁L₁² − 2C₁L₁² + 4D₁L₁U₁ + 2D₁U₁² − L₁² − 2L₁U₁ − 2U₁²)/4`.
- Third order is also computed.

*The index coefficient.*

`ν₂/M² = −2(2A₁ − C₁ + D₁σ² − 4D₁σ − 2σ² − σ − 2)/(1 + σ)²`.

*For a body at rest, at general `β`* (with `σ = 1/β`):

`ν₂/M² = −(2A₁β² + 2A₁β − 2C₁β² − 4D₁β − 2D₁ − 2β² − 5β − 3)/(β + 1)²`.

**(b) The classification.**

*The comparator's second order.* At `σ = 1`, `ν₂/M² = 5/2 − A₁ + C₁/2 + 3D₁/2`. So the comparator's `ν₂ = 7M²/4` holds exactly on the plane

`4A₁ − 2C₁ − 6D₁ = 3`

of third-order jets.
- The curvature member, at `(1, 1/2, 0)`, lies on it.
- The constant-coefficient member, at `(0, 0, 0)`, gives `5M²/2`.
- For other `σ` the condition is the quadric set by the formula above.

*Capture* is not a property of any finite jet, because `min r n(r)` depends on the whole exterior. It is exact for bilinear members.

*Bilinear members*, `F = −c Σ (X_y − X_x)(Y_y − Y_x)`:
- Weight one and `D(0) = 0` force `X = w f(ℓ)` and `Y = g(ℓ)`.
- The jet forces `f(1) = 1` and `f′(1) = 1/2`. Normalise `g(1) = g′(1) = 1`.
- Outside the body `X` and `Y` are exactly harmonic, and the index is `n = ℓ f(ℓ)/X`.
- At `σ = 1` (`p = q/2`) the index is the comparator's `(1 + M/2r)³/(1 − M/2r)` identically, so every turn term and the capture at `3√3 M` agree, if and only if

  `ℓ f(ℓ) = ((1 + g(ℓ))/2)³`.

  That gives one member for every `g`. The curvature member is `g = 2√ℓ − 1`. Others include `g = ℓ` and `g = 1 + log ℓ`.

So the curvature member is not the only bilinear member that bends like the comparator. It is the only one among power laws `Y = ℓ^γ`: those have `ν₂ = (17 − 6γ)M²/8`, which is `7M²/4` only at `γ = 1/2`.

*No named clause forces the plane.*
- **Weight one** (the per-tick ledger) defines the family. It leaves `(A₁, C₁, D₁)` free.
- **Kept books.** By block 55, a variational field equation keeps the ledger. Every completion here is variational.
- **The ledger's wall term** (block 60 T1) is `A(0)L₁`, blind to the third-order jet.
- **Blindness to coin rotations.** Coin rotations act on the amplitude's coin, not on `w` or `ℓ`, so every completion is blind to them.

**(c) Third order.**
- The comparator's `128/3` requires `ν₃ = M³`.
- At `σ = 1`, `ν₃/M³ = 5/2 + 7A₁²/6 − 5A₁C₁/6 − 23A₁D₁/6 − 11A₁/4 + 7C₁D₁/3 + 3C₁/2 + 7D₁²/3 + 4D₁ − A₂/3 + C₂/6 + D₂/2`.
- So `128/3` is one further linear condition on the fourth-order jet, `−A₂/3 + C₂/6 + D₂/2 = …`.
- The curvature member satisfies it. So does every matched bilinear member, which is checked for five choices of `g`.

## (2) Steps

**Step 1 (ASSUMED): the long-wave reduction.**
- The exterior's far-field coefficients `ν₁, ν₂, ν₃` are those of the two-derivative continuum field energy.
- Lattice terms with more derivatives change the fields only at higher order in `(spacing/r)²`.
- The discrete exterior of the curvature member is block 110's harmonic `χ, N` in the continuum. Its exact lattice asymptotics are not re-derived here.

**Step 2 (PROVED): the family and its second-order jet.**
- By weight one the rate enters only as `e^u` times invariants of `∇u`, `λ` and `∇λ`.
- At two derivatives there are three such invariants, which gives `A`, `C` and `D`.
- Integrating block 60 T3's jet by parts gives `A(0) = a`, `C(0) = ap − b`, `D(0) = 0`.

**Step 3 (PROVED; CHECKED, family S): the exterior order by order.**
- The radial Euler–Lagrange equations of `r²e^u[A u′λ′ + C λ′² + D u′²]` are solved with the ansatz `U₁/r + ε u₂/r² + ε² u₃/r³`, and likewise for `λ`.
- At first order both fields are harmonic, so the charges are free.
- At orders 2 and 3 the equations are linear in `(u_k, l_k)` with unique solutions (sympy).

**Step 4 (CHECKED, family S): the curvature member.**
- The exact exterior `λ = 2log(1 + a/r)`, `u = log(1 − p/r) − log(1 + a/r)` is reproduced at orders 2 and 3, with `L₁ = 2a` and `U₁ = −(a + p)`.
- `ν₂ = 3a² + 3ap + p²`, which is block 110's.

**Step 5 (PROVED): the turn.** Along a ray `ρ = r n(r)` is conserved (Bouguer).

- The turn is `α = −2b ∫_b^∞ (d log n/dρ) dρ/√(ρ² − b²)`.
- Expanding `log n` in `1/ρ` and using `∫_1^∞ dt/(t^{k+1}√(t² − 1)) = 1, π/4, 2/3` gives

  `α = 2ν₁/b + π(ν₂ + ν₁²/2)/b² + (4ν₁³/3 + 8ν₁ν₂ + 4ν₃)/b³`.
- The comparator's index has `(ν₁, ν₂, ν₃) = (2M, 7M²/4, M³)`, which gives `4M`, `15π/4` and `128/3`.
- Given the first two orders, `128/3` is exactly `ν₃ = M³`.

**Step 6 (PROVED; CHECKED, family B): the classification.**
- Substituting `U₁ = −σL₁` and `L₁ = 2M/(1 + σ)` gives (a)'s `ν₂`.
- At `σ = 1` it gives the plane.
- `ν₃` is linear in `(A₂, C₂, D₂)`, with coefficients `(−1/3, 1/6, 1/2)`.

**Step 7 (PROVED; CHECKED, family W): bilinear members.**

*The form is forced.*
1. Write `X = w^s f(ℓ)` and `Y = w^{1−s} g(ℓ)`. The `|∇u|²` coefficient `s(1 − s)` must vanish, so `s ∈ {0, 1}`, and I take `s = 1`.
2. Then `A = f g′ ℓ` and `C = g′ ℓ² f′`, so `C(0)/A(0) = 1/2` forces `f′(1) = 1/2`.

*The exterior is exact.*
1. The Euler–Lagrange equation in `u` gives `X ΔY = 0`.
2. The one in `λ` gives `X_λ ΔY + Y_λ ΔX = 0`.
3. So outside the content both `X` and `Y` are harmonic: `X = 1 − p/r` and `Y = 1 + q/r`.

*The matched family.*
1. At first order, `λ ≈ q/r` and `u ≈ −(p + q/2)/r`. So `σ = 1` means `p = q/2`.
2. The index `ℓ f(ℓ)/X` equals `((1 + Y)/2)³/X = (1 + M/2r)³/(1 − M/2r)` exactly when `ℓf = ((1 + g)/2)³`, with `q = M`.
3. With the formulas of Step 6, five choices of `g` each give `ν₂ = 7/4` and `ν₃ = 1`.

*Capture and power laws.*
- For the comparator's index, `min r n(r) = 3√3 M`, found exactly by solving `d(rn)/dr = 0`.
- For power laws, `n = (1 + γM/r)^{3/(2γ)}/(1 − M/2r)` and `ν₂ = (17 − 6γ)M²/8`.

**Step 8 (PROVED): the clauses.**
- Every member of the family is of weight one by construction.
- Every member has a variational field equation, so it keeps the ledger (block 55).
- The wall term, the flux of `∂L/∂u′` at large `r`, is `A(0)L₁`. This is checked symbolically, and it is independent of `(A₁, C₁, D₁)`.
- Coin rotations do not act on `(w, ℓ)`.

**Step 9 (CHECKED `[float]`, family N).**
- *The series.* For a generic jet, direct integration of the nonlinear radial equations reproduces the third-order series. The extracted `1/r³` coefficients agree to 4–5 digits for both fields, at `σ = 1` and `σ = 0.6`.
- *Capture.* The capture thresholds of power-law members are 5.406, 5.196, 4.819 and 4.500 for `γ = 1/4, 1/2, 1, 3/2`. Only `γ = 1/2` gives `3√3 = 5.196`.

## (3) Where the route stops

1. **The long-wave reduction** (Step 1) is assumed, not derived for the lattice exterior.
2. **The charge ratio.** The classification at `σ = 1` is for a body at rest at weak field. Real bodies have `σ` set by their content (block 110 T2), and the full `σ`-dependent formula is given for them.
3. **The clauses.** Only the three named clauses are examined, and each leaves the jet free. The other clauses of blocks 53–66 are not examined one by one.
4. **"Bilinear member"** is read as `F = −cΣ(ΔX)(ΔY)` with site functions `X`, `Y` of `(w, ℓ)`. In the narrower reading, bilinear in the fixed pair `(N, χ)`, weight one allows only the curvature member.

## (4) What would finish it

1. A clause that selects the plane `4A₁ − 2C₁ − 6D₁ = 3`. One candidate is a demand that the rays' index depend on the fields only through two harmonic combinations, which would bring in the bilinear structure together with the matching `ℓf = ((1 + g)/2)³`.
2. The exact lattice asymptotics of the exterior.
3. The fourth order, `3465π/64`, which would add a condition on the fifth-order jet.
