# The blind walk beyond first order — attempt 1

Worker `w-jonathonsmac4f50-jd491`, model `claude-opus-5-5`. Task `J:derive:the-blind-walk-beyond-first-order:a1`.

**Provenance and overlap (declared).**
- Blocks 54 and 62 to 65 were written by the same model family (Claude Opus). They are open and unrefereed.
- **Earlier in this session I delivered the sibling unit `J:derive:a-law-for-the-rotation-of-the-coin-axes:a2` (issue #8843)**, with the same `SU(2)` bond links. Parts (a) and (b) here overlap it. It is not used as authority: every step is restated and re-checked here.
- The new content is:
  - the task's exact bond form;
  - the exact second-order term;
  - the varying-frame weight that explains block 65 N1.3;
  - above all part (c): which links the frame alone can fix, and at what reach they can carry curvature.
- The referee should come from another family.

**Scope.** This works within the supplied clauses of blocks 54 and 62 to 65. Nothing is adopted. Parked decision 4 is untouched: everything stays in `M₂(ℂ)`, with links and frames acting on the existing qubit coin. No gravitational claim is made. The comparator (spin connection, torsion-free condition, Riemann tensor) is named only for comparison.

## 1. The exact statement attempted

**(a) The generator.** `H = Σ_{x,a} (1/(2i)) [ψ†(x) M_a(x) V_a(x) ψ(x+e_a) − h.c.]`, with `V_a ∈ SU(2)` on bonds and `M_a(x)` a 2 × 2 matrix at the bond's first site.
- It is hermitian.
- It is exactly covariant under `ψ → Uψ`, `V_a → U(x) V_a U†(x+e_a)`, `M_a → U M_a U†`.
- At `M_a = σ_a`, `V = 1` it is block 54's walk.

**(b) Links built from the sites' rotations.**
- With `V_a = U_x U†_{x+e_a}` and `M_a = U_x σ_a U_x†`, the generator is exactly `U H U†`, to all orders.
- Its first order is block 65's `H[ϑ]`: the bond-averaged frame rotation, and the scalar hop.
- The scalar hop is `(1/2) tr(σ_a V_a)`, the twist of the link about its own bond, `(i/2)(θ_y − θ_x)_a` at first order.
- The second-order term, which block 65 omits, is exactly `(1/4)(θ_x·σ) σ_a (θ_y·σ) − ((|θ_x|² + |θ_y|²)/8) σ_a`.
- For a varying frame, the weight of the scalar hop is `E(x)·(θ_y − θ_x)`. It is not the naive difference `θ_y·E(y) − θ_x·E(x)`; the two differ by `θ_y·(E(y) − E(x))`. This explains block 65 N1.3's failure.

**(c) Links as functions of the frame.** Write `E = R_E S`, with `S = √g`.
- A link fixed by the frame alone has the form `Û_x f Û†_y`: the frame's rotation part only changes the coin basis. The flat choice `f = 1` needs no new field, to all orders, and the walker then sees only `S`.
- **Curvature at bond reach** (a rule reading the stretches at the bond's two ends, linear in the stretch `s = S − 1`, vanishing on uniform stretch): the plaquette holonomy is blind to every relabelling **only for the zero rule**.
- **Curvature at plaquette reach**: `ω_a = −curl(s e_a)`, which equals block 64's curls `−(1/2) ε F^a`. Its holonomy is blind to relabellings and equals the linearized curvature of `g = 1 + 2s` (for example `R₀₁₀₁`).
- So "no new field" is possible at first order in the stretch, **but only when the link reads block 64's curls on the plaquettes adjoining the bond**. This is shown in long-wavelength symbols.
- Beyond first order in the stretch nothing is constructed.

## 2. Steps

### Step 1 — (a) (PROVED; CHECKED 1.1–1.3)
- **Covariance.** The bond matrix `M V` becomes `(U_x M U_x†)(U_x V U_y†) = U_x (M V) U_y†` (1.1).
- **Hermiticity** holds by construction: the bond term plus its hermitian conjugate.
- **The whole generator.** With block-diagonal `U`, `(U H U†)` has bond matrices `U_x (M V) U_y†`. This is checked exactly on a ring with random rational quaternions (1.2).

### Step 2 — (b) (PROVED; CHECKED 2.1–2.5)
- **Exact equality (2.1).** `M_a V_a = U_x σ_a U_x† U_x U_y† = U_x σ_a U_y†`, so the generator is `U H U†`.
- **Expansion.** Expand `U = exp(−iθ·σ/2)` (checked with the exponential series through third order):
  - **first order (2.2):** `σ_a + [((θ_x + θ_y)/2) × e_a]·σ + (i/2)(θ_y − θ_x)_a`. This is block 65 T1/T2: `(1/2){(ϑ × e_j)·σ, S_j}` has bond matrix `((ϑ_x + ϑ_y)/2 × e_a)·σ`, and `(1/2)C_a[∂_aϑ_a]` has bond coefficient `(1/4)(ϑ_y − ϑ_x)_a`, the same as `(i/2)(ϑ_y − ϑ_x)_a/(2i)`;
  - **the scalar hop (2.3)** is the trace part `(1/2)tr(σ_a V_a)`: the component of the link's rotation along its own bond;
  - **second order (2.4):** `(1/4)(θ_x·σ) σ_a (θ_y·σ) − ((|θ_x|² + |θ_y|²)/8) σ_a`, exactly.
- **A varying frame (2.5).** With `M_a = E(x)·σ`, the scalar part of `U_x (E(x)·σ) U_y†` at first order is `(i/2) E(x)·(θ_y − θ_x)`. The naive weight, the bond difference of `θ·E`, differs from it by `(i/2) θ_y·(E(y) − E(x))`. With block 62's symmetrised frame the weight is `Ē·(θ_y − θ_x)`.

### Step 3 — (c) (PROVED; CHECKED 3.1–3.4)

**3.1 The rotation part is a change of coin basis (3.1).**
- `M_a V_a` with `V = Û_x f Û_y†` equals `Û_x [(S_x e_a)·σ f] Û_y†`.
- Covariance under local rotations at every site makes the frame's rotation part enter only through the end factors `Û`. The rotation part at any other site is gauge there, so `f` depends on the stretches (and on nothing rotational).
- The lift of `R_E` to `SU(2)` is fixed up to a sign per site, the unitary `ψ_x → ±ψ_x`.
- With `f = 1` the walker sees only `S`: no new field, to all orders, and no curvature.

**3.2 Bond reach carries no curvature (3.2).**
- Take long-wavelength symbols (leading order in `k`), with `S = 1 + s` and relabellings `s → s + (i/2)(k ξᵀ + ξ kᵀ)`.
- A link on bond `a` that reads only the bond's two ends is linear in the difference of `s` along `a`: `ω_a = i k_a L_a(s)`. Here `L_a` is any linear map `Sym(3) → ℝ³` covariant under the proper rotations about `e_a`. That is a 4-parameter family: `e_a × (s e_a)`, `s e_a`, `(tr s) e_a`, `(e_a·s e_a) e_a`.
- The plaquette holonomy `i k_a ω_b − i k_b ω_a` vanishes for every relabelling only when all four parameters vanish.
- On the lattice, a rule blind at every `k` is blind at leading order, so the no-go holds for every bond-reach linear rule.

**3.3 Plaquette reach carries curvature (3.3, 3.4).**
- The rule is `ω_a = −curl(s e_a)`: at each bond, the curl of the `a`-th column of the stretch.
- It equals `−(1/2) ε_{cbd} F^a_{bd}`, with `F^a_{bd} = ∂_b s_{da} − ∂_d s_{ba}`: block 64's curls, with the stretch in the place of the strain (3.4).
- Its holonomy is blind to relabellings and not zero. In the plane `(0,1)`, its normal component is `k₀² s₁₁ − 2k₀k₁ s₀₁ + k₁² s₀₀`, the linearized curvature `R₀₁₀₁` of `g = 1 + 2s`.
- **Comparator.** This is the linearized torsion-free connection. It needs transverse derivatives of the stretch, which is why bond reach cannot supply it.

**3.4 Answer to (c).**
- The flat function `V = Û_x Û_y†` is exact and needs no new field.
- A function of the frame that carries curvature must read block 64's curls on the plaquettes adjoining the bond. At first order in the stretch, `V_a = Û_x exp(−(i/2) ω_a·σ) Û†_y` with `ω_a = −curl(s e_a)`.
- The generator stays nearest-neighbour in `ψ`; only the link rule reads the plaquettes.
- So "no new field" is possible at first order in the stretch, at plaquette reach. At second order the torsion-free rule's nonlinear completion is not constructed here.

## 3. Where the route stops

Part (c) beyond first order in the stretch, and on the lattice beyond long-wavelength symbols. There, a consistent lattice placement of the curls on plaquettes and an exact lattice holonomy are needed. No step that is claimed fails.

## 4. What would finish it

1. An exact lattice version of 3.3: the curls placed as block 64 places them, with the link built from them and an exact lattice holonomy that is blind to lattice relabellings.
2. Its second-order completion: a lattice torsion-free condition, and whether the resulting walk's field equations reproduce block 64's `D* = −√g R`.
3. Whether the walker's response to the curvature-carrying links is consistent with a ledger (block 55) that contains no link energy of its own.
