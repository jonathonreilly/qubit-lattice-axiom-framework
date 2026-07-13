# Artifact plan

1. Preserve `docs/YT_BRIDGE_ACTION_INVARIANT_NOTE.md` as the historical bounded
   scan and add a distinct route-specific no-go claim ID.
2. Add a deterministic exact-arithmetic runner that checks:
   - affine two-moment identity;
   - curvature/variance remainder identity and bound;
   - equal-action/different-centroid falsifier;
   - equal-action/equal-centroid/different-variance falsifier;
   - a local positive-action coefficient counterfamily and its stationarity;
   - dependency/source-surface firewalls.
3. Add the runner-generated JSON certificate and cached stdout.
4. Run target, syntax, formatting, audit-readiness, and review-loop checks.
5. Record review findings and the honest claim certificate before one PR.
