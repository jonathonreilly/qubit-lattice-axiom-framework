# J:derive:the-partial-swap-walk-in-three-dimensions:a1

Worker: Claude Sonnet 5.5 (`claude-sonnet-5-5`), same model family as the authors of blocks 53-54, 105, 108. Unrefereed. Nothing below is a status claim.

## Plain-language summary

The partial-swap walk is a set of small two-site rotations applied in layers. Put in three dimensions and applied in a symmetric ("palindromic") order, it has an exact 2x2 recipe per wave vector. Three things came out.

1. The recipe is an explicit polynomial. Its first-order part is `2 eps (cos k_1, cos k_2, cos k_3) . sigma`. The next correction to the frequency is `eps^2 rho(k)`, with `rho = -1/6` at each zero-frequency point (the same number as the line case in block 105 T2).
2. The walk run backwards is the same walk with every angle negated. So the frequency is odd in `eps` and the band's spin direction is even in `eps`: there is **no O(eps) eigenvector term** in the palindromic order, to all orders and for any clock field. In the plain (non-palindromic) order there is one, and it is a fixed linear distortion of the spin field.
3. The sideways drift is **not** produced by an O(eps) eigenvector term. It is the zeroth-order effect of the band's spin texture near the zero-frequency point (a Berry-curvature monopole), which the scalar ray model does not have. A packet run (floating point, labelled) shows it at `eps0 = 0.05` and `0.2` with the same size to 3%, and matches a ray cloud carrying the Berry term to 7-11% (palindromic order). The packet drifts the opposite way to block 54's measurement because the zero-frequency point at `k = (pi/2)(1,1,1)` has the opposite handedness to block 54's point at `k = 0`.

Verdict: **PARTIAL.** The exact dispersion (a) and the exact no-O(eps)-term result for (c) are done. The ray factor (b) is exact at the dispersion level. The exact drift law for the discrete walk is not proved: it rests on the semiclassical Berry-velocity picture (ASSUMED) and floating-point checks.

## 0. What I read, and source status

- Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (lines 35-83: Lattice, Qubit, Admissibility, Record; line 116: "Admissibility is not a dynamics axiom"; it supplies no Hamiltonian, transfer operator, time metric or weights). Read in full: `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (approved primitives: `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`). **None is used.** The walk, its layers, its order and its clock are supplied clauses, not axioms or primitives. The `kinetic_isotropy_primitive` (c_t = c_s) is not used; nothing here fixes a time metric.
- Landed notes on main (`main_wt`, a detached checkout; line numbers are from it):
  - block 105, `docs/ADMISSIBILITY_RULE_IN_DISCRETE_TICKS_A_LOCAL_CLOCK_IS_EXACT_ONLY_FOR_WALKS_THAT_DO_NOT_MOVE_THE_FLAT_BAND_THEOREM_AND_A_WALK_CLOCKED_TO_RELATIVE_EPS_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-23.md` T1 (lines 24-27), T2 (lines 29-35);
  - block 54, `docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md` T1 (32-40), T4 (58-66), N8 (97);
  - the 3D exponential-field note (block 108's extension), `docs/ADMISSIBILITY_RULE_IN_THREE_DIMENSIONS_THE_CLOCKED_WALK_NEEDS_A_FAST_END_CONDITION_..._2026-09-23.md`, used only for its statement of the walk;
  - `docs/ADMISSIBILITY_RULE_RAYS_IN_THE_WALKERS_FRAME_..._2026-09-24.md` lines 49 and 135, which name the anomalous (Berry) velocity as a comparator only.
- **Landed version controls where the SETTING differs.**
  - Block 54: the exact packet force is withdrawn (T3 is a finite-power identity; line 48). T4 is a conditional ray model with `epsilon^2 = |k|^2 + C` as one special case and `M = diag(cos 2k_j)` for the selected walk (lines 58-66). **The sideways-drift fits (`-gT/(2k)`) are "historical author calculations, not a general ray-limit proof"** (N8, line 97). I do not use the number `gT/(2k)` as a landed claim; I use it only as a comparison and re-derive its origin.
  - Block 105 as landed: T1 is about the line, "unitary even for unbounded angles" (a direct sum of finite rotations); T2 is a smooth-branch, nonzero-frequency statement, "not an exact packet trajectory theorem". The phrase "follows block 54's clock to relative eps^2" in the SETTING is exactly `eps omega_eps/omega = 1 - eps^2 sin^2 k/3 + O(eps^4)`; I take it in that form only. Block 105's PR #8934 is closed; I did not build on its branch.
- No task-named source branch exists, so no `RECOVERY_STATUS.json` is written.
- Prior art searched. Both of these are earlier attempts on `ai/probes` (same family), read after I fixed my plan:
  - `probes/work/derive/ray-limit-of-the-clocked-walk/w-macbookpro90c72-j3c21/ATTEMPT.md` (a4) already gives the exact lattice Berry curvature of `H = sigma . sin k`, `Omega_i = -sin k_i cos k_j cos k_l / (2|d|^3)`, and identifies block 54's sideways drift as the anomalous velocity `-kdot x Omega` (floating point, rays against walk: -0.1200 vs -0.1185 at k = 0.5). It marks Lemma C (adiabatic branch purity) ASSUMED.
  - `probes/work/compute/clocked-walk-sideways-drift-grid/w-jonathonsmac4f50-j6c55/RESULT.md` gives the grid and the eight-node handedness signs `+ - - + - + + -`.
  - **So the identification "block 54's drift = Berry anomalous velocity of the band of `sigma . sin k`" is retrieval here, not new.** Open PRs: `gh pr list --search 'sideways drift OR anomalous velocity OR Berry partial-swap'` returned none.

## 1. The exact statement attempted

**Setting (all supplied, nothing adopted).**

- S1. Internal space `C^2`, Pauli matrices `sigma_1, sigma_2, sigma_3`. For each axis `j` a basis `{a_j, b_j}` with `sigma_j = |a_j><b_j| + |b_j><a_j|` and partner `sigma_{j+1} = -i|a_j><b_j| + i|b_j><a_j|` (indices cyclic). This cyclic partner is **my choice**; a3's plan is not visible to me. The parity results below do not depend on it; the explicit polynomial, `rho`, and the plain-order twist do.
- S2. Layers. `A_j` rotates each pair `{(a_j,x),(b_j,x+e_j)}` by `exp(-i eps_b sigma_x)`; `B_j` rotates each pair `{(b_j,x),(a_j,x+e_j)}`. Bond angle `eps_b = eps0 sqrt(w_x w_y)`.
- S3. **Palindromic order** (my reading: six distinct layers cannot themselves be a palindrome). With `L = (A_1, B_1, A_2, B_2, A_3, B_3)`:
  `U = L_1(e/2) L_2(e/2) L_3(e/2) L_4(e/2) L_5(e/2) L_6(e) L_5(e/2) ... L_1(e/2)`, i.e. each layer appears twice at half angle except the middle one. Each layer's total angle is `e`. The plain order is `U_plain = L_6(e) ... L_1(e)`.
- S4. For (a), a uniform angle. For (b), `w` smooth, `E(k,x) = omega(k; eps0 w(x))`.

**Claims attempted.**
- (a) the exact dispersion of `U` at a uniform angle;
- (b) its ray law against block 54's 3D law (`E = w |sin k|`, `M = diag(cos 2k_j)`);
- (c) whether an O(eps) eigenvector term produces the sideways drift.

## 2. Steps

1. **PROVED** (full argument; also **CHECKED** exactly, `check.py` 1.2-1.4). Every layer is a direct sum of disjoint 2x2 rotations, so `U` is unitary for every clock field and moves a site by at most 4, 4, 3 sites along axes 1, 2, 3 (layers touching an axis, counted with multiplicity). Because `L(-a) = L(a)^{-1}` for every layer and the product is palindromic, `U(-angles) = U(angles)^{-1}` for **every** clock field. Check 1.4 verifies this exactly on random finite-support vectors with a non-uniform clock (Pythagorean angles).

2. **CHECKED** (`check.py` 1.1, exact Gaussian rationals on a 4x4x4 torus; 20 wave vectors including all 8 zero-frequency points, both spinors, `cos(e/2) = 3/5`). The lattice walk acts on `e^{ik.x} u` as `u -> S(k) u`, with `S` the product of eleven 2x2 factors `cos a - i sin a g`, `g_A = cos k_j sigma_j - sin k_j sigma_{j+1}`, `g_B = cos k_j sigma_j + sin k_j sigma_{j+1}`. These are dimer symbols with `g^2 = 1`, so each factor is an exact rotation.

3. **CHECKED** (`check.py` 2.1-2.4, exact sympy). `S = q0 - i q.sigma` with `q0^2 + |q|^2 = 1`; the quaternion polynomial equals an explicit 11-factor matrix product at six exact rational points. **This is (a):** the exact dispersion is `cos(omega) = q0(k, eps)`, a trigonometric polynomial in `k` (79 monomials in `(C, Sn, c_j, s_j)` after the reductions `c^2 + s^2 = 1`, `C^2 + Sn^2 = 1`), printed and stored by `check.py`.

4. **PROVED** (from steps 1 and 2) and **CHECKED** (2.2, 2.3): `S(-eps) = S(eps)^{-1}`. So `q0` contains only even powers and `q` only odd powers of `eps`. Hence `omega` is odd in `eps` and the unit vector `n = q/|q|` is **even** in `eps`.

5. **CHECKED** (2.5-2.8, exact series). `q = 2 eps (cos k_1, cos k_2, cos k_3) + O(eps^3)`, with no `eps^2` term. `omega = 2 eps |c| (1 + eps^2 rho(k) + O(eps^4))`, `|c|^2 = P = sum_j cos^2 k_j`, with
   `rho = [c1^4 + c2^4 + c3^4 - 4(c1^2 c2^2 + c1^2 c3^2 + c2^2 c3^2) - (c1^2 + c2^2 + c3^2) - 3 c1^2 c2 s1 - 3 c2^2 c3 s2 + 3 c1 c3^2 s3] / (6 P)`.
   At a zero-frequency point `k = (pi/2)(1,1,1) + t n`: `rho = -1/6 + (t/2)(n1^2 n2 + n2^2 n3 - n1 n3^2)/|n|^2 + O(t^2)`. The isotropic value `-1/6` equals the line value `-sin^2 k/6` of block 105 T2 at its node. The terms with `s_j` come from the layer order and the cyclic partner; they make `rho` odd in `q` at the next order (not inversion symmetric).

6. **CHECKED** (2.9; Hamilton's equations are standard, not re-proved). **This is (b).** For the scalar ray model `E = omega(k; eps0 w(x))`: `kdot = -(eps d_eps omega) grad log w`, `vdot_j = -sum_l (d_j d_l omega)(eps d_eps omega) d_l log w` (exact for that Hamiltonian). Relative to block 54's rays the force factor is `eps d_eps omega/omega = 1 + 2 eps^2 rho + O(eps^4)`, which at the node is `1 - eps^2/3`: the same as the line. In the 3D walk the O(eps^2) correction is anisotropic away from the node (the `s_j` terms). Block 54's law is the `eps -> 0` limit with the time rescaled by `2 eps`.

7. **CHECKED** (3.1-3.4, 4.1-4.4, exact) and **PROVED** (determinant identity, 3.3a). Plain order `U_plain` has `q2 = -2(c2(2c3 + s2), c3(s3 - 2c1), c1(2c2 + s1)) != 0`. At the node `q/eps = -2t(1 - eps R) n + ...`, `R` the cyclic shift. This is a linear map of the monopole field `c`; for `N = M c` the solid-angle density is `det(M) c.(dc x dc)/|Mc|^3`. So the O(eps) eigenvector term of the plain order rescales the monopole density by `1 + eps(tr A - 3 c^.A c^)` (zero sphere average, 3.4), equal to `1 + 3 eps (n1 n2 + n2 n3 + n3 n1) = 1 + (8/3) eps` along `n = (2,1,2)/3` (check 4.4); in the palindromic order the correction at this order is absent (4.2), and the next one is relatively `O(eps^2 t)`: `(43/36) t` along the same `n` (4.3).

8. **READING / ASSUMED** (semiclassics; not proved here). The packet's sideways displacement is `-int kdot x Omega dt` with `Omega` the Berry curvature of the Floquet band eigenvector `n(k; eps)`, plus the scalar ray motion. With step 4 and the leading order of step 5, `n = c^ + O(eps^2)`: the curvature near the node is the monopole of `c^`, `Omega = +q^/(2 q^2)` for this left-handed node (check 4.1; the sign is opposite to the `sigma . sin k` node at `k = 0`). In the tick-time units the drift is `g T/(2 |q|)` at long wavelength, along `+(gradient x motion)` here.

9. **CHECKED** (`check.py` 5.1, exact). For a Bloch rotation by `2 theta` about `n`, `(R - 1)^{-1} v = -v/2 - (cot theta/2) n x v` on `v perp n`. The `n x v` part carries a factor `1/theta ~ 1/eps` and, multiplied by the per-tick change of `n` (order `eps g`), gives an order-`eps^0` sideways velocity. The `-v/2` part is smaller by a factor `theta ~ eps`. **READING:** this is the sense in which an "O(eps) term" cannot be the source: the source is the precession-lag part, present at `eps -> 0`.

10. **CHECKED, floating point, NOT exact** (`check.py` section 6 and `sim2.py` runs, table below).

## 3. Numerical packet runs (floating point)

All: `g = +/-0.004`, `T = 30` (ticks = `T/(2 eps0)`, so the speed is 1 at long wavelength), `k0 = 0.5`, packet width 5 in a periodic box of side 64, packet built on the exact upper Floquet band, centred on the node `(pi/2)(1,1,1)` via the staggering `i^(x+y+z)`. Edge weight about `1e-3`. Displacements are the odd-in-`g` parts. "Cloud" = 1200 rays sampled from the packet's Gaussian phase-space distribution, with the exact `omega` of the stated order; "+Berry" adds the numerically computed anomalous velocity `-kdot x Omega` of the exact Floquet band.

| case | packet (x,y,z) | cloud, no Berry | cloud +Berry | packet - cloud (no Berry) | Berry prediction |
|---|---|---|---|---|---|
| pal, eps0 = 0.2, m = x, grad = z | (0.002, 0.113, -1.536) | (-0.002, -0.013, -1.537) | (-0.003, 0.104, -1.537) | y = 0.126 | y = 0.117 |
| pal, eps0 = 0.05, same | (0.000, 0.117, -1.613) | (-0.003, -0.013, -1.613) | (-0.003, 0.104, -1.613) | y = 0.130 | y = 0.118 |
| pal, eps0 = 0.2, m = (1,1,0), grad = z | (-0.070, 0.069, -1.548) | (0.015, -0.012, -1.552) | (-0.062, 0.066, -1.552) | (-0.085, 0.080) | (-0.077, 0.077) |
| plain, eps0 = 0.2, m = x, grad = z | (-0.247, 0.242, -1.481) | (-0.287, 0.137, -1.429) | (-0.287, 0.247, -1.429) | (0.040, 0.105) | (0.000, 0.110) |
| plain, eps0 = 0.2, m = (1,1,0), grad = z | (-0.335, -0.120, -1.261) | (-0.253, -0.245, -1.222) | (-0.330, -0.167, -1.222) | (-0.082, 0.125) | (-0.077, 0.078) |

Reading of the table:
- The fall (z) of the packet matches the cloud of rays of the **exact** `omega` to 3e-4 in the palindromic cases. The fall at `eps0 = 0.2` is 4.8% smaller than at `eps0 = 0.05` (-1.536 vs -1.613), and the exact-`omega` cloud reproduces that (-1.537 vs -1.613). So the departure from block 54's 3D law at `eps0 = 0.2` is an O(eps^2) effect that the exact `omega` captures; this supports (b).
- The sideways displacement is about 0.12-0.13 at both `eps0 = 0.05` and `0.2` (3% apart). It is an order-`eps^0` effect. Scalar rays give 0.013 or less.
- The Berry cloud reproduces the palindromic sideways displacement to 7-11% (ratios 1.08, 1.11, 1.07), in direction and orientation dependence (axis 0.117 vs diagonal 0.109 predicted; 0.126 vs 0.117 measured). The residual (about 0.01) is unexplained; it is of the size block 54's own runs showed (walk -0.1185 vs `-gT/(2k)` -0.1200, rays 4% different at k = 0.25).
- **The plain order is a worse test.** Its packet moves about 5 units in y and in z even in the part that is even in `g` (the odd part is what is shown), and the Berry cloud is off by 0.05 in the diagonal case (0.125 vs 0.078 in y) and 0.04 in x on the axis. I did not resolve why. I do not claim the plain order obeys the semiclassical picture to better than that.

## 4. What is new, and what is not

**Not new (retrieval or known):** the line formulas of block 105 T1-T2; the Berry-curvature explanation of block 54's drift for `H_w = sqrt(w) (sigma . D) sqrt(w)` (earlier attempt `ray-limit-of-the-clocked-walk:a4` and the grid run); eight-node handedness signs; the standard semiclassical `xdot = d_k E - kdot x Omega`.

**New in this attempt (same-family, unrefereed), scoped to the choices S1-S3:**
- N1. The 3D palindromic partial-swap symbol, exactly, as eleven dimer factors, verified against the lattice walk on a torus (steps 2-3); the explicit half-trace polynomial.
- N2. The parity theorem (step 4): quasi-energy odd, band vector even in `eps`, for every palindromic product and every clock field (step 1 gives the inverse statement for the operator). Consequence (formal, by the Baker-Campbell-Hausdorff series for small angles, which I did not make rigorous): the palindromic walk has no even-order term in its effective generator; its deviation from the first-order bond-weighted generator is relative `O(eps^2)`.
- N3. The exact `eps^2` coefficient `rho(k)` and its node limit with the explicit odd-in-`q` anisotropy (step 5), and the ray-force factor (step 6).
- N4. The no-go for (c): the O(eps) eigenvector term is identically zero in the palindromic order and, in the plain order, is a constant linear map on the node's spin field; neither can create the monopole (its flux is a degree), and the drift is the order-`eps^0` precession lag (steps 7-9). The drift is the same size at `eps0 = 0.05` and `0.2`.
- N5. The handedness: the node `(pi/2)(1,1,1)` of the partial-swap walk is left-handed relative to block 54's `k = 0`; the packet drifts along `+(gradient x motion)` here and `-` in block 54.

## 5. First unresolved step, and what would finish it

**First unresolved step: 8.** There is no exact lattice-packet theorem that the discrete walk's sideways displacement equals `-int kdot x Omega dt` with the Floquet Berry curvature. It is semiclassical (Floquet version) and ASSUMED; the numerics support it to 7-11% in the palindromic order only. The earlier attempt's Lemma C (adiabatic branch purity) is also open for the discrete walk.

What would finish it:
- an adiabatic theorem for the Floquet walk with gap `2 omega` (so degrading like `g/k` at the nodes), giving the anomalous velocity with a stated remainder;
- an exact statement for the plain order explaining the 5-unit even-in-`g` motion and the 0.05 mismatch;
- the choice of basis phases `phi_j` and layer order: the dispersion polynomial depends on S1 and S3, and the cubic-rotation covariance of the axis-dependent basis is not established (the cyclic partner is covariant under 3-fold rotations about (1,1,1) only);
- the extension from the uniform angle to a nonuniform clock for `rho` (step 1 covers parity; the O(eps^3) generator for a gradient is not computed).

## 6. Files

- `ATTEMPT.md`, `check.py` in this directory. Also left here, not required: `sim_lib.py`, `sim2.py` (the packet runs of section 3), `run_*.txt` (their outputs), `explore*.py` (scratch).
