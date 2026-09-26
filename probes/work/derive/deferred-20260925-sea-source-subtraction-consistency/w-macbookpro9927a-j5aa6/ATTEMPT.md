# The sea as a source on an evolving lattice: exact without the mass, a cranking counterterm with it

Task `J:derive:deferred-20260925-sea-source-subtraction-consistency:a1`, worker `w-macbookpro9927a-j5aa6`, model claude-opus-5-5 (owner-requested recovery).

- `check.py`: exact sympy, under 1 s, 9 checks.
- `make_status.py` writes `RECOVERY_STATUS.json`: the sha256-verified heads of the source note and the `origin/main` SHA.

## Sources, corrections and overlap

**The recovered note.** Block 147 (PR #9240, open, not on main).
- Task's frozen head: `b88ec3d5f3`, sha256 of the note `a630ce79…`.
- Current head: `328ab48910`, sha256 `ae09658f…`. It adds three things:
  - T1(e): with block 146's pressure the massless sea has `p = ρ/3`, and the massive sea `0 < p/ρ < 1/3`;
  - the count of all eight light species;
  - a panel note: which zero the member sees is a reading question.

**Taken from block 147's current head, as supplied clauses:**
- block 60's crossing of bonds: hopping is divided by `ℓ`, and the staggered mass is not;
- block 139's staggered mass and zero of energy;
- block 146's zero-mode constraint and its first law `dm/dλ = −3pℓ³` (`ℓ = e^λ`).

`origin/main` is `25b8c1874f`.

**Corrections preserved.**
- The equations of state in T1(e) are kept.
- No vacuum is selected. Which zero the member sees stays the owner's.
- Free fermions and fully occupied hard-core hopping are kept distinct.

**Related prior work.**
- **#9259** (mine) derived the cranking inertia of the same half-filled staggered sea. Its dilation part is reused here (M2).
- **#9198** (mine) gave `I = ⟨|s|⟩`.
- The related task `nonlinear-moving-source-completion` was released by me as broad. It is not duplicated.
- The claim printed no prior attempts on this problem.

## 1. Statement attempted

**Setting.** A closed lattice is stretched uniformly, `ℓ(t) = e^{λ(t)}`, and the walker's plane-wave block on `(k, k + (π,π,π))` is `H_ℓ = (σ·s/ℓ) ⊗ τ_z + μ τ_x`. The sea is the free half-filled state. We use block 146's first law `dm/dλ = −3pℓ³`.

- **(a) Massless.**
  - `H_ℓ = H₁/ℓ`. So every stationary state keeps its occupations for every history `ℓ(t)`, and the sea's energy is exactly `−I/ℓ` per site, with `p = ρ/3`.
  - Measuring energy from the sea at every length needs the counterterm `m_ct = +I/ℓ` with `p_ct = ρ_ct/3`.
  - A subtraction constant in time (the sea's value at one length `ℓ₀`) has `p = 0` and leaves `I/ℓ₀ − I/ℓ` in the zero mode.
  - So block 147 T3's proof sentence, "the subtraction is a constant per site", holds in space, not in time. T3 holds with the ℓ-dependent counterterm.
- **(b) Massive (`μ > 0`).**
  - `‖[H_ℓ₁, H_ℓ₂]‖² = 16μ²|s|²(1/ℓ₁ − 1/ℓ₂)²` per block.
  - A sea started in the instantaneous ground state leaves it at first order in time, in every block with `μ|s| ≠ 0`, wherever `λ̇ ≠ 0`.
  - So neither the instantaneous energy `−⟨√(μ² + s²/ℓ²)⟩` nor its subtraction is the evolving sea's energy at any finite rate.
  - At leading adiabatic order (ASSUMED A1), the missing term is `½ m_λ λ̇²` per site, with `m_λ = ⟨μ²|s|²/(4ℓ²E⁵)⟩` and `E = √(μ² + s²/ℓ²)`. This is the dilation part of the cranking inertia (#9259).
  - The prescription `L_sea = ⟨E⟩ + ½ m_λ λ̇²` is conditional and consistent: its Noether energy together with the member's is conserved.
- **(c) Hard core.** Fully occupied hard-core hopping is blocked. Its energy does not depend on `ℓ`, and its pressure is zero.

## 2. Steps

**S1. The first law for the sea, its counterterm, and a constant subtraction. PROVED; CHECKED K1, K2.**
- Block 146's first law assigns `p = −(dm/dλ)/(3ℓ³)` to any `m(λ)`.
- For `m = −I/ℓ`, `p = −I/(3ℓ⁴) = ρ/3`.
- For `m_ct = +I/ℓ`, `p_ct = ρ_ct/3`, so the counterterm is itself top-speed-like content, of positive energy.
- For `m = I/ℓ₀` (constant), `p = 0`. Added to the sea it leaves `I/ℓ₀ − I/ℓ`, which is not zero for `ℓ ≠ ℓ₀`. So that sea does not drop out of the zero mode.
- K2 restates block 147's massive-mode ratio `p/ρ = y/(3(μ² + y))`, with `y = s²/ℓ²`.

**S2. Commutation. PROVED; CHECKED C1.**
- `‖[H_ℓ₁, H_ℓ₂]‖²_F = 16μ²|s|²(1/ℓ₁ − 1/ℓ₂)²`, computed symbolically on the `4×4` block.
- For `μ = 0`, `H_ℓ = H₁/ℓ` exactly. The propagator is then `exp(−i H₁ ∫dt/ℓ)`, which keeps every eigenstate of `H₁` up to a phase. So the massless sea's energy is `−I/ℓ` exactly, for every history.
- The same holds for any content whose Hamiltonian is pure hopping. That includes hard-core hopping and every stationary state of it (block 146 T3's `1/ℓ` for top-speed walkers is the one-walker case).

**S3. Leaving the instantaneous sea. PROVED; CHECKED A1.**

*The reduction.* `σ·s` has eigenvalues `±|s|`, and its eigenvectors do not depend on `ℓ`. So each block splits into two sectors `h = (±|s|/ℓ)τ_z + μτ_x`, and the evolution keeps each sector. The free sea puts one fermion in each sector's lower state.

*The first-order amplitude.* In one sector, write `c₊(τ) = ⟨+(τ)|ψ(τ)⟩`, with `ψ(0) = |−⟩`. Then:
- `ċ₊ = ⟨∂_τ+|ψ⟩ − iE₊c₊`;
- so `ċ₊(0) = ⟨∂_τ+|−⟩ = −⟨+|∂_τ−⟩ = −λ̇⟨+|∂_λ−⟩`;
- and `⟨+|∂_λ−⟩ = ⟨+|∂_λh|−⟩/(E₋ − E₊)`, with `|⟨+|∂_λh|−⟩|² = μ²s²/(ℓ²E²)`.

*Conclusion.*
- The amplitude is nonzero iff `μ|s| ≠ 0`.
- Hence `c₊(τ) = −λ̇⟨+|∂_λ−⟩τ + O(τ²)` and `E(τ) − E₀(τ) = 2E|c₊|² > 0` for small `τ ≠ 0`.
- The many-walker energy exceeds the instantaneous sea energy by the sum over sectors.

**S4. The leading counterterm. PROVED given A1; CHECKED M1, M2.**
- *The dressing.* The first-order adiabatic amplitude is `c₊ = iλ̇⟨+|∂_λ−⟩/(2E)`. Its energy is `2E|c₊|² = ½ m λ̇²`, with `m = 2|⟨+|∂_λh|−⟩|²/(2E)³ = μ²s²/(4ℓ²E⁵)` per sector (M1).
- *Per site.* There are two sectors per block and half a block per site, so `m_λ = ⟨μ²|s|²/(4ℓ²E⁵)⟩` per site.
- *The cross-check.* At `ℓ = 1` this is four times #9259's dilation part `⟨μ²|s|²/(16E⁵)⟩` per unit `δh`, since `λ = h/2` at first order (M2). It is the same inertia.
- *Scope.* The dressing follows the instantaneous rate and is reversible. It is not particle production. Irreversible production is beyond every order of the adiabatic expansion for analytic histories (Landau–Zener type). That is not used here.

**S5. Conservation of the prescription. PROVED; CHECKED N1.**

Take `L = ½(m_λ + c)λ̇² − e(λ) − V(λ)`, where:
- `e = −⟨E⟩` is the instantaneous sea energy;
- `c` and `V` are the member's homogeneous kinetic coefficient and potential, generic functions.

Then `dh/dt = λ̇·(Euler–Lagrange)`, so the energy `e + V + ½(m_λ + c)λ̇²` is conserved on solutions. Using `e` alone, and dropping `½m_λλ̇²`, gives a source that is conserved as a fluid by construction (S1). It still differs from the evolving sea's energy by `½m_λλ̇²` at this order.

**S6. Hard core. PROVED; CHECKED H1.** With one record per site at full occupation, every hop targets an occupied site. So the hopping annihilates the state, its energy is independent of `ℓ`, and `p = 0`.

## ASSUMED

- **A1.** The leading-order adiabatic expansion. For a smooth history with gap `2E ≥ 2μ > 0`, the state is the instantaneous ground state plus the first-order admixture `c₊ = iλ̇⟨+|∂_λ−⟩/(2E)`, up to `O(λ̇², λ̈)`. This is the standard adiabatic theorem with its first correction (Kato 1950; Nenciu 1993). It is used only in S4.
- **A2.** The supplied clauses as stated in block 147: crossing of bonds, the staggered mass, block 146's first law, and the free half-filled sea (exclusion supplied, block 128).

## 3. Result, first unresolved step and obligations

**Result.**
- Massless: the free instantaneous sea energy is exact for every history. Its subtraction is consistent with the ℓ-dependent counterterm `+I/ℓ`, `p = ρ/3`, and block 147 T3 holds in that sense.
- Massive: neither the instantaneous energy nor its subtraction is the evolving sea's energy at any finite rate. The consistent conditional prescription at leading adiabatic order adds the cranking term `½m_λλ̇²`.

**First unresolved step.** Beyond leading adiabatic order. This covers irreversible pair creation for a given history (exponentially small for analytic histories) and its back-reaction on the zero mode.

**Remaining obligations.**
1. Add the sea's inertia to the member's zero mode. The kinetic coefficient becomes `c_k + m_λ/ℓ³` per unit volume, with `c_k = −24α < 0` (block 146). The question is whether this changes block 147 T2's bounce at `ℓ = I/m₀` (massless: `m_λ = 0`, unchanged) and the threshold `m₀ > μ` (massive).
2. The half-filled hard-core sea with the staggered mass. It does not commute either; exact small cases would settle its counterterm.
3. Non-uniform stretches (shear) of the massive sea. #9259 gives their inertia at `ℓ = 1`.
