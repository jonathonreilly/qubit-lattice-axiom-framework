# Certified touchings of the flux-free comparator for J_x ≠ J_y

Worker `w-jonathonsmac4f50-jf263` (Claude Sonnet 5.5), unit `J:derive:campaign6-20260928-comparator-anisotropic-touchings:a1`.

**Provenance.**
- The claim printed no prior attempts.
- The problem is section 2 of `probes/work/campaign6-probable-20260928/README.md`, written by the owner's other Claude session, the same model family as this worker. Its floating-point nodes are unrefereed.
- Open PRs 9350, 9357 and 9373 (the closed-form families, the κ = 1/2 charge-two points, the handover charge-two points) are the same session's; unrefereed. This worker ran a falsifier and a provenance check on 9373 earlier today, and reuses only its Bloch-matrix idea, rebuilt here.
- The task is not one of this machine's supervisor's blocks.
- Nothing is adopted. `check.py` imports no code from the README, the PRs or their runners; the network and the Bloch matrix are rebuilt from the site and flavour rules.

## 1. The statement attempted

Supplied setting: the four-site Bloch matrix `H(f) = i M(f)` of the `u = +1` quadratic Majorana comparator, couplings `J_x, J_y, J_z`, odd term `κ`.

The README found by floating point that, for `J_x ≠ J_y`, the middle bands still touch on the line `(x, 1 − x, 0)` and at four further points that leave both closed-form planes, and asked for an interval-Newton or topological certificate. This attempt supplies one at the README's two couplings:

- `J = (1, 4/5, 1)`, `κ = 9/20`;
- `J = (6/5, 4/5, 1)`, `κ = 3/10`.

**Result (partial: existence, uniqueness in a box, simplicity, charge).** At each coupling there are six points where the middle bands touch. Each is a simple zero of a three-equation system, unique in an interval box, at zero energy, with the outer bands at `±a`, `a² ≥ 16`. Its charge is `±1`, the sign of the certified Jacobian determinant. The four off-line points lie off both planes `f₁ + f₂ ∈ ℤ` and `f₁ + f₂ − 2f₃ ∈ ℤ` by at least 0.09 and 0.40 (coupling A), 0.155 and 0.24 (coupling B). The count "six" and the absence of further touchings are floating-point search results, not certified.

**A structural consequence.** The charge-two points of the isotropic handover (open PR 9373) have a rank-one Jacobian. For `J_y < 1` each splits into two simple nodes of the same charge at `f₊ ± δ`, `|δ| ≈ 0.46 √(1 − J_y)`, so the charge-two statement of 9373 is special to `J_x = J_y`.

## 2. Steps

Notation: `B = {0, 1}`, `C = {2, 3}` the site pairs of the cell; `S = H_CC − H_CB H_BB⁻¹ H_BC`.

1. **CHECKED (exact, sympy, symbolic in `J_x, J_y, J_z, κ, z₁, z₂, z₃`).**
   - `H` is Hermitian on `|z_j| = 1`.
   - `tr H = 0` and `tr H³ = 0`. So `det(H − λ) = λ⁴ − (tr H²/2) λ² + det H` is even: the spectrum is `{−a, −b, b, a}` at every `f` and every coupling, and a touching of the middle bands is a double zero level.
   - `det(H_BB) · tr S = 0` as a Laurent polynomial identity. So `S` is a traceless Hermitian 2×2 matrix wherever `det H_BB ≠ 0`, and `rank H ≤ 2 ⇔ S = 0 ⇔ F(f) = 0` with the three real functions `F = (S₀₀, Re S₀₁, Im S₀₁)`.
2. **CHECKED (floating point).** A 40³ grid plus Nelder–Mead finds six nodes (gap `ε₃ − ε₂ < 10⁻⁷`) at each coupling and reproduces the README's off-plane node `(0.22300, 0.68644, 0.25024)` and `(0.25506, 0.58995, 0.04264)` to five digits. Discrete sphere fluxes of the lowest two bands (radii 0.004, 0.008; Fukui links) are `±1` at all twelve, summing to zero at each coupling.
3. **CHECKED (interval arithmetic, mpmath `iv`, 40 digits, outward rounding).** A Krawczyk test on `F = 0`, with the Jacobian enclosed over the box from the analytic derivative of the Schur complement, holds in a box around each node (half-width 3·10⁻⁴ or 10⁻³). It shows:
   - exactly one zero of `F` in the box;
   - `|det H_BB| > 0` on the box;
   - the Jacobian determinant has a fixed sign;
   - the enclosure tightened to below `10⁻¹⁹`;
   - `rank H = 2` at the node, with `a² = tr H²/2` bounded below by 16 (from the interval evaluation), so the outer bands are separated.

   Certified nodes (enclosure centres, sign of `det J`):

   | coupling | `f` | sign `det J` | `a²` |
   |---|---|---|---|
   | A | `(0.2229990424374, 0.6864370505652, 0.2502403395392)` | − | 34.7668 |
   | A | `(0.3135629494348, 0.7770009575626, 0.7497596604608)` | − | 34.7668 |
   | A | `(0.3680037841958, 0.6319962158042, 0)` | + | 16 |
   | A | `(0.6319962158042, 0.3680037841958, 0)` | − | 16 |
   | A | `(0.6864370505652, 0.2229990424374, 0.2502403395392)` | + | 34.7668 |
   | A | `(0.7770009575626, 0.3135629494348, 0.7497596604608)` | + | 34.7668 |
   | B | `(0.2550569292669, 0.5899470503957, 0.0426385691717)` | − | 21.0097 |
   | B | `(0.3661397635994, 0.6338602364006, 0)` | + | 16 |
   | B | `(0.4100529496043, 0.7449430707331, 0.9573614308283)` | − | 21.0097 |
   | B | `(0.5899470503957, 0.2550569292669, 0.0426385691717)` | + | 21.0097 |
   | B | `(0.6338602364006, 0.3661397635994, 0)` | − | 16 |
   | B | `(0.7449430707331, 0.4100529496043, 0.9573614308283)` | + | 21.0097 |

   In all twelve, the sign of `det J` equals the sign of the discrete sphere flux. That equality is checked numerically, not derived.
4. **CHECKED (negative control and splitting).**
   - At `J = (1, 1, 1)`, `κ = 1/2`, `f₊ = (1/4, 3/4, 1/2)`: `F = 0` to 10⁻⁴⁰, the Jacobian has singular values `8π, 0, 0`, `a² = 48`, and the Krawczyk test fails, as it must for the charge-two point of 9373. The discrete flux is `−2`.
   - For `J_y = 999/1000, 99/100, 19/20` (`κ = 1/2`, `J_x = J_z = 1`), two simple nodes lie near `f₊`, both certified with the same sign of `det J`. Their distance to `f₊` over `√(1 − J_y)` is 0.4603, 0.4597, 0.4569 (floating point). The flux through the sphere of radius 0.2 around `f₊` at `J_y = 19/20` is `−2`.

## 3. What this does not show

- **No certified count.** "Exactly six" and "no other touching" rest on a grid search. A global certificate (branch and bound on `det H`, which is nonnegative and vanishes only at touchings, outside boxes around the six) is not attempted.
- **Charge.** The identification "charge = sign `det J`" is verified at twelve nodes, not proved. Charge `±1` for a simple zero of the traceless Schur system is the expected degree statement.
- **Two couplings.** Nothing here covers other `J_x ≠ J_y`, `κ`. The method is a template: rational couplings enter through interval endpoints.
- **The `√` law** and its coefficient 0.46 are floating-point fits; deriving the coefficient from 9373's effective Hamiltonian plus the first-order `J_y` perturbation is open.
- **No closed form** for the off-plane positions is given.

## 4. What would finish it

- A branch-and-bound proof that `det H > 0` on the torus outside small boxes around the certified nodes, or a certified degree count on the boundary of each Brillouin cell.
- The coefficient of the `√(1 − J_y)` law from the 2×2 effective Hamiltonian of 9373 at `q = 1/2` plus `∂H/∂J_y` restricted to the kernel.
- A proof that the sign of `det J` is the flux (e.g. via the smooth kernel frame), then the same certificates on a rational grid of `(J_x, J_y, J_z, κ)`.
