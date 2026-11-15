lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-16T05:30Z

# Row 1009: gap-o4-pinned-cell-read-opus — primary reading of the pinned-cell mechanism

Queue row 1009 of `FINISH.md` (line 1090 at pin 4290262a5). Reading only: no attack, no new claim.
Sources are OpenAI's posted preprints (author line "OpenAI"); everything restated from them is credited to OpenAI.
Marks: READ (page) = I read that page of the PDF in this run; ANCHOR = lane file and line I printed; NOT READ.

## 0. Status log (times from `date -u`)

- 2026-11-15 17:30Z: file created, plan written.

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

## Step 1. What row 1007 already settled (do not redo); the tests (2026-11-15 17:33Z)

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

## Step 2. Sources fetched (2026-11-15 17:36Z)

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
