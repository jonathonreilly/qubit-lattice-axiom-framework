# Check of row 1633 (gap-vir-down-e2-neon.md), FINISH row 1635

Checker: Opus 5.5 (Claude Code). Started 2026-11-27.

## 0. Reading log

- FINISH.md rows 1633 (brief and RESULT) and 1635, read in full.
- `library/gap-vir-down-e2-neon.md` (row 1633, 423 lines), read in full.
- Check 1630 (`library/gap-vir-down-twoside-check-opus.md`), read in full (sections 1 and 3.3 with care).
- Row 1628 (`library/gap-vir-down-twoside-astra62.md`), read in full; tests (19), (20), (22), (23) with care.
- Registry row VIR-DOWN (`library/open-registry.md` L1028).
- Inputs the file cites, read at the cited lines: row 1617 (1), (2), (12) (`gap-vir-down-astra62.md` L15-33, L213); row 1618 Theorem 1, Proposition 6, section 6.4 (`gap-vir-down-neon.md` L72-95, L308-322, L353-360); check 1622 section 2.1 (`gap-vir-down-neon-check-opus.md` L50-60); row 710 Corollary U', Theorems B1, B (`gap-vir-sc.md` L85-106); Lemma ALG and tests (g1)-(g6) (`gap-mech-direction4-fable.md` L180-196).
- Not read: `library/gap-vir-down-e12-check-opus.md` and every other `gap-vir-down-e1*`/`gap-vir-down-e2*` file except the one under check.
- Guide run (not a proof step, not a verification record): one Python process, a few MB, `g1635/guide.py` in this session's scratchpad, outside the repository. It (i) redoes the Bessel brackets of Theorem 2.2(2) in exact `Fraction` arithmetic, (ii) evaluates the 1-plaquette spectrum in floating point at a few couplings.

## 1. The reduction first: Theorem 1.1 (1)-(2)

Notation of the file (0.1)-(0.2): O_t = sum_r r^t Tr(J_r b_r), H_adv(k) = sum_r r^t Tr_D((k m - b^h)_+), H_rise = H_adv(0) = sum_r r^t Tr_D((b^h)_-), h W_t = sum_r m r^t dim D_r.

Redone by hand.
- dim F_r = dim J_r + dim D_r, so sum_r r^t Tr(J_r k m) = k (1 - h) W_t. Hence (0.1) reads B(k) = O_t - k(1 - h) W_t - H_adv(k). HOLDS.
- Scalar inequality (a - x)_+ <= a + (-x)_+ for a >= 0, and (-x)_+ <= (a - x)_+. Functional calculus on each finite block of b^h. HOLDS. So H_rise <= H_adv(k) <= k h W_t + H_rise, which is (1.1).
- Insert in B: B(k) >= O_t - k W_t - H_rise, which is (1.2). HOLDS.

An exact form that the file does not state (PROVED here, one line). Since (k m - x)_+ = k m - min(x, k m),

    B(k) = O_t - k W_t + sum_r r^t Tr_D( min(b_r^h, k m I) ).                    (C1)

So the term k h W_t does cancel exactly: B is the observed response, minus k times the FULL thermal energy, plus the hidden response with each hidden eigenvalue capped at k m. (1.2) drops the capped hidden credit sum_r r^t Tr_D(min((b^h)_+, k m)) >= 0. Adding (C1) to the thermal identity G_beta/t = O_t + H_t gives back row 1628 (20); so (C1) is (20) rearranged.

Verdict on Theorem 1.1(1)-(2): HOLDS. Does k_0 h W_t cancel in row 1628 (19)? Yes, identically, by (C1).

Two qualifications the file omits.
(Q1) The cancellation depends on writing (E1) against the full W_t, as check 1630 3.3 does: O_t >= (k_0 + eps) W_t. That form already contains the hidden-energy charge. Since O_t = (1 - h) c_o W_t, (E1) itself forces h <= 1 - (k_0 + eps)/c_o. So "without any upper bound on h" is true of (E2) only; the bound on h has moved into (E1). If (E1) were written per observed energy (c_o >= k_0 + eps), the term k_0 h W_t would not cancel, and B >= (1 - h) eps W_t - k_0 h W_t - H_rise would need a bound on h.
(Q2) H_rise < eps W_t is sufficient, not necessary. The necessary and sufficient form of the hidden estimate, given (E1) with margin eps exactly, is (C1): sum_r r^t Tr_D(min(b^h, k_0 m)) > -eps W_t.

New or on file. Check 1630 3.3 named (E2) as an upper bound on H_adv(k_0) "for instance rho >= 0". The step from pointwise rho >= 0 to the thermally weighted H_rise < eps W_t is new as a stated corollary. It is one line from (19) and the split of check 1630 3.3.

## 2. Theorem 1.1 (3)-(4)

- (3): Tr_D((b^h)_-) = sup over 0 <= Y <= D_r of Tr(-Y b_r) <= the same sup over 0 <= Y <= F_r = Tr_F((b_r)_-), by row 1628 (7) on a finite block. HOLDS. Elementary.
- (4): row 1617 (2) (L27-33) gives beta b_psi log m / m -> 1 uniformly on the unit vectors of the eigenspaces of one fixed box, so b_psi/m -> 0 (from above). If D_r is nonzero for infinitely many r, the infimum of lambda_min(b^h)/m over them is <= 0. HOLDS, conditional on its hypothesis "D_r nonzero for infinitely many r". This hypothesis is not proved for row 1624's partition; the file's own section 5.2 argues that D may be 0 there. The content is that rho = 0 is the best possible pointwise constant. ON FILE in substance (row 1617 (2); row 1618 Theorem 1(2)).

## 3. Theorem 1.2

**(1) Observed-data no-go. HOLDS.** Redone:
- Infinite delay. B_c(b) = I - (c(b - beta)/(2 r_*)) |g~><g~| with R_beta g~ = lambda_0 r_* g~. Then R'_c = R' - (c/(2r_*))(|g~><R g~| + |R g~><g~|) = R' - c lambda_0 |g~><g~|. Since g~ is orthogonal to Omega, lambda_0' and Omega' are unchanged (R'_c Omega = R' Omega). In Doob coordinates A'_c = A' - c|g><g|, S^0 gains -(Delta A' P + P Delta A') = 2 c r_* |g><g|. E P^a |g><g| P^b E = 0 and J_(r_*) g = 0, so every observed product and every Tr(J_r b_r) is unchanged, while b^h_(r_*) gains -(c/r_*)|g><g|. Positivity of the kernel holds only on |b - beta| < delta_c with delta_c -> 0 as c grows; that is enough for a statement at one point.
- Finite delay L. Dimension count dim ran T*_(L+2) <= (L+3)d < M. With B_c = I - (c(b - beta)/2)|g~><g~|: Delta A' = -(c/2)(|g><Pg| + |Pg><g|), Delta S^0 = (c/2)(|g><P^2 g| + 2|Pg><Pg| + |P^2 g><g|). Every term carries E P^k g with k <= L + 2, which vanishes. Delta b_r = -c|g_r><g_r|. I checked each line.
- Wording. "every E fixed by a nontrivial symmetry" must mean a symmetry that fixes every cell (then the odd states lie in ker E). A symmetry that only permutes the cells does not force D nonzero.
- Scope. As check 1630 2.2 said of row 1629 Corollary 2.2(3): the perturbed family is not a Wilson family, so the no-go says nothing about a test that also uses a Wilson-specific a priori bound such as b >= -9n^3.
- Standing: ON FILE in substance. Row 1629 Corollary 2.2(3) (checked in check 1630 2.2) is the same dimension count and the same rank-one change of S. Row 1628 families A and B are the cold instance. New here: the change is realized as a congruence of the transfer, so it comes from an actual positive transfer family; and it is stated for H_rise. The file's duplicate check ("None of the theorems proved below appears on file", L18) is wrong for this item.

**(2) Four-state family. HOLDS.** Entries (1/4)(1 + r_1 + 2r_2), (1/4)(1 + r_1 - 2r_2), (1/4)(1 - r_1): positive. G < 3e^-3 < 3/20 (e^3 > 20 from the 9-term series, which sums to 20.009). 400 * 625 = 250000 > 241753 = 529 * 457. h < 1/4 and O_t = 2 k_0 (1 - h) W_t > (3/2) k_0 W_t. B = k_0 m_1 e^(-t m_1) - 2(k_0 + M) m_2 e^(-t m_2) > (2/3) k_0 m_1 e^(-t m_1). Content: a heavy hidden level that rises fast is harmless because r^t suppresses it. This is immediate from (1.2). New example, small content.

**(3) Six-state family. HOLDS.** Redone. Operator matrices: Pi has entries 1/6; |f_1><f_1| has +-1/6; E_a has 2/3 and -1/3 on C_a. With r_1 = r_2 >= r_3 the entries are (1 + r_1 + 4r_2)/6, (1 - r_1)/6, (1 + r_1 + 4r_3)/6, (1 + r_1 - 2r_3)/6 >= (1 - r_1)/6, and (1 - r_1)/6 across: all positive. t m_1 = a e^(-5 k_0 x) >= a e^(-5 k_0 w) = 4, t m_3 >= a >= 4, G <= 5e^-4 < 1/10 (2.7^4 = 53.1441). 62500 > 55297. At x = 0 the eigenspace is 5-dimensional, J = span f_1, D = ran E_a + ran E_b, h = 4/5, W_t = 5 m_0 r^u; b_r = 6k_0 m_0 (f_1 and E_a), -2k_0 m_0 (E_b). O_t = 6 k_0 m_0 r^u = (6/5) k_0 W_t; H_t = 8 k_0 m_0 r^u; H_adv = 2 * 3 k_0 m_0 r^u; B = 6 - 1 - 6 = -1 in units k_0 m_0 r^u, so B = -(1/5) k_0 W_t. Consistent with (C1): O_t - k_0 W_t = (1/5) k_0 W_t, capped hidden term = r^u (2 k_0 m_0 - 4 k_0 m_0) = -(2/5) k_0 W_t; sum -(1/5). Content: fast-falling hidden levels give at most k_0 m of credit each. This is the mechanism of row 1628 (20) and of check 1627 1.1's corollary ("a faster one gives no credit"). New example of an ON FILE mechanism.

## 4. Theorem 2.1 (compact Gaussian U(1) with magnetic flux)

**The model.** R_el (x) R_mag (x) R_phot, with flux energies |Q|^2/(2 beta n), Q in (2Z)^3, and magnetic energies 2 pi^2 beta |M|^2/n, M in Z^3. The magnetic factor is check 1622 section 2.1's correction of row 1618's model (L52-55 of that check: the zero-monopole sector contains the P_0-neutral flux sectors M). I accept the model as ON FILE from check 1622. The theorem is a theorem about this product operator.

**(1) HOLDS, with one sharpening.** Flat-shift invariance puts every Q != 0 state in ker E (row 1626 (12)-(13), check 1627 1.8); F_r commutes with the shift, so the Q != 0 part of each F_r lies in D_r. The eigenbasis is fixed, so b = -m' = |Q|^2/(2 beta^2 n) - 2 pi^2 |M|^2/n on each state; this is eigenspace-diagonal and therefore convention-free (check 1630 2.2). Negative iff |Q| < 2 pi beta |M|. (2.2): b >= -2pi^2|M|^2/n >= -m/beta, and Q = (2,0,0), nu = 0, |M| -> infinity gives b/m -> -1/beta. HOLDS. Sharpening: the restriction beta > 1/pi is not needed. For every beta > 0 the states Q = (2,0,0), |M| > 1/(pi beta) rise, and (2.2) holds at every beta > 0.

**(2) HOLDS.** Redone: 6 e^-x <= G_el <= 4/21 gives x >= log(63/2) > 3.4; W_t >= (12/(beta n)) e^-x; (b)_- <= (2pi^2|M|^2/n) 1_(M != 0); (1 + G_el)(1 + G_ph) <= 25/21 < 5/4; y = pi^2 beta^2 x; shell count 24 r^2 + 2 <= 26 r^2 with r^2 <= |M|^2 <= 3r^2; r^4 <= e^(4(r-1)), r^2 - 1 >= 3(r - 1), so the shell sum is < 156 e^-y; 390 pi^2/12 < 330; and 3.49 beta^2 - beta + 0.6 >= 52 > log 1320 at beta >= 4. Each step checks.
Standing: the suppression e^(-3.4 pi^2 beta^2) of the magnetic weights on cold tori is ON FILE as ARGUED/GUIDE (check 1622 L55, the checker's own remark). New: the hidden rising levels in D_r, and a hand proof of the bound for H_rise/W_t.
Relevance: in this model (E1) fails outright (O_t = 0, section 8 below), so the small H_rise does not help it pass.

## 5. Theorem 2.2 (1- and 2-plaquette Wilson SU(2))

**(1) Limit (2.4). HOLDS.** Redone:
- Bessel ratio I_(n+2)/I_n < 1/(1 + 2(n+1)/beta) from I_n - I_(n+2) = (2(n+1)/beta) I_(n+1) > (2(n+1)/beta) I_(n+2). The three cases of (2.6) check: log(1+u) >= u/2 on [0,2] by concavity; k^2 <= 5m(m+1); (k+1)^2 <= (9/4)k^2; 16/45 > 1/3; the large-m case gives e^(-(k-1)) <= e^(2 - 2 xi) at beta >= 4.
- Pointwise limit sqrt(beta) e^-beta I_n(beta) -> e^(-xi^2/2)/sqrt(2 pi), so g_beta -> e^(-2 xi^2). The kernel limit is e^(-(x^2+y^2)/4) times the odd heat kernel e^(2 d^2), i.e. (8 pi)^(-1/2)(e^(-(x-y)^2/8) - e^(-(x+y)^2/8)). The HS majorant uses beta sin^2(x/(2 sqrt beta)) >= x^2/pi^2.
- Spectrum. After the dilation the kernel is (2pi)^(-1/2) exp(-(3/2)(x^2+y^2) + xy). For the Mehler kernel sum z^(n+1/2) psi_n psi_n with Hermite scale b, the quadratic form is b[(1+z^2)(x^2+y^2) - 4 z x y]/(2(1-z^2)). So (1+z^2)/(4z) = 3/2, z = 3 - 2 sqrt 2, and b = (1/z - z)/2 = 2 sqrt 2; Mehler's prefactor for sum z^n psi_n psi_n is (b/(pi(1-z^2)))^(1/2), and b/(1-z^2) = 1/(2z) because 1 - z^2 = 4 sqrt 2 z; so sum z^(n+1/2) psi_n psi_n has prefactor (2pi)^(-1/2), as required. I re-derived each constant. Odd n only: lambda_0/lambda_1 = z^(-2) = 17 + 12 sqrt 2, m_1 -> 4 log(1 + sqrt 2) = 3.5255.
- GUIDE (floating point, character basis truncated at 60-120 spins): lambda_0/lambda_1 = 45.64, 26.57, 25.35, 25.56, 28.36, 30.82, 32.98 at beta = 2, 3, 3.5, 4, 6, 10, 30; the limit is 33.97. Consistent with (2.4).

**(2) Rational bound (2.5). HOLDS.** Redone in exact Fraction arithmetic (guide script; the hand inequalities are each rational and I also checked them by hand):
- Six-term sums S_0 = 4.880530..., S_1 = 3.953314...; r = 6 terms 6561/26214400 and 5.363e-5; geometric tails < 0.000263 and < 0.0000559. So I_0(3) in [4.8805, 4.8809] and I_1(3) in [3.9533, 3.9534]. HOLD.
- Recurrence brackets I_2 in [2.2449, 2.24537], I_3 in [0.95948, 0.9602], I_4 in [0.3245, 0.32642]: inside the file's [2.2449, 2.2454], [0.9594, 0.9602], [0.3245, 0.3266]. HOLD.
- 2x2 block: a in [2.63553, 2.6356], b <= 0.96579, c in [0.47349, 0.47417]; det >= 0.31514, Tr <= 3.10977 (the file's coarser 0.3119 and 3.1104 also hold). lambda_1 >= 0.10134 by Cauchy interlacing (lambda_1 of the full positive compact operator >= the smaller eigenvalue of a 2x2 principal block, by min-max).
- Trace tail: m = 2 term < 0.01699; m >= 3 terms < 0.00193 (rho_m <= (3/2)^m/(m+1)!, ON FILE row 1617/check 1621 1.1; float-checked for m = 3..9). Tr < 3.12868.
- lambda_0/lambda_1 < Tr/lambda_1 - 1 < 29.88 from the file's own brackets propagated exactly, below the file's 30.24 and below 31. 17 + 12 sqrt 2 > 33.92. HOLDS. The step from L_el = C^2 M^2 C^2 to T = M C^4 M (same nonzero spectrum, AB and BA) and the matrix element e^-3(I_|m-n|(3) - I_(m+n+2)(3)) check.
- The GUIDE value at beta = 3 is 26.57, so the bound 31 is honest with room.

**(3) Rising level. HOLDS.** m_1 is continuous and piecewise analytic on compacts (lambda_0 simple by positivity; finitely many analytic branches near lambda_1 on a compact interval). m_1(3) < log 31 < lim m_1, so some beta_2 > 3 has m_1(beta_2) > m_1(3), and on one analytic piece m_1' > 0 on an open interval I_*. There b = -m_1' < 0 on the whole first eigenspace (constant multiplicity, so F A' F = lambda_1' F). The cold-t statement: the tail bound sum (r_i/r_1)^t |b_i| <= r_1^(-1) e^(-(t-1) Delta) ||A'||_1 checks. 2-plaquette product: F^(2)_(r_1) = F (x) 1 + 1 (x) F; for E reading plaquette 1 only, F^(2)(g_1 (x) 1) = (F g_1) (x) 1, so 1 (x) F lies in D; the cross blocks of b vanish because <1, A' 1> = 0 and <1, A f> = 0; so b^h = -m_1' I on D. HOLDS.
Scope. These are a single plaquette and a decoupled product, not a periodic torus. The hidden block in the product exists by construction (the observation ignores plaquette 2). In the product the observed block rises too, so (E1) fails there as well.
Standing: b_1 < 0 in 1-plaquette SU(2) is ON FILE as GUIDE (row 710 section 5; row 1618 section 6.4, floating point). New: the hand proof (limit and rational bound) and the product construction.

## 6. Lemma 3.1 and Theorem 3.1 (strong coupling)

**Lemma 3.1. HOLDS.** v_0 and v_psi are unit vectors with <v_0, v_psi> = sqrt(lambda/lambda_0) <Omega, psi> = 0 (P_0 commutes with M and C). w_phi(0) = |<1, v_phi>|^2 because Pi_0 is the projection on constants. Bessel gives w_Omega(0) + w_psi(0) <= 1. N(j) >= 4 for j != 0 with Pi_j H_0 != 0: every vertex of the support S has S-degree >= 2 (a single nontrivial irrep has no invariant), so |S| <= 3 forces a 3-cycle, which exists only for n = 3 as a wrapping line; centre neutrality makes 2j even there and the degree-2 vertices force equal spins, so N >= 6. If |S| >= 4, N >= |S| >= 4. Each step checks.

**Theorem 3.1. HOLDS.** Redone from row 1618 Theorem 1(1) (L76-87): beta D = <N>_w - beta<R>_w - beta<V_1>, with 0 < R < 3n^3, 0 <= V_1 <= 6n^3. c_j/c_0 <= (beta/4)^N from rho_k <= (beta/2)^k/(k+1)! and 2^k <= (k+1)!; N(beta/4)^N decreasing for N >= 4 at beta <= 2; lambda_0 >= c_0^(3n^3) e^(-6 beta n^3) from the constant trial vector. So beta b >= 4 - 8 e^(6 beta n^3)(beta/4)^4 - 9 beta n^3 > 1/2 at beta <= 1/(3n^3) (e^2 < 8, (1/324)^4 < 10^-10). b_r > I/(2 beta) on each eigenspace because every unit vector of an eigenspace is an eigenvector.
Scope: beta <= 1/(3n^3) tends to 0 on the trajectory. Non-selective, as the file says: the proof reads the compact spin gap N >= 4 and the box volume, both present in 4D Wilson U(1) and in 5D SU(2) (I did not redo those two variants; ARGUED).
Standing: the inputs are ON FILE (rows 1617, 1618). Row 710 Theorems B1, B prove the opposite-direction bound (LEV_K, an upper bound on -E') at s b^3 <= 1/10. I found no earlier statement of the lower bound b > 1/(2 beta) for all excited neutral levels. New, by my search of rows 710, 1617, 1618, 1628 only.

## 7. Theorems 4.1 and 4.2 (all-coupling pieces)

**4.1(1) HOLDS.** g(k) - g(k-1) = 1/beta + I_(k+2)/I_(k+1) - I_(k+1)/I_k = d/dbeta log(I_(k+1)/I_k) > 0 (row 1617 (12), L213, moment identity). g(0) = I_0/I_1 - 2/beta - 1 > -min(1, 2/beta). a_0^tau >= 0 because the kernel of C' is -a(g) c(g) <= 0 and Omega > 0. The split b = b^tau + b^sigma checks (the M-derivative gives -lambda<psi, V_1 psi> since M commutes with V_1 and MCM psi = lambda psi). ON FILE in substance (row 1617 (12); row 1618 Lemma 1).

**4.1(2) HOLDS.** psi = lambda^(-1/2) M C^(1/2) w with ||w|| = 1; <psi, e^(hV_1) psi> = lambda^(-1) <w, C^(1/2) M_(beta-h)^2 C^(1/2) w> <= ||M_(beta-h) C M_(beta-h)||/lambda, and the norm on the full link space is the neutral Perron value (positive kernel, symmetric Perron vector). Jensen and the Taylor remainder for the convex f(s) = log lambda_0(beta, s) check (convexity: limit of (1/t) log of positive combinations of Laplace transforms in s). New.

**4.1(3) HOLDS.** a(g) = ||g - I||^2/4; a(uv^-1) <= 2a(u) + 2a(v); a(U_p) <= 4 sum a(g_r); each spatial link lies in 4 spatial plaquettes, so V_1 <= 16 sum_e a(U_e). Product trial vector gives lambda_0 >= (c_0(11 beta)^2/c_0(2 beta))^(3n^3); the scaling c_0(ks) >= 32/(pi^5 k^(3/2)) c_0(s) (k >= 2) checks line by line (2/sqrt k <= pi/2; sin(phi/2) >= phi/pi; sin theta >= 2 theta/pi); 2048 sqrt 2/(1331 pi^10) = 2.32e-5 > e^-11 = 1.67e-5, and the file's integer chain (pi^10 < 10^5, 2048 sqrt 2 > 2867, e^11 > 57563 > 46425) checks. Note the file uses c_0 for both (2/beta) e^-beta I_1(beta) and the one-link integral of e^(-beta a); they are equal. New.

**4.1(4) HOLDS.** h = beta in (4.2) gives <V_1>_psi <= (m + 33n^3)/beta; min(a_1, b_1) + min(a_2, b_2) <= min(a_1 + a_2, b_1 + b_2) gives (4.5); (4.6) uses m t >= log 2. It improves -9n^3 only when beta > 39/9 + m/(9n^3). At cold points on the trajectory (t >= n/512, beta ~ log n) the floor in (4.6) is of order n^4/log n times m: useless for (E2), as the file says ("still extensive").

**4.2(1) HOLDS.** Row 1617 (1) (L21-24) gives Pr_w(Y >= L - 6 beta n^3 - log 2) >= 1/2 with L >= m. Y <= 3 beta n^3 + N(log(N+1) + log_+(2/beta)) from c_(k/2) >= e^-beta (beta/2)^k/(k+1)! and (k+1)! <= (k+1)^k. So m >= Lambda_* forces Pr(N > 18 beta n^3) >= 1/2, <N> > 9 beta n^3, and beta b >= <N> - 9 beta n^3 > 0. Standing: positivity of high levels is ON FILE qualitatively (row 1617 (2), row 1618 Theorem 1(2)); the explicit threshold Lambda_* is new. Lambda_* ~ 18 beta n^3 log(beta n^3), so its levels carry weight below e^(-t Lambda_*) at cold points; it is not a step toward (E2).

**4.2(2) HOLDS.** The split at Lambda, monotonicity of e^(-(1-alpha)tx) and x e^(-(1-alpha)tx) for x >= 1/((1-alpha)t), and W_t >= m_1 e^(-t m_1) check. Standing: ON FILE in substance as row 1618 Proposition 6 (L308-322): the same split, the same hypothesis G(t/2) <= M_0, the same monotonicity, with 9|B| + kappa Lambda in place of min(9n^3, (Lambda + 39n^3)/beta). The file read row 1618 in full but does not cite Proposition 6; its duplicate claim fails here too. "Reducing (E2) entirely to the low-energy window" is conditional on a bound M_0 for G(t/2) that is not proved on the band.

## 8. Item 2: the reduced (E2), and one estimate or two

The reduction holds (section 1). The reduced estimate, at every cold point (G <= c_col) of the k_0-characteristic on [beta_K, beta_(K+r)], l = L_h b^r, r fixed before K, for the infinitely many K of check 1630 3.3, uniformly in K:

- (E1) O_t = sum_(0<r<1) r^t Tr(J_r b_r) >= (k_0 + eps) W_t   (unchanged; W_t is the FULL thermal energy);
- (E2, reduced) H_rise = sum_(0<r<1) r^t Tr_(D_r)((b_r^h)_-) < eps W_t   (sufficient);
  necessary and sufficient, given (E1) exactly at margin eps: sum_(0<r<1) r^t Tr_(D_r)(min(b_r^h, k_0 m I)) > -eps W_t, by (C1).
- and (RB) of check 1630 1.3(d), and (HOT) at the hot box.

One or two? Still two estimates, on disjoint data: (E1) reads the J-blocks; (E2) reads only the negative part of the D-blocks. They are coupled only through eps. The reduction does not merge them. Their conjunction gives the one inequality

    sum_r r^t [ Tr(J_r b_r) - Tr_(D_r)((b_r^h)_-) ] > k_0 W_t,                       (C2)

which is sufficient for B(k_0) > 0 and, since H_t >= -H_rise, implies (VIR-down) at rate k_0 (with m in place of e^m - 1, as in (11) of row 1628). (C2) is strictly stronger than (VIR-down) (it discards hidden credit).

A degenerate case the lead should know (PROVED, one line). If the infinite-delay closure J of the loops is everything (D = 0), then (E2) is empty and (E1) is G_beta/t >= (k_0 + eps) W_t, i.e. (VIR-down) with a margin: one estimate, equal to the target, no progress (row 1628 L227). Row 1633 section 5.2 ARGUES that D = 0 is the generic case for row 1624's partition (no exact symmetry fixes every cell). I have not checked that argument. So (E2) has content only for finite-delay tests (row 1628 (16), row 1629 (2.12)-(2.13)) or for observations with an exact symmetry that fixes every cell.

## 9. Item 3: "all selectivity sits in (E1)"

**What is proved.** (E2), in either form, holds identically in the free photon (b = 0), in zero-flux compact Gaussian U(1) (b = e_Q/beta >= 0), and in the Villain zero-monopole sector with flux at beta >= 4 and cold points (Theorem 2.1(2)). The (g4) computation in section 5.1 HOLDS: with a beta-independent spectator, T_rise^prod = (1 + G_sp) T_rise and W_t^prod >= (1 + G_sp) W_t, so the ratio can only fall; and b_i/(m_i + e_j) >= b_i/m_i when b_i <= 0. So, by Lemma ALG (row 1553), (E2) cannot be the step that separates SU(2) from these models. The chain (E1) + (E2) + (RB) + (HOT) => (VIR-down) => (PUR-io) fails in them, so it fails at (E1), (RB) or (HOT).

**HOLDS AFTER CORRECTION.** The claim should read: "Against the free photon, compact Gaussian U(1) and (g4), (E2) is not selective; the selective step must be (E1), (RB) or (HOT)." The file's table (section 5.1) says "and in (RB)"; its RESULT and FINISH's summary drop it. For (g1) proper (interacting weak Wilson U(1)) and (g2) (weak 5D SU(2)) nothing about (E2) is proved; the file's table entries there are ARGUED or open. A non-selective (E2) is not a defect: a proof may contain non-selective steps if one step is selective.

**What (E1) must read.** At every cold point of the window, uniformly in K:
(i) An order-one rate. (E1) asks the loop-visible cold levels to fall with beta at a rate at least k_0 + eps, measured against the FULL thermal energy. In compact Gaussian/Villain U(1) with contractible flowed loops, J lies in the zero-charge sector (flat shift, row 1626 (12)-(13)), where every eigenspace block of b vanishes (free photon; eigenspace-diagonal, so convention-free, check 1630 2.2). So O_t = 0 and (E1) fails at every point, for every k_0 + eps > 0. This reads the law (no running of the zero-charge dispersion) and a symmetry. In interacting weak Wilson U(1) the expected visible rate is O(1/beta) (ARGUED, not proved), and a c/beta rate is not selective (row 1618 Theorem 2, check 1622). So (E1) must give a rate bounded below uniformly in K, not one that decays like 1/beta_K.
(ii) Four-dimensional running. On the weak part the rate must come from asymptotic freedom of the box coupling at the fixed sides L_h .. L_h b^r (b of order c m, c = 3 pi^2/11, check 1453 at the slope level), and on the band from a non-perturbative order-one statement. Weak 5D SU(2) has no asymptotic freedom; its visible levels are expected to have rate O(1/beta) there (BELIEF; (g2) is open in rows 1628, 1629, 1633 and check 1630 3.1).
(iii) No beta-independent light energy. In (g4) with the observation on the SU(2) factor, J^prod = J (x) |1><1|, so O_t^prod = O_t while W_t^prod = (1 + G_sp) W_t + (1 + G) W_t^sp. (E1) fails once the spectator is light (row 1628's spectator paragraph gives a cold point with B <= -13/(42 w t), and (E2) passes there). So (E1) must read that the whole cold spectrum of the law carries no thermal energy in beta-independent neutral levels. No property of "algebra su(2), d = 4" decides this (Lemma ALG).
(iv) The hidden-energy price. Because W_t includes the hidden energy, (E1) implies h <= 1 - (k_0 + eps)/c_o. In compact U(1) with contractible loops all Q != 0 sectors are hidden; in SU(2), (E1) needs the loops (with all delays) to see, or to be paid by, almost all cold thermal energy.
(g3): line (i) does not fire in strong-coupling 4D U(1), where zero-charge levels depend on beta; this is ARGUED in row 1629 and check 1630 3.1, not proved. I agree with it as ARGUED.
So the brief's selective step is wholly inside (E1), and, by section 8, if D = 0 then (E1) is (VIR-down) itself.

## 10. Item 4: new and on file

| Statement (row 1633) | Verdict | Standing |
|---|---|---|
| Thm 1.1(1)-(2): sandwich, cancellation, H_rise < eps W_t suffices | HOLDS (qualifications Q1, Q2 of section 1) | New as a stated corollary; one line from row 1628 (19)-(20) and check 1630 3.3. Exact form (C1) added here |
| Thm 1.1(3) H_rise <= T_rise | HOLDS | New, elementary (row 1628 (7)) |
| Thm 1.1(4) ceiling rho <= 0 | HOLDS, conditional on D_r nonzero infinitely often | ON FILE in substance: row 1617 (2), row 1618 Thm 1(2) |
| Thm 1.2(1) observed-data no-go | HOLDS | ON FILE in substance: row 1629 Cor 2.2(3) (check 1630 2.2), row 1628 families A, B. New: congruence realization |
| Thm 1.2(2) 4-state family | HOLDS | New example; small content |
| Thm 1.2(3) 6-state family | HOLDS | New example of row 1628 (20) / check 1627 1.1 corollary |
| Thm 2.1 U(1) with magnetic flux | HOLDS (rising levels exist at every beta > 0, not only beta > 1/pi) | Model and e^(-3.4 pi^2 beta^2) suppression ON FILE as ARGUED/GUIDE (check 1622 2.1); hand proof and hidden rising levels new |
| Thm 2.2 1-, 2-plaquette SU(2) | HOLDS (limit, rational bound redone exactly: ratio < 29.88 < 31) | b_1 < 0 ON FILE as GUIDE (row 710 5, row 1618 6.4); hand proof new |
| Lemma 3.1, Thm 3.1 strong coupling | HOLDS | New conclusion (my search: rows 710, 1617, 1618, 1628); inputs ON FILE; non-selective |
| Thm 4.1(1) electric floor | HOLDS | ON FILE in substance (row 1617 (12), row 1618 Lemma 1) |
| Thm 4.1(2)-(4) anisotropic Perron, 33 n^3 gap, combined floor | HOLDS | New; still extensive, no use for (E2) on the trajectory |
| Thm 4.2(1) Lambda_* | HOLDS | Qualitative ON FILE (row 1617 (2)); explicit threshold new |
| Thm 4.2(2) localization | HOLDS | ON FILE in substance: row 1618 Proposition 6, not cited |
| Selectivity of (E2) | HOLDS AFTER CORRECTION (section 9) | Dispersions ON FILE (row 1618 Thm 2, row 1624 (18)); (g4) ratio new, elementary |
| Section 5.2 (D = 0 generic; 2-gluon rising levels; locality wall) | ARGUED | Not checked here |

Overclaims and wording (none changes a theorem):
1. L18 "None of the theorems proved below appears on file": false for Thm 1.2(1) (row 1629 Cor 2.2(3)) and Thm 4.2(2) (row 1618 Proposition 6); Thm 4.1(1) is row 1617 (12).
2. "without any upper bound on h": true of (E2) only; check 1630's (E1) already contains the bound h <= 1 - (k_0 + eps)/c_o.
3. "all selectivity sits in (E1)": should read "(E1), (RB) or (HOT)", and only against the models where (E2) is proved.
4. Thm 2.1: "for every beta > 1/pi" is true but not sharp.
5. Thm 2.2 "a cold Wilson SU(2) system": one plaquette or a decoupled pair, with a hidden block made by the choice of observation. The file's scope note says so.

What moved: nothing on the critical path. The hidden estimate is now a thermally weighted one-sided bound (H_rise < eps W_t) instead of pointwise rho >= 0. All the difficulty, and all the selectivity, are in (E1); if the loops' delay closure hides nothing, (E1) is (VIR-down) itself. (VIR-down) on the band, (HOT), (PUR-io) and the gap stay open. Same-route note: my check is a reading by hand of the author's route; the only different data path is the exact-fraction and floating-point guide run of section 0, which is not a proof.

## RESULT

Reduction (Thms 1.1-1.2) HOLDS: k_0 h W_t cancels identically; exactly, B = O_t - k_0 W_t + sum r^t Tr_D min(b^h, k_0 m) (new form here).
So with (E1) O_t >= (k_0+eps)W_t, H_rise < eps W_t suffices. Caveat: (E1) in check 1630's form already forces h <= 1-(k_0+eps)/c_o.
Reduced (E2): H_rise = sum r^t Tr_D((b^h)_-) < eps W_t (sufficient). (E1) and (E2) stay two estimates on disjoint data, joined
only by eps; together they give (C2) sum r^t [Tr(J b) - Tr_D((b^h)_-)] > k_0 W_t. If D = 0, (E2) is empty and (E1) is (VIR-down).
Thms 1.2(1)-(3), 2.1, 2.2, 3.1, 4.1, 4.2 and Lemma 3.1 all HOLD; no line fails. Bessel bound redone in exact Fractions:
lambda_0(3)/lambda_1(3) < 29.88 < 31 from the file's brackets (float guide 26.57); limit 17+12 sqrt 2 re-derived via Mehler.
Thm 2.1: rising hidden levels exist at every beta > 0 (sharper than beta > 1/pi). Thm 2.2 is a plaquette toy, not a torus.
On file in substance: Thm 1.2(1) (row 1629 Cor 2.2(3)), Thm 4.2(2) (row 1618 Prop 6), Thm 4.1(1) (row 1617 (12)), Thm 1.1(4)
(row 1617 (2)); the file's "none on file" claim is wrong. New: (1.3) as a corollary, Thms 2.1-2.2 hand proofs, Lemma 3.1/Thm 3.1,
Thm 4.1(2)-(4), explicit Lambda_*. Selectivity HOLDS AFTER CORRECTION: (E2) is not selective (photon, Gaussian U(1), (g4));
the selective step must be (E1), (RB) or (HOT). (E1) must give an order-one, K-uniform visible rate from 4D running, with no
beta-independent light energy; U(1) has O_t = 0, 5D lacks running (belief). Nothing on the critical path moved.
