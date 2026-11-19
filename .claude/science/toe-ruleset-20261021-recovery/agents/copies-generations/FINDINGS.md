# copies-generations: findings

Runner `runner.py`: TOTAL PASS=13 FAIL=0, 12 s. Note: `note.md`.

## Theorems (rederived, exact)

1. **Why the copies don't mix.** In the base tick every block step is (+-1,+-1,+-1), so U(K+G) = U(K) for
   G = pi(1,1,0), pi(1,0,1), pi(0,1,1), and U(K + pi(1,1,1)) = -U(K). The four cosets of B = {x = y = z mod 2} are invariant,
   so the four copies are identical, decoupled systems.
2. **Copy symmetry is S4.** Block translations (Z2^2 on cosets) and site rotations (S3) generate S4, which acts on the copies as 1 + 3.
   Its commutant is span{1, J}. The general covariant copy mass matrix is therefore **diag(m_s, m_t, m_t, m_t)**. Singlet-triplet
   mixing is forbidden by crystal momentum. In coset form, m_s = a + 3d and m_t = a - d. Without one-block translations (S3 only)
   the matrix allows singlet-triplet mixing beta. Its spectrum is then b - d (twice) and (a+b+2d)/2 +- sqrt(((a-b-2d)/2)^2 + 3|beta|^2).
   The commutant dimensions are 2 for translations and rotations, 2 for translations and C3, 4 for translations and D2, 5 for S3
   and 6 for C3 alone.
3. **Splitting needs a step outside B.** Mixing in the corner basis is impossible under block-translation covariance. Splitting is possible.

## Proposal (supplied rule)

> "In each axis substep, the left modes move, then turn into right modes within the block by angle theta, then the right modes move."

At theta = 0 this is the base tick. It is unitary, with steps in {-1,0,1}^3.

**Corner theorem (exact, any M, any axis order).** At each corner the spectrum is {+-mu, pi +- mu}, each twice, with
**mu = m + theta(3 - 2n)**, where n is the Hamming weight of the corner.

- **P1: theta replaces m, so no new parameter.** The singlets have mass 3 theta and the triplets theta. In each sector that is
  one heavy and three light, with the ratio 3 exact. Overall there are six light copies, in two triplets. With M = .5 and
  theta = .09 the masses are 0.09 x6 and 0.27 x2, and the zone minimum is 0.0900.
- **P2: m and theta.** This gives exactly three light copies, but only on a tuned branch theta = m + delta, |delta| << m.
  With m = .1, theta = .09 the masses are 0.01 x3, 0.17, 0.19 x3 and 0.37. The tuning is supplied, not a rule.
- The triplet is exactly degenerate whenever the angles are equal. Axis-dependent angles split it as m - sum(theta) + 2 theta_k.
  The only other way to split it is a coset-privileging term. Either way something is privileged: an axis, or a site class.
- The mean block step per axis equals the group velocity (8e-10), so the input to the CL-7 identity survives.

## Koide (structural only)

Covariant rules force b = 0: Q = 1/3, r = 0. A C3 circulant needs a coset-privileging term and the loss of the two-fold axes.
Even then the tick's mass enters the quasi-energy linearly, so r = 1/2 would give sum m^2/(sum m)^2 = 2/3, not Koide's Q.
The n = 1 copies carry exactly the diag(-1,+1,+1) translation triple of the three-generation observable note, and here those
translations are symmetries of the tick. C3[111] is not a symmetry of the proposal off the corners. No generation reading follows.

## Interactions

- **Base tick.** The copies share no block: tick, burns, relays and switching all stay within one coset, assuming relay steps are
  tick steps. They interact **only** through the shared gravity and vector responses, with equal coupling.
- **Proposal.** Burns are site-local, so they scatter copies into one another directly, with |matrix element| = 1 between any two
  corners. That is a direct channel beyond gravity and gauge.

## Smuggling review / failures

- Supplied: the mode assignment, the substep and L/R order, M, theta, and the flip acting on both families. P1 privileges nothing,
  and its ratio 3 follows from three axes. P2's "three light" is a plugged relation.
- The proposal is spectrally covariant under 8 of 24 rotations (the D4 about the middle axis), against 24 of 24 for the base.
  Exact cubic covariance is open; the corner theorem does not depend on it.
- The proposal has a rest step of norm sin^3 theta and non-diagonal steps. **CL-4 ("relays always move one block per tick") would
  need amending.**
- Without M the zone has gapless points, so M is still required. For theta of about 0.3, the band minimum moves off the corners
  (0.2928 < 0.3).
- Process: one exploration run started at load 9.4 (about 2 s) before I enforced the wait loop. Every later run was below 8.
