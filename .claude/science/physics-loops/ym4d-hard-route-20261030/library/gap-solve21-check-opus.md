lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T13:37Z

# Check of row 1204 (`library/gap-solve21-astra62.md`), queue row 1210

Cross-provider check: the author is gpt-6.2-astra max (row 1204), the checker is Claude Opus 5.5 max on the Mac mini
Claude worker. Pinned at commit 5e5082e7c. Started 2026-11-20T01:37Z (date -u).

Scope (row 1210): check line by line, by hand, positive claims first: the relativistic mass test (1), the strip bound
(8), the Wilson contact and infrared estimates (21), (26), (32)-(35), the axial-packet exclusion (36); then everything
else. For each cited earlier row, read the cited statement and its proof where the step depends on it. Verdicts:
HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line. Numerics guide only.

## Plan (at most eight steps; one step per response, appended as done)

1. Read the checked file in full; inventory its labelled statements with line numbers; list cited earlier rows.
2. Check (1), the sharp relativistic mass test, and what it rests on.
3. Check (8), the strict strip bound.
4. Check (21) and (26), the Wilson contact and infrared estimates.
5. Check (32)-(35).
6. Check (36), the exclusion of axial plaquette packets.
7. Check everything else, and the cited statements of earlier rows where a step depends on them.
8. Verdict table and RESULT line.

## Status log

- 2026-11-20T01:37Z: file created; step 1 next.
- 2026-11-20T01:56Z: steps 1-8 done; RESULT line written at the end of the file.

## Step 1. Inventory of the checked file (done 2026-11-20T01:38Z, date -u)

`library/gap-solve21-astra62.md` at the pinned commit: 437 lines, 75,012 bytes, read in full. Labels: 6 GUIDE paragraphs
(L3, L5, L7, L13, L46, L109), 5 OPEN paragraphs (L9, L42, L140, L386, L435), and 61 PROVED paragraphs, which I group into
60 statements S1-S60 in file order (S1 = the two paragraphs L15 and L30; every other S is one paragraph). Each verdict
below gives the S-number, the line and the equation.

| S | lines | content |
|---|---|---|
| S1 | L15-30 | (1) norm of B_h = Q(hM) in a relativistic vacuum representation |
| S2 | L32-40 | q_0 = e^{-pi/2}/2, strict threshold, (2) |
| S3 | L48-61 | PL5 dispersion E >= g(abs eta); (3) B^(k) <= b_k; (4) b_k asymptotics |
| S4 | L63-71 | (5) concentration near x_0 = pi/2 |
| S5 | L75-92 | two perpendicular reflections, (6) |
| S6 | L94-99 | (7) quantitative deficit |
| S7 | L101-107 | (8) strict strip bound (same-time spatial sources, R(F) <= 1) |
| S8 | L113 | strip functions are a proper subspace (one-link variance, row 1173 (8)) |
| S9 | L115-126 | (9) lower bound on the transverse numerator for alternating plaquette sums |
| S10 | L128-138 | (10), (11) R(F) unbounded at the mirror through the source |
| S11 | L144-154 | (12) three reflected correlations give the continuum ratio |
| S12-S13 | L156, L158 | totality of box vectors under the Wightman hypotheses |
| S14 | L160 | abelian time-zero strip algebras are not cyclic |
| S15 | L162 | shell (conditional-integral) representation |
| S16-S17 | L166-172 | free Maxwell singlet approaches q_0 with deficit O(A^-2) |
| S18 | L174-179 | (13) spectral representation of A_0/abs(x)^8 |
| S19 | L181-186 | (14) l^{-9/2} power law for the free action density |
| S20-S21 | L190-197 | (15) momentum projection of strip subspaces |
| S22 | L199-205 | (16) delocalization |
| S23 | L209-214 | (17) |
| S24-S25 | L216-223 | (18) full-space test and its finite Wilson form |
| S26 | L225-229 | (19) small-h expansion of Q |
| S27 | L231-235 | (20) |
| S28-S29 | L239-246 | (21) contact identity for the cube transfer and its proof |
| S30 | L248-253 | (22) |
| S31 | L255-260 | (23) |
| S32-S34 | L264-277 | (24) free lattice singlet comparison, lower edge g(abs eta) |
| S35 | L281 | padding gives R = 1 |
| S36-S37 | L283-289 | (25), no common reflection-norm bound |
| S38-S39 | L293-300 | (26) second-moment contact identity |
| S40-S41 | L302-308 | (27) and its compatibility with (24) |
| S42-S45 | L312-326 | (28), (29) all-momentum neutral weight on a cube |
| S46-S48 | L330-348 | (30) thermal transition measure, first exponential moment |
| S49 | L350-358 | (31) |
| S50 | L362-366 | (32) infrared domination in the four-cube limit |
| S51 | L368-376 | (33) |
| S52 | L378-384 | (34) |
| S53-S55 | L390-399 | (35) and the exact contact in the limit state |
| S56-S58 | L403-422 | (36) axial plaquette packets and its consequence |
| S59 | L426 | Euclidean Gram lower bound in four directions |
| S60 | L428-433 | bounded real-frequency density of the massless singlet |

Cited sources a step depends on (to be read where needed): row 1161 `gap-solve9-astra62.md` (18)-(20), the one-link
conditional variance c_0 and the inverse estimate, with its check `gap-solve9-check-opus.md` (S21-S24); row 1173
`gap-solve15-astra62.md` (8); the outline's PL4-PL7 (lines 3260-3427) and GL3-GL7 (lines 2224-2311) by Sussman and
Alpoge, via `sa-index/chunk-02.md`, `chunk-03.md`; PH1 Lemma 2 `ph1.md`; outline lines 1601-1624 (free curvature);
outline F2/F3 lines 4289-4314, 4360-4374; `gap-neutral-chain-check-astra.md`; row 977 `gap-tiltproof-max.md` 5.3.

## Step 2. The relativistic mass test (1), (2) and its expansion (19), (20) (done 2026-11-20T01:39Z, date -u)

**S1, L15-30, (1): HOLDS.** Checked by hand.
- Multiplier: (1/4)|1 - e^{i h p_1}|^2 e^{-hE} = (1/2)(1 - cos(h p_1)) e^{-hE} = sin^2(h p_1/2) e^{-hE}, as written.
- Norm: for a bounded continuous function b of the commuting generators, the norm of b(H, P) is the essential supremum
  of b under the joint spectral measure, which equals sup over the closed support Sigma because b is continuous. Correct.
- Orbits: covariance U(L) e^{i a.P} U(L)^* = e^{i (L a).P} gives E(L Delta) = U(L) E(Delta) U(L)^*, so Sigma is
  Lorentz invariant. In the closed forward cone E = 0 forces p = 0, so every point of Sigma minus 0 lies on a mass
  hyperboloid (mu > 0) or on the null cone minus 0, and contains (sqrt(mu^2 + (x/h)^2), (x/h, 0, 0)) for every x >= 0
  (x > 0 on the null cone). At fixed p_1 the transverse momentum only raises E; folding h|p_1| into [0, pi] keeps
  sin^2 and lowers E. So the supremum on the orbit of mass mu is Q(h mu); on the null cone the maximiser x = pi/2 > 0
  is admissible, so the value is Q(0).
- Q is the maximum over a compact x-interval of a jointly continuous function, so it is continuous; it is
  non-increasing in y because sqrt(x^2 + y^2) is. Hence sup over the masses in Sigma of Q(h mu) = Q(h M). The origin
  contributes 0. No step uses a discrete mass shell.

**S2, L32-40, q_0 and (2): HOLDS.** d/dx log(e^{-x} sin^2(x/2)) = cot(x/2) - 1, which is strictly decreasing and
vanishes only at x = pi/2; value e^{-pi/2} sin^2(pi/4) = e^{-pi/2}/2. For y > 0, at the maximiser x_y of Q(y) the
value is positive, so sin^2(x_y/2) > 0 and Q(y) = e^{-sqrt(x_y^2+y^2)} sin^2(x_y/2) < e^{-x_y} sin^2(x_y/2) <= q_0.
For (2): Q(y) >= (1/2) e^{-sqrt(pi^2/4 + y^2)} (value at x = pi/2), so Q(hM) <= q_0 e^{-delta} gives
pi/2 + delta <= sqrt(pi^2/4 + (hM)^2), i.e. (hM)^2 >= pi delta + delta^2. Correct. The edge statements: every point of
Sigma minus 0 has E >= sqrt(E^2 - |p|^2) >= M, and each orbit contains its rest point, so inf spec(H) on the complement
of the zero four-momentum space is exactly M. B_h annihilates that zero space, so (1) says nothing about vacuum
multiplicity; the file says so (L40). The empty case (Sigma = {0}) is excluded by the hypothesis on L15.

**S26, L225-229, (19): HOLDS.** With log f(x, y) = log sin^2(x/2) - sqrt(x^2 + y^2) and
sqrt(x^2 + y^2) = x + y^2/(2x) + O(y^4) uniformly for x in a neighbourhood of pi/2: the lower bound
log(Q(y)/q_0) >= -y^2/pi + O(y^4) is the value at x = pi/2. The critical equation cot(x/2) = x/sqrt(x^2+y^2) and the
non-degenerate maximum of log f(., 0) (second derivative -1/2 at pi/2) give x_y = pi/2 + O(y^2); then
log f(x_y, y) <= log q_0 - y^2/(2 x_y) + O(y^4) = log q_0 - y^2/pi + O(y^4). Uniform convergence keeps the maximiser
near pi/2 for small y (the maximiser of f(., 0) is strict and unique on [0, pi]). The remark about a running coupling is
labelled as a hypothesis, which is correct.

**S27, L231-235, (20): HOLDS as a conditional corollary of (7)** (verdict on (7) in Step 3). If the Wilson ratio is
within C_1 (hM)^2 of q_0 and k^{-2} = o((hM)^2), then with b_k = q_0(1 + O(k^{-2})) from (4) the left side of (7) is
at most C_2 (hM)^2, and (7) gives [1 + D/k + log(2 + R(F))]^2 >= c/(C_2 (hM)^2). Note that by (1) and (19) a normalised
continuum state can come no closer than q_0 (hM)^2/pi + O((hM)^4) to q_0, so the hypothesis needs C_1 >= 1/pi; the
file's "c depends on the constant in the approximation" covers this. The sentence "Boosting to weak coupling changes
momentum and energy together" (L235) is commentary, not a step.

## Step 3. The strict strip bound (8) and what it rests on: (3)-(7) (done 2026-11-20T01:41Z, date -u)

Sources read: outline lines 3190-3440 (setting, PL1-PL7 and the proof of PL5; fetched by raw URL at commit
31a47c543775 into a scratch folder), `ph1.md` L43 (import LG1) and L84-131 (Lemma 2, the port of PL4-PL5),
`lg1.md` status lines 475, 485 (frozen; no Outstanding step; not refereed as a whole part).

**Premise of S3-S7 (GUIDE L46).** The state is a translation-invariant measure on the infinite lattice with
reflection positivity on the closed side of every coordinate mirror x_mu = c, c in Z/2, and every diagonal mirror
x_mu +- x_lambda = c, c in Z (outline L3201-3214; reflections act by pullback without complex conjugation). For periodic
Wilson DLR states this is LG1 (`ph1.md` L43), frozen in `lg1.md`; PL4 and PL5 for such laws are PH1 Lemma 2. The file
states the premise correctly and the outline's warning that a torus law lifted periodically is outside the domain
(outline L3204-3205). So "PROVED (from PL5)" means proved by hand from a ported, frozen import, which is how the lane
uses LG1 elsewhere. No objection.

**S3, L48-61, (3), (4): HOLDS.**
- PL5 (outline L3311-3318) is cosh E + cos eta >= 2, i.e. 2 sinh^2(E/2) >= 2 sin^2(eta/2), i.e.
  E >= 2 arsinh|sin(eta/2)| = g(|eta|); kappa = (2/pi) log(1 + sqrt 2) = 2 arsinh(1)/pi as the file writes.
- Multiplier of B^(k): e^{-kE} |1 - e^{ik eta}|^2/4 = e^{-kE} sin^2(k eta/2) <= e^{-k g(|eta|)} sin^2(x/2) with
  x = arccos(cos(k eta)) in [0, pi], x <= k|eta|; g is increasing on [0, pi], so g(|eta|) >= g(x/k), giving (3).
  The kernel of T (E = infinity) gives 0.
- Expansion: sin(t/2) = t/2 - t^3/48 + O(t^5), arsinh u = u - u^3/6 + O(u^5), so g(t) = t - t^3/12 + O(t^5); hence
  k g(x/k) = x - x^3/(12 k^2) + O(k^-4) uniformly on [0, pi]. The log-derivative is cot(x/2) - g'(x/k) with
  g'(t) = 1 - t^2/4 + O(t^4), and d/dx cot(x/2) = -1 at pi/2, so every maximiser is pi/2 + O(k^-2); the value is
  log q_0 + (pi/2)^3/(12 k^2) + O(k^-4) = log q_0 + pi^3/(96 k^2) + O(k^-4). (4) is correct. b_k >= q_0 because
  arsinh u <= u and sin s <= s give g(t) <= t.

**S4, L63-71, (5): HOLDS.** Write the multiplier as e^{-k g(|eta|)} sin^2(k eta/2) e^{-k(E - g)} with E - g >= 0 by PL5.
On x = k|eta| <= pi: log(e^{-x} sin^2(x/2)) has second derivative -(1/2) csc^2(x/2) <= -1/2 and zero derivative at
x_0, so it is <= log q_0 - (x - x_0)^2/4; with k g(x/k) >= x - pi^3/(12 k^2) - O(k^-4) the multiplier is
<= q_0 e^{C/k^2} e^{-Z}, Z = (x - x_0)^2/4 + k(E - g). On x > pi: |eta| > pi/k, so kE >= k g(pi/k) = pi - O(k^-2) and
the multiplier is <= e^{-pi + C/k^2} <= q_0 (1 - c_1) for k >= K, since e^{-pi} = 0.0432 < q_0 = 0.1039. Integrating,
q_0(1 - d) <= <v, B v> gives e^{C/k^2} int_{x<=pi} (1 - e^{-Z}) dmu + (c_1 + e^{C/k^2} - 1) mu{x > pi}
<= d + (e^{C/k^2} - 1), and 1 - e^{-Z} >= (1 - e^{-1}) min(1, Z) >= (1 - e^{-1}) min(1, (x-x_0)^2 + k(E-g))/4. This is (5).

**S5, L75-92, (6): HOLDS.** With F supported in 0 <= x_1 <= D: theta_0 F has the same x_1-range, tau_{-D} theta_0 F has
-D <= x_1 <= 0, and L_F = theta_1 tau_{-D} theta_0 F has 0 <= x_1 <= D, so both L_F and F are on the closed positive side
of x_1 = 0. By PL4 in direction 1 with s = w - D >= 0:
<[L_F]_1, S^{w-D} [F]_1>_1 = nu(conj(theta_1 L_F) tau_{(w-D) e_1} F) = nu(conj(tau_{-D} theta_0 F) tau_{(w-D) e_1} F)
= nu(conj(theta_0 F) tau_{w e_1} F) (translation invariance) = <Phi, U^w Phi>_0 (PL4 in direction 0). Every exponent
w_0 + 2kj, 0 <= j <= m, is >= D, so the polynomial transfers term by term to <[L_F]_1, S^{w_0-D}(1 - S^{2k})^m 2^{-m} [F]_1>_1,
and s^{w_0-D}(1 - s^{2k})^m lies in [0, 1] on spec S in [0, 1]. Hence (6).

**S6, L94-99, (7): HOLDS.** Checked each step: d = (1 - <B>/q_0)_+ <= gamma because b_k >= q_0 and gamma >= k^-2; on
x <= pi, (x - x_0)^2 <= (pi^2/4) min(1, (x - x_0)^2), so int_{x<=pi} (x - x_0)^2 dmu <= C gamma and mu{x > pi} <= C gamma;
w_0 = 4k ceil(D/(4k)) >= D is a multiple of 4k, so e^{i w_0 eta} = 1 and (1 - e^{2ik eta})/2 = 1 at k eta = +-pi/2; the
two Lipschitz bounds and |z^m - 1| <= m|z - 1| on the unit disc give |int phi dmu - 1| <= (w_0/k + m) (C gamma)^{1/2}
+ 2 C gamma <= C(1 + w_0/k + m) gamma^{1/2} for gamma <= 1; with m = ceil(log_2(2 + 2R)), (6) gives
|int phi dmu| <= R/(2 + 2R) < 1/2. Since w_0/k <= D/k + 4 and m <= C log(2 + R), (7) follows (gamma > 1 is trivial
with c <= 1).

**S7, L101-107, (8): HOLDS.** For F reading only spatial bonds in the slice x_0 = 0, theta_0 F = F (pullback fixes these
bonds with their orientation), so ||Phi||^2 = nu(|F|^2); ||[F]_1||^2 = nu(conj(theta_1 F) F) <= ||F||_2^2 by Cauchy-Schwarz
and reflection invariance (outline L3263-3270; PH1 Lemma 2 "||[F]|| <= ||F||_2"), and likewise ||[L_F]_1|| <= ||F||_2.
So R(F) <= 1. Then (7) with D <= Ak gives ratio <= b_k (1 + k^-2 - c/(1 + A + log 3)^2), and b_k -> q_0 by (4), with
(1 + A + log 3) <= (1 + log 3)(1 + A). The constants of (5)-(7) are numerical and depend on the state only through
PL4-PL5, so the supremum over F and over states (any coupling) is legitimate. The tail sentence (R(F) >= exp(c''/sqrt
gamma) for fixed D/k) is (7) solved for R. Scope as stated: local F (finitely many bonds) at time zero in a strip of
lattice width D <= Ak; the bound says nothing about vectors outside the closed span of such F (the file says so, L109,
L140, and proves at S14 that this span cannot be total).

## Step 4. The Wilson contact identities (21), (26) and their first consequences (22), (23), (27) (done 2026-11-20T01:44Z, date -u)

Sources read: outline GL3-GL7 (L2205-2311: c_l, the ratio bounds GL4, the finite-band series GL5 for
f-hat = C^{-1} M_f C on smooth functions, its formal adjoint, GL6 C f-hat = M_f C, GL7, and "operators acting on
disjoint variable sets commute"); row 1161 `gap-solve9-astra62.md` L229-311 (Gram bound, (18), the band proof of
(20), c_0 = 1/4); row 1162's verdicts on these: S20, S21 (18), S23 (c_0), S24 (20) all HOLD
(`gap-solve9-check-opus.md` verdict table).

**S28-S29, L239-246, (21): HOLDS.** Setting as in row 1161: T = DCD/lambda on a periodic spatial cube, D a bounded
strictly positive multiplication (so D^{-1} is bounded at fixed volume), C = tensor product of the one-link
convolutions with c_l > 0 (GL3), psi > 0 the simple top eigenvector, v = D psi, D^{-1} psi = C v/lambda.
- Inverse form: sup_z (2 Re<u, z> - <z, DCD z>) with y = Dz equals ||C^{-1/2} D^{-1} u||^2, so
  <T^{-1/2} f psi, T^{-1/2} g psi> = lambda <C^{-1/2} D^{-1} f psi, C^{-1/2} D^{-1} g psi>
  = lambda^{-1} <C^{-1/2} f C v, C^{-1/2} g C v>, as the file writes (f, D commute).
- Boundedness: on the links of f, the block (in -> out) of C^{-1/2} f C has weight r_out^{-1/2} r_in
  = r_in^{1/2} (r_in/r_out)^{1/2}; the degree shift is bounded, the ratio is polynomial by GL4, r_in^{1/2} decays
  factorially, and the exterior factor is C_ext^{1/2}. So C^{-1/2} f C is bounded on the fixed cube; in particular
  f psi is in the form domain of T^{-1}.
- Identity: for finite Peter-Weyl sums w, w', <C^{-1/2} f C w, C^{-1/2} g C w'> = <w, C f C^{-1} g C w'>, and with
  C = C_A x C_B x C_ext, C f C^{-1} g C = (C_A f) x (g C_B) x C_ext = g C f. Both sides are continuous in (w, w')
  (bounded operators), so the identity extends to v: the mixed form is lambda^{-1} <v, g C f v>
  = lambda^{-1} <f v, C g v> (all objects real) = <f psi, T g psi>. Subtracting a constant from f or g keeps
  C f C^{-1} g C = g C f. Gauge invariance is only needed to stay in the physical space (C commutes with gauge action).
  (21) is an exact finite-cube identity.

**S30, L248-253, (22): HOLDS.** 23-plaquettes at different x_1 have disjoint links, so (21) with f = f_0, g = f_x gives
<u_0, (T^{-1} - T) V^x u_0> = 0 for x != 0 mod n. On Z/n the measure eta -> int 2 sinh E dmu(E, eta) therefore has
Fourier coefficients d_{beta,n} delta_{x,0}, hence is the constant d_{beta,n}/n. Integrability of e^E is the domain
statement above; T is injective (c_l > 0, D invertible), so there is no atom at E = infinity; E >= 0 since T <= 1.

**S31, L255-260, (23): HOLDS.** g_p = T_d(W_p) (Chebyshev) has degree <= d in each of the four links and |f| <= 2, so
(20) gives d_{beta,n} <= <u_0, T^{-1} u_0> <= C_A^4. Gram bound: selecting one edge on each plaquette of one parity of
x, no action plaquette (spatial or temporal) contains two selected edges (a plaquette spans one unit of x_1), the
readings of the other parity are measurable for the conditioning, and the selected readings are conditionally
independent with conditional variance >= c_0 (row 1161 L273-281, S23 of row 1162); total variance and the long-cylinder
limit (trace-class positive transfer, simple top eigenvalue) give ||sum z_x u_x||^2 >= (c_0/2) sum |z_x|^2. With
z_x = e^{-i x eta}/n the vector is the projection of u_0 on V = e^{i eta}, so mu_eta(total) >= c_0/(2n), while
mu_eta(E > E_*) <= (C_A^4/n)/(2 sinh E_*) = c_0/(4n) for E_* = arsinh(2 C_A^4/c_0). Centering and the simple vacuum
remove E = 0. Correct as stated, including eta = 0.

**S38-S39, L293-300, (26): HOLDS.** Checked each step.
- T A_f = f T on smooth functions: T A_f phi = lambda^{-1} D C f-hat D phi = lambda^{-1} D f C D phi (GL6) = f T phi;
  D^{+-1} = exp(smooth) preserve smooth functions; psi is smooth (lambda psi = DCD psi, smooth kernel of C). So
  T A_f psi = f psi and, by injectivity, T^{-1} f psi = A_f psi in L^2.
- A_f^dagger = D f-hat^dagger D^{-1} is the formal adjoint on smooth functions (GL5 adjoint series); for smooth chi,
  <chi, A_f^dagger T phi> = <T A_f chi, phi> = <chi, T f phi>, so A_f^dagger T = T f on smooth functions and
  T f psi = A_f^dagger psi.
- Commutation: factors of D from plaquettes not meeting S_f do not depend on the S_f variables and cancel, so
  A_f = D_f^{-1} f-hat D_f with D_f the product over plaquettes meeting S_f; likewise for g. If no spatial plaquette meets
  both sets, D_g does not depend on S_f variables and D_f not on S_g variables (a spectator of f lying in S_g would put a
  plaquette in both sets), f-hat^dagger and g-hat act on disjoint variables, and shared spectators are parameters. So
  A_f^dagger A_g = A_g A_f^dagger on smooth functions, and
  <A_f psi, A_g psi> = <psi, A_f^dagger A_g psi> = <psi, A_g A_f^dagger psi> = <A_g^dagger psi, A_f^dagger psi>
  = <T g psi, T f psi>, real. (26) holds. Sanity check: with D = 1 both sides of (26) equal <f><g>.

**S40, L302-306, (27): HOLDS.** A spatial plaquette meets links of two parallel 23-planes only if their x_1 differ by at
most one, so by (26) the coefficients of int 2 sinh(2E) dmu at displacement x vanish for x not in {0, +-1} (n >= 4).
The two remaining coefficients are real and equal by reality and reflection x -> -x with translation invariance;
Fourier inversion on Z/n gives n int 2 sinh(2E) dmu_eta = a + 2b cos eta. e^{2E} is integrable since
||T^{-1} u_0|| = ||A_f psi|| < infinity. d_{beta,n} > 0 since psi > 0 a.e. makes f psi != 0 and the vacuum is simple.
Since 2 sinh E cosh E = sinh 2E and n int 2 sinh E dmu_eta = d_{beta,n} by (22), the mean of cosh E under the stated
probability measure is (a + 2b cos eta)/(2 d_{beta,n}). Correct.

## Step 5. The infrared estimates (30)-(35) (done 2026-11-20T01:47Z, date -u)

Inputs: (21) and its per-eigenvector form (Step 4); row 1161's band proof of (20) and its positive-kernel estimate
(`gap-solve9-astra62.md` L283-304, checked HOLDS as S24 of row 1162); PL5 with all three tangential directions
(outline L3311-3318, "E >= kappa |eta|_infinity").

**S46, L330-340, (30) definitions and detailed balance: HOLDS.** Total mass (1/Z) sum_a lambda_a^L ||f e_a||^2 <= 4.
Moments: on the n^3 x L torus, Z = Tr(P_gauge F^L) and nu_{L,n}(f tau_{t e_0 + x} f) = (1/Z) sum_{a,c} lambda_a^{L-t}
lambda_c^t |f_{ca}|^2 e^{i (P_c - P_a).x}, which is int e^{-tE + iP.x} drho with E = log(lambda_a/lambda_c). Swapping
a, c sends the atom (E, P) to (-E, -P) and multiplies its weight by (lambda_c/lambda_a)^L = e^{-LE}. Complex
conjugation commutes with F (real kernel), with real f and with translations, and reverses momenta; rho is basis
independent, so rho(dE, -dP) = rho(dE, dP).

**S47-S48, L342-348, first bound of (30): HOLDS.** int e^E drho = (1/Z) sum_a lambda_a^{L+1} <f psi_a, F^{-1} f psi_a>
(any eigenbasis of F), and D^{-1} psi_a = C v_a/lambda_a gives <f psi_a, F^{-1} f psi_a> = lambda_a^{-2}
||C^{-1/2} f C v_a||^2, hence the displayed Z^{-1} sum_a lambda_a^{L-1} ||B_f v_a||^2. Row 1161's band estimate is an
operator inequality B_f^* B_f <= C_A^b C prod_e exp(C_A l_e/sqrt beta) <= (4 C_A)^b C prod_e m_{l_e}(y) =: K (both are
functions of the commuting degree operators and C; m_l(y) >= e^{ly/2}/4). The kernel of K is a product of Haar-averaged
complex-shifted Wilson kernels; I re-derived Re tr(g V H_y V^{-1})/2 = cosh(y) tr(g)/2 for g in SU(2) (the sinh-part
is i a.n), so |K(u,v)| <= (4 C_A e^{beta(cosh y - 1)})^b C(u,v) =: K_A^b C(u,v), with beta(cosh y - 1) bounded for
y = 2 C_A/sqrt beta, beta >= 1. Then sum_a lambda_a^{L-1} <v_a, K v_a> = Tr(K M), M = D F^{L-1} P_gauge D with a
nonnegative continuous kernel (L - 1 >= 1); Tr(K M) <= int int |K(u,v)| M(v,u) <= K_A^b Tr(C D F^{L-1} P_gauge D)
= K_A^b Tr(F^L P_gauge) = K_A^b Z. Correct; no sign of an excited eigenfunction is used.

**S49, L350-358, (31): HOLDS.** On E < 0, rho(-E', P) = rho(-E', -P) = e^{-LE'} rho(E', P) (both symmetries of (30)),
so the signed integral of 2 sinh E at momentum P is W_{L,n}({P}); total mass <= int e^E drho <= K_A^b. The Fourier
coefficient at displacement x is (1/Z) sum_a lambda_a^L [<f psi_a, (F/lambda_a)^{-1} f_x psi_a>
- <f psi_a, (F/lambda_a) f_x psi_a>] for a real eigenbasis of F; each bracket vanishes by the proof of (21) with psi_a,
lambda_a in place of psi, lambda (it uses only reality and D^{-1} psi_a = C v_a/lambda_a), when f and f_x have disjoint
links. Absolute convergence: Cauchy-Schwarz with the first bound of (30), and Young for the forward sum. At most b^2
displacements share a link; inversion on (Z/n)^3 gives (31).

**S50, L362-366, (32): HOLDS.** Tails: rho_n(E > R) <= K_A^b e^{-R}; int_{E<-eps} e^{-tE} drho_n
= int_{E>eps} e^{-(L-t)E} drho_n <= 4 e^{-(L-t) eps}. So weak limits (in s = e^{-E}) live on E >= 0, their moments
e^{-tE + iP.x} are the limits of the torus correlations, i.e. the infinite-volume correlations nu(f tau f) =
<[f]_0, T^t U^x [f]_0> (theta_0 f = f for a time-zero f), and Stone-Weierstrass on [0,1] x T^3 identifies the limit
with mu_f. For continuous phi(P) >= 0 and an energy cutoff chi in C_c((0, infinity)), 0 <= chi <= 1, the bounded
continuous integrand passes to the limit, 1 - e^{-LE} -> 1 uniformly on supp chi, (31) and Riemann sums give
int chi 2 sinh E phi dmu_f <= b^2 K_A^b int phi dP; monotone convergence in chi gives (32).

**S51, L368-376, (33): HOLDS.** On s < E <= 2s the PL5 carrier puts P in {max_i |P_i| <= 2s/kappa}, of Haar probability
<= C s^3, and 2 sinh E >= 2s; (32) gives mu_f(s < E <= 2s) <= C b^2 K_A^b s^2; dyadic summation gives the first line.
E = 0 forces P = 0 by PL5. Layer cake: int_{E>0} e^{-tE} dmu_f = int_0^infinity t e^{-ts} mu_f((0, s]) ds
<= C b^2 K_A^b t^{-2} + 4 e^{-t} for t >= 1, and the total mass 4 at t = 0. This is (33) (with K_A >= 1).

**S52, L378-384, (34): HOLDS.** sum_{t in Z} e^{i t p_0} e^{-|t|E} = sinh E/(cosh E - cos p_0); the series converges in
total variation by (33) at x = 0; PL5 gives cosh E - 1 >= max_i (1 - cos P_i) >= (1/3) sum_i (1 - cos P_i), so the
kernel is <= 3 sinh E/[(1 - cos p_0) + sum_i (1 - cos P_i)], and (32) bounds int_{E>0} sinh E dmu_f by
(1/2) b^2 K_A^b dP. (32) also shows the E > 0 part has no atom at P = 0. Correct as a measure statement.

**S53-S55, L390-399, (35) and the exact contact in the limit state: HOLD.** Kernel: (A_f F)(u,v)/F(u,v)
= D^{-2}(u) [f-hat(D^2 C(., v))](u)/C(u,v) = (f-hat r)(u_S)/r(u_S), where r is the product of the plaquette factors
of D^2 meeting S and the link kernels on S, with spectators and v_S as parameters; this is a compact family in C^infinity
with positive infimum at fixed beta, and GL5 continuity bounds f-hat r uniformly; only local factors enter, so the
constant is volume-free (for supports that do not wrap). Second moment: F A_f = f F on smooth functions gives
A_f psi_a = lambda_a F^{-1} f psi_a, so int e^{2E} drho = Z^{-1} sum_a lambda_a^L ||A_f psi_a||^2
= Z^{-1} Tr((A_f F) F^{L-2} P_gauge (A_f F)^*), and the absolute kernel bound with a nonnegative middle kernel gives
<= C(beta,f)^2 Tr(F^L P_gauge)/Z = C(beta,f)^2. With this, int_{E>R} e^E drho_n <= C^2 e^{-R} and
int_{E<-R} e^{-E} drho_n <= 4 e^{-(L-1)R}, so 2 sinh E e^{iP.x} is uniformly integrable and the signed Fourier
coefficients pass to the limit; mu_f has no atom at E = infinity. The coefficients vanish off the finite overlap set,
so int_{E>0} 2 sinh E dmu_f(E, dP) has a trigonometric-polynomial density; for a 23-plaquette the overlapping translates
are 0, +-e_2, +-e_3 (shared 3-links and 2-links), and the coefficients are real and even. Correct.

## Step 6. The exclusion of axial plaquette packets (36) (done 2026-11-20T01:53Z, date -u)

**S56-S57, L403-420, (36): HOLDS.** Checked each step.
- Local bound: on u < E <= 2u the PL5 carrier gives |P_2|, |P_3| <= 2u/kappa (Haar area <= C u^2 in normalised
  measure), and 1 <= 2 sinh E/(2 sinh u) there; (32), applied to the nonnegative Borel function
  phi(P_1) 1{|P_2|,|P_3| <= 2u/kappa}, gives int_{u<E<=2u} phi dmu_f <= (2u)^{-1} b^2 K_A^b C u^2 int phi deta/(2 pi).
  Dyadic summation gives the same with u -> eps on (0, eps].
- Spectral measure of Phi_z: [tau_{x e_1} f]_0 = U_1^x [f]_0, so dmu_{Phi_z} = |sum_x z_x e^{i x eta}|^2 dmu_f, and the
  normalised Haar integral of that weight is sum |z_x|^2.
- Numerator: the multiplier of B^(k) is e^{-kE} sin^2(k eta/2), which vanishes on E = 0 (there P = 0 by PL5) and at
  E = infinity. Layer cake on (0, 1]: int_{(0,1]} e^{-kE} dm = e^{-k} m(1) + int_0^1 k e^{-ks} m(s) ds with
  m(s) <= C b^2 K_A^b s sum|z_x|^2, so <= e^{-k} m(1) + C b^2 K_A^b k^{-1} sum |z_x|^2; the part E > 1 is
  <= e^{-k} times its mass. Total <= C k^{-1} sum|z_x|^2 + e^{-k} ||Phi_z||^2 (b = 4; the fundamental reading has degree
  1 <= ceil(A sqrt beta) per link and |f| <= 2, so (30) applies to it too).
- Denominator: ||Phi_z||^2 = nu(|sum z_x tau_{x e_1} f|^2) (time-zero, theta_0 fixes it). On each periodic four-cube,
  condition on all links but one edge of each plaquette of one parity of x; no plaquette contains two selected edges;
  conditional variance >= c_0 = 1/4 (oscillatory reading, row 1161 L273-281) or >= c(1 + 6 beta)^{-2} (fundamental,
  row 1161 Gram bound L237-246); centering constants do not change conditional variances; a fixed finite coefficient list
  passes to the limit. So ||Phi_z||^2 >= c sum|z_x|^2, resp. c (1 + beta)^{-2} sum|z_x|^2. Dividing gives (36).

**S58, L422: HOLDS.** With a_j k_j -> h > 0 and k_j -> infinity, (36) tends to 0 < q_0 for the oscillatory span at any
beta_j >= 1, and for the fundamental span when (1 + beta_j)^2 = o(k_j). The statement is limited to one fixed transverse
plaquette at one time, as the file says; it does not touch vectors prepared with transverse smearing or positive times.

## Step 7. Everything else, and the citations (done 2026-11-20T01:55Z, date -u)

**S8, L113: HOLDS.** W_p = d.z with |d| = 1 for the selected edge; row 1173 (8) (`gap-solve15-astra62.md` L108-114,
checked HOLDS as C33 in `gap-solve15-check-opus.md` L194) gives Var >= c(1 + 6 beta)^{-2}. The strip sigma-field is
inside the sigma-field of all other links, so E|W_p - E[W_p | strip]|^2 >= E Var(W_p | all other links) > 0.

**S9, L115-126, (9): HOLDS.** Plaquettes 3 apart in direction 2 share no action face; total variance gives
nu(|G_m|^2) >= c(1+beta)^{-2} sum_l 4^{-m} binom(m,l)^2 >= c(1+beta)^{-2}/(m+1) (Cauchy-Schwarz with
sum 2^{-m} binom(m,l) = 1). With p in the mirror x_1 = 0, theta_1 fixes F and theta_0 F, so at D = 0 both transverse
norms equal nu(|F|^2).

**S10, L128-138, (10), (11): HOLDS.** [F_{b,m}]_0 = T^b ((1 - U_2^3)/2)^m [W_p]_0, multiplier modulus
e^{-bE} |sin(3 eta_2/2)|^m <= e^{-bE} (3E/(2 kappa))^m by PL5 in direction 2; max of e^{-bE} E^m is (m/(eb))^m, giving
(10); m = floor(kappa b/6) gives 3m/(2 e kappa b) <= 1/(4e). nu(G_m) = 0, so adding eps_b adds exactly eps_b^2 to all
three squared norms; (11) follows.

**S11, L144-154, (12): HOLDS (conditional on the stated matching).** <Phi, B^(k) Phi> = (c(0) - Re c(k))/2 with
c(w) = <Phi, T^k U^w Phi>, c(-k) = conj c(k), and ||Phi||^2 = C(0,0); PL4 identifies the lattice entries. A bound q on
the supremum over the dense subspace {v_A} bounds ||B_h|| by q, which gives (2).

**S12-S13, L156-158: HOLD (standard argument, under the Wightman hypotheses).** Spectral support of
<psi, phi(x_1)...phi(x_r) Omega> in the forward cone in each increment variable, holomorphy in the product forward tube,
vanishing on an open subset of the maximal totally real set {(i tau, x)}, boundary values, and cyclicity: this is the
usual proof that Euclidean vectors from an open region are total. I found no gap in the version written.

**S14, L160: HOLDS.** For abelian M with cyclic Omega, ||A^* Omega|| = ||A Omega||, so J is a well-defined antiunitary;
it commutes with e^{itH} (time translations preserve M and Omega), so J H J^{-1} = -H, impossible for H >= 0, H != 0.
An abelian algebra with a cyclic vector is maximal abelian, so its commutant is abelian, contradicting the translated
noncommuting pair spacelike to the strip.

**S15, L162: HOLDS.** DLR gives E[F | exterior of I] = f; the negative-time insertion and the reflected or displaced
copies are exterior and their interiors share no plaquette at fine spacing, so the three numbers in (12) are unchanged.

**S16-S17, L166-172: HOLD.** Re-derived: the time-zero F_12 density is (p_1^2 + p_2^2)/(2|p|) (transverse projector);
the Wick square sum_a F^a(f_A)^2 (bilinear, so SO(3)-invariant with a complex test) is a two-particle vector whose two
momenta are independent with the one-field law weighted by |f-hat_A|^2; at p = p' = p_c = (pi/4, 0, 0) the multiplier
e^{-|p|-|p'|} sin^2((p_1 + p_1')/2) is q_0 and all six first derivatives vanish (-p_1/|p| + cot(pi/4) = 0); second
moments are O(A^-2). Deficit O(A^-2) follows. This is a free continuum example, not a Wilson statement; it shows the
(1 + A)^{-2} in (8) cannot be improved in general.

**S18, L174-179, (13): HOLDS.** int_0^infinity s^2 e^{-su} ds = 2/u^3; with z = |x|^2/(4u),
int s^2 G_s ds = (2/(16 pi^2)) (4/|x|^2)^4 Gamma(4) = 192/(pi^2 |x|^8). A_0 = 3 d_G g^4/pi^4 matches outline L1617-1620.
G_s is the 4D propagator (-Delta + s)^{-1}, spatial transform e^{-tE}/(2E). Correct.

**S19, L181-186, (14): HOLDS.** Measure ~ s^2 |f_L|^2 ds d^3p/(2E); two nondegenerate maxima of b at s = 0,
p = +-p_* e_1 with log(q_0/b) comparable to s + |p -+ p_* e_1|^2 (E - |p_1| = (s + |p_perp|^2)/(E + |p_1|));
s^2 e^{-cls} gives l^{-3} and three momentum Gaussians l^{-3/2}; the lower bound from s < 1/l,
|p -+ p_* e_1| < l^{-1/2}; the remainder is <= (q_0(1-c))^l times a finite mass (f supported at times >= t_0 > 0). The
semicircle remark: phases p_* x_1 in an interval of length < pi when the bump has x_1-width < 2h. Correct.

**S20-S21, L190-197, (15): HOLD.** For a unit time-zero strip vector, C(w) = int s^{w-D} dsigma with
||sigma||_TV <= ||[L_F]_1|| ||[F]_1|| <= 1 (w >= D); the tail sum is (z e^{-i eta})^{D'} s^{D'-D}/(1 - z s e^{-i eta}),
and |1 - e^{-i eta}| <= |1 - z s e^{-i eta}| + (1 - zs) <= 2 |1 - z s e^{-i eta}|; on the two intervals
|sin(eta/2)| >= c/k, so the Poisson density is <= C(D' + k) and the mass of length 4 eps/k is <= C(1 + D/k) eps; weak
limits z -> 1 and density of local strip functions finish it.

**S22, L199-205, (16): HOLDS.** (5) and Chebyshev give ||(1 - Pi) v||^2 <= C gamma/eps^2; ||P_S v|| <=
||Pi P_S|| + ||(1 - Pi) v||; eps = (gamma/(1 + D/k))^{1/3} makes both terms (1 + D/k)^{1/3} gamma^{1/6}. The conditional
expectation represents P_S [F]_0 because theta_0 fixes strip functions. Correct.

**S23, L209-214, (17): HOLDS.** For a general source the tail measure has TV <= R(F) ||Phi||^2, so the density in
x = k|eta| near pi/2 is <= C(1 + D/k + R(F)); g''(t) = -sin(t/2)/(1 + sin^2(t/2))^{3/2} (re-derived; it is <= 0 and
O(t)), so the log-multiplier has second derivative <= -1/2 + C/k^2 <= -1/4, giving the Gaussian envelope around
x_k = pi/2 + O(k^-2); x > pi loses a fixed factor. Integration gives C(1 + D/k + R)/sqrt(l).

**S24-S25, L216-223, (18): HOLD.** Upper bound by sum w_i ||v_i||^2 <= 1; lower bound by a fixed v_i with nonzero
spectral projection on (r, ||B_h||]. The expansion (2 - U - U^{-1})^l = sum_d (-1)^d binom(2l, l+d) U^d is correct, its
coefficients have absolute sum 4^l, and for even k the combination is ||2^{-l} T^{lk/2} (1 - U^k)^l Phi||^2.

**S32-S34, L264-277, (24) and the lower edge: HOLD.** The lattice propagator inverse
(2 cosh omega - 2 cos p_0)^{-1} -> e^{-|t| omega}/(2 sinh omega); 2 sinh(omega_p + omega_q)/(4 sinh omega_p sinh omega_q)
= (coth omega_p + coth omega_q)/2; in the first term nothing depends on q_1, so the weighted axial density is constant;
cosh omega >= 1 + 2 sin^2(p_1/2) gives omega >= g(|p_1|); g is concave (g'' above), so subadditive on u + v <= pi and
above its chord beyond; support reaches the edge with q -> 0, p -> (eta, 0, 0), transverse curls nonzero.

**S35, L281: HOLDS.** G_m sits at (x_0, x_1) = (0, 0) and is invariant under the 0 <-> 1 swap; the swap is a symmetry of
the axis-symmetric periodic limit (W_4 invariance in LG1). With the source at x_1 = b and D = 2b, all three squared norms
equal nu(G_m tau_{2b e} G_m) for one axis e, and adding eps adds eps^2 to each; so R = 1. This correctly limits (11) to
the mirror through the source.

**S36-S37, L283-289, (25): HOLD (under the stated matching and totality).** Every nonzero orbit has a point with
h p_1 = pi/2, where (25) equals 1 (e^{2 pi i L} = 1, (1 - e^{i pi})/2 = 1); continuity, a contraction error of at most
twice the distance, and (6) at w_0 = 4 L k_j >= A k_j >= D_j give liminf R(F_j) >= 2^{m-1}.

**S41, L308: HOLDS.** 2 sinh(2(omega_p + omega_q))/(4 sinh omega_p sinh omega_q) splits into
cosh omega_p (2 cosh^2 omega_q - 1)/sinh omega_q plus its interchange; cosh omega_p = c(p_perp) - cos p_1 at m >= 0; with
p_1 = eta - q_1 the sin(eta) sin(q_1) part integrates to zero (the rest is even in q_1), leaving const + const cos eta.

**S42-S45, L312-326, (28), (29): HOLD.** Re-derived the edge count: edge (x,2) lies in h_y for
y in {x, x - e_3, x - s, x - e_3 - s}, edge (x+s, 3) for y in {x + s, x + s - e_2, x, x - e_2}; the intersection is
{x} for n >= 16. Greedy colouring with 17^3 colours; selected edges of one class and the two edges of one pair share no
action face; the Hoeffding projections Q_x are mutually orthogonal, kill every h_y, y != x, and send h_x to a product of
two independent centred readings with squared norm >= c_0^2; hence (29). At most 64 overlapping displacements, each
coefficient <= <u_0, T^{-1} u_0> <= C_A^8 by (20) with b = 8 (|h - <h>| <= 2), so int 2 sinh E dmu_P <= 64 C_A^8/n^3 and
(28) follows with the stated E_*, c_*.

**S59, L426: HOLDS.** Same-time requirement for reading a selected spatial edge; spacetime sup distance > 8 keeps
selected links of one class out of common (also temporal) plaquettes; the Gram bound passes to the limit and, by
approximating square roots of nonnegative continuous tests by trigonometric polynomials, gives the four-dimensional
Fourier measure >= c_0^2 17^{-4} Haar. With (34) (b = 8) the density is between two constants times 1 and the massless
symbol.

**S60, L428-433: HOLDS.** At m = 0, b(p) <= 2(cosh omega - 1), so b/sinh omega <= 2 tanh(omega/2) <= omega; with
coth((u+v)/2) <= 1 + 2/(u+v) the integrand is <= C uv(1 + (u+v)^{-1}), bounded; the good transverse sets have measure
> 3/4 each, so their intersection has measure >= 1/2; energies there are in a compact subset of (0, infinity).

**GUIDE and citation spot checks.** Outline L581-599: the polynomial-cluster example (spectral measure E e^{-E} dE,
correlation (1 + t)^{-2}) is there, as L7 says. Outline L1601-1624: C_2 = 3 d_G g^4/(pi^4 |x - y|^8). Outline
L4289-4314 (F2, relative error |r| <= 1/2 on prescribed test classes) and L4360-4374 (F3, g^{-2} = c_* log(1/d)(1 + o(1)))
match L229. GL3-GL7 and PL4-PL7 as in Steps 3-4. A0 (`gap-wall-assumptions-opus.md` L102) is the rest-energy /
invariant-mass equivalence credited at L13. `open-registry.md` has no entry for "mass gap", "neutral trace" or "N-phys"
(grep count 0), as L5 says. Every linked repository file exists at the pinned commit. I did not re-open the external PR
files of L3 (GUIDE only). No home-directory path appears in the checked file.

**Novelty note (for credit only).** The detector B_h of (1) and the value q_0 = e^{-pi/2}/2 occur in no other file of
`library/`, `library/prior/` or `parts/gap.md` (grep for "e^{-\pi/2}"); the underlying equivalence of a rest-energy
gap and an invariant-mass gap is A0 of row 1052 (`gap-wall-assumptions-opus.md` L102), credited at L13. I make no claim that (1) is new to
the literature.

## Step 8. Verdict table and result (done 2026-11-20T01:56Z, date -u)

| S | lines | statement | verdict |
|---|---|---|---|
| S1 | L15-30 | (1) norm of B_h = Q(hM) | HOLDS |
| S2 | L32-40 | q_0, strict threshold, (2) | HOLDS |
| S3 | L48-61 | (3), (4) from PL5 | HOLDS (PL5 via PH1 Lemma 2 under the frozen import LG1) |
| S4 | L63-71 | (5) | HOLDS |
| S5 | L75-92 | (6) | HOLDS |
| S6 | L94-99 | (7) | HOLDS |
| S7 | L101-107 | (8) strict strip bound | HOLDS |
| S8 | L113 | strip functions are a proper subspace | HOLDS |
| S9 | L115-126 | (9) | HOLDS |
| S10 | L128-138 | (10), (11) | HOLDS |
| S11 | L144-154 | (12) | HOLDS (under the stated matching) |
| S12 | L156 | spectral support for totality | HOLDS (under the Wightman hypotheses) |
| S13 | L158 | totality by analytic continuation | HOLDS (under the Wightman hypotheses) |
| S14 | L160 | abelian strip algebras are not cyclic | HOLDS |
| S15 | L162 | shell representation | HOLDS |
| S16 | L166 | free Maxwell singlet set-up | HOLDS |
| S17 | L168-172 | deficit O(A^-2) | HOLDS |
| S18 | L174-179 | (13) | HOLDS |
| S19 | L181-186 | (14) | HOLDS |
| S20 | L190-195 | (15) statement | HOLDS |
| S21 | L197 | (15) proof | HOLDS |
| S22 | L199-205 | (16) | HOLDS |
| S23 | L209-214 | (17) | HOLDS |
| S24 | L216-221 | (18) | HOLDS (under matching and totality) |
| S25 | L223 | finite Wilson form of (18) | HOLDS |
| S26 | L225-229 | (19) | HOLDS |
| S27 | L231-235 | (20) | HOLDS |
| S28 | L239-244 | (21) statement | HOLDS |
| S29 | L246 | (21) proof | HOLDS |
| S30 | L248-253 | (22) | HOLDS |
| S31 | L255-260 | (23) | HOLDS |
| S32 | L264-268 | free lattice covariance | HOLDS |
| S33 | L270-275 | (24) | HOLDS |
| S34 | L277 | lower edge g(abs eta) at m = 0 | HOLDS |
| S35 | L281 | padding gives R = 1 | HOLDS |
| S36 | L283-287 | (25) | HOLDS (under matching and totality) |
| S37 | L289 | no common reflection-norm bound | HOLDS (same hypotheses) |
| S38 | L293-298 | (26) statement | HOLDS |
| S39 | L300 | (26) commutation | HOLDS |
| S40 | L302-306 | (27) | HOLDS |
| S41 | L308 | (27) compatible with (24) | HOLDS |
| S42 | L312-316 | (28) statement | HOLDS |
| S43 | L318 | only h_x reads both selected edges | HOLDS |
| S44 | L320-324 | (29) | HOLDS |
| S45 | L326 | (28) proof | HOLDS |
| S46 | L330-340 | (30) set-up, detailed balance | HOLDS |
| S47 | L342-346 | first bound of (30) | HOLDS |
| S48 | L348 | positive-kernel trace bound | HOLDS |
| S49 | L350-358 | (31) | HOLDS |
| S50 | L362-366 | (32) | HOLDS |
| S51 | L368-376 | (33) | HOLDS |
| S52 | L378-384 | (34) | HOLDS |
| S53 | L390-395 | (35) kernel bound | HOLDS |
| S54 | L397 | (35) second moment | HOLDS |
| S55 | L399 | exact contact in the limit state | HOLDS |
| S56 | L403-413 | (36) statement | HOLDS |
| S57 | L415-420 | (36) proof | HOLDS |
| S58 | L422 | (36) in the physical limit | HOLDS |
| S59 | L426 | four-direction Gram bound | HOLDS |
| S60 | L428-433 | bounded density of the massless singlet | HOLDS |

Count: 60 statements (61 PROVED paragraphs): 60 HOLD, none HOLDS AFTER CORRECTION, none FAILS. GUIDE and OPEN
paragraphs: the spot-checked citations are accurate (Step 7); the OPEN paragraphs L9, L42, L140, L386, L435 are honest.

**What the row establishes and what it leaves (checker's reading, no new claim).** In a relativistic vacuum
representation, the one number sup ||B_h|| decides a mass gap (S1-S2). In the Wilson state, (8) and (36) put a strict
deficit below q_0 on two classes of local vectors: same-time strip sources of bounded physical width, and same-time
axial packets of one plaquette. The row also proves that neither class can be total: abelian time-zero strip algebras
are not cyclic (S14), and the bounded-R classes miss the near-threshold vectors (S22, S36-S37). The infrared estimates
(32)-(34) are uniform in beta and in the volume, but they allow spectral weight in every interval (0, eps) (L386; the
same remark is the outline's example at L588-596). So the gap question stays exactly at the row's OPEN line L435: a
common q < q_0 for the ratios (12) on a total matched family, together with the construction and matching themselves.
No numeric run was made or needed.

RESULT: HOLDS - check of row 1204 (`library/gap-solve21-astra62.md`), line by line by hand, by Claude Opus 5.5 (max) on the Mac mini Claude worker as FINISH row 1210, cross-provider; positive claims first: (1) and (2), (8) with (3)-(7), (21) and (26) with (22), (23), (27), (32)-(35) with (30), (31), and (36) all HOLD; then everything else: 60 statements in 61 PROVED paragraphs, 60 HOLD, none needs correction, none FAILS; conditional as the file states: (12), (18), (25) and totality under the Wightman and matching hypotheses, and (3)-(8) through PL5 (PH1 Lemma 2 under the frozen LG1); the cited row 1161 (18)-(20) and c_0 (row 1162) and row 1173 (8) (C33) were already checked HOLDS; OPEN as the row says: a common q < e^{-pi/2}/2 for the ratios (12) on a total family of matched local states, the 4D SU(2) construction with full matching, and the Jaffe-Witten gap.
