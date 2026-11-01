lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T03:44Z

# Item rc-far: (RC-size), (RC-far), (MC) on the mapped map

Provenance: anthropic/claude-opus-5-5, effort max, Mac mini worker, fresh session, pinned at 23eddd87f. Side: mapped. Firewall: read `parts/upper-chain.md` (interface and Text 14), `parts/hard-core--mapped.md`, `library/`. Not read: `parts/hard-core--independent*.md`, gates on that attempt, `gates/history-budget-*`. The lead's forwarded remainder of the rate condition (PAIR) was not received in this session; I work from (RC-rates) as printed in `library/current-locality-reduced-law.md`. Same-model work, not independent and not an audit. Author work, labelled gap / unchecked / implication / discharged.

## Verdicts

Proof text: `library/far-difference-two-rate.md`, new, unreviewed. Labels below are this repo's; verdicts steer research and grant no status.

| Statement | Result | Label |
|---|---|---|
| E^r = E^good on this map; RC-transfer = 0 | Holds: Q^s = 0, one cut, one domain K, both free of W | discharged |
| (RC-size) | Delivered, Theorem RC | implication from H(k), Prop AN3, (M) |
| (RC-far) | Delivered, both tiers, every non-full cube, across sectors, Theorem RC | implication, level of each term, from H(k) with (Loc^c) strengthened to (Loc^f) |
| (Loc^f_k), D R_k at an absolute rate across sectors | New clause, Prop LF | implication, level of each term; gas clause of Lemma O2 read at its label |
| Lemma W, two-rate inverse | Proved | discharged, elementary |
| Lemma FAR, covariance across a cube, cut and tiers | Proved given its named hypotheses | implication |
| Lemma CL, classical locality in every sector | Order one written; orders 2 to 5 same recursion, not displayed | implication, level of each term |
| (RC-rates) | Met, with rho_v >= 2 kappa_v | implication |
| (MC) as printed | **WRONG** on tori of side >= 12: no regular completion need exist | discharged counterexample |
| (MC'), Lemma EXT' | Replacement, and (I-K3) from it | discharged given RC-size, RC-far |

**Delivered rates**, level j = k, d coarse cells, all constants C(Theta), free of j, K, volume:

| Quantity | Value |
|---|---|
| sigma_f = sigma_s | delta_cl L / 4 >= delta_# L / 8, per coarse cell |
| rho_f | delta_# / 16, absolute |
| rho_s' | mu_s / 2 = min(rho_s, mu_c) / 16, falls with L |
| a_f, a_s | 1, and poly(x_k) z_k^(1/2) <= C zeta_(k+1) |
| kappa | c_t/32 <= delta_#/96, so 2 kappa <= delta_#/48 < rho_f |
| kappa_s | <= rho_s/48; lowered to mu_s/4 if mu_c < rho_s |
| c_I, c_* | c_I := sigma_f, c_* := sigma_f - 2 max(kappa, kappa_s) |

The endpoint rate sigma grows with L, so any fixed multiple of kappa between c_* and c_I is available. rho_f exceeds kappa by a factor 6 only.

## (MC): literal clause is false at large radius; repaired (written first because it is complete)

**Verdict on (MC) as printed: WRONG on every torus of side T >= 12.** It asks a globally regular completion at n_0 - 1 which agrees with W on Q_(n_0 - 1)(o). No such field need exist once the cube is nearly the torus. Pullback cannot supply one either: a lattice retraction of the cycle C_T onto an arc of 2n edges needs a return path of 2n edges, so T >= 4n, which is why Lemma 14.14 stops at n < T/4.

*Counterexample [discharged].* T = 2n + 2, n >= 5, integer centre o = 0, coordinates x_mu in {-n, ..., n} on the cube. Regular means plaquette angle <= T_2, and T_2 is small, 81 T_2 < pi. On the cube put W = exp(i x_1 h(x_3) sigma_3) on links in direction 2, and 1 on all other links, with h(x_3) := (x_3 + n) T_2 / (2 n). Plaquettes in the plane (1,2) have angle h(x_3) <= T_2. Plaquettes in the plane (3,2) have angle |x_1| T_2 / (2 n) <= T_2 / 2. All others are trivial. So Q_n(0) is regular. Extend W arbitrarily to the rest of the torus. Let W# be any field equal to W on Q_n(0). Take the square loop of side 9 in the plane (1,2) at x_3 = n and its translate at x_3 = -n. They bound a ribbon of 2 x 36 = 72 plaquettes through the layer x_3 = n + 1. On the top loop the holonomy has angle 81 T_2, by abelian Stokes. On the bottom loop it is 1, since h(-n) = 0. Non-abelian Stokes on the ribbon, with the bi-invariant metric, gives 81 T_2 <= sum of the 72 plaquette angles of W#. So some plaquette of W# has angle >= (81/72) T_2 > T_2, and W# is not regular. Hence W itself has first bad radius n_0 = n + 1, Q_(n_0 - 1)(0) is regular, and no globally regular field agrees with W there. The same ribbon works for any gap h := T - 2 n - 1 >= 1, with side l := 4 (h + 1) + 1, whenever l <= 2 n and l^2 T_2 < pi. So the obstruction covers every n > 2 T/5 with (h + 1)^2 T_2 small. Elsewhere above T/4 a completion may or may not exist; nothing below needs to know.

**Repair (MC') [discharged, given RC-size and RC-far].** Let n_T := ceil(T/4) - 1, the largest radius with a pullback. The midpoint o of c', c'' is defined coordinatewise along the shorter arc whenever d := d(c', c'') < T/2 (Chebyshev torus distance); half-integer coordinates are allowed, and Lemma 14.14's phi_n is defined about them by the same formula, an arc of at most 2n edges and a return path symmetric about the antipode of o. Define, with n_0 = n_0(W; o) the first radius at which Q_(n_0)(o) is not regular:

- F(W) := f(W) if W is globally regular;
- otherwise F(W) := 0 if d > n_T + 1 or n_0 < d;
- otherwise F(W) := f(pi^*_(min(n_0 - 1, n_T)) W).

This is the recipe of Lemma 14.16 at every W with n_0 - 1 <= n_T, and it fixes the value on the set where Lemma 14.14 gave none. It is measurable: n_0 is Borel, pullback is continuous, and f is continuous on the globally regular set by uniqueness of V^*. It is antisymmetric under c' <-> c'': o, n_0 and the radius depend on the unordered pair, and G is antisymmetric. If d >= T/2 the midpoint is ambiguous but unused, since then d > n_T + 1. What (MC) printed and this does not give: agreement with W on all of Q_(n_0 - 1)(o) when n_0 - 1 > n_T. The value there depends only on, and agrees on, Q_(n_T)(o).

**Lemma EXT' [implication].** Assume RC-size, RC-far, and in each tier rho_v >= 2 kappa_v (one factor 2 stronger than the interface), sigma_v - c_* >= 2 kappa_v. Then for W, Wtilde arbitrary, agreeing on a non-full Q_m(c'), |F(W) - F(Wtilde)| <= C_1 U exp(-c_* d) [exp(-kappa m) + zeta' exp(-kappa_s m)], so (I-K3) holds, for every probability law, by the conditional-Jensen step of `library/current-locality-reduced-law.md`, section 3, unchanged.

*Proof.* If m <= 2 d + 4, every value of F is 0 or f at a globally regular field, so RC-size bounds the difference by twice its right side; sigma_v d >= c_* d + 2 kappa_v d >= c_* d + kappa_v m - 4 kappa_v. This covers d > n_T, since then m < T/2 <= 2 n_T + 2 <= 2 d. Let m > 2 d + 4, so d <= n_T, and n := floor(m - d - 2) >= d, Q_n(o) in Q_m(c'). If a first bad radius about o occurs by n, it is common to both fields; the zero decision is common, and each pullback radius r <= n_0 - 1 < n reads the common cube, so F(W) = F(Wtilde). Otherwise both first radii exceed n. Let W#, Wtilde# be W, Wtilde if globally regular, else their pullbacks at their radii, which are >= min(n, n_T). Both are globally regular and agree on Q_(n')(o), n' := min(n, n_T) >= d. RC-far gives |F(W) - F(Wtilde)| <= C U sum_v a_v exp(-sigma_v d - rho_v (n' - d)). If n' = n this is the old (EXT). If n' = n_T < n: non-full means m < T/2, so n_T >= T/4 - 1 > m/2 - 1, and rho_v (n_T - d) + sigma_v d >= 2 kappa_v (m/2 - 1 - d) + (2 kappa_v + c_*) d = kappa_v m + c_* d - 2 kappa_v. A full-field read has zero conditional fluctuation. QED

*Note for the upper chain.* (CF_j)'s extension a_(j+1,c') and the Rg_c of Lemma 14.15 use pi^*_(n_0 - 1) in the same way, so they have the same hole at n_0 - 1 >= T/4. That is outside this item; I have not repaired it.

## RC-size and RC-far: how the proof goes

**Why the size is easy.** U is about C_I(L) x^(1/2). G is linear plus quadratic in xi, its coefficients for c in B(c'), b in B(c'') carry the tail of a_c at rate delta_cl per level-j cell, so delta_cl L per coarse cell, and (M) bounds moments of xi with no x. That is (RC-size). The same crude bound would not give (K1) or the sharper h, and those are not claimed.

**Why the far bound is not easy, and what was false on the way.** (SPLIT) has two terms. The law term has to compare E_W and E_Wtilde when W, Wtilde may lie in different sectors. There is no path of regular fields, so one interpolates actions, S_t := (1 - t) S_W + t S_Wtilde, on the common free coordinates. Hostile (13) of `library/sector-values.md` is right that M_t has only a Combes-Thomas rate mu_c(L). As written, this gives O2 and (Loc^c) a tail g C(L) exp(-mu_c L r) in the action. That is a slow tail with amplitude a power of g, which is what the rate test in `library/current-locality-reduced-law.md`, section 1, excludes. See defect 2.

**Repair.** Three steps.

1. *Lemma W.* A_t = A_1 - A_t E A_1, with E the far part of M_t - M_1, so |A_t - A_1|(i, j) <= C exp(-(3/4) m max(r(i), r(j))): Theorem F at one field, and only the gap at the other. With the weight f = rho min(d(i, S), R) + rho_c (d(i, S) - R)_+, which grows fast inside Q_n(o) and at the slow rate outside, ||e^f A_t e^-f|| <= C_W, free of n and the volume. The slow rate outside is what removes the volume.
2. *Lemma FAR.* HS-P and HS-C run with A_t and this weight. The result is a covariance across the cube at rate delta_#/8, plus a tier with amplitude poly(x) z^(1/2), though the far gradient of D is of order one on the whole torus.
3. *Lemma CL and Prop LF.* These supply the input that the two actions nearly agree inside Q_n(o). Classical part: V^*(W), V^*(Wtilde) differ by C(L) T_2 exp(-(delta_#/2) r), by a hybrid on the fibre, criticality of V^*(Wtilde), and Mbar^-1 at W. R_k part: (Loc^f_k), by induction on k, since D_y' R_(k+1) is the same far difference one level down, with the lift gaining a factor L in distance.

## Attack log

| Attack | Outcome |
|---|---|
| Rate test: tail below kappa with amplitude a power of g | Real against O2/(Loc^c) as written; removed by Prop LF |
| Different sectors, no regular path | No effect: (INT) reads no path; a hybrid is used only on a class path inside one sector |
| Extra powers of x in the law term | None: d_b S(xi) = int Hess(s xi)[e_b, xi] ds, by criticality at 0. x^(1/2) appears only in grad, and U carries it. On K a sup is poly(x), read only in the slow tier |
| Cut: barrier curvature, far data | Slow tier, amplitude z^(1/2) poly(x); endpoint rate sigma stays large, as d-decay comes from coefficients |
| Volume, since D has order-one gradient everywhere | Removed by the slow outer growth of f |
| Finite torus, large n | RC-far reads no pullback, so no effect; MC does: defect 1 |
| Chart spike at the designated bond in a hybrid | Real: would leave the class. Hybrid built with a bump first; coordinates read from it |
| Amplitude compounding per level in Lemma CL | Real if written linearly; D_k enters E_k only through a power 2/L |

## Defects, ranked

1. **(MC) as printed is unsatisfiable** (section above). It breaks the clause, not the implication: (MC') plus rho_v >= 2 kappa_v gives (I-K3). Repair proved. The upper chain must adopt the changed clause; its Text says not to cap silently, and this cap is stated and estimated.
2. **O2, O3's tail and (Loc^c) at mu_c(L) do not support RC-far.** Hostile (13) says nothing needs the absolute rate. RC-far does, unless L mu_c(L) >= 2 kappa. Repair: Lemma W, Lemma FAR, Prop LF, unreviewed. H(k) must carry (Loc^f_k) in place of (Loc^c_k) at order one.
3. **Rate clause tightened.** Lemma EXT' needs rho_v >= 2 kappa_v, not rho_v >= kappa_v, for radii above T/4. Delivered here; it is a change to the neutral clause.
4. **Text 5.11, (C2_j)(c).** It cites HS-T for the far difference. HS-T bounds cumulants of one law; it does not compare two backgrounds across sectors. Lemma FAR gives that clause, and (GS_j)(d) at the fast rate, by the same proof; I have not written them out.
5. **(CF_j)(d) for a_c.** Consequence 3 of `library/analytic-lift.md` states it for A_n only. One line repairs it: |D_b a_c| <= 2 ||F||_(L^2(c)) ||H_b||_(Eps(c)), with Prop AN3 (2). Higher orders by AN2(a).
6. **`library/sector-values.md`, Section 5, "interpolate to a field"** reads as a sentence. Cutting xi directly makes a designated-bond spike of relative size L^3, out of the class. Lemma CL gives the construction.
7. **Order of constants.** tau and x_* must now satisfy C_W(L) eps_V <= 1/4, with C_W(L) from Lemma W. Harmless: C_W depends on L only.
8. **Same hole as defect 1, not repaired here.** (CF_j)'s extension a_(j+1,c') and Rg_c of Lemma 14.15 pull back at n_0 - 1, undefined at n_0 - 1 >= T/4. For the owner of `parts/upper-chain.md`.

## Still open

- Everything is conditional on H(k): Theorem F at a lift with (R3), Prop AN3, (H1)-(H3), and on the route to H(k) itself, Theorem Z, Lemma EX, Lemma TOP. None is touched here.
- Prop LF reads the gas clause of Lemma O2 at its label, at the rate mu_c(L), unchecked.
- Lemma CL at orders 2 to 5 is not displayed. Theorem RC reads order 2 of a_c and of A_k o Phi; order 3 of A_k o Phi enters only through Prop LF.
- The lead's forwarded remainder of (PAIR) did not reach this session. The margin on sigma is large in L; on rho_f it is a factor 6 over kappa. A condition demanding rho_f >= 7 kappa or more would need the absolute constants rechecked.
- If mu_c < rho_s then kappa_s must come down, and that feeds (TT) in the upper chain's 21.7.
- (K1) for the current and the sharper estimate on h are not touched: RC_j does not imply them.

## Numerics

`checks/rc_far/`, three runs, criteria first, memory free 67 to 69 percent at each start, under the lock, BLAS threads 1, peak RSS 1.99 GB, on the real chart matrix, abelian, trivial background, d = 2, one level, Gaussian, artificial far parts. **All three read FAIL by their registered criteria; none was re-graded.** Run 1 failed T3 at L = 7, rate 0.445 against 0.5. Run 2, Part A then gave 0.994, 0.973, 0.928 per box at L = 3, 5, 7, the registered tail rate of E, so run 1's T3 was saturation at the gap scale. Runs 2 and 3 failed only their vacuity controls: neither far part made a slow region in box units. In run 3 that was my parameter choice. Run 3's far effect decays at 3.12, 2.82, 2.76 per box, with no fall in L. **So the runs support a far rate free of L on these matrices and a two-rate norm bounded in n. They do not show that the two-rate weight is needed.** Lemma W rests on its proof. No test touches SU(2), sectors or the non-Gaussian law.

## Read and not read

Read: FINISH, GOAL, `parts/upper-chain.md` The interface, Text 14 notation through Theorem 14.13, 21.7 and history-related lines by grep; `parts/hard-core--mapped.md` State of attack, Requests 300 to 335, Text 5 to 5.3 head, 5.8, 5.10, 5.11; `library/` current-locality-reduced-law, far-pair-interpolation, preconditioned-covariance, fibre-propagator, one-step-closure, convex-laplace-tree-decay, analytic-lift, sector-values Sections 0 to 2, 5, 6, 8, parts of history-budget-sum, generated-observable-history, quiet-boundary-rarity (Prop MD*), polymer-covariance (head). Not read: Theorem Z, DM, gas proofs, Lemma EX. Forbidden and not opened: `parts/hard-core--independent*.md`, gates on that attempt, `gates/history-budget-*`. No gate file was opened at all. No subagents. Nothing committed or pushed.
