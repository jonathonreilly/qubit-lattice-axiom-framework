# Gauge-Vacuum Plaquette SU3 CG Library Window Displacement Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane. This source note does not set,
predict, promote, or demote any audit outcome and does not edit audit-owned
registry, ledger, queue, or publication-status surfaces.
**Primary runner:** `scripts/gauge_vacuum_plaquette_su3_cg_library_window_displacement_bounded_2026_06_12.py`
**Reusable CG module:** `scripts/su3_fundamental_fusion_cg_b4.py`
**Runner cache:** `logs/runner-cache/gauge_vacuum_plaquette_su3_cg_library_window_displacement_bounded_2026_06_12.txt`

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane owns status.

**Claim boundary:** finite W53 construction of normalized SU(3)
fundamental-fusion Clebsch-Gordan isometries for B4 source labels, the
one-step product closure needed for completeness checks, and the W52
fundamental-window `k = 2` insertion on the W44 B4 pair-label surface at
`beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`,
and source `MODE_MAX = 200`.

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. Existing finite packet values are restated on
their scoped surfaces. Decimal constants below are finite-runner decimal
outputs; no exact-arithmetic claim is made for Wilson-coefficient or Perron
readout decimals.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the Wilson character-expansion and shared-link Haar-integration
  language.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `D_lambda = c_lambda(6)/(d_lambda c_0(6))` convention,
  finite B4 packet, and fundamental / antifundamental fusion matrices.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the same-link matrix-coefficient Schur factor.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the character-level convolution dictionary and inverse-dimension
  normalization.
- [GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the adjacent-word inverse-dimension bond used by the W44 strip-word
  construction.
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
  for the source readout surface used after the finite packet supplies a
  boundary-character vector.

Repo-local context pointers, not one-hop authorities:
scripts/gauge_vacuum_plaquette_window_clebsch_insertion_displacement_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_window_top_down_integral_displacement_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py.
The W50 singlet-isometry and W52 top-down checks are reproduced by the runner
gates above; no tool-worktree artifact is a source dependency.

## CG Library

The reusable module constructs explicit Hermitian generators for SU(3) irreps.
The seeds are `(0,0)`, `(1,0)` with `lambda_A/2`, and `(0,1)` with
`-(lambda_A/2)^T`. Higher labels are realized from `3 x (p,q)` by diagonalizing

```text
C2 = sum_A (T_A total)^2
```

and selecting the target block with

```text
C2(p,q) = (p^2 + q^2 + p q)/3 + p + q.
```

For all B4 source products, the three possible fundamental outcomes have
separate quadratic-Casimir values. No cubic-Casimir or weight-multiplicity
fallback was used.

The module builds all 25 B4 irreps and a one-step closure halo so that every
full product from a B4 source has a completeness check. The W44 contraction
below still restricts label states to the finite B4 packet.

Runner checks:

```text
B4 irrep count = 25
one-step closure irrep count = 35
B4 max dimension = 125 at (4,4)
closure max dimension = 165
C2-degenerate B4 fundamental products = ()
max B4 commutator residual = 4.136e-15
max B4 C2 residual = 9.237e-14
```

The CG isometries are

```text
V[a -> c] : H_c -> H_3 x H_a
W[b -> d] : H_d -> H_3bar x H_b.
```

The product eigenspace is aligned to the realized target basis by solving the
generator intertwiner relation after a deterministic Hermitian polynomial
probe separates basis degeneracies. The reported residual is the direct
generator residual, not the probe residual.

```text
fundamental isometries from B4 sources = 65
antifundamental isometries from B4 sources = 65
max intertwiner residual = 9.212e-10
max V^dag V - I residual = 3.331e-15
max VV^dag - P_C2 residual = 1.887e-15
max product completeness residual = 2.220e-15
W50 |<vec(I)/sqrt(3), V_(3 x 3bar -> 1)>| = 1.000000000000000
```

Thus the W50 `3 x 3bar -> 1` singlet is reproduced up to phase on the same
finite convention.

## Window Bond

For B4 labels `a,b,c,d`, the oriented fundamental window transition is

```text
a x 3    -> c
b x 3bar -> d.
```

The runner evaluates the phase-insensitive projector factor

```text
F(a,b;c,d)
  = Tr[(V V^dag x W W^dag)(P_singlet x I)] / (dim(c) dim(d)).
```

Equivalently, with

```text
R^V_ij = sum_{alpha,gamma} V_{i alpha,gamma} conjugate(V_{j alpha,gamma})
R^W_ij = sum_{mu,delta} W_{i mu,delta} conjugate(W_{j mu,delta}),
```

Schur covariance gives `R^V = dim(c) I_3 / 3` and
`R^W = dim(d) I_3 / 3`, so every allowed B4 transition has

```text
F(a,b;c,d) = 1/9.
```

The runner computes this from `V V^dag` and `W W^dag`, so independent column
phases cannot affect the bond.

```text
B4 fundamental transitions a x 3 -> c = 56
B4 antifundamental transitions b x 3bar -> d = 56
B4 pair-window support entries = 3136
nonzero fundamental bond entries = 3136
CG projector factor min/max = 0.111111111111111 / 0.111111111111111
```

The W44 middle bond used for the direct `k = 2` solve is

```text
B_window = B_0 + (c_fund(6)/c_0(6)) B_f,
B_0[(a,b),(c,d)] = delta_ac delta_bd / (dim(a) dim(b)),
B_f[(a,b),(c,d)] = 1/9  if a x 3 -> c and b x 3bar -> d inside B4,
                    0    otherwise.
```

The existing strip layer coefficients dress this as

```text
middle[(a,b),(c,d)]
  = d_pair(a,b) B_window[(a,b),(c,d)] d_pair(c,d).
```

## Numeric Readout

The direct solver first replays the zero-window bond on the same path:

```text
c_fund(6)/c_0(6) = 1.267595218949950
zero-window direct eig = 1.664872828075301e-01
zero-window residual = 4.564e-15
P(k=2, window -> 0) = 0.449370834209279
W44 k=2 anchor        = 0.449370834209281
delta_zero_window     = -1.942890293094024e-15
```

With the oriented fundamental window bond inserted:

```text
full-window direct eig = 1.951223619010708e-01
full-window residual = 1.177e-14
P(k=2, windowed fundamental) = 0.445084590711323
displacement_vs_anchor = -4.286243497957531e-03
sign = negative
magnitude = 4.286243497957531e-03
```

This is a finite B4, finite-mode, oriented fundamental-window readout. It is
not an infinite-box, higher-window-channel, or conjugate-symmetrized-window
statement. Boundary transitions that leave B4 are present in the library
completeness halo but are not W44 state labels in this finite readout.

## Gates

| gate | result |
|---|---|
| all 25 B4 irreps realized with correct dimensions | PASS |
| B4 product C2 eigenvalues separated; no fallback used | PASS |
| SU(3) commutator and C2 residuals small | PASS |
| 65 fundamental and 65 antifundamental B4-source isometries built | PASS |
| `V^dag V = I`, `VV^dag = P_C2`, and product completeness | PASS |
| W50 `3 x 3bar -> 1` singlet cross-check | PASS |
| W52 B4 transition count `56 x 56 = 3136` | PASS |
| projector factor is phase-insensitive and equals `1/9` on allowed B4 transitions | PASS |
| zero-window direct solve reproduces W44 `k = 2` | PASS |
| oriented fundamental-window `k = 2` number reported | PASS |

## Residual Ledger

Named open targets after this finite readout: B4 boundary truncation versus
larger boxes; higher window channels; conjugate-orientation or real-window
combination if that surface is requested; source/tensor mode extension;
analytic infinite-volume control. These are not retired by the W53 finite
number.

## Reproduction

Run:

```text
python3 scripts/gauge_vacuum_plaquette_su3_cg_library_window_displacement_bounded_2026_06_12.py
```

Regenerate cache:

```text
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_su3_cg_library_window_displacement_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
