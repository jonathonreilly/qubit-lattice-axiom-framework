# R1 pre-registration (BSM-naturalness route agent), 2026-10-18

Written before any run.

## T1 localisation family (clockwork, warped, domain wall, skin, taste clockwork)

Lemma A (transitivity): if the rule's symmetry group acts transitively on the
gears (sites or taste corners) by unitary/permutation maps, every
non-degenerate mode has equal weight on every gear; for a degenerate
multiplet the summed weight is equal on every gear.
Lemma B (orientation): bond reversal (a proper cubic rotation composed with a
translation) forces any link-preserved U(1) to have charge ratio q^2 = 1, so a
one-ended localised protected mode (clockwork, warp, Hatano-Nelson skin) is
impossible; a two-ended edge pair is allowed and its splitting is e^{-L/xi}.

Readings fixed in advance:
- A-CHECKED if the largest weight deviation of non-degenerate modes is below
  1e-10 on the ring, the 4^3 cubic torus with spin-1/2 internal action, and
  the 2^4 block; A-FAIL (kills Lemma A) if any deviation exceeds 1e-6.
- B-CHECKED if: clockwork end ratio equals q^-N at w = 0; for w >= 1e-3 the
  lowest eigenvalue is at least 1e-3 (no protected zero mode); at w = 1 the
  lowest mode has end ratio 1. B-FAIL otherwise.
- C (two walls): report xi and the wall separation L* giving 2e-17 for O(1)
  rule values. No pass/fail; it names the number.

## T2 relaxion toy on the record count (native monotone scanner)

Records are permanent, so the record fraction is monotone: a native relaxion
scanner. Toy: mu^2_i = 1 - 2 s_i, s_i = record fraction in a cube of side
2R+1; unrecorded sites with mu^2_i > 0 form a record with probability p per
tick; formation stops where mu^2_i <= 0 (backreaction). Measure the frozen
floor F = mean |mu^2| and mean v^2 = mean max(0, -mu^2).

Readings fixed in advance:
- NATIVE-RELAX-FAIL if at p = 1 with R = 1 the floor F >= 0.01 (no hierarchy
  from native rate and nearest-neighbour scanning).
- Report the fitted scaling of F with p and with V = (2R+1)^3. The route's
  named number is whichever of p or V the floor tracks.
