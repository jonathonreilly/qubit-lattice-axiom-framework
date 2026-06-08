# Record-Ontology and Positivity Conditions Do Not Fix the Route-2 Readout ρ_E

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a readout-selection no-go: norm, not direction)
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived after
independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_route2_readout_record_positivity_no_go.py`](../scripts/frontier_route2_readout_record_positivity_no_go.py)
**Cached log:**
[`logs/runner-cache/frontier_route2_readout_record_positivity_no_go.txt`](../logs/runner-cache/frontier_route2_readout_record_positivity_no_go.txt)
(TOTAL: PASS=8 FAIL=0)

## 0. The opening this closes

The Route-2 readout-to-slice coupling — the program's single highest-descendant open gate
(`s3_time_theta_to_slice_coupling`, ~819 descendants) — inherits its sole blocker from the
readout map: after the T-side is granted, the only free entry is `ρ_E = β_E/α_E`, and the
retained no-gos
[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
and
[`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
establish the carrier admits **every** `ρ_E`. Those notes tested five frames
(carrier-naturality, T-side transfer, symmetry, low-rationality, source-domain color-bridge).
**One frame was never tested: the framework's own central principle — the record ontology
(registration / the canonical `D(M)=Σ_k P_k M P_k` / the additive `I`-scalar) together with
positivity.** This note tests it and closes it.

**It does not fix `ρ_E`.** Record-ontology and positivity conditions are **norm** conditions
(functions of `P_R P_R^†` or of signs); `ρ_E` is the readout's **direction** in the
(shell, center) plane, and is left free. Selecting `ρ_E` requires a shell-vs-center
**distinguishing** input — the gravity-metric response (→ `5.2575`) or the color bridge
`c_TE = -R_conn = -8/9` (→ `21/4`) — **not** a registration principle. And `ρ_E` is
**physical, not gauge**, so the companion handedness gauge-resolution does **not** transfer.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| carrier columns; readout `P_R=[[α_E,0,β_E,0],[0,α_T,0,β_T]]`; carrier admits every `ρ_E` | [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | `retained_no_go` | the readout structure |
| five tested frames leave `ρ_E` free | [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) | `retained_no_go` | the frames this note extends |
| color bridge `c_TE=-R_conn` ⟹ `ρ_E=21/4` (no typed cross-domain bridge) | [`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | `retained_no_go` | the distinguishing-input lead |
| `δ_A1(center)=1/6` an exact support-side observable | [`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md) | `retained_bounded` | why `ρ_E` is basis-independent |
| `q_E=15/8 ⟹ ρ_E=21/4` is a nearest-rational scan match (live `ρ_E≈5.2575`) | [`QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19`](QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md) | `audited_numerical_match` | the genuine value |

No PDG value is load-bearing. The companion flavor handedness-gauge note is named as context,
not a citation-graph dependency. No new axiom, import, or vocabulary.

## 2. Setup

On the four carrier columns `E_shell=(1,0,0,0)`, `E_center=(1,0,1/6,0)`, `T_shell=(0,1,0,0)`,
`T_center=(0,1,0,1/6)`, the bright readout reads each channel as a combination of its **shell**
(`u_E`) and **center-excess** (`δ_A1 u_E`) endpoints. After the T-side is granted, the free
entry is `ρ_E = β_E/α_E = 6(q_E−1)`, `q_E = γ_E(center)/γ_E(shell)`. Geometrically `ρ_E` is the
**slope** (direction) of the E-readout row in the `(u_E, δ_A1 u_E)` plane.

## 3. Record-ontology and positivity conditions fix the norm, not ρ_E

Each natural record/positivity condition was tested (runner):

- **(N1) Partial isometry / norm-preserving registration** `P_R P_R^† = I_2`. Admits a
  solution for **every** `ρ_E` (it fixes `|α_E| = 1/√(1+ρ_E²)`). `ρ_E` free.
- **(N2) Registration idempotency** — `D = P_R^† P_R` a projection ⟺ `P_R P_R^† = I_2`, the
  same family. `ρ_E` free.
- **(N3) Positivity** (nonnegative carrier columns ↦ nonnegative slice). Gives only the
  **one-sided bound** `ρ_E > −6`, never a unique value.
- **(N4) The additive `I`-scalar as column-sum preservation** forces `ρ_E = 1` — an
  **arbitrary convention** (column-sum), and it equals **neither** the framework value
  `5.2575` **nor** the color-clean `21/4`; it is not a record principle.

**(STRUCT) The structural reason.** Every record/positivity condition is a function of
`P_R P_R^†` (a norm) or of signs. An `O(2)` rotation of the `(α_E, β_E)` readout coefficients
**preserves the norm** while sweeping `ρ_E = β_E/α_E = tan θ` over the whole line (verified:
norm constant `=1` while `ρ_E` sweeps `[−9.9, 9.9]`). So no norm/sign condition can fix the
**direction** `ρ_E`. Selecting `ρ_E` requires a shell-vs-center **distinguishing** input.

## 4. What does fix ρ_E (non-vacuity) — and that ρ_E is physical, not gauge

The obstruction is specifically the lack of a distinguishing input, not a blanket
impossibility:

- **(NONVAC) A distinguishing input fixes it.** The **color bridge** `c_TE = -R_conn = -8/9`
  (the SU(3) color projection `1−1/N_c²`), with the granted T-side, forces `q_E = 15/8` and
  `ρ_E = 21/4` exactly — a **cross-domain** (color → support-endpoint) input, not a record
  principle, and itself a `retained_no_go` for lack of a typed bridge. The **gravity-metric
  `η_floor` directional response** is the other distinguishing input; it gives the genuine
  framework value `ρ_E ≈ 5.2575`, which is **not** `21/4` (the latter is a nearest-rational
  scan match, audited `audited_numerical_match`).
- **(GAUGE) `ρ_E` is physical, not gauge.** A carrier rescale `u_E → λ u_E` rescales
  `δ_A1 u_E → λ δ_A1 u_E` too (`δ_A1` linear), leaving `ρ_E = β_E/α_E` invariant; with
  `δ_A1=1/6` a fixed observable there is no convention freedom. So the companion
  absolute-handedness-is-gauge resolution **does not transfer** — `ρ_E` cannot be dissolved as
  a labeling convention.

## 5. Scope — what this establishes and does not

**Establishes (exact / finite):**
- Record-ontology / registration / idempotency / positivity conditions on `P_R` fix the
  readout **norm** (or a one-sided bound), not `ρ_E`.
- The structural reason: `ρ_E` is the readout direction; these are norm/sign conditions.
- `ρ_E` is physical, not gauge (the handedness resolution does not transfer).
- Non-vacuously, a shell-vs-center distinguishing input (color bridge → `21/4`; gravity
  metric → `5.2575`) does fix it.

**Does NOT establish (separate / open):**
- It does **not** fix `ρ_E`; it closes the record/positivity frame.
- It does **not** resolve the gravity-metric (`5.2575`) vs color-clean (`21/4`) question — the
  framework's genuine value is `5.2575`, with `21/4` a numerical match.
- It does **not** build the typed color→support-endpoint bridge (the located residual).

## 6. Honest verdict

Taking the readout-selection seriously through the framework's own central principle — the
record ontology — the answer is a clean **no**: registration, idempotency, the additive
`I`-scalar, and positivity all fix the readout **norm** (or a bound), while `ρ_E` is the
readout **direction**, left free. And unlike the flavor handedness, `ρ_E` is **physical, not
gauge**, so it cannot be dissolved. The readout-selection residual is therefore precisely a
**shell-vs-center distinguishing-input theorem** — the typed color→support-endpoint bridge
(`c_TE = -R_conn`, which would force the clean `21/4`) or the gravity-metric response (the
genuine `5.2575`) — **not** a registration principle. This closes the record-ontology frame on
the program's highest-leverage gate and relocates the open target with no over-idealization.

## 7. No-Go Discipline Gate

**Status:** PASS for this bounded readout-selection no-go. It says record/positivity conditions
do **not** fix `ρ_E`; it does **not** claim `ρ_E` is underivable, that `5.2575` is unphysical,
or that the color bridge is impossible.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| partial isometry / idempotency (registration) | RULED OUT | fixes norm; `ρ_E` free |
| positivity | RULED OUT | one-sided bound only |
| additive `I`-scalar (column-sum) | RULED OUT | arbitrary `ρ_E=1`, not framework value |
| color bridge `c_TE=-R_conn` | OPEN RESIDUAL / PATH | distinguishing input → `21/4` (typed bridge missing) |
| gravity-metric response | GENUINE VALUE | `ρ_E≈5.2575` (the framework's honest readout) |

**N2 — Wall-independence.** The record/positivity frame (this note), the color bridge, the
gravity-metric value, and the prior five naturality frames are independent; this note closes
only the record/positivity frame.

**N3 — Hidden-wall scan.** Uses only the carrier columns, the readout form, and `O(2)`
invariance of norm/sign conditions; no hidden distinguishing premise.

**N4 — Residual matching.** The residual is the shell-vs-center distinguishing input (color
bridge / gravity metric), not a registration principle.

**N5 — Rhetoric audit.** The claim is that record/positivity conditions fix norm not direction,
proven by `O(2)` invariance; not a derivation or a blanket impossibility.

**N6 — Partial-closure path scan.** The legitimate next step is the typed color→support-endpoint
bridge theorem (`c_TE=-R_conn`), or accepting the gravity-metric `5.2575`. No new axiom requested.

**N7 — Steelman.** A reviewer may propose a *non-isotropic* record condition (e.g. a fixed
central-sector decomposition that distinguishes shell from center). Granted — but that decomposition
is exactly the distinguishing input (it *is* the gravity-metric/color structure), not a generic
registration principle; supplying it is the named residual.

**N8 — Cross-cycle echo.** Extends the retained readout-map and naturality no-gos with the
record/positivity frame, consistent with the `audited_numerical_match` E-channel quotient and the
`retained_no_go` color-bridge — without overruling any by prose.

## 8. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained-no-go / retained-bounded
  / numerical-match rows plus the readout algebra.
- **No PDG/fitted load-bearing input; no new transcendental.**
- The companion handedness-gauge note is named as context, not a citation-graph dependency.

## 9. Command

```bash
python3 scripts/frontier_route2_readout_record_positivity_no_go.py
```

Expected: `TOTAL: PASS=8 FAIL=0`. numpy + stdlib, deterministic, 4-dim carrier / 2×4 readout
(memory-safe). The runner verifies that partial isometry, idempotency, and positivity leave `ρ_E`
free (norm/bound only), that the column-sum `I`-scalar gives an arbitrary `ρ_E=1`, the `O(2)`
norm-invariance / direction-sweep structural reason, the non-vacuous color-bridge and gravity-metric
distinguishing inputs, and that `ρ_E` is basis-independent (physical, not gauge).
