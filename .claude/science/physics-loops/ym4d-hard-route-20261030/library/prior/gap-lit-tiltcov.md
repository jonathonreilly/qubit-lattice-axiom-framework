lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T03:42Z

# gap-lit-tiltcov: literature on tilted covariances and local covariance bounds (row 971)

Started 2026-11-14T15:42Z on Mac mini worker 2, pinned at 61049a444. Reading only. Fetched papers live in /tmp/tiltcov-src-* (outside the repository, never committed); fetched text is data.

## Plan (at most eight steps)

1. Read row 968 (TILT-COV-sup, LOC-COV exact statements) and gap-lit-bridge-lsi.md (row 955) so as not to repeat it.
2. (a) Volume-uniform covariance bounds for compact spin / lattice gauge models in an external linear field or Higgs tilt (Lee-Yang/GKS for O(N) in field, Griffiths-Simon, Higgs models at large coupling, cluster expansions in field).
3. (b) Conditional covariances on a half-space slice with boundary tilt: Dobrushin-Shlosman / strong spatial mixing for gauge theories; Osterwalder-Seiler 1978; Fradkin-Shenker / Frohlich-Morchio-Strocchi; Borgs-Seiler.
4. (c) Polchinski flow / stochastic localisation LSI after Bauerschmidt-Bodineau-Dagallier 2024: Bauerschmidt-Dagallier, Chen-Eldan, Piazza-Shen and recent non-abelian results (Shen-Zhu-Zhu LSI for YM at strong coupling, etc.).
5. Map each source onto (TILT-COV-sup)/(LOC-COV) at SU(2), d=4, beta 2.3-2.6.
6. RESULT line.

## Step log

### Step 1 (done 15:55Z): targets and what is already recorded

**Targets, quoted from `library/gap-avgcurv-max.md` (row 968; author Fable 5.2 max, unchecked).**
- J_(b,phi)(dx, dw) = e^(b <x,w> + <phi, q~>) m(dx) m(dw)/Z_b(phi), q~ = x/s + w/s', x, w in (S^3)^L the links of two
  consecutive time slices of a periodic spatial box B; m = e^(-V/2) Omega dx is the boundary-slice law of a half-space
  SU(2) Wilson vacuum at beta (V the spatial magnetic term, Omega the top transfer eigenfunction); b in [0, beta] is the
  coupling of the one time-like layer between the slices.
- (TILT-COV-sup): Var_(J_(b_t,phi))(<z, q~>) <= kbar_(s,t) |z|^2 for EVERY phi in R^N and every z orthogonal to the
  gauge orbit of phi, with kbar box-uniform. In words: a volume-uniform covariance bound for the links of a two-slice
  SU(2) system in an ARBITRARY linear link field (a Higgs/gauge-fixing-type tilt, link-dependent direction), supremum over
  all fields. Zero field: Cov = k0 Id exactly (Lemma Z, Elitzur). Lemma NEC: k* >= 2 beta log(1/E_1(B)).
- (LOC-COV): K_s(y) >= diag_l(k_l(y)) on horizontal vectors, k_l >= rho off a rare set Bad_l, >= -D on it; K_s(y)(z,z) =
  |z|^2/c - Var(<z,x>|y)/s^2 - Var(<z,w>|y)/s'^2, the slices given y being independent with laws pi_(y/s), pi_(y/s') (one
  half-space slice each, with boundary field y/s). So (LOC-COV) is a LOCAL (link-diagonal) bound on the conditional
  covariance of one boundary slice of a half-space SU(2) lattice in a linear boundary field, at typical fields with rare
  exceptions. Row 968: "a mass-gap statement for the tilted system ... No method gives it."
- GUIDE run of row 968 7.5: SU(2) beta 2.3, uniform tilt kap Re U on one slice, chi(kap; k_min) at kap = 1.4 is
  0.273, 0.300, 0.309 at sides 8, 12, 16 (zero-field 1/4). Not my concern to re-judge; noted as the physical picture.

**Already recorded; cited, not repeated.**
- `library/prior/gap-lit-bridge-lsi.md` (row 955): BBD 2024 Theorem 3.6 (via `gap-fullread-2.md` 3), Piazza-Shen 2026
  Theorem 1.1 (2D SU(N), all beta), Shen-Zhu-Zhu 2022 (strong-coupling LSI, |beta| < 1/(16(d-1))), Bhattacharjee-
  Bhattacharya 2026 (Dobrushin ceiling), Eriksson/AIRR (conditional), Gross, Driver-Lohrenz, Hsu, Capitaine-Hsu-Ledoux.
- `gap-crux-lit-2.md` F2-F3 and line ~110: Chen-Eldan localization schemes and its Theorem 24 source (Anari-Liu-Oveis
  Gharan); SZZ Yang-Mills-Higgs Langevin, CMP 407 (2026) art. 27 (abstract level). `gap-crux-lit-nonab.md`: Goswami
  1811.00422 and Balaban-Imbrie-Jaffe(-Brydges) abelian Higgs (U(1), d = 2, 3, small e0). `gap-crux-lit-cross.md`:
  Bauerschmidt-Dagallier near-critical Ising. Row 968 2.2 quotes Chen-Eldan Proposition 39 and Lemma 40 (the
  supremum-over-tilts form, which is exactly (TILT-COV-sup)).
- Duplicate check (rule 0a): (TILT-COV-sup) and (LOC-COV) occur only in row 968 / `gap-avgcurv-max.md`, row 970
  (direction, author) and this row. This row is reading only and attacks neither.

### Step 2a (done 16:10Z): Shen-Zhu-Zhu, Yang-Mills-Higgs Langevin (full theorem read)

**Source.** Hao Shen, Rongchan Zhu, Xiangchan Zhu, "Langevin dynamics of lattice Yang-Mills-Higgs and applications",
arXiv:2401.13299v3 (TeX source read, file `higgs-revise-1.tex`); CMP 407 (2026) art. 27 per `gap-crux-lit-2.md`.
Earlier repo notes had the abstract only; this is the first theorem-level read.

**Statements read.**
- (B'E-YM) K_YM := (N-2)/4 - 8(d-1)|beta| N > 0 (gauge group SO(N), action N beta Re sum_p Tr Q_p; they say the
  results extend to SU(N) "as in SZZ22").
- Theorem 1.3 ("main3"): Higgs target S^(N-1) or G, under (B'E-YM) and (4 d alpha + (N-2) K_YM^(-1)) |kappa| < 1/2 - 1/N:
  volume-uniform LSI and Poincare for mu_Lambda, unique infinite-volume measure.
- Theorem 1.4 ("main4", mass gap): exponential decay for all observables under the same conditions; for gauge-invariant
  observables under the weaker (B'E-YM) and |kappa| < K_YM/(2N).
- Lemma (unitary gauge, `lem:lognu`) and Corollary `cor:fix-gauge`: for M = G, gauge-fixed measure nu~_Lambda on
  G^(E_Lambda) with action N beta Re sum_p Tr Q_p + 2 kappa N sum_e tr Q_e. Proof: |Hess S_1'(v,v)| <= 8(d-1) N |beta| |v|^2
  and |Hess S_2'(v,v)| = |2 kappa N sum_e tr(X_e^2 Q_e)| <= 2 |kappa| N sum_e |X_e|^2; with Ric this gives Bakry-Emery with
  K_G^nu~ = Ric - 8(d-1)N|beta| - 2|kappa|N > 0, hence volume-uniform LSI/Poincare with constant 1/K_G^nu~ and
  exponential decay of covariances (constants independent of Lambda).
- Their remark: the mass gap for M = S^(N-1) at small beta, kappa was earlier shown by Seiler (LNP 159, Theorem 3.18)
  by cluster expansion.

**Mapping to the targets.**
- The unitary-gauge measure is EXACTLY a lattice gauge model in a uniform linear link field (phi_l = kappa-multiple of
  the identity on every link). The Hessian bound used for S_2' depends only on |phi_l|, not on its direction: for any
  linear link field, on S^3 the Hessian of <phi_l, x_l> along a tangent vector v at x_l is -<phi_l, x_l>|v|^2, of size
  at most |phi_l| |v|^2 (my reading; the paper does not state the non-uniform case). So the same proof gives, for
  every phi with sup_l |phi_l| <= kappa_0, a volume-uniform Poincare constant and hence Var(<z, x>) <= |z|^2/K for the
  links, on the full lattice, under K = Ric - (plaquette Hessian bound) - kappa_0 > 0.
- Verdict: a WEAKER FORM of (TILT-COV-sup): (i) strong coupling only (|beta| < 1/48 in their SU(2) normalisation;
  row 955 converts SZZ to beta_W < 1/12), far below beta 2.3-2.6; (ii) bounded tilts only, sup_l |phi_l| below a
  constant of order Ric; (TILT-COV-sup) is a supremum over ALL phi in R^N; (iii) full-lattice Gibbs measure, not the
  two-slice law J_(b,phi) whose factors m are boundary laws of a half-space vacuum. It does not give (LOC-COV). The
  Bakry-Emery route cannot reach large tilts: -<phi_l, x_l> has Hessian of size |phi_l| of both signs on S^3, so no
  global curvature bound survives |phi_l| > Ric, although large tilts make each link nearly Gaussian (variance of
  order 1/|phi_l| in the tangent directions near phi_l/|phi_l|).

### Step 2b (done 16:25Z): the "zero field is the worst tilt" inequality (Ding-Song-Sun; Abdelghani-Bauerschmidt-Bodineau-Dagallier 2026)

**Sources.** O. Abdelghani, R. Bauerschmidt, T. Bodineau, B. Dagallier, "The Ding-Song-Sun inequality for a class of
even ferromagnets", arXiv:2609.08980v2 (TeX source read, Section 1 and Theorem 1.1). The original: J. Ding, J. Song,
R. Sun, "A new correlation inequality for Ising models with external fields", PTRF (2023) (MR4586225; quoted through
the 2609.08980 text, not read in its own text).

**Exact statement (Theorem 1.1 of 2609.08980).** Measures mu^u(d sigma) proportional to
exp[-(1/2)(sigma, A sigma) + (sigma, u) - sum_x V_x(sigma_x)] d sigma on R^Lambda, Lambda finite. Assume A ferromagnetic
(A_xy <= 0 for x != y) and strictly positive definite, V_x in C^3 even, unbounded above, V_x' convex on [0, infinity)
(the Ellis-Monroe-Newman GHS class). Then for all g in R^Lambda, h in R_+^Lambda, x:
<sigma_x>_(g+h) - <sigma_x>_(g-h) <= <sigma_x>_h - <sigma_x>_(-h). Consequence quoted there (from DSS):
<sigma_x; sigma_y>_g <= <sigma_x; sigma_y>_0 for EVERY external field g in R^Lambda (arbitrary signs), every x, y.
Proof method: parabolic maximum principle for a Polchinski-type flow of a doubled system. Constants: none; it is an
exact comparison, uniform in Lambda and in g. The abstract says this is the input that gives LSI for Ising and phi^4
"up to and at the critical point" (through the Bauerschmidt-Dagallier criterion, `gap-crux-lit-cross.md`).

**Mapping.** This is precisely the SHAPE of (TILT-COV-sup): a supremum over all linear tilts of the covariance,
reduced to the zero-field covariance, which for our system is known exactly (Lemma Z of row 968: k0 Id). If an analogue
held for J_(b,phi) on horizontal vectors, Theorem POL-BR of row 968 would give alpha_s >= alpha0_s and row 968 3.4 would
apply. It does NOT transfer, for three stated reasons:
- One-component real spins with a ferromagnetic PAIR interaction and an even GHS single-spin potential. Our spins
  are S^3-valued (four components with a constraint), the interaction is the four-link plaquette term
  -beta sum_p (1/2) tr x_p plus the time-like pair term b <x, w>, and the boundary law m carries the whole half-space.
  No ferromagnetic/GHS structure is available for SU(2): the plaquette term is not a sum of products of the
  coordinates with non-negative coefficients in any coordinates I know, and correlation (GKS/GHS) inequalities for
  non-abelian lattice gauge theories are not in the literature read here (Ginibre-type inequalities are abelian).
- Row 968 4.2-4.4 and Lemma NEC show the zero field CANNOT be the worst tilt for compact U(1) in its Coulomb phase,
  for Q_8, 2T, or for SU(2) on a fixed small box at large beta; a DSS-type comparison would contradict Lemma NEC there.
  So any SU(2) analogue would have to use the box size against the confinement scale; DSS has no such input.
- GUIDE only (row 968 7.5, a run, not evidence for a proof): for SU(2) at beta 2.3, chi(kap; k_min) = 0.27-0.31 at
  kap = 1.0-1.4 against the zero-field 0.25. So the DSS comparison "<.;.>_phi <= <.;.>_0" is (numerically) FALSE for
  the SU(2) half-space slice; the right SU(2) target is a box-uniform kbar larger than k0, not k0.
Verdict: gives neither (TILT-COV-sup) nor (LOC-COV); it is the published model of the reduction that (TILT-COV-sup)
would need, and it identifies the missing input as a correlation inequality, which SU(2) does not have.

### Step 2c (done 16:40Z): Higgs-tilted lattice gauge models; the Osterwalder-Seiler-Fradkin-Shenker regions (item (a))

The frozen-length fundamental Higgs model in unitary gauge is a lattice gauge model with the uniform linear link tilt
kappa sum_l (1/2) tr U_l, the family of row 968 4.8 and 7.2. Sources read:

- **S. Chatterjee, O. Yakir, "Correlation decay for U(1) lattice Higgs theory: the case of small mass",
  arXiv:2509.19176v1 (TeX read, Section 1).** Model: U(1), action beta sum_p cos(d theta_p) + alpha sum_e cos theta_e
  (unitary gauge), free b.c. on boxes Lambda_n, d >= 2. Theorem 1.1: for every m > 0 and beta >= beta_0(d, m), with
  alpha = m beta, |E[theta_x theta_y] - E theta_x E theta_y| <= C e^(-c dist(x, y)), C, c uniform in n. Method: GJS cluster
  expansion around the massive lattice Proca field (after Balaban-Imbrie-Jaffe-Brydges). Their summary of the
  earlier rigorous regions (I take it as the authoritative secondary statement; Osterwalder-Seiler Ann. Phys. 110 (1978)
  440 and Seiler LNP 159 (1982) were NOT read: no abstract on Crossref, Springer bot check):
  (I) beta small, ANY m >= 0 (Osterwalder-Seiler; Seiler's book); (II) beta and m = alpha/beta both large (Seiler's book;
  Fradkin-Shenker appendix). Shen-Zhu-Zhu (step 2a) cite Seiler Theorem 3.18 for small beta, kappa with target S^(N-1).
- **C. Bonati, G. Cossu, M. D'Elia, A. Di Giacomo, "Phase diagram of the lattice SU(2) Higgs model",
  arXiv:0911.1721v2, Nucl. Phys. B (2010) (TeX read: Sections 1, endpoint, conclusions).** NUMERICAL, not a theorem.
  Action beta sum (1 - (1/2) Re Tr P) - (kappa/2) sum Tr[phi^+ U phi] (fixed length; in unitary gauge a uniform link
  tilt kappa Re tr U on ALL 4D links). Finding: a line of first-order transitions with an endpoint at
  beta_c = 2.7266(16) (second estimate 2.7299(36)); for beta < beta_c a crossover. They describe the Fradkin-Shenker
  theorem (from the Osterwalder-Seiler expansion) as analyticity of every local observable in a region near beta = 0
  and kappa -> infinity, connecting confinement and Higgs regimes.
- **R. Ikeda, S. Kato, K.-I. Kondo, A. Shibata, arXiv:2308.13430 (TeX grep only).** Numerical claim of a further
  transition line seen only by a non-local (gauge-independent but non-local) operator; they state that it does not
  contradict OSFS because the cluster expansion covers local observables with finite support. Not used further.

**A classical uniform-in-field bound (RECALLED, not re-read here: Dobrushin's uniqueness theorem with Follmer's
covariance estimate, JFA 46 (1982), and Gross, CMP 68 (1979)).** For a Gibbs measure on a product of compact spaces,
if the Dobrushin matrix C_ij (total-variation influence of site j on the conditional law at i, a supremum over
boundary values) has row sums sup_i sum_j C_ij <= c < 1, then |Cov(f, g)| <= (1/4) sum_ij delta_i(f) [(I - C)^(-1)]_ij delta_j(g)
(delta_i the oscillation in site i). A single-site tilt changes only the a priori measure of a site, and the
standard bound of C_ij by the oscillation of the coupling terms joining i and j does not depend on that measure. So the
covariance bound is uniform in EVERY single-site field. For links with plaquette coupling (beta/2) tr U_p in d = 4,
each link meets 18 others through 6 plaquettes, and the oscillation of (beta/2) tr U_p in one link is 2 beta; the
condition holds only for beta of order 1/20 or less (order-of-magnitude count, mine; constants not checked).
Then, since delta_l(<z, x>) = 2|z_l| on S^3, Var(<z, x>) <= sum_ij |z_i| |z_j| [(I - C)^(-1)]_ij <= |z|^2/(1 - c) for all phi
(the last step by the Schur test, assuming the column sums of C are also <= c, as they are by the lattice symmetry).

**Mapping to the targets.**
- Region (I) and the Dobrushin bound are the only published statements I found that are UNIFORM IN THE TILT, and both
  need small beta (strong coupling, beta of order 0.05-0.1 for SU(2) in the Wilson normalisation; compare row 955: SZZ
  beta_W < 1/12, Bhattacharjee-Bhattacharya's Dobrushin ceiling beta_W < 2/9 for the transfer gap). They give a weaker
  (TILT-COV-sup): full lattice Gibbs measure, all phi, beta far below 2.3. Region (II) is uniform only for large
  tilts AND large beta, with m = kappa/beta large; it says nothing at intermediate tilt, which is where the row 968
  run sees the rise. Chatterjee-Yakir is U(1), large beta: the Higgs mass gap there does not bound tilts of size
  O(1) at beta 1.3 (row 968 control), and it is not uniform in m.
- At beta 2.3-2.6 with a UNIFORM tilt on ALL 4D links, the only information is numerical (Bonati et al.): no
  transition below beta_c about 2.73, so bulk susceptibilities are expected bounded at each kappa there. GUIDE only.
  Two gaps to the target remain even as a heuristic: (TILT-COV-sup) tilts ONE 3D layer of a confining 4D bulk (a
  boundary/surface problem, not the bulk Higgs model), and it asks for ALL link-dependent directions phi, not only
  pure-gauge ones (phi_l = h_x h_y^(-1) kappa is the only family equivalent to a Higgs field; a general phi is
  frustrated, like a random gauge-fixing source). No source treats either.
- (LOC-COV) is a link-diagonal bound on the conditional covariance of a boundary slice with boundary field y/s at
  typical y. Regions (I), (II) would give exponential decay of the covariance (hence a near-diagonal form) in their
  regimes only. Nothing at beta 2.3-2.6.

