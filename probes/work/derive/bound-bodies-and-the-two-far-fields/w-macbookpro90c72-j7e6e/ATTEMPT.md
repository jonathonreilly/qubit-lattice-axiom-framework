# J:derive:bound-bodies-and-the-two-far-fields:a1 — w-macbookpro90c72-j7e6e

Attempt 1 of 2, by claude-opus-5-5 (all of `check.py` and this file). `python3 check.py` prints 3 `ok` lines, exits 0
with `FAIL` empty, and runs in about 2 s. All checks are exact: sympy symbols, rationals and exact complex matrices.

Nothing is adopted and no gravitational claim is made.

**Setting and sources.** All are supplied clauses, read on their PR branches.

Block 60 (PR #8590):
- rates `w = e^u` and one length `l = e^λ` per site, with `χ = √l` and `N = wχ`;
- the content's bonds are crossed at `√(w_x w_y)/(χ_xχ_y)`;
- the curvature member, whose field energy in bond form is `F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`;
- walls held at `w = l = 1`;
- T3 (weak field) and T4 (pinned bodies: `Q_iχ_i = m_i/(8K)`, `P_i = Q_i w_i`).

Other blocks:
- block 77 (PR #8612): the rest term is timed by the clock, `φ(H + mε)φ = φHφ + mwε`;
- block 66 (PR #8597) T3: `i[φ, S_j] = −C_j[d_jφ]` and `i[H_w, G_ξ] = φ(i[H, G_ξ])φ − (Λ_ξHφ + φHΛ_ξ)`;
- blocks 63 and 69 (PRs #8593, #8601): `G_ξ`, and the two-step momentum `P_j = S_jC_j`.

## 1. Statement attempted

**(a) The supervisor's scratch result, re-derived exactly.** Take content with bond energies and a rest term. Let
`e_z = ∂⟨H⟩/∂u_z`, the energy density, which is block 55's source, and `τ_z = −∂⟨H⟩/∂λ_z`, the hop energy. Then:
- `e_z − τ_z = ρ_z w_z` exactly: the difference is the rest energy.
- Stationarity of `⟨H⟩ + F` gives `Δχ_z = −e_z/(8KN_z)` and `ΔN_z = (e_z + 2τ_z)/(8Kχ_z)`.
- Hence the charges are `Q = Σ e/(8KN)` (lengths) and `P = Σ (e + 2τ)/(8Kχ)` (rates), and
  `P − Q = (1/8K) Σ_z [2τ_z − e_z(1/w_z − 1)]/χ_z` at every strength.
- A pinned body (`τ = 0`, `e = mw`) gives back block 60 T4: `Qχ = m/(8K)` and `P = Qw`.

**(c) Light-like content, stated exactly.** Content with no rest term has `e_z = τ_z` at every site and every field
strength. Hence `P − 3Q = (3/8K) Σ_z e_z(w_z − 1)/(w_zχ_z)` exactly, so `P = 3Q` at weak field.
- The rates' far field `P + Q` is then twice the lengths' far field `2Q`.

**(b) The weak field and the virial.**
1. With `u`, `λ` and `τ/e` of order `ε`, `8K(P − Q) = Σ_z (2τ_z + e_z u_z) + O(ε²e)`. So `P = Q` at leading order iff
   `2τ_tot = −Σ e u`.
2. The lattice virial: block 66 T3 with `ξ_j = x_j` holds exactly on a box with walls.
   - `(1/2){C_a, S_a}` is exactly the truncated two-step hop `(T_a² − T_a†²)/(4i)`.
   - `i[H, G_x] = H₂ := Σ_a σ_a(T_a² − T_a†²)/(4i)`, with **no wall operator**.
   - `i[φHφ, G_x] = φH₂φ − (ΛHφ + φHΛ)`.
3. So every stationary state on the box has `⟨φψ|H₂|φψ⟩ = Σ_x x·f(x)` exactly.
4. For massive (staggered) content the one-step relabelling fails, and the two-step one works:
   - `[ε, G_x] = 2εG_x` is of order one, so `G_x` gives no virial for massive content;
   - `ε` commutes with `G_P = ½Σ_j{x_j, S_jC_j}`.
5. At leading order, the `G_P` virial and the three-dimensional Green function give `2τ_tot = −Σ e u` for a
   self-bound body. **So `P = Q` does not fail at leading order.**

**(d) Strong field.**
- The exact statement is the formula of (a) at every strength, together with the exact identity of (b).
- They do not combine into an exact `P = Q`: the exact virial involves `H₂` and the exact force density `f`, not `τ`
  and `e∇u`.

## 2. Steps

**A1 — the field equations. PROVED; CHECKED** on a 3-site line and a `2×2` box with walls. The inputs are symbolic:
rates and lengths at every interior site, bond energies `h_b` and rest energies `ρ_z`.

Setup:
- The content energy is `⟨H⟩ = Σ_b h_b √(w_xw_y)/(χ_xχ_y) + Σ_z ρ_z w_z`.
- Each bond factor is `exp((u_x+u_y)/2 − (λ_x+λ_y)/2)`.
- So `∂/∂u_z` and `−∂/∂λ_z` agree term by term on bonds (each gives half the bond), and differ by `ρ_z w_z` on sites.

For the field energy, `∂F/∂u_z = 8KN_z(Δχ)_z` and `∂F/∂λ_z = 4K[N_z(Δχ)_z + χ_z(ΔN)_z]`.
- The first follows because `N_z` is the only `u_z`-dependent factor.
- The second because `∂χ_z/∂λ_z = χ_z/2` and `∂N_z/∂λ_z = N_z/2`.
- Walls enter as neighbours held at 1.

Stationarity in `u_z` and in `λ_z` is a `2×2` linear system in `(Δχ)_z` and `(ΔN)_z`. Its solution is the pair stated
in §1(a). All of this is CHECKED as symbolic identities at every interior site.

**A2 — the charges. PROVED; CHECKED.**
- With `𝒢` the Green function of `−Δ` with the walls held, `χ − 1 = 𝒢[e/(8KN)]` and `N − 1 = −𝒢[(e + 2τ)/(8Kχ)]`.
- The far-field coefficients are therefore the total sources `Q` and `P`, and `P − Q` follows since `χ/N = 1/w`.
  CHECKED as an identity, together with the pinned body of T4.

**C1 — light-like content. PROVED; CHECKED.** With `ρ = 0`, A1 gives `e = τ` at every site. Then `P = 3Σe/(8Kχ)`,
`Q = Σe/(8Kwχ)`, and the identity in §1(c) is CHECKED.

**B1 — weak field. PROVED; CHECKED** (sympy series).
- A bound body's hop energy is of the order of its binding, so `τ/e` is of order `ε`, like `u` and `λ`.
- The series gives `8K(P − Q) = ε(2T + eU) + O(ε²)` per site.

**B2 — the lattice virial on a box. PROVED; CHECKED** on a `3×2` box with rational positive rates.

On a rectangle, with truncated shifts:
- `[S_a, S_j] = 0` and `i[S_a, x_j] = δ_{aj}C_a`, so `i[H, G_x] = Σσ_a(1/2){C_a, S_a}`;
- expanding `{C,S}`, the `TT†` and `T†T` terms cancel, leaving `(T² − T†²)/(4i)` exactly.

Block 66 (a) and (b) are bond-by-bond identities and hold on the box. All four identities are CHECKED.

For an eigenstate of `H_w`, `⟨ψ|i[H_w, G_x]|ψ⟩ = 0` gives `⟨φψ|H₂|φψ⟩ = 2Re⟨Λψ|Hφψ⟩ = Σ_x x·f(x)`, which is block 66
T3(c) with `ξ = x`.

**What the walls contribute.** Nothing, as an operator. They enter only through the Dirichlet state.
- For a free confined state (`φ = 1`, so `f = 0`) the identity says `⟨H₂⟩ = 0`, while its hop energy is `E`: the walls
  absorb the whole kinetic term, which is the confinement pressure.
- For a body bound by its own field, far from the walls, the state is exponentially small at the walls. The box
  identity then equals the infinite-lattice one up to exponentially small terms.

**B3 — massive content needs the two-step relabelling. CHECKED; PROVED.**
- `ε = (−1)^{Σx}` anticommutes with every one-step hop, and commutes with `x`.
- So `εG_x = −G_xε`, i.e. `[ε, G_x] = 2εG_x ≠ 0` (CHECKED). The one-step virial therefore carries an order-one term
  `m⟨i[wε, G_x]⟩`.
- But `εS_jC_j = S_jC_jε`, so `[ε, G_P] = 0` (CHECKED).
- `P_j = S_jC_j` is every species' own wave number (block 69), and the mass pairs species `n` and `n + (111)`
  (block 77). So the relabelling that turns into the continuum dilation for the massive, species-paired content is
  `G_P`, not `G_x`.

**B4 — `P = Q` at leading order for a self-bound body. PROVED at leading order;** the lattice-to-continuum steps are
ASSUMED.
1. Continuum image. In the long-wavelength limit the species-paired massive walk is a Dirac particle with clocked hop
   and clocked mass, `φ α·p φ + βm w` (blocks 54 and 77). `G_P` is the dilation `D = (x·p + p·x)/2`. [ASSUMED: the
   standard continuum limit of the staggered walk.]
2. Virial. A stationary state has `⟨i[H, D]⟩ = 0`.
   - The hop part gives `⟨φα·pφ⟩ = τ_tot`, minus terms in `x·∇φ` of order `ε·τ = O(ε²e)`.
   - The mass part gives `−⟨βm x·∇w⟩ = −Σ_z(rest)_z(x·∇u)_z + O(ε²e)`.
   - So `τ_tot = Σ e x·∇u + O(ε²e)`.
3. Field. Block 60 T3's weak field gives `Δu = (e + τ)/(4K) = e/(4K) + O(εe)`, so `u = −(1/4K)Σ g e`. The lattice
   Green function is `g = 1/(4πr)` to the order used. [ASSUMED: its asymptotics, for a body large compared to the
   spacing.]
4. Clausius. Symmetrise, and use `r·∇g = −g` (degree −1). Then `Σ e x·∇u = (1/8K)Σ e e g = −(1/2)Σ e u`.
5. Hence `2τ_tot = −Σ e u + O(ε²e)`, and by B1 `P = Q` at leading order. This is the virial theorem of a body bound
   by its own field, as the task says.
6. In contrast, light-like content (C1) has `τ_tot = e_tot`. The virial would need `e_tot = Σ e x·∇u`, i.e.
   `|x·∇u| ~ 1`, which is not weak field. Such content cannot be self-bound at weak field, and it has `P = 3Q`.

**D1 — strong field. PROVED; the route stops.** A1's formula and B2's identity are exact at every strength. To
replace `P = Q` exactly one would need an identity turning `Σ[2τ − e(1/w − 1)]/χ` into a commutator expectation. The
exact virial has `H₂`, not `H`, and the exact force density `f`, which equals `e∇u` only at leading order with a
`cos k` factor (block 66 T4). No such identity follows from them.

## 3. Where the route stops
- **The leading-order `P = Q` rests on two lattice-to-continuum steps** (B4.1, B4.3). The exact lattice route stops
  at B3:
  - for massive content the exact relabelling `G_x` of block 66 does not give a virial;
  - the two-step `G_P` that does commute with the mass has no exact lattice decomposition yet (block 66's T3(b) is
    for `G_ξ`).
- **(d) has no exact replacement from these identities**, for the reason in D1.
- The task's HIT condition — "`P = Q` fails for a self-bound body at leading order" — is **not met**. The HIT lines are
  the new exact identities (A1, C1, B2, B3), not a failure of `P = Q`.

## 4. What would finish it
- The exact analogue of block 66 T3(b) for `G_P` (reach three), with the staggered rest term included. That would
  give an exact lattice virial for massive content, and a check of B4 beyond leading order.
- A lattice identity of Komar = ADM type for the curvature member: `Σ[2τ − e(1/w − 1)]/χ` as the expectation of a
  commutator on stationary self-consistent states. That is what (d) asks for.
- A floating-point self-consistent bound state, the massive walk in its own fields on a `12³` box, to measure
  `8K(P − Q)/Σ e u` against B4's prediction as the binding weakens.
