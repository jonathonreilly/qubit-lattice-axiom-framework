# Gauge-Vacuum Plaquette Perron/Jacobi Underdetermination

**Date:** 2026-04-17
**Status:** support - exact obstruction theorem on the 36-state `NMAX = 5`
dominant-weight box inside a supplied-diagonal factorized source-sector class;
the untruncated source sector, the physical Wilson compression, and explicit
`beta = 6` Perron / Jacobi data are still not forced
**Script:** `scripts/frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination.py`

## Question

Do the exact plaquette theorems now on `main` already force the symmetry-reduced
Jacobi coefficients, or equivalently the Perron moments of the explicit source
operator `J`, at the framework point `beta = 6`?

## Answer

No.

The live stack now closes:

- the explicit source operator `J`,
- the exact transfer-operator / character-recurrence realization,
- the exact Perron-state reduction,
- the conjugation-symmetry reduction of the Perron state,
- and the conditional source-sector matrix-element law
  `T_src(6) = exp(3 J) D_6 exp(3 J)` after a positive
  character-diagonal `D_6` is supplied.

On the 36-state `NMAX = 5` dominant-weight box, those facts do **not** yet
determine the explicit `beta = 6` Perron moments or Jacobi coefficients there.

The obstruction can be sharpened inside a smaller supplied model class. Supply
both a strictly positive diagonal local packet `D_6^loc` and a strictly
positive diagonal swap-symmetric packet `R`, and set `D_6=D_6^loc R`. Even
inside this restricted class, distinct supplied `R` packets can induce
different Perron moments and therefore different Jacobi data for the same
explicit source operator `J`.

**Scope.** Every theorem below is proved on the finite `NMAX = 5` box the runner
constructs - the 36 dominant weights with `p, q <= 5`. That box is not invariant
under the character recurrence, so the box statement does not by itself give the
untruncated statement; see the boundary and gate sections below.

This sharpening is not a physical mixed-kernel theorem. For the Wilson problem,
the marked/non-marked compression and the character diagonality of the stripped
two-slice residual are prior independent open walls.

So on that box the current exact stack still does **not** force the explicit
framework-point Jacobi coefficients.

## Setup

Let `J` be the explicit self-adjoint plaquette source operator on the
source-cyclic class-function sector already closed in the transfer-operator /
character-recurrence theorem, and let `J_box` be its compression to the 36
dominant weights with `p, q <= 5`. Every statement below is about `J_box`; that
is exactly the matrix the runner builds.

Let `S` be the exact conjugation-symmetry involution `(p,q) <-> (q,p)` on the
dominant-weight basis.

From the conditional source-sector matrix-element factorization theorem,
every member of the supplied-diagonal `beta = 6` model class has the form

`T_src(6) = M D_6 M`,

with

`M = exp(3 J)`,

with:

- `M = M^* > 0`,
- `D_6` diagonal in the character basis,
- `D_6 > 0`,
- `S D_6 = D_6 S`.

For the supplied subclass used by this obstruction, choose an explicit
strictly positive diagonal packet

`D_6^loc chi_(p,q) = a_(p,q)(6)^4 chi_(p,q)`.

Then separately supply a strictly positive diagonal swap-symmetric `R` and
study

`T = M D_6^loc R M`,

with:

- `R` diagonal in the character basis,
- `R > 0`,
- `S R = R S`.

This factorization is a definition of the obstruction class. It does not assert
that the physical Wilson mixed kernel compresses to `D_6^loc`, or that its
stripped residual is diagonal.

Every such supplied-class `T`, compressed to the `NMAX = 5` box, satisfies the
same structural boundary:

- positivity-improving,
- one simple strictly positive Perron state,
- Perron-state symmetry reduction under `S`.

## Theorem 1 (36-state `NMAX = 5` box): the current exact factorized class does not determine a unique residual source-sector environment operator

Choose two distinct positive conjugation-symmetric residual source-sector
environment operators

`R_A != R_B`

on the same explicit source sector, both restricted to the `NMAX = 5` box.

Then

`T_A = M D_6^loc R_A M`,
`T_B = M D_6^loc R_B M`

are both positivity-improving self-adjoint transfer operators with unique
strictly positive Perron states `psi_A`, `psi_B`.

Both lie inside the supplied factorized model class defined above.

## Theorem 2 (36-state `NMAX = 5` box): distinct admissible residual source-sector environment operators can induce distinct Perron moments for the same source operator

For the same explicit plaquette source operator `J`, define the Perron moments

`m_n^(A) = <psi_A, J^n psi_A>`,
`m_n^(B) = <psi_B, J^n psi_B>`.

Because `psi_A` and `psi_B` need not coincide, these moment sequences need not
coincide either.

The runner exhibits, on the `NMAX = 5` box, two explicit admissible positive
residual source-sector environment operators with

`m_1^(A) != m_1^(B)`

and higher moments differing as well.

Therefore, on the 36-state `NMAX = 5` box, the current exact plaquette operator
stack does **not** determine a unique Perron moment sequence at `beta = 6`.

## Corollary 1 (36-state `NMAX = 5` box): the symmetry-reduced Jacobi coefficients are not yet forced

By the spectral theorem and orthogonal-polynomial construction, the Jacobi
coefficients are uniquely determined by the Perron moments of `J_box`.

So if two admissible transfer generators on the current structural boundary
produce different Perron moments, they also produce different Jacobi data.

Therefore:

> on the 36-state `NMAX = 5` box, the current exact plaquette operator stack
> does not yet force the explicit
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

## The untruncated lift reduces to one named analytic gate

Write `R(eps) = R_A + eps R_B`. Each ray member is diagonal, swap-symmetric and
strictly positive, hence admissible in the supplied class. Then

`T(eps) = T_0 + eps V`, with `T_0 = M D_6^loc R_A M` and `V = M D_6^loc R_B M`,

and `V = V^* >= 0`. Suppose the top eigenvalue `lam_0` of `T_0` is **simple and
isolated**. Then the Perron state is differentiable at `eps = 0` with

`psi'(0) = R_red V psi_0`,

where `R_red` is the reduced resolvent of `T_0` on `psi_0^perp`, and the first
Perron moment obeys

`m_1'(0) = 2 <R_red V psi_0, J psi_0>`.

On the `NMAX = 5` box the runner evaluates this closed form as
`m_1'(0) = 4.424199803e-04`, nonzero, and confirms it against a central-
difference derivative whose error falls by `4.000x` per halving of `eps` - the
second-order rate a wrong derivative would not reproduce. The box `T_0` has a
simple top eigenvalue with relative spectral gap `9.768599e-01`, and the ray
stays strictly positive over the sampled window.

The whole untruncated statement therefore reduces to a single named gate:

> **Gate (not supplied here).** On the full untruncated character sector, `T_0`
> and `V` are bounded self-adjoint operators and the top eigenvalue of `T_0` is
> simple and isolated from the rest of the spectrum.

Granting that gate, the identical first-order argument gives untruncated
non-uniqueness. The gate needs essential-spectrum control on the large-`(p,q)`
character coefficients, which the current stack does not supply. Until it is
proved, the untruncated conclusion stands open.

## What this closes

- exact proof, on the 36-state `NMAX = 5` box, that explicit source-operator
  realization plus Perron reduction still do **not** force a unique
  framework-point Perron measure on that box, even inside a supplied strictly
  positive diagonal `D_6^loc R` subclass
- exact proof, on the same box, that the symmetry-reduced Jacobi coefficients
  are still open on the current stack
- exact reduction of the untruncated lift to the single named simple-isolated
  top-eigenvalue gate above, with the first-order derivative that gate would
  activate computed in closed form and verified to second order
- exact clarification of what new theorem object is actually needed next:
  first the untruncated spectral gate, then the physical mixed-kernel
  compression/diagonality identification, then the explicit resulting
  source-sector operator or an equivalent exact Perron eigenvector construction

## What this does not close

- the untruncated source-sector statement: non-uniqueness off the `NMAX = 5` box
  is not proved here
- the simple-isolated top-eigenvalue gate for the untruncated `T_0`
- explicit Jacobi coefficients at `beta = 6`
- explicit Perron moments at `beta = 6`
- physical Wilson mixed-kernel compression or residual diagonality
- analytic closure of canonical `P(6)`
- repo-wide repinning of the canonical plaquette

**Downstream hygiene (2026-07-25).** Every theorem in this note is stated on the
36-state `NMAX = 5` dominant-weight box. Full-sector non-uniqueness and physical
Wilson non-uniqueness remain **open** until the untruncated simple-isolated
top-eigenvalue gate above is proved. Downstream work must cite this note for the
box statement only, and must not read it as an untruncated or physical-Wilson
result.

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_perron_jacobi_underdetermination.py
```

Expected summary:

- `THEOREM PASS=8 SUPPORT=5 FAIL=0`
