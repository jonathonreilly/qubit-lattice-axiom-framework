# Author brief: close H_RP (reflection positivity) on both routes

Lead: Claude Opus 5.5, 2026-10-29. Executor: one Codex author context; a separate reviewer follows.

## Why this item
Of the four top-level inputs to T_OS (H_reg, H_RP, H_Euc, H_int; ASSEMBLY55.md §4), H_RP is nearest to closure.
- **Flat route:** ASSEMBLY55 N3 records a mathematical MATCH, but nothing is banked. PROOF L9a is a pre-S24 "IMPORTED-AND-REVERIFIED" entry that is not in [S26-BANKED].
- **Sphere route:** F3 is "OPEN (small)". The RP that is consumed (θ_μ, great spheres through the base point S) is not the RP that was banked (equatorial). SPHERE55 §1.5 supports it with a single line, and that line contradicts §5.2 and §13.
- **F25:** a HANDOFF wording error.

Deliver a reviewed, bankable H_RP in exactly the form that N1F and N1S consume.

## Read first
- **This folder.** Use `grep -n` to find the anchors and read by offset. Never read a file of more than about 1000 lines whole.
  - ASSEMBLY55.md: N0, N1F, N1S, N3, F3, F25.
  - SPHERE55.md: §1 (lattice K_a and regulator), §1.5, §2, §5.2, §12 errata.
  - CODEX_REVIEW_P4.md: §1.1, §4.1.
  - CODEX_REVIEW_HINT.md: item 4 (the bare marginal is invariant under normalized soft kernels).
  - PANEL_P1.md, OSLEAF55.md: the OS algebra, positive-half polynomials, supports.
  - PROOF.md: L9a, L9a', L9a-m (around line 1016).
  - HANDOFF.md: "Active full-proof goal" (the completion bar).
- **Main, via `git show origin/main:docs/<name>`.** This is prior work. You may use it, but only after re-verifying it, and you must cite each item as used or contradicted.
  - AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md: SU(N) Wilson link-reflection RP on an open temporal slab, by a representation-ring proof.
  - REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md
  - GAUGE_OS_STEP1_WILSON_PLAQUETTE_DECOMPOSITION_THETA_INVARIANCE_REFLECTION_HERMITICITY_NARROW_THEOREM_NOTE_2026-06-02.md
  - AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md
- **Literature, for method and hypotheses only:** Osterwalder–Seiler (1978); Seiler, Lecture Notes in Physics 159; Fröhlich–Israel–Lieb–Simon. Re-prove every load-bearing step here. Mark anything cited from memory as [m]; an [m] item is never load-bearing.

## Deliverable 1: H_RP-flat, as a theorem in the exact form N1F consumes
1. **Finite-torus Wilson RP for SU(N), with a complete proof.**
   - Periodic torus; the side in the reflected direction is even.
   - Both reflections: link reflection (the plane bisects links) and site reflection (the plane passes through sites). On a periodic torus each reflection has two fixed planes, and both must be handled.
   - Positive plaquette couplings β_P that are θ-symmetric and may depend on position. Say whether β_P ≥ 0 is sufficient, and where it is used.
   - All gauge-invariant observables supported in the closed positive half, and all observables if that is needed.
   - The slab note fixes temporal gauge. Either remove that step, or prove that gauge-fixing the crossing links is legitimate on the periodic torus. Note that a gauge-invariant F loses nothing under gauge averaging.
2. **Transfer to the soft-RG construction.**
   - The OS-algebra elements e_a(x) are functions of the bare links.
   - Verify from the definitions on disk that the soft chain's level-0 marginal is exactly the Wilson measure, so that lattice RP applies directly.
   - State the support condition: distance > a from the plane, or the site-reflection variant. It is eventually true for fixed positive-time tests.
   - If any construction step (S4' averaging, normalisation, tilt, coupling trajectory) changes the bare measure, find it and say so.
3. **Passage to the limit.** RP for every positive-half polynomial must survive the common subsequence used by N1F (finitely many moments for each fixed polynomial). If "negative errors tending to zero" are needed, this is where they enter. Be explicit about which H_reg and (EXT) facts are consumed; do not prove those here.
4. **Banking statement.** Give the exact claim scope, the hypotheses, and every place the result is consumed.

## Deliverable 2: θ_μ RP on the sphere lattice K_a (repairs F3)
- Read SPHERE55's actual definitions:
  - K_a and its cells, including the prism cells that cross {x_μ = 0};
  - the position-dependent bare coupling;
  - the measure.
- Prove, or refute with an explicit counterexample, that each coordinate reflection θ_μ is an RP reflection for that regulator. Check these sufficient conditions:
  - θ_μ maps K_a onto itself;
  - the couplings are θ_μ-symmetric and ≥ 0;
  - every cell meeting both open halves is θ_μ-invariant, and its holonomy factors as W·θ(W)^{-1} with W positive-half-determined (up to fixed-plane links in the site case);
  - the measure is a θ_μ-invariant product of Haar measures.
- If some cell fails, propose the smallest regulator change that restores RP, and list what it disturbs (SO(5) on the cap, SPHERE55 §5.2).
- Resolve SPHERE55's internal inconsistency (§1.5 vs §5.2/§13) in an appended, dated erratum. Quote; do not rewrite history.

## Deliverable 3: wording
- Correct F25's HANDOFF sentence in a new, appended HANDOFF subsection. Do not edit the earlier text.

## Exact checks (class A, finite, pre-registered)
- **Criteria first.** Write `checks/hrp_criteria.md` before any script. It holds statements and thresholds only, with no session-derived constants. Record its stat in HRP_LOG.md.
- **Positive checks.**
  - Gauge groups: Z_2, Z_3, and a finite subgroup of SU(2) (Q8, or the binary tetrahedral group of order 24).
  - Lattices: small periodic tori, 2D and 3D, with side 4 in the reflected direction, in both the link and the site case.
  - Compute the RP Gram matrix ⟨Θ(F_i) F_j⟩ exactly, on a basis of positive-half observables, by enumeration or an exact transfer/character method. Check that it is PSD.
  - Include θ-symmetric, position-dependent β_P.
  - Include a small model of the K_a crossing-prism cell structure, built from SPHERE55's definition.
- **Negative controls.** Each must give a negative eigenvalue; if one does not, report it.
  - One β_P < 0 on a crossing plaquette.
  - One non-θ-symmetric crossing cell.
  - A non-θ-symmetric coupling.
- **Resources.**
  - Each process stays under 1 GB RSS; the script checks itself and exits if exceeded.
  - Each job runs under 20 min.
  - Use `nice -n 10` and `OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=1`.
  - Start a run only if load < 8 and at least 30% of memory is free (`memory_pressure`).
- **Numeric lock.** `until mkdir /Users/jonreilly/Projects/Physics/.claude/worktrees/ym4d-hrp/.locks_hrp_numeric 2>/dev/null; do sleep 20; done`, then run, then `rmdir` exactly once. No trap, never pkill, leave no process running.
- Finite checks confirm the algebra only. The theorem is the written proof.

## Write
- **HRP.md**:
  - its first edit is a PRE-STATED section, statements only; log that section's stat and byte size in HRP_LOG.md;
  - then the proofs, each marked PROVEN, ARGUED or OPEN;
  - an "Inputs consumed" table;
  - an "Import status" table (IMPORTED-AND-REVERIFIED or IMPORTED-NOT-YET-REVERIFIED);
  - the banking statement.
- **HRP_LOG.md**: provenance.
- **checks/hrp_\***: criteria, scripts, `_out.txt`, `_err.txt`, `_time.txt`.
- **SPHERE55.md**: the appended erratum only.
- **HANDOFF.md**: the appended subsection only.

## Rules
- Honest statuses. Report a failed check as failed, and label any post-hoc probe as post-hoc.
- No commits, pushes or PRs; the wrapper commits after independent review.
- Edit nothing outside this ym4d-proof folder. No audit or ledger files. No axiom edits.
- Final message: under 300 words, with verdicts per deliverable and the open residue.
