# Handoff

This PR targets `signed_gravity_aps_locked_source_action_proposal_note`.

It does not derive the APS-locked source action. It makes the current negative
route explicit and executable in the row packet: retained APS/Wald/Gauss does
not derive `chi_eta M_phys <rho,Phi>`, and the inserted ansatz passes the local
variation/sign-table controls only after the source term is supplied.

Verification:

```bash
python3 scripts/signed_gravity_aps_locked_source_action_proposal.py
python3 scripts/cached_runner_output.py --refresh scripts/signed_gravity_aps_locked_source_action_proposal.py --tail-chars 12000
python3 scripts/cached_runner_output.py --check-only scripts/signed_gravity_aps_wald_gauss_bridge_audit.py
python3 scripts/precompute_audit_runners.py --runners scripts/signed_gravity_aps_locked_source_action_proposal.py --check-only --allow-non-main
```

No audit ledger/status/queue files were edited.
