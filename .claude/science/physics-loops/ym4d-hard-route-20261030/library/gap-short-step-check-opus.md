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
- 21:31Z: step 3 written (NAB: no WRONG; defect N1, hypothesis). 21:33Z: step 4 (ADD, CHAIN). 21:36Z: step 5 (FLOW, PROJ, FR+, SPLIT). 21:37Z: step 6 (DICH, ENG, test (f)). Step 7, the ARGUED items, next.
- 21:41Z: step 7 written. Next: a bounded source check of the Mack-Petkova credit for Corollary MP (an independent published derivation, if their (2.16) is the same identity), then step 8 (verdict table, RESULT).
- 21:43Z (`date -u`): source check and step 8 written. All eight steps done.

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

### Defect N1 (= D1 of Step 8; hypothesis; does not break the lemma or a consumer)
Line L308: "a torus with all sides at least 3" with "xbar = E x_p". The proof uses one common mean for all plaquettes twice: in (i), E[X^2] = 6 beta xbar needs the six plaquette means on the link to equal E x_p; in (ii), E[x_p x_p'] >= 2 xbar - 1 and |E[y_p . y_p']| <= 2(1 - xbar) need the (1, 2) and (3, 4) means equal. On a torus with unequal sides the plaquette means of different planes differ in general, xbar is not one number, and the line "E[X^2] = - E[D X] = beta sum_q E[x_q] = 6 beta xbar" fails. Without symmetry the same proof gives only E(1 - x_q^2) >= 3 (E x_q)^2/(beta sum_(q' on l) E x_(q')) >= (E x_q)^2/(2 beta). Repair: read "a torus with all sides equal, L >= 3" (the hypercubic group then maps any plaquette to any other, so xbar is one number), or any state invariant under translations and the hypercubic group. The control run (4^4) and the uses in the note (in law, translation-invariant) are of this kind. I do not mark it WRONG: the setting defines xbar = E x_p for an unnamed p, which presupposes one common mean, and on every torus where that holds each line is correct. The stop rule is not triggered.

### Remarks (b)-(d) of 5.4
(b) correct: (ii) has the expected order 1/beta^2 for the cross product; the loss to 1/beta^2 in E lambda_x comes from tr M <= 6 where tr M is typically of order 1/beta. (c) arithmetic correct (1 - 2/8 = 3/4); the bound E(1 - x_p) <= 2/beta stays RECALLED and is not used by the lemma. (d) correct in substance; the constants change with the number of plaquettes on a link (2(d - 1)), so "dimension free" means "the proof works in every dimension with changed constants".

### 6.1 (the control run): not rerun (W1 does not ask for it, and a run proves nothing). Its readings were written before the run and match the identities checked here.

### Verdicts of Step 3
- Lemma NAB (i), (ii), (iii): ADVANCE (with repair N1). Correct by hand with every constant (6 beta xbar, 108 beta^2, 218 beta^2, (8 xbar - 5)/3, 1/(654 beta^2), 1/(3924 beta^2), 1/(23544 beta^2)). It turns row 1011's ARGUED "mean frame defect is positive" into a proved lower bound of order 1/beta^2. It is blind (holds in five dimensions and in the frozen-slice model), as the note says.
- Stop rule: not triggered by Lemma NAB.

## Step 4. Lemma ADD (2.2) with D(2a) = 16 D(a) - Phi(a); Lemma CHAIN (2.3)

Read in full: the note L85-130; `library/gap-crux-restate.md` L27-47 (the objects F, f, Delta, Lemma A and its consequences); `library/gap-mid-max.md` L64-67 ((CAS) and Proposition Delta); row 1011 3.1-3.2 (`library/gap-pinned-cell-gauge-max.md` L131-178: cells, weights, F_c = - log Z_c, Proposition A).

### The identity D(2a) = 16 D(a) - Phi(a) (CORRECT)
D(2a) = F((2a)^4) - f (2a)^4 = F((2a)^4) - 16 f a^4, and 16 D(a) - Phi(a) = 16 F(a^4) - 16 f a^4 - 16 F(a^4) + F((2a)^4) is the same. Phi >= 0 is the input "F(n)/|n| is non-increasing in each side" (run 2, Lemma 1 (c), as gap-crux-restate L41 records it), applied in the four directions.

### Lemma ADD (CORRECT)
(T-per) at a: D(2a) <= D(a) - delta, i.e. 16 D - Phi <= D - delta, i.e. Phi >= 15 D + delta. (CAS) at a: D(2a) <= theta D(a), i.e. Phi >= (16 - theta) D. Both are stated on the same range 6.1 x 10^(-4) < D(a) <= M with D(3) <= M ((CAS) at gap-mid-max L65 has exactly this form). (CAS) => (T-per): on the range (1 - theta) D(a) > (1 - theta) 6.1 x 10^(-4) =: delta. (T-per) => (CAS): D(a) - delta = D(a)(1 - delta/D(a)) <= D(a)(1 - delta/M) =: theta D(a). If delta > M, then (T-per) forces the range to be empty (D(2a) <= M - delta < 0 is impossible), and (CAS) holds vacuously with the same theta; so the proof as written needs no case split.
The series D(a) = sum over k >= 0 of Phi(2^k a)/16^(k+1): iterate D(a) = Phi(a)/16 + D(2a)/16; the remainder D(2^K a)/16^K = a^4 (F/|n| - f) at side 2^K a. It tends to 0: F/|n| is non-increasing in each side, and for any torus n the cube of side 2^K a dominates n in every side for K large, so the limit along the doublings is at most F(n)/|n| for every n, hence equal to f. The note's "which tends to 0" is correct; this is the line that supplies it. "Scale invariant gives Phi = 15 D": Phi constant gives D = Phi/15.
The paragraph "False for compact U(1) and for a product with a massless factor" is a correct implication from its named inputs (Corollary PT1 and I28, Proposition Delta given Theorem SH): no seed gives D(a) > 6.1 x 10^(-4) at every a >= 3; (T-per) from a = 3 gives D(3 * 2^k) <= M - k delta, below 6.1 x 10^(-4) after more than (M - 6.1 x 10^(-4))/delta doublings. The inputs were not re-checked here (W1 does not ask).

### Lemma CHAIN (CORRECT)
Weights add across scales: for a plaquette p of Q, with k_Q the number of its two normal directions in which it lies on the boundary of Q, the fine cells inside Q that contain p are a fraction 2^(-k_Q) of all fine cells that contain p, and the coarse weight of p for Q is also 2^(-k_Q) (inside Q a coarse grid hyperplane is a face of Q). So sum over fine cells c in Q of A_c = A_Q with Q's own weights. Interior links of a cell lie only in plaquettes of that cell, so given the ring links the cell interiors are independent, and Z_Q(Omega) = integral over inner ring links of prod_c Z_c(omega_c), i.e. F_Q = - log integral exp(- sum_c F_c).
For F = - log integral e^(-G): F' = E[G'], F'' = E[G''] - Var(G') in the ring law. With the extension by zero, Proposition A gives d_l F_c = E_c[c . N_l^c] = c . Nbar_l^c (F_c' = - E[A_c'] and A_c' = - c . N_l^c). No cell contains both l and l', so d_l d_l' sum_c F_c = 0 and d_l d_l' F_Q = - Cov(sum over c containing l of c . Nbar_l^c, sum over c' containing l' of c' . Nbar_l'^c'). No plaquette contains both links (each plaquette lies in a cell), so Proposition A for Q itself gives d_l d_l' F_Q = - K_Q(Omega)(l, l') componentwise. Hence the identity, as 3 x 3 matrices. Consistency: the law of total covariance gives the same result, since given the rings the conditional covariance of the two total forces is a sum over pairs of different cells, each 0 by independence.
Side remarks checked: K_c transforms as Ad(g_tail(l)) K Ad(g_tail(l'))^T, so |K|_HS is gauge invariant; links on opposite faces share no plaquette when l >= 2; "Products (PROVED)": with a product group and product weight the Neumann data of the factors are independent, so K is block diagonal and R_c^2 adds. All correct. The "Size (ARGUED)" bullet is not in W1 and was not judged.

### Verdicts of Step 4
- Lemma ADD (with the identity and the series): CORRECT-NO-ADVANCE. It is an exact restatement: (T-per) is (CAS) of row 708, which the lane already holds as blocked-equivalent.
- Lemma CHAIN: CORRECT-NO-ADVANCE. A correct exact identity, immediate from (M1) and Proposition A; it frames (T-pin) and moves no open item ((T-pin) has no blind half and no consumer, as the note says).

## Step 5. Test (e); Lemma FLOW (4.1); Lemma PROJ (4.2); Lemma FR+ (4.3); Lemma SPLIT (4.4)

Read in full: the note L213-270. Conventions of row 1011 3.1-3.2 (read in Step 4).

### Test (e): the Jacobian formula. PASS.
The interior part of V at time s is the vector field sum over interior l and a of b_l^a(., omega_s) xi_l^a, where xi_l^a is the generator of U_l -> exp(eps e_a) U_l. Each xi_l^a has Haar divergence 0 (Haar measure is left invariant), so the Haar divergence of V is sum over l, a of xi_l^a(b_l^a), which is the note's div V. The map U -> U_eps solves a non-autonomous ODE on a compact manifold, so it is a diffeomorphism, and Liouville's formula for a time-dependent field gives d/ds log J_s(U) = (div V)(tau_s(U)). The time dependence enters only through omega_s = exp(s B) omega, which the formula allows.

### Lemma FLOW (CORRECT)
Z_c(omega_eps) = integral of exp(A(tau_eps(U, omega))) J_eps(U) dU, and A(tau_eps) - A + log J_eps = integral from 0 to eps of [(V A)(tau_s) + (div V)(tau_s)] ds = g_eps. So F_c(omega_eps) - F_c(omega) = - log E_omega[e^(g_eps)]. g' = Psi_V and g'' = V Psi_V at 0. d^2/d eps^2 of log E[e^g] at 0 is E[g''] + E[g'^2] - E[g']^2, so H_c = - E[V Psi_V] - Var(Psi_V), with equality in the bound iff Psi_V is a.s. constant; Jensen gives the last bound. With b = 0 inside, Psi_V = A' = X_c(B) and - E[V Psi_V] = - E[A''] = E sum_p beta_p w_p (t_p |delta_p|^2 + kappa_p . s_p) by Proposition A (i): this is Proposition A (ii). For B = 0: F_c is constant along the flow, so E[Psi_V] = 0 and E[Psi_V^2] = - E[V Psi_V].
The existence of a flow with Psi_V constant is ARGUED, as marked: for V = V_0 + grad phi on the interior, Psi changes by L phi with L the generator e^(-A) div(e^A grad .), elliptic and self-adjoint in L^2(e^A dU) with kernel the constants, so L phi = E[Psi_(V_0)] - Psi_(V_0) is solvable by the Fredholm alternative. Not rebuilt; not used. So "response <= cost of every flow" is PROVED, and "response = least cost" rests on that ARGUED existence (an infimum statement would follow without it only if inf Var(Psi_V) = 0, which is the same fact).

### Lemma PROJ (CORRECT; one domain precision in (iv))
(i) X(theta n) = - sum_l theta_l n_tail(l) . N_l at each fixed U; X is linear in the field values, so a U-dependent frame is allowed.
(ii), (iii) g_x U_l g_y^(-1) = exp(eps lambda_x n_x) exp(- eps lambda_y Ad(U_l) n_y) U_l, so the first-order generator is G_l = lambda_tail n_tail - lambda_head Ad(U_l) n_head (tail frame). The action is gauge invariant at each U, so X(G) = 0 whatever the dependence of n on U. (ii): lambda = indicator of z, n_z = a: - sum over tail z of a . N_l + sum over head z of (Ad(U_l) a) . N_l = 0, and (Ad(U_l) a) . N = a . Ad(U_l)^(-1) N. (iii): G_l = (d lambda)_l n_tail + lambda_head D_l n, so X((d lambda) n) = sum_l lambda_head (D_l n) . N_l; with X((d lambda) n) = - sum_z lambda_z (div j)_z, (div j)_z = sum over tail z of j_l - sum over head z of j_l, this is (div j)_z = - sum over head z of (D_l n) . N_l at every site with no pinned link.
(iv) Q(dlambda) = E[(sum_z lambda_z (div j)_z)^2] vanishes for every lambda (zero at pinned sites) iff (div j)_z = 0 a.s. at each such z: correct. Precision: "its cost form is Q(theta) = E[(sum theta_l j_l)^2]" holds for theta = 0 on the pinned links (then the cost - E[V Psi_V] of the divergence-free move equals E[Psi_V^2] by FLOW's last remark, and E[Psi_V] = 0, so it is a covariance). For theta with boundary values the cost is - E[V V A], not Q(theta). The "iff" uses only gradients of lambda that vanish at pinned sites, so the claim stands. "Divergence free (for instance tree-transported)" is a hypothesis: it needs n_tail(l) not to depend on U_l; I did not check C8 of row 1013 for the orientation convention that gives this.

### Lemma FR+ (CORRECT)
The telescoping identity holds exactly: v_x - Ad(U_p) v_x = D_(l1) v + Ad(U_1) D_(l2) v - Ad(U_1 U_2 U_3^(-1)) D_(l3) v - Ad(U_1 U_2 U_3^(-1) U_4^(-1)) D_(l4) v (I wrote out the four brackets; the signs of the last two come from v_head - Ad(U^(-1)) v_tail = - Ad(U^(-1)) D_l v). Ad(omega_p) is the rotation about s_p by twice the class angle phi, so |(1 - Ad(omega_p)) v| = 2 |sin phi| |v_perp| = 2 |s_p x v|. Then |s_p x v_x|^2 <= sum over the links of p of |D_l v|^2, the sum over the six plaquettes based at x is at least lambda_x |v_x|^2 (degree-2 homogeneity; v_x = 0 trivial), and each link lies in at most 6 plaquettes.

### Lemma SPLIT (CORRECT for its exact claims; one size sentence is ARGUED, not PROVED)
U(1): with tau = prod_i tau_i^(alpha_i), multiplicativity gives tau = sigma^(alpha_1 + ... + alpha_n) on bd; tau is closed outside the union of the P_i and equals tau_i^(alpha_i) times a field closed on P_i. The proof of PAR (i) then gives Z(sigma^(sum alpha) Om) = Z(Om) E[prod_i r_i(alpha_i)]. Jensen with alpha_i = alpha/n: rho(alpha) = E[exp(- sum v_i(alpha/n))] >= exp(- sum E v_i(alpha/n)), so V(alpha) <= sum_i E v_i(alpha/n). With v_i(alpha') <= (h/2) alpha'^2 for every sub-pin: V(alpha) <= n (h/2)(alpha/n)^2 = (h/(2n)) alpha^2, for every outer pin. Correct.
SU(2): for a plaquette whose links l_1 and l_3 both cross the cut, U_p -> g U_1 U_2 U_3^(-1) g^(-1) U_4^(-1), and tr(W g^(-1) u^(-1) g) = tr(W u^(-1)) for all W iff g commutes with u = U_4 (the tangential link joining the two tails). So the exact fractional identity needs every such u in the centraliser of n (reducible along the cut), a set of Haar measure zero. Correct.
The last sentence, "the defect per crossing plaquette is the second-order term beta theta^2 |u_perp|^2", is a size, not an identity. Ad(g^(-1)) u^(-1) - u^(-1) is of first order in theta (- 2 theta n x Im(u^(-1)) + O(theta^2)), so the change of the action has a first-order term of size beta theta |u_perp| |s_p|; the second-order classical term of Proposition A (i) is (beta/2) |delta_p|^2 t_p with |delta_p|^2 close to theta^2 |n - Ad(u) n|^2 = 4 theta^2 |s(u) x n|^2 when U_p is near 1. So the sentence holds in order of magnitude in the weak-coupling (classical) regime, with a constant near 2 for the normalisation |u_perp| = |s(u) x n|. It should carry the mark ARGUED. Nothing in the note rests on its exact form.

### Verdicts of Step 5
- Lemma FLOW (test (e) included): ADVANCE (narrow). The exact cost form of field-dependent moves with their Jacobian is new in written form and covers what check 1015 listed as not covered by Lemma WN. Blind, as the note says. Existence of the minimiser: ARGUED.
- Lemma PROJ: ADVANCE (narrow), with the domain precision of (iv). It states, for field-dependent frames, the exact condition (j conserved) under which the cost is a curl form.
- Lemma FR+: CORRECT-NO-ADVANCE (a one-line extension of Lemma FR, as the note says).
- Lemma SPLIT: ADVANCE (narrow) for the U(1) division identity with Jensen and the exact SU(2) reducibility statement; the size sentence at L269 is ARGUED, not PROVED.

## Step 6. Lemma DICH (5.1); Proposition ENG (5.5); test (f), the map of 3.4

Read in full: the note L279-362 (Section 5) and L197-203 (3.4).

### Lemma DICH (CORRECT)
Let J* be the first j >= j_0 with R_j < r_0. By the blind half R_j <= r_1 for j >= j_0, so every step j -> j + 1 with j_0 <= j < J* is random or structured (a step of both kinds is counted once). Random steps: R_(J* - 1) >= r_0 and R decreases by at least delta at each random step before it, so there are at most (r_1 - r_0)/delta random steps before step J* - 1, plus possibly step J* - 1 itself. Structured steps: E is non-decreasing, starts at least 0 and stays at most E_max, so at most E_max/eps. Hence J* - j_0 <= (r_1 - r_0)/delta + 1 + E_max/eps; the "+ 1" of the statement is exactly the last random step. If R_j >= r_0 for all j the same counts give a contradiction, so J* exists. The note's two-line proof is right; this is the bookkeeping behind its "+ 1".

### Proposition ENG (CORRECT as an implication)
Multiply (FL) by c_2 Rbar(l) >= 0 and insert in (DEC): Rbar(2l) <= Rbar(l) - c_2 Rbar(l) NA_l <= Rbar(l) - c_1 c_2 Rbar(l) min(1, 1/Rbar(l)) = Rbar(l) - c_1 c_2 min(Rbar(l), 1). Needs c_1, c_2 >= 0. The consequence in 7.3 (O1 with L = 2 follows when c_1 c_2 min(r_0, 1) >= delta) is correct, since Rbar(l) >= r_0 on the band.
Wording only: 5.5 says NA_l lies in [0, 1] and "for bare links it is the lambda_x of Lemma NAB"; but lambda_x = lambda_2 + lambda_3 <= (2/3) tr M <= 4. Use lambda_x/4 if the [0, 1] range is wanted. ENG itself does not use NA_l <= 1 (it needs c_2 NA_l <= 1 only for (DEC) to be meaningful).

### Test (f): the hand values of the map r -> 2 artanh(tanh(kappa r/2)^4). PASS.
By hand (tanh(u) = (e^(2u) - 1)/(e^(2u) + 1), 2 artanh(x) = ln((1 + x)/(1 - x))), kappa = 4:
- r = 0.3: tanh(0.6) = 2.320117/4.320117 = 0.53705; fourth power 0.083188; ln(1.083188/0.916812) = ln 1.18147 = 0.1668. Note: 0.167.
- r = 0.4: tanh(0.8) = 3.953032/5.953032 = 0.66404; fourth power 0.19443; ln(1.19443/0.80557) = ln 1.48272 = 0.3939. Note: 0.394.
- r = 0.5: tanh(1) = 0.761594; fourth power 0.33643; ln(1.33643/0.66357) = ln 2.01400 = 0.7001. Note: 0.70.
The fixed point lies between 0.402 (value 0.3993, contracts) and 0.405 (value 0.4076, expands), so "contracts below r = 0.40 and expands above" is right to two digits. Large r: tanh(2r)^4 = 1 - 8 e^(-4r) + ..., so the map is 4 r - ln 4 + o(1): "like R(2l) = 4 R(l) - log 4" is right. kappa = 1: tanh(r/2)^4 < tanh(r/2), so the map is below r for every r > 0 ("a contraction" in the sense f(r) < r; its slope tends to 1 at large r, where f(r) = r - ln 4 + o(1), so it is not a uniform Lipschitz contraction; the note's use needs only f(r) < r).
The inequality tanh(xi(Sigma_2l, D_2l)/2) <= tanh(xi(Sigma_2l, D_l)/2)^4 is Lemma PAR (iii) with four parallel copies of D_l in D_2l, which test (a) allows (squares that share an edge line are admissible sub-containers).

### Verdicts of Step 6
- Lemma DICH: CORRECT-NO-ADVANCE (counting; the note says so).
- Proposition ENG: CORRECT-NO-ADVANCE (an implication; (FL) at the cell scale and (DEC) are open).
- 3.4 hand values: correct.

## Step 7. The ARGUED items: the two cautions of 3.4, the sizes of 4.5, the reading 5.3, the last column of 3.3

Read in full: the note L183-203, L271-276, L297-304. Each item is judged as an argument: SOUND (the steps hold as heuristics and the mark ARGUED fits), OVERSTATED (a sentence claims more than its argument gives), or WRONG (a step fails). No new attack.

### 3.4, caution 1 ("the series bound is not proved at any kappa"): SOUND.
Read as "not proved with kappa uniform in l". For one l a kappa_l exists trivially (both costs are finite and positive), so uniformity is the content. Nothing in the note or in the lane files read here proves it. The reason given (a closed vortex cannot be cut into pinned patches without a thin crossing at each cut) is a correct account of why the Markov route fails: pinning the links of a cut fixes the twist there to a thin crossing whose cost is not bounded by xi(Sigma_l, D_l). It is a heuristic about that route, not a proof that no route exists. I checked one other route only to judge the scope of the caution: reflection positivity along the sheet gives (Tr S^k)^(1/k) monotone for the twisted and the untwisted transfer operators separately (Lemma A), which does not bound their ratio; so it does not supply the series bound either.

### 3.4, caution 2 (sup-pin cost not scale invariant at weak coupling): SOUND in its conclusion; the mechanism wording should be sharpened.
A boundary pin cannot keep order-one curvature per plaquette deep inside a container at weak coupling; lattice-scale structure of the pin relaxes in a boundary layer. What a pin can force is the holonomy h(s) of each transverse circle {s} x dD, with an axis n(s) that turns on the lattice scale along Sigma. The interior must carry that flux through every disc {s} x D; with a turning axis the mixed components F_(i3), F_(i4) are of size |d n|/d, so the energy per unit area of Sigma is of order beta (1/d^2 + |d n|^2), which is of order beta when |d n| is of order 1. The twisted and untwisted pins carry fluxes psi and pi - psi along the same turning axis, so their difference is of order beta |Sigma| unless psi is near pi/2. This gives the note's conclusion (cost of order beta |Sigma|, not scale invariant) by the same mass-term mechanism (a spread flux needs a common axis; Lemma FR, Lemma SPLIT), and agrees with Proposition B' of row 1011 and its check (row 1014). The fix in the note is right for this reason: across a distance l the modes of the pin with wavelength below l decay, so pins at distance at least l give |d n| of order 1/l and a scale-invariant classical cost; the moment form of PAR (iii) avoids the supremum.

### 4.5, the sizes: the orders are SOUND; one sentence is OVERSTATED.
- Constants checked: E|N_l|^2 = 18 beta xbar is 3 E[X^2] = 3 (6 beta xbar) from NAB (i) and isotropy. The gradient cost of a divergence-free frame move with theta = d lambda is E[(sum lambda_head (D_l n) . N_l)^2] by PROJ (iii)-(iv).
- The "mass term of order one per site" is the direct term of Proposition A along theta n: |delta_p(theta n)|^2 contains theta^2 |D n|^2, so beta theta^2 |D n|^2 with |D n|^2 of order 1/beta (ARGUED through E lambda_x of order 1/beta; NAB proves only 1/beta^2). Against the curl term beta theta^2/l^2 this gives l^2 of order beta: a mass of order beta^(-1/2), a correlation length of order beta^(1/2). Sound. The bullet mixes the variance form (in lambda) and the direct term (in theta) in one sentence; the conclusion uses the direct term, and the orders agree.
- Tree-transported frames: a defect on non-tree links of size |1 - Ad(hol)|^2 of order l/beta (perimeter count) gives theta^2 l per site against beta theta^2/l^2, so l^3 of order beta. Sound as a count; an area count would give l^4. The cross-check against rows 1011 7.3 and 1013 C8-C9 was not redone (C8, C9 not read here).
- Band sizes: sqrt(2.3) = 1.52, sqrt(2.6) = 1.61, so "cells of side 1 to 2" is right.
- OVERSTATED, bullet 3 (L275): "A covariant current with j conserved pathwise ... or a divisible twist ... Each exists exactly on reducible configurations only ... 4.2 and 4.4 say it for field-dependent frames, in exact form." For the divisible twist this is Lemma SPLIT (proved). For the current it is not shown: by PROJ (iii), j is conserved iff sum over head z of (D_l n) . N_l = 0 at every site, which D n = 0 (a covariantly constant frame, possible only on reducible configurations) implies but which does not imply D n = 0. Bullet 1 of the same section says so itself ("one scalar condition per site against two free angles; no such frame is constructed, none is excluded"). Repair: "a divisible twist exists exactly on reducible configurations (SPLIT); a pathwise conserved projected current exists there, and elsewhere only if a frame with D n orthogonal to the forces in this summed sense exists (OPEN)". A further point the note does not make: a frame chosen to satisfy that constraint depends on the links at its sites, so its move is in general not divergence free, and PROJ (iv) does not apply to it as stated; FLOW still does, with the div V term.
- So the verdict "route (ii) FAILS at one bare coupling" is correctly marked ARGUED, and it rests on the unexcluded aligned frame.

### 5.3, the reading "the dichotomy has no soft sign in the vortex form": SOUND, with one word too strong.
The entropy gain is Lemma PAR in the large-cost regime (n equal parallel costs xi give xi - log n + o(1)). The loss of spreading follows from Lemma SPLIT and the composition count: n fractional twists that must reach the central element -1 need total angle pi; with a coherent axis each needs pi/n (total cost of order pi^2/n), with independent axes each needs of order pi/sqrt(n) (total cost of order pi^2), so the gain 1/n is lost. The frozen Z_2 example is the solid part: it keeps PAR verbatim and shows both outcomes (cost to 0 at strong coupling; degenerate flux sectors above beta = 2.191, the lane's THM, which by the electric-magnetic duality of the sectors is the vortex cost not tending to 0). So the identities of PAR cannot fix the sign. "FAILS as a soft statement" should be read as "no sign is available from the identities that frozen Z_2 keeps; a threshold number decides"; it is not a counter-model in the target's class, and the note marks it ARGUED, which fits.

### 3.3, the last column ("what a proof must therefore use"): SOUND as candidates; the logic is one step weaker than the heading.
The valid form is: a proof whose every step holds in model M cannot prove a statement that is false in M; so it must use some property that fails in M. Each entry names one natural such property: (a) a non-zero bracket; (b) a perfect Lie algebra, [g, g] = g (su(2) + u(1) has the SU(2) bracket and no short step); (c) a connected group, so that fractional vortices exist; (d) isotropy of the 4D cell (the frozen-slice model is a stack of 3D O(4) models; I checked the identification t_(x,t;i,4) = (1/2) tr(q(x+i,t) q(x,t)^(-1)) and that layers share no integrated link; the twist cost there is beta theta^2 l per layer, against the scale-invariant beta theta^2 of the 4D curl form); (e) no matter current; (f) dimension 4; (g) for the consumer, a property of the Wilson weight. Each is a sufficient distinguishing property, not shown to be the only one: the column should read "a property false in M, for example ...". The grades of the barriers are as the table states: (a), (b) and the Z_2 case of (c) at THM or PROVED-given-THM grade; (d) given the RECALLED Froehlich-Simon-Spencer theorem; (e), (f), (g) and Q_8, 2T at BELIEF grade. No entry is wrong.

### Verdicts of Step 7
- 3.4 caution 1: SOUND. 3.4 caution 2: SOUND (mechanism wording to sharpen as above).
- 4.5: SOUND in its orders; OVERSTATED at L275 (the conserved-current half of "each exists exactly on reducible configurations only").
- 5.3: SOUND ("FAILS" means "no sign from the identities kept by frozen Z_2").
- 3.3 last column: SOUND as named candidates; the heading claims necessity of the named property, which the barrier logic does not give.

## Source check: the Mack-Petkova credit for Corollary MP (bounded; not part of W1)

Why: Corollary MP is marked ADVANCE above only because the lane held it as RECALLED; its credit decides what is new, and a published derivation by other authors is an independent check of the identity, which this same-provider check is not. Source: G. Mack and V. B. Petkova, "Sufficient condition for confinement of static quarks by a vortex condensation mechanism", Ann. Phys. 125 (1980) 117-134; the DESY 78/069 scan at www-library.desy.de/preparch/desy/postpr/1978/desy78-069.pdf, fetched into a new scratch folder under /tmp, text extracted with PyMuPDF, not committed. The extracted text of the displayed formulas is partly garbled, so I read the prose around them.
- Their (2.12)-(2.14): container partition functions Z(Lambda', U) with pinned boundary, the substitution U -> U_sigma by a centre element on the links of a cut ("a singular gauge transformation"), and new centre variables between consecutive containers. This is the substitution of Lemma PAR (i) and Corollary MP.
- Their (2.15)-(2.17) (journal p. 129): normalised distributions p_(i tau)(gamma) on the centre, proportional to Z(Lambda_(i tau), U_gamma), and "Eq. (2.16) is exact": the Wilson loop expectation as an integral with the product over containers of the Fourier transforms of p_(i tau) at the character of the loop. For the centre Z_2, p(1) = 1/(1 + r), p(-1) = r/(1 + r), so the transform at the non-trivial character is (1 - r)/(1 + r) = a_i, and the weight of the outer links is prod_i Z_i (1 + r_i). This is the exact form E[O] = Etilde[O a_1 ... a_n] of 7.4. Their (2.18) is the normalisation identity (E[prod (1 + r_i)] = 2^n in MP's form).
- Their (2.19) (p. 129): the bound by chi(1) times the product over containers of the supremum over boundary data of the transform, "derived without any approximations or extra assumptions". Their (2.20)-(2.21) (p. 130): for G = SU(2), Gamma = Z_2, the transform is (1 - Z(U_sigma)/Z(U))/(1 + Z(U_sigma)/Z(U)) with sigma = -1, then written through the change of free energy. Their (2.22) is the oddness v(tau om) = - v(om).
- Their p. 123: "one may compose thick vortices with any gamma from thin vortices with gamma near 1" (abelian, continuous G), and "the change of free energy ... comes out proportional to the length (surface) |P_i| of the vortex container, for fixed diameter d_i", with the effect of the boundary conditions expected to decrease with the diameter. The note's quotations and its use of them (SPLIT credit; 8.8's agreement with caution 2 of 3.4) are faithful.
- Their appendix contains (A.5) and the phrase "a substitute for the central limit" theorem, as SPLIT's credit says.
Conclusion: the credit lines of 3.2, 4.4, 7.4 and 8.8 are accurate on the passages read. Corollary MP's identity and bound are Mack and Petkova's (2.16), (2.19)-(2.21); the note says so. Their derivation is an independent published derivation of the same identity, so Corollary MP now stands on two derivations by different authors. Lemma PAR (ii)-(iii) (vanishing of the proper sub-products, the cumulant form, the Hoelder form) is not on the pages I read (pp. 117-130 and the appendix headings), which agrees with the note's statement.

## Step 8. Verdicts in W1's order, defects, stop rule

Provenance: Claude Opus 5.5, max effort (W1 asked for high), Mac mini worker 3, commit 54b9ac6aa, one session, no subagents, no numeric run. A check by the same provider as the author (Claude Fable 5.2), so not independent. Not an audit.

| W1 item | Statement | Verdict | Note |
|---|---|---|---|
| (i) | Lemma ADD (2.2), D(2a) = 16 D(a) - Phi(a), the series | CORRECT-NO-ADVANCE | exact restatement of (CAS) |
| (ii) | Lemma CHAIN (2.3) | CORRECT-NO-ADVANCE | immediate from (M1) and Proposition A; weights add across scales (checked) |
| (iii) | Fact 0 | CORRECT-NO-ADVANCE | |
| (iii) | Lemma PAR (i)-(iii) | ADVANCE | tests (a), (b) PASS; blind |
| (iii) | 7.2, second derivation in 2D Z_2 | CORRECT-NO-ADVANCE | consistency test; PAR (i) also checked there |
| (iv) | Corollary MP (7.4) | ADVANCE (narrow) | RECALLED -> written; equals Mack-Petkova (2.16), (2.19)-(2.21), confirmed against their text |
| (v) | Lemma FLOW (4.1) | ADVANCE (narrow) | test (e) PASS; existence of the minimiser ARGUED, as marked |
| (vi) | Lemma PROJ (4.2) | ADVANCE (narrow) | (iv) needs theta = 0 on pinned links (D3) |
| (vi) | Lemma FR+ (4.3) | CORRECT-NO-ADVANCE | |
| (vii) | Lemma SPLIT (4.4) | ADVANCE (narrow) | the size sentence at L269 is ARGUED, not PROVED (D4) |
| (viii) | Lemma NAB (5.4) (i)-(iii), all constants | ADVANCE, with repair D1 | tests (c), (d) PASS |
| (ix) | Lemma DICH (5.1) | CORRECT-NO-ADVANCE | counting |
| (ix) | Proposition ENG (5.5) | CORRECT-NO-ADVANCE | implication; (FL) at the cell scale and (DEC) open |
| test (f) | hand values of the map in 3.4 | PASS | 0.1668, 0.3939, 0.7001; fixed point near 0.403 |
| ARGUED | 3.4 cautions 1, 2 | SOUND, SOUND | caution 2: mechanism wording to sharpen |
| ARGUED | 4.5 sizes | SOUND orders; OVERSTATED at L275 (D2) | route (ii) FAILS stays ARGUED |
| ARGUED | 5.3 reading | SOUND | "FAILS" = no sign from the identities frozen Z_2 keeps |
| ARGUED | 3.3 last column | SOUND as candidates | "must use X" should read "must use a property false in M, e.g. X" (D5) |

**Stop rule.** Not triggered: no WRONG in Lemma PAR or Lemma NAB, and no WRONG anywhere else.

**Defects, ranked by what each breaks (none breaks a statement or a consumer).**
- D1 (Lemma NAB, L308). "A torus with all sides at least 3" must read "all sides equal" (or a translation- and hypercubic-invariant state): the proof uses one common plaquette mean in E[X^2] = 6 beta xbar and in the (8 xbar - 5)/3 step. Without it the proof gives only E(1 - x_q^2) >= (E x_q)^2/(2 beta). Every use in the note (4^4 run; laws in a translation-invariant state) is of the symmetric kind.
- D2 (4.5, L275). "Each exists exactly on reducible configurations only" is proved for the divisible twist (SPLIT), not for the pathwise conserved projected current; conservation is sum over head z of (D_l n) . N_l = 0, weaker than D n = 0, and bullet 1 of 4.5 itself says no aligned frame is excluded. Also, a frame chosen to meet that constraint is in general not divergence free, so PROJ (iv) does not apply to it as stated.
- D3 (PROJ (iv), L241). "Its cost form is Q(theta)" holds for theta = 0 on the pinned links; the "iff" claim uses only such theta and stands.
- D4 (SPLIT, L269). The defect size beta theta^2 |u_perp|^2 is an order of magnitude in the classical regime (the change of the action also has a first-order term of size beta theta |u_perp| |s_p|); mark it ARGUED.
- D5 (3.3, heading of the last column). Barrier logic gives "a property false in M"; the named property is a natural candidate, not shown necessary.
- D6 (test (a), L177). The paths must end at a common dual point outside D; "avoiding the other D_j" is not needed and cannot always be met (2 x 2 tiling, one exit); harmless.
- D7 (wording). L179: "tanh(V/2) multiplies" is an inequality. 5.5: NA_l in [0, 1] but lambda_x <= 4.

**What this check did not cover.** The lane inputs that Lemma ADD's U(1) paragraph rests on (I28, Proposition Delta, Theorem SH, Corollary PT1) and the run-2 inputs (TM), Lemma A were not re-checked; C8 and C9 of row 1013 were not read (the divergence-free example of PROJ (iv) and the cross-check of the l^3 count rest on them); the numeric control 6.1 was not rerun; the test table 6.2, the filter corrections 8.3 and the "Size (ARGUED)" bullet of 2.3 are not in W1 and were not judged; the Mack-Petkova check read pp. 117-130 and the appendix in extracted text only.

- 21:43Z (`date -u`, printed when this section was written): Step 8 done.

RESULT: Row 1022, check of row 1018's work item W1 by Claude Opus 5.5 max (same provider as the writer, Claude Fable 5.2, so not independent): no WRONG; stop rule not triggered; tests (a)-(f) PASS. ADVANCE: Lemma PAR (i)-(iii); Lemma NAB (i)-(iii) with every constant, after repair D1 (the torus must have all sides equal, since the proof uses one common plaquette mean); Corollary MP (narrow: it is Mack and Petkova's (2.16) and (2.19)-(2.21), which I confirmed against their text, so MP now has two derivations by different authors); Lemmas FLOW, PROJ (with the domain precision D3) and SPLIT (narrow; its defect-size sentence is ARGUED, D4). CORRECT-NO-ADVANCE: Lemma ADD with D(2a) = 16 D(a) - Phi(a) and the series, Lemma CHAIN, Fact 0, the 2D Z_2 derivation 7.2, Lemma FR+, Lemma DICH, Proposition ENG. ARGUED items: both cautions of 3.4, the reading 5.3 and the last column of 3.3 are SOUND (the column names candidate properties, not necessary ones, D5); the sizes of 4.5 are SOUND in order, but L275 overstates that a pathwise conserved projected current exists only on reducible configurations (D2), so route (ii)'s FAILS stays ARGUED and rests on the unexcluded aligned frame. Still OPEN, as the note says: O1 ((FL) at the cell scale and (DEC)), O2 ((SER) and (SPR) with kappa phi < 1), the frame with D n orthogonal to the forces, E lambda_x of order 1/beta; (W), (CAS) and the seed are not moved.
