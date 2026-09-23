# J:derive:inertial-clause-without-redrawing:a3 — the pass-through streams are coupled, the wave freezes, and re-drawing opposite pairs on a bond clock is enough

**Provenance.** Worker `w-macbookpro90c72-j79a2`, model `claude-opus-5-5`, one session. The claim printed no prior attempts on this problem. Definitions come from block 44 (PR #8550, note `docs/ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_…_NOTE_2026-09-20.md`) and its simulator `probes/lib/inertial.py` (`tick6`).

**The clause.** The six-axis menu has contents `d ∈ {±e_x, ±e_y, ±e_z}`; `−d` is the opposite content.
- **(S).** Each record attempts `x → x + e_d` at rate 1. In every case the attempt exchanges the values of the two sites:
  - into an empty site, the record moves;
  - into a record of another content, the two contents are exchanged;
  - into a record of the same content, nothing happens.
- **(C).** On a bond clock, an opposite pair is re-drawn uniformly on the opposite pairs, and any other pair is exchanged with probability 1/2.

## 1. Statement

The task has three parts:
- (a) Prove that under (S) alone the six contents are six independent totally asymmetric exclusion streams with currents `ρ_d(1 − ρ_d)`, and compute the exact linear evolution of a standing density wave.
- (b) Classify the covariant, number- and momentum-conserving nearest-neighbour clauses in which contents never change, and decide whether any of them thermalizes momentum.
- (c) State the resulting theorem and the weakest re-drawing that keeps the uniform measure stationary.

**Obtained:**
- **(a) is false as stated (COUNTEREXAMPLE).** Each content is blocked only by its own kind. But an exchange moves the *other* content one step back along the mover's axis, so the six streams are coupled.
  - The exact product-state currents and the exact linearized evolution are given instead.
  - A standing wave does not oscillate as sound. At density `ρ0` it keeps the fraction `2/(3 − ρ0)` at zero frequency (20/27 at `ρ0 = 0.3`). The rest oscillates at speed `√(1 − ρ0/3)`.
- **(b)** A clause that never changes a content is a swap process with one rate per orbit; there are 10 orbits.
  - Every such clause conserves all six content numbers, so none thermalizes momentum.
  - "Thermalizes" means that the additive invariants are exactly `N` and `P`.
- **(c)** Waves need re-drawing, and re-drawing *only opposite pairs, on a bond clock* is enough.
  - This holds even when only the pairs on the two axes perpendicular to the bond are re-drawn.
  - The uniform measure then stays stationary, and the only additive invariants are `N` and `P`.
  - Re-drawing only head-on along the bond breaks stationarity, and so does re-drawing on the streaming clock.

## 2. Steps

**Step 1 (PROVED; CHECKED A.ownblock). (S) is a site-value exchange.**
- An attempt from `x` of content `d` replaces `(η_x, η_{x+e_d}) = (d, c)` by `(c, d)`. Here `c` may be empty, another content, or `d` itself.
- It is suppressed exactly when `c = d`. So each content is blocked only by its own kind.
- This much of (a) holds.

**Step 2 (PROVED; CHECKED A.counterexample). The streams are not independent.**
- *The configurations.* Let `A` be `+e_x` at `000` and `+e_y` at `100`. Let `B` be `+e_z` at `000` and `+e_y` at `100`. They have the same `+e_y` occupation.
- *From `A`.* The `+e_x` record's attempt exchanges, which puts the `+e_y` content at `000`. That is a step `−e_x`, at rate 1.
- *From `B`.* No event moves the `+e_y` content.
- *Conclusion.* The `+e_y` occupation process is therefore not Markov on its own: its jump rates depend on the other contents. An exclusion stream along `+e_y` never steps in `−e_x`.
- *In general.* An exchange moves the passed content `d'` by `−e_d`. When `d' = −d` this is `d'`'s own direction (head-on pass-through). When `d' ⊥ d` it is a sideways push.
- Block 44's own T3 momentum count ("an exchange passes `e_d` forward and `e_{d'}` back") records this. Its sentence "without (C) the six contents are six independent streams" does not.

**Step 3 (PROVED; CHECKED B.uniform2, B.product2). Every tilted product measure is stationary under (S).**
- A transition exchanges two site values, so it preserves `Π_x w(η_x)` for any weights.
- Every record `r` of a configuration `c` has exactly one streaming preimage: undo the exchange with the site behind `r`. Its rate is 1.
- So the inflow is `N·μ(c)`, which equals the outflow.
- Consequently the six content numbers `N_d` are conserved, and the local equilibria are product states with six free densities `ρ_d`.

**Step 4 (PROVED; CHECKED C.currents, C.mass, C.xmomflux). Exact product-state currents across an x-bond.**
- Enumerate the two sites' states. Attempts come from `+e_x` at the left end and `−e_x` at the right end; a head-on pair swaps at rate 2.
- The resulting x-currents:
  - `+e_x`: `ρ_+(1 − ρ_+ + ρ_−)`. It moves unless blocked by its own kind, and is also pushed by `−e_x`.
  - `−e_x`: `−ρ_−(1 − ρ_− + ρ_+)`.
  - Each transverse `d`: `−ρ_d g_x`, where `g_x = ρ_+ − ρ_−`.
- Their sum is `(1 − ρ) g_x`, block 44's mass current.
- The x-momentum flux is `ρ_+ + ρ_− − (ρ_+ − ρ_−)²`. It is carried by the x-movers only.
- In three dimensions, `j_d = e_d ρ_d(1 − ρ_d + ρ_{−d}) − ρ_d (g − e_d(e_d·g))`.
- The currents are exact in product states. That the gas follows the resulting conservation laws at large scales is ASSUMED (local equilibrium), exactly as in block 44's T3.

**Step 5 (PROVED from Step 4; CHECKED D.eigen, D.solution, D.amplitude, D.rho03). The linear evolution of a standing wave along x.**
- *The linear system.* Linearize at `ρ_d = c = ρ0/6`. The x-flux Jacobian has characteristic polynomial `λ⁴(λ² − (1 − 2c))`. Write `S = a_+ + a_−`, `D = a_+ − a_−`, and `b_d` for the transverse perturbations. Then:
  - `∂_t S = −(1 − 2c)∂_x D`,
  - `∂_t D = −∂_x S`,
  - `∂_t b_d = c ∂_x D`.
- *The initial wave.* Start with `a_d(0) = cos kx` for all six contents, the wave block 44's `sound` launches.
- *The solution:*
  - `S = 2cos ωt cos kx`,
  - `D = (2/√(1−2c)) sin ωt sin kx`,
  - `b_d = [1 + (2c/(1−2c))(1 − cos ωt)] cos kx`,
  - with `ω = √(1 − ρ0/3) k`.
- *The density amplitude* relative to its initial value is `2/(3 − ρ0) + ((1 − ρ0)/(3 − ρ0)) cos(√(1 − ρ0/3) kt)`.
- *At `ρ0 = 3/10`.* The frozen part is 20/27, the oscillating part 7/27, at speed `√(9/10) = 0.949`.
- *Comparison with sound.* This is not a sound wave: there is no symmetric oscillation through zero, and a zero-frequency mode carries most of the amplitude. Block 44's (C) gives sound at `√(7/30) = 0.483`.
- *Comparison with the task's reading.* The independent-stream reading would give frozen 2/3, oscillating 1/3 at speed `1 − ρ0/3 = 0.9`.

**Step 6 (NUMERICAL, not load-bearing; `N.sim`).** Run block 44's `sound("six", 64, 0.3, γ = 0)`: 4 runs, 300 ticks. The fit of `F + O e^{−gt} cos(vkt)` gives:

| Quantity | Fitted | Linear prediction | Independent-stream reading |
|---|---|---|---|
| Speed `v` | 0.950 | 0.949 | 0.900 |
| Oscillating part `O` | 0.270 | 0.259 | 1/3 |
| Offset `F` | 0.698 | 0.741 | 2/3 |

The offset sits below 0.741 because the frozen mode decays diffusively beyond Euler order.

**Step 7 (PROVED; CHECKED E.group, E.orbits, E.invariants). The class of clauses that never change a content.**
- *Scope.* Two-site events on nearest-neighbour bonds, with rates that depend on the bond and on the two site states.
- *Every event is a swap.* An event that keeps the number and the multiset of contents must turn the pair of states `(a, b)` into `(b, a)`, a swap. Momentum is then conserved automatically.
- *The orbits.* Covariance under the 24 proper cubic rotations leaves one free rate per orbit of (bond, ordered pair of states), where `(e; a, b)` and `(−e; b, a)` are the same bond. There are 10 orbits:
  - a record next to an empty site: forward, backward, sideways;
  - two axial records: approaching, receding;
  - an axial record and a perpendicular one: toward, away;
  - two perpendicular records: opposite, and orthogonal of either handedness.
- *None thermalizes.* Every event of every such clause permutes contents among sites, so all six `N_d` are conserved. This holds for any range, not only for this scope.
- *The definition.* "Thermalizes momentum" means: the additive invariants `Σ_r φ(s_r)` conserved by every event are exactly `span{N, P_x, P_y, P_z}`, the lattice-gas notion.
- Every content-preserving clause has six of them. The additive invariants include the axis populations `N_{+i} + N_{−i}`, which are not functions of `N` and `P`. An anisotropic content distribution therefore never relaxes, and no content-preserving clause thermalizes.

**Step 8 (PROVED; CHECKED F.C, F.opp, F.min, F.fail, F.three). Which re-drawings keep the uniform measure stationary.**
- *Sufficient.* Re-drawing on a bond clock with a symmetric kernel on each bond's pair states keeps the uniform measure stationary, together with (S) (Step 3). This covers:
  - `Copp`: opposite pairs, re-drawn uniformly on the six opposite pairs, with no exchange of other pairs;
  - `Cmin`: on a bond along `e_k`, only the opposite pairs on the two axes perpendicular to `e_k`, re-drawn uniformly among those four.
- *The invariants of `Copp` and `Cmin`.* Invariance requires `φ(d) + φ(−d) = φ(d') + φ(−d')` for the axes that are re-drawn into each other. For `Cmin`, bonds along `e_z` connect the x- and y-axes and bonds along `e_x` connect y and z. Hence `φ(d) = s + v·e_d`, and the invariants are exactly `N` and `P`.
- *Block 44's exchange of non-opposite pairs is unnecessary.* It is content-preserving.
- *Not sufficient.* Two variants break the stationarity of the uniform measure:
  - re-drawing only pairs head-on along the bond;
  - re-drawing a head-on pair when the streaming attempt meets it, that is, on the streaming clock.

  On the `3³` torus with two records, 486 of the 12636 configurations are unbalanced under each. This matches block 44's count for its blocked-attempt rule.
- *Checked.* With three records (631800 configurations), (S) and (S)+`Cmin` balance exactly, and `Cmin` has invariants `N` and `P`.

**ASSUMED:** the local-equilibrium (hydrodynamic) closure behind Step 5's equations, as in block 44's T3.

## 3. The first failing step

The statement to prove in (a), "six independent totally asymmetric exclusion streams with currents `ρ_d(1 − ρ_d)`", fails at its first step. The streams are coupled through the exchange (Step 2).
- The along-axis current is `ρ_d(1 − ρ_d + ρ_{−d})`.
- The transverse contents are advected at `−ρ_d g`.

The requested conclusion for (a), that a standing wave does not oscillate as sound, survives. It holds with the corrected numbers (Step 5).

## 4. What would finish it or extend it

1. **The hydrodynamic limit.** A proof that the six-stream conservation laws of Step 4 govern the gas at large scales, i.e. local equilibrium for (S). This is open, as is block 44's T3 closure.
2. **Finite-torus reducibility is not the right test of thermalization.** In exploration (not claimed), even full (C) leaves 741 classes on the `3³` torus with two records: records on lines that never meet never interact. The collision-invariant test of Steps 7–8 is the right one.
3. **The sphere menu.** A content-preserving sphere clause conserves the whole empirical distribution of contents, which is infinitely many invariants. Block 44's T5 re-drawing on the circle of pairs with the same sum is the analogue of `Copp`. The analogue of `Cmin` is to re-draw only on a sub-circle.
4. **Whether `Cmin` gives the same sound speed as (C) at Euler order.** Expected but not checked here: with invariants `N` and `P` only, the local equilibria are the same tilted product states.

## 5. Running it

```
python3 probes/work/derive/inertial-clause-without-redrawing/w-macbookpro90c72-j79a2/check.py
```

Requires `sympy`. `numpy` and `numba` are used only for the labelled simulation, through `probes/lib/inertial.py`. The run takes about 15 s: exact enumerations on the `3³` torus with two records (12636 configurations) and three records (631800), plus a 5-second simulation.
