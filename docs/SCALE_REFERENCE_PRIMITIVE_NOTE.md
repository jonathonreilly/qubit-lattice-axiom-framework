# Scale-Reference Primitive

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta
**Status:** framework primitive declaration. Registered in
`docs/audit/data/axiom_premise_nodes.json` as
`scale_reference_primitive`. Explicit owner approval is recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.

## What This Declares

The framework takes exactly one dimensionful reference: a scale that converts
the framework's lattice-natural units to physical units. The chosen reference
is the Planck mass scale, `a^{-1} = M_Pl`.

This is a units conversion, not a physics axiom. It carries zero dimensionless
content: no mass ratio, coupling, mixing angle, phase, selector, readout
bridge, or empirical fit is supplied by it. A row whose only otherwise
non-retained dependency is this scale-reference primitive should not become
`retained_bounded` merely for using a ruler.

## Why It Is A Primitive

The framework baseline, Lattice + Qubit + Admissibility + Record, carries no
dimensionful number. Any derived quantity from that structural core is dimensionless or
carries a power of the lattice spacing `[a]^n`; its physical unit is
undetermined until one dimensionful reference is supplied.

That reference is irreducible by dimensional analysis. A dimensionful scale
cannot be derived from purely dimensionless structure, and treating this one
scale choice as a Tier-A admitted derivation target incorrectly bounds lanes
whose dimensionless content is otherwise clean.

## What This Does Not Do

- It does not add or amend an axiom. The minimal framework baseline is the
  four named axioms in `MINIMAL_AXIOMS_2026-06-29.md`: Lattice, Qubit,
  Admissibility, and Record.
- It does not assert `a/l_P = 1` as a derived theorem. The self-consistency
  question that the framework's natural unit equals the Planck length remains
  a separate open gravity derivation.
- It does not supply any dimensionless quantity. Dimensionless physics must
  still derive from the framework baseline or be explicitly recorded as a
  bounded Tier-A admission.
- It does not change any audit verdict. Audit status remains set only by the
  independent audit lane.

## Audit-Pipeline Treatment

The machine-readable distinction is:

- `docs/audit/data/axiom_premise_nodes.json` lists framework axioms and
  explicitly approved framework primitives. These dependencies chain-satisfy
  without bounding downstream rows.
- `docs/audit/data/tier_a_admissions.json` lists non-axiom derivation-target
  admissions. These dependencies chain-satisfy only at `retained_bounded`
  until the relevant admission is retired by a retained derivation.

The scale-reference primitive belongs to the first registry, not the second.
