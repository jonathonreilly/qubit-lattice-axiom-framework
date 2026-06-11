# Weak-Field Source-Response Bridge for the Gravity Clean Chain

**Date:** 2026-06-11. Test-force sign repair: 2026-06-11.
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:** [`scripts/frontier_gravity_weak_field_source_response_bridge_2026_06_11.py`](../scripts/frontier_gravity_weak_field_source_response_bridge_2026_06_11.py)
**Cached output:** [`logs/runner-cache/frontier_gravity_weak_field_source_response_bridge_2026_06_11.txt`](../logs/runner-cache/frontier_gravity_weak_field_source_response_bridge_2026_06_11.txt)

## Claim

On the weak-field `Z^3` graph-Laplacian surface, with

```text
H = -Delta_lat,
G0 = H^{-1}
```

on the zero-mode-removed sector, the following three bridge statements hold as
bounded finite-dimensional variational statements:

1. **Field/operator bridge.** The quadratic source action

   ```text
   A[phi; rho] = (1/2) <phi, H phi> - <P0 rho, phi>
   ```

   has the unique stationary solution, modulo the constant zero mode,

   ```text
   phi = G0 P0 rho.
   ```

   Hence the weak-field operator is `L = H = -Delta_lat` and
   `L^{-1} = G0` on the neutral response sector. This is a variational
   Euler equation, not a symbol renaming.

2. **Source-readout bridge.** For a lattice amplitude `psi`, the only local,
   diagonal, positive, phase-invariant quadratic density that is translation
   covariant and normalized by

   ```text
   sum_x rho_psi(x) = ||psi||^2
   ```

   is

   ```text
   rho_psi(x) = |psi(x)|^2.
   ```

   On finite periodic volumes the Poisson solve uses `P0 rho_psi`, i.e. the
   zero-mode-subtracted density. The zero mode is the total-mass/background
   sector and is not part of the local force law.

3. **Test-source response bridge.** Coupling a localized test source
   `m delta_x` to the same weak field gives, to first order,

   ```text
   S_test(phi; x) = L_test (1 - phi(x)).
   ```

   Equivalently, the weak-field test potential energy is
   `U_test(phi; x) = -m phi(x)`, so the conservative force on the test source
   is

   ```text
   F_x = -grad_x U_test = +m grad_x phi(x).
   ```

   For a source `M delta_y`, this response is bilinear in `M` and `m`.

Composed with the retained-bounded `Z^3` Green-kernel normalization

```text
G(r) -> 1 / (4 pi |r|)
```

from
[`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md),
the bridge supplies the missing weak-field source/readout/test-response
surface for the downstream `GRAVITY_CLEAN_DERIVATION_NOTE.md` consumer.

## Proof Sketch

### 1. Variational Green kernel

Let `P0` be projection off the constant mode on a finite periodic lattice.
The nearest-neighbor graph Laplacian `H=-Delta_lat` is symmetric positive
semidefinite, with kernel exactly the constant mode. On `P0`, the quadratic
functional

```text
A[phi; rho] = (1/2) <phi, H phi> - <P0 rho, phi>
```

has first variation

```text
dA_phi[eta] = <eta, H phi - P0 rho>.
```

Therefore every stationary point satisfies

```text
H phi = P0 rho.
```

Because `H` is positive definite on the `P0` sector, the stationary point is
unique there and equals

```text
phi = H^{-1} P0 rho = G0 P0 rho.
```

This is the weak-field source-response theorem: the field operator is the
quadratic action Hessian `H`, and the Green kernel is its inverse on the
response sector.

### 2. Born-density readout

A local diagonal quadratic density has the form

```text
rho_psi(x) = a_x |psi(x)|^2
```

after phase invariance eliminates all off-diagonal and phase-sensitive terms.
Translation covariance under the `Z^3` shifts forces `a_x` to be independent of
`x`. Normalization then fixes that constant to one:

```text
sum_x rho_psi(x) = a sum_x |psi(x)|^2 = ||psi||^2
```

so `a=1`.

Thus `rho=|psi|^2` is not an arbitrary gravitational readout inside this
bounded weak-field packet; it is the unique local phase-invariant normalized
density available from the amplitude carrier.

### 3. Test-source action response

For a background source `rho`, the stationary field is `phi=G0 P0 rho`. A
localized test source `m delta_x` couples by the same source term:

```text
Delta S_test = -m phi(x) Delta tau.
```

Writing the free test action increment as `L_test=m Delta tau`, the first-order
response is

```text
S_test(phi; x) = L_test - L_test phi(x) = L_test(1 - phi(x)).
```

The static force statement uses the corresponding potential-energy convention
`U_test(phi; x) = -m phi(x)`. Therefore

```text
F_x = -grad_x U_test = +m grad_x phi(x)
```

with the sign fixed by the attractive potential convention in which a positive
source has `phi(r) > 0` and `grad phi` points inward at large separation. With
a source `rho=M delta_y`, linearity gives `phi=M G0 delta_y`, so the test
response is bilinear in `M` and `m`.

### 4. Large-distance law

The retained-bounded framework-local Green theorem supplies

```text
G0(x,y) = 1/(4 pi |x-y|) + lower-order lattice terms.
```

Consequently the first-order test response has a `1/r` potential and an
inverse-square force at large separation in lattice units. This note supplies
the source/readout/response bridge; the Green-kernel asymptotic remains the
load-bearing authority for the coefficient and exponent.

## Boundaries

This is a bounded weak-field theorem. It does not claim:

- nonlinear self-gravity closure;
- the full Einstein equations;
- physical `G_Newton` in SI units;
- a strong-field/horizon/geodesic/lensing theorem;
- that the constant zero mode is fixed by this packet;
- any audit status for this row or for `GRAVITY_CLEAN_DERIVATION_NOTE.md`.

The no-go boundary is compatible with retained no-go rows
[`POISSON_SELF_GRAVITY_LOOP_V3_NOTE.md`](POISSON_SELF_GRAVITY_LOOP_V3_NOTE.md)
and [`GATE_B_POISSON_SELF_GRAVITY_NOTE.md`](GATE_B_POISSON_SELF_GRAVITY_NOTE.md):
the bridge is only the linearized response around a fixed weak-field
background, not a convergent nonlinear back-reaction loop.

## Dependencies

- [`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
  supplies the retained-bounded Poisson operator surface.
- [`POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md`](POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md)
  supplies retained-bounded uniqueness diagnostics for the Poisson operator
  family.
- [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)
  supplies the retained-bounded `Z^3` graph-Laplacian Green-kernel
  normalization.
- [`POISSON_SELF_GRAVITY_LOOP_V3_NOTE.md`](POISSON_SELF_GRAVITY_LOOP_V3_NOTE.md)
  and [`GATE_B_POISSON_SELF_GRAVITY_NOTE.md`](GATE_B_POISSON_SELF_GRAVITY_NOTE.md)
  supply the retained no-go boundary for nonlinear self-gravity iteration.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gravity_weak_field_source_response_bridge_2026_06_11.py
```

Expected result:

```text
TOTAL: PASS=44 FAIL=0
```
