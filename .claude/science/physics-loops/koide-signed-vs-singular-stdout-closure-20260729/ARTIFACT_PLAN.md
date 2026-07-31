# Artifact plan

1. Compact only successful runner presentation; preserve failure diagnostics,
   all assertions, exact samples, and `PASS=30 FAIL=0`.
2. Add live N1 route, N5 resolution, and N7 steelman-resolution locators without
   changing the 30-check count.
3. Add the source-visible N1-N8 checklist required for the derived boundary.
4. Refresh the canonical runner cache against the new source SHA.
5. Verify source, runner, stdout, and cache all fit packet limits without a
   clipping marker.
6. Run vocabulary lint and review-loop; do not edit audit-owned data.
