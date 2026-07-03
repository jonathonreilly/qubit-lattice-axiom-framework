# C1b Degeneracy-Locus Partition Totality

**Date:** 2026-07-02
**Type:** bounded theorem (degeneracy witnesses + conditional exclusion)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Paired runner:**
[`scripts/frontier_c1b_degeneracy_locus_partition_totality_2026_07_02.py`](../scripts/frontier_c1b_degeneracy_locus_partition_totality_2026_07_02.py)
**Cached output:**
[`logs/runner-cache/frontier_c1b_degeneracy_locus_partition_totality_2026_07_02.txt`](../logs/runner-cache/frontier_c1b_degeneracy_locus_partition_totality_2026_07_02.txt)

## Purpose

This note attacks the C1b half left open by the Block03 sibling: whether
S3-class realized-`Y`-dependent fine partitions can be excluded. It proves an
exact finite obstruction on the `hw=1` circulant surface: at law-admissible
degeneracy loci, the fine spectral partition is not recoverable from `Y` alone.

The exclusion is conditional on one named interpretive premise introduced here,
D-totality. D-totality is not asserted as axiom content, primitive content, or
registry content; it is flagged for audit adjudication.

## Setting

Work on the one-site `hw=1` generation surface. Let `U` be the cyclic shift on
`C^3`, and let

```text
Y = a I + b U + conj(b) U^{-1},        b = |b| exp(i delta).
```

The Fourier modes are the common eigenbasis of the circulant algebra generated
by `U`. That basis is determined by the algebra, not by the particular `Y`.
The eigenvalues of `Y` are

```text
lambda_k = a + 2 |b| cos(delta + 2 pi k / 3),        k = 0,1,2.
```

The Block01 sibling names three scoring partitions:

| label | partition provenance | defining condition on the parent real slice |
|---|---|---|
| S1 | generator channels `I` versus `J-I`; algebra-canonical | `3a^2 = 6b^2` |
| S2 | per-mode imported basis | `a^2 = b^2` |
| S3 | `Y` idempotent/eigenvalue frame | `(a+2b)^2 = 2(a-b)^2` |

The Block03 sibling splits C1 into:

```text
C1a: no imported basis.
C1b: no realized-state-dependent partition.
```

Block03 conditionally derives C1a from its registrability reading R*, but
explicitly leaves C1b open because a realized `Y`-dependent frame is supplied
pointwise by the realized-state primitive.

## T1 - Degeneracy Loci Are Admissible And Explicit

**Claim.** For nonzero `b`, `lambda_j = lambda_k` with `j != k` exactly when

```text
delta == m pi / 3        mod 2 pi.
```

At those residues, the colliding pairs are:

| `m mod 6` | colliding pair |
|---|---|
| `0` | `{1,2}` |
| `1` | `{0,2}` |
| `2` | `{0,1}` |
| `3` | `{1,2}` |
| `4` | `{0,2}` |
| `5` | `{0,1}` |

**Derivation.** For `j != k`,

```text
lambda_j = lambda_k
iff cos(delta + 2 pi j/3) = cos(delta + 2 pi k/3).
```

The alternative
`delta + 2 pi j/3 == delta + 2 pi k/3 mod 2 pi` is impossible for distinct
`j,k` in `{0,1,2}`. Hence the equality is exactly

```text
delta + 2 pi j/3 == -delta - 2 pi k/3        mod 2 pi,
```

or

```text
delta == pi n - pi(j+k)/3.
```

Thus every nontrivial collision lies on a `pi/3` residue, and the residue table
above follows by direct substitution. The exact witness used below is

```text
delta = 0,        b real,        lambda_1 = lambda_2 = a - |b|.
```

These loci are law-admissible states on the named surface. Nothing in the
Record axiom sentences excludes them, and the realized-state primitive supplies
no state-selection filter. In particular, it says:

```text
The laws do not pick the state; the world does, among the states the laws
permit.
```

and:

```text
Nothing more is supplied: no averaging over alternatives, no typical or
generic claim, and no quoting a number that would differ had another
law-admissible state been realized.
```

The `b=0` point is a more degenerate limiting case where `delta` is not a
meaningful coordinate; it is not needed for the witness.

## T2 - The Fine Partition Is Not Y-Recoverable On The Locus

**Claim.** At `delta = 0`, the spectral data of `Y` alone determines only

```text
{P_0, P_1 + P_2},
```

not the fine rank-one split of the two-dimensional eigenspace.

Let `f_k` be the Fourier modes and `P_k = |f_k><f_k|`. At `delta = 0`,

```text
Y P_0 = (a + 2|b|) P_0,
Y (P_1 + P_2) = (a - |b|)(P_1 + P_2).
```

The Fourier split

```text
{P_1, P_2}
```

diagonalizes `Y`, but so does the rotated split

```text
g_1 = (f_1 + f_2)/sqrt(2),        g_2 = (f_1 - f_2)/sqrt(2),
Q_1 = |g_1><g_1|,                 Q_2 = |g_2><g_2|.
```

The paired runner checks exactly that:

- `P_1` and `P_2` are idempotent, orthogonal, and sum to `P_1 + P_2`;
- `Q_1` and `Q_2` are idempotent, orthogonal, and sum to `P_1 + P_2`;
- both fine splits commute with `Y` at `delta = 0`;
- `Y Q_i = (a - |b|) Q_i`, so the rotated split also diagonalizes `Y`.

The same coarse spectral data can give different fine per-cell quantities. Let
`T = P_1`, a fixed test element of the circulant algebra. For the per-cell
Hilbert-Schmidt content

```text
c_E(T) = Tr(E T^* T E),
```

the Fourier split gives

```text
(c_{P_1}(T), c_{P_2}(T)) = (1, 0),
```

whereas the rotated split gives

```text
(c_{Q_1}(T), c_{Q_2}(T)) = (1/2, 1/2).
```

Both split choices have the same coarsened content

```text
c_{P_1+P_2}(T) = 1.
```

Thus any S3-class per-cell scoring rule that needs the fine cells is not
well-defined from `Y` alone on the degeneracy locus. The coarsened spectral
algebra remembers the degenerate eigenvalue and its rank-two projector, but it
does not remember the rank-one fine-cell distribution.

## T3 - Provenance Collapse

**Claim.** On the degeneracy locus, a claimed S3-class fine partition faces
exactly three horns:

| horn | result |
|---|---|
| coarsen to `{P_0, P_1+P_2}` | T2 shows the fine per-cell data needed by the S3 condition is gone |
| choose an arbitrary split of `P_1+P_2` | the choice is not R*-registrable under Block03, because it is unsupplied auxiliary frame data |
| choose the Fourier split `{P_1,P_2}` | the split is determined by `U`, hence by the circulant algebra, not by `Y` |

The last horn is provenance collapse. Extending an S3-class rule to the locus by
declaring the Fourier split has borrowed algebra-canonical frame data. That is
Block01's S1-provenance pattern, not S3's `Y`-dependent provenance.

The paired runner supplies the computable checks:

- on the locus, every rank-one split inside `P_1+P_2` commutes with `Y`, so `Y`
  does not select the Fourier split;
- the Fourier projectors are also eigenprojectors of `U`, so their source is
  the circulant algebra;
- the coarsened spectral data records only the total `P_1+P_2` content, not
  the fine-cell values.

## T4 - The Honest Limit: Pointwise Escape

**Claim.** Degeneracy witnesses alone do not exclude S3-class rules pointwise.

At a nondegenerate realized `Y`, the S3 idempotent/eigenvalue frame is
well-defined from `Y`. The realized-state primitive permits pointwise
evaluation at the one realized law-admissible state:

```text
Derivations may evaluate at the realized state, pointwise.
```

It also states:

```text
This is pointwise evaluation, not a state-selection rule. It carries zero
state-contingent content: no state, averaging over alternatives, measure,
weighting, probability rule, typicality claim, genericity claim, preferred
state, default state, boundary condition, normalization rule, or value is
supplied by it.
```

Therefore the primitive supplies no measure, typicality, perturbation,
genericity, or averaging principle that would discount the degeneracy loci, and
it supplies no requirement that a rule extend beyond the one realized point.
Without D-totality, a reviewer may say: the physical rule only needs to be
defined at the actual realized nondegenerate `Y`. That objection is correct as
far as the named primitive goes.

## T5 - D-Totality And Conditional C1b

**Definition (D-totality).** A physical readout rule must be well-defined at
every law-admissible realized state in its stated law-domain. This is a
rule-domain totality constraint: a law-property of the rule, not a state
property.

**Conditional theorem.** D-totality implies that S3-class fine-partition rules
are excluded on the `hw=1` circulant surface:

1. T1 gives law-admissible degeneracy states.
2. T2 shows the fine S3 partition is not recoverable from `Y` alone on those
   states.
3. T3 shows the available extensions either coarsen away the fine S3 data,
   import an arbitrary split, or borrow the algebra frame and collapse to
   S1-provenance.

Therefore, conditional on D-totality, C1b holds. Combined with Block03's R*
conditional C1a, the full C1 frame component holds conditionally.

T5 summary: conditional on D-totality; not adjudicated; pointwise escape (T4)
stands without it.

The premise ladder is:

| premise | source | discriminator | status in this note |
|---|---|---|---|
| R* | Block03 sibling | scalar readouts must be additive and constant on unsupplied auxiliary-choice orbits | not adjudicated here |
| D-totality | this note | physical readout rule must be well-defined at every law-admissible realized state in its law-domain | this note's single interpretive premise; flagged for audit |
| C2 | Block02 sibling, as cited by Block03/user task | weighting is orthogonal to partition/frame data | not adjudicated here |
| equal-channel-energy | Block01/parent surface | after S1 provenance is selected, equal Hilbert-Schmidt energy across generator channels gives `r = 1/2` | not adjudicated here |

D-totality is shape-parallel to R*: both are rule-level constraints transported
from law-likeness. R* constrains dependence on unsupplied auxiliary choices;
D-totality constrains whether a law-domain readout rule may be undefined at
law-admissible realized states. This note does not claim repo authority has
already adopted either reading.

## What This Note Does NOT Claim

- D-totality is not asserted as axiom content, primitive content, or registry
  content.
- S3-class rules are not excluded pointwise at a nondegenerate realized `Y`.
- No wall is closed on the actual current surface.
- C1 completion is conditional on both R* and D-totality.
- The pointwise escape in T4 stands without D-totality.
- No `kappa_EW`, `beta`, probability, Born, typicality, or measure content is
  supplied.
- No equal-channel-energy theorem is derived.
- No new axiom, primitive, admission, normalization, dictionary, or occupancy
  cell is introduced.
- No all-models result is claimed; the theorem is only on the finite `hw=1`
  circulant surface.

## Load-Bearing Inputs

| path | role | dependency class |
|---|---|---|
| [`FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md`](FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md) | Supplies S1/S2/S3 definitions, partition provenance, and the equal-channel-energy parent surface. | landed dependency; independent audit owns its verdict and any retained-grade dependency closure |
| [`C1_FRAME_COMPONENT_FROM_RECORD_REGISTRABILITY_PARTIAL_BOUNDED_NOTE_2026-07-02.md`](C1_FRAME_COMPONENT_FROM_RECORD_REGISTRABILITY_PARTIAL_BOUNDED_NOTE_2026-07-02.md) | Supplies the C1a/C1b split, R*, and the honest limit that R* does not exclude realized-`Y`-dependent partitions. | landed dependency; independent audit owns its verdict and any retained-grade dependency closure |
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Supplies the Record sentences, especially locked possibility under repeated readout, readability, finite additivity, and the open-gates boundary for measurement basis/context selection. | audit status remains independent |
| [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) | Supplies pointwise realized-state evaluation and the no-averaging/no-measure/no-typicality/no-state-selection boundary. | audit status remains independent |

## Paired Runner

Paired runner:

```text
scripts/frontier_c1b_degeneracy_locus_partition_totality_2026_07_02.py
```

Expected terminal line:

```text
TOTAL: PASS=32 FAIL=0
```
