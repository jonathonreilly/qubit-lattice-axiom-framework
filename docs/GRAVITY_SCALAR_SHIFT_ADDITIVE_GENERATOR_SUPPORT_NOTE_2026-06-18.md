# Gravity Scalar-Shift Additive Generator Support Note

**Date:** 2026-06-18
**Claim type:** bounded_theorem / bounded support
**Primary runner:** [`scripts/frontier_gravity_scalar_shift_additive_generator_support_2026_06_18.py`](../scripts/frontier_gravity_scalar_shift_additive_generator_support_2026_06_18.py)

## Purpose

This note supplies the missing one-hop support requested by the audit of
[`GRAVITY_FIXED_ENERGY_EIKONAL_INDEX_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md`](GRAVITY_FIXED_ENERGY_EIKONAL_INDEX_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md):
derive the local additive scalar generator shift

```text
H_s = H_0 + s I
```

with the `+s` sign and normalization used by the fixed-energy eikonal packet.
It is bounded to the same one-axis scalar-symbol packet and weak-field action
normalization. It does not derive a physical Newton constant, nonlinear
Einstein dynamics, a universal matter-coupling theorem, or an arbitrary-graph
WKB theorem.

No observed constants, fitted selectors, new repo-wide axioms, or textbook
theorems are used as proof inputs.

## Inputs

- [`GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  supplies the bounded weak-field action convention
  `S_test(phi; x) = L_test (1 - phi(x))` and the attractive sign
  `U_test(phi; x) = -m phi(x)`.
- [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
  supplies the bounded scalar propagator/action surface on which a nearest
  neighbor scalar response is read.
- The eikonal packet uses the one-axis finite-lattice symbol
  `lambda_axis(k) = 2 - 2 cos(k)`.

## Statement

Fix a monochromatic packet energy `0 < E < 4` on the one-axis scalar symbol.
Let

```text
k0 = arccos(1 - E/2),
c_E = 1 / (k0 lambda_axis'(k0)).
```

The weak-field action convention says that a positive local scalar field
`phi_phys` lowers the dimensionless phase/action density:

```text
S_test(phi; segment) / L_test = 1 - phi_phys.
```

The additive scalar-shift variable used by the fixed-energy eikonal packet is
therefore normalized by

```text
c_E s = phi_phys.
```

With this normalization, the local scalar-shifted generator is

```text
H_s = H_0 + s I,
```

so a plane wave on a constant-field cell satisfies

```text
(H_0 + s I) e^{ikx} = (lambda_axis(k) + s) e^{ikx}.
```

At fixed energy,

```text
lambda_axis(k_s) + s = E,
```

and the first-order normalized phase density is

```text
k_s/k0 = 1 - phi_phys + O(phi_phys^2).
```

Thus the `+s` sign is fixed by the action convention: positive
`phi_phys` gives positive `s`, which lowers `k_s/k0` and therefore lowers the
phase/action density, matching `S_test/L_test = 1 - phi_phys`.

## Proof

The spectral algebra is finite-dimensional. On a constant scalar cell,
adding a scalar multiple of the identity shifts every eigenvalue and leaves
each eigenvector unchanged:

```text
H_0 v = lambda v
=> (H_0 + s I) v = (lambda + s) v.
```

For the axis packet, the eigenvalue is `lambda_axis(k)`, hence the fixed-energy
equation is `lambda_axis(k_s) + s = E`.

Differentiate at `s = 0`:

```text
lambda_axis'(k0) dk_s/ds + 1 = 0,
d(k_s/k0)/ds = -1 / (k0 lambda_axis'(k0)) = -c_E.
```

If `phi_phys = c_E s`, then

```text
d(k_s/k0)/d phi_phys = -1.
```

This is exactly the first-order weak-field action response. The support
runner also checks the finite matrix version on a periodic path graph: the
discrete Laplacian eigenvectors are unchanged by `+sI`, all eigenvalues shift
by `+s`, and the normalization above maps a positive action field to a
smaller fixed-energy wavenumber.

## Boundaries

- This is a bounded scalar-symbol support theorem, not a complete gravity
  claim.
- The physical source of `phi_phys` is inherited from the bounded weak-field
  source-response packet; this note only fixes the additive generator shift
  used by the eikonal bridge.
- The normalization is energy-packet local through `c_E`; it does not set a
  physical value for `G_Newton` or an SI-unit conversion.
- The slowly varying ray/eikonal composition remains in the downstream
  fixed-energy bridge note.
- Independent audit decides whether this one-hop support is sufficient for any
  downstream effective-status change.

## Verification

Run:

```bash
python3 scripts/frontier_gravity_scalar_shift_additive_generator_support_2026_06_18.py
```

Expected final line:

```text
TOTAL: PASS=29 FAIL=0
```
