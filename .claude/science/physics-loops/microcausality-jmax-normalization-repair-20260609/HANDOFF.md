# Handoff

Branch: `physics-loop/microcausality-jmax-normalization-repair-20260609`

Target claim:
`microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09`

What changed:

- Fixed the Wilson-plaquette normalization in the note and runner: the parent
  action has coefficient `beta` multiplying `Re[1 - tr(U_P)/N_c]`, so the
  plaquette contribution is bounded by `2*beta` per plaquette.
- Updated the closed-form action-density bound from `|m| + 30` to
  `|m| + 78` at `d = 4`, `r_W = 1`, `beta = 6`, `N_c = 3`.
- Recomputed the conditional LR velocity using the corrected `J_max`.
- Narrowed the Wilson language to the retained symmetric-canonical
  `M_W = r_W d I` surface and kept exact-H locality conditional.
- Refreshed the runner cache.

Verification:

```text
python3 scripts/microcausality_finite_range_h_bridge_2026_05_09.py
PASS=4, FAIL=0

python3 scripts/cached_runner_output.py scripts/microcausality_finite_range_h_bridge_2026_05_09.py
status: ok
```

Remaining boundary:

This branch does not promote the parent microcausality theorem. The exact
finite-range/quasilocal control of `H = -log(T)/a_tau` remains a separate
bridge.

Next action:

Open a PR for reviewer extraction and independent re-audit. Do not edit
`docs/audit/**`.
