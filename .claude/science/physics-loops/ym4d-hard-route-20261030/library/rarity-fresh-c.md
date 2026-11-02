lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T16:58Z

# rarity-fresh-c: a full-mass producer with no frozen layer

Pinned at 914b36aec on claude/ym4d-hard-route. Mapped side, blind to `rarity-fresh-x`. Anthropic, claude-opus-5-5, effort max, one session, no subagents. Same-model research text, not an audit, no status. Labels: *discharged* (proved here, by hand), *implication* (proved here at the level of each term, given named inputs), *gap*. Nothing here rests on a run.

## 1. The route in one paragraph (draft, final verdict in Section 8)

**Read every rare event one level below the level it lives on, conditional on the exterior at that same level.** Every proof of rarity so far compares two fields across all levels (Theorem Z, (AE-R), (HW)), or needs a surface where the outside cancels exactly, and that surface is why there are frozen layers at all levels. Neither is needed to bound a probability. Given the level-k field off a bounded patch G and the parents, the law on G has density exp(-F_k), one function, and the exterior is literally the same in numerator and denominator. So the only inputs are a difference of F_k on G, and a volume. Fine fields never appear, so there is no heavy pack; no frozen datum appears, so there is no wall, no (QD), no junction.

## 2. Four lemmas proved by hand

Notation as in `library/quiet-boundary-rarity.md` (QB). F_k := -log rho_k, rho_k the density of the level-k field under the full hierarchy, so F_0 = x_0 A.

**Lemma EX (exit bound with the exterior held; discharged).** *Let (G, m) be a finite measure space, F: G -> (-inf, inf] measurable, mu proportional to exp(-F) m. For Q in G, D in G with m(D) > 0 and any number f_D >= sup_D F:*

    mu(Q) <= [ m(Q) / m(D) ] exp( f_D - inf_Q F ).        (2.1)

*Proof.* mu(Q) <= m(Q) exp(-inf_Q F) / integral exp(-F) dm, and the denominator is at least m(D) exp(-f_D). QED

The content is in what G is. Take G the level-k fields on a patch, with fixed exterior and fixed parents. Then F is F_k evaluated at (patch field, exterior), and Lemma EX holds with no stop, no layer and no Markov property: conditioning on the exterior at one level is legitimate because F_k is one function of the whole level-k field. If Q_1, ..., Q_n are events on disjoint patches and every replacement in turn gains at least g_i, whatever the other patches hold, then (2.1) applied to the product patch gives prod_i [m(Q_i)/m(D_i)] exp(-g_i). **So the product form for compatible marks costs nothing**: it is one inequality on the union, and the Bernoulli objection of `one-window` Section 6 does not arise.

**Theorem FC (force concentration, no chart, product form; discharged).** *Let M be a compact Riemannian manifold, m a finite measure with smooth density, O open, F in C^2(O), mu a probability proportional to exp(-F) m on M. Let X_1, ..., X_N be smooth vector fields compactly supported in O, Y_i := X_i F - div_m X_i, and suppose the symmetric part of the matrix (X_i Y_j) is at most B on O, with B > 0. Then E Y_i = 0, and for every a in (0, 1/(2B)):*

    E exp( a sum_i Y_i^2 ) <= (1 - 2 a B)^(-N/2).        (2.2)

*So with a = 1/(4B): P( Y_i^2 >= s for all i in I ) <= 2^(|I|/2) exp( -|I| s / (4B) ) for each subset I.* There is no convexity hypothesis on F.

*Proof.* Integration by parts gives E[X g] = E[g Y] for X compactly supported in O, Y := X F - div_m X, g in C^1. Fix t in R^N, X_t := sum t_i X_i, Y_t := sum t_i Y_i, and g = exp(s Y_t). Then E[Y_t exp(s Y_t)] = s E[(X_t Y_t) exp(s Y_t)]. For s >= 0, with phi(s) := log E exp(s Y_t), this gives phi'(s) <= s B |t|^2, so E exp(Y_t) <= exp(B |t|^2 / 2). For g standard Gaussian in R^N, the Gaussian generating function gives exp(a |Y|^2) = E_g exp((2a)^(1/2) <g, Y>). Fubini and the previous bound at t = (2a)^(1/2) g give E exp(a |Y|^2) <= E_g exp(a B |g|^2) = (1 - 2aB)^(-N/2). Sub-families and Chebyshev give the rest. QED

*Level 0.* With left-invariant fields on the links of a set S, conditional on all other links: if exp(t tau) has angle t, then d^2/dt^2 (1 - (1/2) tr(exp(t tau) S)) = (1/2) tr(exp(t tau) S), which lies in [-1, 1], and mixed second derivatives on one plaquette are at most 1 in size. So one plaquette's Hessian form is at most (sum_b |t_b|)^2 <= 4 sum_b |t_b|^2. Six plaquettes meet a link, so B = 24 x. With f_b := |grad_b A|,

    E[ exp( (x/96) sum_(b in S) f_b^2 ) | links off S ] <= 2^(3 |S| / 2).        (2.3)

Uniform in every other link, in volume and in every rough field. It is a full-law statement outside any chart. **It cannot price a rough field by itself:** (2.1) of `one-window` has f_b = 0 with rough neighbours, and any stationary non-minimal field has f = 0. It does price every pack at a fixed amplitude: M pairs of amplitude a cost at most exp(-c x M sin^2 a), by this line alone. On a fibre the same proof runs with X_i tangent to the fibre. *Its use below is limited (Section 4, S1); the hypothesis it needs at level k is an upper Hessian bound, which survives integration because -Cov has the good sign. An all-depth semi-concavity bound fails by L^2 per level, since dropping Cov loses the gauge cancellation of the mass term; I do not use one.*

**Lemma RANK (parent windows, no rank assumption left; discharged at the scope of (JW) of `one-window`, implication in general).** *Fix a label pattern l, with retained parents R. Suppose each c in R has a private face bond g_c: a fine bond crossing the face between the two blocks of c, along the direction of c, on s_c >= 1 surviving lines of c, off the hull. Let S_c be the surviving lines of c, and K the set of U with flux at most 2 T on every cell not labelled rough. Suppose that on K the surviving lines of c, read in the frames of the block centres, lie within angle theta_0 <= 1/8 of one another, and their transports up to g_c within theta_0 of one another. Then for all parent values W with angle(W_c) <= 1/8 on R, and 0 < eps <= 1/16,*

    integral dU 1_K(U) prod_(c in R) 1( M_l(U)_c in B_eps(W_c) ) <= prod_(c in R) [ C ( |S_c| / s_c )^3 ] h(eps)^|R|,        (2.4)

*with C absolute and h(eps) = Haar(B_eps). In particular, for L^4 lines, s_c >= L: at most (C L^9)^|R| h(eps)^|R|, uniformly in the volume.*

*Proof.* *Privacy.* A contour Gamma_(y,x) stays in its block, and the face bond lies in no block. Among straight segments [x, x + L e_mu], x in B(y), only those of parents (y, y + L e_mu) cross that face: the parents before and after it stop at or start after the face (Text 3.1, read as in `one-window` Section 5). So row c alone reads g_c. Fix all bonds except the g_c. Then the rows are functions of separate variables, and the integral factors. *One row.* On K each of the six plaquettes at g_c has angle at most 2 T, so g_c lies in a ball of radius 4 T about a point fixed by the other bonds. Write g_c = exp(i xi) g_c^0. For the s_c lines through it, ell_x(xi) = A_x exp(i xi) g_c^0 B_x, and the parent is exp(Phi(xi)), Phi = |S_c|^-1 sum_x log ell_x. So D Phi = |S_c|^-1 sum_(x through g_c) (D log)_(ell_x) Ad(A_x). The derivative of log at an angle at most 1/4 is within 1/4 of the identity, up to a factor, and the Ad(A_x) are within 2 theta_0 of one common rotation. So D Phi = (s_c / |S_c|) Ad(A) (1 + E), |E| <= 1/2. Thus Phi is injective on the ball, with Jacobian at least (s_c / (2 |S_c|))^3, and Haar measure is within a constant of Lebesgue measure at these angles. The preimage of B_eps(W_c) has Haar mass at most C (|S_c|/s_c)^3 h(eps). The remaining integrals are at most 1. QED

**(JW) of `one-window` is therefore true** at its stated scope: there P(l_0|U) <= 1_K, because a cell off C_0 labelled 0 has weight 1 - chi(flux) = 0 at flux at least 2 T; the core is one bond, whose hull leaves a block simply connected, so two surviving lines bound a surface off the hull of area at most C L^2 and flux at most 2 T per cell; this gives theta_0 <= C L^2 T = C a_*, which is at most 1/8 since a_* <= a_th(L) in the order of constants at Text 5.10. A column far from the core has s_c = L. So (JW) holds with B_0 = (C L^9)^|R_0|, and (5.4) of that note follows at once. **The general hypothesis** (surviving lines within theta_0 at a general hull) is the rule that the hull spans 2-cycles (Text 5.2): an S^2 of rough cells in a block has linking circles in the complement, and only its spanning 3-chain removes them. For a large hull that step reads `Cut and Poincare`; I checked it for a ball and for a sphere, not in general. That is why the general form is an implication.

**Lemma PER (a value difference by periodization; discharged).** *Let Phi be a real function on configurations of a torus T, covariant under a translation group acting freely on T. Let Q_1, ..., Q_N be disjoint translates of a box Q, and a, a' two configurations on Q, equal near the boundary of Q. Write Psi_m for a' on Q_1, ..., Q_m and a on Q_(m+1), ..., Q_N, with a fixed periodic configuration e elsewhere. Suppose |Phi(Psi_m)| <= B n for all m, and that changing from a to a' on one box is independent of what the other boxes hold, up to eps:*

    | [Phi(a', omega) - Phi(a, omega)] - [Phi(a', omega') - Phi(a, omega')] | <= eps        (2.5)

*for omega, omega' agreeing near that box. Then for each such omega, |Phi(a', omega) - Phi(a, omega)| <= 2 B n / N + eps.*

*Proof.* Phi(Psi_N) - Phi(Psi_0) = sum_m [Phi(Psi_m) - Phi(Psi_(m-1))], and each term is within eps of D := Phi(a', omega) - Phi(a, omega). So N |D| <= 2 B n + N eps. QED

No path joins a to a'. So this reads a value difference across a topological sector from a bound on absolute values, with no class path. With n/N about |Q|, it says: a bound per unit volume plus near-additivity gives a bound per box. This is what `library/sector-values.md` asked of (Jump), by another means.
