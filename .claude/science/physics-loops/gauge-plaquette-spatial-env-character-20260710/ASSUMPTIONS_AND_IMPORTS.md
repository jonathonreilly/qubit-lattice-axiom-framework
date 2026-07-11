# Assumptions and imports

## Minimal allowed premises

`A_min` is exactly the current Lattice + Qubit + Admissibility + Record axiom
surface in `MINIMAL_AXIOMS_2026-06-29.md`. It supplies the cubic `Z^3`
substrate but no gauge action, measure, state selector, or plaquette value.

The primitive registry was checked at
`docs/audit/data/axiom_premise_nodes.json`. None of the scale-reference,
kinetic-isotropy, or realized-state primitives supplies or is needed for the
environment coefficients. In particular, no registered primitive supplies a
measure or weighting rule.

## Import ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Cubic periodic `L_s=3` spatial lattice | finite environment geometry | framework baseline plus named finite target surface | minimal axioms; contraction-cost note | yes | yes | none inside this target; state scope exactly | allowed scoped geometry |
| `SU(3)` link variables and Wilson real-positive measure | defines the environment integral | bounded Wilson action-surface premise | Wilson action-surface selector and real-positive premise bridge | yes | yes | upstream audit/retirement, not hidden here | explicit bounded premise |
| `beta=6` | evaluation point | admitted normalization on the Wilson surface | Wilson action-surface selector | yes | yes for numerical data | upstream canonical-normalization derivation | explicit bounded premise |
| Product normalized Haar measure | integration measure on links | standard compact-group mathematical machinery | Wilson lattice integral | yes | yes | theorem definition / exact quadrature identity | allowed standard mathematics |
| Peter-Weyl/Schur orthogonality | turns boundary density into convolution eigenvalues | standard mathematical theorem | existing formal convolution theorem | yes | yes | prove in note and check runner conventions | allowed standard mathematics |
| Full Wilson-ensemble Monte Carlo | evaluates the derived expectation identity | computed lattice input | new runner/log | yes for quoted numbers; no for the exact identity | multi-chain diagnostics and independent control surfaces | pending computation |
| `0.5934` canonical plaquette | tempting comparison | observational/computed comparator | publication tables | forbidden | no | none | excluded from derivation and pass gates |
| single-link `c_(p,q)/(d c_00)` packet | local factor / control only | retained bounded support | existing bounded coefficient note | forbidden as environment data | no | compare only as a falsifier | excluded as proof input |
| generic positive `rho` sequence | former witness | unsupported import for physical environment | old runner history | forbidden | no | replace by derived estimator | retired route |

## Forbidden imports

- the canonical plaquette number or any fit to it;
- the single-link coefficient packet as if it were the 80-plaquette environment;
- an assumed equality between residual eigenvalues and boundary coefficients;
- orbit-quotient tying as an exact original-graph integral;
- a chosen Perron boundary vector, word-chain surrogate, or fitted selector;
- a new axiom, primitive, probability rule, or typicality claim.

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| Coefficients require boundary-conditioned integrations at many `W` | Integrate the boundary Fourier mode before conditioning | delete the marked local Boltzmann factor in the full Wilson ensemble | one-ensemble estimator for every low irrep | live | 3 |
| The residual/kernel equality must be inserted after computing `rho` | Derive both from the same disintegrated path integral | conditional-density plus Peter-Weyl proof | removes symbol-identification step | live | 3 |
| Exact dense tensor contraction is the only honest computation | A statistically certified finite-volume integral is an independent computed input | multiple seeded Wilson chains plus controls | produces actual-environment data, though not exact arithmetic | live, bounded ceiling | 2 |
| Stabilizer orbit quotient is exact | Independent links cannot be tied | representation blocks on the original state space | possible exact route, substantial engineering | live but deferred | 1 |
| `L_s=3` periodic geometry is framework-forced | It is a scoped finite target rather than a theorem of `A_min` | state geometry in claim scope | prevents false zero-input status | forced narrowing | 2 |

The top live routes are the marked-factor deletion identity, the common-integral
operator proof, and the multi-chain actual-environment computation.
