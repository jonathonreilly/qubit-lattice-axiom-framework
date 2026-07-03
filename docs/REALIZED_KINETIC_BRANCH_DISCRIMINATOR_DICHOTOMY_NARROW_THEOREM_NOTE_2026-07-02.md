# Realized Kinetic Branch: Discriminator Dichotomy on the Two-Flux-Class Surface

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** On the parent two-flux-class kinetic surface, the two
representatives are separated by four computable representative-level
discriminators: D1, internal-factor load and grade-1 Clifford capacity;
D2, first-order Dirac-square dispersion versus scalar perfect-square
dispersion; D3, isolated zero points versus an extensive zero surface;
and D4, nonvacuous per-direction qubit-factor admissibility algebras
versus the scalar vacuous algebra. These discriminators are verified on
the parent K0/K1 phase systems, with frame-covariance and perturbation
legs. The selector bit is not decided here, and the Admissibility
reading is not decided here.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:**
[`scripts/realized_kinetic_branch_discriminators_2026_07_02.py`](../scripts/realized_kinetic_branch_discriminators_2026_07_02.py)
**Runner cache:** `logs/runner-cache/realized_kinetic_branch_discriminators_2026_07_02.txt`

## Why This Note Exists

The reset impact map `AXIOM_RESET_IMPACT_2026-06-29.md` separates the
spatial kinetic branch layer from generic dynamics and says that a
realized branch condition should state the needed structure:
"nonzero first-order Dirac-square kinetic carrier, translation covariance/locality as required by the target theorem, and the mutually anticommuting self-adjoint-unitary coefficient family if the d<=3 Clifford-capacity theorem is being invoked".

The parent kinetic-class note leaves the one-bit residual explicit:
"the flux(-1) selector is not forced because K0 also satisfies the constraints". This note is consistent with that sentence. It supplies
discriminators on the two-class surface; it does not select the branch.

The same reset map also warns that scalar joint commutant is too weak:
a noncommuting Pauli pair can already have scalar joint commutant. D1
therefore states the saturation form: three mutually anticommuting
self-adjoint unitaries exist on `C^2`, and a fourth cannot.

## Statement

The parent representatives are used exactly:

```text
K0: phi=+1, representative t == 1 (scalar tight-binding; extensive zero surface).
K1: phi=-1, representative eta0: eta0_1 = 1, eta0_2 = (-1)^{x1}, eta0_3 = (-1)^{x1+x2}
(Kawamoto-Smit class; 8 isolated Dirac zeros; = absorbed naive Dirac).
```

The runner mirrors the parent phase conventions and symmetric
unit-amplitude nearest-neighbor hopping convention. Thus

```text
K0(p) = 2 * sum_mu cos(p_mu) * I.
```

For K1, the runner computes the absorbing-frame edge coefficients from
the parent construction
`T(x) = sigma_1^x1 sigma_2^x2 sigma_3^x3` and the eta0 phases, then
extracts

```text
Gamma_mu = (1 / 2i) * (K_raw(+q_mu) - K_raw(-q_mu)).
```

The normalized blocked symbol is

```text
K1(p) = sum_mu Gamma_mu sin(p_mu).
```

**D1 - internal-factor load / Clifford capacity.** K0 acts scalarly on
the one-site qubit factor: direction coefficients are proportional to
`I`, and the joint commutant is all of `M_2(C)`. K1 has a computed
coefficient family `{Gamma_1, Gamma_2, Gamma_3}` of mutually
anticommuting self-adjoint unitaries. This family saturates the
grade-1 Clifford capacity of `C^2`: exactly three can exist, and the
linear system for a fourth has only the zero solution.

**D2 - Dirac square versus scalar perfect square.** K1 satisfies
`K1(p)^2 = (sum_mu sin^2 p_mu) * I`; adding a mass slot gives
`m^2 + sum_mu sin^2 p_mu`. K0 is the scalar tight-binding function
`2 * sum_mu cos p_mu`, whose square is a scalar perfect square. A
constant shift of K0 cannot reproduce the Dirac-square dispersion as a
function.

**D3 - zero-set geometry.** K0 has an extensive codimension-1 zero
surface. K1 has the eight isolated zero points with all momenta in
`{0, pi}`.

**D4 - per-direction admissibility action on the qubit factor.** For
each direction, the K1 coefficient `Gamma_mu` generates a
direction-tagged maximal abelian subalgebra of `M_2(C)` of dimension
2. The K0 direction coefficient generates only `C * I`, dimension 1.
The dimensions are invariant under the parent local `U(1)` frame
changes.

## Proof Sketch

**D1.** Checks T2-T4 compute the coefficients before comparing them
with the claimed algebraic properties. T3 verifies the K0 coefficients
are scalar and have joint commutant dimension 4. T4 verifies K1
Hermiticity, unitarity, pairwise anticommutation, scalar joint
commutant, and the no-fourth-element capacity statement by a linear
nullspace computation.

**D2.** Checks T5-T6 evaluate the symbols on grids. T5 verifies
`K1(p)^2` and the mass-slot square. T6 verifies the K0 scalar symbol
and minimizes over constant shifts `c`, finding a positive floor for
`max_p |(2 sum cos p + c)^2 - (m^2 + sum sin^2 p)|`.

**D3.** Check T7 counts zero-grid cells at `N = 24` and `N = 48`.
The K0 count grows from 428 to 1388, while K1 remains exactly 8 at
both resolutions.

**D4.** Check T9 computes the unital star-algebra dimensions generated
per direction. K0 gives `[1, 1, 1]`; K1 gives `[2, 2, 2]`. The same
dimensions survive a local `U(1)` frame change, while an illegal
non-diagonal `SU(2)` subregion frame produces a covariance break.

Two guard legs prevent target-shaped checks from passing accidentally.
T1 recomputes the K0/K1 plaquette fluxes on `L = 4` and `L = 6`. T8
flips one eta0 link sign, producing mixed plaquette flux and a broken
blocked anticommutation norm. T10 checks proper-cubic rotation
covariance by exact K0 equality and an operator-level K1 leg: the
rotated K1 hopping operator equals `W H W` for a site-local `Z2` frame
`W` reconstructed from the edge sign ratios under an explicit
cocycle-consistency gate, and the same reconstruction rejects a
one-link flux flip of the `eta0` background.

## Consequence And Residual

A realized kinetic context on this surface whose nearest-neighbor
structure realizes a NONVACUOUS covariant determination of available
qubit possibilities lies in K1, and then the nonzero first-order
Dirac-square kinetic carrier with the saturating anticommuting
self-adjoint-unitary coefficient family follows from the parent's
absorbing-frame theorem.

The one-bit residual is NOT decided here: it becomes the named
interpretive question whether the Admissibility axiom's clause ("for each site,
the available possibilities are determined by, and vary with, the
nearest-neighbor conditions") is read as a nonvacuous determination on the
qubit factor. The parent sentence "the flux(-1) selector is not forced
because K0 also satisfies the constraints" is therefore preserved:
this note gives discriminators, not a selection theorem.

The next path this opens: the conditional-record route (branch
registration by realized cross-site records) and the adjudication of
the Admissibility-clause reading.

## Boundaries

- Representative-level on the parent's surface. Class-level transport
  is inherited only where the parent frame theorems transport it; D4
  frame covariance is verified for local `U(1)` frames.
- No selector forcing.
- No decision on whether the Admissibility clause must be read
  nonvacuously on the qubit factor.
- No audit status is set here.

## Dependencies

- [`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md)
  - parent surface and the two classes.
- [`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
  - absorbing frame and gauge-class context.
- [`CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md`](CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md)
  - per-site `C^2` carrier.
- [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
  - Cl(3) per-site module.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  - Admissibility clause quoted in the residual.

Context only: `AXIOM_RESET_IMPACT_2026-06-29.md`,
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`.

## Runner And Cache

Primary runner:
[`scripts/realized_kinetic_branch_discriminators_2026_07_02.py`](../scripts/realized_kinetic_branch_discriminators_2026_07_02.py)

Expected cache target:
`logs/runner-cache/realized_kinetic_branch_discriminators_2026_07_02.txt`

Current local runner result:

```text
TOTAL: PASS=20 FAIL=0
```

The cache file is generated from the paired runner and SHA-pinned.

## Changelog

- **2026-07-02.** Initial note and numpy runner. The runner reports
  `TOTAL: PASS=20 FAIL=0`.
