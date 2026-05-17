# Route Portfolio
# Loop: bae-f1f3-and-u0-su2-positive-closure-20260517

## Active routes for F1 vs F3 selection on `Herm_circ(3)`

| # | Route | Cycle | Pre-prob | Status | Outcome |
|---|---|---|---|---|---|
| 1 | NCG / KO-dim real-structure spectral triple | 1 / A | ~18% | shipped | Honest gap. Canonical `J = U_swap * K` constructed; spectral action on `H_R` = spectral action on `C^3`; F1 not selected. |
| 2 | `U_0` SU(2) gauge anchor | TBD | TBD | not started | — |
| 3 | Operator-class change (off `Herm_circ(3)`) | TBD | low | not started | Per 30-probe campaign, blocked across `hw = N` for `N = 1, 2, 3`. |
| 4 | Non-spectral functional class | TBD | low | not started | Block-total Frobenius F1 is such, but no derivation supplies it as canonical. |
| 5 | Larger-symmetry breaking | TBD | very-low | not started | S_3 (Probe V-S_3) and C_3-cycle (Probe 23) already ruled out. |

## Active routes for `U_0` SU(2) closure (separate target)

| # | Route | Cycle | Pre-prob | Status | Outcome |
|---|---|---|---|---|---|
| - | `U_0` SU(2) positive closure | TBD | TBD | not started | Separate from F1-vs-F3. |

## Cycle 1 detailed findings (NCG / KO-dim route)

**Construction:** Anti-unitary `J : C^3 -> C^3` defined as
`J(z) := U_swap * conj(z)`, where `U_swap = perm((0)(12))` swaps
indices 1 and 2. Verified:

- `J^2 = +I` (KO-dim 0 mod 8 family)
- `J C J^{-1} = C^{-1} = C^2` (orbit-orientation reversal)
- `[D, J] = 0` for every circulant Hermitian `D = a I + b C + b̄ C^2`
  with complex `b` (strict improvement over Probe 13's `K`, which
  only commutes for real `b`)
- `H_R = +1` eigenspace of `J` is 3-real-dim with explicit
  orthonormal basis `{e_1, e_2, e_3}`
- `D|_{H_R}` is real symmetric `3 x 3` with eigenvalues identical
  to `D` on full `C^3`

**Negative core:** Spectral action `Tr_{H_R} f(D / Lambda)` = spectral
action `Tr_{C^3} f(D / Lambda)` (same eigenvalues), so the functional
is a symmetric function of `(lambda_0, lambda_om, lambda_omb)`.
Doublet eigenvalues are counted as two distinct eigenvalues; F1
weighting `(1, 1)` is not achieved.

**Admission reduction:** Probe U's 4-primitive count (`J`, `gamma`,
cutoff `f`, spectral action principle) reduces to 3 (the canonical `J`
is now derived, not admitted). The remaining 3 primitives still need
disposition.

## Honest assessment

The Cycle 1 route was tested at the highest single-route positive
probability (~18%). Outcome is honest gap with shipped partial-
narrowing. The structural conclusion of the 30-probe campaign is
unchanged: closing F1 selection requires a multiplicity-counting
principle outside the spectral-action / eigenvalue-symmetric route
class.

Subsequent cycles should attack orthogonal routes (e.g., `U_0` SU(2)
gauge anchor) or accept the F1-vs-F3 selection as a structural feature
of the framework's `C_3` rep theory on `Herm_circ(3)` (path B / honest
gap on the campaign's terminal residue).
