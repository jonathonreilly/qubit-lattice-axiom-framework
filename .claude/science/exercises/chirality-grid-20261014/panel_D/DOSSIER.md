# Panel D dossier: four owner decisions surfaced by the chirality exercise (2026-10-14)

Jon asked for "a panel of physicists on" the owner decisions below. **Jon decides.** The panel advises only. The standing rules:
- Axiom changes are named as prices and are never adopted by agents.
- The standard is "only observed physical outcomes need to be matched".
- Owner readings are thoughts, not rules.

## Where to read

All paths are read-only.

**This exercise.** No local checkout exists. Read files with:

`git -C /Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790 show origin/claude/chirality-grid-exercise-20261014:.claude/science/exercises/chirality-grid-20261014/<file>`

Read SUMMARY.md first, then ROUTES.md (all tables, kill verdicts, referee records), WALL.md, ASSUMPTIONS.md and OUTSIDE_VIEW.md. PR #9562.

**Axioms.** `/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790/docs/MINIMAL_AXIOMS_2026-06-29.md`. Read IN FULL.

**Deferred decision #4 (M₄(C) / site-algebra size).** `git show origin/main:docs/repo/DEFERRED_DECISIONS.md`, lines 121–146. Its wake condition 1 includes "the chirality/generation program resumes, or a C222-class site-algebra extension becomes load-bearing".

**Gravity campaign (C5) and its follow-ups.** `/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790/.claude/science/exercises/gravity-current-state-20261009/`:
- `SUMMARY.md` §26–27;
- `TESTS.md`: the R19-28 and R19-33 set-B results and verdicts, and the "C5 follow-up" section (F1–F6, NF-1, E1, TW-1/2/3);
- `agents/panel_F/SYNTHESIS.md`.

## The decisions

**D1. Matter per site.** Every surviving chirality route needs more than one qubit's worth of fermion modes per lattice site:
- 16 modes per site for the native corner package (X2), plus fermion number conserved only mod 4;
- about 10³ for the inflow slab (F4/X1);
- an infinite real-time fibre for the overlap/set-B route (X3).

The Qubit axiom gives one M₂(C) per site (AX:47). The options:
- (a) keep one qubit per site, and read a physical "site" as a coarse block of many qubits (supplied coarse-graining);
- (b) enlarge the site domain (wakes #4, though not for the γ5 motivation, which Lemma R makes irrelevant);
- (c) refuse both, and accept that chirality is not realized on this lattice.

**D2. Range.** Lemma R (codex-confirmed) says exact Ginsparg–Wilson chirality needs a kernel outside the rational, finitely-generated class, i.e. not a finite nearest-neighbour rule with finitely many auxiliaries. Admissibility says "one fixed nearest-neighbor rule" (AX:57). Should a non-finitely-generated quasi-local kernel be acceptable as law content? Alternatives:
- interactions (symmetric mass generation), which keep finite range;
- finite-n domain-wall fermions with heavy bulk states.

**D3. Time.**
- **Set C:** continuous time on Z³.
- **Set B:** Euclidean hypercubic Z⁴ with a_t = a_s, plus Osterwalder–Schrader reconstruction.

Set B had the best gravity bill (R19-28, refereed) and the only chirality route with a clean free real-time spectrum (X3). But K2/K2b/K2c (codex-confirmed for the 2D U(1) proxy, including tori) show that **gauged reflection positivity fails for the overlap measure**. Set B's real-time branch therefore needs a price:
- Π-W for matter; or
- 5D fermions without Pauli–Villars fields, kept as heavy physical states.

In set C, the continuous-time chirality routes reduce to symmetric mass generation (F2-T; the codex referee says other escapes are not excluded).

NT-1 (chiral-measure RP), NT-2 (3D plaquette-bound RP) and NT-3 (route-2 exact diagonalisation) are running now. Their results may arrive while you work; scratch folders are under `.../scratchpad/chirality_ex/next/NT*/REPORT.md` once written.

**D4. Compute and collaborators.** The decisive tests for routes 2 and 3 are weeks of sign-free QMC (2+1D):
- X2-MB, for the corner package;
- F4's far-wall DQMC.

The 4D tests need HMC. The options:
- (a) fund the compute;
- (b) seek collaborators (Catterall, Hasenfratz, Golterman–Shamir, Fukaya/Onogi, Kikukawa, Thorngren/Preskill/Fidkowski);
- (c) defer, and treat chirality as the field's open problem, recording the prices.

## What each panelist must deliver

Work in your lens. Read SUMMARY.md, ROUTES.md and the axioms fully, plus whatever else you need; cite path:line. Your folder is `.../scratchpad/chirality_ex/panel_D/<lens>/`. Tiny scripts only, under 200 MB. Do not edit any repository.

1. **Per decision D1–D4:** your recommendation, with plain-words reasons.
2. **How the decisions interact.** For example, does D3 = set B force D2? Does D1 = (a) make D2 moot?
3. **The strongest argument from your tradition, and the steelman AGAINST your recommendations.**
4. **What evidence would change your mind**, including how NT-1/2/3 outcomes would move you.
5. **One concrete next action** (a test, a collaborator ask, or a decision) that best serves the program's goal of matching observed physics.

Plain words first, then technical. Labels: proved / checked / suggested / reading / comparator. Return within ~70 minutes. Your final text is your statement; also save it as `statement.md` in your folder. Be direct; no flattery.
