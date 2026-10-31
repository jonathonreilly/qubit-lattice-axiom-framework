# Low orders of a gauge-invariant local function: vanishing, contraction, and rough fields

Producer: `parts/hard-core--mapped.md`, Text 5.5. Status: labelled step by step below. Not reviewed.

Credit. Extraction of the marginal term from the second variation at the trivial background is Balaban's organisation. He works with analytic polymer activities and Cauchy bounds, in an axial gauge on each polymer. The argument here is on real fields and is mine. It does not use the account.

Consumers: the real one-step theorem (uniformity of R_k in k), (P2).

## Setting

Z is a real gauge-invariant function on fields of the level-k lattice in the class. It is invariant under lattice translations, the hypercubic group and the reflection x -> -x, with A_mu(x) -> -A_mu(-x). It obeys Z(1) = 0, has tree-decay derivative norms ||Z||_n up to some N >= 6, and locality, (Loc), in the form given in Text 5.3.

Data: Pi^(n) := D^n Z(1) for n = 2, 3, 4, with symbols Pi-hat^(n)(q_1, ..., q_{n-1}), analytic in a strip |Im q| < mu because the kernels decay exponentially. Write |q| for the maximum of the arguments.

## Lemma 1 (vanishing orders). Proved here.

Let Z be as above, and let the F^2 coefficient vanish: Pi-hat^(2)(q) = O(|q|^3). Then Pi-hat^(2) = O(|q|^4), Pi-hat^(3) = O(|q|^3), Pi-hat^(4) = O(|q|^2).

In general, without the assumption on the F^2 coefficient, the Taylor coefficients of total weight at most 5 of Pi^(2), Pi^(3), Pi^(4) are those of c A, where A is the Wilson action and c a single number.

*Proof.* Take a smooth compactly supported connection a on R^4, and on the lattice put V_eps(b) := the parallel transport of the connection eps a(eps y) dy along the bond b. A smooth compactly supported gauge transformation g acts on V_eps as a lattice gauge transformation, g(eps x) V_eps(b) g(eps x')^-1, and sends a to a^g. So the function I_eps[a] := Z(V_eps) obeys I_eps[a^g] = I_eps[a] exactly.

Expand. The bond variable is log V_eps(b) = eps a_mu(eps y_b) + O(eps^3), at the bond midpoint y_b, where the next terms have weight at least 3 and the midpoint choice removes weight 2. Inserting in the Taylor series of Z at 1, and using the decay of the kernels to expand the slowly varying a, gives

    I_eps[a] = sum_{m} eps^{m-4} J_m[a] + O(eps^{N'}),    J_m[a] := integral W_m[a](y) dy,

where W_m is a polynomial in a and its derivatives of total weight m, with weight(a) = weight(d) = 1. The coefficients of J_m are the Taylor coefficients of total weight m of the Pi^(n), n <= m, up to lower-order mixing from the higher terms of log V_eps, which is triangular. Each J_m is separately gauge invariant, since the identity holds for all eps.

Reflection flips the sign of a and of each derivative, so J_m = 0 for odd m.

m = 2: J_2 = c^{mu nu} integral tr a_mu a_nu. To lowest order in a, invariance under a -> a + d omega gives c^{mu nu} integral tr a_mu d_nu omega = 0 for all a, omega. So c = 0.

m = 4: J_4 = J_4^(2) + J_4^(3) + J_4^(4), by degree in a. Invariance at lowest order says J_4^(2) is invariant under a -> a + d omega. Its symbol is hypercubic and of second order: a delta_{mu nu} q^2 + b q_mu q_nu + c' delta_{mu nu} q_mu^2. Contracting with q_mu gives (a + b) q_nu q^2 + c' q_nu^3 = 0, so c' = 0 and b = -a. Thus J_4^(2) is a multiple of the quadratic part of integral sum tr F_{mu nu}^2. Subtract that multiple of the continuum action; the rest has no quadratic part. Its cubic part, at lowest order, must be invariant under the abelian shift. A cubic of weight 4 has one derivative, and it cannot be built from d a alone, which would need weight 6. So it vanishes, and likewise the quartic, which has no derivative. So J_4 = c integral sum tr F^2.

With the F^2 coefficient zero, J_m = 0 for m <= 5. Hence all Taylor coefficients of Pi^(n), n <= 4, of total weight at most 5 vanish. For fixed n this says Pi-hat^(n) = O(|q|^{6-n}). QED

## Lemma 2 (contraction of divided norms). n = 2 derived here at the trivial background; n = 3, 4 by the same scaling, with the symbol bounds of D^j V* as input.

Let c_k^(n) := sup over the strip of |Pi-hat_k^(n)(q)| / min(|q|, 1)^{6-n}. By Lemma 1 and analyticity, these are finite when the F^2 coefficient is removed, and bounded by the undivided norm through Cauchy.

Let Ghat be the lift: for a level-(k+1) field A', the level-k field is L^-1 (Ghat A')(x) to first order. Normalise Ghat so that constants lift to constants.

`Lift symbol` (derived at the trivial background from the block symbol, given uniform bounds on the level-k form h with h(q) comparable to |q|^2). In Feynman form, with q_n := p + 2 pi n in level-(k+1) units and tau the one-step block symbol, Ghat-hat(q_n) = h^-1(q_n) tau*(q_n) / G(p), where G(p) := sum_n |tau(q_n)|^2 h^-1(q_n) >= |tau(p)|^2 h^-1(p). So for n != 0,

    |Ghat-hat(q_n)| <= C (|p|^2 / |q_n|^2) |tau(q_n)|,

the factor |p|^2 coming from the massless n = 0 term in the denominator. With |tau(q_n)| at most C |p_nu|/|n_nu| per direction nu with n_nu != 0, this gives |Ghat-hat(q_n)| <= C |p|^3 / |n|^3 on the axes, and more off the axes. Hence sup_p sum_{n != 0} |n|^4 |Ghat-hat(q_n)|^2 / |p|^6 <= C_al, with C_al free of L, the sum converging as sum n^-2 on axes. The same bound at a small background is a perturbation, with the constants of Theorem 6 of the energy package.

**n = 2.** Z o V* has second variation at 1 with symbol

    Pi-hat_{k+1}(p) = L^2 sum_n Ghat-hat*(p + 2 pi n) Pi-hat_k((p + 2 pi n)/L) Ghat-hat(p + 2 pi n).

The factor is L^4 for the sum per level-(k+1) cell times L^-2 for the two lifts. n = 0: |L^2 Pi-hat_k(p/L)| <= L^2 c_k |p/L|^4 = L^-2 c_k |p|^4. n != 0: |Pi-hat_k(q_n)| <= c_k (2 pi |n|/L)^4.

*No alias enters the F^2 coefficient (derived).* The minimiser over the fibre of a constant flux at level k+1 is exactly the constant flux at level k: this is Lemma 3.3 of the producer, because U_F is a critical point and M of an abelian configuration of constant curl has constant curl. By Lemma 3.4 there, for a local gauge-invariant function the F^2 coefficient is read by constant flux. So Z o V* has the same F^2 coefficient as Z, which is zero, and the alias sum has no p^2 term. This agrees with `Lift symbol`: the alias sum is at most L^-2 C c_k C_al |p|^6, which has no p^2 or p^4 term. So

    c_{k+1}^(2) <= C L^-2 c_k^(2) + (sources).

**n = 3, 4.** Z o V* has further terms from the non-linear lift, with D^j V* in level-(k+1) coordinates having symbols bounded by a constant times L^-1, because the level-k field is L^-1 times a non-linear function of the level-(k+1) field with L-free coefficients. For a term with Pi^(m) of the original and j_i derivatives of V*, the size is L^4 L^-m c_k^(m) (|q|/L)^{6-m} = L^-2 c_k^(m) |q|^{6-m}. For fixed n, m <= n, |q|^{6-m} <= |q|^{6-n} on the unit cell. So

    c_{k+1}^(n) <= C L^-2 max_{m <= n} c_k^(m) + (sources).

Status: the scaling is derived. The bounds on the symbols of D^j V* are the input `Lift symbol`, and aliases at n = 3, 4 are bounded the same way but not written out.

## Lemma 2, second proof (derived 2026-10-31; replaces `Lift symbol`, the "same scaling" at n = 3, 4 and the alias sums at small momentum; not reviewed)

*A gap in the first proof.* `Lift symbol` used the Feynman form, a lift with the whole gauge term, like Theorem 6 of the energy package. That is not the class response, `library/fibre-propagator.md`. The bound it gave for aliases is right for the transverse part of the class response, so the first proof at n = 2 stands after that correction. At n = 3, 4 it was not written.

*Tools.* (T1) *Schwarz.* By Lemma 1, Pi-hat^(n) vanishes to order 6 - n at q = 0, once the F^2 coefficient is removed. So on complex lines through 0, |Pi-hat^(n)(q)| <= (|q|/rho)^{6 - n} sup_{strip rho} |Pi-hat^(n)|. So c^(n) <= C rho^{-(6 - n)} sup_{strip rho} |Pi-hat^(n)|, and **no cancellation at small momentum has to be followed**: only sizes in the strip. rho must be free of L: Theorem F's Combes-Thomas gives the lift in a strip of absolute width delta_#, and Lemma HS-T gives the same for the source. *This is a consumer of the absolute rate that I had not seen.* With a rate rho(L), the factor rho^-(6-n) would compete with L^-2.

(T2) *Gauge-invariant form at n = 2.* Pi^(2) annihilates gradients, and it is local, so Pi^(2) = d^dagger rho d, with rho exponentially local, by a lattice Poincare lemma with local homotopy, and |rho(q)| <= c^(2) min(|q|, 1)^2 after the F^2 coefficient is removed.

(T3) *An exact identity.* For a fine field H: ||grad d H||_{L^2} = ||d^dagger d H||_{L^2}, at U = 1, as d (d H) = 0 and d d^dagger + d^dagger d = -Delta on 2-forms. The class response of Sad# solves d^dagger d H = -Q^{o*} mu. So ||grad d H||_{L^2} <= ||Q^{o*} mu||_{L^2} <= C |mu|, and with the conjugation of Theorem F the same with weights e^{kappa . x}, |kappa| <= delta_#/2. The gauge of H does not enter, since only d H does.

*n = 2.* The level-k field is f = L^-1 (tile average of H) in potential normalisation. In level-(k+1) units, with level-k momentum q/L: D^2 Z_k(1)[f, g] is at most c_k^(2) L^-2 ||grad d H_f|| ||grad d H_g|| per coarse cell: L^4 sites, L^-2 for the two fields, and |q/L|^2 from rho, while d on the level-k lattice reads L^-1 q, whose two factors cancel the potential normalisation of the curvature. Count: for a curvature theta_p = L^-2 F, sum over L^4 sites of theta_p rho theta_p <= L^4 L^-4 c (|q|/L)^2 |F|^2 = c L^-2 |q|^2 |F|^2. Averaging over tiles is a contraction in Fourier space. So

    sup_{strip} |Pi-hat^(2), mean_{k+1}| <= C L^-2 c_k^(2),   c_{k+1}^(2) <= C L^-2 rho^-4 c_k^(2) + source,

with C absolute. No alias sum and no bound on `Lift symbol` is used beyond (T3). Numerics: `checks/hard-core--mapped_data_contraction.py`, criteria written first, at the trivial background, one level: PASS, run once. Pi(L, p) L^{6-d}, sup over a grid: d = 2: 118, 171, 192, 201, 206 at L = 3, 5, 7, 9, 11, levelling off; d = 3: 193, 313, 368 at L = 3, 5, 7; d = 4: 271, 484 at L = 3, 5. All within the factor 2 of the smallest L stated, but d = 3 and d = 4 have not levelled off at these sizes, so they show the power only roughly (1.91 and 1.78 of the first value). The identity ||grad d H|| = ||d^dagger d H|| holds to 3e-15, longitudinal A' gives d H = 0 to 4e-15, and Pi at small p is level to 3 percent from s = 0.4 to 0.05, so no term of lower order feeds in. Limits: n = 2 only.

*n = 3, 4, same-order term.* D^n Z_k(1)[f, ..., f]. With |Pi-hat^(n)(q_1, ...)| <= c^(n) min(max_i |q_i|/L, 1)^{6 - n}, conservation of momentum means the two largest |q_i| are comparable, so max |q|^{6-n} <= C |q_1|^{(6-n)/2} |q_2|^{(6-n)/2}. The count is L^4 (sites) L^-n (fields) L^{-(6 - n)} = L^-2, times

    sum over momenta of |q_1|^{(6-n)/2} |H^(q_1)| |q_2|^{(6-n)/2} |H^(q_2)| prod_{i >= 3} |H^(q_i)| <= ||H||^2_{H^{(6-n)/2}} ( sum_q |H^(q)| )^{n-2}.

Here H is the class response in the gauge P_r D^* H = 0, in a strip. Its transverse part has |H^_T(q_n)| <= C |tau(q_n)| / |q_n|^2 for n != 0, and its longitudinal part is q-hat_n r-hat(q_n)^* c(p) / |q-hat_n|^2, with |r-hat(q_n)| <= prod_{n_nu != 0} (1/|n_nu|). So H is in H^{3/2 - eps} uniformly, as needed for n = 3, 4, and sum_q |H^(q)| over the level-k zone is at most C log L. So c_{k+1}^(n) <= C (log L)^{n - 2} L^-2 rho^-(6 - n) c_k^(n) + (lower) + source. *Note the gauge.* The longitudinal part does not vanish at n = 3, 4, and it enters as a size, not through a cancellation: Schwarz has taken over the small-momentum cancellations, which belong to the total, gauge invariant, function.

*n = 3, 4, lower terms.* D^2 Z[f_2, f], D^2 Z[f_3, f], D^2 Z[f_2, f_2], D^3 Z[f_2, f, f]: each has a lower c^(m), m < n, with coefficient C_n(L). So the recursion is triangular and these need only finiteness uniform in k, the (SB) at j >= 2 at the trivial background, where the operators do not depend on k except through eta. So the bound is

    c_{k+1}^(n) <= C (log L)^2 L^-2 c_k^(n) + C_n(L) sum_{m < n} c_k^(m) + source.

*Hostile.* (a) The strip of Z_k read at q/L has width rho/L in level-k units, which is within Z_k's own strip, since it has rate at least rho in level-k units by the same statement one level down. (b) The source: its F^2 coefficient is extracted first, and it is the source of beta^0 by Theorem P1; the rest is bounded by C_n(L) in the strip, by Lemma HS-T. (c) The slow tier of R: Schwarz in a narrower strip with a tiny coefficient, Lemma HS-T. (d) I checked only n = 2 numerically.

## Lemma 3 (low orders at a rough field). Derived, given (Loc).

For V in the class, x_1 given, a := the local flux, weighted by e^{-mu' d}, r := c a^{-1/2}, and n <= 4:

    D_{x_1...x_n} Z(V) = sum_{m=0}^{4-n} (1/m!) D^{n+m} Z(1)[A^{⊗ m}] (x_1...x_n) + O( ||Z||_5 |A|^{5-n} ) + O( C e^{-mu r/2} ),

where A is the field of V in axial gauge at x_1, cut off at r. Its size at distance y is at most a |y|, so |A| <= c a^{1/2} on the ball.

*Proof.* Deform V inside the ball by exp(i (s chi + 1 - chi) A), with chi = 1 near x_1, chi = 0 outside the ball. The flux stays within a factor 1 + C a r^2 of a, so the path stays in the formula range. At s = 0 the field is trivial on a ball of radius r/2, so its derivatives at x_1 differ from those of the trivial field by C e^{-mu r/2}: this needs only tree decay of the order-(n + 1) norm along a path of class fields, so (Loc) in its form with rough far data is not read (2026-10-31). Taylor expansion along the path gives the formula. QED

Consequently, for n <= 4, in the l^1 tree norm on the convex range:

    ||Z||_n <= C ( max_m c^(m) + ||Z||_5 T_f^{(5-n)/2} + e^{-mu/(2 T_f^{1/2})} ).

## How the recursion closes (design, with the steps above).

1. Order >= 5: ||R_{k+1}||_n <= C_1' C_1^{n-1} L^{4-n} ||R_k||_n + C(L) g_k^2 (lower norms) + source. For n = 5 the factor is C L^-1.
2. Data: c_{k+1}^(m) <= C L^-2 max c_k^(m) + C(L) g_k^2 (norms up to order 6) + source.
3. Low norms from the two above by Lemma 3.
4. Sources are the one-step functional at level k, bounded uniformly in k by the Laplace lemma. Its F^2 coefficient is beta^0.

So all norms stay bounded uniformly in k, for L large and then x_k large. By the no-alias statement, the F^2 coefficient of R_k o V* is zero after extraction, so the marginal coefficient at step k+1 comes from the one-step functional alone: beta_{k+1} = beta^0_{k+1} + O(C(L) g_k^2). The sum of beta^0 is k c_0 + O(1) by Theorem P1, and sum_k g_k^2 is of order log K, small against k c_0. So the flow bounds follow, with no sign information per step.

**Hostile notes.** (a) My first version of this note fed an alias term of size L^-2 c_k into beta_{k+1} and flagged it as non-summable. That was wrong: the exact lift of constant flux forbids it. The error is recorded because the same mistake would be easy to repeat in a plane-wave computation. (b) The no-alias argument uses that R_k is local and gauge invariant on small fields, so Lemma 3.4 of the producer applies uniformly in k. (c) The vanishing orders in Lemma 1 come from J_m[a^g] = J_m[a], with a single-axis reflection needed to exclude the term epsilon tr(a a d a). (d) `Lift symbol` is derived only at the trivial background, in the quadratic form; the non-linear lifts D^j V*, j >= 2, have symbol bounds that I have estimated by scaling and not derived.
