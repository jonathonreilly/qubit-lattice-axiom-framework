# Minimal Framework Axioms (Lattice, Qubit, Admissibility, Record)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-29
**Type:** meta
**Status:** current public framework axiom memo for the qubit-on-`Z^3`
package with local admissibility and fixed record readout.
**Status authority:** explicit owner approval for the 2026-06-29 foundation
reset is recorded in `docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.
Audit status remains set only by the independent audit lane.

**Supersedes:** `MINIMAL_AXIOMS_2026-06-05.md`. The 2026-06-05 memo remains the
historical source for the prior Lattice/Quantum/Record wording in which
realized outcome was latent in Record and no explicit local admissibility
constraint was named.

## Purpose

This note states the framework's ontology and quantum probability premises.
They are named rather than treated as bare letter codes:

1. **Lattice**
2. **Qubit**
3. **Admissibility**
4. **Record**

Legacy `A1`/`A2` numbering and the older `Quantum` axiom name are historical.
New repo surfaces should use the axiom names above unless quoting an older
document.

## The Four Framework Axioms

### Lattice / Physical Locality

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

No site is privileged. Sites are distinguished by the supplied lattice
structure alone.

### Qubit / Site Possibility

Each site has a domain of local possibilities.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
adds no further primitive structure.

No possibility is privileged. Possibilities are distinguished by the supplied
algebraic structure alone.

For every finite region Lambda, the joint possibility *-algebra is the tensor
product of the one-site algebras in Lambda, with their usual adjoint and
positive cone. The embedding into a larger region tensors with the identity
on the additional sites. Disjoint-region
operations act on their respective tensor factors.


### Admissibility / Local Constraint

There is one fixed law for neighborhood quantum operations and record
formation, covariant under lattice translations and proper cubic rotations.
For fixed accessible record controls, each operation is a quantum instrument
supported in its finite neighborhood and extended by the identity outside.
On a finite outcome menu its outcome maps are linear and completely positive,
and their sum preserves trace. On a standard Borel outcome space it is a
countably additive completely-positive-map-valued measure with trace-preserving
total map. Instrument controls depend only on readable record values obtained
through permitted neighborhood interactions. Influence may pass
through successive overlapping neighborhoods.

For a specified record history used for conditioning, choose a finite region
containing the operation's support and its conditional reduced density matrix.
The probability of a measurable outcome event is the trace of the instrument
map, extended by the identity on the rest of that region, applied to this
matrix. A positive-probability event updates the matrix by this map followed
by normalization. These updates agree under restriction and define the updated
state family; reductions to other regions use a region also containing the
operation's support. For exact outcomes in a continuous menu, conditional
states are measurable versions of the almost-everywhere instrument-density
conditionals, not ratios of zero singleton probabilities. The fixed law
specifies those versions and which null histories, if any, lie in its domain.
Joint probabilities are obtained by composing the instruments. A no-formation
outcome may be included. A forming record locks a supported outcome through
the law's fixed measurable content map. Each realized formation has one outcome;
probabilities describe the law of those outcomes. Conditioning on a recorded
content event uses the instrument on its full preimage under the content map.
Every operation preserves all existing record contents.

Conditioning on a record and physically receiving that record are distinct.
Changing only the history used for conditioning does not change the realized
operation or its controls.
If the conditioning history does not fix the local controls, predictions
average the joint conditional control-and-quantum-state ensemble, equivalently
retaining the control register in the composed instrument.
Predictions available in a neighborhood condition only on its available
record history. Additional remote records may change conditional predictions,
but cannot control a local operation until conveyed through permitted
interactions. Ignoring an operation's outcome gives its trace-preserving
sum, which leaves statistics outside its support unchanged.

*Reading notes (interpretive, non-governing).* The conditioning history and
locally available control information are different objects. A remote result
can change conditional predictions without being an available local control.
The probability law of record contents is the pushforward of the instrument's
outcome law through its fixed measurable content map. Conditioning on a
recorded content uses its full preimage under that map, not an unavailable
refinement of the instrument outcome. Admissibility is support in this
law: on a finite menu this means nonzero probability; in an atomless law a
supported exact point can have zero singleton mass. A measurable instrument
on a finite carrier does not supply finite-register storage for a continuum
of distinct perfectly readable values. All pointer resources must be allocated.

### Record / Fixed Reality

Records form.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. A site with no record cannot be read.

A record's readable value is encoded in a quantum pointer on allocated
lattice sites and is reproduced with certainty by a permitted readout fixed
for that pointer type, independently of the stored value.
All sites used by that pointer and its readout controls are part of the
physical register.

## Qualification

These axioms state only their named primitive content. Further physical
structure requires a retained derivation or bridge, or explicit approved-
primitive registration, before use as a premise. A choice not fixed by the
supplied structure remains a named conditional or open dependency.

A state description consists of a configuration of permanent records and a
compatible joint quantum state of the lattice possibilities. The quantum
state is a family of normalized positive linear functionals on the finite-
region algebras, agreeing under restriction. It assigns probabilities to
possible new records; it is not an additional directly readable record.
Compatibility means that permitted readout of an existing record gives
its recorded value with certainty under that same quantum probability rule.
On a prepared domain where the records and fixed law uniquely determine this
family, the quantum state may be represented by that reconstruction.

A law privileges no states. Its domain is a supplied condition, and at every
state where the condition holds it gives exactly one answer.

## Audit-Pipeline Treatment

The machine-readable source of this axiom set is the stable `minimal_axioms`
entry in `docs/audit/data/axiom_premise_nodes.json`. Dependencies on
`minimal_axioms` chain-satisfy without making downstream rows
`retained_bounded`.

**Primary runner:** `scripts/audit_companion_minimal_axioms_clean_base_exact.py`
checks only elementary algebra/notation sanity for the four axiom names. It
does not derive or enlarge the axiom set.

Axioms and approved primitives are the complete supplied foundation.
Depending on the Lattice, Qubit, Admissibility, or Record axiom, or on an
explicitly approved primitive such as `scale_reference_primitive`, must not be
treated as a source of bounded status. No admission class exists: every other
scientific dependency must be retained-derived or remain conditional/open.

## Relation To Dynamics And Kinetic Branch Selection

Admissibility specifies the quantum form of local operations, probabilities,
conditional state updates and stochastic record registration. It does not
choose a particular Hamiltonian, instrument family, preparation, measurement
basis, outcome-content calibration, formation site/rate, time metric or causal
speed. Those physical choices remain separately supplied or derived.

Static spatial kinetic questions, quantum probability structure and the
selection of physical dynamics are distinct. A realized kinetic branch needs
a derivation or an explicitly approved primitive before it can supply that
physical content. The quantum instrument clause does not select a scalar or
nonzero kinetic branch, a Dirac-square carrier, physical couplings or a
continuum limit. Permanent quantum pointers are an ideal requirement; their
physical persistence dynamics and resource allocation are not supplied by a
bare symbolic record label.

## Relation To The Older Observable-Principle Parent

`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is not this axiom note and is not an
approved axiom-premise node. It remains a broader conditional parent that
packages additive scalar observables with further readout/log-det/modulus
structure. That older parent must not be moved wholesale into
`docs/audit/data/axiom_premise_nodes.json`.

Rows using the generic quantum composition, probability, conditioning and
record requirements should cite this minimal-axiom authority at its actual
revision. Identifying a physical preparation, observable, instrument, pointer
encoding, occurrence rate or dynamics still requires its own derived or
conditional bridge. P2/modulus, log-det, source/action, central-sector
selection and K/CPT identifications are not supplied by the generic quantum
probability structure. Earlier judgments made under different axiom content
must not be promoted or carried across the premise change without the
applicable review and audit checks.

Finite additivity over disjoint record collections, a named scalar collection
functional `I`, and an assigned
value `I(empty)=0` are not Record axiom content. Rows that require any of those
structures must likewise cite a separate retained authority or remain
conditional/open.

## Relation To The 2026-06-05 Record Wording

The 2026-06-05 Record axiom named durable realized-outcome registration and
gave a `K`/CPT orbit reading once a finite central-sector readout context and
fixed `K`/CPT conjugation were supplied. The 2026-06-29 reset distinguished generic site
possibility, local admissibility, and fixed records from context-specific
readout structure. The following bullets describe that historical separation,
before the proposed quantum formation revision:

- Qubit names the domain of local possibilities and its full one-site algebraic
  presentation.
- Admissibility names the neighborhood rule by which, for each site, the
  probability distribution over the possibilities is determined by, and
  varies with, the neighborhood conditions.
- Record names the fixed locking of one admissible local possibility,
  one-record-per-site uniqueness, permanence, content-determined readout, and
  the unreadability of a site with no record.
- `K`/CPT orbit structure, central-sector decomposition, and any sector
  generation rule are downstream readout-context content, not generic axiom
  content.

## Open Gates Outside The Axioms

The four axioms do not close, import, or rename the framework's downstream open
gates. In particular, the following remain outside axiom content:

- the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;
- the strong-CP theta gauge and mass-side derivation obligations;
- P2/modulus/phase-blindness and any log-det readout theorem;
- physical context and measurement-basis selection, calibrated preparations,
  observables, outcome-content maps, permitted instrument families, decoherence
  mechanisms, and the remaining formation choices (at which site and at what
  rate, with which physical coupling or apparatus);
- arrow, record-production dynamics, physical persistence dynamics, time metric,
  and physical implementation of record readout;
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
The 2026-07-04 owner-approved revision appended the formation sentence "Records
form." to the Record axiom: occurrence became named axiom content, while every
formation rule (which admissible possibility, at which site, with what weight,
at what rate) at that time remained downstream supplier content. The file path was kept
unchanged so existing runner needles and links continue to resolve.

The 2026-08-05 owner-approved revision replaced Admissibility's availability
sentence with the distribution sentence: for each site, the probability
distribution over the possibilities is determined by, and varies with, the
nearest-neighbor conditions. The determination of the distribution became
named axiom content; availability became the distribution's support (on finite
menus, exactly the possibilities of nonzero probability; in an atomless law,
supported exact points may have zero singleton measure); the distribution's
extensional form and values are not specified by this memo, and the formation
site/rate and realized draw remain downstream supplier content. The
measure/support formulation was adopted on independent
review (per-point likelihood under-specifies an atomless law on the continuous
one-site domain). The file
path was again kept unchanged so existing runner needles and links continue
to resolve.

The 2026-08-13 owner-approved revision removed the named scalar functional
`I`, finite additivity over disjoint record collections, and `I(empty)=0` from
Record. The replacement says that a site with no record cannot be read; it
does not assign a scalar value to absence. The file path remains unchanged so
the premise-epoch guard can invalidate old judgments and send consumers that
used the removed structure through fresh review and audit.

The 2026-11-09 quantum formation revision is proposed under the owner's
explicit instruction to update the axiom as needed to correctly select or
represent quantum physics. It adds finite-region quantum composition, a
compatible joint quantum probability state, local instruments, explicit
conditioning and a physical pointer requirement. It preserves definite
permanent records and distinguishes available controls from remote
conditioning. This is substantive new premise content, not a deduction from
the previous record constraints or a wording-only migration. Exact adoption
and landing remain governed by the axiom PR and the approval record.

Records are not arbitrary mosaics: proposed formation operations and pointer
readout must be compatible with the joint quantum state and all earlier
records. The particular physical law, preparation, rates, apparatus and
observable identifications remain downstream.
