The supplied full-qubit pair Hamiltonian has dilute mean-energy coefficient
`t0/8`, where `t0` is the coherent minimum of its actual fifteen-channel
four-particle threshold form. This unit proves the physical many-particle
lower comparison and matching upper, then derives grand energy
`-2 nu²/t0`, ground-density onset `4 nu/t0`, and the ordered exact-N dilute
liminf/limsup envelopes. Status: conditional-support; type: bounded_theorem.

The lower proof treats physical boundary rows, the full core/Q response,
compatible collision corrections, internal fragmentation and actual-particle
tails. The upper uses a finite-range unitary on the full hard-core carrier;
exact-N transfer uses finite block sectors, deterministic rounding, reserved
sites and bounded seams. These are one coherent theorem, with three owned
proof appendices.

This proposal is stacked on PR9401's exact
`ea3d4f6236160233f6f9e183b4b6eb5ba3252607` threshold source. Its necessary
three-file threshold proof closure remains inside the required coherent
source review; ancestry alone is not review coverage. The same-model density
and all-density coercivity source is on main. No fixed-rho canonical-limit
existence, unrestricted simultaneous limit, phase/ODLRO, polarization,
excitation spectrum, preparation or framework Hamiltonian selection is claimed.

- Canonical source: `docs/NATIVE_DILUTE_THERMODYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-30.md`.
- Proofs: `NATIVE_DILUTE_PHYSICAL_BOUNDARY_PROOF_2026-09-30.md`,
  `NATIVE_DILUTE_CELL_INTERACTION_PROOF_2026-09-30.md`, and
  `NATIVE_DILUTE_LOWER_AND_LIMITS_PROOF_2026-09-30.md`, all under `docs/`.
- Primary: `scripts/native_dilute_thermodynamics_2026_09_30.py`;
  actual canonical cache: `logs/runner-cache/native_dilute_thermodynamics_2026_09_30.txt`.
- Unit pack: `.claude/science/physics-loops/native-dilute-thermodynamics-20260930/`;
  `HANDOFF.md`, `TRACE_GATE.md`, `ASSUMPTIONS_AND_IMPORTS.md`,
  `REVIEW_HISTORY.md`, `PROVENANCE.json`, and `CONTROL_DERIVATION.md` carry
  scope, exact identities, imports, conformance and evidence limits.

Actual schema2 pre-execution validation passed before the primary. All seven
finite exact control families passed, and all eleven declared operator/geometry/formula/oracle
sensitivity controls failed at their intended assertions. Primary runtime was 2.165 seconds
wall and 1.947 seconds reaped-child CPU including monitoring; sampled aggregate
resident memory was 56.2 MB. Finite controls do not establish the analytic
infinite-volume statements by extrapolation. The boundary fixtures explicitly
distinguish 837 complete-family rows from 1017 actual individual rows at side 5.

Mutations changed gradient weight, boundary-family selection, incident pins,
plane multiplicity, safe diagonal subtraction, bad-particle charge, centering
order, complex-sphere coefficient, integer reserve, seam width and pulse pair
factor. Every candidate, assertion and resource receipt is preserved.

The local third-native-unit content evaluation is OPEN in `CLUSTER_CAP.md`;
this is not a review or audit verdict. Formal whole-unit source review,
integration validation and audit remain separate gates. This is an unpublished
body draft; its paths are converted to actual repository links by delivery,
and the final graph/review/commit receipts must be added before PR creation.
