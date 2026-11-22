lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-22T17:57Z

# The short step as one conditional-variance inequality (row 1383)

Provenance: Claude Fable 5.2, high effort, Mac mini worker 1, pinned commit 2df402783. Not checked by another model.
Not an audit. Started 2026-11-22T05:57Z (date -u).

Moves: mechanism M-D of row 1380 (Section 5, row 3), "dressed moves". Item on the path: the mass-gap seed of the gap
lane. If (BUB) is proved in the window, the short step has a sign and the lane gets a first selective inequality. If
it is disproved or shown equivalent to the seed, M-D is closed and the lead does not queue it again.

## 0. Plan and status log

Plan (one step per response, each appended here before the next):

1. Read the row's sources: row 1380 Section 4-5, row 1018 (short step in three forms), row 1244 (Lemma 2.1, split of
   F'', Proposition 2.3), rows 1026 and 1034 ((SYM), Theorem BD), row 1012 (Balaban CMP 109 Ward-Takahashi quote).
   Repo search and registry grep (rule 0a, Repo first).
2. Fix one explicit gauge-covariant block map of ratio 2 and one explicit lift of a block move. Write the exact
   identity: cost of the block move under the blocked law = cost of the lift under the Wilson law minus the mean
   conditional variance of the lift's divergence term.
3. State (BUB). Run the tests: compact U(1), SU(2) in five dimensions, SU(2) with an adjoint Higgs factor,
   weak coupling against Balaban's Ward-Takahashi identification of the marginal term.
4. Equivalence question: is (BUB) equivalent to the seed (rule "Equivalent is not progress")?
5. Prove or disprove (BUB) in the window beta 2.3 to 2.6; if neither, a GUIDE run (criteria written first, numeric
   lock) for the sign, and what a proof would need.

Status log (times by date -u in the same command):

- 2026-11-22T05:57Z file created with the plan. Nothing proved yet.
- 06:09Z Section 1 written: sources, registry grep, design. Identity next.
- 06:10Z Section 2 written: Proposition LIFT, three explicit lifts, Lemma THIN, lab-frame reduction (PROVED, unchecked). (BUB) forms and tests next.
- 06:18Z Section 3 written: three forms of (BUB), free-field control (run 1 void by a script bug, run 2 passes), Theorem U1 (literal form holds for compact U(1): not selective), Lemma THIN consequences. Weak coupling and Balaban next.

## 1. Sources read, registry matches, and the design (written 06:09Z by date -u)

Credits. The split "response = direct term minus variance" is Lemma FLOW of row 1018 (Claude Fable 5.2,
`gap-short-step-max.md` L217-231). Its Gaussian form with the best flow is Lemma 2.1 of row 1244 (Claude Opus 5.5,
`gap-mini-solve-aa-opus.md` L115-142), which also says where the one-loop running sits (Proposition 2.3). The
corner formalism and Lemma WN are row 1013's (`gap-invent-selective-max.md` L101-102). (SYM), Proposition LF and
Theorem BD are rows 1026 and 1034. The quotation of Balaban, Commun. Math. Phys. 109 (1987), (0.18)-(0.22) and
p. 258, is row 1012's (`prior/gap-gauge-stiffness-read-opus.md` L109-115). Block maps with staples are Swendsen's;
the averaging block map and the background minimiser are Balaban's. The row itself was proposed by row 1380.

**Read in full:** FINISH.md rule sections (L52-73, L299-351) and row 1383; row 1380 Sections 1-5; row 1018
Sections 2 and 4 (Lemmas FLOW, PROJ, FR+, SPLIT, sizes); row 1244 Steps 1-3; row 1012 Step 5 (B1); row 1243
Step 3 ((S-V)). **Read by RESULT line and headings only:** rows 1026, 1034. **Not read:** Balaban's paper itself
(row 1012's quotation is used); the rest of the lane.

**Registry grep (rule 0a), `/usr/bin/grep -l -i -F` over `library/gap-*.md`, `library/prior/gap-*.md`,
`parts/gap.md`; `library/open-core.md` has no hit for "(BUB)" or "conditional variance".**

| Term | Files | What is on file |
|---|---|---|
| "(BUB)", "dressed move", "bubble minus" | 1 (row 1380) | only the proposal of this row |
| "blocked law", "block move" | 4, 2 | rows 1290/1297 ("straight blocked law", another object); no cost identity |
| "one-link Fisher", "Monte Carlo renormalization", "harmonic lift" | 0 | not on file |
| "MCRG", "Swendsen" | 1, 2 | literature notes only |
| "Fisher information" | 19 | (FC), Theorem BR of rows 940/941 (heat-flow contraction of Fisher information; another object); row 1371/1374 (Fisher bound of chord coordinates given all other links) |
| "step scaling" | 22 | killed as a seed supplier in `gap-phys-seed.md` Part 2 (row 720) and `gap-mid-max.md`; a ratio of sizes, not a block law |
| "(S-V)" | 6 | row 1243: an explicit flow whose direct term is below the abelian value; OPEN |
| "straight transport" | 20 | row 1145 (near-Haar straight transports, a sup-norm class), rows 1353-1360 |

So the identity of this row is the blocked form of Lemma FLOW and is not on file. The nearest statements are
Lemma FLOW (pin response, one scale) and row 1244's Gaussian split.

**The design, and what the reading already shows.** Section 2 gives the identity for every block map and every
lift (Proposition LIFT). Three facts about the wording of (BUB) follow from the sources and are proved or tested
below; I state them here so that a reader sees the direction at once.

1. A block move needs a colour direction. For a lab-frame direction the cost under any gauge-invariant law is
   site-local (Lemma WN applied to the blocked law). So "the classical curl form" has a frame-free meaning only
   through one number per law: the one-link Fisher information J (Section 3). For frame moves rows 1026/1034
   bind ((SYM), Theorem BD).
2. The reference matters. With the bare classical form as reference, (BUB) holds for compact U(1) at every
   coupling, by the plaquette tadpole alone (Section 4). So the literal form is not selective.
3. With the previous level as reference (J at level k + 1 against J at level k) the statement is canonical, but
   it is a statement about all levels through the band, and it depends on the block map (Section 4, Lemma THIN:
   for straight-path decimation J tends to 0 in every model).

## 2. The identity (Proposition LIFT), one explicit block map, explicit lifts (written 06:10Z by date -u)

Everything in this section is PROVED by hand by Claude Fable 5.2 in this session and checked by no one.

### 2.1 Setting and notation

- Fine lattice: the torus (Z/nZ)^d, n even, n >= 4, d >= 2. E is the set of fine links, X = SU(2)^E, dU the
  product Haar measure. Wilson law mu(dU) = Z^(-1) exp(A(U)) dU, A = beta sum_p x_p, x_p = (1/2) tr U_p,
  xbar = E_mu[x_p].
- Lie algebra: T_a = (i/2) sigma_a, so T_a^2 = -1/4 and exp(theta T_a) is a rotation by the angle theta in the
  adjoint representation. Left derivative of the link l: (d_l^a f)(U) = (d/d eps) f(..., exp(eps T_a) U_l, ...) at
  eps = 0. A vector field is W = sum over l, a of w_l^a(U) d_l^a; div W = sum d_l^a w_l^a. Haar measure is
  invariant under left translations, so for smooth g: the integral of (W g) e^A dU = - the integral of
  g (W A + div W) e^A dU. Force: N_l^a = d_l^a A.
- Coarse lattice: the sites y with even coordinates; a coarse link c = (y, mu) runs from y to y + 2 e_mu.
  Y = SU(2)^(E'), E' the coarse links.
- **Block map S_alpha (ratio 2; Swendsen's form).** For 0 <= alpha < 1/(2(d-1)) put
  Sigma_c(U) = U_(y,mu) U_(y+mu,mu) + alpha sum over nu != mu and both signs of the path of the same two steps
  displaced by +- e_nu (first step +- e_nu, last step back). Sigma_c is a positive multiple of an SU(2) matrix
  (its norm is at least 1 - 2(d-1) alpha > 0), and C(U)_c = Sigma_c / |Sigma_c|. C is smooth and gauge
  covariant: C(U^g)_c = g_y C(U)_c g_(y+2 mu)^(-1). alpha = 0 is the **straight-path decimation D**:
  C(U)_c = U_(l1) U_(l2), l1 = (y, mu), l2 = (y + mu, mu).
- **Kernel.** For 0 < kappa < infinity: k(V|U) = prod_c phi_kappa(C(U)_c^(-1) V_c), phi_kappa(h) =
  exp(kappa x(h)) / z(kappa), x(h) = (1/2) tr h, z(kappa) = 2 I_1(kappa)/kappa. The joint law is
  P(dU, dV) = mu(dU) k(V|U) dV and the blocked law nu is its V-marginal; nu has a smooth positive density.
  kappa = infinity is the deterministic map, nu = C_* mu. For every kappa, nu is invariant under the coarse
  gauge group and under the lattice symmetries that keep the coarse lattice.
- **Score and cost.** For a smooth vector field W on Y, a function Psi' in L^2(nu) is the nu-divergence of W
  if E_nu[W f] = - E_nu[f Psi'] for every smooth f. If nu = e^(A') dV with A' of class C^1, then
  Psi' = W A' + div W. The **cost** of W under nu is E_nu[Psi'^2]. (E_nu[Psi'] = 0, so the cost is a variance.)
  The **one-link Fisher information** of a gauge-invariant law rho is J(rho) = the cost of the field d_c^a
  under rho (the same for every colour a and every link c, by symmetry). For Wilson,

    J(mu_beta) = E[(N_l^a)^2] = - E[d_l^a d_l^a A] = (beta/4) sum over p containing l of E x_p = (d-1) beta xbar / 2,     (2.1)

  because (d^a)^2 x_p = (1/2) tr(T_a^2 U_l M) = - x_p / 4. In d = 4: J(mu_beta) = (3/2) beta xbar.

### 2.2 Proposition LIFT (the exact identity)

Let W be a smooth field on Y (coefficients depend on V only) and W~ a smooth field on X x Y tangent to X
(coefficients may depend on U and V). Put WW = W~ + W and

  Psi = WW log(e^A k) + div_X W~ + div_Y W.

Then, for every smooth f on Y, E_nu[W f] = - E_P[f(V) Psi]. So Psi'(V) = E_P[Psi | V] is the nu-divergence of W.
It does not depend on W~. Further

  (LIFT-1)   E_nu[Psi'^2] = E_P[Psi^2] - E_P[ Var(Psi | V) ],
  (LIFT-2)   E_P[Psi^2] = - E_P[WW Psi].

In the deterministic case (kappa = infinity) the same holds with W~ a field on X that is C-related to W
(dC_U(W~(U)) = W(C(U))), Psi = W~ A + div W~, and P replaced by mu, V by C(U).

In words: **the cost of the block move under the blocked law is the cost of the lift under the Wilson law minus
the mean conditional variance, given the block field, of the lift's divergence.** (LIFT-2) says that the cost of
the lift is a direct term, the mean of a second derivative. This is Lemma FLOW of row 1018 for a block map in
place of a pin: there H = - E[V Psi_V] - Var(Psi_V); here the variance is conditional on the block field.

Proof. e^A k is a smooth positive density on the compact group X x Y, so E_P[WW g] = - E_P[g Psi] for every
smooth g. With g = f(V): WW f = W f, and E_P[W f] = E_nu[W f]. With g = Psi: (LIFT-2). E_P[f Psi] =
E_nu[f E_P[Psi | V]] gives the second claim, and (LIFT-1) is the law of total variance. Two lifts differ by a
field ZZ tangent to X; ZZ f = 0, so E_P[f Psi_ZZ] = 0 for every f and E_P[Psi_ZZ | V] = 0. In the deterministic
case W~(f o C) = (W f) o C, and the integration by parts is on X. QED

**Corollary (blind half; data processing).** cost_nu(W) <= E_P[Psi^2] for every lift, with equality if and only if
Psi is a function of V. So every explicit lift gives an upper bound that never loses, and the best lift has a
V-measurable divergence. This is clause (L1) of row 1018's contract.

### 2.3 Three explicit lifts of the one-link block move W = d_c^a

(a) **Kernel lift** (every alpha, kappa < infinity): W~ = 0. Then Psi = d_c^a log k = (kappa/2) tr(T_a V_c C(U)_c^(-1)).
Given U, V_c C_c^(-1) has the law phi_kappa, so E[Psi^2 | U] = (kappa/4) u(kappa), u(kappa) = I_2(kappa)/I_1(kappa),
whatever U is. So

  J(nu) = (kappa/4) u(kappa) - E_P Var( (kappa/2) tr(T_a V_c C(U)_c^(-1)) | V ).                              (2.2)

(b) **First-link lift** (alpha = 0, every kappa <= infinity): W~ = d_(l1)^a. Left rotation of U_(l1) and of V_c by
the same element keeps k, and W~ is C-related to W. Psi = N_(l1)^a. So d_c^a log nu (V) = E[N_(l1)^a | V] and

  J(nu) = J(mu_beta) - E Var( N_(l1)^a | V ) = (d-1) beta xbar / 2 - E Var( N_(l1)^a | V ).                   (2.3)

(c) **Spread lift** (alpha = 0; stated for the decimation of ratio m, V_c = U_1 U_2 ... U_m along one line; ratio 2
is m = 2). Put P_j = U_1 ... U_(j-1) and D_j = the derivative of link l_j along P_j^(-1) T_a P_j (the colour axis
a of the coarse site, carried to the tail of l_j). For weights w_j with sum 1, W~ = sum_j w_j D_j is C-related
to W (to first order each factor inserts w_j T_a on the left of V_c), and div W~ = 0 (the coefficient on l_j
does not depend on U_(l_j)). Psi = sum_j w_j D_j A.

**Lemma THIN.** For the decimation of ratio m >= 1 in any dimension d >= 2, at every beta > 0 and every kappa:

  J(nu) <= J(mu_beta) / m = (d-1) beta xbar / (2m).

Proof. E[Psi^2] = sum over j, j' of w_j w_j' E[(D_j A)(D_j' A)]. For j > j': E[(D_j A) g] = - E[D_j g] (D_j has
divergence zero) with g = D_j' A. The coefficient of D_j' depends only on the links before l_j', so D_j g is a
combination of mixed second derivatives of A in l_j and l_j'. Two links of one line lie in no common plaquette,
so it is zero. For j = j': D_j D_j A is the second derivative of A along a direction b with b^2 = -1/4 that does
not depend on U_(l_j); it equals - (beta/4) sum over p containing l_j of x_p. So E[(D_j A)^2] = J(mu_beta) and
E[Psi^2] = J(mu_beta) sum_j w_j^2. Take w_j = 1/m and use the Corollary. QED

The proof uses only: collinear links share no term of the action. It holds for every compact group with the
matching constant, for compact U(1), in five dimensions and with matter fields that sit on sites. It is the
Fisher-information form of the perimeter law: a thin transport is rough for ultraviolet reasons.

### 2.4 Lab-frame block moves see only the site matrix (Lemma WN for the blocked law)

Let W = sum_c theta_c d_c^a with real constants theta_c. By 2.2 its score is sum_c theta_c N'_c^a with
N'_c^a = d_c^a log nu. Under a coarse gauge map g the vector N'_c turns by Ad(g) at the tail of c. nu is gauge
invariant, so E_nu[N'_c^a N'_c'^b] = 0 when the tails differ (average over g at one tail), and it is
delta_ab kappa(c, c') when they agree. So

  cost_nu(theta a) = sum over coarse sites y of sum over c, c' with tail y of theta_c theta_c' kappa(c, c').

The cost of a lab-frame block move is site-local for every gauge-invariant law. This is Lemma WN of row 1013,
applied to nu; with rotations at both ends of the links the form lives on the 8 link-ends at a site, and for
d = 4 lattice symmetry leaves two numbers (the form is zero on constants by the Gauss law, and the other two
isotypic parts under the hyperoctahedral group, of dimensions 3 and 4, are irreducible). I use one number, J(nu).

Consequence for the wording of the row. **For a lab-frame block move there is no curl form on either side of
the identity.** A curl form in d theta exists (i) for an abelian group, where Ad is trivial and the cross terms
survive; (ii) for a frame move, where rows 1026 and 1034 bind: the cost is a curl form only if the current
j - d is conserved ((SYM)); link frames have it with zero gain (Proposition LF), pin-measurable site frames do
not have it at a pinned face (Theorem BD); (iii) in the background-field sense of Balaban (Section 5), which is
not a move of the block field but a second derivative of the effective action along the classical minimiser.
So the frame-free content of "the cost of a block move" is the one-link Fisher information J (and one more
number of the site form). Section 3 states (BUB) in this form.

## 3. (BUB) in three exact forms; the U(1) test decides the literal form (written 06:18Z by date -u)

### 3.1 The reference, and three forms

The row words (BUB) as "variance term minus the excess of the lift cost over the classical curl form >= c > 0".
By (LIFT-1) this is the same as "cost of the block move under nu <= reference - c". The statement depends on
the reference. For the one-link move the candidates are these.

- Free blocked form. C_lin is the linear map of link angles that the block map gives at U = 1 (for the
  decimation D: the sum of the two angles). Q_C(t) = min{ |d t~|^2 : C_lin t~ = t } and q_C = Q_C(e_c) for one
  coarse link. The minimiser is the **harmonic lift**. For the identity map q = 2(d-1). rho_C = q_C / (2(d-1)).
- By (2.1) the free value of J for SU(2) Wilson is (beta/4) 2(d-1), so the classical value of the coarse cost is
  J_cl = (beta/4) q_C. (For compact U(1) with A = beta sum cos F_p: J(mu) = 2(d-1) beta xbar and J_cl = beta q_C.)

  (BUB-lit)   J(nu_beta) <= (beta/4) q_C - c.            Reference: the bare classical form. The row's wording.
  (BUB-d)     J(nu_beta) <= rho_C J(mu_beta) - c.        Reference: the fine cost, with its plaquette tadpole, times the free ratio.
  (BUB-lev)   J(nu^(k+1)) <= J(nu^(k)) - c for every level k >= k_0 with J(nu^(k)) >= j_0.   Reference: the level before.

nu^(k) is the law after k block steps of one fixed kind. In d = 4 the free blocked form of an averaging map
tends to a fixed form (classical scale invariance), so (BUB-lev) needs no free ratio.

### 3.2 Control numbers for the free field (GUIDE grade: floating point, not a proof)

Script `/tmp/row1383/run/gauss_block.py` and `gauss_block2.py` (scratch, not in git), run under the numeric lock
(holder row1383-fable, acquired 06:12Z, released 06:16Z; 61-65 percent memory free). It computes
Q^(m)_cc = mean over coarse momenta of the diagonal of (C G C^*)^(-1) for the free U(1) field (G = (d* d + 1e-9)^(-1)),
for the decimation of ratio m and for a covariant averaging map of ratio m (the coarse variable is the mean
over the m^(d-1) transverse displacements u of: canonical path to y + u, m straight steps, path back).
Criteria written before the run: (a) m = 1 gives 2(d-1); (b) decimation: Q <= 2(d-1)/m (Gaussian form of Lemma
THIN); (c) the averaging coefficients map gradients to coarse gradients to 1e-10.

**Run 1 was wrong and is void.** The criteria passed, but the output contradicted a hand bound: for the
decimation of ratio 2 each of the 2(d-1) coarse plaquettes at c carries flux 1 through 4 fine plaquettes, so
q_D >= 2(d-1)/4 = 1.5 in d = 4; run 1 gave 0.28. The Fourier form of d* d was transposed (it annihilated the
conjugate of a gradient). Run 2 has the corrected form, an assertion that it annihilates gradients, and the
hand bound as criterion (b'). All criteria pass. One case of run 1 (d = 5, n = 16) passed the 2 GB limit before
the script stopped itself (2,335 MB); run 2 does not contain it (largest 1,308 MB).

| d | map | m = 1 | m = 2 | m = 4 | note |
|---|---|---|---|---|---|
| 4 | decimation | 6 | 2.1227 (coarse sides 4, 6, 8 agree to 4 digits) | 0.898 | <= 6/m; tends to 0 |
| 4 | averaging | 6 | 8.27 - 8.30 | 6.77 (coarse side 6), 7.09 (side 4) | stays of order one |
| 5 | decimation | 8 | 3.08 | 1.40 (side 3) | tends to 0 |
| 5 | averaging | 8 | 19.5 - 19.8 | 36.9 (side 3) | grows about 2 per doubling |

So q_D = 2.1227 and rho_D = 0.3538 in d = 4. The run shows what the classical scaling says: for an averaging
map the free one-link cost is scale invariant in four dimensions and grows in five; for the decimation it falls
in every dimension.

### 3.3 Theorem U1: the literal form holds for compact U(1) at every coupling (PROVED, unchecked)

Setting: compact U(1), A = beta sum_p cos F_p, F = d theta, any d >= 2, the torus of 2.1. C is a homomorphism
block map (an integer matrix, for instance the decimation of any ratio m). A block move is a real constant
field t on the coarse links; a lift is a real constant field t~ with C t~ = t.

**Statement.** For every beta > 0, every t and every lift t~:

  cost_nu(t) = beta xbar |d t~|^2 - E Var( beta sum_p (d t~)_p sin F_p | C theta ).                            (3.1)

Hence cost_nu(t) <= xbar beta Q_C(t), and with the harmonic lift

  (variance term) - (excess over the classical curl form) = beta Q_C(t) - cost_nu(t) >= beta (1 - xbar) Q_C(t)
                                                          >= (xbar / (4(d-1))) Q_C(t).                           (3.2)

Proof. The constant field t~ is C-related to t and has divergence zero. Psi = sum_l t~_l d_l A = - beta sum_p
(d t~)_p sin F_p. By (LIFT-2), E[Psi^2] = - E[t~ Psi] = beta sum_p (d t~)_p^2 E cos F_p = beta xbar |d t~|^2. (LIFT-1)
gives (3.1). The variance is >= 0, so cost_nu(t) <= beta xbar |d t~|^2 for every lift; take the harmonic one. The
excess of the lift cost over the classical form beta |d t~|^2 is - beta (1 - xbar) |d t~|^2. For the last bound:
E[(d_l A)^2] = beta sum over p containing l of E cos F_p = 2(d-1) beta xbar, and (d_l A)^2 <= 2(d-1) beta^2 sum over
p containing l of sin^2 F_p, so E sin^2 F_p >= xbar / (2(d-1) beta); and 1 - cos F >= (1/2) sin^2 F. QED

**Reading.** In compact U(1) the "tadpole" of the harmonic lift is negative: it is the plaquette tadpole
- beta (1 - xbar), of order - 1/4 in d = 4 at weak coupling (ARGUED: free equipartition, E F_p^2 = 1/(2 beta)).
The row's sentence "(U1): both terms vanish for the harmonic lift" is true for the non-compact Gaussian field
only. For the compact model (BUB-lit) HOLDS at every coupling and in every dimension, with
c = beta (1 - xbar) q_C > 0. So **(BUB-lit) is not selective. It is a statement about the plaquette tadpole.**
(BUB-d) removes this tadpole: by (3.1) compact U(1) obeys it with c = 0 at every coupling, and the true margin is
the variance of the harmonic lift, which is the variance of beta sum (d t~)_p (sin F_p - F_p) given C theta, because the
linear part beta <d* d t~, theta> is a function of C theta for the harmonic lift (Lagrange condition). It is of order
1/beta at weak coupling (ARGUED). So (BUB-d) with one c > 0 for all large beta fails for U(1), as a test wants.

### 3.4 SU(2) in the window: the literal form holds for the same reason (GUIDE grade)

For the decimation D, Lemma THIN gives J(nu_beta) <= (3/4) beta xbar in d = 4. The reference is (beta/4) q_D. So
(BUB-lit) holds with c >= (beta/4)(q_D - 3 xbar) whenever xbar < q_D/3 = 0.7076. The plaquette of SU(2) Wilson is
about 0.602 at beta = 2.3 and 0.670 at beta = 2.6 (published Monte Carlo values, RECALLED; Section 7 measures
them again). Then c >= 0.18 at 2.3 and c >= 0.07 at 2.6. This is not a proof: the two inputs are a
floating-point number (q_D) and a Monte Carlo number (xbar <= 0.7076 for beta <= 2.6; xbar is increasing in beta,
and the only hand bound I have is xbar <= 4 beta/(4 beta + 1), from Lemma NAB's inequality of row 1018, which is 0.91).
The mechanism is the plaquette tadpole, as in U(1). No bubble is needed and no bracket is used.

### 3.5 The decimation and the level form: no consumer (PROVED from Lemma THIN, given one massless model)

By Lemma THIN, for the decimation J(nu^(k)) <= J(mu)/2^k in every model whose action has no term with two
collinear links: SU(2) and compact U(1) in every dimension, Wilson or Villain weights, with site matter. So:
- "J(nu^(K)) <= j_0 at some level K" holds in massless models (GIVEN the U(1) theorem as the lane holds it, I28).
  No statement "small one-link Fisher information of the decimated law gives the seed" can be true.
- (BUB-lev) for the decimation is not selective: the levels fall to zero in every model.
For an averaging map the free field keeps J of order beta at every level in d = 4 (3.2), so there (BUB-lev)
is false for the free photon. I have no exact statement for an averaging map at finite coupling: its lifts are
not divergence-free fields of one link (the paths of different coarse links share fine links), and only the
kernel lift (2.2) is explicit.
