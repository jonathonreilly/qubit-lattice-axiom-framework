# Handoff

This PR is a post-audit source repair for the Wilson leading-order
Higgs-sector row. It intentionally does not edit:

- `docs/audit/**`
- publication effective-status mirrors
- front-door status files

The source-side repair makes the re-audit target clearer:

1. Audit the new Wilson readout-boundary certificate as the native
   diagnostic curvature-scale support.
2. Re-audit the existing Wilson leading-order row with the new boundary
   dependency and strengthened Taylor checks.
3. Keep any physical Higgs-pole claim conditional unless a separate
   retained bridge supplies the broken-phase readout and the nonzero
   Wilson coefficient.

The expected audit effect is not an automatic status conversion. The PR
queues the row for direct review by making the native support explicit
and leaving the still-open physical readings quarantined.
