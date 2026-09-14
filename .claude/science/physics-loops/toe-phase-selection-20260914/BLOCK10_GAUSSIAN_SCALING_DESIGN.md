# Next leverage: actual finite-clock observables to Gaussian Maxwell scaling

Proposed block10, not yet proved or executed. Selected after the block9
integer normal form and simultaneous actual-ground-state penalty limit.
Continue personally; no workers. The phase of the fixed N=3 Hamiltonian
remains open. This is a distinct route through the finite-clock Villain
family already studied in proposed PR8127 (075a47fd49e98bb4c8f4b88ec149dcb78a52b5cd).

The new target is stronger than a covariance/gaplessness statement: derive
the complete Gaussian joint-law scaling limit for bounded physical clock
score observables, then reconstruct two linear transverse photon modes.
N, beta and lattice spacing vary along an explicit scaling family. This
does not select one native law or prove that the N=3 penalty Hamiltonian
has that phase. All unreviewed dependencies must stay explicit.

Candidate mechanism:

1. Write the positive Villain lifted field y=d theta-2pi m. Its exact
   distribution is the discrete Gaussian on M_N=N Z^P+d Z^E, with
   X=sqrt(beta)y=z/sqrt(beta_d), beta_d=N^2/(4pi^2 beta). Keep gauge and
   torus holonomy multiplicities exact.
2. Every centered Gaussian on a full-rank lattice is sub-Gaussian in real
   sources: completing the square and Poisson positivity give
   M_X(h)<=exp(||h||^2/2). This is a scalar theta maximum, not a false
   all-shift covariance upper bound.
3. Decompose M_N into affine integer-curl cosets. The all-shift lower
   covariance estimate proved provisionally in PR8127 gives, for exact h,
   exp((1-delta_d)||h||^2/2)<=M_X(h)<=exp(||h||^2/2).
   Check that the conditional lower bound survives arbitrary real tilt.
4. Its dual covariance bound controls the perpendicular piece by
   delta_beta P_coexact+P_harmonic. For local or continuum smeared sources
   the harmonic norm goes to zero as the physical torus size grows.
5. MGF squeezing/Cramer-Wold then yields Gaussian exact-two-form laws as
   beta,beta_d go to infinity. Need a precise triangular-array/UI argument.
6. The bounded physical score is s_beta(theta)/sqrt(beta)=-E[X|theta].
   Conditional on clock links, the Villain integer lifts are independent
   between plaquettes. Therefore the noise in a smeared linear source has
   variance sum h_p^2 E Var(X_p|theta), not an l1-squared volume loss.
   A sub-Gaussian tail bounds this local variance by
   (8 pi^2 beta+16)exp(-pi^2 beta/2), using the principal representative as
   a comparison predictor. Check the endpoint convention at pi.
7. In four Euclidean dimensions smear with h_p=a^2 f_mu,nu(a x). Then
   ||h||_2 is bounded; the lattice exact projection converges to the
   continuum Maxwell curvature covariance d(-Delta)^(-1)d^*. Assume
   a->0, aL->infinity, beta,beta_d->infinity. Check aliasing and harmonic
   estimates; no extra beta versus log(1/a) condition should be needed
   for score observables because of conditional lift independence.
8. Reconstruct the Gaussian limit explicitly. For magnetic fields at
   positive/reflected times, the Fourier covariance is
   (|p|/2)exp(-|p|(t+s)) P_transverse(p), giving rank two and energy |p|.
   Contact terms and the zero momentum sector must be explicit. Maxwell
   spacelike commutativity follows from derivatives of the massless
   Pauli-Jordan distribution, if that stronger conclusion is included.

Falsifiers: wrong coset multiplicities, missing contact term, wrong dual
temperature, applying centered covariance upper bound after a shift,
forgetting the harmonic sector, replacing the score with an unsafely summed
principal angle, false l1 accumulation, and identifying an arbitrary
gapless covariance with a Gaussian measure.

Delivery decision after proof: possibly extend our existing PR8127 with a
new source/runner and explicit dependency, using its exact pushed branch
as base so the covariance proof is present. Do not pretend its unreviewed
theorem is already retained. Alternatively keep the new conditional work
durable if the proof or review is incomplete. No new worktree before the
disk guard, and remove completed delivery scratch after exact remote checks.
