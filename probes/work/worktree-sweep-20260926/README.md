# Worktree sweep, 2026-09-26

Owner request: free local disk by removing every worktree not touched in the last three days, Codex worktrees included, after saving any science to `ai/probes`.

Rule applied: a registered worktree of this repository was removed when its newest working-tree file was older than 2026-09-23 06:22 EDT. 24 of 80 matched and 56 were kept. Two leftover probe-worker directories, no longer registered as worktrees, were removed as well. Before removal, each worktree was checked for a process running inside it, for uncommitted, untracked and ignored files, for whether its head is on origin, and for its PR state. `manifest.json` lists each one with its head and where its content now lives.

## Where the removed work lives

| worktrees | content | preserved at |
|---|---|---|
| 15 Codex publication branches | open PRs #8551, #8552, #8557, #8560, #8561, #8565, #8566, #8567, #8569, #8589, #8594, #8600, #8604, #8609, #8610 | branch heads on origin; each PR already has its re-execution unit, and its judgment units where the generator makes them, in `probes/TASKS.json` |
| 4 Codex publication branches | PRs #8635, #8650, #8661, #8672 (closed on landing) | reviewed, narrowed source landed on main in `9d8596c758` from the same heads; their deferred residuals are in `probes/work/deferred-science-20260924/` (`batch-12.json`, `landing-rollup.json`) |
| 1 Codex process branch | `codex/science-token-efficiency-20260920` | merged as #8528 (`5d784d8ccd` on main); methodology, not science |
| 4 probe-worker worktrees | units `J:note:COMPOSITION_LAW_SELECTION_...`, `J:note:G_BARE_PARENT_...`, `J:note:NATIVE_GAUGE_TRANSFER_C00_...`, `J:provenance:PR8024` | heads on `ai/probes`; each unit was later completed by another worker with a committed, self-checked log and no hit; the uncommitted files two of them held are rescued below |
| 2 leftover probe directories | `J:attack-g:PR8155`, `J:attack-g:PR8168` | both units completed with committed logs and no hit; one draft rescued below, the other directory was empty |

Every removed Codex worktree was clean. Its ignored files were regenerated audit data and an empty runner-cache staging directory.

## Rescued files

These files existed only on the local machine. They are stored as `rescued/<worktree>/<original path>`, so each can be restored to its original location.

1. `rescued/J-provenance-PR8024/`: `provenance_theorem_numbers.py` and its run log. The run was made by a grok-4.6 worker (`w-macbookpro90c72-jda2d`) at 2026-09-19T04:43Z; the self-check passed, there was no hit, and the stdout hash matches the log. It was never pushed. The committed run of the same unit (claude-opus-5, `provenance_theorem_numbers_full.py`) is broader: it finds 190 statement numbers, all sourced. Both runs conclude there is no provenance hit. PR #8024 is closed.
2. `rescued/J-note-NATIVE_GAUGE_TRANSFER_C00_LOWER_BOUND_RUNG_TWELVE_BOUNDED_NOTE_2026_06_12/`: `hessian_and_power.py`, a small exact falsifier. It checks Re Tr I = 3, the power (N_c² − 1)/2 = 4, 12⁴ = 20736, and the Cartan-line expansion Re Tr U = 3 − θ² + O(θ⁴) against 3 − ½|X|². It was never run through `run_probe.py`, so it has no log. The unit was completed with a different script (`weyl_torus_bessel_identity_exact_constants.py`, no hit).
3. `rescued/J-attack-PR8155/`: an earlier draft of `probes/work/pr8155/walk_bound_brute.py`. The committed version is the one the completing log ran (grok-4.6, no hit), and it is broader: walks on Z³ and on the 7³ box up to length 24, plus the walk-length and neighbour-step inequalities behind the bound. PR #8155 is closed.

The rescued files sit outside `logs/probes/`, so harvest and claim do not count them. They are archival copies for review.

## Backlog (worktree pass)

No new units were added for the worktrees. Every open PR from the removed branches is already queued. The residuals of the landed PRs are already in the 2026-09-24 deferred bundle. Each rescued file duplicates a completed unit, and that unit reached the same result.

## Second pass, same day: Codex scratch directory

The owner then asked to delete two more things.

- **`~/Documents/Codex/physics-sync-2026-09-21-second`** (4.4 GB, not a worktree). It held raw output from three unpublished computations: geometric fixed-rate formation, the dimer-routed colour-wave screen, and its N = 256 follow-up. Their science is saved in `codex-sync-2026-09-21-second/`, with its own README and manifest.
- **Two stale worktrees of an unrelated repository.** Their uncommitted edits were kept in local backup branches; nothing of theirs is in this repository.

Two worked computations were queued for independent recomputation and replay of the recovered result sets. Each will be run twice: `C:recovered-fixed-rate-geometric-formation:a1/a2` and `C:recovered-dimer-routed-color-waves:a1/a2`, in `probes/tasks/recovered-codex-science-20260926.json`.

## Third pass, same day: 48-hour rule

The owner then asked to remove every Claude and Codex worktree not touched in 48 hours, and to keep a commit only for science. Doubtful science goes here. Fourteen directories were removed; `atomic-autoresearch-202604/manifest.json` lists each one with its head.

- **Five probe-worker worktrees** (`~/.probe-workers/Physics-baremetal-probes/`): `C-six-axis-noise-map-3plus1-a2` and `slot-1` to `slot-4`. Four were clean with their head on `ai/probes`. `slot-1` held one unpushed commit of 40 automatic R re-execution logs from 2026-09-20 that no model had read; it was discarded. Those R units remain in the backlog, since their logs never reached origin.
- **The Claude worktree `gravity-toe-lane-work-427b0b`**: its 7 unpushed commits are earlier drafts of Dirac–Kähler blocks 201–212. Every note and script they touch is on origin in a later corrected version, so nothing was kept. Its 1144 dirty files were regenerated `docs/audit` and `.claude/science` state, already triaged on 2026-09-25.
- **Eight Codex directories `~/CI3Z2*`** from April, none a registered worktree any more:
  - two one-iteration smoke runs and two directories holding only supervisor logs were discarded;
  - four atomic-lane autoresearch runs were kept in `atomic-autoresearch-202604/`, because neither their commits nor the atomic runner scripts ever reached origin. Their science is a fit of H and He levels to 0.065% RMS, plus three negative search boundaries. It is not independently checked; see that folder's README for the two units that would decide it.
