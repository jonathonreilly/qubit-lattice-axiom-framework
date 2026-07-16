# Block-saturated product-reference split handoff and scalar next-activity boundary

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.
**Primary runner:** [`scripts/wilson_staggered_block_saturated_split_handoff_scalar_activity_boundary_2026_07_12.py`](../scripts/wilson_staggered_block_saturated_split_handoff_scalar_activity_boundary_2026_07_12.py)
**Cached output:** [`logs/runner-cache/wilson_staggered_block_saturated_split_handoff_scalar_activity_boundary_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_block_saturated_split_handoff_scalar_activity_boundary_2026_07_12.txt)

## 0. Result

The fixed-product-reference decorated norm from Block42 closes the bounded
local-section part of the earlier strong/weak handoff problem for the **actual
generated residual**. It also exposes the next obstruction more sharply:
aggregate scalar factor smallness at `m=10^44` would be far too weak under a
same-`K` tree-span lift, while a fresh residual-only row at `m=10^46` would
pass that conditional arithmetic. The required diameter-to-tree-span/source-
incidence bridge and the correlated-`S_next` grammar remain unproved.

Use the direct-sum strong/weak split from the
[K-retaining marked-attachment theorem](WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the fixed-product atom algebra from the
[two-horizon intertwining theorem](WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the anchored interaction norm and contractive local projector from the
[declared RG chart](WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md),
the actual enhanced residual row from
[Block42](WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md),
and the center-only output and shortest recursion from the
[extracted `S^(2)` theorem](WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md).

Let `E_0` be the fixed onsite-`G_m`/product-Haar expectation in the Block42
next product dictionary, `L` its fiber-constant injection, and

```text
Pi_empty=L E_0,
Q_0=1-Pi_empty=sum_(S nonempty)Delta_S.                            (0.1)
```

For the actual routed residual carrier define

```text
M_s(F)=sup_z sum_(X contains z) exp(theta_s|X|+Lambda_s diam X)
       sum_(S subset J_X) r_*^|S| ||Delta_S F_X||,

N_bs(F)=sup_z sum_(X contains z) [exp(theta_w|X|+Lambda_w diam X)
        ||(1-P_0)Pi_empty F_X||
       +exp(theta_s|X|+Lambda_s diam X)
        sum_(S nonempty)r_*^|S|||Delta_S F_X||],                  (0.2)
```

with

```text
(theta_s,Lambda_s)=(0.400001,1),
(theta_w,Lambda_w)=(0.0000005,1/2),
r_*=1+sqrt(2).                                                     (0.3)
```

Since the weak carrier weight is no larger than the strong weight,

```text
N_bs(F)<=M_s(F),
||(1-P_0)Pi_empty F||_weak<=M_s(F).                               (0.4)
```

Thus the actual decorated residual has a block-saturated local section with
constant one. This is stronger than the generic constant-three direct-sum
estimate because `M_s` retains the complete fixed-product atom decomposition
at strong spatial weights. The coefficient atom algebra has product constant
one; Block42 separately supplies the spatially anchored `M_s` factor bound on
the actual generated range. Empty atoms are kept, not quotiented out.

Block42 gives at `m=10^44`

```text
B_(2,split)=0.1143355691192827,
K_dec^bd=0.1211282777967557<c=0.2.                               (0.5)
```

Equations (0.2)--(0.4) put this generated residual in the declared linear
split domain. However, conditionally granting `K_tree<=K_dec^bd` in the
marked theorem's tree-span/source-incidence norm gives the arithmetic

```text
D=4.662803929603495,
tau=0.5647974096968162,
A_att=3.740688559840039,
68exp(1/2)K_dec^bd=13.58006022990139>c,
68exp(1/2)A_att=419.3799901057573>1.                              (0.6)
```

For even the scalar factor envelope to lie below `c`, one needs

```text
K_eff<log(1+c)/(68exp(Lambda/2))
     =0.0016262296194422305.                                     (0.7)
```

The `m=10^44` aggregate therefore needs a `74.484117...`-fold effective
reduction before conditional scalar reuse. This is not an actual marked-
response bound and not a no-go for lineage-sensitive or scale-indexed estimates.
The naive generic direct-sum algebra is also too costly:
`3K_dec^bd=0.3633848333902671>c`, so the constant-one atom algebra is
load-bearing for the split, together with Block42's actual-range carrier
estimate.

The predecessor root row is a sharp live target:

```text
K_T2=0.0006173262504064846<(0.7),
exp[68exp(1/2)K_T2]-1=0.07169...<c.                               (0.7a)
```

No current theorem transfers next output-carrier incidence from `K_dec^bd`
back to `K_T2`; proving such a multiscale root-anchor bound without another
factor-`68` loss is precisely a live lineage route, not a result of this note.

The exact conditional target has useful room. If a future theorem proves
`K_eff<=kappa K_T2`, and the worst extended raw potential is bounded by
`B_0<=B_star`, then the factor gate is

```text
kappa<2.628903... with the raw term,
kappa<2.634311... without the raw term.                            (0.7b)
```

At the unproved diagnostic value `kappa=1`, the total potential envelope is
`0.0695846383...`, the factor envelope is `0.072062795...<c`, and the exact
attachment row gives `q_total=exp(-1/2)`. These are targets for a root-anchor
incidence lemma, not claims that such a lemma already exists.

A fresh Block42 rerun at

```text
m=10^46, beta=0, c=0.2,
(theta_s,Lambda_s)=(0.400001,1)                                  (0.8)
```

gives

```text
K_T40=1.228238911464758 10^(-8),
B40=6.171357829397776 10^(-6),
K_T2=6.171376872265679 10^(-6),
B_(2,split)=0.001143007145044298,
K_dec^bd=0.001143660626665446,
tau=0.002115709906776542,
A_att=0.004238836058388475,
q_centered=0.4752288237283523,
q_residual=exp(-1/2)<1.                                          (0.9)
```

Monotonicity licenses substitution of `K_dec^bd` only after a theorem proves
`K_tree<=K_dec^bd`. Block42 controls coarse carrier diameter, whereas the
marked theorem uses hidden tree span. Equation (0.9) is therefore a
conditional scalar diagnostic, not a marked-response theorem.

The exclusions are load-bearing. `P_0` may contain local quadratic and higher
terms. `S_next`, its shortest part `S_next^(2)`, and its normalization are
separate center-only output data. This note does not build the
`S_next`-relative product reference, determinant restore, boundary grammar,
or a Weyl reserve for a projected quadratic update. Consequently (0.9) is not
the next actual bare-range preintegration and not an autonomous RG step.

## 1. Block-saturated section and algebra

For each coordinate, `Delta_empty=E` and `Delta_nonempty=Q=1-E`. Tensoring the
coordinate projections reconstructs every coefficient. At
`r_*=1+sqrt(2)`, the projective weighted atom norm has product constant one.
The fixed `G_m` onsite expectation and normalized Haar expectations are
contractive and symmetry-equivariant in the declared coefficient chart.

The empty term of `N_bs` is the exact extended local section
`(1-P_0)Pi_empty F`; `P_0` was already extracted and the routed parent carrier is
kept rather than shrunk to the visible constant support. No arbitrary choice
of representative occurs. In the declared anchored coefficient chart,
`||1-P_0||<=1`; contractivity of `Pi_empty` and the weight comparison below
therefore control the weak empty arm. For every carrier,

```text
exp(theta_w|X|+Lambda_w diam X)
 <=exp(theta_s|X|+Lambda_s diam X).                               (1.1)
```

Adding the nonempty terms proves (0.4) without a factor two or three.
Coordinate products are formed in the projective coefficient atom algebra,
not in a quotient by `ker E_0`; centered factors may fuse to the empty atom
exactly. Spatial carrier multiplication is not assigned a global
constant-one `M_s` estimate here; the positive carrier bound is the
actual-range Block42 estimate.
`N_bs` is a range-restricted operator handoff and is not claimed to be a
globally submultiplicative algebra norm: weak empty factors can enlarge a
strong centered carrier unless the saturated strong lineage is retained.

Block42's factor bound applies to the complete atom sum, so it simultaneously
bounds the weak empty arm and strong nonempty arm. The finite local jet and
center data are external direct-sum coordinates and are not silently included
in `M_s`.

This closes only the actual-generated-residual version of the local-section
wall identified in the marked-attachment theorem. A generic perturbation
completion would need the same bound uniformly for supplied source directions
and changing center coordinates.

## 2. Exact scalar reuse discriminator

For activity `K<c`, put

```text
s=c-K,
D=sup_(n integer>=1)n exp(-sn),
tau=KD,
a_0=sup_(n integer>=1)exp(-cn)[exp(Kn)-1],
A_att=[a_0+tau/(1-tau)]/(1-tau).                                 (2.1)
```

At fixed `c`, `D`, `tau`, `a_0`, and `A_att` are nondecreasing in `K`: for
each integer `n`, both defining summands increase pointwise, and the final
rational expression increases on `tau<1`. Hence a certified upper bound on
the actual activity may be inserted in (2.1).

At `m=10^44`, the integer maximizers are `n_D=13` and `n_a=8`. Under the named
same-`K` lift, the converted rows in (0.6) fail by large margins. Without that
lift they are downstream arithmetic only. Factor membership `K<c` is not the
next marked contraction theorem.

At `m=10^46`, both conditional converted rows close. This shows that the
arithmetic target is quantitative, but it does not supply the incidence lift
or the full next-center action.

## 3. Shortest-center gain and unchanged-ledger boundary

For the shortest positive center, write `h_j=8k_j/mu_j`. The exact recursion

```text
mu_(j+1)=mu_j-8k_j^2/mu_j,
k_(j+1)=k_j^2/mu_j
```

implies

```text
h_(j+1)=h_j^2/(8-h_j^2).                                        (3.1)
```

At `m=10^44`, the capacity `R_j=-log(C_*h_j)` more than doubles at each of the
first six shortest-center recursions. This is a live mechanism for paying
future path and determinant activities. The aggregate `K_dec^bd`, however,
has discarded lineage depth and does not inherit (3.1) merely by relabeling.

The unchanged fixed-surcharge moment ledger is also finite-horizon. With
`sigma=5log C_*`, it reads

```text
a_(j+1)=(a_j-2c)/2-sigma,
a_j=2^(-j)[a_0+2(c+sigma)]-2(c+sigma).                            (3.2)
```

Every finite `a_0` becomes negative. For the enhanced Block42 input,

```text
18.82747374039086 -> 0.400001 -> -8.813735370195429.              (3.3)
```

Likewise `Lambda_j=Lambda_0/2^j` makes the single-step raw number tend to one.
Equations (3.2)--(3.3) rule out only all-horizon iteration of the unchanged
scalar surcharge/halving certificate. They do not rule out using (3.1) in a
lineage-sensitive activity, a scale-indexed norm, small/large-cluster
decomposition, representation weights, or another physical block.

The next constructive target is the complete `S_next` relative-to-product
grammar. Expand the hidden inverse in

```text
S_next=mu I-R_(2,KI)A_2^(-1)R_(2,IK),
A_2=mu I+R_(2,II),
||R_(2,II)/mu||<=2/(m^2+2),                                      (3.4)
```

localize its paths, assign determinant/restore/boundary ownership once, and
combine that center activity with the residual activity before reusing
(2.1). A separate `P_0^(2)` quadratic projection and Weyl reserve are needed
for an updated interacting center.

## 4. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_block_saturated_split_handoff_scalar_activity_boundary_2026_07_12.py
```

The runner checks a finite fixed-product atom algebra, the block-saturated
split and section inequalities across carrier fixtures, exact reuse of the
Block42 runner, the conditional `m=10^44` scalar failure, the conditional
`m=10^46` scalar closure, the fixed-ledger moment exhaustion, the shortest-center
relative-hopping recursion, and the source/dependency contract.

## 5. Authoritative No-Go Discipline N1--N8

The only negative boundary is

```text
NG43: the unchanged aggregate scalar activity and fixed surcharge/halving
      ledger do not supply an all-horizon actual-range contraction.          (5.1)
```

It is not a claim against lineage-sensitive or alternate-chart closure.

### N1 — alternative-route enumeration

| route | marker | executed result |
|---|---|---|
| Generic constant-three direct-sum estimate | `ATTEMPTED` | Replaced on the actual decorated residual by the constant-one coefficient atom algebra, Block42's anchored carrier bound, and (0.4). |
| Exact empty/nonempty product split | `ATTEMPTED` | Positive: it supplies the block-saturated section without deleting empty fusions. |
| Promote `K_dec^bd<c` directly to marked contraction | `ATTEMPTED` | Rejected: Block42 diameter incidence is not the marked theorem's tree-span incidence; under a same-`K` hypothesis the `m=10^44` arithmetic gives `q=419.38`. |
| Increase the massive witness | `ATTEMPTED` | Conditional arithmetic closes at `m=10^46`, but the incidence lift remains unproved. |
| Use the base gap alone as a product-reference transition | `ATTEMPTED` | Insufficient: contractivity of two expectations is not a local atom-transition or factor-ownership theorem. |
| Repeat the fixed surcharge/halving ledger | `ATTEMPTED` | Equation (3.2) becomes negative for every finite initial moment. |
| Reuse shortest-center squaring on the scalar `K` | `ATTEMPTED` | Insufficient because the aggregate row no longer records path/lineage depth. |

Live routes are **not foreclosed**: Neumann/path localization of (3.4), a
projected quadratic/Weyl reserve, scale-indexed or representation-weighted
norms, small/large clusters, lineage moments, sharper carriers, finite-horizon
mass schedules, and taste-faithful multicomponent blocks.

### N2 — wall-independence audit

Keep six walls:

```text
W1 full next correlated-center/reference/factor grammar and P_0 ownership,
W2 small marked response in that same reference,
W3 horizon-uniform recursion with nondegenerate scale-indexed weights,
W4 generic source embedding and two-mark control,
W5 taste-faithful physical block/chart selection,
W6 critical trajectory, observables, and continuum.                         (5.2)
```

| pair | left=>right? | right=>left? | reason |
|---|---:|---:|---|
| W1--W2 | No | No | A grammar may have large activity; a small residual response does not construct the center grammar. |
| W1--W3 | No | No | One next center is not a uniform recursion; a formal recursion does not prove this factor ledger. |
| W1--W4 | No | No | Base ownership does not embed generic sources; a Hessian does not identify determinants or center updates. |
| W1--W5 | No | No | A positive Hermitian center can be taste-wrong; taste does not supply its norm bounds. |
| W1--W6 | No | No | A massive next step is not critical tuning; continuum matching does not retro-prove the finite ledger. |
| W2--W3 | No | No | One small response is not horizon-uniform; a scale norm need not contract this mark. |
| W2--W4 | No | No | One-mark residual response is not a generic two-mark estimate; the converse also fails. |
| W2--W5 | No | No | Marked smallness does not select taste; taste does not bound the response. |
| W2--W6 | No | No | Ultra-massive response gives no continuum path; a tuned path need not prove this scalar bound. |
| W3--W4 | No | No | Actual-orbit induction does not imply a generic ball; local nonlinear control does not build all scales. |
| W3--W5 | No | No | Recursive locality does not select a physical carrier; taste does not prove recursive estimates. |
| W3--W6 | No | No | A massive induction can remain noncritical; continuum may use another chart. |
| W4--W5 | No | No | Analytic ball control does not identify taste; taste selection does not provide a Hessian. |
| W4--W6 | No | No | A generic massive ball is not critical tuning; a continuum family need not be uniform on that ball. |
| W5--W6 | No | No | Taste selection leaves tuning open; a conditional continuum chart need not prove unique selection. |

### N3 — hidden-condition phrase scan

The authoritative scan covers this note and runner. Dependency residuals are
handled in N4 and prior-cycle mechanisms in N8.

| phrase | classification | action |
|---|---|---|
| `product reference` | declared mathematical chart | Fixed `G_m`/Haar expectations only; not correlated `S_next`. |
| `block-saturated` | defined norm | Equation (0.2), not a physical blocking selector. |
| `actual generated residual` | orbit restriction | Generic perturbations remain W4. |
| `canonical` | product-coordinate projector language | No physical uniqueness is implied. |
| `background` | zero pre-table hit | Its appearance here is self-reporting, not a premise. |
| `we assume`; `by construction`; `as is standard`; `the framework provides`; `bridge context`; `naturally`; `obviously`; `standard QFT`; `registered` | zero pre-table hits | Their appearance in this row is self-referential scan reporting. |

No hidden admission changes W1--W6.

### N4 — residual matching

| dependency | witness lines | witness residual | present use | match? |
|---|---|---|---|---:|
| Marked attachment | `docs/WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md:78-121,181-211,264-318` | Tree-span strong split, attachment envelope, local-section wall | `N_bs` embedding and explicitly conditional scalar reuse | Yes, without identifying diameter and tree-span rows |
| Two-horizon atom algebra | `docs/WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md:152-201,226-284` | Fixed-product atoms, empty fusion, product constant one | Coefficient atom algebra used inside `M_s`, and the linear section | Yes |
| Declared RG chart | `docs/WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md:69-174` | Anchored interaction norm and `||1-P_0||<=1` | Weak empty-arm section | Yes |
| Block42 | `docs/WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md:43-76,142-176,291-304` | `5|X|` decorated residual row and finite-horizon recurrence | Actual factor input and scalar boundary | Yes |
| Extracted `S^(2)` | `docs/WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md:257-278,350-363` | Center-only `S_next`, shortest recursion, and weak-output boundary | Equation (3.1), direct-sum exclusion, and next target | Yes |

### N5 — rhetoric and resolution audit

| resolution | tested? | supported statement |
|---|---:|---|
| One product coordinate | Yes | Exact empty/nonempty reconstruction. |
| One routed carrier | Yes | `N_bs<=M_s` with weak/strong weights. |
| One actual generated residual | Yes | Block42 factor membership and Block43 section. |
| One product-reference marked response | No | Only conditional downstream arithmetic; the incidence bridge is unproved. |
| Full next correlated-center action | No | W1--W2 remain open. |
| Every horizon | No | Only unchanged scalar ledger exhaustion is proved. |
| Generic perturbation ball | No | W4 remains open. |
| Critical continuum | No | W6 remains open. |

### N6 — partial-closure and primitive scan

The product dictionary, local section, running center, projected quadratic
coordinate, and scale-indexed norm are constructive chart mathematics. They
are not axioms or new primitives. No registered premise is being reclassified
as a wall. A future imported physical block would require explicit bounded
scope and an import-retirement path; none is silently used here.

No axiom-update stop is established. Such a stop would require an audited
theorem excluding every axiom-compatible local section, reference, block, and
norm route, or a contradiction between the axioms and a required empirical
limit. The present scalar-certificate boundary is far narrower.

### N7 — hostile steelman

A hostile reviewer of the negative boundary should emphasize that (3.1)
contains double-exponential locality gain which the scalar `K` row discarded.
Neumann localization can restore path length, small/large splitting can spend
massive tails only where needed, and a scale-indexed norm can avoid repeating a
fixed per-site surcharge. They are right; NG43 does not foreclose those routes.

A hostile reviewer of the positive result should emphasize that even (0.9)
uses a tree-span/source incidence not supplied by Block42's diameter row, and
also omits the `S_next` reference, determinant/boundary factors, `P_0`
quadratic update, and generic perturbations. They are right; the positive
theorem is only the actual-range linear split embedding.

### N8 — cross-cycle echo

| earlier wall | mechanism/status | present effect | residual |
|---|---|---|---|
| Raw lifted unit directions | geometric factor-two support | Empty/raw arm can be weakly carried | Nonfiber factors need attachment. |
| Unlocalized Cauchy bound | K-retaining forced attachment | One-step strong-to-weak response | Same reference and next-level handoff were missing. |
| Generic direct-sum section | block-saturated fixed-product atoms | Actual residual section closes with constant one | Generic/changing-center section remains W1/W4. |
| Weak-completion identity mismatch | enhanced actual-base moments | One strong decorated factor return | Fixed ledger cannot repeat. |
| Base-center gap | shortest-center squaring | Live double-exponential path gain | Aggregate scalar K loses lineage depth. |
| Scalar factor smallness | conditional reuse discriminator | Same-`K` arithmetic fails at `10^44` and closes at `10^46` | Tree-span incidence and full correlated-center activity remain W1. |
| Taste and continuum | open | Not addressed | W5--W6 remain. |

**No-Go Discipline verdict:** PASS WITH BOUNDED CLAIMS for the actual-residual
block-saturated linear section, the conditional scalar diagnostics, and the
unchanged-scalar-ledger boundary. Fail any reading as a marked-response
theorem, next full RG step, all-horizon closure, generic invariant ball, or
continuum theorem.
