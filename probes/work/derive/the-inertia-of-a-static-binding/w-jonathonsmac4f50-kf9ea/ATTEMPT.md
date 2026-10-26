# Attempt a1: the inertia of a static binding (massive records, one record per site)

Worker: Claude Sonnet 5.5, same model family as the lane that supplied the models. Unrefereed. Nothing here is adopted.
Task id: `J:derive:the-inertia-of-a-static-binding:a1`. Companion runner: `check.py` (same folder).

**Sources read before concluding.** I read `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (233 lines) and
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` in full (130 lines) on current main. The registry lists three primitives
(`scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`); none is used. I read the four notes named in the task as landed on main
(blocks 115, 133, 139, 142 are all on main; their PRs show CLOSED), and block 144 (landed), for prior art.

## 0. Plain-language summary

Two heavy "records" (each with the staggered rest energy `m eps`), kept off the same site, are pulled together by a fixed attractive
term that acts only when they sit two sites apart. When the pull is only just strong enough to bind them, the pair is huge and loose.

- The pair's weight `W = E0 d^2E/dK^2` (rest energy times its curvature in total momentum; a free record has `W = 1`) tends to 1 at the binding threshold.
  I computed it exactly. The shortfall is `1 - W = alpha(m) * delta`, where `delta` is the pair's inverse size (the decay per two sites of the wave function) and
  `alpha(m) = (16 m^2 + 3 - sqrt(1 + 64 m^4)) / (8 m^2)`, which is always above 1.
- That is **first order in the inverse size**. The binding fraction (energy lost to binding over total energy) is only `delta^2/(8 m^2)`, second order. So the
  "static binding does not carry its inertia" shortfall is not the binding fraction here; it is a threshold effect: **the coupling at which a pair first binds
  itself depends on the pair's total momentum**. The supervisor's formula `W - 1 = -(T - U/2)/m` is also first order in `delta` (near threshold `T = -U`), but its coefficient
  differs from the exact one by a finite, m-dependent factor `R(m)` (21.9 at m = 4, 1.45 at 0.8, 0.373 at 0.1, tending to 1/3 as m tends to 0). Neither limit "static formula" nor "zero" is right.
- A binding strength that depends on the pair's total momentum, `V(K) = V0 (1 + lambda K^2/2)`, shifts `W` by exactly `lambda E0 <U>`. It removes the leading shortfall only
  if `lambda = lambda*(m)`, a number of order one (about -1 for heavy records, about -28 at m = 0.1), not a small correction; a fixed `lambda*` leaves `W - 1 = c2(m) delta^2 > 0`,
  larger than the mass defect. So no fixed coefficient makes `W = 1` beyond leading order.
- An attractive term acting only when the records are neighbours binds **no** pair at rest, for any strength and any m (exact).
- Not done: `Z^3`.

## 1. The exact statement attempted

Setting S (all of it supplied; see section 2). Line `Z`, two records with single-record generator `h = s S + m eps`, where `S = (T - T^{-1})/(2i)`
(`(T psi)(x) = psi(x-1)`), `eps(x) = (-1)^x`, coin `s = +-1` conserved; exclusion `x1 != x2`; static coin-blind term `V` (V < 0) acting when `|x1 - x2| = d`, `d = 2` (two-step) or `d = 1` (neighbour).
For the pair sector of total momentum `K` (conjugate to the centre-of-mass translation by one site; sectors are `pi`-periodic) let `E(K)` be the bound level near `2m`, and `W = E(0) E''(0)`.
A free record has `W = 1`; two free records at threshold have `W = 1` (E_thr(K) = 2 sqrt(m^2 + sin^2(K/2)), step S7).

Claims attempted:
- (a) exact `W`, and its behaviour as the pair loosens to the binding threshold; compare with the static formula and with 0;
- (b) split the lattice/size part from the binding-fraction part;
- (c) decide whether a motion-dependent binding term makes `W = 1` at leading order.

## 2. Premises: what the axioms say, what was supplied, what was proved

- **Axioms say** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): "A site never carries more than one record" (lines 79-80), which I use as the hard-core exclusion
  `x1 != x2` in the two-record space; "No site is privileged" / "No possibility is privileged" (lines 37-41, 50-51); and "Admissibility is not a dynamics axiom" (lines 114-123): no
  Hamiltonian, no mass, no pair interaction is given by the axioms.
- **Supplied by lanes** (not by the axioms): the walker `H = sigma_z D` (block 54 as quoted in the landed blocks, e.g. block 115 premises), the staggered rest energy `m eps`
  (block 77; `(H + m eps)^2 = H^2 + m^2`, block 139 `docs/ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_...2026-09-25.md:102-104`), the two-record tensor-product space, the static
  coin-blind term `V` at separation `d`, the total-momentum fibre decomposition, and the definition `W = E0 E''(0)`.
  The word "weak" in the task: my `V` is weak only in the sense of being near the binding threshold; `|V_c(m)|` is not small (about 1/(4m) for heavy records, about 1/(2m) = 5 at m = 0.1).
- **Proved or checked here:** everything in section 3.
- **Standard import (ASSUMED, also cross-checked):** second-order Rayleigh-Schroedinger perturbation theory for an isolated simple eigenvalue of a norm-analytic family of bounded
  self-adjoint operators (Kato). Cross-checks: exact finite-chain identity (check P5) and the independent determinant method (check P9).

## 3. Numbered steps

**S1 [PROVED; CHECKED P1, P1b].** Fibre reduction. Write `psi(x1,x2) = i^{x1+x2} q^{x1+x2} u(x1 - x2, x1 mod 2)`, `q = e^{iK/2}`. The pair generator becomes the fibre operator on `u(r,p)`, `r >= 1`, `p in {0,1}`:
`(H(K)u)(r,p) = -(1/2)[q u(r+1,1-p) + q^{-1} u(r-1,1-p) + q u(r-1,p) + q^{-1} u(r+1,p)] + m(-1)^p (1+(-1)^r) u(r,p) + V delta_{r,d} u(r,p)`.
check.py P1 verifies this as a symbolic identity on the infinite line (symbolic `u`, `q`, `m`, `V`, windows `r = 1..7`). For opposite coins the gauge `i^{x1}(-i)^{x2}` gives the same operator (P1b); for `(-,-)` the generator is the complex conjugate of `(+,+)`, so spectra agree. Hence the coin pattern does not change `E(K)` or `W`.

**S2 [PROVED].** Exclusion on a line preserves the order of the records (a nearest-neighbour hop changes `r` by one and `r = 0` is removed), so `r >= 1` and `r <= -1` decouple and are exchange images; boson/fermion exchange sign is irrelevant. Only the half-line `r >= 1` remains.

**S3 [PROVED; CHECKED P2].** With `w+- = u(.,0) +- u(.,1)`: chain A (`w+`) has hop `-cos(K/2)`; chain B (`w-`) has hop `+i sin(K/2)` forward, `-i sin(K/2)` back; they are coupled by `m(1+(-1)^r)`, i.e. `2m` on even `r`, nothing on odd `r`; `V` acts on both at `r = d`. (Even `r`, `p = 0` is the (+,+) pair at energy about 2m; `p = 1` is the (-,-) pair at about -2m.)

**S4 [PROVED; CHECKED P3, P4, P6].** At `K = 0`, `w-` has no hop; eliminating it gives a scalar half-line chain (hop -1) with energy-dependent on-site term `4m^2/(E - V delta_{r,2})` on even sites. The bound state (d = 2) is: `w+(1) = -1/E`, `w+(2) = 1`, `w+(2j) = z^{j-1}`, `w+(2j+1) = c z^{j-1}`, `c = -(1+z)/E`, `w-(2) = 2m/t`, `w-(2j) = 2m z^{j-1}/E` (j >= 2), `w-(odd) = 0`, with `t = E - V` and
- `R1: (1+z)^2 = z (E^2 - 4m^2)` (bulk decay `z in (-1,0)`),
- `R2: E t^2 - (2+z) t - 4 m^2 E = 0` (boundary condition at r = 2; `t > 0`).
P3 verifies all eigen-equations at `r = 1..8` and generic `j` modulo `(R1, R2)` (Groebner reduction). Threshold `z = -1`, `E = 2m` is bounded iff `V = V_c(m) = (8m^2 - 1 - sqrt(1 + 64 m^4))/(4m)` (P4a-c). The (+,+) continuum edge at total momentum `K` is `E_thr(K) = 2 sqrt(m^2 + sin^2(K/2))` (bulk quadratic at `z = -1`, P4d), so `E_thr''(0) = 1/(2m)`.

**S5 [PROVED given the standard import; CHECKED P5, P6, P9].** `H(K) = H0 + K H1 + K^2 H2 + O(K^3)` with `H1 = (i/2)` (B-chain antisymmetric hop) and `H2 = (1/8)` (A-chain hop). `H1 psi0` lives on B-chain odd sites, where `H0` has no coupling and energy 0, so `(E0 - H0)^{-1} H1 psi0 = H1 psi0 / E0`. Therefore
`E''(0) = 2[<H2> + |H1 psi0|^2 / E0] / <psi0|psi0>` and, with the geometric sums of `psi0` (P6),
**`W = (E0 S1 + Q) / (2 N)`** with `N = sum (w+^2 + w-^2)`, `S1 = sum_r w+(r) w+(r+1)`, `Q = sum_j (w-(2j) - w-(2j-2))^2`, all closed form in `(z, E, t, m)`. Checks: the structural identity is verified exactly on finite chains N = 4, 5, 6 (P5); the closed form agrees with an independent decaying-mode determinant `F(E,K)` fitted in `K` to 40 digits (differences below 1e-15, P9a, P9c) and reproduces the supervisor's four floats 0.117, 0.201, 0.411, 0.539 (P9b); a 1200-site float diagonalisation selects the same bound state (P10a).

**S6 [CHECKED exact; P7].** Along the branch `z = -1 + delta` (implicit differentiation of R1, R2, exact sympy):
`W = 1 - alpha(m) delta + O(delta^2)`, `alpha(m) = (16 m^2 + 3 - s)/(8 m^2)`, `s = sqrt(1 + 64 m^4)`, `alpha > 1` for all `m > 0`, `alpha -> 1` (m -> infinity), `alpha = 1/(4 m^2) + 2 + ...` (m -> 0);
`2m - E0 = delta^2/(4m) + O(delta^3)` (binding fraction `delta^2/(8 m^2)`);
`dV/dz < 0`, so `delta -> 0+` as `V -> V_c^-`;
`<U> = u1(m) delta + O(delta^2)`, `u1 = V_c (1 + 4 m^2/t_c^2) = -(-64 m^4 + 8 m^2 s + s - 1)/(16 m^3) < 0`.
Numbers (alpha, R, lambda*, V_c): m = 4: 1.0234, 21.92, -1.027, -0.0627; m = 0.8: 1.5670, 1.453, -1.703, -0.3427; m = 0.1: 26.96, 0.3732, -27.99, -4.808.

**S7 [PROVED; algebra].** With `eps_b(K) = E_thr(K) - E(K)`: `W = E0 E''`, `E0 = 2m - eps_b(0)`, `E'' = 1/(2m) - eps_b''(0)`, so
`W = 1 - eps_b/(2m) - (2m - eps_b) eps_b''(0)`.
First term: the mass defect, `delta^2/(8 m^2)`. Second term: how the binding energy changes with the pair's total momentum; it carries the whole `O(delta)` shortfall.

**S8 [CHECKED, NUMERIC; P9f].** Mechanism. The critical coupling at total momentum `K`, `V_c(K)`, decreases in magnitude with `K`; `alpha(m) = V_c''(0)/|dV/ddelta|` to 1e-8 at m = 4, 0.8. So the leading shortfall is the `K`-dependence of the threshold, a property of the zero-energy resonance in the core, not of the bound state's tail.

**S9 [PROVED; CHECKED P7j-n, P11].** (c), motion-dependent binding. Let `V(K) = V0(1 + lambda K^2/2 + ...)` (a function of the pair's total momentum, which is conserved). Hellmann-Feynman in `V` gives `dE0/dV = <P_{r=2}>`, hence **`W(lambda) = W0 + lambda E0 <U>` exactly**.
- `W = 1` at `O(delta)` iff `lambda = lambda*(m) = alpha/(2 m u1) < 0`; `lambda* -> -1` as `m -> infinity` (this is `V cos K`, the lattice pair-translation) and `lambda*(0.1) = -28`. These are O(1), not suppressed by the binding fraction.
- With `lambda = lambda*(m)` fixed: `W - 1 = c2(m) delta^2 + O(delta^3)`, `c2 > 0` in closed form (P7k, P7l); `c2 * 8 m^2` (residual over the mass-defect coefficient) is 66.5, 5.01, 2.27 at m = 4, 0.8, 0.1 (P7m). So the residual is of the order of the binding fraction but is larger than the mass defect.
- Interval arithmetic (P11): `lambda*(delta)` has disjoint enclosures at `delta = 0.01` and `0.001`, so no single `lambda` gives `W = 1` at all binding strengths.
- Adding a second core term (P_4) can remove the `O(delta^2)` residual because `p_4/p_2` has a nonzero derivative (closed form, P7n). **Suggested, not checked:** finitely many core terms give `W = 1` to finite order only.

**S10 [PROVED; CHECKED P8, P10b].** Neighbour term (`d = 1`) at `K = 0`: the matching condition is `V = E/(1+z)` exactly. For a decaying real solution (`|z| < 1`) and `E > 0` this gives `V > 0`. So an attractive neighbour term has no `K = 0` level with `0 < E < 2m`, any `|V|`, any `m`. (Physical reason, reading: records at rest sit on one sublattice, so the neighbour term acts on the energy-zero sector; block 133 T1 `...A_MASSIVE_BODY...2026-09-24.md:52`.) Levels with `E < 0` are not rest pairs of positive-energy records and are not claimed.

**S11 [NOT DONE].** `Z^3`. Reading (suggested, unchecked): the same mechanism should apply, because a near-critical s-wave state of the relative motion has norm `~ 1/kappa` and core weight `~ kappa`, so the core contribution to `E''` and `<U>`, `<T>` is linear in the inverse size; the coefficient needs the 3D lattice threshold state.

## 4. Answers

**(a) [exact on the line, d = 2].** `W -> 1` at threshold. `1 - W = alpha(m) delta + O(delta^2)` with `alpha(m) > 1`. The static-formula deficit `(T - U/2)/m` (actual lattice `<T>`, `<U>`, `T = -U + O(delta^2)`) is also `~ delta`, with coefficient `-(3/2) u1/m`, and the ratio `R(m) = alpha m /(-(3/2) u1)` is `21.9, 1.45, 0.373` at `m = 4, 0.8, 0.1`; `R -> 1/3` (m -> 0), `R ~ 4 m^2/3` (m -> infinity). The deficit is neither the static value nor zero: it is first order in the inverse size with an exactly known coefficient.
**(b)** There is no regime where the binding-fraction part dominates: at fixed `m` the mass defect `delta^2/(8 m^2)` is smaller than the shortfall `alpha delta` by the factor `delta/(8 m^2 alpha)`, and `1/(8 m^2 alpha) -> 1/2` as `m -> 0`, so the ratio is below `delta/2 < 1/2` at all `m`. The task's regime note (binding-fraction part dominating for `m << 1`) is not borne out near threshold. Lattice part: `alpha(infinity) = 1` (pure two-sublattice hopping, exclusion at the wall). The remainder `r(m) = (8 m^2 + 3 - s)/(8 m^2)` (= `3/(8 m^2)` at large `m`, `1/(4 m^2) + 1` at small `m`) is the non-covariance of the instantaneous term with relativistic constituents. This split is a READING; only `alpha(m)` and the mass-defect term are proved.
**(c) [settled for the class `V(K)`].** See S9. Yes at leading order in the inverse size, with an O(1) coefficient; not at leading order in the binding fraction with a small term; no fixed coefficient for all binding strengths. Continuum comparison (landed): `docs/ADMISSIBILITY_RULE_THE_MEMBERS_PULL_CARRIES_THE_VELOCITY_TERMS_THAT_GIVE_PULL_BOUND_PAIRS_WEIGHT_ONE_ALONG_EVERY_AXIS_AT_FIRST_ORDER_BOUNDED_THEOREM_NOTE_2026-09-25.md:39-43` has the same structure for smooth weak binding: `W = 1 + [(1+2(2a+b))<U> + (1+2c)<U_P>]/M`, and `W = 1` needs `2a + b = -1/2`, `c = -1/2`, also O(1). That note excludes lattice results and near-threshold singular cores.

## 5. What is new, and what is not

- **Not new:** the supervisor's floats (reproduced, check P9b); second-order perturbation theory; the formula `W = 1 + <U>/(2m) - <T>/m` and its role (block 144 T4(a): `...VELOCITY_TERMS...:111-118`); the massless line law `E = V + sin^2(K/2)/V`, `c^2 = 1/2` (block 142 T1, `...PAIRS_BOUND_AS_NEIGHBOURS...:51-69`); contact binding (block 115 T1-T4, `...A_REST_ENERGY_FROM_BINDING...:29-66`).
- **New (as far as my search of main and the probes view found; no landed note computes a massive pair's weight or a threshold):** the exact fibre of the massive pair and the K = 0 scalar chain; closed-form `W`; `V_c(m)`; `alpha(m)`, `u1(m)`, `R(m)`; the identity of S7 with the mechanism S8; the exact tuning shift `lambda E0 <U>` and `lambda*(m)`, `c2(m)`; the neighbour-term no-bound-state result.
- **Overlap:** no open PR searched (`gh pr list --search "binding inertia static"`: none). Blocks 115, 133, 139, 142 themselves are on main as landed notes; I used the landed text.
- **Provenance:** one worker, same family as the lane, no other family has read it.

## 6. First unresolved step and what would finish it

- First unresolved step: **S11, `Z^3`**. The task asked for the line and `Z^3`; only the line is done.
- Not claimed: results for `d = 1` at `K != 0`; any statement for deep, wide wells (binding fraction not small); excited bound states; massless limit (the model needs `m > 0` for isolation of `E0` from the mixed continuum).
- To finish `Z^3`: build the 3D fibre (8 components per relative site: 4 coin pairs times 2 sublattice parities), solve the K = 0 threshold state (the s-wave lattice resonance at `V_c`) by the 3D lattice Green's function, and evaluate the same Hellmann-Feynman expression; check `1 - W = alpha_3(m) delta` and whether the critical coupling's `K`-dependence is the mechanism.
- To close (c): decide whether a finite family of local, K-quadratic core terms gives `W = 1` to all orders in `delta` (the first two orders need two terms; infinitely many orders may need infinitely many).

## 7. Files

- `ATTEMPT.md` (this file).
- `check.py`: runs in about 1.5 minutes unloaded (214 s measured on a loaded machine), about 270 MB peak, one process, no network. It prints PASS/FAIL lines, `TOTAL`, `SUMMARY`, `HIT`.
- `explore/` holds my scratch scripts and logs (not part of the deliverable).
