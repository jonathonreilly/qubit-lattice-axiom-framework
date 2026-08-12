# Finite ambient-versus-domain symmetry split of the open-box static assembly — Cycle 720

Date: 2026-08-02

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit status is set only by the independent audit lane.
Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every
such object is named as supplied. The floating-point rows are conditional on the
fixed, landed Cycle-696 compiler contract inventoried below; that compiler is a
landed but audit-excluded support surface, not an independent audit authority.

**Primary runner:**
[`scripts/physical_ambient_domain_symmetry_split_cycle720_2026_08_02.py`](../scripts/physical_ambient_domain_symmetry_split_cycle720_2026_08_02.py);
cached stdout
[`logs/runner-cache/physical_ambient_domain_symmetry_split_cycle720_2026_08_02.txt`](../logs/runner-cache/physical_ambient_domain_symmetry_split_cycle720_2026_08_02.txt);
paired receipt
[`outputs/physical_ambient_domain_symmetry_split_cycle720_2026_08_02_receipt_2026-08-02.json`](../outputs/physical_ambient_domain_symmetry_split_cycle720_2026_08_02_receipt_2026-08-02.json).

**Independent checker:**
[`scripts/physical_ambient_domain_symmetry_split_cycle720_independent_check_2026_08_02.py`](../scripts/physical_ambient_domain_symmetry_split_cycle720_independent_check_2026_08_02.py);
cached stdout
[`logs/runner-cache/physical_ambient_domain_symmetry_split_cycle720_independent_check_2026_08_02.txt`](../logs/runner-cache/physical_ambient_domain_symmetry_split_cycle720_independent_check_2026_08_02.txt).
It reconstructs the signed permutations and endpoint slot maps, forms orbit and
value-equivalence partitions by graph traversal, and obtains inverse diagonals
from the spectral identity `diag(Q^-1)_i = sum_k |u_ik|^2/lambda_k` rather than
calling the primary's dense-inverse path.

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "separate the finite measured ambient-frame clustering from the finite measured domain level-set partition on the supplied Cycle-696 compiler"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "derive exact stencil-level ambient invariance, or test additional declared domains and box sizes without promoting the current finite census"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact finite signed-permutation identities and an exact conditional restriction lemma; numerical five-domain census for the supplied Cycle-696 compiler at L=3,4,5 and stated tolerances"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the group identities are exhaustive finite arithmetic, while the ambient invariance, level partitions, and four-class attainment are bounded numerical compiler evaluations"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target and obligation graph

**Exact target.** Establish the exact order-12 signed-permutation structure and
the exact conditional fact that restricting a matrix after an exact ambient
symmetry preserves the corresponding frame coincidence. On the supplied
Cycle-696 compiler, test the ambient invariance tolerance and the level/orbit and
frame-cluster partitions for five named domains at each `L in {3,4,5}`.

**Obligation graph.** A enumerates the finite signed-permutation group. R1 checks
the relabelling representation against the compiler. B measures the compiler's
ambient near-invariance. C–G independently classify domain-preserving maps,
inverse-diagonal level sets, frame clusters, centre-reflection census, and blind
slots on the fifteen rows. R3–R5 are wrong-convention and perturbed-matrix
controls. The algebraic restriction lemma uses exact ambient invariance as an
explicit hypothesis; the numerical layer establishes only tolerance-resolved
facts on the declared rows.

**Strongest missing lemma.** The packet does not derive exact stencil-level
sextet or centre-reflection invariance of the compiler. Therefore it proves no
exact four-class result for the actual compiler outside the measured rows, no
arbitrary-domain converse for the level partitions, and no arbitrary-`L` law.

## Summary

Cycle 719 measured, on the full open box, that the level sets of the diagonal of
the static assembly's matrix inverse are exactly the orbits of an order-12 set,
and that this set is larger than the order-6 rotation stabilizer of the body
diagonal because it also contains the box-centre point reflection. That left a
direct question: **does an assembly whose box is not centre-symmetric lose the
improper half and restore 24 distinct level sets?** This cycle answers it on five
domain types at three box sizes, and the answer separates into three parts.

First, in the finite census, truncating the box to a corner simplex or to a
slab does reduce the symmetry available inside the order-12 set — from `12` on the
full box, to `6` on every corner simplex, to `2` on the slab — but the reduction
is accompanied by an equal determinant split: `12 = 6 + 6`,
`6 = 3 + 3`, `2 = 1 + 1`, proper and improper, in all fifteen measured rows. None
of these fifteen rows has a purely proper domain-symmetry subgroup.

Second, the measured truncated-domain level sets are finer, but their count is not
fixed at `24`. On the full box
the count of distinct levels sits strictly below the count of orbits of the
axis-permutation direct factor alone — `13` against `25` at `L = 3`, `34` against `64` at
`L = 4`, `66` against `130` at `L = 5`, a deficit of `12`, `30`, `64`. On every
truncated domain that deficit is `0`: the level count, the permutation-orbit
count, and the full domain-orbit count coincide. In this census removal of the
centre reflection accompanies removal of the pairwise merge. The recovered count
is the axis-permutation-factor orbit count, which is a property of the domain, not
the number `24`.

Third, **the measured frame label remains four-valued on all fifteen rows.**
Across all five domains and all three box sizes the `24` restricted
assemblies fall into exactly `4` classes, coinciding within `1.243450e-10` and
separated across classes by `4.000000e+00`. The within-class figure is *identically*
the ambient assembly's measured symmetry tolerance. The exact companion lemma is
conditional: if `s` is an exact symmetry of an ambient `Q`, then the restricted
assembly at frame `sg` equals the one at frame `g`, because relabelling acts on `Q`
before restriction. For the supplied floating-point compiler, sections B and E
establish the corresponding tolerance-resolved statement only on the declared
boxes and domains. Thus this census separates a stable ambient contribution from
the domain-dependent level partition without claiming exact stencil invariance or
an arbitrary-domain classification.

## Improper-frame framing

The runner executes six improper signed permutations — the three odd axis
permutations and the three negated even ones — alongside the six proper members of
the same order-12 set. These are bookkeeping, not physics: improper (det = -1)
signed permutations are NOT axiom symmetries — the Lattice axiom names proper
cubic rotations only. They enter this note ONLY as derived
computational identities of the compiled chain (exact slot relabelings composed
with the coincidences measured here), and every physical frame-scope statement in
this note is over the 24 proper rotations. Nothing in this cycle enlarges the
framework's symmetry group, and no statement below counts frames outside the 24.
The order-12 set is never named as a symmetry group of the framework; where the
note calls it a group it means the closure property verified as an exact integer
matrix identity in section A.

## Setup

The compiled chain is the landed
[Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py),
used verbatim and never re-implemented:

```
idx   = c696.static_variable_index(L, wrap=False)
Q     = c696.assemble_static_hessian(L, wrap=False)["Q"]
smap  = c696.frame_site_map(L, R)
```

`idx` maps a slot key `(c, x)` — a spatial class `c` in
`c696.SPATIAL_CLASSES` and a site key `x` — to a variable index; `Q` is the
symmetric static-sector matrix on those variables. Box sizes are `L = 3, 4, 5`
with slot counts `98`, `279`, `604`. Frames are `c696.c576.FRAMES`, the 24
proper cubic rotations; the identity sits at index `23`.

The seven spatial class directions carried by `c696.regge.DIRS15` are all
non-negative, so the stored site key of a slot is that edge's low corner. For a
signed permutation `R` of the axes the induced **slot relabelling** is

```
w  = R @ dir(c)
y  = R @ x + t(R) + min(w, 0)      with t(R)[a] = (L-1) if R[a].min() < 0 else 0
```

sending slot `(c, x)` to slot `(class(|w|), y)`. The shift `t(R)` and the
`min(w, 0)` correction are what convert the compiler's site-centred convention
into the low-corner convention that the slot key uses; section R1 verifies the
two agree exactly on integers, for all 24 frames at all three box sizes.

Write `m_g` for the relabelling of frame `g`. The **sextet** is
`S = (1, 4, 9, 15, 18, 23)`, the six proper rotations fixing the line through
`(1, 1, 1)`. The **centre reflection** is the relabelling of `-I`, which in slot
terms sends `(c, x)` to `(c, ((L-1) - x_a - |w_a|)_a)`. The order-12 set of
section A is generated by the six axis permutations together with that reflection.

### Restriction to a sub-domain

A domain `D` is a subset of the slot indices. The **restricted assembly** at
frame `g` is the principal submatrix

```
Q_g[a, b] = Q[ m_g[D_a], m_g[D_b] ]
```

and the value functional is the diagonal of its matrix inverse,
`v_i(g) = (Q_g^{-1})_{ii}`. Algebraically, taking a principal submatrix holds
every coordinate outside `D` fixed at zero increment. No claim equates that
operation to re-assembling the compiler on a different physical region: no
re-assembly on a smaller box is performed, and the ambient stencil is never
modified. Five domains
are used at each box size:

- **full box** — every slot;
- **corner simplex `K`** for `K = 2, 3, 4` — slots with `sum(x) + sum(dir(c)) <= K`;
- **slab `x <= 1`** — slots with `x_0 + dir(c)_0 <= 1`.

The corner simplices are the interesting case: a simplex cut off at the origin
corner is manifestly not centre-symmetric, while it retains the full permutation
symmetry of the three axes. The slab retains only the exchange of the two axes it
does not cut.

### Imported compiler contract

The following are supplied inputs, not outputs of this cycle:

- the open spatial box, `wrap = False`, the `L_T = 2` periodic tick fold, and the
  static-sector Regge Hessian construction;
- the slot index convention, the spatial class list, the fifteen direction
  entries, and the site-centred frame map, all read from the landed compiler;
- the selected box sizes `L = 3, 4, 5`, the corner cuts `K = 2, 3, 4`, the slab
  cut `x <= 1`, and every numerical gate tolerance in the runner;
- the sextet membership list, carried forward from the landed cycle-707 coset
  work and re-verified here as an exact matrix identity.

There is no measured, fitted, or literature constant imported by this cycle. The
matrix `Q` is indefinite; no positivity, ordering, or eigen-decomposition property
of it is used or claimed anywhere below, and the value functional is a diagonal of
a matrix inverse only.

## Claims

### A. The order-12 set is a direct product whose proper half is the sextet

Over the six axis permutation matrices `P` and their negatives `-P`, the resulting
`12` matrices are **distinct**, `6` are proper and `6` improper, the set is closed
under composition, and the centre reflection commutes with every member. The
proper half is **exactly** the cycle-719 sextet, and it is exactly the graph of the
sign character: a member `P` is proper when the underlying permutation is even, and
`-P` is proper when it is odd. All four statements are exact integer matrix
identities, reported as

```
A order-12 set: distinct 12 proper 6 improper 6 | proper half is the cycle-719 sextet True
A the proper half is the graph of the sign character True | composition-closed True | centre reflection central True
```

The structural consequence used for the enumerated rows is that the proper half is a **diagonal**
subgroup, not a direct factor. The order-12 set splits as a product of the axis
permutations with the two-element set generated by the centre reflection, but the
proper members are not one of those two factors — they are the graph of a
character. Any subgroup that contains an improper element has equally many proper
and improper elements because determinant restricts to a surjection onto
`{+1,-1}`. A subgroup contained in the determinant kernel can of course be purely
proper; this packet neither excludes nor classifies domains realizing that case.

### R1. Anchor: the generic relabelling reproduces the landed site map exactly

The site component of the relabelling defined above agrees with the landed
`c696.frame_site_map(L, R)` at mismatch `0`, for all 24 frames at `L = 3, 4, 5`;
all `25` slot maps used per box size are bijections; and the map is a homomorphism,
with `m_{ab} = m_a[m_b]` at composition mismatch `0` over all `576` frame pairs:

```
R1 site map vs compiler 0 | slot bijections 25/25 | composition mismatch 0
```

This is a discriminating anchor, not a restatement. The compiler's map is the
affine site action `s -> R(s - c) + c` about the box centre `c`; the relabelling
above is a low-corner action with an integer shift `t(R)`. That the two agree is a
theorem: component `a` of `(I - R)c` is `((L-1)/2)(1 - sum_b R[a,b])`, and since row
`a` of a signed permutation carries exactly one entry `+1` or `-1`, that sum is `+1`
or `-1`, giving `0` or `(L-1)` respectively — which is precisely `t(R)[a]`. The
gate would fail against any other convention, and the six improper members have no
counterpart in the compiler at all, so their relabellings stand on the derived
identity alone.

### B. Ambient tolerance of the assembly

Before any restriction, the ambient assembly's own symmetry is measured. Each
sextet member and the centre reflection leave `Q` invariant to

```
B ambient sextet dev 1.243450e-10 centre-reflection dev 1.243450e-10 | entry max 2.945214e+01 | non-sextet floor 4.000000e+00
```

and this line is **identical at `L = 3, 4, 5`** — the deviation does not grow with
the box. Against a largest entry of `2.945214e+01`, the symmetry holds to about ten
orders of magnitude, while the eighteen proper rotations outside the sextet deviate
by at least `4.000000e+00`. That floor is the rejector for this section: the
tolerance is not a loose threshold that any frame would pass.

### C. Each of the fifteen measured domain-symmetry groups is half improper

For each domain, the members of the order-12 set that map `D` onto itself and
leave the restricted matrix invariant are counted, split by determinant. The
result across all fifteen rows is

- **full box**: `12 = 6 + 6`;
- **corner simplex `K = 2, 3, 4`**: `6 = 3 + 3`;
- **slab `x <= 1`**: `2 = 1 + 1`.

The corner simplex is the intended non-centre-symmetric test, and it behaves as
designed — the centre reflection is gone, the order drops from `12` to `6`. But the
surviving six are not the six proper rotations. They are the three even
permutations together with the three negated odd ones: the same graph-of-a-character
structure as in section A, now restricted to the subgroup that preserves
`sum(x) + sum(dir(c)) <= K`. The slab, cut on one axis, keeps only the identity and
the exchange of the other two, and again splits `1 + 1`.

Thus, for these twelve truncations, removing centre symmetry halves the measured
group while preserving equal proper/improper counts. This census does not exclude
other cuts whose surviving subgroup lies entirely in the proper determinant
kernel.

### D. Level sets are exactly the domain-symmetry orbits

For each domain, the slots are partitioned into orbits under the domain's own
symmetry group, and the value functional's distinct levels are counted at a
dedup tolerance of one part in `10^7`. In all fifteen rows the two counts agree, and the
partition is the same one: values within an orbit coincide, values across orbits
separate. Representative rows:

| box | domain | slots | levels = orbits | within-orbit | smallest gap |
|---|---|---|---|---|---|
| `L = 3` | full box | `98` | `13` | `2.391640e-11` | `4.286579e-05` |
| `L = 3` | corner `K = 2` | `15` | `4` | `2.081668e-17` | `1.951044e-04` |
| `L = 3` | corner `K = 4` | `70` | `17` | `4.718448e-16` | `1.077019e-05` |
| `L = 3` | slab `x <= 1` | `57` | `33` | `2.775558e-16` | `2.874069e-06` |
| `L = 4` | full box | `279` | `34` | `7.638064e-10` | `1.264701e-04` |
| `L = 4` | corner `K = 4` | `91` | `21` | `6.217249e-15` | `8.983150e-06` |
| `L = 4` | slab `x <= 1` | `115` | `64` | `4.024558e-16` | `1.705615e-06` |
| `L = 5` | full box | `604` | `66` | `4.591440e-09` | `1.750560e-05` |
| `L = 5` | corner `K = 4` | `94` | `22` | `2.664535e-15` | `3.428924e-05` |
| `L = 5` | slab `x <= 1` | `193` | `105` | `2.220446e-15` | `3.660977e-06` |

The claim gated is scale-free, not an absolute bound: the largest within-orbit
spread must fall below the dedup tolerance, the smallest level gap must exceed it,
and their ratio must clear `10^3`. Over every row,

```
D0 over all rows: largest within-orbit spread 4.591440e-09 smallest level gap 1.705615e-06 smallest ratio 3.812660e+03
```

so the worst separation in the whole table is better than three thousand to one.
The largest within-orbit spread, `4.591440e-09` on the `L = 5` full box, is the
ambient tolerance `1.243450e-10` carried through the matrix inverse of a `604`-slot
indefinite matrix; its size is measured, not derived, and no constant is fitted
anywhere in this cycle.

**The truncation effect.** Compare the level count against the orbit count of the
axis-permutation direct factor alone. This is **not** the proper half: three of the
six axis-permutation matrices have determinant `-1`. The comparison removes the
central-reflection factor, which is the operation relevant to the observed merges:

| box | domain | permutation orbits | levels | deficit |
|---|---|---|---|---|
| `L = 3` | full box | `25` | `13` | `12` |
| `L = 4` | full box | `64` | `34` | `30` |
| `L = 5` | full box | `130` | `66` | `64` |
| `L = 3` | corner `K = 2`, `K = 3`, `K = 4` | `4`, `10`, `17` | `4`, `10`, `17` | `0` |
| `L = 4` | corner `K = 2`, `K = 3`, `K = 4` | `4`, `11`, `21` | `4`, `11`, `21` | `0` |
| `L = 5` | corner `K = 2`, `K = 3`, `K = 4` | `4`, `11`, `22` | `4`, `11`, `22` | `0` |
| `L = 3`, `4`, `5` | slab `x <= 1` | `33`, `64`, `105` | `33`, `64`, `105` | `0` |

On the full box the merge relative to the axis-permutation factor is real and
large. On every truncated domain in this census it is absent: the deficit is `0`
in all twelve rows. Thus their tolerance-resolved level partitions recover the
axis-permutation-factor orbit count, a geometric property of the cut ranging from
`4` for the smallest corner to `105` for the largest slab. This is a finite-census
statement, not a universal converse.

### E. The frame label has four classes on every measured domain

The `24` restricted assemblies `Q_g` are classified by pairwise agreement. On
every domain and every box size the result is the same:

```
cls 4 coset 1.243450e-10 cross 4.000000e+00
```

Four classes, members agreeing to `1.243450e-10`, distinct classes separated by at
least `4.000000e+00` — a ratio of about `3` times `10^10`. The classes are the
right cosets of the sextet, and the within-class figure is *numerically identical*
to the ambient assembly's own symmetry deviation measured in section B. Truncation
changes the number of level sets by up to a factor of two and changes nothing at
all about the number of frame classes.

### F. In the finite census, the merge is equivalent to centre-reflection membership

Sections C, D and E are tied together by a single gate: in all fifteen rows, the
centre reflection belongs to the domain's symmetry group **if and only if** the
level-count deficit is positive. It is present on the three full-box rows, whose
deficits are `12`, `30`, `64`; it is absent on the twelve truncated rows, whose
deficits are all `0`. There is no row where the reflection is present and the
levels are unmerged, and none where it is absent and they merge anyway.

The forward mechanism is exact under its stated hypothesis: centre-reflection
domain symmetry identifies its orbit partners, while exact sextet ambient
invariance would identify frames after every restriction. The converse—absence of
reflection implies absence of accidental equalities—is numerical evidence on these
fifteen rows, not an arbitrary-domain theorem. For the supplied compiler all
symmetry statements retain the measured tolerances of sections B–E.

### G. Truncation reduces blind slots without refining the label

A slot is **blind** in this packet when its value is the same under one
representative of each of the four measured right-coset frame classes.
Comparing the ambient count against the restricted count on the *same* slot set:

- `L = 3`: corner `K = 3` goes `3 -> 0`; corner `K = 4` goes `6 -> 0`; slab goes `5 -> 1`;
- `L = 4`: corner `K = 4` goes `3 -> 0`; slab goes `3 -> 3`;
- `L = 5`: corner `K = 4` goes `0 -> 0`; slab goes `1 -> 1`.

Across these fifteen comparisons truncation reduces blindness or leaves it fixed.
The full-box rows are the control and agree trivially — `6 -> 6`, `19 -> 19`,
`12 -> 12` — as they must, since there the restricted assembly is the ambient one.
The contrast with section E is the point: the per-slot blindness is a boundary
effect and truncation removes some of it, while the four-fold frame label is not a
boundary effect and truncation removes none of it.

### Wrong-value rejectors

Three rejectors establish that the gates above discriminate:

```
R3 reversed composition differs on 456/576 frame pairs | R4 bumped-diagonal survivors 2/6 at 1.000000e+00 | R5 other-side grouping 4.000000e+00
```

- **R3** — the index map is a homomorphism in the convention `m_{ab} = m_a[m_b]`
  and not in the reversed one; the two differ on `456` of `576` frame pairs, so
  R1's composition gate is a real constraint on the convention.
- **R4** — adding a unit to one diagonal entry inside the domain drops the corner
  simplex's symmetry survivors from `6` to `2`, with the failing members deviating
  by `1.000000e+00`; section C's symmetry test therefore fails on a perturbed
  matrix and is not an identity of the relabelling alone.
- **R5** — grouping the frames by the other-side cosets instead of the right cosets
  produces a deviation of `4.000000e+00` where the correct grouping gives
  `1.243450e-10`; section E's four classes are the right cosets specifically.

## Derivation sketch

The whole cycle turns on where a relabelling acts relative to where a restriction
is taken.

Let `s` be a relabelling with `Q[m_s[u], m_s[v]] = Q[u, v]` for all slots `u, v` —
an ambient symmetry. Then for any domain `D` and any frame `g`,

```
Q_{sg}[a, b] = Q[ m_{sg}[D_a], m_{sg}[D_b] ] = Q[ m_s[m_g[D_a]], m_s[m_g[D_b]] ] = Q_g[a, b]
```

using the homomorphism property gated in R1 and the exact ambient-symmetry
hypothesis. `D` appears only as a passive index list, so this conditional identity
holds for every `D` simultaneously. If the sextet is an exact ambient symmetry,
`g -> Q_g` is constant on right cosets `S·g` and has at most four classes. For the
actual floating-point compiler, section B supplies near-invariance rather than an
exact premise; section E independently measures four tolerance-resolved classes on
the fifteen declared rows.

The level sets obey the opposite rule. `v_i(g)` is a functional of `Q_g`, so a
relabelling permutes the values within a fixed `g` only when it maps `D` to itself.
That is a condition on the domain, and it is exactly what sections C and D count.
Within the measured rows the centre reflection is an ambient near-symmetry and is a
domain symmetry only for the full boxes. Section F records that its membership and
the observed deficit agree on all fifteen rows; it does not promote this finite
agreement to an arbitrary-domain converse.

The corner simplex is the sharp case because it separates the two roles cleanly:
it destroys centre symmetry of the domain — restoring the level sets — while
leaving the ambient assembly, and therefore the frame label, untouched.

## Honest boundary

- Five domain types at three box sizes is a finite census, not a classification. No
  statement is made here about domains outside `{full box, corner simplex, slab}`,
  and in particular no domain has been exhibited whose symmetry group inside the
  order-12 set is purely proper. Section A proves only that a subgroup containing
  any improper element has an equal determinant split. A domain whose surviving
  symmetry lies inside the proper determinant kernel is not excluded and is named
  as a next path below.
- The four-class count is a measured attainment of a derived upper bound. The bound
  `4` follows from the coset argument; that the four classes are separated by
  `4.000000e+00` rather than coinciding further is measured, not derived.
- Every deviation quoted is conditional on this fixed compiler, this slot
  convention, and these tolerances. The `1.243450e-10` ambient figure is a property
  of the landed static assembly's floating-point construction; its stability across
  `L = 3, 4, 5` is measured and not explained here.
- The value functional is a diagonal of a matrix inverse of an indefinite matrix.
  No ordering, positivity, or eigen-structure statement is made or used, and none
  should be read into the level-set language: a "level" here is a coincidence class
  of diagonal entries, nothing more.
- Improper elements are computational identities of the compiled chain only, per
  the framing section above. The order-12 set is not proposed as a symmetry of the
  framework, and the physical frame scope remains the 24 proper rotations.
- Nothing in this cycle touches any coupling, amplitude, normalization, or the
  status of the source-response chain; no dial is set and no constant is fitted.

## The next paths opened

- **Cut the axis permutations, not the centre.** Every domain in this family keeps
  either all three axes symmetric or exactly two. The next path opened is a domain
  whose symmetry inside the axis permutations is trivial or of order three — a
  wedge or a skew cut — to test whether the level count reaches the slot count and
  whether the measured four-class frame label survives. This is an open test, not a
  consequence claimed by the present finite census.
- **Perturb the ambient stencil instead of the domain.** Section F localizes the
  four-class label in the ambient assembly. The next path opened is to modify `Q`
  itself — a boundary-weighted or anisotropic static assembly whose sextet symmetry
  is broken at a controlled size — and to measure whether the class count moves off
  `4` continuously in that breaking, which would turn the label into a measurable
  rather than a discrete artifact.
- **Derive the centrality of the centre reflection from the stencil.** Section A
  verifies centrality as an integer matrix identity over the order-12 set, and
  section B measures that the reflection is an ambient symmetry of `Q`. The next
  path opened is the second question left by cycle 719: whether that ambient
  symmetry follows from the six-neighbour stencil's own construction rather than
  being measured on the assembled matrix.
- **Bound the propagated tolerance.** The within-orbit spread grows from
  `2.391640e-11` to `4.591440e-09` between `L = 3` and `L = 5` while the ambient
  figure holds at `1.243450e-10`. The next path opened is a growth law for that
  propagation in the slot count, which would let the separation ratio be predicted
  rather than measured at each box size.

## Relation to the preceding cycle

Cycle 719, [the finite full-box level-set and centre-reflection census](PHYSICAL_LEVEL_SET_ORBIT_LAW_IMPROPER_CENTER_IDENTITY_CYCLE719_NOTE_2026-08-02.md),
measures the antecedent full-box result. It is contextual rather than load-bearing:
Cycle 720 independently reconstructs the signed-permutation set, compiler maps,
ambient tolerance, and all full-box counts it uses. The Cycle 719 boundary is also
preserved here: its numerical stencil invariance is not promoted to exactness or
arbitrary `L`.

## Runner

The [Cycle720 runner](../scripts/physical_ambient_domain_symmetry_split_cycle720_2026_08_02.py)
executes every gated and diagnostic row above and reports

```
TOTAL: PASS=98 FAIL=0
```

with exit code `0`. Two consecutive runs produce byte-identical standard output and
a byte-identical receipt. The receipt is
written to
`outputs/physical_ambient_domain_symmetry_split_cycle720_2026_08_02_receipt_2026-08-02.json`
and carries no timestamp, no wall clock, no host name, and no absolute path, so it
is comparable across machines. SHA- and declared-input-bound stdout for the primary
and independent checker is preserved under `logs/runner-cache/` at the paths above.

Every floating-point number quoted in this note is the runner's own measurement in
the run that produced that `TOTAL` line; none is copied from an earlier probe.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
- [Cycle 707](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)

Cycle 700 and Cycle 707 are landed. The linked Cycle-696 compiler is a landed
support surface excluded from audit scope, cited for its code contract only and
carrying no authority over any claim above.
