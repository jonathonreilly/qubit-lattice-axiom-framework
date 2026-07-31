# Exact independent-set strata and adjacent-pair incidences on C35 — Cycle 756

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded exact finite calculation

Claim type: bounded_theorem

Runners:

- [`frontier_cycle756_c35_independent_set_census_2026_07_28.py`](../scripts/frontier_cycle756_c35_independent_set_census_2026_07_28.py)
- [`frontier_cycle756_c35_independent_set_census_independent_check_2026_07_28.py`](../scripts/frontier_cycle756_c35_independent_set_census_independent_check_2026_07_28.py)

Receipt:

- [`c35_independent_set_census_cycle756_receipt_2026_07_28.json`](../outputs/c35_independent_set_census_cycle756_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Exact finite result

Let `C_n` be the labelled cycle graph on vertices `0,...,n-1`, and let
`I(C_n,k)` count its independent vertex sets of cardinality `k`. For `k=0`,
`I(C_n,0)=1`; for `1 <= k <= floor(n/2)`,

`I(C_n,k) = binom(n-k,k) + binom(n-k-1,k-1)
           = n binom(n-k,k)/(n-k)`.

At `n=35`, the 18 strata for `k=0,...,17` are

`[1, 35, 560, 5425, 35525, 166257, 573300, 1480050, 2877875,
4206125, 4576264, 3640210, 2057510, 791350, 193800, 27132, 1785, 35]`.

Their sum is exactly `20,633,239`, the Lucas number `L_35`.

Separately, the 35 labelled adjacent-pair masks
`{j,(j+1) mod 35}` are distinct. In each mask both occupied endpoints have
an occupied neighbor, so the complete local occupied-endpoint incidence
count is `35 * 2 = 70`.

## Proof and executable checks

Split an independent set according to whether vertex 0 is absent or present.
The absent class is a `k`-set on a path of length `n-1`, counted by
`binom(n-k,k)`. The present class excludes vertices 1 and `n-1` and chooses
`k-1` nonadjacent vertices on a path of length `n-3`, counted by
`binom(n-k-1,k-1)`. This proves the stratum formula. Summing the cycle
independence polynomial gives the Lucas recurrence and the stated total.

The dependency-free primary runner evaluates both forms of the closed
formula, the path-polynomial split, the Lucas recurrence, and all 35
adjacent-pair masks. The independent checker does not import the primary: it
recomputes the `C35` strata by a first/last-state dynamic program, brute-force
checks all labelled masks for `C_n` with `3 <= n <= 18`, recounts the local
incidences, and executes the primary in a fresh subprocess.

## Scope boundary

This is a finite graph-combinatorics support result only. It does not evaluate
or validate any mapper, reversible word, controller, anchor, covariance,
preparation procedure, orbit, quantum state, physical law, framework
Admissibility condition, no-go statement, or retained-grade claim. It imports
no result from the rejected Cycle-739 or Cycle-740 packets and assigns them no
premise weight. Independent claim audit remains required.
