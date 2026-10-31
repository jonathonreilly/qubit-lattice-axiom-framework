# Pre-registered H_RP finite-check criteria — 2026-10-29

Statements and thresholds only; written before check scripts and runs.

- Gauge groups: Z2, Z3 and Q8 in its faithful two-dimensional SU(2)
  representation. Wilson weights are positive central functions.
- Positive cases: periodic hypercubic tori of dimensions 2 and 3, extent 4
  in the reflected direction, for link and site reflection. Use finite
  transverse extents at least 2. Include reflection-symmetric nonconstant
  nonnegative plaquette couplings, and zero-coupling edge cases.
- Compute the normalized RP Gram matrix exactly on an explicitly declared
  linearly independent basis of positive-half observables (a subalgebra basis
  is permitted and must be identified as such). Exact transfer/character
  reduction is permitted; reconstruct the actual periodic lattice action and
  both reflection planes. No floating-point eigenvalue tolerance proves PSD.
- Use rational Wilson Boltzmann weights by an a priori logarithmic coupling
  choice when possible. Certify PSD with exact rational congruence pivots,
  exact eigenvalues, or an explicit exact positive factorization. State any
  reduction in the observable basis; finite checks do not exhaust SU(N).
- Independently compare at least one reduced formula with direct finite
  enumeration. Verify group multiplication, inverses and the chosen character.
- Build a small doubled digital-ball/prism model directly from SPHERE55's
  definition. Check reflection of its edges and plaquettes, crossing-cell
  factorization, reflection pairing of weights and an exact RP Gram matrix.
- Negative controls: one negative crossing-plaquette coupling; one crossing
  cell not invariant under reflection; one coupling not symmetric under
  reflection. Each requested detection criterion is a strictly negative
  eigenvalue. If a matrix is non-Hermitian, report that separately and examine
  its Hermitian part. If no negative eigenvalue occurs, record the criterion
  as failed, even when a different RP defect is detected. A counterexample
  to a universal necessity claim is not a failed theorem.
- Every numeric process must self-monitor RSS and stop above 1,000,000,000
  bytes; wall-clock runtime must be less than 1,200 seconds. Use nice level
  10 and OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1.
- Start a numeric job only with load strictly below 8 and memory_pressure
  reporting at least 30 percent free memory. Acquire the prescribed
  .locks_hrp_numeric directory before the job and remove it exactly once
  afterward. No traps, pkill, or orphaned processes.
- Save complete stdout, stderr and timing/resource receipts. Report every
  failed assertion and label any later investigation post-hoc.
