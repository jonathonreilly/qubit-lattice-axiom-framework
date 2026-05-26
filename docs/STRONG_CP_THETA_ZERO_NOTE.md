# Strong CP Theta-Zero Selected-Surface Algebra

**Date:** 2026-04-16; selected-surface repair 2026-05-25
**Status:** bounded-support selected-surface algebra. The selected surface is an explicit premise, not a derived framework action-surface theorem. Independent audit remains required before any effective-status change.
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_strong_cp_theta_zero_selected_surface_repair.py`

## Actual claim

On the explicitly selected Wilson-plus-staggered scalar-mass surface with:

1. no bare theta slot in the action functional, so `theta_bare = 0` by surface selection;
2. real positive scalar quark-mass operators `M_u = m_u I` and `M_d = m_d I`, with `m_u, m_d > 0`, by the selected scalar-mass convention;
3. an anti-Hermitian staggered Dirac operator whose nonzero eigenvalues pair as `+i lambda` and `-i lambda`;
4. real Wilson gauge action and positive topological-sector weights `Z_Q >= 0`;

the selected-surface algebra gives:

```text
arg det(M_u M_d) = 0,
theta_eff = theta_bare + arg det(M_u M_d) = 0,
det(D + m I) > 0 for m > 0 on the paired finite spectrum,
S_eff[U] = S_W[U] - log det(D[U] + m I) is real, and
|Z(theta)| <= Z(0), so the selected positive-weight sector sum is maximized at theta = 0.
```

This is a bounded theorem about the explicitly selected surface. It is not a derivation of the selected surface from the framework axioms.

## Why this repair is narrow

The prior audit verdict accepted the internal determinant, axial, effective-action, and positive-weight checks, but marked the row conditional because the load-bearing action-surface choices were being used as premises:

- no admissible CP-odd `F tilde F` or lattice theta slot;
- positive real scalar quark-mass orientation;
- the real-positive Wilson-plus-staggered surface itself.

This repair does not try to hide those premises. It makes them the theorem hypotheses and withdraws any stronger claim that the repo has already derived the action-surface selector or the mass-orientation selector from the minimal framework surface.

## Selected-surface hypotheses

### S1. Theta-free Wilson slot

The selected action surface contains the Wilson real plaquette action and contains no independent bare theta coupling. Therefore:

```text
theta_bare = 0
```

is a surface-selection input for this row. This note does not prove that every possible CP-odd lattice operator slot is inadmissible.

### S2. Real positive scalar mass line

The selected scalar-mass surface uses:

```text
M_u = m_u I,  M_d = m_d I,  m_u > 0,  m_d > 0.
```

For these matrices:

```text
det(M_u M_d) = (m_u m_d)^N > 0,
arg det(M_u M_d) = 0.
```

The positive sign is part of the selected scalar-mass convention here. This row does not derive the scalar-mass-only class or the positive orientation from determinant positivity alone.

### S3. Paired anti-Hermitian staggered spectrum

For a finite anti-Hermitian staggered operator with paired eigenvalues:

```text
spec(D) = {+i lambda_k, -i lambda_k}_k,
```

and `m > 0`,

```text
det(D + m I) = product_k (m + i lambda_k)(m - i lambda_k)
             = product_k (m^2 + lambda_k^2) > 0.
```

Therefore `log det(D + m I)` is real on this selected finite spectral surface.

### S4. Real effective action

Combining S1-S3 with a real Wilson action:

```text
S_eff[U] = S_W[U] - log det(D[U] + m I)
```

is real on the selected surface. This is an internal selected-surface closure statement, not a claim about complex-action formulations or nonselected topological terms.

### S5. Positive topological-sector weights

If the selected surface is decomposed into real nonnegative sector weights:

```text
Z(theta) = sum_Q Z_Q exp(i theta Q),   Z_Q >= 0,
```

then the triangle inequality gives:

```text
|Z(theta)| <= sum_Q Z_Q = Z(0).
```

Thus the positive-weight sector-sum magnitude is maximized at `theta = 0`, and the corresponding `-log |Z(theta)|` readout is minimized at `theta = 0` wherever the logarithm is defined.

## Theorem

**Theorem.** Under S1-S5, the selected Wilson-plus-staggered scalar-mass surface has:

```text
theta_eff = 0
```

and no internal determinant, axial rephasing within the real scalar mass line, exact fermion integration, or positive sector-sum check reintroduces a strong-sector phase on that selected surface.

**Proof.** S1 gives `theta_bare = 0`. S2 gives `arg det(M_u M_d) = 0`, hence `theta_eff = 0`. S3 gives real positive fermion determinants for the paired finite staggered spectrum. S4 gives a real effective gauge action after exact fermion integration on the selected surface. S5 gives the positive-sector triangle-inequality bound with the selected theta-zero readout. These are exactly the selected-surface statements in the theorem. QED.

## What this row does not claim

- It does not derive the theta-free action surface from the minimal framework axioms.
- It does not derive the scalar-mass-only class or positive mass sign from first principles.
- It does not exclude all continuum, clover, higher-loop, or complex-action theta formulations.
- It does not solve strong CP beyond the explicitly selected surface.
- It does not promote any upstream row or apply an audit verdict.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_strong_cp_theta_zero_selected_surface_repair.py
```

The runner checks the selected-surface inventory, finite paired-spectrum determinant positivity, scalar mass determinant phase, real effective action, topological-sector triangle inequality, axial endpoint discipline on the real scalar line, and audit metadata after pipeline regeneration.
