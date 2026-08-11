# Patch-uniformity induction under finite closed-star gluing

Date: 2026-08-11
Cycle: 986
Claim type: `bounded_theorem`
Audit-status authority: independent audit lane only

This packet records no audit verdict and changes no axiom, approved primitive,
registry, queue, policy, or effective-status surface.

## Trace gate

```yaml
trace_class: direct_blocker_closure
reachability_to_target: closes
target_claim_id: null
target_blocker_text: "determine whether translation-uniformity on P2x extends to arbitrary finite target count by closed-star gluing, or identify the first exact obstruction"
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "independent audit of the finite-patch induction packet"
```

## Result up front

The gluing step verifies. The executable verdict line is

```text
FINITE_P2X_ROOTED_STAR_GLUED_PATCH_UNIFORMITY_FOR_ARBITRARY_FINITE_TARGET_COUNT
```

The exact quantifier is:

> For every integer `n >= 2` and every ordered tuple of distinct targets
> `(t_1,...,t_n)` in `Z^3` such that `t_2-t_1` is a signed unit vector and,
> for every `m=3,...,n`, the closed star `S(t_m)` intersects
> `union_{i<m} S(t_i)`, the same relative 23-program dependence-law chart is
> translation-uniform at every target of the finite support union
> `Omega_n = union_{i<=n} S(t_i)`.

This is a theorem for every member of an arbitrary-size **finite** family. It
is not a theorem about the infinite target set `Z^3` considered as one patch,
does not construct an infinite allocation, and does not supply a simultaneous
execution schedule.

## Definitions and supplied boundary

For `t in Z^3`, let

```text
S(t) = {t} union {t+d : ||d||_1 = 1}.
```

At each target use one translated copy of the relative family

```text
I;
X(t);
CNOT(t+d -> t) for each of the six signed unit directions d;
TOF({t+d,t+e} -> t) for every unordered pair d != e.
```

The family has `1+1+6+C(6,2)=23` descriptors. Its exhaustive local census is
21 neighbour-dependence witnesses with proper-cubic classes

| class | size | stabilizer | `J` |
|---|---:|---:|---:|
| CNOT | 6 | 4 | 1 |
| perpendicular-control TOF | 12 | 2 | 2 |
| opposite-control TOF | 3 | 8 | 0 |

where `J` is the squared norm of the sum of the centre-relative control
vectors. Each local word is hosted separately on its complete closed star.
That word-by-word statement does not assert that alternative words can be run
simultaneously.

The only framework source read by the primary is
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). The landed
[`RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md`](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
is the documentation authority for the computed route substrate. Its route
core is loaded from an immutable Git archive and separately SHA-256/Git-blob
pinned. Earlier induction and two-star artifacts supplied the
research question but their text and AST are neither inputs nor executable
dependencies; the base and step are reconstructed in this packet.

## A_GLUING_STEP — checkable lemma

### Finite closed-star chart-gluing lemma

Let `T_k={t_1,...,t_k}` be a finite target patch with support
`Omega_k=union_{i<=k}S(t_i)`. Assume its charts are uniform in the following
explicit sense:

1. each chart carries the same translated 23-descriptor local template and
   every word is route-hostable on that chart's complete star;
2. each global site in two charts is bound to one coordinate-labelled Boolean
   variable;
3. on each shared unordered semantic pair, the two chart restrictions agree
   on the `Z^3`-edge label, normalized Boolean dependence table, witness
   strength, proper-cubic class, `J`, and the canonical global path between
   the shared endpoints; and
4. equality of coordinate bindings is used as the cocycle on a site present
   in three or more charts.

Let `s` be a distinct target. Then `T_k union {s}` is uniform on
`Omega_k union S(s)` if the following mechanically checkable obligations hold:

| obligation | executable condition |
|---|---|
| nonempty gluing | `S(s) intersection Omega_k` is nonempty |
| complete local chart | all seven sites of `S(s)` are in the enlarged support |
| local rule/host | the translated 23-descriptor table and every routed word at `s` reconcile with the universal template |
| pairwise restriction | for every old `t_i` with nonempty star intersection, every shared-site and shared-pair row agrees in all fields listed above |
| multiple-overlap cocycle | every site shared with multiple old charts has the same coordinate binding in all old charts and the new chart |

The conclusion follows because every union datum is old-only, new-only, or
shared. Old-only and new-only values retain their chart values. Pairwise
restriction equality makes every shared datum single-valued, and transitivity
of equality supplies the multiple-chart site cocycle. The target-local rule
record remains one translated template.

The algebraic content is the ordinary compatible-chart statement above:
equality of records on every pairwise intersection, plus the site cocycle,
produces one record on the finite union. The record schema and chart-role
labeling are imported unchanged from the separate
[`Cycle-986 chart-role labeling convention`](PATCH_UNIFORMITY_CHART_ROLE_LABELING_CONVENTION_CYCLE986_META_NOTE_2026-08-11.md).
No labeling rule is asserted by this theorem note. Its use of
“translation-uniform” is limited to the imported record-schema definition.

This is a genuine induction step rather than another fixed-size census: the
number of old charts meeting the new star is arbitrary, while each nonempty
pairwise overlap is drawn from a finite, exhaustible relative-offset set.
Here “arbitrary” means any permitted subset: at most 24 distinct old chart
centres can meet one new closed star. The total finite patch size `k` remains
unbounded.

### Complete two-star overlap census

Two distinct closed unit stars overlap exactly when their centres have
`L1` separation one or two. Exhausting all 24 oriented offsets gives:

| overlap type | oriented offsets | shared sites | shared pairs | normalized shared rule row | `Z^3` edge | class / `J` | agreement |
|---|---:|---:|---:|---|---|---|---|
| adjacent centres (`L1=1`) | 6 | 2 | 1 | `x XOR c` | yes | CNOT / 1 | exact |
| axial distance-two centres | 6 | 1 | 0 | vacuous | vacuous | vacuous | exact |
| diagonal distance-two centres | 12 | 2 | 1 | `x XOR (c_1 AND c_2)` | no | perpendicular TOF / 2 | exact |

For the diagonal row, the two target outputs are distinct global components.
The agreement is equality of the normalized local function under chart-role
identification; it is not the false assertion that outputs with unrelated
target bits must be numerically equal. The path compared by the overlap lemma
is the canonical path between the shared endpoints. Target-to-control routing
outside the intersection belongs to each local chart and need not coincide.

The primary reconstructs all 24 rows; the independent checker reconstructs
them without importing or executing the primary or the pinned router. Both
obtain offset multiplicities `6/6/12` and exact agreement in every row.

## B_STEP_VERIFICATION — smallest extension cases

The mechanical sequence is chosen to exercise all three overlap types:

```text
P2x: A=(0,0,0), B=(1,0,0)
P3x: add C=(2,0,0)
P4T: add D=(1,1,0)
```

### Base reconstruction

The primary independently rebuilds both P2x target charts and their adjacent
overlap. Each target has 23 descriptors, 2944 landed/Boolean evaluations, 21
witnesses, classes `6/12/3`, `J={1,2,0}`, and route totals 232 expanded
primitives and 292 nearest-neighbour gates. The two target-local records and
the adjacent overlap agree exactly; the support has 12 sites.

### Agreement table: `k=2 -> 3`

Adding `C=(2,0,0)` gives 17 support sites. Its new star meets the old support
on `{B,C}`; `B` is already represented in both old charts, so the step includes
one nontrivial multi-chart site-cocycle row.

| old target | offset type | shared sites | shared pairs | site binding | Boolean table | edge | class / `J` | path | result |
|---|---|---:|---:|---|---|---|---|---|---|
| `A=(0,0,0)` | axial distance two | 1 (`B`) | 0 | exact | vacuous | vacuous | vacuous | vacuous | agree |
| `B=(1,0,0)` | adjacent | 2 (`B,C`) | 1 | exact | `x XOR c` exact | yes/yes | CNOT / 1 | exact | agree |

The new target again has 21 witnesses, classes `6/12/3`, `J={1,2,0}`, and all
23 words are hosted. Executable outcome: `GLUING_STEP_VERIFIED`.

### Agreement table: `k=3 -> 4`

Adding `D=(1,1,0)` gives 20 support sites. Its new star meets the old support
on four sites. The site `B` belongs to all three old charts and the new chart,
so equality is checked across a four-chart binding.

| old target | offset type | shared sites | shared pairs | site binding | Boolean table | edge | class / `J` | path | result |
|---|---|---:|---:|---|---|---|---|---|---|
| `A=(0,0,0)` | diagonal distance two | 2 | 1 | exact | `x XOR (c_1 AND c_2)` exact | no/no | perpendicular TOF / 2 | exact | agree |
| `B=(1,0,0)` | adjacent | 2 (`B,D`) | 1 | exact | `x XOR c` exact | yes/yes | CNOT / 1 | exact | agree |
| `C=(2,0,0)` | diagonal distance two | 2 | 1 | exact | `x XOR (c_1 AND c_2)` exact | no/no | perpendicular TOF / 2 | exact | agree |

The new target again has 21 witnesses with the same class/J table, and every
word is hosted. Executable outcome: `GLUING_STEP_VERIFIED`.

## C_INDUCTION_STATUS — exact closure

The base is explicit, the local gluing lemma is reduced to all 24 possible
nonempty two-star offsets, each offset agrees, and the two smallest extension
cases agree with an independent reconstruction. Ordinary induction therefore
closes for the exact quantified family of finite P2x-rooted star-glued patches.

The quantifier permits arbitrary finite target count and arbitrary star-glued
shape satisfying the stated ordering. It does not claim every finite subset of
`Z^3`: a finite target family outside that P2x-rooted gluing condition is not
inside this theorem. It also does not pass to `n=infinity`; no such natural
number occurs in finite induction.

No exact obstruction appears at `k=3`, `k=4`, or in the universal local
overlap census.

## D_CONTROLS

### Inputs and imports

| item | class | load-bearing role | control |
|---|---|---|---|
| minimal axioms | zero-input structural | `Z^3`, nearest-neighbour geometry, translations, proper cubic rotations | byte and Git-blob pinned |
| [Cycle-719 controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md) | one computed lattice input | landed basis-state semantics and Manhattan routing | immutable commit, full scripts-tree object, top-module SHA-256 and Git blob pinned |
| P2x root and star-gluing order | explicit finite boundary condition | exact theorem family | declared in the quantifier |
| 23-program family | explicit finite boundary condition | target-local alphabet and word-length cap | exhausted, no sampling |

No observed value, fitted selector, literature value, normalization, probability
weight, new axiom, or new primitive is load-bearing. The primary's literal
current-surface source-read count is one; the independent checker's is three;
both are below the six-file cap. Separately, importing the pinned Cycle-719
core executes a 52-file transitive Python-module closure from the immutable
historical scripts tree `b74e1639fc2a2250c0de2a56ad33665533a22c81`.
The primary receipt enumerates those paths and binds their manifest digest;
this pinned compute closure is not hidden inside the current-surface read
count.

### Outcome-neutral integrity policy

The primary checks construction and reconciliation only. Its science finding
is derived into one of `FINITE_PATCH_INDUCTION_CLOSES_AT_DECLARED_SCOPE`,
`OBSTRUCTED`, or a named hosting/gluing failure without changing bookkeeping
cleanliness. It self-probes a coherent shared-site binding obstruction and a
coherent not-hostable case; both pass its bookkeeping gate with their narrowed
science outcomes.

The independent checker byte-pins the primary source and receipt, binds the
complete canonical primary cache, and independently reconstructs:

- the 23 descriptors, 21 witnesses, proper-cubic action, classes and `J`;
- all 24 relative overlap offsets and their `6/6/12` type census;
- normalized adjacent and diagonal Boolean tables and witness strengths;
- canonical global paths by a separate Manhattan implementation;
- P2x, `k=2 -> 3`, `k=3 -> 4`, support counts and site cocycles; and
- the exact finite quantifier and false infinite-scope flag.

Science agreement is reported data rather than an integrity condition. The
checker rejects twenty-five corruptions covering census counts, pair/path data,
universal flags, case arity/support/outcome, the exact finite quantifier,
infinite-scope flag, artifact pins and cached stdout. It also constructs
coherent `OBSTRUCTED` and `NOT_HOSTABLE`
receipts; both pass the same bookkeeping validator.

For audit-packet classification, this independent checker is review-only
evidence. It does not replace the bounded theorem's primary runner, does not
determine any audit or effective status, and is attached as the primary runner
of the separate meta convention note so its source, receipt, and cache remain
machine-discoverable.

### Artifacts and reproduction

Primary:

- [`frontier_cycle986_patch_uniformity_induction_2026_08_11.py`](../scripts/frontier_cycle986_patch_uniformity_induction_2026_08_11.py)
- [`patch_uniformity_induction_cycle986_receipt_2026_08_11.json`](../outputs/patch_uniformity_induction_cycle986_receipt_2026_08_11.json)
- [`frontier_cycle986_patch_uniformity_induction_2026_08_11.txt`](../logs/runner-cache/frontier_cycle986_patch_uniformity_induction_2026_08_11.txt)

Independent refutation checker:

- [`frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.py`](../scripts/frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.py)
- [`patch_uniformity_induction_cycle986_independent_check_receipt_2026_08_11.json`](../outputs/patch_uniformity_induction_cycle986_independent_check_receipt_2026_08_11.json)
- [`frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.txt`](../logs/runner-cache/frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.txt)

```bash
python3 scripts/cached_runner_output.py --refresh --timeout-sec 1400 scripts/frontier_cycle986_patch_uniformity_induction_2026_08_11.py
python3 scripts/cached_runner_output.py --refresh --timeout-sec 300 scripts/frontier_cycle986_patch_uniformity_induction_independent_check_2026_08_11.py
```

Both caches pin runner SHA-256, literal inputs and their fingerprint, timeout,
exit status and stdout.
Both runners replay deterministically, keep stdout below 6000 bytes, and end in
zero failures. Independent audit remains required before any effective-status
consequence.
