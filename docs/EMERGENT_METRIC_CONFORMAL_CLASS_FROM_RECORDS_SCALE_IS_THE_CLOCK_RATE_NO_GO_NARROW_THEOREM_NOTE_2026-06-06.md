# The Emergent Lorentzian Metric: the Records Derive the Conformal Class (Causal Structure); the Scale is the Clock-Rate No-Go — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem (a conformal-rigidity assembly + a precisely-located conformal-factor no-go boundary)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/emergent_metric_conformal_class_from_records_runner.py`](../scripts/emergent_metric_conformal_class_from_records_runner.py)
**Cached output:** [`logs/runner-cache/emergent_metric_conformal_class_from_records_runner.txt`](../logs/runner-cache/emergent_metric_conformal_class_from_records_runner.txt)

## Audit context

This session derived the emergent time axis (the record-count `I`-gradient), the thermodynamic
arrow, and the (3,1) Lorentzian signature, and closed the reconstructed-`H` microcausality bridge
(the Lieb-Robinson light cone). This note completes that emergent-spacetime arc: it assembles those
results into the emergent Lorentzian **metric**, and locates exactly which part of the metric the
records deliver — the **conformal class** (causal structure) — and which part is a standing no-go —
the **conformal factor** (scale / clock rate).

## Safe statement

A Lorentzian metric decomposes as `g_{μν} = Ω² ĝ_{μν}`: a **conformal class** `ĝ` (fixed by the null
cones / causal structure) times a **conformal factor** `Ω` (the scale, the proper-time-per-event
rate). By the Hawking-King-McCarthy / **Malament rigidity** theorem, the **causal structure** (the
light cones) determines the metric **up to** the conformal factor.

**Theorem (conformal class derived; conformal factor = the clock-rate no-go).**

1. **The records supply the causal structure.** The event **order** is the record-count `I`-axis
   (the derived time axis); the **light cone** is the Lieb-Robinson cone of the analytic
   reconstructed dispersion `E(p)=arcsinh√(m²+Σ sin²p_μ)` (finite `v_LR`, the merged microcausality
   bridge); the **(3,1) signature** is 1 timelike (the monotone `I`-axis) + 3 spacelike (the
   reversible `Z³`). Together these are the conformal-class data.
2. **Malament rigidity: the cone fixes the conformal class, not the scale.** `g` and `Ω²g` share the
   **same null cone** (null vectors are conformally invariant — verified), while a different
   cone-speed metric does **not**; so the causal cone determines `ĝ` (the conformal class) and
   leaves `Ω` free.
3. **The conformal factor is the post-record clock-rate no-go.** The record count/order is
   **invariant** under reparametrizing the clock map `τ` (the same event history supports many
   inequivalent monotone `τ`, hence many rates — verified). This is the retained
   [`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md)
   (`retained_no_go`): finite histories give order/count, **not** a physical clock metric/rate;
   and [`RECORD_CLOCK_RATE_NORMALIZATION_GATE`](RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md)
   (`retained`): Record does not pick the rate normalization. The conformal factor `Ω` (= the clock
   rate / metric scale) **requires a supplied clock unit `τ`**.

**Conclusion.** The emergent Lorentzian metric's **conformal/causal structure is derived from the
records** (via Malament rigidity); its **scale (the conformal factor = clock rate) is the
precisely-located post-record clock-rate no-go.** Geometry's causal structure is records-native; its
scale needs a supplied clock unit.

## What this completes / opens

- It completes the session's emergent-spacetime arc: **records → time axis → arrow → (3,1) signature
  → light cone → the metric's conformal class.** The metric is derived *up to a conformal factor*.
- It sharpens the metric-scale gap from a vague "no metric" into a **precise** statement: the *only*
  missing datum is the conformal factor, and it coincides with the standing clock-rate no-go (the
  scale needs a supplied clock unit — a Planck/scale-reference primitive).
- A **position-dependent** record-density (varying `v_LR`) would **curve** the conformal class — the
  seed of an emergent curved geometry / gravity. That extension is beyond this note (the homogeneous
  free case gives the Minkowski conformal class).

## Boundary (honest)

- **Conformal class, not the full metric.** The records deliver the causal/conformal structure; the
  conformal factor (scale) is explicitly the located no-go, not delivered here.
- **Malament rigidity is reproduced, not imported as authority** (the null-cone conformal invariance
  is computed). The HKM/Malament theorem is a standard differential-geometry fact, used as the bridge.
- **Homogeneous free case.** The curved (gravity) extension — varying record-density curving the
  conformal class — is named, not built.

## Forbidden imports check

No new axiom. A_min + the session's emergent-time results (time axis / arrow / signature / LR cone,
reproduced self-contained) + the retained clock-rate no-go. The Malament conformal-invariance fact is
reproduced numerically. Exact finite-dimensional.

## Runner check breakdown

Class A: (1) the records supply the causal structure (order + LR cone + (3,1) signature); (2) Malament
rigidity (the cone fixes the conformal class, not the scale); (3) the conformal factor is the
post-record clock-rate no-go (count-invariance under reparametrization); (4) the assembly — conformal
class derived, conformal factor = located no-go. Expected `runner_check_breakdown = {A: 4, B: 0, C: 0,
D: 0, total_pass: 4}`.

## Honest auditor read

The reconstructed dispersion has finite group velocity (a light cone), the `I`-axis is a total order,
and the (3,1) signature gives 1 timelike + 3 spacelike — the causal structure. `g` and `Ω²g` share
the null cone while a different cone-speed metric does not, so the causal cone fixes the conformal
class and leaves the scale free (Malament). The record count/order is invariant under monotone
reparametrization of the clock, so the conformal factor (clock rate) is exactly the retained
post-record clock-rate no-go. The result is an honest assembly: the emergent metric's conformal/causal
structure is records-derived; its scale is a precisely-located no-go requiring a supplied clock unit.
The note is explicit that it delivers the conformal class (not the full metric) and names the curved
(gravity) extension without building it. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/emergent_metric_conformal_class_from_records_runner.py
```
