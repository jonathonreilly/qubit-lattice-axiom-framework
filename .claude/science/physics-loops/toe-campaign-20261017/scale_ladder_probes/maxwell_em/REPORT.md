# Scale-ladder probe: finite-spin EM response and conditional Maxwell dynamics

Provenance: a fresh-context agent of the same model family; not an independent
reviewer. It read origin/main fa841753c1 and the scorecard. Process note: it ran
`git checkout origin/main` once by mistake and restored the branch immediately.
No docs were edited.

## Lane 1: finite-spin EM response (#7966 / W37)

- **O1a, which source is probed. Resolved by the ladder.**
  - Probe 1 rebuilt the 864-state L=2 component. It reproduces the note's χ values exactly (0.285050028242 and 0.105121402155).
  - The full 24×24 source Hessian vanishes on the 14-dimensional space of exact 2-forms (|R·d1| ≤ 2e-15).
  - It is rank one at every nonzero q, with a single transverse value K_T(q).
  - The occupation-sign curvature equals exactly K_T(π,π,π)/3. The 1/3 is the transverse fraction for k ∝ (1,1,1), and follows from gauge invariance and cubic symmetry.
  - So the historical .0756 is one third of the zone-corner stiffness, a lattice-scale quantity. The physical target is lim_{q→0} K_T(q).
  - At L=2, K(Q)/K(0) is 1.106 to 1.356 across the V values tested. So L=2 says nothing about the infrared.
- **O1b, flux-sector target. Reframed.**
  - Ring moves conserve the electric winding sectors exactly (a 1-form symmetry), so their energies need no source convention.
  - The Coulomb phase predicts L·ΔE(W) → const·W², with twist energy 2π²K m²/L. The confined phase predicts ΔE ∝ L.
  - The probe asks for χ_L and K_T(2π/L) to have the same limit.
- **O1c, production health. No help.**
- **O1d, infrared limit. Partly reframed.** The cubic EFT ansatz is K_T(q) = K + O(a²q²). Near RK, c² → 0, so the q² residual is expected there.
- **O1e, time and readout. No help.**

## Lane 2: conditional Maxwell dynamics (#7984/#7980)

- **Items 4/5, covariance and curl. Reframed and partly resolved.**
  - The kernel is B(q² − qqᵀ).
  - Anisotropy is irrelevant: speed spread/q² = 0.0278 = 1/36. The improved-curl variant gives 0.0279.
- **Item 3, locality.** Radius 3 and radius 1 cannot be told apart in the infrared. For the Maxwell target, "radius one" can be replaced by "analytic (quasi-local) symbol". This removes an obligation; it does not derive locality.
- **Item 6, conservation. No help, and the ladder sharpens it.**
  - The damped law has gap 0.3.
  - The overdamped law has a diffusive root λ ≈ −q²/γ, which is more relevant than the Maxwell term.
  - A coarse-graining channel produces dissipation; conservation needs a Hamiltonian.
- **Item 2, time rule. No help.**
- **Items 1/7, payload and coin. Reframed as an infrared branch count.**
  - The vertex+cube member has longitudinal branches with speeds 2 and 3.
  - The onsite-phase coin is gapped at q=0 (3/7) and gapless on the sphere |q| = 0.432; matching excludes it.
  - The K⊗C coin gives two photon doublets with speeds 0.618 and 1.618. This is a consistent infrared theory, so only "one light cone" excludes it.

## Cross-lane links

- **Gauss law across scales.** The block sum of Gauss operators equals the boundary flux (lattice Stokes), so the 1-form symmetry survives coarse-graining exactly.
- **Smallest photon generator.** Two-site generators freeze the field (09-24 note). The smallest generator that moves it is a four-link ring, so the photon generator lives at the neighbourhood scale.
- **The momentum Q = (π,π,π)** appears both as the field-convention sign and as the corner-fermion valley separation. Hypothesis, untested: the #7946 checkerboard source couples to inter-valley bilinears.
- **Gauge group.** The Z2 π-flux of the electron lane does not supply a U(1) Gauss law.
- **Charge quantization.** The full-flux-quantum endpoint identity is the lattice counterpart of Dirac quantization.

## Proposed probes, not run

- **P2.** K_T(2π/L) against χ_L for L = 4 to 8.
- **P3.** Winding-sector energies ΔE(W=1)/ΔE(0) against L.
- **P5.** The thermal coefficient Σ 1/c³ across polarizations.
- **P6.** The block Gauss identity under 2³ block maps.
