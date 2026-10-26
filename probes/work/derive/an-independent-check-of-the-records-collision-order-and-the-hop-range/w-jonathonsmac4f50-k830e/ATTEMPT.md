# Independent check: records' collision order and the hop range (blocks 152 and 154)

Task `J:derive:an-independent-check-of-the-records-collision-order-and-the-hop-range:a1`. Worker: Claude Sonnet 5.5, same family as the supervisor, so this is not an other-family referee. Unrefereed.

Plain language first. The two notes claim: (1) two records cannot scatter into an upper/lower-band pair, so near the corners the pair's momentum changes only at third order; (2) however the walker's energy is "placed" on the lattice, the total momentum the member sees is the same (energy times velocity); (3) the hop range R caps how high the order can go (N at most R+2), and neighbour hops give 3. I re-derived each with my own arguments and ran exact checks. Every landed step I tested holds. I found no error. I found three exact sharpenings and two scope remarks (section 4).

I read `docs/MINIMAL_AXIOMS_2026-06-29.md` (lines 1-233, in full) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (lines 1-130, in full) before choosing premises. No registered primitive is used here.

## 0. Sources read (landed text controls)

`origin/main` at 3e1a2dd2531590dabf85bee8db56175ba9b96e90 (the `main_wt` checkout at a77a3449 has byte-identical copies of both notes, same sha256).
- Block 152, landed: `docs/ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_A_COLLISION_CHANGES_THE_RECORDS_TWO_STEP_MOMENTUM_ONLY_AT_THIRD_ORDER_IN_THEIR_OFFSETS_FROM_THE_CONES_BOUNDED_THEOREM_NOTE_2026-09-26.md`, T1 at lines 48-56, T3(b) line 70.
- Block 154, landed: `docs/ADMISSIBILITY_RULE_THE_ORDER_AT_WHICH_RECORDS_COLLISIONS_BREAK_THE_BOOKS_IS_SET_BY_THEIR_HOPS_NO_PLACEMENT_OF_THE_WALKERS_ENERGY_CHANGES_IT_BOUNDED_THEOREM_NOTE_2026-09-26.md`, T1 lines 47-60, T3 lines 68-84.
- Block 150, landed: `docs/ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_A_RELABELLING_FORCES_THE_WHOLE_MOMENTUM_CONSTRAINT_AND_NO_POSITIVE_INERTIA_CAN_BE_ADDED_TO_THE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-25.md`, T5(a) line 128, block 112's shift line 70.
- Branch snapshot of block 154 (head b484be77...) differs from landed 154 in the status line, T1 orientation sentence (line 60), T2 scope wording and the all-odd-R proof of T3(d); the landed text was used. Hashes in `RECOVERY_STATUS.json`.
- Prior-art search: no attempt directory for this task slug under `probes/work/derive/`; no open PR mentions blocks 152 or 154 collision/hop claims (gh search returned none). Nothing here duplicates a landed note.

## 1. The exact statement attempted

(S1) Block 152 T1(d): for two records in band pair (+,+) with pair energy E, at total wave vector K, the only open outgoing band pair is (+,+) (off a null set of incoming states), and E < sqrt(2)/2 keeps every offset of every component below pi/4.
(S2) Block 154 T1(a)-(c): for any finite-range energy placement e_x with sum H, and any finite-range momentum placement P whose walker bracket matches block 112's shift when one lapse is uniform: the totals agree, P(k,k) = J(k,k), and the band-diagonal of J_j(k,k) is E_b times the band velocity; for block 54's walk it is -sin k_j cos k_j in both bands (in the note's sign convention).
(S3) Block 154 T3(b)-(d): for h = sum_a sigma_a f(k_a), f an odd real trigonometric polynomial of degree R with one light cone, the first order N at which f f'(A+delta) - delta is nonzero satisfies N <= R+2; R = 1, 2 force f = +-sin k and N = 3; odd R reaches N = R+2 by one f up to sign; largest N for R = 1..6.

Premises (supplied, not axioms): block 54's walk h(k) = sum_a sigma_a sin k_a with Pauli sigma_a; block 78's one record per site; block 112's shift and block 150 T5(a)'s match with a uniform lapse (ASSUMED here: I take the match as the stated requirement on placement pairs, as block 154 does); the free-pair band structure E = s1 eps(k1) + s2 eps(K - k1). Axioms used: none beyond "no site privileged" style supplied structure; nothing adopted.

## 2. Steps

Labels: PROVED (argument given in full), CHECKED (executed exactly by `check.py`), ASSUMED, READING.

### Part 1: block 152 T1(d), the channel closure

1.1 PROVED, CHECKED (A1-A3). Write a, b for two wave vectors, s_i = sin a_i, c_i = cos a_i, t_i = sin b_i, w_i = cos b_i, u_i = s_i w_i, v_i = c_i t_i, W = sum_i s_i^2 t_i^2 >= 0. Then sin(a_i+b_i) = u_i + v_i and, modulo sin^2+cos^2 = 1 on each component (Groebner reduction in d = 1, 2, 3 in check.py):
 eps(a+b)^2 = eps(a)^2 + eps(b)^2 - 2W + 2 u.v, |u|^2 = eps(a)^2 - W, |v|^2 = eps(b)^2 - W.
So (eps(a)+eps(b))^2 - eps(a+b)^2 = 2W + 2( eps(a) eps(b) - u.v ) >= 0, because eps(a) eps(b) >= |u||v| >= u.v. This is subadditivity for all a, b, in full (the landed text states it and the runner samples it).

1.2 PROVED, CHECKED (A2, A3). Equality eps(a+b) = eps(a)+eps(b) holds iff eps(a) eps(b) = 0 (one of the two vectors is a corner). Proof: equality needs W = 0, so sin a_i sin b_i = 0 for every i; then u_i v_i = 0 for every i, so u.v = 0, and equality needs eps(a) eps(b) = 0. The converse is immediate. Exact grid: 331,776 pairs in d = 2 (4,592 equalities, all with a corner) and 60,000 random pairs in d = 3. The landed text's necessary condition (cos^2 k_{2,i} = 1 wherever sin k_{1,i} != 0) also gives a null set: at fixed K each component of k_1 lies in {0,pi} or K_i + {0,pi}, finitely many points.

1.3 PROVED, CHECKED (A4). Take an incoming (+,+) pair at K, so E = eps(k_1)+eps(k_2) >= eps(K), equality only if a record is at a corner (1.2). A (+,-) outgoing pair at the same K (records k_1', k_2' = K - k_1') has energy eps(k_1') - eps(k_2') <= eps(K) (subadditivity applied to k_1' = K + (-k_2') and eps(-x) = eps(x)). So the outgoing energy is strictly below E off the null set; (-,+) is the same with the roles swapped; (-,-) has negative energy. Hence only (+,+) is open. This closure does not use E < sqrt(2)/2 (see 4.1). Checked on a d = 2 grid of 331,776 (K, k_1) cases.

1.4 PROVED. If both records are in the upper band, eps(k_i) <= E; and eps(k) >= |sin d_a| for the offset d_a of component a from the nearest multiple of pi, with |d_a| in [0, pi/2]; sin is increasing there and sin(pi/4)^2 = 1/2. So E < sqrt(2)/2 gives |d_a| < pi/4 for every component of every record, before and after. CHECKED (A7) at the grid points.

1.5 PROVED, CHECKED (A5, A6). Crystal momentum: per component, corners A, B, A', B' in {0,pi}, offsets with |delta| < pi/4, A+B+d1+d2 = A'+B'+d1'+d2' mod 2pi. The corner difference is 0 or pi mod 2pi; the offset-sum difference D lies in (-pi, pi); so D = 0. Checked over all corner channels on a grid. The strictness is sharp: at |delta| = pi/4 exactly, corner pi with offsets (pi/4, pi/4) to corner 0 with offsets (-pi/4, -pi/4) is crystal-momentum allowed with the offset sum changed (A6).

1.6 ASSUMED. That outgoing states of the interacting (hard-core) pair at energy E are the free-pair continuum states at E (no outgoing channel other than those counted); that the pair's momentum read-out once the records are apart is the sum of the one-body diagonals. Both are used by blocks 152 and 154 as landed. Not tested here.

Result for S1: confirmed, with the sharper equality set in 1.2 and closure at every E in 1.3.

### Part 2: block 154 T1(a)-(c), every placement gives E_b v_b at zero transfer

2.1 ASSUMED (premise). Block 150 T5(a) (landed line 128): with M = 1, the walker's bracket X = -i[H, H_N] equals -Y with Y the walker part of G[xi(N,1)], xi(N,1)_j = N_{x+e_j} - N_x (K/(4 alpha) = 1; line 70). I did not re-derive block 150 or 112.

2.2 CHECKED (B3), PROVED. Continuity sign. With i[H, e_x] = -(J_{x,j} - J_{x-e_j,j}) summed over j, summation by parts gives i[H, sum_x M_x e_x] = sum_{x,j} (M_{x+e_j} - M_x) J_{x,j}. Verified exactly in position space on a ring of 6 sites with a generic placement. Then X = -sum_{x,j}(N_{x+e_j} - N_x) J_{x,j}, and X = -Y with Y = sum (N_{x+e_j} - N_x) P_{x,j} gives that D = J - P satisfies sum_{x,j}(N_{x+e_j} - N_x) D_{x,j} = 0 for every N: D is divergence-free. So the totals agree, with this orientation, P = J (the landed orientation remark, line 60, covers the overall sign).

2.3 PROVED, CHECKED (B4). A divergence-free translation-covariant family has D_j(k,k) = 0. In symbols sum_j (1 - z_j) D_j(k+q,k) = 0, z_j = exp(-i q_j), for all q. Put q = t e_j, others zero: (1 - z_j) D_j(k + t e_j, k) = 0 for t != 0, so D_j vanishes along the axis, and by continuity (finite range means trigonometric polynomial) D_j(k,k) = 0.

2.4 PROVED, CHECKED (B1). The continuity symbol is i( h(k+q) e(k+q,k) - e(k+q,k) h(k) ) = - sum_j (1 - z_j) J_j(k+q,k). Its first order in q_j, with e(k,k) = h(k): J_j(k,k) = -( d_j h . h + [h, d_{q_j} e] ). This equals the landed formula (b). Independent exact check: 60 (placement, axis) cases with random exact finite-range placements (hermitian and non-hermitian; d = 1, 2, 3; energy placements with sum H and number-density placements with sum 1), each time constructing one valid J by telescoping and exact division of Q by (1 - z_a), not by differentiating, and comparing J_j(k,k).

2.5 PROVED, CHECKED (B1, B2). Band-diagonals without eigenvectors. With Pi_b = (1 + b h/eps)/2, diag_b(J) = tr(J)/2 + b tr(hJ)/(2 eps). For the energy current: tr J = -tr(d_j h h) - tr[h,X] = -2 sin k_j cos k_j (tr(sigma_j h) = 2 sin k_j) and tr(hJ) = -tr(h^2 d_j h) - tr(h[h,X]) = 0 (tr sigma_j = 0, cyclicity), for an arbitrary 2x2 X = d_{q_j} e. So diag_+ = diag_- = -sin k_j cos k_j for every placement. For the number density: tr J = 0, tr(hJ) = -2 sin k_j cos k_j, so the velocity is -d_j E_b = -b sin k_j cos k_j / eps, and (energy b eps) x (velocity) = -sin k_j cos k_j. This reproduces the landed T1(c) and does not use Hellmann-Feynman or non-degeneracy; as a trace statement it holds also at eps = 0 where the band projectors do not exist (the landed text's punctured-neighbourhood remark).

Result for S2: confirmed for all finite-range placements (hermitian or not), given the premise 2.1.

### Part 3: block 154 T3(b)-(d), the hop range

Setup. f(k) = sum_{m=1}^R a_m sin(m k). f(pi+delta) = -o(delta) + e(delta), o the odd-harmonic part and e the even-harmonic part (both odd functions of delta). f f' = (1/2)(f^2)'.

3.1 PROVED. f f'(A+delta) - delta = O(delta^N) at both corners iff (o+e)^2 = delta^2 + O(delta^{N+1}) and (-o+e)^2 = delta^2 + O(delta^{N+1}), i.e. 4oe = O(delta^{N+1}) and o^2 + e^2 = delta^2 + O(delta^{N+1}). N is odd (f f' - delta is odd), N >= 3 because |f'(0)| = |f'(pi)| = 1 gives o'e' = 0 (the two conditions (o'+e')^2 = (-o'+e')^2 = 1 give 4 o'e' = 0).

3.2 PROVED, CHECKED (C1, C4). Case A, o'(0) != 0 (so e'(0) = 0 and o' = +-1). Then e = O(delta^N), o = +-delta + O(delta^N). Write o = sum_{j<m} a_j sin((2j+1)delta), degree 2m-1 <= R. The delta^{2l+1} coefficient is (-1)^l/(2l+1)! sum_j b_j x_j^l, b_j = (2j+1) a_j, x_j = (2j+1)^2. Conditions: sum b_j = +-1 and sum b_j x_j^l = 0 for 1 <= l <= (N-3)/2. If (N-3)/2 >= m, the equations l = 1..m say sum_j (b_j x_j) x_j^{l-1} = 0, a Vandermonde system with distinct positive nodes: det = prod_{i<j}(x_j - x_i) != 0 (verified exactly for m = 1..10 by `C1`, and true for all m), so b = 0, contradicting sum b_j = +-1. Hence N <= 2m+1 <= R+2. For odd R = 2m-1 and N = R+2 = 2m+1 there are m equations (sum b_j = +-1 and l = 1..m-1) in m unknowns, square Vandermonde: the odd part is unique up to sign. The even part e is a sine polynomial of degree <= 2m-2 with m-1 terms, vanishing to order 2m+1, so its coefficients obey a square homogeneous Vandermonde system with nodes (2j)^2: e = 0. CHECKED for m = 1..6 (`C4`): the solved odd stencil equals f_m, and adding the l = m equation is inconsistent.

3.3 PROVED, CHECKED (C2, C3, C7). Case B, o'(0) = 0 (so e'(0) = +-1 and o = O(delta^N)). If o is not identically zero, the lowest Taylor order of a nonzero odd-harmonic sine polynomial of degree d_o is at most d_o (same Vandermonde argument), so N <= lowest order of o <= R. If o is identically zero, f = e is a pure even-harmonic walk; the identical Vandermonde argument with nodes (2j)^2, j <= floor(R/2), gives N <= 2 floor(R/2) + 1 <= R+1. The light cone is used by the landed text to rule this case out (f = e vanishes at pi/2); my argument shows the bound N <= R+2 does not need that exclusion (see 4.2).

3.4 CHECKED (C2). No light cone imposed, all complex solutions. For R = 1..6, the Groebner basis (grevlex, over Q) of the order-N system "f f'(A+delta) = delta + O(delta^N) at A = 0, pi" is {1} at N = 5, 5, 7, 7, 9, 9 and is not {1} at N = 3, 3, 5, 5, 7, 7. So the largest N is 3, 3, 5, 5, 7, 7 (R = 6 is new relative to the runner's R <= 5). The quotient dimension at the largest N is 2, 4, 2, 4, 2, 4. `C3` exhibits exactly that many distinct solutions: +-f_m for every R (m = ceil(R/2)), and for even R also +-(1/2)F(2k), F the degree-R/2 sine polynomial matching u to order R; these are therefore all solutions, each with multiplicity one. The even-harmonic ones vanish at k = pi/2.

3.5 PROVED, CHECKED (C5, C6). The attaining family. f_m(k) = sin k sum_{j<m} [binom(2j,j)/(4^j (2j+1))] sin^{2j} k is the m-term truncation of arcsin(sin k), which equals k near 0. So f_m(delta) = delta - a_m sin^{2m+1}(delta) - ... = delta - a_m delta^{2m+1} + O(delta^{2m+3}), a_m = binom(2m,m)/(4^m (2m+1)) > 0. Since f_m(pi+delta) = -f_m(delta), the corner at pi gives the same series. f_m^2 = delta^2 - 2 a_m delta^{2m+2} + O(delta^{2m+4}), so f_m f_m' = delta - (2m+2) a_m delta^{2m+1} + O(delta^{2m+3}) (m = 2: 9/20). Checked exactly for m = 1..6. Light cone: f_m = sin k times a polynomial in sin^2 k with positive coefficients, so zeros only at 0 and pi, f_m'(0) = 1, f_m'(pi) = -1. Speed bound for every m: f_m' = cos k T(sin^2 k) with T(y) = sum_{j<m} binom(2j,j)(y/4)^j, and T(y) <= (1-y)^{-1/2} termwise (positive coefficients), so f_m'^2 = (1-y) T(y)^2 <= 1; `C5` checks that 1 - (1-y)T(y)^2 has nonnegative coefficients for m = 1..6. The R = 3 and R = 5 closed forms quoted by the note are checked (`C6`).

3.6 CHECKED (C7). Where the light cone does work: at R = 2, N = 3 the complex solutions are +-sin k and +-(1/2) sin 2k. The latter has f'(0) = 1, f'(pi) = 1 but vanishes at pi/2, and f f' = delta - (8/3) delta^3, not sin(delta) cos(delta) = delta - (2/3) delta^3. So the light cone is needed for T3(c) (f = +-sin k) and for the uniqueness statement, not for the bound.

3.7 CHECKED (C8). The sums on block 152's family: cubic p^3/4 + 3 p x^2 takes 79/16 and 1/4 at the two shell points (E = 5/2, p = 1: (x,y) = (5/4, 0) and (0, sqrt(21)/4), both on the shell |delta_1|+|delta_2| = 5/2); fifth-order p^5/16 + (5/2) p^3 x^2 + 5 p x^4 takes 4141/256 and 1/16 there, not constant.

Result for S3: confirmed; the largest N for R = 1..6 is 3, 3, 5, 5, 7, 7.

## 3. First unresolved or failing step

None of the requested steps fails. The first step this check leaves unproved is 1.6/2.1: that the pair's momentum read-out is the sum of one-body diagonals once the records are apart, and that block 150 T5(a)'s match is the right requirement on placement pairs. Both are premises of the landed notes, not tested here.

## 4. What is new, and scope remarks

New relative to the sources (not retrieval, not old numerics):
4.1 Closure of the (+,-) channel holds at every pair energy E >= 0 (off the null set), not only for E < sqrt(2)/2; the threshold sqrt(2)/2 is needed only for the offset bound (1.3, 1.4). Equality in subadditivity is exactly "a record at a corner" (1.2), with an all-points proof by an exact polynomial identity (1.1).
4.2 The bound N <= R+2 does not use the light cone; the odd-R extremal solution is unique up to sign without it; the light cone selects +-sin k at R = 2 and removes the even-harmonic walks (which have extra zeros) (3.3, 3.4, 3.6). The largest N for R = 6 is 7, and the complete complex solution sets for R = 1..6 are exhibited (3.4).
4.3 The band-diagonal statement of block 154 T1(c) follows from two trace identities valid for an arbitrary placement (2.5), and was checked against explicit exact constructions of J for generic hermitian and non-hermitian placements (2.4). |f_m'| <= 1 holds for every m (3.5), not only m = 2.
4.4 Strictness of "below pi/4" in block 152 T1(b) is sharp (1.5).

Scope remarks (not errors):
- Block 154 T3(b) states N <= R+2; for even R the true bound is R+1 (3.2, 3.4: largest N 3, 5, 7 for R = 2, 4, 6).
- The landed 154 T1(a) fixes P = J only up to the overall orientation convention (landed line 60); I derived the orientation from block 150's X = -Y (2.2) and it is consistent. A sign flip changes no order.
- Not covered here: block 152 T2-T4 (rank-one T-matrix, regular-threshold hypotheses), block 154 T4 for added interactions, coin-mixing hops (f matrix valued), members pairing on longer bonds.

## 5. What would finish a stronger result

(i) An other-family referee of 1.1-1.5, 2.2-2.5 and 3.2-3.5 line by line (all are short).
(ii) Re-derive block 150 T5(a) and block 112's shift independently (2.1) so the premise becomes a proved step.
(iii) For T3, drop the form h = sum sigma_a f(k_a): a coin-mixing hop with a matrix-valued symbol needs its own order-versus-range argument.

## 6. Files

- `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/attempts/an-independent-check-of-the-records-collision-order-and-the-hop-range/check.py` (19 checks, about 140 s, one process)
- `.../RECOVERY_STATUS.json`
- `.../ATTEMPT.md`
