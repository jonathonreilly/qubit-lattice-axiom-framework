# Block 171 Landing Checklist (for the fresh session)

Everything needed is IN THIS DIRECTORY — trust nothing from the
prior session's memory or scratchpad.

State at freeze (2026-08-21): drafts complete and verified by their
worker — runner baseline 7/8 (gate H = note-at-final-path, pure
landing-time state; 93/93 scope keys TRUE via the declared draft
fallback), 63.1 s baseline / 70.4 s --deep (both 7/8, A-G PASS);
15 mutations one per gate, the twelve A-G mutations verified
EXCLUSIVE (changed == {target}); the three gate-H mutations are
degenerate at draft time (H already failing) — after the note is
at its final path the standing sweep must show 15/15.

1. Branch: physics-loop/toe-axiom-closure-block171-generator-trilemma-<date>
   off PARENT_COMMIT c2ff6abd1de9dc16a4e8255c164b54762dce8fc2
   (the b170 tip; PR chain base = #7146's branch
   physics-loop/toe-axiom-closure-block170-closure-audit-two-20260821).
2. Copy block171_note_draft.md ->
   docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md
   and block171_runner_draft.py ->
   scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py
3. Pins: PARENT_COMMIT/PARENT_ARTIFACT_BLOBS are already REAL
   values (verified by the draft worker: b170 note blob 7560ecb6…,
   runner blob 8e530d7a…; STALE c57c1c29 carries neither). Re-run
   the five-pin refresh anyway against a fresh `git fetch origin`
   (CURRENT_MAIN was 38109c451a at freeze — if main moved, refresh
   and re-verify before ANY commit; the checkpoint-19 lesson).
4. N5 fence: N5-prefix selection from the note; single-line
   N5_FENCE literal (triple-quote guard).
5. Baseline must be 8/8 exit 0 once the note is at its final path;
   then --deep; then the sweep via mutation_sweep.py (in this
   directory; sed its RUNNER = line) — 15/15 required, and gate on
   the sweep tail + a re-fetch of origin/main immediately before
   commit.
6. Stage exactly 5: note, runner, citation manifest (run
   docs/audit/scripts/write_citation_graph_manifest.py after
   run_pipeline.sh exit-1-at-epoch-gate + scoped restore of
   docs/audit/ docs/publication/), the runner-cache log
   (scripts/cached_runner_output.py x2), and the block pack
   NO_GO_LEDGER.md (write GOAL/TRACE_GATE/NO_GO_LEDGER under
   .claude/science/physics-loops/toe-axiom-closure-block171-…/;
   only NO_GO_LEDGER is staged).
7. audit_lint.py --strict; commit "physics: solve the generator
   trilemma and open the kernel program" (+ Co-Authored-By
   trailer); push; PR stacked on #7146 using b171_pr_body_draft.md.
8. AFTER landing: B2 per B2_B3_SPECS.md (read
   b171_profile_table_v2.py from THIS directory — v1's
   NULL_FIXTURES is refuted); B3 to codex (pool unlocked
   Aug 22 12:35), pins in
   ../hygiene-20260821/GENERATOR_PROGRAM_PINS.md.

Owner-bar items pending (never adopt): the bridge-axiom memo if
the refinement census also collides; the joint-weight design fork
(chain-rule order vs one-shot Gibbs joint); the b141/b142
disposition; the e_x = -1 class.
