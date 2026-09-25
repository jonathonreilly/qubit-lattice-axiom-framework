# Two walkers scattering through the member's pull: where exact books fail

Task `J:derive:scattering-through-the-member-breaks-exact-books:a2`, worker `w-macbookpro9927a-j4dc1`,
model claude-opus-5-5. Checker: `check.py` in this directory (exact arithmetic, about 20 s, `TOTAL: PASS=9 FAIL=0`).

**Sources.** All four notes are read as landed on `origin/main` at `25b8c1874f2ea657653dbb298bf383c18d81e0b5`:
- block 143 (`ADMISSIBILITY_RULE_EXACT_BOOKS_NEED_RECORDS_THAT_NEVER_SCATTER_OR_BIND_...`);
- block 137 (`..._KEEPS_THE_BOOKS_ONLY_AT_LEADING_ORDER_...`);
- block 140 (`..._THE_WALK_CARRIES_AN_EXACT_BOOST_CHARGE_...`);
- block 53 (`..._NO_MASTER_CLOCK_..._LATTICE_LAPLACE_EQUATION_...`).

PRs #9197, #9203, #9229 and #8568 are closed, and their notes are on main.

Landed block 143 narrows its T3 and T5 to conditional implications that rest on an unresolved analytic bridge. The narrowed wording controls here. Nothing below uses T3 as a result.

**Related prior work, disclosed.** I checked block 144's velocity-dependent pull (issue #9245). I also released the excluded-record-interactions recovery unit, with route notes on placements. Neither treats scattering under the pull, and there are no earlier attempts on this problem.

## 1. Statement attempted

**Setting.** These are supplied clauses; nothing is adopted and no gravitational claim is made.

- **One record** on `Z^3` with a coin `C^2`: `H = sum_a sigma_a S_a`, with symbol `h(k) = sum_a sin k_a sigma_a` and `eps(k) = |sin k|`.
  - The energy density is `e_x = (Pi_x H + H Pi_x)/2` (block 137).
  - Its first moment is `D = (XH + HX)/2`, with `i[H, D_a] = P_a = S_a C_a` (block 140 T1). The symbol of `P_a` is `(1/2) sin 2k_a` times the identity on the coin.
- **Two records**: `H2 = H(x)1 + 1(x)H`.
  - The records are either distinguishable or restricted to the exchange-symmetric or exchange-antisymmetric subspace.
  - One record per site is not imposed: under it, block 137 already loses the books with no pull.
- **The pull** (the task's first option). Take block 53's selected log-linear clock law `L u = s`, with `L = I - A` and `A` the six-neighbour average.
  - On `Z^3` use the decaying inverse `G`: `Ghat(p) = 1/Lhat(p)`, with `Lhat(p) = 1 - (1/3) sum_a cos p_a`. On the `L^3` torus use the neutral inverse `G_L`.
  - The interaction is `V = sum_{x,y} G(x-y) e_x (x) e_y`, and `H(lambda) = H2 + lambda V`.
  - This is a static weak-field potential proportional to the product of the two walkers' energy densities, with block 53's Green function.
- **Placements (class Pi).**
  - The pull's energy is placed as `v_w = sum_{x,y} G(x-y) omega(w;x,y) e_x (x) e_y`.
  - The weights `omega` are translation-covariant, with `sum_w omega = 1` and `sum_w |w| |omega| < oo`.
  - Their first moment is `c(x,y) = sum_w w omega(w;x,y) = (x+y)/2 + beta (x-y) + rho0(x-y)`, with `beta` real and `sum_r |G(r) rho0(r)| < oo`.
  - For identical records `omega` is symmetric in `(x,y)`, so `beta = 0` and `rho0` is even.
  - The total first moment is `D'(lambda) = D2 + F0 + lambda (F_V + F1) + O(lambda^2)`, where `D2 = D(x)1 + 1(x)D` and `F_V = sum_w w v_w`.
  - `F0` and `F1` are sums of translation-covariant one-body terms of finite range and two-body terms of finite relative range.
  - `F0` must keep the free books: `[H2, J'(0)] = 0`.
- **The books.** `J'(lambda) = i[H(lambda), D'(lambda)]` is kept iff `[H(lambda), J'(lambda)] = 0`.
  - Write `[H(lambda), J'(lambda)] = lambda C1 + O(lambda^2)`.
  - "Kept to first order" means that `C1` has zero matrix elements between finitely supported states.
- **Fibers.** At total wave vector `K`, record 1 carries `k` and record 2 carries `K - k`.
  - The free fiber generator is `h0(K)(k) = h(k)(x)1 + 1(x)h(K-k)`.
  - The total two-step momentum is `g(K,k) = P(k) + P(K-k) = sin K cos(2k - K)`, a scalar on the coins.
  - The forward set is `Fw = {k' = k mod 2pi}`; for identical records it also contains `{k' = K - k}`.

**Claims.**

- **(A) First-order identity.** Take any placement in Pi. On `Fw`'s complement, the fiber kernel of `C1` is a continuous function. At every on-shell, off-forward pair of band states `a` (at `k`) and `b` (at `k'`), with `E_b(k') = E_a(k)`:

  `<b| c1(K; k', k) |a> = (g(K,k) - g(K,k')) <b| v(K; k', k) |a>`.

  This is the same for every placement. So books kept to first order force the on-shell, off-forward Born amplitude of the pull to vanish wherever `g` changes.
- **(W) Witness.** Take `K = (pi/4, pi/4, 3pi/4)` and `k = (0, pi/2, pi/4)`, scattering to `k' = (pi/2, 0, pi/4)`.
  - The pair is on the shell for all four band pairs, and `g` changes by `(1, -1, 0)`.
  - The Born amplitude is nonzero exactly: `|v|^2 = 9/4` for distinguishable records, and a nonzero element of `Q(sqrt2, sqrt3)` in both exchange sectors.
  - A second shell pair, off the `pi/4` grid, also has a nonzero amplitude.
- **(B) Order.** Exact books first fail at first order in the coupling: `C1 != 0` for every placement in Pi, while the zeroth order holds.
- **(T) Finite torus.** On every `L^3` torus with `8 | L`, no operator family `J(lambda) = sum P + lambda J1 + o(lambda)`, local or not, commutes with `H2 + lambda V_L` for all small `lambda`.
- **(S) Conditional, not claimed.** Under stated long-range scattering hypotheses, kept books force the all-orders off-forward on-shell amplitude to vanish almost everywhere. This is the long-range form of block 143 T3.

## 2. Steps

**Step 1. The free current is a scalar. PROVED; CHECKED A1 and A2.**
- The velocity is `i[H, X_a] = cos k_a sigma_a` in symbols, and `(1/2){h, d_a h} = (1/2) d_a (h^2) = sin k_a cos k_a * 1`. This is block 140 T1 in symbols.
- So `i[H2, D2] = P(x)1 + 1(x)P =: sum P`. Its fiber is multiplication by the scalar `g(K,k)`, which commutes with `h0(K)`. Hence `[H2, sum P] = 0`: free records keep the books.
- `P(k) + P(K-k) = sin K cos(2k - K)` holds componentwise (A2).

**Step 2. Lemma L0: keeping the free books forces `i[H2, F0] = 0`. PROVED; CHECKED A3.**
- `[H2, J'(0)] = 0` with `J'(0) = sum P + i[H2, F0]` gives `[H2, [H2, F0]] = 0`.
- **The fiber.** The one-body part of `F0` acts in the fiber by multiplication by `m(k) = f(k)(x)1 + 1(x)f(K-k)`, a matrix of trigonometric polynomials. Its contribution to `[h0,[h0,.]]` is `M(k) delta(k'-k)`. The two-body part has a trigonometric-polynomial kernel `f2(K;k',k)`.
- **Separating the two parts.** A distribution `M delta(k'-k)` that equals minus a continuous function vanishes, and so does the function.
- **The one-body part.** `[h0,[h0,m]] = [h1,[h1,f]](x)1 + 1(x)[h2,[h2,f]]`. Both terms are traceless, so each vanishes.
  - A3 gives `[h.s, [h.s, f.s]] = 4(|h|^2 f - (h.f)h).s`, which is zero iff `f` is parallel to `h`, iff `[h, f] = 0`.
  - The scalar part `f0` of `f` always commutes.
  - So the one-body part of `i[H2, F0]` vanishes.
- **The two-body part.** In band components, `(E_a(k') - E_b(k))^2 f2_ab(k',k) = 0`.
  - For `K` outside `{0,pi}^3`, no band function `E_{s1 s2}(K, .)` is constant on an open set. Each is real-analytic on the connected set of `T^3` minus the cone points. Near a cone point `k0` of record 1 it equals `s1|k - k0|` (to leading order) plus an analytic term, so it is not constant there.
  - Hence `f2(K) = 0` on a dense set, and by continuity everywhere. By continuity in `K`, `f2 = 0`.
- So `J'(0) = sum P` for every placement in Pi.

**Step 3. The pull's Born kernel. PROVED; CHECKED B1.**
- **General form.** Let `A_x` and `B_y` be covariant local one-body operators, with `<k'|A_x|k> = a(k',k) e^{-i(k'-k).x}`. Let `W` be polynomially bounded, and write `What(p) = sum_r W(r) e^{-ip.r}` (a distribution).
  - Then `sum_{x,y} W(x-y) A_x (x) B_y` has kernel `(2pi)^3 delta(K'-K) What(k_1'-k_1) a(k_1',k_1) (x) b(k_2',k_2)`.
  - Proof: put `x = y + r` and sum over `y`.
- **The pull.** For `e_x`, `a = (h(k') + h(k))/2`. So

  `v(K;k',k) = Ghat(k'-k) (h(k')+h(k))/2 (x) (h(K-k')+h(K-k))/2`,

  with `Ghat = 1/Lhat`.
- **Check B1.** It verifies this formula in position space on the `4^3` torus.
  - `G_4` comes from an exact rational solve of block 53's law with a neutral background, so the kernel is not assumed.
  - Five momentum configurations are used: three generic, one forward and one non-conserving. The coin vectors are arbitrary Gaussian-rational vectors.

**Step 4. The first-order current, regrouped. PROVED; CHECKED C1.**
- **The expansion.** `J'(lambda) = sum P + lambda J1 + O(lambda^2)`, with

  `J1 = i[V, D2] + i[H2, F_V] + i[V, F0] + i[H2, F1]`.
- **The first two terms.** With `D2 = sum_z z h0_z`, `h0_z = e_z(x)1 + 1(x)e_z`, `V = sum_w v_w` and `H2 = sum_z h0_z`:

  `i[V, D2] + i[H2, F_V] = sum_{w,z} (z - w) i[v_w, h0_z]`.
- **Regrouping.** Insert `v_w` and use `sum_w (z - w) omega(w;x,y) = z - c(x,y)`, which holds by absolute convergence. The result is

  `J1^V = sum_{x,y} G(x-y) [ j_x(x)e_y + e_x(x)j_y + (x - c) i[e_x,H](x)e_y + (y - c) e_x(x)i[e_y,H] ]`,

  with `j_x = sum_z (z - x) i[e_x, e_z]`, a finite sum.
  - The step uses `sum_z e_z = H` on finitely supported vectors.
  - Here `x - c = (1/2 - beta) r - rho0(r)` and `y - c = -(1/2 + beta) r - rho0(r)`, with `r = x - y`.
- **Check C1.** It verifies the regrouping exactly on an open chain of 5 sites, a `2x3` box and a `2x2x2` box. It uses a generic even kernel and generic placement weights, including weight placed off both records.

**Step 5. Kernels are continuous off the forward set. PROVED. This step handles the forward singularity.**
- **The weights.** Each term of `J1^V` has the form of Step 3 with `W` equal to `G`, `G r_a` or `G rho0_a`. `A` and `B` are drawn from `e`, `j` and `i[e,H]`, whose symbols are trigonometric polynomials.
- **Their transforms.**
  - `1/Lhat` is in `L^1(T^3)` and real-analytic on `T^3 \ {0}`, where `Lhat > 0`.
  - The Fourier series of `G r_a` is `i d_a Ghat` as a distribution. It is real-analytic off `p = 0`, although it is not locally integrable at `0`.
  - The transform of `G rho0` is continuous, since the sum is absolutely convergent.
- **The other terms of `J1`.**
  - `i[V, F0]` has kernel `v(k',k) m(k) - m(k') v(k',k)`, continuous off `Fw` (by Step 2, `F0` is one-body).
  - `i[H2, F1]` has a one-body part supported on `k' = k` and a continuous finite-range part.
- **The pull.** `V`'s own kernel is singular only at `k' = k mod 2pi` (and at the exchange-forward points for identical records).
- **Conclusion.** Every kernel entering `C1` is a distribution that restricts to a continuous function of `(K, k', k)` off `Fw`.
- **Well-definedness.** The matrix elements of `C1` between finitely supported states are finite sums, and their Fourier series is this kernel. No boundedness is needed for (A).

**Step 6. The on-shell identity (A). PROVED.**
- In the fiber, `C1 = [h0, j1] + [v, g]`. Off `Fw` its kernel is

  `c1(k',k) = h0(k') j1(k',k) - j1(k',k) h0(k) + (g(k) - g(k')) v(k',k)`.
- Sandwich it between band eigenvectors `b` at `k'` and `a` at `k`. The first two terms give `(E_b(k') - E_a(k)) <b|j1|a>`, which is `0` on the shell because `j1` is finite there (Step 5). This leaves (A).
- **Books kept to first order.** Then `c1 = 0` as a distribution. Being continuous off `Fw`, it vanishes pointwise there. So `(g(k) - g(k')) <b|v|a> = 0` at every on-shell, off-forward pair.
- **Identical records.** Sandwich with exchange-symmetrized states. The four kernel values involved, at `(k',k)`, `(k',K-k)`, `(K-k',k)` and `(K-k',K-k)`, are all off `Fw` at the witness. Also `g(k) = g(K-k)`.
- **The forward direction.** Nothing here asks the forward singularity of `Ghat` or `d Ghat` to be integrable. The argument is pointwise off `Fw`.

**Step 7. The witness. CHECKED D1, E1, E2 and E3.**
- **Kinematics.**
  - Initial pair: `k = (0, pi/2, pi/4)`, `K - k = (pi/4, -pi/4, pi/2)`.
  - Final pair: `k' = (pi/2, 0, pi/4)`, `K - k' = (-pi/4, pi/4, pi/2)`. Axes 1 and 2 are swapped, which is allowed because `K_1 = K_2`.
  - `eps^2 = 3/2` and `2` are kept, so all four band energies agree, and they are distinct.
  - `g` goes from `(1/2, -1/2, 1/2)` to `(-1/2, 1/2, 1/2)`.
  - The direct transfer is `(pi/2, -pi/2, 0)`, with `Ghat = 3/2`. The exchange transfer is `(pi/4, pi/4, -pi/4)`, with `Ghat = 2 + sqrt2`. No transfer is `0 mod 2pi`.
- **The distinguishable modulus.**
  - For `eps(k') = eps(k) = eps`, `<u_s(k')|(h(k')+h(k))/2|u_s(k)> = s eps <u_s(k')|u_s(k)>`.
  - Also `|<u_s(k')|u_s(k)>|^2 = Tr(Pi_s(k') Pi_s(k)) = (1 + n.n')/2`, with `n = sin k / eps`.
  - Hence `|v|^2 = Ghat^2 eps^2 (1+n.n')/2 eps~^2 (1+m.m')/2`, which is `9/4` here, independent of the band pair.
- **Exchange sectors (E1).** `|v_dir +- v_ex|^2` is computed from gauge-invariant projector traces. Each value lies in `Q(sqrt2, sqrt3)` and has a nonzero rational Galois norm, so it is nonzero. The values are about 45.42 and 17.37 for band pairs `(+,+)`/`(-,-)`, and about 2.243 and 2.257 for `(+,-)`/`(-,+)`, in the symmetric and antisymmetric sectors respectively.
- **Independent cross-check.** A floating computation with explicit eigenvectors, not part of the checker, reproduces all of these values.
- **The defect (E2).** `<f|C1_a|i> = (g_a(i) - g_a(f)) <f|V|i>` is nonzero for `a = 1, 2`.
- **An off-grid witness (E3).**
  - `sin` and `cos` of `k` are `(3/5, 4/5)`, `(5/13, 12/13)` and `(20/29, 21/29)`; those of `K_1 = K_2` are `(8/17, 15/17)`, and those of `K_3` are `(7/25, 24/25)`.
  - With axes 1 and 2 swapped, `g_1 - g_2 = -147456/1221025` and `|v|^2 > 0`, an exact rational.

**Step 8. The order at which exact books first fail (B). PROVED.**
- Steps 6 and 7 give `C1 != 0` for every placement in Pi, and Step 1 gives the zeroth order. So exact books first fail at first order in `lambda`.
- On the energy shell the defect is not an artefact of the placement: it equals `(g(k) - g(k'))` times the Born amplitude.
- By continuity it is nonzero on an open set of shell pairs around the witness.
- **Small couplings.** Suppose `J'(lambda) - sum P - lambda J1 = O(lambda^2)` in operator norm. Then `||[H(lambda), J'(lambda)]|| >= |lambda| ||C1|| - O(lambda^2) > 0` for `0 < |lambda| < lambda0`.
  - This holds for placements linear in `lambda`, given the standard bound `|G(r)| <= C/(1+|r|)` for block 53's decaying inverse (ASSUMED, not re-proved) and bounded `rho0`.
  - Under that bound, `V`, `J1` and `C1` are bounded: each term is a finite sum of (bounded) times `M_W` times (bounded), with `W` bounded.
  - `i[V, F_V]` is bounded because it equals `(1/2) sum G G' (c' - c) [E_xy, E_x'y']` and only nearby pairs contribute.
- **Remark on orders.** `V` is quadratic in the member-record vertex (source to clock to source). So "first order in `lambda`" is the first order at which one record's pull acts back on the other.

**Step 9. The finite torus (T). PROVED; CHECKED D1 and B1.**
- **The same numbers.** On the `L^3` torus with `8 | L`, the witness momenta are grid points. Step 3's computation holds on every torus, with `Ghat_L(p) = 1/Lhat(p)` for `p != 0` (B1 checks it at `L = 4`). So E1's amplitudes are the torus amplitudes, up to the normalization `1/L^3`.
- **The free current.** Let `J(lambda)` be any family with `[H2, J(0)] = 0`, `J(0) = sum P + i[H2, F]` and `J(lambda) = J(0) + lambda J1 + o(lambda)`.
  - In finite dimension, `[H2,[H2,F]] = 0` makes `[H2, F]` block-diagonal. Its diagonal blocks `P_E [H2, F] P_E` vanish, so `[H2, F] = 0` and `J(0) = sum P`.
- **The obstruction.** `P_E [H(lambda), J(lambda)] P_E = lambda P_E [V, sum P] P_E + o(lambda)`, and `<f|[V, sum P_1]|i> = (g_1(i) - g_1(f)) <f|V_L|i> != 0`. So the commutator is nonzero for every small `lambda != 0`, whatever `J1` is. No locality is used.

**Step 10. The all-orders form (S). CONDITIONAL; hypotheses H1-H3 ASSUMED, not proved.**
- **Hypotheses.**
  - (H1) Modified wave operators `Omega+-(K) = s-lim e^{i h'(K) t} e^{-i h0(K) t - i Phi_K(t)}` exist and are complete. Here `Phi_K(t)` is a multiplication operator in the band basis.
  - (H2) Along the modified free motion, the non-free part `j'(K) - g` has vanishing Cesaro means on a dense set of absolutely continuous states.
  - (H3) Off `Fw`, `S(K) - 1` acts on each shell by a locally integrable kernel `t_E`.
- **The implication.** Given these, block 143 T3's steps 3-5 go through: `Phi` commutes with the scalar `g`. So `[H', J'] = 0` gives `S* g S = g`, and `t_E(w',w)(g(w') - g(w)) = 0` for almost every off-forward shell pair.
- **What is not needed.** No analyticity step is needed for the off-forward conclusion. The forward part, a phase from `Phi`, is not constrained.

**Remarks.**
- **R1. Block 143's own finite-range setting.** Steps 5 and 6 use only continuity off `Fw`. For a finite-range `W` on the full two-record space, books kept to first order force the on-shell Born amplitude of `W` to commute with `g`, with none of block 143's analytic bridge. Exclusion is not a small perturbation and is not covered.
- **R2. Placements outside Pi.**
  - Step 6 does not cover a first-order current whose kernel is singular across the shell, such as a principal-value `(g(k')-g(k)) v/(E(k')-E(k))`.
  - Whether such an operator is bounded, and whether it arises from any density, is not decided here.
  - Step 9 shows that no such escape exists in finite volume.
- **R3. `Z^2`.** Block 53's law is cubic. On `Z^2` the decaying inverse does not exist and the pull grows like `log r`, so nothing is claimed there.
- **R4. Placing the energy in the clock field.** Placing the pull's energy in the clock field's bond energy gives, by the point reflection `z -> x + y - z`, the first moment `(x+y)/2` under symmetric summation. That sum is not absolutely convergent, so this placement is noted, not claimed inside Pi.
- **R5. The member's exchange.** The retarded exchange at the closing ratio is not treated. The static clock-law pull is the task's first option.

## 3. First unresolved step

The first unresolved step is the all-orders statement (S): hypotheses H1-H3 for the matrix-valued walk with a `1/|r|` tail.

The subtle input is H2. `J1^V` carries the weight `G(r) r/2`, which does not decay pointwise. It decays like `1/|r|` only after a summation by parts, using `sum_x i[e_x, H] = 0`. So its Cesaro decay along separating motion needs a minimal-velocity estimate that is not given here.

The first-order results (A), (W), (B) and (T) do not depend on H1-H3.

## 4. What would finish it

1. Modified wave operators (H1) for `h0(K) + lambda v(K)`, with a Dollard phase built from the pull's `1/|r|` tail. This needs threshold and cone control of the kind block 143 lists as open.
2. H2: a minimal-velocity bound for the free walkers away from band stationary points (block 143 T6 supplies nondegenerate stationary points at one `K`). With it, the summation-by-parts decay of the `G(r) r` term follows.
3. An order-by-order link, `t_E = lambda v_on-shell + O(lambda^2)` off forward. It would turn (B) into "books fail for every small coupling" at the level of the scattering operator.
4. The same first-order computation for the member's retarded exchange at the closing ratio, with the field's own energy current in the books.
5. A decision on nonlocal first-order currents (R2) in infinite volume.
