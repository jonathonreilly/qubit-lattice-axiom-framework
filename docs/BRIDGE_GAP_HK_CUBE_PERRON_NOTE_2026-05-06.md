# Bridge Gap — HK Cube Perron (Legacy Identity): Finite Weighted-Transfer Theorem

**Date:** 2026-05-06; narrowed and independently reconstructed 2026-07-16
**Type:** positive_theorem
**Claim type:** positive_theorem
**Status:** candidate self-contained finite numerical-linear-algebra theorem;
independent audit remains required. The historical HK/cube/Perron words in the
stable title and path are identity only.
**Authority role:** source-note proposal. Audit verdict and downstream status
are set only by the independent audit lane.
**Primary runner:**
[`scripts/probe_hk_cube_perron_l2_2026_05_06.py`](../scripts/probe_hk_cube_perron_l2_2026_05_06.py)

## Exact scope

This note defines finite functions and matrices and proves their elementary
spectral properties. It then gives independently reconstructed numerical
enclosures for three separate finite matrices, at `N = 6, 7, 8`.

The definitions are stipulations inside this theorem. They are not derived
from, or identified with, an SU(3) heat-kernel action, a lattice-cube measure,
a physical plaquette, a canonical Brownian time, a topology or link count, a
Wilson comparison, or a thermodynamic observable. The formal parameter is set
to `t = 1` by definition, not by framework authority.

## Definitions

Let `N` be a nonnegative integer and order the finite square box

```text
W_N := {(p,q) : 0 <= p <= N and 0 <= q <= N}
```

lexicographically. Its cardinality is `m_N = (N+1)^2`.

For nonnegative integers `p,q`, define

```text
d(p,q) := ((p+1)(q+1)(p+q+2))/2,                                      (1)
c(p,q) := (p^2 + pq + q^2 + 3p + 3q)/3.                               (2)
```

The first expression is an integer: if either `p+1` or `q+1` is even, their
product is even; if both are odd, their sum `p+q+2` is even. The second is a
nonnegative rational number and vanishes only at `(0,0)`.

Let

```text
S := {(1,0), (-1,1), (0,-1), (0,1), (1,-1), (-1,0)}.                   (3)
```

Define the `m_N x m_N` recurrence matrix, with rows and columns indexed by
`W_N`, by

```text
(J_N)_(x,y) := 1/6  if x-y is in S,
               0    otherwise.                                       (4)
```

The finite-box truncation is exactly the restriction to pairs `x,y` that both
belong to `W_N`; no boundary wrap or extra edge is added.

For a formal real parameter `t`, define the exponential functions

```text
w_t(p,q)   := d(p,q) exp(-t c(p,q)/2),                                 (5)
a_t(p,q)   := w_t(p,q)/d(p,q) = exp(-t c(p,q)/2),                       (6)
rho_t(p,q) := d(p,q)^8 exp(-6t c(p,q)).                                 (7)
```

In the rest of the theorem, set `t := 1`. Define the positive diagonal
matrices

```text
L_N := diag(a_1(p,q)^4) = diag(exp(-2c(p,q))),                           (8)
R_N := diag(rho_1(p,q)),                                                 (9)
```

and define

```text
M_N := exp(3J_N),
T_N := M_N L_N R_N M_N.                                                 (10)
```

Let `lambda_N` be the largest eigenvalue of `T_N`. Let `v_N` be its real
eigenvector normalized by

```text
v_N^T v_N = 1,       sum_x (v_N)_x > 0,                                 (11)
```

and define the scalar

```text
P_N := v_N^T J_N v_N.                                                    (12)
```

## Finite-matrix theorem

For every nonnegative integer `N`:

1. `J_N` is real symmetric and entrywise nonnegative.
2. `M_N` is real symmetric positive definite and entrywise strictly positive.
3. `T_N` is real symmetric positive definite and entrywise strictly positive.
4. The largest eigenvalue `lambda_N` is positive and simple. Its eigenvector
   is entrywise strictly positive up to an overall sign, so convention (11)
   determines `v_N` uniquely.
5. `P_N` is well-defined and unchanged by either sign or nonzero scaling of a
   representative top eigenvector when written as the normalized quadratic
   expectation `(v^T J_N v)/(v^T v)`.

**Proof.** The move set is inverse-closed: `S = -S`. Therefore (4) gives
`(J_N)_(x,y) = (J_N)_(y,x)` even at the boundary, because both entries are
deleted together whenever one endpoint is outside `W_N`. Horizontal and
vertical moves alone connect the square box.

Since `J_N` is real symmetric, `M_N = exp(3J_N)` is real symmetric positive
definite. For any two indices, connectedness supplies a path of some length
`k`; the corresponding entry of `J_N^k` is positive. The power series for the
matrix exponential has nonnegative terms and a positive `k`-th term, so every
entry of `M_N` is strictly positive.

Equations (8) and (9) are positive diagonal matrices and commute. Hence

```text
T_N^T = M_N (L_N R_N) M_N = T_N,
x^T T_N x = (M_N x)^T (L_N R_N) (M_N x) > 0
```

for nonzero `x`. Every entry of `T_N` is a sum of strictly positive terms.
Perron-Frobenius applied to this entrywise-positive symmetric matrix gives a
simple largest eigenvalue and an entrywise-positive eigenvector. The final
claim follows because both numerator and denominator are quadratic in the
chosen representative. ∎

## Certified numerical statement

An independent `mpmath` implementation reconstructs `J_N`, `M_N`, `L_N`,
`R_N`, and `T_N` directly from (1)-(10) at 90 decimal digits. It does not call
the NumPy implementation or read the stored regression centers during matrix
construction, eigenvector selection, or evaluation of `P_N`.

For the full computed symmetric eigensystem, write its eigenvector matrix and
diagonal eigenvalue matrix as `Q_N` and `D_N`. Define the Frobenius residual
and Gram defect

```text
r_N   := ||T_N Q_N - Q_N D_N||_F,
eta_N := ||Q_N^T Q_N - I||_F.
```

The runner verifies `eta_N < 1` and uses the declared 90-digit
working-arithmetic guard `g = 10^-60` to form

```text
delta_N := r_N/sqrt(1-eta_N) + g.                                       (13)
```

Indeed, `||Q_N^(-1)||_2 <= 1/sqrt(1-eta_N)`. Thus
`Q_N^(-1) T_N Q_N = D_N + Q_N^(-1)(T_N Q_N-Q_N D_N)`, and the normal-matrix
perturbation bound places the exact eigenvalues in the corresponding
`delta_N` neighborhoods. The top neighborhood is isolated from all the
others, so it contains exactly one eigenvalue.

If `lambda_hat_1 >= lambda_hat_2` are the two largest computed eigenvalues,
the runner verifies

```text
gamma_N := lambda_hat_1 - lambda_hat_2 - 2 delta_N > 4.95.               (14)
```

Let `tau_N := ||T_N v_hat_N-lambda_hat_1 v_hat_N||_2`. The symmetric
eigenvector residual-angle bound, the isolated interval above, and the exact
row-sum bound `||J_N||_2 <= ||J_N||_infinity <= 1` give

```text
|P_N - P_hat_N|
  <= g + 2(tau_N+g)/(lambda_hat_1-lambda_hat_2-delta_N)
  < 2 x 10^-60.                                                         (15)
```

The independently reconstructed centers and the guarded enclosures are:

| `N` | `P_hat_N` | guarded enclosure `I_N` | lower top-eigenvalue gap |
|---:|---:|---:|---:|
| 6 | `0.522324311537361669376731397147380591681793209294921543147251767405388996516` | `P_hat_6 +/- 2e-60` | `> 4.95` |
| 7 | `0.522324315075691917933023223847885524615477328862129075311171521855593496815` | `P_hat_7 +/- 2e-60` | `> 4.95` |
| 8 | `0.522324315103738928863262943442354237767467710788871114561329778403325241798` | `P_hat_8 +/- 2e-60` | `> 4.95` |

The raw 90-digit basis residual and Gram-defect norms are reported by the
runner; the guard, rather than those raw errors, controls the displayed
enclosure. A 110-digit rerun reproduces every displayed center digit. This is
an independently reconstructed, guarded a-posteriori certificate, not a
directed-rounding Arb/ball proof.

The interval differences are also certified:

```text
P_7 - P_6 = 3.5383302485562918267005049329336841195672075321639e-9
              +/- 4e-60,
P_8 - P_7 = 2.8047010930239719594468713151990381926742039250158e-11
              +/- 4e-60.                                                  (16)
```

Thus `I_6`, `I_7`, and `I_8` are pairwise disjoint. The three enclosures share
seven rounded decimal places; `I_7` and `I_8` share ten. They do not certify
twelve-decimal finite-`N` stability. In particular, `0.5223243151` is only the
common ten-place rounded display of the `N=7` and `N=8` values. It is not a
single cutoff-independent value.

No monotonicity theorem, tail bound in `N`, or `N -> infinity` result is
claimed.

## Executable controls

The primary runner has four decisive modes:

```bash
python3 scripts/probe_hk_cube_perron_l2_2026_05_06.py
python3 scripts/probe_hk_cube_perron_l2_2026_05_06.py --mode high-precision --dps 90
python3 scripts/probe_hk_cube_perron_l2_2026_05_06.py --mode hostile
python3 scripts/probe_hk_cube_perron_l2_2026_05_06.py --mode intentional-failure
```

Normal, high-precision, and hostile modes exit zero only after all checks pass.
Intentional-failure mode injects an asymmetric recurrence edge, reports a
failure, and exits nonzero. Hostile mode requires rejection of an asymmetric
recurrence, a wrong `c` polynomial, wrong `rho` exponential and dimension
exponents, a missing local factor, a non-dominant eigenvector, a sign/scale
dependent scalar, an uncertifiable residual-to-gap ratio, false stability
digits, a wrong reference value, answer-key-fed construction, and illicit
physical or limiting conclusion tags.

The stored centers are used only after reconstruction as regression checks.
Static source/import checks reject a reconstruction function that reads those
centers, repo-local helper imports, literal `True` as check evidence, or
source-note dependency links.

## Legacy identity and non-claims

The old HK/cube/Perron vocabulary remains in the stable claim id, filename,
runner filename, and title solely so repository history and citations can find
this repaired row. Equations (1)-(12) do not supply or inherit their former
physical interpretation.

This theorem does not establish any of the following:

- an SU(3) representation formula or heat-kernel measure;
- a physical action, plaquette, cube, link topology, or multi-plaquette
  correlation;
- a canonical physical meaning for `t=1`;
- a Wilson or Monte Carlo comparison, an action-naturalness ordering, or a
  statement that one value is “closer” to another;
- a physical thermodynamic observable or any finite-volume/thermodynamic-limit
  relationship.

Any downstream physical reuse must add a separate, explicit bridge identifying
the defined functions and matrices with the proposed physical objects. No such
bridge is a dependency of this note.

**2026-07-16 downstream hygiene:** the direct thermodynamic-stretch consumer
was narrowed so this formal theorem no longer closes its physical finite-cube
Path A or supplies a physical comparator.

## Dependencies

None. The integrality, symmetry, positivity, Perron-Frobenius, normalization,
and residual/gap arguments needed for the theorem are stated here. The primary
runner is executable evidence, not a source-note premise.
