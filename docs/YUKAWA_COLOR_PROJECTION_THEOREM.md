# Yukawa Color-Projection Channel-Fraction Theorem

**Date:** 2026-04-14; source-boundary replacement 2026-05-24
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome; later status is generated only by the audit
pipeline after independent review.
**Primary runner:** `scripts/frontier_yukawa_color_projection_boundary.py`
**Supporting exact Fierz runner:** `scripts/frontier_ew_current_fierz_channel_decomposition.py`

## Claim Scope

This row submits only the finite-dimensional SU(N_c) channel-counting fact
needed by later Yukawa/color-matching work:

```text
N_c tensor N_c-bar = 1 plus adj,

f_adj,dim = dim(adj) / dim(N_c tensor N_c-bar)
          = (N_c^2 - 1) / N_c^2,

f_adj,dim |_{N_c=3} = 8/9.
```

Here `f_adj,dim` is a representation-dimension fraction. It is not a
dynamical trace fraction, not a lattice connected-correlator measurement,
not a Higgs wave-function normalization, and not a physical Yukawa
renormalization. The row is deliberately named as a color-projection
**channel-fraction** theorem to keep the audit boundary separate from the
physical matching problem.

## Dependencies

The scoped one-hop dependencies are:

- [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md): exact SU(N_c)
  Fierz/channel decomposition and the distinction between dimension fractions
  and matrix-dependent trace fractions.
- [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md): retained
  nonabelian native-gauge surface.
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md):
  retained graph-first SU(3) closure fixing `N_c = 3` on the graph-visible
  color surface.

Historical color-matching notes such as `RCONN_DERIVED_NOTE.md`,
`YT_EW_COLOR_PROJECTION_THEOREM.md`, and
`EW_CURRENT_MATCHING_OZI_SUPPRESSION_THEOREM_NOTE_2026-04-27.md` are not
load-bearing dependencies of this row.

## Theorem

Let the color representation be the fundamental `N_c` of SU(N_c), with
antifundamental `N_c-bar`. Then the color bilinear representation decomposes
as

```text
N_c tensor N_c-bar = 1 plus adj.
```

The adjoint representation has dimension `N_c^2 - 1`, the singlet has
dimension `1`, and the total tensor-product space has dimension `N_c^2`.
Therefore the adjoint channel's representation-dimension fraction is

```text
f_adj,dim = (N_c^2 - 1) / N_c^2.
```

At the framework color value `N_c = 3`, supplied by the retained graph-first
SU(3) substrate, this gives exactly

```text
f_adj,dim = 8/9,
f_singlet,dim = 1/9.
```

## Proof

Choose SU(N_c) generators `t^A`, `A = 1, ..., N_c^2 - 1`, normalized by

```text
Tr(t^A t^B) = delta_AB / 2.
```

The matrices `{I/sqrt(N_c), sqrt(2) t^A}` form an orthonormal basis for the
singlet plus traceless-adjoint decomposition of the complex `N_c x N_c` color
matrix space. Equivalently, the SU(N_c) Fierz completeness identity is

```text
delta_ac delta_bd
  = (1/N_c) delta_ad delta_bc
    + 2 sum_A (t^A)_ad (t^A)_bc.
```

This identity is pure finite-dimensional linear algebra. It splits a color
bilinear matrix into a one-dimensional singlet component and an
`N_c^2 - 1` dimensional adjoint component. Counting dimensions gives

```text
1 + (N_c^2 - 1) = N_c^2.
```

Dividing the adjoint dimension by the total color-bilinear dimension gives
`(N_c^2 - 1)/N_c^2`. Substituting `N_c = 3` gives `8/9` exactly.

## Runner Evidence

`scripts/frontier_yukawa_color_projection_boundary.py` checks the source
boundary and the exact algebraic content:

- the theorem note names only the scoped Fierz/channel-fraction claim;
- excluded historical matching nodes are not cited as one-hop markdown
  authorities;
- the physical matching claims are absent from the asserted theorem body;
- SU(N_c) generators have the required trace normalization for
  `N_c = 2, 3, 4, 5`;
- the Fierz completeness identity holds numerically over deterministic random
  complex matrices;
- the exact fractions at `N_c = 3` are `8/9` and `1/9`.

The existing supporting runner
`scripts/frontier_ew_current_fierz_channel_decomposition.py` remains useful
for the broader Fierz packet, but this row now has a dedicated runner whose
source-boundary checks are aligned with this theorem note.

## Explicit Non-Claims

This row does not claim any of the following:

- a measured or derived lattice connected-trace observable `R_conn`;
- equality between a dynamical trace fraction and the representation-dimension
  fraction `8/9`;
- a Higgs or scalar wave-function factor;
- a `sqrt(8/9)` physical Yukawa correction;
- a top-mass prediction;
- closure of the Ward-identity Yukawa route;
- closure of the lattice-to-physical matching bridge.

Any later theorem that uses the `8/9` channel fraction as a physical matching
coefficient must separately derive the physical readout/matching map. This
row supplies only the audit candidate for the exact SU(3)
representation-dimension fraction.

## Audit Handoff

```yaml
proposed_claim_type: positive_theorem
proposed_claim_scope: >
  SU(N_c) Fierz/channel decomposition gives the representation-dimension
  fraction f_adj,dim = (N_c^2 - 1)/N_c^2, hence f_adj,dim = 8/9 at N_c = 3,
  with no claim that this equals a dynamical trace observable or physical
  Yukawa matching coefficient.
proposed_load_bearing_step_class: A
status_authority: independent audit lane only
```
