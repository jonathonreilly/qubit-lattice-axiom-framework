# Fixed-Energy Eikonal Index Bridge for the Gravity Premise (4) Packet

**Date:** 2026-06-16
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_gravity_fixed_energy_eikonal_index_bridge_2026_06_16.py`](../scripts/frontier_gravity_fixed_energy_eikonal_index_bridge_2026_06_16.py)
**Cached output:** [`logs/runner-cache/frontier_gravity_fixed_energy_eikonal_index_bridge_2026_06_16.txt`](../logs/runner-cache/frontier_gravity_fixed_energy_eikonal_index_bridge_2026_06_16.txt)

## Purpose

The audit blocker for the Premise (4) refractive-index packet asked for two
bridges rather than another citation to textbook WKB language:

1. an additive scalar shift in the lattice generator, with sign and
   normalization stated; and
2. a fixed-energy eikonal/Fermat identification proving `n = k/k0` on the
   framework surface.

This note supplies the fixed-energy eikonal index `n = k/k0` as a direct
phase-count identity on the bounded scalar dispersion packet. The scalar
generator shift sign and fixed-energy normalization are now supplied by the
2026-06-18 source-side bridge
[`GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md`](GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md):
the generator term is `H_s = H_0 + s I`, and the action-normalized weak-field
variable on this packet is `phi_action = c_E s`. It does not add an axiom and
does not import a textbook result as a proof input.

## One-Hop Inputs

- [`GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  is the retained-bounded weak-field source/action/readout authority. It
  supplies the sign convention in which a positive weak field lowers the
  normalized test action, `S_test(phi;x) = L_test (1 - phi(x))`, on the
  bounded test-source packet.
- [`GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md`](GRAVITY_SCALAR_SHIFT_SIGN_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md)
  is the source-side shift/sign bridge for this packet. It proves that the
  locally constant scalar generator term is `+s I`, that positive `s` lowers
  the fixed-energy phase action, and that the action-normalized weak-field
  variable is `phi_action = c_E s` with
  `c_E = 1/(k0 lambda_axis'(k0))`.
- [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
  is the retained-bounded source packet for the scalar field entering the
  propagator/action surface. This note uses its scalar-field packet as an
  input; it does not rederive universal matter coupling.
- The axis graph-Laplacian dispersion is the finite-lattice symbol
  `lambda_axis(k) = 2 - 2 cos(k)` used by the Premise (4) packet.

No observed constants, PDG values, fitted selectors, new repo-wide axioms, or
literature coefficients are used.

## Statement

Consider the one-axis scalar-shifted lattice generator in a locally constant
weak-field cell:

```text
    H_s = H_0 + s I,
    lambda_axis(k) = 2 - 2 cos(k),
    lambda_axis(k_s) + s = E.
```

Here `s` is the scalar generator shift supplied by the 2026-06-18 sign bridge,
with the sign convention cross-checked against the weak-field source-response
bridge: positive field decreases the normalized action, so the shifted
fixed-energy symbol is written with `+s` and therefore has smaller local
wavenumber at fixed `E`.

For `0 < E < 4` and `|s| << E`, the exact local wavenumber is

```text
    k_s = arccos(1 - (E - s)/2).
```

Let `k0 = k_{s=0}`. For a piecewise constant slowly varying field along a
ray-like lattice path with segment lengths `Delta l_j`, the local
monochromatic phase count is

```text
    Phase / k0 = sum_j (k_{s_j}/k0) Delta l_j.
```

Therefore the framework-native optical index for this scalar dispersion packet
is not an extra physical postulate:

```text
    n_j := k_{s_j} / k0.
```

It is the dimensionless local phase density relative to the free phase density
at the same fixed energy. The Fermat functional for this packet is exactly the
normalized phase action

```text
    S_eik[s] = sum_j n_j Delta l_j.
```

The first-order expansion is

```text
    n(s) = 1 - c_E s + O(s^2),
    c_E = 1 / (k0 lambda_axis'(k0)).
```

Since `lambda_axis'(k) = 2 sin(k)` and `lambda_axis(k0)=E`, the small-`k`
weak-field limit gives

```text
    c_E = 1/(2E) + O(1),
    n(s) = 1 - s/(2E) + O(s^2/E^2, E s).
```

This is the coefficient used by the Premise (4) refractive-index packet.
Choosing the unit normalization `c_E s = phi_phys` recovers the displayed
`S = L - int phi_phys dl` form; without that normalization, this note supplies
the structural index form and the exact coefficient `c_E`, not a physical
value of `G_Newton`.

## Proof

### 1. Additive scalar shift

On a constant-field cell, the 2026-06-18 shift/sign bridge supplies
`H_s = H_0 + s I` and the action normalization `phi_action = c_E s`. The
spectral consequence is immediate: adding a scalar term `s I` shifts every
plane-wave eigenvalue by `s`:

```text
    H_0 e^{ikx} = lambda_axis(k) e^{ikx}
    (H_0 + s I) e^{ikx} = (lambda_axis(k) + s) e^{ikx}.
```

This is finite-dimensional spectral algebra conditional on the cited scalar
shift/sign bridge. The physical weak-field sign for the scalar action shift is
not guessed here; it is inherited from the retained-bounded weak-field
source-response bridge's test-action convention and normalized by
`c_E = 1/(k0 lambda_axis'(k0))` on the fixed-energy packet.

### 2. Fixed-energy inverse

At fixed monochromatic energy `E`, the local symbol equation is

```text
    lambda_axis(k_s) + s = E.
```

For the axis symbol this is

```text
    2 - 2 cos(k_s) = E - s,
```

so

```text
    cos(k_s) = 1 - (E - s)/2,
    k_s = arccos(1 - (E - s)/2)
```

on the positive branch `0 < k_s < pi`.

### 3. Eikonal phase count

For a slowly varying piecewise constant field, the lattice phase accumulated
along a path is the sum of local phase increments:

```text
    Phase[s] = sum_j k_{s_j} Delta l_j.
```

Dividing by the free phase density `k0` gives

```text
    Phase[s]/k0 = sum_j (k_{s_j}/k0) Delta l_j.
```

Thus `n = k_s/k0` is the optical-index functional for this packet by direct
phase counting. No continuum WKB theorem or textbook Fermat import is used as
the load-bearing proof; the only approximation is the explicit slowly varying
piecewise-constant ray-packet boundary.

### 4. First-order coefficient and sign

Differentiate `lambda_axis(k_s) + s = E`:

```text
    lambda_axis'(k0) dk/ds + 1 = 0,
    d(k_s/k0)/ds |_{s=0} = -1/(k0 lambda_axis'(k0)).
```

Since `lambda_axis'(k0)>0`, positive `s` lowers `k_s/k0`, matching the
weak-field source-response convention that positive field lowers the
normalized action. In the small-`k` regime, `lambda_axis(k0)=E` and
`lambda_axis'(k0)=2 sin(k0)=2 k0 + O(k0^3)`, so
`k0 lambda_axis'(k0)=2E+O(E^2)` and `c_E=1/(2E)+O(1)`.

### 5. Ray deflection form

For `n(x)=1-c_E s(x)` and a weak radial scalar `s(r)=a/r`, the linearized
ray-angle magnitude is the transverse gradient integral

```text
    |alpha(b)| = c_E int_{-infty}^{infty} a b / (b^2+z^2)^{3/2} dz
               = 2 c_E a / b.
```

The `1/b` form therefore follows from the same finite phase-count index once
the scalar field has the retained `1/r` weak-field support. The coefficient is
the packet coefficient `c_E a`; this note does not fix a physical Newton
constant.

## Boundaries

- Bounded to the axis symbol and slowly varying piecewise-constant scalar
  packet. It is not a full arbitrary-graph WKB theorem.
- The scalar generator shift/sign and fixed-energy action normalization are
  cited from the 2026-06-18 source-side bridge, not promoted by this note into
  arbitrary-graph WKB or physical `G_Newton` normalization.
- The scalar weak-field sign is inherited from the retained-bounded
  source-response bridge. This note does not derive a universal matter
  coupling theorem.
- The physical `G_Newton` normalization, nonlinear gravity, tensor metric
  sector, strong-field regime, and observed unit conversion remain out of
  scope.
- The result is a source-side repair proposal. Independent audit must decide
  whether it is sufficient for any downstream effective-status change.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gravity_fixed_energy_eikonal_index_bridge_2026_06_16.py
```

Expected result:

```text
TOTAL: PASS=36 FAIL=0
```
