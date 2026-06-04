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

## No-go discipline gate (N1-N8)

**Status:** PASS for the narrow magnitude-promotion no-go only. The claim being
closed is the single structural statement that the `(4 pi)^{-16}` coupling-power
magnitude in `P3` cannot be promoted from the algebraic relabeling `alpha_LM =
alpha_bare/u_0` to a block-determinant / condensate / RG-transport theorem **on
the `delta = 0` `Cl(3)/Z^3` substrate**. It is NOT a claim that `v` is
underivable, that the hierarchy lane is closed, or that no higher-`delta`
substrate could source the magnitude.

### N1 - Alternative route enumeration

Every candidate that would source the `(4 pi)^{-16}` magnitude from an object
the framework owns on the `delta = 0` substrate, and why each fails for this
scoped no-go.

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Block-determinant route | Source `alpha_bare^{16}` from the Matsubara block determinant `prod_w [m^2 + u_0^2 (3 + sin^2 w)]^4`. | The determinant factors contain **only** `u_0`; no explicit `alpha_bare` appears, so they cannot produce the `(4 pi)^{-16}` coupling power. | ATTEMPTED |
| Condensate / free-energy route | Source the magnitude from the condensate density `(m/L_t) sum_w 1/[m^2 + u_0^2 (3 + sin^2 w)]`. | Same form constraint: only `u_0` enters; the condensate is `alpha_bare`-free, so the coupling-power magnitude is not a condensate observable. | ATTEMPTED |
| RG-trajectory / geometric-mean route | Promote `alpha_bare -> alpha_LM -> alpha_s(v) = alpha_bare/u_0^2` to a one-loop RG trajectory and read `alpha_LM^{16}` off transport. | The three couplings form a constant-ratio geometric progression (`Delta_2/Delta_1 = u_0 != 1` for `1/alpha`); equal-log-spacing fails, so this is a power-law not a one-loop trajectory. | ATTEMPTED |
| KK power-law / dimensional-transmutation route | Treat the geometric progression as genuine power-law running `alpha(mu) ~ mu^{-kappa}`. | Power-law gauge running in 4D requires `delta > 0` compactified dimensions (Dienes-Dudas-Gherghetta KK tower); the substrate has `delta = 0`, so the trajectory does not exist on it. | ATTEMPTED |
| Single-link / fluctuation-measure route | Source the prefactor from a single-link or Gaussian-fluctuation measure on the cube. | Already pinned by the cross-cited exponent-side regulator no-go to continuum-Fourier-measure inheritance on the naive-staggered surface, not a block dynamical effect — it is the same imported admission, not a fresh source. | ATTEMPTED |
| Higher-`delta` substrate route | Build a `delta > 0` realization where the geometric progression IS an RG trajectory. | Not foreclosed — but it is a **different substrate** than the `delta = 0` `Cl(3)/Z^3` one the framework owns; left explicitly open in Section 5 as the surviving existence question. | OUT OF SCOPE (left open) |

### N2 - Wall-independence audit

The collapsed wall set for this no-go is a **single** wall: on the `delta = 0`
substrate the `(4 pi)^{-16}` magnitude is sourced by no block observable
(determinant / free-energy / condensate all carry only `u_0`), and the only
structure that supplies it — the constant-ratio geometric progression — is a
power-law-running fingerprint that `delta = 0` cannot realize. The two clauses
are not independent retained walls: they are the **same** obstruction read from
two sides (the magnitude is absent from the owned observables *because* it
lives in a power-law trajectory the substrate forbids). The complementary
exponent-side regulator no-go is a separate witness pointing at the same
prefactor, not an additional wall this proof stacks on. What could change the
verdict: a derivation exhibiting an explicit `alpha_bare` dependence inside a
block determinant / condensate on this substrate, or a `delta = 0`-compatible
mechanism that produces a constant multiplicative `1/alpha` ratio without a
compactified tower. Neither is supplied here, and neither is asserted impossible
in principle — only absent on the owned substrate.

### N3 - Hidden-wall scan

The words "structurally foreclosed", "permanently", "cannot", and "no-go" carry
no load as retained inputs; they are labels for the explicit argument. The
EXPLICIT load-bearing inputs are exactly four, all forms-and-values only (their
audit status is deferred to the independent lane per Section 1):

1. `alpha_bare = 1/(4 pi)` from the `g_bare = 1` rescaling convention
   (`g_bare_rigidity_theorem_note`).
2. Identity `(S)`: `alpha_LM^{16} = alpha_bare^{16} u_0^{-16}` (honest-status
   note, section `P3`) and the geometric-mean form `alpha_LM = sqrt(alpha_bare
   * alpha_s)`, `alpha_s(v) = alpha_bare/u_0^2`.
3. The block-determinant and condensate-density **forms** carrying only `u_0`
   (Matsubara determinant / decomposition notes).
4. The substrate fact `delta = 0` for `Cl(3)/Z^3`, plus the textbook
   Dienes-Dudas-Gherghetta statement that 4D power-law gauge running requires
   `delta > 0`.

No "RG-transport theorem", "dimensional transmutation", or "power-law running"
is invoked as a granted result; each is named only to be **denied** on this
substrate. The Dienes-Dudas-Gherghetta requirement is a textbook
implication used in the standard direction (power-law needs a tower), not a
retained framework claim smuggled in as a premise.

### N4 - Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md) section `P3` | The `u_0^{16} -> alpha_LM^{16}` substitution recorded as an algebraic relabeling whose magnitude is "not derived / non-perturbatively walled." | The same `P3` magnitude, tightened to "structurally foreclosed on `delta = 0`." | yes |
| [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md) route `C3` | Per-step Wilsonian taste-staircase transport leaving a residual `alpha_LM^{16}` factor out of scope (inheriting the YT UV-to-IR transport obstruction). | This note identifies that `C3` residual **as** the `(4 pi)^{-16}` coupling-power magnitude foreclosed here — same object. | yes |
| [`HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md`](HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md) | Pins the `(4 pi)^{-16}` prefactor to continuum-Fourier-measure inheritance on the naive-staggered surface (exponent / measure side). | The same `(4 pi)^{-16}` prefactor, attacked from the magnitude / transport side (not a determinant/condensate/fluctuation/transport effect). | yes (complementary) |
| [`HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md`](HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md) | (positive input) the exact block determinant `prod_w [m^2 + u_0^2 (3 + sin^2 w)]^4`. | Used as the owned block observable shown to carry only `u_0`. | yes (positive form, not an attacked residual) |
| [`HIERARCHY_ALPHA_LM_DIM_TRANS_REFRAMING_BOUNDED_NOTATION_EQUIVALENCE_NOTE_2026-05-16.md`](HIERARCHY_ALPHA_LM_DIM_TRANS_REFRAMING_BOUNDED_NOTATION_EQUIVALENCE_NOTE_2026-05-16.md) | Establishes the geometric-mean notation equivalence as a bounded relabeling. | Supplies the geometric-progression form whose constant ratio is the power-law fingerprint. | yes (form input) |
| [`HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md`](HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md) | Flags the `alpha_bare^{16}` inline-figure typo (`1.34e-17` vs `2.586e-18`). | Corrected here for the record only; **not load-bearing** — the structural argument uses `alpha_bare = 1/(4 pi)`, `(S)`, the progression, and `delta = 0`, none of which depend on the typo. | no (not load-bearing) |
| `HIERARCHY_EXPONENT16_CHIRALITY_FORCED_DOUBLER_NO_GO_NOTE_2026-05-30` (sibling, pending landing) | The exponent count `16` (`P2` question). | A **separate** primitive; this note concerns the `P3` magnitude only. | no (different primitive, not load-bearing) |

Non-matching witnesses (the typo-flag bridge note and the `P2` exponent sibling)
are explicitly marked **not load-bearing**: removing either leaves the no-go
intact.

### N5 - Rhetoric audit

Broad phrases are scoped as follows. "Structurally foreclosed" / "permanently a
relabeling" / "cannot be promoted" apply **only** to the upgrade of `P3`'s
`(4 pi)^{-16}` magnitude to a determinant/condensate/RG-transport theorem on the
`delta = 0` `Cl(3)/Z^3` substrate. "All four candidate derivation classes are
closed" means closed *on that substrate*, against the four named classes
(block-determinant, single-link/fluctuation-measure, RG-trajectory/geometric-mean,
KK dimensional-transmutation) — not against every conceivable future mechanism.
The note explicitly disclaims (Section 5) any reading that (a) the hierarchy lane
is closed, (b) `v` is rendered underivable, (c) the EXISTENCE of a higher-`delta`
substrate sourcing the magnitude is foreclosed, or (d) the exponent `16` (`P2`)
is adjudicated here. The geometric-mean identities and the determinant/condensate
forms remain valid as algebra; only their **promotion** to a magnitude-supplying
theorem is denied.

### N6 - Partial-closure path scan

Open non-axiom partial-closure paths that this note leaves intact (none is a new
axiom):

- A genuinely higher-`delta` realization of the substrate on which the
  geometric progression is a true power-law RG trajectory and the
  `(4 pi)^{-16}` magnitude becomes a transport consequence (Section 5's
  surviving existence question).
- An explicit-`alpha_bare` block observable: any future derivation exhibiting
  `alpha_bare` dependence **inside** a determinant or condensate on the
  `delta = 0` substrate would breach the single wall directly.
- A `delta = 0`-compatible non-KK mechanism producing a constant multiplicative
  `1/alpha` step (e.g. a discrete/holographic source) that is not power-law
  running in the Dienes-Dudas-Gherghetta sense.
- The `P2` exponent-count primitive, handled on its own sibling surface, which
  could close independently of this `P3` magnitude result.

Each path is an open research direction, not a granted axiom; none is asserted to
succeed, and none is asserted impossible in principle.

### N7 - Steelman

The strongest objection: dimensional transmutation routinely manufactures a
coupling-power magnitude like `(4 pi)^{-16}` from a *dimensionless* coupling
without any compactified extra dimension — the QCD scale `Lambda = mu
exp(-1/(b_0 alpha))` is the canonical example, and the framework's own
`alpha_s(v) = alpha_bare/u_0^2` looks like exactly such a running coupling. So
(the objection runs) the magnitude could be a standard 4D dimensional-transmutation
effect, requiring no `delta > 0`. Why it does not break the scoped claim: standard
4D transmutation produces **logarithmic** running — `1/alpha` linear in `ln mu`
(equal log spacing) — whereas the three couplings here sit at a constant
*multiplicative* ratio `1/u_0` in `alpha` itself (`Delta_2/Delta_1 = u_0 != 1` for
`1/alpha`). That is the power-law signature, and it is precisely the equal-log-spacing
test the runner shows **failing**. A log-running transmutation would give a
**different** (`u_0`-only, exponential-of-`1/alpha`) magnitude, not the geometric
`alpha_bare^{16}` power; so the steelman, if pursued, lands on a different number
and still does not source the relabeling's `(4 pi)^{-16}` from an owned `delta = 0`
observable. The objection rightly blocks the *broader* claim "no 4D coupling-power
magnitude is ever derivable"; this note makes no such claim.

### N8 - Cross-cycle echo

A recurring repo overclaim failure mode is to test a single representative object
(here, the four named candidate classes on one substrate) and then declare the
entire lane or a downstream prediction dead. This note avoids that echo by (a)
fixing the claim boundary at the `P3` *magnitude promotion* on the `delta = 0`
substrate only, (b) explicitly preserving the existence of higher-`delta`
substrates and the separate `P2` exponent question (Section 5), and (c) framing
the closure outcome as "B, formal no-go — tightens `P3` from non-perturbatively
walled to structurally foreclosed on this substrate," with `hierarchy_lane_status:
not_closed` recorded in the audit block (Section 6). The two `C2`/`C3` tightenings
(Section 3) are scoped to the honest-status note's own already-recorded candidate
routes, not extended into a lane-wide impossibility.

## 8. Key files

- [`scripts/frontier_hierarchy_p3_alpha_lm_magnitude_no_go.py`](../scripts/frontier_hierarchy_p3_alpha_lm_magnitude_no_go.py)
- [`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md`](HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md)
- [`HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md`](HIERARCHY_MATSUBARA_DECOMPOSITION_NOTE.md)
- [`HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md`](HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md)
- [`HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md`](HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md)
- [`HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md`](HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md)

This note is a formal no-go and asserts no closure of the hierarchy lane.
