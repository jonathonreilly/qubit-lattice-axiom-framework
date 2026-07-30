# Cycle 733: conditional direct-sum algebra on the supplied `2 x 2 x 2` parity sectors

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle733_sector_summed_companion_channel_2026_07_28.py`](../scripts/frontier_cycle733_sector_summed_companion_channel_2026_07_28.py)

Independent check:

- [`frontier_cycle733_sector_sum_independent_check_2026_07_28.py`](../scripts/frontier_cycle733_sector_sum_independent_check_2026_07_28.py)

Load-bearing parent:

- [Cycle 727 finite-box fitted signed pullback note](CROSS_CODE_EQUIVALENCE_CYCLE727_BOUNDED_THEOREM_NOTE_2026-07-28.md)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

On the repaired Cycle-727 `2 x 2 x 2` fixture, the current five-family
dictionary has 312 rows:

| family | rows |
|---|---:|
| `free` | 48 |
| `seam` | 12 |
| `reverse` | 12 |
| `contact` | 120 |
| `coin` | 120 |

For every row, each of the target, reference-physical, and
companion-physical Pauli representatives has even matter-`X` weight.
Consequently all 936 listed representatives commute with total matter parity
and are block diagonal in the supplied even/odd decomposition. This is a
finite enumeration of dictionary representatives, not a census of Hilbert
space states.

The new theorem is only the following conditional algebra lemma. Let
`A = A_+ direct-sum A_-` and `B = B_+ direct-sum B_-` preserve their
respective parity sectors. If separately supplied maps `V_+` and `V_-` obey

`V_s^dagger V_s = I` and `V_s A_s = B_s V_s`

for `s` in `{+,-}`, then, for every relative phase `theta`,

`V_theta = V_+ direct-sum exp(i theta) V_-`

obeys `V_theta^dagger V_theta = I` and
`V_theta A = B V_theta`. Orthogonality removes the off-diagonal Gram blocks;
the same phase multiplies both sides of the odd-sector intertwining relation.
The even dictionary therefore cannot select `theta`.

No `V_s` is constructed in this package. The result does not construct a
reference-to-companion channel, select a within-sector basis identification,
select a relative phase, or close the coherent both-sector and odd-sector
intertwiner items left open by Cycle 727.

## Supplied / derived / open

### Supplied

- the repaired Cycle-727 finite fixtures, shape-specific fitted signed
  pullbacks, and separately supplied parity sectors;
- the `2 x 2 x 2` box; and
- the hypotheses `V_s^dagger V_s = I` and `V_s A_s = B_s V_s` when the
  conditional direct-sum lemma is invoked.

No ordering, basis, or phase convention is promoted to physics by this note.
Serialization order in the JSON reports is non-load-bearing.

### Derived

- the current 312-row five-family census and frozen dictionary digest;
- even matter-`X` weight for all 936 target/reference/companion
  representatives;
- the conditional direct-sum identities above; and
- invariance of those identities under an arbitrary relative sector phase.

The runners include parity-flip, signed-dictionary, and missing-premise
controls. The independent checker reconstructs the current five-family
dictionary directly from the finite fixtures without importing the primary
runner.

### Open

- explicit Hilbert-space maps `V_+` and `V_-`;
- their signed basis actions, admissibility, and sectorwise intertwining
  proofs;
- selection or physical meaning of the relative sector phase;
- a coherent both-sector reference-to-companion channel and an odd-sector
  intertwiner;
- bounded physical preparation, a uniform encoder or tiled channel, and
  every other Cycle-727 open item; and
- occurrence, physical time, permanent Record, Born weighting, and source or
  gravity content.

## No-go discipline gate

Gate disposition: **PASS after narrowing**. The submitted route-unique,
obstruction-discharge, and matter-lane closure language was removed. This
note ships a positive conditional identity and a finite parity census, not an
impossibility theorem.

- **N1 — alternative routes:** at least five routes remain live and untested:
  an explicit sectorwise factorization map; a full unitary that mixes parity
  sectors; an ancillary parity rail; controlled coherent preparation; and a
  larger physical companion space or dissipative sector-summed construction.
- **N2 — wall independence:** no collection of independent walls is claimed.
  The absent `V_s`, sectorwise intertwining, phase selection, and preparation
  tasks are listed as open obligations, not multiplied into a no-go.
- **N3 — hidden conditions:** the finite shape, fitted parent orientation,
  supplied sectors, block-preserving operator hypothesis, and conditional
  `V_s` premises are explicit.
- **N4 — residual matching:** this note relies only on the repaired parent's
  finite signed-pullback scope and exact single-fixed-sector dimension lemma.
  It does not revive the superseded route-independent obstruction.
- **N5 — rhetoric resolution:** 936 means three Pauli representatives for
  each of 312 dictionary rows. It is not a state-space, coherence, or
  all-shapes exhaustion.
- **N6 — partial-closure paths:** explicit encoders, ancillary constructions,
  phase bridges, and preparation mechanisms remain ordinary constructive
  routes rather than new-axiom demands.
- **N7 — steelman:** an explicit pair of sector maps with a retained physical
  phase bridge could establish the coherent channel that this note does not.
- **N8 — cross-cycle echo:** Cycle 720's sector-summed or dissipative options
  and repaired Cycle 727's coherent-channel item remain open. The present
  conditional identity is not evidence against them.

## Claim boundary

This is a finite-box parity-preservation census plus a conditional
direct-sum algebra lemma. It is not a constructed isometry, a physical or
coherent channel, an odd-sector bridge, a phase-selection theorem, a uniform
encoder, a preparation theorem, or a no-go theorem. Independent audit is
still required.
