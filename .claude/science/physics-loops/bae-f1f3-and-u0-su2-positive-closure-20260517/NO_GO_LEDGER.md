# No-Go / Honest-Gap Ledger
# Loop: bae-f1f3-and-u0-su2-positive-closure-20260517

This ledger records routes attacked and not closed positively, so future
cycles can prune the search space.

## 2026-05-17 — Cycle 1 / Agent A — NCG / KO-dim route

**Outcome:** Honest gap (partial-narrowing).

**Mathematical content shipped as positive:**

- Canonical anti-unitary involution `J = U_swap * K` on `C^3` with
  `J^2 = +I`, `[D, J] = 0` for every complex `b`.
- The `J`-real subspace `H_R` is 3-real-dim with explicit orthonormal
  basis; `D` restricted to `H_R` is real symmetric `3 x 3` with same
  eigenvalues as `D` on `C^3`.

**Mathematical content shipped as negative (structural narrowing):**

- The spectral-action functional on `H_R` equals the spectral-action
  functional on `C^3` (same eigenvalues), so the doublet pair
  `(lambda_om, lambda_omb)` is counted as two eigenvalues. F1
  multiplicity weighting `(1, 1)` is not supplied by `J`-projection.

**What the route does not close:** F1 vs F3 selection on
`Herm_circ(3)`.

**Why:** The eigenvalue spectrum of `D` is unchanged by projection
onto the `J`-real subspace. The spectral-action functional remains a
symmetric function of three eigenvalues. F1 weighting requires
collapsing `(lambda_om, lambda_omb)` into a single isotype bin, which
no `J` construction can achieve (the doublet eigenvalues are
algebraically distinct for generic `b`).

**Prior closely-related routes (prune-by-similarity):**

- Probe 13 (`K, T_alg, *, Theta_H, CPT` antilinear involutions, all
  discrete) — Cycle 1's `J = U_swap * K` is a strict generalization of
  `K`; the eigenvalue structure is unchanged.
- Probe U (NCG spectral triple with `D = H_circ`, unspecified `J`) —
  Cycle 1 supplies canonical `J` but does not change the negative
  conclusion.

## Recommended pruning rules for subsequent cycles

1. **Eigenvalue-symmetric routes are precluded.** Any closure route
   whose extremal functional is a symmetric function of `(lambda_0,
   lambda_om, lambda_omb)` cannot select F1 over F3, because F1
   weighting requires breaking the doublet-eigenvalue symmetry. This
   eliminates: spectral action, heat-kernel expansion coefficients,
   power-sum functionals, trace functionals.

2. **Real-structure / antilinear-involution routes are precluded.**
   Any real structure `J` on `C^3` with `J^2 = +I` (KO-dim 0, 1, 6, 7)
   or `J^2 = -I` (KO-dim 2, 3, 4, 5) has a real form of dimension 3
   (matching the eigenvalue count), so projection onto the real form
   does not collapse the doublet count.

3. **Productive directions (not pursued by Cycle 1):**

   - **Operator-class change:** Move from `Herm_circ(3)` to a
     different operator class where the doublet has algebraic
     constraint forcing degeneracy. Probe 25 + 27 + 28 reported this
     line is blocked across `hw = N` for `N = 1, 2, 3`.

   - **Non-spectral functionals:** Functionals that depend on `(a, b)`
     directly (not through the eigenvalue spectrum) could in principle
     break the symmetry. The block-total Frobenius F1 itself is such a
     functional, but no derivation supplies F1 as canonical from
     retained content.

   - **Larger-symmetry breaking:** Probe V-S_3 ruled out S_3-action
     directly on `Herm_circ(3)`. Could a different group action that
     breaks the doublet symmetry be retained? Probe 23 tested the
     C_3-cycle and was ruled out.

   - **`U_0` SU(2) gauge anchor:** Separate route not yet attacked.
     Strategy: `U_0` as a 2-d gauge anchor where the F1 / F3 split
     manifests as an SU(2) vs SO(3) distinction. To be investigated
     in subsequent cycles.

4. **The structural finding from the 30-probe campaign stands:**

   > Closing BAE / F1 selection requires a multiplicity-counting
   > principle outside the spectral-action class on `Herm_circ(3)`.

   No such principle was identified in Cycle 1.
