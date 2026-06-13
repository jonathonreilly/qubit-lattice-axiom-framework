# Gauge-Vacuum Plaquette Window Top-Down Integral Displacement Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Claim boundary:** finite W52 top-down Wilson-character integral gate at
`beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`, source `NMAX = 7`,
and source `MODE_MAX = 200`. The note reverse-anchors the one-word
Haar/character integral against the in-repo `T = D M D M^T D` builder,
rebuilds the 2x2 trivial-window W44 `k = 2` gate, and identifies the exact
remaining window-specific integral needed before a fundamental-window
displacement can be reported.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_window_top_down_integral_displacement_bounded_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_window_top_down_integral_displacement_bounded_2026_06_12.txt

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. Existing finite packet values are restated on
their scoped surfaces. Decimal constants below are finite-runner decimal
outputs; no exact-arithmetic claim is made for Wilson-coefficient decimals.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the Wilson character-expansion and shared-link Haar-integration
  language.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `D_lambda = c_lambda(6)/(d_lambda c_0(6))` convention and
  the one-word `diag_c . (N_f + N_fbar) . diag_c . (N_f + N_fbar)^T . diag_c`
  construction row.
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

Context pointers, not one-hop authorities:
scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_window_intertwiner_basis_displacement_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_window_clebsch_insertion_displacement_bounded_2026_06_12.py,
scripts/frontier_su3_wigner_intertwiner_engine.py,
scripts/frontier_su3_wigner_4fold_haar_projector.py,
scripts/cl3_ks_su3_rep_infrastructure_2026_05_07_w1full.py,
scripts/cl3_ks_su3_clebsch_gordan_2026_05_07_w1full.py.

## Method Anchor

The W52 method gate is the one-word reverse anchor. Let `B_4` be the 25-label
finite dominant-weight box, let

```text
D_lambda = c_lambda(6)/(d_lambda c_0(6)),
M = N_f + N_fbar,
```

and let `N_f`, `N_fbar` be the finite fundamental and antifundamental Pieri
fusion matrices. The top-down one-word character integral has the row

```text
T_ab = D_a * sum_x M_ax D_x M_bx * D_b.
```

Equivalently,

```text
T = D M D M^T D.
```

The three `D` factors are the three normalized Wilson character coefficients
surviving on the one-word packet: left end, middle channel, and right end. The
two `M` factors are the two link Haar integrations where the fundamental or
antifundamental character channel fuses the neighboring class label into the
intermediate label. The two-character Schur identity used at matching links is

```text
int dU D^lambda(U)_ij D^mu(U^(-1))_kl
  = delta_lambda_mu delta_il delta_jk / d_lambda.
```

The runner rebuilds this row from the finite packet and compares it against
both in-repo one-word builders:

```text
one-word states = 25
D_(0,0) = 1.000000000000000
D_(1,0) = 0.422531739649983
c_fund(6)/c_0(6) = 1.267595218949950
max |T_reverse - T_builder| = 0.000e+00
max |T_reverse - T_existing| = 0.000e+00
```

This discharges the method gate for the one-word packet. The top-down
machinery is therefore not blocked at the `D M D M^T D` surface.

## 2x2 Window Integral

Use the W45 orientation for one window face:

```text
T_j L_2 T_(j+1)^(-1) L_1^(-1).
```

The established fundamental truncation writes the window factor as

```text
W_window = 1
         + (c_fund(6)/c_0(6))
           chi_fund(T_j L_2 T_(j+1)^(-1) L_1^(-1)).
```

The trivial channel is the identity insertion. It removes the four-link
window character and returns the W44 unwindowed strip-word assembly. The
fundamental channel places one fundamental matrix coefficient on each of the
four window links. Each two-character matching link contributes a Schur
factor. A link that sees an adjacent external label and the fundamental
window insertion is a three-character link and requires a normalized map of
the form

```text
Hom(V_a x V_3, V_c)
```

or its antifundamental counterpart.

W48 and W50 close the unit invariant carried by the four fundamental legs.
With index order `3bar, 3, 3bar, 3`,

```text
T1[a,b;c,d] = delta_ab delta_cd,
T2[a,b;c,d] = delta_ad delta_cb.
```

The exact Gram matrix is

```text
<T1,T1> = 9,
<T2,T2> = 9,
<T1,T2> = 3.
```

The W50 isometries split

```text
3 x 3bar = 1 + 8,
V_1 = vec(I_3)/sqrt(3),
V_8[A] = vec(lambda_A)/sqrt(2).
```

The runner rechecks the W48/W50 unit object:

```text
normalized T2/3 components in E1/E8 basis:
  (0.333333333333333, 0.942809041582063)

four fundamental Schur factors = 1/81
K_f = (c_fund(6)/c_0(6)) * (1/3)^4 * T2
```

This is exact on the unit `3bar-3-3bar-3` subspace, up to the displayed
finite-packet Wilson coefficient decimal.

## Assembly Gate

For the trivial window channel, the 625-state W44 layer-to-layer transfer is
rebuilt through the existing strip-word code. The result is:

```text
P(k=2, window -> 0) = 0.449370834209281
W44 k=2 anchor        = 0.449370834209281
delta_zero_window     = +3.885780586188048e-16

W44 deep limit        = 0.615191992185898
pair-support limit    = 0.615191992185898
```

The runner also checks the W44 transfer symmetries and admissibility on the
trivial-window object:

```text
transfer symmetry residual = 2.776e-17
pair-swap residual = 2.220e-16
conjugation-swap residual = 2.776e-17
transfer min entry = 0.000e+00
```

Thus gate (a), the trivial-window reproduction of W44 `k = 2`, is satisfied
within the finite-runner tolerance. Gates (b) and (c) are satisfied for the
trivial-window transfer. The nontrivial fundamental-window transfer is not
published by this note.

## Fundamental Channel Result

The fundamental window support is not empty:

```text
B4 fundamental transitions a x 3 -> c = 56
B4 antifundamental transitions b x 3bar -> d = 56
diagonal fundamental transitions = 0
pair-window support entries before Clebsch/Racah weights = 3136
```

Therefore this is not a zero-selection result. The missing object is not
support. The missing object is the normalized external-label Clebsch/Racah
contraction over B4:

```text
sum over alpha,beta
  C[a,3 -> c; alpha]
  C[b,3bar -> d; beta]
  R[a,b,c,d; alpha,beta]
```

with normalization compatible with the dimension-stripped W44 longitudinal
bond. W48/W50 supply the unit `3 x 3bar = 1 + 8` isometries and the
`T1/T2` invariant basis; they do not supply the normalized maps
`Hom(V_a x V_3, V_c)` and `Hom(V_b x V_3bar, V_d)` for every label in the
`B_4` box.

The reported W52 numeric output is therefore:

```text
P(k=2, windowed fundamental) = NOT_REPORTED
displacement_vs_anchor = NOT_REPORTED
sign = NOT_REPORTED
magnitude = NOT_REPORTED
windowed deep probe = NOT_RUN
```

This is outcome (c): a genuine integral obstruction after the method gate.
The obstruction is window-specific and is named above. It is not the one-word
anchor, not the W44 trivial-channel assembly, not the `T1/T2` unit invariant,
and not the `1 + 8` unit isometry.

## Gates

| gate | result |
|---|---|
| one-word top-down reverse anchor reproduces `D M D M^T D` | PASS |
| trivial window channel reproduces W44 `k = 2` | PASS |
| trivial-window transfer has conjugation-swap and pair-swap symmetries | PASS |
| trivial-window transfer is entrywise nonnegative | PASS |
| W48 `T1/T2` unit invariant rebuilt | PASS |
| W50 `V_1/V_8` unit isometries rebuilt | PASS |
| fundamental support nonempty | PASS |
| fundamental displacement | not reported; missing normalized external-label Clebsch/Racah contraction over B4 |

## No-Go Discipline Gate

This is a bounded obstruction statement, not a broad program statement. The
negative part is narrow: this runner cannot report the fundamental-window
`k = 2` displacement without the B4 external-label Clebsch/Racah contraction.

**N1 alternative routes checked.**

| route | outcome on this bounded claim | marker |
|---|---|---|
| Reverse-anchor the one-word integral and reuse it for the block | Succeeds for `T = D M D M^T D`, but the window face adds four-link fundamental matrix coefficients not present in the one-word row. | ATTEMPTED |
| Use the trivial window channel | Succeeds and reproduces W44 `k = 2`, but it is the switch-off gate, not the fundamental channel. | ATTEMPTED |
| Use W48 `T1/T2` alone | Succeeds on the unit `3bar-3-3bar-3` invariant, but it has no arbitrary B4 external labels. | ATTEMPTED |
| Use W50 `V_1/V_8` alone | Succeeds for `3 x 3bar = 1 + 8`, but it does not provide `Hom(V_a x V_3, V_c)` maps across all B4 labels. | ATTEMPTED |
| Use support counts as weights | Fails because 3136 allowed entries do not determine normalized matrix elements, signs, or recoupling weights. | ATTEMPTED |
| Use adjoint Wigner context files | Fails for this insertion because those files are adjoint-sector or sampled-projector context, not the deterministic B4 fundamental external-label kernel. | ATTEMPTED |

**N2 wall-independence audit.** The collapsed wall set has one item:
normalized external-label Clebsch/Racah contraction over B4. The one-word
method gate, the trivial-channel W44 gate, and the unit invariant checks are
not independent walls after this runner; they are passed gates.

**N3 hidden-wall scan.** Phrases such as "same integral", "W44 builder",
"unit invariant", and "window support" were checked. The load-bearing hidden
admission is explicit: support and the unit invariant do not determine the
full B4 external-label contraction. No further hidden wall is used to produce
a numeric result, because no numeric result is produced.

**N4 residual matching.** W45 named a missing non-class window recoupling
object; W48 named the missing lift from `T1/T2` to the 625-state strip
kernel; W50 named the missing external-label kernel after the `1 + 8`
isometries. W52 matches that residual but narrows it after the method gate:
the remaining object is specifically the normalized external-label
Clebsch/Racah contraction over B4 inside the top-down window integral.

**N5 rhetoric audit.** The statement is at finite-block resolution only:
`beta = 6`, `B_4`, the W44 625-state box, and the fundamental window
truncation. It does not speak about all future direct magnetic-index builds,
all tensor-network engines, larger boxes, or higher window channels.

**N6 partial-closure path scan.** A deterministic construction of the B4
maps `Hom(V_a x V_3, V_c)` and `Hom(V_b x V_3bar, V_d)`, followed by their
four-corner contraction, would close the named wall without changing the
one-word anchor or importing a new comparator. Existing context scripts point
toward possible representation-infrastructure directions, but this runner
does not use sampled Haar projectors or external tables as exact W52 input.

**N7 steelman.** A direct magnetic-index build could bypass a separately
named 625-state kernel by representing every B4 irrep explicitly, applying the
four-link window character, and integrating all links with exact projectors.
That would be a valid way to compute the same B4 contraction. The present
runner does not implement those representation matrices and projectors
deterministically, so this note reports a bounded obstruction rather than a
zero displacement.

**N8 cross-cycle echo.** The same wall shape appears in W45, W48, W50, and
the SU3 tensor-network engine roadmap context: fusion counts are available
before normalized intertwiners and link projectors. W52 removes the one-word
method uncertainty but leaves the same B4 external-label contraction as an
open target.

## Runner Command

```bash
python3 scripts/gauge_vacuum_plaquette_window_top_down_integral_displacement_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=37, FAIL=0
```

Cache regeneration:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_window_top_down_integral_displacement_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
