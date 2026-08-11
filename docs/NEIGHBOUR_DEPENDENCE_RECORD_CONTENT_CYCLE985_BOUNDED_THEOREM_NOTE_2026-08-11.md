# Neighbour-dependence changes locked record content on the finite binary star

Date: 2026-08-11

Cycle: 985

Claim type: `bounded_theorem`

Actual current surface: `bounded-support`

Audit-status authority: independent audit lane only

Effective status: pipeline-derived only after independent audit ratification
and dependency closure

Constitutional effect: none. This packet edits no axiom, approved primitive,
premise registry, audit verdict, queue, ledger, or effective-status surface.

## Artifact map

Primary runner:

- [`frontier_cycle985_neighbour_dependence_record_content_2026_08_11.py`](../scripts/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.py)

Independent refutation checker:

- [`frontier_cycle985_neighbour_dependence_record_content_independent_check_2026_08_11.py`](../scripts/frontier_cycle985_neighbour_dependence_record_content_independent_check_2026_08_11.py)

Pinned caches:

- [`frontier_cycle985_neighbour_dependence_record_content_2026_08_11.txt`](../logs/runner-cache/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.txt)
- [`frontier_cycle985_neighbour_dependence_record_content_independent_check_2026_08_11.txt`](../logs/runner-cache/frontier_cycle985_neighbour_dependence_record_content_independent_check_2026_08_11.txt)

Receipts:

- [`neighbour_dependence_record_content_cycle985_receipt_2026_08_11.json`](../outputs/neighbour_dependence_record_content_cycle985_receipt_2026_08_11.json)
- [`neighbour_dependence_record_content_cycle985_independent_check_receipt_2026_08_11.json`](../outputs/neighbour_dependence_record_content_cycle985_independent_check_receipt_2026_08_11.json)

The restricted independent-audit packet must contain the refutation checker:

```text
neighbour_dependence_record_content_cycle985_bounded_theorem_note_2026-08-11:
  scripts/frontier_cycle985_neighbour_dependence_record_content_independent_check_2026_08_11.py
```

## Exact target claim

On the declared binary, radius-one true-`Z^3`, word-length-at-most-one target
instance, conditional on a record forming at the target, every one-neighbour
configuration pair separated by any of the three deterministic dependence
classes locks different target content. The additive scalar readout

```text
I_one(R) = number of records in R whose locked content is 1
```

is determined by record content alone, has `I_one(empty)=0`, is additive on
finite pairwise-disjoint record collections, and separates every such
single-target pair. This is a single-site, conditional-on-formation result.
It is not a mosaic-wide theorem and does not select the framework's physical
readout.

## Declared finite instance

The target is `C=(0,0,0)` and its six neighbour conditions are the signed unit
directions `(+x,-x,+y,-y,+z,-z)`. Target input and every neighbour bit lie in
`{0,1}`. The three representative laws and their proper-cubic orbit data are

| class | representative | target law | multiplicity | stabilizer | `J=||sum controls||^2` |
|---|---|---|---:|---:|---:|
| incoming CNOT | `CNOT(+x->C)` | `y=x XOR n_(+x)` | 6 | 4 | 1 |
| perpendicular-control TOF | `TOF(+x,+y->C)` | `y=x XOR (n_(+x) AND n_(+y))` | 12 | 2 | 2 |
| opposite-control TOF | `TOF(+x,-x->C)` | `y=x XOR (n_(+x) AND n_(-x))` | 3 | 8 | 0 |

The runner reconstructs these laws directly. PRs #6087, #6111, #6113,
#6115, #6106, and #6116 are task-supplied provenance only; none of their
notes, runners, caches, receipts, or verdict fields is read or executed.

## A_LOCKED_CONTENT_CENSUS

The [`Record axiom`](MINIMAL_AXIOMS_2026-06-29.md) says that a record, when
present, locks one admissible local possibility. In this binary deterministic
instance that possibility is the target output `y`. All five neighbour bits
not displayed in a CNOT row, and all four not displayed in a TOF row, are
arbitrary spectators.

### Incoming CNOT class (`J=1`, multiplicity 6)

| `n_(+x)` | locked content for `x=0` | locked content for `x=1` |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 1 | 0 |

For either target input, toggling the control `0 <-> 1` changes the locked
content.

### Perpendicular-control TOF class (`J=2`, multiplicity 12)

| `(n_(+x),n_(+y))` | locked content for `x=0` | locked content for `x=1` |
|---|---:|---:|
| `(0,0)` | 0 | 1 |
| `(0,1)` | 0 | 1 |
| `(1,0)` | 0 | 1 |
| `(1,1)` | 1 | 0 |

The separated one-bit pairs are `(0,1) <-> (1,1)` when `+x` is toggled and
`(1,0) <-> (1,1)` when `+y` is toggled, for either target input. Toggling a
control while the other control is zero does not separate the law.

### Opposite-control TOF class (`J=0`, multiplicity 3)

| `(n_(+x),n_(-x))` | locked content for `x=0` | locked content for `x=1` |
|---|---:|---:|
| `(0,0)` | 0 | 1 |
| `(0,1)` | 0 | 1 |
| `(1,0)` | 0 | 1 |
| `(1,1)` | 1 | 0 |

The separated one-bit pairs are again `(0,1) <-> (1,1)` and
`(1,0) <-> (1,1)`, now for the opposite controls, for either target input.

Across the three representatives there are ten target-input-resolved
one-neighbour-bit separation rows: two CNOT rows and four rows for each TOF
class. Every one flips locked content `0 <-> 1`.

## B_READOUT_VISIBILITY

### Declared readout family

For this binary content census, declare the complete additive scalar family

```text
F_bin = {phi:{0,1}->R},
I_phi(R) = sum over records r in R of phi(content(r)).
```

Every `I_phi` is determined by record content alone. The empty sum gives
`I_phi(empty)=0`, and splitting a finite record collection into pairwise-
disjoint subcollections splits the sum, so additivity is exact. Conversely,
within the binary alphabet, every additive content-only scalar readout is
fixed by its two singleton values `phi(0)` and `phi(1)`. Thus
`delta_0=(1,0)` and `delta_1=(0,1)` form a basis for the declared family.

### Exact separator

Choose `phi(0)=0`, `phi(1)=1`. Then

```text
I_one({target record}) = locked target content.
```

Every separated pair in the census changes `I_one` by `+1` or `-1`. Hence
some admissible readout sees every locked-content difference in section A.
The primary exhausts the two basis readouts and checks finite additivity on
450 ordered disjoint-content-list pairs; there are zero failures.

The existence statement is not universal over readouts. For example,
`phi(0)=phi(1)=1` gives record count, which is admissible and blind to the
content change between equal-size singleton collections. The axiom licenses
`I_one`; it does not select it or require the unspecified fixed physical
readout to be content-faithful.

For completeness, no separator exists in `F_bin` for a compared singleton
pair exactly when the two locked contents are equal: both basis functionals
then agree, so every linear combination agrees. The runner's outcome-neutral
visibility validator accepts a coherent equal-content/no-separator fixture.
Therefore a negative result would pass the same bookkeeping gate as the
positive result found here.

## C_SCOPE

What is established is a bounded observable consequence of the **declared
deterministic realization** of the axiom's neighbour clause together with the
Record locking/readout discipline: at one forming target record, separated
neighbour configurations change locked binary content, and `I_one` reads the
difference.

The generic axiom sentence by itself is weaker. Variation of a probability
distribution need not give disjoint supports or force a different realized
draw, so this packet does not claim that every admissibility law or every
record realization changes content. It also does not establish any of the
following:

- a selected physical readout or visibility to every admissible readout;
- a formation site, formation probability, formation rate, or production
  dynamics;
- a Born weighting or a weighting preference;
- a multi-record correlation, full record-mosaic statistic, or lattice-wide
  observable;
- a continuous-`M_2(C)` probability law; or
- one simultaneous translation-uniform law on the infinite lattice.

No mosaic-level conclusion is inferred from the single-target tables.

## D_CONTROLS and independent refutation

The primary reads one explicit source: the live axiom memo, pinned by SHA-256
and Git blob. It imports and executes no prior-cycle module. It derives all
three truth tables, `J` values, separations, and readout values twice and
requires deterministic equality. Its integrity checks reconcile declared
counts and construction; they do not require a positive visibility headline.
The same validator accepts a coherent no-separator fixture.

The independent checker reads exactly three files: primary source as AST,
primary receipt, and primary cache. It neither imports nor executes the
primary. A separate gate-permutation reconstruction reproduces all ten table
rows, all ten target-input-resolved separation rows, the `6/12/3` class data,
and `J=(1,2,0)`. A dual-basis calculation independently proves the readout
claim. Six active corruptions—locked content, `J`, visibility outcome, mosaic
scope, source pin, and cached headline—are all rejected.

Canonical cached results are:

```text
A_LOCKED_CONTENT_CENSUS PASS
B_READOUT_VISIBILITY PASS
C_SCOPE PASS
D_CONTROLS PASS
TOTAL: PASS=4 FAIL=0

R0_PRIMARY_AST_AND_PINS PASS
R1_INDEPENDENT_CONTENT_CENSUS PASS
R2_INDEPENDENT_READOUT_DUAL PASS
R3_RECEIPT_CACHE_BINDING PASS
R4_ACTIVE_CORRUPTION_PROBES PASS
R5_CONTROLS PASS
VERDICT: PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT
TOTAL: PASS=6 FAIL=0
```

## Assumptions and imports

| item | class | load-bearing role | disposition |
|---|---|---|---|
| `minimal_axioms` | zero-input structural | supplies true-`Z^3` neighbours and conditional record locking plus content-only additive scalar readout | used directly |
| binary content alphabet | explicit finite boundary condition | makes every local content and readout basis enumerable | declared, not extrapolated to continuous `M_2(C)` |
| three deterministic target laws | explicit finite boundary condition | defines the content maps being tested | reconstructed in both runners |
| single forming target | explicit conditioning | isolates record content from formation location/rate | no formation rule inferred |
| `F_bin` | declared readout family | asks existence over every additive scalar binary-content assignment | no claim of physical selection |

No observed value, fitted selector, probability weighting, normalization
rule, literature value, new axiom, or new approved primitive is load-bearing.

## Proof-obligation graph

1. **Content obligation — discharged at the finite cap.** Enumerate every
   relevant control configuration and both target inputs under each target
   law; apply Record conditional on formation.
2. **Class obligation — discharged at the finite cap.** Recompute the
   `6/12/3` multiplicities, stabilizers, and `J=(1,2,0)` representatives.
3. **Readout-family obligation — discharged for `F_bin`.** Show that singleton
   values determine every content-only additive scalar readout and that
   `delta_0,delta_1` span the family.
4. **Separation obligation — discharged.** Evaluate `I_one` on every separated
   content pair and obtain nonzero difference.
5. **Scope obligation — discharged.** Keep formation rules, physical-readout
   selection, probability weights, continuous content, and mosaic-wide claims
   outside the result.

## Trace gate and status fields

```yaml
trace_class: direct_blocker_closure
reachability_to_target: closes
target_claim_id: null
target_blocker_text: "for a site that forms a record, do neighbour configurations separated by the finite dependence law lock different content, and can some Record-admissible additive content-only readout see it?"
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "submit the finite single-site content/readout theorem and paired refutation checker to independent audit; do not extrapolate to a selected physical readout or mosaic-wide observable"
claim_id: cycle985_neighbour_dependence_record_content
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: bounded-support
conditional_surface_status: "exact on the declared binary, radius-one, deterministic single-target witness family conditional on record formation"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite binary deterministic witness cap and declared readout-family existence; no continuous law, physical-readout selection, or mosaic theorem"
claim_type_reason: "exact exhaustive content census and readout separation on the declared finite instance"
audit_required_before_effective_retained: true
bare_retained_allowed: false
audit_status_authority: independent audit lane only
negative_assertion_classes: []
packet_primary_runner: scripts/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.py
packet_helper_runner: scripts/frontier_cycle985_neighbour_dependence_record_content_independent_check_2026_08_11.py
packet_helper_claim_scope: cycle985_neighbour_dependence_record_content
review_loop_disposition: pending
```
