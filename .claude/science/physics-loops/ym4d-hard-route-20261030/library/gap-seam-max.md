lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T16:07Z

# gap-seam-max (row 929): the U(1) fact test for (SEAM), then the SU(2) attack

Provenance: Claude Fable 5.2, max effort, Mac mini worker, pinned at commit 5be5e895d of
`claude/ym4d-hard-route`. Author lane, not a check. Research-stage working state; nothing here is a
public claim and nothing here grants status. Statements are marked PROVED, CONDITIONAL (on named
inputs), GUIDE (numeric or heuristic, never a proof step) or OPEN.

## 0. Plan (at most eight steps; one step per response, appended before the next)

1. Read row 929's inputs in full: `library/gap-glue2-opus.md` (row 920) and
   `library/gap-glue2-check-astra.md` (row 921). Write the exact statements used here (INS, (SEAM)_a,
   Delta_theta, S_ev, the threshold, C1-C3, (I1)-(I3)) into Section 1.
2. Repo search and duplicate check (rule 0a, Repo first): grep `library/open-core.md` and the FINISH
   rows for (SEAM), (I1)-(I3) and the U(1) endpoint; list what is already covered. Section 2.
3. STEP A, set-up: write the Gaussian U(1) model (Villain or noncompact) on the same box and time
   extent, with the same twist/sector definitions, and derive S_ev and Delta_theta in closed form.
   Section 3.
4. STEP A, values: evaluate the exact S_ev, Delta_theta at theta = 0, 1 and an interior theta, and
   the threshold; settle "a^-4 law against a^-3 threshold" by hand, with a numeric GUIDE only as a
   cross-check. Verdict: does U(1) fail (SEAM), where, by how much. Section 4.
5. If U(1) passes (SEAM) at some size: the corrected crux form that U(1) fails. Section 5.
6. STEP B: attack (SEAM) (or the corrected form) for SU(2) Wilson at beta 2.3-2.6, or the weakest of
   (I1)-(I3) that suffices; the proof must use a property U(1) lacks and show the exact step where
   the photon breaks it. Section 6.
7. Binding checks: frozen Q_8 and 2T (check 896 D6), ceilings 2/3, 0.775, 4G_3 = 1.0109. Section 7.
8. Result table and the RESULT line. Section 8.

Status of the plan: step 1 in progress (file created 2026-11-14T04:07Z).

## 1. Inputs read (step 1; READ = read at the pinned commit, not re-proved here)

Read in full: `library/gap-glue2-opus.md` (row 920, Claude Opus 5.5, 304 lines) and
`library/gap-glue2-check-astra.md` (row 921, Codex gpt-6-astra, 232 lines).

Objects (row 920 Sections 4.1-4.4, check 921 Sections 1-4, all HOLDS there).

- Box: spatial b^3 periodic, time a, b = 24a. T = e^(V/2) K e^(V/2) the Wilson transfer operator,
  lambda_0 its simple top eigenvalue, Omega its vacuum, psi = e^(V/2) Omega. P_0 = average of the 8
  centre flips. Z_0(t) = Tr(T^t P_0) = lambda_0^t (1 + S_ev(t)).
- Seam kernel K_theta: the last slices (U, W) of copies 1, 2 are joined to the first slices (U', W')
  with weight exp(beta sum_l [(1-theta)(x_A1 + x_A2) + theta (x_B1 + x_B2)]); A1 = (U,U'), A2 = (W,W'),
  B1 = (U,W'), B2 = (W,U'). delta_l = x_A1 + x_A2 - x_B1 - x_B2 on one spatial link l.
- Z_theta(a) = Tr(T^(a-1) P_0 Nt_theta), Phi_theta = <psi x psi, K_theta psi x psi>; Z_theta(a) =
  lambda_0^(a-2) Phi_theta E_theta^inf[rho], rho = pbar_(a-1)(U', U).
- (INS): log(1 + S_ev(a; b^3)) = 3 b^3 beta int_0^1 Delta_theta dtheta,
  Delta_theta = E_theta^(a)(delta_l) - E_theta^(inf)(delta_l). The reference part integrates to zero
  (Phi_0 = Phi_1), not pointwise.
- (SEAM)_a: sup_theta |Delta_theta(a; 24a)| <= psi_*(a, beta) := log(1.1)/(3 beta (24a)^3).
  Sufficient for (GLUE-FP)_a: S_ev(a; (24a)^3) <= 1/10. The SIGNED theta-average of Delta at most
  psi_* is necessary and sufficient (check 921 Section 4). No converse to the sup.
- Lemma E: Delta_0 = u^t_(a,ev) - u^t_inf (thermal shift of one time-like plaquette), Delta_1 = 0.
  Proof uses the compact gauge average of the mismatched plaquettes.
- Lemma V: d/dbeta_t log(1 + S_ev) = 3 a b^3 Delta_0 at beta_t = beta_s.
- C1: Delta_theta = Cov_theta^inf(delta_l, rho)/E_theta^inf(rho). C2: |Delta| <= 8 d_TV <= 4 sqrt(chi2)
  of one link's seam variables. C3 with (I1) slab clustering in L^2, (I2) spatial localization in L^1
  under BOTH laws, (I3) local chi-square distance of ring and vacuum SEAM marginals (check 921
  Section 8: the reference of (I3) is the seam law, not nu x nu).
- Check 921 Section 12.1 (the point of row 929): from Lemma E only sup_theta |Delta| >= |Delta_0|;
  with a GUIDE law |Delta_0| = C a^-4 the ratio to psi_* is 3 beta 24^3 C/(L a), L = log 1.1, which
  tends to 0. So the exponent alone shows no U(1) failure. "This does not prove that U(1) satisfies
  GLUE or SEAM: an interior theta value, or the exact thermal trace, could still refute them."
- Check 921 Section 12.2: frozen Q_8, 2T fail (SEAM) at each fixed box for large finite beta
  (S_ev >= 1/2 from check 896 D6 plus the necessary average).

Status of the plan: step 1 done. Step 2 (repo search, duplicates) next.

## 2. Repo search and duplicate check (step 2)

- `library/open-core.md`: no line matches (SEAM), GLUE-FP, seam with theta or insertion, (I1), (I3),
  or a U(1) photon / S_ev / endpoint value (grep at the pinned commit, zero hits).
- FINISH rows: (SEAM) and `gap-glue2` appear only in rows 920, 921 (the inputs) and 929 (this row).
  Rows 922-928 treat the flux half (FR), the pin transport and (UNIV-K). No row attacks (SEAM) or
  computes the U(1) seam value. Rows 796, 798 (`gap-seam-astra`) concern an older seam object; I did
  not open them, and I rely on check 921 Section 13 for "different object" (a locator, not evidence).
- Cross-branch search (origin/main, PR branches): NOT run in this session. Check 921 ran it for
  `cut.and.reglue|Proposition INS` and found no hit; that is its result, not mine.
- Verdict: no duplicate found. Step A and Step B proceed.

## 3. STEP A, set-up: the free-photon model and its seam family

Credit. The seam construction, (INS), Lemmas E, V, C1-C3 are row 920's (Claude Opus 5.5), checked
by row 921 (Codex gpt-6-astra). The transfer machinery is the Sussman-Alpoge account's GL8 (Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors of their text), read through those rows.

### 3.1 The model (definition) and its thermal sum (PROVED, by hand)

Model FP(beta; b). "Villain U(1) without monopoles", defined on its physical modes. Spatial momenta
k in (2 pi/b) Z_b^3. For k != 0 put kappa_k = sum_i 4 sin^2(k_i/2), cosh(omega_k) = 1 + kappa_k/2,
sigma_k = sinh(omega_k). The state space is the tensor product of one L^2(R) for each k != 0 and
each of two transverse polarizations, and L^2((R/2 pi Z)^3) for the three Polyakov phases. The
transfer operator is the tensor product of
  T_k(q, q') = exp(-(beta/2)[(kappa_k/2) q^2 + (q - q')^2 + (kappa_k/2) q'^2])   (photon modes),
  T_zm(phi, phi') = prod_i sum_n exp(-(beta b/2)(phi_i - phi'_i - 2 pi n)^2)       (zero modes).
Origin (ARGUED, standard): the action (beta/2) sum_p (dA)_p^2; the temporal links enter a time-like
plaquette through (dg)_l, which is longitudinal, so the Gauss projection removes the longitudinal
part and leaves the transverse modes with kinetic term (q - q')^2 and magnetic term kappa_k q^2;
the constant mode A_i = phi_i/b has kinetic weight beta b^3/b^2 = beta b and period 2 pi.
The Z_2 centre flip C_i is phi_i -> phi_i + pi. P_0 keeps the even electric fluxes.

Lemma M (Mehler form; PROVED by induction). T_k^n = c_n k_n with
  k_n(q, q') = exp(-(beta/2) sigma [(q^2 + q'^2) coth(n omega) - 2 q q'/sinh(n omega)]),
  c_n = (2 pi/beta)^((n-1)/2) (sinh omega/sinh(n omega))^(1/2).
Proof. n = 1: sigma coth(omega) = cosh(omega) = 1 + kappa/2 and sigma/sinh(omega) = 1. Step: the
Gaussian integral of k_n(q, p) k_1(p, q') over p, with coth x + coth y = sinh(x + y)/(sinh x sinh y)
and coth x - coth(x + y) = sinh y/(sinh x sinh(x + y)). QED
Consequences. Tr T_k^n = c_n (pi/(beta sigma tanh(n omega/2)))^(1/2) = (2 pi/beta)^(n/2)
e^(-n omega/2)/(1 - e^(-n omega)) (use sinh x tanh(x/2) = 2 sinh^2(x/2)). So lambda_0 =
(2 pi/beta)^(1/2) e^(-omega/2), Tr T_k^n/lambda_0^n = 1/(1 - e^(-n omega)), and the vacuum is
exp(-(beta/2) sigma q^2).

Lemma F (flux sectors; PROVED). By Poisson summation sum_n exp(-(c/2)(x - 2 pi n)^2) =
(2 pi c)^(-1/2) sum_e exp(-e^2/(2c)) e^(iex). So T_zm has eigenvectors e^(i e.phi), e in Z^3, with
eigenvalue ratio exp(-|e|^2/(2 beta b)). C_i acts as (-1)^(e_i).

Theorem A1 (exact even thermal sum; PROVED).
  1 + S_ev(a; b^3) = prod_(k != 0) (1 - e^(-a omega_k))^(-2) * (sum_(j in Z) e^(-2 a j^2/(beta b)))^3.
Proof. Tensor product; Lemma M per mode (two polarizations per k); Lemma F with e = 2j. QED

Theorem A2 (hand bound at b = 24a; PROVED). For every integer a >= 1 and every beta > 0:
  log(1 + S_ev(a; (24a)^3)) >= 52 e^(-1/2) > 31,
and, from the flux factor alone, 1 + S_ev >= (1 + 2 e^(-1/(12 beta)))^3 (> 22 when beta >= 1).
Proof. Take the 26 momenta k = 2 pi n/b, n in {-1, 0, 1}^3 minus 0 (distinct, since b >= 24).
2 sinh(omega/2) = sqrt(kappa) and sinh x >= x give omega <= sqrt(kappa) <= |k| <= 2 pi sqrt(3)/(24a)
< 0.4535/a. So e^(-a omega) > e^(-1/2) > 0.6, and -log(1 - x) >= x. Two polarizations: 52 terms,
each above 0.6. Flux: 2a/(beta b) = 1/(12 beta); keep j = 0, 1, -1. QED

So FP fails (GLUE-FP)_a at every a: S_ev > e^31 - 1 against 1/10.

Values (GUIDE: lattice sums, script `/tmp/gap-seam-max-929/scripts/u1_seam.py`, log beside it;
continuum value (pi^2/45)(b/a)^3 = 3031.94 at b = 24a, ARGUED Riemann limit):
photon part of log(1 + S_ev) = 4172.39 (a = 4), 3149.04 (a = 10), 3079.10 (a = 15); even-flux part
3 log(sum_j e^(-j^2/(12 beta))) = 6.69 (beta 2.3), 6.82 (beta 2.5). (A variant with conserved
magnetic flux adds 0.79 resp. 0.68. Not used.)

### 3.2 The seam family in the model: path G (definition) and its closed form (PROVED)

Path G is row 920's exponential interpolation applied to the Gaussian weights of one transverse
mode. Variables: u, u' (copy 1, last slice before and first slice after the seam), w, w' (copy 2).
Copy 1 is the ring T_k^(a-1)(u', u); copy 2 is the vacuum on both sides. The exponent is -(beta/2)
times
  Q_theta = sigma[(u^2 + u'^2) coth(n omega) - 2 u u'/sinh(n omega)] + (kappa/2)(u^2 + u'^2)
            + (kappa/2 + sigma)(w^2 + w'^2)
            + (1 - theta)(u - u')^2 + theta (u - w')^2 + (1 - theta)(w - w')^2 + theta (w - u')^2,
n = a - 1 (Lemma M for the ring; psi = e^(V/2) Omega for copy 2; e^(V/2) of Nt on u, u'). The
reference (inf) replaces the first bracket by sigma(u^2 + u'^2). The longitudinal modes carry the
same seam factor in the ring and in the reference, so they are left out (definition of the family).

Notation: c = cosh omega, E = e^omega = c + sigma, t = tanh(n omega/2),
  alpha_- = c - 1 + sigma t,  alpha_+ = c + 1 + sigma/t,  eps_- = E - 1,  eps_+ = E + 1,
  h_- = alpha_- eps_-/(alpha_- + eps_-),  h_+ = alpha_+ eps_+/(alpha_+ + eps_+).

Proposition G (one mode; PROVED).
(a) In the basis (u, w; u', w') the matrix of Q_theta is [[D, -C], [-C, D]] with D = diag(A, E),
    A = sigma coth(n omega) + c, C = [[1 - theta + B, theta], [theta, 1 - theta]], B = sigma/sinh(n omega).
    Hence det Q_theta = det(D - C) det(D + C)
      = [alpha_- eps_- + theta (alpha_- + eps_-)] * [alpha_+ eps_+ - theta (alpha_+ + eps_+)],
    both factors linear in theta. (A - B = c + sigma t, A + B = c + sigma/t.)
(b) Reference: A -> E, B -> 0: det Q_theta^inf = [eps_-^2 + 2 theta eps_-][eps_+^2 - 2 theta eps_+],
    equal at theta = 0 and 1 (value (E^2 - 1)^2). This is Phi_0 = Phi_1 for one mode.
(c) The mode's part of beta sum_l Delta_theta is
      G(theta) = (1/2) d/dtheta [log det Q_theta - log det Q_theta^inf]
               = (1/2)[1/(h_- + theta) - 1/(eps_-/2 + theta)] + (1/2)[1/(eps_+/2 - theta) - 1/(h_+ - theta)].
    Both brackets are positive on [0, 1]: h_- < eps_-/2 because alpha_- < eps_- (t < 1), and
    h_+ > eps_+/2 > 1 because alpha_+ > eps_+. So G > 0: on path G, Delta_theta > 0 for every theta.
(d) (INS) for one mode, by algebra: int_0^1 G = (1/2) log(det Q_1/det Q_0) = -log(1 - e^(-a omega)).
Proof of (d). det Q_1 = ((A - B)E - 1)((A + B)E - 1) = sigma E (1 + t) * sigma E (1 + 1/t), using
c^2 - 1 = sigma^2. det Q_0 = (A - B - 1)(A + B + 1)(E^2 - 1), with (c - 1 + sigma t)(c + 1 + sigma/t)
= sigma[2 sigma + (c - 1)/t + (c + 1) t] and E^2 - 1 = 2 sigma E. The ratio is
E (1 + t)^2/(2[2 sigma t + c - 1 + (c + 1) t^2]). With x = n omega: (1 + t)^2 = e^x/cosh^2(x/2) and
2 sigma t + c - 1 + (c + 1) t^2 = (cosh(x + omega) - 1)/cosh^2(x/2). So the ratio is
e^(x + omega)/(2 cosh(x + omega) - 2) = (1 - e^(-a omega))^(-2). QED
GUIDE cross-check of (a)-(d): a brute-force (a+2) x (a+2) quadratic form at five (kappa, a) pairs
agrees with (d) to 12 digits and with (c) to finite-difference accuracy (log `u1_brute.log`).

So on path G:  3 b^3 beta Delta_theta^G = sum_(k != 0) 2 G_k(theta)  (photon part; exact).

Two endpoint values must be kept apart.
- Path-G endpoints. Delta_0^G and Delta_1^G are NOT given by Lemma E. Lemma E uses the compact
  gauge average, which makes a mismatched plaquette mean zero. A Gaussian mismatched plaquette
  -(1/2)(u - w')^2 has a nonzero mean. On path G: 3 b^3 beta Delta_0^G = beta sum 2 (E_a - E_inf)(u u').
- The compact endpoint. For a compact U(1) theory with this photon spectrum, Lemmas E and V give
  Delta_0^cpt = (1/(3 a b^3)) d/dbeta_t log(1 + S_ev) = (1/(3 b^3 beta)) sum_(k != 0)
  kappa_k/(sigma_k (e^(a omega_k) - 1)) (photon part; from cosh omega = 1 + (beta_s/beta_t) kappa/2).

### 3.3 Sizes (ARGUED: Riemann limits a -> infinity at b = 24a; the GUIDE table confirms them)

  theta-average of Delta (exact by (INS))      = log(1 + S_ev)/(3 beta b^3) -> (pi^2/135)/(beta a^3)
  compact endpoint Delta_0^cpt (Lemmas E, V)   -> (pi^2/90)/(beta a^4)        = (3/(2a)) x average
  path G, theta = 0                            -> 1/(18 beta a^2)             (layer of width ~ 1/a)
  path G, theta = 1                            -> 1/(3 pi^2 beta a^2)         (layer of width ~ 1/a)
  path G, fixed interior theta                 -> [1/(2 pi^2 theta^2) + pi^2/(180 (1 - theta)^2)]/(beta a^4)
  threshold psi_*                              = log(1.1)/(3 beta (24a)^3)    = 2.298e-6/(beta a^3)
Reason for the layers. For a mode with omega << 1: h_- ~ omega(1 - e^(-n omega))/2 and eps_-/2 ~
omega/2, so the first bracket of G is ~ (omega e^(-n omega)/2)/((theta + h_-)(theta + omega/2)): of
size (1/omega) n_B at theta = 0 and of size omega e^(-n omega)/theta^2 once theta >> omega. A spring
of strength theta >> omega to the other copy ties the four ends together; nothing changes until
1 - theta ~ omega. Half of log(1 + S) sits in each layer.

## 4. STEP A, values and verdict

GUIDE table (free-photon lattice sums, photon part only; beta = 2.3 at a = 4, 10 and 2.5 at a = 15).
Each entry: value, and in brackets its ratio to psi_*.

| quantity | a = 4, b = 96 | a = 10, b = 240 | a = 15, b = 360 |
|---|---|---|---|
| psi_* | 1.5613e-8 | 9.9921e-10 | 2.7238e-10 |
| log(1 + S_ev), photon part | 4172.39 | 3149.04 | 3079.10 |
| theta-average of Delta | 6.835e-4 (43777) | 3.301e-5 (33040) | 8.799e-6 (32306) |
| compact endpoint Delta_0^cpt | 2.784e-4 (17834) | 5.014e-6 (5017) | 8.851e-7 (3250) |
| path G, theta = 0 | 1.710e-3 (1.10e5) | 2.221e-4 (2.22e5) | 8.925e-5 (3.28e5) |
| path G, theta = 0.1 | 8.339e-4 (5.34e4) | 4.376e-5 (4.38e4) | 1.118e-5 (4.11e4) |
| path G, theta = 0.5 | 5.085e-4 (3.26e4) | 1.374e-5 (1.38e4) | 2.690e-6 (9.88e3) |
| path G, theta = 0.9 | 8.150e-4 (5.22e4) | 4.522e-5 (4.53e4) | 1.176e-5 (4.32e4) |
| path G, theta = 1 | 1.248e-3 (7.99e4) | 1.510e-4 (1.51e5) | 6.029e-5 (2.21e5) |

Checks inside the table: Delta^G_0 beta a^2 = 0.051, 0.050 at a = 10, 15 (limit 1/18 = 0.056);
Delta^G_1 beta a^2 = 0.035, 0.034 (limit 0.0338); Delta^G_(1/2) beta a^4 = 0.32, 0.34 (limit 0.42,
approached slowly because theta = 1/2 is only a few times omega); Delta_0^cpt beta a^4 = 0.115,
0.112 (limit 0.1097).

Verdict (answers to row 929, Step A).

1. U(1) FAILS the glue half and FAILS (SEAM)_a at every size a. PROVED for the free-photon model:
   Theorem A2 gives log(1 + S_ev) > 31, and the signed theta-average is necessary (check 921
   Section 4), so sup_theta Delta_theta >= average > (31/log 1.1) psi_* > 325 psi_*. GUIDE value of
   that factor: 3.2e4 to 4.4e4, independent of a in the limit ((pi^2/45) 24^3/log 1.1 = 3.18e4).
2. Which is right, "order 24^3" or "a^-4"? Both; they are different quantities. The a^-4 law is
   the compact endpoint Delta_0 (and the path-G interior). The theta-average is exactly
   log(1 + S_ev)/(3 beta b^3) ~ a^-3. Their ratio is 3/(2a). (INS) does not force Delta_theta to be
   of one size in theta; row 920's "about a^-4" described the endpoint only.
3. Check 921's objection is correct as logic and does not change the verdict. With the constant,
   the endpoint alone already exceeds psi_* when a < (pi^2/30) 24^3/log(1.1) = 4.8e4 (ratio
   4.77e4/a; lattice values 5017 at a = 10, 3250 at a = 15). Beyond a = 4.8e4 the endpoint test is
   blind, and the average still fails by 3.2e4.
4. At which theta. On path G: at every theta for the sizes of the table; least at theta = 1/2
   (ratio 1.4e4 at a = 10, falling like 1/a, so the interior passes pointwise only for a above
   about 1.8e5); most in the two layers theta < 1/a and 1 - theta < 1/a, where Delta ~ a^-2 (ratio
   2.2e5 at a = 10, growing like a).
5. No size exists at which U(1) passes (SEAM): the average binds at every a.

What Step A does not show. FP is the Gaussian model named in the row. Nothing here is proved for
compact Wilson U(1) at beta 2.3: its photon is a GUIDE statement (Coulomb phase). On the Wilson
path the profile near theta = 0 and 1 differs from path G: for theta beta < 1 the B plaquettes are
disordered, the relative gauge phase of the slices U' and W' is a three-dimensional XY field on
the seam, and the transition from "two lines" to "four ends tied" is expected near its ordering
point (theta beta of order 0.45), not at theta ~ 1/a (GUIDE, heuristic; OPEN). The average does
not depend on the path.

## 5. Is (SEAM) the right crux form? (step 5)

U(1) passes at no size, so the fact test does not refute (SEAM)_a as a sufficient crux form. It
shows two things about the form (PROVED parts marked).

1. (PROVED) (SEAM) is a Lipschitz statement. Put F(theta) = log E_theta^inf[rho]. By Lemma BR and
   check 921 Section 2, F(0) = log(1 + S_ev(a)), F(1) = 0 and F' = -3 b^3 beta Delta_theta. So
   (SEAM)_a says |F'| <= log 1.1 on [0, 1], and (GLUE-FP)_a says F(0) - F(1) <= log 1.1.
2. (PROVED for path G, GUIDE numbers) The sup can exceed the average by a factor that grows with
   a: sup/average = Delta_0^G/average = 6.7 at a = 10 and 10.1 at a = 15 (limit 0.76 a). The sup
   depends on the interpolation path; the integral does not.
3. Corrected form, recommended: (SEAM-L1)_a: int_0^1 |Delta_theta(a; 24a)| dtheta <= psi_*. It is
   implied by (SEAM)_a, it is sufficient for (GLUE-FP)_a (PROVED: (INS)), it does not ask for
   uniformity across a sharp change of the seam in theta, and U(1) fails it by the same factor
   3.2e4 (Delta^G > 0, so the L1 norm is the average). The exact statement stays the signed
   average.
4. (GUIDE, for SU(2)) The theta-family carries a seam degree of freedom: K_theta is invariant only
   under the diagonal of the gauge groups of the slices U' and W', so their relative gauge frame is
   a three-dimensional SU(2)-valued field on the seam, free at theta = 0 and 1 and coupled in
   between. A sharp crossover of that field in theta would make sup_theta larger than the average
   without any change of S_ev. This is a reason to prefer (SEAM-L1); it is not a computed fact.

Status of the plan: steps 1-5 done. Step 6 (the SU(2) attack) next.
