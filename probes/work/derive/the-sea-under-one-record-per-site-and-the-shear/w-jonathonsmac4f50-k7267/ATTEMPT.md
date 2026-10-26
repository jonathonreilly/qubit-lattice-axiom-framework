# J:derive:the-sea-under-one-record-per-site-and-the-shear:a1

Worker: Claude Sonnet 5.5 (same family as the supervisor's blocks; unrefereed).
Sources read first (all as landed on main a77a3449c91a753b06ce2a63876cd460b62cb4cf): `docs/MINIMAL_AXIOMS_2026-06-29.md` (read in full), `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (read in full; no primitive is used), the block 155 note (landed on main; its pushed branch no longer exists on origin), block 130, block 147, block 78 (`ONE_RECORD_PER_SITE_IS_AN_INTERACTION...`), block 85 (`THE_CROWD_UNDER_EXCLUSION...`), block 62 (`ANGLES_ARE_THE_TILT...`). Hashes are in RECOVERY_STATUS.json.

## Plain language first

The question: if the lattice is stretched along one axis and squeezed along another (same volume per site), does the lowest energy of N records, with at most one record per site, go down? Answer shown here: yes, for every record number strictly between empty and full, for both exchange signs, for every uniform volume-preserving frame (including off-diagonal shears), at every size of the cubic torus. The reason is short. The ground energy is the lowest value of a quantity that is linear in the frame, so it is concave in the frame. The cubic rotations act on the frame and average any frame to a multiple of the identity (its trace over d). The ground energy is also unchanged by a rotation. So the energy of any frame lies below the energy of the "rotation-averaged" frame, which is the equal-length one scaled by trace/d. At fixed volume that trace is at least d, and the equal-length energy is negative, so the energy goes down. No filling, interaction or exchange detail enters. Finite exact spectra on the 4x4 plane and on the 2x2x2 cube agree. One caution found on the way: the strictly periodic 2x2x2 torus has no hopping at all (the forward and backward hops cancel), so the question is empty there; only the bond-once 2x2x2 cube is a nontrivial "2x2x2" torus.

## 1. The exact statement attempted

Setting (supplied, not derived from the axioms; every item is a supplied clause):
- Block 62's uniform frame: `H_F = sum_{j,a} F[a][j] sigma_a S_j`, `S_j = (T_j - T_j^dagger)/(2i)`, `F[a][j] = E_a^j`; `H^2 = g^{ij}s_i s_j` with `g^{-1} = F^T F`; volume per site `= 1/det F` (so `E_j^j = 1/l_j` has `det F = 1/(l_1 l_2 l_3)`). Landed at block 62 T1.
- Block 78's hard-core compression: N records on the sites of a graph, at most one per site, each with a two-state coin; the generator is `P dGamma(h_F) P` with `P` the projector on "no site doubly occupied"; two composition rules (fermionic order sign, bosonic no sign) are both supplied model choices (block 78, block 128).
- `E_N(F) = lambda_min(H_N(F))`; `E_sea(F) = min_N E_N(F)` (block 76/130 meaning of "the sea").
- Graphs: (G3) the torus `L x L x L`, `L >= 3` (hops along three directions, coin matrices `sigma_1, sigma_2, sigma_3`); (G2) the torus `L x L`, `L >= 3`, plane walk with `sigma_1, sigma_2` and a 2x2 frame; (GQ) the bond-once `2x2x2` cube (open box, each bond used once with the orientation of the torus bond).

**Theorem attempted (T).** For G in {G3, G2, GQ}, every `N` with `0 < N < n`, both composition rules, and every real `d x d` frame `F` with `det F = 1` (d = 3 or 2):

`E_N(F) <= c(F) E_N(1) <= E_N(1)`, `c(F) = (sum of singular values of F)/d >= 1`,

with `c(F) = 1` iff `F^T F = 1` (a pure relabelling); hence `E_N(F) < E_N(1)` for every `F` with `F^T F != 1`. The same holds for `E_sea`. At `N = 0` and `N = n` all `E_N` vanish (no fall).

**Corollary (U, uniform in L).** For `L` even `>= 4` and density `rho = N/n` in `(0,1)`, `E_N(1) <= -sum_cells eps_{k_c}` for cell fillings `k_c` summing to N, so `E_N(F) - E_N(1) <= -(c(F)-1) * sum_cells eps_{k_c}`, with `eps_k > 0` independent of L.

Predictions of the supervisor's prior (falls at every density below full occupancy): confirmed, in this form.

## 2. Numbered steps

1. **[PROVED] Linearity and concavity.** `h_F` (single-body) is linear in `F`; so `H_N(F) = P dGamma(h_F) P` is a linear map of `F` into Hermitian matrices (P does not depend on F). `E_N(F) = min_{|psi|=1} <psi|H_N(F)|psi>` is a minimum of linear functions of `F`, so it is concave on the whole space of real `d x d` matrices, and homogeneous: `E_N(cF) = c E_N(F)` for `c > 0`. (Same argument as block 85 T1, which used it for bond-rate alternation; the use below is different: the group is the cubic rotation group and the parameter is the whole frame.)

2. **[PROVED + CHECKED] Rotation covariance.** For each of the 24 proper cubic rotations `R` (signed permutation matrices of determinant +1), let `U_R in SU(2)` satisfy `U sigma_b U^{-1} = sum_a R_{ab} sigma_a`, and let `W_R` act on a mode `(x, s)` as `x -> R x` (mod L, or the corresponding map of the cube) on the site and `U_R` on the coin. Then `W_R h_F W_R^{-1} = h_{R F R^T}` (reversing a hop direction flips the sign of that hop term, and the spinor rotation flips `sigma_a` in the same way). Proof: `h_F` is a sum over bonds of `(-i/2) sigma~_j |x><x+e_j| + h.c.`, `sigma~_j = sum_a F_{aj} sigma_a`; conjugation by `W_R` sends `|x><x+e_j|` to the hop along `R e_j = +-e_{j'}` and `sigma~_j` to `sum_a F_{aj} R_{ba} sigma_b`; the sign from `-e_{j'}` is absorbed by `(−i/2)σ|y⟩⟨y−e| + h.c. = −[(−i/2)σ|y−e⟩⟨y| + h.c.]`. `Gamma(W_R)` (second quantisation, either statistics) preserves `P` because `W_R` maps site-number operators `n_x` to `n_{Rx}` (the coin rotation is on-site). Hence `Gamma(W_R) H_N(F) Gamma(W_R)^{-1} = H_N(R F R^T)` and `E_N(RFR^T) = E_N(F)`. CHECKED exactly (check.py S2, S3): single-body identity on the cube graph, the 3^3 and 4^3 tori for all 24 rotations with a generic non-symmetric rational F; the many-body identity on the cube graph for N = 2 (all 24 rotations, 112 states) and N = 3 (5 rotations including the 90-degree, 3-fold and face-diagonal ones, 448 states), both statistics, and on the 4x4 plane for N = 2 (480 states, 4 in-plane rotations).

3. **[PROVED + CHECKED] Group average.** `(1/|O|) sum_R R F R^T = (tr F / 3) 1` for every real 3x3 `F` (the representation `3 x 3` of the rotation group contains the trivial representation once, spanned by the identity). In the plane the C4 average of `F` is `a 1 + b J` with `a = tr F/2`, `b = (F_21 - F_12)/2`, and `b = 0` for symmetric F. CHECKED symbolically with sympy (S1) over the 24 (resp. 4) exact rotation matrices.

4. **[PROVED] Jensen step.** By steps 1-3, for symmetric `S` with `tr S > 0`: `E_N(S) = (1/24) sum_R E_N(R S R^T) <= E_N( (1/24) sum_R R S R^T ) = E_N((tr S/d) 1) = (tr S/d) E_N(1)`. (Concavity gives mean-of-values <= value-at-mean; homogeneity gives the last equality.) The planar version uses the C4 average, for symmetric S.

5. **[PROVED] Any frame with `det F > 0` reduces to a symmetric one.** Polar decomposition `F = Q S`, `S = sqrt(F^T F)` symmetric positive definite, `Q in SO(d)`. `H_{QS} = (1 (x) U_Q) H_S (1 (x) U_Q)^{-1}` because `sum_a Q_{ab} sigma_a = U_Q sigma_b U_Q^{-1}`; the coin rotation acts site by site and commutes with `P`, so `E_N(QS) = E_N(S)`. (Block 62 T1(b), landed, is the free-walk form of this relabelling invariance; CHECKED here for N = 1, 2 on the plane: the sector characteristic polynomials of a shear and its coin-rotated copy coincide.) Hence `E_N(F) <= (tr S/d) E_N(1) = c(F) E_N(1)` for every F with det F > 0 and `E_N(1) <= 0`.

6. **[PROVED] Fixed volume.** `det F = 1` and `S` positive definite with `det S = 1` give `tr S >= d` by AM-GM on its positive eigenvalues, with equality iff `S = 1`. (AM-GM for 3 numbers: identity `u1^3+u2^3+u3^3-3u1u2u3 = (u1+u2+u3)*sum of squared differences/2` applied to cube roots; CHECKED symbolically.)

7. **[PROVED + CHECKED] The equal-frame energy is negative.** For `0 < N < n` and a connected graph, `H_N(1)` has zero diagonal (every hop moves a record to a different site, hence changes the configuration, for `L >= 3` and for the cube graph), so it is traceless; it is nonzero (some record has an empty neighbour; the amplitude is `(−i/2)` times a nonzero entry of `sigma_j`, times a sign), so a nonzero traceless Hermitian matrix has a negative lowest eigenvalue. This is block 147's argument, restated. CHECKED (S4): zero diagonal, nonzero entries, N = 1..7 on the cube graph (both statistics), N = 1, 2 on the 4x4 plane; zero iff N in {0, 8}.

8. **[PROVED] Conclusion of (T).** Steps 4-7: `E_N(F) <= c(F) E_N(1) <= E_N(1)`, strict unless `c(F) = 1`; `c(F) = 1` iff `S = 1` iff `F^T F = 1`. For the sea, take `N*` minimising `E_N(1)`: `E_sea(F) <= E_{N*}(F) <= c(F) E_{N*}(1) = c(F) E_sea(1)`. At `N = 0, n` all hops are absent/blocked, so `E = 0` (block 147).

9. **[CHECKED] Exact finite spectra.** Lowest eigenvalue of the hard-core generator from sector-reduced characteristic polynomials (translation sectors on the 4x4 plane; a Z2 rotation sector on the cube graph) with exact real-root isolation (width 1e-30), both composition rules: see check.py S5 for the per-frame lines. Frames: plane `diag(1/2,2)` (l = (2, 1/2)), simple shear `[[1,1],[0,1]]`, `[[2,1],[1,1]]`; cube `diag(1/2,1,2)` (l = (2,1,1/2)), simple shear, `[[2,1,0],[1,1,0],[0,0,1]]`. Densities exact: plane 1/16, 2/16; cube 1/8, 2/8. In every case the isolating intervals show `E_N(F) < c(F) E_N(1) < E_N(1)`. Floating-point sanity (S7, not exact) covers N = 1..7 on the cube graph and N <= 4 on the plane for random (including non-symmetric) frames.

10. **[PROVED + CHECKED] Corollary U (uniform in L).** Let `L` be even, `>= 4`, tile the torus with cells (`2x2x2` cubes; `2x2` squares in the plane) whose internal bonds are torus bonds with the torus orientation; each cell with `k` records and its own bond-once Hamiltonian has ground energy `-eps_k`, `eps_k > 0` for `0 < k < 8` (step 7 on the cell), `eps_0 = eps_8 = 0`. Take the (anti)symmetrised product of cell ground states with `k_c` records in cell `c`, `sum k_c = N`. Each factor lies in the hard-core space, so `<H_N> = <dGamma(h)>`; bonds between different cells change the particle numbers of two cells and have zero expectation in a state with definite cell numbers; bonds inside a cell give the cell energy. Hence `E_N(1) <= -sum_c eps_{k_c}`, and with `k_c in {floor(8 rho), ceil(8 rho)}` (planes: `4 rho`; the numbers of cells at each value are fixed by `sum k_c = N`) at least a fraction of the `n/8` cells (planes `n/4`) is interior (`0 < k_c < 8`), so `sum_c eps_{k_c} >= (n/8) * min over the two adjacent values with positive weight of ...` is extensive in `n` for each fixed `rho` in (0,1); the constant degrades as `rho -> 0` or `1` (not claimed uniform in `rho`). The explicit extensive constant is `(n/8)[(x - floor x) eps_ceil(x) + (ceil x - x) eps_floor(x)]`, `x = 8 rho` non-integer (equal to `(n/8) eps_x` for integer x). With step 8: `E_N(F) - E_N(1) <= -(c(F) - 1) sum_c eps_{k_c}`, uniform in L. CHECKED: `eps_k > 0` for k = 1..7 (cube cell) and 1..3 (square cell) in floating point and exactly through steps 7; the exact plane N = 2 values lie below `2*E_cell(1)` as required (S6).

11. **[CHECKED, same proof] Free sea.** The free-fermion filled-lower-band energy `-<|F s|>` is also a minimum over fillings of a linear function of F, so steps 1-8 give `<|F s|> >= c(F) <|s|>` on any zone grid. This extends block 155's T2/T3 (diagonal at every size; off-diagonal at second order only) to every symmetric or non-symmetric frame of determinant 1 at every size, and gives the strict fall at fixed volume for free. CHECKED in floating point (S8) on 2D and 3D grids, 150 random frames.

12. **[OPEN] What the argument does not give** (first unresolved step):
   - (a) A mass or any `F`-independent rotation-invariant term `W` (block 139's staggered mass on an even torus, or an extra interaction): steps 1-4 give `E(F;W) <= lambda_min(c H_1 + W)` with `c = tr S/d >= 1`. The remaining step is that `g(c) = lambda_min(c H_1 + W)` is non-increasing for `c >= 1`. This is true for the free massive sea (block 155 T3 by direct convexity) but not shown in general here.
   - (b) Nonuniform (q != 0) frame fields: step 1 and a translation-plus-rotation average would give `E(F(.)) <= (<tr F>/3) E(1)` for symmetric positive frame fields (suggested, not checked, and the bond-placement convention of the field must be fixed), but that bounds the energy relative to the uniform mean, not a stiffness.
   - (c) Existence of the thermodynamic limit of `E_N/n` at fixed density, and the actual value of `E_N(1)/n` (only the uniform bound of step 10).
   - (d) Odd L, non-cubic tori (the rotation average needs axis-permuting symmetry) and open boundaries other than the cube graph.
   - (e) The instantaneous ground energy is not a dynamical statement (block 155's same caveat).

## 3. Failing or empty route found

- The literal "2x2x2 torus" with periodic bonds: `T_j = T_j^dagger`, so `S_j = 0`, `H = 0` for every frame, every N, both statistics (CHECKED, S4). The ground energy is identically zero, so it neither falls nor rises. Block 147 requires side at least four for this reason. The nontrivial 2x2x2 object is the bond-once cube (GQ).
- Characteristic polynomials alone do not reach N >= 3 on the 4x4 plane (translation sectors of dimension 280 are too large for exact polynomial arithmetic in this runtime); the general proof covers them, and floating point (S7) agrees for N <= 4.

## 4. What is new relative to the sources

Not new: the Hermitian, concave, minimum-of-linear-functions argument (block 85 T1, for alternation); the free-sea T1-T3 (block 155); the negativity of nonzero finite hard-core sectors (block 147); the relabelling invariance of the walk (block 62 T1(b)).
New here: (i) the use of the full cubic rotation group on the frame argument, which gives `E(F) <= (tr sqrt(F^T F)/d) E(1)`; (ii) the application to the hard-core one-record-per-site generator, all N, both statistics, all sizes of the cubic torus; (iii) every frame, not only diagonal, so the off-diagonal-shear-at-every-size item left open in block 155 is closed for the free sea too (step 11); (iv) the uniform-in-L cell bound; (v) exact finite spectra at the stated densities; (vi) the observation that the periodic 2x2x2 torus is empty.

## 5. What would carry it to Z^3

- The statement for tori of every even side already holds with the uniform bound of step 10; it passes to the infinite lattice as bounds on `limsup/liminf` of `E_N/n` at density `rho`: `e(F) - e(1) <= -(c(F)-1) c(rho)` where `c(rho) > 0` is the cell number of step 10. Existence of the limit needs a subadditivity argument (not given).
- For an F-independent rotation-invariant term (mass), prove monotonicity of `g(c)` (step 12a), for instance through a chiral involution anticommuting with `H_1` and commuting with `W`.
- For slowly varying shear, the stiffness needs the second variation of `E` around the uniform frame at q != 0 (not obtainable from concavity).

## 6. Run record

`python3 check.py`: `TOTAL: PASS=122 FAIL=0`, runtime 319 s (one process, under 1 GB). Output saved in `check_output.log`. Steps 2, 3, 7, 9 are exact (rational/Gaussian-rational arithmetic, sympy characteristic polynomials and real-root isolation); steps 10 (the eps_k numbers), 11 and the S7 lines are floating point and are labelled so. Steps 1, 4, 5, 6, 8 are arguments written out above; check.py verifies their finite instances only.
