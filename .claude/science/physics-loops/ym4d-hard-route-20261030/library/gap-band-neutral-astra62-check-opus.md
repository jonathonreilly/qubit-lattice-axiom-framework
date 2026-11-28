# Check of library/gap-band-neutral-astra62.md (FINISH row 1579; source row 1573)

Checker: Claude (Opus 5.5). Status: in progress.

## Plan

1. Read GOAL.md and FINISH.md (Rules, Working efficiently).
2. Read library/gap-band-neutral-astra62.md in full.
3. Read comparison sources: library/gap-mech-attack-fable.md section 3 (row 1529),
   library/gap-mech-attack-fable-check-astra62.md (check 1539), check 1123, row 1121 Lemma JI,
   library/gap-agy-seed-approaches-neon-check-astra62.md (check 1527 (vi)), row 1373.
4. Check Lemma 1 and the regularity boundary first; write verdicts.
5. Check Lemma 2, sewing, identities (1), (3), mixed derivative, separation example, comparisons,
   midpoint law, spectral positivity.
6. Decide the strictly-weaker-than-(PUR-io) question.
7. RESULT line and signature.

## Step log

- Step 1 done: read GOAL.md, FINISH.md Rules and Working efficiently, the full row (233 lines), the
  (PUR-io) definition (library/gap-agy-seed-approaches-neon.md 0.1), check 1123 degree remark
  (library/gap-l3-closure-check-astra.md, "The degree remark"), row 1529 section 3
  (library/gap-mech-attack-fable.md), check 1539 positive claims, check 1527 (vi), row 1121 Lemma JI
  (library/gap-conv-in-law-check-opus.md 8.6), row 1373 outline.
- Step 2 (Lemma 1, regularity boundary, orbit chart, sewing, (1), (3), separation, Lemma 3): verified
  by hand; verdicts written below in the Verdicts section once the cited inputs for (4)-(5) and the
  U(1) section are read.
- Step 3 done: read the cited inputs for (4)-(5) and the U(1) section: row 1568 Theorem E statement and
  Steps 1-4 (library/gap-band-cut-covariance-neon.md lines 247-277), check 1572 Step 7, row 1565 lines
  145-250 (library/gap-band-cut-covariance-astra62.md), check 1571 A1-A3. A numeric guide script for
  Lemma 1 could not run (no numpy under `python3 -I`); it was deleted. No numerics enter any verdict.

---

# Check report

Provenance: Claude (Opus 5.5), cross-provider check of row 1573 (author gpt-6.2-astra max), lane text as
read in the sparse checkout on 2026-11-26. This is a line-by-line check by one reader, not an audit.
Line numbers refer to library/gap-band-neutral-astra62.md.

## A. Decisive outcome

**Lemma 1, lines 37-51: HOLDS.**
- Dimers (line 39). On a j-line of even length the pairs {(2m-1,2m),(2m,2m+1)} partition the links.
  Orienting both links into the shared vertex makes the construction gauge-covariant.
- Algebra (lines 41-46). q_i^2 = r_i, m_i = x_i q_i, so (x_i,y_i) = (m_i q_i^{-1}, m_i q_i). Rotating
  both axes about d by pi sends a_i to -a_i, because a_i is perpendicular to d. This gives q_i -> q_i^{-1}
  and so the swap on both links. The rotation keeps a_1 x a_2, so d, the angles theta_i and m_i stay
  fixed. That makes R a circle action (R_s R_t = R_{s+t}, period 2 pi).
- Speed. Left multiplication is an isometry of R^4. The velocity has norm sin(theta_i/2)|d x a_i| =
  sin(theta_i/2), and a_i'' = -a_i gives the same bound for the second derivative.
- Haar (lines 48-49). (x,y) -> (x,r) -> (m,r) are Haar-preserving translations. The polar form gives
  independent theta, a, and the exceptional set is null. Given gamma = a_1.a_2, the frame
  F = (a_1, (a_2 - gamma a_1)/sqrt(1-gamma^2), d) is right-handed. Its conditional law is left-invariant
  under common rotations, hence Haar on SO(3). The motion is Rot_{d,s} F = F Rot_{e3,s}, a right
  translation by a fixed element. It preserves gamma and the conditional law, so it preserves the full
  product law.
- Covariance (line 51). Simultaneous gauge: r_i -> g_v r_i g_v^{-1}, and cross product and rotation
  commute with Ad(g_v). m_i -> g_t m_i g_v^{-1}, and the outputs transform as links. Common centre sign:
  r is fixed and m picks up the sign. The exceptional set is invariant under both, so the identity
  convention there is covariant.
- Lifted frame h (lines 53-54). Checked: equivariance under h -> g_1 h g_2^{-1}, Fubini for the extended
  measure, and the half-turn (hy, h^{-1}x) on the two physical orbits.

**Regularity boundary, line 56: HOLDS.** Restrict a jointly continuous homotopy to the embedded S^3
(one first-copy link free, everything else 1), then project onto that link. At angle 0 the map is the
identity (degree 1). At pi it is the constant 1 (degree 0). That contradicts homotopy invariance. The
full-support remark also holds: a continuous map equal to S almost everywhere differs from S only on an
open null set, which is empty.

Comparison with the earlier checks:
- Check 1123 (degree remark) excluded uniformly small chains of *site* maps and said multi-site maps
  were not covered. The projection argument here covers every continuous self-map of the doubled raw
  slice, so the stated extension is correct.
- There is no conflict with row 1529 section 3 or check 1539 (INN(a), INN(b) HOLD). There the swap is
  conjugation by J inside the connected group Sp(2). The interpolation is a weak kappa -> infinity limit
  in a larger configuration space. Any path from 1 to J leaves H = SU(2)^2, where the first-copy
  projection is undefined, so the degree argument does not apply.
- Lemma 1 avoids the obstruction differently: it is discontinuous on a null set (theta in {0, pi} or
  a_1 parallel to a_2).
- Endpoints differ. Row 1529 reaches the periodic Pi, which needs more than P_K, and check 1539 notes
  that the neutral form there needs per-replica centre twists. The present row puts P_0 in the kernel,
  so its half-turn reads P_K directly.

## B. Remaining statements

1. **Circle on the gauge and centre quotient Q, lines 60-66: HOLDS.** Checked:
   - tree disintegration;
   - three fundamental cycles with independent winding parities, and exactly one centre class with
     all three real parts positive;
   - the hemisphere-times-Haar law;
   - the frame from the first two axes;
   - the count D = r + 1 + 2(r-2) = 3r - 3 = 6n^3, with r = 2n^3 + 1;
   - the CDF/Gaussian chart and the orthogonal rotation of differences, which is an exact swap at pi
     (D is even).

   The row correctly says this circle has no speed bound.
2. **Sewing and Lemma 2, lines 70-84: HOLDS.**
   - int k^2 = Tr A^2 = Z_+(u), since u = 2v.
   - H(0) = 1.
   - H(pi) = Tr A^4 / Z_+(u)^2 = Z_+(2u)/Z_+(u)^2 = P_K, via the cycle x_1 y_1 x_2 y_2 and the
     symmetry of k.
   - H > 0 because k > 0.
   - H <= 1 by Cauchy-Schwarz and R_s-invariance of dY.
3. **Four-corner identity (1), lines 86-95: HOLDS.**
   - L(SX,SY) = L(X,Y) and L(SX,Y) = L(X,SY), so the corners are f, g, g, f.
   - The double integral of the mixed derivative is 2f - 2g = 2J.
   - E_mu e^{-J} = int L(X,Y) L(X,SY) / Z^2 = H(pi) = P_K.
4. **Mixed derivative as two pinned covariances, line 96: HOLDS.**
   - For v >= 2 no plaquette reads both ends.
   - The end half-weights are deterministic given the pin, so they drop out of the covariance.
   - The centre label is part of the joint law.
   - Speeds are at most 1 everywhere, which justifies Fubini.
   - Harmless slip: "only finitely many small K could have v < 2" is vacuous, since v >= b^K >= 3.
5. **(2) and Jensen, lines 98-105: HOLDS.** -log P_K <= E_mu J <= B_K. (1) is an identity, so it is an
   equivalent readout, as the row says.
6. **Identity (3), lines 109-115: HOLDS.** E J = 2 int (p - m) log k = int (p - m) log p, using
   log p = 2 log k - log Z. The log m term vanishes by equal marginals, which gives
   D(p||m) + D(m||p) = I + L.
   - This is Lemma JI of row 1121 (mean exchange cost equals mutual plus lautum information) in
     substance.
   - JI's display carries a factor 2 from its own Delta convention. The row's identity is verified
     directly, so the normalization difference changes nothing.
7. **Separation example, lines 117-123: HOLDS.**
   - Plaquette-trace functions are gauge and centre invariant: a contractible plaquette crosses each
     centre hyperplane an even number of times.
   - Their law is n-independent.
   - The one-step kernel is PSD, strictly positive, rank 3 and neutral.
   - The v-step kernel tends uniformly to aa* + c bb*, so P -> (1 + c^4)/(1 + c^2)^2 = 257/289 > 457/625.
   - On the a-b event the crossed kernels tend to 0 and the direct ones stay bounded below. The event
     probability is bounded below uniformly in delta and n, so E|J| -> infinity, and B_K >= E|J| by
     (1). The variant with c_K -> 0 also holds.
   - Consequence: on positive kernels, (2) is strictly stronger than the endpoint threshold. So is the
     signed bound E_mu J <= log(625/457), because D(m||p) -> infinity here too.
   - The row does not cite the same two-eigenvalue pattern in check 1527 (vi) (b_N kernel,
     eigenvalues 1 and 1/4, purity 257/289). That is an attribution gap, not a mathematical defect.
8. **Neutral Gaussian spectator, lines 127-129: HOLDS.**
   - The scalar difference rotation preserves Lebesgue measure and swaps at pi.
   - H_product = H_W H_m, and purities multiply.
   - The oscillator purity is tanh(u omega/2) with omega = 2 arsinh(sqrt(kappa)/2).
   - m_K n = l b^{-K} -> 0, so u omega -> 2 pi/512, and limsup P <= tanh(pi/512), about 0.0061, which
     is below 457/625.
   - So (2) fails, by contraposition of Jensen.
9. **Projected weak U(1), lines 131-150: HOLDS** (given row 1565 / check 1571 A2-A3, whose statements I
   re-read).
   - The coset bound sqrt(W_{j+1} W_{j-1}) >= d W_j is uniform over cosets, so it applies at D + jS.
     Here R = n/u = 512, V/n^4 = 1/512, and all periods are even (u = 2(l/1024) b^K).
   - Weights 1, 2, 1: f_{j+2} + f_{j-2} - 2f_j = Delta^2(j+1) + 2 Delta^2(j) + Delta^2(j-1) >= 8 log d,
     hence W_2 + W_{-2} >= 2 d^4 W_0.
   - The families with charge 0 and +-2 are disjoint and all even.
   - d_gamma -> 1 as A -> infinity. Positive-mixture lemma (6) holds at t = 1/gamma, and Tonelli
     applies.
   - lambda_0 sits in Q = 0: the eigenvalue is simple and positive, and flat translations preserve
     positivity.
   - sum p_i^2 <= max p_i then gives P_even <= 1/(1 + 2d^4) < 1/2.
   - The remark on projecting by the whole continuous centre is correct.
10. **Lemma 3 (thermal clock), lines 154-165: HOLDS.**
    - Cocycle, group law, w(R_{r+pi}X) = w(R_r X), Theta(pi) = pi and V_pi = S almost everywhere.
    - Invariance of w dX by orbit disintegration.
    - Each end, V_s X and V_t Y, has exactly the marginal rho x rho.
    - The separate monotone reparametrization leaves both the signed and the absolute mixed integrals
      unchanged (F_ab alpha' beta', no cross terms).
    - The overlap path has endpoints 1 and P_K, and the density ratio at (0, pi) is e^{-2J}.
    - Rank-one obstruction: vanishing 2x2 minors almost everywhere, then everywhere by continuity,
      then k factorizes.
11. **Pinned small-coupling comparison (4)-(5), lines 169-182: HOLDS** (given Theorem E (2.15), checked
    in 1572 Step 7; I verified the application line by line, not the Gibbs-coupling proof).
    - Each spatial link has exactly one inward temporal plaquette, with 3 free readers of Lipschitz
      constant at most beta. The left sum is at most 3N beta.
    - The right maximum is 2(d-1) beta: a temporal link sits in 2(d-1) slab plaquettes.
    - The tau-distance is at least v - 2, and DD^T = sum (r+1) C^r. Together these give (4).
    - Centre term: geodesics of length pi give ranges of at most pi M on each side, using
      K_v(x, C_z y) = K_v(C_z x, y). Then |Cov| <= ab/4 gives (5), and
      B_K <= (1/2) pi^2 . 2 sup = pi^2 (M + pi^2 M^2/4).
    - U(1) square circle: the coarea argument holds (|grad r| = 1), the antipode sits at half the
      perimeter, link speed is at most 2r/pi < 2, and the factor is 4.
    - Thresholds 2/9, 1/9 and 1/6 hold. N v q^{v-2} -> 0 at v = n/1024.
    - These hold only at fixed beta with q < 1, never on the calibrated trajectory, as the row states.
12. **Midpoint composition (6), lines 186-204: HOLDS.**
    - The covariance carry is exact (P_0^2 = P_0).
    - Cov = 2 <F^odd, G^odd> under the half-turn.
    - Parseval on odd frequencies (j^2 >= 1) with stationarity gives the bound.
    - The weight wbar^2/w_nu and the stated failure of the iteration are both correct.
13. **Spectral positivity, lines 208-221: HOLDS.**
    - Under product Haar ends h(s,t) has mean 0, and its law is the same at every (s,t) by the group
      law.
    - h = 0 almost everywhere would force J = 0 and P_K = 1. But T = MKM is injective on the neutral
      space, which has dimension at least 2, so P_K < 1. Hence h takes both signs at every (s,t).
    - ||R||^2 in L^2(pi_0 x pi_0) equals sum_{j>0} r_j^{2v} = s(u).
14. **5D free pair and SU(3) remark, lines 225-227: HOLDS.**
    - 5D pair: omega = 2 arsinh sin(pi/n) <= 2 pi/n, so uE <= 4 pi/512 < log 2 and the purity is below
      2/3, which is below 457/625. This is a free-field test only, as stated.
    - SU(3): for 0 < t < pi/3, {e^{it}, e^{it}, e^{-2it}} is not the multiset of the inverse.

Not checked:
- row 1215 (5) (test g5);
- Theorem DOB and the attributions in the repo-search section;
- the proofs inside PV, row 1565 and Theorem E beyond the statements used;
- the "check 1570 orbit-sign test" attribution.

## C. Equivalent is not progress

Nothing in the row is a sufficient condition strictly weaker than (PUR-io). Each candidate falls into
one of these groups:
- **Equivalent readouts at each K:** (1), H(pi) = P_K, the overlap path of Lemma 3, and Lemma 3's
  re-timed B_K (equal to B_K).
- **One-way stronger:** (2), and the signed form E_mu J = D(p||m) + D(m||p) <= log(625/457). Each
  implies P_K >= 457/625 at the same K by Jensen. The separation example shows both are strictly
  stronger on positive kernels.
- **Stronger still:** bounds on the right side of (6), and pinned contraction (small M), because each
  implies (2).

The only places where (2) is proved are fixed small beta (q < 1), off the calibrated trajectory
(beta_K -> infinity).

Same pattern in the earlier rows:
- Check 1527 (vi) found STIFF-TO-HELL a one-way stronger test, separated from purity by a positive
  kernel with purity 257/289.
- Row 1373's prefix affinities recover the exact seed threshold, an equivalent readout.

The present row adds a geometric way to measure the response, and selectivity passes in which (2) fails
on the gapless spectator and on weak 4D U(1). It adds no weaker sufficient statement. Strict separation
inside pure Wilson is unknown, as the row says (line 123).

## Defects (none breaks a statement)

1. Line 96: "only finitely many small K could have v < 2" is vacuous, since v >= b^K >= 3.
2. Line 117: the separation pattern (two eigenvalues 1 and 1/4, purity 257/289) duplicates check
   1527 (vi) without citing it.
3. Line 115: Lemma JI is cited as the same identity. The normalizations differ by JI's Delta
   convention. The row's (3) is proved directly and is correct.

RESULT — Row 1573 holds as written. Lemma 1 holds: the paired-link circle preserves product Haar
(SO(3) frame argument), is gauge and centre covariant, equals the swap at pi almost everywhere on a
null-complement regular set, and has speed at most sin(theta/2) <= 1. The regularity boundary holds and
correctly extends check 1123; it does not conflict with row 1529 section 3 or check 1539. The Q-orbit
circle, Lemma 2 (H(0) = 1, H(pi) = P_K, 0 < H <= 1), (1), the covariance form of the mixed derivative,
(3) (= I + L, Lemma JI in substance), the separation example (257/289, B_K -> infinity), the spectator
and projected-U(1) failures of (2), Lemma 3, the small-coupling bounds (4)-(5), the midpoint inequality
(6) and the sign result all hold. The defects are three minor wording or attribution points. Nothing in
the row is a sufficient condition strictly weaker than (PUR-io): (1) is equivalent, and (2) and its
signed form are strictly stronger on positive kernels, the same pattern as STIFF-TO-HELL in check
1527 (vi). (PUR-io) and the mass gap remain open.

Checked line by line by Claude (Opus 5.5).
