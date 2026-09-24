---
claim_id: uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Uniform ice on the L x L x L torus puts divergence-free arrows E_i = +-1 on the links; S_ij(k) = <F_i F_j^*>/N is its equal-time correlation tensor, with F_i(k) = sum_r e^(-ik.r) E_i(r). Divergence-freedom makes S annihilate conj(s), s_i = 1 - e^(-ik_i). A Gaussian divergence-free field with stiffness K has S = P/K, P the transverse projector, so its two transverse polarizations carry the same eigenvalue 1/K. On the exact L = 2 torus (all 9600 configurations): S annihilates s at every k, (1/N) sum_k S_zz = 1 exactly, the polarizations at (pi, pi, pi) are degenerate (87/75), and at (pi, pi, 0) they split, 86/75 against 114/75. The worm sampler of open PR 8881 reproduces all 72 entries of that exact tensor within 4 standard errors. On L = 8 with 2 x 10^6 worms: the longitudinal null holds at every k (residual 2.6e-13), and both transverse eigenvalues lie within 1% of 1/K_L at every k (K_L lambda in [0.9934, 1.0088], K_L = 2/3 + 1/(3N)). Where symmetry forces degeneracy, at the 28 axial and body-diagonal wavevectors, the tensor on a fixed real transverse basis is a multiple of the identity in all 84 linear tests (largest 1.94 standard errors). The largest split of the sorted eigenvalues anywhere, an upward-biased and so conservative estimate, is 0.60% +- 0.04% at (1, 3, 4) 2pi/8; at (pi, pi, 0) it is 0.55% +- 0.13%, against 28/75 on L = 2. No limit beyond the sampled sizes is claimed. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_2026_09_23.py
---

# Uniform ice: the static photon has two degenerate transverse polarizations with one stiffness

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. Open PR 8881 found on tori up to
side 24 that the diagonal correlation S_zz of uniform ice matches the
Gaussian projector with the sum-rule stiffness within 1%. A photon has
more than one component, so this block tests the whole correlation
tensor: the longitudinal null, both transverse polarizations, and whether
they share one stiffness.

## Result up front

1. **The tensor and what a Gaussian field predicts.** On the L × L × L
   torus, uniform ice carries divergence-free arrows E_i = ±1 on the links.
   With F_i(k) = Σ_r e^(−ik·r) E_i(r), the equal-time correlation tensor is
   S_ij(k) = ⟨F_i F_j^*⟩/N. The divergence is Σ_i s_i F_i with
   s_i = 1 − e^(−ik_i), so S annihilates conj(s): a longitudinal null. A
   Gaussian divergence-free field with stiffness K has S = P/K, with P the
   transverse projector. Its two transverse polarizations therefore share
   one eigenvalue, 1/K.

2. **The smallest torus, exactly.** On L = 2, over all 9600
   configurations:
   - S annihilates s at every wavevector, and (1/N) Σ_k S_zz = 1 exactly;
   - at (π, π, π) the two polarizations are degenerate, at 87/75, as
     three-fold symmetry requires;
   - at (π, π, 0) they split: 86/75 in the plane against 114/75 along z.
     No symmetry relates the two there, and the smallest torus is far
     from Gaussian.

   The worm sampler of open PR 8881 reproduces all 72 entries of this
   tensor within 4 standard errors.

3. **L = 8.** With 2 × 10^6 worms:
   - the longitudinal null holds at every k, with residual 2.6e-13;
   - both transverse eigenvalues lie within 1% of 1/K_L at every k
     (K_L λ between 0.9934 and 1.0088), with K_L = 2/3 + 1/(3N).

4. **Degeneracy.** At the 28 axial and body-diagonal wavevectors, symmetry
   forces the two polarizations to be degenerate. The tensor on a fixed
   real transverse basis is a multiple of the identity there in all 84
   linear tests (largest 1.94 standard errors). These tests are linear in
   the data, so noise does not bias them.

5. **Splits elsewhere.** The largest split of the sorted eigenvalues is
   0.60% ± 0.04%, at (1, 3, 4) 2π/8. Sorting biases a split upward, so this
   is a conservative bound. At (π, π, 0), the wavevector where L = 2 splits
   by 28/75, it is 0.55% ± 0.13%.

6. **What this means.** The static photon of uniform ice has two
   transverse polarizations, a longitudinal null that is exact, and one
   stiffness for both, within 1% at every wavevector on L = 8. The large
   polarization split of the smallest torus is a finite-size effect: at the
   same wavevector it falls from 28% of the mean on L = 2 to about half a
   percent on L = 8. With open PRs 8869, 8871 and 8881, the static field
   seen by formation units is a two-polarization Gaussian photon with its
   stiffness fixed by the unit link field. No constant is compared with an
   outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_2026_09_23.py`
- **Result:** `TOTAL: PASS=6 FAIL=0`, about 139 s, stdout 1042 characters,
  peak about 390 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_2026_09_23.txt`
- **Arithmetic:** exact integer enumeration and exact fractions on L = 2;
  seeded sampling (numba's generator, fixed seeds) with standard errors
  from 20 bins, and jackknife errors for the splits; eigenvalues of the
  Hermitian 3 × 3 tensor at every wavevector.

## Premises and declared objects

- **Uniform ice** as divergence-free arrows on the cubic torus.
- **Worm sampler** of open PR 8881.
- **Correlation tensor** S_ij(k) as defined, and its transverse
  eigenvalues.
- **Comparison field:** the Gaussian divergence-free field, whose
  projector is built from the Z^3 graph Laplacian of the landed note
  `LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`;
  K_L = 2/3 + 1/(3N) as in open PR 8881.

## Prior art and what is new

- Open PR 8881: the diagonal entry S_zz and the winding stiffness.
- The landed note
  `SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`
  sampled zero-flux tori of side 6 to 12 by plaquette moves. It found one
  longitudinal null per covariance matrix and transverse splits up to
  8.4%, including 2% to 4% at axial momenta, where symmetry forces
  degeneracy. Those splits were therefore statistical.
- New here: the exact L = 2 tensor; the full tensor on L = 8 with every
  winding sector; both polarizations within 1% of the sum-rule stiffness at
  every wavevector; unbiased degeneracy tests; and the finite-size fall of
  the zone-boundary split.

## Theorem — The tensor on the computed tori

On L = 2 the stated tensor is exact. On L = 8 the sampled tensor satisfies
the stated null, eigenvalue range, degeneracy tests and split bounds with
the stated errors. No limit is claimed beyond the sampled sizes.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger tori and longer runs are the direct
  extension.
- **N2 wall independence.** The exact L = 2 tensor checks the sampler; the
  degeneracy tests are linear and unbiased.
- **N3 hidden walls.** Sorted-eigenvalue splits are biased upward; the
  note uses them only as upper bounds.
- **N4 residual matching.** Nothing is fitted.
- **N5 rhetoric audit.** "Degenerate" means the stated tests where symmetry
  requires it, and "within 1%" elsewhere.
- **N6 partial-closure paths.** Whether the zone-boundary split is
  exactly zero in infinite volume; the tensor at larger L.
- **N7 steelman.** Against: splits of about half a percent remain at
  wavevectors without a degeneracy symmetry. For: they are conservative
  bounds, and the one comparable point fell from 28% to 0.55% between L =
  2 and L = 8. Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8869, 8871 and 8881 and the landed RK
  note are cited.

## Falsifiers

- A wavevector on L = 8 with a transverse eigenvalue more than 1% from
  1/K_L.
- An axial or body-diagonal wavevector whose transverse block departs from
  a multiple of the identity by more than 4 standard errors.

## Boundaries and non-claims

- The exact L = 2 torus and the sampled L = 8 torus.
- No limit beyond the sampled sizes is claimed.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, open PRs 8869, 8871 and 8881, and the landed RK and
lattice-Green notes are cited; the comparison field is built from the
framework's Z^3 graph Laplacian. No audit grade, no new axiom, no new
primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the exact L = 2 tensor; the linear degeneracy
  tests; the closed-form projector.
- **Correction before landing.** A first version tested degeneracy on the
  sorted eigenvalues. Noise biases their difference upward, so symmetric
  classes showed a spurious 4.9-standard-error split. The test now uses the
  tensor on a fixed transverse basis, which is linear in the data.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| biased step choice | worm made non-uniform | caught (4 FAILs) |
| tensor without the conjugate | S not Hermitian | caught (2 FAILs) |
| null tested against s in place of conj(s) | null vector changed | caught (1 FAIL) |
| sum rule over half the wavevectors | normalisation changed | caught (1 FAIL) |
| body-diagonal basis not transverse | basis changed | caught (1 FAIL) |
| axial basis includes the longitudinal axis | basis changed | caught (1 FAIL) |
| enumeration misses one in-link | control changed | caught (2 FAILs) |
| worm stops one step early | defects left behind | caught (nonzero exit) |

  8 of 8 are caught.
- **Vacuity guard:** the exact fractions, the eigenvalue range, the
  largest test statistic and the splits with errors are printed.
- **Budget:** 6 checks, stdout 1042 characters (ceiling 6000), about 130 s
  (ceiling 900 s), peak about 390 MB.

## Verification

```bash
python3 scripts/uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_2026_09_23.txt`.
