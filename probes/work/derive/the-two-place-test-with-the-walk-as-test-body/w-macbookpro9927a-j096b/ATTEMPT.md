# Block 116's two-place test with block 54's walk as the test body

Task `J:derive:the-two-place-test-with-the-walk-as-test-body:a2`, worker `w-macbookpro9927a-j096b`, model claude-opus-5-5.
Checker: `check.py` in this directory, about 45 s single-threaded, with peak memory of about 0.5 GB. It reports `TOTAL: PASS=7 FAIL=0`.
- The block-116 field and witness are checked in exact rational arithmetic.
- The walk numbers are labelled floating point. Each is produced two independent ways, and the checks assert that they agree.

**Sources.** Read as landed on `origin/main` at `25b8c1874f2ea657653dbb298bf383c18d81e0b5`:
- block 116 (`ADMISSIBILITY_RULE_FORMING_ONE_RECORD_KEEPS_THE_LEDGER_ONLY_AT_A_PRICE_...`; PR #9159 is closed and the note is on main);
- block 54 (`ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_...`).

Block 54's landed wording controls. T3 is a finite-power identity and T4 a conditional ray model, and neither is used here. Only T1's walk and T2's canonical site-timed evolution enter. Blocks 55 and 56 enter through block 116's premises as landed:
- the static law `((1 - A) + kK) psi = k e` with `psi = 1 - phi` held at zero on the wall;
- the ledger `<chi|phi H phi|chi> + F`.

**Disclosure.** Block 116 T4's discriminator harvests my earlier attempt #8748 (`sources-under-the-record-reading`, a4). Block 116 also harvests #8653. This attempt runs that test with a concrete test body, so it is not independent of where the discriminator came from. There are no earlier attempts on this problem.

## 1. Statement attempted

**Setting (supplied clauses; nothing adopted, no gravitational claim).**
- **The source (block 116 T4).** `B` has energy `E_B` and is at rest. Unformed, it has weights `p_L + p_R = 1` at `L = (0,-2,0)` and `R = (0,2,0)`. Formed, it is one record at `L` or at `R`.
- **The four fields at first order in `k`.** Per unit `k E_B`, they are:
  - `g_L = g(., L)`;
  - `g_R = g(., R)`;
  - `p_L g_L + p_R g_R` (unformed `B`, amplitude sourcing);
  - `0` (unformed `B`, records only).

  Here `g = (1 - A)^{-1}` inside the held box, with zero wall values.
- **The test body (block 54 T1 and T2).** The walk is `H = sum_a sigma_a D_a`, with `D_a = (i/2)(T_a - T_a^dag)` and `(T_a psi)(x) = psi(x - e_a)`.
  - It is site-timed by `W = phi^2`. In the canonical variable `chi = W^{-1/2} psi` it evolves by `i dchi/dt = phi H phi chi`.
  - It is light (condition 3: its own source is dropped), and the field is static during the passage (condition 4).
- **The held box.** The side `n` is odd and the wall layer has `phi = 1`. The walk lives on all `n^3` sites, and hops leaving the box are dropped.
- **The packet (supplied).** Its amplitude is `exp(-s^2 |k - k0|^2) P_+(k) u0`, with `k0 = (pi/4, 0, 0)` and `u0 = (1,1)/sqrt2`. `P_+(k)` projects onto the positive band of `h(k) = sum sin k_a sigma_a`.
  - It is centred at `(-10, -1, 0)` with `s = 2.5`, and moves along block 116's line `(x, -1, 0)`.
  - It is read at `t_f = 20/cos(pi/4) = 20 sqrt2`.

**Claims.**
- **(a) The kicks.** At first order in `k`, the transverse displacement is `dY = k E_B kappa_walk(g)`, with `kappa_walk` a linear functional. So the four kicks are `dY_L`, `dY_R`, `p_L dY_L + p_R dY_R` and `0`, which is block 116 T4(a) with `kappa = kappa_walk`.
  - In the held box of side 61, `dY_L = -0.845766` and `dY_R = +2.192564` per `k E_B`.
  - The walk's own transverse spread at `t_f` is `sigma_Y = 7.393`.
  - In block 116's own box of side 9 the walk makes no clean passage.
- **(b) Two named record rules for the test body, and the resulting distributions.**
  - **R1:** one record forms at `t_f`, at site `x`, with weight `|chi(x, t_f)|^2`. The recorded `y` is distributed as `P_v = P0 + k E_B rho_v + O(k^2)`.
  - **R2:** one record forms at the site nearest the packet's mean position.
- **(c) Resolution.** At the walk's own spread, no single passage resolves the four readings.
  - **Under R1**, every pair of readings separates at every `p_L`. The number of passages needed is `N (k E_B)^2 = c / J`, with `c` between `4 ln(1/(4 eps(1-eps)))` and `8 ln(1/(2 eps))` for error `eps` (for `eps = 0.01`, between 12.9 and 31.3), and `J` between `0.11` and `0.98`.
  - For the pair "mean" against "0", `J = 0.515`, so it takes 25 to 61 passages per `(k E_B)^2` at `eps = 0.01`.
  - The sample mean alone is blind at `p_L* = 0.7216`.
  - **Under R2**, the readings never separate for `k E_B < 0.134`.

## 2. Steps

**Step 1. The first-order generator. PROVED.**
- `phi H phi = (1 - kE_B g) H (1 - kE_B g) = H - kE_B (gH + Hg) + O(k^2)`.
- So `V = -(gH + Hg)` per unit `k E_B`. It is Hermitian and linear in `g`.

**Step 2. The kick is a linear functional of the field. PROVED.**
- **Duhamel.** `chi_k(t) = chi(t) + kE_B eta(t) + O(k^2)`, with `eta(t) = -i int_0^t e^{-iH(t-s)} V e^{-iHs} chi_0 ds`.
  - Equivalently, `i d/dt (chi, eta) = [[H, 0], [V, H]] (chi, eta)` with `eta(0) = 0`.
- **The displacement.** Then `dY = 2 Re <chi(t_f)| Y |eta(t_f)>`. Since `eta` is linear in `V`, which is linear in `g`, `dY` is linear in the field.
- **The four kicks.** They are therefore `dY_L`, `dY_R`, `p_L dY_L + p_R dY_R` and `0`.
  - The mixture's value follows from linearity with no numerics.
  - This is block 116 T4(a) with the abstract `kappa` replaced by the walk's `kappa_walk`.
- **Check.** W3 confirms linearity numerically, to `1e-10`, for `p_L = 1/3`.

**Step 3. The field and block 116's witness. CHECKED X1, exactly.**
- In the box of side 9 I solve `(1 - A) g = delta_L` over the rationals by banded elimination. The residual is verified exactly.
- Block 116 T4(c)'s gradient functional then reproduces `-0.967409...`, `0.201858...`, `-0.382775...` and `-0.187897...`.
- This fixes the geometry and the field conventions.

**Step 4. The walk. CHECKED W1.**
- `H = H^dag` exactly.
- On a plane wave, at interior sites, `H` acts as `sum_a sin k_a sigma_a`.

**Step 5. Block 116's own box has no clean passage. CHECKED W2.**
- In the box of side 9, a positive-band packet with `s = 1` starting at `(-3, -1, 0)` is read at `t_f = 6/cos(pi/4)`.
- The kicks are `dY_L = -0.626108` and `dY_R = 0.427850`. The augmented system and an exact-in-`t` eigendecomposition formula agree to `1e-10`.
- But at `t_f` the packet has `<X> = 0.57`, not `+3`, and `sigma_Y = 2.68` against a half-width of 4. The massless walk fills that box.
- So the test needs a larger held box.

**Step 6. A clean passage in a large held box. CHECKED W3 and W4; controlled floating point.**
- **The field.** In the box of side 61, conjugate gradients reach a residual of `1e-14`.
- **The kicks.** `dY_L = -0.845766` and `dY_R = +2.192564` per `k E_B`. The augmented system and a symmetric finite difference in `k` (step `1e-6`) agree to `1e-7`.
- **The packet at `t_f`.** `<X> = 8.06`, `sigma_Y = 7.393`, and the weight within 3 sites of a wall is `3.5e-4`.
- **The longitudinal delay.** `dX_L = -3.253` and `dX_R = -2.979`: the packet is slowed.
- **Box dependence (W4).** In the box of side 41 the same packet gives `-0.817530` and `2.154261`, 3.3% away, with 6.4% of its weight near the walls.
- **Comparison with block 116's gradient functional.** In the box of side 61 that functional gives `-1.0520` and `0.2644`. The walk's kick is a different functional: its packet is wider than the source separation, so the farther source `R` dominates.

**Step 7. Rule R1 and its distributions. PROVED; CHECKED R1.**
- **The distribution.** `P_v(y) = sum_{x,z} |chi_v(t_f)|^2`. At first order it is `P0 + kE_B rho_v`, with `rho_v = 2 Re sum_{x,z,coin} chi^* eta_v`.
  - `rho_mean = p_L rho_L + p_R rho_R` and `rho_0 = 0`.
  - `sum_y rho_v = 0`, since the norm is kept. `sum_y y rho_v = dY_v`, so the mean shift is the kick. Both are checked.
- **The rule itself.** R1's weights `|chi|^2` are a supplied record clause for this test, as the task suggests. They are not derived or adopted.

**Step 8. How many passages. PROVED; standard inequalities, re-proved.**
- Take `N` independent passages and the Bayes test between readings `v` and `w`, with equal priors.
- **Upper bound on the error.** The error is `(1/2) sum min(P_v^N, P_w^N) <= (1/2) BC^N`, where `BC = sum_y sqrt(P_v P_w)`. This uses `min(a,b) <= sqrt(ab)`.
- **Lower bound.** By Cauchy-Schwarz, `(sum sqrt(P Q))^2 <= (sum min)(sum max) = (sum min)(2 - sum min)`. So the error is at least `(1/2)(1 - sqrt(1 - BC^{2N}))`.
- **Small coupling.** For small `k E_B`, `-ln BC = (k E_B)^2 J/8 + O(k^3)`, with `J = sum_y (rho_v - rho_w)^2 / P0`. Checked at `k E_B = 1e-3` to 1%.
- **The count.** Error `eps` is reached for `N (k E_B)^2` between `4 ln(1/(4 eps(1-eps)))/J` and `8 ln(1/(2 eps))/J`.

**Step 9. The numbers. CHECKED R1.**
- **The Gram matrix.** The Gram matrix of `(rho_L, rho_R)` against `1/P0` is `[[0.8370, 0.2712], [0.2712, 0.6812]]`, with determinant `0.4966 > 0`.
  - So every difference of two readings, `(c_L rho_L + c_R rho_R)` with `(c_L, c_R) != 0`, has `J > 0`.
  - All six pairs therefore separate at every `p_L`.
- **At `p_L = 1/2`.**
  - `J(0, mean) = 0.515`, giving 25 to 61 passages per `(k E_B)^2` at `eps = 0.01`.
  - The hardest pairs are "L against mean" and "R against mean", with `J = 0.244`.
- **At `p_L = 1/3`.** The hardest pair is "R against mean", with `J = 0.108`.
- **The sample mean alone.**
  - It sees only `p_L dY_L + p_R dY_R`, which vanishes at `p_L* = dY_R/(dY_R - dY_L) = 0.7216`. There it equals the records-only value `0`: the mean statistic is blind at that weight.
  - Block 116's gradient `kappa` has its blind weight at `0.1726` in box 9.
  - Away from `p_L*` the mean statistic needs roughly `(2 z sigma_Y / Delta)^2` passages, with `Delta` the kick difference. That is far more than R1's full-distribution test; for "0 against mean" at `p_L = 1/2`, it is about 2600 per `(k E_B)^2` at `z = 2.33`.

**Step 10. Rule R2. CHECKED R2.**
- The mean position at `t_f` is `(8.063, -0.99997, 0)`. It lies 0.437 (in `x`) and 0.500 (in `y`) from the nearest half-integers.
- With `|dX| <= 3.253` and `|dY| <= 2.193`, all four fields give the record `(8, -1, 0)` in every passage whenever `k E_B < 0.134`.
- The dynamics is deterministic, so no number of passages separates the readings at such couplings.

**Step 11. Block 116's four conditions with the walk.**
- **Condition 1** holds only statistically (Steps 8 and 9): one passage never resolves at first order, since `k E_B |kick| << sigma_Y = 7.4`.
- **Conditions 2 to 4** are supplied: `B` is unformed during the passage, `T` is light, and the field is static.
- The walk's own source is `O(k)` and would change the kicks at `O(k^2)`.

## 3. First unresolved step and limits

- **Floating point.** All walk numbers are controlled floating point, for one packet and one reading time in held boxes 41 and 61. Their limit as the box grows, including `Z^3` with the ambient at infinity, is not established; boxes 41 and 61 differ by 3.3%.
- **Supplied choices.** The record rules, R1's weights and the packet are supplied.
- **Not treated.**
  - The task's other example, records forming at a rate `|chi|^2` along the path. Each record would localize and disturb the packet, which needs a formation dynamics.
  - Second order in `k`.

## 4. What would finish it

1. A box sequence (81, 101, ...) or the `Z^3` Green function, to converge `dY_L` and `dY_R` at fixed packet and time.
2. The dependence on `s`, `k0`, the start point and the reading time. Also the asymptotic transverse-momentum kick as an alternative observable.
3. The rate-`|chi|^2` record rule along the path, with back-action.
4. The `O(k^2)` kicks, and the test body's own source (condition 3).
5. An exact-arithmetic version with a discrete-time walk (rational steps), if exact values are wanted.
