# Gauge-Vacuum Plaquette Slab Window Coupling Derived Bounded Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Claim boundary:** finite 2-wide slab-window enumeration and coupling
derivation at `beta = 6`, tensor `NMAX = 4`, tensor `MODE_MAX = 80`,
source `NMAX = 7`, and source `MODE_MAX = 200`. This note identifies the
inter-layer transverse plaquette class in the 2-wide, `k`-deep strip slab.
It derives the formal window coupling and verifies the exact trivial-channel
switch-off gate against W44's `k = 2` value. It does not build the nontrivial
fundamental window transfer because the current strip-word packet supplies
fusion multiplicities but not the needed `3bar-3-3bar-3` non-class
intertwiner basis, recoupling matrix, or normalization.

Status authority: independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome.

Primary runner:
scripts/gauge_vacuum_plaquette_slab_window_coupling_derived_bounded_2026_06_12.py

Runner cache:
logs/runner-cache/gauge_vacuum_plaquette_slab_window_coupling_derived_bounded_2026_06_12.txt

No literature value, new axiom, external citation, new comparator number, or
fitted selector is imported. Existing finite packet values are restated on
their scoped surfaces. Decimal constants below are finite-runner decimal
outputs; no exact-arithmetic claim is made for them.

## One-Hop Authorities

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
  for the finite tensor-transfer construction language: Wilson character
  expansion, shared-link Haar integration, and fusion/intertwiner ingredients.
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
  for the finite `B_4` tensor-word packet, `D_lambda` convention, and
  fundamental / anti-fundamental fusion-multiplicity matrices.
- [GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the Wilson action as a sum over plaquettes and for same-link
  mixed-kernel Schur contraction.
- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  for the character-level Schur convolution identity and the
  inverse-dimension factor.
- [BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md](BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md)
  for the previously named non-abelian link recoupling / intertwiner network
  wall in the `D >= 3` plaquette tensor-network route.

Context pointers, not one-hop authorities:
scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py,
scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py,
docs/SU3_WIGNER_INTERTWINER_BLOCK1_THEOREM_NOTE_2026-05-03.md,
docs/SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md.

## Quote-Anchored Enumeration

The tensor-transfer authority states:

```text
expand each
unmarked spatial plaquette Boltzmann factor in exact SU(3) characters
```

and, for a slice step:

```text
expand every spatial plaquette factor in characters and
integrate all shared slice links.
```

The linkwise factorization authority states:

```text
By definition the Wilson action S_W is a sum over plaquettes
```

and its proof notes that the Wilson action sums over plaquettes, not over
slice-pairs of links. Therefore an inter-layer transverse face in the 2-wide
slab is not optional at the Wilson-action level: it is a plaquette face and
carries a Wilson plaquette weight.

The finite word-packet authority defines the captured one-word object as

```text
tensor_word
         :=  diag_c . ( N_f + N_fbar ) . diag_c . ( N_f + N_fbar )^T . diag_c
```

with `diag_c[(p,q)] = c_(p,q)(6) / (d_(p,q) c_(0,0)(6))` and with `N_f`,
`N_fbar` the finite fundamental / anti-fundamental fusion-multiplicity
matrices. That supplies class-channel Wilson coefficients and fusion
multiplicities, but not magnetic-index Clebsch maps or a four-link `6j`
recoupling matrix.

For the 2-wide, `k`-deep compressed slab, the link/plaquette classes are:

| class | slab object | current scalar architecture |
|---|---|---|
| intra-layer internal links | the rail-to-rail link inside a fixed layer `j` | captured by the W39-derived internal factor `E_D(a,b) = 1 + sum_(lambda != 0) D_lambda N_(a,b)^lambda` |
| per-rail longitudinal links | same-rail links from layer `j` to `j+1` | captured by the W17 bond `delta(a,c)/d_a` on each rail |
| inter-layer transverse plaquettes | the window face with corners `(unit1,j)`, `(unit2,j)`, `(unit1,j+1)`, `(unit2,j+1)` | not captured as a plaquette; its holonomy uses two transverse links and two longitudinal links at once |

The third class is the window class. It is a plaquette of the environment, so
the Wilson action weights it. The current strip-word character expansions do
not capture its nontrivial channels: the intra-layer factor sees the two
transverse links as separate scalar class-channel sums, and the longitudinal
bond sees the two rails as independent diagonal Schur contractions. The
window holonomy couples all four links in one character trace.

## Window Coupling

For one window face between layers `j` and `j+1`, choose an orientation and
write the four link matrices as

```text
T_j       = transverse link inside layer j,
L_2       = longitudinal link on rail 2,
T_(j+1)   = transverse link inside layer j+1,
L_1       = longitudinal link on rail 1.
```

The normalized Wilson plaquette factor is

```text
W_window
  = 1 + sum_(lambda != 0) d_lambda D_lambda
      chi_lambda(T_j L_2 T_(j+1)^(-1) L_1^(-1)),                       (1)
```

where `D_lambda = c_lambda(6)/(d_lambda c_0(6))` is the finite packet
coefficient convention.

Expanding the character into matrix coefficients gives

```text
chi_lambda(A B C^(-1) D^(-1))
  = sum_(r,s,t,u)
      D^lambda(A)_(r,s)
      D^lambda(B)_(s,t)
      D^lambda(C^(-1))_(t,u)
      D^lambda(D^(-1))_(u,r).                                          (2)
```

After multiplying `(2)` into the four adjacent compressed-unit factors, each
of the four shared links is integrated by the same Peter-Weyl / Schur
mechanism used in the one-hop authorities. The surviving nontrivial term has
the form

```text
K_window^lambda((a,b),(c,d))
  = d_lambda D_lambda
    sum_over_intertwiners
      C(a, lambda, c; iota_1)
      C(b, lambda_bar, d; iota_2)
      C(a, b, sigma; kappa_1)
      C(c, d, sigma'; kappa_2)
      F_lambda(iota_1, iota_2, kappa_1, kappa_2),                       (3)
```

with orientations determining which slots use `lambda` and which use
`lambda_bar`. Formula `(3)` is schematic but load-bearing in one respect:
the object is a non-class intertwiner contraction. It is not determined by
the diagonal class sums `N_(a,b)^lambda` alone.

For `lambda = 0`, `(1)` is the identity window channel. The four-link
insertion disappears, and the remaining Haar integrations are exactly the
current per-rail longitudinal contractions. This is the exact switched-off
gate and reproduces W44.

For `lambda = (1,0)` and `lambda = (0,1)`, the window slots carry the
low-dimensional invariant space

```text
3bar x 3 x 3bar x 3.
```

The finite packet can count this space:

```text
3bar x 3 = 1 + 8,
N^0_(3bar x 3 x 3bar x 3) = 2.
```

That count is exact, but it is not the window coupling. A two-dimensional
invariant space still requires a chosen intertwiner basis, normalization, and
the recoupling matrix between the two pairings of the four window legs. The
current W44 modules expose finite character decomposition and fusion
multiplicity helpers; they do not expose a fundamental `3bar-3-3bar-3`
Clebsch/`6j` object. The adjoint Wigner files in the context pointers build
adjoint `(1,1)` infrastructure, not this fundamental window contraction on
the compressed strip packet.

Thus the smallest exact nontrivial window truncation is named precisely:

```text
lambda in {(1,0), (0,1)}
with an explicit 3bar-3-3bar-3 invariant basis,
normalization, and recoupling matrix compatible with the strip packet.
```

It is not built here. The exact current truncation is the trivial window
channel, which is the switch-off gate.

## Measurement

The runner rebuilds the W44 strip object and evaluates the exact
trivial-window gate:

```text
P(k=2, window channel switched off) = 0.449370834209281
W44 unwindowed k=2 reference        = 0.449370834209281
delta_off_minus_W44                = 0.000000000000000

W44 strip-word deep limit           = 0.615191992185898
pair-support limit from runner      = 0.615191992185898
```

This is not a nontrivial windowed measurement. It says the switch-off gate is
wired correctly. The decisive displacement from the fundamental window channel
is not reported because the non-class contraction in `(3)` is not available
inside the current packet.

So the present finding is outcome (c): the window class is enumerated and
shown to carry Wilson weight, but the smallest nontrivial exact truncation is
a precise import-free derivation target rather than a completed numeric
`k = 2` displacement. The architecture residual remains an open target named
by that window recoupling object, along with the previously listed finite-box,
finite-mode, wider-slab, `L_perp`, analytic `P(6)`, and repinning residuals.

## Gates

| gate | result |
|---|---|
| window class enumerated separately from captured link classes | PASS |
| Wilson action weights the window as a plaquette | PASS |
| current scalar strip architecture does not contain a four-link window character | PASS |
| `lambda = 0` window channel reproduces W44 `k = 2` | PASS |
| fundamental window channel exactness | named target, not numerically claimed |
| no nontrivial window displacement reported without recoupling data | PASS |

## No-Go Discipline Gate

This is a bounded wall statement, not a broad no-go. The negative is: current
W44 scalar class-channel data are insufficient to compute the nontrivial
fundamental window coupling exactly.

**N1 alternative routes checked.**

| route | outcome on this bounded claim | marker |
|---|---|---|
| Treat the window as another diagonal class sum | Fails because `3bar x 3 x 3bar x 3` has a two-dimensional invariant space; a scalar multiplicity does not fix a recoupling matrix. | ATTEMPTED |
| Reuse `E_D(a,b)` for the window | Fails because `E_D` is a two-unit internal-link factor, while the window character contains four links in one trace. | ATTEMPTED |
| Reuse the per-rail longitudinal `delta/d` bonds | Fails because those bonds integrate two rails independently and remove the four-link plaquette trace. | ATTEMPTED |
| Use fusion multiplicity counts as the coupling | Fails because counts give dimensions, not Clebsch maps, basis normalization, or `6j` phases/weights. | ATTEMPTED |
| Use the existing adjoint Wigner projector context | Fails for this packet because the available explicit projector is for `(1,1)^x4`, not the fundamental `3bar-3-3bar-3` window. | ATTEMPTED |
| Import an external SU(3) `6j` library or literature coefficient | Blocked by the no-new-import rule for this task. | ATTEMPTED |

**N2 wall independence.** The collapsed wall set for the nontrivial window
measurement has one item: the missing fundamental window intertwiner /
recoupling normalization. Finite `B_4`, finite Bessel support, wider slab,
`L_perp`, analytic `P(6)`, and repinning are real residuals, but they do not
need to be treated as independent reasons for why this runner cannot report
the fundamental-channel `k = 2` displacement.

**N3 hidden-wall scan.** Phrases such as "current" and "finite packet" are
load-bearing scope controls. "Wilson action is a sum over plaquettes" and
"standard Wilson" appear only inside quoted authority/context language. No
unquoted "by construction" or broad "framework provides" step is used as a
proof substitute.

**N4 residual matching.** W44 supplies the unwindowed strip-word product-axis
measurement. W39 supplies the internal-link scalar contraction. W17 supplies
the per-rail longitudinal bond. The residual attacked here is different and
narrower: the four-link inter-layer transverse plaquette recoupling. Prior
rows are used to identify what is already captured, not as witnesses against
the window object.

**N5 rhetoric audit.** The statement "current scalar architecture does not
capture the window" is at finite W44 scalar class-channel resolution. It is
not a statement about all future tensor-network, Wigner, or full-rim
computations.

**N6 partial-closure path scan.** A repo-local construction of the
fundamental `3bar-3-3bar-3` invariant basis and recoupling matrix would close
the named wall without a new axiom. The adjoint Wigner context files show the
shape of such a construction for another representation family; this note
does not reuse them as a completed window object.

**N7 steelman.** A reviewer could argue that the fundamental recoupling is
small enough to build directly from the existing Gell-Mann/Fierz primitives
and finite fusion helpers, so the present cycle should have produced the
nontrivial `k = 2` displacement. That is a strong next step. This note accepts
that path as live and narrows its output to the exact switch-off gate plus the
precise missing object.

**N8 cross-cycle echo.** The beta=6 tensor-network note already names the
non-abelian recoupling/intertwiner network as the remaining `D >= 3`
plaquette contraction object. The SU3 Wigner context files show partial
infrastructure for adjoint sectors. The analogous mechanism for this task is
the fundamental window recoupling object named above.

Gate result: PASS for the bounded wall statement.

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_slab_window_coupling_derived_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=22, FAIL=0
```

Regenerate the cache:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_slab_window_coupling_derived_bounded_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
