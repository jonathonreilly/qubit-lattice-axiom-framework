# A delay for the rate field — independent attempt 4

Worker `w-jonathonsmac4f50-j519d`, model `claude-opus-5-5`. Task `J:derive:a-delay-for-the-rate-field:a4`.

**Provenance.** This attempt and blocks 53 to 57 come from the same model family (Claude Opus). Blocks 53 to 57 are open, unrefereed PRs: #8568, #8570, #8571, #8573 and #8578. Everything I take from them is restated below at the scope I use it. The referee should come from another family. No prior attempt at this problem existed on `ai/probes` when I claimed the unit. I read block 57 (PR #8578, "a delay for the rate field") while planning; it is a PR note, not a probe attempt. It already treats (a) and (b)'s first half: that a kinetic term of the rates must be referred to a clock of the system, and that `c` is a second pure number. I re-prove what I use from it. The new content is in (b)'s wake criterion and in all of (c).

**Scope.** Everything below holds WITHIN the supplied clauses of blocks 53 to 56 (not adopted), plus one of block 57's two readings of the premise's kinetic term: rates referred to the clocks of walls held at the ambient rate far away. The parked statistical postulate (`docs/repo/DEFERRED_DECISIONS.md`, entry 1) is not used. No gravitational claim is made; "the comparator" means Einstein's theory, used for comparison only.

## 1. The exact statement attempted

Take the ledger `<H_w> + F + K` with:
- rates `w_x = φ_x² = w̄ e^{u_x}`;
- the simplest bond energy `F = (2/γ) Σ_bonds (φ_x − φ_y)²` (blocks 55 and 56);
- the kinetic term `K = (1/(2γc²)) Σ_x (du_x/dt)²/w_x`, with `t` the time of the walls' clocks.

Point bodies have ray energies `E_A = w(x_A) √(m_A² + p_A²)`. This is block 54's ray energy with a rest term, which block 54 T4(a) allows.

(a) `K` is the unique on-site quadratic term of weight one, and it is admissible only when referred to the walls. The exact law and its weak-field form: `d²u/dt² = c² w̄² Δ_lat u − γ c² w̄ e`. In the task's form, `c² w̄² · const · (Δ_lat u/6)`, the constant is **6**. About every static background, the principal part is `c² w_x² Δ_lat`: changes travel `c` sites per local tick.

(b) Lattice covariance, the change-of-parameter premise and scale covariance hold for every `c > 0`. The requirement that no body leave an ever-growing wake is, at the continuum level, exactly **`c ≥ 1`**: an inequality, not `c = 1`.

(c) Four parts:
- The static law is the slow-source limit.
- The lattice retarded kernel's odd part is `−λ/(4π)`, the same at every site, followed by `−λ³(|x|² − 3/4)/(24π)`. So the first retarded correction exerts no pull.
- The monopole charge read far away is the ledger, so for two circling point bodies the monopole is silent at leading order. The dipole is silent at leading order by matched pulls.
- The leading power is the scalar quadrupole with its trace, `⟨P⟩ = (G/(60c⁵))⟨2 I⃛:I⃛ + (tr I⃛)²⟩ = (16/15) G⁴μ²M³(1 + 99e²/32 + 51e⁴/128)/(c⁵a⁵(1−e²)^{7/2})`, with `G = γ/(4π)` in local units. At `e = 0` this is 1/6 of the comparator's.

(d) What is added to the clauses: a reference of the rates' motion to distant clocks (non-local), and the second pure number `c`. Under the no-wake requirement, `c ≥ 1`.

## 2. Definitions (from the PR branches' notes)

- **Block 53 (#8568):** rates `w_x = φ_x² = exp(u_x)` on `Z³`; only ratios mean anything.
- **Block 54 (#8570):** `H_w = φHφ`; force `= −E∇u`; rays fall at `−w²∇u + 2(v·∇u)v`; ray energies `E = w(x) ε(k)` with `ε² = |k − k₀|² + const` (T4(a)).
- **Block 55 (#8571):**
  - T1: `∂<H_w>/∂u_x = e_x`, the amplitude's energy density.
  - T3: pulls are matched iff sources are proportional to energies.
  - T4: `F` has weight one.
  - For the simplest bond energy the law is `(12/γ) φ_x(φ_x − avg φ) = −(e_x − μ)`.
- **Block 56 (#8573):**
  - A body at rest has `e_x = m_x w_x`.
  - T1: the static law is linear in `φ`.
  - T2(b): the ledger is `Σ m_i φ_i`, and the wall flux `Σ(1 − φ)` is `γ/2` times it.
- **Block 57 (#8578):**
  - T1: under `t → f(t)`, `w → w/f'` and `du/dt → (du/dt − f''/f')/f'`; `L dt` is invariant iff `L` sees only differences of `du/dt`.
  - T3: the wall-referred kinetic term.
- `Δ_lat u_x = Σ_{y~x}(u_y − u_x)`. `E(k) = Σ_j (2 − 2cos k_j)`. `G(x)` is the Green's function of `−Δ_lat` on `Z³`, with `G(0) = 0.2527310…`.
- **Local units:** `τ = w̄ t` (local ticks), local energy `ε = e/w`, `ϑ = φ/√w̄`, `G = γ/(4π)`. In lattice time a power is `w̄²` times its value in local units.

## 3. Steps

### Part (a)

**Step 1.1 — the kinetic term (PROVED; CHECKED 1.1a–c).**
- *Weight one.* Changing the parameter's unit, `t → t/s`, multiplies every rate and every `du/dt` by `s`. A ledger term has weight one when it is multiplied by `s`.
- *Uniqueness.* An on-site form `Σ a(w_x)(du_x/dt)²` has weight one iff `a(sw)s² = s a(w)` for all `s, w > 0`. Setting `w = 1` gives `a(s) = a(1)/s`. So `(1/(2γc²)) Σ u̇²/w` is the unique such form; `γc²` names its coefficient.
- *Admissibility.* Under a non-constant change `t → f(t)`, `L dt` changes by a multiple of `f''` (1.1a, block 57 T1). It is unchanged when `du/dt` is replaced by `du/dt − du_ref/dt` with `u_ref` the walls' log-rate (1.1b). In the walls' time `du_ref/dt = 0`, so the task's term is exactly block 57's `K_ref`. **This reference to distant clocks is ASSUMED from here on** (block 57 T3). The other reading, a master parameter (block 57 T4), gives the same waves and adds a uniform motion that is not used here.

**Step 1.2 — the law (PROVED; CHECKED 1.2–1.4).**
- `L = K − F − <H_w>`; with `∂<H_w>/∂u_x = e_x` (block 55 T1), the Euler–Lagrange equation is `(ü − u̇²/2)/(γc²w) = −∂F/∂u − e`.
- For the simplest bond energy, `∂F/∂u_x = (12/γ) φ_x(φ_x − avg φ) = −(2/γ) φ_x Δ_lat φ_x`.
- With `u = 2 log φ − log w̄`, `ü − u̇²/2 = 2φ̈/φ − 4φ̇²/φ²`, so exactly:
  `φ̈ − 2φ̇²/φ = c² φ⁴ Δ_lat φ − (γc²/2) φ³ e`.
- Equivalently, in `ψ = 1/φ`: `ψ̈ = −c²φ²Δ_lat φ + (γc²/2) φ e`, which has no first-derivative term (used in E1–E2).
- In local units the factors of `w̄` cancel (CHECKED 4.3a): `ϑ'' − 2ϑ'²/ϑ = c² ϑ⁴ [Δ_lat ϑ − (γ/2) ε ϑ]`.

**Step 1.3 — weak field and the constant (CHECKED 1.5).**
- Expanding about uniform `w̄` to first order: `ü = c² w̄² Δ_lat u − γc² w̄ e`.
- Written as `c² w̄² · const · (Δ_lat u)/6 = c² w̄² · const · (avg u − u)`, the constant is `6`.
- Any weight-one bond energy `√(w_x w_y) f(u_x − u_y)` with the same quadratic coefficient `f''(0) = 1/γ` gives the same first- and second-order law: `f` is even, so its quartic term first acts at third order.

**Step 1.4 — speed set by the local rate (PROVED; CHECKED 1.6, 1.7).**
- *Any background.* Linearize about any static background `φ₀`, `φ = φ₀ + η`. The `φ̇²` term is quadratic in `η̇`, so it drops. Each neighbour's `η_y` enters `η̈_x` with coefficient `c² φ₀ₓ⁴ = c² w_x²` (1.6). The principal part is `c² w_x² Δ_lat`; the rest is a site term.
- *Uniform background.* The dispersion is `ω² = c² w̄² E(k)`. The group speed is `c w̄ |∇_k √E|`, with `|∇√E|² = Σ sin²(k_j/2)cos²(k_j/2) / Σ sin²(k_j/2) ≤ 1`, and equality in the limit `k → 0` (1.7).
- So changes travel at most `c w̄` sites per unit `t`, which is `c` sites per local tick. Executed evidence is in E1 (two ambient rates) and E2 (a non-uniform background).

### Part (b)

**Step 2.1 — covariance does not fix `c` (PROVED).**
- `K` and `F` are each invariant under the lattice's translations and 24 rotations, for every `c > 0`.
- Under the change-of-parameter premise, `L dt` is invariant for every `c` (1.1b).
- Under scale covariance (`w → sw`, `t → t/s`), `K` has weight one for every `c`.
- `c` multiplies a term that is invariant on its own, so none of the three fixes it.

**Step 2.2 — the wake criterion (continuum level).** Take the weak-field law in local units, `(∂²_τ/c² − Δ)u = −γ S(x − Vτ)` for `τ > 0`, with a body of fixed shape `S` and constant speed `V`.
- **(i) V < c (PROVED; CHECKED 2.1).** A steady co-moving solution exists. For a point body it is `u = −GE/√(z'² + (1 − V²/c²)ρ²)`, with `z'` along `V`; its field energy outside the body is finite. The resonance set `{k : c|k| = |k·V|}` is `{0}` (2.3), so the switched-on solution approaches it: no secular term.
- **(ii) V > c.** The resonance cone `cos θ = c/V` is non-empty (2.3). The late-time power fed into the field is the Cherenkov integral `∝ ∫ |Ŝ(k)|² (k·V) δ(c²k² − (k·V)²) d³k`. It is positive whenever `Ŝ ≠ 0` on the cone, so the wake's energy grows linearly. The resonance fact is CHECKED; the golden-rule form of the power is ASSUMED (standard linear response).
- **(iii) V = c (CHECKED 2.2a, 2.2b).** The retarded solution is exactly `u = −GE/(cτ − z)` on the growing disc `ρ² ≤ c²τ² − z²`. Its field energy is at least `const · τ/a²`, where `a` is the body's size.
- So a body at speed `V` leaves no ever-growing wake iff `V < c`.

**Step 2.3 — bodies reach every speed below 1 (PROVED; CHECKED 2.4).**
- For `ε = √(m² + p²)` the speed is `V = p/√(m² + p²)`, which takes every value in `[0, 1)`. The value `V₀` is reached at `p = m V₀/√(1 − V₀²)`.
- Hence "no body leaves an ever-growing wake" ⇔ `c ≥ 1`. If `c < 1`, bodies with `c < V < 1` exist. If `c ≥ 1`, every body has `V < 1 ≤ c`.
- **`c` is not forced to 1.** It is a second pure number, and this requirement bounds it below by the walk's limiting speed.
- Lattice caveat (not claimed): the field's phase speed along an axis falls to `2c/π` at the zone boundary, and the lattice allows umklapp. A body with Fourier weight at `|k| ~ π` can resonate at lower speeds. For smooth bodies this is suppressed but not zero, which is why the statement is continuum-level.

### Part (c)

**Step 3.1 — the retarded kernel on the lattice.**
- Weak field, local units: `(∂²_τ/c² − Δ_lat)u = −γ ε`, with `u = 0` before any source is switched on.
- Laplace transform in `τ` with `λ = s/c`: `û(x) = −γ Σ_y g(x − y; λ) ε̂(y)`, where
  `g(x; λ) = ∫ d³k/(2π)³ e^{ik·x}/(E(k) + λ²) = ∫₀^∞ e^{−λ²t} p_t(x) dt` and `p_t(x) = Π_j e^{−2t} I_{x_j}(2t)`.
- `p_t` is the heat kernel of `Δ_lat` (`∂_t p = Δ_lat p`, `p₀ = δ`).

**Step 3.2 — Theorem (PROVED, given A1; CHECKED 3.1–3.3, executed 3.5).** For each `x ∈ Z³`, as `λ → 0+`:

`g(x; λ) = G(x) − λ/(4π) + a₂(x) λ² − (|x|² − 3/4) λ³/(24π) + O(λ⁴)`,

where `a₂` is a lattice function.

- **ASSUMED A1** (standard; Hankel's large-argument expansion, with its remainder, at fixed order): `e^{−2t} I_n(2t) = (4πt)^{−1/2}(1 − (4n² − 1)/(16t) + O(t^{−2}))` uniformly for `t ≥ 1`. The two displayed coefficients are re-derived by Laplace's method from `(1/π)∫₀^π e^{−2t(1−cos θ)} cos nθ dθ` with `θ = s/√t` (3.1a–c).
- *Product over coordinates.* `p_t(x) = (4πt)^{−3/2}(1 + c₁(x)/t + R)` with `c₁ = −|x|²/4 + 3/16` (3.1d) and `|R| ≤ C_x/t²` for `t ≥ 1`. The remainder's size is checked in executed 3.5.
- *Split at `t = 1`.* `∫₀¹` is entire in `λ²`.
- *Leading terms.* For non-integer `σ > 1`, `∫₁^∞ t^{−σ} e^{−yt} dt = y^{σ−1}Γ(1 − σ, y) = Γ(1 − σ) y^{σ−1} − Σ_{n≥0} (−y)^n/(n!(1 − σ + n))`. This uses the series of the lower incomplete gamma function; its only non-analytic term is `Γ(1 − σ) λ^{2σ−2}`. With `σ = 3/2, 5/2` the odd terms are `(4π)^{−3/2}[Γ(−1/2) λ + c₁ Γ(−3/2) λ³]`, and `(4π)^{−3/2}Γ(−1/2) = −1/(4π)` and `(4π)^{−3/2}Γ(−3/2) = 1/(6π)` (3.2a, 3.2b).
- *Remainder.* `|e^{−y} − 1 + y| ≤ min(y²/2, y)` gives `∫₁^∞ t^{−7/2}|e^{−λ²t} − 1 + λ²t| dt ≤ λ⁴ + (2/3)λ⁵`. So the remainder is a constant, plus a `λ²` term, plus `O(λ⁴)`. ∎
- **Cross-check at `x = 0`.** The density of states of `−Δ_lat` near 0 is `√E/(4π²)(1 + E/8)`, from `⟨Σ n_j⁴⟩ = 3/5` (3.3a, 3.3b). It gives `Im g(0, ω) = (ω/(4πc))(1 + ω²/(8c²))`, which matches the `λ` and `λ³` terms (3.3c).
- **Continuum comparator.** `e^{−λr}/(4πr)` has the same terms with `r²` in place of `|x|² − 3/4` (3.2c).

**Step 3.3 — reading in time (PROVED as the slow-source expansion).**
- Replace `λⁿ` by `c^{−n} ∂ⁿ_τ` acting on the source. This is the standard near-zone expansion for sources that change slowly compared with their size over `c`:
  `u(x, τ) = −γ Σ_y G(x − y) ε_y + (γ/(4πc)) Q̇ − (γ/c²) Σ_y a₂(x − y) ε̈_y + (γ/(24πc³)) Σ_y (|x − y|² − 3/4) ε⃛_y + O(c^{−4})`, with `Q = Σ ε`.
- **Slow-source limit.** The first term is the static law of blocks 55 and 56 at weak field.
- **First retarded correction.** It is `(G/c) Q̇`, exactly the same at every site. It exerts no pull, because pulls are `−E∇u`, and it moves every clock together.
- **First pull that dissipates.** It comes from the `λ³` term, whose gradient is `(G/(3c³))(x Q⃛ − D⃛)` with `D = Σ ε_y y` (3.4). This is the continuum's form exactly. The lattice changes this order only by the uniform `−3/4`, which carries no pull.

**Step 4 — the monopole is the ledger (PROVED; CHECKED 4.1, 4.2).**
- **(i) Static identity.** This is block 56 T2(b), re-proved on `Z³` with `φ → √w̄` at infinity and `e` of finite support.
  - The law is `Δ_lat φ = γ e/(2φ)`.
  - Let `η = φ − √w̄`. Summing by parts (boundary terms vanish because `η = O(1/|x|)`): `F = (2/γ) Σ_bonds (η_x − η_y)² = (2/γ) Σ_x η_x(−Δ_lat η)_x = −Σ_x η_x e_x/φ_x`.
  - So `<H_w> + F = Σ e − Σ η e/φ = √w̄ Σ_x e_x/φ_x`.
  - Far away, `η(x) = −(γ/2) Σ_y G(x − y) e_y/φ_y`. Using `G(x) = 1/(4π|x|) + O(|x|^{−3})` (ASSUMED, standard), `u → −G (L/w̄)/|x|`. **The far field reads the ledger `L`.**
  - The Gauss form needs no asymptotics. In a box with walls at `φ = 1`, the wall flux `Σ(1 − φ)` equals `(γ/2) L`. This is CHECKED exactly with rationals on a `5³` box with three bodies (4.1a, 4.1b). There the linear-in-`u` charge `Σ e` differs from the ledger (4.1c).
- **(ii) Dynamics.**
  - By 4.3b, `(Δ_lat − ∂²_τ/c²) ϑ = σ` with `σ = (γ/2) ε ϑ + c^{−2}[ϑ''(ϑ^{−4} − 1) − 2ϑ'² ϑ^{−5}]`.
  - *Body model (ASSUMED).* Point bodies, each moving in the other's field with no self-action. `ε_A = m_A + T_A + O(mV⁴)` and `ϑ(x_A) = 1 + u_B(x_A)/2`, with `u_B(x_A) = −G m_B/r`.
  - The far charge is `Σ_A ε_A ϑ(x_A) = M + T + U` (4.2a). This is conserved at Newtonian order: in local units slow bodies fall at `−∇u` (block 54), so `T + U` is the Newtonian energy.
  - The `c^{−2}` part of `σ` adds to the charge only at relative order `V²`. The orbit-dependent part of `Σδ²` (with `δ = ϑ − 1`) is the cross term `(G² m_A m_B/2) ∫ d³x/(|x − x_A||x − x_B|) = const − π G² m_A m_B r` (4.4). Its `d³/dτ³` enters as `(G/c²) m_A m_B r⃛`, against the retained `μ (r²)⃛/(6c²)`. Their ratio is of order `GM/a ≈ V²`.
- **Result.** The monopole is silent at the leading order of slow motion. The linear-in-`u` reading, with source `e/w̄`, would give `M + T + 2U` (4.2b). That changes at the rate `U̇ = −(1/2) tr I⃛` (Lagrange–Jacobi, 6.3a) and radiates a spurious monopole. The spurious excess is `(G/c)⟨(tr I⃛)²⟩(1/4 − 1/(6c²))` (6.4); at `c = 1` it makes the spherical radiation six times its true value. **The second-order term of the law, its being linear in `√w`, is what makes the monopole silent.**

**Step 5 — the dipole (PROVED at leading order; CHECKED 5.1).**
- `D_eff = Σ_A ε_A ϑ(x_A) x_A = Σ m_A x_A + O(mV² a)`.
- `d²/dτ² Σ m_A x_A = Σ m_A ẍ_A`, the sum of the pulls, because inertia equals energy for slow bodies (block 54). This is `0` because pulls are matched when sources are proportional to energies (block 55 T3; 5.1).
- So `D̈_eff = O(V² F)`. The dipole's power is at relative order `V²c²` to the quadrupole's: silent at leading order.
- **Not settled at the next order.** Point bodies obey the exact identity `E_A ẋ_A = w_A² p_A`, so `D̈ = Σ w_A² ṗ_A + …`. The bodies sit at different rates, and the retarded field carries momentum, and both enter at that order. For bodies whose own fields slow their own clocks by different amounts, a term `F_A(w_A² − w_B²)` of relative size `Δs` appears, which could exceed the quadrupole when `Δs > V/c`. This is not computed and not claimed.

**Step 6 — the power at leading order (PROVED given A2; CHECKED 6.1–6.5).**
- *Field energy.* In local units it is `(2/γ) Σ (|∇δ|² + δ'²/c²)` with `δ = ϑ − 1`, which equals `(1/(2γ)) Σ (|∇u|² + u'²/c²)`.
- **ASSUMED A2** (standard far-zone multipole expansion, continuum). With `R ≫` wavelength `≫ 1` site, `P = (G/c)⟨(Q̇ + n·D̈/c + nn:I⃛/(2c²))²⟩_n`. The prefactor is `(1/γ)(1/c)(γ/4π)² · 4π = G/c` (6.2). Step 3.2 shows the lattice's first odd correction is uniform. The argument that at order `λ⁵` lattice terms have lower degree in `x`, and so are suppressed by `1/a²` for an orbit `a` sites across, is not proved.
- With `Q̇ = D̈ = 0` at leading order and the angular averages (6.1): `⟨P⟩ = (G/(60c⁵))⟨2 I⃛:I⃛ + (tr I⃛)²⟩`, with `I_ij = Σ m_A x_A^i x_A^j`.
- **Kepler orbits.** In local units `Ω² a³ = GM`. The averages are exact (6.3b):
  `⟨P⟩ = (16/15) (G⁴μ²M³/(c⁵a⁵)) (1 + 99e²/32 + 51e⁴/128)/(1 − e²)^{7/2}`.
  - The same code reproduces the comparator's `(32/5)(1 + 73e²/24 + 37e⁴/96)/(1 − e²)^{7/2}` from its traceless formula (6.3c).
  - At `e = 0` the ratio is `1/6` (6.3d).
  - The trace ("breathing") part `(G/(60c⁵))⟨(tr I⃛)²⟩ = G⁴μ²M³e²(4 + e²)/(120c⁵a⁵(1 − e²)^{7/2})` vanishes on circles and is present on eccentric orbits (6.5).
- In lattice time the power is `w̄²` times this.

### Part (d)

**Step 7 — what is added to the clauses (statement).**
1. A kinetic term for the rates. With no master clock it must refer every rate's motion to a clock of the system: the walls held at the ambient rate. That is not a nearest-neighbour clause (block 57 T3). The alternative is a master parameter (block 57 T4).
2. The number `c`: the field's speed in sites per local tick. Nothing above fixes it. The requirement that no body leave an ever-growing wake gives `c ≥ 1`.
3. Used only as a model, not added: point bodies with ray energy `w √(m² + p²)` and no self-action (Steps 4–6).

Nothing is adopted.

### Executed (floating point; evidence, not claims)

- **E1.** A `49³` box, walls at `φ = √w̄`, the full non-linear law of Step 1.2 in `ψ`, the same step `dt = 0.1` in lattice time at `w̄ = 1` and `w̄ = 2`. A body is switched on at the centre at `t = 0`. Half-rise times at `r = 6..18` on an axis are read against the free-space value `1 − (γ/2) m G(x)/(1 + (γ/2) m G(0))`.

  | source | speed at `w̄ = 1` | speed at `w̄ = 2` | ratio |
  |---|---|---|---|
  | `m = 0.02` (weak) | 0.984 | 1.968 | 2.0003 |
  | `m = 6` (`φ` at the body 0.57 of ambient, clock rate 0.33) | 0.987 | 1.974 | 2.0003 |

  Speeds are in sites per unit `t`. The expected speed is `c w̄`. The 1.5% shortfall is lattice dispersion: the half-rise lags by a slowly growing 0.2 to 0.55 sites.
- **E2 (the local rate).** A `61³` box with a held ball of slow clocks (radius 3). A weak probe pulse starts 16 sites to one side of the well and is detected 16 sites to the other, at impact parameter 5. The pulse's delay against the run with no well is 0.302, 0.594, 1.402 and 2.539 local ticks. The straight-ray integral `∫(1/w − 1) dl/c` gives 0.277, 0.549, 1.333 and 2.550 (`w` at closest approach: 0.984 down to 0.862). This is the lattice analogue of a Shapiro delay. The deviations are below 10%, consistent with the pulse's group speed being below 1.

## 4. Where the route stops

Nothing in the route fails at the stated order. These items are not settled:

1. The dipole and the monopole at the next order (relative `V²`): the near-field momentum, the bodies' different rates, and 1PN corrections to the quadrupole all enter together.
2. Structure: bodies with their own fields (self-rates `s_A`). Step 5 flags a possible dipole of relative size `Δs`.
3. The lattice version of the wake criterion (umklapp, and the zone-boundary phase speed `2c/π`).
4. A2 on the lattice beyond the `λ³` term.
5. The value of `c`, and whether the framework would state a reference to distant clocks at all.

## 5. What would finish it

- A 1PN two-body computation in `σ` of Step 4, with the retarded field's momentum. It would settle whether the monopole and the dipole radiate at relative order `V²`, and whether bodies of different structure fall alike. The latter is the same question as the structure-dependent dipole.
- The `λ⁵` term of Step 3.2's kernel, from the next coefficient of A1. With it the lattice's quadrupole power is exact at the orbit sizes used.
- An owner's decision on the reference clock, and a clause or a measurement that fixes `c`.
