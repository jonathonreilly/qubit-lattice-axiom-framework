# Promotion Value Gate — Cycle 700

Answered before the PR. Not an audit certificate; predicts no audit verdict.

## V1 — obstruction

This cycle does not target an `audited_conditional` row's verdict text. It
targets a **review finding**, which the trace-gate vocabulary admits as a
blocker source. Verbatim from the review-loop findings on PR #5620:

> "C8 checks only occupied-site neighbour content maps on one fixture. It does
> not quantify over an arbitrary nearest-neighbour rule and does not check
> conditions at unrecorded sites. Under a perfectly local,
> translation/rotation-covariant availability rule that makes a site's
> available set empty when it has two occupied neighbours, two individually
> admissible singleton configurations at separation two can make their empty
> midpoint unavailable."

U4 supplies exactly the quantified statement that was missing, for every
nearest-neighbour rule, and U5 identifies the hypothesis the rejected step
needed. The finding is closed rather than worked around.

## V2 — new derivation, with the sweep

**Searched commit `fbd9dd622e03692a3d518fb69b0d0e910e9385b5`**, refreshed with
`git fetch origin main:refs/remotes/origin/main` immediately before the sweep.

| # | command | hits | classification |
|---|---|---|---|
| U1 | `git grep -n -iE "closed under (disjoint )?union\|union of (two )?admissible\|admissib.*compos(e\|ition)\|compos.*admissib" origin/main -- 'docs/*.md'` | Born-form decompositions, gauge sector labels, `GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13`, generation moduli, Koide observable restriction | **nonmatching.** The composition-minimality theorem concerns composing two commuting star-embeddings of `M_2(C)`, not union-closure of admissible configurations. The others use "admissible" for decompositions and dial points. |
| U2 | `git grep -n -iE "do(es)? not compose\|non.composab\|fails to compose" origin/main -- 'docs/*.md'` | four hits, all in `work_history/repo/review_feedback/` | **context-only.** Review-feedback prose about specific gates and interfaces, not a closure theorem. |
| U3 | `git grep -n -iE "admissib.*(many.body\|joint constraint)\|frustrat" origin/main -- 'docs/*.md'` | hard-core boson non-frustration remark; frustration-free history Hamiltonians in tournament notes | **nonmatching.** Frustration-freeness of a Hamiltonian is a different property from closure of a configuration set. |

No landed note states that admissible configurations fail union or subset
closure, or gives the separation condition. New content: U2's two witnesses
under the two semantics, U3's subset witness, U4's rule-independent theorem
with tightness, and U5's threshold table.

## V3 — could the audit lane do it from retained primitives plus standard math?

The combinatorics is elementary — U4's proof is two lines. What is not
available to the audit lane is the observation that the additivity clause's
quantifier depends on an unspecified rule, and the construction of covariant
rules that break closure in each direction while satisfying the axiom's
"vary with the nearest-neighbor conditions" requirement. The audit lane's
current position is that additivity applies to any pairwise-disjoint
collection; this shows what that presumes.

## V4 — non-trivial?

Yes. Two of the results are counterexamples, which cannot be textbook
identities, and each is exhibited concretely. U4 is a positive theorem
quantified over all nearest-neighbour rules with an exhibited tightness
witness. U2's demonstration that the two site semantics disagree on a concrete
union is a distinct finding from either closure failure.

## V5 — one-step variant?

**Checked against `origin/main` at `fbd9dd622e`.** No. Against this campaign's
own cycles: 698 and 699 concern readout functionals and kernels and contain no
admissibility rule, no configuration-closure question, and no semantics
distinction. Against the rejected block: this is the repair of a finding
against it, and it reaches the opposite kind of conclusion — a hypothesis that
makes the step valid, rather than the step itself.

**Verdict: PR allowed.**
