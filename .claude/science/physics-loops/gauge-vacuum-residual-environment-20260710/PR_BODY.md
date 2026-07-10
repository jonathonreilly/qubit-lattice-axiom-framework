## Science block

This physics-loop block attacks the missing residual-environment derivation in
`GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_IDENTIFICATION_THEOREM_NOTE.md`.
It does not claim retained-grade closure of the parent operator identity.

### Honest status

- parent residual/operator identification: **open**;
- exact sub-result: **no-go** for one `L_s`-suppressed environment sequence
  covering both standard `L_s=2` PBC and `L_s=3` PBC surfaces;
- constructive sub-result: **bounded support** for the actual standard
  `L_s=2` PBC 23-active-plaquette environment at `beta=6`;
- independent audit remains required before any effective-status change.

### Claim movement

The exact incidence runner proves a positive cubic fundamental-environment
term at `L_s=2` PBC while all terms below fifth order vanish at `L_s=3` PBC.
Therefore the parent target must carry `L_s`; BC is stated to define the
finite measure but fixed-`L_s` BC dependence is not claimed.

The direct four-chain computation gives
`rho_(1,0)^(env,L_s=2,PBC)(6) = 0.0688943 +/- 0.0047454` under a declared,
uncalibrated batch diagnostic. The selected coupled environment is strongly
distinguished from the single-link packet value `0.422531740`, but temporal
mixed-kernel stripping remains unproved.

### Artifacts

- [Handoff](HANDOFF.md)
- [Trace gate](TRACE_GATE.md)
- [Claim-status certificate](CLAIM_STATUS_CERTIFICATE.md)
- [Review history](REVIEW_HISTORY.md)
- [No-go discipline checklist](NO_GO_DISCIPLINE_CHECKLIST.md)
- [Exact geometry note](../../../../docs/GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_GEOMETRY_DEPENDENCE_NO_GO_NOTE_2026-07-10.md)
- [Bounded direct-computation note](../../../../docs/GAUGE_VACUUM_PLAQUETTE_L2_PBC_ACTUAL_ENVIRONMENT_MC_BOUNDED_NOTE_2026-07-10.md)
- [Exact runner](../../../../scripts/frontier_gauge_vacuum_plaquette_environment_geometry_dependence_no_go_2026_07_10.py)
- [Bounded MC runner](../../../../scripts/frontier_gauge_vacuum_plaquette_l2_pbc_environment_mc_bounded_2026_07_10.py)
- [Exact output](../../../../outputs/frontier_gauge_vacuum_plaquette_environment_geometry_dependence_no_go_2026_07_10.txt)
- [Bounded MC output](../../../../outputs/frontier_gauge_vacuum_plaquette_l2_pbc_environment_mc_bounded_2026_07_10.txt)

### Checks

- exact geometry runner: `PASS=11 FAIL=0`;
- bounded MC runner: `PASS=6 FAIL=0`;
- parent finite-packet runner: `THEOREM PASS=6 SUPPORT=3 FAIL=0`;
- independent MILP minima: `3` and `5`;
- Python compile and `git diff --check`: pass;
- vocabulary lint: zero violations;
- audit pipeline validation and strict lint: zero errors; generated authority
  outputs stripped before commit;
- review-loop: pass with bounded claims.

### Remaining blocker

Write the actual one-clock temporal Wilson kernel on a selected finite
geometry and prove or falsify that division by the four-link local coefficient
commutes with the unmarked Haar marginal. Only that operator bridge can connect
the selected spatial environment to the stripped residual source-sector slot.
