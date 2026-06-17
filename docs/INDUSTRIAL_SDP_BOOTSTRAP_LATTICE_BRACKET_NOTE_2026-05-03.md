# Industrial SDP Bootstrap — Lattice ⟨P⟩(β=6) Bracket Attempt

**Date:** 2026-05-03; 2026-06-13 exact obstruction certificate repair
**Type:** bounded no-upper-bound obstruction certificate + named open gate
**Claim type:** open_gate
**Claim scope:** apply the CVXPY-based SDP infrastructure validated in
block 01 (PR [#433](https://github.com/jonathonreilly/cl3-lattice-framework/pull/433))
to the actual lattice `⟨P⟩(β=6)` problem via multi-Wilson-loop moment
bootstrap. The auditable core is now the exact obstruction certificate:
the PSD + Hausdorff + 4x4 Gram + stated area-law inequalities admit an
explicit feasible point with `p1 = p2 = p3 = p4 = r1 = r2 = q1 = q2 =
pr = pq = rq = 1`. Therefore this SDP surface cannot prove any
nontrivial upper bound `p1 < 1`, even before numerical solver error is
considered. The optional `p1 >= 0.4225` mean-field lower bound is an
admitted comparison/input only, not derived by the SDP and not
load-bearing for the no-upper-bound obstruction. This consolidates the
named obstruction from prior PRs [#420](https://github.com/jonathonreilly/cl3-lattice-framework/pull/420),
[#423](https://github.com/jonathonreilly/cl3-lattice-framework/pull/423):
**loop equations are the critical missing piece** for any nontrivial
framework-native bracket.
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/frontier_industrial_sdp_bootstrap_block02.py`
**Run with:** `.venv/bin/python3 scripts/frontier_industrial_sdp_bootstrap_block02.py`

## 0. Question

Block 01 (PR [#433](https://github.com/jonathonreilly/cl3-lattice-framework/pull/433))
established the CVXPY infrastructure works on this framework. Can it
bracket the actual lattice `⟨P⟩(β=6) ≈ 0.5934` via multi-Wilson-loop
SDP at small L_max, even without explicit Migdal-Makeenko loop equations?

## 0.1 2026-06-13 repair summary

The prior source surface invited a conditional reading because the displayed
best bracket used the admitted `p1 >= 0.4225` bridge-support lower bound. This
repair separates the exact theorem from that admitted comparison:

- **Exact theorem:** on the encoded PSD/Hausdorff/Gram/area-law SDP surface,
  `p1 = 1` is feasible by an explicit all-ones moment certificate. Hence the
  surface has trivial upper optimum `max p1 = 1`; no nontrivial upper bound can
  be derived without additional loop-equation constraints or another strict
  framework-native relation.
- **Non-theorem context:** `0.4225`, `0.5934`, `0.59353`, and the
  Kazakov-Zheng literature brackets are comparison/admitted context only.
- **No status edit:** this source note does not set the audit verdict. The
  independent audit lane owns any reclassification.
- **Scope guard:** this is not an exhaustive no-go against SDP/bootstrap
  routes. Adding explicit loop equations or another strict framework-native
  relation changes the constraint surface and remains the intended open path.

## 1. Setup

The bootstrap problem (CVXPY 1.8.2 + CLARABEL):

**Variables (real-valued):**
- `p1, p2, p3, p4` = `⟨P^k⟩` for k=1..4 (plaquette moments)
- `r1, r2` = `⟨R⟩, ⟨R²⟩` (1×2 rectangle Wilson loop)
- `q1, q2` = `⟨Q⟩, ⟨Q²⟩` (2×2 plaquette / quadrupole)
- `pr, pq, rq` = cross-correlators

**Constraints:**
- 3x3 Hankel PSD on plaquette moments
- Hausdorff-shifted PSD for `[a, b] = [-1/3, 1]` support
- 4x4 Gram matrix on `{1, P, R, Q}` PSD (RP-derived per Lemma BB1 of PR [#420](https://github.com/jonathonreilly/cl3-lattice-framework/pull/420))
- Support bounds: `p1, r1, q1 ∈ [-1/3, 1]`; `p2, r2, q2, p4 ∈ [0, 1]`
- Hausdorff monotonicity: `p4 ≤ p2`
- Area-law / perimeter inequalities: `r1 ≤ p2`, `q1 ≤ p4`
- Optional bridge-support lower bound: `p1 ≥ 0.4225` (admitted comparison
  only: mean-field correlation-raising — single-plaquette is asserted as a
  lower bound for confined lattice gauge; this is not derived by this SDP)

## 2. Result

```text
Constraint set                                          min p1     max p1   width
─────────────────────────────────────────────────────  ────────  ────────  ──────
Pure PSD (no framework constraints)                    -0.3333    1.0000   1.3333
PSD + area-law                                         -0.3333    1.0000   1.3333
PSD + bridge-support lower bound (p1 ≥ 0.4225)          0.4225    1.0000   0.5775
PSD + bridge-support + area-law (full)                  0.4225    1.0000   0.5775
```

**Best numerical bracket with the admitted lower-bound switch enabled:
`⟨P⟩(β=6) ∈ [0.4225, 1.0]`** — width 0.578.

Contains MC value 0.5934 ✓; contains bridge-support upper bound 0.59353 ✓.
These comparator inclusions are not load-bearing theorem content.

## 3. Why the upper bound is trivial

The PSD + Hausdorff constraints alone are satisfiable by the
delta-distribution at `P = 1`, giving `p1 = p2 = p3 = p4 = 1`.
The stronger encoded SDP surface also admits an all-ones certificate:

```text
p1 = p2 = p3 = p4 = 1
r1 = r2 = q1 = q2 = 1
pr = pq = rq = 1
```

Then the plaquette Hankel matrix and the `{1,P,R,Q}` Gram matrix are
all-ones rank-one PSD matrices; the shifted Hausdorff upper matrix is
zero PSD; the shifted lower matrix is a positive all-ones matrix; support
bounds, `p4 <= p2`, `r1 <= p2`, and `q1 <= p4` are saturated. The
optional admitted lower bound `p1 >= 0.4225` is also satisfied. Thus the
feasible set itself contains `p1 = 1`, so no solver or finite precision
issue can produce a framework-native upper bound below 1 from these
constraints.

To get a non-trivial upper bound, we need either:
- **Explicit lattice Migdal-Makeenko / Schwinger-Dyson loop equations**
  relating moments to coupling β
- OR **explicit area-law constraints** with strict inequalities tied to β
- OR **multi-Wilson-loop relations** at higher L_max with industrial SDP
  (e.g., Kazakov-Zheng 2022 at L_max=16 with Mosek)

The lower bound `0.4225` comes only from the admitted "mean-field
correlation-raising" assumption (lattice MC ≥ single-plaquette mean-field
in confined regime), not from the bootstrap. It is not used to prove the
no-upper-bound obstruction.

## 4. Comparison with bridge-support stack and literature

| Approach | Bracket on `⟨P⟩(β=6)` | Width | Method |
|---|---|---|---|
| **This block 02 (CVXPY moment bootstrap)** | `[0.4225, 1.0]` | 0.578 | RP + Hankel + Hausdorff + 4x4 Gram + admitted area-law |
| Block 01 prior campaign analytical (PR [#420](https://github.com/jonathonreilly/cl3-lattice-framework/pull/420)) | `~0.35-0.48` (lower-bound estimate) | n/a | mixed-cumulant + strong-coupling LO |
| Bridge-support analytic upper-bound | `≤ 0.59353` (one-sided) | n/a | Perron-state reduction + 3D environment guess |
| Canonical lattice MC | `0.5934` (point) | 0 | full lattice MC |
| Kazakov-Zheng 2022 SU(∞) bracket near λ≈1.35 | `[0.59, 0.61]` | 0.02 | RP + Migdal-Makeenko + L_max=16 + SDP (Mosek) |
| Kazakov-Zheng 2024 SU(2) finite-N | 0.1% precision in physical range | 0.001 | same with finite-N adaptation |

**Honest assessment:** the CVXPY moment bootstrap from this block does
NOT provide a tighter bracket than the bridge-support stack's analytic
upper-bound candidate (0.59353). More sharply, the all-ones feasible
certificate proves that this encoded SDP surface cannot provide any
nontrivial upper-bound information at all.

## 5. Sharper named obstruction (consolidated, after CVXPY infrastructure validation)

```text
[BOOTSTRAP-LOOP-EQUATION OBSTRUCTION (CONSOLIDATED, with industrial SDP)]:
  Even with industrial CVXPY SDP infrastructure now available (block 01,
  PR #433), the lattice ⟨P⟩(β=6) bracket from PSD + Hausdorff + framework-
  specific positivity is essentially [admitted mean-field LB, 1.0]. The
  upper bound remains exactly trivial: an all-ones moment certificate is
  feasible. Without explicit Migdal-Makeenko loop equations, which were
  already identified as the critical missing piece in PRs #420 + #423,
  this SDP surface cannot prove p1 < 1.

  Tightening to industrial precision (~10⁻²) requires:
    (a) explicit Migdal-Makeenko / Schwinger-Dyson loop equations on
        framework's V-invariant minimal block (still not done — multi-month
        research project);
    (b) industrial SDP solver MOSEK at L_max ≥ 8-16 (CLARABEL/SCS
        precision insufficient; cvxpy infrastructure ready);
    (c) framework-specific positivity refinements from Cl(3) HS + V-invariance
        (block 02 of prior campaign showed this alone insufficient).

  Block 01 + 02 of THIS campaign (industrial-sdp-bootstrap-20260503)
  validate that the CVXPY infrastructure works and that, without loop
  equations, even industrial SDP cannot tighten the bracket below the
  bridge-support stack's analytic upper-bound candidate.
```

## 6. Honest status

```yaml
actual_current_surface_status: bounded no-upper-bound obstruction certificate + named open gate
target_claim_type: open_gate
conditional_surface_status: bounded by missing Migdal-Makeenko derivation
hypothetical_axiom_status: null
admitted_observation_status: bridge-support mean-field lower bound (0.4225) admitted as comparison/input only
claim_type_reason: |
  CVXPY infrastructure validated in block 01 (PR #433); applied here to
  the lattice problem with multi-Wilson-loop moment bootstrap. The exact
  all-ones feasible certificate proves the encoded SDP surface has
  trivial upper optimum p1 = 1. The admitted lower bound 0.4225 is not
  derived by the SDP. The consolidated named obstruction
  (Migdal-Makeenko loop equations missing) is sharper because we now know
  that even this industrial SDP surface cannot upper-bound the lattice
  plaquette without those equations.
audit_required_before_effective_retained: true
bare_retained_allowed: false
proposal_allowed: false
proposal_allowed_reason: |
  Exact no-upper-bound obstruction plus an honest negative bracket result.
  The CONSOLIDATED named obstruction (loop equations are critical) is the
  value, but no physical plaquette-value closure is claimed.
```

## 7. What this note closes

- Exact certificate that the encoded SDP surface admits `p1 = 1` and
  therefore cannot upper-bound `⟨P⟩(β=6)` below the trivial support endpoint
- First numerical CVXPY-based lattice bracket attempt on `⟨P⟩(β=6)` for
  this framework
- Confirms that PSD + Hausdorff + framework-specific positivity alone do
  not improve over the bridge-support stack analytic upper-bound
- Sharpens the consolidated named obstruction (Migdal-Makeenko loop
  equations critical, even with industrial SDP infrastructure)
- Validates that the CVXPY infrastructure (block 01, PR [#433](https://github.com/jonathonreilly/cl3-lattice-framework/pull/433))
  works on the lattice problem (problem solves to optimal status)

## 8. What this note does NOT close

- The lattice `⟨P⟩(β=6)` value (famous open lattice problem)
- A non-trivial upper bound or retained lower bound on `⟨P⟩(β=6)` from the
  bootstrap
- Migdal-Makeenko derivation on framework surface
- Industrial Kazakov-Zheng-precision (~10⁻²) brackets

## 9. Cross-references

- Block 01 of this campaign (CVXPY infrastructure): PR [#433](https://github.com/jonathonreilly/cl3-lattice-framework/pull/433)
- Infra unblocker: PR [#430](https://github.com/jonathonreilly/cl3-lattice-framework/pull/430) (cvxpy + venv)
- Verdict-named obstruction: [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
- Prior bootstrap analytical (small-truncation): PR [#420](https://github.com/jonathonreilly/cl3-lattice-framework/pull/420), PR [#423](https://github.com/jonathonreilly/cl3-lattice-framework/pull/423)
- Bridge-support analytic upper-bound: `GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md`
- Sister obstruction: [`GAUGE_VACUUM_PLAQUETTE_FRAMEWORK_POINT_UNDERDETERMINATION_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_FRAMEWORK_POINT_UNDERDETERMINATION_NOTE.md)
- Literature: Kazakov-Zheng [arXiv:2203.11360](https://arxiv.org/abs/2203.11360), [arXiv:2404.16925](https://arxiv.org/abs/2404.16925)

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [industrial_sdp_bootstrap_infrastructure_note_2026-05-03](INDUSTRIAL_SDP_BOOTSTRAP_INFRASTRUCTURE_NOTE_2026-05-03.md)
