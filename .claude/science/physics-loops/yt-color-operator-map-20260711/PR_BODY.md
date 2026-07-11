## Science block

This physics-loop block makes a sustained first-principles attempt on the
missing physical scalar-normalization map in
[`YT_COLOR_PROJECTION_CORRECTION_NOTE.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/yt-color-projection-block01-20260711/docs/YT_COLOR_PROJECTION_CORRECTION_NOTE.md).

The exact audit target was:

> The physical Yukawa probes only the singlet channel, so
> y_t(physical)/y_t(Ward) = sqrt(Z_phi^{connected/total}) =
> sqrt((N_c^2 - 1)/N_c^2) = sqrt(8/9).

The positive map does not close. The exact obstruction is sharper:

- `8/9` is `rank(P_adj) / dim End(C^3)`, a normalized superoperator rank;
- the specified color-singlet scalar source has insertion `M_phi = c I`, so
  `P_adj(M_phi) = 0`;
- `Hom_SU(3)(1, adj) = 0` without another colored carrier;
- connected/VEV subtraction leaves the scalar source tangent on `I_color`;
- a scalar LSZ residue therefore requires a separate dynamical two-point or
  matching theorem and cannot be replaced by the Fierz dimension count.

This is a narrow `no_go`, not a global obstruction to interacting
colored-composite, direct-response, or top-correlator routes. It does not
derive a physical `sqrt(8/9)` factor.

## Trace and claim state

- Trace: `direct_blocker_closure`
- Artifact role: `no_go`
- Actual branch status: exact negative boundary for the quoted map
- Positive physical Yukawa status: open
- Positive retained-proposal language: not allowed
- Independent audit is required after landing before any effective status may
  change.

See:

- [`TRACE_GATE.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/yt-color-projection-block01-20260711/.claude/science/physics-loops/yt-color-operator-map-20260711/TRACE_GATE.md)
- [`CLAIM_STATUS_CERTIFICATE.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/yt-color-projection-block01-20260711/.claude/science/physics-loops/yt-color-operator-map-20260711/CLAIM_STATUS_CERTIFICATE.md)
- [`NO_GO_DISCIPLINE_CHECKLIST.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/yt-color-projection-block01-20260711/.claude/science/physics-loops/yt-color-operator-map-20260711/NO_GO_DISCIPLINE_CHECKLIST.md)
- [`HANDOFF.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/yt-color-projection-block01-20260711/.claude/science/physics-loops/yt-color-operator-map-20260711/HANDOFF.md)

## Artifacts

- Strengthened source note with the rank-versus-action theorem, equivariant
  source-map obstruction, connected-cumulant boundary, and full N1-N8 gate.
- Exact rational runner constructing both projectors, computing their ranks by
  Gaussian elimination, and solving the invariant/traceless commutant.
- Refreshed SHA-pinned runner cache: `PASS=96 FAIL=0`.
- Durable physics-loop pack with assumptions/imports, five-route fan-out,
  review history, trace gate, status certificate, and handoff.

## Imports retired or exposed

Retired: the implicit identification of the adjoint dimension fraction with
the scalar-source projector action or LSZ residue.

Still exposed:

- a same-surface dynamical scalar two-point/LSZ normalization map; or
- a new equivariant composite-source construction with additional colored
  carriers; or
- a direct physical-response/top-correlator bypass.

No observed masses, PDG values, fitted selectors, literature values,
CMT/tadpole factors, or RGE transport are load-bearing.

## Verification

- `python3 -m py_compile scripts/frontier_yt_color_projection_correction.py`
- `PYTHONPATH=scripts python3 scripts/frontier_yt_color_projection_correction.py`
  (`PASS=96 FAIL=0`)
- independent SymPy vectorized-projector and eight-Gell-Mann constraint check
- four interacting sibling-runner checks; all target-note pins passed, with one
  documented unrelated pre-existing signed-readout phrase failure
- `scripts/vocab_lint.py --fix` and `--report-only`: clean
- full audit pipeline in deterministic stages
- `python3 docs/audit/scripts/audit_lint.py --strict`: zero errors
- validation row: ready `unaudited` `no_go` with the existing Fierz dependency
- `git diff --check`: clean
- runner-cache SHA freshness: clean
- repository-portable links gate: clean
- pipeline-output-stripped gate: clean

## Review-loop

Disposition: `pass` after five fixes covering status wording, N1-N8 evidence,
computed rather than hard-coded projection helpers, the shifted-source tangent
check, and audit-facing claim-boundary metadata.

Detailed findings and the independent check are in
[`REVIEW_HISTORY.md`](https://github.com/jonathonreilly/cl3-lattice-framework/blob/physics-loop/yt-color-projection-block01-20260711/.claude/science/physics-loops/yt-color-operator-map-20260711/REVIEW_HISTORY.md).

This PR must not be merged without normal review, and this physics-loop run
does not merge it or modify repo-wide audit authority surfaces.
