lead: anthropic/claude-fable-5-2/medium laptop-subagent

# gap-band-cut-covariance-fable (row 1566)

## Plan (provisional; refined after reading the brief)
1. Read FINISH.md rule sections (1-84, 299-360), GOAL.md, row 1566 brief, check 1556 section (v).
2. State the lemma exactly, with its (W)/hypotheses, from the brief.
3. Grep library/open-core.md, library/open-registry.md, FINISH rows for prior statements.
4. Attack: one lemma / one test model / one attack stage per step, result appended before going on.
5. End with a RESULT: line.

## Step 0. Sources read, statement fixed

Read: FINISH.md lines 1-84 and 299-360, GOAL.md, row 1566 (brief), check 1556 `library/gap-mech-direction4-check-astra62.md` in full, section (v) lines 56-110 line by line. Row 1565's output was not read.

Credit. The cut rotation R_s, the half-turn R_pi = C_1 a.e., the four-corner identity and the statement of the lemma are check 1556 section (v) (gpt-6.2-astra). The single-link staple rotation is Lemma MC of row 1016; the covariant axis is rows 1034-1035. Twists and flux sectors are 't Hooft's. The pinned-end stiffness idea is from the OpenAI authors' 2D proof (row 1007 reads it). Outline and complete account: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.

**Lemma BC(eps)** (ON FILE, check 1556 lines 102-108; target of this row). 4D SU(2) Wilson, beta in [2,3], spatial slice a periodic n^3 lattice, n in 1024 Z, u = n/512, v in {u/2, u}, v >= 3. K_v = gauge-averaged kernel of the half-cylinder of length v. mu_{z,2v}(dA dB) = K_v(A,B) K_v(B, C_z A) dA dB / Z^z(2v). With h_{s,t}(x,y; X,Y) := (D_x^(1) D_y^(2) log K_v)(R_s X, R_t Y):

  sup_{s,t in [0,pi]} sup_{x in cut} sum_{y in cut} E_{mu_{z,2v}} | h_{s,t}(x,y; B, C_z A) | <= C v^{-2-eps},

for some C < infinity, eps > 0, uniform in beta, n, v and the eight twists z.

## Plan (refined)
1. Lemma P1: exact covariance form of h (what f_x, g_y are).
2. Lemma P2: what BC(eps) gives, exactly (twist ratio and a Kullback-Leibler bound), with the constant.
3. Lemma P3: exact converse-side inequality (a necessary condition for BC(eps)); this is the tool for every test model.
4. Test models: free Maxwell in d = 3, 4, 5 (exact zero-mode identity); compact U(1) 4D weak; 5D SU(2) weak; strong-coupling 4D SU(2); 3D compact U(1).
5. Three attacks on BC(eps) for SU(2) at beta in [2,3].
6. Non-equivalence to (PUR-io); what further input is needed.
7. Greps for prior statements; RESULT line.

## Repo search (lane only, relative paths)

- `library/open-registry.md`: R10 (line 1017) is an in-law covariance bound with exponential decay for a Q2 posterior score at beta in [2,3]. R11 is a transport bound. R12 is the carry from an order-one coupling. TWO-PER is the two-period input. None is the mixed derivative on two pinned ends of the cut (check 1556 line 3 says the same).
- `library/open-core.md`, `library/open-registry.md`: no match for "interface tension", "flux energy", "Tomboulis-Yaffe", "Kullback", "cut rotation". So the statements P2-P6 below are not on those lists.
- FINISH rows: the Tomboulis-Yaffe inequality (Kanazawa, arXiv:0808.3442, Theorem 1) is ON FILE as a lead of row 690 (FINISH line 768, 775), premise open. Fact PUR and the sixteen masses are ON FILE in `library/gap-k2-tool-design-fable.md` lines 100-119. Theorem DOB (beta < 1/18, alpha = 18 beta) is ON FILE in `library/gap-skeleton-final.md` 13.12 (rows 707-711, checked row 709). The six tests (g1)-(g6) are `library/gap-mech-direction4-fable.md` section 1.5.
- Rows 1565 (astra), 1567 (luna, literature) and 1568 (neon) work on the same lemma now. I did not read their outputs.

## Step 1. Lemma P1 (covariance form). PROVED

Convention. K_v(X,Y) = e^{a(X)+a(Y)} K°_v(X,Y). Here a is the end-slice spatial term, and K°_v(X,Y) is the integral over all temporal links of the v layers and all spatial links of slices 1..v-1 of exp((beta/2) sum_p tr U_p), p over the temporal plaquettes of the v layers and the spatial plaquettes of slices 1..v-1. Free temporal links at both ends are the gauge averaging. Any other split of the end terms changes a only.

Single-link rotation. For x on the cut, X^{x,sigma} has X_{x,1} replaced by exp(sigma a_x(X)) X_{x,1}. The axis a_x reads only 2- and 3-links, so a_x(X^{x,sigma}) = a_x(X) and a_x(R_s X) = a_x(X). D_x F(X) := d/dsigma F(X^{x,sigma}) at sigma = 0. Then d/ds F(R_s X) = sum_{x in cut} (D_x F)(R_s X).

Claim. For v >= 2,
  (D_x^(1) D_y^(2) log K_v)(X,Y) = Cov_{X,Y}(f_x, g_y),
  f_x = (beta/2) tr(a_x(X) X_{x,1} W_x),  g_y = (beta/2) tr(a_y(Y) Y_{y,1} W'_y),
where Cov_{X,Y} is the covariance in the probability measure of K°_v(X,Y) (the pinned cylinder), W_x is the product of the other three links of the temporal plaquette on (x,1) in layer 0, and W'_y the same in layer v-1. |f_x|, |g_y| <= beta, so |h| <= beta^2. For v >= 3 the link supports of f_x and g_y are disjoint.

Proof. a(X) + a(Y) has zero mixed derivative. X_{x,1} enters K° only through the one temporal plaquette on it in layer 0. Differentiate under the finite Haar integral (the integrand is smooth in sigma, the axis is fixed): D_x^(1) log K° = <f_x>. For v >= 2, f_x does not read Y, so D_y^(2) <f_x> = <f_x g_y> - <f_x><g_y>. For a unit imaginary quaternion a and M in SU(2), |tr(aM)| <= 2. QED

## Step 2. Lemma P2 (what BC(eps) gives). PROVED as an implication

Notation. L_z := sup_{s,t,x} sum_y E_{mu_z} |h_{s,t}(x,y; B, C_z A)| (the left side of BC, at twist z, period 2v). rho_z(A,B) := K_v(B, C_1 C_z A)/K_v(B, C_z A).

(a) Four corners (ON FILE, check 1556 lines 93-98; re-derived). With Y = C_z A: the integral of d_s d_t log K_v(R_s B, R_t Y) over [0,pi]^2 is log K(C_1B, C_1Y) - log K(C_1B, Y) - log K(B, C_1Y) + log K(B,Y) = 2 log(K(B,Y)/K(B,C_1Y)) a.e. This uses R_pi = C_1 a.e., K(C_1X, C_1Y) = K(X,Y), C_1^2 = 1. Also R_t C_z = C_z R_t because centre flips preserve Q_x. So

  -2 log rho_z(A,B) = int_0^pi int_0^pi sum_{x,y} h_{s,t}(x,y; B, C_z A) ds dt.

(b) E_{mu_z} |log rho_z| <= (pi^2/2) n^2 L_z. (Fubini, n^2 cut links at the first end.)

(c) d mu_{z+e_1}/d mu_z = rho_z Z^z/Z^{z+e_1}. So E_{mu_z} log rho_z = log(Z^{z+e_1}/Z^z) - KL(mu_z | mu_{z+e_1}). Hence

  KL(mu_z | mu_{z+e_1}) + log(Z^z/Z^{z+e_1}) = -E_{mu_z} log rho_z <= (pi^2/2) n^2 L_z,
  KL(mu_{z+e_1} | mu_z) + log(Z^{z+e_1}/Z^z) <= (pi^2/2) n^2 L_{z+e_1}   (same with z and z+e_1 exchanged; rho_{z+e_1} = 1/rho_z).

(d) Since KL >= 0: |log(Z^{z+e_1}(2v)/Z^z(2v))| <= (pi^2/2) n^2 max(L_z, L_{z+e_1}). Adding: KL(mu_z|mu_{z+e_1}) + KL(mu_{z+e_1}|mu_z) <= (pi^2/2) n^2 (L_z + L_{z+e_1}). (This replaces the Jensen step of check 1556 line 110 and gives the same bound, plus the entropy bound, which is new here.)

(e) Under BC(eps): n = 512u <= 1024 v, so both are at most delta_v := 2^19 pi^2 C v^(-eps) (resp. 2 delta_v). The cubic symmetry of the spatial torus gives the same for e_2, e_3. So |log(Z^z(2v)/Z^0(2v))| <= 3 delta_v for all eight z.

(f) Flux weights. W_e(2v) := (1/8) sum_z (-1)^{z.e} Z^z(2v) = Tr(P_e T^{2v}) >= 0 ('t Hooft's electric flux sectors), sum_e W_e = Z^0, W_0 = Z_+. So Z^z <= Z^0 and
  sum_{e != 0} W_e(2v) / Z^0(2v) = 1 - (1/8) sum_z Z^z/Z^0 <= (7/8)(1 - e^{-3 delta_v}) <= (21/8) delta_v.

(g) Purity transfer. P_K = Z_+(2u)/Z_+(u)^2 (neutral), P_full := Z^0(2u)/Z^0(u)^2 (untwisted periodic tori). From (f) at v = u (numerator) and v = u/2 (denominator), and Z_+ <= Z^0:
  (1 - (21/8) delta_u) P_full <= P_K <= P_full / (1 - (21/8) delta_{u/2})^2.

So BC(eps) gives exactly this: at the tested coupling the sixteen masses collapse to two, and neutral purity equals the purity of the untwisted periodic tori up to a factor 1 + O(u^(-eps)). It gives no bound on either purity. Only twist ratios enter (b)-(g).

## Step 3. Test model: free Maxwell field in dimension d (exact zero-mode identity). PROVED

Model. Spatial slice (Z/n)^(d-1), real link angles theta, action (beta/2) sum_p (d theta)_p^2. Q_v(A,B) := minimum of sum_p (d theta)_p^2 over fields on the cylinder with spatial end links A, B (temporal links free). K_v := exp(-(beta/2) Q_v) (the Gaussian integral over the interior modulo interior gauge maps, up to a constant). The cut is the n^(d-2) 1-links with tail at x_1 = 0. The rotation is A -> A + s chi, chi the indicator of the cut (the abelian R_s; for compact U(1), R_pi is the Z_2 twist). The mixed derivative is the constant h(x,y) = -(beta/2) d^2 Q_v / dA_1(x) dB_1(y).

**Lemma Z (zero mode).** For every d >= 3, n, v >= 1 and x on the cut: sum_{y in cut} h(x,y) = beta/(n v). Hence sum_{y in cut} |h(x,y)| >= beta/(n v).

Proof. (1) End gauge invariance: Q_v(A + d lambda, B + d mu) = Q_v(A,B). Add d Lambda to a competitor, with Lambda equal to lambda, mu on the two ends; plaquettes do not change, temporal links are free. (2) chi = (1/n) 1_1 + d lambda, where 1_1 is 1 on every 1-link and lambda(x) = 1 - x_1/n for 1 <= x_1 <= n-1, lambda = 0 at x_1 = 0. (Check: on x_1 = 0 the difference is 1 - 1/n; on every other 1-link it is -1/n; other directions 0.) (3) So Q_v(s chi, t chi) = Q_v((s/n) 1_1, (t/n) 1_1). The functional is convex and translation invariant and so is the constraint, so the translation average of a minimizer is a minimizer. A translation-invariant field is theta_mu(x,tau) = a_mu(tau). Its spatial plaquettes vanish and its temporal (0,i) plaquettes are a_i(tau+1) - a_i(tau). The minimum of n^(d-1) sum_tau sum_i (a_i(tau+1) - a_i(tau))^2 with a_1(0) = s/n, a_1(v) = t/n is n^(d-3) (s-t)^2 / v. (4) d_s d_t of this is -2 n^(d-3)/v = sum_{x,y in cut} d^2 Q/dA_1(x) dB_1(y). Translations along the cut make the inner sum independent of x. Divide by n^(d-2) and multiply by -beta/2. QED

**Corollary Z.** With n = 512u, v in {u/2, u}: sum_y |h(x,y)| >= beta/(1024 v^2), in every dimension d >= 3. The count that pays the cut area n^(d-2) at fixed aspect is v^(-(d-2)-eps). So for the free field:
- d = 4: the analogue of BC(eps) FAILS for every eps > 0 (take v > (1024 C/beta)^(1/eps)). PROVED. The lead's rough count (order v^(-2), GUESSED in the brief) is confirmed as an exact lower bound.
- d = 5: the analogue fails by a full power (needed v^(-3-eps), actual at least beta/(1024 v^2)). PROVED.
- d = 3: the lower bound v^(-2) is below the needed v^(-1-eps) for eps <= 1. The zero mode does not obstruct. See Step 4 (c).

Check against the twist cost. Integrating, log K_v(X,Y) - log K_v(X, R_pi Y) has mixed part (beta/2) pi^2 n^(d-3)/v. In d = 4 this is (beta/2) pi^2 n/v >= 256 pi^2 beta: independent of n at fixed aspect. This is 't Hooft's Coulomb flux energy g^2 e^2/(2n) read through the Poisson sum. In d = 4 the estimate is exactly marginal at the free field.

ARGUED (not proved here): the matching upper bound sum_y |h(x,y)| <= c beta v^(-2) in every d. Reason: in the continuum the transverse mode k contributes beta |k| / sinh(|k| v) to the mixed block, so h(x,y) is of order beta v^(-d) on |x-y| <= v and decays like exp(-pi|x-y|/v) beyond; the cut has dimension d-2. A lattice proof needs the lattice Dirichlet-to-Neumann kernel; it is not needed for any verdict below except (c).

## Step 4. Test-model verdicts (the tests of `library/gap-mech-direction4-fable.md` 1.5, as corrected by check 1556)

"The same estimate" in a model of dimension d: sup over angles and x of sum over the opposite cut of E|mixed derivative| <= C v^(-(d-2)-eps), at fixed aspect n = 512u, v in {u/2,u}. By Lemma P2 it implies |log twist ratio| <= const * v^(-eps) at period 2v.

(a) **4D compact U(1), weak coupling: the estimate FAILS, with eps = 0 exactly.** PROVED for the free field (Corollary Z). ARGUED for Villain or Wilson U(1) at large beta: in the monopole-free Villain sector the twist ratio at angle pi is the theta-function ratio sum_k exp(-(beta/2)(pi + 2 pi k)^2 n/(2v)) / sum_k exp(-(beta/2)(2 pi k)^2 n/(2v)), with n/(2v) in {256, 512}; it is a fixed number below 1, not tending to 1. Monopole loops renormalise beta (Guth; Froehlich and Spencer, recalled, fixed boundary, not rebuilt; row 786 notes their result is not on periodic tori). The failing line l_1 is Lemma Z: the zero mode of the cut is not a gauge mode, and its stiffness beta n/v is scale invariant in d = 4.

(b) **5D SU(2), weak coupling: the estimate FAILS (BELIEF for the model; PROVED for its free part).** Free count: actual at least beta/(1024 v^2), needed v^(-3-eps). ARGUED: for the nonabelian field the abelian zero mode is not the cheapest twist carrier. The (0,1) twist forces anticommuting holonomies, and at weak coupling the cheapest carrier is a Z_2 interface of the short-direction Polyakov loop with area n^(d-2) and tension of order T^(d-2) g_eff^(-1), T = 1/(2v) (recalled from the deconfined-phase literature, GUIDE only). The cost is of order (n/v)^(d-2) g_eff(v)^(-1), which again is exactly the count n^(d-2) v^(-(d-2)) with eps = 0, times a factor that grows with v in d = 5 (g_eff^2(v) ~ g_5^2 / v). The failing line l_2 is the same: no decay of the stiffness beyond the scale-invariant count. No theorem (row 1531 found none).

(c) **Gapped twins.**
- 4D SU(2), strong coupling: the estimate HOLDS with an exponential rate. ARGUED (theorem recalled, not rebuilt): for alpha = 18 beta < 1 the Dobrushin interdependence matrix of the link field has row sums at most alpha uniformly in all boundary values (this is the bound of Theorem DOB, ON FILE, `library/gap-skeleton-final.md` 13.12, checked row 709). The Dobrushin-Kuensch-Foellmer covariance estimate then gives |Cov(f_x, g_y)| <= const * sum_{i,j} osc_i(f_x) D_ij osc_j(g_y), D = sum_k C^k, for every boundary condition, the wall R_s B included. A step of C moves the time coordinate by at most one, so sum_y |h| <= c beta^2 alpha^(v-2)/(1-alpha). The lines l_1, l_2 do not fire. The same holds in 5D at 24 beta < 1 and for U(1) at small beta.
- 3D compact U(1): the estimate HOLDS at the free-field level with eps = 1 and no gap input. ARGUED (Step 3 upper count: v^(-2) against the needed v^(-1-eps)); beyond the Debye length the Goepfert-Mack gap (recalled) can only help. So in d = 3 a pass does not read the gap. The line l_1 (Lemma Z) is true there and harmless.

Reading of (g3). The failure line (a scale-invariant stiffness of the cut's zero mode) fires in the gapless members and not in their small-beta twins. So the estimate reads the law, not the algebra or the dimension alone, in d >= 4. In d = 3 it is passed by a massless free field. For d = 4 it is exactly marginal at the Gaussian fixed point: eps > 0 is a statement beyond every finite order of scale-invariant counting.

(g5) scale: at fixed (n, v) and beta -> infinity the SU(2) twist cost grows (interface count of (b), order (n/v)^2 beta^(1/2); recalled, GUIDE), so BC with constants uniform in beta fails for beta -> infinity. This is the right behaviour: BC at coupling beta needs 2v above the deconfining time extent N_c(beta), which grows like exp(c beta). In the brief's window beta in [2,3], N_c is a fixed number (lattice folklore: about 4 at 2.30, 8 at 2.51, 16 at 2.74; recalled, GUIDE only), and BC is an asymptotic statement in v: for each v there are two values of n, so finitely many (n,v) cost only a constant, by |h| <= beta^2.

(g4) product with a neutral spectator: h is unchanged (Step 7). The estimate holds or fails as for pure SU(2). So BC alone can never be a sufficient condition for purity (Lemma ALG applies to any such use).

## Step 5. The necessary core of BC(eps): the flux half at the tested coupling. PROVED as implications

**(N-flux, eps).** There are C', eps > 0 such that for all beta in [2,3], n in 1024 Z, v in {u/2, u}, v >= 3:
  1 - Tr(P_0 T^{2v}) / Tr(T^{2v}) <= C' v^(-eps)   on the spatial torus n^3,
that is, the electric-flux-charged sectors carry at most the fraction C' v^(-eps) of the periodic thermal trace at period 2v.

- BC(eps) implies (N-flux, eps) with C' = (21/8) 2^19 pi^2 C. PROVED (Lemma P2 (f)).
- (N-flux, eps) implies every consequence listed in P2 (e)-(g) (with Z^z >= (1 - 2C' v^(-eps)) Z^0 from Z^z = sum_e (-1)^{z.e} W_e). PROVED, one line. So the consumer's use of BC reads (N-flux) only.
- (N-flux) does not imply BC. BC also asks for a pointwise, summable bound on a covariance in the pinned cylinder at every angle pair, the wall included (Step 6, A2). ARGUED: I have no model where (N-flux) holds and BC fails; the implication is simply not available.
- ON FILE: this is the flux half of `library/gap-skeleton-final.md` (Theorem F, Proposition T, open (TUBE'), lines 410; and line 555: "every twist ratio holds the flux half at most"). Theorem F is at a fixed transverse section. Here the section n x n grows with v, so Theorem F does not give (N-flux) from one seed; that is the open (TUBE') again.
- The free-field value (Step 3) shows what (N-flux) must beat: for flux energies g^2 e^2/(2n) (Coulomb) the charged fraction at period 2v ~ n/256 is a constant. (N-flux) holds as soon as the lowest odd-flux energy on the n^3 torus exceeds (c log n)/n for every c, with bounded multiplicity. ARGUED. So the gap between failing and holding is a logarithm in the flux energy, and no perturbative order supplies it.
- Through the Tomboulis-Yaffe inequality (Kanazawa Theorem 1, ON FILE row 690, recalled, not used as a proof step) (N-flux) bounds the largest planar Wilson loop of the (0,1) plane by 2 (C' v^(-eps)/2)^(A/(2vn)). So BC(eps) at beta in [2,3] contains a confinement statement at order-one coupling. No converse (decay of loops gives (N-flux)) is on file.

## Step 6. Three attacks on BC(eps) for 4D SU(2) at beta in [2,3]. None closes

**A1. Mixing uniform in the boundary (Dobrushin; Dobrushin-Shlosman).** This is the only method here that handles the sup over the angles, because its constants do not read the boundary values. It proves BC with an exponential rate for 18 beta < 1 (Step 4 (c), ARGUED). First failing step at beta in [2,3]: the row sum of the interdependence matrix is bounded only by 18 beta >= 36. The finite-box form (Dobrushin-Shlosman 1985, 1987; NOT READ in the lane, `library/gap-skeleton-final.md` lines 254, 371) would need one verified box condition, uniform in all boundary values, at a box side above the correlation length at beta = 3. That premise implies a unique state with exponential clustering at the tested coupling. It is stronger than the seed there, and no exact computation of that size is specified. Verdict: fails; premise not weaker than the seed at the tested coupling.

**A2. Transfer-operator expansion.** With T psi_j = lambda_j psi_j on the n^3 slice and phi_j = psi_j/psi_0: log K_v(X,Y) = v log lambda_0 + log psi_0(X) + log psi_0(Y) + log(1 + r_v(X,Y)), r_v = sum_{j>=1} (lambda_j/lambda_0)^v phi_j(X) phi_j(Y). The first three terms have zero mixed derivative. So h = D_x D_y log(1 + r_v). PROVED (algebra). Three failures, in order:
 (i) The norm of r_v in L^2(psi_0^2 x psi_0^2) is exactly the full thermal sum S(2v; n^3; beta)^(1/2). So the first bound this route needs is the full seed at the tested coupling. Equivalent is not progress.
 (ii) BC evaluates h at X = R_s B. R_s preserves Haar but not the slice law: at angles away from 0 and pi it changes the 2 n^2 spatial plaquettes on the cut (each cut link lies in four, each plaquette holds two cut links), so the density of the law of R_s B against the law of B is of order exp(+-c beta n^2) (bounded by exp(4 beta n^2) on the local terms; ARGUED for the size). An L^2 bound of size exp(-m v) cannot pay it, because n^2 = (512 u)^2 >> v. So even a proved mass gap of T at beta in [2,3] does not give BC by this route. This is the main structural finding on the statement as written: the sup over (s,t) asks for mixing on a wall of n^2 excited boundary plaquettes, which is not a spectral statement.
 (iii) The sum over y needs locality of D_x phi_j and D_y phi_j, which the spectrum does not hold.
 Remark (a path that avoids the wall does not exist in this class). Moving the cut links one at a time replaces the wall by a line of about n flipped boundary plaquettes; exp(c beta n) is still not paid by exp(-m v).

**A3. A signed stiffness, as in the OpenAI authors' pinned-spin proof.** If h had one sign, then sum |h| = |sum h| and BC would follow from a bound on d_s d_t log K_v(R_s X, R_t Y), the stiffness of the cut. First failing step: no sign. h is a covariance of two traces against frozen axes (P1); SU(2) lattice gauge fields have no Ginibre-type inequality for it, and check 1556 (vi) (ON FILE) finds no ferromagnetic conditional model in the three natural coordinates. Second failing step, independent of the first: with a sign, BC is the bound stiffness <= C n^2 v^(-2-eps), whose angle integral is (N-flux) itself. The free field has exactly the marginal stiffness beta n/v (Lemma Z). A perturbative improvement is a power of log v at most (running coupling; GUIDE). So A3 reduces BC to (N-flux) and adds no means for it.

Direct means for (N-flux) tried: reflection positivity gives only Z^z <= Z^0 (the free direction). Theorem F needs a fixed section. The energy bound gives |log(Z^{z+e_1}/Z^z)| <= 2 beta n^2 (flip the n^2 plaquettes), which is the count with no decay at all.

**The one precise lemma where this stops: (N-flux, eps)** above, at beta in [2,3]. It is necessary for BC(eps), sufficient for every stated use of BC(eps), false for the 4D free field at every eps > 0 by an exact identity, and true at 18 beta < 1. It was attacked by A1 (uniform mixing: premise stronger than the seed), A2 (spectral: premise is the full seed, and the wall is not paid) and A3 (signed stiffness: no sign, and it returns (N-flux)).

## Step 7. Why BC(eps), and (N-flux), are not equivalent to (PUR-io); what else is needed

(PUR-io) (ON FILE, `library/gap-k2-tool-design-fable.md` line 119): P_K = Z_+(2u)/Z_+(u)^2 >= 457/625 at infinitely many K, at the release couplings beta_K, n = l b^K.

- BC does not imply purity, at any coupling. Spectator (check 1556 line 110, re-derived): for the product with a neutral factor, K_v = K_v^W x K_v^m, the cut rotation acts on the Wilson factor only, so log K_v splits into a sum and the mixed derivative D_x^(1) D_y^(2) log K_v is that of the Wilson factor. The joint law is a product, so the left side of BC is unchanged. Purity becomes P_W P_m, and P_m can be arbitrarily small (a seedless spectator; check 1556 (iii)). PROVED. Inside pure SU(2) the same blindness shows in P2 (g): BC compares P_K with P_full and bounds neither. One light neutral level destroys both and changes no twist ratio.
- Purity does not imply BC or (N-flux). P_K reads the neutral sector only; the charged sectors do not enter it. Seven almost degenerate charged levels (check 1550's example, cited in check 1556 (ii)) leave P_K = 1 and make the charged fraction 7/8. PROVED on transfer data.
- So BC and (PUR-io) are incomparable, and BC is not a rewriting of the seed either. But its consequence is contained in the full seed at the tested coupling: sum_{e != 0} W_e(2v)/Z^0(2v) <= S(2v; n^3; beta). So BC is not a weaker route to anything the full seed would not give. Honest status under the rule "Equivalent is not progress": not equivalent, and no gain shown.
- What BC would add if proved: it reduces the consumer's sixteen masses to two at the tested coupling, by P2 (g).
- Further input needed for (PUR-io), unchanged by this row: (1) the common neutral normalisation across the two periods, that is Z^0(2u)/Z^0(u)^2 >= (457/625)(1 + O(u^(-eps))) on the untwisted tori, which is the full periodic purity and hence the seed-type statement at the tested coupling (P_full <= 1/(1+S)); (2) the carry from beta in [2,3] to the release roots beta_K (registry R12; A1 of check 1556 (viii) is the separate ultraviolet comparison).

## Step 8. Verdict on the statement as written, and two repairs to its wording (unproved suggestions)

- BC(eps) for 4D SU(2) at beta in [2,3]: NOT PROVED, NOT REFUTED. A refutation would need the charged fraction to stay bounded below along v -> infinity at some beta in [2,3], which contradicts the expected confinement there; no estimate the other way exists.
- Repair 1: replace BC by (N-flux) as the band lemma. It is weaker, it is all the consumer reads, and it drops the wall (A2 (ii)).
- Repair 2: if a covariance form is wanted, state it at the corners only (s, t in {0, pi}) for a quantity whose corner values suffice. The sup over the open angle square is the part no spectral input can reach.

## Step 9. Self-check of the proved steps (same model, not an independent check)

Re-read after writing: P1 (support and the bound |tr(aM)| <= 2); P2 (c) (sign of the KL identity; rho_{z+e_1} = 1/rho_z as a function of (A,B)); P2 (f) (1 - (1/8) sum_z Z^z/Z^0 = (1/8) sum_{z != 0} (1 - Z^z/Z^0)); P2 (g) (period 2u uses v = u, period u uses v = u/2, so u >= 6); Lemma Z step (2) (the gauge function) and step (3) (n^(d-1) plaquettes per layer, field strength (s-t)/(n v)); the count of wall plaquettes (corrected from 4 n^2 to 2 n^2). No numeric run was made. Nothing here is checked by another model. Labels: PROVED means a written argument in this file; ARGUED means a reasoned step with a recalled theorem or a continuum count; GUIDE/BELIEF items carry no weight.

RESULT: BC(eps) for 4D SU(2) at beta in [2,3] is neither proved nor refuted; it stops at one precise lemma, (N-flux, eps): the flux-charged fraction 1 - Tr(P_0 T^{2v})/Tr(T^{2v}) on the n^3 torus is at most C' v^(-eps), which BC(eps) implies (PROVED, C' = (21/8) 2^19 pi^2 C, with a Kullback-Leibler bound between the two twisted boundary laws) and which is all the consumer reads; attacked three ways without closure (uniform Dobrushin mixing: only 18 beta < 1; transfer expansion: its first bound is the full seed and no spectral gap pays the exp(c beta n^2) wall that the sup over angles creates; signed stiffness: no sign, and it returns (N-flux)). Test models: free Maxwell, exact zero-mode identity sum_y h = beta/(n v) in every dimension (PROVED), so the estimate FAILS in 4D for every eps > 0 (exactly marginal, the lead's v^(-2) count confirmed as a lower bound beta/(1024 v^2)) and fails by a power in 5D; 4D compact U(1) weak FAILS (ARGUED beyond the free part); 5D SU(2) weak FAILS (BELIEF); 4D SU(2) strong coupling HOLDS exponentially (ARGUED from the on-file Dobrushin bound); 3D compact U(1) HOLDS already at free-field level with eps = 1, so in d = 3 it does not read the gap. What BC would give (PROVED as an implication): twist ratios within 3 delta_v and (1 - (21/8) delta_u) P_full <= P_K <= P_full/(1 - (21/8) delta_{u/2})^2 at the tested coupling only; it is incomparable with (PUR-io) (spectator and charged-level examples), its consequence is contained in the full seed, so no gain over the seed is shown. Open: (N-flux) at beta in [2,3], the wall-uniform covariance bound if BC is kept as written, the untwisted two-period purity, and the carry to the release roots (R12).
