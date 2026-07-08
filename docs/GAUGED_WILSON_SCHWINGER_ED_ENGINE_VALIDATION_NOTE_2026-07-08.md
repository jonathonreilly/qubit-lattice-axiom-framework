# Gauged Wilson Schwinger ED Engine Validation Note

**Date:** 2026-07-08
**Type:** exact_support (machinery validation, no physics claim)
**Claim type:** exact_support
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/gauged_wilson_schwinger_ed_engine_2026_07_08.py`](../scripts/gauged_wilson_schwinger_ed_engine_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/gauged_wilson_schwinger_ed_engine_2026_07_08.txt`](../logs/runner-cache/gauged_wilson_schwinger_ed_engine_2026_07_08.txt)

## Purpose

This note records validation of a SECOND exact-diagonalization
comparator for the gauged mass lane: Hamiltonian WILSON fermions
(two-component spinors, Wilson parameter `r = 1`) with `U(1)` links and
the ring Gauss law reduced to a single Wilson-line rotor. The
construction is declared import **I-GAUGE-W**: a Wilson-kernel bridge
instantiation of the covariant-hopping interaction class that the
record-preservation dynamics-form theorem forces (the Wilson term is a
gauge-invariant local operator, hence in-class). It is a bridge
realization, not a derivation of the framework's gauged surface.

The engine exists for one specific reason: the staggered comparator's
two-band identity test filed a bounded methods no-go whose
strong-coupling wall was the second meson's zone-origin migration -- a
staggered-kernel artifact. The Wilson kernel has no zone split: both
meson bands rest at `P = 0` and the doubler is gapped by construction.

## Convention Note

Three kernels are now in play and must never be conflated: the two-step
transfer kernel (`arcsinh` dispersion), the staggered Hamiltonian
kernel (`E(p) = sqrt(m^2 + sin^2 p)`, two-site cell, momentum unit
`P = theta/2`), and this Wilson Hamiltonian kernel:

```text
    E(p) = sqrt( sin^2 p + (m + r(1 - cos p))^2 ),   r = 1,
```

one-site cell, momentum `P = theta` directly (no halving). The hop
matrix is `K = -(i sigma1 + r sigma3)/2` with staggered-free
half-filling background `q_n = (n_u + n_d)_n - 1`.

## Validated Properties (supervisor-executed)

- gauge/translation symmetry commutator gated at `1e-12` on random
  vectors, with exact Gauss/charge checks; the magnetic translation's
  rotor shift is `DeltaW = -q[N-1]` (verified, printed);
- free-limit particle-hole dispersion agreement with the one-body
  Wilson theory at `1e-10` per momentum sector, and the one-body band
  equals the displayed `E(p)` at `1e-12`;
- **doubler absence**: `E(pi) = m + 2r` exactly (`1e-12`) -- the Wilson
  term gaps the doubler; `E(0) = m`;
- Wilson-rotor truncation convergence `W_MAX 3 -> 4` at `1e-10`;
- momentum-sector reassembly against the unprojected spectrum at
  `1e-10`;
- gapped mesons with momentum resolution at `(N = 8, m = 0.3)`:
  band-1 `P = 0` gaps `0.9934 (g = 0.6)` and `1.3253 (g = 1.0)`;
  band-2 seeds `1.2834` and `2.1969` -- both BELOW the two-meson
  threshold (`2 x band-1 = 1.987 / 2.651`) and rising with `P`
  (`1.746 / 2.365` at `P = 2pi/8`): discrete second mesons with normal
  dispersion, exactly the configuration the identity test needs.

Supervisor-executed result:

```text
TOTAL PASS elapsed=98.03s flags=Q0-ring-Gauss,finite-W-translation-interior,wilson-r1-no-doublers,g0-Uholo-shifts-W
```

## Boundaries

- `d = 1` comparator; validation sizes `N in {6, 8}` (note `N = 8`
  Wilson sites carry 16 fermionic modes -- the same many-body
  dimension class as `N = 16` staggered sites).
- I-GAUGE-W is an import/bridge realization; no equivalence claim; no
  gravitational content; machinery validation only.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  -- the forced class I-GAUGE-W instantiates.
- [`GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md`](GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md)
  -- the structural template and the kernel-convention split.
- [`GAUGED_TWO_BAND_MASS_ENERGY_EQUIVALENCE_OPERATOR_TAGGED_NOTE_2026-07-08.md`](GAUGED_TWO_BAND_MASS_ENERGY_EQUIVALENCE_OPERATOR_TAGGED_NOTE_2026-07-08.md)
  -- the no-go whose named escape (Wilson kernel) this engine executes.

## Changelog

- **2026-07-08.** Initial note. Worker-drafted engine, supervisor
  line-reviewed (independent one-body construction verified against the
  analytic band; hop matrix symbol check in-code) and
  supervisor-executed.
