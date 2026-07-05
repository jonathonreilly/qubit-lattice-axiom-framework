# Gauge-Vacuum Plaquette Window Clebsch Insertion Displacement Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Claim boundary:** finite construction of the normalized
`3 x 3bar = 1 + 8` Casimir-projector isometries, their recoupling into the
`Inv(3bar x 3 x 3bar x 3)` window basis, and the W44 insertion gate for the
fundamental window channel at `beta = 6`, tensor `NMAX = 4`, tensor
`MODE_MAX = 80`, source `NMAX = 7`, and source `MODE_MAX = 200`.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_window_clebsch_insertion_displacement_bounded_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_window_clebsch_insertion_displacement_bounded_2026_06_12.txt

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. Existing finite packet values are restated on
their scoped surfaces. Decimal constants below are finite-runner decimal
outputs; no exact-arithmetic claim is made for Wilson-coefficient decimals.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the Wilson character-expansion and shared-link Haar-integration
  language.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `D_lambda = c_lambda(6)/(d_lambda c_0(6))` convention,
  finite `B_4` packet, and fundamental / anti-fundamental fusion matrices.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the same-link matrix-coefficient Schur factor.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the character-level convolution dictionary and inverse-dimension
  normalization.
- [GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the W44 adjacent-word matrix-element bond and finite-packet boundary
  readout.
- [BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md](BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md)
  for the broader previously named non-abelian recoupling/intertwiner network
  obstacle shape.

Context pointers, not one-hop authorities:
scripts/gauge_vacuum_plaquette_window_intertwiner_basis_displacement_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py,
docs/SU3_TENSOR_NETWORK_ENGINE_ROADMAP_NOTE_2026-05-03.md,
docs/SU3_WIGNER_INTERTWINER_BLOCK1_THEOREM_NOTE_2026-05-03.md,
docs/SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md.

## Casimir Isometries

Use explicit Gell-Mann matrices `lambda_A`, normalized by
`Tr(lambda_A lambda_B) = 2 delta_AB`, and product generators on
`3 x 3bar`

```text
T_A(total) = (lambda_A/2) x I + I x (-conjugate(lambda_A)/2).
```

The runner forms

```text
C2 = sum_A T_A(total)^2.
```

On the 9-dimensional product space the eigenvalues are one `0` and eight `3`s.
Therefore the projectors are the polynomial projectors

```text
P_1 = I - C2/3,
P_8 = C2/3.
```

The normalized isometries are

```text
V_1 = vec(I_3) / sqrt(3),
V_8[A] = vec(lambda_A) / sqrt(2),  A = 1,...,8.
```

The runner verifies

```text
V_1^dag V_1 = 1,
V_8^dag V_8 = I_8,
V_1^dag V_8 = 0,
V_1 V_1^dag = P_1,
V_8 V_8^dag = P_8,
P_1 + P_8 = I_9.
```

It also checks deterministic `SU(3)` elements `exp(i t lambda_1)`,
`exp(i t lambda_4)`, and `exp(i t lambda_8)` at `t = 0.37`: `P_1` and
`P_8` commute with the product action, `V_1` is fixed, and the induced
`V_8` block is unitary.

## Recoupling Map

Use the W48 window index order

```text
a: 3bar leg at (rail 1, layer j)
b: 3    leg at (rail 2, layer j)
c: 3bar leg at (rail 1, layer j+1)
d: 3    leg at (rail 2, layer j+1).
```

The two delta tensors are

```text
T1[a,b;c,d] = delta_ab delta_cd,
T2[a,b;c,d] = delta_ad delta_cb.
```

Their exact Gram matrix is

```text
<T1,T1> = 9,
<T2,T2> = 9,
<T1,T2> = 3.
```

The isometry route gives the orthonormal basis

```text
E1 = V_1(ab) V_1(cd) = T1/3,
E8 = (1/sqrt(8)) sum_A V_8[A](ab) V_8[A](cd)
   = (T2 - T1/3)/(2 sqrt(2)).
```

Thus the normalized plaquette-trace invariant is

```text
T2/3 = (1/3) E1 + (2 sqrt(2)/3) E8,
```

with squared singlet/adjoint fractions

```text
1/9 and 8/9.
```

Equivalently, the normalized external-label map for the four unit legs is:

```text
(1,1) channel pair -> E1 with amplitude 1,
(8,A; 8,B) channel pair -> delta_AB E8 / sqrt(8),
mixed 1/8 channel pairs -> 0.
```

This agrees with the direct `T1/T2` Gram route in the runner to numerical
residual below `1e-14`.

## Fundamental Window Tensor

The finite packet convention gives

```text
D_(1,0) = 0.422531739649983,
c_fund(6)/c_0(6) = d_fund D_(1,0)
                 = 1.267595218949950.
```

The four shared window links each contribute the same fundamental
matrix-coefficient Schur factor, so

```text
(1/d_fund)^4 = (1/3)^4 = 1/81.
```

On the four-unit fundamental subspace the fundamental window tensor is

```text
K_f = (c_fund(6)/c_0(6)) * (1/3)^4 * T2.
```

In the normalized `E1/E8` basis:

```text
K_f = (c_fund/c_0)/81 * E1
    + 2 sqrt(2) (c_fund/c_0)/81 * E8.
```

This is exact on the stated four-unit subspace, up to the finite-packet
decimal evaluation of `c_fund/c_0`. It is not an all-channel window statement.

## W44 Insertion Gate

The W44 middle object is a 625-state pair-label kernel. A fundamental window
insertion has non-diagonal `B_4` support:

```text
B4 fundamental transitions a x 3 -> c       = 56
B4 antifundamental transitions b x 3bar -> d = 56
diagonal fundamental transitions              = 0
pair-window support entries before Clebsch weights = 3136
```

The `1 + 8` isometries above supply the normalized recoupling of the four unit
fundamental legs. They do not supply normalized maps for every W44 external
label of the form

```text
Hom(V_a x 3, V_c),
Hom(V_b x 3bar, V_d),
```

nor the associated four-corner `625 x 625` recoupling weights. The current W44
builders expose the finite fusion support but no callable normalized
external-label Clebsch / `6j` kernel for those weights.

Therefore the runner reports:

```text
P(k=2, windowed fundamental) = NOT_REPORTED
displacement_vs_anchor = NOT_REPORTED
sign = NOT_REPORTED
magnitude = NOT_REPORTED
```

This is not a zero/cancelling displacement claim. It is a bounded result: the
unit-leg Clebsch/isometry object and fundamental window tensor are closed, but
the exact 625-state W44 insertion remains a named kernel target.

The switch-off gate still reproduces W44:

```text
P(k=2, window -> 0) = 0.449370834209281
W44 k=2 anchor        = 0.449370834209281
delta_zero_window     = +3.885780586188048e-16

W44 deep limit        = 0.615191992185898
pair-support limit    = 0.615191992185898
```

No `k = 3` windowed probe is reported because it requires the same 625-state
window recoupling kernel. Higher window channels remain named open targets.

## Gates

| gate | result |
|---|---|
| `3 x 3bar` Casimir eigenvalues `0, 3` | PASS |
| polynomial projectors `P_1`, `P_8` | PASS |
| isometry/completeness for `V_1`, `V_8` | PASS |
| deterministic `SU(3)` equivariance | PASS |
| `T1/T2` Gram exact matrix `[[9,3],[3,9]]` | PASS |
| isometry route agrees with `T1/T2` route | PASS |
| fundamental strength and four Schur factors tracked | PASS |
| zero-window gate reproduces W44 `k = 2` | PASS |
| exact W44 fundamental displacement | not reported; missing 625-state external-label recoupling kernel |
| truncation-exactness statement | exact on the stated four-unit fundamental subspace; higher channels and W44 lift remain open |

## Negative-Claim Discipline Gate

This section scopes the negative part of the result. The negative is narrow:
the completed `3 x 3bar` Casimir-isometry object does not by itself determine
the 625-state W44 middle kernel.

**N1 alternative routes checked.**

| route | outcome on this bounded claim | marker |
|---|---|---|
| Use the Casimir projectors on `3 x 3bar` | Succeeds for the unit-leg `1 + 8` isometries and recoupling, but its carrier is 9-dimensional rather than the W44 625-state external-label kernel. | ATTEMPTED |
| Treat the 3136 pair-window support entries as the kernel | Fails because support does not determine normalized Clebsch weights or signs/phases of the recoupling contraction. | ATTEMPTED |
| Insert the singlet/adjoint fractions `1/9` and `8/9` as class-channel scalars | Fails because those fractions live in `Inv(3bar x 3 x 3bar x 3)`, while W44 labels range over `B_4` irreps. | ATTEMPTED |
| Reuse the W44 diagonal longitudinal bond | Fails because the fundamental insertion has zero diagonal fundamental transitions and requires label motion. | ATTEMPTED |
| Reuse the internal-link scalar factor | Fails because that factor has already summed over class-channel multiplicities and does not expose four-corner magnetic-index maps. | ATTEMPTED |
| Reuse adjoint-sector Wigner context files | Fails for this W44 insertion because those context files do not expose normalized `Hom(V_a x 3, V_c)` maps over the finite `B_4` packet. | ATTEMPTED |
| Import an external `SU(3)` `6j` table or package | Blocked by the no-new-import rule for this task. | ATTEMPTED |

**N2 wall-independence audit.** The collapsed wall set has one item:
construct the normalized 625-state external-label recoupling kernel over the
finite W44 pair labels. Finite `B_4`, finite Bessel support, higher window
channels, wider slabs, `L_perp`, analytic `P(6)`, and repinning remain real
residuals, but they are not needed to explain why this runner does not report
the fundamental-channel W44 displacement.

**N3 hidden-wall scan.** Phrases such as finite packet, four-unit subspace, and
W44 lift are load-bearing scope controls. The approved primitive registry was
checked: scale-reference, kinetic-isotropy, and realized-state primitives do
not supply SU(3) Clebsch maps, and this note does not classify those
primitives as admissions or walls.

**N4 residual matching.** W45 named the missing fundamental window
intertwiner/recoupling normalization. W48 supplied the `T1/T2` invariant basis
and Schur normalization but left the external-label W44 lift open. This note
supplies the explicit `1 + 8` unit-leg isometries and the channel map, while
the remaining residual is narrower: the 625-state external-label kernel for
the W44 middle bond.

**N5 rhetoric audit.** The phrase "does not determine the 625-state W44 middle
kernel" is scoped to the finite W44 pair-label object. It is not a statement
about future direct magnetic-index builds, generic Wigner-Racah engines, or a
full tensor-network contraction.

**N6 partial-closure path scan.** A repo-local construction of concrete
representations for all `B_4` labels, normalized maps
`Hom(V_a x 3, V_c)` and `Hom(V_b x 3bar, V_d)`, and their four-corner
contraction would retire the remaining kernel target without a new axiom. This
is an implementation path, not a physics-premise change. The SU3 tensor-network
roadmap names such a general Clebsch engine as planned infrastructure, but it
is not present as an executable W44 insertion API here.

**N7 steelman.** A hostile reviewer can fairly argue that the Casimir-projector
strategy should be extended from `3 x 3bar` to every finite `B_4` representation
by constructing explicit representation matrices and projectors for
`V_a x 3`, then using projector contractions instead of imported tables. That
would be a finite repo-local route and may produce the requested displacement.
This note does not claim that route fails; it names it as the next exact
implementation target.

**N8 cross-cycle echo.** The beta=6 tensor-network wall and the SU3 engine
roadmap both name non-abelian Clebsch/recoupling infrastructure as missing
for broader lattice-gauge contractions. The present remaining target has the
same shape at W44 scope: the unit-leg map is explicit, and the unresolved
object is the finite external-label recoupling kernel.

Gate result: PASS for this bounded wording.

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_window_clebsch_insertion_displacement_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=50, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_window_clebsch_insertion_displacement_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
