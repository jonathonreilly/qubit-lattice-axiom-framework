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
(c) z_N = sum_j d_j tr[Pi(j)^N]. Every term is non-negative. The term j = 0 is 1. So z_N >= 1, z_N is non-increasing in N, and

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

Let gamma be the standard Gaussian law on R^4, read as quaternions, and put one variable zeta_f on each oriented bond. Consider the joint density, with respect to prod gamma(d zeta_f) prod dk_p,

  prod_p w_zeta(k_p),   w_zeta(k) = prod_f exp( sqrt(beta) < zeta_f k(y'), k(y) > ).

Then: (i) the law of the planes is Kc_N; (ii) given zeta, the planes are independent and identically distributed, with density w_zeta/Z[zeta]; (iii) zeta has density proportional to Z[zeta]^N with respect to prod gamma; (iv) given the planes, the zeta_f are independent Gaussians with mean sqrt(beta) S_f, S_f = sum_p n_p(f), and unit covariance; (v) Z[zeta] is invariant under zeta_f -> c(y) zeta_f c(y')^(-1).

Proof. The n_p(f) are unit vectors of R^4, so sum_(p<p') <n_p, n_p'> = (|S_f|^2 - N)/2. For x in R^4, exp((beta/2)|x|^2) = int gamma(d zeta) exp(sqrt(beta) <zeta, x>). And <zeta, k(y) k(y')^(-1)> = Re(zeta k(y') k(y)^(-1)) = <zeta k(y'), k(y)>. (iv): complete the square. (v): substitute k -> c k. QED.

Reading. Given zeta, each plane is one O(4) sheet with bond strength sqrt(beta)|zeta_f| and a one-sided twist zeta_f/|zeta_f|, and with an exact global symmetry on the other side. This is the class of the posted charged estimates (3.61), (3.62) (row 1009's reading: fixed one-sided twists, signed couplings), except that the strengths are unbounded Gaussian variables. In bilinear form the bond weight of Kc_N is exp((beta/2) |Psi(y) Psi(y')^*|^2 - beta N/2) with Psi = (k_1, ..., k_N) and Psi Psi'^* = sum_p k_p(y) conj k_p(y'). This is a quaternionic relative of the lattice CP^(N-1) weight exp(beta |conj z . z'|^2) (RECALLED form), with gauge group SU(2) and the stronger constraint that every component is a unit quaternion.

### 4.2 Lemma D2 (the three-sheet coupling is frustrated in sheet coordinates)

Write a sheet value as a = [[z_a, w_a], [-conj w_a, conj z_a]], z = r e^(i alpha), w = rho e^(i gamma). For a, b at one base site and a', b' at a neighbour,

  <ab, a'b'> = + T1 - T2 - T3 + T4 + T5 + T6 + T7 + T8,

where each T is a product of four moduli times the cosine of: T1: alpha_a + alpha_b - alpha_a' - alpha_b'; T2: alpha_a + alpha_b - gamma_a' + gamma_b'; T3: gamma_a - gamma_b - alpha_a' - alpha_b'; T4: gamma_a - gamma_b - gamma_a' + gamma_b'; T5: alpha_a + gamma_b - alpha_a' - gamma_b'; T6: alpha_a + gamma_b - gamma_a' + alpha_b'; T7: gamma_a - alpha_b - alpha_a' - gamma_b'; T8: gamma_a - alpha_b - gamma_a' + alpha_b'. No constant shift of the eight angles makes all eight coefficients non-negative when all moduli are in (0, 1).

Proof. (ab)_11 = z_a z_b - w_a conj w_b, (ab)_12 = z_a w_b + w_a conj z_b, and <g, h> = Re(g_11 conj h_11 + g_12 conj h_12). Expand. The forms T2 - T1 and T6 - T5 are the same linear form, alpha_a' + alpha_b' - gamma_a' + gamma_b'. A shift that makes T1, T5, T6 non-negative and turns the sign of T2 would need this form to be 0 and pi at the same shift. QED.

So the energy E(a) + E(b) + E(ab) of K_3 is not of Ginibre type in the Hopf coordinates of the sheets. In the coordinates of the planes the same holds by Lemma HF of row 1188 (the word k_0(y) k_0(y')^(-1) k_1(y') k_1(y)^(-1) is its plaquette word with two letters inverted; inversion reflects one angle and shifts the other, and the property is invariant under reflections and shifts). The entry point of OpenAI's Section 3.11 is closed in both coordinate systems.

### 4.3 Test models inside the family (one PROVED identity, two RECALLED theorems)

Replace SU(2) by another compact group G in the definition of K_N, with the bond function (1/2)(chi + conj chi) of a faithful character where needed.

- **G = Z_2, N = 3 (PROVED): K_3 is the four-state Potts model with coupling 4 beta.** With sigma = k_0 k_1, tau = k_1 k_2 the bond energy is beta (sigma sigma' + tau tau' + sigma sigma' tau tau'). It equals 3 beta when (sigma, tau) = (sigma', tau') and -beta in the three other cases, so it is -beta + 4 beta delta. RECALLED, not rebuilt: on Z^2 this model has its transition at exp(4 beta) = 1 + sqrt 4 = 3, that is beta = (log 3)/4, and the transition is continuous (Baxter; Beffara and Duminil-Copin; Duminil-Copin, Sidoravicius and Tassion). At that coupling no exponential bound holds for the energy covariance. Above it the symmetric state is a mixture.
- **G = Z_2, N = 4 (PROVED):** with x = (sigma, tau, upsilon) the bond energy is 4 beta [delta(x = x') - delta(x = -x')]. This is an Ising sign carried by a four-state colour, coupled only at equal colours (a cubic model with four colours).
- **G = U(1) (GUIDE):** 3.7, the Coulomb gas at inverse temperature N/beta.

Use. A proof of (K_N-N) at every beta must fail for Z_2 at one explicit coupling and for U(1) at large coupling. So it must read that the group is connected and that it is not abelian, both at order one. This is the lane's test table (compact U(1), frozen groups) inside this one family, with a theorem-grade discrete member.
