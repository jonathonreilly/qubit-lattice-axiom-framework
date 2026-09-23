# J:derive:internal-hop-energy-and-the-two-masses:a1: the rates exceed the lengths by the hop energy plus the confining agent's stress; the two-step virial ties the hop energy to the agent's gradients; at strong field P = Q needs a tuned internal hop energy that exists only up to a finite strength

**Provenance.**
- Worker `w-macbookpro90c72-jdb03`, model `claude-opus-5-5`, one session. Attempt 1 of 2; the claim printed no prior attempts.
- **Overlap to declare.** The same model, on this machine on 2026-09-22, did `J:derive:bound-bodies-and-the-two-far-fields:a1` (issue #8649, worker `j7e6e`, unrefereed).
  - That unit derived the strong-field equations and `P − Q = (1/8K) Σ [2τ − e(1/w − 1)]/χ` for content without an agent, and a virial for a body bound by its own field.
  - S2 here re-derives those equations from block 60's bond form, now **with the confining agent's stress**, and checks them symbolically. #8649 is not used as authority.
  - Everything else is new to this attempt:
    - the confining agent and its stress (a);
    - the two-step virial with its exact cubic remainder, and the finite-box no-go;
    - the executed staggered-mass bags;
    - the per-site form of `P − Q` with the weight `(3w − 1)/w`;
    - the two-site body's exact `P = Q` locus and its maximal strength (b);
    - the consequence for bending over fall (c).
- Definitions come from the notes on the PR branches of blocks 59 (#8581) and 60 (#8590): the bond form, T2 to T4, the crossing factor `√(w_xw_y)/(χ_xχ_y)`. The walk is block 54's `H = Σ_j σ_j S_j`. The staggered term is block 77's `mε` (via the fork probe's summary).
- Nothing is adopted and no gravitational claim is made. The agent and its dependence on lengths are **supplied**.

## 1. The statement attempted

**Setting.** Rates `w = e^u` and lengths `ℓ = χ² = e^λ` on `Z³`, with walls held at `w = ℓ = 1`. Block 60's curvature member in bond form: `F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`, `N = wχ`.

**Content.**
- `⟨H⟩ = Σ_b h_b √(w_xw_y)/(χ_xχ_y) + Σ_z w_z (r_z + a_z(λ))`: bare hop energies `h_b` and on-site energies `r_z` (rest energy, if any).
- A **supplied confining agent** `a_z`, an on-site term whose dependence on lengths is supplied.
- Hop energy `t_b`, `τ_z = ½ Σ_{b∋z} t_b`; energy per tick `e_z = ∂⟨H⟩/∂u_z`.
- **Agent's stress** `s_z = −∂(w_z a_z)/∂λ_z`. Totals: `T = Στ`, `S = Σs`, `E = Σe`.

**Claims.**

**(a) Weak field, second-order theory.**
- The lengths carry `E` and the rates `E + T + S` (in units of `1/(4K)`): `Δλ = −e/(4K)`, `Δu = (e + τ + s)/(4K)`. So the two far-field coefficients are equal iff `T + S = 0`. **(CHECKED A.eqs)**
- **The two-step virial.** For every stationary state of `H_hop + A`, with `A` any on-site agent (e.g. `V(x) + M(x)ε(x)`) and finite `⟨x²⟩`, the dilation `G_P = ½ Σ_j {x_j, K_j}`, `K_j = (T_j² − T_j^{−2})/4i`, gives exactly

  `T = ⟨W⟩ + ⟨Σ_j σ_j S_j³⟩`, with `W = i[G_P, A]`.

  `W` sees only the agent's gradients (reach 2): it is zero for constant `V` and constant `M`, since `G_P` commutes with `ε`. **(PROVED; CHECKED A.virial on `Z³`, 128 basis vectors)**
- **No exact lattice dilation.** No operator `G` on a finite box has `i[H_hop, G] = H_hop`. The residue `⟨Σσ_j S_j³⟩` is cubic in the lattice momentum and is not an agent's property.
- **Consequences:**
  - A **length-blind agent** (`S = 0`), for example block 77's staggered term timed by the local clock, leaves the rates heavier than the lengths by `T`, the agent's lattice virial plus the cubic term.
  - Executed staggered-mass bags have `T/E = 0.50` to `0.52`, so the ratio of rates to lengths is about 1.5.
  - An agent whose energy follows stretched distances has `S = −⟨x·∇A⟩`. It levels the two masses only up to `⟨W − x·∇A⟩ + ⟨Σσ_j S_j³⟩`: executed `(T + S)/E = 0.063, 0.038, 0.023` as the bag widens from radius 2.6 to 4.3.
  - **The role of the agent's own stress:** it is exactly what must cancel the hop energy. This is the von Laue/Tolman mechanism, named as a comparator only.

**(b) Strong field.**
- At every strength (**PROVED; CHECKED A.eqs**):
  - `Δχ = −e/(8KN)`, `ΔN = (e + 2τ + 2s)/(8Kχ)`;
  - `8K(P − Q) = Σ_z [τ_z(3w_z − 1)/w_z + 2s_z − r_z(1 − w_z)]/χ_z`, where `r` is the on-site energy per tick, agent included.
- So `P = Q` iff that sum vanishes. Internal hop energy raises `P` where clocks run faster than a third and lowers it where slower.
- **A symmetric two-site body** (rest energy `m` per site, one internal bond of bare hop energy `h`, `μ = m/8K`, `η = h/8K`, `G = g(z,z) + g(z,z′)`):
  - `P = Q` iff `η = 2μχ²(χ − 1)/(3 − 2χ)` and `Gμ = χ(χ − 1)(3 − 2χ)/(2 − χ)` with `χ ∈ (1, 3/2)`. Equivalently, per site `τ/(mw) = (1 − w)/(3w − 1)`, with `w > 1/3`.
  - The locus reaches `Gμ = 0.22374`, at the root `χ = 1.31472` of `4χ³ − 17χ² + 20χ − 6`, and no further.
  - Beyond that strength `P < Q` for every internal hop energy `η ≥ 0`.
  - **(PROVED; CHECKED B.dimer; executed control:** the constructed solution makes the full ledger stationary to `4·10⁻¹⁰` on an `8×7×7` box.)

**(c) Bending over fall.**
- The ratio is `1 + 2Q/(P + Q) = 2 − (P − Q)/(P + Q)`: exactly 2 on the `P = Q` locus.
- For the two-site body beyond `Gμ = 0.22374` it exceeds 2 for every internal hop energy `η ≥ 0`.
- Pinned bodies (block 60 T4) lie between 2 and 3.

## 2. Steps

**S1 (definitions).**
- `S_j = (T_j − T_j†)/2i`, `C_j = (T_j + T_j†)/2`, `(T_jψ)(x) = ψ(x + e_j)`.
- Block 60: `F` in bond form, walls held at 1. Block 59: bonds crossed at `√(w_xw_y)/ℓ_b`, `ℓ_b = χ_xχ_y`.
- `P_z = (ΔN)_z` and `Q_z = −(Δχ)_z` at the content's sites. Far away `χ − 1 = Qg` and `1 − N = Pg`; the lengths carry `2Q`, the rates `P + Q` (block 60 T4(d)).

**S2 (PROVED; CHECKED A.eqs, sympy with symbolic rates, lengths, hop and on-site energies and an arbitrary agent function on a box).**
- **Differentiation.**
  - `∂𝓔/∂u_z = e_z + 8K N_z(Δχ)_z`.
  - `∂𝓔/∂λ_z = −τ_z − s_z + 4K[N_z(Δχ)_z + χ_z(ΔN)_z]`.
  - `e − τ = w(r + a)`.
- **Stationarity** gives `Δχ = −e/(8KN)`, `ΔN = (e + 2τ + 2s)/(8Kχ)`.
- **Per site.** `8K(P_z − Q_z) = (e + 2τ + 2s)/χ − e/(wχ)`, which with `e = w(r + a) + τ` is the form in (b).
- **Weak field.** `χ = 1 + λ/2`, `N = 1 + u + λ/2` to first order gives `Δλ = −e/(4K)`, `Δu = (e + τ + s)/(4K)`. So `λ ≈ Eg/(4K)` and `u ≈ −(E + T + S)g/(4K)` far away.
- **Why the field is sourced only by the content.** Outside the content's support `e = τ = s = 0`, so `χ` and `N` are harmonic there.

**S3 (PROVED; CHECKED A.virial exactly on `Z³` with finitely supported vectors). The two-step virial.**
- **The identity.** On `Z`, `[S_j, x_j] = −iC_j`, and `K_j = S_jC_j` commutes with `S_j` and `C_j`. So `[σ_lS_l, {x_j, K_j}] = −2iδ_{lj} σ_l C_l K_l`, and `i[H_hop, G_P] = Σ_j σ_j C_j K_j = Σ_j σ_j S_j C_j²`.
- **The remainder.** `C² + S² = 1` gives `H_hop − H₃ = Σ_j σ_j S_j³`.
- **Invariance.** `K_j` is two-step, so it commutes with `ε = (−1)^{x+y+z}`, and `x_j` is diagonal. Hence `[G_P, ε] = 0` and `[G_P, c₁ + c₂ε] = 0` for constants.
- **The agent's virial.** `W = i[G_P, A] = (i/2) Σ_j {x_j, [K_j, V] + [K_j, M]ε}`. It depends only on differences of `V` and `M` two sites apart. For smooth states and agents it tends to `x·∇V + (x·∇M)ε`.
- **Stationary states.** `⟨[H, G_P]⟩ = 0` (for bounded states in the domain of `G_P`; the bag states decay exponentially). Hence `⟨H₃⟩ = ⟨W⟩` and `T = ⟨W⟩ + ⟨Σσ_jS_j³⟩`.
- **Why two steps.** The one-step dilation `D = ½Σ{x_j, S_j}` gives `i[H_hop, D] = Σσ_jS_jC_j`, which reverses sign at the doublers. It also fails to commute with `ε`, so a constant staggered mass would enter its virial.
- **CHECKED exactly** on the 128 basis vectors of `{−1, 0, 1, 2}³ × coin`, with rational quadratic `V` and `M`:
  - the identity;
  - the cubic remainder;
  - `[G_P, ε] = 0`;
  - the constant-agent commutator;
  - the reach of `W`.

**S4 (PROVED; CHECKED). No exact lattice dilation.**
- On a finite box, `i[H, G] = H` implies `tr H² = tr(i[H, G]H) = i tr(HGH − GHH) = 0`, so `H = 0`.
- The walk on `2³` has `tr H_hop² = 12`.
- So on the lattice the virial must trade `H_hop` for another operator. `H₃` is the choice that commutes with the staggered term, and it leaves the exact remainder `Σσ_jS_j³`.

**S5 ((a) assembled; the numbers EXECUTED, floating point).**
- **The mass difference.** `M_rate − M_len = T + S = ⟨W⟩ + ⟨Σσ_jS_j³⟩ + S`.
- **Length-blind agent** (`S = 0`): the difference is the agent's lattice virial plus the cubic term.
  - Block 77's staggered term, timed by the local clock and blind to lengths as supplied, is such an agent.
- **An agent following stretched distances** (`a(ℓ·x)`, so `S = −⟨x·∇A⟩`): the difference is `⟨W − x·∇A⟩ + ⟨Σσ_jS_j³⟩`, lattice terms that vanish in the continuum limit.
- **Executed bags.** `A = (m₀ + v r²)ε` on `L³` boxes (`L = 16, 20, 24`), lowest positive state:
  - `E = 0.768, 0.589, 0.464`;
  - `T/E = 0.496, 0.515, 0.519`;
  - `⟨H₃⟩ − ⟨W⟩ = 5·10⁻⁷` to `2·10⁻⁷` (walls and solver);
  - `(T − ⟨x·∇A⟩)/E = +0.063, +0.038, +0.023` at radii `2.57, 3.37, 4.31`.

**S6 ((b) PROVED; CHECKED B.dimer). The two-site body.**
- **Setup.** By symmetry `χ`, `N`, `P`, `Q` are equal at the two sites. `τ = ½hw/χ²` and `e = mw + τ`. With `w/N = 1/χ`:
  - `Q = e/(8KN) = μ/χ + η/(2χ³)`;
  - `P = (e + 2τ)/(8Kχ) = NA`, with `A = (μ + 3η/(2χ²))/χ²` and `N = 1 − PG`, so `P = A/(1 + AG)`;
  - `χ = 1 + QG`.
- **The locus.** `P = Q ⟺ A(1 − QG) = Q ⟺ A(2 − χ) = Q ⟺ η = 2μχ²(χ − 1)/(3 − 2χ)`. Substituting into `χ = 1 + QG` gives `Gμ = f(χ) = χ(χ − 1)(3 − 2χ)/(2 − χ)`.
- **Its range.** Any `P = Q` solution has `N = 2 − χ > 0` and `f(χ) = Gμ > 0`, so `χ ∈ (1, 3/2)`. There `w = (2 − χ)/χ > 1/3`.
  - `f′ = 0 ⟺ 4χ³ − 17χ² + 20χ − 6 = 0`, which has one root in `(1, 3/2)`: `χ* = 1.31472`, `f(χ*) = 0.22374`.
- **Beyond the maximum.** For `η ≥ 0`, `χ` is unique and continuous in `η`: `χ − 1` increasing against a decreasing right-hand side. Also `0 < P < 1/G`, so every solution is admissible, and `P − Q < 0` at `η = 0` (`P = Qw`). So for `Gμ > f(χ*)`, `P − Q < 0` for all `η ≥ 0`.
- **The general body.** For a body of several sites the same S2 relations give block 60 T4's structure: `χ = 1 + Σ_z Q_z g(·, z)`, `N = 1 − Σ_z P_z g(·, z)`, with the finite system `Q_z = e_z/(8KN_z)`, `P_z = (e_z + 2τ_z + 2s_z)/(8Kχ_z)`. Existence and uniqueness are not claimed in general: T4's convex function used `e = mw`.
- **Executed.** On an `8×7×7` box (`G = 0.3048`), `P − Q` on the locus is `4·10⁻¹⁴`. The full bond-form ledger evaluated at the constructed `χ`, `N` has gradient `4·10⁻¹⁰` over all 784 variables. The largest `P − Q` over `η ≥ 0` is `+0.043` at `Gμ = 0.20`, `−0.046` at `0.25`, and `−0.296` at `0.40`.

**S7 ((c)).**
- Bending over fall is `1 + 2Q/(P + Q)` (block 59 T4 with block 60 T4(d)).
- It equals 2 exactly on the locus. For the two-site body beyond `Gμ = 0.22374` it exceeds 2 for every `η ≥ 0`.
- In general it exceeds 2 iff `P < Q`: rest energy, and hop energy where clocks run below a third, push it up; hop energy where clocks run faster pulls it down.

## 3. The first failing step

None for the claims made. The limits:
1. **The agent's dependence on lengths is a supplied clause.** Which agent the framework has decides `S`.
2. **The general several-site body** at strong field is reduced to a finite system; its existence and uniqueness are not proved.
3. **The two-site body** is the one case solved in closed form.

## 4. What would finish it

1. **A derived confining agent.** Whether block 77's staggered term, or a length-dependent version of it, is the framework's agent. As supplied it is blind to lengths, so the bag bodies have unequal masses by `T ≈ E/2`.
2. **A convexity argument** for the several-site strong-field system, extending T4's `Φ`.
3. **The bag body at strong field**, self-consistently: the state and the field solved together.

## 5. Running it

```
python3 probes/work/derive/internal-hop-energy-and-the-two-masses/w-macbookpro90c72-jdb03/check.py
```

The run takes about 10 s. It prints three exact checks, then two floating-point notes, then the SUMMARY and HIT lines.
