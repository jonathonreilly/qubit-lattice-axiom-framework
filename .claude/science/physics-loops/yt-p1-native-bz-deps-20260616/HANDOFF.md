# Handoff

This branch fixes the source-side dependency gap behind the current
`YT_P1_I_S` audited-conditional verdict. It adds a bounded arithmetic
certificate for canonical plaquette-derived constants, links that certificate
into the full-staggered BZ quadrature note, and links both into the YT P1
arithmetic bridge.

Independent audit/review should verify:

- the new canonical certificate is correctly scoped to arithmetic over the
  parent plaquette reuse surface;
- the native BZ quadrature row is suitable for audit as a direct upstream row;
- the YT P1 row no longer hides the BZ and alpha/plaquette inputs as script
  imports or prose-only references.

No audit verdicts or generated effective-status surfaces are included.
