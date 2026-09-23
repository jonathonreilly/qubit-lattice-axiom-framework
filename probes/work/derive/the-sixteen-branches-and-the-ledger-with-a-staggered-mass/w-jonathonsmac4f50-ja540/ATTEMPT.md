# the-sixteen-branches-and-the-ledger-with-a-staggered-mass: derivation attempt 2 of 2

Worker `w-jonathonsmac4f50-ja540` (claude-opus-5-5), unit `J-derive-the-sixteen-branches-and-the-ledger-with-a-staggered-mass-a2`.

**Provenance.** No other attempt at this problem is on `ai/probes`, and the plan is my own. Definitions come from the notes on the PR branches:
- block 70 (#8602): the species maps `V_n = R_nU_n`, `s_n`, and `Θ = σ₂K`;
- block 71 (#8603): the twins `A_n = ΘV_n` and `e_x = Re ψ†_x(H_wψ)_x`;
- block 76 (#8611): `E_sea`, `Π(q) = c₀/4 + (κ/4)|q|²_lat`, and the chessboard invisibility T1;
- block 77 (#8612): the staggered term, with T3(c) `φ(H + mε)φ = φHφ + m w ε`, and W3.

Nothing is adopted.

## 1. Statement attempted

Write `H' = H + mε` (`m > 0`) and `H'_w = φHφ + m w ε`, where `φ = √w = e^{u/2}`.

**(a) Test bodies.**
- The four even maps `V_n` still commute with `H'` exactly.
- The four odd maps now send `H'` to `−H + mε`. So `εV_n` commutes with `H'`: a symmetry that keeps the sign of the energy.
- `Θ` commutes with `H'`. Block 71's twin maps `A_n = ΘV_n` (odd `n`) therefore no longer reverse the energy: `A_nH'A_n^{-1} = −H + mε`.
- **No on-site map reverses the energy of `H'` when `m ≠ 0`.** An on-site `X` commutes with `ε`. So `XH'X^{-1} = −H'` would force `XHX^{-1} + H = −2mε`, where the left side moves one step and the right side is on-site.
- Twins need a map that reverses `ε`. The translation `τ` by `e₁` composed with the site sign, `τε`, anticommutes with `H'` in a uniform field. In a rate field, `τε H'_w (τε)^{-1} = −H'_{τw}`.

  So **a negative-energy massive packet is the exact twin of a positive one in the field translated by one site.** It is not an exact twin in the same field. The difference is first order in the field's gradient.

**(b) Sources.** For every state `ψ`, `e_{z+e₁}[τεψ] = −e_z[ψ]`: the twin's energy density is minus the original's, displaced by one site. The sublattice alternation is this displacement:
- a positive-energy packet at rest (energy `+m w`) lives on the `ε = +1` sublattice;
- its twin (energy `−m w`) lives on the other sublattice.

**(c) The massive sea's stiffness.** Floating point, labelled.

| m | 0 | 0.25 | 0.5 | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|
| κ (L = 24) | 0.0980 | 0.0970 | 0.0915 | 0.0766 | 0.0630 | 0.0523 | 0.0382 | 0.0297 | 0.0204 | 0.0154 |

- `κ(m) > 0` at every `m` computed. It decreases from `m = 0.25` on and tends to 0 like `1/(8m)`.
- **Exactly at large `m`: `κ = 1/(8m) + O(m^{−3})`.** This is second-order perturbation theory in the hop. The executed values fit `1/(8m) − 0.104/m³`.
- **The heavy sea decouples, and `κ` does not change sign: the HIT condition is not met.**
- The volume term is `c₀(m) = −⟨√(|sin k|² + m²)⟩_BZ`, exact for uniform clocks: `−1.194, −1.569, −2.342, −4.183` at `m = 0, 1, 2, 4`.
- For `m > 0` the numbers converge fast in `L`, because the sea is gapped. Block 77's W3 (`κ = 0.089, 0.090, 0.076` at `L = 8`) is reproduced.

**(d) The chessboard zero mode. A mass removes it; the parenthetical in the task expected the opposite.**
- A chessboard of clocks is still invisible to the hop, since `φHφ = H` (block 76 T1). But the rest term is `m w ε`, and it is not invisible: for `w = e^{aε}`,

  `m w ε = m cosh a · ε + m sinh a`.

  It adds a uniform offset `m sinh a` and raises the staggered mass to `m cosh a`.
- `ε` does commute with the chessboard of rates. But commuting does not make the term invariant: the term's size is `w`.
- Exactly, `E_sea(a) = N m sinh a − Σ_k √(E_k² + m² cosh²a)`.
- Its first variation at `a = 0` is `+Nm`, not 0. The chessboard mode becomes a linearly driven direction: the sea's energy falls if the clocks on the `ε = −1` sublattice run faster.

## 2. Steps

**S1 (PROVED; CHECKED `E1.1`–`E1.3`). The maps.** `U_n` is a site sign and `R_n` a coin rotation, so both commute with `ε` and with every site field. By block 70 T1(b), `V_nHV_n = s_nH`. So `V_nH'V_n = s_nH + mε`. For odd `n`, `ε` anticommutes with `H` and commutes with `ε`, so `ε(−H + mε)ε = H'`. `Θ` commutes with `H` (block 70 T3(b)) and with the real, coin-scalar `mε`. `E1` checks all of this with exact integer matrices on the `4³` torus at `m = 3`.

**S2 (PROVED; CHECKED `E1.6`). No on-site twin.** An on-site operator is block-diagonal in sites, so it commutes with `ε`. `H` moves exactly one step, so `XHX^{-1} + H` has no on-site part while `−2mε` is purely on-site. Both sides vanish only if `m = 0`.

**S3 (PROVED; CHECKED `E1.4`, `E1.5`). Twins by translation.**
- `τ` commutes with `H` and with uniform fields, and sends `ε` to `−ε`.
- So `τεH'ετ^{-1} = τ(−H + mε)τ^{-1} = −H − mε`.
- In a rate field `τ` moves the field: `τφHφτ^{-1} = (τφ)H(τφ)` and `τ(wε)τ^{-1} = −(τw)ε`.

`E1.5` checks the identity exactly for a random integer `φ`. Inversion through a bond centre is another `ε`-reversing twin map, with the field inverted.

**S4 (PROVED; CHECKED `E2`). The twin's energy density.** Let `χ = τεψ`. Then `H'χ = −τεH'ψ` (uniform field; in a rate field, `H'_{τw}χ = −τεH'_wψ`). Hence

  `χ†_{z+e₁}(H'χ)_{z+e₁} = −ψ†_z(H'ψ)_z`,

because `ε² = 1`. Taking real parts gives the claim. `E2` checks it at every site for random Gaussian-integer states.

**S5 (PROVED; CHECKED `E3`). The chessboard with mass.**
- `φ_xφ_y = 1` on every bond (neighbours have opposite `ε`), so `φHφ = H`.
- `m e^{aε}ε = m(cosh a·ε + sinh a)`, checked separately on each sublattice.
- `(H + m cosh a·ε)² = H² + m²cosh²a`, because `{H, ε} = 0`. So the eigenvalues are `m sinh a ± √(E² + m²cosh²a)`.
- `m sinh a < m cosh a` means the `N` negative states are exactly the minus branch. Hence the closed form for `E_sea(a)`, whose derivative at 0 is `Nm`.

**S6 (PROVED to second order in `1/m`; CHECKED `E4`). The large-mass stiffness.** Take `H'_w = m w ε + K` with `K = φHφ`.
- At `K = 0` the negative space is the odd sublattice (two coin states per site, energies `−m w_x`). This has no gradient term.
- `K` joins odd to even sites only. Summed over the two negative states, its second order is `−Σ_bonds tr(K_{xy}K_{xy}†)/(m(w_x + w_y))`, with `tr(K K†) = w_x w_y · tr(σ_a²)/4 = w_x w_y/2`.
- Expanding `w_x w_y/(w_x + w_y)` to second order in `u` (`E4.2`), the bond term contains `+(1/(16m))(u_x − u_y)²`, i.e. `κ = 1/(8m)`.
- The third order vanishes, because `K` changes sublattice.

This is perturbation theory, valid while `‖K‖ < m min w` (`‖H‖ ≤ √3`). The executed approach to `1/(8m)` (`N2`) is the numerical check.

**S7 (floating point; `N`). `κ(m)` by block diagonalisation.**
- For a mode `u = ε₀cos(2πnx/L)` along `e₁`, the problem stays translation-invariant in `y` and `z`.
- The mass pairs `(k_y, k_z)` with `(k_y + π, k_z + π)`, giving blocks of size `4L` with `x` explicit.
- `Π(q)` comes from two-amplitude second differences with Richardson extrapolation. Then `κ = (Π(q) − c₀/4)/(|q|²_lat/4)`, with `c₀ = E_sea/N` (block 76's definitions).
- `N3` reproduces block 77 W3 at `L = 8`. Values at `L = 32`, not in the script: `κ(0) = 0.0986`, and for `m ≥ 1` identical to 4 digits with `L = 24`.

## 3. What remains

- **A true twin in the same field.** The massive walk has no energy-reversing map in the same field: S2 is exact. Whether block 71's "chase" survives is therefore a gradient-order question. The twin of a packet in field `w` lives in the field shifted by one site, and the difference in fall is `O(∇w)`. Computing that correction is the next step.
- **The driven chessboard (d).** If the sea's energy is booked as the field's energy (block 76's reading), a massive sea drives the clocks toward a chessboard at linear order. With the volume term also present, whether this is an instability or is balanced by the field's own energy (block 56's bond term, which does see the chessboard) is a question about the full ledger, not settled here.
- **`κ(m)` between 0 and 1** is flat-then-decreasing, and the massless value converges slowly in `L`. No exact expression is given for small `m`.

`SUMMARY: PARTIAL` (no HIT: `κ(m)` does not change sign).
