# Independent referee report: SIGN-1

## Verdict

**CONFIRMED WITH CORRECTIONS.**  The ungauged, global-Spin(10) matter
Hamiltonian has a genuine Kramers-class sign-free subfamily.  The exact
`lambda1 = 0`, `lambda2 != 0` point already establishes the fixed SIGN-FREE
reading for the explicitly allowed ungauged reduction.  The wider numerical
cone is supported, but the worker's write-up and filtered cluster implementation
need the corrections below.

## 1. Positivity theorem

- The matrices in `scripts/kramers_fams.py:7-11` obey
  `T1^2 = T2^2 = -1` and `{T1,T2}=0` exactly.  Independent checks also give
  zero defects for all 1,024 channels under `T1`, `T2`, and `U(1)c`, and for
  each of the three walker directions.  A real flavour-blind filter intertwines
  these symmetries, so non-on-site filtered vertices are allowed.
- With negative coefficients decoupled by real fields and positive
  coefficients by imaginary fields, every one-body slice is invariant under
  both MTRs.  The unitary product defines the conserved complex structure; in
  its `+i` sector, `T2` is antiunitary and squares to `-1`.  The Wu-Zhang
  conjugate-pair theorem therefore gives a nonnegative ordinary fermion
  determinant for every auxiliary-field configuration.
- `REPORT.md:72` is incomplete about the full weight.  In the Majorana frame,
  the full Gaussian trace is, up to a positive scalar,
  `det(1+M_d)/sqrt(det M_d)`, not merely `det(1+M_d)`.  The denominator is
  positive because the Kramers-invariant one-body generators have real trace;
  `scripts/p4c_stable.py:88-90` actually uses this factor.
- The filtered remainder in the worker's cluster scripts is wrong away from
  `lambda1=0`.  If `F_x F_x^T = rho I`, direct Clifford contraction gives
  `K_R,filtered = rho F_x^T K_R F_x`, plus the scalar remainder multiplied by
  `rho^2`.  `scripts/p4_cluster_weights.py:44-47` and
  `scripts/p4c_stable.py:44-46,69-70` omit `rho`.  For their four-site `f_NN`,
  `rho=3/8`; the unscaled worker remainder has relative error `5/3`.  The
  corrected remainder retains both symmetries, so this is an implementation
  correction rather than a sign-free obstruction.  At `lambda1=0`, the
  remainder vanishes and the exact endpoint is unaffected.

## 2. Decomposition

- I reconstructed theta=230 degrees using an independent 5,000-component
  sample and exhausted all `C(64,4)=635,376` quartic components in batches.
  The maximum relative residual was `4.24e-16`; the sign-cone margin was
  `0.317862823`.
- I independently exhausted the theta=270 degrees Fierz identity with Re
  coefficients `(-34,+2,-2,+2)` and opposite Im coefficients.  Its maximum
  relative residual was `2.96e-16`.  Re/Im scalar terms cancel family by
  family, so the identity remains exact after a real flavour-blind filter.
- The worker's sampled map is not 11-dimensional as claimed in
  `REPORT.md:64` and `scripts/p5_exact_margin.out:1`; a generic sample has 12
  singular values of order `0.058` or larger.  The seed-91 sample missed one
  supported direction.  Consequently the worker's rank-11 minimal-norm step
  was not, by itself, a proof of full exactness; its own fresh residual remains
  `9.5e-12` at theta=230 (`scripts/p5_exact_margin.out:4`).  Correcting in the
  rank-12 map gives the exhaustive residual above without leaving the cone.
- At theta=270, the worker's minimal correction actually leaves the cone:
  margin `-4.276e-7` at `scripts/p5_exact_margin.out:23`.  The separate exact
  Fierz solution in `scripts/p6_fierz_lambda1_zero.out:10` repairs this endpoint
  with margin 2.
- The displayed theta=230 decomposition is incomplete.  `REPORT.md:90-97`
  omits the four nonzero doubled density blocks printed at
  `scripts/p5_exact_margin.out:18-21`; it also does not write `R`.  The correct
  full filtered identity must use the remainder formula above and define the
  density channels as centred Majorana bilinears (or move their normal-ordering
  terms into `R`).

## 3. Cluster weights

Using the corrected filtered remainder, theta=230, the four-site cluster, and
three configurations per point:

- weak: `W=0.5`, `dt=0.05`, `Lt=4`, maximum weight phase `1.13e-14`;
- strong: `W=8`, `dt=0.05`, `Lt=10`, maximum stabilized weight phase
  `2.09e-12`.

The corresponding `arg det(M_d)` values, evaluated from exact traces rather
than determinants of ill-conditioned exponentials, were below `8.2e-16`.
The reproducible implementation is `REFEREE_CHECKS.py:320-417`.  It uses no
Fock-space matrix; exponentials are 128 by 128.

## 4. Boundaries and gauge scope

- I also exhausted all 635,376 components at theta=190 degrees.  The residual
  was `2.25e-16` and the cone margin `0.0155744`.  Convexity with the exact
  theta=270 endpoint therefore certifies the conservative sector
  `lambda1<=0`, `|lambda2/lambda1| >= tan(10 degrees)=0.17632698`, and its
  `lambda2 -> -lambda2` image.  The actual onset between the sampled 188 and
  190 degree points was not located; `0.15-0.18` is a scan bracket, not a
  proved boundary.
- `lambda1>0` is genuinely OPEN in this packet.  The worker explicitly did not
  test the other MTR pairs (`REPORT.md:101`), and the known MTR, Majorana
  positivity, and split-orthogonal theorems are sufficient criteria, not an
  automatic decomposition of this quartic.
- Under `G_SM`, the real vector 10 branches as the real 6 of the colour triplet
  plus the real 4 of the weak doublet, so there is no invariant real 2-plane.
  This correctly destroys the proposed fixed `(9,10)` `U(1)c` sector for
  arbitrary dynamical links.  It does **not** prove that every possible
  Kramers/Majorana/reflection-positive construction of the gauged model fails.
- The representative odd-reflection MTRs and their squares are correct, but
  the packet does not prove the exhaustive P1 classification asserted at
  `REPORT.md:54-58`: `scripts/p1_p2_p3_lp.py:54-70` constructs only the
  `k=1,3,5` representatives and gives a character check, not a classification
  of every admissible `V` or every accidental Fierz symmetry.

## 5. Fixed reading

`TESTS.md:98-102` explicitly permits a faithful reduction consisting of the
walker plus the filtered global-Spin(10) quartic.  Setting the dynamical gauge
links to the identity gives precisely that stated reduction; choosing
`lambda1=0`, `lambda2!=0` selects an allowed member because X2 leaves the two
couplings free (`PREREG.md:10-15`).  Thus SIGN-FREE is met for a stated
ungauged subfamily, not for all X2 couplings and not for the gauged theory.

## Resource note

The exhaustive algebra run peaked at 192.6 MiB RSS and the final weak/strong
weight run at 229.8 MiB, with `OMP_NUM_THREADS=2`.  A discarded preliminary
weight implementation duplicated the 1,024-channel array and peaked at 316.4
MiB before it was replaced; no scientific conclusion above relies on that run.
