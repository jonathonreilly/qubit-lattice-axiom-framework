# NT1 from one flat fibre: the strict inequality of NT1-NF

Author: anthropic/claude-opus-5-5/max mac-mini-worker, 2026-11-01, queue item 8f.
Source: `be5e58b30`. Neutral: reads interface statements only and carries no proof of either hard-core attempt.
Status: Theorem F and Corollary NT1-F are implications with their clauses named. Lemma FB and the table in section 4 are discharged for the map (B-1). No clause is certified for Wilson. Author work, not a review or an audit. No status.
Credit: (NF-1) to (NF-4) are `witness-two-separation.md`; the pullback and moment bookkeeping is `witness-interface-moments.md`; Theorem 10.7 of `parts/upper-chain.md` is the route this shortens.

## 1. What changes

`witness-two-separation.md` stopped at a > 2v + d, with n the near conditional covariance, v the conditional-mean oscillation and d the DEC bound. The stop has three parts: a non-zero near fibre covariance, a small oscillation, and control of C(L) in a bound C(L) L^(-2 kappa).

All three follow from one observation. (GS_j)(a) with (LE_j) compares the fibre over any regular W with the fibre over W = 1, with a constant that does not grow with L. So the level-j law on a fixed window is close to one law, E_1, and the near and the far correlator can both be read there. DEC, the tower split and Cauchy-Schwarz are not needed. What is left is one number at one field: the value of Cov_1 at W = 1.

## 2. Comparison with the flat fibre

Fix one map, its source-free trajectory, a level j < K, and write W = V_(j+1), x = x_j, nu' the mu-law of W, nu = nu' P_j. Let D be a finite set of level-j plaquettes inside Q_n(c), c in B(c'), n <= n_L = L/C. Let R = R(g_j), G the event that W is regular on Q'_R(c'), and W^pi = pi_R^* W, with R < T_tor/4, so W^pi is regular everywhere on G by Lemma 14.14(c).

Clauses read, each as printed in `parts/upper-chain.md`:

- (GS_j)(a), for bounded e. For W regular everywhere and |e| <= 1, |(E_W - E_1)[e]| <= C_n t^2 + C_n (t^3 + omega_L(g) t^2 + omega^GS_j), t = t_n(c; W).
- (LE_j), second inequality. t_n(c; W)^2 <= C_n C_s^2 L^(-2 kappa_lift) x Ebar(c'; W). C_n is polynomial in n and free of L up to powers of log L.
- (OS_j)(c'). E_mu[1_G TV(E_W, E_(W^pi) on D)] <= omega(g_j). Source: (S) of Proposition 20.4 with (MD*_j) and (20.2).
- (FF_(j+1)) with the reflection-grid hypotheses of Lemma 10.6. They give m_1 := sup_p ||x_(j+1) s_p(W)||_(L^1(mu)) < infinity and eta(g_j) := P(G^c) -> 0 at fixed L.
- (FLOW), the ratio x_j <= (5/4) x_(j+1) only.

Put theta_L := C_n C_s^2 L^(-2 kappa_lift), bold-C_n := 2 + C_n (2 + omega_L(g_j)), N_h := 6 (2h + 1)^4, Mbar_q := sup_p ||x_(j+1) s_p(W)||_(L^q(mu)) sum_(h >= 0) exp(-c_E h) N_h, and

    eps_j := 2 omega(g_j) + 2 eta(g_j) + C_n omega^GS_j + (5/4) bold-C_n theta_L Mbar_1.          (F-0)

**Theorem F [implication; proof below].** For every measurable gauge-invariant function e of V_j on D with |e| <= 1,

    | E_nu e - E_1 e | <= eps_j,                                                                 (F-1)

and for gauge-invariant A, B on D with |A|, |B| <= b,

    | Cov_nu(A, B) - Cov_1(A, B) | <= 3 b^2 eps_j.                                               (F-2)

Proof. E_nu e - E_1 e = E_mu[(E_W - E_1) e]. Split on G:

    |E_nu e - E_1 e| <= E_mu[1_G |(E_W - E_(W^pi)) e|] + E_mu[1_G |(E_(W^pi) - E_1) e|] + 2 P(G^c).

The first term is at most 2 omega(g_j), since |(P - Q) e| <= 2 TV(P, Q) for |e| <= 1. No moment of the replacement law is needed, because e is bounded. For the second, W^pi is regular everywhere on G. If t <= 1 then t^3 <= t^2, so (GS_j)(a) gives at most C_n (2 + omega_L) t^2 + C_n omega^GS_j. If t > 1 the trivial bound 2 is at most 2 t^2. So at every W^pi,

    |(E_(W^pi) - E_1) e| <= bold-C_n t^2 + C_n omega^GS_j <= bold-C_n theta_L x_j Ebar(c'; W^pi) + C_n omega^GS_j.

By Lemma 14.14(c), s_p(W^pi) is s_(pi p)(W) or 0, so with x_j <= (5/4) x_(j+1), E_mu[1_G x_j Ebar(c'; W^pi)] <= (5/4) Mbar_1. This is (M-2) of `witness-interface-moments.md` at q = 1. That proves (F-1).

For (F-2) write

    Cov_nu(A, B) - Cov_1(A, B) = (E_nu - E_1)[A B] - (E_nu - E_1)[A] E_nu[B] - E_1[A] (E_nu - E_1)[B],

and apply (F-1) to A B / b^2, A / b, B / b. []

Second moments give the oscillation of `witness-two-separation.md`. With the same split, ||E_W A - E_1 A||_(L^2(nu')) <= b (2 omega^(1/2) + 2 eta^(1/2) + C_n omega^GS_j + (5/4) bold-C_n theta_L Mbar_2). So v in (NF-1) is at most b^2 times the square of that bracket: second order in theta_L, with no chart and no covariance clause. This also bounds k_p of (NF-6).

**Sign of the error.** (F-2) is first order in theta_L, with no factor of the small covariance, because (GS_j)(a) is a sup-norm statement. Theorem 10.7 has the sharper C_6 |P| L^(-2 kappa), and it reads (OS_j)(a) to (d) at all W^pi. So this route trades a larger L_0 for fewer clauses.

## 3. NT1

**The flat value.** At W = 1 the chart of (OS_j)(b) has phi = 0, so X_p := x s_p = Q_p + g_j Y_p on the chart event, with Q_p = (1/8) |(D xi)_p|^2. Read (OS_j)(b), (c) at the one field W = 1 and (GS_j)(c) at W = 1 for the moments. On the chart event X_p X_q - Q_p Q_q = g_j (Q_p Y_q + Q_q Y_p) + g_j^2 Y_p Y_q, which is bounded by C(L) g_j (1 + |xi|_loc)^8, a polynomial within the degree 8 of (c). Off the chart event, Cauchy-Schwarz and (GS_j)(c) give C omega^(1/2). The Gaussian value is (NF-5) at phi = 0, and Gamma_pq(1) = 4 P^fib_pq 1_3 gives ||Gamma_pq(1)||_HS^2 / 32 = (3/2) (P^fib_pq)^2. So:

**(FT) [implication from (OS_j)(b), (c) and (GS_j)(c), at W = 1 only].** For p, q in D, Cov_1(X_p, X_q) -> (3/2) (P^fib_pq)^2 as g_j -> 0 at fixed L, uniformly in j.

(FT) is the only place where the theorem below reads a value rather than a comparison. No clause of the regular package evaluates anything at W = 1, so some statement of this kind is needed: a comparison with E_1 cannot create a non-zero value, and the product law of Proposition 10.4 has separated correlators zero at every level.

**Clipped energies.** Y_p := min(X_p, b). From X_p <= tau_n^2 and (GS_j)(c) at W = 1, for any r >= 1,

    |Cov_1(Y_p, Y_q) - Cov_1(X_p, X_q)| <= C_(n,r) b^(-r) =: tau_b.                               (F-3)

Y_p is bounded by b, and it is a continuous gauge-invariant function of level-j links. At fixed physical scale it is a sequence in the blocked family of Theorem 10.2, after replacing x_(j_i, i) by its limit at cost o(1).

**Geometry.** Take supports of level-j plaquette observables within w level-j cells of the plaquette, with w free of L. This holds for (LOC) if d_f <= w (L - 1), which must be checked per map. Choose q_n = p + z_n and q_f = q_n + t e_4 with both pairs strictly ordered along all four axes, and n <= n_L large enough to contain them.

**Corollary NT1-F [implication].** Assume H-NET, the fixed-scale part of H-SCALE, the clauses of section 2 and (FT) at the two pairs. Put

    a_L := (3/2) | (P^fib_(p q_n))^2 - (P^fib_(p q_f))^2 |.

If a_L >= a_0 > 0 for all large L, then choose in this order: the clip level b with 2 tau_b <= a_0 / 4; L with 6 b^2 (5/4) bold-C_n theta_L Mbar_1 <= a_0 / 4; then X large, so that every g_j on the trajectory is small enough for (FT) to within a_0 / 8 and for the omega and eta terms of 6 b^2 eps_j to total at most a_0 / 8. Then, at fixed level distance m from the top, for all large i,

    | Cov_nu(Y_p, Y_(q_n)) - Cov_nu(Y_p, Y_(q_f)) | >= a_0 / 4 > 0,

and Theorem 4.1 gives H != 0 on the orthocomplement of Omega. C_(n,r) is free of L up to powers of log L, so b grows at most like a power of log L and the condition on L can be met. (NF-3) holds in the same order: n at the near pair is within 3 b^2 eps_j of Cov_1, by the three fixed tests of (F-2) read inside E_mu, v is second order in theta_L, and the far conditional covariance is bounded the same way. If a far pair outside n_L is wanted, DEC gives d_i as printed, at an admissible m_f, and it is small for X large.

Proof. Add (F-2) at the two pairs, (F-3) and (FT). Mbar_1 is bounded at fixed L by Lemma 10.6, and as g -> 0 it is bounded independently of L: the clipped moments are absolute there, and the unclipped remainder carries the rarity factor. Only (FLOW)'s x_i >= x_K / 2 is used to make every g_j small from X large. []

So theta_L is what makes L large, and it does not depend on g. This reads (LE_j) as printed, with C_n free of L up to powers of log L, and C_s free of L, which is an unchecked item of the part's Obligations. The scale of the constants is not modest: with the numbers of section 4, a_0 is about 4e-9, so L^(2 kappa_lift) must exceed about 10^12 times C_n^2 C_s^2 Mbar_1 at r = 8. With (OS_j)(a), (d) the requirement falls to about 10^4 C, as in Theorem 10.7.

**What is not read.** DEC, (SCR_j), the tower identity, (OS_j)(a), (OS_j)(d) away from W = 1, CF, REG, C2, Q, RC, (COV8), (TV-P) for unbounded tests, JET8, H-LIFT, any Gaussian limit at W != 1, any vertex, and the flow beyond the two lines named.

**Static test.** A static random variable has equal correlators at all separations, so it cannot satisfy these clauses together with a_L > 0. The theorem does not mistake it for dynamics: the contradiction falls on (GS_j)(a) or (FT).

## 4. The free input for the map (B-1)

**Lemma FB [discharged].** For the map (B-1), as n -> infinity, the flux of the (a, b) plaquette at the origin is the average of F_ab against the positive density of unit mass

    rho_ab(x) = tri(x_a - 1/2) tri(x_b - 1/2) box(x_c) box(x_d),

with box the unit-interval indicator centred at 0 and tri = box * box. For parallel plaquettes at offset z,

    P_infinity(z) = int R(w) M(z - w) dw,    R = T_4(w_a) T_4(w_b) T_2(w_c) T_2(w_d),
    M(x) = (1 / (pi^2 r^4)) (1 - 2 (x_a^2 + x_b^2) / r^2),

T_2 = box^(*2), T_4 = box^(*4).

Proof. In (B-7), a_a(p) Jhat_a = exp(-i (p_a + p_b)/2) [prod_nu s(p_nu)] s(p_a) s(p_b) i p_b, and a_b(p) Jhat_b is the same with -i p_a. Here 1 - exp(-i p_b) = exp(-i p_b / 2) i p_b s(p_b). So the current is the curl of the scalar rho-hat, the transform of rho_ab. By (B-4), P_infinity(z) is the integral of |rho-hat|^2 (p_a^2 + p_b^2) / |p|^2 exp(-i p . z), and (p_a^2 + p_b^2) / |p|^2 is the transform of (-d_a^2 - d_b^2)(1 / (4 pi^2 r^2)) = M. []

**Near and far values [computed, `checks/witness/near_flux.py`, W2].** The supports of parallel (1, 2) plaquettes for (B-1) are strictly ordered from offset (3, 3, 2, 2). Enclosures come from exact spline masses and monotone bounds of M on sub-boxes. Rounding is far below their width.

| z | enclosure of P_infinity(z) | Fourier (B-4) | Maxwell M(z) |
|---|---|---|---|
| (3, 3, 2, 2) | [-6.011e-5, -5.092e-5] | -5.537e-5 | -5.765e-5 |
| (3, 3, 2, 3) | [-2.021e-5, -9.96e-6] | -1.486e-5 | -1.701e-5 |
| (3, 3, 2, 4) | [3.76e-6, 6.11e-6] | 4.92e-6 | 3.69e-6 |
| (6, 6, 4, 4) | [-3.907e-6, -3.256e-6] | -3.569e-6 | -3.603e-6 |
| (6, 6, 4, 8) | [1.79e-7, 3.24e-7] | 2.50e-7 | 2.31e-7 |
| (9, 9, 6, 6) | [-7.53e-7, -6.67e-7] | -7.09e-7 | -7.12e-7 |
| (9, 9, 6, 12) | [3.83e-8, 5.65e-8] | 4.70e-8 | 4.56e-8 |

So z_n = (3, 3, 2, 2), z_f = (3, 3, 2, 4), t = 2, is a pair with (P_n)^2 at least 69 times (P_f)^2, and at P^fib = P_infinity the enclosures give a >= 3.8e-9. The sign change along t is the Maxwell one. This is much better than the pair (d, d, 2d, 2d), (d, d, 2d, 3d) of Corollary 4.2.

**Fibre split [computed, `checks/witness/fibre_split.py`, `fibre_edge.py`, W3].** With the span of the coarse closed currents pulled back to level j, delta_pq := P^inf_pq - P^fib_pq is the P-inner product of the projections of the two currents on that span. Thus delta >= 0 as a form and |delta_pq|^2 <= delta_pp delta_qq. In Bloch form it is a 3 x 3 Schur complement per coarse momentum. The pair sits at p = (-2, -2, -1, -1), q_n = (1, 1, 1, 1), q_f = (1, 1, 1, 3), around a block centre, n -> infinity.

| L | delta_pp | delta_(p q_n) | delta_(p q_f) | P^fib near | P^fib far | a_L |
|---|---|---|---|---|---|---|
| 3 | 9.34e-3 | 1.479e-4 | -1.05e-5 | -2.03e-4 | 1.54e-5 | 6.2e-8 |
| 5 | 9.34e-4 | -9.11e-5 | -2.02e-5 | 3.58e-5 | 2.51e-5 | 1.0e-9 |
| 7 | 1.32e-4 | -2.78e-6 | 8.7e-7 | -5.26e-5 | 4.05e-6 | 4.1e-9 |
| 9 | 3.45e-5 | 4.62e-6 | 4.41e-6 | -6.00e-5 | 5.1e-7 | 5.4e-9 |
| 15 | 2.91e-6 | 1.51e-6 | 1.44e-6 | -5.69e-5 | 3.48e-6 | 4.8e-9 |
| 21 | 6.54e-7 | 4.68e-7 | 4.57e-7 | -5.58e-5 | 4.47e-6 | 4.6e-9 |

L^4 delta_pp at a block centre: 0.120, 0.112, 0.109, 0.108 at L = 9, 15, 21, 33. At a plaquette straddling a block corner in its plane: 2.59, 2.90, 3.04, 3.17, which still rises slowly. So kappa = 2 in the Gaussian theory of this map, at most up to a logarithm at block edges. This is a computed trend, not a bound. As L -> infinity, a_L tends to (3/2)(P_n^2 - P_f^2), about 4.6e-9, and for L >= 7 it is within 20 percent of that.

The limit P^fib_(n,S) -> P^fib_infinity for this Schur complement follows from the domination (B-5) at each coarse momentum, with the coarse Gram matrix non-singular away from zero momentum. That is not written line by line [unchecked]. The bound |P^inf_pq - P^fib_pq| <= C_5 L^(-2 kappa) of Text 10 is what the corollary consumes, with P^inf -> P_infinity discharged by (B-4).

**Other maps.** The mapped attempt has its own first jet. If its blocked plaquette flux is an average of F_ab against a density of unit mass, radius w and zero first moment about the plaquette centre, then P(z) = M(z) (1 + O(w^2 / |z|^2)) at large |z|, and the offsets scale with w. [implication, not computed for that map.]

## 5. Reach and what stays open

Corollary NT1-F proves no fact about Wilson. Open, as producer clauses: (GS_j)(a) and (LE_j) at the printed L-dependence, (OS_j)(c'), (FF_(j+1)), (FT), H-NET, H-SCALE, and w free of L. The interface table in `parts/upper-chain.md` records (GS_j)(a) as not stated in this form on the independent map, whose 4.7c has g^eta and small-support restrictions, and as stated and unproved on the mapped map. An additive omega^GS_j -> 0 is all this theorem needs from it. (FT) is new as a separate request: a Laplace expansion of one product of two plaquette energies at one field, W = 1, on one fibre.
