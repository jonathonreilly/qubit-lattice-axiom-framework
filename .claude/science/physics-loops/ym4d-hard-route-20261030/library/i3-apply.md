lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T00:44Z

# i3-apply (FINISH row 643): edits applied to `library/i3-cert.md`

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort high, Mac mini worker 2, branch `claude/ym4d-hard-route` at c33161ce2. Not an audit. Started 2026-11-10T12:44Z.

Outputs of this row: `library/i3-cert.md` (edited) and this log.
Inputs: `library/i3-repairs.md` (row 634), `library/cov-x-check.md` (row 633), `library/cov-global-check.md` (row 636, defect (6)), `library/cov-x.md` (row 628, (c2')), `library/cov-xstar-check.md` (row 639, `C_2''`), `library/i3-cert-check.md` (row 630).

## Repo search

- `library/open-core.md`: no entry for i3-cert, i3-apply, (COV) or `C_2''` (grep). This row attacks no open lemma; it edits text.
- FINISH rows near this one: 624 (i3-cert), 630 (its check), 633 (cov-x-check), 634 (i3-repairs), 636 (cov-global-check), 639 (cov-xstar-check), 642 (cov-apply, which edits `cov-global.md` and `cov-xstar.md` and is told not to edit `i3-cert.md`). None of them edits `library/i3-cert.md`; row 643 is the one row allowed to.
- `library/i3-cert.md` is unchanged since 01af230c4 (the commit `i3-repairs.md` quotes), checked with `git diff 01af230c4 HEAD`; so every "Old" fragment of i3-repairs is quoted from the text being edited.
- Credit: the argument of i3-cert is Sussman and Alpoge's (`YM4_1400.tex` at 2bc0658f91d2; their text names Claude and Codex as authors), paragraph `hi:prepared-real-endpoint`; the nest and the stage test are Bałaban's (CMP 122). The repairs are by the checks named above (Claude Opus 5.5) and by `library/cov-x.md`, `library/cov-xstar.md` (Claude Fable 5.2).

## How the edits were made

Each edit is an exact replacement of an old fragment by a new one. A small text script (in my own scratch folder, not a proof step) asserted that each old fragment occurs exactly once before replacing it. No numeric job was run. Memory free at start: 61 percent.
