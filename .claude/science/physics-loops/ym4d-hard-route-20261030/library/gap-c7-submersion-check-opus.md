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

