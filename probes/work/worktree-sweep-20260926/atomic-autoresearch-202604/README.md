# Atomic-lane autoresearch, April 2026 (recovered from local directories)

Four Codex autoresearch runs on the atomic lane from 2026-04-19 to 2026-04-26 existed only on this machine. They lived in orphaned directories `~/CI3Z2 Main-atomic-*` (1.9 GB in total). None of their commits reached origin. The atomic runner scripts they used were never on origin either; the later `lane2-atomic-scale-20260428` physics loop on main is a separate, derivation-based lane.

This folder holds the files needed to read and replay the results. Everything else (loop scratch output, logs, a copy of the whole April tree) was deleted with the directories. The copies are verbatim, so local absolute paths inside them point at directories that no longer exist.

Provenance: Codex runs, model gpt-5.4 (from `run-20260419/status.json`). Nothing here has been checked by an independent run. This machine's worker family (`w-jonathonsmac4f50`, claude-opus-5-5) only copied and summarized the files.

## What the lane computes

A tuned lattice Hamiltonian reads out hydrogen and helium energies: the H ground state, the He⁺ ground state, the He ground state, the He triplet state, the He ionization energy and the singlet–triplet gap. It also reports the relative error of each against the known values. The primary metric is `full_rms_relative_error`, the root-mean-square of those errors.

A candidate counted as kept only if both of these held:

- it beat the leader;
- it survived the correlated-basis robustness check on at least two CI slices.

The couplings are fitted to the targets; they are not derived. The numbers are therefore fit quality, not predictions.

## Runs

| folder | branch | loops | result |
|---|---|---|---|
| `run-20260419/` | `autoresearch/atomic-2026-04-19-200` | 178 | full RMS 0.0513 → 0.000655 (kept at loop 93, commit `b28f48dc`); loops 94–178 all rejected |
| `pair-continuum-20260425/` | `autoresearch/atomic-pair-continuum-2026-04-25` | 94–140 | no kept candidate; fixed scalar finite-range pair corrections on top of loop 93 exhausted |
| `multibasis-renorm-20260425/` | `autoresearch/atomic-multibasis-renorm-2026-04-25` | 145–198 | 54 clean rejections, 0 promotions |
| `spin-exchange-shell-20260425/` | `autoresearch/atomic-spin-exchange-shell-2026-04-25` | to 199 | no robust multibasis candidate; the agent replayed the same six-point scout |

Loop-93 leader (39 spatial orbitals), relative errors:

| observable | relative error |
|---|---|
| H ground | 1.50e-4 |
| He⁺ ground | 2.39e-5 |
| He ground | 1.99e-4 |
| He triplet | 6.99e-4 |
| He ionization | 5.86e-4 |
| singlet–triplet gap | 1.29e-3 |

The common failure in the three April-25 runs: gains seen in a small basis did not survive the large-basis CI gate. Candidates collapsed at 32, 40 or 48 virtual orbitals, or they broke one-body invariance.

## Files

- **`run-20260419/`**
  - the program;
  - `results.tsv` (one row per loop);
  - `status.json`;
  - five JSON files taken at `b28f48dc`: scoreboard, current readout, current candidate, next-phase assessment, bound-shell diagnostics;
  - `scripts/`: all 68 `scripts/atomic_*` files at `b28f48dc`;
  - `scripts-64adb833-to-b28f48dc.patch`: what the loop changed in them.
- **Each `*-20260425/` folder**
  - `commits.patch`: the run's three commits in `git format-patch` form. These are the program, the search script and the negative-boundary summary JSON.
  - Bases: pair-continuum and spin-exchange-shell start from `b28f48dc`; multibasis-renorm starts from the pair-continuum head `aa3579bf`.

The base commits `64adb833` and `b28f48dc` are present only as local objects on this machine. The atomic scripts here are therefore the only copy that is reachable from origin.

## Backlog

No task was queued; queueing is the supervisor's step. Two units would decide whether anything here is worth keeping:

1. Replay the loop-93 readout from `run-20260419/scripts/` and `autoresearch_current_candidate.json`, and confirm the six relative errors above.
2. Count the fitted couplings against the six targets. This decides whether 0.065% RMS carries information or is a fit with as many knobs as targets.
