# Check of library/gap-cf-astra.md (FINISH row 788), by Claude Opus 5.5, line by line

- Checker: Claude Opus 5.5, one session, no subagents, 2026-11-12. Cross-provider check of a Codex gpt-6-astra max note.
- Clone read: `/Users/jonreilly/ym4d-lead/clone`, branch `claude/ym4d-hard-route`, HEAD `31f93f865`. The note entered at commit `8e2dbd4b3` ("docs(ym4d): Codex lane output, gap-cf-astra").
- File checked (read in full, 580 lines): `.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-cf-astra.md`.
- Inputs read: `gap-vortex-astra.md` in full (row 778); `gap-vortex-check-opus.md` in full (row 780); `gap-kappa-order.md` lines 95-135 (Q_8 counts).
- Row label: the note calls itself FINISH row 783 (line 49). The header uses row 788 as requested. Its source pin is `cbfbf26f0`; its last line says "local and uncommitted", but the file is now committed at `8e2dbd4b3`.
- Method: by hand. No numerical run. Section 1.1 ((17)-(18), Cao, Adhikari-Cao, Vecsernyes, Borgs) is outside the brief and NOT CHECKED against the primary texts.

## 1. Sections 1.2-1.3: limits (20), incidence count (21), extension, bound (22)

**(19), reused.** I re-derived the counts. Let v_mu be the image of g_mu in Q_8/{±1} = F_2^2. Then [g_mu,g_nu] = (-1)^{omega(v_mu,v_nu)}, and the Gram matrix is a∧b for the two coordinate rows a, b in F_2^4. a∧b = 0 iff a, b are dependent: 31 pairs with a or b zero, plus 15 with a = b ≠ 0, total 46. A nonzero decomposable k is a∧b for the 6 ordered bases of one 2-plane (35 planes; 46 + 210 = 256). Each image quadruple has 2^4 = 16 lifts. So N_0 = 46·16 = 736 and N_k = 6·16 = 96 for rank 2. A rank-4 form is not of the form a∧b, so N_k = 0. HOLDS.

**Flat count.** Fix a spanning tree and the root. Each configuration is the image of a unique pair (gauge transformation with g_root = 1, tree-gauged configuration). The based gauge group acts freely: a stabilizer is fixed by its root value through transport. So the number of twisted flat assignments is 8^(V-1) times the number of based classes. Based classes of twisted flat connections correspond bijectively to holonomy quadruples with [g_mu,g_nu] = (-1)^(k_mu nu). Surjectivity: put g_mu on the links that cross x_mu = 0; the only nontrivial plaquettes are the corner stack, with value [g_mu,g_nu], a representative of k. A change of representative is a link-sign bijection. HOLDS.

**(20).** As beta -> infinity at fixed size, e^(-6 beta V) Z^k -> 8^(-4V) 8^(V-1) N_k, since tr g/2 < 1 for g ≠ 1 and the sum is finite. Hence Z^(v_34)/Z^0 -> 96/736 = 3/23, and Z^(k*)/Z^(v_34) -> 0 because N_(k*) = 0 while the denominator limit is positive. k* = v_12 + v_34 has Pf = 1, so rank 4. HOLDS. The note correctly says these are fixed-size limits.

**Bad plaquettes on S_y.** Suppose every plaquette of the six coordinate 2-tori through y is good, so U_p = eta_p is central there. Cut T_(mu nu)(y) to its fundamental rectangle. The non-abelian Stokes product of conjugated plaquette holonomies equals the boundary word. Central curvatures make the transports irrelevant, so the product is the product of eta over the torus, which is (-1)^(k_mu nu) for any closed representative of k. The boundary word of the cut torus is the commutator of the mu- and nu-circle holonomies based at y. So the four circle holonomies have commutator matrix k*. This contradicts N_(k*) = 0. HOLDS.

**Incidence count.** A plaquette p of orientation mu nu lies in S_y only through T_(mu nu)(y). That happens iff y agrees with p in the two complementary coordinates. The two free coordinates give exactly n_mu n_nu vertices. With n = (a,a,c,d) and c, d >= a, every product of two sides is at most cd. Summing over the V_lat = a²cd vertices gives a²cd <= Σ_(p bad) n_mu n_nu <= cd·#bad, so #bad >= a². (21) HOLDS.

**Q_8 action cost.** For g ≠ 1 in Q_8, tr g/2 is 0 or -1. So 1 - tr(eta_p U_p)/2 >= 1 on each bad plaquette, and the deficit is >= a². HOLDS.

**Extension to finite subgroups of SU(2) containing -1.** [A,B] = -1 means AB = -BA. Write A = a_0 + a⃗ and B = b_0 + b⃗. Then AB + BA = 2(a_0 b_0 - a⃗·b⃗) + 2(a_0 b⃗ + b_0 a⃗) = 0. If a_0 ≠ 0, then b⃗ = -(b_0/a_0)a⃗, and the scalar equation gives b_0(a_0² + |a⃗|²) = 0. So b_0 = 0 and B = 0, which is impossible. Hence a_0 = b_0 = 0 and a⃗ ⊥ b⃗. The centralizer of a pure unit quaternion â is {cos t + sin t â}. Two such circles on orthogonal axes meet in {±1}. For k*, g_3 and g_4 commute with g_1 and g_2, so they lie in {±1} and commute, contrary to [g_3,g_4] = -1. HOLDS. The argument is written for k* only. That is all (21) needs. A general rank-4 form reduces to k* by GL(4,Z) -> GL(4,F_2) surjectivity, but the note does not need this. The SU(2) result also holds: the same counting gives a² bad plaquettes in SU(2), but Delta_SU(2) = 0. Delta_G > 0 for finite G since tr g/2 = 1 only at g = 1. HOLDS.

**(22).** A periodic 4-torus with sides >= 3 has 4V links and 6V plaquettes. Each assignment has counting-Haar mass 8^(-4V). Numerator: Z^(k*) <= e^(6 beta V - beta a²), since the masses sum to one. Denominator: Z^(v_34) >= 8^(-4V)·8^(V-1)·96·e^(6 beta V), keeping only flat assignments. The ratio is 8^(4V)/(8^(V-1)·96)·e^(-beta a²) = 8^(3V+1)/96·e^(-beta a²). (22) HOLDS. It grows at fixed beta because V ~ a^4. HOLDS.

**Frame-1 reading.** With time 1 and spatial 2, m = v_34 is spatial, and (m, m+v_12) = (v_34, k*). HOLDS. *Precision:* "would directly refute (V)" means the Q_8 analogue of (V). In absolute-log form, |log Z^(k*)/Z^(v_34)| <= 2D, so a bound C a^p e^(-tau a²) on that ratio forces D >= (tau a² - log(C a^p))/2 -> infinity. With this reading it HOLDS.

Verdict for item 1: HOLDS. One precision: the refutation in the frame-1 sentence concerns the Q_8 analogue of (V).

## 2. Section 2: (23), (24), the contradiction (25), the identity (26)

**Setup.** Row 778 Section 5 selects the outgoing direction-1 and direction-2 links at the bases (4j,4l,0,0). Take time r = 3 and spatial i = 4. Then (0, v_34) is an actual pair (m, m+v_ri) with m = 0. HOLDS.

**Representative Σ.** Σ = {p_34(x): x_3 = x_4 = 0} has one plaquette for each (x_1,x_2), so |Σ| = n_1 n_2 = a². It is closed: a cube of directions (3,4,rho) at x_3 = x_4 = 0 has its two 34-faces in Σ; cubes of other directions have no face in Σ. It meets each 34-torus T_34(y) once and no torus of another orientation. So it represents v_34. HOLDS.

**No plaquette of Σ meets a selected link.** A 34-plaquette has only direction-3 and direction-4 links. Every selected link has direction 1 or 2. HOLDS. So H(ξ) is a function of the unselected links alone. HOLDS.

**(23).** Row 778's (15) splits the weight into C_k(ξ) (plaquettes meeting no selected link) and f_(k,x) (plaquettes meeting pair x). The twist on Σ changes only factors in C_k. So f_(v_34,x) = f_(0,x) and z_(v_34,x) = z_(0,x). For the weight exp(beta tr(eta_p U_p)/2) with eta_p = -1 on Σ, each changed factor has ratio exp(-beta tr U_p/2)/exp(beta tr U_p/2) = exp(-2 beta·tr U_p/2). The product over Σ is e^(-2 beta H(ξ)). The sign and the factor 2 HOLD. The normalized conditional laws f/z are equal, so all commutator laws and their product density are equal. HOLDS.

**(24).** At the identity exterior every U_p = 1 and H = a². H is continuous on the compact product of SU(2) copies, so {H > a²/2} is open, contains the identity exterior, and has positive product-Haar measure. On it e^(-2 beta H) < e^(-beta a²). HOLDS. (The remark that the Wilson weights are positive is true everywhere and adds nothing.)

**(25).** A fiberwise (CF) gives, for each ξ, B_k(ξ) = lambda(ξ)·∫F_ξ(±g) w_(ξ,N)(g) dg. B_0(ξ) > 0 forces lambda(ξ) > 0 and a finite nonzero integral. Then (13) gives |B_(v_34)(ξ)/B_0(ξ) - 1| <= eps_N on every such fiber. HOLDS.

**Contradiction.** eps_N = 8 delta^(-4) s^(N-2) with delta = e^(-24 beta_+) fixed on I, and N >= c a², so eps_N -> 0 uniformly on I. On the open set the left side of (25) exceeds 1 - e^(-beta_- a²). For large a these are incompatible on a set of positive measure. So an almost-everywhere version fails too. HOLDS.

**Scope paragraph.** HOLDS, with one precision. The fiber masses B_k(ξ) depend on the chosen representative of v_34, so the refuted implementation fixes Σ as well as the selection. I checked that this costs nothing for sign changes on selected links. U_e -> -U_e preserves Haar measure, so z_(k,x) is unchanged. It sends A to ±A, and [-A,B] = [A,B], so the commutator laws are unchanged. Sign changes on unselected links act on ξ itself. They are fiber-mixing maps, which the note already leaves open. *Precision:* "this one fixed selection" should read "this fixed selection and the representative Σ, up to sign changes on selected links".

**(26).** Z^k = ∫B_k dξ by (15), and B_(v_34) = e^(-2 beta H) B_0. Dividing by Z^0 gives (26). HOLDS. The remarks that follow are correct: each conditional commutator density integrates to one, so it cannot estimate this exterior expectation.

Verdict for item 2: HOLDS, with the precision on the representative.

## 3. Section 3: the converse (27)-(29)

**R, q, d.** q/(1-q) = ((1-R)/2)/((1+R)/2) = (1-R)/(1+R) = d. HOLDS. Row 778's (1) gives q in [0,1/2), so 0 < R <= 1. HOLDS. Row 778's (2) gives 2q <= 2Q <= D. HOLDS. If D <= 1 then q <= 1/2, so d = q/(1-q) <= (D/2)/(1/2) = D. HOLDS.

**w_N inside (12).** Take nu_j = mu for every j. Then delta mu <= nu_j <= delta^(-1) mu for any delta <= 1, and row 778's proof of (12) applies verbatim. So w_N obeys (12) with the same delta = e^(-24 beta_+) and the same eps_N. HOLDS.

**(28).** |tr g/2| <= 1 and tr(-g) = -tr g on SU(2). HOLDS. For a representation rho, ∫rho d(mu*nu) = (∫rho dmu)(∫rho dnu). Row 778's (6) gives ∫rho dmu = I/4 for the fundamental (d = 2). So ∫rho w_N dg = 4^(-N) I, and half the trace is 4^(-N). HOLDS.

**Choice of N.** With x = sigma a²/(2 log 4), N = floor(x) >= x/2 once x >= 1, and N >= 2 once x >= 2. HOLDS for large a. u_N = 4^(-N) >= 4^(-x) = e^(-sigma a²/2). HOLDS. e^(-sigma a²/2) >= C a^p e^(-sigma a²) iff e^(sigma a²/2) >= C a^p, true for large a. HOLDS. For large a, D <= 1 by (27), so d <= D <= C a^p e^(-sigma a²) <= u_N. So t = d/u_N is in [0,1]. HOLDS. N >= c a² with c = sigma/(4 log 4), independent of the frame, the pair and beta in I. HOLDS.

**F >= 0.** F = 1 + t h with |h| <= 1 and 0 <= t <= 1. HOLDS.

**(29).** lambda ∫F w_N = lambda(1 + t u_N) = lambda(1 + d) = Z^m. HOLDS. lambda ∫F(-g) w_N = lambda(1 - t u_N) = Z^m (1-d)/(1+d). With 1 - d = 2R/(1+R) and 1 + d = 2/(1+R), the quotient is R. So the value is Z^(m+v_ri). HOLDS.

**Equivalence claim.** Row 778, checked in row 780, gives (CF) => (V) with p = 0 and sigma = c delta/2. The construction gives (V) => (CF) with c = sigma/(4 log 4). Both hold for sufficiently large a, uniformly on I. *Precision:* "equivalent, up to constants in the area exponent" holds in this large-a sense. For a fixed small a, (CF) with N = 2 needs d <= 1/16, which (V) does not give. Row 778's own implication is also stated for large a, so this matches.

**Circularity paragraph.** Correct. F uses R, and lambda uses Z^m. HOLDS.

Verdict for item 3: HOLDS.

## 4. Section 4: (30), the block argument (31), the binary icosahedral case

**Fourier coefficient.** Row 778's (6) uses only Schur's lemma and the orthogonality relation ∫rho_ij conj(rho_kl) = delta_ik delta_jl / d. Both hold for a finite group with normalized counting measure. So mu_G-hat(rho) = d_rho^(-2) I for every irreducible rho of any finite G. HOLDS. Perfectness is used only for d_rho >= 2 when rho ≠ 1: a one-dimensional rho factors through G/[G,G], which is trivial. HOLDS.

**(30).** With density w relative to the uniform probability, w(g) = Σ_rho d_rho tr(nu-hat(rho) rho(g)^(-1)), by Σ_rho d_rho chi_rho(h g^(-1)) = M delta_(h,g). With nu-hat = d^(-2L) I this gives w_L(g) = Σ_rho d_rho^(1-2L) chi_rho(g^(-1)). The trivial term is 1. With |chi_rho| <= d_rho, |w_L - 1| <= Σ_(rho≠1) d_rho^(2-2L). Each term is d_rho²·d_rho^(-2L) <= d_rho²·4^(-L), and Σ_(rho≠1) d_rho² = M - 1. (30) HOLDS.

**Block bounds.** Convolution of positive measures is monotone. So delta mu_G <= nu_j <= delta^(-1) mu_G gives delta^L mu_G^(*L) <= block <= delta^(-L) mu_G^(*L). With (M-1)4^(-L) <= 1/2 the density of mu_G^(*L) lies in [1/2, 3/2]. So the block density lies in [delta^L/2, 3 delta^(-L)/2], and the block is eta·Haar + (1-eta)·(probability) with eta = delta^L/2. HOLDS.

**Odd contraction.** z is central, so convolution commutes with g -> zg and maps odd parts to odd parts. An odd function has Haar mean zero, so the Haar part kills it and ||o * block||_inf <= (1-eta)||o||_inf. HOLDS. After the first block both v(g) and v(zg) lie in [delta^L/2, 3 delta^(-L)/2], so |v(g) - v(zg)| < 3 delta^(-L)/2. The note's 3 delta^(-L) is valid but loose by a factor 2. Later convolutions by probability measures keep the lower bound delta^L/2 and do not increase the sup norm. With floor(N/L) - 1 further full blocks, the odd part is at most 3 delta^(-L)(1 - delta^L/2)^(floor(N/L)-1). Dividing by delta^L/2 gives (31). HOLDS for every N >= L. The g -> zg substitution gives the analogue of (13). HOLDS.

**Finite-energy hypothesis.** The finite-group Wilson weight exp(beta tr(eta_p U_p)/2) has the same incidences and the same oscillation 2 beta per plaquette. Left and right multiplication by fixed group elements preserve the uniform measure. So the conditional law of (A,B) has density in [e^(-24 beta), e^(24 beta)] relative to the uniform law on G², and delta = e^(-24 beta_+) on I. HOLDS.

**SL(2,F_5).** The identification of the binary icosahedral group with SL(2,F_5) is standard. I did not read the cited Frey-Rudelius page. Isomorphism carries perfectness, and -1 is the unique central involution on both sides. Order: 24 nonzero first columns; for each, ad - bc = 1 is an affine line in the second column with 5 points. 120. HOLDS.

**Commutators.** a = diag(2,3) has det 6 = 1. Conjugation by diag(alpha, alpha^(-1)) sends u(t) to u(alpha² t) and l(t) to l(alpha^(-2) t). With alpha = 2: alpha² = 4 and alpha^(-2) = 9 = 4 in F_5. So [a,u(t)] = u(4t) u(-t) = u(3t), and [a,l(t)] = l(3t). HOLDS. Since 3 is invertible, u(s) = [a, u(3^(-1) s)]. HOLDS.

**Generation.** u(r) l(-r^(-1)) = [[0, r], [-r^(-1), 1]]; times u(r) this is [[0, r], [-r^(-1), 0]] = b(r). HOLDS. b(r) b(-1) = [[r, 0], [0, r^(-1)]]. HOLDS. Elementary row operations reduce every det-1 matrix to the identity (if gamma ≠ 0, set the corner to 1 with u, clear gamma with l, finish with u; if gamma = 0, apply l(1) first). So unipotents generate and the group is perfect. HOLDS.

**L = 4.** (120 - 1)/4^4 = 119/256 < 128/256. L = 3 would give 119/64 > 1/2. HOLDS.

**Interpretation paragraph.** HOLDS, with one precision. "A binary polyhedral subgroup has the stronger full-density mechanism too" is true for the binary icosahedral group only. The binary dihedral, tetrahedral and octahedral groups are not perfect. For them mu_G lives on [G,G], a proper subgroup, so no mu_G^(*L) has full support. *Precision:* read "a binary polyhedral subgroup" as "the binary icosahedral subgroup, the only perfect one".

Verdict for item 4: HOLDS. Two precisions: the loose constant 3 delta^(-L), and the binary icosahedral wording.

## 5. Section 5: U(1) and the limits of the finite-group test

**U(1).** All commutators equal 1 for every joint law. So commutator convolution is the identity, also on f(g) = g, which is odd under g -> -g. There is no strict odd contraction and no Haar part after convolution. ∫h d(delta_1)^(*N) = 1, not 4^(-N). HOLDS. The disclaimers (no (CF) for SU(2); the fixed-fiber refutation is not a confinement mechanism) are correct.

**Limits of the finite-group discrimination.** Q_8 has [Q_8, Q_8] = {±1}, so its commutator law lives on {±1}. It is (5/8) delta_1 + (3/8) delta_(-1): omega(v,w) = 1 exactly for nonzero distinct v, w, which is 6 of 16 pairs. On odd functions it acts by 5/8 - 3/8 = 1/4, a strict contraction. So the odd contraction alone does not separate SU(2) from Q_8. HOLDS. Section 4 extends this to full-Haar flattening for the binary icosahedral group. HOLDS. (20) is a fixed-size beta -> infinity limit and decides nothing at fixed finite beta. HOLDS. *Precision:* "the subgroups in row 780" should read "Q_8 (row 780) and, by Section 4, the binary icosahedral group". Row 780 discusses only Q_8.

**OPEN list and GUIDE.** The three routes correctly restate Sections 1.3, 2 and 3, with their labels. Route 1's missing estimate and route 3's circularity match the text. HOLDS.

Verdict for item 5: HOLDS, with the wording precision.

## 6. The RESULT line (line 580)

The RESULT line says: (CF), (V), (FQ) and order-one (F-h) stay unproved; the fixed-exterior implementation is refuted by an actual SU(2) twisted pair; density-only (CF) is equivalent to (V); and the checked primary statements do not certify a fixed-beta Q_8 obstruction. The first three clauses match Sections 2-3 and the OPEN labels. The equivalence holds for large a, up to constants. The refutation is for the fixed selection and the representative Σ. The fourth clause rests on Section 1.1, which I did not check against the primary sources. The RESULT line does not mention Section 4's binary icosahedral result. That is an omission, not a mismatch. The line MATCHES what the sections prove.

## Verdict table

| # | Statement (lines) | Verdict | Finding |
|---|---|---|---|
| 1a | (19) counts, reused (168-179) | HOLDS | 46·16 = 736, 6·16 = 96, rank 4 gives 0 |
| 1b | (20) limits (180-189) | HOLDS | Fixed size; 96/736 = 3/23; N_(k*) = 0 |
| 1c | Bad plaquette in each S_y (199-209) | HOLDS | Stokes on cut torus; central curvature |
| 1d | Incidence n_mu n_nu, at most cd; (21) (209-218) | HOLDS | Complementary coordinates fixed |
| 1e | Q_8 deficit >= a² (220-222) | HOLDS | 1 - tr/2 is 1 or 2 off the identity |
| 1f | Flat count 8^(V-1) N_k; masses 8^(-4V); (22) (224-238) | HOLDS | Based gauge group acts freely |
| 1g | Frame-1 pair (v_34, k*); "would refute (V)" (244-247) | HOLDS AFTER CORRECTION (precision) | Refers to the Q_8 analogue of (V); absolute-log form |
| 1h | Every finite subgroup of SU(2) containing -1; Delta_G (249-265) | HOLDS | Anticommuting pairs are orthogonal pure quaternions; centralizer {±1} |
| 2a | Σ represents v_34, avoids selected links (275-281) | HOLDS | |
| 2b | (23): equal laws, ratio e^(-2 beta H) (283-297) | HOLDS | Sign and factor 2 correct |
| 2c | (24) on an open set of positive measure (298-306) | HOLDS | |
| 2d | (25) and the contradiction (308-323) | HOLDS | eps_N -> 0 uniformly on I |
| 2e | Scope of the refutation (325-335) | HOLDS AFTER CORRECTION (precision) | Fixes the representative Σ too, up to selected-link sign changes |
| 2f | (26) (337-350) | HOLDS | |
| 3a | R, q, d relations (370-377) | HOLDS | d <= D needs D <= 1 |
| 3b | w_N satisfies (12) (378-380) | HOLDS | nu_j = mu |
| 3c | (28): ∫h w_N = 4^(-N) (381-388) | HOLDS | Fundamental coefficient (1/4)^N |
| 3d | Choice of N, t in [0,1] (390-399) | HOLDS | Large a; c = sigma/(4 log 4) |
| 3e | F >= 0 and (29) (400-417) | HOLDS | (1-d)/(1+d) = R |
| 3f | Equivalence with (V) (354-361, 416-426) | HOLDS AFTER CORRECTION (precision) | In the large-a sense, as row 778 states its own implication |
| 4a | mu_G-hat = d^(-2) I; d_rho >= 2 (434-443) | HOLDS | |
| 4b | (30) with (M-1) 4^(-L) (444-454) | HOLDS | |
| 4c | Block bounds and (31) (454-482) | HOLDS | 3 delta^(-L) valid but loose; 3 delta^(-L)/2 suffices |
| 4d | SL(2,F_5): order 120, [a,u(t)] = u(3t), generation, L = 4 (484-516) | HOLDS | Identification standard; source not read |
| 4e | "A binary polyhedral subgroup" has full density (518-525) | HOLDS AFTER CORRECTION (precision) | Only the binary icosahedral group is perfect |
| 5a | U(1) failure (529-539) | HOLDS | |
| 5b | Limits of the finite-group test (541-550) | HOLDS AFTER CORRECTION (precision) | Row 780 discusses Q_8 only, not several subgroups |
| 5c | OPEN list, GUIDE (552-572) | HOLDS | |
| 6 | RESULT line (580) | MATCHES | Omits the Section 4 result; equivalence in the large-a sense |
| - | Section 1.1, (17)-(18), literature imports | NOT CHECKED | Outside the brief; primary texts not read |

Checked line by line by Claude Opus 5.5. Nothing FAILS. Five precision corrections (1g, 2e, 3f, 4e, 5b) and one loose constant (4c). None changes a conclusion. Credit Codex gpt-6-astra max for the incidence bound (21), the fixed-fiber refutation (23)-(26), the converse (27)-(29) and the finite perfect group flattening (30)-(31).

RESULT: Sections 1.2-5 of gap-cf-astra.md HOLD under a hand check by Claude Opus 5.5 — (19)-(22), the fixed-fiber refutation (23)-(26), the converse (27)-(29) and the binary icosahedral flattening (30)-(31) are correct, with five precision corrections (Q_8 analogue of (V), fixed representative Σ, large-a equivalence, "binary icosahedral" for "binary polyhedral", Q_8 only in row 780) and one loose constant; nothing FAILS, Section 1.1's literature is not checked, and the RESULT line matches.
