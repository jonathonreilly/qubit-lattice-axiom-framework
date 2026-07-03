# Native Transfer-Kernel Twist Sufficiency Test: the Actual Two-Step Log-Generator Has the Holonomy-Odd Tail but No In-Gap Edge Tower

**Date:** 2026-06-11
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** Finite-dimensional single-particle test of the native free
staggered two-step transfer log-generator on a 2D cylinder with boundary-cycle
`U(1)` holonomy. The runner first validates the retained 1D two-step transfer
object, then tests whether the actual native `K = -log(T_hat^2)` satisfies the
Wilson-mass holonomy note's named sufficiency conditions for the signed-gravity
twist datum. Outcome: the native kernel contains the same-parity,
orientation-odd holonomy-dependent component requested by the parity-dichotomy
candidate, but the #3585 sufficiency chain fails at the in-gap edge-tower
condition. The native free transfer log therefore does not source the twist
datum on this route. Named residual: a sector that creates an actual
zero-centered boundary tower, e.g. Wilson-mass/domain-wall structure,
interaction-induced boundary structure, a gauged/interacting log-transfer
extension, or another explicitly derived boundary mechanism.

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:**
[`scripts/signed_gravity_native_transfer_kernel_twist_sufficiency_2026_06_11.py`](../scripts/signed_gravity_native_transfer_kernel_twist_sufficiency_2026_06_11.py)

**Runner cache:**
[`logs/runner-cache/signed_gravity_native_transfer_kernel_twist_sufficiency_2026_06_11.txt`](../logs/runner-cache/signed_gravity_native_transfer_kernel_twist_sufficiency_2026_06_11.txt)

## Question

The Wilson-mass holonomy realization constructed the twist datum on a
hand-built QWZ/Wilson cylinder. The parity-grading dichotomy then observed that
the native transfer log already contains same-parity couplings, the coupling
class that a parity-flipping-only staggered operator lacks. This note tests the
actual native kernel, not a hand-built Wilson mass:

```text
    Does K_2D = -log(T_hat^2) on the native staggered cylinder satisfy the
    named sufficiency conditions for the holonomy twist datum?
```

Both outcomes were allowed. A positive outcome would have supplied the twist
datum with no added Wilson/domain-wall pin. The measured outcome is negative
for the sufficiency route: same-parity orientation-odd content is present, but
there is no in-gap boundary tower to label.

## Construction

The 1D validation gate uses the retained two-step transfer construction from
[`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md).
For each spatial momentum,

```text
    T2cl(p) = T_odd(p) T_even(p),
    spec_decaying(T2cl(p)) = exp(-2 E(p)),
    E(p) = arcsinh(sqrt(m^2 + sin^2 p)).
```

Therefore the unnormalized single-particle log used here is
`K = -log(T_hat^2)` with spectrum `2 E(p)`. The normalized Hamiltonian
convention of the retained notes is `K / 2`.

The 2D cylinder uses the native staggered spatial hop in the realization-gate
form, with no Wilson mass, no domain wall, and no added term:

```text
    D_{x,y}[U] =
      sum_mu (1/2) eta_mu(x)
        [ U_mu(x) delta_{y,x+mu} - U_mu(y)^dag delta_{y,x-mu} ],

    H_hop = -i D[U],
    H_raw = H_hop + m epsilon,
    epsilon(x,y) = (-1)^(x+y).
```

`x` is periodic and carries holonomy `theta`; `y` is open. The runner inserts a
uniform phase `exp(i theta / L_x)` on each `x`-link and verifies spectral
equivalence to a single twisted bond. The transfer log is the retained
decaying-channel spectral calculus applied to the same anti-Hermitian spatial
hop:

```text
    K_2D = 2 arcsinh(sqrt(m^2 + H_hop^2)).
```

The largest default carrier is `28 x 40 = 1120` single-particle sites. No Fock
space is built.

## Validation Gate

At `m = 0.5`, the runner validates the 1D retained object before interpreting
the 2D cylinder:

| Check | Measured value |
|---|---:|
| `-log(T_hat^2) = 2 E(p)` on `L=64` | max real residual `2.44e-15`, max imaginary part `8.72e-16` |
| Even-distance support | max odd-distance coefficient `3.60e-17` |
| Quasilocality rate | fitted rate `0.482148`, retained sharp rate `arcsinh(0.5)=0.481212` |

The geometry controls also pass:

| Check | Measured value |
|---|---:|
| Uniform holonomy vs single twisted bond | spectral residual `1.78e-15` |
| Two-site-cell mixed `(p_x,y)` blocks vs full cylinder | spectral residual `3.11e-15` |

## Dichotomy Gates

On the `20 x 30` cylinder, the parity and orientation measurements are:

| `theta` | `||[Gamma,K]||` | `||{Gamma,K}||` | `||K_same||` | `||K_flip||` | orientation-odd op norm |
|---:|---:|---:|---:|---:|---:|
| `0` | `2.37e-14` | `4.771` | `2.385734` | `1.18e-14` | `7.73e-15` |
| `1.0` | `2.83e-14` | `4.770` | `2.384806` | `1.41e-14` | `0.048571` |
| `pi` | `1.74e-14` | `4.753` | `2.376607` | `8.70e-15` | `0.150585` |

So the failure is not the parity-flipping mirror obstruction. The native log
commutes with the parity grading up to machine precision and is same-parity.
The load-bearing candidate requested by the parity-dichotomy note is present:
the same-parity orientation-odd component is zero at `theta=0` and nonzero at
generic holonomy.

The raw massive staggered block remains a control, not the transfer log:
`||[Gamma,H_raw]|| ~= 2.82` and `||{Gamma,H_raw}|| = 1.00`; the pure hop has
`||{Gamma,H_hop}|| = 0`.

## Sufficiency Verdict Table

The in-gap window is the Wilson-mass note's zero-centered criterion:
`|lambda| <= bulk_gap / 2`, with the bulk gap measured on the matching
periodic-`y` carrier. Edge localization uses the same `0.99` outer-row
criterion. Eta labels are counted only on spectrally truncated in-gap edge
states; the `Lambda` sweep is `(0.20, 0.35, 0.48)`.

| condition | theta | size | measured value | met |
|---|---:|---:|---|---|
| gapped zero window | `0` | `20x30` | `gap0=0.966999`, periodic-bulk `gap0=0.962424` | met |
| orientation-odd same-parity coupling | `0` | `20x30` | Fro norm `0.000000` | not-met |
| in-gap edge tower | `0` | `20x30` | `|lambda|<=0.481212`: states `0`, edge99 `0` | not-met |
| spectral eta labels | `0` | `20x30` | bottom eta `(0,0,0)`, top eta `(0,0,0)` | not-met |
| gapped zero window | `0.6` | `20x30` | `gap0=0.968597`, periodic-bulk `gap0=0.964031` | met |
| orientation-odd same-parity coupling | `0.6` | `20x30` | Fro norm `0.360999` | met |
| in-gap edge tower | `0.6` | `20x30` | `|lambda|<=0.482016`: states `0`, edge99 `0` | not-met |
| spectral eta labels | `0.6` | `20x30` | bottom eta `(0,0,0)`, top eta `(0,0,0)` | not-met |
| gapped zero window | `1.0` | `20x30` | `gap0=0.971427`, periodic-bulk `gap0=0.966879` | met |
| orientation-odd same-parity coupling | `1.0` | `20x30` | Fro norm `0.600935` | met |
| in-gap edge tower | `1.0` | `20x30` | `|lambda|<=0.483439`: states `0`, edge99 `0` | not-met |
| spectral eta labels | `1.0` | `20x30` | bottom eta `(0,0,0)`, top eta `(0,0,0)` | not-met |
| gapped zero window | `pi` | `20x30` | `gap0=1.009298`, periodic-bulk `gap0=1.004973` | met |
| orientation-odd same-parity coupling | `pi` | `20x30` | Fro norm `1.856417` | met |
| in-gap edge tower | `pi` | `20x30` | `|lambda|<=0.502486`: states `0`, edge99 `0` | not-met |
| spectral eta labels | `pi` | `20x30` | bottom eta `(0,0,0)`, top eta `(0,0,0)` | not-met |
| gapped zero window | `0` | `28x40` | `gap0=0.965043`, periodic-bulk `gap0=0.962424` | met |
| orientation-odd same-parity coupling | `0` | `28x40` | Fro norm `0.000000` | not-met |
| in-gap edge tower | `0` | `28x40` | `|lambda|<=0.481212`: states `0`, edge99 `0` | not-met |
| spectral eta labels | `0` | `28x40` | bottom eta `(0,0,0)`, top eta `(0,0,0)` | not-met |
| gapped zero window | `0.6` | `28x40` | `gap0=0.965861`, periodic-bulk `gap0=0.963244` | met |
| orientation-odd same-parity coupling | `0.6` | `28x40` | Fro norm `0.351666` | met |
| in-gap edge tower | `0.6` | `28x40` | `|lambda|<=0.481622`: states `0`, edge99 `0` | not-met |
| spectral eta labels | `0.6` | `28x40` | bottom eta `(0,0,0)`, top eta `(0,0,0)` | not-met |
| gapped zero window | `1.0` | `28x40` | `gap0=0.967313`, periodic-bulk `gap0=0.964701` | met |
| orientation-odd same-parity coupling | `1.0` | `28x40` | Fro norm `0.585745` | met |
| in-gap edge tower | `1.0` | `28x40` | `|lambda|<=0.482350`: states `0`, edge99 `0` | not-met |
| spectral eta labels | `1.0` | `28x40` | bottom eta `(0,0,0)`, top eta `(0,0,0)` | not-met |
| gapped zero window | `pi` | `28x40` | `gap0=0.987063`, periodic-bulk `gap0=0.984519` | met |
| orientation-odd same-parity coupling | `pi` | `28x40` | Fro norm `1.824384` | met |
| in-gap edge tower | `pi` | `28x40` | `|lambda|<=0.492260`: states `0`, edge99 `0` | not-met |
| spectral eta labels | `pi` | `28x40` | bottom eta `(0,0,0)`, top eta `(0,0,0)` | not-met |

## Theorem

**Negative native-transfer sufficiency theorem.** On the tested native free
staggered cylinder, the actual two-step transfer log-generator satisfies the
1D retained transfer validation and contains a nonzero holonomy-dependent
same-parity orientation-odd component, but it does not satisfy the named
#3585 sufficiency conditions for the signed-gravity twist datum. The failing
condition is the in-gap edge tower: for every tested `theta in {0, 0.6, 1.0,
pi}` and both tested sizes `(20,30)` and `(28,40)`, the accepted in-gap window
contains `0` states and hence `0` edge-localized states at the `0.99` bar.
Consequently the spectral `Lambda`-sweep eta labels are undefined, not
opposite and stable. The native free kernel therefore cannot source the twist
datum on this sufficiency route.

This is a bounded route result. It does not test or exclude a Wilson-mass or
domain-wall sector, an interacting or fully gauged transfer log, a 3D lift, a
different derived boundary mechanism, eta-sector superselection, or the source
action.

## Structural Reading of the In-Gap Emptiness (reviewer addition, 2026-06-11)

The condition-(ii) failure is stronger than an edge-localization miss on the
tested carriers: it is caused by the positive-log spectral floor, and the scan
instantiates that mechanism. By the retained two-step positivity, `T_hat^2` is
a positive contraction, so
`K = -log(T_hat^2)` is a positive operator; on the validated spectral
calculus `K = 2 arcsinh(sqrt(m^2 + H_hop^2))` and `H_hop^2 >= 0`, hence

```text
    spec(K) is contained in [2 arcsinh(m), infinity)
```

For the tested carriers, the zero-centered acceptance window has half-width
`bulk_gap/2 ~= arcsinh(m)`, strictly below that floor. The window is therefore
empty by the floor/window separation verified here, not by an edge-localization
threshold artifact; the runner verifies the floor inequality and the
window-below-floor inequality explicitly on every tested carrier
(`gap0 >= 2 arcsinh(m) = 0.962424` at `m = 0.5`).

This sharpens the named residual. A zero-centered labeled tower on this
readout requires a symmetric-spectrum carrier, and a positive transfer log is
not such a carrier.
The holonomy-odd same-parity resource measured above therefore cannot be
labeled *in `K` itself* on the tested free carriers; a derived mechanism would
have to transport that odd component into a symmetric-spectrum object — for
example the boundary-block form `A(a) (x) epsilon` of the product-grading
construction (in-flight plain-text reference:
`SIGNED_GRAVITY_PRODUCT_GRADING_ETA_SECTOR_SELECTION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md`)
with `A(a)` built from the odd component, or an effective boundary Dirac
operator of a Wilson-mass/domain-wall or interacting sector. Constructing any
such transport from retained primitives is the named open derivation target;
none is claimed here.

## Bounded Negative Discipline Check

- **N1, attack routes against this negative result.** Step-1 mismatch was
  tested and fails as an objection: the 1D construction matches `2E(p)` to
  `2.44e-15`. Gauge-placement artifact was tested and fails as an objection:
  uniform holonomy and a single twisted bond agree to `1.78e-15`. Momentum-block
  artifact was tested and fails as an objection: the two-site-cell
  `(p_x,y)` blocks reproduce the full spectrum to `3.11e-15`. Mirror-grading
  tautology was tested and fails as the explanation: `K` commutes with `Gamma`
  and has nonzero same-parity content. Index-truncation fake labels were
  avoided by spectral `Lambda` sweeps on accepted in-gap edge states; those
  sets are empty. Finite-size hiding of an edge tower was tested at two sizes;
  the larger size still has `in_gap=0`, `edge99=0`.
- **N2, wall independence.** The route failure has one load-bearing measured
  wall: absence of an in-gap edge tower. Label failure follows from that wall
  and is not counted as independent.
- **N3, hidden-wall scan.** The construction uses the retained two-step
  transfer formula and the native staggered realization-gate hop. The note does
  not import a Wilson term, domain wall, literature invariant, fitted physical
  value, or external citation.
- **N4, residual matching.** The Wilson-mass note supplies sufficiency
  conditions and the parity-dichotomy note names the native-log candidate. This
  note attacks exactly that candidate: native free `K_2D`, holonomy cylinder,
  edge tower, spectral eta labels.
- **N5, rhetoric audit.** The negative wording is route-local: "native free
  kernel on this sufficiency route." It is not a statement about every possible
  boundary mechanism, interaction, gauge-integrated transfer, or dimensional
  lift.
- **N6, partial-closure scan.** The measured orientation-odd same-parity tail is
  a partial positive: it preserves a possible downstream route if another
  derived mechanism creates the missing edge tower.
- **N7, steelman.** The strongest objection is that the nonzero
  holonomy-dependent orientation-odd tail is the hard part, and a different
  spectral centering or boundary projection might expose the tower. The runner
  rejects that objection only for the #3585 accepted readout: actual
  zero-centered in-gap states with `0.99` edge localization and spectral eta
  stability.
- **N8, cross-cycle echo.** The prior pure-staggered containment and
  parity-dichotomy references warned that parity-flipping-only matter cannot
  host the datum while the transfer log might escape that obstruction. This
  note confirms the escape component but names the remaining wall more sharply:
  no edge tower appears in the native free transfer log.

## References

Retained one-hop authorities:

- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  — supplies the free staggered two-step blocked transfer construction and
  the `exp(-2E(p))` decaying-channel convention.
- [`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
  — supplies the native free log-generator symbol, even-distance support, and
  sharp rate `eta* = arcsinh(m)`.

Plain-text construction references, in-flight and not cited as retained
authorities:

- `.claude/tmp/signed-gravity-refs/SIGNED_GRAVITY_PRODUCT_GRADING_ETA_SECTOR_SELECTION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md`
  (in-flight, cited as construction reference).
- `.claude/tmp/signed-gravity-refs/SIGNED_GRAVITY_WILSON_MASS_HOLONOMY_TWISTED_EDGE_REALIZATION_NARROW_THEOREM_NOTE_2026-06-11.md`
  (in-flight, cited as construction reference).
- `.claude/tmp/signed-gravity-refs/SIGNED_GRAVITY_PARITY_GRADING_ESCAPE_DICHOTOMY_NARROW_THEOREM_NOTE_2026-06-11.md`
  (in-flight, cited as construction reference).
