# J:derive:the-rest-energy-density-of-a-massive-walker:a2 — a body at rest sits on one sublattice, its chessboard stays home, and a massive walker still feels a chessboard of clocks

**Provenance.** Worker `w-macbookpro90c72-j35f5`, model `claude-opus-5-5`, one session. The claim printed no prior attempts, and there is no `a1` directory on `ai/probes`. Definitions come from the notes on the PR branches of blocks 53–56, 60, 76 and 77 (PRs #8568, #8570, #8571, #8573, #8590, #8611, #8612). Every clause is supplied and nothing is adopted.

**Objects.**
- **The walk.** `H = Σ_j σ_j D_j`, with `(D_j ψ)(x) = (i/2)(ψ(x − e_j) − ψ(x + e_j))`, whose symbol is `sin k_j` (block 54).
- **The massive walk.** `ε(x) = (−1)^{x+y+z}` and `H + mε` (block 77).
- **The clocked walk.** `φ(H + mε)φ = φHφ + m w ε`, with `w = φ² = e^u` (block 77 T3).
- **The source.** `e_x = Re ψ_x†(H_w ψ)_x` (block 55 T1).
- **The simplest member.** `F = (2/γ) Σ_bonds (φ_x − φ_y)²`. Its weak-field law is `(1 − A)u = −(γ/6)(e − ē)/w̄`, where `A` averages over the six neighbours (block 55 T4, block 56).
- **The curvature member.** `F = Σ_x w_x G_x(λ)`: the rates are multipliers and have no stiffness of their own (block 60 T2). Its weak-field laws are `Lap λ = −e/(4K w̄)` and `Lap u = (e + τ)/(4K w̄)`, with `γ = 1/(4K)` (block 60 T3).

## 1. Statement

The task asks three things:
- (a) The site-resolved energy density of a positive-energy walker at the zero: its sublattice structure and its sum.
- (b) The static field that the chessboard part of the source produces, and whether that chessboard of clocks costs energy while no walker feels it.
- (c) Whether the chessboard part contributes to the pull between two bodies at rest at leading order, in the simplest member and in the curvature member.

**Obtained:**
- **(a)** The premise that the density at rest alternates in sign is false for exact rest states. The positive-energy rest states at the zero lie on the `ε = +1` sublattice, so `e_x = m w_x|χ_x|² ≥ 0` there and `0` on the other sublattice, with sum `m`. Every positive-energy eigenstate has `e_x = E|ψ_x|² ≥ 0`. Only the mass part `mε|ψ|²` alternates, with odd-sublattice weight exactly `(E − m)/(2E)`.
- **(b)** In the simplest member, the chessboard part of the source makes a local chessboard of clocks.
  - On a torus the whole mean-removed rest source is a chessboard, and the field is exactly `u = −(γm/(12V))ε`.
  - It costs bond energy.
  - No odd-step operator feels it (block 76 T1). **A massive walker does:** `φ(mε)φ` with `φ = c^ε` is `m(c² − c^{−2})/2 + mε(c² + c^{−2})/2`, a scalar potential plus a mass factor.
  - In the curvature member a chessboard of clocks costs nothing by itself, and its weak-field chessboard response is again local.
- **(c)** No. In both members the pull between two bodies at rest is, to every power of `1/R`, a function of the sources' moments only. The chessboard (staggered) part enters only through terms that decay faster than any power, because both weak-field operators are invertible at `k = π(111)` (symbols `2` and `12`). The `1/R` term is `−(γ/4π) Q_A Q_B/R`, where `Q` is the total energy.

## 2. Steps

**Step 1 (PROVED; CHECKED A1.rest, A1.density). Rest states lie on one sublattice.**
- `ε` anticommutes with `H` (block 77 T3), so `ε` maps `ker H` to itself and `ker H` splits into `ε = ±1` parts.
- On the `ε = +1` part, `(H + mε)χ = mχ`; on the `ε = −1` part the energy is `−m`.
- The zero modes are `e^{iπn·x}u` with `n ∈ {0, 1}³`. The positive rest states are `e^{iπn·x}(1 + ε)u`, and they vanish on every odd site.
- *With a clock field.* For such a `χ`, `(φHφχ)_x` involves only odd neighbours at even `x`, where `χ = 0`. So `e_x = m w_x|χ_x|²` exactly, for any `w`.
- *On the `4³` torus.* `e_x = 2m/V` on the even sites and `0` on the odd sites, with sum `m`. It is non-negative, not alternating.

**Step 2 (PROVED; CHECKED A2.*). Moving eigenstates.**
- `(H + mε)² = H² + m²`, so `E = √(|sin k|² + m²)`.
- For an eigenstate, `e_x = Re ψ_x†(Eψ)_x = E|ψ_x|² ≥ 0`.
- By Hellmann–Feynman, `⟨ε⟩ = ∂E/∂m = m/E`. So the even weight is `(E + m)/(2E)` and the odd weight is `(E − m)/(2E)`.
- The mass part `mε|ψ|²` alternates in sign and sums to `m²/E`. The kinetic part sums to `|sin k|²/E` and fills the odd sites.
- *Exactly at `k = (π/2, 0, 0)`, `m = 3/4`.* `ψ = e^{ik·x}(1 + ε/3)(1, 1)`, `E = 5/4`, weights `4/5` and `1/5`, mass part `9/20`, kinetic part `4/5`.

**Step 3 (CHECKED A3.packet). A packet.** Take the rest state plus the moving state, with norms `2` and `5/2`. Then `Σ e = (m·2 + (5/4)(5/2))/(9/2) = 53/44`, with `43/44` on the even sites and `5/22` on the odd ones. The minimum of `e_x` is `5/704 > 0`. Interference can lower `e_x` at some sites but does not change the sum.

**Step 4 (PROVED; CHECKED B.Aeps, B.identity, B.source, B.field, B.cost). The chessboard's field in the simplest member.**
- `Aε = −ε`, hence `(1 − A)(εf) = ε(1 + A)f`.
- *On the torus.* For the rest state of Step 1, `e − ē = (m/V)ε` exactly: the whole mean-removed source is a chessboard. The weak-field law is solved by `u = −(γm/(12V))ε`, which is `φ = c^ε` with `c = e^{−γm/(24V)}`: clocks run slow on the body's sublattice.
- *Its cost.* The bond energy is `(2/γ)·3V(c − 1/c)² > 0`.
- *A localized body with smooth envelopes.* Write `e = e_s + εe_c`. The chessboard part of `u` then solves `(1 + A)u_c = −(γ/6)e_c`. Since `1 + A` has symbol `≈ 2` on smooth envelopes, `u_c ≈ −(γ/12)e_c`: local, attached to the body.

**Step 5 (PROVED; CHECKED B.feel±1). Who feels a chessboard of clocks.**
- `φ = c^ε` gives `φ_xφ_y = 1` on every bond. So every operator that moves an odd number of steps is unchanged (block 76 T1).
- The on-site term is not. Write `u = u_s + εu_c`; then `w = e^{u_s}(cosh u_c + ε sinh u_c)`, and
  `φ(mε)φ = mεw = m e^{u_s}(sinh u_c + ε cosh u_c)`.
- So a massive walker feels a chessboard of clocks in two ways:
  - an additive scalar potential `m e^{u_s} sinh u_c`, of the same sign for both signs of energy, giving a force `−m∇ sinh u_c` where the envelope varies;
  - a mass factor `cosh u_c`.
- A body at rest therefore sits in its own chessboard. That is a self-energy of order `γm²/V` on the torus, and local for a localized body.
- *In the curvature member* the rates are multipliers (block 60 T2). A chessboard of clocks at uniform lengths costs nothing, because `F = Σ w_x G_x(λ)` vanishes. The rates are fixed through the lengths' stationarity, and at weak field `Lap u = (e + τ)/(4K w̄)` gives the same local chessboard response (Step 6).

**Step 6 (PROVED). The chessboard part of a field is local.**
- In both members the weak-field `u` is `κ(k) ê(k)` in Fourier space, with:
  - `κ = −(γ/6)/(1 − Â(k))`, where `1 − Â = 1 − (1/3)Σcos k_j`, for the simplest member;
  - `κ = −(γ)/Δ(k)`, where `Δ = Σ 2(1 − cos k_j)`, for the curvature member at rest (`τ = 0`, `γ = 1/(4K)`).
- Both symbols vanish only at `k = 0`, and at `π(111)` they equal `2` and `12` (CHECKED C.symbols).
- So `κ` is analytic on a neighbourhood of every `k ≠ 0`, in particular near `π(111)`. The part of the source carried by wave vectors away from `0`, including the staggered part, produces a field that is the Fourier transform of a smooth function. It decays faster than any power of the distance.

**Step 7 (PROVED). The pull between two bodies at rest.**
- *Setup.* At weak field and linear order in each body, the energy of `A` in `B`'s field is `U(R) = Σ_x e_A(x)u_B(x)` (block 54: energy scales with `w`). In Fourier space,
  `U(R) = ∫ ê_A(k)* ê_B(k) κ(k) e^{ik·R} dk/(2π)³`.
  The sources are localized with all moments finite, so `ê_A` and `ê_B` are `C^∞`.
- *The split.* Split with a smooth cutoff `χ(k)` that equals `1` near `k = 0` and vanishes outside a small ball.
  - `U_far` has a `C^∞` periodic integrand, so it is `O(|R|^{−n})` for every `n`.
  - `U_near` depends only on the germs of `ê_A` and `ê_B` at `0`, that is, on the moments of the sources.
- *The staggered data enter only `U_far`.* These are `ê(π(111)) = Σ ε(x)e_x` and the behaviour of `ê` near `π(111)`.
- *Conclusion.* The pull to every power of `1/R` is a function of the moments. The leading term is `−(γ/6)(6/(4π|R|))Q_AQ_B = −(γ/4π)Q_AQ_B/R` in both members, where `Q` is the total energy. For a positive-energy rest state that is `m w`, whatever its sublattice structure.
- For smooth envelopes, the moments of `εe_c` are derivatives of `ê_c` at `π(111)`, and so negligible as well.

**Step 8 (NUMERICAL, not load-bearing; `N.field`).** Solve `(1 − A)u = e` on a `48³` torus for two bodies with total `2` and dipole `0`:
- smooth weights `(1/2, 1, 1/2)`, with staggered charge `0`;
- all weight `2` on the even site, with staggered charge `2`.

Their fields at `(0, R, 0)` differ by `R^{−3}` × 0.29, 0.245, 0.232, 0.225 for `R` = 4, 8, 12, 16. That is a quadrupole difference; the staggered charge adds no `1/R` term.

**ASSUMED:** block 54's reading that a body's energy scales with the local rate. Two linearization steps are also taken: in each body, and in the weak field.

## 3. The first failing step for the HIT

The task's HIT condition is "the chessboard component contributes to the pull between two bodies at rest at leading order". It fails at Step 6 in both members, because the weak-field operators are invertible at `π(111)`.

The task's premise that the density of a body at rest alternates in sign also fails:
- for exact rest states (Step 1);
- for the full density of every positive-energy eigenstate (Step 2).

## 4. What would finish or extend it

1. **The strong field.** Check block 56's nonlinear law `((12/γ)(1 − A) + K)φ = 0` and block 60's T4 solution for a sublattice-supported source. Linearity in `φ` (resp. `χ`) suggests the same locality, with `K = diag(m ε|χ|²)` supported on one sublattice.
2. **A short-range force.** Where two massive bodies' chessboard fields overlap, the scalar potential `m sinh u_c` of Step 5 couples them. This is a short-range force not present for massless walkers. Its sign and size, `O(γm²)`, are not computed here.
3. **Block 76's induced-energy reading.** There, the chessboard is a zero mode of the field energy (block 76 T4: the linearized law never fixes the chessboard component). Yet a massive body at rest has staggered charge `ê(π(111)) = Q ≠ 0` (Steps 1 and 4). In that reading the static law would have a zero mode driven by a nonzero source. This is worth a separate probe: it may make that reading inconsistent for massive bodies at rest.

## 5. Running it

```
python3 probes/work/derive/the-rest-energy-density-of-a-massive-walker/w-macbookpro90c72-j35f5/check.py
```

Requires `sympy`; `numpy` is used only for the labelled illustration. The run takes about 1 s, with exact Gaussian-rational arithmetic on the `4³` torus at `m = 3/4`.
