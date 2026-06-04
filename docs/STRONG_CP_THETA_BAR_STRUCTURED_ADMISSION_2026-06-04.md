# Strong-CP — θ̄ = θ_QCD + arg det M is a genuine admission (not forced; shared with the SM), sharpened into a two-prong admission with two verified sub-results, and its mass half reduces to AC_φλ

**Date:** 2026-06-04
**Claim type:** sharpening of a Tier-A admission (`strong_cp_theta_zero`) — structures the flat θ̄=0 admission into two prongs with named residuals, two verified forced sub-results, and a partial Tier-A reduction. Not a strong-CP solution.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade. It does not edit, re-cite, or promote any existing row.
**Runner:** `scripts/strong_cp_theta_bar_structured_admission_2026_06_04.py` (SCORECARD 6/6).

## Result — θ̄=0 is not forced; it is a genuine admission honestly shared with the Standard Model
The physical, basis-invariant strong-CP parameter `θ̄ = θ_QCD + arg det(M_quark)` is **not forced** to
zero by the framework. Neither prong closes; the full RP+CPT+conjugation-even structure does **not** beat
the retained `strong_cp_rp_half_cannot_forbid_cp_odd` no-go. But the admission sharpens, and the framework
does **modestly better than the SM** in two concrete, verified ways.

## Prong A (gauge, θ_QCD) — a derived "no bare 4-form slot," but the canonical θ-vacuum survives
- **NEW (verified):** the topological term's Euclidean writing `θ ∫ Tr(F∧F)` is a **4-form**, which has
  `C(3,4)=0` components on the fundamental dim-3 `Z³` *space* (the slot exists only at dim-4, `C(4,4)=1`).
  So "no bare `F∧F` slot at the fundamental level" is **derived**, not merely admitted — a mechanism the
  RP-half no-go lacked.
- **But it does not force θ_QCD=0:** (1) the θ-vacuum is fundamentally **canonical** — the phase of
  large-gauge winding `π₃(SU(3))=ℤ` coupling to the Chern–Simons 3-form *on the 3-space* — untouched by a
  4-form-degree argument (the argument removes the 4-form *writing*, not θ itself); (2) whether `Z³`
  realizes any winding/instanton sector is **unsettled** (the instanton sector is a textbook `R⁴` import,
  `instanton_4d_action` retained_bounded-but-named-admission; meron/fractional are open_gate); (3) the
  emergent-level kill needs the **undelivered premise** that the gauge emergence measure is
  O_h-even/parity-even.
- **One genuine lever the SM lacks:** the spatial **O_h pseudoscalar character** — verified
  `R·R·R·ε = det(R)·ε` on all 48 signed permutations, so the lattice θ-slot `Q[F]=ε^{ijk}F_{0i}F_{jk}`
  carries `det(R)` (no `i`, no `K`) and an **O_h-even action forbids it outright** (no Θ-pairing
  cancellation). Conditional on O_h-invariance of the full action class + slot identification (the
  pseudoscalar-measure loophole: odd measure × odd slot = even).

## Prong B (mass, arg det M) — K-reality collapses it to {0,π}, but only the chiral-removable part
- **NEW (verified):** under the framework's K-reality, the C₃ conjugate-symmetric circulant
  `M = aI + bC + b̄C²` has a **real determinant** (`max|Im det| ≈ 1.5e-16`), so `arg det M ∈ {0,π}` — a
  genuine collapse of the SM's continuous O(1) phase to a **discrete ℤ₂**.
- **But this is decisively only the chiral-removable part:** `arg det M` is chiral-basis-dependent — an
  axial rotation `M→e^{2iα}M` shifts `arg det` by `2nα=6α` (verified) and breaks Hermiticity; only the sum
  `θ̄` is invariant. The retained Wilson-measure constraint (`operator_basis` Thm 2.4, audited_conditional)
  only fixes `Re Tr U_P` and is **anomaly-blind** (invariant under that axial rotation), so it does not
  forbid the rotation that un-does Hermiticity. The load-bearing **joint-basis bridge** — that the
  gauge-OS reflection is the *same* antiunitary as the generation conjugation-parity that Hermitianizes
  `M` — is **unbuilt** (the two antiunitaries act on different sectors: gauge links vs generation index).
  Without it, "arg det M=0" is the removable, physically-vacuous statement. Even granting it, `{0,π}→0`
  rests on the positive-mass-sign **convention** (`θ̄=π` is equally CP-violating), and lepton→quark
  transport is asserted, not proven.

## The full RP+CPT route does not beat the no-go
Verified: the retained emergent-time reality is **reflection-composed** K (`P M P = M(b̄)` with `P` a real
generation transposition; `conj(M)≠M`), under which the T-odd θ density is conjugation-**even** and
**survives** — reproducing the RP-half cancellation. Only an unretained **pure-K** would forbid it. And
CPT is the wrong tool: `θ·F∧F̃` is P-odd × T-odd × C-even = **CPT-even**, so CPT cannot forbid it (category
error). The no-go extends.

## θ ↔ AC_φλ — the mass half reduces (partial Tier-A consolidation)
The mass-orientation half `arg det M` **is** the AC_φλ object: the same C₃-Schur conjugate-symmetric
circulant (verified `Im det = 0` around the full coupling circle), and the reduction *needs* the
conjugate-symmetry — a genuinely complex coupling `c≠b̄` gives surviving `arg det ≠ 0` (verified). So θ's
mass contribution collapses onto AC_φλ's open gates (the holomorphic/complex-coupling BAE gate + the
signed-vs-singular-value `{0,π}` readout). **θ_QCD is independent** and does not reduce. A verified
reduction would shrink the genuine Tier-A count from **2** (θ_QCD; arg det M) to **(1 shared
mass-orientation = AC_φλ) + (1 residual θ_QCD)** — but it inherits the tier of the *unaudited*
`ac_phi_lambda_preserved_c3_structural_foreclosure` note, so it is currently a proposal, not settled.

## Honest standing
The framework does **not** solve strong-CP — θ̄=0 is a genuine admission, honestly shared with the SM. It
does modestly better in two verified ways (the derived no-4-form-slot; the continuous→{0,π} mass-phase
collapse) and has one genuine gauge-side lever the SM lacks (the O_h pseudoscalar character). The flat
admission is now a structured two-prong one with named residuals.

## The next paths this opens (not closing)
- **Joint-basis bridge** (the load-bearing Prong-B blocker): prove or admit that the gauge-OS reflection
  is the same antiunitary as the generation conjugation-parity — without it Prong B is vacuous.
- **O_h-even gauge measure:** derive parity/conjugation-evenness of the *gauge*-sector emergence measure
  (analogous to the retained generation-sector result, not transported), closing the pseudoscalar loophole.
- **Z³ instanton sector:** settle whether the discrete substrate realizes a large-gauge winding sector at
  all (whether θ is even a fundamental coupling).
- **Audit `ac_phi_lambda_preserved_c3_structural_foreclosure`** to settle the θ→AC_φλ reduction tier.

## Provenance (verified 2026-06-04)
- `C(3,4)=0`, `C(4,4)=1`; O_h law `R·R·R·ε=det(R)·ε` on 48 elements; K-real circulant `Im det≈0`;
  axial-rotation shift `6α` breaking Hermiticity; `Im det=0` around the coupling circle; `c≠b̄ ⇒ Im det≠0`:
  verified directly (runner 6/6). Repo anchors read on origin/main (`strong_cp_theta_zero_note`,
  `strong_cp_rp_half_cannot_forbid_cp_odd_imaginary` retained_no_go, `strong_cp_operator_basis_and_mass_orientation`
  audited_conditional, `strong_cp_epsilon_pseudotensor_oh_sign_bridge` retained_bounded,
  `koide_emergent_time_eta_conjugation_parity` retained_bounded).
- This note sets no audit status; it structures the θ̄ admission and names its residuals and the partial
  AC_φλ reduction.
