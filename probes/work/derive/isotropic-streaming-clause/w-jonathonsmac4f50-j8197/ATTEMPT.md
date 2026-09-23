# isotropic-streaming-clause, attempt a1: a continuous forward-only rule, and what it cannot fix

**Provenance.** Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-jonathonsmac4f50-j8197`, task
`J:derive:isotropic-streaming-clause:a1`.

The prior attempt a2 (`w-jonathonsmac4f50-j1e60`) was written by Claude Opus 5 (`claude-opus-5`). It is in the same model
family as this worker and is unrefereed. Blocks 44, 48 and 51 were supervisor-run in the same family. Nothing here is an
independent confirmation of that work.

**Plan before reading a2.** My plan was to take one-way rates proportional to `(s·d̂)_+` on the 26 neighbours, one rate per
shell, and to impose the task's condition exactly on the sphere-averaged fourth-rank moment. After reading a2 I kept that
plan, because a2 took a different route: it imposed the stronger pointwise condition `M(s) ∝ I`. a2 left three things
open:
- a closed-form forward-only rule ("the obvious ansatz … `(s·d)_+ w(|d|)` … I did not test");
- stationarity;
- the collisionless shadow.

This attempt addresses those three.

## 1. What is claimed

**Setting.** This is block 51's inertial gas on the sphere menu (open PR "ail51"). A record of content `s` hops to `x + d` at
rate `a(s, d)`. Block 51's clause is `a(s, sign(s_k)e_k) = |s_k|/√3`.

To second order the streaming is `−(Σ_d a d)·∇ + ½ M_kl(s)∂_k∂_l`, with `M_kl(s) = Σ_d a(s,d) d_k d_l`. The task's moment is
`T_ijkl = ⟨s_i s_j M_kl(s)⟩` over the uniform sphere.

**(a) The rule.** Consider the forward-only shell rule

```
a(s, d) = λ_{|d|²} (s·d/|d|)_+     on the 6 axis (λ₁), 12 face-diagonal (λ₂), 8 body-diagonal (λ₃) neighbours.
```

- It is non-negative, continuous in `s`, and forward-only: `a > 0` only when `s·d > 0`.
- Its mean displacement is `κ s` with **one** constant, `κ = λ₁ + 2√2λ₂ + 4λ₃/√3`, for every unit `s`.
- The departure of `T` from isotropy is the single number `T₁₁₁₁ − T₁₁₂₂ − 2T₁₂₁₂ = (λ₁ − λ₂ − (8/3)λ₃)/8`. So **`T` is
  isotropic iff `λ₁ = λ₂ + (8/3)λ₃`**.
- The smallest neighbour sets on that line are:
  - axes plus the 12 face diagonals, at equal rates (`λ₁ = λ₂`, 18 targets);
  - axes plus the 8 body diagonals, at `8 : 3` (14 targets).
- Axis hops alone are never isotropic, which is block 51's case.
- On the line:
  - the momentum equation's second-order term is `(3/2)[α∇²g_i + 2β∂_i∇·g]`, with `α = (3/4)λ₂ + λ₃` and
    `β = λ₂/8 + λ₃/6`;
  - there is no term of cubic symmetry;
  - the number equation is `((5/4)λ₂ + (5/3)λ₃)∇²n`;
  - on a potential inflow both terms vanish identically. So block 51's T3 obstruction, a viscous stress that no pressure
    can balance, is absent for these rates at the level of the streaming term.

**(b) What the rule keeps and what it does not.**
- **Stationarity is kept.** The uniform product measure is stationary for **every** rate function `a(s,d)` on any hop set,
  with the exchange rule. Block 44's predecessor argument goes through per record and per hop vector. With reflecting
  solids it holds if reflection reverses the content and `a(−s,d) = a(s,−d)`, which is true for the shell rule.
- **The capture law.** A capturing site takes content-`s` records at rate `ρ r(s)`, where `r(s) = Σ_d a(s,d)`:
  `r(s) = λ₁|s|₁ + λ₂√2 Σ_{i<j} max(|s_i|,|s_j|) + λ₃(1/√3)Σ_{±,±}|s₁ ± s₂ ± s₃|`. Block 48's `|s|₁` is the axis case, and
  `⟨r⟩ = (3/2)λ₁ + 3λ₂ + 2λ₃`. `r` is **never constant** on the sphere. On the whole isotropy line
  `r(body diagonal) − r(axis) = 0.3531λ₂ + 1.6427λ₃ > 0`.
- **The collisionless shadow stays anisotropic.** Far from a capturing site, the missing flux per unit capture has angular
  density `r(n̂)/(4π⟨r⟩)`. The spread across the three direction classes is:
  - 73% (`1 : √2 : √3`) for block 51's clause;
  - 15% for axes plus face diagonals;
  - 33% for axes plus body diagonals.

**(c) The cost.** Records must step to diagonal sites at a distance of `√2` or `√3`. That is outside the six-neighbour stencil
that every other clause of the lane uses (pair weights, exchange, bonds). Exchange with a diagonal target has to be admitted.
Reflection at solids has to be content reversal, because "reflected in the face" is undefined for a diagonal hop. The rule
keeps "content = direction of travel": a record never steps against its content. a2's two-way axis rule gives that up
instead.

## 2. Steps

1. **ASSUMED — the setting.** The following are used as supplied hypotheses; none is adopted:
   - block 51's inertial clause, with its streaming defined as a sum over hop vectors;
   - block 44's exchange and re-draw rules;
   - bodies that capture.

   The second-order streaming form is exact on fields of degree two, since `f(x−d) − f(x) = −d·∇f + ½(d·∇)²f` there, as in
   block 51 T1.

2. **PROVED / CHECKED (A1) — the sphere lemma: `⟨s_i s_j |s·n|⟩ = (δ_ij + n_i n_j)/8`.**
   - For unit `n`, the coordinate `t = s·n` is uniform on `[−1,1]`. That is the area of a spherical zone, `2π × height`.
   - Given `t`, the transverse part is uniform on a circle of radius `√(1−t²)`.
   - Hence `⟨s_i s_j |t|⟩ = n_i n_j⟨|t|³⟩ + ½(δ_ij − n_i n_j)⟨|t|(1−t²)⟩ = n_i n_j/4 + (δ_ij − n_i n_j)/8`.
   - The odd part of `(t)_+ = (t + |t|)/2` averages to zero, so `⟨s_i s_j(s·n)_+⟩ = (δ_ij + n_i n_j)/16`.
   - check.py integrates the case `n = e₃` exactly over the sphere. Rotation invariance of the uniform measure gives every
     other `n`.

3. **PROVED / CHECKED (A2) — the moment of the shell rule.**
   - By step 2, `T_ijkl = (1/16)Σ_d λ_d d_k d_l(δ_ij + d̂_i d̂_j) = (1/16)[δ_ij S_kl + Q_ijkl]`.
   - The second moment is `S = Σ_d λ_d d dᵀ = (2λ₁ + 8λ₂ + 8λ₃)I`.
   - The fully symmetric fourth moment is `Q = Σ_d λ_d d⊗d⊗d⊗d/|d|²`. It has `Q_iiii = 2λ₁ + 4λ₂ + (8/3)λ₃` and
     `Q_iijj = 2λ₂ + (8/3)λ₃`.
   - An isotropic `T` of this symmetry is `αδ_ijδ_kl + β(δ_ikδ_jl + δ_ilδ_jk)`. The only obstruction is
     `T₁₁₁₁ − T₁₁₂₂ − 2T₁₂₁₂ = (Q_iiii − 3Q_iijj)/16 = (λ₁ − λ₂ − (8/3)λ₃)/8`.
   - check.py compares all 81 components, and reproduces block 51's `1/(4√3)`, `1/(8√3)` and `0` at `λ₁ = 1/√3`.

4. **PROVED / CHECKED (A3) — the mean displacement.**
   - Write `(t)_+ = (t + |t|)/2`. The `|s·d|` part cancels between `d` and `−d`.
   - So the mean is `½(Σ_d λ_d d dᵀ/|d|)s = κ s`, because each shell's sum of `d dᵀ` is a multiple of `I`.
   - check.py verifies this exactly at nine directions, including generic ones. The rule is homogeneous of degree 1 in `s`.

5. **PROVED / CHECKED (A4) — the equations.**
   - The local-equilibrium content law `(n/4π)(1 + 3u·s)` gives `∫ s_i M_kl f = 3T_ijkl g_j`, because `⟨s_i M_kl⟩ = 0` (`M` is
     even in `s`). The momentum term is therefore `(3/2)∂_k∂_l T_ijkl g_j`, and the number term is `(1/2)⟨M_kl⟩∂_k∂_l n`,
     with `⟨M⟩ = (S/4)`.
   - On the line, with `g = ∇χ` and `∇²χ = 0`, we have `∇²g = 0` and `∇·g = 0`, so the second-order streaming term vanishes.
     check.py verifies this for `χ = 1/r`.
   - The collisional part of the viscosity is not addressed. Block 51 marks its isotropy as not proved.

6. **PROVED / CHECKED (B1) — stationarity for every rate function.**
   - Take a configuration `c`, a record at `y` with content `s`, and a hop vector `d`. Look at `y − d`.
     - If it is empty, `c` is reached by the record moving from `y − d`.
     - If it holds content `s'`, `c` is reached by the exchange triggered by content `s` at `y − d`, from the configuration
       with `s` at `y − d` and `s'` at `y`.
     - If it is solid, `c` is reached from the configuration with `−s` at `y`, by the reflection of the record attempting
       `−d`. That has rate `a(−s, −d)`, which equals `a(s, d)` if `a(−s,d') = a(s,−d')`.
   - Each case is one predecessor, with the rate `a(s,d)` and the same uniform weight. So the inflow into `c` is
     `Σ_records Σ_d a(s,d)`, which is the outflow.
   - The re-draw kernel is uniform on each momentum class, so it is symmetric.
   - check.py covers the `3³` torus with all 26 hop vectors and random positive rational rates:
     - 2 records with a solid site: 11700 configurations;
     - 2 records without it: 12636;
     - 3 records with two contents: 23400.

     Every configuration balances. Without the exchange, 10422 of 12636 do not.
   - The theorem needs neither the shell form nor a constant total rate. This settles a2's "must be re-argued": its
     forward-only witnesses are stationary too.

7. **PROVED / CHECKED (B2) — the capture law.** The density at the upstream neighbours of a capturing site is unaffected by
   it, since a forward-only walk can reach `y` with `s·y < 0` only from `s·x < s·y`. So at first order in the density
   (block 48's level) the capture rate of content `s` is `ρ Σ_d a(s,d) = ρ r(s)`. The closed form is checked against the
   direct sum at nine directions.

   **Never constant.** `r` is a positive combination of finitely many `|s·d̂|`. On an open cone of the sphere, avoiding the
   finitely many planes `s·d̂ = 0`, it equals `v·s` for a fixed `v`. A linear function is not constant on an open subset of
   the sphere.

   On the isotropy line:
   - `r(body) − r(axis) = (√3 + √6 − 1 − 2√2)λ₂ + (4√3/3 − 2/3)λ₃`;
   - both coefficients are positive (`0.3531`, `1.6427`).

8. **PROVED given the strong law (flux form); ASSUMED (density form) (B3) — the far shadow.**
   - At first order in the density, the site removes content-`s` records at rate `ρ r(s)dΩ/4π`.
   - Each would have continued as a forward walk with mean step `κ s/r(s)`. By the strong law of large numbers (ASSUMED,
     standard), its exit direction from the ball of radius `R` tends to `ŝ`.
   - So the missing outgoing flux through that sphere, as a measure on directions, tends to `ρ r(n̂)dΩ/(4π)` per unit time.
     Per unit capture this is `r(n̂)/(4π⟨r⟩)`.
   - The speed along `s` is `κ` for every content, so the momentum-density form of the same statement is
     `g(Rn̂)R²/Q → r(n̂)/(4πκ⟨r⟩)`. Passing from flux through a sphere to density at a point is a local-limit step, and I
     ASSUME it.
   - Its solid-angle mean is `1/(4πκ)`. For block 51's clause this is `√3/(4π)`, the isotropic closure at `ρ → 0`, and its
     direction dependence is block 48's leading term `|n̂|₁`.
   - check.py gives the exact ratios in §1(b).

9. **The cost (c).** See §1(c). In numbers:
   - the smallest isotropic sets have 18 targets (`λ₁ = λ₂`) or 14 (`λ₁ : λ₃ = 8 : 3`);
   - the speed `κ` carries `√2` and `√3`;
   - the collisionless shadow keeps at least the 15% spread across the three direction classes of the best of the two
     minimal members. I did not optimize over the whole line or over the whole sphere.

## 3. Where the route stops

- **Only the shell-linear form.** (a) is solved inside the shell-linear forward-only family. I do not classify all
  forward-only rules, nor find the member with the least anisotropic capture law over the whole sphere.
- **Is the capture law's anisotropy forced?** The never-constant statement of step 7 is for positive combinations of
  `|s·d̂|`. Whether any forward-only rule with a constant `κ` can have a constant total rate is open. At `s = e₁` every
  forward neighbour has `d₁ = 1`, so `r(e₁) = κ`. That forces nothing at other directions.
- **Moderate distances.** The shadow at moderate distances, the analogue of block 48's exact multinomial values at `r` of 6
  to 10, is not computed. It needs a sum over paths of the 26-neighbour forward walk.
- **Not addressed here:**
  - whether the collisional viscosity is isotropic;
  - the two-body force off the lattice axes;
  - a simulator run of the new rule.

## 4. What would finish it

1. **The shadow at moderate distances.** Compute the exact first-order shadow for the member `λ₁ = λ₂`, by dynamic
   programming over paths of the forward walk. Compare it with a run of a modified `inertial_wind_by_direction.py` in which
   records hop to face diagonals.
2. **The best member.** Minimize the spread of `r` over the sphere along the isotropy line. `r` is the support function of a
   zonotope, so its extremes lie at normals of the zonotope's faces.
3. **The forced-anisotropy question.** Decide whether any forward-only rule with constant `κ` has a constant total rate. If
   none has, the collisionless shadow of a forward-only gas is anisotropic whatever the rule.
4. **A referee from another family**, for all of the above.

## 5. Running it

```
python3 probes/work/derive/isotropic-streaming-clause/w-jonathonsmac4f50-j8197/check.py
```

It needs `sympy` and the standard library. It runs 7 checks (A1–A4, B1–B3) in exact arithmetic: sympy with `√2` and `√3`, and
`Fraction` for the Markov-chain balances. It takes about 10 seconds.
