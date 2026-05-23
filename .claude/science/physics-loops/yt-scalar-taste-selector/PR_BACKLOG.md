# PR Backlog

PR creation failed after the branch was pushed because GitHub returned:

```text
GraphQL: API rate limit already exceeded for user ID 246726392.
```

Branch:

```text
physics-loop/yt-scalar-taste-selector-20260523
```

Open when the GitHub API limit resets:

```bash
gh pr create \
  --base main \
  --head physics-loop/yt-scalar-taste-selector-20260523 \
  --title "[physics-loop] Y_T scalar/taste selector no-go" \
  --body-file /tmp/yt_scalar_taste_selector_pr_body.md
```

Suggested body:

~~~markdown
## Summary

This PR attempts the next positive Y_T bridge after the repaired
color-projection row: derive `kappa_Y = 0` from the scalar/taste-condensate
Yukawa operator.

The attempt does **not** close positively. It lands a narrow route-specific
no-go:

```text
one-Higgs color-singlet scalar/taste insertion -> M_color proportional to I_color
kappa_Y = 0 via projection -> requires nonzero Tr(M_color)=0
```

Those are incompatible. The direct scalar/taste-condensate route therefore
cannot derive the connected-trace specialization `kappa_Y = 0` without
replacing the physical color-singlet Higgs insertion by a nonzero
traceless/color-adjoint insertion, or supplying a different matching theorem
for `kappa_Y`.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_yt_scalar_taste_condensate_selector_no_go.py` -> `RESULT: PASS=37 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_yt_color_projection_correction.py` -> `RESULT: PASS=42 FAIL=0`
- `bash docs/audit/scripts/run_pipeline.sh` -> OK
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, no errors; existing warnings/notices only
- `git diff --check` -> OK
~~~
