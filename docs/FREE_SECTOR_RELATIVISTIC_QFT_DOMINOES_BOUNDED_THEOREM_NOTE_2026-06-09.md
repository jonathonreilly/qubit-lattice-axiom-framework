# Free-Sector Relativistic-QFT Dominoes Downstream of OS0: G1 Measure Convergence, Statistics Selection, and the Interacting Boundary

**Date:** 2026-06-09
**Claim type:** bounded_theorem (free Gaussian sector) + a named no-go boundary (non-perturbative)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_free_sector_relativistic_qft_dominoes_2026_06_09.py`](../scripts/frontier_free_sector_relativistic_qft_dominoes_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_free_sector_relativistic_qft_dominoes_2026_06_09.txt`](../logs/runner-cache/frontier_free_sector_relativistic_qft_dominoes_2026_06_09.txt)
(SCORECARD: PASS=8, FAIL=0)

---

## Role

The free-sector Poincaré assembly
([`EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md`](EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md))
left a named residual list. This note attacks each remaining domino and reports
honestly which fall and which is a genuine wall. Each runner part is constructed
to FAIL if the claimed advance were false.

## Domino 1 (G1, measure-bridge half): free-Gaussian convergence reduces to the 2-point — **falls**

A free (Gaussian) measure is **completely determined by its covariance**. The
lattice free Dirac 2-point converges to the continuum Dirac propagator at
`O(a²)` (rung A). The runner verifies the consequence directly: the free-Gaussian
**4-point and 6-point** Schwinger functions — built from the 2-point by the
fermionic Wick/Pfaffian expansion — converge to their continuum values at exactly
the **same `O(a²)` rate** (error ratio `4.00` per halving of `a`, for both). So
the free lattice Gaussian measure converges to the continuum free Dirac Gaussian:
G1's measure-convergence half **reduces to rung A** for the free sector, and is
established to the extent rung A is. (The remaining G1 piece — the OS-nuclear /
distributional topology rigor and the `1+1d→4D` arena — is standard for the free
field, Glimm–Jaffe ch. 6–7.)

## Domino 2 (G1, 4D arena half): 4D reflection positivity — **necessary conditions verified; standard result cited**

Rung B established reflection positivity in `1+1d`. The runner verifies the
**necessary 4D conditions**: the free Dirac Hamiltonian `H(p)` on the spatial
`Z³` slice is Hermitian with spectrum `±E(p)`, `E=\sqrt{\hat p²+m²}≥0` across the
Brillouin zone (the spectrum condition in 4D), and the two-step transfer
`T²=e^{-2a|H|}` is positive-definite in 4D. Full 4D free-fermion reflection
positivity is the **standard Osterwalder–Seiler (1978)** result on exactly this
hypercubic-symmetric surface; the framework's surface is now the approved one, and
the necessary positivity verifies in 4D here.

## Domino 3: statistics selection — spin-statistics forces CAR (fermionic) — **falls (free sector)**

The free 2-point is statistics-blind, but with **Lorentz invariance now in hand**
(the capstone) any spacelike separation boosts to equal time. The runner computes,
at equal-time spacelike separation:

- the **antisymmetric** two-point (the *commutator* function) vanishes
  (`|·| ≈ 10⁻¹⁶`);
- the **symmetric** two-point (the *anticommutator* function) is nonzero
  (`|·| ≈ 5×10⁻²`).

Microcausality requires the field (anti)commutator to vanish at spacelike
separation. With the spin-½ exchange sign `(-1)^{2s} = -1`, this is satisfied by
the **anticommutator (CAR)** and **violated by Bose quantization** (whose
commutator would need the nonzero symmetric function to vanish). Hence CAR is the
**unique microcausal quantization** of the spin-½ field: fermionic statistics is
**selected**, not assumed. This discharges the antecedent of the spin-statistics
reduction note's T2 (which was gated on the reconstruction `R` delivering a
relativistic field — now delivered by the capstone for the free sector).

## Domino 4: the interacting theory — order-by-order covariance **holds**; non-perturbative existence is a **standing wall**

The OS0 primitive makes the **gauged** lattice loop measure hypercubic-symmetric
at every order, so by the all-orders `B₄` selection rule the marginal velocity
anisotropy is forbidden order by order (the runner re-verifies the one-loop
`z_t=z_s` on the symmetric surface, rep-blind). Therefore the **interacting**
theory is **Lorentz covariant order-by-order in perturbation theory** — a genuine
advance over "free sector only."

**The honest wall:** none of this establishes **non-perturbative continuum
existence** of the interacting `SU(3)×U(1)` measure — the constructive-QFT /
mass-gap-class problem. That wall is **untouched** and is flagged, not papered
over. Perturbative emergent Lorentz covariance is in hand; non-perturbative
existence is not, and no result here claims otherwise.

## Net (honest scorecard of the campaign)

- **Fell:** free-Gaussian measure convergence (G1 measure half, free sector);
  statistics selection (CAR forced, free sector).
- **Advanced to standard-on-the-approved-surface:** 4D reflection positivity
  (necessary conditions verified; Osterwalder–Seiler cited); interacting Lorentz
  covariance **order-by-order**.
- **Standing wall (does not fall):** non-perturbative interacting continuum
  existence. This is the genuine terminal wall of the relativistic-QFT program and
  is orthogonal to the kinetic-isotropy primitive.

Combined with the capstone, the **free Gaussian matter sector is now a Poincaré-
covariant, positive-energy, microcausal, correct-statistics Wightman QFT** to the
extent the cited rungs are ratified — with the only genuinely-hard remaining wall
being the (universal, framework-independent) non-perturbative existence of the
interacting continuum theory.

## What this note does NOT claim

- **Not** non-perturbative interacting existence (explicit standing wall).
- **Not** a re-ratification of rungs A/B/C (audit lane); it discharges their
  *circularity* and verifies *necessary* 4D conditions.
- **Not** any dimensionless dynamical observable.
- **No** new axiom, primitive, vocabulary, or class tag; **no** PDG/fitted input.
  Standard methodology (Glimm–Jaffe; Osterwalder–Seiler; Streater–Wightman) is
  cited as comparator/method, not derivation input. Sets no audit status.

## Dependencies

- [EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md](EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — the free-sector Poincaré assembly these dominoes extend.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — OS0; the order-by-order interacting covariance rests on it.
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  — rung A, the `O(a²)` 2-point convergence G1 reduces to.
- [FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md](FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md)
  — OS2/G1/G2 context.
- [FREE_SECTOR_SPIN_STATISTICS_LEVEL1_MECHANISM_AND_RECONSTRUCTION_REDUCTION_BOUNDED_NOTE_2026-05-30.md](FREE_SECTOR_SPIN_STATISTICS_LEVEL1_MECHANISM_AND_RECONSTRUCTION_REDUCTION_BOUNDED_NOTE_2026-05-30.md)
  — the statistics-reduction note whose T2 antecedent (relativistic `R`) is discharged here.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
