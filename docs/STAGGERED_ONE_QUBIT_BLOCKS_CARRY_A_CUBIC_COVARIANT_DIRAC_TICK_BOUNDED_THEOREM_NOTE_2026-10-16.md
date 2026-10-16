---
claim_id: staggered_one_qubit_blocks_carry_a_cubic_covariant_dirac_tick_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
claim_scope: "One amplitude per site of Z^3, grouped into 2x2x2 blocks (translations by two sites), with the proper cubic rotations acting about block centres by signed permutations of the eight corners (staggered phases). Up to diagonal gauge, the signed corner actions are either integer or spinorial (quarter-turn lifts of order 8); the spinorial ones are, up to phases, C^2 (x) E (x) E_1/2, i.e. two copies of the spin-3/2 representation (independently confirmed). The other classes contain only scalar and spin-1 pieces. For the spinorial class there is a unitary, exactly block-covariant, moving one-tick walk with hops of at most one block, obtained by transporting the two-qubit Dirac walk U_2q (x) 1_E through an intertwiner. Numerically it has a single isotropic massless cone at k = 0 carrying eight components (two Dirac fermions) and no other band touching on a grid. Not claimed: that the integer classes freeze, that a nearest-site (KS-type) version exists, any continuum identification beyond the cone."
upstream_dependencies:
  - minimal_axioms
  - two_qubit_site_unfreezes_the_cubic_tick_doubler_free_dirac_walk_bounded_theorem_note_2026-10-16
runner: scripts/staggered_one_qubit_block_cubic_dirac_tick_2026_10_16.py
---

# Staggered one-qubit blocks carry a cubic-covariant Dirac tick

**Date:** 2026-10-16
**Type:** bounded_theorem
**Status:** bounded-support; exact construction with numerical spectral
checks; unaudited.
**Status authority:** independent audit only. Nothing here is adopted.

## Result up front

The companion notes show two things:
- with one qubit per site and the cube symmetry acting about every site, no
  one-tick walk moves;
- a two-qubit site does move, and carries a Dirac fermion.

This note shows the extra information does not have to sit on one site. It
can be spread over a neighbourhood of one-amplitude sites:

1. **The signed corner actions.** Rotating a 2x2x2 block about its centre
   permutes the eight corners. Allowing a sign on each corner (staggered
   phases), the actions fall into three classes. Exactly one class is
   spinorial, and up to phases it is

       C^2 (x) E (x) E_1/2  =  two copies of spin 3/2,

   with E the two-dimensional irrep of the cube group and E_1/2 the spin-1/2
   lift. The other two classes contain only scalar and spin-1 pieces, so no
   spinor factor.
2. **A moving, exactly covariant tick on the spinorial blocks.** Take the
   two-qubit Dirac walk U_2q (flavor (x) spin) of the companion note,
   tensor it with the identity on E, and transport it to the eight corners
   with a unitary intertwiner T. The result is

       W(k) = T (U_2q(k) (x) 1_E) T^dagger.

   It is unitary, covariant under the signed block action, and moves. Its
   hops reach at most one block, i.e. up to three sites per axis.
3. **Spectrum (numerical).** W has one isotropic massless cone at k = 0 in
   block momentum, with all eight components at the same speed: two Dirac
   fermions per block. There is no other zero of the quasienergy on the grid
   checked.

Implication, not adopted: the one-qubit-per-site reading of the Qubit axiom
is not ruled out by the freeze theorems. Motion and Dirac structure come back
when the cube symmetry acts on staggered 2x2x2 neighbourhoods rather than on
single sites. Per Dirac fermion this uses the same four complex amplitudes as
the two-qubit site, spread over four sites instead of stacked on one. This is
the discrete-time, exactly covariant counterpart of the framework's open
staggered-Dirac gate.

## Premises

- **Axioms used.** The Lattice axiom supplies Z^3 and the proper cubic
  rotations; the Qubit axiom is read in its single-amplitude (slot) form, one
  complex amplitude per site.
- **Declared objects, not framework content.** These are the 2x2x2 blocking
  (translations by two), the action of the rotations about block centres,
  the corner signs and the one-tick walk. Nothing selects a block origin.

## Theorem 1 — classification of signed corner actions

Let P(R) be the permutation of the corners v in {0,1}^3 under rotation about
the centre, and D(R) = diag(s_R) P(R) with signs s_R in {+-1}^8 chosen for
the two quarter-turn generators. Over all 2^16 choices, the generated groups
of order 24 or 48 fall into three classes by their trace data:

- **Order 24.** A linear representation of O, which decomposes as
  (A1 + T1) + (A1 + T1) twisted by a character.
- **Order 48, quarter-turn lifts of order 4.** Projectively the same
  integer content.
- **Order 48, quarter-turn lifts of order 8.** This class is spinorial. Its
  intertwiner space with phase-twisted C^2 (x) E (x) E_1/2 has dimension
  4 = 2^2, and with twisted spin 3/2 it has dimension 2. So it is two copies
  of spin 3/2, and as a conjugation action it is the same as
  1_2 (x) D_E (x) D_1/2.

The other classes have no intertwiners with E_1/2 or spin 3/2. The
intertwiner computations are numerical null spaces on exact signed-
permutation and spin matrices, with residuals at machine precision.

## Theorem 2 — a moving, exactly covariant block tick

U_2q is covariant under 1 (x) D_1/2 on flavor (x) spin (companion note,
Theorem 1). Then U_2q (x) 1_E is covariant under 1 (x) D_1/2 (x) D_E, and
conjugation is blind to the phases. So for the spinorial class,
W = T (U_2q (x) 1_E) T^dagger satisfies W(Rk) = D(R) W(k) D(R)^dagger. W is
unitary because U_2q is, and it has the same hop range in block units. The
runner checks unitarity and covariance at random momenta (error ~ 1e-15). ∎

**Spectrum (numerical).** With U_2q the companion note's explicit massless
member (b* = (11/30, sqrt(u*), 3/20)), W has all eight quasienergies equal
to 0.9144 |k| near k = 0 in four directions. On a 21^3 grid,
omega >= 0.63 |2 sin(k/2)|, so the only zero is k = 0. The eight components
form two Dirac fermions. The pair is the counterpart of the two "tastes" of
Kogut–Susskind fermions in three spatial dimensions.

## Independent check

A fresh agent context, given only the problem, confirmed the classification
and found more. The signed corner actions form four diagonal gauge classes
(H^2(S4, Z2) = Z2^2). Two are integer, one of them projectively the other.
Two are spinorial, gauge-equivalent to each other and each two copies of
spin 3/2 (the "one spinorial class" above, up to gauge).

It also found propagating walks by a different construction, the two-layer
(partitioned) walk W = G(k) qB G(k)^dagger qA. That is a block unitary
followed by a shifted-block unitary, both in the commutant, with maximum
displacement two sites. One exact example has
cos omega = (1/2)[1 +- sqrt((sin^2 k1 + sin^2 k2 + sin^2 k3)/3)] and
isotropic cones, but it has identical nodes at all eight time-reversal-
invariant momenta, so unlike Theorem 2's walk it is not doubler-free.

On nearest-site locality:
- the integer classes have exact dispersive walks, but an antipodal-symmetry
  argument shows they have no linear cone;
- the spinorial classes gave only flat, strictly localized solutions in about
  300 converged runs, which agrees with the search here and is not proved.

Scripts are in `.claude/science/physics-loops/toe-campaign-20261015/independent_check_B7/`.

## What did not work, or was not tested

- **Nearest-site locality.** Kogut–Susskind fermions hop to nearest sites
  only. Restricting the spinorial block walk to hops of one site per axis
  leaves an 11-dimensional covariant family. Unitary solutions found there
  have flat bands: the spectrum does not depend on k, so nothing propagates.
  This holds for 20 dispersion-constrained starts here and about 300
  independent runs; it is numerical, not proved. The tick of Theorem 2 needs
  hops of up to three sites per axis. The independent check's two-layer walks
  need two, but they have doublers.
- **Integer classes.** These have no spinor factor. By the companion note's
  criterion they are not expected to move, but that is not proved here.
- **Larger blocks, other block origins, interacting rules.** Not considered.

## Relation to prior work

- **Taste basis.** That the eight sites of a cube carry two Dirac flavors is
  standard for Kogut–Susskind fermions in 3+1 dimensions (Hamiltonian
  formulation; see e.g. arXiv:2511.06198).
- **Staggered walks.** Staggered discrete-time quantum walks and their
  relation to Kogut–Susskind fermions have been studied mainly in lower
  dimensions (arXiv:1807.08303, arXiv:1906.04483).
- **Non-staggered walks.** 3+1-dimensional Dirac walks with several
  components per site are known (D'Ariano et al., Entropy 18, 228, 2016).
- **New here.**
  - the classification of signed corner actions under block-centred cubic
    rotations, and the identification of the spinorial one as two copies of
    spin 3/2;
  - an exactly block-covariant one-tick unitary walk with one amplitude per
    site that carries a massless isotropic Dirac pair.

## No-Go Discipline Gate

This note makes no impossibility claim; the boundary items above are
reported at their own evidence level.

## Verification

```bash
python3 scripts/staggered_one_qubit_block_cubic_dirac_tick_2026_10_16.py
```

Expected: `TOTAL: PASS=11 FAIL=0` (a few minutes).
