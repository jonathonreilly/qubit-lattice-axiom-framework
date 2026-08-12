# Signed-stabilizer classifier for a supplied source-response compiler: conditional algebra and a four-domain finite battery — Cycle 708

**Date:** 2026-08-02 (revised 2026-08-11, review-loop iteration 1)

**Type:** bounded_theorem

**Status:** proposed_retained

**Primary runner:**
[`physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02.py`](../scripts/physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02.py)

**Independent checker:**
[`physical_source_edit_set_signed_stabilizer_classification_cycle708_independent_check_2026_08_02.py`](../scripts/physical_source_edit_set_signed_stabilizer_classification_cycle708_independent_check_2026_08_02.py)

**Run artifacts:**
[`cold stdout`](../outputs/physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02_cold_2026-08-02.txt)
and
[`receipt`](../outputs/physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02_receipt_2026-08-02.json),
plus the source-bound
[`primary cache`](../logs/runner-cache/physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02.txt)
and
[`independent-check cache`](../logs/runner-cache/physical_source_edit_set_signed_stabilizer_classification_cycle708_independent_check_2026_08_02.txt).

## Trace gate

```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "classify the proper-frame K-sign behavior of a supplied finite source-response compiler"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "test the conditional classifier on broader edit families and derive, rather than sample, the constant-sign transport premise"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: supports
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "an exact finite-group implication conditional on a supplied compiler transport premise, with that premise and its numerical converse tested only on four edit domains at L in {3,7}"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/physical_source_edit_set_signed_stabilizer_classification_cycle708_independent_check_2026_08_02.py
```

## Abstract

This note separates an exact finite-group implication from a finite numerical
battery. For an edit domain `D`, if the supplied compiler obeys the stated
constant-sign pointwise transport law on `D`, the intersection of the domain
stabilizer `Stab48(D)` with the 12 constant-sign matrices along the right coset
of a proper frame gives every sign that the implication proves for that frame.
The sign set is empty, plus, minus, or both. An empty sign set is not a proof
that no other mechanism carries the field; that converse is measured only.

The primary runner tests the transport premise and the measured converse on
four declared domains at `L = 3` and `L = 7`. The three-distinct-axis domain
has six lawful proper frames, split 3 plus / 3 minus with 18 measured broken;
the inversion-pair domain makes all 24 proper frames double-signed and exhibits
a palindromic spectrum, pointwise central antisymmetry, and a centre value at
the numerical floor. Predicted and measured profiles agree 24 of 24 on every
declared domain at both sizes. The independent checker reconstructs the finite
group, stabilizers, cosets, collision criterion, and profiles without importing
the numerical primary or its compiler.

## Scope guard

The 24 proper (determinant `+1`) rotations are the symmetries supplied by the
[Lattice axiom](MINIMAL_AXIOMS_2026-06-29.md). The 48 signed permutation
matrices used here are computational bookkeeping for the compiled chain: the
24 improper elements enter purely as tested identities of the supplied map
from chain-input fingerprint to `K`, never as physical symmetries. Every
symmetry statement below concerns a proper frame.

## Setting and definitions

The supplied chain is the landed Cycle-696 open-coframe endpoint compiler
([`physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)), whose stages
are: source domain `D` on an open `L^3` box, source vector `rho(D)`, load
`b = rho G`, linear response `eps`, clipped coframe, and the scalar endpoint field `K`.
The runner drives this chain unmodified and rebuilds nothing of its internals.

- `G48` is the set of all 48 signed permutation matrices in three dimensions, built as
  permutation matrices times the eight sign patterns. Its proper part `SO`, the 24
  elements of determinant `+1`, is measured equal as a set to the module's own frame list
  (`c696.c576.FRAMES`); the `group_order` check.
- `CS` is the set of 12 constant-sign matrices, those of the form `+P` or `-P` with `P` a
  permutation matrix. `CS` is a subgroup: closure follows from `(-P)(-Q) = PQ`, and the
  runner checks closure on all 144 products directly; the
  `constant_sign_closure` check.
- The sign character `sx : CS -> {+1, -1}` sends `+P` to `+1` and `-P` to `-1`. It is
  multiplicative, verified on all 144 pairs; the `sign_character` check.
- `CS_proper = CS` intersect `SO` has 6 elements: the identity, the two 3-cycles with all
  entries `+1`, and the three negated transpositions `-T` (with `det(-T) = -det(T) = +1`
  in three dimensions). The runner re-derives this set and cross-checks that it sits at
  frame indices `[1, 4, 9, 15, 18, 23]`; the `constant_sign_proper`
  check.
- A domain's chain-input fingerprint is the order-independent key
  `c696.domain_key(D)`: anchor, sorted ports, and sorted directed link triples.
  It is not claimed to encode every auxiliary field in the compiler's domain
  object. `c696.apply_frame_to_domain`
  accepts any signed permutation matrix, improper ones included.
- `Stab48(D) = { R in G48 : domain_key(R . D) == domain_key(D) }`, recomputed by
  fingerprint equality and never hardcoded.

Because `rho` is recomputed from the link state alone, fingerprint equality
implies bit-identical source input. The runner also recomputes `rho` outside
the fingerprint-keyed chain cache and measures bit equality for every
constant-sign representative of every lawful proper frame at both sizes.

## Imports, declared scope, derived content, and open work

### Load-bearing imported implementation

The primary imports the supplied Cycle-696 compiler and its complete ordinary
Python source closure: the Cycle-576 source-law module, its Regge and plaquette
helpers, and the cubic-Coxeter Regge second-variation module. Their exact paths
are declared in the primary's `AUDIT_INPUT_PATHS`, so the runner cache becomes
stale if any imported byte changes. The
[Cycle-700 source-response note](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
records the compiler's bounded interpretation and limitations. That row is
currently an unaudited bounded source, so this note remains conditional support
pending independent audit and dependency closure.

### Declared finite scope

The four weighted edit domains, open boundaries, `L in {3,7}`, response
amplitude `0.05`, principal-coframe no-clip requirement, and classification and
separation tolerances are supplied experimental choices. The response map,
source normalization, static sector, metric fit, and endpoint interpretation
are inherited supplied structure; this note derives none of them and makes no
gravity, energy, rate, or empirical claim.

### Derived here

The finite-group right-coset implication, determinant balance, subgroup-product
count, and collision criterion are exact. The independent checker reconstructs
them using pure integer tuples. The primary measures the premise and the
four-domain profiles through the supplied floating-point compiler.

### Open

The constant-sign transport premise is not proved for arbitrary edit sets, and
an empty sign set does not exclude a different transport mechanism. Wider edit
families, a derived response-floor constant, and size scaling remain open.

## Exact target and proof-obligation graph

**Exact target.** Conditional on constant-sign pointwise transport for a
declared edit domain of the supplied compiler, prove that the right-coset sign
set supplies valid multiset signs, then test that implication and its unproved
converse on the four declared finite domains.

1. `G48`, `CS`, and the sign character form the stated finite-group objects:
   proved here and independently enumerated.
2. Right multiplication by a stabilizer element preserves the domain's
   chain-input fingerprint: exact by the group action and checked on every
   representative.
3. Constant-sign pointwise transport: a named conditional premise in the
   general statement; measured on every distinct constant-sign representative
   used by the four-domain battery.
4. Multiset transport: follows from items 2 and 3.
5. Empty sign set implies measured broken: not proved; only tested at the two
   sizes. This is the strongest missing lemma for any wider classification.

Degenerate cases are included: the sign set may be empty or double-signed, and
the stabilizer may be trivial. Domains outside the declared battery, clipped
coframes, periodic boundaries, and other response amplitudes are not covered by
the numerical statement.

## The classification theorem

For a proper frame `g`, define

    sgn-set(g) = { sx(h) : h in (g . Stab48(D)) intersect CS }.

**Conditional derived direction.** Let `s` be in `Stab48(D)` with `h = g . s`
in `CS`. Sidedness matters and is fixed by the group action:
`h . D = (g . s) . D = g . (s . D) = g . D`, so the frame image of
`D` under `g` has the same chain-input fingerprint as its image under `h`.
Conversely, a constant-sign `h` in `g . Stab48(D)` gives
`s = g^{-1} . h` in the stabilizer. The primary recomputes fingerprint and
`rho` equality for every such representative. Conditional on the pointwise
transport law

    K^{h . D}(h x) = sx(h) . K^D(x)   pointwise, at floor-scale defect,

and composing the two gives `multiset(K^{g . D}) = multiset(sx(h) . K^D)`. Hence every
element of `sgn-set(g)` is a valid multiset sign for `g`.

**Tetrachotomy.** `sgn-set(g)` takes one of four values — empty, `{+1}`, `{-1}`,
`{+1,-1}` — which label the frame broken, plus, minus, or both. These are all four
subsets of `{+1,-1}`, so the four labels partition the 24 proper frames for any domain.

**Counting law.** `Stab48(D)` and `CS` are both subgroups, so the finite-set
subgroup-product formula gives

    |CS . Stab48| = |CS| . |Stab48| / |CS intersect Stab48|,

and the lawful proper frames are exactly `(CS . Stab48) intersect SO`.
Left multiplication by `-I in CS` is a fixed-point-free involution of
`CS . Stab48` that flips determinant. Therefore exactly half the product is
proper, and the proper lawful-frame count is `|CS . Stab48| / 2`. The primary
and independent checker both verify these counts.

**Collision criterion.** `sgn-set(g)` contains both signs for some `g` if and
only if `Stab48(D)` meets `CS_minus`, the six constant-sign matrices of the
form `-P`. If `h_plus = g . s_plus` and `h_minus = g . s_minus`, then
`h_minus^{-1} . h_plus = s_minus^{-1} . s_plus` lies in both `CS_minus`
and `Stab48(D)`. Conversely, if `m` is a minus-sign element of
`CS intersect Stab48(D)`, then for any constant-sign representative
`h = g . s`, the element `h . m = g . (s . m)` is another representative
with the opposite sign.

**Corollaries when the criterion fires.** Taking `g` to be the identity gives
the palindromic spectrum `multiset(K^D) = multiset(-K^D)`, conditional on the
same measured transport premise. If `-I` lies in `Stab48(D)`, the pointwise law
for `-I` gives `K^D(sigma x) = -K^D(x)`, where `sigma` is central inversion
about the anchor. Its fixed point has `K^D(centre) = 0`. The primary observes
these relations at its floating-point floor; it does not claim symbolic zero
from the numerical solve.

## Battery

Four domains, edit weights all distinct from the background ray weight 3, centre
`c = (A,A,A)` with `A = (L-1)//2`, edit keys directed away from the anchor. Profiles are
written plus / minus / both / broken. `Stab48` orders, `CS` intersect `Stab48` orders, and
the member index lists are measured identical at `L = 3` and `L = 7`,
so the stabilizer data below is size-independent across the sizes tested.

| domain | edits | `Stab48` | `CS^Stab` | `-1` in `CS^Stab` | `|CS.Stab|` | predicted | measured `L=3` | measured `L=7` | agreement |
|---|---|---|---|---|---|---|---|---|---|
| one edit | `(c,c+ex):5` | 8 | 2 | no | 48 | 12/12/0/0 | 12/12/0/0 | 12/12/0/0 | 24/24 |
| two distinct-axis edits | `(c,c+ex):5 (c,c+ey):7` | 2 | 1 | no | 24 | 6/6/0/12 | 6/6/0/12 | 6/6/0/12 | 24/24 |
| three distinct-axis edits | `(c,c+ex):5 (c,c+ey):7 (c,c+ez):11` | 1 | 1 | no | 12 | 3/3/0/18 | 3/3/0/18 | 3/3/0/18 | 24/24 |
| inversion pair | `(c,c+ex):5 (c,c-ex):5` | 16 | 4 | yes | 48 | 0/0/24/0 | 0/0/24/0 | 0/0/24/0 | 24/24 |

Measured `|CS.Stab|` equals the counting-law value 48 / 24 / 12 / 48 on all four domains
at both sizes. For the three-distinct-axis domain the six lawful proper frames
are exactly `CS_proper` itself: the
three all-plus even permutations carry the plus sign, the three negated transpositions the
minus sign. For the inversion-pair domain the `CS` intersect `Stab48`
subgroup is `{I, swap_yz, -I, -swap_yz}`,
which contains `-I`, so the collision criterion fires and all three corollaries apply.

Every chain the battery evaluates — lawful, broken, and wrong-sign rejector rows alike —
reports the principal coframe unclipped, with measured minimum metric positivity margin
4.8e-01 at `L = 3` and 4.2e-01 at `L = 7` over all 57 distinct chains per size. The
compiler's clip branch is a guard, never a smoothing: no gated value in this note rests
on a clipped coframe. The insertion amplitude 5.0e-02 is chosen inside this unclipped
regime — at amplitude 2.0e-01 the two-distinct-axis and
three-distinct-axis domains, plus the `L = 3` inversion-pair domain, drive
the metric non-positive and the guard fires, so the working point sits below that
threshold.

Measured floors, `.1e`, taken as the worst defect within each branch across the domain's
lawful pairs; `none` means the branch is empty for that domain.

| domain | `L` | plus floor | minus floor | both floor | broken minimum |
|---|---|---|---|---|---|
| one edit | 3 | 2.3e-15 | 2.5e-12 | none | none |
| two distinct-axis edits | 3 | 3.0e-15 | 2.4e-11 | none | 5.7e-02 |
| three distinct-axis edits | 3 | 3.3e-15 | 2.7e-11 | none | 8.5e-02 |
| inversion pair | 3 | none | none | 6.4e-12 | none |
| one edit | 7 | 8.9e-14 | 8.2e-11 | none | none |
| two distinct-axis edits | 7 | 2.1e-13 | 1.5e-10 | none | 4.1e-02 |
| three distinct-axis edits | 7 | 1.4e-13 | 1.6e-10 | none | 1.2e-01 |
| inversion pair | 7 | none | none | 1.2e-10 | none |

Pointwise transport, measured over the distinct constant-sign representatives
(12 / 12 / 6 / 12 for one edit / two distinct-axis edits / three
distinct-axis edits / inversion pair at both sizes): worst plus-branch defect
3.8e-15 and worst minus-branch
defect 2.7e-11 at `L = 3`; 2.1e-13 and 1.6e-10 at `L = 7`. State collapse holds over
48 / 12 / 6 / 96 constant-sign representatives per domain, with `rho` bit-equality
on the same representatives. No
frame anywhere in the battery lands in the forbidden band between the classification hit
tolerance 1.0e-05 and the classification miss tolerance 1.0e-03; the measured count of
such gap hits is 0 on every domain at both sizes.

Inversion-pair corollaries, measured: `-I` is in its stabilizer at both sizes;
palindrome
defect 6.3e-12, `|K(centre)|` 6.5e-12, antisymmetry defect 1.3e-11 at `L = 3`; and
1.2e-10, 3.4e-11, 1.2e-10 at `L = 7`.

The primary runner's own final line is `TOTAL: PASS=95 FAIL=0`, and its stdout is captured
byte-for-byte in the cold output named above.

## Rejectors

Each of these numbers discriminates: a wrong model of the sign law changes it.

- **Proper-only classifier.** Restricting the stabilizer to its proper part and running the
  same coset construction labels only 6 of the two-distinct-axis domain's proper frames lawful,
  against 12 measured — a mismatch of 6, identical at both sizes. The improper elements of
  `Stab48` are load-bearing bookkeeping: dropping them loses half the lawful frames. This
  is why the construction is carried out in `G48` and not in the 24 proper frames alone.
- **Determinant-as-sign model.** The hypothesis that the multiset sign is the frame
  determinant fails immediately: all 24 proper frames have determinant `+1`, yet 12 of the
  24 are measured minus on the one-edit domain. The model misclassifies 12 of 24, at
  both sizes.
- **Wrong-sign distances.** Comparing a lawful frame's `K` multiset against the opposite
  sign of the reference gives minimum distances, at `L = 3`, 5.0e-02 over
  the plus and minus frames of the one-edit domain and 4.2e-02 over those of
  the three-distinct-axis domain; at `L = 7`, the corresponding minima are
  1.2e-02 and 3.2e-02. Every one of these
  is far above the corresponding floors, so the branch assignment is not an artefact of a
  loose tolerance.
- **Single-valuedness.** On every lawful frame where the collision criterion does not
  fire, the measured `sgn-set` is single-valued: 24 lawful frames on the
  one-edit domain, 12 on the two-distinct-axis domain, and 6 on the
  three-distinct-axis domain, each carrying exactly one sign. (Distinct lawful
  frames can share a stabilizer coset — the one-edit domain's 24 lawful frames
  sit on 6 distinct cosets — so the per-frame count
  exercises each coset more than once.) The criterion's "if and only if" therefore has
  both directions exercised by the battery.
- **Separation margin.** The smallest ratio of an off-class distance (a broken minimum or a
  wrong-sign distance) to the worst lawful floor in the same row is measured 1.5e+09 at
  `L = 3` and 1.5e+08 at `L = 7`, across four rows at each size.

## Honest boundary

- The converse of the conditional classification implication — that an empty
  `sgn-set` implies the frame
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
  shrinking of the one-edit domain's wrong-sign distance from 5.0e-02 to 1.2e-02, both
  of which are visible in the tables above.
- The minus-branch floor values are **measured, not derived**. Their scale is inherited
  from the chain's linear solve and its response amplitude, not predicted by anything in
  this note. On the declared domains, the conditional sign-set construction predicts
  which branch a frame lands in after its transport premise is verified; it does not
  predict the residual defect within a branch.
- Improper bookkeeping carries no symmetry claim, as stated in the scope guard.
- All numerical claims are scoped to this supplied chain, this four-domain battery, and `L` in
  `{3, 7}`, with the open-box boundary (no wrap) and response amplitude 5.0e-02.

## Named next paths

- Derive the response-stage floor constant, so that the minus-branch floor values become
  predicted rather than measured, and the separation margin becomes a computed quantity
  rather than a reported one.
- Classify over larger edit families: off-centre edits, mixed-axis edits, and edit sets
  whose stabilizer is not a subgroup of the axis stabilizers exercised here. The
  three-distinct-axis domain already reaches the trivial stabilizer, so the interesting direction is
  domains whose stabilizer is a different subgroup of the same order.
- Measure the size scaling of the floors across a longer ladder in `L`, which would turn
  the size dependence noted in the honest boundary into a quantitative law and would say
  whether the separation margin has an asymptote.

## Review record

Review-loop iteration 1 on 2026-08-11 narrowed the original arbitrary-edit-set
headline to the conditional finite-group implication and the four-domain
measurement actually supported. It corrected the collision proof's sidedness,
added the determinant-balance step omitted from the counting argument, changed
the state-collapse gate from one chosen representative per sign to every
constant-sign representative, and changed wrong-sign controls from a first-row
sample to the minimum across every measured frame in the branch. It also added
the independent pure-integer checker and source-bound runner caches.

Hard landing conditions are:

- `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` maps
  `physical_source_edit_set_signed_stabilizer_classification_cycle708_note_2026-08-02`
  to
  `scripts/physical_source_edit_set_signed_stabilizer_classification_cycle708_independent_check_2026_08_02.py`;
- both runner caches are fresh against their declared input fingerprints; and
- the citation-graph manifest is regenerated from the final landing tree.

No audit verdict is proposed by this record. Independent audit owns any
effective status after landing.

## Provenance context

The open (unlanded) sibling
`PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01` measures
two source domains by a coset-collapse argument. Those domains are the
one-edit and two-distinct-axis rows, re-derived inside this package rather than
copied. That sibling is open work and nothing
in this note depends on it.
