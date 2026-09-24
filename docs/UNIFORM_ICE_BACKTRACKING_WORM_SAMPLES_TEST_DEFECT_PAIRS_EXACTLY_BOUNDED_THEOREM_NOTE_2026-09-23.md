---
claim_id: uniform_ice_backtracking_worm_samples_test_defect_pairs_exactly_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "A worm on the divergence-free arrows of uniform ice that starts at a uniformly random vertex, reverses one of its three outgoing arrows, then moves its head by reversing one of the head's outgoing arrows chosen uniformly among all of them (the one just reversed included), and stops when the head returns to the start, carries between start and stop exactly two defects: the start, of divergence -2, and the head, of divergence +2. Head steps have probability 1/4 both ways, creation 1/(3N) and annihilation 1/4, so the chain balances with uniform weight on ice configurations and on two-defect states, the latter at relative weight 4/(3N). The time spent at head-minus-start displacement r is therefore proportional to Z_pair(r), the number of two-defect configurations with that displacement, and V(r) = -ln Z_pair(r) + const is the test-defect pair free energy on any torus. On the exact L = 2 torus, all 2^24 arrow patterns give 307968 two-defect patterns at seven displacements, and the worm reproduces the normalised counts within 4 standard errors (largest 2.81) together with the ice measure's <W^2> = 76/25; the loop worm that never reverses the arrow just reversed, whose chain is doubly stochastic once the last reversed arrow is part of the state, reproduces them too (largest 2.21). Compared with the Gaussian prediction K Q^2 (G(r') - G(r)), Q = 2, K = 2/3 + 1/(3N), G the torus Green's function of the Z^3 graph Laplacian: on L = 8 with 2 x 10^6 worms, relative to the nearest pair, measured over predicted is 0.915 to 0.969 at ten separations (errors 0.008 to 0.014); on L = 16 with 10^6 worms, along the axis for r = 2 to 8, it is 0.960 to 0.986 (errors 0.011 to 0.017). The pair attracts. No limit beyond the sampled sizes is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_backtracking_worm_samples_test_defect_pairs_exactly_2026_09_23.py
---

# Uniform ice: a backtracking worm samples test-defect pairs exactly, and on tori their free energy follows the lattice Green's function

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8875 found that two test
defects in the layer measure of uniform ice interact through the lattice
Green's function at the flux-cost stiffness, on prisms of cross-section 4 ×
4 and 2 × 8. Transfer matrices cannot reach the 1/r regime. This block
records a sampler that can: its intermediate states are the two-defect
ensemble itself. The result is less precise than the prisms, and it is
preserved here with its precision stated.

## Result up front

1. **The sampler.** A worm on the divergence-free arrows starts at a
   uniformly random vertex and reverses one of its three outgoing arrows.
   It then moves its head: at every step it reverses one of the head's
   outgoing arrows, chosen uniformly among all of them, including the one
   just reversed. It stops when the head returns to the start. In between,
   the configuration carries exactly two defects: the start, with
   divergence −2 (two arrows out, four in), and the head, with divergence
   +2.

2. **The identity.** Head steps have probability 1/4 forwards and
   backwards. Creation has probability 1/(3N) and annihilation 1/4. The
   chain on ice configurations and two-defect states therefore balances
   with uniform weight on each, the two-defect weight being 4/(3N)
   relative to an ice configuration. So the time the worm spends at
   head-minus-start displacement r is proportional to Z_pair(r), the number
   of two-defect configurations with that displacement. Its logarithm is
   the test-defect pair free energy, V(r) = −ln Z_pair(r) + const, on any
   torus and without a transfer matrix. The loop worm of open PR 8881,
   which never reverses the arrow just reversed, satisfies the same
   identity once its last reversed arrow is kept as part of the state.
   Every such state then has three successors and three predecessors, each
   with probability 1/3, so the chain is doubly stochastic and balances
   with uniform weight too.

3. **The exact control.** On L = 2, all 2^24 arrow patterns give 307968
   two-defect patterns at the seven displacements. The worm reproduces
   their normalised counts within 4 standard errors (the largest is 2.81)
   and the ice measure's ⟨W²⟩ = 76/25. The loop worm reproduces the same
   counts (largest deviation 2.21 standard errors).

4. **The pair free energy on tori.** The Gaussian prediction is
   V(r) − V(r′) = K Q² (G(r′) − G(r)), with Q = 2, K = 2/3 + 1/(3N) (open
   PR 8881) and G the torus Green's function of the Z^3 graph Laplacian.
   Measured over predicted, relative to the nearest pair:

   | torus | worms | separations | ratio | standard errors |
   |---|---|---|---|---|
   | L = 8 | 2 × 10^6 | ten, out to (4, 4, 4) | 0.915 to 0.969 | 0.008 to 0.014 |
   | L = 16 | 10^6 | axis, r = 2 to 8 | 0.960 to 0.986 | 0.011 to 0.017 |

   The pair attracts, and the free energy rises with distance.

5. **What this means.** Test defects on tori interact through the lattice
   Green's function at the sum-rule stiffness out to r = 8 on L = 16,
   which is well into the 1/r regime, with the measured differences 1.4%
   to 4% below the Gaussian's there. The nearest pair sits slightly above
   the Gaussian line: it is less bound than a point charge pair would be,
   a contact effect of the defect's core. This extends open PR 8875 from
   prisms to tori. It is less precise: the prisms reach 1% beyond distance
   2, and the tori about 3%, because each worm's visits near its start are
   heavy-tailed. No constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_backtracking_worm_samples_test_defect_pairs_exactly_2026_09_23.py`
- **Result:** `TOTAL: PASS=5 FAIL=0`, about 154 s, stdout 1315 characters,
  peak about 560 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_backtracking_worm_samples_test_defect_pairs_exactly_2026_09_23.txt`
- **Arithmetic:** exact integer enumeration on L = 2; seeded sampling
  (numba's generator, fixed seeds) with jackknife errors over 20 bins; the
  torus Green's function by FFT with the zero mode removed.

## Premises and declared objects

- **Uniform ice** as divergence-free arrows on the cubic torus.
- **Backtracking worm** as stated, with fixed seeds.
- **Test defects:** vertices of divergence ±2, a probe only.
- **Comparison field:** the Gaussian divergence-free field with the Z^3
  graph Laplacian of the landed note
  `LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`;
  K = 2/3 + 1/(3N) as in open PR 8881.

## Prior art and what is new

- Open PR 8875: test defects on prisms by layer transfer.
- Open PR 8881: the loop worm and the sum-rule stiffness.
- The landed note
  `SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md`
  fitted charge-pair energies of a supplied quantum Hamiltonian; this
  note measures the entropic free energy of the static measure, with
  nothing fitted.
- New here: the exact identity between the intermediate states of both
  worms and the two-defect ensemble; its exact L = 2
  check; the pair free energy on tori out to r = 8.

## Theorem — The identity and the sampled tori

The backtracking worm's chain balances as stated, so its displacement
histogram is proportional to Z_pair. On L = 2 the counts are exact. On L = 8
and L = 16 the sampled ratios are as stated with their standard errors. No
limit is claimed beyond the sampled sizes.

## No-Go Discipline Gate

- **N1 alternative routes.** Improved estimators with lower variance near
  the start are the direct extension.
- **N2 wall independence.** The exact L = 2 counts check the identity; the
  prediction uses the stiffness of open PR 8881, not these data.
- **N3 hidden walls.** Worm-to-worm fluctuations near the start are
  heavy-tailed; the errors come from jackknife over bins.
- **N4 residual matching.** Nothing is fitted; the offsets are reported.
- **N5 rhetoric audit.** "Follows the lattice Green's function" means the
  stated ratios with their errors.
- **N6 partial-closure paths.** Larger tori; references beyond the nearest
  pair; lower-variance estimators.
- **N7 steelman.** Against: the ratios sit a few percent below 1. For:
  they are flat from r = 2 to 8 on L = 16, as a contact offset would be.
  Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8875 and 8881 and the landed notes are
  cited.

## Falsifiers

- An L = 2 displacement at which the worm departs from the exact count by
  more than 4 standard errors.
- A sampled separation outside the stated range of ratios.

## Boundaries and non-claims

- Tori of side 2 (exact), 8 and 16 (sampled).
- Test defects are a probe; none is admitted into the rule.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, open PRs 8875 and 8881, and the landed notes are
cited. No audit grade, no new axiom, no new primitive, no new comparator
and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Provenance.** This experiment was first set aside as too noisy
  (prototype errors of 15% to 25% on L = 16 with 10^5 worms). It is
  preserved here, with 10 times more worms and jackknife errors, because
  it carries an exact identity and reaches the 1/r regime.
- **Independence sources:** the exact L = 2 two-defect counts; the
  prediction from the sum-rule stiffness.
- **Correction before landing.** A draft stated that excluding the arrow
  just reversed breaks the identity. The exact L = 2 counts refuted it,
  and the doubly stochastic argument above explains why. Both worms are
  now checked.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| head never takes one of its four arrows | worm made non-uniform | caught (3 FAILs) |
| charge 1 in place of 2 | prediction changed | caught (2 FAILs) |
| stiffness halved | prediction changed | caught (2 FAILs) |
| enumeration misses one in-link | control changed | caught (3 FAILs) |
| biased step choice | worm made non-uniform | caught (4 FAILs) |
| worm stops one step early | defects left behind | caught (nonzero exit) |
| loop worm excludes forward links only | exclusion made asymmetric | caught (1 FAIL) |

  7 of 7 are caught.
- **Vacuity guard:** the exact counts, every ratio with its error and the
  control statistics are printed.
- **Budget:** 5 checks, stdout 1315 characters (ceiling 6000), about 154 s
  (ceiling 900 s), peak about 560 MB.

## Verification

```bash
python3 scripts/uniform_ice_backtracking_worm_samples_test_defect_pairs_exactly_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=5 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_backtracking_worm_samples_test_defect_pairs_exactly_2026_09_23.txt`.
