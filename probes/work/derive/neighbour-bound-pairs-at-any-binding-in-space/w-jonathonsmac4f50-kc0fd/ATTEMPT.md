# Neighbour-bound pairs at any binding strength: finite-g axis sums, thresholds and the 1/g^2 term

Task `J:derive:neighbour-bound-pairs-at-any-binding-in-space:a1`. Worker: Claude Sonnet 5.5, same model family as the supervisor's own block 142; nothing here is refereed by another family.
Files: `check.py` (34 checks; about 2.5 minutes of CPU, 12 minutes of wall time on the heavily loaded host at load average 60 to 85, 6 minutes at lower load), `RECOVERY_STATUS.json`, this note.

## Plain-language summary

Block 142 studies two records that obey the walk, may not share a site, and attract each other only when they are neighbours, with a "possibility shift" of strength `g`. At very large `g` it finds that the pair's curvature of `E^2/2`, added over the three axes, is at most 3/2, while a free record has 3 (one along each axis). It then concludes that no rest level can have curvature one along all three axes.

I computed the same quantity at finite `g`, using the exact lattice Green function of the pair instead of an expansion in `1/g`.

- **Answer to (a): the conclusion does not survive to finite `g`.** For the covariant shift `M = Pi_pm + (1/4)|S><S|` (spin +-1 value 1, singlet value 1/4, the other value 0) there is an exactly known three-fold level with `E = g`. Its axis sum falls from above 3 near the binding threshold to below 3 at larger `g`, and equals exactly 3 at `g* = 3.6601173879`. At that point a unit vector of the level has curvature weight 1 along each of x, y and z. This is a floating-point lattice-integral result, cross-checked three ways; it is not an interval-certified proof.
- **What stays true.** For coin-blind `M = 1` the axis sum never exceeds about 1.52 at any `g` on the grid (1.5211 in `check.py`, 1.5213 on a denser development grid). For the pure spin +-1 shift `M = Pi_pm` alone it stays below 3 (about 2.87 at the threshold). For the single-ray shifts scanned in development (`cos^2 theta` = 0, 1/4, 1/2, 3/4, 0.9, 1) the largest axis sum on the grid is 1.52, 0.50, -0.50, -1.25, -1.49, -1.60, i.e. close to the leading-order values 3/2, 1/2, -1/2, -3/2, .... In a random sample of 100 covariant shifts it stays below 1.7 for `E >= 26` (1.82 in a 150-draw development run). The excess over 3/2 comes from the `1/g^2` term, which can be large when two coin values of `M` are close.
- **Why the sum is big there.** The level repels from, or avoids, the nearby singlet-channel levels. That is a level-repulsion effect at moderate coupling, not a smooth speed. Nothing here is a speed, an inertia or a fall coefficient.

## 0. What I read and how sources were used

- I read in full `docs/MINIMAL_AXIOMS_2026-06-29.md` (main checkout `a77a3449c9`, sha256 `93af34cf…`) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`. The four axioms (Lattice, Qubit, Admissibility, Record) say nothing about a walk, a neighbour term, or a rate. Everything below the axioms is supplied by the lane. No approved primitive is used.
- Block 142 as landed on main: sha256 `fb9b11df…`. The PR snapshot at the task's head `5c7c52847e` has a different text (`350fd6eb…`), and the landed text controls. Key lines of the landed note: the setting and the covariant family (`…2026-09-25.md:43`, `:103`), the energy-squared curvature definition (`:47`), the table of leading-order axis sums (`:112`), the conclusion (`:126`), the falsifier "a rest level with an axis sum above 3/2" (`:238`), and the stated open item "moderate binding" (`:193`, `:200`).
- Blocks 54 (the walk `H1 = sum_j sigma_j D_j`, `…2026-09-21.md:26`) and 78 (one record per site) and block 115 are on main and were consulted for definitions only. Their notes are cited in 142 as the source of the walk and of exclusion.
- **Source mismatch to report.** The task text calls blocks 115, 133, 139 and 142 (PRs 9157, 9191, 9201, 9227) "OPEN". `gh pr view` shows all four CLOSED, and the notes for 115, 133, 139 and 142 are present on the main checkout. I used the landed text. Blocks 133 and 139 are not used.
- **Prior attempt.** The directory `deferred-20260925-nearest-neighbour-finite-coupling/w-macbookpro9927a-jce96` (Opus 5.5, same family, unrefereed) did the coin-blind case with an expansion in `1/g`. I read it only after fixing my own plan. My route differs (exact resolvent, all `g`, every covariant shift). Its coin-blind `1/g^2` coefficients are reproduced here independently (step 7).

## 1. Statement attempted

Setting (supplied by the lane, from block 142 as landed). Two records of block 54's walk on Z^3, relative coordinate `r != 0` (exclusion), total wave vector `K`; relative generator `<r|H2|r+-e_a>` as in block 142; neighbour term `V = g sum_{r=+-e_a} |r><r| (x) M(r)`, `M(e_z)` hermitian on the two coins, covariant under the bond's rotations and the records' exchange (five real numbers); `M(r)` on the other bonds by the cubic rotations. Energy-squared curvature matrix `W(n)` of a rest level: the `K^2` form of `E^2/2` on the level.

To decide:

- (a) Does the axis sum `sum_d W_dd` stay below 3 for every `g`, or is there a `g` and a covariant `M` with a rest level of weight one along all three axes?
- (b) Binding thresholds and ground channels as functions of `g`.
- (c) The next, `1/g^2`, term of the axis sum.

## 2. Steps

**S1. PROVED.** *Reduction to the bond space.* Let `H_ex` be the compression of `H2(K)` to `r != 0`; `||H_ex|| <= ||H2|| <= 2 sqrt 3` because the symbol is `sigma.s(p1) (x) 1 + 1 (x) sigma.s(p2)` with `|s| <= sqrt 3`. For real `|E| > 2 sqrt 3` let `G1(E,K)` be the 24 x 24 block of `(E - H_ex)^{-1}` on the six bond positions x four coins. It is hermitian and positive definite. If `(H_ex + gM) psi = E psi` with `psi` in `l^2`, then `phi = psi|_bond` satisfies `B(E,K) phi = 0` with `B = G1^{-1} - gM`, and conversely. (Proof: `psi = (E - H_ex)^{-1} P gM phi`; restrict to the bond.)

**S2. PROVED.** *Monotonicity and thresholds.* `dB/dE = G1^{-1} P (E - H_ex)^{-2} P G1^{-1}` is positive definite, so each ordered eigenvalue of `B` increases strictly in `E`, and from the edge to +infinity it goes from `beta_j(2 sqrt 3^+)` to `+infinity`. Hence (i) each branch has at most one root, (ii) the number of bound levels above the continuum at `K = 0` equals the number of negative eigenvalues of `G1^{-1}(2 sqrt 3^+) - gM`, i.e. of eigenvalues of `g G1^{1/2} M G1^{1/2}` exceeding 1 (Sylvester), (iii) for `M >= 0` each level `E_k(g)` increases with `g` (`dE/dg = <phi|M|phi> / <phi|dB/dE|phi>`), and (iv) the threshold of the channel with eigenvalue `tau` is `g_th = 1/tau`. For `g M` of either sign the lower edge maps to the upper edge: the parity `(-1)^{|r|}` gives `Spec(H_ex + gM) = -Spec(H_ex - gM)` at every `K`, and `E E''` is invariant. So `g > 0` and all `M` cover everything. Assumed: `G1(2 sqrt 3^+)` is finite (checked numerically by extrapolation).

**S3. PROVED (derivation) / CHECKED (inputs).** *Weight formula.* At `(E0, K=0)` let `N` be the null space of `B0`, `N_E = N^† (dB/dE) N`, and for axis `d` the series `B(E0, t e_d) = B0 + t B_d + (t^2/2) B_dd + ...`. If `N^† B_d N = 0` (checked: below 1e-12 in every level reported), the Schur complement on `N` gives, for the roots near `E0`,
`E - E0 = -(t^2/2) N_E^{-1} C_dd`, with `C_dd = N^† (B_dd - 2 B_d B0^+ B_d) N`,
where `B0^+` is the pseudo-inverse on the complement of `N`. Since `E' = 0`, `d^2(E^2/2)/dt^2 = E0 E''`, so `W_d = -E0 N_E^{-1/2} C_dd N_E^{-1/2}` (hermitian in the `N_E`-orthonormal basis). The derivatives of `B` are lattice integrals of `R`, `R H' R`, `R H'' R + 2 R H' R H' R` with `R = (E - H)^{-1}`, after removing the origin by `G1 = Gpp - Gp0 G00^{-1} G0p`. Remainders are higher order by analyticity of `B` in `(E,K)` outside the continuum.

**S4. PROVED (exact algebra, sympy; `check.py` A1-A2).** *The covariant family.* The hermitian 4 x 4 matrices commuting with the quarter turn about the bond and with (half turn across it x exchange) form a real space of dimension 5, equal to `{mu Pi_pm + a|S><S| + b|t0><t0| + z|S><t0| + conj(z)|t0><S|}`. The six-bond assignment is covariant under all 24 proper rotations (A8, checked with spinor lifts).

**S5. PROVED (exact algebra, sympy; A3-A7).** *The dark triplet.* Take the 12 states supported on the six bond positions with both coins of spin +1 (or both -1) along the bond axis. The hop equations at every site except the origin have a null space of exact dimension 3. These three vectors are exchange-antisymmetric (a fermion triplet), and their hops into the origin also vanish. Since `M` acts as `mu_pm` on the spin +-1 plane, `(H_ex + gM) psi = g mu_pm psi` for every `g`. The continuum is `[-2 sqrt 3, 2 sqrt 3]` (A7: top symbol eigenvalue `2 sqrt 3` at `K = 0`, and the compression and the finite-rank bond term change only discrete spectrum). So for every covariant `M` the triplet is a bound level with `E = g mu_pm` exactly when `g mu_pm > 2 sqrt 3`, and its binding threshold is exactly `g mu_pm = 2 sqrt 3`. This is the exchange-antisymmetric `omega = 0` level of block 142's rows, now exact in energy.

**S6. CHECKED (floating-point lattice integrals; B1, B2).** *The engine is right.* (i) The trapezoid sums converge exponentially (at the smallest `E - 2 sqrt 3 = 0.03` used, `N = 90` vs 120 changes `G1` by 2e-11 and its `K`-second derivative by 2e-9). (ii) Coin-blind `M = 1`, `g = 6`: all 24 bound rest levels agree with brute-force diagonalisation of the `|r_i| <= 5` box to 2e-7.

**S7. CHECKED (B3-B5, B9).** *Large `g` reproduces block 142 and fixes the next order.* Fits `W(g) = W2 + W4/g^2 + W6/g^4` over `E` in `[25, 73]` (sector assigned by the exchange operator):

- **Block 142's leading values are reproduced** for coin-blind `M=1` (7/10, 3/2, -1/2, -17/10 fermions; 3/2, 1/2, -5/2 bosons), for `M = Pi_pm` (3/2, -1/2 fermions; 1/2 bosons), and for the single rays `(3 - 8x)/2`, `x = cos^2 theta`.
- **Coin-blind `W4`:** fermions 6/5; -21/2, 3/2, 3/2; -12; 123/10; bosons -5/2; -7; 31/2. This agrees with the earlier finite-coupling attempt's `7/10 + 6/(5g^2)`, `3/2 + {3/2, 3/2, -21/2}/g^2`, `-1/2 - 12/g^2`, `-17/10 + 123/(10 g^2)`, `3/2 - 5/(2g^2)`, `1/2 - 7/g^2`, `-5/2 + 31/(2g^2)`.
- **New: `M = Pi_pm`,** fermions `3/2 + 6/g^2` (the dark triplet), `-1/2 - 12/g^2`; bosons `1/2 - 7/g^2`.
- **New: single ray `M = |psi><psi|`,** `x = cos^2 theta`, `W2 = (3-8x)/2`: fermion A1 `W4 = -21/2 - 18x + 48x^2`; fermion E (two states) `3/2 - 30x + 48x^2`; boson (three states) `-5/2 - 30x + 48x^2`. Identified as rationals from fits good to about 1e-2, at `x = 0, 1/4, 1/2, 3/4, 1`.
- **New: the dark triplet with a second coin value.** For `M = mu Pi_pm + a|S><S| + b|t0><t0|`, `rho = a/mu`:
  `W_sum = 3/2 + (6 + 4 rho/(1-rho)) / (g mu)^2 + O(g^-4)`.
  This is independent of `b`. It was matched at `rho = -1/2, 0, 1/10, 1/4, 1/2, 3/4, 9/10` (and `mu = 0.7`) to 3-4 digits. It diverges as `rho -> 1`, which is the failure of block 142's fixed-gap hypothesis. It is an identification, not a derivation.

So block 142's "at most 3/2" is a leading-order statement. Already at next order the dark triplet exceeds it by `6/g^2` even for `rho = 0`.

**S8. CHECKED (B6-B8).** *Binding thresholds* `g_th = 1/tau` (S2 (iv)), with `G1(2 sqrt 3)` extrapolated in `sqrt(E - 2 sqrt 3)` (degree 8 vs 10 differ by 1.2e-5; thresholds good to about 1e-4). Sector F = exchange-antisymmetric, B = symmetric; multiplicities in brackets:

| shift | thresholds `g_th` |
|---|---|
| coin-blind `M = 1` | 1.1863 F(3), 1.4294 B(3), 1.7321 F(3), 2.4831 B(6), 2.5841 F(1), 2.8633 B(3), 2.9227 F(2), 3.4641 F(3) |
| `Pi_pm` | 1.1863 F(3), 2.4831 B(6), 3.4641 F(3) |
| singlet ray (`x=1`) | 1.4294 B(3), 1.7321 F(3) |
| `t0` ray (`x=0`) | 2.5841 F(1), 2.8633 B(3), 2.9227 F(2) |
| ray `x = 1/2` | 1.9069 B(3), 2.0740 F(1), 2.1751 F(2) |

The last fermion triplet is `2 sqrt 3 = 3.4641`, the dark triplet of S5 (exact). 1.7321 agrees with `sqrt 3` to the accuracy of the extrapolation (reading only). The order of the thresholds equals the order of the large-`g` ladder (`omega = 5, 5, 4, 2, 1, 1, 1, 0` for coin-blind). So the ground channel (the first to bind, and the top level at every `g`) is the fermion triplet at `g_th = 1.1863` for coin-blind and `Pi_pm`, the symmetric triplet at 1.4294 for the singlet ray, and so on; the dark triplet is always the last.

**S9. CHECKED (C1-C8, D1-D3).** *The finite-`g` question (a).*

- C1/C2. For `M = Pi_pm` alone the dark triplet's axis sum falls from 2.78 at `E - 2 sqrt 3 = 0.03` to 2.15 at 0.57. Closer in, development runs (N up to 240) gave 2.8077, 2.8371, 2.8530, 2.8615 at 0.02, 0.01, 0.005, 0.0025, rising slowly towards about 2.87. It stays below 3.
- **The counterexample.** `M(e_z) = Pi_pm + (1/4)|S><S|`. The dark fermion triplet (`E = g` exactly, S5) has axis sum 3.1695 at `g = 3.60` and 2.8634 at `g = 3.72` (C3). The root is `g* = E* = 3.6601173879` (C4).
  - At `g*`: null space 3-dimensional, exchange-antisymmetric, first-order `K` terms 5e-16, axis-sum matrix equal to `3 * identity` on the level.
  - A unit vector of the level has weights `(1, 1, 1)` along `(x, y, z)` to 1e-9. The per-axis matrices have eigenvalues `0.33805, 0.33805, 2.32389`.
  - Isolation (C6): the other bound levels are at 4.27397 (x6) and 4.7118 (x3), at least 0.61 away. The edge of the continuum is 0.196 below.
- **Independent check 1 (C7).** Finite differences of the exact bound energy, by root-finding `det B(E, K = (0,0,t)) = 0`, give `E* sum E''_i = 2.99650` (t = 0.05), `2.98610` (t = 0.1), and `2.99997` after removing the `t^2` term. That is the trace of `W_z`, equal to 3 when the sum is 3. This does not use S3.
- **Independent check 2 (C8).** Brute-force diagonalisation of the `|r_i| <= 6` box: the triplet sits at 3.660117 (K = 0) and at 3.660578 (x2), 3.663275 at `K = (0,0,0.1)`, matching the resolvent roots to 3e-5.
- A second example with a generic `M` was found in a development run and is not in `check.py`: `M(e_z)` with spin +-1 value 0.6021, singlet value 0.0467, t0 value -0.4362 and singlet-t0 mixing 0.0377 + 0.1996i; the triplet at `g* = 5.8747`, `E* = 3.5372` has axis sum 3. It was confirmed by finite differences and a box diagonalisation (roots 3.537241, 3.537747 x2, 3.540449).
- **Random family sample (D1, D2).** For 100 draws of `(mu_pm, a, b, z)` on the unit 5-sphere: every rest level with `E >= 26` has axis sum at most 1.693 (1.566 for `E >= 40`, 1.533 for `E >= 60`; 1.82 in a 150-draw development run). Levels well separated from the rest of the spectrum reach 3.53 (4.2 in the 150-draw run), at `E - 2 sqrt 3 = 0.03`; the largest value for `E >= 11` is 6.6. Values of order 10 to 30 occur for levels within a few 1e-3 of another level of a coupled symmetry; those are level-repulsion divergences and are not meaningful weights.
- **Coin-blind (D3).** Largest axis sum over every rest level and the whole grid (`E - 2 sqrt 3` from 0.03 to 70): 1.5211.

**S10. READING (interpretation).** The curvature in the counterexample is the repulsion between the dark triplet and singlet-channel levels at distance of order one. For `rho = 1/4` the leading formula `3/2 + 7.33/g^2` gives 2.05 at `g = 3.66`, so the example is outside the asymptotic regime. As `rho -> 1/2` the singlet fermion triplet binds exactly at `g = 2 sqrt 3` (`sqrt 3/rho`), at the same point as the dark triplet; the axis sum then grows like `1/(g - 2 sqrt 3)`. Also, the quadratic form is accurate to about 2% for `|K| <= 0.2` (C7). I make no claim about speeds, inertia, fall or stability.

## 3. First failing / unresolved step

Nothing failed for (a); it is decided negatively by an explicit finite-`g` covariant `M`. Unresolved, in order:

1. **S9 is not interval-certified.** `g*` and the equal-weight vector rest on floating-point lattice integrals (converged, three independent evaluations). A rigorous version needs an enclosure of the lattice integrals (S9's two margins, 3.17 vs 2.86, are large compared with the observed 1e-9 quadrature error, so it looks routine but is not done).
2. **S7's closed forms are numerical identifications.** In particular `6 + 4 rho/(1-rho)` and the three ray polynomials in `x`; the exact route is fourth-order degenerate perturbation theory on the 24-dimensional bond space with symbolic `rho`, `x`.
3. **(b), exact thresholds:** only `2 sqrt 3` (the dark triplet) is exact; the others are numerical (about 1e-4). `sqrt 3` for the singlet fermion triplet is a reading.
4. **(c) for general `M`** with several coin values and an S-t0 mixing `z != 0`: not computed beyond the dark triplet (`z = 0`).
5. **The sup of the axis sum over the covariant family** is not determined; the sample shows it exceeds 3 at moderate binding and stays near 3/2 for `E >= 26`.

## 4. What is new (relative to the sources)

- Not new: block 142's leading-order table, the coin-blind `1/g^2` coefficients (earlier attempt), the box check.
- New and exact: the covariant family's dimension and the dark fermion triplet `E = g mu_pm` with threshold exactly `2 sqrt 3` for every covariant shift (S4-S5); the Birman-Schwinger/monotonicity structure for this problem (S1-S2).
- New and numerical: the finite-`g` counterexample (S9); the threshold tables (S8); `W4` for `Pi_pm`, single rays and the dark triplet with a second coin value (S7); the sup behaviour for coin-blind and `Pi_pm` (S9).

## 5. What would finish it

An interval enclosure of the lattice integrals at `g*` (or an exact evaluation of the dark triplet's second-order sum, which involves only `G1(E = g)`); a symbolic fourth-order effective generator to prove S7's coefficients; and a statement of the exact region of `(rho, g)` in which the dark triplet's axis sum exceeds 3 (here: from the threshold `2 sqrt 3` up to a `g*(rho)`, with `g*(1/4) = 3.6601`).
