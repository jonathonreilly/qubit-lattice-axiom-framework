lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T09:57Z

# Lift repair: finite displacement, localized variation, exact restoration

Queue item `lift-repair`, mapped side, pinned at `e6028aa14`. Own derivation, 2026-11-01, by claude-opus-5-5 at max effort. Same-model, unread by anyone else, not independent and not an audit. It grants no status. Abbreviations: **ES** `library/energy-by-stages.md`; **gate** `gates/energy-stages-codex-b87de884f.md`; **PE** `library/paid-inputs-frozen-energy.md`; **AN** `library/analytic-lift.md`; **LU** `library/lattice-uhlenbeck.md`; **RD** `library/relative-density-bound.md`.

Labels as in `FINISH.md`: *discharged*, *implication*, *gap*. "Level of each term" means each term is displayed but constants are not computed.

**State of this file: being written section by section. Sections 1 to 3 are saved; verdicts are at the end when finished.**

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

Let **R^# := the lift of Lemma LW with its tails cut**: x := T^-1 h, x^# := x on the cube Q + rho_t, zero off it, R^# h := Wh_1 x^# + sum_c e_t(c) psi_c, where e_t := h - T x^# is the tail, of size e^{-c_w rho_t} ||h||, and psi_c are the compact biorthogonal bumps of Theorem 6 of the package, at U = 1. Then Q^o R^# h = h exactly, R^# h is supported in the shadow of Q + rho_t + 1, and

    ||d R^# h||_{l^2} <= 2^4 ||d h||_{l^2} + C e^{-c_w rho_t} ||h||_{l^2},    ||R^# h||_{l^4} <= C_7 ||h||_{l^4},

the first by (LW), the second since Wh_1 is a tent product with scale-invariant l^4 norm and T^-1 has an exponentially decaying kernel. rho_t := (2/c_w) log(2 + R) makes the tail term at most C ||h||_{l^4} / (2 + R), since ||h||_{l^2(Q)} <= C R ||h||_{l^4}.

**Theorem LIFT-NL (finite gauge-corrected displacement; implication, given Lemma U, Lemma LW, Lemma CH, the bumps; level of each term).** *Let Q be a cube of radius R in level-j cells, with the shadow of Q + rho_t + 2 at positive distance from every lower layer. Let U be a fine field on that shadow, with chain all-lines there, energy eps^2 := ||theta(U)||^2 there, W := V_j(U). Let W' be a level-j field equal to W off Q, and suppose there is a level-j site function sigma, equal to 1 off Q, with G . W'^sigma = e^{i (v + h)} on Q, h supported on Q, in the frames G of Section 2. If eps + ||h||_{l^4} <= eps_2(L), there is a fine field U' with*

    V_j(U') = W' exactly,   U' = U off the shadow of Q + rho_t + 1,   all lower data unchanged,
    A(U') <= A(U) + N D + D^2/2,    N := ||theta(U)||_(shadow of Q + rho_t + 2),
    D <= 2^4 ||d h||_{l^2} + C (1 + C_2(L)) ( eps + ||h||_{l^4} ) ||h||_{l^4} + C ||h||_{l^4}/(2 + R).        (LIFT-NL)

*Here d h is the flat curl of the small field h, and the exact level-j curvature displacement Theta^j := Theta(e^{i v}, e^{i (v + h)}) obeys ||d h|| <= ||Theta^j|| + C (||v||_{l^4} + ||h||_{l^4}) ||h||_{l^4}. If sigma puts h in relative Coulomb gauge on Q, then ||h||_{l^4} <= C ||d h||, by Gaffney and the lattice Sobolev inequality for a compactly supported field, so*

    D <= (2^4 + C_8(L) (eps + ||Theta^j||) + C/(2 + R)) ||Theta^j||.

*Consequently, if U = U^* is a minimiser for Phi_j(W), and every field with level-j data W' of flux at most T_2 has action at least Phi_j(W'), which is Xi_j >= 0:*

    Phi_j(W') <= Phi_j(W) + N D + D^2/2.

*Proof.* Solve H = R^#( h - [R(a + H) - R(a)] ). By (CH) and ||R^#||_{l^4} <= C_7, this is a contraction for C C_7 C_2(L) (eps + ||h||_{l^4}) <= 1/2, on ||H||_{l^4} <= 2 C_7 ||h||_{l^4}, in the norm of l^4 and in the local one. Then Q^o H + R(a + H) - R(a) = h, so log N^(j)(e^{i (a + H)}) = v + h. With zeta := R(a + H) - R(a), Cauchy-Schwarz over bonds, **not a count of bonds**, gives

    ||zeta||_{l^2} <= 2 C_2(L) ( sum_c ( e_j(c; a) + e_j(c; a + H) )^4 )^(1/4) ( sum_c e_j(c; H)^4 )^(1/4) <= C C_2(L) (eps + ||H||_{l^4}) ||H||_{l^4},

as sum_c e_j(c; .)^4 has finite overlap. So ||d H|| <= 2^4 ||d h|| + C ||zeta||_{l^2} + tail: **there is no factor of the radius R in the constraint's second-order term.** For a fine plaquette, BCH gives Theta_p(e^{i a}, e^{i (a + H)}) <= |(d H)_p| + C (|a|_p + |H|_p) |H|_p, so in l^2, by Hoelder, D := ||Theta|| <= ||d H|| + C (eps + ||H||_{l^4}) ||H||_{l^4}. That bounds D as stated.

*Exact data.* M^j(e^{i (a + H)}) = G_1(a + H)^-1 . e^{i (v + h)}, while W' = sigma^-1 g^-1 G_1(a)^-1 . e^{i (v + h)}. So the two differ by a level-j site function kappa, equal to 1 where neither H nor sigma reaches. Transform the field by a fine site function equal to kappa at level-j sites and 1 at all other fine sites. That is U', and its plaquettes are unchanged. Lower data lie outside the shadow, so they do not move. (FD), applied to U^g and e^{i (a + H)}, gives the energy. The relation between d h and Theta^j is BCH on level-j plaquettes, and Gaffney for compact support is Step 1 of LU on a torus containing Q. For the last line, Phi_j(W') <= A(U') by the hypothesis Xi_j >= 0, and A(U) = Phi_j(W). QED at this level.

*What it does not read:* Lemma AD, (R3), Theorem F, the multiplier, the size of the fine energy of U away from the support, and any count of bonds.

**Hand test 1, commutator square, j = 0, W = 1.** No chain, Q^o = 1. With sigma := 1, h is the exact gradient, ||d h|| = 0, ||h||_{l^4} of order t, and the bound keeps C ||h||_{l^4}^2 of order t^2, so D^2 of order t^4, against the true action 2 sin^4 t plus the other plaquettes: consistent, and it does not assert zero. With sigma(x) := e^{omega_x}, the bond becomes e^{omega_x} e^{omega_y - omega_x} e^{-omega_y} = exp( (1/2) [omega_x, omega_y] + O(t^3) ), of size t^2. So relative gauge reduces ||h||_{l^4} to order t^2, and D is the exact curvature at leading order. **Passes.**

**Hand test 2, locked frozen pair, j >= 1.** W = 1, U the explicit minimiser of PE, (E5), Phi_j(1) = M e(a) > 0. The hypothesis puts the shadow of Q away from all lower layers, so away from the pairs, where U = 1. So eps = 0, N = 0, a = 0, and the statement reads Phi_j(W') <= M e(a) + D^2/2. That is true, and it is a statement about the *variation*: the term M e(a) sits on both sides and is not bounded by anything. Nothing here compares the fine energy of the lift with the coarse curvature, which is the statement the gate refuted. **Passes.**
