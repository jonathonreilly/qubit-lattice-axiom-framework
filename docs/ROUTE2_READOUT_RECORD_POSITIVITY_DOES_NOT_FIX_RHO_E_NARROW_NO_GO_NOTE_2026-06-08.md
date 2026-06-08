---
claim_id: route2_readout_record_positivity_does_not_fix_rho_e_narrow_no_go_note_2026-06-08
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Registration and Positivity Conditions Do Not Fix the Route-2 Readout rho_E

**Date:** 2026-06-08
**Claim type:** no_go.
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived after
independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_route2_readout_record_positivity_no_go.py`](../scripts/frontier_route2_readout_record_positivity_no_go.py)
**Cached log:**
[`logs/runner-cache/frontier_route2_readout_record_positivity_no_go.txt`](../logs/runner-cache/frontier_route2_readout_record_positivity_no_go.txt)
(TOTAL: PASS=8 FAIL=0)

## 0. The frame this closes

The Route-2 readout-to-slice coupling — the program's single highest-descendant open gate
(`s3_time_theta_to_slice_coupling`, ~819 descendants) — inherits its sole blocker from the
readout map: after the T-side is granted, the only free entry is `ρ_E = β_E/α_E`, and the
retained no-gos
[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
and
[`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
establish the carrier admits **every** `ρ_E`. Those notes tested five frames
(carrier-naturality, T-side transfer, symmetry, low-rationality, source-domain color-bridge).
**One frame was not tested there: supplied registration-style readout conditions
(`D(M)=sum_k P_k M P_k`, partial-isometry/idempotency, and additive scalar
conventions) together with positivity.** This note tests that supplied frame and
closes it. The Record axiom itself is not used to supply the readout context,
projectors, decomposition, `P_R`, positivity rule, or scalar convention.

**It does not fix `rho_E`.** The tested registration/positivity conditions are
**norm** conditions (functions of `P_R P_R^dag` or of signs); `rho_E` is the
readout's **direction** in the (shell, center) plane, and is left free. Selecting
`rho_E` requires a shell-vs-center **distinguishing** input — for example the
separate gravity-metric response lane (live value near `5.2575`) or the
conditional color bridge `c_TE = -R_conn = -8/9` (which gives `21/4`) — **not**
a generic registration principle. The tested carrier-rescale gauge freedom also
does not remove `rho_E`, so the companion handedness gauge-resolution does not
transfer.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| carrier columns; readout `P_R=[[alpha_E,0,beta_E,0],[0,alpha_T,0,beta_T]]`; carrier admits every `rho_E` | [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | `retained_no_go` | the readout structure |
| five tested frames leave `rho_E` free | [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) | `retained_no_go` | the frames this note extends |
| color bridge `c_TE=-R_conn` gives `rho_E=21/4` conditionally (no typed cross-domain bridge) | [`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | `retained_no_go` | a distinguishing-input lead |
| `delta_A1(center)=1/6` an exact support-side observable | [`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md) | `retained_bounded` | carrier-rescale invariance input |
| `q_E=15/8` gives `rho_E=21/4` as a nearest-rational scan match; the live gravity-metric value is near `5.2575` | [`QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19`](QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md) | `audited_numerical_match` | comparator / residual context |

No PDG value is load-bearing. The companion flavor handedness-gauge note is
named as context, not a citation-graph dependency. No new axiom, primitive,
import, or vocabulary is introduced.

## 2. Setup

On the four carrier columns `E_shell=(1,0,0,0)`, `E_center=(1,0,1/6,0)`, `T_shell=(0,1,0,0)`,
`T_center=(0,1,0,1/6)`, the bright readout reads each channel as a combination of its **shell**
(`u_E`) and **center-excess** (`delta_A1 u_E`) endpoints. After the T-side is granted, the free
entry is `rho_E = beta_E/alpha_E = 6(q_E-1)`, `q_E = gamma_E(center)/gamma_E(shell)`. Geometrically `rho_E` is the
**slope** (direction) of the E-readout row in the `(u_E, δ_A1 u_E)` plane.

## 3. Registration and positivity conditions fix the norm, not rho_E

Each supplied registration/positivity condition was tested (runner):

- **(N1) Partial isometry / norm-preserving registration** `P_R P_R^† = I_2`. Admits a
  solution for **every** `rho_E` (it fixes `|alpha_E| = 1/sqrt(1+rho_E^2)`). `rho_E` free.
- **(N2) Registration idempotency** — `D = P_R^† P_R` a projection ⟺ `P_R P_R^† = I_2`, the
	  same family. `rho_E` free.
- **(N3) Positivity** (nonnegative carrier columns ↦ nonnegative slice). Gives only the
  **one-sided bound** `rho_E > -6`, never a unique value.
- **(N4) The additive `I`-scalar as column-sum preservation** forces `rho_E = 1` — an
	  **arbitrary convention** (column-sum), and it equals **neither** the live value
  `5.2575` **nor** the color-clean `21/4`; it is not a record principle.

**(STRUCT) The structural reason.** Every record/positivity condition is a function of
`P_R P_R^dag` (a norm) or of signs. An `O(2)` rotation of the `(alpha_E, beta_E)` readout coefficients
**preserves the norm** while sweeping `rho_E = beta_E/alpha_E = tan(theta)` over the whole line (verified:
norm constant `=1` while `rho_E` sweeps `[-9.9, 9.9]`). So no norm/sign condition can fix the
**direction** `rho_E`. Selecting `rho_E` requires a shell-vs-center **distinguishing** input.

## 4. Distinguishing inputs and carrier-rescale invariance

The obstruction is specifically the lack of a distinguishing input, not a blanket
impossibility:

- **(NONVAC) A distinguishing input can fix it.** The **color bridge** `c_TE = -R_conn = -8/9`
  (the SU(3) color projection `1−1/N_c²`), with the granted T-side, forces `q_E = 15/8` and
  `rho_E = 21/4` exactly — a **cross-domain** (color -> support-endpoint) input, not a
  registration principle, and itself a `retained_no_go` for lack of a typed bridge. The
  **gravity-metric directional response** is the other distinguishing-input lane and carries
  the live value near `rho_E = 5.2575`; this note does not derive that lane.
- **(GAUGE) Carrier rescale does not remove `rho_E`.** A carrier rescale `u_E -> lambda u_E`
  rescales `delta_A1 u_E -> lambda delta_A1 u_E` too (`delta_A1` linear), leaving
  `rho_E = beta_E/alpha_E` invariant. Thus the companion absolute-handedness gauge-resolution
  does **not** transfer to this tested carrier-rescale freedom.

## 5. Scope — what this establishes and does not

**Establishes (exact / finite):**
- Supplied registration / idempotency / positivity conditions on `P_R` fix the
  readout **norm** (or a one-sided bound), not `rho_E`.
- The structural reason: `rho_E` is the readout direction; these are norm/sign conditions.
- `rho_E` is invariant under the tested carrier-rescale freedom, so the handedness
  gauge-resolution does not transfer.
- Non-vacuously, a shell-vs-center distinguishing input could fix it; the color bridge
  gives `21/4` conditionally, while the gravity-metric lane carries the live value near
  `5.2575`.

**Does NOT establish (separate / open):**
- It does **not** fix `rho_E`; it closes only the supplied registration/positivity frame.
- It does **not** resolve the gravity-metric (`5.2575`) vs color-clean (`21/4`) question.
- It does **not** build the typed color→support-endpoint bridge (the located residual).

## 6. Honest verdict

Taking the supplied registration/positivity frame seriously, the answer is a
clean **no**: registration, idempotency, additive-scalar conventions, and
positivity all fix the readout **norm** (or a bound), while `rho_E` is the
readout **direction**, left free. The tested carrier-rescale gauge freedom does
not remove `rho_E`, so the companion handedness gauge-resolution does not
transfer. The readout-selection residual is therefore a **shell-vs-center
distinguishing-input theorem** — such as the typed color->support-endpoint
bridge (`c_TE = -R_conn`, which would force `21/4`) or the gravity-metric
response lane — **not** a generic registration principle.

## 7. No-Go Discipline Gate

**Status:** PASS for this bounded readout-selection no-go. It says the supplied
registration/positivity conditions do **not** fix `rho_E`; it does **not** claim `rho_E` is underivable, that `5.2575` is unphysical,
or that the color bridge is impossible.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| partial isometry / idempotency (registration) | ATTEMPTED | fixes norm; `rho_E` free |
| positivity | ATTEMPTED | one-sided bound only |
| additive `I`-scalar (column-sum) | ATTEMPTED | arbitrary `rho_E=1`, not the live value |
| color bridge `c_TE=-R_conn` | OPEN RESIDUAL | distinguishing input -> `21/4` conditionally; typed bridge missing |
| gravity-metric response | OPEN RESIDUAL | separate lane with live value near `rho_E=5.2575`; outside this no-go |

**N2 — Wall-independence.** The registration/positivity frame (this note), the color bridge, the
gravity-metric value, and the prior five naturality frames are independent; this note closes
only the registration/positivity frame.

**N3 — Hidden-wall scan.** Uses only the carrier columns, the readout form, and `O(2)`
invariance of norm/sign conditions; no hidden distinguishing premise.

**N4 — Residual matching.** The residual is the shell-vs-center distinguishing input (color
bridge / gravity metric), not a registration principle.

**N5 — Rhetoric audit.** The claim is that the supplied registration/positivity conditions fix norm not direction,
proven by `O(2)` invariance; not a derivation or a blanket impossibility.

**N6 — Partial-closure path scan.** The legitimate next step is the typed color→support-endpoint
bridge theorem (`c_TE=-R_conn`), or an approved input or derivation for the gravity-metric lane. No new axiom requested.

**N7 — Steelman.** A reviewer may propose a *non-isotropic* record condition (e.g. a fixed
central-sector decomposition that distinguishes shell from center). Granted — but that decomposition
is exactly the distinguishing input (it *is* the gravity-metric/color structure), not a generic
registration principle; supplying it is the named residual.

**N8 — Cross-cycle echo.** Extends the retained readout-map and naturality no-gos with the
registration/positivity frame, consistent with the `audited_numerical_match` E-channel quotient and the
`retained_no_go` color-bridge — without overruling any by prose.

## 8. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained-no-go / retained-bounded
  / numerical-match rows plus the supplied readout algebra. The Record axiom supplies no readout
  context, decomposition, weighting rule, positivity rule, or `P_R` map here.
- **No PDG/fitted load-bearing input; no new transcendental.**
- The companion handedness-gauge note is named as context, not a citation-graph dependency.

## 9. Command

```bash
python3 scripts/frontier_route2_readout_record_positivity_no_go.py
```

Expected: `TOTAL: PASS=8 FAIL=0`. numpy + stdlib, deterministic, 4-dim carrier / 2×4 readout
(memory-safe). The runner verifies that partial isometry, idempotency, and positivity leave `rho_E`
free (norm/bound only), that the column-sum `I`-scalar gives an arbitrary `rho_E=1`, the `O(2)`
norm-invariance / direction-sweep structural reason, the non-vacuous color-bridge and gravity-metric
distinguishing-input lanes, and carrier-rescale invariance of `rho_E`.
