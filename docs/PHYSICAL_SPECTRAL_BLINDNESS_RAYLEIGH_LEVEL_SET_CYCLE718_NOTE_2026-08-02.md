# The Frame Dependence Is Non-Spectral: The Rayleigh Transfer and the Level-Set Law — Cycle 718

Date: 2026-08-02

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

## Setting

The open-coframe static Hessian `Q(L)` is assembled by the cycle-696 compiler
[physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
on an `L x L x L` box with a free (unwrapped) boundary. The 24 proper rotations
of the cube act on the static variable index by relabelling; write `P_a` for the
permutation carried by frame `a`, and `Q_g` for the operator reassembled in frame
`g`. The measured degree-of-freedom counts are `n = 98` at `L = 3` and `n = 279`
at `L = 4`, at scale `2.9e+01`. The identity-frame operator is symmetric to
`0.0e+00` at both sizes.

Cycle `physical_source_stabilizer_coset_collapse_k_sign_law_cycle707` measured
the stabilizer sextet `S = [1, 4, 9, 15, 18, 23]`; cycle
`physical_frame_group_factorization_cycle715` showed the reassembled operator is
constant on the right cosets `S.g`; cycle
`physical_complete_averaging_set_frame_blindness_classification_cycle716`
classified the frame-blind averaging sets over the complete powerset; and cycle
`physical_body_diagonal_frame_functional_transversal_law_cycle717` named the
four-valued invariant as the body diagonal `delta(g)` that frame `g` carries onto
`(1, 1, 1)`, with the four fibres of `delta` equal to the right cosets of the
sextet.

The sextet and the degree-of-freedom counts are still **measured, not derived**,
from the assembled operator here.

## The question this cycle answers

Cycles 715–717 established *what* the frame dependence is a function of. They did
not say *where in the operator* it lives, nor why averaging over a transitive
subgroup should make a value agree when the underlying objects plainly do not.
This cycle answers both: the frame dependence is entirely non-spectral, and
blindness is a coincidence of one scalar level, never an equality of the
compared objects.

## Theorem A — reassembly is an orthogonal relabelling, so the spectrum cannot see the frame

Reassembly in frame `g` is exactly conjugation by the permutation matrix of `P_g`:

    Q_g = P_g Q P_g^T,   deviation 0.0e+00 over all 24 frames, at L = 3 and L = 4.

A permutation matrix is orthogonal, so all 24 reassembled operators are
orthogonally similar and therefore isospectral. The measurement confirms it
against four independent spectral summaries: sorted eigenvalues agree to
`1.8e-13` at `L = 3` and `4.3e-13` at `L = 4`, and trace, Frobenius norm and
log-determinant agree to `1.7e-13` and `1.8e-12` respectively.

The frame dependence is nevertheless real and large in the entries: two frames on
the same body diagonal differ by at most `1.2e-10`, while two frames on different
diagonals differ by at least `4.0e+00` — ten orders apart from the
same-diagonal residual, at both sizes.

The spectral comparison is not a vacuous gate. A rank-one bump of size `1.0e-03`
added to the identity-frame operator moves its spectrum by `2.3e-04` at `L = 3`
and `2.1e-04` at `L = 4` — some nine orders above the isospectrality residual. A
spectral difference of the size the entries suggest would have been seen.

## Theorem B — the explicit conjugator, and the index that fails

The similarity is not only existential. For every ordered pair of frames `(a, b)`
the conjugator is the inverse-left product `b^-1 a`:

    Q_a = P_{b^-1 a} Q_b P_{b^-1 a}^T,   deviation 0.0e+00 over all 576 pairs.

The reversed product `a b^-1` is not a conjugator. On the 456 ordered pairs where
the two products differ, the reversed index fails by up to `4.0e+00` — the full
cross-diagonal scale. This is the discriminating form of the identity: the gate
would fail outright if the index convention were the other one, at both sizes.

## Theorem C — the frame moves off the operator and onto the source

Let `b` be a source vector, `bbar_A = sum_{a in A} P_a^T b` the source averaged
over a collection `A` of frames, and

    v_A(g) = <bbar_A, Q_g^-1 bbar_A> / <bbar_A, bbar_A>

the value functional of cycles 707 and 715–717. Because `P_g^T bbar_A = bbar_{gA}`,

    v_A(g) = R(bbar_{gA}),   R(u) = u^T Q^-1 u / ||u||^2,

where `Q` is the **single fixed** identity-frame operator. The frame index has
been removed from the operator entirely and moved onto the source. Measured over
120 evaluations per source, the two sides agree to `2.2e-16` and `6.0e-16` at
`L = 3`, and to `5.9e-14` and `2.0e-14` at `L = 4`, for two independent generic
sources at each size.

This is the structural content of Theorem A made usable: there is one operator,
not 24, and the whole frame story is a story about where the source points.

## Theorem D — the weight law and the hull bound

Diagonalise the identity-frame operator, `Q = V diag(lambda) V^T`, and set
`c = V^T u`, `w_k = c_k^2 / ||c||^2`. Then

    R(u) = sum_k w_k / lambda_k,

a weighted mean of inverse eigenvalues with non-negative weights summing to one.
The identity is measured to `3.1e-15` and `7.9e-15` at `L = 3`, and to `7.4e-14`
and `5.3e-14` at `L = 4`.

Two consequences follow with no further measurement. First, every value the
functional can take — for any source, any collection, any frame — lies in the
convex hull of the inverse eigenvalues. The measured hull is `-7.1e-01` to
`2.1e+00` at `L = 3` and `-2.3e+00` to `2.7e+01` at `L = 4`, and the observed
values sit strictly inside it with margins `6.2e-01` and `5.7e-01` at `L = 3` and
`2.3e+00` and `2.2e+00` at `L = 4`. Second, the operator is indefinite — the hull
straddles zero at both sizes — so the value functional is not a norm and no
positivity argument is available to it.

## Theorem E — the level-set law: four levels, and they are the diagonal fibres

Take the singleton collection and let the frame vary. The 24 pulled-back sources
are pairwise well separated: at least `1.2e+01` apart at `L = 3` and `2.1e+01` at
`L = 4`. They are 24 genuinely different vectors.

The scalar `R` nevertheless takes exactly four values on them, and its level sets
are exactly the four body-diagonal fibres of six frames each. At `L = 3` the
within-fibre spread is `3.0e-12` against a between-fibre gap of `2.7e-03` (ratio
`9.2e+08`) for the first source and `2.7e-12` against `2.2e-02` (ratio `8.0e+09`)
for the second; at `L = 4`, `1.9e-10` against `5.6e-03` (ratio `3.0e+07`) and
`9.0e-11` against `1.7e-02` (ratio `1.8e+08`).

So the four-valued invariant of cycle 717 is realised in the value functional as
a level-set structure of a single Rayleigh quotient. The vectors within a fibre
are not equal; only their levels are.

## Theorem F — blindness is a coincidence of levels, not of sources

Cycle 716 found the minimum blind size to be four, and cycle 717 identified the
minimal blind collections as the right cosets of the four regular subgroups —
those transitive on the diagonals. The runner rebuilds those four subgroups
independently and takes one such coset.

Its left stabiliser has order 4, so its 24 left translates collapse to 6 distinct
averaged sources. Those 6 sources are far apart — at least `2.4e+01` and
`1.6e+01` at `L = 3`, `3.7e+01` and `4.6e+01` at `L = 4` — and their spectral
weight vectors differ substantially, by `1.5e-05` to `8.5e-01` and `2.2e-05` to
`9.2e-01` at `L = 3`, and `1.3e-02` to `8.4e-01` and `3.4e-02` to `8.1e-01` at
`L = 4`. Yet they all take one value, to `2.8e-12` and `1.8e-12` at `L = 3` and
`6.6e-11` and `1.3e-11` at `L = 4`.

Six distinct vectors with distinct spectral weight profiles that land on one
number: blindness is a coincidence of levels. For contrast, a four-frame set
drawn from a single body diagonal has all 24 left translates distinct and spreads
`3.9e-02` and `7.0e-02` at `L = 3`, `5.2e-01` and `2.9e-01` at `L = 4`.

## The single-slot census — the size-dependent part, reported as such

The theorems above are size-stable. The next measurement is not, and the honest
reading matters.

Classify a source by which of the four diagonals it separates — 15 possible
coincidence patterns on four labels. Over the single-slot sources:

- At `L = 3`, the 98 slots realise 14 of the 15 patterns. The missing one is the
  all-distinct pattern: **no single-slot record at `L = 3` separates all four
  body diagonals.** The count of slots at the finest pattern is 0.
- At `L = 4`, the 279 slots realise all 15 patterns, and 48 of them separate all
  four diagonals.

The `L = 3` obstruction is therefore a box-size effect, not a law, and is
reported as such. Slots that are frame constant with no averaging at all — below
the generic floor of four that cycle 716 measured — number 6 at `L = 3`, in
direction classes `[1, 3, 7]`, and 19 at `L = 4`, in direction classes
`[5, 9, 11, 13]`: a different geometric family at each size.

Generic sources behave uniformly: 20 of 20 realise the finest pattern at both
sizes. The coincidences therefore belong to the individual slots, not to the
operator — which gives cycle 716's observation that structured sources blind more
collections than generic ones an explicit mechanism, and localises it in the
source rather than in the assembly.

## Boundary

The results are **computational identities** measured at `L = 3` and `L = 4` on
an unwrapped box, for the operator of the cycle-696 compiler. Theorems A–D are
algebraic and would hold for any symmetric operator carried by these
permutations; what is measured is that the compiler's operator is in fact carried
by them, at deviation `0.0e+00`, and the numerical size of every residual.
Theorems E and F are measured facts about this operator at these two sizes, and
the census section is explicitly size-dependent.

Two frames on the same body diagonal agree to `1.2e-10` rather than exactly; that
residual is the assembly's own floating-point floor and is ten orders below
the cross-diagonal scale, but it is not zero.

## What this cycle claims and does not claim

Claimed: for the reassembled static operator of the cycle-696 compiler on an
unwrapped box, at `L = 3` and `L = 4`, reassembly is conjugation by a permutation
matrix at deviation `0.0e+00`; the 24 reassembled operators are consequently
isospectral, so the frame dependence is entirely non-spectral while the entries
differ by at least `4.0e+00` across diagonals; the conjugator index is the
inverse-left product and the reversed product is rejected by up to `4.0e+00`; the
value functional equals a Rayleigh quotient of the single identity-frame operator
evaluated at a translated source; that quotient is a weighted mean of inverse
eigenvalues with non-negative weights, hence bounded by their convex hull; the
quotient's level sets on a generic frame orbit are exactly the four
body-diagonal fibres; and a minimal blind collection has 6 distinct averaged
sources, mutually far apart with differing spectral weights, that share one
value.

Not claimed: any statement about a continuum limit, about wrapped boundaries,
about box sizes beyond those measured, or about the audit status of this or any
other row. The single-slot census is claimed only at the two measured sizes and
is explicitly reported as size-dependent. No new axiom, primitive, or import is
proposed. The sextet and the degree-of-freedom counts remain inputs measured from
the compiler.

## Physics reading

Frame dependence in this sector is not a deformation of the operator — it is a
relabelling. Every spectral quantity a physicist would reach for first is frame
constant: eigenvalues, trace, norm, determinant. What changes is which
degree-of-freedom the source addresses, and the whole 24-frame structure reduces
to one fixed operator seen from a moving source.

That reframing explains the blindness family that cycles 716 and 717 counted.
Averaging over a transitive subgroup does not make the averaged sources agree —
they stay far apart, with visibly different spectral content. It makes their
Rayleigh levels agree. A frame-blind prescription is one whose translates land on
a common level set of a fixed quotient, and the nearest structure to that is a
regular subgroup of the rotation group acting on the cube diagonals. The value
functional holds at that structure, and the evidence ceiling in this lane is now
a statement about level coincidences of one scalar rather than about 24 separate
operators.

## Reproduction

Runner:
[physical_spectral_blindness_rayleigh_level_set_cycle718_2026_08_02.py](../scripts/physical_spectral_blindness_rayleigh_level_set_cycle718_2026_08_02.py)

Cold stdout and the machine-readable receipt are landed under `outputs/`. The
runner prints one line per gate and ends with a `TOTAL: PASS=` line; every
floating-point value quoted above is printed by the runner itself.
