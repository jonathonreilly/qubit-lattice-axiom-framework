# Gate report: field tier of upper-chain (Text 14, Text 16)

**Provenance.** Reviewer Opus 5.5 at high effort, checking text written by Opus 5.5 at max effort. This is a same-model check, not an independent one. Snapshot at commit c3242879df, the three part files. Scripts: `checks/gate_ft_virial.py`, `checks/gate_ft_rough.py`, each under a minute, deterministic. Nothing in the repo was edited.

Line numbers are lines of `upper-chain.md` unless a file is named.

## Overall verdict

The chain has three parts, and they come out differently.

1. **From the first-order mark to (SM): holds.** Theorem 14.1b is exact. Theorem 14.1c is right given its hypotheses, with one input (the fibre derivative) not delivered by the stated chain (D6).
2. **Regular tier of the mark: holds, and it is a real advance.** Lemma 14.10, the identity in Lemma 14.16, the recursions for z, rho, r in Theorem 14.13, Lemma 14.15(a), (b). The source a_(j+1)/l against an operator of norm below L is correct, and the geometric sum is right. No circularity in the order of constants.
3. **Rough tier: Lemma 14.15(c) is wrong as stated, and (K3) is not preserved by the block map.** There is an explicit element of the input class whose image violates (K3), by a factor L^(4+4C) on a coarse field with only of order D rough cells. So the author's worry understated it: the failure starts at N' of order D, not at astronomically large N'. Theorem 14.13 therefore does not yet deliver (TR_p), since the telescoped form and Step 1 of Lemma 14.15(a) both consume (K3).

The rough-tier failure is pointwise. Fields that cause it are rare under mu, so I do not think the tier is dead, but "should cost nothing in L^p" is not a one-line remark: a plain L^p bound fails, and the class has to change (Item 3).

UV-OS is not an empty reduction. It also is not strictly smaller than UV-CT: the two are logically incomparable (Item 6). Its clause (GS_j)(e3) is false as stated in the free theory (D5), and neither hard-core attempt comes near it (Item 7).

## Verdicts by item

| Item | Statement | Verdict | Delivers |
|---|---|---|---|
| 1 | Lemma 14.10 | ADVANCE | exact identity consumed by Lemma 14.16 |
| 2 | Theorem 14.13, z, rho, r in (K1) | ADVANCE, regular tier | the (K1) part of the mark |
| 2 | Theorem 14.13, (K2), (K3), and hence (iii) in L^p | WRONG as stated (inherits Item 3) | not yet (TR_p), (TR'_p) |
| 3 | Lemma 14.15(a), (b) | ADVANCE, given clauses and input (K3) | Theorem 14.13 |
| 3 | Lemma 14.15(c), (K2) | Correct under (G1). (G1) is available to neither attempt (D3) | conditional |
| 3 | Lemma 14.15(c), (K3) | WRONG | nothing |
| 4 | Lemma 14.16 | ADVANCE. One-loop cancellation derived, the g^4 residue conditional on (C2), (Q) | z recursion |
| 5 | Theorem 14.1b | ADVANCE | (SM) from (TR_n), (CC_n), the assembly gap of mapped |
| 5 | Theorem 14.1c | ADVANCE given hypotheses; derivative half of (TR'_p) not delivered (D6) | (CC_n) |
| 6 | UV-OS as interface | CORRECT-NO-ADVANCE as an interface until fixed: not strictly smaller than UV-CT, one clause false, class in (Q_j) tied to (K3) | conditional |
| 7 | Fit claim in Text 16 | Partly accurate, four entries overstated (D3, D8) | |

## Defects, in order of severity

**D1. (K3) is not preserved: failing case, the diagonal staircase. Lines 787, 818, 840.** Line 840 claims d_V(c; k-1) >= (L/2) r_k - C off a small event, because "crossing a regular coarse cell with fewer than L/2 regular fine cells needs L/2 non-regular ones". A path need not cross a regular coarse cell. It can clip it at a corner, using one fine cell.

Take W regular except on the diagonal coarse cells (t, t, 0, 0), t = 0..m+1, with flux of order one. The children of those cells are all non-regular whenever the threshold is below the lift scale; line 710 says this for independent, and D3 shows it holds for mapped too. Going from (t,t) to (t+1,t+1) costs one regular coarse cell and exactly one regular fine cell. Exact count, `checks/gate_ft_rough.py` R1, with N' the rough coarse cells:

| L | m | D | d_V | (L/2) D | N' |
|---|---|---|---|---|---|
| 5 | 12 | 13 | 12 | 32.5 | 13 |
| 9 | 12 | 13 | 12 | 58.5 | 13 |
| 15 | 12 | 13 | 12 | 97.5 | 13 |

So d_V is of order D, not (L/2) D, deterministically, with probability one. This is a path in the 2D embedding, so in 4D the true d_V is at most this. If a rough plaquette marks four coarse sites rather than one, take rough squares at (2t, 2t); the count per regular coarse cell is the same.

*An element of the input class whose image fails (K3).* Fix R := L m + L. Let g_c be a gauge-invariant function with 0 <= g_c <= 1 of V on the annulus Q_(R+2)(c) \ Q_R(c). Put

  chi_c(V) := min( 1, min over n <= R of L^p exp(-kappa d_V(c; n)) (1 + N_n(c; V))^C ),
  e_c := (u / (2 x)) 1[Q_R(c) not regular at V] chi_c(V) g_c(V).

Check of the class. (K1) with eta = 0: if Q_n(c) is regular, pi_n^* V is regular everywhere, so the indicator vanishes on every increment. (K2) is immediate. (K3): for V_1 = V_2 on Q_n(c), n <= R, each value is at most (u/2x) L^p exp(-kappa d(c;n)) (1 + N_n)^C by the min over n, and d, N depend only on Q_n(c), so the difference is within the bound. For n >= R + 2 the difference is zero; for n = R, R+1 the chi factor is common and the same bound applies with a constant. So e_c is in K_j(c; 0, u), and Lemma 14.15(c) then claims u' = u/4.

*The image.* Let W_1 be the staircase. Let W_2 = W_1 on Q'_m(c'), with an order-one change on the coarse shell just outside, so that the law of each g_c differs by c_g > 0 between the two (order one, since g_c sits at the place of the change). Under both laws d_V(c; R) is about m and N_R(c) about L^4 m for every child c of c' = (0,0,0,0). Then, for m with the chi bound below 1,

  LHS := | x h(W_1) - x h(W_2) | >= c L^4 u c_g L^p exp(-kappa m) (L^4 m)^C,
  RHS of (K3) := L^p (u/4) exp(-kappa D) (1 + N')^C, with D about m, N' about m.

The ratio is about 4 c_g L^(4 + 4C), for every exponent C, at every large m. It carries no exponential gain, so raising D_L does not help, and raising the exponent C makes it worse. `checks/gate_ft_rough.py` R2: log(LHS/RHS) = 25.4, 38.6, 69.4 at (L, C) = (9, 2), (27, 2), (81, 3), with smallest m = 231, 322, 624 at kappa = 0.2.

The closure at line 844 relies on the factor exp(-kappa L r_k / 2) to pay for C(L). In this geometry that factor is exp(-kappa r_k), and C(L) contains the two factors L^4 (children) and L^(4C) (the moment step "(1 + N_k)^C <= C(L)(1 + N')^C"), with nothing left to absorb them.

**D2. A second failing case: thin regular shells. Lines 840, 842, 796 (e1).** Let W have concentric regular shells of coarse width 1, with strongly rough shells between them, out to radius m. Then D is about m/2 and N' about m^4, so the (K3) bound is exponentially small in m. The fine first-passage distance is destroyed in either of two ways.

(a) *Lift tail.* Text 13 E2 gives amplitude decay 1.6 per coarse cell, so fine flux in a regular coarse cell next to flux F' is about 0.2 F' L^-2 near the interface. With the threshold c_1 L^-2 or a_* L^-2 this exceeds the threshold when c_1 < 0.2 F'. Then (e1), read for cells below regular coarse cells under rough W as line 840 reads it, is false: those cells are non-regular with probability near one. Line 791 restricts (GS_j) to regular W "unless stated", and (e1) is not so stated: line 840 uses it outside its range.

(b) *Pierced columns.* Even without the tail, let p_col be the probability that a given column of L fine cells across the shell is entirely non-regular. A shell of area R^3 has about R^3 L^3 such columns, so for R >= p_col^(-1/3) one exists with probability near one, under both W_1, W_2. Rough shells are transparent, so a path reaches it. Then d_V(c; k_1) = 0 on an event of probability near one, and "except on an event of probability at most omega_j^(L D/C)" at line 842 is false. Line 912(g) is right to look at this, but the prefactor cannot pay: taking D about R, N' about R^4, (1 + N')^C exp(-kappa D) is still exponentially small. The element of the class is e_c with chi replaced by the indicator of a chain of non-regular cells to the annulus. The image differs by order u.

**D3. The mapped attempt is not in the (G1) branch. Lines 710, 799, 1013.** Text 14 and 16 say mapped has "constant threshold a_c, so (G1)". `hard-core--mapped.md` line 23 says "One threshold: T = a_*/L^2", and its line 592 has T_c = a_*/L^2, T_f about L^(1/4) T_c. The lift bound there is C_r L^-1 flux' (its line 590), and even a smooth lift gives flux' L^-2. So for flux' of order one above a_*, the children sit above the threshold, exactly as for independent. Its line 448 says "a_c depends on d and L only. It is a constant, not g p(g)": constant means free of x, not large against the lift scale, and Text 14 and 16 read it the second way. Both attempts are in the (G1') branch. So (G1) has no customer, the proof of (K2) at line 836 is written only for it, and D1 applies to both attempts.

**D4. The (G1') recursion at lines 710, 799 does not close with mean 1/8.** Line 710: u_(j+1)(f) <= C(L) x^(3/2) eta + L^4 u_j(C_s L^-kappa_s f) + (1/8) u_j(2). Unrolling two bands, U_(j+1) <= A' + U_j/8 + (L^4/8) U_(j-1) + ..., since the rare top-band children of the middle band feed back with the factor L^4. The growth is L^2/sqrt(8) per level, and it compounds over all levels. `checks/gate_ft_rough.py` R4: mean growth 29.1 at L = 9, 262 at L = 27, 2955 at L = 27, h = 3; with q = L^(-4h)/8 the recursion closes (growth 1.000). The flux contraction bounds the number of bands, but not this feedback. Fix: state (G1') with mean at most c L^(-4h), which is harmless at large x because the true mean is far smaller. Also write the (K2) proof for (G1'), which line 836 omits.

**D5. (GS_j)(e3) is false as stated, in the free theory. Lines 796, 840, 912(g).** The clause gives total variation at most C_n exp(-c_F d'), with C_n independent of j. In a Gaussian fibre the mean shift does not depend on x and the covariance is 1/x, so TV = erf(sqrt(x) s(d') / (2 sqrt 2 sigma)). At fixed d', TV tends to 1 as x grows. `checks/gate_ft_rough.py` R3 (2D scalar with block-average constraint, L = 3, order-one coarse change, one site):

| m | shift | TV x=4 | TV x=100 | TV x=10^4 | TV x=10^6 |
|---|---|---|---|---|---|
| 2 | 5.1e-3 | 0.0089 | 0.0447 | 0.4248 | 1.0000 |
| 3 | 6.6e-4 | 0.0012 | 0.0058 | 0.0581 | 0.5339 |
| 4 | 8.7e-5 | 0.0002 | 0.0008 | 0.0076 | 0.0758 |

Decay rate 2.04 per coarse cell, stable. Correct form: TV <= min(1, C_n x^(1/2) Delta exp(-c_F d')). Both files already carry such a prefactor: independent (TAIL), its line 517, "min(1, eps_0 exp(-c d) / g)"; mapped, its line 602, "C x^M (1 + |gamma|) e^{-mu_1 d}". (GS_j)(d) carries it through tau' at line 796, so the clause list is internally uneven.

Consequence, repairable: (K3) needs a prefactor x^(1/6), because exp(-(c_F/2 - kappa) D) x^(1/2) <= 1 needs D >= (4/(3 c_F)) log x, and kappa D is then (1/6) log x. This agrees with line 912(e) that rough cells within log x matter. Regular-tier Step 3 is unaffected: min(P, TV) <= (P TV)^(1/2), and omega_j^(1/2) beats any power of x.

Also, line 796's "(FC_j) is the two-point form of this" is wrong in direction: (FC_j) holds in this model with no x-prefactor, and (e3) does not.

**D6. The derivative half of (TR'_p) is not delivered. Lines 685, 706, 974.** Line 974 says the mark "with Lemma 10.6 gives (TR'_p)". The class K_j has sup bounds and differences only, no derivative. Line 706 derives D_x Y^(j) = Cov(Y^(j-1), score_x), "given the marginal density has a score in L^2". The score is in no clause of the table at lines 978-992. Neither is its decay: the L^p bound with weight exp(mu d) needs an induction through (FC_(j-1)) applied to "Y^(j-1) near x", which is not written. The count looks fine (D_x in the chart carries g_j, and g_j x_(j-1) g_(j-1) is of order one, so the score is C(L)(1 + |xi|)) and the rates fit (decay c_1 per level-j cell, any mu with c_1/L < mu <= c_1/2 works). Fix: add a score clause and write the induction. This is an omission, not an error.

**D7. Closure bookkeeping inside (K3), even where the L gain exists. Line 840.** "The sum over k costs C(L)(1 + N')^C", with the same C as the input. The sum over k <= L N' of polynomial C_k adds (1 + N')^(s+1), and the input factor (1 + N_k)^C is already at exponent C. So the exponent grows at each step as written. Repair exists: for those k use the sup 2u, which has no N factor; for r_k >= D/2 interpolate min(1, A (1+N)^C) <= A^t (1+N)^(C t). Needs C >= (s+1)/(1-t). Not fatal; D1 is the real obstruction.

**D8. Fit table overstatements. Lines 796, 1006, 1010-1012.** See Item 7. Row (GS_j) says "(e) from 4.7b and stage (ii)": (e1) at regular W comes from there; (e2), (e3) do not. Row (Q_j) says "Fits both as they stand": the shape does, but Q^s must lie in K_j, which includes (K3), and neither file states first-passage locality for EE^R or R_k. Row (FC_j): see Item 7. Line 1006, library files are not in this snapshot, so I could not check them.

**D9. Inconsistency on what g^4 means. Lines 25, 910.** Line 25 says the factor g^4 "cannot be relaxed (finding 7)". Finding 7 says "any g_j^(2 + eps) would also do". Finding 7 is right: the condition is that sum_j b^new_j converges and is small, which needs only sum_j g_j^(2+eps) finite, true by (FLOW) or (T4) of independent. This matters for fit: independent has no parity improvement (its line 812, size g p^3; its (EI), line 430), so (C2)(b) with the factor g is not available there. With g p(g)^3 in place of g it gives b^new about g^4 p^3, which is enough.

**D10. Support of the remainder. Line 888.** r_(j,c) is claimed on S_j, the a_j-neighbourhood of supp f. The term (f(c') - f(c'')) I_(j; c',c'') at line 896 is non-zero for c' far from supp f and c'' in it, with size exp(-c d). So r has exponential tails on the whole torus. The sum converges with no change of power, but (ii) and (iii) should carry the weight exp(-c d(c, supp f)/a_j), and the recursion should propagate it.

**D11. (SM) in the measure of the support is not what is delivered. Lines 384, 679, 702, 890.** (SM) has M_n(v, delta) with v the measure of the supports. The mark bound counts level-k cells meeting the a_k-neighbourhood of the support. Failing case: f = sum of N bumps of radius rho and height rho, spread over a region of side R, with v = N rho^4 fixed, R large, rho -> 0, and ||f||_T bounded. The bound grows like (R/a_k)^4, while the measure stays at v. Similarly E_j must read max(1, E_j) at line 702: there is at least one term when the support is smaller than a_j. Harmless for Theorems 8, 9 if v is re-read as the measure of a fixed neighbourhood of the support, since those proofs work with supports in fixed neighbourhoods. But the statement should change.

**D12. (FLOW) as written is stronger than independent gives. Lines 800, 1005.** "x_j - x_(j+1) lies between positive constants." Independent's Prop 8.4, its lines 821-823, has w_j = u_j - d_j strictly decreasing, and says u_j "need not be monotone". What Theorem 14.13 consumes is (T3), which suffices. Restate (FLOW) as sum_j C(L) g_j^(2+eps) <= 1/C.

**D13. The cut is absent from S^r_W. Lines 854, 862.** Lemma 14.10 for a law with a cut has the extra term xi_b d_b Psi, or a surface term for a sharp cut. Line 854 says so, and line 862 does not include it. `checks/gate_ft_virial.py` B shows the size on a periodic chart: E = 1 - boundary exactly, with boundary 0.29 at b = 1, 2.5e-4 at b = 5. For independent, whose cuts are at p(g), this gives exp(-p^2/3)-type terms, which fit in omega_j only if omega_j includes them. Put it in h explicitly.

**D14. Typo. Line 826.** "x_(j+1)/x_j is at most 2" should read x_j/x_(j+1).

## Item 1. Lemma 14.10: verdict ADVANCE

Rederived: on R^n with S growing, integrate d_b(xi_b e^{-S}) = 0. Hence E[xi_b d_b S] = 1 for each b, so any diagonal weight sums. Correct as stated.

Exact small cases, `checks/gate_ft_virial.py`:
- **A.** SU(2), one link in the exponential chart, including log J = 2 log(sin|v|/|v|). E[v . grad S_eff] = 3.000000000000 at y = 1, 5, 40. There is no boundary term, because J vanishes on the cut locus. This is the right chart for free links.
- **B.** U(1) on a periodic chart: E = 1 - boundary, to 12 digits. A real but tiny term (D13).
- **D, per coordinate.** Asymmetric chain, v1 - 1, v2 - 1 at 1e-15.

## Item 2. Theorem 14.13: closes on the regular tier

Line by line.

*z and rho.* (i) follows from the definitions and the tower, and the double sum of I vanishes by antisymmetry. Coefficient exactly 1: z_(j+1) = z_j + beta_j, since Lemma 14.16 has a_(j+1,c') with coefficient 1 by the definition a_(j+1,c') = sum_c a_(j,c) o V^*. b_(j+1) <= b_j/4 + 2 b^new_j + small. Sum gives sum b_j <= 4 sum b^new_j (the true factor is 8/3). |z_j - 1| <= 1/2 under 8 C sum b^new_j <= 1. The induction is closed: z_j <= 2 is used only to bound z_(j+1).

*r.* I recomputed the tower:

  r_(j+1) = (E_W - E_1)[r_j] + sum_c' sum_c (f(c) - f(c')) (E_W - E_1)[D_(j,c)] + (z_j/2) sum_c' sum_c'' (f(c') - f(c'')) I.

This matches line 896. With theta_r absolute, because sum_c t_n^2 <= C_n x Ebar replaces L^4 by energy conservation: eta_(j+1) <= theta_r eta_j + (theta_r Lam + C iota_*) a_(j+1)/l. Unrolled, eta_k <= (S a_k / (2 l)) sum_i (theta_r/L)^i, a geometric series below L. This is correct, and it is the new idea: the source grows faster than the operator. Hypothesis needed: theta_r < L; no contraction.

*Order of constants.* c_F, kappa absolute. Then theta_r, theta_rho free of L up to logs, so L can be chosen. Then eps_0, C(L). Then gamma, against C_h(L), C_I(L), since sum_j g_j^4 is at most C g_K^2 / log L by (FLOW). No circularity. Exponents in (K3): writing L^p for the prefactor and L^q for the extra factor per step, D_L = (8 q / (3 c_F)) log L, and p >= q/3 + small. No circularity if the exponent C of (1+N) is fixed first; but see D1, where q contains 4C and is not absorbed.

*Power.* From (ii), (iii): the main term is C_p Lam g_j^2 (l/a_j)^4; the remainder is smaller by a_j/l. So (TR_p) comes out at the power (l/a_k)^4 with an extra g_k^2. The constant A_p may depend on p: at fixed gamma and large p, omega_j^(1/p) is not small on finitely many coarse levels, which costs only a constant. Fine, since n comes after gamma.

*Condition.* The telescoped form at line 789 and the L^p bound use (K3) at n = n_0 - 1. With (K2) alone, every cell sees a far rough cell with probability near one in large volume, so there is no bound. Hence (TR_p) depends on the rough tier.

Lemma 14.14 checked line by line: the map is odd, degree zero, sends plaquettes to plaquettes or degenerate; preimage count of order 4 (m-n+2)^2, so the stated C (2m+1)^4 is safe. All of (a)-(d) correct.

## Item 3. Lemma 14.15: the rough tier does not close as written

(a) Steps 1-3 checked against the clauses, with (K3) as input. Correct. (b) The algebra at line 832 is correct. The Schur step is correct, but note it needs reflections: `checks/gate_ft_rough.py` R6 gives <chi,chi> = 1 on Lambda^2 R^4 under the 384 elements of B_4, and 2 under its rotation subgroup. So the hypercubic group at c must include reflections, as (CF_j)(c) and the odd-L remark give. min(A,B) <= (A B)^(1/2) gives theta_rho, with rate c_F/2 >= kappa.

(c): D1, D2, D3, D4, D5, D7.

**Decision on the question put: does the union bound close in L^p, or does the rough tier fail?**

*As written it fails.* Not only for N' astronomically large: (K3) fails on the staircase with N' of order D, on all W of that kind, and on shells with N' polynomial in D.

*A plain L^p replacement also fails.* By Jensen, ||E[e_c^rough | W]||_p <= ||e_c^rough||_p, so the rare part of level j contributes (l/a_j)^4 x_j^(3/2) omega_j^(1/p) to level k. With omega_j = exp(-c eps_0^2 x_j) and x_j = x_K + (K - j) b log L, each level multiplies by L^4 and gains only L^(-c eps_0^2 b / p). Since eps_0 is at most of order L^-2 in both files, the sum diverges like a^-4. This is the LF-count of line 846, and it is the reason (K3) exists.

*What is true.* (K3) is consumed only on fields typical under a regular parent, and the fields that violate it have small probability: about omega^D for the staircase, about omega^(R^3) for shells. So the violation does not matter in L^p, if the class is rewritten so it can see that. A candidate, not verified, is two changes.
- Replace (1 + N)^C by a path weight: the first-passage functional gets a gain per rough cell on the path, with weights by flux band, capped by (K2). Counting all rough cells in a cube would fail, since N_n is about omega n^4 and exp(nu N_n) beats exp(-kappa n); counting only cells on the path gives a Peierls sum with no volume term.
- Use bands so that a strongly rough cell pays L^4 only for a bounded number of generations, by flux contraction.

Checks by hand on the two failing cases: the staircase pays through N' at least of order D, and shells become trivially true. That is all I checked. This needs a full write-out, and it changes what the hard core is asked for: (e1) under rough W, (G1') with L^(-4h), (e3) with x^(1/2).

## Item 4. Lemma 14.16: identity exact, g^4 conditional

*Identity, line by line.* Lemma 14.10 with weight phi^', the criticality sum_c grad_c = 0, insertion, antisymmetric split: all correct. `checks/gate_ft_virial.py` D tests it on an exact non-Gaussian model with no symmetry (k = 1, 1.7, 0.6, three cells, two coarse cells, linear chart, Th = 0.5):

| x | LHS | classical | current | G^hi | defect | current/(g^2 cl) | hi/(g^4 cl) |
|---|---|---|---|---|---|---|---|
| 20 | 3.723888e-1 | 3.711407e-1 | 1.1782e-3 | 6.99e-5 | 2e-16 | 0.0635 | 0.0753 |
| 80 | 1.485668 | 1.484563 | 1.0889e-3 | 1.65e-5 | 2e-16 | 0.0587 | 0.0713 |
| 320 | 5.939323 | 5.938251 | 1.0679e-3 | 4.08e-6 | 2e-15 | 0.0575 | 0.0703 |

Identity to 1e-15. Current is relative g^2 and the rest relative g^4, with stable coefficients, as claimed.

*Exact coefficient, a non-abelian test.* SU(2) chain of n links with product W, exact character sum, `checks/gate_ft_virial.py` C. R = (T_n(theta) - T_n(0))/a_n(theta) with a_n = n (1 - cos(theta/n)). No 1/beta term; beta^2 (R - 1) tends to a constant:

| n | beta = 20 | 40 | 80 | 160 |
|---|---|---|---|---|
| 2 | -0.1007 | -0.0981 | -0.0969 | -0.0963 |
| 4 | +0.0358 | +0.0381 | +0.0390 | +0.0394 |
| 8 | +0.1655 | +0.1578 | +0.1542 | +0.1525 |

For n = 2 by hand, T_2 = 2 - 2c I_2(2 beta c)/I_1(2 beta c) gives -(3/32)/beta^2 at small theta; the table is at theta = 0.4 and agrees. Over levels at beta = 320: -0.096, +0.040, +0.152, +0.219, +0.256, +0.275 at n = 2, ..., 64. Increments halve, so no compounding in this toy. (Chain, so there is no running.)

*Is g^4 obtained or assumed?* Split it.
- **Derived:** there is no O(g^2) coefficient in front of a_(j+1). This is exact and comes from Lemma 14.10.
- **Assumed:** the residue is O(g^4), through (C2)(a) on P^(4) and d^2 Q^reg, through (C2)(b) on P^(3) and d Q^reg, and through (Q_j) for the regularity of Q^reg at unit scale.
- **Assumed outright:** x^(1/2) eta^s <= C g^4 for the non-smooth part, which is a direct hypothesis.

So the mechanism is proved, and the size is a clause. The arithmetic of the counts at line 876 is right. The Q^s estimate at line 878 is first order only: the second-order term is not written, though given eta^s <= g^5 it is small. Its stated worst case x^(1/2) is right.

Finding 6 is confirmed by the same reasoning. One-loop has no x, so its x-derivative vanishes.

## Item 5. Theorems 14.1b and 14.1c: multi-source bounds follow

Theorem 14.1b. Law of total cumulance: `checks/gate_ft_rough.py` R5, differences below 1e-16 at |I| = 2, 3, 4. C_m = 2, 6, 26. Hoelder on the moment expansion is correct. The replacement of kappa_{i} by y_k for |pi| >= 2 is correct. Exact and clean.

Theorem 14.1c.
- The one-step formula: R5, 1.6e-16.
- The two-point formula is the iterated law of total covariance.
- The bound on G_j: with weights exp(-mu d_j) and rate c_1/L per fine cell, the sum converges for mu > c_1/L, which holds.
- The sum over j: at i = j - 1 the term is L^8 E_j^2 exp(-c delta/a_j), and i = j - 2 is much smaller, so the stated bound holds with C about L^8.
- Higher m: split at any pair, since all supports are separated. Blocks with |B'| >= 2 use induction at mp, so P_n is finite.

There is no second source. Uniformity in a, torus and positions is correct, given that all norms are local and priced by Lemma 10.6. G_j should exclude a chain with a positive fraction of rough cells, not only a full chain, since (FC_j) at Euclidean distance is false across a partly rough chain. Same probability up to constants; minor.

Consistency in the free theory: (l/delta)^8 g^4 at a_j of order delta matches the true separated covariance g^4 l^8 / delta^8.

Prop 14.7: R7 confirms y_+ = 0, 0, 1.3, -1.3 and y_+ + y_- = 0 at 2e-16.

## Item 6. UV-OS as an interface

*Internal consistency.* I found no contradiction among the clauses apart from (e3) against (d) on the x-prefactor (D5). (GS)(a) with (C2), (Q) is consistent with Lemma 14.16 at level of orders.

*Two-loop term.* The clause on the flow derivative accommodates it. With B(x) = 2 b_0 + 2 b_1/x, x_(j+1) = x_j - B(x_j) log L gives dx_(j+1)/dx_j = 1 + 2 b_1 log L g_j^4 per step, which is order g^4. The product telescopes: z_K = B(x_K)/B(x_0), about 1 + (b_1/b_0)(g_K^2 - g_0^2). So z is bounded uniformly in a, with limit 1 + (b_1/b_0) g_K^2. b_1/b_0 = 34 N/(11 . 16 pi^2), about 0.039 for N = 2. So 1/2 <= z_K <= 2 is comfortable. This also matches, from memory and not derived here, the known statement that beta(g)/g F^2 is renormalisation-group invariant, so F^2 has anomalous dimension starting at the two-loop coefficient. Independent's own bound (its line 726, Cauchy on rho_j) gives 1 + O(g^3 p^3), also summable.

*Clauses tested.*

| Clause | Test | Result |
|---|---|---|
| (CF), (LE), (REG) | Text 13, read only; trivial in free theory | consistent |
| (GS)(a), (c) | Lemma 14.11 rederived, exact Gaussian | true |
| (GS)(b), (d) | Read; (d) by Cauchy-Schwarz with (LE) gives the block sum | plausible |
| (GS)(e1) | Regular W: fine. Next to strong rough W with threshold below lift scale | false as read at line 840 (D2) |
| (GS)(e2) | Same Cauchy-Schwarz as Lemma 14.11 | true in Gaussian |
| (GS)(e3) | Free theory | false as stated (D5) |
| (C2)(a), (b) | Exact chain, D above; free theory by colour | consistent |
| (Q_j) | One-loop x-free; two-loop O(g^2); n-chain | consistent |
| (FC_j) | Helffer-Sjostrand plus Combes-Thomas in convex case, from memory; free theory | true there |
| (G1), (G1') | See D3, D4 | (G1) unavailable, (G1') misstated |

*Is the reduction empty?* No. No clause implies (SM) or (TR_p): all are one-step statements, and the multi-level content is in Lemma 14.15, Theorem 14.13. Theorem 4 is not contradicted: the clauses are local, far beyond Z(beta + s). I looked for a clause equivalent to its consumer and found none. (Q_j) with (CF_j) is the hard core's constant-coupling induction, so it is large, but it is not the conclusion.

*Is it strictly smaller than UV-CT?* **No: the two are logically incomparable.** UV-CT gives complex-source bounds and CT4, which UV-OS does not imply. UV-OS requires local densities, position independence, block-summed locality, screening and rarity under rough W, none implied by I^w(K). Independent has UV-CT at the label "implication, given I^w(K) and Proposition 8.4" (its line 66) and has no such statement for UV-OS. The smallness is of a different kind: no source, no complex w, no CT4, no factor E carried through the induction. Line 1015's practical point (real-only R sector available again) stands as the real gain; I confirmed only that independent line 26 lists such routes among those dropped, not that they work. Recommendation: do not describe the swap as a strict reduction. The honest description is a trade: drop the source from the induction, add rough-parent and locality statements.

## Item 7. Fit: what each attempt actually states

None of (CF_j), (LE_j), (REG_j), (GS_j), (C2_j), (Q_j), (FC_j), or UV-OS appears by name in either file (grep count 0), so this is fit by content.

| Clause | hard-core--independent | hard-core--mapped | Text 16 claim |
|---|---|---|---|
| (CF_j) | F_k, V^* minimiser, form bounds; no density uniform in level | A_k minimal fine energy (line 442); A_c(U_k(V)) as source density (line 649) is the closest thing | Accurate |
| (LE_j) | Kernel and C_s L^-2 interior, lines 883, 614 | Line 590 kappa = 1; block energy | Accurate for W regular everywhere |
| (REG_j) | Holder modulus line 883, linear | L^4 gradient bound line 586; not this form | Accurate |
| (GS_j)(a),(c) | 4.7c lines 596, 608, close | Nothing | Accurate |
| (GS_j)(b),(d) | Not stated. Line 623 sums over positions for size only | Nothing | Accurate |
| (GS_j)(e1) | Activity bound line 236; regular parent | Prop R1 line 486, class parent; superseded by (RP'_k), line 84 | Accurate only at regular parents |
| (GS_j)(e2) | Nothing explicit | Nothing | Overstated |
| (GS_j)(e3) | Nothing. (TAIL) line 517 is sensitivity with 1/g prefactor | Nothing. Line 602 is covariance of bounded functions with x^M | **Overstated; neither is near** |
| (C2_j) | (a): N_good analytic line 500, Cauchy in W, plausible. (b): no parity, line 812; (EI) line 430 has g p^3 | (a), (b) in shape: lines 453, 472; Laplace lemma in library; Hessian and Geometric package are gaps, lines 97, 103 | Fair as shape, not stated |
| (Q_j) | EE^an analytic on the class, line 234; EE^R tiny | R_k derivative norms free of x_k, lines 23, 444 | Shape fits; first-passage class membership of Q^s not stated |
| (FC_j) | 7.3: decay of the Hessian inverse kernel at background, rate c/L; not Cov(F, H) in L^2 derivative form | Mixture: conditional covariance plus bounded polymer covariance, lines 602, 606; "functions must be bounded" | Partial. Y^(j) is unbounded, so the consumer's exact form is delivered by neither |

**The clause neither comes near: (GS_j)(e3)**, screening in total variation in the first-passage metric for arbitrary W, with rough regions transparent. Same remark for (G1') under a rough parent, outside the list asked. In the sections I read, both attempts bound the density at a rough W only from above, so the conditional law given a rough W, which needs a lower bound on rho(W), is not controlled. Line 1013 notes this for (G1'). (GS)(b), (d) are absent too, but they look like rewrites of existing estimates.

Line 1013's "Constant threshold a_c" is wrong: D3.

## What was checked and how

**Line by line, recomputed:** Lemma 14.10; Lemma 14.11; Lemma 14.14; Lemma 14.15(a), (b), (c); Lemma 14.16; Theorem 14.13; Theorem 14.1b; Theorem 14.1c; Prop 14.7 by enumeration; the formula for the two-loop term.

**Read only, not recomputed:** Theorem 14.1, Lemma 14.2, Lemma 14.3, F1-F14, Prop 14.6, Prop 14.8 except the recursion, findings 1-7 except as cited; Text 13; Theorem 10.7 and Lemma 10.6 (statement only).

**In the hard-core files:** read the cited sections and grep only. Independent 4.7c, (TAIL), 3.2, Prop 8.4 read; (EI), 7.3, 4.7b read in part. Mapped lines 23, 442-458, 486-494, 586-592, 596-606 read. `library/*` is not in this snapshot and was not read, so the mapped rows that cite it rest on that file's summaries.

**Limits of the failing cases.** D1 and D2 are counterexamples to closure of the class, not to the statement that the actual mark D_(j,c) is small. The actual D_(j,c) may well be better than a worst-case class member. Order-one claims about g_c in D1 use only that the fibre law next to a changed coarse field changes; this conflicts with no clause, but I did not compute it in a model.

**Scripts.** `checks/gate_ft_virial.py` (A, B, C, D), `checks/gate_ft_rough.py` (R1-R7).
