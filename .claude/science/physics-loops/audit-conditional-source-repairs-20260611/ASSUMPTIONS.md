# Assumptions

- Audit verdicts and effective statuses are owned by the independent audit
  lane. This PR only changes source notes, runners, and runner caches.
- Conditional rows may be source-repaired without claiming clean or retained
  status. The auditor/reviewer decides whether any repaired row becomes
  re-auditable or changes status.
- New axioms are not introduced.
- Narrowing is allowed where it removes a false import or overclaim while
  preserving the runner-backed science.
- Remaining unclosed premises are intentionally left named:
  - P-KIN/P-SD kinetic-class derivation and BlockT1 statistics selection.
  - B-AXIS and B-RANGE for single-clock evolution.
  - Staggered-Dirac realization / physical carrier gates for downstream
    Koide, quark, taste-scalar, and related rows.
  - CAR-vs-hard-core-boson selection for Pauli/fermionic-frame consumers.
  - Framework-native Coulomb/atomic sector and full hydrogenic spectrum.
  - Physical beta=6 Wilson/Haar exhaustiveness for the plaquette evaluator
    route.
