# Metric-Reparametrized Vertex And Operator-Lift Boundary

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_universal_gr_metric_reparam_operator_lift_boundary.py`](../scripts/frontier_universal_gr_metric_reparam_operator_lift_boundary.py)
**Cached log:**
[`logs/runner-cache/frontier_universal_gr_metric_reparam_operator_lift_boundary.txt`](../logs/runner-cache/frontier_universal_gr_metric_reparam_operator_lift_boundary.txt)

## Statement

For the native elliptic generator

```text
D(q) = i sigma_a sin(q_a) + m,
```

the finite-lattice runner checks three bounded facts.

First, the metric-reparametrized momentum argument

```text
P_eff,a = (sqrt(I + h) . q)_a
```

has first variation matching the conserved velocity-times-momentum stress
vertex used by the two-point stress-Ward packet.

Second, the naive hop-amplitude/vielbein coupling has shear first variation
matching the bare-sigma shear vertex, not the conserved velocity-times-momentum
vertex. In the tested shear sector the two vertices are numerically distinct.

Third, one proposed operator-level lift of the cubic Ward contact fails: for
the tested longitudinal first graviton and transverse second graviton, the
second variation's longitudinal contraction is not a constant multiple of the
corresponding conserved-vertex difference across the sampled loop momenta.

## Boundary

This is a finite-lattice support and boundary note. It does not prove a unique
all-orders metric coupling, does not prove or disprove the loop-integrated
cubic diffeomorphism Ward identity, does not demonstrate an `a -> 0` continuum
limit, does not classify all possible seagull or measure schemes, and does not
derive an Einstein-Hilbert normalization or `G_Newton`.

The negative result is deliberately narrow: the tested clean
operator-proportionality lift fails. Loop-integrated cancellation, an alternate
local completion, a continuum extrapolation, and full nonlinear closure remain
outside this note.

## Load-Bearing Inputs

- [`UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  for the conserved velocity-times-momentum vertex and the earlier distinction
  between conserved and naive stress vertices.
- [`UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  for the exact finite stress-vertex Ward/telescoping support that this note
  does not extend to a clean cubic operator identity.
- [`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the native elliptic Dirac generator used in the finite tests.

## No-Go Discipline Gate

**Gate result:** broad no-go failed; narrowed boundary shipped. The submitted
claim that the cubic Ward is intrinsically loop-level/continuum-only was not
landed.

- **N1 alternative routes:** exact operator proportionality was attempted and
  failed in the runner. Loop-integrated cancellation, alternate seagull or
  measure completion, explicit continuum extrapolation, and full nonlinear
  closure were not ruled out here.
- **N2 wall independence:** the only landed wall is the tested proportionality
  lift. The loop and continuum questions are independent and remain open.
- **N3 hidden-wall scan:** phrases like "all-orders", "manifest", and
  "expected continuum closure" were removed because they would require
  additional authority.
- **N4 residual matching:** this note matches only the operator-lift residual
  adjacent to the cubic telescoping support; it does not claim to settle the
  full Ward residual.
- **N5 rhetoric audit:** "not an operator identity" was narrowed to "the tested
  operator-proportionality lift fails."
- **N6 partial-closure scan:** a loop-integrated or continuum route could still
  retire the residual without new axioms.
- **N7 steelman:** a hostile reviewer can fairly say the cubic Ward may still
  close after loop integration, regulator subtraction, or continuum
  extrapolation. This source accepts that steelman and does not claim otherwise.
- **N8 cross-cycle echo:** prior GR stress-Ward notes distinguish finite
  operator identities from loop-level/continuum statements; this note preserves
  that distinction.

## Forbidden-Imports Check

No observed value, fitted selector, empirical comparator, new axiom, primitive,
or audit verdict is consumed. The runner verifies finite matrix/lattice
diagnostics only.

## Validation

Run:

```bash
python3 scripts/frontier_universal_gr_metric_reparam_operator_lift_boundary.py
```

Expected: `TOTAL: PASS=3 FAIL=0`.
