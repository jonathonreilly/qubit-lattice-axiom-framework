# Charter — Dynamics Lane, Native From Axioms Only

**Date:** 2026-05-26
**Branch:** `research/dynamics-lane-native-axioms-only-20260526`
**Status:** **research lane / side project.** Not a source PR. Not for landing on
`main` as a lane wrapper. Individual clean import-free science pieces may spawn
small PRs along the way per the reviewer's "small PRs only" rule; the lane itself
lands later (if ever) once the chain tells a story.

## Mandate (user, 2026-05-26)

> "Build the FULL dynamics program natively off the axioms ONLY and see where we
> get after a 12 hour physics-loop campaign."

## Strict constraints

The lane uses **only**:

1. **A1** — per-site `M₂(ℂ) = Cl(3,0)`; the "i" is the Cl(3) pseudoscalar.
2. **A2** — `Z³` locality.
3. **Retained inventory** — every claim in retained `Status:` notes on `origin/main`
   that does not itself require imports. Each retained citation in this lane must
   point to an actual `origin/main` retained note; branch-local-only claims are
   not citable as retained.

The lane **does not use, cite, or import**:

- D1-D3 (dynamical flavon, IR fixed point, phase-locking) — these were the M-work's
  rejected imports.
- Eichhorn-Held asymptotic-safety literature (arXiv:1707.01107, 1803.04027).
- Wetterich-equation / functional-RG machinery.
- Mode-locking / Arnold-tongue commensurability.
- "Dynamics lane" as a registered lane category (not in `LANE_REGISTRY.yaml`).
- "Positive relocation" theorem-type label.
- "Kinematic vs dynamical residual" reframe vocabulary.
- `KH` (kinematic-reformulation hypothesis from the closed scoping PR #1942).
- Milestone labels `M0-M4` from the prior session's research plan.
- The Wilson plaquette action as derivation input (it is itself an admitted import
  per the `Bridge gap fragmentation 2026-05-07` memory).

**Standard mathematics** (Lindemann-Weierstrass, group representation theory,
character algebra, complex analysis) is not an import — it is the math used to
manipulate retained content.

## What the lane is for

Given the strict constraint, the lane explores how far native-only machinery can
go toward addressing the dynamics-lane questions:

- Can the lepton mass observable be reconstructed natively from A1+A2 + retained
  inventory, with no admitted imports?
- Can the value of δ (the C₃-azimuthal phase appearing in the Brannen-Koide
  formula) be derived natively, OR is the gap precisely a structural import
  (e.g. requires the Wilson action), AND if so, can that import be derived
  natively elsewhere?
- Does the retained framework's NATIVE dynamics — lattice + decoherence
  (`mirror_symmetry_breakthrough`, `axiom_chain_closure` memories; see retained
  notes), Brannen CH closure (`brannen_ch_three_gap_closure`), corrected
  propagator gravity — say anything about δ that the FRG attempt didn't?

These are research questions, not theorem candidates yet.

## Deliverable types

The lane produces (in increasing order of formality):

- **Mapping notes** — dependency maps tagging existing chain steps native/import.
- **Native derivations** — clean algebraic / combinatorial / kinematic derivations
  using only retained content. Each is a candidate small-PR.
- **Identified gaps** — places where the chain hits a non-derivable import; each
  is a candidate research question for a future native attack.
- **Synthesis notes** — once gaps are characterized and native steps chain into a
  coherent story, a synthesis note ties them together. The lane wrapper PR (if
  ever) summarizes the synthesis.

## Process rules

1. **Each native derivation explicitly states `Imports: NONE` and lists the
   retained sources it cites.** Any imported content invalidates that piece's
   candidacy for a small-PR.
2. **Vocabulary stays within `docs/repo/controlled_vocabulary.yaml`** — no new
   reframe terminology.
3. **Standard math may be used freely** (group theory, character algebra,
   transcendence results); cite the theorem name only.
4. **Each clean import-free deliverable runs vocab_lint + a verifier runner**
   before commit.
5. **Small PRs are single-claim** (one algebraic identity OR one mapping note OR
   one gap-identification, not bundled).
6. **PR bodies quote the user's 2026-05-26 mandate** plus list "Imports: NONE"
   explicitly.
7. **The lane wrapper does NOT open as a PR** during this campaign; it
   accumulates on the research branch.

## Honesty contract

- No fitted values, no PDG as proof input (only as falsifier comparator).
- No bare `retained` / `promoted` in branch-local source-note `Status:` lines.
- N1-N8 No-Go Discipline applies if any negative claim is made.
- Native derivations that turn out to require admitted imports are demoted to
  "gap identified" status, not bare-retained.

## Resume

```
/physics-loop --mode resume --loop dynamics-lane-native-axioms-only-20260526
```

State surface: `.claude/science/research-lanes/dynamics-lane-native-axioms-only-20260526/STATE.yaml`
