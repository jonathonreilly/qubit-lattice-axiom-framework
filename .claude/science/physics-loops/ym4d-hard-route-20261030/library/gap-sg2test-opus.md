lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T21:59Z

# Row 952 (`gap-sg2test-opus`): GUIDE refutation test of (SG2)

Started 2026-11-14 09:59Z on the Mac mini, worker 1, pinned at commit 8ce7831ef. Claude Opus 5.5, max effort, as author.
This is a GUIDE item: a run may refute (SG2) or guide; no run proves anything. Every statement is marked PROVED,
CONDITIONAL (on named inputs), GUIDE or OPEN. Scripts and logs: `library/guide/lane952/`.

Builds on row 950 (`library/gap-sc-max.md`, Sections 5 and 7: (SG2), frame-lag test 7.4, first run 7.5) and on the
Sussman-Alpoge account (outline `YM4_sketch_500.tex` and complete account at commit 31a47c543775; credited where used).

## 0. Plan (at most eight steps; one step per response; each result appended before the next)

1. Read row 950 Sections 5 and 7 (and row 951 if present). Restate (SG2) and the frame-lag observable exactly.
   Write pass and fail criteria before any run. Duplicate check against `library/open-core.md` and FINISH rows.
2. Port or rebuild the frame-only heat-bath code (row 950's scripts if found). Run the two controls:
   compact U(1) at u_xy must grow like L^3; the temporal-gauge covariance C_0 must reproduce row 950's volume growth at
   beta 2.5-2.6.
3. Slice family A: anisotropic deformations of the layered pi-flux slice u_pi; beta 2.3, 2.45, 2.6; L sweep.
4. Slice family B: tilted copies of u_xy at several tilt angles.
5. Slice family C: slices drawn from the vacuum (typical slices, which the averaged chain sees).
6. Slice family D: slices interpolating between two gauge-inequivalent near-degenerate configurations.
7. Analysis: top eigenvalue versus L with errors and lag convergence, per slice and coupling; verdict per cell.
8. RESULT line.

Compute budget: about 60 minutes in total, one numeric job at a time under `scripts/lab_ops.py numeric-lock`,
BLAS threads 1, nice, peak memory under 2 GB, started only at 50 percent memory free or more.

