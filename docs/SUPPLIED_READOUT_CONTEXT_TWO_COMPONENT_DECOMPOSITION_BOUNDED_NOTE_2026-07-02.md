# Supplied Readout Context Two-Component Decomposition

**Date:** 2026-07-02
**Type:** bounded support (structural decomposition + witnesses)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only, note does not set or predict audit outcome.
**Paired runner:**
[`scripts/frontier_supplied_readout_context_two_component_decomposition_2026_07_02.py`](../scripts/frontier_supplied_readout_context_two_component_decomposition_2026_07_02.py)
**Cached output:**
[`logs/runner-cache/frontier_supplied_readout_context_two_component_decomposition_2026_07_02.txt`](../logs/runner-cache/frontier_supplied_readout_context_two_component_decomposition_2026_07_02.txt)

## Purpose

This note separates one supplied readout context into two finite components:

- **C1 (FRAME):** the partition/frame data of a readout.
- **C2 (WEIGHTING):** scalar weighting/normalization data on the partition cells.

The point is not to close either wall. The point is to give exact finite
witnesses that a frame part and a weighting part can be independent, and to
record a candidate overlap between Block01's frame residual and the
`kappa_EW` wall's quoted "supplied readout context" objection. This note does
not prove that the `kappa_EW` wall has a separate C1 frame half.

This is a finite supplier-shape decomposition plus a candidate wall-map
boundary, conditional on the quoted wall texts; it is not a closure of either
wall.

## The Two Walls

The `kappa_EW` wall names the missing item as:

```text
weighting/readout-bridge rule
```

It also names an open future closure route:

```text
Add a selector, readout convention, or admitted observable-bridge placement.
```

Its hostile-reviewer clause is:

```text
A hostile reviewer could say: "The axioms permit a supplied
readout context, and a sufficiently constrained EW readout context might force
`kappa_EW`." That would defeat a broad no-go, but not this one: supplying that
readout context is exactly extra non-axiom content.
```

Its common-factor fact is:

```text
Within the existing construction, a common `K_EW` factor cancels from
`sin^2(theta_W)`, so that ratio is insensitive to `kappa_EW` placement as
implemented here.
```

Block01's D4 item 4 requirement is:

```text
4. NO IMPORTED FRAME: its channel partition is definable from the
   framework-supplied circulant algebra alone (the unit direction and its
   Hilbert-Schmidt orthocomplement), with no imported per-mode basis and no
   Y-dependent idempotent frame,
```

Block01's residual list is:

```text
1. **The no-imported-frame requirement (item 4).** Deriving, from the current
   authority surface, that the physical generation readout admits no imported
   frame — equivalently, that its partition data is exhausted by the
   framework-supplied algebra (unit + HS-orthocomplement). This note supplies
   the discriminator for that requirement; it does not derive the requirement.
   Its supplier shape — "supplied readout context" — is the same shape the
   `kappa_EW` weighting wall names, so these two residuals are candidate
   wall-merge targets (one supplier could close both).
2. **The equal-channel-energy theorem.** The parent note's own "if a separate
   theorem selects equal Hilbert-Schmidt energy across the two generator
   channels" clause: this note leaves that clause exactly as open as the
   parent states it.
```

The minimal axiom surface leaves these gates outside the axioms:

```text
- the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;
- the strong-CP theta admission;
- P2/modulus/phase-blindness and any log-det readout theorem;
- context selection, measurement basis selection, Born weights, probability
  rules, update laws, decoherence mechanisms, and formation rules (which
  admissible possibility a new record locks, at which site, with what weight,
  or at what rate);
- arrow, record-production dynamics, physical persistence dynamics, time metric,
  and local observability of records;
- source/action and physical-observable identification;
- `g_bare = 1` convention handling;
- the scale-reference primitive and the separate gravity self-consistency
  question that the framework's natural unit equals the Planck length.
```

## C1/C2 Definitions

Work with a finite algebraic readout surface. A supplied readout context has:

- **C1 (FRAME):** a partition/frame `F = {F_i}` of the finite readout channels.
  In the Block01 `hw=1` circulant witness, C1 is the requirement that the
  channel partition is definable from the framework-supplied circulant algebra
  alone: the algebra unit direction and its Hilbert-Schmidt orthocomplement.
  This is exactly Block01 D4 item 4.
- **C2 (WEIGHTING):** scalar weights `w_i` or normalization data assigned to the
  cells of `F`. C2 is not the existence of the cells; it is the scalar rule on
  those cells. This is the shape named by the `kappa_EW` wall's
  "weighting/readout-bridge rule".

Record additivity used here is only the minimal axiom sentence:

```text
Only records are readable. For any finite collection of pairwise-disjoint
records, scalar readout `I` is additive, with `I(empty)=0`.
```

## T1 - Block01 Restated Through C1

**Claim.** On the `hw=1` circulant witness surface, if C1 is imposed as
Block01 D4 item 4, then among the three parent-named scoring rules only
generator-channel Hilbert-Schmidt scoring survives.

**Witness-level proof.** The finite circulant algebra supplies the unit `I` and
the Hilbert-Schmidt orthocomplement represented by `B = J - I`. The
Hilbert-Schmidt inner product gives

```text
<I, B> = 0.
```

So the generator-channel partition is supplied by the algebraic surface itself.
The runner checks the exact `N=3` identities:

```text
||I||^2 = 3,   ||B||^2 = 6,   <I, B> = 0,
3 a^2 = 6 b^2,   r = b^2/a^2 = 1/2.
```

The same runner uses the Hadamard matrix

```text
H = (1/sqrt(2)) [[1, 1], [1, -1]]
```

to reuse Block01's exclusion witnesses. For S2, `H(1, 1)^T =
(sqrt(2), 0)^T`, so per-mode equality depends on an imported frame. For S3,
the parent root satisfies the idempotent/eigenvalue equation before Hadamard
mixing and fails it after mixing. Thus S2 and S3 are excluded by C1, while S1
is the unique parent-named rule with an algebra-canonical partition.

This is only a restatement bridge. The IF-clause item 4 is exactly C1: "its
channel partition is definable from the framework-supplied circulant algebra
alone (the unit direction and its Hilbert-Schmidt orthocomplement), with no
imported per-mode basis and no Y-dependent idempotent frame".

## T2 - C1 Does Not Supply C2

**Claim.** There is a finite additive readout with the algebra-canonical
partition in which the C2 scalar weight remains unconstrained by C1 plus
Record additivity.

**Witness-level proof.** Take two partition cells `A` and `B` supplied by the
finite algebraic frame. For records represented by pairs `(x_A, x_B)`, define

```text
I_w(x_A, x_B) = x_A + w x_B.
```

The frame is fixed for every `w`: the cells are still `A` and `B`, and no
imported frame is used. The runner checks the empty record and direct-sum
additivity for both `w = 1` and `w = 2`:

```text
I_w(0, 0) = 0,
I_w(R + S) = I_w(R) + I_w(S).
```

Both choices satisfy every C1 constraint and Record additivity on explicit
direct sums. Therefore the frame component leaves the weighting component free
at witness level. This supports only the abstract separation needed for a
future wall-merge attempt; it does not show that the actual `kappa_EW` wall has
already separated weighting from every partition/readout-context choice.

## T3 - C2 Does Not Supply C1

**Claim.** A fixed weighting rule does not recover the C1 frame selection.

**Witness-level proof.** Fix equal weights across cells. Now allow an imported
Hadamard-mixed frame. The S2 per-mode witness

```text
H(1, 0)^T = (1/sqrt(2), 1/sqrt(2))^T
```

has equal cell weights/squares:

```text
(1/2, 1/2).
```

So it satisfies the equal-weighting constraint. But its cells are the
Hadamard-mixed pair

```text
(I + B)/sqrt(2),   (I - B)/sqrt(2),
```

not the algebra unit plus Hilbert-Schmidt orthocomplement partition: the first
cell is not the unit direction, and the second is not Hilbert-Schmidt
orthogonal to the unit. Thus C2 alone permits an imported S2 frame and recovers
no selection among the parent-named scorings.

## T4 - Candidate Wall-Map Boundary

Every clause below is a bounded wall-map statement; neither supplier is derived
here, and neither wall is closed by this note.

1. Block01 residual item 1 is C1 exactly (T1's restatement bridge).
2. The `kappa_EW` wall text names two open phrases: a possible "supplied
   readout context" in a hostile-reviewer objection and a missing
   "weighting/readout-bridge rule" in the wall summary.
3. This creates a candidate overlap only: a future C1 supplier might also
   answer the quoted supplied-readout-context objection, but that is not proved
   here and is not claimed as a `kappa_EW` closure.
4. Independently, T2 shows that a frame supplier would not by itself fix scalar
   weights, and T3 shows that equal weighting would not by itself recover the
   frame. Thus the finite C1/C2 components are non-identical even in the
   abstract witness model.

## What This Note Does NOT Claim

- No `kappa_EW` value is claimed.
- No C1 supplier is derived here.
- No C2 supplier is derived here.
- Neither wall is closed by this note.
- No theorem-grade decomposition of the actual `kappa_EW` wall into a C1 half
  and C2 half is claimed.
- The walls are not identical; T2 and T3 witness component independence.
- No new axiom or primitive is introduced.
- No probability or Born content is introduced.
- No EW physics reconstruction is attempted.

## Load-Bearing Inputs

| path | role |
|---|---|
| [`EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md) | Supplies the `kappa_EW` wall text quoted above: the missing weighting/readout-bridge rule, the open selector/readout-convention/observable-bridge route, the supplied-readout-context hostile-reviewer clause, and the common `K_EW` cancellation fact. |
| [`FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md`](FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md) | Supplies Block01's D4 item 4 C1 requirement, residual list, and the finite Hadamard witnesses reused here. This dependency has landed on `main` via PR #4816; independent audit still owns its verdict and any retained-grade dependency closure. |
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Supplies the finite Record additivity sentence and the Open Gates list showing readout context, measurement basis, Born weights, source/action, and physical-observable identification remain outside axiom content. |

## Paired Runner

Paired runner:

```text
scripts/frontier_supplied_readout_context_two_component_decomposition_2026_07_02.py
```

Expected terminal line:

```text
TOTAL: PASS=32 FAIL=0
```
