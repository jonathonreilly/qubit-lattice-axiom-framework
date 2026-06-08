# The Lattice→Physical Unit Conversion is the Accepted Non-Bounding Ruler, Not a Blocking Gap: Dimensionful Results are Scale-Resolved; the Genuine Open Inputs are Dimensionless — Reconciliation Note

**Date:** 2026-06-08
**Claim type:** meta (a units/tier reconciliation: the scale reference is non-bounding; dimensionful results are scale-resolved by it)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/unit_conversion_is_accepted_non_bounding_ruler_runner.py`](../scripts/unit_conversion_is_accepted_non_bounding_ruler_runner.py)
**Cached output:** [`logs/runner-cache/unit_conversion_is_accepted_non_bounding_ruler_runner.txt`](../logs/runner-cache/unit_conversion_is_accepted_non_bounding_ruler_runner.txt)

## Audit context

Something must convert lattice-natural units (powers of the spacing `a`) to physical units, or no
prediction can be compared to experiment. The framework supplies exactly one such converter — the
[`SCALE_REFERENCE_PRIMITIVE`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (`a⁻¹ = M_Pl`, owner-approved,
registered in `axiom_premise_nodes.json`). This note reconciles the framework's "scale / unit"
language with the accepted-primitive policy: the ruler is a **non-bounding** primitive, so dimensionful
results are **scale-resolved** by it — not blocked. It records the correction across this session's
emergent-spacetime/gravity arc and separates the genuinely-different "unit" objects.

## Safe statement

**Theorem (the ruler resolves the unit; the genuine gaps are dimensionless).**

1. **Dimensionless framework data needs no ruler.** Ratios, mixing angles, and counts are **invariant**
   under rescaling the ruler `a → λa` (verified) — they carry no unit and are derivable without any
   scale.
2. **Every dimensionful output = (dimensionless data) × (the one ruler).** The lattice baseline carries
   no dimensionful number; by Buckingham-Pi any dimensionful prediction factorises as a dimensionless
   framework quantity times `a^n`, with `a` set **once** by `a⁻¹ = M_Pl` (e.g. `a_τ = (1/v_front)·a_s`;
   `m_phys = (m/M_Pl)·M_Pl`). So the **only** dimensionful input any prediction needs is the single
   accepted ruler.
3. **The ruler is an approved, non-bounding primitive.** Per `AXIOM_MINIMALITY_POLICY` §6, approved
   framework primitives **chain-satisfy dependencies without bounding downstream status**, whereas
   Tier-A admitted imports chain-satisfy only at `retained_bounded`. So a row whose **only**
   non-retained dependency is the ruler is **retention-eligible at the full tier** — the ruler neither
   blocks nor caps it.
4. **Reconciliation.** "The absolute scale is the clock-rate no-go"
   ([`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md),
   `retained_no_go`) is a statement about the **records** (they supply the tick/edge *count*, not the
   physical rate). The accepted ruler supplies the **unit**. So the dimensionful results that name this
   no-go are **scale-resolved** by the ruler — retention-eligible *modulo their dimensionless inputs* —
   **not blocked**.

## What this reconciles

- **This session's emergent-spacetime/gravity arc** — the `EMERGENT_METRIC` conformal-class note, the
  gravity-lensing note, the gravity-sign no-go, and the min-time-step tie — each describes the absolute
  scale as "the clock-rate no-go." Read precisely (per §4) that is the *records'* no-go; the **accepted
  ruler** supplies the unit, so those dimensionful pictures (the metric scale, the Planck-time minimum,
  the lensing/Shapiro magnitudes) are **scale-resolved**, not open scale-gaps. (The companion
  `MIN_TIME_STEP_IS_THE_PLANCK_TIME...` note already states this for the time minimum.)

## What this is NOT (genuinely different objects)

- **The `Y_T` source-measure / `g_bare` action-unit "no-go" notes** concern a **dimensionless**
  path-integral source/measure normalization (a separate Tier-A question) — **not** the dimensionful
  ruler. They are correctly bounded by *that* admission, not by the scale reference.
- **The dimensionful-value lanes** (e.g. the atomic Rydberg eV scale,
  `ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY`) need the ruler **plus** dimensionless ratios
  (`m_e/M_Pl`, `α`). The ruler being accepted resolves the *unit*; the **residual is dimensionless**
  (the mass ratio / coupling), not the ruler.
- **The `planck_*_no_go` notes** ("cannot *derive* the Planck scale from structure") are **correct and
  consistent** — they *justify* treating the scale as a primitive (a unit is not derivable); they do
  not mis-frame it.

So the framework is, in fact, consistent on the ruler: the only correction is to read "scale = no-go"
as the records' no-go (resolved by the accepted non-bounding ruler), never as a tier-bounding block.

## Boundary (honest)

- A **reconciliation / tier-hygiene** result, not a new physical derivation. It demonstrates the
  Buckingham-Pi distinction and applies the accepted-primitive policy; it derives no new dimensionless
  content.
- It does **not** re-tier any row (the independent audit lane does). It identifies which "scale gaps"
  are the accepted non-bounding ruler (scale-resolved) versus genuine dimensionless residuals.

## Forbidden imports check

No new axiom, import, or primitive. It *uses* the already-approved scale-reference primitive and the
§6 policy. Finite, memory-safe arithmetic.

## Runner check breakdown

Class A: (A1) dimensionless data is ruler-invariant; (A2) dimensionful = dimensionless × the one ruler;
(A3) the ruler is non-bounding (vs Tier-A which caps); (A4) the records' clock-rate no-go is resolved by
the accepted ruler ⟹ dimensionful results are scale-resolved. Expected `runner_check_breakdown = {A: 4,
B: 0, C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

Dimensionless quantities are invariant under rescaling the ruler (verified), and any dimensionful output
factorises as dimensionless data times the single accepted ruler `a⁻¹ = M_Pl` (Buckingham-Pi). That
ruler is an approved framework primitive that chain-satisfies without bounding downstream status (policy
§6), so a result whose only non-retained dependency is the ruler is retention-eligible at the full tier.
The "absolute scale is the clock-rate no-go" language across the session's arc is therefore about the
records (count, not rate); the ruler supplies the unit, so those dimensionful results are scale-resolved,
not blocked. The note is honest that it is a units/tier reconciliation (no new physics, no re-tiering)
and that the genuinely-open inputs elsewhere (source-measure, mass ratios, couplings) are dimensionless,
not the ruler. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/unit_conversion_is_accepted_non_bounding_ruler_runner.py
```
