# Handoff

This PR adds an explicit downstream-use firewall to the RCONN kappa-EW
register-not-read route demotion.

What changed:

- The note now lists allowed and forbidden downstream citations.
- The runner checks that the firewall exists and forbids reusing this row as a
  `kappa_EW = 0` or `R_conn = 8/9` selector theorem.
- The cache is refreshed with `TOTAL: PASS=20 FAIL=0`.

What this does not do:

- It does not close the wider `kappa_EW` gate.
- It does not supply a physical EW readout/weighting bridge.
- It does not edit audit verdicts or status surfaces.
