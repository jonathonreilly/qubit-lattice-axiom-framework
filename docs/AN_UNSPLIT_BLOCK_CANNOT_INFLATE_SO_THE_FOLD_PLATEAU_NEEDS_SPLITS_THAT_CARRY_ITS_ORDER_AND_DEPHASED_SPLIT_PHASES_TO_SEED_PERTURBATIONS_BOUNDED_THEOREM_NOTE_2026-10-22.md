---
claim_id: an_unsplit_block_cannot_inflate_so_the_fold_plateau_needs_splits_that_carry_its_order_and_dephased_split_phases_to_seed_perturbations_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's tied lapse, edge-register window [L/8, 2^(1+Delta) L], 4s split trigger and passing (vacuum to vacuum, each excitation to the same), with the bare-axis-hop nested sea's Hartree density-wave fold (spinless NN repulsion g) as the plateau: (A) exact: an unsplit block's edges span (4+Delta) ln2 e-folds, so 60 e-folds need Delta >= 82.6; but with the tied lapse the plateau is V0 per site per tick, and read in the vacuum's own units aH stays constant (zero horizon exits for any stretch); with G fixed in proper units rho ~ a^-4. Generally a fixed site set with per-site energy ~ l^p (p <= 0) has w = -p/3 >= 0, so e-folds need new sites: 86.6 split generations during the plateau. (B) Without order carriage a split gives children zero overlap with the fold coordinate (x = 1): no exit, and no folded vacuum survives any later split. Carrying each order with its total momentum makes friction impulsive (mean drift 27 ln2/14), and the plateau attractor is friction-blind: P(N) = V0 N^2/(12 pi^2 mu^2) for any friction factor. (C) Computed V and cranking mass give n_s = 1 - 2/N; with the rung FITTED to A_s (18.4 at g = 0.5, 20.2 at g = 1), the matching condition gives N* = 46.8-47.4, so n_s = 0.957 (-1.8 sigma Planck, -5.6 sigma ACT+DESI), r = 5e-18, running -9e-4. (D) The register's passing is adiabatic for every mode and the tick is static in cell units, so the vacuum seeds no perturbation (superhorizon variance x1/4 per split; A_s = 0). Carrying the order field's configuration through synchronized splits gives |beta|^2 = 9/16 per sub-horizon mode per split and a ln2-periodic spectrum (first harmonic 1.3). With split phases dephased by sigma, the modulation is 0.81, 0.30 and 0.007 at sigma = 0.1, 0.2 and 0.35 e-folds, with mean power 1.2-1.3 times Bunch-Davies; the laws' Poisson estimate gives sigma = 0.07-0.10. (E) The amplitude mode at D* sits 1.19 times above the pair edge 2D*; the folded-vacuum standard gives the plateau departure V0. (F) The 4s trigger is untouched: H a = 2.3e-13. Supplied: g, the fold rung (FITTED to A_s), J a = sqrt3, M_P a = 1, Hartree, instant reheating, g_* = 106.75, mode speed 1, the dephasing sigma (scanned)."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/an_unsplit_block_cannot_inflate_so_the_fold_plateau_needs_splits_that_carry_its_order_and_dephased_split_phases_to_seed_perturbations_2026_10_22.py
---

# An unsplit block cannot inflate, so the fold plateau needs splits that carry its order, and dephased split phases to seed perturbations

Claim type: bounded_theorem. The candidate-law register has zero premise weight, and the axioms are unchanged.

## Where this starts

The fold-inflaton and nested-prefold-sea notes found three things:
- The density-wave fold of the bare-axis-hop (nested) sea is a Starobinsky-class plateau.
- A split cannot pass the fold, so the children are born unfolded.
- The friction needs CL-3's vacuum standard to be read from the folded vacuum.

The candidate tested first is: "the universe begins as one block with the pre-role nested sea, and no block splits until its fold completes", so that inflation happens inside one unsplit block and the passing problem never comes up. Measured values: n_s = 0.9649 +- 0.0042 (Planck), 0.974 +- 0.003 (ACT with DESI), A_s = 2.1e-9, r < 0.036.

## A. The candidate fails for every Delta

**A1 [T]. Window.**
- An unsplit block's edges run from the floor to the top of the window, which is (4 + Delta) ln2 e-folds; from birth at flat length to the top it is (1 + Delta) ln2.
- At Delta = 0 that is only 2.77 e-folds. 60 e-folds would need Delta >= 82.6 (from the floor) or 85.6 (from birth), plus a new clause holding the 4s trigger.
- When the hold is released, children start at the parent's value minus s, which is still at least 4s, so 86 generations split in a burst.

**A2 [T]. Dilation gauge.**
- Under the tied lapse the tick's proper time scales with the cell, so the plateau is V0 per site per tick and rho ~ V0/l^4.
- Read in the vacuum's own units (CL-3, with M_P l = 1), G ~ l^2 and H l is constant. So aH is constant, and there are zero horizon-exit e-folds however far the edges stretch. Uniform stretching is the register's "uniform dilation is a common whole shift": pure relabelling.
- With G held fixed in proper units instead, rho ~ a^-4 (radiation), and aH falls by e^-60.

**A3 [T]. General no-go.**
- Take a fixed set of sites whose per-site energy scales as l^p, with p <= 0 for bounded energy per tick (p = -1 under the tied lapse). Then w = -p/3 >= 0, and acceleration needs w < -1/3.
- So e-folds need new sites: 60 e-folds are 86.6 split generations, and they must happen during the plateau.

Verdict: the unsplit-block rule cannot inflate. Bending the window or Delta does not help, so the passing problem cannot be avoided.

## B. The split must carry the order

**B1 [T]. What happens without carriage.**
- Site-zone passing gives a parent staggered order zero overlap with the child's fold coordinate (integer overlap 0; nested-prefold E1). So x = 1, and q = 1/8 + 7x/8 = 1: de Sitter with no exit.
- After reheating, every later split would re-seed V0. So no folded vacuum, which is the vacuum CL-3 needs, survives even one split.
- Order carriage is therefore needed for the fold to exist at all as a lasting vacuum, not just for inflation.

**B2 [T+D]. Impulsive friction.**
- In cell units the tick is static between splits.
- If the split carries the order's total momentum, it divides the order's velocity by 8 at each split. The mean drift is then 3 ln2 (f/(1-f) + 1/2) with f = 1/8, which is 27 ln2/14 = 1.337 times -V'/3H (stepped check 1.338). This rederives nested-prefold D1.

**B3 [T]. The plateau is friction-blind.**
- With friction factor c, N = N_std/c and P = (dN/dchi)^2 H^2/4pi^2 = V0 N^2/(12 pi^2 mu^2) (sympy). This does not depend on c.
- So n_s(N), r(N) and A_s(N) are the same for impulsive and continuous friction, at leading slow-roll order.

## C. Numbers from the computed potential

**C1 [T+D].** Rederived: the gap equation 1 = 3g int rho/E has a solution at every g > 0, the cranking pole is M -> rho0/(12 D^2) (rho0 = 0.14267), and W ~ D^2 ln^2(1/D). D* = 0.641 at g = 0.5 and 2.300 at g = 1.

**C2 [D]. Slow roll at N* = 55.** n_s = 0.9636 = 1 - 2/N. eps reaches 1 long before D*, which is the graceful exit.

**C3 [T+E]. Self-consistent N*.**
- Setup: instant reheating, k* = 0.05/Mpc, g_* = 106.75, the Planck-2018 matching formula.
- Results: N* = 47.4 (g = 0.5) and 46.8 (g = 1).
- The rung is FITTED to A_s: 18.4 and 20.2. Then H/M_P = 7.6e-13 and 2.3e-13.
- The low plateau shortens N*, and 55 is not available.

**C4 [E]. Predictions the rule was not built for** (at the self-consistent N*, g = 1):

| Quantity | Rule | Measured | Pull |
|---|---|---|---|
| n_s | 0.9572 | Planck 0.9649 +- 0.0042 | -1.8 sigma |
| n_s | 0.9572 | ACT+DESI 0.974 +- 0.003 | -5.6 sigma (excluded) |
| r | 5e-18 | < 0.036 | passes; prediction: no observable tensors |
| running | -9.1e-4 | -0.0045 +- 0.0067 | consistent |

Delayed or stiff reheating could add up to about 11 e-folds, which still falls short of ACT's N ~ 77.

## D. Perturbations: a new wall and its rule

**D1 [T]. The register's passing seeds nothing.**
- The passing (vacuum to vacuum, each excitation to the children's lowest excitation of the same) maps every mode adiabatically: u -> u/2 and pi -> 2 pi in the instantaneous basis.
- Between splits the tick is static in cell units, so occupations never change. This is a conformally coupled field.
- Superhorizon variance therefore falls by 1/4 per split (2.3e-10 of Bunch-Davies after 16 splits), and A_s = 0 from the vacuum.
- This holds for the inflaton fluctuation under the register as written. It is the mechanism behind the predictions sheet's "scalar seed absent".

**D2 [D]. Order carriage with synchronized splits.**
- The continuum check (smooth a^3 weight) reproduces Bunch-Davies, R = 0.9999.
- Carrying the order field's configuration and total momentum through synchronized splits is sudden. It gives |beta|^2 = 9/16 per sub-horizon mode per split, which heats.
- The frozen spectrum is then 17 times Bunch-Davies on average and saw-toothed with period ln2 in ln k (first harmonic 1.30). That is excluded.

**D3 [D+E]. Dephased splits restore the continuum.** If block split phases are spread by sigma e-folds, a long mode sees the summed cell count:

| Phase spread | Mean power / Bunch-Davies | ln2-periodic modulation |
|---|---|---|
| sigma = 0.1 | 1.78 | 0.81 |
| sigma = 0.2 | 1.17 | 0.30 |
| sigma = 0.35 | 1.27 | 0.007 |
| uniform within one generation | 1.24 | 0.32 |

A modulation below the few-percent log-oscillation bound needs sigma of about 0.35 e-folds or more. The bound is approximate, from the Planck feature search; check it before citing. The rung shift log2(R)/2 is 0.17 or less.

**D4 [E]. The laws do not supply enough dephasing.** The Poisson register estimate (spectral-tilt, m s <= 2034) over the 22-42 levels since a Hubble patch's common ancestor gives sigma = 0.07-0.10, so a dephasing source is still needed.

## E. Exit, reheating, vacuum standard

**E1 [E].** After exit the order oscillates about D*. The amplitude mode's frequency is 5.47, which is 1.19 times the pair edge 2D* = 4.60, so it can decay into the fold sea's quasiparticle pairs (fold-sea matter). Misfolds are at most 0.36 walls per site (fold-inflaton E). Rates are not computed.

**E2 [T].** With CL-3's vacuum read as the lowest state over orders (the folded vacuum), the plateau's departure is V0 (0.1673 per site at g = 1), and it is zero after exit. Lambda stays a separate supplied constant.

## F. Trigger consistency (F1)

Under IN-1 the plateau rides the ordinary 4s trigger: one generation is s steps, which is ln2.
- H a = 2.3e-13 per finest tick, far below the edge-rate cap and inflaton A1's 1.93e-5.
- That is about 3e12 ticks per split, with 68 generations within N*.
- The window and Delta are unchanged.

## Rule text (proposed, tested)

> IN-1 (order carriage; amends CL-1's passing). "An update's vacuum is its lowest state at its block's orders: the orders are the site averages of the odds that the update's interaction makes nonzero, and the vacuum at given orders has every negative-quasi-energy mode of the tick, with the mean fields at those orders, filled. The passing carries a block's vacuum at its orders, and each order's total momentum, onto the children's vacuum at the same orders, read in the children's own cells."

> IN-2 (vacuum standard; CL-3 reading). "The vacuum CL-3 measures departures from is the update's lowest state over all orders."

> Pre-role sea (nested-prefold clause, kept). "While a block of rung r_f is unfolded, its role sites tick with the bare axis hop and nearest-neighbour repulsion g."

> IN-3 (dephasing). Needed, not supplied: split phases must be spread by at least about 0.35 e-folds within a Hubble patch. A candidate source is "the first odds spread each block's edge registers over one register octave". It is UNTESTED: a spread of one generation alone gives modulation 0.32 (D3), not enough, and whether the coupled trigger keeps or erases an initial spread is not computed.

Reasons:
- IN-1 is the minimal completion of the passing clause, which needs a quadratic tick to define "negative-quasi-energy modes". For an interacting update that quadratic tick is the mean-field tick at the current orders.
- Without IN-1, no condensate of the sea (the folded vacuum, or any staggered-density Dirac-mass condensate) survives a split (B1).
- IN-1 is symmetric: no lopsided choice, and the Z2 sign of the order is carried.

## Anti-smuggling gate (owner 2026-10-22)

1. Measured numbers chosen: the fold rung (18.4 or 20.2) is FITTED to A_s, and the coupling g is supplied. N* is NOT chosen: it is computed from the plateau height. The dephasing sigma is a requirement read off measurement (the modulation bound), not a fitted parameter, and is not supplied by the rules.
2. Observed structure inserted by name: none. IN-1 and IN-2 speak only of sites, odds, orders (site averages) and the passing. The rung r_f is a supplied scale (a role-layout number).
3. Predictions not built for:
   - n_s = 0.957 at the computed N*: -1.8 sigma Planck, -5.6 sigma ACT+DESI, so it FAILS ACT+DESI;
   - r = 5e-18 (no detectable tensors);
   - running -9e-4 (consistent);
   - D1: A_s = 0 under the register as written (a failure of the register, now explained);
   - D2: an O(1) ln2-periodic spectral sawtooth for synchronized splits, excluded.
4. Axiom bent:
   - IN-1 and IN-2 are CL-level and bend no axiom beyond the split's existing Lattice departure.
   - The pre-role rung-r_f sea uses the role layout, which is the recorded Lattice departure ("no site is privileged").
   - The unsplit-block candidate would have needed Delta >= 82.6 and a trigger hold; it is rejected.

Gate verdict: IN-1 and IN-2 pass items 2 and 4. On item 1, A_s is FITTED. On item 3 the rule makes testable predictions: it passes Planck at 1.8 sigma, fails ACT+DESI at 5.6 sigma, and needs the unsupplied IN-3 to give any A_s at all. As a full inflation rule it is reported as INCOMPLETE and FAILING against ACT+DESI. It is not adopted.

## Smuggling review

Supplied:
- g, the fold rung (FITTED);
- J a = sqrt3;
- M_P a = 1;
- the Hartree reading;
- instant reheating and g_* = 106.75 (for N*);
- mode speed 1;
- the dephasing sigma (scanned; mean-field summed cell count as the long mode's inertia);
- the Poisson register model (D4 only).

Forced, given those:
- the window arithmetic;
- the dilation gauge and the fixed-site no-go;
- the B1 re-seeding;
- the 27 ln2/14 drift;
- friction-blindness;
- n_s = 1 - 2/N;
- N* of about 47;
- the adiabatic no-seed theorem;
- 9/16 heating per synchronized split;
- the D3 modulation numbers.

Not computed:
- the 3D star or fold selection;
- the coupling of the rung-r_f fold sea to finest-rung matter, and reheating rates;
- whether the coupled trigger keeps an initial phase spread;
- quantum diffusion near the top;
- the face-phase switch from the nested to the Dirac sea (nested-prefold B; not needed here, because the fold sea is a separate rung-r_f sea).

## Dependencies

- Used: fold-inflaton (#9979; C5 re-seeding, E misfolds); nested-prefold-sea (#9982; C potential, D1 friction, E1 overlap); pi-flux-fold (#9986; face phases stay fixed, no Stokes issue); spectral-tilt (Poisson spread, n_s - 1 = log2 lam); record-clock-tilt (no record clock); act-tilt (#9918; every exponential plateau gives 1 - 2/N); inflaton A1.
- Narrows: the owner's candidate that inflation happens in one unsplit block (refuted, A), and the nested-prefold claim that the passing must "write the clock" (IN-1 is the vacuum clause completed, B1).

## How to run

python3 scripts/an_unsplit_block_cannot_inflate_so_the_fold_plateau_needs_splits_that_carry_its_order_and_dephased_split_phases_to_seed_perturbations_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120. It takes about 6 s, peaks at about 137 MB, prints 5629 characters and ends with TOTAL: PASS=17 FAIL=0. It was checked through scripts/runner_cache.execute_runner from a temporary origin/main worktree (status ok, exit 0).
