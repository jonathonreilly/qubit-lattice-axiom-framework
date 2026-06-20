# Block02 Section — N2 (blocked time-step)

**B-AXIS clause:** B-AXIS.1 = N2 — "one supplied blocked time step `2 a_τ`."
**Decomposition (carried verbatim from the blocked-time-unit-split branch):**

- **N2a** — the INTERNAL blocked-transfer denominator `1/(2 a_τ)`. This is
  **SUPPLIED / exact-support FORCED**, *not* a wall.
- **N2b** — the ABSOLUTE physical clock unit `a_τ` (a number carrying units of
  time). This is the **NO-GO** half: underivable from A_min.

**Type:** mixed by sub-clause. N2a = exact-support (internal denominator forced
for the supplied object). N2b = exact negative boundary / no-go (absolute clock
unit not derivable from Lattice / Quantum / Record / post-record counts /
transfer-spectrum). **Claim type (intended audit classification):** N2a
bounded exact-support; N2b negative_route_pruning. Independent audit lane is the
sole status authority; nothing here is retained, promoted, or audit-ratified.

**Hard separation enforced throughout:** N2 is NOT a single opaque import. The
two-step transfer FORCES the denominator (N2a); the absolute unit is gauge
(N2b). Only N2b walls.

---

## N2a — exact-support FORCED (positive; the `1/(2 a_τ)` denominator is supplied)

### Statement

For the supplied two-step staggered transfer `T̂² = exp(-2 a_τ H)` (`H ≥ 0`,
vacuum-normalized), the aligned spectral reconstruction

```
H_block = -(1/(2 a_τ)) · log(T̂² / M_T) = Ĥ − E₀
```

is FORCED internally by the retained two-step blocked-time normalization
bridge. The `1/(2 a_τ)` denominator is a source-side consequence of the
already-retained `T̂²` object — it is **not a new import, axiom, or primitive**.

### The factor-two falsifier (the discriminating certificate)

The wrong one-step denominator `1/a_τ` applied to the SAME `T̂²` doubles every
non-vacuum energy:

```
H_wrong = -(1/a_τ) · log(T̂² / M_T) = 2 · H_block .
```

This factor-two falsifier is what makes N2a a *forced* result rather than a
convention: only `1/(2 a_τ)` recovers the correct generator from the two-step
object; `1/a_τ` is exactly excluded.

### Recomputed in-tree (load-bearing, not cited blind)

The in-tree block01 runner recomputes the N2a reconstruction directly on the
A_min surface (block [A]):

- `scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py`, block [A]:
  `[PASS] GATE-S: 1/(2 a_τ) reconstruction recovers H (N2a forced) :: resid 0.0e+00`.

Reconstruction residual is exactly 0 — N2a is FORCED and stays FORCED under the
N2b rescaling (block [B] confirms `T̂²` invariant, so the reconstructed `H` is
unchanged structurally; the denominator structure is preserved). N2a is the
exact-support half and must be kept separate from the walled N2b.

### Absorbed runner (cite by branch / path / PASS — NOT rebuilt)

The full N2a exact-support result (denominator forced + factor-two falsifier) is
owned and computed by the **blocked-time-unit-split branch**:

- **Branch:** `origin/physics-loop/single-clock-blocked-time-unit-split-20260617`
- **Note:** `docs/SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md`
- **Runner:** `scripts/single_clock_blocked_time_unit_split_n2_support_2026_06_17.py`
- **Result:** `TOTAL: PASS=35 FAIL=0`
- **Mechanism (cited, not rebuilt):** finite functional calculus on the positive
  vacuum-normalized `T̂²` forces `2 a_τ`; the one-step `1/a_τ` denominator is the
  factor-two falsifier (`H_wrong = 2 H_block`). This is a source-side consequence
  of the retained `T̂²`, citing the two-step normalization bridge
  `AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`.

**Bottom line for N2a:** SUPPLIED, not a wall. The consolidated no-go must never
again relist N2 as a single opaque import — the internal denominator is forced
exact-support; only the absolute unit walls.

---

## N2b — NO-GO (the absolute clock unit `a_τ` is underivable)

### Statement

The absolute physical clock unit / time metric carried by `a_τ` is NOT derivable
from A_min (Lattice + Quantum + Record), nor from post-record count histories,
nor from the transfer spectrum, nor from the two retained rate gates jointly.
The simultaneous rescaling

```
a_τ → c · a_τ ,   H → H / c ,   Q → Q / c        (c > 0)
```

is an **EXACT 1-parameter gauge** of the joint construction: `T̂²`, the record
kernel `K`, and the full joint per-block evolution `T̂² ⊗ K` are all invariant.
The two retained rate gates fix only DIMENSIONLESS ratios; **no A_min observable
carries `1/time` units**, so no datum can fix `c`.

### Absorbed runner — R-N2b-JOINT (in-tree; cite by path / PASS — NOT rebuilt)

The sharpened N2b wall is the block01 fresh-attempt route **R-N2b-JOINT**, whose
runner is IN-TREE on the current stack and recomputes every load-bearing N2b
fact:

- **Runner (in-tree):** `scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py`
- **Branch:** `physics-loop/single-clock-baxis-wall-block01-20260620` (stacked under)
- **Result (recomputed in-tree this cycle):** `TOTAL: PASS=18 FAIL=0`

Load-bearing residuals recomputed in-tree (recompute discipline — NOT taken on
citation):

| block | check | residual |
|---|---|---|
| [A] | `1/(2 a_τ)` reconstruction recovers `H` (N2a forced) | `0.0e+00` |
| [B] | `T̂²` invariant under joint rescaling | max Δ `5.6e-17` |
| [B] | record-block kernel `K = exp(2 a_τ Q)` invariant | max Δ `3.3e-16` |
| [B] | FULL joint `T̂² ⊗ K` invariant → `a_τ` is gauge | max Δ `3.3e-16` |
| [C] | dimensionless ratio `m_gap / relax` invariant (the fixed datum) | `0.400000`, max dev `5.6e-17` |
| [D] | record COUNT-per-block datum clock-free under CORRECT joint rescaling | max dev `2.2e-16` |
| [D] | MALFORMED rescaling (`a_τ` scaled, `Q` NOT) MOVES the count datum (proves the 0 is a real computed gauge) | `0.50` |

All resid `< 4e-16` for the gauge invariances; the malformed-rescaling
discriminator moves the count datum by exactly `0.50`, proving the
gauge-invariance zeros are real computed facts and not vacuous identities.

### What R-N2b-JOINT genuinely attempted (closes the N1 honesty gap)

This was a GENUINE fresh derivation attempt, not a citation of the single-gate
argument: it built BOTH retained rate gates and tied them under the strongest
possible single-clock coupling — ONE clock driving both the transfer step and
the record stream (continuous-time record kernel over one transfer block
`K = exp((2 a_τ) Q)`) — precisely the case most likely to over-determine and pin
`a_τ` if anything could.

- **GATE-S** — spectrum-condition blocked-time normalization bridge: supplies
  the dimensionless `T̂² = exp(-2 a_τ H)` and the `1/(2 a_τ)` reconstruction.
- **GATE-R** — record clock/rate normalization gate: a supplied production
  generator `Q` stabilizes a dial (`Q π = 0`); `exp(t Q)` fixes only the
  dimensionless product `t·Q`, so `(r, t)` and `(r/c, c·t)` give the same kernel.

**CRACK criterion:** some A_min + GATE-S + GATE-R observable changes under the
rescaling ⟹ `c = 1` forced ⟹ `a_τ` absolute.
**WALL criterion:** every such observable is invariant ⟹ ratio-only ⟹ unit not
derived.

**Outcome: WALLED (ratio-only).** Every joint observable is invariant
(resid `< 4e-16`); the gates pin `m_gap · relaxation-time` (a pure number) and
counts-per-block (a pure count). The rescaling is an exact 1-parameter group
`R_{>0}` (block [E]: `c = 1` identity, composition `c₁·c₂` fixed, observable
stabilizer is full `R_{>0}`). This did NOT crack N2b.

### The sharpened structural reason (stronger than the single-gate argument)

R-N2b-JOINT strengthens the wall with a basis-free structural fact:

> **No A_min observable returns a unit-bearing `1/time` number.** Every
> observable is a dimensionless ratio of two such, or a pure count — so no datum
> reachable from A_min + the two gates can fix `c`.

This is sharper than the single-gate `UNIQUENESS_SCOPE_BOUNDARY` rescaling
argument: it explains WHY no additional gate of this type can EVER pin the unit,
not just that the two specific gates fail. Block [D]'s malformed-rescaling
discriminator (which moves the count datum by `0.50` when the joint tie is
broken) proves the invariance is a genuine computed gauge, not an artifact of
the diagonal exhibit.

### Why the joint construction does not escape the single-gate boundary

Adding GATE-R to GATE-S does not escape `UNIQUENESS_SCOPE_BOUNDARY_2026-06-06`:
the same `a_τ → c·a_τ` rescaling extends verbatim to the record-rate generator
(`Q → Q/c`), so the joint system inherits the identical gauge. Stone
reconstruction is transfer-relative and τ-relative; `2 a_τ → 2c·a_τ` rescales
`H` by `1/c` with `T̂²` unchanged, and the record stream rides the same scaling.

### Where the residual relocates

The N2b residual relocates to the **emergent-dynamics / clock-rate OPEN GATE** of
the minimal axioms. A_min (Lattice / Quantum / Record) supplies no dynamics and
no metric scale; any downstream physical-rate or unitful (mass-in-seconds)
claim must identify a SEPARATE supplied clock/rate bridge carrying an actual
`1/time` unit. No retained framework row supplies one. B-AXIS.1 therefore stays
LIVE on its N2b half.

---

## Authorities (RETAINED no-gos + minimal-axioms; cited, load-bearing facts recomputed)

- **`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06`** (retained_no_go) —
  Stone reconstruction is transfer-relative and τ-relative; `2 a_τ → 2c·a_τ`
  rescales `H` by `1/c` with `T̂²` unchanged. The single-gate boundary that
  R-N2b-JOINT shows the two-gate joint construction does NOT escape.
- **`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06`** — finite record histories fix
  ORDER + COUNTS, not seconds; the same word + counts under uniform / slow /
  accelerated clocks give distinct elapsed times and rates. Backs block [D]:
  counts-per-block is a pure dimensionless datum, never a per-second number.
- **`MINIMAL_AXIOMS_2026-06-05`** — the two A_min withholdings that combine into
  the wall: **Lattice** supplies sites + adjacency but "does not supply a metric
  scale, lattice spacing, … or physical unit conversion"; **Record** supplies
  durable outcomes + finite scalar additivity but "supplies no time metric, …
  rate." No metric scale + no time metric ⟹ `a_τ` (a unit-bearing number) has no
  A_min supplier.

(Per source discipline: load-bearing N2a/N2b facts were RECOMPUTED in-tree via
`single_clock_n2b_joint_clock_unit_check_2026_06_20.py`; the conditional parent
keystone, the unaudited finite-speed cone note, and the downstream
ANOMALY_FORCES_TIME consumer were NOT taken as citation edges.)

---

## Status discipline

Branch-local source artifact. Adds NO framework axiom, introduces NO primitive,
sets / updates NO audit status, edits NO audit / publication / effective-status
surface. Branch-local status vocabulary only. `proposal_allowed: false`;
`bare_retained_allowed: false`; `audit_required_before_effective_retained: true`.
Cited upstream statuses (`retained_no_go`, `retained_bounded`, `exact-support`)
are quoted from their source notes, not reasserted here. Independent audit lane
is the sole status authority.
