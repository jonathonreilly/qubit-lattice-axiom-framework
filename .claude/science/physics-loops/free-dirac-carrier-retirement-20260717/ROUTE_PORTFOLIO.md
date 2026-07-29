# Route Portfolio

Scores are `0..3`; risk is negative. Execution is sequential because the user
forbids additional workers.

| Route | Orthogonal frame | Movement | Novelty | Authority closure | Review | Risk | Initial disposition |
|---|---|---:|---:|---:|---:|---:|---|
| R1 | finite-spacing complex pole and residue | 3 | 3 | 3 | 3 | -1 | selected: derive `E_a` and the `1/(2E)` measure from `D_red`, not from continuum convention |
| R2 | Hamiltonian spectral-projector graph limit | 3 | 3 | 3 | 2 | -2 | selected: derive positive/negative Dirac fibers and compact-momentum convergence |
| R3 | qubit/JW finite-mode CAR functor | 3 | 2 | 1 | 2 | -3 | hard-premise test: composition may be absent from the actual surface |
| R4 | Euclidean reflection-positive transfer route | 3 | 2 | 1 | 1 | -3 | bounded by missing retained OS/continuum authority; no reconstruction claim |
| R5 | Poincare action from the limiting pole shell | 2 | 2 | 2 | 2 | -2 | only usable if action/measure are derived from R1-R2 rather than assumed |
| R6 | textbook continuum authority wiring | 1 | 0 | 0 | 0 | -1 | rejected by V2-V4 and the user objective |
| R7 | Pattern-A algebra rescope of P1-P8 | 0 | 0 | 0 | 0 | -1 | rejected as corollary/review churn |

## Deep-block discriminator

The route passes the dramatic-step gate only if it produces at least one of:

- an exact finite-`a` pole/residue formula whose continuum limit supplies the
  previously imported mass-shell carrier and measure;
- a machine-checked deformation control showing how the displayed pole shell
  changes when its temporal coefficient is varied;
- a precise CAR-composition theorem on authorities already retained; or
- an honest hard-premise isolation showing exactly why the actual Qubit/Lattice
  surface cannot instantiate the CAR relabelling.

Writing down standard boosts or the standard Dirac-sea relabelling without
those steps is not a useful cycle.

## Cycle 2 prior-art sweep and route selection

Searched landed commit `b377240587dc9cb0640cb4424e4ea25261687e7a` with
`rg` over packet/clipping terms, inspected `authority_note_limit` and
`clip_packet_text` in `scripts/codex_audit_runner.py`, and reviewed commit
`47cc52f33f` plus
`docs/audit/scripts/tests/test_teleportation_taste_packet_repair.py`. The
matched prior result is an exactly scoped per-edge authority-size override; it
is a tooling precedent, not prior proof of this target's formulas. The target's
current ledger row confirms that its sole dependency is the 20,118-character
free-staggered authority and quotes the unclipped Sections 2–5 as the repair.

| Route | Mechanism | Trace | Risk | Cycle-2 disposition |
|---|---|---:|---:|---|
| R8 | exactly scoped `(target, authority) -> 22,000` transport override plus real-prompt regression | 3 | -1 | selected |
| R9 | raise `AUTHORITY_PER_NOTE_MAX` globally | 1 | -3 | rejected: widens every restricted packet without need |
| R10 | copy Sections 2–5 into the target source note | 1 | -3 | rejected: duplicates authority custody and obscures the dependency edge |
| R11 | rewrite or extend the existing pole/residue runner | 0 | -2 | rejected: the audit identified clipping, not missing formula code |
| R12 | edit audit ledger/status outputs | 0 | -3 | forbidden: independent audit owns those surfaces |
