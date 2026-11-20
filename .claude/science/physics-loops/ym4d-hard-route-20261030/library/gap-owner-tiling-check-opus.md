lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:40Z

# Check of row 1286 (gap-owner-tiling-astra62): cross-provider, line by line

Queue row 1287. Checker: Claude Opus 5.5 max, Mac mini Claude worker 2. Started 2026-11-20T14:40Z (date -u).
Branch claude/ym4d-hard-route, pinned at a725fa855.
Target of the check: `library/gap-owner-tiling-astra62.md` (gpt-6.2-astra max, row 1286).
Background read against: rows 1273 and 1279 and their notes.

Process: each statement gets HOLDS, HOLDS AFTER CORRECTION, or FAILS, with the line.
Labels in this file: PROVED, ARGUED, GUIDE, OPEN. No numeric run is a proof step.

## Plan (at most eight steps)

1. Read the target note in full; list its claims with line numbers; read rows 1273 and 1279 and their notes.
2. Check the tree-sewing gap kappa_r g^(2/3)/(N l) for N^3 reduced blocks with dynamical frames; decide whether it is uniform in N.
3. Check the cyclic adjoint sewing count (12): at least 3N^3 soft centre-neutral excitations.
4. Check the Wilson-law bound (7).
5. Check every other statement of the note, against rows 1273 and 1279.
6. Say plainly what this means for the owner's tiling question.
7. Verdict table and RESULT line.

## Step log

(Steps are appended below as they finish.)

### Step 1. What the note claims (line numbers of `gap-owner-tiling-astra62.md` at a725fa855)

Read in full: the note (209 lines); row 1273's note, Lemma S and S_n (`gap-owner-threeaxis-opus.md` 324-395); check 1279 (`gap-threeaxis-check-astra.md`, all 123 lines); FINISH rows 1273, 1279, 1286, 1287.

Claims labelled PROVED by the author, grouped as the row asks:

- **Tree sewing (row's first claim).** (3) at 60-65 (common-frame constrained array); (4) at 67-72 (stiff springs, fixed graph, gap -> M^(-1/3) kappa_r in units g^(2/3)/l); (5) at 74-83; (6) at 85-91; spectral limit, upper and lower bounds 93-95; the "fixed fraction fails" corollary 97; thermal opposite answers 99-101; the tree with dynamical links and Gauss law 172-176.
- **Cyclic adjoint sewing (row's second claim).** (8)-(9)-(10) at 136-168 (ground energy and loop holonomy bounds); (11) at 153-159 (heat-kernel walk inequality); (12) at 178-191 (3M soft neutral levels); thermal consequence 193-197; the Wilson Hessian example at 170.
- **Wilson law (row's third claim).** Commutator mean 3/4 at 15; bond colouring 19-21; conditional density (1) at 23-27; low-energy bound (2) at 30-46; cutoff scope 48; trace sandwich (7) at 107-124; J > 0 at 126; comparison operators with the same O-histories 201-205.
- **OPEN and GUIDE.** 11, 128, 207 (OPEN); 3-9, 17, 52, 103, 130, 134 (GUIDE).

Background fixed by check 1279 (HOLDS there): Lemma S_n, K_n >= sqrt((n-1)/2) sum_i |y_i|, discrete singlet spectrum, gap kappa_n g^(2/3)/L, n >= 2. The note's r is row 1273's n (number of colour vectors per block).

### Step 2. Tree sewing: (3)-(6), the limit (4), lines 97-101 and 172-176

Units: K_r = (-Delta + V)/2 on R^(3r), d = 3r; one block l H_1 = g^2(-Delta_c/2) + V(c)/(2g^2), and c = g^(2/3) y gives l H_1 = g^(2/3) K_r. This is row 1273's H_g with n = r.

**(3), lines 60-65: HOLDS.** On c_x = c the induced metric is sum_x |dc_x|^2 = M |dc|^2, so Q = sqrt(M) c has metric dQ^2. V has degree 4, so sum_x V(c_x) = M V(Q/sqrt M) = V(Q)/M. With Q = lambda q, kinetic and quartic coefficients agree when lambda^6 = g^4 M; the common factor is g^(2/3) M^(-1/3). So the gap is kappa_r g^(2/3)/(l M^(1/3)) = kappa_r g^(2/3)/L. This is the one-block model of side L = N l at the same coupling g. The note itself marks the constrained model as a separate model (measure-zero submanifold). Correct.

**Spring units, line 67: HOLDS.** With c_x = g^(2/3) y_x, the edge energy sigma |c_x - c_y|^2/(2 g^2 l) becomes (g^(2/3)/l)(t/2)|y_x - y_y|^2 with t = sigma g^(-4/3). So only t enters, and g -> 0 at fixed sigma is t -> infinity.

**(5), lines 74-83: HOLDS** (typo: "qquad" for "\qquad" in line 81). Q = M^(-1/2) sum_x y_x is an orthonormal coordinate. The relative part in w_x = y_x - Q/sqrt M has kinetic -Delta_w/2 and spring (t/2) w^T (Lap ⊗ I_d) w. With z = t^(1/4) w (unitary dilation) it is sqrt(t) F_perp. F_perp is a harmonic oscillator on {sum z_x = 0} with frequencies sqrt(lambda_k), k >= 2, each d times. So e_* = (d/2) sum_(k>=2) sqrt(lambda_k), gap gamma = sqrt(lambda_2) > 0 (connected graph), Gaussian ground vector phi invariant under simultaneous rotation. W_t is as written since y_x = Q/sqrt M + t^(-1/4) z_x.

**(6), lines 85-91: HOLDS.** Dilation: with y = b^(1/3) w, (-b^2 Delta_y + V(y))/2 = b^(4/3) K_r(w) >= b^(4/3) s_r sum|w_i| = b s_r sum|y_i| (Lemma S_n, checked in 1279). At fixed z, the x-th share -Delta_Q/(2M) + V(Q/sqrt M + t^(-1/4) z_x)/2 is, in y = Q/sqrt M + t^(-1/4) z_x, the operator with b^2 = 1/M^2. Summing over x and using the triangle inequality with sum_x z_x = 0 gives sum_x |Q_i/sqrt M + t^(-1/4) z_(x,i)| >= sqrt(M) |Q_i|. Fubini over z gives the form inequality.

**Upper and lower bounds, lines 93-95: HOLD.** Trials v(Q) phi(z) are singlets when v is, since phi is rotation invariant. Their (5)-energy is <v, -Delta_Q v>/2 + <W_t>, and <W_t> -> <v, V(Q) v>/(2M) by finite Gaussian moments and compact support of v. Lower bound: the three terms of (5) are nonnegative. So bounded energy gives: bounded Q-gradient; ||(1 - P_phi) u_t||^2 <= C/(gamma sqrt t), since F_perp - e_* >= gamma (1 - P_phi); tail mass beyond |Q| = R at most C sqrt(M)/(s_r R) by (6) and sum_i|Q_i| >= |Q|. Rellich on v_t = <phi, u_t> plus the tail gives strong convergence u_t -> v phi with ||v|| = 1. The Q-Dirichlet form is weakly lower semicontinuous. W_t >= 0 converges uniformly on compacts, so exhaustion gives liminf <W_t> >= <V/(2M)>. The k-vector min-max step is the standard one and is correctly stated. K_c is unitarily M^(-1/3) K_r by Q = M^(1/6) q. Subtracting the first two singlet levels removes sqrt(t) e_*. So (4) holds for every fixed connected graph, and the limit does not depend on the graph.

**Line 97: HOLDS.** For a fraction b > 0 take N > 1/b; (4) at M = N^3 gives a gap below b kappa_r g^(2/3)/l at large finite t. No limit interchange is used.

**Lines 99-101: HOLD.** Independent blocks: the simultaneous-singlet subspace reduces H, the product vacuum is a singlet, so the normalized singlet trace is at most the full product trace (1 + s(v))^M, v = N g^(2/3)/512 the dimensionless time of L/512. 2K_r >= -Delta/2 + s_r sum|y_i| gives a finite heat trace; s(v) <= s(1) e^(-(v-1) d_r) for v >= 1; so N^3 s(v) -> 0. Stiff array at the same N, g, l, r: the singlet gap tends to kappa_r g^(2/3)/L, so one level contributes exp(-kappa_r g^(2/3)/512) > 1/2 exactly when kappa_r g^(2/3) < 512 log 2. Small positive t: levels are nondecreasing in t (spring >= 0) and converge as t -> 0 by fixed trials; mu_1(t) is bounded, so e^(-tau(mu_k(t) - mu_1(t))) <= C e^(-tau mu_k(0)), summable; dominated convergence keeps the strict pass. The logical conclusion (one-block theorem plus a positive joining interaction does not decide the thermal test) holds.

**Lines 172-176, tree with dynamical links: HOLD.** On a tree, every invariant psi(y, U) equals f(Ad(P_x) y_x) with P_x the transport to the root, f invariant under SO(3) at the root; the map is unitary, since Ad(P_x) preserves Lebesgue measure and Haar is normalized. If x is the parent of y then Ad(P_x) R_xy y_y = Ad(P_y) y_y, so the spring becomes |y~_x - y~_y|^2 and alpha = 0 gives K_t of (5) on the tree. Varying U_e rotates all y~_x below e together about the axes Ad(P_c) e_a; the sum of squares over an orthonormal frame is frame free, so the electric form is alpha sum_e |J_e f|^2 >= 0. On trials v phi: y x grad_y = (Q/sqrt M) x (M^(-1/2) grad_Q + t^(1/4) grad_z) + t^(-1/4) z x (...), so ||J_e (v phi)||^2 <= C(1 + sqrt t); with alpha = g^(4/3)/2 = sigma/(2t) this is O(t^(-1/2)) -> 0. Lower bounds by positivity. So each singlet level minus sqrt(t) e_* has the limit of the alpha = 0 case, and the gap in units g^(2/3)/l tends to M^(-1/3) kappa_r = kappa_r/N.

**Uniform in N? No, and the note does not claim it.** The asymptotic kappa_r g^(2/3)/(N l) is a limit g -> 0 at fixed N (fixed graph). The limit constant kappa_r/N tends to 0 as N grows. So no lower bound c g^(2/3)/l uniform in N holds in the stiff regime; line 97 states exactly this. Nothing in the note bounds the gap for N -> infinity at fixed g; the relative spring modes have frequency sqrt(t lambda_2) with lambda_2 -> 0 as the graph grows, so the proof's separation of scales is itself non-uniform in N. The physical-unit gap kappa_r g^(2/3)/L is the zero-mode gap of one block of side L at the block coupling g; it is not the one-block gap kappa_r g^(2/3)/l.

What this step shows (GUIDE, my reading): in the reduced zero-mode model, weak-coupling sewing turns N^3 blocks into one block of side L. The springs lock whole tuples across blocks, not the vectors inside one tuple, so the Simon mechanism survives, but only as the big box's own zero-mode gap. This agrees with check 1279's rejection of the alignment inference (locking is not alignment) and removes the "fixed fraction" hope at weak coupling.

### Step 3. Cyclic adjoint sewing: (8)-(12), lines 134-197

**Site gauge invariance of (8): HOLDS.** Under h: y_x -> Ad(h_x) y_x, U_xy -> h_x U_xy h_y^(-1), the spring |y_x,i - R_xy y_y,i| is unchanged; (8) depends on U only through Ad U, so it is also invariant under every single-edge sign change U_e -> -U_e. This large symmetry group Z_2^E drives (12).

**(11), lines 153-159: HOLDS.** At fixed U the y-part is r copies of -Delta/2 + (t/2) z^T D_R z on R^(3M), with bottom (sqrt t / 2) Tr sqrt(D_R) per copy (zero eigenvalues are free directions with infimum 0). V >= 0 and -Delta_U >= 0, so (8) dominates the multiplication operator sqrt(t) e(R(U)) as a form (direct integral over U). Walk expansion: D_R = Deg ⊗ I_3 - A_R with (A_R)_xy = R_xy, so bI - D_R = (b - Deg) ⊗ I_3 + A_R has nonnegative stays and SO(3) blocks. In Tr exp(u(bI - D_R)) each closed walk carries a nonnegative weight times the trace of its SO(3) holonomy, at most 3, and exactly 3 at R = I. Keeping only the walks of C (length s, weight 1, coefficient u^s/s!) gives Tr e^(-u D_I) - Tr e^(-u D_R) >= e^(-bu) (u^s/s!) sum_C (3 - Tr R_gamma). The identity sqrt(v) = (2 sqrt pi)^(-1) int_0^inf (1 - e^(-uv)) u^(-3/2) du holds (integrate by parts: 2v Gamma(1/2) v^(-1/2)); the integrand difference is O(u) at 0 and bounded at infinity. int_0^inf e^(-bu) u^(s - 3/2) du = Gamma(s - 1/2) b^(-(s - 1/2)) for s >= 1. Multiplying by r/2 gives exactly the constant r Gamma(s - 1/2)/(4 sqrt(pi) s! b^(s - 1/2)).

**(9), lines 142-145 and 161-168: HOLDS.** Lower bound: (11) with C empty. Upper bound, after z = t^(1/4) y and division by sqrt t: kinetic -Delta_z/2, spring z^T D_R z/2, quartic coefficient t^(-3/2)/2 (V has degree 4), link coefficient alpha/sqrt(t). Gaussian trial with matrix D_I + mu^2: flat harmonic energy <= (r/2) Tr sqrt(D_I + mu^2) <= e_I + 3 r M mu/2; covariance (1/2)(D_I + mu^2)^(-1/2) <= (2 mu)^(-1); quartic <= C_r M mu^(-2) (copies independent, |a x b|^2 <= |a|^2 |b|^2). Bumps of radius epsilon: Dirichlet energy <= C epsilon^(-2); for a conjugation-invariant law E Ad U = c_eps I (Schur on R^3), 1 - c_eps = E[2(1 - cos 2 theta)]/3 <= 4 eps^2/3; the cross term changes by 2(1 - c_eps) E[z_x . z_y] <= C eps^2/mu per edge and copy. Gauge averaging (int |f(g .)|^2 dg)^(1/2) keeps the norm and the potential term and does not raise the kinetic term (Cauchy-Schwarz; isometric action). mu = eps = t^(-1/6) gives each term <= C(1 + alpha) t^(-1/6) per site, with eps <= 1 for t >= 1.

**(10), lines 146-151: HOLDS.** Ground expectation: sqrt(t)[e_I + c_s sum_C <3 - Tr R_gamma>] <= E(t) <= sqrt(t)[e_I + M C (1 + alpha) t^(-1/6)]. Compact resolvent at alpha > 0: form domination by sum_x K_r + alpha sum_e (-Delta_U).

**(12), lines 178-191: HOLDS, count and N-uniformity included.** f_p = tr(U_dp)/2 is gauge invariant and invariant under centre-plane flips (an elementary square crosses each plane 0 or 2 times when N >= 3); one edge flip negates it, so <f_p> = 0 in a flip-invariant psi. For tr V = 2 cos theta, Tr Ad V = 1 + 2 cos 2 theta = 4 f^2 - 1, so 3 - Tr R = 4(1 - f^2). (10) with C = the 3M oriented rooted squares (b = 6, s = 4) and translation and cubic invariance give <1 - f_p^2> <= C_r (1 + alpha) t^(-1/6) for every p, constant free of N. Ground-state localisation identity: <f psi, (K - E) f psi> = alpha int psi^2 sum_e |grad_(U_e) f|^2, since f does not depend on y. For each of the four edges the holonomy is an isometric image of U_e on the unit S^3 and f is its first coordinate, so |grad f|^2 = 1 - f^2; the energy ratio is 4 alpha <1 - f^2>/<f^2>. Distinct squares have distinct edge sets (simple graph, N >= 3), so f_p psi carry distinct characters of Z_2^E, distinct from psi's trivial one: orthogonal, with no cross terms. Min-max on the (3M + 1)-dimensional span gives 3M levels above the simple vacuum within C_r alpha (1 + alpha) t^(-1/6), with the threshold in t free of N. With alpha = sigma/(2t) and mu = eps = t^(-1/2) all four trial terms are O_sigma(t^(-1/2)), so <1 - f_p^2> <= C t^(-1/2) and the energies are <= C_(r,sigma) t^(-3/2). In physical units that is C g^(8/3)/l against the block gap kappa_r g^(2/3)/l.

**Thermal consequence, lines 193-197: HOLDS.** Dimensionless time N g^(2/3)/512; 3M levels each weigh at least exp(-(N g^(2/3)/512) C t^(-3/2)), which tends to 1 as g -> 0. The note's caveat is right and essential: the soft vectors are Z_2 plaquette variables with no magnetic cost, because (8) sees only Ad U. The Wilson action breaks single-edge flips, so <f_p> = 0 and the orthogonal supply fail there. (12) refutes a carry for adjoint sewing only; it says nothing about the fundamental Wilson tiling.

**Line 170, Wilson Hessian example: HOLDS.** One link at -I, the rest I: all adjoint transports are I, the incident plaquettes have tr U_p/2 = -1. Replacing the link by -exp(s i) gives plaquette action beta(1 + cos s), second derivative -beta at s = 0 (the note writes -1 per unit beta). So the Wilson magnetic Hessian is not bounded below by an adjoint-transport comparison like (11).
