# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Finite-speed wavefield update rule | Defines the wavefield candidate compared against same-site memory | computed lattice input | `scripts/source_resolved_wavefield_escalation.py` | Yes | Needed for any mechanism reading beyond controls | Constructive theorem or exact derivation from retained framework | Open import; demoted out of closure language |
| Wavefield parameter envelope | Fixes `wave_lag_blend`, `wave_speed2`, damping, source blend, mix, mu, eps | computed lattice input | parent escalation runner | Yes | Needed for exact numerical scan | Sensitivity atlas or framework-native parameter derivation | Explicitly runner-selected |
| Zero-source reduction | Checks source-free consistency | computed lattice input | mechanism runner/log | Yes | Needed for bounded support | Existing exact runner check | Preserved |
| Source-depth phase-ramp scan | Evidence that ramp coefficient changes with source-detector depth | computed lattice input | mechanism runner/log | Yes | Needed for bounded support | Runner replay and cache | Preserved |
| Continuum causal-field interpretation | Physics interpretation beyond the exact-lattice family | unsupported import | none in this block | No for bounded support | Theorem or bridge lane | Excluded |
| Absolute experimental transfer | NV/experiment amplitude and unit bridge | unsupported import | downstream Diamond lane | No for bounded support | Separate calibration and detector theorem work | Excluded |
