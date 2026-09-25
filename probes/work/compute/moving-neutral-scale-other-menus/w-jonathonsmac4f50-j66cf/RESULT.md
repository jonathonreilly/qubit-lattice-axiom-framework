# The neutral scale and the reflection-positivity bound beyond six axes — run 2

Worker `w-jonathonsmac4f50-j66cf`, model `claude-opus-5-5`. Blocks 39 and 40 were written by the same model family (Claude). The log is `logs/probes/C:moving-neutral-scale-other-menus:a2/w-jonathonsmac4f50-j66cf__da21499e__20260925T023336Z.*`.

## As landed on main

- Block 39 (#8530, T5): a positive semidefinite bond kernel `B = [[1, 1ᵀ], [1, cω]]` gives reflection positivity through bond planes. `B ⪰ 0` exactly when `cω − J ⪰ 0`.
- Block 40 (#8546, T1): `c₀ = N/R`.
- Block 40 N1.2 already flags menus without constant row sums as the failure route.

The moving-records reading and the value `c = c₀` are supplied, not adopted. Nothing below depends on a withdrawn statement.

## Method (exact, sympy)

For each menu:
1. The class of a pair is its dot product. Each value is one orbit of pairs, and every row has the same class counts (PASS).
2. The class matrices commute (PASS).
3. Their joint eigenspaces are separated with a generic integer combination. The check that every class matrix is a scalar on each whole eigenspace PASSES.
4. The spectrum of `ω = Σ w_i A_i` is then a set of linear forms in the class weights.

## (1) and (2): c₀ and the positive-semidefinite region

In each table the first line of the spectrum column is the eigenvalue on the constant vector.

| menu | classes (dot: count per row) | spectrum of ω (multiplicity) |
|---|---|---|
| six axes | 1:1, 0:4, −1:1 | `w0+4w1+w2` on the constant vector; `w0−w2` (3); `w0−2w1+w2` (2) |
| eight cube corners | 1:1, 1/3:3, −1/3:3, −1:1 | `w0+3w1+3w2+w3` on the constant vector; `w0+w1−w2−w3` (3); `w0−w1−w2+w3` (3); `w0−3w1+3w2−w3` (1) |
| twelve edge midpoints | 1:1, 1/2:4, 0:2, −1/2:4, −1:1 | `w0+4w1+2w2+4w3+w4` on the constant vector; `w0+2w1−2w3−w4` (3); `w0−2w1+2w3−w4` (3); `w0−2w2+w4` (3); `w0−2w1+2w2−2w3+w4` (2) |

On each of these menus the row sum R is the same for every content, so `c₀ = N/R` does not depend on a. `B ⪰ 0` holds **exactly when both** of these are true:
- `c ≥ c₀`;
- every complement eigenvalue listed above is `≥ 0`.

If any complement eigenvalue is negative, no scale gives `B ⪰ 0`. The six-axis line reproduces block 39's `p ≥ q`, `p + q ≥ 2r`.

**Numerical cross-check.** 200 random shape parameters per menu: `B ⪰ 0` at `c₀(1 + 10⁻⁶)` exactly when the complement eigenvalues are ≥ 0, and never at `c₀(1 − 10⁻⁶)` (PASS).

**Exponential family `ω = exp(β s·s')`:**

| menu | c₀ | complement eigenvalues |
|---|---|---|
| six axes | `3/(cosh β + 2)` | `2 sinh β` (3), `2(cosh β − 1)` (2) |
| eight corners | `8/(6 cosh(β/3) + 2 cosh β)` | `2(sinh β + sinh(β/3))` (3), `2(cosh β − cosh(β/3))` (3), `2(sinh β − 3 sinh(β/3)) = 8 sinh³(β/3)` (1) |
| twelve edges | `12/(8 cosh(β/2) + 2 cosh β + 2)` | `2(sinh β + 2 sinh(β/2))` (3), `2(sinh β − 2 sinh(β/2))` (3), `2(cosh β − 1)` (3), `2(cosh β − 2 cosh(β/2) + 1)` (2) |
| sphere | `β/sinh β` (**confirmed**) | Funk–Hecke `λ_l = β^l/(2^{l+1} l!) ∫ e^{βt}(1 − t²)^l dt` (Rodrigues; checked l = 0..6) |

- **β > 0:** every complement eigenvalue is positive. This was checked at β = 1/4 … 3, and it holds in general because the sum of Schur powers of a Gram kernel is positive semidefinite.
- **β < 0:** some complement eigenvalue is negative. The odd vector `v(a) = a_x` is orthogonal to 1, and `vᵀωv` is odd in β.

**Therefore:** for the exponential family, the kernel is positive semidefinite exactly when `β ≥ 0` and `c ≥ c₀`.

## The 26 directions: row sums are not constant

The 26 directions are three orbits under the cube group: 6 faces, 12 edges, 8 corners.

**Row sums of `exp(β s·s')`** (exact):
- face: `2cosh β + 8cosh(β/√2) + 8cosh(β/√3) + 8`
- edge: `8cosh(β/2) + 2cosh β + 4cosh(β/√2) + 4cosh(β√(2/3)) + 8`
- corner: `6cosh(β/3) + 2cosh β + 6cosh(β/√3) + 6cosh(β√(2/3)) + 6`

**Expansion.** The row sums agree through β², because the second moment is isotropic. They differ at β⁴: 11/54 (face), 95/432 (edge), 73/324 (corner). So `c₀(a) = 26/R(a)` depends on the orbit, with face > edge > corner.

**Exact floor.** For β > 0 the floor is `c* = 1ᵀω⁻¹1`.
- `ω⁻¹1` is invariant under the cube group, so it is found from the 3×3 orbit quotient.
- The smallest eigenvalue of B changes sign at c* for β = 1/2, 1, 2, 4 (PASS).

| β | c* | c₀(face) | c₀(edge) | c₀(corner) | 26²/Σω | β/sinh β (sphere) |
|---|---|---|---|---|---|---|
| 1/2 | 0.9595173753 | 0.9595463878 | 0.9595101291 | 0.9594980228 | 0.9595147712 | 0.9595173757 |
| 1 | 0.8509180558 | 0.8512956633 | 0.8508240512 | 0.8506659075 | 0.8508841601 | 0.8509181282 |
| 2 | 0.5514327023 | 0.5543383839 | 0.5507213594 | 0.5494961310 | 0.5511731474 | 0.5514411295 |
| 4 | 0.1463670874 | 0.1518699955 | 0.1451232097 | 0.1428385298 | 0.1459009162 | 0.1465742813 |

- c* lies between the smallest and the largest `c₀(a)`.
- c* is at least `26²/Σω` (Cauchy–Schwarz).
- c* is within 3.5e−10, 7.2e−8, 8.4e−6 and 2.1e−4 of the sphere's `β/sinh β`.

**At c*, one neighbour** (β = 1): an empty site next to one record forms at 0.99956 (face), 1.00011 (edge) and 1.00030 (corner) of the empty-space rate. So on this menu, "an empty site is a record of random content" and "the least reflection-positive scale" are no longer the same number.

## (3) Formation-rate multipliers at c₀

The formation rate over its empty-space value is:
- next to one record: `c₀R/N = 1` on every transitive menu;
- next to two records `b1`, `b2`: `c₀² (ω²)(b1, b2)/N`.

General class-weight formulas are in the log. For `exp(β s·s')`:

| menu | β | agreeing | orthogonal (corners: nearest, dot 1/3) | opposite |
|---|---|---|---|---|
| six axes | 1 | 1.377042 | 0.976505 | 0.716936 |
| six axes | 3 | 4.196617 | 0.435395 | 0.061801 |
| eight corners | 1 | 1.343272 | 1.091580 (nearest) | 0.720840 |
| eight corners | 3 | 3.944504 | 1.048458 (nearest) | 0.074074 |
| twelve edges | 1 | 1.318655 | 0.985546 | 0.723574 |
| twelve edges | 3 | 3.476863 | 0.604846 | 0.085853 |
| 26 directions, at c*, face records | 1 | 1.306172 | 0.991125 | 0.724062 |
| sphere | 1 | 1.313035 (`β coth β`) | 0.990733 (`(β/√2) sinh(√2β)/sinh²β`) | 0.724062 (`β²/sinh²β`) |
| sphere | 3 | 3.014909 | 0.735344 | 0.089679 |

## Verdict

There is no HIT. On every menu whose ω has constant row sums (six axes, eight corners, twelve edge midpoints, the sphere), the bound is exactly `c ≥ c₀ = N/R`. This holds together with the shape condition that ω is positive semidefinite on the complement of the constant vector; for `exp(β s·s')` that means `β ≥ 0`. For the sphere, `c₀ = β/sinh β`.

The 26 directions do not have constant row sums. There c₀ is not one number, and the exact floor `c* = 1ᵀω⁻¹1` differs from every `c₀(a)`.
