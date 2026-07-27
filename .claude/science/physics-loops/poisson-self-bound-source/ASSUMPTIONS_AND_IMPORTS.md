# Assumptions and Imports — poisson-self-bound-source (cycle 713)

## Import ledger

| # | Item | Role | Retired here? |
|---|---|---|---|
| I1 | Dirichlet nearest-neighbour graph Laplacian `A` on the `N^3` interior (diagonal `-6`, off-diagonal `+1`), taken from `F.build_laplacian_sparse` in the parent runner | Construction shared with the parent note, so the comparison is on the parent's own surface | No — deliberately inherited so the result speaks to the parent row |
| I2 | Operator family `{poisson, biharmonic, screened, local}` | The parent note's own tested family | No — inherited |
| I3 | Hopping amplitude `t = 1` in `H = -t A + V` | Sets the kinetic scale against which the self-attraction competes; only the dimensionless ratio `g/t` is physical, and `t` is scaled out of every reported statement | No — an explicit convention, stated |
| I4 | Coupling `g` | Free parameter, scanned; no value is fitted to an observed target | Not applicable |
| I5 | Screening mass `mu^2 = 0.25` | The parent runner's own screened-Poisson sweep value | No — inherited |
| I6 | Lowest eigenpair via `eigsh(..., which='SA')` | Numerical method | Not applicable |

No observed physical value, fitted selector, literature constant, or empirical
comparator enters any claim. No probability, readout, occurrence, or update rule
is used. No new axiom and no new framework primitive is introduced or required.

## Primitive-registry check

Per `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`: the construction
uses the supplied lattice structure and a linear operator on it. It does not
invoke the scale-reference primitive (no absolute scale is set — `g/t` is
dimensionless and scanned), the kinetic-isotropy primitive (no `c_t`/`c_s`
comparison is made), or the realized-state primitive (no record content is
read out). Nothing in this cycle needs a registry entry.

## Counterfactual pass over implicit choices

| Choice | What if it is wrong | Direction opened | Handled |
|---|---|---|---|
| Dirichlet boundary | A torus removes the wall entirely | The biharmonic depth divergence could be a wall artifact rather than a kernel property | Row R7 repeats the depth test with the zero mode removed on a torus |
| Single particle | Many fermions add Pauli pressure | A second stabilizing mechanism could mask the kernel's role | Deliberately excluded; recorded as a named untested route, and the landed frozen-stars note already occupies the fermionic case |
| Source sign chosen per operator | The parent runner used one fixed negative source for operators of opposite definiteness | Precisely the defect the parent row's re-audit note names | Fixed by construction and stated in row R0 |
| `V = phi` with no self-interaction subtraction | A one-body self-energy is included | The single-particle self-energy is the whole point of the Schrodinger-Newton shape, not an error, but it does mean `g` is not a two-body coupling | Stated as a scope limit, not corrected |
| Zero initial potential `V = 0` | Another initial iterate could select a different fixed point | Multiple self-consistent branches | Found real for `local`, which is bistable; reported in row R8 rather than hidden |
