lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-28T16:30Z

# Cross-provider check of row 1661 (`library/gap-newmath-astra62-max3.md`)

Provenance: Claude Fable 5.2, high effort, Mac mini worker 1, pinned commit e5286638b. One reading by one model of another provider (the checked file was written by gpt-6.2-astra max). Not an audit and not human review. Queue row 1663.

Started 2026-11-28T04:30Z (date -u). No commit, claim or push from this machine; the relay copies this file.

Plan: read the whole checked file once, then give a verdict per claim in the order of the brief: 1. (30) and selectivity; 2. (37); 3. (38) / Stage 27; 4. (22), (28a), (29) and the zero count; 5. (34); 6. (39) / Stage 28; 7. the closing OPEN statement and the gap to the isotropic point. Each verdict is appended when reached.

## 0. Status log

- 2026-11-28T04:30Z: file created; reading the checked file.
- 04:31Z: read all 901 lines of the checked file (Stages 1-28). Next: look up the on-file inputs (rows 1468, 1553, 1145, 1143, 1227) and check claim 1.
- (log) inputs read for claim 1: FINISH rows 1661, 1553, 1556, 1468; `gap-k2-tool-design-fable.md` 3.1 (L99-L120); `gap-mech-direction4-fable.md` 1.4-1.5 (L180-L196); `gap-solve-astra62.md` (1) and its proof (L25-L45); RESULT lines of checks 1144, 1384, rows 1227, 1642.

## 1. Claim 1: formula (30) and its selectivity

Verdict: **the formula HOLDS; the selectivity claim HOLDS AFTER CORRECTION (it is selective in the sense "the three numbers differ", and it FAILS the tests (g1), (g3), (g5), (g6) of row 1553); the ordered limit is NOT a limit the consumer can use.**

### 1.1 What I redid (line anchors are of the checked file)

The first entry of (30) rests on (16)-(17) (Stage 13, L342-L387), (20)-(21) (L402-L410), the heat-trace limit (25)-(26) (Stage 17, L497-L533). The other two entries are Stage 20 (L653-L679). I recomputed each constant by hand. Status of my recomputation: ARGUED (a second derivation of the leading terms, not a new complete proof); the proofs are the checked file's.

1. Coordinates. The comb gauge and the triangular pivots are ON FILE (row 1143 (1), `gap-solve-astra62.md` L29-L41, checked by row 1144). I checked that the pivot face of a link (x, i) uses the first earlier coordinate j with x_j > 0, so it never wraps in both directions. So the seam field (wrapping i-links h_i, all else 1) has every pivot equal to 1, as L357 uses. Count: 3N links, N - 1 tree links, 3 windings, M = 2N - 2. Correct.
2. Magnetic exponent. For pure quaternions, log of the group commutator of exp(x), exp(y) is 2 x times y + O(3). With h_i = exp(X_i/sqrt(an)) the double-seam curvature is 2 (X_i x X_j)/(an), on the n faces with chi_i chi_j = 1. The source is closed (it depends on x_i, x_j only). Its mean is 1/n^2 of its seam value. Half the squared norm of the harmonic part, times s, is (n^3/2) (2 sqrt(s)/(a n^3))^2 |X_i x X_j|^2 = 2 gamma |X_i x X_j|^2 at s = gamma n^3 a^2. This is (18) and the display after it. Correct. The exact part is removed by a shift of the pivot Gaussian because range(dL) is the space of exact two-forms: dimensions 2N - 2 on both sides per colour, and a closed one-form that vanishes on the tree and on the three based wrapping edges is zero. Correct.
3. Electric exponent. The seam one-form chi_i (R Y_i - X_i)/sqrt(n), in units a^(-1/2), has harmonic part of squared norm |R Y_i - X_i|^2. So the kernel is (17). Correct. Error terms: pivots are O(1/a), seams O(a^(-1/2)), sqrt(s) = O_n(a); every mixed or cubic term times sqrt(s) is O_n(a^(-1/2)). Correct.
4. Tails. With r_i = sqrt(an) phi_i, row 1143's upper bound and the identity 1 - Re[h_i, h_j] = 2 sin^2 phi_i sin^2 phi_j |omega_i x omega_j|^2 give the radial bound C prod r_i^2 prod_(i != k) (1 + c r_k^2 r_i^2)^(-1) <= C' |r|^(-2). The electric bound for arbitrary slice fields is exp(-c_n |r - r'|^2): along a based line, |g h' g^(-1) - h| <= sum of the n link mismatches, so the constant is c_n of order 1/n^2. Fixed n only, as the file says at L379. The kernel exp(-c|x - y|^2) is Hilbert-Schmidt for |x|^(-2) d^3x (the displacement integral is C/|z|). Correct.
5. Dilation. X = gamma^(-1/6) Y turns (17) into e^(-hU) e^(h Delta/2) e^(-hU) on rotation invariants, h = gamma^(1/3). Correct. (21): m trial functions give lambda_m >= 1 - C_m h, the top eigenvalue is at most 1, and purity <= lambda_1^v / Tr S^v <= 1/(m (1 - C_m h)^v). Correct.
6. Heat trace. The arithmetic-geometric step at L515-L519 is exp(-2h sum_j U_j) = prod_j [exp(-t(U_j + U_(j+k)))]^(1/v) <= mean. Correct. The two-point majorant is the same radial bound. The limit object is H = -Delta/2 + 2U on invariants; its discrete spectrum and finite heat trace are ON FILE (row 1227 (4)-(8), `gap-solve25-astra62.md` L61-L93, check 1230). The purity of exp(-tH) increases strictly in t (its log-derivative is 2(E_t - E_2t) of the thermal mean energy). So q rises strictly from 0 to 1 and tau_* is unique. With gamma = kappa/n^3 and v = n/512, v h = kappa^(1/3)/512. Correct: first entry of (30).
7. Five dimensions (four spatial directions, N = n^4, M = 3(N - 1)). Scale h_i = exp(X_i/sqrt(a n^2)). Electric constant part: n^4/(n^2 n^2) = 1. Magnetic: (n^4/2)(2 sqrt(s)/(a n^2 n^2))^2 = 2 s/(a^2 n^4). So gamma_4 = kappa/n^4 and v h = kappa^(1/3) n^(-1/3)/512 -> 0. Radial weight w(r) <= C (1 + |r|)^(-4) on R^4. It is not integrable (a logarithm, the on-file log of row 1143 (2)), and it is square integrable, which is what the Hilbert-Schmidt bound needs at v >= 2. Correct: second entry.
8. Compact U(1), order-two flips. Plaquettes do not see the windings; the windings are Haar; a cycle of v slices keeps v - 1 Gaussian winding differences of width a^(-1/2) in d = 3 coordinates. So Z_+(v) is of order [slice constant]^v a^(-3(v-1)/2) and P is of order a^(-3/2) -> 0 at every fixed n, v. Correct: third entry. With the whole centre in the projector the kernel reads only the pivots, which move by s^(-1/2) = o(a^(-1/2)); rank one in the limit; purity 1. Correct.
9. Numbers in (14) (used by Stage 14 and later, not by (30)): Tr K = 4 pi sqrt(pi/2), ||f||^2 = 2 pi^(3/2), ratio sqrt 2; second term 1/72; 72 sqrt 2/73 - 1 < 2/5; (25/29)^2 = 625/841 > 457/625. Correct. The limit measure de d^3A/|A|^2 in (19): the Jacobian gamma^2 d^9X = r^(-2) dr de d^2A d^4w and the two transverse determinants |A|^2/r^2 give 1/|A|^2. Correct.

First failing step in the proof of (30): none found. Not rechecked by me: row 1143 (1) and row 1227 (4)-(8) (both have a check on file), and the Feynman-Kac identification at L522 beyond its outline.

### 1.2 The selectivity tests

What decides each entry (ARGUED, from the proof lines above):

- 4D SU(2) against 4D U(1): the commutator potential U = sum |X_i x X_j|^2 is not zero for su(2) and is zero for u(1). So the unprojected winding modes are bound for SU(2) and free for U(1). This is the Lie algebra. Which winding modes are unprojected is the centre convention: with the centre of U(1) (the whole group) in the projector, the U(1) entry is 1, which is >= 457/625.
- 4D against 5D: the one exponent in v h = kappa^(1/3) n^(1 - d/3)/512, d the number of spatial directions. It comes from the volume factor n^d in the harmonic projection. This is the dimension. With s = kappa n a^2 in five dimensions the same proof gives gamma_4 = kappa/n^3 and a five-dimensional entry q_4(kappa^(1/3)/512), which passes for large kappa. So the sign in the 5D entry is a power of n in the chosen magnetic scale.
- The 4D SU(2) entry changes sign with kappa. kappa sets the thermal time of the constant-mode Hamiltonian H against its level spacing. Any Hamiltonian with discrete spectrum and a simple ground state has this crossing. It is a property of an anisotropy parameter of the lattice, not of the Wilson law at a fixed physical size.

Tests of row 1553 (`gap-mech-direction4-fable.md` L188-L193), with F = "the ordered-limit purity is at least 457/625":

- **(g1) FAILS in the consumer's own convention.** The consumer's projector P_0 is on the centre-neutral states (row 1468 3.1). The centre of U(1) is U(1). With that projector the file's own table gives 1 for weak 4D U(1) (L651, proof L679). So F holds in a massless model. F is false for U(1) only with the order-two projector, where the failing line is "the flat winding torus carries free translation modes" (L672-L677).
- **(g2) passes formally**, at the line "v h -> 0 at d = 4" (L668).
- **(g3) FAILS.** The U(1) line fires in the gapped twin 3D compact U(1): the abelian proof at L670-L677 is written for general d and gives P of order a^(-d/2) -> 0 at d = 2 (the file says the same for the iterated limit at L323). The 5D line is a power count with no coupling left in it, because a went to infinity first; it cannot tell a gapped member from a gapless one. Also, the 4D SU(2) entry itself is 0 for small kappa, in a family whose members are all 4D SU(2) Wilson laws.
- **(g4) not informative.** Purities multiply under products, so the product with a factor of ordered-limit purity 0 gives 0, and the product with weak 4D U(1) under its full centre gives q: a model with a massless factor passes F. This is the Lemma ALG situation in the consumer's convention.
- **(g5) FAILS by construction.** The inner limit is a -> infinity on a fixed lattice. The box has physical size zero. Row 1553 asks that the hypothesis fail when the coupling grows on a fixed lattice; here the statement lives only there.
- **(g6) FAILS.** No consumer, no carry. The file says so at L681.

Answer to the brief's question: the difference in (30) is a property of the centre convention, of the Lie algebra (U not zero) and of the dimension (the exponent 1 - d/3). No line of the proof reads the law at a fixed physical size. By Lemma ALG and (g1) it is not an input.

ON FILE, to be credited: the constant-mode quartic Hamiltonian on a small torus is the small-volume Hamiltonian of Luescher (and Koller and van Baal), named in the lane at `gap-solve25-astra62.md` L99 and `gap-direction8-astra62-check-opus.md` L99; row 1227 has its one-vertex spectrum. What Stage 13 adds is a derivation on the full n^3 cube in an anisotropic joint limit, with the exact discrete-time kernel (17). I found no earlier lane text with (17) on the full cube (grep of "sinh", "K_gamma", "gamma n^3" in library/open-core.md and FINISH.md: see Section 8). The file does not name Luescher at Stages 13-17; it should.

### 1.3 Can the consumer use the ordered limit?

No. Three separate reasons, each enough.

1. Ratio. (PUR-io) is at s = a = beta_K. The limit is at s = kappa a^2, so s/a -> infinity.
2. Order and rate. (PUR-io) has a = beta_K of order log n on n = l b^K. The limit needs a -> infinity at fixed n. The constants of Stage 13 (c_n of order 1/n^2, C_n from row 1143 with Q = n^2) give no rate; the windings are concentrated at angle (an)^(-1/2) in the limit and are Haar on the calibrated sequence (file L440, L533; row 1145). So the two regimes are separated by an observable, not only by a missing estimate.
3. At the consumer's ratio the same ordered limit gives the wrong side for 4D SU(2) itself: (15) (L331-L336) gives P of order a^(-3/2)/log a -> 0 at s = a for fixed n, v >= 3, and (21) with gamma = 1/(beta_K n^3) gives 0 (L434). So at s = a the ordered limit gives 0 for all three models.

The checked file states 1-3 itself (L434, L440, L681). Its RESULT line "In the ordered weak limit (30), 4D SU(2) passes the threshold" is true and is not progress on the seed.

### 1.4 Required corrections for claim 1

- C1. L651 and L900: replace "selective" and "law-dependent" by the facts of 1.2: with the consumer's projector, weak 4D U(1) passes; the 5D entry is a power of n; the statement lives at physical size zero.
- C2. L311 and L651: "the strict intermediate value still fails" is true and is not a test. The consumer reads only P >= 457/625.
- C3. Stages 13-17: credit Luescher's small-volume Hamiltonian and row 1227.

- 04:36Z: Section 1 (claim 1) written. Next: claim 2, formula (37).
