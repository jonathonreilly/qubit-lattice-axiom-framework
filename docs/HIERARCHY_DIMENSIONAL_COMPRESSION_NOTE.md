# Hierarchy Dimensional Compression Note

**Status:** bounded_theorem (proposed; audit lane ratifies)
**Status authority:** independent audit lane only; effective status is
pipeline-derived from the audit ledger. The status line above is the
source-note proposal and is not an audit-ratified retained status.
**Date:** 2026-04-13 (created); 2026-05-16 (rescoped to retire the
observation-comparison load-bearing step flagged by the 2026-05-05 audit).
**Script:** `scripts/frontier_hierarchy_dimensional_compression.py`

## 0. Audit context — what this note still claims, and what it does not

The 2026-05-05 audit pass returned `audited_numerical_match` with the
verdict that the load-bearing within-scope content of the prior revision
was a numerical-closeness comparison against an imported observed
prefactor `C_obs = v_obs / v_pred`, not a derivation. That comparison
was rescoped to a non-load-bearing diagnostic-context line in this
2026-05-16 revision. The runner's PASS gates were rebuilt so that NO
PASS condition depends on `C_obs`, `v_obs`, or any external observed
target. The new load-bearing content is purely the dimensional
arithmetic on the framework-internal staggered Dirac condensate-density
ratio plus the structural D=4 dimensional-analysis identity already
derived in the 2026-05-10 sister bounded theorem note
`HIERARCHY_HEAT_KERNEL_D4_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-05-10.md`.

The `C_obs` value is still printed by the runner for reader
transparency but is explicitly marked as external-context output and is
not used in any PASS condition.

## 1. Within-scope claim (this note)

> **Claim (dimensional-compression arithmetic).** Let `R` denote the
> framework-internal staggered Dirac condensate-density ratio
>
> ```text
> R  =  cond(L_t = 10, L_s = 2, u_0 = 0.9, m = 1e-2)
>       /  cond(L_t = 2,  L_s = 2, u_0 = 0.9, m = 1e-2)
> ```
>
> on the operator built in `scripts/frontier_hierarchy_dimensional_compression.py`.
> Then:
>
> (i) **D=4 compression formula.** Under the per-determinant
>     geometric-mean readout `v ∝ |det|^(1/(N_taste · L_t))` with
>     `N_taste = 2^D = 16` in `D = 4` (the admission inherited from
>     the 2026-05-10 heat-kernel sister bounded theorem note), the
>     dimensional reading of the residual produces a compression
>     factor `R^(-1/D) = R^(-1/4)`.
> (ii) **D=16 alternative.** A naive direct scale reading with the
>     `(1/16)`-th root would give `R^(-1/16)`.
> (iii) **Order-of-magnitude separation.** The two compression
>     candidates differ in inverse shift by an algebraic factor that
>     is bounded away from numerical degeneracy:
>     `R^(-1/4) / R^(-1/16)` deviates from unity by more than 2%, so
>     `R^(-1/4)` and `R^(-1/16)` are NOT a single observable choice
>     dressed as two — they are quantitatively distinct
>     compression candidates that any audit-ratable VEV-readout
>     theorem would have to pick between by structural means.
> (iv) **D=4 vs general D structural identity.** The (1/4) exponent
>     decomposes as `1/D = 4 / 2^D` at `D = 4`, which is an
>     algebraic identity tied to the staggered taste count
>     `N_taste = 2^D`; the same identity fails at `D ∈ {1, 2, 3, 5,
>     6, 8}` (verified explicitly in the runner). The (1/4) is
>     therefore D=4-specific under the inherited per-determinant
>     readout, not an interchangeable choice.

The (1/4) derivation itself is the heat-kernel D=4 sister bounded
theorem note (2026-05-10); this note inherits that derivation and
records the consequent intra-framework arithmetic on the staggered
Dirac condensate-density residual.

## 2. What this note does NOT claim

- **Not a determinant-to-VEV theorem.** The closed retained derivation
  of the physical EW VEV `v` from the framework primitive stack remains
  open (the broader hierarchy chain `v_UV = M_Pl × α_LM^16 × (7/8)^(1/4)`
  is asserted elsewhere with its own open admissions).
- **Not a derivation of the order parameter.** The identification of
  the physical order parameter as a dimension-4 effective-potential
  density is the admission inherited from the 2026-05-10 heat-kernel
  sister note; this note does not re-derive it.
- **Not an observation-comparison closure.** The `C_obs = v_obs / v_pred`
  ratio is printed as context only. The within-scope load-bearing
  content is intra-framework dimensional arithmetic, not any claim
  that `R^(-1/4)` matches `C_obs`.
- **Not a sign / placement theorem.** The exact sign and placement of
  the (1/4) compression in the full physical formula remain open;
  see Section 5 below.
- **Not a retained-grade status proposal.** This is a bounded source
  note proposal; the independent audit lane ratifies status.

## 3. Numerical inputs (intra-framework only)

All inputs are computed inside the runner from the registered staggered
Dirac operator and from algebraic identities. None are observed values.

- condensate-density ratio
  `R = cond(L_t=10) / cond(L_t=2) ≈ 1.15469`
- D=4 inverse compression
  `R^(-1/4) ≈ 0.96468`
- D=16 inverse compression
  `R^(-1/16) ≈ 0.99105`
- D=4 vs D=16 fractional separation
  `R^(-1/4) / R^(-1/16) ≈ 0.97339` (i.e. ~2.7% gap)
- structural identity check `1/D = 4 / 2^D` at `D = 4`
  `1/4 = 4/16` — holds; same identity fails at all other D ∈ {1,2,3,5,6,8}

## 4. External context (NOT load-bearing)

The runner additionally prints, for reader transparency only:

- the broader-hierarchy pre-selector prediction
  `v_pred = M_Pl × α_LM^16 ≈ 254.64 GeV`
- the observed EW scale
  `v_obs = 246.22 GeV`
- the residual prefactor needed to match observation
  `C_obs = v_obs / v_pred ≈ 0.96692`
- the resulting distance `|R^(-1/4) − C_obs| ≈ 0.0022`

This block is labeled `external context` in the runner output and is
explicitly excluded from PASS conditions. It is preserved so the reader
can see why the dimensional-compression direction is of physical
interest, without that interest becoming a load-bearing audit input.

## 5. What is still open (re-audit targets)

The closure of these items would lift the broader hierarchy chain from
bounded-support to retained-grade; none are claimed in this note.

1. **Effective-potential-density bridge.** A retained derivation
   showing how the `L_t > 2` block normalization enters the physical
   VEV formula with explicit sign and placement (the parent narrow
   theorem
   `HIERARCHY_MATSUBARA_DETERMINANT_RATIO_NARROW_THEOREM_NOTE_2026-05-10.md`
   names this as its single remaining named admission).
2. **Per-determinant readout admission.** The
   `v ∝ |det|^(1/(N_taste · L_t))` reading is recast as a D=4
   dimensional-analysis statement by the 2026-05-10 heat-kernel sister
   note but is not derived from primitives there.
3. **Staggered-Dirac realization gate.** The `N_taste = 2^D` count
   in `D = 4` inherits from the open realization-gate note
   [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md).
4. **Continuum-limit corrections.** Sub-leading Seeley-DeWitt
   coefficients modify the (7/8) prefactor at sub-leading orders in a
   continuum-limit reading; at the minimal block the (1/4) is bounded
   D=4-consistent.

## 6. Dependencies

- `HIERARCHY_HEAT_KERNEL_D4_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-05-10.md`
  — sister bounded theorem note deriving the D=4 (1/4) compression
  exponent via heat-kernel + zeta-regularized free-energy density
  reading; provides the (1/4) used here as a structural admission.
- `HIERARCHY_MATSUBARA_DETERMINANT_RATIO_NARROW_THEOREM_NOTE_2026-05-10.md`
  — sister narrow theorem deriving the (7/8) factor as an exact
  rational determinant identity.
- `HIERARCHY_DIMENSIONAL_COMPRESSION_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md`
  — companion narrowing note from 2026-05-10 isolating prior
  within-scope arithmetic from the open effective-potential-density
  bridge.
- `HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md`
  — sibling endpoint algebra note.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
  — open realization gate for `N_taste = 2^D` structural origin.

## 7. Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_dimensional_compression.py
```

Verifies, using only intra-framework arithmetic, that:

1. The D=4 inverse compression `R^(-1/4)` agrees with the explicit
   `1/4` power computed two independent ways (`R**(-1/4)` and
   `math.exp(-math.log(R)/4)`).
2. The D=4 and D=16 candidates are numerically distinct (their ratio
   deviates from unity by > 2%), so the two compression readings are
   not a single observable hidden as two.
3. The structural identity `1/D = 4 / 2^D` holds at `D = 4` and FAILS
   at all of `D ∈ {1, 2, 3, 5, 6, 8}` (so the (1/4) reading is
   D=4-specific under the inherited per-determinant readout, not an
   interchangeable choice).
4. The runner does NOT depend on the imported `v_obs`, `v_pred`, or
   `C_obs` in any PASS condition. Those quantities are printed as
   `external context` for reader transparency and are explicitly
   excluded from PASS gates.

Expected scorecard: `4 pass, 0 fail out of 4`.

```yaml
claim_id: hierarchy_dimensional_compression_note
note_path: docs/HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md
runner_path: scripts/frontier_hierarchy_dimensional_compression.py
proposed_claim_type: bounded_theorem
proposed_load_bearing_step_class: B
status_authority: independent audit lane only
audit_required_before_effective_status_change: true

declared_one_hop_deps:
  - hierarchy_heat_kernel_d4_compression_bounded_theorem_note_2026-05-10
  - hierarchy_matsubara_determinant_ratio_narrow_theorem_note_2026-05-10
  - hierarchy_dimensional_compression_audited_scope_narrow_bounded_note_2026-05-10
  - hierarchy_effective_potential_endpoint_note
  - staggered_dirac_realization_gate_note_2026-05-03

admitted_context_inputs:
  - per-determinant geometric-mean readout
    v(L_t) ∝ |det(D, L_t, m=0)|^(1/(N_taste · L_t)) with
    N_taste = 2^D = 16 in D = 4 (inherited from 2026-05-10
    heat-kernel sister bounded theorem note)
  - staggered taste count N_taste = 2^D in D = 4 (inherits from
    open realization gate)

forbidden_imports_used: false
observed_target_used_in_pass_conditions: false
proposal_allowed: true
```
