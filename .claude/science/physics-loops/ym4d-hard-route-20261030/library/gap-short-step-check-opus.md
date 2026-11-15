lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T09:21Z

# Check of row 1018 (`gap-short-step-max`), work item W1

Row 1022. Claude Opus 5.5 max, Mac mini worker 3. Started 2026-11-15 21:21Z.
Pinned at commit 54b9ac6aa on branch `claude/ym4d-hard-route`.
Checked text: `library/gap-short-step-max.md` (written by Claude Fable 5.2, row 1018).
Same provider as the author, so this check is not independent.
Task: do work item W1 of that note's Section 8.7 exactly as written: the statements in its order, the tests first, the verdicts and the stop rule. Give Lemma PAR and Lemma NAB the most care. No new attack.

## W1 as written (row 1018, `library/gap-short-step-max.md` L475)

Statements, in this order: (i) Lemma ADD (2.2) with D(2a) = 16 D(a) - Phi(a); (ii) Lemma CHAIN (2.3); (iii) Lemma PAR (3.2), Fact 0, (i)-(iii), and the second derivation 7.2; (iv) Corollary MP (7.4); (v) Lemma FLOW (4.1); (vi) Lemma PROJ (4.2) and Lemma FR+ (4.3); (vii) Lemma SPLIT (4.4); (viii) Lemma NAB (5.4) (i)-(iii) with every constant; (ix) Lemma DICH and Proposition ENG (5.1, 5.5).

Tests first: (a) PAR: a twist system with (H1), (H2) exists for Sigma x D with paths ending at one common boundary point, and boundary plaquettes are unchanged; (b) PAR (i): Z_j(tau_S eta) = Z_j(tau_j eta) for j in S; (c) NAB (ii): (x; 1, 3) is the only plaquette containing links (x, 1) and (x, 3) when all sides are at least 3; the gauge-average constant sum_i ((c x e_i) x (c' x e_i)) . e = (c x c') . e; E[X^4] <= 108 beta^2; (d) NAB (iii): lambda_x = lambda_2 + lambda_3 and e_2 <= tr M (lambda_2 + lambda_3); (e) FLOW: the Jacobian formula; (f) the hand values of the map in 3.4.

Then judge the ARGUED items: the two cautions of 3.4, the sizes of 4.5, the reading 5.3, the last column of 3.3.

Verdict per statement: ADVANCE, CORRECT-NO-ADVANCE or WRONG with the failing line. Stop rule: stop at the first WRONG in Lemma PAR or Lemma NAB and report it; no new attack.

Note on effort: W1 asks for high effort; the row (1022) runs this at max. Same provider (Anthropic) as the author (Claude Fable 5.2), so this is not an independent check.

## Plan (at most eight steps; updated in place)

1. Done: read FINISH rules, rows 1018 and 1022, the note's 8.7 (W1). Duplicate check (below).
2. Tests (a), (b) with Lemma PAR (3.2), Fact 0, (i)-(iii), 7.2, and Corollary MP (7.4). PAR gets the most care. Stop rule applies.
3. Tests (c), (d) with Lemma NAB (5.4) (i)-(iii), every constant. Stop rule applies.
4. Lemma ADD (2.2) and Lemma CHAIN (2.3).
5. Test (e) with Lemma FLOW (4.1); Lemmas PROJ (4.2), FR+ (4.3), SPLIT (4.4).
6. Lemma DICH and Proposition ENG (5.1, 5.5); test (f), the map of 3.4.
7. ARGUED items: two cautions of 3.4, sizes of 4.5, reading 5.3, last column of 3.3.
8. Verdict table in W1's order; RESULT line.

Order note: W1 fixes the order of the statements and puts the tests first. The tests (a)-(d) sit inside PAR and NAB, and the stop rule binds there, so I run PAR and NAB (with their tests) first. The verdict table at the end is in W1's order (i)-(ix).

## Progress log

- 21:21Z (`date -u`): file created.
- Step 1 done before 21:27Z (an earlier estimate of 21:30Z is replaced).
- 21:27Z (`date -u`): step 2 written (PAR, MP: no WRONG). Step 3, Lemma NAB, next.

## Step 1. Duplicate check and scope

This row is a check of row 1018, named by the queue (row 1022). It attacks no open lemma, so the duplicate rule (FINISH How we work 0a) binds only if I were to attack. W1 says "no new attack", and I make none.

**Verdict words.** ADVANCE: correct, and it changes the lane's record (a new exact tool, a RECALLED item now written, a filter narrowed). CORRECT-NO-ADVANCE: correct, and the record does not change. WRONG: a line fails; the line is named. This is the reading used by the row-1014 check.

## Step 2. Tests (a), (b); Lemma PAR (3.2), Fact 0, (i)-(iii); the second derivation 7.2; Corollary MP (7.4)

Read in full: the note L150-181 (3.2), L414-420 (7.2), L429-441 (7.4). Everything below is redone by hand. No source outside the note was used for this step.

### Fact 0 (CORRECT)
Haar measure on each integrated link is invariant under multiplication by the central element -1. Substitute U -> tau U on Lam. Then t_p(tau U, tau Om) = (d tau)_p t_p(U, Om) = t_p(U, Om) when d tau = 1 on every plaquette of the model. So Z(tau|_bd Om) = Z(Om). The hypothesis "t_p changes sign when one link is multiplied by -1" holds for SU(2) (central -1 commutes out of the ordered product, and (-1)^(-1) = -1), Z_2, and the 2-dimensional faithful representations of Q_8 and 2T.

### Test (a): a twist system with (H1), (H2) on Sigma x D, common exit, boundary plaquettes unchanged. PASS, with two remarks.
Construction (flat case; written out). Coordinates (x1, x2) on Sigma (a closed lattice surface; take the 2-torus of a lattice periodic in directions 1, 2), (x3, x4) on D = {0, ..., m}^2, m >= 2. bd = the links of Sigma x dD: links in directions 1, 2 at vertices of dD, and links of dD (direction-4 links at x3 in {0, m}, direction-3 links at x4 in {0, m}), at every (x1, x2). Lam = the other links of Sigma x D. Sub-containers Lam_i = interior links of Sigma x D_i for squares D_i in D. Two squares that share an edge line still have no plaquette with links of both interiors (the shared line is boundary for both), so a 2 x 2 tiling is allowed.
For a dual path gamma in the (3, 4) dual plane, let tau = -1 on the transverse (direction 3 or 4) links crossed by gamma, at every (x1, x2), and +1 elsewhere. Then: (1, 2)-plaquettes have d tau = 1 (all links +1); (k, 3) and (k, 4) plaquettes, k in {1, 2}, have d tau = 1 (their two transverse links sit at the same transverse position, so they carry equal signs); a (3, 4)-plaquette has d tau = -1 exactly when its centre is an endpoint of gamma (mod 2 coboundary of a dual path in 2D).
Take gamma_i from a dual point c_i deep inside D_i (so the (3, 4)-plaquettes around c_i have all four links in Lam_i, hence lie in P_i) to one common dual point e just outside D, e.g. e = (-1/2, y4) with 0 < y4 < m. Every gamma_i stays strictly inside D except for one common last step (1/2, y4) -> (-1/2, y4), which crosses the direction-4 link at x3 = 0, x4 in [y4 - 1/2, y4 + 1/2], a bd link. Then:
- (H1): tau_i|_bd = sigma for every i, with sigma = -1 exactly on that row of bd links (one per (x1, x2)).
- (H2): d tau_i = -1 only on the (3, 4)-plaquettes around c_i (in P_i) and around e. The plaquettes around e have no link in Lam, so they are not plaquettes of the container's model. So tau_i is closed on every model plaquette outside P_i.
- Boundary plaquettes (all four links in bd) are unchanged: the (1, 2) and (k, 3), (k, 4) ones by the rule above; for m >= 2 no (3, 4)-plaquette of D has all four links in dD.
- sigma|_bd is closed on dGamma = Sigma x S^1 and has holonomy -1 around each transverse circle {s} x dD (one crossing). So it is the vortex twist of the container, and tau_i|_(bd_i) has holonomy -1 around {s} x dD_i (gamma_i leaves D_i once), so r_i is the vortex ratio of sub-container i. Any two fields with the same restriction class differ by d g with g = +-1 on boundary sites; extending g by +1 inside gives a closed field, so by Fact 0 the ratios do not depend on the choice of path.
- A non-flat Sigma (for example the boundary of a 3-cube in a hyperplane, with D = radial interval x x4-interval) works the same way: Sigma x {c} is then a closed dual cube surface, and Sigma x gamma is a union of shells and slabs of dual 3-cells with mod-2 boundary Sigma x {c} + Sigma x {e}.
Remark 1. e must lie outside D (a dual point cannot lie on the primal boundary); "a fixed point of the boundary of D" is read as the common exit crossing. Remark 2. The clause "avoiding the other D_j" (L177) is not needed and cannot always be met: with a 2 x 2 tiling and one common exit, two of the paths must cross another sub-square. It is harmless: (H2) needs only d tau_i = 1 on P_j, and Fact 0 allows tau_i to be non-trivial on Lam_j and bd_j. Neither remark changes a statement.

### Test (b): Z_j(tau_S eta) = Z_j(tau_j eta) for j in S. PASS.
tau_S = tau_j tau' with tau' = prod over k in S, k != j, of tau_k. Each such tau_k is closed outside P_k, hence on P_j (the P's are disjoint: a plaquette in P_j and P_k would contain links of Lam_j and Lam_k). So tau' is closed on all of P_j, and Fact 0 in sub-container j with pin tau_j eta gives Z_j(tau' tau_j eta) = Z_j(tau_j eta). Also bd_j lies outside every Lam_k (a bd_j link in Lam_k would put a plaquette of P_j in P_k), so Z_j is a function of the outer links eta, as the proof needs.

### Lemma PAR (i) (CORRECT)
Marginal of the outer links eta (pin Om on bd): weight exp(A_rest(eta)) prod_j Z_j(eta|_(bd_j)), where A_rest sums the plaquettes in no P_j; every plaquette is in at most one P_j and the others see only outer links. Then Z(sigma^|S| Om) = integral of exp(A_rest(eta)) prod_j Z_j(eta) with pin sigma^|S| Om. Since tau_S = sigma^|S| on bd (H1), write eta = tau_S eta' with eta' pinned to Om; the substitution on the integrated outer links is Haar-invariant. A_rest(tau_S eta') = A_rest(eta') (tau_S is closed outside the union of P_i, i in S). Z_j(tau_S eta') = Z_j(eta') for j not in S (Fact 0; tau_S closed on P_j). Z_j(tau_S eta') = Z_j(tau_j eta') = r_j Z_j(eta') for j in S (test (b)). So Z(sigma^|S| Om) = Z(Om) E[prod_S r_i], and sigma^|S| = sigma or 1. Case S empty gives 1. Consistent.

### Lemma PAR (ii) (CORRECT)
E[prod (1 + eps_i r_i)] = sum_S (prod_S eps_i) E[prod_S r_i] = sum over even S + rho sum over odd S = (1/2)[P_+ + P_-] + (rho/2)[P_+ - P_-], with P_+- = prod (1 +- eps_i). Values: eps = +1: 2^(n-1)(1 + rho); eps = -1: 2^(n-1)(1 - rho); mixed: P_+ = P_- = 0, so 0. With Etilde[X] = E[X prod (1 + r_i)]/(2^(n-1)(1 + rho)) and prod_M a_i prod_i (1 + r_i) = prod_M (1 - r_i) prod_(not M) (1 + r_i): proper non-empty M gives 0; M = all gives (1 - rho)/(1 + rho) = tanh(V/2) with rho = e^(-V). The weight is positive, so Etilde is a probability.

### Lemma PAR (iii) (CORRECT)
The joint cumulant is sum over partitions pi of (|pi| - 1)! (-1)^(|pi| - 1) prod over blocks of the block moment. Every partition with two or more blocks has only proper non-empty blocks, each with moment 0 by (ii). So the cumulant is Etilde[a_1 ... a_n] = tanh(V/2). For n = 1 this reads Etilde[a_1] = tanh(V/2), consistent. Sup bound: v_i(tau_i om) = - v_i(om) (r_i(tau_i om) = 1/r_i(om), tau_i^2 = 1), so the value set of v_i is symmetric, sup |v_i| = sup v_i = xi_i >= 0, and sup |a_i| = tanh(xi_i/2) (tanh odd and increasing; the sup over all pins of bd_i bounds a_i at every outer configuration). Hoelder with n exponents n gives the moment form. Also V(sigma Om) = - V(Om), so the container's own xi = sup V = sup |V| >= 0, and xi <= min_i xi_i ("at most that of any parallel sub-container") holds.
Wording only (no statement changes): L179 "tanh(V/2) multiplies over parallel sub-containers" is an inequality, tanh(xi/2) <= prod tanh(xi_i/2), not a product law.

### 7.2, the second derivation in 2D Z_2 (CORRECT)
Z_A(W) = C_A (1 + W t^A): for a disc with pinned boundary, interior link configurations map onto plaquette configurations with product W, each fibre of size 2^(V_int) (H^1(D, dD; Z_2) = 0 and E_int - V_int = A - 1 by Euler), and the sum over sign vectors with fixed product is (1/2)[(2 cosh b)^A + W (2 sinh b)^A]. rho = (1 - t^A)/(1 + t^A), tanh(V/2) = t^A. r_i = (1 - W_i t^(A_i))/(1 + W_i t^(A_i)), a_i = W_i t^(A_i), Z_i(W_i)(1 + r_i) = 2 C_(A_i). Law of (W_1, W_2) on the rest region (a disc with two holes, outer boundary pinned): the map from its link configurations to (U_p, W_1, W_2) is onto the set with prod U_p W_1 W_2 = W_Om, with fibres of equal size (Euler characteristic -1 gives E' - V' = A_0 + 1, matching 2^(A_0 + 1) tuples). So the weight is proportional to 1 + W_1 W_2 t^(A_0), Etilde[W_1] = 0, Etilde[W_1 W_2] = t^(A_0), Etilde[a_1 a_2] = t^A. I also checked Lemma PAR (i) in this model: E[r_1] = 4(1 - t^A)/(4(1 + t^A)) = rho. This is the same author's consistency test, as the note says; my recomputation is a second derivation by a different model of the same provider.

### Corollary MP (7.4) (CORRECT)
With tau_i = +1 on the pinned links, eta = tau_S eta' leaves the pin unchanged. Z_j(tau_S eta') = Z_j(eta') for j not in S; Z_i(tau_i tau_S eta') = Z_i(eta') for i in S (tau_i tau_S is a product of tau_k, k != i, closed on P_i); O(tau_S eta') = (-1)^|S| O(eta'). So E[O prod_S r_i] = (-1)^|S| E[O], and E[prod_S r_i] = 1. Then E[O prod (1 - r_i)] = 2^n E[O], E[prod (1 + r_i)] = 2^n, and 1 - r_i = (1 + r_i) a_i give E[O] = Etilde[O a_1 ... a_n] and |E[O]| <= sup|O| prod tanh(xi_i/2). The example holds: for a closed Sigma x {c_i} take tau_i = -1 across a spanning 3-chain of it (d tau_i = -1 only on P_i), and a loop C outside the containers that links each Sigma x {c_i} crosses each chain an odd number of times, so (1/2) tr of its holonomy is odd under each tau_i. xi_i is the vortex cost for the restriction tau_i|_(bd_i), whose transverse holonomy is -1; the identity holds for any such restriction.
Not checked here: the attribution to Mack and Petkova's (2.16), (2.19)-(2.21) (W1 does not ask for it; the paper was not fetched by this check).

### Verdicts of Step 2
- Fact 0: CORRECT-NO-ADVANCE (a change of variables).
- Lemma PAR (i)-(iii): ADVANCE. Correct as stated; the exact cumulant form and the written proof are new to the lane's record. It is blind (the note says so, and frozen Z_2 keeps it).
- 7.2: CORRECT-NO-ADVANCE (a consistency test).
- Corollary MP: ADVANCE in the narrow sense: the lane's RECALLED Mack-Petkova criterion now has a written proof. Off the direct path of (W) (centre-odd sector only).
- Stop rule: not triggered by Lemma PAR.

## Step 3. Tests (c), (d); Lemma NAB (5.4) (i)-(iii), every constant

Read in full: the note L306-319 (5.4) and L363-387 (6.1); Lemma FR of row 1011 (`library/gap-pinned-cell-gauge-max.md` L460-473). Everything below is redone by hand. Conventions are the lemma's own: weight exp(A), A = beta sum_p x_p, Haar links; D = d/d eps of U_l -> exp(eps c) U_l on one link l with tail x; Haar invariance gives E[D G] + E[G D A] = 0.

### Basic formulas (CORRECT)
For a representative U_q that leaves x along l, D U_q = c U_q. Quaternion product: c U = (- c . y, x c + c x y), so D x_q = - c . y_q, D y_q = x_q c + c x y_q. Each of the six plaquettes on l has such a representative (cyclic shift and inversion keep (1/2) tr), so X = D A = - beta sum over the six q of c . y_q. D X = - beta sum_q c . (x_q c + c x y_q) = - beta sum_q x_q.

### Lemma NAB (i) (CORRECT on a torus with all sides equal; see defect N1)
G = X: E[X^2] = - E[D X] = beta sum_q E x_q. G = c . y_q: D G = c . (x_q c + c x y_q) = x_q, so E[(c . y_q) X] = - E x_q. The gauge rotation at x maps y_q to R y_q for q based at x (U_q -> g U_q g^(-1)) and keeps the measure, so E[(c . y_q)^2] = E|y_q|^2/3 = E(1 - x_q^2)/3. Cauchy-Schwarz: (E x_q)^2 <= (E(1 - x_q^2)/3) beta sum_(q' on l) E x_(q'). With one common mean xbar for all plaquettes this is xbar^2 <= E(1 - x^2) 6 beta xbar/3, i.e. E(1 - x_p^2) >= xbar/(2 beta). xbar > 0 for beta > 0: d/d beta of log Z is the sum of the plaquette means, 0 at beta = 0, and its derivative is a variance > 0.
Remark (a) (one free plaquette, equality E(1 - x^2) = 3 E x/beta) is correct by the same two identities with one plaquette.

### Test (c). PASS on all three items.
- (c1) A plaquette containing (x, 1) and (x, 3) lies in a (1, 3)-plane. The plaquettes of that plane containing (x, 1) are (x; 1, 3) and (x - e3; 1, 3). The second has direction-3 links (x - e3, 3) and (x - e3 + e1, 3); neither is the link (x, 3) unless L_3 = 1 or e1 = e3 on the torus. So (x; 1, 3) is the only one when all sides are at least 2; "at least 3" is more than enough. Hence D D' A = beta D D' x_(x;1,3), and with U_(x;1,3) -> exp(eps c) U exp(- eps' c') (the link (x, 3) enters as its inverse), D D' x = - Re(c U c'), |D D' x| <= 1, |D D' A| <= beta.
- (c2) The vector identity (A x B) x (C x D) = C [(A x B) . D] - D [(A x B) . C] gives (c x e_i) x (c' x e_i) = - e_i [(c x e_i) . c'] = e_i [e_i . (c x c')]. Summed over i: c x c'. Dotted with e: (c x c') . e. And the SO(3) average of (R u)_a (R v)_b is (u . v/3) delta_ab, which is the step that produces this sum.
- (c3) G = X^3: E[X^4] = - 3 E[X^2 D X] = 3 beta E[X^2 sum_q x_q] <= 18 beta E[X^2] <= 18 beta (6 beta) = 108 beta^2. This holds on any torus (E[X^2] = beta sum_q E x_q <= 6 beta needs no symmetry).

### Lemma NAB (ii) (CORRECT on a torus with all sides equal)
D (link (x, 1)) moves y_p, p = (x; 1, 2), and not y_p' (p' = (x; 3, 4) does not contain (x, 1)); D' (link (x, 3)) moves y_p' and not y_p. D and D' act on different links and commute, D' y_p = 0, D y_p' = 0, so D D' f = (D y_p x D' y_p') . e exactly. The expansion has four terms; under the common gauge rotation at x (x_p, x_p' fixed) the two terms linear in y average to 0, and the bilinear term gives (1/3) E[y_p . y_p'] (c x c') . e by (c2). So E[D D' f] = (c x c') . e (E[x_p x_p'] + (1/3) E[y_p . y_p']).
Integration by parts: D D' e^A = (X X' + D D' A) e^A = S_2 e^A; two integrations by parts (signs (-1)^2) give E[f S_2] = E[D' D f] = E[D D' f], and E[S_2] = 0 (not used further).
E[S_2^2] <= 2 E[X^2 X'^2] + 2 E[(D D' A)^2] <= 2 (E X^4 E X'^4)^(1/2) + 2 beta^2 <= 216 beta^2 + 2 beta^2 = 218 beta^2.
Cauchy-Schwarz: (E[D D' f])^2 <= E[f^2] 218 beta^2; E[f^2] = E|y_p x y_p'|^2/3 (the cross product rotates with the common rotation). With (c x c') . e = 1 (c = e1, c' = e2, e = e3): E|y_p x y_p'|^2 >= 3 (bracket)^2/(218 beta^2). Second claim: x x' >= x + x' - 1 on [-1, 1]^2 ((1 - x)(1 - x') >= 0), so E[x_p x_p'] >= 2 xbar - 1; |y_p . y_p'| <= (|y_p|^2 + |y_p'|^2)/2 and 1 - x^2 <= 2(1 - x), so |E[y_p . y_p']| <= 2(1 - xbar). Bracket >= 2 xbar - 1 - (2/3)(1 - xbar) = (8 xbar - 5)/3 >= 1/3 at xbar >= 3/4. Right side >= 3 (1/9)/(218 beta^2) = 1/(654 beta^2). All constants confirmed.

### Test (d). PASS.
|y x n|^2 = |y|^2 - (y . n)^2, so the sum over the six plaquettes based at x is tr M - n^T M n, M = sum_p y_p y_p^T (positive semi-definite). Its minimum over unit n is tr M - lambda_1 = lambda_2 + lambda_3 = lambda_x. And (lambda_1 + lambda_2)(lambda_2 + lambda_3) - e_2 = lambda_2^2 >= 0, with lambda_1 + lambda_2 <= tr M (lambda_3 >= 0). So e_2 <= tr M (lambda_2 + lambda_3).

### Lemma NAB (iii) (CORRECT)
e_2 = (1/2)((tr M)^2 - tr M^2) = (1/2) sum over p, p' of (|y_p|^2 |y_p'|^2 - (y_p . y_p')^2) = sum over p < p' of |y_p x y_p'|^2 (Lagrange; diagonal terms vanish). So lambda_x tr M >= e_2, and lambda_x >= e_2/tr M when tr M > 0 (tr M = 0 forces both sides to 0). tr M <= 6. So lambda_x >= (1/6) |y_p x y_p'|^2 for the pair p = (x; 1, 2), p' = (x; 3, 4), which are two of the six plaquettes based at x. E lambda_x >= 1/(6 * 654 beta^2) = 1/(3924 beta^2). Lemma FR (row 1011 7.3; I redid its last line: |s_p x n_x|^2 <= sum over the four links of p of |D_l n|^2, summed over all plaquettes, each plaquette has one base, each link lies in 6 plaquettes in 4D) gives sum_l |D_l n|^2 >= NA/6 for every configuration and every frame, so E sum_l |D_l n|^2 >= (number of sites) E lambda_x/6 >= (number of sites)/(23544 beta^2), and 6 * 3924 = 23544. "However it depends on the field" holds because Lemma FR is pointwise in the configuration.

### Defect N1 (hypothesis; does not break the lemma or a consumer)
Line L308: "a torus with all sides at least 3" with "xbar = E x_p". The proof uses one common mean for all plaquettes twice: in (i), E[X^2] = 6 beta xbar needs the six plaquette means on the link to equal E x_p; in (ii), E[x_p x_p'] >= 2 xbar - 1 and |E[y_p . y_p']| <= 2(1 - xbar) need the (1, 2) and (3, 4) means equal. On a torus with unequal sides the plaquette means of different planes differ in general, xbar is not one number, and the line "E[X^2] = - E[D X] = beta sum_q E[x_q] = 6 beta xbar" fails. Without symmetry the same proof gives only E(1 - x_q^2) >= 3 (E x_q)^2/(beta sum_(q' on l) E x_(q')) >= (E x_q)^2/(2 beta). Repair: read "a torus with all sides equal, L >= 3" (the hypercubic group then maps any plaquette to any other, so xbar is one number), or any state invariant under translations and the hypercubic group. The control run (4^4) and the uses in the note (in law, translation-invariant) are of this kind. I do not mark it WRONG: the setting defines xbar = E x_p for an unnamed p, which presupposes one common mean, and on every torus where that holds each line is correct. The stop rule is not triggered.

### Remarks (b)-(d) of 5.4
(b) correct: (ii) has the expected order 1/beta^2 for the cross product; the loss to 1/beta^2 in E lambda_x comes from tr M <= 6 where tr M is typically of order 1/beta. (c) arithmetic correct (1 - 2/8 = 3/4); the bound E(1 - x_p) <= 2/beta stays RECALLED and is not used by the lemma. (d) correct in substance; the constants change with the number of plaquettes on a link (2(d - 1)), so "dimension free" means "the proof works in every dimension with changed constants".

### 6.1 (the control run): not rerun (W1 does not ask for it, and a run proves nothing). Its readings were written before the run and match the identities checked here.

### Verdicts of Step 3
- Lemma NAB (i), (ii), (iii): ADVANCE (with repair N1). Correct by hand with every constant (6 beta xbar, 108 beta^2, 218 beta^2, (8 xbar - 5)/3, 1/(654 beta^2), 1/(3924 beta^2), 1/(23544 beta^2)). It turns row 1011's ARGUED "mean frame defect is positive" into a proved lower bound of order 1/beta^2. It is blind (holds in five dimensions and in the frozen-slice model), as the note says.
- Stop rule: not triggered by Lemma NAB.
