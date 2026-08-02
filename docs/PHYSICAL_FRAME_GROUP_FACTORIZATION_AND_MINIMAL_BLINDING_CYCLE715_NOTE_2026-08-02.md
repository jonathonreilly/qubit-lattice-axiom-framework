# The frame group factors through the zero-defect stabilizer: the reassembled operator lives on four cosets, and minimal frame-blinding has order four — Cycle 715

Date: 2026-08-02

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every
such object is named as supplied. The floating-point rows are conditional on the
fixed, joined Cycle-696 compiler contract inventoried below; that compiler is a
landed but audit-excluded support surface, not an independent audit authority.

Earlier cycles in this lane measured the mixed-frame assembly defect of the
Cycle-696 static assembly and found two four-fold structures that looked
unrelated: a source-side stabilizer quartet governing the endpoint sign law, and
an assembly-side collapse of one source's pairing onto four values. This cycle
identifies them as complementary halves of a single exact factorization of the
24 proper rotations, and converts the four-fold count from a measurement into an
index. Three statements are executed. First, the six frames that reassemble the
operator unchanged form a subgroup `S` of order 6, the four-element source
stabilizer of the sign law meets it in the identity alone, and the product map
is a bijection onto all 24 — so the rotations factor exactly as `S . C4`. Second,
the reassembled operator *itself*, not merely one supplied source's pairing, is
constant on each right coset of `S`: measured to `1.2e-10` against an operator
scale of `29.5` at `L = 3` and `L = 4`, while the four coset representatives are
separated by `4.0000`. There are therefore exactly four distinct reassembled
operators, and the count four is the index `24 / 6`. Third, averaging a supplied
source over a subgroup `H` makes its pairing frame-blind exactly when the product
set `S . H` is the whole rotation group, equivalently when `|H| = 4 |H meet S|`;
this is verified against the measured blindness in `30 / 30` subgroups at both
sizes, with a separation factor of `2.2e+09` at `L = 3`. The counting identity
forces a minimal blinding order of four, attained by exactly four of the thirty
subgroups — one of which is the sign law's own source stabilizer.

## Setup

The static spatial sector of the Cycle-696 open-coframe assembly is used as a
fixed, supplied support surface. For a proper rotation `g`, the coframe
relabelling `m_g` acts on the degree-of-freedom index by composing the frame's
site map, the class relabelling `v -> |g v|`, and the negative-part anchor shift;
the reassembled operator is `Q_g = P_g Q P_g^T` for the permutation `P_g` induced
by `m_g`. Nothing in this cycle introduces a new operator, source, coupling, or
normalization: `Q`, the relabelling, and the rotation list are all read from the
supplied compiler.

Two index sets are then measured rather than assumed. The set `S` of frames with
`Q_g = Q` to `1.0e-09` is computed directly from the assembled operator, and the
four-element set `C4` is generated as the powers of the single x-axis rotation
`[[1,0,0],[0,0,-1],[0,1,0]]`. No membership list is hard-coded as an input to
any claim below.

### Imported compiler contract

`scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`
supplies `assemble_static_hessian`, `static_variable_index`, `frame_site_map`,
the 24-frame list, and the 15-direction class table. Finite-difference step and
the open-box admission rule are the compiler's, unchanged. The residual floors
quoted below (`1.2e-10`, `1.1e-11`, `1.8e-10`) are that compiler's
finite-difference residual, not a claim tolerance chosen here.

## Claims

### The rotations factor exactly through the zero-defect stabilizer

The measured zero-defect set is `{1, 4, 9, 15, 18, 23}` with the identity frame
`23` among it; it has order 6 and is closed under composition in `36 / 36`
ordered products, hence a subgroup `S`. The generated quartet `C4` coincides with
the source stabilizer of the supplied sign law, has order 4, and meets `S` in the
identity alone. The product map `S x C4 -> Rot` is a bijection onto all 24 proper
rotations, so `C4` is a transversal for the right cosets of `S` and the index of
`S` is `24 / 6 = 4`.

The factorization is not automatic for order-4 subgroups. The rejector
`{0, 4, 19, 23}` is a subgroup of order 4 that meets `S` twice; its product with
`S` covers only `12` of the 24 rotations, so it is not a transversal.

### The reassembled operator is a function on the four right cosets

From the composition law of the relabelling — `P_a P_b = P_{ba}`, an
anti-homomorphism — it follows for `s` in `S` that
`Q_{s a} = P_a (P_s Q P_s^T) P_a^T = P_a Q P_a^T = Q_a`, since `S` fixes `Q`.
The reassembled operator therefore depends only on the right coset `S . a`.

Measured: within each of the four right cosets the operator deviation is
`1.2e-10` at `L = 3` (`n = 98`) and `1.2e-10` at `L = 4` (`n = 279`), against an
operator scale `max|Q| = 29.5`; the four coset representatives are pairwise
separated by at least `4.0000`. A direct clustering of all 24 reassembled
operators returns exactly four distinct members at both sizes.

The composition order is load-bearing and the gate discriminates on it: the *left*
cosets `a . S` are not constancy classes, with a within-class deviation of
`4.0000` at both sizes — the same magnitude as the separation between genuine
classes. A construction that mistook the anti-homomorphism for a homomorphism
would fail this row.

Because the statement is about the operator rather than about any supplied
source, every frame functional of the reassembled operator — spectrum, weight,
pairing, or a solved floor — takes at most four values, and the bound four is the
index rather than an observed coincidence.

### Complete classification of frame-blinding subgroups

Call a supplied source frame-blind when its pairing `b . Q_g^{-1} . b` is constant
over all 24 rotations. Averaging a source over a subgroup `H` produces `b` bar
with `P_t^T b` bar `= b` bar for every `t` in `H`. If `g = s t` with `s` in `S`
and `t` in `H`, then `P_g^T b` bar `= P_s^T b` bar, and the pairing is unchanged
because `S` fixes `Q`. So the average is frame-blind whenever the product set
`S . H` is the whole group.

The product-set count `|S . H| = |S| |H| / |H meet S|` turns that condition into
arithmetic: covering requires `|H| = 4 |H meet S|`, hence `|H| >= 4`, with
equality exactly when `H` meets `S` trivially. **The minimal frame-blinding order
is four, and it is attained exactly by the complements of `S`** — derived from the
counting identity, not read off a scan.

The subgroup lattice of the rotation group has 30 members, and a complete scan
over all of them was run at `L = 3` and `L = 4` with three supplied sources each.
Measured blindness agrees with the covering condition in `30 / 30` subgroups at
both sizes. Nine subgroups cover; exactly four of them have order four —
`{0,3,20,23}`, `{0,7,16,23}`, `{3,10,14,23}`, and the sign law's source
stabilizer `{20,21,22,23}`.

The dichotomy is sharp, not marginal. At `L = 3` the worst covering spread is
`1.1e-11` while the smallest non-covering spread is `2.5e-02`, a separation factor
of `2.2e+09`; at `L = 4` the corresponding numbers are `1.8e-10` and `9.5e-02`,
a factor of `5.3e+08`.

Three rejectors are carried inside the same scan. The zero-defect subgroup `S`
itself does not cover and does not blind (`3.9e-02` at `L = 3`, `6.2e-01` at
`L = 4`). The four-element subset `{1,4,9,23}` drawn from inside `S` is not a
subgroup at all and does not blind (`5.2e-02`, `8.4e-01`). The three order-4
subgroups that meet `S` non-trivially all fail to blind. Meanwhile the source
stabilizer's own four-fold average is blind to `3.5e-12` and `1.8e-10`, and the
full 24-frame average is blind to `2.4e-16` and `1.7e-13`.

## Derivation sketch

The whole cycle rests on one asymmetry. The relabelling composes as an
anti-homomorphism, so the frames that fix `Q` act on the *left* of the frame
label. Left action partitions the group into right cosets; the invariant of a
frame is therefore its right coset, and the number of distinct reassembled
operators is bounded by the index of the fixing subgroup. Measuring that subgroup
to have order 6 fixes the bound at 4, and the measured operator clustering
saturates it.

The blinding statement is the same asymmetry read on the source side. A
subgroup-averaged source is invariant under `H` acting on the right of the label,
and the operator is invariant under `S` acting on the left; a pairing is blind at
frame `g` exactly when `g` can be written with one factor from each. Coverage of
the group by `S . H` is therefore the precise condition, and the product-set
count converts it into the divisibility statement `|H| = 4 |H meet S|`.

## Honest boundary

The order of `S` is measured, not derived: the claim "the index is four" is exact
given `|S| = 6`, and `|S| = 6` is a property of the supplied assembly at the sizes
tested. The sufficiency direction of the blinding classification is derived
exactly; the necessity direction is measured — a supplied source could in
principle be accidentally blind under a non-covering subgroup, and what is
established is that none of the tested sources is, in `30 / 30` subgroups at two
sizes with three sources each.

The reassembled operator is nonsingular but indefinite in this sector, so the
pairing is signed and no positivity or energy reading is licensed here. Sizes are
capped at `L = 4` for the full 30-subgroup scan by host memory rather than by
structure; the factorization and coset rows are size-independent algebra once the
zero-defect set is fixed. Static spatial sector only. The four specific operator
values, and the specific spreads quoted for non-covering subgroups, are properties
of the supplied sources; the coset partition itself is source-independent.

Nothing here selects a frame, adopts a preferred rotation, or licenses replacing
a physical average by a smaller one as a matter of definition — it establishes
that on this supplied assembly the larger average and the four-fold average agree
exactly.

## The next paths opened

The identification of the two quartets suggests three continuations. The
minus-branch floor scan of this lane can be solved on four coset representatives
instead of 24, and the floor can then be tested for coset-constancy in its own
right, which would promote the present operator-level statement to the solved
quantity. The remaining covering subgroups — three of order 8, one of order 12,
and the full group — give a coarser blinding ladder whose physical reading is not
yet fixed.
And the counting identity `|H| = 4 |H meet S|` is stated for subgroups; extending
the classification to arbitrary averaging sets would characterize frame-blindness
without a group hypothesis.

## Relation to the interacting cycle

The supplied sign law's source stabilizer enters here purely as a group-theoretic
object — a specific order-4 subgroup — and this cycle makes no use of, and no
claim about, its endpoint sign content. The two cycles meet only in the
observation that the same subgroup is a minimal blinder for the assembly-side
pairing.

## Runner

`scripts/physical_frame_group_factorization_and_minimal_blinding_cycle715_2026_08_02.py`
— `TOTAL: PASS=35 FAIL=0`, 5 s, self-contained against the landed Cycle-696
compiler chain. The zero-defect set, the quartet, the subgroup lattice, and every
blindness measurement are recomputed inside the runner; no membership list is
supplied as an input to a claim.

## Citations

- [The all-24 frame sign law of the source-driven K field, derived by source-stabilizer coset collapse — Cycle 707](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)

Context, no dependency edge: the Cycle-696 compiler
`physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25`, and the in-flight
Cycle-708 through Cycle-714 rows of this lane, whose measurements are not inputs
to any claim above.
