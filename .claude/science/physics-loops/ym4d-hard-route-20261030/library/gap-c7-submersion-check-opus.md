lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-23T12:32Z

# Check 1411: cross-provider check of row 1409 (`library/gap-c7-submersion-astra62.md`)

Started 2026-11-23T00:31Z (date -u), Mac mini worker, Claude Opus 5.5 high, on branch claude/ym4d-hard-route at da2172a15.
Author of the checked text: gpt-6.2-astra max (row 1409). This check is a different vendor and a separate derivation.

## Plan

1. Read row 1409 in full; list its numbered claims (1)-(11).
2. Check the horizontal lift (5) and the transport it induces on the conditional law (3).
3. Check the regular fibre and its orbit type.
4. Check identity (7), including a direct computation of the derivative of a normalised conditional
   expectation with a smooth test localised near one of the two regular fibre orbits.
5. Passage to the gauge quotient; (8) for U(1).
6. Scale factors of (9) and the table, with the physical adjoint; the sign in (10); times in (11) against row 708 and its check.
7. Lott's hypothesis (math/0211065), read from the source.
8. Verdict: HOLDS / HOLDS AFTER CORRECTION / FAILS, at most ten defects ranked.

## Steps

### Step 1. Map, measures, lift (5), transport on (3), criterion (6)  [written by 2026-11-23T00:37Z, date -u]

Re-derived by hand, independently of the text's wording.

- (1)-(3). Change of variables (u_c, v_c) -> (h_c = u_c, V_c = u_c v_c) on each retained pair: for fixed h, v -> h v
  preserves Haar, so du dv = dh dV and the pushforward density is H_beta(V) as in (2); the conditional (3) follows.
  HOLDS.
- (5). d(uv)(uv)^{-1} = X_1 + Ad_u X_2 with X_1 = u' u^{-1}, X_2 = v' v^{-1}. Ad_u is an isometry of the bi-invariant
  form, so the minimal-norm solution of X_1 + Ad_u X_2 = Y is X_1 = Y/2, X_2 = Ad_{u^{-1}} Y/2, X_z = 0; the kernel
  (K, -Ad_{u^{-1}} K) is g_a-orthogonal to it. Norm of the lift s_a |Y|^2/2, so D is a Riemannian submersion onto
  (coarse links, ghat = (s_a/2) sum_c |Y_c|^2). Vertical norm of (K, -Ad_{u^{-1}}K) is 2 s_a |K|^2. HOLDS.
- Transport in (h, z). With h = u: h' h^{-1} = Y/2, independent of h, so h_c(t) = r_c(t) h_c with r_c' r_c^{-1} = Y_c/2,
  r_c(0) = 1, and z fixed; then v = h^{-1}V has v' v^{-1} = Ad_{h^{-1}}(Y/2), consistent with (5). Left translation
  preserves dh dz, and the fibre Riemannian volume is a constant multiple of dh dz (bi-invariant fibre metric
  2 s_a |X_h|^2). HOLDS.
- (6). For a Riemannian submersion the conditional law of phi dvol_M on a fibre is phi dvol_F normalised (coarea
  with Jacobian 1). Since P_t preserves dh dz, the density ratio is
  L_t(p) = exp(-beta[S(P_t p) - S(p)]) * H_beta(V(0))/H_beta(V(t)),
  and exact transport (L_t = 1 on the fibre) holds iff S(P_t p) - S(p) is constant in p. HOLDS (as stated in (6)).

### Step 2. The regular fibre, the path, and identity (7)  [written by 2026-11-23T00:37Z, date -u]

- Path. Selected coarse row (direction 1, transverse 0) moved to exp(tT), Y = T on each of its coarse links. Coarse
  gauge-horizontality: pairing of the velocity with the vertical vector of xi at a row vertex x is
  <Y_out - Ad_{U_in^{-1}} Y_in, xi> = <T - Ad_{exp(-tT)}T, xi> = 0. HOLDS. Lift: h_c = 1 -> exp(tT/2), v_c -> exp(tT/2);
  all fine row links exp(tT/2). HOLDS.
- The off-string link e_2 -> e_2 + e_1 has transverse coordinate x_2 = 1, odd, so it lies on no retained pair. HOLDS.
  Plaquettes meeting a moving row link: for row link j -> j+1 the 2(d-1) plaquettes in the (1, mu) planes; each has
  exactly one row link (the parallel 1-link sits at transverse +-e_mu). The only one also containing the link
  e_2 -> e_2+e_1 is the (1,2) plaquette with corners 0, e_1, e_1+e_2, e_2. Its other links 0 -> e_2 (retained) and
  e_1 -> e_1+e_2 (off-string) are the identity in the stated configuration. HOLDS.
- Holonomy exp(tT/2) D_pm^{-1} = exp((t/2 -+ pi/2)T), T = i diag(1,-1,0,...), so
  chi = (N - 2 + 2 cos(t/2 -+ pi/2))/N. HOLDS. Increments: Delta S_+ = -(2/N) sin(t/2), Delta S_- = +(2/N) sin(t/2)
  (cos(+-pi/2) = 0). All other plaquette increments agree for U_+ and U_- (they do not contain the D link).
- (7). log L_t(U_+) - log L_t(U_-) = -beta(Delta S_+ - Delta S_-) = (4 beta/N) sin(t/2); derivative at 0 is 2 beta/N.
  HOLDS, for N = 2, 3 (the formula is uniform in N >= 2).
- Regular orbit type. P = exp(pi T/2) has eigenvalues i, -i, 1, ... (distinct for N = 2, 3); Q = scalar times cyclic
  shift (det 1 can be arranged: for N = 2 the shift has det -1, multiply by i; for N = 3 det 1 already). Centraliser of
  P = diagonal matrices; of P and Q = scalars = Z(G). Coarse stabiliser of V(t): value at origin commutes with the P- and
  Q-loop holonomies, hence central = z; propagating k_y = V_{xy}^{-1} k_x V_{xy} gives z at every coarse site. Fine
  stabiliser of any U in the fibre: restriction to coarse sites stabilises D(U) (equivariance), hence is z; at a midpoint
  m, k_m = u^{-1} z u = z; at other odd sites, connectivity of the fine graph gives z. So every fine orbit in the whole
  fibre over V(t) is principal (stabiliser Z(G)). HOLDS, and slightly more than the text states: not only U_pm but the
  entire fibre lies in the principal stratum, so the quotient fibre is a compact smooth manifold.
- Separating loop. chi(P D_+^{-1}) = chi(1) = 1; chi(P D_-^{-1}) = chi(exp(pi T)) = (N-4)/N. HOLDS.

### Step 3. Lott's hypothesis, read from the source  [written by 2026-11-23T00:37Z, date -u]

Source: J. Lott, "Some geometric properties of the Bakry-Emery-Ricci tensor", arXiv math/0211065v2 (fetched by URL
into /tmp/c7chk-lott, text extracted with PyMuPDF).

- Theorem 2 (p. 3): "Suppose that fiber transport preserves the fiberwise measure phi_M dvol_F up to a multiplicative
  constant ... 1. For any r in R, if Ric~^M_inf >= r g_M then Ric~^B_inf >= r g_B." Row 1409's paraphrase (line 58) is
  accurate.
- (3.9) (p. 9): Ric~^B_inf(X,X) phi_B = int_F [Ric~^M_inf(X,X) + 2(A_X,A_X) + (T_X,T_X) - (X phi_M/phi_M - (X,N))^2]
  phi_M dvol_F + (int_F (X phi_M/phi_M - (X,N)) phi_M dvol_F)^2 / phi_B. The last two terms together equal
  -phi_B Var_cond(sigma_X), sigma_X = X phi_M/phi_M - (X,N) = L_X(phi_M dvol_F)/(phi_M dvol_F) by (3.10). Row 1409's
  "minus the conditional variance of the logarithmic rate" is accurate. (3.9) is an identity with no transport
  hypothesis; the hypothesis is used only at (3.11) to set the variance to zero.
- Single-orbit-type example (end of Section 3, pp. 10-11): quotient by an isometric action with one orbit type
  satisfies the hypothesis. Accurate as cited on line 91.
- In the present map the fibre Riemannian volume is invariant under horizontal transport (Step 1), so the term (X,N)
  drops out of sigma and sigma_X = -beta (X^ S) restricted to the fibre. Exact transport <=> Var_cond(sigma_X) = 0
  for every X <=> (6) to first order. Consistent with the row.

### Step 4. Direct computation with a localised test; passage to the gauge quotient  [written by 2026-11-23T00:37Z, date -u]

Separate derivation (not a re-reading of line 81-89).

**Fibre-preserving gauge group.** Fine gauge transformations k with D(kU) = D(U) = V(0) are those whose restriction
to the even sites stabilises V(0): by Step 2 that is a single central z at all even sites, and k arbitrary at odd
sites. Such k acts on a pair by h_c -> z h_c k_m^{-1} and on off-string links by conjugation-type multiplications;
P_t acts by h_c -> r_c(t) h_c and fixes z-links. Since z is central, P_t k = k P_t. S is gauge invariant, so
S(P_t kp) - S(kp) = S(P_t p) - S(p): the score is constant on these orbits.

**D-bar is a Riemannian submersion on the principal stratum.** Let rho: G_f -> G_c be restriction to even sites
(surjective; D(kU) = rho(k)D(U)). For W fine-gauge-horizontal at U, write dD W = Y + Z with Y coarse-gauge-horizontal
and Z coarse-vertical; Z = dD Z' for the fine vertical vector of any lift of the coarse generator, so dDbar[W] = [Y].
The D-lift Y^ of Y satisfies g_a(Y^, W') = ghat(Y, dD W') for every fine W' (Riemannian submersion), so Y^ is
orthogonal to every fine vertical vector and to every fine horizontal W' with dDbar[W'] = 0, and |Y^|_{g_a} = |Y|_ghat.
Hence Dbar is a Riemannian submersion for the quotient metrics, its horizontal lift of [Y] is [Y^], and its transport
is Pbar_t[U] = [P_t U]. This confirms line 89. By Step 2 the whole fibre over [V(t)] is principal, so Dbar has compact
smooth fibres there and Lott's setting applies locally over the path.

**Conditional law on the quotient.** For gauge-invariant f, coarse-gauge equivariance of (2)-(3) gives
E[f | Dbar = [V]] = int f dmu_{beta,V}, so the quotient conditional is mubar_V = q_* mu_{beta,V}. On a Riemannian
submersion the normalised Lott fibre measure phibar dvol_{Fbar} is the conditional law (coarea, Jacobian one), and the
continuous version is unique; orbit volumes are already inside phibar. So there is no free factor to adjust.

**Derivative.** For a continuous f on Fbar_0 put E_t(f) = int_{Fbar_t} f o Pbar_t^{-1} dmubar_t = int_{F_0} (f o q) L_t
dmu_{beta,V(0)}. L_t is smooth in (t, p) on the compact fibre, so
  d/dt E_t(f) at 0 = int (f o q) sigma dmu_{beta,V(0)},  sigma(p) = -beta d/dt S(P_t p)|_0 + beta E_{mu_0}[d/dt S(P_t .)|_0].
Choose phi in C_c^inf([0,1)), phi >= 0, phi(0) > 0, and f_eps^pm([U]) = phi(dbar([U],[U_pm])/eps) with dbar the
quotient distance (Lipschitz; a smooth mollified version gives the same limit). [U_+] != [U_-] by the separating loop,
so for small eps the supports are disjoint. mu_0 has a positive continuous density, so int f_eps^pm dmu_0 > 0, and
since sigma is continuous and constant on the orbits,
  d/dt log E_t(f_eps^pm) at 0  ->  sigma(U_pm)   (eps -> 0).
From Step 2, d/dt Delta S_+ = -1/N and d/dt Delta S_- = +1/N at t = 0, so
  sigma(U_+) - sigma(U_-) = 2 beta / N,
in agreement with the derivative of (7) at 0. Exact transport (in Lott's sense, on the quotient) would give
E_t(f) = E_0(f) for every f, hence a zero derivative for both tests. Contradiction for every beta > 0.

**Decisive outcome of the row's question.** The ratios differ as claimed; orbital disintegration does not cancel the
difference (the quotient conditional is the pushforward of the fibre conditional, and the score is gauge invariant).
No cancelling factor exists, so no quotient case is reopened. Exact Lott transport is retired for this map and the
metric class "configuration-independent constant multiples of g_a and g_{2a}" (such rescalings do not change the
horizontal distribution (5), hence not P_t, hence not (7)). HOLDS.

Scope remark (not a defect). The obstruction is first order in t and linear in beta; Lott's identity (3.9) still holds
without the hypothesis, with the term -phibar Var_cond(sigma). Row 1409 states this scope correctly (line 146).

### Step 5. (8) for U(1); scale factors (9), the table and the physical adjoint; sign of (10)  [date -u at write: 2026-11-23T00:37Z]

**(8).** For U(1) in angle coordinates the metric is flat with constant coefficients, the gauge generators are the
constant image of d_0, the horizontal space ker d_0^* is a constant subspace, horizontal lifts of constant fields are
constant and commute, so A = 0 everywhere. HOLDS. The abelian version of (7): with chi = cos theta and the off-string
angle at +-pi/2, the plaquette angle is t/2 -+ pi/2, Delta S_pm = -+ sin(t/2), difference of log rates
-beta(Delta S_+ - Delta S_-) = 2 beta sin(t/2). HOLDS. (For U(1) every orbit has stabiliser the constants, so no P, Q
construction is needed; the text does not claim one.) The (t1) reading: zero O'Neill gain at (8), nonzero score
variance, so the variance in (3.9) cannot be credited to the nonabelian bracket. Sound.

**(9) and the physical adjoint.** lambda_d^2 = 2 s_{2a}/s_a = 2 * 2^{d-2} = 2^{d-1}; g_{2a} = lambda_d^2 ghat. For coarse
F, grad_a(F o D) is the D-lift of grad_ghat F, so |grad_a(F o D)|^2 = |grad_ghat F|_ghat^2 o D. With the physical
coarse metric, grad_ghat F = lambda^2 grad_{2a} F and |.|_ghat^2 = lambda^{-2}|.|_{2a}^2, giving
|grad_a(F o D)|^2 = lambda^2 |grad_{2a} F|^2 o D. Equivalently, the g_a-to-g_{2a} adjoint of dD is lambda^2 times the
ghat-lift. Var is equal under the pushforward (2); W_f = W_c o D pointwise (the fine holonomy of a coarse path is the
product of the coarse links). So R_{2a} = 2^{1-d} R_a and k_{2a}/k_a = 2^{d-2} 2^{1-d} = 1/2. HOLDS.

Table: lambda^2 = 8, 16; c(d) = 1/8, 1/16; k-ratio 1/2, 1/2; inverse susceptibility ratio 1, 1; classical factor
beta_{2a}/beta_a = 2^{d-4} = 1, 2 (from (1/2) beta_l l^{4-d} int sum |F|^2: a plaquette gives l^4 |F|^2/2 at second
order with |X|^2 = -Re tr X^2/N, and l^{-d} cells per unit volume). All entries HOLD.

Bochner step on line 46: integrated Bochner for the weighted Laplacian gives lambda_1 >= rho (Lichnerowicz), hence
Var W <= E/rho, R >= rho. HOLDS. I_Gamma = 1/Var W: HOLDS. Invariance of rho/E under a constant metric rescaling
(g' = c g gives rho' = rho/c and E' = E/c): HOLDS.

Reading of (b). Lott's descent, if it applied, gives Ric_B + Hess >= rho ghat = (rho/lambda^2) g_{2a}, that is
B_a(x) => B_{2a}(x/2 + eta) in the dimensionless floors x = s rho, in every d, not B_{2a}(2^{d-4} x + eta). The
d-dependence of c(d) = 2^{1-d} is the normalisation s_l = l^{d-2} of (1) and nothing else (k, the dimensionless
version, is 1/2 in both dimensions, and the physical loop's inverse susceptibility is carried with factor 1). So
(t2)/(b) fails as stated. HOLDS, with defect D1 below on wording.

**(10).** On the row with every fine link exp((pi+t)T), each row link lies in 2(d-1) plaquettes with one moving link,
1 - chi = (2 + 2 cos t)/N, second derivative -2/N at 0; Hess S(X,X) = -4(d-1) n_1/N; |X|^2_{g_a} = s_a n_1 * 2/N
(|T|^2 = 2/N). Ratio -2(d-1)/s_a. The path is a product of one-parameter-subgroup translates, hence a g_a-geodesic, and
horizontal at every t by the same incoming/outgoing cancellation, so it projects to a quotient geodesic and the
second derivative is the same downstairs. Sign negative. HOLDS.
Explicit constant upstairs (my addition): Ric of the bi-invariant metric is -(1/4)Killing; for su(N) with
|X|^2 = -tr X^2/N this is (N^2/2)|X|^2, so in g_a the Bakry-Emery value in this direction is
(N^2/2 - 2(d-1) beta)/s_a, negative for beta > N^2/(4(d-1)) (1/3 for SU(2), d = 4). Downstairs C changes by the
finite O'Neill and orbit-volume terms at this fixed point.

The fixed-lattice large-beta estimate on line 130: P(S >= m) <= e^{-beta m}/(e^{-beta m/2} Haar{S < m/2}). HOLDS.

**Reading of (t4).** Row 1386 (4.3 (e), 4.5 (t4)) asks that the hypothesis FAIL when beta grows at a fixed lattice.
(10) shows it does fail. So C7 passes (t4); row 1409's text reports the computation without saying pass or fail
(see D2). But the consequence the text does not draw is stronger against C7: the fine class B_a(x), x > 0, is empty on
any lattice once beta > N^2/(4(d-1)) (upstairs) or beta > C s_a/(2(d-1)) (quotient), a fixed constant, while the
prescribed trajectory has beta_j -> infinity. So a pointwise Bakry-Emery seed at the fine scale cannot be the input
on the trajectory at late cutoffs, independently of the transport failure (see D3).

### Step 6. Times and constants in (11) against row 708 and its check  [date -u at write: 2026-11-23T00:39Z]

Sources read: `library/gap-mid-max.md` lines 100-158 (Lemma 4.1, Theorem TR, Proposition Delta, Corollary TR1);
`library/gap-dob-astra.md` section 7 (lines 343-397, Corollary TR1 HOLDS) and section 6 heading (Proposition Delta
HOLDS); `library/gap-seed-astra62.md` line 11 (the OPEN seed: range of P_0, s(t) = sum (lambda_a/lambda_0)^t,
w_j = floor(n_j/1024), threshold 4/21, 4 | n_j, n_j >= 2^70).

- Coupling: beta_* <= 1/25600 gives theta = 12800 beta_* <= 1/2, the hypothesis of TR1's strong-coupling part. HOLDS.
- Bound: Proposition Delta with a = t_0, b = n (needs a >= 3, b >= a) and gap-seed-sc Theorem 1 (iii) via
  Delta(t_0^4) <= 0.0101 t_0^4 theta^{4 t_0} (needs t_0 >= 4) give g(t_0; n^3; beta_*) <= 0.0101 n^3 t_0 16^{-t_0}
  <= 0.0101 t_0/n, using 2^{t_0} >= n. This is exactly the first display of TR1's proof with b = n, and it uses neither
  (VIR_K) nor Theorem SH (SH enters only the gap sentence). 101/10000 = 0.0101. HOLDS. (TR1's "b >= 256, even" is only
  for a = b/2 and the time window [t_0, a]; not needed here.)
- g = log(1 + S): G(t; B) = log Tr T^t - t log lambda_0 = log(1 + sum rho_i^t) (Lemma 4.1 (b)). HOLDS.
- Time: t = 2 floor(n/1024) >= t_0 = ceil(log_2 n) once n >= 2^14 or so; on admissible sides n >= 2^70 always. S is
  non-increasing in real t because 0 <= rho_i <= 1 (T >= 0 by reflection positivity; Lemma 4.1 (b)). HOLDS.
- Neutral versus full trace: the neutral range of P_0 is an invariant subspace of the same transfer, so its excited
  eigenvalues are a sub-multiset of the full ones provided the global top eigenvector lies in it. That holds: the
  transfer has a strictly positive kernel, so its top eigenvector is simple and positive (Jentzsch), and electric-centre
  translations commute with T and preserve positivity, so they fix it. Row 1409 asserts this in one clause ("the neutral
  sector contains the vacuum"); the positive normalised vacuum is used on file (row 1367, line 33). HOLDS; see D5.
- Conclusion s_{n,beta_*}(2w) <= exp(0.0101 t_0/n) - 1 -> 0, below 4/21 for large n. HOLDS.
- Logic of (t5): the seed holds at (beta_*, large n) while (6) fails there (the construction needs side >= 16 and
  beta > 0), so the seed does not imply the transport premise. HOLDS. The text correctly flags that beta_* is off the
  prescribed trajectory.

### Step 7. Remaining lines (spot checks)  [date -u at write: 2026-11-23T00:39Z]

- Line 46 (Bochner, R >= rho, I_Gamma = 1/Var W): HOLDS (Step 5).
- Line 72: SU(2) shift has det -1, multiply by i; SU(3) cyclic shift has det 1; P = diag(i, -i, 1) for N = 3. HOLDS.
- Line 91 (singular orbits at identity links; Lott's single-orbit-type example only covers the gauge quotient): HOLDS.
- Line 93: Ric of the bi-invariant SU(N) product is (N^2/2)|X|^2 in the unscaled form, kernel = centre of the Lie
  algebra (zero); so the fine law has a positive Bakry-Emery floor for beta < N^2/(4 (d-1)) up to the Hessian bound,
  and (7) still breaks transport there. HOLDS.
- Line 121 (t3): third eigenvalue contributes 1 to both traces; rates differ by 2 beta/3. HOLDS.
- Line 130: W_Gamma = 1 when all plaquettes are trivial (flat connection, contractible loop); tail bound HOLDS.
- Line 148 (target recap): matches row 1367 line 11. HOLDS.

## Verdict  [date -u at write: 2026-11-23T00:40Z]

**Row 1409 (`library/gap-c7-submersion-astra62.md`): HOLDS.** Every numbered display (1)-(11), the lift, the transport on
(3), the regular orbit type, the passage to the quotient, (8), the table, the sign in (10) and the times in (11) were
re-derived and hold. No line fails. The defects below are about wording, labelling and scope. None changes a conclusion
of the file. D1 corrects the one-line summary of row 1409 in FINISH, not the file.

**Decisive outcome (the row's question).** The two conditional log-density ratios differ as claimed: by
(4 beta/N) sin(t/2), with derivative 2 beta/N. A separate derivation with smooth tests localised near the two regular
quotient orbits gives the same difference (Step 4). Orbital disintegration does not cancel it, for two reasons. First,
the quotient conditional is the pushforward q_* mu_{beta,V}. Second, the score is invariant under the fibre-preserving
gauge group. The whole fibre over the path is principal, so Lott's smooth setting applies there, and the orbit-volume
density is already contained in the unique continuous conditional law. No cancelling factor exists, so no quotient
case is reopened. **Exact Lott transport is retired** for the two-link product map D of row 1383 together with the
metric class "positive configuration-independent multiples of the physical metrics g_a, g_{2a}". This holds for every
beta > 0, for N = 2 and 3, and for d = 4 and 5. Lott's identity (3.9) remains true without the hypothesis, with the
term -phi_B Var_cond(sigma). Bounding that term is a different statement. Row 1409 does not claim to bound it, and
neither does this check.

### Defects, ranked by what each breaks (at most ten)

- **D1 (decision record; (t4) mislabelled in the FINISH summary).** The RESULT of row 1409 in FINISH lists "(t4) the
  pointwise floor fails at large beta on a fixed lattice by (10)" among the filter outcomes, in a way that reads as a
  filter failure. Row 1386, 4.3 (e) and 4.5 (t4), asks that the hypothesis fail as beta grows at a fixed lattice. So C7
  **passes** (t4). The file itself (lines 123-128) reports the computation without a label. Correction: record (t4) as
  passed. The negative content belongs under D2.
- **D2 (consequence not drawn; a second, independent obstruction).** By (10), the fine pointwise class B_a(x) with
  x > 0 is empty on every lattice once beta exceeds a fixed constant. Upstairs this constant is N^2/(4(d-1)), from
  Ric = (N^2/2)|X|^2 in the unscaled form (Step 5). For SU(2), d = 4 it is 1/3, the same threshold as Proposition BE
  of row 708 (`gap-mid-max.md` line 79), reached here by a different configuration. On the prescribed trajectory
  beta_j -> infinity, so a bare-scale Bakry-Emery floor cannot be C7's input at late cutoffs, whatever happens to
  transport. Line 128 states the inequality but not this consequence.
- **D3 ((t2) wording).** c(4) = 1/8 and c(5) = 1/16 differ by 2^{-(d-4)}. That d-dependence comes only from the
  normalisation s_l = l^{d-2} in (1). The text should say so, and should also state the carry of the dimensionless
  floor x = s rho that Lott would give if he applied: B_a(x) => B_{2a}(x/2 + eta) in every d. That halves the floor
  even in d = 4, which is stronger than "no factor 2^{d-4} is carried". The conclusion that (b) fails stands.
- **D4 ((t5) is trivially satisfied).** Non-equivalence with the seed is shown at fixed strong coupling. Because the
  transport premise is false for every beta > 0, it cannot be equivalent to a seed that is true at small beta, so the
  test carries little information. It says nothing about the floor statement without transport, that is (3.9) with
  the variance kept. Line 146 states that scope correctly, and no conclusion changes.
- **D5 (one clause asserted without proof).** In (11), "the neutral sector contains the vacuum" needs a sentence:
  the transfer kernel is strictly positive, so the top eigenvector is simple and positive (Jentzsch); electric-centre
  translations commute with T and preserve positivity, so they fix it (Step 6). The positive vacuum is used on file
  (row 1367, line 33).

Not defects: line 89 proves regularity only near U_pm, but the whole fibre is principal (Step 2), which is slightly
stronger. The U(1) analogue needs no P, Q construction, and the text does not claim one.

### Provenance and independence

Author of row 1409: gpt-6.2-astra max (OpenAI). This check: Claude Opus 5.5 high (Anthropic), Mac mini worker, hand
derivations, no computation, no numeric job, no Monte Carlo. Independence is partial. (5), (6), (9) and (10) were
re-derived from the definitions. (7) was re-derived on the text's own configuration; I constructed no second witness.
The quotient step and the localised-test derivative (Step 4) follow a separate route from lines 81-89. Lott's Theorem 2
and (3.9)-(3.11) were read from arXiv math/0211065v2. Row 708's constants were read from `gap-mid-max.md` and its
check `gap-dob-astra.md` section 7, and were not re-derived beyond the arithmetic in Step 6.

Nothing in this file is claimed as new. The beta threshold in D2 reproduces Proposition BE of row 708. A search of
`library/open-core.md` for "Lott" gave no lines. FINISH has 3 lines that mention Lott, all in rows 1402-1411.

### Next

No band proof row follows from C7 in this form (I agree with row 1409's recommendation). Any revival would have to be
a different block map or metric with a different horizontal distribution, or a bound on the variance term in (3.9).
Under D2 it would also need a floor at a renormalised scale, not at the bare scale. That needs a new row with its own
gate, and this check does not queue one.
