# The Polarization-Frame Ambiguity Is a Basis Artifact: a Canonical Irreducible-Channel Graviton Section With Linearized-Einstein Signs

**Date:** 2026-06-17
**Type:** positive_theorem — narrow_theorem (two computed results) — advances the polarization-frame open gate
**Claim type:** positive_theorem — narrow_theorem

**Claim scope (narrow):** Two machine-precision results on the universal-GR polarization
sector. **(1)** The polarization-frame open gate of
[`UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE`](UNIVERSAL_GR_POLARIZATION_FRAME_BUNDLE_BLOCKER_NOTE.md)
(`frame_delta = 6.767e-2`, reproduced) is a **within-channel basis artifact**: the canonical
irreducible-channel **projectors** are frame-independent (`||P_c^canon − P_c^rot|| ≈ 1e-16`),
the four 3+1/SO(3) channels are mutually orthogonal on an isotropic background, and the
5-dim spatial spin-2 channel is **SO(3)-irreducible** (the canonical graviton channel) —
matching the Regge atlas's multiplicity-free `1+4+5`. So a canonical *point-wise* polarization
section exists. **(2)** The emergent channel **sign structure matches linearized Einstein**:
the validated linearized Einstein operator (gauge-invariant to 1e-16) has TT eigenmodes with
`μ_TT = −½·p² > 0` (the exact TT ½ coefficient) and a conformal mode with `μ_conf < 0`
(opposite sign — the conformal-factor structure); the emergent Regge channels reproduce this
pattern (`h_five(5) = +9.96`, `h_uniform(1) = −5.18`). This note proposes **no** status change
and edits no other note. **Status authority: independent audit lane only.**

## 1. Result (1): the frame ambiguity is a basis artifact; the channel section is canonical

The gate measures `frame_delta` by projecting a test perturbation onto the *individual basis
vectors* of a polarization frame, then comparing the canonical frame to a π/6-rotated one. The
rotation only mixes basis vectors *within* the irreducible 5-dim spin-2 channel, so the
*coefficients* are frame-dependent (`6.767e-2`) but the **channel projector** is not. Computed
(runner blocks `STEP 0/1/2`):

- `frame_delta_BASIS = 6.767361e-2` — the gate's value, reproduced exactly.
- `||P_c^canonical − P_c^rotated|| ≈ 1e-16` for every channel (`tt`, `ts`, `s-trace`, `s2`), on
  both the anisotropic test background and the isotropic physical one ⇒ `frame_delta_CHANNEL ≈ 1e-16`.
- On the isotropic background the four channels are mutually `B`-orthogonal (0.0), and the 5-dim
  `s2` channel is SO(3)-irreducible (orbit rank 5) — the canonical graviton channel, consistent
  with the round-S³ Regge multiplicity-free decomposition `10 = 1+4+5`.

**The point-wise polarization section is canonical.** The gate's residual obstruction is thereby
relocated precisely: it is **not** the point-wise frame, but the polarization-frame **bundle
*connection*** (transport across spacetime points) plus the **5→2 transverse-traceless reduction**
(which requires a propagation direction `k`).

## 2. Result (2): the emergent channel signs match linearized Einstein

The linearized Einstein tensor `G_lin` is built and **validated by gauge invariance**
(`max|G_lin(p⊗ξ + ξ⊗p)| = 1.8e-16`). Read off-shell (`p² = −1.53`):

- TT polarizations `h_+`, `h_×` are **exact eigenmodes** with `μ_TT = +0.765 = −½·p²` — the
  exact transverse-traceless **½ coefficient**, positive stiffness, 2 polarizations.
- The conformal mode `h = φ·η` has `μ_conf = −1.15` — opposite sign (the conformal-factor mode).
- **Opposite signs** = the linearized-Einstein channel structure.

The emergent Regge channels (`h_five(5) = +9.96` physical, `h_uniform(1) = −5.18` conformal)
reproduce this **sign pattern** (physical-positive / conformal-negative).

## 3. Honest scope and residual

- The **sign pattern** matches; the **magnitudes** do not — the coarse 5-vertex round-S³ complex
  is not expected to reproduce continuum eigenvalues, and the round-S³ → flat-graviton map is a
  **continuum-limit gap**. So Result (2) is Einstein-sign *consistency* of the emergent channels,
  not the flat graviton dispersion.
- **Not closed by this note:** the bundle connection across points; the 5→2 TT reduction; the
  flat graviton dispersion via the induced fermion determinant; and the **Einstein–Hilbert
  normalization / G_Newton magnitude** with the reflection-positivity source-sign for `G > 0`
  (which ties to the unaudited metric-DOF posit). These remain the gravity program's deeper
  residual.

Combined with the program's existing bounded results (positive isotropic TT spin-2 stiffness;
diffeomorphism-Ward identities to quintic order), these two results complete the *polarization
sector* of the emergent-graviton picture: a **canonical, frame-independent, SO(3)-irreducible
spin-2 graviton channel with linearized-Einstein sign structure**, from `{qubit, Z³, Record}`
via the induced determinant — with the residual obstruction precisely located at the
connection / TT reduction / G_Newton.

**Runner:** [`scripts/frontier_universal_gr_canonical_channel_section_and_einstein_signs_2026_06_17.py`](../scripts/frontier_universal_gr_canonical_channel_section_and_einstein_signs_2026_06_17.py)
(deterministic, no RNG load-bearing; `frame_delta_CHANNEL ≈ 1e-16`, gauge-invariance `1.8e-16`,
`μ_TT = −½p²`, sign-pattern match). No fitted parameters, no observed values, no axiom-file
edits, no `docs/audit/data/*` edits. Sets no audit status.
