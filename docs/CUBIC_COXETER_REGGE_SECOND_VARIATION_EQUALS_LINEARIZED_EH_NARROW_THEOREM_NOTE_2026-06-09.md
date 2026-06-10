# The Second Variation of the Regge Action on the Retained Cubic-Coxeter Complex Equals the Linearized Einstein-Hilbert Second Variation at Leading Order — Exactly, Isotropically, with Derived Normalization

**Date:** 2026-06-09
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_cubic_coxeter_regge_second_variation_3d_2026_06_09.py`](../scripts/frontier_cubic_coxeter_regge_second_variation_3d_2026_06_09.py) (PASS=10 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_cubic_coxeter_regge_second_variation_3d_2026_06_09.txt`](../logs/runner-cache/frontier_cubic_coxeter_regge_second_variation_3d_2026_06_09.txt)

## Scope

The retained row
[`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)
establishes, for the standard six-tetrahedra body-diagonal Coxeter chain `T(Z³)` (flat edge lengths
`{1,√2,√3}`, corrected 6-tet axis edge-star), that flat space has zero deficits and zero Regge action —
i.e. *flat is a solution*. The landed but unaudited R3 target row
`R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md`
certifies the **target** operator and explicitly guards that "the cubic-Coxeter Regge action's explicit
`δ²S_R`" is not supplied. This note supplies it: the **second variation of `S_R = Σ_e ℓ_e δ_e` around
flat, on exactly the retained complex**, computed natively and compared against the continuum.

## Theorem (runner-verified, machine-exact gates throughout)

On the retained complex (periodic build, `L=4` cells per side; all couplings range-complete):

1. **Flat anchor (R1).** Every interior edge deficit is `0` to machine precision; the representative
   axis edge has the corrected **6-tet** edge-star of the retained row's 2026-05-19 repair; `S_R = 0`.
2. **Exactness gates (R2, R2b, R2c).** The per-tetrahedron Schläfli identity `Σ_e ℓ_e dθ_e = 0` holds
   to machine precision; `J = ∂δ/∂ℓ` is **symmetric** (Regge's first-variation identity `∂S_R/∂ℓ_e =
   δ_e` realized: `J` is the Hessian); a numerical second difference of the **actual action** matches
   `εᵀQε` end-to-end; and a continuum gauge perturbation maps through the exact line-averaged metric
   map onto **exactly** the discrete vertex-displacement family (pins all phase conventions).
3. **Discrete gauge, exact (R3, R3b).** Vertex displacements of the flat complex are **exact zero
   modes of `δ²S_R` at every momentum** (machine precision, real-space and Bloch) — the discrete
   diffeomorphism family. *(Contrast: the stencil-transcribed continuum operator on the hypercubic
   lattice has only approximate gauge zero modes, residual `~p⁵` — the genuinely geometric action does
   exactly what the transcription could not.)*
4. **k=0 (R5).** Constant metric perturbations re-flatten the complex (exact zero modes). The complex
   has **seven** edge classes per cell (3 axis + 3 face-diagonal + 1 body-diagonal) against six metric
   components: the single **non-metric breathing mode** is **massive** (weight `−24` in the raw `S_R`
   orientation, `+48` in the standard Euclidean orientation `S_E = −2S_R`): **no spurious flat
   direction beyond gauge + metric.**
5. **The main result (R6).** At small `k`, the metric-sector quadratic form (exact line-averaged
   metric map; slice-invariance verified by Schur complement vs projection) satisfies

   > `Q_h(k) = c · Q_EH(k) + O(k⁴)` with the **single constant `c = −1/2`**, in **all three** lattice
   > directions (axis, face-diagonal, body-diagonal); relative residual `~10⁻⁸`; direction spread
   > `~10⁻⁸` — **exact O(k²) isotropy**.

   Here `Q_EH` is the 3D Euclidean linearized EH pairing `Σ h_ab G^{ab}(h)`, with the operator derived
   in-runner from the curvature definitions (the same machinery as the 3+1 target-operator row).
   `c = −1/2` **is** the textbook correspondence: `δ²S_R = ½ δ²(∫√g R)` combined with the variational
   sign `δ(√g R) = −√g G^{μν} δg_μν` — the Regge↔EH second-variation correspondence, **including its
   `1/2` normalization, is derived on the retained complex**, not asserted.
6. **Channel structure (R7).** The two TT channels are **equal** (exact O(k²) spin-2 isotropy); the
   transverse-trace channel has the **opposite sign with equal magnitude** (ratio exactly `−1`); the
   gauge channel is zero. The landed but unaudited degenerate-supermetric no-go
   `UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`
   named exactly this pair (`V_trace = −k²/2`, `V_TT = +k²/2`, equal magnitudes): that pair is
   hereby **derived from the framework's own retained geometry**.

## Orientation (the one remaining sign — honest)

Everything orientation-independent is derived: the opposite-sign trace/TT pair with equal magnitudes,
the exact isotropy, the exact gauge zeros, the massive breathing mode, the `1/2` normalization. The
**overall orientation** (`S_R` vs `−S_R`, equivalently which channel is "positive") is the single
remaining sign. In the standard Euclidean orientation `S_E = −2S_R`: TT positive, conformal/trace
negative (the textbook Euclidean conformal-factor structure), breathing `+48` massive. This residual
orientation is the **same single located sign** as the residual named in
`GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md`
(landed but unaudited) — the geometric route does not add a second sign admission.

## What is and is not claimed

- **Is:** on the retained 3D cubic-Coxeter complex, `δ²S_R` around flat — with machine-exact internal
  gates (Schläfli, Hessian symmetry, end-to-end action finite-difference, gauge-exactness, Bloch
  faithfulness) — equals `−½ ×` the in-runner-derived 3D Euclidean linearized EH pairing at `O(k²)`,
  isotropically, with the stated channel structure, exact discrete gauge zero modes, and a massive
  non-metric breathing mode. The comparator pair named by the no-go is derived here at the spatial
  level rather than consumed from that unaudited row.
- **Is not:** does **not** supply the 4D/timelike cubic-Coxeter complex or its kinetic fiber metric /
  multiplier structure (the 3+1 split of the **target** operator is the separate in-review row; the 4D
  geometric extension is the named next step); does **not** derive the edge-length degrees of freedom
  or select the Regge action from the axioms (edge lengths are the supplied dynamical variables, as in
  the retained row's premise; action selection remains open); does **not** fix the overall action
  orientation (the located sign residual, unchanged); does **not** make any nonlinear/strong-field
  claim. Adds no axiom, no primitive, no fitted value.

## Boundaries (honest)

- **3D spatial** (the retained complex's own dimension). The decisive 4D objects (graviton kinetic
  term from the geometric action; lapse/shift multipliers) require the 4D complex — named follow-up.
- **`O(k⁴)` and beyond:** the proportionality is leading-order; lattice corrections enter at `O(k⁴)`
  (residuals `~10⁻⁸` at `k = 10⁻³` are consistent with `O(k⁴)`/numerical floor; the `O(k⁴)`
  anisotropy is not characterized here).
- **The exact line-averaged metric map is load-bearing** for the comparison (midpoint phase × sinc):
  a phase-free map is an `O(k)`-wrong slice of edge space whose breathing-leak reproduces exactly the
  contaminated numbers of the first draft — documented in the runner as a convention gate (R2c).
- The continuum comparator is derived in-runner from curvature definitions; literature (Regge 1961;
  Rocek–Williams lattice graviton; Cheeger–Müller–Schrader convergence) is cited as context only.

## Load-bearing input and contextual targets

- [`CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md) — the retained complex (verbatim chain), flat anchor, corrected edge-star (all reproduced in R1).
- Context only, not consumed as retained authority: `UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md` names the comparator pair this note derives; `R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md` names the target-operator guardrail this note addresses at the 3D spatial level; `GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md` names the located sign residual this note leaves unchanged. These rows are landed but unaudited at review time.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The complex, its dihedral geometry, the Regge Hessian,
and the continuum comparator operator are all constructed/derived inside the runner from the retained
row's stated geometry and the curvature definitions; Regge/Rocek–Williams/Cheeger–Müller–Schrader are
cited as context only and enter no check. The `c = −1/2` value is an output, cross-checked against the
independently derived textbook normalization, not an input.
