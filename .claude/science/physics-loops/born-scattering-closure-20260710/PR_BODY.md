## Summary

- replace the old imported-slope proximity argument with a direct derivation
  of the finite-path ray law and the literal signed-adjoint detector response;
- prove that the displayed unregularized 2D and 3D Gaussian ray averages have
  an interior zero-impact pole and do not define ordinary expectations;
- add a target-exponent-free two-harness discriminator with literal detector
  endpoints, complete supplied-input disclosure, helper provenance, and a
  fail-closed analytic-only mode;
- preserve the result as a bounded no-go packet: the Gaussian pole subtheorem
  is exact, while the plane/adjoint comparison is deterministic floating-point
  evidence on two declared finite harnesses.

## Scientific boundary

The old conclusion is withdrawn: numerical proximity of the nominal long-path
ray slope to a separately supplied lattice slope is not an observable bridge.
The replacement does not claim a global geometric-optics no-go, a coherent 3D
closure, a derived `beta`, or an analytic closed form for the signed-adjoint
`b`-law. Independent audit remains the sole authority for any retained status.

## Key results

- Endpoint-matched plane slopes: `-1.561303798`, `-1.279250536`; cross-path
  shape change `0.282053262`.
- Rebuilt signed-adjoint slopes: `-1.435642062`, `-1.433548534`; cross-path
  shape change `0.002093528`.
- Gaussian pole law: `I_ray(b_eff) = 2/b_eff + O(b_eff)` at every declared
  zero-impact ray, with positive 2D and old-3D angular weights.
- Full runner: `PASS=12 FAIL=0`; analytic-only: `PASS=7 FAIL=0 SKIP=5`,
  disposition `INCOMPLETE`, exit code `2`.

## Review-loop disposition

- Code / Runner: PASS.
- Imports / Support: DISCLOSED.
- Physics / Nature: PASS WITH BOUNDED CLAIMS.
- No-Go Discipline: PASS.
- Repo Governance: PASS.
- Labeling Convention: NA.

## Validation

```text
python3 -m py_compile scripts/gaussian_beam_eikonal.py
python3 scripts/gaussian_beam_eikonal.py
python3 scripts/gaussian_beam_eikonal.py --analytic-only  # expected exit 2
python3 scripts/vocab_lint.py --report-only docs/BORN_SCATTERING_COMPARISON_NOTE.md .claude/science/physics-loops/born-scattering-closure-20260710
python3 scripts/render_controlled_vocabulary.py --check
bash docs/audit/scripts/run_pipeline.sh                  # detached validation worktree
python3 docs/audit/scripts/audit_lint.py --strict        # zero errors
git diff --check
```

Detached pipeline validation seeded one new/changed row, preserved `3717`
audits, invalidated `0`, and produced target metadata `claim_type=no_go`,
`audit_status=unaudited`, `effective_status=unaudited`. Generated ledgers and
status views were discarded and are not part of this PR.

## Primary artifacts

- `docs/BORN_SCATTERING_COMPARISON_NOTE.md`
- `scripts/gaussian_beam_eikonal.py`
- `logs/runner-cache/gaussian_beam_eikonal.txt`
- `.claude/science/physics-loops/born-scattering-closure-20260710/`

