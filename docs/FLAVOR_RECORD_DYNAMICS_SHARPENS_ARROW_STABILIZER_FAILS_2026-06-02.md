# Flavor Record Dynamics: The Tested Thermalizing-Arrow Attractor/Stabilizer Routes Fail (Attractor-Scope No-Go)

**Date:** 2026-06-02 (2026-06-11: title and scope statement corrected to the
proof's own N4/N5 boundary — no claim changes, no runner changes; the old
title "Stabilizer Fails" overstated the closure as if it covered every use
of the fixed-point structure)
**Claim type:** no_go.
**Runner:** `scripts/flavor_record_dynamics_sharpens_arrow_stabilizer_fails_2026_06_02.py`.

This source note closes one proposed route: using a thermalizing time-arrow map
to force `r=1/2` as a dynamical attractor. It is not a no-go on the value and
does not derive record dynamics from the baseline axioms.

**Scope (made explicit 2026-06-11, matching N4/N6 below).** What is closed:
attractor/stabilizer dynamics in the tested family (the reverse map is
erasure; honest thermalization gives `r=1`; tested einselection is a no-op;
arrow parity carries no block-count information). Out of scope and NOT
closed here: stationarity/durability occupancy of a records-flow fixed point
(fixedness without attraction), and measure/reference choices. The
stationarity route is examined in
`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`
(plain-text reference; downstream of this note, not an input to it).

## Result

For the tested two-sector record map, Lüders self-composition sharpens:

```text
r -> 2 r^2.
```

The fixed point `r=1/2` has multiplier `2`, so it is unstable. Iterating from
`r=0.49` runs away toward `0`.

The map

```text
g(r) = sqrt(r/2)
```

does make `r=1/2` stable, but it is the formal reverse of the sharpening map in
this one-dimensional variable. It is record erasure in the tested model, not a
record-forming channel.

The runner also verifies that the C3-invariant generation operator is already
block diagonal in the singlet/doublet isotype projectors, so the tested
einselection channel is a no-op on `r`. Finally, thermalizing to `I/3` gives
dimension weights `(1/3,2/3) -> r=1`, not `r=1/2`.

## Consequence

The thermalizing-arrow stabilizer route does not force `r=1/2`: nothing in
the tested record dynamics makes it a dynamical attractor. The remaining
routes (corrected 2026-06-11 to enumerate what the proof actually leaves
open) are: (i) a measure/reference choice on the two-sector partition, or
(ii) a stationarity/durability principle — occupancy of a records-flow fixed
point without any attraction claim, which this note's N4 scope never tested.
The earlier wording named only route (i).

## No-Go Discipline Gate

This gate applies only to the narrow route closure above.

### N1 - Alternative route enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Sharpening route | Use record self-composition to stabilize `r=1/2`. | Fails: `r=1/2` is unstable with multiplier `2`. |
| Reverse-map route | Use `sqrt(r/2)` to stabilize `r=1/2`. | Fails as a record-forming route: it is the tested reverse/erasure map. |
| Einselection route | Let block decoherence flow the measure. | Fails in the tested family: the operator is already block diagonal. |
| Thermal equilibrium route | Let honest thermalization choose the value. | Fails for `r=1/2`: `I/3` gives `(1/3,2/3) -> r=1`. |
| Arrow parity route | Use conjugation-even time direction to select block count. | Fails in the tested setup: it carries no selective information for block count. |
| Measure-admission route | Approve block count as the measure. | Possible future route, but not a dynamical derivation. |

### N2 - Wall Independence

The collapsed residual is one measure/reference choice. Dynamics, basis, and
measure are separate axes.

### N3 - Hidden-Wall Scan

"Record dynamics" names the tested Lüders/self-composition and block
einselection maps only. No general theorem about all possible dynamics is
claimed.

### N4 - Residual Matching

The residual checked is whether the tested dynamics makes `r=1/2` an attractor.
It is not a claim about all future dynamics or all possible reference-state
principles.

### N5 - Rhetoric Audit

The negative statement is restricted to the thermalizing-arrow stabilizer
route. The value remains open as a measure choice.

### N6 - Partial-Closure Path Scan

A future derivation of a physical channel with `r=1/2` as an attractor could
reopen the dynamics route. A direct block-measure admission could close the
value without using dynamics. Neither is supplied by the Lattice, Quantum, or
Record axioms.

### N7 - Steelman

A hostile reviewer can argue that a real record-production model may not be the
tested Lüders self-composition map and could have a different attractor. That
is accepted; this note closes only the tested stabilizer route.

### N8 - Cross-Cycle Echo

Prior flavor work separates basis selection, phase handling, dynamics, and
measure choice. This note keeps that split: dynamics does not silently become
the measure selector.

**Gate result:** pass for the narrow route closure only.
