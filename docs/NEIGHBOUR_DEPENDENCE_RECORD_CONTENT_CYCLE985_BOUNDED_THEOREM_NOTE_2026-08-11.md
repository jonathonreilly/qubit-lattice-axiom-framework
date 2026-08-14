# Conditional locked-content separation in declared binary point-mass laws

Date: 2026-08-11

Cycle: 985

Claim type: `bounded_theorem`

Actual current surface: `bounded support theorem`

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
Boolean output locks different target content, conditional on formation.
Separately declare the non-axiom single-record separator

```text
r_one(P_0)=0,    r_one(P_1)=1.
```

It is a real-valued function of the declared content and separates every such
single-target pair. Its optional declared finite-collection extension

```text
I_one(R) = number of records in R whose locked content is P_1
```

has `I_one(empty)=0` and is additive on finite pairwise-disjoint record
collections by construction. Those collection properties are extra declared
structure, not Record axiom content. This is a single-site,
conditional-on-formation theorem of the declared construction. The
framework's one physical admissibility rule, a mosaic-wide extension, and the
physical readout all remain outside the quantified claim.

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

## B_DECLARED_SEPARATOR

### Declared non-axiom readout family

For this two-possibility content census, declare the complete additive scalar
family

```text
F_bin = {phi:{P_0,P_1}->R},
I_phi(R) = sum over records r in R of phi(content(r)).
```

Every `I_phi` is determined by record content alone by its declared formula.
The empty sum gives `I_phi(empty)=0`, and splitting a finite record collection
into pairwise-disjoint subcollections splits the sum, so additivity is exact
inside this extra construction. Neither the scalar codomain, the family, the
collection extension, finite additivity, nor the empty value is supplied by
Record. Within the declared family, singleton values fix a functional and
`delta_0=(1,0)`, `delta_1=(0,1)` form a basis.

### Exact separator

Choose `phi(P_0)=0`, `phi(P_1)=1`. Then

```text
I_one({target record}) = y when its locked content is P_y.
```

Every separated pair in the census changes `I_one` by `+1` or `-1`. Hence the
declared separator sees every locked-content difference in section A.
The primary exhausts the two basis readouts and checks finite additivity on
450 ordered disjoint-content-list pairs; there are zero failures.

The construction is not universal over readouts. For example,
`phi(P_0)=phi(P_1)=1` gives record count and is blind to the content change
between equal-size singleton collections. Record requires an actual readout
value to depend on content alone; it supplies neither the existence of this
declared family nor a selection of `I_one` as the physical readout.

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

The theorem is conditioned on the declared point masses. General varying
distributions, including overlapping-support laws and their realized draws,
are outside its domain. This packet also treats the 21 transported programs
and the two fixed target-input values as alternative finite conditioned laws;
assembly into the framework's one fixed, simultaneous, translation-uniform
admissibility rule is an open dependency. The following are likewise outside
the result:

- a selected physical readout or visibility to every content-only readout;
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

The independent checker reads exactly five files: the current axiom memo, the
narrowed note, primary source as AST, primary receipt, and primary cache. It
neither imports nor executes the primary. A separate gate-permutation
reconstruction reproduces all ten table
rows and all target-input-resolved Hamming edges. Its proper-cubic group is
built independently from oriented right-handed frames, reproducing the
`6/12/3` orbits, `4/2/8` stabilizers, and `J=(1,2,0)` without copying those
values as expectations. A dual-basis calculation independently proves the
declared-functional claim. Active corruptions cover locked content, `J`,
separator outcome, mosaic scope, current Record non-use, note/source pins, and
cached headline; all are rejected.

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
| `minimal_axioms` | zero-input structural | supplies true-`Z^3` neighbours, the `M_2(C)` possibility domain, neighbour-dependent distributions, and conditional locking of one supported possibility | used directly; supplies no scalar/additive collection readout |
| `P_0/P_1` embedding | explicit finite construction | embeds the two Boolean labels as diagonal `M_2(C)` possibilities | declared and checked; no unique physical basis claimed |
| point-mass laws `mu_(g,x)` | explicit finite construction | makes `P_y` the unique supported possibility for each fixed `(g,x,n)` | normalized and support-checked; not promoted to one global physical rule |
| fixed target input `x` | explicit conditioning parameter | makes each `mu_(g,x)` a neighbour-determined map | both values enumerated separately; no extra varying site condition hidden |
| three deterministic target-law classes | explicit finite boundary condition | defines the output maps and proper-cubic orbits being tested | reconstructed in both runners; alternative laws, not simultaneous assembly |
| single forming target | explicit conditioning | isolates record content from formation location/rate | no formation rule inferred |
| `F_bin` and its finite-sum extension | explicit non-axiom construction | supplies the declared scalar codomain, separator, collection rule, empty value, and finite additivity checked here | no claim of axiom supply, existence as the physical readout, or physical selection |

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
3. **Declared-functional obligation — discharged for `F_bin`.** Show that
   singleton values determine every member of the explicitly declared family,
   that `delta_0,delta_1` span it, and that the optional finite-sum extension
   has its claimed algebraic properties. This is not an axiom derivation.
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
target_blocker_text: "for a site that forms a record, do neighbour configurations separated by the declared finite point-mass law lock different content, and does an explicitly declared content-only separator distinguish it?"
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "submit the finite conditional content/separator theorem and paired refutation checker to independent audit; keep physical-law assembly, physical-readout selection, and mosaic observables open"
claim_id: cycle985_neighbour_dependence_record_content
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: bounded support theorem
conditional_surface_status: "exact for the declared P0/P1 embedding, finite point-mass conditioned laws, and explicit non-axiom separator on the binary radius-one single-target family, conditional on record formation"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "finite constructed point-mass witness cap and explicit non-axiom separator; physical admissibility-law assembly, physical-readout selection, and mosaic extension remain open"
claim_type_reason: "exact exhaustive supported-content census and declared-functional separation in the finite M2(C) point-mass construction"
audit_required_before_effective_retained: true
bare_retained_allowed: false
audit_status_authority: independent audit lane only
negative_assertion_classes: []
packet_primary_runner: scripts/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.py
packet_helper_runner: scripts/frontier_cycle985_neighbour_dependence_record_content_independent_check_2026_08_11.py
packet_helper_claim_scope: cycle985_neighbour_dependence_record_content
review_loop_disposition: pass
```
