# Hierarchy Dimensional Compression Note

**Type:** open_gate / conditional-support
**Claim type:** open_gate / conditional D=4 arithmetic support
**Status:** conditional D=4 arithmetic support (source proposal; audit lane ratifies effective status)
**Status authority:** independent audit lane only; effective status is
pipeline-derived from the audit ledger. The status line above is the
source-note proposal and is not an audit-ratified retained or bounded-theorem
status.
**Date:** 2026-04-13 (created); 2026-05-16 (rescoped to retire the
observation-comparison load-bearing step flagged by the 2026-05-05 audit).
**Script:** `scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py`

## 2026-06-12 audit firewall: D=4 readout bridge still open

The current source claim is conditional support for D=4 arithmetic only. The
runner checks the framework-internal condensate-density ratio, the D=4 versus
D=16 separation, and the algebraic identity `1/D = 4/2^D` at `D = 4`.

This note does not derive the D=4 readout / effective-potential-density bridge
that would place the compression factor in the physical VEV formula with
sign, placement, and normalization. The old source edge to the unaudited
staggered-realization gate is no longer load-bearing here: the D=4 taste-count
input is now routed through retained bounded taste-count authorities named
below. No new axiom, Tier-A admission, observed target, or audit status is
introduced here.

## 2026-06-15 source-side bridge candidate

The bounded bridge note
[`HIERARCHY_D4_EFFECTIVE_POTENTIAL_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-15.md`](HIERARCHY_D4_EFFECTIVE_POTENTIAL_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-15.md)
proves the finite D=4 effective-potential-density readout map under the
explicit premise `rho_* = A(L_t) v(L_t)^4`. That source bridge fixes:

- exponent: the readout is a fourth root because `rho_*` is a D=4 density and
  `v` has mass dimension one;
- placement: `v_b/v_a = (A_a/A_b)^(1/4)`, so larger effective-potential
  coefficient means smaller readout scale;
- sign: since `A_4 > A_2`, the `L_t=4` endpoint compresses downward;
- normalization: the common `u_0` factor cancels exactly, giving
  `(7/8)^(1/4)` for `L_t=4` versus `L_t=2` and `(3/4)^(1/8)` for
  `L_t -> infinity` versus `L_t=2`.

This bridge does not promote the row or close the full hierarchy theorem.
Independent review/audit must decide whether the bounded premise is accepted as
the physical electroweak insertion map.

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
> on the operator built in
> `scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py`.
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
>     algebraic identity tied to the retained bounded D=4 taste-count
>     surface `N_taste = 2^D`; the same identity fails at
>     `D ∈ {1, 2, 3, 5, 6, 8}` (verified explicitly in the runner).
>     The (1/4) is therefore D=4-specific under the inherited
>     per-determinant readout, not an interchangeable choice.

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
- **Not a retained- or bounded-theorem status proposal.** This is conditional
  D=4 arithmetic support; the independent audit lane ratifies effective
  status.

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
   The 2026-06-15 bounded bridge candidate above supplies the finite
   source-side readout map and fixes the algebraic sign, placement, exponent,
   and normalization under its explicit D=4 density premise. It is not an
   audit-ratified retained derivation of the physical electroweak insertion map.
2. **Per-determinant readout admission.** The
   `v ∝ |det|^(1/(N_taste · L_t))` reading is recast as a D=4
   dimensional-analysis statement by the 2026-05-10 heat-kernel sister
   note but is not derived from primitives there.
3. **Taste-count authority.** The old open realization-gate pointer is
   replaced, for this packet's D=4 arithmetic support, by retained bounded
   one-hop authorities:
   [`HIGGS_LATTICE_TASTE_COUNT_AND_WJ_FORM_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](HIGGS_LATTICE_TASTE_COUNT_AND_WJ_FORM_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
   for the naive `N_taste = 2^D = 16` count and mean-field `W(J)` form, and
   [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md)
   for the `2^4 = 16` BZ-corner/Hamming-staircase combinatorics. The
   `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` remains only a
   broader physical-realization context pointer, not this note's
   load-bearing taste-count dependency.
4. **Continuum-limit corrections.** Sub-leading Seeley-DeWitt
   coefficients modify the (7/8) prefactor at sub-leading orders in a
   continuum-limit reading; at the minimal block the (1/4) is bounded
   D=4-consistent.

### 5.1 D=4 readout / effective-potential-density bridge check (2026-06-11)

The load-bearing readout used by this note is the parent claim's
`v ∝ |det|^(1/(N_taste · L_t))` with `N_taste = 2^D = 16` in `D = 4`.
The bridge it would need is the Section 5 item 1 target above: a retained
derivation showing how the `L_t > 2` block normalization enters the
physical VEV formula with explicit sign and placement.

Current retained-row check: no retained row checked in this repair
supplies that exact bridge at this scope.
`HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md` is retained-bounded
for endpoint coefficient algebra, but its audited scope excludes the
physical electroweak insertion map and its source text leaves Bridge 2
as the dimension-4 insertion theorem.
`SCALAR_3PLUS1_TEMPORAL_RATIO_NOTE.md` is retained for the scalar
endpoint ratio `A_inf/A_2 = 2/sqrt(3)`, but its audited scope excludes
observable-level dimension-4 insertion.
`HIGGS_MASS_FROM_AXIOM_NOTE.md` supplies a retained-bounded per-color
determinant to `V_taste` symmetric-point curvature theorem, but it
declares the EW VEV scale as boundary input B2 and D1 as a diagnostic
definition; it does not derive this note's per-determinant `v(L_t)`
readout or the `L_t` sign/placement bridge. The heat-kernel and
Matsubara-ratio notes still name the D=4 readout as an admission in
their own current text and are unaudited in the current ledger.

Future bridge note proof obligation: derive, from retained framework
inputs, the map from the per-determinant or effective-potential-density
coefficient on the `L_t > 2` block to the physical VEV readout,
including the exponent, inverse/direct placement, sign, and
normalization relative to the `L_t = 2` baseline.

## Registered Tier-A routing (2026-06-11; audit-requested repair)

The 2026-06-11 audit repair target routes the carrier admission into
the registered Tier-A derivation target rather than treating it as an
unregistered conditional blocker.

1. **The algebra is standalone.** The load-bearing computations of this
   note close as arithmetic on the computed condensate-density ratio:
   `R` maps to `R^(-1/4)` and `R^(-1/16)`, the two candidates are
   separated, and the identity `1/D = 4/2^D` holds at `D = 4` and fails
   at the tested neighboring dimensions. This standalone arithmetic
   does not consume carrier naming.
2. **What the remaining admission carries.** The carrier-consuming part
   still open here is the per-determinant readout naming the arithmetic as a
   VEV or effective-potential-density readout. The `N_taste = 2^D = 16` D=4
   count is no longer admitted through the open realization gate in this
   packet; it is consumed from the retained bounded taste-count authorities
   cited above, while the physical realization of the full carrier remains
   outside this note.
3. **The remaining Tier-A target is context only.** The canonical
   `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` remains the
   registered Tier-A derivation target `AC_phi_lambda` in
   `docs/audit/data/tier_a_admissions.json`, but this note no longer uses it
   as the D=4 taste-count authority. The unresolved target here is the
   determinant/effective-potential-density readout map, not the finite
   `2^4 = 16` count.
4. **Routing boundary.** This section records the carrier route only.
   It does not supply the per-determinant readout bridge, does not
   assert full physical-carrier realization, and does not assert an audit
   outcome.

## 6. Graph-visible retained dependencies and context pointers

Graph-visible retained one-hop dependencies for the taste-count repair:

- [`HIGGS_LATTICE_TASTE_COUNT_AND_WJ_FORM_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](HIGGS_LATTICE_TASTE_COUNT_AND_WJ_FORM_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — retained bounded D=4 `N_taste = 2^D = 16` and mean-field `W(J)` bridge.
- [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md)
  — retained bounded `2^4 = 16` BZ-corner/Hamming-staircase combinatorics.

Non-load-bearing context pointers, intentionally left as backticked plain
text rather than graph-visible dependency edges:

- `HIERARCHY_HEAT_KERNEL_D4_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-05-10.md`
  — sister note that motivated the D=4 (1/4) compression exponent, but is
  unaudited in the current ledger and is not a closure authority here.
- `HIERARCHY_MATSUBARA_DETERMINANT_RATIO_NARROW_THEOREM_NOTE_2026-05-10.md`
  — sister determinant-ratio note whose D=4 readout remains an admission.
- `HIERARCHY_DIMENSIONAL_COMPRESSION_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10.md`
  — prior narrowing note isolating arithmetic from the open
  effective-potential-density bridge.
- `HIERARCHY_EFFECTIVE_POTENTIAL_ENDPOINT_NOTE.md`
  — sibling endpoint algebra note; not a physical VEV insertion bridge.

Source-side bridge candidate for independent review:

- [`HIERARCHY_D4_EFFECTIVE_POTENTIAL_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-15.md`](HIERARCHY_D4_EFFECTIVE_POTENTIAL_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-15.md)
  — source-side bounded bridge fixing the D=4 readout map's exponent, sign,
  placement, and normalization under an explicit effective-potential-density
  premise; independent audit owns any status movement.

## 7. Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py
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
   `C_obs` in any load-bearing arithmetic gate.
5. The explicit import-hygiene PASS gate records that `v_obs`,
   `v_pred`, and `C_obs` are introduced only after the PASS-gate block.
   Those quantities are printed as `external context` for reader
   transparency and are explicitly excluded from PASS gates.
6. The source firewall records the packet as conditional D=4 arithmetic
   support, not a bounded-theorem status proposal.
7. The source firewall leaves the D=4 readout / effective-potential-density
   bridge open while consuming retained bounded taste-count authorities.
8. The live ledger reports the two taste-count one-hop authorities as
   retained-grade.

Expected scorecard: `8 pass, 0 fail out of 8`.

### 7.1 Scorecard sync (2026-06-15)

The current runner has eight PASS gates after the taste-authority repair.
Gate-by-gate check against
`scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py`:

1. `D=4 inverse compression R^(-1/4) reproduces by independent routes`
   — current runner computes `R**(-0.25)` and `exp(-log(R)/4)` and
   checks agreement to `1e-12`.
2. `D=4 and D=16 inverse compressions differ by more than 2%` —
   current runner computes `abs(R^(-1/4)/R^(-1/16) - 1) > 0.02`.
3. `Structural identity 1/D = 4 / 2^D holds at D = 4` — current runner
   checks `1/4 = 4/2^4`.
4. `Structural identity FAILS at D in {1,2,3,5,6,8}` — current runner
   checks each listed dimension separately.
5. `PASS conditions are free of observed-target imports` — this gate
   checks that `v_obs`, `v_pred`, and `C_obs` are introduced only after
   all PASS gates, in the external-context block.
6. `source note demotes stale bounded-theorem proposal to conditional support`
   — current source metadata no longer proposes a bounded theorem.
7. `source note leaves D=4 readout bridge open while consuming retained
   taste-count authority` — the note names the effective-potential-density
   bridge as open and records the retained bounded taste-count authorities.
8. `taste-count one-hop authorities are retained-grade in the live ledger` —
   the runner checks the effective statuses of the Higgs lattice taste-count
   bridge and the Wilson BZ-corner staircase row.

```yaml
claim_id: hierarchy_dimensional_compression_note
note_path: docs/HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md
runner_path: scripts/frontier_hierarchy_dimensional_compression_taste_authority_2026_06_15.py
proposed_claim_type: open_gate / conditional-support
proposed_load_bearing_step_class: B
status_authority: independent audit lane only
audit_required_before_effective_status_change: true

graph_visible_one_hop_deps:
  - higgs_lattice_taste_count_and_wj_form_bridge_narrow_theorem_note_2026-06-05
  - wilson_bz_corner_hamming_staircase_bounded_note_2026-05-08
context_pointers_not_dependency_edges:
  - hierarchy_heat_kernel_d4_compression_bounded_theorem_note_2026-05-10
  - hierarchy_matsubara_determinant_ratio_narrow_theorem_note_2026-05-10
  - hierarchy_dimensional_compression_audited_scope_narrow_bounded_note_2026-05-10
  - hierarchy_effective_potential_endpoint_note
source_side_bridge_candidates:
  - hierarchy_d4_effective_potential_readout_bridge_bounded_theorem_note_2026-06-15

admitted_context_inputs:
  - per-determinant geometric-mean readout
    v(L_t) ∝ |det(D, L_t, m=0)|^(1/(N_taste · L_t)) with
    N_taste = 2^D = 16 in D = 4

forbidden_imports_used: false
observed_target_used_in_pass_conditions: false
proposal_allowed: false
proposal_allowed_reason: "D=4 arithmetic support is source-ready and the finite taste-count authority is retained-bounded, but the D=4 readout / effective-potential-density bridge remains open."
```

## 8. Changelog

- **2026-06-11 audit-requested repair.** Synced the source scorecard to
  the runner's five PASS gates after checking the current runner; added
  registered Tier-A routing for the staggered-Dirac carrier admission
  through `AC_phi_lambda`; and recorded the strict D=4 readout /
  effective-potential-density bridge check, leaving the future proof
  obligation scoped to the determinant/effective-potential-density to
  physical-VEV map with exponent, sign, placement, and normalization.
- **2026-06-12 audit firewall.** Demoted the stale bounded-theorem proposal
  wording to conditional D=4 arithmetic support and made the D=4 readout /
  effective-potential-density bridge an explicit open target.
- **2026-06-15 taste-authority repair.** Replaced the stale load-bearing
  citation edge to the unaudited staggered-realization gate with retained
  bounded taste-count authorities. The D=4 readout / effective-potential-density
  bridge remains open.
- **2026-06-15 D=4 readout bridge candidate.** Added a bounded source-side
  bridge note and runner proving the D=4 effective-potential-density readout
  map's exponent, sign, placement, and normalization under the explicit
  `rho_* = A(L_t) v(L_t)^4` premise. This does not apply any audit verdict or
  status movement.

## 2026-06-15 audit-unlock residual certificate

This row is re-opened only as conditional D=4 arithmetic support. The
runner-checked facts are the condensate-density ratio, the distinct
`D = 4` versus `D = 16` compression candidates, and the identity
`1/D = 4/2^D` at `D = 4`.

The remaining blocker is not arithmetic: a later theorem must derive the
D=4 readout / effective-potential-density insertion map, including exponent,
sign, placement, normalization, and the framework-native `N_taste = 2^D`
carrier realization. No observed VEV, new axiom, or status promotion is
introduced by this repair.
