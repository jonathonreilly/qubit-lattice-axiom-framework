# Industrial SDP Bootstrap — Infrastructure + SU(2)/SU(3) Single-Plaquette Validation

**Date:** 2026-05-03 (original); 2026-05-28 (SU(2) full-class-angle Haar fix).
**Type:** bounded_theorem

## 2026-05-28 Audit Repair (SU(2) full class-angle Haar reference)

The 2026-05-28 audit verdict was `audited_failed`:

> *"the SU(2) reference surface is not the stated full SU(2) Haar/Bessel
> single-plaquette integral. The runner integrates theta in [0, pi] with
> P=cos(theta/2), restricting to P>=0; the full SU(2) class-angle integral
> gives I2(6)/I1(6)=0.76272608, not 0.76736480."*

Fixed. The SU(2) conjugacy classes are parametrized by an eigenvalue angle
`alpha in [0, pi]` (eigenvalues `e^{±i·alpha}`), with `P = (1/2) tr U =
cos(alpha) in [-1, +1]` and class measure `(2/pi) sin^2(alpha) dalpha`. The
prior runner integrated `theta in [0, pi]` with `P = cos(theta/2)`, i.e.
`theta/2 in [0, pi/2]`, which silently truncated the domain to `P >= 0`.
The runner now integrates the **full class-angle domain** and a self-check
asserts `<P> = I_2(beta)/I_1(beta)`. At `beta=6` this gives the correct
`<P> = 0.76272608` (was `0.76736480`); see corrected table below.

Two additional repair details:

- The runner's `cvxpy` import is now optional. The scipy-only
  single-plaquette REFERENCE section (the load-bearing audit-repair
  content) runs and is cacheable without the SDP solver env; the CVXPY
  containment certificate is reported as SKIPPED when `cvxpy` is absent.
- The CVXPY containment certificate was **regenerated in the SDP venv**
  (cvxpy 1.9.1 + CLARABEL/SCS) with the corrected SU(2) `m_2, m_3, m_4`.
  The re-solved SU(2) fixed-moment bracket is `m_1 ∈ [0.679959, 0.766941]`
  (was `[0.684871, 0.769227]` with the old truncated moments) and it
  contains the corrected reference `m_1 = 0.76272608`. All 14 CVXPY
  containment assertions pass (PASS=14 / FAIL=0). The SHA-pinned cache
  reflects this full CVXPY run.

**Type:** infrastructure + validation support theorem
**Claim scope:** establish a working CVXPY-based moment-problem SDP
infrastructure for lattice gauge bootstrap on this framework, validated by
support-aware bracket containment of SU(2) and SU(3) single-plaquette
reference data via Bessel functions and numerical Haar integration on the
Cartan torus. The infrastructure is
unblocked by infra PR
[#430](https://github.com/jonathonreilly/cl3-lattice-framework/pull/430)
which added cvxpy 1.8.2 + open-source SDP solvers via venv. The
infrastructure provides the foundation for actual lattice bracketing of
`⟨P⟩(β=6)` (block 02 of this campaign).
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/frontier_industrial_sdp_bootstrap_block01.py`
**Run with:** `.venv/bin/python3 scripts/frontier_industrial_sdp_bootstrap_block01.py`

## 0. Question

Can CVXPY (now installed via venv per PR #430) actually produce useful
SDP-based brackets on plaquette moments for SU(N) lattice gauge theory?
Validation requires checking that CVXPY brackets contain known reference
values (single-plaquette via Bessel for SU(2), Haar integration for SU(3)).

## 1. Setup

CVXPY 1.8.2 + open-source solvers (CLARABEL, SCS, HIGHS, OSQP, SCIPY).
No commercial Mosek (industrial Kazakov-Zheng-class precision out of
reach without it).

Three primitives implemented:

| # | Primitive | Description |
|---|---|---|
| BS1 | SU(2) single-plaquette moments via Bessel + numerical Haar | `⟨((1/2) tr U)^k⟩_single` for k ∈ {0,1,2,3,4} from numerical integration of `∫dα sin²(α) cos^k(α) exp(β cos α) dα` over the **full class-angle domain** α ∈ [0, π] (P = cos α ∈ [−1,1]); self-checked against `⟨P⟩ = I_2(β)/I_1(β)` |
| BS2 | SU(3) single-plaquette moments via Cartan-torus Haar integration | `⟨((1/3) Re tr U)^k⟩_single` from 2D grid integration over Weyl chamber with Vandermonde measure |
| BS3 | CVXPY moment-problem bootstrap | Hankel-PSD + Hausdorff-shifted-PSD on `[a, b]`-supported moment sequences; max/min `m_1 = ⟨P⟩` subject to PSD constraints; supports fixing higher moments to known reference values |

## 2. Validation results

At `β = 6`:

### SU(2) single-plaquette (Bessel/Haar reference)

```text
⟨P^0⟩_SU(2)_single = 1.00000000  (normalization)
⟨P^1⟩_SU(2)_single = 0.76272608  (= I_2(β)/I_1(β) exactly, full class-angle domain)
⟨P^2⟩_SU(2)_single = 0.61863696
⟨P^3⟩_SU(2)_single = 0.51696810
⟨P^4⟩_SU(2)_single = 0.44207224
```

(2026-05-28: corrected from the prior `P >= 0`-truncated values
`0.76736480 / 0.62153293 / 0.51967618 / 0.44425771`. The `⟨P^1⟩` value
now equals `I_2(6)/I_1(6) = 0.76272608` exactly, as the runner asserts.)

CVXPY bracket with `m_2, m_3, m_4` fixed to reference, `m_1` free
(regenerated 2026-05-28 in the SDP venv with the corrected moments):
`m_1 ∈ [0.679959, 0.766941]` — contains the corrected reference
`0.76272608`. Containment holds and is not endpoint recovery
(`|0.679959 − 0.7627| > 1e-3` and `|0.766941 − 0.7627| > 1e-3`). All 14
CVXPY containment assertions pass.

### SU(3) single-plaquette (Haar reference, 80×80 grid)

```text
⟨P^0⟩_SU(3)_single = 1.00000000
⟨P^1⟩_SU(3)_single = 0.42253174
⟨P^2⟩_SU(3)_single = 0.24341355
⟨P^3⟩_SU(3)_single = 0.14974607
⟨P^4⟩_SU(3)_single = 0.09939457
```

CVXPY bracket: `m_1 ∈ [0.281915, 0.451550]` — width 0.170, contains
reference 0.4225.

### Pure PSD bracket (no fixed moments)

For SU(N) with `P ∈ [a, b]` support but no other constraints:
- SU(2) (`P ∈ [-1, 1]`): `m_1 ∈ [-1.00, 1.00]` — trivial (full support)
- SU(3) (`P ∈ [-1/3, 1]`): `m_1 ∈ [-0.333, 1.000]` — trivial (full support)

PSD + Hausdorff alone gives only the support endpoints. **Loop equations
or higher-moment constraints are required for non-trivial brackets.**

## 3. Connection to lattice ⟨P⟩(β=6)

The single-plaquette reference values are:
- SU(2)_single ≈ 0.767 (vs lattice MC ≈ 0.770 at the SU(2) Wilson convention)
- SU(3)_single ≈ 0.422 (vs lattice MC = **0.5934** at the framework's β=6)

The SU(3) single-plaquette gap to lattice MC (~30% relative) reflects the
**mean-field deficiency**: in lattice gauge theory, plaquettes share
links and the correlations among plaquettes raise `⟨P⟩` substantially
above the single-plaquette mean-field value.

**Block 02 of this campaign** will attempt to bracket the FULL LATTICE
`⟨P⟩(β=6)` using:
- CVXPY moment bootstrap on a multi-Wilson-loop set
- Loop equations (Schwinger-Dyson on framework's V-invariant minimal block) or
- Framework's mixed-cumulant audit (`P_full(β) = P_1plaq(β) + β^5/472392 + O(β^6)`) as
  a soft constraint

## 4. What this note closes

- **CVXPY-based SDP infrastructure** for moment-problem bootstrap is
  validated and working on this framework.
- SU(2) and SU(3) single-plaquette references computed analytically/numerically.
- CVXPY brackets contain known reference values when higher moments are fixed.
- Pure PSD brackets without loop equations are demonstrated to be trivial
  (just support endpoints).

## 5. What this note does NOT close

- Lattice ⟨P⟩(β=6) bracket (deferred to block 02).
- Industrial-precision (Kazakov-Zheng 2022 ~10⁻²) brackets (require Mosek
  + ~3-month engineering; out of scope of this 12h campaign).
- Loop-equation derivation on framework's V-invariant minimal block (deferred).

## 6. Honest status

```yaml
actual_current_surface_status: infrastructure validation support theorem
target_claim_type: positive_theorem (infrastructure works)
conditional_surface_status: bounded by the open lattice ⟨P⟩(β=6) target
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  This is an infrastructure/methodology cycle: it establishes that
  CVXPY-based SDP moment-bootstrap is functional and correctly contains
  reference values when higher moments are constrained. It does NOT
  bracket the lattice ⟨P⟩(β=6) target on its own; that requires loop
  equations (block 02).
audit_required_before_effective_retained: true
bare_retained_allowed: false
proposal_allowed: false
proposal_allowed_reason: |
  Infrastructure validation cycle. The retained-positive value comes
  in block 02 where the infrastructure is applied to the actual lattice
  target.
```

## 7. Comparators (admitted-context only)

- Canonical lattice MC SU(3) `⟨P⟩(β=6)` = **0.5934**
  (`PLAQUETTE_SELF_CONSISTENCY_NOTE`)
- Bridge-support analytic upper-bound candidate = **0.59353**
- SU(2) lattice MC at β=6 ≈ 0.7706 (Creutz 1980)
- Kazakov-Zheng 2022 SU(∞) bracket near λ≈1.35: `[0.59, 0.61]` at L_max=16
  ([arXiv:2203.11360](https://arxiv.org/abs/2203.11360))
- Kazakov-Zheng 2024 SU(2) finite-N: 0.1% precision in physical range
  ([arXiv:2404.16925](https://arxiv.org/abs/2404.16925))

## 8. Cross-references

- Infra unblocker: PR [#430](https://github.com/jonathonreilly/cl3-lattice-framework/pull/430) (cvxpy + venv setup)
- Verdict-named obstruction: [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
- Prior bootstrap framework integration (analytical small-truncation): PR [#420](https://github.com/jonathonreilly/cl3-lattice-framework/pull/420), PR [#423](https://github.com/jonathonreilly/cl3-lattice-framework/pull/423)
- Block 02 (planned, this campaign): apply CVXPY to lattice ⟨P⟩(β=6)
- Loop pack: `.claude/science/physics-loops/industrial-sdp-bootstrap-20260503/`
