# Gauge-Vacuum Plaquette Window Intertwiner Basis Displacement Bounded Note

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim boundary:** finite construction of the universal
`Inv(3bar x 3 x 3bar x 3)` window tensor basis, its exact Gram
normalization, explicit non-random `SU(3)` invariance checks, and the
four-fundamental Schur normalization of the fundamental window tensor at
`beta = 6` using the existing finite packet coefficient convention. This note
does not report an exact nonzero `P(k=2, windowed fundamental)` value because
the universal four-fundamental invariant still has to be lifted through
normalized external-label Clebsch maps before it becomes a 625-state W44 strip
kernel.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_window_intertwiner_basis_displacement_bounded_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_window_intertwiner_basis_displacement_bounded_2026_06_12.txt

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. Existing finite packet values are restated on
their scoped surfaces. Decimal constants below are finite-runner decimal
outputs; no exact-arithmetic claim is made for the Wilson coefficient
decimals.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the character-expansion and shared-link Haar-integration language.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `D_lambda = c_lambda(6)/(d_lambda c_0(6))` convention and
  the `NMAX = 4`, `MODE_MAX = 80` tensor-word packet.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the same-link matrix-coefficient Schur factor `1/d_lambda`.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the character-level Schur convolution dictionary.
- [GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)
  for the W44 adjacent-word matrix-element bond and inverse-dimension
  normalization.
- [BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md](BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md)
  for the previously named non-abelian recoupling/intertwiner network wall.

Context pointers, not one-hop authorities:
scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py,
docs/SU3_WIGNER_INTERTWINER_BLOCK1_THEOREM_NOTE_2026-05-03.md,
docs/SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md.

## Index Convention

Use the W45 window orientation

```text
T_j L_2 T_(j+1)^(-1) L_1^(-1)
```

on the rectangular face with corners `(rail 1, layer j)`,
`(rail 2, layer j)`, `(rail 1, layer j+1)`, and
`(rail 2, layer j+1)`.

The four fundamental-index legs are ordered as

```text
a: 3bar leg at (rail 1, layer j)
b: 3    leg at (rail 2, layer j)
c: 3bar leg at (rail 1, layer j+1)
d: 3    leg at (rail 2, layer j+1)
```

With that order,

```text
T1[a,b;c,d] = delta_ab delta_cd
T2[a,b;c,d] = delta_ad delta_cb
```

`T1` is the same-layer transverse singlet pairing. `T2` is the oriented
plaquette-trace pairing for the fundamental window character in this corner
order.

## Basis And Normalization

The runner constructs `T1` and `T2` directly from Kronecker deltas and sums the
natural inner product over all four indices. The exact Gram matrix is

```text
<T1,T1> = 9
<T2,T2> = 9
<T1,T2> = 3
det Gram = 72.
```

An orthonormal basis is

```text
E1 = T1 / 3
E2 = (T2 - T1/3) / (2 sqrt(2)).
```

The explicit Gell-Mann completeness check gives

```text
T2 - T1/3 = (1/2) sum_A lambda_A[a,b] lambda_A[c,d],
```

with maximum residual `1.110e-16` in the runner. Thus normalized `T2/3`
splits into singlet and adjoint components with exact squared fractions

```text
singlet fraction = 1/9
adjoint fraction = 8/9.
```

The simultaneous four-leg action is

```text
T'[a,b;c,d]
  = sum_(a',b',c',d')
      conjugate(U[a,a']) U[b,b']
      conjugate(U[c,c']) U[d,d']
      T[a',b';c',d'].
```

For the explicit non-random elements `exp(i t lambda_1)`,
`exp(i t lambda_4)`, and `exp(i t lambda_8)` at fixed `t = 0.37`, the runner
checks unitarity, determinant one, individual fixation of `T1` and `T2`, and
zero residual outside the `T1/T2` span to machine precision.

## Fundamental Window Normalization

The finite packet convention is

```text
D_lambda = c_lambda(6) / (d_lambda c_0(6)).
```

For the fundamental channel,

```text
D_(1,0) = 0.422531739649983
c_fund(6) / c_0(6) = d_fund D_(1,0)
                   = 1.267595218949950.
```

The anti-fundamental packet coefficient agrees by conjugation at the displayed
precision.

On the four-fundamental matrix-coefficient subspace, the fundamental window
character contributes one fundamental matrix coefficient on each of the four
window links. Contracting those four link variables against adjacent
fundamental matrix coefficients uses four Schur factors:

```text
(1/d_fund)^4 = (1/3)^4 = 1/81.
```

Therefore the universal four-fundamental tensor produced by the fundamental
window channel is

```text
K_f = (c_fund(6) / c_0(6)) * (1/3)^4 * T2.
```

Its components are

```text
T1/T2 basis:
  (0, (c_fund/c_0)/81)

E1/E2 basis:
  ((c_fund/c_0)/81, 2 sqrt(2) (c_fund/c_0)/81).
```

This is exact on the stated four-fundamental subspace, up to the finite-packet
decimal evaluation of `c_fund/c_0`.

## W44 Insertion Gate

The new universal invariant is not yet an exact 625-state W44 strip kernel.
The W44 middle labels range over the 25 `B_4` irreps on each rail. A
fundamental window insertion changes those labels through maps of the form

```text
Hom(V_a x 3, V_c)
Hom(V_b x 3bar, V_d)
```

and their four-corner recoupling. The runner checks that the finite packet has
`56` fundamental transitions and `56` anti-fundamental transitions on `B_4`,
with no diagonal fundamental transitions. So replacing the window by a
diagonal scalar would erase the actual label motion.

The existing W44 modules expose fusion multiplicities but no normalized
external-label Clebsch maps or `6j` recoupling API. Fusion counts determine
which entries may be nonzero; they do not determine the normalized matrix
elements of the class-channel kernel. For that reason:

```text
Exact P(k=2, windowed fundamental) is not reported.
```

This is not a zero/cancelling displacement claim. It is a narrower result:
the universal fundamental window tensor and its normalization are built, while
the exact W44 insertion remains an open external-label recoupling target.

The switched-off gate still reproduces W44:

```text
P(k=2, window coupling -> 0) = 0.449370834209281
W44 unwindowed k=2 anchor      = 0.449370834209281
delta_zero_coupling            = +3.885780586188048e-16

W44 strip-word deep limit       = 0.615191992185898
pair-support limit from runner  = 0.615191992185898
```

No `k=3` windowed probe is reported, for the same external-label recoupling
reason. Higher window channels remain named open targets.

## Gates

| gate | result |
|---|---|
| `T1/T2` exact Gram matrix `[[9,3],[3,9]]` | PASS |
| orthonormal basis `E1`, `E2` verified numerically | PASS |
| Fierz split of `T2` into singlet and adjoint components | PASS |
| explicit non-random `SU(3)` invariance checks | PASS |
| fundamental Wilson strength stated as `c_fund(6)/c_0(6)` | PASS |
| four-link Schur normalization `(1/3)^4` | PASS |
| exact four-fundamental tensor `K_f` built | PASS |
| zero window coupling reproduces W44 `k=2` | PASS |
| exact fundamental-window W44 displacement | not reported; external-label recoupling remains open |
| truncation-exactness statement | exact on the stated four-fundamental subspace; higher channels and the W44 lift remain open |

## No-Go Discipline Gate

This is a bounded partial wall statement, not a broad no-go. The negative is:
the universal four-fundamental invariant basis does not by itself determine the
625-state W44 strip kernel.

**N1 alternative routes checked.**

| route | outcome on this bounded claim | marker |
|---|---|---|
| Treat `K_f` as a diagonal scalar multiplying the W44 middle bond | Fails on the finite packet because fundamental insertion has 56 non-diagonal `B_4` transitions and no diagonal fundamental transitions. | ATTEMPTED |
| Use fusion multiplicities as the window kernel | Fails because multiplicities give allowed channels, not normalized Clebsch maps or four-corner matrix elements. | ATTEMPTED |
| Use the `T2 = 1/3 T1 + adjoint` Fierz fractions as a class-channel kernel | Fails because those fractions live in the universal four-fundamental space, while W44 labels are arbitrary `B_4` irreps. | ATTEMPTED |
| Reuse the per-rail W44 `delta/d` bond | Fails for the nontrivial channel because that bond is exactly the switched-off longitudinal contraction. | ATTEMPTED |
| Reuse the previous adjoint Wigner context | Fails for this strip insertion because the context is adjoint-sector infrastructure, not normalized maps `Hom(V_a x 3, V_c)` across all W44 labels. | ATTEMPTED |
| Import an external `SU(3)` `6j` table or package | Blocked by the no-new-import rule for this task. | ATTEMPTED |

**N2 wall independence.** The collapsed wall set has one item: construct the
normalized external-label Clebsch/recoupling maps needed to lift the universal
`3bar-3-3bar-3` tensor into the W44 625-state strip kernel. Finite `B_4`,
finite Bessel support, higher window channels, wider slabs, `L_perp`, analytic
`P(6)`, and repinning remain real residuals, but they are not needed to explain
why this note does not report the fundamental-window `k=2` displacement.

**N3 hidden-wall scan.** Phrases such as finite packet, four-fundamental
subspace, and W44 lift are load-bearing scope controls. The note avoids
phrases that would silently assert a full physical spatial-environment
contraction.

**N4 residual matching.** The old W45 window note named the missing
fundamental window intertwiner/recoupling normalization. This note closes the
universal four-fundamental basis and four-link Schur normalization part of
that residual, but not the external-label W44 lift. The beta=6 tensor-network
wall names the broader non-abelian recoupling/treewidth residual; this note's
remaining wall is a narrower instance of that shape.

**N5 rhetoric audit.** The phrase "does not report exact windowed
displacement" is scoped to the W44 625-state class-channel object. It is not a
claim about all future Wigner-Racah, direct magnetic-index, or tensor-network
computations.

**N6 partial-closure path scan.** A repo-local construction of normalized
`Hom(V_a x 3, V_c)` and `Hom(V_b x 3bar, V_d)` maps on the `B_4` box, followed
by the four-corner recoupling contraction, would retire the remaining wall
without a new axiom. No approved primitive in docs/audit/data/axiom_premise_nodes.json
supplies that map.

**N7 steelman.** A reviewer can fairly object that the remaining lift is a
finite representation-theory computation, not a conceptual obstruction: the
same explicit-matrix strategy used here for the universal tensor could be
extended to all `B_4` labels by constructing concrete representation bases and
Clebsch maps, then inserting the resulting dense 625-state middle kernel into
the existing direct `k=2` solver. This note accepts that as the next exact
route and therefore reports a partial result rather than a fundamental-window
displacement.

**N8 cross-cycle echo.** Prior plaquette tensor-network notes already name
non-abelian recoupling/intertwiner computation as the live `D >= 3` contraction
object. The present wall has the same shape at smaller scope: the universal
four-fundamental tensor is now explicit, and the remaining work is the
external-label W44 recoupling lift.

Gate result: PASS for this bounded partial-wall wording.

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_window_intertwiner_basis_displacement_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=34, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_window_intertwiner_basis_displacement_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
