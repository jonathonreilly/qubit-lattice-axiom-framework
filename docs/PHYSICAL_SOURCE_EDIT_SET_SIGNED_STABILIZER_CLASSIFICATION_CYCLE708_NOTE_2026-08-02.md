# PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02

Date 2026-08-02. Paired runner
`scripts/physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02.py`;
paired outputs
`outputs/physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02_cold_2026-08-02.txt`
and
`outputs/physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02_receipt_2026-08-02.json`.

## Abstract

This note gives a computable classification of the per-frame sign law of the registered
`K` multiset over arbitrary integer edit sets on the six-ray source domain. For a source
domain `D` carrying edits, the decorated stabilizer `Stab48(D)` inside the 48 signed
permutation matrices, intersected with the 12 constant-sign matrices along the coset of
a proper frame, determines a four-valued label for every one of the 24 proper frames:
the multiset of `K` is carried to itself with sign `+1`, with sign `-1`, with both signs,
or is not carried at all. The classification is exercised on a battery of four domains at
`L = 3` and `L = 7`. Two of the four are new predictions confirmed by the paired runner:
the three-edit domain narrows the lawful set to exactly the six constant-sign proper
frames, split 3 plus / 3 minus with 18 broken; and the symmetric-pair domain makes all 24
proper frames lawful with BOTH signs, which forces a palindromic spectrum, pointwise
central antisymmetry, and an exact centre zero of `K` at floor scale. Predicted and
measured profiles agree 24 of 24 on every domain at both sizes, with 95 gates passing and
none failing.

## Scope guard

The 24 proper (determinant `+1`) rotations are the axiom symmetries of the cubic lattice
setting. The 48 signed permutation matrices used here are computational bookkeeping for
the compiled chain: the 24 improper (determinant `-1`) elements enter this note purely as
**computational identities** of the compiled map from decorated domain to `K`, and never
as symmetries of the physical setting. Every claim about a symmetry is a claim about a
proper frame; the improper elements appear only as intermediate labels that the compiled
chain happens to realise, and the classification's output is always a statement about the
24 proper frames. This is stated once here and assumed throughout.

## Setting and definitions

The compiled chain is the landed cycle-696 open-coframe endpoint compiler
(`scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`), whose stages
are: decorated source domain `D` on an open `L^3` box, source vector `rho(D)`, load
`b = rho G`, linear response `eps`, clipped coframe, and the scalar endpoint field `K`.
The runner drives this chain unmodified and rebuilds nothing of its internals.

- `G48` is the set of all 48 signed permutation matrices in three dimensions, built as
  permutation matrices times the eight sign patterns. Its proper part `SO`, the 24
  elements of determinant `+1`, is measured equal as a set to the module's own frame list
  (`c696.c576.FRAMES`); gate A1.
- `CS` is the set of 12 constant-sign matrices, those of the form `+P` or `-P` with `P` a
  permutation matrix. `CS` is a subgroup: closure follows from `(-P)(-Q) = PQ`, and the
  runner checks closure on all 144 products directly; gate A2.
- The sign character `sx : CS -> {+1, -1}` sends `+P` to `+1` and `-P` to `-1`. It is
  multiplicative, verified on all 144 pairs; gate A4.
- `CS_proper = CS` intersect `SO` has 6 elements: the identity, the two 3-cycles with all
  entries `+1`, and the three negated transpositions `-T` (with `det(-T) = -det(T) = +1`
  in three dimensions). The runner re-derives this set and cross-checks that it sits at
  frame indices `[1, 4, 9, 15, 18, 23]`; gate A3.
- A domain's fingerprint is the canonical, order-independent key `c696.domain_key(D)`:
  anchor, sorted ports, and sorted directed link triples. `c696.apply_frame_to_domain`
  accepts any signed permutation matrix, improper ones included.
- `Stab48(D) = { R in G48 : domain_key(R . D) == domain_key(D) }`, recomputed by
  fingerprint equality and never hardcoded.

Because `rho` is recomputed from the link state alone, fingerprint equality implies
bit-identical chain input. The runner does not rely on that argument alone: gate C2
measures `rho` bit-equality directly over every lawful pair at both sizes.

## The classification theorem

For a proper frame `g`, define

    sgn-set(g) = { sx(h) : h in (g . Stab48(D)) intersect CS }.

**Derived direction.** Let `s` be in `Stab48(D)` with `h = g . s` in `CS`. Sidedness
matters and is fixed by the group action: `h . D = (g . s) . D = g . (s . D) = g . D`,
so the frame image of `D` under `g` is EXACTLY the frame image under `h` — not merely
close, but the same decorated state. Equivalently `h = g . s^{-1}` recovers `s` from a
constant-sign representative, since `Stab48(D)` is a group. This state collapse is
re-measured, not assumed: gates C1 and C2 confirm fingerprint equality and `rho`
bit-equality across every such pair. The constant-sign pointwise transport law for `h`,
also re-measured by this runner, reads

    K^{h . D}(h x) = sx(h) . K^D(x)   pointwise, at floor-scale defect,

and composing the two gives `multiset(K^{g . D}) = multiset(sx(h) . K^D)`. Hence every
element of `sgn-set(g)` is a valid multiset sign for `g`.

**Tetrachotomy.** `sgn-set(g)` takes one of four values — empty, `{+1}`, `{-1}`,
`{+1,-1}` — which label the frame broken, plus, minus, or both. These are all four
subsets of `{+1,-1}`, so the four labels partition the 24 proper frames for any domain.

**Counting law.** `Stab48(D)` and `CS` are both subgroups, so the subgroup product
formula gives

    |CS . Stab48| = |CS| . |Stab48| / |CS intersect Stab48|,

and the lawful proper frames are exactly `(CS . Stab48)` intersect `SO`. Gate B3 measures
the set order of the product against this formula on every domain at both sizes.

**Collision criterion.** `sgn-set(g)` contains BOTH signs for some `g` if and only if
`Stab48(D)` meets `CS_minus`, the six constant-sign matrices of the form `-P`. Proof, two
lines: if `h_plus . s1 = h_minus . s2` with both `h` in `CS` and both `s` in `Stab48`,
then `s2 . s1^{-1} = h_minus^{-1} . h_plus` lies in `CS_minus` intersect `Stab48`, since
`sx` is multiplicative and the two sides have opposite sign; conversely, multiplying any
lawful constant-sign representative by a minus-sign stabilizer element produces a second
representative of the same coset with the opposite sign.

**Corollaries when the criterion fires.** Taking `g` to be the identity forces the
PALINDROMIC SPECTRUM `multiset(K^D) = multiset(-K^D)`. If in addition `-I` itself lies in
`Stab48(D)`, the pointwise law for `-I` — whose permutation part is the identity and whose
signs are all `-1` — forces POINTWISE ANTISYMMETRY `K^D(sigma x) = -K^D(x)`, where `sigma`
is the site map of `-I`, central inversion about the anchor. Evaluating at the fixed point
of `sigma` gives the FORCED CENTRE ZERO `K^D(centre) = 0` at floor scale.

## Battery

Four domains, edit weights all distinct from the background ray weight 3, centre
`c = (A,A,A)` with `A = (L-1)//2`, edit keys directed away from the anchor. Profiles are
written plus / minus / both / broken. `Stab48` orders, `CS` intersect `Stab48` orders, and
the member index lists are measured identical at `L = 3` and `L = 7` (gates B1, B2, B4),
so the stabilizer data below is size-independent across the sizes tested.

| domain | edits | `Stab48` | `CS^Stab` | `-1` in `CS^Stab` | `|CS.Stab|` | predicted | measured `L=3` | measured `L=7` | agreement |
|---|---|---|---|---|---|---|---|---|---|
| d1 one-edit | `(c,c+ex):5` | 8 | 2 | no | 48 | 12/12/0/0 | 12/12/0/0 | 12/12/0/0 | 24/24 |
| d2 two-edit | `(c,c+ex):5 (c,c+ey):7` | 2 | 1 | no | 24 | 6/6/0/12 | 6/6/0/12 | 6/6/0/12 | 24/24 |
| d3 three-edit | `(c,c+ex):5 (c,c+ey):7 (c,c+ez):11` | 1 | 1 | no | 12 | 3/3/0/18 | 3/3/0/18 | 3/3/0/18 | 24/24 |
| d4 symmetric pair | `(c,c+ex):5 (c,c-ex):5` | 16 | 4 | yes | 48 | 0/0/24/0 | 0/0/24/0 | 0/0/24/0 | 24/24 |

Measured `|CS.Stab|` equals the counting-law value 48 / 24 / 12 / 48 on all four domains
at both sizes. For d3 the six lawful proper frames are exactly `CS_proper` itself: the
three all-plus even permutations carry the plus sign, the three negated transpositions the
minus sign. For d4 the `CS` intersect `Stab48` subgroup is `{I, swap_yz, -I, -swap_yz}`,
which contains `-I`, so the collision criterion fires and all three corollaries apply.

Every chain the battery evaluates — lawful, broken, and wrong-sign rejector rows alike —
reports the principal coframe unclipped, with measured minimum metric positivity margin
4.8e-01 at `L = 3` and 4.2e-01 at `L = 7` over all 57 distinct chains per size. The
compiler's clip branch is a guard, never a smoothing: no gated value in this note rests
on a clipped coframe. The insertion amplitude 5.0e-02 is chosen inside this unclipped
regime — at amplitude 2.0e-01 the multi-edit domains d2, d3, and (at `L = 3`) d4 drive
the metric non-positive and the guard fires, so the working point sits below that
threshold.

Measured floors, `.1e`, taken as the worst defect within each branch across the domain's
lawful pairs; `none` means the branch is empty for that domain.

| domain | `L` | plus floor | minus floor | both floor | broken minimum |
|---|---|---|---|---|---|
| d1 | 3 | 2.3e-15 | 2.5e-12 | none | none |
| d2 | 3 | 3.0e-15 | 2.4e-11 | none | 5.7e-02 |
| d3 | 3 | 3.3e-15 | 2.7e-11 | none | 8.5e-02 |
| d4 | 3 | none | none | 6.4e-12 | none |
| d1 | 7 | 8.9e-14 | 8.2e-11 | none | none |
| d2 | 7 | 2.1e-13 | 1.5e-10 | none | 4.1e-02 |
| d3 | 7 | 1.4e-13 | 1.6e-10 | none | 1.2e-01 |
| d4 | 7 | none | none | 1.2e-10 | none |

Pointwise transport, measured over the distinct coset representatives (6 / 12 / 6 / 6 for
d1 / d2 / d3 / d4 at both sizes): worst plus-branch defect 3.8e-15 and worst minus-branch
defect 2.7e-11 at `L = 3`; 2.1e-13 and 1.6e-10 at `L = 7`. State collapse holds over
24 / 12 / 6 / 48 lawful pairs per domain, with `rho` bit-equality on the same pairs. No
frame anywhere in the battery lands in the forbidden band between the classification hit
tolerance 1.0e-05 and the classification miss tolerance 1.0e-03; the measured count of
such gap hits is 0 on every domain at both sizes.

Symmetric-pair corollaries, measured: `-I` is in `Stab48(d4)` at both sizes; palindrome
defect 6.3e-12, `|K(centre)|` 6.5e-12, antisymmetry defect 1.3e-11 at `L = 3`; and
1.2e-10, 3.4e-11, 1.2e-10 at `L = 7`.

The paired runner's own final line is `TOTAL: PASS=95 FAIL=0`, and its stdout is captured
byte-for-byte in the cold output named above.

## Rejectors

Each of these numbers discriminates: a wrong model of the sign law changes it.

- **Proper-only classifier.** Restricting the stabilizer to its proper part and running the
  same coset construction labels only 6 of the two-edit domain's proper frames lawful,
  against 12 measured — a mismatch of 6, identical at both sizes. The improper elements of
  `Stab48` are load-bearing bookkeeping: dropping them loses half the lawful frames. This
  is why the construction is carried out in `G48` and not in the 24 proper frames alone.
- **Determinant-as-sign model.** The hypothesis that the multiset sign is the frame
  determinant fails immediately: all 24 proper frames have determinant `+1`, yet 12 of the
  24 are measured minus on the single-edit domain. The model misclassifies 12 of 24, at
  both sizes.
- **Wrong-sign distances.** Comparing a lawful frame's `K` multiset against the OPPOSITE
  sign of the reference gives, at `L = 3`, 5.0e-02 from both the plus and the minus frame
  on d1 and 4.2e-02 on d3; at `L = 7`, 1.2e-02 on d1 and 3.2e-02 on d3. Every one of these
  is far above the corresponding floors, so the branch assignment is not an artefact of a
  loose tolerance.
- **Single-valuedness.** On every lawful frame where the collision criterion does not
  fire, the measured `sgn-set` is single-valued: 24 lawful frames on d1, 12 on d2, 6 on
  d3, each carrying exactly one sign. (Distinct lawful frames can share a stabilizer
  coset — d1's 24 lawful frames sit on 6 distinct cosets — so the per-frame count
  exercises each coset more than once.) The criterion's "if and only if" therefore has
  both directions exercised by the battery.
- **Separation margin.** The smallest ratio of an off-class distance (a broken minimum or a
  wrong-sign distance) to the worst lawful floor in the same row is measured 1.5e+09 at
  `L = 3` and 1.5e+08 at `L = 7`, across four rows at each size.

## Honest boundary

- The converse of the classification theorem — that an empty `sgn-set` implies the frame
  really is broken — is **measured, not derived**. The derived direction supplies only
  sufficiency: every element of `sgn-set(g)` is a valid sign. The battery measures the
  broken frames sitting far above every floor, but no argument here forbids some other
  mechanism from carrying a multiset without a constant-sign coset representative.
- The measured separation of the broken and wrong-sign distances above the lawful floors is
  at least 8 orders of magnitude everywhere in the battery, with minimum ratio 1.5e+08.
  This is an honest shortfall against the 9-order separation anticipated when the battery
  was specified: at `L = 3` the minimum ratio is 1.5e+09, comfortably past 9 orders, but at
  `L = 7` it falls to 1.5e+08, about 8.2 orders. The measured value stands; the anticipated
  one does not. The drop tracks the growth of the minus-branch floor with size and the
  shrinking of the single-edit domain's wrong-sign distance from 5.0e-02 to 1.2e-02, both
  of which are visible in the tables above.
- The minus-branch floor VALUES are **measured, not derived**. Their scale is inherited
  from the chain's linear solve and its response amplitude, not predicted by anything in
  this note. The classification predicts which branch a frame lands in; it does not predict
  the magnitude of the residual defect within a branch.
- Improper bookkeeping carries no symmetry claim, as stated in the scope guard.
- All claims are scoped to this compiled chain, this four-domain battery, and `L` in
  `{3, 7}`, with the open-box boundary (no wrap) and response amplitude 5.0e-02.

## Named next paths

- Derive the response-stage floor constant, so that the minus-branch floor values become
  predicted rather than measured, and the separation margin becomes a computed quantity
  rather than a reported one.
- Classify over larger edit families: off-centre edits, mixed-axis edits, and edit sets
  whose stabilizer is not a subgroup of the axis stabilizers exercised here. The
  three-edit domain already reaches the trivial stabilizer, so the interesting direction is
  domains whose stabilizer is a different subgroup of the same order.
- Measure the size scaling of the floors across a longer ladder in `L`, which would turn
  the size dependence noted in the honest boundary into a quantitative law and would say
  whether the separation margin has an asymptote.

## Citations

- [docs/MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)
- [docs/PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
- [docs/RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md](RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md)

The open (unlanded) sibling
`PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01` measures
two source domains by a coset-collapse argument; those two domains appear here as the
first two battery rows, d1 and d2, re-derived from the classification theorem rather than
measured case by case, and their profiles reproduce. That sibling is open work and nothing
in this note depends on it.
