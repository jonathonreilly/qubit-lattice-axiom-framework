# Physics Loop Goal — BAE F1-vs-F3 + U(1)_b SO(2) positive closure
# 2026-05-17

## Top-level target

Attempt positive closure of the F1 multiplicity-weighted Frobenius
measure (over F3 rank-weighted) as the canonical extremal principle on
`Herm_circ(3)`, the unique open derivation gap in the BAE closure
chain after the 30-probe BAE campaign + PR #1174 narrow theorem.

Pre-closure probability (BAE = F1-canonicality): low-bounded. The
30-probe campaign across six structural layers (operator,
wave-function, topological, thermodynamic, larger-symmetry,
NCG-spectral-action) consistently selects F3 (rank-`(1, 2)` weighting),
not F1 (multiplicity-`(1, 1)`). Closing F1 requires a
multiplicity-counting principle outside retained `C_3` rep theory on
`Herm_circ(3)`.

## Cycle 1 / Agent A — NCG / KO-dim real-structure route

**Pre-closure probability:** ~18% (highest single-route positive
probability per the brief).

**Strategy:** Build an explicit real spectral triple `(A_F, H_F, D, J, Gamma)`
with `J = U_swap * K` swapping the doublet eigenvectors. Test whether
KO-dim conditions on `J` (`J^2 = +I`, `[D, J] = 0` per chosen KO-dim)
project the spectral-action heat-kernel weights onto the **real
bimodule** with F1 isotype counting.

**Outcome:** Honest gap. Partial-narrowing note shipped.

- **Positive content (T1)-(T4):** Explicit canonical `J = U_swap * K`
  on `C^3` with `J^2 = +I`, `J C J^{-1} = C^{-1}`, and `[D, J] = 0` for
  every complex `b`. The `J`-real subspace `H_R` is 3-real-dim with
  explicit orthonormal basis on which `D` restricts to a real symmetric
  `3 x 3` matrix with the same eigenvalues as `D` on full `C^3`. This
  is a strict improvement over Probe 13 (where `K` alone only commuted
  with real-`b` `D`).

- **Negative core (T5):** The spectral-action functional on `H_R`
  equals the spectral-action functional on `C^3` (same eigenvalues),
  hence remains a symmetric function of `(lambda_0, lambda_om,
  lambda_omb)`. This weights the doublet pair as two distinct
  eigenvalues at the eigenvalue level (F3-style), not as a single bin
  (F1-style). The NCG / KO-dim route does NOT supply the F1 selector.

- **Counterfactual (T6):** Pointwise `K` alone does not commute with
  complex-`b` `D`. The `U_swap`-twist is what enables `J` to commute
  with the full complex-`b` doublet.

## What this closes / does NOT close

- **Closes:** the structural narrowing that the explicit canonical `J`
  exists and reduces Probe U's primitive admission count from 4 to 3
  (now `{gamma, cutoff f, spectral action principle}`).
- **Does NOT close:** F1 vs F3 weighting selection. The remaining gap
  is unchanged: a multiplicity-counting principle outside the
  spectral-action class is still required.

## Subsequent cycle targets (not pursued by this cycle)

- **U_0/SU(2) positive closure:** an orthogonal route to BAE via the
  `U_0` SU(2) gauge anchor. Not attacked by Cycle 1.
- **Multiplicity-counting principle hunt:** outside the
  spectral-action class. Open.
