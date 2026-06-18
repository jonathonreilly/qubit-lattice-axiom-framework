# The Retained Cubic-Coxeter Regge Graviton Action Sections the SO(3) Frame Gauge at O(k⁴): Covariant at EH, Frame-Selecting at the Lattice Scale, with a Lattice-Fixed Amplitude

**Date:** 2026-06-17
**Claim type:** narrow_theorem (synthesis of retained rows; turns the open frame-sectioning *channel* of PR #4285 into an actual *selection*, and removes the import-bound on the structural anisotropy amplitude)

**Claim scope:** The cubic-Coxeter Regge graviton second variation `δ²S_R` on the framework's
`Z³ × Z_τ` complex — a derivative-dependent (momentum-dependent) action — is **frame-covariant at
O(k²)** (the retained EH/orbit-flat regime: `δ²S_R = −½·Q_EH`, isotropic) and **frame-sectioning at
O(k⁴)**. Specifically: **(1)** its retained O(k⁴) on-shell tail `α(n̂) = −(1 + Σ_a n̂_a⁴)/12` has a
lattice-**fixed** amplitude (axis `−1/6`, face `−1/8`, body `−1/9`; spread `1/18`) — derived from
`H = 6I − A` geometry, **no GR/PDG input**; **(2)** the cubic-harmonic frame functional
`f(n̂) = Σ_a n̂_a⁴` on `S²` has a **discrete critical set = the lattice crystal directions** (6 axis
**maxima** `f=1`, 8 body-diagonal **minima** `f=1/3`, 12 face-diagonal **saddles** `f=1/2`; Hessian
signatures certified), so the O(k⁴) energy's stationarity **reduces the continuous SO(3) frame
freedom to the discrete O_h crystal frame** — the canonical (discrete) frame *section* the
polarization-frame-bundle blocker names as missing; **(3)** the O(k⁴) angular weight (the cubic axis
4-tensor) as a graviton quadratic form **equals** the spin-2 `E ⊕ T2` weight `G_aniso` (recomputed
self-contained here; consistent with the companion PR #4285, pending), which is **not** SO(3)-orbit-flat — so the dispersion-direction anisotropy and the field-frame
sectioning are the **same `l=4` object**. **(4)** This is **strictly O(k⁴)**: O(k²) carries no angular
anisotropy (EH covariance preserved); and the weight is `k`-dependent (derivative-dependent), so it
lies **outside** the constant linear Casimir-projector class — escaping the Casimir-class no-go via
that no-go's own named escape.

**Status authority:** independent audit lane only. This note writes no audit verdict and retags no
ledger row.
**Loop:** science-fix lane 2026-06-17 (#4285 follow-on).
**Runner:** [`scripts/regge_ok4_frame_section_2026_06_17.py`](../scripts/regge_ok4_frame_section_2026_06_17.py)
(`TOTAL: PASS=14 FAIL=0`, deterministic — SO(3) probes seeded; numpy only).
**Authority role:** source-note proposal. If retained, supplies (a) the O(k⁴) frame-*selection*
that converts PR #4285's open sectioning channel into the discrete crystal-frame canonical section
the frame-bundle blocker requires (flat atlas), and (b) the lattice-fixed value of the leading
SO(3)-breaking graviton anisotropy amplitude (removing the import-bound on the *structural* value).

## 1. The two regimes (what is already retained)

- **O(k²) — covariant (no sectioning).** `CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09`
  (**retained_bounded**): `δ²S_R = −½·Q_EH` at O(k²), exactly and **isotropically**; and
  `UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10` (**retained**): the isotropic
  complement energy is SO(3)-orbit-flat. So at the EH order there is **no** preferred frame — GR-like
  covariance. (The flat-atlas note `UNIVERSAL_GR_SPIN2_TWO_DERIVATIVE_CURVATURE_GENERATOR_SUPPLIED_FLAT_ATLAS`,
  unaudited, independently shows the O(k²) generator transforms as `c·M_EH(Rk)` with the same `c=−½`
  in all frames.)
- **O(k⁴) — anisotropic.** `CUBIC_COXETER_REGGE_OK4_LATTICE_FINGERPRINT_BOUNDED_THEOREM_NOTE_2026-06-10`
  (**retained_bounded**): the on-shell tail `α(n̂) = −(1 + Σ_a n̂_a⁴)/12`, spread `1/18`.

This note proves the O(k⁴) tail is exactly the orbit-flat-breaking / frame-**selecting** structure,
and that its amplitude is lattice-intrinsic.

## 2. Inputs (one hop, fresh statuses on origin/main)

| Input | Role | Status |
|---|---|---|
| `δ²S_R = −½ Q_EH` at O(k²), isotropic | [SPLIT]/[WEIGHT] O(k²) covariant regime | `CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH…2026-06-09` — **retained_bounded** |
| on-shell O(k⁴) tail `α(n̂) = −(1+Σ n̂_a⁴)/12` | [DISP] | `CUBIC_COXETER_REGGE_OK4_LATTICE_FINGERPRINT…2026-06-10` — **retained_bounded** |
| isotropic complement energy is SO(3)-orbit-flat (the criterion) | [WEIGHT] | `UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT…2026-05-10` — **retained** |
| cubic O_h weight `G_aniso` breaks orbit-flatness (spin-2 ↓ O_h = E⊕T2) | [WEIGHT] (recomputed self-contained here) | companion **PR #4285** (`science/cubic-anisotropy-sections-so3-frame-2026-06-17`, not yet in ledger) |
| `Z³` adjacency `H = 6I − A` (the amplitude source) | [DISP] | `MINIMAL_AXIOMS_2026-06-05` — Lattice axiom |

No fitted parameters, no observed values, no GR/PDG comparator, no new axioms, numpy only.

## 3. The theorem (computed; runner blocks [DISP],[CRITSET],[WEIGHT],[SPLIT],[ESCAPE])

- **[DISP]** `α(axis) = −1/6`, `α(face) = −1/8`, `α(body) = −1/9`; spread `|α_axis − α_body| = 1/18`.
  Every value is fixed by `H = 6I − A` geometry — a **derived** lattice amplitude, not a GR/PDG match.
- **[CRITSET]** `f(n̂) = Σ_a n̂_a⁴` on `S²` has critical set: **6 axis maxima** (`f=1`), **8
  body-diagonal minima** (`f=1/3`), **12 face-diagonal saddles** (`f=1/2`) — 26 directions, the O_h
  crystal axes (Riemannian-Hessian signatures certified). Stationarity of the O(k⁴) frame energy is a
  **discrete** set ⇒ the continuous SO(3) frame freedom is reduced to the discrete crystal frame: a
  canonical frame **section**.
- **[WEIGHT]** the O(k⁴) angular weight (the cubic axis 4-tensor, de-traced) splits spin-2 into
  `E(2) ⊕ T2(3)` — it **is** `G_aniso` (recomputed self-contained here; consistent with the companion
  PR #4285, pending) — and the `G_aniso`-weighted complement energy is **not** SO(3)-orbit-flat
  (orbit-variation `> 0`; magnitude depends on the chosen mixing amplitude, not lattice-fixed), while
  the isotropic energy **is** (`1.2e-15`). The dispersion-direction anisotropy and the field-frame
  sectioning are the same `l=4` object.
- **[SPLIT]** no O(k²) angular anisotropy: EH-order covariance is preserved; the sectioning is
  **strictly O(k⁴)** — the leading lattice correction.
- **[ESCAPE]** the sectioning weight is carried at O(k⁴) (`k`-dependent ⇒ derivative-dependent), so it
  is **outside** the constant linear Casimir-projector class `CB(V)` ⇒ it escapes
  `UNIVERSAL_GR_TENSOR_ACTION_CASIMIR_EQUIVARIANT_CLASS_NOGO_NOTE_2026-05-17` (unaudited) via that
  no-go's own verbatim escape: *"derivative-dependent functionals (e.g. those involving spatial
  gradients of h)."*

## 4. What this contributes toward the frame-bundle blocker (flat atlas)

`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE` (audited_conditional) names the missing
primitive as a covariant 3+1 polarization-frame/projector bundle *with a distinguished connection /
horizontal distribution that picks a canonical section* and a `Π_curv` splitting the Hessian before
localization; its obstruction is that the localized channel coefficients move under spatial-frame
rotation. The O(k⁴) frame-selection here supplies a **candidate discrete crystal-frame section**: the
crystal frame is the discrete orientation at which the anisotropy is extremal/diagonal. This is a
*section*, not yet the *connection* the blocker names — so it **contributes toward**, but does not
discharge, the blocker. Combined with the O(k²) covariance (retained EH + the flat-atlas covariance
note), the picture is covariant at EH and frame-selecting strictly at O(k⁴) (the IR/O(k²) Lorentz
covariance is preserved — see §4bis and §6(iii); whether the O(k⁴) section is a physical preferred
frame or a regulator artifact is left open).

## 4bis. Cross-sector corroboration (not a conflict): the same dim-6 l=4 Lorentz-violation object

The O(k⁴) anisotropy is **not** in tension with the framework's emergent-Lorentz results — it is the
**same** dimension-6, `l=4` cubic-harmonic object they already carry. The retained
`EMERGENT_LORENTZ_INVARIANCE_NOTE` (**retained_bounded**, "(Conditional)") is "isotropic at leading
order" with a "leading `O(a²p⁴)` dimension-6 anisotropic correction / `l=4` cubic-harmonic angular
signature"; `EMERGENT_LORENTZ_RADIATIVE_STABILITY…B4` (**retained**) forbids only the marginal
(dim-4 / O(k²)) anisotropy, leaving the dim-6 residual; and `LORENTZ_VIOLATION_DERIVED_NOTE` +
`LORENTZ_VIOLATION_ANGULAR_FINGERPRINT…` (**retained_bounded**) state the violation is dim-6,
parity-even, `l=4` cubic-harmonic. The angular functional `Σ_a n̂_a⁴` here carries exactly that
pattern — `[100]:[111] = 3:1` (runner [LV]) — so the gravity-sector O(k⁴) frame-selection is
**corroborated by** the (independently retained) fermion-sector Lorentz-violation fingerprint, and no
retained exact/all-orders Lorentz or rotation-invariance result exists to contradict it. The IR
(O(k²)) covariance is preserved; the selection is strictly the dim-6 correction.

## 5. The import-bound on the matching value: removed for the structural amplitude

PR #4285 §4 called a "tensor-valued GR matching value" import-bounded. Two values were conflated:
- **(A) the lattice-intrinsic anisotropy amplitude** — `−1/12`, the per-direction `α` values, spread
  `1/18`, and (companion) `G_aniso`-coefficient — is **derived** from `H = 6I − A` + finite rep
  theory, fit-free, **no GR/PDG comparator**. The import-bound on (A) was a framing artifact; this
  note states the amplitude as the value the **lattice produces**. **Import-bound removed for (A).**
- **(B) the dimensionful GR calibration** (Newton constant in physical units; the source-channel
  `K_tensor`/`η` of `TENSOR_MATCHING_COMPLETION_THEOREM_NOTE`; comparison of the lattice lensing/anisotropy
  to an observed bound) — **genuinely external** (the readout-import / register-not-read class;
  consistent with the retained `BH_QUARTER_WALD_NEWTON_COEFFICIENT` identity, which consumes no
  observed value). **Stays import-bounded.**

## 6. Boundary / honest-auditor read

Load-bearing content is finite/exact: the closed-form `α` values ([DISP]), the certified critical-set
counts + Hessian signatures ([CRITSET]), the exact `E⊕T2` split + the seeded but convention-robust
orbit-flat contrast ([WEIGHT]). The result is a **structural** frame-selection + a derived amplitude,
**not** a completed GR matching. Open/external, explicitly: **(i)** the full polarization-frame-bundle
blocker needs the **S³ curved-background (PL `S³ × R`) transplant** of the cubic-Coxeter Regge second
variation (reproducing the flat-atlas frame collapse on a curved background) — finite/firewall-clean
but not done here; **(ii)** the **dimensionful GR calibration** (§5B) is genuinely import-bounded;
**(iii)** the O(k⁴) frame-selection is a lattice rotational anisotropy — its **comparison to an
observed Lorentz/rotation-violation bound** would be an import, not made here. Whether the O(k⁴)
crystal-frame selection should be read as a physical preferred frame or as a regulator artifact that a
continuum/coarse-graining limit removes is left to the audit lane and downstream work; this note proves
only the structural sectioning, its lattice-fixed amplitude, and the Casimir-class escape.
