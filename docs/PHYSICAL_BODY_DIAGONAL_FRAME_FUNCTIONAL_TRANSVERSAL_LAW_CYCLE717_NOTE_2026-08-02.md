# Finite Body-Diagonal Action, Covering-Family Census, and Seeded Transversal Scans — Cycle 717

Date: 2026-08-02

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit status is set only by the independent audit lane. This
note changes no axiom, approved primitive, premise registry, policy, queue, or
audit-status surface, and it selects no coupling, sign, or continuum limit.

**Primary runner:**
[`scripts/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.py`](../scripts/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.py);
cached stdout
[`logs/runner-cache/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.txt`](../logs/runner-cache/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02.txt);
paired receipt
[`outputs/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02_receipt_2026-08-02.json`](../outputs/physical_body_diagonal_frame_functional_transversal_law_cycle717_2026_08_02_receipt_2026-08-02.json).

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "identify the finite four-valued frame label of the supplied Cycle-696 operator and derive the associated covering-family census without promoting seeded pairing scans to a source-independent theorem"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "derive exact stencil-level sextet invariance and classify the nonzero-average source subspaces on which covering is also necessary"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact finite S4 body-diagonal action and covering-family combinatorics for the supplied frame table; numerical operator and seeded source scans on the stated Cycle-696 boxes"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the finite group identities follow from exhaustive enumeration, while operator invariance and pairing blindness use bounded numerical compiler evaluations"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target and obligation graph

**Exact target.** For the supplied 24 proper rotations, identify the exact
four-point action on unoriented cubic body diagonals and derive the subgroup
covering family and its 231-member census. For the byte-bound Cycle-696
compiler, test at `L in {3,4}` that the assembled operators form four numerical
diagonal-labelled clusters, then scan all 1296 diagonal transversals for two
declared random seeds and five structured sources at each size.

**Obligation graph.** T1 enumerates the four-diagonal action and its stabilizers.
T2 obtains all subgroups by closure expansion and proves, on the enumerated
finite group, that sextet covering is equivalent to transitivity. T3 constructs
the sufficient coset-union family in two ways and derives its census by
inclusion and exclusion. T4 measures the operator clusters. T5 scans seeded
transversals and complements. T6 supplies nearby non-blind controls, structured
source counterexamples to a converse, and an exact zero-average domain guard.

**Strongest missing lemma.** This cycle does not prove exact stencil-level
sextet invariance, an arbitrary-`L` operator statement, or a source-independent
necessity theorem for blind averaging sets. A classification of the source
subspaces that add accidental cancellations remains open.

## Supplied inputs and read inventory

The matrix `Q`, dof index, site map, spatial classes, boundary convention, and
frame table are supplied by the landed
[`Cycle-696 compiler`](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
and its four transitive local imports. The runner declares that complete
five-file runtime closure in `AUDIT_INPUT_PATHS`, declares a 300-second timeout,
and writes only its paired receipt. Cache acceptance therefore binds both the
runner and all load-bearing repository inputs.

The finite permutation-similarity and seeded four-cluster context comes from
[`Cycle 714`](PHYSICAL_ASSEMBLY_DEFECT_ISOSPECTRALITY_AND_SOURCE_PAIRING_CYCLE714_NOTE_2026-08-02.md).
The exact finite group complement criterion and its stated probe boundary come
from [`Cycle 715`](PHYSICAL_FRAME_GROUP_COMPLEMENT_AND_FINITE_PROBE_BLINDING_CYCLE715_NOTE_2026-08-02.md).
The 231-member sufficient family and four-seed finite powerset checks are
context from
[`Cycle 716`](PHYSICAL_COMPLETE_AVERAGING_SET_FRAME_BLINDNESS_CLASSIFICATION_CYCLE716_NOTE_2026-08-02.md).
No dependency's audit status is imported as scientific evidence.

## Result I — exact finite body-diagonal action

Take the four unoriented cubic body diagonals

`d0=(1,1,1)`, `d1=(1,1,-1)`, `d2=(1,-1,1)`, and `d3=(-1,1,1)`.

A body diagonal here is an axis of the rotation group, not a lattice adjacency;
the supplied nearest-neighbour stencil is unchanged. Exhaustive evaluation of
the supplied 24 proper rotations gives all 24 permutations of these four axes,
once each. Thus this finite action is faithful and isomorphic to `S4`.

The stabilizer of `d0` is exactly
`S=[1,4,9,15,18,23]`. Define `delta(g)` as the diagonal that `g` carries onto
`d0`. Its four fibres have size six and are exactly the right cosets `Sg`.
The other three point stabilizers are different sextets.

This exact statement concerns the supplied frame table. Its identification with
the compiler operator is numerical: at `L=3,4`, the measured operator stabilizer
at tolerance `1e-9` is `S`; over all 276 frame pairs, the largest same-fibre
entrywise difference is `1.2e-10`, while the smallest cross-fibre difference is
`4.0`, a separation ratio `3.2e10`. Hence the two bounded compiler scans resolve
four operator clusters labelled by body diagonal.

## Result II — covering is transitivity

For a subgroup `H`, the finite condition `SH=G` holds exactly when `H` acts
transitively on the four body diagonals. The runner obtains the complete
30-member subgroup lattice by starting from the identity subgroup and repeatedly
adjoining every group element and taking closure; it assumes no generator-count
bound.

Exactly nine subgroups are transitive, with orders
`[4,4,4,4,8,8,8,12,24]`. The four order-four examples are regular: each maps
`d0` once to every diagonal. The three other order-four subgroups have only
two-point diagonal orbits. No subgroup of order `1`, `2`, `3`, or `6` is
transitive, and every transitive subgroup contains one of the four regular
subgroups.

Thus four is the minimum order of a **covering subgroup**. It is not a universal
minimum size for physical blindness: structured sources can add blind sets of
smaller size, as Cycle 716 records.

## Result III — exact 231-member covering-criterion family

Under the exact conditional that the sextet fixes the relevant operator/pairing,
unions of right cosets of a covering subgroup are sufficient averaging sets.
The family can be constructed either from all nine covering subgroups or from
the four minimal regular subgroups; direct deduplication gives the same 231
nonempty sets.

Each regular subgroup has six right cosets and contributes `2^6-1=63` unions.
The six pairwise joins have orders `[8,8,8,24,24,24]`, every triple join has
order 24, and the fourfold join has order 24. Inclusion and exclusion gives

`4*63 - (3*7 + 3*1) + 4*1 - 1 = 252 - 24 + 4 - 1 = 231`.

The exact size histogram is
`[(4,24),(8,51),(12,80),(16,51),(20,24),(24,1)]`. Complementation is an
involution on the 230 proper members. At size eight, nine members are cosets of
order-eight covering subgroups and the other 42 are unions of two regular
cosets. These are finite combinatorial identities, not continuum or
arbitrary-box claims.

## Result IV — bounded seeded transversal scans

A diagonal transversal chooses one frame from each of the four six-frame
fibres, giving `6^4=1296` sets of size four. The union of right cosets of the
four regular subgroups contains 24 such sets. For NumPy seeds 7170 and 7171,
all 1296 transversals are evaluated against the normalized averaged-source
pairing at each size:

| box | seed | measured blind sets | least average norm | worst blind spread | best other spread |
|---|---:|---:|---:|---:|---:|
| `L=3` | 7170 | 24, exactly regular cosets | `1.6e1` | `1.4e-11` | `4.4e-3` |
| `L=3` | 7171 | 24, exactly regular cosets | `1.8e1` | `8.8e-13` | `3.7e-3` |
| `L=4` | 7170 | 24, exactly regular cosets | `3.1e1` | `9.7e-11` | `6.0e-2` |
| `L=4` | 7171 | 24, exactly regular cosets | `3.3e1` | `1.0e-10` | `9.5e-2` |

For these four seeded scans, the complements of the 24 regular cosets are also
blind below `1.1e-10`, whereas the other complements spread by at least
`3.9e-4`. This is a finite observation for the named seeds, not a generic-source
statement.

## Rejectors and source boundary

Three nearby group-theoretic controls are non-blind for the first seed. One
whole diagonal fibre spreads by `1.8e-2` at `L=3` and `2.0e-1` at `L=4`. The 18
cosets of the three intransitive order-four subgroups spread by at least
`4.8e-3` and `3.0e-1`. The transversal `[0,1,3,5]`, which has the right balance
but is not a regular coset, spreads by `2.3e-2` and `4.7e-1`.

The runner then makes the failure of a source-independent converse explicit:

| source | `L=3` blind transversals | `L=4` blind transversals |
|---|---:|---:|
| unit slot 0 | 24 | 24 |
| unit slot 1 | 24 | 72 |
| unit slot 7 | 24 | 24 |
| unit slot 8 | 264 | 24 |
| all ones | 1296 | 1296 |

Every row still contains the 24 sufficient regular cosets. Unit slot 8 at
`L=3` and unit slot 1 at `L=4` have nontrivial frame orbits yet add respectively
240 and 48 blind transversals. The all-ones source has a one-point orbit and is
blind everywhere. Therefore neither nondegeneracy of the orbit nor equal
diagonal coverage makes the regular-coset criterion necessary.

The normalized pairing has the explicit domain condition
`||sum_(a in A) P_a^T b|| > 1e-12`. At `L=3`, the integer source with nonzero
entries
`{2:-1,3:1,6:1,7:-1,10:1,11:-1,14:-1,15:1}` has orbit diameter two but
averages exactly to zero on `A=[0,1,3,5]`. The runner returns `NaN` and rejects
classification rather than labelling this undefined normalization blind.

## Claim boundary

Claimed: the exact finite `S4` action of the supplied 24 rotations on four body
diagonals; the exact subgroup lattice, covering/transitivity equivalence,
minimal covering order, 231-member sufficient-family census, and size ladder;
the numerical four-cluster operator identification at `L=3,4`; and the stated
finite source/transversal scans on the byte-bound Cycle-696 compiler.

Not claimed: source-independent necessity; a universal minimum blind-set size;
that every non-one-point source has only 24 blind transversals; exact
stencil-level sextet invariance; exact numerical zero below tolerance; boxes
beyond `L=3,4`; wrapped boundaries; alternative compilers, sources, transports,
or pairings; continuum, asymptotic, covariance, or dynamical conclusions; or an
audit verdict.

## Review record

Review repair removed the false source-robust converse and universal minimum,
added explicit structured and zero-average counterexamples, replaced a
three-generator subgroup search by complete closure expansion, bound the full
runtime input closure and cache, moved stdout to the canonical cache surface,
and added current status, traceability, dependency, obligation, artifact-link,
and conditional receipt-verdict surfaces. Hostile cache/input and semantic
mutation checks are recorded in the review-loop findings ledger, not as audit
verdicts.

## Runner

The primary runner prints `TOTAL: PASS=51 FAIL=0` on the repaired source tree.
Its receipt verdict is conditional on the accumulated gate failures.
