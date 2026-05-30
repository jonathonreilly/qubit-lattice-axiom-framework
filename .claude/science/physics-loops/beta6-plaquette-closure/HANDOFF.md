# Handoff — β=6 Plaquette Closure Loop

## Where this loop stands (after cycle 1, 2026-05-30)

- **d₆ = 7/5668704 computed EXACTLY** and shipped as a bounded note +
  audit-companion runner (cycle-1 PR). Reproduces the retained anchor
  d₅ = 1/472392. Per-shell d₆ = 7/(12·18⁵); per-shell ratio d₆/d₅ = 7/12.
- **New exact finite-geometry fact:** zero order-β⁶ distinct connected supports
  are GF(3)-closable (of 5966 leaf-free size-6 supports over the radius-1
  patch); d₆ is the four cube shells' order-6 multiplicity contribution.
- **Engine (single self-contained artifact for resumption):**
  `scripts/frontier_beta6_connected_coefficient_2026_05_30.py` — exact SU(3)
  link integrals via invariant-tensor projector → moments → set-partition
  cumulants → support+multiplicity sum + GF(3) pre-filter, plus the GF(3)
  cycle-space certificate (5b) that settles which distinct supports can
  contribute without the cluster-growth enumeration. Validated end-to-end. To
  resume, extend `compute_dn` / `cube_shells_size5` in that file; no other
  module is needed.

## Resumable next action (CYCLE 2)

**Run the landed resummation harness #2255 to a tadpole verdict, and forward-test
the d-log-Padé route.**

1. Edit `scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py` drop-in:
   ```python
   EXACT_HIGHER = {6: Fraction(7, 5668704)}          # + 7: <exact d_7> once available
   ```
2. Rerun. With {d₅, d₆} the tadpole/geometric ansatz predicts
   d₇^pred = (d₆/d₅)·d₆ = (7/12)·(7/5668704) = 49/68024448 ≈ 7.20e-07.
   - If exact d₇ is supplied, the harness prints SUPPORT/FALSIFY (5% window) —
     the clean predictive verdict on the tadpole route.
   - The d-log-Padé PREDICTIVE verdict needs {d₅..d₈} (= β⁸). β⁸ is at/past the
     treewidth wall, so **only the d-log-Padé FORWARD <P>(6) sensitivity test is
     in-runway**; do not claim a d-log-Padé predictive verdict in-runway.
3. Ship a bounded note recording the tadpole predictive verdict + the forward
   <P>(6) band. Audit-shippable either outcome (SUPPORT or FALSIFY is a result).

## d₇ status (the stretch goal of cycle 1)

- d₇ contributions: (i) the four cube shells via order-7 multiplicity; (ii) any
  GF(3)-closable size-6 distinct support — **none** (established at order 6);
  (iii) any GF(3)-closable size-7 distinct support — **probed in cycle 1**
  (see `_dev_closable7.py` / the cycle-1 PR body for the result).
- **Named computational wall:** the cube-shell order-7 multiplicity cumulants
  reach single links with up to four fundamental factors, whose exact SU(3)
  invariant-projector contraction is a 3^(2k) sum (3^8 per such link); combined
  with the μ≈8 cluster growth and Bell(8)=4140 partition sums per 8-slot
  cumulant, this is the practical edge. If cycle 1 did not land an exact d₇,
  resume here: the remaining work is purely the cube-shell order-7 multiplicity
  cumulants (the distinct-support side is settled), so an optimized contraction
  (sparse einsum over the per-link invariant tensors, or pure-int Fraction
  arithmetic replacing sympy in the hot loop) should bring d₇ in reach without
  any new physics.

## CHECKPOINT (after cycle 2) — the treewidth-29 wall

A genuine resummation closing <P>(6) needs ~15–40 exact coefficients; the
exact-coefficient engine collides with the treewidth-29 infeasibility well
before that. **At the wall, STOP brute extension.** Closure then needs a
genuinely new dynamical input (Münster-style graphical organizer / rank-aware
contractor / proof of complex-pair analyticity of Δ on (0,6]) — each a separate
first-principles research item, not a brute extension. This is where the loop
hands back to `/first-principles` / `/frontier` work, NOT another coefficient
cycle.

## Discipline reminders for the next agent

- Verify `effective_status` in `docs/audit/data/audit_ledger.json` before citing
  any status from these notes or from memory.
- Framework PRs land science/fixes only; `git checkout -- docs/audit/` before
  committing if the audit pipeline was run.
- No new vocabulary / tags / meta-framings; mirror existing bounded-theorem
  note templates; no bare "retained"/"promoted"; cite 0.594 only as comparator.
