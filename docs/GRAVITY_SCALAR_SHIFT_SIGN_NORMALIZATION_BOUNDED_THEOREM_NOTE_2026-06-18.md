# Gravity Scalar-Shift Sign and Fixed-Energy Normalization Bridge

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_gravity_scalar_shift_sign_normalization_2026_06_18.py`](../scripts/frontier_gravity_scalar_shift_sign_normalization_2026_06_18.py)
**Cached output:** [`logs/runner-cache/frontier_gravity_scalar_shift_sign_normalization_2026_06_18.txt`](../logs/runner-cache/frontier_gravity_scalar_shift_sign_normalization_2026_06_18.txt)

## Purpose

This is the source-side sign/normalization bridge requested by the fixed-energy
eikonal audit blocker. It proves, on the bounded one-axis scalar dispersion
packet, which scalar generator shift is meant by

```text
H_s = H_0 + s I
```

and how its coefficient is normalized against the weak-field action variable
used by the gravity source-response packet.

No observed constants, fitted selectors, textbook WKB theorem, new axiom, or
physical value of `G_Newton` is used.

## Inputs

- [`GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  supplies the bounded weak-field sign convention:

  ```text
  S_test(phi; x) = L_test (1 - phi(x)).
  ```

  A positive weak field lowers the normalized test action.
- The one-axis scalar dispersion packet has graph-Laplacian symbol

  ```text
  lambda_axis(k) = 2 - 2 cos(k)
  ```

  on the positive branch `0 < k < pi`.

## Statement

On a locally constant scalar cell, the scalar generator contribution is the
identity term `s I` on the one-component axis packet:

```text
H_s = H_0 + s I.
```

The sign is fixed as follows. At fixed energy `E`, the shifted symbol obeys

```text
lambda_axis(k_s) + s = E.
```

For positive `s`, the local wavenumber `k_s` decreases. The normalized
fixed-energy phase/action density is therefore

```text
n(s) = k_s / k0 = 1 - c_E s + O(s^2),
c_E = 1 / (k0 lambda_axis'(k0)),
lambda_axis(k0) = E.
```

Since `c_E > 0`, positive `s` lowers the normalized phase action, matching the
weak-field source-response sign. The action-normalized weak-field variable on
this packet is therefore

```text
phi_action := c_E s,
```

so that, to first order,

```text
S_eik/L = n(s) = 1 - phi_action + O(phi_action^2).
```

Equivalently,

```text
s = phi_action / c_E = k0 lambda_axis'(k0) phi_action.
```

In the small-`k` regime, `k0 lambda_axis'(k0) = 2E + O(E^2)`, so the familiar
weak-field normalization is `s = 2E phi_action + O(E^2 phi_action)`. This
normalization is internal to the bounded fixed-energy scalar packet; it does
not set a physical Newton constant.

## Proof

### 1. Scalar shift as identity term

On the locally constant scalar cell used by the bounded ray packet, the scalar
field has no site, direction, taste, or internal label inside the cell. On the
one-component axis dispersion surface, the corresponding generator term is
therefore the scalar identity `s I`. In momentum eigenvectors of `H_0`,

```text
H_0 |k> = lambda_axis(k) |k>,
(H_0 + s I) |k> = (lambda_axis(k) + s) |k>.
```

This is finite-dimensional spectral algebra, not a continuum import.

### 2. Sign

At fixed `E`, differentiating

```text
lambda_axis(k_s) + s = E
```

gives

```text
lambda_axis'(k0) dk_s/ds + 1 = 0.
```

On the selected branch `lambda_axis'(k0)>0`, so `dk_s/ds<0`. A positive scalar
shift decreases `k_s/k0` and therefore lowers the normalized phase action.
This matches the weak-field source-response convention
`S_test/L_test = 1 - phi`.

### 3. Normalization

The fixed-energy eikonal bridge defines normalized phase action by

```text
S_eik/L = k_s/k0.
```

The derivative above gives

```text
d(k_s/k0)/ds |_{s=0} = -1/(k0 lambda_axis'(k0)) = -c_E.
```

Thus the weak-field action variable for this packet is exactly
`phi_action = c_E s` at first order. The generator shift itself is `s`; the
action-normalized field variable is the rescaled object `c_E s`.

## Boundaries

- This is bounded to a locally constant scalar cell on the one-axis
  graph-Laplacian dispersion packet.
- It derives the `+s I` sign and fixed-energy normalization used by the
  eikonal bridge. It does not derive arbitrary-graph WKB, nonlinear gravity,
  tensor metric structure, or physical SI units.
- It consumes the weak-field source-response sign convention as a retained
  bounded input; it does not derive universal matter coupling.
- Independent audit is the only effective-status authority.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gravity_scalar_shift_sign_normalization_2026_06_18.py
```

Expected result:

```text
TOTAL: PASS=28 FAIL=0
```
