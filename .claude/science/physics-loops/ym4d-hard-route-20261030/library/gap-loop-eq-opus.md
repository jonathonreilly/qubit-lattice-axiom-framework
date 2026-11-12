# gap-loop-eq-opus: lattice loop equations at the middle scale, with positivity (FINISH row 754)

- Author: Claude Opus 5.5 (one session, alone). Date: 2026-11-12 UTC.
- **Not checked by another model.** Research note, not a public claim. **No mass gap is proved here.**
- Marks: **PROVED** (every step written), **ARGUED** (a step not closed; the gap is named), **GUIDE** (numeric or heuristic; refutes or guides, never discharges), **RECALLED** (a known result used from memory, not re-read), **OPEN**.

## Sources read

Library folder `ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/` (read-only):

- `gap-skeleton-final.md`: Sections 1 to 3 in full; 13.15 to 13.19 in full; 13.12 item 4 and the (BOOT_eps) paragraph (lines 500 to 515).
- `gap-means-max.md` (Claude Fable 5.2 max): Sections 1, 2 (2.1 to 2.5) and 4 (4.1 to 4.10) in full.
- `gap-means-astra.md` (Codex gpt-6-astra max): Sections 1, 2 (2.1 to 2.6) and 4 in full.
- `gap-es1-opus.md` (Claude Opus 5.5): Sections 0, 1, 2, 5, 6, 7, 8 in full.
- `gap-crux-fp.md`: Section 3b.3 and the table of 3b.4.
- `gap-mid-max.md` (row 708): candidate C-E (the bootstrap form (BOOT_eps)), lines 81 to 89. Found by the repo search below.
- `prior/gap-lit-assoc.md` lines 1 to 60 and its grep hits; `FINISH.md` row 754 (this item).

Repo search before deriving (rule: check the repo first). `grep` of the library for "loop equation", "Makeenko", "master loop", "Chatterjee", "Kazakov", "(EP)": the loop-equation hits are `gap-mid-max.md` C-E ((BOOT_eps); not attacked there), `gap-crux-fp.md` line 238 and `gap-flux-exercise.md` line 311 (set aside as numerical), `gap-means-max.md` (M8) (absent by rule), and the literature digests `prior/gap-crux-lit-cross.md`, `prior/gap-crux-lit-nonab.md` (Kazakov and Zheng: the SU(2) trace identity closes the loop equations on single traces). (EP) is OPEN in `gap-means-astra.md` 2 and 4 and in `prior/gap-lit-assoc.md`; no file combines (EP) with Corollary NS0 of `gap-means-max.md`. No row owns the statements of Sections 1, 4, 5, 6 below.

Literature (arXiv abstract pages only; no PDF was downloaded; fetched text treated as data):

- S. Chatterjee, arXiv:1502.07719. **Correction to the brief:** this paper is on **SO(N)** lattice gauge theory (strong coupling, large N, Wilson loops as sums over lattice string trajectories). It is the origin of the rigorous lattice master loop equation.
- S. Chatterjee and J. Jafarov, arXiv:1604.04777. **Correction to the brief:** the 1/N expansion for **SO(N)** at strong coupling.
- J. Jafarov, arXiv:1610.03821: the SU(N) form (1/N expansion at strong coupling). This is the SU(N) source; I did not read its equations.
- S. Cao, M. Park and S. Sheffield, arXiv:2307.06790: Wilson loop expectations as sums over embedded maps, for U(N), SU(N) and other groups, every beta and dimension (abstract read). Its Proposition 6.27 (the sign mechanism for non-orientable surfaces) is cited through `gap-skeleton-final.md` 13.19, not read by me.
- V. Kazakov and Z. Zheng, arXiv:2203.11360 and arXiv:2404.16925 (bootstrap; SU(2) single-trace closure): cited through the lane digests named above, not read by me.

**Every equation of Section 1 is derived here by hand from integration by parts on SU(2).** No step rests on a paper. The credits are for priority: the lattice Schwinger-Dyson (Makeenko-Migdal) equations are classical; the rigorous lattice master loop equation is Chatterjee's (SO(N)) and Jafarov's (SU(N)); the linear closure for SU(2) is stated by Kazakov and Zheng.

Scripts and outputs (this folder; pure Python, `python3 -I`, under 50 MB, no numpy): `le_link_check.py` / `le_link_check.out` (Section 1, GUIDE), `s0_check.py` / `s0_check.out` (Section 4, exact computation, GUIDE).

---

## 1. The SU(2) loop equations in Ward form

**Setting.** A finite periodic four-dimensional torus with all sides at least 3, links U_l in SU(2), x_p := (1/2) tr U_p, Wilson measure proportional to exp(beta sum_p x_p) times Haar measure. For a loop C, W(C) := (1/2) tr U_C and w(C) := E W(C). For a link e, h_e := sum of x_p over the six plaquettes p that contain e (the local energy at e). For a plaquette p that contains e, write U_p = U_e B_p (the plaquette read from the start of e; B_p is its staple; orientation does not matter for SU(2) traces, since tr U = tr U^(-1)). If C passes e, C ⊖_i p is the loop C with its i-th passage of e replaced by the staple path B_p^(-1) (the deformation of C across p).

Generators t_a = i sigma_a (a = 1, 2, 3), (d_a f)(U_e) := d/ds f(e^(s t_a) U_e) at s = 0. With this normalization the geodesic s -> e^(s t_3) has period 2 pi, as for U(1) embedded as the maximal torus diag(e^(i s), e^(-i s)), and (1/2) tr diag(e^(i s), e^(-i s)) = cos s. So the SU(2) coupling beta and the U(1) coupling beta are comparable on the maximal torus.

Three algebraic facts (PROVED; standard): (i) sum_a t_a t_a = -3. (ii) The completeness relation sum_a (sigma_a)_ij (sigma_a)_kl = 2 delta_il delta_kj - delta_ij delta_kl gives, for 2 x 2 matrices X, Y,
sum_a tr(t_a X) tr(t_a Y) = tr X tr Y - 2 tr(XY), and sum_a tr(t_a X t_a Y) = tr(XY) - 2 tr X tr Y.
(iii) For X, Y in SU(2): tr X tr Y = tr(XY) + tr(XY^(-1)). With (iii), the first identity of (ii) becomes sum_a tr(t_a X) tr(t_a Y) = tr(XY^(-1)) - tr(XY).

Integration by parts: d_a is a left-invariant vector field, so the integral of d_a g against Haar measure is 0, and E[d_a d_a f + (d_a f)(d_a S)] = 0 for S = beta sum_p x_p and smooth f; sum over a.

**Lemma 1.1 (Ward form, one passage; PROVED).** If C passes e exactly once,

E[ W(C) (3 + beta h_e) ] = beta sum over the six p containing e of w(C ⊖ p).

Proof. Write tr U_C = tr(U_e A). By (i), sum_a d_a d_a tr(U_e A) = -3 tr(U_e A). By (ii)-(iii), sum_a d_a(tr U_e B_p) d_a(tr U_e A) = tr(U_e B_p A^(-1) U_e^(-1)) - tr(U_e B_p U_e A) = tr(B_p A^(-1)) - tr(U_e B_p U_e A), and by (iii) again tr(U_e B_p U_e A) = tr(U_e B_p) tr(U_e A) - tr(B_p A^(-1)). With S = (beta/2) sum_p tr U_p: 0 = E[-3 tr(U_e A) + (beta/2) sum_p (2 tr(B_p A^(-1)) - tr(U_e B_p) tr(U_e A))]. Divide by 2 and use tr(B_p A^(-1)) = tr(B_p^(-1) A) = 2 W(C ⊖ p), tr(U_e B_p) = 2 x_p. QED

**Lemma 1.2 (Ward form, m passages in the same direction; PROVED).** If C passes e exactly m times, all in the same direction, so tr U_C = tr(U_e A_1 U_e A_2 ... U_e A_m), then

E[ W(C) (m(m+2) + m beta h_e) ] = beta sum over p containing e, sum over i = 1..m of w(C ⊖_i p) - 4 sum over i < j of w(o_ij),

where, cutting the word before its i-th and j-th U_e as tr(XY), o_ij is the loop of tr(X Y^(-1)).

Proof. The second derivative of the word puts t_a t_a at each U_e (giving -3m W) and t_a ... t_a at each pair (i, j). By (ii) a pair gives tr(XY) - 2 tr X tr Y, and by (iii) tr X tr Y = tr(XY) + tr(XY^(-1)). So the Laplacian is -3m W + sum_{i<j} 2(-W - 2 o_ij) in trace units, that is -(3m + m(m-1)) W - 4 sum o_ij = -m(m+2) W - 4 sum o_ij. The first derivative is a sum over i of tr(t_a W_i), W_i the word read from its i-th U_e; by (ii)-(iii) the gradient term is (beta/2) sum_p sum_i (2 tr(U_p W_i^(-1)) - tr U_p tr U_C), and U_p W_i^(-1) is the loop C ⊖_i p. Normalize by 1/2. QED

For m = 2, o_12 = tr(A_1 A_2^(-1)) no longer passes e. m(m+2) = 4 j(j+1) with j = m/2: the Casimir of spin m/2.

**The U(1) analogue (PROVED, same computation with d/d theta).** For U(1) with x_p = cos theta_p and a loop that passes e m times in the same direction:

E[ W(C) (m^2 + m beta h_e) ] = m beta sum_p w(C ⊖ p),

with no splitting term. So at one passage SU(2) has 3 where U(1) has 1 (the dimension of the group; the eigenvalue of the fundamental character), and at m passages SU(2) has m(m+2) and the splitting terms -4 sum o_ij, which U(1) lacks.

**GUIDE check of the coefficients (`le_link_check.py`).** Both lemmas are identities of the one-link conditional law, so they can be tested on one link with six random staples. Criteria written before the run: the residual of Lemma 1.1 (m = 1), of Lemma 1.2 (m = 2) and of the U(1) form must vanish within 5 standard errors; the same residuals with the coefficient 1 in place of 3 (SU(2)) and 3 in place of 1 (U(1)) are controls that must fail. Result, 8 x 10^5 Haar samples at beta = 0.3, 1, 2: all six true residuals within 1.4 standard errors of 0; all six controls fail (8.7 to 292 standard errors). PASS.

## 2. The shapes

All statements in this section are **PROVED** specializations of Lemmas 1.1 and 1.2 and of identity (iii), in a state that is invariant under the lattice symmetries (all six plaquettes at a link equivalent). w_1 := E x_p; w_R := the 1 x 2 rectangle; w_C := the chair (the 1 x 2 rectangle bent through a right angle at its middle link).

**2.1 Plaquette.** C = p, e in p. C ⊖ p is the trivial loop (W = 1). For the coplanar neighbour p'_0 of p at e, C ⊖ p'_0 is the 1 x 2 rectangle; for each of the four plaquettes at e in the two other planes, a chair. So

3 w_1 + beta E[x_p h_e] = beta (1 + w_R + 4 w_C).    (E1)

Summed over the six plaquettes at e: 18 w_1 + beta E[h_e^2] = 6 beta (1 + w_R + 4 w_C). With E h_e^2 >= (E h_e)^2 = 36 w_1^2:

3 w_1 + 6 beta w_1^2 <= beta (1 + w_R + 4 w_C).    (E1')

U(1): w_1 + 6 beta w_1^2 <= beta (1 + w_R + 4 w_C), with the same loops. Check at beta = 0: (E1) gives w_1 = beta/4 + O(beta^2), the strong-coupling value (E x^2 = 1/4 under Haar).

**2.2 Double-winding plaquette.** C = p∘p, W(C) = (1/2) tr U_p^2 = 2 x_p^2 - 1, every link passed twice in the same direction, o_12 = trivial loop. Lemma 1.2 with m = 2, and (iii) to write C ⊖_i p' as 2 x_p W(R_pp') - x_p' (R_pp' := p ⊖ p', a rectangle or a chair), gives

4 E x_p^2 = 1 + beta [ E(x_p - x_p^3) + sum over the five p' != p at e of E(x_p W(R_pp') - x_p^2 x_p') ].    (E2)

I derived (E2) a second time directly from the second derivative of tr(U_e B U_e B); the two forms agree. Check at beta = 0: E x^2 = 1/4.

**2.3 1 x 2 rectangle and chair.** For the rectangle R and e its short end link: R ⊖ (its own end plaquette) is the other plaquette with a backtrack (W = x), R ⊖ (the outer coplanar plaquette) is the 1 x 3 rectangle, and the four others give the 1 x 2 rectangle with a bent end. So 3 w_R + beta E[W(R) h_e] = beta (w_1 + w_(1x3) + 4 w_(bent)). The chair is the same with its own neighbours. Each equation brings loops of length 8; the system does not close on any finite set of shapes, which is the standard situation.

**2.4 Figure-8 loops and the SU(2) identity.** Two plaquettes p, p' through e in the same direction (the merger C ⊕ p of Lemma 1.1): pointwise W(p ⊕ p') = 2 x_p x_p' - W(R_pp'). Two plaquettes through one vertex only (astra's F, G of `gap-means-astra.md` 2.1): F + G = 2 x_p x_q pointwise. **For the U(1) test this matters:** on the maximal torus the identity (iii) is cos(a + b) + cos(a - b) = 2 cos a cos b. So the trace identity, used on loops whose holonomies commute, is a property that U(1) (as the maximal torus) shares. What U(1) lacks is (a) the Casimir 3 and the splitting terms of Lemma 1.2, (b) non-commuting holonomies (commutator loops with tr != 2), (c) the pseudoreality of the spin-1/2 representation: the Haar mean of U^2 is -1/2 times the identity (`gap-means-max.md` 2.4, integral (3)). Of these, (c) is used in Section 4.

**2.5 Clovers.** Let U_1, ..., U_4 be the four plaquettes around a site O in one plane, each read counter-clockwise from O, in cyclic order. Consecutive ones share a link that the first leaves on and the second enters on, so U_1 U_2 is the 1 x 2 rectangle based at O and **U_1 U_2 U_3 U_4 is the boundary of the 2 x 2 square**: the ordered clover loop has no self-crossing after cancellation. The genuinely self-crossing clover loops are the other orders, for example U_1 U_3 (opposite quadrants, a figure-8 through O) and, in four dimensions, U_(12) U_(34) (the 4D clover of astra's F). The clover matrix Q := U_1 + U_2 + U_3 + U_4 is a quaternion; |Q|^2 = (1/2) tr(Q Q^dagger) = 4 + 2 sum_{i<j} W(U_i U_j^(-1)) >= ((1/2) tr Q)^2 = (sum_i x_i)^2 pointwise. So

sum_{i<j} W(U_i U_j^(-1)) >= ((sum_i x_i)^2 - 4)/2 pointwise.    (E3)

This is a pointwise inequality between figure-8 loops and plaquettes. It holds on the maximal torus as well (complex numbers), so it is no filter for U(1).

**What the shapes give.** Every relation above is local: it holds for every state that satisfies the loop equations near one site. Section 5 shows that this is the reason they cannot bound (ES) without loops of the size of the seed.

## 3. Positivity: what it gives for the even sector

Inputs: the class of `gap-es1-opus.md` Section 1 ((TM-tw), (F1), (S3); positive trace-class transfer operators; lambda_0(B) simple with an even eigenvector Omega_B). For a box B, the ground state of B is the state on B x Z (time infinite) given by Omega_B; its Euclidean correlations are E[F(0) G(t)] = <F Omega, (T/lambda_0)^t G Omega> for functions F, G of the links of one time slice. Write r_n := lambda_n/lambda_0 in [0, 1) for the even excited eigenvalues (T >= 0), so S_ev(t; B) = sum_{n >= 1} r_n^t.

**Lemma 3.1 (even thermal sum against one correlation; PROVED).** Let O be a real, centre-even function of the links of one time slice with Var(O) > 0 in the ground state of B, and C_O(t) := E[O(0) O(t)] - (E O)^2. Then for every t >= 1

S_ev(t; B) >= C_O(t)/C_O(0) >= (C_O(1)/C_O(0))^t.

Proof. psi := (O - E O) Omega is even and orthogonal to Omega, with ||psi||^2 = C_O(0). In the even eigenbasis, C_O(t) = sum_{n>=1} |c_n|^2 r_n^t <= (sum |c_n|^2) max_n r_n^t <= C_O(0) S_ev(t; B). For the second inequality, mu := |c_n|^2/C_O(0) is a probability on {r_n}, and Jensen gives E_mu[r^t] >= (E_mu r)^t. QED

**Reading.** Lemma 3.1 points the wrong way for (ES): it is a *necessary* condition. (ES) at a needs, for every even observable O of a time slice of the cube a^3, C_O(1)/C_O(0) <= 10^(-7/a). It points the *right* way for the fusion input (F-h), which needs a lower bound on S_ev (Section 6). The Gram matrices of the Kazakov-Zheng bootstrap are matrices of the numbers E[theta(F_i) F_j]; Lemma 3.1 is what they say about S_ev, one vector at a time. **U(1):** the lemma holds; it gives no gap (a lower bound on S_ev).

## 4. The association (EP) is false (aim (c))

(EP) of `gap-means-astra.md` 2: on every finite four-dimensional periodic torus with sides at least four, Cov_beta(prod_p W_p^(n_p), prod_p W_p^(m_p)) >= 0 for all beta_p >= 0 and n_p, m_p in N_0, with W_p = x_p = (1/2) tr U_p.

Inputs. S_0: the 92-plaquette lattice projective plane of `gap-means-max.md` 2.4 (constructed there by Claude Fable 5.2 max, row 737), with Proposition NS for chi = 1: the Haar integral of prod_{p in S_0} x_p is -2^(-183). Both were **checked by Codex gpt-6-astra max (row 744, `gap-skeleton-final.md` 13.19: "Corollary NS0 holds", with one added hypothesis in Proposition NS that the chi = 1 case with one plaquette cycle at every vertex satisfies)**. Write S_0 = M + (A + C) for its three families (the Moebius band M, the collar A, the disc C).

**Theorem EP-NO (PROVED given the inputs).** Let the torus contain S_0 (sides at least 4, 4, 5, 3 up to a permutation of the axes; for example all sides at least 5). Put F := prod_{p in M} x_p and G := prod_{p in A + C} x_p (so n = 1_M, m = 1_(A+C)).

(a) At beta_p = 0 for all p: Cov_0(F, G) = -2^(-183) < 0.
(b) If 0 <= beta_p <= 2^(-197) for every plaquette p (inhomogeneous couplings allowed): Cov(F, G) < 0.
(c) The same holds in the centre-even state of the torus.

So (EP) is false.

Proof. (a) Under Haar measure, Cov_0(F, G) = E_0[FG] - E_0[F] E_0[G], and FG = prod_{S_0} x_p, whose mean is -2^(-183) by the input. M is a nonempty proper subset of S_0, and S_0 is connected through shared links with every link in exactly two of its plaquettes; so some link l lies in exactly one plaquette of M (and one of A + C). In F that link occurs in exactly one factor, once, so F is of the form (1/2) tr(U_l X) with X independent of U_l, and the Haar mean of U_l is 0: E_0[F] = 0. (Likewise E_0[G] = 0.)
(b) This is the argument of `gap-means-astra.md` 2.3 with other constants. Let E be the 184 links of S_0. Conditionally on all other links, the density of the links of E relative to product Haar measure is proportional to exp(V), V = sum of beta_p x_p over the plaquettes that touch E, at most 184 x 6 = 1104 of them; V has oscillation at most 2 x 1104 x beta_max = 2208 beta_max. So the conditional density f obeys exp(-2208 beta_max) <= f <= exp(2208 beta_max), and for every H supported on E with |H| <= 1, |E[H | exterior] - E_0 H| <= delta := exp(2208 beta_max) - 1; average over the exterior. With beta_max <= 2^(-197) and 2208 < 2^12: 2208 beta_max < 2^(-185), and delta <= 2 x 2^(-185) = 2^(-184) (e^u - 1 <= 2u for u <= 1). Apply this to F, G, FG (each bounded by 1, supported on E): Cov(F, G) <= -2^(-183) + delta + delta^2 <= -2^(-183) + 2^(-184) + 2^(-368) < 0.
(c) The centre-even state is a positive mixture of electrically twisted measures (Lemma MX of row 731, as used in `gap-means-astra.md` 2.4), each a Wilson measure with couplings +beta_p or -beta_p. The bound of (b) uses only |beta_p|, so it holds in each, and the three moment bounds pass to a positive mixture. QED

**GUIDE (exact computation, an implementation separate from row 737's scripts): `s0_check.py`.** Criteria written first: K1, the list built from the text of 2.4 has F = 92, every link in exactly two plaquettes, connected, one plaquette cycle at every vertex, chi = 1; K2, the exact Haar integral of prod x_p over S_0, by the four SU(2) gluing rules in exact rationals, equals -2^(-183); K3, the two partial products have Haar mean 0. Result (`s0_check.out`): F = 92, E = 184, V = 93, chi = 1, all checks true; the integral is exactly -2^(-183); the control (the surface of a unit cube, chi = 2) gives +2^(-10) as Proposition NS predicts; Cov_0 = -2^(-183). PASS. This re-derives the input with a different data path (my reading of the construction and my own gluing code), but it is a computation: it guides, it does not discharge.

**The U(1) test (Propositions T1 to T3 of `gap-crux-fp.md`).** (EP) holds for U(1) with x_p = cos theta_p (Ginibre's inequality, RECALLED: products of cosines expand into cosines of integer combinations with positive coefficients) and for Z_2 (Griffiths, Kelly and Sherman, RECALLED). So (EP) is a property that U(1) and Z_2 have and SU(2) lacks. The failing mechanism is the pseudoreality of the spin-1/2 representation (Frobenius-Schur indicator -1, Haar mean of U^2 = -I/2), which U(1) and Z_2 do not have. **So no Ginibre-type or Griffiths-type proof over monomials of elementary plaquettes can exist for four-dimensional Wilson SU(2).**

**What survives (marks).**
- The two-plaquette form Cov(x_p, x_q) >= 0: OPEN. NS0 does not touch it at leading order: the lowest terms of Cov(x_p, x_q) at small beta come from the smallest closed plaquette surfaces through p and q, which are orientable (cube surfaces and tubes), so they are positive (ARGUED; not written as a theorem).
- Restricted cones (sources whose union contains no closed non-orientable plaquette set): OPEN; I state no such cone.
- The smallest closed plaquette set with odd Euler characteristic in Z^4: OPEN (row 737 found none in one or two hypercubes).
- On tori with all sides 4, (EP): not decided here (S_0 needs a side of at least 5).

## 5. The crux in loop variables, and why local equations cannot reach it (aims (a) and (d))

### 5.1 The two numbers of (ES) are integrated finite-size shifts of the plaquette

For a box B (three sides at least 3) and t >= 3 let wbar(s; t, B) be the mean of x_p over the 6 t |B| plaquettes of the torus t x B at coupling s.

**Lemma 5.1 (PROVED, in the class).** For every box B, e(B)(0) = 0, the limit wbar_inf(s; B) := lim_{t -> inf} wbar(s; t, B) exists for almost every s, and

e(B)(beta) = 6 |B| * integral_0^beta wbar_inf(s; B) ds.

Proof. Z(t, B) = Tr T_B^t (class input (TM)) and d/ds log Z(t, B) = E[sum_p x_p] = 6 t |B| wbar(s; t, B). So g_t(s) := (1/t) log Z(t, B)(s) is convex in s (a log-moment generating function) and g_t(0) = 0 (Haar is a probability, so Z = 1 at s = 0). g_t -> e(B) pointwise: Z(t, B) = lambda_0^t (1 + S(t)) with S(t) := Tr T^t/lambda_0^t - 1 non-increasing in t and finite (trace class), so (1/t) log(1 + S(t)) -> 0. A pointwise limit of convex functions is convex, and at every point where the limit is differentiable the derivatives converge (the standard lemma on convex functions); a convex function is differentiable almost everywhere and is the integral of its derivative. QED

**Corollary 5.2 (the plaquette form of (ES); PROVED).** With wbar_L := wbar_inf(s; L^3), the ground-state mean plaquette of the periodic cube of side L,

delta = a (8 e(a^3) - e((2a)^3)) = 48 a^4 * integral_0^beta [ wbar_a(s) - wbar_(2a)(s) ] ds,

Delta(c, d) = a (2 e(a, c, d) - e(2a, c, d)) = 12 a^2 c d * integral_0^beta [ wbar_inf(s; (a, c, d)) - wbar_inf(s; (2a, c, d)) ] ds,

log(1 + eps) = 6 a^4 * integral_0^beta [ wbar_ev(s; a^4) - wbar_a(s) ] ds,

where wbar_ev(s; a^4) := (1/(6 a^4)) d/ds log Z_0(a; a^3) is the mean action density of the centre-even thermal state of the torus a^4 (a positive mixture of twisted Wilson measures, by (F1) and positivity of each twisted partition function).

Proof. The first two: Lemma 5.1 and |a^3| = a^3, |(2a)^3| = 8 a^3. The third: log(1 + eps) = log Z_0(a; a^3) - a e(a^3); Z_0 = (1/8) sum_e Z^e is 1 at s = 0 (each Z^e is a Haar integral of 1 at s = 0), and Lemma 5.1. QED

So **(ES) is the statement that the plaquette, integrated along the coupling, does not see whether it sits in the cube a^3 or (2a)^3 (delta), or in the ground state or the even thermal state of a^4 (eps), to the precision 10^(-7)/(48 a^4 beta) on average.** The lower sides are free: delta >= 0 (Lemma K) and eps >= 0. A proof must supply the upper sides. This is the exact consumer for any loop-equation method, because loop equations are equations for wbar and its neighbours. (Credit: the plaquette difference of two tori as the seed quantity is in `gap-mid-max.md` Lemma M and Proposition MIX, row 708; the three formulas above, for the numbers of (ES), are new in the searched record.)

### 5.2 Volume blindness

**Proposition VB (PROVED; it is an embedding argument).** Fix r >= 1. Let K_r be any set of constraints on a linear functional w on loop functions, each of one of these kinds: (i) a loop equation of Lemma 1.1 or 1.2 for a pair (C, e) such that C, every C ⊖_i p, every o_ij and the six plaquettes at e lie in a lattice ball of radius r; (ii) positivity of a Gram matrix [w(theta(F_i) F_j)] for contractible loop functions F_i in a half-ball of radius r, theta a reflection in a time plane; (iii) normalization and lattice symmetry. Then K_r is satisfied by the ground state of every cube L^3 with L >= 2r + 3, and by the centre-even thermal state of every torus a^4 with a >= 2r + 3. Hence any inequality |wbar_a - wbar_(2a)| <= eta(s) that follows from K_r alone also holds for every pair of sides L, L' >= 2r + 3 in place of a, 2a, and for the pair (even thermal state of a^4, ground state of a^3).

Proof. A ball of radius r embeds isometrically in each of these tori. (i): the loop equations are identities of the one-link conditional law, which in each of these states is the Wilson one, after a centre gauge change moves the twist stacks of the even state away from the ball (the stack moves within its homology class; loop functions in the ball are unchanged). (ii): the ground state is the vacuum of the positive operator T, so E[theta(F) F] = ||F Omega||^2 >= 0 for a reflection across a time plane; in the even thermal state, contractible loop functions commute with the centre projection P_0, and the trace form Tr(P_0 X^dagger X)/Z_0 is >= 0. (iii) is clear. QED

**Consequence (ARGUED; the physical input is GUIDE).** A certificate for delta from K_r needs eta <= 10^(-7)/(48 a^4 beta) on average, while eta(s) is at least |wbar_(2r+3)(s) - wbar_L(s)| for every L >= 2r + 3. The finite-size shift of the plaquette of a cube of side L is of order exp(-m L) in a massive phase (GUIDE: Luescher's picture of virtual states winding the box; recalled). So a certificate needs 2r + 3 of about a + log(48 a^4 beta 10^7)/m: **loops of the size of the seed itself, at about a/2**, and precision far below any hand certificate. This makes the verdict on (BOOT_eps) in `gap-mid-max.md` C-E quantitative; it is the same verdict.

### 5.3 Winding loops and the difference equation

What distinguishes the cubes a^3 and (2a)^3 in loop variables is the set of loops that wind. The difference D := w^(1) - w^(2) of two states that satisfy the loop equations on a set of loops solves the homogeneous equations there (Lemma 1.1, 1.2 with the source terms removed). Bounding D at the plaquette from |D| <= 2 on winding loops needs a contraction of the homogeneous map.

**Proposition CR (the l-infinity ratios; PROVED by counting coefficients).** Bound |D| at a loop that passes e m times in one direction by the sum of the absolute coefficients of the other loops of its equation, written with single loops only (the mergers C ⊕ p kept as loops, as in Lemma 1.1's proof). The ratio is

SU(2): theta_m(beta) = (2(m - 1) + 6 beta)/(m + 2), so theta_1 = 2 beta, theta_2 = (1 + 3 beta)/2, theta_3 = (4 + 6 beta)/5, theta_4 = 1 + beta;
U(1): theta_m(beta) = 6 beta/m.

Proof. SU(2): the coefficient of D(C) is m(m+2); the m passages and six plaquettes give 6m deformation and 6m merger terms of absolute weight beta/2 each (6 m beta in all, from (beta/2)(tr(U_p W_i^(-1)) - tr(U_p W_i)) per pair); the splitting terms give 4 C(m, 2) = 2 m(m-1). U(1): coefficient m^2, gradient weight 6 m beta, no splitting. QED

**Reading (ARGUED).** At one passage the Casimir 3 makes the SU(2) map three times more contracting than the U(1) map (beta < 1/2 against beta < 1/6): a property U(1) lacks, and it acts in the right direction. But the iteration creates multiple passages at once (C = p, p' = p gives p∘p), and theta_m >= 1 for m >= 4 at every beta >= 0, through the splitting terms (at beta = 0 these are exact Haar recursions; the l-infinity count ignores their cancellations). So the plain scheme fails at every beta, and a weighted norm is needed (the method of Chatterjee and of Jafarov, at strong coupling). Even at one passage the natural range ends at beta = 1/2, far below the crossover of Wilson SU(2) near beta = 2.2 (GUIDE, recalled). The strong-coupling seed is already proved for beta < 1/18 (Theorem DOB, `gap-skeleton-final.md` 13.12), so a loop-equation contraction would at best extend that range by a factor below 9; I did not pursue it. **Positivity does not repair the ratio:** Gram constraints act on each state separately, and D ranges over differences of two points of one convex set, which reach its diameter unless the set is small (that is, unless a uniqueness statement is already known). OPEN: a weighted norm in which the homogeneous SU(2) map, restricted to differences of positive solutions, contracts at an effective coupling of order one. I know no candidate weight that does not presuppose an area law.

## 6. Fusion (aim (b)): what positivity gives, and the one input it lacks

Notation of `gap-es1-opus.md` Sections 1, 2, 5: on the box A = (a, c, d) at the time a, sector weights p_z, light set L, heavy weight H_L, light thermal sums s_z, S := eps_cd.

**Remark 6.1 (any positive exponent suffices; PROVED from Theorem V (b) of `gap-es1-opus.md`).** Replace (F-h) by (F-h_gamma): p_z <= K S^gamma for the twelve z not in L, with some gamma in (0, 1]. If also (F-l) s_z <= K S on L, and 6 K S^gamma + 2 K S <= 1/2, then Delta(c, d) <= 12 K S^gamma + 4 K S + S'_cd. Proof: eta_L <= 6 K S^gamma + 2 K S <= 1/2, then Theorem V (b), -log(1 - y) <= 2y for y <= 1/2, log(1 + S') <= S'. QED. Since (ES) is wanted at one physical size and any size will do, the constants and the exponent only move that size; what matters is uniformity in the cutoff. So the target is: **some** power of the even sum bounds the heavy weights.

**Lemma 6.2 (fusion by the product rule; PROVED given (PK)).** Input (PK): T_B has a continuous, strictly positive kernel on the spatial configurations (in temporal gauge; true for the Wilson weight of every compact group, RECALLED, not re-checked here). Let Ptilde := Omega^(-1) (T/lambda_0) Omega, the ground-state transform, a self-adjoint Markov operator on L^2(pi), pi := Omega^2 dU. Let r_1 be the top of the spectrum of Ptilde on centre-even functions orthogonal to 1 (so r_1 = the top even excited ratio, and S_ev(t; B) >= r_1^t), and Dir(f) := <f, (1 - Ptilde) f>_pi. Then for every real, bounded function f in an electric sector chi != 0 (f(C^e U) = (-1)^(chi.e) f(U) for the centre flips C^e), with Var_pi(f^2) > 0:

1 - r_1 <= 4 ||f||_inf^2 Dir(f)/Var_pi(f^2).

Proof. Omega is even, so the flips preserve pi and commute with Ptilde; f^2 is even, and g := f^2 - E_pi f^2 is even and orthogonal to 1. For a reversible Markov operator, Dir(h) = (1/2) double integral of (h(x) - h(y))^2 pi(dx) Ptilde(x, dy) (expand, and use Ptilde 1 = 1 and reversibility). Pointwise (f(x)^2 - f(y)^2)^2 = (f(x) - f(y))^2 (f(x) + f(y))^2 <= 4 ||f||_inf^2 (f(x) - f(y))^2, so Dir(g) = Dir(f^2) <= 4 ||f||_inf^2 Dir(f). By the min-max principle (Ptilde >= 0 since T >= 0), 1 - r_1 <= Dir(g)/||g||^2 and ||g||^2 = Var_pi(f^2). QED

**Corollary 6.3 (from a good trial flux function to (F-h_gamma); PROVED).** Let r_chi be the top eigenvalue ratio of T/lambda_0 in the electric sector chi, and Theta_chi := Tr(T^(a/2) P_chi)/lambda_0^(a/2). If some f in the sector chi has Dir(f) <= c_1 (1 - r_chi) ||f||^2 and ||f||_inf^2 ||f||^2 <= c_2 Var_pi(f^2), then with c := 4 c_1 c_2,

p_chi(a; B) <= Theta_chi * max( S_ev(a; B)^(1/(4c)), exp(-a/(4c)) ).

Proof. Lemma 6.2 gives 1 - r_1 <= c (1 - r_chi). p_chi <= Tr(T^a P_chi)/lambda_0^a <= r_chi^(a/2) Theta_chi (on the chi-sector, T^a <= (r_chi lambda_0)^(a/2) T^(a/2)). Put u := 1 - r_chi, so r_chi^(a/2) <= exp(-u a/2). If c u <= 1/2: r_1 >= 1 - c u >= exp(-2 c u), so S_ev >= r_1^a >= exp(-2 c u a), and exp(-u a/2) = (exp(-2 c u a))^(1/(4c)) <= S_ev^(1/(4c)). If c u > 1/2: exp(-u a/2) < exp(-a/(4c)). QED

With Remark 6.1 this gives (ES) as one kind of number for the **electric** heavy sectors, once c and Theta_chi are bounded uniformly in the cutoff.

**Where it breaks (ARGUED, with a GUIDE).**
1. *The true flux eigenfunction is too spread out.* For f = psi_chi (the eigenfunction, in the ground-state representation) c_1 = 1, but c_2 = ||psi||_inf^2/(||psi||_4^4 - 1) is of the order of the number of places the flux can sit (GUIDE: for the one-particle state of the 2D Ising model, psi is close to a normalized zero-momentum sum of spins, so ||psi||_inf^2 grows like the length L while ||psi||_4^4 - 1 stays near 2). In four dimensions the analogue is a^2/xi^2 transverse positions, so 1/(4c) is about xi^2/a^2 and S_ev^(1/(4c)) is about exp(-m xi^2/a): not small. The product rule loses exactly the locality of the flux.
2. *A bounded localized trial function is what is needed:* the statement (LOC) below. Polyakov loops are bounded (|tr H| <= 2), and Ptilde is a contraction in L^inf, so smoothing f -> Ptilde^s f keeps ||f||_inf <= 2; but it shrinks ||f||_2 like the overlap with the low states, and c_2 then grows. Taking a single local Polyakov loop keeps c_2 = O(1) (at beta = 0: E (tr H)^2 = 1, E (tr H)^4 = 2) but makes Dir(f)/||f||^2 an ultraviolet number of order one, so c_1 is of order 1/(1 - r_chi). The trade-off between the two constants is the missing locality estimate of `gap-es1-opus.md` Section 5, now as one inequality for one trial function.
3. *Magnetic and dyonic heavy sectors are not covered.* Lemma 6.2 needs f and f^2 in the space of one Markov operator. For a heavy sector with a magnetic twist m != 0 the operator is T_(B,m), and f^2 lands in the untwisted space with a different kernel. In the believed confining picture (alpha = alpha_full, `gap-means-max.md` 4.7), the heavy single-direction types are (1,0) (electric: covered) and (1,1) (dyonic: not covered). OPEN.
4. *The SU(2) identity enters only cosmetically:* tr H tr H' = tr(H Gamma H' Gamma^(-1)) + tr(H Gamma H'^(-1) Gamma^(-1)) splits f^2 for Polyakov loops f into a doubly winding loop and a contractible flux-pair loop, both centre-even. On the maximal torus this is the cosine identity, so it is shared by U(1).

**The U(1) test.** Lemma 6.2 and Corollary 6.3 hold for U(1) (they need only (PK)); their conclusion is a fusion bound, not a gap, and U(1) at weak coupling has eps of order one, so nothing false follows (Proposition T1). The property that U(1) lacks would have to enter through (LOC): in the U(1) Coulomb phase the electric flux energy is of order g^2/a and photons of order 2 pi/a; (LOC) with uniform constants may well hold there too, and it is harmless there for the same reason.

## 7. Aim (d): the one-sided inequality that loop equations plus positivity would need, and where each attempt breaks

**The inequality (exact, by Corollary 5.2).** (ES) at a is equivalent to the two upper bounds

(LE-delta) 48 a^4 * integral_0^beta [ wbar_a(s) - wbar_(2a)(s) ] ds <= 10^(-7),
(LE-eps) 6 a^4 * integral_0^beta [ wbar_ev(s; a^4) - wbar_a(s) ] ds <= log(1 + 10^(-7)),

whose left sides are >= 0 at every beta for free. They are one-sided: a proof must show that the ground-state plaquette of the smaller cube exceeds that of the larger one by little, on average along the coupling, and that the even thermal plaquette of a^4 exceeds the ground-state one by little. Both are false for U(1) at weak coupling (the photon: delta of order one; RECALLED), so any proof must use a property U(1) lacks.

**Where each loop-equation attempt breaks.**

| Attempt | Breaks at | Mark |
|---|---|---|
| Local loop equations of any shapes (plaquette, rectangles, chairs, figure-8, clovers, double windings) with RP Gram positivity | Proposition VB: every such constraint with loops in a ball of radius r holds on all cubes of side >= 2r + 3, so the bound is no better than the finite-size shift at side 2r + 3; needs r near a/2 and precision 10^(-7)/(48 a^4 beta) | PROVED (VB); ARGUED (the size estimate, GUIDE input) |
| Difference equation with winding loops (contraction) | l-infinity ratios theta_1 = 2 beta (U(1): 6 beta) and theta_m >= 1 for m >= 4 at every beta (splitting terms); positivity does not bound differences | PROVED (counts); ARGUED (no scheme) |
| Association / Griffiths over elementary plaquettes (EP) | False: Theorem EP-NO (projective plane S_0, pseudoreality) | PROVED (given NS0, checked by astra) |
| Fusion through positivity (Lemma 3.1, Lemma 6.2) | Needs one bounded localized trial flux function (LOC); covers electric heavy sectors only | PROVED (lemmas); OPEN (LOC) |

**The single most promising open inequality (my judgement).** (LOC) at the seed size, uniformly in the cutoff: for the cube B = (a, a, a) at the coupling of the trajectory and each heavy electric sector chi, there is a real centre-odd function f of the links of one time slice (for example a combination of Polyakov loops in the direction of chi, with smoothing) such that

Dir(f) <= c_1 (1 - r_chi) ||f||_(L^2(pi))^2 and ||f||_inf^2 ||f||_(L^2(pi))^2 <= c_2 Var_pi(f^2),

with c_1, c_2 and Theta_chi bounded independently of the cutoff. By Corollary 6.3 and Remark 6.1 it makes the electric part of (ES) one number (a power of the even thermal sums on six boxes). It is a statement about one trial function, not about a trace or a volume difference; it is plausible in the confining picture (a flux tube at one transverse place has energy close to the flux gap, since its transverse kinetic energy is of order 1/(sigma a xi^2); GUIDE); and the place where a property U(1) lacks would have to enter is the bounded localization of the flux, which in U(1) is harmless (Section 6). It does not cover the dyonic sectors, and it does not touch the even half of (ES) itself.

## 8. Status of the statements

| Statement | Mark |
|---|---|
| Lemma 1.1: E[W(C)(3 + beta h_e)] = beta sum_p w(C ⊖ p) (one passage); U(1) has 1 for 3 | PROVED; GUIDE check PASS |
| Lemma 1.2: m passages in one direction, coefficient m(m+2), splitting terms -4 sum o_ij; U(1) coefficient m^2, no splitting | PROVED; GUIDE check PASS (m = 2) |
| (E1), (E1'), (E2), the rectangle and chair equations, the figure-8 identity, (E3); the ordered clover loop is the 2 x 2 loop | PROVED |
| The trace identity on commuting holonomies is the U(1) cosine identity (not a U(1) filter by itself) | PROVED |
| Lemma 3.1: S_ev(t; B) >= C_O(t)/C_O(0) >= (C_O(1)/C_O(0))^t for even O | PROVED |
| Theorem EP-NO: (EP) false at beta = 0 and for 0 <= beta_p <= 2^(-197), also in the even state, on every torus containing S_0 | PROVED given NS0 (checked by astra, row 744) |
| Exact recomputation of the S_0 combinatorics and of -2^(-183) | GUIDE (exact computation) PASS |
| (EP) holds for U(1) and Z_2 | RECALLED (Ginibre; Griffiths-Kelly-Sherman) |
| Cov(x_p, x_q) >= 0 for single plaquettes | OPEN (leading terms positive: ARGUED) |
| Lemma 5.1 and Corollary 5.2: delta, Delta(c, d), log(1 + eps) as integrated plaquette shifts | PROVED |
| Proposition VB (volume blindness of local constraints) | PROVED |
| Loops of size about a/2 and precision 10^(-7)/(48 a^4 beta) needed for a local certificate | ARGUED (GUIDE input: finite-size shifts exp(-mL)) |
| Proposition CR: theta_m = (2(m-1) + 6 beta)/(m+2) (SU(2)), 6 beta/m (U(1)) | PROVED |
| No l-infinity contraction for SU(2) at any beta once m >= 4; positivity does not repair it | ARGUED |
| A weighted-norm contraction at order-one coupling | OPEN |
| Remark 6.1: (F-h) with any exponent gamma > 0 suffices | PROVED |
| Lemma 6.2 (product-rule fusion) and Corollary 6.3 | PROVED given (PK) (RECALLED for Wilson weights) |
| (LOC) for SU(2) at the seed size, uniformly in the cutoff | OPEN |
| Fusion for magnetic and dyonic heavy sectors | OPEN |
| (ES), (F-h), (ES-1) for Wilson SU(2) at order-one coupling | OPEN |

**Credits.** Integration-by-parts loop equations: Makeenko and Migdal (classical; RECALLED); the rigorous lattice master loop equation: Chatterjee (arXiv:1502.07719, SO(N)) and Jafarov (arXiv:1610.03821, SU(N)); the SO(N) 1/N expansion: Chatterjee and Jafarov (arXiv:1604.04777); surface sums: Cao, Park and Sheffield (arXiv:2307.06790); SU(2) single-trace closure and the bootstrap: Kazakov and Zheng (via the lane digests). S_0, Proposition NS and Corollary NS0: Claude Fable 5.2 max (row 737), checked by Codex gpt-6-astra max (row 744); the conditional-density bound and the mixture step of Theorem EP-NO (b), (c): Codex gpt-6-astra max (row 738, Sections 2.3, 2.4); Theorem V, FUSE-suff, (F-h): Claude Opus 5.5 (`gap-es1-opus.md`); Theorem R, Lemma K, the class inputs: the files named in `gap-means-max.md` 4.1; (BOOT_eps) and the plaquette-difference form of the seed: `gap-mid-max.md` (row 708). The product rule for Dirichlet forms is the standard Beurling-Deny computation (RECALLED).

**Not done.** No bootstrap was run. No PDF was read; only four arXiv abstract pages. The class membership (PK) and the time-reflection positivity of the even thermal state for contractible loops are used as standard, not re-derived. Nothing here was checked by another model.

RESULT: (EP) is false for four-dimensional Wilson SU(2) (at beta = 0 and for 0 <= beta_p <= 2^(-197), also in the even state, through the projective plane S_0; U(1) and Z_2 satisfy it); the two numbers of (ES) are exactly integrated finite-size shifts of the ground-state plaquette, which local loop equations with RP cannot bound without loops of the seed size (Proposition VB) and the difference equation does not contract (theta_m >= 1 for m >= 4); positivity gives fusion with any exponent from one bounded localized flux trial function (LOC), which is open, as are (ES), (F-h) and (ES-1) at order-one coupling.
