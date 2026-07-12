# S_3 Mass-Matrix No-Go Note

**Date:** 2026-04-17
**Claim type:** open_gate
**Status:** unaudited historical carrier-scope audit target; not publication-usable
**Script:** `scripts/frontier_s3_mass_matrix_no_go.py`
**Authority role:** historical proposed symmetry constraint; no current
retained authority for a physical `hw=1` generation carrier

This historical filename does not turn the row into a current no-go. The
physical carrier question remains open; the separate conditional lemma holds
only on a supplied abstract representation.

## Safe statement

Let `V = span(X_1, X_2, X_3)` be the `hw=1` triplet with the natural
axis-permutation action of `S_3`. Then `V ~= A_1 + E`, and every
`S_3`-invariant Hermitian operator on `V` has the form

```text
M = alpha I_3 + beta P_(A_1),
```

where `P_(A_1) = J_3 / 3` is the orthogonal projector onto the symmetric line.
Hence every such operator has spectrum

```text
{alpha, alpha, alpha + beta},
```

so the exact unbroken `S_3` class allows at most two distinct eigenvalues on
the `hw=1` carrier.

Under the residual axis-fixing subgroup `Z_2 < S_3`, the invariant Hermitian
space expands to real dimension `5`.

## Classical results applied

- Schur's lemma on `V ~= A_1 + E`
- the Hermitian spectral theorem
- the fixed-space dimension formula `dim End(V)^G = sum_i m_i^2`

## Historical physical-carrier proposal (not authority)

- The old physical identification of `hw=1` as a generation carrier and reuse
  of the taste-cube decomposition are not established by this note or runner.
- They remain excluded external bridge questions; this source supplies no
  retained physical-carrier dependency.

## Why it matters on `main`

This legacy note is not current theorem authority. Its algebraic core has been
rescoped to the separate conditional `A_1 direct-sum E` lemma. Any future
physical flavor statement must independently identify its carrier and group
action before consuming that abstract result.

## Verification

Run:

```bash
python3 scripts/frontier_s3_mass_matrix_no_go.py
```

The runner checks the invariant-algebra dimension, the form
`alpha I_3 + beta P_(A_1)`, the forced two-value spectrum, and the residual
`Z_2` dimension jump from `2` to `5`.
