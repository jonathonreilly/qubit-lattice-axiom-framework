# Exact independent-set strata and one-edge mask families on C43 — Cycle 761

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded exact finite calculation

Claim type: bounded_theorem

Runners:

- [`frontier_cycle761_c43_independent_set_census_2026_07_28.py`](../scripts/frontier_cycle761_c43_independent_set_census_2026_07_28.py)
- [`frontier_cycle761_c43_independent_set_census_independent_check_2026_07_28.py`](../scripts/frontier_cycle761_c43_independent_set_census_independent_check_2026_07_28.py)

Receipt:

- [`c43_independent_set_census_cycle761_receipt_2026_07_28.json`](../outputs/c43_independent_set_census_cycle761_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Exact finite result

Let `C_n` be the labelled cycle graph on vertices `0,...,n-1`, and let
`I(C_n,k)` count its independent vertex sets of cardinality `k`. For `k=0`,
`I(C_n,0)=1`; for `1 <= k <= floor(n/2)`,

`I(C_n,k) = binom(n-k,k) + binom(n-k-1,k-1)
           = n binom(n-k,k)/(n-k)`.

At `n=43`, the 22 strata for `k=0,...,21` are

`[1, 43, 860, 10621, 90687, 567987, 2701776, 9970840, 28915436,
66335412, 120609840, 173376645, 195747825, 171655785, 115000920,
57500460, 20764055, 5167525, 826804, 76153, 3311, 43]`.

Their sum is exactly `969,323,029`, the Lucas number `L_43`.

Separately, the 43 labelled adjacent-pair masks
`{j,(j+1) mod 43}` are distinct. In each mask both occupied endpoints have
an occupied neighbor, so the complete local occupied-endpoint incidence
count is `43 * 2 = 86`.

There is also an exact labelled family with one occupied edge. For every
`k=12,...,21`, labelled edge `{j,(j+1) mod 43}`, and phase `p` in `{0,1}`,
define

`S(k,j,p) = {j,j+1} union
             {j+3+p+2r (mod 43) : 0 <= r < k-2}`.

Every `S(k,j,p)` has cardinality `k` and exactly one occupied edge, namely
`{j,j+1}`. The masks are pairwise distinct, so this family contains exactly
`10 * 43 * 2 = 860` masks. Exactly the two endpoints of the unique occupied
edge have an occupied neighbor in each mask, giving `860 * 2 = 1,720`
occupied-endpoint incidences across the family.

Extension boundary (2026-07-31): the 22 independent-set strata, `L_43`
total, 43 adjacent-pair masks, and 86 adjacent-pair incidences above were
already present on live main before this extension. The only new finite result
in this extension is the exact 860-mask one-edge family and its 1,720
occupied-endpoint incidences.

## Proof and executable checks

Split an independent set according to whether vertex 0 is absent or present.
The absent class is a `k`-set on a path of length `n-1`, counted by
`binom(n-k,k)`. The present class excludes vertices 1 and `n-1` and chooses
`k-1` nonadjacent vertices on a path of length `n-3`, counted by
`binom(n-k-1,k-1)`. This proves the stratum formula. Summing the cycle
independence polynomial gives the Lucas recurrence and the stated total.

For the one-edge family, rotate so that `j=0`. The additional occupied
vertices have offsets `3,5,...,2k-3` when `p=0`, or
`4,6,...,2k-2` when `p=1`. Since `12 <= k <= 21`, these offsets are distinct,
lie between 3 and 40, and differ pairwise by at least 2. They are therefore
nonadjacent to each other and to the occupied edge endpoints 0 and 1. Thus
the edge `{0,1}` is the unique occupied edge and the mask has
`2+(k-2)=k` vertices. The unique occupied edge recovers `j`, cardinality
recovers `k`, and the least additional offset recovers `p`, proving that all
860 masks are distinct. Rotation proves the statement for every `j`.

The dependency-free primary runner evaluates both forms of the closed
formula, the path-polynomial split, the Lucas recurrence, all 43
adjacent-pair masks, and all 860 masks in the one-edge family. The independent
checker does not import the primary: it recomputes the `C43` strata by a
first/last-state dynamic program, brute-force checks all labelled masks for
`C_n` with `3 <= n <= 18`, reconstructs the one-edge family as vertex sets,
derives its size structurally, recounts its edges and local incidences, and
executes the primary in a fresh subprocess.

## Scope boundary

This is a finite graph-combinatorics support result only. It does not evaluate
or validate any mapper, reversible word, controller, anchor, covariance,
preparation procedure, orbit, quantum state, physical law, framework
Admissibility condition, no-go statement, or retained-grade claim. It imports
no result from the rejected Cycle-739 or Cycle-740 packets and assigns them no
premise weight. Independent claim audit remains required; the audit lane may
classify this numerical specialization as decoration.
