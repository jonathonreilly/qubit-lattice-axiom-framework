# Assumptions and imports

The primitive-registry check was run against
`docs/audit/data/axiom_premise_nodes.json`. No approved primitive is load-bearing for
this finite-matrix claim, and no primitive is reclassified as an import or wall.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---:|---:|---|---|
| Finite staggered `M_KS[U]+mI` | common Grassmann measure | computed lattice input | primary runner | yes | yes | exact runner/log | computed directly |
| `Theta(chi)=-bar(chi)` and two-step block | reflection convention | literature theorem / explicit convention | cited OS/STW/Palumbo methodology | yes | yes | one-field sign falsifier | explicit and tested |
| `C_BLOCK=2` | temporal normalization | computed lattice input | same-`M` cross-block eigenvalues | yes | yes | same-matrix eigenvalue ratio | retired as an assumption |
| Hop eigenbasis `Q` | spatial-mode identification | computed lattice input | finite anti-Hermitian hop | yes | yes | eigensystem residual | computed directly |
| `NT_BULK=14`, open temporal ends | finite carrier boundary | admitted normalization | primary runner | yes, for listed carrier | yes | rerun other extents for wider claim | bounded to stated carrier |
| `m=0.5` | finite test parameter | admitted normalization | primary runner | yes, for listed carrier | yes | parameter-family theorem for wider scope | bounded to stated carrier |
| Finite U(1)/SU(3) samples | gauge averaging domain | admitted normalization | primary runner | yes | yes | exact/full Haar theorem for wider scope | finite sample/quadrature only |
| Positive determinant | positive gauge weight | retained support | `STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md` | yes | yes | already supplied upstream | consumed narrowly |
| Continuum/Wightman/Lorentz reconstruction | outside claim | support-only | none | no | no | separate lane | excluded |

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| The determinant may use a shorter temporal matrix | The weighted measure would not be the correlator's Gaussian measure | use `slogdet` of the exact `Lt=28` matrix inverted for the minor | directly closes the audit obstruction | live, selected | 3 |
| A reduced `Tr[V^dag GVG]` expansion is a direct four-field computation | It omits the Wick determinant and disconnected subtraction | evaluate the raw `2 x 2` covariance minor before comparison | directly closes the audit obstruction | live, selected | 3 |
| Spectrum matching is enough | Degenerate eigenspaces could conceal a wrong field identification | construct two temporal isometries mode-by-mode and test intertwining | checks eigenvectors and normalization | live, selected | 3 |
| The meson sign itself fixes the reflection convention | Two reflected fields cancel a global sign | test the one-field physical cross-kernel spectrum | removes misleading rhetoric | live, selected | 2 |
| `NT_BULK=14` represents every temporal carrier | Boundary corrections can differ at other extents | enumerate `nt` and prove a uniform family statement | widens scope but is not needed here | live future route | 1 |

The selected three score-3 counterfactuals are implemented together in the direct
same-matrix route.
