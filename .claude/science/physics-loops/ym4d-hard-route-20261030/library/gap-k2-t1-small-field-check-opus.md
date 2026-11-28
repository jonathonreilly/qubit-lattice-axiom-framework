lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T03:38Z

# Check of row 1472 (`library/gap-k2-t1-small-field-astra62.md`)

Row 1478. Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, commit 490b37e88, started 2026-11-24T15:38Z (date -u). Cross-provider check of a gpt-6.2-astra max output. Not an audit. Written arguments, no Lean.

## Plan

1. Read `gap-k2-t1-small-field-astra62.md` in full, and `gap-k2-tool-design-fable.md` 3.2 (the 384-contour definition of Q2).
2. Test the two period-two fields: does every Q2 contour equal the identity on them.
3. Singleton condition and floors 2,560,000, 20,000, 12,500.
4. Hot-block majorant and KP count (320^(m-1), 81 blocks, x >= 64 or 96).
5. Log-cosh pairing bound 72 h^6/x.
6. Conditioned Gaussian quartic bound 15/x.
7. Verdict: HOLDS / HOLDS AFTER CORRECTION / FAILS at first wrong line.

## Repo search

Searched: `grep -n` of `library/open-core.md` and FINISH rows 1468-1480 for `period-two`, `three-face`, `cubic`, `15/x`, `72 h`; the only hits are rows 1472 and 1478-1480 themselves (the claims under check). No earlier check of row 1472 is on file. Sources read in full: the row 1472 file (169 lines), `gap-k2-tool-design-fable.md` 3.2 (lines 126-188), and `gap-k2-floor-sizing-opus.md` Step 5 (lines 156-185, the estimate that row 1472 makes concrete).

## Step 1. The two period-two fields against the 384-contour definition (hand check)

Q2 (row 1468 3.2): contour of e = (xi, pi), xi in {0,1}^4, pi a permutation: axis path 2y -> 2y + xi in order pi, two mu-steps, then the reverse of the path 2y + 2e_mu -> 2y + 2e_mu + xi taken in the same order. M_c = (1/384) sum of the 384 holonomies. Row 1472 describes the same contour ("offset path, two steps, inverse of the translated offset path"). Faithful.

**Field 1 (noncommuting, three faces).** HOLDS. Restated proof: the assignment W(x, nu) = h(edge {n, n+e_nu})^(+1 or -1), n = x mod 2, sign by the bit n_nu, is the pull-back of a connection on the 1-skeleton of the unit 4-cube under the map x -> x mod 2. Every lattice path's holonomy is the holonomy of its image path in the cube graph. The image of a Q2 contour is P . (xi -> xi+e_mu -> xi) . P^(-1), with P the image of the offset path (translation by 2e_mu fixes parities), and the middle backtrack has product h^(-1)h or h h^(-1). So every one of the 384 holonomies is 1, for all labels, including xi_mu = 1 and every order pi. Each fine plaquette maps onto a 2-face of the cube; 16 sites x 6 planes = 96 = 24 faces x 4 base vertices, so each face is seen by 4 assigned plaquettes per block, from different corners and possibly with reversed orientation (conjugate or inverse holonomy, same real part).
Selected faces: boundary from (n3,n4) = (0,0), first in direction 3. Oriented labels e^(It), e^(Jt), e^(Kt), 1 give holonomy e^(It)e^(Jt)e^(Kt); its real part is c^3 + c s^2 Re(IJ + IK + JK) + s^3 Re(IJK) = cos^3 t - sin^3 t (IJ = K, IK = -J, JK = I, IJK = -1). Checked the other faces: a (k,3) or (k,4) face, k in {1,2}, contains two marked parallel edges with equal labels (holonomy 1) or one marked edge and one identity edge (real part cos t); (1,2) faces and the (3,4) face at (0,0) are flat. So the odd part of S_B is exactly 12 x sin^3 t. Block tree in decreasing axis order: a nu-edge of the tree has all lower coordinates 0, and every marked edge (directions 3, 4) has (n1,n2) != (0,0); tree links are the identity. Link logarithms are +-It, +-Jt, +-Kt, linear in t. HOLDS.

**Field 2 (commuting, Cartan).** HOLDS. A_mu(n) = (-1)^(n_mu) c_mu(n), c_mu = number of odd n_i with i < mu; c_mu does not depend on n_mu. Contour: the two offset legs are translates by 2e_mu (period two) traversed oppositely, so they cancel (abelian); the middle pair gives A_mu(m) + A_mu(m+e_mu) = 0. So M_c = 1 for every c, t, xi, pi. Plaquette (i,mu), i < mu: A_i does not depend on n_mu, and A_mu(n+e_i) - A_mu(n) = (-1)^(n_mu)(-1)^(n_i); angle t(-1)^(n_i+n_mu), so all 96 plaquettes of a block have real part cos t, S_B = 96x(1 - cos t). Tree mu-edges have c_mu = 0. HOLDS.

An independent computational check of both fields on the actual lattice (all 384 contours, all plaquettes) is Step 2.

## Step 2. Computational cross-check: DEFERRED

Before 2026-11-24T15:42Z `memory_pressure` reported 37 percent free, below the 50 percent rule for numeric jobs on this machine. No job was started. Rechecked later (see the end of this file). The hand proof of Step 1 does not depend on it.

## Step 3. Singleton condition and the three floors

**Model faithfulness.** Row 1470 Step 5 states (F1) and (F2) only as guesses ("z e mu <= 1 roughly", "z = c1/x"). Row 1472 makes them concrete as a sup-norm (pointwise) KP test on block activities e^(-R_B) - 1 (cold) and e^(-S_B) (hot), with star-touching incompatibility. That is a legitimate concretisation and the file labels it POINTWISE throughout; the floors are floors of that estimate, not of Q2 (the file says so in its last Open paragraph). HOLDS as scoped.

**Singleton condition.** HOLDS. KP: for each polymer P, sum over P' incompatible with P of |z(P')| e^(a(P')) <= a(P). For P = {B} with least weight a_min, the 81 = 3^4 singletons of the closed star (B included, self-incompatible) all carry the same majorant z (uniform sup), so 81 z e^(a_min) <= a_min, and u e^(-u) <= 1/e gives z <= z_* = 1/(81e). Dropping all other polymers only weakens the left side, so the condition is necessary for this test. For the cold majorant with optimised constant, 1 - z_* <= e^(-R_B) <= 1 + z_* on the cold region, so osc R_B <= L_* = log((1+z_*)/(1-z_*)) = 2 artanh z_*. Arithmetic: 81e - 1 > 81(65/24) - 1 = 218.375, so L_* < 2/218 = 1/109. HOLDS.
Hot majorant: S_B >= x(1 - Re U_p) = x |U_p - 1|^2/2 >= x s^2/2 for the hot witness; the equality example is right: the link (2e_i, mu), i != mu, lies in plaquettes based at 2e_i (any plane) and at 2e_i - e_j (plane (j, mu)); only 2e_i - e_i = e_i is in B = {0,1}^4, so exactly one assigned plaquette changes, with chord s. So z_H = e^(-x s^2/2) and the singleton condition gives x s^2 >= 2 log(81 e) = 2 + 8 log 3. log 3 = 2 artanh(1/2) > 1 + 1/12 + 1/80 gives 2 + 8 log 3 > 10.766 > 43/4 > 9, and 2 + 4 log 3 > 6.383 > 19/3. HOLDS.

**Odd residual.** HOLDS. On field 1 the Haar density and the pin are even (pin constant), every link log is linear in t, so any polynomial of degree <= 2 in link logs contributes only b t to the odd part: r_o = 12 x sin^3 t - b t, and |r_o| <= O/2. Then r_o(T) - 2 r_o(T/2) = 12x[sin^3 T - 2 sin^3(T/2)] has absolute value <= 3O/2, so O >= 8x[...]. sin T >= T(1 - T^2/6) >= (23/24) T > (15/16) T for T <= 1/2; (15/16)^3 = 3375/4096 > 13/16 = 3328/4096; 2 sin^3(T/2) <= T^3/4. So O > 8x(9/16)T^3 = (9/2) x T^3. HOLDS.
Chords on field 1: |U - 1|^2 = 2(1 - Re U). Selected faces: 2(1 - cos^3 t + sin^3 t) <= 2(3t^2/2 + |t|^3) = (3 + 2|t|) t^2, using (1 - t^2/2)^3 >= 1 - 3t^2/2 (Bernoulli, 1 - t^2/2 >= 0). Faces with real part cos t: chord^2 = 2(1 - cos t) <= t^2. HOLDS.

**Floor 2,560,000.** HOLDS. T = 3/(2 sqrt x) = 3/3200 < 1/2. Max chord^2 < 4T^2, so chord < 2T = 3/sqrt x, while the hot condition forces s >= sqrt(2 log(81e)/x) > 3/sqrt x: every t in [-T, T] is cold, for every admissible s. O >= (9/2) x T^3 = 243/(16 sqrt x) = 243/25,600; 243 * 109 = 26,487 > 25,600, so O > 1/109 > L_*. Contradiction at x = 2,560,000, hence any uniform floor of this test exceeds 2,560,000. HOLDS.
Remark (not a defect): the same inequality fails for every x with tanh(243/(32 sqrt x)) > 1/(81e), i.e. up to about x = 2.8e6 (sqrt x < 243 * 81e/32, about 1672), and passes beyond: 2,560,000 is a valid lower bound, not the exact threshold of this test. The "no finite c1" clause: with the same T for all large x, z_S >= tanh(O/2) >= tanh(243/(32 sqrt x)) (optimal constant: R in an interval of length O gives best sup|e^(-R) - 1| = tanh(O/2)); so x z_S -> infinity and no c1 with z_S <= c1/x exists. HOLDS.

**Floor 20,000 (face neighbours, D = 1 + 8 = 9).** HOLDS. T = 1/100, x T^2 = 2; x chord^2 <= 2(3 + 2/100) = 6.04 < 19/3 < 2 log(9e); all cold. O >= (9/2)(20,000)(10^-6) = 9/100. L_*(D=9) = log((9e+1)/(9e-1)) < 2/(9e - 1) < 2/23 < 9/100 using e > 8/3. HOLDS.

**Floor 12,500 (field 2, cubic subtraction allowed).** HOLDS. Symmetrising a degree-<=3 subtraction at +-t removes its odd part and keeps the even residual in the convex hull of residual values, so its oscillation does not grow; what is left is b + q y, y = t^2. The three-point combination at y = 0, T^2/2, T^2 annihilates every affine function of y, so O >= H = 96x[(1 - cos(T/sqrt2)) - (1/2)(1 - cos T)]. With 1 - cos v >= v^2/2 - v^4/24 and 1 - cos T <= T^2/2 - T^4/24 + T^6/720: H >= 96x[T^4/96 - T^6/1440] = x T^4 (1 - T^2/15). HOLDS. Concavity: f''(y) = 24x(t cos t - sin t)/t^3 <= 0. HOLDS.
At x = 12,500, T^2 = 43/(4x) = 43/50,000 < 2 log(81e)/x <= s^2, so all of [-T, T] is cold (field-2 chords are 2 sin(|t|/2) <= |t|). H >= (1849/(16x))(1 - T^2/15) with 1 - T^2/15 > 999/1000; (1849/16)(999/1000) = 115.447 > 115; 115 * 109 = 12,535 > 12,500, so H > 1/109 > L_*. HOLDS.
Haar: one-link density (sin u/u)^2 in exponential coordinates (radial S^3 metric du^2 + sin^2 u dOmega^2). |g(u) - u^2/3| <= u^4/30 for |u| <= 1/2: upper tail v^2/(1-v) with v = u^2/6 <= 1/24 gives u^4/34.5; lower bound u^2/3 - u^4/60 from the sine upper bound. Here |u| = |t A_e| <= 3T < 0.09. Fourth-power sums of A over the 64 block links: 0, 8, 4(2 + 16) = 72, 2(3 + 48 + 81) = 264, total 344 (recounted: mu = 3, (n1,n2) has one odd coordinate for 2 of 4 values and two for 1 of 4; mu = 4, n1..n3 has one odd for 3 of 8, two for 3, three for 1). Height change <= (344/30)(T^4/4 + T^4/2) = 8.6 T^4 < 9T^4; 9/x = 0.00072, so x T^4(1 - T^2/15 - 9/x) > (1849/(16x))(999/1000) > 115/x. HOLDS.
c1 pricing liminf x z_S >= 2 log^2(81e) (about 58.2): from H ~ 4 log^2(81e)/x and z_S >= tanh(H/2). HOLDS. Taylor discrepancy 96x(T^2/2 - 1 + cos T) ~ 4 x T^4 = 4h^4/x at T = h/sqrt x. HOLDS.

## Step 4. Hot-block majorant and the KP count

HOLDS. Assigned plaquette sets of distinct blocks are disjoint, and every summand of S_B is nonnegative, so m hot blocks have assigned weight at most e^(-m x s^2/2), and the same bound holds for the integral of the product of indicators times weights against any probability measure. Count: a star-connected set of m blocks containing a fixed block is recovered from a rooted ordered spanning tree (fixed deterministic rule), whose shape is a plane tree with m vertices (Catalan number C_(m-1) <= 4^(m-1), parenthesis word of length 2(m-1)) and whose m - 1 edges each carry one of 3^4 - 1 = 80 star directions; the map is injective, so at most 320^(m-1). KP with a(P) = |P|: an incompatible P' meets the closed star of P, which has at most 81|P| blocks, so the left side is at most 81|P| sum_m 320^(m-1)(ez)^m = 81|P| e z/(1 - 320 e z) <= |P| iff 401 e z <= 1. At s = 1/2, z = e^(-x/8): x >= 8(1 + log 401) (about 55.9); x = 64 works since e^7 > (5/2)^7 = 610.4 > 401. With labels z = 96 e^(-x/8): x >= 8(1 + log 38,496) (about 92.5); x = 96 works since (8/3)^5 = 32768/243 > 128 gives e^11 > 128^2 (8/3) > 43,690 > 96 * 401 = 38,496. HOLDS. The file correctly withholds any claim about normalisation, boundary interactions or mixed polymers.

## Step 5. The log-cosh pairing bound 72 h^6/x

HOLDS. With an even reference, the mean of e^(-R_e - R_o) and e^(-R_e + R_o) is e^(-R_e) cosh R_o; 0 <= log cosh u <= u^2/2 (integrate 0 <= tanh u <= u). On field 1, R_o = 12 x sin^3 t; for |t| <= h/sqrt x, R_o^2/2 <= 72 x^2 t^6 <= 72 h^6/x. HOLDS. Scope as stated: it is a statement on the one-parameter test, where t -> -t is linkwise inversion W_e -> W_e^(-1). That map keeps Haar measure but not M_c in general; on field 1 both signs give M_c = 1. The file claims no more.

## Step 6. The conditioned Gaussian quartic bound 15/x

HOLDS. Normalisation matches the rest of the file: Re U_p = cos|F_p| with F_p in R^3, so x(1 - Re U_p) = (x/2)|F_p|^2 + ..., and the linearised measure on (ker d)^perp per colour has density proportional to exp(-(x/2)||dA||^2); the covariance of F = dA is x^(-1) d(d*d)^(-1)d* = x^(-1) P_(ran d). rank d on 1-forms on a torus of N sites is 4N - (N - 1) - 4 = 3(N - 1) (closed = exact + harmonic), equal to the per-momentum count (rank 3 at k != 0, 0 at k = 0). On an equal-sided torus hypercubic symmetry makes the diagonal constant over the 6N plaquettes: 3(N-1)/(6N x) < 1/(2x). Conditioning a centred Gaussian on a linear observation (with independent noise) at Y = 0 keeps it centred and lowers the covariance in PSD order, so v_p <= 1/(2x); colours stay iid. E|F|^4 = 3*3v^2 + 6v^2 = 15v^2. So E[(x/24) sum_(p in B) |F_p|^4 | Y = 0] <= (x/24) * 96 * 15/(4x^2) = 15/x. HOLDS, as a bound on the mean of the linearised quartic only; the file lists the omitted terms (commutators, cubic insertions, pin response, external field) and draws no lower-bound conclusion from it.

## Step 7. The bond-kernel domain (cut 1/2 and tube), checked as well

HOLDS. Chord 1/2 gives cos alpha = 1 - 1/8 = 7/8 > sqrt3/2, so 6 alpha < pi. A transverse offset bit nu turns the straight pair into a 1 x 2 rectangle, two plaquettes, so angle <= 2 alpha by the bi-invariant triangle inequality; a xi_mu bit costs nothing (checked for both orders of a mu and a nu bit: the path reduces to the transverse-only contour). The j-distribution over the 16 offsets is C(3, j)/8; Re(hol S^(-1)) >= cos(2 j alpha) since 2 j alpha <= 6 alpha < pi. Sum = Re[((1 + e^(2 i alpha))/2)^3] = cos^3 alpha cos 3 alpha = (343/512)(4 * 343/512 - 21/8) = (343/512)(7/128) = 2401/65536 > 1/32. Tube: at most 10 links per contour (4 + 2 + 4); telescoping about unitaries gives ||M - M_0|| <= e^(10 eps) - 1 = 1/128; ||M_0^(-1)|| <= 32; |det(1 + E) - 1| <= |tr E| + |det E| <= 2/4 + 1/16 = 9/16; so Re det M > 0. F(w) = integral of e^(w q_0) over S^3 (= 2 I_1(w)/w) vanishes only at w^2 < 0; the radial-ODE proof given is correct (f not identically 0 as f(0) = 1). Since F is even and entire, F(kappa sqrt(det M)) is a holomorphic function of det M, zero-free where Re det M > 0. HOLDS.

## Step 8. Scope notes (no defect; they bound what the floors mean)

1. **Variables of the subtraction.** The floors 2,560,000 and 20,000 use field 1's odd part, which survives every polynomial of degree <= 2 in fine LINK logarithms. It does not survive a quadratic in PLAQUETTE angles: on a selected face 1 - cos theta = 3t^2/2 + t^3 + O(t^4), so q theta^2 has an odd t^3 part, and after the subtraction x theta^2/2 the odd residual is of order x t^5, which is order x^(-3/2) at t ~ x^(-1/2). Row 1472 flags this ("Retaining the full Wilson plaquette term in the reference would change this estimate"). The floor 12,500 is robust to this choice: on field 2 every plaquette angle is +-t and every link log is linear in t, so any polynomial of degree <= 3 in either set of variables restricts to a cubic in t, and the three-point height bound applies unchanged (Haar included). So the variable-independent pointwise floor on file is X > 12,500, not 2,560,000.
2. **Plaquette assignment.** On period-two fields every block carries the same configuration, so any block-translation-covariant assignment of plaquettes to blocks gives each block 1/(number of blocks) of the total; the odd part 12x sin^3 t and the even part 96x(1 - cos t) per block do not depend on the assignment rule. The floors therefore do not depend on the "based at a block site" convention.
3. **Threshold versus bound.** 2,560,000 is a valid lower bound; the star test of field 1 fails for all x up to about 2.8e6. Not a correction, the file only claims X > 2,560,000.
4. **What is not concluded.** Every floor is a floor of the pointwise (sup before integration) KP estimate with these majorants. No lower bound on the floor of Q2 itself, or of an integrated estimate, follows; row 1472 says this in its Open paragraph. Row 1480 (integrated activities) is the right next test.

## Verdict

**HOLDS.** Every item named in row 1478 checks line by line, by independent hand derivation:

- both period-two fields have all 384 Q2 contour holonomies equal to 1 (field 1 via the cube-graph pull-back, for any labels; field 2 by abelian cancellation), with the stated plaquette values, odd part 12x sin^3 t and even action 96x(1 - cos t);
- the singleton condition z <= 1/(81e), L_* < 1/109, x s^2 >= 2 log(81e) > 43/4;
- the floors X > 2,560,000 (star), X > 20,000 (face neighbours) and X > 12,500 (cubic subtraction, Haar included);
- the hot majorant e^(-m x s^2/2), the count 320^(m-1), 81|P| blocks, z <= 1/(401e), x >= 64 (96 with labels);
- 72 h^6/x and 15/x as scoped;
- also the bond cut 1/2 (2401/65536 > 1/32) and the tube with Re det M > 0.

No repair needed. Scope note 1 matters for consumers: only X > 12,500 is independent of whether the Gaussian subtraction is written in link logarithms or plaquette angles.

Not verified: the computational cross-check of Step 2 (memory free 37, 39 and 38 percent at 15:42Z, 15:43Z and 15:44Z, below the 50 percent rule; no job started, all checks done by hand), the repo-search paragraphs of row 1472, and the Sussman-Alpoge outline line citations in its last paragraphs (not on the proof path of any checked item).

Credit: Tadeusz Balaban (small-field and large-field block renormalisation), Kotecky and Preiss (activity criterion), Ethan Sussman and Levent Alpoge, with Claude and Codex (outline, complete account, the normalised contour kernel behind Q2); row 1472 (Codex, gpt-6.2-astra) for every argument checked here; row 1468 (Q2 definition) and row 1470 (the estimate made concrete).

## Next rows (unchanged from row 1472)

Row 1480 (integrated activities) and row 1479 (signed readout) stand as queued; this check gives them no new input beyond scope note 1: an integrated test should state which variables its Gaussian reference uses, since the odd field-1 obstruction is tied to link logarithms and the field-2 quartic is not.
