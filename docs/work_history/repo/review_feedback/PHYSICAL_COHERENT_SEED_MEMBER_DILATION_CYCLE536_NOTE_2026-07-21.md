# Physical coherent-seed member dilation — Cycle 536 note (2026-07-21)

## Status and claim ceiling

- **Authority: none**
- **Audit: unset**
- runner:
  `scripts/physical_coherent_seed_member_dilation_cycle536_2026_07_21.py`
- runner SHA-256: 911d500b42d6c45644ad6d0a9f50a79572380e7b01592a6bf66a842c3c4fcf2f
- no axiom, foundation, Qualification, primitive-registry, policy, queue,
  audit-status, or other control-plane file is edited;
- no stage, commit, push, PR mutation, or merge is performed by this lane.

This cycle constructs a **finite reversible unitary dilation** with a retained
seed/bath and the exact Cycle-531 member and receipt interface.  Its strongest
unconditional result is a coherent premeasurement/dilation theorem.  It is not
stochastic dynamics, not Born, not actualization, not a Record, and not
realized history.

The fixed circuit derives that the seed/member **reduced diagonal** equals the
operational grade vector `q`.  The further statement that an actual-member
kernel obeys `p=q` is a supplied candidate kernel interpretation.  No single
member is read or selected by the unitary.

## Constructive circuit

The bounded port composite contains:

```text
176 M2  exact frozen Cycle-531 port/interface composite
  5 M2  retained seed/bath S
  5 M2  recurrent echo head Q
 20 M2  five reversible candidate-echo slots
---
206 M2
```

The seed begins blank.  Because the imported Cycle-505 binding candidate is
one-hot, five fixed CNOTs prepare it coherently:

```text
S[label] ^= BINDING_ELIGIBILITY[label]   for every label 0,...,4.
```

On a coherent binding state this produces orthogonal retained bath labels with
no random seed and no host choice.  The recurrent schedule then executes:

```text
MEMBER[label]      ^= S[label]
LAW_RECEIPT[label] ^= S[label]           for every label

apply exact Cycle-531 binder

ECHO_OCCURRENCE[q] ^= Q[q] AND OCCURRENCE
ECHO_CONTENT[q,l]  ^= Q[q] AND ATOM_CONTENT[l]

apply exact Cycle-531 inverse

MEMBER[label]      ^= S[label]
LAW_RECEIPT[label] ^= S[label]

Q -> Q+1 mod 5.
```

The retained seed is never changed by recurrence.  Member, receipt, and all
Cycle-531 output/work scratch finish blank.  The Cycle-526 public ports and
Cycle-505 binding block are unchanged.  Reapplying the seed-preparation CNOTs
at a later clean boundary unprepares the seed exactly; doing so retains no
classical read of it.

No runtime helper calls a norm, grade, random generator, choice, sampler,
partial trace, or host randomness service.  Operational grades enter only the
separate state-level diagnostics described below.

## What `p=q` does and does not mean

Let the coherent operational binding sectors be orthogonal and have squared
norms

```text
q_lambda = ||psi_lambda||^2,   sum_lambda q_lambda = 1.
```

The fixed seed copy gives

```text
sum_lambda |psi_lambda>_binding |lambda>_seed.
```

At the Cycle-531 midpoint it also gives one-hot `MEMBER=lambda` and matching
receipt on each retained sector.  A **diagnostic partial trace** over the
orthogonal binding/seed environment has seed and member diagonal `q`.  That
equality is algebraically derived and tested on actual train and held
operational grade vectors.

However, a diagonal density operator is not one realized member.  The runner
therefore represents two different types:

```text
ReducedSeedDiagonal:
    diagonal=q,
    actual_member=None,
    probability_law=None

CandidateKernelInterpretation:
    p=q,
    derived_from_unitary=False,
    stochastic_process_derived=False,
    Born_derived=False,
    sampler=None.
```

Thus `p=q` is a supplied candidate kernel if it is used to assign
actual-member probabilities.  What is derived is only the reduced diagonal.
No Born rule or actualization law follows from the equality.

A pure correlated dilation does not require a supplied bath mixture.  If the
same diagonal is instead described as a classical ensemble, then the supplied
bath mixture and its weights are additional inputs.  In either description,
reading one member requires a branch actualization/read law that this circuit
does not contain.

## Exact Cycle-531 composition

For every binding label, every echo-head origin, all 16 `K` positions, and
each lawful current pair `(0,0)`, `(1,0)`, `(0,1)`, the runner checks:

1. blank seed -> one-hot seed equal to binding label;
2. exact seed-preparation inverse;
3. exact one-hot Cycle-531 `MEMBER` plus matching receipt;
4. bit-for-bit equality with the original Cycle-531 midpoint;
5. occurrence exactly when `EDGE_PASSED=1` on the correlated code;
6. correct atom flag/content;
7. recurrent inverse and zero scratch;
8. unchanged source, binding, and retained seed.

Mismatched seed/binding counterfactuals produce no occurrence.  This shows that
the seed-binding correlation is load-bearing; it is not a hidden label service.

The result remains a port/interface composition.  Cycle 531's native upstream
amplitudes and remaining dense/preparation walls are strict-hash imported, not
rebuilt as one integrated 206-M2 amplitude encoder.

## Train/held dilation diagnostics

The runner evaluates all four frozen operational fixtures:

- L5 interface / train program: `z-plus`, `y-plus`;
- held L6 interface / held program: `x-plus-held`, `held-skew`.

For each it builds the label-algebra representative with sector amplitudes
`sqrt(q_lambda)` and nontrivial retained phases.  It requires:

- unit input and output norm;
- five distinct coherent seed sectors;
- reduced seed diagonal exactly `q`;
- reduced member-scratch diagonal exactly `q` at the binder midpoint;
- exact recurrent inverse;
- exact seed unpreparation;
- `actual_member_read=None` throughout.

The representative compresses the internal normalized state of each
operational sector to its label ray.  It is exact for the label algebra and
sector norms; it is not a new synthesis of every internal apparatus amplitude.

Empirical strings remain separate from grades.  Actual empirical strings are
absent, and no grade is called a probability outside the supplied candidate
kernel interpretation.

## Recurrence, capacity, renewal, reset, and independence

### Retained same-seed recurrence

With one retained seed and a matching static binding branch, the conditional
label string is

```text
lambda, lambda, lambda, ...
```

not an independent draw sequence.  For each seed/head pair:

- the first five recurrent steps fill all five candidate-echo slots;
- steps six through ten XOR-delete those same echoes;
- after ten steps the seed, head, binding, source, scratch, and archive return
  exactly to the initial seeded state.

This is genuine autonomous finite-capacity echo renewal after the one-time
coherent seed preparation.  It requires no host reset.  It is not permanent
history because renewal deletes the candidate echoes.

The exact finite capacity is five candidate-echo slots.

### Fresh product-bank comparator

For train `N=2` and held `N=4`, the runner also constructs the exact finite
table

```text
P_fresh(lambda_1,...,lambda_N) = product_j q(lambda_j).
```

That table is conditional on separately supplied tensor-product
re-preparation and independence.  It is not generated by the retained-seed
recurrence.  Its finite bank capacity is exactly `N`; reset, bath renewal, and
independence beyond the bank are open.

The same-seed table has support only on five constant words with weights
`q_lambda`.  The runner reports its exact total-variation separation from the
fresh-product table.  A one-step marginal cannot decide independence.

Neither finite table is called stationarity, stochasticity, actual empirical
frequency, or Born probability.  New independent empirical strings require a
fresh independently prepared bath or a physical reset/renewal law.  No host
randomness is used in either calculation.

## Cycle 534 comparator

Cycle 534's explicitly ontic deterministic carrier rotates:

```text
h, h+1, h+2, h+3, h+4, ... mod 5,
```

giving exact 25-step label counts `(5,5,5,5,5)`.  Cycle 536's retained coherent
seed branches are constant, with conditional counts `(25,0,0,0,0)` and their
label permutations.  These are sharply different temporal correlations.

Cycle 534 supplies an explicit non-Born actuality ontology.  Cycle 536 does
not: it retains all orthogonal seed/binding sectors.  Therefore Cycle 536 can
derive a `q` diagonal while still failing to produce the unique ontic member
that Cycle 534 stipulates.  Neither comparator derives Born probability.

## Locality, covariance, inverse, and leakage

The one-time preparation and recurrent dilation use CNOT and Toffoli with
maximum displayed support three M2s.  A fixed line compiler routes each gate
by adjacent SWAPs and restores labels.  Runtime state never selects the
schedule.

Seed, head, member, receipt, occurrence, and echo content are proper-cubic
scalars.  Cycle-531 signed-current rails exchange under endpoint reversal.
The complete recurrent map is tested under all 24 proper-cubic frames with the
same schedule at train L5 and held L6.

The full binary map is a permutation.  Exact reverse-schedule recovery proves
ambient unitary/inverse closure.  On the declared code, clean scratch and
unchanged inputs give zero terminal leakage.  Distinct coherent input sectors
remain distinct.

As in Cycles 531/534, the displayed three-site Toffoli layer is not decomposed
to literal two-site gates here.  One-hot/blank input constraints are validated,
but their autonomous physical preparation/enforcement and preservation through
every intermediate routing SWAP remain open.

The dilation leaves the underlying matter/data fixture unchanged but can
entangle sidebands.  It preserves the prior mass parameter only in that
qualified sense; no enlarged history-output mass eigenstate is claimed.

## Deletions and lawful domains

Separate deletion witnesses cover:

- every binding-to-seed preparation CNOT;
- every seed-to-member and seed-to-receipt emit/unemit;
- every echo occurrence and content gate;
- the Cycle-531 forward/reverse occurrence primitives;
- echo-head recurrence;
- deletion of the retained seed input itself.

Each changed computational basis output has residual `sqrt(2)`.  Removing the
entire seed violates the declared recurrent one-hot domain and is rejected.
Zero-hot, multi-hot, malformed grade, and malformed head inputs are likewise
outside the lawful domain rather than coerced into an outcome.

These residuals establish load-bearing implementation ingredients.  They do
not establish a no-go against other actualization or bath laws.

## Supplied / derived / open

### Supplied

- exact frozen Cycle-531 port/interface binder and upstream event/binding
  surfaces;
- operational coherent branch state and its grade vector `q`;
- blank seed, echo head, archive, and member/binder scratch;
- the interpretation `p=q` if the reduced diagonal is promoted to an
  actual-member candidate kernel;
- fresh tensor-product preparations and independence for the finite product
  comparator;
- proper-cubic field action and static router.

### Derived

- coherent singleton-binding-label copy into a retained seed;
- finite reversible unitary dilation feeding exact Cycle-531 member/receipt;
- reduced seed/member diagonal equal to operational `q`;
- exact inverse, zero terminal scratch/leakage, and deletion witnesses;
- retained same-seed constant strings and five-slot period-ten echo renewal;
- finite product-cylinder consequences conditional on supplied independent
  preparations;
- train/held and all24 covariance controls;
- exact discrimination from Cycle 534's rotating deterministic strings.

### Open

- a law interpreting the reduced diagonal as actual-member probability;
- branch actualization and reading one member;
- a supplied bath mixture if a classical rather than pure dilation is meant;
- autonomous fresh-bath reset, renewal, independence, and arbitrary horizon;
- actual empirical strings, calibration, likelihood, and stationarity;
- Born law, stochastic dynamics, sampler, Record, realized history,
  close/commit, permanence, and readability;
- autonomous input constraints, two-site Toffoli decomposition, integrated
  amplitude compiler, cubic tiling, and full-volume recurrence;
- physical time, energy/stress/source, response, and gravity.

## No-go discipline N1–N8

The exact negative boundary is narrow: this finite unitary and diagnostic
partial trace do not themselves output one realized member.  The following
stress test applies only to that statement.  No broad impossibility or
minimum-content theorem is claimed.

### N1 — normalized constructive families

| family | enforcement class | target | disposition |
|---|---|---|---|
| coherent retained-seed dilation | fixed reversible label copy | derived diagonal `q`; one read | **ATTEMPTED**: diagonal closes, read absent |
| classical supplied seed mixture | mixed-state preparation with weights `p` | conditional member ensemble | **ATTEMPTED**: consequences explicit, mixture supplied |
| fresh independent seed bank | tensor-product preparations | finite product cylinder | **ATTEMPTED**: closes conditionally through N2/N4; independence supplied |
| autonomous regenerative bath | local bath dynamics | fresh independent events | **OPEN** |
| branch-actualization law | objective selection of one retained sector | one actual member | **RULED OUT BY PRIOR as derived**, but remains a candidate law class |
| host random read | external random choice | one sampled label | **RULED OUT BY SCOPE** |
| Cycle-534 deterministic carrier | explicit ontic phase | non-Born member string | **RULED OUT BY PRIOR as a stochastic route**, retained comparator |
| objective stochastic field | law-owned noise/dilation plus calibration | actual strings and probabilities | **OPEN** |

The open regenerative-bath and objective-field routes prevent any shared no-go.

### N2 — wall-independence audit

- coherent seed preparation is independent of branch actualization;
- branch actualization is independent of Record permanence;
- fresh-bank independence is independent of the one-step marginal;
- bath reset is independent of branch reading;
- empirical calibration is independent of the reduced diagonal;
- absence of host randomness is independent of unitary closure.

The retained-seed/fresh-product TV discriminator directly separates one-step
kernel content from temporal independence.

### N3 — hidden-wall scan

Named inputs are the operational branch state, singleton binding, blank seed,
blank member/receipt/output scratch, echo head, `p=q` interpretation, optional
classical bath mixture, optional fresh-product preparations/independence, and
the routing/frame chart.  Diagnostic partial trace, finite horizon, L5/L6 port
scope, three-site Toffoli, absence of reset, and absence of empirical data are
explicit.  No host random helper or selected outcome hides in the runner.

The approved primitive registry is checked.  Its realized-state primitive
supplies a pointwise slot but no content, selector, measure, probability, or
typicality.

### N4 — residual matching

| residual | diagnoses | does not diagnose |
|---|---|---|
| zero unitary/inverse/leakage | reversible dilation | one actual member |
| zero reduced-diagonal residual | algebraic equality to `q` | Born probability |
| nonzero same-seed/product TV | temporal independence wall | actualization |
| `sqrt(2)` gate deletion | load-bearing primitive | ontology necessity |
| zero all24 mismatch | covariance | stationarity or empirical truth |

No residual has the signature of a route-independent actualization obstruction.

### N5 — rhetoric audit

Permitted: coherent dilation, derived reduced diagonal, supplied candidate
kernel, retained sector, conditional table, diagnostic trace, candidate echo.

Forbidden as conclusions: derived stochasticity, Born rule, collapse, actual
member read, empirical frequency, stationary bath, Record, realized history,
required ontology, shared no-go, or axiom pressure.

### N6 — partial closure

Retain the exact one-step dilation, exact `q` diagonal, retained-seed recurrent
comparator, supplied fresh-product cylinders, Cycle-534 temporal discriminator,
and all physical controls.  Leave branch read, reset, independence derivation,
and calibration open.  This partial result is useful even if no actualization
law is selected.

### N7 — steelman and concrete route

Construct a bounded local regenerative bath whose physical recurrence prepares
fresh orthogonal seed sectors without host refresh.  Prove its finite-window
mixing and reset law rather than assuming an iid bank.  Couple a law-owned
actualization receipt to the exact Cycle-531 interface and compare blinded
member strings against separately typed operational grades on train and held
preparations.  Require inverse/leakage for the dilation, an explicit nonunitary
or enlarged-unitary account of reset, all24 covariance, and a predeclared
likelihood test capable of rejecting `p=q`.

This route could overturn the current open boundary without changing axioms.

### N8 — cross-cycle echo

Cycles 243, 259/262/266, 500, 505, 508, 531, and 534 repeatedly separate
coherent event/candidate support from one law-owned realized member.  Cycle 536
adds the strongest local unitary form: even exact reduced `q` survives with all
branches retained.  The repetition prioritizes the N7 bath/read experiment,
but open constructive families mean there is no axiom pressure.

## Disposition and TOE dependency ledger

### Executed result

The frozen evaluator returns `PASS=8 FAIL=0`.  Its final measured scientific
body runs in `51.90234416699968` seconds after imports, with maximum RSS
`855195648` bytes and process swap count zero.  Exact controls are:

- `1,200` binding x head x `K` x current compositions, with zero preparation,
  member/receipt-type, Cycle-531 midpoint, occurrence, inverse, scratch,
  mutation, or mismatched-seed occurrence failures;
- all four train/held coherent dilation fixtures, with maximum
  `p=q` reduced-diagonal residual `5.551115123125783e-17`, exact norm/inverse,
  and `actual_member_read=None`;
- all 25 retained seed/head recurrence origins: five occupied slots after five
  updates, zero after ten, exact ten-step return, and zero inverse failures;
- supplied fresh-product marginal residual at most
  `5.551115123125783e-17`;
- exact same-seed versus fresh-product TV separations
  `0.7467648282773651`, `0.6942593037478927`,
  `0.9199590713745073`, and `0.972585710332243` for the four fixtures;
- `1,800` all24 frame tests and zero failures;
- 48 separate deletion witnesses, each with basis residual `sqrt(2)`, plus
  rejection of a deleted retained-seed word;
- 176 recurrent gates; 186 gates for prepare–recur–unprepare; static routing
  through `21,603` adjacent SWAPs / `129,804` nearest-neighbor primitives,
  maximum displayed support three, exact routed/logical equality and inverse,
  and zero route/label failures;
- routed schedule SHA-256
  `ad73383c7cd2f10adbc61b266b0570d50f00cb80f56dc95287b540d36f665991`;
- full N1–N8 control PASS with shared obstruction, minimum-content theorem,
  and axiom pressure all false.

The conditional 25-step same-seed strings have exact frequencies `1` for the
retained label and `0` for the other four labels.  They are explicitly marked
`empirical=False` and `probability=None`.  Cycle 534's comparator has exact
frequency `1/5` per label.  Actual empirical strings remain absent in both
comparisons.

Gate disposition: **PASS** for the bounded coherent-seed dilation, derived
reduced diagonal, exact Cycle-531 interface, recurrent same-seed comparator,
and conditional finite fresh-product table.  **FAIL / DO NOT SHIP** for derived
`p=q` probability, stochastic dynamics, Born, actualization, empirical
frequency, stationarity, Record, realized history, permanent renewal,
source/gravity, shared obstruction, minimum-content theorem, or axiom pressure.

| wall | Cycle-536 movement | remaining obligation |
|---|---|---|
| `C_ref` | binding label prepares a retained seed by a fixed coherent copy, removing runtime label choice | derive physical operational-state preparation and any actualization/read law |
| `C_num` | exact train/held reduced diagonals and finite N2/N4 tables | empirical calibration, arbitrary horizon, precision/mixing theorem |
| `C_wrap` | same-seed period-ten echo renewal is exact but deletes candidates and is not time | non-erasing history, physical interval, autonomous fresh-bath reset |
| `C_int` | exact Cycle-531 member/receipt/binder composition | integrated primitive compiler and recurrent full-volume dynamics |
| `C_local` | bounded 206-M2 port dilation, inverse, deletions, all24, train/held | two-site layer, autonomous constraints, amplitude integration, cubic tiling |
| `C_source` | coherent candidate member interface and `q` diagonal now exact | branch actualization, empirical source law, energy/stress/gravity response |

Maturity remains operational quantum/Records `3.4/5`, causal time `1.8/5`,
inertia/matter `4.2/5`, gravity/source `2.1/5`, and Born/probability `2.0/5`.
The exact dilation sharpens the probability boundary but does not cross it.

The optimal next experiment is N7: a regenerative physical bath/reset law and
blinded empirical member-string comparison, with actualization and `p=q`
calibration independently declared rather than inferred from a partial trace.
