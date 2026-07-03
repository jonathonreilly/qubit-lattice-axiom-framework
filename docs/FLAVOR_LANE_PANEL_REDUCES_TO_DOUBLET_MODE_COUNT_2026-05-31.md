# Flavor Lane Algebra and Doublet Mode-Count Branch Inventory

**Date:** 2026-05-31; audit-scope repair 2026-06-08
**Claim type:** bounded_theorem
**Claim boundary:** finite lane-vs-channel algebra, two explicit mode-count branches, and two non-forcing escape checks. The panel's universal exhaustiveness thesis is route support, not a retained conclusion of this row.
**Runner:** `scripts/flavor_lane_panel_reduces_to_doublet_mode_count_2026_05_31.py` (SCORECARD 13/13).
**Source:** workflow `wf_9028152c` — 20-physicist panel + 4 meta-exercises (assumptions / first-principles / literature / math-rigor), framed find-the-escape, + chair synthesis (25 agents). Convened at user request.

## Question
Is the determination correct that the three Koide values {1/3, 2/3, 1} are **lanes** (settings of the
ratio `r=|b|²/a²`), not three **channels** of one operator — and what (if anything) forces the
charged-lepton sector to **r=1/2** (C₃ isotype equipartition)?

## Verdict

### D1 — UNANIMOUS (24/24, no dissent): the three values are LANES, not channels
`Q` is a **single** observable `Q = 1/3 + (2/3)r`, the **ratio** channel — δ-independent and
**scale-invariant** (runner D1). A single sector has one `r`, hence one `Q`. So {1/3, 2/3, 1} are three
**settings of `r`** (three lanes: degenerate / equipartition / maximal-hierarchy), **not** three
channels. The genuine orthogonal channels are `{scale a (Q-invariant), ratio r (sets Q), phase
δ=arg b (Q-orthogonal CP)}` + the topological index `2/9`. **This corrects the prior
`FLAVOR_VALUE_CAMPAIGN_CAPSTONE_FOUR_CHANNEL` note**, which mislabeled `Q=1/3` and `Q=1` as separate
channels — they are the `r=0` and `r=1` lane-points of the *one* ratio observable. (The user's lane
reading is the correct one.)

### Assignment — open_confirmed; finite branch algebra exposes one named decider
No escape in this packet forces `r=1/2` from framework baseline+emergent-spacetime. The source packet verifies the lane-vs-channel algebra and the two finite mode-count branches of the named det_C/det_R candidate:
**block-count (1,1) vs dimension-count (1,2)  =  det_C vs det_R  =  doublet is ONE complex mode vs TWO
real modes.** Verified (runner BRANCH):
- equal power **per block** (`3a² = 6|b|²`, det_C, doublet = 1 complex mode) → `r=1/2` → `Q=2/3`;
- equal power **per real dimension** (`3a² = 3|b|²`, det_R, doublet = 2 real modes) → `r=1` → `Q=1`.

Thus the det_C/det_R proposal would decide the charged-lepton lane if a later restricted bridge proves that the admissible lane-selection mechanisms reduce to this metric choice. This row does **not** claim that universal exhaustiveness. It sits on the retained obstruction:
`koide_frobenius_isotype_split_uniqueness` (retained_no_go — the C₃-invariant Gram is a 2-parameter
block-constant cone with the singlet:doublet ratio **free**) and `action_normalization` (retained_no_go —
declines to rank (1,1) vs (1,2)).

2026-06-08 audit-scope repair: the source-side retained-eligible content of this row is the accepted `Q` identity, the lane
interpretation of `{1/3, 2/3, 1}`, the Casimir/swap non-forcing check, and the det_C/det_R branch
calculations above. The not-retained bridge is the holomorphic/Kähler metric or other restricted-packet
theorem proving that all admissible charged-lepton lane-selection mechanisms are exhausted by this
det_C/det_R choice.

### Dependency packets made explicit for re-audit

The two obstruction packets used above are concrete graph dependencies, not
bare labels:

- Frobenius isotype split:
  [`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md),
  runner
  [`scripts/frontier_koide_frobenius_isotype_split_uniqueness.py`](../scripts/frontier_koide_frobenius_isotype_split_uniqueness.py),
  cache
  [`logs/runner-cache/frontier_koide_frobenius_isotype_split_uniqueness.txt`](../logs/runner-cache/frontier_koide_frobenius_isotype_split_uniqueness.txt).
- Action normalization:
  [`ACTION_NORMALIZATION_NOTE.md`](ACTION_NORMALIZATION_NOTE.md),
  runner
  [`scripts/frontier_action_normalization.py`](../scripts/frontier_action_normalization.py),
  cache
  [`logs/runner-cache/frontier_action_normalization.txt`](../logs/runner-cache/frontier_action_normalization.txt).

The paired runner checks that both dependency rows are currently
`audited_clean` / `retained_no_go` in `docs/audit/data/audit_ledger.json` and
that their source runners/caches are present. This does not edit the audit
ledger; it makes the cited dependency packets visible in the source packet for
independent re-audit.

### Two escapes KILLED (the wrong-escape check)
- **The most-converged escape (10+ specialties): "r=1/2 = self-dual fixed point of the swap `r→1−r`"
  is a SCALAR RELABELING, not a forcing.** Verified (runner ESC1-KILLED): `r→1−r` changes the Casimir
  `Tr(H²)=3a²+6|b|²` except at `r=1/2`, so it is **not** realized by any C₃-covariant operator
  involution — it moves power between channels and changes the invariant. The convergence is on the
  *geometry* of `r=1/2` (it genuinely IS the unique power-swap / AM-GM / MaxEnt-on-2-channels point),
  **not** a mechanism. This is the no-coincidence signal misread — the real triple-convergence
  (Adversarial-no-go + Math-Rigor meta + retained ledger) is on the **obstruction**: the genuine
  equipartition theorem *per quadratic DOF* gives `r=1` (Q=1), and `r=1/2` needs the block/holomorphic
  measure nothing on the retained surface fixes.
- **The antilinear CPT / real-structure reflection does not force equal-block** either (consistent with
  `koide_real_rep_block_count_permitted_not_forced`, *unaudited* — mentioned, not load-bearing).

### The honest survivor — and the one decidable next calculation
The single escape the adversarial no-go specialist could **not** kill from first principles is the
**holomorphic / Kähler collapse**: Axiom 1's qubit complex structure `J` makes the Bargmann coherent-state
(det_C) measure canonical, counting `b` as **one complex mode** (phase = gauge) → (1,1) → `r=1/2`. It is
honest precisely because it openly imports `J` as the measure-canonicalizer — a genuine, non-circular
*missing ingredient* (a measure choice), not a forcing. Its appeal: it would simultaneously explain why
`δ=arg b` is a free Tier-A admission (the gauge phase).

The panel synthesis makes the open datum a **single, sharply-posed, framework-internal calculation** if its
exhaustiveness premise is later proved: derive the field-space metric on the doublet coefficient `b` from
the Quantum axiom's one-qubit coherent-state resolution-of-identity restricted to the hw=1 C₃ orbit, and ask whether the
doublet kinetic term is **holomorphic `|∂b|²`** (one complex mode → det_C → `r=1/2` → `Q=2/3`) or
**doubled-real `(∂Re b)²+(∂Im b)²`** (two modes → det_R → `r=1` → `Q=1`). This is not the continuous
`U(1)_b` route the retained no-go closed and not the discrete-reflection route checked above. If a retained
holomorphic bridge is proved, `r=1/2` becomes derived relative to that bridge; if a retained doubled-real
bridge is proved, `r=1` is the framework branch. Until such a bridge is supplied, the metric selection is
open route support.

## Net standing
The row cleanly retains the lane structure, the finite `Q=1/3+(2/3)r` identity, the Casimir/swap
non-forcing check, and the two finite mode-count branches:
det_C gives `r=1/2` / `Q=2/3`, while det_R gives `r=1` / `Q=1`. The stronger claim that the charged-lepton
assignment is exhausted by this binary remains an open bridge theorem, shared with the standing
holomorphic/Kähler metric datum across the flavor sector.

## Provenance (verified 2026-05-31)
- D1, the swap-kill (Casimir-change), the dependency packet, and the det_C/det_R → r=1/2 / r=1 branch algebra verified directly (runner 13/13).
- Anchors: `koide_frobenius_isotype_split_uniqueness` (**retained_no_go**), `action_normalization` (**retained_no_go**); `koide_signed_eigenvalue_vs_singular_value_readout` (**audited_failed**); `koide_real_rep_block_count_permitted_not_forced` (**unaudited** — mentioned, not load-bearing).
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
