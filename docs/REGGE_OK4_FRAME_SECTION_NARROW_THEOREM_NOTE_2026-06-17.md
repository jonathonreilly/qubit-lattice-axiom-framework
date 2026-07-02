# Cubic-Coxeter Regge O(k⁴) Frame-Section Support: EH-Covariant at O(k²), Cubic at the Lattice Scale, with a Lattice-Fixed Amplitude

**Date:** 2026-06-17
**Claim type:** bounded_theorem

**Claim scope:** The cubic-Coxeter Regge graviton second variation `δ²S_R` on the framework's
`Z³ × Z_τ` complex — a derivative-dependent (momentum-dependent) action — is **frame-covariant at
O(k²)** (the retained EH/orbit-flat regime: `δ²S_R = −½·Q_EH`, isotropic) and **frame-sectioning at
O(k⁴)**. Specifically: **(1)** its retained O(k⁴) on-shell tail `α(n̂) = −(1 + Σ_a n̂_a⁴)/12` has a
lattice-**fixed** amplitude (axis `−1/6`, face `−1/8`, body `−1/9`; spread `1/18`) — derived from
the finite `H = 6I − A` adjacency computation, **no GR/PDG input**; **(2)** the cubic-harmonic frame functional
`f(n̂) = Σ_a n̂_a⁴` on `S²` has a **discrete critical set = the lattice crystal directions** (6 axis
**maxima** `f=1`, 8 body-diagonal **minima** `f=1/3`, 12 face-diagonal **saddles** `f=1/2`; Hessian
signatures certified), so the O(k⁴) stationarity set gives a **finite O_h crystal-frame section
candidate**, not a physical preferred-frame theorem; **(3)** the O(k⁴) angular weight (the cubic axis
4-tensor) as a graviton quadratic form splits spin-2 into `E ⊕ T2` and is **not** SO(3)-orbit-flat —
so the dispersion-direction anisotropy and the field-frame sectioning are the **same `l=4` object**.
**(4)** This is **strictly O(k⁴)**: O(k²) carries no angular anisotropy (EH covariance preserved);
and the weight is `k`-dependent (derivative-dependent), so it lies outside the constant linear
Casimir-projector class by construction.

**Status authority:** independent audit lane only. This note writes no audit verdict and retags no
ledger row.
**Loop:** science-fix lane 2026-06-17.
**Runner:** [`scripts/regge_ok4_frame_section_2026_06_17.py`](../scripts/regge_ok4_frame_section_2026_06_17.py)
(`TOTAL: PASS=14 FAIL=0`, deterministic — SO(3) probes seeded; numpy only).
**Authority role:** source-note proposal. If retained, supplies bounded finite support for (a) an
O(k⁴) discrete crystal-frame section candidate on the flat atlas and (b) the lattice-fixed value of
the leading SO(3)-breaking graviton anisotropy amplitude. It does not discharge the
polarization-frame-bundle blocker, construct a connection, transplant the result to a curved `S³`
Regge background, or calibrate the dimensionful GR coupling.

## 1. The two regimes (what is already retained)

- **O(k²) — covariant (no sectioning).** [`CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md)
  (**retained_bounded**): `δ²S_R = −½·Q_EH` at O(k²), exactly and **isotropically**; and
  [`UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10.md`](UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10.md) (**retained**): the isotropic
  complement energy is SO(3)-orbit-flat. So at the EH order there is **no** preferred frame — GR-like
  covariance. (The flat-atlas note `UNIVERSAL_GR_SPIN2_TWO_DERIVATIVE_CURVATURE_GENERATOR_SUPPLIED_FLAT_ATLAS`,
  unaudited, independently shows the O(k²) generator transforms as `c·M_EH(Rk)` with the same `c=−½`
  in all frames.)
- **O(k⁴) — anisotropic.** [`CUBIC_COXETER_REGGE_OK4_LATTICE_FINGERPRINT_BOUNDED_THEOREM_NOTE_2026-06-10.md`](CUBIC_COXETER_REGGE_OK4_LATTICE_FINGERPRINT_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  (**retained_bounded**): the on-shell tail `α(n̂) = −(1 + Σ_a n̂_a⁴)/12`, spread `1/18`.

This note proves the O(k⁴) tail is an orbit-flat-breaking / finite frame-section support structure,
and that its structural amplitude is lattice-intrinsic.

## 2. Inputs (one hop, fresh statuses on origin/main)

| Input | Role | Status |
|---|---|---|
| `δ²S_R = −½ Q_EH` at O(k²), isotropic | [SPLIT]/[WEIGHT] O(k²) covariant regime | [`CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH…2026-06-09`](CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md) — **retained_bounded** |
| on-shell O(k⁴) tail `α(n̂) = −(1+Σ n̂_a⁴)/12` | [DISP] | [`CUBIC_COXETER_REGGE_OK4_LATTICE_FINGERPRINT…2026-06-10`](CUBIC_COXETER_REGGE_OK4_LATTICE_FINGERPRINT_BOUNDED_THEOREM_NOTE_2026-06-10.md) — **retained_bounded** |
| isotropic complement energy is SO(3)-orbit-flat (the criterion) | [WEIGHT] | [`UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT…2026-05-10`](UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10.md) — **retained** |
| cubic O_h weight splits spin-2 as `E⊕T2` and breaks orbit-flatness | [WEIGHT] | recomputed self-contained here; not imported from PR #4285 |
| `Z³` adjacency `H = 6I − A` | [DISP] baseline finite lattice surface | [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — Lattice axiom baseline, not a bounded-status source |

No fitted parameters, no observed values, no GR/PDG comparator, no new axioms, numpy only.

## 3. The theorem (computed; runner blocks [DISP],[CRITSET],[WEIGHT],[SPLIT],[ESCAPE])

- **[DISP]** `α(axis) = −1/6`, `α(face) = −1/8`, `α(body) = −1/9`; spread `|α_axis − α_body| = 1/18`.
  Every value is fixed by the finite `H = 6I − A` lattice computation — a **structural** lattice
  amplitude, not a GR/PDG match.
- **[CRITSET]** `f(n̂) = Σ_a n̂_a⁴` on `S²` has critical set: **6 axis maxima** (`f=1`), **8
  body-diagonal minima** (`f=1/3`), **12 face-diagonal saddles** (`f=1/2`) — 26 directions, the O_h
  crystal axes (Riemannian-Hessian signatures certified). Stationarity of the O(k⁴) frame energy is a
  **discrete** set, giving a finite crystal-frame **section candidate** on the flat lattice atlas.
- **[WEIGHT]** the O(k⁴) angular weight (the cubic axis 4-tensor, de-traced) splits spin-2 into
  `E(2) ⊕ T2(3)` and is recomputed self-contained here; the corresponding cubic-weighted complement
  energy is **not** SO(3)-orbit-flat
  (orbit-variation `> 0`; magnitude depends on the chosen mixing amplitude, not lattice-fixed), while
  the isotropic energy **is** (`1.2e-15`). The dispersion-direction anisotropy and the field-frame
  sectioning are the same `l=4` object.
- **[SPLIT]** no O(k²) angular anisotropy: EH-order covariance is preserved; the sectioning is
  **strictly O(k⁴)** — the leading lattice correction.
- **[ESCAPE]** the sectioning weight is carried at O(k⁴) (`k`-dependent ⇒ derivative-dependent), so it
  is **outside** the constant linear Casimir-projector class `CB(V)`. This is an internal scope
  statement about the finite runner's weight, not a discharge of the unaudited Casimir-class no-go.

## 4. What this contributes toward the frame-bundle blocker (flat atlas)

`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE` (currently not retained) names the missing
primitive as a covariant 3+1 polarization-frame/projector bundle *with a distinguished connection /
horizontal distribution that picks a canonical section* and a `Π_curv` splitting the Hessian before
localization. The O(k⁴) calculation here supplies only a **candidate discrete crystal-frame section**
on the flat lattice atlas: the crystal frame is the discrete orientation at which the anisotropy is
extremal/diagonal. This is a *section candidate*, not the connection, horizontal distribution,
curved-background transplant, or `Π_curv` splitting the blocker asks for. Combined with the O(k²)
covariance (retained EH + the flat-atlas covariance note), the picture is covariant at EH and
frame-sectioning strictly at O(k⁴); whether the O(k⁴) section is a physical preferred frame or a
regulator artifact is left open.

## 4bis. Cross-sector corroboration (not a conflict): the same dim-6 l=4 Lorentz-violation object

The O(k⁴) anisotropy has the same dimension-6, `l=4` cubic-harmonic shape that appears on the
framework's emergent-Lorentz surfaces. The retained
`EMERGENT_LORENTZ_INVARIANCE_NOTE` (**retained_bounded**, "(Conditional)") is "isotropic at leading
order" with a "leading `O(a²p⁴)` dimension-6 anisotropic correction / `l=4` cubic-harmonic angular
signature"; `EMERGENT_LORENTZ_RADIATIVE_STABILITY…B4` (**retained**) forbids only the marginal
(dim-4 / O(k²)) anisotropy, leaving the dim-6 residual; and `LORENTZ_VIOLATION_DERIVED_NOTE` +
`LORENTZ_VIOLATION_ANGULAR_FINGERPRINT…` (**retained_bounded**) state the violation is dim-6,
parity-even, `l=4` cubic-harmonic. The angular functional `Σ_a n̂_a⁴` here carries exactly that
pattern — `[100]:[111] = 3:1` (runner [LV]). This is consistency/corroboration context, not an added
empirical constraint and not an all-orders Lorentz claim. The IR (O(k²)) covariance is preserved; the
sectioning is strictly the dim-6 correction.

## 5. The import-bound on the matching value: removed for the structural amplitude

Two values must stay separate:
- **(A) the lattice-intrinsic anisotropy amplitude** — `−1/12`, the per-direction `α` values, spread
  `1/18`, and the finite cubic-weight split — is fixed by the `H = 6I − A` lattice computation plus
  finite representation arithmetic, fit-free, **no GR/PDG comparator**. This note states that
  structural amplitude as the value the lattice calculation produces.
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
only the structural finite sectioning support, its lattice-fixed amplitude, and the derivative-order
separation from constant projector classes.
