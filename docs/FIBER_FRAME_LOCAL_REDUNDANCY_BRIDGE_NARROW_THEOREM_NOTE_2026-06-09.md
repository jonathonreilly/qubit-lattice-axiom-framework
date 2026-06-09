# Fibre-Frame Local Redundancy Bridge Narrow Theorem

**Date:** 2026-06-09
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/fiber_frame_local_redundancy_bridge_2026_06_09.py`](../scripts/fiber_frame_local_redundancy_bridge_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/fiber_frame_local_redundancy_bridge_2026_06_09.txt`](../logs/runner-cache/fiber_frame_local_redundancy_bridge_2026_06_09.txt)

## Claim under test

The conditional audit on the 2026-06-08 minimal-coupling fibre-frame note asked
for a one-hop theorem proving that local `U(3)` fibre-frame choices are
observational redundancies and that the translation bridge's `U=I` reference is
not a canonical physical cross-site frame pinning. This note is the bridge, so
the dependency edge is intentionally one-way: the minimal-coupling note cites
this bridge, not conversely.

This note supplies the narrow current-surface bridge. On the retained
graph-first `SU(3)` fibre and tensor-product hopping surface, a local `U(3)`
change of fibre basis is a passive trivialization change for the registered
weak-sector and Record-sector data currently present in the cited authorities.
The flat `U=I` hopping reference is therefore a choice of cross-site
trivialization. Under independent local fibre bases it is rewritten as
`g_x g_y^dag`; it is not invariantly singled out by the current framework
surface as a physical pinning of fibre bases across sites.

## Cited authorities

1. [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies
   the approved Lattice, Quantum, and Record axioms. Record contributes only
   durable realized-outcome registration and finite additivity in a supplied
   readout context; it does not supply gauge dynamics, measurement dynamics,
   probabilities, or sector generation.

2. [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
   supplies the graph-first internal `SU(3)` fibre as the compact semisimple
   part of the retained commutant surface, with the abelian factor left
   hypercharge-like.

3. [`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
   supplies the finite tensor-product operator surface and the translation
   identity `T_a a_x T_a^dag = a_{x+a}`. This is the flat reference
   trivialization used by free hopping.

4. [`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
   supplies the Hermitian, number-conserving nearest-neighbor hopping bilinear
   on the same tensor-product surface.

## Statement

Work on a finite periodic block. At each site, write the current graph-first
weak/fibre carrier as

```text
    V_x = C^2_weak tensor C^3_fibre.
```

The weak generators act as `sigma_i tensor I_3`. A local fibre-frame re-choice
acts as

```text
    G_x = I_2 tensor g_x,        g_x in U(3).
```

Then:

**(F1) Current registered weak data are fibre-frame invariant.**
`G_x` commutes with the graph-first weak `su(2)` generators and fixes the
weak central-sector projectors `P_up`, `P_down`. Therefore a Record readout
context whose realized central sectors are these current weak-sector projectors
is unchanged by the fibre-frame basis re-choice. The scalar finite additivity
of the disjoint sectors is also unchanged.

**(F2) No fibre colour basis is selected by the current surface.**
The only fibre operator invariant under conjugation by all local `U(3)` frame
changes is a scalar multiple of `I_3`. Hence a rank-one fibre-colour projector
or labelled fibre basis vector would add extra structure not supplied by the
current cited authorities.

**(F3) The flat `U=I` link is a trivialization choice.**
The free hopping link written as `I` is invariant under a common global frame
rotation, but under independent local bases at adjacent sites it is represented
as

```text
    I  ->  g_x I g_y^dag = g_x g_y^dag.
```

The operator itself is unitarily rewritten, not physically changed:

```text
    G H[U=I] G^dag = H[U'=g_x g_y^dag].
```

Therefore the translation bridge's `U=I` reference is the flat choice of
coordinates on neighbouring fibres, not an invariant physical rule that pins
the fibre basis at `x` to the fibre basis at `y`.

**(F4) A link transporter is the coordinate form of cross-site comparison.**
For a general unitary transporter `U_xy`,

```text
    G H[U_xy] G^dag = H[g_x U_xy g_y^dag].
```

This is exactly the passive-frame form of the lattice connection law consumed
by the minimal-coupling note.

## Proof sketch

For (F1), `G_x = I_2 tensor g_x` and each weak generator has the form
`sigma_i tensor I_3`, so the commutator vanishes. The same tensor-factor
calculation fixes `P_up` and `P_down`. Record is used only at its approved
scope: given those finite disjoint central sectors, the sector labels and
additive scalar readout are unchanged by a fibre-basis rotation that acts
inside each sector.

For (F2), the commutant of the defining `U(3)` action on `C^3_fibre` is
`C I_3`. Equivalently, any rank-one fibre projector is moved by a permitted
frame permutation, while `I_3` is fixed. Thus the current retained surface
does not name a canonical fibre basis.

For (F3) and (F4), write the two-site single-particle hopping block as

```text
    H[U] = |x><y| tensor U + |y><x| tensor U^dag.
```

Conjugating by `G = G_x oplus G_y` gives the same block with
`U` replaced by `g_x U g_y^dag`. The case `U=I` proves that the free
translation bridge chooses the flat trivialization; it does not prove that
the `I` matrix is a local-frame-invariant physical cross-site frame.

## What the runner verifies (`PASS=18 FAIL=0`)

- local `U(3)` fibre-frame rotations are unitary;
- they commute with the graph-first weak `su(2)` generators;
- weak-sector central projectors and their finite additive scalar rank check
  are unchanged;
- only scalar fibre operators are invariant under the full local `U(3)` frame
  group;
- a candidate fibre-colour projector is not invariant;
- local basis changes rewrite the identity link as `g_x g_y^dag`, generally
  not `I`;
- `G H[U=I] G^dag = H[g_x g_y^dag]`;
- a common global fibre rotation leaves the flat identity link fixed;
- for a general sampled link, `G H[U] G^dag = H[g_x U g_y^dag]`;
- guardrails: no gauge action, no physical `SU(3)_c` identification, no future
  colour-readout theorem.

## What this closes

This closes the one-hop kinematic bridge needed by the minimal-coupling source
note: on the current registered operator surface, local fibre-frame choices are
passive redundancies, and the retained translation bridge's `U=I` reference is
not a canonical physical cross-site frame pinning.

The result is deliberately current-surface and kinematic. It lets the
minimal-coupling note use local frame covariance without making a new axiom or
promoting a gauge action.

## What this does not close

- No Yang-Mills/Wilson gauge action or gauge-field dynamics.
- No continuum limit, coupling value, or `g_bare` convention.
- No physical `SU(3)_c` identification beyond the graph-first algebraic fibre.
- No theorem saying future colour-readout contexts cannot register additional
  fibre data. The bridge only covers the registered weak/Record-sector data
  currently present in the cited authorities.
- No Born rule, measurement/decoherence dynamics, or sector-generation rule
  from Record.

## Honest status metadata

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "Current-surface finite operator-algebra theorem: local U(3) fibre-frame changes are passive trivialization changes for the registered weak/Record-sector data currently present in the cited authorities; U=I is the flat cross-site trivialization, not a canonical physical fibre pinning."
upstream_dependencies:
  - minimal_axioms
  - graph_first_su3_integration_note
  - tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25
  - hopping_bilinear_hermiticity_theorem_note_2026-05-02
admitted_context_inputs: []
source_sets_audit_outcome: false
audit_required_before_effective_status_change: true
```
