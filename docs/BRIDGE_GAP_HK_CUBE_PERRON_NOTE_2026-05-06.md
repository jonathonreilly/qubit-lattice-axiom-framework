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
spectral properties. It then gives independently reconstructed high-precision
estimates for three separate finite matrices, at `N = 6, 7, 8`.

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
D_N := L_N R_N = diag(d(p,q)^8 exp(-8c(p,q))),                           (10)
```

and define

```text
M_N := exp(3J_N),
T_N := M_N D_N M_N.                                                     (11)
```

The constants `3` in `M_N`, `4` in `a_1^4`, `8` on `d`, and `6` in
`rho_1` are parts of these definitions. In particular, the powers `4` and `8`
and the exponential factors `2`, `6`, and their combined value `8` do not
inherit a topology, dimension, incidence count, or other interpretation from
the stable legacy name.

Let `lambda_N` be the largest eigenvalue of `T_N`. Let `v_N` be its real
eigenvector normalized by

```text
v_N^T v_N = 1,       sum_x (v_N)_x > 0,                                 (12)
```

and define the scalar

```text
P_N := v_N^T J_N v_N.                                                    (13)
```

## Finite-matrix theorem

For every nonnegative integer `N`:

1. `J_N` is real symmetric and entrywise nonnegative.
2. Under the actual finite-box truncation, `||J_N||_2 <= 1`.
3. `M_N` is real symmetric positive definite and entrywise strictly positive.
4. `D_N` is positive diagonal, while `T_N` is real symmetric positive
   definite and entrywise strictly positive.
5. The largest eigenvalue `lambda_N` is positive and simple. Its eigenvector
   is entrywise strictly positive up to an overall sign, so convention (12)
   determines `v_N` uniquely.
6. `P_N` is well-defined and unchanged by either sign or nonzero scaling of a
   representative top eigenvector when written as the normalized quadratic
   expectation `(v^T J_N v)/(v^T v)`.

**Proof.** The move set is inverse-closed: `S = -S`. Therefore (4) gives
`(J_N)_(x,y) = (J_N)_(y,x)` even at the boundary, because both entries are
deleted together whenever one endpoint is outside `W_N`. Horizontal and
vertical moves alone connect the square box for `N >= 1`; the one-vertex
`N=0` graph is connected as well. Each truncated row has at most six entries,
each equal to `1/6`, so `||J_N||_infinity <= 1`. Symmetry gives
`||J_N||_1 = ||J_N||_infinity`, and therefore
`||J_N||_2 <= sqrt(||J_N||_1 ||J_N||_infinity) <= 1`.

Since `J_N` is real symmetric, `M_N = exp(3J_N)` is real symmetric positive
definite. For any two indices, connectedness supplies a path of some length
`k`; the corresponding entry of `J_N^k` is positive. The power series for the
matrix exponential has nonnegative terms and a positive `k`-th term, so every
entry of `M_N` is strictly positive.

Equations (8)-(10) give the explicitly combined positive diagonal `D_N`.
Hence

```text
T_N^T = M_N D_N M_N = T_N,
x^T T_N x = (M_N x)^T D_N (M_N x) > 0
```

for nonzero `x`. Every entry of `T_N` is a sum of strictly positive terms.
Perron-Frobenius applied to this entrywise-positive symmetric matrix gives a
simple largest eigenvalue and an entrywise-positive eigenvector. The final
claim follows because both numerator and denominator are quadratic in the
chosen representative. ∎

## High-precision numerical estimates

An independent `mpmath` implementation reconstructs `J_N`, `M_N`, `D_N`, and
`T_N` from (1)-(11) at 90 decimal digits and repeats the computation at 110
digits. This execution path has no module-scope NumPy dependency and does not
read the stored regression centers, directly or through a reachable helper,
during matrix construction, eigenvector selection, or evaluation of `P_N`.

The two working precisions agree on the following conservative displays:

| `N` | high-precision estimate of `P_N` | observed top eigengap |
|---:|---:|---:|
| 6 | `0.52232431153736166937673139714738059168179320929492` | `4.95928143865115310329935689152` |
| 7 | `0.52232431507569191793302322384788552461547732886213` | `4.95928144134063313074991808640` |
| 8 | `0.52232431510373892886326294344235423776746771078887` | `4.95928144135451144353469487140` |

At 90 digits the runner reports full-basis residuals, Gram defects, and top
residuals of order `10^-89` to `10^-90`. These residuals are computed against
the `mpmath` matrix actually constructed at that working precision. They do
not bound the difference between that matrix and the exact matrix in (11):
`mpmath` supplies neither directed rounding for these operations nor an
analytic operator-norm bound for accumulated rounding in `exp(3J_N)`,
`exp(-2c)`, and `exp(-6c)`.

For orientation only, if `Q` and its reported Gram defect `eta` were treated
as exact stored arrays, `eta < 1` would imply
`sigma_min(Q)^2 >= 1-eta`, so `Q` would be invertible and

```text
||Q^(-1)(TQ-Q Lambda)||_2 <= ||TQ-Q Lambda||_F/sqrt(1-eta).
```

Likewise, for a genuinely bounded perturbation of a symmetric matrix, the
top-eigenvector residual-angle estimate combined with the exact
`||J_N||_2 <= 1` bound would change the quadratic expectation by at most
`2 sin(theta)`: the factor `2` follows from the nuclear norm of the difference
of the two rank-one projectors. The runner reports these quantities as
diagnostics only. It does not turn them into an enclosure by adding an
unproved decimal guard. Nor does it assert that the small-eigenvalue portion
of the full computed spectrum is pairwise isolated; only the large observed
top gap is used as a numerical stability diagnostic.

The estimated differences are

```text
P_7 - P_6 = 3.53833024855629182670050493293e-9,
P_8 - P_7 = 2.80470109302397195944687131520e-11.
```

Their signs and displayed digits are stable between 90 and 110 digits, but
this agreement is numerical evidence, not an outward-rounded proof of exact
ordering. The three estimates share only seven rounded decimal places; the
`N=7` and `N=8` estimates share ten, not twelve. In particular,
`0.5223243151` is only the common ten-place rounded display of the latter two
estimates, not a cutoff-independent value.

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
recurrence, a wrong multiplier exponential, a wrong `c` polynomial, wrong
local and `rho` exponential factors, a wrong defined dimension exponent, a
missing local factor, a non-dominant eigenvector, a sign/scale-dependent
scalar, an insufficient residual-to-gap ratio, false stability digits, a wrong
reference value, helper-mediated answer-key-fed construction, and illicit
physical or limiting conclusion tags.

The stored centers are used only after reconstruction as regression checks.
An AST call-graph check follows reachable local helpers from both reconstruction
roots and rejects any answer-key read. Static checks also reject a
module-scope NumPy import, repo-local helper imports, literal `True` as check
evidence, or source-note dependency links.

## Legacy identity and non-claims

The old HK/cube/Perron vocabulary remains in the stable claim id, filename,
runner filename, and title solely so repository history and citations can find
this repaired row. Equations (1)-(13) do not supply or inherit their former
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

None. The integrality, symmetry, norm, positivity, Perron-Frobenius, and
normalization arguments needed for the exact theorem are stated here. The
primary runner is executable numerical evidence, not a source-note premise.
