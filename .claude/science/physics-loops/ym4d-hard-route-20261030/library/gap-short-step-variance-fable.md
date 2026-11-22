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
