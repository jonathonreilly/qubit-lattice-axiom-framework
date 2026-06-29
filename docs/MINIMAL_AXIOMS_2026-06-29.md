# Minimal Framework Axioms (Lattice, Qubit, Actualization, Record)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-29
**Type:** meta
**Status:** current public framework axiom memo for the qubit-on-`Z^3`
package with an explicit actualization relation and fixed scalar record readout.
**Status authority:** explicit owner approval for the 2026-06-29 foundation
reset is recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.
Audit status remains set only by the independent audit lane.

**Supersedes:** `MINIMAL_AXIOMS_2026-06-05.md`. The 2026-06-05 memo remains the
historical source for the prior Lattice/Quantum/Record wording in which
realized outcome was latent in Record rather than named as an explicit
actualization relation.

## Purpose

This note states the framework's minimal ontology premises. They are named
rather than treated as bare letter codes:

1. **Lattice**
2. **Qubit**
3. **Actualization**
4. **Record**

Legacy `A1`/`A2` numbering and the older `Quantum` axiom name are historical.
New repo surfaces should use the axiom names above unless quoting an older
document.

## The Four Framework Axioms

### Lattice / Locality

Reality has a discrete locality substrate. The primitive site set is `Z^3`
with standard translation action and nearest-neighbor cubic adjacency.

Local structure is finite-supported or finite graph-distance range with
respect to this lattice when a local expression is specified.

### Qubit / Local Alternatives

At each site `x`, the primitive local quantum degree of freedom is one qubit;
equivalently, the primitive one-site operator algebra is `A_x ~= M_2(C)`.

This is the local capacity for alternatives.

A real `Cl(3,0)`-compatible encoding may be used as notation. This encoding
does not add primitive spin, rotation, gauge, or geometric content.

### Actualization / Definite Realization

For finite lattice support and a declared readout context with an outcome set,
a primitive actualization relation identifies exactly one context-indexed
realized outcome.

Actualization names definite realization within the declared context. It does
not choose the context or specify an occurrence rule.

### Record / Fixed Registration

A record is a context-indexed registration of a realized outcome whose
registered value is fixed within that context.

For any finite pairwise-disjoint collection of records, scalar record readout
`I` is finitely additive, with `I(empty)=0`.

Fixed means the registered value is an invariant of that record identity within
the declared context.

## Boundary Convention

These axioms state only their named primitive content. Additional structures
such as probability rules, update laws, metric scale, measurement basis, gauge
content, species identity, observable bridges, source/action bridges, occurrence
rules, context-selection rules, central-sector decompositions, `K`/CPT
structure, weighting, normalization, log-det readouts, P2/modulus structure,
law-admissibility or transition relations, record-production dynamics, physical
persistence dynamics, or local observability remain compatible downstream
targets, but require derivation, bridge, or explicit admission before use.

This convention replaces the older "does not supply" wording pattern. It is an
anti-laundering rule, not an exclusion rule: a downstream structure is not
primitive content of an axiom merely because it is compatible with that axiom.

## Audit-Pipeline Treatment

The machine-readable source of this axiom set is the stable `minimal_axioms`
entry in `docs/audit/data/axiom_premise_nodes.json`. Dependencies on
`minimal_axioms` chain-satisfy without making downstream rows
`retained_bounded`.

**Primary runner:** `scripts/audit_companion_three_axiom_clean_base_exact.py`
checks only elementary algebra/notation sanity for the four axiom names. It
does not derive or enlarge the axiom set.

Axioms and approved primitives are not Tier-A admitted derivation targets.
Depending on the Lattice, Qubit, Actualization, or Record axiom, or on an
explicitly approved primitive such as `scale_reference_primitive`, must not be
treated as a source of bounded status. Bounded status belongs to non-axiom
Tier-A admissions recorded in `docs/audit/data/tier_a_admissions.json`.

## Relation To Dynamics And Kinetic Branch Selection

Actualization is not a dynamics axiom. It names definite realization within a
declared context; it does not by itself select a scalar or nonzero kinetic
branch, assert a Dirac-square carrier, choose a Hamiltonian or transfer
operator, or provide a law-admissibility relation, record-production process,
or temporal evolution.

Static spatial kinetic questions, law-admissibility/process questions, and
temporal evolution questions should be tracked separately. A realized kinetic
branch, if proposed, is downstream content: it needs derivation, bridge,
explicit admission, or approved primitive registry update before audit rows may
use it as load-bearing content. The four axioms are compatible with such later
Actualization-instance content, but do not include it.

## Relation To The Older Observable-Principle Parent

`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not this axiom note and is not an
approved axiom-premise node. It remains a broader conditional parent that
packages additive scalar observables with further readout/log-det/modulus
structure. That older parent must not be moved wholesale into
`docs/audit/data/axiom_premise_nodes.json`.

Rows that require only the Record axiom should cite this minimal-axiom
authority. Rows that require P2/modulus, log-det, source/action, measurement,
Born weights, readout-context selection, central-sector decomposition, `K`/CPT
structure, law-admissibility or transition relations, record-production
dynamics, physical persistence dynamics, local observability, or any other
additional bridge must cite separate retained authorities or remain
bounded/pending according to the audit ledger.

## Relation To The 2026-06-05 Record Wording

The 2026-06-05 Record axiom named durable realized-outcome registration and
gave a `K`/CPT orbit reading once a finite central-sector readout context and
fixed `K`/CPT conjugation were supplied. This reset separates the generic
actualization interface from context-specific readout structure:

- Actualization names the primitive relation from local alternatives, under a
  declared context, to one context-indexed realized outcome.
- Record names fixed registration of that realized outcome.
- `K`/CPT orbit structure, central-sector decomposition, and any sector
  generation rule are downstream readout-context content, not generic axiom
  content.

## Open Gates And Admissions Outside The Axioms

The four axioms do not close, import, or rename the framework's downstream open
gates. In particular, the following remain outside axiom content:

- the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;
- the strong-CP theta admission;
- P2/modulus/phase-blindness and any log-det readout theorem;
- context selection, measurement basis selection, Born weights, probability
  rules, update laws, decoherence mechanisms, and occurrence rules;
- arrow, record-production dynamics, physical persistence dynamics, time metric,
  and local observability of records;
- source/action and physical-observable identification;
- `g_bare = 1` convention handling;
- the scale-reference primitive and the separate gravity self-consistency
  question that the framework's natural unit equals the Planck length.

## Historical Context

The April 15 through May 20 sequence separated the one-qubit local algebra and
the `Z^3` lattice from downstream realization gates that had previously been
written too axiomatically. The 2026-06-04 memo added scalar finite Record
additivity as the third explicitly approved premise. The 2026-06-05 memo refined
Record to durable realized-outcome registration in a supplied readout context.

This memo exposes a latent premise in that Record wording: realized outcome
requires a named actualization interface. Actualization is therefore stated as
its own narrow axiom, while context selection, probability, update dynamics,
physical observability, and phenomenological bridges remain downstream.
