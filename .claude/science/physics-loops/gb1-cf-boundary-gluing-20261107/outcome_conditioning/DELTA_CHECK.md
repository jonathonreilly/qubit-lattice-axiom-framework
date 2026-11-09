# Revised quantum formation unit: bounded delta check

Date: 2026-11-09. Research comparison, not a landing approval or audit verdict.
Requested profile: `gpt-6-astra`, effort `max`; backend attestation unavailable.
Baseline: `bf92a1d763030836ed55631d5d7a7ef3b288f284`.

**Finding:** the seven frozen sources identified below support a coherent,
reviewable quantum-formation proposal and a narrower conditional construction.
The previous six findings and the omitted-control conditioning issue are
resolved. No remaining defect was found in those checked arguments or in the
agreement of the proposed clauses. They do not yet prove that one finite
allocated model satisfies every proposed clause jointly; the remaining
obligation is stated below.

The owner's latest instruction is: "dont update the axiom until we prove the
change works". No adoption is recommended by this check. The supervisor reports
that the four governing files were restored to the pinned main/HEAD bytes,
with the candidates preserved only as non-governing snapshots, and that no
axiom commit, push or PR occurred. This check assigns no retention or audit
verdict. Pinned main remains the governing premise source.

## Scope actually examined

The revised research RESULT, ASSUMPTIONS and AXIOM_PROPOSAL and the complete
candidate canonical axiom memo were read. The actual registry, policy and
companion diffs against the baseline were read in full. The entire registry,
the policy's authority and dated-history context, and the companion's input
closure, relevant checks, purity-guard invocation, failure propagation and
exit logic were also inspected. Unchanged scientific proofs and exact-code
evidence reuse the frozen SOURCE_CHECK, with code/cache hashes refreshed.

During the check the RESULT status header first changed alone. Replacing that
header with the previously read header reproduced the earlier file's SHA-256
`d1204793cf72a4e6b6a3fc5ceaaedeb70ad074dd2e1395d98360737e875cbeaa`.
The subsequent omitted-control sentence in the proposal/canonical memo and
the RESULT witness were read fully. Removing exactly those additions recovers
the previously checked hashes `f3b1552e...`, `0004c044...` and `a32d6ee2...`,
respectively. The final snapshot hashes were verified against their mapping.
No revised mathematical text was covered merely by a summary or filename.

## Resolution of previous findings

| Finding | Revised evidence and conclusion |
|---|---|
| Bob's conditional state had an overbroad antecedent | RESULT section 4 now explicitly requires A formed and B still unformed, before B's outcome. The singlet expression is correct on that domain; it is no longer asserted after both measurements. |
| Numerical order fixture differs from the equal-mass hand witness | RESULT section 5 now explicitly identifies the code's `|0><0|` input and says it checks the final states/future odds, not the equal-prefix-mass `I/2` fixture. Both variants remain correct; no rerun is needed to substantiate this disclosure. |
| Capacity theorem needs one decoder independent of stored value | Proposal and canonical Record text now require a permitted readout fixed for its pointer type independently of its stored value, and count both pointer and readout-control sites. ASSUMPTIONS C4 names the same condition. The previously checked orthogonal-support capacity proof now binds to that wording. |
| Infinite state family versus an unspecified global trace; fixed controls versus changed conditioning | Proposal and canonical Admissibility use reduced density matrices on finite regions containing the operation support, identity extension and compatible reductions. They explicitly say that changing only conditioning history does not change the realized operation or controls. No global trace-class density is assumed. |
| Almost-everywhere posterior versus pointwise law; measurable content map | Proposal, canonical text, RESULT section 8 and ASSUMPTIONS M1 explicitly require measurable versions, a declared null-history domain and a measurable content map. They do not claim that RN determines a unique posterior at every supported singleton. |
| Coarse recorded content must condition the whole instrument | Proposal and canonical text use the full content-map preimage. RESULT gives `K(C)=I(c^{-1}(C))` and the equal-weight `|0>`, `|1>` example yielding `I/2` for their shared recorded content. A hidden fine outcome is not silently used as the record-conditioned state. |

## Clause agreement and coherence

After removing Markdown quote markers and normalizing whitespace, each of
the four proposed new blocks occurs exactly in its corresponding candidate
canonical section: Qubit composition, Qualification state description,
Record pointer/readout, and Admissibility instrument/conditioning. This is
an exact text comparison, not merely similar terminology. The Lattice block
is byte-identical to the baseline. The original Record permanence,
one-record-per-site, content-only readout and unreadable-absence sentences
are preserved; the pointer requirements are additions.

The finite-region update is well typed. Given consistent initial reductions
and a fixed local CP event map, extending that map by identity commutes with
tracing out factors outside its support. Event probabilities therefore agree
across containing regions, and normalized positive-event updates give a
consistent state family. Regions not containing the operation are obtained
by reduction from a containing region, as the text now specifies. Selective
remote conditioning can change those reductions; the nonselective
trace-preserving map leaves exterior statistics unchanged. These are
compatible statements about the same operation.

The final omitted-control clarification is necessary when a conditioning
history does not fix a control correlated with the quantum state. For a
classical control C and history h, the correct event probability is

    p(E|h) = sum_c p(c|h) tr I_E^c(rho_{h,c}).

The reduced quantum posterior numerator is the same sum with the trace omitted.
Equivalently, retain the classical control blocks in the joint state and use
one controlled instrument. A fair C, state `|C>` and measurement Z for C=0 or
-Z for C=1 give `p(+)=1`; either fixed measurement on the averaged `I/2` gives
`1/2`. The new RESULT witness proves exactly that point. The added canonical
and proposed sentences agree, preserve the actual operation, and avoid
confusing less informative conditioning with physically changing a control.

The measurable-instrument extension and pointer-capacity limitation remain
distinct. The former defines outcome laws and conditional states on finite
quantum carriers; the latter prevents arbitrary exact continuum storage in
a finite perfectly readable pointer. Measurable content coarsening handles
finite recorded readouts without importing a hidden fine-outcome predictor.
The general state may contain predictive quantum information beyond records;
the record-only reconstruction is explicitly restricted to sufficient
preparation/history domains. No unrestricted reconstruction theorem is claimed.

The stochastic single-outcome rule is expressly supplied. The research model
continues to distinguish its local two-site pointer writes from a distant
atomic pair, and its six-site dynamic carrier from complete apparatus,
source, reservoir and repeated-trial resources. Mathematical locality of the
CP maps is not advertised as a derived microscopic actuator or a solution
of arbitrary fundamental dynamics. The revised scope introduces no such
false physical implication.

## Joint-model obligation still open

The finite absorbing construction is a conditional model with the following
proved core: native-qubit tensor factors, a normalized CP instrument on all
input matrices and passive references, an absorbing pointer sector, permanent
branch records, one-wing intermediate histories, a state-independent occurrence
hazard, the quantum Bell law, and no change of exterior statistics under a
nonselective local operation. Its pointer code has a fixed perfectly
distinguishable readout, and the prepared branches support its stated content
dictionary. These checks remain valid.

It is **not yet an exhibited joint model of every proposed clause**. RESULT
and ASSUMPTIONS explicitly supply preparation, calibration, local controls,
activation and readout/registration. The six-site count excludes their
registers. A family indexed by external settings and activation is not itself
an explicit finite record-controlled implementation of that family. In
particular the checked unit does not specify all of the following together:

1. A declared preparation domain and a finite allocation of setting/activation
   and readout controls, with their permanent record contents and compatible
   quantum state. Any invoked source/apparatus resources must also be counted.
2. One permitted local rule controlled only by those readable values, with
   fixed pointer decoding and a stated domain that does not make absence of
   a record readable. It must preserve every previously existing record,
   including controller and apparatus records, under the full permitted
   operation set.
3. The state/record registration interpretation at every legal intermediate
   history, including no-formation and null-history domain choices, and the
   same law under the required lattice translations and rotations. The
   displayed covariance of supplied apparatus data is correct; it does not
   by itself provide their allocation or synthesis.

These are bounded completion checks for one benchmark, not a demonstrated
contradiction. They do not require a laboratory actuator, a complete theory of
fundamental dynamics, or derivation of unique actualization from unitary
evolution. The candidate expressly supplies a stochastic single-outcome rule.
A prepared singlet may be a declared initial state; there is no additional
demand to produce it from a record-free vacuum.
A finite CHSH benchmark can use a finite setting menu; it need not implement
every continuous instrument allowed by the proposal. The measurable-instrument
theorem remains a separate formal extension, not continuum storage hardware.
Thus the present evidence supports further research on this candidate, not
foundation adoption under the owner's latest condition. No guard PASS can
discharge this joint-model obligation.

## Policy, registry and companion boundaries

The owner's earlier instruction to update the axiom as needed to select or
represent quantum physics authorized preparation of the substantive candidate.
The frozen policy addition records that earlier scope and distinguishes it
from independent validation or an audit verdict. The owner's later instruction
withholds an axiom update until the change is proved to work and controls the
present disposition. The snapshot is evidence of candidate wording, not an
active authorization to change the foundation. It does not purport to derive
quantum mechanics from the older foundation or to make a wording-only migration.

The registry diff changes only `nodes.minimal_axioms.note`: after removing
that field from the before/after parsed JSON, the objects are identical.
Canonical IDs, source paths, aliases, legacy IDs, schema and all three other
primitive nodes are unchanged. The new note agrees with the canonical
composition/state/instrument/readout scope, retains specific physical choices
as downstream content, and explicitly disclaims retained-status promotion.
No audit verdict or ledger field is edited in this unit.

The policy's sole diff is the new owner-authorization entry. Its disallowed
ordinary-lane axiom changes, approval requirements and prohibition on using
policy as a scientific premise remain unchanged. Old record-only state and
no-probability statements occur inside explicitly dated historical approval
entries; those are not asserted as the new governing state/probability rule.
The canonical memo separately labels its pre-revision comparison bullets as
historical and removes the stale exclusions from its active dynamics/open-gate
paragraphs. No stale active record-only state sentence remains in the reviewed
canonical qualification or registry note.

The snapshot's canonical header and policy approval entry were written for a
potential source amendment. They must not be cited as current adopted status:
the enclosing snapshot status and latest owner instruction explicitly prevent
that reading. This is a status boundary, not a change to the mathematical text.

The companion updates its old distribution/state needles to the substantive
new quantum clauses. It adds checks for CP normalization, finite-region
conditioning, measurable outcomes, null-history versions, content-map preimages,
fixed pointer decoding, control/readout resources and owner authorization.
The classical toy menu and partial toy state are now labelled as such, without
claiming they derive quantum structure or establish full-state sufficiency.

Source comparison confirms that the companion's complete `AUDIT_INPUT_PATHS`
closure, purity-guard subprocess call and return-code check, and `main()`
failure/exit propagation are unchanged. The stable-node/alias, retired
additive-`I`, no-laundering and independent-status boundaries are not removed
by the inspected diff. Replacing the superseded full-neighborhood-odds needle
is the declared premise change, not disabling the purity guard. These remain
source/notation checks; passing them would not be proof of the quantum model.

No companion, purity guard, numerical diagnostic or pipeline was executed by
this worker. Their execution status is not certified by this delta check.
No repository-wide dependent-proof migration or validation was performed.
An unchanged ledger, or absence of current audited rows, would not establish
that the proposed foundational change has no downstream impact.

## Exact source identities and recovery

Research base:
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/outcome_conditioning/`.

Non-governing candidate snapshot base, relative to the research base:
`proposal_review/candidate_sources/`.
`proposal_review/CANDIDATE_SNAPSHOTS.json` maps the original axiom-worktree
paths to these preserved copies. `proposal_review/candidate.patch` preserves
the original proposed source diff. The following axiom/policy/registry/companion
identities refer to snapshots, not the now-restored governing paths.

| Reviewed source | Final SHA-256 |
|---|---|
| Research `RESULT.md` | `1d359c695e04012f2f8b4737e4404b2cc992a09bf2402c7739a4ea38ca49cc2f` |
| Research `ASSUMPTIONS.md` | `97ee3285e305396b0b1b4565c1d76013c14edcdfd2e1e09e040d18283d00f869` |
| Research `AXIOM_PROPOSAL.md` | `8114435616610a8f2a217ec44e582cf76ad37522a9f0397997798a86854b4811` |
| Snapshot `docs/MINIMAL_AXIOMS_2026-06-29.md` | `146b803b105b8d558f8ea97db8c11a23be7b12b7a8479a1ab7446553b79a4642` |
| Snapshot `docs/audit/AXIOM_MINIMALITY_POLICY.md` | `ebd5519f1ec8359ad4b2bdcf69ea21b23d8f8ca6b285a01847625558ff22c40b` |
| Snapshot `docs/audit/data/axiom_premise_nodes.json` | `cf66d44d0fc1839e8a6670275d62e8dce6ffc038c40b40a2ff255c620fe54c8c` |
| Snapshot `scripts/audit_companion_minimal_axioms_clean_base_exact.py` | `c0f006558c1e9392fe592a45e1dcff1885c5cc327c2b673d0059559d0b8f3c67` |

The unchanged research code and cache retain the identities in SOURCE_CHECK:
`check.py` is `46127f2c9050de484dc444e5a3543a9d9aa8d93072d65c34ec33ecc9f1d9e0d0`;
`outputs/exact.stdout` is
`663852ae828eb236c753d869e85e630f9cd7a7da3e3b8b83fdd1533b6a3c6c6e`.
The earlier reports remain separate evidence:
`INDEPENDENT.md` is
`1eea23f7ba75a9b269eb40b2667cf3a54002eecdd56396a5e4eefdc01b9ec999`;
`SOURCE_CHECK.md` is
`41b5161c00f313d2588f0e2935c10ac6c717d01b12932c02476c2abc814cf232`.

Only this DELTA_CHECK.md is written. No source modification, numerical job,
commit, push, audit-status change, merge or landing action is taken. The note
and final input hashes are read back before handoff. Further changes require
review of the affected content at new identities; this conclusion covers
only the unit recorded here.
