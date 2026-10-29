# H_RP provenance and current checkpoint

## Initial source and authorization

- Task: execute briefs_hrp/AUTHOR_BRIEF_HRP.md in this folder, one author
  context; independent review follows. No commits, pushes, PRs or ledger edits.
- HEAD: 1d221a0063566d5270b60cc543690d7c4d8c68ba.
- Local origin/main: ca2bc7ddf64790da96cd43d42017d000fbfe4808.
- Local origin/ai/execution: 56c5c0ab64f532c5784e895b2f9aa6894fa334e0.
- Remote refs are locally pinned, not freshly fetched: fetching would mutate
  Git storage outside the task's allowed folder. No freshness claim is made.
- Read SCIENCE_WORKFLOW and the physics-loop entry point. Its evidence,
  premise and checkpoint rules apply; the explicit brief supersedes generic
  campaign packets, delegation, commits and PR delivery. Existing target and
  source selections come from the brief; no separate campaign is launched.

## Pre-registration receipts (before scripts or computations)

Native stat, recorded immediately after the first edit, which contained only
the PRE-STATED statements and heading:

```text
HRP.md | bytes=1881 | mtime=2026-10-29T12:52:09-0400 | birth=2026-10-29T12:52:09-0400
SHA256 de2d53d4bfc42fc6b78580e6da82a6f40e5eb72478e1b9705d8a557e2790e3bf
checks/hrp_criteria.md | bytes=2734 | mtime=2026-10-29T12:52:09-0400 | birth=2026-10-29T12:52:09-0400
SHA256 3e00f5ec5bbc32522636004aa72628c45884fe3762573c047e1105593ea82173
```

## Current checkpoint

Target: finite-torus link/site RP; bare-marginal transfer; polynomial limit
closure; actual sphere coordinate-reflection geometry; append-only F3/F25
corrections. Accepted premises: compact-group Haar integration, the specified
Wilson regulator, and separately named convergence/extension hypotheses.
No new physical axiom is proposed. H_reg, (EXT), common-algebra selection,
rotational covariance, interaction and mass gap are not targets proved here.

Status: written proofs and source-level author verification complete. The exact
runner stopped before computation at the nice-priority guard. A specific
waiver question is pending; no waiver is inferred from elapsed time.
Independent review/banking are pending. Next decision: run numerics only if
the priority requirement can be satisfied
or the owner explicitly waives it. The source identities below govern reuse.

## Source coverage and proof route

- Read ASSEMBLY55 N0/N1F/N1S/N3/F3/F25 and surrounding domain qualifications;
  SPHERE55 §§1–2, §5.2 and appended §§9–13 errata/status; P4 §1.1 and
  §4.1–4.3; HINT's actual bare-marginal item in §5; PANEL_P1's closure and
  positive-half contract; OSLEAF55 D1–D9, RP-lat, CLOSURE-sep, CONTRACT-sep,
  relevant errata and §13 bridge statement. PROOF L9a/L9a-m/L9a′ and
  S4′/S4″/Decision-4 definitions were read at their actual current offsets.
- Checked ROTDEF's bare clover and chain definitions, RLARGE's exact chain
  and conditioned-history distinction, SRCAN55 §2.1's source perturbation,
  and OSLEAF55 §6's trajectory/normalization convention. Read HANDOFF's
  current full-proof completion bar and final checkpoint. No full-proof
  completion is asserted.
- Pinned all twelve working sources and four main imports in
  `checks/hrp_sources_initial.json`. Read the main June 5 proof completely;
  inspected the May 10 scoped identity, June 2 carrier/holonomy/split/support
  proof and April 29 parent dependency/scope surface. The parent's fermion
  proof is not used or certified. Import status is component-specific in HRP.
- Prior-art classification: Wilson kernel/RP is established mathematics;
  this task is the requested re-verification and periodic/sphere interface
  repair, not a novelty claim. The four named main imports were found with
  `git ls-tree`/`git show` on the pinned local origin/main. No broad open-PR
  search or new campaign selection was needed for this assigned brief.
- Primary proof route: split every crossing Haar link into two independent
  half-links, then integrate an absolutely convergent positive feature
  expansion. This avoids a periodic temporal-gauge assumption and covers
  all bounded half-observables. Separate representation-ring derivation
  checks the Wilson-kernel sign. Site RP conditions on both fixed planes.
- Sphere route: classify every chart/seam 2-face directly; check all
  crossing higher cells are fixed, and sum the actual radial cell weights.
  No regulator repair is needed. This is not a new seam-transparency claim.

## Literature provenance

Web search/open on 2026-10-29 located Osterwalder–Seiler, Ann. Phys. 110
(1978), DOI 10.1016/0003-4916(78)90039-8. The publisher abstract was
available in search; article and PDF fetches returned 403. Seiler's LNP
159 book and lattice-chapter publisher pages were available, full text
subscription-only. Their detailed statements are not treated as read;
recalled attribution is marked [m] in HRP, never load-bearing.

FILS IHES/P/78/224 PDF was opened and §2, Theorems 2.1–2.2 and their
commuting-algebra/exponential-expansion argument were read. Links and
access boundaries appear in HRP §7. All load-bearing steps are proved
in HRP itself, including convergence and integration of the expansion.

## First execution attempt — preserved failure

- Criteria SHA-256 remained
  `3e00f5ec5bbc32522636004aa72628c45884fe3762573c047e1105593ea82173`.
- Initial script SHA-256:
  `31af46940c861b09cc7aac42efd00261790296b652bbeacd1ede6c6362c137d1`.
- Initial launcher SHA-256:
  `2dffd4949e2185a4b2fe5d192dd0f178b2d044a3849cfa469287db7b92215582`.
- Exact initial source bytes are archived as `checks/hrp_attempt1_script.py`
  and `checks/hrp_attempt1_run.sh`. They were recovered by reversing only
  the documented later additions/timing change, then checked against the
  hashes recorded before those changes. Both identities match exactly.
- Command: `sh checks/hrp_run.sh`. Initial preflight reported load
  1.46044921875 and 37 percent free memory; complete native receipts
  are in `checks/hrp_attempt1_preflight.txt`, including the second
  memory check after acquiring the lock.
- The exact prescribed mkdir-until loop acquired the lock. `nice -n 10`
  printed `nice: setpriority: Operation not permitted`; the script's
  independent priority assertion stopped it before the START line,
  group construction, or any Gram computation. `/usr/bin/time -l` also
  reported `sysctl kern.clockrate: Operation not permitted` after timing.
- Files: `checks/hrp_attempt1_out.txt` (empty), `_err.txt` (traceback),
  `_time.txt` (0.08 s real; numeric_exit=1, cleanup_exit=0). The directory
  lock was removed exactly once. No job was left running.
- This was an execution prerequisite failure, not a failed RP theorem
  or a numeric PASS. The user was asked asynchronously whether to waive
  only the nice-priority requirement; no answer had arrived at this
  checkpoint. Numeric execution is held; the authorized proof and
  append-only wording work are complete.
- Recovery under the original brief: run `sh checks/hrp_run.sh` from
  this folder in an environment permitting `nice -n 10`. A failing
  preflight or priority guard is not permission to relax a condition.

## Author verification and changes after the prerequisite failure

- Read the complete new proof and exact-check script in bounded chunks,
  and the complete two-file appended diff. Re-derived the split-link
  noncommutative word, the two periodic partitions, the shared site-plane
  conditioning, and the sphere prism factorization. Corrected a notation
  ambiguity: R is linear reflection of tests; Θ is antilinear reflection
  of observables, so the form contains R(F*) and exactly one conjugation.
- Added an explicit L² truncation extension and the exact source filenames.
  Hand-derived the two asymmetric controls: the malformed one-cell Gram
  has raw spectrum 1,0,0,0 but a negative Hermitian-part eigenvalue; the
  asymmetric same-half coupling Gram is nonsymmetric yet similar to a
  positive matrix. These are analytic pre-computation predictions, not
  fabricated runner results. They show why both raw-negative-spectrum
  criteria must be allowed to report failure.
- Added an exhaustive Q8 split-word check and crossing-4-cell invariance
  assertions to the still-unexecuted numeric body. These strengthen the
  pre-registered factorization/geometry checks; criteria and thresholds
  are unchanged. No post-hoc numerical probe has been performed.
- Changed the launcher's timing option from `time -l` to portable `time -p`
  because the former's extended resource query was sandbox-denied. The
  script still self-monitors/reports RSS and wall time, and still refuses
  to compute unless nice priority is at least 10. This does not waive a
  resource rule. The original failed attempt remains unchanged.
- Mechanical validation is recorded in `checks/hrp_author_validation.json`:
  Python syntax parse, shell syntax, whitespace diff, immutable criteria,
  original PRE-STATED prefix, source stability and append-only byte-prefix
  verification. These checks do not execute the scientific runner and do
  not certify its eventual results. The manifest binds all author artifacts
  except itself. No independent reviewer was launched in this author seat.

## Scope of edits

Created HRP.md, HRP_LOG.md and `checks/hrp_*`; appended only to SPHERE55.md
and HANDOFF.md. No editable prompt/brief file changed. No platform
instruction, axiom, audit or ledger file changed. The only temporary
mutation outside the assigned folder was the exact root-level numeric
lock explicitly prescribed by the brief, which was removed after the job.
