# Proposed quantum formation amendment: exact wording and consequences

Status: proposed foundation revision, not governing axiom content.

Owner hold, 2026-11-09: "dont update the axiom until we prove the change works".
All four uncommitted governing-source edits were restored to main bf92a1d7.
This is non-governing candidate wording. No axiom PR is opened. The finite
construction is checked; joint satisfaction of the complete proposed package
remains the proof obligation in JOINT_MODEL_OBLIGATION.md.

 The owner
authorized considering and making a needed axiom change to correctly select or
represent quantum physics. This text makes the substantive change reviewable;
it does not claim that quantum theory follows from the old premises. The source
comparison is against MINIMAL_AXIOMS_2026-06-29.md at main bf92a1d7, SHA-256
301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc.

## Recommendation

Keep Lattice and Record's definite-content, permanence and readability clauses;
tie physical readout to the same quantum probability structure.
Add quantum composition, replace the ambiguous local-probability clause with
local quantum formation and explicit conditioning, and enlarge the general
state description. This is a substantive adoption of finite-region quantum
probability and instruments. It is not a two-word clarification or a derivation
of quantum mechanics. A prepared record-only model remains a restriction when
its preparation/history records uniquely reconstruct the quantum state.

### Qubit: addition after its existing text

Old: no joint-composition clause; the supplied algebra is one-site M2(C).

Proposed addition:

> For every finite region Lambda, the joint possibility *-algebra is the tensor
> product of the one-site algebras in Lambda, with their usual adjoint and
> positive cone. The embedding into a larger region tensors with the identity
> on the additional sites. Disjoint-region
> operations act on their respective tensor factors.

### Qualification: replace the state sentence

Old:

> A state is a configuration of records.

Proposed replacement:

> A state description consists of a configuration of permanent records and a
> compatible joint quantum state of the lattice possibilities. The quantum
> state is a family of normalized positive linear functionals on the finite-
> region algebras, agreeing under restriction. It assigns probabilities to
> possible new records; it is not an additional directly readable record.
> Compatibility means that permitted readout of an existing record gives
> its recorded value with certainty under that same quantum probability rule.
> On a prepared domain where the records and fixed law uniquely determine this
> family, the quantum state may be represented by that reconstruction.

This avoids requiring a trace-class density matrix on an infinite tensor
product. Finite-region functionals have density matrices. The conditional
quantum state must be compatible with the actual existing records: any
permitted rereading of an existing record gives its content with certainty.
Compatibility and permanence are imposed on the record realization, not by
identifying an arbitrary content label in M2 with a density matrix.

### Record: add a physical encoding sentence

Old: no explicit identification of record readout with quantum pointers.
The current definite-content, one-record-per-site, permanence and unreadable-
absence sentences are retained verbatim.

Proposed addition:

> A record's readable value is encoded in a quantum pointer on allocated
> lattice sites and is reproduced with certainty by a permitted readout fixed
> for that pointer type, independently of the stored value.
> All sites used by that pointer and its readout controls are part of the
> physical register.

Consequently, k pointer qubits cannot hold more than 2^k distinct perfectly
readable values in one fixed readout. This is proved in RESULT.md rather than
assumed as a separate numerical capacity axiom. A symbolic real-valued matrix
label does not certify an exact infinite-precision one-qubit memory. The
construction's two-qubit empty/plus/minus pointer satisfies this condition.

### Admissibility: replace the governing two sentences

Old:

> There is one fixed neighborhood admissibility rule, covariant under lattice
> translations and proper cubic rotations.
>
> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the neighborhood conditions.

Proposed replacement:

> There is one fixed law for neighborhood quantum operations and record
> formation, covariant under lattice translations and proper cubic rotations.
> For fixed accessible record controls, each operation is a quantum instrument
> supported in its finite neighborhood and extended by the identity outside.
> On a finite outcome menu its outcome maps are linear and completely positive,
> and their sum preserves trace. On a standard Borel outcome space it is a
> countably additive completely-positive-map-valued measure with trace-preserving
> total map. Instrument controls depend only on readable record values obtained
> through permitted neighborhood interactions. Influence may pass
> through successive overlapping neighborhoods.
>
> For a specified record history used for conditioning, choose a finite region
> containing the operation's support and its conditional reduced density matrix.
> The probability of a measurable outcome event is the trace of the instrument
> map, extended by the identity on the rest of that region, applied to this
> matrix. A positive-probability event updates the matrix by this map followed
> by normalization. These updates agree under restriction and define the updated
> state family; reductions to other regions use a region also containing the
> operation's support. For exact outcomes in a continuous menu, conditional
> states are measurable versions of the almost-everywhere instrument-density
> conditionals, not ratios of zero singleton probabilities. The fixed law
> specifies those versions and which null histories, if any, lie in its domain.
> Joint probabilities are obtained by composing the instruments. A no-formation
> outcome may be included. A forming record locks a supported outcome through
> the law's fixed measurable content map. Each realized formation has one outcome;
> probabilities describe the law of those outcomes. Conditioning on a recorded
> content event uses the instrument on its full preimage under the content map.
> Every operation preserves all existing record contents.
>
> Conditioning on a record and physically receiving that record are distinct.
> Changing only the history used for conditioning does not change the realized
> operation or its controls.
> If the conditioning history does not fix the local controls, predictions
> average the joint conditional control-and-quantum-state ensemble, equivalently
> retaining the control register in the composed instrument.
> Predictions available in a neighborhood condition only on its available
> record history. Additional remote records may change conditional predictions,
> but cannot control a local operation until conveyed through permitted
> interactions. Ignoring an operation's outcome gives its trace-preserving
> sum, which leaves statistics outside its support unchanged.

RESULT.md section 8 proves the measurable-instrument density statement on
finite-dimensional carriers. A record's actual law is the pushforward through
the fixed content map; support refers to that law. This preserves the
distinction between zero singleton mass and being outside the support.
It does not imply that a finite pointer can store an exact continuum of
distinct perfectly readable outputs. Such experiments must account for their
actual register resources or use an explicitly specified finite readout.

## What the change does and does not select

The proposed probabilities are not arbitrary joint tables with local marginals.
Positivity on the joint quantum algebra, consistent effect probabilities and
local completely positive instruments exclude the polynomial control. They
imply the quantum CHSH upper bound for binary local measurements under the
usual common-preparation and independent-setting experiment. Entangled
preparation and suitable local measurements can attain it. Neither the
singlet nor a violation on every trial is forced by the amendment.

The existing Record clauses need no weakening for the exhibited local
absorbing instrument. What changes is the quantum information needed to
predict new records and the meaning of locality for those probabilities.
An unrestricted state may carry joint quantum information absent from its
record configuration; the two-qubit tomography witness proves why a list of
one-site marginals is insufficient. Complete prepared histories can instead
make the quantum state a derived predictor within a narrower domain.

The fixed law must still choose permitted instruments, physical couplings,
preparation, occurrence sites/rates and the realization of a measurement
apparatus. The construction supplies one such finite model; the amendment
does not specify a universal Hamiltonian, time metric, causal speed, Standard
Model, gravity, continuum limit or mass gap. The actual single-outcome rule
is adopted as stochastic formation, not explained by unitary premeasurement
or decoherence. Record permanence remains an ideal primitive of this project.

## Migration and adoption boundary

The old interpretive Admissibility notes and downstream paragraphs saying
joint quantum states, update laws and quantum probabilities are wholly absent
would need to be synchronized with precisely the approved new scope. Historical
accounts of what earlier axiom versions supplied must remain historical.
The axiom premise registry and owner-approval entry must be updated in the
same governed axiom change; old audit judgments must not be carried forward
as if the premise change were only wording. This is not automatic closure of
any downstream physical identification or existing audit.

This proposal is tested against a finite permanent-record process, the
full-history conditional collision, same-record state/history witnesses and
the preserved superquantum control. It is a defensible sufficient foundation
for the finite quantum models tested here, not a proof of minimality or the
unique correct ontology. The narrower alternative of adding only local
effect consistency is enough for the displayed two-wing bound but does not
by itself supply composition and general sequential quantum formation.
