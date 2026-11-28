lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T09:57Z

# Lift repair: finite displacement, localized variation, exact restoration

Queue item `lift-repair`, mapped side, pinned at `e6028aa14`. Own derivation, 2026-11-01, by claude-opus-5-5 at max effort. Same-model, unread by anyone else, not independent and not an audit. It grants no status. Abbreviations: **ES** `library/energy-by-stages.md`; **gate** `gates/energy-stages-codex-b87de884f.md`; **PE** `library/paid-inputs-frozen-energy.md`; **AN** `library/analytic-lift.md`; **LU** `library/lattice-uhlenbeck.md`; **RD** `library/relative-density-bound.md`.

Labels as in `FINISH.md`: *discharged*, *implication*, *gap*. "Level of each term" means each term is displayed but constants are not computed.

**Result.** (LIFT-1) is replaced by an exact inequality at the fine level, (FD), and a level-j theorem, LIFT-NL, whose proof expands around the identity in one Uhlenbeck gauge and so needs neither (R3), Lemma AD, nor a multiplier. The ES:65 claim is replaced by LOC-V. Both hand tests pass. Lemma REST's exact restoration is constructed, with frozen bonds restored inside each step, including j = 0, and parents once at the minimal lift. The budget of defect 3 survives for sparse steps, with m_0 no longer needed. **First failed term: Section 6.** At depth, next to a wall whose frozen side has energy growing outward, Z is not empty and no step of ES Section 3 applies, so the stage has no output. That example does not refute (4.2) or (AE-R). It does break their proof, and LOC-V's a priori input rests on the same stage below.

## 1. The exact inequality at the fine level (discharged)

Write |g| := |log g| in [0, pi], so that a_p(U) = 1 - cos |theta_p(U)| is the Wilson action of a plaquette with half real trace cos |theta_p|, the normalisation of the gate. d_G(g, g') := |g g'^-1| is bi-invariant. For two fields U, U' and a plaquette p, with both holonomies based at the same corner,

    Theta_p(U, U') := d_G( hol_p(U'), hol_p(U) ),

which does not depend on the corner. Then:

**Lemma FD (finite displacement, fine level).** *For any two fine fields, with S the plaquettes where Theta_p != 0,*

    A(U') - A(U) <= ||theta(U)||_S ||Theta(U, U')|| + (1/2) ||Theta(U, U')||^2,        (FD)

*and the same holds with U' replaced by any gauge transform of U', which leaves A(U') fixed and changes Theta.*

*Proof.* Put x := |theta_p(U)|, y := |theta_p(U')|. By the triangle inequality y <= x + Theta_p. On [0, pi], (1 - cos)' = sin t <= t, so 1 - cos y - (1 - cos x) <= integral from x to max(x, y) of t dt <= x Theta_p + Theta_p^2/2. Sum over p and apply Cauchy-Schwarz. QED

No criticality, no multiplier, no gauge condition and no smallness is read. This is the whole energy estimate below. **The multiplier term |lambda| ||H||^2 of ES:65 does not occur**: it arose from expanding around a critical point, and (FD) does not expand.

*Test: the commutator square.* X := i sigma_1, Y := i sigma_2, U = 1, U' := e^h with h_xy = omega_y - omega_x and omega = 0, tX, t(X + Y), tY on the vertices of a square. Direct multiplication, as in the gate, gives holonomy with half real trace 1 - 2 sin^4 t, so Theta_p = |theta_p(U')| = 2 arcsin(sin^2 t) on that square. (FD) reads 2 sin^4 t <= 2 arcsin^2(sin^2 t) on it, true since arcsin u >= u, and the term that carries the action is Theta, which is the exact nonlinear curvature. Here d h = 0, so any bound reading d h alone is false, and this one does not read it.

## 2. The chain near the identity needs no curvature in L^4 (implication)

ES:65 needed the composite derivative at a background, and read Lemma AD as a black box; the gate's D8 says that does not give the local curl comparison. It is not needed. Take the base point of the contour-free chain at the identity, **in a Lemma U gauge**.

*Setting.* P a box of comparable sides, in fine units, the shadow of a cube of level-j cells. U on P with ||theta(U)||_P =: eps <= eps_0, and **its chain all-lines on P**: no label and no excluded line at levels below j. By Lemma TE this holds as soon as E(P^+) < T^2/C_T, and it holds for any chain with no cell above T. Lemma U gives g with U^g = e^{i a}, ||a||_{l^4(P)} <= C_U eps, sup |a| <= C_U eps.

N_l, N^(j) := N_(j-1) o ... o N_0 are the maps of Theorem 7, Step 1 of `library/block-poincare-energy-package.md`, **with base point V_l = 1**: g^[l](e^{i theta})(y) := exp(-i Phi^[l]_y theta), N_l(V) := g^[l](V) . M_l(V), with M_l the all-lines log-average. So N^(j)(e^{i b}) = G_1(b) . M^j(e^{i b}) with G_1(b) a level-j site function, and D N_l at 1 is Q^{o,[l]} at U = 1, the path part alone. Let Q^o := Q^{o,(j)} at U = 1, a positive kernel: this is the operator of Lemma LW. e_j(c; b) := ||b||_{l^4(c^+)} for a level-j bond c. Note ||b||_{l^4} = ||b/eta||_{L^4}, so this is the critical norm of AN.

**Lemma CH (the chain chart; implication: this is the proof of Lemma AN1 of AN read at U_0 = 1).** *There are rho(L), C_2(L), free of j and of the volume, such that for e_j(c; b) <= rho(L) on the bonds of the region,*

    log N^(j)(e^{i b})(c) = Q^o b (c) + R(b)(c),    |R(b)(c)| <= C_2(L) e_j(c; b)^2,
    |R(b)(c) - R(b')(c)| <= 2 C_2(L) ( e_j(c; b) + e_j(c; b') ) e_j(c; b - b').        (CH)

*Proof.* AN1's recursion at U_0 = 1. Its hypotheses (i), (ii) read U_0, and at U_0 = 1 they hold trivially: F = 0, so the residual in its "Linear part" vanishes, and |Q^o b(c)| <= C_1 e_j(c; b) by Hoelder against the kernel of Lemma 1 of the package. With zeta^l := theta^l - Q^{o,(l)} b, zeta^(l+1) = Q^{o,[l]} zeta^l + b_l(theta^l), the step uses only (1) of AN, sum over the block of e_l^4 <= C e_(l+1)^4, the factor 2 L against L^-2, and |b_l(theta)(c')| <= C_b(L) sum_block |theta|^2, for sup |theta| <= rho_b(L). The second line of (CH) follows from the first by Cauchy on the polydisc, since all maps are analytic there. QED at the level of AN1's proof, which I reread and in which I found no use of curvature at U_0 = 1. `checks/hard-core--mapped_composite_jet.py` and `_d4.py` tested exactly this case, U = 1, and passed. Those runs are guidance only.

So in the gauge g, V_j(U)^G = N^(j)(e^{i a}) =: e^{i v} on bonds read in P, with G := G_1(a) g at level-j sites. **The hypothesis is only that a Lemma U gauge exists with small critical norm: no (R3), no L^4 bound on F, no Theorem F, no Lemma AD.** Hostile note (f) of RD asked for L^4 of F at the base field because it expanded around that field. Expanding around 1 in one Uhlenbeck gauge costs the constant C_2(L) on the remainder, which T small in L pays, and it costs nothing on the leading term, because the leading term is the exact Lemma LW at U = 1.

## 3. The replacement of (LIFT-1)

Let **R^# := the lift of Lemma LW with its tails cut, on a fixed support**. Put Omega_0 := the shadow of Q + rho_t + 1, a union of whole level-j cells, and 𝖢 := the level-j bonds whose kernel rho_c meets Omega_0. For a bond c of 𝖢, R_c is a union of two whole cells, so R_c cap Omega_0 holds a whole cell, with tent mass at least 1/2. So there are bumps psi_c supported in Omega_0, with <rho_c', psi_c> = delta_(c c') on 𝖢 and ||d psi_c||_{l^2} <= C: the straddling bumps of Theorem F-D, at U = 1. For x on 𝖢: y := T^-1 x, y^# := y on Q + rho_t, zero off it, R^# x := Wh_1 y^# + sum_(c in 𝖢) e_t(c) psi_c, e_t := x - T y^# on 𝖢. Then **Q^o R^# x = x on all of 𝖢, and R^# x is supported in Omega_0, for every x**, so the support does not grow when R^# is iterated. In general ||d R^# x||_{l^2} <= C ||x||_{l^2}. For h supported on Q,

    ||d R^# h||_{l^2} <= 2^4 ||d h||_{l^2} + C e^{-c_w rho_t} ||h||_{l^2},    ||R^# x||_{l^4} <= C_7 ||x||_{l^4},

the first by (LW), the second since Wh_1 is a tent product with scale-invariant l^4 norm and T^-1 has an exponentially decaying kernel. rho_t := (2/c_w) log(2 + R) makes the tail term at most C ||h||_{l^4} / (2 + R), since ||h||_{l^2(Q)} <= C R ||h||_{l^4}.

**Theorem LIFT-NL (finite gauge-corrected displacement; implication, given Lemma U, Lemma LW, Lemma CH, the bumps; level of each term).** *Let Q be a cube of radius R in level-j cells, with the shadow of Q + rho_t + 2 at positive distance from every lower layer. Let U be a fine field on that shadow, with chain all-lines there, energy eps^2 := ||theta(U)||^2 there, W := V_j(U). Let W' be a level-j field equal to W off Q, and suppose there is a level-j site function sigma, equal to 1 off Q, with G . W'^sigma = e^{i (v + h)} on Q, h supported on Q, in the frames G of Section 2. If eps + ||h||_{l^4} <= eps_2(L), there is a fine field U' with*

    V_j(U') = W' exactly,   U' = U off the shadow of Q + rho_t + 1,   all lower data unchanged,
    A(U') <= A(U) + N D + D^2/2,    N := ||theta(U)||_(shadow of Q + rho_t + 2),
    D <= 2^4 ||d h||_{l^2} + C (1 + C_2(L)) ( eps + ||h||_{l^4} ) ||h||_{l^4} + C ||h||_{l^4}/(2 + R).        (LIFT-NL)

*Here d h is the flat curl of the small field h, and the exact level-j curvature displacement Theta^j := Theta(e^{i v}, e^{i (v + h)}) obeys ||d h|| <= ||Theta^j|| + C (||v||_{l^4} + ||h||_{l^4}) ||h||_{l^4}. If sigma puts h in relative Coulomb gauge on Q, then ||h||_{l^4} <= C ||d h||, by Gaffney and the lattice Sobolev inequality for a compactly supported field, so*

    D <= (2^4 + C_8(L) (eps + ||Theta^j||) + C/(2 + R)) ||Theta^j||.

*Consequently, if U = U^* is a minimiser for Phi_j(W), and every field with level-j data W' of flux at most T_2 has action at least Phi_j(W'), which is Xi_j >= 0:*

    Phi_j(W') <= Phi_j(W) + N D + D^2/2.

*Proof.* Solve H = R^#( h - [R(a + H) - R(a)]|_𝖢 ) on fields supported in Omega_0. By (CH) and ||R^#||_{l^4} <= C_7, this is a contraction for C C_7 C_2(L) (eps + ||h||_{l^4}) <= 1/2, on ||H||_{l^4} <= 2 C_7 ||h||_{l^4}, in the norm of l^4 and in the local one. Then Q^o H + R(a + H) - R(a) = h on 𝖢, so log N^(j)(e^{i (a + H)}) = v + h on 𝖢. Off 𝖢 a bond reads no link of Omega_0, since N^(j)(c) reads only R_c, so it is unchanged, exactly. With zeta := R(a + H) - R(a), Cauchy-Schwarz over bonds, **not a count of bonds**, gives

    ||zeta||_{l^2} <= 2 C_2(L) ( sum_c ( e_j(c; a) + e_j(c; a + H) )^4 )^(1/4) ( sum_c e_j(c; H)^4 )^(1/4) <= C C_2(L) (eps + ||H||_{l^4}) ||H||_{l^4},

as sum_c e_j(c; .)^4 has finite overlap. So ||d H|| <= 2^4 ||d h|| + C ||zeta||_{l^2} + tail: **there is no factor of the radius R in the constraint's second-order term.** For a fine plaquette, BCH gives Theta_p(e^{i a}, e^{i (a + H)}) <= |(d H)_p| + C (|a|_p + |H|_p) |H|_p, so in l^2, by Hoelder, D := ||Theta|| <= ||d H|| + C (eps + ||H||_{l^4}) ||H||_{l^4}. That bounds D as stated.

*Exact data.* M^j(e^{i (a + H)}) = G_1(a + H)^-1 . e^{i (v + h)}, while W' = sigma^-1 g^-1 G_1(a)^-1 . e^{i (v + h)}. So the two differ by a level-j site function kappa, equal to 1 where neither H nor sigma reaches. Transform the field by a fine site function equal to kappa at level-j sites and 1 at all other fine sites. That is U', and its plaquettes are unchanged. Lower data lie outside the shadow, so they do not move. (FD), applied to U^g and e^{i (a + H)}, gives the energy. The relation between d h and Theta^j is BCH on level-j plaquettes, and Gaffney for compact support is Step 1 of LU on a torus containing Q. For the last line, Phi_j(W') <= A(U') by the hypothesis Xi_j >= 0, and A(U) = Phi_j(W). QED at this level.

*What it does not read:* Lemma AD, (R3), Theorem F, the multiplier, the size of the fine energy of U away from the support, and any count of bonds.

**Hand test 1, commutator square, j = 0, W = 1.** No chain, Q^o = 1. With sigma := 1, h is the exact gradient, ||d h|| = 0, ||h||_{l^4} of order t, and the bound keeps C ||h||_{l^4}^2 of order t^2, so D^2 of order t^4, against the true action 2 sin^4 t plus the other plaquettes: consistent, and it does not assert zero. With sigma(x) := e^{omega_x}, the bond becomes e^{omega_x} e^{omega_y - omega_x} e^{-omega_y} = exp( (1/2) [omega_x, omega_y] + O(t^3) ), of size t^2. So relative gauge reduces ||h||_{l^4} to order t^2, and D is the exact curvature at leading order. **Passes.**

**Hand test 2, locked frozen pair, j >= 1.** W = 1, U the explicit minimiser of PE, (E5), Phi_j(1) = M e(a) > 0. The hypothesis puts the shadow of Q away from all lower layers, so away from the pairs, where U = 1. So eps = 0, N = 0, a = 0, and the statement reads Phi_j(W') <= M e(a) + D^2/2. That is true, and it is a statement about the *variation*: the term M e(a) sits on both sides and is not bounded by anything. Nothing here compares the fine energy of the lift with the coarse curvature, which is the statement the gate refuted. **Passes.**

*Kill test, a guide only.* `checks/lift_nl/lift_nl_kill.py`, criteria first in `CRITERIA.md`, one run, log kept. SU(2), d = 2, L = 3, j = 1, 2, the actual block map with comb contours and the contour-free chain. Base fields noise, smooth and fine pairs, at ||a||_{l^4} = 0.02, 0.05; displacements bump, exact gradient, random. **PASS, no failed line.** The iteration of the proof, with no term from Lemma AD, converged to 1e-10 in at most 6 steps. Worst D / (||d h||_2 + (eps + ||h||_4) ||h||_4) was 0.77 at j = 1 and 0.37 at j = 2, so no growth with level. An exact level-j gradient has ||d h|| = 0 and positive D, as Hand test 1 says. Limits: d = 2, where l^4 is not the critical norm, one L, two levels. It says nothing about constants in d = 4.

## 4. The localized variation estimate, in place of the claim at ES:65

The refuted sentence bounded the fine energy of the minimal lift by weighted coarse curvature. The replacement compares the minimal lift with **any competitor having the same level-j data**, on a region that no lower layer meets. It never bounds the whole lift.

*Region.* 𝖡 a union of level-j cells, 𝖡_i := 𝖡 + 8 i cells. C_f' := the constant of (RF-X) below, theta_h := 1 - 1/C_f', rho_1 := (1/16) log(1/theta_h), absolute.

*Inputs at level j.* (a) U^* attains Phi_j(W), W of flux at most T_2. By the chain's definition it has no cell above T below level j, so it is all-lines. (b) *A priori, from the Corollary of ES Section 4 at the stage below:* on 𝖡_m, every level-(j-1) cell of U^* has energy at most kappa T^2, and every level-j cell at most K T^2. (c) Ũ is a fine field on the shadow of 𝖡_m with V_j(Ũ) = W there, all-lines, with the same two bounds. (d) The shadow of 𝖡_m misses all lower layers.

**(RF-X), Lemma RF with exact data (implication, given Lemma RF, LIFT-NL; level of each term).** *Let S be a band of level-j cells at least 8 wide, inside 𝖡_m, with U_1, U_2 two fields as in (b), (c). There is a field Û with V_j(Û) = W on all of 𝖡_m, equal to U_1 off the outer side of S and to U_2 on the inner side, with ||theta(Û)||^2_S <= C_f' (||theta(U_1)||^2_S + ||theta(U_2)||^2_S), C_f' absolute, and every level-(j-1) cell of Û of energy at most C_g kappa T^2, C_g absolute.*

*Proof.* Lemma RF, with level-j cells as its blocks, gives Û_0, with mismatch |s(b)| <= C (||theta(U_1)||_(N(b)) + ||theta(U_2)||_(N(b))) on level-j bonds of S. So ||s||^2_{l^2} <= C times the two band energies, with no factor of a radius, as the band has bounded width. Colour the bonds of S with boundedly many colours so that one colour lies in disjoint patches of bounded radius. On each patch apply LIFT-NL with h := -s on that colour. It restores those bonds exactly and leaves all other level-j bonds fixed, at D <= C ||s||_(l^2(patch)) + C_8(L) (small) ||s||. *Cell bound.* In a patch the field is e^{i (chi a' + (1 - chi) a_2)}, chi at scale s_j. On a level-(j-1) cell c_1 of side s_j/L, ||d chi ^ b||^2_{c_1} <= (C/s_j)^2 ||b||^2_{l^2(c_1)} <= C L^-2 ||b||^2_{l^4}, and ||b||_{l^4} is at most C K^(1/2) T. So the term is at most C K L^-2 T^2 <= kappa T^2 for L large, and the rest is at most C kappa T^2 by (b), (c). QED

So for kappa with C_g kappa <= 1/(2 C_T), Û has no rough cell below level j, by Lemma TE, its chain is all-lines, and A(Û) >= Phi_j(W) is immediate from the definition.

**Theorem LOC-V (localized variation; implication, given (RF-X); level of each term).** *Under (a) to (d), for all m,*

    E(U^*; 𝖡) <= sum_(i = 1)^m theta_h^(i - 1) E(Ũ; 𝖡_i) + theta_h^m E(U^*; 𝖡_m).        (LOC-V)

*So E(U^*; 𝖡) <= C_E sum_c exp(-2 rho_1 d(c, 𝖡)) E(Ũ; c) + theta_h^m E(U^*; 𝖡_m), sum over level-j cells of 𝖡_m.*

*Proof.* With E_k := E(U^*; 𝖡_k), let Û be (RF-X) with U_1 := U^*, U_2 := Ũ, S := 𝖡_(k+1) minus 𝖡_k. Minimality, with Û equal to U^* off 𝖡_(k+1), gives E_(k+1) <= E(Û; 𝖡_(k+1)) <= E(Ũ; 𝖡_k) + C_f' (E_(k+1) - E_k) + C_f' E(Ũ; S). Rearranged, E_k <= theta_h E_(k+1) + E(Ũ; 𝖡_(k+1)): Widman's hole-filling. Iterate. QED

*Hand test 2.* The term M e(a) is not read: by (d) the pairs are outside the shadow of 𝖡_m, so neither side contains them, and the last term carries only U^* on the clear region. With W = 1 and Ũ = 1 near 𝖡 it gives E(U^*; 𝖡) <= theta_h^m E(U^*; 𝖡_m), and in the explicit minimiser both sides vanish. *Hand test 1* does not apply, since j >= 1; at j = 0, U^* = W and there is nothing to prove.

*This is the tail the gate asked for:* quantified, with lower data exactly fixed, and exponentially small only relative to a clear region's own a priori bound, not relative to locked energy, which is never in the sum. **(R3), Theorem F and the trial are not read.**

## 5. Exact restoration

The design change from ES Section 4: **the frozen bonds are restored inside each step, in one Uhlenbeck chart of the cube, and no mismatch is carried.** Parents are restored once, at the end, at the minimal lift. No history of mismatches M_old exists, so **m_0 is not needed**, and the gap between ES:86 and ES:188 does not arise.

### 5.1 Changes to the stage

(a) *Active zone.* 𝖠 := level-j cells within (J + 6) L of a free level-j cell. Z := cells of 𝖠, free or frozen, with A_c(U) > kappa T^2. A frozen cell in 𝖠 holds no locked energy: by (CL) no lower layer is within t_0/12 of it, provided t_0 >= 12 (J + 6) L + 12 r_*. At j = 0, (QD) keeps locked energy below kappa T^2. So all fine links under a cell of 𝖠 are free at j >= 1. This fixes ES:90's unproved "T/2 + o(T) on frozen": at the end every cell of 𝖠, and every cell changed by a sparse step, has energy at most kappa T^2, so level-j flux at most T/4.

(b) *Order of constants, acyclic.* C_T, C_f, C_U, C_ext, C_9 (below), kappa, then J (from a hole-filling constant C_** absolute, so J is free of K), K, then c_1 := min(c_b, 1/C_T)/(8 C_9), C_* >= C K/c_1, eta_0 <= c_1/(C kappa), I_*, R_1 >= C (I_* + 8) so that rho_t + 4 fits in a dyadic shell (I_* does not read R_1), r_*, eps_q, L, a_*, T. C_* now comes after K for a new reason, and **no constant enters from a multiplicity**. This answers the kappa, C_T, C_* part of the gate's D8.

(c) *Shells are below T^2.* Take n first with C_* C_9 (a_n + a_(n+1) + a_(n+2)) <= E_n/2. As E_n <= C K T^2 off dense boxes, the shells of Q_(n+3) minus Q_n carry energy at most c_1 T^2/C_9. So by Lemma TE they hold no rough cell at any level, and the chain is all-lines on them, whatever happens in Q_n.

### 5.2 One step, with frozen data exact (Lemma STEP+; implication, level of each term)

*Let V_j(U) = d_j on all frozen bonds at the start of the step, and let c, n be as above. There is U^+ with U^+ = U off Q_(n+2), V_j(U^+) = d_j on all frozen level-j bonds, all lower data unchanged, E(U^+; Q_(n+2)) <= C_9 (a_n + a_(n+1) + a_(n+2) + E_(Q_(n+2))(T_Q)), and so*

    A(U) - A(U^+) >= (1/4) E_n.        (3.2')

*This includes j = 0.*

*Proof.* *Fill.* Let T_Q be (EXT-d), T_Q = d_j on frozen bonds of Q_(n+2), or T_Q = 1 if there are none. By (QD), E(T_Q) <= C eta_0 kappa T^2. So T_Q = e^{i b} in a Lemma U gauge g_T of level j on Q_(n+2), ||b||_{l^4} <= C E(T_Q)^(1/2). LIFT-NL at U = 1 gives a fine U_T with V_j(U_T) = T_Q and E(U_T) <= C E(T_Q): **this replaces the trial, and it is an exact lift**. Fill U towards U_T across the shell Q_(n+1) minus Q_n by Lemma F, with its target, ES:67. No frozen bond is respected at this stage. Call the result Û_0. Its energy on Q_(n+2) is at most C_F (a_n + a_(n+1) + E(T_Q)) + a_(n+1), below c_1 T^2. So it is all-lines on all of Q_(n+2), and *one* Lemma U gauge covers the cube, with Û_0 = e^{i a}, ||a||_{l^4} <= C eps, eps^2 := C_F (sum of a's + E(T_Q)). Let e^{i v} := N^(j)(e^{i a}), in frames G.

*Compare with the data at the end, not along the history.* F := frozen level-j sites of Q_(n+2), F_e := those in Q_(n+2) minus Q_(n+1) + 2. On bonds of F_e, Û_0 = U, so V_j(Û_0) = d_j = T_Q. Hence tau := G g_T^-1 on F_e has ||grad tau||_{l^4(F_e)} <= ||v||_{l^4} + ||b||_{l^4} <= C eps. By Lemma BG (b), since r_* <= t_0/16, F is a half-ball up to a bi-Lipschitz map and F_e is connected, so as in Steps 3, 4 of Lemma RF, reflection and Lemma M extend tau to all level-j sites of Q_(n+2) with the same bound. Replacing g_T by tau g_T makes b-tilde := the field of T_Q in that gauge equal v on F_e, with ||b-tilde||_{l^4} <= C eps. Put

    h := psi (b-tilde - v),    psi = 1 on Q_(n+1) + 2,  psi = 0 near the edge of Q_(n+2) - rho_t - 1,  |d psi| <= C/r_n.

On frozen bonds of Q_(n+1) + 2, v + h = b-tilde, which is d_j in the gauge tau g_T. On the rest of F, in the band, b-tilde = v, so h = 0 and v + h = v, which is already d_j. So with sigma := G^-1 tau g_T on F and 1 off Q_(n+2), W' := G^-1 . e^{i (v + h)} is d_j on every frozen bond, after the site function sigma^-1: this is the sigma of LIFT-NL, and sigma = 1 on F_e. **The curl is bounded with no factor of r_n and no reference to any mismatch:**

    ||d h||_{l^2} <= ||d b-tilde|| + ||d v|| + (C/r_n) ||b-tilde - v||_{l^2(Q)} <= C ( E(T_Q)^(1/2) + eps ) + C ||b-tilde - v||_{l^4} <= C eps,

using ||.||_{l^2(Q)} <= C r_n ||.||_{l^4(Q)}, and ||d v|| <= C eps by (CH) and (J). LIFT-NL with base Û_0 and R := r_n gives U^+, with D <= C eps. At **j = 0** there is no chain: v, b-tilde are the links themselves, U^+ := e^{i (v + h)}, and frozen links are exact because b-tilde = d_0 in the gauge there. So **Step 5 of Lemma RF is not asked to preserve anything**, which was the gate's objection: exactness comes from the final interpolation at the level where the bonds are data. In all cases energy after is at most C_9 eps^2-type, and (3.2') follows from (c) and E_n >= kappa T^2. QED

*Why this is allowed at a general field.* The cube's interior may have been rough before the step, but after the fill the whole cube has energy below T^2, so Lemma CH applies to Û_0. The proof reads no regularity of U beyond the shell.

**Local amortized energy, not consumed here (discharged, given (3.2')).** This answers the gate's D4 if m_0 is wanted elsewhere. For a region D with D^+ := D + 2 r_*, let M(D) := sum E(s) over sparse steps touching D. Steps inside D^+ lower E(.; D^+) by at least E(s)/4, and a straddling step raises it by at most E(s)/C_*. So M(D) <= 4 E_0(D^+) + (4/C_*) M(D^+), which iterates to M(D) <= 4 sum_k (4/C_*)^(k-1) E_0(D^(k)), where E_0 is the energy at the start of the sparse phase. The factor 4/C_* beats the polynomial growth of a region without dense boxes, so m_0 <= C K/kappa holds with the influx charged.

### 5.3 Parents, at the minimal lift

After the stage, W^- := V_j(U^-) equals d_j on all frozen bonds touched by sparse steps. Let f_c be the fraction of lines of a parent c meeting a step's cube, and n_c the number of steps in its blocks. A parent with both blocks frozen is exact. Bricks are whole blocks, so any other parent has at least half its lines free. All such blocks lie within 2 L of a free cell, so at distance at least (J + 4) L inside 𝖠.

*(a) Mismatch from the final field.* Q = Q^o + D' Phi. A change of contours is a coarse gradient, removed by a level-j site function sigma at free centres. Frozen centres have whole frozen blocks, so unchanged contours and no frame change. What is left is the line part. Let g(x_perp) be the line sum. Then, by Poincare in the three transverse variables, for either field the mean over a subset of density f_c differs from the mean by at most C f_c^(1/2) E_2, with E_2 its block energy off hulls. So

    |s(c)| <= C min(1, n_c (r_*/L)^3)^(1/2) K^(1/2) T,

as in hostile (a) of RD, with BCH terms of relative size C(L) K^(1/2) T. No history is read: both fields have block energy at most C K T^2.

*(b) Exact solve at one level.* h_P := sum_c s(c) psi-tilde_c + (Newton), with psi-tilde_c the box-scale bumps of Theorem F-D on free lines, biorthogonal to the parents, zero on frozen bonds, |psi-tilde_c| <= C/L, |d psi-tilde_c| <= C/L^2. This is a one-level implicit function theorem, with second-order error C(L) |s|^2. **The composite map does not enter this solve**, and the frozen bonds are not touched, so the two corrections do not interact: this is the gate's "simultaneous constraint". ||d h_P||^2_(block) <= C |s|^2. Flux rises by at most C K^(1/2) T/L^2 <= T/8, so W^+ := (W^-)^sigma e^{i h_P} has flux at most T, parents W, and data d_j.

*(c) Cost.* Apply LIFT-NL at U^* := the minimiser for Phi_j(W^-), on blocks of one colour at a time. By LOC-V with Ũ := U^-, 𝖡 := the shadow of the two blocks, m := L, which is inside 𝖠 by the margin: E(U^*; 𝖡) <= C_10 K T^2. The tail is theta_h^L L^4 K T^2, and the first sum is at most C K T^2, since U^- has no dense box left. So N <= C K^(1/2) T, and

    Phi_j(W^+) <= Phi_j(W^-) + C sum_c ( K^(1/2) T |s(c)| + |s(c)|^2 ) <= Phi_j(W^-) + C K (r_*/L)^(3/2) T^2 #{s},        (4.1')

using sum_c n_c <= C #{s}, and if n_c (r_*/L)^3 >= 1/2 the crude |s| <= C K^(1/2) T with n_c (r_*/L)^3 as the factor. **This is (4.1) with the term (1/8) sum E(s) gone,** since the frozen cost is already inside (3.2'). For L large, the right side is at most Phi_j(W^-) + (1/16) sum_s E(s).

So, for a stage with sparse steps only, **Theorem AE-T holds as (4.2) with the constant 3/16 (implication)**: Xi_(j+1)(U) >= (3/16) sum E(s) + Xi_j(U^-).

### 5.4 The budget of defect 3

| Term in the gate's table | Gate's size | Here |
|---|---|---|
| Frozen correction, linear | C sqrt(m) q B | Gone as a separate term: paid inside (3.2'), by C_9 (a's + E(T_Q)) <= q E(s). **No sqrt(m)** |
| Frozen correction, quadratic | C m q B | Same. **No m** |
| Parent, linear | C K N_p (r_*/L)^(3/2) T^2 | Same size, derived from N <= C K^(1/2) T by LOC-V: C K (r_*/L)^(3/2) T^2 #{s} |
| Parent, quadratic | C K N_p (r_*/L)^3 T^2 | Same |
| N_p <= C N | asserted | Replaced by sum_c n_c <= C #{s}, and min(1, .) for a crowded block |
| Multiplier term, ES:65 | no estimate | Does not occur, by (FD) |
| Nonlinear remainder, ES:188 | C(L) T B not written | Displayed: relative factor C_8(L) (eps + D) in LIFT-NL, with eps <= C K^(1/2) T at a block and eps <= c_1^(1/2) T at a cube. So a relative C(L) K^(1/2) T, small after L |
| Lift constant, ES:49 | to be proved absolute | 2^4 on the leading term, from Lemma LW, exact. Only the remainder carries C(L) |
| Lower-data tail, ES:51 | unassigned positive term | Zero: lower data are not in any support, and LOC-V's tail is relative to clear energy |

**The budget survives, for sparse steps, with room.** The only condition left is C (K/kappa) (r_*/L)^(3/2) <= 1/16, the gate's own condition, with L after K, kappa, r_*.

*Dense clusters away from every frozen bond (implication, level of each term).* All boxes near such a cluster are counted, so Prop 10's layers exist. Use a hole-filling constant C_** >= 32 C_5, with C_5 the constant below. Band parents have |s(b)|^2 at most C times the local final energies, by (RF-X)'s count. So the band cost is at most C_5 (final band energy + target energy on the band) <= (1/16) E(s), for K >= C C(J) b_2^2. This is an energy budget, not a count of parents, which fills the gap the gate named at ES:88, 98. It reads the target of ES:88, whose existence and energy I did not rebuild; that is a named input.

## 6. The first failed term: the dense step next to a wall has no hole-filling layer

Sections 2 to 5 restore any stage output. The stage itself does not always have an output. **This is where I stop.** The failed term is ES:88, "first hole-filling layer at most J", read with the restriction of ES:192 (2) that "dense boxes at stage j must be only those within L of a free level-j cell".

Prop 10 proves J from layers "free of dense boxes, each with energy at most C K T^2 |D|". That restriction was introduced to keep locked energy out, and it removes the hypothesis: a layer box more than L from a free cell can hold any energy, and it is not counted.

**Example (written to be checked by hand; no run).** Take j >= j_0 below, a flat wall of frozen level-j bricks, data identity at all levels, and a frozen-side region within t_0/12 of the wall, so free of lower layers by (CL). All fine links there are free variables. Let U be 1 except for fine pairs of PE, Section 2, amplitude a := T/8, at most one in each of a separated set of level-1 blocks. By (E3) all parents are exactly 1, so V_l = 1 for all l >= 1, W = 1, the data are exact, and every plaquette is below T/8: **a class chain with no rough cell at any level.** Each pair has energy e := e(a) >= T^2/12.

Choose a patch of 𝔫 boxes along the wall, on the frozen side. Put in each box at depth i, for i = 0, ..., I := floor(t_0/(12 L)), exactly n_i := ceil(2^i (K + 1) T^2/e) pairs, at depth 0 with some inside the level-j cells touching the wall. Off the patch, and on the free side, U = 1. A box holds about L^(4 j) level-1 blocks, so this fits once L^(4 j) >= C 2^I (K + 1), which defines j_0. Depth is not bounded in any statement here, and t_0 >= C L log(1/T) only raises I.

- A free cell c at the wall has c + 4 s_j meeting the pairs, so c is in Z.
- The depth-0 boxes are within L of a free cell and hold energy above K T^2, so they are dense. So a sparse step at c, which needs to be "off dense boxes", is excluded.
- Depth i >= 1 boxes are at least L from free cells, so they are not dense under the restriction, and they are not merged. The cluster is D := the depth-0 patch.
- Let E_i be the energy of D^(+i) and a_i := E_(i+1) - E_i. Lateral layers are empty. So E_i <= (1 + o(1)) sum_(k <= i) 2^k (K + 1) T^2 𝔫 <= (1 + o(1)) 2^(i+1) (K + 1) T^2 𝔫, and a_i >= 2^(i+1) (K + 1) T^2 𝔫. Thus a_i/E_i >= 1 - o(1) for every i < I. So C_f a_i <= E_i/2 fails at every layer up to clearance, for C_f >= 1. By t_0 >= 12 (J + 3) L, I exceeds J.

So Z is not empty and no step of Section 3 of ES applies: **the stage does not reach "no cell of Z and no dense box", and U^-, W^- are not defined.** Filling anyway across layer i gains nothing: the bound is E_i + a_i - C_f a_i, which is at most (2 - C_f + o(1)) E_i, so not positive for C_f > 2, and a band further out is heavier. Enlarging "dense" to all boxes within t_0/12 only moves the cut to a heavier band.

*What this does and does not refute.* It does not refute (4.2), (AE-R) or the Corollary as statements: here R is empty and (AE-R) reads 0 <= A(U). It refutes the proof of Theorem AE-T at depth, and with it the claim of ES:124 that the left side telescopes through stages. It is the same phenomenon ES:192 (5) saw, a heavy frozen side made of many cells each below kappa T^2, where crossing the wall was offered as the cure. It is not cured when the frozen side's energy grows outward. Note what kind of energy this is: under frozen level-j bonds, at levels below j, with zero level-j curvature. It belongs to stages below j, and stage j should not have to read it.

*The same example at the Corollary.* A minimiser has no such profile freely: Z_(j-1) empty gives at most K T^2 per level-j cell, so a box holds at most L^4 K T^2. Geometric growth at a fixed ratio then stops within about log L layers, so for minimisers J would become J(L). That still breaks the order of constants, K before L and r_* << L, unless K is unaffected. **I have not resolved this**, and LOC-V's input (b) reads this Corollary. So Sections 4, 5.3 are conditional on the Corollary at the stage below, which rests on the failed term.

**Repairs, all unproved, in the order I would test them.**

1. *Pay lower energy first.* Where V_j(U) is class, replace U by a minimal lift of V_j(U) on the frozen side before stage j, paying the removed rough cells by the recursion at lower stages with level-j bonds as fixed tops. Then each box holds at most L^4 K T^2, as above, and the difficulty is the J(L) of the last paragraph plus a band against the unrelaxed far field. This changes the order of the recursion near a wall.
2. *Trigger Z by level-j quantities only:* a cell is in Z only if labelled or of level-j flux above T/4. Then the example has Z empty, and no step is needed. The obstruction moves to a rough free cell adjacent to the heavy wall, where cubes cross into the heavy side. That variant is open. Lemma F's constant is near 1 on the high-frequency part, since |chi d a|^2 <= |d a|^2 and d chi ^ a is small for zero block averages, but Lemma U's energy hypothesis can fail there, as a single cube can hold more than eps_0^2 of pairs.
3. *The lead's fallback in `FINISH.md`:* compare with an induction that carries the heavy region explicitly. In this example the heavy set is a large-field-like region in energy only, with trivial coarse data.

## 7. Verdicts, by the words of the queue item

| Ask | Result | Label |
|---|---|---|
| Finite gauge-corrected displacement bound keeping nonlinear curvature | (FD), Lemma FD: exact. Theorem LIFT-NL at level j | FD discharged; LIFT-NL implication, given Lemma U, Lemma LW, Lemma CH, the bumps |
| Localized variation estimate replacing ES:65 | Theorem LOC-V with (RF-X) | implication, given Lemma RF, and for its input (b) the Corollary at the stage below |
| Hand test: commutator square | passes, Sections 1, 3 | discharged |
| Hand test: locked frozen pair | passes, Sections 3, 4 | discharged |
| Lemma REST's exact restoration | Lemma STEP+ for frozen bonds, including j = 0; Section 5.3 for parents | implication, level of each term, for sparse steps and interior clusters |
| Budget of defect 3 | survives for sparse steps; frozen terms absorbed, m_0 not needed, remainders displayed | implication |
| First failed term | ES:88 with ES:192 (2): no hole-filling layer next to a heavy wall at depth | **explicit example, hand-checkable: the stage has no output** |

| Gate defect | Status after this note |
|---|---|
| D1 (LIFT-1) false | Replaced, Theorem LIFT-NL |
| D2 fine-energy claim false | Replaced, Theorem LOC-V; ES:102's cell-energy claim dropped, frozen cells of 𝖠 are now processed |
| D3 exact restoration | Constructed; ES:86 against ES:188 does not arise; simultaneous solve split into two commuting pieces |
| D4 multiplicity | m_0 not needed; ledger written for sparse steps. The dense-step count is now an energy budget, conditional on Section 6 |
| D5, D6, D7 | Not touched |
| D8 order of constants | Acyclic order given, Section 5.1. Lemma AD not read here. (QD)'s own order not re-derived |

**Still gaps under this note:** Section 6. Lemma RF and Lemma F, as labelled, not reviewed, and reread here only as needed; the compactly supported straddling bumps at U = 1 in d = 4, whose compact dual to the tent is asserted here and in Theorem F-D but not displayed, and the reading range of N^(j) inside R_c, which holds for block contours and should be checked against rerouted ones; the target of ES:88; (QD) and (Resp+); and what ES:88's target needs near a wall. Lemma CH rests on Lemma AN1's proof, not gated. A claim that a level-j site function is free uses that its fine extension avoids lower layers, which holds on all regions used. The reflection extension of tau at a fan in Lemma STEP+ reads Lemma BG (b) at the level of a paragraph.

## 8. Provenance and what was read

Model: anthropic/claude-opus-5-5 at max effort, mac-mini-worker. Commit `e6028aa14`. Same-model; not independent; not an audit; no status.

*Read:* `FINISH.md`, `GOAL.md`; `gates/energy-stages-codex-b87de884f.md`; ES in full; PE; `library/lattice-uhlenbeck.md`; `library/composite-adjoint.md`; `library/fibre-propagator.md`; `library/analytic-lift.md`; `library/block-poincare-energy-package.md` to Theorem 7; `library/seam-nlpay.md` Sections 1, 4, 5; `library/relative-density-bound.md`, Prop 10 and its hostile pass, Lemma TE; `library/quiet-boundary-rarity.md` to Theorem DM's statement; Text 1, 5, 5.1, 5.2, 5.5 and R1 to R3 of `parts/hard-core--mapped.md`.

*Not read:* `parts/hard-core--independent.md`, any gate on it, `library/shelling-by-hand.md`, `library/adapted-domains.md`, `gates/history-budget-*`, `gates/compute-inventory-*`. The Sussman-Alpoge repository was not opened or needed. A search of the home folder for a local copy was stopped at its time limit, and it returned nothing that was used. No literature was consulted. Uhlenbeck's gauge and Widman's hole-filling are named for credit; their lattice forms are LU and Section 4.

*Numerics.* One job, `checks/lift_nl/lift_nl_kill.py`, under the numeric lock, at 63 percent memory free, peak RSS 0.05 GB, log in `checks/lift_nl/lift_nl_kill.log`. Nothing above rests on it, and the example of Section 6 was not run.
