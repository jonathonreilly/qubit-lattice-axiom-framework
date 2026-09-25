# Nonlinear record motion, attempt 1: without randomness a density disturbance never dies; with any randomness it does

Worker `w-macbookpro9927a-j0bdc` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory. They run in about 2.5 minutes with a peak of about 250 MB. The families are:

- **Q**: pinned sources.
- **D**: the deterministic rule.
- **E**: the random rule on finite rings.
- **M**: the mean-field version.
- **N**: floating-point numerics, marked `[float]`.

Families D, E and M are exact: integers, fractions, Gaussian rationals and sympy. Family M's last line is a `[float]` scan.

## Sources, provenance and route

**Sources.**
- **Block 96**, landed on main (pinned at `60c5f194`).
  - T1: with detailed balance, a stationary autocorrelation is completely monotone.
  - T2: the direction-memory rule's endpoint p = 1 is "free streams".
- **Block 122**, PR #9176 at head `248efca4`.
  - T1: nonnegative gain-one weights give every branch `|λ(k)| ≤ 1`.
  - T2: a branch with `|λ| = 1` on an open set of k exists only for rigid transport. Rigid transport is defined as "each entry of each `w_j` is carried by a single displacement ... The rule then moves everything at one velocity, up to a gauge".
  - Its first open item: "A nonlinear formation law is not covered."
- **Block 123**, PR #9177 at head `f8fb5519`. T4: "Every such density branch has modulus below one away from `k = 0`, as block 122 requires".
- **The task text**, from `probes/TASKS.json` at `74754e62`.

Family Q checks the file hashes and the quoted lines verbatim. I use only the quoted statements of blocks 122 and 123, not their proofs.

**Provenance.**
- The claim printed no prior attempts. My plan was fixed before I read anything beyond the task.
- None of my earlier units treats this problem.
- Block 122 is a harvest of attempts by Claude Opus 5, the same model family as this worker, refereed by Grok. It enters only as the quoted statements above.

**Route.**
- I take the task's example rule literally. It is the Nagel–Schreckenberg traffic rule (1992).
- For r = 0 I prove what every orbit does, on every ring and from every initial state (§A).
- For 0 < r < 1 I prove that every finite ring has a single aperiodic closed class, so every disturbance decays (§B). Controlled numerics then follow the decay at fixed wave number as the ring grows (§N).
- §C linearizes the site-factorized mean-field version exactly.
- §D answers part (c).

## The rule

**Setting.**
- N records sit on the ring Z_L, with 1 ≤ N ≤ L − 1, at most one per site.
- Record i carries a speed content v_i ∈ {0, …, V}.
- Its leader is record i + 1, cyclically.
- Its gap g_i is the number of empty sites between it and its leader. For N = 1 the record is its own leader, with g = L − 1.

**One step, all records at once.**
1. The move is `u_i = min(v_i + 1, V, g_i)`.
2. With probability r, independently for each record, `u_i → max(u_i − 1, 0)`.
3. Every record advances: `x_i → x_i + u_i` and `v_i → u_i`.

This is the task's wording: the speed "rises by one if the sites ahead are empty, falls to the gap if blocked, then slows by one with probability r".

**Quantities used below.**
- The slack is `s_i = g_i − u_i ≥ 0`. Record i is *saturated* at a step when s_i = 0, that is, when it moves its full gap.
- The occupation is `n_t(x) ∈ {0, 1}`.
- The density mode is `ρ̂_k(t) = Σ_x e^{−ikx} n_t(x) = Σ_i e^{−ik x_i(t)}`, with k ∈ (2π/L)Z.

## (1) The statement attempted

**(A) The deterministic rule, r = 0.** Take any L, any N with 1 ≤ N ≤ L − 1, any V ≥ 1 and any initial state. There is a finite t* such that for all t ≥ t*:

| Density | What every record does | Occupation | Density mode |
|---|---|---|---|
| N(V+1) < L | moves exactly V | `n_{t+1}(x) = n_t(x − V)` | `ρ̂_k(t+1) = e^{−ikV} ρ̂_k(t)` |
| N(V+1) > L | moves exactly its gap | `n_{t+1}(x) = n_t(x + 1)` | `ρ̂_k(t+1) = e^{+ik} ρ̂_k(t)` |
| N(V+1) = L | every gap equals V; both rows hold | | |

So |ρ̂_k(t)| is constant for t ≥ t*, for every k. Because 0 < N < L, some k ≢ 0 has ρ̂_k(t*) ≠ 0. States carrying any prescribed long-wave modulation that respects the gap conditions of Step 6 need no transient at all.

**(B) The random rule on finite rings, 0 < r < 1.** For every L, every N with 1 ≤ N ≤ L − 1 and every V ≥ 1, the rule's Markov chain on its finite state space has exactly one closed class, and that class is aperiodic. Hence, using the ASSUMED convergence theorem for finite chains, for every k ≢ 0:
- `E[ρ̂_k(t) | X_0] → 0` geometrically, from every initial state;
- the stationary autocorrelation `E_π[ρ̂_k(t) conj ρ̂_k(0)] → 0` geometrically.

**(C) The mean-field version.** This is the site-factorized version defined in Step 13. Exactly:
- (i) Its uniform fixed point and its linearization weights equal the ring Jacobian, at four points.
- (ii) For V = 1 the linearization closes on the density. Its weights are nonnegative and sum to one, and `1 − |λ|² = 2p(1−p)(1 − cos k) + 4p²ρ(1−ρ) sin² k` with p = 1 − r.
- (iii) For V ≥ 2 the speed-resolved weights include negative ones. Every root lies strictly inside the unit circle at 144 rational points. A root lies strictly outside at 3 points: V = 2 with r ∈ {0, 1/50}, ρ = 3/20 and `e^{ik} = (−5+12i)/13`; and V = 5 with r = 0, ρ = 1/50 and `e^{ik} = (−8+15i)/17`.

**Controlled numerics (§N; not part of the statement proved).** At r = 1/4 the stationary autocorrelation of ρ̂_k decays at fixed k = 2π/64. The decay curve converges as the ring grows from L = 128 to 1024. The phase velocity is forward on the free side and backward on the jam side. For V = 1 it matches the kinematic speed J'(ρ).

## (2) Steps

### A. The deterministic rule (r = 0)

**Step 1 (PROVED): bookkeeping.**
- `g_i(t+1) = g_i(t) − u_i(t) + u_{i+1}(t) = s_i(t) + u_{i+1}(t)`.
- `v_i(t+1) = u_i(t)`.
- Records never collide or pass, because u_i ≤ g_i.
- These hold at every r, with u the final move.

**Step 2 (PROVED): at t ≥ 1 the gap is at least the leader's speed.** For t ≥ 1, `g_i(t) ≥ v_{i+1}(t)`.

*Proof.* `g_i(t) = s_i(t−1) + u_{i+1}(t−1) ≥ u_{i+1}(t−1) = v_{i+1}(t)`. ∎

**Step 3 (PROVED): saturation persists.** Let r = 0 and t ≥ 1. If s_i(t) = 0, then s_i(t+1) = 0 and `u_i(t+1) = u_{i+1}(t)`. A saturated record stays saturated and copies its leader's move one step late.

*Proof.*
1. By Step 1, `g_i(t+1) = u_{i+1}(t)`, so `u_i(t+1) = min(u_i(t) + 1, V, u_{i+1}(t))`.
2. Now `u_{i+1}(t) ≤ V`.
3. Also `u_{i+1}(t) ≤ v_{i+1}(t) + 1 ≤ g_i(t) + 1 = u_i(t) + 1`, by Step 2 and s_i(t) = 0.
4. So the minimum is `u_{i+1}(t) = g_i(t+1)`. ∎

At t = 0 this can fail, because the initial speeds are arbitrary. With gaps (0, 2), speeds (0, 2), V = 2 and L = 4, both records are saturated at t = 0, and record 0 is not at t = 1 (family D).

**Step 4 (PROVED): an unsaturated record moves `min(v_i + 1, V)`.** If s_i(t) > 0, then `u_i(t) = min(v_i(t) + 1, V)`, because the gap is not the minimum.

With Step 3, each record i has a saturation time T_i ∈ {1, 2, …, ∞}:
- it is unsaturated at every t ∈ [1, T_i);
- it is saturated at every t ≥ T_i.

On [1, T_i), `u_i(t) = min(u_i(t−1) + 1, V)`. By induction, `u_i(t) = min(u_i(0) + t, V)`.

**Step 5 (PROVED): the dichotomy.** Let U = {i : T_i = ∞}.

*(a) U is not empty.*
1. Every i ∈ U has `u_i(t) = V` for t ≥ V, by Step 4.
2. Going backwards from a record of U, the records behind it are saturated from τ = max(V, max_{j∉U} T_j) on.
3. By Step 3 each copies its leader one step late. So `u_{i−q}(t + q) = V`, and every record moves V at every t ≥ τ + N.
4. Then `NV = Σ u_j ≤ Σ g_j = L − N`, so N(V+1) ≤ L.

*(b) U is empty.* From max_j T_j on, every record is saturated, so `Σ u_j = Σ g_j = L − N`. Since every u_j ≤ V, this gives L − N ≤ NV, so N(V+1) ≥ L.

*Conclusion.*
- If N(V+1) > L, then U is empty. Eventually every record moves its full gap at every step.
- If N(V+1) < L, then U is not empty. Eventually every record moves V at every step.
- If N(V+1) = L, either case gives `Σ u = NV = L − N` with `u_j ≤ min(V, g_j)`. This forces `u_j = g_j = V` for every j.

∎

**Step 6 (PROVED): rigid translation, and the two invariant sets.**

*Every record moves V.* Then x_i → x_i + V, so `n_{t+1}(x) = n_t(x − V)`.

*Every record moves its full gap.* Then `x_i(t+1) = x_i(t) + g_i(t) = x_{i+1}(t) − 1`, so the occupied set moves by −1: `n_{t+1}(x) = n_t(x + 1)`.

*Fourier modes.* `ρ̂_k(t+1) = e^{−ikV} ρ̂_k(t)` in the first case and `e^{+ik} ρ̂_k(t)` in the second. If every ρ̂_k with k ≢ 0 vanished, Fourier inversion would make n constant, equal to N/L. That is impossible for 0/1 values with 0 < N < L.

*The two invariant sets.* The free set is `F = {v_i ≥ V − 1, g_i ≥ V}`. The jam set is `J = {g_i ≤ min(v_i + 1, V), g_{i+1} ≤ g_i + 1 for all i}`.
- On F every record moves V, and the gaps are unchanged.
- On J every record moves its gap, and then `g_i' = g_{i+1}` and `v_i' = g_i`. The conditions for J are carried over: `g_{i+1} ≤ g_i + 1 = v_i' + 1` and `g_{i+2} ≤ g_{i+1} + 1`.

**Step 7 (CHECKED): family D.**
- **The lemmas.** Steps 2 to 4 hold on every state that occurs after one step. Every state at every t ≥ 1 is such a state. The check covers every initial state (car 0 at site 0 by rotation) on every ring with L ≤ 11, 9, 8 for V = 1, 2, 3, every N and all speeds: 708 916 initial states.
- **The orbits.** Every orbit enters F when N(V+1) < L, J when N(V+1) > L, and the uniform gaps V when N(V+1) = L. Both sets are invariant, with the rigid move.
- **Transients.** The longest transient is at most ⌊L/2⌋ on these rings. This is observed, not claimed in general.
- **Two modulated states on L = 240, V = 2.**
  - A free state with N = 60, gaps 2 + {0, 1, 2}.
  - A jam with N = 120, gaps {0, 1, 2} following 1 + cos.
  - Both move by exactly +2 and −1 per step for 2000 steps. |ρ̂(2π/L)| is 8.04 and 31.50, both constant.
- **Random large rings.** 40 random initial states on L = 500 and 2000 with V = 2 and 5 all reach F or J.

### B. The random rule (0 < r < 1) on finite rings

**Step 8 (PROVED): the support of one step.**
- The one-step law puts positive probability exactly on the 2^m outcomes that slow any subset of the m records whose move before slowing is ≥ 1.
- This support does not depend on r ∈ (0, 1).
- Under the all-slowdown outcome, `u_i = max(min(v_i + 1, V, g_i) − 1, 0) ≤ v_i`, so no speed rises.

**Step 9 (PROVED): with N ≥ 2, every state reaches the stopped jam.** Let N ≥ 2. Every state reaches `M_{x0}` for every x0 with positive probability. Here M_{x0} is the stopped jam: records at x0 − N + 1, …, x0, all with speed 0.

*(a) Repeated all-slowdown leads to a common speed.*
1. By Step 8 the speeds are non-increasing, hence eventually constant, equal to w_i say.
2. With constant speeds, `g_i(t+1) = g_i(t) − w_i + w_{i+1}` must stay ≥ 0 forever. So `w_{i+1} ≥ w_i` for all i, cyclically, and all w_i equal a common w.
3. If w ≥ 1, then `w = min(w+1, V, g_i) − 1` forces g_i ≥ w + 1 and w ≤ V − 1.

*(b) If w ≥ 1, the common speed can be lowered.*
1. Pick a record f and its leader c ≠ f, which exists because N ≥ 2.
2. Every record except f takes the slowdown at every step. Their speeds stay at w: every gap stays ≥ w + 1, and c's gap only grows if c's leader is f.
3. f never takes the slowdown. While `g_f ≥ w + 1`, its move `min(v_f + 1, V, g_f)` is ≥ w + 1, so g_f falls by at least one per step.
4. g_f first drops to w or below exactly when the move is gap-limited, and then the new gap is exactly w. At that moment v_f ≥ w + 1.
5. One slowdown step for f now gives `u_f = min(v_f + 1, V, w) − 1 = w − 1`.
6. Everyone then returns to all-slowdown. The speeds are non-increasing, and f's speed stays ≤ w − 1. So the new common limit is ≤ w − 1.
7. By induction, every record ends up stopped.

*(c) From all stopped, a stopped jam behind any chosen front record F.*
1. A record with gap ≥ 1 skips the slowdown once. It moves one site, with speed 1. Everyone else takes the slowdown and stays stopped.
2. Slowed at every step, this record keeps moving one site per step while its gap is ≥ 2 (for V = 1 it stops after each move and is released again). It stops when its gap is 1.
3. One step without slowdown makes it adjacent to its leader. The next step, with gap 0, stops it.
4. Walk the records behind F up in turn: F − 1, then F − 2, and so on.

*(d) The jam can be moved to any place.*
1. Release the front record and walk it around the ring, as in (c), until it stops behind the jam's last record.
2. The stopped jam now ends one site earlier.
3. Repeat until the jam is at the wanted place.

*(e) Uniqueness and aperiodicity.* M_{x0} has a self-loop. Its front record has gap L − N ≥ 1 and move 1 before slowing, and it stays put with probability r. Every other record has gap 0. So the closed class containing M_{x0} is aperiodic. Every state reaches M_{x0}, so every closed class contains it: this class is the only one. ∎

**Step 10 (PROVED): N = 1.**

*If V = 1 or L = 2.* Then u ≤ 1, the record can stop, and Steps 9(c) to 9(e) apply unchanged.

*Otherwise, m = min(V, L − 1) ≥ 2.*
1. The record is never blocked. Its speed can never fall below m − 1, so the stopped states are transient. This is why family E uses a different reference state for this case.
2. Skipping the slowdown raises the speed to m within m steps.
3. The speed set {m − 1, m} is closed.
4. Over t = L + 1 steps with the last step unslowed, the displacements tm − j with 0 ≤ j ≤ L cover L + 1 consecutive integers. So (x0, m) is reached from anywhere in the class.
5. The record returns to (x0, m) after L steps and after L + 1 steps. So the period is 1. ∎

**Step 11 (CHECKED): family E.**
- The check uses the exact support graph on every state of every ring with L ≤ 12, 9, 7 for V = 1, 2, 3, and every N < L: 123 cases, 1 184 754 states.
- Every state reaches the reference state. In the 111 cases where the stopped jam is the reference, it has a self-loop. The other 12 cases are one record at m ≥ 2, cruising.
- The forward closure of the reference state has period 1, computed as the gcd of level differences along its edges.
- No speed rises under all-slowdown.

A first version of this check used the stopped jam for N = 1 too, and failed at N = 1 with V ≥ 2. That failure is what exposed Step 10's separate case.

**Step 12 (ASSUMED, then PROVED).**
- *ASSUMED: the convergence theorem for finite Markov chains.* If a finite chain has a unique closed class and that class is aperiodic, then its stationary law π is unique, and `P^t(x, ·) → π` geometrically from every x.
- *PROVED: rotation invariance and decay.*
  1. The rule commutes with rotating the ring. So π composed with a rotation is also stationary, and it equals π by uniqueness.
  2. Hence `E_π n(x) = N/L`, and `E_π ρ̂_k = 0` for k ≢ 0.
  3. So `E[ρ̂_k(t) | X_0] → 0` geometrically.
  4. Also `E_π[ρ̂_k(t) conj ρ̂_k(0)] = Σ_y π(y) conj ρ̂_k(y) E_y ρ̂_k(X_t) → 0`.

The rate is positive at each fixed L. That it stays positive at fixed k as L grows is §N's numerical question, not a proved step.

### C. The mean-field version

**Step 13 (definition; PROVED).**

*The fields.* c_v(x) is the probability that site x holds a record of speed v, and `ρ(x) = Σ_v c_v(x)`.

*The update.*
- A record of speed v at site x takes the move u with probability `T_{v→u}(ρ(x+1), …, ρ(x+V))`.
- T comes from the rule with the gap law computed as if the sites were independent. With a = min(v + 1, V):
  - `P(gap = d) = Π_{j≤d}(1 − ρ(x+j)) · ρ(x+d+1)` for d < a;
  - `P(gap ≥ a) = Π_{j≤a}(1 − ρ(x+j))`.
- Then comes the slowdown with probability r.
- So `c'_u(y) = Σ_v c_v(y − u) T_{v→u}(ρ(y−u+1), …)`.

*The uniform fixed point* is `c_v = ρ p_v`, where p is the stationary law of the speed chain `T⁰ = T(ρ, …, ρ)`.

*The linearization.* With ε the perturbation and `η = Σ_v ε_v`:
- `δc_u(y) = Σ_{v'} T⁰_{v'→u} ε_{v'}(y − u) + Σ_{j=1}^{V} G_u(j) η(y − u + j)`;
- `G_u(j) = ρ Σ_v p_v ∂T_{v→u}/∂ρ_j`.

T is affine in each ρ_j. So `∂T/∂ρ_j = T|_{ρ_j = 1} − T|_{ρ_j = 0}` exactly. The ring map is affine in each variable, so unit differences give its exact Jacobian.

The symbol is `M(k)_{u v'} = e^{−iku} T⁰_{v'→u} + Σ_j G_u(j) e^{−ik(u−j)}`. Because `Σ_u T ≡ 1`, `Σ_u G_u(j) = 0`, and the column sums at k = 0 are 1.

**Step 14 (PROVED, CHECKED): V = 1 closes on the density.**
- T does not depend on the speed. So the density obeys `δρ'(y) = r δρ(y) + (1−r)(1−ρ) δρ(y−1) + (1−r)ρ δρ(y+1)`.
- These are nonnegative gain-one weights at displacements (0, +1, −1), a rule of the kind block 122 covers.
- `λ(k) = r + (1−r)(1−ρ)e^{−ik} + (1−r)ρ e^{ik}`. Expanding, with p = 1 − r, gives `1 − |λ|² = 2p(1−p)(1 − cos k) + 4p²ρ(1−ρ) sin² k`. This is checked symbolically.
- So `|λ| < 1` for every k ≢ 0 when 0 < r < 1 and 0 < ρ < 1.
- At r = 0, `|λ| = 1` only at k ∈ {0, π}, with λ(π) = −1. That is a single point, not an open set, as block 122 T2 allows.

The contrast with part A is exact, at V = 1 and r = 0.
- The deterministic rule ends every orbit in rigid transport at +1 or at −1, undamped at every k.
- Its mean-field linearization damps every k except 0 and π.
- The weights p(1−ρ) forward and pρ backward are exactly the two rigid motions the deterministic rule chooses between. The mean field mixes them, and the mixing damps.

**Step 15 (CHECKED): family M.**
- **The Jacobian.** The fixed point and the weights equal the exact ring Jacobian at four (V, r, ρ) points, one of them with r = 0.
- **Signed weights for V ≥ 2.** At r = ρ = 1/4 the speed-resolved weights include negative ones: 3 for V = 2 (the least is −111/880), 6 for V = 3 and 15 for V = 5. So block 122's nonnegativity fails for the linearization itself.
- **The Schur–Cohn routine.** Its recursion is `q = (conj(a_n) p − a_0 p*)/z` while `|a_0| < |a_n|`. It is checked against numpy on 300 random Gaussian-rational polynomials.
- **Damping.** Every root lies strictly inside the unit circle at all 144 points V ∈ {2, 3, 5}, r ∈ {1/4, 1/2}, ρ ∈ {1/10, 1/4, 1/2, 4/5}, `e^{ik}` ∈ {(4+3i)/5, (3+4i)/5, i, (−5+12i)/13, (−3+4i)/5, −1}.
- **Roots outside.** At the three points of (C)(iii), Schur–Cohn fails and the resultant `Res(χ, χ*) ≠ 0`. So no root lies on the circle, and one lies outside. The float moduli are 1.0456, 1.0199 and 1.0064.

Where the mean-field linearization fails to damp, it is a linear instability of the uniform state at short wavelength (k ≈ 2, about three sites), not a lasting long wave. The `[float]` scan finds max|λ| > 1 only in three places:
- V = 2, r = 0, for ρ from 0.01 to 0.37;
- V = 2, r = 1/50, for ρ from 0.05 to 0.28;
- V = 5, r = 0, for ρ from 0.01 to 0.03.

The scan covers V = 2 to 6, r ∈ {0, 1/50, 1/20, 1/10, 1/5}, ρ from 0.01 to 0.99 and 360 wave numbers. Every point with r ≥ 1/20 is damped.

### N. Controlled numerics at r > 0 (`[float]`)

**What is measured.**
- 32 independent rings per point.
- Equilibration of 10 000 steps, then 16 384 measured steps.
- `R(τ) = |⟨ρ̂_k(t+τ) conj ρ̂_k(t)⟩| / ⟨|ρ̂_k|²⟩`, time-averaged per ring, with jackknife errors over the rings.
- k0 = 2π/64 on L = 128, 256, 512 and 1024.

**R at τ = 64, 256, 1024, for L = 128 and L = 1024.**

| Point | L = 128 | L = 1024 | Phase velocity |
|---|---|---|---|
| V = 1, ρ = 1/4, r = 1/4 | (0.717, 0.150, 0.025) | (0.692, 0.121, 0.025), errors (0.005, 0.011, 0.013) | 0.572 |
| V = 2, ρ = 1/2, r = 1/4 | (0.649, 0.140, 0.008) | (0.643, 0.156, 0.009) | −0.52 (backward: the jam side) |
| V = 2, ρ = 0.15, r = 1/4 | (0.570, 0.112, 0.018) | (0.544, 0.096, 0.009) | +1.60 |

For V = 1, the current J = 0.16939 matches the exact current `(1 − √(1 − 4pρ(1−ρ)))/2 = 0.16928` of this rule, and the phase velocity 0.572 compares with J'(ρ) = 0.5669. Both formulas are ASSUMED and are used only as controls.

**The pass criteria**, which all hold:
- R(1024) < 0.05 on every ring;
- L = 512 and 1024 agree within 3 errors;
- every ring is within 0.05 of L = 1024.

Every ring is within 0.04 of L = 1024, in either direction. At τ = 256 the smallest ring decays slightly more slowly at the V = 1 and free-side points, and slightly faster at the jam-side point. L = 512 and 1024 agree within 2.5 errors at every point.

**Controls and scaling.**
- **The same simulator at r = 0** keeps the mode exactly, as part A requires: |R − 1| ≤ 4e−16, with velocities exactly +2.000000 on the free side and −1.000000 on the jam side.
- **Decay time against k**, at L = 1024 with m = 4 to 64. The local exponents −dlog τ/dlog k are 1.42 to 1.51 for V = 1 and 1.41 to 1.50 for V = 2 at ρ = 1/2. The value 3/2 expected in the literature for driven exclusion is a comparison only, not a premise.
- **Small r.** At V = 2, ρ = 1/2, r = 0.05 and L = 512, R(2048) = 0.014 ± 0.016.

## D. Answer to (c): which hypothesis of block 122 fails, and what kind of disturbance lasts

**The hypothesis that fails is linearity.** A record's move depends on the occupation of the sites ahead, through the minimum with the gap.

**In block 122's own terms, what lasts at r = 0 is still rigid transport.** But it is rigid transport of the occupied set, with a velocity the density chooses:
- Below density 1/(V+1), every record moves V, and the pattern travels with the records.
- Above it, every record moves its full gap. The pattern then travels backward one site per step. This is a *jam wave*, moving against the records at velocity −1, a velocity no record ever has.

Block 122 defines rigid transport by the displacements that carry its weights. A single displacement y ≥ 0 at depth j moves at velocity y/(j+1) ≥ 0. So a linear rule whose weights are the records' own displacement odds, supported on 0, …, V, can transport rigidly only at a velocity ≥ 0. The jam wave is beyond such rules. The nonlinear rule reaches it because the configuration makes the choice between the two rigid motions, and it does so from every initial state (Step 5).

**On the configuration space the rule is linear**: a Markov matrix, nonnegative with gain one. Block 122's dichotomy reappears there, though its theorems are not invoked for it.
- At r = 0 the rule is a deterministic map. On its final cycles it is a permutation, so it keeps eigenvalues of modulus one.
- At 0 < r < 1 there is one aperiodic closed class, and every non-stationary mode decays (Step 12).

So the nonlinearity does not get around nonnegativity. It supplies a velocity chosen by the density. A lasting disturbance still needs zero randomness.

**Kind of disturbance.**
- At r = 0 it is a travelling pattern: free transport below 1/(V+1) and a jam wave above it. Boundaries between jammed and free stretches are fronts, and they move with the pattern at −1.
- It is not an oscillation. Nothing restores it. The Fourier amplitude only turns in phase, at the same phase velocity for every k: V, or −1. There is no dispersion.
- At 0 < r < 1 disturbances still travel, at J'(ρ): forward on the free side and backward on the jam side. They die at every fixed k.

Block 96 T2's "free streams" at p = 1 are the linear counterpart of the free case.

## (3) Where the route stops

- **The limit of large rings at r > 0.** Decay at fixed k as L → ∞ is shown only numerically. Step 12's rate is positive at each L, and §N shows the fixed-k curve converging from L = 128 to 1024.
- **The unstable region of the mean field.** It is certified at three points only. Its extent comes from a float scan.
- **The transient.** Its length at r = 0 is not bounded in general. On the exhaustive rings it is at most ⌊L/2⌋.
- **The rule itself** is a supplied, named rule. It is not derived from the framework, and nothing here is adopted.

## (4) What would finish it

1. A proof that the decay rate at fixed k stays positive as L → ∞ for 0 < r < 1. A coupling argument, or known results for driven exclusion, might supply one.
2. The exact boundary of the mean field's unstable region.
3. Nonlinear rules with a restoring interaction, which could oscillate rather than only transport. In the rule treated here, what lasts is purely kinematic.
