# Codex scratch recovery: physics-sync-2026-09-21-second

2026-09-26. At the owner's request, the Codex working directory `~/Documents/Codex/physics-sync-2026-09-21-second` was deleted: 4.4 GB in 25,669 files. It was not a worktree. Almost all of its space was raw simulation output from three computations, run on 2026-09-21, whose results were never published:

- Open PR #8589 says "the fixed-rate Monte Carlo follow-up remain[s] outside this milestone".
- No PR branch contains the dimer-routed screen or its N = 256 follow-up.

The analyses, assessments and independent checks for these runs were committed only on a local Codex branch that is not on origin: `codex/mobile-record-post-formation-campaign-20260923` (`eb34060bef`, 73 commits ahead of `origin/codex/mobile-record-formation-20260920`). This directory saves the science from both places. `MANIFEST.json` gives each file's original path and SHA-256, and lists what happened to every entry of the deleted directory. The saved source, protocol, analysis plan, analyzer, `RESULTS.json` and `PER_HISTORY.json` hashes equal the identities recorded in the assessments and run manifests.

## The three result sets

These are the author's assessments of finite numerical runs on supplied classical processes. They are not theorems, and they make no physical identification.

1. **Geometric fixed-rate formation** (`geometric-fixed-rate-formation/`).
   - **Setup:** 2,496 seeded histories on periodic cubic lattices N = 16, 32, 64, 128. Slide rate κ = 1; paired-birth rates β = 0.1, 1, 10. Each history ran from empty to its first complete matching, with no plaquette moves afterwards (ν = 0).
   - **Findings:**
     - The long-wavelength transverse amplitude S₁ stays near 0.19 from N = 16 to 128 at all three rates.
     - Winding and low-shell ratios stay of order one. Some pointwise intervals exclude the flat-spectrum or Gaussian reference values.
     - At fixed rate, mean formation time per site is roughly independent of size.
     - At N = 128, 12–26% of sites host more than one birth, so sites are reused.
   - **Context:** open PR #8589 proves the slow-birth regime, which is a different question.
   - **Open step named by the assessment:** the ν = 0 process freezes once full. Propagation needs local record moves on the formed state, the ensemble those moves preserve, and a transverse dispersion law there.
2. **Dimer-routed colour waves, finite screen** (`dimer-routed-dynamic-screen/`).
   - **Setup:** 960 histories at N = 16–128 on two frozen full matchings. They test the conditional Euler propagator for record-colour waves, whose asymptotic statements are in open PRs #8600 and #8604.
   - **Findings:** at the quarter period, the propagation error falls from 1.87–1.92 at N = 16 to 0.73–0.78 at N = 128. The signed cross term rises from 0.04–0.08 to 0.55–0.68 (its limit is 1). Finite damping is large at every tested size.
   - **Status:** the runs neither establish nor contradict the limit. The assessment records that a separate aggregate check was still pending.
   - **Frozen sources:** `run/frozen_sources/` holds the exact versions the screen ran with. Its `DIMER_ROUTED_RECORD_TRANSPORT.md` is an earlier revision of the construction note than the copy in `assessment/`.
3. **Dimer-routed N = 256 follow-up** (`dimer-routed-256-followup/`).
   - **Setup:** 16 histories, declared after the screen's outcomes had been inspected.
   - **Outcome:** 10 completed with verified receipts, 2 failed, and 4 had not started by the hard deadline.
   - **Analysis:** only a censored descriptive analysis exists. It is not pooled with the screen.

## What was saved and what was deleted

- **Saved:**
  - assessments, protocols, analysis plans and corrections;
  - generating sources (`geometric_partner_growth.cpp`, `dimer_routed_dynamics.cpp`) and the setup, run, analysis and plot scripts;
  - results (`RESULTS.json`, `TABLE.md`, per-history sufficient statistics, figures);
  - verification records, plus the independent reviewers' reports and scripts;
  - run manifests with every seed, command and file hash;
  - small validation outputs.
- **Deleted:**
  - per-history trajectories and endpoint states, geometry fixtures, raw csv and stdout;
  - compiled binaries and a plotting virtualenv;
  - copies of published papers;
  - publication tooling and logs whose science is in open PRs.
- **Regenerating the raw data:** trajectories and fixtures can be regenerated from the manifest seeds with the saved sources. Byte-identical output would also need the recorded compiler.

## Backlog

`probes/tasks/recovered-codex-science-20260926.json` adds two worked computations, each for two independent runs:

- `C:recovered-fixed-rate-geometric-formation:a1` and `:a2`
- `C:recovered-dimer-routed-color-waves:a1` and `:a2`

They ask for the checks the original reviews left open:

- an independent recomputation of every table value and interval from the saved per-history statistics;
- an independent small-N replay, compared against the saved tables.
