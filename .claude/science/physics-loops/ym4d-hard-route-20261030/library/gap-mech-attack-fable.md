lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-26T07:53Z

# Row 1529, gap-mech-attack-fable: solve brief on the selective mechanism

Started 2026-11-25T19:53Z (date -u). Pinned commit e7c98d99e, branch claude/ym4d-hard-route. Author: Claude Fable 5.2
(Anthropic), high effort, Mac mini worker 1. Not yet checked by another model. Research-stage working state; no
public claim.

Machine: memory_pressure reported 37 percent free at the start, below the 50 percent floor. No numeric job is
started unless this changes; work is by hand.

## 0. Plan (written first, per the save protocol)

1. Read the seed statement and its consumer (library/gap-k2-tool-design-fable.md 3.1, lean/gapchain), rows
   1378, 1386, 1442, 1443, and the RESULT text of rows 1510 to 1527.
2. List the candidate selective inputs. For each: the 4D U(1) test, the 5D SU(2) test, the Villain test (row
   1442 Proposition VIL), the K7 test, and a grep of library/open-core.md and the FINISH rows.
3. Push the best candidate. Write each stage here before thinking further.
4. End with the exact stopping statement, why it is not equivalent to the seed, and why it is selective.

## Status log

- 2026-11-25T19:53Z file created, plan written.

- 20:13Z Section 1 written (frame; nothing new in it).

- 20:28Z Section 2 written: eight approaches, each searched on file; seven are on file, T7 is not.

- 20:30Z Section 3 written: Lemma INN, Lemma PER, Proposition BASE (proved), statement (HT) and its tests.

- 20:31Z Section 4 written: verdict, the stopping statement (HT), what is not done.

- 20:32Z Wording corrected in 1.1 (c), 3.2, 3.3 marks made exact. Row 1143 (10) was then read at its RESULT line and at `gap-solve-astra62.md` L15: the seven charged bottom energies are at most of order n/beta, so the periodic seed needs n^2 of order beta at least.

- 20:32Z RESULT line written. Row ran 19:53Z to 20:32Z by date -u.

- 20:33Z Full re-read of Sections 1-4. Eleven wordings tightened: marks added where a line was recalled or argued, the Feynman-Hellmann identity given its two-line proof, the rate symbol renamed c_T, item 1 of the verdict cut back to what CEN2 states. End time of the RESULT line updated.

<!-- LOG-END -->

## 1. The frame used in this row

Marks: PROVED (by hand here, checked by no one), ON FILE (with the anchor), ARGUED, OPEN, FAILS.

### 1.1 The target in the two channels

Notation of `library/gap-k2-tool-design-fable.md` 3.1. E_i are the neutral levels of H = -log T on (Z/n)^3,
E_0 the vacuum, m = E_1 - E_0, s(u) = sum over i > 0 of exp(-u (E_i - E_0)).

- (a) ON FILE (Fact PUR; Lemma B of row 1515): P_K >= 457/625 gives s(u) <= 4/21, and
  log(1 + s(u)) <= -log P_K <= 2 log(1 + s(u)). So the seed is a bound on the neutral thermal sum at the
  temperature 512/n. In one number (PROVED, one line): s(u) >= exp(-u m), so the dimensionless neutral gap
  z = n m is at least 512 log(21/4), about 849, wherever the seed holds.
- (b) ON FILE (Theorem S, `library/gap-crux-restate.md` 3.4; Lean `wilson_theoremS`, row 1525): at one fixed
  coupling a seed at one size gives a gap on all larger dyadic boxes. So the lane already has a finite-size
  criterion in law at fixed coupling. What is missing is uniformity along beta_K.
- (c) Crossed channel (PROVED in one line from the flux formalism of `gap-flux-exercise.md` 3.0-3.1; I did not
  look for this exact display on file). Read direction 1 as time: the twist in the plane (0,1) stays a time
  twist, and the twists in the planes (0,2), (0,3) become magnetic. Then
  Z_+(v) = (1/4) sum over m in Z_2^2 of Tr over H_m(n, n, v) of (P' T'^n).
  H_m is the state space of the box n x n x v with magnetic twists m in the planes (0,2), (0,3). P' projects
  on even electric flux along the short side. Reading (ARGUED): the seed asks that the magnetic twists of the
  thin box are degenerate and that its vacuum energy is additive in v between u and 2u (no Casimir term).

### 1.2 Where selectivity has to sit (ARGUED; the reading is Remark PAIR of row 1386)

- Compact U(1), d = 4, Coulomb side (massless photon recalled: Guth; Frohlich and Spencer): free photons have
  z = 2 pi at every size. The seed fails at every size,
  so every transport statement of the form "a seed at beta_w gives a seed at larger beta" is vacuous there.
  The group-reading input is the base seed.
- SU(2), d = 5 (belief): a base seed exists on the strong side of the bulk transition and none on the weak
  side. So
  the transport along the coupling is the dimension-reading input.
- Hence a proof needs both: a base that fails for U(1), and a transport that fails in d = 5. Theorem T of row
  1332 has this form ((KER) and (A2)).

### 1.3 The transport in one line (the statement is ON FILE: row 708 (VIR_K), row 1517; the identity is PROVED here in two lines and I did not look for this display on file)

Write T(beta) = exp(beta W/2) K_beta exp(beta W/2), W = sum over spatial plaquettes of (1/2) tr U_p, K_beta the
product over links of the convolution with exp((beta/2) tr g). Then for a normalized eigenvector psi_i

    - dE_i/dbeta = <psi_i, W psi_i> + Re <e^(beta W/2) psi_i, D e^(-beta W/2) psi_i>,   D = sum over links of d_beta(Casimir) >= 0.

Proof. With lambda_i = exp(-E_i): lambda_i' = <psi_i, T' psi_i>, and T' = (W T + T W)/2 + e^(beta W/2) K_beta' e^(beta W/2).
K_beta is a product over links of functions of the link Casimir with positive eigenvalues that increase with
beta, so K_beta' = D K_beta with D >= 0 commuting with K_beta; and K_beta e^(beta W/2) psi_i = lambda_i e^(-beta W/2) psi_i. QED

The first term is the spatial action insertion, the second the temporal one. The transport statement is a
relative bound: the action insertion of a low neutral level exceeds that of the vacuum by at most c_T times
its excitation energy, with c_T below about 4.0 (one loop: 2.69; GUIDE of row 1332). In continuum words: the
trace anomaly as an inequality. Free photons have c_T = 0 (ARGUED). Nothing in this row proves it at a coupling
of order one.


## 2. Approaches tested in this row, each against the file

Each line was derived from first principles here and then searched in `library/gap-*.md`, `parts/gap.md`,
`library/open-core.md` and the FINISH rows (`grep -l -i -F`). "Stops" names the first step with no proof.

| # | Approach | Why it could be selective | Where it stops | On file |
|---|---|---|---|---|
| T1 | The centre twist as a discrete stiffness (vortex free energy), carried through scales | A twisted sector of SU(2) has classical action 0 (constant transition functions i sigma_1, i sigma_2). A flux sector of Villain U(1) on a symmetric torus costs 2 pi^2 beta k^2 at every size in d = 4 | A discrete twist has no Hessian. The best case gives the flux half (string tension), not the neutral gap: a confined theory with a decoupled massless neutral field has all twist ratios near 1 | Lemma CEN and Corollary CEN2 (row 1011, `gap-pinned-cell-gauge-max.md` 4.3); row 1025 ("the flux half at one coupling, not the seed"); (T-vor) of row 1018 |
| T2 | A soft abelian twist about a colour frame, with the bracket (paramagnetic) gain | The bracket is zero for U(1); the shell sum is a logarithm only in d = 4 | A bound by a rigid link map is first order (Jensen). By gauge averaging the cost of a fixed-colour rotation depends on the potential, not on its curl. The gain is second order and needs a Ward cancellation in law | Proposition SEAG and (N1)-(N3) (row 1011, 4.4 and 7.4); Theorem C1 (row 1380); Lemma PRIV and Theorem BD (row 1034); (PARA-COVAR) of row 1526, which check 1527 rejects as a reduction |
| T3 | The time-independent gauge group as a non-abelian exact symmetry of the temporal-gauge chain. Its twist is the temporal link, and it has a bracket | The symmetry is non-abelian for SU(2) only | The direct cost of the twist is the covariant Laplacian of the slice field, not a classical form (the same mass-like term as SEAG). Small stiffness of this twist is the Gauss-law half (static adjoint sources are heavy), not the neutral gap (ARGUED) | Proposition A and SEAG cover the Hessian; the reading as a chain symmetry is not on file under this name (grep "Polyakov-loop effective": 1 file). No new statement results |
| T4 | Transport along the coupling from a base seed (Theorem T) | Base reads the group; transport reads the dimension (1.2) | The relative bound of 1.3 at a coupling of order one | row 708 (VIR_K), (VIR-log); rows 1515-1523 (TR2, (ABS-band), (*)); registry RB |
| T5 | Double positivity: Z_+(v; beta) is a Laplace transform in beta and a Gram form in the two halves of the time circle | none by itself | Remark SAND below: the two bounds differ by an extensive term | Lemma SQ (row 1522), Lemma CLIMB (row 1332) |
| T6 | A fundamental Higgs field of fixed length as an infrared regulator; transport in the hopping parameter | For U(1) the path meets the Higgs-Coulomb line | The corner of the plane at weak gauge coupling | R5 and b5 (i) of `gap-crux-exercise2-max.md` L264, L336; I10 of `gap-outside-box-max.md` L146 |
| T7 | Make the replica swap an inner twist of a connected group: Sp(2) with a unit 5-vector field | Section 3 | Section 3.3: the same corner as T6 | The swap as the outer twist of Pin(4): `gap-laptop-solve3-fable.md` L135-139; route COVER of `gap-band-fresh-fable.md` L110-192. The Sp(2) form: not found (grep "Sp(2)", "SO(5)", "outer automorphism": 0 files) |
| T8 | A finite computation at the base | reads the Wilson weight | cost | rows 1326, 1332 (COST, SURF) |

**Remark SAND (PROVED, three lines; no gain).** Put G(beta, beta') = Tr(P_0 T_beta^u T_beta'^u). It is the
neutral partition function of the torus n^3 x 2u with the coupling beta on one half of the time circle and
beta' on the other. So G is a Laplace transform of a positive measure in (beta, beta'), and log G is jointly
convex. G is symmetric (cyclicity of the trace). It is also the Hilbert-Schmidt inner product of P_0 T_beta^u
and P_0 T_beta'^u. Hence, with bbar = (beta + beta')/2,

    Z_+(2u; bbar) <= G(beta, beta') <= ( Z_+(2u; beta) Z_+(2u; beta') )^(1/2).

The left bound is convexity at the midpoint of (beta, beta') and (beta', beta). The right bound is
Cauchy-Schwarz. To second order in beta - beta' the two sides differ by (beta - beta')^2/8 times the variance
of the action, which is of the order of the volume. So the sandwich moves a seed only over coupling intervals of length volume^(-1/2). This
is Lemma SQ and Lemma CLIMB again.

**GUIDE for 1.2 (continuum dispersion, two polarizations, no zero modes; not a proof step).** For a free
massless vector field the swap is a reflection in the replica rotation group O(2), so the purity is the
ratio of the charge-conjugation twist: P = product over modes of tanh(u omega/2). At u = n/512 this gives
log P = -(512^3) pi^2/24, about -5.5e7, at every size. SU(2) has no replica rotation.


## 3. The construction not found on file: the swap as an inner twist (T7)

Idea. The purity is the ratio of a twisted partition function of two replicas: the twist is the swap
(ON FILE: rows 1115-1122; `gap-laptop-solve3-fable.md` L135-139, which notes that the swap is outer in Pin(4)
and so cannot be spread). Here the two replicas are put inside the connected group Sp(2), where the swap is
conjugation by a group element, and a unit 5-vector field with hopping kappa restores Sp(1) x Sp(1) at
kappa = infinity. This gives a one-parameter family with an exactly trivial start at kappa = 0, at every
coupling and on every torus. Sections 3.1-3.2 are proved. Section 3.3 is where the route stops.

### 3.1 Definitions and Lemma INN

G = Sp(2), the 2 x 2 quaternion matrices g with g* g = 1. H = {diag(a, b): a, b in Sp(1)} = SU(2) x SU(2).
J = the matrix with rows (0, 1), (1, 0); J is in G and J^2 = 1. V_5 = the real 5-space of matrices
X = ((t, q), (qbar, -t)), t real, q a quaternion, with <X, Y> = (1/2) Re tr(XY). rho(g) X = g X g* maps G to
SO(5). e_5 = diag(1, -1). chi(g) = Re(g_11 + g_22).

Facts (direct checks). (i) rho(g) e_5 = e_5 exactly when g commutes with diag(1, -1), that is g in H.
(ii) rho(J) e_5 = -e_5. (iii) J diag(a, b) J = diag(b, a). (iv) chi(diag(a, b)) = Re a + Re b
= (1/2) tr a + (1/2) tr b in the 2 x 2 complex form of Sp(1) = SU(2).

The family. Lattice Lambda = (Z/n)^3 x (Z/u). Variables: V_b in G on the bonds with Haar measure, n_x on the
unit sphere S^4 of V_5 on the sites with the uniform measure. For a sign field s on the bonds,

    Z_s(beta, kappa) = integral of exp( beta sum_p chi(V_p) + kappa sum over b = (x, y) of s_b <n_x, rho(V_b) n_y> ).

Z_per has s = 1. Z_tw has s_b = -1 on the time bonds from the slice u - 1 to the slice 0 and s_b = 1 elsewhere
(the field n is antiperiodic in time). R(beta, kappa) = Z_tw / Z_per. The weight is invariant under the gauge
group G and under the global Z_2: n -> -n. R is the twist ratio of this Z_2, which is not in SO(5).

Z^0(v) is the periodic SU(2) Wilson partition function on n^3 x v with weight exp(beta sum_p (1/2) tr U_p), and
Pi = Z^0(2u) / Z^0(u)^2 is the periodic purity.

**Lemma INN (PROVED here by hand, unchecked).** For every beta >= 0 and all n, u:
(a) R(beta, 0) = 1. (b) R(beta, kappa) tends to Pi as kappa tends to infinity.

Proof. (a) At kappa = 0 both integrands are the same. (b) The weight is invariant under V_b -> g_x V_b g_y^(-1),
n_x -> rho(g_x) n_x. G is transitive on S^4. For each n choose g_x measurably with rho(g_x) n_x = e_5. By Fubini
and the invariance of Haar measure, Z_s = integral over V of exp(beta sum chi(V_p) + kappa sum_b s_b k(V_b)),
k(V) = <e_5, rho(V) e_5>. By (i), k <= 1 with equality exactly on H, and k is invariant under H on both sides.
By (ii), k(JV) = -k(V). On a seam bond put V = J V'. Then the seam weight is exp(kappa k(V')) and the seam
link is J V'. With the probability measure mu_kappa = exp(kappa (k - 1)) dV / c_kappa on G,

    R = integral of exp(beta sum_p chi(V_p^J)) prod_b d mu_kappa(V_b) / integral of exp(beta sum_p chi(V_p)) prod_b d mu_kappa(V_b),

where V^J has the factor J on the left of every seam link. The normalizations cancel. mu_kappa tends weakly to
the Haar measure of H: for delta > 0, mu_kappa(k <= 1 - delta) <= exp(-kappa delta) / c_kappa, and c_kappa is at
least a constant times kappa^(-2) (the set k >= 1 - 1/kappa has Haar measure of that order, G/H has dimension 4);
so every weak limit point lives on H, and it is invariant under left translation by H, so it is the Haar measure
of H. The integrands are continuous. In the limit all V_b are in H. For a plaquette with seam links,
(J V'_1) V_2 (J V'_3)^(-1) V_4^(-1) = J (V'_1 V_2 V'_3^(-1)) J V_4^(-1), and by (iii) the two factors of the
bracket change places. So the two SU(2) fields continue into each other across the seam and form one SU(2)
field on n^3 x 2u; by (iv) the weight is its Wilson weight. The numerator tends to Z^0(2u), the denominator to
Z^0(u)^2. QED

**Lemma PER (consumer; PROVED, the algebra is Fact PUR).** Pi >= 457/625 gives s_K(u) <= 4/21, the seed of
(M-io-exists) at this K.

Proof. T has a strictly positive kernel on the gauge-invariant functions, so its top eigenvector is positive,
hence centre-invariant. Let S be the sum of r_i^u over all levels i > 0 of all sectors. Fact PUR's two lines,
applied to the full spectrum, give S <= 4/21. The neutral sum is at most S. QED

Remark. Pi asks more than P_K: the flux levels must also be cold. The neutral form needs the centre twists
of each replica, which exist at kappa = infinity only (the bonds outside H carry both centre charges).

### 3.2 Proposition BASE (the start is free at every coupling)

**Proposition BASE (PROVED here given the convergence criterion of Kotecky and Preiss for a polymer gas,
which 32 files of the lane cite; the constants are absolute and not computed).** There are absolute
constants eps_0 > 0 and C_1, C_2 such that for every real beta, all n, u >= 1 and every kappa with
eps = e^kappa - 1 <= eps_0:

    abs(log R(beta, kappa)) <= C_2 n^3 u (C_1 eps)^u.

Proof. Fix V. Let Xi_s(V) be the integral over n of prod_b exp(kappa s_b h_b), h_b = <n_x, rho(V_b) n_y> in
[-1, 1]. Write exp(kappa s_b h_b) = 1 + f_b with abs(f_b) <= eps. Then Xi_s is the partition function of a gas
of polymers (connected sets of bonds; two polymers are compatible when they share no site) with activities
w_s(gamma) = integral of prod over b in gamma of f_b, and abs(w_s(gamma)) <= eps^size(gamma) for every V. If no
closed walk in gamma crosses the seam an odd number of times, there are signs tau_x on the sites of gamma with
tau_x tau_y = s_b on its bonds; the change n_x -> tau_x n_x gives w_tw(gamma) = w_per(gamma). Otherwise gamma
contains a closed walk of odd winding around the time circle, so size(gamma) >= u. For eps <= eps_0 the cluster
expansion of log Xi_s converges absolutely, uniformly in V. log Xi_tw - log Xi_per is a sum over clusters that
contain a polymer of size at least u; it is at most delta = C_2 n^3 u (C_1 eps)^u in absolute value. Both
Xi are positive, and R is the ratio of their integrals against the same positive weight exp(beta sum chi(V_p)).
So exp(-delta) <= R <= exp(delta). QED

Reading. For kappa <= kappa_0 the Z_2-odd states are heavy at every gauge coupling, on every torus, in every
dimension and for every pair (G, H) of this kind. So BASE is not selective. All content is in the passage of
kappa from kappa_0 to infinity at the couplings beta_K.

### 3.3 Where the route stops

**(HT)** For one l and infinitely many K: R(beta_K, kappa) >= 457/625 for every kappa >= 0, on the torus
n = l b^K, u = n/512.

- Consumer. Lemma INN (b), then Lemma PER, then (M-io-exists) by rows 1461, 1462, 1465. Hypotheses checked:
  the consumer reads s_K(u) <= 4/21 at infinitely many K for one l, and nothing else.
- Proved part. kappa <= kappa_0, every K (BASE).
- First step with no proof: the passage through the Higgs transition of this model at weak gauge coupling.
  ARGUED: at beta = infinity the model is the O(5) spin model in d = 4, and above its critical hopping the
  antiperiodic ratio is small (ordered phase, spin waves). At large finite beta the bonds outside H are
  massive vector fields above the transition, and the model is the SU(2) x SU(2) Wilson theory at a coupling
  shifted by a bounded amount. So the last part of the kappa axis is the seed again, at a nearby coupling.
  This is the obstruction R5 of `gap-crux-exercise2-max.md` L336 for the fundamental Higgs plane, with O(5)
  for O(4). I found no monotone quantity in kappa: R cannot be non-decreasing in kappa at every coupling, because at
  a fixed lattice the periodic seed fails when n^2 = o(beta) (row 1143 (10)) while R = 1 at kappa = 0.
- (HT) may be false while the seed is true: a continuous Higgs transition at beta_K would close the odd gap
  at one kappa. I recall that such transitions are of first order at weak gauge coupling (fluctuation
  induced); belief only.

Tests.

| Test | Result | Line that decides |
|---|---|---|
| (t1) compact U(1), d = 4 | (HT) fails at kappa = infinity | The same construction with G = U(2), H = U(1) x U(1), n in S^2 (the adjoint triplet), J the Weyl element. Lemmas INN, PER and BASE hold with the same proofs (G/H has dimension 2 in place of 4; the restricted weight is exp(beta cos theta) for each replica). R(beta, infinity) is the purity of compact U(1), which is small at weak coupling (massless photon: Guth; Frohlich and Spencer; recalled; GUIDE number in Section 2). The failing step is the passage from the confined side to the Coulomb side of the adjoint Higgs model |
| (t2) SU(2), d = 5 | (HT) fails at kappa = infinity under the belief that the model has no gap at weak coupling | INN and BASE do not read the dimension |
| (t4) beta grows at a fixed lattice | (HT) fails | R(beta, infinity) = Pi, and the periodic seed fails when n^2 = o(beta) (row 1143 (10); orders of the decay in rows 1144, 1215 (5)) |
| K7 | (HT) fails at a two-phase point of the one-replica weight | four vacua, one swap-odd combination: R(infinity) = 1/2 |
| (t5) equivalence and method | (HT) implies the seed's conclusion. I cannot show that the seed does not imply (HT) for the Wilson model; (HT) says more (every kappa, and the flux levels). No method beyond kappa_0 | this section |

So (HT) is a new sufficient statement with a proved start and a named consumer. It is selective. Its
unproved part contains the seed at a nearby coupling. By the rule of 2026-11-22 it is no progress, and I do
not propose a row on it. It is recorded so that a later blind pass does not derive it again.


## 4. Verdict

**Outcome.** (PUR-io) is not proved. No selective input that a consumer accepts is proved. The seed is not
disproved. This is the outcome the brief calls stopping short.

**What is proved in this row (by hand, unchecked).**

- Lemma INN: the periodic purity is the kappa = infinity value of the Z_2 twist ratio R(beta, kappa) of an
  Sp(2) lattice gauge model with a unit 5-vector field, and R(beta, 0) = 1.
- Lemma PER: the periodic purity at 457/625 gives the consumer's seed s_K(u) <= 4/21.
- Proposition BASE (given the Kotecky-Preiss criterion; constants not computed): R is within
  exp(+- C_2 n^3 u (C_1 (e^kappa - 1))^u) of 1 for small kappa, at every coupling and on every torus.
- Remark SAND: the two-coupling sandwich; it gives nothing beyond Lemma SQ.

None of these moves the seed. BASE is not selective. INN is an identity.

**The statement where I stopped.** (HT) of Section 3.3: R(beta_K, kappa) >= 457/625 for every kappa >= 0, for
one l and infinitely many K.

- Why it is not the seed rewritten: it is a statement about a different model at every finite kappa, with a
  proved part (kappa <= kappa_0) and a consumer (INN, PER, then rows 1461, 1462, 1465). It implies the seed's
  conclusion. I cannot show that the seed does not imply it. Its unproved part contains the seed at a
  coupling within a bounded shift (ARGUED), so under the lane rule it counts as no progress.
- Why it is selective: for compact U(1) (the U(2) form) and for d = 5 the start holds and the end fails; the
  failing step is the passage from the confined side to the Coulomb side of the Higgs model. It also fails
  when beta grows at a fixed lattice and at a two-phase point of the one-replica weight.

**The statement on the lane's main line where every other approach of Section 2 stopped** (ON FILE, not
mine): the relative transport bound of 1.3 at a coupling of order one, in the forms (VIR-log), (ABS-band)
and (*) of rows 708 and 1515-1523. T1, T2 and T3 stop before it: they reach the flux half or the Gauss-law
half, or need the Ward cancellation (N2).

**What this row adds to the direction record (a judgment, not a theorem).**

1. By Corollary CEN2 the configuration-independent link multipliers that keep the action are central; for
   SU(2) they are discrete. The exact twists I found are the centre twists and the replica swap (gauge
   twists are trivial). The centre twists read the flux half. Only the swap reads the neutral gap. Making the swap inner (Section 3) does
   not make it soft: in the Sp(2) model it is still a global Z_2 outside the identity component.
2. So I found no 4D form of the 2D engine through an exact twist of the Wilson theory or of the embeddings
   tried here. A mechanism has to be a relative bound in law at order-one coupling (K-I as (N2)) or a block step
   (K-II). This agrees with rows 1386 and 1442; I add no new trigger.
3. Blind candidates to add to the list of row 1402: the inner swap in Sp(2) with a 5-vector (this file,
   Section 3); the gauge group of the temporal-gauge chain as the symmetric twist (T3); the two-coupling
   Gram and Laplace sandwich (Remark SAND).

**Not done.** No numeric run (memory stayed at 36 to 37 percent free, below the 50 percent floor). No Lean.
The Sussman-Alpoge repository was not read in this row: nothing here uses their text beyond what the cited
rows already credit (the kernel of Q2 in `gap-k2-tool-design-fable.md` 3.2 is theirs, with Claude and Codex
as authors of their text). The constants of BASE are not computed. The claims marked ARGUED in 3.3 (the
O(5) corner, the bounded coupling shift above the Higgs transition, first order of that transition) are
not proved. Credit: Osterwalder and Seiler, and Fradkin and Shenker, for the Higgs-plane picture recalled in
T6 and 3.3; Kotecky and Preiss for the polymer criterion; 't Hooft for the twist formalism of T1.

**For the cross-provider check.** Lemma INN (b): the weak limit of mu_kappa and the seam algebra. Proposition
BASE: the claim that a polymer with no odd closed walk has equal twisted and periodic activity, and the
uniformity in V. Lemma PER: the positivity step. The table of Section 2: each "on file" anchor.

RESULT: Row 1529 (Claude Fable 5.2 high, Mac mini worker 1, 19:53Z to 20:33Z by date -u, author only, unchecked, no numeric run, no Lean): (PUR-io) NOT proved; no selective input for a consumer proved; the seed NOT disproved. Eight approaches were derived from first principles and searched on file; seven are on file (centre-twist stiffness reads the flux half only, Lemma CEN and row 1025; colour-frame twist is (N1)-(N3) of row 1011 with first-order bounds blind, Proposition SEAG and Theorem C1; the gauge group of the temporal-gauge chain gives the Gauss-law half; transport along beta is (VIR-log), (ABS-band), (*) of rows 708 and 1515-1523; the two-coupling Gram and Laplace sandwich is Lemma SQ again; the fundamental Higgs plane is R5 and I10; the finite base is rows 1326, 1332). PROVED by hand here, unchecked: Lemma INN (the periodic purity is the kappa to infinity limit of the Z_2 twist ratio R(beta, kappa) of an Sp(2) lattice model with a unit 5-vector field, in which the replica swap is conjugation by a group element; R(beta, 0) = 1); Lemma PER (periodic purity at least 457/625 gives s_K(u) at most 4/21); Proposition BASE (given the Kotecky-Preiss criterion, constants not computed: abs(log R) at most C_2 n^3 u (C_1 (e^kappa - 1))^u for small kappa at every coupling, torus and dimension, so not selective); Remark SAND (no gain). Stopped at (HT): R(beta_K, kappa) at least 457/625 for every kappa at least 0, for one l and infinitely many K. Consumer: INN, PER, then (M-io-exists) by rows 1461, 1462, 1465. Selective: the start holds and the end fails for compact U(1) (the U(2) form) and in d = 5 (belief), and it fails at a fixed lattice when n^2 = o(beta) and at a two-phase point. Not the seed rewritten in form (a different model at finite kappa, with a proved part), but I cannot show that the seed does not imply it, and its unproved part, the Higgs transition at weak gauge coupling (obstruction R5 with O(5) for O(4)), contains the seed at a nearby coupling (ARGUED); so it is no progress under the rule of 2026-11-22 and no row is proposed. Open: (PUR-io), the relative transport bound at a coupling of order one, the Ward cancellation (N2), the mass gap.
