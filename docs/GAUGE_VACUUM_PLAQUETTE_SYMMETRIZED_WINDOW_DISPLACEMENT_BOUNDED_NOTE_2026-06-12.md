# Gauge-Vacuum Plaquette Symmetrized Window Displacement Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Claim boundary:** finite W54 conjugate-symmetrized SU(3) B4 window
measurement at `beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`,
source `NMAX = 7`, and source `MODE_MAX = 200`. The construction uses the
W53 normalized fundamental/antifundamental Clebsch-Gordan isometry library and
the W44 `k = 2` pair-label direct readout, then adds both orientation channels
at the equal Wilson coefficient.

**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_symmetrized_window_displacement_bounded_2026_06_12.py

Reusable CG module:
scripts/su3_fundamental_fusion_cg_b4.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_symmetrized_window_displacement_bounded_2026_06_12.txt

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. Existing finite packet values are restated on
their scoped surfaces. Decimal constants below are finite-runner decimal
outputs; no exact-arithmetic claim is made for Wilson-coefficient or Perron
readout decimals.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for Wilson character-expansion and shared-link Haar-integration language.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `D_lambda = c_lambda(6)/(d_lambda c_0(6))` convention,
  finite B4 packet, and fundamental / antifundamental fusion matrices.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the same-link matrix-coefficient Schur factor.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the character convolution dictionary and inverse-dimension normalization.
- [GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the adjacent-word inverse-dimension bond used by the W44 strip-word
  construction.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source readout surface used after the finite packet supplies a
  boundary-character vector.

Repo-local context pointers, not one-hop authorities:
scripts/gauge_vacuum_plaquette_su3_cg_library_window_displacement_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py,
scripts/su3_fundamental_fusion_cg_b4.py.

## Symmetrized Window

W53 inserted one oriented channel:

```text
a x 3    -> c
b x 3bar -> d.
```

The real Wilson plaquette window also carries the conjugate orientation:

```text
a x 3bar -> c
b x 3    -> d.
```

The finite coefficient packet gives

```text
c_fund(6)/c_0(6) = 1.267595218949950
c_antifund(6)/c_0(6) = 1.267595218949950
```

so the symmetrized middle bond is

```text
B_sym = B_0 + (c_fund(6)/c_0(6)) B_f
            + (c_antifund(6)/c_0(6)) B_fbar.
```

The two branch matrices have the same nonzero count and the same projector
factor:

```text
fundamental branch nonzero entries = 3136
antifundamental branch nonzero entries = 3136
fundamental/antifundamental support overlap = 0
fundamental factor min/max = 0.111111111111111 / 0.111111111111111
antifundamental factor min/max = 0.111111111111111 / 0.111111111111111
conjugation transform residual = 3.886e-16
```

Thus the two orientations add as a linear nonnegative branch-bond sum before
the Perron/source readout. They do not cancel. The final source readout is
nonlinear in the bond, so the measured displacement is not forced to be a
literal factor of two.

## Numeric Readout

The zero-window gate is unchanged:

```text
zero_window: P=0.449370834209279; delta=-1.942890293094024e-15
W44 k=2 anchor = 0.449370834209281
```

The W53 continuity branch is reproduced:

```text
oriented_fundamental: P=0.445084590711323
displacement_vs_anchor = -4.286243497957531e-03
```

The conjugate branch gives the same individual readout on this symmetric B4
surface:

```text
oriented_antifundamental: P=0.445084590711324
displacement_vs_anchor = -4.286243497956643e-03
```

With both branches in the same physical window:

```text
P(k=2, symmetrized window) = 0.443437364621406
displacement_vs_anchor = -5.933469587874829e-03
ratio_sym_displacement_to_oriented = 1.384305299197824
```

This is the finite B4, finite-mode, conjugate-symmetrized `k = 2` readout on
the same surface as W53.

## Adjoint Channel

The same finite coefficient packet gives

```text
c_(1,1)(6)/c_0(6) = 1.298078395839505
```

The adjoint displacement is not evaluated here because the available CG module
builds fundamental and antifundamental `3 x (p,q)` / `3bar x (p,q)`
isometries, not the needed `8 x (p,q)` isometry family.

## Gates

| gate | result |
|---|---|
| finite B4 packet and strip layer built | PASS |
| fundamental and antifundamental fusion recurrences verified | PASS |
| 65 fundamental and 65 antifundamental B4-source isometries built | PASS |
| isometry intertwiner, orthonormality, projector, and completeness checks | PASS |
| `c_fund(6) = c_antifund(6)` verified from coefficient data | PASS |
| antifundamental branch is the conjugation transform of W53 branch | PASS |
| zero-window direct solve reproduces W44 `k = 2` | PASS |
| oriented branch reproduces W53 `P` and displacement | PASS |
| symmetrized branch reports finite negative displacement | PASS |

## Residual Ledger

Named open targets after this finite readout: finite B4 boundary truncation
versus larger boxes; higher window channels; adjoint `8 x (p,q)` CG
contraction; source/tensor mode extension; analytic infinite-volume control;
full physical rim/slab geometry; no canonical repinning.

## Reproduction

Run:

```text
python3 scripts/gauge_vacuum_plaquette_symmetrized_window_displacement_bounded_2026_06_12.py
```

Regenerate cache:

```text
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_symmetrized_window_displacement_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
