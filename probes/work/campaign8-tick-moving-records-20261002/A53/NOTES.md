# A53 notes (cluster rivals to the parton under A51's short rules; exploration only, nothing adopted)

Started 2026-10-04 ~08:35. Owner decisions: exact turns (Q3, 4 Oct), reach beyond six neighbours = exploration (22).
Rules used: A51 rules51_L.npz keys B4_r4 (|d|^2 <= 4 classes + 8 star four-spin terms) and B4_inner (finite reach,
components < L/2), J_NN = 1, dual frame (states and operators in the Klein-dual frame of A44/A49).

## 0. Plan
- a53lib.py: wrapped-rule term builder (bilinear class sums + star four-spin terms regrouped per star centre),
  S^z = 0 sector with optional spin-flip reduction (singlets are flip-even for N = 0 mod 4), numba matvec with
  Lin two-table ranking, pair correlations, parton amplitudes.
- Task 1: 16-site GS anatomy. Task 2: exact cluster products on 6^3/8^3/10^3. Task 3: 24-site Lanczos (tilted cluster
  2*{a+b+c = 0 mod 3}, the only index-24 sublattice of 2Z^3 without NN doubling, up to symmetry).

## 1. Task 1: 16-site ground state anatomy (t1_16.py, 90 s, 188 MB) -- EXACT
- Code checks: star-grouped kernel = generic four-set kernel = flip-reduced sector, all to 1e-6 in E0/N; E0/N -2.334578
  (L6 rule) and -2.302792 (L8 rule) = A51 fwd16; parton <H>/N -1.77524 / -1.76626 = A51 fwd16 exactly; overlap 1.98e-4.
- Wrapped structure of the 16-site cluster (lattice (2,2,0),(2,0,2),(0,2,2)): pair types 001x1 (48 pairs), 011x2 (48),
  111x4 (16), 002x6 (8).  All six (002)-type displacements of a site land on ONE partner: the (002) pairs are a perfect
  matching, each carrying 6 J(002) = 2.2 (in s.s units).
- GS (both rules): <s.s> = -3.000 on every (002) pair and 0.000 on EVERY other pair type; S = 0 (sum C = 1e-15).
  => the 16-site GS is EXACTLY the product of singlets on the 8 wrapped (002) pairs.  Energy check:
  0.373 * (-9) + Dm0 0.119 * 5.196 + Dm1 0.190 * 2.121 = -2.335 (only Dm sets = two (002) dimers survive).
- Cube singlet weight 0.055 and plaquette 0.125 = exactly the random-state values (14/256, 2/16): NO cube/plaquette
  structure.  Control (parton, same cluster): cubes 0.347, plaquettes 0.438, NN <s.s> -1.089, (002) +0.752.
- Reading: the 0.54-0.56/site gap is a wrapping artifact of this cluster (6-fold (002) coupling on a perfect matching).
  On 6^3+ tori a (002) pair carries J(002) once; the analogous (002)-dimer covering gets only ~ -0.55/site there.

## 2. 24-site cluster setup (bench24.py, 12.7 s, 229 MB)
- Tilted cluster, lattice 2(1,-1,0), 2(0,1,-1), 2(1,1,1) (index 3 in 2Z^3; every index-24 sublattice of 2Z^3 holds a
  vector of length^2 <= 8, and this one is the only class without NN doubling).  Parton (A49 mf_state, APBC): MF gap
  4.00 at half filling -> closed shell, non-degenerate.  (Twist 0: gap 0, open shell.)
- Wrapped pair types: 001x1 72, 011x1 72, 011x2 36 (mixed-sign FDs doubled), 002x3 24 ((002) partners form 8
  TRIANGLES x, x+2e1, x+4e1, each bond 3 J(002)), 111x2 12, 111x3 24, far 36.  Same shortest wrap (|(2,-2,0)|^2 = 8)
  as the 16-site cluster, so wrapping artifacts persist, but (002) now forms frustrated triangles, not dimers.
- Flip-even sector 1,352,078 states; star-kernel matvec 1.9 s; parton amplitudes (1.35M 24x24 dets) 5.9 s.
- Parton exact <H>/N = -1.748825 (L6 B4_r4 rule), var/N 0.110.
- Lanczos (random start) batch 1: E0/N -2.01560 after 120 steps (resid est 0.17), E1/N -2.0080 close above.

## 3. Factorization control (t2_check.py, 1.1 s) -- EXACT + CHECKED
- 3x3x2 open region (18 sites), clusters of 8 and 10, random singlets: exact <H> = factorized formula to 4e-15
  (18 four-sets split 2+2, 40 split 3+1, 20 intra), both rules.  Negative control (S = 1, m = 0 on both clusters):
  formula off by 0.017-0.018, as it must be.
- For the block tilings 2x1x1, 2x2x1, 2x2x2 of Z^3 the star four-sets never split 2+2 (checked by enumeration in
  t2_prod: n_inter_terms), so a block-singlet product gets exactly its intra-block energy.

## 4. Parton / reference energies under the rules (ref51.py on A51's VMC samples)
| L | parton B4_inner | parton B4_r4 | Neel .05 B4_inner | VBS B4_inner |
| 6 | -1.72681(10) | -1.72841(11) | -1.72410(34) | -1.50202(117) |
| 8 | -1.69469(11) | -1.71461(13) | -1.69109(46) | -1.50000(118) |
| 10 | -1.66262(14) | -1.72022(16) | -1.65891(42) | - |

## 5. Task 2 block-singlet products, 6^3, B4_inner rule (t2_prod.py, 3.3 s, 128 MB) -- EXACT
| block | n | E/N (product = intra GS / n) | minus parton (-1.72681(10)) |
| 2x1x1 (columnar dimers) | 2 | -1.50000 | +0.2268 (A51 VMC VBS -1.50202(117): agrees) |
| 2x2x1 (plaquettes) | 4 | -1.61239 | +0.1144 |
| 2x2x2 (cubes) | 8 | -1.65459 | +0.0722 |
| 2x2x3 | 12 | -1.66065 | +0.0662 |
- n_inter_terms = 0 for all four tilings: no star four-set splits 2+2 across blocks, so self-consistency is trivial
  and the restricted-rule singlet GS is the optimal block state.  Margin shrinks with block size, slowly.

## 6. 8^3 block products (B4_inner L8 rule; t2_prod 10.3 s, 172 MB) -- EXACT; delta = 0 block partons
| block | n | E/N | minus parton (-1.69469(11)) |
| 2x2x1 | 4 | -1.59654 | +0.0982 |
| 2x2x2 | 8 | -1.63287 | +0.0618 |
| 2x2x4 | 16 | -1.64353 | +0.0512 |
- n_inter_terms = 0 again.  Projected block partons (delta = 0, t2_cubeparton): dimer and plaquette parton = block GS
  exactly (overlap 1.0000); cube parton overlap 0.994 (6^3 rule) / 0.9937 (8^3), E/N -1.65137 (6^3) / -1.63001 (8^3).

## 7. Wrap conventions on small clusters (t3_once16, 4.6 s)
- 'pair-once' (each cluster pair once, shortest displacement; A51's torus convention) on 16 sites: E0/N -4.799, parton
  -3.873, gap 0.93/site, overlap 0.716.  But the parton's own energy moves from -1.78 (wrapped) to -3.87 because
  16 sites keep only 3 FD bonds and 0.5 (002) bonds per site (lattice: 6 and 3): pair-once on 16 sites is a much
  less frustrated rule, not a faithful small version.  Wrapped convention keeps the per-site term count: parton
  -1.775 (16), -1.749 (24) vs -1.728/-1.715/-1.720 (6^3/8^3/10^3, B4_r4).  => keep the wrapped convention for 24.
- Star four-sets: 16 sites 428 distinct of 560 (duplicates), 24 sites 804 of 840.

## 8. All block products (t2_blocks, 108 s / 92 s, 139 MB; t2_prod 233 at 6^3 59 s: n_inter_terms 0) -- EXACT
E/N of block-singlet products (restricted-rule singlet GS / n); parton from A51 VMC samples (ref51):
| rule | 2x2x2 | 2x2x3 | 2x2x4 | 2x3x3 | parton | best block - parton |
| L6 B4_inner | -1.65459 | -1.66065 | -1.66582 | -1.66593 | -1.72681(10) | +0.0609 |
| L8 B4_inner | -1.63287 | -1.63889 | -1.64354 | -1.64408 | -1.69469(11) | +0.0506 |
| L10 B4_inner | -1.61240 | -1.61719 | -1.62103 | -1.62121 | -1.66262(14) | +0.0414 |
| L6 B4_r4 | -1.65867 | -1.66425 | -1.66942 | -1.66908 | -1.72841(11) | +0.0590 |
| L8 B4_r4 | -1.64623 | -1.65229 | -1.65725 | -1.65773 | -1.71461(13) | +0.0569 |
| L10 B4_r4 | -1.64938 | -1.65554 | -1.66069 | -1.66101 | -1.72022(16) | +0.0592 |
(10^3 B4_inner also 2x2x1 -1.58052.)  Under B4_inner the margin shrinks with L (rule changes with L); under the fixed
short rule B4_r4 it is flat at ~0.058.
- Dressed-cube estimate (ARGUED, not a bound): interface gain dE = E(2x2x4) - 2E(2x2x2) = -0.17..-0.18 per cube
  pair; E(222)/8 + 3 dE/8 = -1.7219 (L6 inner) / -1.6969 (L8) / -1.6642 (L10); B4_r4: -1.7232 / -1.7123 / -1.7172.
  Within -0.005..+0.002 of the parton: a dressed cube crystal is a near-tie competitor (second-order additivity,
  3-cube four-spin channels and higher orders not included).

## 9. 24-site Lanczos, random start (lz24 x5 batches, 246 s each, 175-191 MB) -- EXACT upper bound
- Pass 1 capped at m = 300 (slow convergence: second Ritz value within 0.0008/site of the first, dense low spectrum);
  pass 2 reproduced every alpha (checked to 1e-9).  Reconstructed vector: <H>/N = -2.0167759 (variational upper bound
  on E0), residual |H psi - E psi| = 0.020 (total-energy units; E_total = -48.4).
- Parton <H>/N -1.748825 => gap >= 0.268/site.  |<psi|parton>|^2 = 4.4e-11: the low state lies in a symmetry sector
  the parton does not occupy (parton-start Lanczos queued to get the lowest state in the parton's own sector).

## 10. VMC block-modulated partons (vmc53, 266 s, 119 MB), 6^3, cube blocks
| delta | E/N B4_inner | E/N B4_r4 | samples |
| 0 (exact, t2_cubeparton) | -1.65137 | - | - |
| 0.6 | -1.69543(39) | -1.69739(41) | 16,978 |
| 1 (A51 parton) | -1.72681(10) | -1.72841(11) | 34,138 |
Controls: Casimir estimator max dev 2.4e-11 (exact singlet), drift 2e-13, MF gap 3.02 (closed shell).
| 0.3 | -1.66359(45) | -1.66677(44) | 16,956 |   (vmc53 266 s, 112 MB; MF gap 3.08; drift 1e-12)
- Cube-modulated family is monotonic so far: -1.6514 (0) > -1.6636 (0.3) > -1.6954 (0.6) > -1.7268 (1).
- 09:27 an24 rerun SKIPPED (1-min load 10.1 from desktop apps, not a numeric job); chain retrying every 30 s.

## 11. 24-site low state anatomy (an24, 40 s, 454 MB) -- EXACT for the reconstructed vector
- Unit translations: <T_e1> = <T_e2> = <T_e3> = -0.9994 (low state) vs +1.000000 (parton) => different momentum
  sector; overlap 4.4e-11 is a symmetry zero.  S check 2e-6 (singlet up to Lanczos residual).
- <s.s> by wrapped pair type (low state / parton): 001x1 +0.032 / -1.055; 002x3 -0.203 / +0.500; 011x1 +0.057 / +0.402;
  011x2 -0.971 / +0.636; 111x2 +0.019 / -0.285; 111x3 -0.106 / -0.378; far -0.007 / -0.315.
- Energy decomposition per site (coef * <op>/N), low state: NN +0.095, FD 0.768*(-2.741) = -2.105, (002) -0.227,
  (111) ~0, four-spin total ~ +0.21.  Parton: NN -3.166, FD +2.39, (002) +0.56, four-spin ~ -1.53.
  => all of the low state's advantage comes from the FD class, carried by the 36 wrap-DOUBLED mixed face diagonals
  (-0.97 each, coupling 2*0.768); NN bonds are uncorrelated; it pays for the four-spin terms the parton gains on.
- Singlet weights (low state / parton): cubes 0.107 / 0.352, plaquettes 0.142 / 0.436 (random 0.055 / 0.125);
  (002)-triangle S=1/2 weight 0.601 / 0.250 (random 0.5).  Not built from local cube/plaquette singlets.
- Cube-singlet product placed on the 24-site cluster: <H>/N -1.63276 (open cube -1.65867; wrap costs +0.026);
  overlap with the low state 0.0000, with the parton 0.1615.
- Reading (ARGUED): on Z^3 every FD pair carries J2 once and the FD graph is two FCC lattices (frustrated); the
  24-site doubling turns 36 FD pairs into a 3-regular network of 1.54 bonds that can be nearly singlet-paired.
| 0.85 | -1.72130(19) | -1.72268(20) | 16,684 |   (266 s, MF gap 3.24, Casimir dev 2.8e-11)
- Cube-modulated family at 6^3 (B4_inner): -1.6514 (0), -1.6636 (0.3), -1.6954 (0.6), -1.7213 (0.85), -1.7268 (1).
  Monotonic; delta = 1 is stationary by symmetry (shifting the tiling maps delta -> 1/delta) and is the minimum:
  E(0.85) - E(1) = +0.0055(2) (27 sigma).  Roughly quadratic, b ~ 0.24 in (1 - delta)^2.

## 12. Parton-start Lanczos with translation symmetrizer (lz24 parton, 2 batches, 247 s, ~185 MB)
- Operator (prod_a (2 + T_a + T_a^-1)/4) H, start = parton: converged (resid 2.4e-4) to Ritz/N -2.0145030, next
  -2.00697, -2.00573.  But |<parton|Ritz_0>|^2 = 1.6e-10 and |<parton|Ritz_1>|^2 = 8e-6: rounding leaked in a k = 0
  state of ANOTHER point-group irrep (a k != 0 state would be scaled by <= 0.75).  So: a translation-invariant
  singlet-sector state at -2.0145/site exists, distinct in symmetry from the parton.  The parton's own irrep is
  isolated next with the point-group projector (lzpg.py).

## 13. 8^3 cube-modulated parton (vmc53 8 222 0.6; 267 s, 190 MB; 3,614 samples; MF gap 2.48; Casimir dev 4e-11)
- delta 0.6: E/N -1.66823(36) (B4_inner), -1.68353(43) (B4_r4); delta 0 exact -1.63001; parton -1.69469(11) /
  -1.71461(13).  Same monotonic picture as 6^3: +0.0265 above the parton at delta 0.6.
- 6^3 plaquette-modulated parton (block 2x2x1), delta 0.6: -1.69058(35) (B4_inner), -1.69231(36) (B4_r4); 16,693
  samples, 267 s, 100 MB, MF gap 2.74, Casimir dev 4e-11.  Between the plaquette product (-1.61239) and the parton.

## 14. 24-site point group (lzpg setup; first 3 attempts stopped at an assertion, 9 s each)
- Cluster point group D3d (coordinate permutations x {+-1}).  Exact term-list check: the rule is invariant under the
  6 PROPER rotations (D3) and not under inversion / mirrors (four-spin pairing-weight defect 0.0027): the rule is
  covariant under proper turns only (A49 four-spin terms are averages over the 24 proper rotations).
- Parton expectation values of the D3 elements: 1 (e), 0.6866 (both C3, two C2), 1 (third C2) => the parton is NOT
  a D3 eigenstate (the APBC twist is not C3-symmetric on this cluster): weights A1 0.791, E 0.209, A2 0.000.
  => the k = 0 state at -2.0145 with 1.6e-10 overlap is most plausibly A2 (ARGUED from the zero A2 weight).
- Restarted as an A1-projected Lanczos (P_A1 D H, start = normalized A1 part of the parton).

## 15. A1-sector Lanczos (lzpg, P_A1 D H; 2 batches 242 s + 18 s, 205 MB) -- EXACT upper bound
- Kept group D3 (proper rotations); matvec invariance 4e-15; |P_A1 D p|^2 = 0.791036 = A1 weight (consistent).
- Ritz/N after 110 steps: -2.00727, -2.00535, -2.00188 (resid est 0.33, not converged): the lowest k = 0 A1 state lies
  at or below -2.0073/site (k != 0 components are scaled by D <= 0.75, other irreps by 0, so this Ritz value can only
  be A1, k = 0).  Gap to the parton >= 0.258/site INSIDE the parton's main sector.
- |<p_A1|Ritz_0>|^2 fell 6.5e-3 (step 10) -> 9.5e-5 (20) -> 2.7e-5 (60) -> 6.2e-6 (110) => parton overlap
  <= 0.791 * 6.2e-6 = 4.9e-6 and falling.  At step 10 the parton's A1 part was 98% one Ritz vector at -1.760/site:
  the parton sits ~0.26/site above the bottom of its own sector and reaches it only through tiny components.
- Wrap-up 10:00.  Queue empty; NUMLOCK released by run.sh.
- 10:01 a redundant 3rd A1 batch re-ran from scratch after DONE (no done-guard in lzpg); its checkpoint deleted. Queue empty.
