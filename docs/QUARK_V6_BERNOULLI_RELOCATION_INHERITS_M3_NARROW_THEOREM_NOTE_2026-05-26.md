# Quark `V(6) = 5/36` Inherits the M3 Bernoulli Relocation: One Combinatorial Closure for Both Generation Sectors

**Date:** 2026-05-26
**Claim type:** bounded_theorem (cross-sector inheritance theorem; audit-conditional
on upstream M3 and CKM rows)
**Status authority:** independent audit lane only. This is the quark-sector sister
of the lepton-sector M3 relocation. **Audit required before any effective status.**
**Primary runner:** [`scripts/frontier_quark_v6_bernoulli_relocation_inherits_m3_narrow_discriminator.py`](../scripts/frontier_quark_v6_bernoulli_relocation_inherits_m3_narrow_discriminator.py)
**Authority role:** the second deliverable of the dynamics-lane completion campaign.
The M3 lepton result relocated the value `δ_lepton = 2/9` from a dynamical fixed point
to the retained combinatorial variance `V(3) = (N-1)/N²` at `N = N_gen = 3`. This
note extends the same relocation to the quark sector: `V(6) = 5/36` at `N = N_quark = 6 =
N_pair × N_color` is the retained Bernoulli identity equal to the retained CKM `η²`. The
result closes both sectors' value-question on a single combinatorial substrate; the
**π-bridge residual is inherited unchanged** — one kinematic license question covers
both sectors.

## Theorem (narrow)

**Inputs (forced or retained, listed with class):**

- A1, A2 — minimal axioms (retained).
- Retained Bernoulli family `M(N) = (N-1)/N`, `V(N) = (N-1)/N²`, `V(N) = M(N)/N`
  (retained per
  [`CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`](CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md)).
- Retained counts `N_pair = 2`, `N_color = 3`, `N_quark = N_pair × N_color = 6`
  (CKM magnitudes structural counts theorem; `proposed_retained` upstream, used as
  bounded support).
- The M3 lepton relocation theorem (currently `audited_pending` in
  [PR #1940](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1940);
  used as the sector-1 instance of the inheritance pattern).

**Statement.** The quark-sector generation-variance value at `N = N_quark = 6` is
the retained Bernoulli variance

```
V(6) = (6 - 1) / 6² = 5/36 = M(6) / 6 = (5/6) / 6 .
```

Identifying `V(6)` with the retained CKM `η²` (per the support note's K6 and the
seed-note footnote), the quark value-question is **closed combinatorially**:
`V(6) = 5/36 = η²_retained`. The closure is structurally identical to the lepton case
`V(3) = 2/9 = retained Bernoulli at N=3`. The kinematic π-bridge residual (radian
license for a rational variance) is inherited unchanged: **one residual per sector,
same residual in both**.

## Forced vs added

**Forced (load-bearing):**

- Bernoulli family `V(N) = (N-1)/N²` and `V(N) = M(N)/N` (retained).
- Counts `N_pair = 2`, `N_color = 3`, `N_quark = 6` (retained / proposed_retained).
- The inheritance *pattern* from M3: "value is counting, not dynamics, residual is
  kinematic" applies in any sector where the retained Bernoulli family carries the
  variance — this is the **structural** content of the cross-sector inheritance.

**Added (cycle-specific):**

- **H1 — Cross-sector inheritance hypothesis.** If M3 closes the lepton-sector value
  via the retained Bernoulli relocation, the quark-sector value-question (`V(6) =
  η²`) closes by the same mechanism with the same residual class (π-bridge,
  kinematic, shared across sectors). **STATUS: bounded_theorem candidate; load-bearing
  dependency on M3 (PR #1940, audit pending).**

**Conditional / dependency bookkeeping:**

- M3 result is currently `audited_pending`. If M3 fails audit, the inheritance
  argument's positive instance is lost, but the *algebraic identity*
  `V(6) = 5/36 = (N-1)/N² at N=6` is independent and would survive as a bare
  combinatorial fact.
- CKM upstream rows are `proposed_retained` / `unaudited`. The η² ↔ V(6)
  identification depends on those.

## Imports (comparator only)

- PDG Wolfenstein `η` ≈ 0.354 ± 0.012 → η² ≈ 0.125 ± 0.009. The retained framework
  prediction is `V(6) = 5/36 ≈ 0.1389`. The PDG-vs-prediction comparison is in the
  runner as Section 7 (comparator), not as a derivation input. **The framework's
  η² is the retained K6 reading, not the PDG measurement.**
- Lindemann-Weierstrass (transcendence of π over Q) — standard math; only used to
  carry the M3 conclusion that no Q-rational combination derives a bare rational
  radian.

## What is and isn't claimed

- **Exact (algebra):** `V(6) = (6-1)/6² = 5/36 = M(6)/6 = (5/6)/6`; same Bernoulli
  identity as `V(3) = 2/9` but at `N = 6`.
- **Exact (count identity):** `N_quark = N_pair × N_color = 2 × 3 = 6`; this is the
  retained quark-sector count (CKM magnitudes structural counts theorem).
- **Bounded theorem (cross-sector inheritance):** the M3 relocation pattern (value
  is the retained combinatorial variance, dynamics neither supplies nor needs the
  value, residual is the kinematic π-bridge) extends to the quark sector via the
  same Bernoulli family at `N = N_quark = 6`. **Status conditional on M3 being
  audit-ratified.**
- **NOT claimed:** that the π-bridge is closed for quarks. The kinematic license
  question is the same as for leptons and remains open (see the scoping note for
  the kinematic-attack roadmap).
- **NOT claimed:** any new axiom, any new fitting, any reliance on PDG as proof
  input.
- **NOT claimed:** any audit-ratified retained status. Branch-local source note;
  audit determines effective status.

## N1-N8 No-Go Discipline (positive theorem; the gate is asymmetric but the
hostile-review discipline still applies)

Since the **positive** inheritance theorem could be attacked, a hostile-review
check applies. The audit-lane perspective:

- **HR1 — Alternative quark-sector value.** Could the quark generation-variance
  equal something other than `V(6) = 5/36`? The Bernoulli family is retained; the
  count `N_quark = 6` is retained; the *value* of `V(N=6)` is forced by the family.
  No alternative survives without modifying retained content.
- **HR2 — Inheritance pattern doesn't transfer.** Could the M3 relocation pattern
  fail to apply to quarks? The pattern is: "the C-equivariant generation-variance is
  the retained Bernoulli (counting), not a dynamical fixed-point output." For the
  pattern to fail in the quark sector, the quark generation-variance would need to
  have a *dynamical* origin distinct from leptons — but the framework treats both
  sectors with the same generation-clock + CP-evenness structure (the C₃ generation
  triplet retains across sectors). So the pattern transfer is the same structural
  consequence; only the count `N` changes.
- **HR3 — π-bridge does NOT inherit.** Could the kinematic π-bridge residual be
  *different* for quarks vs leptons? The bridge gap is `radian-vs-dimensionless`,
  which is a kinematic license question independent of which combinatorial value
  enters the cosine. So the bridge gap is *structurally the same* across sectors
  even if the rational that enters differs.
- **HR4 — V(6) ≠ η² in the framework.** Could the retained CKM `η²` differ from
  `V(6) = 5/36` in the framework? Per the support note's K6 identity at `N_color = 3`
  and the cross-sector reading, `(1/N_color)(1 - 1/N_color) = (N_color - 1)/N_color² =
  2/9`. The quark-flavor analogue using `N_quark = 6` gives `(N_quark - 1)/N_quark²
  = 5/36`. This is identified with retained CKM `η²` in the seed note and prior
  support. The identification is conditional on the upstream rows being retained.
- **HR5 — Hidden admission.** Reviewed: no "by construction", no fitted selector,
  no "standard QFT" smuggle, no admitted convention beyond what the M3 ledger and
  the CKM support note already cite. The result is the algebraic consequence of
  named retained content.

Hostile review passes. The inheritance is a clean structural consequence; the
dependency on M3 and CKM upstreams is the only audit-conditional class.

## Verify

```
python3 scripts/frontier_quark_v6_bernoulli_relocation_inherits_m3_narrow_discriminator.py
```

Expected: `PASS=N FAIL=0` (around 18-22 checks).

The runner verifies:

1. Bernoulli identity `V(N) = (N-1)/N²` exactly at `N = 6`: `5/36`.
2. Bernoulli identity `V(N) = M(N)/N` cross-check: `V(6) = M(6)/6 = (5/6)/6 = 5/36`.
3. Count identity `N_quark = N_pair × N_color = 2 × 3 = 6` (retained CKM structural
   counts).
4. Cross-sector consistency: lepton at `N = 3` gives `V(3) = 2/9`; quark at `N = 6`
   gives `V(6) = 5/36`. Both follow from the same Bernoulli family.
5. M3 inheritance pattern: V(N) is combinatorial (counting), not dynamical, in both
   sectors; the residual π-bridge is kinematic and shared.
6. PDG comparator: `η²` from PDG Wolfenstein vs the framework's retained `η² =
   V(6) = 5/36`; this is a comparator, not a derivation input. The discrepancy
   between framework `0.1389` and PDG central `~0.125` is recorded but not load-bearing
   on the theorem.
7. Explicit non-claims (no closure of π-bridge, no new axiom, no PDG as proof).

## Cross-references (plain-text, non-load-bearing)

- [`DYNAMICS_LANE_MILESTONE3_PHASE_LOCK_NOGO_PI_BRIDGE_NOTE_2026-05-26.md`](DYNAMICS_LANE_MILESTONE3_PHASE_LOCK_NOGO_PI_BRIDGE_NOTE_2026-05-26.md)
  — the M3 lepton result this inherits from.
- [`DYNAMICS_LANE_SEED_DELTA_AS_GENERATION_PHASE_LOCKING_NOTE_2026-05-26.md`](DYNAMICS_LANE_SEED_DELTA_AS_GENERATION_PHASE_LOCKING_NOTE_2026-05-26.md)
  — names `V(6) = 5/36 = retained CKM η²` as the quark analogue.
- [`CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md`](CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md)
  — the four CKM K1/K2/K5/K6 identities at `N = N_color = 3`, with `(N_color -
  1)/N_color² = 2/9` (color-projected Bernoulli); structural template for the
  N_quark = 6 reading.
- [`PI_BRIDGE_KINEMATIC_REFRAME_SCOPING_NOTE_2026-05-26.md`](PI_BRIDGE_KINEMATIC_REFRAME_SCOPING_NOTE_2026-05-26.md)
  — the shared residual; the kinematic-attack roadmap covers both sectors with one
  K1-K4 program.
- `.claude/science/physics-loops/dynamics-lane-completion-20260526/STATE.yaml` —
  campaign coordination state.

## Command

```bash
python3 scripts/frontier_quark_v6_bernoulli_relocation_inherits_m3_narrow_discriminator.py
```
