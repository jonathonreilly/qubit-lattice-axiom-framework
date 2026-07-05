# Zero-Import Hydrogen: Lepton `1/256` Full-Cell Source-Carrier Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-carrier support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_full_cell_source_carrier_support.py`

## Scope

This note follows the A1 tensor-lift firewall:

- `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md`
  shows that OS0 supplies the four-slot geometry, while D17 supplies only the
  charged-lepton scalar singlet and its `1/sqrt(2)` block normalization.
- The missing A1 theorem is not the finite count. It is the carrier statement
  that the charged-lepton scalar source is local over a full OS0 cell, with one
  `M_2(C)` algebra factor per OS0 slot.

This note proves the finite positive half of that carrier statement:

```text
If the charged-lepton scalar source is a full OS0-cell linear source over the
four local qubit-slot algebras, then its source-carrier coordinate space is
M_2(C)^tensor4 and has 256 matrix-unit coordinates.
```

It does not prove that the charged-lepton scalar source has that full-cell
source locality, does not prove the source-coupled local-action convention, and
does not identify the resulting carrier with `S_l`.

## Conditional Theorem

Let an OS0 cell have four regulator slots

```text
s in {x, y, z, tau}.
```

The Qubit axiom supplies the one-site possibility algebra

```text
A_s = M_2(C)
```

for each slot once the OS0 regulator cell is in view. As a complex vector
space,

```text
dim_C A_s = 4.
```

If the charged-lepton scalar source is a full-cell linear source, its local
source-carrier algebra is the tensor product

```text
A_cell = A_x tensor A_y tensor A_z tensor A_tau
       = M_2(C)^tensor4.
```

Choosing the matrix-unit basis `E_11, E_12, E_21, E_22` in each slot gives

```text
C = {0,1,2,3}^4
O_c = E_{c_x} tensor E_{c_y} tensor E_{c_z} tensor E_{c_tau}
|C| = 4^4 = 256.
```

A full-cell linear source has the coordinate form

```text
S_src[J] = sum_{c in C} j_c O_c.
```

Therefore the source-carrier coordinate space has exactly `256` independent
matrix-unit coordinates. This is the A1 carrier count needed by the later A2
source-density route.

## Why The Assumption Is Load-Bearing

The theorem depends on **full-cell source locality**. Weaker source shapes do
not give the same carrier:

| source shape | coordinate count | consequence |
|---|---:|---|
| full-cell tensor source `A_x tensor A_y tensor A_z tensor A_tau` | `4^4 = 256` | supports the A1 carrier count |
| slot-additive source `A_x + A_y + A_z + A_tau` | `4 * 4 = 16` | too small for the `1/256` carrier |
| diagonal slot-locked source `c_x = c_y = c_z = c_tau` | `4` | too small |
| scalar/tracial source only | `1` | no matrix-unit carrier |
| D17 weak-isospin singlet alone | `2` components before unit normalization | supplies `1/sqrt(2)`, not `M_2(C)^tensor4` |

So the support theorem is not A1 closure. It narrows A1 to the physical
claim that the charged-lepton scalar source is a full OS0-cell source rather
than a slot-additive, diagonal, scalar, tracial, or D17-only source.

## Authority Boundary

The retained/approved surfaces split cleanly:

| source | supplies | does not supply |
|---|---|---|
| `MINIMAL_AXIOMS_2026-06-29.md` | one-site `M_2(C)` possibility algebra | source/action, physical-observable identification, probabilities, weights, dynamics |
| `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | OS0 `Z^3 x Z_tau` regulator geometry | selector, readout bridge, normalization rule, mass ratio |
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | charged-lepton scalar singlet and `1/sqrt(2)` normalization | OS0-cell source carrier |
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | candidate convention for source-coupled local action | retained derivation of the convention or lepton-specific full-cell source locality |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md` | if linear source simplex and local relabeling symmetry are supplied, coefficient uniformity gives `1/256` | source convention, physical frame, charged-lepton bridge |

The source-coupled local-action candidate is relevant because it has the right
shape: local source derivatives define local operator insertions. But it is an
`open_gate`, not an approved primitive or retained theorem. This note therefore
uses it only as a route marker.

## What This Moves

| Before | After |
|---|---|
| A1 asked vaguely how four OS0 `M_2(C)` factors attach to the charged-lepton scalar coefficient. | The finite carrier part is explicit: full OS0-cell linear source locality implies `M_2(C)^tensor4`. |
| A1 could be confused with D17 weak-isospin normalization. | D17 remains the `1/sqrt(2)` block anchor; the `256` carrier is a separate source-carrier algebra. |
| A2 source-density work had to keep rechecking the carrier count. | A2 may assume the `256` carrier only after full-cell source locality and physical frame selection are supplied. |

The paired D17/full-cell note
`ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md`
checks that separation explicitly: with a supplied scalar source multiplier,
D17's `1/sqrt(2)` block normalization and the `256` source weights do not have
to collapse into a `512`-component unit vector.

## Remaining A1 Residual

The live A1 target is now:

```text
charged-lepton scalar source
  -> full OS0-cell source locality over x,y,z,tau qubit slots
  -> physical tensor-product matrix-unit source frame
  -> M_2(C)^tensor4 carrier.
```

This residual is smaller than the old tensor-lift wall, but still real. The
framework must still derive or explicitly admit:

1. the source-coupled local-action convention, or another retained source
   semantics with the same carrier consequence;
2. charged-lepton sector specificity, so the full-cell carrier attaches to the
   charged-lepton scalar source and not to every regulator-side source;
3. full-cell tensor locality rather than slot-additive, diagonal, scalar, or
   tracial locality;
4. A2 readout/source-density semantics selecting `1/256` instead of `1/16`;
5. A3 precision correction from exact `256` to the comparator divisor
   `256.082435...`, or a direct noninteger-divisor theorem.

## Open PR Alignment

Open PRs were checked on 2026-07-04. The current open-review surface sharpens
context but does not close this A1 carrier theorem on current main:

| PR | effect on A1 |
|---|---|
| `#4925` presentation-gauge axis-sign theorem | Provides fresh gauge-section/orientation context, but not a charged-lepton full-cell source-locality theorem. |
| `#4903` D4 kinetic pattern dichotomy | Potentially relevant to per-direction algebra-dimension patterns, but it is open/dirty, selector-undecided, and not a lepton scalar source theorem. |
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | Useful normalization/readout context; they do not prove full-cell source locality or matrix-unit source-frame selection for the lepton scalar. |
| `#4932` AC measure binary axiom shortcut block | Koide K1 hygiene; it blocks an axiom/primitives shortcut but does not provide the charged-lepton full-cell source carrier. |
| `#4933` theta mass no-go | Theta hygiene; no direct A1 movement. |

## No-Go Discipline Gate

This section prevents overclaiming the support theorem. The broad claim "A1 is
closed" is **not** shipped. The narrowed claim is: full OS0-cell linear source
locality would supply the `M_2(C)^tensor4` carrier; the framework still must
derive or admit that full-cell source locality for the charged-lepton scalar.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| full-cell linear source | Treat the scalar source as a linear source over `A_x tensor A_y tensor A_z tensor A_tau`. | SUPPORTED CONDITIONALLY. It gives the `256` carrier. |
| slot-additive source | Couple separately to four one-slot source algebras. | ATTEMPTED. It gives `16` coordinates, not `256`. |
| diagonal slot-locked source | Force the same coordinate choice in all four slots. | ATTEMPTED. It gives `4` coordinates, not `256`. |
| scalar/tracial source | Couple only to the identity or trace channel. | ATTEMPTED. It gives `1` coordinate, not `256`. |
| D17 singlet alone | Use the charged-lepton scalar-singlet theorem as the carrier. | ATTEMPTED. It gives the `1/sqrt(2)` weak-isospin block anchor, not the OS0-cell source carrier. |
| source-coupled local-action candidate | Use the local-action convention to justify source derivatives as local operator insertions. | OPEN. The candidate has the right shape but remains an open gate, not retained closure. |
| D4 kinetic-pattern PR | Use open per-direction algebra-dimension work. | OPEN/UNMERGED. It may help later, but currently supplies no lepton scalar source theorem. |

### N2 - Wall-independence audit

| pair | closes automatically? | conclusion |
|---|---|---|
| source convention <-> charged-lepton sector specificity | no in either direction | independent |
| source convention <-> full-cell tensor locality | no in either direction | independent |
| charged-lepton sector specificity <-> full-cell tensor locality | no in either direction | independent |
| full-cell tensor locality <-> A2 readout/source density | no in either direction | independent |
| A2 readout/source density <-> A3 precision correction | no in either direction | independent |

The finite theorem closes only the conditional carrier arithmetic after the
first three source-side walls are supplied. It does not collapse A2 or A3.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `full-cell` | explicit source-locality wall. |
| `source` / `local action` | explicit source-convention wall; candidate only. |
| `charged-lepton` | explicit sector-specificity wall. |
| `matrix-unit` / `tensor-product frame` | explicit physical source-frame wall. |
| `primitive` / `registered` | primitive registry checked; approved primitives are used only to declared content. |
| `readout` / `normalization` / `density` | A2 wall, not supplied here. |

No source-locality, sector, or readout premise is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md` | A1 carrier attachment and A2 readout separation | yes |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md` | OS0 geometry slots and `4^4 = 256` count | yes for geometry, not source locality |
| `LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md` | charged-lepton scalar singlet and `1/sqrt(2)` normalization | yes as D17 anchor, no as full-cell carrier |
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | source-coupled local-action convention candidate | route marker only; not closure |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md` | coefficient uniformity after source-action semantics and physical frame are supplied | downstream A2 support, not A1 source locality |

No cited surface is counted as a retained derivation of charged-lepton
full-cell source locality.

### N5 - Rhetoric audit

The note avoids claiming A1 closure or saying "`S_l` is derived." Tested
resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| one-slot algebra | yes | `dim_C M_2(C) = 4`. |
| full four-slot tensor carrier | yes | `4^4 = 256`. |
| slot-additive source | yes | `16`, not `256`. |
| diagonal slot-locked source | yes | `4`, not `256`. |
| scalar/tracial source | yes | `1`, not `256`. |
| physical charged-lepton full-cell locality | not closed | named as the remaining A1 residual. |
| A2 source-density readout | not closed | downstream wall. |

### N6 - Partial-closure path scan

The primitive registry was checked. `minimal_axioms`,
`kinetic_isotropy_primitive`, `scale_reference_primitive`, and
`realized_state_primitive` are approved premise nodes, but only to their
declared content. The relevant partial-closure path is the
source-coupled local-action candidate: if adopted and re-audited in a
lepton-specific full-cell form, it could close the source-convention part of
A1 without adding a new axiom. This note therefore does not say a new axiom is
required.

### N7 - Steelman

A hostile reviewer can argue that this effectively closes A1: the current
foundation already has one-site `M_2(C)`, OS0 already supplies the
`Z^3 x Z_tau` cell, and a Yukawa term is a source/action term, so the
charged-lepton scalar source should automatically be a full-cell source over
`M_2(C)^tensor4`. That is the strongest positive reading. The reply is scope:
the minimal axioms explicitly leave source/action outside axiom content, the
source-coupled local-action note is still an open gate, and D17 proves the
weak-isospin scalar contraction, not OS0 full-cell locality.

### N8 - Cross-cycle echo

This mirrors two prior patterns. First, kinetic isotropy turned a hidden
geometry premise into an approved primitive while leaving downstream selectors
separate. Second, the observable-principle source-coupled local-action note
shows a convention/adoption path can relocate a wall without becoming a new
axiom. The same mechanism may apply here: a future lepton-specific source
convention could close part of A1 by reframe and audit, but it has not done so
yet.

**Gate result:** broad A1 closure fails; narrowed full-cell carrier support
passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar source has full OS0-cell source
  locality.
- No derivation of the source-coupled local-action convention.
- No derivation of charged-lepton sector specificity for the full-cell carrier.
- No derivation of A2 source-density readout.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_full_cell_source_carrier_support.py
```

The verifier checks the finite carrier counts, weaker-source counterexamples,
source-authority boundaries, open-PR references, and non-claim guards.
