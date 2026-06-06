# Handoff

PR purpose:

Repair the conditional RP/Radon-Nikodym row by narrowing it to the finite
normalized-trace Gibbs density theorem and adding an executable certificate.

What changed:

- The note no longer consumes `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION` as
  a markdown load-bearing dependency.
- `rho_ref` and Wilson/RP compatibility are conditional downstream applications,
  not premises of the theorem.
- A new runner checks the finite matrix theorem and note dependency hygiene.

Verification:

- Runner passes with `PASS=14 FAIL=0`.
- Runner cache is fresh.
- `git diff --check` passes.
- `git diff -- docs/audit --exit-code` passes.

Audit boundary:

No `docs/audit/**` files are modified. This PR does not set an audit verdict or
claim an effective status change.

Remaining science:

The `rho_ref|_Lambda = tau_Lambda` bridge and the Wilson/RP carrier
representation bridge remain open.
