lead: anthropic/claude-fable-5-2/medium laptop-subagent
row: 1085

# gap-descent-sign-2

## Plan (eight steps; fixed after reading row 1085)
1. Read row 1085 in FINISH.md; record its files, tasks, tests, stop rule, marks. DONE.
2. Read the named files in order; grep open-core.md, parts/gap.md, the registry and the FINISH rows for overlap. DONE.
3. Task 1: the transverse-plaquette kill test (reduction by hand, checks of the script, n = 2, n = 3, sectors, the two ends, the exact statement). DONE: a negative sign found; counterexample written in 3.9.
4. Task 2 (step (S) at n = 2 for beta_M > 3/2). NOT RUN: the row ends at a confirmed negative sign.
5. Task 3 (Remark CUM with eigenvector control). NOT RUN: same rule.
6. Tests named by the row, applied to what is on file. DONE (step 6).
7. Marks, scope, what was not checked, credits, files. DONE (step 7).
8. RESULT line. DONE.

## Log

### Step 1 (row read). DONE.

Row 1085 (FINISH.md line 1166). Tasks, in order: (1) kill test on boxes with a transverse plaquette: sign of l_1 - l_0 (large t), one transverse plaquette, n = 2, then n = 3 if feasible; beta_T = 0 and small positive; beta_M from 0.5 to 8; two converged truncations; GUIDE. A confirmed negative sign ends the row. (2) If none: step (S), Cov_p(r^2, c) >= 0 at n = 2 for every beta_M > 3/2; new methods in turn (association or Chebyshev; higher total positivity; log-concavity; Gaussian comparison); stop each at its first failing line. (3) Remark CUM at large beta_M with the eigenvector control. Tests: Q_8 and 2T must fail; U(1) may pass; Example KIN-6. Stop rule: proof, counterexample, or one named step failed in three written ways beyond those on file.

### Step 2 (files read; prior-work grep). DONE.

Read in full: `library/gap-descent-sign.md` (row 1081), `library/gap-descent-sign-check-astra.md` (row 1082), `library/gap-descent-sign-check-opus.md` (row 1083). Read sections 6.1, 6.3, 6.4, 7.4 of `library/gap-bridge-vectors-max.md` (row 1076). Read the two scripts of `runs/gap-descent-sign/`.

Corrected statements used here (from rows 1082, 1083):
- DIL with its operator premises named; nu_1 = 3/2 on one-sheet boxes with the corrected reason (an integer cut spin costs at least 2 whatever the other spin is).
- N2-SMALL with the rational endpoint bound (e^(3/2) < 9/2, n_0(0) < 243/328 < 3/4).
- Non-negative face part: proved for n at most 3 only.
- Truncation 10 of the two-sheet test is not converged at beta_M = 6, 8.
- CUM is ARGUED only; the missing item is control of the second eigenvector (row 1082).
- The large-t formula l_i = norm(P_1 M phi_i)^2 / lambda_i^2 is a Schur-complement formula. It needs lambda_i simple in P_0 M P_0, and 3/2 the first contributing level (row 1082).
- The Q_8 box of row 1076 refutes the Wilson endpoint form only (check 1079).

Grep of `library/open-core.md`, `parts/gap.md`, `library/open-registry.md`, FINISH.md for FLUX-EXC, transverse plaquette, descent sign, l_1 - l_0: hits are rows 1076, 1081, 1082, 1083 and this row. No other row covers the transverse-plaquette test, step (S) beyond row 1081, or CUM. `scripts/lab_ops.py` is absent in this checkout, so there is no numeric lock. Runs are serial with one BLAS thread.

### Step 3 (task 1: the transverse-plaquette kill test). DONE: negative sign found for beta_M >= 8.5 at beta_T = 0; counterexample in 3.9.

**3.1 Reduction by hand (used by the script).** Box: transverse square with sites 1..4 and links l = 1..4 (one transverse plaquette), n layers. Unreduced slice graph for n = 2: the cube. Spin networks on it: 12 edge spins, trivalent sites. N = sum of j(j+1) over the four vertical edges. K_Phi = product of a_d over the eight horizontal edges, a_d = I_d(beta_M)/I_1(beta_M), d = 2j+1.
- ker N: vertical spins 0. Basis chi_a(U_1) chi_b(U_2), U_k the plaquette of layer k. K_Phi = a_a^4 a_b^4.
- P_0 e^(-V_f) P_0 is the multiplication by Z(U_1,U_2) e^(beta_T (x(U_1)+x(U_2))), with Z = sum_d a_d^4 chi_d(U_1) chi_d(U_2) (integrate the four cut rotations; each Haar integral joins two characters; constant c_1^4 dropped). So P_0 M P_0 = K_0^(1/2) Z E_T K_0^(1/2) on l^2 of pairs (a, b).
- Level N = 3/2: two vertical edges x, y with spin 1/2, the other two 0 (a half-integer vertical spin changes the layer spin by a half-integer, so the number per layer gap is even). The spin-0 sites join the links of each arc. So the state lives on the pillow graph: top arcs T_I, T_II (spins j, j'), bottom arcs B_I, B_II (spins k, k'), two verticals of spin 1/2. Arc lengths (n_I, n_II) = (1, 3) for the four adjacent pairs, (2, 2) for the two diagonal pairs. K_Phi = a_j^(n_I) a_j'^(n_II) a_k^(n_I) a_k'^(n_II).
- The vector F G, F = product of the four side-plaquette weights, G = G(U_1, U_2), projected on the spin-0 sites, is sum over J_I, J_II, a, b of d_(J_I) d_(J_II) a_(J_I)^(n_I) a_(J_II)^(n_II) G_ab chi_(J_I)(side I) chi_(J_II)(side II) chi_a(bottom) chi_b(top): four loops on the pillow graph, each edge in two loops.
- Coefficient formula used (recalled form: one 6j per trivalent site; to be TESTED before use by an exact Gram identity):
  <j j' k k' s_x s_y | L(J_I, J_II, a, b)> = sqrt(d_j d_j' d_k d_k' d_sx d_sy) {j j' s_x; J_II J_I b}{j j' s_y; J_II J_I b}{k k' s_x; J_II J_I a}{k k' s_y; J_II J_I a}.
  Exact Gram identity (hand, by Schur orthogonality): <L, L'> = sum over P of [P in J_I x J_I'][P in J_II x J_II'][P in a x a'][P in b x b'] / d_P^2.
- l_i = sum over the six pairs and the states of K_Phi abs(amplitude)^2 / lambda_i^2, G = E_T K_0^(1/2) phi_i.

**3.2 Checks of the script before use (all GUIDE).** Scripts in `runs/gap-descent-sign-2/`: `gram_test.py`, `tplaq.py`, `assembly_test.py`. The 6j routine is copied from row 1081's `su2box.py`.
- Gram identity: 3256 pairs of loop labels with doubled spins up to 3, all sectors (s_x, s_y): worst error 1.3 x 10^(-14) (`log_gram_3.txt`). So the coefficient formula of 3.1 is an orthonormal expansion with the right Gram matrix. In the sector s_x = s_y = 1/2 the coefficient is a product of two squares, so it is non-negative.
- One sector by hand, a = b = 0: the formula gives squared norm d_sx d_sy/(d_I d_II)^2 for the (s_x, s_y) part of chi_(J_I)(side I) chi_(J_II)(side II). Schur orthogonality for the irreducible representation J_I x J_II of SU(2) x SU(2) gives tr(P_sx) tr(P_sy)/(d_I d_II)^2, the same. So the labels s_x, s_y are the cut spins in this case.
- Contraction in `tplaq.py` against a brute-force sum with the Gram-tested coefficients, random G, both arc types, with the K_Phi weights: relative difference 4 x 10^(-16) (`log_assembly.txt`).
- Small beta_M by hand (beta_T = 0). Vacuum (1, 1): only the loop (J_I, J_II) = (1/2, 0) on the short arc of an adjacent pair enters at leading order; amplitude 2 a_2, K_Phi = a_2^2, four pairs: l_0 = 16 a_2^4 (1 + a_2^4 + ...), the a_2^4 from the diagonal pairs. Excited state ((1,2) + (2,1))/sqrt 2, lambda_1 = a_2^4 at leading order: l_1 = 4 a_2^2 (1 + O(beta_M^2)). With a_2 = beta_M/4 + ...: l_0 = beta_M^4/16 and l_1 = beta_M^2/4, the values of row 1081 step 7 (l_0 checked by row 1083; l_1's coefficient 1/4 is now derived: the coefficient of the bottom state k = 0 is 1/2, and 4 pairs x 2 layers x (2 a_2 a_2^2/sqrt 2 x 1/2)^2 a_2^4 / a_2^8 = 4 a_2^2). The script gives l_0/(16 a_2^4) - 1 = a_2^4 to four digits at beta_M = 0.02, 0.05, 0.1, 0.2, 0.5, and l_1/(beta_M^2/4) = 1.0001, 1.0007, 1.0029 at beta_M = 0.02, 0.05, 0.1 (`log_smallbeta.txt`).
- Not checked: no second implementation of l_i at beta_M of order one exists. The full cube basis is too large for this laptop at beta_M = 8 or more.

**3.3 Result for n = 2 (GUIDE; a sign change found).** Truncations (A, D) = number of characters per layer in ker N, number of loop spins: (12, 12), (16, 16), (22, 20) on the main grid; (18, 18), (26, 24) on the fine grid. All l_i agree between truncations to 10^(-13) (the vectors decay like a_d^4). lambda_1 of P_0 M P_0 is simple at every grid point, and phi_1 is even under the swap of the two layers. For beta_M >= 3 the ratio lambda_2/lambda_1 is at most 0.82. For small beta_M it is close to 1 (0.9995 at beta_M = 0.5: phi_1 and phi_2 are the swap-even and swap-odd combinations of (1,2) and (2,1), split at relative order a_2^4); the two are in different symmetry sectors of the layer swap, so the Schur-complement formula applies to each, for t large enough.

beta_T = 0:
| beta_M | lambda_1/lambda_0 (t = infinity) | l_0 | l_1 | l_1 - l_0 |
|---|---|---|---|---|
| 0.5 | 2.343e-4 | 0.003749 | 0.066841 | +0.063091 |
| 1 | 3.340e-3 | 0.053434 | 0.310069 | +0.256636 |
| 2 | 3.643e-2 | 0.583613 | 1.553069 | +0.969456 |
| 2.4 | 6.284e-2 | 1.008754 | 2.290676 | +1.281923 |
| 3 | 0.11484 | 1.855737 | 3.503241 | +1.647504 |
| 4 | 0.22248 | 3.668167 | 5.510939 | +1.842772 |
| 6 | 0.44882 | 7.830889 | 8.969137 | +1.138248 |
| 8 | 0.63490 | 11.658050 | 11.776050 | +0.117992 |
| 8.5 | 0.67337 | 12.493750 | 12.392900 | -0.100851 |
| 9 | 0.70876 | 13.274440 | 12.978100 | -0.296345 |
| 10 | 0.77086 | 14.667900 | 14.057130 | -0.610771 |
| 12 | 0.86444 | 16.805890 | 15.876330 | -0.929559 |
| 16 | 0.96047 | 19.104980 | 18.404820 | -0.700166 |
| 24 | 0.99767 | 20.984760 | 20.893740 | -0.091021 |
| 48 | 0.9999994 | 23.191610 | 23.191550 | -0.000054 |

Sign of l_1 - l_0 for beta_T > 0 (same truncations):
| beta_M | beta_T = 0.02 | 0.05 | 0.1 | 0.15 | 0.2 | 0.5 |
|---|---|---|---|---|---|---|
| 0.5 to 8 (ten values) | + | + | + | + | + | + |
| 8.5 | -0.0982 | -0.0843 | -0.0392 | +0.0251 | +0.1001 | |
| 9 | -0.2909 | -0.2632 | -0.1767 | -0.0618 | +0.0635 | |
| 10 | -0.5953 | -0.5204 | -0.3144 | -0.0809 | +0.1468 | +1.3283 |
| 12 | -0.8598 | -0.5912 | -0.1113 | +0.2888 | +0.6506 | +2.6079 |
| 16 | -0.3265 | +0.0614 | +0.4479 | +0.8134 | +1.2479 | +4.5753 |
| 24 | +0.0583 | +0.1532 | +0.3126 | +0.4815 | +0.6722 | |

**Reading.** On the row's grid (beta_M from 0.5 to 8) the sign is positive at beta_T = 0 and at beta_T = 0.02 to 0.5. It turns negative between beta_M = 8 and 8.5 at beta_T = 0, and stays negative for all larger beta_M on the grid at beta_T = 0 (tending to 0 from below). For beta_T > 0 the negative region is bounded: about 8.5 <= beta_M <= 16 at beta_T = 0.02, about 9 <= beta_M <= 10 at beta_T = 0.15, none at beta_T = 0.2.

**3.4 One more hand check of the level-3/2 norm (PROVED identity; a = b = 0, no K_Phi weight).** For F = product over l of f(Phi_l(2) Phi_l(1)^(-1)), f = sum_J d_J a_J chi_J, and cut rotations h_l at the layer-2 sites: integrate Phi_l(2), then Phi_l(1), by Schur orthogonality. Result: <F, rho(h) F> = product over l of sum_J a_J^2 chi_J(h_l) chi_J(h_(l+1)). (The layer-1 link cannot be gauged away; a first attempt that did so gave a wrong formula with only s_x = s_y.) The projection on cut spins (s_l) is then sum over J_1..J_4 of prod_l a_(J_l)^2 prod_sites d_(s_l) [s_l in J_(l-1) x J_l]. For the pair pattern (1/2, 1/2, 0, 0) this is 4 sum over abs(J_I - J_II) = 1/2 of a_(J_I)^(2 n_I) a_(J_II)^(2 n_II). The coefficient formula of 3.1 gives the same: amplitude d_I d_II a^(n_I) a^(n_II) x 2/(d_I d_II). So the script's level-3/2 norm of M applied to the constant is right for every loop spin, by a derivation that uses no 6j symbol.

**3.5 The centre symmetry at beta_T = 0 (PROVED observation).** Fix one transverse link l_0 and let c multiply Phi_(l_0)(k) by -1 for every layer k. Then q_(l_0) = Phi_(l_0)(2) Phi_(l_0)(1)^(-1) is unchanged, and every transverse plaquette changes sign. At beta_T = 0 the face potential V_f does not contain the transverse plaquettes, so c commutes with V_f. It commutes with K_Phi (convolution by a class function), with G and with every cut rotation (-1 is central). So c is a unitary symmetry of S, of N and of B_t for every t, at beta_T = 0, for every n. On ker N it acts on chi_a(U_1) chi_b(U_2) as (-1)^(a+b) (a, b dimensions). This holds for any transverse lattice: one such symmetry per transverse link. It is -1 in the left SU(2) of the sheet over l_0.
GUIDE: at beta_T = 0 the script gives centre parity -1 for phi_1 at every sampled beta_M (n = 2: nine values from 2 to 16, `log_sectors_bT0.txt`; n = 3: twelve values from 0.5 to 14, where phi_0 is also printed, with parity +1). So at beta_T = 0 the gap m at large t is the splitting between the centre-even vacuum and the lowest centre-odd state. It closes fast as beta_M grows (lambda_1/lambda_0 = 0.960 at beta_M = 16, 0.9999994 at 48, n = 2). For beta_T > 0 the symmetry is broken and the parities are no longer exact (at beta_T = 0.05, beta_M = 10: +0.93 and -0.92).

**3.6 Result for n = 3 (GUIDE; the same sign change).** Three layers, two layer gaps. Level 3/2 has both spin-1/2 edges in one gap. The other gap is integrated to the factor sum_e a_e^4 chi_e chi_e on its two layers; layer 3 (or 1) is a spectator. The two gaps give equal contributions for a state with a parity under the reflection of the layers. Truncations (A, D) = (10, 10) and (12, 12) (ker N blocks of dimension 1000 and 1728; 219 MB peak); l_0, l_1 agree to 1.3 x 10^(-13). Check: l_0 = 2 x 16 a_2^4 at small beta_M (0.0074986 at 0.5, twice the n = 2 value).

| beta_M | lambda_1/lambda_0 (t = infinity) | l_0 | l_1 | l_1 - l_0, beta_T = 0 | beta_T = 0.05 | beta_T = 0.2 |
|---|---|---|---|---|---|---|
| 0.5 | 2.344e-4 | 0.007499 | 0.101895 | +0.094396 | +0.094390 | +0.094307 |
| 2 | 3.697e-2 | 1.167227 | 2.588031 | +1.420804 | +1.420569 | +1.417057 |
| 4 | 0.24047 | 7.339644 | 10.005100 | +2.665457 | +2.658638 | +2.559515 |
| 6 | 0.51640 | 15.696480 | 17.300440 | +1.603958 | +1.574499 | +1.219416 |
| 8 | 0.75662 | 23.254330 | 23.349390 | +0.095062 | +0.112210 | +0.295621 |
| 8.5 | 0.80425 | 24.818520 | 24.642330 | -0.176183 | -0.085245 | +0.411459 |
| 9 | 0.84578 | 26.222820 | 25.847210 | -0.375613 | -0.168994 | +0.606712 |
| 10 | 0.90993 | 28.556580 | 28.001460 | -0.555118 | -0.070803 | +1.017587 |
| 12 | 0.97472 | 31.782270 | 31.400920 | -0.381349 | +0.173807 | +1.167280 |
| 14 | 0.99381 | 34.018630 | 33.868110 | -0.150518 | +0.174704 | +0.832234 |
(l_0, l_1 and the ratio are at beta_T = 0.)

**3.7 Symmetry sectors (GUIDE; n = 2; `log_sectors_bT0.txt`, `log_sectors_bT0.5.txt`).** The layer swap is a symmetry for every beta_T. The centre flip is a symmetry at beta_T = 0 (3.5).
- The vacuum is swap-even and centre-even. phi_1 is swap-even and centre-odd at beta_T = 0.
- First excited state in the vacuum's own sector (swap-even, centre-even), beta_T = 0: l - l_0 = +2.73, +2.31, +2.00, +1.67, +1.16, +1.06, +0.96, +1.39, +3.74 at beta_M = 2, 3, 4, 6, 8, 8.5, 10, 12, 16. Positive at all nine.
- Lowest swap-odd state (it is centre-odd at beta_T = 0; it is the third eigenvector for beta_M <= 8): l - l_0 = +0.264, -0.036, -0.512, -1.227, -1.292, -1.223, -0.881, -0.226, +1.094 at the same beta_M, beta_T = 0. At beta_T = 0.5: -0.072, -0.605, -1.355, -1.119 at beta_M = 3, 4, 6, 8. So the lowest state of the swap-odd sector carries less level-3/2 leakage than the vacuum for beta_M from 3 to 12, inside the row's range and also at beta_T = 0.5. This is not the gap m. It says that a sector-by-sector form of (FLUX-EXC) is false on this box at these couplings (GUIDE).

**3.8 The two ends of the kinetic time, n = 2, beta_T = 0 (the endpoint form; GUIDE with hand reductions).** This part uses no pillow coefficient. It uses 3.1's formula for P_0 M P_0 and the single-sheet blocks of row 1081.
- End t = infinity is also the Wilson end beta_L = 0: lambda_j(beta_L) tends to 0 for j >= 1/2, so D tends to P_0 in norm (the norm of M_c - P_c^0 is lambda_(1/2)(beta_L)). The operator is P_0 M P_0. Its two top eigenvalues are positive and simple on the grid. So m(beta_L) tends to m(beta_L = 0) := log(lambda_0/lambda_1)(P_0 M P_0) as beta_L tends to 0, and m(t) tends to the same number as t tends to infinity.
- End t = 0 (beta_L = infinity) is the face S S*. **Lemma FACE-PROD (PROVED by hand).** At beta_T = 0, with a = 1, V_f is a sum over the four transverse links l of -beta_M x(Phi_l(2) Phi_l(1)^(-1)), and K_Phi is a product over links. So on L^2 of all Phi the face operator is a tensor product over the four sheets of the one-sheet operator T_1 = K^(1/2) e^(beta_M x) K^(1/2). T_1 commutes with the left and right SU(2) of its sheet. Split the sheet space by (left spin p, right spin q); T_1 acts on the multiplicity space M_(p,q), with top eigenvalue mu_(p,q). The group G at a transverse site acts on the right index of one sheet and the left index of the next. Its invariants need q of one sheet = p of the next, and then they are one-dimensional. So K is the direct sum over cycles (p_1, p_2, p_3, p_4) of the tensor products of M_(p_l, p_(l+1)), and the face eigenvalues are the products of the sheet eigenvalues along a cycle. The vacuum is mu_(0,0)^4. QED
  For n = 2 each sector is multiplicity free: basis (j_1, j_2) with p and q in j_1 x j_2, K = a_(j_1) a_(j_2), and x has the entries (1/2) sqrt(d_1 d_1' d_2 d_2') {p j_2' j_1'; 1/2 j_1 j_2}{q j_2' j_1'; 1/2 j_1 j_2} up to a phase that is constant on the sector (Edmonds (7.1.6), once on the left and once on the right indices; x is bipartite in 2 j_1, so a global sign does not change the spectrum). For p = q this is row 1081's squared-6j matrix on the block j_3 = p.
- Script `endpoint2.py` (and `endpoint.py`, four candidate cycles only): all cycles with doubled spins up to 4, sheet truncations 2Jmax = 40 and 56, ker N truncations (18, 18) and (24, 22). The two runs agree in every printed digit. Regression: the singlet gap of one sheet is 2.282987 at beta_M = 2.4 and 2.540323 at 8 (row 1081: 2.2829867 and 2.5403231). Operator order (Corollary KIN-1) is respected: lambda_0(t = infinity) <= mu_(0,0)^4 and the centre-odd top eigenvalue at t = infinity is below mu_(1/2,1/2)^4, at every beta_M.
- For beta_M >= 2 the first excited face state is the cycle (1/2, 1/2, 1/2, 1/2): every sheet in its lowest (1/2, 1/2) state. It is centre-odd. For beta_M <= 1 it is the singlet excitation of one sheet. The next cycle is far above ((1,1,1,1) or (0,0,0,1)).

| beta_M | m(t = 0) = m(beta_L = infinity), the face | m(t = infinity) = m(beta_L = 0) | difference |
|---|---|---|---|
| 0.5 | 4.211900 | 8.358770 | +4.146871 |
| 1 | 2.993688 | 5.701915 | +2.708227 |
| 2 | 2.241941 | 3.312306 | +1.070365 |
| 2.4 | 1.754451 | 2.767209 | +1.012758 |
| 3 | 1.302616 | 2.164191 | +0.861575 |
| 4 | 0.905590 | 1.502936 | +0.597346 |
| 6 | 0.563103 | 0.801124 | +0.238021 |
| 8 | 0.408996 | 0.454295 | +0.045299 |
| 8.5 | 0.382832 | 0.395467 | +0.012635 |
| 9 | 0.359822 | 0.344243 | -0.015579 |
| 10 | 0.321221 | 0.260247 | -0.060973 |
| 12 | 0.264499 | 0.145668 | -0.118831 |
| 16 | 0.195495 | 0.040328 | -0.155166 |
| 24 | 0.128485 | 0.002332 | -0.126153 |

**Reading.** For beta_M >= 9 the gap at beta_L = 0 is below the face gap. So on this box the endpoint form m(beta_L, beta_M) >= m(infinity, beta_M) fails for small beta_L (Wilson form) and for large t (heat-kernel form). The two runs fit together: m(t) falls towards m(t = infinity) at large t exactly where l_1 < l_0 (beta_M >= 8.5), and the end value drops below the face value from beta_M = 9. At beta_M = 8.5 the ends are still ordered (+0.0126) while m already falls at large t, so m(t) is not monotone there.
Why (ARGUED). On the face the sheets are free rotors: the transverse plaquette is spread over the group, and the centre-odd state costs four rotor quanta, about 3/beta_M. At beta_L = 0 the layers are separately gauge invariant, and the weight Z(U_1, U_2) K_0 has two wells, at U_1 = U_2 = 1 and at U_1 = U_2 = -1 (Z(U, U) = sum_d a_d^4 chi_d(U)^2 is largest at the centre). The vacuum and phi_1 are the even and odd combinations of the two wells, and their splitting is a tunnelling term. It falls much faster than 1/beta_M (0.0023 at beta_M = 24 against 0.128).

**3.9 The counterexample, written exactly (GUIDE grade; hand reductions as stated; checked by no one).**
Box: SU(2); transverse lattice one square (four sites, four links, one plaquette); free ends in direction 1; beta_T = 0.
(a) Heat-kernel monotone form, n = 2, beta_M = 10: lambda_1/lambda_0 of P_0 M P_0 = 0.7708608, lambda_2/lambda_1 = 0.4647944, l_0 = 14.667900, l_1 = 14.057130, and l_1 - l_0 = -0.6107714675445894 at (A, D) = (12, 12), -0.6107714675445877 at (16, 16), -0.6107714675446108 at (22, 20), -0.6107714675445663 at (18, 18), -0.6107714675445717 at (26, 24). So n_1(t) - n_0(t) = (3/2) e^(-3t/2) (l_1 - l_0) + O(e^(-2t)) is negative for all large t. First negative grid value: beta_M = 8.5, l_1 - l_0 = -0.10085076888083 at (18, 18) and -0.10085076888083 at (26, 24) (they differ in the 14th digit). Also at beta_T = 0.1, beta_M = 10: -0.3143977371226 at both truncations.
(b) The same for n = 3, beta_M = 10, beta_T = 0: l_1 - l_0 = -0.5551180738401342 at (10, 10) and -0.5551180738401023 at (12, 12).
(c) Endpoint form, n = 2, beta_M = 10: m(beta_L = 0) = 0.260247 and m(beta_L = infinity) = 0.321221, the same at both truncation pairs (2Jmax 40 with (18, 18); 2Jmax 56 with (24, 22)). First negative grid value: beta_M = 9, 0.344243 against 0.359822. By the norm continuity of D in beta_L at 0, m(beta_L, 10) < m(infinity, 10) for all small beta_L > 0. By continuity of both ends in beta_T, the strict inequality (c) holds for small beta_T > 0 too (size not computed).
What it refutes: (FLUX-EXC) and (MON-L), in the monotone form and in the endpoint form, on boxes with a transverse plaquette, at beta_T = 0 (and small beta_T) and beta_M >= 8.5 (monotone) or >= 9 (endpoint).
What it does not refute: one-sheet boxes and transverse trees (there ker N is the constants, m tends to infinity as beta_L tends to 0, and rows 1076 and 1081 found no dip); any coupling with beta_M <= 8 for the gap m (all signs positive on the grid, both tests); beta_T >= 0.2 (monotone test positive on the grid); the first excited state of the vacuum's own symmetry sector (positive at all nine values in 3.7).
Grade. The reductions are by hand (Lemma KIN (c) of row 1076, used as stated and reported HOLDS by check 1079; the Z formula; Lemma FACE-PROD; the Schur-complement formula with the conditions of row 1082, which hold on the grid). The numbers are double-precision eigenvalues of explicit matrices of dimension at most 1728, with no error bounds. Item (c) does not use the pillow coefficient formula. Items (a), (b) use it; it is recalled and tested (3.2, 3.4), not proved here.

### Steps 4 and 5 (tasks 2 and 3). NOT RUN.

Row 1085 says that a confirmed negative sign in task 1 ends the row, and it makes task 2 conditional on no negative sign. Task 1 gave a negative sign at five truncations (3.9). So step (S) at n = 2 for beta_M > 3/2 and Remark CUM were not attacked here. Their status is unchanged from rows 1081 to 1083: (S) OPEN with three written failures on file; CUM ARGUED with the eigenvector control missing. Nothing in this row bears on them: the counterexample needs a transverse plaquette, and the n = 2 one-sheet box has none.
One caution for whoever reads the two together. The negative sign sits outside the row's stated range of beta_M (0.5 to 8). On that range the kill test is passed. I extended the grid because the excess at beta_M = 8 was small (+0.118) and falling.

### Step 6 (the row's tests). DONE as far as they apply.

The tests are for a proof of the sign. This row has no such proof. Applied to what is here:
- Lemma FACE-PROD and the Z formula use Peter-Weyl, Schur and Haar measure only. They hold for frozen Q_8, 2T and for compact U(1) with their own characters. They make no sign claim, so the Q_8 and 2T tests do not bind them.
- The centre symmetry (3.5) needs a central element -1 of the group that changes x to -x. SU(2), Q_8, 2T have it. U(1) has a continuous centre and more symmetry at beta_T = 0 (by the same Z formula with Fourier modes, a + b is conserved in ker N; not computed).
- Example KIN-6: not relevant; no step here argues from the form S* e^(-tN) S.
- Strength warning of brief P2: the result goes the other way. A volume-free form of (FLUX-EXC) that covers boxes with transverse plaquettes at beta_T = 0 and all beta_M is refuted at GUIDE grade. The three-dimensional test-bed VB-18 has such boxes when its transverse lattice has a plaquette; I did not check which boxes VB-18 needs.

### Step 7 (marks, scope, what was not checked, credits, files). DONE.

**Marks.**
- Reduction of the plaquette box at t = infinity: ker N = class functions of the layer plaquettes; P_0 M P_0 = K_0^(1/2) Z E_T K_0^(1/2) with Z = sum_d a_d^4 chi_d chi_d: PROVED by hand (3.1), given Lemma KIN (c).
- Level 3/2 on the pillow graph and the coefficient formula: recalled; tested by the Gram identity (3256 pairs), by one sector by hand, by the 6j-free identity of 3.4, and by the small-beta_M hand values. Not proved here. GUIDE.
- l_1 = beta_M^2/4 at leading order (row 1081 had it ARGUED, coefficient unchecked): derived by hand in 3.2 and met by the run. PROVED at leading order by hand, given the coefficient formula.
- Centre symmetry at beta_T = 0 (3.5): PROVED observation.
- Lemma FACE-PROD (3.8): PROVED by hand.
- Kill test, n = 2 and n = 3, heat-kernel form at large t: sign of l_1 - l_0 positive for beta_M from 0.5 to 8 at beta_T = 0 to 0.5; negative for beta_M >= 8.5 at beta_T = 0 (all larger grid values, to 48 for n = 2 and to 14 for n = 3) and on a bounded region for 0 < beta_T <= 0.15. GUIDE; a counterexample at GUIDE grade (3.9 (a), (b)).
- Endpoint form on the plaquette box, n = 2, beta_T = 0: m(beta_L = 0) < m(beta_L = infinity) for beta_M >= 9 on the grid (9 to 24). GUIDE; a counterexample at GUIDE grade (3.9 (c)).
- (FLUX-EXC) and (MON-L) on boxes with a transverse plaquette, for all couplings: FAILS at GUIDE grade, by 3.9. Scope: beta_T = 0 and small beta_T, beta_M >= 8.5; the single-plaquette box with n = 2 (both forms) and n = 3 (monotone form).
- (FLUX-EXC) on one-sheet boxes: untouched. OPEN as in row 1081 (n = 2, beta_M > 3/2; n >= 3 outside the dilute range).
- Sector form on the plaquette box: the lowest swap-odd state has l below l_0 for beta_M from 3 to 12 (GUIDE); the first excited state of the vacuum's own sector has l above l_0 at all nine sampled beta_M (GUIDE).
- Step (S) and Remark CUM: not attacked (steps 4, 5).

**Scope of the negatives.** The word FAILS above is about the statement "n_1 >= n_0 for all t > 0, and m(beta_L) >= m(infinity), on every box and at all couplings". It is refuted on one family of boxes, at beta_T at most 0.15, at beta_M at least 8.5, by double-precision runs with hand reductions. It is not a statement about one-sheet boxes, about the window couplings (beta_M near 2.4, where both tests are positive on these boxes), about beta_T of order one, or about infinite volume. It does not say that a descent with a different quantity or a different path cannot work.

**Not checked, not computed.**
- One session, one author (Claude Fable 5.2 medium), no second reader. No second implementation of l_i at beta_M of order ten.
- The pillow coefficient formula is not proved here (tests in 3.2, 3.4). Item (c) of 3.9 does not need it.
- No error bounds on eigenvalues. The truncation agreement (10^(-13)) is not a bound for the infinite matrices.
- m(t) at finite t between the two ends. The Wilson form at small beta_L beyond the limit value: at order beta_L^2 the level with one vertical spin 1 (N = 2) enters with the same power as level 3/2 (lambda_1(beta_L) = beta_L^2/24 against lambda_(1/2)^2 = beta_L^2/16); its leakage was not computed. So the sign of the first Wilson correction at beta_L = 0 is not known; only the limit value is.
- The face for n = 3, and the face at beta_T > 0 (no tensor product there).
- Face cycles with a sheet spin above 2, and second eigenvalues of charged sheet sectors (both should lie higher; not computed).
- Larger transverse lattices, and several plaquettes.
- Lemma KIN of row 1076 is used as stated.
- No numeric lock (`scripts/lab_ops.py` is absent in this checkout). Runs were serial, one BLAS thread, peak memory 219 MB, longest run 8 minutes.

**Credits.** Lemma KIN, Identity KIN-5, Corollary KIN-1, Remark FLAT, Example KIN-7 and brief P2: row 1076 (Claude Fable 5.2 max). The spin-network form, the squared-6j matrix, the large-t criterion l_1 against l_0 and the name of this kill test: row 1081 (Claude Fable 5.2 medium). The conditions of the Schur-complement formula, the n = 4 warning on signs, and the corrections used here: row 1082 (gpt-6-astra xhigh) and row 1083 (Claude Opus 5.5 max). 6j symbols and the scalar-product formula (7.1.6): G. Racah; E. Wigner; A. R. Edmonds' text. The following attributions are recalled from memory; no source was opened in this row. Spin networks: R. Penrose; the electric basis of lattice gauge theory: J. Kogut and L. Susskind. Character expansion and the integration of a tube of plaquettes: A. Migdal; the review of J.-M. Drouffe and J.-B. Zuber. Centre symmetry and centre-odd sectors: G. 't Hooft. The rotor picture of a finite O(N) system: H. Leutwyler; P. Hasenfratz and F. Niedermayer. The lane builds on T. Balaban and on the account of E. Sussman and L. Alpoge; no step of theirs is used in this row.

**Files** (all in `runs/gap-descent-sign-2/`, 280 KB in all; `tplaq.py` gained the centre-parity column and the NEIG option after the n = 2 logs were written, with no change to l_i): `gram_test.py`, `assembly_test.py`, `tplaq.py`, `sectors.py`, `endpoint.py`, `endpoint2.py`; logs `log_*.txt`; data `out_tplaq_*.json`. The originals in `runs/gap-descent-sign/` are unchanged; the 6j routine was copied.

RESULT: Row 1085 (Claude Fable 5.2 medium, laptop subagent; one session, checked by no one). COUNTEREXAMPLE at GUIDE grade (double-precision runs on hand reductions) on the SU(2) box with one transverse plaquette at beta_T = 0. (a) Monotone heat-kernel form, n = 2, beta_M = 10: l_1 - l_0 = -0.6107714675 at five truncations from (12, 12) to (26, 24) (agreement 10^(-13)), so n_1 < n_0 for all large t; the sign is negative at every grid beta_M >= 8.5 (to 48), also for n = 3 (beta_M = 10: -0.5551180738 at (10, 10) and (12, 12)), and for 0 < beta_T <= 0.15 on a bounded range of beta_M. (b) Endpoint form, n = 2, beta_M = 10: m(beta_L = 0) = 0.260247 < m(beta_L = infinity) = 0.321221 at two truncation pairs, negative at every grid beta_M >= 9, by a computation that uses no pillow coefficient. PROVED by hand: the formula P_0 M P_0 = K_0^(1/2) Z E_T K_0^(1/2) with Z = sum_d a_d^4 chi_d chi_d, Lemma FACE-PROD (the face at beta_T = 0 is a product over sheets, cycles of sheet sectors), the centre symmetry at beta_T = 0 (phi_1 is the lowest centre-odd state), l_1 = beta_M^2/4 at leading order. On the row's own range beta_M 0.5 to 8 every sign is positive (least +0.118 at beta_M = 8, n = 2). Not refuted: one-sheet boxes, beta_M <= 8, beta_T >= 0.2, the first excited state of the vacuum's own symmetry sector. Tasks 2 and 3 NOT RUN, by the row's rule that a confirmed negative sign ends it: step (S) stays OPEN and Remark CUM stays ARGUED. Output `library/gap-descent-sign-2.md`.
