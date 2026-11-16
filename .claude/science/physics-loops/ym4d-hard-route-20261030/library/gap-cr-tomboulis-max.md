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

## 3. Step 3 result: registry grep before the attack (rule 0a), and what is found again

Done at 00:17Z. `library/open-core.md`: no line on Tomboulis, Kanazawa, decimation, Migdal-Kadanoff, a vortex
container, (K-RESP), (SER), (SPR) or a bracket (grep, zero hits). `library/l17c.md`: zero hits. FINISH rows that
name these objects: 47 (list by `awk` on the row text), of which the ones that hold a statement used below are:

| Earlier item | Where | What it holds | Relation to this row |
|---|---|---|---|
| Item 16 of the second brainstorm (row 876) | `library/gap-brainstorm2-max.md` L163, L221 | "The true model differs at bond moving, which bounds Z but not the ratio Z(twist)/Z ... Needs: a sign for the effect of bond moving on the ratio." | **(TB)_n of 2.4 is this need, with quantifiers.** Proposition SIGN (Section 7) answers it for Z_2: no sign. |
| "Carry by decimation inequalities" (row 978) | `library/gap-ladder-max.md` L224 | found again there; "bond moving bounds Z, not the ratio that the seed reads" | same |
| C14, Migdal-Kadanoff sandwich (row 889) | `library/gap-next3-max.md` L361 | REJECTED: "bounds log Z with an extensive error and treats U(1) and SU(2) alike" | the extensive error is Kanazawa's mismatch; 5.2 below says what it is in the lane's variables |
| Form F (row 735) | `library/gap-form-exercise.md` L141-145, L348 | the decimation line as "base, one-way step, sufficiency"; Ito's theorem quoted | Proposition BR is the exact one-way step |
| Numeric guide run of the Migdal-Kadanoff map (row 670) | `library/gap-skeleton-max-b.md` 2.4, item 1 | "The effective coupling ... drops by D = 0.2515 per step at beta = 12, 16, 20 ... c_a = ln 2/D = 2.756. (The true one-loop value is 2.692.)" | the rate of 5.3; a hand derivation of 1/4 is added there |
| Check 799 B2, B5 | `library/gap-tomboulis-check-opus.md` L114-118, L174-186 | the bracket form; the 2008 sign is a convention | Proposition BR (a)-(e) |
| Row 800 (K17), (K21) | `library/gap-kanazawa-astra.md` | the mismatched representation encodes any ratio; D = H_f - H_c | 2.5; Section 6 |
| Row 802 | FINISH row 802 RESULT | "Kanazawa inverse representations exist with F(a) = epsilon at every size, so they give no recursion"; a size recursion needs a quartic exponent | Section 6 does not attempt a size recursion (row 802 holds it) |
| Row 1018 Lemma PAR, Corollary MP, (T-vor), O2 | `library/gap-short-step-max.md` 3.2, 3.4, 7.3, 7.4 | the parallel law on pinned containers; (SER), (SPR) open | Section 6 writes the torus form and reads (K-RESP) through it |
| Row 1017 Theorem CR, Propositions OM, SI, Lemma PT-inf | `library/gap-compact-rigidity-max.md` 3.5-3.7, 4.1 | the limit set Omega | Section 5 |

I do not attack (SER), (SPR), (CAS), (LIOU), (EV-STEP), (BDD-Delta) or a size recursion for the twist free
energy (row 802): each is held by a row. Where a step below reduces to one of them I name the match and stop.

Cross-branch search (main and PR 10114): not run in this row. Rows 797 and 800 ran it for the same names on
2026-11-12 and found only the soft route's Migdal-Kadanoff toy and its literature note. So no item below is
called new beyond this lane's files at fe79776a6.

## 4. Step 4 result (Question 4, run first as the row orders): the tests

Valid form (`parts/gap.md` L196-199): a tool is a hypothesis H with a written proof of "H(M) implies T(M)". A
model M' refutes the tool only if H(M') holds and T(M') fails. Otherwise it says what a proof of H must use.

### 4.1 The three candidate tools of the combination

- **Tool DEC** (the decimation line after Proposition BR). H_DEC = (O-flow)_(b,r) and (TB)_n for all n >= n_0(beta)
  and all admissible tori. Written implication: H_DEC gives the area bound of the odd-flux weight at that
  coupling, u(Lambda) <= u(Lambda(n); c^U(n)) <= C (L_3 L_4/b^(2n)) exp(- kappa L_1 L_2/b^(2n)) (T (6.6)-(6.14),
  whose convergence is cited there, not proved; for a one-character coarse weight row 800 (K18) proves it). Its
  T is therefore **T_flux at one coupling**: the odd-flux weights of the six planes tend to 0 on large tori.
  T_flux is not T_fix, T_per or T_W (4.3).
- **Tool CMP** (the combination asked for in Question 2). H_CMP = "the compactness of Omega supplies (O-match)_n
  or (TB)_n". It has no written implication. Section 5 tests whether one can be written.
- **Tool VOR** (Question 3). H_VOR = Lemma PAR and Corollary MP on containers. Written implications: PAR (iii)
  and MP (row 1018). The question is whether they give (K-RESP).

### 4.2 Three lemmas the table uses (PROVED here; Z_2 in full in Section 7)

**Lemma FAC (the decimation map respects products).** Let G = G_1 x G_2 with the product weight
f(U, V) = f_1(U) f_2(V), f_i positive class functions with non-negative coefficients. Then M_(b,r)(f) =
M_(b,r)(f_1) M_(b,r)(f_2) and F_0' = F_0'^1 F_0'^2. If -1 is a central involution of G_1, the twist by (-1, 1)
has rho(n; f) = rho(n; f_1).
Proof. The irreducible characters of G are chi_j(U) chi_k(V), of dimension d_j d_k. f^(b^2) = f_1^(b^2) f_2^(b^2),
so Fhat_(j,k) = Fhat^1_j Fhat^2_k and chat_(j,k) = chat^1_j chat^2_k, with chat_0 = 1 in each factor. A power of a
product is the product of the powers. The Haar integral over G-valued links factorizes, and the twist changes
f_1 only, so Z^(12) = Z_1^(12) Z_2. QED

**Proposition SIGN (Z_2; proof in 7.2).** For the Z_2 gauge theory with weight 1 + c s_p on a torus whose sides
are multiples of b with quotients at least 3: (TB)_1 holds for all small c > 0, and fails for all c close to 1,
for every r in (b^(-16/9), 1]. In the second range the decimated model has the **smaller** odd-flux weight.

**Estimate RATE (ARGUED: a small-angle computation, not a proof; it agrees with the lane's run).** On SU(2) = S^3
with psi the distance to the identity, the heat kernel is K_tau(psi) = const (psi/sin psi) exp(- psi^2/(4 tau)) up to
images, and convolution adds tau. Then K_tau^zeta = const (psi/sin psi)^(zeta-1) (psi/sin psi) exp(- zeta psi^2/(4 tau)),
and (psi/sin psi)^(zeta-1) = exp((zeta - 1) psi^2/6 + O(psi^4)). So the power is K at 1/(4 tauhat) = zeta/(4 tau) -
(zeta - 1)/6, and b^2 r convolutions give tau' = b^2 r tauhat. With beta = 1/(2 tau) (the Wilson weight is
exp(- beta psi^2/2 + ...)) and zeta = b^(d-2):

    d = 4:  beta' = beta/r - (b^2 - 1)/(3 b^2 r);      d = 5:  beta' = (b/r) beta - (b^3 - 1)/(3 b^2 r).

For d = 4, r = 1, b = 2 the drop is 1/4 per step; the lane's run found 0.2515 (`gap-skeleton-max-b.md` 2.4).
The true one-loop drop per doubling is (11/(3 pi^2)) log 2 = 0.2575 (c_AF = 3 pi^2/11, `gap-ladder-max.md` L65).
For every integer b >= 2 the map is slower than the true flow: log b/Delta_b = 3 b^2 log b/(b^2 - 1) is 2.773
at b = 2, 3.708 at b = 3 and increases, against c_AF = 2.692. For r < 1 the d = 4 map **raises** beta above
beta_c(r) = (b^2 - 1)/(3 b^2 (1 - r)) (this is Ito and Seiler's remark of 0803.3019 p. 13-14 with a number). For
d = 5 it raises beta above (b^2 + b + 1)/(3 b^2) at r = 1.

### 4.3 The table

| Test | Tool DEC (decimation line) | Tool CMP (compactness supplies the parameter) | Tool VOR (PAR and MP give (K-RESP)) |
|---|---|---|---|
| **Lemma PT** (product with a massless factor) | By Lemma FAC the line for the twist of the SU(2) factor is the line of that factor. So H_DEC of SU(2) gives H_DEC of the product, and the product has no seed (Corollary PT1, given the U(1) theorem). **The line reads one factor: as a tool for T_fix or T_W it is refuted GIVEN H_DEC for SU(2); as a tool for T_flux it is not touched.** This is lead rule W2's clause. | Lemma PT-inf (row 1017): the limit forgets every seeded factor and absorbs every bounded one. A parameter read off Omega would be the same for SU(2) and for SU(2) x (seeded factor), but (TB)_n of the product with the diagonal twist is not (rho = rho_1 rho_2). So Omega does not determine (TB)_n. | PAR holds per central involution and says nothing on the other factor (row 1018 6.2). (K-RESP) of the SU(2) factor is unchanged. Not bound; the consumer of (K-RESP) is. |
| **Proposition NP** (D contracts on J doublings, no seed) | The line reads no value of D. As a product with a no-seed factor it is bound as under PT. (TB)_1 at strong coupling: holds for Z_2 at small c (Proposition SIGN); for SU(2) not proved here. | Not bound: NP's limits are those of its Ising factor (row 1017 3.7). | not bound |
| **Theorem D2** (no supremum over tilts) | The line has homogeneous weights and no supremum. Not bound. A proof of (TB)_n through sup-pin boxes would be bound. | not bound | PAR (iii)'s sup form is a supremum over pins: bound. Row 1018 3.4 (caution 2) and 6.2: the sup-pin cost of a thin container is of order beta times its area. So only the moment form of (iii) can feed (K-RESP). |
| **Lemma SHEET** (no uniformity over coupling fields) | (TB)_n compares two coupling fields (the homogeneous one and the moved one). A form "moving plaquettes never raises rho", uniform over fields or groups, is false (Proposition SIGN). The proof must be for the Wilson field and its own image. | not bound | holds for every strength field; blind |
| **Compact U(1)** | (O-flow) holds (Ito at r = 1; Kanazawa). (TB)_n fails at large beta and large n, GIVEN Ito's theorem and the torus bound of Ito and Seiler's Theorem 2.2 (2) (cited, not a lane theorem). At the level of rates: the Villain map at r = 1 is beta' = beta up to terms exp(- c beta), so it drifts to strong coupling for ever, and the true theory does not (Coulomb phase). **A proof of (TB)_n must use that the group is not abelian.** | Omega of U(1) holds a photon limit if D is bounded (row 1017 4.2). No parameter exists there, as it must. | PAR-T (6.1) holds with the Z_2 subgroup; its sup and moment bounds are scale invariant with zero gain (row 1018, Lemma SPLIT). (K-RESP) fails. Blind. |
| **Frozen Z_2, Q_8, 2T** | (O-flow) fails at large beta (row 797 3.1, PROVED there for every finite subgroup). (TB)_1 fails at large beta for Z_2 (Proposition SIGN, PROVED); for Q_8 and 2T the same mechanism is ARGUED in 7.3, not proved. **Both hypotheses fail, so no refutation; a proof of H_DEC must use connectedness twice.** | Omega holds the constants log m. | PAR and MP hold verbatim (row 1018 3.3 (c)); (K-RESP)'s analogue fails for Z_2 above beta = 2.191 (the lane's Peierls bound). **So H_VOR does not give (K-RESP): refuted as a tool.** |
| **Five dimensions** (`gap-crux-fp.md` F15) | (O-flow) fails at large beta by Estimate RATE (ARGUED); T states d <= 4. **The decimation line sees the dimension, through the flow.** This is the one test where it differs from every proved piece of rows 1017 and 1018. (TB)_n in d = 5 is not needed and not known. | The construction is the same with five sides. | PAR-T holds verbatim; blind |

### 4.4 What the tests say, before any attack

1. **DEC is a tool for T_flux at one coupling only.** By Lemma FAC and Lemma PT it cannot give the seed or (W),
   whatever is proved about (TB)_n. Its consumer in the lane is route RE (`parts/gap.md` L159, L177), which
   still needs the even step.
2. **(TB)_n is not blind.** It fails for Z_2 at large beta (PROVED) and for U(1) at large beta (GIVEN). It holds
   for Z_2 at small c. So it is a selective inequality, and it is the only one in the line.
3. **(TB)_n in the range where DEC needs it is the flux half itself.** DEC uses n >= n_0(beta), so the fine torus
   has sides of at least 3 b^(n_0(beta)) lattice units. There (TB)_n says: the odd-flux weight of the true model
   is below that of an explicit strong-coupling model. That is T_flux with a rate. So the step from "T_flux"
   to "(TB)_n" **renames** the flux half of the fixed-coupling crux. By the row's rule this is a FAIL as a step.
   What Proposition BR adds is only that the rename is exact (one inequality, r = 1, no parameter).
4. **VOR is refuted as a tool for (K-RESP)** (frozen Z_2). Section 6 gives the exact identity that replaces it.
5. **CMP has no implication to test.** Section 5 shows why none can be written.

- 00:17Z Step 3 and Step 4 written. Step 5 (Question 2) next.

## 5. Step 5 result (Question 2): does the compactness of Theorem CR or Proposition OM supply the parameter?

**Answer: no. FAILS, with three written reasons (5.1-5.3) and one conditional theorem that says what the
combination does give (5.4).** Everything marked PROVED is by hand here and unchecked.

### 5.1 The compactness the decimation argument needs is already there; what is missing is a sign (PROVED)

By Proposition BR (c) the parameter alpha* exists if and only if rho_f lies in the range of the continuous
function rho_c on the **compact** interval [0, 1]. The range is [min rho_c, 1]. So the only way to fail is
rho_f < min rho_c: a strict inequality at the lower end. No compactness of a domain can turn that sign.

The same in the printed form. Tomboulis's Psi(1, t) is a function of t through alpha(t) only, alpha(.) is
increasing, and by row 797 2.1 Psi(1, t) = 0 is Q_c(alpha(t)) = Q_f. Reparametrised by alpha in [0, 1] the domain
is compact. Kanazawa's example Psi = e^(-t) - 1 + 2 lambda (row 797 2.1) has the same structure: with s = e^(-t)
in [0, 1] it is s - 1 + 2 lambda, the root s = 1 - 2 lambda leaves the compact domain at lambda = 1/2, and
Psi(1, s) = s + 1 has one sign on all of it. A branch is trapped exactly when the end-point sign is right.
The 2008 "bounded invariant domain" is this sign (Proposition BR (e)).

So the row's sentence "by compactness a strict decrease on every element of Omega is automatically uniform"
(check 1019, 6.5 (i)) has no place to act here: (TB)_n is not short of uniformity. For a fixed torus it is one
inequality between two numbers.

### 5.2 The parameter is a Casimir datum of two models, and Omega holds the data of one (PROVED)

**Identity MIS.** Fix h and t. Let A be the fine model with bulk free energy f_A per site, and B(alpha) the coarse
model with weight ctilde(alpha) and bulk free energy f_B(alpha) per site. Let alpha_n be the level parameter of
2.2 (I) for the fine torus b n and the coarse torus n. Put G(alpha) = 6 h(alpha, t) log F_0^U + f_B(alpha). Then for
every torus n

    Delta_A(b n) - Delta_B(n; alpha_n) = |n| (G(alpha_n) - b^4 f_A).

Proof. (I) reads F_A(b n) = 6 |n| h(alpha_n, t) log F_0^U + F_B(n; alpha_n) (a torus n has 6 |n| plaquettes).
Subtract b^4 f_A |n| on the left and f_B(alpha_n) |n| on both sides. QED

Consequences. (a) The left side is a difference of Casimir free energies; the right side is extensive. So a
parameter alpha_inf common to tori n of unbounded volume with bounded Casimir free energies has G(alpha_inf) =
b^4 f_A, and then Delta_A(b n) = Delta_B(n; alpha_inf) on all of them: **a common parameter is the statement that
the fine model at the sizes b n and one coarse model at the sizes n have the same Casimir free energy.** (b) The
same holds with Z^+, so the parameter common to Z and Z^+ on one torus is the statement that they have the same
twisted quotient (this is Proposition BR (b) again). (c) This is Kanazawa's mismatch (row 800 (K2), (K7); row
797 2.3) in the lane's variables: an error of order 1/|n| in alpha is an error of order one in Delta.

What it says for Question 2. The quantities that (O-match) equates are of the kind that Omega records (Delta
and the twisted quotients, Theorem CE (b), (e)). But they belong to **two** models: the trajectory, and an
auxiliary strong-coupling model. Omega is built from the trajectory alone, and by row 1017 3.4 it forgets the
action; the decimation map acts on the action and on nothing else. By Identity MIS it does not even induce a map
on data, because alpha_n depends on the torus. So there is no map on Omega whose invariant set, fixed point or
recurrent point (Proposition OM (c), (d)) could be a trapping domain. Mark: FAILS as a construction; I found no
statement to write.

One check that Omega does not determine (TB)_n (ARGUED): let M be Wilson SU(2) times an SU(2) factor at strong
coupling, with the twist by (-1, -1). Its blow-down limits along a common sequence are those of the first factor
(Lemma PT-inf (ii), with repair D12 of check 1019). Its bracket is rho_1 rho_2 >= rho_1' rho_2' (Lemma FAC), which
holds or fails with the size of the second factor's margin. Two families with the same limits have different
brackets.

### 5.3 The one thing the bracket would give to Omega, and the test against Proposition SI (PROVED as a conditional)

**Setting.** A trajectory (a_j, beta_j) with units u_j (multiples of 4), (BDD-Delta) with a bound D_0, and the
set Omega = Omega(D_0) of row 1017 3.5 with repair D2. Let Omega^gr be the set of limits (Delta_*, zeta_*) of
admissible sequences along which the twisted quotients converge as well (Theorem CE (e)); it is compact and
invariant under the doubling, by the proof of Proposition OM (a) with countably many more coordinates in [0, 1].
For E in Omega^gr and x in DD put u_E(x) = (1 - zeta_E^(12)(x, x, x, x))/2. It is the limit of
u_(j_i)(2^(k_i) u_(j_i) x), the odd-flux weight of the plane (1,2) on the cube of that side. u_E(x) = 0 means that
every level of the cube that is odd under the flip of that plane is at + infinity.

**Hypothesis (DEC-traj).** b = 2. For all large j: (O-flow) holds at beta_j with a step number n_j = n_0(beta_j),
(TB)_(n_j) holds at beta_j on every cube of side N with N/2^(n_j) an integer at least 3, and the coarse models obey
u(N'^4; c^U(n_j; beta_j)) <= g(N') for N' >= 3, with one non-increasing g that tends to 0 (T (6.6)-(6.14) would
give g(N') = C N'^2 exp(- kappa N'^2)).

**Proposition RS (the rate decides).** Assume (DEC-traj). Let (j_i, k_i) be an admissible sequence with limit E, and
put N'_i(x) = 2^(k_i - n_(j_i)) u_(j_i) x.
- (i) If N'_i(1) tends to infinity, then u_E(x) = 0 for every x in DD: E is centre-even on cubes for the plane
  (1,2), and by the symmetry of the sides for every plane.
- (ii) If N'_i(1) tends to 0, the hypothesis gives no inequality for E at any scale.
- (iii) If (RATE): sup over j of 2^(n_j)/u_j is finite, then (i) holds for every element of Omega^gr. If instead
  2^(n_j)/u_j tends to infinity and Omega is not empty, then there are admissible sequences of kind (ii).

Proof. (i) For fixed x and large i, N'_i(x) is an integer at least 3 (u_j is a multiple of 4 and k_i - n_(j_i) +
log_2 x tends to infinity through integers when N'_i tends to infinity). Then (TB) and the coarse bound give
u_(j_i)(2^(k_i) u_(j_i) x) <= g(N'_i(x)), which tends to 0. (ii) For each x, N'_i(x) < 3 for large i, so no cube of
the sequence at the scale x admits n_(j_i) halvings, and (DEC-traj) says nothing about it. (iii) First part:
N'_i(1) >= 2^(k_i)/sup(2^(n_j)/u_j), and k_i tends to infinity. Second part: in the construction of Theorem CE
(i)(b) the index j_i is any large enough member of the subsequence J of Lemma UF; every condition on it holds
for all large j in J. Add the condition 2^(n_j)/u_j > 2^(k_i + i). Then N'_i(x) < x 2^(-i). QED

**The rate (ARGUED, from Estimate RATE and the lane's run).** n_0(beta) is (beta - const)/Delta_2 up to lower
order, with Delta_2 = 1/4 (hand) or 0.2515 (run), so log 2^(n_j) = 2.77 beta_j or 2.756 beta_j. The trajectory has
log u_j = c_AF beta_j + O(log beta_j) with c_AF = 2.692 (`gap-ladder-max.md` L65). So 2^(n_j)/u_j grows like
exp(0.06 beta_j) to exp(0.08 beta_j): (RATE) fails, and the second case of (iii) is the actual one. For r < 1 or
b >= 3 the map is slower still. This is not an accident of the scheme. (TB)_n with (O-flow) gives the bound
sigma_true(beta) >= sigma_MK(beta) for the 't Hooft string tension in lattice units. If a bounding flow were
faster than the true flow, that bound would exceed the true value at large beta (a BELIEF about the true
scaling, not a theorem). So **a one-sided decimation bracket can be true only for a flow that is too slow to
reach a physical size.**

**Reading against Proposition SI.** A kept property holds at every scale of every element of Omega (SI, with
repair D14: the statement is about conditions on a fixed range of scales). The decimation bound starts at the
physical size L_MK(j) = 2^(n_j) a_j, which runs to infinity along the trajectory. In the limit it is a condition
"from the scale X on" with X = lim 2^(n_(j_i))/(2^(k_i) u_(j_i)), and X can be + infinity. So it is not kept. It is
kept exactly under (RATE), and then it is the sigma-invariant property "centre-even". **The property that the
argument needs and the decimation flow does not keep is the unit of length:** the flow has its own scale
2^(n_0(beta)), which is not the trajectory's.

### 5.4 What the combination gives at one coupling (PROVED GIVEN H_DEC; it is the even half, found again)

At one coupling the family is constant, n_0(beta) is fixed, and every admissible sequence has N'_i tending to
infinity. So:

**Corollary EVEN.** Let Wilson SU(2) at one beta have D(a) <= D_0 for a >= a_0, and let H_DEC hold at beta with
b = 2. Then every element of Omega^gr of that coupling is centre-even on cubes. So, with Theorem CE (i)(a) and
Proposition OM (b), (d): the seed at beta holds if and only if there is no centre-even uniformly recurrent
critical element of that coupling.

This is the statement that a flux bound leaves the even sector, in the limit language. The lane holds it as
route RE (the even step, row 731; `parts/gap.md` L114, L159). It is not new, and it does not need the limit:
u tends to 0 directly. It is recorded because it is the complete answer to "what does CR add to the decimation
line": the form of the remaining half, and nothing in the flux half.

### 5.5 Result of Question 2

- The common interpolation parameter and the trapping domain are one end-point sign, (TB)_n (5.1). Compactness
  does not supply a sign. FAILS.
- Omega holds the O(1) data of the trajectory and no action; the decimation acts on actions and its exact
  representation has a torus-dependent parameter (Identity MIS). No map on Omega comes from it. FAILS.
- Given the bracket, its consequence is kept by the limit only under (RATE), and (RATE) fails at one-loop
  order for every integer b (ARGUED). On the trajectory the combination gives nothing. At one coupling it gives
  the even half (Corollary EVEN), which the lane already has as route RE.
- 00:19Z Step 5 done. Step 6 (Question 3) next.
