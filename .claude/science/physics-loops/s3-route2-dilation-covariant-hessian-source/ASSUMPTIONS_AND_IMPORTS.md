# Assumptions And Imports

## Minimal Allowed Premises

- Lattice/Quantum/Record from `MINIMAL_AXIOMS_2026-06-05.md`.
- Seven-site O_h star weights `w_E=1/3`, `w_T=1/2` from the O_h support
  theorem.
- Route-2 restricted readout algebra from
  `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`.
- Block99 inverse-square reduction, available on the stacked base branch.
- Exact rational arithmetic.

## Forbidden Proof Inputs

- observed quark masses;
- fitted Yukawa values;
- CKM or Jarlskog targets;
- nearest-rational selection from live endpoint data;
- an admitted endpoint triple;
- PR state, audit verdicts, or mergeability.

## Open Imports Exposed

- Physical coordinate bridge: Route-2 channel weights must be proved to be the
  positive coordinates of the Hessian source density.
- Dilation covariance: the source/readout Hessian must satisfy
  `H(a*w)=a^-2 H(w)`.
- Counterterm exclusion: positive terms such as `epsilon w^2/2` in the
  potential, giving `H=C/w^2+epsilon`, must be ruled out by a real theorem.

## Import Classification

The dilation-covariant Hessian premise is not an axiom, retained theorem, or
current named primitive. It is an exact future theorem target.
