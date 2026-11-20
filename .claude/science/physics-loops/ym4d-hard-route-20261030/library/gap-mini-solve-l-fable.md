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
