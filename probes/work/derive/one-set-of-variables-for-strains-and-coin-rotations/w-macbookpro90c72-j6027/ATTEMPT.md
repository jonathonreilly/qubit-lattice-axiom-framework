# J:derive:one-set-of-variables-for-strains-and-coin-rotations:a2 — w-macbookpro90c72-j6027

Attempt 2 of 3, by claude-opus-5-5 (all of `check.py` and this file). At claim time no other attempt existed on
`ai/probes` for this problem. `python3 check.py` prints 2 `ok` lines, exits 0 with `FAIL` empty, and runs in about 1 s.

All claims are exact:
- sympy identities for the plane-wave symbols;
- Gaussian-rational arithmetic on the exactly stationary state of the `4³` torus. Every value is a multiple of `1/8`,
  and this is asserted.

Nothing is adopted and no gravitational claim is made.

**Sources** (PR branches):
- block 63 (#8593):
  - `G_ξ = ½Σ{ξ_j, S_j}` and `i[H, G_ξ] = Σσ_a ½{C_a[d_aξ_j], S_j}`;
  - the bond current `J`;
  - the plane-wave pair `J = e^{iq_a/2} cos k̄_a Θ`.
- block 64 (#8595):
  - `H[B] = H + Σσ_a ½{C_a[B_a^j], S_j}`;
  - T5, the forward-bond torque `J_a^j(x) − J_j^a(x)`, non-zero on stationary states.
- block 65 (#8596):
  - T1 `−(i/2)[θ·σ, H] = ½Σ_j{(θ×e_j)·σ, S_j} + ½Σ_a C_a[d_aθ_a]`;
  - T2 `H[ϑ]`;
  - T3: the response to `ϑ` is `(1/2)d(ψ†σψ)/dt`, zero on stationary states.

## 1. Statement attempted

**(a) The deformations and their variables.** The two symmetries generate, at first order:
- **relabellings `ξ_j`** (3 per site): the strain `B_a^j = d_aξ_j` on the forward bonds, coupled at second-neighbour
  reach;
- **coin rotations `θ_c`** (3 per site): the site rotation `ϑ`, coupled at nearest-neighbour reach, plus the twist hop
  `½Σ_a C_a[d_aϑ_a]`.

The variables that absorb them are `B_a^j` on the three forward bonds of each site (9) and `ϑ_c` on each site (3). The
antisymmetric part of `B` and `ϑ` coincide at long wavelength. (b) gives the exact difference.

**(b) The exact difference.** Let the rotation of the three forward bonds of `x` be `B_a^j = ε_abj θ_b(x)`. Compare it
with the rotation of the coin at `x` by the same `θ`, with block 65's coupling. On plane waves (`k → k + q`) the two
deformations differ by exactly

`D(k,q) = Σ_{a,j} σ_a ε_abj θ_b [e^{−iq_a/2} cos(k_a + q_a/2) − 1] sin(k_j + q_j/2) cos(q_j/2) − i Σ_a θ_a sin(q_a/2) cos(k_a + q_a/2)`.

- For a uniform rotation (`q = 0`), `D = Σσ_a ε_abj θ_b sin k_j (cos k_a − 1) = O(k³)`: the bond coupling carries
  `cos k_a`.
- At first order in `(k, q)` jointly, `D = −(i/2)θ·q`. This is the twist hop, which a rotation of bonds does not
  carry.
- The half-bond shift `e^{−iq_a/2}` enters the coin-dependent part at order `q·k`.

**(c) The decision.** Tie the antisymmetric part of the bond strain to the site rotation. Two placements were tested:
- **forward:** the three forward bonds of `x` rotate by `ϑ(x)`;
- **shared:** the rotation is split equally between the forward and backward bonds of `x`.

**Neither tie makes both laws exact with consistent static equations for a field energy blind to `ϑ`.** Under the tie,
such an energy's static equation for `ϑ` requires the content's total response to `ϑ` to vanish on every stationary
state. That response is the coin response (block 65 T3) plus the tied bond torque. On the exactly stationary state of
the `4³` torus:
- the coin response is **0 at all 64 sites**;
- the forward torque is **non-zero at all 64 sites**;
- the shared torque is **non-zero at 60 sites**.

So the tie fails on a stationary state.

The choice that does work keeps the antisymmetric bond strain as **independent** variables: 9 + 3 per site, with the
field energy blind to `ϑ` but not to rotations of the bonds.
- Both laws are then exact by construction.
- The `ϑ` equation is block 65 T3's identity, zero on stationary states.
- The antisymmetric `B` equations balance block 64 T5's torque against the field's own response to bond rotations.

That field energy is not pointwise blind to `e → R(x)e` in the bond variables. So block 64's continuum argument for
`β = 1`, which assumes pointwise blindness, does not carry over as stated. On the lattice, bond rotations and coin
rotations are different, and the field must see the first but not the second.

## 2. Steps

**B1 — the plane-wave pieces. CHECKED** (sympy scalar identities); the assembly is **PROVED**.
- `C_a[v]` with `v = a·e^{iq·x}` on bond `x → x+e_a` acts as `a·(e^{ik_a} + e^{−iq_a}e^{−ik_a})/2 = a·e^{−iq_a/2}cos(k_a + q_a/2)`.
- The anticommutator with `S_j` gives `(sin k_j + sin(k_j + q_j))/2 = sin(k_j + q_j/2)cos(q_j/2)`, for a site
  multiplier and a bond hop alike.
- The twist hop gives `θ_a(e^{iq_a} − 1)(e^{ik_a} + e^{−iq_a}e^{−ik_a})/4 = iθ_a sin(q_a/2)cos(k_a + q_a/2)`.
- Assembling block 64's strain term and block 65's `H[ϑ]` term by term gives `D`.

**B2 — the orders. CHECKED** (series of the scalar factors).
- The `σ` part: `[e^{−iλq/2}cos(λk + λq/2) − 1]·sin(λk + λq/2)cos(λq/2)` has no `λ¹` term and a non-zero `λ²` term.
- The twist: `−i sin(λq/2)cos(λk + λq/2) = −(i/2)λq + O(λ³)`.
- At `q = 0`: `(cos λk − 1)sin λk = O(λ³)`, with a non-zero `λ³` term.

**C1 — the exactly stationary state. CHECKED.**
- The state is `ψ = Σ_a i^{x_a}u_a`, with `u_a` the `+1` eigenvectors of `σ_a`: `(1,1)`, `(1,i)`, `(1,0)`.
- For each `a`, `S_b i^{x_a} = δ_ab i^{x_a}` (the wave number is `π/2`), so `Hψ = ψ` exactly. This is checked.

**C2 — the responses. CHECKED** exactly at all 64 sites.
- The combination `Σε_cad Θ_d^a − ½[b_c(x) − b_c(x − e_c)]` is 0 at every site. This re-checks block 65 T3.
- The forward torque `Σε_caj J_a^j(x → x+e_a)` is non-zero at 64 sites.
- The shared torque `Σε_caj ½[J_a^j(x → x+e_a) + J_a^j(x−e_a → x)]` is non-zero at 60 sites.

**C3 — the decision. PROVED.**
- Under a tie `B_antisym = T[ϑ]`, the response of `⟨H[B(ϑ), ϑ]⟩` to `ϑ_c(x)` is the coin response plus `T†` applied
  to the bond currents. For the two ties this is the forward or the shared torque.
- A field energy blind to `ϑ` contributes nothing to the `ϑ` equation. That equation therefore requires this response
  to vanish, which C2 refutes.
- With `B_antisym` independent, the `ϑ` equation is C2's zero, and the `B` equations are ordinary balance equations.

**ASSUMED.**
- Block 63's plane-wave-pair formula, used only in §3 for the long-wavelength order of the torque.
- The couplings of blocks 64 and 65 as stated on their branches.

## 3. Where the route stops
- **(c) is decided for local ties of the tested form**: forward bonds, and shared forward/backward bonds. A general
  linear tie `B_antisym = T[ϑ]` would work only if `T†` annihilated the bond currents of every stationary state. The
  `4³` state constrains `T` but does not by itself exclude every `T`.
- **The long-wavelength order of the obstruction** is not checked here. By block 63's pair formula, for symmetric `Θ`
  the torque is `Θ_aj(e^{iq_a/2}cos k̄_a − e^{iq_j/2}cos k̄_j)`, i.e. of second order in the wave vectors. The exact
  state has wave numbers `π/2`, where it is of order one.

## 4. What would finish it
- The general tie: the space of local linear maps `T` with `T†J = 0` on all stationary states of the `4³` and `6³`
  tori (a finite linear-algebra problem). An empty space would close (c) for every local tie.
- The field energy the 9 + 3 choice needs: relabelling-blind, blind to `ϑ`, seeing bond rotations. Its second-order
  form, and whether block 64's `β = 1` survives with it.
- Block 65's rotation carried along bonds, the finite-rotation version: whether a single bond variable can carry both
  laws beyond first order.
