---
claim_id: staggered_one_qubit_blocks_carry_a_cubic_covariant_dirac_tick_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
claim_scope: "One amplitude per site of Z^3, grouped into 2x2x2 blocks (translations by two sites), with the proper cubic rotations acting about block centres by signed permutations of the eight corners (staggered phases). Up to diagonal gauge, the signed corner actions are either integer or spinorial (quarter-turn lifts of order 8); the spinorial ones are, up to phases, C^2 (x) E (x) E_1/2, i.e. two copies of the spin-3/2 representation (independently confirmed). The other classes contain only scalar and spin-1 pieces. For the spinorial class there is a unitary, exactly block-covariant, moving one-tick walk with hops of at most one block, obtained by transporting the two-qubit Dirac walk U_2q (x) 1_E through an intertwiner. Numerically it has a single isotropic massless cone at k = 0 carrying eight components (two Dirac fermions) and no other band touching on a grid. Exact (Theorem 3, Singular primary decomposition plus a hand real-locus argument): with nearest-site hops only, every unitary covariant walk on the spinorial block is flat. Not claimed: that the integer classes freeze, or any continuum identification beyond the cone."
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

## Theorem 3 — no nearest-site staggered tick propagates (exact, computer-assisted)

Restrict the spinorial block walk to nearest-site hops: every site
displacement has components in {-1, 0, 1}. Then every unitary covariant walk
is flat, i.e. its spectrum does not depend on k. Nothing propagates.

*Proof.*
1. **The equations.** The covariant nearest-site family has one coefficient
   c_t per hop-type orbit t, eleven in all. The independent checker derived
   the unitarity equations exactly over Q: 55 bilinear equations in c and
   cb = conj(c), with cb treated as independent variables.
2. **The components.** Singular `minAssGTZ` over Q gives the minimal
   associated primes, eight components of dimensions 4, 4, 2, 2, 2, 2, 4, 4.
   Every unitary walk lies on one of them.
3. **Reality on each component.** Impose cb = conj(c), reading off the
   printed generators:
   - **Components 1, 2.** Every hop type with an inward step vanishes. On
     component 2 this uses the generators c4 cb4 + c5 cb5 and c2 cb2 + c8 cb8,
     which are sums of |c|^2.
   - **Component 7.** Every hop type with an outward step except 000
     vanishes, because cb3..cb6 are generators.
   - **Components 3–6.** Only the on-site coefficient survives: either a
     generator c9 cb9 + c10 cb10 appears, or the phase relations force
     c9 = 0.
   - **Component 8.**
     - The relations c_a cb_b = c_b cb_a among the in-type coefficients
       a, b in {7, 8, 9, 10} make them share one phase, c_a = r_a e^{i theta}.
     - The quartic generator becomes
       (r8^2 - 2 r9^2)^2 + r10^2 (2 r8^2 + 4 r9^2 + r10^2) = 0, so
       r10 = 0 and r8^2 = 2 r9^2. The norm generator then gives
       r7^2 + 9 r9^2 = 1.
     - The generators for c3..c6 become c_j = e^{2 i theta} conj(c_j), so
       c_j = rho_j e^{i theta} with rho_j real.
     - cb4^2 + cb5^2 = 0 gives rho4 = rho5 = 0; cb4 cb5 = cb6^2 gives
       rho6 = 0; cb3^2 + 2 cb5^2 - 2 cb3 cb6 + cb6^2 = 0 gives rho3 = 0.
4. **Flatness.** A walk with inward and on-site steps only never leaves its
   block. One with outward and on-site steps only never leaves the shifted
   cube around each block corner. Either way it is block-diagonal on a
   translation-invariant partition, every block is identical, and the bands
   are flat. ∎

Scripts and outputs are in
`.claude/science/physics-loops/toe-campaign-20261015/nearest_site/` (Singular)
and `independent_check_B7/` (the equations).

Reading: on staggered one-amplitude blocks, propagation and locality trade
off. Nearest-site hops cannot propagate at all. The independent check's
two-layer walks reach two sites per tick and propagate, but with doublers.
The doubler-free tick of Theorem 2 reaches three.

## What did not work, or was not tested

- **Nearest-site locality.** Settled by Theorem 3: no nearest-site version
  propagates.
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

## No-Go Discipline Gate (Theorem 3)

- **N1 — routes around the claim.** Longer hops (Theorem 2, and the
  two-layer walks) do propagate; that is covered and they are outside the
  claim. So are other sign classes (integer classes move with nearest-site
  hops but have no linear cone, per the independent check), larger blocks,
  interacting rules and continuous time. None of these is excluded.
- **N2/N3 — scope.** One wall only, stated for the spinorial class,
  nearest-site displacement and the covariant family of 11 coefficients.
- **N4 — inputs.** The equations come from the independent checker's exact
  derivation. The component computation is a standard exact algorithm over
  Q. The real-locus steps use only printed generators.
- **N5 — wording.** The claim is "flat bands only". It is not a statement
  about what nature uses.
- **N6/N7 — strongest objection.** The checker's equations could carry a
  convention error. Mitigation: my own covariant nearest-site family also
  has dimension 11, and all ~320 numerical solutions from both
  implementations were flat.
- **N8 — earlier claims.** This narrows the earlier "nearest-site open"
  statement to a no-go.

## Verification

```bash
python3 scripts/staggered_one_qubit_block_cubic_dirac_tick_2026_10_16.py
```

Expected: `TOTAL: PASS=11 FAIL=0` (a few minutes).
