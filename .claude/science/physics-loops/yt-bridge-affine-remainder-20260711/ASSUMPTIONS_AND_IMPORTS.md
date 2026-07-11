# Assumptions and imports

## First-principles reset

[`A_min`](../../../../docs/MINIMAL_AXIOMS_2026-06-29.md) supplies Lattice,
Qubit, Admissibility, and Record. Its own qualification and dynamics sections
state that it supplies no dynamics, RG equation, source/action bridge, Yukawa
readout, physical boundary value, bridge profile, or affine local-Hessian
identification. None of those objects is used as an `A_min` consequence here.

The theorem in this block therefore starts from an explicitly stated scalar
transport equation and proves a mathematical consequence of that equation. It
does not claim the equation follows from `A_min`.

Forbidden proof inputs are observed or target `y_t`, PDG/SM boundary values,
the plaquette number, a fitted center/width, a selected profile family, or the
historical `x>=0.95` window.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---:|---:|---|---|
| `c,d,e>0`, `G,q in C(I)`, `y_0>0`, and `G+eq>=0` for convexity | theorem hypotheses | explicit stated mathematical premises | theorem statement | yes | yes | none; universally quantified hypotheses | closed on the stated surface; support-only for physical YT reuse |
| variation of constants | endpoint derivative | exact calculus | in-note proof and primary runner | yes | yes | direct derivation | closed |
| continuous `L2` affine projection | definition of best affine model | exact functional analysis | in-note proof and primary runner | yes | yes | normal equations | closed |
| Cauchy-Schwarz/Riesz equality witness | exact residual functional norm | exact functional analysis | in-note proof and primary runner | yes | yes | explicit witness `R/||R||` | closed |
| interpolation curvature bound | uniform remainder control | exact calculus | in-note proof and primary runner | yes | yes | chord remainder plus exact integral | closed |
| `M_Pl` scale label/conversion | diagnostic units conversion | registered scale-reference primitive; no dimensionless content | diagnostic companion constant and primitive registry | no | no | none for units role | disclosed, non-load-bearing and not a bounded-status source |
| `M_Z`, `alpha_EM(M_Z)`, and `sin^2(theta_W)(M_Z)` | diagnostic boundary data | observational comparator / admitted boundary data | diagnostic companion constants | no | no | keep outside claim surface | disclosed, non-load-bearing |
| plaquette `0.5934`, APBC `7/8` factor, and derived `V` identification | diagnostic framework/package calibration | computed-lattice plus support-only modeling input | diagnostic companion constants | no | no | keep outside claim surface | disclosed, non-load-bearing |
| one-loop beta coefficients and SM-like transport equation | diagnostic evolution model | standard correction / support-only model | diagnostic companion ODEs | no | no | keep outside claim surface | disclosed, non-load-bearing |
| logistic background, center `0.975`, width `0.020`, and `x>=0.95` cutoff | diagnostic selector/profile inputs | fitted/support-only | diagnostic companion | no | no | keep outside claim surface | disclosed, non-load-bearing |
| connected-trace factor `sqrt(8/9)` and boundary identifications | diagnostic normalization/readout inputs | support-only physical bridge | diagnostic companion | no | no | derive separate physical bridge | disclosed, non-load-bearing |
| `y_t(v)` target or viability filter | historical selector | fitted/observational comparator | prior runner history | no | no | remove from proof path | retired from this claim |
| exact lattice action -> scalar transport equation | physical reuse bridge | unsupported import | absent | no for theorem; yes for physical interpretation | no for bounded theorem | derive an operator/source bridge | separate open physical-reuse target |
| identification of affine residual as physical nonlocality | semantic bridge | unsupported import | absent | no | no | derive a locality-resolved operator decomposition | excluded from claim |
