# Check of library/gap-mech-k2-step2-astra62.md (FINISH row 1555)

Checker: Claude (Opus 5.5). Target: row 1552 (gpt-6.2-astra max). Status: complete.

## Plan
1. Read GOAL.md, FINISH.md Rules and Working efficiently.
2. Read library/gap-k2-tool-design-fable.md section 4.3 (K2-STEP), check 1551, the target note.
3. Check positive claims in order: circle; soft kernel on circle; radius/wrap cost and budgets (9); one-link-test witness; conclusion and extensivity.
4. Check selectivity and purity section against check 1551.
5. Novelty relative to rows 1544, 1549 and their checks.
6. RESULT line.

## Steps

Step 1 done: GOAL.md (computation-as-proof rule), FINISH Rules and Working efficiently read.
Step 2 done: read the target note in full (174 lines), check 1551 in full, row 1468 sections 3.1-4.3.
Steps 3-6 done: sections 1-7 below.
Also read: check 1527 (iii) (library/gap-agy-seed-approaches-neon-check-astra62.md lines 59-84), row 1544 statements A and B and its zero-free/Fourier method (library/gap-mech-k2-solve-astra62.md lines 9-44), check 1548 RESULT, row 1549 Theorem (3) and its class (library/gap-mech-k2-step-astra62.md lines 83-169).

Guide run (python3 -I, floats, not a proof step, no lattice): det[v_0,v_1,v_2] - (3 sqrt3/8) sin 3t below 2e-15 on 200 angles; 8e(9/2)^6 = 180576 < 24*5^6 = 375000 < 25^4 = 390625; a_12^2/8 = 1.56e-64 > 1/(72 (2^24 24!)^2) = 1.28e-64; I_24(1)/I_0(1) = 7.7e-32 >= a_12 = 3.5e-32; (9/2)^72/72! / a_12 = 5e-26 <= 1/2. All agree with the hand checks below.

Provenance: Claude Opus 5.5, subagent, lane checkout as found 2026-11-25 (note's working tree 325e79f87 as it states); not an audit. Hand check; no Lean.

## 1. Circle of fields with constant plaquette traces, (1)-(3) -- HOLDS

- J_y^h in [0,1]: Hadamard with |E_i| <= 1; conjugation at y rotates the three columns by one SO(3) element. HOLDS. E_B(0) = 1. HOLDS.
- v_i(t) are pure unit quaternions (h_i orthogonal to k, both unit). HOLDS.
- One mark per plaquette. Marks of a patch sit at x+e_i: pairwise lattice distance 2, never in one plaquette. Across patches in a slab: grid gaps >= 4 (also the wrap gap L_i - 4(floor(L_i/4)-1) >= 4), and e_j - e_i moves each coordinate by at most 1, so cyclic distance >= 3 in some coordinate. Marks in consecutive slabs are collinear time links. So every plaquette holonomy is 1 or a mark up to inversion, trace 1 or 0, for all angles. HOLDS.
- Star count. Spatial distinguished axis: one purely spatial plaquette, holonomy 1, J = 0. Time distinguished, central link marked: the neighbours x+e_k+s_i e_i are unmarked (e_k + s_i e_i is never a unit vector e_j, j != k, and is 0 or 2e_k for i = k), so the three columns are all +-Im(mark): parallel, J = 0. Central link unmarked: need three marked neighbours, all in one patch (neighbours of y differ by <= 2 per coordinate); the common neighbours of x+e_1, x+e_2 are x, x+e_1+e_2, only x also neighbours x+e_3, so y = x (spatially) with all s_i = +1. Base at the slab bottom with time sign +, or at the slab top with sign -: holonomies -v_i and v_i, same squared volume. The 3! orders of the transverse axes permute columns. Count 2*3!/384 = 1/32. HOLDS.
- Determinant. Multilinear expansion in v_i = a_i h_i + b_i k: only one-k terms survive; det[h_0,h_1,k] = det[h_1,h_2,k] = det[h_2,h_0,k] = sin(2pi/3) = sqrt3/2 (cyclic reordering of det[k,h_1,h_2], det[h_0,k,h_2]). So det = (sqrt3/2) sum_i b_i prod_{j!=i} a_j = -(sqrt3/2) d/dt prod cos(t+phi_i). With prod = cos(3t)/4 this is (3 sqrt3/8) sin 3t, alpha = 27/64. HOLDS (guide agrees).
- (3): every nonzero star belongs to one patch and gives (B(w(t_j)) - B(0))/32. HOLDS.

## 2. What the soft kernel allows, (4), (5), (6) and the tuning restriction -- HOLDS

- D(V) = int exp(kappa sum_e M_e.V_e) dxi: Re(M V^{-1}) = M.V for unit V; normalizers and the fine density absorbed into xi. HOLDS (as in check 1551 section 1).
- (4). On a marked link the exponent is kappa[(M.h_i) cos(t+phi_i) + (M.k) sin(t+phi_i)], a first harmonic with coefficient length <= kappa|M| <= kappa; three add to radius <= 3 kappa <= L. All other factors (fixed links, earlier angles, later angles integrated) are a positive measure in W independent of t_j. Pushforward to (u,v) gives pi. HOLDS.
- (5). f(z) restricts to u cos t + v sin t on |z| = 1; |f(z)| <= exp(L(|z|+|z|^{-1})/2). Equal densities give f(e^{it})/f(1) = E_B(w(t)) since w(0) = 0. Invariance under t -> t + pi/3 and t -> -t extends to C* by the identity theorem. sin^2 3t = (2 - zeta - zeta^{-1})/4 with zeta = z^6, so zeta + zeta^{-1} = 2 - 4w/alpha; root choices differ by the two proved symmetries; branch points only at w = 0, alpha, where F is bounded, so removable. |zeta| >= 1 gives |zeta| <= 3 + 4|w|/alpha, |z|^{-1} <= 1, f(1) >= e^{-L}, hence (5). HOLDS.
- (6). E = D_0^p near [0,1], p = -lambda/32. Meromorphic identity E'/E = p D_0'/D_0; residues give that E vanishes only at zeros of D_0, and p m in Z_{>=0}. log|E| - p log|D_0| locally constant on a connected set, zero at 0. p > 0: |E| = |D_0|^p contradicts (6) against the O(R^{1/6}) bound (5). p < 0: D_0 zero-free, then E zero-free; E = e^g, mean Re g = 0 on |w| = R, mean |Re g| <= 2U(R), |g_n| R^n/2 <= 2U(R), U = O(R^{1/6}), so g = 0, then D_0 constant. HOLDS.
- Tuning: a nonconstant entire E_{lambda_0 b} obeying (5) has a zero of order m >= 1; a second amplitude needs m lambda/lambda_0 in Z_{>=0}. HOLDS.
- cosh(c sqrt w) and the compact mixtures: entire, D_0(0) = 1, positive, log D_0(R) >= c sqrt R - log 2 (resp. a_0 sqrt R + log(m/2)), so (6) holds; excluded for both signs of lambda. HOLDS. The auxiliary-variable sentence is informal: one symmetric bounded variable per oriented star coupled to det gives D_0(J) per star, i.e. B = -384 log D_0 in (1); this is a nonzero multiple, so it is excluded. HOLDS with that reading.

## 3. Cost in radius and wrap error, (7), (8), (9) and the extensive error -- HOLDS; (9) HOLDS AFTER CLARIFICATION

- (7): compactness of disk probabilities, uniform convergence of f_pi (pointwise + derivative bound L e^L), e^{-L} <= f_pi <= e^L, continuity of KL, strict positivity for unequal continuous positive densities. Compact parameter sets give a common minimum; the remark on lambda, c -> 0 is right (q_{delta_0} = 1, p_B -> 1). HOLDS.
- (8): P = prod p_B(t_j) is the normalization of exp(-A_B) by (3). Chain rule: KL(P||Q) = sum_j E_P KL(p_B || q_{pi_j}) >= M d_{L,B} by (4). Upper side: KL(P||Q) = log E_P e^Y - E_P Y <= osc Y with Y = log D + A_B; e V_Lambda and S_tr are constant on the circle; osc of R over the circle <= 3 M Gamma (3M single-link changes, each <= Gamma); endpoint errors <= 2 eta. HOLDS.
- Gamma <= C rho: #(plaquettes inside X) <= 6m/4, each term <= 2, so E_X <= 3m; |R_X| <= a_X e^{-rm}(1 + 3 theta x' m) with sum_{X containing e} a_X <= rho; osc <= 2 sup. C finite. Periodized terms of diameter < s/2 lift injectively through a fixed copy of the bond. HOLDS.
- (9): if an image lay in the output tube centred at S_tr + A_B, (8) with eta = eta_{k+1} <= eta_k + V e^{-rs/8} and Gamma <= C rho_{k+1} contradicts (9). L = 3 kappa_* covers every kappa <= kappa_*. The input tube enters only through nonemptiness; the bound is input-independent. HOLDS.
  Clarification (not a change of content): (9) must be applied on an untwisted member with all periods > 20 (the patch geometry and the survival of the ten-bond star under the diameter cut s/2). On row 1468's tori the time sides are v_k = 2^{N-k} v_E, v_E >= 4, so late band levels may have no such member; the exclusion then uses an earlier level.
- Extensive error: R = 0 gives eta >= M d/2; M = V/64 at spatial periods divisible by four (eta >= dV/128); floor(L/4) >= (L-3)/4 >= L/5 for L >= 15 (eta >= dV/250). Large-torus limit at fixed aspect with eta_k = o(V): 2 eta_k/M -> 0 and 2V e^{-rs/8}/M <= 128 e^{-rs/8} -> 0. HOLDS.
  Size remark: with the explicit bound (11), d is about 1.3e-64, so (9) bites only for M of order 1e64 or more and r s/8 above about 150. The note says the fixed-side comparison with the (C5) margin is not made; I agree. The exclusion is a large-volume statement.

## 4. Finite real witness, (10), (11), and the passing example 1 + eps w -- HOLDS

- B = -32 log cosh(c sqrt w): E_B = cosh(c sqrt w), on the circle cosh(A sin 3t), A = c sqrt alpha, normalizer I_0(A). Row 1549's one-link odds cosh(c sin t) from atoms (0, +-c), (0,0), radius c <= kappa: HOLDS (check 1551 agrees).
- I_k series, phase rotation of atoms, (k+l)! >= k! l! gives I_k <= (r/2)^k I_0/k!, so |q_pi^(k)| <= (L/2)^k/k!. p_B^(6n) = (-1)^n I_{2n}(A)/I_0(A) (even harmonics survive the cosh average with phase cos(k pi/2)). |p_B^(6n)| >= a_n by the first term and I_0 <= e^A. (6n)!/(2n)! >= (2n+1)^{4n}; with (10) the ratio is <= e^A (2e^A)^{-n} <= 1/2. HOLDS.
- Test function f = (-1)^n cos 6nt, |f| <= 1: Lambda'' <= 1, Donsker-Varadhan gives KL >= Delta^2/2 >= a_n^2/8 for every pi. HOLDS.
- Example: kappa in [2,3], L = 9, c = 8/(3 sqrt3) <= 2, A = 1; 8e(9/2)^6 < 24*5^6 < 25^4 with e < 3; a_12^2/8 = e^{-2}/(8(2^24 24!)^2) > 1/(72(2^24 24!)^2) since 8e^2 < 72. HOLDS (guide agrees). Hand arithmetic; no numerical proof input, as stated.
- Passing example: E_B = 1 + eps w gives 1 - delta cos 6t with delta = (eps alpha/2)/(1 + eps alpha/2); atoms at radius r with angular density 1 - [delta I_0/I_6] cos 6 phi give f = I_0(r)(1 - delta cos 6t) by convolution. Positive for small eps. HOLDS. Consistent with (6): lambda = -32, p = 1, E = D_0 polynomial.

## 5. Conclusion and extensivity -- HOLDS as stated in the note's RESULT

The class "arbitrary elementary-plaquette-trace interaction + hypercubic lambda log cosh(c sqrt J), lambda != 0, c > 0, kappa <= kappa_*" cannot be an output centre of (K2-STEP) whenever (9) holds on an untwisted member with all periods > 20; with no other colour dependence the log error is at least d V/250. The note's RESULT carries the qualifier "with the radius and wrap budgets in (9)". Read without that qualifier ("cannot satisfy (K2-STEP)" on the actual sixteen tori at fixed side) it would overclaim: no comparison of rho_bar, eta_k and e^{-rs/8} with d on fixed tori is made. A check of the sense of the result: the growth reason is visible directly, |f(z)| <= exp(L(|z|+1/|z|)/2) while cosh(A (z^3 - z^{-3})/(2i)) grows like exp(A|z|^3/2).

## 6. Selectivity, purity and the open estimate

- U(1) 4D and SU(2) 5D: rank <= 1 (scalars) and four vectors in R^3; every full electric Gram determinant is zero for every field, before orientation averaging; A_B = 0, target density constant, realized by pi = delta_0 (f = 1). HOLDS.
- "The rank of the three actual colour vectors in (2) is precisely where the proof distinguishes four-dimensional SU(2)": HOLDS AFTER CORRECTION. As check 1551 found, the vanishing is algebraic: it holds exactly when dim(Lie algebra) < d - 1 and tracks nothing dynamical. Gapped 3D compact U(1) and strong-coupling 4D U(1), 5D SU(2) also have zero Gram, and 3D SU(2) or 4D SU(3) do not. Corrected sentence: "The proof uses that the three colour vectors in (2) have full rank, which is possible only when dim(Lie algebra) >= d - 1; this separates 4D SU(2) from 4D U(1) and 5D SU(2) algebraically and is not a gap-tracking selectivity." The note's next two sentences ("uses the uniform realization clause"; "no sign for the typical-field stiffness") already disclaim more, so nothing downstream breaks.
- Purity blindness: multiplying the time-u inputs by c_u and the time-2u inputs by c_2u multiplies P by c_2u/c_u^2 and leaves every normalized angle conditional unchanged. HOLDS (in the class of positive inputs, as stated; one common site constant in the tube would not absorb two different constants, and the note does not claim it does).
- Wilson separation at one box: beta -> 0, bounded convergence, all sixteen normalized masses -> 1, P -> 1. HOLDS. beta -> infinity: P asymp_{n,u} beta^{-3/2}/log beta is stated in check 1527 (iii) line 77; I did not re-derive it (it rests on row 1143 and check 1144). (8) is input-independent, so the same d at both ends. Uncalibrated sequences only. HOLDS. Same argument as row 1549's purity paragraph (checked in 1551 section 6); not new.
- Open statement: matches row 1468 4.3 ((DR), (TR), (WR) with size(T) = V_Lambda, start window, stop rule, (C5) margin). It omits "below the end threshold" from (TR), as row 1549 did; no change of content. HOLDS.
- Zero Hessian: E_i = O(A) at the flat field, J = O(A^6), B analytic, so B(J) - B(0) = O(A^6): zero Hessian, no readout change. HOLDS.

## 7. Novelty against rows 1544, 1549 and checks 1548, 1551

- Row 1544 A excludes globally entire actions. S_tr is arbitrary and log cosh(c sqrt w) has zeros of cosh on the negative axis, so the centre is not entire; also the circle density prod cosh(A sin 3t_j) has complex zeros, so 1544 A's zero argument does not exclude it. 1544 B is a fixed-range statement. Neither implies the present exclusion.
- Row 1549 (Theorem (3)) excludes nonconstant polynomial B on a one-link labelled-pair test, and check 1551 confirmed that this test accepts B - B(0) = -+32 log cosh(c sqrt u). The present note excludes exactly that profile, and the classes (6), by a new test: the colour-rotation circle at constant traces turns J into alpha sin^2 3t, a frequency three times the kernel's first harmonic per link, and the exponential-type bound (5) (growth O(R^{1/6}) in w) then fails.
- New here: the three-mark colour-rotation circle with constant traces; (4) as a direct bound on conditionals (no labelled ratio); (5) via the sixth-root map; the residue/growth exclusion (6) for lambda log D_0; the amplitude-quantization restriction; the explicit Fourier witness (10)-(11); the passing example 1 + eps w. Reused with credit: trace cancellation, packing, chain rule and the extensive-error form from row 1549; the zero-free Fourier-mean method from row 1544 A.
- All are obstructions, not sufficient conditions; the equivalence rule does not apply. On (K2-STEP): CORRECT-NO-ADVANCE. It excludes one more closure class (the one the 1549 test let through) and leaves the step open, as the note says.

## Defects (ranked; none breaks a stated theorem)

1. Selectivity sentence (section "Selectivity, purity"): "precisely where the proof distinguishes four-dimensional SU(2)" overstates; correction in section 6 above.
2. (9) and the application paragraph: state that the untwisted member has all periods > 20; on row 1468's tori late levels (v_k = 2^{N-k} v_E) may have none.
3. RESULT wording depends on the qualifier "with the radius and wrap budgets in (9)"; without it the claim would overclaim on fixed sixteen tori. The explicit d of (11) is about 1e-64, so the bite is only on very large tori.
4. The auxiliary-variable sentence after (6) should name the multiple (for one variable per oriented star, B = -384 log D_0).

## Scope

Checked: all of library/gap-mech-k2-step2-astra62.md from "Plan and choice of test" to the RESULT line, against row 1468 sections 3.1-4.3, check 1551, row 1549 Theorem (3), row 1544 A-B, check 1548 RESULT and check 1527 (iii) line 77. Not checked: the Repo search claims about PR branches and the SA account lines; check 1527 (iii)'s asymptotic itself (taken from that check). Hand check only; no Lean. Float runs were guides.

RESULT Circle and (1)-(3) HOLD; (4), (5), (6), the cosh/mixture exclusions and the amplitude restriction HOLD; (7), (8), Gamma <= C rho and the extensive error eta >= dV/128 (dV/250) HOLD; (9) HOLDS AFTER CLARIFICATION (untwisted member with all periods > 20); the witness (10)-(11) and the passing 1 + eps w example HOLD; the conclusion HOLDS as conditioned on (9) (no fixed-side comparison is made; d of (11) is about 1e-64); U(1)/5D vanishing HOLDS but the "distinguishes 4D SU(2)" sentence HOLDS AFTER CORRECTION (algebraic, dim g >= d-1, not gap-tracking: gapped 3D compact U(1) also has zero Gram); purity blindness and the Wilson separation HOLD (not new); open statement and zero Hessian HOLD; new relative to rows 1544, 1549 and checks 1548, 1551 (it excludes the log-cosh profile the 1549 test accepted); CORRECT-NO-ADVANCE on (K2-STEP).
Checked line by line by Claude (Opus 5.5).
