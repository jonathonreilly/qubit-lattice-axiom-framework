# Emergent Lorentzian Metric: Conditional Conformal-Class Assembly and Clock-Rate Boundary

**Date:** 2026-06-06
**Claim type:** bounded_theorem (conditional conformal-rigidity assembly + retained conformal-factor boundary)
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/emergent_metric_conformal_class_from_records_runner.py`](../scripts/emergent_metric_conformal_class_from_records_runner.py)
**Cached output:** [`logs/runner-cache/emergent_metric_conformal_class_from_records_runner.txt`](../logs/runner-cache/emergent_metric_conformal_class_from_records_runner.txt)

## Audit context

This session proposed an emergent-spacetime arc: the record-count `I`-gradient, the thermodynamic
arrow, the (3,1) Lorentzian signature, and the reconstructed-`H` microcausality bridge (the
Lieb-Robinson light cone). This note narrows that arc on current main: it conditionally assembles the
causal-source packet needed for a Lorentzian **conformal class** (causal structure), and locates the
remaining metric datum as the retained **clock-rate boundary** for the conformal factor (scale /
clock rate).

## 2026-06-08 audit-edge repair: explicit causal-source packet

The current audit found a real source-boundary problem: the clock-rate boundary is backed by retained
authorities, but this note's conformal-class premise also used the record `I`-axis, reconstructed-H /
Lieb-Robinson cone, and `(3,1)` signature as if all three were retained one-hop inputs. On current
main that is too strong. This repair therefore makes the one-hop packet explicit and narrows the
current theorem to the conditional packet below.

```yaml
actual_current_surface_status: conditional-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "conformal-class assembly conditional on the listed causal-source packet and Malament/HKM interface assumptions"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

| input | one-hop authority | current ledger status used by this note |
|---|---|---|
| record event order / prefix-count axis | [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md), cache [`frontier_record_history_time_rate_firewall_2026_06_05.txt`](../logs/runner-cache/frontier_record_history_time_rate_firewall_2026_06_05.txt) | `unaudited`, so this is a conditional input, not a retained premise |
| clock-rate no-go | [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md), cache [`frontier_post_record_clock_rate_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_clock_rate_interface_2026_06_06.txt) | `retained_no_go` |
| clock-rate normalization gate | [`RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06`](RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md), cache [`frontier_record_clock_rate_normalization_gate_2026_06_06.txt`](../logs/runner-cache/frontier_record_clock_rate_normalization_gate_2026_06_06.txt) | `retained` |
| nearest-neighbor causal/light-cone bound | [`LATTICE_NN_LIGHT_CONE_NOTE`](LATTICE_NN_LIGHT_CONE_NOTE.md), cache [`lattice_nn_topological_causal_bound_check.txt`](../logs/runner-cache/lattice_nn_topological_causal_bound_check.txt) | `retained` |
| equal-time tensor locality | [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md), cache [`audit_companion_lieb_robinson_equal_time_tensor_locality_exact_2026_05_10.txt`](../logs/runner-cache/audit_companion_lieb_robinson_equal_time_tensor_locality_exact_2026_05_10.txt) | `retained_bounded` |
| reconstructed-H analytic-dispersion LR bridge | [`RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06`](RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md), cache [`reconstructed_h_quasilocal_microcausality_bridge_runner.txt`](../logs/runner-cache/reconstructed_h_quasilocal_microcausality_bridge_runner.txt) | `unaudited`, so the analytic reconstructed-H cone remains conditional here |
| `(3,1)` Lorentzian bounded signature/covariance surface | [`LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE`](LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md) and [`WICK_ROTATION_COMPACT_SO4_TO_LORENTZIAN_DIRAC_DOUBLING_ORIENTATION_NOTE_2026-06-07`](WICK_ROTATION_COMPACT_SO4_TO_LORENTZIAN_DIRAC_DOUBLING_ORIENTATION_NOTE_2026-06-07.md), caches [`frontier_lorentz_boost_3plus1d.txt`](../logs/runner-cache/frontier_lorentz_boost_3plus1d.txt) and [`wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation.txt`](../logs/runner-cache/wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation.txt) | `retained_bounded` / `retained_bounded`; does not by itself retain the record-time axis |

The Malament/Hawking-King-McCarthy interface assumptions are also explicit: a distinguishing,
time-oriented Lorentzian manifold of dimension >= 2, a causal/chronological order represented by the
framework event order, a light-cone relation on that event set, and the usual differentiability/
manifold hypotheses needed by the theorem. The runner computes conformal null-cone invariance on the
finite algebraic model; it does not claim to reprove the global HKM/Malament theorem. Therefore the
current theorem remains conditional until the unaudited causal-source inputs are retained or
separately admitted by the audit/review process.

## Safe statement

A Lorentzian metric decomposes as `g_{μν} = Ω² ĝ_{μν}`: a **conformal class** `ĝ` (fixed by the null
cones / causal structure) times a **conformal factor** `Ω` (the scale, the proper-time-per-event
rate). By the Hawking-King-McCarthy / **Malament rigidity** theorem, the **causal structure** (the
light cones) determines the metric **up to** the conformal factor.

**Theorem (conditional conformal-class assembly; conformal factor = retained clock-rate no-go).**

1. **The explicit causal-source packet supplies the conformal-class input conditionally.** The event
   **order** is the record-prefix/count axis; the **light cone** is the finite-cone diagnostic
   associated to the analytic reconstructed dispersion `E(p)=arcsinh√(m²+Σ sin²p_μ)` plus retained
   nearest-neighbor/locality anchors; the **(3,1) signature** is supported by retained-bounded
   Lorentzian signature/covariance authorities. Because the record-order and reconstructed-H
   analytic-dispersion source rows remain `unaudited` on current main, this conformal-class input is
   conditional-support, not retained.
2. **Malament rigidity: the cone fixes the conformal class, not the scale.** `g` and `Ω²g` share the
   **same null cone** (null vectors are conformally invariant — verified), while a different
   cone-speed metric does **not**; under the explicit HKM/Malament assumptions above, the causal cone
   determines `ĝ` (the conformal class) and leaves `Ω` free.
3. **The conformal factor is the post-record clock-rate no-go.** The record count/order is
   **invariant** under reparametrizing the clock map `τ` (the same event history supports many
   inequivalent monotone `τ`, hence many rates — verified). This is the retained
   [`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md)
   (`retained_no_go`): finite histories give order/count, **not** a physical clock metric/rate;
   and [`RECORD_CLOCK_RATE_NORMALIZATION_GATE`](RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md)
   (`retained`): Record does not pick the rate normalization. The conformal factor `Ω` (= the clock
   rate / metric scale) **requires a supplied clock unit `τ`**.

**Conclusion.** The emergent Lorentzian metric's **conformal/causal structure is assembled only
conditionally** from the explicit causal-source packet above (via the stated HKM/Malament interface);
its **scale (the conformal factor = clock rate) is the retained post-record clock-rate no-go.**
Geometry's scale needs a supplied clock unit. The conformal-class side can be promoted only after the
record-order and reconstructed-H/LR causal inputs are themselves retained or explicitly admitted.

## What this packages / opens

- It packages the session's emergent-spacetime arc: **records -> time axis -> arrow -> (3,1) signature
  -> light cone -> the metric's conformal class.** On current main the conformal-class package is
  conditional on the explicit source packet, and the metric is assembled only *up to a conformal
  factor*.
- It sharpens the metric-scale gap from a vague "no metric" into a **precise** statement: the *only*
  missing metric datum within the supplied causal-source packet is the conformal factor, and it
  coincides with the standing clock-rate boundary (the scale needs a supplied clock unit).
- A **position-dependent** record-density (varying `v_LR`) would **curve** the conformal class — the
  seed of an emergent curved geometry / gravity. That extension is beyond this note (the homogeneous
  free case gives the Minkowski conformal class).

## Boundary (honest)

- **Conformal class, not the full metric.** The explicit causal-source packet conditionally assembles
  the causal/conformal structure; the conformal factor (scale) is explicitly the located no-go, not
  delivered here.
- **Malament rigidity is assumption-gated.** The runner computes null-cone conformal invariance, but
  the HKM/Malament theorem is a standard differential-geometry bridge requiring the stated
  distinguishing, time-oriented Lorentzian-manifold assumptions.
- **Homogeneous free case.** The curved (gravity) extension — varying record-density curving the
  conformal class — is named, not built.

## Forbidden imports check

No new axiom. This note uses the Lattice + Quantum + Record baseline plus the explicit causal-source
packet above, with the record-order and reconstructed-H/LR components kept conditional on current
main, and the retained clock-rate no-go retained only for the conformal-factor boundary. The runner
reproduces the finite null-cone conformal-invariance algebra and checks the dependency/status
firewall; it does not claim full global HKM/Malament authority from the finite computation alone.

## Runner check breakdown

Class A: (1) the named one-hop source docs/runners/caches exist and report passing checks; (2) ledger
statuses match the retained/no-go clock authorities and expose current non-retained causal inputs;
(3) the source note is explicitly `conditional-support`; (4) finite cone/order/signature-anchor checks
provide the conditional conformal-class packet; (5) null-cone conformal invariance verifies the
class/scale split; (6) count/order invariance under monotone clock reparametrization verifies the
clock-rate no-go boundary. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The runner now checks the exact audit-edge issue: the clock-rate rows are retained/retained-no-go, but
the record-order firewall and reconstructed-H analytic-dispersion bridge are still unaudited on
current main. Therefore the conformal-class result is an honest conditional assembly, not a retained
metric theorem. `g` and `Ω²g` share the null cone while a different cone-speed metric does not, so
under the stated HKM/Malament interface the causal cone fixes the conformal class and leaves the scale
free. The record count/order is invariant under monotone reparametrization of the clock, so the
conformal factor (clock rate) is exactly the retained post-record clock-rate no-go. The note is
explicit that the conformal class is conditional on the packet, the full metric is not delivered, and
the curved (gravity) extension is named without being built. Effective source status remains
`conditional-support`; audit decides any row status.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/emergent_metric_conformal_class_from_records_runner.py
```
