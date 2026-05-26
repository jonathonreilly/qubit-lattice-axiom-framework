# Lane Proposal — Dynamics-Lane Investigation Import Inventory

**Date:** 2026-05-26
**Status:** **proposal / approval request, NOT a theorem note, NOT for audit.**
**Branch:** `research/dynamics-lane-import-inventory-2026-05-26` (off `origin/main`; no PR).
**Audience:** repo owner (user) for explicit approve/reject decisions per import.
**Trigger:** review-loop rejection of PRs #1940 (M2+M3), #1942 (π-bridge scoping), #1946
(block01-quark-vq6) on 2026-05-26 with consistent feedback: "needs explicit user science
approval; no content from this PR was landed." Reviewer's recommended remediation
process: produce a scoped import inventory before any further PR.

## 1. Purpose

This document is the **import inventory + scoped approval request** for the dynamics-lane
investigation inherited from the 2026-05-26 remote-session handoff. It separates content
the way the reviewer specified:

1. **Existing retained framework content** — no approval needed; listed for reference.
2. **Bridge claims** — identifications between retained content and new structures
   (e.g. `δ ↔ V(3)`); these are STRUCTURAL hypotheses needing approval.
3. **External dynamics machinery** — FRG, asymptotic safety, Eichhorn-Held, Wetterich,
   mode-locking; literature comparators needing approval.
4. **Dynamical hypotheses** added as background-for-testing (D1, D2, D3); each needs
   approval even if the hypothesis is ultimately disproven by the test.
5. **New framing language** — "dynamics lane", "kinematic vs dynamical residual",
   milestone labels (M0-M4); each needs approval if used in source notes.

This document **does not propose source PRs**. After your approve/reject decisions, the
reviewer's "small PRs only" rule applies (pure no-go OR pure algebra OR pure bridge,
one per PR, no bundling).

## 2. Category 1 — Existing retained framework content (no approval needed)

These items are listed for reference only. They are already retained in the framework.

| Item | Provenance | Role in dynamics-lane work |
|---|---|---|
| A1 | `MINIMAL_AXIOMS_2026-05-03.md` | per-site `M₂(ℂ) = Cl(3,0)`; the "i" is the pseudoscalar |
| A2 | `MINIMAL_AXIOMS_2026-05-03.md` | `Z³` locality |
| C₃ generation triplet | retained | the circulant structure for leptons |
| Bernoulli family `V(N) = (N-1)/N²` | retained | the identity at the heart of the relocation |
| `V(N) = M(N)/N` identity | retained | same family, alternative form |
| `V(3) = 2/9` algebraic identity | retained | the lepton instance |
| `V(6) = 5/36` algebraic identity | retained | the quark instance |
| Koide cone `Q = 2/3` (lepton) | retained | radial parameter |
| `N_pair = 2`, `N_color = 3`, `N_quark = 6` | retained (CKM structural counts) | quark-sector counts |
| Brannen circulant eigenvalue formula | retained (`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`) | shape of the lepton mass observable |
| Lindemann-Weierstrass theorem | standard math (not a framework import) | used to argue π is transcendental over Q |

Decision needed on Category 1: **none**.

## 3. Category 2 — Bridge / identification claims (each requires explicit approval)

A "bridge" here is a proposed *identification* between two retained quantities, or
between a retained quantity and a new structural object. The bridge itself is a
structural hypothesis even if both endpoints are individually retained.

### B1 — `3δ = Q` (azimuthal radian ↔ radial Koide ratio)

- **What:** identify the C₃-azimuthal phase `3δ` (a literal radian) with the retained
  radial Koide cone `Q = 2/3` (a dimensionless ratio).
- **Where it lives:** `DYNAMICS_LANE_SEED_DELTA_AS_GENERATION_PHASE_LOCKING_NOTE_2026-05-26.md`
  (currently on the dynamics branch, not in main).
- **Role:** the bridge that makes `δ = Q/N_gen = 2/9` an inheritance from retained
  content rather than a free parameter.
- **Risk:** identifies a radian with a pure rational; the radian-bridge primitive `P`
  is itself an open admission per six prior no-go routes.
- **Falsifier:** Lindemann-Weierstrass already shows `2/3` (dimensionless) ≠ `2/3` (rad)
  in `cos`; the identification is a *structural identification*, not an equality of
  numerical values.
- **Decision needed:** **approve** as a bridge hypothesis with a narrow non-derivation
  role; **reject**; or **defer**.

### B2 — Bernoulli relocation: `the C-equivariant generation-variance VALUE is the retained Bernoulli V(N)`

- **What:** identify the value that appears as a generation-variance parameter in the
  Brannen mass formula (`δ` for leptons, `η²` for quarks) with the retained Bernoulli
  variance `V(N)` at the appropriate count.
- **Where it lives:** the cross-sector reading in
  `CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md` (retained as
  bounded support; the inheritance reading to leptons is what's added by M3).
- **Role:** closes the value-question combinatorially (the value is counting, not
  dynamical); shifts the open residual to the kinematic π-bridge.
- **Risk:** the identification with `δ` requires the radian-bridge primitive (open).
  The identification with `η²` requires the Wolfenstein-derived CKM identity (CKM
  upstreams `proposed_retained`).
- **Falsifier:** PDG `η²` ≈ 0.125 vs framework `V(6) = 5/36` ≈ 0.139 (~11%
  discrepancy); needs explanation if claim is taken seriously.
- **Decision needed:** **approve**, **reject**, or **defer**.

### B3 — `KH` kinematic-reformulation hypothesis (π-bridge attack)

- **What:** hypothesize that the Brannen-Koide circulant `cos(δ + 2πk/3)` is a
  *re-expression* of an underlying observable that takes `Q` (dimensionless) as input
  without passing through any literal radian.
- **Where it lives:** `PI_BRIDGE_KINEMATIC_REFRAME_SCOPING_NOTE_2026-05-26.md` (closed
  PR #1942).
- **Role:** the kinematic attack route on the π-bridge primitive `P`; if `KH` holds,
  `P` dissolves into a coordinate label.
- **Risk:** structural hypothesis with no derivation; the four candidate substrates
  (K1-K4) each face L-W blockers in initial analysis.
- **Falsifier:** if K1-K4 each fail to encode the literal `δ=2/9 rad` without
  smuggling, `KH` is bounded-no-go.
- **Decision needed:** **approve**, **reject**, or **defer**.

## 4. Category 3 — External dynamics machinery (literature comparators; each requires explicit approval)

These are CITED LITERATURE used as comparator/context, not as derivation inputs.
The reviewer's policy: even comparator-only citations count as imports and need
approval.

### L1 — Eichhorn-Held asymptotic-safety gravitational fixed point

- **Citation:** arXiv:1707.01107, arXiv:1803.04027.
- **Role:** precedent that fixed points fix VALUES (Yukawa coupling). Comparator only;
  not used as a derivation input.
- **Risk:** importing the asymptotic-safety framing language into the repo even as
  context.
- **Decision needed:** **approve**, **reject**, or **defer**.

### L2 — Wetterich-equation / functional-RG machinery

- **Citation:** Wetterich 1993 (standard).
- **Role:** the β-function FORM the dynamics-lane attempts use; coefficients are
  toy/illustrative unless derived from A1+A2. Comparator only.
- **Risk:** importing FRG technology even as background.
- **Decision needed:** **approve**, **reject**, or **defer**.

### L3 — Mode-locking / Arnold-tongue commensurability

- **Citation:** Arnold (standard dynamical systems literature).
- **Role:** candidate mechanism for rational phase-locking. Comparator only.
- **Risk:** importing nonlinear-dynamics framing.
- **Decision needed:** **approve**, **reject**, or **defer**.

## 5. Category 4 — Dynamical hypotheses (background-for-testing; each requires explicit approval)

The M3 work used D1-D3 as the "lane's new inputs" — hypotheses posited as background
for the FRG-fixed-point test of `δ=2/9`. The test concluded D3 fails. But D1 and D2
were carried as background regardless.

### D1 — `z` is a dynamical flavon (kinetic term + RG flow)

- **What:** posit that the C₃ order parameter `z = r·e^{iδ}` is a dynamical field
  with a kinetic term and RG flow, not a frozen background.
- **Role:** required for any RG-based attempt to constrain `δ`.
- **Risk:** imports "dynamical field with RG flow" as a concept; A1+A2 alone don't
  specify dynamics.
- **Decision needed:** **approve as bounded exploratory import for a dynamics-lane
  investigation only**, **reject**, or **defer**.

### D2 — `A, B` couplings fixed by an IR fixed point

- **What:** posit that the coefficients in the C₃-flavon potential `V(δ) = A cos(3δ)
  + B cos(6δ)` are fixed by an IR fixed point of the RG flow.
- **Role:** the asymptotic-safety mechanism applied to flavor.
- **Risk:** imports the "fixed point fixes values" mechanism as background.
- **Decision needed:** **approve as bounded exploratory import**, **reject**, or **defer**.

### D3 — fixed point LOCKS `arg(z) → V(N)` (phase = variance)

- **What:** posit that the IR fixed point under D2 *locks* the azimuthal phase to the
  radial variance, giving `δ = V(N)/something`.
- **Role:** the decisive hypothesis the M3 test was designed to falsify.
- **Result:** **disproved by M3** (no algebraic fixed-point / mode-locking /
  group-theoretic dynamics produces `δ=2/9` as a radian phase, bounded by the
  algebraic-fixed-point assumption).
- **Risk:** D3 was disproved — but the act of POSITING it as background is itself
  the import that needed approval.
- **Decision needed:** **approve (retroactively) as bounded exploratory import that
  was tested and refuted**, **reject** (and treat the M3 negative result as not
  landable), or **defer**.

## 6. Category 5 — New framing language (each requires explicit approval)

### F1 — "dynamics lane" as a lane category

- **What:** treat "dynamics lane" as a research lane on par with other registered
  lanes in `LANE_REGISTRY.yaml`.
- **Risk:** governance-level addition; not in the current registry.
- **Decision needed:** if approved, requires `LANE_REGISTRY.yaml` update first (per
  reviewer's recommendation).

### F2 — Milestone labels M0-M4

- **What:** the prior session's research-plan labels (`M2 = dynamical-layer setup`,
  `M3 = decisive FRG test`, `M4 = mass-scale closure`).
- **Risk:** local milestone labels that read as framework-level if not flagged.
- **Decision needed:** **keep as branch-local research labels only** (don't appear in
  source notes intended for audit), **drop entirely**, or **defer**.

### F3 — "Kinematic vs dynamical residual" reframe terminology

- **What:** the language used to characterize the post-M3 residual ("the missing
  principle is not dynamical, it's kinematic — the radian-bridge license").
- **Risk:** new framework-level vocabulary.
- **Decision needed:** **approve as bounded research vocabulary** (with controlled
  vocabulary update first), **reject**, or **defer**.

### F4 — "Positive relocation" theorem-type label

- **What:** the language "the value relocates to the retained variance" used to
  describe the M3 result's positive component.
- **Risk:** new theorem-type label that conflicts with single-claim PR hygiene.
- **Decision needed:** **drop** (use only "bounded no-go" framing); **approve** (only
  in separate positive-theorem PRs with V1-V5 gate); or **defer**.

## 7. Decision matrix (for explicit user response)

Please respond with one of `APPROVE` / `REJECT` / `DEFER` per item. Approvals should
name the scope (e.g. "approve D1-D3 as bounded exploratory imports for a dynamics-lane
investigation, comparator/context role only, not as derivation inputs in retained
theorems").

| ID | Item | Decision |
|---|---|---|
| B1 | `3δ = Q` identification | _____ |
| B2 | Bernoulli relocation reading | _____ |
| B3 | `KH` kinematic-reformulation hypothesis | _____ |
| L1 | Eichhorn-Held citation (comparator only) | _____ |
| L2 | Wetterich/FRG machinery citation (comparator only) | _____ |
| L3 | Mode-locking/Arnold-tongue citation (comparator only) | _____ |
| D1 | Dynamical flavon hypothesis (bounded, for testing) | _____ |
| D2 | IR fixed point fixes couplings (bounded, for testing) | _____ |
| D3 | Fixed point locks `arg(z) → V(N)` (bounded, disproved) | _____ |
| F1 | "Dynamics lane" as registered lane category | _____ |
| F2 | Milestone labels M0-M4 | _____ |
| F3 | "Kinematic vs dynamical residual" reframe vocabulary | _____ |
| F4 | "Positive relocation" theorem-type label | _____ |

## 8. What would proceed under various approval patterns

The reviewer's "small PRs only" rule means each approved-item enables a specific kind
of follow-up PR. Examples:

- **If only B2 approved (Bernoulli relocation reading) + nothing else**: a pure-algebra
  PR confirming `V(3) = 2/9` and `V(6) = 5/36` as instances of the retained Bernoulli
  family, with explicit "no dynamics-lane framing, no bridge claim to `δ`" disclaimers.
  This is essentially what the reviewer noted is already in CKM-Bernoulli surfaces, so
  this PR may be redundant.
- **If D1-D3 approved (bounded exploratory) + L1-L3 (comparator)**: a pure no-go PR
  attacking ONE route (e.g. R1 polynomial-truncation FRG) against `δ=2/9`, with
  Lindemann-Weierstrass as the standard math, and explicit "imports D1-D3 + L1-L3
  approved 2026-05-26 by repo owner as bounded exploratory" markers.
- **If only B1 approved (`3δ=Q` identification)**: a bridge-theorem PR for `3δ=Q`
  alone, no dynamics-lane framing, no D1-D3 imports, no FRG language. Just the
  algebraic identity `3·(2/9) = 2/3` and the structural identification as a hypothesis.
- **If F1 approved (dynamics lane as registered category)**: governance PR updating
  `LANE_REGISTRY.yaml` + `controlled_vocabulary.yaml` BEFORE any source notes use the
  terminology.
- **If everything rejected**: dynamics-lane work is permanently dropped; the existing
  closed PRs remain as historical record only.

## 9. Process commitments under any approval pattern

- **No source PR opens until** the user has responded to this proposal with explicit
  approve/reject decisions per item.
- **If governance items (F1, F3) are approved**, governance PRs (LANE_REGISTRY,
  controlled_vocabulary updates) open BEFORE any source-note PRs using the terminology.
- **Each downstream PR is single-claim** (one no-go OR one algebra OR one bridge); no
  bundling.
- **PR bodies explicitly cite approval text** from the user response, e.g. quoting
  "approve D1-D3 as bounded exploratory imports for a dynamics-lane investigation".
- **The bare algebraic identities** (`V(3)=2/9`, `V(6)=5/36`) are not load-bearing in
  any PR unless they constitute a genuinely new lemma — the reviewer noted these are
  already in CKM-Bernoulli surfaces, so a new PR for them would be redundant.

## 10. Cross-references (record only; non-load-bearing)

- **Closed PRs (rejected):**
  - [#1940 (M2+M3)](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1940)
  - [#1942 (π-bridge scoping)](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1942)
  - [#1946 (block01 V(6) inheritance)](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1946)
- **Branches still on remote (not deleted; not for PR):**
  - `claude/lattice-negative-numbers-exploration-FwRQE`
  - `science/dynamics-lane-m3-pi-bridge-nogo-2026-05-26`
  - `science/pi-bridge-kinematic-reframe-scoping-2026-05-26`
  - `physics-loop/dynamics-lane-completion-block01-quark-vq6-20260526`
- **Reviewer's recommended approach** (reproduced in this conversation):
  "Use a research/work-history branch or lane proposal packet, not theorem notes
  intended for audit. ... The next useful artifact is not another PR; it's a short
  lane proposal/import inventory that asks you to approve or reject specific
  hypotheses."

## 11. What this proposal is NOT

- Not a theorem note.
- Not intended for audit.
- Not a PR.
- Not a request for the user to defend any of the items — only to approve / reject /
  defer them per the proposal's scoped framing.
- Not load-bearing on any existing retained surface.
