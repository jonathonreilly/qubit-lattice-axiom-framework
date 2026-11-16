lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T11:55Z

# gap-cr-tomboulis-max (queue row 1025): the decimation line against Theorem CR and the vortex containers

Worker result file, research-stage working state. It grants no status and is no public claim. Pinned at commit
fe79776a6 of `claude/ym4d-hard-route`. Started 2026-11-15T23:55Z (`date -u`). Marks used: PROVED, ARGUED, OPEN,
FAILS. Nothing here is checked by a second reader yet.

Credit, by name, for everything this row builds on: E. T. Tomboulis (the decimation / vortex-free-energy argument,
arXiv:0707.2179 and the 2008-2009 follow-ups); T. Kanazawa (the comparison form of the same line); K. R. Ito and
E. Seiler (arXiv:0711.4930, the two obligations); G. Mack and V. B. Petkova (vortex containers and the 't Hooft
loop bound); N. Sussman and L. Alpoge (the complete account this lane ports). The lane's own rows used are named
where used.

## 0. Plan (at most eight steps; one step per response; each appended before the next)

1. Read `parts/gap.md`, the exercise skill (main 8b11ae2bb9), and the five named inputs with their checks. Log
   one line per source below as it is read.
2. Question (1): write Ito and Seiler's two obligations and the 2008 repair's trapping-domain / endpoint-bracket
   statement exactly, in the lane's notation.
3. Registry grep before any attack: `library/open-core.md`, FINISH rows, the idea digests. Name every match.
4. Question (4) first, as the row orders: run the tests (Lemma PT, Proposition NP, Theorem D2, Lemma SHEET,
   compact U(1), frozen Q_8 and 2T, the five-dimensional test) against the combination before building on it.
5. Question (2): does the compactness of Theorem CR / Proposition OM supply the common interpolation parameter
   or the trapping domain; test against Proposition SI.
6. Question (3): does (K-RESP) follow from Lemma PAR and Corollary MP on vortex containers, or reduce to (SER)
   and (SPR).
7. The first surviving piece: prove it by hand or build the counterexample.
8. Re-read of every PROVED item, verdict table, RESULT line.

## Status log (times from `date -u`)

- 23:55Z file created; GOAL.md and queue row 1025 read.
- 23:56Z read in full: `parts/gap.md`; exercise skill and `proof-search-governance.md` (main 8b11ae2bb9, fetched to
  /tmp/row1025-skill); `library/gap-tomboulis-read.md` (row 797, gpt-6-astra). Notes from row 797 kept for Step 2:
  T = Tomboulis 0707.2179; Z^+ = (Z + Z^-)/2; upper bound (3.1)-(3.4) Z_(m-1) <= (F_0^U)^(N_m) Z_m(c^U(r));
  interpolation alpha(t, r) per partition function (3.12)-(3.24); A = (N_m log F_0^U)^(-1) d/dalpha log Z_m,
  alpha_t = - h_t/(h_alpha + A); the disputed step is Appendix C (C.8)-(C.10): one t_* with
  alpha(t_*) = alpha^+(t_*); row 797 2.1: Psi(1, t) = 0 is exactly Z_c^+(alpha(t))/Z_c(alpha(t)) = Z_f^+/Z_f,
  and Psi_t = h_t (A - lambda A^+)/(h_alpha + A); Kanazawa v3 Theorem 4 (bounding flow reaches the small-coefficient
  basin for connected groups, U(1) included, b large, r = 1 - b^-2); Kanazawa v3 Theorem 1 (mismatched ratio,
  |alpha_Lambda - alpha| <= C/|Lambda_c|); 2008 repair = PoS Confinement8 020, (4.5)-(4.6) r_m adaptive,
  (4.9)-(4.11) Meyer's monotone iteration needing F(x_0) < 0, entrywise non-negative inverse, a bounded invariant
  domain with a boundary sign.
- 23:56Z read in full: `library/gap-tomboulis-check-opus.md` (row 799) and `library/gap-kanazawa-astra.md` (row 800).
  Kept for Step 2: check 799 B2: by the intermediate value theorem Psi(1, .) has a zero iff the fine ratio
  Z_f^+/Z_f lies in the range of alpha -> Z_c^+(alpha)/Z_c(alpha) over the alpha values the level curve reaches,
  "Appendix C therefore needs an endpoint bracket of the fine ratio by coarse ratios", which is T (5.23); check 799
  B5: the 2008 sign condition (ii) is met after t -> -t, "the substantive unproved hypotheses of the 2008 repair
  are (i) and the bounded invariant domain with a boundary sign, which amount to the endpoint bracket of B2".
  Row 800: (K1)-(K8) exact (D = log Q_c(alpha) - log Q_f; D = int_0^beta G_f - int_0^alpha G_c; G = -d/ds log Q;
  (K6) G_f = (2<WY> - Cov(W, H_m))/(1 + R)); (K17) inverse branch trapped in J for EVERY q in [1/2, 1] (so the
  mismatched representation encodes any ratio); (K-RESP) = [int_0^beta G_f ds - int_0^alpha G_c du]_+ <=
  (1/8) min{1/96, K(a) eta_*^(a/2)/4}, i.e. by (K21) up to 2N e^(-l^2): H_f = -log((1 + R_f)/2) small at the scale
  of the consumer (FQ) (or area-small for (V)).
- 23:56Z read: `library/gap-compact-rigidity-max.md` (row 1017) Sections 1-6 in full (L1-403). Kept for Steps 4-5:
  datum (E1)-(E3), eternal datum, admissible sequence (H1), (H2), critical element (3.1); Theorem CE (limit keeps the
  spectral form in four directions, the engine's non-strict finite inequalities, the centre grading (e); loses the
  ultraviolet data, the group, the action); Proposition OM (Omega compact, sigma a homeomorphism; stall (c),
  recurrence (d), monotone gives stationarity (e)); Theorem CR ((W) iff Omega empty iff no uniformly recurrent
  element iff for one continuous Lambda no element has Lambda(sigma E) >= Lambda(E), GIVEN (BDD-Delta)); Lemma
  PT-inf (the blow-down forgets every seeded factor); Proposition NR (constants log m are critical elements);
  Proposition SI (a kept property is sigma-invariant: no condition at one end of the scale axis is kept); Remark
  MON (a non-increasing continuous Lambda passes the ultraviolet data as one inequality Lambda(E) <= Lambda_UV).
- 23:56Z read: row 1017 Sections 7-8; check `library/gap-compact-rigidity-check-opus.md` (row 1019) Steps 6-8 and RESULT
  (L145-256; Steps 1-5 not read: they re-derive UF, CE, OM line by line). Repairs that bind this row: D2 (Omega =
  Omega(D_0) with D_0 a (BDD-Delta) bound), D4 ("no element of Omega(D_0)", not "no critical element"), D14 (SI
  says nothing on asymptotic conditions as b -> 0; what keeps the ultraviolet growth out of Omega is CE (d)), and
  6.5 (i): "by compactness a strict decrease on every element of Omega is automatically uniform".
- 23:57Z read: `library/gap-short-step-max.md` (row 1018) Sections 2-3, 5.2-5.3, 6.2, 7 (L70-212, L289-305, L389-443);
  not read: Sections 4, 5.1, 5.4-5.6, 6.1 (route (ii), Lemma NAB, the control run), which this row does not use.
  Check `library/gap-short-step-check-opus.md` (row 1022): headings and RESULT only (no WRONG; Lemma PAR (i)-(iii)
  and Corollary MP confirmed, MP against Mack and Petkova's (2.16), (2.19)-(2.21)). Kept for Step 6: Lemma PAR
  setting (sub-containers Lam_i with disjoint plaquette sets, twist system (H1), (H2), rho = Z(sigma Om)/Z(Om),
  r_i, a_i = tanh(v_i/2)); (i) E[prod_S r_i] = rho or 1 by parity of |S|; (ii) Etilde[a_1 ... a_n] = tanh(V/2), all
  proper sub-products vanish; (iii) |tanh(V/2)| <= prod_i tanh(xi_i/2); Corollary MP: E[O] = Etilde[O a_1 ... a_n]
  for O odd under each tau_i; (T-vor) open half O2: (SER) xi(Sigma_2l, D) <= kappa xi(Sigma_l, D), (SPR)
  xi(Sigma, D_2l) <= phi xi(Sigma, D_l), kappa phi < 1; Lemma PAR holds verbatim in frozen Z_2, Q_8, 2T and in five
  dimensions.
- 00:09Z primary sources fetched once into /tmp/row1025-lit (one folder each; PyMuPDF text; nothing executed) and read at
  the pages named in 1.2: Tomboulis 0707.2179v1; Ito and Seiler 0711.4930v1 (in full), 0803.3019v1; PoS
  Confinement8 020. Step 1 done. Step 2 next.

## 1. Step 1 result: what was read, what is pinned

### 1.1 Header in the form the exercise skill asks

Writer: Claude Fable 5.2 (Anthropic), max effort, Mac mini worker 1, one session, no subagents. Commit fe79776a6.
Date 2026-11-15/16. **Nothing in this file is checked by another model.** This is a standalone proof target, so
`GOAL.md` and the FINISH rules replace the skill's framework refresher read (the skill allows this and asks that
it is said). The row's brief names the files to read first, so the skill's "closed list" is empty here: the brief
wins. The wall has had five exercises (rows 878, 998, 1003, 1011, 1017); by skill step 0 their inventory,
assumption tables and set-aside lists are reused, not rewritten. This row runs the skill on one combination.

What this run did not cover is listed in Section 9.4.

### 1.2 Sources, with how each was read

| Source | Read | Used for |
|---|---|---|
| `parts/gap.md` (lead, 2026-11-15) | in full | the wall (W), lead rule W2, test table, registry |
| `library/gap-tomboulis-read.md` (row 797, gpt-6-astra) | in full | the reading of Tomboulis, Kanazawa, Ito and Seiler |
| `library/gap-tomboulis-check-opus.md` (row 799) | in full | B2 (bracket form), B5 (the 2008 sign is a convention) |
| `library/gap-kanazawa-astra.md` (row 800, gpt-6-astra) | in full | (K1)-(K8), (K17), (K21), (K-RESP) |
| `library/gap-compact-rigidity-max.md` (row 1017) | L1-480 | Theorems CE, CR, Propositions OM, NR, SI, Lemma PT-inf |
| `library/gap-compact-rigidity-check-opus.md` (row 1019) | L145-256 (Steps 6-8, RESULT) | repairs D2, D4, D14 |
| `library/gap-short-step-max.md` (row 1018) | L70-212, L289-305, L389-443 | Lemma PAR, Corollary MP, (T-vor), (SER), (SPR) |
| `library/gap-short-step-check-opus.md` (row 1022) | headings and RESULT | no WRONG on PAR, MP |
| E. T. Tomboulis, arXiv:0707.2179v1 | pp. 7-8, 10, 12-14, 24-28, 43-46 (text layer) | (2.18)-(2.22), (3.12)-(3.29), (5.1)-(5.24), Appendix C |
| K. R. Ito and E. Seiler, arXiv:0711.4930v1 | in full (10 pp.) | Claim 2.1, Theorem 2.1 (flow at r = 1), (3.1)-(3.11) |
| K. R. Ito and E. Seiler, arXiv:0803.3019v1 | pp. 6-7, 12-16 | Theorem 2.2, Problems 1-3, Section 3.3 |
| E. T. Tomboulis, PoS(Confinement8)020 | pp. 6-9 | (4.2)-(4.13), the 2008 repair |
| T. Kanazawa, arXiv:0805.2742v3 | fetched; not re-read (rows 797, 799, 800 read it) | - |
| G. Mack and V. B. Petkova, Ann. Phys. 125 (1980) 117 | not fetched; as rebuilt in row 1018 7.4 and confirmed by check 1022 | Corollary MP |
| Sussman and Alpoge's account (with Claude and Codex as authors of their text) | not opened in this row: rows 797 and 800 searched its index for Tomboulis, Migdal-Kadanoff, Kanazawa and found no entry | - |

## 2. Step 2 result (Question 1): the two obligations and the 2008 statement, in the lane's notation

Marks: READ (a source, with page or equation), DEF, PROVED (by hand here, checked by no one), ARGUED, OPEN, FAILS.

### 2.1 Notation (DEF)

- **Lane objects** (`library/gap-crux-restate.md` L31-45). Torus n = (n_1, ..., n_4), Z(n), the transfer operator T
  of a box, and the twisted partition function Z^(12)(n) = Tr(T^(n_1) C_2) (one stack of (1,2)-plaquettes with the
  flipped weight, one plaquette for each value of (x_3, x_4)). Put

    rho(n) = Z^(12)(n)/Z(n) in (0, 1],   u(n) = (1 - rho(n))/2 (the odd-flux weight of the plane (1,2)),
    Q(n) = (1 + rho(n))/2 in (1/2, 1],   V(n) = - log rho(n),   H(n) = - log Q(n).

  Tomboulis writes Z^(-) for Z^(12), Z^+ = (Z + Z^(-))/2 = Q Z, and F^(-) for V. Row 800 writes R for rho.
- **Class weights.** WW is the set of families c = (c_j), j = 1/2, 1, 3/2, ..., with c_j >= 0 and
  ||c|| := sum_j d_j^2 c_j finite (d_j = 2j + 1). f_c(U) = 1 + sum_j d_j c_j chi_j(U). Z(n; c) is the integral of
  the product over plaquettes of f_c(U_p); Z^(12)(n; c) has f_c(- U_p) on the stack; rho(n; c), u(n; c), Q(n; c)
  as above. Wilson: c_j(beta) = I_(2j+1)(beta)/I_1(beta), and rho(n) = rho(n; c(beta)), because the constant
  factor of the weight cancels in the quotient (READ: T (2.1)-(2.11); Ito and Seiler (2.1a)-(2.1c)).
- **The decimation map** (READ: T (2.17)-(2.22), p. 7-8; d = 4, so zeta = b^2). For an integer b >= 2 and
  r in (0, 1]: M_(b,r)(c) = c' with

    Fhat_j = integral of f_c(U)^(b^2) chi_j(U)/d_j dU,   chat_j = Fhat_j/Fhat_0,   c'_j = chat_j^(b^2 r),   F_0' = Fhat_0^(b^2).

  The **bounding sequence** of a coupling beta: c^U(0) = c(beta), c^U(m) = M_(b,r)(c^U(m - 1)), with bulk factors
  F_0^U(m). (This is the scheme (3.38) of T, in which the upper coefficients evolve on their own; row 797 Section 1.)
  For r < 1 with b^2 r not an integer the power is a power of Fourier coefficients, not a convolution of weights
  (row 797 5.2: positivity of the resulting weight then needs separate care).
- **Tori of the scheme.** Lambda is a torus whose sides are multiples of b^N; Lambda(m) is the torus with sides
  divided by b^m. The stack of Lambda(m) is one stack of coarse (1,2)-plaquettes.

### 2.2 What the construction proves before the disputed step (READ; rows 797 and 799 checked these readings)

- (U) Upper bound, T III.1: Z(Lambda(m-1); c) <= F_0'^(|Lambda(m)|) Z(Lambda(m); M_(b,r)(c)) for c in WW (|.| counts
  the coarse plaquettes), and the same for Z^+. Proved in T on dyadic tori from reflection positivity; r <= 1 only
  raises the coefficients.
- (L) Lower bound with the safe end point (row 797 2.4): Z(.; c) >= 1 = Z(.; 0), and the same for Z^+.
- (M) Monotony, T II.1 and IV: Z(n; c) and Z^+(n; c) do not decrease when a coefficient is raised.
- (I) Separate interpolation, T (3.12)-(3.24) and (4.19): with ctilde(alpha) = w(alpha) c^U(m) (lower end 0),
  w(0) = 0, w(1) = 1, w' > 0, and a bulk factor (F_0^U(m))^(h(alpha, t)), h increasing in alpha from 0 to 1 and
  decreasing in t in [t_a, t_b], there are unique alpha(t) and alpha^+(t) in (0, 1) with

    (F_0^U)^(h(alpha(t), t) |Lambda(m)|) Z(Lambda(m); ctilde(alpha(t))) = Z_fine,
    (F_0^U)^(h(alpha^+(t), t) |Lambda(m)|) Z^+(Lambda(m); ctilde(alpha^+(t))) = Z^+_fine.

  The two level curves are different functions of t.

### 2.3 Ito and Seiler's two obligations, exactly

Sources: Ito and Seiler 0711.4930, Claim 2.1 and (3.1)-(3.11), with the Discussion; 0803.3019 Section 3.2
(Problems 1-3) and 3.3; T p. 19 with footnote 8, (5.14), Appendix C. Fix b, r and a coupling beta.

**(O-flow)_(b,r).** There is an integer n_0(beta) with ||c^U(n)|| <= eps_SC for all n >= n_0(beta), where eps_SC is
a radius below which (i) the small-norm recursion of T II.2 and Appendix D keeps the sequence small, and (ii) the
polymer expansion of the coarse model converges uniformly in the torus (the coarse lemma (K11)-(K16) of row 800
is such a statement for the one-character weight).

Standing, as read. r = 1: a published theorem for SU(N) and U(N) in dimension at most 4 (K. R. Ito, Phys. Rev.
Lett. 55 (1985) 558; quoted as Theorem 2.1 of 0711.4930; not read here). b large and r = 1 - b^(-2): Kanazawa v3
Theorem 4, for every compact connected group, U(1) included, conditional on the Mueller-Schiemann inequalities
(row 797 2.2). Fixed b and fixed r < 1 at all beta: false for the Gaussian model, where beta' = beta/r (Ito and
Seiler 0803.3019 p. 13, a hand calculation), and T's p. 19 claim for SU(2) is asserted there, not proved. The
2008 choice r_m = 1 - eps/(1 + beta_eff(m-1)) (PoS (4.5)): its flow is asserted.

**(O-match)_n.** At the last step n >= n_0(beta) there is t* in [t_a, t_b] with alpha_n(t*) = alpha_n^+(t*).
(Ito and Seiler 0711.4930 (3.2); 0803.3019 Problem 2, (3.4); T (5.14).) Here "Z_fine" and "Z^+_fine" are the
numbers that the first n - 1 steps produce; by T (5.10) their quotient is Q(Lambda) of the original Wilson
model, and nothing else about them is used.

Two side obligations of the printed proof, both made unnecessary by Proposition BR below: Problem 1 (the shifts
t_m of T (5.9) at the steps m < n, which need alpha <= 1 - delta and are the only reason for r < 1) and Problem 3
(the continuation of a root of Psi(lambda, t) from lambda = 0 to 1, which does not follow from Psi_t != 0:
Kanazawa's example, row 797 2.1).

What Ito and Seiler say the proof would have to use (0803.3019 p. 16): the map, the flow and the matching are
the same for U(1) and SU(2); "for large beta and r = 1 such a t* does not exist" for U(1).

### 2.4 Proposition BR: the matching obligation is one inequality between two models (PROVED; found again)

This is check 799's remark B2 ("Appendix C therefore needs an endpoint bracket of the fine ratio by coarse
ratios") written with quantifiers, plus the converse and the consequence for r. No novelty beyond the lane.

**Setting.** Fix the coarse torus Lambda' = Lambda(n), the family ctilde(alpha) = w(alpha) c^U(n) on [0, 1] and
h as in (I). Write Z_c(alpha) = Z(Lambda'; ctilde(alpha)), Q_c(alpha) = Q(Lambda'; ctilde(alpha)),
rho_c(alpha) = 2 Q_c(alpha) - 1, and Q_f = Q(Lambda), rho_f = rho(Lambda) for the fine Wilson model. Z_c and
Q_c are continuous on [0, 1] (a finite lattice, and the character series converges uniformly because ||c|| is
finite). rho_c(0) = 1.

**Statement.**
- (a) For every t: alpha^+(t) - alpha(t) and Q_f - Q_c(alpha(t)) have the same sign (both positive, both zero, or
  both negative).
- (b) (O-match)_n holds if and only if Q_f = Q_c(alpha) for some alpha in the interval I_h = {alpha(t): t in
  [t_a, t_b]}.
- (c) The statement that is consumed, T V.1 (5.17) (PoS (4.12)), is: there is alpha* in [0, 1] with
  rho_f = rho_c(alpha*). It holds if and only if min over [0, 1] of rho_c <= rho_f. In particular it follows from

    **(TB)_n   rho(Lambda; c(beta)) >= rho(Lambda(n); c^U(n)),   that is   u(Lambda) <= u(Lambda(n); c^U(n)).**

  If rho_c does not increase on [0, 1] (T (5.24), which T needs at small coefficients only), then (5.17), (TB)_n
  and T V.2 (5.23) are equivalent.
- (d) So the conclusion of T Section 5 follows from (O-flow) and (TB)_n for one n >= n_0(beta) alone. No
  interpolation h, no parameter t, no shift (5.9), no continuation and no value r < 1 enters. With r = 1 the flow
  is Ito's theorem, so the decimation line has **one** open obligation, (TB)_n at r = 1.
- (e) The 2008 repair. PoS p. 7-8 asks for a solution (t, alpha) of the system (4.9), which is (O-match)_n, by a
  monotone iteration (Meyer) with hypotheses (i) F(x_0) < 0, (ii) (1 + lambda F_x)^(-1) >= 0 entrywise on a
  bounded domain D for lambda in [0, lambda_0], (iii) the iterates stay in D, "assured if at least one component
  of F is positive on" the boundary of D. Its heuristic support is the printed chain (p. 7)

    [Z^(-)(alpha)/Z(alpha)] at alpha = 0  >  Z^(-)(Lambda)/Z(Lambda)  >  [Z^(-)(alpha)/Z(alpha)] at alpha = 1,

  "seen numerically to hold". The right-hand inequality is (TB)_n. If a solution exists in D, then by (b)
  Q_f lies in Q_c of the alpha-range of D. Conversely (TB)_n gives the solution of (5.17) by the intermediate
  value theorem with no iteration. So a trapping domain exists for some admissible h exactly when the bracket
  holds on its alpha-range: **the trapping domain and the endpoint bracket are the same statement**, and its
  non-trivial half is (TB)_n. (Check 799 B5 reached "amount to the endpoint bracket" for (i) and the domain.)

**Proof.** (a) Put G^+(alpha) = h(alpha, t) |Lambda'| log F_0^U + log Z_c(alpha) + log Q_c(alpha). It is the
logarithm of the left side of the second equation of (I), and it is strictly increasing in alpha (T IV.5: Z^+
increases with the coefficients, h with alpha, and F_0^U >= 1). By (I), G^+(alpha^+(t)) = log Z^+_fine and
G^+(alpha(t)) = log Z_fine + log Q_c(alpha(t)). Subtract: G^+(alpha^+(t)) - G^+(alpha(t)) = log Q_f -
log Q_c(alpha(t)).
(b) By (a), alpha(t*) = alpha^+(t*) if and only if Q_c(alpha(t*)) = Q_f. I_h is an interval because alpha(.) is
continuous (T (3.25)).
(c) rho_c is continuous on [0, 1] with rho_c(0) = 1 >= rho_f. The intermediate value theorem gives the first
claim. If rho_c does not increase, its minimum is rho_c(1) = rho(Lambda(n); c^U(n)), which is the right side of
(TB)_n and of (5.23); the left inequality of (5.23) with the end point 0 is rho_f <= 1.
(d) T's use of V.1 and V.2 in his Section 6 is: rho_f >= rho(Lambda(n); c^U(n)) and the expansion at the small
coefficients c^U(n). That is (TB)_n and (O-flow). (e) is (b) and (c). QED

**What the two obligations are, after BR.** (O-flow) is a statement about a map on class functions of the group.
It holds for U(1) and SU(2) alike (Ito; Kanazawa). (TB)_n is a comparison between two lattice models: the Wilson
model on Lambda and the model with the weight f_(c^U(n)) on Lambda(n). It says that the Migdal-Kadanoff model
has the larger odd-flux weight. All the group dependence of the decimation line is in (TB)_n. For U(1) at large
beta and r = 1 it is false for large n, given Ito's flow and the deconfinement bound on tori that Ito and Seiler
state as Theorem 2.2 (2) of 0803.3019 (attributed there to a preprint in preparation; not a lane theorem).

### 2.5 Kanazawa's form of the same obligation (READ row 800; one line PROVED here)

Row 800 (K1)-(K8), (K17), (K21): for a prescribed small coarse weight, the mismatched representation
Q_f = Z_c^+(alpha)/Z_c(alpha_Lambda) always exists, for **every** number Q_f in [1/2, 1], and the mismatch is
D = H_f - H_c(alpha) with 0 <= H_c <= 2 N exp(- l^2). So (K-RESP), the bound [D]_+ <= e_a/8, is the bound
H_f <= e_a/8 + H_c(alpha): up to the explicit coarse error it is the smallness of the fine odd-flux weight
itself, u_f = (1 - exp(- H_f)) . (PROVED: H = - log(1 - u), so H_f <= eps is u_f <= 1 - exp(- eps).) Section 6
below uses this form.

- Step 2 done. In one sentence: after Proposition BR the decimation line is Ito's flow at r = 1 plus the single
  comparison inequality (TB)_n, and (K-RESP) is the smallness of u_f.
