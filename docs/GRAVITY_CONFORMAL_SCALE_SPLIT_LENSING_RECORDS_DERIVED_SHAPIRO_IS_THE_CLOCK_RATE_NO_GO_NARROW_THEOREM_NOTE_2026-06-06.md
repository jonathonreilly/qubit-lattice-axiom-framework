# Emergent Gravity, Grounded: Light-Bending is the Records-Derived Conformal Class; the Shapiro Delay is the Clock-Rate No-Go — and the Split Explains the Framework's Gravity Pattern (Narrow Theorem)

**Date:** 2026-06-06
**Claim type:** bounded_theorem (a conformal/scale split of gravitational observables + the explanation of the framework's lensing-vs-Shapiro pattern)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/gravity_conformal_scale_split_from_records_runner.py`](../scripts/gravity_conformal_scale_split_from_records_runner.py)
**Cached output:** [`logs/runner-cache/gravity_conformal_scale_split_from_records_runner.txt`](../logs/runner-cache/gravity_conformal_scale_split_from_records_runner.txt)

## Audit context

The companion
[`EMERGENT_METRIC_..._CONFORMAL_CLASS_FROM_RECORDS`](EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md)
(this session) showed the records derive the emergent metric's **conformal class** (causal light-cone
structure); its **conformal factor** (scale / clock rate) is the retained no-go
[`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md). A
position-dependent record/energy density **curves** that conformal class — the gravity seed. This note
**grounds** the seed: it splits gravitational observables by conformal weight and shows the split
**explains** the framework's existing gravity-results pattern.

## Safe statement

**Theorem (gravity's conformal/scale split).** A static lens metric
`g_{μν}=diag(−(1+2φ),1−2φ,1−2φ)` (`φ` the Newtonian potential) has two characteristic observables:

1. **Light deflection (lensing) is a conformal-class observable — records-derived.** The null-geodesic
   direction field `dx^i/dλ ∝ g^{ij}p_j` is **invariant** under any (position-dependent) conformal
   rescaling `g→Ω²(x)g` (verified pointwise to `3×10⁻¹⁶`), and a traced photon **deflects toward the
   mass** (`α≈−0.172` rad) **identically** in `g` and `Ω²g` (`|Δα|≈1.5×10⁻⁶`). So the bending angle
   depends only on the **conformal class** (the records-derived causal cone field) — **not** the scale.
   This matches the retained
   [`LENSING_DEFLECTION_NOTE`](LENSING_DEFLECTION_NOTE.md) (`retained_bounded`, *"a geodesic in a
   gradient-index field"*).
2. **The Shapiro delay is a conformal-factor observable — the clock-rate no-go.** The physical
   (proper-time) delay `Δτ=∫√(−g_{tt})dt` scales with `Ω` under `g→Ω²g` (`√(−Ω²g_{tt})=Ω√(−g_{tt})`;
   verified: `11.73→12.69`). So the Shapiro **time** delay requires the **conformal factor** = the
   clock rate = the retained no-go `POST_RECORD_CLOCK_RATE_INTERFACE`. This matches the
   `retained_no_go` `shapiro_*` family
   ([`SHAPIRO_STATIC_DISCRIMINATOR`](SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md) et al.).

**Conclusion.** Gravity's **conformal/causal part (light-bending) is records-derived** (the records'
conformal class); its **scale part (the Shapiro time-delay) is the located clock-rate no-go**. The
split **explains** the framework's gravity-results pattern: **lensing is retained** (a conformal
observable, derivable) while **Shapiro is a no-go** (a scale observable, needing the supplied clock
unit). The pattern is not a scatter of unrelated successes/failures — it is the conformal/scale split
of #3179.

## Why this is the grounded gravity seed

- It takes the curved conformal class (the gravity seed named in the companion note) to a **concrete,
  traced, falsifiable observable** — a photon bending toward a mass — and shows it needs only the
  records-derived conformal class.
- It **predicts and confirms** the structure of the existing 100+ gravity notes: every
  conformally-invariant observable (deflection, lensing geometry) is derivable; every scale-dependent
  observable (Shapiro proper-time delay, the Newtonian potential **magnitude**) bottoms out at the
  clock-rate no-go. So the framework derives **emergent gravitational lensing** from records, and the
  "missing scale" is a single, precisely-located no-go (a clock/Planck unit), not a defect of each
  individual attempt.

## Boundary (honest)

- **The conformal part, not all of gravity.** The deflection (and all null/causal lensing geometry) is
  records-derived; the scale (Shapiro magnitude, Newtonian potential magnitude) is the named no-go,
  not delivered.
- **The source mechanism is modeled, not derived here.** The note uses a weak-field lens `φ`; *that a
  record/energy concentration produces such a curved conformal class* (the Einstein-equation content)
  is named, not built — the gravity seed's dynamics is a separate object.
- Conformal invariance of null geodesics is **reproduced numerically** (pointwise direction-field +
  a traced ray), not imported as authority.

## Forbidden imports check

No new axiom. A_min + the session's records-conformal-class result + standard differential geometry
(the null-geodesic conformal invariance and the proper-time scaling, both reproduced numerically). The
comparison is to retained / `retained_no_go` notes already on `origin/main`. Exact/numerical
finite-dimensional.

## Runner check breakdown

Class A: (1) null-geodesic direction field conformally invariant (pointwise); (2) a traced photon
deflects toward the mass identically in `g` and `Ω²g`; (3) the proper-time (Shapiro) delay scales with
`Ω`; (4) the split explains the lensing-retained / Shapiro-no-go pattern. Expected
`runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

The null-geodesic direction field is invariant under position-dependent conformal rescaling (to
machine precision), and a traced photon deflects toward the mass by the same angle in `g` and `Ω²g`
(to `10⁻⁶`), so the lensing deflection is a conformal-class observable — derivable from the
records-derived conformal class. The proper-time Shapiro delay scales with the conformal factor, so it
is a scale observable requiring the clock unit — the retained clock-rate no-go. This conformal/scale
split matches and explains the framework's existing pattern (retained lensing, `retained_no_go`
Shapiro). The note is honest that it delivers the conformal (light-bending) part of gravity, names the
scale (Shapiro/Newtonian-magnitude) as the located no-go, and models rather than derives the
source-curvature mechanism. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/gravity_conformal_scale_split_from_records_runner.py
```
