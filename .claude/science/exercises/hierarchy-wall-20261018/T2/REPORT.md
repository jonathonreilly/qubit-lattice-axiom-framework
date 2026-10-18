I ran T-LIGHTCONE, and the result is **OPEN** under the rule I registered. There is no spiral. The coupling that sets the scale grows fast (y_t = 1.40 ± 0.05), so it gives no native slow passage. OPEN comes only from the shrinking couplings: I could not measure the slowest one well enough to show its |y| is above 0.2. This is a same-family run (Opus 5.5), not refereed. PREREG.md was written before any run (18:39–18:41Z). Two dated addenda (18:59Z, 19:39Z) were added after I had seen data. They add checks only; the readings and decision rules are unchanged.

## Plain version
- **The model.** The landed level-time model is a classical Heisenberg magnet on a two-layer cubic lattice. I simulated it exactly as written.
- **Where it orders.** β_c = 0.5561. That is below the landed proof's sufficient bound of 0.5905, as it has to be.
- **The coupling that grows.** Each doubling of scale multiplies the distance from the critical point by about 2^1.4. So 38.4 e-folds of scale need a starting distance of about e^{−54} ≈ 10^{−23.5}. The model does not fix β, so that distance is a number put in by hand.
- **Spirals.** No complex eigenvalue pair survives the counting rule.
- **What stays open.** It is the rate of the slowest shrinking coupling. A shrinking coupling cannot create a large scale by itself, so this gap cannot hide a native passage (suggested).
- **Cubic anisotropy.** The one nearly marginal direction known for this class is exactly zero here, because the model is symmetric under spin rotations (proved).

## Read first (step 1)
- MINIMAL_AXIOMS_2026-06-29.md in full.
- PRIMITIVE_REGISTRY_CHECK.md and SCALE_REFERENCE_PRIMITIVE_NOTE.md.
- derivation_obligations.json: it has no hierarchy entries.
- WALL.md, TESTS.md and T/REPORT.md.
- The 09-23 bilayer note and its 09-20 parent.

## Prior art (origin/main 584755767d)
- **09-23 note:**
  - T1: detailed balance.
  - T2: the map to the bilayer.
  - T3: order for β > 3(I₀+I₂)/2 ≈ 0.5905. This is a sufficient bound, not the onset.
- **09-20 parent:** a historical onset "between 0.5 and 0.6". It is marked deferred.
- **Not on main:** β_c, any critical exponent, Monte Carlo RG or a dynamic exponent for this model. I searched for Binder, MCRG, critical exponent, and Heisenberg or O(3) universality.
- **Scope flag, from the note itself:** the model re-records every site at every tick. The Record axiom excludes that. So this model is a comparator, not framework content.

## Method
- **Model.** Contents are unit 3-vectors with uniform measure, and K(s′|s) ∝ exp(β s′·Σ_{N7} s). I simulated the doubled graph directly, so T2 is not an input.
- **M0, model check (checked).** At L=8 I ran the landed kernel tick by tick and compared it with a cluster sampler. One level's ⟨|m|²⟩ agrees at β=0.50 (+0.7σ) and β=0.60 (−0.4σ). The pair energies also agree.
- **M1.** Wolff cluster updates, L=8–64, single-histogram reweighting, jackknife errors.
- **M2.** Swendsen's Monte Carlo RG with b=2, using 6 even and 3 odd operators that are invariant under spin rotations. L=16–128.
- **M3.** Autocorrelation under the landed kernel in level time.

## Results
- **β_c (checked):** 0.5561(1).
- **y_t (checked, M1):** from the ξ₂/L slopes:

  | Size pair | (12,24) | (16,32) | (24,48) | (32,64) |
  |---|---|---|---|---|
  | y_t | 1.41(3) | 1.46(3) | 1.41(2) | 1.32(5) |

  Joint fits give 1.40–1.41(1).
- **y_h (checked, M1):** 2.48(1). The 3D O(3) literature values are 1.406 and 2.481 (comparator only).
- **ω, the slowest shrinking coupling (M1, not resolved):**
  - R at fixed ξ₂/L falls from 1.153 at L=8 to 1.138 at L=64.
  - One-correction fits give ω = 0.5–0.7 ± 0.4 for L ≥ 8, and no constraint for L ≥ 12.
  - ω fixed at 0.2 fits about as well: χ² 5.4/5, against 4.6/4 free.
  - Literature value: 0.76 (comparator).
- **MCRG (checked, limited by truncation):**
  - y_t is 1.29–1.53 and y_h is 2.37–2.48, depending on how many operators are kept.
  - With 2–3 operators, the leading shrinking eigenvalue is −0.41 to −1.10.
  - Adding the distance-2 operator brings in a second shrinking eigenvalue:
    - On 4³ final lattices it is +0.26 to +0.80. That is an artefact: there, x+2e and x−2e are the same site.
    - On 8³ final lattices at blocking steps 2–3 it is −0.20 to +0.10.
    - On 16³ and 32³ final lattices it is −0.33(17) to −0.75.
    - It moves away from 0 as the final lattice grows, so it is not stable. Even so, −0.33(17) does not exclude |y| < 0.2.
  - **Odd sector:** there is a +0.37 to +0.65 eigenvalue in a sector that breaks spin rotation. It is close to Δ_φ, which fits the known redundant equation-of-motion direction (suggested). Its coefficient is zero by symmetry.
  - **Complex pairs:** 24 instances. All have |Re y| ≥ 0.47, none has Im y beyond 3σ, and none passes the counting rule. They are artefacts.
- **Level time (M3, checked):** τ_int(|m|²) is 19, 43, 74 and 167 ticks at L = 8, 12, 16 and 24, so z ≈ 2.0. Near the critical point the level-time direction is diffusive, not light-like (light-like would be z = 1).

## Marginal check
- **Proved:** the kernel is invariant under one global spin rotation acting on all contents, and the block map commutes with it. So every coupling that breaks spin rotation is exactly zero at every scale. That covers a magnetic field, the odd sector and cubic spin anisotropy.
- **Comparator:** at the O(3) critical point, cubic anisotropy is nearly marginal, y ≈ +0.01 (Hasenbusch–Vicari 2011; Chester et al. 2021). In this model its starting value u0 is 0.
- **Suggested, if a spin–lattice locking were added by hand:**
  - With u0 > 0, the flow goes to another critical point and produces no gap.
  - With u0 < 0, it runs away, and the passage is about 1/(b|u0|) e-folds. So 38.4 e-folds need |u0| ≤ 1/(38.4b), which again is a smallness put in by hand.
- **Suggested:** a shrinking direction, however slow, decays toward the critical point and cannot make a large scale. Only y_t can, and it is fast.

## Readings
- **LC-SPIRAL:** fails.
- **LC-MARGINAL:** not met. M1 cannot see a direction with |y| < 0.1, and in M2 the values near 0 change with lattice size.
- **LC-HYPERBOLIC:** holds for the growing directions. The registered rule also needs ω separated from 0.2, and neither method separates it. **Result: OPEN.**
- **What a hierarchy costs either way:** the distance from criticality must satisfy δ = |β−β_c|/β_c ≤ e^{−38.4·y_t}, which is e^{−56} to e^{−51}, or about 10⁻²⁴ to 10⁻²². β is put in by hand.
- No claim about v.

## What would close it
Either measure ω on lattices of L ≥ 128 with an estimator that cancels the leading correction, or get a cross-family referee to accept the O(3) comparator.

## Files
Everything is in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hierwall/T2/`:
- `PREREG.md`, with the two dated addenda
- Simulator: `lc.c`
- Run scripts: `stage1.sh`, `stage2.sh`, `stage3.sh`
- Analysis scripts:
  - M0: `m0.py`
  - M1: `fss.py`, `rbar.py`, `omega.py`
  - M2: `mcrg.py`, `mcrg_summary.py`, `mcrg128.py`
  - M3: `m3.py`
- Outputs: `m0.out`, `m3.out`, `fss.out`, `rbar.out`, `omega.out`, `mcrg.out`, `mcrg_summary.out`, `mcrg128.out`
- Raw data (132 MB): `data/`

Peak memory was 237 MB, in the L=128 run. Runs went one at a time, all under the cap. Nothing is left running, and nothing outside the folder was edited.