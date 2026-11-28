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
- 06:20Z Section 7.1 written (design and criteria of the SU(2) GUIDE run) before the batch starts. Batch launched in the background under the lock.
- 06:22Z Sections 4-6 written (tests in five dimensions and with an adjoint Higgs field; Balaban comparison, ARGUED; Lemma BOG PROVED; what a proof needs; equivalence). Batch still running.
- 06:33Z SU(2) batch done (06:20Z-06:32Z by its log): all controls pass; (BUB-lit) and (BUB-d) POSITIVE at six couplings; D levels near 0.35. Section 7.2 and the U(1) criteria 7.3 written; U(1) run next.
- 06:48Z U(1) batch done (06:33Z-06:47Z by its log): controls pass, Theorem U1's D >= 0 holds, D falls to 0. Sections 7.4, 7.5 and 8 (report, RESULT) written. Re-read of the PROVED items next.
- 06:49Z Re-read of the PROVED items done: four wording repairs (the two-number clause marked ARGUED; a proof line for "not a curl form"; "onto" in Theorem U1; "class-level" in 3.5). Finished.

## 1. Sources read, registry matches, and the design (written 06:09Z by date -u)

Credits. The split "response = direct term minus variance" is Lemma FLOW of row 1018 (Claude Fable 5.2,
`gap-short-step-max.md` L217-231). Its Gaussian form with the best flow is Lemma 2.1 of row 1244 (Claude Opus 5.5,
`gap-mini-solve-aa-opus.md` L115-142), which also says where the one-loop running sits (Proposition 2.3). The
corner formalism and Lemma WN are row 1013's (`gap-invent-selective-max.md` L101-102 and L136). (SYM), Proposition LF and
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
| "Fisher information" | 19 | (FC), Theorem BR (`gap-fc-max.md`; row 941 `gap-lsivac-max.md`: heat-flow contraction of Fisher information; another object); rows 1371, 1375 (Fisher bound of chord coordinates given all other links) |
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
isotypic parts under the hyperoctahedral group, of dimensions 3 and 4, are irreducible; this clause is ARGUED in
these two lines and not used). I use one number, J(nu).

The site-local form is not a curl form unless J(nu) = 0. Proof: take theta = d lambda with lambda the indicator of
one coarse site y. Then theta = 1 on the d links with tail y and theta = -1 on the d links with head y, whose tails
are d distinct sites. The cost is a non-negative term at y plus d J(nu). A curl form is zero on d lambda. QED

Consequence for the wording of the row. **For a lab-frame block move the cost under the blocked law is not a curl
form, and the cost of a lab-frame lift is not one either (Lemma WN of row 1013).** A curl form in d theta exists (i) for an abelian group, where Ad is trivial and the cross terms
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
block map (an integer matrix that is onto as a real map, for instance the decimation of any ratio m). A block move is a real constant
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
  No class-level statement "small one-link Fisher information of the decimated law gives the seed" (one whose
  hypotheses compact U(1) also meets) can be true.
- (BUB-lev) for the decimation is not selective: the levels fall to zero in every model.
For an averaging map the free field keeps J of order beta at every level in d = 4 (3.2), so there (BUB-lev)
is false for the free photon. I have no exact statement for an averaging map at finite coupling: its lifts are
not divergence-free fields of one link (the paths of different coarse links share fine links), and only the
kernel lift (2.2) is explicit.

## 4. The other tests: five dimensions, adjoint Higgs (written 06:22Z by date -u)

Each line says what was proved and what is only argued.

- **(5D), literal form.** Proposition LIFT, Lemma THIN and Theorem U1 do not use the dimension. So (BUB-lit)
  holds for compact U(1) in five dimensions at every coupling (PROVED), and for SU(2) in five dimensions with the
  decimation whenever xbar < q_D/4 = 0.769 (q_D = 3.08 in d = 5, Section 3.2; from Lemma THIN, GUIDE grade for
  the number). By row 1380's rule, a fact that holds verbatim in five dimensions is ultraviolet. The literal form
  is the plaquette tadpole.
- **(5D), dressed one-step form.** No exact statement. The dimension enters (BUB-d) only through the free ratio
  rho_C, which is the classical scaling of the map (averaging: between 0.8 and 1.4 per step in d = 4 and between
  1.9 and 2.4 in d = 5 by Section 3.2). After rho_C is taken out, what is left at weak coupling is a one-loop number of one
  momentum shell. Such a number exists in d = 4 and d = 5 alike (ARGUED; not computed). So I expect (BUB-d) to
  be true or false together in four and five dimensions at weak coupling. It does not see the scale.
- **(5D), level form.** For an averaging map in d = 5 the free value of J doubles at each level (3.2). So
  (BUB-lev) is false in five dimensions at weak coupling (ARGUED from the free field). This is the only form in
  which the dimension four enters: the free ratio tends to 1, so drops of order one per level are not covered by
  a classical growth.
- **(AH), SU(2) with an adjoint Higgs field on the sites.** The hopping term of a site field holds one link per
  term. So Lemma THIN holds verbatim with J(mu) the full one-link cost: the decimated law has J to 0 at every
  coupling, also in the Coulomb phase. The literal form is again decided by one-link tadpoles. For an averaging
  map the level form must fail in the Coulomb phase if the photon is there (BELIEF grade, as item A16 of row
  1017): the photon keeps a stiffness. So a proof of (BUB-lev) for pure SU(2) must use a property that the Higgs
  model lacks; this is the clause "no long-range order of an adjoint section" that row 1380 put into M-D.

Test summary.

| Form | compact U(1), d = 4 | SU(2), d = 5 | adjoint Higgs | verdict |
|---|---|---|---|---|
| (BUB-lit) | HOLDS at every beta (Theorem U1, PROVED) | holds while xbar < 0.769 (decimation; GUIDE number) | not run; set by one-link tadpoles | not selective: a tadpole fact |
| (BUB-d), one step | holds with c = 0 at every beta (PROVED); margin tends to 0 at weak coupling (ARGUED) | expected as in d = 4 (ARGUED) | not run | selective against U(1) only at weak coupling; does not see the scale |
| (BUB-lev), averaging map | false for the free photon (GUIDE numbers 3.2) | false at weak coupling (ARGUED) | false in the Coulomb phase (BELIEF) | passes the three tests; it is a statement about all levels |
| (BUB-lev), decimation | levels fall to 0 (Lemma THIN, PROVED) | same | same | not selective |

## 5. Weak coupling: the comparison with Balaban's identification of the marginal term (ARGUED; written 06:22Z by date -u)

Source: Balaban, Commun. Math. Phys. 109 (1987), as quoted by row 1012 (`prior/gap-gauge-stiffness-read-opus.md`
L109-115): A_k(g_k, V) = (1/g_k^2) A(U_k(V)) + E_k(U_k(V)) (0.22), with U_k(V) the minimiser of the action among the
fields with k-fold block average V; 1/g_1^2 = 1/g_0^2 - beta_1(g_0) (0.18) and 1/g_(k+1)^2 = 1/g_k^2 + beta_(k+1)(g_k)
(0.20), signs as printed; "gauge invariance ... identifies the action A(U_k), through a set of Ward-Takahashi
identities, as ... the marginal variable"; valid for small fields while every g_k <= gamma. I did not re-read the
paper. Nothing in this section is proved.

The dictionary with Section 2.

1. **Balaban's lift is the harmonic lift.** U_k(V) is the non-linear form of the minimiser t~ of 3.1. The first
   term of (0.22) is the classical form of the harmonic lift with the running coefficient 1/g_k^2. For a
   constant-coefficient block move W, (LIFT-2) on the coarse side gives cost_nu(W) = E_nu[- W W A_k]. With (0.22):

     J(nu^(k)) = (1/g_k^2) h_k + e_k,   h_k = E[- W W (A o U_k)],   e_k = E[- W W (E_k o U_k)].

   h_k is the mean Hessian of the classical action at the minimiser; e_k is of order one if the bounds on E_k
   carry to two derivatives (Balaban's analyticity in the field gives this on the small-field set; not derived
   here, and the large-field regions are not treated here).
2. **One step.** J(nu^(k+1)) - J(nu^(k)) = [1/g_(k+1)^2 - 1/g_k^2] h_(k+1) + (1/g_k^2)(h_(k+1) - h_k) + (e_(k+1) - e_k). The
   first term is the running: for SU(2), beta = 4/g^2 falls by (11/(3 pi^2)) log 2 = 0.2575 per doubling at one
   loop (RECALLED; the lane has this number in row 1025). The second term is the classical transient of the map
   times a LARGE factor: for the averaging map of 3.2 the free value goes 6, 8.3, 6.8, so at the first steps the
   change of J is of order beta and has no fixed sign. The third term is a change of one-loop constants.
   Balaban's own formulas name the first step apart ((0.18) against (0.20)).
3. **So the universal coefficient is the one-step drop of J only at levels where h_k and e_k have converged.**
   At the first step from the Wilson action it is one summand among map-dependent terms. This is why no
   one-step statement about the Wilson law itself can be "asymptotic freedom" in exact form, and why (BUB-d)
   needs the factor rho_C and still keeps map-dependent constants.
4. **(BUB-lev) at weak coupling is the account's own statement.** GIVEN Balaban's Theorems 1 and 2 as the
   account ports them (every g_k <= gamma), the convergence of h_k and e_k, and small large-field terms, an
   averaging map has J(nu^(k+1)) <= J(nu^(k)) - c for k >= k_0, with c near 0.2575 times the limit of h_k. Not derived
   here; it would be a corollary of the small-field expansion, and it gives nothing new where the account works.
   In the band (g_k of order one) the expansion stops, and (BUB-lev) there is M-D of row 1380, unchanged.
5. **What the Ward identities do, in the language of Section 2.** Gauge invariance of the blocked law gives the
   FORM of the cost: site-local for lab-frame moves, zero on constants (the Gauss law), two numbers per law
   (2.4). Balaban's identities do the same for the effective action: they say the marginal term is the gauge
   invariant action; its coefficient comes from the perturbative computation. In neither place does gauge
   invariance give the sign of the change of the coefficient. This agrees with rows 1243 and 1244.
6. **Where row 1244's logarithm sits in block form.** Row 1244 (Proposition 2.3) shows that a bounded flow loses
   the logarithm of the bubble, because the best flow K_* = -(1/2) G M_1 grows like 1/lambda on the infrared modes.
   Given the block field of an averaging map, the fluctuation has a mass of the order of the block scale (ARGUED;
   it is Balaban's regularity of the propagators with the averaging constraint, CMP 99, on the small-field set).
   So in one block step the conditional bubble is one momentum shell, its size is of order log 2 and not a
   logarithm of the box, and the best correction of a lift is bounded and local. In Lemma H's language (row
   1380) one step has no spread of softness and a gain of order one; the logarithm is the number of levels.
   This is the positive content of M-D, and it is ARGUED only.

## 6. What a proof would need; the equivalence question (written 06:22Z by date -u)

### 6.1 Lemma BOG: a lower bound on the variance term is a better lift (PROVED, unchecked)

Deterministic block map C, a lift W~ of W with Psi = W~ A + div W~, and a **vertical** field Z on X (dC(Z) = 0),
with D_Z = Z A + div Z. Then

  (i)   E[D_Z | V] = 0 and E[Z g | V] = - E[g D_Z | V] for every smooth g;
  (ii)  E[Z Psi | V] = E[W~ D_Z | V];
  (iii) E Var(Psi | V) >= (E[W~ D_Z])^2 / E[D_Z^2],  and  E[D_Z^2] = - E[Z D_Z].

Proof. (i) For smooth f on Y, Z(f o C) = 0, so E[f(V) Z g] = E[Z(f(V) g)] = - E[f(V) g D_Z]; g = 1 gives the first
claim. (ii) [Z, W~] is C-related to [0, W] = 0, so it is vertical and its divergence Z Psi - W~ D_Z has conditional
mean zero by (i). (iii) By (i), Cov(Psi, D_Z | V) = E[Psi D_Z | V] = - E[Z Psi | V] = - E[W~ D_Z | V]. The
Cauchy-Schwarz inequality, first given V and then for the mean, gives (E[W~ D_Z])^2 <= E Var(Psi | V) E Var(D_Z | V)
<= E Var(Psi | V) E[D_Z^2]. The last identity is (LIFT-2) for Z. QED

Reading. The right side of (iii) is what the lift W~ - s Z gains at the best s. So **every lower bound of this
kind on the bubble is an upper bound on J(nu) by an explicit lift, and its three terms are means of explicit local
functions under the Wilson law** (direct terms, by (LIFT-2)). This is Lemma 2.1 of row 1244 (direct term minus
the best Bogoliubov ratio) without the Gaussian model, in block form. Lemma THIN is the case W~ = first-link
lift, Z = the difference of the two transported link moves.

### 6.2 What a proof of a one-step form in the window would need

1. An explicit lift of finite range (for the decimation: the transported harmonic lift, or the spread lift
   corrected by a few vertical fields on the links next to the coarse line).
2. Its cost, which is a finite combination of means of local functions of the Wilson law at the coupling (small
   loops with insertions). Example: Lemma THIN needs none; (BUB-lit) through Lemma THIN needs the one number
   xbar(beta) <= 0.7076.
3. Rigorous upper bounds on these means at beta from 2.3 to 2.6. No expansion reaches these couplings, so this
   is a (K-one) number: a formal computation in the sense of `GOAL.md`, not a hand proof. I know no inequality
   that gives xbar(2.6) <= 0.7076 by hand (the bound from Lemma NAB of row 1018 gives 0.91).
So even the trivial form (BUB-lit) has no hand proof in the window. The obstruction is not the bubble. It is
that a one-step statement at an order-one coupling is a number.

### 6.3 The rule "Equivalent is not progress"

- (BUB-lit) is not equivalent to the seed and does not imply it: it holds in compact U(1) (Theorem U1).
- (BUB-d), one step, is not equivalent to the seed and does not imply it: it is one number at one lattice scale,
  compact U(1) obeys it with c = 0 at every coupling, and the blocked law is not a Wilson law, so the step does
  not repeat. It has no consumer.
- (BUB-lev) for an averaging map, at every level through the band, would give J(nu^(K)) <= j_0 at some level K. **I
  cannot show that this is not equivalent to the seed, and I cannot show that it implies the seed.** What small
  J gives by a standard route: the relative entropy of the blocked law with respect to the product Haar measure
  is at most 3 J per coarse link (Bakry-Emery for SU(2) with the metric of 2.1, where the Ricci curvature is
  1/2, and tensorisation; RECALLED, not rebuilt). That bounds the law of a bounded window (Pinsker). It gives no
  decay at long distance and no thermal count. For the decimation the implication is false (3.5). For an
  averaging map a consumer "J small gives the seed" is not on file (grep: "one-link Fisher" 0 files) and I did
  not find one.
- By Lemma ADD of row 1018 a step statement with a fixed drop restates its end point in steps unless an
  identity proves the step. Here the identity exists (Proposition LIFT) and its mechanism slot is Lemma BOG.
  The slot is filled by a number at each level, not by a sign: Section 6.2. In the band nothing fixes these
  numbers. So (BUB-lev) is M-D with an exact first statement and without a proof route; it is not progress on the
  seed in the sense of the rule.

## 7. GUIDE run: the one-link Fisher information of the decimated SU(2) law (criteria written 06:20Z by date -u, before the batch)

### 7.1 Design and criteria (fixed before the batch; a smoke test on 4^4 and a 2.5 s timing run on 8^4 were made first)

- Model: SU(2) Wilson on 8^4, periodic. Block map: the decimation D of ratio 2 (kappa = infinity). Lift: the
  spread lift Psi = (N_l1 + N_l2 carried to the coarse site)/2 of 2.3 (c), and the first-link lift N_l1 as a second
  estimator.
- Estimator: J(nu) = E[Psi(U_a) Psi(U_b)] per colour, with U_a, U_b two runs of the conditional heat bath started
  from the same Wilson configuration U and keeping V = C(U): the pair (U_l1, U_l2) of each coarse link is updated
  as g, g^(-1) V with the exact conditional weight; all other links by the usual heat bath. This is
  E[(E[Psi | V])^2] = J(nu) once the two runs are independent given V (Proposition LIFT).
- Schedule: 300 sweeps from a cold start, then 40 samples, 10 sweeps apart; 30 conditional sweeps for each
  replica, with a reading at 15. Couplings: 2.3, 2.45, 2.6 (the window) and 4, 8, 16 (trend to weak coupling).
- Script `/tmp/row1383/run/dec_mc.py` (scratch, not in git); plain numpy, quaternion links; under the numeric
  lock (holder row1383-fable), BLAS threads 1, nice, RSS guard 2 GB.

Controls (if one fails at a coupling, that coupling's result is void):
- (C1) the exact identity (2.1): the measured E[(N_l^a)^2] over all links equals (3/2) beta xbar within 1.5 percent.
- (C2) Lemma THIN's identities on the same configurations: E[N_l1 . N_l2] = 0 within 3 standard errors, and
  E[Psi^2] = J(mu)/2 within 3 percent.
- (C3) the conditional update keeps V (defect below 1e-9) and unit quaternions.
- (C4) plateau: the estimate at 15 conditional sweeps and at 30 agree within 3 standard errors of the latter
  (else the replicas are not yet independent given V and the value is only an upper bound).
- (C5) xbar at beta = 2.3 within 0.006 of 0.602 (published value, RECALLED).

Readings, with R = J(nu)/J(mu) and s its standard error (40 samples, treated as independent; a GUIDE only):
- (BUB-lit) is POSITIVE at a coupling if R < 0.3538/xbar - 3 s.
- (BUB-d) is POSITIVE if R < 0.3538 - 3 s, NEGATIVE if R > 0.3538 + 3 s, UNDECIDED otherwise.
- Trend: D(beta) = rho_D J(mu) - J(nu) at beta = 4, 8, 16. If it levels at a positive number, the first step has a
  non-abelian one-loop gain (U(1) has D to 0 by 3.3); if it levels at a negative number, the tadpole wins there.
What the run cannot do: prove a sign; say anything about an averaging map, a second level, or five dimensions.

### 7.2 Result of the SU(2) batch (GUIDE only; written 06:33Z by date -u)

Batch 06:20:47Z to 06:32:52Z by the log's own `date -u` stamps, six couplings, about 121 s and at most 63 MB each,
63-64 percent memory free; the lock was released by the exit trap ("released"). Log: `/tmp/row1383/run/batch.log`.

Controls: all pass at every coupling. (C1) measured E[(N_l^a)^2] / ((3/2) beta xbar) = 0.9987, 0.9995, 1.0020, 0.9994,
0.9977, 0.9973. (C2) E[N_l1 . N_l2] = -0.001(6), 0.005(7), 0.004(8), -0.004(14), -0.02(3), -0.11(7), each within 2
standard errors of 0; E[Psi^2] / (J(mu)/2) = 0.999, 1.003, 1.000, 0.997, 0.992, 0.993. (C3) constraint defect and unit
defect print as 0.000000. (C4) the readings at 15 and at 30 conditional sweeps agree within one standard error at
every coupling. (C5) xbar(2.3) = 0.6030(5).

| beta | xbar | J(mu) = (3/2) beta xbar | J(nu), spread lift | J(nu), first-link lift | R = J(nu)/J(mu) | 0.3538/xbar | D = rho_D J(mu) - J(nu) |
|---|---|---|---|---|---|---|---|
| 2.3 | 0.6030(5) | 2.080 | 0.2330(41) | 0.2390(72) | 0.1120(20) | 0.587 | 0.503(4) |
| 2.45 | 0.6418(5) | 2.359 | 0.4001(44) | 0.4060(71) | 0.1696(19) | 0.551 | 0.434(4) |
| 2.6 | 0.6701(4) | 2.614 | 0.5246(37) | 0.5223(82) | 0.2007(14) | 0.528 | 0.400(4) |
| 4.0 | 0.7998(2) | 4.799 | 1.3512(70) | 1.333(14) | 0.2816(15) | 0.442 | 0.347(7) |
| 8.0 | 0.9037(1) | 10.845 | 3.490(20) | 3.463(34) | 0.3218(18) | 0.391 | 0.347(20) |
| 16.0 | 0.95263(5) | 22.863 | 7.724(34) | 7.694(63) | 0.3378(15) | 0.371 | 0.365(34) |

Readings by the criteria of 7.1.
- **(BUB-lit): POSITIVE at all six couplings** (R is below 0.3538/xbar by more than 20 standard errors everywhere).
- **(BUB-d): POSITIVE at all six couplings.** In the window R = 0.11 to 0.20 against rho_D = 0.354: the one-link
  cost of the decimated law is a third to a half of the dressed classical value.
- Trend: R rises to the free ratio 0.354 as beta grows, as it must, and **D levels near 0.35** (0.347(7), 0.347(20),
  0.365(34) at beta = 4, 8, 16). So at the first decimation step the variance term exceeds the non-abelian excess of
  the lift cost by about 0.35 per colour at weak coupling, and by 0.40 to 0.50 in the window. For scale: the
  one-loop running alone would give 0.2575 x q_D/4 = 0.14 per step (Section 5); the rest is specific to the map.
What this does not show. It is a Monte Carlo result on one lattice size, with errors that treat the 40 samples
as independent. It concerns the decimation, whose level form is not selective (3.5). It says nothing about a
second level or an averaging map. Whether the level 0.35 is non-abelian is tested next against compact U(1).

### 7.3 Compact U(1) comparison: design and criteria (written 06:33Z by date -u, before the run)

Same estimator for compact U(1) Wilson on 8^4 with the decimation (script `/tmp/row1383/run/dec_mc_u1.py`, von
Mises heat bath, conditional pair update theta_l1 = g, theta_l2 = V - g). J(mu) = 6 beta xbar. Couplings 1.05, 1.5, 2,
4, 8, 16 from a cold start (all in the Coulomb phase; 1.05 is close to the transition and may be metastable).
Controls: J_link/J(mu) within 1.5 percent of 1; E[Psi^2]/(J(mu)/2) within 3 percent of 1; E[N_l1 N_l2] = 0 within 3
standard errors; the constraint is kept; half-time and full-time readings agree within 3 standard errors.
Check of Theorem U1: D >= 0 at every coupling (a negative D beyond 3 standard errors means an error in the
theorem or in the code).
Reading: SU(2)'s D levels near 0.35. The one-step dressed form is **selective at weak coupling** if D of U(1)
is below 0.12 at beta = 8 and at beta = 16 and falls with beta; it is **not selective** if D of U(1) stays above
0.2 at beta = 8 and 16. In between: undecided. At the couplings 1.05 to 2 the reading is only the size of D
against SU(2)'s 0.40 to 0.50 in the window: if U(1) has a D of the same order there, a positive (BUB-d) in the
window does not separate SU(2) from a massless theory.

### 7.4 Result of the compact U(1) comparison (GUIDE only; written 06:48Z by date -u)

Batch 06:33:47Z to 06:47:23Z by the log's own stamps, 200 samples per coupling, 136 s each, 62-65 percent memory
free; lock released by the exit trap and confirmed free. Log: `/tmp/row1383/run/batch_u1.log`. (My time estimate
was a factor 2 low, so the foreground call passed its limit and the batch finished in the background.)

Controls: all pass. J_link/J(mu) between 0.9999 and 1.0009; E[Psi^2]/(J(mu)/2) between 0.997 and 1.002; E[N_l1 N_l2]
within 1.2 standard errors of 0; constraint defect 9e-16; half-time and full-time readings agree within one
standard error. Check of Theorem U1: D >= 0 at every coupling within errors. PASS.

| beta | xbar | J(mu) = 6 beta xbar | J(nu) | R | D = rho_D J(mu) - J(nu) | beta (1 - xbar) |
|---|---|---|---|---|---|---|
| 1.05 | 0.6912(4) | 4.354 | 1.3002(56) | 0.2986(13) | 0.240(6) | 0.324 |
| 1.5 | 0.8124(2) | 7.312 | 2.530(10) | 0.3460(14) | 0.057(10) | 0.281 |
| 2.0 | 0.8649(1) | 10.379 | 3.638(15) | 0.3506(15) | 0.034(15) | 0.270 |
| 4.0 | 0.93532(5) | 22.448 | 7.913(32) | 0.3525(14) | 0.029(32) | 0.259 |
| 8.0 | 0.96824(3) | 46.475 | 16.394(63) | 0.3528(14) | 0.048(63) | 0.254 |
| 16.0 | 0.98425(1) | 94.488 | 33.43(15) | 0.3538(15) | 0.00(15) | 0.252 |

Readings.
- R tends to 0.3538 = rho_D. This checks the free-field number of 3.2 by an independent method (a Monte Carlo of
  the compact model against a Fourier sum), to three digits.
- beta (1 - xbar) tends to 1/4: the margin of the literal form in U(1) (Theorem U1), as argued in 3.3.
- **By the criterion of 7.3 as written:** the central values at beta = 8 and 16 (0.05 and 0.00) are below 0.12, but
  the errors there (0.06 and 0.15) do not resolve 0.12; strictly the criterion is met at beta = 8 against the
  "not selective" level 0.2 by 2.4 standard errors and is UNDECIDED at beta = 16. I set the couplings badly: the
  absolute error grows with J(mu).
- **Comparison at equal J(mu), not written before the run:** U(1) at beta = 2 (J(mu) = 10.4) has D = 0.034(15) and
  SU(2) at beta = 8 (J(mu) = 10.8) has D = 0.347(20); U(1) at beta = 4 (22.4) has 0.029(32) and SU(2) at beta = 16 (22.9)
  has 0.365(34). The differences are 0.31(3) and 0.34(5). So at weak coupling the one-step dressed margin of
  SU(2) is a non-abelian constant near 0.35, and that of U(1) is consistent with the 1/beta fall of 3.3.
- **Near the transition** U(1) at beta = 1.05 (Coulomb side from a cold start; possibly metastable) has D = 0.240(6)
  and R = 0.299. SU(2) in the window has D = 0.40 to 0.50 and R = 0.11 to 0.20. Both are positive and of the same
  order. So a positive (BUB-d) at an order-one coupling does not separate SU(2) from a massless theory in kind;
  only its size does, and no threshold for the size is known.

### 7.5 What the two runs establish together (GUIDE grade)

1. The sign of (BUB) in the window, for the decimation of ratio 2: positive in the literal and in the dressed
   form, by 20 to 100 standard errors.
2. The literal form is positive for compact U(1) as well (Theorem U1; margin 0.25 to 0.32 measured).
3. The dressed form has a non-abelian margin at weak coupling: SU(2) levels near 0.35, U(1) falls to 0.
4. Nothing on an averaging map, on a second level, or on five dimensions.

## 8. Report (written 06:48Z by date -u)

**Kind of result.** A direction row with one exact identity, two short theorems that decide the row's literal
statement, and a GUIDE run. No step of the gap chain is proved. Nothing here is checked by another model.

**PROVED by hand in this session (unchecked).**
- Proposition LIFT (2.2): for every block map (deterministic or with a kernel) and every lift, the score of the
  blocked law along a block move is the conditional mean, given the block field, of the divergence of the lift;
  cost under the blocked law = cost of the lift under the Wilson law - mean conditional variance; the cost of the
  lift is a direct term. Corollary: every lift gives an upper bound that never loses.
- Three explicit lifts for the block map S_alpha (2.3) and Lemma THIN: for the straight-path decimation of ratio
  m, J(nu) <= J(mu)/m in every model whose action has no term with two collinear links.
- Lab-frame block moves have a site-local cost under every gauge-invariant law (2.4; Lemma WN of row 1013 applied
  to the blocked law). It is not a curl form unless J = 0; the frame-free content is the one-link Fisher information J.
- Theorem U1 (3.3): compact U(1) obeys the row's literal inequality at every coupling and in every dimension,
  with margin beta (1 - xbar) Q_C(t) >= (xbar/(4(d-1))) Q_C(t), by the plaquette tadpole alone; and it obeys the
  dressed form with c = 0.
- Lemma BOG (6.1): a lower bound on the variance term by a vertical field is the gain of a better lift, and all
  its terms are means of explicit local functions under the Wilson law.

**ARGUED (not proved).** The margin of the dressed form in U(1) is of order 1/beta (3.3; supported by 7.4). The
five-dimensional and adjoint-Higgs verdicts on the dressed and level forms (Section 4). All of Section 5 (the
dictionary with Balaban's formulas; (BUB-lev) at weak coupling as a corollary-shaped statement of the account;
one block step holds one momentum shell). The two-number structure of the site form (2.4) is argued by
representation theory in two lines.

**GUIDE (floating point or Monte Carlo; proves nothing).** q_D = 2.1227, rho_D = 0.3538 and the table of 3.2
(after a void first run, script bug found by a hand bound). SU(2), decimation of ratio 2, 8^4: R = J(nu)/J(mu) =
0.112(2), 0.170(2), 0.201(1) at beta = 2.3, 2.45, 2.6; D = rho_D J(mu) - J(nu) = 0.50, 0.43, 0.40 there and 0.35 at
beta = 4, 8, 16. Compact U(1): D = 0.24 at beta = 1.05 and 0.03 to 0.06 from beta = 1.5 on.

**Verdicts on the row's questions.**
1. *The identity.* Written and proved (Proposition LIFT), with the explicit block map S_alpha and explicit lifts.
2. *(BUB) as worded* (reference: the classical curl form; called (BUB-lit) here). For a lab-frame move there is
   no curl form; in the frame-free reading it is J(nu) <= (beta/4) q_C - c. In the window it is TRUE at GUIDE grade
   (Lemma THIN with xbar < 0.7076, and the direct measurement). **It is not selective: Theorem U1 proves it for
   compact U(1) at every coupling, in four and in five dimensions.** Its mechanism is the plaquette tadpole. The
   row's test line "(U1): both terms vanish for the harmonic lift" holds for the Gaussian field only. As a gap
   mechanism this form is dead.
3. *The dressed one-step form (BUB-d).* POSITIVE in the window at GUIDE grade, with a non-abelian margin near
   0.35 at weak coupling that U(1) does not have. But compact U(1) obeys it with c = 0 at every coupling (PROVED)
   and with a margin of the same order near its transition (GUIDE); it is expected to hold in five dimensions as
   in four (ARGUED); it has no consumer; and a proof at a coupling in the window is a (K-one) number (6.2).
4. *The level form (BUB-lev).* For the decimation it is not selective and "J small" has no consumer (Lemma THIN,
   PROVED given one massless model). For an averaging map it passes the three tests, it is the exact first
   statement of M-D, at weak coupling it is a corollary-shaped statement of the account (ARGUED), and in the band
   it is open with no proof route found.
5. *Weak-coupling comparison.* Balaban's lift is the harmonic lift and his identities fix the form of the
   marginal term, not the sign of its change. The universal coefficient is the one-step drop of J only after the
   classical transient of the map has died; Balaban names the first step apart.
6. *Equivalence.* (BUB-lit) and (BUB-d) are not equivalent to the seed and do not imply it. For (BUB-lev) with an
   averaging map **I cannot show non-equivalence to the seed, and I cannot show that it implies the seed**: no
   consumer from a small one-link Fisher information to the seed exists on file or here.

**What a proof would need (6.2).** For any one-step form in the window: an explicit lift of finite range and
rigorous bounds on finitely many local means of the Wilson law at beta from 2.3 to 2.6. That is a formal
computation, not a hand proof; even the literal form needs xbar(2.6) <= 0.7076. For the level form: a class of
blocked laws that is kept by an averaging step, with a consumer; this is M-D, unchanged.

**For the lead.** (i) M-D now has an exact first statement, and its one-step versions are decided as mechanisms:
the literal one is a tadpole fact, the dressed one is a number without a consumer. I would not queue a further
row on a one-step (BUB). (ii) The one open item with content is a consumer: does a small one-link Fisher
information of an AVERAGED blocked law give the seed? It is false for the decimation. Without it (BUB-lev) cannot
be told apart from the seed. (iii) If a cross-check is wanted, the claims to test first are Theorem U1, Lemma
THIN, and the sentence "no curl form for lab-frame block moves".

**Not done.** No averaging map at finite coupling (its lifts are not explicit; only the kernel lift (2.2)). No
second level. No five-dimensional or adjoint-Higgs run. No one-loop computation of the constant 0.35. Balaban's
paper was not re-read (row 1012's quotation). Rows 1026 and 1034 were read by RESULT line only. No cross-branch
search beyond row 1379's (as in row 1380). The Monte Carlo errors treat samples as independent; one lattice size.

**Credits.** Balaban (block averaging, the background minimiser, the effective action (0.22), CMP 109 and 99);
Swendsen (block maps with staples); Sussman and Alpoge with Claude and Codex (the account); Kennedy and Pendleton,
Creutz (heat bath); the lane's rows: 1018 (Lemma FLOW, Lemma ADD, Lemma NAB; Claude Fable), 1244 (Lemma 2.1,
Proposition 2.3; Claude Opus), 1013 (Lemma WN, corner formalism; Claude Fable), 1026 and 1034 ((SYM), LF, BD;
Claude Fable), 1012 (the Balaban quotation; Claude Opus), 1243 ((S-V); Claude Opus), 1025 (the number 0.2575),
1380 (the proposal of this row).

RESULT: Row 1383 (Claude Fable 5.2 high, Mac mini worker 1; author, checked by no one; three numeric runs under the lock, GUIDE only; no subagents). The short step is written as one exact conditional-variance identity, and its one-step inequality (BUB) is decided as a mechanism: not selective. PROVED by hand, unchecked: Proposition LIFT (cost of a block move under the blocked law = cost of any lift under the Wilson law minus the mean conditional variance of the lift's divergence given the block field; every lift is a bound that never loses); explicit lifts for the block map S_alpha and Lemma THIN (straight-path decimation of ratio m has one-link Fisher information J(nu) <= J(mu)/m in every model, so it is rough in U(1) and in five dimensions too); lab-frame block moves have a site-local cost under every gauge-invariant law, so no curl form exists for them; Theorem U1 (compact U(1) obeys the row's literal (BUB) at every coupling and in every dimension, margin beta(1 - xbar) Q, by the plaquette tadpole; the test "both terms vanish" holds for the Gaussian field only); Lemma BOG (a variance lower bound is a better lift, with Wilson means of local functions as its terms). GUIDE (Monte Carlo, 8^4, decimation of ratio 2): the sign of (BUB) in the window is positive in the literal and in the dressed form, J(nu)/J(mu) = 0.112(2), 0.170(2), 0.201(1) at beta = 2.3, 2.45, 2.6 against the free ratio 0.354; the dressed margin levels near 0.35 at weak coupling for SU(2) and falls to 0 for compact U(1), but U(1) has a margin of the same order (0.24) near its transition. Verdicts: the literal form is a tadpole fact and dead as a gap mechanism; the dressed one-step form is a number at each coupling with no consumer, and a proof in the window would be a formal computation of local Wilson means; the level form with an averaging map is the exact first statement of M-D, holds at weak coupling only as the account's own statement (ARGUED) and is open in the band. Equivalence: the one-step forms are not equivalent to the seed and do not imply it; for the level form I cannot show non-equivalence and cannot show that it implies the seed (no consumer from small J to the seed; false for the decimation). OPEN: the seed, (M-neutral), (W); a consumer for small one-link Fisher information of an averaged blocked law; any exact statement for an averaging map at finite coupling; the five-dimensional and adjoint-Higgs runs; the one-loop value of the constant 0.35.
