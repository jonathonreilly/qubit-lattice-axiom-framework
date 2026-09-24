---
claim_id: uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Conditional on the supplied ring Hamiltonian of the landed cubic-ice notes, H(V) = D - A + (V - 1) N_f, at its RK point V = 1, where H = D - A is a graph Laplacian and the uniform superposition of ice configurations is a ground state of energy 0 whose equal-time law is the uniform ice measure. For O = E_z(k)/sqrt(N), the double commutator gives the f-sum <0|O^+ H O|0> = 2 n_f (s_x^2 + s_y^2), with n_f the density of flippable plaquettes and s_i^2 = 2 - 2 cos k_i; the single-mode bound puts the lowest excitation at momentum k at or below omega_SMA(k) = 2 n_f (s_x^2 + s_y^2)/S_zz(k). On the exact L = 2 torus (9600 configurations, 49920 flips) n_f = 13/60 and the f-sum identity holds exactly at all 8 wavevectors; the worm sampler reproduces n_f within 4 standard errors. On L = 8 with 10^6 worms, n_f = 0.25934 +- 0.00002 and omega_SMA(k)/(2 n_f K_L |s|^2) lies in [0.9914, 1.0083] at every k with P_zz > 0.05 (K_L = 2/3 + 1/(3N), 2 n_f K_L = 0.3461): the bound is quadratic, omega_SMA = 2 n_f K |s|^2 within 1%. On L = 16 at the smallest wavevector, omega_SMA = 0.0531 at |k| = 0.3927, within 0.71% of 2 n_f K_L |s|^2, and from L = 8 to 16 omega_SMA/|k| falls by 0.5227 against the quadratic factor 0.5198 (a linear branch would keep it fixed). No Hamiltonian is adopted, and no limit beyond the sampled sizes is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_2026_09_23.py
---

# Uniform ice at the RK point: the photon's single-mode bound is quadratic with the sum-rule stiffness

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. The assembly's record-dynamics
target carries an open edge: photon dynamics rests on the landed quantum
Hamiltonian, a supplied bridge. Open PRs 8881 and 8890 fixed the static
photon of uniform ice: its equal-time correlations, two polarizations and
one stiffness. That static law is exactly the ground state of the supplied
Hamiltonian at its RK point. This block asks, conditionally, what the
supplied Hamiltonian then implies for the photon's energy.

## Result up front

1. **The supplied Hamiltonian and its ground state.** The landed cubic-ice
   notes supply H(V) = D − A + (V − 1) N_f on the ice configurations. Here
   A flips a flippable plaquette (all four arrows circulating) and D counts
   the flippable plaquettes. At V = 1, the RK point, H = D − A is a graph
   Laplacian. The uniform superposition of ice configurations is then a
   ground state of energy 0, and its equal-time law is the uniform ice
   measure. This block adopts no Hamiltonian; it states what this one
   implies.

2. **The f-sum.** Take O = E_z(k)/√N. For a diagonal O,
   [O^+, [H, O]] = Σ_p |Δ_p O|² T_p, where T_p flips p. An xz or yz
   plaquette changes E_z by ∓2 on its two z links, so
   |Δ_p O|² = 4 s_x²/N or 4 s_y²/N, with s_i² = 2 − 2 cos k_i. Hence

   ⟨0|O^+ H O|0⟩ = 2 n_f (s_x² + s_y²),

   with n_f the density of flippable plaquettes. On the exact L = 2 torus
   (9600 configurations and 49920 flips), n_f = 13/60 and the identity
   holds exactly at all 8 wavevectors. The worm sampler of open PR 8881
   reproduces n_f within 4 standard errors.

3. **The single-mode bound.** The lowest excitation at momentum k has
   energy at most ω_SMA(k) = 2 n_f (s_x² + s_y²)/S_zz(k). With the
   Gaussian S_zz = P_zz/K and P_zz = (s_x² + s_y²)/|s|², the transverse
   factor cancels, and ω_SMA = 2 n_f K |s|²: quadratic in k.

4. **Measured.** On L = 8 with 10^6 worms, n_f = 0.25934 ± 0.00002, and
   ω_SMA(k)/(2 n_f K_L |s|²) lies between 0.9914 and 1.0083 at every k with
   P_zz > 0.05. So the bound is 2 n_f K_L |s|² within 1%, with
   2 n_f K_L = 0.346. On L = 16, at the smallest wavevector (2π/16, 0, 0),
   ω_SMA = 0.0531 at |k| = 0.3927, within 0.71% of that form. From L = 8 to
   L = 16, ω_SMA/|k| at the smallest wavevector falls by 0.5227, against
   the quadratic factor 0.5198. A linear branch would keep it fixed.

5. **What this means.** If the photon's dynamics is the supplied ring
   Hamiltonian at its RK point, the photon is soft. Its lowest excitation
   at small k lies at or below 0.346 |s|², so no linearly dispersing mode
   can be the lowest one there. The coefficient is fixed by uniform ice,
   with no free constant in units of the ring coefficient: the flippable
   density 0.259 times the sum-rule stiffness 2/3. A light-like photon
   needs the supplied Hamiltonian off its RK point, where the landed
   finite-detuning notes use an external phase input. The static photon
   fixed tonight, with its two polarizations and one stiffness, is the RK
   ground state's equal-time law. What it lacks at the RK point is speed,
   not structure. The landed RK note cites a special RK scaling for this
   point; here the quadratic bound is derived from the framework's own
   quantities. No constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_2026_09_23.py`
- **Result:** `TOTAL: PASS=4 FAIL=0`, about 127 s, stdout 870 characters,
  peak about 390 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_2026_09_23.txt`
- **Arithmetic:** exact integer enumeration, the exact flip graph and
  exact fractions on L = 2; seeded sampling (numba's generator, fixed
  seeds) with standard errors from 20 bins; the bound in closed form from
  the sampled n_f and S_zz.

## Premises and declared objects

- **Supplied Hamiltonian:** H(V) = D − A + (V − 1) N_f of the landed
  cubic-ice notes, for example
  `SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md`,
  at V = 1. It is a premise of this conditional statement, not adopted.
- **Ground state:** the uniform superposition of ice configurations, whose
  equal-time law is the uniform ice measure.
- **Single-mode bound:** the variational inequality
  E_1(k) ≤ ⟨0|O^+ H O|0⟩/⟨0|O^+ O|0⟩ for O|0⟩ orthogonal to the ground
  states, as it is at k ≠ 0.
- **Sampler:** the worm of open PR 8881; K_L = 2/3 + 1/(3N) as there.

## Prior art and what is new

- The landed note
  `SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`
  measured the flippable density in the zero-flux sector (0.2601 on L = 8)
  and cited a special RK scaling for the photon at V = 1. The two
  flippable densities differ by 0.3%. They are measured in different sets
  of flux sectors and by different samplers.
- Open PRs 8881 and 8890: the equal-time law and its stiffness.
- New here: the exact f-sum identity; the single-mode bound computed from
  the framework's own static law; its quadratic form with coefficient
  2 n_f K.

## Theorem — The bound on the computed tori

At V = 1 and on the computed tori, the f-sum identity and the single-mode
bound hold as stated, with the stated numbers. The statement is
conditional on the supplied Hamiltonian. No limit is claimed beyond the
sampled sizes.

## No-Go Discipline Gate

- **N1 alternative routes.** The same bound off the RK point needs the
  detuned ground state, which the sampler does not provide.
- **N2 wall independence.** The f-sum identity is checked exactly on L = 2,
  and n_f and S_zz are sampled independently.
- **N3 hidden walls.** The single-mode bound is an upper bound; the true
  lowest energy can only be lower.
- **N4 residual matching.** Nothing is fitted.
- **N5 rhetoric audit.** "Soft" means the stated upper bound; no exact
  dispersion is claimed.
- **N6 partial-closure paths.** Multi-mode bounds; the bound for the
  detuned Hamiltonian.
- **N7 steelman.** Against: an upper bound cannot show a mode is absent
  above it. For: the lowest mode lies below a quadratic, which is what
  "soft" asserts. Both are recorded.
- **N8 cross-cycle echo.** The landed cubic-ice notes and open PRs 8881
  and 8890 are cited.

## Falsifiers

- An exact L = 2 wavevector where the f-sum identity fails.
- A sampled wavevector on L = 8 where ω_SMA departs from 2 n_f K_L |s|² by
  more than 1.5%.

## Boundaries and non-claims

- Conditional on the supplied Hamiltonian at V = 1; nothing is adopted.
- The tori L = 2 (exact), 8 and 16 (sampled).
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, the landed cubic-ice notes (as the source of the
supplied Hamiltonian) and open PRs 8881 and 8890 are cited. No audit grade,
no new axiom, no new primitive, no new comparator and no new framing is
imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the exact L = 2 flip graph; the sampled n_f and
  S_zz; the closed-form bound.
- **Correction before landing.** A first version of the last check asked
  ω_SMA/|k| to halve exactly from L = 8 to 16. On the lattice the quadratic
  factor is |s|²/|k|, which gives 0.5198. The check now compares with it.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| f-sum without the diagonal D | Hamiltonian changed | caught (1 FAIL) |
| f-sum factor 2 dropped | identity changed | caught (1 FAIL) |
| sampled plaquettes read without circulation | n_f changed | caught (1 FAIL) |
| exact plaquette orientation wrong | flip graph changed | caught (nonzero exit) |
| S_zz from the x links | correlation changed | caught (2 FAILs) |
| f-sum weighted by s_z | numerator changed | caught (1 FAIL) |
| biased step choice | worm made non-uniform | caught (3 FAILs) |
| exact flip reverses three links | flip leaves the ice | caught (nonzero exit) |
| worm stops one step early | defects left behind | caught (nonzero exit) |

  9 of 9 are caught.
- **Vacuity guard:** n_f, the bound's range, its value at the smallest
  wavevector and the slope factor are printed.
- **Budget:** 4 checks, stdout 870 characters (ceiling 6000), about 127 s
  (ceiling 900 s), peak about 390 MB.

## Verification

```bash
python3 scripts/uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=4 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_2026_09_23.txt`.
