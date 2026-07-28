# Gauge-Vacuum Plaquette Perron/Jacobi Underdetermination

**Date:** 2026-04-17
**Type:** positive_theorem
**Claim scope:** deterministic finite-box existence witness. On the 36-state
`NMAX = 5` dominant-weight box, one explicitly computed positive diagonal
packet and two explicitly supplied positive swap-symmetric residual packets
give different Perron moments and Jacobi data for the same `J_box`.
**Status authority:** independent audit lane only. This note does not set or
predict an audit verdict or effective status.
**Status:** support - finite-box witness inside the supplied-diagonal
factorization class; the untruncated source sector, the physical Wilson
compression, and explicit physical `beta = 6` Perron / Jacobi data remain open
**Script:** `scripts/frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination.py`

## Question

Within the finite
[supplied-diagonal source-sector factorization theorem](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md),
do the typed inputs alone determine the symmetry-reduced Jacobi coefficients,
or equivalently the Perron moments of `J_box`, at the supplied value
`beta = 6`?

## Answer

No, on the stated finite box.

The linked retained theorem supplies the finite recurrence `J_box`, the
multiplier `M = exp(3 J_box)`, and the algebraic class
`T = M D M` for a separately supplied positive swap-symmetric diagonal `D`.
It does not select that diagonal.

This note fixes one explicit finite fourth-power packet `D_6^packet`, supplies
two positive swap-symmetric packets `R_A` and `R_B`, and sets
`D = D_6^packet R`. The two resulting matrices have different Perron moments
and Jacobi data. Thus those typed finite inputs do not select a unique Perron
moment sequence at `beta = 6`.

**Scope.** Every theorem below is proved on the finite `NMAX = 5` box the runner
constructs—the 36 dominant weights with `p, q <= 5`. The result is the
positive existence witness just stated, together with its negative consequence
for the typed finite inputs. That box is not invariant under the character
recurrence, so the witness does not by itself give the untruncated statement;
see the boundary and gate sections below.

The fourth-power packet is a stipulated/computed finite matrix. It is not
identified here as a physical local Wilson factor. The marked/non-marked
compression, residual diagonality, and physical realizability of the supplied
packets are outside this claim.

So on that box the supplied-diagonal inputs do **not** force the explicit
symmetry-reduced Jacobi coefficients at `beta = 6`.

## Setup

Let `J_box := J_5` be the explicit real six-neighbor recurrence from the linked
finite factorization theorem, on the 36 dominant weights with `p, q <= 5`.
Every theorem below is about this finite matrix.

Let `S` be the exact conjugation-symmetry involution `(p,q) <-> (q,p)` on the
dominant-weight basis.

The linked finite factorization theorem gives the supplied-diagonal
`beta = 6` class

`T = M D M`,

with

`M = exp(3 J_box)`,

with:

- `M = M^* > 0`,
- `D` diagonal in the character basis,
- `D > 0`,
- `S D = D S`.

For this witness, the runner evaluates the stipulated finite coefficient
formula

`a_(p,q)(6) = c_(p,q)(6) / (d_(p,q) c_(0,0)(6))`

by the Bessel-determinant mode sum with `MODE_MAX = 80`, and constructs the
strictly positive diagonal finite packet

`D_6^packet chi_(p,q) = a_(p,q)(6)^4 chi_(p,q)`.

The fourth power is part of this explicit finite witness. It is not a theorem
identifying the matrix with a physical local factor.

Separately supply a strictly positive diagonal swap-symmetric `R` and study

`T = M D_6^packet R M`,

with:

- `R` diagonal in the character basis,
- `R > 0`,
- `S R = R S`.

The runner uses the two explicit packets

`(R_A)_(p,q) = exp[-0.34(p+q) - 0.04(p-q)^2]`,

`(R_B)_(p,q) = exp[-0.25(p+q) - 0.11(p-q)^2]`.

This is a definition of the finite witness class. It does not assert that the
physical Wilson mixed kernel compresses to `D_6^packet`, that its stripped
residual is diagonal, or that either residual packet is physically realized.

The finite recurrence graph is connected, so `M` has strictly positive matrix
entries. Every such supplied-class `T` therefore has the following properties:

- it is positivity-improving;
- it has one simple strictly positive Perron state;
- its Perron state lies in the symmetric sector of `S`.

## Theorem 1 (36-state `NMAX = 5` box): the supplied class contains distinct positive swap-symmetric residual packets

The packets

`R_A != R_B`

are distinct, strictly positive, diagonal, and swap-symmetric on the same
finite source sector.

Then

`T_A = M D_6^packet R_A M`,
`T_B = M D_6^packet R_B M`

are both positivity-improving self-adjoint transfer operators with unique
strictly positive Perron states `psi_A`, `psi_B`.

Both lie inside the supplied factorized model class defined above.

## Theorem 2 (36-state `NMAX = 5` box): the two explicit residual packets induce distinct Perron moments for the same recurrence matrix

For the same `J_box`, define the Perron moments

`m_n^(A) = <psi_A, J_box^n psi_A>`,
`m_n^(B) = <psi_B, J_box^n psi_B>`.

Because `psi_A` and `psi_B` need not coincide, these moment sequences need not
coincide either.

The runner exhibits two distinct admissible inputs within the supplied finite
class and distinct Perron moments, including

`m_1^(A) != m_1^(B)`

and higher moments differing as well.

Therefore, on the 36-state `NMAX = 5` box, the typed supplied-diagonal inputs
do **not** determine a unique Perron moment sequence at `beta = 6`.

## Corollary 1 (36-state `NMAX = 5` box): the symmetry-reduced Jacobi coefficients are not yet forced

By the spectral theorem and orthogonal-polynomial construction, the Jacobi
coefficients are uniquely determined by the Perron moments of `J_box`.

The runner directly finds different `alpha_0` and `beta_1`; in particular,
`alpha_0 = m_1`, so the first moment difference already separates the two
Jacobi packets.

Therefore:

> on the 36-state `NMAX = 5` box, the typed supplied-diagonal inputs do not
> force the explicit
> symmetry-reduced Jacobi coefficients at `beta = 6`.

## Boundary: the box statement does not lift by restriction

The `NMAX = 5` box is **not** invariant under the character recurrence. The
runner reports 11 of the 36 box weights whose `J`-image leaves the box, with up
to 4 of the 6 recurrence moves leaking. So `J_box` is a non-invariant
compression of `J`, not the restriction of `J` to an invariant subspace, and
positivity plus differing moments on the box therefore do not transfer to the
untruncated source sector by restriction.

The runner also samples the cutoff at `NMAX = 3, 4, 5, 6, 7` and reports a
moment gap between `4.394768e-04` and `4.418926e-04` across those boxes. That is
a cutoff-sensitivity diagnostic on the sampled boxes only: it shows the two
witnesses are not an artifact of one particular truncation, and it bounds
nothing about the untruncated sector.

## A perturbative untruncated route leaves two analytic gates

Write `R(eps) = R_A + eps R_B`. In a neighborhood of `eps = 0` (in
particular, for the runner's sampled window `|eps| <= 0.01`), each finite-box
ray member is diagonal, swap-symmetric, and strictly positive. Then

`T(eps) = T_0 + eps V`, with
`T_0 = M D_6^packet R_A M` and `V = M D_6^packet R_B M`,

and `V = V^* >= 0`. Suppose the top eigenvalue `lam_0` of `T_0` is **simple and
isolated**. Then the Perron state is differentiable at `eps = 0` with

`psi'(0) = R_red V psi_0`,

where `R_red` is the reduced resolvent of `T_0` on `psi_0^perp`, and the first
Perron moment obeys

`m_1'(0) = 2 <R_red V psi_0, J_box psi_0>`.

On the `NMAX = 5` box the runner evaluates this closed form as
`m_1'(0) = 4.424199803e-04`, nonzero, and confirms it against a central-
difference derivative whose error falls by `4.000x` per halving of `eps`—the
second-order rate a wrong derivative would not reproduce. The box `T_0` has a
simple top eigenvalue with relative spectral gap `9.768599e-01`, and the finite
ray stays strictly positive over the sampled window.

The same formula is available on the untruncated sector only after two
separate obligations close:

1. **Operator/spectral gate (not supplied here).** On the full untruncated
   character sector, `T_0` and `V` are bounded self-adjoint operators and the
   top eigenvalue of `T_0` is simple and isolated from the rest of the
   spectrum.
2. **Response gate (not supplied here).** The resulting full-sector response
   is nonconstant; for the displayed first-order route it is enough to prove
   `2 <R_red V psi_0, J psi_0> != 0`.

The finite-box value does not prove the response gate after removing the
cutoff. Essential-spectrum control addresses the first gate but does not by
itself imply the second. Granting both gates would give untruncated
non-uniqueness along this ray; until then, that conclusion remains open.

## What this closes

- a deterministic witness, on the 36-state `NMAX = 5` box, that one explicit
  positive `D_6^packet` and two supplied positive swap-symmetric residual
  packets produce different Perron moments and Jacobi data for the same
  `J_box`
- the exact finite-matrix identities that make both transfer matrices
  self-adjoint, positive definite, swap-commuting, and positivity-improving
- a finite-box perturbative response formula whose independently reproduced
  value is nonzero and whose central-difference error converges at second order
- an honest reduction of this particular untruncated perturbative route to
  the separate operator/spectral and nonconstant-response gates above

## What this does not close

- the untruncated source-sector statement: non-uniqueness off the `NMAX = 5` box
  is not proved here
- the operator/spectral or response gate for the untruncated `T_0`
- explicit physical or untruncated Jacobi coefficients at `beta = 6`
- explicit physical or untruncated Perron moments at `beta = 6`
- physical Wilson mixed-kernel compression, residual diagonality, or physical
  realizability of either residual packet
- analytic closure of canonical `P(6)`
- repo-wide repinning of the canonical plaquette

**Downstream hygiene (2026-07-25).** Every theorem in this note is stated on the
36-state `NMAX = 5` dominant-weight box. Full-sector non-uniqueness and physical
Wilson non-uniqueness remain **open** until both untruncated gates and the
separate physical-class identification are proved. Downstream work must cite
this note for the supplied-class finite-box witness only, and must not read it
as an untruncated or physical-Wilson result.

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination.py
```

Expected summary:

- `THEOREM PASS=7 SUPPORT=6 FAIL=0`
