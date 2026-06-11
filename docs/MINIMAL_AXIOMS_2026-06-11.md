# Minimal Framework Axioms (Lattice, Quantum, Record)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-11
**Type:** meta
**Status:** current public framework axiom memo for the qubit-on-`Z^3`
package with durable scalar record readout.
**Status authority:** explicit owner approval for the 2026-06-11 Record
rewording is recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.
Audit status remains set only by the independent audit lane.

**Supersedes:** `MINIMAL_AXIOMS_2026-06-05.md`. The 2026-06-05 memo remains
the historical source for the prior `K`/CPT-orbit Record wording. New
framework-facing surfaces should cite this memo.

## Purpose

This note states the framework's minimal premises. They are named rather than
treated as bare letter codes:

1. **Lattice**
2. **Quantum**
3. **Record**

Legacy `A1`/`A2` numbering in older notes is historical. New repo surfaces
should use the axiom names above unless quoting an older document.

## The Three Framework Axioms

### Lattice

The site set is `Z^3` with standard translation action and nearest-neighbor
cubic adjacency. Finite-range locality means finite support or finite
graph-distance range with respect to this lattice when a local expression is
specified.

This axiom supplies the discrete site set and local adjacency notion. It does
not supply a dynamics, boundary condition, metric scale, lattice spacing,
continuum or infrared limit, causal cone, probabilistic independence rule, or
physical unit conversion.

### Quantum

At each site `x`, the primitive physical local degree of freedom is one qubit;
equivalently, the primitive one-site operator algebra is
`A_x ~= M_2(C)`, equivalently `Cl(3,0)` in its real-algebra reading.

This axiom supplies the one-site algebraic carrier. It does not supply a
dynamics, composition theorem beyond the named lattice placement, measurement
instrument, Born rule, species identification, gauge group, particle content,
or physical observable bridge.

### Record

A record is the durable registration of the realized outcome.

Given a readout context with a finite central-sector decomposition and a
registered scalar surface, the realized outcome is the realized central
sector individuated by that surface: sectors that no readout in the context's
registered surface distinguishes register as the same outcome. For any finite
pairwise-disjoint collection of records, the scalar readout `I` is finitely
additive, with `I(empty)=0`.

Durable means fixed once registered: the recorded outcome does not change. A
record supplies no readout context, decomposition, registered surface,
`K`/CPT structure, sector-generation rule, weighting, normalization,
probability, measurement/decoherence dynamics, time metric, within-sector
data, or occupancy rule.

## Relation To The Prior K/CPT-Orbit Wording

The 2026-06-05 Record wording stated the realized outcome as the `K`/CPT
orbit of the realized central sector, given a context supplying a fixed
`K`/CPT conjugation. That outcome structure is recovered exactly under this
memo's wording: when a context's registered surface is invariant under a
`K`/CPT conjugation compatible with its decomposition and separates its
orbits, the individuation classes are exactly the `K`/CPT orbits
(`KCPT_ORBIT_CLAUSE_KINVARIANT_SURFACE_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-06-10.md`,
both directions). Rows that consumed the orbit clause consume the same
outcome structure through their context's surface properties. The rewording
relocates where the same content sits; it does not add or remove strength.

## Audit-Pipeline Treatment

The machine-readable source of this axiom set is the stable `minimal_axioms`
entry in `docs/audit/data/axiom_premise_nodes.json`. Dependencies on
`minimal_axioms` chain-satisfy without making downstream rows
`retained_bounded`.

**Primary runner:** `scripts/audit_companion_three_axiom_clean_base_exact.py`
checks only elementary algebra/notation sanity for the three axiom names. It
does not derive or enlarge the axiom set.

Axioms and approved primitives are not Tier-A admitted derivation targets.
Depending on the Lattice, Quantum, or Record axiom, or on an explicitly
approved primitive such as `scale_reference_primitive`, must not be treated as
a source of bounded status. Bounded status belongs to non-axiom Tier-A
admissions recorded in `docs/audit/data/tier_a_admissions.json`.

## Relation To The Older Observable-Principle Parent

`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not this axiom note and is not an
approved axiom-premise node. It remains a broader conditional parent that
packages additive scalar observables with further readout/log-det/modulus
structure. That older parent must not be moved wholesale into
`docs/audit/data/axiom_premise_nodes.json`.

Rows that require only the Record axiom should cite this minimal-axiom
authority. Rows that require P2/modulus, log-det, source/action, measurement,
Born weights, record-production dynamics, physical persistence dynamics, or
any other additional bridge must cite separate retained authorities or remain
bounded/pending according to the audit ledger.

## Open Gates And Admissions Outside The Axioms

The three axioms do not close, import, or rename the framework's downstream
open gates. In particular, the following remain outside axiom content:

- the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;
- the strong-CP theta admission;
- P2/modulus/phase-blindness and any log-det readout theorem;
- arrow, measurement, decoherence, record-production dynamics, and physical
  persistence dynamics;
- source/action and physical-observable identification;
- `g_bare = 1` convention handling;
- the scale-reference primitive and the separate gravity self-consistency
  question that the framework's natural unit equals the Planck length;
- the dimension-consolidation surface: theorems about the Lattice axiom's
  `Z^3` (the qubit adjacency-rank bound and the dimension-selection pinch)
  are derivation rows about the axiom, not axiom content; `Z^3` remains
  posited here, and those rows carry their own named scopes.

## Historical Context

The April 15 through May 20 sequence separated the one-qubit local algebra and
the `Z^3` lattice from downstream realization gates that had previously been
written too axiomatically. The 2026-06-04 memo added scalar finite Record
additivity as the third explicitly approved premise. The 2026-06-05 memo
refined Record to durable realized-outcome registration with the `K`/CPT-orbit
outcome clause. This memo rewords the Record outcome clause to
surface-individuation form on the strength of the landed two-way equivalence,
preserving the same premise boundary: no readout context, decomposition,
registered surface, probability, dynamics, or downstream theory consequence
is added by the axiom itself.
