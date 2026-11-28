lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T12:00Z

# gap-mini-solve-e-fable (queue row 1194)

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, one session, pinned at commit 36be8070a. Not an audit. Not checked by another model. Start 2026-11-20T00:00Z (`date -u`).

Problem of the row: prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

Labels used below: PROVED (every step written here, by hand), ARGUED (argument written, a step is not fully written or rests on a named input), GUIDE (numeric or heuristic, never a proof step), OPEN.

Status of this file: in progress. Sections are appended step by step.

## Step 0. Plan (written before any reading of earlier results)

1. Read the RESULT lines of the sibling rows (gap-mini-solve-a to -d) and of the gap lane, `parts/gap.md` (method list, route registry, test table) and the route screening table in `library/gap-mini-solve-b-fable.md` Step 2.1.
2. Name the exact open statement the lane has reduced the gap to, and the attacks already on file for it.
3. Choose one attack that is not on file, or one named unattempted item, and carry it to a proof, a counterexample, or one precise lemma with the reason each way failed.
4. Rule 0a: before a statement is called new, grep `library/open-core.md` and the FINISH rows for it.

## Step 1. What the record holds (read in this session; statements about the record, not evidence)

Read in full: `GOAL.md`; `FINISH.md` L1-84 and L299-360; the row (L1275); the RESULT lines of rows 1178-1190 and 1193; the three sibling files `gap-mini-solve-a-fable.md`, `-b-`, `-c-` and the start of `-d-`; `parts/gap.md` L1-104 and L213-322; `library/gap-council-synthesis.md`.

1. The lane reduces the Jaffe-Witten gap clause to two open inputs (Theorem BP of row 1179; check row 1183: main chain HOLDS AFTER CORRECTION): the continuum datum of the T0 chain, and one lattice estimate (N-phys) of row 1161. (N-phys) is a neutral gap with a level count on one periodic cube of fixed physical side, uniformly in the cutoff. Rows 1180 and 1184: it is a uniform neutral lattice gap at arbitrarily weak coupling with an asymptotic-scaling bound.
2. The wall in the lane's words (`parts/gap.md` L321-322): one selective inequality at every scale between first passage and the seed size. Selective means false for a massless factor.
3. Siblings of this row. Row 1188 (a): the pinned-slice Ward route, Lemma PC. Row 1189 (b): the doubly flat corner, Theorem A8, stop at (Sigma-unif) and (SING). Row 1190 (c): seventeen candidates on file; cube identity; chi-square form of (N-phys). Row 1193 (d): started, no attack written at this pin. Each sibling found the lane's map again and advised against one more fresh choice of route.
4. Consequence for this row: I do not screen routes again. I choose one mechanism question and work it to a proof or to a first failing step.

## Step 2. Choice of attack (written 2026-11-20T00:51Z, `date -u`)

### 2.1 What was screened in this session (GUIDE; statements about the record)

I derived routes again from the target and grepped each before any work. Each has a match. I list only the ones that are not in the tables of rows 1189 and 1190.

| Route, from first principles | Match on file |
|---|---|
| The Witten Laplacian on exact one-forms: the glue half as the ground energy of one adjoint ("gluelump") particle | `gap-brainstorm-max.md` L299 (idea 20), `gap-next3-max.md` L336 (C6), rows 957, 968. My own count: the Ricci term is cancelled to every order of perturbation theory, because the true gap is of order exp(-c beta). So an averaged-curvature bound of order one cannot hold in the band (ARGUED) |
| The thin twisted torus with a dilute gas of fractional instantons (Tanizaki and Unsal) | Route T, rows 678-684, 842, 856, 862 (Theorem S1, Lemma PE; open above the vortex spacing M_1) |
| Centre twist as a double rigid colour twist with anticommuting transition elements; the zero-action twist eater | rows 731, 1013 (Lemma TWIST, C1, C2), row 1181 (Proposition J) |
| Singlet response to a far bond cut as an average over Haar twists on the cut | reduces to a singlet covariance again; rows 1115-1123 hold the conversion question (CONV), (RESP-TR) |
| Convexity in the coupling: the volume-normalized energy variance is integrable in beta, uniformly in the volume | elementary; no pointwise consequence (a free photon has a finite specific heat and no gap) |
| The SO(3) x Z_2 form (Mack and Petkova; Tomboulis): given the SO(3) field, the centre field is a Z_2 gauge theory | 62 files name Petkova, 88 Tomboulis; flux half only (council 2c) |
| Feynman-Hellmann and a continuity method in beta from strong coupling | (NOCRIT-HF), rows 859, 878: needs a lower bound on the lattice beta function |

So the screening of rows 1189 and 1190 stands. I add no route.

### 2.2 Where every route stops, in one sentence (ARGUED; the lane's reading, row 1115)

The posted two-dimensional proofs reach singlet observables only through association of the untwisted O(4) ferromagnet (OpenAI Section 3.11, as read in row 1009 and `library/prior/gap-o4-pinned-cell-read-opus.md` L128-141). In four dimensions every observable is a singlet, link coordinates are uncorrelated by Elitzur's theorem, and associated uncorrelated variables are independent. So no association of link coordinates exists, and the glue half needs another conversion from charged decay to singlet decay. The lane names this step (SING), with the cleanest open member (K4-N) (`gap-sing-direction-fable.md` L144-150): a neutral bound for the constrained law (K4), "the first neutral bound for interacting non-abelian sheets with no association".

### 2.3 The attack chosen

**Item.** The conversion step in its smallest exact instance: the family K_N of N sheets with product one (N = 4 is the lane's (K4); it is the doubly flat corner of row 1053 with a fibre that is one cycle; rows 1110 and 1189).

**Why.** (a) It is the named first lemma of the neutral half in the lane's own registry (BR-2 reopen condition). (b) It has a rigid group that is transitive on the one-site space, so the charged half is supplied (GIVEN the posted estimate (3.61); row 1110 (O5), row 1115 3.2). (c) I found an exact structure of K_N that is not on file under the words I grepped ("convolution" in the corner and face files, "Plancherel", "charge gas", "Coulomb gas", "random walk on"; `library/open-core.md` has no line on K4, on a corner or on a cycle): K_N is a convolution power on the group of sheets, and it has a positive dual gas of non-abelian charges. Step 3 proves it. Steps 4 and 5 use it on (K4-N).

**What it can give.** Not the Jaffe-Witten gap. By row 1115 2.2 the family (SING) is not on the path from the target; BR-2 fully proved stops at C_beta. A proof of (K_N-N) would be a mechanism for singlet decay with no association. A failure names the first step that a mechanism has to supply.

**Stop rule.** A proof, a counterexample, or one lemma that failed in three written ways.

## Step 3. Exact structure of the cycle models K_N (all statements PROVED here by hand unless marked; unchecked)

Credit. The model (K4) and its place in (SING): row 1110 (gpt-6-astra, `gap-face-order-one-astra.md` (K1)-(K9)) and row 1115. The corner model: row 1053 6.8; rows 1189 A1-A5. The flux (character) form of a positive transfer operator is standard (Osterwalder and Seiler; Luscher); for the centre it is 't Hooft's. The lemmas below are elementary. I did not find them on file for K_N (grep words in 2.3).

### 3.1 Setting

- B is a finite connected graph, for example a rectangle of Z^2. Its largest degree is Delta. Bonds f = <y, y'>.
- K = SU(2)^B, a compact group under pointwise multiplication, with Haar probability measure dk.
- <a, b> = (1/2) tr(a b^(-1)) for a, b in SU(2). This is the inner product of R^4 on unit quaternions.
- E(m) = sum over bonds of <m(y), m(y')>. The sheet density is pi(m) = exp(beta E(m))/Z_1, beta >= 0. It is the O(4) sheet at coupling beta.
- Convolution: (f * g)(k) = int f(l) g(l^(-1) k) dl.
- K_N, N >= 2: planes k_p in K, p in Z_N, with density z_N^(-1) prod_p pi(k_p^(-1) k_(p+1)). Sheets m_p = k_p^(-1) k_(p+1). Their ordered product is 1.
- For N = 4, with A = m_0, B = m_1, C = m_2^(-1): the sheet law is (K4) of row 1110, exp{beta [E(A) + E(B) + E(C) + E(A B C^(-1))]} dA dB dC. (Uses P1 below.) For a fibre that is a chain with free ends the sheets are independent (row 1189 A4). So the cycle condition is the only coupling.

### 3.2 Lemma C0 (three properties of pi)

(P1) pi(m^(-1)) = pi(m). (P2) pi(a m b) = pi(m) for constants a, b in SU(2). (P3) For every finite-dimensional unitary representation rho of K, the matrix rho(pi) = int pi(m) rho(m) dm is Hermitian, 0 <= rho(pi) <= 1.

Proof. (P1): <a^(-1), b^(-1)> = (1/2) tr(a^(-1) b) = (1/2) tr(b^(-1) a) = <a, b>, because tr g = tr g^(-1) in SU(2). (P2): the constants cancel in a b^(-1) under the trace. (P3): Hermitian by (P1) and the invariance of Haar measure under inversion. The norm is at most 1 because pi is a probability density. Positivity: let D be the defining representation, w = (e_1 (x) e_1 + e_2 (x) e_2)/sqrt 2, and sigma_f(m) = D(m(y)) (x) conj D(m(y')). Then <w, sigma_f(m) w> = (1/2) sum_(a,b) D(m(y))_(ab) conj D(m(y'))_(ab) = <m(y), m(y')>. Expand the exponential: Z_1 pi(m) = sum_n (beta^n/n!) sum over (f_1, ..., f_n) of <W, tau(m) W>, with tau = sigma_(f_1) (x) ... (x) sigma_(f_n) and W = w^((x) n). For v in the space of rho, int <W (x) v, (tau (x) rho)(m) (W (x) v)> dm = |P (W (x) v)|^2 >= 0, where P is the orthogonal projection on the invariant vectors of tau (x) rho. Sum with the non-negative coefficients. QED.

### 3.3 Lemma C1 (convolution form)

Let (C f)(k) = int pi(k^(-1) l) f(l) dl on L^2(K), and for bounded F let C_F = int pi(u) F(u) R_u du, with (R_u f)(k) = f(k u). Then:
(a) C = C_1. C is self-adjoint and positive, C 1 = 1, and its norm is 1. C commutes with all left translations.
(b) z_N = Tr(C^N) = pi^(*N)(1).
(c) For bounded F_0, ..., F_(N-1) on K: E_(K_N)[prod_p F_p(m_p)] = Tr(C_(F_0) C_(F_1) ... C_(F_(N-1)))/Tr(C^N).

Proof. (a) Put l = k u: (C f)(k) = int pi(u) f(k u) du. Self-adjoint by (P1). Positive by (P3) and the Peter-Weyl theorem (L^2(K) is the closure of the sum of the finite-dimensional invariant subspaces of R). (b), (c): R_u R_v = R_(uv), so the product is int H(g) R_g dg with H(g) = int over u_0 ... u_(N-1) = g of prod pi(u_p) F_p(u_p). Its kernel is H(k^(-1) l), continuous. For N >= 2 it is a product of Hilbert-Schmidt operators with continuous kernels, so its trace is the integral of the diagonal, H(1). With the change of variables l_p = k_0^(-1) k_p, the integral of prod_p pi(k_p^(-1) k_(p+1)) F_p(k_p^(-1) k_(p+1)) over all planes is H(1). QED.

### 3.4 Lemma C2 (flux form, and a positive dual gas)

The irreducible representations of K are rho_j = (x)_y D^(j_y) on V_j, for j: B -> {0, 1/2, 1, ...}, with dimension d_j = prod_y (2 j_y + 1). Put Pi_F(j) = int pi(m) F(m) rho_j(m) dm in End(V_j), and Pi(j) = Pi_1(j). Then:
(a) Tr(C_(F_0) ... C_(F_(N-1))) = sum_j d_j tr[Pi_(F_0)(j) ... Pi_(F_(N-1))(j)], absolutely convergent for N >= 2.
(b) Pi(j) is Hermitian, 0 <= Pi(j) <= 1, Pi(0) = 1. Pi(j) = P_j Pi(j) P_j, with P_j the projection on the vectors of V_j that are invariant under the diagonal SU(2). So Pi(j) = 0 unless such vectors exist.
(c) z_N = sum_j d_j tr[Pi(j)^N]. Every term is non-negative. The term j = 0 is 1. So z_N >= 1, z_N is non-increasing and log-convex in N (it is a sum of terms lambda^N with 0 <= lambda <= 1 and non-negative weights; for example z_3^2 <= z_2 z_4), and

  P_N(j) = d_j tr[Pi(j)^N]/z_N

is a probability law on flux configurations j on B.

Proof. (a) The right regular representation is the orthogonal sum of d_j copies of rho_j over all j. A trace-class operator that commutes with left translations is block diagonal there, and its trace is the sum of the traces of its blocks. On a copy of rho_j the operator int H(g) R_g dg acts as int H(g) rho_j(g) dg = prod_p Pi_(F_p)(j), in order. (b) is (P3), and (P2) integrated over the constants a and b. (c) is (a) with F_p = 1 and (b). QED.

Reading. In the gauge-theory picture K_N is the three-dimensional model on (cycle Z_N) x B with flat base plaquettes. j_y is the electric flux that threads the cycle at the base site y. Because the transfer operator along the cycle commutes with the whole group K, and not only with the centre, the full non-abelian flux is conserved. The matrix entries of Pi(j) are the multi-point charged correlations of one O(4) sheet, contracted with invariant tensors: for two charges 1/2 at y_0 and y_1, Pi(j) is the number c(y_0, y_1) = E_pi <m(y_0), m(y_1)>.

### 3.5 Lemma C3 (a bound uniform in the base)

For every j not identically 0: norm Pi(j) <= 1 - exp(-2 beta Delta). So the transfer operator C has a spectral gap of at least exp(-2 beta Delta) above its simple top eigenvalue 1, for every B.

Proof. Choose y_0 with j_(y_0) != 0. Given the other spins, m(y_0) has density proportional to exp(beta <m(y_0), S>) on S^3, with S the sum of the neighbouring spins, |S| <= Delta. This density is at least exp(-2 beta Delta) with respect to Haar measure. So the conditional law is exp(-2 beta Delta) times Haar measure plus a positive measure of mass 1 - exp(-2 beta Delta). The Haar part integrates D^(j_(y_0)) to zero. So the conditional mean of D^(j_(y_0))(m(y_0)) has norm at most 1 - exp(-2 beta Delta), for every value of the other spins. QED.

What C3 does not give. At a fixed N the trace sums over a number of sectors that grows exponentially with |B|. So C3 alone gives no bound on a K_N correlation that is uniform in B. I draw no such consequence.

### 3.6 Lemma C4 (marginals; the escort form of (K4))

(a) Each plane k_p is Haar distributed. (b) The sheet m_0 has density pi(m) pi^(*(N-1))(m^(-1))/z_N. (c) For N = 2, m_0 is the O(4) sheet at coupling 2 beta. (d) For N = 4, R = m_0 m_1 has density p_2(R)^2/z_4, with p_2 = pi * pi the density of the product field of two independent sheets. Given R, the pairs (m_0, m_1) and (m_2, m_3) are independent. (e) With rho_f = R(y) R(y')^(-1), of rotation angle theta_f in [0, 2 pi]:

  p_2(R) = Z_1^(-2) int da exp( beta sum_f < (1 + rho_f) a(y'), a(y) > ),   1 + rho_f = 2 cos(theta_f/4) rho_f^(1/2).

So p_2(R) is, up to Z_1^(-2), the partition function of one O(4) sheet with bond strengths 2 beta cos(theta_f/4) and left twists rho_f^(1/2), the geodesic midpoints of the increments of R.

Proof. (a)-(d): integrate, as in C1, and use (P1) to see p_2(R^(-1)) = p_2(R). (e): pi(a) pi(a^(-1) R) has exponent beta sum_f [<a(y), a(y')> + <a(y)^(-1) R(y), a(y')^(-1) R(y')>], and <a^(-1) R, a'^(-1) R'> = (1/2) tr(a^(-1) R R'^(-1) a') = <rho_f a', a>. For g = cos(theta/2) + sin(theta/2) n, n a unit imaginary quaternion: 1 + g = 2 cos^2(theta/4) + 2 sin(theta/4) cos(theta/4) n = 2 cos(theta/4) g^(1/2). QED.

Remark (the size of the frustration; ARGUED, second order of the Baker-Campbell-Hausdorff series). The increments rho_f of a site field multiply to 1 around a base plaquette. Their midpoints do not. With rho_i = exp(X_i) on the four bonds, prod exp(X_i/2) = exp(-(1/8) sum_(i<j) [X_i, X_j] + third order). So the twist field of (e) is frustrated exactly by the commutators of the increments. For U(1) the product is +1 or -1, and -1 only at a vortex of R. This is where (K4) reads the group at order one: the abelian model has a frustration-free conditional sheet away from vortices, the SU(2) model has a commutator frustration on every plaquette.

### 3.7 Comparison of the dual gases (GUIDE for U(1); GIVEN the posted estimate for SU(2))

- U(1), spin-wave (Gaussian) sheet: Pi(n) = exp(-(1/(2 beta)) <n, G n>) on neutral integer charge configurations n, with G the Green function of B. So P_N is the two-dimensional Coulomb gas at inverse temperature N/beta. Its charges interact by a logarithm. At large beta/N it is in its dipole phase (Kosterlitz and Thouless; Frohlich and Spencer, RECALLED). This matches the lane's record that the U(1) form of (K4) has no neutral gap (check 1114, guide).
- SU(2), GIVEN OpenAI's charged two-point bound (3.62) as read in row 1009: for two charges 1/2 at distance r, Pi(j) = c(r) <= C exp(-c r/s(beta)). So in P_N a separated pair has weight at most 4 C^N exp(-c N r/s): the dual charges are confined by a linear potential. The neutral question for K_N becomes: does a dense gas of linearly confined non-abelian charges, with positive weights d_j tr[Pi(j)^N], have a finite correlation length? At N = 2 it has (C4 (c), GIVEN the posted O(4) theorem at 2 beta). At N = 3 and 4 this is (K_N-N), OPEN.

## Step 4. Two more exact forms, and two test models inside the family (PROVED unless marked; unchecked)

### 4.1 Lemma D1 (complete-graph fibres: planes independent in an annealed quaternion bond field)

Let Kc_N be the model of N planes k_1, ..., k_N in K with all pairs coupled: density proportional to prod over bonds f of exp(beta sum_(p<p') <n_p(f), n_p'(f)>), with n_p(f) = k_p(y) k_p(y')^(-1). (Every relative sheet k_p^(-1) k_p' carries one O(4) energy, because <n_p, n_p'> = <k_p'^(-1) k_p (y), k_p'^(-1) k_p (y')>.) For N = 3 the cycle is the complete graph, so Kc_3 = K_3.

Let gamma be the standard Gaussian law on R^4, read as quaternions. Fix one orientation y -> y' of every bond f and put one variable zeta_f on it. Consider the joint density, with respect to prod gamma(d zeta_f) prod dk_p,

  prod_p w_zeta(k_p),   w_zeta(k) = prod_f exp( sqrt(beta) < zeta_f k(y'), k(y) > ).

Then: (i) the law of the planes is Kc_N; (ii) given zeta, the planes are independent and identically distributed, with density w_zeta/Z[zeta]; (iii) zeta has density proportional to Z[zeta]^N with respect to prod gamma; (iv) given the planes, the zeta_f are independent Gaussians with mean sqrt(beta) S_f, S_f = sum_p n_p(f), and unit covariance; (v) Z[zeta] is invariant under zeta_f -> c(y) zeta_f c(y')^(-1).

Proof. The n_p(f) are unit vectors of R^4, so sum_(p<p') <n_p, n_p'> = (|S_f|^2 - N)/2. For x in R^4, exp((beta/2)|x|^2) = int gamma(d zeta) exp(sqrt(beta) <zeta, x>). And <zeta, k(y) k(y')^(-1)> = Re(zeta k(y') k(y)^(-1)) = <zeta k(y'), k(y)>. (iv): complete the square. (v): substitute k -> c k. QED.

Reading. Given zeta, each plane is one O(4) sheet with bond strength sqrt(beta)|zeta_f| and a one-sided twist zeta_f/|zeta_f|, and with an exact global symmetry on the other side. This is the class of the posted charged estimates (3.61), (3.62) (row 1009's reading: fixed one-sided twists, signed couplings), except that the strengths are unbounded Gaussian variables. In bilinear form the bond weight of Kc_N is exp((beta/2) |Psi(y) Psi(y')^*|^2 - beta N/2) with Psi = (k_1, ..., k_N) and Psi Psi'^* = sum_p k_p(y) conj k_p(y'). This is a quaternionic relative of the lattice CP^(N-1) weight exp(beta |conj z . z'|^2) (RECALLED form), with gauge group SU(2) and the stronger constraint that every component is a unit quaternion.

### 4.2 Lemma D2 (the three-sheet coupling is frustrated in sheet coordinates)

Write a sheet value as a = [[z_a, w_a], [-conj w_a, conj z_a]], z = r e^(i alpha), w = rho e^(i gamma). For a, b at one base site and a', b' at a neighbour,

  <ab, a'b'> = + T1 - T2 - T3 + T4 + T5 + T6 + T7 + T8,

where each T is a product of four moduli times the cosine of: T1: alpha_a + alpha_b - alpha_a' - alpha_b'; T2: alpha_a + alpha_b - gamma_a' + gamma_b'; T3: gamma_a - gamma_b - alpha_a' - alpha_b'; T4: gamma_a - gamma_b - gamma_a' + gamma_b'; T5: alpha_a + gamma_b - alpha_a' - gamma_b'; T6: alpha_a + gamma_b - gamma_a' + alpha_b'; T7: gamma_a - alpha_b - alpha_a' - gamma_b'; T8: gamma_a - alpha_b - gamma_a' + alpha_b'. No constant shift of the eight angles makes all eight coefficients non-negative when all moduli are in (0, 1).

Proof. (ab)_11 = z_a z_b - w_a conj w_b, (ab)_12 = z_a w_b + w_a conj z_b, and <g, h> = Re(g_11 conj h_11 + g_12 conj h_12). Expand. The forms T2 - T1 and T6 - T5 are the same linear form, alpha_a' + alpha_b' - gamma_a' + gamma_b'. A shift that makes T1, T5, T6 non-negative and turns the sign of T2 would need this form to be 0 and pi at the same shift. QED.

So the energy E(a) + E(b) + E(ab) of K_3 is not of Ginibre type in the Hopf coordinates of the sheets. In the coordinates of the planes the same holds by Lemma HF of row 1188, which I use as stated and did not check again (the word k_0(y) k_0(y')^(-1) k_1(y') k_1(y)^(-1) is its plaquette word with two letters inverted; inversion reflects one angle and shifts the other, and the property is invariant under reflections and shifts). The entry point of OpenAI's Section 3.11 is closed in both coordinate systems.

### 4.3 Test models inside the family (one PROVED identity, two RECALLED theorems)

Replace SU(2) by another compact group G in the definition of K_N, with the bond function (1/2)(chi + conj chi) of a faithful character where needed.

- **G = Z_2, N = 3 (PROVED): K_3 is the four-state Potts model with coupling 4 beta.** With sigma = k_0 k_1, tau = k_1 k_2 the bond energy is beta (sigma sigma' + tau tau' + sigma sigma' tau tau'). It equals 3 beta when (sigma, tau) = (sigma', tau') and -beta in the three other cases, so it is -beta + 4 beta delta. RECALLED, not rebuilt: on Z^2 this model has its transition at exp(4 beta) = 1 + sqrt 4 = 3, that is beta = (log 3)/4, and the transition is continuous (Baxter; Beffara and Duminil-Copin; Duminil-Copin, Sidoravicius and Tassion). At that coupling the charged (spin) two-point function has no exponential bound. Above it the symmetric state is a mixture of four ordered states. For the energy covariance at the transition I recall no theorem and I claim none.
- **G = Z_2, N = 4 (PROVED):** with x = (sigma, tau, upsilon) the bond energy is 4 beta [delta(x = x') - delta(x = -x')]. This is an Ising sign carried by a four-state colour, coupled only at equal colours (a cubic model with four colours).
- **G = U(1) (GUIDE):** 3.7, the Coulomb gas at inverse temperature N/beta.

Use. A proof of exponential clustering of all local observables of K_N at every beta must fail for Z_2 at beta at least (log 3)/4 (theorem grade, RECALLED) and for U(1) at large coupling (GUIDE). So it must read that the group is connected and that it is not abelian, both at order one. This is the lane's test table (compact U(1), frozen groups) inside this one family, with a discrete member whose transition coupling is explicit. It does not bind a statement about neutral observables alone.

## Step 5. The neutral lemma (K_N-N): what is supplied, three ways in, and the one statement where each stops

### 5.1 Proposition E1 (the charged half for every fibre; PROVED GIVEN one posted estimate)

GIVEN. Estimate (3.61) of OpenAI's O(4) paper in its cell-boundary form, as checked against the primary text in row 1079 (`gap-bridge-vectors-check-astra.md` L238-296, item 5): on a finite rectangle with free boundary, with bond strengths anywhere in [0, b] and fixed one-sided twists, condition on the sheet outside a union of coarse cells that is a neighbourhood of supp O inside its r/2 neighbourhood; then an observable O with zero average under the rigid rotation of its support has |E O| <= C |O| |supp O| exp(-c r/s(b)), after a change of absolute constants. That check records that the paper states no theorem for a pin on an arbitrary interior set, and gives this repair with boundary pins. I did not read the primary text.

Statement. In the corner model of row 1189 on F x B, with F any finite graph of degree at most Delta_F: for planes p_0 != p_1 and base sites y_0, y_1 at distance r, the mixed rectangle W = (1/2) tr[k(p_0, y_0)^(-1) k(p_1, y_0) k(p_1, y_1)^(-1) k(p_0, y_1)] has |mu(W)| <= 2 C exp(-c r/s(Delta_F beta)). If F is a rectangle too, the same holds with the fibre distance R of p_0 and p_1 in place of r. So |mu(W)| <= 2 C exp(-c max(R, r)/s(4 beta)).

Proof. By Lemma A5 of row 1189, given the other planes the plane p_0 is one O(4) sheet with bond strengths beta |Q| <= Delta_F beta, a one-sided twist, and an exact rigid group on the other side. Condition also on that plane outside a union of coarse cells around y_0 inside the r/2 neighbourhood of y_0. For r above a fixed multiple of s this fixes the spin at y_1. The entries of the spin at y_0 have zero average under the rigid rotation, and W is linear in that spin with coefficients of norm at most 1. For smaller r use |W| <= 1 and enlarge C. The second claim is the first after the exchange of Lemma A2 of row 1189. QED.

This is (O5) of row 1110 for every fibre, with the same input. It is a bound of perimeter type. For a fibre that is a chain the sheets are independent and mu(W) = c(r)^R exactly, an area law; for a two-dimensional fibre I have no area law (two attempts in my notes stop at a diamagnetic comparison for one-sided twists, which I can neither prove nor find on file; method 36 refutes the two-sided form).

### 5.2 The lemma

**(K_N-N), N = 3 or 4, beta > 0 (OPEN).** There are C and c > 0 such that for every rectangle B, all bonds f, f' of B and all functions F, G with values in [-1, 1], F of m_0 on f and G of m_0 on f', both invariant under m_0 -> a m_0 b: |Cov_(K_N)(F, G)| <= C exp(-c dist(f, f')).

N = 4 is (K4-N) of row 1115 3.2 with its (K9). N = 3 is smaller and has the same features: no one-site singlet, a rigid group SU(2)^3 that is transitive on the one-site space, no association (D2). N = 2 is the posted O(4) theorem at coupling 2 beta (C4 (c)). So N = 3 is the first open member. I recommend it as the form of the lemma.

### 5.3 Three ways, each to its first failing step

**Way 1: association (the posted route to singlets).** Fails at its entry. D2 and Lemma HF: the energy is not of Ginibre type in the Hopf coordinates of the sheets or of the planes. I know no third coordinate system. The Z_2 member is a ferromagnet (the four-state Potts model) and the U(1) member has Ginibre's inequalities; the obstruction is the sign pattern of the SU(2) product.

**Way 2: one sheet given the others, then the posted theorem.** By C4 (e) and row 1115 3.2, a sheet given the others is one O(4) sheet with strengths 2 beta cos(theta_f/4) and twists that are the geodesic midpoints of the increments of the other sheets. The posted charged estimates hold for it (E1). The posted singlet step does not: it needs untwisted non-negative couplings, and the midpoint field is frustrated by the commutators of the increments (remark after C4). For U(1) the same conditional sheet is frustration-free away from vortices, and the substitution phi -> phi - alpha/2 removes the twist. So the first failing step is exactly the non-abelian part. Its size per plaquette is of order 1/beta in angle, but the commutator sum over a block of side l has size of order l/beta (ARGUED: sum of l^2 terms of size 1/beta with no fixed sign), so the frustration is of order one at side beta, far below the mixing length. It is not a small perturbation at the scale that matters.

**Way 3: the dual gas (C2).** (K_N-N) for one-sheet observables is a statement about the positive weights d_j tr[Pi_(FG)(j) Pi(j)^(N-1)]. GIVEN (3.62) the charges are confined linearly, and that is where SU(2) differs from U(1) (3.7). First failing step: a bound that factorizes tr[Pi(j)^N] over separated neutral clusters of a dense flux configuration with a relative error that can be summed. The posted covariance bound (3.67) is additive. The cluster weights are exponentially small in N and in the cluster size, so an additive error does not control the ratio. At N = 2 the sum is known in closed form (the sheet at 2 beta); I found no interpolation from N = 2 to N = 3 that keeps a bound.

**A fourth form with the same stop (D1).** For complete-graph fibres the planes are independent given the annealed quaternion bond field zeta, and for a two-plane singlet Q_f = <n_1(f), n_2(f)> one has E[Q_f | zeta] = |nu_f(zeta)|^2 with nu_f the mean current of one twisted sheet. So the covariance of Q_f and Q_f' is controlled by the dependence of nu_f(zeta) on zeta at f', and by the current covariance of one twisted sheet. Both are neutral responses of a twisted sheet. ARGUED reading at large N with beta = lambda/N: the saddle is an untwisted sheet at the coupling b that solves b = lambda e(b), e the mean bond energy, non-zero only for lambda > 4; the phase of zeta is a two-dimensional SU(2) gauge field with an induced action of order N. So in this family the neutral sector is a two-dimensional gauge theory with N flavours of S^3-valued scalars at infinite gauge coupling. That is a picture, not a bound.

### 5.4 The statement where all ways stop

**(N-tw) (OPEN; on file in other words: (S-a) and NR of rows 1109, 1110, 1115).** For one O(4) sheet on a rectangle with strengths in [0, 2 beta] and one-sided twists drawn from the law that K_N induces: the covariance of two singlet bond observables at distance d, and the response of a singlet bond expectation to a change of the twist field at distance d, are at most C exp(-c d), in mean over the twist field.

What this session adds to it: (1) the twist field is explicit, the midpoint field of C4 (e); (2) its frustration is the commutator sum, which vanishes identically for an abelian group away from vortices; (3) an equivalent positive form with no twist at all, the flux gas of C2, in which the group enters through the confinement of the dual charges; (4) the smallest member, N = 3, and its two test models (4.3). None of these proves (N-tw).

Three ways failed at one statement, so the stop rule of 2.3 applies. I did not find a fourth way that is not a renaming.

## Step 6. State at the end (2026-11-20T01:04Z, `date -u`; last correction 01:06Z)

Provenance: Claude Fable 5.2 max, Mac mini worker 2, one session from 2026-11-20T00:00Z, no subagents. Author only. Checked by no one. No numeric run: free memory was 40 percent and then 42 percent (`memory_pressure`), below the 50 percent rule, so every identity was derived by hand and re-derived once before it was written. No literature was fetched. I did not read the primary text of the posted O(4) proof; I used the lane's digests (`library/prior/gap-o4-pinned-cell-read-opus.md`, rows 1009, 1076, 1110, 1115) and marked each use GIVEN. I did not open the Sussman-Alpoge repository in this session: the lane's index of their outline lists the mass gap as their own open requirement (`library/sa-index/chunk-01.md` L70 "assumed", L86 "named open"; `chunk-04.md` L277 "a separate positive spectral estimate for a mass gap"), so no step of the gap can be ported from their text. The search of `origin/main` and of the open PR branches was not possible from this checkout.

| Statement | Label |
|---|---|
| Four-dimensional SU(2) Yang-Mills has a mass gap (Jaffe and Witten) | OPEN. Not proved here |
| (N-phys), the continuum datum, (BS), (W) | OPEN. Not attacked directly. Step 2.1 found no route off the lane's map |
| Step 2.1, the screening; 2.2, where every route stops | GUIDE; ARGUED |
| C0-C4: K_N is a convolution power on the group of sheets; flux form with the positive dual gas P_N(j) = d_j tr[Pi(j)^N]/z_N; exact formula for all sheet correlations; the bound norm Pi(j) <= 1 - exp(-2 beta Delta), uniform in the base; marginals; (K4) as the squared density of a product of two sheets; the midpoint twist identity | PROVED (elementary; by Claude Fable 5.2, not yet checked by the other model) |
| Remark after C4: the conditional twist field is frustrated by commutators, at second order | ARGUED (second order of the series only) |
| 3.7: the dual gas is a Coulomb gas for U(1), and a gas of linearly confined charges for SU(2) | GUIDE for U(1); GIVEN (3.62) for SU(2) |
| D1: complete-graph fibres are independent planes in an annealed quaternion bond field, with weight Z[zeta]^N | PROVED (same standing) |
| D2: the three-sheet energy is not of Ginibre type in sheet coordinates | PROVED (same standing) |
| 4.3: the Z_2 form of K_3 is the four-state Potts model at coupling 4 beta; the Z_2 form of K_4 is a four-colour cubic model | PROVED identities; the Potts transition facts are RECALLED |
| E1: perimeter-type exponential bound for every mixed rectangle of the corner model, every fibre | PROVED GIVEN (3.61) in the cell-boundary form of check row 1079 and Lemmas A2, A5 of row 1189 (unchecked) |
| (K_N-N), N = 3, 4; (N-tw) | OPEN. Three ways written, each stops at (N-tw) |
| Large-N reading of the complete-graph family | ARGUED |

New against the record, as far as my greps show: C1-C4 (the convolution and flux form of the cycle models, which contain the lane's (K4)); D1; D2; the two discrete identifications of 4.3; the explicit midpoint twist of C4 (e) and its commutator frustration. Not new: E1 is (O5) of row 1110 extended to every fibre with the same input; (N-tw) is (S-a) and NR in other words; the screening of Step 2; everything in 2.2.

What none of it does. It gives no bound on any neutral covariance. It does not move (N-phys), (SING), (BS) or (W). By row 1115 2.2 the family (SING) is beside the path from the target, so even a proof of (K_3-N) would be a mechanism, not a step of the chain.

For the lead (ARGUED, short).
1. The smallest open member of (SING) is N = 3, three O(4) sheets with product one. Its one-site space is SU(2)^3 modulo the diagonal, a Ledger-Obata space (RECALLED name), and its bond weight is exp((beta/2)|n_0 + n_1 + n_2|^2). It has no vortices (the space is simply connected), no association (D2), and exact discrete and abelian relatives with known behaviour (4.3, 3.7). If a reading row is spent on (SING) again, these are the words to search: sigma models on G^3 modulo the diagonal, and lattice models with the weight exp(beta |conj z . z'|^2).
2. The flux form C2 is the only form I found in which the group enters a neutral question through a proved (GIVEN) charged fact: confinement of the dual charges. A consumer would be a theorem that a dense gas with positive weights and linearly confined constituents mixes. I know none, and the Z_2 member shows that none can hold without reading that the group is connected.
3. I agree with rows 1188-1190: one more plain-brief row by this model family will find the same map. This row spent its effort on one lemma instead; the lemma stayed open.

Check request: one cross-provider read of C0-C4, D1, D2 and 4.3 is enough; they are short. E1 uses the repaired form of (3.61) from check row 1079 item 5 and two lemmas of row 1189 that are themselves unchecked.

Credits. Jaffe and Witten (the problem). Balaban; Sussman and Alpoge, with Claude and Codex as authors of their text (the account that the lane's chain reads; not used in a step here). OpenAI (the posted O(4) and O(3) proofs: the pinned-cell stiffness iteration, the charged estimates (3.61), (3.62), the association step 3.11); Ding, Huang and Yang (the second posted proof). Claude Opus 5.5 and gpt-6-astra for the digests and for rows 1009, 1076, 1110, 1114. Row 1053 (the doubly flat corner), row 1115 ((SING), (K4-N)), row 1188 (Lemma HF), rows 1189 and 1190. Durhuus and Frohlich; Orland (sheets in anisotropic gauge theory). Osterwalder and Seiler; Luscher; 't Hooft (transfer operator, flux sectors). Peter and Weyl. Ginibre; Dunlop and Newman. Baxter; Beffara and Duminil-Copin; Duminil-Copin, Sidoravicius and Tassion (four-state Potts, recalled). Kosterlitz and Thouless; Frohlich and Spencer (Coulomb gas, recalled). Ledger and Obata (the homogeneous space, recalled). Tanizaki and Unsal (thin twisted torus, named in 2.1). Mack and Petkova; Tomboulis (named in 2.1).

RESULT: Row 1194 (Claude Fable 5.2 max, Mac mini worker 2, 2026-11-20 00:00Z-01:06Z; author only, checked by no one; no numeric run, free memory 40-42 percent). The mass gap is NOT proved and nothing is disproved; (N-phys), the continuum datum, (BS), (W) stay OPEN. Seven more routes derived from the target were all on the lane's map (GUIDE). The effort went to the lane's named neutral first lemma, (K4-N) of row 1115, in the family K_N of N O(4) sheets with product one. PROVED by hand, unchecked, not selective: K_N is a convolution power on the group of sheets (C1), with an exact flux form and a positive dual gas of non-abelian charges, P_N(j) = d_j tr[Pi(j)^N]/z_N, and an exact formula for all sheet correlations (C2); norm Pi(j) <= 1 - exp(-2 beta Delta) uniformly in the base (C3); (K4) is the squared density of the product of two sheets, and a sheet given the others has the geodesic midpoints of their increments as twists (C4), frustrated at second order by commutators (ARGUED); complete-graph fibres are independent planes in an annealed quaternion bond field (D1); the three-sheet energy is not of Ginibre type (D2); the Z_2 form of K_3 is the four-state Potts model at coupling 4 beta (4.3). PROVED GIVEN the posted estimate (3.61) in the cell-boundary form of check row 1079: a perimeter-type exponential bound for every mixed rectangle of the doubly flat corner, every fibre (E1). OPEN: (K_N-N) for N = 3, 4, attacked three ways (association, conditional sheets, dual gas), each stopping at the neutral response of one twisted sheet (N-tw), which is the lane's (S-a) and NR; (SING); (N-phys); the mass gap. Output library/gap-mini-solve-e-fable.md.
