# DM PMNS Chamber Spectral Completeness — Krawczyk-Interval Certificate

**Date:** 2026-05-16
**Lane:** DM A-BCC / open import `I11`
**Status:** bounded — existence-side certificate complements the parent note's
multistart enumeration; chamber-completeness upper bound is not derived
**Type:** support note (Krawczyk-interval certificate)
**Parent note:** `DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE_2026-04-20.md`

**Status authority:** independent audit lane only. This source note does
not set or move its own audit verdict; downstream audit lane and packet
status are decided by the audit lane.

**Primary runner:**
`scripts/frontier_dm_pmns_chamber_spectral_completeness_krawczyk_certificate_2026_05_16.py`

---

## 0. Why this note exists

The parent theorem note
`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE_2026-04-20.md` makes the
load-bearing claim

> The reduced real ordered-eigenvalue system has exactly four real roots on
> each of the two electron-axis-3 branches, and the independent
> all-permutation chamber solve finds no other chamber `chi^2 = 0` roots.

That claim is currently supported in the parent runner by:

1. a multi-start `scipy.optimize.root` solve from hardcoded basin coordinates
   and a 500-seed random box, and
2. an all-permutation direct chamber search seeded from the listed three
   chamber basins plus 250 random seeds per permutation.

Both legs are numerical multistart — they show the listed roots are
present, but they do not by themselves rule out additional real ordered
roots on either branch or additional chamber roots on the other four
permutations.

This source note records what we *can* certify on the existence side and is
explicit about what we cannot.

## 1. Bottom line

For each of the 8 candidate real ordered-eigenvalue triples listed in the
parent runner (4 on `sigma = (2,1,0)`, 4 on `sigma = (2,0,1)`), there is a
closed box

```text
B_k = {(l_1, l_2, l_3) : |l_i - l_i^(k)| ≤ 10^-6}    k = 1, ..., 8
```

such that:

- **K1** (existence + local uniqueness) — the reduced residual system
  `F_branch(l_1, l_2, l_3)` has a unique zero inside `B_k`, certified by
  the Krawczyk operator condition `K(B_k) ⊂ int(B_k)` evaluated at
  200-bit mpmath precision; the contraction margin per axis is at least
  `~ 8 × 10^-7` and the mid-point Jacobian determinant is bounded away
  from zero;
- **K2** (pairwise disjointness) — the four boxes on each branch are
  pairwise disjoint, so the corresponding zeros are eight distinct real
  ordered triples;
- **K3** (certified chamber-side sign) — over the three chamber-survivor
  boxes `B_{Basin 1}, B_{Basin 2}, B_{Basin X}` the chart-image margin
  `q(l_·) + δ(l_·) - sqrt(8/3)` is a strictly positive interval, and
  over the five non-survivor boxes
  `B_{Basin N}, B_{Basin P}, B_{X_a}, B_{X_b}, B_{X_c}` the same margin
  is a strictly negative interval — both verified by direct interval
  evaluation on the boxes.

What this note does **not** certify (carried over from the parent):

- **C1** an upper bound on the number of additional real ordered roots of
  the reduced system outside the union `⋃ B_k`;
- **C2** a Sturm / resultant univariate elimination certificate on either
  branch (the lex Groebner basis over `Q(√2, √3, √6)` did not terminate in
  the time budget allocated to this iteration);
- **C3** exclusion of chamber `chi^2 = 0` roots on the other four row
  permutations beyond the parent runner's multistart sweep.

So the present note tightens the parent runner's "existence" side from
multistart-with-hardcoded-seeds to a certified-existence-and-local-uniqueness
statement on disjoint boxes, but leaves the "no other roots" side as an
empirical chamber-search finding to be closed in a future certificate.

## 2. Setup

We use the reduced-system formulation from the parent runner. After the
linear elimination `delta(l), q(l)` derived from the two PMNS-angle linear
equations and the chart map `m = l_1 + l_2 + l_3`, the reduced residual on
each branch is

```text
F_branch(l_1, l_2, l_3) =
    (   eq_proj(d(l), q(l), l_1, l_2, l_3),
        Tr_chart(m, d(l), q(l)) - (l_1^2 + l_2^2 + l_3^2),
        det_chart(m, d(l), q(l)) - l_1 l_2 l_3    ).
```

Both `delta` and `q` are explicit rational functions in
`(l_1, l_2, l_3)` with coefficients in `Z[sqrt(6), sqrt(2), sqrt(3)]`.
The chart invariants `Tr_chart, det_chart` come from
`H(m, delta, q_+) = H_base + m T_m + delta T_delta + q_+ T_q` with the
parent runner's constants.

The 8 candidate triples are precisely the lambda images of the parent
runner's listed basins (`Basin 1, 2, N, P, X, X_a, X_b, X_c`),
each refined to residual `~ 10^-13` by the parent runner's Newton solve.

## 3. Krawczyk operator and result

For each candidate triple `c = l^(k)` and radius `r = 10^-6` form the box

```text
X = [c_1 - r, c_1 + r] × [c_2 - r, c_2 + r] × [c_3 - r, c_3 + r].
```

Let `Y` be the mid-point preconditioner — the point-valued inverse of the
mid-point Jacobian `J(c)` (computed at mpmath 200-bit precision); let
`J(X)` be the interval-evaluated Jacobian on `X` via forward-mode
automatic differentiation; let `F(c)` be the interval residual at the
mid-point. The Krawczyk operator is

```text
K(X) := c - Y F(c) + (I - Y J(X)) (X - c).
```

The runner verifies, axis by axis, that `K(X) ⊂ int(X)` — equivalently
that each axis margin between `K_i(X)` and the box wall is strictly
positive. The condition `K(X) ⊂ int(X)` together with invertibility of
the mid-point Jacobian (the runner reports the mid-point determinant) is
sufficient (Krawczyk-Moore) for existence and local uniqueness of a zero
of `F` in `X`. See the parent
DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE for the multistart
ordering and chamber inequality.

The runner reports a contraction margin of approximately the full
`r ≈ 10^-6` on every axis of every box, with mid-point Jacobian
determinants between `|det| ≈ 7.5` and `|det| ≈ 300` — a wide safety
factor.

For the chamber sign, the runner interval-evaluates
`q(l) + δ(l) - sqrt(8/3)` directly on each box; the resulting interval
is reported. For all three chamber survivors the interval is strictly
positive (e.g. `Basin 1: [+1.5849 × 10^-2, +1.5862 × 10^-2]`), and for
all five non-survivors the interval is strictly negative (e.g.
`Basin P: [-1.5296, -1.5295]`).

## 4. Theorem (certificate)

**Theorem (Krawczyk-interval certificate for the chamber-spectral roots).**
Fix the PMNS target triple
`(sin^2 θ_12, sin^2 θ_13, sin^2 θ_23) = (0.307, 0.0218, 0.545)`. On the
affine DM Hermitian family
`H(m, δ, q_+) = H_base + m T_m + δ T_δ + q_+ T_q` the reduced
ordered-eigenvalue residual system `F_branch` of
DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE_2026-04-20 has

  - **at least four** distinct real ordered roots on the branch
    `sigma = (2,1,0)`, located inside disjoint Krawczyk boxes of radius
    `10^-6` around the listed candidates `Basin 1, 2, N, P`;
  - **at least four** distinct real ordered roots on the branch
    `sigma = (2,0,1)`, located inside disjoint Krawczyk boxes of radius
    `10^-6` around the listed candidates `Basin X, X_a, X_b, X_c`;
  - the chamber half-space `q + δ ≥ sqrt(8/3)` strictly contains the
    boxes around `Basin 1, Basin 2, Basin X` and is strictly disjoint
    from the boxes around `Basin N, Basin P, X_a, X_b, X_c`.

**Proof.** The Krawczyk-Moore theorem (Neumaier, *Interval Methods for
Systems of Equations*, 1990, Thm 5.1.7) gives: if `K(X) ⊂ int(X)` and
`J(X)` is non-singular over the box, then `F` has a unique zero in `X`.
The runner verifies both conditions for each of the eight boxes at 200-bit
mpmath precision; the per-axis margins and the mid-point Jacobian
determinants are reported in the runner output. Pairwise disjointness of
the eight boxes follows directly from the explicit listed centers and the
fixed radius `r = 10^-6`. The chamber margin certificates are direct
interval evaluations of `q(l) + δ(l) - sqrt(8/3)` on each Krawczyk box,
also reported in the runner output. ∎

## 5. Scope versus parent theorem

| Parent theorem claim | Status in parent | Status here |
|---|---|---|
| `sigma=(2,1,0)` reduced system has exactly four real ordered roots | numerical multistart | **at least four**, each certified |
| `sigma=(2,0,1)` reduced system has exactly four real ordered roots | numerical multistart | **at least four**, each certified |
| chamber cut keeps exactly `{Basin 1, Basin 2, Basin X}` (≥ 1) | derives from above + interval `q + δ - sqrt(8/3)` evaluation | certified for the listed 3 survivors and 5 non-survivors |
| chamber cut keeps exactly `{Basin 1, Basin 2, Basin X}` (≤ 1) | inherits the parent "exactly four roots" claim | **not certified** here |
| all-permutation direct chamber solve finds no other chamber root | 250 seeds per permutation, multistart | not strengthened |

So this note closes the **existence side** of the parent theorem
rigorously and demarcates the unclosed **upper-bound side**. The
chamber-survivor sign list itself is now an exact interval inclusion of
the chamber half-space.

## 6. What this does and does not say

What is closed:

- the eight listed reduced-spectral candidates are each certified real
  ordered roots, in disjoint boxes of radius `10^-6`;
- the listed three chamber survivors are certified to lie strictly inside
  the active chamber half-space; the five non-survivors are certified to
  lie strictly outside it.

What is not claimed:

- no statement about additional reduced-spectral roots outside the listed
  8 boxes;
- no statement about chamber `chi^2 = 0` roots on the four non-listed row
  permutations beyond the parent's multistart sweep;
- no Sturm / resultant univariate elimination certificate;
- the parent's "exactly four real ordered roots per branch" upper bound
  is still inherited as an empirical multistart result, not as a
  Krawczyk-style certificate.

## 7. Open work

The honest next step for full chamber-completeness closure is either

- a Sturm / Krawczyk exclusion sweep on a partitioned cover of the
  reduced-system search region with explicit bounds on the spectral
  norms `|l_i|`, or
- a successful Groebner-basis-based univariate elimination over the
  algebraic field `Q(sqrt(2), sqrt(3), sqrt(6))` with `sympy.count_roots`
  applied to the resulting univariate polynomial.

Both are out of scope for this iteration's time budget and are left to
future work. The bounded-status box of this note records exactly that.

## 8. Reproduction

```bash
PYTHONPATH=scripts python3 \
    scripts/frontier_dm_pmns_chamber_spectral_completeness_krawczyk_certificate_2026_05_16.py
```

Expected final line:

```text
PASS=18  FAIL=0
```
