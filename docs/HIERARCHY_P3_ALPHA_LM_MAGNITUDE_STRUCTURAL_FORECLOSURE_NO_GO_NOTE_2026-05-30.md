# Hierarchy P3: `alpha_LM^{16}` Magnitude Substitution — Structural Foreclosure on the `delta = 0` Substrate

**Date:** 2026-05-30
**Claim type:** no_go
**Status:** formal no-go proposal. This note adds no axiom, no fitted input, and
no audit verdict. The independent audit lane sets audit and effective status.
**Status authority:** independent audit lane only. This source note does not
quote, set, or predict an audit outcome for any cited claim_id.
**Primary runner:** [`scripts/frontier_hierarchy_p3_alpha_lm_magnitude_no_go.py`](../scripts/frontier_hierarchy_p3_alpha_lm_magnitude_no_go.py)
**Closure outcome:** B, formal no-go. It tightens the hierarchy formula's `P3`
magnitude primitive from "not derived / non-perturbatively walled" to
"structurally foreclosed on the `delta = 0` substrate." It is NOT a closure of
the hierarchy lane.

## 0. Object being scoped

The hierarchy formula

```text
v = M_Pl * (7/8)^{1/4} * alpha_LM^{16},      alpha_LM = alpha_bare / u_0,
```

uses the primitive substitution `u_0^{16} -> alpha_LM^{16}`
([`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
section `P3`). The honest-status note already records that this is an
**algebraic relabeling**, not a determinant identity, because

```text
alpha_LM^{16} = alpha_bare^{16} * u_0^{-16},                              (S)
```

and the suppression is dominated by the coupling power `alpha_bare^{16} =
(4 pi)^{-16}` (with `g_bare = 1`, so `alpha_bare = 1/(4 pi)`), not by the
determinant power `u_0^{16}`. This note records the next, stronger statement:
the relabeling cannot be **upgraded** to an RG-transport or determinant theorem
on the `Cl(3)/Z^3` substrate. The foreclosure is structural.

This note keeps the lane's `A_min` and forbidden-import list fixed. No PDG
comparator and no fitted coupling is used.

## 1. Inputs (exact / retained, on-main)

| object | value / form | source |
|---|---|---|
| `alpha_bare` | `1/(4 pi)` (`g_bare = 1`) | `g_bare_rigidity_theorem_note` (rescaling convention) |
| substitution `S` | `alpha_LM^{16} = alpha_bare^{16} u_0^{-16}` | [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md) section P3 |
| geometric-mean identity | `alpha_LM = sqrt(alpha_bare * alpha_s)`, `alpha_s(v) = alpha_bare/u_0^2` | [`HIERARCHY_ALPHA_LM_DIM_TRANS_REFRAMING_BOUNDED_NOTATION_EQUIVALENCE_NOTE_2026-05-16.md`](HIERARCHY_ALPHA_LM_DIM_TRANS_REFRAMING_BOUNDED_NOTATION_EQUIVALENCE_NOTE_2026-05-16.md) |
| block determinant | `\|det(D+m)\| = prod_w [m^2 + u_0^2 (3 + sin^2 w)]^4` | [`HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md`](HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md) |
| condensate density | `(1/N) Tr[(D+m)^{-1}] = (m/L_t) sum_w 1/[m^2 + u_0^2 (3 + sin^2 w)]` | [`HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md`](HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md) |

Status authority for each cited claim_id is the independent audit lane
(`rows[<claim_id>]['effective_status']`). This note quotes the **forms and
values** only.

## 2. Theorem (the no-go)

> **Claim.** On the `delta = 0` `Cl(3)/Z^3` substrate, the `P3` substitution
> `u_0^{16} -> alpha_LM^{16}` cannot be promoted from an algebraic relabeling to
> a determinant / condensate / RG-transport theorem. The `(4 pi)^{-16}`
> magnitude is supplied by **no** block observable the framework owns; it enters
> **solely** through the relabeling `alpha_LM = alpha_bare/u_0`, whose
> geometric-progression structure is a power-law-running fingerprint that a
> `delta = 0` substrate cannot source. Hence `P3` is a genuinely **separate**
> admission, and the four candidate derivation classes (block-determinant,
> single-link/fluctuation-measure, RG-trajectory/geometric-mean, KK
> dimensional-transmutation) are all closed.

**Proof skeleton (exact / symbolic; reproduced in the runner).**

1. **The block observables carry only `u_0`.** The determinant factors
   `[m^2 + u_0^2 (3 + sin^2 w)]^4`, the free-energy density, and the condensate
   density `(m/L_t) sum_w 1/[m^2 + u_0^2 (3 + sin^2 w)]` are all exact and all
   contain **only** `u_0` — there is no explicit `alpha_bare` in any of them.
   Therefore the `~ 10^{-18}` suppression, dominated by `alpha_bare^{16} =
   (4 pi)^{-16} = 2.586e-18`, is produced by no determinant / condensate object
   the framework owns; it enters solely via the relabeling `alpha_LM =
   alpha_bare/u_0`.

2. **The relabeling is a power-law-running fingerprint.** The three couplings
   `alpha_bare` (UV cell), `alpha_LM` (geometric mean), `alpha_s(v) =
   alpha_bare/u_0^2` (IR) form an exact geometric progression with constant
   multiplicative ratio `1/u_0`. A constant per-step multiplicative ratio in
   `alpha` is the defining fingerprint of **power-law running**
   `alpha(mu) ~ mu^{-kappa}`, not one-loop running (which is linear in
   `1/alpha` versus `ln mu`): the equal-log-spacing test fails,
   `Delta_2/Delta_1 = u_0 != 1` for `1/alpha`.

3. **`delta = 0` forbids power-law running.** Power-law gauge running in 4D
   requires `delta > 0` compactified extra dimensions (Dienes-Dudas-Gherghetta
   Kaluza-Klein tower). The `Cl(3)/Z^3` substrate has `delta = 0`. Therefore the
   geometric-mean structure is **permanently** a relabeling on this substrate
   and cannot be promoted to an RG trajectory.

4. **Both no-go directions agree.** This magnitude-side foreclosure is
   complementary to the exponent-side regulator no-go
   [`HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md`](HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md):
   that result pins the `(4 pi)^{-16}` prefactor to continuum-Fourier-measure
   inheritance on the naive-staggered surface; this result independently
   confirms it is not a block-determinant, condensate, fluctuation-measure, or
   transport effect. QED.

## 3. Consequence for `C2` and `C3`

The honest-status note's two candidate transport routes for the `alpha_LM^{16}`
suppression are tightened:

- **`C2` (extra-dimension power-law).** Previously recorded as "not theorem
  support for `(H)`." This note upgrades it to **structurally foreclosed**: the
  geometric-progression magnitude requires power-law running, which `delta = 0`
  cannot produce. `C2` is closed.
- **`C3` (per-step Wilsonian taste-staircase transport).** The honest-status
  note already records (inheriting the YT UV-to-IR transport obstruction
  theorem) that per-step one-loop integration across the 16-step staircase is
  non-perturbative at the canonical coupling, leaving a residual `alpha_LM^{16}`
  factor out of scope by design. This note identifies that residual **as** the
  `(4 pi)^{-16}` coupling-power magnitude foreclosed here: the `C3` residual and
  the `P3` magnitude admission are the same object.

## 4. Arithmetic of record

[`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
section `P3` prints the inline figure `alpha_bare^{16} = 1.34e-17`. That figure
is a typo: the exact value is `(4 pi)^{-16} = 2.586e-18` (off by `5.18x`), and
it is inconsistent with that same note's **own** companion numbers
`alpha_LM^{16} = 2.09e-17` and `u_0^{-16} = 8.07`, which force `alpha_bare^{16} =
alpha_LM^{16}/u_0^{-16} = 2.59e-18` via identity `(S)`. The discrepancy is
already flagged by the EW-VEV-bridge note
[`HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md`](HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md).
This note records the corrected value `2.586e-18`; it does **not** edit the
honest-status note. (No claim in this no-go depends on the typo: the structural
argument uses only `alpha_bare = 1/(4 pi)`, identity `(S)`, the geometric
progression, and `delta = 0`.)

## 5. Precise scope (what survives — honesty, non-negotiable)

- **No closure is claimed.** This note does not derive `v`, does not supply the
  `alpha_LM^{16}` magnitude, and does not close the hierarchy lane. It records
  that `P3` is a separate, **imported** admission — the `(4 pi)^{-16}`
  coupling-power suppression is not a determinant/condensate/transport theorem on
  this substrate.
- **What is NOT foreclosed.** The note does not foreclose the EXISTENCE of a
  substrate on which the suppression would be derivable (e.g. a genuinely
  higher-`delta` realization); it forecloses only the promotion on the actual
  `delta = 0` `Cl(3)/Z^3` substrate the framework owns.
- **`P2` (the exponent count `16`) is a separate question** handled elsewhere
  (`HIERARCHY_EXPONENT16_CHIRALITY_FORCED_DOUBLER_NO_GO_NOTE_2026-05-30.md`, a
  sibling review-loop proposal cited by name pending its landing on main);
  this note concerns the `P3` magnitude only.

## 6. Audit consequence

```yaml
claim: hierarchy_p3_alpha_lm_magnitude_structural_foreclosure_no_go
closure_proposal: no_go
foreclosed: promotion_of_u0^16_to_alpha_LM^16_to_determinant_or_rg_transport_theorem_on_delta0_substrate
mechanism: block_observables_carry_only_u0 + geometric_progression_is_power_law_fingerprint + delta_eq_0
tightens: [hierarchy_formula_honest_status_C2_to_structural, hierarchy_formula_honest_status_C3_residual_identified]
hierarchy_lane_status: not_closed
forbidden_imports_used: false
audit_status_authority: independent audit lane only
```

## 7. Runner

```bash
python3 scripts/frontier_hierarchy_p3_alpha_lm_magnitude_no_go.py
```

Expected summary:

```text
SCORECARD: PASS=12 FAIL=0
```

The runner certifies `(4 pi)^{-16} = 2.586e-18`, the `5.18x` typo and its
internal-consistency refutation, the exact geometric progression and the failed
equal-log-spacing test (`Delta_2/Delta_1 = u_0 != 1`), the absence of any
explicit `alpha_bare` in the block determinant and condensate-density forms, and
the `delta = 0` foreclosure of power-law running.

## 8. Key files

- [`scripts/frontier_hierarchy_p3_alpha_lm_magnitude_no_go.py`](../scripts/frontier_hierarchy_p3_alpha_lm_magnitude_no_go.py)
- [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
- [`HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md`](HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md)
- [`HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md`](HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md)
- [`HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md`](HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md)
- [`HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md`](HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md)

This note is a formal no-go and asserts no closure of the hierarchy lane.
