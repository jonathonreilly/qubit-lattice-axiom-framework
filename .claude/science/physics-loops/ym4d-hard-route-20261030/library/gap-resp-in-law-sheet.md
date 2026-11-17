# gap-resp-in-law-sheet: (RESP-TR) cell responses in law for one zero-field O(4) sheet (FINISH row 1119)

Written by Claude Fable 5.2, reasoning effort medium, as a laptop subagent. No mass gap is claimed.

Marks used: proved, argued, guide, reading, open.

## 0. Plan (save protocol; at most six steps)

1. Read the named lane sources in full. Record the definitions that the statement needs: K_c, rings, ring law, the scale-invariant normalisation, (H-two), the posted engine, (3.11)-(3.12), (3.61), (3.62).
2. Order (1): independent random rotations of the pins. Test whether the posted profile bound reaches rough profiles.
3. Order (2): a chord through the cell, the Markov property, and (3.62) across the chord.
4. Order (3): the two-sample form through a coupling in annuli, the charged part by (3.61).
5. Run the tests on each written step: U(1) sheet at large coupling, Lemmas W, P1, A1, G1, G2 of row 1096, the first-order model, fixed twists.
6. Verdict by the stop rule, credits, RESULT line.

Each step appends its result below.

## Step 1 result: sources, definitions, the statement in exact form

### 1.1 Read

Lane files read in full: `library/gap-sing-direction-fable.md` sections 1, 3.4 to 3.7 and 6 (3.5 and 6.3 are the brief); `library/prior/gap-resp-in-law-sheet-read-luna.md` (row 1117); `library/gap-face-stability.md` (row 1091); `library/gap-sheet-field.md` (row 1096); `library/gap-pinu-ev.md` (row 1099); `library/prior/gap-fstn-read-luna.md` (row 1095); `library/gap-checkerboard-singlet-astra.md` L49-186 (row 1084's dependency map); the `parts/gap.md` entries of rows 1091, 1096, 1099 with the verdicts of checks 1093, 1094, 1097, 1098, 1100; `library/gap-short-step-max.md` L83-134 (row 1018, the definition of K_c and Rbar). The three check files (`library/gap-sheet-field-check-astra.md`, `library/gap-sheet-field-check-opus.md`, `library/gap-pinu-ev-check-opus.md`): see 1.5.

Paper: OpenAI, *Sharp mass bounds for the two-dimensional O(4) model* (September 23, 2026). I downloaded the PDF once into a new empty scratch directory. Its SHA-256 is e87f407df77777cadabcce10347533a68e7744be365ecd40c9602acc1129baac, the value row 1084 records for commit 4eaee875. The machine has no PDF text tool, so I read the LaTeX source that row 1078 had fetched (file `preliminary.tex`, 1284 lines): Sections 3.1 to 3.3 (source lines 66-253) and 3.8 to 3.11.1 (lines 833-1060) in full. I did not open the O(n) preprint. Nothing was copied into the repository.

### 1.2 Equation numbers (reading)

The source labels of Section 3 map to the PDF numbers by count: Theorem 3.1 holds (3.1)-(3.3); Section 3.1 holds (3.4)-(3.8); Section 3.2 holds (3.9)-(3.12); Section 3.3 holds (3.13)-(3.16); Section 3.8 holds (3.53)-(3.54); Section 3.9 holds (3.55)-(3.58); Section 3.10 holds (3.59)-(3.62). This count agrees with every number that rows 1084, 1091 and 1096 quote. I use these facts of the paper. All of them are stated there for signed couplings, fixed right twists and pins ("the class").

- (3.6): for a one-axis profile f, D_f A = sum_e w_e (s_e . a)(f_y - f_x) and D_f^2 A = sum_e w_e t_e (f_y - f_x)^2. Here t_e + s_e = q_y U_e q_x^{-1}, t_e real, s_e imaginary. s_e is the current of the bond e.
- (3.11): for f zero on the pins, E exp(t D_f A) <= exp(b t^2 E(f)/2), E(f) = sum_e (f_y - f_x)^2. This is "the second variation against the profile energy". (3.10): every fixed moment of a current tested against a C^1 field on a pinned square of side S is at most C_p (1 + b) log(2 + S) times the C^1 norm, for all pins.
- (3.54): a common side R_* with stiffness H_{R_*} <= B^{-D} I, uniformly over the class.
- (3.55), (3.56): for coarse cells of side comparable to s = R_* M_* and a one-axis profile f with bounded cellwise C^2 norm, supported on a fixed number of coarse cells, the coarse ring action F obeys D_f^2 F <= C B^{-D} at every ring configuration, and E (D_f F)^2 = E D_f^2 F <= C B^{-D} by Haar integration by parts on the free ring spins. (3.57), (3.58): the action displacement under such rotations is small in the ring law; "All estimates are uniform under conditioning outside the collar."
- (3.61): for a bounded observable O on A whose average under a common left rotation is zero, |E O| <= C ||O|| |A| e^{-c d_pin / s}. (3.62): |E O(q_x) O'(q_y)| <= C ||O|| ||O'|| e^{-c d(x,y)/s} for a Haar-centered one-site O, on large unpinned tori and free subgraphs. The paper ends Section 3.10 with: "Right twists and signed couplings are still allowed in this step; no association is being used yet."
- Section 3.11 opens: "From now on use the untwisted zero-field ferromagnet ... This restriction is essential. Neither the association argument nor its conclusion is being claimed for arbitrary pinned or frustrated systems."

So "the posted engine" has two outputs. (E-smooth): the ring law is almost invariant under rotations by profiles that are smooth at the scale s; the gain is the number eps = C B^{-D}, the same at every scale above s. (E-charged): observables with zero common-left average have small means at distance from the pins, at rate c/s, for all pins. I write X(b) for s.

### 1.3 The objects of the statement (definitions; my transcription of row 1018 2.3 to two dimensions)

- The sheet: a finite subgraph G of Z^2 or a torus with sides at least L_0, spins q_x in S^3 (unit quaternions), density proportional to exp(sum_e b_e t_e), b_e = b in [2.3, 2.6]. mu is its law. The class of (3.61) allows |b_e| <= b and right twists U_e.
- Cells: squares of side l from a tiling; the rings are the boundary sites of the cells; Omega is the ring configuration. Given Omega the cell interiors are independent (Markov). Bonds between two ring sites carry half weight in each of the two cells, as in the paper. F_c(Omega) = - log Z_c(Omega). The ring law has density proportional to exp(-F_tot), F_tot = sum_c F_c, with respect to the product Haar measure.
- For a ring site y of the cell c that is not a corner, e(y) is the bond from y to its interior neighbour. N_y = b s_{e(y)}, a vector in R^3, is the Neumann datum: for an imaginary unit a, a . N_y is, up to sign, the derivative of the cell action when the pin at y is rotated by e^{ta}. Nbar_y(Omega) = E_{c,Omega}[N_y] and, up to sign, a . Nbar_y = D_{y,a} F_c.
- For y, y' on opposite faces F_-, F_+ of c: K_c(Omega)(y, y') = Cov_{c,Omega}(N_y, N_y'), a 3 x 3 matrix. Minus K_c is the mixed second derivative of F_c in the rotations of the two pins. Under a common left rotation k of the ring, K changes to Ad(k) K Ad(k)^T, so its Hilbert-Schmidt norm is invariant.
- Normalisation. For the free field with action (b/2) sum (d phi)^2 the kernel between opposite faces is b times the off-diagonal block of the Dirichlet-to-Neumann map, of size b l^{-2}. There are l^2 pairs. So sum_{y,y'} |K|^2 is of order b^2 l^{-2}, and the scale-invariant quantity is

      R_c(Omega)^2 = l^2 sum_{y in F_-, y' in F_+} |K_c(Omega)(y, y')|_HS^2,     Rbar(l)^2 = E_mu[R_c(Omega)^2].

  (argued, as in row 1018: the convergence of the lattice kernel is not proved here.)
- **(i)** is: Rbar(l) tends to 0 as l grows, for l >= C X(b). In entries: the mean square of an entry must be o(l^{-4}).
- **(ii)**, (H-two): row 1115 3.4 defines it in words. I fix it as follows. For a cell c and its core c' (the concentric square at depth l/3), m_Omega is the law of the spins of c' under the pinned law (c, Omega). (H-two)(l, eta) says: for two independent ring samples Omega, Omega' from mu, E d(m_Omega, m_Omega') <= eta, with d the total variation distance; the tail clause is P(d(m_Omega, m_Omega') > eta^{1/2}) <= eta^{1/2}, which follows from the mean bound by Markov's inequality. A weaker form tests one local Lipschitz observable at a time.

### 1.4 What is on file before this row (reading)

- Row 1117: no source read states (i) or (ii). OpenAI's Theorem 3.1 gives neutral covariance decay for unpinned systems through association.
- Row 1096, Lemma CO (checked by row 1097: holds given Pei's (I1)-(I3)): the effect of far pins on any observable equals their effect on the law of the gauge-fixed rings, up to an exponentially small term. Row 1096 5.3, last bullet (argued): Theorem 3.1 gives Var(E[F | ring]) <= C poly(l) L_F^2 e^{-c d/Xi} for a local Lipschitz F at depth d. That is the one-observable form of (ii), with association.
- Rows 1096 and 1099: the forms that are uniform in the pins (PIN-U, EV, FST-P) are open. Lemmas P1, A1, G1, G2 and W refute steps of association or monotonicity proofs in small examples. None of them is a statement in the ring law.
- No in-law form of (i) or (ii) is on file (rows 1115 and 1117 say so; my reading of the files above agrees).

### 1.5 The check files, and two facts from them that bind this row (reading)

Read in full: `library/gap-sheet-field-check-opus.md` (row 1097), `library/gap-sheet-field-check-astra.md` (row 1098), `library/gap-pinu-ev-check-opus.md` (row 1100).

- Check 1100: OpenAI's (3.61) is proved in the class of Section 3.1, a square with all boundary spins fixed, and d_pin is the distance to that boundary. A use on another domain needs a written extension. So every use of (3.61) below is inside a square whose boundary is conditioned.
- Check 1098: "Bad-site estimates were averaged over the ring law; they are not uniform mixing estimates at every fixed ring configuration." So (E-smooth) is a statement in the ring law (uniform under conditioning outside a collar), and (E-charged) is the statement that is uniform in the pins.

Status: step 1 done. Step 2 next.

## Step 2 result: order (1), random rotations of the pins. Two written ways; both stop

Notation. A profile on a face is a real function f on its non-corner sites. For an imaginary unit a, D_{f,a} rotates each pin y by e^{t f(y) a}. For f on F_- and g on F_+ and units a, a':

    D_{f,a} D_{g,a'} F_c(Omega) = - sum_{y,y'} f(y) g(y') a . K_c(Omega)(y,y') a'  =:  - K_c[f a, g a'].      (2.0)

(proved: differentiate -log Z_c twice; the bond terms of the two pins are in different factors; no bond joins the two faces away from the corners.)

### 2.1 The identity for independent random rotations (proved)

Let theta_y, theta'_y' be independent fair signs and a, a' independent uniform members of an orthonormal basis of Im H. Then E_theta |K_c[theta a, theta' a']|^2 = (1/9) sum_{y,y'} |K_c(y,y')|_HS^2. So R_c^2 = 9 l^2 times the mean square response to independent random rotations of the two faces. This is the first sentence of order (1).

### 2.2 Way 1: the profile bound at rough profiles (written out; it gives the trivial bound)

**What the posted bound gives.** For vectors U, V: |Cov(U, V)|_HS^2 <= E|U - EU|^2 E|V - EV|^2. With |N_y| <= b:

    sum_{y,y'} |K_c(y,y')|_HS^2 <= (sum_y E_{c,Omega}|N_y - Nbar_y|^2)(sum_y' E_{c,Omega}|N_y' - Nbar_y'|^2) <= b^4 l^2.      (2.1)

So R_c^2 <= b^4 l^4 for all pins. (proved; it uses nothing.) The posted profile bound does not improve the order. (3.11) bounds the variance of a compact score by b E(f). A rotation of the pins by a rough profile theta is equivalent, for far observables, to a compact score of any extension of theta into the cell. Every extension of a profile of independent signs has energy E at least c l, because neighbouring pins differ by 2 on half of the pairs and the energy of an extension is at least a constant times the sum of the squared jumps along the face (discrete trace inequality; argued). So the posted bound gives a variance of order b l per face and a mean square response of order b^2 l^2. The target is o(l^{-2}). The bound misses by l^4. This is the death that row 1115 predicted: "the profile energy of a rough profile grows with the boundary".

**Why no repair of this way exists inside its own tools (Lemma GB; proved for the Gaussian sheet, with one standard random-walk estimate argued).** The tools of way 1 are (3.6), (3.11), (3.12), the Markov property and the Cauchy-Schwarz inequality. All of them hold for the Gaussian sheet: real field phi, action (b/2) sum_e (phi_y - phi_x)^2, pins on the ring. There D_f A = b sum_e (phi_y - phi_x)(f_y - f_x), D_f^2 A = b E(f), and (3.11) holds with equality. For the Gaussian sheet F_c(Omega) = (b/2) Omega . Lambda Omega + const, with Lambda the Dirichlet-to-Neumann matrix of the square, and K_c(y,y') = - b Lambda(y,y') for every pin. For y in F_-, y' in F_+: - Lambda(y,y') = P_{x(y')}(the walk leaves the cell through y) >= 0. The total sum_{y,y'} |Lambda(y,y')| is the sum over y' of the probability that the walk from x(y') leaves through F_-. For y' in the middle half of F_+ this probability is at least c_0 / l (gambler's ruin to depth l/4, then a crossing with probability bounded below; argued, standard). So sum |Lambda| >= c_0 / 2, and by Cauchy-Schwarz over the l^2 pairs

    R_c^2 = b^2 l^2 sum Lambda(y,y')^2 >= b^2 (sum |Lambda(y,y')|)^2 >= b^2 c_0^2 / 4      for every l and every pin.

So any argument that uses only the tools of way 1 would prove (i) for the Gaussian sheet, where (i) is false. This is the U(1) test in its exact Gaussian form. For the compact U(1) sheet at large coupling the same size is recalled (Frohlich and Spencer; not rebuilt, not used).

**Conclusion of way 1.** The entrywise bound needs the non-abelian gain at rough profiles. The posted gain (3.54)-(3.56) is stated for profiles that are smooth at the scale s. Way 2 uses that gain in the ring law.

### 2.3 Way 2: the gain in the ring law, by Haar integration by parts (written out)

**Lemma IBP (proved).** Let eta be an Im H-valued function on a set of free ring sites, and D_eta the derivative along q_y -> e^{t eta_y} q_y. For every smooth function u of the ring, E_mu[D_eta u] = E_mu[u D_eta F_tot]. Hence

    E_mu[(D_eta F_tot)^2] = E_mu[D_eta^2 F_tot],      (2.2)
    E_mu[(D_g G)^2] = E_mu[ G ( D_g G . D_g F_tot - D_g^2 G ) ]      for every smooth G and every such g.      (2.3)

Proof. The flow of eta preserves the product Haar measure, so the integral of D_eta(u e^{-F_tot}) vanishes. Take u = D_eta F_tot for (2.2). Take u = G D_g G for (2.3). QED. (2.2) is the paper's (3.56). It holds in the class.

**Input (E-smooth) at the scale l (argued from (3.14), (3.54) and the proof of (3.55); the bookkeeping is not written here).** Let l be a multiple of s, l >= C s. Let eta = f a + g a', with f, g restrictions to the middle halves of F_-, F_+ of functions phi(. / l) with C^2 norm at most 1. Then at every ring configuration

    D_eta^2 F_tot <= C_1 eps,   D_{f,a}^2 F_tot <= C_1 eps,   D_{g,a'}^2 F_tot <= C_1 eps,      eps = B^{-D}.      (2.4)

Reason. Extend f and g to the plane with disjoint supports and gradients of order 1/l. The ring action at the scale l is minus the logarithm of the integral of the exponential of minus the ring action at the scale s. So its second derivative is a conditional mean of the second derivative at the scale s minus a conditional variance ("conditional variance subtraction", the paper's words). At the scale s each coarse cell costs C (gradient in coarse units)^2 [B^{-D} + P(B)/M_*], by the proof of (3.55), which is bilinear in the test. The gradient is s/l and there are at most C (l/s)^2 coarse cells. The total is C_1 B^{-D}, the same at every scale. The gain does not improve with l in the posted text: the iteration of Section 3.8 runs under the premise (3.9), log(2 + S) <= 16 B.

**Lemma LOW (the low block of (i) in the ring law; proved given (2.4)).** For f, g, a, a' as above:

    E_mu | K_c[f a, g a'] | <= 3 C_1 eps.      (2.5)

Proof. D_f D_g = (D_eta^2 - D_f^2 - D_g^2)/2, because the two flows act on different sites. By (2.0) and since only the cell c holds both faces, K_c[f a, g a'] = - D_f D_g F_tot. For each of the three profiles h: D_h^2 F_tot <= C_1 eps pointwise by (2.4), and E_mu[D_h^2 F_tot] >= 0 by (2.2). So E_mu|D_h^2 F_tot| = 2 E_mu[(D_h^2 F_tot)_+] - E_mu[D_h^2 F_tot] <= 2 C_1 eps. Add the three. QED

Reading of Lemma LOW. A profile of amplitude 1 and wavelength of order l has l^2 norm of order l^{1/2}. So K_c[f a, g a'] is l times a matrix element of K_c between normalised low modes, and its square is one term of R_c^2. Lemma LOW says: every fixed low-low term of R_c is at most 3 C_1 eps in mean. For the Gaussian sheet the same term is of order b. So here a collective gain does drive a response, in law: the response of a whole face to a smooth rotation of the opposite face. The bound does not decay in l.

**Lemma SR (one smooth side, one single pin; proved given (2.4)).** For f, a as above, a non-corner site y' of F_+ and a unit a', put kappa = sum_y f(y) a . K_c(y,y') a' and sigma_f^2 = E_mu Var_{c,Omega}(sum_y f(y) a . N_y). Then

    (E_mu[kappa^2])^{1/2} <= 4 b (C_1 eps)^{1/2} + ((b + 4 b^2) sigma_f)^{1/2} (C_1 eps)^{1/4}.      (2.6)

Proof. Put G = D_{f,a} F_tot and let g be the unit rotation of the pin y' about a'. Then D_g G = - kappa. By (2.2) and (2.4), E_mu[G^2] <= C_1 eps. |D_g F_tot| <= 4 b (four bonds at y'). D_g^2 G is a third derivative of F_c: with X = D_{f,a} A_c and Y = D_g A_c it equals kappa_3(X, Y, Y) - Cov(X, D_g Y) under (c, Omega), and |Y - E Y| <= 2 b, |D_g Y| <= b. So |D_g^2 G| <= (b + 4 b^2) E_{c,Omega}|X - E X|. Put x = (E_mu[kappa^2])^{1/2}. (2.3) and Cauchy-Schwarz give x^2 <= (C_1 eps)^{1/2} (4 b x + (b + 4 b^2) sigma_f). Solve the quadratic inequality. QED

Reading of Lemma SR. One boundary current responds little, in law, to a smooth collective rotation of the far face. It is a true entry-against-collective statement. It has no consequence for (i): the scale-invariant size of kappa is b / l, and l >= s > eps^{-1/4} (s contains the factor M_* = B^{D + C_0}). So the right side of (2.6) is never below the Gaussian size.

**Where way 2 stops (the exact failing line).** Write a face profile as a sum of bumps of width lambda between s and l. (2.2) and (2.4) hold for each bump with the same eps. So way 2 gives, for bumps f_lambda, g_lambda' at distance l: E_mu|K_c[f_lambda a, g_lambda' a']| <= C eps, for every lambda, lambda'. The scale-invariant size of this term is b lambda lambda' / l^2. So (i) needs the bound eps to be replaced by o(lambda lambda' / l^2): a decay in the distance, measured in units of the bump. (2.2) and (2.4) contain no distance. A second application of Lemma IBP produces third derivatives, which are bounded and not small (the proof of Lemma SR). For widths below s (down to one pin) (2.4) is not stated at all, and for a single pin (2.2) reads E_mu[(D_y F_tot)^2] = E_mu[D_y^2 F_tot], which is of order b and not small. So way 2 proves the low-low block, scale-free, and nothing for the l^2 - M^2 other blocks.

**What would be needed.** A composition law: the response across a distance l is at most the product of the responses across pieces of the distance, in the ring law. For the Gaussian sheet the kernels compose exactly and nothing is lost (row 1018, Lemma CHAIN). A loss per piece is clause (DEC) of row 1018. Way 3 tests whether the Markov property and (E-charged) give it.

Status: step 2 done. Ways 1 and 2 are written. Step 3 next.

## Step 3 result: order (2), a chord, the Markov property and (3.61)-(3.62). Way 3, written out; it stops

Setting. c is a cell of side l with ring Omega. Gamma is the column of interior sites of c at horizontal position floor(l/2). It runs from the bottom side to the top side. Given Omega and the spins sigma_Gamma, the two halves of c are independent.

### 3.1 What is proved

**Lemma CH (chord identity; proved, Markov only).** For non-corner y in F_-, y' in F_+ put alpha_y = E_{c,Omega}[N_y | sigma_Gamma] and alpha'_y' = E_{c,Omega}[N_y' | sigma_Gamma]. alpha_y is a function of sigma_Gamma and of the pins of the left half; alpha'_y' of sigma_Gamma and of the pins of the right half. Then

    K_c(Omega)(y, y') = Cov_{c,Omega}(alpha_y, alpha'_y') = E_{c,Omega}[alpha_y (x) alpha'_y'] - Nbar_y (x) Nbar_y'.      (3.1)

Proof. E[N_y (x) N_y' | sigma_Gamma, Omega] = alpha_y (x) alpha'_y' by conditional independence. Take the mean and subtract the product of the means. QED. For the Gaussian sheet alpha and alpha' are linear in sigma_Gamma and (3.1) is the exact composition of the two half kernels through the covariance of the chord.

**Lemma CH2 (the two half fluxes are uncorrelated in the law of the model; proved given (3.61)).** On a free subgraph or a torus with sides at least C s, with y, y' as above and c at distance at least l from the boundary of a free subgraph:

    E_mu[alpha_y (x) alpha'_y'] = E_mu[N_y (x) N_y'],      |E_mu[N_y (x) N_y']|_HS <= C b^2 e^{-c (l/2 - 2)/s}.      (3.2)

Proof. The equality is the tower property. For the bound let B be the square of radius r = floor(l/2) - 1 around y. It holds the bond e(y) and not the bond e(y'). Condition on all spins outside the interior of B. Inside B the law is a pinned square of the class (zero couplings are allowed, so a free subgraph is padded). N_y is a function of the two spins of e(y), bounded by b. Under a common left rotation k it changes to Ad(k) N_y, and the Haar average of Ad(k) is zero. So (3.61) gives |E[N_y | outside B]| <= 2 C b e^{-c (r - 1)/s}. N_y' is a function of the outside. Multiply and average. QED. This is (3.62) for the two bond currents. It holds in the class.

**Corollary CH3 (the mean of an entry in law; proved given (3.61)).** E_mu[Nbar_y] = 0 by the rotation invariance of mu, and

    E_mu[K_c(Omega)(y,y')] = - E_mu[Nbar_y (x) Nbar_y'] + O(b^2 e^{-c l/(2s)}).      (3.3)

So the mean of an entry is, up to an exponentially small term, minus the covariance under mu of the two mean fluxes. Both are functions of the whole ring.

**Lemma DEEP (the charged channel is closed for all pins; proved given (3.61)).** Let O be a bounded function of the spins of a set A inside c, with zero common-left average. Let B be a square inside c that contains A at distance at least d from its boundary. Let G be any bounded function of the spins of c outside the interior of B. Then for every pin Omega: |E_{c,Omega}[O G]| <= C ||O|| ||G|| |A| e^{-c d/s}, and the same bound holds for |E_{c,Omega}[O]|. So |Cov_{c,Omega}(O, G)| <= 2 C ||O|| ||G|| |A| e^{-c d/s}.

Proof. Condition on the spins outside the interior of B and apply (3.61) in B. QED

### 3.2 Where way 3 stops (two exact failing lines)

(i) needs the second moment E_mu |K_c(y,y')|^2 = o(l^{-4}). Lemmas CH2 and CH3 give first moments.

**Failing line 1 (in law).** By (3.1), K = E[alpha (x) alpha' | Omega] - Nbar (x) Nbar'. Each of the two terms is of order b at a typical ring: |Nbar_y| is the mean current at a pin whose neighbours on the ring are fixed, and it is of order b^{1/2} (argued; spin-wave size, not proved). (3.2) says that the mean over mu of the first term is small. It is small because the orientation of the ring is averaged, not because the term is small. The square of the first term is

    E_mu | E[alpha_y (x) alpha'_y' | Omega] |^2 = E[ alpha_y(sigma^1) (x) alpha'_y'(sigma^1) . alpha_y(sigma^2) (x) alpha'_y'(sigma^2) ],

with two copies sigma^1, sigma^2 of the interior of c drawn independently given one ring Omega from mu. The function alpha_y(sigma^1) (x) alpha_y(sigma^2) lives near one place and has a non-zero invariant part (its trace). Its common-left average is not zero. So (3.61) and (3.62) do not apply to it. The law of the two copies is also outside the class: its ring weight is Z_c(Omega)^2 Z_ext(Omega) / Z_c(Omega). No written step bounds this two-copy function. In words: K is small at a ring only if the two faces are independent given that ring. The ring fixes the frame, so no rotation is left to average, and the statement is one about neutral functions.

**Failing line 2 (uniform in the pins).** One can try to split alpha_y into a charged and a neutral part under rotations of the chord, and to close the charged part by Lemma DEEP for every pin. This fails at the ends of the chord. A chord that separates the two faces must touch the ring. Its sites near the top and bottom sides are at distance of order 1 from pins, and (3.61) says nothing there. A rotation of the deep part of the chord alone is not covered either: the deep part is adjacent to the rest of the chord, which would then act as a pin at distance 1. So the chord carries two channels that (E-charged) does not close: the neutral functions of the deep part, and all functions of the two boundary layers along the top and bottom sides, where the pins keep the symmetry broken over the whole distance l.

**What way 3 proves about the supplier question.** Lemma DEEP is the exact reach of the charged engine inside a pinned cell: any covariance with one deep charged factor is exponentially small, for all pins. N_y and N_y' are charged, but they are not deep. They sit on the pins. By Lemma CH the correlation between them passes through the chord as the covariance of two functions alpha_y, alpha'_y' that are not charged under any rotation that the engine controls. So the entries of K_c are neutral-channel quantities. The charged engine closes the other channel and gives no bound on this one.

Status: step 3 done. Way 3 is written. Step 4 next.

## Step 4 result: order (3), the two-sample form. Way 4, written out; it stops, and (ii) is not weaker than singlet mixing

Setting as in 1.3: c' is the core of c, m_Omega the law of the core spins under (c, Omega), mbar = E_mu[m_Omega] the law of the core under mu, d the total variation distance (supremum over events).

### 4.1 What (ii) is (proved; elementary)

**Lemma TS.** Put beta_mix = E_mu d(m_Omega, mbar). Then

    beta_mix <= E d(m_Omega, m_Omega') <= 2 beta_mix,

for Omega, Omega' independent with the ring law. beta_mix is the total variation distance between the joint law of (core, ring) under mu and the product of its two marginals.

Proof. d(m_Omega, mbar) = d(m_Omega, E' m_Omega') <= E' d(m_Omega, m_Omega') by convexity of the distance. The upper bound is the triangle inequality. The last sentence is the disintegration of the joint law over the ring. QED

**Lemma TS2.** Let F be a bounded function of the core spins and G a bounded function of the spins outside the interior of c (the ring included). Then |Cov_mu(F, G)| <= 4 ||F|| ||G|| beta_mix.

Proof. By the Markov property E_mu[F | outside] = m_Omega(F). So Cov_mu(F, G) = E_mu[(m_Omega(F) - mbar(F)) G], and |m_Omega(F) - mbar(F)| <= 2 ||F|| d(m_Omega, mbar). QED

So (H-two)(l, eta) for one tiling scale gives |Cov_mu(F, G)| <= 4 eta ||F|| ||G|| for every bounded core observable and every bounded outside observable, neutral ones included, with no factor for the supports. That is singlet mixing between a core and its outside at distance l/3. Two consequences.

- A proof of (ii) in the class of fixed twists and signed couplings is a proof of neutral mixing in that class. The paper declines that claim: "Neither the association argument nor its conclusion is being claimed for arbitrary pinned or frustrated systems." So (ii), with every step in the class, is at least as strong as a statement that the source of the engine leaves open.
- (ii) is not an easier supplier for row 1118. It already contains the conclusion of (CONV) at one scale. Row 1118 could only improve the rate.

For comparison (reading; row 1096 5.3 and check 1098 section 7): with association, Theorem 3.1 gives the one-observable form of (ii) for the untwisted sheet. For a local Lipschitz F at depth d, Var_mu(m_Omega(F)) = Cov_mu(F, m_Omega(F)), and m_Omega(F) has one-site Lipschitz constants at most 2 b ||F||. So Var_mu(m_Omega(F)) <= C poly(l) L_F ||F|| e^{-c d / Xi}. The supplier there is Section 3.11, not the engine.

### 4.2 Way 4: a coupling in annuli with the charged part closed (written out)

**Step A (the charged part; proved given row 1096's Lemma CO at zero field, which check 1097 and check 1098 found to hold given Pei's (I1)-(I3), that is OpenAI's (3.54), Section 3.10.1 and (3.58)).** Tile c by coarse cells of side s. Adjoin Haar orientations g at the free coarse vertices and write the coarse rings as omega = Phi(g) omega-tilde. For two pins Omega^1, Omega^2 of c, a bounded O on a set A at depth d > C s in c:

    m_{Omega^1}(O) - m_{Omega^2}(O) = integral of Psi d(mt^1 - mt^2) + Rem,      |Rem| <= C |A| ||O|| e^{-c d/s},      (4.1)

where mt^j is the law of the gauge-fixed rings omega-tilde under (c, Omega^j) and |Psi| <= ||O||. (4.1) holds for all pairs of pins. The orientations couple by the disagreement exploration of the paper's Section 3.10.2; that is the coupling in annuli, and the charged part is closed by it. For an O with zero common-left average Psi itself is small, and (4.1) is (3.61).

**Step B (what is left).** By (4.1), for independent ring samples,

    E | m_Omega(O) - m_Omega'(O) | <= 2 ||O|| E d_A(mt_Omega, mt_Omega') + C |A| ||O|| e^{-c d/s},      (4.2)

with d_A the total variation distance on the sigma-field that Psi reads. So (ii) follows from the same two-sample statement for the gauge-fixed rings. The gauge-fixed ring is the coarse ring after a random smooth rotation. Its law carries the neutral data of the cell: local shapes with no frame.

**The exact failing line.** To continue the coupling one needs, for the gauge-fixed rings of one annulus, a common component: two conditional laws of the annulus, given two outside data drawn from mu, overlap with probability at least delta > 0, with delta independent of l. I tried three sources for delta.
- (E-smooth), (3.55)-(3.58): it says that the law of omega is almost invariant under smooth rotations. It is the reason why omega-tilde can be defined with good conditional densities for g. It contains no comparison of two outside data. It gives nothing.
- (E-charged), (3.61): by Lemma DEEP it bounds covariances with one deep charged factor. Functions of omega-tilde are neutral. It gives nothing.
- The density bound: the conditional density of an annulus given its outside changes by a factor at most e^{C b l'} with the outside (l' the length of the annulus boundary). This gives delta >= e^{-C b l'}, which is not uniform in l. In the ring law one may discard atypical outsides, but the typical ones still differ by order l' bonds. (This is the final bullet of row 1096 5.3, now in law; the in-law form does not change the exponent.)

So way 4 stops at Step B. By Lemma TS2 it had to stop at a statement of neutral mixing, because its target contains one.

**A remark on the first-order model (guide; belief grade, not used).** At a coexistence point of a rotation-invariant model with a neutral order parameter, Lemma TS2 shows that (H-two) is false. If such a model had both outputs of the engine, then no argument from (E-smooth), (E-charged) and the Markov property alone could prove (ii). I do not know such a model with a proved engine. The posted engine uses the linear bond action (the Ward identity (3.6)-(3.8)); a model with a first-order point has another bond law. So this is a guide to where a proof of (ii) must use the exact action a second time, not a counterexample.

Status: step 4 done. Way 4 is written. Step 5 next.

## Step 5 result: the tests

Each statement of this file with a proved mark is tested. The statements are: (2.0), 2.1, (2.1), Lemma GB, Lemma IBP, Lemma LOW, Lemma SR, Lemma CH, Lemma CH2, Corollary CH3, Lemma DEEP, Lemma TS, Lemma TS2, and (4.1)-(4.2).

**The U(1) sheet at large coupling; the proof must stop there.**
- No statement here proves (i) or (ii), so nothing has to stop. The partial statements stop where they should. Lemma LOW and Lemma SR use (2.4). For the Gaussian sheet D_f^2 F_tot = b times the energy of the harmonic extension of f, which is of order b for a smooth f of amplitude 1 at every scale. So (2.4) is false there, and Lemma LOW's conclusion is false there too (the low-low term is of order b). Lemmas CH2 and DEEP and Corollary CH3 use (3.61), which fails for a sheet with power-law decay.
- (2.0), 2.1, (2.1), Lemma IBP, Lemma CH, Lemma TS and Lemma TS2 hold for every group and every coupling. They prove no decay. Lemma GB shows that R_c is bounded below for the Gaussian sheet, so these blind statements cannot be combined into (i).

**Lemmas W, P1, A1, G1, G2; the in-law forms must not contradict them.**
- P1, A1, G1 and G2 are about a sheet in a field: pinning monotonicity, amplitude association and cosine positivity fail in small examples. W is about a wall monotonicity at zero field. This file uses no monotonicity, no association and no positivity of a correlation. Its only statements that are uniform in the pins are (2.0), (2.1), Lemma CH (identities and a trivial bound) and Lemma DEEP and (4.1) (the posted (3.61) and row 1096's Lemma CO, restated). None of them is a statement about a field or about an increasing event.
- The uniform forms PIN-U, EV and FST-P are not claimed here in any form. Lemma LOW is in the ring law and for smooth profiles only. In the two-site and three-site examples of those lemmas there is no ring law at a scale above s, so no comparison arises.

**The first-order model; small entries need not give mixing.**
- Lemma TS2 gives the test in a sharp form: (ii) implies mixing, so (ii) must fail at coexistence, and it does (two independent rings fall in different phases with positive probability).
- (i) is not claimed. Lemma LOW, Lemma SR and Corollary CH3 are statements about responses. They are compatible with a mixture: in each phase the low-mode response can be small.
- This file does not use (i) to conclude anything about mixing.

**Fixed twists; every step must hold in the class of (3.61).**
- (2.0), 2.1, (2.1), Lemma IBP, Lemma CH, Lemma TS, Lemma TS2: they use the Markov property, the Haar measure and bounded bond terms. They hold for signed couplings and right twists. With right twists the symmetry is the left SU(2); N_y is the left current and K_c is 3 x 3, as defined in 1.3.
- Lemma LOW and Lemma SR use (3.14), (3.54) and the proof of (3.55), all stated in the class.
- Lemma CH2, Corollary CH3, Lemma DEEP use (3.61) on a conditioned square, in the class. (4.1) is row 1096's Lemma CO, stated there for couplings in [-beta, beta].
- The one statement of this file outside the class is the comparison at the end of 4.1 (the one-observable form of (ii) from Theorem 3.1). It is marked reading and nothing rests on it.

**The earlier routes.** Ways 1, 2 and 3 are not among the six routes of row 1096 or the three ports of row 1084: none of those is in the ring law and none treats K_c. Step A of way 4 is row 1096's Lemma CO, and its density bound is the final bullet of row 1096 5.3, taken in the ring law. So way 4 is not counted for the stop rule. It is written because order (3) asked for it and because Lemma TS2 settles what (ii) is.

**Numerics.** No numeric run was made. A cell of side C X(b) at b in [2.3, 2.6] is far outside any run (X(b) contains e^{pi b} and more). No computer-assisted step is used. Every proof above is a finite identity, an integration by parts on a compact group, a conditional expectation, or the Cauchy-Schwarz inequality, so each is Lean-formalizable in principle, given the cited inputs as hypotheses.

Status: step 5 done. Step 6 next.

## Step 6 result: verdict by the stop rule, marks, limits, credits

### 6.1 Verdict

**Stopped. Neither (i) nor (ii) is proved.** No counterexample to (i) or (ii) for the O(4) sheet was found.

**The named step that failed (C-E, collective to entries).** From the two outputs of the posted engine, (E-smooth) and (E-charged), with the Markov property and Haar integration by parts, derive in the ring law a bound o(l^{-4}) on the mean square of one entry of K_c between opposite faces. It failed in three written ways.

1. **Way 1 (2.2), rough profiles and the profile bound (3.11)-(3.12).** Result: R_c^2 <= b^4 l^4, the trivial bound. Failing line: the profile energy of a rough profile is of order l, so the posted bound is of the trivial order. It cannot be repaired inside its tools: the Gaussian sheet satisfies all of them and has R_c >= c b (Lemma GB).
2. **Way 2 (2.3), the gain in the ring law.** Result: Lemma LOW (each low-low term of R_c is at most 3 C_1 eps in mean) and Lemma SR. Failing line: (2.2) and (2.4) hold with the same eps for bumps of every width between s and l and contain no distance; (i) needs o(lambda lambda' / l^2) for bumps of widths lambda, lambda'; a second integration by parts gives third derivatives that are not small; below the width s nothing is posted.
3. **Way 3 (step 3), a chord, Markov and (3.61)-(3.62).** Result: Lemma CH, Lemma CH2, Corollary CH3 (first moments in law), Lemma DEEP (the charged channel is closed for all pins). Failing lines: the second moment is a two-copy function with a non-zero invariant part, outside the reach of (3.61); a chord that separates the faces touches the ring, and at its ends and along the top and bottom layers (3.61) is silent.

**For (ii)**: by Lemma TS2 it contains singlet mixing between a core and its outside. Way 4 closes the charged part (4.1) and stops at the two-sample statement for the gauge-fixed rings (4.2), with no common component uniform in l.

**Answer to the supplier question of the row.** In the one model where the engine and singlet mixing are both posted, the collective gain drives, in law, the response of a whole face to a smooth rotation of the opposite face (Lemma LOW), at a size that does not decay with l. It drives the charged channel for all pins (Lemma DEEP). By the three ways above it does not drive the entries, and it does not drive the two-sample distance. Both are carried by the neutral channel: the correlation of the two faces given the ring, where the ring has fixed the frame. This is a statement about three written ways, not a theorem that no way exists.

**What changes (the "stopped" branch that row 1115 6.3 wrote beforehand).** (SING) stays blocked-local. The lane can record: an engine of Ward type gives the low-mode block of Rbar in law and the charged channel, and no entrywise response, even where singlet mixing is a theorem by another method. For (T-pin): the clause (DEC) of row 1018 asks for a loss when kernels compose across a ring. In this model that loss is the decay of the neutral channel across a chord, in the ring law (Lemma CH and failing line 1). The engine does not supply it. For row 1118: (ii) is not a weaker hypothesis than its conclusion at one scale (Lemma TS2); if row 1118 proves an implication from (H-two), its supplier is a mixing statement.

**The next decision (one item, named).** The smallest open statement that this row isolates is (N-CH): for the pinned cell of side l with a middle chord, in the ring law, the covariance under (c, Omega) of the two half fluxes alpha_y, alpha'_y' of Lemma CH has mean square o(l^{-4}). With association it should follow from the method of the paper's Section 3.11 applied in a cell with typical pins; I did not derive it. Without association nothing on file reaches it. A row on it would have to name a property of the exact bond action that the engine has not used yet.

### 6.2 Marks

| Mark | Statement and scope |
|---|---|
| proved | (2.0); the identity 2.1 (R_c^2 is 9 l^2 times the mean square response to independent random rotations); the trivial bound (2.1). All pins, all groups. |
| proved, with one standard random-walk estimate argued | Lemma GB: the Gaussian sheet satisfies (3.6), (3.11) with equality and has R_c^2 >= b^2 c_0^2 / 4 at every l and pin. |
| proved | Lemma IBP, (2.2), (2.3): Haar integration by parts in the ring law. In the class. |
| argued | (2.4): the pointwise upper bound C_1 B^{-D} on the second derivative of the ring action at the scale l for smooth one-axis and disjoint two-axis profiles, from OpenAI's (3.14), (3.54) and the proof of (3.55). Bookkeeping not written. |
| proved given (2.4) | Lemma LOW: E_mu of a low-low response is at most 3 C_1 eps. Lemma SR: (2.6). Both in the class. Neither decays in l. |
| proved | Lemma CH: K_c(y,y') is the covariance of the two half fluxes given the chord. |
| proved given OpenAI's (3.61) on a conditioned square | Lemma CH2 and Corollary CH3: first moments in the law of the model. Lemma DEEP: a covariance with one deep charged factor is exponentially small for all pins. |
| proved | Lemma TS, Lemma TS2: (H-two) in total variation is, within a factor 2, the mixing coefficient of core and ring, and it bounds every covariance of a core observable with an outside observable. |
| proved given row 1096's Lemma CO (checks 1097, 1098: holds given Pei's (I1)-(I3)) | (4.1), (4.2): the charged part of the two-sample distance is closed; the gauge-fixed rings are left. |
| argued | The lower bound on the energy of extensions of a rough profile; the size b^{1/2} of a mean flux; the scale-invariant sizes quoted for the Gaussian sheet; the remark that (N-CH) should follow with association. |
| reading | The equation numbers of 1.2 (by count of the source labels); the one-observable form of (ii) from Theorem 3.1 (row 1096 5.3, check 1098); the U(1) sheet at large coupling (Frohlich and Spencer, recalled, not rebuilt). |
| guide | The remark on the first-order model in 4.2 (belief grade; not used). |
| open | (i). (ii). (N-CH). A stiffness bound that improves with l beyond B^{-D} (the posted iteration runs under (3.9)). |

### 6.3 Limits

- Nobody has checked this file. Nothing was formalized in Lean. Every proof is a hand argument.
- OpenAI's paper is unrefereed. (3.14), (3.54), (3.55), (3.56) and (3.61) are inputs that I did not check. I read Sections 3.1 to 3.3 and 3.8 to 3.11.1 of the source; Sections 3.4 to 3.7 (the stiffness gain itself) were not read. Pei's paper and Ding, Huang and Yang's paper were not opened in this row; they enter through rows 1096 to 1100.
- (2.4) is argued. Lemma LOW and Lemma SR rest on it. If (2.4) fails, the low-low statement falls back to cells of side comparable to s, where (3.55) is stated.
- Lemma LOW covers profiles supported in the middle halves of the faces. Corners are not treated.
- The stop is a stop of three ways. It is not a no-go theorem. Lemma GB is the only exclusion with a proof, and it excludes only arguments that are blind to the group.
- (H-two) was fixed in 1.3 from the words of row 1115 3.4. If row 1118 fixes another distance (for example a transport distance on a smaller core), Lemma TS2 holds for the functions that this distance controls.
- Files changed: this file only. One download (the paper's PDF, into a new empty scratch directory; hash checked against row 1084's record). The LaTeX source read is row 1078's earlier scratch copy. No commit, no push, no post. No numeric job.

### 6.4 Credits

OpenAI's authors for the two-dimensional O(4) paper: the Ward identity (3.6)-(3.8), the profile bound (3.11), the cell conditioning (3.13)-(3.16), the stiffness iteration (3.54), the ring-law estimates (3.55)-(3.58), the charged decay (3.61)-(3.62), and Theorem 3.1 with its association argument. N. David Mermin; Driessler, Landau and Perez; Aizenman and Simon for the Ward-identity tradition that the paper cites. Jacob van den Berg and Christian Maes for disagreement percolation. Yan Ru Pei for the coarse-orientation transfer behind row 1096's Lemma CO. Jian Ding, Fenglin Huang and Peng Yang for the independent decay mechanism mapped in rows 1084 and 1099 (not used here). Jurg Frohlich and Thomas Spencer for the power-law phase of the plane rotator (recalled). Roland Dobrushin and Senya Shlosman for the mixing conditions behind (H-sup) and the two-sample form. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account that the lane serves, and Tadeusz Balaban for the renormalization group construction behind it; neither is an input of this row. In the lane: row 1018 (K_c, Rbar, Lemma CHAIN, (DEC)); row 1084 (gpt-6-astra max) for the dependency map of the paper; rows 1091, 1096, 1099 (Claude Fable 5.2 medium) for FST-BD, Lemma CO, Lemmas P1, A1 and W, and row 1091's G1 and G2; checks 1094, 1098 (gpt-6-astra xhigh) and 1097, 1100 (Claude Opus 5.5 max); row 1115 (Claude Fable 5.2) for the statement (RESP-TR) and its tests; row 1117 (gpt-6-luna high) for the reading.

RESULT: STOPPED, neither (i) nor (ii) is proved for the zero-field O(4) sheet at b in [2.3, 2.6], and no counterexample was found; the named step, from the collective and charged gains of the posted engine to an entry of K_c of mean square o(l^-4) in the ring law, failed in three written ways (rough profiles against the profile bound (3.11), which gives only the trivial bound and cannot be repaired by group-blind tools since the Gaussian sheet has Rbar bounded below, proved; Haar integration by parts in the ring law, which gives the low-mode block only and no decay in the distance; a chord with the Markov property and (3.61)-(3.62), which gives first moments and closes the charged channel for all pins but leaves the neutral channel); proved on the way, every step in the class of fixed twists: Lemma LOW (given the argued scale-l form (2.4) of OpenAI (3.55), the mean response of a face to a smooth rotation of the opposite face is at most 3 C_1 B^-D, with no decay in l), Lemma SR, Lemma CH (an entry is the covariance of the two half fluxes given a chord), Lemmas CH2, CH3 and DEEP given (3.61), and Lemmas TS and TS2 (the two-sample form (H-two) in total variation equals the core-ring mixing coefficient up to a factor 2 and bounds every core-outside covariance, so (ii) contains singlet mixing and is not a weaker supplier); way 4 for (ii) closes the charged part by row 1096's Lemma CO and stops at the gauge-fixed rings; answer to the supplier question: by these ways a collective rotation-type gain drives the low-mode block and the charged channel but not the per-site responses; open: (i), (ii), the neutral chord statement (N-CH), a stiffness bound improving with l; unchecked, not formalized, no numeric run, no mass gap claimed; written by Claude Fable 5.2 medium.
