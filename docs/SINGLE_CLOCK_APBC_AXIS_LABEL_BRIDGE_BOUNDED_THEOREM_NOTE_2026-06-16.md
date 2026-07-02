# Single-Clock APBC Axis-Label Bridge

**Date:** 2026-06-16
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set audit status, does not update audit data, and does not assert package
promotion.
**Primary runner:** [`scripts/frontier_single_clock_apbc_axis_label_bridge_2026_06_16.py`](../scripts/frontier_single_clock_apbc_axis_label_bridge_2026_06_16.py)
**Runner cache:** [`logs/runner-cache/frontier_single_clock_apbc_axis_label_bridge_2026_06_16.txt`](../logs/runner-cache/frontier_single_clock_apbc_axis_label_bridge_2026_06_16.txt)
**No-promotion statement:** This source note records a conditional bounded
bridge only; it creates no promotion, no registry edit, and no audit verdict.

## Result

This note packages the positive half of the single-clock axis-selection
route-pruning result:

```text
bc = (APBC, PBC, PBC, PBC)
```

is a per-axis `Z_2` boundary-condition datum. Conditional on a supplied
per-axis boundary-condition datum of this form, the APBC coordinate is an
invariantly selected axis label.

Equivalently, the axis-label part of `(B-AXIS.2)` in
`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`
can be discharged for rows that already carry this APBC/PBC datum:
the declared evolution axis is the unique APBC axis. This does not derive the
APBC/PBC datum.

## Proof Surface

On the even staggered block

```text
(L_tau, L_1, L_2, L_3) = (4, 4, 2, 2)
```

with time-first Kawamoto-Smit phases, the all-periodic surface is invariant
under the conjugated exchange

```text
W = P_{tau<->1} diag((-1)^(x_tau x_1)).
```

Adding APBC on `tau` while keeping `x_1` periodic breaks that exchange:

```text
|| W M_APBC(tau) W^T - M_APBC(tau) || > 0.
```

The distinction is not a basis artifact. The temporal APBC hop sector has
trivial kernel on the tested block, while the periodic `x_1` hop sector has
nonzero kernel. Kernel dimension is invariant under unitary relabeling, so no
signed exchange map can identify those two sectors once the boundary datum is
supplied.

The falsification leg is symmetric APBC: if both `tau` and `x_1` are APBC, the
same `W` exchange is restored exactly. Therefore the selecting input is the
boundary-condition asymmetry, not APBC by itself.

At the finite boundary-data level, the vector

```text
(A, P, P, P)
```

has automorphism group `S_3`, permuting only the three `P` axes. Every
automorphism fixes the APBC axis. Thus the supplied datum selects one axis
label without selecting a spatial orientation inside the residual spatial
`S_3`.

## Downstream Contract

This note supplies exact support for only one clause:

```text
B-AXIS.2 axis label, given the supplied APBC/PBC boundary datum.
```

B-AXIS.1 and B-AXIS.3 are untouched. This note does not close:

- `B-AXIS.1`, the supplied blocked time step `2 a_tau`;
- the existence or uniqueness of the RP/transfer construction itself;
- `B-AXIS.3`, exclusion of independent commuting transfer factors;
- derivation of the APBC/PBC boundary datum from the baseline axioms;
- any continuum, Wightman, interacting, or no-second-clock claim.

The single-clock theorem can cite this row only in the conditional form:

```text
if APBC-on-axis/PBC-on-others is supplied, then the axis-label part of
B-AXIS.2 is fixed by the APBC axis.
```

## Relation To The No-Go Pin

[`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`](SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md)
showed that the retained record, OS/GNS, registration-cone, and anomaly
surfaces are `W`-transportable and therefore do not derive the axis label.
Its sharpened pin identified the APBC/PBC asymmetry as a sufficient datum.

This note extracts that sufficient datum into an auditable bridge theorem. It
does not contradict the no-go: the no-go says the datum is not derived by the
retained surfaces it enumerates; this note says that once the datum is supplied,
the axis label is fixed.

## Honest Status

Bounded theorem / conditional support. The theorem is exact after the APBC/PBC
boundary datum is supplied. The datum itself is not derived, is not promoted to
an axiom, and is not an approved framework primitive here. This note does not
update audit data, does not set audit status, and does not land any effective
retained result.

## Runner Summary

The runner verifies:

- all-PBC exchange symmetry under `W`;
- failure of the plain unsigned exchange;
- APBC-on-`tau` / PBC-on-`x_1` breaks `W`;
- temporal APBC and spatial PBC hop sectors have different kernel dimensions;
- symmetric APBC restores `W`;
- the `A,P,P,P` boundary vector has exactly residual `S_3` symmetry and fixes
  the APBC axis;
- the target single-clock source note cites this bridge without status
  promotion and keeps B-AXIS live unless the APBC/PBC datum is supplied.

Expected scorecard after cache refresh:

```text
TOTAL: PASS=21 FAIL=0
```

## Citations

- target theorem:
  `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`
- route-pruning parent:
  [`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`](SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md)
- scope boundary:
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
