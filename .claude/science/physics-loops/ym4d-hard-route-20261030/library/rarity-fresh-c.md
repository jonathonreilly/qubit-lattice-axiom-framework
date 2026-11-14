lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T16:58Z

# rarity-fresh-c: a full-mass producer with no frozen layer

Pinned at 914b36aec on claude/ym4d-hard-route. Mapped side, blind to `rarity-fresh-x`. Anthropic, claude-opus-5-5, effort max, one session, no subagents. Same-model research text, not an audit, no status. Labels: *discharged* (proved here, by hand), *implication* (proved here at the level of each term, given named inputs), *gap*. Nothing here rests on a run.

## 1. The route in one paragraph

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

Uniform in every other link, in volume and in every rough field. It is a full-law statement outside any chart. **It cannot price a rough field by itself:** (2.1) of `one-window` has f_b = 0 with rough neighbours, and any stationary non-minimal field has f = 0. It does price every pack at a fixed amplitude: M pairs of amplitude a cost at most exp(-c x M sin^2 a), by this line alone. On a fibre the same proof runs with X_i tangent to the fibre. *It is not used in S1 to S6. At level k it would need an upper Hessian bound on F_k, which survives integration because -Cov has the good sign. An all-depth semi-concavity bound fails by L^2 per level, since dropping Cov loses the gauge cancellation of the mass term; I do not use one.*

**Lemma RANK (parent windows, no rank assumption left; discharged at the scope of (JW) of `one-window`, implication in general).** *Fix a label pattern l, with retained parents R. Suppose each c in R has a private face bond g_c: a fine bond crossing the face between the two blocks of c, along the direction of c, on s_c >= 1 surviving lines of c, off the hull. Let S_c be the surviving lines of c, and K the set of U with flux at most 2 T on every cell not labelled rough. Suppose that on K the surviving lines of c, read in the frames of the block centres, lie within angle theta_0 <= 1/8 of one another, and their transports up to g_c within theta_0 of one another. Then for all parent values W with angle(W_c) <= 1/8 on R, and 0 < eps <= 1/16,*

    integral dU 1_K(U) prod_(c in R) 1( M_l(U)_c in B_eps(W_c) ) <= prod_(c in R) [ C ( |S_c| / s_c )^3 ] h(eps)^|R|,        (2.4)

*with C absolute and h(eps) = Haar(B_eps). In particular, for L^4 lines, s_c >= L: at most (C L^9)^|R| h(eps)^|R|, uniformly in the volume.*

*Proof.* *Privacy.* A contour Gamma_(y,x) stays in its block, and the face bond lies in no block. Among straight segments [x, x + L e_mu], x in B(y), only those of parents (y, y + L e_mu) cross that face: the parents before and after it stop at or start after the face (Text 3.1, read as in `one-window` Section 5). So row c alone reads g_c. Fix all bonds except the g_c. Then the rows are functions of separate variables, and the integral factors. *One row.* On K each of the six plaquettes at g_c has angle at most 2 T, so g_c lies in a ball of radius 4 T about a point fixed by the other bonds. Write g_c = exp(i xi) g_c^0. For the s_c lines through it, ell_x(xi) = A_x exp(i xi) g_c^0 B_x, and the parent is exp(Phi(xi)), Phi = |S_c|^-1 sum_x log ell_x. So D Phi = |S_c|^-1 sum_(x through g_c) (D log)_(ell_x) Ad(A_x). Each ell_x has angle at most 1/2 in the frame (the window, eps, and theta_0), the derivative of log at such an angle is within 1/4 of the identity, and the Ad(A_x) are within 2 theta_0 of one common rotation. So D Phi = (s_c / |S_c|) Ad(A) (1 + E), |E| <= 1/2. Thus Phi is injective on the ball, with Jacobian at least (s_c / (2 |S_c|))^3, and Haar measure is within a constant of Lebesgue measure at these angles. The preimage of B_eps(W_c) has Haar mass at most C (|S_c|/s_c)^3 h(eps). The remaining integrals are at most 1. QED

**(JW) of `one-window` is therefore true** at its stated scope: there P(l_0|U) <= 1_K, because a cell off C_0 labelled 0 has weight 1 - chi(flux) = 0 at flux at least 2 T; the core is one bond, whose hull leaves a block simply connected, so two surviving lines bound a surface off the hull of area at most C L^2 and flux at most 2 T per cell; this gives theta_0 <= C L^2 T = C a_*, which is at most 1/8 since a_* <= a_th(L) in the order of constants at Text 5.10. A column far from the core has s_c = L. So (JW) holds with B_0 = (C L^9)^|R_0|, and (5.4) of that note follows at once. **The general hypothesis** (surviving lines within theta_0 at a general hull) is the rule that the hull spans 2-cycles (Text 5.2): an S^2 of rough cells in a block has linking circles in the complement, and only its spanning 3-chain removes them. For a large hull that step reads `Cut and Poincare`; I checked it for a ball and for a sphere, not in general. That is why the general form is an implication.

**Lemma PER (a value difference by periodization; discharged).** *Let Phi be a real function on configurations of a torus T, covariant under a translation group acting freely on T. Let Q_1, ..., Q_N be disjoint translates of a box Q, and a, a' two configurations on Q, equal near the boundary of Q. Write Psi_m for a' on Q_1, ..., Q_m and a on Q_(m+1), ..., Q_N, with a fixed periodic configuration e elsewhere. Suppose |Phi(Psi_m)| <= B n for all m, and that changing from a to a' on one box is independent of what the other boxes hold, up to eps:*

    | [Phi(a', omega) - Phi(a, omega)] - [Phi(a', omega') - Phi(a, omega')] | <= eps        (2.5)

*for all configurations omega, omega' off that box (Q contains the collar on which a, a' agree). Then for every omega, |Phi(a', omega) - Phi(a, omega)| <= 2 B n / N + eps.*

*Proof.* Phi(Psi_N) - Phi(Psi_0) = sum_m [Phi(Psi_m) - Phi(Psi_(m-1))]. By covariance the m-th term is a change from a to a' on Q_1 with some exterior, so by (2.5) it is within eps of D := Phi(a', omega) - Phi(a, omega). So N |D| <= 2 B n + N eps. QED

No path joins a to a'. So this reads a value difference across a topological sector from a bound on absolute values, with no class path. With n/N about |Q|, it says: a bound per unit volume plus near-additivity gives a bound per box. This is what `library/sector-values.md` asked of (Jump), by another means.

## 3. State and inputs

**State.** The mapped one-function state on the torus, with no boundary datum: F_k on all level-k fields; on class fields (flux at most T_2) F_k = x_k A_k + vac_k |cells| + R_k. The rough part of the state is not a bound on F_k at rough fields. **There is none.** (RP'), (Z) and every lower bound on F_k at a rough field are dropped from the producer. A rough field enters in only two ways: through the branch of its density whose children are class, where the class formula holds (S2); or at a lower level, where it is class (S3).

**Inputs, all from the regular package, all on the torus, all with no frozen data.** None is proved here.

- (I_k), with (Loc_k) in the form of Text 5.3, including its first-order tail at a distance d >= d_1 from cells above T_2: |D_y (F_k - x_k A^B)| <= C + C x_k e^{-mu d}. Rough far data allowed.
- Theorem VAL of `library/sector-values.md` Section 4: on a torus, for globally class V, in every sector, |R_k(V)| <= B_v (I^grad_k(V) + f(V) E_k(V) + toron term), with B_v free of x and of the charge.
- (ADD_k): across a class shell, F_k(p, m, q) = u(p, m) + v(m, q) + E with |E| <= eps(shell). This is Step 3 of Prop MD, Text 5.3, one level at a time, with base E = 0 at level 0, since A is local. It needs no path in p or q, and it allows holes.
- F-D and the lift bounds at class backgrounds: `library/fan-ext.md`, `library/c0-loc.md`, `library/lc-u.md`, as gated, on the admitted domain.
- The chart fill: for a class top, a class stationary lift in the same fibre, and a local competitor on a patch: the `fill-supply` row.

**One choice of constants, used below:** a_* <= epsilon_1 / (C A_f L^2), allowed by the order "L, then a_* <= a_th(L)" of Text 5.10. Then a level-k field of flux at most L T_2 = 2 A_f a_*/L has energy below epsilon_1^2 on every patch of radius C L.

**Definitions at level k.** A *hole* of V_k is a cell above T_2 or a labelled cell. Holes other than the mark being priced are kept: a labelled cell of flux in (T, T_2] is also a hole, so numerator and denominator have the same label pattern near it, and the same map M_l. Only the mark itself changes its label, and S1 handles that by comparing fibre minima, with no restoration. *So Lemma REST and every exact restoration across labels are gone.* A parent is *mild* near c if its flux is at most L T_2 (its lift is class) or it is Haar. The *collar* of a hole is its d_1 neighbourhood, with d_1 >= (1/mu) log(C / T^2), the constant of RD. A box is *dense* if it holds at least m_* labelled cells; its parents are Haar.

## 4. The route, step by step

**S1. Marks on class patches: full law, one level (implication; reads (I_k), (Loc_k), F-D, RANK, EX).** Fix V_(k+1), and a level-k brick b with patch P, parents class on P. Condition on V_k off P, on all holes of V_k and their collars, and on the *site data* omega: the level-(k-1) field within d_x of the shadows of holes. Let G be the free bonds of P off the collars. *The site data are needed:* within d_x of a hole F_k itself is a mixture of wells, with Hessian negative at strength x e^{-2 mu d} in B units (Text 5.3), so (Loc_k) alone gives no coercivity there; given omega the wells are resolved, and P(event) = E_omega P(event | omega) keeps the bound. On the event that b is non-quiet and V_k is class on G: let F(. | omega) := -log Inner(omega; .) as in the local form of Theorem OS, and V° its minimiser on G, given the exterior, the holes and the parents. It lies in the convex chart, since G is class. So

    F_k(V) - F_k(V°) >= c x_k Dev_b(V) - C n >= (c/2) x_k eps_q^2 T^2   for x_k >= x_*,

given that V° is within eps_q T / 2 of Lift_b on b (decay of the response, and the tail from holes at distance d_1). Lemma EX, with D the ball of radius x_k^(-1/2) about V° and (2.4) for the numerator's volume, gives P(b non-quiet, b class | rest) <= exp(-c x_k eps_q^2 T^2) =: z^Q_k. This holds **for every exterior**, rough or not, so it is the rarity that Lemma FIB gave only on the chart. Disjoint patches multiply, by Lemma EX on the union. A cell of flux in (T, T_2] makes its brick non-quiet (quiet bricks have flux at most T/2), so a labelled class cell is priced here too, in the band that QB left unpaid. *The label changes between numerator and denominator, and no restoration is needed.* The numerator is in branch l, with M_l(V) = V'; the denominator is the minimiser V° of A_k over the label-0 fibre of V', with the same exterior. Write M_0(V) = V' + Delta. Only lines through the hull differ, so |Delta| <= C (|hull lines| / L^3) L^2 T_2. If the hull's lines are rough, first replace V on the hull by a class fill V^nat (own-level energy, small hull): this lowers the energy and keeps |Delta| that small. The class fibre minimum is Lipschitz in its parents, with multiplier |lambda| <= C T by F-D. So A_k(V) >= A_k(V^nat) >= min A_k over the fibre of (V' + Delta), which is at least A_k(V°) - C T |Delta| - C |Delta|^2, and the gain survives, since C T |Delta| << T^2. (2.4) bounds both fibres' volumes. *Patches are clusters:* take P the cluster of non-quiet bricks at range 2 bricks; its boundary bricks are quiet, so V° next to them has flux at most T/2 by Lemma ST at one level, with the exterior field as data. All its labels are then 0 with weight one.

**S2. A rough cell whose children are class (implication; reads S1 at level k, the constants of Section 3).** Let c be a level-k cell above T_2 under class parents, not in a dense box, with its children class off holes. Take the patch P to be the cluster of such cells and of non-quiet bricks, with quiet boundary, as in S1, so that its minimiser has flux at most T by Lemma ST. Then the numerator's branch is rho^cl_k(V), the part of the density with class children near c, and rho^cl_k obeys the class formula with F_k^cl = x_k A_k + O(1) per bond at any V with flux at most L T_2: its proof reads only the children, and (R3) gives a lift of flux at most C_r f/L. (A smooth V would allow L^2 T_2; an oscillating one does not. Above L T_2 the children are rough: S3.) Class parents force the block average of V to have flux at most T_2 / L^2 on a block, so flux above T_2 on c is an oscillation at block scale, and it is not stationary. By the choice of a_*, a patch of radius C L has energy below epsilon_1^2. Expanding about the patch minimiser V°, which has flux at most T: A(V° e^h) - A(V°) >= c ||dh||^2 for ||dh||_2 <= epsilon_1, by the Sobolev bound on the fibre; the cubic term is at most C ||dh||_2^3. So the gain is at least c x_k T_2^2, and Lemma EX prices c. **No lump occurs here:** a lump in this branch has radius at least (L/(2 A_f a_*))^(1/2), above L; its parents see it, and they are not class.

**S3. A rough tower (implication; this is where a lump goes).** Now let the children of c be rough. Go down until the field is class: h(c) levels, h <= h_max bounded (Section 2 of `library/explicit-region-two-step.md`, row (f); a parent of flux f forces children of flux about f/L^2 only). Three cases, at each level of the descent.

(a) *Sparse rough children.* Fewer than m_* labelled cells per box. They are holes: kept, identical in numerator and denominator, and their collars removed from the changed region. The surviving lines then carry V, so c is priced by S1 or S2 at this level, with the holes as exterior. Summing over hole patterns H inside the changed region costs at most (1 + p)^|G| <= 2, by the product bound for holes at the lower level.

(b) *Dense children, not a lump.* The box is dropped and the parents of c are Haar. Then c is paid by the m_* labelled cells, with no energy read at c. These are level-(k-1) marks: the product comes from Lemma EX on their union, read at their own lower level. *This is the Haar plateau:* a rough cell costs at most C x m_* T^2 per box, whatever its flux, so no statement of the form "cost c x flux^2" holds at flux above sqrt(m_*) T, and (I_k) is limited to T_2^2 << m_* T^2. Text 5.8 records the price; I record that it also bounds what any producer can deliver.

(c) *A tower down to a class level m, with a lump.* A cluster of rough cells over levels m + 1, ..., m + j, class at m. Example: a lump of radius about T^-1/2 at level m, hidden under a class top at level m + j + 1, with j about log_L(1/sqrt(a_*)) + 1. It is stationary at every level, and every local gain is zero. The only competitor is the same field with the lump removed: **a different sector.** Read at level m: W class with the lump on J, W' class without it, equal off J, with the same higher parents off the tower. Then

    F_m(W) - F_m(W') = x_m (A_m(W) - A_m(W')) + [ R_m(W) - R_m(W') ].

Energy gives 2 pi^2 (1 - small). So what is needed is

    | R_m(W) - R_m(W') | <= B' (1 + I^grad_m(W) + I^grad_m(W') + f E_m),   W = W' off J, both class near J, any sector, any exterior beyond the collar,        (SEC_m)

with B' free of x. By Lemma PER, (SEC_m) follows from **Theorem VAL of `library/sector-values.md` Section 4, on the torus**, which holds in every sector and gives |R_m(V)| <= B_v (I^grad + f E + toron) with no constant per unit of charge, together with (ADD_m): take Q_i disjoint translates of a box holding J and its collar, in a flat background; Phi = F_m - x_m A_m - vac; the Psi_m are globally class; (2.5) is (ADD_m) across the collar, whose thickness is C log(x |Q|) so that the error of Prop MD is below 1. *So the region clause (VAL^𝔡), recorded as open, is not read.* A large J is cut into boxes of side C T^-1/2 and replaced one box at a time, since each intermediate field exists by (F2). With x_* >= C B' T^-2, the bracket does not matter, and the lump pays x_m. *A hole inside J* is kept, and it adds a cross term at the hole, bounded by (Loc_m) with its tail, by (ADD_m) across a shell about the hole.

**S4. The recursion for one cell (implication).** Let p_k be the supremum, over all data, of the conditional odds of a hole at level k, given the parents class or mild near it, and given the exterior and the site data. S1 to S3 give

    p_k <= z_k + C_L p_(k-1)^(m_*),   z_k := exp(-c(L, a_*) x_k T^2),        (4.1)

and p_k <= 2 z_k for x >= x_*, as m_* >= 2 and x_(k-1) >= x_k - C(L). **There is no factor N per level:** a sparse hole does not cause a rough parent, because the kernel excludes its lines. This is the step that defeats Proposition HOLES: holes are everywhere at a fine enough level, and none of them matters, since (a) reads them as exterior.

**S5. Marks at several levels (implication; the form of Theorem DM, with no data and no stop).** For a top V, regular near the marks, and a mark set M at levels at most i: split on V_i. Where V_i is class near a lower mark, the exact identity exp(-F_i^M(W) + F_i(W)) = Q_(i-1)(W; M_<) of DM Step 3(a) prices it, by induction, with coefficient one and no free bond. Where V_i is a hole near it, the mark pays through that hole, at one level's shift, as at QB:143. So

    P(all of M | V_r = W_r) <= prod_(b in M) z_b^(1/C_R),   C_R = C(L, a_*),        (4.2)

with own-level factors. A forced child under a very rough parent pays through that parent. A non-Haar parent has fewer than m_* labelled children, and its own price, at least x f^2 >= x L^2 T_2^2 by S2 or S3, covers them at x T^2 each, since L^2 T_2^2 >> m_* T^2. A parent with L^4 forced children has a dropped box and is Haar. So the rate per cell is kept. The column count of QB:101 is not needed, because nothing is summed over a column.

**S6. Under mu (implication).** Top level K has no parent, and Lemma EX holds at level K given the exterior. So (4.2) holds under mu, including stacks reaching K, with **no chessboard**: `one-window` Section 3 does not bear on this route.

## 5. What the attack on this route found

Each item was tried as a way to kill a step. The first four changed the route.

1. **Mixture of wells (S1).** The first form of S1 read coercivity from (Loc_k). Within d_x of a hole F_k is not convex, at strength x e^{-2 mu d}. Repaired by conditioning on site data, which is free for a probability. Not repaired by (Loc_k) itself.
2. **Flux range (S2).** The first form took the class formula up to L^2 T_2. (R3) gives only L^-1 for an oscillating parent, and an oscillating parent is what S2 is about. Repaired to L T_2; the rest goes to S3.
3. **An all-field Lipschitz bound |D F_k| <= C(L) x_k**, the first form of how to cut a rough chain. At a label surface the slope of log(1 - chi) is about x^2 for a flat chi, not x, because a branch of weight exp(-c x) lives where chi is that close to 1. Computing the two branches, the surface lies deep inside the Haar plateau, so the slope does no harm there. I dropped the bound anyway, once holes were kept: no rough chain is cut in this route.
4. **Two-level coercivity.** S2 first worked on the fibre over V_(k+1) at level k - 1. There the block is L^2 and the flux term T_2 L^4 beats the gap unless the background is the very smooth lift. Moved to level k, on a patch of radius C L.
5. **Crossing (fourth hostile pass of RD, the failure of (RP')).** A chain of rough children crossing the annulus to a forced region broke (RP'), because (RP') compares F at two rough-adjacent fields. Here children holes are kept in both numerator and denominator, so a chain is exterior wherever it runs. Only a dense box is read, and it is paid by its own cells. **(RP') is not needed, so this gap does not arise.**
6. **Proposition HOLES and the factor per level.** Holes fill every top cell at depth. A union bound "c is rough or some child near c is" gives p_k <= z_k + N p_(k-1), which diverges at d = 4. (4.1) has an exponent m_* instead, because the kernel excludes a hole's lines. If a sparse hole could move a parent by a non-rare amount, (4.1) would fail. Its influence is zero on the retained lines, by the kernel's definition. This is the main reason the route is not refuted by HOLES.
7. **Lemma TYP.** Nothing tests fine energy. S1 tests Dev_b at own level; S2, S3 test own-level or lower flux, on fields already integrated up to that level. No trigger reads a sum over a level-j cell at level 0.
8. **Lowering the class value with a Haar sheet.** A chain can free parents by dropping boxes, at m_* c T^2 per box, and might undercut the class value of a lump by dropping a shell around it. The interior keeps its energy unless all interior boxes drop, which costs m_* T^2 T^-2 = m_*, above 2 pi^2. So class minimality survives, with L large against A_f^2.
9. **Lemma RANK at a winding hull.** An S^2 of rough cells in a block has linking circles, and lines inside and outside it would differ by the holonomy around it. The hull's spanning 3-chain removes the inside lines. The general form of (2.4) stands or falls with `Cut and Poincare`.

## 6. Which consumers change

| Consumer | Change |
|---|---|
| (RAR^1), below regular tops, D empty | **Statement unchanged.** Producer is S1 to S5. Rate c(L, a_*) x_l T^2; the reader's alpha, l_1 are chosen after Theta, as at the interface |
| (RAR^ch), below regular tops | **Unchanged**, by (4.2), with C_R = C(L, a_*) |
| (RAR^1), (RAR^ch), under mu, stacks to K | **Unchanged in statement.** Producer S6. Lemma 10.6 and Lemma 1.2' are no longer read for own-level marks, and 22.3's flux route is not needed |
| (A1') | **Unchanged.** S4 gives it, conditional on the family. The polymer lemmas read nothing else from Theorem Z |
| Theorem OS, local form | The step "rarity of Omega near y'" reads S4 in place of the peel of RD. Its other steps are unchanged |
| (20.2), Lemma 22.2 | Unchanged; they read (RAR^1) |
| **(FF_j)(U), Text 5.8; Lemma 10.6, Theorem 10.7** | **Changes.** (FF_j)(U) as supplied, at Text 5.8:846, is a pointwise bound on the density at a rough field from (RP'_j), and this route has none. (FF_j)(Lo) is a class statement and stays. Lemma 10.6 prices rough fields under mu by a chessboard from (FF_j)(U); here S6 gives that rarity directly, with exponential moments of rough counts from (4.2). So Theorem 10.7 would read S6 in place of Lemma 10.6's (U) clause. I have not rewritten it |
| **(MD*), Lemma 20.3, Prop 20.4** | **Changes, or keeps a boundary induction.** (MD*) is stated between frozen layers at all levels, so it reads rarity with frozen data. S1 to S5 run unchanged with F_k^𝔡 in place of F_k, provided (I_k^𝔡), (Loc^𝔡), Lemma ST and (VAL^𝔡) hold uniformly in the data. That keeps the boundary-data induction and the open region clause, but it still needs no (HW), (LNC), (W2), (CI-paid^𝔡), Lemma OW or Theorem Z, because no chain is compared. The alternative is to rewrite Prop 20.4 so that it reads (ADD_j) and the conditional odds of S4 through a one-level Dobrushin comparison (Lemma 3 of `library/polymer-covariance.md`). That is unproved |
| (J+), (Resp+), (QD), (VAL^𝔡), (CI-paid^𝔡), (W2), Lemma OW, (LNC), (HW), Theorem Z, Theorem DM | Not read by any clause above; the first four only through (MD*) with data, the rest by none. None is refuted here. Lemma ST is still read, in its one-level form with the exterior field as data (S1) |
| Text 5.2 | One addition: labelled class cells are kept as holes. The kernel does not change |
| Order of constants | a_* <= epsilon_1/(C A_f L^2) and L large against A_f^2 are added. Both fit "L, then a_* <= a_th(L)" |

## 7. Where the route stops

**No step failed under attack, and none is proved in full.** The route is carried through at the level of each term, as an implication. Its inputs, in the order the induction reads them at level k:

1. **Regular package on the torus, no data:** (I_k); (Loc_k) in the local form of Theorem OS, with its site data; Theorem VAL (torus, every sector, reading SRC and Prop GS, so FALL, so the open row (UP)); (ADD_k) = Step 3 of Prop MD, with holes. Every mapped route reads these, Theorem Z included. Their closure reads rarity only through (A1') and the peel in Theorem OS, and S4 supplies both.
2. **Written here only at the level of a paragraph:**
   - S1: the multiplier bound |lambda| <= C T for the class fibre minimum, and its Lipschitz dependence on the parents. A standard consequence of F-D, but not displayed.
   - S3(c): the competitor W' without the lump, in the fibre of a top j + 1 levels up, restored by the same multiplier bound at each level of the tower.
   - Lemma RANK at a general hull: the surviving lines of a block lie within theta_0 of one another off the hull. This is the hull rule of Text 5.2 with `Cut and Poincare`. I checked a ball and a sphere.

**So the first step not carried to a proof is S1's multiplier bound for a label change** (item 2, first bullet). If it failed, a labelled class cell in (T, T_2] would not be priced, and every hole would have to be read with its label kept, which S1 cannot do: the mark is the label. Then the band (T, 2T] would be unpaid, as it is in QB. The other two bullets break only the lump case and the general hull.

**What the route does not supply.** (MD*) as stated reads rarity between frozen layers. S1 to S5 run with data only given (I^𝔡), (VAL^𝔡) and Lemma ST, so the boundary-data induction and the open region clause are still needed there, though (HW) and the chain statements are not. Making (MD*) free of data is a rewrite of Prop 20.4, proposed in Section 6 and not attempted.

## 8. Verdict

| Question | Answer |
|---|---|
| A complete route to a full-mass producer? | **Yes, as an implication at the level of each term, same-model and ungated.** It reads rough events one level below their own, conditional on the exterior at that level: Lemma EX, Lemma RANK, S1 to S6 |
| What it removes from rarity | Frozen layers, stops, (Z), (RP'), (AE-R), (HW), (LNC), (W2), (CI-paid^𝔡), Lemma OW, (J+), (Resp+), (QD), REST across labels, the region clause (VAL^𝔡), the chessboard, chart concentration, and Lemma U on any fine field |
| Raw fine energy (Lemma TYP) | Never tested. Every test reads one integrated level |
| Heavy wall | Not met. A wall is a frozen datum, and there is none. The heavy-wall example is a free pack below a frozen level-j bond, and here it is an integrated variable of F_j |
| Chart concentration not bounding the complement | Not used. Lemma EX bounds the full conditional law outside every chart, given only the exterior |
| Centre-plane chessboard fails | Not used, also under mu (S6) |
| Uniform local gain fails | Not used. Gains are per patch of radius C L, or per cluster, and are own-level |
| (HW) | Not refuted, and no longer needed by any rarity clause. It is still needed by Theorem Z, which no consumer of rarity now has to read |
| Proved by hand here | Lemma EX; Theorem FC, a full-law force bound in product form (a side result: it prices packs, it does not price rough fields); Lemma PER; Lemma RANK at the scope of (JW), **which settles (JW) of `one-window`**, with B_0 = (C L^9)^|R_0| |
| Consumers that change | (FF_j)(U), restated as a moment; (MD*), either rewritten or kept with data. RAR^1, RAR^ch, (A1'), (20.2) and Lemma 22.2 keep their statements |
| First step not carried | S1's multiplier bound for a label change (Section 7) |
| Most likely failure now | The regular package (Theorem VAL's FALL input, so (UP)), not rarity. A sparse hole that could move a parent by a non-rare amount would break (4.1); the kernel's line exclusion forbids it by definition |

## 9. Reading boundary

Read: FINISH.md, GOAL.md; `library/one-window.md`, `library/fill-supply.md`, `library/heavy-wall.md`, `library/explicit-region-two-step.md` in full; `library/quiet-boundary-rarity.md` Setting through Theorem DM, the proof of Theorem Z and Lemma OW; `library/relative-density-bound.md` Prop 8, its fourth hostile pass and items (f), (r); `library/sector-values.md` Sections 1, 4, 5, 6; `parts/hard-core--mapped.md` Text 3.1 (Lemma 3.1), Text 5 to 5.4 (lines 560 to 760), header and obligations searches; `parts/upper-chain.md` The interface, lines 175 to 216; `gates/energy-stages-codex-b87de884f.md`, verdicts and defects 1 to 5. Statements only, by search: `library/gas2.md` headings, (Loc^c), (VAL^𝔡).

Not read: `rarity-fresh-x`, `parts/hard-core--independent.md` or any gate on it, `library/shelling-by-hand.md`, `library/adapted-domains.md`, `library/tail-two-step*.md`, `library/mixed-coefficient*.md`, `library/conditional-normalization.md`, `library/cn-tree.md`, `library/pos-beta.md`, `library/signed-cut.md`, `gates/history-budget-*`, `gates/compute-inventory-*`, `gates/strategy-*`, the Sussman-Alpoge repository, and any literature. No numerical job was run: every claim here is a written argument, and no check was needed to decide one. Memory was at 60 to 65 percent free throughout. No commit, push, claim or subagent.
