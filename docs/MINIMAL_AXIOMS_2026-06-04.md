# Minimal Framework Axioms (Lattice, Quantum, Record)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta
**Status:** current public framework axiom memo for the qubit-on-`Z^3`
package with scalar record readout.
**Status authority:** explicit owner approval for the Record axiom is recorded
in `docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6. Audit status remains set
only by the independent audit lane.

**Supersedes:** `MINIMAL_AXIOMS_2026-05-20.md`. The 2026-05-20 qubit reframe
remains the local-algebra authority and historical source for the prior
two-axiom wording. New framework-facing surfaces should cite this memo.

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

When a finite record-readout surface is specified, its scalar record functional
is additive over disjoint record collections:

```text
I(R_1 sqcup R_2) = I(R_1) + I(R_2)
```

with `I(empty)=0` after an explicit additive-baseline convention.

This axiom supplies only additive scalar record readout. It does not supply a
rule for record production, persistence, measurement/decoherence, Born
weights, P2/modulus/phase-blindness, log-det structure, time arrow, system
composition, normalization/scale, source/action identification,
`AC_phi_lambda`, theta, or arbitrary observable identification.

## Audit-Pipeline Treatment

The machine-readable source of this axiom set is the stable `minimal_axioms`
entry in `docs/audit/data/axiom_premise_nodes.json`. Dependencies on
`minimal_axioms` chain-satisfy without making downstream rows
`retained_bounded`.

**Primary runner:** `scripts/audit_companion_three_axiom_clean_base_exact.py`
checks only elementary algebra/notation sanity for the three axiom names. It
does not derive or enlarge the axiom set.

Axioms and approved primitives are the complete supplied foundation.
Depending on the Lattice, Quantum, or Record axiom, or on an explicitly
approved primitive such as `scale_reference_primitive`, must not be treated as
a source of bounded status. Every other scientific dependency must be retained-
derived or remain conditional/open; decision history supplies no premise.

## Relation To The Older Observable-Principle Parent

`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not this axiom note and is not an
approved axiom-premise node. It remains a broader conditional parent that
packages additive scalar observables with further readout/log-det/modulus
structure. That older parent must not be moved wholesale into
`docs/audit/data/axiom_premise_nodes.json`.

Rows that require only finite scalar record additivity should cite this
minimal-axiom authority. Rows that require P2/modulus, log-det, source/action,
measurement, Born weights, or any other additional bridge must cite separate
retained authorities or remain bounded/pending according to the audit ledger.

## Open Gates Outside The Axioms

The three axioms do not close, import, or rename the framework's downstream
open gates. In particular, the following remain outside axiom content:

- the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;
- the strong-CP theta derivation obligations;
- P2/modulus/phase-blindness and any log-det readout theorem;
- arrow, measurement, decoherence, and record-production dynamics;
- source/action and physical-observable identification;
- `g_bare = 1` convention handling;
- the scale-reference primitive and the separate gravity self-consistency
  question that the framework's natural unit equals the Planck length.

## Historical Context

The April 15 through May 20 sequence separated the one-qubit local algebra and
the `Z^3` lattice from downstream realization gates that had previously been
written too axiomatically. This memo preserves that separation while adding
Record as the third explicitly approved premise. It does not re-promote the
older A3/A4 material or any later derivation target.
