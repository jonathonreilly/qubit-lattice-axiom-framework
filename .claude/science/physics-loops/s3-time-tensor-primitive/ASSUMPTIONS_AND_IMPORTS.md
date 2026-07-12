# Assumptions, explicit conditions, and imports

## Canonical `A_min`

The repository's minimal axiom set is exactly Lattice + Qubit + Admissibility
+ Record.  This block uses only the Lattice axiom's nearest-neighbor cubic
adjacency as background structure.  Qubit, Admissibility, and Record do not
supply the finite metric/readout computation.  No approved framework primitive
and no admission class is used.

## Explicit non-satisfying theorem-domain conditions

The bounded claim fixes, rather than derives, all of the following: `15^3`
Dirichlet box; center-plus-six-arm support; unit-charge scalar segment; `R=4`
exterior projector; `(3,3,0)` anisotropic functional; cubic interpolation with
`order=3`, `mode=nearest`, `prefilter=True`; static conformal metric; coordinate
step `h=1/25`; three probe coordinates; maximum-absolute trace-free Einstein
readout; and the helper replay's `PAD=12` spline emulation.  These conditions
bound the theorem.  They do not chain-satisfy a physical or continuum claim.

Forbidden proof inputs remain: reported endpoint targets, fitted source
families, observed gravity values, literature values, or an asserted physical
tensor interpretation.

| Item | Role | Class | Load-bearing? | Disposition |
|---|---|---|---|---|
| Cubic adjacency | Defines finite Laplacian | axiom background | yes | supplied Lattice structure |
| Finite box/boundary/support | Defines operator | explicit condition | yes | theorem-domain restriction |
| Metric/interpolation/probes/readout | Defines response functional | explicit condition | yes | theorem-domain restriction; no physical bridge claimed |
| Adapted basis and stabilizer | Selects fixed tangents | zero-input algebra on fixed support | yes | derived/checkable |
| `delta_A1` coordinate | Parametrizes scalar segment | exact finite algebra | yes | derived by `H(delta_center/6)=e0-s_unit` |
| Reduced-shell normalization | Normalizes response | computed lattice output | yes | computed with total-charge check |
| Endpoint/midpoint coefficients | Main values | computed lattice output | yes | source-step-free replay, helper-hash pinned |
| Endpoint secant residual | Bounded comparison | computed lattice output | yes | eleven-point bound only |
| Exact algebraic non-affinity | Stronger negative | open | no | explicitly not claimed without enclosure |
| Physical interpolator/tensor bridge | Physical meaning | open semantic bridge | no | excluded from bounded theorem |
| Observation/literature/fit | None | forbidden | no | absent |

## Counterfactual pass

- Replacing cubic with local linear interpolation removes the observed
  scalar-segment tail at the checked stencil; therefore interpolation choice is
  load-bearing and kept explicit.
- Changing size, boundary, coordinate step, probes, metric, or readout defines
  a different theorem object; no portability claim is made.
- Changing the max-absolute envelope can change the active branch; the branch
  is enumerated only on the declared grid.
- Removing the shell functional changes normalization; the runner computes the
  exact fixed functional rather than importing its decimal value.
