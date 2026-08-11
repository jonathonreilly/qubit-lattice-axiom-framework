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
instance, embed the two output labels as the `M_2(C)` possibilities
`P_0=diag(1,0)` and `P_1=diag(0,1)`. For each fixed representative `g` and
target-input parameter `x`, define the deterministic local distribution
`mu_(g,x)(P_y|n)=1`, where `y=L_g(x,n)`. Conditional on a record forming at the
target, Record then locks the unique supported possibility `P_y`.

Within this explicit finite point-mass construction, every one-neighbour
configuration edge on which any of the three dependence classes changes its
Boolean output locks different target content. The additive scalar readout

```text
I_one(R) = number of records in R whose locked content is P_1
```

is determined by record content alone, has `I_one(empty)=0`, is additive on
finite pairwise-disjoint record collections, and separates every such
single-target pair. This is a single-site, conditional-on-formation theorem
of the declared construction. It does not derive that the construction is the
framework's one physical admissibility rule, is not a mosaic-wide theorem,
and does not select the framework's physical readout.

## Declared finite instance

The target is `C=(0,0,0)` and its six neighbour conditions are the signed unit
directions `(+x,-x,+y,-y,+z,-z)`. Target input and every neighbour bit lie in
`{0,1}`. For each table, `x` is fixed as a supplied parameter, so the displayed
neighbour condition `n` determines the point-mass distribution. The three
representative laws and their proper-cubic orbit data are

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
present, locks one admissible local possibility. This packet constructs two
such possibilities inside the supplied one-site algebra,

```text
P_0 = [[1,0],[0,0]],    P_1 = [[0,0],[0,1]],
mu_(g,x)(P_y|n)=1,      mu_(g,x)(P_(1-y)|n)=0.
```

Thus `P_y` is the unique supported possibility and, conditional on formation,
the locked content in this construction. This is a declared embedding and
point-mass law, not a derivation of a unique physical basis or of the
framework's one global admissibility rule. All five neighbour bits not
displayed in a CNOT row, and all four not displayed in a TOF row, are arbitrary
Boolean spectators in the finite fixture.

### Incoming CNOT class (`J=1`, multiplicity 6)

| `n_(+x)` | locked content for `x=0` | locked content for `x=1` |
|---:|---:|---:|
| 0 | `P_0` | `P_1` |
| 1 | `P_1` | `P_0` |

For either target input, toggling the control `0 <-> 1` changes the locked
content.

### Perpendicular-control TOF class (`J=2`, multiplicity 12)

| `(n_(+x),n_(+y))` | locked content for `x=0` | locked content for `x=1` |
|---|---:|---:|
| `(0,0)` | `P_0` | `P_1` |
| `(0,1)` | `P_0` | `P_1` |
| `(1,0)` | `P_0` | `P_1` |
| `(1,1)` | `P_1` | `P_0` |

The separated one-bit pairs are `(0,1) <-> (1,1)` when `+x` is toggled and
`(1,0) <-> (1,1)` when `+y` is toggled, for either target input. Toggling a
control while the other control is zero does not separate the law.

### Opposite-control TOF class (`J=0`, multiplicity 3)

| `(n_(+x),n_(-x))` | locked content for `x=0` | locked content for `x=1` |
|---|---:|---:|
| `(0,0)` | `P_0` | `P_1` |
| `(0,1)` | `P_0` | `P_1` |
| `(1,0)` | `P_0` | `P_1` |
| `(1,1)` | `P_1` | `P_0` |

The separated one-bit pairs are again `(0,1) <-> (1,1)` and
`(1,0) <-> (1,1)`, now for the opposite controls, for either target input.

Across the three representatives there are ten target-input-resolved
one-neighbour-bit changing rows: two CNOT rows and four rows for each TOF
class. Every one flips locked content `P_0 <-> P_1`. The runners also enumerate
the non-changing Hamming edges rather than defining the census by preselecting
unequal outputs.

## B_READOUT_VISIBILITY

### Declared readout family

For this two-possibility content census, declare the complete additive scalar
family

```text
F_bin = {phi:{P_0,P_1}->R},
I_phi(R) = sum over records r in R of phi(content(r)).
```

Every `I_phi` is determined by record content alone. The empty sum gives
`I_phi(empty)=0`, and splitting a finite record collection into pairwise-
disjoint subcollections splits the sum, so additivity is exact. Conversely,
within the declared two-point content alphabet, every additive content-only
scalar readout is fixed by its two singleton values `phi(P_0)` and `phi(P_1)`. Thus
`delta_0=(1,0)` and `delta_1=(0,1)` form a basis for the declared family.

### Exact separator

Choose `phi(P_0)=0`, `phi(P_1)=1`. Then

```text
I_one({target record}) = y when its locked content is P_y.
```

Every separated pair in the census changes `I_one` by `+1` or `-1`. Hence
some admissible readout sees every locked-content difference in section A.
The primary exhausts the two basis readouts and checks finite additivity on
450 ordered disjoint-content-list pairs; there are zero failures.

The existence statement is not universal over readouts. For example,
`phi(P_0)=phi(P_1)=1` gives record count, which is admissible and blind to the
content change between equal-size singleton collections. The axiom licenses
`I_one`; it does not select it or require the unspecified fixed physical
readout to be content-faithful.

The outcome-neutral bookkeeping path is exercised without shipping a negative
science claim: on a synthetic equal-content fixture, both basis functionals
agree and the full top-level B/R2 validators accept the report
`DECLARED_READOUT_FAMILY_AGREES_ON_ALL_COMPARED_PAIRS`. Thus a content-blind
finding would pass the same integrity gates as the positive result found here.

## C_SCOPE

What is established is a bounded observable consequence inside the **declared
finite point-mass construction**: for each fixed `(g,x)` conditioned law,
changing a neighbour along one of the enumerated changing edges changes the
unique supported `M_2(C)` possibility, Record locks that possibility if a
record forms, and `I_one` reads the difference.

The generic axiom sentence by itself is weaker. Variation of a probability
distribution need not give disjoint supports or force a different realized
draw. This packet also treats the 21 transported programs and the two fixed
target-input values as alternative finite conditioned laws; it does not prove
that they assemble into the framework's one fixed, simultaneous,
translation-uniform admissibility rule. Therefore the packet does not claim
that every admissibility law or every record realization changes content. It
also does not establish any of the following:

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
requires deterministic equality. It enumerates the 24 proper cubic rotations,
orbits, stabilizers, every control-hypercube Hamming edge, both point-mass
normalizations, and support membership. Its integrity checks reconcile counts
and construction; they do not require a positive visibility headline. The
same top-level validator accepts the coherent family-agreement fixture.

The independent checker reads exactly three files: primary source as AST,
primary receipt, and primary cache. It neither imports nor executes the
primary. A separate gate-permutation reconstruction reproduces all ten table
rows and all target-input-resolved Hamming edges. Its proper-cubic group is
built independently from oriented right-handed frames, reproducing the
`6/12/3` orbits, `4/2/8` stabilizers, and `J=(1,2,0)` without copying those
values as expectations. A dual-basis calculation independently proves the
readout claim. Six active corruptions—locked content, `J`, visibility outcome,
mosaic scope through the actual scope validator, primary source through the
actual AST pin validator, and cached headline—are all rejected.

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
| `minimal_axioms` | zero-input structural | supplies true-`Z^3` neighbours, `M_2(C)` possibility domain, conditional record locking, and content-only additive scalar readout | used directly |
| `P_0/P_1` embedding | explicit finite construction | embeds the two Boolean labels as diagonal `M_2(C)` possibilities | declared and checked; no unique physical basis claimed |
| point-mass laws `mu_(g,x)` | explicit finite construction | makes `P_y` the unique supported possibility for each fixed `(g,x,n)` | normalized and support-checked; not promoted to one global physical rule |
| fixed target input `x` | explicit conditioning parameter | makes each `mu_(g,x)` a neighbour-determined map | both values enumerated separately; no extra varying site condition hidden |
| three deterministic target-law classes | explicit finite boundary condition | defines the output maps and proper-cubic orbits being tested | reconstructed in both runners; alternative laws, not simultaneous assembly |
| single forming target | explicit conditioning | isolates record content from formation location/rate | no formation rule inferred |
| `F_bin` | declared readout family | asks existence over every additive scalar binary-content assignment | no claim of physical selection |

No observed value, fitted selector, probability weighting, normalization
rule, literature value, new axiom, or new approved primitive is load-bearing.

## Proof-obligation graph

1. **Content obligation — discharged for the declared construction.** Embed
   `P_0/P_1` in `M_2(C)`, construct normalized point-mass distributions,
   verify `P_y` is their unique support point, enumerate every control
   configuration and both fixed target-input parameters, and apply Record
   conditional on formation.
2. **Class obligation — discharged at the finite cap.** Recompute the
   proper-cubic group, `6/12/3` multiplicities, `4/2/8` stabilizers, and
   `J=(1,2,0)` representatives by independent group constructions.
3. **Readout-family obligation — discharged for `F_bin`.** Show that singleton
   values determine every content-only additive scalar readout and that
   `delta_0,delta_1` span the family.
4. **Separation obligation — discharged.** Evaluate `I_one` on every separated
   content pair and obtain nonzero difference.
5. **Scope obligation — discharged.** Keep formation rules, physical-readout
   selection, global-law assembly, probability weights beyond the constructed
   point masses, continuous content, and mosaic-wide claims outside the result.

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
conditional_surface_status: "exact for the declared P0/P1 embedding and finite point-mass conditioned laws on the binary radius-one single-target family, conditional on record formation"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite constructed point-mass witness cap and declared readout-family existence; no global physical admissibility rule, physical-readout selection, or mosaic theorem"
claim_type_reason: "exact exhaustive supported-content census and readout separation in the declared finite M2(C) point-mass construction"
audit_required_before_effective_retained: true
bare_retained_allowed: false
audit_status_authority: independent audit lane only
negative_assertion_classes: []
packet_primary_runner: scripts/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.py
packet_helper_runner: scripts/frontier_cycle985_neighbour_dependence_record_content_independent_check_2026_08_11.py
packet_helper_claim_scope: cycle985_neighbour_dependence_record_content
review_loop_disposition: pass
```
