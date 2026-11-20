lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T14:41Z

# gap-mini-solve-l-fable: the mass gap of four-dimensional SU(2) Yang-Mills

Queue row 1202 of `FINISH.md`, pinned at commit ac1da4568. Worker: Claude Fable 5.2, max effort, Mac mini worker 3. Research-stage working state. Nothing here is a public claim, and no status is granted.

Labels used below: PROVED (every step written here or in a cited checked note), ARGUED (an argument with a named unproved step), GUIDE (heuristic or numeric, never a proof step), OPEN.

## 0. Session log

- 2026-11-20T02:41Z. File created. Next: read the sibling rows `gap-mini-solve-a` to `-k`, `parts/gap.md`, and the RESULT lines, so that this row attacks something they did not.
- 2026-11-20, between 02:41Z and 03:20Z (time not read from the clock). Record read (Section 1 below). No screening of route families is repeated in this row: rows 1188-1201 did it eleven times and found the lane's map each time.
- 2026-11-20, about 03:20Z (time not read from the clock; an earlier version of this line said 04:30Z, which was wrong). Section 2 written (how I looked for an attack, and what I found again). Attack item chosen in Section 3.
- 2026-11-20T03:27Z (`date -u`). Sections 3.1 to 3.4 written.
- 2026-11-20T03:31Z (`date -u`). Sections 3.5 to 3.7 written. Then four wording corrections after a re-read of the proofs.
- 2026-11-20T03:35Z (`date -u`). Section 3.8, Section 4 and the RESULT line written.

## 1. Where the record stands (statements about the record, not evidence)

Read in this session: `GOAL.md` in full; `FINISH.md` L1-84, L299-350, row 1202 and the RESULT lines of rows 1179-1201; `parts/gap.md` L1-104 and L223-330; `library/gap-council-synthesis.md` in full; `library/gap-mini-solve-g-fable.md` and `-i-fable.md` in full; `library/prior/gap-2don-proofs-read-opus.md` L1-201 (the digest of Ding, Huang and Yang, arXiv:2611.04908, and of OpenAI's two-dimensional O(n) preprints); `library/gap-solve9-astra62.md` L1-180 (row 1161, the form of (N-phys)).

1. **Two open inputs.** By Theorem BP of row 1179 (check row 1183: the main chain HOLDS AFTER CORRECTION), the Jaffe-Witten gap clause follows from (a) the continuum datum of the T0 chain and (b) one lattice estimate, (N-phys) of row 1161: on one periodic cube n^3 of fixed physical side, uniformly in the cutoff, the centre-neutral excited trace s(u) at a time u at most n/K is at most 1/2. Both are OPEN.
2. **The wall in one sentence** (`parts/gap.md`, The exact price): one selective inequality at every scale between first passage and the seed size is missing. Selective means false for a massless factor.
3. **The only known mechanism at all couplings** is the pair of posted, unrefereed two-dimensional O(n) proofs. Its three parts are: an exact symmetry twist with a smooth periodic free energy; a fourth-order commutator inequality that bounds the twist stiffness by C/log N; a positivity structure (sign clusters, Ginibre, pinning) that turns a small twist cost into decay. The lane's rows 1009-1018, 1076-1086, 1188, 1193, 1195 found that pure SU(2) gauge theory has the bracket, has no non-gauge continuous symmetric twist on the integration variables, and has no association.
4. **Siblings.** Rows 1188-1201 (a to k) each re-derived the map and then worked one small item. None is on the path of (N-phys) except by restatement.

## 2. How best to attack it: what I derived, and where each line already sits (GUIDE; nothing here is a proof step)

I did not screen route families from a list. I started from the one mechanism that is known to cross an asymptotically free band (the posted two-dimensional O(n) proofs, read in `library/prior/gap-2don-proofs-read-opus.md` and `library/prior/gap-o4-pinned-cell-read-opus.md`; credit OpenAI, and Ding, Huang and Yang) and asked what each of its three parts needs in four dimensions. Every line below was derived in this session and then found on file.

| What I derived | Where it already sits |
|---|---|
| The posted iteration is a one-sided renormalization: "stiffness = direct term minus current variance", the direct term is a gradient form for every pin because the group is rigid, and the bracket term of the Ward identity gives a lower bound on the variance | rows 1009, 1010 (reading); row 1011 |
| In the gauge theory a link translation by a fixed colour has a direct term of mass form: beta a^2 abs(A_perp)^2, about a^2 per link for a typical field. The exact response is of curl form only after the seagull term cancels against the current variance. A Jensen bound drops the variance, so it cannot see the cancellation | Lemma WN, Lemma JEN and "best lab-frame bound of order beta eta^2 R" (row 1013); Proposition J (row 1181); Lemmas PC, PC-c (rows 1188, 1193); (HM) of row 1195 |
| A covariant colour axis does not help: the adjoint covariant Laplacian of a typical field has a gap of order 1/beta per link | row 1141 (2); row 1177 (14), (26) |
| Colour twists of pins are free unless a pinned path carries them; the only non-removable continuous twist is a Schrodinger-functional deformation (a holonomy of the pin) | Lemma TWIST (row 1013), Lemma REM (row 1016) |
| A trivially pinned plate has the full rigid group on its free side (the adjacent layer of normal links is an O(4) model in a one-sided background) | Lemma EMB (row 1011), Lemma SLAB (row 1013), sheets with one-sided twists (rows 1096-1123, 1194, 1199) |
| The twist can be spread along the plate at gradient cost but not across the thickness; spreading across the thickness is a translation of rough slices and pays the seagull | row 1013 5.1; (HM) |
| Rough pins have stabiliser Z_2, so a class of pins that is closed under conditioning carries no rigid group | (R-b) of row 1016 6.2; row 1011 7.1 |
| Neutral observables are the whole content of a gauge theory; charged decay is automatic (Elitzur) and gives nothing | rows 731, 1025 (Lemma FAC), 1134 2c |
| SO(3) x Z_2 split: the centre is a ferromagnetic Z_2 gauge theory given the SO(3) part on monopole-free fields, with Griffiths inequalities; frozen at order-one coupling | rows 858-900 (ideas 15, 38, 52; C4, GKS-C) |
| Spacetime symmetries cannot be selective, because the free Maxwell field has them | row 1201 |
| A step-scaling inequality for a finite-volume coupling is the wall in another form | (CAS), route RA; row 859 |

Verdict (GUIDE): a twelfth plain-brief pass by this model family finds the same map. I found no mechanism for the neutral half and no route off the map.

## 3. The worked item: the slab between two trivially pinned plates

**Why this item.** Row 1016 6.2 corrected the reopen condition of row 1013 to three clauses: a rigid group (R-a), charged pins (R-b), a response on the gauge-invariant algebra (R-c). Lemma REM of row 1016 says that a colour twist is not removable exactly when a pinned path carries it. The smallest object that has (R-a) and (R-c) together is a slab whose two plates are pinned to the trivial field, with a periodic cross-section: the rigid group is the constant gauge rotation of one plate, and the twist is a flat holonomy of that plate around a cycle (a toron). I work this object out exactly. It does not have (R-b): 3.7 says where it stops. Kind of result: exact statements about a setting that the lane has in pieces (Lemma EMB of row 1011, Lemmas SLAB and JEN of row 1013, Lemma REM and Identity HAM1 of row 1016, (S1') of row 1195). None of it moves (N-phys).

Greps before writing (`library/open-core.md`, `FINISH.md`, `library/gap-*.md`): open-core has no entry for toron, plate, trivial pin or Schrodinger functional. FINISH rows 1011, 1014, 1016, 1195 list "the Schrodinger-functional bound at the trivial pin" as OPEN. I found no file with the crossed transfer operator of a pinned slab, the flux-sector expansion 3.3, or the limit 3.5.

### 3.1 Setting

- Cross-section: the torus Lambda = (Z/R_1) x (Z/R_2) x (Z/R_3), every R_i at least 3. Heights t = 0, ..., T, with T at least 2. Area A = R_2 R_3.
- Horizontal links (x, t; i), i = 1, 2, 3, go from (x, t) to (x + e_i, t). Vertical links (x, t; 0) go from (x, t) to (x, t + 1), t at most T - 1.
- Pinned links: the horizontal links at heights 0 and T. The bottom pin is 1. The top pin is a given field omega. All other links are free and carry Haar measure.
- Weight w(g) = exp((beta/2) tr g), beta > 0. Plaquette variable U_p = U_mu(y) U_nu(y + e_mu) U_mu(y + e_nu)^(-1) U_nu(y)^(-1). Z_T(omega) is the integral over the free links of the product of w(U_p) over the plaquettes with at least one free link.
- Toron pin omega^h, h in SU(2): omega_1(x) = h when x_1 = R_1 - 1; every other top link is 1. It is flat, with holonomy h around the x_1 cycles.
- R_T(h) = Z_T(omega^h)/Z_T(1). h_phi = cos(phi/2) + i sigma_3 sin(phi/2). chi_j is the character of spin j and d_j = 2j + 1.
- For compact U(1): links e^(i theta), plaquette weight exp(beta cos theta_p), toron angle alpha, R_T(alpha).

### 3.2 Lemma 1 (pins up to gauge; PROVED; it is Lemma TWIST of row 1013 and Lemma REM of row 1016 in this geometry)

For every site map g on the slab, Z_T does not change when the two pins are replaced by their gauge transforms. So: (a) Z_T(omega^h) = Z_T(omega^(k h k^(-1))) for every k, and R_T is a class function; (b) the "spread" toron (omega_1(x) = eta for all x, eta^(R_1) = h, other top links 1) has the same Z_T as omega^h; (c) for every real function f on Lambda, the top pin omega_i(x) = exp(i (f(x) - f(x + e_i)) sigma_3/2) has the same Z_T as the trivial pin.

Proof. Transform the free links by g. Haar measure is invariant and every plaquette trace is invariant. For (a) take g = k on the top sites and 1 elsewhere: the trivial top links stay trivial and the seam links become k h k^(-1). For (b) take g(x, T) = eta^(x_1), x_1 in {0, ..., R_1 - 1}. For (c) take g(x, T) = exp(i f(x) sigma_3/2). QED

(c) is the Ward identity of the plate in integrated form: a gradient twist of the plate costs nothing. The toron is the closed form on the plate that is not a gradient.

### 3.3 Lemma 2 (the crossed transfer operator and the flux sectors; PROVED)

**Statement.** There are numbers m_j(T) > 0, j = 0, 1/2, 1, ..., with sum_j d_j m_j = Z_T(1), such that Z_T(omega^h) = sum_j m_j chi_j(h). Hence, with P_T(j) = d_j m_j/Z_T(1), a probability law on spins,

  R_T(h) = sum_j P_T(j) chi_j(h)/d_j,   0 < R_T(h) < 1 for h not 1,   - (d^2/d phi^2) log R_T(h_phi) at phi = 0 equals (1/3) sum_j P_T(j) j (j + 1).

For U(1): Z_T(alpha) = sum over integers n of m_n e^(i n alpha) with m_n > 0.

**Proof.** Slice c is the set of free links of directions 0, 2, 3 whose base point has x_1 = c. H = L^2 of the slice configurations Sigma. Put V(Sigma) = -(beta/2) sum of tr U_p over the plaquettes of directions (0,2), (0,3), (2,3) in the hyperplane x_1 = c that have a free link (pinned links enter as 1). Put

  K_0(Sigma, Sigma') = prod over slice links l of w(Sigma'_l Sigma_l^(-1)),   K(Sigma, Sigma') = integral dg K_0(Sigma, g.Sigma'),

where g runs over SU(2)^(sites of the slice at heights 1..T-1), g = 1 at heights 0 and T, and (g.Sigma')_l = g_b Sigma'_l g_e^(-1) for a link from b to e. A (1, nu) plaquette with base y is U_1(y) U_nu(y + e_1) U_1(y + e_nu)^(-1) U_nu(y)^(-1), so with g_y = U_1(y) the kernel K is the integral over the direction-1 links between two neighbouring slices of all the plaquette weights that contain them. T_x = e^(-V/2) K e^(-V/2) is the crossed transfer operator.

1. T_x is self-adjoint, trace class and positive semi-definite. w = sum_k a_k chi_k with a_k = (2/beta)(2k + 1) I_(2k+1)(beta) > 0, so w is a positive-definite function on SU(2), K_0 is a positive semi-definite kernel (a tensor product of convolution kernels), and K_0 is injective. The map Sigma -> g.Sigma is a unitary action of a compact group that commutes with K_0, because w is a class function. Its average is the orthogonal projection P on the invariant functions. So K = P K_0 P, and T_x = e^(-V/2) P K_0 P e^(-V/2) is positive semi-definite. The kernel is continuous on a compact space, so T_x is trace class.
2. Let rho_h multiply every top vertical link (x, T - 1; 0) of the slice on the right by h^(-1), and (R_h psi)(Sigma) = psi(rho_h^(-1) Sigma). R is a unitary representation of SU(2). V o rho_h = V: the top vertical links enter V through tr(Sigma_nu(y) Sigma_0(y + e_nu) Sigma_0(y)^(-1)), where the top side is pinned to 1, and the two factors h cancel. K(rho_h Sigma, rho_h Sigma') = K(Sigma, Sigma') in the same way. So R commutes with T_x and with P.
3. For the seam slice pair the pinned top link of direction 1 is h, not 1. Its factor is w(g_b Sigma'_l h^(-1) Sigma_l^(-1)), so the seam kernel is K(Sigma, rho_h Sigma'), which is the kernel of K R_h. Each plaquette with a free link occurs once, so Z_T(omega^h) = Tr(T_x^(R_1) R_h).
4. Decompose H into isotypic parts of R: H = sum_j C^(d_j) (x) M_j and T_x = sum_j 1 (x) T_(x,j). Then Tr(T_x^(R_1) R_h) = sum_j chi_j(h) m_j with m_j = Tr(T_(x,j)^(R_1)), at least 0. At h = 1 the sum is Z_T(1).
5. m_j > 0. On the range of P the form of T_x is <e^(-V/2) psi, K_0 e^(-V/2) psi> > 0 for psi not 0 (V is invariant, so e^(-V/2) keeps the range of P). The matrix entries of D^j(Sigma_0(x_perp, 0) ... Sigma_0(x_perp, T - 1)), the vertical line from plate to plate, are invariant under g and transform with spin j under R. So every spin occurs in the range of P.
6. chi_(1/2)(h) < 2 for h not 1 gives R_T(h) < 1. R_T > 0 is clear. Z_T(omega^h) is smooth in h, so the m_j d_j decay faster than every power and the series may be differentiated term by term. chi_j(h_phi)/d_j is the mean of e^(i m phi) over m = -j, ..., j, which is 1 - j (j + 1) phi^2/6 + O(phi^4). QED

**Reading.** P_T(j) is the law of the colour flux that the plate sends around the x_1 direction: the "x_1-thermal" law of the rigid charge of the plate. The stiffness of the toron twist is one third of the mean Casimir of that flux. Half-integer spins are the centre-odd sectors: R_T(-1) = P_T(integer) - P_T(half-integer). Identity HAM1 of row 1016 is the same statement for a colour twist in a periodic time direction with no plates; there the twist is a Polyakov-loop insertion. Here the plates make it a boundary datum.

### 3.4 Proposition 4 (the blind bounds; PROVED; (a) is Lemma JEN of row 1013 in this geometry, (b) is row 1011 3.2)

(a) SU(2), every beta > 0 and every T: R_T(h_phi) >= exp(- beta A phi^2/(8 R_1)). So (1/3) sum_j P_T(j) j (j + 1) <= beta A/(4 R_1).

(b) Compact U(1), every beta > 0 and every T: R_T(alpha) >= exp(- beta A alpha^2/(2 R_1 T)).

Proof of (a). Use the spread toron of Lemma 1 (b) with eta = h_(phi/R_1). The only plaquettes that change are the (1, 0) plaquettes under the top plate. With c_x = U_0(x, T-1)^(-1) U_1(x, T-1) U_0(x + e_1, T-1), their traces change from tr c_x to tr(c_x eta^(-1)). So R_T(h_phi) = E[exp((beta/2) sum_x (tr(c_x eta^(-1)) - tr c_x))], E the trivially pinned law. By Jensen it is at least the exponential of the mean. The rigid rotation of 3.3 step 2 maps c_x to k^(-1) c_x k and keeps the law. The Haar average of k^(-1) c k is (tr c/2) 1. So E tr(c_x eta^(-1)) = E[tr c_x] cos(phi/(2 R_1)). With abs(tr c_x) <= 2 the exponent is at least - beta R_1 A (1 - cos(phi/(2 R_1))), which is at least - beta A phi^2/(8 R_1). The second statement follows because both sides are 1 at phi = 0 with zero first derivative.

Proof of (b). Use the spread toron, top links of direction 1 at angle alpha/R_1. Shift the free links (x, t; 1) by a(t) = alpha t/(R_1 T). Only the (1, 0) plaquettes change, each by f = alpha/(R_1 T). There are R_1 A T of them. Under the untwisted law E sin theta_p = 0 by theta -> - theta. Jensen gives R_T(alpha) >= exp(- beta R_1 A T (1 - cos f)) >= exp(- beta A alpha^2/(2 R_1 T)). QED

In (a) the twist sits in one layer. In (b) it is spread over the thickness, which is a translation of every slice by an abelian constant. For SU(2) that translation is not a change of variables with a curl-form cost: it is the seagull term of Lemma WN and (HM).

### 3.5 Proposition 5 (the vertical channel: the limit of a thick slab, and the neutral gap of the box; PROVED; standard spectral theory)

Let X be the space of fields Sigma on the horizontal links of Lambda, W(Sigma) = -(beta/2) sum of tr U_p over the horizontal plaquettes, K_v(Sigma, Sigma') = integral over g in SU(2)^Lambda of prod_l w(g_b Sigma'_l g_e^(-1) Sigma_l^(-1)), and T_v = e^(-W/2) K_v e^(-W/2). T_v is the ordinary transfer operator of the periodic box Lambda. As in 3.3 step 1 it is self-adjoint, trace class and positive semi-definite, and it vanishes on the orthogonal complement of the gauge-invariant functions. K_v is symmetric, because tr g^(-1) = tr g. Its kernel is continuous and strictly positive. By Jentzsch's theorem the top eigenvalue lambda_0 is simple, with a continuous, strictly positive, gauge-invariant eigenfunction Omega of norm 1. Let q < 1 be the second eigenvalue divided by lambda_0. So -log q is the gap of the box on all gauge-invariant states.

For a pin omega put u_omega(Sigma) = e^(-W(Sigma)/2) K_v(Sigma, omega), a continuous gauge-invariant function. For a slab with bottom pin omega_b and top pin omega_t write Z_T(omega_b, omega_t). Then, for T at least 2:

(a) Z_T(omega_b, omega_t) = <u_(omega_b), T_v^(T-2) u_(omega_t)>. This is a positive semi-definite kernel in the two pins.

(b) <Omega, u_omega> = lambda_0 e^(W(omega)/2) Omega(omega) > 0, and Z_T(omega_b, omega_t) = lambda_0^(T-2) ( <u_(omega_b), Omega><Omega, u_(omega_t)> + eps_T ), with abs(eps_T) <= norm(u_(omega_b)) norm(u_(omega_t)) q^(T-2).

(c) R_T(h) tends to R_inf(h) = Omega(omega^h)/Omega(1) as T grows, and sup over h of abs(R_T(h) - R_inf(h)) <= C q^T for T at least some T_0. So R_inf is the value of the vacuum wave functional of the box at the flat connection of holonomy h, relative to the trivial one.

(d) Conversely, if lambda is an eigenvalue of T_v with 0 < lambda < lambda_0 and psi is a normalized eigenfunction, then psi is continuous and there is a pin omega with psi(omega) not 0, and Z_T(omega, omega)/lambda_0^(T-2) - <u_omega, Omega>^2 >= (lambda/lambda_0)^(T-2) lambda^2 e^(W(omega)) psi(omega)^2. So the gap of the box is exactly the worst rate, over pins, at which a slab with equal pins forgets its thickness.

Proof. (a) Write the integral slice by slice at heights 1, ..., T - 1. There are T kernels K_v, one for each layer of vertical links, and each interior slice carries e^(-W), which is split into two halves. (b) The eigen-equation at the point omega gives the first formula, and the spectral theorem the second. (c) Divide the two expansions of (b); W(omega^h) = W(1) because omega^h is flat; the norms of u_(omega^h) are bounded uniformly in h. (d) <u_omega, psi> = lambda e^(W(omega)/2) psi(omega), and every term of the spectral sum of (a) at omega_b = omega_t is non-negative. QED

**Corollary 5.1 (compact U(1): the vacuum does not see torons; PROVED).** For every beta > 0 and every box, R_inf(alpha) = 1 for all alpha, so Omega takes the same value at the toron omega^alpha as at the trivial field, and P_T(n) tends to 0 for every n not 0. (The same proof, with a shift in each direction, covers every flat connection.) Proof: 1 >= R_T(alpha) >= exp(- beta A alpha^2/(2 R_1 T)) by 3.3 and 3.4 (b), and (c). QED

**Corollary 5.2 (SU(2): a limit law of the plate flux; PROVED).** P_T(j) converges for every j, to a probability law P_inf with (1/3) sum_j P_inf(j) j (j + 1) <= beta A/(4 R_1), and R_inf(h) = sum_j P_inf(j) chi_j(h)/d_j. P_inf(j) = 0 for half-integer j. Proof: P_T(j) = d_j integral dh chi_j(h) R_T(h), so abs(P_T(j) - P_inf(j)) <= d_j C q^T by (c). Tightness is 3.4 (a). For half-integer j see 3.6 (c): the centre shift is a symmetry of T_v, Omega is even under it, so R_inf(-h) = R_inf(h). QED

**OPEN, with an argument (ARGUED).** P_inf(0) < 1 for SU(2), that is, the vacuum wave functional is not constant on the flat connections. At small beta the first term of the character expansion that depends on h is a tube of 3 R_1 plaquettes of spin 1/2 that joins two neighbouring pinned cycles of the top plate one layer down. Its two ends see the same holonomy with opposite orientations, so it carries (tr h)^2 = chi_0(h) + chi_1(h) in place of 4. Each such tube has weight u^(3 R_1) (tr h)^2 against the vacuum term, u = I_2(beta)/I_1(beta), and there are 2 A of them. This gives - log R_inf(h) = 2 A u^(3 R_1) (4 - (tr h)^2) (1 + o(1)) as beta tends to 0, and the same leading term for R_T at every T at least 4. For U(1) the same tube carries e^(i alpha) e^(-i alpha) = 1, in agreement with Corollary 5.1. I did not write the remainder bound of the expansion, so this is not PROVED. At weak coupling and small R_1 the same statement is the one-loop potential of the holonomy (the Debye mass of the component along the short cycle). Consequence, with the same status: for SU(2) no bound R_T(h_phi) >= exp(- C beta A phi^2/(R_1 T)) holds with C independent of T. So the periodic form of the start bound (S1') of row 1195 is false in the direction of the thickness. The lane's cells are boxes with every face pinned; a constant normal potential between two pinned faces is a pure gauge there, so (S1') itself is not touched.

### 3.6 Proposition 6 (two plates: two rigid groups, double positivity, no common frame; PROVED)

Let L_k act on a slice field by multiplying every bottom vertical link (x, 0; 0) on the left by k, and R_k as in 3.3. Write Z_T(h_b, h_t) for toron pins on both plates, v_j = integral dh chi_j(h) u_(omega^h), and m_jk(T) for the coefficient of chi_j(h_b) chi_k(h_t).

(a) Z_T(h_b, h_t) = Tr(T_x^(R_1) L_(h_b) R_(h_t)), up to the choice of h or h^(-1) in the definitions, and it is a class function of each argument separately. L and R commute with each other and with T_x.

(b) Double positivity. m_jk(T) = <v_j, T_v^(T-2) v_k>, so for every finite set of spins the matrix (m_jk(T)) is positive semi-definite and is a moment sequence in T. Also m_jk(T) = Tr of T_x^(R_1) on the multiplicity space of the sector (j, k), so every entry is non-negative.

(c) Centre. On the range of P, L_(-1) = R_(-1). So m_jk = 0 unless j - k is an integer. The half-integer spins are the sectors with odd electric flux of the box in direction 1; the integer spins lie in the same sector of T_v as the vacuum.

(d) Rank one at the rate of the gap. m_jk(T) = lambda_0^(T-2) ( a_j a_k + O(q^(T-2)) ), with a_j = <Omega, v_j> at least 0 and a_0 > 0. So the law of the pair of plate fluxes factorizes in the limit, P_T(j, k) -> P_inf(j) P_inf(k), and the neutral gap of the box bounds the rate. In the other direction, an eigenfunction of T_v that does not vanish identically on the torons omega^h is seen at its own rate in some m_jj(T), as in 3.5 (d).

(e) No common frame. The mixed second derivative of log Z_T(h_(phi_b), h_(phi_t)) at phi_b = phi_t = 0 is zero for SU(2). For compact U(1), Z_T(alpha_b, alpha_t) = Z_T(alpha_t - alpha_b), and the mixed second derivative is sum_n n^2 m_n/Z_T(0) > 0.

(f) Gauss law. For s = 1, ..., T let Gamma_s(k) be the gauge transformation of the slice that is k on the sites of height at least s and 1 below. On the range of P, Gamma_s(k) = R_(k^(-1)) for every s. In generators: the rigid charge of the top plate equals the flux through the layer of vertical links below height s plus the colour charge of the free links above it. For U(1) the second term is zero.

Proof. (a) is 3.3 steps 2 and 3, applied also to the bottom plate; the two actions touch different links. The class property is Lemma 1 with g constant on one plate. (b) u_(omega^h) is a class function of h with values in the gauge-invariant functions, because u_omega(Sigma) depends on the pair (Sigma, omega) only up to a common gauge transformation and is gauge invariant in Sigma. So u_(omega^h) = sum_j chi_j(h) v_j, and 3.5 (a) gives the first formula. The second is the isotypic decomposition of (a). The coefficients of a double character expansion are unique. (c) The gauge transformation by -1 on the slice sites of heights 1, ..., T - 1 lies in the group of 3.3 step 1. It multiplies the bottom and the top vertical links by -1 and no other link. (d) 3.5 (b); a_0 > 0 because v_0 is the Haar mean of strictly positive functions; a_j a_0 is a limit of non-negative numbers. (e) By (a), Z_T is even in phi_b and in phi_t separately. For U(1), shift every direction-1 link, pinned or free, by the same angle - alpha_b/R_1 (spread form): no plaquette changes. (f) Gamma_s(k) is a transformation of the group of 3.3 step 1 followed by k on the top sites alone, which is rho_k. QED

**Reading.** (i) The toron family of a plate resolves the centre-neutral sector of the box into colour-flux channels j = 0, 1, 2, ...; in U(1) each flux is its own sector of a continuous symmetry and nothing of this kind exists. (ii) By (d), the neutral gap of the box is the rate at which the fluxes of the two plates decorrelate; in the crossed channel this is the breaking of the integer-spin flux tube between the plates: m_jk m_00/(m_j0 m_0k) -> 1. (iii) By (e), this decorrelation is invisible to every second-order (stiffness) response: the first connected response between the plates is of fourth order, a covariance of two Casimirs. This is the theorem-grade form, in this setting, of "twist tools read one factor" (Lemma FAC of row 1025; row 1134 2c). (iv) By (f), the bracket enters the crossed channel in one place: flux need not cross the slab, it can end on the colour charge of the field.

### 3.7 Where the item stops (ARGUED)

1. **The plate has the Ward identity of the two-dimensional engine, but only a three-dimensional shell sum.** Lemma 1 (c), differentiated twice, fixes the variance of the plate current of every gradient profile to its direct term, for every thickness and every field below the plate. This is the fuel of the posted engine. A port of OpenAI's fourth-order inequality to the plate layer would lower the bound of 3.4 (a) by a sum over plate momenta of abs(k)^(-2)/abs(Lambda), which is bounded: the plate is three-dimensional. I did not port it. Its gain would be a constant, not a logarithm.
2. **The logarithm needs four-dimensional shells, and the interior has no fuel.** In the interior every exact symmetry is a gauge transformation, its current is zero (3.6 (f) says the same in the crossed channel: there is one rigid charge per plate and none in between). The thickness law, stiffness = mean over the slice A below the plate of the layer stiffness minus the variance of the conditional mean current, puts the factor 1/T of 3.4 (b) into the variance term. A lower bound on that variance is the cancellation of the seagull term, (HM) of row 1195.
3. **No closure.** Conditioning on an interior slice gives rough pins with stabiliser Z_2. The trivially pinned slab is not closed under any conditioning that I know. This is (R-b) of row 1016 6.2. Reflection positivity relates Z_T(omega, omega) to Z_T(omega_b, omega_t) but gives upper bounds on mixed pins only.
4. **The neutral half.** 3.5 (d) and 3.6 (d) restate the neutral gap in plate language. They give no handle: by 3.6 (e) the plates share no frame, so the gap is a fourth-order neutral correlation, as on tori.

### 3.8 Lemma 3 (stiffness as direct term minus variance; the thickness law; PROVED; elementary)

Use the spread toron with eta = h_(phi/R_1) and c_x as in the proof of 3.4 (a). Put J = (beta/(4 R_1)) sum_x tr(i sigma_3 c_x) and D = (beta/(8 R_1^2)) sum_x E[tr c_x], with E the trivially pinned law. Then E J = 0 and

  - (d^2/d phi^2) log R_T(h_phi) at phi = 0 equals D - Var(J) = (1/3) sum_j P_T(j) j (j + 1).

Let A be the field of all free links except the top layer of vertical links. Given A, the top vertical links g_x = U_0(x, T-1) have the density proportional to the product over x and i = 1, 2, 3 of w(g_x^(-1) A_i(x) g_(x + e_i)), an O(4) layer in the one-sided background A (Lemma EMB of row 1011). By the law of total variance,

  D - Var(J) = E[ D(A) - Var(J given A) ] - Var( E[J given A] ),   D(A) = (beta/(8 R_1^2)) sum_x E[tr c_x given A].

Proof. tr(c eta^(-1)) = tr(c) cos(phi/(2 R_1)) - tr(i sigma_3 c) sin(phi/(2 R_1)). Differentiate log E[exp((beta/2) sum_x (tr(c_x eta^(-1)) - tr c_x))] twice at phi = 0. E tr(i sigma_3 c_x) = 0 by the rigid rotation of 3.3 step 2. The second line is the definition of conditional variance. The equality with the mean Casimir is 3.3. QED

For compact U(1) at the Gaussian level the first term is beta A/R_1 at every thickness, and the second term is beta A (T - 1)/(R_1 T): the conditional mean current is beta times the zero mode of the slice below the plate, a bridge between the two plates. The factor 1/T of 3.4 (b) is the difference. So a bound of the right order in the thickness is a lower bound on the variance of the conditional mean current. This is where (HM) of row 1195 sits in this setting (GUIDE for the Gaussian values; the identity is PROVED).

## 4. Verdict

### 4.1 What this row holds

The mass gap is NOT proved. Nothing on the path of (N-phys) moved. The statements below are about one side object, the slab between two trivially pinned plates. None is selective as an inequality in the direction that the wall needs.

| Statement | Label | On file before? |
|---|---|---|
| Lemma 1: pins up to gauge; the plate Ward identity in integrated form | PROVED | yes: Lemma TWIST (row 1013), Lemma REM (row 1016) |
| Lemma 2: crossed transfer operator of the pinned slab; Z_T(omega^h) = sum_j m_j chi_j(h), every m_j > 0; R_T(h) < 1 for h not 1; stiffness = one third of the mean Casimir of the plate flux | PROVED | not found. Nearest: Identity HAM1 (row 1016), no plates, twist in time |
| Proposition 4 (a): R_T(h_phi) >= exp(- beta A phi^2/(8 R_1)) for every T | PROVED | yes in substance: Lemma JEN (row 1013) |
| Proposition 4 (b): compact U(1), R_T(alpha) >= exp(- beta A alpha^2/(2 R_1 T)) | PROVED | yes: row 1011 3.2, in this geometry |
| Proposition 5: R_T(h) -> Omega(omega^h)/Omega(1) at the rate of the gap of the box; the gap of the box is the worst rate over pins | PROVED, standard | not found in plate form; the trace forms are the lane's (rows 697-720, 1161) |
| Corollary 5.1: for compact U(1) at every beta the vacuum takes the same value at every toron | PROVED | not found |
| Corollary 5.2: for SU(2) the plate flux has a limit law P_inf, carried by integer spins, with mean Casimir at most 3 beta A/(4 R_1) | PROVED | not found |
| P_inf(0) < 1 for SU(2); no thickness-uniform start bound in the periodic slab | ARGUED (leading strong-coupling term; no remainder bound); OPEN | not found; (S1') of row 1195 for boxes is not touched |
| Proposition 6 (a)-(d): two rigid groups; the matrix m_jk(T) is positive semi-definite, a moment sequence in T, and entrywise non-negative; rank one at the rate of the gap | PROVED | not found in this form; the double positivity of twisted traces on tori is the lane's (rows 731, 1157, 1161) |
| Proposition 6 (e): the mixed second response of two plates is zero for SU(2) and positive for U(1) | PROVED | in substance: Lemma FAC (row 1025), row 1134 2c |
| Proposition 6 (f): the plate charge is the flux through any layer plus the colour charge above it | PROVED | not found; the Gauss law is in rows 1016 (HAM), 1161 |
| Lemma 3: stiffness = D - Var(J); the thickness law | PROVED | the structure is OpenAI's, as read in row 1009; for sheets, rows 1096-1123 |
| 3.7: the plate has the fuel of the two-dimensional engine with a three-dimensional shell sum; the interior has none | ARGUED | in other words: Lemma WN (row 1013), (R-b) of row 1016 |

### 4.2 What it says about the wall (ARGUED)

1. The posted two-dimensional engine needs a Ward identity that fixes a current variance at every scale. In a gauge theory that identity exists only at a trivially pinned plate (3.2 (c), 3.7.1). In the interior the current of every exact symmetry is zero.
2. A plate has its rigid group, but two plates share no frame (3.6 (e)). So every second-order response is a statement about one plate. The gap of the box is the rate at which the fluxes of two plates decorrelate (3.6 (d)), a fourth-order neutral quantity.
3. The non-abelian structure enters the crossed channel through one identity, 3.6 (f): integer flux can end on the colour charge of the field. This is why the toron family of SU(2) probes the neutral sector (3.6 (c)) and why the vacuum of SU(2) should see torons while that of U(1) does not (3.5). It gives no inequality toward a gap: a Coulomb phase with charged matter would have the same property (ARGUED).
4. So this row ends where rows 1188 to 1201 ended: no mechanism for the neutral half, and no selective inequality at order-one response.

### 4.3 Conditions of the run

- No numeric run. No subagent. No outside search or download. Sources: files of this checkout only, as listed in Section 1 and at each citation.
- I did not open the Sussman-Alpoge repository in this session. Their positive projected transfer and trace identity (GL8) and Balaban's renormalization group stand behind rows 697 to 1179, on which Section 1 relies; I used them only through those rows.
- Credit. OpenAI's authors, and Jian Ding, Fenglin Huang and Pu Yang, for the two-dimensional proofs (as read in rows 1007 and 1009; I did not open the preprints). Tadeusz Balaban; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; Sourav Chatterjee: for the work behind the lane's reduction. Recalled, not rebuilt here: the construction of the lattice transfer operator (Osterwalder and Seiler; Luscher), Jentzsch's theorem, the Peter-Weyl theorem, 't Hooft's flux sectors. The lane's rows are credited where cited.
- Every proof in Section 3 was written by hand and re-read once by its author. Checked by no one.

### 4.4 Open after this row

(N-phys); the continuum datum; (BS); (W); a selective inequality at order-one response; P_inf(0) < 1 for SU(2) with a remainder bound; a port of the fourth-order inequality to the plate layer (it would give a bounded gain; no consumer); (HM) of row 1195; the Jaffe-Witten mass gap.

RESULT: Row 1202 (Claude Fable 5.2 max, Mac mini worker 3, 2026-11-20 02:41Z to 03:35Z, plain brief; author only, checked by no one; no numeric run, no subagent, no outside source). The mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; (N-phys), the continuum datum, (BS), (W) stay OPEN. A twelfth pass from the target found the lane's map again (Section 2), so no route family was screened; one side object was worked exactly, the slab between two trivially pinned plates with a periodic cross-section, which is where pure SU(2) has a rigid non-abelian group together with a response on the gauge-invariant algebra. PROVED by hand, unchecked, not selective toward the gap: the crossed transfer operator and the flux-sector expansion Z_T(omega^h) = sum_j m_j chi_j(h) with every m_j > 0, so the toron stiffness is one third of the mean Casimir of the plate flux (Lemma 2); the thick-slab limit R_T(h) -> Omega(omega^h)/Omega(1) at the rate of the gap of the box, and the gap as the worst rate over pins (Proposition 5); for compact U(1) at every coupling the vacuum takes the same value at every toron (Corollary 5.1); for SU(2) a limit law of the plate flux on integer spins (Corollary 5.2); two rigid groups, a flux matrix m_jk(T) that is positive semi-definite, a moment sequence in the thickness and entrywise non-negative, rank one at the rate of the gap, zero mixed second response of the two plates for SU(2) against a positive one for U(1), and the Gauss-law identity plate charge = flux through a layer + colour charge above it (Proposition 6); the thickness law (Lemma 3). Found again: Lemma 1 and Proposition 4 (rows 1011, 1013, 1016). ARGUED: P_inf(0) < 1 for SU(2) (leading strong-coupling term 2 A u^(3 R_1) (4 - (tr h)^2), no remainder bound), hence no thickness-uniform start bound in the periodic slab ((S1') of row 1195 for boxes is not touched); the plate carries the Ward identity of the two-dimensional engine with a three-dimensional shell sum (a bounded gain), and the interior carries none. First failing steps: (HM) of row 1195 across the thickness; no class of pins closed under conditioning ((R-b) of row 1016); the neutral half is a fourth-order correlation between plates. OPEN: (N-phys), the continuum datum, (BS), (W), a selective inequality at order-one response. Output library/gap-mini-solve-l-fable.md.
