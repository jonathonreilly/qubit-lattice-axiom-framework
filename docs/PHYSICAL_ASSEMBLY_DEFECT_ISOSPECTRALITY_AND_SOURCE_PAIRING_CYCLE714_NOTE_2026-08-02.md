# Finite Permutation Similarity and Seeded Source-Pairing Coset Clusters — Cycle 714

Date: 2026-08-02

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit status is set only by the independent audit lane; this
note changes no axiom, approved primitive, premise registry, or policy surface.
No coupling, sign, scale, or physical interpretation is selected here.

**Primary runner:**
[`scripts/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02.py`](../scripts/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02.py);
cached stdout
[`logs/runner-cache/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02.txt`](../logs/runner-cache/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02.txt);
paired receipt
[`outputs/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02_receipt_2026-08-02.json`](../outputs/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02_receipt_2026-08-02.json).

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "identify the finite frame dependence of the supplied Cycle-696 assembled matrix and its seeded source pairing without promoting numerical sextet invariance or finite polynomial agreement to an arbitrary-size theorem"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "derive exact stencil-level sextet invariance and an arbitrary-L incidence theorem, then classify the source subspaces that reduce the four numerical clusters"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "permutation action and similarity on the supplied Cycle-696 compiler at L=3..6; finite resolved-weight/Frobenius agreement on the stated frame-size scans; one deterministic source at L=3..6"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the permutation-conjugacy core is exact once the finite bijections are enumerated, while sextet invariance, Frobenius values, inverse pairings, and four-cluster separation are bounded numerical statements"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target and obligation graph

**Exact target.** For the byte-bound Cycle-696 compiler closure, establish at
`L in {3,4,5,6}` that all 24 frame maps are distinct permutations satisfying
the finite group law and that the constructed matrices
`Q_g = P_g Q P_g^T` are therefore permutation-similar to `Q`. On separately
stated finite scans, test the Cycle-713 resolved-weight prediction for
`||Q_g-Q||_F^2` and measure the inverse pairing for one deterministic source.

**Obligation graph.** T1 enumerates the supplied proper-frame table, derives
the constant-sign sextet, and checks the dof maps for bijectivity,
faithfulness, identity, and composition. T2 is the exact index-roundtrip
identity for permutation similarity; numerical eigensystem and power-sum rows
are consistency checks, not its proof. T3 reads and validates the Cycle-713
receipt, squares its finite resolved-weight rows, and compares their prediction
with the assembled matrices. T4 proves the source-transfer identity by the same
permutation algebra and separately measures fixed-source pairings. T5 derives
the four right cosets and measures both operator and seeded-pairing clustering.

**Strongest missing lemma.** This cycle does not derive exact stencil-level
invariance of `Q` under the sextet, an arbitrary-`L` action/census theorem, or a
source-independent claim of four distinct pairing values. Those are not
silently inferred from permutation similarity.

## Supplied inputs and read inventory

The matrix `Q`, dof index, site map, spatial classes, tick multiplier `LT=2`,
finite-difference convention, and frame table are supplied by the landed
[`Cycle-696 compiler`](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
and its four transitive local imports. The finite resolved-weight rows are
supplied by the landed
[`Cycle-713 classification`](PHYSICAL_DEFECT_WEIGHT_LAW_AND_COMPLETE_CENSUS_CYCLE713_NOTE_2026-08-02.md)
and its paired receipt. The primary runner declares all seven source/receipt
paths in `AUDIT_INPUT_PATHS`, so drift in either closure invalidates its cache.
It writes only its paired receipt and declares `AUDIT_TIMEOUT_SEC = 300`.

The transport and defect convention agrees with the landed
[`Cycle-710 finite covariance-boundary census`](PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_AND_MIXED_FRAME_COMPARATOR_CYCLE710_NOTE_2026-08-02.md):
`E_g = Q_g-Q`, with `Q_g[i,j]=Q[m_g(i),m_g(j)]`. No audit verdict from any
dependency is imported as scientific evidence.

## Result I — a faithful finite permutation action

For every supplied proper rotation `g`, the map `m_g` combines the compiler's
site map, the class relabeling `v -> |g v|`, and the low-corner anchor shift
`x -> x + min(g v,0)`.

- All 24 maps are bijections at `L=3,4,5,6`, with dof counts
  `98, 279, 604, 1115` matching
  `3(L-1)L^2 + 3(L-1)^2L + (L-1)^3`.
- All 24 induced permutations are distinct at each size, so the enumerated
  action is faithful on this finite surface.
- The identity frame gives the identity map, and
  `m_(ab)=m_a after m_b` holds for all 576 ordered pairs at `L=3,4`.
- Dropping the anchor shift rejects the construction: at the recorded `L=3`
  witness, 45 of 98 dofs fall outside the index and only 53 images remain.

The constant-sign predicate is evaluated rather than stored as six frame
indices. It derives frames `[1,4,9,15,18,23]`, exactly the six supplied
rotations that stabilize the unoriented `(1,1,1)` body diagonal. Closure,
identity, and the trace multiset `[-1,-1,-1,0,0,3]` are checked independently.

## Result II — positive permutation similarity

Let `P_g` be the pullback permutation defined by `(P_g v)_i=v[m_g(i)]`.
The runner constructs

`Q_g = P_g Q P_g^T = Q[m_g,m_g]`.

Because `m_g` is a bijection, applying the inverse index permutation recovers
`Q` bit for bit for every frame at `L=3..6`. Thus `Q_g` and `Q` have the same
eigenvalue multiset on this bounded surface. This positive algebraic identity,
not a finite list of power sums, is the reason every function only of that
eigenvalue multiset agrees.

Numerical consistency checks give worst sorted-eigenvalue differences
`1.9e-13` (18 mixed frames, `L=3`), `4.8e-13` (18, `L=4`), `4.0e-13`
(4, `L=5`), and `9.4e-13` (2, `L=6`). The trace, second-power, third-power,
and extreme-eigenvector rows are redundant checks. A magnitude-preserving
random resigning of one defect support moves the spectrum by at least
`8.92` at `L=3` and `9.36` at `L=4`, showing that equal defect size and
sparsity alone do not imply similarity.

This is not a claim that the defect has no other observable content. In
particular, the next two sections measure its Frobenius norm and a supplied
source pairing, both of which depend on more than the eigenvalue multiset.

## Result III — finite resolved-weight Frobenius prediction

The Cycle-713 receipt classifies resolved entries (`|E_ij|>1e-9`) at every
mixed frame and `L=3..9` into per-sign magnitude rows

`4: 8u^3`, `2 sqrt(3): 8u^3`,
`2 sqrt(2): 12u^3+16u^2`,
`2: 20u^3-8u^2+4u`, and `1: 16u^2`, with `u=L-1`.

Squaring those target magnitudes and doubling for the two signs gives the
finite prediction

`||E_g||_F^2 = 800u^3 + 224u^2 + 32u`.

This arithmetic reassembly is exact for the supplied integer rows; agreement
with the finite-difference assembled matrix remains numerical. The runner
checks all 18 mixed frames at `L=3..7` and three at `L=8`:

| `L` | prediction | frames | worst relative difference |
|---|---:|---:|---:|
| 3 | 7360 | 18 | `3.4e-9` |
| 4 | 23712 | 18 | `2.1e-9` |
| 5 | 54912 | 18 | `1.5e-9` |
| 6 | 105760 | 18 | `1.1e-9` |
| 7 | 181056 | 18 | `8.2e-10` |
| 8 | 285600 | 3 | `6.4e-10` |

The sextet's measured squared-Frobenius defect ceiling is `2.9e-17` over all
six frames at `L=3..6`; it is below the declared compiler tolerance, not
promoted here to an exact arbitrary-size zero theorem. The relative ratio
`||E||_F^2/||Q||_F^2` increases across the six scanned sizes from `0.1029` to
`0.1802`; no asymptotic conclusion is drawn.

## Result IV — transfer identity and seeded four-cluster measurement

For every invertible `Q` on the finite surface, permutation algebra gives

`b^T Q_g^-1 b = (P_g^T b)^T Q^-1 (P_g^T b)`.

Direct solve versus source-orbit evaluation agrees for all 24 frames to
`1.1e-16` at `L=3` and `3.4e-14` at `L=4`. With NumPy RNG seed 714, transporting
the source reproduces the reference solution to `4.2e-14`. Holding that source
fixed changes each of the three tested mixed-frame solutions; the minimum
relative deviation is `1.5316` (the three values are approximately
`1.6463, 2.6671, 1.5316`).

The derived sextet has four right cosets of size six. On the compiled matrices,
the 24 `Q_g` form four numerical right-coset clusters at `L=3..6`; the runner
records the worst entrywise within-cluster variation. For the one seeded source
at each size, the inverse pairings are constant within those clusters to
`6.2e-10`, and the four cluster means are separated by at least `0.0027`.
Consequently this deterministic finite scan has four numerical values at each
of `L=3,4,5,6`.

The algebraic conditional is narrower than the submitted claim: if
`P_h Q P_h^T=Q` exactly for every sextet element `h`, then every fixed source
has at most four right-coset pairing values. This runner measures the needed
operator invariance only on the stated finite compiler surface. Permutation
similarity by itself does not imply coset constancy, and a symmetric source can
produce fewer than four distinct values.

## Boundary

- The action/similarity statement is enumerated at `L=3..6`; composition is
  checked at `L=3,4`. No arbitrary-size action theorem is claimed.
- The Frobenius prediction inherits Cycle 713's resolved-entry threshold and
  finite `L=3..9` census. Cycle 714's direct matrix scan covers the frames and
  sizes listed above only. Polynomial agreement is not induction in `L`.
- Eigensystem, sextet-defect, inverse-solve, and pairing values are numerical
  measurements against the supplied finite-difference compiler and backend.
- Four distinct pairing values are properties of seed 714 on `L=3..6`, not of
  every source. Exact source-independent coset constancy would require the
  missing exact sextet-invariance lemma.
- The matrix is nonsingular and indefinite on the tested sizes. The pairing is
  signed; no positivity, energy, minus-branch-floor, continuum, wrapped-box,
  temporal-sector, or dynamical interpretation is licensed.
- The frame action is compiler structure. It is not a symmetry claim about the
  framework axioms and introduces no primitive or premise.

## Review record

Review repair replaced universal spectral-blindness/no-go language by the
positive permutation-similarity statement; bound the complete Cycle-696
runtime closure and Cycle-713 source/receipt; derived and checked the sextet and
faithfulness; corrected the fixed-source minimum; separated exact algebra from
finite numerical measurements; made the finite Cycle-713 dependence explicit;
and added current status, traceability, obligation, artifact-link, and graph
surfaces. Hostile dependency/cache and implication checks are recorded in the
review-loop findings ledger, not as audit verdicts.

## Runner

The primary runner prints `TOTAL: PASS=47 FAIL=0` on the repaired exact-current
tree. Its receipt verdict is conditional on the accumulated gate failures.
