# DM Neutrino Triplet Even-Response Theorem

**Date:** 2026-04-15  
**Status:** support - structural or confirmatory support note
**Script:** `scripts/frontier_dm_neutrino_triplet_even_response_theorem.py`

**Audit-lane runner update (2026-05-09):** the primary runner `scripts/frontier_dm_neutrino_triplet_even_response_theorem.py` exits 0 with PASS in the current cache; the prior audit verdict citing a nonzero exit was generated against a stale cache and is invalidated by this source-note hash drift. The runner output and pass/fail semantics are otherwise unchanged.

**Symbolic-proof companion (2026-05-23):** the prior audit verdict
(`audited_failed`, 2026-05-10) flagged that a single-instance numerical check
cannot establish the universal exact factorization or the word "exactly" for
the even sector. The runner now carries a `sympy` symbolic-parameter proof
(Part 4) that closes that gap. Over symbolic real parameters
`(A, b, c, d, delta, rho, gamma)` with `H = H_core + B(delta, rho, gamma)` as
in the cited breaking-triplet CP theorem note, the same
`K_mass = R^T U_Z3^dagger H U_Z3 R` transform reduces
`Im[(K_mass)01^2] - (-2 gamma (delta + rho) / 3)` and
`Im[(K_mass)02^2] - ( 2 gamma (A + b - c - d) / 3)` to `0` identically; the
partial-derivative check then exhibits the full gradient in the six even
coordinates and shows `cp1` depends on no even coordinate other than the
combination `delta + rho` and `cp2` on no even coordinate other than
`A + b - c - d`. Together these establish the universal two-channel theorem
over the full breaking-triplet coordinate space, not just at a single
numerical point.

## Question

Once the CP-odd source `gamma` is isolated, what exactly is the even sector it
couples to in the DM CP tensor?

## Bottom line

Exactly two even response channels:

- `E1 = delta + rho`
- `E2 = A + b - c - d`

and the intrinsic tensor factorizes as

- `cp1 = -2 gamma E1 / 3`
- `cp2 =  2 gamma E2 / 3`.

Under character conjugation `phi -> -phi`:

- `gamma` is odd
- `E1` and `E2` are even
- `cp1` and `cp2` flip sign

So the last-mile denominator law is no longer a vague seven-variable problem.
It is:

- one odd source
- two even response channels

## What this closes

This closes the **form** of the response law.

The branch no longer has to say only “derive the triplet somehow.” It can now
say exactly:

- source leg: `gamma`
- response legs: `E1`, `E2`
- leptogenesis tensor: odd times even

## What this does not close

This note does **not** derive the actual values of `gamma`, `E1`, or `E2`.

It only fixes the exact response structure they must satisfy.

## Command

```bash
python3 scripts/frontier_dm_neutrino_triplet_even_response_theorem.py
```
