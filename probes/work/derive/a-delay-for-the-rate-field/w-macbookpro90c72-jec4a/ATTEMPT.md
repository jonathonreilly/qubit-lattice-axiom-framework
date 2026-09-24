# A rate field with its own motion: derivation attempt 3 of 4

Worker `w-macbookpro90c72-jec4a` (claude-opus-5-5), unit `J-derive-a-delay-for-the-rate-field-a3`.

**Sources.**
- The task's statement of blocks 53–55: the rate `w = e^u`, the walk `H_w = φHφ`, the ledger `⟨H_w⟩ + F`, `F = (2/γ)Σ_bonds(φ_x − φ_y)²`, and the static law.
- Block 57, "a delay for the rate field" (PR #8578, head `621c0c56`). Its T1–T3 were read after I formed my plan.

`check.py` is exact (sympy) in six families, plus one labelled floating-point simulation. It runs in about 8 s.

**Prior attempt and overlaps.**
- I formed the plan below before reading anything of attempt a4 (`w-jonathonsmac4f50-j519d`, claude-opus-5-5). It is unrefereed, so nothing of it is GIVEN.
- a4 reaches the same (a) and the same (b) at continuum level. It also gives the lattice retarded kernel's odd terms and the eccentric-orbit power.
- This attempt re-derives both independently. The odd terms come from a small-momentum expansion (S7). The eccentric factor is checked exactly at five eccentricities (S9).
- It adds two things:
  - (b) at lattice level: the field's phase-velocity floor, and a hopping point source that radiates for every `c` (S5, S6);
  - the requested front-speed simulation.
- Related earlier unit of mine: #8830, what fixes the powers and the sign of the kinetic term. That was a different task, on the curvature member's kinetic term. There, agreement of speeds was likewise a choice, not forced.

## 1. The statement attempted

**(a) The kinetic term.**
- Under a change of unit (`w → sw` with the ambient time `t → t/s`), an on-site term `u̇²w^α` has weight one iff `α = −1`. So the term is `(1/(2γc²))Σ_x u̇_x²/w_x`.
- Under a general change of parameter `t → f(t)` (with `w → w/f'`), this term survives iff `f'' = 0`. The term with the rates referred to one clock of the system, `(u̇_x − u̇_ref)²/w_x`, survives every `f` (block 57 T1, T3).
- The equation of motion is:

  ```
  u'' − u'²/2 = −γc² w_x [ (12/γ) φ_x(φ_x − avg φ) + e_x − μ ].
  ```

- At weak field about a uniform `w̄`:

  ```
  u'' = c² w̄² Lap u − γ c² w̄ (e − μ),    Lap u = Σ_y(u_y − u_x) = 6(avg u − u_x).
  ```

  In the task's form `c²w̄² × (Lap/6) × const`, the constant is 6.
- About any static background, the coefficient of a neighbour is `c²w_x^{3/2}w_y^{1/2}`, which tends to `c²w_x²`. So changes travel at `c·w_x` sites per ambient tick: `c` sites per local tick.
- Executed: a weak source switched on at `t = 0` gives half-rise fronts moving at 1.03 and 2.05 sites per ambient tick at `w̄ = 1` and `2`. The ratio is 2.000.

**(b) Is `c` forced?**
- Not by covariance, and not by scale covariance. The whole construction is consistent, with weight one, for every `c > 0`, so `c` is a second pure number.
- The walker's group speed is at most 1 per local tick, with supremum 1. So no ever-growing wake for any smooth body requires `c ≥ 1`. This is an inequality, not an equality.
- On the lattice the field's phase velocity lies between `(2/π)c` and `c`. It reaches `(2/π)c` at the zone boundary, because `sin(x/2) ≥ x/π` on `[0, π]`.
- A point source hopping one site at a time resonates with some field mode for every `c`: the `m = 1` harmonic of its hopping, or the ordinary lattice Cherenkov condition. So no value of `c` removes the wake of a lattice-scale hopping body. The requirement constrains `c` only for smooth bodies.

**(c) Slow sources and radiation.**
- The static law is the limit `ω → 0`. The first retarded corrections on the lattice are the odd terms of the kernel `(p² + λ²)^{−1}`, with `λ = −iω/(cw̄)`:
  - `−λ/(4π)`, the same at every site, so it multiplies the total charge;
  - `−λ³(|x|² − 3/4)/(24π)`.
- The monopole is silent: the charge is the conserved energy, with its mean removed. The dipole is silent: matched pulls conserve the dipole moment of energy.
- The leading power is the scalar quadrupole, trace included:

  ```
  P = (γ/(240π c⁵)) < (tr Q''')² + 2 Q''':Q''' >       (local units),
  ```

  with `Q_ij = Σ E x_i x_j`.
- For two bodies circling at separation `d`: `P = (16/15)G⁴μ²M³/(c⁵d⁵)`, with `G = γ/(4π)`, `M = E₁ + E₂` and `μ = E₁E₂/M`.
- On a Kepler ellipse the time average carries the factor `(1 + 99e²/32 + 51e⁴/128)/(1 − e²)^{7/2}`. That is a4's closed form, checked exactly at five eccentricities.

**(d) What is added to the clauses.**
- A kinetic term for the rates, with a coefficient `1/(2γc²)`.
- A second pure number `c`.
- A reference clock (the walls') or a master parameter. The on-site term needs one of them.

## 2. Steps

**S1 (PROVED; CHECKED K1).** The weight and the reparametrisation.
- Weight: `(s u̇)²(s w)^α = s^{α+2}u̇²w^α` equals `s·u̇²w^α` iff `α = −1`.
- Reparametrisation: with `τ = f(t)`, `u_new = u − log f'`, `du_new/dτ = (u̇ − f''/f')/f'`. The action element `(du_new/dτ)² w_new^{−1} dτ` minus `u̇²w^{−1}dt` is proportional to `f''` (sympy). For the difference `u_x − u_ref` the shift `f''/f'` cancels.

**S2 (PROVED; CHECKED L1).** The equation of motion. `L = Σu̇²/(2γc²w) − F − Σ(e − μ)u`. With `∂(1/w)/∂u = −1/w`, the Euler–Lagrange equation gives the displayed law. `∂F/∂u_x = (12/γ)φ_x(φ_x − avg φ)` is checked symbolically.

**S3 (PROVED; CHECKED L1).** The weak field and the principal part.
- Linearising about `u₀ = log w̄` gives `c²w̄²(Σ_y v_y − 6v_x)`.
- About a general static background, `∂/∂u_y` of the right side is `c²w_x^{3/2}w_y^{1/2}`. For a smooth background this is `c²w_x²` at leading order.

**S4 (PROVED; CHECKED W1).** Dispersion.
- `ω² = c²w̄²Σ4 sin²(k_j/2)`.
- `h = sin(x/2) − x/π` has `h(0) = h(π) = 0` and `h'' = −sin(x/2)/4 < 0`, so `h ≥ 0` on `[0, π]`. The phase velocity is therefore at least `(2/π)cw̄`, with equality at the zone boundary.
- The walker: `E = |s|` with `s_a = sin k_a`, and `|v|² = Σs_j²cos²k_j/Σs_j² ≤ 1`, tending to 1 as `k → 0`.

**S5 (PROVED).** No wake for smooth bodies needs `c ≥ 1`.
- A smooth source moving at `v` has space-time support near `ω = v·q` with small `q`, and resonates with the long-wavelength field iff `|v| > c`, the continuum Cherenkov condition.
- Walker packets reach every `|v| < 1`. So the condition for all smooth bodies is `c ≥ 1`.
- Nothing in covariance or scale covariance forces equality. `c` is a second pure number.

**S6 (PROVED; CHECKED H1).** A hopping point source radiates for every `c`.
- A source moving one site along `e₁` every `1/v` has weight on `ω = (q₁ + 2πm)v`, with amplitude `(e^{iq₁} − 1)/(iω)`.
- For fixed `q₁`, `g(q_⊥) = c²p(q)² − ((q₁ + 2πm)v)²` is continuous on the segment `q_⊥ = s(π, π)`. A sign change gives a resonant mode, by the intermediate value theorem.
- For every `c` and `v > 0` there is such a `q₁`:
  - `m = 1` with small `q₁` when `v ≤ c√2/π`;
  - `m = 1` with `q₁ = −π/2` in the middle range;
  - `m = 0` (lattice Cherenkov) when `v > (2/π)c`.
- Checked exactly for six pairs `(c, v)`, from `(5, 1/10)` to `(3, 1)`. The amplitude `2sin(q₁/2)` is non-zero in each.

**S7 (PROVED; CHECKED R2).** The lattice retarded kernel.
- `G(x, λ) = ∫e^{iq·x}/(p² + λ²) d³q/(2π)³`, with `p² = q² − Σq_j⁴/12 + O(q⁶)`.
- Its odd-in-`λ` part comes from small `q` only. Expand `e^{iq·x}` and `1/(p² + λ²) = 1/(q² + λ²) + (Σq_j⁴/12)/(q² + λ²)² + …`, average over angles (`⟨(n·x)²⟩ = |x|²/3`, `⟨Σn_j⁴⟩ = 3/5`), and take the odd parts of the radial integrals over `(0, ∞)`:
  - `∫q²/(q² + λ²) → −πλ/2`, giving `−λ/(4π)`;
  - `∫q⁴/(q² + λ²) → πλ³/2`, giving `−|x|²λ³/(24π)`;
  - `∫q⁶/(q² + λ²)² → (5/4)πλ³`, giving `+λ³/(32π)`.
- Together: `−λ³(|x|² − 3/4)/(24π)`. The `q⁶` and cross terms enter at `λ⁵`.

**S8 (PROVED; CHECKED R1).** Radiation.
- Take `ℒ = (A/2)(u̇² − v²|∇u|²) − ρu`, with `A = 1/(γc²w̄)`, `v = cw̄` and `ρ = e − μ`.
- The retarded far field is `u ≈ −(1/(4πAv²r))∫ρ(y, t − r/v + n·y/v)`. The energy flux is `S = Av u̇² n`.
- The multipole expansion gives `Ṁ` (monopole), `D̈/v` (dipole) and `n n : Q'''/(2v²)` (quadrupole):
  - `Ṁ = 0`: the total energy is conserved and the mean is removed;
  - `D̈ = Σ_i ṗ_i = 0` by matched pulls (block 55: `ṗ_i = −E_i∇u(x_i)` and `∇u` at `i` is proportional to `E_j`).
- With `∮n_in_jn_kn_l = (4π/15)(δδ + δδ + δδ)`, the power is the displayed `P`.
- Circular pair: `Q''':Q''' = 32μ²d⁴Ω⁶` and `tr Q''' = 0`. Kepler for this law is `Ω²d³ = GM`.

**S9 (CHECKED R1).** The Kepler average along the true anomaly, for `a = G = M = μ = 1`, is exact at `e = 0, 5/13, 8/17, 3/5, 4/5`. These eccentricities make `√(1 − e²)` rational. It matches a4's closed form at all five.
- Not proved for all `e` here. That closed form is a4's.

**S10 (EXECUTED; not claimed).** The front's speed (check.py family S).
- The full non-linear law on a `48³` lattice, leapfrog with `dt = 0.05/w̄`, rates held at the ambient value on the outer layer, and a weak point source (0.02) switched on at `t = 0`.
- Half-rise times at `r = 8, 12, 16`:
  - `8.25, 12.55, 16.05` at `w̄ = 1`, a speed of 1.03 sites per ambient tick;
  - `4.12, 6.25, 8.03` at `w̄ = 2`, a speed of 2.05;
  - ratio `2.000`.

**ASSUMED.**
- The block 53–55 objects as the task states them.
- Block 55's matched pulls and energy source, used in S8.
- Slow bodies with rest energy for the Kepler example. Block 54's single walker has no rest energy, so a circling body is a composite.

## 3. Where the route stands

No step fails.
- (a), (b) and (d) are complete.
- (c) is complete at leading order. The eccentric factor is checked at five values, not proved for all `e`.
- The lattice statements in (b) are, as far as I can tell, new relative to a4 and block 57. They are: the phase-velocity floor, and the radiation of a hopping point source for every `c`.

## 4. What would finish it, or go further

- A closed-form proof of the eccentric factor for all `e`, by residues in `z = e^{if}`.
- The power radiated by a lattice-scale hopping body, as a function of `c` and `v`. That would be the lattice cost of discreteness.
- The next retarded correction, `λ⁵`, on the lattice.
