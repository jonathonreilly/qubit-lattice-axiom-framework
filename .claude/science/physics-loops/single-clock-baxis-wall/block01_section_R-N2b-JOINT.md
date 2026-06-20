# Block01 section — Route R-N2b-JOINT

**Clause:** N2b (B-AXIS.1b) — the ABSOLUTE physical clock unit `a_τ` (a number
carrying units of time), as distinct from the internal blocked-transfer
denominator `1/(2 a_τ)`, which N2a already FORCES.

**Date:** 2026-06-20
**Branch:** `physics-loop/single-clock-baxis-wall-block01-20260620`
**Runner:** `scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py`
**Cached log:** `logs/runner-cache/single_clock_n2b_joint_clock_unit_check_2026_06_20.txt`
**Runner result:** `TOTAL: PASS=17 FAIL=0`

---

## 1. The exact thing attempted

A genuine fresh derivation attempt: derive an ABSOLUTE clock unit `a_τ` (not the
`1/(2 a_τ)` denominator) by combining the framework's TWO retained rate gates
JOINTLY, where neither alone pins the unit:

- **GATE-S** — the spectrum-condition blocked-time normalization bridge
  (`AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`,
  live ledger 2026-06-05: `retained_bounded` upstream input). Supplies the
  DIMENSIONLESS two-step transfer object `T̂² = exp(-2 a_τ H)` and the
  reconstruction `H = -(1/(2 a_τ)) log(T̂²/M_T)`.

- **GATE-R** — the record clock/rate normalization and stable-dial gate
  (`RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06`, status `exact-support`).
  A supplied production generator `Q` stabilizes a dial (`Q π = 0`); the
  transition kernel `exp(t Q)` fixes only the DIMENSIONLESS product `t·Q`, i.e.
  `(r, t)` and `(r/c, c·t)` give the same kernel. Rate vs clock stay separate.

**Hypothesis to test (the would-be CRACK):** demanding that the SAME physical
clock underlie BOTH the transfer step (block time `2 a_τ`) AND the record-rate
generator might over-determine the joint system and pin `a_τ` absolutely.
**Expected (to be falsified by working it):** ratio-only — the joint system
still admits the exact rescaling `a_τ → c·a_τ` with `T̂²` invariant.

## 2. The A_min-only method (no new axiom / primitive)

On a finite carrier, build both gate objects from A_min surface only:

1. **GATE-S object.** Vacuum-normalized `H = diag(E_i − E_0) ≥ 0`; supplied
   two-step transfer `T̂² = exp(-2 a_τ H)`, positive Hermitian, spectrum in
   `(0, M_T]`. Reconstruction with `1/(2 a_τ)` returns `H` exactly (N2a forced,
   residual 0).
2. **GATE-R object.** Complete-graph reversible generator `Q` (column
   convention) with detailed balance `Q π = 0` for a supplied dial `π`.
3. **JOINT tie (strongest possible single-clock coupling).** Advance the record
   stream by exactly one transfer block per step: continuous-time record kernel
   over one block `K = exp((2 a_τ) Q)`. This is the most aggressive joint
   normalization available — ONE clock drives BOTH objects — precisely the case
   most likely to pin the unit if anything can.

Apply the candidate **second-clock-unit rescaling** the wall predicts is free:

```
a_τ → c · a_τ ,   H → H / c ,   Q → Q / c        (c > 0).
```

- **CRACK criterion:** some observable built ONLY from A_min + GATE-S + GATE-R
  changes under this rescaling ⟹ the system forces `c = 1` ⟹ `a_τ` absolute.
- **WALL criterion:** EVERY such observable is invariant ⟹ only dimensionless
  ratios are fixed; `a_τ → c·a_τ` is an exact gauge ⟹ unit NOT derived.

## 3. Worked steps and residuals (runner blocks)

- **[A]** Both gate objects build correctly on the A_min surface: `T̂²` positive
  Hermitian with spectrum in `(0, M_T]`; `1/(2 a_τ)` reconstruction recovers `H`
  (resid 0, N2a forced); `Q` columns sum to zero and `Q π = 0` (`‖Qπ‖ 2.8e-17`).

- **[B] CORE.** Under the joint rescaling, `T̂² = exp(-2 a_c H_c) = exp(-2 a_τ H)`
  is invariant (max Δ `5.6e-17`); the record-block kernel
  `K = exp(2 a_c Q_c) = exp(2 a_τ Q)` is invariant (max Δ `3.3e-16`); and the
  FULL joint per-block evolution `T̂² ⊗ K` is invariant (max Δ `3.3e-16`).
  Swept over `c ∈ {0.5, 1.3, 2.0, 5.0}`. **The absolute unit is gauge.**

- **[C] What the gates DO fix.** The dimensionful mass gap `m_gap` CHANGES under
  rescaling (it carries `1/a_τ`); the dimensionful relaxation rate of `Q`
  CHANGES likewise; but the DIMENSIONLESS ratio `m_gap / relaxation_rate` is
  INVARIANT (`0.400000`, max dev `5.6e-17`). Equivalently the joint gates pin
  `m_gap · relaxation_TIME` — a pure number — exactly as GATE-R's `r·t`
  invariance already states. The gates fix a RATIO, not a unit.

- **[D] STEELMAN — explicit record-rate datum.** Supply `ν` record events per
  transfer block (the only thing post-record counts can give: per
  `POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06`, counts fix order + number, not
  seconds). The count-per-block datum is clock-free (invariant under `c`).
  Converting it to a per-time rate `ν/(2 a_τ)` changes under `c` ONLY because we
  inserted `a_τ` in seconds — circular, not an A_min observable. Decisive
  structural point checked: **no A_min observable returns a unit-bearing
  `1/time` number**; every observable is a dimensionless ratio of two such, or a
  pure count, so no datum can fix `c`.

- **[E] Exact 1-parameter symmetry group.** `c = 1` is the identity;
  composition `c₁·c₂` leaves observables `(T̂², K)` at their fixed point; the
  stabilizer of the observable data is the full multiplicative group `R_{>0}`.
  No `c` is preferred ⟹ the absolute unit is undetermined.

## 4. Honest OUTCOME

**WALLED (ratio-only), as expected — confirmed by an explicit, worked
rescaling-invariance falsifier.** The two retained rate gates JOINTLY — even
under the strongest single-clock coupling where one clock drives both the
transfer and the record stream — fix only dimensionless ratios
(`m_gap · relaxation-time`, counts-per-block). The simultaneous rescaling
`a_τ → c·a_τ`, `H → H/c`, `Q → Q/c` is an EXACT 1-parameter gauge of the joint
construction: `T̂²`, `K`, and `T̂² ⊗ K` are all invariant. The absolute clock
unit `a_τ` is NOT derived. This did NOT crack N2b.

The route's value for the consolidated no-go: it CLOSES the N1 honesty gap on
N2b by genuinely building the joint two-gate construction (not just citing the
single-gate UNIQUENESS_SCOPE_BOUNDARY argument). It strengthens the wall with a
basis-free structural reason — **no A_min observable carries units of `1/time`**
— so the rescaling invariance is not an artifact of the diagonal exhibit but a
property of the entire observable algebra reachable from A_min + the two gates.

## 5. Named load-bearing wall + authority

**Wall:** the absolute physical clock unit / time metric requires a metric scale
that A_min does not supply. Two independent A_min withholdings combine:

- **Lattice** supplies the site set and adjacency but "does not supply a …
  metric scale, lattice spacing, … or physical unit conversion"
  (`MINIMAL_AXIOMS_2026-06-05.md`, Lattice clause).
- **Record** supplies durable outcomes and finite scalar additivity but "supplies
  no … time metric, … rate" (`MINIMAL_AXIOMS_2026-06-05.md`, Record clause);
  finite histories fix order + counts, not seconds
  (`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06`).

**Retained authority the wall rests on:**
`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md` (retained_no_go) — Stone
reconstruction is transfer-relative and τ-relative; `2 a_τ → 2c·a_τ` rescales
`H` by `1/c` with `T̂²` unchanged. This route shows that adding GATE-R to GATE-S
does not escape that boundary: the rescaling extends verbatim to the record-rate
generator, so the joint system inherits the same gauge.

**Where the residual relocates:** the emergent-dynamics / clock-rate OPEN GATE of
the minimal axioms. A_min (Lattice/Quantum/Record) supplies no dynamics and no
metric scale; any downstream physical-rate or unitful claim must identify a
SEPARATE supplied clock/rate bridge that carries an actual `1/time` unit. No
retained framework row supplies one.

## 6. What the consolidated no-go should carry from this attempt (for N1/N7)

- **N2b is route-honest:** the joint two-gate construction was genuinely built,
  not asserted. The expected ratio-only outcome is now backed by a 17/0 runner.
- **Carry the exact falsifier:** the explicit 1-parameter gauge
  `(a_τ, H, Q) → (c·a_τ, H/c, Q/c)` with `T̂²`, `K`, and `T̂² ⊗ K` invariant
  (residuals `< 4e-16`) — the basis-free statement that the joint observable
  algebra's stabilizer of `a_τ` is the full `R_{>0}`.
- **Carry the sharpened structural reason:** *no A_min observable returns a
  unit-bearing `1/time` number* — every observable is a dimensionless ratio or a
  pure count (block [D]). This is a stronger N2b wall statement than the
  single-gate rescaling argument: it explains WHY no additional gate of this
  type can ever pin the unit.
- **Keep N2a separate:** N2a (the `1/(2 a_τ)` internal denominator) remains
  FORCED/exact-support (resid 0, block [A]); only N2b walls. The no-go must not
  relist N2 as a single opaque import.

## 7. Status discipline

This is a branch-local source artifact. It does NOT add a framework axiom, does
NOT introduce a primitive, does NOT set or update any audit status, and does NOT
edit any audit/publication/effective-status surface. Branch-local status
vocabulary only; the independent audit lane is the sole status authority.
`proposal_allowed: false`; `bare_retained_allowed: false`. The cited upstream
statuses (`retained_bounded`, `retained_no_go`, `exact-support`) are quoted from
their source notes, not reasserted here; all load-bearing facts (the joint
rescaling invariance, the dimensionless-ratio fixity) are recomputed in the
paired runner.
