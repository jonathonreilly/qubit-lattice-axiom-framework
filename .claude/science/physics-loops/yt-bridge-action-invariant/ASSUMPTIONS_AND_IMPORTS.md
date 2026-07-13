# Assumptions and imports

## First-principles reset

`A_min` is the current Lattice, Qubit, Admissibility, and Record surface in
`docs/MINIMAL_AXIOMS_2026-06-29.md`, plus no unlisted primitive.

Forbidden proof inputs:

- observed or accepted `y_t(v)`;
- fitted endpoint selectors or retention cuts;
- hard-coded plaquette, electroweak, QCD, or Planck values;
- the logistic/erf/smoothstep bridge families;
- the accepted-branch affine-kernel fit;
- a source/action, RG, time, or scale bridge not derived on the current
  surface.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Lattice/Qubit/Admissibility/Record | Current framework premise set | zero-input structural | `docs/MINIMAL_AXIOMS_2026-06-29.md` | Yes for the nonselection theorem | Yes | Already canonical | Allowed |
| Nonnegative surplus density `q` on an interval | Abstract variable in the response theorem | theorem-local definition | This block | Yes | Yes | Defined, not imported | Allowed |
| Endpoint derivative kernel `K_(s,q)` | Abstract response datum | theorem-local hypothesis | This block | Yes only for the support lemma | No for the no-go | Derive from a retained exact interacting bridge | Explicit hypothesis |
| Affine or `C^2` regularity of a supplied kernel | Moment-compression premise | theorem-local hypothesis | This block | Yes only for the support lemma | No for the no-go | Derive a kernel regularity bound from the exact operator | Explicit hypothesis |
| Exact interacting bridge/source-action map | Physical identification of the continuum surplus and endpoint | unsupported import on `A_min` | No retained authority found | No for the narrow no-go; yes for physical YT closure | No for no-go | New same-surface theorem | Open physical blocker, outside claimed no-go |
| `I_2 = interval-average of q` | Zeroth moment definition once `q` exists | framework-derived only after a bridge is supplied | Target note | Yes | Yes | Derive the physical `q` identification | Conditional definition |
| UV centroid `c_2` | First normalized moment once `q` exists | framework-derived only after a bridge is supplied | Target note | Yes | Yes | Derive the physical `q` and its selected solution | Conditional definition |
| `y_t(v)=0.9176` | Old comparator/row selector | observational comparator | Old scan | No in new theorem | No | Remove from proof core | Excluded |
| One-loop SM-like reference transport | Old definition of reference trajectory | standard correction / unsupported physical bridge | Old scan | No in new theorem | No | Remove from proof core; future retained bridge needed for physical reuse | Excluded |
| Constructive profile families and scan cuts | Old finite-family evidence | fitted input / support-only | Old runner | No in new theorem | No | Preserve only as historical motivation | Excluded |

## Nature-grade conclusion

The moment algebra can be exact without phenomenological inputs. The exact
counterfamily needs no physical import. Physical YT closure still requires a
theorem supplying the microscopic operator, observable map, and finite-response
bound; that live route is not ruled out here.

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| The physical surplus is a nonnegative density | The bridge correction changes sign | Signed measure with Jordan decomposition | Breaks rearrangement and requires separate positive/negative response bounds | live future operator test | 2 |
| One common affine kernel controls finite endpoint differences | The derivative kernel depends on profile amplitude | Path-averaged kernel `Kbar_q` from the exact fundamental-theorem identity | Exposes the required nonlinear-response uniformity theorem | executed in support lemma | 3 |
| Generic locality and strict convexity select a unique profile | Selector coefficients remain free | Exact `S_kappa` coefficient family | Produces the route-specific nonselection no-go | executed | 3 |
| The scale chain is the physical bridge geometry | The actual coarse object is operator-valued on `Z^3` | Gauge-covariant Schur/adjoint operator derived from the finite partition | Could defeat this narrow no-go by adding real microscopic structure | live highest-blast-radius residual | 3 |
| The observed endpoint may choose the selector | The endpoint is only a comparator | Remove the target and derive the operator first | Prevents fit-as-derivation | target-fit route falsified | 0 |
| A new primitive supplies the action | The premise registry is enlarged | Proposed source/action primitive | Forbidden by the no-new-primitive rule | infeasible | 0 |

The two highest-scoring live successor directions are the profile-dependent
path-kernel bound and the gauge-covariant microscopic operator construction.
The former is isolated explicitly; the latter remains the next hard residual.
