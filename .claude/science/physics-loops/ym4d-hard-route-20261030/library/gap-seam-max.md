lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T16:07Z

# gap-seam-max (row 929): the U(1) fact test for (SEAM), then the SU(2) attack

Provenance: Claude Fable 5.2, max effort, Mac mini worker, pinned at commit 5be5e895d of
`claude/ym4d-hard-route`. Author lane, not a check. Research-stage working state; nothing here is a
public claim and nothing here grants status. Statements are marked PROVED, CONDITIONAL (on named
inputs), GUIDE (numeric or heuristic, never a proof step) or OPEN.

## 0. Plan (at most eight steps; one step per response, appended before the next)

1. Read row 929's inputs in full: `library/gap-glue2-opus.md` (row 920) and
   `library/gap-glue2-check-astra.md` (row 921). Write the exact statements used here (INS, (SEAM)_a,
   Delta_theta, S_ev, the threshold, C1-C3, (I1)-(I3)) into Section 1.
2. Repo search and duplicate check (rule 0a, Repo first): grep `library/open-core.md` and the FINISH
   rows for (SEAM), (I1)-(I3) and the U(1) endpoint; list what is already covered. Section 2.
3. STEP A, set-up: write the Gaussian U(1) model (Villain or noncompact) on the same box and time
   extent, with the same twist/sector definitions, and derive S_ev and Delta_theta in closed form.
   Section 3.
4. STEP A, values: evaluate the exact S_ev, Delta_theta at theta = 0, 1 and an interior theta, and
   the threshold; settle "a^-4 law against a^-3 threshold" by hand, with a numeric GUIDE only as a
   cross-check. Verdict: does U(1) fail (SEAM), where, by how much. Section 4.
5. If U(1) passes (SEAM) at some size: the corrected crux form that U(1) fails. Section 5.
6. STEP B: attack (SEAM) (or the corrected form) for SU(2) Wilson at beta 2.3-2.6, or the weakest of
   (I1)-(I3) that suffices; the proof must use a property U(1) lacks and show the exact step where
   the photon breaks it. Section 6.
7. Binding checks: frozen Q_8 and 2T (check 896 D6), ceilings 2/3, 0.775, 4G_3 = 1.0109. Section 7.
8. Result table and the RESULT line. Section 8.

Status of the plan: step 1 in progress (file created 2026-11-14T04:07Z).
