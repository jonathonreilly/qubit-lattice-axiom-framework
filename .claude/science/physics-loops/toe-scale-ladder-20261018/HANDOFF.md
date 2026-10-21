# Handoff — toe-scale-ladder-20261018

Campaign: 24 h, 2026-10-18 18:36Z → 2026-10-19 18:36Z. Branch `claude/focused-mccarthy-q4vbgt`
(base main `584755767`). Delivery: milestone; no PR opened (platform rule: PRs only on
explicit user request) — ready body in `PR_BACKLOG.md`.

## State
- Results by rung: `RESULTS.md`. Review record: `REVIEW_HISTORY.md`. Frontier map and
  candidate list: `SCALE_LADDER_MAP.md`. Block packets: `blocks/<id>/{NOTE,REVIEW,WORKLOG}.md`.
- All blocks were reviewed in a separate agent context by the same model as the author
  (not an independent audit). Formal audit stays deferred. No axiom or primitive adopted.
- Two main-surface repairs on the branch (separate commits):
  `f46a89b7b` (two-qubit Dirac tick runner/note: arccos² series 8/45 → 4/45, isotropic k⁶
  coefficient) and `68a504d6d` (induced-G note: determinant half-factor addendum,
  G = 6π/(N_f Λ²)). No audit-ledger files touched; the mechanical ledger refresh is pending.

## Strongest results (see RESULTS.md for scope)
1. C5 + C5b: finite-range walks on Z³ have W3 = 0 and per-level chirality balance — free
   chiral fermions cannot arise from finite-range walks, even with the partner at π/a.
2. C4f + C9: under the axis soldering action an O-covariant one-qubit U(1) QCA with a moving
   bound pair exists (range ≤ 18); under the full action every such QCA is the identity
   (SU(2)-symmetric TI one-qubit QCAs are translations).
3. C3 + C3b: covariant formation with local/mixing clocks has no ordered or critical record
   phase; order needs infinite ancestries.
4. C6: twisted fermion codes (F1–F4) are BHM-stable Z2 phases with emergent fermions; no
   photon by small perturbation.
5. C7 + C8: 3+1D Dirac-walk continuum limit with explicit errors; exact lattice Sakharov
   coefficient (a/l_P = 0.43–0.69 √N_f across couplings) with stated caveats.
6. C2: light-cone equality is not implied by the registered premises.

## Open, highest-blast-radius residuals (next campaign)
- **Photon phase (R2→R3):** C1/C1b inconclusive; bottleneck is winding-sector mixing at
  β ≥ L. C1c equilibrated L=4,6: pre-declared tests conflict (no verdict); its L=8
  energy −443.85(15) indicates the repo's 8³ guided-projector value (−443.364) is too high —
  a repair candidate for that note after an owner/review decision. Next: equilibrated L ≥ 8
  (dual-height/worm formulation or much longer PT), and a declared rule for combining tests.
- **Chiral matter (R3):** K + L force interacting dynamics. Precise next question: can a
  strictly local interacting one-qubit (or emergent-fermion code) dynamics carry net
  chirality at low energy? Relate to anomaly / symmetric-mass-generation literature.
- **Moving excitations:** C4e/C4f pair glider has range ≤ 18; range 2 open (necessary
  k ≤ 3 conditions satisfiable). Single excitations cannot move with U(1) (C4b Lemma 2).
- **Owner decisions:** (a) adopt the reviewed candidate KI+_G (C2b) into the premise
  registry? It ties light cones, survives renormalization, and selects ±b_gold. (b) accept the two repairs above via a PR? (c) C1b's 42 MB raw data on the
  branch — keep or strip before a PR?

## Resume
Read `STATE.yaml`, then this file, then `RESULTS.md`. Lock: `scripts/automation_lock.py`
(owner physics-loop) — release at stop.

## Follow-up (2026-10-21)
- PR opened: jonathonreilly/qubit-lattice-axiom-framework#9831.
- C2b (KI+ candidate extension) and C10 (burn/turn on the Dirac walk) added, both reviewed.
- Cross-thread links with the burn/turn thread and recent main landings: `CROSS_THREAD_LINKS.md`
  (no conflicts; joint targets ranked there).
