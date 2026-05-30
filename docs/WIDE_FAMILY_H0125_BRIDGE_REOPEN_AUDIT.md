# Wide-Family `h = 0.125` Bridge Reopen Audit — Reduced-Family Fixed `h = 0.125` Negatives (Binding)

**Date:** 2026-04-06 (scope narrowed 2026-05-17 per audited_conditional `runner_artifact_issue` repair: binding scope is the reduced/fixed-family `h = 0.125` bounded negatives already carried by retained dependencies; the wider `phys_w = 4` continuation is out of scope without a separately registered retained note/log/runner)
**Status:** bounded fixed/reduced-family `h = 0.125` weak-field-closure
negatives, inherited from the retained dependencies named below; the
wider `phys_w = 4` continuation reopen path is **out-of-binding-scope**
in this revision.

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `runner_artifact_issue`, stating: *"Re-audit after adding
a retained note/log/runner for the wider `phys_w = 4` continuation, or
after narrowing this row to the fixed/reduced `h = 0.125` negatives
already carried by its retained dependencies."*

This revision takes the second option. The binding evidence of this
note is exactly the **fixed/reduced-family `h = 0.125` bounded
negatives** already carried by its retained one-hop dependencies
(notably `LATTICE_3D_L2_NUMPY_H0125_BRIDGE_NOTE.md` and the upstream
runner caches). This note re-states those negatives at the
reopen-audit level; it does not add a new fixed/reduced-family
result.

The **wider `phys_w = 4` family continuation** is **demoted to
out-of-binding-scope** in this revision. Promoting that wider-family
reopen requires a separately registered retained note/log/runner that
this revision does not supply. The current narrative content
discussing the wider-family probe is retained for context but is not
load-bearing for the audited claim.

This note is a narrow audit of the Claude-side claim that the wider fixed
family behind the 3D dense `1/L^2 + h^2` lane can still complete the `h =
0.125` continuation test.

It is intentionally narrower than the earlier reduced-family `h = 0.125`
bridge note. The point here is not to relitigate the reduced audit-family
negative. The point is to isolate whether the wider fixed family deserves a
fresh, narrow reopen path.

## Existing artifacts

- [`scripts/lattice_3d_l2_numpy_h0125_bridge.py`](/Users/jonreilly/Projects/Physics/scripts/lattice_3d_l2_numpy_h0125_bridge.py)
- [`scripts/lattice_3d_l2_numpy_h0125_only.py`](/Users/jonreilly/Projects/Physics/scripts/lattice_3d_l2_numpy_h0125_only.py)
- [`scripts/lattice_3d_l2_wide.py`](/Users/jonreilly/Projects/Physics/scripts/lattice_3d_l2_wide.py)
- [`docs/LATTICE_3D_L2_NUMPY_H0125_BRIDGE_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/LATTICE_3D_L2_NUMPY_H0125_BRIDGE_NOTE.md)
- [`docs/H2T_H0125_NARROW_BRIDGE_NOTE.md`](/Users/jonreilly/Projects/Physics/docs/H2T_H0125_NARROW_BRIDGE_NOTE.md)

## What the current local replay confirmed

I replayed the wide-family bridge under the retained system interpreter
because the default Homebrew `python3` on this machine does not ship with
`numpy`, while `/usr/bin/python3` does.

The replay wrappers now call
[`scripts/numpy_replay_bootstrap.py`](/Users/jonreilly/Projects/Physics/scripts/numpy_replay_bootstrap.py)
so future numpy-heavy retained replays land on the same interpreter
convention without depending on shell `PATH` order.

The local replay confirmed:

- the bridge script is runnable in a clean venv
- the family reproduces the same coarse rows as the retained note
- the replay reaches the `h = 0.25` row cleanly
- the wide-family setup is therefore not identical to the reduced-family
  dead-end audit

What the focused decision harness added afterward:

- a completed local `h = 0.125` row on the same fixed bridge family
- Born `6.59e-15`
- `k = 0` clean
- gravity `+0.029856` (`TOWARD`)
- `F~M alpha = 0.501`

## Why this is still not retained

The focused single-row replay makes the scale issue explicit:

- `h = 0.125`
- `117649` nodes
- `49` layers
- `276710448` dense transition entries in the focused replay

On this machine the original edge-list path remained computationally heavy,
but the focused dense-matrix replay now completes. That completion sharpens
the result rather than promoting it:

- the fixed bridge family no longer looks unresolved at `h = 0.125`
- it now looks like a completed same-family row that still fails the
  weak-field `F~M \approx 1` bridge criterion

That means the only safe present-tense reading is:

- the reduced-family `h = 0.125` negative still stands separately
- the current fixed bridge family now also completes without closing the
  weak-field mass-law gap
- the first genuinely wider retained continuation can now be read directly:
  `phys_w = 4`, `phys_l = 6`, full-window `alpha = 0.499` with clean Born,
  clean `k = 0`, and `TOWARD` gravity
- the immediate wider-family reopen therefore also closes as a bounded
  negative on the tested retained row

## Safe read

The strongest honest statement right now is:

- the Claude-side `h = 0.125` story was worth reopening
- the current fixed bridge family now resolves as a bounded negative for
  weak-field closure
- the first genuinely wider `phys_w = 4` replay also resolves as a bounded
  negative on the retained full-window row
- there is no currently retained live reopen on this exact bridge family

## Reopen condition

This lane should only be promoted if a fresh retained replay captures:

- the `h = 0.125` row on a materially different family beyond the now-tested
  `phys_w = 4` continuation
- clean Born on the completed rows
- the same-family weak-field observables without a silent geometry change
- a reproducible log file or note chain on `main`

Until then, the fixed bridge family and the first wider-family continuation
should both be treated as resolved bounded negatives rather than as live
reopen candidates.
