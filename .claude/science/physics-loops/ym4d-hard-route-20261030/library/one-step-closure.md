# The one-step theorem: closure, with every norm named

Status: own assembly, 2026-10-31, not reviewed. It is the proof of closure given the named lemmas of the other notes, each at its own label, and it records five mismatches between those notes that the assembly found, with repairs. It replaces the display "Recursion" of Text 5.9 of `parts/hard-core--mapped.md`, which had an error in its coefficients (mismatch 4 below). Organisation after Balaban (block averages, minimal fields, running coupling, vacuum subtraction, extraction of the marginal term at the trivial background). This line is not independent of the Sussman-Alpoge repository.

## 1. Constants and norms

*Order.* d = 4; J, K, c, C_T; m_*; S_*; delta_#, rho_f, the absolute rates; N := 6; mu := rho_f / (4 N), the rate of the norms, per cell of the level; L >= L_0; rho_s(L), the slow rate of Lemma HS-C; a_* <= a_th(L), T := a_*/L^2, T_2, tau(L, a_*), the cut; B_n(L), B'_m(L); then x_*(L, a_*). g_k^2 := 1/x_k, x_k >= x_*.

*Field and derivatives.* A function Z on the class D_k := { flux <= T_2 } of the level-k torus. D^n Z(V)[b_1, ..., b_n]: derivatives along e^{i t_i b_i} V, in log coordinates at V.

*The profile.* Phi_k(t) := e^{-mu t} + zeta_k e^{-mu_s t}, with mu_s := rho_s/4, zeta_k := x_k^M z_k^{1/2}, and M, z_k as in Lemma HS-T. Norm, for 1 <= n <= N:

    ||Z||_n := sup_{V in D_k} sup_{b_1} sum_{b_2, ..., b_n} |D^n Z(V)[b_1, ..., b_n]| / Phi_k(tau(b_1, ..., b_n)/2),

with tau the tree length in cells of level k. A norm with one profile, and no splitting of the function, is what is needed: it is the bound Lemma HS-T gives, and the upper chain's two-tier profile (its 21.7) is of the same form. Summing over b_i is free at half the exponents, with a constant C(rho_s) in the second tier, which zeta_k beats.

*Data at V = 1.* Pi^(n) := D^n Z(1), n = 2, 3, 4, translation invariant. *Split by distance.* With y_* := log(1/zeta_k) / (mu - mu_s), Pi^(n) = Pi^(n)_near + Pi^(n)_far, by kernel support in tree length at most y_* or above it. On tree length at most y_*, the second tier of the profile is below the first, up to a factor 2. So:

    sup_{|Im q| <= rho} |Pi-hat_near^(n)| <= C ||Z||_n,  rho := mu/2;   sup_{|Im q| <= mu_s/2} |Pi-hat_far^(n)| <= C(rho_s) zeta_k^{1/2} ||Z||_n.

Define c^(n)(Z) through the near part, after a polynomial transfer (mismatch 2).

## 2. The hypothesis and the conclusion

*H(k).* On D_k, F_k = x_k A_k + vac_k |Lambda_k| + R_k, with R_k(1) = 0, R_k with no F^2 coefficient, lattice symmetric and gauge invariant, ||R_k||_n <= B_n for 5 <= n <= N, c^(m)(R_k) <= B'_m for m = 2, 3, 4. And, added after the gate's D4 (`library/sector-values.md`): (VAL_k), |R_k(V)| <= B_v I_k(V; 1) plus a toron term, in every sector; (Jump_k), |R_k(V_1) - R_k(V_2)| <= B_j T_2^2 |J^+| for V_1, V_2 equal off J; and (Loc^c_k), for class fields equal on a ball, in any sector. And the classical statements below, which are free of k; Theorem Z at level k; and, for all boundary data, the same in (I_k^𝔡) with ||Delta R_k^𝔡||_n <= C_n(L) and (VAL^𝔡_k). D_k has T_2 enlarged by a fixed factor, for the cut field of Lemma O3. Quiet means flux at most T_q := T/(2 C_bd).

*Conclusion.* H(k) implies H(k + 1), if x_{k+1} >= x_*, with x_{k+1} = x_k - beta_{k+1}, beta_{k+1} = beta^0_{k+1} + O(C(L) g_k^2) + O(x_k^M z_k).

## 3. Steps, with input and output norms

| Step | Input | Output | Where |
|---|---|---|---|
| Classical, by induction on j | CA_{j-1}, R3_{j-1} | NC_j, CA_j, (CI''')_j, then R3_j | `relative-density-bound.md`, (f') |
| Theorem F at a lift | R3 | Sad# inverse, local norms, rate delta_# per box | `fibre-propagator.md` |
| Composite map | (i), (ii) of its setting | analytic, remainder C(L) e^2 | `analytic-lift.md`, AN1 |
| Lift, all orders | Theorem F, AN1, AN2 | H_S, lambda_S, tree decay | `analytic-lift.md`, AN3 |
| (H1)-(H3) in the chart | AN3 at Phi(xi), ||R_k||_{<=N} | S = S_0 + R_k o Phi on K | Text 5.9 |
| Base integral | (H1)-(H3), cut | G, in the profile | `preconditioned-covariance.md`, HS-T with V_s (mismatch 1) |
| Rarity | Theorem Z at level k, (CI'''), Lemma OC | z per cell, (A1') | `quiet-boundary-rarity.md` |
| Gas | (A1'), (A2), Prop MD* | W, in the profile | `polymer-covariance.md`, Text 5.4 |
| Order >= 5 | ||R_k||_n, K | contraction | Section 4 |
| Data | c^(m)(R_k), T3, Schwarz | contraction | Section 5, `gauge-taylor-contraction.md` |
| Low orders | data, order 5 | ||R_{k+1}||_m | Lemma 3 of that note |
| Flow | Theorem LS, P1; p^2 coefficient at V' = 1 | beta_{k+1} | `twisted-order-calculus.md`, Text 3, 5.9 |
| Theorem Z at level k + 1 | (I_k^𝔡), (Jump_k), (VAL^𝔡_k), Theorem Z at level k, classical, (CI''')_q, (F2) | same | `quiet-boundary-rarity.md` |
| Values, locality | gas, Theorem F-D on a staircase, Prop AN3, (R3), (AD); lifted norms | (VAL_{k+1}), (Jump_{k+1}), (Loc^c_{k+1}), (VAL^𝔡_{k+1}) | `sector-values.md` |

F_{k+1} on D_{k+1} is

    F_{k+1} = x_k A_{k+1} + (vac part) + (R_k o V^* in the mean) + G_0 + G_1 - W,   R_{k+1} := beta_{k+1} A_{k+1} + (R_k o V^*)_mean + G_0 + G_1 - W - (vac part),

with G_0 the base integral for R_k = 0, G_1 the rest of the base integral, W := log(1 + gas), and beta_{k+1} A_{k+1} = (x_k - x_{k+1}) A_{k+1} by definition of x_{k+1}. ||A_{k+1}||_n <= C(L) by Prop AN3, so beta A is a source of size C(L) log L at every order.

## 4. Orders 5 and 6

*The kernel.* K(y, x') := level-k value of D_{x'} U^*. For a tuple x'_1, ..., x'_n let g(s) := exp(sum s_i omega_i) with omega_i the gauge parameter from K#'s gauge to the weighted Landau gauge of Text 5.5 at x'_i, level-k block means taken. Since R_k is gauge invariant, R_k(V^*(V'_s)) = R_k(g(s) . V^*(V'_s)). *To avoid a far part:* in the radial gauge about x'_i, subtract from omega_i its value at radius R_* := C (log L)/delta_#, and cut it off there. The error at that radius is of size T_2 R_* against what it replaces, and K# there is below L^-C. So the omega_i have compact support, and [omega_i, K_j] has tree decay in the tuple. So:

- first order, D_{s_i} (g . V^*) = Q^{o,(k)} H'_i =: K_i, with sup_y sum_{x'} |K(y, x')| e^{mu d} <= C_1 (log L)^{1/2} L^-1, sup_{x'} sum_y |K(y, x')| e^{mu d} <= C_1 L^3, C_1 absolute, by the H^2 bound of Text 5.5 with Lemma AD, as H^2 controls block means in d = 4 up to (log L)^{1/2} at the ratio L;
- each mixed derivative of order at least 2 has size at most C_n(L) with tree decay at rate delta_n >= 4 mu, by Prop AN3 and the compact support of the omega_i.

So the chain rule gives, at V^*,

    ||R_k o V^*||_n <= C_1^n L^{4 - n} (log L)^{(n-1)/2} ||R_k||_n + C_n(L) sum_{m < n} ||R_k||_m.

The weight: tau' at level k + 1 is at most tau/L + sum_i d'(y_i, x'_i), so the first exponent is carried by K, as delta_# >= 4 mu, and the second tier has rate mu_s against L mu_s/L. So the profile at level k + 1 dominates that at level k read through the lift, given zeta_k <= zeta_{k+1} up to a factor, which holds since x_k >= x_{k+1} - C(L).

*The chart.* At xi != 0: D_{V'} Phi = (1 + O(C(L) tau)) D_{V'} V^* in tree gauge, and tree gauge is per box, with omega vanishing at block centres, so it costs C(L) with the same rate. So this adds at most C(L) tau to the top coefficient, below L^-2 for tau small in L, and tau comes after L.

*The cumulants.* G_1 = <R_k o Phi> + (cumulants with at least one factor of R_k). A factor of R_k in a cumulant of order at least 2 carries D_xi (R_k o Phi) = g D R_k [D B], so at most C(L) g_k ||R_k||_{<= n}.

*The gas.* W: at most x_k^{M n} z_k in the profile, by Text 5.4, with the second tier in its influence from (A2).

*Result, for 5 <= n <= N:*

    ||R_{k+1}||_n <= ( C_1^n L^{4-n} (log L)^{(n-1)/2} + C(L) tau + C(L) g_k ) ||R_k||_n + C_n(L) sum_{m < n} ||R_k||_m + C_n(L) + x_k^{M n} z_k.

Note the middle term, with no factor g_k: it is the mean term's non-singleton partitions.

## 5. Low-order data

For m = 2, 3, 4, with Pi_{k+1} the data of R_{k+1}. Terms: (a) the mean term at V' = 1 with singletons, on the near part: at most C L^-2 c^(m)(R_k), up to (log L)^2, by T3 and the sum over momenta, in the strip |Im q| <= rho; (b) non-singleton partitions, at most C_m(L) sum_{m' < m} c^(m')(R_k); (c) the mean at V' = 1 has fields Phi(xi), not 1: <D^m R_k(Phi(xi))> - D^m R_k(1) is at most C(L) g_k^2 ||R_k||_{<= N}; (d) the source G_0, G_1 at V' = 1, by HS-T, of size C_m(L) on the near part; (e) beta A_{k+1}, of size C(L) log L; and W, tiny; (f) far parts.

*The polynomial transfer (mismatch 2).* Lemma 1 gives vanishing to order 6 - m for the total, Pi-hat = Pi-hat_near + Pi-hat_far, after the F^2 coefficient is removed. Neither part vanishes alone. Let P be the Taylor polynomial of degree below 6 - m of Pi-hat_far at q = 0, of size at most C(rho_s) zeta_k^{1/2}. Then Pi-hat_near + P and Pi-hat_far - P each vanish to order 6 - m, and Pi-hat_near + P is analytic on the strip rho, as P is a polynomial. So Schwarz applies to each on its own strip:

    c^(m)(R_{k+1}) := rho^{-(6-m)} sup_{strip rho} |Pi-hat_near + P|.

The far part does not need a recursion at low order, by the ladder below.

*The ladder (mismatch 3).* A far part fresh at level j is analytic in the strip mu_s/2 in level-j momentum. Read through the lift it is analytic in the strip L mu_s/2 in level-(j+1) momentum, and so on. A direct recursion on it by Schwarz in a fixed narrow strip would lose rho_s^-(6-m) per level, and that is above any L^-2: it would grow like a power of L per level, while zeta_k stays nearly level with k, since z_k/z_{k+1} = exp(-c T^2 beta) is near 1. So do not fix the strip. After m_0 := 1 + log_L(rho/mu_s) levels, its strip has reached rho, and it enters the near part, with amplitude at most C(L)^{m_0} zeta_j^{1/2}, where it contracts by L^-2 rho^-(6-m) with the rest. Since m_0 depends on L only, and zeta_j <= x_*^{-M} and smaller than any power of L for x_* large, the near part receives a source of that tiny size at each level, and the far part of level k + 1 consists of at most m_0 ages, each tiny. So all low-order bounds on the second tier hold with amplitude C(L) zeta_k^{1/2}, with no growth in k.

*Result, for m = 2, 3, 4:*

    c^(m)(R_{k+1}) <= C_2 (log L)^2 L^-2 rho^{-(6-m)} c^(m)(R_k) + C_m(L) sum_{m' < m} c^(m')(R_k) + C(L) g_k^2 ||R_k||_{<= N} + C_m(L).

C_2 and rho are absolute, so the first coefficient is below 1/2 for L >= L_0.

## 6. Low orders and closure

Lemma 3 of `library/gauge-taylor-contraction.md`, applied with the whole profile: for n <= 4,

    ||R_{k+1}||_n <= C ( max_m c^(m)(R_{k+1}) + ||R_{k+1}||_5 T_2^{(5-n)/2} + e^{-mu r/2} + C(L) zeta^{1/2} ),  r := c T_2^{-1/2}.

The second tier's error is zeta e^{-mu_s r/2} and it is below everything.

*Closure.* Take L >= L_0 with C_1^5 L^-1 (log L)^2 <= 1/8, C_1^6 L^-2 (log L)^{5/2} <= 1/8, and C_2 (log L)^2 L^-2 rho^-4 <= 1/4. In this order:

1. B'_2 := 4 C_2(L), the source; then B'_3, B'_4 by the triangular system.
2. For B_5: by Section 4, B_5 <= (1/4) B_5 + C_5(L) sum_{m <= 4} ||R||_m + C_5(L), and ||R||_m <= C (B' + B_5 T_2^{1/2} + 1). As C_5(L) is uniform in a_* <= a_th(L), take a_th so small that C C_5(L) T_2^{1/2} <= 1/4. Then B_5 <= 4 C_5(L) (C B' + 2). B_6 likewise.
3. Then x_* so large that C(L) g B_N, C(L) g^2 B_N, x^{M N} z are at most 1.

All are free of k. No constant depends on the volume. So H(k + 1) holds with the same B's. QED of the closure, given the lemmas at their labels.

## 7. With boundary data

The same with Sad#_N, and with no extraction: Delta R_{k+1}^𝔡 := G^𝔡 - G^bulk at a class extension, plus the old Delta R_k read through K across clearance r_S at contraction C^n L^{4-n} e^{-n delta_# r_S} <= 1/2, for every n >= 1, by the choice of r_S, as `library/quiet-boundary-rarity.md` has it. *The second tier in Delta R:* the old part is read through K, so it is suppressed by the fast rate, whichever tier it has. So ||Delta R_{k+1}||_n <= (1/2) ||Delta R_k||_n + C_n(L).

## 8. The mismatches, recorded

**1. (A) of Lemma HS-P fails at the fast rate on the real S.** Lemma HS-T assumes (A) for weights of rate rho_f. But V contains g^2 D^2 R_k o Phi, and R_k has a second tier from the previous level, with rate at most L mu_s per box. Conjugating by e^{rho_f d} makes this grow exponentially, however small its coefficient. So HS-T as written did not apply beyond the first level. *Repair:* split V by distance: V_f, kernel at tree length at most y_*, and V_s, the rest. V_f satisfies (A) at rate rho_f, as on tree length at most y_* the second tier is below the first. V_s goes into the second tier with the barrier, in Lemma HS-C. Done in `library/preconditioned-covariance.md`.

**2. Schwarz on one tier.** Lemma 2's (T1) needs vanishing at q = 0, which only the total has, and analyticity in a strip of absolute width, which only the near part has. Repair: the polynomial transfer of Section 5. Its hostile note (c) had said "Schwarz in a narrower strip with a tiny coefficient", which is wrong as a recursion, as the next point says.

**3. The second tier does not obey the low-order recursion.** A power of L per level against a coefficient nearly level with k: a true growth if a fixed strip is used. Repair: the ladder, since each level widens the strip by L. So an old slow tier becomes part of the near part after boundedly many levels, with a coefficient tiny against any power of L. Without this, zeta's recursion at low order would have been a real divergence in k.

**4. The display "Recursion" in Text 5.9 and the chain rule.** It had C(L) g_k on the lower norms at order at least 5, but the mean term's partitions into fewer blocks carry C_n(L) with no factor of g_k. The closure then needs B_5 T^{1/2} C_5(L) small, as in Section 6, step 2: fine, since a_* comes after L, and it shows that this is where a_* small in L is really read in the recursion.

**5. The hard cut.** Lemma HS-C read the barrier's mean curvature zeta_c, which I had called a boundary integral for a hard cut. In the hard limit it diverges. The base integral must use the soft cut chi_c of Text 5, which it does, and HS-C is now stated for it, with zeta_c <= poly(x) z_c.

**6. Own-level factors.** Not a mismatch of norms but a false step, found while naming the next inequality: tubes of width d_x >= 3 L are not small against a block, so the old comparison of fills had a delta that is not small. Lemma OC of `library/quiet-boundary-rarity.md` replaces it, with no sign of beta.

Smaller points fixed here: the rate mu of the norms must be below rho_f / N, since HS-T degrades with the order; one rate for all orders, as Lemma 3 reads order 5 at that rate. In `library/analytic-lift.md`, Consequence 2 claimed one gauge at all orders: the top coefficient needs the H^2 bound, so the weighted Landau gauge at order 1, and the family g(s) above; with compact omega_i, mixed derivatives need only sizes.

## 9. Hostile check

1. *Is zeta_k <= zeta_{k+1} up to a factor?* It reads x_k >= x_{k+1} - C(L) only, from the flow, with no sign per step.
2. *The profile at level k + 1 against the lift.* Two exponents at level k read through the lift have rates L mu and L mu_s in level-(k+1) units. So the first is above mu, and the second is above mu_s. Good. The direction would be wrong if a norm were carried from coarse to fine, and it never is.
3. *What reads the absolute rate.* rho in Section 5. If rho fell with L, then rho^-4 L^-2 would stop contracting. Theorem F and HS-T supply it.
4. *C_1 absolute* is read through Lemma AD and (R3). This is where the top coefficient could fail, and Lemma AD now has an adversarial search in d = 4, which finds the ratio falling with L, and Lemma AN1's check has run there too. Both pass, and both are searches, at one level for AD and to n = 3 for AN1.
5. *The ladder's m_0* is finite only because rho_s(L) is a fixed negative power of L, a statement about this chart.
6. *Volume.* Every norm has a sup over a root, and every step is local or with exponential kernels. (A) has a Schur test. So there is no volume factor. Prop MD*, with its |A|^C, is not used in this closure beyond (A2), where kappa has no volume factor.
7. *Not displayed.* Polarisation constants in Prop AN3; the corner sum in (R1). (E) and `Brick geometry` have since been written, in `library/twisted-order-calculus.md` and `library/fibre-propagator.md`.
8. *What this does not check.* That the named lemmas are true: their own labels stand. This note checks that their outputs fit their inputs. It found five places where they did not. **A gate at 3b7fd4e57 then found Theorem Z, (A1') and the class path lemma wrong as written, so at that commit the closure's rows on rarity were not available; they now read the repaired form, not gated.**
