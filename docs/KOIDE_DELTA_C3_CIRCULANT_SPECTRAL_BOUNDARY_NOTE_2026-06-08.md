# Koide Delta C3 Circulant Spectral Boundary Note

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:**
[`scripts/koide_delta_c3_circulant_spectral_boundary_2026_06_08.py`](../scripts/koide_delta_c3_circulant_spectral_boundary_2026_06_08.py)
**Cached log:**
[`logs/runner-cache/koide_delta_c3_circulant_spectral_boundary_2026_06_08.txt`](../logs/runner-cache/koide_delta_c3_circulant_spectral_boundary_2026_06_08.txt)

## Purpose

This note preserves the supported algebra from the submitted Koide-delta
packet while removing the global closure/admission claim.

The bounded setting is the Hermitian `C_3` circulant

```text
M = a I + b C + bbar C^2,        b = |b| exp(i delta),
lambda_k = a + 2 |b| cos(delta + 2 pi k/3).
```

Within that setting, the runner verifies a spectral boundary: symmetric
spectral quantities depend on the phase only through `u = cos(3 delta)`;
the determinant and `Tr log|M|` are monotone in `u`; and the
squared-Vandermonde discriminant has its interior extremum at `u = 0`
(`delta = 30 degrees`), not at the Brannen comparator `delta = 2/9`.

## Supported Result

The runner verifies:

- `e1 = 3a` and `e2 = 3(a^2 - |b|^2)` are phase-independent.
- `e3 = det(M) = a^3 - 3a|b|^2 + 2|b|^3 cos(3 delta)`.
- Power sums tested through `p6` are invariant under the stabilizers of
  `cos(3 delta)`, consistent with the elementary-symmetric collapse.
- `det(M)` and `Tr log|M|` are monotone in `u` on the positive cone, so their
  phase-stationary points occur at `sin(3 delta) = 0`, the degenerate boundary.
- The spectrum is even under `delta -> -delta`, so spectral data does not fix
  orientation.
- The squared-Vandermonde discriminant's interior extremum is at `u = 0`,
  amplitude-independently.

## Boundary

This note does not claim:

- that the framework cannot derive the Koide phase by any non-spectral route;
- that `delta` is an admitted input;
- that all CP-odd, labeled, dynamical, or readout routes are closed;
- that Record supplies, forbids, or classifies the relevant readout;
- a value link to `theta_gauge`;
- a charged-lepton mass prediction or PDG fit;
- a new axiom, primitive, or Tier-A admission.

The safe conclusion is narrower: standard spectral invariants of the Hermitian
`C_3` circulant do not single out the interior comparator `delta = 2/9`; a route
to that value would need additional non-spectral structure or an explicitly
named future premise.

## Inputs

| Input | Source | Role |
|---|---|---|
| charged-lepton Koide cone algebra and Hermitian circulant lane | [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md), [`KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md`](KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md) | bounded context for the `C_3` circulant calculation |
| Brannen `delta = 2/9` comparator | [`KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25.md`](KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25.md) | target comparator only, not an input to the proof |

No PDG value or fitted number is used by the runner.

## Command

```bash
python3 scripts/koide_delta_c3_circulant_spectral_boundary_2026_06_08.py
```
