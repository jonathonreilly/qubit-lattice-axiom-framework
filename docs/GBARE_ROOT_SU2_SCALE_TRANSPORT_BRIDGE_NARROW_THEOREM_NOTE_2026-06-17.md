# g_bare Root-SU2 Scale Transport Bridge

**Date:** 2026-06-17
**Claim type:** bounded_theorem
**Status:** bounded-support scale-transport bridge; independent audit required.
This note does not apply an audit verdict, does not retag any ledger row, and
does not promote a parent `g_bare` claim.
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/gbare_root_su2_scale_transport_bridge_2026_06_17.py`
**Runner cache:** `logs/runner-cache/gbare_root_su2_scale_transport_bridge_2026_06_17.txt`

## Purpose

The `g_bare` promotion panel isolated one hard residual: the parent route can
move only if the per-site spin-double-cover normalization propagates to the
graph-first gauge `su(3)` trace surface by derivation, not by a free
normalization convention.

This note supplies the narrow finite bridge for that residual. It does not
derive Wilson dynamics, beta=6 selection, physical color naming, EW matching,
or a parent `g_bare = 1` theorem. It proves only that, once the graph-first
`V_3` gauge carrier is used, each root `SU(2)` subgroup of the compact
unitary `SU(3)` representation carries the same Pauli/2 scale as the per-site
spin double cover.

## Source Inputs

- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  supplies the structural graph-first `su(3)` carrier on the selected-axis
  `V_3` surface.
- [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md) supplies the
  source separation that combines native cubic `Cl(3)` / `su(2)` with the
  graph-first structural `su(3)` while excluding Wilson dynamics and
  phenomenology.
- [`STAGGERED_GBARE_TRACE_SURFACE_BRIDGE_NOTE_2026-06-06.md`](STAGGERED_GBARE_TRACE_SURFACE_BRIDGE_NOTE_2026-06-06.md)
  isolates this bridge as the remaining scale gate for the `g_bare`
  trace-normalization route.

## Theorem

Let `V_3 = C^3` be the graph-first gauge carrier and let `E_ij` be matrix
units on `V_3`. For each coordinate pair `(i,j)`, define the root-subgroup
generators

```text
J_x^(ij) = (E_ij + E_ji)/2
J_y^(ij) = (-i E_ij + i E_ji)/2
J_z^(ij) = (E_ii - E_jj)/2.
```

Then, on the active two-plane spanned by `e_i,e_j`, these are exactly the
Pauli/2 generators. In the full `V_3` representation they satisfy:

```text
[J_x, J_y] = i J_z,   [J_y, J_z] = i J_x,   [J_z, J_x] = i J_y,
Tr_V3(J_a J_b) = (1/2) delta_ab,
spec(J_z) = {-1/2, 0, +1/2},
exp(4 pi i J_z) = I, while exp(2 pi i J_z) is nontrivial on the active pair.
```

Therefore every root `SU(2)` subgroup in the graph-first `V_3` gauge
carrier has the same spin-double-cover normalization as the per-site
`Pauli/2` `SU(2)`.

The scale cannot be changed inside the same unitary commutator
representation. If `J_a` is replaced by `c J_a`, then

```text
[c J_x, c J_y] = i c^2 J_z,
```

which equals `i (c J_z)` only for `c = 1` among positive scalings. Thus a
nontrivial positive dilation is not another root `su(2)` embedding with the
same bracket and primitive spin period on the same `V_3` carrier.

## Consequence For The g_bare Gate

At the level of finite compact unitary representation theory, this supplies
the scale-transport identity:

```text
per-site Pauli/2 spin scale
  = root-SU2 Pauli/2 scale inside graph-first V_3 gauge SU(3).
```

If independent review accepts this bridge and the graph-first `V_3` gauge
surface as the trace surface consumed by the Wilson/Ward algebra, then the
old `N_F = 1/2` blocker is no longer a free scalar at this bridge. The parent
`g_bare` route still needs its own review/audit pass, and this note does not
claim that parent promotion.

## Boundaries

- No new axiom, primitive, observed constant, fitted selector, or
  same-surface family argument is introduced.
- No Wilson action, beta=6, continuum matching, physical-color naming, or EW
  readout theorem is derived here.
- The full matter tensor trace `V_3 x C^2` still doubles the trace; the
  bridge is specifically for the graph-first gauge trace on `V_3`.
- Species-label bijections remain irrelevant to this trace scale.

## Verification

Run:

```bash
python3 scripts/gbare_root_su2_scale_transport_bridge_2026_06_17.py
```

Expected summary:

```text
TOTAL: PASS=91, FAIL=0
```
