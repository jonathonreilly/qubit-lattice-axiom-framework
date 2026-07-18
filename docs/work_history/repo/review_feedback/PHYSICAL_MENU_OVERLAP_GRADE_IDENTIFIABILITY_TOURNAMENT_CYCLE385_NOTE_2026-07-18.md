# Physical menu-overlap grade identifiability tournament — Cycle 385

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none. This cycle changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface and
drafts no axiom language.

Companion runner:

```text
scripts/physical_menu_overlap_grade_identifiability_tournament_cycle385_2026_07_18.py
```

## Result up front

Under an explicitly supplied effect-functionality premise, the 36 menu
presentations enumerated by Cycle 381 contain 117 effect occurrences and 55
equal-effect classes. Their exact integer menu-incidence matrix has rank 20,
nullity 35, 20 distinct rows, and 14 connected components with sizes

```text
(8, 6, 5, 5, 5, 4, 4, 4, 4, 3, 2, 2, 2, 1).
```

The maximally mixed trace label is a strictly positive normalized solution.
More decisively, the runner constructs a reproducible strictly positive
nontrace finite-table witness by shifting equal-incidence classes 0 and 1 by
`+epsilon` and `-epsilon`. It is not representable by any single qubit density
matrix on all 55 effects. Thus menu normalization plus the supplied finite
effect identification does not select a unique numerical vector on this exact
finite table.

That last sentence is a bounded diagnostic only. It quantifies this
55-class/36-presentation incidence matrix and nothing larger. It is no no-go,
global Born failure, minimum-content claim, or axiom pressure. Live extensions
are exhibited below. There is no probability, actuality, sampler, or frequency
promotion, and neither normalized vector is selected as a law.

## Finite effect-functionality system

Each Cycle-381 fine or declared coarse physical menu is a row. A matrix key
rounded at 13 decimal places is accepted only after the corresponding matrices
are checked equal in Frobenius norm below `1.2e-10`; the largest within-class
residual is `4.3676465171938503e-16`. One supplied grade variable `g_j` is then
assigned to each equal-effect class, including multiplicity when a menu repeats
an effect. The equation is

```text
A g = 1,    g >= 0.
```

This is conditional effect functionality: equal operators share one table
entry. It is not a derived universal effect-functional law. The system has:

| quantity | value |
|---|---:|
| menu presentations | 36 |
| effect occurrences | 117 |
| equal-effect classes | 55 |
| deduplication identifications | 62 |
| rank | 20 |
| nullity | 35 |
| distinct incidence rows | 20 |
| connected components | 14 |
| smallest nonzero singular value | `1.1993528201455856` |
| largest numerical null singular value | `3.7942580809304975e-16` |

The singular-value gap separates the integer rank from roundoff by more than
15 orders of magnitude.

## Positive solutions and bounds

For the trace-labelled comparison

```text
g_trace(E) = Tr(E) / 2,
```

all 55 entries are positive, the range is
`[0.05132596848241043, 0.6800000000000002]`, and the Euclidean normalization
residual is `5.874748045952207e-16`.

Classes 0 and 1 have identical incidence columns and both initially carry
`0.19204418910553744`. Therefore the explicit perturbation

```text
epsilon = 0.09602209455276872
g_alt[0] = g_trace[0] + epsilon
g_alt[1] = g_trace[1] - epsilon
g_alt[j] = g_trace[j] otherwise
```

obeys `A g_alt = 1` without relying on a numerically chosen SVD direction. Its
minimum remains `0.05132596848241043`, its distance from the trace label is
`0.13579574840399722`, and its normalization residual is
`5.874748045952207e-16`. Fitting the difference to the three Bloch parameters
of a single fixed density matrix leaves residual `0.13046989074391827`, so the
assignment is a nontrace finite-table witness, not merely a differently
prepared trace functional.

Perturbation stability is analytic because the two incidence columns are
identical: every signed shift `delta` in the open interval
`(-0.19204418910553744, 0.19204418910553744)` preserves all 36 equations and
strict positivity. The runner additionally checks fractions
`(-0.9,-0.5,-0.1,0.1,0.5,0.9)` of that radius; the smallest grid grade remains
above `0.019` and every normalization residual remains below tolerance. The
witness is therefore an open one-parameter family, not a tuned SVD point.

Linear programs over the exact integer system `A g = 1, g >= 0` give:

- 50 classes with bounds `[0,1]`;
- 2 classes with bounds `[0,1/2]`;
- the identity classes `I/2`, `I/4`, and `I/3` fixed at `1/2`, `1/4`, and
  `1/3`; and
- 52 classes that can reach zero on the closed positive polytope.

Positivity therefore leaves large finite-table freedom. No extremal point or
interior witness is selected by the framework.

## Cycle-383 quotient and refinement contribution

Cycle 383 is used only at its declared quotient levels:

- the canonical unsplit/refined ray has equal coarse effects and equal grouped
  CP maps, both at zero reported residual in the registered quotient;
- the canonical axis pair has equal coarse effects but grouped-CP residual
  `0.43472221389739873`, so only the explicitly supplied effect quotient may
  identify its grade variables; and
- process and future separators remain intact. Equal effect is not asserted to
  mean equal process, occurrence, or Record.

On the fixed 55-variable universe, the fine-only rank is 15, the coarse-only
rank is 12, and the combined rank is 20. Thus including all exact coarse and
refinement presentations adds five independent constraints relative to the
fine-only system. Nine fine-minus-coarse rows are nonzero and have rank 8.
These exact identities narrow the finite grade space but do not select a
single vector.

## Bounded Cycle-317 host-instantiated menus

The landed bounded Cycle-317 compiler is tested on the same three mixed binary
menus and four-component axis merge used by Cycle 381. Their coefficients,
directions, grouping, and constructor invocation remain host supplied.

Appending all four menus gives 40 rows, 61 effect classes, rank 24, and nullity
37. The three binary menus introduce six new classes and three new internal
degrees of freedom. The axis merge uses only old classes, adds one independent
equation, tightens eight old-class upper bounds, and the host merge reduces the
original-class freedom by one: the projection of the augmented kernel onto the
original 55 classes has dimension 34 rather than 35.

This is a real partial narrowing. It is not autonomous menu registration or a
global functionality law.

## Concrete augmenting menus

The runner exhaustively searches two-, three-, and four-outcome multisets of
the 55 already enumerated effects. It finds 13 exact candidate augmenting menus
that sum to identity, are not existing incidence rows, and individually add a
constraint. A deterministic greedy rank scan extracts 7 independent
constraints, raising rank from 20 to 27 and lowering nullity from 35 to 28
without adding effect variables.

The seven class multisets and representative sources are:

| classes | representative construction |
|---|---|
| `(29,30,34)` | development paired-two-axis fine outcomes 0,1 plus its other coarse outcome |
| `(33,53,54)` | development `0.32I` coarse outcome plus held paired-two-axis fine outcomes 2,3 |
| `(0,0,25,28)` | two copies of canonical axis fine class 0 plus development cancellation fine class 25 and mixed coarse class 28 |
| `(2,2,24,28)` | two copies of canonical axis fine class 2 plus development cancellation fine class 24 and mixed coarse class 28 |
| `(16,36,36,41)` | contact-trine class 16, two copies of a cubic-control fine class, and `I/3` |
| `(17,18,35,35)` | contact-trine classes 17,18 and two copies of a cubic-control fine class |
| `(37,38,41,41)` | a cubic-control antipodal pair and two copies of `I/3` |

The maximum operator sum-to-identity residual among all 13 is
`4.982553445399165e-16`. These are exact operator partitions made from current
effect classes, but they are not physically registered by this cycle. Their
eligibility, local carrier slots, program genesis, and physical compilation
remain constructive work. They cannot be counted as new physical equations
until that work is done.

## Held-size and frame invariance

For every one of the 24 proper-cubic frames, the runner rotates every effect by
its Bloch-vector action, re-deduplicates from scratch, and recovers the same
`36 x 55` incidence matrix and rank. The maximum rotated menu completeness
residual is below `1.2e-10`, and the trace label is frame invariant.

The inherited Cycle-381 carrier checks retain all three six-program carriers
with zero frame-branch failures, held `L=6` leakage below tolerance, and both
canonical and scaled held corpora at `N=12`. The Cycle-383 fixed canonical
carrier preserves the ray two-use coarse-CP quotient in all 24 frames. Corpus
multiplicity repeats physical menu rows; it does not add a new independent
grade equation by itself.

## Deletion and lawful-domain controls

Deleting the final branch of each of the 36 presentations produces a positive
trace-normalization defect; the minimum is greater than `0.05`. Deleting one
menu equation shows 9 rank-essential rows and 27 redundant rows; the minimum
remaining rank is 19.

Eight malformed cases reject: empty menu family, deleted effect-functionality
premise, empty menu, non-Hermitian effect, negative/out-of-range effects,
wrong matrix dimension, nonfinite matrix, and incomplete menu. Positive-bound
linear programs are required to terminate successfully for every class.

## Status-split provenance and supplied structure

The Cycle-317/321/323 substrate/compiler/carrier surfaces were present in the
pinned main base. The Cycle-349/350/351 campaign corpus commit is
`06cb17dcb26c7b6d0aa4377b6f1125bdc3d210bf`; it was not in the pinned main base
at construction, `0355ac4728f57d9fdc62cb27764bbd33e6e8b8df`. Cycle 381 and
Cycle 383 are current campaign working-tree inputs at Cycle-385 construction.
This is historical provenance and permits future landing without invalidating
the computation.

Supplied rather than derived are:

1. the finite Cycle-381 carrier/program tables and menu presentations;
2. the effect-functionality identification on equal matrix keys;
3. the menu-normalization right-hand side `1`;
4. the Cycle-383 quotient level and registration comparator;
5. all Cycle-317 host-menu coefficients, directions, grouping, and invocation;
6. the candidate-menu enumeration range of two through four outcomes;
7. any decision to physically register or declare a candidate menu eligible;
8. any extension, regularity, convex-additivity, or numerical selection law;
9. any probability interpretation, actual-member selection, sampler,
   frequency theorem, or empirical calibration.

## No-Go Discipline Gate

Gate disposition: FAIL for any negative claim. The live routes and steelman
below make a no-go or global nonforcing conclusion premature. The artifact is
therefore demoted to an exact positive alternative-solution witness plus a
finite incidence census. No negative claim is shipped.

### N1 — Alternative route enumeration

| route | attempted action and result | honesty marker |
|---|---|---|
| installed fine/coarse overlap graph | all 36 presentations were deduplicated and solved; a positive alternative assignment remains | ATTEMPTED |
| lawful refinement/effect quotient | Cycle-383 ray and axis quotients plus all coarse rows add five constraints but leave nullity 35 | ATTEMPTED |
| bounded host compiler menus | three mixed binaries and one merge were instantiated; the merge lowers old-class freedom by one | ATTEMPTED |
| exact hybrid menus from current effects | 13 exact partitions were found and seven are independent, but physical registration was not built | ATTEMPTED algebraically; LIVE physically |
| larger rotated/coefficient menu family | compile additional directions and coefficient families so effects recur across more menus | UNTESTED — LIVE |
| derive convex additivity/affinity | seek a physical split/merge law that forces `g(E+F)=g(E)+g(F)` beyond row subtraction | UNTESTED — LIVE |
| multi-use/composed instruments | register lawful two-use effects as new menu equations while preserving process distinctions | UNTESTED — LIVE |

Because at least three distinct constructive routes remain live, N1 blocks any
negative conclusion.

### N2 — Wall-independence audit

For this constructive diagnostic the collapsed open-condition set has only two
items:

- `O_menu`: physically compile/register additional overlap menus;
- `O_law`: derive an effect law such as additivity/affinity that supplies more
  equations on the same classes.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `O_menu`, `O_law` | no | no | yes |

The supplied finite effect-functionality premise and supplied normalization
rows are not counted as walls. Numerical selection/actuality is a later
semantic task, not a third identifiability wall. No inflated wall count is
used.

### N3 — Hidden-condition scan

The trigger terms were audited as follows:

| phrase class | classification |
|---|---|
| `canonical` | source label for the Cycle-321 carrier; non-load-bearing |
| `registered` | physical-status distinction stated explicitly for installed versus candidate menus |
| `at construction` | immutable provenance date, not a physics premise |
| `supplied` | explicit load-bearing imports listed above |

The note does not use “we assume,” “as is standard,” “naturally,” “obviously,”
“standard QFT,” or “the framework provides” to hide a condition. No hidden
condition changes the N2 set.

### N4 — Residual matching

| cited witness | witness residual | Cycle-385 use | match? |
|---|---|---|---:|
| `physical_born_menu_grade_interface_census_cycle381_2026_07_18.py:245` and `:263` | exact installed fine/coarse effects and their equality tolerance | constructs the same 36 presentations and 55 effect classes | yes |
| `physical_mixed_projective_refinement_functionality_born_bridge_cycle383_2026_07_18.py:455` | ray effect/coarse-CP quotient | validates the ray quotient before sharing grade variables | yes |
| `physical_mixed_projective_refinement_functionality_born_bridge_cycle383_2026_07_18.py:514` | axis effect equality with CP separation | permits only the supplied effect quotient and retains process separation | yes |
| `physical_born_menu_grade_interface_census_cycle381_2026_07_18.py:443` | bounded Cycle-317 host mixed/merge witnesses | reconstructs the same four host menus | yes |

No prior no-go is cited as evidence. Unrelated Records, gravity, inertia,
source, or actuality residuals are not used.

### N5 — Rhetoric audit

“The finite graph is underdetermined” means exactly the 36-row, 55-class
matrix. Per-effect occurrences and per-menu rows were tested; the bounded
three-M2 carriers and held `L=6,N=12` reuse were checked for invariance.
Arbitrary local-menu families, all blocks, all lattice regions, continuum
effects, and lattice-wide laws were not tested. Therefore the note never says
Born form, trace form, or grade selection is globally impossible.

“The alternative is not representable by any single qubit density matrix” is
restricted to fitting this one 55-entry vector to one fixed three-parameter
Bloch density functional. It says nothing about contextual, extended,
multi-site, or dynamically selected functionals.

### N6 — Partial-closure path scan

No new axiom is requested. Concrete partial-closure routes are:

1. compile the seven independent candidate hybrid menus into fixed local
   carrier slots and rerun the rank audit;
2. enlarge the physical coefficient/direction family so disconnected graph
   components overlap;
3. derive a lawful additive split/merge identity from physical compositions,
   then audit whether the effect-functionality import retires;
4. register multi-use effects without collapsing distinct CP processes; and
5. separate a later numerical selector from the present algebraic
   identifiability calculation.

These are constructive physics or import-retirement tests, not automatic axiom
pressure.

### N7 — Steelman

A hostile reviewer should reject any no-go here: the tested graph is sparse by
design, has 14 components, and contains only a finite installed menu family.
Cycle 385 itself finds 13 exact missing overlap partitions, seven of which add
independent constraints without new effect nodes, while the single physically
host-instantiated merge already reduces old-class freedom. A compiler that
registers those hybrid menus, a broader rotated coefficient family, or a
physical additivity law could reduce the kernel sharply and perhaps identify a
trace functional. The positive alternative assignment therefore refutes
uniqueness only on the enumerated table; it supplies no reason to foreclose
those live routes.

This steelman is convincing, so the negative gate fails and the claim remains
the narrow positive finite-table witness.

### N8 — Cross-cycle echo

The repository search found the closest same-residual echoes:

- Cycle 321 already exhibited finite normalized nontrace freedom and explicitly
  queued enlargement of the linked menu family;
- Cycle 380 stated that effect functionality plus a sufficiently linked finite
  menu family could fix trace form and warned that no finite witness alone is a
  Born law;
- Cycle 381 enlarged and classified the physical menu family; and
- Cycle 383 supplied a conditional refinement/effect quotient while preserving
  CP separators.

The mechanism across those cycles is progressive menu linking and quotient
discipline, not constitutional foreclosure. Cycle 385 applies the same
mechanism quantitatively and finds further exact augmentations. The echo
therefore reinforces the N7 steelman and blocks a negative conclusion.

## Disposition

The strongest result is positive and exact: one explicit strictly positive
nontrace normalized vector exists on the current physical overlap table, the
full positive bounds are computed, and seven concrete independent overlap
menus are named for physical compilation. The bounded residual is 35 affine
directions on this table, reduced to 34 on the original variables by the tested
host merge.

The optimal next campaign is to compile the seven candidate menus into fixed
bounded physical carrier slots with local eligibility/genesis, then rerun the
same deduplication, rank, positivity, frame, held-size, deletion, and
process-separator audits. Until that is done, candidate rows remain algebraic
operator partitions rather than physical menu equations.

## Verification

```text
python3 -m py_compile \
  scripts/physical_menu_overlap_grade_identifiability_tournament_cycle385_2026_07_18.py

python3 \
  scripts/physical_menu_overlap_grade_identifiability_tournament_cycle385_2026_07_18.py
```
