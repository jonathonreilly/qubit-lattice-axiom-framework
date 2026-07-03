# A Sampled O(k⁴) Lattice Fingerprint of the Regge Graviton Sector on the 3+1 Tick Complex: Machine-Certified k⁴ Scaling, a Degenerate TT Pair, and the Candidate Dispersion Law α(n̂) = −(1 + Σₐ n̂ₐ⁴)/12

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_cubic_coxeter_regge_ok4_fingerprint_2026_06_10.py`](../scripts/frontier_cubic_coxeter_regge_ok4_fingerprint_2026_06_10.py) (PASS=13 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_cubic_coxeter_regge_ok4_fingerprint_2026_06_10.txt`](../logs/runner-cache/frontier_cubic_coxeter_regge_ok4_fingerprint_2026_06_10.txt)

## Framing (3D+1 — the framework's structure, kept explicit)

The Lattice axiom supplies **space = `Z³` only**; time is the **emergent record tick**. The complex
is `Z³ × Z_τ`: the path (Kuhn-chain) simplicial complex whose constant-tick spatial face carries the
six-tetrahedra body-diagonal chain of
[`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)
— the tick extension of that spatial complex note, **not a fundamental 4D lattice**. The tick edge is grained
on the same footing as the spatial edge per the registered
[`kinetic_isotropy_primitive`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) (`c_t = c_s`,
structural grant only; nothing beyond it is consumed). Euclidean signature is the OS0 surface; no
tick-scale or clock-rate content is touched.

The landed 3+1 tick-extension note
`CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md`
is provenance for the machinery and comparator. This note reuses that machinery inline, re-gates
faithfulness internally (flat deficits, Schläfli, Hermiticity, analytic-continuation consistency,
EH-pairing cross-derivation — F0), and reproduces the prior runner cache's comparator block (F1).
The present claim is the sampled `O(k⁴)` fingerprint of the remainder, standing on this runner's own
gates rather than on PR-status authority.

## Results (runner-verified; machine-certified gates throughout)

Let `D(k) := Q_h(k) + ½·Q_EH(k)` (the deviation from the comparator at the recomputed anchor
`c = −1/2`, refit at `k = 10⁻³`: `|c + ½| ≤ 5.4×10⁻⁸` in all five comparator directions, cache
reproduced — F1).

1. **Sampled `O(k⁴)` scaling (F2).** `log‖Re D‖–log k` slope over `k ∈ [3×10⁻³, 3×10⁻²]` is
   **4.0000–4.0001 in all 17 directions** (the 5 comparator directions + 12 random unit 4D
   directions); the numerical floor sits ≥ 100× below the smallest fitted signal.
2. **No odd order (F3).** `‖Im D‖/‖Re D‖ ≤ 2×10⁻⁹` (floor): no `O(k³)` term appears, although the
   complex's point group (`S₄ × inversion`; no single-axis reflections) would allow one.
3. **Machine-zero gauge residuals for the deviation (F4, F6).** At representative sample momenta of the
   fit grid **and at the complex on-shell root momenta**: `|Q(k)Γ(k)|`, `|Q_h(k)·h_gauge(k)|` and
   `|D(k)·h_gauge(k)|` are machine-zero at the tested points.
4. **Fifth branch re-verified at the sample points (F5).** Exactly five machine-zero modes
   (4 discrete-diffeomorphism + the decoupled branch; metric-overlap pattern 4 + 1 outside) at the
   real sample momenta — the fifth-branch pattern holds at this note's own sample points.
5. **The sampled on-shell TT dispersion law (F6, F7).** Locating on-shell points **basis-free**
   as rank drops of the full 15×15 edge-space form at `p = (k n̂, iE)`:

   > `ω²(k) = k² [ 1 − k²·(1 + Σₐ n̂ₐ⁴)/12 ] + O(k⁶)`

   with **both TT polarizations degenerate to machine floor at the sampled roots** (σ₆ *and* σ₇
   `< 10⁻¹³` at the same real root; σ₈ a full `O(k²)` gap above): no sampled birefringence at
   `O(k⁴)`. The candidate closed form
   holds to `≤ 7×10⁻⁸` across all 15 sampled spatial directions: `α(axis) = −1/6`,
   `α(face diagonal) = −1/8`, `α(body diagonal) = −1/9`; anisotropy spread `max−min = 1/18`; all
   directions subluminal. Equivalently, the on-shell deficit is `−(1/12)·Σ_μ p_μ⁴` with the **tick
   fourth power on the same footing as the spatial ones** within the kinetic-isotropy primitive's
   structural graining, and the same correction law as the
   standard hypercubic (sin²-type) scalar dispersion.
6. **The chain orientation does not imprint at the sampled tolerance (F8).** In the spatial-harmonic fit
   `α(n̂) = c₀ + c₁P₄ + c₂P₃₁ + c₃P₂₁₁`, the `S₃`-only harmonics (sensitive to the body-diagonal
   chain orientation; allowed by the complex's symmetry) are **absent**: `|c₂|, |c₃| < 2×10⁻⁸`,
   `face+ = face−`, `body+ = body−`. The on-shell `O(k⁴)` anisotropy has **full cubic (B₃) symmetry,
   more symmetry than the complex itself**; `c₀ = c₁ = −1/12`.
7. **No other branch near the cone in the three scanned F9 directions.** A wide rank-drop scan
   over `E²/k² ∈ [0.3, 2.5]` in the axis, face-diagonal, and one random spatial
   direction finds no additional on-shell branch. In those scanned directions, the
   continuum trace-comparator channel's third on-shell null is **not** realized as an
   independent lattice branch (diagnostic: the
   exactly-decoupled fifth branch carries an `O(1)` share of the on-shell trace class — metric
   share 0.58, class overlap 0.59 mod gauge).
8. **Projection-convention boundary, numerically pinned (F10, F12).** The TT-block roots of the
   *projected* metric-sector form (exact line-averaged map) at the axis are `{−2/9, −1/9}` — split,
   and unequal to the physical degenerate `−1/6`: at `O(k⁴)` the projected block's on-shell content
   is map-convention-tagged (the complement leaks back at exactly this order). The physical
   dispersion is the full-form rank drop. Likewise the off-shell per-channel table (F11/F12) is
   stated in the exact line-averaged convention; within it, the **pure-tick row equals the
   pure-space row channel-by-channel** (the `S₄` tick↔space footing at `O(k⁴)`), with rational
   values `1/72` (off-diagonal TT), `1/48` (diagonal-doublet TT), `−1/48` (transverse trace).
9. **Structure fit — honest negative (F11).** The off-shell projected coefficient `C4(k̂)`
   (machine-zero gauge residuals; extraction residual `< 4×10⁻⁷`) is **not** captured by the 8-element basis of
   linearized-curvature-squared contractions tried (`Riem²/Ric²/R²` + axis-anisotropic + `S₄`-only
   terms): relative residual 0.31 (isotropic-only 0.42). Per the brief, no fit is forced; the raw
   per-channel table is reported in the runner, and the convention-free `O(k⁴)` structure is the
   closed form of item 5.

## Units remark (primitive-respecting; context only, enters no check)

In lattice units the correction is relative size `|α(n̂)|·(ka)² ≤ (ka)²/6`. With the registered
[`scale_reference_primitive`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (`a⁻¹ = M_Pl`, a units conversion
only) this is a **Planck-suppressed** dispersion/anisotropy correction — of order `10⁻⁸⁰` relative
at gravitational-wave-band momenta (context arithmetic only). The primitives grant a
ruler and a graining form, no dimensionless physics; nothing here is a phenomenology or bound claim. This is
the structural signature by which the geometric route could in principle be falsified against an
alternative discretization, **not a near-term test**.

## What is and is not claimed

- **Is:** on the `Z³ × Z_τ` tick extension of the spatial complex, around flat, on the OS0
  surface: the deviation of the metric-sector second variation from `−½·Q_EH` scales as
  `k⁴` in the sampled directions, is even in `k` to the numerical floor, and has machine-zero gauge
  residuals at the sampled momenta;
  the on-shell graviton content near the cone is a machine-degenerate TT pair with real
  dispersion `ω² = k²[1 − k²(1+Σn̂ₐ⁴)/12] + O(k⁶)` (verified to `≤ 10⁻⁷` at 15 sampled
  directions, closed form consistent across all of them); the anisotropy is B₃-symmetric with
  spread `1/18`; no other on-shell branch appears in the F9 three-direction scan over
  `E²/k² ∈ [0.3, 2.5]`; the projected-block
  `O(k⁴)` content is convention-tagged and machine-distinguished from the physical one. All with
  the F0/F1 faithfulness gates re-certifying the complex in-runner.
- **Is not:** does **not** prove the closed form symbolically (it is verified at 15 sampled
  spatial directions + 5 four-dimensional comparator directions, at machine precision); does
  **not** characterize `O(k⁶)`; does **not** make Lorentzian-signature claims beyond the
  framework's RP/OS route (everything here is the OS0 surface); does **not** derive the
  edge-length degrees of freedom or select the Regge action (open, as in the source premises'
  premise); does **not** fix the overall action orientation (the located sign residual, unchanged
  — `α` is orientation-independent: it is a root location, not a sign); does **not** derive the
  tick scale (clock-rate boundary respected); adds no axiom, no primitive, no fitted value, and
  **no testability claim** (the units remark is a units remark).

## Boundaries (honest)

- **Closed form by sampling, not by symbol.** `α(n̂) = −(1+P₄)/12` is established numerically at
  machine precision over 15 spatial directions (5 symmetry-special + 10 random) and three `k`
  values each, with Richardson closure `< 10⁻⁶`; a symbolic proof from the dihedral algebra is a
  natural follow-up, not supplied here.
- **Euclidean/OS0 level.** On-shell points are rank drops of the analytically continued Bloch form
  at `p = (k n̂, iE)`; the roots come out real (the complex-plane scan finds no off-axis rank
  drops), but the Lorentzian reading remains by the framework's RP/OS route.
- **Convention-tagged off-shell tables.** At `O(k⁴)` the projected (line-averaged-map) quadratic
  form and the full edge-space form genuinely differ (F10): all off-shell `C4` tables are stated in
  the exact line-averaged convention of the 3D row
  ([`CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md));
  the dispersion `α` is convention-free.
- **The structure fit is a reported negative.** The 8-element curvature-contraction basis tried
  does not close on `C4`; a complete enumeration of `S₄×inversion`-invariant 8-index weight
  tensors was not attempted. The raw table stands in its place, per the brief.
- **Trace-channel reading.** "The continuum trace third null is not realized as a lattice branch"
  is a statement about rank drops of the full form near the cone only in the F9
  three-direction machine scan; the accompanying fifth-branch class diagnostic
  (overlaps 0.58/0.59) is descriptive, not a theorem.
- Literature (Regge 1961; Roček–Williams lattice graviton; Cheeger–Müller–Schrader;
  gravitational-wave dispersion-bound phenomenology for the units remark) is context only; every
  number is computed from the complex's geometry in-runner.

## No-Go Discipline Gate (scoped negatives only)

This note contains two negative statements: no additional rank-drop branch in the three scanned F9
spatial directions over `E²/k² ∈ [0.3, 2.5]`, and non-closure of the particular 8-element
curvature-contraction basis tried for the projected off-shell `C4` table. It does **not** assert a
universal no-go, a missing primitive, a required new axiom, or exhaustion of all directions,
branches, or invariant bases.

- **N1 alternatives:** symbolic branch analysis, wider energy-window scans, complex off-axis root
  searches, a complete `S₄×inversion` invariant-tensor basis, and higher-order/nonlinear closure
  are distinct routes; none is declared closed here.
- **N2 walls:** no wall count is asserted.
- **N3 hidden-wall scan:** approved primitives are used only within their declared grants; the
  units remark is non-load-bearing context.
- **N4 residual matching:** no prior no-go witness is used as authority for these negatives.
- **N5 rhetoric:** each negative is limited to the tested resolution: the scan window and the
  named 8-element basis.
- **N6 partial closure:** no convention or reframe path is rejected; no axiom or primitive change is
  requested.
- **N7 steelman:** a symbolic dihedral derivation or complete invariant-basis enumeration could
  replace the sampled/basis-limited statements with a sharper theorem.
- **N8 echo:** similar historical wall language is avoided; this note ships only the runner-backed
  scoped negatives above.

## Load-bearing inputs

- [`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)
  — the spatial complex whose tick extension is built here; its flat fact is re-verified
  in-runner (F0).
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the `c_t = c_s` structural grant for the symmetric tick graining; nothing beyond its declared
  grant is consumed (the `O(k⁴)` tick↔space footing found here is an *output* about the geometric
  action, not an input).
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — the single
  dimensionful reference `a⁻¹ = M_Pl`, consumed **only** by the units remark as a units
  conversion; no dimensionless content drawn.
- [`CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md)
  — the 3D row on main: source of the exact line-averaged metric-map convention used
  for the projected objects.
- **Context, not load-bearing:** the landed 3+1 tick-extension note
  `CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md`
  — the machinery's provenance and the `c = −1/2` anchor this note cross-checks (F1) and extends;
  all facts used from it are re-derived or re-verified by this runner's own gates.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The complex, dihedral geometry, Bloch forms, gauge
and metric maps, and both EH comparator derivations are constructed in-runner; the anchor
`c = −1/2` is recomputed, not assumed; the closed-form coefficients (`−1/12`, `−1/6`, `−1/8`,
`−1/9`, `1/18`, `1/72`, `1/48`) are outputs. Regge / Roček–Williams / Cheeger–Müller–Schrader and
gravitational-wave dispersion-bound phenomenology appear as context only and enter no check.
