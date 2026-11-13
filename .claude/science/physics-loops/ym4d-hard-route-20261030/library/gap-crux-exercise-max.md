lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-12T13:30Z

# Exercise v2 on the gap crux, first run at max (row 743)

Provenance: Claude Fable 5.2, max effort, as author, one session, no subagents. An earlier run of this item wrote the header only (at commit 7c58883f4). This run is pinned at commit 18aeda83a, date 2026-11-12 UTC.
Nothing in this file is checked by another model. Nothing here grants status. Every statement below carries its own mark.

Skill: `docs/ai_methodology/skills/exercise/SKILL.md` at 1eb15ac428 (fetched to /tmp/gcx743/skill, read in full). The target reads no framework axiom, so the refresher read is replaced by `GOAL.md` and the rules of `FINISH.md` (lines 1-84, 299-349), as the skill allows for a standalone proof target.

**What this run did not cover** (kept true as the run goes):

- The account `YM4_1400.tex` was not opened. Its statements are used only as the definition files quote them.
- `library/gap-flux-exercise.md`: read 3.0, 3.1 (C1, C2), 8.2 to 8.4. Step 9 was not read; its content is taken from skeleton 13.16.
- `library/gap-flux-exercise-check.md` Section 7: not read; its three corrections are taken from skeleton 13.16.
- `library/gap-seed-limit.md`: Sections 1, 5, 7 and the statement of Theorem L3 read; proofs not read.
- `library/gap-seed-shape.md`: status block and Section 3 read; the rest not read.
- `library/gap-crux-restate.md`: Sections 1, 2, 3.1, 3.2, 3.4 read in full; 3.3, 4, 5 not read before step 5.
- No blind check of the plain version (no subagents).

## Status block

| Step | State | Main result |
|---|---|---|
| 0 record | done | lists below |
| 1 wall | done | below |
| 2 inventory | not started | |
| 3 reason up | not started | |
| 4 assumptions | not started | |
| 5 compare | not started | |
| 6 filters | not started | |
| 7 routes | not started | |
| 8 attempts | not started | |
| 9 report | not started | |

## Step 0. Where the record is; open and closed lists

**Open now** (the brief's list): `library/gap-skeleton-final.md` Sections 0 to 3 and 13.15 to 13.17; `library/gap-flux-exercise.md` Step 9 and 8.2 to 8.4; `library/gap-flux-exercise-check.md` Section 7; `library/gap-crux-restate.md`; `library/gap-seed-limit.md`; `library/gap-seed-shape.md`; the account's statements. Reading state: see the list above.

**Closed until step 5** (the brief's list): `library/gap-means-max.md` (row 737), `library/gap-means-astra.md` (738), `library/gap-form-exercise.md` (735), `library/prior/gap-lit-*.md` (739 to 742), every other `library/gap-*.md`, `library/exercise-skill-v2.md`, FINISH rows 697 to 742. I add skeleton Section 13.18 (written from rows 737 to 744 after this row was queued) and FINISH rows 744 to 747.

One exposure to record: my memory note on this lane (written by an earlier session on row 737) says in one line that row 737 has a "Theorem R (even seed (ES) gives two of the three seeds)" and a lattice projective plane with a negative character term. I read that line while looking for navigation hints. I did not open the files. Steps 2 to 4 below do not use it.

Literature: the lane's records (`library/prior/gap-lit-*.md`) are on the closed list. Before step 5 I use only statements of results that the open files quote, and results I recall, marked `recalled`.

## Step 1. The wall, stated twice

**Plain version.** We want to show that the quantum theory of the SU(2) gauge field in four dimensions has a mass gap: the lightest excitation has a positive mass, so all correlations die off exponentially with distance. The lane has a proved machine for this. If, on one periodic box of one physical size, the excited states together carry little thermal weight (a "seed"), then every larger box has a gap, and so has the infinite-volume theory. The machine works for any model. What keeps failing is the seed itself. It has to be checked on a box many correlation lengths wide, where the interaction is strong. There no expansion has a small parameter, and every exact tool known to the lane also holds for models that have no gap. Getting past the wall means: a proof of one seed, or of the gap by a route that needs no seed. Analogy (only an analogy): we have a proved domino chain and no hand to push the first domino.

**Precise version.** Quoted, not rewritten.

- Target (GAP): `library/gap-skeleton-final.md` Section 1: sigma a canonical component of a volume-first limit at reference coupling g; then spec(H) is in {0} union [m, infinity) with m > 0, on the cyclic sector of tr(F^2).
- Lattice engine (proved, checked by two models): Theorem S and Corollary S3' (`library/gap-crux-restate.md` L170-222). If s = S(N; (2N)^3) < 1/5041 at one N >= 3, then m(L^3) >= log(1/(5041 s))/N for every L >= 2N.
- The three seeds (checked): Theorem S-w and Corollary EV (`library/gap-flux-exercise.md` 8.4): S_w(N; (2N)^3) < 1/5041 for w one of per, full, kappa gives (G_ev) on all cubes; Theorem EV-L (8.2) turns (G_ev) into clustering of every periodic limit on centre-blind functions.
- Scaling form: (SEED-phys) and Propositions P, P' (`library/gap-seed-limit.md` Section 5): the seed at physical size at most ell_*, uniformly in the cutoff, gives spec(H) in {0} union [M_*, infinity), given the T0 chain's continuum datum, (H2), (TOT).
- The wall: (SEED-phys), or its even form, at an effective coupling of order one. By the rate filter the seed size is more than 8.5 correlation lengths of its cube. Skeleton 13.15: equivalently (BDD-Delta) and (Z-UNB). Skeleton 13.17: a brief must name the means (M1) to (M4), or a fifth, by which the criterion is verified at the scale of the correlation length.
- Does not count: a statement at a size below the correlation length; a gap in lattice units that is not uniform in the cutoff; an argument that also runs for U(1) at weak coupling, for the fundamental-adjoint action at its transition line, or on a slab of critical width (skeleton Section 3); a route whose last step is the seed again.
- Counts as progress: a seed proved; an exact equivalence of the seed with a statement that a known tool reaches; a filter of the lane shown wrong; a route outside the frame with its first statement proved.

No blind check ran (no subagents). The plain version is corrected in step 9.
