# Block 228 Result Adjudication

## Decision

`partial-attempt-with-named-untested-routes`

The generated reduced-word phase/contact product does not pass Stage A1. Its
exact local-cylinder completion is positive, but the first root/seam
two-contact separation produces three normal forms. This excludes only the
frozen 45-row product table. It is not a no-go for finite coalescence,
permanent Record formation, the carrier, or the axioms.

## Positive compiler result

The mechanical precompiler emits 50 raw rows over 45 exact source cylinders.
Four complete cylinders initially have distinct controller-first and
contact-first successors:

```text
H-L-T_F-L
P-H-T_F-A
P-H-T_F-T
P-H-T_F-T_F
```

In every case both successors reduce, using only the frozen lower table, to
one identical bounded state. The compiler therefore collapses all `4/4`
cells without priority or a handwritten repair. The resulting 45-row table
has one output per exact cylinder, fixed onsite alphabet, and support at most
four arm sites.

## Exact first reduced witness

The first 20 canonical fixtures pass. Fixture 21 is

```text
n=4, contacts={1,4}
R-H-T_F-T-T-T_F-A
```

Its required normal form is `R-P-P-P-P-P-S`. The frozen product table instead
has three normal forms and no cycle:

```text
CF_A, M, QF_T:
R-H-T_F-T-T-T_F-A -> R-H-T-L-L-T-A

CF_A, QF_T, B:
R-H-T_F-T-T-T_F-A -> R-P-H-T-L-L-A

QF_T, B, B_F3, A:
R-H-T_F-T-T-T_F-A -> R-P-P-P-P-P-S
```

The two failed schedules consume both exact contacts but leave two adjacent
visible `L` certificates. The successful schedule consumes the seam contact
inside the moving abort front. Thus the residue is schedule-selected
certificate multiplicity, not missing contact visibility or an unserviced
participant.

## Strong live-route diagnostic

A separate post-stop diagnostic adds exactly one coalescence cell,

```text
H-T-L-L -> P-H-T-L,
```

without changing the Block-228 table or crediting it as a Block-228 pass. It
closes the original 230 fixtures and every contact subset on
`R-H-T^n-A`, `1<=n<=10`: 2,046 fixtures, 249,006 reachable states, 576,990
transitions, maximum 513 states per fixture, one declared normal form, and no
cycle. This is bounded reduced-word evidence for Block 229, not a local-rank,
full-state, CP, fairness, or Record result.

## Executed boundary

- primary science checks: `10/10`;
- raw/completed rows: `50/45`, with `4/4` same-cylinder joins;
- canonical Stage-A1 fixtures before stop: `20/230`;
- reachable states/transitions before stop: `117/120`;
- participant-accounting transitions/mismatches: `120/0`;
- behavioral mutation checks: `5/5` over 32 live row omissions;
- mutation surface: `contract_bound=48`, `behaviorally_executed=32`,
  `graph_changed=21`, `downstream_unexecuted=16`.
- independent reduced reconstruction: `12/12`, reproducing fixture 21, the
  same three normals and histories, zero cycles, and the separate
  `2,046/2,046` coalescence diagnostic without importing the primary.

The arbitrary-length rank, translated critical-pair census, labelled
full-state lift, Y/parallel cells, carrier projectors, CP, fairness, Record
writing, physical time, and law selection are unexecuted and inherit no
result.

## Portfolio action

Block 229 should preregister the one-cell certificate coalescence as an
associative/commutative/idempotent component law, extend the reduced domain to
every contact subset and longer arms, derive a local rank and translated
critical-pair closure, and only then lift it to exact labelled full states and
CP. The first failure of associativity, fixed support, carrier capacity, or
full-state incidence pivots to distributed set-valued incidence.

The independent five-lens tally is `3 one-cell finite completion / 1 general
component coalescence / 1 gravity`. It explicitly rejects a capacity wall:
the failed graph has only 13 states, support remains four, and no new carrier
state is demanded. General component coalescence is the immediate fallback if
the one frozen merge cell exposes any second missing cell or unbounded overlap.

PR #7776 remains a meaningful fixed-carrier transfer-limit result but imports
its clock, scaling, action family, coefficients, and carrier. Its
changing-carrier and physical-law obligations remain longer than this exact
coalescence test, so it does not rerank Block 229.

No axiom update, audit verdict, retained-status promotion, obligation
retirement, or TOE percentage movement is made.
