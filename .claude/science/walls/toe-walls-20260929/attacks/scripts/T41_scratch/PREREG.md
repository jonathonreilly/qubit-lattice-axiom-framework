# T41 pre-registration (written before any of t41_test.py was run)

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check only).

## Hypothesis under test (H*)

Closing T41 as posed (the quark determinant readout is in the block-multiplicative
class and is constant on K-orbits, "same channel as the charged-lepton carrier")

  (a) is NOT NEEDED for a real determinant on the repo's balanced surface (pairing gives it
      with no lepton input, and the mass phase does not couple to anything there), and
  (b) is NOT SUFFICIENT for arg det(M_q) = 0 where the phase does couple (a surface with
      nonzero index): the class readouts are blind to the phase while the weight carries it.

## Sub-tests and readings

S1 Balanced additive surface (K real antisymmetric on a 4^3 torus with random Z2 links, eps grading,
   equal sublattices; flavor factor A, operator K(x)1 + 1(x)A).
   PASS: for Hermitian A with every sign pattern of eigenvalues, arg det = 0 (|phase| < 1e-8) and
         |det| equal across sign patterns at fixed |a_k|; det(K + m e^{i alpha eps}) independent of
         alpha (rel. spread < 1e-8).
   FAIL: any Hermitian sign pattern gives arg det != 0, or alpha-dependence > 1e-6.
   (Non-Hermitian A is recorded as information only: expected arg det != 0.)

S2 Index-carrying graded surface, Yukawa form O = [[1(x)m, B(x)1],[-B^dag(x)1, 1(x)m^dag]],
   B is n+ x n-, index nu = n+ - n-.
   PASS: arg det O = nu * arg det m (mod 2 pi) within 1e-8 for all random cases with nu in
         {-2,-1,0,1,2} and generic complex m; nu = 0 gives phase 0 for every complex m; Hermitian m with
         exactly one negative eigenvalue gives phase pi for nu = 1 and 0 for nu = 2;
         |det O| equals det|m|^|nu| * prod det(m m^dag + s^2) within 1e-8 relative.
   FAIL: phase depends on phi on the balanced (nu = 0) surface (then T41's target is live there), or
         formula mismatch > 1e-6.

S3 Class readouts versus the weight phase, on the S2 family m(phi) = diag(e^{i phi},1,1) * m0.
   Class = {|det O|, exp(i k arg det O) with k = 0 forced by orbit constancy}.
   PASS: every class readout is phi-independent (spread < 1e-9) while the toy topological-sum weight
         Z(phi)/Z(0) = sum_nu p_nu cos(nu phi) / sum p_nu deviates from 1 by > 1e-3 at phi = 0.3 and the
         CP-odd moment Im<nu>_phi is nonzero (> 1e-3).  p_nu is a stand-in, NOT framework content.
   FAIL: class readouts vary with phi.

S4 Native quark carrier (Hermitian Schur-NNI + complex 1-3 carrier, docs/QUARK_CP_CARRIER_COMPLETION_NOTE,
   scripts/frontier_quark_cp_carrier_completion.py; note's solved point, imported read-only).
   PASS: reproduces the note's |V_us|,|V_cb|,|V_ub|,J to 0.5%; then for all 64 eigenvalue-sign patterns
         (s_u, s_d in {+-1}^3 x {+-1}^3 applied in the eigenbasis, Hermiticity kept) the masses, |V_ij|, J are
         unchanged (< 1e-8) while arg det(M_u M_d) takes both values 0 and pi (32 / 32).
   FAIL: the fitted observables change under sign flips (then the atlas already contains the sign datum).
   Also recorded: number of negative eigenvalues of the note's native M_u, M_d.

S5 K-orbit indexing, lepton circulant vs quark carrier (the lane's "cheapest test", L11-W5).
   Gauge invariants of a Hermitian 3x3 under diagonal rephasing and permutation: diag, |off-diag|, cycle
   phase Phi = arg(M12 M23 M31).  K (complex conjugation) sends Phi -> -Phi.  K is a gauge relabeling
   iff Phi in {0,pi} or some odd permutation preserves (diag, |off-diag|).
   PASS (for "the two K-orbit structures differ"): lepton Brannen circulant admits such a permutation;
         the quark M_u and M_d do not, and have Phi not in {0,pi}; J flips sign under (M_u,M_d)->(M_u*,M_d*).
   FAIL: a quark carrier admits it.

## Decision rule for the outcome

All of S1-S4 PASS -> MISFRAMED (cheaper question: is there an index supplier; then joint theta-bar).
S2 FAIL -> STANDS (the phase would be visible on the balanced surface, T41 is live).
S4 FAIL -> re-examine toward PRICED (the atlas would carry the datum; the wall would be the sign bit).
S5 is informational for Route 3 only.

## What this test cannot say

It does not show the four axioms have or lack an index supplier; it does not touch real 4D QCD, the
continuum anomaly, or any gauge-side statement; it uses the repo's own K-real staggered surface and a
graded-block model of the chiral index, which is the same algebra as
docs/THETA_ASSEMBLY_PAIRED_SHIFT_FIXED_GRADING_MCKEAN_SINGER_REDUCTION_NARROW_THEOREM_NOTE_2026-07-02.md
(L2, C1) generalised to a flavor matrix (that note treats a scalar m).
