lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-16T05:30Z

# Row 1009: gap-o4-pinned-cell-read-opus — primary reading of the pinned-cell mechanism

Queue row 1009 of `FINISH.md` (line 1090 at pin 4290262a5). Reading only: no attack, no new claim.
Sources are OpenAI's posted preprints (author line "OpenAI"); everything restated from them is credited to OpenAI.
Marks: READ (page) = I read that page of the PDF in this run; ANCHOR = lane file and line I printed; NOT READ.

## 0. Status log (times from `date -u`)

- 2026-11-15 17:30Z: file created, plan written.
- 2026-11-15T17:37Z: Steps 1-8 written; RESULT line at the end. Sections 4-8, 10 and the appendices of the O(4) paper NOT READ (see Step 8).

## 0.1 Plan (at most eight steps; one step per response)

1. Read inputs: row 1007's file `library/prior/gap-2don-proofs-read-opus.md` (do not redo), `parts/gap.md` (lead rule
   W2, Lemma PT, Proposition NP anchors). Write a summary of what row 1007 already settled.
2. Fetch both PDFs into new empty /tmp folders; dump text with PyMuPDF under `python3 -I`; record page counts.
3. Read the O(4) paper: statement of the main theorem, the mixing bound with X(b) = C e^((4 pi - eta) b), and its proof
   structure. Write per-step entries.
4. Continue the O(4) paper: where the "strict saving below 4 pi from the transverse fluctuations in the first coarse
   tile" comes from; uniformity in bond strengths up to b.
5. Read O(3) paper Section 2 (pp. 9-21), proof of Proposition 2.1; per-step entries.
6. Classify the input: K-one versus K-flow (lead rule W2); test against Lemma PT and Proposition NP.
7. 4D lattice SU(2) gauge analogue per step (THM / RECALLED / NONE); lane counterparts with file:line.
8. Answers to the row's four questions; RESULT line.

## Step 1. What row 1007 already settled (do not redo); the tests

- Row 1007 (`library/prior/gap-2don-proofs-read-opus.md`) read the O(4) paper ("[28]" there) only at pp. 1-9, 11-16, 25
  (L205-212): Theorems 1.1, Corollary 1.2, Proposition 2.2 (finite-volume criterion = lane's Corollary S2 in Delta form,
  L208), Theorem 3.1 (preliminary mixing with Xi(beta) = exp(pi beta + C sqrt((1+beta) log(2+beta))), L209), and a
  summary of the stiffness flow of Sections 3.1-3.8 (L210), which it classed as a selective (K-flow) input (L211).
  It read the O(3) paper ("[15]") only at pp. 1-9 (L197-201): Proposition 2.1 statement with X(b) = C e^((4 pi - eta) b);
  the proof (pp. 9-21) is UNREAD there (L242: "The proofs of [28] Section 3 and [15] Section 2 are unread and unchecked").
- So this row's new work: the O(4) paper in full (above all Section 3, pp. 12-25+, and the parts row 1007 skipped),
  and the O(3) paper pp. 9-21; the four questions of row 1009.
- Tests (from `parts/gap.md`): lead rule W2 at L90 (K-one = a property of the measure at one scale naming a number;
  K-flow = reads first-passage data and is carried through the band by a step; PT binds a step that reads one factor;
  NP binds one that reads the whole space only through finitely many values of D). Lemma PT = row 998
  `gap-crux-exercise3-max.md` L690-713 (as cited by row 1007 L32); Proposition NP = `gap-crux-exercise4-max.md` 5.1, 6.1
  (L342-437 per row 1007 L33).

## Step 2. Sources fetched

- (a) OpenAI, "Sharp mass bounds for the two-dimensional O(4) model", September 23, 2026, at openai/math commit
  4eaee8754 (URL of the row): 102 pp., 961,282 bytes, `/tmp/row1009-o4/paper.pdf`; text by PyMuPDF (`python3 -I`).
  Contents (p. 1): 1 Intro 2; 2 finite-volume criterion 9; **3 Preliminary mixing 12-33**; 4 linear block
  transformation 34; 5 exact RG map 38; 6 kinetic drift 56; 7 admission and terminal matching 61; 8 relative comparison
  65; 9 reference box and lower bound 77; 10 upper bound 79; 11 physical units 81; Appendices A-D 82-102.
- (b) OpenAI, "The canonical massive continuum limit of the two-dimensional O(3) model", October 4, 2026, same commit:
  122 pp., 1,036,781 bytes, `/tmp/row1009-o3/o3.pdf`. Neither committed.
- Scope decision: the row's question is the mixing bound; in (a) that is Theorem 3.1 and Section 3 (pp. 12-33), read
  in full. Sections 4-11 (the cutoff comparison, row 1010's subject for O(3)) are read by statement only and marked so.

## Step 3. O(4) paper, Section 3.0-3.3 (READ pp. 4-6, 12-15)

Credit: OpenAI. Restated, not checked.

- **Strategy, p. 5 (1.2.2), quoted:** "The first source of decay is specific to the spin geometry. Identify S3 with the
  unit quaternions. The first-order change of each bond energy under a spin rotation defines its current in that rotation
  direction. The corresponding stiffness is the second-order response of the free energy to the imposed twist. Its
  defining identity has the form 'direct quadratic cost minus current covariance.' Conditioning on the boundaries of
  smaller squares gives the same structure: the stiffness of the larger square is an average of cell stiffnesses minus a
  covariance. A lower bound on these current fluctuations therefore improves an upper bound on stiffness. No positive
  lower bound on the local stiffness is needed. Rotations about different quaternion axes do not commute. Their
  integration-by-parts identities consequently contain a term that rotates the current itself. Applying these identities
  over a range of wavelengths gives a stiffness reduction with leading term (log l)/pi when the side of a square is
  increased by a factor l. The logarithm comes from a reciprocal-square frequency sum in two dimensions. Starting from
  stiffness at most beta, one can therefore reach a small upper bound after a total logarithmic length close to pi beta."
  p. 6: small stiffness -> coarse orientations -> disagreement coupling -> decay of charged observables; then the
  (cos alpha z, sin alpha w) decomposition into two S^1 ferromagnets and Ising signs -> mixing of all local Lipschitz
  observables, "uniformly when bonds are weakened or removed. That uniformity also compares the mean bond energy on the n
  and 2n tori. Integrating the difference with respect to the coupling gives ... (1.8)".
- **Theorem 3.1 (p. 12)** as row 1007 L209. Note the quantifiers: "for every beta >= 0", "every choice 0 <= beta_e <=
  beta", "every unpinned free subgraph", constants C, c, p absolute.
- **p. 13, order of the proof:** (i) small stiffness on a suitable pinned square, "This part allows arbitrary signed
  couplings and fixed right twists"; (ii) coarse orientations -> charged decay; (iii) two conditional decompositions ->
  all observables. "Only this last part requires nonnegative untwisted couplings."
- **3.1 Local class and Ward identities (p. 13-14).** Square Q(S) = {0..S}^2, all boundary spins fixed (pinned). Bond
  quaternion t_e + s_e = q_y U_e q_x^(-1) (t_e real, s_e in Im H = R^3), U_e a fixed unit quaternion (twist); signed
  |b_e| <= b <= B; tangent boundary edges at half weight ("adjacent cell actions sum exactly"). Current and stiffness
  (3.4): X_Q(F) = S^(-1) sum_e w_e s_e . F_mu(e)(z_e); H_Q(F, G) = S^(-2) E sum_e w_e t_e F_e . G_e - Cov(X_Q(F), X_Q(G)).
  H_Q = restriction to constant 3x2 matrices. **(3.5): H_Q <= b I** (sum of |coefficients| per direction <= b S^2).
  Rotation q_x -> e^(a f_x) q_x: D_f A, D_f^2 A (3.6). **(3.7), the non-abelian input, quoted:** "For a general
  infinitesimal imaginary profile eta_x, the imaginary bond derivative is exactly D_eta s_e = t_e(eta_y - eta_x) +
  (eta_y + eta_x) x s_e." Ward identity **(3.8)**: E[X_Q(d_S eta) X_Q(F)] = S^(-2) E sum w_e t_e (d_S eta)_e . F_e +
  E X_Q(F_e x (eta_y + eta_x)) — "a contact term and a bracket term"; "For the same-axis score there is no bracket term".
- **3.2 Current moments (Lemma 3.2, p. 14-15).** Under the "local induction" log(2 + S) <= 16 B (3.9):
  ||X_Q(F)||_p <= C_p (1 + b) log(2 + S) ||F||_C1 (3.10), uniform in pins, signs, twists, side. Proof: compact
  one-axis score has sub-Gaussian exponential moment E exp(t D_f A) <= exp(b t^2 E(f)/2) (3.11) (Haar invariance + Taylor,
  uses only |w_e t_e| <= b); a transverse current is extracted on a buffered patch as the difference of a perpendicular
  score rotated by two opposite profiles f = (1/2) arcsin(h/N) — this uses the product of two different axes, i.e.
  again the non-commutativity — (3.12); Whitney summation over O(log S) dyadic scales gives (3.10).
- **3.3 Conditioning into cells (p. 15-).** Tile Q(S) by L^2 cells of side R = S/L, condition on the cell boundary
  rings omega; cell interiors independent; j(F) = E[X_Q(F) | omega] = L^(-1) sum_c E_c X_c(F). Bounds (3.13)-(3.15)
  with polynomial P(B) errors; (3.15) covariance of cell stiffness under a ring rotation u. (Continues p. 16.)

## Step 3 (cont.). O(4) paper Sections 3.3-3.5 (READ pp. 16-19)

- **(3.16), exact Hessian identity (p. 16):** rotating all rings while fixing the outer boundary,
  D_u^2 S_g = L^(-2) sum_c H_c(a d_S u, a d_S u): the ring action's Hessian is the sum of cell stiffnesses.
- **3.4 Gaussian augmentation (p. 16-17).** Hypothesis on the whole pinned cell class: **H_c <= h I with B^(-D) <= h <= B**
  (the inductive upper bound). Pick h < v <= 2B, c_0 >= B^(-D'), C_c = v I - H_c - c_0 P_a >= B^(-D') I (3.17); add
  independent Gaussian noise to the conditional current: J(F) = j(F) + L^(-1) sum_c (sqrt(C_c) n_c + a n_(0,c)) . F_c (3.18);
  then **H_Q(A, A) = v|A|^2 - Var J(A)** exactly (3.19). So "upper bound on stiffness" = "lower bound on the variance of
  the augmented current". A band-limited trigonometric family f_i = psi phi_i (frequencies |k| <= 4K) and a Gaussian
  potential theta = f . p; exact change of variables (3.20) gives a log-concave-in-p-type density e^(-V(p)); commuting
  derivatives d_i (shift theta by t u_i); the **Brascamp-Lieb / Helffer-Sjostrand type identity (3.21)**:
  E (sum_i d_i^* Y_i)^2 = E sum_ij (d_j Y_i)(d_i Y_j) + E sum_ij Y_i (d_i d_j V) Y_j.
- **3.5 band estimates (p. 17-19):** requires K/L <= B^(-J), S >= L, (3.9), B m <= K. (3.22) sampling;
  (3.24) good event rho <= B^(-n) off probability e^(-B^3); **(3.25) Hessian: d_u^2 V <= (v + B^(-N)) ||grad u||^2** on the
  good event (the sum H_c + C_c + c_0 P_a = v I is exact). **(3.28) non-abelian derivative estimate:** for F of band O(K)
  perpendicular in colour to a, F' = -a x F: E sum_i |d_i J(F) - 2 J(u_i F')|^2 <= B^(-N) ||F||^2, from the exact
  derivative (3.29) d_u j(F) = 2 j(u F') + j(r_u F') + L^(-2) sum_c H_c(a d_S u, F) — the factor 2 and the rotated current
  F' = -a x F are the bracket term of (3.7)-(3.8); the H_c term cancels against the noise drift because H_c + C_c =
  v I - c_0 P_a and F perp a (p. 19). (3.34) same-frequency Ward bound: begins p. 19.

## Step 3 (cont.). O(4) paper Sections 3.5.4-3.7.1 (READ pp. 20-23)

- **(3.35) Ward bound at one frequency (p. 20):** for eta = r xi e^(ik.z)/(i|k|), |D(d_S eta, G)| <= P(B)/|k| + B^(-N):
  the contact term of (3.8) cancels the raw defect; the bracket term costs P(B)/|k|.
- **3.6 weighted current estimate (pp. 20-22):** parameters M = B^J, K = L/B^J, L >= B^(10J), cutoff psi with
  m = ceil(B^4) (vanishing on the cell seams), chi = psi^2, I_chi >= 1 - C B^(-2) (3.36). Two step types:
  "In a long step use K_1 = L/B^(4J), K_2 = L/B^(3J). In a short step use K_1 = 8M, K_2 = 256M." The key sum (3.37):
  **T = sum over M <= |k| <= K_1 of |k|^(-2) = (1/(2 pi)) log(K_1/M) + O(1/M)**, "The coefficient is (2 pi)^(-2) x 2 pi =
  1/(2 pi)" (both signs of each frequency counted). Dyadic weights w(k) (3.38). A two-colour closing estimate
  (3.39)-(3.41) gives U_r + U_r' <= C v(v + T_w) (both perpendicular colours r, r' = -a x r, neither assumed for the other),
  and (3.42) the weighted bound W^r <= C v(v + T_w).
- **3.7 variance gain (p. 23):** "For a real constant 3 x 2 matrix A of Hilbert-Schmidt norm one, choose a unit a
  perpendicular to both its columns. **This is where the three-dimensional imaginary quaternion space is used.**"
  A' = -a x A. Directions u_i = chi phi_i / |k_i| on the main annulus. (3.43): sum E Y_i^2 = v I_chi T/2, sum
  E(d_i J(A)) Y_i = v I_chi T (the factor 2 of (3.28)), (3.44) E Y^T V'' Y <= v^2 I_chi T/2. Crossed term (3.45):
  |sum E (d_j Y_i)(d_i Y_j)| <= C[v T^2 + v(v + T_w)]... (continues p. 24).

## Step 3 (cont.). O(4) paper Sections 3.7.2-3.10.1 (READ pp. 24-27): the variance gain and the stiffness iteration

- **(3.50), the variance gain (p. 24):** with S = sum_i d_i^* Y_i, Cov(J(A), S) = v I_chi T, and Cauchy-Schwarz,
  Var J(A) >= (v I_chi T)^2 / (v^2 I_chi T/2 + C[v T^2 + v(v + T_w)]). **Long regime** (v >= h >= 1, log L <= h), (3.51):
  **Var J(A) >= 2 I_chi T - C[1 + T^2/v + T_w/v] >= (log L)/pi - C_J[log B + (log L)^2/v].** Arithmetic of the leading
  term: 2 T = (1/pi) log(K_1/M) and K_1/M = L/B^(5J), so 2T = (log L)/pi - O(J log B / pi). The 2 is the factor two of
  the bracket term (3.28); 1/(2 pi) is the 2D reciprocal-square frequency sum (3.37). **Short regime** (T, T_w of order
  one), (3.52): Var J(A) >= c_sh min(v, 1), c_sh absolute.
- **3.8 Iteration (p. 25), restated.** Start: H_1 <= b I (3.5) at the lattice scale. Long steps while h >= A log B:
  v = h + 1, c_0 = 1/2, L = ceil(e^(sqrt(h log B))); then by (3.19) and (3.51) the stiffness bound drops by
  **delta_h >= (log L)/pi - C log B >= c sqrt(h log B)**; at most C sqrt(B/log B) steps; summing log L <= pi delta_h +
  C log B gives total log side length **<= pi b + C_D sqrt(B log B)** (3.53). Short steps from h <= C log B down to
  B^(-D): v = h + delta min(h, 1), L = ceil(B^(11J)), each lowers h by c min(h, 1); O_D(log B) steps, extra log length
  O_D((log B)^2). The premise (3.9) log(2 + S) <= 16 B is verified along the way ("rather than assuming it
  retrospectively"). Output **(3.54): "uniformly over the signed/twisted/pinned class, ... a common integer side R* with
  H_(R*) <= B^(-D) I, log R* <= pi b + C_D sqrt(B log B)."**
- **What the induction reads.** The hypothesis of each step is "H_c <= h I uniformly throughout the pinned cell class"
  (p. 16, before (3.17)): a sup over ALL cells of side R, all pins (boundary spins), all signed couplings |b_e| <= b, all
  fixed right twists U_e. The output is the same sup at side L R. So the induction is closed in a class defined by
  bounds only (|b_e| <= b), not by the law of one model; this is why the result is uniform in bond strengths up to b
  (row question 1, see Step 6). The parameter B (>= b, a fixed bound) controls all error polynomials P(B).
- **3.9 Local rotations (pp. 25-27):** coarse cells of side s = R* M*, M* = ceil(B^(D + C_0)); for a fixed-axis profile
  f, the effective coarse ring action obeys D_f^2 F <= C B^(-D) (3.55) by subdividing into side-R* squares (each costs
  C M*^(-2)[B^(-D) + P(B)/M*]) — conditional variance subtraction makes the Hessian at most the sum of subcell Hessians;
  then E(D_f F)^2 <= C B^(-D) (3.56), Hellinger bound (3.57), and uniformity over compact profile families (3.58).
- **3.10 Coarse orientations (p. 27-):** Haar variables g_X at coarse vertices, interpolated ring rotations Phi(g; t);
  conditional density of g proportional to e^(-F(Phi(g) omega~)), invariant under common left multiplication per cell;
  "bad" vertex = the incident-cell action moves by more than epsilon under some variation of its own g_X; 3.10.1:
  finitely many smooth profile families (stereographic charts, Coons interpolation) so (3.58) applies.

## Step 3 (cont.). O(4) paper Sections 3.10.1-3.11.2 (READ pp. 28-30)

- **(3.59)** bad vertices with disjoint collars: Pr(E entirely bad) <= zeta^(|E|/C). **3.10.2 disagreement exploration**
  (van den Berg-Maes mechanism, re-proved for continuous spins with Haar minorization e^(-epsilon) at good vertices):
  path bound (3.60) E[q^(#good)] <= (q + zeta^(1/C))^r; connection probability <= C e^(-c distance/s).
  **(3.61):** for O with zero average under common left rotation, |E O| <= C ||O|| |A| e^(-c d_pin/s); **(3.62):** charged
  two-point decay on unpinned tori with sides >= C s. "Right twists and signed couplings are still allowed in this step;
  no association is being used yet."
- **3.11 (p. 29-):** "From now on use the untwisted zero-field ferromagnet, with 0 <= b_e <= b. This restriction is
  essential." Association covariance inequality (3.63) (Newman-type); plane-rotator Ginibre by the two-replica map;
  Ising random-cluster FKG; FKG lattice condition for the angle marginals. 3.11.2: XY split (tau^1 cos gamma, tau^2 sin
  gamma); (3.64) E[tau_i tau_j] <= C c_ij^(1/3), |Cov(gamma_i, gamma_j)| <= C c_ij^(1/3) with c_ij the XY two-point
  function; localisation by cutting sign bonds (3.65).

## Step 3 (cont.). O(4) paper Sections 3.11.3-3.12 (READ pp. 31-33); Section 3 now READ in full

- **3.11.3 O(4) decomposition (p. 31):** q_i = (cos alpha_i z_i, sin alpha_i w_i), z, w in S^1; given alpha the two circle
  sectors are independent XY models with couplings b_e cos alpha_x cos alpha_y and b_e sin alpha_x sin alpha_y; the alpha
  law is associated. Charged decay (3.62) gives (3.66) for the circle components and alpha - pi/4 (zero Haar mean); two
  localisations; **(3.67): |Cov(F, G)| <= C(1 + B + |A| + |A'| + d)^20 L_F L_G e^(-c d/s)**, uniform on unpinned tori and
  free subgraphs, "for every set of couplings 0 <= b_e <= b, including all intermediate bond weakenings".
- **3.12 (pp. 32-33).** B = max(B*, b); s(b) <= exp[pi b + C sqrt(B log B)] (3.68). Unique periodic local limit by
  cutting bonds around a square (uses (3.67) along the interpolation). Reflection positivity (site and link) and the
  transfer contraction; Corollary 1.2 from (3.67). **3.12.3, the partition-function bound:** e_t(n) = E_(t;n,n)(q_0 . q_e1);
  for 0 <= t <= b, |e_t(n) - e_t(2n)| <= C(1 + B + n)^P e^(-c n/s(b)) (3.69) by cutting the O(n) bonds of a free square
  of radius ~ n/4 in both tori ("This comparison does not invoke mixing with pinned boundary fields; every system
  encountered is an unpinned ferromagnet with some weakened or zero bonds"); **(3.70): d/dt Delta_t(n) = 8 n^2 [e_t(n) -
  e_t(2n)], Delta_0(n) = 0**; integrate over t in [0, b]. Nonnegativity: Delta(n) = 2 p(n, n) + p(n, 2n) >= 0 with
  p(n, w) = 2 log Z(n, w) - log Z(2n, w) >= 0 from the row transfer operator T_w (trace class powers).
- **Why uniformity in 0 <= b_e <= b is needed (answer to part of Q1):** (i) the stiffness induction is closed only in a
  class defined by bounds (signed couplings, twists, pins), see 3.8; (ii) (3.70) integrates the coupling from 0 to b,
  so the mixing must hold at every intermediate coupling t <= b with the SAME length s(b); (iii) bond cutting to get
  local limits and the torus comparison passes through weakened bonds. So "uniformly up to b" is not an extra; the
  proof of Delta(n) small consumes it.

## Step 4. O(4) paper: how Theorem 3.1 is consumed (READ pp. 7-8, 77-78, 81; Sections 4-8, 10 NOT READ beyond
## their statements as quoted on pp. 6-8 and 77-78)

- **The loss is subexponential in O(4), and that is why one reference box suffices.** Theorem 3.1's length is
  Xi(beta) = exp(pi beta + C sqrt((1 + beta) log(2 + beta))); the true correlation length is rho(beta)^(-1) =
  beta^(-1/2) e^(pi beta). p. 7 (1.2.4): "Equation (1.9) gives Xi(beta_K(h)) L^(-K) = exp(O_(L,H)(sqrt(K log K))). Thus the
  coarse side required by the preliminary decay bound grows subexponentially in K. The comparison (1.11), however,
  permits coarse sides growing exponentially in K." Choose log M_K = K^(3/4); Theorem 9.2 (p. 78): one reference depth
  K_0 and box M_0 with D_(K_0)(h; M_0) + C_H e^(-d_H K_0) <= 2^(-10); then Proposition 9.1 (cutoff comparison, |D_N - D_K|
  <= C_H e^(-d_H K) for (2M)^2 <= e^(c_H K)) gives D_N(h; M_0) <= 2^(-10) for every finer N, and Proposition 2.2 (box
  doubling) gives m_lat(beta_N(h)) >= log 2/(M_0 L^N). p. 78: "More generally an error o(beta) in the logarithm of the
  preliminary length can be absorbed in a subexponentially growing reference box."
- So in O(4) the preliminary length is used ONLY at one reference cutoff K_0; the leading rate pi of the stiffness flow
  (= one-loop (N-2)/(2 pi) per unit log length at N = 4, inverted: length e^(pi beta)) matches the RG drift
  b_(h+1) = b_h - (log L)/pi - ... (p. 6), so the only loss is o(beta).
- Order of choices (p. 77-78): L, then H (terminal coupling), then K_0, M_0, then every N >= K_0. "Neither the reference
  depth nor the coarse box subsequently changes."
- Note for Step 5 (not a claim): in O(3) the one-loop rate is 2 pi per unit log length (beta_N = H + (log L/2 pi) N), while
  X(b) = C e^((4 pi - eta) b) loses a factor up to 2 in the exponent; X(beta_K) L^(-K) then grows exponentially in K, not
  subexponentially, so the O(4) choice log M_K = K^(3/4) cannot be copied; how the O(3) paper closes this is row 1010's
  subject (Section 8 there), not this row's.

## Step 5. O(3) paper Section 2 (proof of Proposition 2.1). READ pp. 9-11 so far

Credit: OpenAI, "The canonical massive continuum limit of the two-dimensional O(3) model" (2026-10-04). Restated, not checked.

- **Proposition 2.1 (p. 9)**, as row 1007 L201. Quoted framing (p. 9): "The first input is a mixing estimate that is
  uniform when bonds are weakened or deleted. Its exponential scale need not be sharp. **The strict inequality in the
  exponent below is, however, essential to the later comparison of effective densities.** We adapt the pinned-cell
  argument of [28], retaining its current estimates and modifying the rotation algebra for spins on S2." Three stages
  (p. 9): "We first obtain a uniform upper bound on the response of a pinned square to slowly varying rotations. **A
  one-site estimate supplies a strict saving in the initial bound.** Finally, local rotation estimates give decay for
  centered one-site functions, and two conditional ferromagnetic decompositions extend that decay to arbitrary local
  observables."
- **2.1 (p. 10), the S^2 rotation algebra.** Pinned square Q(S), half weights on tangent bonds. Current s_e = q_x x q_y,
  E_e = (q_x . q_y) 1 - (1/2)(q_x q_y^T + q_y q_x^T) (2.4); X_Q, H_Q as in [28] (2.5)-(2.6); a^T E_e a = q_x^(perp a) .
  q_y^(perp a), |a^T E_e a| <= 1, so **H_Q <= b 1 (2.7)**. (2.8) one-axis derivatives. **(2.9), the non-abelian input,
  quoted:** "D_u s_e = E_e(u_y - u_x) + (1/2)(u_y + u_x) x s_e". Ward identity (2.10): E[X_Q(d_S u) X_Q(F)] = S^(-2) E sum
  w_e (d_S u)_e . E_e F_e + (1/2) E X_Q(F_e x (u_y + u_x)). "These are the replacements for [28, (3.4), (3.6), (3.8)]. ...
  **The factor 1/2 in Equation (2.10) determines the variance gain below.**" (In [28] the bracket term carries no 1/2 and
  the quaternion derivative (3.28) has a factor 2.) Current moments (2.12) under log(2 + S) <= 16 B (2.11), proof
  adapted (p. 11; profile f = arcsin(h/N) instead of the half angle).
- **Lemma 2.2, stiffness iteration (p. 11), quoted:** "Fix a sufficiently large D. Suppose that, on squares of side R,
  H_R <= h 1 uniformly over all boundary pins and all strengths in [0, b], where B^(-D) <= h <= B and B >= b is
  sufficiently large. The pinned-cell iteration produces a common side R* with H_(R*) <= B^(-D) 1, **log(R*/R) <= 4 pi h +
  C_D sqrt(B log B)** (2.14), provided Equation (2.11) holds throughout the iteration, including each proposed next square.
  All stiffness bounds remain uniform in the original pin and strength class." Note: the rate is 4 pi per unit of
  stiffness, against pi in [28] (3.53); the one-loop O(3) rate would be 2 pi. So the bare iteration started from h = b
  gives log R* <= 4 pi b + o(b), i.e. no saving below 4 pi; the saving must come from the initial bound (next pages).

## Step 5 (cont.). O(3) paper pp. 12-14 (READ)

- Cell conditioning (2.15)-(2.18) = [28] (3.13)-(3.16), unchanged in form; "Each cell law in this calculation still has
  the original untwisted interaction" (p. 12): the O(3) class is pins x strengths in [0, b] (no signed couplings or
  twists, unlike [28] Section 3, which allows signed couplings and right twists in the stiffness part).
- Gaussian augmentation (2.19)-(2.20) = [28] (3.17)-(3.19); change of variables (2.21) and integration-by-parts identity
  (2.22) = [28] (3.20)-(3.21); band estimates (2.23)-(2.24) = [28] 3.5.1-3.5.2.
- **(2.25), the modified non-abelian derivative estimate:** E sum_i |d_i J(F) - J(u_i F')|^2 <= B^(-N) ||F||^2, from
  d_u j(F) = j(u F') + (1/2) j(r_u F') + ...: "This replaces the coefficients 2, 1 in [28, Equation (3.29)] by 1, 1/2."
  This is the whole difference S^2 versus S^3: the rotation of the current under an infinitesimal rotation has
  coefficient 1 (S^2, so(3) acting on R^3) instead of 2 (S^3 = SU(2), left multiplication, [u, v] = 2 u x v, [28] p. 8).
- (2.26) Ward bound = [28] (3.35) ("The changed bracket coefficient affects only an absolute constant").
- Same parameters M = B^J, K = l/B^J, l >= B^(10J), m = ceil(B^4); same T = (1/(2 pi)) log(K_1/M) + O(1/M) (p. 14).

## Step 5 (cont.). O(3) paper pp. 15-17 (READ): the variance gain at rate 4 pi, and the strict saving

- **Two-colour closing (p. 15):** "Equation (2.25) supplies signal U_r rather than 2 U_r"; U_r + U_r' <= C v(v + T_w);
  weighted bound (2.27) = [28] (3.41)-(3.42).
- **Main divergence test (pp. 15-16).** Same test array; only the signal line changes: sum_i E(d_i J(A)) Y_i =
  v I_chi T/2 (against v I_chi T in [28] (3.43)). **(2.28):** Var J(A) >= (v I_chi T/2)^2 / (v^2 I_chi T/2 + C{v T^2 +
  v(v + T_w)}). Long step, **(2.29): Var J(A) >= (log l)/(4 pi) - C_J[log B + (log l)^2/v]**; short step (2.30):
  >= c_sh min(v, 1). Arithmetic: (v T/2)^2/(v^2 T/2) = T/2 = (1/(4 pi)) log(K_1/M). So the S^2 bracket coefficient 1
  (against 2 for S^3) costs a factor 4 in the gain per unit log length: (log l)/(4 pi) against (log l)/pi. Iteration
  (p. 16): v = h + 1, l = ceil(exp sqrt(h log B)), delta_h >= (log l)/(4 pi) - C log B; total log length 4 pi h +
  C_D sqrt(B log B). "At every stage the only conditioned cell laws are the original nearest-neighbor laws with new
  boundary pins, so the uniformity class is preserved."
- **Why 4 pi and not 2 pi.** The one-loop O(3) beta function gives length e^(2 pi beta) (the trajectory beta_N = H +
  (log L/2 pi) N of p. 6). The Cauchy-Schwarz lower bound (2.28) captures only half the one-loop rate for S^2; for S^3 it
  captures the full one-loop rate pi = 4 pi/(N - 2) at N = 4... (one-loop length e^(2 pi beta/(N-2)): N = 4 gives pi,
  N = 3 gives 2 pi). So [28]'s Cauchy-Schwarz is sharp at the leading rate for O(4) and loses a factor 2 for O(3). This
  is my reading of the two displayed rates, not a statement of either paper.
- **Lemma 2.3, Initial reduction (p. 17), quoted:** "There is a fixed sufficiently small u > 0 such that, for all
  sufficiently large b, the square of side S = floor(e^(2 pi b u)) satisfies H_S <= b(1 - 3u/4) 1 uniformly in all its
  boundary pins and all strengths 0 <= beta_e <= b." Lead-in: "Starting Lemma 2.2 with Equation (2.7) would give
  logarithmic length 4 pi b + o(b). The next argument saves a fixed multiple of b before the iteration begins."
  **This is the "strict saving below 4 pi from the transverse fluctuations in the first coarse tile" (p. 7).** Proof:
  1. **One-site Hessian bound (2.31):** at a site at distance >= S/b from the pinned boundary, the one-site marginal
     density e^(-F) (relative to area on S^2) obeys Hess F <= (1 + o_b(1)) u^(-1) g_(S^2), uniformly in pins, strengths,
     and the point. Proof: rotate the spin and all others about ONE axis with a radial cutoff equal to 1 within radius 2,
     0 at radius S/(2b), linear in log radius between; second derivative of -log(marginal) = expected action second
     derivative minus a variance <= b x (cutoff Dirichlet energy) by (2.8); the energy is 2 pi/log(S/(2b)) + o =
     (1 + o_b(1))/(b u). "No positive lower bound on any coupling entered this calculation." This is the classical 2D
     log-cutoff spin wave (Mermin-Wagner / McBryan-Spencer type estimate): a one-axis rotation, no commutator.
  2. **Transverse variance (2.32):** for a unit v, z = v . q, Y = grad z on S^2 (|Y|^2 = 1 - z^2, div Y = -2z,
     nabla_Y Y = -z Y); integration by parts: E(YF)^2 = E{Hess F(Y, Y) - 3 z YF}, E z YF = 1 - 3M with M = E z^2; so
     (1 - 3M)^2 <= M(a + 6), a = (1 + o_b(1))/u, which forces **M >= (7/8) u** at every interior site (u small, b large).
     I.e. every spin keeps a transverse fluctuation of order u in every direction, whatever the pins.
  3. **Contact bound:** for an interior edge, E[v^T E_e v] = E(q_x^(perp v) . q_y^(perp v)) <= sqrt((1 - E(v.q_x)^2)(1 -
     E(v.q_y)^2)) <= 1 - 7u/8; boundary strips are an O(1/b) fraction of bonds; **discard the nonpositive covariance in
     (2.6)**: H_S <= b(1 - 3u/4).
- **Arithmetic of eta (my reading, from (2.14) and Lemma 2.3):** log R* <= log S + 4 pi h_S + o(b) = 2 pi b u +
  4 pi b(1 - 3u/4) + o(b) = (4 pi - pi u) b + o(b). So eta is any number below pi u, with u the fixed small constant of
  Lemma 2.3. The saving exists because the first tile costs log length 2 pi u b and lowers the stiffness by (3/4) u b,
  worth 3 pi u b of log length at the iteration's rate 4 pi; it is a strict saving only because the iteration's rate
  (4 pi) is worse than the spin-wave rate (2 pi per unit of b on the first square). In [28] (O(4)), the iteration already
  runs at the one-loop rate pi, so no such device is needed there (loss o(beta) only).

## Step 5 (cont.). O(3) paper pp. 18-21 (READ); Section 2 now READ in full (pp. 9-21)

- **(2.33), p. 18, the paper's own arithmetic (confirms my reading above):** "Take B = b and apply Lemma 2.2 after this
  first square. The total logarithmic side is at most 2 pi b u + 4 pi b(1 - 3u/4) + C_D sqrt(b log b) = (4 pi - pi u) b +
  o(b). ... Any fixed polynomial enlargement can be absorbed by taking, for example, eta = pi u/2". Premise (2.11) holds
  since 4 pi + 1 < 16.
- **2.4 (pp. 18-19)** = [28] 3.9-3.10 with S^2: coarse cells s = R* ceil(b^(D + C_0)); D_f^2 F_ring <= C b^(-D) (2.34);
  Hellinger (2.35); uniform over compact profile families (2.36); orientation variables g_X in S^3 acting on S^2 through
  the covering rho: S^3 -> SO(3); profile construction "takes place in S3 itself"; bad vertices, disagreement exploration;
  **(2.37):** |E O(q_x) O'(q_y)| <= C ||O|| ||O'|| e^(-c d(x,y)/s) for Haar-centred one-site O ("the S2 version of [28,
  (3.62)]").
- **2.5 (pp. 19-21):** q_i = (cos alpha_i z_i, sin alpha_i w_i), z in S^1, w in {-1, 1} (one XY sector and one Ising sector
  given alpha); association of alpha; (2.38) = [28] (3.63); (2.39) = [28] (3.66); localisations as [28] 3.11; (2.2) with
  s <= X(b). Periodic limit by collar cutting; (2.3) upper bound by the common-cutout comparison of [28] 3.12.3, applied to
  horizontal and vertical bonds, "Integration of the coupling from zero to b gives the upper bound in Equation (2.3); the
  comparison is uniform at every intermediate coupling because all strengths remain in [0, b]"; lower bound from
  Tr T^(2k) <= (Tr T^k)^2 in both directions.
- Difference of the O(3) class from [28]'s: O(3) Section 2 keeps the pinned class = {pins} x {strengths in [0, b]}
  throughout (no signs, no twists: p. 12, p. 16); [28] Section 3 allows signed couplings and right twists in 3.1-3.10.

## Step 5 (end). Why the strict saving is needed in O(3) (READ p. 7-8, Section 1.4)

- Quoted (p. 7-8): "The strict saving in the preliminary length permits a reference box larger than that mixing length,
  while the nearly L^(-2) contraction keeps the error over its coarse volume small. ... More concretely, at a reference
  depth K, the preliminary mixing length in physical units is a_K X(beta_K) = L^((1 - eta/(2 pi))K + o(K)). Matching the
  effective densities to finer cutoffs is controlled by the error parameter C_H M^2 L^(-(2 - upsilon)K) in a physical
  square of side M, where upsilon > 0 can be chosen arbitrarily small. Thus M can be much larger than the mixing length
  while this error tends to zero."
- Arithmetic: beta_K = H + (log L/(2 pi)) K + O(log K), so X(beta_K) L^(-K) = L^(((4 pi - eta)/(2 pi) - 1) K + o(K)) in
  coarse cells = L^((1 - eta/(2 pi)) K) coarse cells; the comparison allows M up to L^((1 - upsilon/2) K). A window exists
  iff upsilon/2 < eta/(2 pi). With eta = 0 (the bare Lemma 2.2 rate 4 pi) the mixing length would equal the largest box
  the L^(-2) contraction can afford (contraction exactly L^(-2) per step against the volume factor M^2), and the
  argument would close only with an exact L^(-2) and no loss. So the O(3) proof needs BOTH a contraction arbitrarily
  close to L^(-2) (Section 5, "spatial inversion and tangent reflection", row 1010's subject) AND a strict saving in the
  exponent, from Lemma 2.3. In O(4) neither margin is tight: the stiffness flow runs at the one-loop rate (loss o(beta)),
  so a box of side e^(K^(3/4)) coarse cells suffices (Step 4).

## Step 6. Kind under lead rule W2; Lemma PT; Proposition NP (reading-level verdicts, unchecked)

W2 (`parts/gap.md` L90): (K-one) = a property of the measure at one scale naming a number; (K-flow) = reads first-passage
data and is carried through the band by a step. The pinned-cell proof has three parts of different kind:

1. **Start data, (K-one), blind.** (a) H_Q <= b I on every pinned square ([28] (3.5); O(3) (2.7)): a trivial bound from
   the action, true for every O(N) including N = 2. (b) O(3) only: Lemma 2.3, H_S <= b(1 - 3u/4) on the square of side
   e^(2 pi b u), uniformly in pins and strengths. Its proof uses a ONE-AXIS rotation with a log cutoff (the 2D spin-wave
   / Mermin-Wagner bound) and the S^2 identities (2.32); it uses no commutator. Its S^1 form would hold the same way
   (my reading: the one-axis estimate (2.31) and a transverse-variance bound do not need a second axis), so it is not
   selective. It names numbers (u, 3u/4). It is a property of the class at one scale.
2. **The engine, a flow, selective.** Lemma 2.2 / [28] 3.3-3.8: "H_R <= h I uniformly over all pins and strengths" at side
   R implies the same with h - delta_h at side l R, delta_h >= (log l)/pi - C log B ([28]) or (log l)/(4 pi) - C log B
   (O(3)). Carried scale by scale from the lattice scale to e^((4 pi - eta) b) (O(3)) or e^(pi b + o(b)) (O(4)), i.e.
   through the whole band from weak coupling to the correlation length. The gain is the bracket term: "For the
   same-axis score there is no bracket term" ([28] p. 14); at S^1 the gain is zero. So in SHAPE it is (K-flow): a
   statement carried through the band by a step that fails for the abelian model. It differs from W2's (K-flow) in its
   input: **it does not read first-passage data**. It runs at one fixed bare coupling b, needs no RG trajectory, and
   starts from the bare bound alone. What makes the step close is the class: the hypothesis is a SUPREMUM over every
   cell, every boundary pin and every strength field in [0, b] (in [28] also signed couplings and right twists),
   because conditioning a large square on its cell rings produces exactly such cells with arbitrary pins (3.16).
   So: **(K-flow) in shape, with a class-supremum hypothesis instead of first-passage data.** Row 1007 L211 called it a
   selective (K-flow) monotone; I agree with the shape and add this difference of input.
3. **Output, (K-one).** Mixing at length X(b) uniformly in strengths [0, b] gives, through the coupling integral (3.70)
   d/dt Delta_t(n) = 8 n^2 [e_t(n) - e_t(2n)], the number Delta(n) <= C(1 + b + n)^p e^(-c n/X(b)) at one size n: the 2D
   seed (lane: Phi small; Theorem D (b) then S(n; 2n) small; row 1007 7.2 bridge).

- **What the flow's monotone quantity is.** It is the twist stiffness H (second-order response of a pinned square's free
  energy to a slowly varying global rotation: "direct quadratic cost minus current covariance"), NOT Delta / Phi / D.
  The 2D proof never proves a contraction of Delta above a threshold (the lane's (CAS), `library/gap-mid-max.md` L64); it
  proves Delta small directly at n >= C X(b), and uses the Delta-doubling (Proposition 2.2 of [28], = Corollary S2) only
  below the threshold 2^(-10).
- **Lemma PT: passes** (reading level). For a product O(N) x (massless factor), the stiffness, the currents and the
  bracket term are those of the O(N) rotations; the other factor is invariant under them and contributes nothing to
  H or to its gain. The final mixing step (3.11 / 2.5) decomposes the S^3 or S^2 spin into circle and Ising sectors of
  that spin only; it gives no covariance bound for observables of the other factor. So it does not prove a gap for the
  product. The step reads one factor (the factor with the non-abelian global symmetry) and is selective inside it
  (zero gain at N = 2).
- **Proposition NP: passes, trivially.** The induction never reads D, Phi or any finite list of free-energy values;
  its hypothesis is a uniform bound on a twist response over a class of boundary conditions and couplings. NP binds an
  induction on the history of D; this is not one.
- **Notes for other lane filters, not verdicts.** (i) The hypothesis is a supremum over boundary pins. Theorem D2
  (`parts/gap.md` L26) binds supremum-over-TILT forms (bulk tilts) for gauge fields; the pinned-cell supremum is over
  boundary data and strengths with a fixed bound b, and it is an UPPER bound on a response, which is the direction a
  supremum over pins can keep. Whether D2 binds a gauge form of it is not tested here. (ii) Lemma SHEET (forms uniform
  over coupling fields fail as the coupling bound grows) does not bind a fixed bound b (as row 1007 L150 noted).
  (iii) Proposition V (W2's test for (K-one) inputs) is a gauge-model test; the K-one parts here are spin-model
  statements, so it was not run.

## Step 7. Per-step table: statement, inputs, where N >= 3 enters, lane counterpart, 4D SU(2) gauge analogue

Pages: [28] = O(4) paper; O3 = O(3) paper. Marks for the analogue column: THM = a theorem I can point to (lane file or
published); RECALLED = from memory, not re-read in this row; NONE = no analogue known to me. Lane anchors are in this
folder: R = `library/gap-crux-restate.md`; P = `parts/gap.md`; M = `library/gap-mid-max.md`. Marks for the step column:
READ (page) as in Steps 3-5.

| # | Step (READ page) | Inputs | Where non-abelian algebra / N >= 3 enters (quoted) | Lane counterpart | 4D lattice SU(2) gauge analogue |
|---|---|---|---|---|---|
| 1 | Pinned square Q(S), half weights on tangent bonds so cell actions add ([28] p. 13; O3 p. 10) | nearest-neighbour action, Haar | none | none (the lane works on periodic tori, R L57) | THM-level as a definition: box with fixed boundary links; Markov (DLR) property of lattice gauge fields. Half-weight boundary plaquettes: RECALLED (Balaban's block conditioning). |
| 2 | Current X_Q and stiffness H_Q = direct cost minus current covariance (3.4); O3 (2.6) | a GLOBAL rotation applied with a slowly varying profile | not yet; defined for any N | none. Nearest: the twist free energies of the flux sectors (R Theorem D (e), L98), which are discrete. | Object: RECALLED, the Schrodinger-functional coupling of Luscher, Narayanan, Weisz, Wolff (1992): the response of the free energy of a box to a boundary-induced background field, which is 1/g-bar^2(L) times the classical action. Not re-read here. A constant boundary gauge rotation is pure gauge (row 1007 B(5)); the analogue of the TWIST is a background connection, not a symmetry rotation. |
| 3 | H_Q <= b I (3.5); O3 (2.7) | drop the covariance; count bonds | none | Theorem D (f) direction: Phi is an integral of a mean action (R L99); no stiffness bound on file | NONE as a theorem known to me (an SF form "1/g-bar^2 <= the bare value times the classical action" would follow the same way by dropping a variance; not on record that I know). |
| 4 | Ward identity with bracket term (3.7)-(3.8); O3 (2.9)-(2.10) | Haar integration by parts for a profile vanishing on the pins | [28] p. 13: "the imaginary bond derivative is exactly D_eta s_e = t_e(eta_y - eta_x) + (eta_y + eta_x) x s_e"; p. 14: "For the same-axis score there is no bracket term". O3 p. 10: "(1/2)(u_y + u_x) x s_e ... The factor 1/2 ... determines the variance gain". | none | NONE. A local rotation profile of link variables is a gauge transformation: the Ward identity is exact invariance with no contact and no bracket term on gauge-invariant data. A bracket arises for the background connection in the background-field method (RECALLED), not as written here. |
| 5 | Current moments (3.10)-(3.12), Whitney summation; O3 (2.12)-(2.13) | one-axis sub-Gaussian bound (3.11); the 2D spin wave: Dirichlet energy O(1) across an annulus | the transverse-current extraction rotates a perpendicular score by two opposite profiles, i.e. uses two axes ([28] p. 14) | none | NONE: a scalar profile costs order R^2 on a 4D annulus (row 1007 A(5)). |
| 6 | Conditioning on cell rings; exact Hessian identity D_u^2 S_g = L^(-2) sum_c H_c (3.16); O3 (2.18) | Markov property; the class must contain every cell with every pin | none | Lemma E / Lemma A are torus identities (R L37); no conditioning on cell boundaries in the lane's engine | THM-level: conditioning on the links of the cell boundaries (3-skeleton) makes cell interiors independent; the block effective action of Balaban's RG is of this type (RECALLED). |
| 7 | Gaussian augmentation H_Q(A, A) = v|A|^2 - Var J(A) (3.17)-(3.19); change of variables and the identity (3.21); O3 (2.19)-(2.22) | upper bound H_c <= h I on the whole class; Gaussian noise; commuting derivatives | none (dimension-free probability) | none | THM-level as probability (a Helffer-Sjostrand/Brascamp-Lieb type integration by parts); generic, any model. |
| 8 | Band estimates; non-abelian derivative (3.28), (2.25) | sampling, good event | [28] (3.28): d_i J(F) ~ 2 J(u_i F'), F' = -a x F; O3 (2.25): "replaces the coefficients 2, 1 ... by 1, 1/2" | none | NONE. |
| 9 | Frequency sum T = (1/(2 pi)) log(K_1/M) (3.37); O3 p. 14 | 2D reciprocal-square sum | none (scalar) | none | NONE known: in 4D the scalar sum sum |k|^(-2) grows like K^2; the scale-invariant 4D sum is sum |k|^(-4), which is where the one-loop Yang-Mills logarithm sits (RECALLED, perturbation theory). No non-perturbative family with this gain is known to me. |
| 10 | Variance gain (3.50)-(3.52); O3 (2.28)-(2.30) | steps 7-9; Cauchy-Schwarz | [28] p. 23: "choose a unit a perpendicular to both its columns. This is where the three-dimensional imaginary quaternion space is used." Gain (log L)/pi ([28]) or (log l)/(4 pi) (O3) | the lane's selective step that is missing: P L33-47 ("no input excludes branch G beyond first passage"); (CAS) M L64 | NONE as a theorem. The analogue statement would be a non-perturbative monotone decrease of an SF-type coupling 1/g-bar^2(L) with scale at a rate tied to the one-loop coefficient; believed (asymptotic freedom; step-scaling numerics, RECALLED), not proved. |
| 11 | Iteration of the stiffness bound (3.53)-(3.54); O3 Lemma 2.2 (2.14) | the class-uniform hypothesis at each scale; log(2 + S) <= 16 B | through step 10 | the band between lattice scale and seed size: P L19 (W), L90 (first passage, K_j to infinity at fixed g) | NONE. |
| 12 | O3 Lemma 2.3, strict saving (2.31)-(2.33), p. 17-18 | one-axis log-cutoff spin wave; S^2 integration by parts (2.32) | none (one axis only) | a one-scale number (K-one): compare (SEED) R L59 in kind only | NONE known: the proof is a 2D log-cutoff spin wave for one site. |
| 13 | Small stiffness gives cheap local rotations (3.55)-(3.58); O3 (2.34)-(2.36) | stiffness at side R*; Hellinger; compact profile families | rotations in S^3 (O3: S^3 acting on S^2 through rho) | none | NONE. |
| 14 | Coarse orientations, bad vertices, disagreement percolation; charged decay (3.59)-(3.62); O3 (2.37) | Haar minorisation at good vertices; path counting | invariance of cell potentials under common LEFT multiplication | one-scale counting as in Theorem S's use of sizes (R L192-203) | Counting: THM-level, dimension-free. Charged observables: NONE (no global symmetry acts on gauge-invariant data; only the Z_2 centre, row 1007 B(5)). |
| 15 | Mixing for all local observables via circle/Ising decompositions, association, Ginibre (3.63)-(3.67); O3 (2.38)-(2.39) | 0 <= b_e <= b, untwisted, unpinned | none (abelian conditional systems) | none | NONE for SU(2) (row 1007 A(5), B(5)). |
| 16 | Delta(n) by coupling integration: d/dt Delta_t(n) = 8 n^2 [e_t(n) - e_t(2n)] (3.69)-(3.70); O3 p. 21 | mixing at EVERY coupling t in [0, b] with the same length | none | **Theorem D (f)**, R L99: Phi(n; beta) = 96 n^4 int_0^beta (abar_2n - abar_n) ds; and R L61. The same identity in 4D, proved in the lane. | THM (lane, Theorem D (f)) for the identity. Its input, plaquette mixing on n^4 tori at every coupling s <= beta with a length below n, is the open problem itself (for s in the band). |
| 17 | Box doubling: Delta(2n) <= 64 Delta(n)^2, Delta <= 2^(-10) gives m >= log 2/n ([28] Prop. 2.2) | reflection positivity, Lemma A | none | **Theorem S, Corollary S2** (R L192, L205), Lemma A (R L37), Theorem D (b) (R L95); row 1007 L208 | THM (lane; checked in rows 698, 699): the 4D engine exists. |
| 18 | O(4) only: one reference cutoff, cutoff comparison, RG trajectory b_(h+1) = b_h - gamma - gamma/(2 pi b_h) + r_h ([28] p. 6-8, 77-78; Sections 4-9 NOT READ) | Theorem 3.1 at the reference depth only; loss o(beta) | none in the comparison | the account's trajectory and the carry to finer cutoffs: P L19 ("along the account's trajectory"), P L21-23 ((SEED) with a carry to finer cutoffs) | RECALLED: Balaban's RG for 4D lattice YM (small-field, ultraviolet stability); the carry of a box seed to finer cutoffs is the lane's open (W) (P L19). |

Net of the table: the steps that carry the non-abelian input (4, 5, 8, 9, 10, 11, 13, 14) have no 4D gauge analogue
known to me; the steps that have one are the generic ones (1, 6, 7, the counting in 14) and the two torus identities the
lane already has (16 = Theorem D (f), 17 = Theorem S / Corollary S2). The nearest 4D object to the stiffness is the
Schrodinger-functional coupling (RECALLED), whose monotone decrease at the one-loop rate is a belief, not a theorem.

## Step 8. Answers to the row's four questions, marks, and RESULT (2026-11-15T17:37Z)

Reading only; no attack, no new claim. Everything restated is OpenAI's (author line "OpenAI"), from two posted,
unrefereed preprints at github.com/openai/math commit 4eaee8754. Nothing was checked line by line, and no other
provider has checked this reading.

**Marks.** (a) O(4) paper (102 pp.): READ pp. 1, 4-8, 12-33 (all of Section 3, the preliminary mixing), 77-78
(Proposition 9.1, Theorem 9.2), 81 (completion of Theorem 1.1); excerpts of pp. 40, 66; pp. 2-3, 9, 11-16, 25 were read
by row 1007. **NOT READ: pp. 10, 34-76 (Sections 4-8: block map, exact RG, drift, admission, density comparison), 79-80
(Section 10), 82-102 (Appendices A-D).** The row asked for (a) in full; I read in full only the part that answers its
question (Section 3) and the places where Section 3 is consumed. (b) O(3) paper: READ pp. 7-8 (Section 1.4) and pp. 9-21
in full (Section 2, Proposition 2.1 and its proof); ANCHOR p. 22 (start of Section 3).

**Q1. How is a mixing bound with X(b) = C e^((4 pi - eta) b) obtained at every coupling b, uniformly in bond strengths
up to b?** (O3 Section 2, building on [28] Section 3.) Put B = b. (i) On every pinned square, for every pin and every
strength field in [0, b]: stiffness H <= b (2.7). (ii) Lemma 2.3: on the square of side e^(2 pi b u) the bound improves to
b(1 - 3u/4). (iii) Lemma 2.2: a scale-by-scale iteration, each step conditioning a square of side l R on its cell rings and
lowering the class-uniform bound by at least (log l)/(4 pi) - C log B, through the Gaussian augmentation (2.20) and a
Cauchy-Schwarz lower bound on the augmented current variance (2.28) whose signal is the bracket term of the S^2 Ward
identity (2.10), (2.25). It reaches H <= b^(-D) at a side R* with log R* <= (4 pi - pi u) b + o(b) (2.33); eta = pi u/2
absorbs polynomial losses. (iv) Small stiffness makes local rotations cheap (2.34)-(2.36); coarse orientation variables
and disagreement percolation give decay of Haar-centred one-site functions at scale s = R* b^(D + C_0) (2.37); the
decomposition q = (cos alpha z, sin alpha w) into a conditional XY and a conditional Ising system, with association
and Ginibre, gives mixing for all local Lipschitz observables (2.2). (v) (2.3) by integrating the coupling from 0 to b
with the common-cutout comparison of bond means. **Uniformity in strengths** is built in, not added: every estimate uses
only |w_e| <= b ("No positive lower bound on any coupling entered this calculation", p. 17); the iteration's class must be
closed under conditioning on rings, which produces cells with arbitrary pins (p. 16: "the only conditioned cell laws are
the original nearest-neighbor laws with new boundary pins, so the uniformity class is preserved"); and the coupling
integral in (v) needs mixing at every intermediate strength with the same length X(b). "At every coupling b": b >= b_0
in Proposition 2.1; [28] Theorem 3.1 covers all b >= 0 by enlarging constants on [0, B*] (p. 33).

**Q2. Where does "the strict saving below 4 pi from the transverse fluctuations in the first coarse tile" come from?**
From Lemma 2.3 (O3 p. 17). On the first square, of side S = e^(2 pi b u), a one-axis rotation with a log cutoff bounds the
Hessian of every interior one-site marginal by (1 + o(1))/u (2.31) (2D spin wave); integration by parts on S^2 (2.32) then
forces the transverse variance E(v . q)^2 >= (7/8) u in every direction v, whatever the pins; so each interior bond's
contact term is at most 1 - 7u/8 and, dropping the covariance, H_S <= b(1 - 3u/4). The first tile costs log length
2 pi u b and removes (3/4) u b of stiffness, worth 3 pi u b of log length at the iteration's rate 4 pi; net saving pi u b
(2.33). It is needed because the S^2 bracket coefficient 1/2 (against the quaternion factor 2 in [28]) makes the
iteration's rate 4 pi, twice the one-loop 2 pi; with eta = 0 the preliminary length in physical units, L^((1 - eta/(2 pi))K),
would reach the largest box that the near-L^(-2) contraction allows (C_H M^2 L^(-(2 - upsilon)K)), and the cutoff
comparison would have no room (p. 8). In O(4) no saving is needed: the iteration runs at the one-loop rate pi and the loss
is o(beta) ([28] p. 7, 78). The saving itself is blind (one axis, no commutator; my reading is that it holds for S^1 too).

**Q3. One-scale (K-one) or first-passage (K-flow), in the sense of lead rule W2?** Both, in different parts (Step 6). The
start data (H <= b; Lemma 2.3) and the output (Delta(n) small at one size) are (K-one). The engine (Lemma 2.2 / [28] 3.3-3.8)
is a scale-by-scale flow carried through the whole band by a selective step (zero gain for S^1): (K-flow) in shape. It
does NOT read first-passage data: it runs at one fixed bare coupling with no RG trajectory, and closes because its
hypothesis is a supremum over every cell, boundary pin and strength field in [0, b]. Its monotone quantity is a twist
stiffness, not Delta, Phi or D; the 2D proof never proves (CAS) (M L64).

**Q4. Does it pass Lemma PT and Proposition NP?** PT: passes (reading level). The gain and the final mixing step read
only the factor with the non-abelian global symmetry; for a product with a massless factor they give nothing for that
factor and claim no gap for the product. NP: passes trivially (no history of D is read). Not run: Proposition V (the
K-one parts are spin-model statements), and whether Theorem D2 binds a gauge form of the supremum over pins.

**For the lane (evidence for the lead, not claims).** (1) The 2D route from mixing to the seed is the lane's own identity:
[28] (3.70) is Theorem D (f) (R L99) in 2D, and [28] Proposition 2.2 is Corollary S2 (R L205). (2) What the lane lacks in
4D is steps 4-5 and 8-11 of the Step 7 table: a twist with a bracket term, a log-gain frequency sum, and a class-uniform
monotone response. The nearest 4D object is the Schrodinger-functional coupling (RECALLED; Luscher-Narayanan-Weisz-Wolff
1992), whose monotone decrease at the one-loop rate is believed, not proved. (3) The pinned-cell class (all pins, all
strengths up to b) is the device that makes a scale-by-scale step close without first-passage data; for the gauge
problem, whether a class-uniform upper bound on such a response can hold is constrained by Theorem D2 and Lemma SHEET
(P L25-27). That was not tested here.

RESULT: Row 1009, reading only, checked by no one. Read OpenAI's O(4) paper Section 3 in full plus where it is used; Sections 4-8, 10 and the appendices NOT READ. Read the O(3) paper's Section 2 (pp. 9-21) in full. The mixing bound comes from a pinned-cell stiffness iteration. It is uniform over all boundary pins and all strengths in [0, b], starts from H <= b, and lowers the class bound by (log l)/pi per step for O(4) (by (log l)/(4 pi) for O(3), because the S^2 bracket coefficient is 1/2 against the quaternion factor 2). The saving below 4 pi is Lemma 2.3 (O(3) p. 17): a one-axis log-cutoff spin wave forces transverse variance >= 7u/8 on the first square of side e^(2 pi b u), so H <= b(1 - 3u/4) and eta = pi u/2. That saving is blind; the selective step is the bracket term. Kind: K-one start and output, and a selective K-flow-shaped engine that reads a class supremum, not first-passage data. It passes PT and NP at reading level. [28] (3.70) is the lane's Theorem D (f) and [28] Proposition 2.2 is Corollary S2. Open: no 4D SU(2) gauge analogue is known for the bracket-term steps (the nearest object, the Schrodinger-functional coupling, is RECALLED only). Proposition V and the Theorem D2 test of the pin supremum were not run.
